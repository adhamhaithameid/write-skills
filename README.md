# write-skills

[![npm](https://img.shields.io/npm/v/write-skills.svg)](https://www.npmjs.com/package/write-skills)
[![ci](https://github.com/adhamhaithameid/write-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/adhamhaithameid/write-skills/actions/workflows/ci.yml)
[![license MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Twenty-two agent skills that fix how agents write. Each skill works alone. Install one skill or all of them.

> The mission: the reading experience must never feel like hell. Every skill serves that.

## Why

AI text is hard to read. Subjects sit far from their verbs. Nouns stack four deep. Databases want things and conversations eat their own tails. A 2026 study by NYU and UT Austin found these patterns across 14 models and tied them to how the models train. This set fixes the patterns at the source.

It also gives the agent a shape for every text a developer writes: chat replies, commit messages, PR bodies, docs, tickets, reports, plans.

## Quick start

1. Install the set: `npx skills add adhamhaithameid/write-skills`
2. Start a session and ask your agent to write anything.
3. Watch the reply land on the first read.

## The skills

### Chat and replies

| Skill | Use for |
|---|---|
| write-better | The general floor: reader levels, sentence rules, AI patterns, reader load. |
| write-compact | Brief replies on request. The whole reply stays short. |
| write-tldr | A short block at the end of a long answer: TLDR plus what was found. |
| write-again | Rewrite the last output, explain a failed answer again, or refresh a stale doc. |
| help-write | Ask in chat which skill fits the task; it routes and follows. |

### Code

| Skill | Use for |
|---|---|
| write-commit | Commit message from the staged diff and the repository history. |
| write-pr | PR title and description from the change and the evidence. |
| write-comments | Code comments that state intent, constraints, and invariants. |
| write-review | Review comments on a diff: location, problem, fix. |

### Product and planning

| Skill | Use for |
|---|---|
| write-plan | A plan before work starts: goal, approaches, steps, risks. |
| write-adr | Architecture decision records: context, decision, consequences. |
| write-prd | Product requirements: problem, goals, testable requirements, metrics. |
| write-jira | Jira epics, stories, and story points from a plan. |
| write-issue | GitHub issues and bug reports with reproduction steps. |
| write-release | Release notes from git history. |

### Knowledge

| Skill | Use for |
|---|---|
| write-docs | READMEs, tutorials, reference pages, RFCs, and documents an agent reads. |
| write-summary | Summaries of threads, docs, logs, and meetings that keep the facts. |
| write-report | Status updates, incident reports, and findings for a decision-maker. |
| write-handoff | Handoff notes so work continues in a fresh session. |
| write-longform | A staged long-form mission: collect raw material, then build the article. |
| write-glossary | Build or clean a glossary, one term per concept. |
| write-ste | Enforce Simplified Technical English on any text, violations named by rule. |

## See the difference

Three samples. The full gallery covers every skill in `docs/examples.md`. The pairs are hand-written examples of the rules, not recorded sessions.

write-better, a chat answer:

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

## Your rules win

Every skill reads your local rule files first: `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and `GLOSSARY.md`. Your glossary terms and repo conventions beat the skill defaults. The skills never edit those files.

## Install

The skills CLI detects your agent and installs into the right folder:

```
npx skills add adhamhaithameid/write-skills
```

Install one skill:

```
npx skills add adhamhaithameid/write-skills --skill write-better
```

Install the npm package and copy a skill folder into your agent's skills folder:

```
npm install write-skills
```

| Agent | Skills folder |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.agents/skills/` |
| Any other agent | your agent's skills folder |

Or copy a folder from `skills/` by hand. Each skill folder holds everything the skill uses. No skill needs another skill.

## Output language

Every skill writes its prose output in ASD-STE100 Simplified Technical English. Each skill carries its own copy of the rules in `references/ste.md`.

## Docs

- [docs/BLOCKS.md](docs/BLOCKS.md): the manifest and the set cap.
- [docs/examples.md](docs/examples.md): the before-and-after gallery.
- [docs/STATE.md](docs/STATE.md): what the set is, skill by skill.
- [docs/AUDIT.md](docs/AUDIT.md): the 24-check rubric scores.
- [docs/EVALS.md](docs/EVALS.md): the behavior evidence.

## Check the repo

Run these commands from the repo root:

```
python3 tools/check.py
python3 -m unittest discover -s tests
```

The check script tests frontmatter, links, private data, synced rule copies, and the style of the files that this repo authors.

## Contribute

Read `CONTRIBUTING.md` first.
