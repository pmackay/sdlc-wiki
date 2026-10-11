---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-validate]]"
delegates_to: ["[[pstack-swarm]]"]
produces: ["[[artifact-pull-request]]", "[[artifact-skill-doc]]"]
applies: ["[[pattern-wave-parallelism]]", "[[pattern-evidence-before-claims]]", "[[pattern-living-specification]]"]
equivalent_to: ["[[ce-compound-refresh]]", "[[openspec-sync]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /maintain-verification-skill

The upkeep loop for what [[pstack-create-verification-skill]] generates. Its premise is that **a feature map rots the moment the app changes**, so the harness needs a scheduled pass of its own. The unit of rigor is the feature, not every sentence: cover every feature file from source and exercise every feature live, *without terminalising every bullet*.

A run declares one of three **outcomes** up front and says which: **clean** (every feature got source and live coverage, nothing worth shipping, no branch and no PR), **changed** (one PR ships proven doc, harness, or map corrections), or **blocked** (coverage could not finish or a proven fix could not ship safely, with exactly what blocked it named).

The pass is a wave then a live session. **Index hygiene** fixes missing, extra, duplicate, or dead feature-map entries. The **source wave** launches one read-only subagent per feature file concurrently, each explaining how that user-facing feature works from source, flagging likely doc drift with citations, and returning one concise live-verification recipe; children never drive the app and never edit files. **Reconcile** merges overlapping recipes into as few app states as practical, spot-checks cited drift without re-proving clean claims, and sweeps recent churn for user-facing surfaces missing from the map — requiring **a concrete source path before calling one missing**. One live pass then drives every feature, and at most one PR of proven corrections ships.

Its **edit scope** is the sharpest rule and the reason it earns a separate page from its generator. Only the verification skill's own directory may be edited, and **never product code during a run**. When the map describes a behavior the app no longer does, that is either doc drift (fix the map) or a **product regression (report it, do not paper over it in docs)**. Forcing that fork prevents the failure mode where documentation quietly relaxes to match a bug.

Structurally this is [[pattern-living-specification]] applied to a *verification* artifact rather than a requirements one — the same drift-reconciliation job [[openspec-sync]] does for specs and [[ce-compound-refresh]] does for a learnings corpus, which is why those are its counterparts despite sitting in different stages.

## See Also
- [[pstack-create-verification-skill]] — generates the skill this maintains.
- [[pstack-swarm]] — the fan-out shape the source wave uses.
- [[ce-compound-refresh]] · [[openspec-sync]] — the corpus-drift counterparts.
- [[stage-validate]] — the canonical stage this implements.
