from fastapi import APIRouter
from pydantic import BaseModel
from app.services.summarizer import summarize_text

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/summarize-text")
async def summarize_text_endpoint(request: TextRequest):
    summary = await summarize_text(request.text)
    return {"summary": summary}
