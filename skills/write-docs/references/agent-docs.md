# Agent-doc standard

For documents an agent reads: skill files, agent instruction files such as AGENTS.md, and memory files. The goal is a predictable process: the agent takes the same path on every run. The same levers work for all three shapes.

## Context pointers

A context pointer names material that sits outside the context, and states when to reach it. A skill description is one. A line in an instruction file that names a doc is the same object.

- The wording of the pointer, not its target, decides when the agent reaches the material, and how reliably.
- A pointer does two jobs: state what the material is, and list the cases that should trigger it.
- Put the key word first. The start of the pointer does the trigger work.
- One trigger per case. Synonyms that rename one case are one case written twice. Cut them.
- A weak pointer in front of a must-have target is a bug. Sharpen the wording first. Inline the material only when sharpening fails.

## The two loads

Every document and pointer spends one of two budgets.

- Context load is the cost of always-present material: an instruction file line, a skill description. It spends attention on every turn, fired or not.
- Cognitive load is the cost on the human: which documents exist, and when to reach for each. The human is the index.
- Spend cognitive load where human judgment matters. Remove it where it does not.

## Information hierarchy

A document holds steps, the ordered actions, and reference, the facts read on demand. Each piece sits on a ladder ranked by how soon the agent needs it.

1. In-file step: what the agent does, in order. The primary tier.
2. In-file reference: rules and facts read on demand. A flat set of peer rules is a fine shape.
3. Disclosed reference: a separate file behind a pointer, loaded only when the pointer fires.

Push too little down and the top bloats. Push too much down and you hide material the agent needs.

- Move material down the ladder so the top stays legible. This protects the hierarchy, not only the token count.
- The cleanest test: inline what every path needs. Push behind a pointer what only some paths reach.
- Keep the definition, the rules, and the caveats of one concept under one heading. Reading one part then carries its neighbors.
- A document can be too long even when every line is live. The cure is the ladder, not deletion of meaning.

## Completion criteria

Every step ends on a condition that tells the agent the step is done.

- Make the condition checkable: can the agent tell done from not done?
- Make the condition demanding: "account for every changed model" forces thorough work. "List the changes" does not.
- A vague bound invites an early stop. Sharpen the bound first. Only a bound that cannot be made sharp justifies hiding the later steps behind a split.
- A demanding criterion also binds flat reference: "apply every rule" holds a rule set to full coverage.

## Leading words

A leading word is a compact concept the model already knows. Used as a repeated token, it anchors a region of behavior in few words.

- Reach for a word that already exists in pretraining. A made-up word recruits nothing and pays in definition.
- The same word in your prompts, your docs, and your code links them all to the material, and the agent reaches it more reliably.
- One strong word replaces a spelled-out triad. "Fast, deterministic, low overhead" collapses into one word the reader already holds.

## State the positive

Steering by prohibition names the behavior you do not want and makes it more available, not less.

- State the target behavior, so the banned one is never spoken.
- Keep a prohibition only as a hard guardrail you cannot phrase in positive form. Pair it with the positive target.
- A weak instruction the model already obeys by default says nothing. Delete it. When it fails the default test, the fix is a stronger word, not more words.

## Pruning

- Keep each meaning in one authoritative place, so a change is a one-place edit. The same meaning in two places costs maintenance and tokens.
- The environment is a source of truth too: config files, scripts, directory layout, help output. Do not restate what the agent can look up. It goes stale.
- Cache only what the environment cannot show: the reason behind a choice, the trap, the convention nobody wrote down.
- Check every line for relevance on every edit. Stale layers settle because adding feels safe and removing feels risky. Core down through them.
- Delete a sentence that fails the default test whole. Do not trim words from it.

## Skill files

When the document is a skill file, add:

- Frontmatter holds the name and the description. The description states when to use the skill. It never summarizes the workflow.
- Keep the skill auto-invoked when the agent must reach it on its own. Restrict it to manual use only when the human is the sole caller.
- When manual skills multiply past memory, one router names them all, and when to reach for each.
