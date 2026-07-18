---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-edit-guardrails]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /careful

`/careful` — **safety guardrails**. Warns before **destructive commands** — `rm -rf`, `DROP TABLE`, force-push, `git reset --hard` — using inline advisory prose; the user can override any warning. Say "be careful" to activate.

One of gstack's four safety power-tools implementing [[pattern-edit-guardrails]] — the confirm- before-you-destroy half (the scope-lock half is [[gstack-freeze]]; [[gstack-guard]] combines both). This enacts the *User Sovereignty* ethos: the agent surfaces the risk and lets the human decide. No cross-framework counterpart — explicit, toggleable safety guardrails are a gstack signature.

## See Also
- [[gstack-freeze]] — the directory-scope-lock guardrail.
- [[gstack-guard]] — careful + freeze together.
- [[pattern-edit-guardrails]] — the technique.
- [[stage-implement]] — the stage these guardrails protect.
