"""Call MiniMax through LangChain's compatible chat model client."""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(encoding="utf-8")

model = ChatOpenAI(
    model="MiniMax-M3",
    api_key=os.getenv("MINIMAX_API_KEY"),
    base_url="https://api.minimax.io/v1",
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain LangChain in one sentence."},
]

response = model.invoke(messages)
print(response.content)
