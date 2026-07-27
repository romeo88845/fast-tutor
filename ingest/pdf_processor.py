#!/usr/bin/env python3
"""PDF to Fast-Tutor pipeline — extract text, chapters, images, auto-ingest."""
import os, re, json, tempfile, shutil
from pathlib import Path
import fitz  # pymupdf

STATIC_DIR = Path("/opt/fast-tutor/static/images")
STATIC_DIR.mkdir(parents=True, exist_ok=True)

def process_pdf(pdf_path: str, exam_code: str = "PDF-Content") -> dict:
    """Process a PDF and return Destillo-format markdown + image info."""
    doc = fitz.open(pdf_path)
    
    chapters = []
    segments = []
    key_points = []
    image_map = {}  # page_num -> [image_paths]
    
    current_chapter = "Introduction"
    current_segments = []
    all_text = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text").strip()
        
        if not text:
            continue
            
        # Extract images from page
        img_paths = _extract_page_images(doc, page, page_num)
        if img_paths:
            image_map[page_num] = img_paths
        
        # Detect chapter headings
        lines = text.split('\n')
        chapter_detected = False
        for line in lines:
            line_s = line.strip()
            # Detect common chapter patterns
            if re.match(r'^(Chapter|CHAPTER|Module|MODULE|Lesson|LESSON)\s+\d+', line_s):
                if current_segments:
                    _finalize_chapter(chapters, current_chapter, current_segments, all_text)
                current_chapter = line_s[:80]
                current_segments = []
                chapter_detected = True
                break
            # Detect markdown-style headings
            if re.match(r'^#{1,3}\s', line_s):
                if current_segments and len(current_segments) > 3:
                    _finalize_chapter(chapters, current_chapter, current_segments, all_text)
                current_chapter = re.sub(r'^#+\s*', '', line_s)[:80]
                current_segments = []
                chapter_detected = True
                break
        
        # Extract key points (bulleted lists)
        for line in lines:
            line_s = line.strip()
            if line_s.startswith('- ') or line_s.startswith('* ') or line_s.startswith('\u2022 '):
                point = re.sub(r'^[-*\u2022]\s*', '', line_s)
                if len(point) > 20 and point not in key_points:
                    key_points.append(point)
        
        # Add to segments
        time_label = f"{page_num // 60}:{page_num % 60:02d}"
        seg_text = text[:500]
        if img_paths:
            for ip in img_paths:
                seg_text += f"\n![Page {page_num + 1} diagram](images/{ip})"
        current_segments.append({"time": time_label, "text": seg_text})
        all_text.append(text)
    
    # Finalize last chapter
    if current_segments:
        _finalize_chapter(chapters, current_chapter, current_segments, all_text)
    
    page_count = len(doc)
    doc.close()
    
    # Limit key points
    key_points = key_points[:20]
    
    # Generate markdown
    md = _generate_markdown(pdf_path, chapters, key_points)
    
    return {
        "markdown": md,
        "chapters": len(chapters),
        "key_points": len(key_points),
        "images_extracted": sum(len(v) for v in image_map.values()),
        "pages": page_count
    }

def _extract_page_images(doc, page, page_num):
    """Extract images from a PDF page, save to static dir."""
    paths = []
    image_list = page.get_images(full=True)
    
    for img_idx, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        ext = base_image["ext"]
        
        filename = f"pdf-p{page_num + 1}-i{img_idx}.{ext}"
        filepath = STATIC_DIR / filename
        with open(filepath, "wb") as f:
            f.write(image_bytes)
        paths.append(filename)
    
    return paths

def _finalize_chapter(chapters, title, segments, all_text):
    """Add a chapter to the list."""
    desc = segments[0]["text"][:200] if segments else ""
    chapters.append({
        "time": segments[0]["time"] if segments else "0:00",
        "title": title[:100],
        "desc": desc,
        "segments": segments
    })

def _generate_markdown(pdf_path, chapters, key_points):
    """Generate Destillo-compatible markdown."""
    title = Path(pdf_path).stem.replace("_", " ").replace("-", " ").title()
    
    lines = ["---"]
    lines.append(f'title: "{title}"')
    lines.append(f"source: pdf")
    lines.append(f"processed: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"PDF processed into {len(chapters)} chapters with {len(key_points)} key points.")
    lines.append("")
    lines.append("## Key Points")
    for kp in key_points:
        lines.append(f"- {kp}")
    lines.append("")
    lines.append("## Chapters")
    for ch in chapters:
        lines.append(f"**{ch['time']} - {ch['title']}** - {ch['desc'][:100]}")
    lines.append("")
    lines.append("## Distilled Report")
    for ch in chapters:
        for seg in ch["segments"]:
            lines.append(f"[{seg['time']}] {seg['text']}")
    lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 pdf_processor.py <pdf_path> [exam_code]")
        sys.exit(1)
    pdf = sys.argv[1]
    code = sys.argv[2] if len(sys.argv) > 2 else "PDF-Content"
    result = process_pdf(pdf, code)
    print(json.dumps(result, indent=2))
    # Save markdown
    md_path = Path(pdf).with_suffix(".md")
    md_path.write_text(result["markdown"])
    print(f"\nMarkdown saved to {md_path}")
    print(f"Images saved to {STATIC_DIR}/")
