---
name: write-commit
description: >
  Use when the agent writes a commit message, or when the user asks for
  commit text, a commit subject, or a commit body.
---

# Write commit

One change, one commit, one message. The message gives the intent. The diff already shows the what.

## Read first

1. Read the staged diff. A commit message describes the staged change, not the plan.
2. Read the history with `git log --oneline -15`. Match the type words, the scope style, and the capitalization of the repo.
3. Read the contribution guide when the repo has one. It wins on format.

## Subject

- Format: `type(scope): summary`. The scope part is optional.
- Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `chore`, `build`, `ci`, `style`, `revert`.
- Imperative mood: "add", not "added" or "adds".
- Fifty characters or fewer when possible. Seventy-two is the hard cap. No trailing period.

## Body

Skip the body when the subject says it all. Add a body only for:

1. A why the diff cannot show.
2. A breaking change and its migration path.
3. A linked issue or a follow-up.

Always add a body for a breaking change, a security fix, a data migration, and a revert. Future debuggers need the context. Wrap the body at 72 characters. Use dash bullets.

## Never

- No narration of files the diff already lists.
- No "I", "we", "now", "this commit".
- No tool attribution, unless a repo rule requires a trailer. Then add it as a trailer.
- No emoji, unless the repo history uses them.

## Example

```text
fix(auth): reject expired tokens with 401

The old check compared dates as strings, so a token issued last year
passed as valid. Compare timestamps as numbers instead.

Closes #412
```

## Output

Give one code block, ready to paste. This block writes text only. It never stages, commits, or amends.

## Output language

Write prose in ASD-STE100 Simplified Technical English. The rules live in `references/ste.md`.
