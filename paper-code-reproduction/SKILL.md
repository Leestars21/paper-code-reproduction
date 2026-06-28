---
name: paper-code-reproduction
description: Reproduce a scientific, machine learning, computational, or methods paper from one or more local PDF files with a compact code-first workflow. Use when the user places a paper PDF in a folder and asks Codex to rebuild the method, implement runnable code, understand equations or experiments, run a faithful or proxy baseline, document assumptions and gaps, and prioritize learning the paper's method over producing a large reproduction archive.
---

# Paper Code Reproduction

Help the user understand a paper by turning the method into runnable, inspectable code. Keep the workspace small and project-like by default. Add files and folders only when they directly support reading the paper, coding the method, running the baseline, comparing results, or explaining gaps.

The default deliverables are:

1. runnable baseline code,
2. a concise method/assumption note,
3. result evidence from smoke tests or experiments,
4. a README that tells the user the reading order for learning the reproduction.

Do not build a large report package, numbered admin tree, dashboard, artifact guide, or broad literature archive unless the user explicitly asks for it or real results make it useful.

## Core Rules

1. Treat the PDF as the primary source unless official code, data, or supplements are provided.
2. Reproduce one valuable target first: the core algorithm, one headline figure/table, one metric, or one model behavior.
3. Prefer the smallest faithful implementation before adding abstractions, sweeps, dashboards, or polished reports.
4. Separate exact paper facts from inferred implementation choices.
5. Record missing details, assumptions, substitutions, and deviations in one concise note instead of scattering them across many files.
6. Keep code readable enough that the user can study the method directly.
7. Do not call external reference skills. Use only this skill's scripts, references, and local project artifacts.

## First Move

1. Search the working directory for PDF files.
2. If there is exactly one plausible paper PDF, use it. If there are several, ask which one is the target.
3. Run `scripts/inspect_pdf.py` when lightweight PDF metadata or an intake summary will help.
4. Run `scripts/scaffold_reproduction_workspace.py --project-root <project-root> --paper <paper>` before substantial file creation.
5. Fill the top of `README.md` before coding: target, reading order, first runnable command, current status, and known gaps.

The default scaffold is intentionally small:

```text
paper_src/
code/
results/
README.md
notes.md
```

Use this meaning consistently:

- `paper_src/`: paper PDF, supplement, screenshots, and original source files.
- `code/`: all reproduction implementation, run entry points, configs, helper scripts, and code-local tests.
- `results/`: metrics, figures, logs, generated data summaries, and other run evidence.
- `README.md`: user-facing orientation, reading order, run command, current status.
- `notes.md`: paper facts, method sketch, equations, assumptions, missing information, and deviations.

Do not create top-level `src/`, `scripts/`, `runs/`, or `configs/` in reproduction projects by default. Put implementation modules, command entry points, experiment drivers, and configs under `code/`. Put logs and run artifacts under `results/`.

Create extra folders only when they are actually needed:

- `code/configs/` for reusable configuration files.
- `code/tests/` for reusable checks.
- `results/figures/` for generated plots.
- `results/logs/` for command logs or long-run logs.
- `data/` only when real, substitute, or generated datasets are too substantial to keep under `results/` and the project rules permit a separate data folder.
- `report.md` only when experiments produce enough evidence for a compact written report.

If a project-level `AGENTS.md` defines a different convention, follow it while preserving the compact code-first principle.

## README Reading Order

Every generated `README.md` must tell the user how to learn the reproduction:

1. Start with `README.md` for the target claim, reproduction tier, run command, and current status.
2. Read `notes.md` for the paper method, recovered equations, assumptions, missing details, and deviations from the paper.
3. Open `code/` to study the implementation, starting from the runnable entry point named in `README.md`.
4. Check `results/` for smoke-test output, metrics, figures, logs, and comparison evidence.
5. Read `report.md` only if it exists and there are non-trivial quantitative comparisons or discrepancies.

## Workflow

### 1. Intake and paper reading

Read the paper structurally and write concise notes in `notes.md`. Extract only what is needed to implement the first target:

- problem definition,
- inputs and outputs,
- model or numerical method,
- loss/objective and constraints,
- data source or simulation setup,
- training/evaluation protocol,
- metrics and baselines,
- exact equations and paper claims needed for the target.

Use `references/reproduction-workflow.md` as a checklist. If PDF text extraction is weak, combine direct PDF inspection, figure/table reading, equation transcription, appendix parsing, and manual summarization.

### 2. Lock the first reproduction target

Record the first target in `README.md` under a short "Target" section. Choose one of:

- core algorithm behavior,
- one headline figure,
- one headline table,
- one main metric claim,
- or a proxy target when original data/settings are unavailable.

Define target outputs, required metrics, acceptable proxies, success criteria, and untestable claims. Avoid trying to reproduce the whole paper before one defensible target runs.

### 3. Audit feasibility without creating bureaucracy

Keep these sections in `notes.md`:

- Paper facts
- Method sketch
- Equations and implementation notes
- Data/code availability
- Assumptions
- Missing information
- Reproduction tier
- Deviations from paper

Track missing data links, hidden preprocessing, split rules, random seeds, optimizer or scheduler settings, geometry/mesh/boundary condition details when relevant, domain assumptions, units, hardware, and runtime assumptions.

Classify the paper type and read only the relevant guidance:

- `references/scientific-ml-guidance.md` for scientific ML, computational science, physics-informed learning, inverse problems, surrogate models, or domain-constrained methods.
- `references/domain-playbooks.md` for branch-specific checklists.

### 4. Build the baseline

Implement the simplest faithful version first. Put all reproduction code under `code/`.

Implementation rules:

- Prefer direct, readable code over framework-heavy abstractions.
- Start with one clear runnable entry point such as `code/reproduce.py`, `code/run_baseline.py`, or an equivalent project-appropriate file.
- Put reusable modules below `code/` rather than creating a top-level `src/`.
- Put configuration below `code/configs/` only when configs are actually needed.
- Mirror the paper's notation and variable meanings when practical.
- Preserve units, coordinate conventions, tensor component order, geometry assumptions, and boundary/loading conditions explicitly.
- Add comments only where the paper-method or modeling intent is not obvious.

The code deliverable is mandatory. If the paper cannot run end-to-end because data or settings are missing, implement the largest verifiable subset and mark the remaining gap explicitly.

### 5. Verify and run experiments

Run small checks before long experiments:

- shape and unit sanity checks,
- one-batch forward pass,
- loss decomposition check,
- metric calculation check,
- train/validation leakage check,
- tiny-subset baseline when full data is unavailable.

Use this reproduction ladder:

1. smoke test,
2. minimal working baseline,
3. paper-faithful setting,
4. ablations needed to explain discrepancies,
5. sensitivity runs only when they clarify a gap.

Store result evidence in `results/`. Use `results/results.tsv` only after there are multiple comparable runs. Keep logs in `results/logs/` when they help the user continue or audit the run.

### 6. Report only what helps

Update `README.md` with:

- reading order,
- setup and run commands,
- what target was reproduced,
- current tier: exact, faithful, proxy, partial, or blocked,
- key result evidence,
- remaining gaps and next steps.

Create `report.md` only when there are quantitative comparisons or non-trivial discrepancies to explain. Generate dashboard pages or visual summaries only after meaningful result ledgers exist and the user would benefit from reviewable visual artifacts.

Distinguish reproduced, partially reproduced, non-reproduced, and untestable claims. For every mismatch, explain whether the likely cause is missing information, data mismatch, implementation uncertainty, numerical instability, insufficient compute, or possible paper inconsistency.

## Domain-Specific Checks

For scientific, engineering, medical, or domain-constrained papers, be strict about unit consistency, domain normalization, subject/specimen split leakage, temporal leakage, protocols, boundary or operating conditions, plausible parameter ranges, and domain plausibility.

If the paper predicts fields, curves, sequences, structures, or parameters, do not rely on a single scalar metric. Compare shape, peak value and location, monotonicity or hysteresis when relevant, area-under-curve or conservation-style quantities when meaningful, and qualitative output patterns.

## Handling Missing Data or Code

If official code or data is unavailable:

1. Search the paper for supplements, appendix links, GitHub URLs, dataset names, and benchmark references.
2. Record why the original asset is unavailable before using substitutes.
3. Keep substitute datasets or generated data separate from original-claim outputs.
4. Downgrade the reproduction tier when the substitute changes the scientific claim being tested.

## Visual Communication

Read `references/visual-reporting.md` before generating figures, scorecards, dashboard pages, or final visual summaries.

At minimum, label axes and units, distinguish paper results from reproduced results, choose plot types that match the comparison, explain each figure in nearby text, and avoid raw screenshots without interpretation.

## Bundled Resources

- `scripts/scaffold_reproduction_workspace.py`: create the compact code-first workspace and starter `README.md`/`notes.md`.
- `scripts/inspect_pdf.py`: find local PDFs, extract lightweight metadata, and create an intake summary when useful.
- `scripts/generate_reproduction_dashboard.py`: optionally build dashboard HTML and SVG charts from result ledgers after meaningful runs.
- `references/reproduction-workflow.md`: paper reading and target-locking checklist.
- `references/scientific-ml-guidance.md`: scientific ML, physics, engineering, and domain-constrained checks.
- `references/domain-playbooks.md`: branch-specific guidance for PINNs, surrogates, inverse problems, structured scientific models, and related paper types.
- `references/visual-reporting.md`: figure and report presentation guidance.

## Output Standard

A good run leaves behind a compact folder where the user knows the reading order, can open the code, run the baseline, inspect the evidence, and understand what paper details are exact, inferred, missing, or substituted.
