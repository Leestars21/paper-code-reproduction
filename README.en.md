# Paper Code Reproduction

[中文](README.md) | English

This is a Codex skill for code-first paper reproduction. It is designed for scientific, machine learning, computational, and engineering papers. The goal is not to create a large reproduction archive, but to help users turn the core method from a paper into runnable, readable, and extensible code.

Project website: [Leestars21/paper-code-reproduction](https://github.com/Leestars21/paper-code-reproduction)

The skill package lives in `paper-code-reproduction/`.

## Features

- Starts from a local paper PDF and locks one high-value reproduction target.
- Creates a compact default workspace: `paper_src/`, `code/`, `results/`, `README.md`, and `notes.md`.
- Requires the generated README to explain the reading order for learning the reproduction.
- Keeps implementation, run entry points, configs, and code-local tests under `code/`.
- Records paper facts, assumptions, missing details, deviations, and reproduction tier.
- Supports exact, faithful, proxy, and partial reproduction modes.
- Includes scripts for scaffolding, PDF metadata inspection, and optional result dashboards.

## When to Use

Use this skill when you want to:

- reproduce the core algorithm, model, loss, experiment, or headline metric from a paper;
- understand a paper by implementing its method;
- build a faithful or proxy reproduction when original code or data is missing;
- keep a reproduction project small and easy to continue.

Do not use it for:

- generating a large reproduction archive or decorative dashboard by default;
- generic literature organization without a concrete target paper;
- bypassing access restrictions for papers, datasets, or code.

## Installation

### Option 1: Ask Codex to install it

You can ask Codex:

```text
Install the paper-code-reproduction skill from https://github.com/Leestars21/paper-code-reproduction into my Codex skills directory and validate it.
```

Codex will usually:

1. Open or clone [Leestars21/paper-code-reproduction](https://github.com/Leestars21/paper-code-reproduction).
2. Copy the repository's `paper-code-reproduction/` skill folder into the user's Codex skills directory.
3. Validate that the skill is usable.
4. Tell the user to start a new Codex chat or refresh the session if `$paper-code-reproduction` does not appear immediately.

### Option 2: Install manually

Open [Leestars21/paper-code-reproduction](https://github.com/Leestars21/paper-code-reproduction), download or clone the repository, then run this from the project directory:

```powershell
Copy-Item -Recurse .\paper-code-reproduction "$env:USERPROFILE\.codex\skills\paper-code-reproduction"
```

Optional: if you already have Codex's `skill-creator` tooling installed, you can run an advanced validation check with:

```powershell
conda run -n envpymc5 python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "$env:USERPROFILE\.codex\skills\paper-code-reproduction"
```

Expected output:

```text
Skill is valid!
```

Start a new Codex chat after installation if the skill does not appear immediately.

## Usage Examples

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

More examples:

- `examples/sample-requests.md`
- `examples/sample-requests.en.md`

## Project Structure

```text
paper-code-reproduction/
  SKILL.md
  agents/openai.yaml
  scripts/
  references/
```

Key files:

- `SKILL.md`: main skill instructions and trigger metadata.
- `agents/openai.yaml`: Codex UI metadata.
- `scripts/scaffold_reproduction_workspace.py`: creates the compact reproduction workspace.
- `scripts/inspect_pdf.py`: scans local PDF candidates and writes lightweight metadata.
- `scripts/generate_reproduction_dashboard.py`: optionally builds result dashboards after ledgers exist.
- `references/`: on-demand references for workflow, scientific ML checks, domain playbooks, and visual reporting.

## Validation

Validate skill metadata:

```powershell
conda run -n envpymc5 python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\paper-code-reproduction
```

Validate script syntax:

```powershell
python -m py_compile .\paper-code-reproduction\scripts\scaffold_reproduction_workspace.py .\paper-code-reproduction\scripts\inspect_pdf.py .\paper-code-reproduction\scripts\generate_reproduction_dashboard.py
```

Smoke-test the scaffold:

```powershell
python .\paper-code-reproduction\scripts\scaffold_reproduction_workspace.py --project-root .\_smoke_paper_repro
```

By default, it should only create `paper_src/`, `code/`, `results/`, `README.md`, and `notes.md`.

## Important Notes

- This skill treats the PDF as the primary evidence source, but it does not invent missing data, code, or experiment settings.
- If original data or official code is unavailable, downgrade the result to proxy or partial reproduction and state that clearly in README/notes.
- Do not commit paper PDFs, private data, model weights, training outputs, or sensitive materials to public repositories.
- Do not include API keys, private datasets, complete PDFs, personal information, or internal materials in public issues.

## Feedback

If you run into problems with installation, scaffolding, paper parsing, reproduction structure, baseline execution, or result recording, please send feedback to the author or open an issue/PR.

Useful feedback includes:

- operating system and Codex surface;
- paper type;
- target you wanted to reproduce;
- command or input that triggered the issue;
- error message, failure reason, or unexpected output structure.

## License

MIT License. See `LICENSE`.
