"""
【案例】用 PyPDFLoader 加载 PDF 为 Document 列表

对应教程章节：第 19 章 - RAG 检索增强生成 → 2、RAG 文本处理核心知识

知识点速览：
- PDF 需专用加载器；PyPDFLoader 支持本地路径或在线 URL，extraction_mode 可选 plain（纯文本）或 layout（按版面）。
- 每页通常对应一个 Document，metadata 中会带页码等信息，便于后续检索时定位来源。
- PDF 往往是文档解析里最麻烦的一类：同样是“能读出来”，不代表读出来的结构就一定适合直接做 RAG，因此很多项目里还会继续接切块、清洗，甚至更强的 PDF 解析工具。
- 若需更好排版与表格识别，可了解 Unstructured 等库的 PDF 加载器（见教程 2.2 常用加载器表）。
- 为何没 import pypdf 却要装 pypdf？PyPDFLoader 在 langchain_community 内部会「按需」import pypdf 来解析 PDF，langchain-community 不自动安装它，所以需单独 pip install pypdf。
"""

# pip install langchain_community pypdf
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

docs_path = Path(__file__).parent / "assets" / "sample.pdf"
docs = PyPDFLoader(
    file_path=docs_path,
    extraction_mode="plain",  # plain 纯文本；layout 按版面
).load()

print(docs)
"""
【输出示例】
[Document(metadata={'producer': 'Microsoft® Word 2019', 'creator': 'Microsoft® Word 2019', 'creationdate': '2023-07-24T17:46:07+08:00', 'title': '中国科学院国家天文台2023年度部门预算', 'author': 'MC SYSTEM', 'moddate': '2023-07-24T17:46:07+08:00', 'source': 'assets/sample.pdf', 'total_pages': 36, 'page': 0, 'page_label': '1'}, page_content='中国科学院国家天文台 \n2023 年部门预算'), Document(metadata={'producer': 'Microsoft® Word 2019', 'creator': 'Microsoft® Word 2019', 'creationdate': '2023-07-24T17:46:07+08:00', 'title': '中国科学院国家天文台2023年度部门预算', 'author': 'MC SYSTEM', 'moddate': '2023-07-24T17:46:07+08:00', 'source': 'assets/sample.pdf', 'total_pages': 36, 'page': 1, 'page_label': '2'}, page_content='目……
"""
