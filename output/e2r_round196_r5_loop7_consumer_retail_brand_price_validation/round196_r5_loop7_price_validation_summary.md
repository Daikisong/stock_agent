# Round-196 R5 Loop-7 Price-Path Validation Summary

- source_round: `docs/round/round_196.md`
- large_sector: `CONSUMER_RETAIL_BRAND`
- scope: K-food, K-beauty, ODM, beauty-device, retail platform, apparel, IPO, and M&A event validation
- case_candidate_count: 7
- required_target_count: 18
- score_adjustment_count: 21
- price_backfill_field_count: 51
- structural_success_count: 1
- success_candidate_count: 3
- overheat_count: 1
- failed_rerating_count: 1
- event_premium_count: 1
- hard_4c_case_count: 0
- stage3_case_count: 0
- stage3_possible_candidate_count: 1
- stage4b_watch_or_elevated_count: 4
- needs_ohlc_backfill_count: 7
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true
- needs_ohlc_backfill: true

## Interpretation

- R5는 진짜 구조적 수출 소비재와 viral/event premium을 분리하는 라운드다.
- 농심은 K-food staple Stage 2 후보지만 OPM/EPS와 channel sell-through 전에는 Stage 3가 아니다.
- APR은 overseas/US sales와 device revenue가 강하지만 2025년 4배 상승 anchor 때문에 4B-watch가 필요하다.
- d'Alba는 retail talks와 IPO 2x rally를 Green 근거로 쓰면 안 된다.
- 코스맥스/한국콜마 ODM은 고객 다변화, 주문 visibility, OPM, 재고/채권 확인 전 Green 금지다.
- 아모레퍼시픽은 K-beauty macro와 China/COSRX company-level risk를 분리해야 한다.
- CJ/올리브영은 좋은 private platform과 listed-parent value capture를 분리해야 한다.
- F&F TaylorMade는 M&A event premium이지 본업 브랜드 rerating 증거가 아니다.

쉬운 예: `as_of_date=2025-06-05`에 d'Alba가 미국 매장 입점 논의를 했더라도, 실제 매장 회전율과 반복 발주가 없으면 Stage 3-Green이 아니다.
