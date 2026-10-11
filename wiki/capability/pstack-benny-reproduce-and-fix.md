---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-pull-request]]"]
applies: ["[[pattern-systematic-debugging]]", "[[pattern-evidence-before-claims]]", "[[pattern-autonomous-loop]]", "[[pattern-deterministic-gates]]", "[[pattern-action-gating]]"]
equivalent_to: ["[[gstack-ios-fix]]", "[[ce-dogfood]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-26
---

# reproduce-and-fix-issues

The second half of the **benny** automation pack, and the framework's only fully unattended code-writing capability. It waits for a trusted triage marker from [[pstack-benny-triage]] in the source thread, reproduces the exact symptom **through the target app's real UI** via a configured control adapter, verifies an existing fix when one exists, and opens a bounded **draft** pull request only after before-and-after proof.

Every clause of that sentence is a constraint, and together they are the most conservative autonomous-fix loop in the wiki:

- **It never self-starts.** A trusted triage marker, posted by the separate triage automation, is the entry condition.
- **Reproduction goes through the real UI**, not through a unit test or an internal call, using the configured control adapter — the same standard [[pstack-create-verification-skill]] writes into every harness it generates.
- **An attempted fix requires a confirmed repro first**, which is [[pstack-principle-fix-root-causes]] as a gate rather than as advice.
- **Before-and-after proof gates the PR**, and the PR is a **draft** and **bounded**. A human still reviews and lands.
- **It fails closed.** If the config, required actions, control adapter, or completed feature map is missing, the run stops.

Compared with the wiki's other autonomous fix loops — [[gstack-ios-fix]] and [[gstack-qa]] find, fix, and re-verify against a live surface in a developer's session, and [[ce-dogfood]] runs the product against itself — this one is triggered by an external report from a non-developer, runs with nobody watching, and therefore ends at a draft rather than at a merge. The distance between a capability's autonomy and its **authority** is the thing this page records: benny is highly autonomous and deliberately low-authority.

## See Also
- [[pstack-benny-triage]] — supplies the trusted marker this waits for.
- [[pstack-benny-setup]] — configures the control adapter and feature map it fails closed without.
- [[pstack-create-verification-skill]] — the same real-user-path proof standard, for a developer-driven harness.
- [[gstack-ios-fix]] · [[ce-dogfood]] — the autonomous-loop counterparts.
- [[stage-implement]] — the canonical stage this implements.
