# Contributing

Thanks for helping improve this skill.

## How to Contribute

1. Fork the repository.
2. Create a branch for your change.
3. If you are updating the skill, keep the change inside `skills/code-explainer/`.
4. Run the validator and tests:

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -p "test_*.py"
```

5. Open a pull request with a clear description.

## Skill Quality Rules

- Keep `SKILL.md` under 500 lines.
- Keep the `description` under 1024 characters.
- Preserve the narrative-first output style.
- Move deep reference material into `references/`.
- Add a worked example when you add a new mode or rule.
- Keep the skill self-contained under `skills/code-explainer/`.
