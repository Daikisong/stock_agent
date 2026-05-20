# Round 243 R13 Loop 10 Cross-Archetype RedTeam Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_243.md
- large_sector: CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION
- cases: 8
- structural_success: 2
- success_candidate: 1
- failed_rerating: 1
- overheat: 1
- hard_4c_case_count: 3
- Stage 3 dated cases: 2
- 4B-watch cases: 5
- price_moved_without_evidence: 2
- deep_sub_archetype_count: 8
- shadow_weight_row_count: 8
- r13_default_stage3_bias: redteam_first_after_price_validation
- full_ohlc_complete: false

## Case Matrix

| case | company | source | type | stage3 | 4B | 4C | round alignment | note |
|---|---|---|---|---|---|---|---|---|
| r13_loop10_sk_hynix_hbm_stage3_4b | SK하이닉스 | R2 | structural_success | 2024-06-25 | 2026-05-04 |  | aligned | Stage 3 성공 benchmark다. 다만 2026년 현재는 신규 Green이 아니라 4B-watch/crowding watch다. |
| r13_loop10_apr_medicube_structural_4b | APR / Medicube | R5 | structural_success | 2025-10-01 | 2025-07-08 |  | aligned | Viral이 실제 해외 매출로 내려온 구조 후보지만 매출 집중도와 valuation 때문에 4B-watch가 필요하다. |
| r13_loop10_samsung_sds_kkr_ai_event_4b | 삼성SDS | R8/R6 | success_candidate |  | 2026-04-15 |  | event_premium_success_candidate | 좋은 Stage 2 후보지만 AI revenue conversion 전 +20.8%는 Green이 아니라 4B-watch다. |
| r13_loop10_hyundai_steel_policy_capex_failure | 현대제철 | R4/R11 | failed_rerating |  | 2025-03-25 | 2025-04-22 | false_positive_score_prevention | 정책·관세 대응 CAPEX는 funding·margin·FCF가 없으면 Green이 아니라 RedTeam이다. |
| r13_loop10_lnf_tesla_cathode_contract_hard_4c | L&F | R3/R4 | 4c_thesis_break |  |  | 2025-12-29 | thesis_break | 고객명과 계약금액 headline은 actual call-off, volume, margin, FCF 없이 Green이 아니다. |
| r13_loop10_jeju_air_operational_safety_hard_4c | 제주항공 | R9 | 4c_thesis_break |  |  | 2024-12-30 | thesis_break | 여행수요가 좋아도 fatal accident가 나오면 Green은 즉시 차단한다. |
| r13_loop10_hormuz_iran_macro_hard_4c | Hormuz / Iran macro energy shock | R11 | 4c_thesis_break |  |  | 2026-05-18 | thesis_break | Hormuz/Iran shock은 에너지·운송·제조·환율 리스크를 동시에 찌르는 cross-sector hard 4C다. |
| r13_loop10_stablecoin_policy_theme_overheat | KRW stablecoin policy basket | R6/R11 | overheat |  | 2025-06-01 |  | price_moved_without_evidence | Stablecoin basket은 발행권·reserve income·fee revenue 전 2~3배 상승한 price-only 사례다. |

## Interpretation
- SK Hynix and APR/Medicube are aligned structural-success benchmarks, but both need 4B-watch after major rerating.
- Samsung SDS is Stage 2 plus 4B-watch; CB and AI capital allocation are not recurring AI revenue.
- Hyundai Steel prevents false Green from policy-induced CAPEX without funding or margin clarity.
- L&F and Jeju Air are hard 4C anchors for contract quality and operational safety.
- Hormuz/Iran is a macro hard 4C overlay across energy, shipping, FX, manufacturing, and airlines.
- Stablecoin basket is price_moved_without_evidence before issuer license, reserve income, fee revenue, or regulatory capital clarity.
