---
type: pattern
sources: "Addy Osmani — Agent Skills (2026)"
updated: 2026-07-04
---

# Pattern: Feature flags (decouple deploy from release)

Gate new behavior behind a flag so code can be **deployed** to production continuously while its **release** to users is a separate, controlled decision. Enables safe defaults, staged rollouts (percentage ramps), instant rollback (flip the flag, no redeploy), and lets unfinished work live on trunk. Flags have a lifecycle — they must be retired once the rollout completes, or they become their own [[addy-deprecation]] liability.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-incremental-implementation]] — feature flags + safe defaults for rollback-friendly slices.
- [[addy-ci-cd]] — flag-driven deployment strategies.
- [[addy-shipping]] — feature-flag lifecycle, staged rollouts, rollback procedures.

## See Also
- [[pattern-trunk-based-development]] — keeps in-progress work on trunk without shipping it.
- [[artifact-launch-checklist]] — where flag state and rollback are recorded.
- [[stage-release]] — the stage this pattern serves.
