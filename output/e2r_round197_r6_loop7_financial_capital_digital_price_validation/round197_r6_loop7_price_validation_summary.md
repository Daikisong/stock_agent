# Round-197 R6 Loop-7 Price-Path Validation Summary

- source_round: `docs/round/round_197.md`
- large_sector: `FINANCIAL_CAPITAL_DIGITAL`
- scope: Korean bank, insurance, holding value-up, payment fintech, digital asset, and stablecoin policy validation
- case_candidate_count: 7
- required_target_count: 21
- score_adjustment_count: 21
- price_backfill_field_count: 53
- structural_success_count: 1
- success_candidate_count: 3
- overheat_count: 1
- failed_rerating_count: 1
- thesis_break_count: 1
- hard_4c_case_count: 2
- stage3_case_count: 0
- stage3_conditional_candidate_count: 1
- stage4b_watch_or_elevated_count: 7
- needs_ohlc_backfill_count: 7
- production_scoring_changed: false
- candidate_generation_input: false
- shadow_weight_only: true
- needs_ohlc_backfill: true

## Interpretation

- R6는 저PBR과 정책 밸류업을 실제 ROE/CET1/소각/credit-cost evidence와 분리한다.
- SK스퀘어는 소각과 NAV discount가 강하지만 SK하이닉스 랠리 뒤에는 4B-watch가 필요하다.
- 하나금융의 두나무 지분은 Stage 2 후보지만 규제수익, 지분법, 자본비율 영향 전에는 Green이 아니다.
- 삼성생명은 NAV discount가 있어도 규제성 지분매각과 capital release를 같이 봐야 한다.
- 카카오뱅크/카카오페이는 사용자 수보다 대주주 적격성, 개인정보, 규제 신뢰가 먼저다.
- 스테이블코인 테마는 수익모델 전에는 price_moved_without_evidence로 분리한다.
- 우리금융은 비은행 확장과 CET1/credit cost/주주환원을 함께 검증해야 한다.

쉬운 예: `as_of_date=2025-06-18`에 스테이블코인 정책 기대가 커져 관련주가 올라도, 실제 발행권·수수료·reserve income이 없으면 Stage 3-Green이 아니다.
