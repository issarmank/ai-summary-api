from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-5-mini",
    temperature=0.7
)

async def summarize_text(text: str) -> str:
    prompt = PromptTemplate(
        template="Summarize the following text:\n\n{text}\n\nSummary:",
        input_variables=["text"]
    )
    chain = prompt | llm
    result = await chain.ainvoke({"text": text})
    return result.content
