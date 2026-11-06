# AI Agents and LLM Application Development Interview Question Bank

> Positioning: For **AI Agent / LLM Application Development Engineers**, **AI Application Development Engineers**, and **Agent Development Engineers**.  
> Style: Focuses on **application implementation, architecture design, engineering governance, and hands-on project experience**, rather than pure algorithm research or pre-training details.

> 🎉 **MianStack officially launched on November 6, 2026, free and open source!** The complete question bank, real interview experiences, stable question IDs, and review entry points have been migrated to [MianStack](https://mianstack.com/); the [GitHub open-source repository](https://github.com/didilili/mianstack) is open—welcome to Star, contribute, and correct errors. This document remains as a course companion compilation of 89 questions for convenient review by tutorial chapters.

Document features:

- Each question is tagged with **importance** and **difficulty**, making it easy to distinguish must-do, frequently tested, and advanced content.
- Where possible, the **corresponding chapter** is added below each question, making it easy to revisit knowledge points and learn while practicing.
- A considerable number of questions come from **real interview experiences at major companies** and actual high-frequency follow-up scenarios, closely matching real interviews.
- The overall expression maintains **professional yet readable language**, avoiding empty talk, boilerplate, and pure concept-stacking.
- Second-level headings are categorized by topic with a clear structure, making systematic review by module easy.

Importance tag explanation:

- `必刷`: Highly likely to be asked; a poor answer directly exposes weaknesses.
- `高频`: Very common in interviews, usually a main question or high-frequency follow-up.
- `中频`: More focused on engineering design, deep project exploration, and implementation details.
- `低频`: Bonus questions, extension questions, and role-specific deep-dive questions.

Difficulty tag explanation:

- `基础`: Focuses on conceptual foundations and standard answers, suitable for building a base in the first round.
- `中等`: Requires combining engineering understanding, layered expression, or some project experience.
- `较难`: More focused on system design, complex governance, protocol details, or advanced architectural trade-offs.

## 1. Fundamentals and Technology Selection

### Q1-1. What is the core difference between RAG and fine-tuning (SFT)? Can they be used together?

RAG solves the problem of "where knowledge comes from," while fine-tuning solves the problem of "how the model should behave."

RAG does not modify model parameters; instead, it retrieves relevant materials at runtime and then feeds them to the model to generate answers. This makes it more suitable for handling knowledge that is highly time-sensitive, frequently updated, or requires traceability. Fine-tuning does modify model parameters and is better suited for improving consistency of output style, structured output capabilities, classification abilities, or stability of domain-specific behavior.

They can certainly be used together, and many enterprise projects are implemented this way: RAG provides the knowledge, while fine-tuning or strong output constraints improve behavioral stability. For example, in a customer service project, product policies stay current through RAG, while reply format and field output are kept stable through fine-tuning or structured output.

**Common follow-ups:**

- Why don't most enterprise projects prioritize continued pre-training?
- What scenarios are suitable for a `RAG + 微调` combination?
- If the budget is limited, which one should you do first?

**Importance:** `必刷` (occurrences: 3 times) | **Difficulty:** `中等`

**Assessment points:** Ability to distinguish between knowledge enhancement and behavior optimization.

**Corresponding chapters:** [1-3 RAG, Fine-tuning, Continued Pre-training, and Agent Selection §1, RAG](1-3-RAG%E3%80%81%E5%BE%AE%E8%B0%83%E3%80%81%E7%BB%AD%E8%AE%AD%E4%B8%8E%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%89%E5%9E%8B.md#_1、rag); [1-3 RAG, Fine-tuning, Continued Pre-training, and Agent Selection §2, Fine-tuning](1-3-RAG%E3%80%81%E5%BE%AE%E8%B0%83%E3%80%81%E7%BB%AD%E8%AE%AD%E4%B8%8E%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%89%E5%9E%8B.md#_2、微调%EF%BC%88fine-tuning%EF%BC%89)

### Q1-2. What is an AI Agent? What is the difference between it and a traditional AI application?

It can be summarized as: **Agent = Model + Toolset + Execution Loop + Current State**.

- The model is responsible for understanding the goal and deciding the next step.
- The toolset provides external capabilities.
- The execution loop enables the system to do more than answer once—it can "think one step, act one step, observe the result, then decide the next step."
- The current state is responsible for storing messages, tool results, and intermediate conclusions.

Traditional AI applications are closer to a single-turn system of "input a request, return a result"; an Agent is closer to an operating mode of "continuously making decisions around a goal." Its key feature is not just using a large model, but having tool-calling, state advancement, and dynamic decision-making capabilities.

So not all AI applications should be called Agents. Systems with fixed form generation, fixed knowledge Q&A, or fixed process approval often only need a regular pipeline or Workflow. An Agent is truly appropriate only when the path is not fixed and the system needs to continue selecting tools or adjusting the route based on intermediate results.

Also note that many people treat "long-term memory, complex planning, multi-agent collaboration" as prerequisites for an Agent—that is not the case. For many entry-level scenarios, being able to "understand the goal, decide whether to call a tool, get the result, and continue judging" is already an Agent.

**Importance:** `高频` (occurrences: 2 times) | **Difficulty:** `基础`

**Assessment points:** Whether you understand the essence of an Agent and won't call any chatbot an Agent.

**Corresponding chapters:** [21 Agent §1, Agent Introduction](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_1-introduction-to-agents); [1-3 RAG, Fine-tuning, Continued Pre-training, and Agent Selection §4, Agent Development](1-3-RAG%E3%80%81%E5%BE%AE%E8%B0%83%E3%80%81%E7%BB%AD%E8%AE%AD%E4%B8%8E%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%89%E5%9E%8B.md#_4、智能体开发)

### Q1-3. When should you use Prompt, RAG, Fine-tuning, Workflow, or Agent?

The most reliable way to decide is to first determine whether the problem is **lacking knowledge, lacking behavior, or lacking process capability**.

- If the model already knows the answer but the task is not clearly described, start with Prompt.
- If what's missing is private knowledge, up-to-date knowledge, or external knowledge, prioritize RAG.
- If what's missing is stable behavior, such as fixed format, fixed tone, or fixed classification habits, then consider fine-tuning.
- If the process is fixed, nodes are clear, and stability and auditability are emphasized, prioritize Workflow.
- If the path is not fixed and the system needs to decide the next step while working and dynamically call tools, then consider an Agent.

This selection framework can be compressed into one sentence:

- **Prompt** solves the task expression problem.
- **RAG** solves the knowledge source problem.
- **Fine-tuning** solves the behavioral stability problem.
- **Workflow** solves the fixed process problem.
- **Agent** solves the dynamic decision-making problem.

In real projects, you usually won't start by saying "we must build an Agent." Most requirements can first be covered with `Prompt + RAG + Workflow`; only when the task openness is high, tool selection depends on intermediate results, and the process cannot be hardcoded in advance does the value of an Agent truly emerge.

**Common follow-ups:**

- Why don't many projects start with fine-tuning?
- Why aren't all complex tasks suitable for Agents?
- What is the dividing line between Workflow and Agent?

**Importance:** `必刷` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment points:** Technology selection ability, boundary awareness, and engineering judgment.

**Corresponding chapters:** [1-3 RAG, Fine-tuning, Continued Pre-training, and Agent Selection §1, RAG](1-3-RAG%E3%80%81%E5%BE%AE%E8%B0%83%E3%80%81%E7%BB%AD%E8%AE%AD%E4%B8%8E%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%89%E5%9E%8B.md#_1、rag); [1-3 RAG, Fine-tuning, Continued Pre-training, and Agent Selection §4, Agent Development](1-3-RAG%E3%80%81%E5%BE%AE%E8%B0%83%E3%80%81%E7%BB%AD%E8%AE%AD%E4%B8%8E%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%89%E5%9E%8B.md#_4、智能体开发)

### Q1-4. What are tokens and context windows? What do they mean from an engineering perspective?

A token can be viewed as the basic unit of measurement for text processed by the model; it is not equal to "character count" or "word count." During training and inference, the model does not see raw text but rather a sequence of tokens produced by the tokenizer.

The context window is the upper limit on how many tokens the model can see in a single inference pass. What engineers often refer to as `8K`, `32K`, or `128K` essentially means "the maximum number of tokens that can be packed into this request when system prompts, conversation history, retrieval results, and the user question are combined."

Its engineering implications are very direct:

- The context window determines whether you can do long-document Q&A, multi-turn dialogue, and large-scale RAG context concatenation.
- More tokens usually mean higher cost and are more likely to increase latency.
- Content exceeding the window will be truncated, compressed, or simply never reach the model, so "more is not always better."

As a rough reference, `128K token` can be considered a very long piece of content. By common rules of thumb, one Chinese character is approximately `0.6` tokens, and one English character is approximately `0.3` tokens, so `128K token` can be roughly approximated as on the order of two hundred thousand Chinese characters. But this is only an estimate; real numbers vary depending on the tokenizer, language type, code, punctuation, and formatting.

**Common follow-ups:**

- Roughly how many tokens are one Chinese character or one English word, and why can't you memorize a fixed value?
- If the context gets truncated, what would you prioritize doing?

**Importance:** `高频` (occurrences: 1 time) | **Difficulty:** `基础`

**Assessment points:** Whether you truly understand the relationship between tokens, context windows, and cost/truncation/long-text scenarios.

**Corresponding chapters:** [1-1 LLM Fundamentals and Engineering Overview §1, Understanding Large Models](1-1-%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%A4%E7%9F%A5%E4%B8%8E%E5%B7%A5%E7%A8%8B%E6%A6%82%E8%A7%88.md#_1-getting-to-know-llms); [11 Model I/O and Model Integration §2, LangChain Model Types, Parameters, and Outputs](11-Model-I-O%E4%B8%8E%E6%A8%A1%E5%9E%8B%E6%8E%A5%E5%85%A5.md#_2-langchain-model-categories-parameters-and-returns)

**Source:** Tencent AI Backend Engineer First Round (actual major-company interview question)

### Q1-5. What engineering metrics do you care about most before launching an LLM application?

I typically look at five dimensions: effectiveness, performance, cost, stability, and governance.

- Effectiveness: accuracy, faithfulness, task completion rate, citation correctness.
- Performance: first-token latency, end-to-end latency, P95/P99.
- Cost: token consumption, retrieval cost, tool-calling cost.
- Stability: timeout rate, error rate, retry rate, fallback hit rate.
- Governance: logs, traces, Prompt versions, index versions, permission auditing.

If it is a RAG / Agent project, I also pay extra attention to retrieval recall quality, tool-calling success rate, manual fallback ratio, and badcase feedback efficiency, because these are the key metrics that truly affect the online experience.

**Common follow-ups:**

- How do you design a fallback strategy?
- If costs exceed the budget, which layer do you optimize first?
- How do you do Prompt / model / index rollbacks?

**Importance:** `高频` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment points:** Whether you have production-environment awareness.

**Corresponding chapters:** [1-1 LLM Fundamentals and Engineering Overview §4, LLM Engineering Implementation (Overview)](1-1-%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%A4%E7%9F%A5%E4%B8%8E%E5%B7%A5%E7%A8%8B%E6%A6%82%E8%A7%88.md#_4、大模型的工程实现%EF%BC%88概览%EF%BC%89); [7 Enterprise-level LLM Deployment §1, Enterprise-level LLM Deployment Overview](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_1-overview-of-enterprise-level-large-model-deployment)

---

## 2. Prompt, Structured Output, and Guardrails

### Q2-1. How should System Message and User Message be divided?

System Message is responsible for holding stable constraints, while User Message is responsible for holding dynamic tasks.

System typically contains the role, goals, boundaries, safety rules, output format requirements, and tool usage specifications—these should be as stable as possible and rarely changed. User Message contains the user's current task, input data, supplementary context, and personalized requirements.

The benefit of this separation is clearer structure, easier version management, and better suitability for subsequent templating, canary release, and evaluation. If all content is mixed into a single prompt, it becomes very difficult to troubleshoot performance fluctuations later.

**Importance:** `必刷` (Occurrences: 1) | **Difficulty:** `基础`

**Assessment Focus:** Ability to design layered prompts.

**Corresponding Sections:** [13 Prompt and Message Templates §3, Input Message Types](13-%E6%8F%90%E7%A4%BA%E8%AF%8D%E4%B8%8E%E6%B6%88%E6%81%AF%E6%A8%A1%E6%9D%BF.md#_3-message-types-for-input); [13 Prompt and Message Templates §7, Chat Prompt Templates (ChatPromptTemplate)](13-%E6%8F%90%E7%A4%BA%E8%AF%8D%E4%B8%8E%E6%B6%88%E6%81%AF%E6%A8%A1%E6%9D%BF.md#_7-chat-prompt-template-chatprompttemplate)

### Q2-2. What are common approaches to structured output? What are their respective pros and cons?

From the Model I/O perspective, structured output can roughly be divided into two categories: "post-processing parsing" and "pre-constrained structured output."

- Pure prompt constraints: directly require the model to return JSON. The advantage is that it is the simplest and quickest to start; the disadvantage is that if the model says one extra word or omits a comma, the program easily breaks, making it the least stable.
- Output Parser: for example `StrOutputParser`, `JsonOutputParser`, `PydanticOutputParser`. It is closer to "the model has already produced output, and I convert the result into program-usable data," suitable for the classic `prompt | model | parser` chain.
- Structured Output: for example `with_structured_output(TypedDict / Pydantic / JSON Schema)`. It is closer to "defining the schema before the model outputs," so the model generates according to the structure and automatically parses it, providing stronger constraints.
- Function Calling / Tool Calling: essentially also a form of structured output, but the goal leans more toward "generating calling intent and parameters," especially suitable for tool invocation, external interface orchestration, and Agents.

If the model platform supports stricter structured output capabilities, the mode that only guarantees "returning valid JSON" is usually preferred, because the former is closer to "generation according to schema," while the latter is often only "JSON-shaped."

If we break it down further:

- `TypedDict` is suitable for scenarios where fields are fixed but strong runtime validation is not required.
- `Pydantic` is suitable for business scenarios with strict field types, ranges, and required fields.
- `JSON Schema` is more suitable for sharing structural protocols across languages and systems.

In engineering practice, "making the model output JSON" is usually not considered a real production solution. A more stable order is usually:

1. Prefer native structured output when available.
2. Prefer Pydantic-style schemas when strong validation is needed.
3. Even if the model already produces structured output, still add business validation, default value handling, and retry on failure.

Ultimately, prompts can only "try to make it look like this," while Parsers and Structured Output are what really help you integrate model output into your program system.

**Importance:** `高频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment Focus:** Engineering awareness of moving from "being able to output JSON" to "being able to connect to the system stably."

**Corresponding Sections:** [14 Output Parsers §1, Introduction to Output Parsers](14-%E8%BE%93%E5%87%BA%E8%A7%A3%E6%9E%90%E5%99%A8.md#_1-introduction-to-output-parsers); [14 Output Parsers §4, Structured Output](14-%E8%BE%93%E5%87%BA%E8%A7%A3%E6%9E%90%E5%99%A8.md#_4-structured-output)

### Q2-3. What is Prompt Injection? Why should you be especially careful in RAG / Agent scenarios?

Prompt Injection is essentially: **untrusted input attempting to rewrite system instructions, induce the model to exceed its authority, or make the Agent execute actions it should not execute.**

It does not only come from direct user input; it can also hide in web pages, PDFs, knowledge base documents, emails, or even images. As long as these contents can be read by the model, "indirect injection" may occur. Therefore, in systems that read external content, such as RAG, browser Agents, and code interpreters, the risk is significantly higher.

Defense is usually implemented at five layers:

- Layered instructions: put stable rules in System, treat User and external documents as untrusted input, and do not give them the same authority as system constraints.
- Content isolation: treat retrieved snippets, web content, and user-uploaded documents only as "material to be analyzed," and do not assume by default that they can issue new instructions.
- Tool permissions: all write operations and dangerous operations go through whitelists, schema validation, and least privilege, so the model does not get raw capabilities.
- Action validation: perform rule validation on critical outputs, and require confirmation, approval, or HITL for critical actions, so a single malicious sentence cannot directly trigger side effects.
- Observability and fallback: record injection samples, failure trajectories, and abnormal calls, and add them to evaluation sets and interception rules in a timely manner.

There is a particularly critical point here: **RAG is not a security layer, and knowledge base documents themselves may contain malicious instructions.** As long as "retrieved content" is directly treated as "trusted prompts," the system is in great danger.

**Common Follow-up Questions:**

- If a document says "ignore all previous instructions," how would you handle it?
- How does a browser Agent defend against hidden prompts in web pages?
- Why cannot fine-tuning and alignment fundamentally solve Prompt Injection?

**Importance:** `高频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment Focus:** Application-layer security awareness, and understanding of the risks of direct injection, indirect injection, and tool privilege escalation.

**Corresponding Sections:** [13 Prompt and Message Templates §1, Introduction to Prompt](13-%E6%8F%90%E7%A4%BA%E8%AF%8D%E4%B8%8E%E6%B6%88%E6%81%AF%E6%A8%A1%E6%9D%BF.md#_1-introduction-to-prompts); [17 Tools and Tool Calling §6, From Course Examples to Real Projects](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_6-from-course-examples-to-real-projects)

### Q2-4. In Prompt Engineering, how do you systematically optimize prompts and improve accuracy?

Prompt optimization is usually not understood as "repeatedly hand-editing a few prompt sentences," but rather as a small engineering closed loop. The core of truly improving accuracy stably is not mysterious tricks, but **task decomposition, example-driven iteration, evaluation regression, and boundary convergence**.

A more reliable approach is usually:

- First define task boundaries: clarify what counts as a correct answer, what counts as a wrong answer, and which situations must be refused or clarified.
- Layer inputs: put stable rules in `System` and dynamic tasks in `User`, rather than squeezing all constraints into one long prompt.
- Fix major issues before wording: if the root problem is missing knowledge, missing tools, or missing processes, do not force the prompt to bear the entire burden.
- Use examples and counterexamples: few-shot examples, counterexample constraints, and output format examples are usually more stable than abstract requirements.
- Apply structural constraints: wherever schemas, parsers, and structured output can be used, do not just write "please return JSON."
- Build a badcase set: turn online errors into a fixed evaluation set, and run regression every time the prompt is changed, rather than relying on intuition that "it seems more accurate now."
- Manage versions and canary releases: manage the prompt, model version, temperature, and output format requirements together, so you do not change one thing without being able to trace the impact.

If expressed from a more practical interview perspective, one more sentence is needed: the so-called "accuracy > 95%" must be tied to a specific task, such as classification, extraction, format generation, or customer service Q&A; it is not a universal promised number. The real engineering goal should be for a specific task to stably meet the standard on a fixed evaluation set, rather than chasing a number detached from the scenario.

**Common Follow-up Questions:**

- If the prompt cannot be improved no matter how you change it, how do you decide whether to switch to RAG, Tool, Workflow, or fine-tuning?
- How should a badcase set be built so that it can truly guide iteration?
- If online performance suddenly drops, how do you determine whether it is a prompt problem, a model version problem, or a problem in the external knowledge / tool pipeline?

**Importance:** `高频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment Focus:** Prompt optimization methodology, awareness of evaluation closed loops, and knowing that prompts are not a universal repair tool.

**Corresponding Sections:** [1-2 Prompt Engineering Basics §2, How to Write Prompts](1-2-%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80.md#_2-how-to-write-prompts); [14 Output Parsers §8, Practical Development Choices](14-%E8%BE%93%E5%87%BA%E8%A7%A3%E6%9E%90%E5%99%A8.md#_8-practical-development-choices)

### Q2-5. What are the boundaries of Prompt Engineering? Why can't all problems be left to prompts?

Prompts are closer to a "means of task expression and constraint," but they cannot solve the problems of missing knowledge, complex state management, or strong execution requirements.

For example, when there is too much material, relying only on prompts to stuff the context will cause high cost, more noise, and loss of key information; in this case, you should switch to RAG. If a multi-step complex process is entirely orchestrated through prompts, it will become an unmaintainable long instruction set and should be converted to Workflow or LangGraph. When stable external system calls are needed, you should use Tools / Function Calling rather than letting the model "pretend to call an interface" in text.

Therefore, a more reasonable engineering approach is: prompts handle rule expression, RAG supplements knowledge, Tools provide execution capability, and Graph / Workflow handles process control.

**Importance:** `中频` (Occurrences: 1) | **Difficulty:** `基础`

**Assessment Focus:** Understanding that prompts are not a cure-all.

**Corresponding Sections:** [1-2 Prompt Engineering Basics §4, Boundaries of Prompt Engineering](1-2-%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80.md#_4、提示词工程的边界); [13 Prompt and Message Templates §1, Introduction to Prompt](13-%E6%8F%90%E7%A4%BA%E8%AF%8D%E4%B8%8E%E6%B6%88%E6%81%AF%E6%A8%A1%E6%9D%BF.md#_1-introduction-to-prompts)

### Q2-6. How do you manage prompt versions and regression?

If a prompt has already entered a production environment, it can no longer be treated as a "temporarily edited string" but should be managed as a configuration asset or code asset.

Four things are usually managed at the same time:

- The prompt template itself: System, User templates, few-shot examples, and output format requirements.
- Runtime parameters: model name, model version, temperature, top_p, max_tokens.
- Evaluation set: fixed golden questions, typical badcases, and failure samples.
- Release information: template version number, release time, owner, canary scope, and rollback version.

A more reliable approach is usually:

1. Version the prompt together with the code, or manage it centrally in a configuration center.
2. Run a fixed regression set every time the prompt is changed, not just relying on subjective feeling.
3. Record the template hash, model version, and key parameters so that if "the prompt was not changed but the performance changed," the cause can still be traced.
4. Perform canary release and sampled manual review before going live, and retain rapid rollback capability for high-risk pipelines.

There is another easily overlooked point: **after switching the underlying model, the old prompt may no longer maintain its original performance.** Therefore, in many cases the target of regression is not "whether this prompt is correct," but "whether the combination of the prompt and the current model is still stable."

**Common Follow-up Questions:**

- How should a golden set be constructed?
- If online performance fluctuates, how do you determine whether it is a prompt problem or a model version problem?
- When prompts, models, and indexes are changed together, how do you design a rollback strategy?

**Importance:** `中频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment Focus:** Prompt engineering governance capability, not just hand-editing prompts.

**Corresponding Sections:** [13 Prompt and Message Templates §8, Loading Prompts from Files](13-%E6%8F%90%E7%A4%BA%E8%AF%8D%E4%B8%8E%E6%B6%88%E6%81%AF%E6%A8%A1%E6%9D%BF.md#_8-loading-prompts-from-files); [1-2 Prompt Engineering Basics §5, Several Considerations for Prompt Engineering](1-2-%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B%E5%9F%BA%E7%A1%80.md#_5、提示词工程的几个注意点)

---

## 3. Full RAG Pipeline

### Q3-1. Please describe a complete RAG pipeline.

A complete RAG is generally divided into the **indexing stage** and the **retrieval stage**.

The indexing stage consists of document loading, cleaning, chunking, vectorization, writing to the vector database, and adding metadata. The retrieval stage consists of receiving the question, performing query rewriting when necessary, retrieval recall, reranking and filtering, context assembly, handing it to the model to generate an answer, and finally performing citation, desensitization, and formatted output.

In engineering practice, the real difficulty is usually not "connecting the models," but three things: whether documents are parsed correctly, whether chunking preserves semantics, and whether retrieval results are actually helpful for the current question. Poor online performance is most often stuck at these three layers, rather than at the final generation step.

**Common Follow-up Questions:**

- How should chunks be divided?
- What fields should metadata store?
- Why add rerank?

**Importance:** `必刷` (occurrences: 3) | **Difficulty:** `中等`

**Assessment focus:** Whether you truly understand RAG, rather than just being able to say "retrieval-augmented generation."

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §1. Introduction to RAG](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_1-introduction-to-rag); [19 RAG Retrieval-Augmented Generation §2. Core Knowledge of RAG Text Processing](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_2-core-knowledge-of-rag-text-processing)

### Q3-2. How should text chunking be designed? What are the common pitfalls?

The goal of chunking is not to "divide evenly," but to "preserve semantic units that are meaningful for retrieval as much as possible."

Usually, fixed length, paragraph boundaries, heading hierarchy, and overlapping windows are combined in the design. If chunks are too large, there will be more noise and inaccurate matching; if too small, context is lost, and retrieval results cannot support answering. For manuals, FAQs, policy documents, and mixed text-and-image PDFs, these documents often cannot simply be split by character count; layout structure, headings, tables, and semantic boundaries must also be considered.

Common pitfalls include: chunks that are too fragmented, ignoring heading hierarchy, insufficient overlap, dirty raw OCR text that is not cleaned, table content being broken apart, and cramming multiple topics into one chunk, which causes vector semantic pollution.

**Importance:** `高频` (occurrences: 3) | **Difficulty:** `中等`

**Assessment focus:** Whether your RAG fundamentals are solid.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §2. Core Knowledge of RAG Text Processing](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_2-core-knowledge-of-rag-text-processing); [2-RAG Building Enterprise Private & Personal Knowledge Bases §2. Overview of Knowledge Bases](2-RAG-%E6%90%AD%E5%BB%BA%E4%BC%81%E4%B8%9A%E7%A7%81%E6%9C%89&%E4%B8%AA%E4%BA%BA%E7%9F%A5%E8%AF%86%E5%BA%93.md#_2-overview-of-knowledge-bases)

### Q3-3. When RAG does not perform well, how do you troubleshoot it?

Troubleshooting can be expanded into three layers: "before retrieval, during retrieval, and after retrieval."

- Before retrieval: Check whether the query is clearly expressed and whether it needs rewriting, decomposition, or additional context.
- During retrieval: Check whether chunking, embedding, vector database index parameters, top_k, filtering conditions, and reranking are reasonable.
- After retrieval: Check whether the context assembled for the model is too long, whether there is noise, whether key information is being drowned out, and whether the generation prompt requires refusing to answer when there is no basis.

For enterprise knowledge bases, you must also check document quality, whether versions are up to date, and whether permission filtering is mistakenly blocking relevant content. Many of the problems described as "the model is not smart enough" can ultimately be traced to dirty document parsing, chunks that are too small, noisy recall, or poor context assembly.

**Common follow-up questions:**

- Is a larger top_k always better?
- How do you identify whether the problem is in recall or generation?
- What is Lost in the Middle?

**Importance:** `必刷` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Troubleshooting ability and whether the approach to locating problems is layered.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §2. Core Knowledge of RAG Text Processing](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_2-core-knowledge-of-rag-text-processing); [19 RAG Retrieval-Augmented Generation §3. Comprehensive RAG Case Study: Intelligent Operations Assistant](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_3-comprehensive-rag-case-intelligent-operations-assistant)

### Q3-4. What problems do hybrid retrieval, reranking, and query rewriting solve respectively?

These three solve problems at three different levels.

- Query rewriting solves the problem that the user's question does not look enough like a retrieval query.
- Hybrid retrieval solves the problem that relying only on dense vectors may miss keyword matches.
- Reranking solves the problem that a batch of candidates has been recalled, but the order is still not accurate enough.

In real projects, especially for knowledge such as policies, product parameters, order fields, and error codes, keywords are often very important, so dense retrieval alone is often insufficient. A relatively stable solution is usually "query rewriting + dense retrieval + sparse retrieval + rerank," combined with metadata filtering for final narrowing.

**Common follow-up questions:**

- What is the difference between dense retrieval and sparse retrieval?
- At which layer is it most appropriate to place reranking?
- Will hybrid retrieval be more expensive?

**Importance:** `高频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Whether you understand the division of responsibilities in retrieval optimization.

**Corresponding sections:** [18 Vector Databases and Embedding in Practice §6. Writing to and Retrieving from Vector Databases](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_6-writing-to-and-retrieving-from-a-vector-database-rags-underlying-capability); [19 RAG Retrieval-Augmented Generation §2. Core Knowledge of RAG Text Processing](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_2-core-knowledge-of-rag-text-processing)

### Q3-5. How should RAG be integrated into an Agent execution pipeline?

Integrating RAG into an Agent should not be understood only as "search the material first and then answer." A more stable approach is usually to make the retrieval capability a component that the Agent can call on demand.

There are three common integration patterns:

- Pre-retrieval: As soon as the user's question comes in, retrieval is performed uniformly first, and then the evidence is handed to the Agent for further planning.
- On-demand retrieval: Wrap the Retriever / Search as a tool, and the Agent actively calls it when factual evidence is needed.
- Post-generation verification: Generate the result first, and then use retrieval for evidence verification or citation completion.

In real projects, "on-demand retrieval as the main approach, with pre-retrieval as a supplement" is usually more recommended. This is because not every step requires querying the knowledge base; some steps involve planning, routing, parameter confirmation, or tool execution. Making RAG a callable capability can reduce ineffective retrieval and is also more suitable for multi-step tasks. Post-generation verification can be used as enhancement, but it is usually not suitable as the main pipeline, because it increases latency, and if the earlier steps have already gone off track, the cost of later verification and correction will be higher.

**Common follow-up questions:**

- Are you familiar with multiple retrievals during generation, adaptive retrieval, or Agentic RAG? What is the difference between that and "retrieve once, then generate"?
- Under what circumstances should you upgrade from "single retrieval" to "multi-round retrieval + mid-process supplementary retrieval"?

**Importance:** `高频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Whether you understand how Agentic RAG is integrated, rather than only treating RAG as a fixed pre-processing pipeline.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §1. Introduction to RAG](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_1-introduction-to-rag); [21 Agent §6. Summary: Differences and Connections Among Agent, Tool, Function Calling, RAG, and MCP](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_6-summary-differences-and-relationships-among-agent-tool-function-calling-rag-and-mcp)

### Q3-6. Why must enterprise RAG projects pay attention to permissions, versions, and citations?

Because enterprise knowledge is not just about "being able to find it"; it is about "finding the right information, within the right permission scope, and being able to trace the source."

For permissions, vector retrieval must implement tenant isolation, role filtering, and document-level or paragraph-level permission control. Security cannot be left to the model's "self-discipline in not answering." For versions, the index and source documents must be traceable, and after document updates, you must know which vectors require incremental rebuilding. For citations, if answers cannot be traced back to original text fragments, it is difficult for business stakeholders to build trust, and it is also not conducive to auditing and review.

Therefore, in an enterprise, RAG is not only a retrieval effectiveness issue; it is also a data governance issue.

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Enterprise implementation awareness, not just staying at the demo stage.

**Corresponding sections:** [2-RAG Building Enterprise Private & Personal Knowledge Bases §2. Overview of Knowledge Bases](2-RAG-%E6%90%AD%E5%BB%BA%E4%BC%81%E4%B8%9A%E7%A7%81%E6%9C%89&%E4%B8%AA%E4%BA%BA%E7%9F%A5%E8%AF%86%E5%BA%93.md#_2-overview-of-knowledge-bases); [19 RAG Retrieval-Augmented Generation §3. Comprehensive RAG Case Study: Intelligent Operations Assistant](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_3-comprehensive-rag-case-intelligent-operations-assistant)

### Q3-7. What is Lost in the Middle? What implications does it have for RAG design?

Lost in the Middle refers to the phenomenon that when the context becomes long, models tend to make better use of information at the beginning and end, while key evidence in the middle is "seen but not effectively used."

Its implication for RAG is very direct: stuffing more chunks into the context is not necessarily better. If there is too much noise in the middle, the truly critical evidence is more likely to be drowned out.

Therefore, in engineering practice, the following approaches are usually adopted:

- Perform reranking and filtering first, and then decide what is allowed into the context.
- Minimize low-value fragments as much as possible; do not stuff everything that is "possibly relevant" into the context.
- Put important evidence near the front, and add summaries or lead with conclusions when necessary.
- For complex problems, use staged retrieval rather than dumping a large amount of material into the context all at once.

In summary: **Long context does not equal high-quality context. The core of RAG is still "placing the most useful evidence in the position where the model can use it most easily."**

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Understanding of long contexts, and awareness of the interplay among retrieval, reranking, and context assembly.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §2. Core Knowledge of RAG Text Processing](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_2-core-knowledge-of-rag-text-processing); [19 RAG Retrieval-Augmented Generation §3. Comprehensive RAG Case Study: Intelligent Operations Assistant](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_3-comprehensive-rag-case-intelligent-operations-assistant)

### Q3-8. With ultra-long-context models, is RAG still needed?

In most scenarios, it is still needed, because "being able to fit it in" and "should fit it in" are entirely different matters.

Ultra-long-context models do make long-document understanding and reasoning over a small number of documents more convenient, but in enterprise scenarios, the more common problem is not that "the model's context window is not big enough," but rather:

- The total amount of knowledge is too large to fit everything in every time.
- Long context incurs higher cost and latency.
- Permission filtering, tenant isolation, and version control cannot be solved simply by cramming everything into the window.
- Auditing and citation tracing are more suitable when handled through the retrieval pipeline.

Therefore, a more reasonable understanding is usually: **Long context expands the range that can be processed, but it does not eliminate the value of retrieval.** It is more suitable for analyzing a small number of long documents, context integration, and complex reasoning; RAG is more suitable for narrowing down massive knowledge, permission filtering, evidence citation, and continuous updating.

If compressed into one sentence, it can be summarized as: **Long context is not a replacement for RAG; it is closer to a complementary capability to RAG.**

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Whether you understand that "long-window capability" and "the value of a retrieval system" are not problems at the same level.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §1. Introduction to RAG](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_1-introduction-to-rag); [1-1 LLM Cognition and Engineering Overview §1. Understanding LLMs](1-1-%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%A4%E7%9F%A5%E4%B8%8E%E5%B7%A5%E7%A8%8B%E6%A6%82%E8%A7%88.md#_1-getting-to-know-llms)

### Q3-9. How should complex-document RAG or multimodal RAG be implemented?

The biggest pitfall in these scenarios is treating PDFs, scanned documents, tables, images, and web pages all as "ordinary plain text."

A more stable approach is usually to treat the parsing layer separately first:

- First perform layout analysis, OCR, table extraction, and heading hierarchy recovery, instead of chunking by character count from the beginning.
- Chunks should be divided by structural blocks as much as possible, such as headings, paragraphs, tables, and figure captions, rather than cutting a table into several incomplete pieces of text.
- Metadata should preserve page numbers, section headings, document version, source file, coordinates, or structural position information to facilitate citation and traceability.
- When querying, use multi-route retrieval when necessary, such as text retrieval, table retrieval, and image caption retrieval, then uniformly rerank and assemble the results.

For enterprise knowledge bases, complex-document RAG often affects the upper limit more than “model selection.” If parsing is wrong, tables are broken, or image-text correspondence is lost, even a much stronger downstream model can hardly make up for it.

**Common follow-up questions:**

- Why are many equipment manuals and institutional PDFs especially difficult for RAG?
- What is the relationship between OCR accuracy and final Q&A quality?
- When is multimodal RAG worth adopting, and when is plain text sufficient?

**Importance:** `中频` (appears 1 time) | **Difficulty:** `较难`

**Assessment focus:** Whether the candidate realizes RAG is not only a retrieval problem, but also involves document parsing, structure recovery, and citation tracking.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §2, Core Knowledge of RAG Text Processing](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_2-core-knowledge-of-rag-text-processing); [2-RAG for Building Enterprise Private & Personal Knowledge Bases §2, Overview of Knowledge Bases](2-RAG-%E6%90%AD%E5%BB%BA%E4%BC%81%E4%B8%9A%E7%A7%81%E6%9C%89&%E4%B8%AA%E4%BA%BA%E7%9F%A5%E8%AF%86%E5%BA%93.md#_2-overview-of-knowledge-bases)

### Q3-10. What is Agentic RAG? How does it differ from “retrieve once and then generate directly”?

Traditional RAG is closer to a fixed pipeline: retrieve once, then hand the results to the model to generate an answer. Agentic RAG is closer to a closed-loop process, where the model or agent decides based on current progress whether to retrieve, what to retrieve, whether to rewrite the query, whether to continue with supplementary retrieval, or even proactively go back and search again when it finds the evidence insufficient.

The biggest difference between the two is not “whether there is retrieval,” but whether **retrieval is managed as a dynamic decision-making process**.

- Traditional RAG: stable workflow, more controllable cost, simple to implement, suitable for single-turn Q&A and most standard knowledge-base scenarios.
- Agentic RAG: more suitable for complex questions, multi-hop evidence, and scenarios requiring self-checking and supplementary retrieval, but at the cost of a longer chain, higher cost, and higher risk of losing control.

Therefore, in engineering practice, we usually do not start with Agentic RAG right away. Instead, we first examine whether the bad cases are truly concentrated in these kinds of problems:

- A single retrieval often fails to obtain enough evidence.
- The question itself requires decomposition, multi-turn verification, or cross-source validation.
- Before generation, the system needs to determine “whether to query the knowledge base, the web, or a business system.”

If Agentic RAG really needs to be put into production, I would definitely add step limits, budget limits, failure exit conditions, and observability at the same time. Otherwise, it can easily turn from “smarter retrieval” into “more expensive random wandering.”

**Common follow-up questions:**

- Under what circumstances should we stick with fixed RAG instead of upgrading to Agentic RAG?
- In which bad cases does the benefit of Agentic RAG usually show?
- How can we prevent multi-turn supplementary retrieval from pushing latency and cost too high?

**Importance:** `中频` (appears 1 time) | **Difficulty:** `较难`

**Assessment focus:** Whether the candidate truly understands the boundary and cost of RAG evolving from a fixed pipeline to an intelligent retrieval closed loop.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §1, Introduction to RAG](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_1-introduction-to-rag); [21 Agent §1, Introduction to Agent](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_1-introduction-to-agents)

---

## 4. Retrieval Infrastructure and Retrieval Optimization

### Q4-1. What is a vector database? How does it differ from a traditional database? Why can’t we just use MySQL?

First, a definition: a vector database is a storage system specifically designed for “similarity retrieval,” used to store vectors, original content, and metadata, and to support nearest-neighbor search, filtering, and recall.

Traditional databases excel at exact filtering, transactions, and structured queries, while vector databases excel at nearest-neighbor retrieval based on “semantic similarity.” The two are not replacements for each other, but rather complementary.

If you use only MySQL, you can of course still store embeddings, but once the data volume grows, approximate vector retrieval, ANN indexes, hybrid retrieval, and large-scale recall all become inefficient, and engineering complexity rises noticeably. In enterprises, a more common approach is: structured conditions go through a traditional database, semantic recall goes through a vector database, and the two sides are combined through metadata.

**Importance:** `高频` (appears 2 times) | **Difficulty:** `基础`

**Assessment focus:** Understanding of the underlying retrieval infrastructure.

**Corresponding sections:** [18 Vector Databases and Embedding in Practice §2, Vector Databases](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_2-vector-databases); [18 Vector Databases and Embedding in Practice §6, Writing to and Retrieving from Vector Databases](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_6-writing-to-and-retrieving-from-a-vector-database-rags-underlying-capability)

### Q4-2. What is Embedding? What is its core value in application development?

The essence of embedding is to convert raw content such as text and images into a fixed-length vector, so that “semantic relationships” are mapped as much as possible into “spatial relationships.” In another engineering-oriented formulation, it turns “similar in meaning” into “close in distance,” enabling programs to perform similarity calculations.

Its core value in application development is not merely “encoding text into numbers,” but giving the system the ability to perform semantic retrieval for the first time. That is why it is often used for semantic search, similarity matching, deduplication, clustering, recommendation, and RAG recall.

In RAG, embedding determines whether “the question and the knowledge can meet correctly in vector space.” If the embedding is chosen incorrectly, no matter how much you compensate later with the vector database, reranking, or prompts, you can only optimize on top of a skewed recall base.

Two additional engineering details deserve special emphasis:

- It is best to use the same embedding model for both indexing and querying; otherwise either the dimensions will not match, or even if the dimensions are the same, the similarity may be meaningless.
- Embedding only represents the layer of converting text into “dense vectors.” During actual retrieval, it is often combined with scalar-field filtering and even sparse retrieval, so it should not be understood as the entirety of a retrieval system.

**Importance:** `高频` (appears 1 time) | **Difficulty:** `基础`

**Assessment focus:** Whether the candidate understands that embedding is not an “auxiliary model,” but part of the retrieval infrastructure.

**Corresponding sections:** [18 Vector Databases and Embedding in Practice §1, Vectors and Vectorization](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_1-vectors-and-embedding); [18 Vector Databases and Embedding in Practice §4, Text Vectorization with Embedding](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_4-embedding-text-vectorization)

### Q4-3. How do you choose a suitable embedding model? What should you look at when evaluating its quality?

Usually we do not look at leaderboards first. Instead, we first look at our own knowledge types and retrieval goals, and then work backward to model selection. A more reasonable approach is to look at three things first:

- Language and domain fit: Chinese, English, multilingual, code, legal, finance—the suitable models may be completely different.
- Consistency between indexing and querying: indexing and querying should use the same embedding model as much as possible; this is the bottom line.
- Whether cost and latency are acceptable: higher dimensionality is not always better, and larger models are not always better. It depends on whether the knowledge base scale and query volume can support them.

When actually evaluating, we should pay more attention to “whether it lifts the entire retrieval chain as a whole” rather than only looking at a single leaderboard score. There are usually three practical layers of judgment:

- Retrieval layer: whether relevant chunks are more easily recalled, whether bad examples decrease, and whether the gap before and after reranking is large.
- Business layer: whether the final answer’s faithfulness, citation accuracy, and task completion rate improve.
- Engineering layer: whether latency, cost, and integration complexity are acceptable.

Two points deserve special emphasis in engineering:

- Embedding selection is not an isolated problem; together with chunking strategy, index parameters, hybrid retrieval, and reranking, it determines the upper limit.
- Public leaderboards can only serve as an initial screen. What ultimately decides whether to go live is still your own knowledge samples and bad cases.

Therefore, a more reliable approach is usually: first select two or three candidate models and get them running, then conduct a small-scale comparison on your own knowledge-base samples, observe recall quality, final answer quality, and cost and latency, and finally decide.

**Importance:** `高频` (appears 1 time) | **Difficulty:** `中等`

**Assessment focus:** Embedding model selection, evaluation awareness, and understanding of “model consistency + retrieval chain linkage.”

**Corresponding sections:** [18 Vector Databases and Embedding in Practice §4, Text Vectorization with Embedding](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_4-embedding-text-vectorization); [18 Vector Databases and Embedding in Practice §6, Writing to and Retrieving from Vector Databases](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_6-writing-to-and-retrieving-from-a-vector-database-rags-underlying-capability)

### Q4-4. How do you balance approximate retrieval and exact retrieval?

Exact retrieval gives more controllable results, but at large data scales it incurs high cost and high latency. Approximate retrieval sacrifices some precision in exchange for better throughput and response speed, so most online systems prefer approximate retrieval.

In engineering, it is not a simple either-or choice, but depends on business requirements. For high-risk retrieval, small data volumes, or extremely strict requirements on result consistency, you can use exact or more conservative index strategies. For general knowledge Q&A, product search, and massive document recall, approximate retrieval is usually more realistic, with reranking used as compensation.

**Importance:** `中频` (appears 1 time) | **Difficulty:** `中等`

**Assessment focus:** Ability to trade off performance and effectiveness.

**Corresponding sections:** [18 Vector Databases and Embedding in Practice §2, Vector Databases](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_2-vector-databases); [18 Vector Databases and Embedding in Practice §5, Computing Semantic Similarity Through Vectors](18-%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8EEmbedding%E5%AE%9E%E6%88%98.md#_5-calculating-semantic-similarity-through-vectors)

### Q4-5. In what scenarios are knowledge graphs or graph databases more valuable than pure vector retrieval?

When the core of the problem is not just “semantic similarity,” but “entity relationships, path reasoning, multi-hop associations, and structural constraints,” knowledge graphs or graph databases become more valuable.

For example, equipment troubleshooting, product attribute associations, organizational relationships, legal provision citations, and dependency chain analysis often depend more on “who is related to whom and how” than on “which piece of text looks most similar.” In such cases, relying only on vector retrieval can easily recall content that is semantically close but relationally incorrect.

In engineering, it is better to understand this as enhancement rather than simple replacement. A more reliable approach is usually: vector retrieval handles semantic recall, while the knowledge graph handles structural constraints, entity disambiguation, and relational reasoning. Only when the problem itself is highly structured and the relationship chain is especially critical might the graph database become the main path.

**Importance:** `中频` (appears 1 time) | **Difficulty:** `较难`

**Assessment focus:** Understanding of the boundary between “semantic recall” and “relational reasoning,” and the ability to choose retrieval architecture.

### Q4-6. What scenarios is GraphRAG suitable for? How do you choose between it and traditional vector RAG?

GraphRAG is more suitable for scenarios with dense entity relationships, requiring multi-hop reasoning, community summaries, or strong structural constraints.

For example, organizational relationship analysis, supply chain dependencies, equipment failure chains, legal provision associations, and person-event networks—these problems are often not about “which piece of text is most similar,” but about “who is associated with whom and how, and how many hops are needed to reach the answer.” In such cases, the advantages of a knowledge graph or graph database become more obvious.

But in engineering, we usually do not start with GraphRAG by default. A more common and safer path is:

- First use traditional vector RAG as the baseline to solve most semantic recall problems.
- When bad cases are clearly concentrated in multi-hop relationships, entity disambiguation, and structural constraints, introduce graph enhancement.
- In real implementation, it is often not an either-or choice, but rather combining "vector retrieval + graph retrieval + fusion reranking" together.

A more accurate conclusion is: **Only when the core of the problem lies in relational structure will the graph approach yield benefits that exceed its complexity.**

**Common follow-up questions:**

- What is the relationship between GraphRAG and knowledge graph databases?
- Under what circumstances is multi-route retrieval more realistic than a pure graph-based primary route?
- Will the cost of graph updating and maintenance be too high?

**Importance:**`中频` (occurrences: 1) | **Difficulty:**`较难`

**Assessment focus:** GraphRAG selection capability, and awareness of the trade-off between complexity and benefit.

---

## 5. Tools, Function Calling, and Agent

### Q5-1. What is the ReAct pattern? What problem does it solve?

The value of ReAct lies in connecting "reasoning" and "acting," so that the model not only thinks but can also continuously adjust its next step based on external observations.

It usually takes the form of a `Thought -> Action -> Observation` loop. The model first makes a judgment based on the current situation, then decides which tool to call, and then updates its judgment based on the tool's returned result, until the task is completed. Compared with relying solely on one-shot generation, ReAct is better suited to tasks with uncertain paths, multi-step decision-making, and strong dependence on external information.

One important point also needs to be added here: modern Tool Calling Agents do not necessarily expose `Thought` in plain text. In actual code, what is more common is `AIMessage.tool_calls`, tool execution results, and the next round of messages. Therefore, a more accurate understanding is: **ReAct is closer to a working mechanism, rather than just a fixed Prompt template.**

From an engineering perspective, it is worth noting that ReAct's advantage is flexibility, but the cost is longer chains, higher expense, and more complex debugging, so not every scenario is worth implementing a full loop.

**Common follow-up questions:**

- What is Chain of Thought (CoT)? Why can it improve performance on complex reasoning questions?
- What is the difference between CoT and ReAct? When is CoT alone sufficient, and when should you upgrade to ReAct?

**Importance:**`高频` (occurrences: 3) | **Difficulty:**`基础`

**Assessment focus:** Understanding of Agent operating paradigms.

**Corresponding sections:** [21 Agent §3. How Agents Work (V0.3)](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_3、agent-工作原理%EF%BC%88v0.3%EF%BC%89); [17 Tools §2. How Tool Calling Works](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_2-how-tool-calling-works)

### Q5-2. What is the relationship among Tool, Function Calling, and Agent?

Tool is a capability unit, Function Calling is an invocation mechanism, and Agent is an operating pattern that organizes the model, tools, state, and decision-making process together.

Tool addresses "what can be done," Function Calling addresses "how to initiate a structured call," and Agent addresses "how to make multi-round decisions around a goal about whether to call, whom to call, and how many times to call." Therefore, Tool is not equal to Agent, and a single Tool Calling is not necessarily equal to Agent either.

In real projects, many requirements only need Tool Calling, and it is not always necessary to build a full Agent. Only when a task requires multi-step planning, repeated decision-making, and state progression is an Agent worth introducing.

**Common follow-up questions:**

- Does a single-tool assistant count as an Agent?
- What is the relationship between ReAct and Function Calling?
- What should be the minimum granularity of Tool design?

**Importance:**`必刷` (occurrences: 2) | **Difficulty:**`基础`

**Assessment focus:** Whether conceptual distinctions are clear.

**Corresponding sections:** [17 Tools §1. Introduction to Tools](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_1-introduction-to-tools); [21 Agent §6. Summary: The Differences and Connections Among Agent, Tool, Function Calling, RAG, and MCP](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_6-summary-differences-and-relationships-among-agent-tool-function-calling-rag-and-mcp)

### Q5-3. How should an Agent be designed? What core components does it usually consist of?

If summarized in the most minimal way, it can be written as: **Agent = Model + Tool Set + Run Loop + Current State**.

- Model: responsible for understanding goals, analyzing the current situation, and deciding the next step.
- Tool set: responsible for providing external capabilities, such as search, databases, file systems, and business APIs.
- Run loop: responsible for ensuring that the system does not answer only once, but can "think one step, do one step, look at the result, and then decide the next step."
- Current state: responsible for saving messages, tool returns, intermediate results, and thread context.

On top of this minimal skeleton, memory, planning, reflection, and multi-agent collaboration can all be added further, but they are better understood as "extension capabilities" rather than something every Agent must have from the start.

From an engineering design perspective, a deployable Agent should focus on controlling five things:

- Goals and responsibilities: what problem an Agent solves should be as singular as possible; it should not try to do everything.
- Tool boundaries: expose only the capabilities truly needed to complete the task, and avoid giving the model blanket permissions.
- State design: explicitly design where current task progress, intermediate conclusions, and message history are stored.
- Stop conditions: when to continue, when to clarify, when to hand off to a human, and when to end must not be ambiguous.
- Governance capabilities: logging, tracing, retries, timeouts, auditing, and manual takeover must all be in place.

In summary, the focus of Agent design is not "piling on more capabilities," but rather building a system around the four main lines of **model, tools, loop, and state** to make it more controllable, more traceable, and more reliably deliverable.

**Common follow-up questions:**

- When building a complex Agent, what do you think the main challenge is?
- Why do many Agents fail not because of insufficient capability, but because state, boundaries, and governance were not well designed?

**Importance:**`必刷` (occurrences: 2) | **Difficulty:**`中等`

**Assessment focus:** Agent architecture capability, rather than staying at the conceptual level.

**Corresponding sections:** [21 Agent §1. Introduction to Agents](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_1-introduction-to-agents); [21 Agent §6. Summary: The Differences and Connections Among Agent, Tool, Function Calling, RAG, and MCP](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_6-summary-differences-and-relationships-among-agent-tool-function-calling-rag-and-mcp)

### Q5-4. What is the basic principle of Function Calling?

The core division of labor in Function Calling can be summarized in one sentence: the model is responsible for decisions, and the program is responsible for execution.

More completely, this chain usually works as follows:

1. The host program sends the tool's `name`, `description`, and parameter schema to the model together.
2. The model determines whether to call a tool, and if so, it first returns a structured `tool_calls` instead of directly giving the final natural language response.
3. The host program reads the `AIMessage.tool_calls` and actually executes the Python function, HTTP API, database query, or business service.
4. The program wraps the execution result into a `ToolMessage` or equivalent message and sends it back to the model.
5. The model generates the final reply based on the tool result.

Therefore, Function Calling is not the model calling an API by itself; it only generates the structured intent of "which tool to call and what parameters to pass." The actual authentication, parameter validation, timeout handling, idempotency, retries, and security control all still remain at the host program layer.

If you want to answer in a more engineering-oriented way, you also need to add one more point: Function Calling solves "how the model expresses invocation intent," not "whether the tool is safe, whether invocation is allowed, or how to handle invocation failures."

**Common follow-up questions:**

- What is the difference between Function Calling and text-parsing-based invocation?
- Why is native Tool Calling more recommended in production environments?
- How should tool execution failures be handled?

**Importance:**`必刷` (occurrences: 1) | **Difficulty:**`中等`

**Assessment focus:** Whether the boundary of responsibilities between the model and the host program is understood.

**Corresponding sections:** [17 Tools §1. Introduction to Tools](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_1-introduction-to-tools); [17 Tools §2. How Tool Calling Works](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_2-how-tool-calling-works)

**Source:** Tencent AI Backend Engineer First Round (actual big-tech interview question)

### Q5-5. What are the most important engineering principles when designing a Tool?

The four most important points are: single responsibility, a clear schema, observability, and failability.

Single responsibility means one Tool does only one clear thing, avoiding a "large and all-encompassing universal tool." A clear schema is meant to help the model understand parameter meanings more stably. Observability means every call must be able to trace the request, parameters, latency, result, and errors. Failability means the tool must have timeout handling, exception codes, retry strategies, and fallback logic, rather than assuming success.

If the Tool needs to connect to business systems, you also need to add permission checks, idempotency control, and audit logs. Because once a tool changes from "checking the weather" to "sending messages, creating work orders, or writing to a database," the risk level becomes completely different.

**Importance:**`高频` (occurrences: 1) | **Difficulty:**`中等`

**Assessment focus:** Whether there is practical awareness of connecting tools to production systems.

**Corresponding sections:** [17 Tools §3. Custom Tools](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_3-custom-tools-start-with-the-simplest-tool); [17 Tools §4. Parameter Schema: Why Pydantic Should Be Used](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_4-parameter-schema-why-pair-it-with-pydantic)

### Q5-6. If you were asked to implement an AI assistant for "checking weather and news," how would you design it?

For this type of question in an interview, it is better to first analyze the scenario and then discuss the approach. For requirements like checking weather or news, the core is not complex planning, but rather "intent recognition + tool invocation + result integration."

A relatively stable implementation usually includes four layers:

- Input and routing layer: first determine whether the user wants weather, news, or both. If necessary, extract parameters such as city, time, and news topic.
- Tool layer: wrap weather query and news retrieval separately as clear Tools, with well-defined schemas, parameter descriptions, exception returns, and timeout strategies.
- Orchestration layer: first use Function Calling or a lightweight Agent to let the model decide which tool to call, how to pass parameters, and whether multiple tools need to be chained.
- Output layer: organize the tool results in a unified way, for example weather gives key fields and news gives summaries and sources, and then let the model generate the natural language reply.

If the requirement is only single-turn weather or news queries, `Prompt + Function Calling` is often sufficient, and a full ReAct Agent is not necessarily required. Only when the requirement upgrades to a multi-step dynamic chain such as "first check the weather, then recommend local news based on the weather, and then continue asking about the details of a certain news item" does the value of an Agent become more apparent.

From an engineering perspective, three points need special attention: tool descriptions must be clear to avoid the model calling tools randomly; external APIs must have fallback and timeout handling; and output results should ideally include sources or key fields to avoid the model fabricating the tool results a second time.

**Importance:**`高频` (occurrences: 1) | **Difficulty:**`中等`

**Assessment focus:** Whether a simple assistant can be broken down into the four layers of "intent, tools, orchestration, and output," rather than immediately saying to build an Agent.

**Corresponding sections:** [17 Tools §5. Weather Assistant Hands-On](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_5-weather-assistant-in-practice-running-tools-as-a-complete-business-loop); [21 Agent §5. Practice and Cases](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_5-hands-on-practice-and-case-studies)

**Source:** Tencent AI Backend Engineer First Round (actual big-tech interview question)

### Q5-7. What is "tool hallucination"? How can it be mitigated in engineering?

Tool hallucination refers to the model calling a tool that does not exist, passing unreasonable parameters, or attempting to trigger a write operation when it should only be reading data.

This type of problem is especially common when there are many tools, vague descriptions, and unclear schemas. Sometimes the model's issue is not that it "does not know how to use the tool," but rather that it "misunderstands the tool's boundaries."

In engineering, the following safeguards are usually implemented:

- Tool registry whitelist: directly reject tool names that do not exist.
- Strong schema validation: parameter types, required fields, and enum values must all be validated at runtime, without trusting the model's return.
- Tool set convergence: Expose a minimal tool set per scenario; don't let the model guess among dozens of similar tools.
- Clear descriptions: Tool names, descriptions, and parameter meanings should clearly distinguish read/write boundaries and applicable scenarios.
- High-risk confirmation: Side-effect actions such as sending messages, writing to databases, creating tickets, or placing orders must require approval or second confirmation.
- Failure feedback: Return error causes to the model so it can correct itself, but limit retry attempts to avoid infinite loops.

It can be summarized as: **Tool Calling is not "plug it in and you're done"; instead, you need to make the model "call accurately, stay under control, and avoid major incidents even when it calls incorrectly."**

**Importance:** `高频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Understanding of Tool Use stability and risk control.

**Corresponding sections:** [17 Tools §6, From Course Examples to Real Projects](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_6-from-course-examples-to-real-projects); [17 Tools §4, Parameter Schema: Why Pydantic Should Be Used Together](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_4-parameter-schema-why-pair-it-with-pydantic)

### Q5-8. What is the difference between Function Calling and "having the model output JSON and then parsing it yourself"?

On the surface, both look like "the model outputs structured results," but they differ significantly in stability and engineering boundaries.

- Having the model output JSON is closer to making a request at the Prompt layer. It is simple, universal, and quick to start, but once the model adds an extra sentence of natural language, omits a field, or writes the wrong type, the program side has to handle all the fallback itself.
- Function Calling is closer to protocol-level structured output. The model does not arbitrarily return a piece of text; instead, it explicitly returns a tool name and parameters, and the host parses and executes them according to the contract, which is usually more reliable.

Therefore, in production environments, the usual judgment is:

- If you only need to extract fields and return lightweight structured output, and the platform's native capabilities are limited, start with JSON + parser.
- If you need to enter real tool invocation, external system orchestration, and side-effect execution, prioritize native Function Calling or an equivalent Tool Use protocol.

The more critical difference lies in the boundary of responsibility. JSON parsing is closer to "you try to make the model produce this format as much as possible"; Function Calling is closer to "there is an explicit contract between the model and the host." The clearer this contract is, the easier the subsequent validation, auditing, retrying, and observability become.

**Common follow-up questions:**

- When is JSON + parser already sufficient?
- Why is Function Calling more suitable for connecting to production systems?
- If the platform does not provide native Function Calling, how can you make the JSON approach as stable as possible?

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Understanding of the protocol-level difference between structured output and tool invocation.

**Corresponding sections:** [14 Output Parsers §4, Structured Output](14-%E8%BE%93%E5%87%BA%E8%A7%A3%E6%9E%90%E5%99%A8.md#_4-structured-output); [17 Tools §2, How Tool Invocation Works](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_2-how-tool-calling-works)

### Q5-9. When there are many tools, how do you control context length and invocation stability?

Once there are many tools, the problem is usually no longer "whether the model can invoke tools," but "whether it will select the wrong one, invoke it incorrectly, and become increasingly chaotic among a pile of similar tools."

There are roughly four stable approaches:

- Layered exposure: First split tools by business domain into search, data, execution, and write-operation categories; do not expose all tools to the same Agent at once.
- Dynamic selection: First perform Tool Retrieval or routing, and put only the Top-N most relevant tool descriptions into the current context instead of listing everything.
- Tool aggregation: Wrap overly granular underlying APIs into higher-level business actions to reduce the model guessing names among dozens of similar functions.
- Description governance: Tool names, descriptions, and parameter documentation should clearly state "when to use, when not to use, and whether there are side effects."

Taking it one step further, in production you can also make "tool selection" itself an independent stage, such as first performing intent classification or subdomain routing, and then entering specific tool invocation. This controls context length while also reducing the probability of tool hallucination and incorrect invocation.

It can be summarized as: **Having many tools is not the problem; the key is not letting the model blindly choose in an unstructured sea of tools.**

**Common follow-up questions:**

- When there are too many tools, should routing or adjusting tool granularity be prioritized?
- What is the difference between Tool Retrieval and ordinary knowledge retrieval?
- Why are business-action-level tools usually more suitable for model invocation than atomic APIs?

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `较难`

**Assessment focus:** Context governance and tool orchestration capability in multi-tool scenarios.

**Corresponding sections:** [17 Tools §6, From Course Examples to Real Projects](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_6-from-course-examples-to-real-projects); [21 Agent §5, Hands-on Practice and Examples](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_5-hands-on-practice-and-case-studies)

---

## 6. Agent Frameworks and Orchestration: LangChain, LCEL, LangGraph

### Q6-1. Compared with ordinary Workflows or chained invocation, what is the greatest value of LangGraph?

The greatest value of LangGraph is that it explicitly expresses state, nodes, edges, and loops in complex processes, making LLM-driven dynamic processes truly designable, traceable, and recoverable.

Ordinary chained invocation is suitable for simple serial processes, Workflows are suitable for fixed paths, and LangGraph is more suitable for tasks involving branching, loops, human interruption, state persistence, and multi-Agent collaboration. It is not "a different way of writing code," but rather turning complex control flow from implicit logic into an explicit graph structure.

So when your system starts showing questions like "should we keep searching, when to stop, where to recover after failure, and how to preserve state across turns," the advantages of LangGraph emerge.

**Common follow-up questions:**

- What is the relationship between LangGraph and Agent?
- In what scenarios is an ordinary Workflow sufficient?
- Will the maintenance cost of graph orchestration be higher?

**Importance:** `必刷` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Whether the necessity of graph orchestration is understood.

**Corresponding sections:** [22 LangGraph Overview and Quick Start §1, Introduction to LangGraph](22-LangGraph%E6%A6%82%E8%BF%B0%E4%B8%8E%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8.md#_1-introduction-to-langgraph); [23 LangGraph API: Graphs and State §1, Graph API - Graph](23-LangGraphAPI%EF%BC%9A%E5%9B%BE%E4%B8%8E%E7%8A%B6%E6%80%81.md#_1-graph-api-the-graph)

### Q6-2. In LangGraph, what do State, Node, and Edge represent respectively?

State is the shared state, Node is the processing logic, and Edge is the transition rule.

State determines what the "context that everyone operates on together" is in the graph; Node determines what each step specifically does, such as calling a model, querying a database, or executing a tool; Edge determines where to go next after the current node finishes, which can be a fixed jump or conditional routing.

In real projects, whether LangGraph is well designed often depends on whether the State is clear, whether the Node granularity is reasonable, and whether the Edge conditions are explainable. Many graphs become difficult to maintain not because the graph itself is complex, but because too much implicit logic has been stuffed into a single node.

**Importance:** `高频` (occurrences: 1) | **Difficulty:** `基础`

**Assessment focus:** Basic mental model of LangGraph.

**Corresponding sections:** [23 LangGraph API: Graphs and State §2, Graph API - State](23-LangGraphAPI%EF%BC%9A%E5%9B%BE%E4%B8%8E%E7%8A%B6%E6%80%81.md#_2-graph-api-state); [24 LangGraph API: Nodes, Edges, and Advanced Topics §2, Graph API - Edge](24-LangGraphAPI%EF%BC%9A%E8%8A%82%E7%82%B9%E3%80%81%E8%BE%B9%E4%B8%8E%E8%BF%9B%E9%98%B6.md#_2-graph-api-edge)

### Q6-3. What is the value of LangChain today? Why is simply writing the SDK directly not enough?

The value of LangChain is not "whether it can call a model," but that it unifies common capabilities such as model input and output, Prompt, Parser, Retriever, Tools, Memory, and Callbacks into a set of composable interfaces.

If you are only building a minimal demo, writing the SDK directly is of course fine. But once you enter the stage of multi-model integration, chain orchestration, structured output, observability, and long-term maintenance, a unified abstraction will significantly reduce code fragmentation. What it truly solves is the problem of "application-layer orchestration and ecosystem integration," not "sending an HTTP request for you."

**Importance:** `高频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Framework selection judgment, rather than blind worship of frameworks.

**Corresponding sections:** [9 LangChain Overview and Architecture §2, Positioning of LangChain](9-LangChain%E6%A6%82%E8%BF%B0%E4%B8%8E%E6%9E%B6%E6%9E%84.md#_2-positioning-of-langchain); [9 LangChain Overview and Architecture §4, Core Modules of LangChain](9-LangChain%E6%A6%82%E8%BF%B0%E4%B8%8E%E6%9E%B6%E6%9E%84.md#_4-langchain-core-modules)

### Q6-4. How do you develop an Agent using LangChain?

A minimal usable LangChain Agent is usually explained through two routes.

- Classic route: Combine the model, tools, Prompt, `create_tool_calling_agent(...)`, and `AgentExecutor(...)` layer by layer, which is more suitable for understanding the internal structure.
- 1.x route: Directly use `create_agent(...)`, with the LangGraph-based runtime driving loops, state, and tool invocation behind the scenes, which is closer to the current official mainstream.

No matter which route you take, the underlying main line remains the same:

- First define Tools, wrapping external capabilities into clear capability units.
- Then select an LLM and let the model know the schema of the callable tools.
- Then design the Prompt, clarifying roles, tool usage rules, stop conditions, and output boundaries.
- Finally, let the system form the closed loop of "model decision -> tool execution -> result return -> continue or stop."

For simple scenarios, you can directly use high-level wrappers; for complex scenarios, you still need to clearly explain the underlying main execution line. In interviews, what truly earns points is not memorizing API names, but being able to explain clearly why the Agent invokes a tool, when it stops, and how to handle failures when they occur.

**Importance:** `高频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Whether it is understood that an Agent is not "done after calling a create_agent function," but rather a clear understanding of the underlying composition.

**Corresponding sections:** [21 Agent §5, Hands-on Practice and Examples](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_5-hands-on-practice-and-case-studies); [17 Tools §5, Weather Assistant Hands-on](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_5-weather-assistant-in-practice-running-tools-as-a-complete-business-loop)

### Q6-5. What is the value of LCEL? Why is it not just syntactic sugar?

The core value of LCEL is abstracting Prompt, Model, Parser, Retriever, and function logic into Runnable, and then combining and calling them through a unified approach.

It is not just shorter syntax; it allows sequential chains, branching chains, parallel chains, and function chains to be assembled, debugged, and replaced through the same interface. This is very valuable for real projects, because when you later add logging, streaming, batch processing, callbacks, and partial replacement, a unified interface makes the system more maintainable.

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Whether the unified interface concept of chain orchestration is understood.

**Corresponding sections:** [15 LCEL and Chain Invocation §1, Runnable and Unified Invocation](15-LCEL%E4%B8%8E%E9%93%BE%E5%BC%8F%E8%B0%83%E7%94%A8.md#_1-runnable-and-the-unified-invocation-style); [15 LCEL and Chain Invocation §2, Introduction to LCEL](15-LCEL%E4%B8%8E%E9%93%BE%E5%BC%8F%E8%B0%83%E7%94%A8.md#_2-introduction-to-lcel)

### Q6-6. Among LangGraph's advanced features, which ones do you think have the greatest engineering value?

Prioritize four categories: streaming, persistence, time travel, and subgraphs. These four also happen to be the main line of LangGraph's advanced features.

First look at streaming. LangGraph's streaming is not just "the model spits out tokens bit by bit"; more importantly, it can stream the execution of the entire graph. The commonly used `stream_mode` in real projects are:

- `values`: View the complete state snapshot after each step.
- `updates`: View which fields were actually changed in the current step.
- `messages`: View model message fragments or token streams.
- `custom`: Actively push business progress within nodes, such as "retrieving from the knowledge base."

Next, let's look at persistence. In LangGraph, `checkpointer` is closer to short-term memory within a thread or session, suitable for saving graph state by `thread_id`, and used for breakpoint recovery, human-in-the-loop collaboration, and multi-turn task continuation. If you need to save longer-term information across threads and sessions, that is closer to the Store line.

The engineering value of time travel mainly lies in troubleshooting, retrospective review, and replay. Many complex Agents fail not because the final result is wrong, but because the state at some intermediate step was polluted. Time Travel allows you to review a specific node or even rerun from it.

The value of subgraphs is breaking down complex systems into reusable modules. For example, a "retrieval subgraph," "approval subgraph," and "report generation subgraph" can be independently encapsulated, while the main graph is responsible only for higher-level orchestration.

These four types of capabilities can be summarized in one sentence: streaming provides observability, persistence provides recoverability, time travel provides reviewability, and subgraphs provide maintainability. Only when all four are used together does LangGraph truly resemble production infrastructure, rather than just a demo graph that can run.

**Common follow-up questions:**

- What is the difference between Checkpointer and long-term memory?
- What scenarios are suitable for Time-Travel?
- When should you split out a subgraph?

**Importance:** `中频` (Occurrences: 1) | **Difficulty:** `较难`

**Assessment point:** Whether the candidate cares about real production capability, rather than only knowing HelloWorld.

**Corresponding sections:** [25 LangGraph Advanced Features §1, Streaming](25-LangGraph%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7.md#_1-streaming); [25 LangGraph Advanced Features §2, State Persistence](25-LangGraph%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7.md#_2-state-persistence); [25 LangGraph Advanced Features §3, Time Travel](25-LangGraph%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7.md#_3、时间回溯%EF%BC%88time-travel%EF%BC%89); [25 LangGraph Advanced Features §4, Subgraphs](25-LangGraph%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7.md#_4、子图%EF%BC%88subgraphs%EF%BC%89)

### Q6-7. How can Checkpoint, HITL, and Time-Travel be explained in a more engineering-oriented way in an interview?

These three concepts are best understood together because they jointly address one issue: **a complex Agent is not enough just because it "can run"; it also needs to be able to pause, observe, approve, and continue.**

- Checkpoint: Solves "whether recovery is possible after doing half of the work", and is suitable for long tasks, resuming from a breakpoint, and failure replay.
- HITL: Solves "whether high-risk actions need human decision-making", and is suitable for human confirmation before actions such as payments, data modification or deletion, and external sending.
- Time-Travel: Solves "how to look back and review after something goes wrong", and is suitable for troubleshooting, debugging, and rerunning specific stages.

To summarize in a very engineering-oriented sentence:

> Checkpoint ensures recoverability, HITL ensures controllability, and Time-Travel ensures reviewability.

When these three capabilities are discussed together, interviewers usually feel that what you understand is not "whether you can draw a graph," but "how to govern a system after it goes live."

**Common follow-up questions:**

- Which nodes would you definitely add human approval to?
- How do you explain the boundary between Checkpointer and long-term memory / Store?
- When is time travel merely a debugging tool, and when is it already a production necessity?

**Importance:** `中频` (Occurrences: 1) | **Difficulty:** `较难`

**Assessment point:** Understanding of LangGraph production capability, and the ability to generalize the three types of capabilities: recovery, approval, and review.

**Corresponding sections:** [25 LangGraph Advanced Features §2, State Persistence](25-LangGraph%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7.md#_2-state-persistence); [25 LangGraph Advanced Features §3, Time Travel](25-LangGraph%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7.md#_3、时间回溯%EF%BC%88time-travel%EF%BC%89)

---

## 7. Memory, MCP, and Multi-Agent

### Q7-1. What is the relationship among context window, short-term memory, and long-term memory?

The context window is the upper limit of content that the model can see in a single inference, short-term memory is session-level state, and long-term memory is user or task information retained across sessions.

In engineering practice, these three should not be conflated. The window is an expensive resource and cannot be filled with unlimited history. Short-term memory generally retains history, summaries, and thread state related to the current task. Long-term memory is better suited for storing preferences, profiles, historical conclusions, and reusable facts, which need to be retrieved on demand rather than being placed into the prompt in full every time.

Therefore, a mature system usually works like this: only high-signal context is placed in the window, short-term memory ensures the current thread is uninterrupted, and long-term memory is recalled on demand through a database or vector store.

**Common follow-up questions:**

- What is the difference between memory and RAG?
- Why is it said that memory is not model training?
- What is Redis suitable for in memory?
- If the context is too long and gets truncated, would you choose a sliding window, summary compression, or retrieval-based supplementation? How do you decide?

**Importance:** `必刷` (Occurrences: 3) | **Difficulty:** `中等`

**Assessment point:** State design capability for conversational systems and Agents.

**Corresponding sections:** [16 Memory and Conversation History §1, Introduction to Memory](16-%E8%AE%B0%E5%BF%86%E4%B8%8E%E5%AF%B9%E8%AF%9D%E5%8E%86%E5%8F%B2%EF%BC%88%E5%90%ABRedis%E5%9F%BA%E7%A1%80%EF%BC%89.md#_1-introduction-to-memory); [25 LangGraph Advanced Features §2, State Persistence](25-LangGraph%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7.md#_2-state-persistence)

### Q7-2. How do you design short-term and long-term memory systems for an Agent? How is it usually implemented technically?

First, split "memory" into two layers. Otherwise, it is easy to stuff all information into the context, which ultimately becomes both expensive and chaotic.

- Short-term memory: Solves the problem of keeping the current session or thread uninterrupted. The core flow is "read history -> assemble it into the prompt -> call the model -> write back the history."
- Long-term memory: Solves the problem of retaining user preferences, profiles, historical conclusions, and reusable facts across sessions. The core idea is to "store structured information and recall it on demand," rather than cramming everything into the prompt every turn.

Technically, a common approach for short-term memory is to persist message history or thread state into memory, Redis, or a checkpointer, and then inject it back in the next turn through `MessagesPlaceholder` or graph state. Long-term memory is better placed in a database, a vector store, or, in scenarios where relationships are important, a knowledge graph. A relatively solid engineering approach is: short-term memory serves current-task continuity, long-term memory serves cross-task reuse, and the two should be designed separately.

In the LangChain / LangGraph ecosystem, `RunnableWithMessageHistory + BaseChatMessageHistory` is better understood as "conversation history injection," while LangGraph persistence / checkpointer is better understood as thread-level state persistence. The former is better suited for first explaining clearly "how message history is read and written," while the latter is better suited for Agents, graph orchestration, and thread-level state management.

Therefore, in actual implementation the division is usually as follows:

- Chat assistants or lightweight multi-turn Q&A: prioritize the message history approach.
- Complex Agents or LangGraph: prioritize the `thread_id + checkpointer` approach.
- Cross-session preferences, facts, and user profiles: use long-term storage and retrieve on demand; do not force them directly into the context.

If the follow-up question is "how can ultra-long multi-turn conversations maintain continuity while saving tokens," four common methods are usually added:

- Sliding window: keep only the most recent N turns of original text. It is simple and direct, but early constraints are easily lost.
- Periodic summarization: every few turns, compress the history into a structured summary that retains goals, confirmed facts, pending items, and preferences.
- Retrieval-based supplementation: write old conversations into a vector store or long-term storage, and recall relevant fragments based on the current question, rather than putting all old messages back into the window.
- Structured memory slots: fixed information such as city, membership level, preferences, and key states is stored directly in key-value stores or databases, so the model does not need to "recall" it every time.

So a memory system is not about "the more history is saved, the better." Instead, it is about distinguishing what should be kept verbatim, what should be summarized, what should be structured, and what should be retrieved on demand.

**Common follow-up questions:**

- How do you understand the respective roles of `RunnableWithMessageHistory` and LangGraph persistence / checkpointer?
- Is Redis more suitable for short-term memory persistence, or for long-term memory?

**Importance:** `高频` (Occurrences: 2) | **Difficulty:** `较难`

**Assessment point:** Memory layering design capability, and understanding of the boundaries among short-term state, long-term knowledge, and external storage.

**Corresponding sections:** [16 Memory and Conversation History §4, RunnableWithMessageHistory and BaseChatMessageHistory](16-%E8%AE%B0%E5%BF%86%E4%B8%8E%E5%AF%B9%E8%AF%9D%E5%8E%86%E5%8F%B2%EF%BC%88%E5%90%ABRedis%E5%9F%BA%E7%A1%80%EF%BC%89.md#_4、实现类介绍：runnablewithmessagehistory-与-basechatmessagehistory); [25 LangGraph Advanced Features §2, State Persistence](25-LangGraph%E9%AB%98%E7%BA%A7%E7%89%B9%E6%80%A7.md#_2-state-persistence)

### Q7-3. What is MCP? What core problem does it solve? How is it different from Tool, RAG, and Agent?

To give a definition first, MCP is the Model Context Protocol. It is an open standard used to regulate how AI applications connect to external tools, resources, and prompt templates in a unified way.

In essence, MCP is building a "unified protocol layer for model capability integration." What it solves is not "whether the model can call tools," but "how different AI applications can connect external tools, resources, and context in a unified way."

A more intuitive way to understand it is that MCP is best seen as a unified socket for the AI world. What it unifies is not the model itself, but the way capabilities are discovered, exposed, and invoked among Host, Client, and Server. An MCP Server does not only expose Tools; it can also expose Resources and Prompts.

- Tool / Function Calling: Solves how the model expresses "which tool I want to call and what parameters to pass."
- RAG: Solves how the model obtains external knowledge.
- Agent: Solves who plans, decides, and invokes these capabilities.
- MCP: Solves how these external capabilities are exposed and integrated in a standardized way.

Therefore, MCP is not equal to Agent, nor to Tool. It leans more toward the protocol and ecosystem layer, and its value lies in exposing once and reusing everywhere, with a unified schema and lower integration costs.

**Common follow-up questions:**

- What capabilities does an MCP Server usually expose?
- How do you choose between STDIO and HTTP transport?
- Why do enterprises care about MCP?

**Importance:** `高频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment point:** Understanding of the protocol layer.

**Corresponding sections:** [20 MCP Model Context Protocol §2, Introduction to MCP](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_2-introduction-to-mcp); [20 MCP Model Context Protocol §3, What MCP Can Do](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_3-what-mcp-can-do)

**Source:** Tencent AI backend engineer first-round interview (real major-company interview question)

### Q7-4. What is the relationship between MCP and Function Calling?

Function Calling is closer to the "structured invocation mechanism" on the model side, while MCP is closer to the "unified capability integration protocol" on the application side.

The former solves how the model expresses "which function to call and what parameters to pass"; the latter solves how different external tools, resources, and prompt templates are exposed to clients under a unified standard. The two are not substitutes for each other but rather upper-layer and lower-layer relationships.

It can be simply understood as: Function Calling is closer to model decision-making, while MCP is closer to ecosystem integration and protocol standardization. In actual implementation, an Agent can perfectly well continue to use Function Calling for invocation decisions on top of capabilities exposed by MCP.

**Importance:** `高频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment point:** Understanding of the boundary between the protocol layer and the invocation mechanism.

**Corresponding sections:** [20 MCP Model Context Protocol §2, Introduction to MCP](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_2-introduction-to-mcp); [17 Tools and Tool Invocation §2, How Tool Invocation Works](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_2-how-tool-calling-works)

### Q7-5. How does MCP achieve cross-platform compatibility?

MCP's cross-platform compatibility essentially comes from "unified protocol, not unified implementation."

That is to say, different platforms, different languages, and different host programs can interoperate at the protocol layer as long as they all follow the same message structure, capability exposure method, and invocation conventions. In this way, the client does not need to write a private integration approach for every external system, and the server can also expose capabilities according to the standard.

Therefore, the value of MCP does not lie in its binding to a particular technology stack, but in its ability to converge integration differences into a unified protocol surface.

**Importance:** `中频` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment point:** Understanding of protocol standardization.

**Corresponding section:** [20 MCP Model Context Protocol §5, MCP Architecture Knowledge](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_5-mcp-architecture-knowledge)

### Q7-6. What is the main content of the MCP technical protocol?

If expanded from the protocol layer, the main content of MCP is clearest when explained in four layers:

- Participating roles: Host, Client, Server.
- Capability types: Tools, Resources, Prompts.
- Communication mechanisms: capability discovery, request, response, error, notification.
- Transport methods: stdio, Streamable HTTP, and other channels that carry the protocol.

One more detail needs to be added here:

- Tools are more model-controlled, suitable for letting the model automatically decide whether to call them.
- Resources are more application-driven, usually determined by the host on how to incorporate them into context.
- Prompts are more user-controlled, suitable for reusing prompt templates or workflow templates.

Answering this way usually shows the interviewer that you understand the protocol itself, rather than treating MCP merely as some "ready-made plugin marketplace."

**Importance:** `中频` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment point:** Whether you understand the basic composition of the MCP protocol layer.

**Corresponding section:** [20 MCP Model Context Protocol §5, MCP Architecture Knowledge](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_5-mcp-architecture-knowledge); [20 MCP Model Context Protocol §3, What MCP Can Do](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_3-what-mcp-can-do)

### Q7-7. What is the development process for an MCP server?

A typical development process for an MCP Server is usually:

1. Clarify the capability boundary to be exposed: whether it is a tool, resource, or prompt template.
2. Define the input/output schema and error handling approach.
3. Choose the transport method, such as STDIO or HTTP.
4. Implement the server-side logic and complete authentication, logging, timeout, and exception handling.
5. Complete registration, discovery, invocation, and integration testing on the client side.

In engineering practice, the most easily overlooked aspects are the capability boundary and error handling. An MCP Server is not simply wrapping an existing API in a shell, but rather designing capabilities into interfaces that are truly suitable for model consumption.

**Importance:** `中频` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment point:** Whether you understand that MCP is not just about "using it," but also includes server-side construction.

**Corresponding section:** [20 MCP Model Context Protocol §4, How to Use MCP](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_4-how-to-use-mcp); [20 MCP Model Context Protocol §6, Case Practice: Local MCP Weather Service and Client](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_6-hands-on-case-study-local-mcp-weather-service-and-client)

### Q7-8. How should an Agent integrate MCP tools?

The core of integrating MCP tools into an Agent is to incorporate the capabilities exposed by MCP into its own tool registration and scheduling system.

The usual approach is:

- First discover the tools or resources exposed by the MCP Server.
- Then convert these capabilities into tool descriptions and schemas that the Agent can consume.
- During execution, let the model decide when to call, while the host is responsible for actually initiating the MCP request.
- Return the result to the Agent, which enters the next round of decision-making.

The real key is not in "connecting," but in "how to ensure controllability after connection," including permissions, timeouts, failure retries, observability, and auditing.

**Common follow-up questions:**

- In your architecture, does MCP only perform permission checks, or does it work together with an environment-level security sandbox?
- If MCP already exists, why do you still need containers, read-only mounts, or system-level isolation?

**Importance:** `中频` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment point:** How Agent architecture and MCP are combined.

**Corresponding section:** [20 MCP Model Context Protocol §4, How to Use MCP](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_4-how-to-use-mcp); [20 MCP Model Context Protocol §6, Case Practice: Local MCP Weather Service and Client](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_6-hands-on-case-study-local-mcp-weather-service-and-client)

### Q7-9. What is the core advantage of MCP's streaming HTTP transport?

The core value of streaming HTTP is that results can be returned while being produced, rather than having to wait for the entire invocation to complete before returning all at once.

This brings three direct benefits:

- Lower time-to-first-token latency, giving users faster feedback.
- Supports mid-progress reporting for long tasks, reducing the feeling of being "stuck."
- Makes it easier for the host to handle cancellation, timeouts, and partial results.

For Agent or research-oriented tasks, this capability is especially important, because many calls are not "instantaneous" in nature.

**Importance:** `中频` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment point:** Understanding of the value of streaming protocols in terms of experience and concurrency.

**Corresponding section:** [20 MCP Model Context Protocol §5, MCP Architecture Knowledge](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_5-mcp-architecture-knowledge)

### Q7-10. How do MCP calls ensure concurrency?

MCP concurrency capability is not determined solely by the protocol itself, but depends more on how the host and server design the request processing model.

To ensure concurrency, you usually need to pay attention to:

- Whether requests have unique identifiers to avoid response mismatches.
- Whether the server supports parallel processing rather than serial blocking.
- Whether tool execution has timeout, rate limiting, and priority control.
- Whether the client can correctly manage multiple request contexts.

If the underlying tools themselves are very slow, no matter how good the protocol is, it cannot save the situation, so concurrency governance must be designed across all three layers: "protocol layer + service layer + tool layer."

**Importance:** `中频` (occurrences: 1 time) | **Difficulty:** `较难`

**Assessment point:** Protocol and host design capabilities under high-concurrency calls.

**Corresponding section:** [20 MCP Model Context Protocol §5, MCP Architecture Knowledge](20-MCP%E6%A8%A1%E5%9E%8B%E4%B8%8A%E4%B8%8B%E6%96%87%E5%8D%8F%E8%AE%AE.md#_5-mcp-architecture-knowledge)

### Q7-11. What is the difference between A2A and MCP? When do you need multi-agent?

MCP focuses more on "how models and external capabilities connect," while A2A focuses more on "how Agents collaborate with each other."

The former leans toward tool and resource integration standards, while the latter leans toward multi-agent communication and division of labor. If the system only needs to connect search, databases, or file systems, the value of MCP is more evident; if the system has evolved to have multiple Agents with clear roles and separated responsibilities, such as planning, retrieval, execution, and review each being independent, then A2A or multi-agent orchestration becomes meaningful.

Multi-agent is not a case of the earlier the better. If a task can be handled clearly by a single Agent, multi-agent only increases communication, debugging, and governance costs. Splitting is worthwhile only when responsibility boundaries are clear, a single Agent's prompt is already overloaded, and the process genuinely requires role-based division.

**Common follow-up questions:**

- How do you choose between Supervisor and Handoff?
- What are the most common failure points of multi-agent?
- Under what circumstances is a Skill more appropriate than an independent Agent?
- What exactly are the boundaries between A2A, application-level orchestration frameworks like LangGraph, and ordinary Agent frameworks?
- How should the boundaries between Agent Skills, Tools, and independent Agents be understood? When is it more suitable to build a Skill rather than splitting out another Agent?

**Importance:** `中频` (occurrences: 1 time) | **Difficulty:** `较难`

**Assessment point:** Protocol boundaries and system decomposition capabilities.

**Corresponding section:** [26 LangGraph Multi-Agent and A2A §1, A2A Protocol and Multi-Agent Architecture](26-LangGraph%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E4%B8%8EA2A.md#_1、a2a-协议与多智能体架构); [26 LangGraph Multi-Agent and A2A §2, Supervisor and Handoff](26-LangGraph%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E4%B8%8EA2A.md#_2-supervisor-and-handoff); [26 LangGraph Multi-Agent and A2A §3, Skills and the Boundaries of Multi-Agent](26-LangGraph%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E4%B8%8EA2A.md#_3-the-boundary-between-skills-and-multi-agent-systems); [27 Agent Skills: Agent Skills and AI Programming Tool Practices](../../27-Agent%20Skills%E6%99%BA%E8%83%BD%E4%BD%93%E6%8A%80%E8%83%BD%E4%B8%8EAI%E7%BC%96%E7%A8%8B%E5%B7%A5%E5%85%B7%E5%AE%9E%E8%B7%B5.md)

**Source:** Tencent AI backend engineer first-round interview (actual large-company interview question)

### Q7-12. What are some popular MCP tools?

Commonly discussed MCP tools usually fall into several categories:

- Browser automation, such as Playwright.
- Data and backend, such as databases and services like Supabase.
- Files and code, such as local file systems and code repositories.
- Search and knowledge, such as web search and knowledge base retrieval.

In an interview, the more important thing is not memorizing all the names, but knowing why these tools are popular: because they cover the most common external capability needs of Agents.

**Importance:** `低频` (occurrences: 1 time) | **Difficulty:** `基础`

**Assessment point:** Have a basic understanding of the MCP ecosystem, but rote memorization is not required.

---

## 8. Platform Practice and Framework Selection: Coze, Dify, RAGFlow

### Q8-1. How should the relationship between platforms like Coze / Dify and LangChain / LangGraph be understood?

Coze / Dify lean more toward the application layer, low-code, and visual delivery, while LangChain / LangGraph lean more toward code-level development frameworks. They are not substitutes for each other, but different layers on the same AI application chain.

If understood from this layered relationship:

- Dify / Coze are more suitable for quickly setting up Agent, RAG, and Workflow, making it convenient for business-side validation, collaboration, and delivery.
- LangChain is more suitable for combining components such as Prompt, Model I/O, Parser, Retriever, and Tools in a code-based manner.
- LangGraph is more suitable for complex orchestration such as explicit state, loops, conditional routing, human-machine collaboration, and multi-agent.

Therefore, platforms are closer to the "application building layer," while code frameworks are closer to the "underlying orchestration layer." A very common path in real projects is: first use the platform to validate business value, then migrate the core chain to the code framework; or let the platform handle upper-level business orchestration while underlying complex capabilities are taken on by self-built services.

**Importance:** `高频` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment point:** Selection judgment between platform capabilities and code capabilities.

**Corresponding section:** [3 Agent Development Based on Coze & Dify Platforms §1, Overview of AI Agents](3-%E5%9F%BA%E4%BA%8ECoze&Dify%E5%B9%B3%E5%8F%B0%E7%9A%84%E6%99%BA%E8%83%BD%E4%BD%93%E5%BC%80%E5%8F%91.md#_1、智能体ai-agent概述); [9 LangChain Overview and Architecture §2, LangChain Positioning](9-LangChain%E6%A6%82%E8%BF%B0%E4%B8%8E%E6%9E%B6%E6%9E%84.md#_2-positioning-of-langchain)

### Q8-2. How should various Agent development frameworks be selected?

Framework selection should not be based on popularity, but on task complexity, team capability, and delivery requirements.

- If the goal is rapid prototyping, a rich ecosystem, and complete common components, LangChain is very suitable.
- If the task involves explicit state, loops, conditional routing, human-machine collaboration, or multi-agent, LangGraph is more suitable.
- If it is low-code and rapid validation of business processes, Coze / Dify are more suitable.
- If the system boundaries are simple and the requirements are very clear, directly writing an SDK may also be the lowest-cost solution.

A more mature way to answer is not simply comparing "which is best," but explaining "what is more cost-effective in which scenario." Being able to name alternatives and migration paths is usually more persuasive than simply praising a particular framework.

**Common follow-up questions:**

- What indicators will you ultimately use to judge whether this framework selection is successful?
- If you use a platform in the early stage and later migrate to a self-developed framework, how should the migration boundary be drawn?

**Importance:** `高频` (occurrences: 1 time) | **Difficulty:** `中等`

**Assessment Focus:** Framework selection and engineering judgment.

**Corresponding Sections:** [9 LangChain Overview and Architecture §2, LangChain Positioning](9-LangChain%E6%A6%82%E8%BF%B0%E4%B8%8E%E6%9E%B6%E6%9E%84.md#_2-positioning-of-langchain); [22 LangGraph Overview and Quick Start §1, Introduction to LangGraph](22-LangGraph%E6%A6%82%E8%BF%B0%E4%B8%8E%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8.md#_1-introduction-to-langgraph)

### Q8-3. When are workflows more appropriate than Agents?

Workflows are usually more appropriate than Agents when business steps are fixed, the output format is clear, and strong controllability and easy auditability are desired.

For example, classification, summarization, content moderation, report generation, form filling, and fixed approval chains: in these scenarios the process paths are usually stable. Using workflows makes it clearer to define node responsibilities, failure retries, human intervention points, and SLAs. Agents are better suited for open-ended tasks and dynamic decision-making, while workflows are better suited for the large number of rule-based, accountable, replayable process-type tasks in enterprises.

**Common Follow-up Questions:**

- Which nodes in a workflow are suitable to hand over to an LLM?
- Where should human review points be added?
- How can a workflow gradually evolve into an Agentic Workflow?

**Importance:** `高频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment Focus:** Awareness of process governance.

**Corresponding Sections:** [3 Agent Development Based on Coze & Dify Platforms §6, Building Workflows](3-%E5%9F%BA%E4%BA%8ECoze&Dify%E5%B9%B3%E5%8F%B0%E7%9A%84%E6%99%BA%E8%83%BD%E4%BD%93%E5%BC%80%E5%8F%91.md#_6-building-workflows); [21 Agent §1, Introduction to Agents](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_1-introduction-to-agents)

### Q8-4. When calling Dify / Coze workflows with Python, which engineering details deserve the most attention?

The key focus should be on five categories of issues: authentication, parameter alignment, streaming mode, timeout limits, and log tracing.

Let's start with Dify. The key fields of its workflow API are usually:

- `Authorization: Bearer {api_key}`
- The `inputs` in the request body
- `response_mode`
- `user`

There are two very easy pitfalls here: first, API Keys and workflows are bound together; you should not use a global key everywhere. Second, for long processes, try to use `streaming` as much as possible, because `blocking` is easily interrupted by gateway timeouts. When actually implementing streaming, you need to be able to identify the `workflow_finished` in the SSE stream and correctly obtain the final `outputs`.

Now for Coze. There you need to pay even closer attention to:

- `workflow_id`
- `app_id`
- `parameters`

Among them, `parameters` must be strictly aligned with the input variables defined in the workflow. If the variable names do not match, the code may appear to run, and the request may even succeed, but the business result will simply be wrong. During streaming, you need to be able to distinguish `PING`, `MESSAGE`, `DONE`, or the `MESSAGE / ERROR / INTERRUPT` event in the SDK.

To summarize from an engineering perspective, the main things to look at are:

- Whether the binding relationships among keys, workflows, and applications are clearly understood.
- Whether request parameter names are strictly consistent with the platform workflow inputs.
- Whether streaming is used by default instead of compressing long tasks into blocking calls.
- Whether platform logs, `workflow_run_id`, and business `request_id` are linked together.
- If the process has external side effects, whether idempotency, retries, and failure compensation are properly handled.

What this question really tests is not "whether you know how to send a POST request," but whether you truly understand the real invocation chain of the platform API.

**Common Follow-up Questions:**

- How to choose between streaming and blocking responses?
- What troubleshooting problems can platform logs solve?
- How should platform workflows and self-built backend services collaborate?

**Importance:** `中频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment Focus:** Whether the candidate has looked at the real invocation chain of the platform API, rather than only knowing how to click through the interface.

**Corresponding Sections:** [4 Calling Dify Platform Workflows with Python §4, Request Format](4-Python%E8%B0%83%E7%94%A8Dify%E5%B9%B3%E5%8F%B0%E5%B7%A5%E4%BD%9C%E6%B5%81.md#_4、请求格式); [5 Calling Coze Platform Workflows with Python §3, Calling Workflows via Python Code](5-Python%E8%B0%83%E7%94%A8Coze%E5%B9%B3%E5%8F%B0%E5%B7%A5%E4%BD%9C%E6%B5%81.md#_3-通过-python-代码调用工作流)

### Q8-5. How should you evaluate open-source RAG platforms such as RAGFlow? How do they compare with Dify or self-built pipelines?

This question should not be answered as "which one is stronger," but as "what does the current knowledge base scenario need more."

If the focus is on document ingestion, parsing, chunking, retrieval, and RAG orchestration experience, then platforms like RAGFlow will be more attractive. If the focus is on multiple types of Agents, workflows, plugin ecosystems, and business API orchestration, then platforms like Dify / Coze will have broader boundaries. If the core pipeline involves deep customization, complex state governance, compliance auditing, and coupling with internal systems, a self-built code pipeline is usually more stable.

When actually making a selection, prioritize four categories of factors: document ingestion and parsing quality, permissions and multi-tenancy capabilities, ease of integration with business systems, and room for secondary development. Many projects do not get stuck on "whether RAG can be done," but rather on "whether parsing quality is stable, whether permissions can be enforced properly, and whether it can later be integrated into enterprise systems."

**Importance:** `中频` (Occurrences: 1) | **Difficulty:** `中等`

**Assessment Focus:** RAG platform selection judgment, as well as awareness of the boundary between platform capabilities and self-built capabilities.

---

## 9. Security, Evaluation, Deployment, and Observability

### Q9-1. How would you evaluate the effectiveness of a RAG or Agent system?

Evaluation should first be split into **offline evaluation** and **online evaluation**, and then the problem should be broken down into specific layers, rather than focusing only on a single total score.

For RAG, it is usually viewed at two layers:

- Retrieval layer: whether relevant content was recalled, whether the cited passages are correct, and whether bad cases are stuck in chunking, retrieval, reranking, or filtering.
- Generation layer: whether the answer is faithful to the evidence, whether citations are correct, whether it can refuse to answer when there is no basis, and whether the final answer is helpful to the business.

For Agents, evaluation should be divided into two categories:

- Trajectory-level evaluation: whether the right tools were selected, whether parameters were correct, whether there were invalid loops, and whether it ended too early.
- Result-level evaluation: whether the final task was completed, and whether output quality and user experience met the standard.

Online evaluation looks at user satisfaction, human handoff rate, task interruption rate, latency, and the distribution of bad case types. For Agents, it should also look at tool call success rate, retry rate, number of loops, and the proportion of human fallback.

For automated evaluation, it is usually unwise to rely on only one approach; instead, rule-based evaluation, `LLM-as-a-judge`, and manual sampling should be combined. Rule-based and LLM evaluation are suitable for scaling up and performing regression testing, while manual sampling handles high-risk misjudgments and evaluation drift.

More importantly, evaluation must not only tell you that "the score has dropped," but must also be able to locate exactly which layer has the problem. For example, poor recall, poor context assembly, hallucination during generation, tool failures, and unreasonable termination conditions all require completely different fixes.

The more recommended evaluation closed loop is: **first build metrics layer by layer, then accumulate bad cases, and finally let bad cases in turn drive iteration of prompts, retrieval, tools, and processes.**

**Common Follow-up Questions:**

- What are frameworks like RAGAS suitable for?
- How do you build a bad case dataset?
- How should automated evaluation and manual evaluation work together?

**Importance:** `必刷` (Occurrences: 2) | **Difficulty:** `较难`

**Assessment Focus:** Whether the candidate has a sense of evaluation closed loop.

**Corresponding Sections:** [19 RAG Retrieval-Augmented Generation §3, RAG Comprehensive Case: Intelligent Operations Assistant](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_3-comprehensive-rag-case-intelligent-operations-assistant); [21 Agent §5, Practice and Case Studies](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_5-hands-on-practice-and-case-studies)

### Q9-2. What is "hallucination"? How should it be mitigated at the application layer?

Hallucination is not just "complete nonsense"; more commonly, it is "something that looks very real, but the details, citations, time points, permission scope, or tool results have already drifted."

Therefore, hallucination should not be treated as a purely model problem, but should be viewed as a systemic problem along the entire chain. A relatively robust mitigation approach usually has four layers:

- Knowledge layer: use RAG, external retrieval, citations, and refusal to answer without basis to make the model answer based on evidence as much as possible.
- Execution layer: hand tasks such as calculation, database queries, sending messages, and checking orders to Tools, rather than letting the model fabricate results in plain text.
- Constraint layer: use structured output, schema validation, key field rule validation, and low-temperature strategies to reduce cases where "the format is correct but the content is wrong."
- Governance layer: implement bad case feedback loops, manual sampling, online monitoring, and degradation, rather than treating "the model will probably be fine" as a launch condition.

In summary, hallucination is difficult to eliminate completely. The engineering goal is not to "guarantee it will never make mistakes," but to make it **discoverable, constrainable, rollbackable, and reviewable**.

**Common Follow-up Questions:**

- Why can't RAG completely eliminate hallucination?
- What does "having citations but still unfaithful" mean?
- Are hallucination and Prompt Injection the same thing?

**Importance:** `高频` (Occurrences: 2) | **Difficulty:** `中等`

**Assessment Focus:** Whether the candidate understands the boundary between "model capability issues" and "application chain governance issues."

**Corresponding Sections:** [19 RAG Retrieval-Augmented Generation §1, Introduction to RAG](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_1-introduction-to-rag); [14 Output Parsers §4, Structured Output](14-%E8%BE%93%E5%87%BA%E8%A7%A3%E6%9E%90%E5%99%A8.md#_4-structured-output)

### Q9-3. In multi-user scenarios, how do you implement security sandbox isolation for Agents?

If an Agent is only a standalone demo, many risks will not surface. But once it enters a multi-user scenario, security isolation must be elevated from "tool permissions" to "execution environment isolation."

A more robust solution usually has three layers:

- Environment layer: use Docker or other containers to isolate each task or tenant, limiting CPU, memory, network, and filesystem access scope.
- System layer: use seccomp, AppArmor, read-only root directories, temporary working directories, and non-root user execution to avoid directly touching the host machine.
- Application layer: enforce allowlists and auditing for tools, file access, system commands, and external connections, so the model does not get raw permissions.

If code execution, commands, or file reads are required, limitations are usually not enforced only through prompts or business code. Instead, the working directory is mounted as a least-privilege space, sensitive directories are not mounted, and database keys and host credentials are not placed inside the container. MCP or Tools are responsible for "whether it can be called," while the sandbox is responsible for "even if it is called, it cannot escape the boundary." These two responsibilities are different, and it is best to use both together.

**Importance:** `高频` (Occurrences: 2) | **Difficulty:** `较难`

**Assessment Focus:** Security isolation design for multi-user Agents, as well as the division of responsibilities between protocol-layer control and environment-layer isolation.

**Corresponding Sections:** [7 Enterprise-Level LLM Deployment §1, Overview of Enterprise-Level LLM Deployment](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_1-overview-of-enterprise-level-large-model-deployment); [17 Tools §6, From Course Cases to Real Projects](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_6-from-course-examples-to-real-projects)

### Q9-4. What metrics are involved in Agent deployment and operations?

Agent operations should at least look at five categories of metrics:

- Effectiveness metrics: task completion rate, user satisfaction, citation accuracy.
- Performance metrics: first token, end-to-end latency, P95/P99.
- Stability metrics: call success rate, timeout rate, retry rate, failure rate.
- Cost metrics: token consumption, tool invocation cost, average cost per task.
- Governance metrics: human takeover rate, audit log completeness, abnormal task review efficiency.

For a multi-tool, multi-step Agent, you also need to look at the success rate of each step and where tasks get stuck; otherwise, you will only know that "it ultimately failed" without knowing which layer the failure occurred in.

**Importance:**`高频` (occurrences: 1) | **Difficulty:**`中等`

**Assessment focus:** The operational perspective of moving from demo to production.

**Corresponding sections:** [7 Enterprise-grade Large Language Model Deployment §1, Overview of Enterprise-grade Large Language Model Deployment](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_1-overview-of-enterprise-level-large-model-deployment); [21 Agent Intelligence §5, Practice and Cases](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_5-hands-on-practice-and-case-studies)

### Q9-5. What challenges may a RAG system face in actual deployment?

Once RAG truly goes live, the difficulty usually lies not in "whether it can retrieve," but in "whether this complete pipeline from indexing to answering can operate stably over the long term."

The first point to emphasize here is that RAG is not a single-point capability, but an engineering pipeline consisting of an "indexing stage + retrieval and generation stage." Many online issues are essentially caused by a problem at some layer within these two stages.

First, break the challenges down into six categories:

- Data side: document parsing quality, chunking strategy, table and PDF processing, and knowledge update timeliness. If the source data is dirty and chunking is unreasonable, subsequent retrieval and generation will both be dragged down.
- Retrieval side: embedding selection, recall quality, hybrid retrieval, reranking effectiveness, and metadata filtering. Many systems appear to answer correctly offline, but once scaled up online, they expose problems such as inaccurate recall, excessive noise, and missing key passages.
- Generation side: context assembly, citation traceability, faithfulness control, and refusal strategies. RAG is not "retrieved, therefore no hallucination." If context stitching is poor, the prompt is weak, or citations are unclear, the model will still fabricate information.
- Governance side: permission isolation, version management, citation traceability, and knowledge rollback. In an enterprise, the greatest fear is not answering incorrectly, but answering content outside of authorized permissions, or providing an answer without being able to explain where the basis came from.
- Evaluation side: badcase construction, offline evaluation, and closed-loop online metrics. Without evaluation, it is very difficult to know whether the problem lies in chunking, recall, reranking, or generation.
- Engineering side: latency, cost, caching, observability, index rebuilding, and online operations. For example, when the knowledge base is updated, should it be a full rebuild or an incremental update? If queries are slow, is the bottleneck in retrieval, reranking, or the model? These all need to be examined separately.

Therefore, a more reliable answer in an interview is not simply to say "deployment will involve many engineering issues," but to clearly state that RAG is a complete pipeline from data ingestion, index construction, and retrieval recall to answer generation, and that if any layer has a problem, the final answer will be affected.

**Common follow-up questions:**

- If the online performance of RAG is poor, which layer would you prioritize for troubleshooting?
- When the knowledge base is updated frequently, how do you handle index rebuilding and version rollback?

**Importance:**`高频` (occurrences: 1) | **Difficulty:**`较难`

**Assessment focus:** Whether the candidate has a production system mindset.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §2, Core Knowledge of RAG Text Processing](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_2-core-knowledge-of-rag-text-processing); [7 Enterprise-grade Large Language Model Deployment §1, Overview of Enterprise-grade Large Language Model Deployment](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_1-overview-of-enterprise-level-large-model-deployment)

### Q9-6. How do you ensure that an Agent's behavior is safe, controllable, and aligned with human intent?

This cannot rely solely on the hope that the model itself is "smart enough" or "already aligned." SFT, RLHF, and RLAIF at the model layer can only provide a basic safety boundary. When actually deployed in an application, application-layer governance must also be added.

This is usually handled at four layers:

- Model and prompt layer: use the system message to clearly define roles, boundaries, safety rules, and refusal policies.
- Tool and permission layer: do not give the model unrestricted permissions. All tools must have schema constraints, authentication, parameter validation, and least-privilege exposure.
- Execution and process layer: set maximum steps, timeouts, human approval, escalation to humans, and failure fallbacks to avoid infinite loops and dangerous actions being executed directly.
- Observability and audit layer: retain call logs, traces, inputs and outputs, key decision points, and paths for human review.

If adding another layer from a production perspective, I would also include budget control and circuit breaking:

- Budget control: maximum tool call count, time budget, token budget, and cost budget.
- Circuit breaker mechanisms: stop after consecutive failures, alert on abnormal rates, and exit when repeated attempts show no progress.

The value of these mechanisms is not only about saving money; more importantly, they contain the risk that "the model may keep trying indefinitely."

To summarize at a higher level: model alignment solves the problem of "basic behavior not being too far off," while application governance solves the problem of "not causing incidents within your business system." A truly stable Agent must be built by combining "model capability + permission boundaries + process control + human-machine collaboration," rather than relying on any single layer alone.

**Common follow-up questions:**

- The model has already undergone alignment, so why does the application layer still need so much security governance?
- Which actions would you require human approval for, rather than allowing the Agent to execute them directly?

**Importance:**`高频` (occurrences: 1) | **Difficulty:**`较难`

**Assessment focus:** Whether the candidate understands that "model alignment" and "application-layer security governance" are two complementary mechanisms.

### Q9-7. When an Agent pipeline takes a long time, how do you locate the performance bottleneck?

When an Agent pipeline takes several minutes, you cannot simply say "the model is too slow"; you first need to break down the time spent.

This is usually decomposed across the following layers:

- Model layer: single inference duration, time-to-first-token latency, and output token length.
- Retrieval layer: recall, reranking, external search, and knowledge base request latency.
- Tool layer: API latency, browser actions, code execution, and waiting for external system responses.
- Orchestration layer: routing decisions, supervisor decisions, repeated retries, and serial waiting.
- Result layer: post-processing, validation, storage, and log persistence.

A more reliable approach is to attach traces and spans to each step, first look at where the wall time is spent, and then decide whether to switch models, change the pipeline, reduce steps, or convert serial execution into parallel execution. If LangGraph is used, I also look at node-level latency, whether the flow repeatedly enters the same node, and whether it keeps going back and forth due to a lack of a clear completion signal.

Many five-minute tasks are ultimately not bottlenecked by a single model call, but by overly long multi-step pipelines, tool waiting, repeated supervisor decisions, or the absence of a clear success signal in the middle that causes repeated checking. In other words, performance problems are often not caused by "the model being too slow," but by **poorly designed state transitions and execution loops**.

**Importance:**`高频` (occurrences: 1) | **Difficulty:**`较难`

**Assessment focus:** Agent performance troubleshooting ability, and the ability to decompose long pipeline latency into model, tool, retrieval, and orchestration layers.

### Q9-8. How should intent recognition / task routing be done?

It must first be emphasized that this topic is not the same as "model routing." Model routing is closer to "should this time use a large model or a small model," while intent recognition / task routing is closer to "should this request go through FAQ, RAG, Tool, Agent, Workflow, or be directly escalated to a human."

A more reliable design usually consists of three layers:

- The first layer is target classification: first clearly define what routing destinations the system has, such as chitchat, FAQ, knowledge Q&A, status inquiry, action execution, complex tasks, and human fallback.
- The second layer is the routing mechanism: use rules and keywords as a fallback for high-certainty scenarios, and use a classification model or LLM for semantic judgment in ambiguous scenarios.
- The third layer is confidence governance: do not force a decision at low confidence. Allow clarification, degradation, or escalation to a human, and do not let the system continue running with a mistaken judgment.

In engineering practice, a single universal router is usually not built; instead, multi-level routing is preferred:

- First, perform business intent routing: determine whether this is FAQ, RAG, Tool, or Agent.
- Then perform sub-domain routing: for example, in customer service, further distinguish among orders, refunds, tickets, and complaints.
- Finally, perform model routing: decide within the specific pipeline whether to use a strong model or a lightweight model.

The advantage of this approach is that it is easier to govern and easier to evaluate. During evaluation, the key focus is on routing accuracy, the proportion of low-confidence cases, the cost of incorrect routing, clarification hit rate, and the final task completion rate of each routing branch.

**Common follow-up questions:**

- When is rule-based routing sufficient, and when is semantic classification necessary?
- If a question looks like both an FAQ and a Tool call, how do you handle it?
- How do you prevent incorrect routing from derailing the entire downstream pipeline?

**Importance:**`高频` (occurrences: 1) | **Difficulty:**`较难`

**Assessment focus:** Layered routing capability, practical ability in intent recognition, and the system design awareness to connect FAQ / RAG / Tool / Agent into a unified entry point.

**Corresponding sections:** [17 Tools and Tool Calling §6, From Course Cases to Real Projects](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_6-from-course-examples-to-real-projects); [19 RAG Retrieval-Augmented Generation §3, RAG Comprehensive Case: Intelligent Operations Assistant](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_3-comprehensive-rag-case-intelligent-operations-assistant)

### Q9-9. How would you implement observability for large language model applications?

At minimum, three things must be achieved: **logs, metrics, and traces**. That is, being able to see how requests flow through the system, how long each step takes, where failures occur, how many tokens are used, and what is ultimately output.

Specifically, trace_id / request_id should be linked throughout, connecting entry requests, prompt versions, model versions, index versions, retrieval results, tool calls, exception information, latency, and token usage. If LangChain / LangGraph is used, special attention should also be paid to node transitions, state updates, human interruption points, retry counts, and the final exit reason.

For Agent systems, observability is especially important because many problems occur in intermediate steps rather than at the moment of final output. Truly useful observability is not just "an error was reported at the end," but being able to tell you: **at which node it got stuck, why it retried, why it ended, and what state it saw at that time.**

**Importance:**`中频` (occurrences: 1) | **Difficulty:**`中等`

**Assessment focus:** Awareness of traces, logs, and metrics.

### Q9-10. For controlling the cost of large language model applications, which layers would you prioritize?

Usually, the approach starts from four layers: model, context, retrieval, and process.

- Model layer: tiered use of high- and low-spec models, using strong models for large tasks and lightweight models for small tasks.
- Context layer: compress prompts, reduce ineffective history, and control output length.
- Retrieval layer: optimize recall and reranking, and reduce content that enters the context window without meaningful value.
- Process layer: reduce unnecessary LLM call counts, and use rules wherever possible instead of relying entirely on the model.

Many systems have high costs not because the model is too expensive, but because the pipeline design is too wasteful, such as indiscriminate full retrieval, overly long history concatenation, repeated calls to large models, and blind retries after tool failures.

**Common follow-up questions:**

- When should model routing be introduced?
- How do you balance cost and effectiveness?
- Between token cost and tool cost, which is more worth optimizing first?

**Importance:**`中频` (occurrences: 1) | **Difficulty:**`中等`

**Assessment focus:** Cost optimization mindset.

**Corresponding sections:** [1-1 Large Language Model Cognition and Engineering Overview §4, Engineering Implementation of Large Language Models (Overview)](1-1-%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%A4%E7%9F%A5%E4%B8%8E%E5%B7%A5%E7%A8%8B%E6%A6%82%E8%A7%88.md#_4、大模型的工程实现%EF%BC%88概览%EF%BC%89); [7 Enterprise-grade Large Language Model Deployment §1, Overview of Enterprise-grade Large Language Model Deployment](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_1-overview-of-enterprise-level-large-model-deployment)

### Q9-11. How should model routing be done?

The core of model routing is not "letting all requests automatically find the strongest model," but rather directing requests of different complexity and risk levels to the most appropriate pipeline.

A relatively common approach has three layers:

- Intent routing: first determine whether this is an FAQ, RAG, tool call, complex Agent, or whether it should be transferred directly to a human.
- Complexity routing: simple classification, formatted extraction, and lightweight summarization go to a small model; multi-step planning, open-ended generation, and complex decision-making go to a large model.
- Cost routing: check the cache first for hot questions. If it can be solved with rules, don't send it to a large model. Give a stronger model budget only to high-value users or high-risk tasks.

In real implementation, routing is usually not made into purely subjective rules. Instead, it is adjusted together with evaluation and online data:

- Look at the completion rate, latency, and per-task cost of different routing branches.
- Check whether certain types of questions are being incorrectly downgraded to a small model.
- Check whether the routing rules need a fallback mechanism, such as escalating to a large model after a small model fails.

Therefore, model routing is essentially a balancer among effectiveness, cost, and stability. A well-built system does not always use the most expensive model, but rather can "save where it should save and spend where it should spend."

**Common follow-up questions:**

- In what scenarios is it better to start with rule-based routing instead of jumping straight into model routing?
- After a small model routing failure, how should upgrade and fallback strategies be designed?
- How can you avoid breaking the overall system effectiveness just to save cost?

**Importance:**`中频` (occurrences: 1 time) | **Difficulty:**`较难`

**Examination points:** Cost governance, model tiering, and routing strategy design capability.

**Corresponding chapters:** [11 Model I/O and Model Integration §2, LangChain Model Classification, Parameters and Returns](11-Model-I-O%E4%B8%8E%E6%A8%A1%E5%9E%8B%E6%8E%A5%E5%85%A5.md#_2-langchain-model-categories-parameters-and-returns); [7 Enterprise-grade Large Language Model Deployment §1, Overview of Enterprise-grade Large Language Model Deployment](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_1-overview-of-enterprise-level-large-model-deployment)

### Q9-12. How do you design an Agent / RAG system in an intranet environment?

The core of building Agent / RAG in an intranet environment is not simply "copying the public-network solution." Instead, the first priority is to establish several fundamentals: **data does not leave the domain, models are controllable, dependencies are replaceable, and the pipeline is observable**.

If designed with an enterprise deployment mindset, it is usually divided into three layers:

- Application layer: privatized versions of platforms such as Dify or Coze, or self-developed backend services, responsible for workflows, Agent orchestration, permissions, and business interfaces.
- Inference layer: use a hosting platform such as Xinference to centrally manage LLM, Embedding, and Rerank, exposing OpenAI-compatible APIs to the outside.
- Data layer: intranet vector databases, relational databases, object storage, knowledge base indexes, logs, and audit systems are all placed within a controllable domain.

The key points of this kind of architecture generally include:

- Unified model access: the upper layers should use compatible APIs as much as possible, making it convenient to swap between online models, local models, and different inference engines.
- Network and permission isolation: access to intranet systems by the Agent must be opened according to the principle of least privilege. Do not give the model a master key that can access everything on the intranet.
- Knowledge governance: document parsing, index rebuilding, version rollback, tenant isolation, and citation tracking must all be built in. Otherwise, an intranet knowledge base will quickly get out of control.
- Observability and auditing: request pipelines, tool calls, retrieval results, model versions, token usage, and anomaly alerts must all be viewable in a closed loop within the intranet.
- Degradation capability: when intranet models experience instability, there should be cache, rule-based pipelines, manual fallback, or backup models. Otherwise, the system will be very fragile.

In summary: an intranet solution is not an "offline demo." It is a production architecture that places even greater emphasis on security boundaries, operations governance, and model replaceability.

**Common follow-up questions:**

- Why do many enterprises choose to decouple the "application layer + inference layer" instead of mixing everything on a single machine?
- In an intranet environment, why is it best to deploy and manage LLM, Embedding, and Rerank separately?
- If direct access to public web search is not available, how should dynamic information be supplemented?

**Importance:**`中频` (occurrences: 1 time) | **Difficulty:**`较难`

**Examination points:** Understanding of enterprise private deployment, awareness of decoupling the application layer and inference layer, and the ability to design secure and operable intranet Agent / RAG systems.

**Corresponding chapters:** [7 Enterprise-grade Large Language Model Deployment §1, Overview of Enterprise-grade Large Language Model Deployment](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_1-overview-of-enterprise-level-large-model-deployment); [7 Enterprise-grade Large Language Model Deployment §3, Model Deployment](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_3-model-deployment); [12 Ollama Local Deployment and Invocation §5, LangChain Integration with Ollama](12-Ollama%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2%E4%B8%8E%E8%B0%83%E7%94%A8.md#_5-integrating-ollama-with-langchain)

---

## 10. Typical Business Scenario Design Questions

### Q10-1. If you were asked to design an enterprise knowledge base Q&A system, how would you do it?

It is usually designed in four layers: "data ingestion, retrieval pipeline, generation pipeline, and governance capability."

First, build the document ingestion, parsing, chunking, vectorization, and index update mechanisms. Then design the query pipeline, including query rewriting, hybrid retrieval, reranking, permission filtering, and context assembly. The generation layer should emphasize "answering based on evidence, refusing to answer when there is no evidence, and providing citations whenever possible." The governance layer should add permissions, versioning, monitoring, evaluation, and badcase feedback.

In an enterprise scenario, it is also common to reserve capabilities for handing off to human agents, knowledge revision, index rollback, and multi-tenant isolation, because these often affect long-term usability more than "getting the first answer right."

**Common follow-up questions:**

- How do you support knowledge updates?
- How do you prevent users from asking about documents outside their permissions?
- If the system gives irrelevant answers, where should you prioritize troubleshooting?

**Importance:**`必刷` (occurrences: 1 time) | **Difficulty:**`较难`

**Examination points:** Complete ability to express requirements into architecture.

**Corresponding chapters:** [2-RAG Building Enterprise Private & Personal Knowledge Bases §5, Building a Knowledge Base with Dify](2-RAG-%E6%90%AD%E5%BB%BA%E4%BC%81%E4%B8%9A%E7%A7%81%E6%9C%89&%E4%B8%AA%E4%BA%BA%E7%9F%A5%E8%AF%86%E5%BA%93.md#_5-building-a-knowledge-base-with-dify); [19 RAG Retrieval-Augmented Generation §3, RAG Comprehensive Case: Intelligent Operations Assistant](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_3-comprehensive-rag-case-intelligent-operations-assistant)

### Q10-2. If you were asked to design an NL2SQL Agent, which risks would you focus on controlling?

The focus should be on controlling four types of risk: schema injection, SQL security, execution verification, and ambiguity clarification.

First, do not stuff the entire database schema into the context. Instead, trim it and perform schema linking according to the question. Second, restrict queries to read-only, prohibit dangerous statements, and add an execution sandbox and timeout control. Third, perform syntax checking and pre-execution validation to avoid generating SQL that looks reasonable but cannot run. Finally, for issues such as time ranges, metric definitions, and field ambiguity, support clarification rather than letting the model make assumptions on its own.

**Common follow-up questions:**

- Should a preview be shown before generating SQL?
- How do you implement self-correction?
- When should you give up generating SQL and transfer it to a human or to a report template?

**Importance:**`高频` (occurrences: 1 time) | **Difficulty:**`较难`

**Examination points:** Structured queries and security awareness.

### Q10-3. If you were asked to design a customer service agent, which capabilities would you prioritize?

Prioritize intent recognition, knowledge retrieval, process execution, human-machine collaboration, and a retrospective closed loop.

Customer service is not simple Q&A. It often involves FAQ, order inquiry, refund processes, ticket routing, and emotional soothing at the same time. Therefore, the system must be able to answer questions, query status, call interfaces, supplement materials, and also promptly transfer to a human when uncertain, handing over the complete context.

After going live, it is also necessary to continuously review high-frequency unresolved issues, misidentified intents, knowledge gaps, and reasons for transfer to human agents. This is how the system becomes progressively more stable instead of only looking good in demos.

**Common follow-up questions:**

- How should the conditions for transferring to a human be designed?
- Why do customer service scenarios especially need long-term memory or user profiles?
- How do you evaluate satisfaction and closed-loop performance?

**Importance:**`高频` (occurrences: 1 time) | **Difficulty:**`较难`

**Examination points:** Ability to design business-oriented Agents.

**Corresponding chapters:** [3 Agent Development Based on Coze & Dify Platforms §7, Project: Merchant Operations Steward](3-%E5%9F%BA%E4%BA%8ECoze&Dify%E5%B9%B3%E5%8F%B0%E7%9A%84%E6%99%BA%E8%83%BD%E4%BD%93%E5%BC%80%E5%8F%91.md#_7-project-merchant-operations-manager); [21 Agent Intelligent Agents §5, Practice and Cases](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_5-hands-on-practice-and-case-studies)

### Q10-4. How do you design completion judgment and termination conditions for an Agent to avoid ending prematurely?

An Agent's "ending" cannot rely only on intuition, nor only on reading logs or a broad completion-rate score. A more reliable approach is to design explicit completion conditions for it.

Termination logic is usually divided into four layers:

- Task layer: whether the user's goal has been achieved and whether the necessary deliverables or fields have been obtained.
- Tool layer: whether key tool calls succeeded and whether the returned results meet expected constraints.
- State layer: whether the current state has entered a terminal state such as done / failed / need_human.
- Protection layer: maximum number of steps, timeout, repeated no-progress count, and abnormal exit conditions.

If the pipeline includes a Supervisor or supervision node, it is more appropriate to treat it as "auxiliary review" and "abnormal fallback" rather than the sole basis for ending. A truly stable solution is to allow entry into the final answer node only when the key task result, tool return, and state machine conditions are all satisfied. Otherwise, it is better to continue execution, ask for clarification, or transfer to a human rather than returning an unfinished result to the user prematurely.

**Common follow-up questions:**

- Why is relying only on a supervision node to calculate completion rate and read logs slow and prone to misjudgment?
- Is there a more general judgment method, such as directly checking key tool call results and state fields?
- How do you prevent the Agent from returning to the user before the task is actually finished?

**Importance:**`高频` (occurrences: 1 time) | **Difficulty:**`较难`

**Examination points:** Agent termination condition design, state machine thinking, and the ability to combine Supervisor / tool results / state fields.

**Corresponding chapters:** [24 LangGraph API: Nodes, Edges, and Advanced Topics §2, Graph API Edges](24-LangGraphAPI%EF%BC%9A%E8%8A%82%E7%82%B9%E3%80%81%E8%BE%B9%E4%B8%8E%E8%BF%9B%E9%98%B6.md#_2-graph-api-edge); [21 Agent Intelligent Agents §4, How Agents Work (V1.0)](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_4、agent-工作原理%EF%BC%88v1.0%EF%BC%89)

### Q10-5. How do you design a Code Agent?

The core of a Code Agent is not simply "being able to write a few lines of code," but being able to complete a closed loop around a code task: **read the codebase, make a plan, modify files, run verification, and continue correcting based on the results**. From a system structure perspective, it is still essentially an execution system composed of **model + toolset + execution loop + current state**, except that the tools and state are more oriented toward code scenarios.

If broken down into modules, it is usually designed into the following layers:

- Task understanding layer: first convert the requirement into a clear goal, and determine whether it is reading code, fixing a bug, supplementing tests, refactoring, or answering an architecture question.
- Codebase understanding layer: establish the minimum necessary context through code search, file tree, symbol index, dependency relationships, and commit history, rather than dumping the entire codebase into the model all at once.
- Planning and execution layer: first list the modification plan, then decide which files to read, which files to modify, which commands to run, and what verification is needed.
- Tool layer: at least the abilities to search, read files, edit files, run tests, execute commands, and view logs.
- Feedback closed-loop layer: continue correcting based on lint, tests, runtime errors, and diff results, rather than ending after generating a patch once.
- Security governance layer: restrict execution permissions, isolate dangerous commands, and retain change and execution logs to prevent the Agent from making unconstrained arbitrary changes in the codebase.

The real difficulty usually lies not in "whether it can generate code," but in three places:

- Context governance: when the codebase is very large, how to obtain only the context most relevant to the current task.
- Verification loop: how to determine whether a fix really works, rather than just letting the model say “I’ve fixed it.”
- Failure handling: when an Agent repeatedly fails to fix a bug, how to stop, how to expose intermediate diagnostics, and how to hand it back to a human.

Therefore, a mature Code Agent is closer to an “execution system for code tasks” than to a “scaled-up code autocomplete tool.” Its key capability is not just writing code, but turning **codebase understanding, tool invocation, verification feedback, and stopping conditions** into a stable closed loop.

**Common follow-up questions:**

- In a codebase with tens of millions of lines, where is a Code Agent most likely to get stuck first?
- When an Agent cannot fix a bug, how do you design stopping conditions and human takeover?
- In code scenarios, how do you distinguish static knowledge from dynamic data, and which should rely on indexes versus runtime feedback?

**Importance:** `高频` (occurrences: 1) | **Difficulty:** `较难`

**Assessment focus:** Agent design capability in code scenarios, codebase context governance capability, and awareness of the “modify - verify - continue fixing” closed loop.

### Q10-6. If you were asked to design a Deep Research system, how would it differ from ordinary RAG?

Ordinary RAG is closer to “retrieve first, then answer,” while Deep Research is closer to “around a complex topic, first break down the research task, then perform multiple rounds of retrieval, cross-verification, synthesis, and finally output a structured report.”

Therefore, Deep Research usually requires capabilities such as query planning, subtask decomposition, multi-source retrieval, conflict detection, citation management, credibility assessment, and iterative supplementary retrieval. It is closer to a research assistant than a Q&A assistant. Its output also tends more toward reports, summaries, and citation lists rather than a single direct answer.

If understood from an engineering implementation perspective, it is essentially closer to a combined capability of “**workflow / graph orchestration + multi-round retrieval + report generation**,” rather than simply stuffing more context into ordinary RAG. The key is not just recall, but whether the research process has been decomposed, whether evidence has been repeatedly verified, and whether a structured conclusion with citations can ultimately be produced.

**Common follow-up questions:**

- How do you ensure the reliability of the results?
- What does multi-source cross-verification mean?
- Why do such systems require more human review checkpoints?

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Understanding of complex retrieval and report generation.

### Q10-7. How do you design a Deep Research system?

The core of Deep Research is not “look up information once and then summarize,” but “conduct sustained research around a complex problem and form structured conclusions.”

A relatively complete design usually includes:

- Query planner: decompose a complex problem into sub-problems.
- Retrieval executor: perform multi-source retrieval across search, databases, and knowledge bases.
- Information fusion layer: perform deduplication, conflict detection, evidence alignment, and credibility weighting.
- Iteration controller: continue supplementary retrieval when evidence is insufficient, rather than ending after a single pass.
- Report generator: output summaries, main text, citations, and timestamps.

If expressed in a more engineering-oriented way, it can be understood as a research-oriented workflow:

- The front end is task decomposition and retrieval orchestration.
- The middle is multiple rounds of evidence collection, deduplication, and conflict handling.
- The back end is structured report generation and citation organization.

Its biggest difference from ordinary RAG is that it upgrades from “single-round Q&A” to a “multi-round research process.” Therefore, the design focus is not only on recall rate, but also on planning quality, citation quality, credibility, and process replayability. In actual implementation, it is also usually more inclined to use explicit orchestration methods such as Workflow or LangGraph, rather than handing everything over entirely to a black-box conversational Agent.

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `较难`

**Assessment focus:** Ability to decompose modules of a complex research-oriented system.

### Q10-8. How do you design a Python code interpreter?

A Python code interpreter is essentially a closed-loop system of “model-generated code + secure execution + result return.”

The core design usually includes:

- Code generation layer: the model converts user requirements into Python code.
- Sandbox execution layer: isolated environment, module allowlist, timeout limits, and resource limits.
- Result return layer: collect stdout, stderr, file artifacts, charts, and return values.
- State management layer: support preserving variables or working directories across multiple execution rounds.
- Security governance layer: prohibit dangerous system calls, network access, and unauthorized reads and writes.

The real difficulty of such a system is not “whether it can run Python,” but “how to give it execution capability without exposing the host environment.”

**Common follow-up questions:**

- If an Agent needs to execute system commands or access files, how do you prevent it from exceeding its authority to delete databases or read sensitive files on the host?
- Besides an allowlist, what other restrictions would you impose on host environment isolation?

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `较难`

**Assessment focus:** Execution-oriented agents and secure sandbox design.

**Corresponding sections:** [17 Tools Tool Invocation §6, From Course Cases to Real Projects](17-Tools%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8.md#_6-from-course-examples-to-real-projects); [21 Agent §5, Hands-on and Cases](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_5-hands-on-practice-and-case-studies)

### Q10-9. How do you design a Manus-like general-purpose agent?

For such systems, it is better not to emphasize “general-purpose” first. Instead, return to the minimal skeleton of an Agent: **model + tool set + execution loop + current state**. The so-called Manus-like system is essentially extending these four layers to longer task chains and a more complex task space.

The design usually requires:

- Task understanding and planning module: decompose goals into executable steps.
- Tool scheduling module: uniformly integrate tools such as search, browser, code execution, and file system.
- State and memory module: maintain task context, to-do items, and staged results.
- Execution and reflection module: continue execution, correct, or retry based on intermediate results.
- Security and governance module: permission control, logging, failure recovery, and human takeover.

The difference between such systems and ordinary Agents is not “more tools,” but that they need to advance tasks over a long period, handle intermediate artifacts, manage complex state, and maintain stability across longer chains. Therefore, it is closer to a general-purpose task execution framework than a scaled-up single-turn Q&A bot.

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `较难`

**Assessment focus:** Ability to decompose a general-purpose task-oriented Agent system.

### Q10-10. How do you develop a browser automation Agent?

The core of a browser automation Agent is to make “seeing the page, understanding the page, operating the page, and verifying the result” into a stable closed loop.

A relatively reasonable design usually includes:

- Page perception layer: obtain DOM, screenshots, and interactive element information.
- Decision layer: decide whether to click, input, scroll, wait, or go back based on the goal.
- Execution layer: call browser automation tools to complete actions.
- Verification layer: confirm whether the action took effect and whether the page entered the expected state.
- Governance layer: timeouts, retries, idempotency, prevention of misoperation, and log replay.

The biggest difficulty of such an Agent is not “whether it can click a button,” but that web pages are unstable, loading is asynchronous, state drifts, and the cost of misoperation is high. Therefore, awareness of verification and rollback must be built in.

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `较难`

**Assessment focus:** Browser tools, task planning, and reliability design.

### Q10-11. When an Agent needs to execute tasks in a real or simulated environment, what is the essential difference from a pure software tool-based Agent?

The biggest difference is that software-based Agents mainly operate within digital systems, with more structured inputs and outputs and stronger replayability, while Agents in real or simulated environments face perceptual noise, incomplete state, real-time feedback, and physical-world side effects.

In other words, pure software tool-based Agents are closer to “calling APIs, reading and writing data, and operating pages,” with emphasis on permissions, state machines, and tool orchestration. Real-environment Agents add perception, localization, action execution, and safety constraints. Often, “the call succeeded” does not mean completion; it is also necessary to determine whether the action actually took effect, whether the environment changed, and whether the risk is controllable.

Therefore, such systems place more emphasis on closed-loop perception, real-time performance, simulation validation, failure protection, and human takeover. Essentially, it is not about adding a few more tools, but about advancing the Agent from an “information processing system” to a “perception-decision-action closed-loop system.”

**Importance:** `中频` (occurrences: 1) | **Difficulty:** `较难`

**Assessment focus:** Understanding of the boundary between “software-based Agents” and “action-oriented / embodied environment Agents.”

---

## 11. Project Presentation and Interview Practice

### Q11-1. When an interviewer asks you to introduce a RAG / Agent project you have done, how should you present it?

A more reliable presentation order is `业务目标 -> 方案设计 -> 你负责的部分 -> 难点 -> 指标结果`.

Do not start by listing the technology stack. Instead, first explain what business problem the project solved, such as “reducing the cost of customer service document lookup” or “enabling operations staff to query data in natural language.” Then talk about the architecture, for example whether you used RAG, Tools, LangGraph, or a platform workflow. Next, focus on what you specifically did yourself, such as indexing strategy, permission design, tool integration, evaluation system, and cost optimization. Finally, give quantifiable results, such as hit rate, latency, human handoff rate, and saved human time.

If you want a more stable presentation, you can use a lightweight STAR structure suitable for application-oriented positions:

- Situation: what the business problem and constraints were.
- Task: which part you were responsible for and what the target metrics were.
- Action: what specific design, troubleshooting, and optimization you did.
- Result: final metrics, launch results, and review takeaways.

In project questions, what interviewers most often dig into is usually not “whether you have used a certain framework,” but these directions:

- Which layer you were specifically responsible for; do not present the entire team’s results as your own.
- What bad cases you encountered and how you ultimately fixed them.
- Why you made this choice rather than another solution.
- How the project’s effectiveness was evaluated after launch, and how issues were diagnosed.

**Common follow-up questions:**

- What was the hardest part of this project?
- What trade-offs did you make?
- If you had to do it again, what would you change?

**Importance:** `必刷` (occurrences: 1) | **Difficulty:** `中等`

**Assessment focus:** Project presentation ability.

**Corresponding sections:** [19 RAG Retrieval-Augmented Generation §3, RAG Comprehensive Case: Intelligent Operations Assistant](19-RAG%E6%A3%80%E7%B4%A2%E5%A2%9E%E5%BC%BA%E7%94%9F%E6%88%90.md#_3-comprehensive-rag-case-intelligent-operations-assistant); [21 Agent §5, Hands-on and Cases](21-Agent%E6%99%BA%E8%83%BD%E4%BD%93.md#_5-hands-on-practice-and-case-studies)

### Q11-2. If an interviewer asks, “Why didn’t you use a more popular framework or model?” how should you answer more reliably?

The key point of the answer is not to prove that “the current choice is always the best,” but to explain that “the current choice matches the business constraints.”

A relatively complete answer can be expanded in four layers:

- Business complexity: whether the current problem really requires a single Agent, a Workflow, or is already complex enough to require LangGraph / multi-agent.
- Engineering constraints: team familiarity, delivery cycle, observability, maintainability, and migration cost.
- Deployment conditions: whether to use an online model directly, or whether to connect to OpenAI-compatible APIs, local models, Ollama, Xinference, or similar self-hosted inference layers.
- Cost and performance: latency, throughput, token cost, model version stability, and whether there is a risk of third-party version drift.

For example, we might not choose a heavier multi-agent framework because a single Agent or Workflow is sufficient for the current task; we might not choose a larger model because latency and cost are not worthwhile; we might not choose a managed platform because we place more value on a unified OpenAI-compatible API, model control, and private deployment capability.

Going one step further, you should also naturally reflect two points:

- You know the alternatives, meaning you have not failed to do your research.
- You have left a migration path for the current solution and will not lock the system in.

**Common follow-up questions:**

- If requirements become more complex in the future, what is the migration path?
- How did you carry out technical validation?
- How do you avoid technology selection lock-in?
- If your MCP is self-developed based on Java, compared with mature Agent frameworks, where exactly does the extensibility advantage lie?

**Importance:**`高频` (occurrences: 1) | **Difficulty:**`中等`

**Assessment focus:** technical judgment and maturity of expression.

**Corresponding sections:** [9 LangChain Overview and Architecture §2, LangChain Positioning](9-LangChain%E6%A6%82%E8%BF%B0%E4%B8%8E%E6%9E%B6%E6%9E%84.md#_2-positioning-of-langchain); [7 Enterprise-grade LLM Deployment §1, Enterprise-grade LLM Deployment Overview](7-%E4%BC%81%E4%B8%9A%E7%BA%A7%E5%A4%A7%E6%A8%A1%E5%9E%8B%E9%83%A8%E7%BD%B2.md#_1-overview-of-enterprise-level-large-model-deployment)

### Q11-3. If online performance fluctuates significantly, how do you demonstrate your troubleshooting ability to the interviewer?

The most important thing is layered troubleshooting, together with a clear chain of evidence.

A more standard answer is: first confirm whether there is a change in input distribution, then check whether the model version or Prompt has changed, and then inspect retrieval recall, tool calls, context assembly, interface timeouts, and logging traces. If it is RAG, sample and check whether the query, retrieved chunks, and final answer are consistent; if it is an Agent, check whether each step of tool invocation and state progression is abnormal. Finally, check whether the evaluation set is distorted or the cache is polluted.

This kind of answer is more convincing than vaguely saying "tune parameters and optimize prompts," because it demonstrates layered troubleshooting capability.

**Common follow-up questions:**

- Have you ever encountered intermittent errors?
- How do you reproduce issues?
- How do you conduct an effective retrospective?
- How would you determine whether a problem mainly comes from model hallucination, or from the RAG, Prompt, or tool chain itself?

**Importance:**`中频` (occurrences: 1) | **Difficulty:**`中等`

**Assessment focus:** fault localization and retrospective capability.

---

## 12. Tool Ecosystem and Role Awareness

### Q12-1. Which AI development tools do you commonly use? What scenarios is each suitable for?

A relatively solid answer is not to list names, but to layer them by scenario.

They can usually be divided into several categories:

- General conversation and research: for example `ChatGPT`, `Claude`, and `Perplexity`, suitable for quickly validating ideas, organizing solutions, writing first drafts, and summarizing materials.
- AI coding collaboration: for example `Cursor`, `Claude Code`, and `GitHub Copilot`, suitable for reading code, modifying code, supplementing tests, and explaining codebase structure. The key is to see whether it leans more toward in-IDE collaboration, or toward a codebase-level Agent in the terminal.
- Low-code / workflow platforms: for example `Coze` and `Dify`, more suitable for rapid business validation, workflow orchestration, knowledge base integration, and multi-person collaboration.
- RAG / knowledge base platforms: for example `RAGFlow`, more suitable for document import, parsing, chunking, retrieval, and citation chain validation.

In a real project, we usually do not choose only one tool, but combine them by stage. For example, in the early stage we use general conversation tools to organize the approach, use a low-code platform for POC, use AI coding tools to take over core chain implementation, and later fill in evaluation, deployment, and observability.

If you need a sentence that sounds more like an interview response, you can summarize it directly like this: for approach planning and material summarization, I commonly use general tools such as `ChatGPT` and `Claude`; for code implementation and repository-level modification, I lean more toward `Cursor`, `Claude Code`, and `Copilot`; for business validation and workflow orchestration, I more often use `Dify` and `Coze`; for knowledge base chain validation, platforms like `RAGFlow` are more suitable.

What this kind of question really assesses is not "how many tools you have used," but whether you have formed your own layered mental model of tools and know what problem each tool solves.

**Importance:**`中频` (occurrences: 1) | **Difficulty:**`基础`

**Assessment focus:** awareness of the tool ecosystem, and whether you can choose tools by scenario rather than by popularity.

**Source:** Tencent AI backend engineer first-round interview (actual large-company interview question)

### Q12-2. How should we understand the differences among AI coding tools such as Cursor, Claude Code, and Copilot?

They can be understood as "all helping with development, but with different collaboration positions and interaction styles."

- Tools like Cursor lean more toward in-IDE collaboration, suitable for reading code while completing, making localized rewrites, and editing based on the current file or workspace.
- Tools like Claude Code lean more toward a codebase-level Agent in the terminal, suitable for cross-file understanding, executing commands, modifying a group of files, and completing a fuller task loop.
- Tools like Copilot lean more toward lightweight code completion and editing assistance, with advantages usually in low interruption and fitting into the existing editor workflow.

Therefore, it is not appropriate to simply judge which one is stronger; instead, we should return to the task type itself. If it is "completing while writing and quickly modifying a piece of code," in-IDE tools provide a smoother experience; if it is "understanding the entire codebase, running commands, making cross-file modifications, and completing a more complete task," terminal-based Agents have more advantages; if the team already has stable IDE habits, lightweight completion tools also have lower integration cost.

One more point can be added: tool capabilities will keep changing, so the truly stable evaluation criteria are not names, but their depth of understanding of codebase context, execution boundaries, controllability, and whether they fit the team workflow.

**Importance:**`中频` (occurrences: 1) | **Difficulty:**`基础`

**Assessment focus:** ability to compare AI coding tools, and whether you have stable selection criteria.

**Source:** Tencent AI backend engineer first-round interview (actual large-company interview question)

### Q12-3. If you were asked to summarize the differences between an "AI application engineer" and an "algorithm research role," what would you say?

It can be summarized as follows: AI application engineers focus more on "delivering model capabilities into business systems stably, safely, and at low cost," while algorithm research roles focus more on "how to improve the capability boundary of the model itself."

The former's core work usually includes technology selection, RAG / Agent architecture, tool and data integration, workflow orchestration, evaluation, deployment, monitoring, and business closure; the latter leans more toward model training, fine-tuning strategies, data construction, algorithm experiments, and metric breakthroughs. The two overlap, but their capability emphases are different.

**Importance:**`低频` (occurrences: 1) | **Difficulty:**`基础`

**Assessment focus:** whether role awareness is accurate.
