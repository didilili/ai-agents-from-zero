"""
【案例】从 YAML 文件加载提示词模板

对应教程章节：第 13 章 - 提示词与消息模板 → 8、从文件加载提示词（JSON / YAML）

知识点速览：
- YAML 版本与 JSON 版本的使用方式完全一致，差别主要在于文件格式是否更适合人读和写注释。
- 本案例的 `prompt.yaml` 同样描述的是一个文本模板，因此加载后的使用方式仍然是 `.format(...)`。
- 和 JSON 版本一样，运行时要留意当前工作目录，避免相对路径找不到文件。
"""

import warnings

warnings.filterwarnings(
    "ignore", message="Core Pydantic V1 functionality isn't compatible with Python 3.14"
)

# 从 YAML 加载提示词模板，API 与 load_prompt("prompt.json") 一致
from langchain_core.prompts import load_prompt

template = load_prompt(
    r"案例与源码-2-LangChain框架\04-prompt\load_external\prompt.yaml", encoding="utf-8"
)
print(template.format(name="年轻人", what="滑稽"))
#

"""
【输出示例】
请年轻人讲一个滑稽的故事
"""
