#!/usr/bin/env python3
"""EPUB to Fast-Tutor pipeline — extract chapters, images, generate Destillo MD."""
import os, re, json, tempfile, shutil, html
from pathlib import Path
from datetime import datetime

import ebooklib
from ebooklib import epub
import html2text

STATIC_DIR = Path("/opt/fast-tutor/static/images")
STATIC_DIR.mkdir(parents=True, exist_ok=True)
H = html2text.HTML2Text()
H.ignore_links = False
H.ignore_images = False
H.body_width = 0

def process_epub(epub_path: str, exam_code: str = "EPUB-Content") -> dict:
    """Process an EPUB and return Destillo-format markdown + image info."""
    book = epub.read_epub(epub_path)
    
    title = _get_metadata(book, 'title') or Path(epub_path).stem.replace("_", " ").replace("-", " ").title()
    author = _get_metadata(book, 'creator') or ""
    
    chapters = []
    key_points = []
    total_images = 0
    image_idx = 0
    
    # Get TOC and document items
    doc_items = [item for item in book.get_items() if item.get_type() == ebooklib.ITEM_DOCUMENT]
    
    for doc in doc_items:
        content = doc.get_content()
        if not content:
            continue
        
        # Decode HTML
        html_content = content.decode('utf-8', errors='replace')
        
        # Extract chapter title from HTML
        ch_title = _extract_title(html_content, doc.get_name())
        
        # Convert to markdown
        md_text = H.handle(html_content)
        md_text = _clean_md(md_text)
        
        if not md_text.strip():
            continue
        
        # Extract key points (bulleted lines)
        for line in md_text.split('\n'):
            line_s = line.strip()
            if line_s.startswith('- ') or line_s.startswith('* '):
                point = re.sub(r'^[-*]\s*', '', line_s)
                if len(point) > 25 and point not in key_points:
                    key_points.append(point)
        
        # Extract inline images
        md_text, img_count = _extract_book_images(book, html_content, md_text, image_idx)
        image_idx += img_count
        total_images += img_count
        
        chapters.append({
            "title": ch_title or f"Chapter {len(chapters) + 1}",
            "content": md_text[:2000],  # Truncated for overview
            "full_content": md_text,
        })
    
    # Limit key points
    key_points = key_points[:25]
    
    # Generate markdown
    md = _generate_markdown(title, author, chapters, key_points)
    
    return {
        "markdown": md,
        "chapters": len(chapters),
        "key_points": len(key_points),
        "images_extracted": total_images
    }

def _get_metadata(book, key):
    """Get metadata from EPUB."""
    for item in book.get_metadata('DC', key):
        if item:
            return item[0]
    return None

def _extract_title(html_content, name):
    """Extract chapter title from HTML."""
    m = re.search(r'<h[1-3][^>]*>(.*?)</h[1-3]>', html_content, re.DOTALL | re.IGNORECASE)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()[:100]
    # Try TOC match
    m = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()[:100]
    return None

def _extract_book_images(book, html_content, md_text, start_idx):
    """Extract inline images from EPUB and reference them in markdown."""
    img_count = 0
    img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html_content, re.IGNORECASE)
    
    imported_images = {}
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_IMAGE:
            fname = os.path.basename(item.get_name())
            imported_images[fname] = item.get_content()
    
    for src in img_tags:
        fname = os.path.basename(src)
        img_data = imported_images.get(fname)
        if img_data:
            ext = os.path.splitext(fname)[1] or '.png'
            out_name = f"epub-img{start_idx + img_count}{ext}"
            out_path = STATIC_DIR / out_name
            with open(out_path, 'wb') as f:
                f.write(img_data)
            img_count += 1
    
    # Replace image references in markdown
    for i in range(img_count):
        out_name = f"epub-img{start_idx + i}.png"
        md_text = md_text.replace(f"![]({img_tags[i]})", f"![Chapter image](images/{out_name})") if i < len(img_tags) else md_text
    
    return md_text, img_count

def _clean_md(text):
    """Clean up markdown output."""
    # Remove excessive blank lines
    text = re.sub(r'\n{4,}', '\n\n', text)
    # Remove navigation artifacts
    text = re.sub(r'\[.*?\]\(.*?\)\s*', '', text)  # Remove empty links
    return text.strip()

def _generate_markdown(title, author, chapters, key_points):
    """Generate Destillo-compatible markdown."""
    lines = ["---"]
    lines.append(f'title: "{title}"')
    lines.append("source: epub")
    if author:
        lines.append(f"author: {author}")
    lines.append(f"processed: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"EPUB processed into {len(chapters)} chapters with {len(key_points)} key points.")
    lines.append("")
    lines.append("## Key Points")
    for kp in key_points:
        lines.append(f"- {kp}")
    lines.append("")
    lines.append("## Chapters")
    for i, ch in enumerate(chapters):
        tm = f"{i}:00"
        lines.append(f"**{tm} - {ch['title']}** - {ch['content'][:150]}")
    lines.append("")
    lines.append("## Distilled Report")
    for i, ch in enumerate(chapters):
        tm = f"{i}:00"
        lines.append(f"[{tm}] **{ch['title']}**")
        lines.append("")
        lines.append(ch['full_content'][:3000])
        lines.append("")
    lines.append("")
    return "\n".join(lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 epub_processor.py <epub_path> [exam_code]")
        sys.exit(1)
    epub_path = sys.argv[1]
    code = sys.argv[2] if len(sys.argv) > 2 else "EPUB-Content"
    result = process_epub(epub_path, code)
    print(json.dumps(result, indent=2))
    # Save markdown
    md_path = Path(epub_path).with_suffix(".md")
    md_path.write_text(result["markdown"])
    print(f"\nMarkdown saved to {md_path}")
    print(f"Images saved to {STATIC_DIR}/")
