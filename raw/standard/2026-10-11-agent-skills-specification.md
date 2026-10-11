---
source_urls:
  - https://agentskills.io/home
  - https://agentskills.io/specification
  - https://github.com/agentskills/agentskills
collected: 2026-10-11
published: Unknown
authors: Agent Skills project (originally developed by Anthropic; open to ecosystem contributions)
publication: agentskills.io
---

# Agent Skills — overview and specification

> Source assembly (2026-10-11): the site's Overview and Specification pages, fetched verbatim as Markdown (agentskills.io serves each page at `<url>.md`). The Mintlify "Documentation Index" banner was stripped from each page, and the overview's animated logo-carousel component was replaced by the adopter list it renders (name and description of each client, verbatim from the component's data, in source order). The specification carries no version number or date. Nothing else is altered.

## Agent Skills Overview

> A standardized way to give AI agents new capabilities and expertise.


### What are Agent Skills?

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows.

At its core, a skill is a folder containing a `SKILL.md` file. This file includes metadata (`name` and `description`, at minimum) and instructions that tell an agent how to perform a specific task. Skills can also bundle scripts, reference materials, templates, and other resources.

```
my-skill/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

### Why Agent Skills?

Agents are increasingly capable, but often don't have the context they need to do real work reliably. Skills solve this by packaging procedural knowledge and company-, team-, and user-specific context into portable, version-controlled folders that agents load on demand. This gives agents:

* **Domain expertise**: Capture specialized knowledge — from legal review processes to data analysis pipelines to presentation formatting — as reusable instructions and resources.
* **Repeatable workflows**: Turn multi-step tasks into consistent, auditable procedures.
* **Cross-product reuse**: Build a skill once and use it across any skills-compatible agent.

### How do Agent Skills work?

Agents load skills through **progressive disclosure**, in three stages:

1. **Discovery**: At startup, agents load only the name and description of each available skill, just enough to know when it might be relevant.

2. **Activation**: When a task matches a skill's description, the agent reads the full `SKILL.md` instructions into context.

3. **Execution**: The agent follows the instructions, optionally executing bundled code or loading referenced files as needed.

Full instructions load only when a task calls for them, so agents can keep many skills on hand with only a small context footprint.

### Where can I use Agent Skills?

Agent Skills are supported by a large number of AI tools and agentic clients — see the [Client Showcase](/clients) to explore some of them!



### Open development

The Agent Skills format was originally developed by [Anthropic](https://www.anthropic.com/), released as an open standard, and has been adopted by a growing number of agent products. The standard is open to contributions from the broader ecosystem.

Come join the discussion on [GitHub](https://github.com/agentskills/agentskills) or [Discord](https://discord.gg/MKPE9g8aUy)!

### Get started with Agent Skills

<CardGroup cols={2}>
  <Card title="Quickstart" icon="rocket" href="/skill-creation/quickstart">
    Create your first Agent Skill and see it in action.
  </Card>

  <Card title="Specification" icon="file-code" href="/specification">
    The complete format specification for Agent Skills.
  </Card>
</CardGroup>

### Adopters shown in the overview's client carousel (46)

- **Junie** — Junie is an LLM-agnostic coding agent built for real-world development. It is built on top of the IntelliJ Platform, so it understands your project the same way your editor does.
- **ZeroClaw** — ZeroClaw is an open-source, Rust-first AI agent runtime for local, provider-agnostic personal agents with Agent Skills support.
- **Gemini CLI** — Gemini CLI is an open-source AI agent that brings the power of Gemini directly into your terminal.
- **Autohand Code CLI** — Autohand Code CLI is an autonomous LLM-powered coding agent that lives in your terminal. It uses the ReAct (Reason + Act) pattern to understand your codebase, plan changes, and execute them with your approval.
- **OpenCode** — OpenCode is an open source agent that helps you write code in your terminal, IDE, or desktop.
- **OpenHands** — OpenHands is the open platform for cloud coding agents. Scale from one to thousands of agents — open source, model-agnostic, and enterprise-ready.
- **Mux** — Mux makes it easy to run parallel coding agents, each with its own isolated workspace, right from your browser or desktop. Mux is open source and LLM provider-agnostic.
- **Cursor** — Cursor is an AI editor and coding agent. Use it to understand your codebase, plan and build features, fix bugs, review changes, and work with the tools you already use.
- **Amp** — Amp is the frontier coding agent that lets you wield the full power of leading models.
- **Letta** — Letta is the platform for building stateful agents: AI with advanced memory that can learn and self-improve over time.
- **Firebender** — Firebender is the first Android-native coding agent that writes features, tests them in the emulator, and fixes issues automatically.
- **Goose** — Goose is an open source, extensible AI agent that goes beyond code suggestions — install, execute, edit, and test with any LLM.
- **GitHub Copilot** — GitHub Copilot works alongside you directly in your editor, suggesting whole lines or entire functions for you.
- **VS Code** — Visual Studio Code combines the simplicity of a code editor with what developers need for their core edit-build-debug cycle.
- **Claude Code** — Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser.
- **Claude** — Claude is Anthropic's AI, built for problem solvers. Tackle complex challenges, analyze data, write code, and think through your hardest work.
- **ChatGPT & Codex** — ChatGPT brings together agents for different kinds of work, including Codex for software development and ChatGPT Work for broader work. Use ChatGPT across desktop, web, and mobile, with Codex also available in your editor and terminal.
- **Piebald** — Piebald is a desktop & web app that makes it easier than ever to do agentic development, while at the same time giving you complete control over the configuration, context, and flow.
- **Factory** — Factory is an AI-native software development platform that works everywhere you do. From IDE to CI/CD — delegate complete tasks like refactors, incident response, and migrations to Droids without changing your tools, models, or workflow.
- **pi** — Pi is a minimal terminal coding harness. Adapt pi to your workflows, not the other way around.
- **Databricks Genie Code** — Genie Code is an autonomous AI partner purpose-built for data work in Databricks.
- **Agentman** — Agentman is an agentic healthcare platform. It automates revenue cycle workflows using AI agents without sacrificing control. Every action is testable, traceable, and auditable.
- **TRAE** — Trae is an adaptive AI IDE that transforms how you work, collaborating with you to run faster.
- **Spring AI** — Spring AI aims to streamline the development of applications that incorporate artificial intelligence functionality without unnecessary complexity.
- **Roo Code** — Roo Code puts an entire AI dev team right in your editor, outpacing closed tools with deep project-wide context, multi-step agentic coding, and unmatched developer-centric flexibility.
- **Mistral AI Vibe** — Mistral Vibe is a command-line coding assistant powered by Mistral's models. It provides a conversational interface to your codebase, allowing you to use natural language to explore, modify, and interact with your projects through a powerful set of tools.
- **Command Code** — Command Code is a coding agent that continuously learns your coding taste. Our meta neuro-symbolic AI model taste-1 with continuous reinforcement learning combines LLMs with your coding taste.
- **Ona** — Ona is a platform for background agents. Run a team of AI software engineers in the cloud. Orchestrated, governed, secured at the kernel.
- **VT Code** — VT Code is an open-source coding agent with LLM-native code understanding and robust shell safety. Supports multiple LLM providers with automatic failover and efficient context management.
- **Qodo** — Qodo is an agentic code integrity platform for reviewing, testing, and writing code, integrating AI across development workflows to strengthen code quality at every stage.
- **Laravel Boost** — Laravel Boost accelerates AI-assisted development by providing the essential guidelines and agent skills that help AI agents write high-quality Laravel applications that adhere to Laravel best practices.
- **Emdash** — Emdash is a provider-agnostic desktop app that lets you run multiple coding agents in parallel, each isolated in its own git worktree, either locally or over SSH on a remote machine.
- **Snowflake Cortex Code** — Cortex Code is an AI-driven intelligent agent integrated into the Snowflake platform, optimized for complex data engineering, analytics, machine learning, and agent-building tasks.
- **Kiro** — Kiro helps you do your best work by bringing structure to AI coding with spec-driven development.
- **Workshop** — Workshop is a cross-platform AI coding agent for building full applications. It supports multi-LLM models, sub-agents, custom agents, and skills — available as a desktop app, web app, and CLI.
- **Google AI Edge Gallery** — Google AI Edge Gallery is the premier destination for running the world's most powerful open-source Large Language Models (LLMs) on your mobile device
- **nanobot** — nanobot is an ultra-lightweight, open-source personal AI agent. It runs across multiple platforms — terminal, Telegram, Discord, Slack, WeChat, and more — with built-in MCP support and a skills system for extensibility.
- **fast-agent** — fast-agent is a simple, extendable way to interact with LLMs. Excellent for Coding, Evals, ACPX and Skills development.
- **bub** — Bub is a lightweight, hook-first Python framework for channel-native agents that live alongside people.
- **Tabnine** — Tabnine is an AI engineering platform that combines code assistants, agentic workflows, and enterprise context to help development teams build, review, and maintain software with context-aware AI—while keeping code private, secure, and fully under your control.
- **Vita** — Vita provides autonomous digital workers with virtual desktops to execute complex workflows. It learns your intent to automate end-to-end tasks like creating and posting engaging social media content.
- **Superconductor** — Superconductor is a multiplayer workspace for your team and coding agents. Run many agents in the cloud, build together in shared sessions, and ship faster with live app previews and guided code review.
- **Deep Code** — Deep Code is an open-source terminal AI coding assistant for the DeepSeek model, supporting deep thinking, reasoning effort control, and extending its capabilities with Skills and MCP.
- **Pulumi Neo** — Pulumi Neo is an AI agent that manages cloud infrastructure with Pulumi. It runs in Pulumi Cloud, the CLI, GitHub, and Slack, and works within your organization's policies and approvals.
- **Hermes Agent** — Hermes Agent is a personal AI agent by Nous Research that runs across a CLI, a desktop app, and messaging platforms. It is open source and model-agnostic, learns across sessions, and drives a real terminal and browser.
- **OpenClaw** — OpenClaw is an open-source personal AI assistant that runs locally and connects to the messaging platforms and tools you already use.

## Specification

> The complete format specification for Agent Skills.

### Directory structure

A skill is a directory containing, at minimum, a `SKILL.md` file:

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

### `SKILL.md` format

The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

#### Frontmatter

| Field | Required | Constraints |
| - | - | - |
| `name` | Yes | Max 64 characters. Lowercase letters, numbers, and hyphens only. Must not start or end with a hyphen. |
| `description` | Yes | Max 1024 characters. Non-empty. Describes what the skill does and when to use it. |
| `license` | No | License name or reference to a bundled license file. |
| `compatibility` | No | Max 500 characters. Indicates environment requirements (intended product, system packages, network access, etc.). |
| `metadata` | No | Arbitrary key-value mapping for additional metadata (a map from string keys to string values). |
| `allowed-tools` | No | Space-separated string of pre-approved tools the skill may use. (Experimental) |

<Card>
  **Minimal example:**

  ```markdown SKILL.md theme={null}
  ---
  name: skill-name
  description: A description of what this skill does and when to use it.
  ---
  ```

  **Example with optional fields:**

  ```markdown SKILL.md theme={null}
  ---
  name: pdf-processing
  description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
  license: Apache-2.0
  metadata:
    author: example-org
    version: "1.0"
  ---
  ```
</Card>

##### `name` field

The required `name` field:

* Must be 1-64 characters
* May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)
* Must not start or end with a hyphen (`-`)
* Must not contain consecutive hyphens (`--`)
* Must match the parent directory name

<Card>
  **Valid examples:**

  ```yaml theme={null}
  name: pdf-processing
  ```

  ```yaml theme={null}
  name: data-analysis
  ```

  ```yaml theme={null}
  name: code-review
  ```

  **Invalid examples:**

  ```yaml theme={null}
  name: PDF-Processing  # uppercase not allowed
  ```

  ```yaml theme={null}
  name: -pdf  # cannot start with hyphen
  ```

  ```yaml theme={null}
  name: pdf--processing  # consecutive hyphens not allowed
  ```
</Card>

##### `description` field

The required `description` field:

* Must be 1-1024 characters
* Should describe both what the skill does and when to use it
* Should include specific keywords that help agents identify relevant tasks

<Card>
  **Good example:**

  ```yaml theme={null}
  description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.
  ```

  **Poor example:**

  ```yaml theme={null}
  description: Helps with PDFs.
  ```
</Card>

##### `license` field

The optional `license` field:

* Specifies the license applied to the skill
* We recommend keeping it short (either the name of a license or the name of a bundled license file)

<Card>
  **Example:**

  ```yaml theme={null}
  license: Proprietary. LICENSE.txt has complete terms
  ```
</Card>

##### `compatibility` field

The optional `compatibility` field:

* Must be 1-500 characters if provided
* Should only be included if your skill has specific environment requirements
* Can indicate intended product, required system packages, network access needs, etc.

<Card>
  **Examples:**

  ```yaml theme={null}
  compatibility: Designed for Claude Code (or similar products)
  ```

  ```yaml theme={null}
  compatibility: Requires git, docker, jq, and access to the internet
  ```

  ```yaml theme={null}
  compatibility: Requires Python 3.14+ and uv
  ```
</Card>

<Note>
  Most skills do not need the `compatibility` field.
</Note>

##### `metadata` field

The optional `metadata` field:

* A map from string keys to string values
* Clients can use this to store additional properties not defined by the Agent Skills spec
* We recommend making your key names reasonably unique to avoid accidental conflicts

<Card>
  **Example:**

  ```yaml theme={null}
  metadata:
    author: example-org
    version: "1.0"
  ```
</Card>

##### `allowed-tools` field

The optional `allowed-tools` field:

* A space-separated string of tools that are pre-approved to run
* Experimental. Support for this field may vary between agent implementations

<Card>
  **Example:**

  ```yaml theme={null}
  allowed-tools: Bash(git:*) Bash(jq:*) Read
  ```
</Card>

#### Body content

The Markdown body after the frontmatter contains the skill instructions. There are no format restrictions. Write whatever helps agents perform the task effectively.

Recommended sections:

* Step-by-step instructions
* Examples of inputs and outputs
* Common edge cases

Note that the agent will load this entire file once it's decided to activate a skill. Consider splitting longer `SKILL.md` content into referenced files.

### Optional directories

A skill directory may contain any files and directories beyond the required `SKILL.md`. The conventions below are recommendations for organizing common types of content.

#### `scripts/`

Contains executable code that agents can run. Scripts should:

* Be self-contained or clearly document dependencies
* Include helpful error messages
* Handle edge cases gracefully

Supported languages depend on the agent implementation. Common options include Python, Bash, and JavaScript.

#### `references/`

Contains additional documentation that agents can read when needed:

* `REFERENCE.md` - Detailed technical reference
* `FORMS.md` - Form templates or structured data formats
* Domain-specific files (`finance.md`, `legal.md`, etc.)

Keep individual [reference files](#file-references) focused. Agents load these on demand, so smaller files mean less use of context.

#### `assets/`

Contains static resources:

* Templates (document templates, configuration templates)
* Images (diagrams, examples)
* Data files (lookup tables, schemas)

### Progressive disclosure

Agents load skills *progressively*, pulling in more detail only as a task calls for it. Skills should be structured to take advantage of this:

1. **Metadata** (\~100 tokens): The `name` and `description` fields are loaded at startup for all skills
2. **Instructions** (\< 5000 tokens recommended): The full `SKILL.md` body is loaded when the skill is activated
3. **Resources** (as needed): Files (e.g. those in `scripts/`, `references/`, or `assets/`) are loaded only when required

Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files.

### File references

When referencing other files in your skill, use relative paths from the skill root:

```markdown SKILL.md theme={null}
See [the reference guide](references/REFERENCE.md) for details.

Run the extraction script:
scripts/extract.py
```

Keep file references one level deep from `SKILL.md`. Avoid deeply nested reference chains.

### Validation

Use the [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) reference library to validate your skills:

```bash theme={null}
skills-ref validate ./my-skill
```

This checks that your `SKILL.md` frontmatter is valid and follows all naming conventions.
