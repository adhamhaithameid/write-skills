---
name: write-commit
description: >
  Use when the agent writes a commit message, or when the user asks for
  commit text, a commit subject, or a commit body.
---

# Write commit

The message gives the intent. The diff already shows the what.

## Read first

1. Read the staged diff. The message describes the staged change, not the plan.
2. Read the history with `git log --oneline -15`. The history sets the format: the type words, the scope style, the capitalization, the length.
3. Read the contribution guide when the repo has one. It wins over the history.

The repo convention wins over any default. When the history writes "Area: change", write "Area: change". When the history writes Conventional Commits, write Conventional Commits.

## Write

- One subject line, imperative, the real change. Keep to the length the history uses.
- Add a body only for what the diff cannot show: a why, a migration path, a linked ticket.
- A breaking change, a security fix, a data migration, and a revert always get a body.
- Keep file narration out. The diff lists files.
- No tool attribution, unless a repo rule requires a trailer.

## Output

Give one code block, ready to paste. This block writes text only. It never stages, commits, or amends.

## Example

```text
fix(auth): reject expired tokens with 401

The old check compared dates as strings, so a token issued last year
passed as valid. Compare timestamps as numbers instead.

Closes #412
```

## Output language

Write prose in ASD-STE100 Simplified Technical English. The rules live in `references/ste.md`.
