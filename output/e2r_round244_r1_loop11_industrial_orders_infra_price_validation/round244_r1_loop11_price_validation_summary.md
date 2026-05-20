# Round 244 R1 Loop 11 Industrial Orders / Infrastructure Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_244.md
- round_id: round_172
- large_sector: INDUSTRIAL_ORDERS_INFRA
- cases: 9
- success_candidate: 7
- failed_rerating: 1
- hard_4c_case_count: 1
- Stage 3 dated cases: 0
- 4B-watch cases: 7
- price_moved_without_evidence: 3
- evidence_good_but_price_failed: 3
- target_archetype_count: 11
- deep_sub_archetype_count: 9
- shadow_weight_row_count: 9
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r1_loop11_czech_nuclear_doosan_kepco_stage2 | Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO | success_candidate | 2025-06-04 |  | 2024-07-17 | 2025-05-06 | success_candidate_4b_watch | Preferred bidder에서 signed contract로 올라온 강한 Stage 2지만 상장사별 package, margin, cash collection 전 Green은 금지다. |
| r1_loop11_doosan_smr_ai_power_mou | Doosan Enerbility / SMR-AI power cooperation | success_candidate | 2025-08-26 |  |  |  | event_premium_success_candidate | SMR/AI power 협력은 좋은 Stage 2 후보지만 funded order 전에는 Green이 아니다. |
| r1_loop11_ls_grid_cable_transformer_price_failed | LS Electric / LS Corp | success_candidate | 2024-06-20 |  |  |  | evidence_good_but_price_failed | 계약과 U.S. mix 증거는 좋지만 가격경로가 즉시 실패했다. 납품·마진·FCF 전 Green은 보류다. |
| r1_loop11_hd_hyundai_marine_solution_ipo_4b | HD Hyundai Marine Solution | success_candidate | 2024-05-08 |  | 2024-05-08 |  | success_candidate_4b_watch | MRO 반복서비스 스토리는 좋지만 IPO debut +96.5%는 실적검증 전 4B다. |
| r1_loop11_hd_hyundai_heavy_mipo_masga_merger | HD Hyundai Heavy / HD Hyundai Mipo | success_candidate | 2025-08-27 |  | 2025-08-27 |  | event_premium_success_candidate | MASGA/합병은 Stage 2와 4B-watch다. funded U.S. order와 margin 전에는 Stage 3가 아니다. |
| r1_loop11_samsung_heavy_zvezda_contract_cancellation | Samsung Heavy Industries | 4c_thesis_break |  |  |  | 2025-06-18 | thesis_break | Zvezda 취소는 hard 4C다. 러시아·제재 고객 수주잔고는 Green 전 RedTeam으로 강하게 걸러야 한다. |
| r1_loop11_hanwha_aerospace_poland_jv_dilution_watch | Hanwha Aerospace | success_candidate | 2025-04-15 |  | 2025-03-21 |  | success_candidate_aligned_4B_detection | Poland missile JV는 Stage 2지만 대형 증자 shock 때문에 dilution 4B-watch가 필수다. |
| r1_loop11_hyundai_rotem_morocco_rail_order | Hyundai Rotem | success_candidate | 2025-02-26 |  |  |  | success_candidate | Morocco rail order는 강한 Stage 2다. 납품·마진·working capital 전 Stage 3는 보류다. |
| r1_loop11_hanwha_ocean_china_sanction_watch | Hanwha Ocean | failed_rerating |  |  |  | 2025-10-14 | thesis_break_watch | U.S. shipbuilding exposure가 좋아도 China sanctions는 4C-watch다. 실제 매출·부품·계약 차질 확인 시 hard 4C다. |

## Interpretation
- R1 Stage 3 is not an order headline. It needs delivery, revenue, margin, EPS revision, cash collection, and post-evidence price path.
- Czech nuclear is strong Stage 2 after the signed contract, but listed-company scope and margin are still required.
- SMR/AI power, MASGA, IPO, and merger events are Stage 2/4B-watch until funded orders and economics confirm.
- Samsung Heavy/Zvezda is a hard 4C contract-cancellation anchor.
- Hanwha Ocean sanctions are 4C-watch, not hard 4C until actual revenue, module, or contract disruption appears.
