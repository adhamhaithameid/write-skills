# Set state, 2026-11-07

The one file that records what this set is. Update it in the same commit as any set change. The mission: the reading experience must never feel like hell.

## The skills (22)

| Skill | Role | Trigger | Lines | Example | Eval cases |
|---|---|---|---|---|---|
| write-better | Chat answers, explanations, notes | Auto, on any prose task | 172 | yes | 4 |
| write-compact | The whole reply stays short | Auto, or "brief mode" | 69 | yes | 3 |
| write-tldr | Short block at the end of a long answer | Auto, past 30 lines | 59 | yes | 2 |
| write-again | Rewrite, explain again, refresh a stale doc | Auto, on "again" or "wait what" | 72 | yes | 2 |
| help-write | In-chat router to the right skill | On request | 71 | yes | 2 |
| write-docs | Docs for humans and for agents | Auto, on doc tasks | 122 | yes | 4 |
| write-pr | PR title and body with evidence | Auto, on PR text | 119 | yes | 3 |
| write-commit | Commit message from diff and history | Auto, on commit text | 55 | yes | 4 |
| write-comments | Code comments: intent, constraints, traps | Auto, on comment edits | 60 | yes | 2 |
| write-review | Review comments: location, problem, fix | Auto, on review requests | 58 | yes | 3 |
| write-jira | Jira epics, stories, points (Fibonacci) | Auto, on Jira text | 129 | yes | 3 |
| write-issue | GitHub issues with repro steps | Auto, on issue text | 67 | yes | 2 |
| write-release | Release notes from git history | Auto, on release text | 59 | yes | 3 |
| write-report | Reports: answer first, evidence after | Auto, on report requests | 81 | yes | 2 |
| write-summary | Summaries that keep decisions and owners | Auto, on summarize | 59 | yes | 2 |
| write-handoff | Handoff notes for a fresh session | Auto, on handoff | 86 | yes | 2 |
| write-plan | Plans before work starts | Auto, on plan requests | 75 | yes | 3 |
| write-adr | Architecture decision records (Nygard) | Auto, on ADR requests | 102 | yes | 2 |
| write-prd | Product requirements with metrics | Auto, on PRD requests | 81 | yes | 2 |
| write-longform | Staged long-form mission | Explicit request | 98 | yes | 2 |
| write-glossary | One term per concept | Auto, on glossary work | 58 | yes | 3 |
| write-ste | Enforce STE, violations named by rule | Auto, on "ste" | 63 | yes | 3 |

Line counts and the Example column reflect the files at the enforcement update (2026-11-16). Every skill carries an example, in the skill file, in `docs/examples.md`, or in both.

Evidence notes: four behaviors carry graded run evidence in docs/EVALS.md. They are the pattern sweep, the PR and Jira templates, and the commit process rules. The other skills carry eval cases. Run them before claiming behavior. The eight thin-pass additions carry probe evidence from 2026-11-16.

## Shared machinery

- `shared/ste.md`: the Simplified Technical English rules. Synced into every skill as `references/ste.md`. Enforced by `tools/check.py`.
- `shared/local-rules.md`: the local-rules step. Synced into every skill as `references/local-rules.md`. Every skill reads AGENTS.md, CLAUDE.md, CONTRIBUTING.md, and GLOSSARY.md first. Local rules beat skill defaults.
- `<!-- sync:NAME -->` markers: the brief voice, the sentence floor, and the local-rules block exist once in source and one identical copy in every skill. The check fails on drift.
- `tools/check.py` + `tests/`: frontmatter, links, cross-references, sync regions, privacy blocklist, lint, noreply authors, sizes. The lint enforces the mechanical STE rules: word and phrase bans, the 25-word cap (20 in numbered steps), passive voice, "-ing" verbs, contractions, dashes, curly quotes, and title case. A `<!-- ste:ok: reason -->` marker exempts one line.
- `tools/blocklist.txt`: privacy guard. Allows the public handle, bans personal name parts and old names.

## Docs map

- `README.md`: the visitor page. Mission, skill table, three example pairs, install.
- `docs/BLOCKS.md`: the manifest and the set-size cap.
- `docs/RULES.md`: the rule register with stable IDs, A to N, and the machine-check map.
- `docs/EVALS.md`: the behavior evidence and the routing-test results.
- `docs/AUDIT.md`: the 24-check rubric scores per skill.
- `docs/EXPERIMENT.md`: the full before-and-after run over all 22 skills.
- `docs/ROUTING-TEST.md`: the routing fixture with prompts and expected answers.
- `docs/examples.md`: the before-and-after gallery.
- `docs/STATE.md`: this file.

## Release history

- 0.1.0 (2026-10-24): first eight skills on GitHub and skills.sh.
- 0.2.0: commit block pruned to process rules, thin-plan rule, evals for every block, trigger routing evidence 16 of 16.
- 0.2.1: Fibonacci story points with the effort, complexity, uncertainty model.
- 0.3.0: seven more skills (review, release, issue, summary, handoff, report, glossary), local-rules step in every skill, examples everywhere, 24-check audit.
- 0.3.1: rich styling rules in write-better, write-docs, write-pr.
- 0.4.0 (2026-10-29): seven new skills, write-core renamed to write-better, reader-load rules, docs/STATE.md, routing fixture.
- 0.4.1 (2026-10-29): store-front polish, grouped skill table, badges, why section, npm description and keywords fix.
- Experiment (2026-10-30 to 31): all 22 skills before-and-after on the subagent channel. 14 clear passes, 8 thin passes, 0 failures. Full pairs in docs/EXPERIMENT.md.
- Routing test (2026-11-07): the 22-skill fixture ran with four fresh subagents. 38 of 40 verdicts correct; part B clean in both runs. Verdicts in docs/EVALS.md.
- Enforcement (2026-11-16): the lint gained the step cap, passive voice, and "-ing" verb checks. It also covers docs/EXPERIMENT.md. The reader-load rules moved from B23-B30 to N1 to N8.
- Thin passes (2026-11-16): the eight thin skills each gained their missing proven property. Probes for the new rules: 8 of 8 pass. Verdicts in docs/EVALS.md.

## Published channels

- GitHub: github.com/adhamhaithameid/write-skills
- skills.sh: skills.sh/adhamhaithameid/write-skills
- npm: write-skills (0.3.0 live at the time of writing; the npm token expired. Publish 0.4.1 after `npm login`.)

## Name check, 2026-10-29

skills.sh: write-tldr, write-again, help-write, write-adr, write-prd, write-ste, and write-better are free. write-plan exists under another owner (manastalukdar/ai-devstudio); kept, because installs are owner-namespaced.

## Open work

- npm publish 0.4.1 (user, after `npm login`; the token expired).
- Delete the old private repo github.com/adhamhaithameid/writing-skills (user).

## Done, for the record

- Eval evidence for all 22 skills: docs/EXPERIMENT.md, 14 clear passes, 8 thin passes, 0 failures.
- Routing test (2026-11-07): 38 of 40 verdicts correct, part B clean in both runs. Recorded in docs/EVALS.md and docs/ROUTING-TEST.md. The negative-trigger gate for a twenty-third skill is green.
- Addition verification (2026-11-16): one probe per thin-pass addition, 8 of 8 pass. Recorded in docs/EVALS.md.

## Held for later

- Marketing text modules, language modules beyond English, memory-file compression tools.
