---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl search

Search the registry and install from the results, interactively or by query. The discovery half of the package manager, against an index that is both **public** (thousands of evaluated skills and plugins, advertised at 3,000+) and **private** (a workspace's own context), searched as one surface.

Its interesting property is what the results carry. Because [[tessl-review]] runs automatically on publish and its score is published with the entry, search results come with a quality signal attached — *"it is also where your published quality scores appear, so others can judge whether a skill is worth installing"*. Discovery in this layer is therefore never purely nominal: the index is also the place a capability's review score, security findings, and eval evidence are visible before you take it.

That is the difference between a registry and a list of links, and it is the dimension along which the layer's `index` and `platform` subtypes separate.

## See Also
- [[tessl-install]] — takes what this finds.
- [[tessl-review]] · [[tessl-review-security]] — produce the scores shown against a result.
- [[tessl-inventory]] — the inward-facing counterpart: search finds what exists publicly, inventory finds what you already have.
