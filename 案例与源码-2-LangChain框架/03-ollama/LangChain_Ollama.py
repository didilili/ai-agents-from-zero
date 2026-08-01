"""
【案例】LangChain + Ollama 本地大模型对话

对应教程章节：第 12 章 - Ollama 本地部署与调用 → 5、LangChain 整合 Ollama 调用本地大模型

知识点速览：
- 本案例对应第 12 章里“把本地 Ollama 服务接进 LangChain”的最小落地示例。
- 使用 `ChatOllama` 连接本机模型，无需云端 API Key；前提是本机已安装并启动 Ollama，且已经拉取过目标模型。
- `base_url` 指向本机 Ollama 服务根地址（默认 `http://localhost:11434`），`model` 必须与 `ollama list` 里已存在的标签一致。
- `invoke()` 返回的仍然是 LangChain 语义下的 `AIMessage`，因此和第 11 章云端模型调用一样，正文通常用 `response.content` 读取。
"""

from langchain_ollama import ChatOllama

# ---------- 第一步：创建“聊天客户端” ----------
# ChatOllama 是 LangChain 中连接本地 Ollama 服务的聊天模型类。
# 你可以把它理解成“本地模型版本的 Chat Model 客户端”：
# - base_url：Ollama 服务根地址（本机默认 http://localhost:11434）
# - model：已通过 ollama pull / ollama run 拉取到本机的模型标签
# - reasoning：是否开启推理/思考模式（是否支持取决于具体模型）
model = ChatOllama(
    base_url="http://localhost:11434",
    model="qwen3.5:4b",
    reasoning=False,
)

# ---------- 第二步：发一条消息并打印回复 ----------
# invoke(问题) 会把输入发给本地模型，并返回一个 LangChain 的消息对象（通常是 AIMessage）。
# 直接 print(response) 适合观察完整对象结构；业务里若只关心正文，一般读取 response.content。
response = model.invoke("什么是LangChain，100字以内回答")
print(response)

"""
【可选】如果你只想看到模型回复的纯文字，可以这样取：
print(response.content)
"""
