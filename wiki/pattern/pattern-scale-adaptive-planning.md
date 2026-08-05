---
type: pattern
sources: "bmad-code-org/BMAD-METHOD (2026); tao-hpu/nano-spec (2025); Agent OS — Builder Methods (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md", "../../raw/gstack/2026-07-05-gstack-framework.md", "../../raw/nano-spec/2025-12-01-nano-spec.md", "../../raw/agent-os/2026-08-05-agent-os.md"]
updated: 2026-08-05
---

# Pattern: Scale-adaptive planning

Size the *ceremony* to the *work*: a one-line fix skips straight to code, an enterprise system runs the full spec → architecture → epics → stories pipeline, and everything in between takes a proportionate middle path. Planning depth is a **dial, not a fixed gate** — "Choose your track based on planning needs, not story math." This is [[bmad]]'s answer to the tension every spec-driven framework faces: rigour that helps big projects becomes dead weight on small ones.

BMAD expresses it two ways across its v6 line:

- **Numeric Levels 0–4** (classic v6) — Single Atomic Change → Small Feature → Medium Project → Complex System → Enterprise Scale, each prescribing which artifacts exist (tech-spec only → PRD → PRD + architecture + just-in-time tech specs).
- **Stakes-calibrated tracks** (current v6) — **Quick Flow** (skip planning) / **BMad Method** (PRD + architecture + UX) / **Enterprise** (adds Security + DevOps). Solutioning is skipped, optional, or required per track.

A close relative is **just-in-time design**: the architecture [[artifact-architecture|spine]] fixes only invariants and defers concrete structure to the code, so detail is produced only when needed.

## Applied by (backlinks)

BMAD:

- [[bmad-quick-dev]] — collapses the whole pipeline to a few turns for small, well-understood work.
- [[bmad-spec]] — the lightweight SPEC kernel used instead of a full PRD on the light track.
- [[bmad-architecture]] — the invariants-only spine (just-in-time design).

gstack:

- [[gstack-autoplan]] — smart review routing sizes the review ceremony to the change (CEO skips infra, design skips backend).

nano-spec:

- [[nano-spec-create]] — applies the pattern at the *methodology* level: rather than a dial inside one framework, nano-spec is a deliberate **fixed middle tier** on the no-spec → nano → full-spec (Kiro) ceremony spectrum, chosen because most work lives there. The dial is exercised by *choosing nano-spec* over the neighbours, not within it.

Agent OS:

- [[agent-os-plan-product]] · [[agent-os-shape-spec]] — lightweight-by-default docs, sized to the project; v3's whole design is *subtraction* — it deleted its own scaffolding and delegates the heavy lifting to the harness's Plan Mode (another methodology-level point on the ceremony spectrum, like nano-spec).

## See Also
- [[pattern-spec-driven-development]] — the method whose ceremony this pattern modulates.
- [[pattern-vertical-slice]] — the unit of work the light tracks ship directly.
- [[bmad]] — the framework built on this pattern.
