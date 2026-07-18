---
source_urls:
  - https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents
collected: 2026-07-04
published: 2025-12-11
authors: Dan Shipper, Kieran Klaassen
publication: Every — Chain of Thought
---

# Compound Engineering: How Every Codes with Agents

> Fetched rendition (WebFetch summary of the essay, 2026-07-04). Preserves the article's
> thesis, definitions, the four-phase workflow, and key quotes. Not the full verbatim text.

## Core thesis

When AI agents write ~100% of the code, traditional engineering practices become obsolete.
Every developed **"compound engineering"** — a methodology where **each completed feature
makes subsequent features easier to build**, because the learnings from each unit of work get
documented and reused by future agents. Unlike traditional engineering, where complexity
accumulates as technical debt, here complexity grows *alongside* accumulated AI knowledge,
accelerating development velocity over time.

## Definition

Compound engineering creates **"a learning loop for your agents and members of your team, so
that each bug, failed test, or problem-solving insight gets documented and used by future
agents."**

## Impact & scale

At Every, single developers now manage **five software products** serving thousands of daily
users. One developer can accomplish *"the work of five developers a few years ago, based on
our experience at Every."*

## The four-phase workflow

Effort allocation across the loop: **~80% planning and review, ~20% work and compounding.**

### 1. Plan
Developers spend roughly **40% of their time here**. Agents research the codebase and commit
history, study internet best practices, then synthesize findings into detailed implementation
plans covering objectives, proposed architecture, code approaches, research sources, and
success criteria. *"Planning helps build a shared mental model between you and the agent for
exactly what you're building, before you build it."*

### 2. Work
Agents execute the plan step-by-step. Key technique: using **model context protocols**
(Playwright, XcodeBuildMCP) that let agents **simulate actual usage while building**,
identifying and fixing issues iteratively.

### 3. Assess
Developers and automatic review agents examine output using linters, unit tests, manual
testing, and **parallel subagents checking from different angles** (security, performance,
complexity, overbuilding).

### 4. Compound
*"This is the money step."* Learnings from reviews — bugs, performance issues, reusable
solutions — get recorded and stored so agents **automatically reference them in future work**.
These become **distributed team knowledge automatically**: new hires inherit accumulated best
practices without explicit training, making them *"as well-armed to avoid common mistakes as
someone who's been on the team a long time."*

## Tools & systems

- **Primary:** Anthropic's Claude Code.
- **Alternatives:** Factory's Droid, OpenAI's Codex CLI.
- **Custom:** a Compound Engineering plugin for Claude Code (open-sourced — see companion raw file).
- **Automatic review agents mentioned:** Claude, Codex, Friday, Charlie.

## Key practice: knowledge compounding

After code reviews, agents summarize the feedback and store it as prompts/notes within the
codebase. Subsequent cycles read these learnings so *"brainstorms sharpen plans, plans inform
future plans, reviews catch more issues, and patterns get documented."* The return
mechanism — compounded learnings feeding future cycles — *"is the whole point"* of the system.
