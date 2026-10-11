---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-source-grounding]]", "[[pattern-evidence-before-claims]]"]
equivalent_to: ["[[addy-source-driven-development]]"]
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /read-the-damn-docs

Make the agent **web-search for current official docs before guessing from model memory**. *"Do not guess where authoritative docs can answer the question."*

The skill's main contribution is its **trigger list**. Docs are required when the user says *latest / current / official / supported / recommended*; when a package, SDK, CLI, model, or provider is added, upgraded, or configured; when the API is fast-moving (it names AI SDKs, Next.js, Tailwind, Drizzle, Stripe, GitHub, and others); when auth, OAuth scopes, secrets, webhooks, billing, PII, migrations, rate limits, deploys, or compliance are involved; when an error mentions deprecation, unknown options, missing exports, or version mismatch; when the repo has local ADRs, schemas, or registries that could define the contract; when the choice is expensive to reverse; and when *"you catch yourself about to write 'usually', 'probably', 'I think', 'from memory'."*

The source hierarchy is local repo docs, then official upstream docs and changelogs, then package-registry metadata (`npm view <pkg> version` *before* adding a dependency), then source and types. Stack Overflow and blog posts are for debugging symptoms only *"after the authoritative contract is known."* If docs cannot be reached, the agent says so and does not present the result as confirmed-current. It also scales down: trivial syntax and self-contained code proceed normally.

[[stage-implement]], matching its counterpart [[addy-source-driven-development]]. The signature capability for [[pattern-source-grounding]] in this framework.

## See Also
- [[addy-source-driven-development]] — the counterpart in Addy's framework.
- [[pattern-source-grounding]] — the pattern.
- [[stage-implement]] — the canonical stage this implements.
