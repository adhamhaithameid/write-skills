# Behavior eval results

Date: 24 October 2026. Method: one eval case per skill, run twice in fresh agent contexts. One run without the skill text, one run with the skill text in the prompt. A human graded both runs against the assertions in the `evals/` folder of each skill.

## Results

| Skill | Case | Control run | Skilled run | Verdict |
|---|---|---|---|---|
| write-commit | 1, simple fix | Correct subject, correct format | Same subject, code block as specified | No separation. The case is too easy for the base model. |
| write-commit | 2, breaking change | Correct subject with "!", body, migration date, ticket, BREAKING CHANGE footer | Same structure, dash bullets, migration step | No separation. The base model knows the breaking-change convention. |
| write-commit | 3, repo with its own convention | Followed the observed "Area: change" style | Same style, matched the history wording | No separation. Both arms respected the given convention. |
| write-pr | 1, rate limit change | Improvised sections, invented a justification the input never gave | Exact template: summary with sketch, evidence before and after, door type, blast radius | Clear pass for the skill. |
| write-jira | 1, attachments plan | Sliced by layer, bare points, no blocking edges | Vertical slices, outcome epic, blocking edges, points with reason lines | Clear pass for the skill. |
| all blocks | Trigger routing, 8 tasks, 2 samples | 16 of 16 correct, no variance | same | Discovery works from the descriptions alone. |
| write-commit | Live repo with its own convention | Ignored the observed convention, narrated implementation detail | Read the history, matched it: "Queue: add RetryQueue class" | Clear pass for the process rules. The format spec was pruned in 0.2.0. |
| write-jira | 3, vague plan, first run | Invented precise targets from nothing | Also invented targets | No separation. Both arms failed the intent. |
| write-jira | 3, vague plan, after the thin-plan rule | not rerun | Refused to slice, named the missing facts, asked, offered an assumption-marked draft | Fixed and validated. The rule was added in 0.2.0. |
| write-compact | 1, explain again | Rebuilt well, missed two terms, no next step | Named the break, defined all five terms, ended with a next step | Partial pass for the skill. |
| write-docs | 1, revise a paragraph | Good revision, warning after the action | Good revision, explicit warning before the action | Thin separation. Both improved the text. |
| write-comments | 1, comment a function | Acceptable, one restated line | Constraint at the decision line, no restatement | Thin separation. |

## Reading

- Every block now carries eval cases in its `evals/` folder. Cases for write-core and write-longform are written but not run.
- The PR, Jira, and commit blocks change behavior in the intended direction. The commit value sits in the process rules, proven by the live-repo test: read the history first, let the repo convention win.
- The compact block earns a partial pass. The docs and comments blocks show thin separation on one case each. The base model is already close, and the skill adds placement and ordering discipline.
- Trigger routing is clean: 16 of 16 in two samples. This test shows the descriptions as written to a host. A real host injects them differently, so in-host firing stays unverified.
- The vague-plan case exposed a real gap, fixed the same day. The thin-plan rule now stops slicing before the facts arrive, and the rerun proved it.

## Run more

The cases live in `skills/<name>/evals/evals.json`. Run a case with two fresh agents: one gets the bare prompt, one gets the prompt with the skill text. Grade both outputs against the assertions.
