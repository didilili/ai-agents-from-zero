"""
【案例】RAG 综合流程：加载 docx → 分割 → 向量化存 Redis → 检索 → 提示词模板 → 大模型回答

对应教程章节：第 19 章 - RAG 检索增强生成 → 3.3 After：使用 RAG 的完整流程

知识点速览：
- 这是一个完整的管道式 RAG 案例：同一份脚本里同时包含了索引阶段（加载、切分、向量化、入库）和检索生成阶段（检索、拼 Prompt、调 LLM）。
- 本例展示的是文档流驱动的入库路线：先通过 Loader 和 Splitter 得到 `Document` 列表，再用 `Redis.from_documents(...)` 一步完成向量化与建索引。
- 流程：文档加载（Docx2txtLoader）→ 分割（CharacterTextSplitter）→ 向量化并写入 Redis（from_documents）→ `as_retriever()` 得到检索器 → 用 LCEL 把 retriever、prompt、llm 串成链（context + question → prompt → llm）→ `invoke(question)` 得到答案。
- `RunnablePassthrough()` 表示「把输入原样传给下一环节」；这里把用户问题同时传给 retriever（作为查询）和 prompt（作为 `{question}`）。
- 本例刻意保留了“有 RAG / 无 RAG”的对比，便于直观看到：RAG 的价值不只是“能回答”，而是“回答时是否真的用到了外挂知识库”。
- 运行前需启动 Redis、配置 aliQwen-api，且 alibaba-java.docx 在可访问路径（如本脚本同目录）。
"""

# pip install unstructured docx2txt python-docx
from langchain.chat_models import init_chat_model
import os
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.prompts import PromptTemplate
from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Redis
from dotenv import load_dotenv

load_dotenv()
from pathlib import Path

# 大模型：用于最终根据「检索到的上下文 + 用户问题」生成回答
llm = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("aliQwen-api"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 提示词模板：{context} 由检索器填充，{question} 由用户输入填充；最终会生成一段字符串 Prompt 再交给聊天模型
prompt_template = """
    请使用以下提供的文本内容来回答问题。仅使用提供的文本信息，
    如果文本中没有相关信息，请回答"抱歉，提供的文本中没有这个信息"。

    文本内容：
    {context}

    问题：{question}

    回答：
    "
"""
prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

# 嵌入模型：用于文档与查询的向量化
embeddings = DashScopeEmbeddings(
    model="text-embedding-v3", dashscope_api_key=os.getenv("aliQwen-api")
)

docs_path = Path(__file__).parent / "alibaba-java.docx"
# 1. 加载 docx（错误码文档）
loader = Docx2txtLoader(docs_path)
documents = loader.load()

# 2. 分割（此处用 CharacterTextSplitter 便于快速跑通；真实项目里更常见的通用首选是 RecursiveCharacterTextSplitter）
text_splitter = CharacterTextSplitter(
    chunk_size=1000, chunk_overlap=0, length_function=len
)
texts = text_splitter.split_documents(documents)

print(f"文档个数:{len(texts)}")

# 3. 向量化并写入 Redis，建立索引（必须用分割后的 texts，否则整篇文档作为一块）
vector_store = Redis.from_documents(
    documents=texts,
    embedding=embeddings,
    redis_url="redis://localhost:26379",
    index_name="my_index3",
)

# 4. 检索器：按相似度取前 k 条作为 context
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 5. LCEL 链：输入 question → context 由 retriever 查得，question 直通 → 拼 prompt → 调 llm
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

# 6. 提问并打印答案（有 RAG：从知识库检索）；未接输出解析器时，聊天模型返回的是 AIMessage，正文通常通过 .content 读取
question = "00000和A0001分别是什么意思"
result = rag_chain.invoke(question)
print("\n=== 有外挂知识库（RAG：从 alibaba-java.docx 检索）===")
print("问题:", question)
print("回答:", result.content)

# 7. 对比演示：同一问题但「无外挂知识库」（context 为空，不查向量库，模拟未挂载文档）
no_rag_chain = (
    {
        "context": lambda _: "（未提供相关文档，模拟无外挂知识库）",
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
)
result_no_rag = no_rag_chain.invoke(question)
print("\n=== 无外挂知识库（模拟：不检索，仅靠模型自身知识）===")
print("问题:", question)
print("回答:", result_no_rag.content)

"""
【输出示例】
文档个数:1
"""

# === 有外挂知识库（RAG：从 alibaba-java.docx 检索）===
# 问题: 00000和A0001分别是什么意思
# 回答: 00000 的意思是“一切 ok”，表示正确执行后的返回；
# A0001 的意思是“用户端错误”，属于一级宏观错误码。

# === 无外挂知识库（模拟：不检索，仅靠模型自身知识）===
# 问题: 00000和A0001分别是什么意思
# 回答: 抱歉，提供的文本中没有这个信息
