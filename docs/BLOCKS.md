# Block manifest

The mission of this set: the reading experience must never feel like hell.

One row for each block in this set. Change this file first when the set changes. The rule register in `docs/RULES.md` stays the authoring source for every rule a block embeds.

## The set

| Block | Role | Activation |
|---|---|---|
| write-better | General prose floor: reader levels, depth, sentence rules, AI patterns, reader load. | Auto, on any prose task. |
| write-compact | The whole reply stays short. | Auto, or "brief mode". |
| write-tldr | A short block at the end of a long answer: TLDR plus Found. | Auto, past 30 lines or on request. |
| write-again | Rewrite the last output, explain again, or refresh a stale doc. | Auto, on "again" or "wait what". |
| help-write | Read the conversation, name the skill that owns the deliverable. | On request, or when the type is unclear. |
| write-docs | Documents for humans, and documents an agent reads. | Auto, on document tasks. |
| write-pr | PR title and body from the change and the evidence. | Auto, on PR text. |
| write-commit | Commit message from the staged diff and the history. | Auto, on commit text. |
| write-comments | Code comments: intent, constraints, invariants, traps. | Auto, on comment edits. |
| write-review | Review comments on a diff: location, problem, fix. | Auto, on review requests. |
| write-jira | Jira epics, stories, and story points from a plan. | Auto, on Jira text. |
| write-issue | GitHub issues and bug reports with reproduction steps. | Auto, on issue text. |
| write-release | Release notes from git history. | Auto, on release text. |
| write-report | Reports for a decision-maker: answer first, evidence after. | Auto, on report requests. |
| write-summary | Summaries that keep decisions, numbers, and owners. | Auto, on summarize requests. |
| write-handoff | Handoff notes for a fresh session. | Auto, on handoff requests. |
| write-longform | Staged long-form mission under one shared brief. | Explicit request only. |
| write-glossary | Build or clean a glossary, one term per concept. | Auto, on glossary work. |
| write-plan | A plan before work starts: goal, approaches, steps, risks. | Auto, on plan requests. |
| write-adr | Architecture decision records in the Nygard shape. | Auto, on decision records. |
| write-prd | Product requirements: problem, goals, requirements, metrics. | Auto, on PRD requests. |
| write-ste | Enforce STE on any text, violations named by rule. | Auto, on "ste" requests. |

## Design rules

1. Each block works alone. A block never requires another block at run time, and never uses a term only another block defines.
2. A rule changes in the register first. Then it changes in every block that embeds it.
3. Every block auto-invokes. A description states trigger conditions only. It never summarizes the workflow.
4. Every block writes prose in Simplified Technical English and carries `references/ste.md`.
5. Every block reads local rule files first. Local rules beat skill defaults. See `shared/local-rules.md`.
6. Blocks that produce saved text write text only. They never run repository or tracker actions.
7. Name collisions with public skill registers were checked before release. Check again before any publish.

## Source lineage

The upstream projects and their licenses are listed in `THIRD_PARTY_NOTICES.md`.

## Held for a later version

- Marketing text modules.
- Language modules beyond English.
- Memory-file compression tools.

## Set size

Twenty-two descriptions load in every session. The negative-trigger routing test in `docs/ROUTING-TEST.md` is the regression net. It is pending for the 22-skill set. Run it before adding a twenty-third.
