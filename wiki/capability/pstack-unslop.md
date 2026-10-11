---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /unslop

Cuts AI tells from any writing. Its frontmatter description is two words long and carries the whole policy: ***"Must always apply."*** [[pstack-poteto-mode]] routes every prose surface through it and states that the agent's own reply is a prose surface.

The rules are a numbered catalogue of detectable patterns — superficial `-ing` phrases (*"highlighting…", "ensuring…", "showcasing…"*), vague attributions (*"experts believe", "industry reports suggest"*), AI vocabulary (*additionally, crucial, delve, enhance, intricate, landscape, pivotal, showcase, tapestry, testament, underscore*), fancy ways to say *is* (*"serves as", "stands as", "boasts"*), *"not just X, but Y"*, the forced rule of three, and synonym cycling. Three steps: scan, rewrite preserving meaning and tone, then self-audit by asking *what makes this obviously AI generated?*

**The mechanism worth recording is that the rule numbers are a stable API.** *"Rule numbers are stable ids that other skills cite. A removed rule leaves a gap."* Numbers are never reused, so [[pstack-poteto-mode]]'s reply rules can cite *unslop rule 14* (no colon as a mid-sentence connector) and [[pstack-technical-writing]] can propose a new offender as an addition to unslop's abstract-metaphor rule — *with the diff, in the reply, without editing that skill*. A prose-quality skill given a versioned identifier scheme so sibling skills can depend on individual rules is a small thing, but it is the clearest instance in the wiki of a framework treating its own skills as an interface rather than as documents.

The framework also ships a **narrower relative that is not this skill**: `/deslop`, which runs before commit, lives in the separate `cursor-team-kit` plugin and is not bundled here.

## See Also
- [[pstack-technical-writing]] — the layered doc standard; unslop is the always-on floor beneath it.
- [[pstack-bro]] — the plain-language restatement skill.
- [[pstack-poteto-mode]] — carries the reply rules that cite unslop by rule number.
