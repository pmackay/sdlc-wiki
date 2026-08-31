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

## Orchestration profile (the synthesis axis)

The runtime layer's analogue of the SDLC-stage synthesis: the dimensions runtimes are compared on are **orchestration concerns**, not lifecycle stages. Held as this matrix (not their own node namespace) until the layer grows enough to warrant graduating them — see [CONVENTIONS](../CONVENTIONS.md#the-execution-layer-runtimes).

| Concern | [[sandcastle]] (library) | [[warren]] (platform) | [[bernstein]] (platform) |
|---|---|---|---|
| Isolation | container bind-mount / microVM / worktree / none | OS-level `bwrap` workspace or k8s pod per run | worktree by default + 7 pluggable backends (docker · e2b · modal · daytona · blaxel · runloop · vercel) |
| Parallelism | you script it — parallel `run()`s, session fork | many concurrent runs; plan-run is serial | **declarative task DAG** — `[P]` markers + dependency arrows, topological batching, adaptive `max_agents` |
| Coordination logic | your TypeScript | the control plane, one run at a time | **deterministic Python — zero LLM tokens on scheduling** |
| Autonomy / AFK | `maxIterations` + `completionSignal` + timeouts | ephemeral dispatch→validate→push→spin-down; cron; seeds self-claim | tick loop to quiescence; adaptive timeouts; retry-with-model-escalation; circuit breaker; cost kill-switch |
| Verification | `exec()`-gated — your script decides | validates before push | **janitor (completion signals + gate pipeline) then a fresh-session, different-model review gate** |
| Steering (HITL) | `interactive()` before handoff; no mid-run steer | **real-time mid-run `steer` + `cancel`** | gate-shaped — permission modes, approval cards, plan-comment approval, hold leases; no mid-run steer |
| Persistence / memory | session capture/resume/fork; no memory store | **`.mulch/` cross-run memory**; canopy prompts; run/cost history | confidence-decayed **lessons**, per-task diaries + HITL-gated synthesis, CrossTaskKB, tiered compaction |
| Provider-agnostic | Claude Code · Codex · pi · Cursor · OpenCode · Copilot | claude-code · sapling · pi (+ canopy custom) | **40+ adapters** — claude · codex · gemini · qwen · ollama · aider · cursor · opencode · pi · droid · copilot · … |
| Branch → PR | branch strategies; PR is your script's job | **built-in templated auto-PR** | merge queue + PR creation; opt-in issue→plan→draft-PR→revise pipeline; never auto-merges |
| Governance / audit | — | run history, cost analytics, documented security posture | **HMAC-chained audit log, signed lineage, offline-recomputable taint verdicts, credential scoping, air-gap profile** |
| Topology | a library embedded in your process (local / Vercel) | one container (home server) or Kubernetes | local-first single process; optional coordinator+workers cluster mode; Helm chart |
| Distribution | **library / SDK** | **platform** (UI + API + CLI + SDK) | **platform** (task server + REST/OpenAPI + dashboard + TUI + CLI + MCP server) |

Two axes fall out of the matrix, and they are not the same axis. The first is **distribution**: Sandcastle hands you primitives to compose in TypeScript, while Warren and Bernstein are deployed services that own the loop end-to-end. The second, visible only once there are three instances, is **what the runtime takes responsibility for**. Warren owns *dispatch and steering* — one agent at a time, watched live and redirectable mid-run. Bernstein owns *coordination and verification* — many agents at once, scheduled by code rather than by a model, with the quality gate pulled down into the substrate. Both absorb a process-layer concern into the runtime (Warren a `learn`-stage one via `.mulch/`, Bernstein a [validate](../sdlc-stage/stage-validate.md)-stage one via the janitor and review gate), which is the recurring finding of this layer.

A third axis worth naming is **weight**. Sandcastle is a three-line API; Bernstein is 349 documentation pages with a compliance surface, a lineage graph, and a cluster mode. They are not competing at the same scale, and "which runtime" is partly a question of how much infrastructure the work justifies.

## Patterns this layer supplies

The execution layer touches the wiki only through the patterns it `enables:` — each has a **process-side** roster (capabilities that `apply` it) and now an **infra-side** roster (runtimes that `enable` it):

- [[pattern-worktree-isolation]] — sandcastle (git worktree/branch), warren (`bwrap`/pod), bernstein (worktree + 7 pluggable backends)
- [[pattern-autonomous-loop]] — sandcastle (AFK `run()`), warren (ephemeral dispatch + plan-run), bernstein (tick loop to quiescence)
- [[pattern-wave-parallelism]] — sandcastle (parallel `run()`s / fork), bernstein (declarative task DAG, topological batching)
- [[pattern-session-handoff]] — sandcastle (session resume/fork), warren (`.mulch/` prime + steer + event log), bernstein (`handoff emit`/`claim` across surfaces)
- [[pattern-knowledge-compounding]] — warren (`.mulch/` machine-consumable memory across runs), bernstein (confidence-decayed lessons + HITL-gated diary synthesis)
- [[pattern-evidence-before-claims]] — bernstein (janitor completion signals + gate pipeline; the agent's own report is not an input)
- [[pattern-cross-model-review]] — bernstein (review gate `DifferentModelRequired`; cross-provider verifier)
- [[pattern-fresh-context-subagents]] — bernstein (review gate raises `FreshContextViolation` on a threaded implementer transcript)

The last three arrived with Bernstein and are the layer's newest move: patterns that were **process-layer instruction everywhere else in the wiki** — verify before claiming, review with a different model, review in clean context — become *enforced properties of the substrate*, failing loudly rather than degrading quietly when violated.

## The broader category

Three documented instances are the start, not the extent. The same layer includes **Conductor** (already referenced by [[gstack-context-restore]] as a workspace host), Dagger's **Container-use**, Imbue's **Sculptor**, **Vibe-Kanban**, and the coding harnesses' own worktree/sandbox modes — plus Warren's own [os-eco](https://github.com/jayminwest/os-eco) siblings (burrow, canopy, mulch, seeds, plot, sapling). Ingest more as they warrant pages; graduate the matrix above into derived nodes if it stops scaling.
