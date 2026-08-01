"""
【案例】用 UnstructuredMarkdownLoader 加载 Markdown 为 Document 列表

对应教程章节：第 19 章 - RAG 检索增强生成 → 2、RAG 文本处理核心知识

知识点速览：
- Markdown 是一种典型的半结构化文本：天然带有标题、列表、段落等结构，因此很适合做知识库文档。
- Markdown 可用 UnstructuredMarkdownLoader；mode 为 elements 时会按标题、段落等元素拆成多个 Document，便于保留结构。
- 适合技术文档、README 等；后续分割时也可选用 MarkdownHeaderTextSplitter 按标题切分（见 2.3 文本分割器表）。
"""

# pip install langchain_community unstructured[md]
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from pathlib import Path

docs_path = Path(__file__).parent / "assets" / "sample.md"
docs = UnstructuredMarkdownLoader(
    file_path=docs_path,
    mode="elements",  # single 整篇；elements 按元素切分
).load()

print(docs)
"""
【输出示例】
[Document(metadata={'source': 'assets/sample.md', 'category_depth': 0, 'languages': ['ron'], 'file_directory': 'assets', 'filename': 'sample.md', 'filetype': 'text/markdown', 'last_modified': '2026-03-10T10:36:41', 'category': 'Title', 'element_id': 'e6a3b421f39f298fffbc3cf1b3b95817'}, page_content='投机解码（Speculative Decoding）介绍'), Document(metadata={'source': 'assets/sample.md', 'category_depth': 1, 'languages': ['kor'], 'file_directory': 'assets', 'filename': 'sample.md', 'filetype': 'text/markdown', 'last_modified': '2026-03-10T10:36:41', 'parent_id': 'e6a3b421f39f298fffbc3cf1b3b95817', 'category': 'Title', 'element_id': '3a77bcc407e48690734a4701557ffdb6'}, page_content='引言'), Document(metadata={'source': 'assets/sample.md', 'languages': ['nor', 'vie', 'zho'], 'file_directory': 'assets', 'filename': 'sample.md', 'filetype': 'text/markdown', 'last_modified': '2026-03-10T10:36:41', 'parent_id': '3a77bcc407e48690734a4701557ffdb6', 'category': 'UncategorizedText', 'element_id': '5a9685df7e44c7f338356ef37bc09149'}, page_content='投机解码（Speculative Decoding）是……
"""
