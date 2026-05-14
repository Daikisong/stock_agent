# Checkpoint 28A-18: Round 17 Theme Absorption Audit

## Summary

Round 17 was applied as a theme-coverage audit layer, not as a production
scoring change.

The round's main rule is:

> Theme names route research. Evidence creates score.

Example: `스테이블코인` now maps to `DIGITAL_ASSET_TOKENIZATION`, but that only
routes research toward regulated revenue, volume, and fee economics. It does
not create Stage 3-Green evidence.

## Implemented

- Added `src/e2r/sector/round17_theme_absorption_audit.py`.
- Added `src/e2r/cli/audit_round17_theme_coverage.py`.
- Added `tests/test_round17_theme_absorption_audit.py`.
- Added `docs/e2r_theme_coverage_round17.md`.
- Generated Round 17 machine-readable outputs.

## Output Files

- `data/sector_taxonomy/theme_tag_map_v05.csv`
- `data/sector_taxonomy/theme_aliases_round17.yml`
- `output/e2r_round17_theme_absorption_audit/theme_coverage_report.md`
- `output/e2r_round17_theme_absorption_audit/round17_theme_coverage_audit.json`
- `output/e2r_round17_theme_absorption_audit/theme_coverage_matrix.csv`
- `output/e2r_round17_theme_absorption_audit/unmatched_theme_tags.csv`
- `output/e2r_round17_theme_absorption_audit/green_policy_distribution.csv`

## Audit Result

- total_theme_tags: 151
- mapped_theme_tags: 151
- unmatched_theme_tags: 0
- large_sector_count: 12
- archetype_count: 73
- production_scoring_changed: false
- theme_tags_are_score_input: false
- scoring_ready: false

## Green Policy Distribution

- green_allowed: 17
- watch_to_green: 27
- watch_only: 65
- red_watch: 20
- event_watch: 10
- event_only: 7
- red_flag: 5

## Interpretation

The theme structure is now absorbed for case-mining purposes. This is still not
enough to apply final scoring weights.

For example:

- `라면` can map to `EXPORT_RECURRING_CONSUMER`.
- It still needs export/channel expansion, repeat demand, OPM, and revision evidence.
- Without those evidence fields, the tag remains a research route only.

## Guardrails Preserved

- StageClassifier thresholds were not changed.
- Production scoring modules do not import the Round 17 audit module.
- Theme tags are not candidate-generation labels.
- Benchmark/case labels remain outside production candidate generation.
- Event, policy, and speculative tags remain RedTeam or Watch first unless actual EPS/FCF evidence exists.

## Next Step

Use `theme_tag_map_v05.csv` to drive case-library mining and unmatched-tag
monitoring. Do not apply new score weights until archetype-level success,
counterexample, and price-path validation are complete.
