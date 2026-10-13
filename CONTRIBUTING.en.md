# Contributing to AI-Agents-From-Zero

Thanks for your interest in this project 🙌

This project aims to build a hands-on AI Agent tutorial that takes you from zero background to production-grade delivery.
All forms of contribution are welcome.

> **Note for English readers**: This is the English translation of `CONTRIBUTING.md`. The Chinese original is the source of truth — see [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## 📌 What can you contribute?

We welcome the following kinds of contributions:

- Fixing documentation errors / typos
- Expanding case descriptions
- Adding hands-on project examples
- Improving code structure
- Providing better prompt templates
- Improving RAG / Agent architecture designs
- **English translation (planned)**

---

## 🛠 How to contribute?

### 1️⃣ Fork the repository

Click "Fork" in the top right corner.

### 2️⃣ Create a new branch

```bash
git checkout -b feature/your-feature-name
```

### 3️⃣ Make your changes and commit

Keep commits small and focused. If you are changing the tutorial content, split chapters into separate commits so reviewers can follow along.

```bash
git add .
git commit -m "docs: fix typo in chapter 12"
```

For translation work, we suggest a branch named `feature/english-translation` (or `feature/en-<chapter>`) and one commit per translated file.

### 4️⃣ Push to your fork

```bash
git push origin feature/your-feature-name
```

### 5️⃣ Open a Pull Request

Open a Pull Request against the `main` branch of [didilili/ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero).
In the description, please state:

- What you changed and why
- Which files are affected
- For translations: whether the file is a full or partial translation, and whether you kept the original structure (headings, tables, code blocks, links)

---

## 🌐 Translation guidelines

If you are contributing to the English translation, please follow these conventions so the result stays consistent and reviewable:

- **Keep the directory structure**: English docs live under `en/`, mirroring the root-level chapters. Use English, kebab-case-ish filenames, e.g. `en/01-1-llm-fundamentals-and-engineering-overview.md`.
- **Never modify code blocks** other than comments. Code, config keys, environment variable names, file paths and CLI commands stay exactly as they are.
- **Keep the markdown structure** — heading levels, tables, callouts and image references should line up one-to-one with the original, so the two versions can be diffed side by side.
- **Use the shared glossary**: the English glossary (`en/Glossary.md`) holds the agreed translations of recurring terms. If a term is missing, propose it in your PR.
- **Keep Chinese where it is meaningful**: platform names, product names and proper nouns (Coze, Dify, Qwen, LLaMA-Factory, Alibaba Bailian, Shang Silicon Valley, …) are not translated.
- **Mark progress honestly**: if you only translated part of a file, add a short translator's note at the top and say so in the PR description.

---

## 📝 Commit message convention

This repository uses [commitlint](https://commitlint.js.org/) with a Husky pre-commit hook (`commitlint.config.js`).

A commit message is expected to look like:

```
<type>: <subject>
```

Common types used here include `docs`, `feat`, `fix`, `chore`, `refactor`.

Examples that pass the hook:

```
docs: translate chapter 1-1 into English
docs: add English glossary
fix: correct broken link in README
```

If a commit is rejected by the hook, fix the message rather than bypassing it with `--no-verify`.

---

## ❓ Questions

If you are unsure about anything, open an issue first and describe what you would like to work on — that also helps avoid two people translating the same chapter.
