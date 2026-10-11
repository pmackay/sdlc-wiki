---
source_urls:
  - https://docs.tessl.io/
  - https://tessl.io/registry
  - https://tessl.io/blog/skills-are-software-and-they-need-a-lifecycle-introducing-skills-on-tessl
collected: 2026-09-12
published: 2026
authors: Tessl (founded by Guy Podjarny)
publication: Tessl documentation (docs.tessl.io), CLI v0.108.0
---

# Tessl — an open platform for managing agentic development

> Source assembly (2026-09-12): the documentation's own pages, fetched verbatim as Markdown (docs.tessl.io publishes every page at `<url>.md` and indexes them at `llms.txt`). GitBook's trailing "Agent Instructions" boilerplate and the repeated llms.txt banner have been stripped from each page; nothing else is altered. The CLI reference is 122KB and is reproduced here as its **complete command index** rather than in full — every command family is listed, with the full flag documentation left at the source.
>
> Company context from search, recorded separately below and **not** part of the documentation: Tessl is a London company founded 2024 by Guy Podjarny (previously founder of Snyk and Blaze), with $125M raised ($25M seed led by boldstart/GV, $100M Series A led by Index with Accel, GV, boldstart). It advertised 3,000+ searchable skills in the registry in 2026. In 2025 it **paused Framework development and removed Framework functionality from its rebuilt CLI to concentrate on the registry and agent integrations** — the pivot that produced the product documented here.


---

## docs.tessl.io/overview/readme.md — What is Tessl?

# What is Tessl?

The core components of the Tessl platform, the agentic-development problems they solve, and why teams choose Tessl.

{% hint style="info" %}
**Takeaways**

* What are the core components of the Tessl platform?
* What problems do those components solve?
* Why choose Tessl over the alternatives?
  {% endhint %}

Tessl is an open platform for managing agentic development across your organization. It takes you from scaling skills to building your software factory, one workflow at a time.

Tessl works with every popular coding agent and is made up of six components:

| Component                      | What it is                                                                                                                                                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Registry & package manager** | Discover, install, version, and roll back skills and plugins like any other dependency. One searchable index of public and private context, agent-agnostic.                                                                                                                                                        |
| **Governance**                 | Scan and score every skill against best practices and your own company standards, with Snyk security scoring built in. RBAC controls who can create, publish, and view skills, while install and publish policies and required skills enforce your standards across every workspace, backed by a full audit trail. |
| **Evals**                      | Measure a skill or plugin's actual impact by running your agent on real-world tasks with and without the context. Every change ships with evidence instead of a guess.                                                                                                                                             |
| **Observability**              | See where skills actually activate across agent sessions, not just where they're installed. Mine agent logs to find recurring mistakes.                                                                                                                                                                            |
| **Inventory**                  | Scan your GitHub org and map every skill across every repo in one living view. Surface duplicates and unmanaged copies so you can govern what you can see.                                                                                                                                                         |
| **Tessl Agent**                | A conversational agent that drives the platform and autonomously monitors and improves your agentic setup. Runs alongside your existing agents (open beta).                                                                                                                                                        |

## What problems does Tessl solve?

See how Tessl solves the most common agentic development problems:

* Installing skills from public sources exposes you to new supply-chain and prompt-injection risk. → [Protecting yourself from insecure skills](/tutorials/protecting-against-insecure-skills.md)
* Skills sprawl into overlapping, drifting copies with no enforced standard. → [Codifying and enforcing your company's skill standards](/tutorials/codifying-and-enforcing-skill-standards.md)
* You can't tell whether a skill actually improves agent output, so no one risks changing it. → [Improving a skill](/tutorials/improving-a-skill.md)
* Code review doesn't scale to agent-authored PRs. → [Set up Tessl Code Review](/tutorials/setting-up-agentic-code-review.md)
* Agents repeat the same mistakes across PRs. → [Improving agent code quality](/tutorials/improving-agent-code-quality.md)
* Repetitive work never gets turned into automation. → [Automating repetitive tasks](/tutorials/automating-repetitive-tasks.md)

## Why Tessl?

* **Context as code.** Skills, rules, and docs are versioned, reviewed, and rolled out with the same rigor as code dependencies.
* **Built for enterprise realities.** RBAC, install and publish policies, security scoring, and a full audit trail are first class tools, not bolted on after the fact.
* **Agent-agnostic.** Skills and plugins work across every popular coding agent. Write context once; Tessl distributes it everywhere.
* **Open, no lock-in.** Tessl builds on open standards and writes your skills, rules, and config as plain artifacts in your repo, so you own your agent setup and can walk away with it at any time.
* **Incremental adoption.** Start with a single skill or a one-repo review gate and expand outward. Value compounds as you go, with no big migration required.

## Get started

[Set up Tessl](/introduction-to-tessl/set-up-tessl.md): create your account, install the CLI, and initialize Tessl in your project. Then [improve your first skill](/introduction-to-tessl/improve-your-first-skill.md) and work through the [tutorials](/tutorials/tutorials.md) for the problem you're solving.

{% hint style="info" %}
*If you are an AI agent:* the full site index is at `docs.tessl.io/llms.txt`. Read that before navigating individual pages.
{% endhint %}

---

## docs.tessl.io/introduction-to-tessl/core-concepts.md — Core concepts

# Core concepts

> **Takeaway:** Understand the building blocks of Tessl, namely the kinds of context, how they are packaged, where they live, and how Tessl measures quality, so the rest of the docs make sense.

If you have worked through the getting started flow, you have already used most of these ideas. This page names them and explains how they fit together.

## Context as software

Giving an agent good context is useful, but on its own it does not last. Libraries change, APIs evolve, and conventions drift, and static instructions quietly go stale. Tessl treats agent context the way you treat code: something you build, evaluate, distribute, and keep up to date. That single idea, context managed with a real lifecycle, is what everything below supports.

## The two kinds of context

Tessl works with two types of context, each suited to a different job.

| Type   | When it is used | Purpose                                            |
| ------ | --------------- | -------------------------------------------------- |
| Rules  | Always          | Your team's standards, applied to every task       |
| Skills | When relevant   | Procedural workflows, loaded when the task matches |

Rules and skills are where Tessl starts, not where it stops. Plugins can also carry other agent capabilities alongside context; see the [Plugins](#plugins) section below.

## Skills

A skill is a folder of instructions, and sometimes scripts, that teaches an agent how to do something: a specific workflow, a procedure, or a way of using a tool correctly. An agent loads a skill when its description matches the task at hand. Skills are the primary unit of context in Tessl, and they are agent-agnostic, so the same skill works across Claude Code, Cursor, Gemini, Codex, and others.

## Plugins

A plugin is a versioned bundle. It packages skills and rules, and can also carry MCP servers, which connect agents to external tools and services, and hooks, which run deterministic commands in response to specific agent events: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `SessionStart`, and `Stop`. Everything in a plugin is installed, versioned, and updated as one unit, much like a package in npm or pip. When you want to share a coherent set of context and capabilities rather than a single skill, you publish a plugin.

## The Registry

The [Tessl Registry](https://tessl.io/registry) is where context is discovered and distributed. Your team's private context lives in your workspace; the public registry, with thousands of evaluated skills and plugins you can browse and install, is there when you want to reach beyond it. It is also where your published quality scores appear, so others can judge whether a skill is worth installing.

## Workspaces

A workspace is the shared, private home for your team's context. It holds the skills and plugins you publish privately, controls who can access them, and is where your Skill Inventory results and the private index Tessl generates from them live. Workspace context stays with your team unless you choose to share it.

## Projects

A project is the stable anchor for Tessl inside a repository. It identifies the repository and gives Tessl a fixed place to attach repository-connected data, such as evaluation runs, so your results stay tied to the right codebase over time even as branches and checkouts come and go.

## How projects, workspaces, and plugins fit together

These three are easy to mix up, because each one groups things, but they work on different axes. A plugin is content and capability: the skills, rules, MCP servers, and hooks you package up. A workspace is ownership: the team boundary that decides who can see and publish private plugins, and where your inventory lives. A project is location: the tie between Tessl and one repository, so your results stay attached to the right codebase.

In practice, your team shares a workspace and publishes plugins to it, and in each repository where you want Tessl to track work, you create a project. A workspace can hold many plugins and back many projects, while each project belongs to one workspace and maps to a single repository.

## Reviews and evals

Tessl offers two ways to judge context quality, and they answer different questions. It is worth being clear on the distinction, because the names sound similar.

A **review** checks a single skill against best practices. It is fast and cheap, it runs automatically when you publish, and it produces a score across three areas: validation (structure and format), description (how well the description triggers the skill at the right time), and content (how well the instructions guide the agent once loaded). It is also where a team enforces its own skill-authoring standards, much like static analysis for code. Use a review for quick, structural feedback on the skill itself.

A **scenario eval** measures impact rather than structure. It runs an agent on real tasks, once with your context and once without, and compares the results, so you can see how much the context actually improves performance. Each scenario pairs a task with a rubric of weighted criteria used to grade the result. Evals are slower and more involved, and they attach to a project. Use an eval when you want evidence that context helps, not just that it is well formed.

In short: a review tells you whether a skill is well written; an eval tells you whether it works.

## Security checks

Alongside quality, Tessl checks the safety of skills and plugins. A security scan looks for risky or malicious patterns in a component's content and behavior, such as prompt injection buried in instructions, hardcoded secrets, suspicious download URLs, unverifiable external dependencies, or hidden and obfuscated text. Findings are graded by severity. Tessl surfaces critical and high severity findings when you install, warning rather than blocking and leaving the decision to you. A serious finding on a third-party skill can signal a supply-chain attack, so treat it with care.

## Next

With the vocabulary in place, the Tutorials section goes deeper on creating, improving, and distributing context.

---

## docs.tessl.io/reference/glossary.md — Glossary

# Glossary

Key concepts and terminology used throughout Tessl.

This glossary defines the core concepts you'll encounter when working with Tessl.

## Tessl CLI

Tessl's command line tool for installing, updating and managing context for coding agents.

It enables users to:

* Create, install and manage agent skills and Tessl packages across their coding agents
* Publish skills and Tessl packages to the Tessl Registry
* Locally evaluate skills and Tessl packages

## Tessl Registry

Tessl's online registry for discovering and distributing agent context.

It enables users to:

* Discover agent skills and Tessl packages (plugins) and assess their quality (via evals)
* Connect their repositories to Tessl and automatically generate context for them
* Request new skills and Tessl context

## Skill

Agent Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently, giving agents access to procedural knowledge and specific context they can load when the agent determines they're relevant (lazy push).

In Tessl, skills are treated as software with a complete lifecycle: versioned, evaluated, and maintained as dependencies and systems change.

See <https://agentskills.io/home> for more information.

## Tessl package (Plugin)

Tessl packages (or plugins) are versioned bundles of reusable, agent-agnostic context that make coding agents more effective. They can (but do not always) contain:

* Skills
* Rules

Like software packages in npm or pip, Tessl packages are versioned, dependency-managed, and can be safely updated as libraries and systems evolve.

## Tessl project

The stable home for Tessl in a Git repository. A Tessl project identifies that repository and acts as the anchor for the eval runs and other repository-connected data attached to it.

## Repository

A Git repository containing your code and history.

## Codebase

The code inside a repository.

## Working directory

The directory, or subdirectory, where you run the CLI.

## Project link

The link stored in `tessl.json` that connects a repository to a Tessl project.

## Rules

Mandatory steering for the agent to always follow, always pushed to the agent's context (eager push).

## Evaluations (evals)

Structured testing processes to systematically measure AI system performance, accuracy and reliability. Evaluations are typically contextual - they depend on the type of evaluation and the type of AI system or agent.

Tessl uses evaluations to validate that skills and context actually improve agent behavior, catch regressions as systems change, and ensure updates are safe before they reach production workflows.

The evaluations we run at Tessl typically measure the success rate of agents on real world tasks with and without some context, by:

* Generating a representative set of tasks
* Prompting agents to solve the tasks with and without the context
* Scoring the agent's solution to the tasks using grading criteria (we typically use criteria with multiple binary criteria at Tessl)
* Comparing baseline performance against performance with the context over all tasks

---

## docs.tessl.io/support/supported-platforms.md — Supported platforms

# Supported platforms

This page lists the supported version. Even if your favorite platform is not listed, it might still work  as we support many industry standards.

## Agents

Tessl supports multiple coding agents through MCP (Model Context Protocol) integration.

| Agent                          | Skills | Rules | MCP |
| ------------------------------ | ------ | ----- | --- |
| **Claude Code**                | Yes    | Yes   | Yes |
| **Cursor**                     | Yes    | Yes   | Yes |
| **Codex**                      | Yes    | Yes   | Yes |
| **Gemini CLI**                 | Yes    | Yes   | Yes |
| **Antigravity**                | Yes    | Yes   | Yes |
| **GitHub Copilot CLI**         | Yes    | Yes   | Yes |
| **GitHub Copilot for VS Code** | Yes    | Yes   | Yes |

When `tessl init` detects or you select any of the agents above (**Claude Code**, **Cursor**, **Codex**, **Gemini CLI**, **Antigravity**, **GitHub Copilot CLI**, **GitHub Copilot for VS Code**), it configures them automatically.

Other agents that support MCP can also be manually configured to work with Tessl. See [Custom agent setup](/reference/custom-agent-setup.md) for detailed instructions.

For more details on agent installation, see the [init command](/reference/cli-commands.md#tessl-init).

## Node runtime

* You need to have a modern version of Node.js installed (we use **v22.17.0 or higher**)

## Operating system

* **Supported**: Mac, Linux, Windows

On Windows, skills are linked with directory junctions rather than symbolic links. If you move or rename your project folder, run `tessl install` again to restore the links. See [Skills not found after moving the project folder on Windows](/support/troubleshooting.md#skills-not-found-after-moving-the-project-folder-on-windows).

---

## docs.tessl.io/creating-skills-and-plugins/overview.md

# Overview

Create a skill or a plugin - the packaged, versioned context you share with your team and your agents.

{% hint style="info" %}
**Takeaway** A skill teaches an agent how to do something. A plugin is how you package one or more skills, together with rules, commands, MCP servers, and hooks, so you can version and share them. Start with a skill; reach for a plugin when you need to bundle more than one thing.
{% endhint %}

A skill is a folder with a `SKILL.md` that teaches an agent how to do something. A plugin is the package that holds it: a `.tessl-plugin/plugin.json` manifest plus its content. Every skill you create with `tessl skill new` is already a minimal plugin, so "skill" and "single-skill plugin" are the same thing. You only think about plugins explicitly when you bundle more: several skills, a rule, a command, an MCP server, or a hook.

Whatever you create, you create it once. Tessl makes it work across every agent it supports, Claude Code, Cursor, Codex, and more, adapting it to each agent's own format on install. You never write a per-agent version.

The examples in this section use `engteam` as the workspace name. It is a stand-in: run `tessl workspace list` to see the workspaces you belong to, and use one of those in its place.

This section covers creating that context and getting it ready to share: writing a skill, bundling a plugin, adding an MCP server, testing locally, and publishing. It does not cover improving a skill's quality once written (see [Improving your skills](/improving-your-skills/overview-improving-skills-and-plugins.md)), enforcing a standard in CI (see [Codifying and enforcing your skill standards](/codifying-and-enforcing-your-skill-standards/overview.md)), or rolling context out across many repositories (see [Distribute](/distribute/distributing-via-registry.md)).

{% hint style="info" %}
All of this is also available through your agent. Install Tessl's plugin creator and it will do the steps below for you, from understanding the problem to building the plugin: `tessl install tessl/plugin-creator`
{% endhint %}

## In this section

|                                                                                      |                                                                              |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| [Create a skill](/creating-skills-and-plugins/create-a-skill.md)                     | Write a `SKILL.md`, scaffold it, and validate it. The common starting point. |
| [Create a plugin](/creating-skills-and-plugins/create-a-plugin.md)                   | Bundle several skills, rules, and commands into one versioned package.       |
| [Add an MCP server](/creating-skills-and-plugins/add-an-mcp-server.md)               | Give a plugin live tools or data, not just instructions.                     |
| [Develop and test locally](/creating-skills-and-plugins/develop-and-test-locally.md) | Install a plugin from your filesystem and iterate before you publish.        |
| [Publish and update](/creating-skills-and-plugins/publish-and-update.md)             | Publish to the registry, control visibility, and ship new versions.          |

## Next

* [Create a skill](/creating-skills-and-plugins/create-a-skill.md) - the fastest way to package a single capability.
* [Create a plugin](/creating-skills-and-plugins/create-a-plugin.md) - when one skill is not enough.

---

## docs.tessl.io/creating-skills-and-plugins/create-a-plugin.md

# Create a plugin

Bundle skills, rules, and commands into one versioned plugin, and choose what each piece should be.

{% hint style="info" %}
**Takeaway** Reach for a plugin when a single skill is not enough: several related skills, an always-on rule, a command, or an MCP server that belong together. Scaffold it with `tessl plugin new`, add content under the plugin directory, and validate with `tessl plugin lint`.
{% endhint %}

A single skill is already a minimal plugin. You create a plugin explicitly when you want to bundle more than one thing and version and share it as a unit: a set of related skills, a rule that captures a convention, a command the user invokes, an MCP server, or a hook. Keep a plugin focused on one responsibility; unrelated work belongs in separate plugins. Whatever it contains, Tessl installs it into each agent's native format, so one plugin serves your whole team across every agent Tessl supports.

This page covers scaffolding a plugin and choosing what each part should be. Adding an MCP server has its own page, and publishing is covered in [Publish and update](/creating-skills-and-plugins/publish-and-update.md).

{% hint style="info" %}
Your agent can decide the right shape and build it for you. Install Tessl's plugin creator with `tessl install tessl/plugin-creator`, or use Tessl Agent, which ships with it built in.
{% endhint %}

## Scaffold the plugin

`tessl plugin new` creates the plugin directory and its `.tessl-plugin/plugin.json`. Pass `--skill` or `--rules` to seed initial content, and set the workspace explicitly:

```bash
tessl plugin new --name engteam/api-conventions --summary "Conventions and workflows for our REST APIs" --workspace engteam --skill --skill-name write-endpoint --skill-description "When adding a REST endpoint" --path ./api-conventions
```

`engteam` is a stand-in workspace. Run `tessl workspace list` and use one of yours in its place.

| Flag                                             | Purpose                                                                  |
| ------------------------------------------------ | ------------------------------------------------------------------------ |
| `--name`                                         | Plugin name, `workspace/plugin` format.                                  |
| `--summary`                                      | Short description of the plugin.                                         |
| `--workspace`                                    | Workspace for the plugin. Not inferred from `--name`, set it explicitly. |
| `--path`                                         | Directory to create the plugin in.                                       |
| `--skill`, `--skill-name`, `--skill-description` | Seed an initial skill.                                                   |
| `--rules`, `--rule-description`                  | Seed an initial rule file.                                               |
| `--install`                                      | Install into the current project immediately.                            |
| `--public`                                       | Make it public. Private by default.                                      |

## Anatomy of a plugin

A plugin is a directory with a manifest and one or more content types:

```
api-conventions/
├── .tessl-plugin/
│   └── plugin.json
├── skills/
│   └── write-endpoint/SKILL.md
├── rules/
│   └── api-style.md
├── commands/
│   └── new-migration.md
└── .mcp.json
```

The manifest declares what the plugin ships:

```json
{
  "name": "engteam/api-conventions",
  "version": "0.1.0",
  "description": "Conventions and workflows for our REST APIs",
  "private": true,
  "skills": "./skills/",
  "rules": "./rules/",
  "commands": "./commands/",
  "mcpServers": ".mcp.json"
}
```

`name`, `version`, and `description` are required. `skills` and `rules` each take a path or an array of paths and default to their conventional directory (`./skills/`, `./rules/`) when it exists; `commands` and `mcpServers` are declared explicitly. The full field reference, including `author`, `homepage`, `repository`, and `license`, is in [Configuration files](/reference/configuration.md).

## Choose what each piece should be

Match the behavior you want to the right content type. Add only what earns its place.

* **Skill** - a workflow the agent reaches for when a task matches its description. Most content is skills. See [Create a skill](/creating-skills-and-plugins/create-a-skill.md). To add a further skill to a plugin, author `skills/<name>/SKILL.md` directly.
* **Rule** - an always-on convention the agent follows without being asked. A plain Markdown file in `rules/`, no frontmatter. Use a rule when something should always hold ("errors return `problem+json`"), not just during one task.
* **Command** - a named action the user invokes on demand. A Markdown file in `commands/`. Use a command when the human wants a button to press rather than something the agent decides to do.
* **MCP server** - live tools or data, not just instructions. See [Add an MCP server](/creating-skills-and-plugins/add-an-mcp-server.md).

Hooks run a command automatically at an agent lifecycle event, such as after a tool runs or when a prompt is submitted. Declare them with a `hooks` (cross-agent) or `nativeHooks` (per-agent) field in `.tessl-plugin/plugin.json`; see [Configuration files](/reference/configuration.md) for the detail.

## Validate

Lint checks the plugin structure and manifest:

```bash
tessl plugin lint ./api-conventions
```

Confirm what will actually ship by packing it and inspecting the archive, not just linting:

```bash
tessl plugin pack ./api-conventions --output /tmp/check.tgz
tar tzf /tmp/check.tgz
```

## Next

* [Add an MCP server](/creating-skills-and-plugins/add-an-mcp-server.md) - give the plugin live tools or data.
* [Develop and test locally](/creating-skills-and-plugins/develop-and-test-locally.md) - install from your filesystem and iterate.
* [Publish and update](/creating-skills-and-plugins/publish-and-update.md) - share the plugin with your team or publicly.

---

## docs.tessl.io/creating-skills-and-plugins/publish-and-update.md

# Publish and update

Publish a skill or plugin to the registry, control who can install it, and ship new versions.

{% hint style="info" %}
**Takeaway** Publish a skill or plugin with `tessl skill publish` or `tessl plugin publish`. It goes to your workspace as private by default. Bump the version to ship an update, and request public visibility only when you want anyone to install it.
{% endhint %}

Publishing puts a skill or plugin on the [Tessl Registry](https://tessl.io/registry) so it can be installed by name. This page covers the publish command, visibility, and versioning. Rolling context out across many repositories, and the GitHub-based publishing flow, are covered in [Distribute](/distribute/distributing-via-registry.md).

{% hint style="info" %}
Your agent can run this step too: `tessl install tessl/plugin-creator`
{% endhint %}

## Publish

From the skill or plugin directory, or with a path:

```bash
tessl plugin publish ./api-conventions --workspace engteam
```

`engteam` is a stand-in workspace. Run `tessl workspace list` and use one of yours.

A single skill uses the same flow through `tessl skill publish`. Both publish to your workspace as **private**: only workspace members can install it.

| Flag                         | Purpose                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------- |
| `--workspace`                | Workspace to publish under. Required when non-interactive.                        |
| `--dry-run`                  | Run every pre-publish check without publishing. Use it first.                     |
| `--bump patch\|minor\|major` | Bump the version automatically if the current one already exists on the registry. |
| `--skip-evals`               | Skip publishing the eval scenarios in `evals/`.                                   |
| `--version`                  | Publish a specific version (plugin publish).                                      |

On publish, Tessl lints and reviews the content automatically, and the review score appears on the registry. See [Check a skill's quality using review](/improving-your-skills/reviewing-skills.md).

## Install it

Once published, you or your workspace can install it in any project:

```bash
tessl install engteam/api-conventions
tessl install engteam/api-conventions@1.2.0
```

To let teammates install a private plugin, add them to the workspace with `tessl workspace add-member`. See [Workspaces](/reference/workspaces.md).

## Ship an update

1. Make your changes.
2. Bump `version` in `.tessl-plugin/plugin.json` following [semantic versioning](https://semver.org/): patch for fixes, minor for backward-compatible additions, major for breaking changes.
3. Validate with `tessl plugin lint`.
4. Publish again.

```bash
tessl plugin publish ./api-conventions --workspace engteam
```

Anyone who installed it updates by running `tessl install engteam/api-conventions` again, which fetches the latest version.

## Make it public

Public means anyone can discover and install it. It is irreversible, so it needs approval first:

1. Open your plugin or skill in the [Tessl Registry](https://tessl.io/registry) and sign in.
2. Select **Actions** then **Make Public**, and confirm the request.

Once approved, set the visibility and publish again:

* **A plugin** takes its visibility from the `private` field in `.tessl-plugin/plugin.json`. Set `"private": false` and publish.
* **A skill** can be published public directly with `--public`:

```bash
tessl skill publish ./my-skill --workspace engteam --public
```

See [Sharing with your team and publicly](/distribute/sharing-plugins-publicly.md) for more.

## Remove or deprecate

Published something you should not have, or no longer want it installed? There is no hard delete, but two options cover it. Both use `tessl plugin` whether you published a skill or a plugin.

To drop one skill from a plugin that contains others, delete the skill file and publish a new version with `tessl plugin publish`. The old version remains on the registry; the new version simply omits the skill.

* **Unpublish** removes a version as if it was never published. It has a short time limit, a couple of days after publishing:

```bash
tessl plugin unpublish --plugin engteam/api-conventions@0.1.0
```

* **Archive** hides it from search but keeps it working for anyone who already references it, so existing installs do not break:

```bash
tessl plugin archive --plugin engteam/api-conventions --reason "superseded"
```

To simply stop new people finding it, you can also make it private again: set `"private": true` in the manifest and republish, or change visibility from the registry UI.

## Next

* [Distributing via registry](/distribute/distributing-via-registry.md) - archive, unpublish, and monitor usage.
* [Distribute plugins across multiple repositories](/distribute/distribute-plugins-across-multiple-repositories.md) - push plugins across many repos.
* [Improving your skills](/improving-your-skills/overview-improving-skills-and-plugins.md) - raise quality before you publish widely.

---

## docs.tessl.io/distribute/distributing-via-registry.md

# Distributing via registry

Distribute, share, and maintain plugins through the Tessl Registry

Once you've created and published a plugin, you'll need to share it with your team, keep it updated, and manage its lifecycle. This guide covers the common tasks for managing published plugins.

## Sharing with your team

Add members to your workspace so they can access your private plugins:

```bash
tessl workspace add-member --username <tessl-username> --role member --workspace myworkspace
```

The `member` role gives read-only access to plugins. See [Roles](/administrators/roles.md) for more information about workspace roles and permissions.

To verify members have been added:

```bash
tessl workspace list-members myworkspace
```

## Installing plugins in projects

Team members can install your plugin in their projects:

```bash
tessl install myworkspace/your-plugin
```

Or search for it:

```bash
tessl search your-plugin
```

Private plugins appear in search results for workspace members just like public plugins.

To install a specific version:

```bash
tessl install myworkspace/your-plugin@1.0.0
```

## Updating documentation

When your library or service changes, update the plugin to keep documentation current.

### For automated plugins

If you used automated generation from a repository:

1. Merge code changes to your repository
2. Navigate to the Tessl interface and regenerate the plugin
3. Review new evaluation results
4. Publish the updated version

### For manual plugins

If you created the plugin manually:

1. Edit your documentation files
2. Increment the version in `.tessl-plugin/plugin.json` (following [semantic versioning](https://semver.org/))
3. Validate with `tessl plugin lint`
4. Publish with `tessl plugin publish`

**Version guidelines:**

* **Patch** (1.0.0 → 1.0.1): Bug fixes, typo corrections
* **Minor** (1.0.0 → 1.1.0): New content, backward-compatible changes
* **Major** (1.0.0 → 2.0.0): Restructuring, breaking changes

Users can update to the latest version:

```bash
tessl install myworkspace/your-plugin
```

## Archiving plugins

To remove a plugin from search results without deleting it:

```bash
tessl plugin archive --plugin myworkspace/your-plugin@1.0.0 --reason "replaced by new library"
```

Archived plugins:

* No longer appear in search results
* Cannot be installed by new users
* Remain accessible to projects that already have them installed
* Can be restored by contacting support

Use archiving when:

* A library is deprecated but still used by some projects
* You're migrating to a new plugin and want to phase out the old one
* The plugin is outdated but may still be needed for reference

## Unpublishing plugins

To completely remove a plugin within ***2 days*** of upload:

```bash
tessl plugin unpublish --plugin myworkspace/your-plugin@1.0.0
```

**Important:** Unpublishing is only available within 2 days of the original publish. After that, use archiving instead.

Unpublished plugins are completely removed and cannot be recovered.

## Monitoring plugin usage

Track how your plugins are being used:

1. Navigate to the [Tessl Registry](https://tessl.io/registry)
2. Log in and select your workspace
3. View your plugins to see usage statistics and install counts

This helps you understand which plugins are most valuable to your team.

## Best practices

* **Update regularly** - Keep documentation in sync with code changes
* **Use semantic versioning** - Help users understand the impact of updates
* **Archive deprecated plugins** - Guide users to replacement plugins
* **Monitor usage** - Focus maintenance effort on widely-used plugins
* **Document breaking changes** - Communicate major version updates to your team

## Related

* [Workspaces](/reference/workspaces.md) - Understanding workspaces and permissions
* [Configuration files](/reference/configuration.md) - Complete `.tessl-plugin/plugin.json` reference

---

## docs.tessl.io/improving-your-skills/reviewing-skills.md — Check a skill's quality using review

# Check a skill's quality using review

Run a review to score how well a skill is written, read the result, and apply fixes.

{% hint style="info" %}
**Takeaway** Run a review to score how well a skill is written, read the result, and apply fixes. A review checks the skill itself in under a minute. It does not run the skill against any task.
{% endhint %}

`tessl review` reads a skill and scores it against Tessl's standard rubric. Use it for fast feedback while you are writing a skill, or to check one before you rely on it. At a high level it tells you whether the skill is well structured and formatted, and whether its description and content are clear. It does not tell you whether the skill improves what the agent produces; for that, see [Prove a skill works using evaluation](/improving-your-skills/evaluate-skill-quality-using-scenarios.md).

A review runs through an agent that reads your whole skill bundle, not just `SKILL.md`. References, scripts, and assets are all in scope. It runs server-side: `tessl review run` polls until it finishes and prints the score, so a single command feels synchronous.

{% hint style="info" %}
All the steps on this page are also available through your agent. Install Tessl's Skill Optimizer to run reviews, apply fixes, and check scores without leaving your editor: `tessl install tessl/skill-optimizer`
{% endhint %}

{% hint style="info" %}
`tessl skill review` has been removed; `tessl review` replaces it. See [Migrate from skill review](/improving-your-skills/migrate-from-skill-review.md).
{% endhint %}

## Run a review

```bash
tessl review run ./my-skill --workspace engteam
```

The command packs the skill, uploads it, runs the review pipeline, and prints the score when it finishes. Pressing Ctrl+C detaches from the run; the review continues server-side and you can check on it later.

`tessl review run` scores quality. To scan a skill for security issues instead, run `tessl review run security ./my-skill --workspace engteam` — see [Protect against insecure skills](/tutorials/protecting-against-insecure-skills.md).

```bash
# View the most recent run
tessl review view --last

# View a specific run by ID
tessl review view <run-id>

# List recent runs
tessl review list

# Re-run a failed review
tessl review retry --last
```

## Read the score

A review produces an overall score from 0 to 100, a weighted average of three components:

|                 |                                                                                                                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Validation**  | Deterministic checks that the skill follows the [Agent Skills specification](https://agentskills.io/specification): line count, frontmatter, schema, licence, and metadata. Each check passes, warns, or fails. |
| **Description** | An LLM judge on the description, scoring how likely an agent is to load the skill at the right time. Graded on specificity, completeness, trigger term quality, and distinctiveness.                            |
| **Content**     | An LLM judge on the `SKILL.md` body, scoring how well it guides the agent once loaded. Graded on conciseness, actionability, workflow clarity, and progressive disclosure.                                      |

Each component comes with specific recommendations, for example tightening a vague description or adding trigger terms a user would naturally say. As a rough guide:

* **90% and above**: the skill conforms well to best practices.
* **70% to 89%**: a good skill, with minor improvements available.
* **Below 70%**: likely needs work before you rely on it or share it.

Example output:

```
Validation Checks

  ✔ skill_md_line_count - SKILL.md line count is 9 (<= 500)
  ✔ frontmatter_valid - YAML frontmatter is valid
  ✔ name_field - 'name' field is valid: 'format-commit-messages'
  ✔ description_field - 'description' field is valid (70 chars)
  ✔ body_present - SKILL.md body is present

Overall: PASSED (0 errors, 0 warnings)

Judge Evaluation

  Content: 85%
    A tightly written, token-efficient body that gives clear and unambiguous
    guidance for a simple task. Adding one complete worked commit-message
    example would lift actionability from good to fully concrete.

    Suggestions:
      - Add a short worked example showing a complete commit message to
        make the guidance copy-paste concrete.

  Description: 90%
    A concise, well-triggered description that clearly states both capability
    and usage conditions with natural user-facing language.

Review Score: 90%
```

## Apply fixes

`tessl review fix` runs an improve-and-review loop: it reviews the skill, applies improvements, and re-reviews. The loop runs up to `--max-iterations` times (default 3, maximum 10). It stops early once the score reaches the `--threshold` target (default 90). The highest-scoring version wins, so if no iteration improves on the original skill, no changes are applied.

```bash
tessl review fix ./my-skill --workspace engteam
```

It prompts before applying changes, since the loop edits the skill content directly. Pass `--yes` (or `-y`) to apply without a prompt, which is useful in CI or batch workflows. Review the changes before you publish.

## Score against your own standards

By default a review scores against Tessl's standard rubric, based on Anthropic's best practices. To score against your organisation's own bar instead, with your own judges and weights, run the review against a custom reviewer plugin. Pass a local directory or a `workspace/plugin` registry reference with `--review-plugin`:

```bash
tessl review run ./my-skill --workspace engteam --review-plugin <reviewer-plugin>
```

The same `--review-plugin` flag works with `tessl review fix`. To build a reviewer, see [Define your own quality standards](/codifying-and-enforcing-your-skill-standards/define-your-own-quality-standards.md).

## Gate a pull request on a review score

You can run the same review in CI and fail the build when the score is too low. Combine `--json` with `--threshold`:

```bash
tessl review run ./my-skill --workspace engteam --json --threshold 80
```

The command exits non-zero when the score is below the threshold, so the CI step fails. For a complete GitHub Actions workflow, see [Gate skill quality in CI](/codifying-and-enforcing-your-skill-standards/gate-skill-quality-in-ci.md).

## Reviews when you publish

You do not have to run a review by hand. When you publish a plugin to the registry, Tessl lints and reviews it automatically, and the score appears on the registry. See [Distributing via registry](/distribute/distributing-via-registry.md).

## Prerequisites

`tessl review run` and `tessl review fix` need authentication and a workspace. The companion commands `view`, `list`, and `retry` need authentication only.

* Authentication, either a logged-in session, confirmed with `tessl whoami` and started with `tessl login`, or a `TESSL_TOKEN` API key in the environment. Any workspace member can run a review.
* A workspace to attribute the run to, passed with `--workspace`. It is required when `--json` is set, because a non-interactive run cannot prompt for one.

## Next

* [Prove a skill works using evaluation](/improving-your-skills/evaluate-skill-quality-using-scenarios.md) - measure whether a skill changes an agent's output, not just how it reads.
* [Codifying and enforcing your skill standards](/codifying-and-enforcing-your-skill-standards/overview.md) - build a custom rubric, set an organisation-wide quality bar, and gate pull requests on it.

---

## docs.tessl.io/improving-your-skills/evaluate-skill-quality-using-scenarios.md — Prove a skill works using evaluation

# Prove a skill works using evaluation

Generate scenarios, run an evaluation, and read the score difference to see whether a skill actually changes what an agent produces.

{% hint style="info" %}
**Takeaway** Generate scenarios from a skill, run an evaluation, and read the score difference to see whether the skill actually changes what an agent produces. Scenarios are saved with the skill, so they become a regression test you re-run after every change.
{% endhint %}

An evaluation runs an agent on real tasks twice, once without the skill and once with it, then scores the difference. That difference is the skill's value: proof it changes what the agent does, not just that it reads well. Where a review checks the skill itself, an evaluation measures its effect.

Evaluation is more rigorous than review and takes longer to set up and run. Reach for it when you need confidence a skill works, for example before you publish it or share it into a repository where you will not see how others' agents use it.

You can evaluate a single skill against generated scenarios, or evaluate context files against real tasks taken from your codebase's commit history. Both run through the same `tessl eval` commands.

{% hint style="info" %}
All the steps on this page are also available through your agent. Install Tessl's Skill Optimizer to generate scenarios, run evaluations, and improve skills without leaving your editor: `tessl install tessl/skill-optimizer`
{% endhint %}

## Skills are evaluated inside Tessl plugins

A Tessl plugin is a structure that bundles the skills, rules, and documentation an agent needs for an area of context, packaged so it can be versioned and shared. An evaluation generates scenarios and produces results, and a plugin is the natural place to keep them with the skill they belong to.

For this reason `tessl eval run` expects the generated scenarios to live inside the plugin, and the shorthand `tessl eval run ./my-skill` expects a directory containing a `.tessl-plugin/plugin.json`. If you have a standalone skill, import it into a plugin first:

```bash
tessl skill import ./my-skill
```

## Generate scenarios

Scenarios are the tasks an agent is assessed against. Generate them from the plugin:

```bash
tessl scenario generate ./my-skill
```

Each generated scenario is put through a feasibility check on the server. Only scenarios that pass are saved, so the generator gives you tests that actually exercise the skill rather than filler.

`--count` sets how many scenarios to target, and defaults to 3. Pass a higher number to cover more of what the skill claims to do. For a narrowly scoped skill the generator may return fewer than requested, because it will not save scenarios that fail the feasibility check.

```bash
tessl scenario generate ./my-skill --count 5
```

Generation runs server-side. Check progress with `tessl scenario list --mine`, then download the scenarios once it completes:

```bash
tessl scenario download --last
```

When run from inside a plugin directory (or any subdirectory of one), `tessl scenario download` writes scenarios directly into the plugin's `evals/` directory, so they are immediately runnable by `tessl eval run`. When run outside a plugin, it writes to an `evals/` directory relative to your current directory. Override the location with `--output`, and choose whether new scenarios merge with or replace existing ones with `--strategy merge` (the default) or `--strategy replace`. The command always prints where the files landed.

{% hint style="warning" %}
**The default destination is the plugin's `evals/`, wherever you run from inside the plugin.** Two consequences follow from this:

* `--strategy replace` clears the plugin's `evals/` directory before writing, even when you run from a subdirectory such as `src/`. It does not target `src/evals`. Pass `--output <dir>` to replace a different directory.
* `--strategy merge` (the default) overwrites existing scenario files with the same name. Scenario names are canonical (`scenario-1/`, `scenario-2/`, …), so a re-download replaces `scenario-1/` and any hand-edits in it. Copy edited scenarios you want to keep to a directory the download will not touch, or download with `--output` to a separate directory.
  {% endhint %}

The scenarios are saved with the skill, so anyone who changes it later can re-run the same scenarios and confirm it still behaves as expected.

You do not have to generate scenarios. You or your agent can write them by hand instead, as long as they sit in the plugin's `evals/` directory, one scenario per subdirectory. See [File formats](#file-formats) for the structure.

### Generate scenarios from your codebase

Instead of generating scenarios from a skill, you can build them from real changes in your repository, so the tasks reflect work your team actually does. Point `tessl scenario generate` at a repository with commit hashes or PR numbers:

```bash
# From commits
tessl scenario generate org/repo --commits abc123,def456 --workspace engteam

# From pull requests
tessl scenario generate org/repo --prs 42,107 --workspace engteam
```

Tessl analyses each diff and reconstructs the intent of the change as a task brief and a scoring rubric. The starting state has your context files stripped out, so the agent solves the task without them.

`--context` tells Tessl which files are context files. The patterns are saved in each scenario as the codebase fixture's exclude list. When omitted, Tessl excludes `*.mdc`, `*.md`, `tile.json`, `.tessl-plugin/plugin.json`, `tessl.json`, and `.tessl/` by default.

To browse recent commits and choose which to turn into scenarios, use `tessl repo select-commits org/repo`. It accepts `--keyword`, `--author`, `--since` / `--until`, and `--count`, and prints a table of commit hashes to pass to `generate`.

{% hint style="info" %}
Your GitHub or GitLab account must be connected in workspace settings.
{% endhint %}

Because these scenarios start from a state with your context files stripped out, pass `--context` again at run time with a glob matching those files. This adds a with-context variant on top of the baseline so you can measure the delta:

```bash
tessl eval run ./my-skill/evals/ --context 'src/**/*.knowledge.md'
```

Match the `--context` glob to the files each scenario excludes. With no `--context`, only the baseline runs.

## Run an evaluation

```bash
tessl eval run ./my-skill
```

The agent solves each scenario twice, without the skill and with it, and a judge scores both against a per-scenario rubric. The run reports the baseline score, the with-skill score, and the difference between them. Runs can take a while; pressing Ctrl+C detaches and the run continues server-side.

Label a run to find it again later:

```bash
tessl eval run ./my-skill --label "baseline"
```

```bash
# List your recent runs
tessl eval list --mine

# View a run, including the per-scenario breakdown
tessl eval view --last
tessl eval view abc123

# Retry a failed run
tessl eval retry abc123
```

## Read the result

A run produces output like this:

```
Eval Results: baseline

Agent:     claude:deepseek-v4-flash
Variants:  Without this plugin, With this plugin
Status:    Completed

Scenario: Commit message formatting for complex refactor

  Without this plugin
  Check                         Score
  ------------------------------------------
  Conventional Commits format   30/30  (100%)
  Valid type                    0/20   (0%)
  Subject line <= 72 chars      0/30   (0%)
  Blank line separator          20/20  (100%)
  Total                         50/100  (50%)

  With this plugin
  Check                         Score
  ------------------------------------------
  Conventional Commits format   30/30  (100%)
  Valid type                    20/20  (100%)
  Subject line <= 72 chars      30/30  (100%)
  Blank line separator          20/20  (100%)
  Total                         100/100  (100%)

Scenario: Type selection for a small fix

  Without this plugin
  Total                         90/100  (90%)

  With this plugin
  Total                         95/100  (95%)

Summary
  Scenarios: 3 completed
  Without this plugin avg:  71%
  With this plugin avg:     92%
```

The score difference tells you what the skill is worth:

* **A large positive difference** means the skill reliably moves the agent toward the right behaviour.
* **Little or no difference** means the agent already did the task well without the skill, or the skill is not landing.
* **A small negative difference** is usually normal model variance, not evidence the skill is harmful.
* **A large or consistent negative difference** is a real sign the skill is confusing the agent or pushing it toward unhelpful behaviour, and the content needs work.

Read the per-scenario breakdown rather than just the headline average, since a strong result on one scenario can hide a weak one on another.

### Outcome and activation

A standard evaluation measures **outcome**: with the context forced on, does the agent produce better work against the rubric. It does not test whether the agent would have loaded the skill on its own.

To measure **activation**, whether the agent picks up the skill itself without being told to, add `--skip-forced-context-activation`. A skill can score well on outcome but fail to activate, which means it would not help in practice because the agent never reaches for it.

```bash
# Measure activation only: don't force the context, and skip outcome scoring
tessl eval run ./my-skill --skip-forced-context-activation --skip-scoring
```

The two flags are independent: `--skip-forced-context-activation` stops forcing the context so activation can be observed, and `--skip-scoring` skips rubric scoring. Used together they give a pure activation check.

Example activation output:

```
Activation Results

Agent:     claude:deepseek-v4-flash
Variants:  baseline, with context
Status:    Completed

Injected context
Plugin: format-commit-messages@0.1.0

Scenario                                            Activated skills
--------------------------------------------------------------------
1. Conventional Commits format and type selection   format-commit-messages
2. Commit message formatting for complex refactor   format-commit-messages
3. Conventional Commits with multi-line message     —
```

`—` in the Activated skills column means the skill was not selected by the agent on its own. A skill that does not activate is a description problem, best fixed with a [review](/improving-your-skills/reviewing-skills.md). A skill that activates but does not improve the outcome is a content problem to fix in the skill body.

## Choose how rigorous to be

Evaluation is a toolkit, not a single fixed test. Scale the rigour to how much confidence you need.

* **More scenarios.** Generate a higher `--count` to cover more of what the skill claims to do.
* **Repeated runs.** An evaluation runs a real agent, and agents are non-deterministic, so a single run can mislead. Pass `--runs` (or `-n`) to run each scenario several times and average out the variance. Worth doing before you publish.
* **Different agents.** Run the evaluation against more than one agent with `--agent` to check the skill holds up across the models your team uses.
* **Quality filter.** Pass `--quality-check` to exclude scenarios the platform judges low-feasibility, rubric-leaking, or low-signal at run time, a stricter filter than the one applied at generation.
* **Skip the baseline.** Pass `--skip-baseline` to run only the with-context variant when you do not need the comparison.
* **Override the scorer.** Pass `--scorer-agent` to score with a different agent from the one solving the tasks.

## Passing secrets to an evaluation

Some scenarios need external credentials, for example an API key or a database URL. The `--env-file` flag encrypts a local `.env` file client-side and injects the variables into the eval sandbox, where setup scripts and the agent inherit them:

```bash
tessl eval run ./my-skill --env-file ./secrets.env
```

The file uses standard `KEY=VALUE` lines; blank lines and `#` comments are ignored. The CLI rejects reserved keys at submit time, including `LITELLM_ADMIN_KEY`, `LITELLM_MASTER_KEY`, `UPLOAD_WORKSPACE`, `DOWNLOAD_WORKSPACE`, and any key prefixed `AWS_`, `S3_`, `DAYTONA_`, or `RECIPE_RUN_`. Rename conflicting keys before running.

## Choosing an agent

By default an evaluation runs against agent `claude`, and in the US region model `deepseek-v4-flash`. Choose a different agent and model with `--agent` and `--model`. An evaluation takes a single agent and model; to compare models, run it once per model.

The default model and the available models both depend on the region you are connected to: the open-weight models below (DeepSeek, GLM, Kimi, Qwen, MiniMax, GPT OSS, and Nemotron) are not offered in the EU region, which defaults to a Claude model instead. Run `tessl eval run --list-agents` to print the models and the default for your region.

```bash
$ tessl eval run ./my-skill --agent claude --model claude-opus-4-8
```

`--agent` values: `claude`, `codex`, `tessl`. Pair each with a `--model` value from its tab below.

{% tabs %}
{% tab title="Claude" %}

| Model             | `--model` value     |
| ----------------- | ------------------- |
| Claude Fable 5    | `claude-fable-5`    |
| Claude Opus 5     | `claude-opus-5`     |
| Claude Opus 4.8   | `claude-opus-4-8`   |
| Claude Opus 4.7   | `claude-opus-4-7`   |
| Claude Opus 4.6   | `claude-opus-4-6`   |
| Claude Sonnet 5   | `claude-sonnet-5`   |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` |
| Claude Opus 4.5   | `claude-opus-4-5`   |
| Claude Sonnet 4.5 | `claude-sonnet-4-5` |
| Claude Haiku 4.5  | `claude-haiku-4-5`  |
| {% endtab %}      |                     |

{% tab title="Other hosted models" %}
Also served through `--agent claude`.

| Model                       | `--model` value          |
| --------------------------- | ------------------------ |
| Deepseek V4 Flash (default) | `deepseek-v4-flash`      |
| Deepseek V4 Pro             | `deepseek-v4-pro`        |
| Kimi K2.6                   | `kimi-k2.6`              |
| Kimi K2.7 Code              | `kimi-k2.7-code`         |
| GLM 5.2                     | `glm-5.2`                |
| Qwen3.7 Plus                | `qwen3.7-plus`           |
| MiniMax M3                  | `minimax-m3`             |
| MiniMax M2.7                | `minimax-m2.7`           |
| GPT OSS 20B                 | `gpt-oss-20b`            |
| GPT OSS 120B                | `gpt-oss-120b`           |
| Nemotron 3 Ultra            | `nemotron-3-ultra-nvfp4` |
| {% endtab %}                |                          |

{% tab title="Codex" %}

| Model         | `--model` value |
| ------------- | --------------- |
| GPT 5.6 Sol   | `gpt-5.6-sol`   |
| GPT 5.6 Terra | `gpt-5.6-terra` |
| GPT 5.6 Luna  | `gpt-5.6-luna`  |
| GPT 5.5       | `gpt-5.5`       |
| GPT 5.4       | `gpt-5.4`       |
| GPT 5.4 Mini  | `gpt-5.4-mini`  |
| GPT 5.4 Nano  | `gpt-5.4-nano`  |
| GPT 5 Codex   | `gpt-5-codex`   |
| GPT 5.3 Codex | `gpt-5.3-codex` |
| GPT 5.2 Codex | `gpt-5.2-codex` |
| GPT 4.1       | `gpt-4.1`       |
| GPT 4.1 Mini  | `gpt-4.1-mini`  |
| {% endtab %}  |                 |

{% tab title="Tessl" %}

| Model             | `--model` value          |
| ----------------- | ------------------------ |
| Claude Fable 5    | `claude-fable-5`         |
| Claude Opus 5     | `claude-opus-5`          |
| Claude Opus 4.8   | `claude-opus-4-8`        |
| Claude Opus 4.7   | `claude-opus-4-7`        |
| Claude Opus 4.6   | `claude-opus-4-6`        |
| Claude Sonnet 5   | `claude-sonnet-5`        |
| Claude Sonnet 4.6 | `claude-sonnet-4-6`      |
| Claude Opus 4.5   | `claude-opus-4-5`        |
| Claude Sonnet 4.5 | `claude-sonnet-4-5`      |
| Claude Haiku 4.5  | `claude-haiku-4-5`       |
| Kimi K2.6         | `kimi-k2.6`              |
| Deepseek V4 Flash | `deepseek-v4-flash`      |
| GLM 5.2           | `glm-5.2`                |
| Kimi K2.7 Code    | `kimi-k2.7-code`         |
| Qwen3.7 Plus      | `qwen3.7-plus`           |
| MiniMax M3        | `minimax-m3`             |
| Deepseek V4 Pro   | `deepseek-v4-pro`        |
| MiniMax M2.7      | `minimax-m2.7`           |
| GPT OSS 20B       | `gpt-oss-20b`            |
| GPT OSS 120B      | `gpt-oss-120b`           |
| Nemotron 3 Ultra  | `nemotron-3-ultra-nvfp4` |
| {% endtab %}      |                          |
| {% endtabs %}     |                          |

## Evaluations when you publish

Publishing a plugin to the registry runs an evaluation as part of publishing, and the results appear on the registry. The evaluation is optional: pass `--skip-evals` to publish without it, or `--with-scenario-quality-check` to apply the quality filter to the publish-time run. See [Distributing via registry](/distribute/distributing-via-registry.md).

## Prerequisites

* Authentication, either a logged-in session, confirmed with `tessl whoami` and started with `tessl login`, or a `TESSL_TOKEN` API key in the environment.
* Workspace access at Publisher level or above.
* A Tessl project, so Tessl knows which repository an evaluation belongs to and your results stay tied to your codebase over time. Create one with `tessl project create <name> --workspace engteam`, link an existing one with `tessl project link`, and repair a broken link with `tessl project repair`. See [Projects overview](/projects/overview.md).

A plugin that holds evaluations looks like this on disk:

```
my-plugin/
├── .tessl-plugin/
│   └── plugin.json      workspace, name, version
├── skills/<name>/SKILL.md
├── tessl.json           links the directory to a Tessl project
└── evals/
    └── scenario-name/
        ├── task.md          the task brief the agent sees
        ├── criteria.json    the scoring rubric
        └── scenario.json    fixture and include declarations
```

## File formats

### task.md

Free-form markdown, and the only file the agent sees. Typically structured with problem, expected behaviour, and acceptance criteria sections. Edit it freely before running.

### criteria.json

Defines how a solution is scored, as a weighted checklist:

```json
{
  "context": "Brief description of what is being evaluated.",
  "type": "weighted_checklist",
  "checklist": [
    {
      "name": "fixes_syntax_error",
      "description": "The solution adds the missing closing parenthesis.",
      "max_score": 1,
      "category": "INTENT"
    }
  ]
}
```

Each checklist item carries a `category`: `INTENT`, `DESIGN`, `MUST_NOT`, `MINIMALITY`, `REUSE`, `INTEGRATION`, or `EDGE_CASE`. The score is the sum of awarded scores over the sum of maximum scores, as a percentage, and the grader can award partial credit.

### scenario.json

Optional. Declares fixtures, included files, and setup scripts. A skill scenario can simply list `include` paths to copy into the working directory. A codebase scenario carries a commit fixture with the repository URL, the starting commit, and the context exclude patterns. See the [configuration reference](/reference/configuration.md) for the full schema.

## Next

* [Codifying and enforcing your skill standards](/codifying-and-enforcing-your-skill-standards/overview.md) - set an organisation-wide quality bar and enforce it.
* [Troubleshooting reviews and evaluations](/improving-your-skills/troubleshooting-reviews-and-evals.md) - what to do when a run fails or scores look wrong.

---

## docs.tessl.io/codifying-and-enforcing-your-skill-standards/overview.md

# Overview

Gate skill quality automatically and define your organisation's standard for what a good skill looks like.

{% hint style="info" %}
**Takeaway** Keep poor-quality skills out of your repository. Set the bar for what "good" means, then gate it in CI so skills that fall short do not get merged.
{% endhint %}

When a team shares skills, quality stops being a personal matter. A weak skill that one person tolerates becomes everyone's problem once it is in the shared repository, shaping how every agent on the team behaves. This section is about holding a quality line automatically, so you do not depend on everyone remembering to check.

There are two parts to it:

* **Gate on a review score.** Run a review in CI and fail the build when a skill scores below your bar, so substandard skills never merge. See [Gate skill quality in CI](/codifying-and-enforcing-your-skill-standards/gate-skill-quality-in-ci.md).
* **Define your own bar.** The default rubric scores against general best practices. Fork it to encode what your organisation cares about, and apply it to every review. See [Define your own quality standards](/codifying-and-enforcing-your-skill-standards/define-your-own-quality-standards.md).

This section covers protecting a repository from low-quality skills. It does not cover managing your wider skill estate, surveying what is installed across your organisation, or org-level policy; those are separate capabilities.

## Next

* [Gate skill quality in CI](/codifying-and-enforcing-your-skill-standards/gate-skill-quality-in-ci.md) - run reviews on pull requests and block merges below your threshold.
* [Define your own quality standards](/codifying-and-enforcing-your-skill-standards/define-your-own-quality-standards.md) - build a custom rubric and apply it to every review.

---

## docs.tessl.io/codifying-and-enforcing-your-skill-standards/gate-skill-quality-in-ci.md

# Gate skill quality in CI

Run a review on every pull request and fail the build when a skill scores below your threshold.

{% hint style="info" %}
**Takeaway** Run a review on every pull request and fail the build when a skill scores below your threshold. Skills that fall short of the bar never merge.
{% endhint %}

A review tells one person whether a skill is good. Gating in CI applies that check to everyone, automatically, so a substandard skill cannot reach your shared repository in the first place.

## Fail a build below a threshold

Pass `--threshold` to exit non-zero when a review score falls below your bar:

```bash
tessl review run ./my-skill --workspace engteam --threshold 80
```

`--threshold` takes a 0-100 integer. The default is 0, which never fails. Any value above 0 causes the command to exit non-zero - and fail the CI step - when the score falls below it.

Add `--json` when you need machine-readable output, for example in a script that reads the score programmatically:

```bash
tessl review run ./my-skill --workspace engteam --json --threshold 80
```

`--workspace` is required when `--json` is set, because a non-interactive run cannot prompt for one. In practice, always pass `--workspace` in CI regardless.

You can also re-check an existing run against a threshold without starting a new review:

```bash
tessl review view <run-id> --json --threshold 80
```

## Authenticating in CI

A review runs against your workspace, so CI needs to authenticate without an interactive login. Create an API key for your workspace:

```bash
tessl api-key create --workspace engteam
```

Set the key as a repository secret named `TESSL_TOKEN`. The CLI and the Tessl GitHub Action both read it from that variable.

### Keys expire after 30 days

Every API key expires. Unless you pass `--expiry-date`, the key you just created is valid for **30 days from creation**, and the CLI prints the exact date when it issues the key.

This matters most in CI, because nothing fails at the moment the key expires. Your pipeline stays green for a month and then starts failing authentication on a run that changed nothing. Put a reminder in your calendar, or pass a longer `--expiry-date` when you create the key:

```bash
tessl api-key create --workspace engteam --name ci --role member --expiry-date 2027-12-31T00:00:00Z
```

### Rotating a CI key

Rotation is always something you run from your own machine, never from inside the pipeline. An API key cannot create another API key, which means a leaked CI credential cannot renew itself. That is deliberate.

Two paths, depending on whether the key has already expired.

**The key has already expired.** Your pipeline is broken, so there is no window to protect. Replace it under the same name:

```bash
tessl api-key delete --workspace engteam ci
tessl api-key create --workspace engteam --name ci --role member
```

**The key is still valid.** Create the replacement under a new name first, confirm a run passes with it, and only then remove the old key. Your pipeline is never without a working credential:

```bash
tessl api-key create --workspace engteam --name ci-2 --role member
# update the secret, confirm a run passes, then:
tessl api-key delete --workspace engteam ci
```

Key names are unique per workspace, which is why the second path needs a different name rather than reusing `ci`.

Both paths involve reading your pipeline to find which secret feeds `TESSL_TOKEN`, and that secret can be named anything. `tessl agent` can do that part for you: ask it to rotate your Tessl CI key and it finds the secret, shows you a plan naming where each fact came from, and waits for a go-ahead before it changes anything.

```bash
tessl agent "rotate my Tessl CI key"
```

Nothing to install. The skill behind this ships with the CLI.

Use `tessl api-key list --workspace engteam --json` when you want key ids, roles, or expiry dates in a script.

### Where the key lives on each CI platform

Whatever your platform, the CLI reads the key from the `TESSL_TOKEN` environment variable. What changes is where the secret behind that variable is stored. The secret itself can be named anything, so check your pipeline definition to see which one it maps to `TESSL_TOKEN`.

| Platform            | Where the secret lives                                 | CLI                            |
| ------------------- | ------------------------------------------------------ | ------------------------------ |
| GitHub Actions      | Settings > Secrets and variables > Actions             | `gh secret set <secret>`       |
| GitLab CI           | Settings > CI/CD > Variables                           | `glab variable set <variable>` |
| CircleCI            | Project Settings > Environment Variables               |                                |
| Buildkite           | Pipeline Settings > Secrets                            | `bk secret set <secret>`       |
| Azure Pipelines     | Pipelines > Library                                    | `az pipelines variable update` |
| Jenkins             | Manage Jenkins > Credentials                           |                                |
| Bitbucket Pipelines | Repository settings > Pipelines > Repository variables |                                |
| TeamCity            | Build Configuration > Parameters                       |                                |

When a key expires, the CLI names your platform and its secret location in the error, so you do not have to come back to this table.

## Run it on pull requests

Tessl publishes a GitHub Action that installs the CLI and runs this gate on pull requests, so you do not have to wire up the CLI by hand. For the complete workflow, see [Review, lint & publish with GitHub Actions](/distribute/review-and-publish-with-github-actions.md).

## Next

* [Define your own quality standards](/codifying-and-enforcing-your-skill-standards/define-your-own-quality-standards.md) - gate against your organisation's own rubric, not just the default.
* [Check a skill's quality using review](/improving-your-skills/reviewing-skills.md) - full reference for `tessl review run`, score interpretation, and applying fixes.

---

## docs.tessl.io/tutorials/protecting-against-insecure-skills.md

# Protecting yourself from insecure skills

Inventory the skills running across your org, read their Snyk-powered security scores, and use install policies to block risky skills before they reach a developer.

{% hint style="info" %}
**Takeaways**

* How to inventory the skills across your org and tell first-party skills from matched third-party ones.
* How Snyk-powered security scores surface on import, and how to review any skill on demand.
* How an admin sets org, workspace, or project install policies to block risky skills.
  {% endhint %}

Skills run inside your agent with access to your code, your shell, and your secrets. A skill pulled from a public source can carry a prompt-injection payload or instructions that exfiltrate data, and the risk compounds once a skill spreads across repos. The danger is not only external: a first-party skill can leak credentials through an honest mistake by the developer who wrote it, or carry a deliberate payload from an insider. This tutorial maps what is already installed, reads each skill's security score, and gates future installs against a policy.

## Inventory the skills across your org

Start from what is already running. `tessl inventory import` scans the repositories in a GitHub org through your local `gh` CLI and uploads the result to a workspace:

```bash
tessl inventory import --org your-org --workspace engteam
```

This relies on the [GitHub CLI](https://cli.github.com/) being installed and authenticated locally, and on being logged in to Tessl for the upload, so run `gh auth login` and `tessl login` before you import. For more on inventory, see [Understand your skill estate](/use/understand-your-skill-estate.md).

The scan collects every `SKILL.md` and sorts what it finds. Skills that match a published registry skill are flagged as third-party; skills unique to your repos are your first-party skills, marked publishable or untracked. It also surfaces overlap and drift between near-duplicate copies. Browse the result in the app at `Workspaces → your workspace → Inventories`. Use `--repo` to scope the scan, or `--dry-run ./inventory.json` to write it to disk without uploading.

## Read the security scores

Security scores are powered by Snyk. Each score is a severity: `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`.

Third-party skills that match a published registry skill show their score in the inventory automatically. For your first-party skills, connect the Tessl GitHub App and import them; the import security-scans each one and brings its score into the inventory. Between the two, your whole skill estate ends up scored in one place. Sort the inventory by security score to find the skills that need attention first.

## Review a single skill on demand

You do not need a full inventory to check one skill. Review any skill directly from its directory:

```bash
tessl review run security ./path-to-skill --workspace engteam
```

This is the quickest way to vet a skill before you install it, or to gate a skill in CI. The review is powered by Snyk and returns the same severities. Add `--json` for machine-readable output, or `--fail-on high` to make the command exit non-zero when a finding meets or exceeds a severity. The `--fail-on` values are lowercase: `low`, `medium`, `high`, `critical`.

## Gate risky installs with a policy

An inventory and a score tell you what is risky. An install policy stops a risky skill from being installed at all. As a security admin, this is your main lever.

Policies can be set at three levels, and the tightest one wins:

* Org level: the broadest reach and your most impactful control as a security admin. It applies to every workspace and project in the org.
* Workspace level: tightens the org policy for a single workspace.
* Project level: tightens it further for a single project.

Set policy in the app under `Settings → Policy`. Setting org-level policy is an organization admin action, so if you do not see it, ask your admin. A policy combines three kinds of rule:

* Security threshold: choose the severity at which an install is warned and the severity at which it is blocked, for example warn at `MEDIUM` and block at `HIGH`.
* Source restriction: limit the registry to your own org, or to Tessl plus your org, and choose whether installs from git sources are allowed at all. When git sources are allowed, add a git source allowlist to permit only specific hosts and orgs, for example `github.com/your-org`, so developers can still install public skills from your trusted vendors while everything else is blocked.
* Minimum release age: for git sources, require a release to be a minimum number of days old before it can be installed.

Once a policy is in place, `tessl install` evaluates every source against it:

* A source under the warn threshold installs without interruption.
* A source that hits the warn threshold prompts for confirmation. A developer can proceed, or pass `--accept-warnings` to skip the prompt in automation.
* A source that hits the block threshold cannot be installed. There is no override.

```bash
tessl install your-org/some-skill
```

When the skill's score meets the block threshold, the install is refused and the offending finding is shown. The headline uses a severity label: `Passed` for `LOW`, `Advisory` for `MEDIUM`, `Risky` for `HIGH`, and `Critical` for `CRITICAL`. A `Risky` headline below therefore means a `HIGH` score that met the block threshold:

```
Blocked by install policy (not added to tessl.json):
  ✖ Security  Risky · Do not use without reviewing
    your-org/some-skill
    W011 Third-party content exposure detected.
    View full report: https://app.tessl.io/...
```

{% hint style="info" %}
You can also set a publish policy that blocks publishing a skill whose security score is under a threshold, so risky skills never enter your registry in the first place. See [Codifying and enforcing your company's skill standards](/tutorials/codifying-and-enforcing-skill-standards.md).
{% endhint %}

## Where to go next

* [Understand your skill estate](/use/understand-your-skill-estate.md) for more on inventory.
* [Administrating organizations, workspaces, and roles](/administrators/administrating-organizations-workspaces-and-roles.md) to control who can install and publish.
* [Codifying and enforcing your company's skill standards](/tutorials/codifying-and-enforcing-skill-standards.md) to extend governance from security to quality.

---

## docs.tessl.io/use/understand-your-skill-estate.md — Inventory

# Understand your organization's context

How to connect a source-control integration so Tessl scans your repositories and shows your organization's context and findings.

Connect a source-control integration and Tessl scans your repositories, indexes the skills and configuration it finds as **context**, and surfaces **findings** you can act on. This is the primary way to see what exists across your organization.

***

Source-control integrations are managed at the organization level. Connecting one needs the integration-management permission (**manager** or **owner**). Viewing **Context** and **Findings** is open to every role. See [Roles](/administrators/roles.md) for the full breakdown.

### Connect a source-control integration

Tessl supports these source-control providers:

* **GitHub** (GitHub App)
* **GitLab** (access token)
* **Bitbucket**

**To connect:**

1. Open the Tessl web app.
2. Select your organization from the dropdown at the top of the sidebar, then go to **Settings**, then **Integrations**.
3. Under **Source control**, select **Add** next to your provider and follow the prompts to authorize Tessl.

Connecting authorizes Tessl to read from the provider. When organization-level inventories are enabled for your organization, connecting also provisions an inventory and starts a first scan of the repositories in scope. Both steps are best-effort and separate from the connection: the connection succeeds and stays connected even when provisioning does not run (organization-level inventories are not enabled) or the scan does not start or finish. So a successful connection does not guarantee a scan. When a scan does run, the connection page shows its status, and a **manager** or **owner** can retry it or set the **Scan scope** there.

### See your context and findings

Once a scan has run:

* Open **Context** in the sidebar to see the skills and configuration Tessl found across your connected repositories, including which repository each item lives in.
* Open **Findings** to see the issues Tessl surfaced, ranked by severity.
* **Home** gives you an overview across your organization.

To control which repositories Tessl scans, open the connection under **Settings**, then **Integrations**, and set the **Scan scope**. For GitHub-specific setup, including private indexing, see [Connect Tessl to GitHub](/distribute/connect-tessl-to-github.md).

---

## docs.tessl.io/use/using-the-tessl-agent.md

# Using the Tessl agent

Six things teams use the agent for, the way you'd actually ask for each one, the command it runs underneath, and what you should see back.

## 01 See what you already have

Skills are multiplying across repos, and most teams can't say how many they have or who owns them. This is free, needs no changes to your code, and is the first thing worth running.

<details>

<summary>See what skills you already have</summary>

USE WHEN You have skills spread across repos and no single view of what exists or who owns it.

**Ask your agent**

"Scan our GitHub org and build a skill inventory."

**Under the hood**

`tessl inventory import`

Scans your repos, collects `skill.md` and manifest files, and uploads a snapshot. Forked repos are skipped.

**What to expect**

A snapshot of your whole skill estate: what exists, where it lives, who last touched it, and which skills are near-duplicates of each other. Run it again any time. Each scan is diffed against the last, so you get a living view of what's new, unchanged, and removed.

Trial it on a subset first with `tessl inventory import --repo repo-a --repo repo-b`. The flag repeats as many times as you like.

It reads only `skill.md` files and manifests. No source code, no real names or email addresses (GitHub usernames only), and no repo clones: files are fetched one at a time through the API.

{% hint style="warning" %}
**Heads up:** the default scan covers your 100 most recently active repos. Large orgs can hit GitHub's limit of 5,000 API requests per hour mid-scan. Scans are diffed, so nothing is lost: wait for the reset and run it again.
{% endhint %}

</details>

***

## 02 Bring or create skills

Three starting points, depending on what you already have.

<details>

<summary>Import a skill you already have</summary>

USE WHEN Best if you already have a skill in your repo. The agent brings it in as-is.

**Ask your agent**

"Import the skill at plugins/my-plugin into Tessl."

**You provide**

The path to a skill you already have, either a `SKILL.md` file or the directory holding it.

**Under the hood**

`tessl skill import`

Wraps a standalone skill as a plugin: `SKILL.md` plus a `.tessl-plugin/plugin.json` manifest.

**What to expect**

Your skill unchanged, now with a manifest beside it, so it can be reviewed, evaluated, versioned, and published.

</details>

<details>

<summary>Create a new skill</summary>

USE WHEN Nothing to bring yet? The agent walks you through a new one from scratch.

**Ask your agent**

"Help me create a skill."

Or name it: `"run plugin-creator"`

**Under the hood**

Built-in `plugin-creator` skill

Interviews you about the skill's scope, scaffolds the plugin and skill directory, then validates the result.

**What to expect**

An interview about what the skill should cover, then a drafted `SKILL.md`. Check the `description` carefully: it's what decides whether an agent picks the skill up at the right moment.

</details>

<details>

<summary>Create context for recurring agent mistakes</summary>

USE WHEN You have PR review history, and the same corrections keep coming up in it.

**Ask your agent**

"Agents keep getting this wrong. Look at our last 2 weeks of PR reviews."

Or name it: `"run find-optimizations on the last 2 weeks"`

**You provide**

A PR number, or a time window in plain language such as "the last 2 weeks". It will not run without one.

**Under the hood**

Built-in `find-optimizations` skill

Batch-fetches feedback from change-requested PRs, then splits it across subagents so no PR body ever crowds out the context.

**What to expect**

A deduplicated, numbered list of improvements. Each one is typed (`skill`, `review`, `skill`, `rule`, `hook`, `test`, `refactor`, or `verifier`), backed by the PR numbers and specific comments that motivate it, and pointed at an exact destination rather than a vague suggestion.

It triages before it proposes. When a linter, typechecker, or schema validator could own the pattern, it names that tool instead of reaching for a verifier. Nothing gets changed: the output is the deliverable.

It reads your source control preferences from `.tessl/memory/` first, so it may run `/setup-memory` before the analysis if this is your first time. Needs real review history to work with, so run it on a repo where people leave PR comments.

</details>

***

## 03 Automate code review

Tessl Code Review reviews the exact pull request head and publishes one native GitHub review. A review can request required changes while keeping optional suggestions visible, and later rounds account for fixes and replies.

<details>

<summary>Set up Tessl Code Review</summary>

USE WHEN You want a first review before a human starts, or a repeatable review on every merge candidate.

**The supported path is the GitHub App**

The Tessl Review GitHub App is the supported way to run Tessl Code Review. It reviews pull requests on Tessl's infrastructure, with no workflow to write and no token to store. Open **Code reviews** in the Tessl web app and select **Connect GitHub**, then enable each repository you want reviewed. Read [Set up Tessl Code Review](/tutorials/setting-up-agentic-code-review.md) for install, the separate enable step, trigger policies, approval, the config file, and troubleshooting.

**If you cannot install a GitHub App**

An unsupported GitHub Action can run reviews from a workflow you own instead. The `tessl/code-review` plugin carries a setup skill that writes it for you:

```sh
tessl install tessl/code-review
```

If your `tessl.json` still declares `tessl/code-review-setup` or `tessl/code-review-lens-creator`, replace it with `tessl/code-review`. Those plugins were folded into `tessl/code-review` and are being retired; while a project declares one of the old names, `tessl agent` skips its built-in copy of the merged plugin so the same skill is not loaded twice, and the project gets only what the old plugin carried.

Ask your agent to set up code review, and it points you to **Code reviews** for your organization, where you select **Connect GitHub** to install the Tessl Review GitHub App. The agent cannot install the App for you: the install starts in the browser. It also tells you that the repository has to be enabled in Tessl afterwards, since installing the App alone does not start reviews. See [Set up Tessl Code Review](/tutorials/setting-up-agentic-code-review.md) for the whole setup.

If you cannot install a GitHub App, an unsupported GitHub Action can run Tessl Code Review from a workflow you own. Ask for the GitHub Action by name to get it. See [Running Code Review in your own CI](/tutorials/setting-up-agentic-code-review/code-review-action.md) for its input and output reference.

</details>

<details>

<summary>Choose and tune review lenses</summary>

A lens is a focused set of review instructions. The `standard` profile runs the lenses from the [`tessl/code-review`](https://tessl.io/registry/tessl/code-review) plugin by default: `review-correctness-and-data-integrity`, `review-maintainability-and-code-quality`, `review-scale-and-resilience`, and `review-security-and-privacy`. Begin without overriding the selection and evaluate the results on pull requests you understand.

Ask your agent to add repository-specific lenses only when you can name the concern and show examples of what a good review should catch:

> Add our versioned API-contract and data-handling lenses to Tessl Code Review. Keep the existing cadence and advisory mode.

Passing `lenses` replaces the profile's complete default selection, and a review supports at most eight lenses. Pin every registry reference (for example `tessl/code-review@0.2.0#review-security-and-privacy`) and keep each lens responsible for a distinct concern, so findings do not repeat each other. To fork a default lens, start from its source in [`tesslio/product-plugins`](https://github.com/tesslio/product-plugins); to write one from scratch, use the `create-code-review-lens` skill in the same [`tessl/code-review`](https://tessl.io/registry/tessl/code-review) plugin.

</details>

<details>

<summary>Move from advisory to gate mode</summary>

USE WHEN Advisory reviews have earned trust and every merge candidate can receive a review.

**Ask your agent**

"Change Tessl Code Review to gate mode and tell me which GitHub repository settings and required check I need."

**What to expect**

The workflow changes to `mode: gate`. An approved review attempts a native GitHub approval and reports a successful check. A review that requires changes attempts to request changes and reports a failed check.

The agent should also tell you to:

* allow GitHub Actions to create and approve pull requests;
* require the Action-owned check named exactly `Tessl Code Review`;
* use an automatic cadence or make requested reruns part of the merge process;
* test both an approved change and a change that should be blocked.

Do not require the caller workflow job as the review gate. Mention-driven and manually dispatched jobs are associated with the default branch, while the Action reports its own check against the reviewed pull request head.

</details>

<details>

<summary>Decide separately whether a human review is required</summary>

USE WHEN You want a repository-owned risk policy to decide which pull requests still need a human reviewer.

**Ask your agent**

"Set up a PR risk gate for this repo."

**You provide**

A choice of starter policy: `conservative-starter` or `official-review-policy-parity`. Read and edit the generated policy files before you depend on the gate.

**Under the hood**

```sh
tessl change risk init
tessl change risk --base origin/main \
  --fail-if-review-required --json
```

This combines deterministic git measurements with an advisory agent judgment, followed by a deterministic policy decision. It is separate from Tessl Code Review: one reviews the code, while the other decides whether repository policy requires a human.

**What to expect**

Starter files under `.github/pr-review-gate/`: a config, a policy, and a prompt. Two starters are available: `conservative-starter` is the default and requires human review for most changes; `official-review-policy-parity` tracks your existing branch protection more closely. Read and edit the policy before you rely on it.

In CI, `--fail-if-review-required` exits non-zero when the gate decides a human is needed.

{% hint style="warning" %}
**Heads up:** `change risk init` writes the policy files only. It does not create a workflow and does not touch branch protection. Add the check as advisory first, watch it on real PRs for a few weeks, and make it required once you trust the signal.
{% endhint %}

</details>

***

## 04 Enforce your standards

Verifiers check binary, observable facts about committed files. Reach for one when a reviewer keeps flagging the same structural pattern and no linter can own it.

<details>

<summary>Write your first verifier</summary>

USE WHEN A reviewer keeps flagging the same structural pattern and no linter can express it.

**Ask your agent**

"Create a verifier that checks every Fastify route file returns via our typed response helpers."

**You provide**

The rule you want enforced, in plain language and specific enough that someone could score a file pass or fail by reading it.

**Under the hood**

```
tessl change verify lint <file>
tessl change verify --dry-run --all --show-files
```

Validates the structure against the schema, then previews exactly which files would be judged before spending any judge calls.

**What to expect**

A verifier JSON file plus an entry in the `verify` block of `tessl.json`. Each verifier carries a `name`, an `instruction`, a `relevant_when` eligibility test, `context` a `scope` (file, paths, or diff) with its `scope_reason`, and a `checklist` of one to three binary rules.

Severity is never in the verifier file. It's repo policy, set per group in `tessl.json` as `info`, `warn`, or `error`. That way the same verifier can be advisory in one repo and blocking in another.

{% hint style="warning" %}
**Heads up:** most bad verifiers fail for one reason: a `relevant_when` that's too broad. "Backend file", "React component", and "any TypeScript file" are all too vague to judge consistently. Name the observable trait that makes a file in scope.
{% endhint %}

</details>

<details>

<summary>Run verifiers on every PR</summary>

USE WHEN Your first verifier has earned trust and you want it enforced in CI.

**Ask your agent**

"Run verifiers on every PR."

**You provide**

The verifier group already wired into `tessl.json`, plus a base ref. Nothing else.

**Under the hood**

`tessl change verify --base origin/main --git`

`--github` emits GitHub Actions annotations, so findings appear inline in the PR even when the run exits 0.

**What to expect**

Findings in the PR UI, anchored to the lines that violate the rule. Verifiers set to `error` make the check blocking; `warn` annotates without failing, unless you add `--fail-on-warn`.

Start every new verifier at `warn` while you calibrate. Promote it to `error` only after you've confirmed it avoids false positives on real PRs.

**Widen the blast radius one rung at a time**

`tessl change verify lint` → `--dry-run --all --show-files` → `--sample 5` → full run

</details>

***

## 05 Automate the chores

The recurring work that never makes it onto a sprint board: the scan someone runs by hand, the cleanup that gets deferred, the check everyone forgets.

<details>

<summary>Find chores worth automating</summary>

USE WHEN You suspect there is repeat work in this repo but have not pinned down what.

**Ask your agent**

"There's a chore I keep doing by hand."

Or name it: `"run find-automations"`

**Under the hood**

Built-in `find-automations` skill

Reads the repo and its history for work that recurs on a predictable trigger.

**What to expect**

A numbered list of opportunities. Each one carries a ticket-style title, its pattern type (`established`, `emerging`, or `one-off`), the evidence behind it, a suggested trigger and execution mode, and a description detailed enough to implement from. The numbering is the point: you can come back and say "create a ticket from item 2".

It looks for signals like the same person filing the same maintenance PR, the same reviewer leaving the same comment, repeated CI babysitting, and release or dependency chores. Strictly read-only: it won't write a file, comment on a PR, or trigger a workflow.

</details>

<details>

<summary>Turn a chore into a CI workflow</summary>

USE WHEN You have agreed on a candidate and want it running without anyone remembering to.

**Ask your agent**

"Run this recurring task automatically in CI."

Or name it: `"run workflow-automator"`

**You provide**

The task you want automated and roughly when it should run. It interviews you for the rest: what counts as a successful run, what the agent needs as input, the exact trigger, and any secrets or admin approvals required.

**Under the hood**

Built-in `workflow-automator` skill

Builds the scheduled GitHub Actions workflow and the skill it invokes.

**What to expect**

A committed workflow on a schedule you chose, plus the auth to run it. Create the key with `tessl api-key create --workspace <name>`, store it as a `TESSL_TOKEN` repository secret, and the `tesslio/setup-tessl@v2` action picks it up. Scheduled agent workflows need `ANTHROPIC_API_KEY` as a repository secret too.

The default shape is a weekly cron plus a `workflow_dispatch` trigger, so you can run it by hand while you're still building trust in it, with the results uploaded as an artifact you can read after each run.

</details>

<details>

<summary>Run a skill unattended</summary>

USE WHEN You want a skill to run without sitting through it, locally or in a Tessl cloud sandbox.

**Ask your agent**

"Run the find-automations skill on the payments repo."

**You provide**

The skill to run: a bare installed name such as `find-automations`, a registry ref `workspace/skill[@version]`, or `file:path/to/skill`. Plus an `--agent`. Pass per-run input with `--instructions "…"`, and add `--repo owner/name` when you use `--cloud`.

**Under the hood**

```
tessl launch skill <workspace/skill> \
  --agent claude-code --yolo
```

Add `--cloud --repo owner/name` to run it in the cloud instead of on your machine.

**What to expect**

The skill runs through your chosen agent with output streaming back. `--yolo` skips permission prompts, which is what makes it usable in CI. Use `--interactive` to watch it in the foreground instead, and `tessl launch list` to see recent runs.

</details>

<details>

<summary>Hooks, when the trigger is an agent event</summary>

* **Two tiers, declared in `.tessl-plugin/plugin.json`.** Use `hooks` for the portable path that works across agents, and `nativeHooks` to pass agent-specific config straight through when you need the escape hatch.
* **Five generic events.** `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `SessionStart`, and `Stop`. A `matcher` narrows a hook to specific tools; omit it to fire on all of them.
* **Anchor every path with `${TESSL_PLUGIN_DIR}`.** It's the only reference that survives a change of working directory. Bare relative paths resolve against wherever the event fired, not your plugin.

{% hint style="warning" %}
**Heads up:** hook scripts have to live under `hooks/` in the plugin to ship at all, and only the files you actually declare are made executable at install time. A `timeout` in the manifest is accepted but not currently enforced, so don't rely on it to stop a slow hook.
{% endhint %}

</details>

***

## 06 Measure your context

Context is the skills and rules your agents load. One that reads well can still fail to fire, or fire and change nothing. Reviews score the writing. Evals measure the difference it makes.

<details>

<summary>Score a skill's quality</summary>

USE WHEN You want to know how a skill reads against a rubric before anyone depends on it.

**Ask your agent**

"Review this skill."

**You provide**

The path to the skill or plugin, plus `--workspace`. Defaults to the current directory if you omit the path.

**Under the hood**

```
tessl review run ./my-skill \
  --workspace <name>
```

Runs server-side. Ctrl-C detaches from the output; the review keeps going.

**What to expect**

A score with a per-judge breakdown, so you can see which dimension pulled it down. In CI, `--threshold <percent>` exits non-zero below the bar you set; `0` never fails and skips score gating entirely.

For a security pass instead, run `tessl review run security` and gate it with `--fail-on low|medium|high|critical`.

</details>

<details>

<summary>Improve a skill automatically</summary>

USE WHEN The review found problems and you would rather the agent fixed them than do it by hand.

**Ask your agent**

"Optimize my skill."

**You provide**

The same path and workspace. It prompts before it edits unless you pass `--yes`.

**Under the hood**

`tessl review fix`

An improve-then-re-review loop. `--max-iterations` caps the passes (1 to 10) and `--threshold` stops it early once the score clears your bar.

**What to expect**

It prompts before it edits, then hands you a change summary of exactly what it improved. Pass `--yes` to skip the prompts and `--threshold` to stop once the score clears a bar.

</details>

<details>

<summary>Measure whether a skill helps</summary>

USE WHEN A skill reads well, but you have not proved it changes what an agent actually does.

**Ask your agent**

"Build an eval for this skill."

**You provide**

The plugin directory. `scenario generate` needs a source to generate from, and `scenario download` reads scenarios from `evals/`.

**Under the hood**

```
tessl scenario generate <plugin> --count 5
tessl scenario download --last
tessl eval run <path/to/plugin>
```

Keep counts low at first so runs finish while you're still watching.

**What to expect**

Each scenario runs twice, once with your skill injected and once without, so the result is a delta rather than a bare score. That's the number that tells you whether the skill earns its place. Add `--runs 3` to average out model variance.

Downloaded scenarios land as `evals/<hash>-<slug>/` with a `task.md`, a `criteria.json`, and a `scenario.json`.

{% hint style="info" %}
**Note:** `scenario download` writes to the plugin's `evals/` directory automatically when run from the plugin root or any subdirectory of it. The plugin root is the directory that contains `.tessl-plugin/plugin.json`. Evals need at least `publisher` access; `member` is enough to run a review but not an eval.
{% endhint %}

</details>

---

## docs.tessl.io/projects/overview.md

# Overview

Understand what Tessl projects are and why we need them.

A Tessl project gives Tessl a stable place to attach eval runs and other repository-connected data, so your results stay tied to your codebase over time.

### Why projects exist

Tessl needs a project so it knows where an eval belongs. That way your results aren’t just a one-off run — they stay linked to the repository, so you can find them later, compare runs, and keep improving the same codebase.

### Common workflows

#### Create a new project

Use `tessl project create` when this repository is not linked yet and you want to create a new Tessl project. The command creates the project, then records the project link in `tessl.json`, creating the file if it does not exist yet. `tessl init` sets up local agent configuration and bootstraps `tessl.json` if it does not exist, but it does not create or link a remote project on its own; run `tessl project create` or `tessl project link` for that.

#### Link to an existing project

Use `tessl project link` when the Tessl project already exists for that repository.

#### Repair a project link

Use `tessl project repair` when the project link is missing, broken, outdated, or linked to the wrong project.

### Current limitations

Projects currently have limited fallback when a directory is not a Git repository.

### See also

* [Manage projects from the CLI](/projects/manage-projects-from-the-cli.md)
* [Projects in the app](/projects/projects-in-the-app.md)

---

## docs.tessl.io/reference/mcp-gateway.md

# MCP gateway

Create a workspace MCP gateway in Tessl and connect to it from any agent with \`tessl mcp proxy\`.

A **workspace MCP gateway** lets Tessl broker connections to an external [Model Context Protocol](https://modelcontextprotocol.io) server for a workspace. You register the upstream server once in the workspace's settings, authorize it (via OAuth where required), and then any workspace member can connect to it through a single stable address: `tessl mcp proxy <workspace>/<mcp>`.

A gateway is useful when:

* You want a shared, authorized MCP server that every workspace member can use without each person re-running an OAuth flow.
* You want to keep upstream credentials (client secret, tokens) inside Tessl rather than copy them into individual agent configurations.
* You want one identifier (`<workspace>/<mcp>`) to reference the same MCP server from a coding agent, a plugin, or a CI environment.

The gateway sits between the agent's MCP client and the upstream MCP server: the agent talks to `tessl mcp proxy` over stdio, the CLI relays JSON-RPC messages to the gateway over HTTP with Tessl auth headers, and the gateway relays them on to the upstream MCP server using the credentials you stored when you registered it.

## Create a gateway in a workspace

Workspace owners and managers can register MCP servers. Members without `manage_mcp_servers` permission see the page in read-only mode.

1. Open the workspace in the Tessl web app and go to **Settings → Integrations → MCP servers**.
2. Click **Add MCP server**.
3. Fill in the form:
   * **Server name** — used as the slug in the gateway path. Use only alphanumerics, hyphens, and underscores (max 63 characters). Example: `linear`.
   * **Upstream URL** — the URL of the MCP server you are wrapping. Example: `https://mcp.example.com`.
   * **Transport** — `HTTP` or `SSE`, matching how the upstream server exposes itself.
   * **Optional OAuth overrides** — leave blank to use the upstream server's discovery defaults. Fill them in if you need to pin a specific client, scope, resource, or authorization server:
     * **Client ID** and **Client secret** — pre-registered OAuth client for the upstream server. The client secret is encrypted at rest.
     * **Scope** — space-separated OAuth scopes (for example `openid profile email`).
     * **Resource URL** — RFC 8707 resource indicator for the upstream API.
     * **Authorization server URL** — explicit authorization server, used when discovery does not point at the right one.
4. Click **Add MCP server**.

The server appears in the MCP servers list with an **Unauthorized** badge. Click **Authorize** to start the OAuth flow against the upstream provider; once the upstream returns successfully, the badge flips to **Authorized** and the server is ready to use.

If credentials change or expire upstream, the server is flagged as **Needs reauth**. Click **Re-authorize** to refresh; existing proxy sessions are unaffected until they reconnect.

## Connect to the gateway with `tessl mcp proxy`

Once a gateway is authorized, any workspace member can connect to it through the CLI:

```sh
tessl mcp proxy <workspace>/<mcp>
```

* `<workspace>` is the workspace slug (the same one used in registry URLs).
* `<mcp>` is the server name you chose when creating the gateway.

For example, with a workspace named `engteam` and an MCP server named `linear`:

```sh
tessl mcp proxy engteam/linear
```

The command runs in the foreground and speaks the MCP protocol over its own stdin/stdout. It is intended to be launched by an MCP client (your coding agent, or any other tool that supports stdio-transport MCP servers) — running it directly in a terminal is only useful for smoke-testing connectivity.

### Authentication

`tessl mcp proxy` authenticates to the gateway as the calling user:

* **Interactive use** — sign in once with `tessl login`; the proxy reuses the same credentials.
* **CI or other non-interactive contexts** — set the `TESSL_TOKEN` environment variable to a Tessl API key for the workspace. See [`tessl api-key create`](/reference/cli-commands.md#tessl-api-key-create).

### Use the proxy from a coding agent

`tessl mcp proxy` is a standard stdio MCP server, so any agent that supports stdio-transport MCP servers can launch it. Add it to your agent's MCP configuration in the same way you would any other stdio server — see [Custom agent setup](/reference/custom-agent-setup.md) for the shape your agent expects.

A typical `.mcp.json`-style entry looks like:

```json
{
  "mcpServers": {
    "engteam-linear": {
      "command": "tessl",
      "args": ["mcp", "proxy", "engteam/linear"]
    }
  }
}
```

You can include several gateways at once — give each one a distinct key so the agent can address them individually.

### Use the proxy from a plugin

Plugins can declare MCP servers in their bundled [`.mcp.json`](/reference/configuration.md#bundled-mcp-json), and a workspace gateway is just another stdio MCP server from the plugin's perspective. Add an entry that invokes `tessl mcp proxy`:

```json
{
  "mcpServers": {
    "engteam-linear": {
      "command": "tessl",
      "args": ["mcp", "proxy", "engteam/linear"]
    }
  }
}
```

When a project installs the plugin, the gateway is wired into the project's agents automatically.

## Related

* [MCP tools](/reference/mcp-tools.md) — the registry MCP server (`tessl mcp start`) versus the workspace gateway (`tessl mcp proxy`).
* [Configuration files](/reference/configuration.md) — how `.mcp.json` is shaped and discovered.
* [Custom agent setup](/reference/custom-agent-setup.md) — how individual agents read MCP server entries.

---

## docs.tessl.io/reference/custom-agent-setup.md

# Custom agent setup

For agent setup, perform the following steps:

1. Run `tessl init` from your project root first. Auto-detected agents (Cursor, Claude, Gemini, Copilot, Codex) need no further configuration. You can skip the rest of these steps and start your agent to [validate it's configured](#validating-configuration).
2. MCP configuration
3. Setup rules
4. Accept running Tessl

## Configuring your agent

### MCP setup

This will allow your agent to access context from installed plugins through the Tessl exposed tools.

Typically most agents have a settings file for MCP, often .mcp.json or support for that file. Refer to your agents documentation for the specific formats and files involved for your agent. The values are the following:\
\
**Name**: "tessl"\
\
**Command**: "tessl"

**Args**: "mcp", start"

**Type**, if asked: "stdio"

#### Examples

```json
{
  "mcpServers": {
    "tessl": {
      "command": "tessl",
      "args": [
        "mcp",
        "start"
      ]
    }
  }
}
```

```toml
[mcp_servers.tessl]
type = "stdio"
command = "tessl"
args = ["mcp", "start"]
```

### Rules setup

Rules setup will load the configuration to help your agent use the Tessl MCP effectively plus any other rules from the plugins you installed.

Determine what file you can indicate to the agent to use Tessl and provide steering rules. If there is capability to use AGENTS.md, use or create an `AGENTS.md` file with the following content:

```
# Agent Rules

@.tessl/RULES.md
```

### Enable Tessl

Most agents will prompt on startup to allow the MCP tool to be used, however some may require you to take an extra step and go into the agent's settings to enable it:

<figure><img src="https://1171143958-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXbWzspFdXV0HNujz6gJ9%2Fuploads%2Fgit-blob-2f2e1eeece163942531890b4e63298031710fac3%2Fimage%20(147).png?alt=media" alt=""><figcaption></figcaption></figure>

## Validating configuration

Review the agent mcp configuration, often "/mcp" in terminal based agents, and determine if Tessl is enabled/review tools are available.\
\
`/mcp`

<figure><img src="https://1171143958-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXbWzspFdXV0HNujz6gJ9%2Fuploads%2Fgit-blob-d5a1fd78c124f1e90cc61a0ae947426e2576e948%2Fimage%20(148).png?alt=media" alt=""><figcaption></figcaption></figure>

Prompt your agent:\
`Use tessl to search for code review skills`

You will see calls to tessl **query\_library\_docs**, and/or tessl **search** , and results if configured properly.

<figure><img src="https://1171143958-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXbWzspFdXV0HNujz6gJ9%2Fuploads%2Fgit-blob-cce9176f4b902115b042080bbb365281b03ea111%2Fimage%20(149).png?alt=media" alt=""><figcaption></figcaption></figure>

## Sample configurations for agents not auto-detected

[OpenCode](/reference/custom-agent-setup/opencode.md)

---

## docs.tessl.io/reference/cli-commands.md — complete command index (CLI v0.108.0)

The reference page is 122KB of per-flag documentation. Reproduced here is its complete heading structure: `##` are command groups, `###` are commands.

## Getting started
### tessl help command
## Authentication
### tessl login
### tessl logout
### tessl whoami
## Setup and initialization
### tessl init
### tessl project
### tessl project create
### tessl project link
### tessl project repair
### tessl project list
## Project dependencies
### tessl install
### tessl search
### tessl uninstall
### tessl list
### tessl outdated
### tessl update
## Skill management
### tessl skill new
### tessl skill import
### tessl skill lint
### tessl skill publish
### tessl skill unpublish
## Tessl Review
### tessl review run
### tessl review run security
### tessl review view
### tessl review list
### tessl review retry
### tessl review fix
## Plugin management
### tessl plugin new
### tessl plugin lint
### tessl plugin migrate
### tessl plugin pack
### tessl plugin info
### tessl plugin publish
### tessl plugin unpublish
### tessl plugin archive
## Organization management
### tessl org list
### tessl org usage
## Workspace management
### tessl workspace create
### tessl workspace list
### tessl workspace delete
### tessl workspace add-member
### tessl workspace remove-member
### tessl workspace list-members
### tessl workspace archive
### tessl workspace unarchive
## Configuration management
### tessl config get
### tessl config set
### tessl config list
### tessl config add
### tessl config remove
## Diagnostics and utilities
### tessl doctor
### tessl feedback
## CLI self-management
### tessl cli update
## API key management
### tessl api-key create
### tessl api-key list
### tessl api-key delete
## Environment management
### tessl environment create
### tessl environment list
### tessl environment view
### tessl environment update
### tessl environment delete
## Model Context Protocol (MCP)
### tessl mcp start
### tessl mcp proxy
## Repository
### tessl repo select-commits
## GitHub integration
### tessl github token
### tessl github setup-auth
## Inventory
### tessl inventory import
## Scenario management
### tessl scenario generate
### tessl scenario list
### tessl scenario view
### tessl scenario download
## Evaluations
### tessl eval run
### tessl eval list
### tessl eval view
### tessl eval retry
### tessl eval lint
## Agent
### tessl agent
### tessl agent mcp add
### tessl agent mcp get
### tessl agent mcp list
### tessl agent mcp remove
## Change
### tessl change risk
### tessl change risk init
### tessl change verify
### tessl change verify suggest-scopes
### tessl change verify lint
## Code review
### tessl code review
## Launch
### tessl launch \<agent>
### tessl launch skill
### tessl launch list
### tessl launch view
### tessl launch logs
## Schedules
### tessl schedule create
### tessl schedule list
### tessl schedule view
### tessl schedule runs
### tessl schedule pause
### tessl schedule resume
### tessl schedule update
### tessl schedule trigger
### tessl schedule delete
## Querying This Documentation
