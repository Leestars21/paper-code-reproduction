#!/usr/bin/env python3
"""Create a compact code-first workspace for a paper reproduction."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


CORE_DIRS = [
    "paper_src",
    "code",
    "results",
]


CORE_FILES = {
    "README.md": """# Paper Reproduction

## Target

- Paper:
- First reproduction target:
- Reproduction tier:
- Current status:

## Reading Order

1. Start here: `README.md` for the target, runnable command, current status, and next step.
2. Read `notes.md` for the paper method, recovered equations, assumptions, missing details, and deviations.
3. Open `code/` to study the implementation. Start from the runnable entry point listed below.
4. Check `results/` for smoke-test output, metrics, figures, logs, and comparison evidence.
5. Read `report.md` only if it exists and there are non-trivial quantitative comparisons or discrepancies.

## How to Run

```bash
# Add the first runnable command here, for example:
# python code/run_baseline.py
```

## Code Map

- `code/`: implementation, run entry points, configs, and code-local tests.
- `paper_src/`: paper PDF, supplements, screenshots, and original source files.
- `results/`: metrics, figures, logs, generated summaries, and comparison evidence.

## Current Result

- Evidence:
- Gap:
- Next step:
""",
    "notes.md": """# Reproduction Notes

## Paper Facts

## Method Sketch

## Equations and Implementation Notes

## Data and Code Availability

## Assumptions

## Missing Information

## Deviations From Paper
""",
}


OPTIONAL_DIRS = [
    "code/configs",
    "code/tests",
    "results/figures",
    "results/logs",
]


OPTIONAL_FILES = {
    "results/results.tsv": "run_id\tstatus\tprimary_metric\tcompare_to_paper\twall_time_min\tdescription\n",
    "results/trajectory.csv": "run_index,run_id,primary_metric,reference_metric,delta,label\n",
    "report.md": """# Reproduction Report

## Target Claim

## Reconstruction Choices

## Evidence

## Agreement With Paper

## Discrepancies
""",
}


def write_text_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def resolve_paper_path(root: Path, paper: str | None) -> Path | None:
    if not paper:
        return None
    candidate = Path(paper)
    return candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve()


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a compact code-first paper reproduction workspace.")
    parser.add_argument("--project-root", default=".", help="Target project root. Defaults to current directory.")
    parser.add_argument("--paper", help="Optional paper PDF filename or path.")
    parser.add_argument(
        "--include-optional",
        action="store_true",
        help="Also create code/configs, code/tests, result ledgers, figures/logs folders, and report starter.",
    )
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    root.mkdir(parents=True, exist_ok=True)

    for relative_dir in CORE_DIRS:
        (root / relative_dir).mkdir(parents=True, exist_ok=True)

    if args.include_optional:
        for relative_dir in OPTIONAL_DIRS:
            (root / relative_dir).mkdir(parents=True, exist_ok=True)

    for relative_file, content in CORE_FILES.items():
        write_text_if_missing(root / relative_file, content)

    if args.include_optional:
        for relative_file, content in OPTIONAL_FILES.items():
            write_text_if_missing(root / relative_file, content)

    paper_path = resolve_paper_path(root, args.paper)
    manifest = {
        "project_root": str(root),
        "paper": str(paper_path) if paper_path else None,
        "workspace_version": 4,
        "profile": "compact-code-first",
        "core_dirs": CORE_DIRS,
        "optional_starters_created": bool(args.include_optional),
    }
    manifest_path = root / "paper_src" / "workspace_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"Workspace created at: {root}")
    print("Profile: compact-code-first")
    print(f"Key output: {manifest_path}")
    if not args.include_optional:
        print("Optional starters were skipped. Re-run with --include-optional only when needed.")


if __name__ == "__main__":
    main()
