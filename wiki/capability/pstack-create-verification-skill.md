---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: ["[[artifact-skill-doc]]"]
applies: ["[[pattern-tooling-leverage]]", "[[pattern-evidence-before-claims]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: ["[[gstack-skillify]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /create-verification-skill

Generates a **project-local** verification skill at `.cursor/skills/verify-<app>/` that drives the real app the way a user does, for any language, framework, or platform. The premise: *every serious project needs a scripted way to launch the app, exercise a feature the way a user would, and capture evidence* — and most repos have none.

This is [[pattern-tooling-leverage]] pointed at the hardest thing for an agent to fake. [[gstack]] solves the same problem with shipped infrastructure (a persistent browser daemon behind [[gstack-browse]]); pstack instead **generates a bespoke harness per repository**, which is why it works for a CLI, a TUI, a desktop app, an API, a mobile app, or a library rather than only for the browser.

It **interviews the repo, not the user**, answering five questions from the codebase and asking only what cannot be observed: the **surface** a user actually touches, how the app **runs** locally (preferring the repo's own documented dev command), how an agent can **drive** it programmatically (existing Playwright or Cypress specs, expect scripts, PTY helpers, curl-able endpoints, a debug port — only then a generic recipe), what **evidence** can be captured, and whether two instances can be **isolated** side by side. If the checkout does not build or start, that is fixed or reported precisely first, because *a skill written against a broken base teaches wrong steps*.

The generated skill has a fixed shape, and its author is told who reads it: *you write the generator's output for the next agent, not for a human — it will be read cold, mid-task, by an agent that has never seen the app.* Sections are **Launch** (with a readiness signal and teardown), **Doctor** (one read-only "is this instance worth driving?" check), **Drive** (real selectors and commands from this repo, preferring stable handles like ARIA labels, data attributes, prompt strings, and route paths over coordinates and tab order), **Evidence**, **Cleanup**, and **Helpers**.

The **proof standards** written into the Evidence section are the framework's operational definition of verification: exercise the real user path, not internal setters or test-only endpoints; capture the action *and* the resulting state, not just the final screen; verify side effects (files written, rows inserted, messages sent) alongside what is visible; and mock only where a production boundary already isolates the external system. A pointed one closes it — when the safe path is a dry-run or test mode, **verify what it actually skips by observing files, network, and git refs rather than trusting its name**, because some dry-runs still touch the network or open a browser.

Cleanup never kills by process name, only what the run started, and **proof artifacts survive the teardown** in a location the skill names.

## See Also
- [[pstack-maintain-verification-skill]] — the upkeep loop for what this generates.
- [[pstack-tdd]] — the cheap-local-test path; this is the answer when there is none.
- [[gstack-browse]] — the shipped-infrastructure alternative to a generated harness.
- [[stage-validate]] — the canonical stage this implements.
