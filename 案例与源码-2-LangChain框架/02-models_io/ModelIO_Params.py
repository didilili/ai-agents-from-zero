"""
【案例】模型标准化参数：temperature、max_tokens 等

对应教程章节：第 11 章 - Model I/O 与模型接入 → 2.5 常用模型参数、2.6 Token、max_tokens 与计费的关系、2.9 调用后的返回信息

知识点速览：
- 这是一个“观察型案例”，重点不是业务功能，而是帮助你理解模型参数与返回对象结构。
- 演示 `temperature` 如何影响输出随机性，以及 `max_tokens` 与回复长度 / 成本控制的关系。
- 也适合配合第 11 章里关于 `AIMessage`、`response.content`、`response_metadata`、`usage_metadata` 的讲解一起看。
- 依赖 `langchain`、`langchain-openai`，运行前在 `.env` 中配置 `deepseek-api`。
"""

# ========== 1. 导入与环境 ==========
import os
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

# ========== 2. 实例化时设置常用参数 ==========
# temperature：控制输出随机性，0 更确定、高重复，越大越随机、越有创意。
# 通常取 0~2，源于 OpenAI API 约定；具体上下界以所用 API 文档为准。
# 超过 2（如 2.1）可能被部分接口拒绝或截断，且与 2.0 效果差异不大，建议不超过 2。
model = init_chat_model(
    model="deepseek-v4-flash",
    model_provider="openai",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com",
    temperature=0.1,  # 0～1，越高越随机；此处略高便于看到多次输出差异
    # max_tokens=256,  # 可选：限制单次回复长度
)

# 直接打印完整 response，便于观察 AIMessage 结构：
# - content：正文
# - response_metadata：厂商原始元数据
# - usage_metadata：统一整理后的 token 用量
print(model.invoke("写一句关于春天的词，14 字以内"))
# <class 'langchain_openai.chat_models.base.ChatOpenAI'>
print(type(model))
# <class 'str'>
print(type(model.invoke("写一句关于春天的词，14 字以内").content))
# <class 'langchain_core.messages.ai.AIMessage'>
print(type(model.invoke("写一句关于春天的词，14 字以内")))

# ========== 3. 多次调用观察参数效果（如 temperature 对多样性的影响） ==========
# 你可以把 temperature 改成 0、0.7、1.2 等再运行，对比回答是否更稳定、更多样。
for i in range(3):
    print(f"--- 第 {i + 1} 次 ---")
    print(model.invoke("写一句关于春天的诗词，14 字以内").content)


"""
【输出示例】温度为 2.0 时，输出如下结果
莺惊柳浪春犁响，一鞭云水碧
**诗家酥雨润，闲趁卖花声。**
寒威已退先春雨，万枝吐翠流云间。
"""

"""
【输出示例】温度为 0 时，输出如下结果
风软一溪云，花明两岸春。
风软一溪云，花明两岸春。
风软一溪云，花明两岸春。
"""
