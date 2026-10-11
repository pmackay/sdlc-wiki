---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: ["[[artifact-skill-doc]]"]
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-cross-model-review]]", "[[pattern-wave-parallelism]]", "[[pattern-deterministic-gates]]"]
equivalent_to: ["[[ce-compound]]", "[[gstack-skillify]]", "[[sp-writing-skills]]", "[[gstack-learn]]", "[[mp-retro]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-10-11
---

# /reflect

Mines the current conversation for durable learnings and routes each to a concrete edit on an **existing** skill. pstack's member of the [[pattern-knowledge-compounding]] cluster, and the framework's loop-closing step.

Three reviewers run in parallel over the active transcript, each on a different lens and an explicitly chosen model: **Judgment**, **Tooling**, and **Divergent**. A fourth call synthesizes their findings into a structured **Accepted / Rejected / Backlog** list. All four run in agent mode rather than readonly, and the skill says why: *readonly strips MCPs*, and both the reviewers (looking up tickets, chat threads, observability traces referenced in the transcript) and the synthesizer (spot-verifying citations) need them.

Two guards are unusual enough to be the reason this page exists.

**The structural-enforcement check.** Before anything is applied, the synthesizer's Accepted list is re-read and *any item that would be enforced more reliably by a lint rule, script, metadata flag, or runtime check is moved from Accepted to Backlog.* [[pstack-principle-encode-lessons-in-structure]] is thereby wired in as a gate on the framework's own growth, not just advice to the agent. This is the sharpest answer in the wiki to the accretion failure mode that skill libraries drift into, where every lesson becomes another paragraph of prose nobody reads.

**Approval is mandatory and scoped.** The full Accepted/Rejected/Backlog output is presented and the user picks which subset to apply, with the stated reason that *skill changes affect every future agent in the org*. Backlog items file to the team's tracker automatically; only the Accepted list waits. That is a deliberate exception to [[pstack-principle-never-block-on-the-human]] — editing the shared skill corpus is treated as irreversible in the way a deploy is.

The skill also gates its own invocation: skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. **One-offs are not learnings.** And it scopes transcript discovery tightly, forbidding a glob across `~/.cursor/projects/*/` because that crosses workspace boundaries and reads private chats from unrelated projects.

## See Also
- [[pstack-automate-me]] — the sibling compounding skill, aimed at a whole personal mode skill rather than a targeted edit.
- [[pstack-principle-encode-lessons-in-structure]] — the principle this enforces as a gate.
- [[ce-compound]] · [[gstack-skillify]] · [[gstack-learn]] · [[sp-writing-skills]] — the knowledge-compounding cluster.
- [[stage-learn]] — the canonical stage this implements.
- [[mp-retro]] — Matt Pocock: a session retrospective routed into environment changes; mechanical findings become deterministic checks.
