# Code Explainer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](skills/code-explainer/SKILL.md)
[![Frontmatter validated](https://img.shields.io/badge/frontmatter-validated-success.svg)](scripts/validate_skills.py)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Code Explainer** is a production-grade Agent Skill that teaches AI agents how to explain code to smart learners with no programming background. It turns code into one logical, readable narrative, keeps exact code identifiers visible, and uses plain analogies without losing technical precision.

The skill is written for Chinese-speaking learners by default, but the method is language-neutral and can be applied to any codebase.

## Quick Start

### Install into Codex

```bash
mkdir -p ~/.codex/skills
cp -r skills/code-explainer ~/.codex/skills/
```

### Install into Claude Code

```bash
mkdir -p ~/.claude/skills
cp -r skills/code-explainer ~/.claude/skills/
```

### Install with the open skills CLI

```bash
npx skills add liujieranjerry-lgtm/code-explainer --skill code-explainer
```

After installation, the skill triggers automatically when a user says things like:

- "解读代码"
- "解释代码"
- "分析代码"
- "explain this code"
- "walk me through this code"
- "解释每个具体代码词"

## What This Skill Does

- Explains code in a coherent narrative, not a glossary dump.
- Weaves exact code identifiers into the explanation.
- Covers what the code is for, how it runs, and why it matters.
- Supports word-by-word mode when the user asks for it.
- Keeps the tone warm and accessible without being condescending.

## Skill Anatomy

```
skills/code-explainer/
├── SKILL.md                    # Required entry point
├── agents/openai.yaml          # Codex UI metadata
├── references/method.md        # Deep method, term mappings, worked examples
├── examples/                   # Input code + expected explanation style
└── ...
```

See [docs/skill-anatomy.md](docs/skill-anatomy.md) for the full authoring standard used by this repository.

## Quality and Validation

The repository ships a zero-dependency validator:

```bash
python3 scripts/validate_skills.py
```

It checks:

- `name` is hyphen-case, <= 64 characters, and matches the folder name.
- `description` is non-empty, <= 1024 characters, and contains trigger keywords.
- `SKILL.md` exists in every skill folder.
- The body stays under 500 lines (warning only).

Run the tests:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

GitHub Actions runs both commands on every push and pull request.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
