#!/usr/bin/env python3
"""Validate the structure and frontmatter of every skill in this repository."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
RESERVED_NAMES = {"anthropic", "claude"}
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    if not text.startswith("---"):
        return None, "missing YAML frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "unterminated YAML frontmatter"
    fields: dict[str, str] = {}
    for line in parts[1].splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields, None


def validate_skill(skill_dir: pathlib.Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        return [f"{skill_dir}: missing SKILL.md"], warnings

    text = skill_md.read_text(encoding="utf-8")
    fields, fm_error = parse_frontmatter(text)
    if fm_error:
        return [f"{skill_md}: {fm_error}"], warnings
    if fields is None:
        return [f"{skill_md}: missing YAML frontmatter"], warnings

    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()

    if not name:
        errors.append(f"{skill_md}: frontmatter 'name' is required")
    elif len(name) > 64:
        errors.append(f"{skill_md}: name is longer than 64 characters")
    elif not NAME_RE.match(name):
        errors.append(f"{skill_md}: name must be lowercase hyphen-case")
    elif name != skill_dir.name:
        errors.append(f"{skill_md}: name '{name}' does not match folder '{skill_dir.name}'")
    if name in RESERVED_NAMES:
        errors.append(f"{skill_md}: name '{name}' is reserved")

    if not description:
        errors.append(f"{skill_md}: frontmatter 'description' is required")
    elif len(description) > 1024:
        errors.append(f"{skill_md}: description is longer than 1024 characters")

    body_lines = len(text.splitlines())
    if body_lines > 500:
        warnings.append(f"{skill_md}: body is {body_lines} lines; consider moving material to references/")

    return errors, warnings


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"error: no skills directory at {SKILLS_DIR}")
        return 1

    all_errors: list[str] = []
    all_warnings: list[str] = []
    skill_count = 0

    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        if not (skill_dir / "SKILL.md").is_file():
            continue
        skill_count += 1
        errors, warnings = validate_skill(skill_dir)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    if skill_count == 0:
        print("error: no skills found")
        return 1

    for warning in all_warnings:
        print(f"warning: {warning}")
    for error in all_errors:
        print(f"error: {error}")

    print(f"validated {skill_count} skill(s); {len(all_errors)} error(s), {len(all_warnings)} warning(s)")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
