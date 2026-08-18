import importlib.util
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_skills.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_skills", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    sys.modules["validate_skills"] = module
    spec.loader.exec_module(module)
    return module


class ValidateSkillsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_validator()

    def test_valid_skill_passes(self):
        fixture = ROOT / "tests" / "fixtures" / "valid-skill"
        errors, warnings = self.module.validate_skill(fixture)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_missing_description_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = pathlib.Path(tmp) / "bad-skill"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text(
                "---\nname: bad-skill\n---\n\n# Bad Skill\n",
                encoding="utf-8",
            )
            errors, _ = self.module.validate_skill(skill_dir)
            self.assertTrue(any("description" in error for error in errors))

    def test_name_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill_dir = pathlib.Path(tmp) / "actual-name"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text(
                "---\nname: wrong-name\ndescription: Explain code for beginners.\n---\n",
                encoding="utf-8",
            )
            errors, _ = self.module.validate_skill(skill_dir)
            self.assertTrue(any("does not match folder" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
