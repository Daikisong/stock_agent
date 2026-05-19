# Round-205 R1 Loop-8 Price-Path Validation Summary

- source_round: `docs/round/round_205.md`
- large_sector: `INDUSTRIAL_ORDERS_INFRA`
- scope: defense backlog, combat validation, aircraft export, shipbuilding/MRO, IPO premium, sanction watch, and merger-event price anchors
- case_candidate_count: 7
- required_target_count: 14
- score_adjustment_count: 14
- price_validation_field_count: 14
- structural_success_count: 2
- success_candidate_count: 3
- overheat_or_watch_count: 2
- hard_4c_case_count: 0
- stage3_case_count: 1
- stage4b_watch_or_elevated_count: 6
- reported_price_anchor_count: 7
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Interpretation

- 현대로템과 한화에어로스페이스는 방산 backlog/납품 visibility가 실제 큰 가격경로와 맞았던 aligned benchmark다.
- LIG넥스원과 한국항공우주는 Stage 2 watch 성공 사례지만, Stage 3-Green에는 계약기간·납품·마진·EPS 전환 확인이 더 필요하다.
- HD현대마린솔루션 IPO 첫날 급등은 MRO 플랫폼 가능성과 별개로 price-before-evidence 이벤트다.
- 한화오션 중국 제재는 hard 4C가 아니라 4C-watch다. 매출 차질, 금융 실패, 계약 취소가 확인되어야 hard 4C다.
- HD현대중공업/현대미포 이벤트 급등은 조선 Stage 2 watch 가능성이지만, 합병/정책 이벤트만으로 Green은 만들지 않는다.

쉬운 예: `as_of_date=2024-05-08`에 IPO 첫날 96% 급등이 보여도, 그날 확인 가능한 MRO 반복매출·마진·EPS 상향이 없으면 Stage 3-Green 근거가 아니라 이벤트 프리미엄이다.
