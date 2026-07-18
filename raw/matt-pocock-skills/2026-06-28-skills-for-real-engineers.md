---
source_urls:
  - https://github.com/mattpocock/skills
  - https://raw.githubusercontent.com/mattpocock/skills/main/README.md
collected: 2026-06-28
published: Unknown
author: Matt Pocock
---

# Skills for Real Engineers (mattpocock/skills)

## What it is
A curated set of agent skills "designed for real engineering work — not 'vibe coding'",
by **Matt Pocock**, sourced from his personal `.claude` directory. Small, adaptable,
composable skills that work with any model, based on decades of engineering experience.
Philosophy: "Hack around with them. Make them your own." Maintains developer control and
debuggability.

Install: `npx skills@latest add mattpocock/skills`. After selecting skills, run
`/setup-matt-pocock-skills` to configure issue tracker (GitHub, Linear, or local files),
triage label preferences, and documentation save location.

## Four failure modes addressed
1. **The agent didn't do what I want** — communication gap; fix with a *grilling session*
   (agent asks detailed questions before proceeding). Skills: `/grill-me`, `/grill-with-docs`.
2. **The agent is way too verbose** — projects lack shared domain language; fix by
   establishing a shared-language document so agents decode project jargon (built into
   `/grill-with-docs`).
3. **The code doesn't work** — no feedback loops on real execution; fix with static types,
   browser access, automated tests, red-green-refactor. Skills: `/tdd`, `/diagnosing-bugs`.
4. **We built a ball of mud** — complex codebases deteriorate fast under AI-accelerated
   coding; fix via daily design investment. Skills: `/to-prd`,
   `/improve-codebase-architecture`, domain modeling.

## Skills

### Engineering — user-invoked
- **ask-matt** — router for selecting the appropriate skill for a situation.
- **grill-with-docs** — grilling session building a domain model and updating CONTEXT.md / ADRs.
- **triage** — move issues through a triage state machine.
- **improve-codebase-architecture** — scan codebase for architectural improvements; presents HTML visual reports.
- **setup-matt-pocock-skills** — configure repo (issue tracker, labels, documentation paths).
- **to-issues** — break plans/specs/PRDs into independently-grabbable vertical-slice issues.
- **to-prd** — synthesize the current conversation into a PRD and publish to the issue tracker.
- **prototype** — build throwaway prototypes (terminal apps or toggleable UI variations) for design validation.

### Engineering — model-invoked
- **diagnosing-bugs** — structured debugging loop: reproduce → minimize → hypothesize → instrument → fix.
- **tdd** — red-green-refactor loop for features/bugs.
- **domain-modeling** — build and sharpen the project domain model; stress-test terminology.
- **codebase-design** — design deep modules with small interfaces at clean seams.

### Productivity — user-invoked
- **grill-me** — comprehensive interview on plans/designs until all decision branches resolve.
- **handoff** — compact a conversation into a handoff document for agent transitions.
- **teach** — teach concepts over multiple sessions using the directory as workspace.
- **writing-great-skills** — reference guide for writing/editing skills effectively.

### Productivity — model-invoked
- **grilling** — reusable interview loop underlying grill-me and grill-with-docs.

### Miscellaneous
- **git-guardrails-claude-code** — block dangerous git commands via pre-execution hooks.
- **migrate-to-shoehorn** — migrate test files from `as` assertions to @total-typescript/shoehorn.
- **scaffold-exercises** — create exercise directories (sections, problems, solutions, explainers).
- **setup-pre-commit** — configure Husky hooks with lint-staged, Prettier, type checking, tests.

## Key concepts
- **CONTEXT.md** — project domain glossary / shared-language document that reduces verbosity
  and improves agent understanding through shared terminology.
  (NOTE: GSD also uses a `CONTEXT.md`, but for *locked phase decisions* — different artifact,
  same filename.)
- **ADRs** — Architecture Decision Records, updated inline during grilling sessions.
- **Vertical slices** — independent, independently-grabbable work units.
- **Deep modules** — John Ousterhout's principle: "a lot of functionality accessed through a
  simple interface."
- **Red-green-refactor** — the TDD loop.
- **Grilling** — interview/elicitation loop to close the user↔agent communication gap.

## Repository structure
```
skills/
├── skills/{engineering,productivity,misc}/   # one folder per skill
├── scripts/  docs/  .changeset/  .claude-plugin/  .github/workflows/  .out-of-scope/
├── CONTEXT.md   CLAUDE.md   README.md   package.json   LICENSE (MIT)
```

## Intended use
Integrate with Claude Code and other coding agents. Skills are user-invoked (slash command)
or model-invoked (auto-loaded by the agent when relevant).
