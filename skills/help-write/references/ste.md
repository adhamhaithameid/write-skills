# Simplified Technical English rules

## Purpose

Write prose that a non-native English reader understands at first read, without guessing. These rules follow the Issue 9 principles of ASD-STE100.

## Scope

Applies to chat replies, commit messages, PR descriptions, documentation, release notes, status updates, and bug reports.
Does not apply to code identifiers, product UI copy, quoted user text, file paths, and shell commands.

## Writing rules

1. Keep sentences short. Use 20 words or fewer in instructions. Use 25 words or fewer in descriptive text.
2. Write one instruction, or one topic, per sentence.
3. Use the active voice. Use the passive voice only when the agent is unknown. Name the agent when you know it.
4. Write one topic per paragraph. Use 6 sentences or fewer per paragraph.
5. Use simple verb forms only: simple present, simple past, simple future, imperative, infinitive.
6. Do not use the "-ing" form of a verb unless it is a technical noun.
7. Use each word with one meaning only.
8. Do not use multi-word nouns with more than three words.
9. Do not use idioms, slang, metaphors, jokes, or cultural references.
10. Do not use double negatives. Write one clear negative, or write the positive statement.
11. Do not use contractions. Keep the articles "the" and "a" in sentences.
12. Use the same word for the same thing. Do not alternate synonyms.
13. Use vertical lists for data or steps with more than two items.
14. In procedures, start each step with the command verb. Put warnings before the step.
15. Split complex text into more sentences. Do not omit the subject or the article to make a sentence shorter.

## Word guidance

- Prefer the shortest common word: "use", not "utilize". Write "start", not "initiate". Write "before", not "prior to".
- Treat the approved word list of STE, about 900 words, as the target vocabulary. Approximate it with common English words, one sense each.
- Technical terms are allowed. Define a technical term on first use.
- Do not invent a new term for a thing you already named.

## Examples

Commit message, before and after:

```text
Before: "Refactored auth layer to leverage modern async patterns, kicking
off the long-overdue cleanup of the legacy session nightmare."
After: "Make the auth module use async functions. Remove the old session
code. Do not migrate session data. See ticket ABC-123."
```

Status update, before and after:

```text
Before: "We're currently experiencing some issues with the deployment
pipeline, which has been acting up since this morning."
After: "The deployment pipeline failed at 09:15. The build step gave error
E403. We are investigating the cause. The next update comes at 14:00."
```

Bug report, before and after:

```text
Before: "Users can't seem to export their reports whenever the dataset is
particularly large. It just silently fails without any error."
After: "Export fails for datasets larger than 50000 rows. The app shows no
error. To reproduce: load the sample dataset, click Export, wait 60 seconds."
```

## Conflicts with other styles

When another active style conflicts with these rules, these rules win for prose. A brief style may shorten sentences further. It keeps every fact, negation, and number.

## Compliance check

- Are all sentences 25 words or fewer?
- Does each sentence give one instruction or one topic?
- Is the voice active, except where the agent is unknown?
- Are there no idioms, jokes, metaphors, contractions, or double negatives?
- Is every technical term defined on first use, and is each term stable?

## Sources

- https://asd-ste100.org/
- https://en.wikipedia.org/wiki/Simplified_Technical_English
- https://github.com/danyuchn/asd-ste100-skill
