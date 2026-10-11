---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: ["[[pstack-unslop]]"]
produces: ["[[artifact-decision-log]]"]
applies: ["[[pattern-evidence-before-claims]]", "[[pattern-tooling-leverage]]", "[[pattern-session-handoff]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /show-me-your-work

Keeps a reviewable decision trail for long-running or unattended work. One canonical **TSV file, one row per decision**, cells single-line, evidence a pointer rather than prose. [[pstack-poteto-mode]] fires it for any task the user steps away from to review later — *"going to bed"*, *"trust it when i'm back"*, *"/loop until X"*.

Six columns: `ts` (ISO8601), `phase`, `decision` (what was chosen, one line), `why` (the reason in plain words — *if a principle drove it, say it plainly, not as a jargon tag*), `evidence` (a commit SHA, PR number, `file:line`, or an artifact, trace, or screenshot path — **never a paragraph**), and `result` (the outcome or predicate state: `tests green`, `reverted`, `pixel-diff 0`, `INCONCLUSIVE`, `open`).

The rules are short and mostly about trust. **Append-only**: a wrong call gets a new row that supersedes it, and history is never edited or deleted. Log decision points and checkpoints — a fork chosen, a unit completed with its verification result, a pivot or revert with its trigger, a blocker surfaced, a gate fixed — not every action. Prefer evidence produced by **committed scripts** over hand-made one-offs, per [[pstack-principle-encode-lessons-in-structure]]. And the log text is prose like any other, so [[pstack-unslop]] applies to it: write each row the way you would tell a teammate what you did.

It ships a `log.sh` helper that stamps the timestamp, writes the header on first use, strips stray tabs and newlines, and **prefixes any cell starting with `=`, `+`, `-`, or `@` with a single quote** — a spreadsheet-formula-injection guard on an agent's own audit log, which is a nice illustration of [[pstack-principle-boundary-discipline]] applied to the framework's own output.

**Where it lives is a deliberate default.** The log is a working artifact at `decisions.tsv` (or `.audit/<task-slug>.tsv` when several efforts run at once) and is **left out of git**, committed only when the work is ambitious enough that a reviewer needs the trail to trust the result. That is the framework's answer to the audit-trail tension: the trail is always kept, but it becomes a repository artifact only when it has a reader.

This is the wiki's first capability whose entire product is a **decision trail as a review affordance** rather than as memory. [[artifact-handoff-doc]] and [[pattern-session-handoff]] exist so the *next agent* can continue; this exists so a *human who stepped away* can audit what happened and decide whether to trust it.

## See Also
- [[pstack-figure-it-out]] — its main consumer; Phase D weaves a row in as each step lands.
- [[pstack-recall]] — the complement, reconstructing state rather than recording it.
- [[artifact-decision-log]] — the artifact this produces.
- [[pattern-tooling-leverage]] — the committed-script preference.
