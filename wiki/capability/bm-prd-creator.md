---
type: capability
subtype: skill
belongs_to: "[[bm-skills]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-prd]]", "[[artifact-plan-md]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-grilling]]", "[[pattern-scale-adaptive-planning]]"]
equivalent_to: ["[[bmad-prd]]", "[[mp-to-spec]]", "[[addy-spec-driven-development]]", "[[openspec-propose]]", "[[speckit-specify]]", "[[gstack-spec]]", "[[nano-spec-create]]"]
sources: "Brian Casel (Builder Methods) — BM Skills (2026)"
raw: ["../../raw/bm-skills/2026-07-09-bm-skills.md"]
updated: 2026-07-09
---

# PRD Creator (bm-prd-creator)

`bm-prd-creator` — a user-invocable skill that guides a **non-technical business builder** through turning a raw idea into a structured **Product Requirements Document** ([[artifact-prd]]) plus a sequence of **milestone prompt files** ([[artifact-plan-md]]) ready to hand to a coding agent. The reason [[bm-skills]] was ingested.

It runs a **structured, multi-phase interview** ([[pattern-grilling]]) — each phase in its own `steps/` file, executed in order, each locked before the next: brain-dump intake → format choice → core purpose → top-level features (in/out of scope) → tech stack → integrations & credentials → data model → per-feature scoping → milestone breakout → write files. Interaction principles: **propose a default with reasoning, then confirm** (never open-ended "what do you want?"), use `AskUserQuestion` for discrete choices (mobile-friendly tappable options), **one decision at a time**, and **adapt depth to the idea** (~10–15 decisions default; compress simple, expand complex → [[pattern-scale-adaptive-planning]]).

**Distinctive in the specify cluster:**
- **Non-technical audience** — every technical concept (background job, API token, data model) is explained in plain language before a decision is asked. The other frameworks' spec authors assume a developer.
- **Strict what-not-how boundary** — the PRD names the stack (e.g. Rails, React) and integration providers (e.g. OpenAI, Resend) and stops there; no code, libraries, method names, or implementation patterns (those belong to the agent in plan mode per milestone).
- **Visual HTML by default** — output format is HTML (recommended) / Markdown / Both; the format changes presentation only, not the locked scope.
- **Milestone prompts** — the build is decomposed into `milestones/N-{slug}/prompt.md` files, a specify→plan bridge that drives implementation.

It is [[bm-skills]]'s member of the cross-framework **specify** cluster ([[pattern-spec-driven-development]]) — author the durable spec before code — alongside [[bmad-prd]] (its closest match, also a facilitated PRD), [[mp-to-spec]], [[addy-spec-driven-development]], [[openspec-propose]], [[speckit-specify]], and [[gstack-spec]].

## See Also
- [[bmad-prd]] — the closest counterpart: a facilitated create/update/validate PRD → [[artifact-prd]].
- [[mp-to-spec]] · [[speckit-specify]] · [[gstack-spec]] — other specify-cluster members.
- [[artifact-prd]] — the primary output; [[artifact-plan-md]] — the milestone prompt files.
- [[stage-specify]] — the canonical stage this implements.
