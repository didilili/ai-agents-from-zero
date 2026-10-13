# Full-Book Glossary

This glossary is not here to pile up jargon — it is here to thread the core concepts of this tutorial together for you.

When reading this tutorial, what usually trips people up is not "I have never seen this word", but rather:

- You have seen Prompt, RAG, Tool and Agent, yet cannot tell which problem each one solves.
- Coze, Dify, LangChain, LangGraph, MCP and DeepAgents all talk about "agents", but on different levels.
- You can follow the cases and run the code, yet cannot explain why a Workflow is the right choice here and an Agent there.
- Once you reach the hands-on projects, `thread_id`, `session_dir`, Checkpoint, Backend and ContextVar start blurring together.

So this glossary is organized progressively: first build the concept map, then look terms up by capability layer, and finally tie it together with a confusable-concepts comparison.

---

## 1. How to use this glossary

If this is your first time studying, this order works well:

1. Read Section 2, "Concept map of the book", to see where each family of concepts sits in the book.
2. Read Section 3, "Quick reference for high-frequency confusable concepts", to get the muddiest boundaries straight first.
3. When you reach a chapter, come back to the matching group and look terms up — there is no need to memorize them all at once.
4. When working on a project, focus on "Engineering and delivery terms", since those are closest to real delivery.

Each term tries to answer three questions:

| Question | What to read |
| -------------- | ---------------------- |
| What is it | Read "one-line explanation" |
| What problem does it solve | Read "problem it solves" |
| What is it easily confused with | Read "confusion point" |
| Want to go deeper | Follow "suggested reading" back to the original chapter |

---

## 2. Concept map of the book

You can start by thinking of the whole course as 8 capability layers.

| Layer | What you are learning | Representative terms | Core question |
| ---- | ---------------- | --------------------------------------------- | -------------------------------- |
| 1 | LLM fundamentals | LLM, Token, context window, inference, hallucination | What a model is, and where the capability boundary lies |
| 2 | How to talk to a model | Prompt, Message, Output Parser, structured output | How to state a task clearly, and how to get results back |
| 3 | Supplementing external knowledge | Embedding, vector database, Retriever, RAG, Rerank | How to retrieve what the model does not know |
| 4 | Tools and actions | Tool, Function Calling, ToolMessage, idempotency | How a model calls out to external systems |
| 5 | Flows and agents | Workflow, Agent, ReAct, create_agent | Who decides where to go next |
| 6 | Protocols and ecosystem integration | MCP, Resource, Server, A2A, Handoff | How external capabilities and other agents plug in |
| 7 | Stateful orchestration | LangGraph, State, Node, Edge, Checkpoint | How complex flows become controllable, recoverable and observable |
| 8 | Production project engineering | FastAPI, SSE, WebSocket, ContextVar, logging | How to turn a capability into a usable, inspectable system |

One-line mnemonic:

> Prompt handles "how to ask", RAG handles "looking things up", Tool handles "taking action", Workflow handles "a fixed process", Agent handles "dynamic decisions", MCP handles "standardized capability integration", LangGraph handles "running a process with state", and engineering handles "delivering it reliably".

---

## 3. Quick reference for high-frequency confusable concepts

| Easily confused concepts | Quick distinction |
| ------------------------ | ------------------------------------------------------------------ |
| Prompt vs System Message | Prompt is the umbrella term for input instructions; System Message is a higher-priority message carrying system rules |
| RAG vs fine-tuning | RAG does not change model parameters and looks things up at runtime; fine-tuning changes model behaviour, format and habits |
| Continued pre-training vs fine-tuning | Continued pre-training leans towards filling in domain knowledge distribution; fine-tuning leans towards task behaviour and output style |
| Workflow vs Agent | A Workflow's path is designed mainly by people; an Agent participates in deciding the next step |
| Tool Calling vs MCP | Tool Calling is how a model expresses its intent to call something; MCP is a protocol for standardized external capability integration |
| Tool vs Resource | A Tool is an executable action; a Resource is more like readable context |
| Agent vs multi-agent | An Agent is a single decision-making system; multi-agent emphasizes collaboration and transfer of control between several agents |
| MCP vs A2A | MCP connects tools and resources; A2A connects another agent or agent system |
| LangChain vs LangGraph | LangChain leans towards component encapsulation; LangGraph leans towards stateful flow orchestration |
| Conversation history vs memory | Conversation history is the message content; memory is the system's ability to make use of that history |
| Checkpoint vs Store | A Checkpoint saves the state of one execution thread; a Store leans towards long-term data shared across threads |
| Backend vs database | In DeepAgents, Backend is an abstraction over files, state and storage — it is not the same thing as a business database |
| Subagent vs Skill | A Subagent is an assistant that can execute tasks independently; a Skill is a reusable capability description and resource bundle |
| SSE vs WebSocket | SSE is mainly one-way server push; WebSocket supports two-way real-time communication |
| thread_id vs session_dir | `thread_id` identifies the same execution thread; `session_dir` identifies the file directory for the current task |

---

## 4. LLM and training fundamentals

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| ---------------- | ------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------------------------- |
| **LLM** | Large Language Model | Mainly handles natural language understanding, generation, reasoning and coding tasks | [1-1](../1-1-大模型认知与工程概览.md) |
| **AIGC** | AI Generated Content | A results-oriented view; it does not mean the underlying stack must be an LLM only | [1-1](../1-1-大模型认知与工程概览.md) |
| **AGI** | Artificial General Intelligence | More of a long-term goal than a practical technology term in current projects | [1-1](../1-1-大模型认知与工程概览.md) |
| **Token** | The basic unit a model uses to process text | It is not character count; Chinese, English and code are split differently | [1-1](../1-1-大模型认知与工程概览.md) |
| **Context window** | The maximum context a model can see at once | Affects long-document Q&A, multi-turn dialogue and how much RAG content you can concatenate | [1-1](../1-1-大模型认知与工程概览.md) |
| **Transformer** | An important architectural foundation of modern LLMs | Self-attention is the key part; not all AI models are Transformers | [1-1](../1-1-大模型认知与工程概览.md) |
| **MoE** | Mixture of Experts | Not all parameters are activated every time; experts are activated selectively via routing | [1-1](../1-1-大模型认知与工程概览.md) |
| **Pre-training** | Training foundational capability on large-scale general corpora | Gives the model broad language and knowledge capability first | [1-1](../1-1-大模型认知与工程概览.md) |
| **Continued pre-training** | Continue pre-training on top of an existing base | Leans towards filling in domain knowledge distribution; usually costs more than ordinary fine-tuning | [1-3](../1-3-RAG、微调、续训与智能体选型.md) |
| **Fine-tuning** | Adjust model behaviour with task data | Leans towards format, style, preferences and task habits | [1-3](../1-3-RAG、微调、续训与智能体选型.md) |
| **SFT** | Supervised Fine-Tuning | Trains the model on labelled input-output samples | [1-1](../1-1-大模型认知与工程概览.md), [1-3](../1-3-RAG、微调、续训与智能体选型.md) |
| **RLHF / RLAIF** | Alignment training based on human or AI feedback | Makes the model better match preferences, safety norms and answering habits | [1-1](../1-1-大模型认知与工程概览.md) |
| **LoRA** | Low-Rank Adaptation | Fine-tunes the model incrementally at lower cost | [1-3](../1-3-RAG、微调、续训与智能体选型.md) |
| **QLoRA** | Quantized LoRA | Commonly used in fine-tuning scenarios with tighter VRAM | [1-3](../1-3-RAG、微调、续训与智能体选型.md) |
| **Catastrophic forgetting** | New training washes out capability the model already had | Something both fine-tuning and continued pre-training must guard against | [1-3](../1-3-RAG、微调、续训与智能体选型.md) |
| **Hallucination** | The model states something wrong with total confidence | RAG can mitigate it but cannot guarantee eliminating it | [1-1](../1-1-大模型认知与工程概览.md), [19](../19-RAG检索增强生成.md) |
| **Inference** | The stage where the model generates answers online | Different from the training stage; online calls mainly happen at inference time | [11](../11-Model-I-O与模型接入.md) |
| **Temperature** | A parameter controlling output randomness | Higher is usually more divergent, lower usually more stable — lower is not always better | [11](../11-Model-I-O与模型接入.md) |
| **Top P** | A sampling parameter based on probability mass | Together with Temperature it affects output diversity | [11](../11-Model-I-O与模型接入.md) |

---

## 5. Prompt and Model I/O terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| -------------------------- | ---------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------ |
| **Prompt** | The input instruction given to a model | Ranges from a single sentence to a complex template | [1-2](../1-2-提示词工程基础.md), [13](../13-提示词与消息模板.md) |
| **Prompt engineering** | The systematic design of prompts | The point is not writing pretty words but making task boundaries and output constraints clearer | [1-2](../1-2-提示词工程基础.md) |
| **Zero-shot** | Let the model do the task with no examples | Suited to simple problems with clear boundaries | [1-2](../1-2-提示词工程基础.md) |
| **Few-shot** | Give a few examples before the task | Suited to tasks where format, style or classification criteria need to be demonstrated | [1-2](../1-2-提示词工程基础.md) |
| **System Message** | System-level rule message | Commonly defines role, boundaries, style and hard constraints | [13](../13-提示词与消息模板.md) |
| **Human Message** | User message | Represents the current user input | [13](../13-提示词与消息模板.md) |
| **AI / Assistant Message** | Model message | Can be a past reply, and may also contain traces of tool calls | [11](../11-Model-I-O与模型接入.md), [13](../13-提示词与消息模板.md) |
| **PromptTemplate** | Text template | Suited to a single block of text prompt | [13](../13-提示词与消息模板.md) |
| **ChatPromptTemplate** | Chat message template | Suited to multi-role, multi-turn message structures | [13](../13-提示词与消息模板.md) |
| **MessagesPlaceholder** | Message placeholder | Used to insert history messages back into a prompt dynamically | [13](../13-提示词与消息模板.md), [16](../16-记忆与对话历史（含Redis基础）.md) |
| **Model I/O** | The model input/output layer | Handles how to feed the model, how to get results back and how to parse them | [11](../11-Model-I-O与模型接入.md) |
| **AIMessage** | The model reply object in LangChain | Not just text — it may also carry metadata, tool_calls and more | [11](../11-Model-I-O与模型接入.md) |
| **invoke** | One-shot call | The most common execution mode | [10](../10-LangChain快速上手与HelloWorld.md), [15](../15-LCEL与链式调用.md) |
| **batch** | Batch call | Suited to processing a set of inputs together | [15](../15-LCEL与链式调用.md) |
| **stream** | Streaming output | Returns while generating; suited to real-time interaction and observing the process | [10](../10-LangChain快速上手与HelloWorld.md), [25](../25-LangGraph高级特性.md) |
| **Output Parser** | Output parser | Turns raw model output into a structure that is easier for programs to handle | [14](../14-输出解析器.md) |
| **Structured Output** | Structured output | Makes the model return along specified fields or a schema | [14](../14-输出解析器.md), [21](../21-Agent智能体.md) |
| **TypedDict** | Lightweight structure declaration | More of a type hint; not the same as strong runtime validation | [14](../14-输出解析器.md) |
| **Pydantic** | Python data validation library | Commonly used for schema definition and runtime validation | [14](../14-输出解析器.md), [17](../17-Tools工具调用.md) |
| **JSON Schema** | JSON structure constraint specification | Describes field types, required fields, enum values and more | [14](../14-输出解析器.md) |
| **response_format** | The entry point for constraining result structure | In the LangChain 1.x context, often used to constrain an agent's final output | [21](../21-Agent智能体.md) |
| **ProviderStrategy** | Use a provider's native structured output | Requires the underlying model or provider to actually support it | [21](../21-Agent智能体.md) |
| **ToolStrategy** | Achieve structured output via tool calling | Commonly used when there is no native structured output capability | [21](../21-Agent智能体.md) |

---

## 6. Platform, deployment and model-serving terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| -------------------- | ------------------------------------ | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Coze** | An AI platform leaning towards zero-code, templated, rapid building | Better suited to quick validation and a platform-driven operating experience | [3](../3-基于Coze&Dify平台的智能体开发.md), [5](../5-Python调用Coze平台工作流.md) |
| **Dify** | An AI application platform leaning towards developers and team collaboration | Better suited to workflows, knowledge bases, API calls and private deployment | [3](../3-基于Coze&Dify平台的智能体开发.md), [4](../4-Python调用Dify平台工作流.md), [6](../6-Coze与Dify的Windows平台部署.md#_4、dify-的安装和启动) |
| **Workflow** | Fixed or semi-fixed process orchestration | Appears in Coze, Dify and LangGraph, but is not the same as an Agent | [3](../3-基于Coze&Dify平台的智能体开发.md), [4](../4-Python调用Dify平台工作流.md) |
| **API Key** | Identity credential for API calls | Do not lump it together with a model name or Base URL | [4](../4-Python调用Dify平台工作流.md), [10](../10-LangChain快速上手与HelloWorld.md) |
| **Base URL** | The root path of an API endpoint | Determines where requests are sent | [10](../10-LangChain快速上手与HelloWorld.md), [11](../11-Model-I-O与模型接入.md) |
| **Ollama** | A lightweight tool for running LLMs locally | Suited to local development, personal learning and small-scale local deployment | [12](../12-Ollama本地部署与调用.md) |
| **Xinference** | A model-serving platform that hosts many model types | Better suited to exposing LLM, Embedding and Rerank uniformly | [7](../7-企业级大模型部署.md) |
| **Inference engine** | The low-level execution layer that runs models efficiently | Such as vLLM, SGLang, Ollama, TEI — the focus is running the model | [7](../7-企业级大模型部署.md) |
| **Model hosting platform** | The service layer that manages and exposes models uniformly | The focus is a unified entry point and unified governance | [7](../7-企业级大模型部署.md) |
| **OpenAI-compatible API** | An API shape that imitates OpenAI's style | The goal is to lower integration cost; it does not mean the underlying model is OpenAI | [7](../7-企业级大模型部署.md), [11](../11-Model-I-O与模型接入.md) |
| **Docker** | A containerized runtime environment | The point is not virtual machines but packaging and running services reproducibly | [8](../8-Docker快速入门与Dify部署排障.md) |
| **Image** | A template for running a container | More like an application snapshot | [8](../8-Docker快速入门与Dify部署排障.md) |
| **Container** | A running instance started from an image | One image can start many containers | [8](../8-Docker快速入门与Dify部署排障.md) |
| **Volume** | Persistent storage outside the container | Deleting a container does not necessarily delete data — it depends on whether the volume is kept | [8](../8-Docker快速入门与Dify部署排障.md) |
| **Docker Compose** | A multi-container service orchestration tool | Commonly used to start a database, backend, frontend and other services in one go | [8](../8-Docker快速入门与Dify部署排障.md) |

---

## 7. LangChain and LCEL terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| -------------------- | ----------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------- |
| **LangChain** | A component framework for LLM application development | Leans towards encapsulating models, prompts, parsers, tools and agents | [9](../9-LangChain概述与架构.md), [10](../10-LangChain快速上手与HelloWorld.md) |
| **Runnable** | A unified abstraction for executable components | Prompt, Model, Parser and Tool can all be abstracted into Runnables | [15](../15-LCEL与链式调用.md) |
| **LCEL** | LangChain Expression Language | Chains several Runnables together in a declarative style | [15](../15-LCEL与链式调用.md) |
| **RunnableSequence** | Sequential chain | The output of one step feeds the next | [15](../15-LCEL与链式调用.md) |
| **RunnableParallel** | Parallel chain | Runs several branches at once, then merges the results | [15](../15-LCEL与链式调用.md) |
| **RunnableBranch** | Conditional branch chain | Routes to different handling paths based on a condition | [15](../15-LCEL与链式调用.md) |
| **RunnableLambda** | Custom logic node | Suited to field processing, business mapping and lightweight logic | [15](../15-LCEL与链式调用.md) |
| **Chain** | A processing chain made of several steps | In the LCEL era it is better understood through the Runnable system | [9](../9-LangChain概述与架构.md), [15](../15-LCEL与链式调用.md) |
| **Provider** | A model provider or integration vendor | Such as OpenAI, DeepSeek, Alibaba Bailian, Ollama | [10](../10-LangChain快速上手与HelloWorld.md), [11](../11-Model-I-O与模型接入.md) |
| **Callback** | An event hook during execution | Useful for logging, monitoring, streaming and debugging | [9](../9-LangChain概述与架构.md), [25](../25-LangGraph高级特性.md) |

---

## 8. Memory, session and persistence terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| ------------------------------ | ------------------------------ | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Conversation history** | The content of past messages | It is the content itself; it does not mean the system will really use it correctly | [16](../16-记忆与对话历史（含Redis基础）.md) |
| **Memory** | The system's ability to make use of historical information | Can come from conversation history, a database, a vector store or long-term storage | [16](../16-记忆与对话历史（含Redis基础）.md), [25](../25-LangGraph高级特性.md) |
| **RunnableWithMessageHistory** | Wraps a Runnable with message-history management | Suited to understanding how LangChain wires up conversation history | [16](../16-记忆与对话历史（含Redis基础）.md) |
| **Session ID** | Session identifier | Used to distinguish different users or different conversations | [16](../16-记忆与对话历史（含Redis基础）.md) |
| **Redis** | A commonly used in-memory database | Can store session history, caches, queues and more | [16](../16-记忆与对话历史（含Redis基础）.md) |
| **Checkpoint** | A snapshot of execution state | Lets a graph or agent recover to a particular execution point | [25](../25-LangGraph高级特性.md), [Deep Research 5](../实战项目-深度研搜/5-人机协作与中断恢复.md) |
| **Checkpointer** | The component that saves and loads checkpoints | Saves execution state on a given thread; the basis for recovery and Time-Travel | [25](../25-LangGraph高级特性.md), [Deep Research 5](../实战项目-深度研搜/5-人机协作与中断恢复.md) |
| **Store** | Cross-thread long-term storage | Unlike a single-thread checkpoint, better suited to sharing long-term memory or business data | [25](../25-LangGraph高级特性.md), [Deep Research 6](../实战项目-深度研搜/6-长期记忆与Backend存储.md) |
| **thread_id** | Execution thread identifier | Recovery, interruption and progress push often depend on it | [Deep Research 5](../实战项目-深度研搜/5-人机协作与中断恢复.md), [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |
| **session_dir** | The file directory for the current task | Used to isolate uploaded files, Markdown, PDFs and other artifacts | [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |

---

## 9. Vector, retrieval and RAG terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| ---------------------- | ------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------------------- |
| **Embedding** | Turning text into a vector representation | Makes semantically similar text closer together in vector space | [18](../18-向量数据库与Embedding实战.md) |
| **Vector** | A numerical representation of content such as text or images | In this tutorial it mainly means text vectors | [18](../18-向量数据库与Embedding实战.md) |
| **Vector database** | A database or capability that stores and retrieves vectors | Its core value is semantic similarity search, not ordinary SQL queries | [18](../18-向量数据库与Embedding实战.md) |
| **Qdrant** | A vector database | Used for vector retrieval in the Shopkeeper Data Q&A project | [Data Q&A 5](../实战项目-电商问数/5-Qdrant与ES快速入门与接入.md) |
| **Elasticsearch / ES** | A search engine | Leans towards full-text search, keyword search and inverted indexes | [Data Q&A 5](../实战项目-电商问数/5-Qdrant与ES快速入门与接入.md) |
| **Similarity** | Measuring how close two vectors are | Common options include cosine similarity, dot product and Euclidean distance | [18](../18-向量数据库与Embedding实战.md) |
| **Chunking** | Cutting long text into smaller pieces | Too large adds noise; too fragmented loses semantic completeness | [19](../19-RAG检索增强生成.md) |
| **Chunk Overlap** | The overlapping region between adjacent chunks | Used to reduce information loss caused by chunk boundaries | [19](../19-RAG检索增强生成.md) |
| **Metadata** | Structural information attached to a document chunk | Such as source, time, title and tags; useful for filtering and explaining results | [18](../18-向量数据库与Embedding实战.md), [19](../19-RAG检索增强生成.md) |
| **Retriever** | The retriever | Responsible for finding candidate passages from the knowledge base | [19](../19-RAG检索增强生成.md) |
| **Recall / retrieval** | Finding a batch of candidates first | The point is not missing anything; it does not mean the final ranking is best | [18](../18-向量数据库与Embedding实战.md), [19](../19-RAG检索增强生成.md) |
| **Rerank** | Re-ordering retrieved results | Puts the genuinely most useful passages first | [7](../7-企业级大模型部署.md), [19](../19-RAG检索增强生成.md) |
| **Filter** | Narrowing the retrieval scope by metadata conditions | Commonly used for tenant isolation, time ranges and document-type limits | [19](../19-RAG检索增强生成.md) |
| **RAG** | Retrieval-Augmented Generation | Looks up external material first, then generates answers grounded in it | [1-3](../1-3-RAG、微调、续训与智能体选型.md), [19](../19-RAG检索增强生成.md) |
| **Indexing stage** | The stage that prepares the knowledge base | Includes loading documents, chunking, embedding and writing into the store | [19](../19-RAG检索增强生成.md) |
| **Retrieval stage** | The stage that looks up candidates when a user asks | This is runtime behaviour | [19](../19-RAG检索增强生成.md) |
| **Generation stage** | Handing retrieval results and the question to the model | Not just concatenating passages — prompt constraints matter too | [19](../19-RAG检索增强生成.md) |
| **Pipeline RAG** | RAG whose retrieval steps are basically fixed | Easier to debug; better for learning the base pipeline first | [19](../19-RAG检索增强生成.md) |
| **Agentic RAG** | Whether and how to retrieve is decided by an agent | More flexible, but also more complex and more uncertain | [19](../19-RAG检索增强生成.md), [21](../21-Agent智能体.md) |
| **RAGFlow** | A platform for knowledge bases and RAG applications | Used in the Deep Research project to query an enterprise internal knowledge base | [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |

---

## 10. Tool, Workflow, Agent and protocol terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| ---------------------- | ------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Tool** | An external capability exposed for a model to use | In essence usually a function, an API, a database read/write or a wrapped third-party service | [17](../17-Tools工具调用.md) |
| **Tool Calling** | The mechanism by which a model expresses intent to call a tool | Often understood at the same layer as Function Calling | [17](../17-Tools工具调用.md) |
| **Function Calling** | A common name for Tool Calling | This wording is more common in vendor API documentation | [17](../17-Tools工具调用.md), [20](../20-MCP模型上下文协议.md) |
| **args_schema** | The definition of a tool's parameter structure | Tells the model which parameters a tool needs and what their types are | [17](../17-Tools工具调用.md) |
| **ToolMessage** | The tool execution result message | Hands the tool result back to the model so it can keep reasoning or answering | [17](../17-Tools工具调用.md) |
| **Workflow** | Fixed or semi-fixed step orchestration | Control of the process lies mainly with the developer | [3](../3-基于Coze&Dify平台的智能体开发.md), [15](../15-LCEL与链式调用.md) |
| **Agent** | A system with decision-making and multi-step action capability | The point is deciding when to call, what to call and what to do next | [1-3](../1-3-RAG、微调、续训与智能体选型.md), [21](../21-Agent智能体.md) |
| **ReAct** | Reason + Act pattern | Reason first, then act, then observe, then continue | [21](../21-Agent智能体.md) |
| **AgentExecutor** | The classic agent executor | Better for understanding early agent mechanics and historical material | [21](../21-Agent智能体.md) |
| **create_agent** | The LangChain 1.x high-level agent entry point | Closer to the currently recommended usage; relies on the LangGraph runtime underneath | [21](../21-Agent智能体.md) |
| **MCP** | Model Context Protocol | A protocol that uniformly exposes external tools, resources and prompt templates to AI applications | [20](../20-MCP模型上下文协议.md) |
| **Host** | The side that hosts and initiates an MCP session | Often understood as the AI application host | [20](../20-MCP模型上下文协议.md) |
| **Client** | The client component connecting to an MCP Server | Handles protocol interaction, call forwarding and session management | [20](../20-MCP模型上下文协议.md) |
| **Server** | The side that exposes MCP capabilities | Can expose Tool, Resource and Prompt | [20](../20-MCP模型上下文协议.md) |
| **Resource** | The resource object in MCP | More like readable context; not necessarily an executable action | [20](../20-MCP模型上下文协议.md) |
| **Prompt (in MCP)** | A reusable prompt-template resource in MCP | Do not conflate it with the general Prompt concept | [20](../20-MCP模型上下文协议.md) |
| **FastMCP** | A more convenient development tool for MCP servers | Helps you write Servers more easily, but it is not the protocol itself | [20](../20-MCP模型上下文协议.md) |
| **stdio** | MCP's local standard-input/output transport | Commonly used for local process communication | [20](../20-MCP模型上下文协议.md) |
| **Streamable HTTP** | MCP's HTTP transport | Suited to networked integration | [20](../20-MCP模型上下文协议.md) |
| **A2A** | Agent-to-Agent protocol | Leans towards cross-system agent collaboration; it is not a tool-integration protocol | [26](../26-LangGraph多智能体与A2A.md) |
| **Supervisor** | The central-scheduler pattern | One upper-layer agent decomposes tasks and distributes them downstream | [26](../26-LangGraph多智能体与A2A.md) |
| **Handoff** | Transfer of control | The current task switches from one agent to another to continue | [26](../26-LangGraph多智能体与A2A.md) |
| **Skill / Skills** | A reusable capability bundle | More like a combination of prompts, descriptions, scripts and resources — not an independent agent | [27](../27-Skills技能与AI编程工具实践.md), [Deep Research 7](../实战项目-深度研搜/7-中间件机制与Skills配置.md) |

---

## 11. LangGraph and stateful orchestration terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| -------------------- | ------------------------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------- |
| **LangGraph** | A graph orchestration framework for stateful workflows | Better suited to complex, branchable, loopable, persistable processes | [22](../22-LangGraph概述与快速入门.md) |
| **State** | The shared state inside a graph | The whole graph flows around it | [22](../22-LangGraph概述与快速入门.md), [23](../23-LangGraphAPI：图与状态.md) |
| **StateGraph** | A state-based way to define a graph | One of the most common graph-building entry points in LangGraph | [23](../23-LangGraphAPI：图与状态.md) |
| **Node** | A node | A processing unit in the graph, often a function or capability block | [24](../24-LangGraphAPI：节点、边与进阶.md) |
| **Edge** | An edge | Determines where the flow goes from one node | [24](../24-LangGraphAPI：节点、边与进阶.md) |
| **Conditional Edge** | Conditional edge | Decides the next branch based on state content | [24](../24-LangGraphAPI：节点、边与进阶.md) |
| **Reducer** | State merge rule | Decides how old and new state values are merged; especially affects parallel branches | [23](../23-LangGraphAPI：图与状态.md) |
| **Pregel** | LangGraph's underlying graph execution model | Advances graph execution using Actors, Channels and Supersteps | [23](../23-LangGraphAPI：图与状态.md) |
| **Superstep** | One scheduling round in graph execution | Each round plans first, then executes in parallel, then merges updates | [23](../23-LangGraphAPI：图与状态.md) |
| **StateSnapshot** | A state snapshot | Saves the values, next steps, config and other execution context at a moment in time | [23](../23-LangGraphAPI：图与状态.md), [25](../25-LangGraph高级特性.md) |
| **START / END** | The graph's entry and exit | Define where the process starts and where it ends | [23](../23-LangGraphAPI：图与状态.md) |
| **Command** | A runtime control primitive | Suited to expressing execution and the decision of where to jump together | [24](../24-LangGraphAPI：节点、边与进阶.md) |
| **Send** | A dynamic dispatch control primitive | Suited to dispatching subtasks in parallel at runtime | [24](../24-LangGraphAPI：节点、边与进阶.md) |
| **Runtime** | The runtime context object | Commonly used for configuration, dependencies and non-business state | [24](../24-LangGraphAPI：节点、边与进阶.md) |
| **Streaming** | Observing execution as a stream | Suited to real-time display, debugging and monitoring | [25](../25-LangGraph高级特性.md) |
| **Interrupt** | Interrupt execution and wait for external handling | Commonly used for human confirmation, approval and pausing at critical nodes | [25](../25-LangGraph高级特性.md), [Deep Research 5](../实战项目-深度研搜/5-人机协作与中断恢复.md) |
| **Time-Travel** | Replay or re-run based on historical checkpoints | Suited to debugging, retrospectives and error correction | [25](../25-LangGraph高级特性.md) |
| **Subgraph** | A subgraph | Used to modularize a complex process | [25](../25-LangGraph高级特性.md) |
| **Multi-agent graph** | Organizing several agents to collaborate with a graph | The point is how state, routing and context passing are designed | [26](../26-LangGraph多智能体与A2A.md) |

---

## 12. DeepAgents and Deep Research project terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| ------------------------ | ------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **DeepAgents** | Agent-building capability for deep tasks and multi-agent collaboration | The point is the engineering combination of main agent, subagents, tools, Backend and Skill | [Deep Research 1](../实战项目-深度研搜/1-DeepAgents基础与核心概念.md) |
| **Main Agent** | The main agent | Responsible for understanding the task, planning steps, dispatching assistants and consolidating results | [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |
| **Subagent** | A subagent | Dedicated to one class of task, such as search, database queries or RAGFlow queries | [Deep Research 3](../实战项目-深度研搜/3-子智能体进阶与异步执行.md) |
| **Orchestrator-Workers** | A master-worker multi-agent architecture | The main agent is like a lead; subagents are like specialist assistants | [Deep Research 1](../实战项目-深度研搜/1-DeepAgents基础与核心概念.md), [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |
| **Backend** | DeepAgents' abstraction over files, state and storage | Not the same as a business backend, nor a database | [Deep Research 6](../实战项目-深度研搜/6-长期记忆与Backend存储.md) |
| **FilesystemBackend** | A Backend that maps the agent filesystem to a local directory | Commonly used for Skills, file read/write and session-directory isolation | [Deep Research 6](../实战项目-深度研搜/6-长期记忆与Backend存储.md), [Deep Research 7](../实战项目-深度研搜/7-中间件机制与Skills配置.md) |
| **StateBackend** | A Backend that stores execution state | Leans towards current task state and recovery | [Deep Research 6](../实战项目-深度研搜/6-长期记忆与Backend存储.md) |
| **StoreBackend** | A long-term storage Backend | Leans towards long-term data shared across sessions and threads | [Deep Research 6](../实战项目-深度研搜/6-长期记忆与Backend存储.md) |
| **CompositeBackend** | Combines several Backends | Used to manage files, state and long-term storage in layers | [Deep Research 6](../实战项目-深度研搜/6-长期记忆与Backend存储.md) |
| **Middleware** | A governance layer in the execution chain | Does not handle the business itself, but applies limits, retries, redaction, approval and similar governance | [Deep Research 7](../实战项目-深度研搜/7-中间件机制与Skills配置.md) |
| **Model Call Limit** | A cap on model calls | Controls cost and prevents infinite loops | [Deep Research 7](../实战项目-深度研搜/7-中间件机制与Skills配置.md) |
| **Tool Call Limit** | A cap on tool calls | Prevents repeated tool calls from creating cost or risk | [Deep Research 7](../实战项目-深度研搜/7-中间件机制与Skills配置.md) |
| **HITL** | Human In The Loop | Pauses high-risk actions to wait for a human to approve, edit or reject | [Deep Research 5](../实战项目-深度研搜/5-人机协作与中断恢复.md) |
| **SKILL.md** | A Skill's description file | Usually contains name, description, execution rules and resource notes | [27](../27-Skills技能与AI编程工具实践.md), [Deep Research 7](../实战项目-深度研搜/7-中间件机制与Skills配置.md) |
| **Progressive disclosure** | Read Skill metadata first, then load the full description on demand | Avoids stuffing every skill's content into context at once | [27](../27-Skills技能与AI编程工具实践.md), [Deep Research 7](../实战项目-深度研搜/7-中间件机制与Skills配置.md) |
| **Thinking Loop** | The main agent's thinking loop | Plans, dispatches, collects results, then judges whether to continue | [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |
| **RAGFlow assistant** | A subagent that queries the enterprise internal knowledge base | Not the RAGFlow platform itself, but an agent wrapper around the platform's capabilities | [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |

---

## 13. Shopkeeper Data Q&A project terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| ------------------ | ------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Shopkeeper Data Q&A** | A project for querying business data in natural language | The user asks a business question, the system generates and executes SQL, and returns data results | [Data Q&A 1](../实战项目-电商问数/1-项目概述与数仓基础.md), [Data Q&A 10](../实战项目-电商问数/10-问数智能体总览与工作流骨架.md) |
| **Data warehouse** | An analysis-oriented collection of data | Not the same as an online business database; emphasizes analytical statistics and metric definitions | [Data Q&A 1](../实战项目-电商问数/1-项目概述与数仓基础.md) |
| **Metadata** | Data that describes data | Such as table names, field names, field meanings and metric definitions | [Data Q&A 7](../实战项目-电商问数/7-元数据知识库总览与构建入口.md) |
| **Metadata knowledge base** | A knowledge base holding tables, fields, metrics and similar information | Helps the model understand the database structure and reduces guesswork when generating SQL | [Data Q&A 7](../实战项目-电商问数/7-元数据知识库总览与构建入口.md) |
| **Metric** | A business statistical definition | Such as sales amount, order count and conversion rate — you cannot just guess from a field name | [Data Q&A 7](../实战项目-电商问数/7-元数据知识库总览与构建入口.md) |
| **Field-value retrieval** | Looking up typical or candidate values in a field | Helps the model understand where values like "North China" or "women's wear" should map to | [Data Q&A 11](../实战项目-电商问数/11-关键词抽取与多路召回.md) |
| **Multi-route retrieval** | Finding context from several sources at once | Fields, metrics and field values can be retrieved in parallel and then merged | [Data Q&A 11](../实战项目-电商问数/11-关键词抽取与多路召回.md), [Data Q&A 12](../实战项目-电商问数/12-召回信息合并与上下文构建.md) |
| **SQL generation context** | The material assembled before asking the model to generate SQL | Includes table structures, field meanings, metric definitions and filter conditions | [Data Q&A 13](../实战项目-电商问数/13-SQL生成前的信息过滤与补全.md) |
| **SQL validation** | Checking before execution whether SQL is safe, legal and runnable | Prevents wrong or dangerous SQL from being executed directly | [Data Q&A 14](../实战项目-电商问数/14-SQL生成与执行闭环.md) |
| **SQL correction** | Fixing SQL based on validation errors | Forms a "generate, validate, correct, execute" loop for queries | [Data Q&A 14](../实战项目-电商问数/14-SQL生成与执行闭环.md) |
| **QueryService** | A query service wrapper layer | Connects the API, the LangGraph workflow and dependency assembly | [Data Q&A 16](../实战项目-电商问数/16-查询接口实现与依赖组装.md) |
| **request_id** | A request tracing ID | Used to string together the logs of a single API request | [Data Q&A 17](../实战项目-电商问数/17-前后端联调与日志追踪.md) |

---

## 14. Engineering and delivery terms

| Term | One-line explanation | Problem it solves / confusion point | Suggested reading |
| ------------------------- | ---------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Idempotency** | Repeated execution produces no extra side effects | Especially important for Tools that delete, charge, send messages or write to a database | [17](../17-Tools工具调用.md) |
| **Side effect** | An action that genuinely changes the outside world | Such as sending a message, placing an order, changing a database or writing a file | [17](../17-Tools工具调用.md) |
| **Timeout** | Give up waiting once a time limit is exceeded | Needs consideration for tools, model calls and platform workflows | [11](../11-Model-I-O与模型接入.md), [17](../17-Tools工具调用.md) |
| **Retry** | Trying again after a failure | Not every error deserves a retry; be especially careful in scenarios with side effects | [17](../17-Tools工具调用.md), [Deep Research 7](../实战项目-深度研搜/7-中间件机制与Skills配置.md) |
| **Rate limiting** | Controlling call frequency | Both a stability concern and a cost concern | [17](../17-Tools工具调用.md) |
| **Authentication** | Confirming who you are | Such as API Key, Token or login state | [4](../4-Python调用Dify平台工作流.md), [20](../20-MCP模型上下文协议.md) |
| **Authorization** | Confirming what you are allowed to do | Do not lump it together with authentication | [20](../20-MCP模型上下文协议.md) |
| **Least privilege** | Only exposing the capability required to finish the task | Critical for Tools, MCP and enterprise deployment | [17](../17-Tools工具调用.md), [20](../20-MCP模型上下文协议.md) |
| **Observability** | Making a running system traceable and diagnosable | Especially important in complex agent and LangGraph scenarios | [25](../25-LangGraph高级特性.md), [Data Q&A 17](../实战项目-电商问数/17-前后端联调与日志追踪.md) |
| **Logging** | Recording what the system does as it executes | The first entry point for debugging and operations | [Data Q&A 17](../实战项目-电商问数/17-前后端联调与日志追踪.md) |
| **Evaluation loop** | Continuously validating system quality with data and metrics | RAG, agents and prompts cannot be judged on subjective feeling alone | [19](../19-RAG检索增强生成.md), [21](../21-Agent智能体.md) |
| **FastAPI** | A Python web API framework | Commonly used to expose AI capability as HTTP endpoints | [Data Q&A 15](../实战项目-电商问数/15-API接口基础与FastAPI入门.md), [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |
| **SSE** | Server-Sent Events | Suited to one-way streaming results pushed from server to browser | [Data Q&A 15](../实战项目-电商问数/15-API接口基础与FastAPI入门.md) |
| **WebSocket** | A two-way real-time communication protocol | Suited to real-time frontend-backend interaction and progress push | [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |
| **ContextVar** | A Python coroutine-level context variable | Suited to isolating context such as request_id and thread_id in FastAPI async requests | [Data Q&A 17](../实战项目-电商问数/17-前后端联调与日志追踪.md), [Deep Research 8](../实战项目-深度研搜/8-项目总览与工程初始化.md) |
| **Dependency injection** | Handing dependency objects to a framework or service to assemble | Reduces module coupling and makes testing and substitution easier | [Data Q&A 16](../实战项目-电商问数/16-查询接口实现与依赖组装.md) |
| **Lifespan event** | Initialization or cleanup logic on application start and shutdown | Commonly used to create connection pools, load resources and close connections | [Data Q&A 15](../实战项目-电商问数/15-API接口基础与FastAPI入门.md) |

---

## 15. The most easily confused concepts, side by side

### 15.1 RAG vs fine-tuning vs continued pre-training

- **RAG**: supplements external knowledge at runtime without changing model parameters.
- **Fine-tuning**: changes behaviour, format, style and task habits.
- **Continued pre-training**: fills in a deeper domain knowledge distribution, usually at a higher cost.

One-line test: **Missing material → think RAG first. Missing behaviour → look at fine-tuning. Only when the underlying knowledge distribution itself is wrong should you consider continued pre-training.**

### 15.2 Workflow vs Agent

- **Workflow**: the process is designed by people; the model only completes subtasks at predefined positions.
- **Agent**: the model participates in deciding what to do next.

One-line test: **Fixed path → prefer Workflow. Open path → consider an Agent.**

### 15.3 Tool / Function Calling vs MCP

- **Tool / Function Calling**: how a model expresses "I want to call this tool".
- **MCP**: how an external capability is exposed in a standardized way.

One-line test: **One is about the calling mechanism, the other is about the integration protocol.**

### 15.4 MCP vs A2A

- **MCP**: lets a model connect to external tools, resources and prompt templates.
- **A2A**: lets different agents or agent systems collaborate with each other.

One-line test: **One connects capabilities, the other connects another agent.**

### 15.5 LangChain vs LangGraph

- **LangChain**: a wrapping layer for components, models, prompts, parsers, tools and agents.
- **LangGraph**: a layer for graph orchestration, state flow, persistence, recovery and observation.

One-line test: **LangChain is more about assembling capabilities; LangGraph is more about running a process.**

### 15.6 Conversation history vs memory vs Checkpoint

- **Conversation history**: the messages themselves.
- **Memory**: the system's ability to make use of history.
- **Checkpoint**: a snapshot of state during one execution.

One-line test: **History is content, memory is capability, and a checkpoint is a state-saving mechanism.**

### 15.7 Subagent vs Skill

- **Subagent**: a specialist assistant that the main agent can dispatch.
- **Skill**: a reusable set of descriptions, prompts, scripts and resources.

One-line test: **A Subagent is more like a person; a Skill is more like a toolkit.**

### 15.8 Backend vs Checkpointer vs Store

- **Backend**: in DeepAgents, a unified abstraction over files, state and long-term storage.
- **Checkpointer**: saves execution state snapshots so they can be restored.
- **Store**: saves long-term data across threads and sessions.

One-line test: **Backend is the abstraction layer, Checkpointer handles recovery, and Store handles long-term data.**

### 15.9 SSE vs WebSocket

- **SSE**: the server keeps pushing messages to the frontend; the browser mainly receives.
- **WebSocket**: frontend and backend can communicate in both directions in real time.

One-line test: **If you only need server push, SSE is lighter. If you need two-way real-time interaction, WebSocket fits better.**

---

## 16. Acronym quick reference

| Acronym | Full name | Meaning |
| --------- | ------------------------------------------ | ---------------------- |
| **LLM** | Large Language Model | Large language model |
| **AIGC** | AI Generated Content | AI-generated content |
| **AGI** | Artificial General Intelligence | Artificial general intelligence |
| **SFT** | Supervised Fine-Tuning | Supervised fine-tuning |
| **RLHF** | Reinforcement Learning from Human Feedback | Reinforcement learning from human feedback |
| **RLAIF** | Reinforcement Learning from AI Feedback | Reinforcement learning from AI feedback |
| **LoRA** | Low-Rank Adaptation | Low-rank adaptation fine-tuning |
| **RAG** | Retrieval-Augmented Generation | Retrieval-augmented generation |
| **LCEL** | LangChain Expression Language | LangChain expression language |
| **MCP** | Model Context Protocol | Model Context Protocol |
| **A2A** | Agent-to-Agent | Agent-to-agent communication or collaboration protocol |
| **HITL** | Human In The Loop | Human in the loop |
| **SSE** | Server-Sent Events | Server-sent events |
| **API** | Application Programming Interface | Application programming interface |
| **SDK** | Software Development Kit | Software development kit |
| **SQL** | Structured Query Language | Structured Query Language |
| **JSON** | JavaScript Object Notation | A commonly used structured data format |

---

> **Translator's note**: The "suggested reading" links in this glossary currently point to the original Chinese chapters, because the English chapters are still being translated. They will be repointed to the `en/` versions as those are published.
