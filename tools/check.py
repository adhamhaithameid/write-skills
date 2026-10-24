#!/usr/bin/env python3
"""Tier 1 checks for this skill set. Standard library only.

Run:  python3 tools/check.py
Fix:  python3 tools/check.py --fix-shared   (copy shared/ste.md into every skill)
Exit code 0 means all checks pass. Exit code 1 means at least one check failed.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

FOOTER_MARKER = "## Output language"
BANNED_WORDS = [
    "additionally", "crucial", "delve", "enduring", "enhance", "fostering",
    "garner", "interplay", "intricate", "pivotal", "showcase", "tapestry",
    "testament", "underscore", "vibrant", "seamless", "seamlessly", "robust",
    "powerful", "streamline", "empower", "utilize", "leverage", "facilitate",
]
BANNED_PHRASES = [
    "i hope this helps", "let me know if", "great question", "certainly!",
    "of course!", "in order to", "it is important to note",
]
EMAIL_OK = re.compile(r"@users\.noreply\.github\.com$")


class Failure:
    def __init__(self, check, path, line, message):
        self.check, self.path, self.line, self.message = check, path, line, message

    def __str__(self):
        where = f"{self.path}:{self.line}" if self.line else f"{self.path}"
        return f"FAIL [{self.check}] {where} {self.message}"


# ---------------------------------------------------------------- helpers

def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def load_config(repo):
    cfg = {"style_skill": None, "lint_paths": [], "max_lines": {}, "default_max_lines": 500}
    p = repo / "tools" / "config.json"
    if p.exists():
        cfg.update(json.loads(p.read_text(encoding="utf-8")))
    return cfg


def skill_dirs(repo):
    root = repo / "skills"
    if not root.is_dir():
        return []
    return sorted(d for d in root.iterdir() if d.is_dir())


def parse_frontmatter(text):
    """Return (dict, error). Handles key: value and key: > block scalars."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, "file does not start with ---"
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, "frontmatter is not closed"
    data, key = {}, None
    for raw in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", raw)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            data[key] = "" if val in (">", "|", ">-", "|-") else val
        elif key and raw.startswith((" ", "\t")):
            data[key] = (data[key] + " " + raw.strip()).strip()
    return data, None


def strip_code_spans(line):
    return re.sub(r"`[^`]*`", "X", line)


def strip_examples(line):
    line = strip_code_spans(line)
    return re.sub(r'"[^"]*"', '""', line)


# ---------------------------------------------------------------- lint

def lint_text(text):
    """Return a list of (line_number, rule, message) for one authored file."""
    found = []
    in_fence = False
    block, block_start = [], 0
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break

    def flush():
        nonlocal block, block_start
        if block:
            joined = " ".join(block)
            joined = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", joined)
            joined = strip_code_spans(joined)
            joined = re.sub(r"[*_]{1,3}", "", joined)
            for sentence in re.split(r"(?<=[.!?])\s+", joined):
                words = re.findall(r"[\w'-]+", sentence)
                if len(words) > 25:
                    found.append((block_start, "sentence-length",
                                  f"{len(words)} words: {' '.join(words[:8])} ..."))
        block, block_start = [], 0

    for n, raw in enumerate(lines, 1):
        if raw.strip().startswith("```"):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if raw.lstrip().startswith("<!--"):
            flush()
            continue
        stripped = strip_code_spans(raw)
        if re.search(r"[\u2014\u2013]", stripped):
            found.append((n, "dash", "em dash or en dash: use a period, a comma, or a hyphen"))
        if re.search(r"[\u201c\u201d\u2018\u2019]", stripped):
            found.append((n, "curly-quote", "curly quote: use a straight quote"))
        plain = strip_examples(raw)
        if re.search(r"(?i)\b(?:\w+n't|\w+'(?:re|ve|ll|d|m)|(?:it|that|there|here|what|who|let|he|she)'s)\b", plain):
            found.append((n, "contraction", "contraction: write the full words"))
        low = plain.lower()
        for word in BANNED_WORDS:
            if re.search(rf"(?<![\w-]){word}(?![\w-])", low):
                found.append((n, "banned-word", f"banned word: {word}"))
        for phrase in BANNED_PHRASES:
            if phrase in low:
                found.append((n, "banned-phrase", f"banned phrase: {phrase}"))
        heading = re.match(r"^#{1,6}\s+(.*)$", raw)
        if heading:
            flush()
            words = re.findall(r"[A-Za-z][A-Za-z'-]*", heading.group(1))
            rest = [w for w in words[1:] if len(w) > 3]
            if len(words) >= 3 and len(rest) >= 2 and all(w[0].isupper() for w in rest):
                found.append((n, "title-case", "heading uses title case: use sentence case"))
            continue
        if raw.strip().startswith("|") or raw.strip() == "---" or not raw.strip():
            flush()
            continue
        if re.match(r"^\s*([-*]|\d+\.)\s+", raw):
            flush()
            raw = re.sub(r"^\s*([-*]|\d+\.)\s+", "", raw)
        if not block:
            block_start = n
        block.append(raw.strip())
    flush()
    return found


# ---------------------------------------------------------------- reference forms

def skill_ref_regex(name):
    n = re.escape(name)
    return re.compile(
        rf"(`/?\$?{n}`"
        rf"|(?<![\w-])[/$]{n}(?![\w-])"
        rf"|\*\*{n}\*\*"
        rf"|(?<![\w-]){n} skill(?![\w-])"
        rf"|(?<![\w-])skill {n}(?![\w-]))",
        re.IGNORECASE,
    )


def parse_blocklist(repo):
    entries = {"plain": [], "regex": [], "legacy": [], "skillref": []}
    p = repo / "tools" / "blocklist.txt"
    if not p.exists():
        return entries
    for raw in p.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        kind, _, value = raw.partition(":")
        kind, value = kind.strip(), value.strip()
        if kind in entries and value:
            entries[kind].append(value)
    return entries


# ---------------------------------------------------------------- checks

def check_structure(repo, fails):
    if not skill_dirs(repo):
        fails.append(Failure("structure", "skills/", 0, "no skill folders found"))
    for d in skill_dirs(repo):
        if not (d / "SKILL.md").exists():
            fails.append(Failure("structure", d.relative_to(repo), 0, "SKILL.md is missing"))


def check_frontmatter(repo, fails):
    for d in skill_dirs(repo):
        f = d / "SKILL.md"
        if not f.exists():
            continue
        data, err = parse_frontmatter(read_text(f) or "")
        rel = f.relative_to(repo)
        if err:
            fails.append(Failure("frontmatter", rel, 1, err))
            continue
        if data.get("name") != d.name:
            fails.append(Failure("frontmatter", rel, 2, f"name '{data.get('name')}' must equal folder '{d.name}'"))
        if not data.get("description"):
            fails.append(Failure("frontmatter", rel, 0, "description is empty"))
        if "disable-model-invocation" in data:
            fails.append(Failure("frontmatter", rel, 0, "remove disable-model-invocation: every skill must auto-invoke"))
        y = d / "agents" / "openai.yaml"
        if y.exists() and re.search(r"allow_implicit_invocation:\s*false", read_text(y) or ""):
            fails.append(Failure("frontmatter", y.relative_to(repo), 0, "allow_implicit_invocation must not be false"))


def check_ste(repo, fails):
    shared = repo / "shared" / "ste.md"
    if not shared.exists():
        fails.append(Failure("ste", "shared/ste.md", 0, "file is missing"))
        return
    for d in skill_dirs(repo):
        f = d / "SKILL.md"
        text = read_text(f) or ""
        if FOOTER_MARKER not in text:
            fails.append(Failure("ste", f.relative_to(repo), 0, f"missing '{FOOTER_MARKER}' section"))
        copy = d / "references" / "ste.md"
        if not copy.exists():
            fails.append(Failure("ste", copy.relative_to(repo), 0, "missing: run tools/check.py --fix-shared"))
        elif copy.read_bytes() != shared.read_bytes():
            fails.append(Failure("ste", copy.relative_to(repo), 0, "differs from shared/ste.md: run tools/check.py --fix-shared"))


def check_links(repo, fails):
    for d in skill_dirs(repo):
        for f in d.rglob("*.md"):
            text = read_text(f)
            if text is None:
                continue
            in_fence = False
            for n, line in enumerate(text.split("\n"), 1):
                if line.strip().startswith("```"):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                targets = re.findall(r"\]\(([^)\s]+)\)", line)
                targets += re.findall(r"`((?:references|scripts)/[\w./-]+)`", line)
                for t in targets:
                    if re.match(r"^(https?:|mailto:|#)", t):
                        continue
                    t = t.split("#")[0]
                    if not t:
                        continue
                    base = d if t.startswith(("references/", "scripts/")) and f.name == "SKILL.md" else f.parent
                    if not (base / t).exists() and not (d / t).exists():
                        fails.append(Failure("links", f.relative_to(repo), n, f"target does not exist: {t}"))


def check_cross_refs(repo, fails, blocklist):
    names = [d.name for d in skill_dirs(repo)]
    for d in skill_dirs(repo):
        others = [n for n in names if n != d.name]
        forbidden = others + blocklist["skillref"] + blocklist["legacy"]
        patterns = [(n, skill_ref_regex(n)) for n in forbidden]
        for f in d.rglob("*"):
            if not f.is_file():
                continue
            text = read_text(f)
            if text is None:
                continue
            for n, line in enumerate(text.split("\n"), 1):
                for name, rx in patterns:
                    if rx.search(line):
                        fails.append(Failure("cross-ref", f.relative_to(repo), n,
                                             f"reference to another skill: {name}"))


def iter_text_files(repo):
    skip_dirs = {".git", "tests", "__pycache__", ".opencode", ".zcode", "node_modules"}
    for f in repo.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(repo)
        if any(part in skip_dirs for part in rel.parts):
            continue
        if rel.as_posix() == "tools/blocklist.txt":
            continue
        if rel.as_posix() == "THIRD_PARTY_NOTICES.md":
            continue
        yield f, rel


SYNC_START = re.compile(r"^\s*<!--\s*sync:([A-Za-z0-9_-]+)\s+start\s*-->\s*$")
SYNC_END = re.compile(r"^\s*<!--\s*sync:([A-Za-z0-9_-]+)\s+end\s*-->\s*$")


def check_sync_regions(repo, fails):
    """A sync region carries the same rule text in every skill that embeds it."""
    regions = {}
    for d in skill_dirs(repo):
        for f in d.rglob("*.md"):
            text = read_text(f)
            if text is None:
                continue
            rel = f.relative_to(repo)
            buf, name = None, None
            for n, line in enumerate(text.split("\n"), 1):
                m = SYNC_START.match(line)
                if m and buf is None:
                    buf, name = [], m.group(1)
                    continue
                m = SYNC_END.match(line)
                if m:
                    if buf is None or m.group(1) != name:
                        fails.append(Failure("sync", rel, n, f"unexpected end marker for {m.group(1)}"))
                    else:
                        regions.setdefault(name, []).append((rel.as_posix(), "\n".join(buf)))
                    buf, name = None, None
                    continue
                if buf is not None:
                    buf.append(line.rstrip())
            if buf is not None:
                fails.append(Failure("sync", rel, 0, f"sync region '{name}' is not closed"))
    for rid, copies in regions.items():
        if len({t for _, t in copies}) > 1:
            where = ", ".join(p for p, _ in copies)
            fails.append(Failure("sync", where, 0, f"sync region '{rid}' differs across copies"))


def check_blocklist(repo, fails, blocklist):
    for f, rel in iter_text_files(repo):
        text = read_text(f)
        if text is None:
            continue
        for n, line in enumerate(text.split("\n"), 1):
            low = line.lower()
            for term in blocklist["plain"]:
                if term.lower() in low:
                    fails.append(Failure("privacy", rel, n, f"blocked term: {term}"))
            for term in blocklist["legacy"]:
                if re.search(rf"(?<![\w-]){re.escape(term.lower())}(?![\w-])", low):
                    fails.append(Failure("legacy-name", rel, n, f"old name: {term}"))
            for pat in blocklist["regex"]:
                m = re.search(pat, line)
                if m and not EMAIL_OK.search(m.group(0)):
                    fails.append(Failure("privacy", rel, n, f"blocked pattern match: {m.group(0)}"))


def check_git_authors(repo, fails):
    if not (repo / ".git").exists():
        return
    try:
        out = subprocess.run(["git", "-C", str(repo), "log", "--format=%ae%n%ce"],
                             capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return
    for email in sorted({e.strip() for e in out.splitlines() if e.strip()}):
        if not EMAIL_OK.search(email):
            fails.append(Failure("git-author", ".git", 0, f"commit email is not a noreply address: {email}"))


def check_size(repo, fails, cfg):
    for d in skill_dirs(repo):
        f = d / "SKILL.md"
        if not f.exists():
            continue
        limit = cfg["max_lines"].get(d.name, cfg["default_max_lines"])
        count = len((read_text(f) or "").split("\n"))
        if count > limit:
            fails.append(Failure("size", f.relative_to(repo), 0, f"{count} lines; the limit is {limit}"))


def check_lint(repo, fails, cfg):
    for rel in cfg["lint_paths"]:
        f = repo / rel
        if not f.exists():
            fails.append(Failure("lint", rel, 0, "file listed in tools/config.json does not exist"))
            continue
        for n, rule, msg in lint_text(read_text(f) or ""):
            fails.append(Failure(f"lint:{rule}", rel, n, msg))


def check_readme(repo, fails):
    readme = repo / "README.md"
    if not readme.exists():
        fails.append(Failure("readme", "README.md", 0, "file is missing"))
        return
    text = read_text(readme) or ""
    for d in skill_dirs(repo):
        if d.name not in text:
            fails.append(Failure("readme", "README.md", 0, f"skill not listed: {d.name}"))


def check_notices(repo, fails):
    for name in ("THIRD_PARTY_NOTICES.md", "LICENSE"):
        f = repo / name
        if f.exists() and "<FILL" in (read_text(f) or ""):
            fails.append(Failure("notices", name, 0, "placeholder <FILL ...> is still present"))


def run_checks(repo):
    repo = Path(repo)
    cfg = load_config(repo)
    blocklist = parse_blocklist(repo)
    fails = []
    check_structure(repo, fails)
    check_frontmatter(repo, fails)
    check_ste(repo, fails)
    check_links(repo, fails)
    check_cross_refs(repo, fails, blocklist)
    check_sync_regions(repo, fails)
    check_blocklist(repo, fails, blocklist)
    check_git_authors(repo, fails)
    check_size(repo, fails, cfg)
    check_lint(repo, fails, cfg)
    check_readme(repo, fails)
    check_notices(repo, fails)
    return fails


def fix_shared(repo):
    repo = Path(repo)
    shared = repo / "shared" / "ste.md"
    for d in skill_dirs(repo):
        dest = d / "references" / "ste.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(shared, dest)
        print(f"synced {dest.relative_to(repo)}")


def main(argv):
    repo = Path(__file__).resolve().parent.parent
    if "--fix-shared" in argv:
        fix_shared(repo)
    fails = run_checks(repo)
    for f in fails:
        print(f)
    print(f"\n{len(fails)} failure(s)." if fails else "All checks passed.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
