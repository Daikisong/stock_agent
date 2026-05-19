# Round-194 R3 Loop-7 Price-Path Validation Summary

- source_round: `docs/round/round_194.md`
- large_sector: `BATTERY_EV_GREEN`
- scope: Korean EV battery, ESS pivot, cathode, separator, lithium event, and battery-material false-Green prevention
- case_candidate_count: 7
- required_target_count: 16
- score_adjustment_count: 19
- price_backfill_field_count: 51
- success_candidate_count: 2
- overheat_count: 2
- failed_rerating_count: 2
- hard_4c_case_count: 1
- stage3_case_count: 0
- stage4b_watch_or_elevated_count: 6
- needs_ohlc_backfill_count: 7
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true
- needs_ohlc_backfill: true

## Interpretation

- R3는 현재 Stage 3-Green을 많이 찾는 라운드가 아니라 false Green을 막는 라운드다.
- LG에너지솔루션은 ESS LFP 계약으로 Stage 2는 가능하지만, EV 계약 손실과 OPM/FCF 공백 때문에 Stage 3는 보류한다.
- L&F의 Tesla 계약가치 붕괴는 계약 headline이 실제 call-off와 매출로 내려오지 않을 때 생기는 hard 4C 사례다.
- 삼성SDI의 미확정 Tesla ESS 보도는 회사 확인 전 Stage 1 attention에 머문다.
- 포스코퓨처엠과 에코프로머티리얼즈는 리튬 이벤트/IPO/그룹 스토리와 구조적 EPS/FCF evidence를 분리해야 한다.

쉬운 예: `as_of_date=2025-11-03`에 Tesla ESS 보도가 있어도 회사가 '결정된 것 없음'이라고 하면 Stage 3-Green 근거가 아니다. 계약 확인, GWh, 출하, OPM, FCF가 보여야 한다.
