# Skill audit, 25 October 2026

Rubric: the 24-check skill checklist. Each check scores 0, 1, or 2. Weighted total out of 70. The audit ran on the 0.3.0 tree, after the fixes listed below.

## Scores

| Skill | Score | Percent | Grade |
|---|---|---|---|
| write-better | 58 | 81 percent | B |
| write-compact | 63 | 88 percent | B |
| write-docs | 61 | 85 percent | B |
| write-pr | 63 | 88 percent | B |
| write-commit | 62 | 86 percent | B |
| write-comments | 63 | 88 percent | B |
| write-review | 58 | 81 percent | B |
| write-jira | 61 | 85 percent | B |
| write-issue | 58 | 81 percent | B |
| write-release | 56 | 78 percent | C |
| write-report | 58 | 81 percent | B |
| write-summary | 58 | 81 percent | B |
| write-handoff | 56 | 78 percent | C |
| write-longform | 61 | 85 percent | B |
| write-glossary | 58 | 81 percent | B |
| Set average | | 83 percent | B |

## Findings fixed in this audit

1. Four skills used terms that only write-better defines: "floor rules" in write-compact, "reader level" in write-longform, and "level 2" in write-pr. All reworded. No skill now depends on the vocabulary of another.
2. Jargon before definition: "one-way door" in write-pr and "pile file" in write-longform. Both defined at first use, or reworded.
3. write-docs claimed release notes while the manifest held them back. write-release now owns them, and the write-docs description dropped the claim.
4. write-better claimed status updates and bug reports. write-report and write-issue own them now, so the three descriptions no longer collide.
5. Four skills had no example. Every skill now carries one, and docs/examples.md holds the gallery.

## Weakest checks, set wide

- Check 6, completion criteria. Steps say what to do, but few say how the agent knows the step is done. Scored 1 across the set.
- Check 21, trigger tests both ways. The routing test covers the should-fire direction only. The seven new skills have no trigger evidence yet. New skills scored 0.
- Check 24, real-host tests. Installs are verified, behavior inside a host is not.
- Check 3, scope boundary in the description. Most descriptions state when to fire, not when not to. Scored 1, except write-longform.

## Next actions, in order of weight

1. Run the eval cases for the seven new skills and the unrun core and longform cases.
2. Add three should-not-fire prompts per skill to the routing test.
3. Sharpen step endings into checkable criteria, starting with write-better and write-docs.
4. Cap the set at fifteen until the trigger test proves no collisions.

## Method note

Scores were assigned by reading each skill against the checklist. The behavior evidence in docs/EVALS.md is the proof for checks 20 and 22. Re-run this audit after every release and record the delta.
