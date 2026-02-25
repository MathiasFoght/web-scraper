from langchain_openai import ChatOpenAI


def analyze_model() -> ChatOpenAI:
    return ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000, max_retries=3)
