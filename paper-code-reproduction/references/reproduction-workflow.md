# Reproduction Workflow

Use this checklist to keep the reproduction compact, code-first, and easy to study.

## 1. Intake

- Confirm the target PDF.
- Keep the PDF and original source files under `paper_src/` when project rules allow it.
- Create the workspace with `scripts/scaffold_reproduction_workspace.py`.
- Run `scripts/inspect_pdf.py` only when a PDF candidate log is useful.
- Keep the top level limited to `paper_src/`, `code/`, `results/`, `README.md`, and `notes.md` unless a real need appears.

## 2. Reading order for the user

Write this into `README.md` and keep it current:

1. `README.md`: target, runnable command, current status, next step.
2. `notes.md`: paper method, equations, assumptions, missing details, deviations.
3. `code/`: implementation, starting from the runnable entry point named in `README.md`.
4. `results/`: metrics, figures, logs, and comparison evidence.
5. `report.md`: only when there are non-trivial quantitative comparisons or discrepancies.

## 3. Paper parsing checklist

Extract only the details needed for the first runnable target:

- full title and year,
- problem statement,
- domain and application,
- data source or simulator,
- input and output representation,
- model or numerical method,
- loss/objective and constraints,
- training or solver schedule,
- evaluation metrics,
- baselines,
- first figure, table, metric, or behavior to reproduce.

## 4. Reproduction plan checklist

Before implementation, answer in `README.md` or `notes.md`:

- What is the minimum end-to-end baseline?
- What assets are missing?
- Which settings are explicit in the paper?
- Which settings must be inferred?
- Which result is the highest-value first target?

## 5. Code organization

- Put all implementation under `code/`.
- Put config files under `code/configs/` only when configs are needed.
- Put code-local tests under `code/tests/` only when they are useful.
- Do not create top-level `src/`, `scripts/`, `runs/`, or `configs/` by default.
- Put metrics, generated summaries, figures, and logs under `results/`.

## 6. Execution ladder

Run work in this order:

1. Intake summary
2. Equation and metric recovery
3. Data/code audit
4. Minimal baseline implementation
5. Smoke run
6. Metric verification
7. Paper-faithful or proxy run
8. Gap analysis

## 7. Reporting standard

Keep reporting compact. `README.md` plus `notes.md` is enough until real experiment results require `report.md`.

Every final handoff should include:

- target claim,
- runnable command,
- evidence produced,
- mismatch summary,
- reproduction tier,
- most likely blockers,
- next experiment recommendation.
