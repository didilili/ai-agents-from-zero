<div align='center'>
  <img src="./images/banner-v8.png" alt="AI Agents Tutorial" width="950px">
  <h1 style="margin-top: 15px;">🚀 The Most Systematic Hands-On Guide to AI Agents (From Zero to Production)</h1>
  <h4><b>ai-agents-from-zero</b></h4>
  <p><em>Continuously updated in 2026 · Aiming to be the <b>best AI Agent tutorial on the planet</b> —— <b>systematic lessons + runnable source code + interview question bank + production-grade projects + a long-term evolving tech stack</b>, a one-stop learning path fully aligned with "AI Agent / LLM Application Developer" <b>training curricula</b> and <b>job descriptions</b></em></p>
</div>

<div align="center">

![AI](https://img.shields.io/badge/AI-Agent-00c853?style=flat)
![Language](https://img.shields.io/badge/language-English%20%7C%20Chinese-2ea44f?style=flat)
![Stars](https://img.shields.io/github/stars/didilili/ai-agents-from-zero?logo=github&style=flat)
[![GitHub](https://img.shields.io/badge/GitHub-Project-181717?logo=github&logoColor=white)](https://github.com/didilili/ai-agents-from-zero/)
[![Read Online](https://img.shields.io/badge/Read%20Online-Click%20to%20Visit-blue?logo=bookstack)](https://didilili.github.io/ai-agents-from-zero/#/)

[Quick Start](#quick-start) • [Outline](教程目录大纲.md) • [Case Index](教程案例链接汇总.md#教程案例链接汇总源码与在线演示) • [Changelog](教程更新日志.md) • [Interview Bank](AI智能体与大模型应用开发面试题库.md) • [Getting Started & FAQ](新手入门与常见问题.md)

  <p>
    <a href="https://didilili.github.io/ai-agents-from-zero/#/">📚 Read Online</a>
  </p>

</div>

> **📖 Language note**
> This is the English translation of the README. The tutorial itself is being translated chapter by chapter — the English chapters will live in the `en/` directory. See the [translation progress](#-translation-progress) section below.
> The Chinese original is the source of truth: **[中文版 README](./README.md)**.
> Translations are maintained by the community. Corrections and suggestions are very welcome — see [CONTRIBUTING.en.md](./CONTRIBUTING.en.md).

**📢 Update note**: **AI never stops, and neither do the updates.** This repository evolves together with the **LLM tech stack**, and stays **open source, systematic, and long-term maintained**. Models, frameworks, agents and hands-on projects will keep improving as the ecosystem changes. It is not just here to get you started — it is here to grow with you, from zero background to actually shipping things.

The **concepts section** is now fully published, and both complete hands-on projects are finished: the `NL2SQL + LangGraph` project [Shopkeeper Data Q&A](实战项目-电商问数/0-前言.md) ([source repo](https://github.com/didilili/shopkeeper-agent)) was completed on May 3. The `DeepAgents` multi-agent project [Deep Research](实战项目-深度研搜/0-前言.md) ([source repo](https://github.com/didilili/deepsearch-agents)) was completed on May 17. Check the [changelog](教程更新日志.md) for the latest repository news.

There is plenty of content about LLM applications out there, but most of it is fragmented posts or paid bootcamps. This repository exists so that you can get into LLM application development systematically without first spending thousands (or tens of thousands) of yuan. If it helps you, a **Star** ⭐ would be much appreciated~

---

## 🤝 Sponsorship

<table>
<tr>
<td width="220" align="center" valign="middle">
  <a href="https://passport.compshare.cn/register?referral_code=KyLCDhVe3j5E9o1XBWmIku&ytag=GPU_YY_YX_git_ai-agents-from-zero">
    <img src="./images/sponsor-compshare-agent-plan.jpg" alt="Compshare" width="160">
  </a>
  <br>
  <sub>Cost-effective Agent Plan</sub>
</td>
<td valign="middle">

Thanks to <a href="https://www.compshare.cn/coding-plan"><strong>Compshare</strong></a> for sponsoring this project! Compshare is an AI cloud platform under UCloud. It offers cost-effective monthly and pay-per-use Agent Plan packages for domestic models, starting from 49 CNY/month. It also provides officially proxied, stable overseas models, supports integration with Claude Code, Codex and API calls, and offers high-concurrency, 24/7 technical support and self-service invoicing for enterprises.

🎁 Users who register through <a href="https://passport.compshare.cn/register?referral_code=KyLCDhVe3j5E9o1XBWmIku&ytag=GPU_YY_YX_git_ai-agents-from-zero"><strong>this link</strong></a> get 5 CNY of free platform credit.

</td>
</tr>
</table>

---

## ✨ Highlights

- **🌱 The first systematically open-sourced AI Agent tutorial**: This is a long-term maintained roadmap for LLM application development. The world is not short of scattered posts or paid bootcamps, but truly systematic, continuously updated tutorials covering **lessons + source code + hands-on projects + an interview question bank** are rare. This repository aims to make that path public, deep and complete, walking with you from beginner to advanced to real projects.
- **🧭 One thread through the whole LLM application stack**: From large models and prompting, to low-code platforms (Coze/Dify) and code frameworks (LangChain/LangGraph), to production-grade RAG/Agents, fine-tuning and engineering conventions — all organized into a single coherent knowledge system. A **complete closed loop**, suited for actually mastering the material rather than bookmarking fragments.
- **🐍 Focused on the Python ecosystem, aimed straight at Agent engineering**: Many courses center on **Spring AI** or **langchain4j** and lean towards the Java stack. This tutorial's main line focuses on **Python + LangChain + LangGraph**, directly aligned with the engineering path most commonly used today for AI Agents and LLM applications.
- **📘 Accessible to beginners, deep enough for engineers**: The whole tutorial is organized progressively — first thoroughly explaining core concepts like LLMs, Agents, RAG, MCP and tool calling, then moving into source code, frameworks, deployment and project design. Less mystical jargon, more "why it is designed this way, how the code runs, how a project ships".
- **💼 Production-grade practice, benchmarked against "can actually do the job"**: Centered on projects like Shopkeeper Data Q&A, Deep Research, Shopkeeper Knowledge Base and E-commerce Assistant, it threads together intent parsing, multi-source knowledge, human handoff, retrospectives and monitoring — putting **multi-route retrieval, evaluation, observability, cost and guardrails** into real contexts. Something concrete for your résumé and for talking about your projects.
- **✅ Every case is held to the standard of "it actually runs"**: Not just concepts or pseudocode — runnable examples, source code, environment notes and troubleshooting are provided wherever possible. The materials are organized around what was actually run through by hand, to help you step on fewer landmines and get going faster.
- **📚 Tutorial, source code and interview prep in one**: Not just "read it" — you can "run it" and "answer it". **Runnable examples and source code**, prompt templates and deployment approaches; no "concepts only". The interview bank is broken down by the competency areas common in **training programs and job descriptions**, and a good portion of the questions are compiled from **real interviews at major tech companies**, public interview reports and frequently probed follow-up scenarios — well suited for career switchers and new graduates doing focused review.
- **🚀 Built for 2026, continuously evolving and hardcore**: The tech stack and the most frequently asked questions iterate along with the ecosystem, aligned with the dimensions of ten-thousand-yuan-level "AI Application Developer" training curricula. It does not just tell you "what to learn" — it tells you "how to build a project, how to present it, how to answer in an interview". If it helps, **a Star is the best tip ⭐**.

---

## 🛠 Tech Stack Overview

| Category                | Technologies / Platforms                    | Notes                                                                            |
| ----------------------- | ------------------------------------------- | -------------------------------------------------------------------------------- |
| **LLMs & Foundations**  | LLM, Transformer, MoE, self-attention       | LLaMA/Qwen/GPT, multimodal, pre-training/fine-tuning/inference                   |
| **Prompting & Orchestration** | Prompt engineering, Tool Calling, Skills | Multi-turn dialogue, message templates, structured output, tool calling, skill-based capability capture |
| **Low-code Platforms**  | Coze, Dify                                  | Workflows, agents, knowledge bases, plugins, Python invocation and local deployment |
| **Development Frameworks** | LangChain, LangGraph, DeepAgents         | Model I/O, Runnable / LCEL, Memory, Tools, Agents, graph-based workflows, multi-agent |
| **Protocols & Communication** | MCP (Model Context Protocol), A2A     | Function Calling, service decoupling, external tool integration, cross-agent collaboration |
| **RAG & Retrieval**     | Vector databases, sparse retrieval, hybrid retrieval, BGE-Rerank | Multi-route retrieval, reranking, knowledge graphs, RAGAS evaluation, advanced RAG optimization |
| **Documents & Multimodal** | MinerU, OCR                              | Mixed text-and-image PDF parsing, device manuals and after-sales guides          |
| **Deployment & Ops**    | Docker, Ollama, Xinference, vLLM             | Tencent Cloud/Alibaba Cloud, AutoDL, local Coze deployment                       |
| **Fine-tuning & Training** | PEFT, LoRA, QLoRA, DeepSpeed, Llama-Factory | Alpaca/ShareGPT data formats, Safetensors, keyword-based evaluation             |
| **Programming & Tools** | Python; Codex, Cursor                        | Main language is Python; covers AI coding tools, Agent Skills, multi-model APIs, MCP integration and debugging |
| **Career & Interviews** | Interview question bank                      | Organized by job competency area with **how it is asked + how to answer**; aligned with comparable **online training learning outcomes** and **high-frequency JD topics** |

---

## 🎯 What You Will Gain

- **Ship-ready project skills** — deliver AI Agent applications independently (from environment to deployment), leveling up from "I can only call an API" to engineering practice that actually ships.
- **Systematic architectural thinking** — articulate the design and trade-offs behind RAG, Agents, MCP and more, and hold up under follow-up questions in interviews and on your résumé.
- **Interview and JD alignment** — a standalone [interview question bank](AI智能体与大模型应用开发面试题库.md), cross-linked with the main text by question number, organized by job competency area with both question phrasings and answer approaches. Well suited to new graduates and career switchers consolidating their narrative.
- **Engineering and résumé material** — production-oriented cases and formulations around multi-route retrieval, observability and cost. Projects you can demo and write up.
- **A searchable knowledge map** — a structured table of contents plus case source code, aligned with the dimensions of common "Agent / application development" curricula, making it easy to fill gaps and avoid the trap of "I only read articles, never ran anything".
- **Clear job targeting** — qualifies you for roles such as AI Application Developer, AI Agent Engineer, AI Automation Workflow Developer and technical lead for AI products. Especially suited to people from frontend / backend / product backgrounds transitioning into AI and agent development.

---

## 📚 Tutorial Outline (Excerpt)

The full navigation is in **[Tutorial Outline](教程目录大纲.md)** and the [online docs](https://didilili.github.io/ai-agents-from-zero/#/).

> This outline is not fixed. It will keep evolving with the AI tech stack — new core concepts, new frameworks and new project practices will be folded into this path.

### 01 Foundations of Large Language Models

| Chapter                                    | Content Summary                                                              |
| ------------------------------------------ | ---------------------------------------------------------------------------- |
| Understanding LLMs and environment setup   | Origins and evolution, relationship to AGI, characteristics and use cases of mainstream models, pre-training/fine-tuning/inference |
| LLM architecture principles                | Transformer, MoE, self-attention, LLaMA/Qwen/GPT, multimodal                 |
| LLM serving platforms                      | Ollama, private LLM invocation, cloud/local deployment (AWS, Alibaba Cloud, etc.) |
| Prompt engineering                         | Core principles and structure, chain-of-thought and few-shot, multi-turn dialogue and memory, application in agents and tool calling |

### 02 Enterprise Low-code Platforms and Project Practice

| Chapter                        | Content Summary                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| Coze platform                  | UI and features, plugins / knowledge bases / workflows / agents, calling workflows from Python |
| Project 1: Merchant Operations Assistant | Industry research decks, viral video replication, marketing posters, selling-point extraction, review analysis |
| Dify AI platform               | Workflows / agents / knowledge bases, multiple cases (complaint classification, research reports, customer service analysis, review analysis), Python invocation |
| Containerization               | Core Docker concepts, installation and common commands                               |
| Enterprise LLM deployment      | Tencent Cloud/Alibaba Cloud, Docker, Dify, AutoDL, Ollama, Xinference, local Coze deployment |
| AI coding tool — Trae AI       | Installation and usage, multi-model APIs, MCP integration                            |
| AI coding tool — Qoder         | Usage and debugging, project development                                             |

### 03 Core LLM Development Frameworks

| Chapter                          | Content Summary                                                                |
| -------------------------------- | ------------------------------------------------------------------------------ |
| LangChain principles and usage   | Model I/O, Prompt, Parser, Runnable / LCEL, Memory, Tools, Retrieval, Agent    |
| LangGraph principles and usage   | Graph thinking, State/Node/Edge, persistent memory, streaming, multi-agent and A2A |
| MCP from principles to practice  | Comparison with Function Calling, communication mechanisms, workflow, server deployment and custom development |
| Cross-agent communication: A2A   | Relationship with MCP, messages and authentication, typical scenarios          |

### 04 Enterprise RAG / Agent Project Practice

| Chapter                                        | Content Summary                                                                                                                                                                        |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shopkeeper Knowledge Base                      | LangGraph RAG workflow, MinerU/OCR, vector + sparse + Neo4j multi-route retrieval, HyDE/BGE-Rerank, RAGAS evaluation                                                                    |
| E-commerce Assistant                           | Intent parsing, multi-source knowledge bases, streaming replies, human handoff, conversation retrospectives, multi-channel and monitoring                                              |
| [Shopkeeper Data Q&A](实战项目-电商问数/0-前言.md) | Around natural-language data querying, threading together MySQL data warehouse, metadata knowledge base, Qdrant vector retrieval, Elasticsearch field-value retrieval, LangGraph workflow, SQL generation/validation/execution, FastAPI SSE and frontend-backend integration |
| [Deep Research](实战项目-深度研搜/0-前言.md)     | A multi-agent research system built on [DeepAgents](实战项目-深度研搜/1-DeepAgents基础与核心概念.md), threading together web search, MySQL queries, RAGFlow knowledge base, file reading and generation, FastAPI endpoints and WebSocket real-time progress push |
| Market Compass                                 | Scenario-based task decomposition, 0-to-1 design and development, milestone and progress control, code review and results presentation                                                   |

> **Recommended completed hands-on projects:**
>
> - [Shopkeeper Data Q&A](实战项目-电商问数/0-前言.md) ([source repo](https://github.com/didilili/shopkeeper-agent)): not a simple SQL generation demo — it puts `MySQL`, `LangGraph`, `Qdrant`, `Elasticsearch`, `FastAPI` and more into a single runnable intelligent data-query pipeline.
> - [Deep Research](实战项目-深度研搜/0-前言.md) ([source repo](https://github.com/didilili/deepsearch-agents)): not an ordinary chat box — around open-ended research tasks, it turns main-agent scheduling, sub-agent division of labor, multi-source retrieval, file generation and delivery, and real-time frontend-backend interaction into a complete closed loop.

### 05 Fine-tuning in Practice

| Chapter                                                                             | Content Summary                                                  |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [28 Fine-tuning Overview](28-大模型微调概述与整体流程.md)                            | Problem diagnosis, model types, baselines and a keyword-driven project workflow |
| [29 Data and Templates](29-微调数据准备与对话模板.md)                                 | Real JSONL, sample quality, cleaning and splitting, dialogue templates |
| [30 Training and Efficient Fine-tuning](30-模型训练原理与高效微调.md)                  | Training parameters, VRAM worked examples, LoRA and QLoRA        |
| [31 LLaMA-Factory Hands-on](31-LLaMA-Factory环境搭建与微调实战.md)                     | AutoDL single GPU / FP16, cleaned-version training, logging and backups |
| [32 Evaluation and Deployment](32-微调效果评估与模型部署.md)                           | Single-sample validation, 200-sample two-group prediction and scoring, export and standalone loading; vLLM as optional |
| [33 VRAM Optimization and Multi-GPU Training](33-微调显存优化与多卡训练.md)            | Single-GPU VRAM troubleshooting, parallelism division of labor, ZeRO and short-run log interpretation |

### 06 Engineering Conventions at Major Tech Companies

| Chapter                                  | Content Summary                                                              |
| ---------------------------------------- | ---------------------------------------------------------------------------- |
| Enterprise LLM R&D process               | Technical research, solution and framework design, RAG and pipelines, evaluation and roles, project initiation and requirements documents |
| Current hot topics in LLMs               | Mainstream Agent/RAG techniques, tracking the frontier and hot topics        |

---

## 🏗️ Agent Project Architecture and Technical Architecture

![Agent ecosystem architecture diagram](images/智能体生态架构图.png)

---

<a id="quick-start"></a>

## 🚀 Quick Start

Study alongside the [online docs](https://didilili.github.io/ai-agents-from-zero/#/). Want to run a case right now? Just follow the steps below. For detailed environment notes, API application instructions and common error handling, see [Getting Started & FAQ](新手入门与常见问题.md).

1. **Clone the repository and enter the project directory**

   ```bash
   git clone https://github.com/didilili/ai-agents-from-zero.git
   cd ai-agents-from-zero
   ```

2. **Set up the environment** (Python 3.10 recommended; 3.10–3.13 supported)

   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate          # macOS/Linux
   # .venv\Scripts\activate           # Windows CMD
   pip install -r requirements.txt
   ```

3. **Configure your API key**
   - Copy `.env-example` in the repository root to `.env`
   - Fill in your API key (e.g. Qwen / Alibaba Bailian, DeepSeek) in `.env`. Variable names must match the code (e.g. `aliQwen-api`, `QWEN_API_KEY`, `deepseek-api`)
   - How to apply for a key on each platform: see [Getting Started & FAQ — How to apply for an API key on each platform](新手入门与常见问题.md#_5、各-api-平台如何申请-key？)

4. **Run your first case from the repository root**

   ```bash
   python 案例与源码-2-LangChain框架/01-helloworld/StandardDesc.py
   ```

   **Tip**: run `python` from the **repository root** so that virtual environments, dependencies and output files stay in one place. `load_dotenv()` in ordinary scripts usually searches upward for `.env` automatically; if you are using an IDE, a REPL or a debugger and the key is not being picked up, check its working directory configuration. If you would rather not use a cloud API, you can use a [local Ollama model](新手入门与常见问题.md#_54-不想用云-api：用本地-ollama（无需-key）) instead (no key required).

If you hit `ModuleNotFoundError`, API key errors, or "cannot find `.env`", see [Getting Started & FAQ — Common problems and solutions](新手入门与常见问题.md#_6、常见问题与解决).

---

## 💬 Community

Want to discuss **AI coding, hands-on Agent / RAG practice, and interview experience** with more readers? Leave a message in the [GitHub group application thread](https://github.com/didilili/ai-agents-from-zero/issues/46) to apply for the WeChat group.

---

## 📖 About This Repository

- **Goal**: to build a set of **AI Agent hands-on crash-course tutorials that are genuinely beginner-friendly, systematic and long-term maintained** — not only explaining concepts clearly but also getting the cases running, so you can go from zero to independently building **RAG / Agent / multi-agent** projects, and articulate your solutions and projects in engineering language.
- **Technical positioning**: focused on the **Python agent development path**, emphasizing **LangChain / LangGraph** and related engineering practice. It deliberately **does not follow the Java route of Spring AI / langchain4j**, making it a better fit for those who want to go directly into Python-based LLM application development.
- **Tutorial sources**: draws on course materials such as the **Shang Silicon Valley "LLM Agent Crash Course"**, and builds on top of them by continuously **restructuring, supplementing and maintaining** the content using public documentation, community practice and project experience, progressively shaping it into a systematic learning resource for **Python agent application development**.
- **Interview question sources**: a good portion of the question bank is compiled from **real interviews at major tech companies**, public interview reports and frequently probed follow-up scenarios, refactored in an engineering-oriented way around this repository's main chapter line, making it better suited for review from a project and system-design perspective.
- **Content composition**: **systematic chapter notes** + **runnable case source code** + **[interview question bank](AI智能体与大模型应用开发面试题库.md)** (benchmarked against **comparable online training** and **experienced/graduate hire JDs**).

---

## 🌐 Translation Progress

| Item | Language | Status |
| ---- | -------- | ------ |
| `README.en.md` | English | ✅ Done |
| `CONTRIBUTING.en.md` | English | ✅ Done |
| `en/Glossary.md` (full glossary) | English | 🚧 In progress |
| `en/01-1-...` (Chapter 1-1) | English | 🚧 In progress |
| Chapters 1-2 … 33, interview bank, hands-on projects | English | ⏳ Planned |

Translation is tracked per file. If you would like to help with a specific chapter, please open an issue or comment on an existing one to avoid duplicate work.

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/image?repos=didilili/ai-agents-from-zero&type=date&legend=top-left)]()

---

**Repository name (English)**: `ai-agents-from-zero` · **Repository name (Chinese)**: 《AI 智能体实战速成指南：从零到企业级落地》
