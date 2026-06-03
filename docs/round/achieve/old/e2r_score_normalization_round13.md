# E2R Score Normalization Round 13

Round 13 turns the latest sector/theme research into score-weight hypotheses.

This is not production scoring.

Easy example:

- `손해보험` can be Green-possible in the future.
- But only if loss ratio, CSM/capital, ROE, and shareholder return all support the thesis.
- Low PBR or high dividend alone stays insufficient.

Another example:

- `스테이블코인` can be a useful search theme.
- It remains RedTeam-first until there is regulated revenue, issued volume, adoption, and fee economics.

## What Round 13 Adds

- Score-weight hypothesis rows for selected refined sub-archetypes.
- Green conditions.
- Stage 4B watch conditions.
- Stage 4C thesis-break conditions.
- Case candidates for future case-library records.

## Output Files

- `data/sector_taxonomy/score_weight_profiles_round13.csv`
- `output/e2r_round13_score_normalization/round13_score_normalization_summary.md`
- `output/e2r_round13_score_normalization/round13_score_normalization_targets.csv`
- `output/e2r_round13_score_normalization/round13_green_watch_red_policy.md`
- `output/e2r_round13_score_normalization/round13_case_candidate_plan.md`
- `output/e2r_round13_score_normalization/round13_shadow_scoring_next_plan.md`

## Guardrails

- Do not apply these weights to production scoring yet.
- Do not change StageClassifier thresholds.
- Do not use theme tags as evidence.
- Backfill stage prices, MFE/MAE, peak prices, and drawdowns before shadow scoring.
