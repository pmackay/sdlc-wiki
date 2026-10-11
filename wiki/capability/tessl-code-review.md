---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-adversarial-review]]", "[[pattern-parallel-persona-review]]", "[[pattern-deterministic-gates]]"]
equivalent_to: ["[[gstack-review]]", "[[addy-code-review]]", "[[mp-code-review]]", "[[ce-code-review]]", "[[pstack-interrogate]]", "[[sp-requesting-code-review]]"]
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl code review

Agentic pull-request review, shipped both as the **Tessl Review GitHub App** and as `tessl code review` in CI. It reviews the current PR, a named PR, or an explicit git range, and can publish its verdict back to the pull request or approve on behalf of a bot login.

**This is a registry capability that genuinely performs an SDLC stage**, and it is the clearest instance of the sideways growth the [supply layer](../registry/index.md) page warns about: a company that sells capability distribution also sells the review those capabilities are meant to improve.

Its distinctive mechanism is **lenses** — named, versioned review perspectives that replace the default set, configurable per repository through a `.tessl-code-review.yml` profile and pinnable by version. That is the persona-panel idea ([[pattern-parallel-persona-review]]) rebuilt as **installable, versioned units** rather than as prompts baked into a framework's skill. [[gstack]] and [[ce-code-review]] hard-code their reviewer roster; [[pstack-interrogate]] deliberately replaces personas with model diversity; Tessl makes the roster a dependency you install and pin. Same pattern, distributed through the layer it belongs to.

The premise is stated as a scaling problem rather than a quality one: *"Code review doesn't scale to agent-authored PRs."* That is the honest framing for why a supply-layer product ends up here — the volume of agent-written code is what creates the market for both halves.

## See Also
- [[tessl-change-risk]] · [[tessl-change-verify]] — the two other lifecycle capabilities, aimed at a diff rather than a PR.
- [[gstack-review]] · [[addy-code-review]] · [[mp-code-review]] · [[ce-code-review]] · [[pstack-interrogate]] · [[sp-requesting-code-review]] — the framework-side review cluster.
- [[stage-review]] — the canonical stage this implements.
