# write-skills

Fifteen agent skills for writing. Each skill works alone. Install one skill or all of them.

## Skills

| Skill | Use for |
|---|---|
| write-core | Chat answers, explanations, and notes. Reader levels, depth, sentence rules, AI patterns. |
| write-compact | Brief replies on request, or explain a confusing reply again. |
| write-docs | READMEs, tutorials, how-to guides, reference pages, explanations, RFCs, and documents an agent reads. |
| write-pr | PR title and description from the change and the evidence. |
| write-commit | Commit message from the staged diff and the repository history. |
| write-comments | Code comments that state intent, constraints, and invariants. |
| write-review | Review comments on a diff: location, problem, fix. |
| write-jira | Jira epics, stories, and story points from a plan. |
| write-issue | GitHub issues and bug reports with reproduction steps. |
| write-release | Release notes from git history. |
| write-report | Status updates, incident reports, and findings for a decision-maker. |
| write-summary | Summaries of threads, docs, logs, and meetings that keep the facts. |
| write-handoff | Handoff notes so work continues in a fresh session. |
| write-longform | A staged long-form mission: collect raw material, then build the article. |
| write-glossary | Build or clean a glossary, one term per concept. |

## See the difference

Every skill states what it changes. Three samples here. The full gallery of all fifteen is in `docs/examples.md`. The pairs are hand-written examples of the rules, not recorded sessions.

write-core, a chat answer:

```text
Before: "Sure! I'd be happy to help. In order to boost your productivity,
this robust tool leverages cutting-edge caching."
After:  "The tool caches your queries. A repeat query answers in 12 ms."
```

write-pr, a PR body:

```text
Before: "This PR makes several improvements to the authentication system
and cleans up a number of related issues."
After:  "Summary: reject expired session tokens at login. Evidence: the
reset test fails on main, passes here. Risk: two-way door, login only."
```

write-jira, a story:

```text
Before: "BE-1 Backend table (3)   BE-2 Upload endpoint (5)   WEB-1 Button (5)"
After:  "One vertical story: POST /tasks/{id}/attachments saves the file,
the web view lists it. Points: 5. Reason: one table, one endpoint,
one screen in a single slice."
```

## Local rules

Every skill reads your local rule files first: `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and `GLOSSARY.md`. Your glossary terms and repo conventions beat the skill defaults. The skills never edit those files.

## Install

Install every skill from this repository:

```
npx skills add adhamhaithameid/write-skills
```

Install one skill:

```
npx skills add adhamhaithameid/write-skills --skill write-core
```

Install the npm package, then copy a skill folder into the skills folder of your agent, for example `~/.claude/skills/`:

```
npm install write-skills
```

Or copy a folder from `skills/` by hand. Each skill folder holds everything the skill uses.

No skill needs another skill.

## Output language

Every skill writes its prose output in ASD-STE100 Simplified Technical English. Each skill carries its own copy of the rules in `references/ste.md`.

## Check the repo

Run these commands from the repo root:

```
python3 tools/check.py
python3 -m unittest discover -s tests
```

The check script tests frontmatter, links, private data, synced rule copies, and the style of the files that this repo authors.

## Contribute

Read `CONTRIBUTING.md` first.
