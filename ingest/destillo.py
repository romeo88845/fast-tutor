"""Ingest Destillo-processed markdown into the Fast-Tutor DB."""
import re, json
from pathlib import Path
from sqlalchemy.orm import Session as DBSession

from models import Exam, Domain, Objective, Lesson, LessonSegment, Question, AnswerOption, QuestionType, Difficulty

def ingest_destillo(md_path: str, db: DBSession, exam_code: str = "MS-Intune") -> dict:
    """Parse a Destillo markdown file and seed the database."""
    md = Path(md_path).read_text("utf-8")
    
    # Parse frontmatter
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---", md, re.DOTALL)
    if m:
        for line in m.group(1).strip().split("\n"):
            kv = re.match(r"^(\w+):\s*(.*)", line)
            if kv: fm[kv.group(1)] = kv.group(2).strip('" ')
    
    title = fm.get("title", "Untitled")
    
    # Create exam
    exam = db.query(Exam).filter(Exam.code == exam_code).first()
    if not exam:
        exam = Exam(code=exam_code, name=title, vendor="Microsoft")
        db.add(exam)
        db.flush()
    
    # Parse sections
    def section(name):
        m = re.search(rf"^## {name}\s*$(.+?)(?=^## |\Z)", md, re.MULTILINE | re.DOTALL)
        return m.group(1).strip() if m else ""
    
    # Parse chapters → lessons
    chapters = []
    for line in section("Chapters").split("\n"):
        m = re.match(r"\*\*([\d:]+)\s*[–—\-]\s*(.+?)\*\*\s*[–—\-]\s*(.*)", line.strip())
        if m:
            chapters.append({"time": m.group(1).strip(), "title": m.group(2).strip(), "desc": m.group(3).strip()})
    
    # Parse segments
    segments = []
    cur_time, cur_text = "0:00", []
    for line in section("Distilled Report").split("\n"):
        m = re.match(r"\[([\d:]+)\]\s*(.*)", line.strip())
        if m:
            if cur_text: segments.append({"time": cur_time, "text": " ".join(cur_text)})
            cur_time, cur_text = m.group(1), [m.group(2)]
        else: cur_text.append(line.strip())
    if cur_text: segments.append({"time": cur_time, "text": " ".join(cur_text)})
    
    # Parse key points
    kp = [l[2:].strip() for l in section("Key Points").split("\n") if l.strip().startswith(("- ", "* "))]
    
    # Parse quotes
    quotes = [m.group(1).strip().strip('"') for m in re.finditer(r">\s*(.*?)(?=\n>|\n\n|\Z)", section("Notable Quotes"), re.DOTALL)]
    
    # Create domains + objectives
    domain_map = _ensure_domains(db, exam.id)
    
    # Create lessons from chapters
    lesson_count = 0
    seg_count = 0
    q_count = 0
    
    for i, ch in enumerate(chapters):
        # Assign to domain based on title keywords
        domain_key = _classify_chapter(ch["title"])
        domain = domain_map.get(domain_key, list(domain_map.values())[0])
        obj = domain["objectives"][0] if domain["objectives"] else None
        if not obj:
            continue
        
        lesson = Lesson(
            objective_id=obj.id,
            title=ch["title"],
            content_md=ch["desc"],
            source_type="video",
            source_ref=fm.get("url", ""),
            sort_order=i,
            estimated_min=5
        )
        db.add(lesson)
        db.flush()
        lesson_count += 1
        
        # Add segments for this chapter
        ch_sec = _ts_to_sec(ch["time"])
        next_ch_sec = _ts_to_sec(chapters[i+1]["time"]) if i+1 < len(chapters) else 999999
        for seg in segments:
            seg_sec = _ts_to_sec(seg["time"])
            if ch_sec <= seg_sec < next_ch_sec:
                db.add(LessonSegment(
                    lesson_id=lesson.id,
                    sort_order=0,
                    content_md=seg["text"],
                    time_start=seg["time"]
                ))
                seg_count += 1
        
        # Create question from key points
        if i < len(kp):
            kp_text = kp[i % len(kp)]
            q = Question(
                objective_id=obj.id,
                lesson_id=lesson.id,
                type=QuestionType.MCQ,
                stem=_kp_to_question(kp_text),
                explanation_md=kp_text,
                difficulty=Difficulty.FOUNDATION
            )
            db.add(q)
            db.flush()
            # Add True/False options
            db.add(AnswerOption(question_id=q.id, label="A", text="True", is_correct=True))
            db.add(AnswerOption(question_id=q.id, label="B", text="False", is_correct=False))
            q_count += 1
    
    db.commit()
    return {"lessons_created": lesson_count, "segments_imported": seg_count, "questions_created": q_count, "exam_id": exam.id}

def _ensure_domains(db, exam_id):
    """Create default domains + objectives for Intune content."""
    domains_data = [
        ("Intune Fundamentals", [
            "Understand MDM vs MAM and their use cases",
            "Explain the relationship between Compliance, Configuration, and CA"
        ]),
        ("Device Enrollment", [
            "Windows Autopilot deployment profiles",
            "iOS/macOS Automated Device Enrollment",
            "Android Enterprise enrollment modes"
        ]),
        ("Configuration & Compliance", [
            "Create and assign configuration profiles",
            "Create and assign compliance policies",
            "Configure Windows Update rings"
        ]),
        ("App Management", [
            "Deploy Win32 apps and LOB apps",
            "Configure MAM protection policies",
            "Volume Purchase Program (VPP) for iOS"
        ]),
        ("Security & Monitoring", [
            "Configure BitLocker and disk encryption",
            "Monitor device compliance and generate reports",
            "Implement Conditional Access with Intune compliance"
        ])
    ]
    
    result = {}
    for dname, objectives in domains_data:
        domain = db.query(Domain).filter(Domain.exam_id == exam_id, Domain.name == dname).first()
        if not domain:
            domain = Domain(exam_id=exam_id, name=dname, weight_pct=20.0)
            db.add(domain)
            db.flush()
        
        obj_list = []
        for i, desc in enumerate(objectives):
            obj = db.query(Objective).filter(
                Objective.domain_id == domain.id,
                Objective.description == desc
            ).first()
            if not obj:
                obj = Objective(domain_id=domain.id, code=f"{i+1}.0", description=desc)
                db.add(obj)
                db.flush()
            obj_list.append(obj)
        
        result[dname] = {"domain": domain, "objectives": obj_list}
    
    return result

def _classify_chapter(title: str) -> str:
    t = title.lower()
    if any(w in t for w in ["intro", "terminology", "what is", "key", "overview"]):
        return "Intune Fundamentals"
    if any(w in t for w in ["enroll", "autopilot", "ade", "byod"]):
        return "Device Enrollment"
    if any(w in t for w in ["configur", "compliance", "update", "restriction"]):
        return "Configuration & Compliance"
    if any(w in t for w in ["app", "deploy", "mam", "vpp"]):
        return "App Management"
    if any(w in t for w in ["security", "encrypt", "bitlocker", "monitor", "report", "endpoint"]):
        return "Security & Monitoring"
    return "Intune Fundamentals"

def _ts_to_sec(ts: str) -> int:
    p = ts.split(":")
    return int(p[0]) * 60 + int(p[1]) if len(p) >= 2 else 0

def _kp_to_question(kp: str) -> str:
    """Convert a key point to a True/False question."""
    return f"True or False: {kp}"
