---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-contract-first]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /make-bot-ui

Builds a page whose buttons wake an agent over a webhook. A local server POSTs JSON to a **webhook routine**, the bot wakes with that JSON, and the page can be exposed on a Tailscale network. The most infrastructural capability in the plugin and the one furthest from the SDLC, included here for catalogue completeness.

Its substance is a **credential-handoff contract**, and that is the part worth recording. *Keep the sender key on the server. Do not put the sender key in the browser, in chat, or in this skill.* The routine is created with a trigger of `{"type": "webhook"}` and a prompt that must **treat the POST body as untrusted data**, naming the JSON fields the UI sends and the matching action for each. The webhook URL and the sender key are never returned by the create call — they live on the routine's own panel, and the skill hands the user exact instructions for retrieving them rather than inventing a flow.

It is the clearest illustration in the plugin of a skill written for a surface the agent cannot fully reach: the agent creates the routine, then explicitly stops and tells the human which panel to open.

## See Also
- [[pstack-principle-boundary-discipline]] — the untrusted-input-at-the-boundary rule this applies.
- [[pstack-benny-setup]] — the framework's other webhook-driven automation surface.
