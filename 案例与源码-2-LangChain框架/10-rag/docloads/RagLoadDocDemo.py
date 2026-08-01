"""
【案例】用 UnstructuredWordDocumentLoader 加载 Word（.docx）为 Document 列表

对应教程章节：第 19 章 - RAG 检索增强生成 → 2、RAG 文本处理核心知识

知识点速览：
- .docx 需专用加载器；UnstructuredWordDocumentLoader 的 mode 可选 single（整篇一个 Document）或 elements（按标题等元素切分）。
- Word 文档虽然本质上是机器可读的结构化文件，但现实里标题样式和段落样式常常不够规范，所以“视觉上像标题”不一定能被稳定识别。
- 为何要装 unstructured？UnstructuredWordDocumentLoader 内部会按需 import unstructured 解析 .docx，langchain-community 不自动安装，需单独 pip install unstructured（若只加载 docx 可装 unstructured[docx]）。
- `single` 更适合快速看整篇内容；`elements` 更适合理解“按结构拆成多个 Document”的效果。加载后得到 `List[Document]`，与 TXT/PDF 等一致，可统一走「分割 → 向量化 → 入库」流程。
"""

# pip install langchain_community unstructured[docx] python-docx
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from pathlib import Path

docs_path = Path(__file__).parent / "assets" / "alibaba-more.docx"
docs = UnstructuredWordDocumentLoader(
    file_path=docs_path,
    mode="single",  # single 整篇一个 Document；elements 按元素切分
).load()

print(docs)
"""
【输出示例】
[Document(metadata={'source': 'assets/alibaba-more.docx'}, page_content='Java开发手册（黄山版）\n\nJava开发手册（黄山版）\n\n前言 \n\n《Java 开发手册》是阿里巴巴技术团队的集体智慧结晶和经验总结，经历了多次大规模一线实战的检验及不断完善，公开到业界后，众多社区开发者踊跃参与打磨完善，系统化地整理成册，当前的最新版本是黄山版。现代软件行业的高速发展对开发者的综合素质要求越来越高，因为不仅是编程知识点，其它维度的知识点也会影响到软件的最终交付质量。比如：五花八门的错误码会人为地增加排查问题的难度；数据库的表结构和索引设计缺陷带来的系统架构缺陷或性能风险；工程结构混乱导致后
"""
