---
type: pattern
sources: "Tessl docs (2026); Anthropic — The AI-Native SDLC playbook (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md", "../../raw/reference/2026-08-21-ai-native-sdlc-playbook.md"]
updated: 2026-09-12
---

# Pattern: Capability evals (prove the instructions changed the behavior)

Measure whether a **capability actually works** by running an agent on real tasks twice — once without it and once with it — and scoring the difference. Keep the tasks as a suite alongside the capability so every later change re-runs them.

> An evaluation runs an agent on real tasks twice, once without the skill and once with it, then scores the difference. That difference is the skill's value: **proof it changes what the agent does, not just that it reads well.** — [[tessl]]

The A/B is the whole point and is what separates this from ordinary review. A skill can be well-structured, well-described, and clearly written and still change nothing about the output; without a baseline run you cannot tell. The unit under test is not the code the agent wrote, it is **the instructions that shaped it**.

## Why it is distinctive

Every other verification pattern here tests the **product**: [[pattern-test-driven-development]] tests the code, [[pattern-evidence-before-claims]] tests the claim about the code, [[pattern-deterministic-gates]] runs a program over the code. This one tests **the agent's own configuration** — the layer that decides how all of those get done. It is the QA gate rebuilt for the thing that now varies.

That makes it the first pattern in the wiki whose subject is a `capability` page rather than a piece of software, and it is why it belongs to the [supply layer](../registry/index.md): once capabilities are traded as versioned dependencies, "does this dependency help?" becomes a question someone has to answer with evidence rather than taste.

**The scenarios become a regression suite.** *"The scenarios are saved with the skill, so anyone who changes it later can re-run the same scenarios and confirm it still behaves as expected."* This is the mechanism that makes a shared skill corpus safe to edit — the failure mode it addresses is a team that will not touch a skill because nobody can tell what a change would break → [[artifact-eval-suite]].

**It has a cheap sibling it should not be confused with.** Tessl runs both, and names the distinction: a **review** is fast, structural, and automatic on publish (*is it well written?*); an **eval** is slow, task-based, and deliberate (*does it work?*). Reach for the eval before publishing something others will use in agents you never see.

## Supplied by (registry)

- [[tessl]] — [[tessl-eval]] runs the A/B and scores it; [[tessl-scenario]] generates the tasks, each server-side feasibility-checked so the suite exercises the skill rather than padding it, each pairing a task with a weighted rubric. Evals attach to a project (a repository anchor), so results stay tied to the right codebase.

## Applied by (backlinks)

pstack — the in-framework version of the same instinct, without the measurement:

- [[pstack-poteto-mode]] — ships an **Eval playbook** for testing how a skill, structure, or prompt change affects agent behavior *before promoting it*, run blinded.
- [[pstack-reflect]] — gates its own accepted learnings with a structural-enforcement check, which is the same question (does this instruction earn its place?) answered by judgment rather than by an A/B.

## See Also
- [[artifact-eval-suite]] — the durable output: scenarios plus rubrics, versioned with the capability.
- [[pattern-evidence-before-claims]] — the parent discipline; this is that discipline pointed at the instructions instead of the work.
- [[pattern-deterministic-gates]] — what an eval becomes once its score is enforced at merge.
- [[pattern-knowledge-compounding]] — capability evals are what make a compounding corpus safe to keep editing.
- [[topic-ai-native-sdlc]] — recorded this instrument as unshipped by any framework; [[tessl]] ships it from the supply layer.
