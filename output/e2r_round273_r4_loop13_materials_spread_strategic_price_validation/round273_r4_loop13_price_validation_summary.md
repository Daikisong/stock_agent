# Round 273 R4 Loop 13 Materials Spread Strategic Resources Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_273.md
- round_id: round_201
- large_sector: MATERIALS_SPREAD_STRATEGIC_RESOURCES
- cases: 8
- success_candidate: 2
- event_premium: 3
- failed_rerating: 2
- 4B-watch case_type: 1
- hard_4c_case_count: 0
- Stage 3 dated cases: 0
- 4B-watch cases: 6
- 4C-watch cases: 4
- price_data_unavailable: 4
- price_moved_without_evidence: 3
- false_positive_score: 1
- evidence_good_but_price_failed: 2
- full_adjusted_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r4_loop13_korea_zinc_control_premium_dilution_watch | Korea Zinc | success_candidate_overheat_4B_watch | 2024-09-13 |  | 2024-09-13 | 2025-12-16 | event_premium_4B_watch | 전략광물 후보이지만 지배권 프리미엄과 희석·거버넌스가 먼저 가격을 움직였다. |
| r4_loop13_posco_futurem_graphite_lithium_event | POSCO Future M | event_premium_price_moved_without_evidence | 2025-07-18 |  | 2025-07-18 |  | price_moved_without_evidence | graphite/lithium event는 가격을 움직였지만 실제 공급계약·인증·마진 전에는 Green이 아니다. |
| r4_loop13_steel_tariff_two_sided_posco_hyundai_seah | POSCO Holdings / Hyundai Steel / SeAH Steel | event_premium_4C_watch | 2025-02-20 |  | 2025-02-20 | 2025-06-02 | event_premium_plus_thesis_break_watch | 국내 anti-dumping relief와 미국 수출 관세 리스크를 같이 봐야 한다. |
| r4_loop13_hyundai_steel_us_plant_policy_capex_false_positive | Hyundai Steel | failed_rerating_policy_CAPEX_false_positive | 2025-03-25 |  |  | 2025-04-22 | false_positive_score | 정책 CAPEX headline은 funding/ROI가 없으면 false positive가 된다. |
| r4_loop13_lgchem_hanwha_dl_yncc_petchem_credit_watch | LG Chem / Hanwha Solutions / DL Chemical / YNCC | 4C-watch_credit_spread | 2025-12-19 |  |  | 2025-08-27 | thesis_break_watch | YNCC D/E 249%와 cracker shutdown은 구조조정 relief 전에 보는 credit/spread 4C-watch다. |
| r4_loop13_lotte_hd_hyundai_petchem_restructuring_relief | Lotte Chemical / HD Hyundai Chemical | success_candidate_policy_relief | 2026-02-24 |  | 2026-02-24 |  | success_candidate_policy_relief | Daesan shutdown과 2T won support package는 위기 완화다. spread/FCF 전에는 Stage 3가 아니다. |
| r4_loop13_lotte_chemical_overseas_portfolio_spread_gate | Lotte Chemical | success_candidate_but_spread_gated | 2025-11-13 |  | 2025-11-13 |  | success_candidate_but_insufficient_price_data | 해외 capex와 asset sale은 utilization, ROIC, spread가 확인되어야 한다. |
| r4_loop13_poongsan_defense_metals_mna_rumor | Poongsan | event_premium_mna_rumor |  |  | 2026-04-09 |  | event_premium | 방산금속 optionality는 있지만 M&A rumor는 Green이 아니다. |

## Interpretation
- R4 Stage 3 is not the word strategic minerals, graphite, lithium, steel tariff, capex, restructuring, or defense metals.
- Korea Zinc is strategic-minerals Stage 2 plus governance/dilution 4B-watch, not operating Green.
- POSCO Future M graphite/lithium moves are price events until contracts, certification, margin and FCF confirm.
- Steel tariff relief is two-sided because domestic protection and export tariff damage can coexist.
- Petrochemical restructuring is relief before spread, OPM, debt cleanup and FCF prove out.
- Poongsan M&A rumor is event premium until a confirmed transaction, ammunition orders, copper spread or cash return appears.
