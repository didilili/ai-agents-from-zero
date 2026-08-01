"""
【案例】使用 ChatTongyi 原生集成调用阿里云百炼（通义千问）

对应教程章节：第 11 章 - Model I/O 与模型接入 → 3、接入大模型

知识点速览：
- 本案例对应第 11 章中“通义原生集成”路线，和 `ChatOpenAI` / `init_chat_model` 的兼容接口路线是并列关系。
- `ChatTongyi` 更贴近阿里云原生接法，不需要手动写 `base_url`；如果你更强调多模型统一风格，通常会优先学兼容接口写法。
- 这个案例同时演示了 `invoke()` 和 `stream()`，方便和第 10 章的流式输出、以及第 13 章的消息体系衔接起来看。
- 依赖 `langchain-community`、`dashscope`；若 `cffi` 报错可尝试 `pip install --upgrade --force-reinstall cffi`。运行前配置 `aliQwen-api`。
"""

# ========== 1. 导入与环境 ==========
import os
from langchain_community.chat_models.tongyi import (
    ChatTongyi,
)  # 注意ChatTongyi 将逐步 从langchain_community包中遗弃
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

# ========== 2. 初始化通义千问聊天模型 ==========
# 这里走的是阿里云原生集成，不是 OpenAI 兼容接口路线，因此不需要手动填写 base_url。
chat_llm = ChatTongyi(
    model="qwen-plus",
    api_key=os.getenv("aliQwen-api"),
    streaming=True,
)

# ========== 3. 调用方式一：invoke 一次性返回 ==========
print(chat_llm.invoke("你是谁").content)

print("*" * 60)

# ========== 4. 调用方式二：stream 流式返回 ==========
# 这里传入 HumanMessage，是为了和后续第 13 章里的“多角色消息”概念提前建立联系。
for chunk in chat_llm.stream([HumanMessage(content="你好，你是谁")], streaming=True):
    print(chunk.content, end="")
print()
