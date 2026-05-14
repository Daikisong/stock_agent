# Checkpoint 28A-12: Round 10 Theme Tag Taxonomy

Round 10 converts the broad theme list into a report-only taxonomy layer.

## What Changed

- Added a 12-large-sector Round 10 taxonomy.
- Added 65 sub-archetype/theme groups.
- Generated `data/sector_taxonomy/theme_tag_map.csv`.
- Added a CLI to rebuild Round 10 reports.
- Kept production scoring unchanged.

## Why

The prior 10 large sectors and 32 archetype view were directionally correct but too coarse for the actual Korea theme universe.

Example:

- `편의점` should not become its own scoring engine.
- It maps to `RETAIL_CONVENIENCE_OFFLINE`.
- That maps to canonical `RETAIL_DOMESTIC_CONSUMER`.
- Future scoring should still check same-store sales, OPM, inventory, and cash flow.

## Guardrail

Theme tags are search/routing labels only.

Examples:

- `초전도체` maps to speculative/theme risk and remains RedTeam-first.
- `엠폭스` maps to one-off infectious disease event risk.
- `스테이블코인` maps to digital asset/tokenization risk and needs regulated revenue before any high-conviction treatment.

## Outputs

- `data/sector_taxonomy/theme_tag_map.csv`
- `output/e2r_round10_theme_tag_taxonomy/theme_tag_map.csv`
- `output/e2r_round10_theme_tag_taxonomy/round10_theme_taxonomy_summary.md`
- `output/e2r_round10_theme_tag_taxonomy/round10_large_sector_map.csv`
- `output/e2r_round10_theme_tag_taxonomy/round10_sub_archetype_map.csv`
- `output/e2r_round10_theme_tag_taxonomy/round10_posture_report.md`
- `output/e2r_round10_theme_tag_taxonomy/round10_case_record_candidate_plan.md`

## What Did Not Change

- No StageClassifier threshold change.
- No production scoring weight change.
- No case/theme label is used as candidate-generation evidence.
- No fabricated stage dates or price paths.

## Next Step

Use the theme tag map to mine case records for v0.3, then backfill price paths and score-price alignment before any scoring-weight implementation.
