#!/usr/bin/env python3
"""Generate optional SVG charts and an HTML dashboard from result ledgers."""

from __future__ import annotations

import argparse
import csv
import html
from collections import Counter
from pathlib import Path


def read_results(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader)


def read_trajectory(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def to_float(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def generate_trajectory_svg(rows: list[dict[str, str]], output_path: Path) -> None:
    width = 840
    height = 420
    padding = 60
    plot_w = width - 2 * padding
    plot_h = height - 2 * padding

    numeric_rows = []
    for index, row in enumerate(rows):
        metric = to_float(row.get("primary_metric", ""))
        if metric is None:
            continue
        label = row.get("label") or row.get("run_id") or f"run-{index + 1}"
        numeric_rows.append((index, metric, label))

    if not numeric_rows:
        svg = (
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="16"/>'
            '<text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" '
            'font-family="Georgia, serif" font-size="20" fill="#475569">No trajectory data yet.</text>'
            "</svg>"
        )
        output_path.write_text(svg, encoding="utf-8")
        return

    metrics = [item[1] for item in numeric_rows]
    min_metric = min(metrics)
    max_metric = max(metrics)
    margin = (max_metric - min_metric) * 0.1 or 1.0
    y_min = min_metric - margin
    y_max = max_metric + margin

    def x_pos(i: int) -> float:
        return padding + (i / max(len(numeric_rows) - 1, 1)) * plot_w

    def y_pos(v: float) -> float:
        return padding + plot_h - ((v - y_min) / max(y_max - y_min, 1e-9)) * plot_h

    parts = [
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
        f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="16"/>',
        f'<rect x="{padding}" y="{padding}" width="{plot_w}" height="{plot_h}" fill="#ffffff" stroke="#cbd5e1" rx="10"/>',
        '<text x="50%" y="34" text-anchor="middle" font-family="Georgia, serif" font-size="20" fill="#0f172a">Reproduction Trajectory</text>',
    ]

    for i in range(5):
        y = padding + i * plot_h / 4
        value = y_max - i * (y_max - y_min) / 4
        parts.append(f'<line x1="{padding}" y1="{y:.1f}" x2="{padding + plot_w}" y2="{y:.1f}" stroke="#e2e8f0"/>')
        parts.append(f'<text x="{padding - 8}" y="{y + 4:.1f}" text-anchor="end" font-family="Georgia, serif" font-size="11" fill="#475569">{value:.4g}</text>')

    baseline = numeric_rows[0][1]
    baseline_y = y_pos(baseline)
    parts.append(
        f'<line x1="{padding}" y1="{baseline_y:.1f}" x2="{padding + plot_w}" y2="{baseline_y:.1f}" '
        'stroke="#94a3b8" stroke-dasharray="6 4"/>'
    )
    parts.append(
        f'<text x="{padding + plot_w - 4}" y="{baseline_y - 6:.1f}" text-anchor="end" font-family="Georgia, serif" font-size="11" fill="#64748b">baseline</text>'
    )

    point_string = " ".join(f"{x_pos(i):.1f},{y_pos(metric):.1f}" for i, metric, _ in numeric_rows)
    parts.append(f'<polyline points="{point_string}" fill="none" stroke="#0f766e" stroke-width="3"/>')

    for i, metric, label in numeric_rows:
        x = x_pos(i)
        y = y_pos(metric)
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#e76f51"/>')
        parts.append(f'<text x="{x:.1f}" y="{y - 10:.1f}" text-anchor="middle" font-family="Georgia, serif" font-size="10" fill="#7c2d12">{html.escape(label)}</text>')

    parts.append(f'<text x="{width / 2:.1f}" y="{height - 16}" text-anchor="middle" font-family="Georgia, serif" font-size="12" fill="#475569">Run order</text>')
    parts.append("</svg>")
    output_path.write_text("".join(parts), encoding="utf-8")


def generate_status_svg(rows: list[dict[str, str]], output_path: Path) -> None:
    width = 840
    height = 320
    padding = 70
    plot_w = width - 2 * padding
    plot_h = 170
    counts = Counter((row.get("status") or "unknown").strip().lower() or "unknown" for row in rows)

    if not counts:
        svg = (
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="16"/>'
            '<text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" '
            'font-family="Georgia, serif" font-size="20" fill="#475569">No run status data yet.</text>'
            "</svg>"
        )
        output_path.write_text(svg, encoding="utf-8")
        return

    colors = {
        "keep": "#0f766e",
        "discard": "#e76f51",
        "crash": "#b91c1c",
        "timeout": "#d97706",
        "unknown": "#64748b",
    }
    items = sorted(counts.items())
    max_count = max(counts.values())
    bar_width = plot_w / max(len(items), 1) * 0.6

    parts = [
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
        f'<rect width="{width}" height="{height}" fill="#f8fafc" rx="16"/>',
        '<text x="50%" y="34" text-anchor="middle" font-family="Georgia, serif" font-size="20" fill="#0f172a">Run Status Breakdown</text>',
        f'<line x1="{padding}" y1="{padding + plot_h}" x2="{padding + plot_w}" y2="{padding + plot_h}" stroke="#94a3b8"/>',
    ]

    for idx, (name, count) in enumerate(items):
        x = padding + (idx + 0.5) * (plot_w / len(items))
        bar_h = (count / max_count) * plot_h
        y = padding + plot_h - bar_h
        color = colors.get(name, "#64748b")
        parts.append(f'<rect x="{x - bar_width / 2:.1f}" y="{y:.1f}" width="{bar_width:.1f}" height="{bar_h:.1f}" fill="{color}" rx="8"/>')
        parts.append(f'<text x="{x:.1f}" y="{y - 8:.1f}" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#334155">{count}</text>')
        parts.append(f'<text x="{x:.1f}" y="{padding + plot_h + 18:.1f}" text-anchor="middle" font-family="Georgia, serif" font-size="11" fill="#475569">{html.escape(name)}</text>')

    parts.append("</svg>")
    output_path.write_text("".join(parts), encoding="utf-8")


def build_dashboard_html(results: list[dict[str, str]], trajectory: list[dict[str, str]]) -> str:
    latest = results[-1] if results else {}
    best_metric = None
    for row in trajectory:
        metric = to_float(row.get("primary_metric", ""))
        if metric is None:
            continue
        best_metric = metric if best_metric is None else max(best_metric, metric)

    latest_run = latest.get("run_id", "N/A")
    latest_status = latest.get("status", "N/A")
    latest_desc = latest.get("description", "No description yet.")
    best_metric_text = f"{best_metric:.6g}" if best_metric is not None else "N/A"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Reproduction Dashboard</title>
  <style>
    body {{ font-family: Georgia, "Times New Roman", serif; margin: 24px; background: #f8fafc; color: #1f2937; }}
    h1, h2 {{ color: #0f172a; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px; }}
    .card {{ background: white; border: 1px solid #dbe4ee; border-radius: 12px; padding: 16px; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06); }}
    img {{ max-width: 100%; height: auto; display: block; }}
    code {{ background: #e2e8f0; padding: 2px 6px; border-radius: 6px; }}
    ul {{ padding-left: 18px; }}
  </style>
</head>
<body>
  <h1>Reproduction Dashboard</h1>
  <p>Refresh this page with <code>scripts/generate_reproduction_dashboard.py</code> after updating the run ledger.</p>
  <div class="grid">
    <div class="card">
      <h2>Current Snapshot</h2>
      <ul>
        <li>Latest run: {html.escape(latest_run)}</li>
        <li>Latest status: {html.escape(latest_status)}</li>
        <li>Best metric seen: {best_metric_text}</li>
      </ul>
      <p>{html.escape(latest_desc)}</p>
    </div>
    <div class="card">
      <h2>Trajectory</h2>
      <img src="./figures/trajectory.svg" alt="Trajectory chart" />
    </div>
    <div class="card">
      <h2>Status Breakdown</h2>
      <img src="./figures/status_breakdown.svg" alt="Status breakdown chart" />
    </div>
    <div class="card">
      <h2>Linked Files</h2>
      <ul>
        <li><a href="../README.md">README.md</a></li>
        <li><a href="../notes.md">notes.md</a></li>
        <li><a href="../report.md">report.md</a></li>
      </ul>
    </div>
  </div>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate dashboard assets from reproduction result ledgers.")
    parser.add_argument("--project-root", default=".", help="Reproduction project root.")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    results_path = root / "results" / "results.tsv"
    trajectory_path = root / "results" / "trajectory.csv"
    report_dir = root / "results"
    figures_dir = root / "results" / "figures"

    report_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    results = read_results(results_path)
    trajectory = read_trajectory(trajectory_path)

    generate_trajectory_svg(trajectory, figures_dir / "trajectory.svg")
    generate_status_svg(results, figures_dir / "status_breakdown.svg")
    dashboard_html = build_dashboard_html(results, trajectory)
    (report_dir / "dashboard.html").write_text(dashboard_html, encoding="utf-8")

    print(f"Dashboard updated under: {report_dir}")


if __name__ == "__main__":
    main()
