---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-idempotent-operations]]"]
equivalent_to: []
docs_url: "https://www.aihero.dev/skills-wizard"
sources: "Matt Pocock — Skills for Real Engineers v1.3.1 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md"]
updated: 2026-10-11
---

# wizard

`wizard` — a **model-invoked** engineering skill that "generate[s] an interactive bash wizard that walks a human through steps only they can perform". The four trigger branches are provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, and a one-off migration or cutover. It has an explicit non-trigger: "Don't invoke this for steps the agent can perform itself."

Model invocation is the point. The agent can reach for it "the moment it hits a step only a human can perform, instead of dumping numbered instructions into the chat and hoping you follow them." Progress is counted in stages, with no time estimate.

## How it works

The UX is "already solved" by a bundled `template.sh`. It provides stage-by-stage progress, confirmation gates, cross-platform URL opening (including WSL), hidden secret entry, **idempotent `.env` upserts** ([[pattern-idempotent-operations]]), `gh secret` / `gh variable` writes that degrade gracefully, and a closing skip summary. Everything above the `STAGES` marker is a fixed library that is never hand-edited. "Your job is only to scope the procedure and author its stages."

1. **Scope.** Read the repo before asking anything: `.env*`, `README`, `docker-compose*`, framework config, and every `secrets.*` / `vars.*` reference in `.github/workflows/`. For each captured value, know where the human gets it, where it is written, and whether it is secret. Confirm the stage list with the user.
2. **Map each stage's journey.** Write the exact click-path ("Dashboard → Developers → API keys → Reveal test key → copy"). Where the current UI is unknown, say so and check: "never invent steps that may not exist."
3. **Author.** One `stage` per step, in dependency order. Open the URL before asking for its value, use `ask_secret` for secrets, and `confirm` before anything irreversible.
4. **Verify statically.** Run `bash -n` and `shellcheck`. Trace that every value lands where step 1 said, and that every `set_secret` name matches a CI reference. Don't run it end-to-end, since it blocks on human input.

A wizard is **ephemeral by default**. It is committed and linked from the README only when it is a repeatable setup path, "so the next person runs the script instead of asking an AI".

## Why off-stage

It advances no lifecycle step itself. It is the **human-in-the-loop escape hatch** any stage can hit: configuring a service mid-[[stage-implement]], wiring secrets before [[stage-release]], running a cutover. Its nearest relatives are the wiki's human-gating work, e.g. [[builder-factory-human-digest]] (a queue of decisions only a human can make), but no other framework hands the human an **executable procedure** rather than a message.

## See Also
- [[mp-ask-matt]] — routes it under Standalone, "for the steps only a human can take".
- [[pattern-idempotent-operations]] — the re-runnable `.env` upsert discipline the template builds in.
- [[topic-harness-engineering]] — a wizard is a human-facing guide that the agent generates.

## Version history
- **v1.2.3 (2026-08-06):** removed the time estimate. The template dropped `TOTAL_MINUTES` and the time-remaining display; `stage` takes a name only.
- **v1.2.0 (2026-08-05):** graduated from `in-progress/` into `engineering/` and made model-invoked; routed by [[mp-ask-matt]] under Standalone.
