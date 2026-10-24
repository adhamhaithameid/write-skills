# Block manifest

One row for each block in this set. Change this file first when the set changes. The rule register in `docs/RULES.md` stays the authoring source for every rule a block embeds.

## The set

| Block | Role | Activation |
|---|---|---|
| write-core | General prose floor: reader levels, depth, sentence rules, AI patterns. | Auto, on any prose task. |
| write-compact | Brief replies on request, or rebuild a reply that did not land. | Auto, or "brief mode". |
| write-docs | Documents for humans, and documents an agent reads. | Auto, on document tasks. |
| write-pr | PR title and body from the change and the evidence. | Auto, on PR text. |
| write-commit | Commit message from the staged diff and the history. | Auto, on commit text. |
| write-comments | Code comments: intent, constraints, invariants, traps. | Auto, on comment edits. |
| write-jira | Jira epics, stories, and story points from a plan. | Auto, on ticket text. |
| write-longform | Staged long-form mission under one shared brief. | Explicit request only. |

## Design rules

1. Each block works alone. A block never requires another block at run time.
2. A rule changes in the register first. Then it changes in every block that embeds it.
3. Every block auto-invokes. A description states trigger conditions only. It never summarizes the workflow.
4. Every block writes prose in Simplified Technical English and carries `references/ste.md`.
5. Blocks that produce saved text write text only. They never run repository or tracker actions.
6. Name collisions with public skill registers were checked before release. Check again before any publish.

## Source lineage

The upstream projects and their licenses are listed in `../THIRD_PARTY_NOTICES.md`.

## Held for a later version

- Marketing text modules.
- Language modules beyond English.
- Memory-file compression tools.
- Release notes from git history.
