---
type: framework
source_url: "https://github.com/tao-hpu/nano-spec"
docs_url: "https://generativeai.pub/nano-spec-the-sweet-spot-between-chaos-and-over-engineering-in-ai-assisted-development-0d0ccec202c0"
sources: "Tao An — nano-spec, tao-hpu/nano-spec (MIT, 46★); intro article in Generative AI / Medium (2025-12-01)"
raw: ["../../raw/nano-spec/2025-12-01-nano-spec.md"]
updated: 2026-07-13
---

# nano-spec

**nano-spec** (Tao An, `tao-hpu/nano-spec`, MIT) is a deliberately **minimal, tool-agnostic
task-specification methodology** for AI-assisted development. Its tagline — *"Spec-driven
thinking, nano-sized docs"* — is the whole idea: capture just enough written structure to think
clearly before coding, and no more. Like [[bm-skills]], it is **not a full-SDLC framework**; it
owns exactly one slice of the lifecycle (authoring a lightweight spec) and leaves the rest to the
coding agent.

Its thesis is a **ceremony spectrum**. AI makes it trivial to skip specs (fast but chaotic —
scope creep, misaligned code, painful handoffs) *or* to over-invest in enterprise-grade
PRD + design + tech-spec stacks (complete but slower than the build). nano-spec claims the
middle — the ~80% of tasks "too complex for *just do it*, too simple for enterprise-grade
specs" — with **four tiny markdown files per task**. It is explicitly *"inspired by
[Kiro's Spec-Driven Development](https://kiro.dev/docs/specs/), but minimal and practical"*:

| Approach | Docs | Overhead | Best for |
|:---|:---:|:---:|:---|
| No spec | 0 | none | trivial tasks |
| **nano-spec** | 4 | low | most tasks |
| Kiro SPEC | 3+ | high | complex features |

## The 4-document pack

Every task gets a folder `tasks/{task-name}/` holding the [[artifact-nano-spec-pack|4-document pack]]:

- **README.md** — *Context: what & why.* Background, goals, explicit in/out **scope**, dependencies.
- **todo.md** — *Plan.* Research / implementation / verification checklists + Must-Have / Nice-to-Have / Out-of-Scope **acceptance criteria** ([[artifact-plan-md]]).
- **doc.md** — *Output.* Key **decisions** (options considered · chosen · rationale), schemas/architecture, open questions ([[artifact-adr]]).
- **log.md** — *Journey.* Dated Done / In-Progress / Blocked / Notes entries; the handoff and retrospective trail.

*"The documents aren't the point. Clarity is."* — the pack is external memory, a thinking
framework that happens to produce files.

## Capabilities

nano-spec ships **one Claude Code skill** (`SKILL.md`) exposing a single `/nano-spec` command
with three actions. The same instructions are re-published verbatim as system-prompt configs for
nine other tools (Codex, Gemini, OpenCode, Antigravity, Cline, Cursor, Windsurf, Trae, GitHub
Copilot) — the capability is identical; only the invocation differs (native slash-command vs.
natural-language prompt). Documented here as one page per action for full coverage:

- [[nano-spec-create]] — **the focus**: generate the 4-document pack from a one-line task description. Implements [[stage-specify]]; the 8th member of the cross-framework specify cluster.
- [[nano-spec-status]] — read `todo.md` + `log.md` and report progress (done vs. total, blockers, last-log date). A lightweight status read; no canonical stage.
- [[nano-spec-update]] — apply a requested change to the pack and append a dated `log.md` entry. Living-doc maintenance across the build; no canonical stage.

## Distinctive contribution

nano-spec is the specify cluster's **minimalist, tool-neutral** entry. Where the other spec
authors run facilitated interviews ([[bm-prd-creator]], [[bmad-prd]]), enforce quality gates
([[speckit-checklist]], [[gstack-codex]]), or maintain a permanent delta-tracked spec
([[openspec]]), nano-spec's entire value proposition is *subtraction*: a fixed set of four
short files, ~10-minute setup, no bespoke tooling, portable across ten agents. It is the wiki's
clearest embodiment of [[pattern-scale-adaptive-planning]] applied at the **methodology** level —
not a dial inside one framework (as in [[bmad]]/[[gstack]]) but a deliberate, fixed *point* on
the ceremony spectrum, chosen because most work lives there. Its second distinctive move is
treating the spec as a **living pack maintained through the build** (`update` + daily `log.md`),
which doubles as the [[pattern-session-handoff|handoff]] artifact.

## Patterns applied
- [[pattern-spec-driven-development]] — write a spec and drive the agent from it; the core practice ([[nano-spec-create]]).
- [[pattern-scale-adaptive-planning]] — size the doc weight to the task; nano-spec is the deliberate middle tier of the no-spec → nano → full-spec spectrum (whole framework).
- [[pattern-session-handoff]] — the 4-file pack (esp. `log.md`) is shared for instant context to a teammate or fresh agent ([[nano-spec-status]], [[nano-spec-update]]).

## See Also
- [[bm-skills]] — the other deliberately-minimal, non-full-SDLC entry; both touch only [[stage-specify]] substantively.
- [[openspec]] — the opposite pole of spec durability: a permanent, delta-maintained spec vs. nano-spec's per-task throwaway pack.
- [[speckit]] — the maximalist reference implementation of spec-driven development; nano-spec is the minimalist counterpoint.
- [[bmad]] · [[gstack]] — where scale-adaptive ceremony is a *dynamic dial*; nano-spec fixes a single point on that same spectrum.
- [[stage-specify]] — the one canonical stage nano-spec substantively implements.
</content>
