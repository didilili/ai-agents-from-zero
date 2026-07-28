"""
【案例】使用 init_chat_model 统一入口调用大模型（1.0 推荐写法）

对应教程章节：第 11 章 - Model I/O 与模型接入 → 3、接入大模型

知识点速览：
- 本案例对应 LangChain 1.x 更推荐的“统一入口”思路：同一套初始化骨架可切换不同模型和 provider。
- 本例选择 `deepseek-v4-flash + base_url`，演示在“可推断 provider”的场景下，`init_chat_model` 可以写得更简洁。
- 但这不代表任何模型都能省略 `model_provider`；像 `qwen-plus` 这类模型名，真实项目里通常仍建议显式指定。
- `invoke()` 既可接单条字符串，也可接与 `ChatOpenAI` 相同格式的消息列表。
- 依赖 `langchain`、`langchain-openai`（或对应 provider 包），运行前配置 `.env`。
"""

# ========== 1. 导入与环境 ==========
import os
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

# ========== 2. 实例化模型（本例中可由 base_url 推断 provider） ==========
# 注意：这里能省略 model_provider，是因为本例刻意选择了更容易推断的 DeepSeek 兼容接口场景。
model = init_chat_model(
    model="deepseek-v4-flash",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com",
)

# ========== 3. 调用并取正文（两种写法均可） ==========
# 写法一：单条用户输入字符串（最简）
# 仅传 str 时，框架会当作一条 user/human 消息，无法在此形式下单独写 system；要 system 请用写法二或消息对象。
print(model.invoke("你是谁？").content)

# 写法二：与 ModelIO_ChatOpenAI.py 相同的多角色消息列表（system + user）
# 统一入口的优势主要体现在“初始化更统一”，返回值仍然是 AIMessage。
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"},
]
response = model.invoke(messages)
print(response.content)
print(response.response_metadata)
