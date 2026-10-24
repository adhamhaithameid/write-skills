# Docs standard

The standard behind the document writer, as four questions. Ask them in order, when you draft and when you review.

## What job does this document do?

A document does one job. Settle the job before the first sentence. Two facts pick the job. Does the reader try to get something done, or to understand? Are they learning the field, or already working in it?

| Job | What the reader leaves with |
|---|---|
| Tutorial | A working thing they built with you, step by step. |
| How-to | A solved problem, through steps alone. |
| Reference | The fact they came to look up. |
| Explanation | The reason the thing is the way it is. |

**Tutorial.** You carry the newcomer. Their finished result is your responsibility, not theirs. Start with the thing they will have at the end. Every step ends in something they can see: output, a changed prompt, a log line. Park the theory in one clause and a link. Teach in the first person plural, as commands.

**How-to.** The reader already works in the field. Give the path to one goal and hold the teaching. Steps, decisions at forks, and links for the background. Name the page after the task the reader came for.

**Reference.** The reader is mid-task and wants a fact. Give facts, options, limits, and failure modes, with no opinion and no persuasion. Shape the page like the thing it describes, so both can be walked in the same order. Where code can generate the page, generate it.

**Explanation.** One bounded subject that still reads outside the product. Open on a real question about why. Bring in the decisions, the history, the constraints, and the roads not taken. This is the one job where the writer may argue a position.

Keep the jobs apart. A reference table inside a tutorial stalls the lesson; a how-to that argues slows the fix. Split the page and link.

## Do the sentences talk to the reader?

- Write to "you", in the now. Reserve "will" for events that truly sit in the future.
- Give every action an owner: "the loader parses the file". The passive voice earns its place only when the doer is unknown or beside the point.
- Steps are commands: "Click Submit." A step never "should be done"; it is done.
- Put the gate before the action it guards, so a reader who does not qualify can jump past.
- The normal path comes first. The exceptions wait below it.
- Write like a colleague who knows the subject. Instructions skip "please". Procedures never claim to be "simple", "easy", or "quick"; a reader in a procedure is stuck, or they would not be there.
- Promise nothing ahead of time, and do not open two sentences in a row with the same words.
- A link says where it goes, in its own words. A bare "click here" says nothing.
- Headings state the point, in sentence case. A task heading is a verb phrase; a concept heading is a noun phrase. One h1, no level skips.
- Sequences take numbers. Everything else takes dashes. A list gets a lead-in sentence and parallel items.
- Code sits in code font, screen parts in bold, series get their final comma. When a list is partial, say so up front instead of ending with "etc.".

## Does each sentence carry one thing?

- One instruction, or one thought, per sentence. Long sentences split: near 20 words for instructions, near 25 elsewhere.
- Warnings arrive before the step they protect.
- Articles stay. "Remove backup file" asks a question; "Remove the backup file" answers it.
- A word keeps one meaning and one role for the whole document.
- One verb per action, kept for the whole document.
- Procedures are commands, never stories and never passive.
- The "-ing" form of a verb takes on too many roles. Prefer the plain form.

## Can any sentence be read two ways?

- "Only" and "not" stand next to the word they change. "Only fails on growth" and "fails only on growth" disagree.
- Unstack the nouns. "The proto import budget check script" becomes "the script that checks the proto-import budget".
- Every "it", "they", and "this" points at exactly one thing. In doubt, say the noun again.
- Half-written pairs mislead. "Phase 1 moves the converters and Phase 2 the runtime" starves Phase 2 of its verb. Give it one.
- Small joining words stay when they settle the parse: "Ensure that the switch is off".
- Two articles prevent a false pair: "the client and the host" when they are two things.
- Say what "and" and "or" join: "both, and", "either, or", "if, then".
- A period beats a semicolon. A new sentence replaces a dash.
- Parentheses hold a whole grammatical unit, or nothing. Plurals never come from "(s)".
- Write "a, b, or both" over "a/b".
- One thing carries one name across the whole document. Three names for one thing force three memories.
- Idioms, slang, and Latin shortforms leave. A reader working in a second language, a translator, and an agent all parse plain constructions fastest.

## Three rules above all

1. When the sentence survives without a word, the word goes.
2. The short everyday word wins, unless the long one buys precision.
3. A rule that makes the sentence worse loses. Fix the sentence another way, or leave it.

The codebase supplies the words. Name the real symbol, file, flag, and command. Jargon you invent gets replaced by what a developer would say out loud.

## Keep it human

A page can pass every rule and still read like a machine wrote it. Every sentence the same length. No position taken. Nothing particular in sight.

- Vary the length on purpose. A short sentence lands a point. A long one carries a fact together with its condition or its cost.
- Take a position where the job allows it. Explanation weighs options, so say which one you favor. Reference stays neutral.
- Trade the sterile for the particular. "Schema changes can cause issues" says nothing; "a column rename fails the build" says the thing.

## Claims and evidence

- Write the symbols and paths that exist at this commit.
- A count or a tree in the page stays true at the commit that carries it, and the page includes the command that regenerates it.
- PR bodies and commit messages are documents too, with every rule here except the job rule. A PR body is a one-minute briefing.
- Product UI text is not a document. The product copy rules own it.

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
