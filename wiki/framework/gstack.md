---
type: framework
source_url: "https://github.com/garrytan/gstack"
sources: "Garry Tan — gstack (github.com/garrytan/gstack), MIT (2026); README, AGENTS.md, ETHOS.md, ARCHITECTURE.md"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# gstack

**gstack** is Garry Tan's (President & CEO of Y Combinator) open-source, MIT-licensed toolkit that **turns Claude Code into a virtual engineering team** — "a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who opens a real browser, a security officer who runs OWASP + STRIDE audits, and a release engineer who ships the PR." It is the **largest framework in this wiki**: ~54 skills (all slash-commands, all Markdown) plus standalone CLIs, organized around a full **sprint**:

> **Think → Plan → Build → Review → Test → Ship → Reflect**

"gstack is a process, not a collection of tools. The skills run in the order a sprint runs" — each skill feeds outputs into the next (`/office-hours` writes a design doc `/plan-ceo-review` reads; `/plan-eng-review` writes a test plan `/qa` picks up; `/review` catches bugs `/ship` verifies). It is built for founders/CTOs/tech-leads who still ship, is engineered for **10–15 parallel sprints** (via [Conductor](https://conductor.build)), and works across 10 coding agents (Claude Code, Codex, Cursor, Factory, …). Install: `git clone … ~/.claude/skills/gstack && ./setup`.

- **Root router:** [[gstack-router]] — the `gstack` skill dispatches work to the right specialist skill (its counterpart is Addy's [[addy-using-agent-skills]]).
- **Builder ethos (injected into every workflow preamble):** *Boil the Ocean* (completeness is near-free with AI — do the complete thing), *Search Before Building* (three layers of knowledge; the "eureka" is zigging where others zag → [[pattern-source-grounding]]), *User Sovereignty* (models recommend, users decide — the generation-verification loop, Karpathy's "Iron Man suit").

## Distinctive contributions to the ontology

- **The clean Review ∥ Test partition — it promoted a new canonical stage.** gstack's sprint separates a **Review** phase (code/design/security review: [[gstack-review]], [[gstack-codex]], [[gstack-design-review]], [[gstack-devex-review]]) from a distinct **Test** phase (functional browser QA: [[gstack-qa]], [[gstack-qa-only]]). As the **second framework** (after Addy) with that clean *functional-validation ∥ quality-review* partition, gstack **cleared the bar to split [[stage-review]] out of [[stage-validate]]** (2026-07-05): its Review-phase skills implement [[stage-review]], its Test-phase skills [[stage-validate]].
- **A genuine deploy + operate arc.** gstack is the **first framework here to separate deploy from ship**: [[gstack-ship]] (PR) → [[gstack-land-and-deploy]] (merge, deploy, verify prod health) → [[gstack-canary]] (post-deploy monitoring). This strengthens the [[stage-release]] `stage-operate` split candidate.
- **A third framework for [[stage-learn]].** [[gstack-retro]] (team retrospective) + [[gstack-learn]] (a compounding cross-session learnings corpus) + [[gstack-skillify]] (codify a successful run into a permanent skill) give the *Reflect* stage a **third framework** alongside Compound Engineering and BMAD — beyond doubt now.
- **A third framework for [[pattern-persona-agents]].** gstack is thoroughly persona-oriented (CEO / Eng Manager / Senior Designer / DX Lead / Staff Engineer / QA Lead / CSO / SRE / Release Engineer), joining BMAD as the second framework whose whole toolkit is named expert personas.

## Signature mechanisms

- **Persistent browser daemon ("the eyes").** A long-lived headless Chromium daemon ([[gstack-browse]]) gives the agent real clicks/screenshots at ~100ms/command with persistent cookies/tabs — the infrastructure that makes live [[gstack-qa]], [[gstack-design-review]], [[gstack-canary]], and [[gstack-benchmark]] possible. `/qa` "let me go from 6 to 12 parallel workers."
- **Cross-model second opinion.** [[gstack-codex]] runs an independent OpenAI Codex review; when both [[gstack-review]] (Claude) and Codex have run, a cross-model analysis shows overlapping vs unique findings — [[pattern-cross-model-review]] (shared with Compound Engineering).
- **Safety guardrails on demand.** [[gstack-careful]] / [[gstack-freeze]] / [[gstack-guard]] / [[gstack-unfreeze]] confirm destructive commands and lock edits to a directory ([[pattern-edit-guardrails]]); [[gstack-investigate]] auto-freezes to the module under investigation.
- **Knowledge compounding.** [[gstack-learn]] (cross-session learnings), gbrain persistent memory ([[gstack-setup-gbrain]], [[gstack-sync-gbrain]]), design **taste memory** ([[gstack-design-shotgun]]), and per-site domain skills ([[gstack-skillify]]) all make the agent smarter on your codebase over time — [[pattern-knowledge-compounding]].
- **Autonomous self-fixing loops.** [[gstack-qa]], [[gstack-ios-fix]], and [[gstack-canary]] find→fix→re-verify with regression tests generated per fix ([[pattern-autonomous-loop]], [[pattern-test-driven-development]]).
- **Continuous checkpointing.** Opt-in `WIP:` commits with structured `[gstack-context]` bodies survive crashes; [[gstack-context-save]] / [[gstack-context-restore]] reconstruct session state ([[pattern-session-handoff]]).
- **Prompt-injection defense** for the browser sidebar agent (ML classifier + Haiku vote + canary token + verdict combiner) — a security-hardening stack unique among these frameworks (infra, not a lifecycle capability).

## Capabilities by sprint stage

### Think — [[stage-align]]
- [[gstack-office-hours]] — YC Office Hours; reframe the product with six forcing questions before any code; writes the design doc every downstream skill reads.

### Plan — [[stage-plan]]
- [[gstack-plan-ceo-review]] — CEO/founder review; find the 10-star product; four scope modes.
- [[gstack-plan-eng-review]] — Eng-manager review; lock architecture, data flow, edge cases, tests.
- [[gstack-plan-design-review]] — Senior-designer review; rate each design dimension 0-10; AI-slop detection.
- [[gstack-plan-devex-review]] — Developer-experience review; TTHW, personas, magical moment, friction traces.
- [[gstack-autoplan]] — run CEO → design → eng → DX reviews sequentially with auto-decisions; surface only taste calls.
- [[gstack-plan-tune]] — self-tune AskUserQuestion sensitivity + developer psychographic (plan-review meta).
- [[gstack-design-consultation]] — build a complete design system from scratch (aesthetic/type/color/layout/motion) → `DESIGN.md`.

### Specify — [[stage-specify]]
- [[gstack-spec]] — turn vague intent into a precise, executable spec in five phases; Codex quality gate; files a GitHub issue; `--execute` spawns a fresh-worktree agent.

### Build — [[stage-implement]]
- [[gstack-design-shotgun]] — generate 4-6 AI mockup variants, comparison board, taste-memory iteration.
- [[gstack-design-html]] — turn an approved mockup into production Pretext-native HTML/CSS.
- [[gstack-investigate]] — systematic root-cause debugging; Iron Law: no fixes without investigation; auto-freeze.
- [[gstack-scrape]] — pull structured data from a web page (prototype run, then ~200ms codified run).
- [[gstack-careful]] · [[gstack-freeze]] · [[gstack-guard]] · [[gstack-unfreeze]] — safety guardrails and directory-scoped edit locks ([[pattern-edit-guardrails]]).
- [[gstack-context-save]] · [[gstack-context-restore]] — save/restore working context across sessions and Conductor workspaces ([[pattern-session-handoff]]).

### Review — quality gate ([[stage-review]])
- [[gstack-review]] — Staff-Engineer pre-landing PR review; finds bugs that pass CI but break in prod; auto-fixes the obvious.
- [[gstack-codex]] — OpenAI Codex second opinion; review / adversarial-challenge / consult modes; cross-model analysis.
- [[gstack-design-review]] — Designer-who-codes live visual audit + fix loop with atomic commits.
- [[gstack-devex-review]] — live developer-experience audit; measures TTHW against the real flow (the `/plan-devex-review` boomerang).
- [[gstack-cso]] — Chief Security Officer; OWASP Top 10 + STRIDE threat model with concrete exploit scenarios.
- [[gstack-health]] — code-quality dashboard (type checker, linter, tests, dead code).

### Test — functional QA ([[stage-validate]])
- [[gstack-qa]] — QA Lead; real browser, find bugs, fix with atomic commits, re-verify, auto-generate regression tests.
- [[gstack-qa-only]] — same methodology, report-only (no code changes).
- [[gstack-benchmark]] — performance regression: page load, Core Web Vitals, resource sizes, before/after per PR.

### Ship — [[stage-release]]
- [[gstack-ship]] — Release Engineer; sync base, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, open PR.
- [[gstack-land-and-deploy]] — merge the PR, wait for CI + deploy, verify production health.
- [[gstack-canary]] — SRE; post-deploy monitoring loop (console errors, perf regressions, page failures).
- [[gstack-landing-report]] — read-only dashboard for the workspace-aware ship queue.
- [[gstack-document-release]] — post-ship doc update; Diataxis coverage map in the PR body.
- [[gstack-document-generate]] — generate missing Diataxis docs (tutorial/how-to/reference/explanation) from code.
- [[gstack-setup-deploy]] — one-time deploy-config detection (Fly.io / Render / Vercel / …).
- [[gstack-ios-clean]] — strip the DebugBridge + `#if DEBUG` wiring before a Release build.

### Reflect — [[stage-learn]]
- [[gstack-retro]] — team-aware weekly retrospective; per-person breakdowns, shipping streaks, test-health trends.
- [[gstack-learn]] — manage the cross-session learnings corpus (patterns/pitfalls/preferences) so gstack compounds on your codebase.
- [[gstack-skillify]] — codify the most recent successful [[gstack-scrape]] into a permanent browser-skill.

### iOS live-device QA
- [[gstack-ios-qa]] — drive a real iPhone over USB CoreDevice (optionally over Tailscale) with an embedded StateServer ([[stage-validate]]).
- [[gstack-ios-fix]] — autonomous iOS bug fixer with regression-snapshot capture ([[stage-validate]]).
- [[gstack-ios-design-review]] — designer's-eye QA on real hardware; 10-dimension Apple HIG rubric ([[stage-review]]).
- [[gstack-ios-sync]] — regenerate the iOS debug-bridge accessors against the latest templates (enabling; [[stage-validate]]).

### Browser & agent-integration infrastructure
- [[gstack-browse]] — the persistent headless-Chromium daemon; the "eyes" behind live QA ([[stage-validate]] enabling).
- [[gstack-open-gstack-browser]] — launch the visible GStack Browser with sidebar + anti-bot stealth.
- [[gstack-setup-browser-cookies]] — import cookies from your real browser for authenticated testing.
- [[gstack-pair-agent]] — pair a remote/cross-vendor AI agent with your browser (scoped tokens, tab isolation).

### Memory & knowledge infrastructure
- [[gstack-setup-gbrain]] — set up gbrain persistent cross-machine memory (PGLite / Supabase / remote MCP).
- [[gstack-sync-gbrain]] — re-index this repo's code into gbrain and refresh CLAUDE.md search guidance.

### Cross-cutting utilities (no single lifecycle stage)
- [[gstack-diagram]] — English (or mermaid) → diagram triplet (mermaid + editable `.excalidraw` + SVG/PNG), offline.
- [[gstack-make-pdf]] — any markdown → publication-quality PDF (renders mermaid/excalidraw fences), `--to html|docx`.
- [[gstack-benchmark-models]] — cross-model benchmark for gstack's own skills (Claude / GPT / Gemini) (meta/tooling).
- [[gstack-upgrade]] — self-updater; detects global vs vendored install (meta/tooling).

## Artifacts produced
- [[artifact-product-brief]] — [[gstack-office-hours]]' reframed product/design doc that feeds the plan reviews.
- [[artifact-design-md]] — the `DESIGN.md` design system ([[gstack-design-consultation]]).
- [[artifact-design-mockup]] — **AI-generated visual mockup variants** on a comparison board ([[gstack-design-shotgun]]).
- [[artifact-spec-md]] · [[artifact-issue]] — the executable spec + filed GitHub issue ([[gstack-spec]]).
- [[artifact-review-report]] — review findings ([[gstack-review]], [[gstack-codex]], [[gstack-design-review]], [[gstack-devex-review]]).
- [[artifact-security-audit]] — OWASP + STRIDE report with exploit scenarios ([[gstack-cso]]).
- [[artifact-perf-audit]] — Core Web Vitals / load benchmark ([[gstack-benchmark]]).
- [[artifact-atomic-commit]] — one commit per fix/slice ([[gstack-qa]], [[gstack-design-review]], [[gstack-ship]]).
- [[artifact-pull-request]] · [[artifact-changelog]] — the opened PR + version/changelog bump ([[gstack-ship]]).
- [[artifact-diataxis-docs]] — **Diataxis-structured documentation** (tutorial/how-to/reference/explanation) ([[gstack-document-generate]], [[gstack-document-release]]).
- [[artifact-retrospective]] — the weekly retro report ([[gstack-retro]]).
- [[artifact-solution-doc]] — the compounding learnings corpus ([[gstack-learn]]; agent-grounding flavor).

## Patterns applied
- [[pattern-persona-agents]] — **signature (shared with BMAD)** — a named expert specialist per role (CEO, eng manager, designer, QA lead, CSO, SRE, release engineer).
- [[pattern-parallel-persona-review]] — the plan-review panel + smart review routing ([[gstack-autoplan]], the four `plan-*-review` skills).
- [[pattern-cross-model-review]] — **signature (shared with CE)** — an independent second opinion from a different model/vendor ([[gstack-codex]]).
- [[pattern-edit-guardrails]] — **signature** — confirm destructive commands + lock edits to scope ([[gstack-careful]], [[gstack-freeze]], [[gstack-guard]]).
- [[pattern-autonomous-loop]] — self-fixing find→fix→verify loops ([[gstack-qa]], [[gstack-ios-fix]], [[gstack-canary]]).
- [[pattern-knowledge-compounding]] — **third framework** — learnings, gbrain, taste memory, domain skills ([[gstack-learn]], [[gstack-skillify]], [[gstack-sync-gbrain]]).
- [[pattern-test-driven-development]] — regression test per fix; `/ship` bootstraps a test framework if none exists; 100% coverage goal.
- [[pattern-systematic-debugging]] — Iron Law: no fixes without investigation ([[gstack-investigate]], [[gstack-ios-fix]]).
- [[pattern-session-handoff]] — **third framework** — continuous WIP-checkpoint commits + context save/restore ([[gstack-context-save]], [[gstack-context-restore]]).
- [[pattern-adversarial-review]] — Codex's challenge mode "actively tries to break your code" ([[gstack-codex]], [[gstack-review]]).
- [[pattern-source-grounding]] — the *Search Before Building* ethos; landscape research ([[gstack-design-consultation]], [[gstack-office-hours]]).
- [[pattern-spec-driven-development]] — the executable spec drives execution ([[gstack-spec]]).
- [[pattern-throwaway-prototype]] — visual mockup exploration before committing to code ([[gstack-design-shotgun]]).
- [[pattern-measure-first]] — baseline before optimizing ([[gstack-benchmark]]).
- [[pattern-trunk-based-development]] — atomic commits, short branches, PR flow ([[gstack-ship]]).
- [[pattern-fresh-context-subagents]] — the sidebar agent's isolated session; `spec --execute`'s fresh worktree.
- [[pattern-context-engineering]] — gbrain search guidance written into CLAUDE.md ([[gstack-sync-gbrain]]).
- [[pattern-scale-adaptive-planning]] — smart review routing sizes the review ceremony to the change (CEO skips infra, design skips backend).

## See Also
- [[bmad]] — the other fully **persona-oriented** framework; both center named expert specialists ([[pattern-persona-agents]]). gstack's [[gstack-retro]] ↔ BMAD's [[bmad-retrospective]] (the team-retro flavor of [[stage-learn]]).
- [[compound-engineering]] — shares [[pattern-knowledge-compounding]] ([[gstack-learn]] ↔ [[ce-compound]]), [[pattern-cross-model-review]], [[pattern-autonomous-loop]] ([[gstack-qa]] ↔ [[ce-dogfood]]), and the persona-review fan-out.
- [[addy-agent-skills]] — the other lifecycle-broad pack; both split **Review** from **Test/Verify** as distinct phases (together they promoted [[stage-review]] out of [[stage-validate]]); [[gstack-router]] ↔ [[addy-using-agent-skills]]; [[gstack-cso]] ↔ [[addy-security-auditor]]; [[gstack-benchmark]] ↔ [[addy-web-performance-auditor]]; [[gstack-ship]] ↔ [[addy-shipping]].
- [[gsd]] — the plan→execute→verify→ship spine; [[gstack-ship]] ↔ [[gsd-ship]]; [[gstack-investigate]] ↔ [[gsd-debugger]].
- [[stage-align]] · [[stage-plan]] · [[stage-specify]] · [[stage-implement]] · [[stage-review]] · [[stage-validate]] · [[stage-release]] · [[stage-learn]] — the canonical stages this framework's capabilities feed (spanning **all eight**, and the only framework here with a genuine deploy + post-deploy-monitor arc).
