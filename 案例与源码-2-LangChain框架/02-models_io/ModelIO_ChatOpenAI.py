"""
【案例】使用 LangChain ChatOpenAI 调用大模型（OpenAI 兼容接口）

对应教程章节：第 11 章 - Model I/O 与模型接入 → 3、接入大模型

知识点速览：
- 本案例对应第 11 章中“OpenAI 兼容接口 + LangChain provider 类”这条接法。
- 通过 `ChatOpenAI + base_url` 可接入通义 / 阿里百炼等兼容接口，并继续与 Prompt、Parser、Chain、Agent、Memory 等组件配合。
- 与 `ModelIO_OpenAI.py` 的核心区别在于：这里返回的是 LangChain 语义下的 `AIMessage`，通常先用 `response.content` 取正文。
- 依赖 `langchain-openai`，运行前在 `.env` 中配置 API Key。
"""

# ========== 1. 导入与环境 ==========
from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

# ========== 2. 初始化聊天模型（OpenAI 兼容接口） ==========
# 这里选择 qwen-plus + 阿里百炼兼容端点，目的是演示“如何把兼容接口接进 LangChain 模型对象”。
chat_llm = ChatOpenAI(
    model="qwen-plus",  # 可按需更换，模型列表见阿里云文档
    api_key=os.getenv("aliQwen-api"),  # 或 os.getenv("QWEN_API_KEY")
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# ========== 3. 调用模型并打印回复 ==========
# 这里直接传入多角色消息列表，后续第 13 章会继续系统讲解 Message 体系。
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"},
]

response = chat_llm.invoke(messages)
# 返回值是 AIMessage；若你要看 token 用量、finish_reason、模型名等，可继续查看 response.response_metadata。
print(response.response_metadata)
print(response.content)
