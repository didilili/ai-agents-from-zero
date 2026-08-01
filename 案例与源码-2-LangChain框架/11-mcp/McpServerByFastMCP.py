"""
【案例】使用 FastMCP 官方库搭建 MCP 服务端（工具 / 资源 / 提示词）

对应教程章节：第 20 章 - MCP 模型上下文协议 → 6、案例实战：本地 MCP 天气服务与客户端

知识点速览：
- FastMCP 是 MCP 的 Python 官方实现之一，通过 @mcp.tool()、@mcp.resource()、@mcp.prompt() 暴露
  工具、静态资源和提示词模板，对应教程中「MCP 能做什么」这一节的三类核心能力。
- 从控制方式理解会更清楚：Tool 更偏 model-controlled，Resource 更偏 application-driven，
  Prompt 更偏 user-controlled；本案例的价值就是把这三类能力放在同一个最小服务端里看清楚。
- 本示例使用 transport=\"stdio\"，即通过标准输入/输出与客户端通信，最适合本地开发、命令行宿主、
  IDE 插件这类场景；如果你后面看到仓库里的 `sse` 写法，可以把它理解为网络化演示和兼容语境。
- 注意：直接在终端单独运行 stdio 服务时，没有 MCP 客户端接管 stdin/stdout，输入回车就可能触发
  Invalid JSON 这类报错；这不是 FastMCP 坏了，而是因为 stdio 服务本来就应该由宿主进程来启动。
"""

# pip install mcp
# uv pip install fastmcp
# pip install pywin32  # Windows 下部分功能需要
# from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP

# 创建 MCP 实例，对应「MCP 服务器」角色
mcp = FastMCP("Demo")


# 为 MCP 实例添加工具：最典型的“可执行动作”
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


# 为 MCP 实例添加资源：资源更像“可读取内容”，常由宿主决定是否拿来做上下文
@mcp.resource("greeting://default")
def get_greeting() -> str:
    return "Hello from static resource!"


# 为 MCP 实例添加提示词模板：更像“可复用的提示词入口”或工作流模板
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    styles = {
        "friendly": "写一句友善的问候",
        "formal": "写一句正式的问候",
        "casual": "写一句轻松的问候",
    }
    return f"为{name}{styles.get(style, styles['friendly'])}"


if __name__ == "__main__":
    # STDIO 模式：与主进程通过标准输入/输出通信，适合本地集成。
    # 注意：直接运行本脚本时，没有 MCP 客户端连接，stdin 收到终端输入（如回车）会被当 JSON 解析，
    # 导致 Invalid JSON / Internal Server Error，属预期现象。正确用法是由 Cursor/Claude 等 MCP 客户端
    # 启动本进程并接管 stdin/stdout；如果想做网络化示例，可看仓库里的 McpServerWeatherByFastMCP.py。
    mcp.run(transport="stdio")


"""
常见问题（保留供排查）：

方案 1：若出现 ModuleNotFoundError: No module named 'pywintypes'
- Windows 下部分依赖需要 pywin32，可尝试：pip install pywin32

方案 2：等待 pywin32 适配 Python 3.13（被动，无需改动环境）
- 若不想降级 Python 版本，可等待 pywin32 官方发布支持 Python 3.13 的版本；
  或使用本仓库中的 McpServer.py 极简实现（无 FastMCP，适配更多 Python 版本）。

方案 3：直接运行脚本报 Invalid JSON / Internal Server Error
- STDIO 模式需由 MCP 客户端（如 Cursor、Claude Desktop）启动本进程并接管 stdin/stdout；
  在终端单独运行时没有客户端发送 JSON-RPC，收到回车等会解析失败，属正常现象。
"""
