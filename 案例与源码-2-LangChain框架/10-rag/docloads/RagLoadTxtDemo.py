"""
【案例】用 TextLoader 加载纯文本（TXT）为 Document 列表

对应教程章节：第 19 章 - RAG 检索增强生成 → 2、RAG 文本处理核心知识

知识点速览：
- 文档加载器负责把各种格式的文件读成 LangChain 的 Document；每个 Document 有 page_content（正文）和 metadata（如 source 路径）。
- TextLoader 用于纯文本（.txt），需指定文件路径和编码（如 utf-8）；load() 返回 List[Document]，多行文本通常合并为一个 Document。
- TXT 是最容易入门的加载场景，但“能加载”不等于“适合直接检索”：真实 RAG 中通常仍要继续切块，再做向量化与入库。
- 后续可接文本分割器、嵌入模型与向量库，完成 RAG 的「加载 → 分割 → 向量化 → 存储」流程。
"""

# pip install langchain_community
from langchain_community.document_loaders import TextLoader
from pathlib import Path

file_path = Path(__file__).parent / "assets" / "sample.json"
encoding = "utf-8"

# load() 为 BaseLoader 统一接口，返回 List[Document]
docs = TextLoader(file_path, encoding).load()

print(docs)
"""
【输出示例】
[Document(metadata={'source': 'assets/sample.txt'}, page_content='LangChain 是一个用于构建基于大语言模型（LLM）应用的开发框架，旨在帮助开发者更高效地集成、管理和增强大语言模型的能力，构建端到端的应用程序。它提供了一套模块化工具和接口，支持从简单的文本生成到复杂的多步骤推理任务。')]
"""
