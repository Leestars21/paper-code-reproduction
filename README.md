# Paper Code Reproduction

中文 | [English](README.en.md)

这是一个用于“代码优先复现论文方法”的 Codex skill。它面向科学、机器学习、计算方法和工程类论文，目标不是生成庞大的复现归档，而是帮助用户把论文中的核心方法整理成可运行、可阅读、可继续实验的代码项目。

Skill 本体位于 `paper-code-reproduction/` 目录。

## 功能

- 从本地论文 PDF 开始，锁定一个最有价值的复现目标。
- 默认创建紧凑目录：`paper_src/`、`code/`、`results/`、`README.md`、`notes.md`。
- 强制 README 写明阅读顺序，帮助用户知道先看哪里学习论文复现。
- 要求所有实现、运行入口、配置和代码局部测试归到 `code/`，避免顶层目录混乱。
- 记录论文事实、假设、缺失信息、偏离点和复现等级。
- 支持 exact / faithful / proxy / partial 等不同复现层级。
- 提供脚手架、PDF 元数据检查和可选结果 dashboard 生成脚本。

## 适用场景

- 想复现论文中的核心算法、模型、损失函数、实验设置或主要指标。
- 想通过写代码理解论文方法，而不是只做文献总结。
- 原始数据或代码缺失，需要构建 faithful 或 proxy 复现。
- 需要一个清晰、可继续维护的小型复现项目结构。

不适合用于：

- 直接生成完整论文复现大包、课程归档或复杂 dashboard。
- 还没有明确目标论文或复现目标的泛泛资料整理。
- 需要绕过论文、数据集或代码访问限制的场景。

## 安装方式

### 方式一：让 Codex 安装

你可以在 Codex 中说：

```text
请把这个仓库里的 paper-code-reproduction skill 安装到我的 Codex skills 目录，并验证它可用。
```

Codex 应执行：

1. 将仓库中的 `paper-code-reproduction/` skill 目录复制到用户的 Codex skills 目录。
2. 运行 `skill-creator` 的 `quick_validate.py` 验证 skill。
3. 如果当前对话里 `$paper-code-reproduction` 没有立即出现，提示用户新开对话或刷新会话。

### 方式二：手动安装

在本项目目录下执行：

```powershell
Copy-Item -Recurse .\paper-code-reproduction "$env:USERPROFILE\.codex\skills\paper-code-reproduction"
```

然后验证：

```powershell
conda run -n envpymc5 python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "$env:USERPROFILE\.codex\skills\paper-code-reproduction"
```

期望输出：

```text
Skill is valid!
```

如果安装后当前对话看不到该 skill，请新开 Codex 对话或刷新会话。

## 使用示例

```text
Use $paper-code-reproduction to reproduce the local paper PDF in this folder.
Focus on the core model behavior first and keep the project structure compact.
```

```text
Use $paper-code-reproduction to rebuild the method from this paper.
If the original dataset is unavailable, create a proxy baseline and clearly mark assumptions.
```

```text
Use $paper-code-reproduction to inspect the paper, scaffold the reproduction workspace, and implement the first runnable baseline.
```

更多示例见：

- `examples/sample-requests.md`
- `examples/sample-requests.en.md`

## 项目结构

```text
paper-code-reproduction/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
```

其中：

- `SKILL.md`：skill 主说明和触发规则。
- `agents/openai.yaml`：Codex UI 元数据。
- `scripts/scaffold_reproduction_workspace.py`：生成紧凑复现项目结构。
- `scripts/inspect_pdf.py`：扫描本地 PDF 候选并输出轻量元数据。
- `scripts/generate_reproduction_dashboard.py`：在有结果台账后生成可选 dashboard。
- `references/`：按需读取的复现流程、科学 ML 检查、领域 playbook 和视觉报告建议。

## 验证

验证 skill 元数据：

```powershell
conda run -n envpymc5 python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\paper-code-reproduction
```

验证脚本语法：

```powershell
python -m py_compile .\paper-code-reproduction\scripts\scaffold_reproduction_workspace.py .\paper-code-reproduction\scripts\inspect_pdf.py .\paper-code-reproduction\scripts\generate_reproduction_dashboard.py
```

脚手架烟测：

```powershell
python .\paper-code-reproduction\scripts\scaffold_reproduction_workspace.py --project-root .\_smoke_paper_repro
```

默认应只生成 `paper_src/`、`code/`、`results/`、`README.md`、`notes.md`。

## 重要注意事项

- 该 skill 会把 PDF 当作主要证据来源，但不会替用户确认未提供的数据、代码或实验细节。
- 当原始数据或官方代码不可得时，应降级为 proxy 或 partial 复现，并在 README/notes 中明确说明。
- 不要把论文 PDF、私有数据、模型权重、训练输出或敏感材料提交到公开仓库。
- 不要在 issue 中公开 API key、私有数据集、完整 PDF、个人信息或机构内部材料。

## 反馈

如果你在安装、脚手架、论文解析、复现目录结构、运行 baseline 或结果记录中遇到问题，欢迎向作者反馈建议或提交 issue/PR。

有用的反馈包括：

- 操作系统和 Codex 使用方式；
- 使用的论文类型；
- 你期望复现的目标；
- 触发问题的命令或输入；
- 错误信息、阻塞点或不合理的输出结构。

## License

MIT License. See `LICENSE`.
