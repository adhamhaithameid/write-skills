# Behavior eval results

Date: 24 October 2026. Method: one eval case per skill, run twice in fresh agent contexts. One run without the skill text, one run with the skill text in the prompt. A human graded both runs against the assertions in the `evals/` folder of each skill.

## Results

| Skill | Case | Control run | Skilled run | Verdict |
|---|---|---|---|---|
| write-commit | 1, simple fix | Correct subject, correct format | Same subject, code block as specified | No separation. The case is too easy for the base model. Cases 2 and 3 in the eval file stay unrun. |
| write-pr | 1, rate limit change | Improvised sections, invented a justification the input never gave | Exact template: summary with sketch, evidence before and after, door type, blast radius | Clear pass for the skill. |
| write-jira | 1, attachments plan | Sliced by layer, bare points, no blocking edges | Vertical slices, outcome epic, blocking edges, points with reason lines | Clear pass for the skill. |

## Reading

- The PR and Jira blocks change behavior in the intended direction. The evidence sits in the table above.
- The commit block needs its harder cases run before any claim. Case 2, the breaking change, and case 3, the repo with its own convention, are the ones that can separate.
- No trigger tests exist yet. Every test above inlines the skill text, so it measures the instructions, not the discovery.
- write-core carries the earlier pattern micro-test from 24 October 2026, in the repository history. The remaining blocks carry no runtime evidence.

## Run more

The cases live in `skills/<name>/evals/evals.json`. Run a case with two fresh agents: one gets the bare prompt, one gets the prompt with the skill text. Grade both outputs against the assertions.
