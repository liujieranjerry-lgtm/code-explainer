# Code Explainer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-blue.svg)](skills/code-explainer/SKILL.md)
[![Frontmatter validated](https://img.shields.io/badge/frontmatter-validated-success.svg)](scripts/validate_skills.py)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Code Explainer** 是一个生产级的 Agent Skill，专门教 AI Agent 如何给“聪明但没有编程基础”的学习者解释代码。它把代码讲成一段有逻辑、连贯的叙述，保留准确的代码标识符，同时用通俗类比降低理解门槛。

这个 Skill 默认面向中文学习者，但它的方法论是通用的，可以应用于任何代码。

## 快速开始

### 安装到 Codex

```bash
mkdir -p ~/.codex/skills
cp -r skills/code-explainer ~/.codex/skills/
```

### 安装到 Claude Code

```bash
mkdir -p ~/.claude/skills
cp -r skills/code-explainer ~/.claude/skills/
```

### 作为 Claude Code 插件安装

```text
/plugin marketplace add https://github.com/liujieranjerry-lgtm/code-explainer
/plugin install code-explainer@code-explainer
```

### 作为 Codex 插件安装

```bash
codex plugin marketplace add liujieranjerry-lgtm/code-explainer
codex plugin add code-explainer@code-explainer
```

### 使用 skills CLI 安装

```bash
npx skills add liujieranjerry-lgtm/code-explainer --skill code-explainer
```

安装后，当用户说出以下类似的话时，Skill 会自动触发：

- “解读代码”
- “解释代码”
- “分析代码”
- “这段代码是什么意思”
- “explain this code”
- “walk me through this code”
- “解释每个具体代码词”

## 这个 Skill 做什么

- 用连贯的叙述解释代码，而不是堆术语。
- 把准确的代码标识符保留在解释里。
- 说明代码是干什么的、怎么运行的、为什么重要。
- 支持“逐词解释”模式，方便用户逐个理解代码词。
- 保持亲切、清晰、有逻辑的语气，不居高临下。

## Skill 目录结构

```
skills/code-explainer/
├── SKILL.md                    # 必需入口文件
├── agents/openai.yaml          # Codex UI 元数据
├── references/method.md        # 详细方法、术语映射、示例
├── examples/                   # 输入代码 + 期望的解释风格
└── ...
```

完整规范见 [docs/skill-anatomy.md](docs/skill-anatomy.md)。

## 质量与校验

仓库自带零依赖校验脚本：

```bash
python3 scripts/validate_skills.py
```

它会检查：

- `name` 是否为小写连字符格式，不超过 64 个字符，且与目录名一致。
- `description` 是否非空、不超过 1024 个字符，并包含触发关键词。
- 每个 Skill 目录是否存在 `SKILL.md`。
- `SKILL.md` 正文是否控制在 500 行以内（超出仅警告）。

运行测试：

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

GitHub Actions 会在每次 push 和 pull request 时自动运行这两条命令。

## 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

MIT
