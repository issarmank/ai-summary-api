from fastapi import APIRouter, UploadFile, File
from app.services.pdf_reader import extract_text_from_pdf
from app.services.summarizer import summarize_text

router = APIRouter()

@router.post("/summarize-pdf")
async def summarize_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    text = extract_text_from_pdf(file.file)
    summary = await summarize_text(text)
    return {"summary": summary}