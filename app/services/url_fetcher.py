import httpx
from bs4 import BeautifulSoup

async def fetch_url_content(url: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(str(url))  # Convert to string
            response.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Failed to fetch URL: {e}")

    try:
        soup = BeautifulSoup(response.text, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text(separator="\n", strip=True)
    except Exception as e:
        raise RuntimeError(f"Failed to parse HTML: {e}")
