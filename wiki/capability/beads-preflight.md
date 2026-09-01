---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-deterministic-gates]]", "[[pattern-shift-left]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd preflight

`bd preflight [--check]` — *"a checklist of common pre-PR checks for contributors"*, which `--check` runs rather than merely printing, with `--json` for programmatic use.

The checklist is the interesting part, because it is a tracker checking the *working tree*:

- tests not run locally
- lint errors
- unformatted Go files
- **`.beads/issues.jsonl` pollution**
- stale nix `vendorHash`
- version mismatches

Two observations. First, this is the one command on this page that reaches outside the store's own concerns into the repository — and it earns that by catching the store's own footgun: a stray `.beads/issues.jsonl` diff in a PR, which is exactly the noise that follows from keeping the tracker inside the repo. Second, several checks are beads-repo-specific (nix vendorHash, Go formatting), so this is partly a tool that grew from dogfooding rather than a general capability — worth recording plainly rather than presenting as universal.

`--fix` is declared *"not yet implemented"*, which is honest and unusual.

Maps to **no canonical SDLC stage**: it gates a PR without performing review or validation. Its [[pattern-shift-left]] edge is the intent — move the CI failure to before the push.

## See Also
- [[beads-doctor]] · [[beads-lint]] — the checks on the installation and on issue content.
- [[gstack-health]] — the same idea as a first-class codebase review capability.
- [[pattern-deterministic-gates]] — the pattern it applies.
