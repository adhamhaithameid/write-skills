# Changelog

## Unreleased

- Enforcement: the lint checks the mechanical STE rules. It adds the 20-word cap in numbered steps, passive voice, and "-ing" verb checks, and it now covers docs/EXPERIMENT.md. A `<!-- ste:ok: reason -->` marker exempts one line, with the reason beside it.
- New `--lint FILE` mode in tools/check.py, and a commit-msg hook in .githooks that fails a commit with a violation.
- One addition per thin skill from the experiment:
- write-better: stop and ask when a fix would change the meaning.
- write-docs: a check before you send.
- write-commit: never invent a ticket number.
- write-review: quote the code line behind every severity. A mandatory not-checked list.
- write-release: unclear history lands as unknown, with the hash.
- write-plan: the plan ends on the approval question.
- write-glossary: definitions point at repo sources.
- write-ste: run the mechanical lint first.
- Addition probes: 8 of 8 pass, recorded in docs/EVALS.md. The probes live as eval cases.
- Rules register: the reader-load rules moved from B23-B30 to N1-N8. The old IDs had belonged to merged rules. The experiment score line is corrected to 14 clear passes, 8 thin passes.

## 0.4.1 - 2026-10-29

- Store-front polish: badges, a why section, a quick start, the skill table grouped into four families, per-agent install, and a docs map in the README. The npm description and keywords now match the twenty-two-skill set.


## 0.4.0 - 2026-10-29

- Seven new skills: write-tldr, write-plan, write-again, help-write, write-adr, write-prd, write-ste. The set is now twenty-two.
- write-core renamed to write-better. New reader-load rules: the seven reader-slowing patterns from the NYU/UT Austin study, plus the anti-homework rules.
- write-compact: explain-again moved to write-again. A sibling rule sends long answers to a short end-of-turn block.
- Mission line added to the README and BLOCKS: the reading experience must never feel like hell.


## 0.3.1 - 2026-10-25

- Rich styling rules in write-core, write-docs, and write-pr: bold discipline, callouts, diff fences, collapsed sections, tables, alt text. Markdown carries no color codes, so emphasis comes from structure.


## 0.3.0 - 2026-10-25

- Seven new skills: write-review, write-release, write-issue, write-summary, write-handoff, write-report, write-glossary. The set is now fifteen.
- Every skill reads local rule files first: agent instructions, contribution guides, and glossaries. A synced section and a shared reference enforce it, and local rules beat skill defaults.
- Every skill carries a before-and-after example. A gallery lives in docs/examples.md.
- Vocabulary fixes: no skill depends on terms only another skill defines.
- write-core no longer claims status updates and bug reports. write-report and write-issue own them.


## 0.2.1 - 2026-10-24

- write-jira: Fibonacci story points with the effort, complexity, and uncertainty model, and a three-point calibration.

## 0.2.0 - 2026-10-24

- write-commit: pruned the formatting rules that duplicate default model behavior. The process rules stay: read the history, let the repo convention win, write text only.
- write-jira: new thin-plan rule. A plan without a goal, a number, or a constraint does not get sliced. Ask for the facts first.
- write-docs: new revision section. Read the page once, settle the job, repair what breaks, leave what holds.
- Eval cases for every block. Trigger routing evidence: 16 of 16. Live-repo evidence for the commit process rules.

## 0.1.0 - 2026-10-24

- First release with eight skills.
- Each skill works alone.
- Every skill writes in Simplified Technical English.
