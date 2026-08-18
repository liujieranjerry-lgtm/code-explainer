# Skill Anatomy

This repository follows the portable Agent Skills format used by high-star skill projects.

## File Location

```
skills/
  code-explainer/
    SKILL.md           # Required entry point
    agents/openai.yaml # Optional Codex UI metadata
    references/        # Deep reference material loaded on demand
    examples/          # Input code and expected explanation style
```

`SKILL.md` is the only required file for the skill to work. Add `references/` or `examples/` only when they carry material that would otherwise bloat the main file.

## Frontmatter

```yaml
---
name: code-explainer
description: What the skill does AND when to use it, including trigger keywords.
---
```

Rules:

- `name` is lowercase, hyphen-separated, <= 64 characters, and matches the folder name.
- `description` is the routing contract. It is the only text preloaded into context, so it must say what the skill does and when to activate it.
- Do not put process steps in the description. If the description summarizes the workflow, the agent may follow the summary instead of reading the full skill.

## Progressive Disclosure

1. Metadata: `name` + `description` are always in context.
2. Body: `SKILL.md` loads only when the skill triggers. Keep it under 500 lines.
3. References and examples: loaded only when needed.

## Writing Principles

- Narrative over glossary.
- Specific code identifiers over vague paraphrases.
- Concrete examples over abstract rules.
- Plain analogies connected back to real code.
- Anti-rationalization tables and verification checklists where behavior can drift.
