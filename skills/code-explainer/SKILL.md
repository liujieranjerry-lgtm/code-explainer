---
name: code-explainer
description: Explains code in plain, logical Chinese for smart learners without a programming background. Use when the user says 解读代码, 解释代码, 分析代码, 这段代码是什么意思, explain this code, interpret this code, walk me through this code, or asks for a beginner-friendly code walkthrough. Also use when the user wants each specific code identifier explained.
---

# Code Explainer

## Overview

Turn code into a readable narrative that a smart non-programmer can follow without losing the code itself. The explanation must feel like one connected story, not a lecture or a list of unrelated facts.

## When to Use

- The user asks to "解读代码", "解释代码", "分析代码", or "看懂这段代码".
- The user says "explain this code", "interpret this code", or "walk me through this code".
- The user selects a code snippet and asks what it does or how it works.
- The user asks for "每个代码词解释一下" or a word-by-word breakdown.
- The user is learning and has no programming background, but is smart and capable.

Do NOT use this skill for a code review, a bug diagnosis, or a refactoring recommendation unless the user explicitly asks for explanation as the primary goal.

## Output Style

- Use one coherent logical paragraph by default, weaving exact code identifiers into the prose with backticks.
- Do not switch to tables, lists, or separate glossaries unless the user explicitly asks for a word-by-word breakdown.
- Begin with what the whole code is for, then walk through how it runs, then explain why it matters.
- Use plain analogies for technical terms, then immediately connect the analogy back to the actual code.
- When a technical term appears, explain it at that point instead of dumping unrelated jargon.
- If the user asks for two code snippets together, explain them as one connected system, not two separate mini-essays.

## Core Method

1. Identify the code's role in the larger system: interface, tool definition, loop, conversion layer, event handler, error handling, etc.
2. Name the concrete code identifiers in execution order.
3. Translate each identifier into a real-world role: contract, dictionary, promise, event stream, callback, observer, etc.
4. Trace the full flow in one narrative, using the exact code tokens.
5. End with one sentence that summarizes what the code does and why it matters.

## Word-by-Word Mode

When the user asks for "每个具体代码词解释一下":

- Keep each explanation to one or two sentences.
- Group terms by stage: entry, data preparation, loop, model call, tool execution, ending.
- Use exact backticked code tokens as labels.
- Do not omit identifiers the user selected.
- Preserve the same plain-language tone instead of becoming more technical.

## Common Mistakes

| Mistake | Correct behavior |
|---|---|
| Starting with a table or glossary by default | Start with one narrative paragraph; use lists only when explicitly requested |
| Replacing code tokens with vague words like "那个方法" or "这个字段" | Keep the exact identifiers in backticks and explain them in context |
| Explaining programming syntax without explaining what the code is for | First state the role, then trace the flow |
| Over-abstracting into a general programming lesson | Explain the specific code the user selected |
| Using a condescending tone | Assume the learner is smart but lacks experience |

## Red Flags

- The answer becomes a wall of technical definitions instead of a story.
- The user's exact code identifiers disappear from the explanation.
- The explanation is correct about syntax but never says why the code matters.
- The answer switches to a table after the user asked for "像刚才那样解读".

## Verification

Before finishing, confirm:

- [ ] The explanation starts with the code's role in the system.
- [ ] Every user-selected identifier is either explained in context or covered in word-by-word mode.
- [ ] The flow follows the actual execution order.
- [ ] The ending states why the code matters.
- [ ] The tone is plain, warm, and logical, not condescending.

## References

For the narrative template, common term mappings, and worked examples, read `references/method.md`.

## Examples

- `examples/example-interface.ts` and `examples/example-interface.explained.md` show how to explain an interface.
- `examples/example-loop.ts` and `examples/example-loop.explained.md` show how to explain a loop.
