# Set state, 2026-10-29

The one file that records what this set is. Update it in the same commit as any set change. The mission: the reading experience must never feel like hell.

## The skills (22)

| Skill | Role | Trigger | Lines | Example | Eval cases |
|---|---|---|---|---|---|
| write-better | Chat answers, explanations, notes | Auto, on any prose task | 172 | yes | 3 |
| write-compact | The whole reply stays short | Auto, or "brief mode" | 70 | no | 3 |
| write-tldr | Short block at the end of a long answer | Auto, past 30 lines | 60 | yes | 2 |
| write-again | Rewrite, explain again, refresh a stale doc | Auto, on "again" or "wait what" | 73 | yes | 2 |
| help-write | In-chat router to the right skill | On request | 72 | yes | 2 |
| write-docs | Docs for humans and for agents | Auto, on doc tasks | 116 | no | 3 |
| write-pr | PR title and body with evidence | Auto, on PR text | 120 | yes | 3 |
| write-commit | Commit message from diff and history | Auto, on commit text | 55 | yes | 3 |
| write-comments | Code comments: intent, constraints, traps | Auto, on comment edits | 61 | no | 2 |
| write-review | Review comments: location, problem, fix | Auto, on review requests | 58 | yes | 2 |
| write-jira | Jira epics, stories, points (Fibonacci) | Auto, on Jira text | 130 | yes | 3 |
| write-issue | GitHub issues with repro steps | Auto, on issue text | 68 | yes | 2 |
| write-release | Release notes from git history | Auto, on release text | 59 | yes | 2 |
| write-report | Reports: answer first, evidence after | Auto, on report requests | 82 | yes | 2 |
| write-summary | Summaries that keep decisions and owners | Auto, on summarize | 60 | yes | 2 |
| write-handoff | Handoff notes for a fresh session | Auto, on handoff | 62 | no | 2 |
| write-plan | Plans before work starts | Auto, on plan requests | 75 | yes | 2 |
| write-adr | Architecture decision records (Nygard) | Auto, on ADR requests | 103 | yes | 2 |
| write-prd | Product requirements with metrics | Auto, on PRD requests | 82 | yes | 2 |
| write-longform | Staged long-form mission | Explicit request | 99 | yes | 2 |
| write-glossary | One term per concept | Auto, on glossary work | 58 | yes | 2 |
| write-ste | Enforce STE, violations named by rule | Auto, on "ste" | 62 | yes | 2 |

Evidence notes: four behaviors carry graded run evidence in docs/EVALS.md. They are the pattern sweep, the PR and Jira templates, and the commit process rules. The other skills carry eval cases. Run them before claiming behavior.

## Shared machinery

- `shared/ste.md`: the Simplified Technical English rules. Synced into every skill as `references/ste.md`. Enforced by `tools/check.py`.
- `shared/local-rules.md`: the local-rules step. Synced into every skill as `references/local-rules.md`. Every skill reads AGENTS.md, CLAUDE.md, CONTRIBUTING.md, and GLOSSARY.md first. Local rules beat skill defaults.
- `<!-- sync:NAME -->` markers: the brief voice, the sentence floor, and the local-rules block exist once in source and one identical copy in every skill. The check fails on drift.
- `tools/check.py` + `tests/`: frontmatter, links, cross-references, sync regions, privacy blocklist, lint, noreply authors, sizes.
- `tools/blocklist.txt`: privacy guard. Allows the public handle, bans personal name parts and old names.

## Docs map

- `README.md`: the visitor page. Mission, skill table, three example pairs, install.
- `docs/BLOCKS.md`: the manifest and the set-size cap.
- `docs/RULES.md`: the rule register with stable IDs, A1 to B30.
- `docs/EVALS.md`: the behavior evidence and the routing-test method.
- `docs/AUDIT.md`: the 24-check rubric scores per skill.
- `docs/examples.md`: the before-and-after gallery.
- `docs/STATE.md`: this file.

## Release history

- 0.1.0 (2026-10-24): first eight skills on GitHub and skills.sh.
- 0.2.0: commit block pruned to process rules, thin-plan rule, evals for every block, trigger routing evidence 16 of 16.
- 0.2.1: Fibonacci story points with the effort, complexity, uncertainty model.
- 0.3.0: seven more skills (review, release, issue, summary, handoff, report, glossary), local-rules step in every skill, examples everywhere, 24-check audit.
- 0.3.1: rich styling rules in write-better, write-docs, write-pr.
- 0.4.1: store-front polish in the README, npm description and keywords.
- 0.4.0: seven new skills, write-core renamed to write-better, reader-load rules, docs/STATE.md.

## Published channels

- GitHub: github.com/adhamhaithameid/write-skills
- skills.sh: skills.sh/adhamhaithameid/write-skills
- npm: write-skills (0.3.0 live at the time of writing; publish 0.4.1 after `npm login`)

## Name check, 2026-10-29

skills.sh: write-tldr, write-again, help-write, write-adr, write-prd, write-ste, and write-better are free. write-plan exists under another owner (manastalukdar/ai-devstudio); kept, because installs are owner-namespaced.

## Open work

- Run the eval cases for the new skills and record verdicts in docs/EVALS.md.
- The full before-and-after experiment is in docs/EXPERIMENT.md: 13 clear passes, 9 thin passes, 0 failures over 22 skills.
- Keep the negative-trigger routing test green before adding a twenty-third skill.
- npm publish 0.4.1 (user, after npm login).
- Delete the old private repo github.com/adhamhaithameid/writing-skills (user).

## Held for later

- Marketing text modules, language modules beyond English, memory-file compression tools.
