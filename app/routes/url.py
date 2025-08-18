from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl
from app.services.url_fetcher import fetch_url_content
from app.services.summarizer import summarize_text

router = APIRouter()

class URLRequest(BaseModel):
    url: HttpUrl

@router.post("/summarize-url")
async def summarize_url(request: URLRequest):
    content = await fetch_url_content(request.url)
    summary = await summarize_text(content)
    return {"summary": summary}
