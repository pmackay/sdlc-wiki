---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd rules

`bd rules audit|compact` — *"audit and compact Claude rules"*: scan `.claude/rules/` for **contradictions and merge opportunities** (Jaccard similarity, default threshold 0.6) and merge related rules into composites (`--auto` applies the audit's suggestions, `--dry-run` previews, `--group` names them explicitly).

This is the odd one out on the page — a tracker with a command that operates on **the harness's guide layer**, not on work at all — and it is the most interesting boundary crossing beads makes.

The problem it targets is real and well documented in [[topic-harness-engineering]]: a project's rule set grows by accretion as agents and humans add instructions, and after a few months it contains rules that overlap, rules that contradict, and rules that are dead. Nobody rereads it, so it silently degrades, and it degrades the model's behaviour with it. [[ce-compound-refresh]] is the only comparable capability in the wiki — keeping a corpus healthy over time (Keep / Update / Consolidate / Replace / Delete) — and it is a *framework* skill, an LLM asked to curate. Beads' version is **mechanical**: a similarity metric, a threshold, a merge.

Why it lands in a store is not obvious and is probably not principled — it is a tool built by people who felt the pain in their own repo. But there is a defensible reading: rules are durable project state that outlives every session, which is this layer's whole subject, and `.claude/rules/` is exactly the kind of file [[beads-remember]] argues should not be maintained by hand.

Maps to **no canonical SDLC stage**.

## See Also
- [[topic-harness-engineering]] — the guide layer this maintains, and why it decays.
- [[ce-compound-refresh]] — the LLM-driven counterpart for a solutions corpus.
- [[beads-setup]] — the command that *writes* into the same guide layer.
- [[beads-remember]] — the store-native alternative to hand-maintained instruction files.
