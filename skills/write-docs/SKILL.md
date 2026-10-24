---
name: write-docs
description: >
  Use when the agent writes or revises a technical document: README,
  tutorial, how-to guide, reference page, explanation, RFC, design note, or
  release note. Also use for a document an agent reads, such as a skill file
  or an agent instruction file.
---

# Write docs

A tired engineer understands the document at the first read. Settle the job of the document, then hold every sentence to the rules. For the full standard, open `references/docs-standard.md`.

## Settle the job first

One document, one job. Two facts pick it: does the reader act or understand, and are they learning or working?

| Job | What the reader leaves with |
|---|---|
| Tutorial | A working thing they built with you, step by step. |
| How-to | A solved problem, through steps alone. |
| Reference | The fact they came to look up. |
| Explanation | The reason the thing is the way it is. |

Jobs stay separate. Split the page and link, rather than mixing.

## Sentence rules

1. Cut every word that does no work.
<!-- sync:sentence-floor start -->
2. One idea per sentence. Use 20 words or fewer in instructions and 25 words or fewer elsewhere.
3. Name the actor. Use the active voice. Use the passive voice only when the actor is unknown.
<!-- sync:sentence-floor end -->
4. Prefer the short everyday word, unless the long one buys precision.
5. Write to the reader as "you", in the now.
6. Steps are commands, and the gate comes before the action it guards.
7. The normal path comes first. The exceptions wait below it.
8. Pin "only" and "not" next to the word they change.
9. Unstack the nouns, and give every "it" and "this" exactly one target.
10. A period beats a semicolon. A new sentence replaces a dash. No slash-joins, no "(s)" plurals.
11. One thing carries one name across the whole document.
12. Name the real symbols, paths, flags, and commands. The codebase supplies the words.

## Revise an existing document

1. Read the whole page once before you change a line.
2. Settle the job of the page. Check every section against that job.
3. Repair the sentences that break the rules. Leave the sentences that hold.
4. Do not reword text that did not change. A rewrite of untouched text costs the reviewer time.

## Rhythm

A page can pass every rule and still read like a machine wrote it.

- Vary the sentence length on purpose. A short sentence lands a point.
- Take a position where the job allows it. Explanation weighs options. Reference stays neutral.
- Trade the sterile for the particular. "A column rename fails the build" beats "schema changes can cause issues".

## Agent mode

When an agent reads the document, add the scan rules. Skill files and agent instruction files follow this mode.

- Give every section a stable heading. The agent navigates by headings.
- End every step on a condition that tells the agent the step is done. Make the condition checkable.
- State what the environment does not show: the reason for a choice, the trap, the convention.
- Keep one meaning in one place. Do not restate a rule in a second section.
- Prune stale lines on every edit. A wrong instruction costs more than a missing one.

For the full agent-doc standard, open `references/agent-docs.md`.

## Worked example

Before:
```text
The configuration of retry behavior for the mail client is handled in
client.json. Running the client with --dry-run will output what would
have been sent, which is useful to know. If settings are wrong, errors
may occur.
```

After:
```text
`mail.ts` reads the retry count and the delay from `client.json`. Each
retry waits twice as long as the one before it. Run `mail.ts --dry-run`
to print the messages without sending them.
```

## Output language

Write prose in ASD-STE100 Simplified Technical English. The rules live in `references/ste.md`.
