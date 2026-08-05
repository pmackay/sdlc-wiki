---
type: capability
subtype: command
belongs_to: "[[agent-os]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-spec-md]]", "[[artifact-standards]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-grilling]]", "[[pattern-scale-adaptive-planning]]"]
equivalent_to: ["[[mp-to-spec]]", "[[addy-spec-driven-development]]", "[[openspec-propose]]", "[[speckit-specify]]", "[[bmad-prd]]", "[[gstack-spec]]", "[[bm-prd-creator]]", "[[nano-spec-create]]"]
sources: "Agent OS v3.0.0 — shape-spec (2026)"
raw: ["../../raw/agent-os/2026-08-05-agent-os.md"]
updated: 2026-08-05
---

# Agent OS: shape-spec

`/shape-spec` — **shape a spec in Plan Mode** into a persistent, timestamped pack. It hard-stops unless the agent is in plan mode (*"Shape-spec must be run in plan mode. Please enter plan mode first."*) — a deliberate handoff to the harness's own planning primitive. Nine steps: clarify scope → gather visuals → identify code references → read `agent-os/product/` (the [[agent-os-plan-product|product docs]]) → **surface relevant standards** from `index.yml` → generate a `YYYY-MM-DD-HHMM-{slug}/` folder → structure the plan (**Task 1 is always "Save spec documentation"**) → remaining tasks → confirm before execution. The pack persists beyond the conversation as `plan.md`, `shape.md`, `standards.md` (a snapshot of the relevant [[artifact-standards|standards]]), `references.md`, and `visuals/`.

This is Agent OS's member of the cross-framework **specify** cluster ([[pattern-spec-driven-development]]) — *author the durable spec before code* — the **ninth**, alongside [[mp-to-spec]], [[addy-spec-driven-development]], [[openspec-propose]], [[speckit-specify]], [[bmad-prd]], [[gstack-spec]], [[bm-prd-creator]], and [[nano-spec-create]].

**Distinctive in the specify cluster:**
- **It shapes, it does not generate.** v3 deliberately hands spec *authoring* to the harness's Plan Mode + extended thinking, and confines itself to *structuring* the questions and *persisting* the result. Where [[gstack-spec]] adds a cross-model quality gate and [[speckit-checklist]] a checklist gate, shape-spec adds *durability + standards-binding* and little ceremony ([[pattern-scale-adaptive-planning]]).
- **Standards-bound by construction.** Step 5 pulls the matching standards into the spec (`standards.md`), so the spec ships with the conventions it must honor — the guide layer welded onto the spec. No other specify-cluster member embeds project standards into the spec artifact.
- **Timestamped, persistent pack** — like [[nano-spec-create]]'s 4-file pack and unlike a single `SPEC.md`, the output is a dated folder that doubles as a durable record of *what was built and why*.

## See Also
- [[nano-spec-create]] — the closest kin: a minimal, persistent multi-file spec pack (but generated in one shot, not shaped in Plan Mode).
- [[gstack-spec]] · [[speckit-specify]] · [[openspec-propose]] · [[mp-to-spec]] — other specify-cluster members.
- [[agent-os-plan-product]] · [[agent-os-inject-standards]] — the product docs and standards shape-spec reads in.
- [[artifact-spec-md]] — the spec this produces (as a persistent pack); [[artifact-standards]] — snapshotted into it.
- [[stage-specify]] — the canonical stage this implements.
