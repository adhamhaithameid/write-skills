# Contributing

## Before you commit

Run both commands. Both must pass.

```
python3 tools/check.py
python3 -m unittest discover -s tests
```

To run them on every commit, run `git config core.hooksPath .githooks` once. The `commit-msg` hook in that folder then runs the STE lint on your commit message and fails the commit on a finding.

You can lint any file on demand:

```
python3 tools/check.py --lint FILE
```

## Rules for edits

- Edit `shared/ste.md` to change the STE rules. Never edit `references/ste.md` inside a skill. Then run `python3 tools/check.py --fix-shared`.
- Wrap rule text that appears in more than one skill in `<!-- sync:NAME start -->` and `<!-- sync:NAME end -->` markers. The check fails when copies differ. Edit every copy together.
- Change `docs/BLOCKS.md` first when the set of skills changes.
- Update `docs/STATE.md` in the same commit as any change to the set.
- Update the README skill table in the same commit too. It renders on GitHub, npm, and skills.sh.
- List every authored markdown file in `tools/config.json` under `lint_paths`.
- Keep each skill alone. Do not name another skill inside a skill folder.
- Keep every skill auto-invoked. Do not add `disable-model-invocation`.
- Keep private data out of the repo. Add new private names to `tools/blocklist.txt`.
- Write the files that this repo authors in Simplified Technical English. The file `tools/config.json` lists these files. The lint checks the mechanical rules: banned words and phrases, the 25-word cap (20 words in numbered steps), passive voice, and "-ing" verbs. It also catches contractions, dashes, and curly quotes.
- A line that carries `<!-- ste:ok: reason -->` is exempt from the lint. Use it only when a rule allows the text, for example a passive with an unknown actor. Write the reason beside the marker.
- Use `docs/RULES.md` as the register of rules. Add a rule there first.
