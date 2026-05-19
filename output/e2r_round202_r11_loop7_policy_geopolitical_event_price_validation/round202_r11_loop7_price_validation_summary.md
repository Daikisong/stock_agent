# Round-202 R11 Loop-7 Price-Path Validation Summary

- source_round: `docs/round/round_202.md`
- large_sector: `POLICY_GEOPOLITICAL_EVENT`
- scope: resource discovery, nuclear/SMR policy, shipbuilding MOU, disease demand, speculative science, political shock, and market-structure events
- case_candidate_count: 7
- required_target_count: 17
- score_adjustment_count: 20
- price_backfill_field_count: 52
- success_candidate_count: 3
- event_premium_count: 2
- overheat_count: 1
- hard_4c_case_count: 1
- stage3_case_count: 0
- stage4b_watch_or_elevated_count: 6
- needs_ohlc_backfill_count: 7
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true
- needs_ohlc_backfill: true
- r11_default_stage3_bias: conservative

## Interpretation

- R11은 대부분 Stage 3가 아니라 Event/Watch/RedTeam이다.
- 한국가스공사 동해 가스 이벤트는 강한 Stage 1이지만 시추·상업성 전 Green이 아니다.
- 두산에너빌리티 원전·SMR은 Stage 2 후보지만 final contract와 장비 backlog 전 Green이 아니다.
- HD현대·삼성중공업 미국 조선정책 MOU는 funded order 전 Stage 3가 아니다.
- 조류독감 poultry basket은 단기 MFE가 가능하지만 수입제한 완화가 event fade가 될 수 있다.
- LK-99는 speculative science hard 반례이며 failed replication은 thesis break다.
- 계엄·정치 shock은 개별 기업 Stage가 아니라 macro RedTeam overlay다.
- 공매도·MSCI 접근성은 시장구조 Stage 2 watch지만 개별 기업 EPS 전 Green이 아니다.

쉬운 예: `as_of_date=2024-06-03`에 동해 가스 뉴스로 주가가 급등해도, 시추 성공과 상업성이 없으면 Stage 3-Green이 아니라 4B-watch다.
