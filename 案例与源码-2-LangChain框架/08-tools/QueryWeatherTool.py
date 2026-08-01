"""
【案例】天气查询工具：用 @tool 定义可被 LLM 调用的天气接口，请求 OpenWeather API 并返回 JSON

对应教程章节：第 17 章 - Tools 工具调用 → 5、天气助手实战：把 Tool 跑成业务闭环 → 5.2 定义天气查询工具

知识点速览：
- 本例的重点不是天气业务本身，而是把“第三方 HTTP API”封装成一个可被模型理解和调用的 Tool。
- 工具 docstring 要尽量写清调用场景和关键参数规则；像 `loc` 需要英文城市名这种约束，最好直接写在工具说明里，而不是留给模型猜。
- 返回值这里使用 JSON 字符串，是为了方便后续链路继续处理；真实项目里也可以返回更稳定的结构化对象，但要注意和后续消费方式保持一致。
- 本例聚焦 Tool 封装本身，未展开重试、降级、异常兜底等工程细节；这些通常会在真实项目的 service / client 层补齐。
"""

from langchain_core.tools import tool
import json
import os
import httpx
from dotenv import load_dotenv

load_dotenv(encoding="utf-8")


# @tool 装饰器：函数名 get_weather 即工具名，下方 docstring 会成为模型理解工具的重要依据
@tool
def get_weather(loc: str) -> str:
    """
    查询指定城市的即时天气。

    参数:
        loc: 城市名称字符串。为了提高调用成功率，建议优先传英文城市名，
             如 Beijing、Shanghai。

    返回:
        OpenWeather 当前天气接口返回的 JSON 字符串，包含气温、体感温度、
        湿度、风速、天气描述等信息。
    """
    # Step 1. 构建请求 URL（OpenWeather 当前天气接口，见教程 5.2 API 文档）
    url = "https://api.openweathermap.org/data/2.5/weather"

    api_key = os.getenv("OPENWEATHER_API_KEY")
    print(
        f"读取到的 API Key: [{api_key}]"
    )  # 用中括号包起来，方便看出有没有多余的空格或引号

    # Step 2. 设置查询参数：q=城市名，appid 从环境变量读取（安全实践），units=metric 为摄氏度，lang=zh_cn 为中文描述
    params = {
        "q": loc,
        "appid": os.getenv(
            "OPENWEATHER_API_KEY"
        ),  # 从 .env 读取，勿将 Key 写死在代码中
        "units": "metric",  # 温度单位：metric=摄氏度
        "lang": "zh_cn",  # 天气描述语言：简体中文
    }

    # Step 3. 发送 GET 请求；httpx 与 requests 用法类似，timeout 避免长时间阻塞
    response = httpx.get(url, params=params, timeout=30)

    # Step 4. 解析响应为 Python 字典后，再序列化为 JSON 字符串返回，供后续链继续处理
    data = response.json()
    return json.dumps(data)


# 本地测试：单参数工具可直接传值；若和更通用的工具调用风格保持一致，也可传 {"loc": "..."}
# result = get_weather.invoke("shanghai")
result = get_weather.invoke("beijing")
print(result)

"""
【输出示例】
{"coord": {"lon": 116.3972, "lat": 39.9075}, "weather": [{"id": 800, "main": "Clear", "description": "\u6674", "icon": "01d"}], "base": "stations", "main": {"temp": 10.76, "feels_like": 8.26, "temp_min": 10.76, "temp_max": 10.76, "pressure": 1033, "humidity": 14, "sea_level": 1033, "grnd_level": 1027}, "visibility": 10000, "wind": {"speed": 1.6, "deg": 232, "gust": 2.63}, "clouds": {"all": 0}, "dt": 1773034935, "sys": {"country": "CN", "sunrise": 1773009388, "sunset": 1773051236}, "timezone": 28800, "id": 1816670, "name": "Beijing", "cod": 200}
"""
