# Checkpoint 28A-13: Round 12 Theme Refinement

Round 12 adds a refinement overlay for theme families that were still too broad after Round 10.

## What Changed

- Added 18 refined sub-archetype targets.
- Added `theme_tag_map_round12.csv` with the Round 12 schema.
- Added stage-1 query terms, must-have evidence, red-flag evidence, and future score-weight profile labels.
- Added a report CLI for Round 12 outputs.

## Why

Round 10 correctly separated theme tags from scoring, but some themes still needed sharper routing.

Example:

- `손해보험` should not be treated like a generic bank.
- It needs loss ratio, CSM/capital, ROE, and shareholder-return execution.
- Low PBR alone is not enough.

## Output Files

- `data/sector_taxonomy/theme_tag_map_round12.csv`
- `output/e2r_round12_theme_refinement/round12_theme_refinement_summary.md`
- `output/e2r_round12_theme_refinement/round12_sub_archetype_refinements.csv`
- `output/e2r_round12_theme_refinement/round12_case_candidate_plan.csv`
- `output/e2r_round12_theme_refinement/round12_theme_tag_map_schema.md`
- `output/e2r_round12_theme_refinement/round12_next_case_library_plan.md`

## What Did Not Change

- Production scoring is unchanged.
- StageClassifier thresholds are unchanged.
- Theme tags are not candidate-generation evidence.
- Case candidates remain planned calibration records only.

## Next Step

Convert the Round 12 case candidates into v0.3 case-library records, then backfill price paths and score-price alignment before any scoring-weight shadow simulation.
