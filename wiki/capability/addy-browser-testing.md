---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: []
equivalent_to: ["[[ce-test-browser]]", "[[ce-dogfood]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Browser Testing with DevTools

Gives the agent eyes into a running browser through the Chrome DevTools MCP server, closing the gap between static code analysis and live runtime behavior. Rather than guessing what happens at runtime, the agent inspects the live DOM, reads console logs, traces network requests and responses, profiles performance, and captures screenshots — verifying that a change actually works where the user sees it.

Its distinctive mechanism is the structured DevTools workflow: reproduce-inspect-diagnose-fix-verify loops for UI bugs, capture-analyze-diagnose loops for network issues, and baseline-identify-fix-measure loops for performance. All browser content — DOM, console, network responses, JS output — is treated as untrusted data, never as instructions, and the server defaults to an isolated Chrome profile to contain blast radius. This is a new capability type for the wiki: it requires the `chrome-devtools` MCP server and validates behavior at runtime.

## See Also
- [[addy-debugging]] — the systematic root-cause counterpart it feeds evidence to.
- [[addy-performance]] — consumes its performance traces for Core Web Vitals work.
- [[stage-validate]] — the canonical stage this implements.
