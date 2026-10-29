# Routing test fixture

Run this test with fresh agents before adding a twenty-third skill, and after any description change. Two runs. Compare against the expected answers below.

## Prompt, part A (should fire)

Send this to a fresh agent, verbatim:

```text
You are an agent host with 22 installed writing skills: write-better,
write-compact, write-tldr, write-again, help-write, write-docs, write-pr,
write-commit, write-comments, write-review, write-jira, write-issue,
write-release, write-report, write-summary, write-handoff, write-plan,
write-adr, write-prd, write-longform, write-glossary, write-ste. Each
skill has a "Use when" description matching its name. For each task, name
the one skill that fires, or "none". Format: "FIRE n: name-or-none".

1. Write the PR description for this branch.
2. Explain that again, I'm lost.
3. Record the decision about the queue as an ADR.
4. Give me a TLDR of what you just did.
5. Run the test suite and report failures.
6. Deploy the staging build.
7. Write a plan for migrating the auth service.
8. Summarize this 200-line log file.
9. Rotate the API key in the vault.
10. Which skill should I use to describe this endpoint to the team?
```

Expected: 1 write-pr, 2 write-again, 3 write-adr, 4 write-tldr, 5 none, 6 none, 7 write-plan, 8 write-summary, 9 none, 10 help-write.

## Prompt, part B (should fire nothing)

Send this to a fresh agent, verbatim:

```text
You are an agent host with the same 22 installed writing skills. For each
task, answer "OK n" if no skill fires; answer "MISFIRE n: name" if one
does.

1. Bump the dependency version and run the build.
2. Git rebase this branch onto main.
3. Print the current git branch and the last commit hash.
4. Warm up the application cache.
5. Set the git remote to the new URL.
6. Close the stale issues older than 90 days.
7. Rotate the application logs.
8. Scale the worker pool to 4 replicas.
9. Vacuum the database and report the table sizes.
10. Pin the base image to the new patch version.
```

Expected: OK for all ten.

## Status

- 2026-10-24: 8 descriptions, should-fire only, 16 of 16 over two samples. Recorded in docs/EVALS.md.
- 2026-10-29: the 22-skill run is pending. The provider refused the subagent dispatch three times in a row. Run the two prompts above and record the verdicts in docs/EVALS.md.
