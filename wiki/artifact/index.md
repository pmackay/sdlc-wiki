# Artifacts

*Index — lifecycle flow + counterpart map.*

The concrete **outputs** capabilities produce, one page per artifact. Each artifact is `produces:`-linked from the capabilities that write it (see [CONVENTIONS.md](../CONVENTIONS.md)) and carries its own `See Also` cross-links. This index projects those links two ways: a whole-lifecycle **flow overview** showing how one artifact leads to the next across the eight [SDLC stages](../sdlc-stage/index.md), then a **stage-by-stage detail** section that zooms into each stage with the layout that best fits its artifacts. The lifecycle is a loop, not a line — the Learn-stage artifacts feed back into the front of the next iteration.

## Lifecycle flow — how artifacts lead to one another

Solid arrows are the **production chain** (`X leads to / feeds / gates Y`); dotted arrows are the **loop-back** (`Learn output grounds the next iteration`). Nodes are grouped by the stage that produces them; the stage order runs top to bottom.

```mermaid
flowchart TD
    subgraph AL["1 · Align"]
        strat["STRATEGY.md"]
        const["constitution"]
        brief["product brief"]
        brain["brainstorm doc"]
        ctx["CONTEXT.md (phase)"]
        dom["domain model"]
    end
    subgraph SP["2 · Specify"]
        spec["SPEC.md / spec.md"]
        prd["PRD"]
        prop["proposal.md"]
        delta["spec delta"]
        chk["quality checklist"]
        nano["nano-spec pack"]
    end
    subgraph PL["3 · Plan"]
        res["RESEARCH.md"]
        arch["architecture spine"]
        design["design.md"]
        adr["ADR"]
        plan["PLAN.md / tasks.md"]
        issue["tracker issue"]
        story["story"]
    end
    subgraph IM["4 · Implement"]
        mock["design mockup"]
        commit["atomic commit"]
    end
    subgraph VA["5 · Validate"]
        uat["UAT.md"]
    end
    subgraph RV["6 · Review"]
        rev["code review report"]
        sec["security audit"]
        perf["perf audit"]
    end
    subgraph RE["7 · Release"]
        pr["pull request"]
        chlog["changelog + tag"]
        launch["launch checklist"]
        docs["Diataxis docs"]
    end
    subgraph LE["8 · Learn"]
        sol["solution doc"]
        expl["explainer"]
        retro["retrospective"]
        skill["skill doc"]
        handoff["handoff doc"]
    end

    strat -->|grounds| brain
    brief -->|scopes| prd
    const -->|governs| plan
    brain -->|enriched into| plan
    ctx -->|locks scope for| plan
    dom -->|informs| design
    prop -->|frames| delta
    delta -->|realised by| design
    chk -->|hardens| spec
    spec -->|decomposed into| plan
    prd -->|cut into| issue
    prd -->|cut into| story
    nano -->|packs as| plan
    res -->|feeds| design
    res -->|informs| plan
    arch -->|constrains| design
    design -->|derives| plan
    design -->|explored as| mock
    plan -->|exported as| issue
    plan -->|executed as| commit
    story -->|built as| commit
    issue -->|built as| commit
    mock -->|approved → code| commit
    commit -->|verified by| uat
    commit -->|reviewed by| rev
    commit -->|scanned by| sec
    commit -->|profiled by| perf
    commit -->|bundled into| pr
    uat -->|gates| pr
    rev -->|merged into| launch
    sec -->|merged into| launch
    perf -->|merged into| launch
    pr -->|shipped as| chlog
    launch -->|go / no-go| chlog
    pr -->|documented as| docs
    pr -->|mined into| sol
    pr -->|explained as| expl
    chlog -->|reviewed in| retro
    commit -->|codified as| skill

    sol -.->|grounds next loop| brain
    sol -.->|grounds next loop| plan
    sol -.->|grounds next loop| rev
    retro -.->|action items| strat
    skill -.->|reused in| plan
    handoff -.->|resumes| ctx
```

## Stage-by-stage detail

The overview above compresses everything into one loop. Below, each stage gets its own diagram laid out in the shape that fits its artifacts — a hub where several documents are variants of one canonical spec, a pipeline where research feeds design feeds tasks, a fan-in where three reports converge on a go/no-go. Solid arrows are `produces` / `feeds` / `gates`; dotted arrows are `counterpart` / `variant` resemblances. **Dashed rounded nodes** are boundary artifacts owned by an adjacent stage, shown only to place the stage in context.

### 1 · [Align](../sdlc-stage/stage-align.md) — *what to build and why*

Two standing anchors that persist across iterations, and four decision/scope docs that feed the spec and plan. The GSD and Matt Pocock frameworks both write a `CONTEXT.md`, but they are different artifacts — the dotted edge flags the clash.

```mermaid
flowchart LR
    subgraph anchors["Standing anchors — read across many iterations"]
        strat["STRATEGY.md"]
        const["constitution"]
    end
    subgraph shaping["Decision & scope capture"]
        brief["product brief"]
        brain["brainstorm doc"]
        ctx["CONTEXT.md (phase)"]
        dom["domain model"]
    end
    strat -.->|durable anchor: product vs code| const
    strat -->|grounds| brain
    brief -.->|pre-spec scoping sibling| brain
    brain -.->|decision-capture analogue| ctx
    ctx -.->|same filename, different artifact| dom
    brief -->|scopes| oPRD(["→ PRD · Specify"])
    brain -->|requirements| oPLAN(["→ PLAN.md · Plan"])
    ctx -->|locks scope| oPLAN
    dom -->|informs| oDES(["→ design.md · Plan"])
    classDef bound stroke-dasharray:5 4,fill:transparent;
    class oPRD,oPLAN,oDES bound
```

### 2 · [Specify](../sdlc-stage/stage-specify.md) — *the written contract*

A hub: five frameworks write the same slot as slightly different documents, all variants of one canonical `spec`. OpenSpec is the outlier — it splits the spec into a `proposal` (why/what) plus a behavioral `spec delta`.

```mermaid
flowchart LR
    prd["PRD"] -->|leaner counterpart| spec["SPEC.md / spec.md"]
    prop["proposal.md"] -.->|rationale-only slice| spec
    nano["nano-spec pack"] -.->|minimalist 4-file form| spec
    chk["quality checklist"] -.->|spec-quality gate| spec
    prop -->|frames| delta["spec delta"]
    spec -.->|delta-against-living-spec| delta
    spec -->|decomposed| oPLAN(["→ PLAN.md · Plan"])
    delta -->|realised by| oDES(["→ design.md · Plan"])
    classDef bound stroke-dasharray:5 4,fill:transparent;
    class oPLAN,oDES bound
```

### 3 · [Plan](../sdlc-stage/stage-plan.md) — *research, design, decompose*

A pipeline from investigation to executable units. Research and architecture feed the design; the design derives the task list; the task list becomes issues or context-rich stories that implementation consumes.

```mermaid
flowchart LR
    res["RESEARCH.md"] -->|feeds| design["design.md"]
    res -->|informs| plan["PLAN.md / tasks.md"]
    arch["architecture spine"] -->|constrains: system to per-change| design
    design -->|derives| plan
    design -.->|decision + rationale| adr["ADR"]
    plan -->|exported to| issue["tracker issue"]
    issue -.->|context-inlined form| story["story"]
    plan -.->|flat list vs context bundle| story
    plan -->|executed| oCMT(["→ atomic commit · Implement"])
    story -->|built| oCMT
    classDef bound stroke-dasharray:5 4,fill:transparent;
    class oCMT bound
```

### 4 · [Implement](../sdlc-stage/stage-implement.md) — *write the code*

Disposable UI mockups converge with the plan/story into the one durable output of this stage: an atomic commit per completed task, which then flows into validation and release.

```mermaid
flowchart LR
    iDES(["design.md · Plan"]) -->|explored as| mock["design mockup"]
    iPLAN(["PLAN.md / story · Plan"]) -->|implemented as| commit["atomic commit"]
    mock -->|approved then coded| commit
    commit -->|verified by| oUAT(["→ UAT.md · Validate"])
    commit -->|bundled into| oPR(["→ pull request · Release"])
    classDef bound stroke-dasharray:5 4,fill:transparent;
    class iDES,iPLAN,oUAT,oPR bound
```

### 5 · [Validate](../sdlc-stage/stage-validate.md) — *does it work?*

A single functional gate with a repair loop: UAT diagnoses gaps, the gaps become fix plans that re-enter implementation, and only a pass releases the change.

```mermaid
flowchart LR
    vCMT(["atomic commit · Implement"]) -->|UAT + auto-diagnosis| uat["UAT.md"]
    uat -->|gaps become fix plans| vCMT
    uat -->|passes| oPR(["→ pull request · Release"])
    classDef bound stroke-dasharray:5 4,fill:transparent;
    class vCMT,oPR bound
```

### 6 · [Review](../sdlc-stage/stage-review.md) — *is it good?*

A fan-in: three sibling assessment reports run in parallel over the change and converge into the release go/no-go decision.

```mermaid
flowchart LR
    rCMT(["atomic commit · Implement"]) -->|reviewed by| rev["code review report"]
    rCMT -->|scanned by| sec["security audit"]
    rCMT -->|profiled by| perf["perf audit"]
    rev -.->|sibling report| sec
    sec -.->|sibling report| perf
    rev -->|merged| gate(["→ go/no-go · Release"])
    sec -->|merged| gate
    perf -->|merged| gate
    classDef bound stroke-dasharray:5 4,fill:transparent;
    class rCMT,gate bound
```

### 7 · [Release](../sdlc-stage/stage-release.md) — *deliver it*

Commits, UAT pass, and the review reports converge on the pull request and launch checklist; shipping produces the changelog and the how-to-use documentation, then hands off to Learn.

```mermaid
flowchart LR
    reCMT(["atomic commit · Implement"]) -->|bundled into| pr["pull request"]
    reUAT(["UAT pass · Validate"]) -->|gates| pr
    reRPT(["review / security / perf · Review"]) -->|merged into| launch["launch checklist"]
    pr -->|shipped| chlog["changelog + tag"]
    launch -->|go/no-go| chlog
    pr -->|documented as| docs["Diataxis docs"]
    chlog -.->|what shipped vs how-to-use| docs
    chlog -->|reviewed in retro| oLEARN(["→ Learn"])
    classDef bound stroke-dasharray:5 4,fill:transparent;
    class reCMT,reUAT,reRPT,oLEARN bound
```

### 8 · [Learn](../sdlc-stage/stage-learn.md) — *harvest reusable lessons*

A hub around the agent-facing solution doc, with human-facing siblings, that closes the loop: its outputs ground the next iteration's Align, Plan, and Review.

```mermaid
flowchart LR
    lWORK(["shipped work · Release"]) -->|mined into| sol["solution doc"]
    sol -.->|agent- vs human-facing| expl["explainer"]
    sol -.->|agent- vs team-facing| retro["retrospective"]
    sol -.->|lesson vs runnable skill| skill["skill doc"]
    expl -.->|teach vs resume| handoff["handoff doc"]
    sol -->|grounds next iteration| loop(["→ Align · Plan · Review"])
    skill -->|auto-triggers in| loop
    classDef bound stroke-dasharray:5 4,fill:transparent;
    class lWORK,loop bound
```

## All artifacts by stage

| Stage | Artifact | Framework(s) | What it is |
|-------|----------|--------------|------------|
| Align | [[artifact-strategy-md\|STRATEGY.md]] | Compound Engineering | Standing product/engineering strategy that grounds ideation, brainstorm, and plan. |
| Align | [[artifact-constitution\|constitution]] | Spec Kit | Immutable project-wide governing principles that later phases are mechanically gated against. |
| Align | [[artifact-product-brief\|product brief]] | BMAD | Pre-PRD scoping doc (problem/audience/boundaries); variants PRFAQ and forged-idea. |
| Align | [[artifact-brainstorm-md\|brainstorm doc]] | Compound Engineering | Requirements-only unified plan (WHAT, not HOW) from a collaborative Q&A dialogue. |
| Align | [[artifact-phase-context\|CONTEXT.md (phase)]] | GSD | Locked decisions and scope guidance for a phase; feeds planning. |
| Align | [[artifact-domain-model\|domain model]] | Matt Pocock | Shared-language glossary (`CONTEXT.md`) mapping jargon to precise concepts. |
| Specify | [[artifact-spec-md\|SPEC.md / spec.md]] | Addy · Spec Kit · BMAD · MP | The durable written spec the lifecycle plans and builds against. |
| Specify | [[artifact-prd\|PRD]] | BMAD · Builder Methods | Fuller product-requirements document; intent and scope before issues/stories are cut. |
| Specify | [[artifact-proposal-md\|proposal.md]] | OpenSpec | The why/what + scope rationale layer, first in a change's dependency chain. |
| Specify | [[artifact-spec-delta\|spec delta]] | OpenSpec | ADDED/MODIFIED/REMOVED requirements against a living spec (brownfield-first). |
| Specify | [[artifact-checklist\|quality checklist]] | Spec Kit | Generated "unit tests for your English" — a spec-quality gate. |
| Specify | [[artifact-nano-spec-pack\|nano-spec pack]] | nano-spec | Four tiny files (README/todo/doc/log) per task — the minimalist spec form. |
| Plan | [[artifact-research-md\|RESEARCH.md]] | GSD · Spec Kit · BMAD · MP | Domain/technology research that informs the design and plan. |
| Plan | [[artifact-architecture\|architecture spine]] | BMAD | Lean invariants-only system-architecture contract. |
| Plan | [[artifact-design-md\|design.md]] | OpenSpec · Spec Kit · BMAD · BM | The technical/UX *how* — approach, decisions, data flow — kept separate from behavior. |
| Plan | [[artifact-adr\|ADR]] | MP · Addy · nano-spec | Per-decision architecture record: options · chosen · rationale. |
| Plan | [[artifact-plan-md\|PLAN.md / tasks.md]] | GSD · Addy · OpenSpec · Spec Kit · CE · BM · nano-spec | The executable task list / checklist derived from the spec and design. |
| Plan | [[artifact-issue\|tracker issue]] | MP · Spec Kit | A tracker issue materialised from a plan (decomposed or exported). |
| Plan | [[artifact-story\|story]] | BMAD | Context-rich story file: an issue with all implementation context inlined. |
| Implement | [[artifact-design-mockup\|design mockup]] | gstack | Disposable AI-generated UI variants on a comparison board with taste memory. |
| Implement | [[artifact-atomic-commit\|atomic commit]] | GSD · Addy · BMAD · CE | One atomic git commit per completed task. |
| Validate | [[artifact-uat-md\|UAT.md]] | GSD | User-acceptance-testing results + diagnosed gaps and fix plans. |
| Review | [[artifact-review-report\|code review report]] | Addy · BMAD · CE · gstack · MP | Structured five-axis review with severity labels and fix recommendations. |
| Review | [[artifact-security-audit\|security audit]] | Addy · CE · gstack | OWASP Top 10 vulnerability + threat-model assessment. |
| Review | [[artifact-perf-audit\|perf audit]] | Addy · CE · gstack | Core Web Vitals performance scorecard (Quick source scan / Deep measured). |
| Release | [[artifact-pull-request\|pull request]] | GSD · CE · gstack | The PR that aggregates a phase's commits at ship time. |
| Release | [[artifact-changelog\|changelog + tag]] | Addy · gstack | Human-readable release record + semver bump and git tag. |
| Release | [[artifact-launch-checklist\|launch checklist]] | Addy · CE | Pre-launch go/no-go gate: checks, flags, rollout, rollback, monitoring. |
| Release | [[artifact-diataxis-docs\|Diataxis docs]] | gstack | Docs organized by the four Diataxis quadrants, tracked against a coverage map. |
| Learn | [[artifact-solution-doc\|solution doc]] | Compound Engineering | Machine-consumable reusable lesson future agents pull in automatically. |
| Learn | [[artifact-explainer\|explainer]] | Compound Engineering | Dense visual explainer — the human-facing learning counterpart. |
| Learn | [[artifact-retrospective\|retrospective]] | gstack · BMAD | Human/team-facing learning report: what went well/badly, action items. |
| Learn | [[artifact-skill-doc\|skill doc]] | Superpowers · gstack | Executable process knowledge (`SKILL.md`) that grows the capability library. |
| Learn | [[artifact-handoff-doc\|handoff doc]] | Matt Pocock | Compacted conversation summary so a fresh session can resume without re-deriving context. |

## See also

- [SDLC Stages — Index](../sdlc-stage/index.md) — the eight-stage lifecycle these artifacts flow through.
- [CONVENTIONS.md](../CONVENTIONS.md) — the ontology: how `produces:` links capabilities to these artifacts.
- [Knowledge Base Index](../index.md) — all five namespaces.
