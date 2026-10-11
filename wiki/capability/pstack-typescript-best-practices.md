---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-standards]]"]
applies: ["[[pattern-contract-first]]", "[[pattern-deterministic-gates]]", "[[pattern-test-driven-development]]"]
equivalent_to: ["[[agent-os-inject-standards]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# /typescript-best-practices

Grounds [[pstack-principle-type-system-discipline]] in actual syntax. It is the **only skill in the plugin that attaches by file path** (`paths: ["**/*.ts", "**/*.tsx"]`) rather than by invocation, so it loads whenever TypeScript is read or edited — the one place pstack accepts automatic skill activation, having set `disable-model-invocation: true` on everything else.

The body is a rule table, and the rules are noticeably sharper than the usual style-guide fare:

- **Constructive modeling.** Build the shape so the illegal value cannot be constructed: `[T, ...T[]]` for non-empty, `[T, T][]` for even length, `start` plus `duration` for a range. *Not a runtime guard, not a wish for refinement types.*
- **Simplest total type.** Keep `T[]` while every operation on it stays total. Strengthen to `NonEmpty<T>` only where the loose type forces a `!`, a cast, or a "should never happen" throw. This is the counterweight that stops the previous rule turning into type astronautics.
- **Narrowing hierarchy**, ranked: discriminant switch > `in` > `typeof`/`instanceof` > user-defined type guard > `as`.
- **Type guards must verify the claim.** *A lying guard is worse than `as` because the bug hides behind a name that says it is safe.*
- **Schemas before guards** — infer from the repo's runtime schema library (`z.infer`) rather than hand-writing a property-by-property guard — and **schema-derived types**: reach for `Pick`/`Omit`/`Parameters`/`ReturnType`/`Awaited`/`typeof` before declaring a new interface.
- **Boundary validation.** Parse where data crosses in, into a named domain type. `Record<string, unknown>`, however spelled, **stops at that parse**. Trust types inside. ([[pstack-principle-boundary-discipline]].)
- **Exhaustiveness** via an inline `const _exhaustive: never = x;` in default arms, `satisfies` over `as`, `unknown` over `any`, branded primitives, and no `as` casts before validation.
- **Real tests.** *Do not mock what you can run.* Prefer the framework's real test primitives with leak and disposable checks, verify UI in a running build, and mock only what cannot run locally.

It is the framework's only language-specific capability, and its existence is the tell for how pstack thinks about standards: the general rule lives in a principle skill, and the language binding is a separate document that the harness attaches automatically where it applies.

## See Also
- [[pstack-principle-type-system-discipline]] — the general principle this grounds.
- [[pstack-principle-boundary-discipline]] — the parse-at-the-boundary rule.
- [[agent-os-inject-standards]] — the cross-framework durable-standards counterpart.
- [[stage-implement]] — the canonical stage this implements.
