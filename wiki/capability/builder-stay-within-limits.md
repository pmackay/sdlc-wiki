---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: ["[[artifact-handoff-doc]]"]
applies: ["[[pattern-autonomous-loop]]", "[[pattern-session-handoff]]", "[[pattern-wave-parallelism]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /stay-within-limits

Keep long-running agent work inside the current **5-hour and weekly usage windows**. The loop: run a bounded wave (by default at most 3 parallel subagents), wait for it to finish (*"do not interrupt in-flight subagents just to save budget; that usually loses work"*), check usage with the host's tool (in Claude Code, `npx -y ccusage@latest blocks --active --json`), and if either window is at or above **95%**, stop launching work and schedule a self-contained resume.

On resume it rechecks the actual window instead of trusting elapsed time. *"A new timestamp is stronger evidence than 'enough time passed.'"* Wakeups are clamped to `min(3600, secondsUntilWindowClears)` and chained for longer waits. The wake prompt carries the remaining plan, the check-then-reschedule rule, the threshold, the usage command, the previous block ID, and the next wave's handoff packets. It is a [[pattern-session-handoff]] written to a future turn of the same agent.

It also gives a rule for choosing a wait mechanism: use a wake tool when instructions need to travel with the resume, a background watcher for things a process can observe directly, and cron only for recurring fresh-session work. Avoid short-interval polling for things the host will announce. Off-stage: it handles the **budget** concern from the factory glossary for a single interactive agent.

## See Also
- [[builder-efficient-frontier]] — the delegation habit whose waves this throttles.
- [[pattern-autonomous-loop]] — long unattended runs; budget is one of the things that ends them.
- [[topic-software-factory]] — *budget* in the glossary.
