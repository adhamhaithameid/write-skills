# Skill experiment, 30 to 31 October 2026

Every skill in the set, tested with and without its own rules. The method, the raw before-and-after pairs, and the verdicts.

## Method

- 22 skills, one case each, two arms. Control arm: the task prompt only. Skilled arm: the task prompt plus the skill rules. Nothing else in the prompt.
- Channel 1: fresh subagents of the coding agent, 2 samples of context. One per run, no tools allowed, answer from the prompt only.
- Channel 2: OpenCode 1.19.5 on the beam-free model, 8 representative skills, run from a clean directory.
- Both arms of the subagent channel ran with the machine's global Simplified Technical English rules in the system prompt. That raises the control arm's floor. The comparison measures what the skill adds on top of that floor.
- Grading: against the assertions in each skill's `evals/` folder.

One control arm went off prompt and investigated the real repository with tools. That run was discarded and the whole experiment moved to tool-free prompts. The verdicts below are honest about thin separation: where the base model is already good, the report says so.

## Verdict summary

| Skill | Verdict | What the skill changed |
|---|---|---|
| write-better | Thin pass | Less ceremony, a code example, varied rhythm |
| write-compact | Clear pass | The exact one-line answer; the control run went off prompt and was invalid |
| write-tldr | Clear pass | The exact TLDR and Found block |
| write-again | Clear pass | Named the broken terms, a new analogy, a next step |
| help-write | Clear pass | Routed to the report skill; the control routed to the issue skill |
| write-docs | Thin pass | Warning before the action, reader addressing |
| write-pr | Clear pass | The exact template with sketch, door, blast radius |
| write-commit | Thin pass | Tighter intent body, less diff narration |
| write-comments | Clear pass | No restatement; the constraint at the decision line |
| write-review | Thin pass | Exact path:line format, severity tags, an honest not-checked line |
| write-jira | Clear pass | Vertical slices, reasoned points, blocking edges |
| write-issue | Clear pass | Missing facts listed, suspicion labeled |
| write-release | Thin pass | Internal noise dropped, user-visible effects named |
| write-report | Clear pass | Answer first, observed and inferred labels, honest risks |
| write-summary | Clear pass | Gist, decisions with owners, numbers table, open questions |
| write-handoff | Clear pass | Claim labels, commands block, traps |
| write-plan | Thin pass | Source labels, marked assumptions, costed options |
| write-adr | Clear pass | Full record shape with honest costs |
| write-prd | Clear pass | No invented targets; unknown baselines named |
| write-longform | Clear pass | Brief as a draft, approval gate, no premature prose |
| write-glossary | Thin pass | One tight line, no invented features |
| write-ste | Thin pass | A definition point and a length check on top of an already good control |

Score: 13 clear passes, 9 thin passes, 0 failures.

## Before and after, channel 1

### write-better

Before (control):
```text
The build failed because of a type check, not a runtime crash.
...
How to fix it:
1. Open `src/cart.ts` and go to line 41.
2. Find where the string value comes from. Common sources are form
   inputs, URL parameters, and API responses.
3. Choose one of these fixes: ...
```

After (skilled):
```text
The build failed because TypeScript found a type mismatch in `src/cart.ts`
at line 41.
...
To fix the build, open `src/cart.ts` and go to line 41. ...
- Remove the quotes, if the value should be a number: `let quantity: number = 3;`
...
If you cannot tell which fix is correct, ask the person who last changed
that file. The git history (`git blame src/cart.ts`) shows who that is.
```

Verdict: thin pass. Both arms are clear. The skilled arm drops the "How to fix it" ceremony, shows the wrong code inline, and ends on a next step. The control's structure reads more like homework.

### write-compact

The control arm left the prompt: it inspected the real repository with tools and refuted the task's premise. Discarded as invalid. The skilled run:

```text
The PR 41 migration drops `users.email`. A revert before the next
release restores it.
```

Verdict: clear pass. One line, both facts, nothing else.

### write-tldr

Before (control):
```text
**TL;DR**
- Run `scripts/migrate-login.ts` once, then deploy.
- Rollback is possible before the next release.
- Side note: the retry helper in `queue.py` counts each failure twice.
  Fix it separately.
```

After (skilled):
```text
TLDR: Run scripts/migrate-login.ts once, then deploy. Rollback is
possible until the next release.
Found: The retry helper in queue.py double-counts failures.
```

Verdict: clear pass. The control improvised a near-miss format. The skilled arm hit the contract: one TLDR line, one Found line, no advice.

### write-again

Before (control): rebuilt with pseudo-code and decoded "pure" and "composable". Sound, but it reused the original framing.

After (skilled):
```text
Let me rebuild this from the start. Three terms did the damage:
"decorator", "pure", and "composable". I will define each one and show
the steps.
...
**New analogy**
Think of airport security. You (the handler) are the passenger with one
job: fly. Each checkpoint is a decorator ...
**The one-sentence version** ...
Next step: look at one decorator in the code and name its single job in
one line.
```

Verdict: clear pass. The skilled arm names where the read broke, brings a genuinely new analogy, and closes on a next step.

### help-write

Before (control): "Route to: **write-issue**." A defensible read, but a pasted stack trace with "tell the team what happened" is an incident explanation, not a filed issue.

After (skilled): "Route: **write-report** — a stack trace explained as 'what happened' for the team is an incident-style status report."

Verdict: clear pass. The three routing questions picked the right row.

### write-docs

Before (control):
```text
Configure the exporter with exporter.json. Use `--reset` only when you
want to delete all state. Incorrect use of `--reset` can cause data loss.
```

After (skilled):
```text
You configure the exporter with `exporter.json`. Warning: `--reset`
forgets all state and can cause data loss. Use `--reset` only when you
want to forget all state.
```

Verdict: thin pass. Both cut the filler. The skilled arm puts the warning before the action and addresses the reader.

### write-pr

Before (control): improvised sections — What, Why, Test, Rollback. No sketch. The risk framing is a rollback note.

After (skilled): the exact Summary, Evidence, Risk template, with a file sketch, a two-way door, and a blast radius line about shared clients behind one address.

Verdict: clear pass. The template is the product.

### write-commit

Before (control): correct conventional subject plus a body that narrates the diff: "Change the check to `issuedAt < expiry`. ... Update the test to cover the boundary case."

After (skilled):
```text
fix(auth): reject tokens at exact expiry

A token issued exactly at its expiry time was valid before. Treat it as
expired, and cover the boundary in the test.
```

Verdict: thin pass. Both follow the repo format. The skilled body gives the why and stops narrating the diff.

### write-comments

Before (control): restated the code twice — "Read the protocol version from byte 0." and "Reject all versions except 2."

After (skilled):
```js
// Byte 0 holds the protocol version.
const version = buf.readUInt8(0);
// The gateway accepts only version 2; versions 0 and 1 were removed in 2025.
if (version !== 2) throw new Error('unsupported');
```

Verdict: clear pass. The restatement is the exact anti-pattern the skill names. The skilled arm keeps one constraint comment at the decision line.

### write-review

Before (control): the same three findings, wrapped in bold headers and long sentences.

After (skilled):
```text
- src/auth.ts:41 bug. `user` is null on the reset path, so `if
  (user.token)` throws. Check `user` first: use `if (user?.token)` or an
  early null check.
- src/auth.ts:58 nit. The literal 3 as a retry cap has no name. Extract
  a named constant ...
- src/auth.ts:41 bug. No test covers the reset path ... Add a test that
  runs the reset path with `user` null.
Could not check: I did not see the full diff or the file ...
```

Verdict: thin pass. Same substance; the skilled arm lands the format, the severity tags, and the honest not-checked line.

### write-jira

Before (control): layer slices — a data-model story, an endpoint story, one combined mobile story. Points mostly bare, though Fibonacci appeared.

After (skilled): outcome epic with out-of-scope, three vertical stories, testable checkboxes, blocking edges, and points with effort, complexity, and uncertainty reasons.

Verdict: clear pass. The slice direction is the whole game.

### write-issue

Before (control): good structure, but it invented a cause: "the silent failure suggests the export code does not catch or report the error."

After (skilled): exact size, format, and console output listed under "The reporter must add these facts", and the cause labeled "Suspected, unconfirmed ... No evidence supports it yet."

Verdict: clear pass. The skill's honesty rules are the difference.

### write-release

Before (control): kept the refactor and the dependency bump as "Internal Changes".

After (skilled): two heads, two sentences, both naming the user-visible effect. Internal noise gone.

Verdict: thin pass. The control is close; the skill enforces the drop.

### write-report

Before (control): invented an event. "We rolled back 2.6 and latency returned to the old value." The prompt said only that a rollback restores the old plan.

After (skilled): answer first, every evidence line labeled observed or inferred, a confidence statement, and a risk the control missed: the plan count could come from stale statistics instead of the PR.

Verdict: clear pass. The fabrication is exactly what the labels prevent. One honest note: the skilled arm labeled one line "observed; source: post-rollback test" with a source the prompt never gave. The labels help; they do not replace judgment.

### write-summary

Before (control): one accurate paragraph. All facts kept, the open question named.

After (skilled): gist line, decisions with owners, a numbers table, open questions as a list.

Verdict: clear pass. Same facts, scannable shape.

### write-handoff

Before (control): decent sections, but claims stand unmarked and the commands live in prose.

After (skilled): every claim labeled verified or not verified, a commands code block, traps with reasons, and an explicit limits note.

Verdict: clear pass. The labeling discipline is the product.

### write-plan

Before (control): a strong plan — approach, steps with checkable results, rollback, risks. No marked option among alternatives, no out-of-scope, no source labels.

After (skilled): source and assumption labels on every fact, three options each with cost, risk, and what it buys, a recommended pick with the reason, steps that each end on a check, risks with early signs, and an out-of-scope list.

Verdict: thin pass. The control was already good; the skill adds the approval-facing honesty layer.

### write-adr

Before (control): a five-line record. Decision, reason, rejected options. No status, no consequences, no number.

After (skilled): the full record — status, context with the numbers and the rejected options with reasons, a one-sentence decision, and consequences that name the costs: a new dependency, a network hop, an outage mode.

Verdict: clear pass. The consequences section is the part teams skip.

### write-prd

Before (control): invented freely. New targets ("less than 20 percent", "99.9 percent availability"), new scope (email fallback, phases, seven requirement details) that the input never gave.

After (skilled): the two goals as given, requirements that restate only the input, and four metrics that say "Baseline: not measured yet." Open questions with unassigned owners.

Verdict: clear pass. The no-invention rule is the difference.

### write-longform

Before (control): wrote article prose without approval, framed "three problems" from nothing, and used placeholder tokens for numbers.

After (skilled): the brief marked "draft, pending your approval", no prose written, and four questions including the path to the notes and the leading word to mine.

Verdict: clear pass. The approval gate held.

### write-glossary

Before (control): a solid entry, but it invented features: "It also handles authentication, rate limits, and response formatting."

After (skilled): one table line — term, definition from the given facts only, merged synonyms with their sources.

Verdict: thin pass. Tighter, and nothing invented.

### write-ste

Before (control): a good fix with six named violations and rule numbers. The machine's global STE rules already train this.

After (skilled): the same violations, plus two points the control missed: define "upstream dependency" on first use, and check the sentence length explicitly.

Verdict: thin pass. The skill adds the checklist's last mile.

## Channel 2: OpenCode 1.19.5, the beam-free model

Eight representative skills, same cases, run from a clean directory. This channel produced three findings, and one of them changes how the results read.

### Finding 1: the skills fire in a real host

OpenCode auto-discovered the installed skills and invoked them on its own. The run logs show `→ Skill "write-adr"`, `→ Skill "write-ste"`, and the local-rules step executing. This confirms in-host discovery, which no prompt test can prove.

### Finding 2: the control arms are contaminated on this channel

Because the skills auto-fire, the "control" arm received the skill too. The write-adr control produced a full record shape, and the write-plan control echoed the skill's own example almost verbatim. No control comparison is valid on this channel. The pairs below are qualitative only.

### Finding 3: the local-rules step executed for real

The write-prd skilled run opened with a live check, logged by the host:

```text
=== AGENTS.md === NOT FOUND
=== CLAUDE.md === NOT FOUND
=== CONTRIBUTING.md === NOT FOUND
=== GLOSSARY.md === NOT FOUND
```

It found no local files, continued without comment, and kept the source attribution on the problem statement. That is the synced local-rules block doing its job in a host we do not control.

### Qualitative results, beam-free

- write-tldr: the skilled arm hit the exact TLDR and Found block. The control improvised a TL;DR bullet list.
- write-again: both arms rebuilt well; the skilled arm kept the "new example, same mechanism" shape and closed on a next step.
- write-prd: the skilled arm separated observed facts from targets, marked unknown baselines, and left open questions with owners.
- write-better: the skilled arm defined string and number with concrete examples and gave file-and-line next steps.
- help-write: both arms routed to the report skill.
- write-ste: both arms named the same violations; the control had already loaded the skill.

### A warning about beam-free itself

The model returned a duplicated answer on one run: the write-plan skilled slot received the write-better answer from an earlier turn. beam-free is usable for smoke tests, not for graded comparisons. For graded runs, use a stronger model on the same OpenCode setup.

## What the experiment changed

1. The eval method now has two validated channels, and the prompt-only constraint is part of the fixture.
2. In-host firing is proven on OpenCode. The remaining unknown is firing inside this coding agent's own host, which the provider blocked during this experiment.
3. The thin passes point at one truth: the machine's global STE rules already lift every control arm. The skills earn their keep where they own a format, gate an approval, or forbid fabrication.
