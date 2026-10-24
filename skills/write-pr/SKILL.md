---
name: write-pr
description: >
  Use when the agent writes a pull request title or description, or when the
  user asks for PR text, a PR body, or a reviewable summary of a change.
---

# Write PR

Write a briefing a reviewer reads in under one minute. Build it from the actual change and the evidence. Never invent evidence.

## Read first

1. Read the full diff of the branch.
2. Read the linked issue or ticket when one exists.
3. Read the test output, the build result, or the screenshots that show the change works.
4. Read recent PR titles in the repo. Match their format.

## Title

- One line, imperative, names the real change. Example: "Add rate limits to the login endpoint".
- Use the type prefix the repo already uses, when it uses one.
- Keep 72 characters or fewer.

## Body template

```markdown
## Summary

What the change does, and why, in 2 or 3 sentences.
Sketch: file tree, call tree, or diff sketch.

## Evidence

- Before: failing test, error output, or old behavior.
- After: passing test, output, or new behavior.

## Risk

- Door: one-way or two-way.
- Blast radius: the parts this change can break.
```

## Sketch rules

Pick the smallest view that makes the point. One sketch is enough for most changes.

- Show logic as short code or plain steps.
- Show a file layout change as a shallow tree with one-line comments.
- Show a control flow change as a diff of the call tree.
- Show a UI change with a screenshot when the environment allows it.

## Rules

- State what the change does first. State why second.
- Link long logs and dashboards. Do not paste them.
- Name the risk honestly. A one-way door gets a warning line in the summary.
- Write saved text at level 2 or higher. Never use a brief voice here.
- This block writes text only. It never opens, merges, comments on, or closes a pull request.

## Output language

Write prose in ASD-STE100 Simplified Technical English. The rules live in `references/ste.md`.
