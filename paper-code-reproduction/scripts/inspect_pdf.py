#!/usr/bin/env python3
"""Find local PDF candidates and emit lightweight metadata."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def find_pdfs(root: Path) -> list[Path]:
    return sorted(path for path in root.iterdir() if path.is_file() and path.suffix.lower() == ".pdf")


def guess_title_from_filename(path: Path) -> str:
    title = path.stem.replace("_", " ").replace("-", " ").strip()
    title = re.sub(r"\s+", " ", title)
    return title


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect local PDF candidates for paper reproduction.")
    parser.add_argument("--project-root", default=".", help="Directory to inspect.")
    parser.add_argument(
        "--output",
        help="Optional JSON output path. Defaults to paper_src/metadata.json when available.",
    )
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    if not root.exists():
        raise SystemExit(f"Project root does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Project root is not a directory: {root}")

    pdfs = find_pdfs(root)

    payload = {
        "project_root": str(root),
        "pdf_count": len(pdfs),
        "pdfs": [
            {
                "filename": path.name,
                "path": str(path),
                "size_bytes": path.stat().st_size,
                "title_guess": guess_title_from_filename(path),
            }
            for path in pdfs
        ],
    }

    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = (root / output_path).resolve()
    else:
        default_output = root / "paper_src" / "metadata.json"
        output_path = default_output if default_output.parent.exists() else None

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"Wrote PDF summary to: {output_path}")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
