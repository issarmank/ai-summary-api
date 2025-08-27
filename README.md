# AI Summarizer API

A FastAPI-based web service that provides AI-powered text summarization using OpenAI's GPT models through LangChain.

## Features

- **Text Summarization**: Summarize any plain text input
- **URL Content Summarization**: Fetch and summarize content from web pages
- **PDF Summarization**: Extract text from PDF files and generate summaries
- **Async Processing**: Built with async/await for optimal performance
- **Interactive Documentation**: Auto-generated API docs with Swagger UI
- **Error Handling**: Comprehensive error handling with meaningful responses

## Tech Stack

### Backend Framework
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running the FastAPI application

### AI & Language Processing
- **LangChain**: Framework for building applications with LLMs
- **OpenAI GPT**: Language model for text summarization
- **langchain-openai**: OpenAI integration for LangChain

### Text Processing & Extraction
- **PyPDF**: PDF text extraction
- **BeautifulSoup4**: HTML parsing and web scraping
- **httpx**: Async HTTP client for fetching web content

### Data Validation & Serialization
- **Pydantic**: Data validation and serialization
- **python-dotenv**: Environment variable management

### Development & Dependencies
- **Python 3.9+**: Core programming language
- **Virtual Environment**: Isolated dependency management

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- OpenAI API key

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ai-summary-api
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment setup
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the application
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.