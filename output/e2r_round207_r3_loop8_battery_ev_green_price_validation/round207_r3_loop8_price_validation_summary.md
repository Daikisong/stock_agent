# Round-207 R3 Loop-8 Price-Path Validation Summary

- source_round: `docs/round/round_207.md`
- large_sector: `BATTERY_EV_GREEN`
- scope: ESS LFP contracts, EV demand slowdown, contract cancellation, cathode value collapse, SK On restructuring, lithium event premium, and precursor overheat
- case_candidate_count: 7
- required_target_count: 15
- score_adjustment_count: 18
- price_validation_field_count: 17
- success_candidate_count: 2
- failed_rerating_count: 2
- event_premium_or_overheat_count: 2
- hard_4c_case_count: 3
- stage3_case_count: 0
- stage4c_watch_or_hard_count: 7
- reported_price_anchor_count: 6
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Interpretation

- LG에너지솔루션과 삼성SDI의 ESS/LFP 계약은 Stage 2 후보지만, 배송·가동률·OPM·FCF 확인 전 Green은 보류한다.
- L&F는 Tesla 계약가치 붕괴로 `contract_value_collapse` hard 4C 기준점이다.
- SK이노베이션/SK온과 SKIET는 EV 배터리 성장 thesis가 손실·부채·수요 둔화로 깨질 때의 failed rerating 사례다.
- 포스코퓨처엠 리튬 이벤트와 에코프로머티리얼즈 전구체 narrative는 event premium/overheat로 분리한다.

쉬운 예: `as_of_date=2025-07-30`에 LGES가 43억 달러 ESS 계약을 발표했더라도, 2027년 이후 배송·마진·FCF가 아직 없으면 Stage 3-Green이 아니라 Stage 2 watch다.
