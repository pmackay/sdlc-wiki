# Source capture — Tessl: Context-Driven Factories

- URLs: https://tessl.io/blog/context-driven-factories (blog post); https://docs.tessl.io/automations/overview , https://docs.tessl.io/automations/overview/overview (Schedules), https://docs.tessl.io/automations/overview/overview/example-schedules/use-case-review-miner (docs, fetched as Markdown via the `.md` suffix)
- Collected: 2026-10-24
- Published: 2026-09-15 (blog post, `datePublished` in page metadata); docs pages unversioned, captured as of 2026-10-24
- Author: Dru Knox, Head of Product & Design, Tessl
- Type: registry re-ingest source (Tessl's factory thesis and its repo-defined automation surface)
- Scope of capture: the post body verbatim (navigation, promo banner, author bio, and related-post links removed; image placeholders marked `[diagram]`); transcriptions of the post's six diagrams; three docs pages that document the `tessl.json` automation surface the post relies on, verbatim with GitBook's appended agent-query boilerplate removed. The post's diagrams show a `triggers` block in `tessl.json` (Linear and GitHub events); the captured docs document `schedules` and `actions` blocks only, and no trigger reference page was found in the docs index on 2026-10-24.

## Blog post (verbatim)

Dru Knox, "Context-Driven Factories", Tessl blog, 15 Sept 2026.

Software factories are the frontier of agentic software development. They promise a compounding development process that gets cheaper, faster, and better every week. But most teams struggle to build factories that deliver these compounding outcomes. Their buildout stalls, or the gains are merely incremental.

We have seen this pattern before. When coding agents first arrived, it was suddenly easy to crank out features, and just as easy to end up with slop. The teams that got real value learned to separate planning from implementation and to write down the context an agent needed before letting it build. Factories are following the same path. The tempting move is to dive straight into automation, but we regularly see this fail for three reasons:

- Workflows defined in code are brittle and cannot improve as stronger models ship.

- Knowledge is siloed and improvements in one workflow don't benefit others.

- Tooling comes before process design, so the team never buys in.

Our answer is context-driven factories, a method centered on defining your team’s workflows and standards in plain files that run on simple, transparent infra. This post describes what that looks like, why the common alternative struggles, and how to start.

## Context-driven factories in action

A context-driven factory has two principles designed to keep decision-making out of code, let knowledge flow across tools, and make business context easy to collaborate on across the team.

Workflow definition lives in context, not code. The agent reads a description of the job and what good looks like, has the tools it needs, and decides what to do next. Code is still present, as scripts, CLIs, and MCP tools the agent can call, but it does not sit in the outer loop deciding how the agent progresses through the task or what it is allowed to see.

Every workflow and standard lives in a plugin. Those plugins are checked into your repos and shared between projects with a context registry. Read a plugin and you know how the factory works. Change a plugin and you have changed the factory.

Once your team starts capturing their workflows and standards in skills, you automate them with loops. A loop is a skill you have deployed to run automatically, one that improves over time as it runs. A factory composes skills and loops into a full agentic SDLC. This path has become a mantra at Tessl: from skills, to loops, to factory.

Context-driven factories make this journey easier for two reasons. Plain context files are easy for an agent to read and change safely, so the self-improvement step is tractable and loops can run with more autonomy. And because context is portable and reused across surfaces, loops collect signal from everywhere a skill is used and distribute improvements equally broadly.

Below, we show a context-driven factory across the three main factory surfaces:

- Ticket to PR flows

- Agentic code review

- General automations

### From ticket to PR

Implementing a ticket is an ambiguous task that requires a large amount of judgment. A feature may touch one repo or three. A large change may be better shipped as a couple of stacked PRs. A copy fix should skip the heavyweight review. Engineers absorb these variations without thinking about them, and a factory has to model the same ambiguity.

[diagram]

In a context-driven factory, the ticket-to-PR workflow is a set of skills:

[diagram]

When someone delegates an issue to the factory, there is no extra logic or magic routing. An agent starts with the triage-issue skill loaded. The skill describes how this team triages: what to look at, what questions to answer, and which sibling skills to move to next. Once a PR exists, pr-shepherd takes over in the same shape: resolve CI, address review, merge when the criteria are met. When exceptions arise, the agent can handle them gracefully.

### Code review

Good code review makes all your engineers better. Review is where a team's standards get applied most sharply, and if those learnings don’t disseminate across your SDLC, your factory will never compound.

[diagram]

In a context-driven factory, this sharing is the default, since your code review standards live in skills that can be reused elsewhere. Add a code-review plugin and point the review entry point at it.

[diagram]

Note that the design system, brand guidelines, and company brain are not in the repo. They are dependencies, resolved from the Tessl registry. Design owns the design system and publishes it. Every project that needs it declares a dependency and gets the current version.

When review keeps flagging a spacing pattern and the design system's guidance gets fixed, the next implementation gets it right the first time. Review improved generation without anyone wiring the two together, because they were reading the same file all along. This is a loop in its simplest form: a skill that gets better every time it runs, with the improvement landing everywhere the skill is used.

### Automations

Some work runs on a schedule or trigger outside of the ticket-to-PR flow:

[diagram]

A schedules entry in tessl.json turns a plugin into a loop. Anyone can open the skill to see how a changelog gets written or what counts as a flaky test. Anyone can propose a workflow change in a pull request, and the team can debate it there before it is enforced. The process belongs to the team and is easy to review as a team.

### Simple, transparent infrastructure

Context-driven factories require less infrastructure, since most of the work is an exercise in creating and improving plugins. The infrastructure that remains (sandboxes, secrets, the scheduler, etc.) is invisible, because it carries no logic.

Put it together and the whole factory is a few plugins, versioned in git or tracked as dependencies from your context registry. Because the factory is driven by skills, it’s easy to change without “breaking the factory”. Because every loop is just a skill in the repo, it’s easy for the factory to optimise itself as it runs. And because skills are portable, what one loop learns is reused by every other loop that uses those skills.

[diagram]

## How most people build factories, and why they fail

Most factories start from a different instinct. Engineers reach for code first, because code is what we know and it feels like the predictable choice. The bias is toward building fast and getting something working, so the slower work of writing the process down and agreeing on it with the team gets skipped. Each of the three failures below traces back to that.

### Workflows defined in code are brittle

Every workflow has ambiguity. Any rule enshrined in deterministic code turns out to have exceptions, and code handles them badly. Worse, guardrails that were prudent for one model generation become an invisible straitjacket for the next, and nobody goes back to remove scaffolding that is not visibly failing.

The ticket-to-PR flow shows both problems. It almost always gets modelled as a pipeline with code at the core. Code pulls the repo and runs setup. An agent is handed the task, often tightly locked down in what it can access and do. Code pushes the PR. Webhooks fire specific agent tasks: fix CI, respond to review. After some gate, code merges the branch.

But this pipeline quickly becomes a mess of exceptions and special cases. Big features touch multiple repos. One ticket needs stacked PRs. A trivial copy change deserves a lighter review. Each one becomes a branch in the pipeline, and the pipeline hardens around whatever the models could do when it was written.

Context-driven factories default to adaptability. The agent reads the process and exercises judgment, and it gets efficiency and determinism from the tools it calls rather than from a pipeline deciding on its behalf. Context drives the work and tools are helpers, as they are for humans, not the other way around.

### Knowledge is siloed

Today's SDLC works because the engineer who reviews a PR brings that same knowledge to their own development. Agents break that flow, since a different agent picks up every task and is gone when it finishes. Tools with memory features help, but they hold their learning in private state. A review tool that has learned your preferences reviews better, but your PRs do not arrive any cleaner.

Those shared learnings are the flywheel a factory has to produce, and the payoff is large. When review learnings feed back into generation, PRs arrive correct the first time. That means fewer implementation rounds and cheaper, lighter review. The same standards can then power maintenance agents that sweep the codebase on a schedule and catch the drift that slips through any individual PR. Teams that do not close this loop face a hard future: engineers burning out under the volume of agent PRs, or falling behind competitors who have made this process compound.

Context-driven factories solve this by keeping standards in plugins that every surface reads. Review, generation, and maintenance agents draw on the same files, so learnings in one place cascade everywhere automatically.

### Tooling comes before process design, preventing team buy-in

Nearly every factory buildout starts with infra and tools. Wiring a few things together and watching workflows run feels like a superpower. But this approach scatters decisions and business context across tools, trapped in configuration screens, or hidden in glue code only half the team understands. There is nowhere to lay it out so the team can say yes, this is how we do this.

We learned this lesson on our own GTM team. Someone built a set of automations that crawled customer calls, generated insights, and fed them into a chain of other tools to drive prioritisation. Nobody knew exactly how the insights were generated, so whenever people disagreed they dismissed the process. The impact was limited because the team had never been brought on board. When we decided to rework the process, the policy lived in a scatter of prompt text boxes that were hard to collaborate on, and other automations relied on its output, so we were migrating a pipeline rather than editing a document.

We corrected this by rebuilding it as a context-driven automation. The policy moved into a skill in the repo, where anyone can read it and propose a change in a pull request, and the pipeline shrank to a scheduler around that file. Disagreements now improve the skill instead of discrediting the process.

## Skills, to loops, to factory

Everything above comes down to structure: workflows and standards written down as plugins, shared across every tool, and agreed on by the team before they are enforced. With that structure in mind, the remaining question is how to get started. Our answer is the mantra “skills, to loops, to factory.”

Do not try to build everything at once. Start with one or two workflows. Write the process and the standards down as skills, run them by hand, and adjust until the team trusts the output. Your team is probably already doing this, you just need to curate the good skills lying around. Then close the loop on that workflow and let it run and evolve. Expand from there as your processes evolve to be more agent-native.

Context-driven factories make this natural. The skill you run by hand is a single click to deploy. But automation is the payoff at the end of the effort, not the starting point. The durable value in a factory is a legible, versioned, portable record of how your organization builds software, one that gets a little better every time the factory runs.

## Diagram transcriptions (from the post's images; layout described, text verbatim)

1. **"Flexible SDLC"** — one `ticket` branching into three paths: `edit → merge` labelled *Copy fix*; `triage → implement → review → merge` labelled *Scoped feature*; `triage → decompose → (repo a · repo b · repo c) → PR 1 → PR 2 (stacked) → merge` labelled *Migration*.
2. **"repo"** — `repo/` containing:
   - `tessl.json`:
     ```json
     {
       "triggers": {
         "issue-delegated": {
           "on": "linear:issue.delegated",
           "skill": "triage-issue"
         },
         "pr-opened": {
           "on": "github:pull_request.opened",
           "skill": "triage-pr"
         }
       }
     }
     ```
   - `factory/issue-handling/` → `skills/`: `triage-issue` (marked TRIGGER), `decompose-ticket`, `implement-frontend-change`, `add-service`, `…`; plus `scripts/`, `hooks/`, `mcp.json`.
   - `factory/pr-shepherd/` → `skills/`: `triage-pr` (marked TRIGGER), `resolve-ci-failures`, `address-review-feedback`, `merge-when-ready`.
3. **"code-review"** — a central `code-review` skill connected both ways to `code-standards`, `design-system`, `triage-issue`, `implement-change`, `nightly-maintenance`, `brand-guidelines`. Legend: *"Standards and insights from review flow out to every skill"* (solid) · *"As skills run, improvements flow back into review"* (dashed).
4. **"code review config"** — `repo/tessl.json`:
   ```json
   {
     "dependencies": {
       "@design/design-system": "^3",
       "@brand/brand-guidelines": "^2",
       "@ops/company-brain": "^1"
     },
     "triggers": {
       "issue-delegated": { … },
       "pr-opened": { … },
       "pr-ready-for-review": {
         "on": "github:pull_request.ready_for_review",
         "skill": "review-pr"
       }
     }
   }
   ```
   `factory/code-review/` → `skills/`: `review-pr` (TRIGGER), `check-accessibility`, `check-design-composition`, `…`; `hooks/`, `scripts/`. A separate panel, **"Tessl registry — NOT IN REPO"**: `@design/design-system` (Owned by Design · ^3), `@brand/brand-guidelines` (Owned by Brand · ^2), `@ops/company-brain` (Owned by Ops · ^1).
5. **"schedules config"** — `factory/automations/docs-update/`: `tessl.json` with `"schedules": { "weekly-changelog": { … }, "flaky-test-hunt": { … }, "docs-update": { "cron": "0 7 * * MON", "skill": "update-docs" } }`; `skills/`: `update-docs` (SCHEDULE), `read-notion-specs`, `read-linear-issues`, `write-docs`; `mcp.json` servers: `notion`, `linear`.
6. **"full picture"** — `repo/` with `src/`, `tessl.json` (TRIGGERS · SCHEDULES · DEPENDENCIES), `factory/` (PLUGINS · SKILLS) containing `issue-handling/`, `pr-shepherd/`, `code-review/`, `automations/` (SCHEDULES: `weekly-changelog/`, `flaky-test-hunt/`, `docs-update/`). Below, a dashed box **"SIMPLE, TRANSPARENT INFRA"**: `sandboxes` · `secrets` · `webhooks` · `scheduler`.

## Documentation pages (verbatim)

#### Automations overview

Automate recurring work by declaring schedules in your tessl.json and pushing them to your default branch.

Automations run plugins on a schedule so recurring work happens without CI or GitHub Actions configuration.

##### Define an automation in tessl.json

The primary way to create an automation is to declare a schedule in your project's `tessl.json`. Add a `schedules` block and push it to your default branch. Tessl syncs the manifest and creates the schedule when it can resolve the project and apply the entry. The schedule lives next to the code it runs against, so it is reviewed and version-controlled like any other change.

See [Schedules](/automations/overview/overview.md) for prerequisites, the `schedules` block reference, validation, and schedule behavior.

##### Example schedules

{% content-ref url="/pages/jqRZh2ForMPs2Jpj4zox" %}
[Example Schedules](/automations/overview/overview/example-schedules.md)
{% endcontent-ref %}

#### Schedules

No CI setup, no GitHub Actions config. Declare a schedule in your tessl.json, push to your default branch, and Tessl runs it for you.

{% hint style="info" %}
**Takeaways:**

* A schedule runs a plugin against a repo on a cron, with no CI or GitHub Actions config needed.
* The primary way to create one is a `schedules` block in your `tessl.json`. Push to your default branch and Tessl syncs it.
* An unparseable or invalid file never deletes anything. Removing a schedule from a valid file is what deletes it.
* Run `tessl schedule validate` before you push to catch errors locally.
* When repo-defined schedules are enabled for your organization, they are read-only in the web app and CLI. Change the file to change them.
  {% endhint %}

##### What is a schedule?

A schedule runs a plugin on a cron. You pick a plugin, a repo, and a time, and Tessl runs the plugin against that repo on that schedule. Each time the schedule fires, Tessl starts a cloud run and reports the result back so you can see what happened.

Tessl skips a tick if the previous run from the same schedule is still active when the next one would start. There is no queue: a skipped tick does not run later.

Think of it as two parts working together. The **plugin** describes the task: it tells the agent what to do. The **schedule** describes the timing: it tells Tessl when to do it.

##### What you need first

* A Tessl account with a workspace.
* GitHub connected to your workspace. See [Connect Tessl to GitHub](/distribute/connect-tessl-to-github.md).
* A plugin that describes the task. See [Create a plugin](/creating-skills-and-plugins/create-a-plugin.md).
* An environment, if the plugin needs secrets or has to push to your repo. Without one, a run gets a read-only GitHub token, which can check out your repo but can't open PRs. See [Environments](/automations/environments.md).

##### Define a schedule in tessl.json

The primary way to create a schedule is to declare it in your project's `tessl.json`. Add a `schedules` block, push it to your default branch, and Tessl reads the file and creates the schedule for you. The schedule lives next to the code it runs against, so it is reviewed and version-controlled like any other change.

The `name` field helps Tessl resolve the manifest to a project. Use the `workspace/project` format, for example `"name": "my-org/my-app"`. Before schedules sync, an active project must exist in that workspace, be connected to the same GitHub repository, and use the manifest's directory as its repository subpath. The GitHub App installation must currently have access to the workspace. When Tessl resolves that binding, schedules from the manifest appear under the project's **Schedules** tab in the web app. Schedule sync does not create or reassign projects.

Tessl discovers and syncs each `tessl.json` in a repository independently. In a monorepo, a manifest such as `apps/backend/tessl.json` manages only its own schedules, without affecting the root or sibling manifests. Deleting that subdirectory manifest removes only the schedules managed by that manifest in workspaces that the GitHub App installation can still access. Schedules in workspaces it can no longer access are not reconciled by that deletion.

###### Let the schedule-setup skill do it for you

If you'd rather describe the schedule in plain language than write the JSON yourself, install [tessl/schedule-setup](https://tessl.io/registry/tessl/schedule-setup).

When invoking the skill, tell your agent what you want to run and when ("run the docs audit every Monday at 9am London time using the production environment"). The skill asks clarifying questions one at a time, picks the most readable schedule format, writes and validates the entry, and explains what happens on push. It can also author a new repo-local skill for your schedule to use if you don't have one yet.

###### The schedules block

`schedules` is a map from each entry's name to the entry. The name is the entry's stable identity: a lowercase kebab-case slug, not a display label. See [Behaviors to know](#behaviors-to-know) for what renaming an entry does.

Each entry names what it runs with `action` and when it runs with one timing field. Use either `cron` or its alias, `schedule`, but not both. Beside `action`, an entry carries only its timing and its description:

| Field         | Required   | What it is                                                                                                                        |
| ------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `action`      | Yes        | What the schedule runs: an inline action, the name of an action declared in the `actions` block, or that name with overrides.     |
| `cron`        | One of two | A five-field cron expression, supported shorthand, or structured schedule object. The minimum interval between runs is 5 minutes. |
| `schedule`    | One of two | Alias for `cron`. Use one timing field, not both.                                                                                 |
| `timezone`    | No         | IANA timezone the cron is interpreted in (for example `America/New_York`). Defaults to `UTC`.                                     |
| `description` | No         | A human-readable description of the schedule.                                                                                     |

An inline action takes these fields inside `action`. Setting any of them beside `action` is an error:

| Field          | Required | What it is                                                                                                                                                                                      |
| -------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `skill`        | Yes      | The plugin to run: a registry ref `workspace/plugin[@version][#skill]`, or a repo-local `file:path` relative to the directory of the project's `tessl.json`.                                    |
| `environment`  | No       | The workspace environment the run executes in, referenced by **name**. It supplies the GitHub token and any other secrets the plugin needs. Without one, the run gets a read-only GitHub token. |
| `baseBranch`   | No       | The branch each run checks out and opens PRs against. When omitted, each run uses the project's Loop default branch or the repository default.                                                  |
| `workdir`      | No       | A subdirectory of the repo the plugin runs in.                                                                                                                                                  |
| `agent`        | No       | Which agent runs the plugin (`claude-code` or `claude` (default), `cursor`, `codex`, `gemini`, `tessl` or `tessl-agent`).                                                                       |
| `model`        | No       | Which model the agent uses (e.g. `claude-sonnet-5-5` for `claude`, `auto` for `cursor`, `gpt-6.1-sol` for `codex`).                                                                             |
| `effort`       | No       | How hard the agent thinks: `minimal`, `low`, `medium`, `high`, `xhigh`, or `max`. When omitted, the agent uses its own default. A run whose agent doesn't offer that level doesn't start.       |
| `inputs`       | No       | Skill input values, as a map of string keys to string values.                                                                                                                                   |
| `instructions` | No       | Free-text directions appended to the plugin prompt for this schedule.                                                                                                                           |

To run the same action from more than one schedule, declare it once in the manifest's top-level `actions` block and name it from each entry. A declaration takes the same fields as an inline action, and its name follows the same rule as a schedule entry's name: a lowercase kebab-case slug. `"action": "pr-report"` runs the declared action as written. `"action": { "use": "pr-report", ... }` runs it with overrides: each field you give replaces the declared one, `null` removes any field except `skill`, and `inputs` merges by input name, so an input you set to `null` is removed and `"inputs": null` removes them all.

```json
{
  "actions": {
    "pr-report": { "skill": "file:tiles/pr-report", "environment": "reports" }
  },
  "schedules": {
    "pr-report-nightly": { "action": "pr-report", "cron": "0 2 * * *" },
    "pr-report-weekly": {
      "action": { "use": "pr-report", "instructions": "Cover the last 7 days." },
      "cron": "0 4 * * 1"
    }
  }
}
```

You may also see entries in the flat form, which writes the action's fields directly beside the timing, with no `action`. A flat entry still runs, as the inline action its fields describe. It needs both `skill` and `environment`, and it can't set `effort`. To convert one, move its action's fields into `action`; it stays the same schedule with the same run history.

Raw cron expressions have five fields: minute, hour, day of month, month, and day of week. `0 9 * * 5` means "at 9:00 on every Friday". `0 8 * * *` means "at 8:00 every day".

You can also use these shorthand strings:

* `hourly`
* `daily at HH:MM`
* `weekdays at HH:MM`
* `weekly on DAY at HH:MM`
* `monthly on Nth at HH:MM`
* `every N minutes` or `every N hours`, when `N` divides evenly into 60 or 24
* `every N minutes between HH:MM-HH:MM`; the start is inclusive and the end is exclusive, and multi-hour windows use whole-hour endpoints
* `every N minutes on weekdays`

For schedules that don't fit those patterns, use an object with `minute`, `hour`, `day`, `month`, and `weekday` fields. Omitted fields mean every value. Numeric fields accept a number, a list of numbers, `{ "every": N }`, or `{ "between": [N, M] }`. `month` and `weekday` also accept names or lists of names.

```json
{
  "cron": {
    "minute": { "every": 15 },
    "hour": { "between": [9, 17] },
    "weekday": ["mon", "tue", "wed", "thu", "fri"]
  }
}
```

Tessl compiles shorthand strings and objects to cron before validation and storage. The timezone and 5-minute minimum apply to every input form.

###### A complete example

```json
{
  "name": "my-org/my-repo",
  "schedules": {
    "weekly-changelog": {
      "action": {
        "skill": "tessl/changelog-writer",
        "environment": "production"
      },
      "schedule": "weekly on friday at 09:00",
      "timezone": "America/New_York",
      "description": "Draft the weekly changelog every Friday morning."
    },
    "api-docs-audit": {
      "action": {
        "skill": "tessl/docs-audit",
        "environment": "production",
        "instructions": "Focus on the API reference section only."
      },
      "cron": "weekly on monday at 08:00"
    }
  }
}
```

This declares two schedules. `weekly-changelog` runs the `changelog-writer` plugin every Friday at 9:00 New York time. `api-docs-audit` runs the `docs-audit` plugin every Monday at 8:00 UTC, steered at the API reference by the `instructions` in its action.

###### Behaviors to know

A schedule's identity is its entry's name. Renaming an entry with an inline action is therefore a delete and a create, not an update. For example, changing `nightly-scan` to `nightly-check` deletes the old schedule and creates a new schedule with the new name. Prior launch runs are preserved but are no longer linked to a schedule. If the new entry fails validation, neither the deletion nor the creation is applied.

Entries that name the same declared action show up in the web app and CLI as one schedule, named after the action. That schedule lists each entry's timing and keeps one run history for all of them, so renaming one of those entries keeps its runs where they are. Moving an entry from an inline action to a declared one, or back, or renaming the declared action, moves the entry to a different schedule, and its earlier runs don't carry over.

The `schedules` block is the source of truth. Removing the block from `tessl.json`, or setting it to `{}`, means “no schedules” and deletes all schedules managed by that manifest. To recover from an accidental removal, revert the commit and push again.

###### Validate before you push

Run `tessl schedule validate` before you push to catch errors locally. You can also [run the validator in your CI workflow](/automations/overview/overview/validate-in-ci.md):

```bash
tessl schedule validate
```

It reads your `tessl.json`, checks the `schedules` block and the `actions` block, and reports every problem against the schedule entry or action it belongs to. It exits non-zero when it finds a problem, so it also works as a CI check. A file with neither block is valid, and a file with no `schedules` block is valid as long as its `actions` block is.

On its own, `validate` checks the file: its shape, its cron expressions, the minimum interval, that every action a schedule names is declared, that each declaration in the `actions` block is valid, and that each repo-local `file:` skill a schedule runs exists in your working tree. It reports an `actions` problem against the action, as in `actions.pr-report`, so you can tell it from a schedule entry.

When you're signed in and the manifest's `name` identifies a project, `validate` also runs the checks Tessl applies when the file syncs and when a run starts: that the plugin resolves and its inputs match, that the named environment exists and can give the run a GitHub token, that your organization can use the agent, model, and effort, and that the workspace has room for the schedules. Otherwise it tells you these checks were skipped.

##### How the sync works

When you push to your default branch, Tessl reads `tessl.json` at the pushed commit and reconciles the schedules of the project its `name` identifies:

* An entry with an inline action is its own schedule. Adding the entry **creates** the schedule, changing it **updates** the schedule, and removing it **deletes** the schedule.
* An entry that names a declared action adds its timing to that action's schedule. Adding, changing or removing the entry **updates** the action's schedule, which stays as long as the `actions` block declares the action.

Tessl applies the `schedules` block as a whole. If any entry fails validation, names an action the `actions` block doesn't declare, or points at a repo-local skill missing from the pushed commit, or if the block would take the workspace over its limit on active schedules, none of the block's changes apply and every schedule stays as it was. Tessl checks the environment, plugin, agent, and model each time a run starts: if one is missing or unavailable, that run doesn't start, Tessl records why on the schedule, and the schedule stays active for its next run.

Tessl reads the `name` field, the `schedules` block, and the `actions` block. A schedule that names a declared action picks up a change to that action on the next push, even when the push changes only the `actions` block. Changes to other parts of `tessl.json` don't change your schedules. Most pushes that don't touch `tessl.json` are ignored. A force push, branch creation, or push with an empty or truncated commit list bypasses that optimization, and Tessl reads the manifest at the pushed revision.

The sync runs off the default branch only. A schedule declared on a feature branch does not sync until the change reaches your default branch.

##### The safety model

Tessl never deletes a schedule because it could not understand your file. Deletion only ever follows from a file it read cleanly.

* **Unparseable or invalid: nothing changes.** If the file is malformed JSON or cannot be read, Tessl makes no changes at all. If the `schedules` block fails validation, every schedule stays exactly as it is. If the `actions` block fails validation, the declared actions stay as they are, and so does every schedule that names one; schedules with an inline action still sync. A typo in either block doesn't delete your schedules. Fix the file and push again.
* **Valid and read cleanly: the file wins.** Once Tessl reads a valid file, the file is the source of truth. Remove an entry with an inline action and its schedule is deleted. Remove an entry that names a declared action and only its timing is removed from the action's schedule. Remove the whole `schedules` block, or delete a `tessl.json`, and every repo-defined schedule managed by that manifest is deleted.

So the only way to delete a repo-defined schedule is to remove it from a valid file and push. An error in the file is always safe.

##### Read-only in the web app and CLI

When repo-defined schedules are enabled for your organization, a schedule defined in `tessl.json` is read-only from the web app and the CLI. Attempts to edit, pause, resume, or delete it through those surfaces return an error telling you it is defined in `tessl.json`. To change it, change the file and push.

You can still watch a repo-defined schedule and its runs in the web app and CLI. Only mutations are blocked.

A repo-defined schedule reflects the last push whose `schedules` block Tessl applied. While a later push's block is refused, each schedule keeps its previous configuration and keeps running.

##### Create from the CLI or web app (alternative)

You can also create a schedule directly from the CLI or the web app, without a `tessl.json` block. This is the older path and is not version-controlled. It may be disabled for some users.

{% tabs %}
{% tab title="CLI" %}
Use `tessl schedule create`. Pass the plugin as the first argument, then the repo, the cron, and the environment:

```bash
tessl schedule create tessl/changelog-writer \
  --project engteam/my-repo \
  --repo my-org/my-repo \
  --cron "0 9 * * 5" \
  --environment production
```

This runs the `changelog-writer` plugin against `my-org/my-repo` every Friday at 9:00 UTC.

Common flags:

| Flag             | What it does                                                                                                                                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--project`      | The Tessl project that owns the schedule, as `workspace/name`, a name in the linked workspace, or an ID. Required unless the current directory is linked to a Tessl project. `--project-id` also works.                      |
| `--repo`         | The repository the plugin runs against. Required, and it must be the selected project's repository.                                                                                                                          |
| `--cron`         | When the schedule fires, as a cron expression. Required.                                                                                                                                                                     |
| `--environment`  | The environment the run executes in. It supplies the GitHub token and any other secrets or API keys the plugin needs. The project must be bound to it. Required when you specify the plugin, repo, and environment directly. |
| `--timezone`     | The timezone for the cron expression. Optional; defaults to UTC.                                                                                                                                                             |
| `--agent`        | Which agent runs the plugin (for example `claude-code`, `cursor`, `codex`, `gemini`, or `tessl-agent`). Optional.                                                                                                            |
| `--model`        | Which model the agent uses. Optional.                                                                                                                                                                                        |
| `--instructions` | Extra directions layered on top of the plugin for this schedule. Optional.                                                                                                                                                   |
| `--base-branch`  | The branch to check out and open PRs against. Optional.                                                                                                                                                                      |

With `--environment`, the schedule runs in the project's workspace. Passing `--workspace` instead of `--project` uses that workspace's only project; when the workspace has none or several, pass `--project`. `--workspace` still chooses the workspace for a schedule created with `--from-run`.

The cron expression has five fields: minute, hour, day of month, month, and day of week. `0 9 * * 5` means "at 9:00 UTC on every Friday". `0 8 * * *` means "at 8:00 UTC every day".

Use `--instructions` to point a generic plugin at a specific job:

```bash
tessl schedule create tessl/docs-audit \
  --project engteam/my-repo \
  --repo my-org/my-repo \
  --cron "0 8 * * *" \
  --environment production \
  --instructions "Focus on the API reference section only"
```

{% endtab %}

{% tab title="Web app" %}
Open **Projects > \[project] > Schedules** and choose **Create schedule**. The form asks for the project, schedule (cron), name, description, and environment. These are the primary fields.

Below the environment and mode selection is an **Advanced options** control. Expand it to set the agent, model, inputs, instructions, and base branch. Leave it collapsed to accept the defaults.
{% endtab %}
{% endtabs %}

##### How instructions work

The `instructions` field layers extra directions on top of whatever the plugin already says. The plugin is the base recipe; instructions are the per-schedule customization. The plugin still runs its normal task. The instructions steer it for this one schedule.

This lets you reuse one plugin for several jobs. The same `docs-audit` plugin, pointed two ways in one `schedules` block:

```json
{
  "schedules": {
    "audit-api-reference": {
      "action": {
        "skill": "tessl/docs-audit",
        "environment": "production",
        "instructions": "Focus on the API reference section only."
      },
      "cron": "0 8 * * 1"
    },
    "audit-getting-started": {
      "action": {
        "skill": "tessl/docs-audit",
        "environment": "production",
        "instructions": "Focus on the getting-started guide and its code samples."
      },
      "cron": "0 8 * * 3"
    }
  }
}
```

Same plugin, two schedules, two different jobs.

##### Monitoring your runs

Each schedule keeps a table of its past runs. Open a schedule in the web app to see its full run history, including output and duration. From the CLI, `tessl schedule runs <id>` lists runs with their ID, status, skill, repo, workspace, creator, and creation time.

| Status       | What it means                                                | What to do                   |
| ------------ | ------------------------------------------------------------ | ---------------------------- |
| In Progress  | Still running                                                | Wait                         |
| Completed    | The skill finished and reported a result                     | Nothing. Check the output.   |
| Agent failed | The skill reported that it could not complete the task       | Check the output for why     |
| Error        | The platform failed, or the run ended without a skill result | Check the run's error detail |
| Cancelled    | Someone stopped the run                                      | Nothing                      |

##### Next steps

* [Environments](/automations/environments.md)
* [Connect Tessl to GitHub](/distribute/connect-tessl-to-github.md)
* [Create a plugin](/creating-skills-and-plugins/create-a-plugin.md)
* [Keep docs in sync](/automations/overview/overview/example-schedules/use-case-docs-audit.md)
* [Weekly changelog](/automations/overview/overview/example-schedules/use-case-changelog.md)
* [Review pattern mining](/automations/overview/overview/example-schedules/use-case-review-miner.md)
* [Test health monitor](/automations/overview/overview/example-schedules/use-case-test-health.md)
* [Release readiness check](/automations/overview/overview/example-schedules/use-case-release-check.md)

#### Review pattern mining

Stop repeating the same code-review comment. A scheduled review miner reads recent reviews, finds the feedback that keeps coming up, and proposes a lint rule for it.

{% hint style="info" %}
**Goal:** Stop reviewers repeating the same comment by turning it into a rule.
{% endhint %}

##### What it does

Weekly, a schedule reads the last 50 code reviews and looks for feedback that keeps coming up. If reviewers keep saying the same thing, the plugin proposes a lint rule, an automated check, or a documented convention to address it. Reviewers spend less time repeating the same comment and more time on the decisions that need their judgment.

##### The plugin

[`tessl/review-miner`](https://tessl.io/registry/tessl/review-miner) reads recent review comments, groups the recurring ones, and proposes a rule, check, or convention for each. Install it with:

```bash
tessl install tessl/review-miner
```

##### Define the schedule

Run it every Monday at 9:00 UTC. Add this entry to the `schedules` block in your project's `tessl.json`, and keep any other entries already in that block. Replace `production` with the name of your environment (see the [Schedules overview](/automations/overview/overview.md) for the prerequisites).

{% stepper %}
{% step %}
**Add the schedule entry**

```json
{
  "schedules": {
    "review-miner": {
      "action": {
        "skill": "tessl/review-miner",
        "environment": "production"
      },
      "schedule": "weekly on monday at 09:00"
    }
  }
}
```

{% endstep %}

{% step %}
**Validate and push**

Signed out, validation checks the local file only. Signed in, with a `name` that identifies your project, it also runs the checks Tessl applies when the file syncs and when a run starts. Commit and push the change, then confirm Tessl applied the schedule in your workspace before checking its run history.

```bash
tessl schedule validate
git add tessl.json
git commit -m "chore(docs): add review miner schedule"
git push
```

{% endstep %}

{% step %}
**Check the runs**

Open the schedule in the web app, or run `tessl schedule runs <id>` to see its run history.
{% endstep %}
{% endstepper %}

##### Customize with instructions

Focus the search on one area by adding `instructions` inside the same entry's `action`. Keep all other entries in the `schedules` block:

```json
{
  "schedules": {
    "review-miner": {
      "action": {
        "skill": "tessl/review-miner",
        "environment": "production",
        "instructions": "Only look for repeated feedback about error handling and logging"
      },
      "schedule": "weekly on monday at 09:00"
    }
  }
}
```

##### Create your own

Want a different behavior? [Create your own plugin](/creating-skills-and-plugins/create-a-plugin.md) that reads recent review comments and proposes a rule your way.

