"""
【案例】对 Document 列表做分割：先加载再 split_documents

对应教程章节：第 19 章 - RAG 检索增强生成 → 2、RAG 文本处理核心知识

知识点速览：
- 实际 RAG 流程常是「加载器 load() → Document 列表 → 分割器 split_documents() → 更小的 Document 列表」。
- split_documents(documents)：直接对 Document 列表切分，每个 Document 的 page_content 会被按 chunk_size/chunk_overlap 切块，切出的块仍带 metadata（可继承或按实现保留）。
- 这类写法最贴近真实 RAG 项目，因为它既保留了 loader 产出的 metadata，又完成了后续向量化之前最关键的切块步骤。
- 本示例用 UnstructuredLoader 加载 rag.txt，再用 RecursiveCharacterTextSplitter 切分；需 pip install python-magic-bin（部分环境）。
- 为何用 split_documents 而不是 split_text？split_text(字符串) 入参是「一段文本」，返回字符串列表；这里入参是 Document 列表（来自 loader.load()），需要得到「带 metadata 的 Document 列表」供后续向量化/检索，只能用 split_documents。
"""

# pip install langchain-unstructured（部分环境加载本地文件还需 python-magic-bin）
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_unstructured import UnstructuredLoader
from pathlib import Path

txt_path = Path(__file__).parent / "rag.txt"
# 1. 加载文档得到 Document 列表
loader = UnstructuredLoader(txt_path)
documents = loader.load()

# 2. 同一套分割参数：块 100 字符，重叠 30
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=30, length_function=len
)

# 3. 直接对 Document 列表分割，返回更小的 Document 列表（不能改用 split_text：入参是 Document 列表，且需保留 metadata）
splitter_documents = text_splitter.split_documents(documents)

print(f"分割文档数量：{len(splitter_documents)}")
for splitter_document in splitter_documents:
    print(f"文档片段：{splitter_document.page_content}")
    print(
        f"文档片段大小：{len(splitter_document.page_content)}, 文档元数据：{splitter_document.metadata}"
    )

"""
【输出示例】
分割文档数量：14
文档片段：《倚天屠龙记》是金庸“射雕三部曲”的终章，以元末乱世为背景，谱写了一曲江湖侠义与家国情怀交织的传奇。
文档片段大小：50, 文档元数据：{'source': 'rag.txt', 'last_modified': '2026-03-10T10:36:41', 'languages': ['zho'], 'filename': 'rag.txt', 'filetype': 'text/plain', 'category': 'Title', 'element_id': '2089ea66f6635c149a4ea8fda049b579'}
文档片段：小说核心围绕张无忌的成长轨迹展开，他本是武当弟子张翠山与天鹰教殷素素之子，自幼身中玄冥神掌，历经磨难却得奇遇，
文档片段大小：55, 文档元数据：{'source': 'rag.txt', 'last_modified': '2026-03-10T10:36:41', 'languages': ['zho'], 'filename': 'rag.txt', 'filetype': 'text/plain', 'category': 'Title', 'element_id': '391f965ee98ac9ace2fac0a7c04ce062'}
……
"""
