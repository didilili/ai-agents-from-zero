"""
【案例】用 JSONLoader 加载 JSON 文件为 Document 列表

对应教程章节：第 19 章 - RAG 检索增强生成 → 2、RAG 文本处理核心知识

知识点速览：
- JSONLoader 通过 jq_schema 指定要提取的 JSON 路径（如 "." 表示整份、".key" 表示某字段）；text_content 控制是否把内容当作文本。
- `jq_schema="."` 表示把整份 JSON 当成一条内容读取，适合演示；真实 RAG 中通常会抽取更具体的字段或列表项，避免“一个 JSON 文件只变成一个很大的 Document”。
- 依赖 jq：pip install jq；若 JSON 较复杂可先查看文档确定 jq_schema 写法。
- 返回的每个 Document 对应一条被提取出的内容，便于后续向量化与检索。
"""

# pip install jq langchain_community
from langchain_community.document_loaders import JSONLoader
from pathlib import Path

docs_path = Path(__file__).parent / "assets" / "sample.json"
docs = JSONLoader(
    file_path=docs_path,
    jq_schema=".",  # 提取所有字段
    text_content=False,  # 是否按字符串处理内容
).load()

print(docs)

"""
【输出示例】
[Document(metadata={'source': '/Users/tools/Desktop/agent/ai-agents-from-zero/案例与源码-2-LangChain框架/10-rag/docloads/assets/sample.json', 'seq_num': 1}, page_content='{"status": "success", "data": {"page": 2, "per_page": 3, "total_pages": 5, "total_items": 14, "items": [{"id": 101, "title": "Understanding JSONLoader", "content": "This article explains how to parse API responses...", "author": {"id": "user_1", "name": "Alice"}, "created_at": "2023-10-05T08:12:33Z"}, {"id": 102, "title": "Advanced jq Schema Patterns", "content": "Learn to handle nested structures with...", "author": {"id": "user_2", "name": "Bob"}, "created_at": "2023-10-05T09:15:21Z"}, {"id": 103, "title": "LangChain Metadata Handling", "content": "Best practices for preserving metadata...", "author": {"id": "user_3", "name": "Charlie"}, "created_at": "2023-10-05T10:03:47Z"}]}}')]
"""
