---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-learn]]"
delegates_to: ["[[mp-writing-for-agents]]"]
produces: ["[[artifact-standards]]"]
applies: ["[[pattern-knowledge-compounding]]", "[[pattern-deterministic-gates]]", "[[pattern-context-engineering]]"]
equivalent_to: ["[[pstack-reflect]]", "[[ce-compound]]", "[[gstack-retro]]"]
docs_url: "https://www.aihero.dev/skills-retro"
sources: "Matt Pocock — Skills for Real Engineers v1.3.1 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md"]
updated: 2026-10-11
---

# retro

`/retro` — a user-invoked engineering skill: "Conduct a retrospective on a coding session." It suggests improvements to the coding agent's **environment**, not the code, so that future runs go better.

[[mp-ask-matt]] routes it as **step 4, the last step of the main flow**, after [[mp-code-review]]: "`/retro` closes the loop." It is also the follow-up to [[mp-diagnosing-bugs]]: once a fix is in, run `/retro` in the same session to ask what would have prevented the bug. It is the toolkit's only [[stage-learn]] capability.

## Steps

1. Load [[mp-writing-for-agents]] (via the Skill tool) for the writing style.
2. Read the session's **primary sources**: the current session by default, or a named one found in the session logs on this machine.
3. Look for candidates in seven categories:
   - **Navigation**: was finding the right file slow? Would a **navigation pointer** help?
   - **Automated checks**: could a lint/type/test/filesystem check have caught the agent's mistake? Read the repo's own check command and CI first, so an existing-but-unwired check is the finding, not a reinvention. A repo with **no guardrail at all** (no pre-commit hook and no CI running lint/typecheck/test) is itself a finding.
   - **Coding standards**: should the reviewer get a new rule? Classify the violation first. A **mechanical** violation gets a deterministic check ("full stop": a custom linter rule, a pre-commit hook, or a CI job). `CODING_STANDARDS.md` is kept for genuine **judgement calls** ([[pattern-deterministic-gates]] over prose rules).
   - **Global AGENTS.md**: steering that should move to standards or checks instead.
   - **Tool economy**: expensive or token-inefficient tool calls (CLIs, MCPs).
   - **No-ops**: steering instructions that don't change the agent's behaviour.
   - **Information access**: teeing dev-server logs, read-only access to third-party services.
4. Present the candidates **in order of severity**.

## The reasoning it rests on

- **Implementation vs review.** The implementation agent carries the most **context pressure** (exploration, code, debugging); the review agent gets a diff and carries the least. So "the review agent should be responsible for imposing coding standards, not the implementation agent". That is why standards go in `CODING_STANDARDS.md` (read at review, → [[artifact-standards]]) and not in always-loaded `CLAUDE.md`/`AGENTS.md`, which should hold little beyond navigation pointers.
- **Mechanical → deterministic.** A rule a program can check should be a program. This matches [[pstack-reflect]] demoting any learning "a lint rule would enforce better".

## Where it sits in the cluster

Of the [[stage-learn]] flavors, `retro` is **environment compounding**. It is not a solutions corpus ([[ce-compound]] → [[artifact-solution-doc]]), not a team-process retrospective ([[gstack-retro]], [[bmad-retrospective]]), and not a skill edit ([[pstack-reflect]], [[sp-writing-skills]]). It produces edits to the agent's harness: checks, standards, pointers, tooling. That puts it close to the *guides + sensors* framing in [[topic-harness-engineering]], and it is the MP entry in [[topic-compounding-loop]].

## See Also
- [[mp-code-review]] — the step it follows; the standards it tunes are the ones code-review enforces.
- [[mp-writing-for-agents]] — the style guide it loads before writing any steering change.
- [[mp-diagnosing-bugs]] — routes a post-fix `/retro` from it.
- [[pstack-reflect]] · [[ce-compound]] · [[gstack-retro]] — stage-learn counterparts.
- [[stage-learn]] — the canonical stage this implements.

## Version history
- **v1.3.1 (2026-10-04):** [[mp-ask-matt]] routes [[mp-diagnosing-bugs]] to `/retro` once a fix is in, replacing the stale post-mortem hand-off to [[mp-improve-codebase-architecture]].
- **v1.3.0 (2026-10-04):** graduated from `in-progress/` into `engineering/`, routed as the last step of the main flow. The toolkit's first [[stage-learn]] capability, closing a gap the wiki had listed since the initial ingest.
