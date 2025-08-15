from fastapi import FastAPI
from app.routes import text

app = FastAPI(title="AI Summarizer API")

app.include_router(text.router)
