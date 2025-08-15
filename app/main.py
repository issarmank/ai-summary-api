from fastapi import FastAPI
from app.routes import text, url, pdf

app = FastAPI(title="AI Summarizer API")

app.include_router(text.router)
app.include_router(pdf.router)
app.include_router(url.router)


