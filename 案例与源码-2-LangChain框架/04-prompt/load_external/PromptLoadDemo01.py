"""
【案例】从 JSON 文件加载提示词模板

对应教程章节：第 13 章 - 提示词与消息模板 → 8、从文件加载提示词（JSON / YAML）

知识点速览：
- 把 Prompt 放到 JSON / YAML 里，有助于版本管理、多人协作和 A/B 测试，也能避免长提示词把业务代码挤得很乱。
- `load_prompt(...)` 会根据文件内容加载出模板对象；对于本案例的 `_type: "prompt"`，它会得到一个 `PromptTemplate` 风格的对象。
- 运行这类案例时，要特别注意当前工作目录和相对路径，否则脚本可能找不到 `prompt.json`。
"""

# 从 langchain_core 引入 load_prompt，用于从 JSON/YAML 加载模板
from langchain_core.prompts import load_prompt

# 从当前目录（或指定路径）加载 prompt.json，得到与 PromptTemplate 用法相同的模板对象
# encoding="utf-8" 保证中文等字符正常显示
template = load_prompt(
    r"案例与源码-2-LangChain框架\04-prompt\load_external\prompt.json", encoding="utf-8"
)

# 用 .format() 填入占位符变量，得到最终字符串（与第 6 节 PromptTemplate.format 的使用方式一致）
print(template.format(name="张三", what="搞笑的"))

"""
【输出示例】
请张三讲一个搞笑的的故事
"""
