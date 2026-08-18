# AGENTS.md

This repository is a single production-grade Agent Skill.

## Working Here

- Keep the authoritative skill at `skills/code-explainer/SKILL.md`.
- Keep deep material in `skills/code-explainer/references/`.
- Keep worked examples in `skills/code-explainer/examples/`.
- Run `python3 scripts/validate_skills.py` before committing.
- Run `python3 -m unittest discover -s tests -p "test_*.py"` before committing.
- Update the root `README.md` when the install path or behavior changes.
- Do not create a `README.md` inside the skill folder; repository-level docs belong at the repo root.
