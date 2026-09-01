---
type: index
updated: 2026-08-31
---

# Runtime

*The execution layer — the harness-agnostic substrate deciding where and how agents run.*

The `framework` / `capability` / `sdlc-stage` triad models the **process layer** — *what* an agent does across the lifecycle. This namespace models a second, orthogonal **execution layer** — *where and how* the agent runs. A **runtime** is the harness-agnostic substrate that provides sandbox isolation, parallelism, branch→PR flow, AFK autonomy, steering, and persistence — an *agent* execution substrate, not a language, container, or model runtime. It runs Claude Code, Codex, pi, … interchangeably, and could host any process framework's skills — so it performs no SDLC stage and carries no `belongs_to` / `implements` / `equivalent_to` edge. It connects to the rest of the wiki at exactly one seam: the `pattern` namespace, via `enables:`. See [CONVENTIONS §The execution layer](../CONVENTIONS.md#the-execution-layer-runtimes).

## Members

| Runtime | Subtype | One-liner |
|---------|---------|-----------|
| [sandcastle](sandcastle.md) | library | TypeScript SDK — `sandcastle.run()` sandboxes an agent with a branch strategy and merges commits back; built for parallelizing AFK agents and review pipelines. The **embeddable pole**. |
| [warren](warren.md) | platform | *"Coolify for coding agents"* — a self-hostable control plane: dispatch ephemeral agents at your repos, watch/steer live, get a PR back. The **service pole**. |
| [bernstein](bernstein.md) | platform | *"Kubernetes for AI coding agents"* — a goal becomes a task DAG, scheduled by **pure Python with no model in the loop**, run in parallel worktrees, verified before merge. The **coordination pole**. |
| [sssf](sssf.md) | library | *"Agent proposes, code disposes"* — a stamped Python control plane where agents are bounded **phases**, typed JSON envelopes cross every seam, gates verify the claims, and every event streams into SQLite live. No sandbox, no parallelism, by admission. The **minimal pole**. |

One caveat on membership, recorded rather than smoothed over: the layer definition calls a runtime *harness-agnostic*, and [[sssf]] runs [[pi]] **only** in v1 (`coding_agent: claude_code` is schema-valid and raises). It is still filed here because agnosticism is a property of the *interface* — one `agent_*.py` module per harness behind one call site, with the second specced and stubbed — and because the agnosticism that matters most to it is at the *model* layer, where it is total: any `provider/model-id` in pi's catalog, chosen per phase, in one run.

## Orchestration profile (the synthesis axis)

The runtime layer's analogue of the SDLC-stage synthesis: the dimensions runtimes are compared on are **orchestration concerns**, not lifecycle stages. Held as this matrix (not their own node namespace) until the layer grows enough to warrant graduating them — see [CONVENTIONS](../CONVENTIONS.md#the-execution-layer-runtimes).

| Concern | [[sandcastle]] (library) | [[warren]] (platform) | [[bernstein]] (platform) | [[sssf]] (library) |
|---|---|---|---|---|
| Isolation | container bind-mount / microVM / worktree / none | OS-level `bwrap` workspace or k8s pod per run | worktree by default + 7 pluggable backends (docker · e2b · modal · daytona · blaxel · runloop · vercel) | **none** — current branch, current tree; substituted by a post-hoc rollback of unauthorized writes |
| Parallelism | you script it — parallel `run()`s, session fork | many concurrent runs; plan-run is serial | **declarative task DAG** — `[P]` markers + dependency arrows, topological batching, adaptive `max_agents` | none — one process, one sequence of phases |
| Coordination logic | your TypeScript | the control plane, one run at a time | **deterministic Python — zero LLM tokens on scheduling** | **your Python** — a 40–180-line ADW script of `run.phase()` blocks |
| Autonomy / AFK | `maxIterations` + `completionSignal` + timeouts | ephemeral dispatch→validate→push→spin-down; cron; seeds self-claim | tick loop to quiescence; adaptive timeouts; retry-with-model-escalation; circuit breaker; cost kill-switch | a chain runs unattended to a two-part gate (all phases green **and** `accepted=`), bounded fix/revise loops |
| Verification | `exec()`-gated — your script decides | validates before push | **janitor (completion signals + gate pipeline) then a fresh-session, different-model review gate** | **gates over the envelope's claims** + `kind="code"` quality blocks; violations return as corrections to the live session |
| Steering (HITL) | `interactive()` before handoff; no mid-run steer | **real-time mid-run `steer` + `cancel`** | gate-shaped — permission modes, approval cards, plan-comment approval, hold leases; no mid-run steer | none mid-run — the human is the first phase and the exit code |
| Persistence / memory | session capture/resume/fork; no memory store | **`.mulch/` cross-run memory**; canopy prompts; run/cost history | confidence-decayed **lessons**, per-task diaries + HITL-gated synthesis, CrossTaskKB, tiered compaction | per-session only — `agent_map.json` resumes each agent's context window across ADWs; nothing compounds |
| Provider-agnostic | Claude Code · Codex · pi · Cursor · OpenCode · Copilot | claude-code · sapling · pi (+ canopy custom) | **40+ adapters** — claude · codex · gemini · qwen · ollama · aider · cursor · opencode · pi · droid · copilot · … | **pi only** (claude_code stubbed) — but fully model-agnostic *per phase*, a different `provider/model-id` per agent in one run |
| Branch → PR | branch strategies; PR is your script's job | **built-in templated auto-PR** | merge queue + PR creation; opt-in issue→plan→draft-PR→revise pipeline; never auto-merges | — |
| Governance / audit | — | run history, cost analytics, documented security posture | **HMAC-chained audit log, signed lineage, offline-recomputable taint verdicts, credential scoping, air-gap profile** | the trace **is** the audit — 7 tables, 10 event types, itemised per-phase spend, gate evidence, pid table; plus `writes`/`protected_files` rollback |
| Topology | a library embedded in your process (local / Vercel) | one container (home server) or Kubernetes | local-first single process; optional coordinator+workers cluster mode; Helm chart | a stamped `adws/` directory; `uv run` per workflow; optional Bun visualizer over the SQLite file |
| Distribution | **library / SDK** | **platform** (UI + API + CLI + SDK) | **platform** (task server + REST/OpenAPI + dashboard + TUI + CLI + MCP server) | **library**, stamped from a Claude Code **skill** rather than imported — the code lands in your repo to be edited |

Two axes fall out of the matrix, and they are not the same axis. The first is **distribution**: Sandcastle and sssf hand you primitives to compose yourself, while Warren and Bernstein are deployed services that own the loop end-to-end. The second, visible only once there are several instances, is **what the runtime takes responsibility for**. Warren owns *dispatch and steering* — one agent at a time, watched live and redirectable mid-run. Bernstein owns *coordination and verification* — many agents at once, scheduled by code rather than by a model, with the quality gate pulled down into the substrate. sssf owns *the seams* — the phase boundary, the typed envelope crossing it, the gate that closes it, and the trace that records all three — and owns nothing else, deliberately. Each absorbs a process-layer concern into the runtime (Warren a `learn`-stage one via `.mulch/`, Bernstein and sssf a [validate](../sdlc-stage/stage-validate.md)-stage one via gates), which is the recurring finding of this layer.

The **library pole now has two occupants, and they divide cleanly**: Sandcastle's primitives are about the *sandbox* (`run()`, branch strategies, `exec()` gating, session fork) and leave the workflow to you; sssf's primitives are about the *workflow* (phases, envelopes, gates, corrections) and leave the sandbox out entirely. Neither ships the other's half, which makes them closer to complementary than competing — and makes "library vs platform" a weaker distinction than the subtype implies.

A third axis worth naming is **weight**, and with four instances it spans two orders of magnitude. sssf is a few hundred lines of Python you are told to edit; Sandcastle is a three-line API; Bernstein is 349 documentation pages with a compliance surface, a lineage graph, and a cluster mode. They are not competing at the same scale, and "which runtime" is partly a question of how much infrastructure the work justifies. sssf makes that explicit from the light end — *"Is this overkill for a one-off feature? Yes. Prompt an agent and move on. This earns its keep when the same workflow runs a hundred times."*

The light end also demonstrates that the concerns in this matrix are **separable rather than a package**. sssf ships *no* isolation at all — current branch, current tree — and says so in its own README, listing a branch per run, a sandbox, and a merge step as *"the obvious next things to build"*; Sandcastle ships no memory; Warren no real parallelism. Only one row is filled by all four members, and it is **verification**: every runtime here decided that something between the agent's report and the merge had to be checked by code. That is the layer's most-agreed claim.

## Patterns this layer supplies

The execution layer touches the wiki only through the patterns it `enables:` — each has a **process-side** roster (capabilities that `apply` it) and now an **infra-side** roster (runtimes that `enable` it):

- [[pattern-worktree-isolation]] — sandcastle (git worktree/branch), warren (`bwrap`/pod), bernstein (worktree + 7 pluggable backends)
- [[pattern-autonomous-loop]] — sandcastle (AFK `run()`), warren (ephemeral dispatch + plan-run), bernstein (tick loop to quiescence), sssf (a bounded chain to a two-part acceptance gate)
- [[pattern-wave-parallelism]] — sandcastle (parallel `run()`s / fork), bernstein (declarative task DAG, topological batching)
- [[pattern-session-handoff]] — sandcastle (session resume/fork), warren (`.mulch/` prime + steer + event log), bernstein (`handoff emit`/`claim` across surfaces), sssf (`agent_map.json` rejoins each agent's own context window across ADWs)
- [[pattern-knowledge-compounding]] — warren (`.mulch/` machine-consumable memory across runs), bernstein (confidence-decayed lessons + HITL-gated diary synthesis)
- [[pattern-deterministic-gates]] — bernstein (named gate pipeline, `required` gates hard-block merge), sandcastle (`exec()`-gated pipeline steps), sssf (per-call gate callables + `kind="code"` phases; *"a known command is code, not an agent"*)
- [[pattern-evidence-before-claims]] — bernstein (janitor completion signals + gate pipeline; the agent's own report is not an input), sssf (gates run *after* the agent, against the envelope's own declarations)
- [[pattern-cross-model-review]] — bernstein (review gate `DifferentModelRequired`; cross-provider verifier)
- [[pattern-fresh-context-subagents]] — bernstein (review gate raises `FreshContextViolation` on a threaded implementer transcript)
- [[pattern-contract-first]] — sssf (a typed Pydantic envelope is the interface at every seam, re-prompted until it validates) — the layer's first supply of this pattern
- [[pattern-context-engineering]] — sssf (two output channels only; the previous envelope injected by code, not carried in conversation; bounded output tails)
- [[pattern-edit-guardrails]] — sssf (`writes:` + `protected_files:` enforced by diffing the repo around every call and rolling back what the agent introduced) — the layer's first supply of this pattern too

[[pattern-evidence-before-claims]], [[pattern-cross-model-review]] and [[pattern-fresh-context-subagents]] arrived with Bernstein and named the layer's characteristic move: patterns that were **process-layer instruction everywhere else in the wiki** — verify before claiming, review with a different model, review in clean context — become *enforced properties of the substrate*, failing loudly rather than degrading quietly when violated. The last three bullets are sssf continuing it from the light end, and they are the two layers meeting at a smaller seam than usual: a typed envelope instead of a conversation ([[pattern-contract-first]] supplied as infrastructure for the first time), and a write boundary enforced by reverting the write rather than by asking a human first ([[pattern-edit-guardrails]], likewise).

## The broader category

Four documented instances are the start, not the extent. The same layer includes **Conductor** (already referenced by [[gstack-context-restore]] as a workspace host), Dagger's **Container-use**, Imbue's **Sculptor**, **Vibe-Kanban**, and the coding harnesses' own worktree/sandbox modes — plus Warren's own [os-eco](https://github.com/jayminwest/os-eco) siblings (burrow, canopy, mulch, plot, sapling). Two of those siblings belong to a **different** layer: [[seeds]] and [[beads]] are [stores](../store/index.md), not runtimes — they spawn no agent and decide nothing about where one runs; Warren consumes `.seeds/`, not the reverse. The test is *a runtime spawns loops; a store is read by them*, and beads' charter states it from the other side, naming *"schedulers, swarms, release coordinators"* as the layer above it and declining to encode them. **mulch** and **canopy** are `memory`-subtype store candidates on the same test, not runtimes. Ingest more as they warrant pages; graduate the matrix above into derived nodes if it stops scaling.
