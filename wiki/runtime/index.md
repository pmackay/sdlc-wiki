---
type: index
updated: 2026-07-26
---

# Runtime — the execution layer

The `framework` / `capability` / `sdlc-stage` triad models the **process layer** — *what* an agent does across the lifecycle. This namespace models a second, orthogonal **execution layer** — *where and how* the agent runs. A **runtime** is the harness-agnostic substrate that provides sandbox isolation, parallelism, branch→PR flow, AFK autonomy, steering, and persistence. It runs Claude Code, Codex, pi, … interchangeably, and could host any process framework's skills — so it performs no SDLC stage and carries no `belongs_to` / `implements` / `equivalent_to` edge. It connects to the rest of the wiki at exactly one seam: the `pattern` namespace, via `enables:`. See [CONVENTIONS §The execution layer](../CONVENTIONS.md#the-execution-layer-runtimes).

## Members

| Runtime | Subtype | One-liner |
|---------|---------|-----------|
| [sandcastle](sandcastle.md) | library | TypeScript SDK — `sandcastle.run()` sandboxes an agent with a branch strategy and merges commits back; built for parallelizing AFK agents and review pipelines. The **embeddable pole**. |
| [warren](warren.md) | platform | *"Coolify for coding agents"* — a self-hostable control plane: dispatch ephemeral agents at your repos, watch/steer live, get a PR back. The **service pole**. |

## Orchestration profile (the synthesis axis)

The runtime layer's analogue of the SDLC-stage synthesis: the dimensions runtimes are compared on are **orchestration concerns**, not lifecycle stages. Held as this matrix (not their own node namespace) until the layer grows enough to warrant graduating them — see [CONVENTIONS](../CONVENTIONS.md#the-execution-layer-runtimes).

| Concern | [[sandcastle]] (library) | [[warren]] (platform) |
|---|---|---|
| Isolation | container bind-mount / microVM / worktree / none | OS-level `bwrap` workspace or k8s pod per run |
| Parallelism | you script it — parallel `run()`s, session fork | many concurrent runs; plan-run is serial |
| Autonomy / AFK | `maxIterations` + `completionSignal` + timeouts | ephemeral dispatch→validate→push→spin-down; cron; seeds self-claim |
| Steering (HITL) | `interactive()` before handoff; no mid-run steer | **real-time mid-run `steer` + `cancel`** |
| Persistence / memory | session capture/resume/fork; no memory store | **`.mulch/` cross-run memory**; canopy prompts; run/cost history |
| Provider-agnostic | Claude Code · Codex · pi · Cursor · OpenCode · Copilot | claude-code · sapling · pi (+ canopy custom) |
| Branch → PR | branch strategies; PR is your script's job | **built-in templated auto-PR** |
| Topology | a library embedded in your process (local / Vercel) | one container (home server) or Kubernetes |
| Distribution | **library / SDK** | **platform** (UI + API + CLI + SDK) |

The two occupy opposite poles: Sandcastle hands you primitives to compose in TypeScript; Warren is a deployed service that owns the loop end-to-end (and even absorbs a `learn`-stage concern into the runtime via `.mulch/`).

## Patterns this layer supplies

The execution layer touches the wiki only through the patterns it `enables:` — each has a **process-side** roster (capabilities that `apply` it) and now an **infra-side** roster (runtimes that `enable` it):

- [[pattern-worktree-isolation]] — sandcastle (git worktree/branch), warren (`bwrap`/pod)
- [[pattern-autonomous-loop]] — sandcastle (AFK `run()`), warren (ephemeral dispatch + plan-run)
- [[pattern-wave-parallelism]] — sandcastle (parallel `run()`s / fork)
- [[pattern-session-handoff]] — sandcastle (session resume/fork), warren (`.mulch/` prime + steer + event log)
- [[pattern-knowledge-compounding]] — warren (`.mulch/` machine-consumable memory across runs)

## The broader category

Two documented instances are the start, not the extent. The same layer includes **Conductor** (already referenced by [[gstack-context-restore]] as a workspace host), Dagger's **Container-use**, Imbue's **Sculptor**, **Vibe-Kanban**, and the coding harnesses' own worktree/sandbox modes — plus Warren's own [os-eco](https://github.com/jayminwest/os-eco) siblings (burrow, canopy, mulch, seeds, plot, sapling). Ingest more as they warrant pages; graduate the matrix above into derived nodes if it stops scaling.
