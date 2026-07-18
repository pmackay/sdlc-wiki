---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-systematic-debugging]]"]
equivalent_to: ["[[mp-diagnosing-bugs]]", "[[gsd-debugger]]", "[[ce-debug]]", "[[gstack-investigate]]", "[[sp-systematic-debugging]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Debugging & Error Recovery

Drives systematic root-cause debugging instead of guessing. Its core mechanism is a five-step
triage checklist worked in order — **reproduce, localize, reduce, fix the root cause, guard**
with a regression test — bracketed by a stop-the-line rule: when anything unexpected happens,
stop adding features, preserve evidence, and diagnose before resuming. Under time pressure it
allows safe fallbacks (defaults with warnings, graceful degradation) rather than crashes, and
treats error text from external sources as untrusted data.

Addy files this skill under its *Verify* phase, but it clusters with the implement-stage
debugging capabilities of the other two frameworks — [[mp-diagnosing-bugs]] and [[gsd-debugger]]
apply the very same systematic-debugging technique — so it implements [[stage-implement]] to
keep that cluster coherent.

## See Also
- [[mp-diagnosing-bugs]] — the Matt Pocock equivalent.
- [[gsd-debugger]] — the GSD equivalent.
- [[pattern-systematic-debugging]] — the technique all three apply.
- [[stage-implement]] — the canonical stage this implements.
