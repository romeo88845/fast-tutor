import concurrent.futures

"""Reformat extracted chapter content into proper lessons using LLM."""
import json, urllib.request, time, os
from pathlib import Path

API_URL = os.environ.get("OPENCODE_URL", "https://opencode.ai/zen/go/v1")
API_KEY = os.environ.get("OPENCODE_KEY", "") or open("/opt/fast-tutor/.opencode-key").read().strip()
MODEL = "deepseek-v4-flash"

def llm_reformat_chapter(title: str, raw_text: str, image_refs: list = None) -> dict:
    """Send chapter content to LLM and get structured lesson back."""
    imgs = image_refs or []
    img_section = "\n".join([f"- See diagram: {img}" for img in imgs[:5]]) if imgs else "No diagrams."
    
    prompt = f"""You are a technical instructor. Given this chapter from a technical book, create a well-structured lesson with 5 exam-style multiple choice questions.

Chapter Title: {title}

Raw Content:
{raw_text[:4000]}

Images in this chapter:
{img_section}

Output ONLY valid JSON with exactly these fields (generate exactly 5 questions and at least 10 key points):
{{
  "title": "Descriptive chapter title (not just Chapter N)",
  "explanation": "2-3 paragraph clear explanation of this topic, referencing any diagrams where relevant.",
  "key_points": ["Point 1", "Point 2", "Point 3", "Point 4", "Point 5", "Point 6", "Point 7", "Point 8","Point 9","Point 10"],
  "questions": [
    {{"stem": "MCQ question based on this chapter", "options": [{{"label": "A", "text": "option"}}, {{"label": "B", "text": "option"}}, {{"label": "C", "text": "option"}}, {{"label": "D", "text": "option"}}], "correct": "A", "explanation": "Why this answer is correct"}}
  ]
}}"""
    
    if not API_KEY:
        return _fallback(title, raw_text)
    
    try:
        data = json.dumps({
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 2000
        }).encode()
        req = urllib.request.Request(f"{API_URL}/chat/completions", data=data,
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}", "User-Agent": "Mozilla/5.0 (compatible; FastTutor/1.0)"},
            method="POST")
        resp = json.loads(urllib.request.urlopen(req, timeout=60).read())
        text = resp["choices"][0]["message"]["content"]
        # Extract JSON from response
        start = text.find("{")
        end = text.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end])
            except json.JSONDecodeError:
                # Try lenient parsing - fix common issues
                jtext = text[start:end]
                # Remove trailing commas before closing braces/brackets
                import re
                jtext = re.sub(r',\s*}', '}', jtext)
                jtext = re.sub(r',\s*]', ']', jtext)
                # Unescape single quotes (sometimes used instead of double)
                jtext = jtext.replace("'", '"')
                # Try again
                try:
                    return json.loads(jtext)
                except:
                    pass
    except Exception as e:
        print(f"  LLM error: {e}")
    
    return _fallback(title, raw_text)

def _clean_title(t):
    """Clean up a chapter title."""
    t = t.replace("CHAPTER ", "Chapter ").replace("_", " ").strip()
    import re
    t = re.sub(r"[#*]+", "", t)
    return t[:80]

def _fallback(title, raw_text):
    """Fallback if LLM unavailable."""
    import re
    lines = [l.strip() for l in raw_text.split("\n") if l.strip()]
    bullets = [l[2:] for l in lines if l.startswith("- ") or l.startswith("* ")]
    return {
        "title": _clean_title(title),
        "explanation": raw_text[:500] if raw_text else "No content.",
        "key_points": bullets[:5] if bullets else ["See chapter content"],
        "questions": [
            {"stem": f"True or False: This chapter covers {title[:50]}.",
             "options": [{"label": "A", "text": "True"}, {"label": "B", "text": "False"}],
             "correct": "A", "explanation": "Review the chapter content for details."}
        ]
    }

def batch_reformat(chapters: list, max_workers: int = 3) -> list:
    """Reformat multiple chapters in parallel."""
    results = [None] * len(chapters)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
        fut = {ex.submit(llm_reformat_chapter, c["title"], c.get("full_content", c.get("content", "")), c.get("images", [])): i for i, c in enumerate(chapters)}
        for f in concurrent.futures.as_completed(fut):
            idx = fut[f]
            try:
                results[idx] = f.result()
                print(f"  Chapter {idx+1}/{len(chapters)} done")
            except Exception as e:
                print(f"  Chapter {idx+1} failed: {e}")
                results[idx] = _fallback(chapters[idx]["title"], chapters[idx].get("full_content", ""))
    return results
