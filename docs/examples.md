# Example gallery

One before-and-after pair per skill. The pairs are hand-written examples of each rule set, not recorded sessions. Each skill folder carries its own example, and its `evals/` folder turns the same scenario into a testable case.

## write-better

Before:
```text
Sure! I'd be happy to help. In order to boost your productivity, this
robust tool leverages cutting-edge caching to deliver a seamless
experience.
```

After:
```text
The tool caches your queries. A repeat query answers in 12 ms. A cold
query answers in 340 ms.
```

## write-compact

Before:
```text
Certainly! Let me explain. The issue you're experiencing is likely caused
by a misconfiguration of your authentication settings.
```

After:
```text
Auth fails. The token check reads the wrong claim. Fix in auth.ts line 40:
```

## write-docs

Before:
```text
Configuration of the retry behavior for the mail client is performed via
client.json. Note that it's important to remember that running with
--dry-run will output what would have been sent.
```

After:
```text
`mail.ts` reads the retry count and the delay from `client.json`. Each
retry waits twice as long as the one before it. Run `mail.ts --dry-run` to
print the messages without sending them.
```

## write-pr

Before:
```text
This PR makes several improvements to the authentication system and
cleans up a number of related issues that we noticed during testing.
```

After:
```text
## Summary
Reject expired session tokens at the login endpoint. Users stayed logged
in after a password reset.

## Evidence
- Before: the reset test fails on main. The token stays valid.
- After: the reset test passes. The token gets a 401.

## Risk
- Door: two-way. A revert restores the old check.
- Blast radius: login only. No other token check changes.
```

## write-commit

Before, a repo whose history reads "Docs: fix typo", "Parser: handle empty lines":
```text
feat(queue): add RetryQueue class with capacity limit and item list
```

After, the convention discovered from the history:
```text
Queue: add RetryQueue class
```

## write-comments

Before:
```ts
// increment i by one
i++;
```

After:
```ts
// Skip the header row, which the parser keeps in the array.
i++;
```

## write-review

Before:
```text
I noticed that the error handling here could probably be improved. Also,
nice work on the tests!
```

After:
```text
src/auth.ts:41 risk. A null user throws on the reset path. Check the user
before the token load.
src/auth.ts:58 nit. The number 3 is the retry cap. Name it.
src/auth.test.ts question. No test covers the reset path. Skipped on
purpose?
```

## write-jira

Before:
```text
BE-1 Backend table (3)   BE-2 Upload endpoint (5)   WEB-1 Button (5)
```

After:
```text
Title: A user attaches a file to a task on the web

Story: As a task owner, I attach a file from the web app, so that the file
stays with the task.

Acceptance criteria:
- [ ] POST /tasks/{id}/attachments saves the file and the record.
- [ ] The web task view lists the file name and size after the upload.

Blocked by: none

Points: 5
Points reason: one table, one endpoint, and one screen in a single slice.
```

## write-issue

Before:
```text
Export is broken for me. It just fails sometimes, probably a size thing.
```

After:
```text
Title: Export fails for datasets larger than 50000 rows

Steps to reproduce:
1. Load the sample dataset with 60000 rows.
2. Click Export.
3. Wait 60 seconds.

Expected: a CSV file downloads.
Actual: no file, no error. The console shows the line below.

Evidence: "Uncaught RangeError: Invalid array length" at export.ts:214.
```

## write-release

Before:
```text
a1b2c3 refactor: move helpers
d4e5f6 fix: off-by-one in budget check
7890ab feat(api): add retry on 429
```

After:
```text
## Fixed
- Budget checks no longer fail on the first day of a month. (#412)

## Added
- The API retries a request once when the server answers 429. (#390)
```

## write-report

Before:
```text
We looked into the latency problem and did some analysis. It seems like
there might be some issues with the database, though more investigation
is probably needed.
```

After:
```text
Answer: the checkout latency doubled after the 2.6 deploy. Roll back the
query change in PR 881 today.

Evidence:
- Latency is 480 ms at the 95th percentile. It was 120 ms on 2026-10-20.
  Source: the dashboard, 7-day window.
- PR 881 moved the discount lookup into the order query. The plan count
  went from 1 to 14.

Confidence: high. The rollback restores the old plan.
```

## write-summary

Before: forty messages of a release thread.

After:
```text
Gist: the team delayed release 2.6 to fix the sync bug first.

Decisions:
- Delay 2.6 by one week. Owner: Mona.
- Freeze scope today. Owner: Priya.

Numbers:
| Metric | Value |
|---|---|
| Affected users | 340 |
| Sync failure rate | 2.1 percent |

Open questions:
- Who staffs the hotfix? No owner yet.
```

## write-handoff

Before: the last hour of a session, from memory.

After:
```text
Where the work stands: repo writing-tools, branch fix/login-test, commit
9c31aa. No pull request yet.

Done: the login test waits for the session cookie. Proof: 214 tests pass.

Verified: the test run. Not verified: the retry flake, untouched.

Next steps:
1. Rename the helper in src/auth.ts.
2. Push the branch and open a pull request.

Traps: do not touch the cache module. The flake there is a known issue.
```

## write-longform

Before, a fragment in the pile:
```text
---
something about how retries feel like a treadmill, work this out later
```

After, the grounded beat it became:
```text
Retries hide the failure instead of fixing it. The queue drains, the
error count stays at zero, and the broken consumer never gets a ticket.
That is the trade: calm dashboards, slower truth.
```

## write-glossary

Before, terms scattered across three docs:
```text
readme: "the gateway service"
docs/api.md: "the edge proxy"
team chat: "the front door"
```

After:
```text
| Term | Meaning | Used in |
|---|---|---|
| gateway | The service that routes requests to the backends. | readme, api docs |
| edge proxy (merged) | Old name for the gateway. | api docs before 2026-09 |
```

## write-tldr

Before, a 60-line migration answer ends with nothing.

After, the same answer ends with:
```text
TLDR: Run scripts/migrate-login.ts once, then deploy. Rollback: restore
the users.email column before the next release.
Found: The retry helper in queue.py double-counts failures. No ticket yet.
```

## write-plan

Before:
```text
We should improve search. First we profile, then look at options, then
implement. We will iterate as needed.
```

After:
```text
Goal: search answers in 200 ms or less at 10000 rows. Approaches: the
index (recommended), a search engine, caching. Steps: add the index on
staging, load-test, ship. Risk: writes slow; watch insert time.
```

## write-adr

Before:
```text
We talked about caching and decided to use Redis. We might revisit later.
```

After:
```text
# 0012. Store sessions in Redis
Status: Accepted
Context: 40000 sessions lost on every deploy. Rejected: sticky balancer,
Postgres.
Decision: We will store user sessions in Redis with a 7-day TTL.
Consequences: deploys keep sessions. One more service to run.
```

## write-prd

Before:
```text
We need better notifications. It should be flexible and robust.
```

After:
```text
Problem: 62 percent of September tickets asked where an order is after an
unreported delay. Goal: users learn of a change in 60 s or less.
Non-goals: email digests, partner APIs.
Metric: ticket count, baseline 340 per month, target 100.
```

## write-again

Before, the same failed explanation repeated.

After:
```text
New example, same mechanism. A coffee shop takes orders. One worker
remakes a lost order; the queue grows. Retries work the same way.
Next step: say which part is unclear, the policy or the queue.
```

## write-ste

Before:
```text
Utilization of the retry mechanism should be avoided in scenarios where
the upstream dependency has been observed to exhibit flakiness.
```

After:
```text
Do not retry when the upstream dependency is flaky.
```
