---
type: artifact
sources: "bmad-code-org/BMAD-METHOD — create-story / create-epics-and-stories (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# Artifact: story

BMAD's **signature artifact** — a context-rich `story-[slug].md` that is the atomic unit of
implementation. Unlike a tracker ticket, "Stories in BMad aren't isolated tickets. Each story
file embeds architectural decisions, dependency context, and project conventions directly into
the implementation artifact." A story carries:

- **Status** (`backlog → ready-for-dev → in-progress → review → done`) and an As-a/I-want/so-that statement.
- **Acceptance Criteria** and **Tasks/Subtasks** (checkboxes mapped to ACs).
- **Dev Notes** — architecture constraints, source-tree touch-points, testing standards, with `[Source: docs/<file>#Section]` citations.
- **Dev Agent Record** — Agent Model Used, Debug Log, Completion Notes, File List, Change Log (filled during implementation).

The story file is the concrete mechanism of BMAD's [[pattern-context-engineering|context
engineering]]: because it embeds everything the implementer needs, [[bmad-dev-story]] can run in
a [[pattern-fresh-context-subagents|fresh context]]. Each story is an independently shippable
[[pattern-vertical-slice|vertical slice]], and a new one is created only after the previous is
`done`, so learnings propagate.

## Produced by (backlinks)
- [[bmad-create-story]] — expands one backlog item into a full context-filled story file.
- [[bmad-create-epics-and-stories]] — produces the epics + stories breakdown the stories come from.

## See Also
- [[artifact-issue]] — the plainer tracker-issue counterpart (MP / SpecKit); a BMAD story is an issue with all its implementation context inlined.
- [[artifact-plan-md]] — a flat task list, versus the story's self-contained context bundle.
- [[pattern-context-engineering]] — the technique this artifact realizes.
- [[stage-plan]], [[stage-implement]] — authored in plan, consumed in implement.
