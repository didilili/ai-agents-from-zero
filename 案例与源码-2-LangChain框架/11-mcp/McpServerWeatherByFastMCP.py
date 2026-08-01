"""
【案例】用 FastMCP 实现天气查询 MCP 服务（SSE + 指定 host/port）

对应教程章节：第 20 章 - MCP 模型上下文协议 → 6、案例实战：本地 MCP 天气服务与客户端

知识点速览：
- 这是一个“网络化 MCP Tool 服务”案例：它只暴露一个天气查询工具，用来配合同目录的 mcp.json
  和 McpClientAgent.py 演示“服务端独立启动 → 客户端连接 → Agent 调工具”这条完整链路。
- 与 McpServer.py 的关系：McpServer.py 是教学版极简服务端，这个文件才是更贴近真实 SDK 用法的
  FastMCP 写法；两者都在讲“服务端暴露工具”，只是抽象层级不同。
- 与 McpServerByFastMCP.py 的关系：后者重点在 Tools / Resources / Prompts 三类能力，这个文件则聚焦
  “一个真实工具如何通过网络方式暴露出去”。
- 本仓库保留 transport="sse" 的写法，是为了和 mcp.json、课程截图、网络化示例保持一致；如果从
  当前官方主线理解，初学者还要知道 stdio 和 HTTP/Streamable HTTP 才是更需要重点理解的传输方式。
- 正确写法：mcp = FastMCP("服务名")  →  mcp.run(transport="sse", host="127.0.0.1", port=8000)
- 错误写法：mcp = FastMCP("服务名", host="127.0.0.1", port=8000)  # FastMCP 构造函数不支持 host/port
"""

from typing import Any


import json
import os

# pip install mcp httpx python-dotenv
from dotenv import load_dotenv

# from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP

import httpx

load_dotenv()

# 构造函数只接受「服务名」；网络绑定信息在 run() 时再指定
mcp = FastMCP(
    "WeatherServerSSE"
)  # "WeatherServerSSE" 就是你自己起的名，可改成 "MyWeather" 等


@mcp.tool()
def get_weather(city: str) -> str:
    """查询指定城市的即时天气信息。city 为城市英文名，如 Beijing、Shanghai。"""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": os.getenv("OPENWEATHER_API_KEY"),
        "units": "metric",
        "lang": "zh_cn",
    }
    resp = httpx.get(url, params=params, timeout=10)
    data = resp.json()
    return json.dumps(data, ensure_ascii=False)


if __name__ == "__main__":
    # host、port 在 run() 时传入，不是构造函数。
    # 这里启动后，mcp.json 中的 weather 服务就可以按约定地址连到它。
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
