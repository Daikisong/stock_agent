# V12 Rolling Calibration Apply Report

v12 연구 결과의 `apply_next_patch` 항목을 기본 점수 프로파일에 반영했습니다.
반영은 전역 완화가 아니라 large sector / canonical archetype scope가 맞을 때만 작동합니다.
Stage 3-Green 기준은 낮추지 않았고, 가격만 오른 케이스는 positive Stage 승격을 막는 방향으로 유지했습니다.

- profile_id: `e2r_2_2_rolling_calibrated`
- profile_path: `configs/e2r_scoring_profile_v2_2.yaml`
- active_profile_path: `configs/e2r_scoring_profile_active.yaml`
- production_default_scoring_changed: `True`
- applied_patch_count: `111`
- applied_axis_counts: `{'earlier_thesis_break_watch': 34, 'full_4b_overlay_candidate': 12, 'local_4b_watch_guard': 20, 'stage2_bonus_candidate_delta': 2, 'stage2_required_bridge': 43}`
- rollback_profile: `calibrated`

## Applied Scope Counts
- v12_stage2_bonus_scopes: `2`
- v12_stage2_required_bridge_scopes: `43`
- v12_local_4b_watch_guard_scopes: `20`
- v12_full_4b_overlay_scopes: `12`
- v12_earlier_4c_watch_scopes: `34`
- v12_hard_4c_confirmation_scopes: `0`

## Simple Example

- 예전: C22 보험 archetype 연구가 쌓여도 보고서에만 남고 기본 점수는 바뀌지 않았습니다.
- 지금: payload에 `canonical_archetype_id=C22_INSURANCE_RATE_CYCLE_RESERVE`가 붙고 비가격 증거가 있으면 Stage2 근처 점수에 최대 +1 보정이 실제 적용됩니다.
- 반대로 price-only 4B scope에서는 주가 급등만으로 Stage2/Stage3 또는 full 4B가 되지 않도록 더 강하게 막습니다.
