import importlib.util
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("check", HERE.parent / "tools" / "check.py")
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


def rules(text):
    return {r for _, r, _ in check.lint_text(text)}


class LintTests(unittest.TestCase):
    def test_clean_text_passes(self):
        self.assertEqual(check.lint_text("Use the short word. Write one idea in each sentence.\n"), [])

    def test_em_dash_fails(self):
        self.assertIn("dash", rules("This is wrong \u2014 very wrong.\n"))

    def test_curly_quote_fails(self):
        self.assertIn("curly-quote", rules("Do not use \u201cthis\u201d.\n"))

    def test_contraction_fails(self):
        self.assertIn("contraction", rules("Don't do this.\n"))

    def test_possessive_passes(self):
        self.assertNotIn("contraction", rules("Read the user's file.\n"))

    def test_long_sentence_fails(self):
        text = " ".join(["word"] * 30) + ".\n"
        self.assertIn("sentence-length", rules(text))

    def test_title_case_heading_fails(self):
        self.assertIn("title-case", rules("# Writing Style Slider\n"))

    def test_sentence_case_heading_passes(self):
        self.assertNotIn("title-case", rules("# Writing style slider\n"))

    def test_banned_word_fails_but_code_span_passes(self):
        self.assertIn("banned-word", rules("This is a robust tool.\n"))
        self.assertNotIn("banned-word", rules("Avoid the word `robust` in text.\n"))

    def test_frontmatter_is_skipped(self):
        text = '---\nname: a\ndescription: Some long description that runs past the twenty five word limit for sure yes indeed it does go on.\n---\nShort text.\n'
        self.assertEqual(check.lint_text(text), [])

    def test_code_fence_is_skipped(self):
        self.assertEqual(check.lint_text("```\nDon't \u2014 robust\n```\n"), [])


class RefTests(unittest.TestCase):
    def test_reference_forms_match(self):
        rx = check.skill_ref_regex("shape")
        for text in ("use `shape` now", "run /shape", "the shape skill", "**shape**", "$shape"):
            self.assertTrue(rx.search(text), text)

    def test_plain_word_does_not_match(self):
        rx = check.skill_ref_regex("shape")
        self.assertIsNone(rx.search("shape the article into paragraphs"))


class FrontmatterTests(unittest.TestCase):
    def test_parse_block_description(self):
        data, err = check.parse_frontmatter("---\nname: a\ndescription: >\n  one\n  two\n---\nbody\n")
        self.assertIsNone(err)
        self.assertEqual(data["description"], "one two")

    def test_missing_frontmatter(self):
        _, err = check.parse_frontmatter("no frontmatter")
        self.assertIsNotNone(err)


def make_repo(tmp, name="alpha", body="Short text.\n", extra_skill=None):
    repo = Path(tmp)
    (repo / "shared").mkdir()
    (repo / "shared" / "ste.md").write_text("ste rules\n", encoding="utf-8")
    (repo / "shared" / "local-rules.md").write_text("local rules\n", encoding="utf-8")
    (repo / "tools").mkdir()
    names = [name] + ([extra_skill] if extra_skill else [])
    (repo / "README.md").write_text(" ".join(names) + "\n", encoding="utf-8")
    for n in names:
        d = repo / "skills" / n
        (d / "references").mkdir(parents=True)
        (d / "SKILL.md").write_text(
            f"---\nname: {n}\ndescription: Does a thing.\n---\n{body}\n## Output language\nRules.\n",
            encoding="utf-8")
        (d / "references" / "ste.md").write_text("ste rules\n", encoding="utf-8")
        (d / "references" / "local-rules.md").write_text("local rules\n", encoding="utf-8")
    return repo


def fails_for(repo):
    return [str(f) for f in check.run_checks(repo)]


class SyncRegionTests(unittest.TestCase):
    def build(self, tmp, beta_body):
        repo = make_repo(tmp, body="<!-- sync:x start -->\nsame rule text\n<!-- sync:x end -->\n", extra_skill="beta")
        f = repo / "skills" / "beta" / "SKILL.md"
        f.write_text(f.read_text(encoding="utf-8").replace("same rule text", beta_body), encoding="utf-8")
        return repo

    def test_matching_regions_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertFalse(any("[sync]" in f for f in fails_for(self.build(tmp, "same rule text"))))

    def test_mismatched_regions_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(any("[sync]" in f for f in fails_for(self.build(tmp, "drifted rule text"))))


class RepoTests(unittest.TestCase):
    def test_good_repo_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(fails_for(make_repo(tmp)), [])

    def test_cross_reference_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp, body="Use `beta` first.\n", extra_skill="beta")
            self.assertTrue(any("[cross-ref]" in f for f in fails_for(repo)))

    def test_ste_copy_must_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp)
            (repo / "skills" / "alpha" / "references" / "ste.md").write_text("changed\n", encoding="utf-8")
            self.assertTrue(any("[ste]" in f for f in fails_for(repo)))

    def test_name_must_match_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp)
            f = repo / "skills" / "alpha" / "SKILL.md"
            f.write_text(f.read_text(encoding="utf-8").replace("name: alpha", "name: other"), encoding="utf-8")
            self.assertTrue(any("[frontmatter]" in x for x in fails_for(repo)))

    def test_privacy_term_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp, body="Written by someone.\n")
            (repo / "tools" / "blocklist.txt").write_text("plain: someone\n", encoding="utf-8")
            self.assertTrue(any("[privacy]" in x for x in fails_for(repo)))

    def test_notices_file_exempt_from_blocklist(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp)
            (repo / "THIRD_PARTY_NOTICES.md").write_text("Thanks to the caveman authors.\n", encoding="utf-8")
            (repo / "tools" / "blocklist.txt").write_text("legacy: caveman\nplain: someone\n", encoding="utf-8")
            self.assertFalse(any("[legacy-name]" in f or "[privacy]" in f for f in fails_for(repo)))

    def test_real_email_fails_noreply_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp, body="Mail me at a@b.com now.\n")
            (repo / "tools" / "blocklist.txt").write_text(
                "regex: [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\n", encoding="utf-8")
            self.assertTrue(any("[privacy]" in x for x in fails_for(repo)))
            f = repo / "skills" / "alpha" / "SKILL.md"
            f.write_text(f.read_text(encoding="utf-8").replace("a@b.com", "1+x@users.noreply.github.com"), encoding="utf-8")
            self.assertFalse(any("[privacy]" in x for x in fails_for(repo)))

    def test_broken_link_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp, body="See [x](references/missing.md).\n")
            self.assertTrue(any("[links]" in f for f in fails_for(repo)))

    def test_auto_invocation_flag_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = make_repo(tmp)
            f = repo / "skills" / "alpha" / "SKILL.md"
            f.write_text(f.read_text(encoding="utf-8").replace("description:", "disable-model-invocation: true\ndescription:"), encoding="utf-8")
            self.assertTrue(any("disable-model-invocation" in x for x in fails_for(repo)))


if __name__ == "__main__":
    unittest.main()
