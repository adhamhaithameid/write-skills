---
name: write-jira
description: >
  Use when the user asks for Jira epics, stories, tickets, or story points,
  or asks to break a plan, spec, or discussion into ticket text.
---

# Write Jira tickets

Turn a plan into tickets an engineer can pick up without a meeting. Each story cuts through all layers and works on its own. Slice vertical, never by layer.

## Read first

1. Read the plan, the spec, or the discussion the user names.
2. Read the code area when access exists. Use the domain words of the codebase.
3. List the slices before you write the tickets. Confirm the list with the user.

## When the plan is thin

A plan without a goal, a number, or a constraint is not a plan yet. Do not slice it.

1. Name what is missing: the user-visible goal, the current numbers, the constraints.
2. Ask for those facts before you draft. A story with invented targets tests nothing.
3. When the user wants a draft anyway, mark every invented target as an assumption. Carry every unknown into the points reason.

## Slice rules

1. One story is one complete path through the stack: data, API, interface, tests.
2. A finished story demos on its own. A layer without a user-visible result is not a story.
3. Size a story to fit one work session. Split anything larger.
4. Name the blocking stories of each story. A story with no blockers can start.
5. A mechanical change that touches the whole repo gets its own sequence. Add the new form beside the old. Move the callers in batches. Then delete the old form.

## Epic template

```markdown
Title: <outcome, not a feature word>

Outcome:
<the user-visible state when this epic closes>

Scope:
- <story list, one line each>

Out of scope:
- <what this epic does not do>
```

## Story template

```markdown
Title: <what works when this story closes>

Story:
As a <role>, I <action>, so that <value>.

Acceptance criteria:
- [ ] <a testable condition>
- [ ] <a testable condition>

Blocked by:
- <ticket key or title, or "none">

Points: <n>
Points reason: <size, risk, or unknowns, in one line>
```

## Story points

1. Estimate from three inputs: size, risk, and unknowns.
2. Every estimate carries one reason line. A bare number carries no information.
3. When estimates differ by much, the story hides an unknown. Split it, or list the unknown in the story.
4. Points measure effort, not value. The value lives in the story line.

## Rules

- Write criteria a test can check. "The query answers in 200 ms at 10000 rows" is a criterion. "Works fast" is not.
- Keep file paths and code out of tickets. They go stale. A schema or type shape that holds a decision can go in, trimmed to the decision.
- This block writes text only. It never creates, edits, or moves an item in Jira.

## Output language

Write prose in ASD-STE100 Simplified Technical English. The rules live in `references/ste.md`.
