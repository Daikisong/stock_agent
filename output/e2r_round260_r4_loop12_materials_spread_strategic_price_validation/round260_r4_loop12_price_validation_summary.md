# Round 260 R4 Loop 12 Materials Spread Strategic Resources Price Validation

This pack is calibration-only. Production scoring and candidate generation are unchanged.

## Summary

- source_round: docs/round/round_260.md
- round_id: round_188
- large_sector: MATERIALS_SPREAD_STRATEGIC
- cases: 8
- success_candidate: 2
- event_premium: 2
- failed_rerating: 2
- watch_cases: 2
- hard_4c: 0
- Stage 3 dated cases: 0
- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false

## Case Matrix

| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |
|---|---|---|---|---|---|---|---|---|
| r4_loop12_poongsan_defense_metals_mna_rumor | Poongsan | event_premium / defense-metals optionality |  |  | 2026-04-09 |  | event_premium_insufficient_price_data | M&A rumor는 Green이 아니다. 예: 실제 인수계약, 탄약 수주, 구리 spread, 현금환원이 확인돼야 Stage 2 이후로 간다. |
| r4_loop12_korea_zinc_critical_minerals_dilution_watch | Korea Zinc | success_candidate + dilution/governance 4B-watch | 2026-03-12 |  | 2025-12-31 |  | success_candidate_dilution_watch | 전략광물 구조는 강하지만, offtake·최저가격·마진·FCF·희석 통과 전에는 Green이 아니다. |
| r4_loop12_china_rare_earth_end_use_restriction_overlay | Korean rare-earth-dependent manufacturers | 4C-watch / strategic supply-chain overlay |  |  |  | 2025-04-22 | thesis_break_watch | 전략자원 수혜와 동시에 중국 end-use restriction이 붙으면 RedTeam overlay다. |
| r4_loop12_posco_hyundai_seah_steel_tariff_two_sided | POSCO Holdings / Hyundai Steel / SeAH Steel | event_premium + 4C-watch | 2025-02-20 |  | 2025-02-20 | 2025-06-02 | event_premium_thesis_break_watch | 국내 anti-dumping relief만 보면 Stage 2지만, U.S. tariff가 export margin을 때리면 Green이 막힌다. |
| r4_loop12_hyundai_steel_us_capex_false_positive | Hyundai Steel | failed_rerating / policy CAPEX false positive | 2025-03-25 |  | 2025-03-25 | 2025-04-22 | false_positive_score | 미국 공장과 tariff hedge는 좋아 보이지만, 고객수요·spread·margin·FCF가 없으면 policy CAPEX false positive다. |
| r4_loop12_lgchem_hanwha_dl_yncc_petrochemical_credit_watch | LG Chem / Hanwha Solutions / DL Chemical / YNCC | 4C-watch / petrochemical overcapacity | 2025-12-19 |  |  | 2025-08-27 | thesis_break_watch | 정부가 capacity cut을 요구한 것은 sector crisis 증거다. spread와 FCF 전에는 구조적 Green이 아니다. |
| r4_loop12_lotte_hd_hyundai_chemical_restructuring_relief | Lotte Chemical / HD Hyundai Chemical | failed_rerating_then_policy_relief | 2026-02-24 |  |  |  | failed_rerating_then_policy_relief | Daesan shutdown과 정부지원은 crisis relief다. spread·OPM·FCF가 돌아오기 전 Stage 3가 아니다. |
| r4_loop12_korea_critical_minerals_policy_relief | Korea critical-minerals policy basket | success_candidate policy relief | 2026-02-05 |  |  |  | success_candidate_policy_relief | 정책은 좋은 Stage 2 relief지만 공급계약·offtake·재고·마진으로 닫혀야 한다. |

## Interpretation
- Poongsan is defense-metals optionality, but M&A rumor is event premium, not Green.
- Korea Zinc is strategic-minerals Stage 2 plus dilution/governance watch.
- China rare-earth end-use pressure is a sector 4C-watch overlay.
- Steel tariff is two-sided: domestic anti-dumping relief can be offset by U.S. export tariff risk.
- Hyundai Steel U.S. plant is policy CAPEX false positive until demand, spread, margin and FCF confirm.
- Petrochemical restructuring is relief; spread, OPM, FCF and debt cleanup are required before Green.
