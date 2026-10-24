# write-skills

Eight agent skills for writing. Each skill works alone. Install one skill or all of them.

## Skills

| Skill | Use for |
|---|---|
| write-core | Chat answers, explanations, status updates, bug reports. Reader levels, depth, sentence rules, AI patterns. |
| write-compact | Brief replies on request, or explain a confusing reply again. |
| write-docs | READMEs, tutorials, how-to guides, reference pages, explanations, RFCs, and documents an agent reads. |
| write-pr | PR title and description from the change and the evidence. |
| write-commit | Commit message from the staged diff and the repository history. |
| write-comments | Code comments that state intent, constraints, and invariants. |
| write-jira | Jira epics, stories, and story points from a plan. |
| write-longform | A staged long-form mission: collect raw material, then build the article. |

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

The check script tests frontmatter, links, private data, and the style of the files that this repo authors.

## Contribute

Read `CONTRIBUTING.md` first.
