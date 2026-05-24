# E2R Calibrated Profile Report

- promotion_status: `applied`
- production_default_scoring_changed: `True`
- active_profile_path: `configs/e2r_scoring_profile_active.yaml`
- baseline rollback: set `E2R_SCORING_PROFILE=baseline` or edit `configs/e2r_scoring_profile_active.yaml` to `active_profile: baseline`.
- auto-trading: false
- brokerage API touched: false

## Applied Axes
- stage2_actionable_evidence_bonus / global: 0 -> 2.0 (Deduped Stage2/Stage2-Actionable rows repeatedly captured early non-price evidence before Green confirmation.)
- stage3_yellow_total_min / global: 80.0 -> 75.0 (Stage3-Yellow is validated as an intermediate state when evidence is strong but Green gates remain open.)
- stage3_green_total_min / global: 85.0 -> 87.0 (Late/false Green evidence supports stricter Green confirmation rather than broad relaxation.)
- stage3_green_revision_min / global: 50.0 -> 55.0 (Green should require stronger EPS/OP/FCF revision confirmation after cumulative calibration.)
- stage3_cross_evidence_green_buffer / global: 0 -> 1.5 (Strong multi-family evidence may bridge small total-score rounding gaps while stricter Green gates remain active.)
- full_4b_requires_non_price_evidence / 4B_guardrail: False -> True (Price-only local peaks repeatedly failed as full 4B; full 4B now requires non-price evidence.)
- hard_4c_thesis_break_routes_to_4c / 4C_guardrail: False -> True (4C rows are thesis-break/protection logic and must never train positive entry weights.)

## Guardrails
- 4B rows do not train positive entry weights.
- 4C rows are thesis-break/protection only.
- Price-only blowoff cannot promote Stage2/Stage3.
