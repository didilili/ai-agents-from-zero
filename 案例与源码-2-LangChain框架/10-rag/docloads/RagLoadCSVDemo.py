"""
【案例】用 CSVLoader 加载 CSV 为 Document 列表

对应教程章节：第 19 章 - RAG 检索增强生成 → 2、RAG 文本处理核心知识

知识点速览：
- CSVLoader 按行加载，每行可转成一个 Document。
- 不指定列时：整行（所有列）会拼成一条字符串作为 page_content，metadata 通常只有 source，检索时整行一起被向量化。
- 指定 `content_columns` + `metadata_columns` 时：只有指定列作为正文（page_content），其余列进 metadata；这正好对应了 RAG 里 `Document.page_content` 与 `Document.metadata` 的分工。
- 检索时只对正文向量化，metadata 更适合拿来做过滤、来源展示和结果解释，因此结构化表格数据尤其适合这样拆分。
"""

# 获取当前脚本所在目录，拼接出绝对路径
from pathlib import Path

# pip install langchain_community
from langchain_community.document_loaders.csv_loader import CSVLoader

# 方式一：不指定列 → 整行（所有列）拼成一条字符串作为 page_content，metadata 通常只有 source 等

# ——file__: 表示获取脚本的绝对路径
csv_path = Path(__file__).parent / "assets" / "sample.csv"
docs_all = CSVLoader(file_path=csv_path).load()
print("=== 方式一：整行作为 page_content ===")
print(
    "page_content 示例:",
    (
        docs_all[0].page_content[:80] + "..."
        if len(docs_all[0].page_content) > 80
        else docs_all[0].page_content
    ),
)
print("metadata 示例:", docs_all[0].metadata, "\n")

# 方式二：指定 content_columns 与 metadata_columns → 正文只取 content 列，title/author 进 metadata，便于检索时按作者/标题过滤
docs_split = CSVLoader(
    file_path=csv_path,
    metadata_columns=["title", "author"],
    content_columns=["content"],
).load()
print("=== 方式二：content 列作为正文，title/author 进 metadata ===")
print("page_content 示例:", docs_split[0].page_content)
print("metadata 示例:", docs_split[0].metadata)


"""
【输出示例】
=== 方式一：整行作为 page_content ===
page_content 示例: id: 1
title: Introduction to Python
content: Python is a popular programming lan...
metadata 示例: {'source': 'assets/sample.csv', 'row': 0}

=== 方式二：content 列作为正文，title/author 进 metadata ===
page_content 示例: content: Python is a popular programming language.
metadata 示例: {'source': 'assets/sample.csv', 'row': 0, 'title': 'Introduction to Python', 'author': 'John Doe'}
"""
