---
type: capability
subtype: sub-agent
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-perf-audit]]"]
applies: ["[[pattern-measure-first]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[ce-performance-oracle]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-05
---

# Web Performance Auditor (persona)

A Web Performance Engineer persona that audits Core Web Vitals (LCP, INP, CLS) and prioritizes findings by real-world user impact. It runs in two modes. Quick mode (the default, no tool artifacts) scans source directly for structural anti-patterns and tags every finding "potential impact", leaving the scorecard "not measured". Deep mode interprets measured data from Lighthouse, PageSpeed Insights, the CrUX API, or a DevTools trace, and labels each scorecard value with its source. A strict metric-honesty rule forbids fabricating metrics or presenting lab numbers as field numbers — an LLM reading static code cannot measure LCP, INP, or CLS.

It runs as a stateless review subagent with a fresh context and never invokes other personas. It is run via the dedicated `/webperf` command and is deliberately excluded from the [[addy-shipping]] `/ship` fan-out, since performance audits apply only to web applications and would add noise in non-web projects.

## See Also
- [[addy-performance]]
- [[pattern-measure-first]]
- [[artifact-perf-audit]]
- [[stage-review]]
