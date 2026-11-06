# 6 - Shopkeeper Data Q&A: MySQL, Embedding Integration, and Log Management

---

**Goals of this chapter:**

- Understand the role of the `Embedding` client manager and how it connects to the subsequent vector retrieval flow.
- Understand that `MySQL` plays a dual role in this project as both a metadata database and a simulated data warehouse.
- Learn how the project uses unified logging configuration to support debugging, troubleshooting, and operational observation.

**Study suggestion:** This chapter is a wiring diagram for three foundational capabilities: Embedding turns text into vectors, MySQL stores and queries structured data, and logging lets you know where the system is at each step. When reading the code, don't just look at the wrapper classes themselves - trace where they are initialized, how they are injected into the business layer, and whether errors can be located to specific requests through the logs.

**Corresponding code branch:** `06-embedding-mysql-logging`

---

In the previous chapter, we already integrated `Qdrant` and `Elasticsearch`, but there are still two critical questions that haven't been closed:

1. Where exactly do the vectors to be written into `Qdrant` come from?
2. During retrieval, database creation, and SQL execution, how are structured data and runtime logs managed uniformly?

This chapter addresses exactly these two questions.

Placing them back into the overall architecture, they can be summarized as the following chain:

```text
文本
  -> Embedding 服务
  -> 向量
  -> Qdrant 检索

结构化元数据 / 数仓数据
  -> MySQL

运行过程
  -> Loguru + request_id + contextvars
```

In other words:

- `Embedding` is responsible for "turning text into vectors"
- `MySQL` is responsible for "storing and querying structured information well"
- The logging system is responsible for "recording clearly what was done at each step"

Taken together, these three types of capabilities are not three isolated branches; they jointly support the subsequent database building, retrieval, generation, and troubleshooting.

![How Embedding, MySQL, and logging as three foundational capabilities support the metadata knowledge base and data Q&A pipeline](../../../%E5%AE%9E%E6%88%98%E9%A1%B9%E7%9B%AE-%E7%94%B5%E5%95%86%E9%97%AE%E6%95%B0/images/6/6-0-0-1.svg)

Only when all three parts are connected can the subsequent metadata knowledge construction, hybrid recall, SQL generation, and execution truly form a closed loop.

---

## 1. Embedding Client Management

### 1.1 Introduction to Embedding

`Embedding` simply means: **turning a sentence, a field description, or a metric name into a set of numbers that can participate in vector computation.**

For example:

- Keywords in user questions need to be vectorized first before they can be used to search for similar fields and metrics in `Qdrant`
- Table descriptions, field descriptions, and metric descriptions in the metadata database also need to be vectorized first before they can be written into the vector store in advance

Therefore, this layer is not a "peripheral function"; it is a foundational capability within the entire retrieval pipeline.

In "Shopkeeper Data Q&A," we don't simply hand a natural language question to the large language model and call it done. In field recall, metric recall, and metadata knowledge construction, the system needs to first convert text into vectors, then hand them over to `Qdrant` for similarity-based retrieval. That is, there is a very important chain here: **text -> Embedding service -> vector -> Qdrant retrieval**. Without this layer, the downstream vector recall pipeline cannot run.

### 1.2 Introduction to TEI

The current project does not choose to "directly load Embedding model weights in business code." Instead, it uses:

- **Server-side component**: `Text Embeddings Inference`, abbreviated as `TEI`
- **Embedding model**: `BAAI/bge-large-zh-v1.5`

`Text Embeddings Inference`, commonly abbreviated as `TEI`. It is essentially a service framework specifically designed to deploy Embedding models and provide vector inference capabilities externally through HTTP interfaces.

Corresponding official documentation: https://huggingface.co/docs/text-embeddings-inference/index (English)

Placed into the current project, it can be understood through the following chain:

```text
BAAI/bge-large-zh-v1.5
  -> TEI 服务
  -> EmbeddingClientManager
  -> 字段召回 / 指标召回 / 元知识构建
```

In other words:

- `BAAI/bge-large-zh-v1.5` is the model that actually turns text into vectors
- `TEI` is responsible for running this model and exposing it as a callable service
- `EmbeddingClientManager` is responsible for integrating this service layer in the project

From an engineering perspective, `TEI` solves two practical problems here: there is no need to load model weights in business code, and the backend only needs to access the service via an HTTP address to obtain Embedding results.

In the current project, `TEI` still runs as an **independent service**. More specifically, it is not written as an ordinary Python class inside the backend code; instead, it starts as a container service within this project's Docker base service environment, and the backend calls it through the `host` and `port` in the configuration.

### 1.3 Overview of Common Server-Side Components

The server-side component used in the current project is `Text Embeddings Inference（TEI）`. It fits the current tutorial well because its positioning is very clear: **dedicated to Embedding model inference**.

Besides `TEI`, common server-side components on the market can be roughly divided into several categories:

- **General model serving platforms**
  For example: `Xinference`, `Ollama`, `BentoML`, `Ray Serve`
- **Large model inference frameworks**
  For example: `vLLM`, `TGI`, `SGLang`, `LMDeploy`, `Triton Inference Server`
- **Cloud provider managed services**
  For example: `OpenAI Embeddings API`, `Azure OpenAI`, `阿里云百炼`, `火山方舟`, `百度千帆`, `AWS Bedrock`

If we only consider the needs of the current project, the most important judgments are:

- If you want to **deploy an Embedding service locally or self-hosted**, `TEI` is a very suitable choice
- If you want to **centrally manage multiple types of model services**, platforms like `Xinference` are more common
- If you want to **directly call cloud Embedding APIs**, you would use the managed interfaces provided by various cloud vendors or model service providers

So this chapter uses `TEI` not because it is the only option, but because it best fits the current project's chain of "**deploy Embedding service -> expose HTTP interface -> unified backend integration**."

### 1.5 Access Methods for TEI

Official documentation: https://huggingface.co/docs/text-embeddings-inference/quick_tour (English)

`TEI` inference access mainly has **3 methods**:

- **Directly calling the native HTTP interface**: for example, using `curl` to directly request `/embed`
- **Using Hugging Face's Python client**: that is, the `InferenceClient` in `huggingface_hub`
- **Using OpenAI-compatible access**: that is, treating the interface exposed by `TEI` as an OpenAI-style `/v1/embeddings` to call

However, in the current project, these native calling methods are not directly adopted. Instead, the project chooses a solution more aligned with the overall tutorial technology stack: using the `HuggingFaceEndpointEmbeddings` provided by LangChain.

This approach has two clear benefits: it maintains consistency with the previously learned `LangChain / LangGraph` ecosystem; and when called later in the service layer and Agent nodes, the interface is more unified. That is, the current project is not unable to directly call `TEI`; rather, it deliberately chooses an integration layer that is more aligned with the overall tutorial technology stack.

### 1.6 Wrapping the Embedding Client

Corresponding file path in the project: `shopkeeper-agent/app/clients/embedding_client_manager.py`

The code is as follows:

```python
import asyncio
from typing import Optional

from huggingface_hub import AsyncInferenceClient, InferenceClient
from langchain_huggingface import HuggingFaceEndpointEmbeddings

from app.conf.app_config import EmbeddingConfig, app_config


class EmbeddingClientManager:
    def __init__(self, config: EmbeddingConfig):
        # 客户端在模块导入阶段先不立即创建，避免启动时就发起外部依赖连接
        self.client: Optional[HuggingFaceEndpointEmbeddings] = None
        # 保存 Embedding 服务配置，供 init() 时组装服务访问地址使用
        self.config = config

    def _get_url(self):
        # 当前项目通过 host + port 访问外部已启动的 Embedding 推理服务
        return f"http://{self.config.host}:{self.config.port}"

    def init(self):
        # 在应用启动阶段显式调用，完成真正的客户端初始化
        # LangChain 的 model 参数使用模型 ID，本地 TEI 地址交给底层推理客户端
        self.client = HuggingFaceEndpointEmbeddings(model=self.config.model)
        endpoint_url = f"{self._get_url()}/embed"
        self.client.client = InferenceClient(model=endpoint_url)
        self.client.async_client = AsyncInferenceClient(model=endpoint_url)


# 模块级单例，供其他模块按需复用同一个客户端管理器
embedding_client_manager = EmbeddingClientManager(app_config.embedding)


if __name__ == "__main__":
    # 本地调试入口：初始化客户端后执行一次最小化向量化调用
    embedding_client_manager.init()
    client = embedding_client_manager.client

    async def test():
        # 使用示例文本验证 Embedding 服务是否可正常响应
        text = "What is deep learning?"
        query_result = await client.aembed_query(text)
        # 只打印前 3 个维度，便于快速确认返回结果结构正确
        print(query_result[:3])

    # 运行调试测试
    asyncio.run(test())
```

Executing the file to verify, success:

```bash
(shopkeeper-agent) didilili@DidililiMacBook-Pro shopkeeper-agent % python3 -m app.clients.embedding_client_manager

[-0.005919582676142454, 0.005813124123960733, 0.018300632014870644]

```

#### 1.6.1 Responsibilities of This Wrapper Layer

If we set aside the details for now, this manager does only three things:

1. Saves the Embedding service configuration
2. Constructs the service URL based on `host + port`
3. Creates a globally reusable Embedding client

It does not handle: model training, model downloading, or vector post-processing. It handles only one thing: centrally managing "how the project accesses the Embedding service."

#### 1.6.2 Responsibilities of config and client

```python
class EmbeddingClientManager:
    def __init__(self, config: EmbeddingConfig):
        self.client: Optional[HuggingFaceEndpointEmbeddings] = None
        self.config = config
```

There are two core attributes here:

- `self.config`: saves the configuration object, which contains `host`, `port`, `model`
- `self.client`: saves the actual callable Embedding client instance

Like the earlier client managers, the constructor does not immediately complete initialization here either. Instead, the object is first created, and the client is actually instantiated later in `init()`.

#### 1.6.3 The Role of \_get_url() and URL Composition

```python
def _get_url(self):
    return f"http://{self.config.host}:{self.config.port}"
```

What happens here is not complicated, but it is critical: **it combines the `host` and `port` from the configuration file into a unified service address**.

Extracting this into a separate method has two benefits: the service address construction logic is maintained in only one place; and if the deployment method changes later, modifications will be more centralized.

In the current project, this address typically points to the `TEI` service that has already been started in the Docker environment.

#### 1.6.4 The Initialization Process of init()

```python
def init(self):
    self.client = HuggingFaceEndpointEmbeddings(model=self.config.model)
    endpoint_url = f"{self._get_url()}/embed"
    self.client.client = InferenceClient(model=endpoint_url)
    self.client.async_client = AsyncInferenceClient(model=endpoint_url)
```

Here we need to distinguish between the **model ID** and the **service address**: `HuggingFaceEndpointEmbeddings(model=...)` uses the model ID from the configuration, for example, `BAAI/bge-large-zh-v1.5`; the underlying `InferenceClient` and `AsyncInferenceClient` use the local TEI's `/embed` address, for example, `http://localhost:8081/embed`.

That is, the calling method of this client can be understood as:

- It does not directly access Hugging Face over the internet
- It does not load model weights itself
- Instead, it sends requests to the locally started TEI service

This is also why this layer is more like "service integration" than "model training" or "model loading."

#### 1.6.5 Why a close() Method Is Not Provided Separately

The earlier `Qdrant`, `Elasticsearch`, and `MySQL` clients often require explicit initialization and shutdown because they are closer to: long-lived connections, connection pools, and persistent database connections.

The current Embedding client, however, is essentially closer to **a stateless HTTP call wrapper**. It does not need to hold long-term connection resources like a database connection, so no dedicated `close()` method is written here. This is also why its implementation is noticeably lighter.

---

## 2. MySQL Client Management

### 2.1 Why Two Sets of MySQL

Many readers, when first looking at the project configuration, are most confused by this: why are there two sets of configurations when both are called MySQL?

The answer is simple: they serve two different responsibilities:

| Configuration item    | Connects to | Main responsibility                                               |
| --------- | ---------- | ------------------------------------------------------ |
| `db_meta` | Metadata database   | Stores metadata such as table information, field information, metric information, and relationships between fields and metrics |
| `db_dw`   | Simulated data warehouse | Provides the data that real business queries access, used to validate SQL and execute SQL   |

So the key understanding here is not "why the trouble," but:

> **One handles "what the system knows is in the database," and the other handles "what the system ultimately queries."**

This is also why the project ultimately creates not just one MySQL client, but two:

- `meta_mysql_client_manager`
- `dw_mysql_client_manager`

### 2.2 Introduction to SQLAlchemy

Official documentation: https://www.sqlalchemy.org/

Before diving into the MySQL client implementation, it helps to first understand `SQLAlchemy` on its own. That's because the MySQL integration in the current project is not written directly at the low-level connection layer; it is built on top of `SQLAlchemy`.

Grasp three key terms:

- **ORM**: the translation layer between database tables and Python classes. You operate on classes and objects in code, and the ORM translates those operations into SQL that the database can execute.
- **Engine**: The main entry point through which a program connects to a database, responsible for establishing a connection with the database and maintaining a group of reusable connections.
- **Session**: A working window for a specific database operation; a round of queries, writes, and commits is usually completed through it.

If we only need to remember one sentence, it can be summarized as: `Engine` is more like the "connection infrastructure," and `Session` is more like the "working context of this database operation."

### 2.3 SQLAlchemy Quick Start Example

Official documentation: https://docs.sqlalchemy.org/en/20/orm/quickstart.html

This quickstart can help us first establish the following most basic chain of understanding:

```text
声明模型
  -> 创建 Engine
  -> 建表
  -> 创建 Session
  -> 写入对象
  -> 查询对象
```

For ease of learning, the official example uses: synchronous code and an in-memory SQLite database. But the final implementation in our project uses: asynchronous code and MySQL. In other words, **the scenarios are different, but the core concepts are the same**. So this section is the most suitable for helping us understand these basic concepts such as `ORM / Engine / Session / 模型映射`.

First, look at the model declaration in the official example:

```python
from typing import List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")
```

Understand what it is expressing:

- `Base`: the base class that all ORM models inherit from
- `User`, `Address`: classes in the program, and also correspond to two tables in the database respectively
- `__tablename__`: specifies which table in the database this class maps to
- `mapped_column(...)`: defines field types, primary keys, and other information
- `relationship(...)`: used to describe relationships between tables

Next, create the `Engine`:

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)
```

One point is especially worth adding here: `Engine` is not "a single query"; it is more like the core object of the database connection layer, and it maintains a connection pool for us underneath.

Then, create tables directly from the models:

```python
Base.metadata.create_all(engine)
```

The meaning of this line of code is: **automatically generate the corresponding data table structure based on the previously declared models**. However, a reminder should also be added here: in our project, we have not taken this path of "letting the ORM create tables automatically." Because the database and table structure of the current project were already initialized during the earlier environment preparation stage, this is more about helping you understand the boundaries of SQLAlchemy's capabilities, rather than being the actual table creation method that the project relies on at runtime.

Then comes writing data, using `Session` like this:

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")

    session.add_all([spongebob, sandy, patrick])
    session.commit()
```

This section focuses on explaining two things:

- When writing data to the database, what actually interacts with the database is `Session`.
- The ORM style looks like operating on Python objects, but underneath it ultimately generates SQL and sends it to the database.

This also corresponds exactly to these two key actions: `add_all()` and `commit()`.

Finally, perform a simple query:

```python
from sqlalchemy import select

session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)
```

What this code expresses is:

- First construct a query statement `stmt`.
- Then execute this statement through `Session`.
- Finally, iterate over the ORM objects that are found.

Here you can also see that the official quickstart leans more toward demonstrating the ORM-style query approach. This ORM style can be understood as: **instead of writing SQL strings by hand, use classes, attributes, and methods in Python to express "what I want to query."** However, when it comes to the actual project, it does not force all queries to be written in this form. Because for complex SQL, especially data warehouse query scenarios, writing native SQL directly is often more intuitive and makes it easier to control the details.

Therefore, the value of this quickstart in the current tutorial can be summarized in one sentence: it mainly helps us first understand the basic components and usage order of SQLAlchemy, and then the project code later makes choices and adaptations based on the real requirements of asynchronous MySQL.

### 2.4 Wrapping the MySQL Client

The corresponding file path in the project: `shopkeeper-agent/app/clients/mysql_client_manager.py`

The core code of this part is the MySQL client wrapper in the current project. The previous `SQLAlchemy` fundamentals, quickstart, Engine and Session, all ultimately serve to help us understand this code.

Here we also need to first add a point that is easy to overlook in the course but is actually already used in the code: `asyncmy` is the MySQL asynchronous driver used by the current project. More specifically, `SQLAlchemy` is responsible for providing the database abstraction layer, while the underlying driver that actually communicates asynchronously with MySQL is `asyncmy`.

#### 2.4.1 MySQL Client Code Implementation

```python
import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)

from app.conf.app_config import DBConfig, app_config


class MySQLClientManager:
    def __init__(self, config: DBConfig):
        # Engine 是数据库连接层核心对象，底层会维护连接池
        self.engine: AsyncEngine | None = None
        # session_factory 用来按需创建新的 AsyncSession
        self.session_factory = None
        # 保存数据库配置，后面拼接连接地址要用
        self.config = config

    def _get_url(self):
        # mysql+asyncmy 表示：连接 MySQL，并使用 asyncmy 作为异步驱动
        return f"mysql+asyncmy://{self.config.user}:{self.config.password}@{self.config.host}:{self.config.port}/{self.config.database}?charset=utf8mb4"

    def init(self):
        # 创建异步 Engine，相当于先把“数据库连接能力”准备好
        self.engine = create_async_engine(
            self._get_url(), pool_size=10, pool_pre_ping=True
        )
        # 基于 Engine 创建 Session 工厂，后面真正查库时再拿 session
        self.session_factory = async_sessionmaker(
            self.engine, autoflush=True, expire_on_commit=False
        )

    async def close(self):
        # 程序结束时释放连接池资源
        await self.engine.dispose()


# 一套连元数据库，一套连数仓模拟库
meta_mysql_client_manager = MySQLClientManager(app_config.db_meta)
dw_mysql_client_manager = MySQLClientManager(app_config.db_dw)

if __name__ == "__main__":
    # 这里演示的是数仓库查询，所以先初始化 dw 这一套客户端
    dw_mysql_client_manager.init()

    async def test():
        # 通过 session_factory 创建一次数据库会话
        async with dw_mysql_client_manager.session_factory() as session:
            sql = "select * from fact_order limit 10"
            # text(sql) 表示把原生 SQL 语句交给 SQLAlchemy 执行
            result = await session.execute(text(sql))

            # mappings().fetchall() 会把结果转成“按列名访问”的行对象列表
            rows = result.mappings().fetchall()

            # 下面三行只是为了帮助观察返回结果的结构
            print(type(rows))
            print(type(rows[0]))
            print(rows[0]["order_id"])

    asyncio.run(test())

```

Execute the file to verify, and it succeeds:

```bash
(shopkeeper-agent) didilili@DidililiMacBook-Pro shopkeeper-agent % python3 -m app.clients.mysql_client_manager
<class 'list'>
<class 'sqlalchemy.engine.row.RowMapping'>
ORD20250101001
```

This manager mainly does four things:

1. Save the database configuration
2. Create the `Engine`
3. Create the `Session` factory
4. Close the connection pool when the program exits

Its approach is consistent with the previous `QdrantClientManager` and `ESClientManager`: they all belong to the infrastructure layer that provides "unified initialization, unified shutdown, and unified exposure of basic capabilities.”

#### 2.4.2 Why Engine Is Suitable for Global Reuse

There is a very critical point here: `Engine` can be understood as a global singleton, but `Session` should not be made into a global singleton.

The reason is as follows:

- `Engine` maintains a database connection pool underneath.
- A connection pool is something that should inherently be reused globally.
- If you create a new `Engine` for every request, it is equivalent to creating a whole new connection pool each time, which is very costly and unnecessary.

`Session`, on the other hand, is different. `Session` is more like the session context corresponding to one database interaction, and it should usually be **created per request and per usage scenario**, rather than keeping only one globally. Because:

- A `Session` often binds a transaction context.
- Different requests should not share the same transactional session.
- Whenever you need to access the database, create the `Session` based on the `Engine` at that time.

To summarize in a more straightforward sentence: `Engine` is responsible for maintaining connection capability over the long term, and `Session` is responsible for one specific database operation.

#### 2.4.3 Why session_factory Is What Is Actually Exposed

This is also a point that many beginners do not immediately understand when first reading the code. In the current project, there is no practice of "first creating a global `Session` object and then passing it everywhere"; instead, it does this:

```python
self.session_factory = async_sessionmaker(
    self.engine,
    autoflush=True,
    expire_on_commit=False,
    autobegin=True,
)
```

The reason is simple: the project as a whole follows an asynchronous style, and later sessions will be created repeatedly in many places. Rather than manually writing the creation logic every time, it is better to first create a unified **Session factory**. This way, whether it is API dependency injection, the metadata knowledge building script, or the Agent execution chain, all can obtain a new asynchronous session object through:

```python
async with xxx_mysql_client_manager.session_factory() as session:
    ...
```

to obtain a new asynchronous session object.

So here, `session_factory` can be regarded as: **a factory specifically used to create `AsyncSession` in batches, uniformly, and stably.**

#### 2.4.4 Explanation of pool_size, pool_pre_ping, and autoflush Parameter Configuration

This part has two layers of focus: **Engine parameters** and **Session parameters**.

First, let's look at the `Engine` layer:

```python
self.engine = create_async_engine(
    url=self._get_url(),
    pool_size=10,
    pool_pre_ping=True,
)
```

##### 2.4.4.1 pool_size=10

Indicates how many reusable connections are maintained in the connection pool by default. This value is not the larger the better; it needs to be balanced against your concurrency level, database carrying capacity, and deployment environment. For the current tutorial project, it is fine to give a teaching-friendly default value first.

##### 2.4.4.2 pool_pre_ping=True

Indicates that an availability check is performed first when retrieving a connection.

Why is this parameter important? Because the database server sometimes actively disconnects connections that have been idle for a long time. If we take a connection from the pool that "appears to still be there but has actually become invalid," subsequent queries will report errors. What `pre_ping` does is test whether this connection is still alive before actually using it.

Now look at the `Session` layer:

```python
self.session_factory = async_sessionmaker(
    self.engine,
    autoflush=True,
    expire_on_commit=False,
    autobegin=True,
)
```

##### 2.4.4.3 autoflush=True

It is easier to understand if you approach it this way:

- `add()` does not mean immediately and ultimately committing data to the database.
- Before the transaction is actually committed, many changes still remain in the current `Session`.
- The role of `flush()` is to synchronize these pending changes to the database connection layer, but the transaction has not yet been finally committed.

So the significance of `autoflush=True` is: before executing a query, the framework automatically performs a `flush` for us, avoiding the confusion of "I clearly added an object earlier, but the subsequent query still cannot see it."

Let's also take the opportunity to distinguish the two further:

- `flush`: synchronize the pending changes in the current Session to the database connection layer.
- `commit`: actually commit the transaction on the basis of `flush`.

That is to say, `flush` is not equivalent to final commit.

##### 2.4.4.4 expire_on_commit=False

If the default behavior is kept, after a transaction is committed, the object state is marked as "expired"; the next time you access the object's attributes, the ORM may try to query the database again. But in an asynchronous project, this kind of implicit re-query is not suitable as default behavior, so setting it explicitly to `False` here is to make the usage process more stable and predictable.

##### 2.4.4.5 autobegin=True

Indicates that transactions are automatically started when needed. This way, in most business code, there is no need to manually write a piece of "begin transaction" boilerplate every time.

So looking at these parameters together, they are actually solving three types of problems:

- `pool_pre_ping=True`: solves the problem of stale connections in the connection pool.
- `autoflush=True`: solves the consistency experience problem of "having written an object but not seeing it in the query."
- `expire_on_commit=False`: solves the uncertainty problem of object attribute access in asynchronous scenarios.

### 2.5 Why Not Use ORM Query Syntax

Earlier, we already compared with the `SQLAlchemy` official quickstart and also looked at the ORM-style query approach. But in practice, not all queries in the current project have been rewritten into ORM query expressions.

The reasons are very practical:

- For simple queries, using the ORM is certainly fine.
- For complex queries, especially those more like data warehouse analytical queries, native SQL is often more direct.
- The focus of the current project is not to "fully demonstrate ORM syntax," but to "stably integrate database capabilities into the backend."

So the strategy here is actually very clear:

- **Connection management and Session management** use `SQLAlchemy`.
- **Complex query statements** can still be written directly in native SQL.

This is also why the test code directly uses:

```python
await session.execute(text("select * from table_info limit 10"))
```

---

## 3. Log Management

### 3.1 Why Not Use print

Let us first emphasize a very practical issue: for temporary local testing alone, `print` is of course usable; but once you enter a formal project, it quickly becomes insufficient.

There are two main categories of reasons:

- **The output information is not standardized enough**: if you only use `print`, you usually still have to manually concatenate information such as time, module name, function name, line number, and log level.
- **The output destination is not flexible enough**: after a project goes live, logs often need to be output not only to the console but also written to log files at the same time, for easier troubleshooting and archiving.

So the key point here is not that "`print` cannot be used at all," but that: **the project needs a more stable and more configurable logging solution**.

### 3.2 Introduction to loguru

Official documentation: https://loguru.readthedocs.io/en/stable/#readme

The current project chooses `loguru` to manage logs. Looking at one of its minimal examples first will make it easier to understand why it is chosen here:

For example:

```python
from loguru import logger

logger.info("starting")
logger.warning("warning")
logger.error("error")
```

After running it directly, you can see log output with time, level, location, and colors.

However, there is another key point here: **out-of-the-box usability does not mean the project can simply copy the default configuration directly**. Because a real project usually still has these requirements:

- Whether to output to the console
- Whether to write to log files
- Where to write log files
- At what size to split into a new file
- How long to retain
- Whether to add extra fields to the log format

Therefore, the current project does not stop at "just `import logger` and print"; it goes one step further: **making logging a configurable foundational capability**.

### 3.3 Logging Description in the Configuration File

Corresponding project file path: `shopkeeper-agent/conf/app_config.yaml`

The corresponding configuration is as follows:

```yaml
logging:
  file:
    enable: true
    level: INFO
    path: logs
    rotation: "10 MB"
    retention: "7 days"
  console:
    enable: true
    level: INFO
```

The design philosophy here is well worth understanding first: logs can ultimately have two "output destinations": `console`: output to the console; `file`: output to log files.

And the role of `enable` is to decide whether this output channel is enabled.

Breaking it down further, these fields can be understood as follows:

- `level`: Sets the minimum log level for this output channel
- `path`: Specifies the log file directory
- `rotation`: Specifies the file size threshold after which a new file is split off
- `retention`: Specifies how long logs are retained

The two parameters most likely to feel unfamiliar at first are `rotation` and `retention`.

- `rotation: "10 MB"`: Indicates that when a log file reaches approximately 10MB, it is automatically split into a new file
- `retention: "7 days"`: Indicates that only logs from the most recent 7 days are retained

Why are these two parameters needed? Because if you keep writing to the same file, the log file grows larger and larger, making it inconvenient to inspect; if logs are never cleaned up, disk space will eventually be slowly consumed. So these two parameters are actually addressing the **maintainability of log files during long-term operation**.

### 3.4 Encapsulating Logging Configuration

Corresponding project file path: `shopkeeper-agent/app/core/log.py`

The code is as follows:

```python
import sys
from pathlib import Path

from loguru import logger

from app.conf.app_config import app_config
from app.core.context import request_id_ctx_var

# 统一日志展示格式，包含时间、级别、请求 ID 和调用位置等关键信息
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<magenta>request_id - {extra[request_id]}</magenta> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)


# 通过 Loguru patch 钩子，把上下文中的 request_id 写入每条日志的 extra 字段
def inject_request_id(record):
    request_id = request_id_ctx_var.get()
    record["extra"]["request_id"] = request_id


# 移除 Loguru 默认的输出目标，避免和项目自定义配置重复打印
logger.remove()

# 生成带 request_id 注入能力的 logger，后续业务代码统一使用这个实例
logger = logger.patch(inject_request_id)

# 根据配置决定是否输出控制台日志，适合本地开发和容器标准输出采集
if app_config.logging.console.enable:
    logger.add(
        sink=sys.stdout,
        level=app_config.logging.console.level,
        format=log_format,
    )

# 根据配置决定是否写入文件日志，并在启动时确保日志目录存在
if app_config.logging.file.enable:
    path = Path(app_config.logging.file.path)
    path.mkdir(parents=True, exist_ok=True)
    logger.add(
        sink=path / "app.log",
        level=app_config.logging.file.level,
        format=log_format,
        rotation=app_config.logging.file.rotation,
        retention=app_config.logging.file.retention,
        encoding="utf-8",
    )

```

#### 3.4.1 What This Encapsulation Layer Does

If we set aside the details for a moment, this logging encapsulation code primarily unifies four types of capabilities:

1. Defining a unified log format
2. Deciding whether logs are output to the console or to files
3. Enabling or disabling different output channels based on the configuration file
4. Automatically adding `request_id` to each log entry

So the focus here is not "how to print a single log entry," but rather: **how to turn logging into reusable infrastructure for the entire backend project**.

#### 3.4.2 The Role of logger.remove() and logger.add(...)

`loguru` is "ready to use out of the box" because it ships with a set of default configurations. Therefore, if a project wants to use its own log format and output strategy, the first step is usually to do:

```python
logger.remove()
```

Its purpose is: **to remove the default logging configuration first**.

Then, through:

```python
logger.add(...)
```

we add back our own output channels. In other words, the overall logic here is:

```text
移除默认配置
  -> 判断是否启用 console
  -> 判断是否启用 file
  -> 分别添加自己的日志输出规则
```

The core goal of this logging capability is "configurability." It is not hardcoded to "always print to the console," nor hardcoded to "always output to files"; instead, users decide which output channels to enable through the configuration file.

#### 3.4.3 Log Format Design

In this section, the part most worth examining carefully is `log_format`.

```python
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<magenta>request_id - {extra[request_id]}</magenta> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)
```

This is not just casually piecing together a string; it is defining: **what each log entry ultimately looks like**.

The most important fields are:

- `{time:YYYY-MM-DD HH:mm:ss.SSS}`: Time
- `{level: <8}`: Log level, aligned to a fixed width
- `{name}`: Module name
- `{function}`: Function name
- `{line}`: Line number
- `{message}`: Specific log content
- `{extra[request_id]}`: Additionally injected request identifier

What this addresses is a very practical problem: without a unified format, logs are merely "readable"; but with these fields, logs become "useful for troubleshooting."

#### 3.4.4 request_id Injection Mechanism

Corresponding project file path: `shopkeeper-agent/app/core/context.py`

```python
from contextvars import ContextVar

request_id_ctx_var = ContextVar("request_id", default="1")
```

In the logging module, it is written into the log's `extra` field through the following logic:

```python
def inject_request_id(record):
    request_id = request_id_ctx_var.get()
    record["extra"]["request_id"] = request_id
```

This layer is very important. In concurrent scenarios, if multiple requests are running simultaneously, logs become interleaved. Without a unified identifier, it is difficult to link all logs of "the same request" together.

So the role of `request_id` can be summarized in one sentence: **used to link all logs related to the same request into a single chain.**

This is also why the current project's log format specifically adds:

```python
<magenta>request_id - {extra[request_id]}</magenta>
```

#### 3.4.5 File Logging Output Strategy

```python
path = Path(app_config.logging.file.path)
path.mkdir(parents=True, exist_ok=True)
logger.add(
    sink=path / "app.log",
    level=app_config.logging.file.level,
    format=log_format,
    rotation=app_config.logging.file.rotation,
    retention=app_config.logging.file.retention,
    encoding="utf-8",
)
```

What it expresses is:

- First read the log directory from the configuration file
- If the directory does not exist, create it automatically
- Then write logs to `app.log` under this directory
- At the same time, apply the previously configured level, format, splitting strategy, and retention strategy

The design intent here is actually very clear: **not to make the logging system merely work, but to make it work stably over the long term.**

---

**Chapter Summary:**

- In the **Embedding** part, the core is to connect the relationships among **model, inference service, client encapsulation, and business invocation**.
- In the **MySQL** part, the core is to clarify the division of labor among **SQLAlchemy, Engine, Session, and Session factory**.
- In the **logging** part, the core is to understand **why formal projects need unified logging configuration, and why `request_id` is important**.
- Up to this point, these foundational services including `Qdrant / Elasticsearch / Embedding / MySQL / 日志` are essentially in place, and we can move on to the construction pipeline of the metadata knowledge base.

The next article will formally enter the **metadata knowledge base** part, starting with the overall goals, script entry points, configuration structure, and code layering, to first establish the main thread of "how metadata is organized, how it is constructed, and why it is designed this way."
