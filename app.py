import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException, Depends, Body, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

from database import init_db, engine
from models import Base
from routers.content import router as content_router
from routers.sessions import router as sessions_router
from routers.progress import router as progress_router
from database import get_db
from sqlalchemy.orm import Session as DBSession

BASE = Path(__file__).parent

app = FastAPI(title="Fast-Tutor", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Static files for images
static_dir = Path(__file__).parent / "static"
static_dir.mkdir(exist_ok=True)
(static_dir / "images").mkdir(exist_ok=True)

# Create tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(content_router)
app.include_router(sessions_router)
app.include_router(progress_router)

# Serve frontend
@app.get("/", response_class=HTMLResponse)
def index():
    tpl = BASE / "templates" / "index.html"
    if tpl.exists():
        return HTMLResponse(tpl.read_text(encoding="utf-8"))
    return "<h1>Fast-Tutor</h1><p>Frontend coming in Phase 4.</p>"

# Health


import tempfile, shutil
from ingest.pdf_processor import process_pdf
from ingest.destillo import ingest_destillo
from database import SessionLocal

@app.post("/api/ingest/pdf")
async def ingest_pdf(file: UploadFile = File(...), exam_code: str = "PDF-Content"):
    """Upload a PDF, extract content, ingest into Fast-Tutor."""
    if not file.filename.endswith(".pdf"):
        raise HTTPException(400, "Only PDF files accepted")
    
    # Save to temp
    tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    content_bytes = await file.read()
    tmp.write(content_bytes)
    tmp.close()
    
    try:
        # Process PDF
        result = process_pdf(tmp.name, exam_code)
        
        # Ingest into DB
        db = SessionLocal()
        try:
            ingest = ingest_destillo(tmp.name.replace(".pdf", ".md"), db, exam_code)
            db.commit()
        finally:
            db.close()
        
        # Clean up generated .md
        md_path = tmp.name.replace(".pdf", ".md")
        if os.path.exists(md_path):
            os.unlink(md_path)
        
        return {
            "status": "ok",
            "chapters": result["chapters"],
            "key_points": result["key_points"],
            "images_extracted": result["images_extracted"],
            "lessons_created": ingest.get("lessons_created", 0)
        }
    except Exception as e:
        raise HTTPException(500, f"PDF processing failed: {str(e)}")
    finally:
        os.unlink(tmp.name)

@app.post("/api/ingest")
def ingest_content(content: str = Body(""), exam_code: str = Body("MS-Intune"), db: DBSession = Depends(get_db)):
    """Ingest Destillo markdown content into Fast-Tutor."""
    import tempfile, os
    from ingest.destillo import ingest_destillo

    if not content.strip():
        raise HTTPException(400, "Empty content")
    
    # Write to temp file
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False)
    tmp.write(content)
    tmp.close()
    
    try:
        result = ingest_destillo(tmp.name, db, exam_code)
        return {"status": "ok", "result": result}
    except Exception as e:
        raise HTTPException(500, f"Ingestion failed: {str(e)}")
    finally:
        os.unlink(tmp.name)


@app.get("/api/health")
def health():
    return {"status": "ok", "app": "fast-tutor", "version": "1.0.0"}

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8411
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
