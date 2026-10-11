---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-idempotent-operations]]"]
equivalent_to: ["[[gstack-setup-deploy]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# setup-benny

Installs and configures **benny**, the dormant automation pack pstack ships alongside its skills. Benny gives a repository two Cursor automations for Slack issue reports: one triages each report ([[pstack-benny-triage]]), the other reproduces confirmed bugs and may prepare a small draft fix ([[pstack-benny-reproduce-and-fix]]).

The pack's status is the distinctive thing. **Its files are not registered as slash skills** — the plugin manifest exposes only pstack's normal skill root, so benny ships inert inside the plugin and is activated per repository. A human enters setup by pointing Cursor at the pack's `FOR_AGENTS.md`, which copies the whole pack into the target repository at `.cursor/automations/benny/` and then reads this file from its new location.

Four installation rules carry the design:

- The copy **preserves destination-only files and reviews conflicts instead of overwriting local edits**, so re-running setup over a customized installation is safe.
- Setup **enables pstack in the target repository's `.cursor/settings.json`** for shared skills, making benny a consumer of the parent plugin rather than a self-contained pack.
- **User-owned configuration stays outside the copied pack** (for example in `.cursor/benny/`), adapted from shipped `configuration.example.yaml` and `feature-map.example.md` templates. That boundary is what makes the pack upgradable without clobbering a team's settings.
- Nothing is enabled until `.cursor/settings.json`, the pack, and any **secret-free** configuration are committed, each automation draft is reviewed in its editor, and a harmless test report has been sent to verify every source-channel post stays in its original thread.

This is the wiki's first instance of a framework shipping a **dormant, repo-installed automation pack** distinct from its invocable skill surface — capabilities that run on an external trigger rather than on a developer's prompt.

## See Also
- [[pstack-benny-triage]] · [[pstack-benny-reproduce-and-fix]] — the two automations this configures.
- [[pstack-setup-pstack]] — the framework's other setup command, for model roles.
- [[pstack]] — the plugin benny ships inside.
