# Applied Scoring Diff

| axis | scope | old baseline axis | new calibrated axis | delta | confidence | unique cases | unique rounds | reason |
|---|---|---:|---:|---:|---|---:|---:|---|
| stage2_actionable_evidence_bonus | global | 0 | 2.0 | 2.0 | medium | 347 | 13 | Deduped Stage2/Stage2-Actionable rows repeatedly captured early non-price evidence before Green confirmation. |
| stage3_yellow_total_min | global | 80.0 | 75.0 | -5.0 | medium | 183 | 13 | Stage3-Yellow is validated as an intermediate state when evidence is strong but Green gates remain open. |
| stage3_green_total_min | global | 85.0 | 87.0 | 2.0 | high | 225 | 13 | Late/false Green evidence supports stricter Green confirmation rather than broad relaxation. |
| stage3_green_revision_min | global | 50.0 | 55.0 | 5.0 | high | 225 | 13 | Green should require stronger EPS/OP/FCF revision confirmation after cumulative calibration. |
| stage3_cross_evidence_green_buffer | global | 0 | 1.5 | 1.5 | medium | 225 | 13 | Strong multi-family evidence may bridge small total-score rounding gaps while stricter Green gates remain active. |
| full_4b_requires_non_price_evidence | 4B_guardrail | False | True | 1.0 | high | 282 | 13 | Price-only local peaks repeatedly failed as full 4B; full 4B now requires non-price evidence. |
| hard_4c_thesis_break_routes_to_4c | 4C_guardrail | False | True | 1.0 | high | 92 | 11 | 4C rows are thesis-break/protection logic and must never train positive entry weights. |
