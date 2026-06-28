# Visual Reporting

Use this reference when turning reproduction outputs into figures, tables, and easy-to-review reports.

## 1. Story before exhaustiveness

Do not present the final output as a raw folder dump. Prefer a compact research story:

1. target claim,
2. reconstruction approach,
3. evidence,
4. discrepancy,
5. next action.

## 2. Minimum visual package

For a meaningful reproduction, try to produce at least three review artifacts:

- a trajectory plot across runs,
- a paper-vs-reproduction comparison figure or table,
- one focused figure showing the most important success or failure mode.

## 3. Chart selection rules

- Use a line plot for optimization or training trajectories.
- Use grouped bars for method or benchmark comparisons.
- Use a horizontal bar chart for ranked results.
- Use a heatmap for structured matrices or ablation grids.
- Use a scatter plot only when two continuous variables need correlation analysis.

If a figure has numerical axes, prefer a reproducible plotting workflow instead of screenshots.

## 4. Figure quality rules

- Label every axis.
- Include units whenever the quantity is physical.
- Use consistent colors across the whole reproduction.
- Make the reproduced method visually distinct from the paper baseline.
- Add short captions or adjacent explanation text.
- Avoid cluttered legends and avoid unexplained abbreviations.

## 5. Suggested semantics

- Paper-reported result: neutral dark tone
- Reproduced result: accent color
- Best baseline: secondary strong tone
- Missing or unavailable result: muted gray

## 6. Recommended report structure

For `report.md`, prefer this order:

- Executive summary
- Background and target claim
- Methodology and reconstruction choices
- Key findings
- Data and evidence
- Implications
- Recommendations
- Appendix

For `notes.md`, prefer this order:

- Core idea in plain language
- Minimal reproducible recipe
- What each main figure teaches
- Common pitfalls
- What to try next

## 7. Easy-to-learn output

Assume the reader is a new student joining the project. The artifacts should let them answer:

- What does the paper claim?
- What did we actually implement?
- Which results match and which do not?
- Why do we think the mismatch happened?
- What should be tried next?

If the reader cannot answer those five questions in under ten minutes, the output is not clear enough.
