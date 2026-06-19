# E2R v12 Residual Research — R2 loop 129 — L2_AI_SEMICONDUCTOR_ELECTRONICS / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 129
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C10 recovery-cycle early false positives and order-conversion confirmation after recent C05/C01/C13/C15 runs
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_VS_BETA_CHASE
loop_objective: sector_specific_rule_discovery; canonical_archetype_rule_candidate; memory recovery positive/counterexample balance; 4B/4C high-MAE path; direct URL quality repair; complete_30_90_180_MFE_MAE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patched: false
live_candidate_mode: false
auto_trading_allowed: false
```

## 1. Selection / Novelty Check

This run follows the v12 coverage-index scheduler, not a mechanical R1→R13 loop. The current ledger says every C01~C32 canonical archetype already exceeds 80 representative rows, so the useful work is URL/proxy quality repair, counterexample/positive balance, and residual rule discovery. Recent local outputs in this session covered C05, C01, C13, and C15, so this run moves to **C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE** under **R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS**.

C10 currently has a high information-confidence runtime weight and a known need to distinguish true order conversion from broad memory-cycle beta. This loop therefore deliberately uses less-repeated symbols than the current top-symbol list and mixes early memory-recovery positives with post-headline late-chase 4B/4C failures.

```yaml
hard_duplicate_key_checked: canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 4
positive_case_count: 3
counterexample_count: 3
stage4b_or_4c_case_count: 3
source_proxy_only_count: 0
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
```

## 2. Price Source Validation

Stock-Web manifest/schema basis used in every trigger row:

```yaml
price_atlas_repo: https://github.com/Songdaiki/stock-web
manifest: atlas/manifest.json
schema: atlas/schema.json
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
MFE_formula: (max_high_from_entry_window - entry_close) / entry_close
MAE_formula: (min_low_from_entry_window - entry_close) / entry_close
required_windows: 30D, 90D, 180D
corporate_action_window_rule: entry_date through D+180 must be clean for calibration_usable=true
```

Profile caveats checked from Stock-Web symbol profiles:

```yaml
281820_KCTech: corporate_action_candidate_dates=[]; 180D_window_clean=true
064760_TCK: corporate_action_candidate_dates=[]; 180D_window_clean=true
036810_FST: corporate_action_candidate_dates=[2000-05-02, 2004-05-06]; 180D_window_clean=true
160980_CYMECHS: corporate_action_candidate_dates=[2017-11-10, 2017-11-17]; 180D_window_clean=true
079370_ZEUS: corporate_action_candidate_dates=[2024-01-16, 2024-02-08]; selected_entry=2024-04-25; 180D_window_clean=true
086390_UNITEST: corporate_action_candidate_dates=[2007-07-16, 2010-05-03]; 180D_window_clean=true
```

## 3. Case Table

| case_id | symbol | company | trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | outcome | verdict |
|---|---:|---|---|---|---:|---:|---:|---|---|
| C10_KCTECH_2023_SEMI_MEMORY_CAPEX_RECOVERY | 281820 | 케이씨텍 | Stage2-Actionable 2023-09-12 | 2023-09-13 @ 21,650 | 6.93% / -14.46% | 56.81% / -14.46% | 149.88% / -14.46% | positive_memory_capex_equipment_follow_through | current_profile_correct_but_order_conversion_gate_needed |
| C10_TCK_2023_MEMORY_FAB_RECOVERY_SIC_COMPONENTS | 064760 | 티씨케이 | Stage2 2023-09-12 | 2023-09-13 @ 93,200 | 11.48% / -12.98% | 27.25% / -13.63% | 51.39% / -13.63% | positive_process_component_follow_through | current_profile_too_late_if_consumable_component_quality_underweighted |
| C10_FST_2024_SEMI_Q1_MEMORY_CAPEX_UTILIZATION_RECOVERY | 036810 | 에프에스티 | Stage3-Yellow 2024-02-14 | 2024-02-15 @ 21,850 | 14.19% / -2.52% | 91.53% / -2.52% | 91.53% / -21.97% | positive_equipment_component_recovery_with_drawdown_guard | current_profile_correct_stage3_yellow_not_green_due_180D_MAE |
| C10_CYMECHS_2024_SKHYNIX_DRAM_INVESTMENT_LATE_BETA_CHASE | 160980 | 싸이맥스 | Stage4B 2024-04-24 | 2024-04-25 @ 22,150 | 7.22% / -12.91% | 7.22% / -50.38% | 7.22% / -66.55% | counterexample_late_beta_chase_high_MAE | current_profile_false_positive_if_customer_capex_headline_overcredited |
| C10_ZEUS_2024_SKHYNIX_DRAM_INVESTMENT_CLEANING_EQUIPMENT_4B | 079370 | 제우스 | Stage4B 2024-04-24 | 2024-04-25 @ 16,050 | 24.30% / 0.00% | 24.30% / -34.58% | 24.30% / -36.39% | counterexample_high_MAE_after_local_MFE | current_profile_false_positive_if_cleaning_equipment_map_treated_as_order |
| C10_UNITEST_2024_SKHYNIX_AI_MEMORY_CAPEX_LATE_TESTER_BETA | 086390 | 유니테스트 | Stage4C 2024-06-30 | 2024-07-01 @ 14,470 | 1.59% / -36.63% | 1.59% / -42.29% | 4.56% / -48.38% | counterexample_long_term_capex_no_near_term_order_high_MAE | current_profile_thesis_break_if_long_term_capex_fails_near_term_order_conversion |

## 4. Actual Stock-Web Entry Rows / Peak-Trough Rows

| trigger_id | symbol | entry_date | o | h | l | c | v | 30D peak/trough | 90D peak/trough | 180D peak/trough |
|---|---:|---|---:|---:|---:|---:|---:|---|---|---|
| T1 | 281820 | 2023-09-13 | 21,600 | 22,150 | 21,200 | 21,650 | 24,694 | 2023-10-18 23,150 / 2023-10-31 18,520 | 2024-01-22 33,950 / 2023-10-31 18,520 | 2024-03-08 54,100 / 2023-10-31 18,520 |
| T2 | 064760 | 2023-09-13 | 92,700 | 95,400 | 91,900 | 93,200 | 34,014 | 2023-09-15 103,900 / 2023-10-20 81,100 | 2024-01-02 118,600 / 2023-11-13 80,500 | 2024-04-12 141,100 / 2023-11-13 80,500 |
| T3 | 036810 | 2024-02-15 | 22,100 | 22,550 | 21,700 | 21,850 | 118,863 | 2024-02-20 24,950 / 2024-02-20 21,300 | 2024-06-11 41,850 / 2024-02-20 21,300 | 2024-06-11 41,850 / 2024-10-28 17,050 |
| T4 | 160980 | 2024-04-25 | 20,400 | 22,300 | 19,990 | 22,150 | 644,134 | 2024-05-29 23,750 / 2024-05-10 19,290 | 2024-05-29 23,750 / 2024-09-04 10,990 | 2024-05-29 23,750 / 2024-12-10 7,410 |
| T5 | 079370 | 2024-04-25 | 16,170 | 16,570 | 16,050 | 16,050 | 422,598 | 2024-05-21 19,950 / 2024-04-25 16,050 | 2024-05-21 19,950 / 2024-08-05 10,500 | 2024-05-21 19,950 / 2024-12-09 10,210 |
| T6 | 086390 | 2024-07-01 | 14,520 | 14,600 | 14,340 | 14,470 | 110,403 | 2024-07-03 14,700 / 2024-08-05 9,170 | 2024-07-03 14,700 / 2024-09-11 8,350 | 2025-01-22 15,130 / 2024-12-09 7,470 |

## 5. Case Notes

### T1 — 케이씨텍 / 281820 / positive memory capex equipment follow through

SEMI forecast was an early broad memory capex recovery signal; KCTech has direct CMP/wet-clean equipment exposure. The path validates actionable recovery, but Green needs later order/revenue bridge rather than market forecast alone. Entry uses 2023-09-13 close because the trigger was either disclosed before the local session or treated conservatively as next tradable day. Stock-Web path: 30D 6.93% / -14.46%, 90D 56.81% / -14.46%, 180D 149.88% / -14.46%. Evidence URLs: https://www.semi.org/en/news-media-press-releases/semi-press-releases/2024-globaL-fab-equipment-spending-recovery-expected-after-2023-slowdown-semi-reports, https://www.kctech.com/eng/page/product1.php.

### T2 — 티씨케이 / 064760 / positive process component follow through

TCK is not a pure memory equipment order name; it is a process consumable/component route. It should help Stage2 evidence when memory fab recovery is accompanied by etch/diffusion process-component mapping, not by memory beta alone. Entry uses 2023-09-13 close because the trigger was either disclosed before the local session or treated conservatively as next tradable day. Stock-Web path: 30D 11.48% / -12.98%, 90D 27.25% / -13.63%, 180D 51.39% / -13.63%. Evidence URLs: https://www.semi.org/en/news-media-press-releases/semi-press-releases/2024-globaL-fab-equipment-spending-recovery-expected-after-2023-slowdown-semi-reports, https://www.tck.co.kr/eng/business/SolidSiC.php.

### T3 — 에프에스티 / 036810 / positive equipment component recovery with drawdown guard

Q1 2024 recovery signal was more concrete than 2023 macro forecast. The path shows strong upside, but later drawdown says Yellow is safer than Green unless company order/revision evidence closes the bridge. Entry uses 2024-02-15 close because the trigger was either disclosed before the local session or treated conservatively as next tradable day. Stock-Web path: 30D 14.19% / -2.52%, 90D 91.53% / -2.52%, 180D 91.53% / -21.97%. Evidence URLs: https://www.semi.org/en/news-media-press-releases/semi-press-releases/global-semiconductor-manufacturing-industry-poised-for-2024-expansion-semi-reports, https://www.fstc.co.kr/bbs/content.php?co_id=egreeting.

### T4 — 싸이맥스 / 160980 / counterexample late beta chase high MAE

SK Hynix capex headline is relevant to wafer transfer automation, but without company-specific order conversion this became a late beta trap. The stock gave a short local high then deep MAE. Entry uses 2024-04-25 close because the trigger was either disclosed before the local session or treated conservatively as next tradable day. Stock-Web path: 30D 7.22% / -12.91%, 90D 7.22% / -50.38%, 180D 7.22% / -66.55%. Evidence URLs: https://www.reuters.com/technology/sk-hynix-invest-386-bln-dram-chip-production-base-korea-2024-04-24/, https://cymechs.com/en/.

### T5 — 제우스 / 079370 / counterexample high MAE after local MFE

Zeus has direct semiconductor cleaning equipment exposure, but the 2024-04-25 entry is after its corporate-action candidate dates. The local MFE did not survive 90/180D drawdown, supporting 4B watch rather than positive Stage2. Entry uses 2024-04-25 close because the trigger was either disclosed before the local session or treated conservatively as next tradable day. Stock-Web path: 30D 24.30% / 0.00%, 90D 24.30% / -34.58%, 180D 24.30% / -36.39%. Evidence URLs: https://www.reuters.com/technology/sk-hynix-invest-386-bln-dram-chip-production-base-korea-2024-04-24/, https://www.globalzeus.com/en/sub/products/list.asp?p_cate=10.

### T6 — 유니테스트 / 086390 / counterexample long term capex no near term order high MAE

Long-term SK Hynix AI/memory capex and UniTest memory tester exposure are thematically linked, but without near-term tester order conversion the entry became a clean high-MAE counterexample. Entry uses 2024-07-01 close because the trigger was either disclosed before the local session or treated conservatively as next tradable day. Stock-Web path: 30D 1.59% / -36.63%, 90D 1.59% / -42.29%, 180D 4.56% / -48.38%. Evidence URLs: https://www.reuters.com/technology/south-koreas-sk-hynix-invest-75-bln-by-2028-ai-chips-2024-06-30/, https://www.uni-test.com/en/semiconductor/semiconductor_list.php?part1_idx=2&part2_idx=5.


## 6. Current Calibrated Profile Stress Test

| profile_id | hypothesis | selected reps | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false-positive pressure | missed structural pressure | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | Current profile already gives C10 high information-confidence weight, but may still confuse broad memory recovery headlines with order conversion. | T1~T6 | 34.79% | -26.31% | 54.82% | -33.56% | 3/6 | 1/6 | mixed; needs canonical gate |
| P0b e2r_2_0_baseline_reference | Looser baseline would likely overcredit late customer-capex headlines and miss the 4B/4C route. | T1~T6 | 34.79% | -26.31% | 54.82% | -33.56% | 4/6 | 1/6 | weaker than P0 |
| P1 positive_order_conversion_profile | Early recovery signal plus direct equipment/component map, while requiring order/revenue/revision confirmation before Green. | T1,T2,T3 | 58.53% | -10.20% | 97.60% | -16.68% | 0/3 | 0/3 | best positive alignment |
| P2 late_chase_guard_profile | Customer capex headline without company order conversion becomes local 4B; long-dated capex with high MAE/no near-term order becomes 4C review. | T4,T5,T6 | 11.04% | -42.42% | 12.03% | -50.44% | 0/3 after guard | n/a | best counterexample alignment |
| P3 combined_shadow_profile | Use P1 positive gate plus P2 late-chase 4B/4C guard. | T1~T6 | 34.79% | -26.31% | 54.82% | -33.56% | 0/6 after gate | 0/6 after gate | preferred shadow rule |

## 7. Residual Error / Shadow Rule Candidate

```yaml
new_axis_proposed: C10_MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_GATE
scope: canonical_archetype_specific
sector_specific_rule_candidate: L2 memory-cycle equipment cases need market recovery evidence plus direct equipment/component mapping plus near-term company order/revenue/revision conversion before Stage2-Actionable or Green.
canonical_archetype_rule_candidate: C10 broad memory capex forecast alone is capped at Stage2-Watch; customer capex headline without company order conversion is capped at local 4B; long-dated AI/memory capex with no near-term order conversion and high MAE routes to 4C review.
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - earlier_thesis_break_watch
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
production_scoring_changed: false
shadow_weight_only: true
```

Mechanism:

- **Positive C10** = memory spending/utilization recovery + equipment/component map + low-to-manageable drawdown + later order/revenue bridge optionality. KCTech, TCK, and FST show this path.
- **False-positive C10** = already-matured recovery trade + customer capex headline + no company-specific order conversion. Cymechs and Zeus show local 4B behavior.
- **Harder 4C C10** = long-dated AI/memory capex promise with memory-tester exposure but no near-term tester order bridge and a deep high-MAE path. UniTest July 2024 shows this route.

The waterline is simple: memory recovery is the tide; equipment order conversion is the boat actually moving. If the tide rises but the boat is not tied to a confirmed order/revenue line, the price can float for a few sessions and then drift into a deep MAE channel.

## 8. Machine-Readable JSONL Rows

```jsonl
{"row_type":"trigger","round":"R2","loop":"129","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_VS_BETA_CHASE","case_id":"C10_KCTECH_2023_SEMI_MEMORY_CAPEX_RECOVERY","trigger_id":"T1","symbol":"281820","company":"케이씨텍","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-12","entry_date":"2023-09-13","entry_price":21650.0,"entry_open":21600.0,"entry_high":22150.0,"entry_low":21200.0,"entry_close":21650.0,"entry_volume":24694,"entry_amount":533653850.0,"entry_market_cap":451652687400.0,"entry_market":"KOSPI","MFE_30D_pct":6.9284,"MAE_30D_pct":-14.4573,"peak_30D_date":"2023-10-18","peak_30D_high":23150.0,"trough_30D_date":"2023-10-31","trough_30D_low":18520.0,"MFE_90D_pct":56.8129,"MAE_90D_pct":-14.4573,"peak_90D_date":"2024-01-22","peak_90D_high":33950.0,"trough_90D_date":"2023-10-31","trough_90D_low":18520.0,"MFE_180D_pct":149.8845,"MAE_180D_pct":-14.4573,"peak_180D_date":"2024-03-08","peak_180D_high":54100.0,"trough_180D_date":"2023-10-31","trough_180D_low":18520.0,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_MFE_MAE_clean_180D_window","source_proxy_only":false,"evidence_url_pending":false,"evidence_family":"SEMI_2024_MEMORY_SPENDING_RECOVERY_FORECAST_PLUS_CMP_WET_CLEAN_EQUIPMENT_MAP","trigger_family":"memory_spending_forecast_recovery","evidence_urls":["https://www.semi.org/en/news-media-press-releases/semi-press-releases/2024-globaL-fab-equipment-spending-recovery-expected-after-2023-slowdown-semi-reports","https://www.kctech.com/eng/page/product1.php"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/281/281820.json","corporate_action_candidate_dates":[],"window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C10_20230913_memory_spending_forecast_recovery","representative_for_aggregate":true,"independent_evidence_weight":1.0,"outcome_label":"positive_memory_capex_equipment_follow_through","current_profile_verdict":"current_profile_correct_but_order_conversion_gate_needed"}
{"row_type":"trigger","round":"R2","loop":"129","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_VS_BETA_CHASE","case_id":"C10_TCK_2023_MEMORY_FAB_RECOVERY_SIC_COMPONENTS","trigger_id":"T2","symbol":"064760","company":"티씨케이","trigger_type":"Stage2","trigger_date":"2023-09-12","entry_date":"2023-09-13","entry_price":93200.0,"entry_open":92700.0,"entry_high":95400.0,"entry_low":91900.0,"entry_close":93200.0,"entry_volume":34014,"entry_amount":3167838500.0,"entry_market_cap":1088110000000.0,"entry_market":"KOSDAQ GLOBAL","MFE_30D_pct":11.4807,"MAE_30D_pct":-12.9828,"peak_30D_date":"2023-09-15","peak_30D_high":103900.0,"trough_30D_date":"2023-10-20","trough_30D_low":81100.0,"MFE_90D_pct":27.2532,"MAE_90D_pct":-13.6266,"peak_90D_date":"2024-01-02","peak_90D_high":118600.0,"trough_90D_date":"2023-11-13","trough_90D_low":80500.0,"MFE_180D_pct":51.3948,"MAE_180D_pct":-13.6266,"peak_180D_date":"2024-04-12","peak_180D_high":141100.0,"trough_180D_date":"2023-11-13","trough_180D_low":80500.0,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_MFE_MAE_clean_180D_window","source_proxy_only":false,"evidence_url_pending":false,"evidence_family":"SEMI_2024_KOREA_MEMORY_SPENDING_RECOVERY_PLUS_DRY_ETCH_DIFFUSION_COMPONENT_MAP","trigger_family":"memory_spending_forecast_recovery","evidence_urls":["https://www.semi.org/en/news-media-press-releases/semi-press-releases/2024-globaL-fab-equipment-spending-recovery-expected-after-2023-slowdown-semi-reports","https://www.tck.co.kr/eng/business/SolidSiC.php"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/064/064760.json","corporate_action_candidate_dates":[],"window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C10_20230913_memory_spending_forecast_recovery","representative_for_aggregate":true,"independent_evidence_weight":1.0,"outcome_label":"positive_process_component_follow_through","current_profile_verdict":"current_profile_too_late_if_consumable_component_quality_underweighted"}
{"row_type":"trigger","round":"R2","loop":"129","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_VS_BETA_CHASE","case_id":"C10_FST_2024_SEMI_Q1_MEMORY_CAPEX_UTILIZATION_RECOVERY","trigger_id":"T3","symbol":"036810","company":"에프에스티","trigger_type":"Stage3-Yellow","trigger_date":"2024-02-14","entry_date":"2024-02-15","entry_price":21850.0,"entry_open":22100.0,"entry_high":22550.0,"entry_low":21700.0,"entry_close":21850.0,"entry_volume":118863,"entry_amount":2615776500.0,"entry_market_cap":475385839650.0,"entry_market":"KOSDAQ","MFE_30D_pct":14.1876,"MAE_30D_pct":-2.5172,"peak_30D_date":"2024-02-20","peak_30D_high":24950.0,"trough_30D_date":"2024-02-20","trough_30D_low":21300.0,"MFE_90D_pct":91.5332,"MAE_90D_pct":-2.5172,"peak_90D_date":"2024-06-11","peak_90D_high":41850.0,"trough_90D_date":"2024-02-20","trough_90D_low":21300.0,"MFE_180D_pct":91.5332,"MAE_180D_pct":-21.968,"peak_180D_date":"2024-06-11","peak_180D_high":41850.0,"trough_180D_date":"2024-10-28","trough_180D_low":17050.0,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_MFE_MAE_clean_180D_window","source_proxy_only":false,"evidence_url_pending":false,"evidence_family":"SEMI_Q1_2024_MEMORY_CAPEX_UTILIZATION_RECOVERY_PLUS_PELLICLE_CHILLER_EQUIPMENT_MAP","trigger_family":"fab_utilization_and_memory_capex_recovery","evidence_urls":["https://www.semi.org/en/news-media-press-releases/semi-press-releases/global-semiconductor-manufacturing-industry-poised-for-2024-expansion-semi-reports","https://www.fstc.co.kr/bbs/content.php?co_id=egreeting"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/036/036810.json","corporate_action_candidate_dates":["2000-05-02","2004-05-06"],"window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C10_20240215_fab_utilization_and_memory_capex_recovery","representative_for_aggregate":true,"independent_evidence_weight":1.0,"outcome_label":"positive_equipment_component_recovery_with_drawdown_guard","current_profile_verdict":"current_profile_correct_stage3_yellow_not_green_due_180D_MAE"}
{"row_type":"trigger","round":"R2","loop":"129","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_VS_BETA_CHASE","case_id":"C10_CYMECHS_2024_SKHYNIX_DRAM_INVESTMENT_LATE_BETA_CHASE","trigger_id":"T4","symbol":"160980","company":"싸이맥스","trigger_type":"Stage4B","trigger_date":"2024-04-24","entry_date":"2024-04-25","entry_price":22150.0,"entry_open":20400.0,"entry_high":22300.0,"entry_low":19990.0,"entry_close":22150.0,"entry_volume":644134,"entry_amount":13701439170.0,"entry_market_cap":241971982450.0,"entry_market":"KOSDAQ","MFE_30D_pct":7.2235,"MAE_30D_pct":-12.912,"peak_30D_date":"2024-05-29","peak_30D_high":23750.0,"trough_30D_date":"2024-05-10","trough_30D_low":19290.0,"MFE_90D_pct":7.2235,"MAE_90D_pct":-50.3837,"peak_90D_date":"2024-05-29","peak_90D_high":23750.0,"trough_90D_date":"2024-09-04","trough_90D_low":10990.0,"MFE_180D_pct":7.2235,"MAE_180D_pct":-66.5463,"peak_180D_date":"2024-05-29","peak_180D_high":23750.0,"trough_180D_date":"2024-12-10","trough_180D_low":7410.0,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_MFE_MAE_clean_180D_window","source_proxy_only":false,"evidence_url_pending":false,"evidence_family":"SKHYNIX_DRAM_FAB_INVESTMENT_PLUS_WAFER_TRANSFER_ROBOT_MAP_WITHOUT_ORDER_CONVERSION","trigger_family":"customer_capex_headline_without_order_conversion","evidence_urls":["https://www.reuters.com/technology/sk-hynix-invest-386-bln-dram-chip-production-base-korea-2024-04-24/","https://cymechs.com/en/"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/160/160980.json","corporate_action_candidate_dates":["2017-11-10","2017-11-17"],"window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C10_20240425_customer_capex_headline_without_order_conversion","representative_for_aggregate":true,"independent_evidence_weight":1.0,"outcome_label":"counterexample_late_beta_chase_high_MAE","current_profile_verdict":"current_profile_false_positive_if_customer_capex_headline_overcredited"}
{"row_type":"trigger","round":"R2","loop":"129","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_VS_BETA_CHASE","case_id":"C10_ZEUS_2024_SKHYNIX_DRAM_INVESTMENT_CLEANING_EQUIPMENT_4B","trigger_id":"T5","symbol":"079370","company":"제우스","trigger_type":"Stage4B","trigger_date":"2024-04-24","entry_date":"2024-04-25","entry_price":16050.0,"entry_open":16170.0,"entry_high":16570.0,"entry_low":16050.0,"entry_close":16050.0,"entry_volume":422598,"entry_amount":6845670950.0,"entry_market_cap":497822689500.0,"entry_market":"KOSDAQ","MFE_30D_pct":24.2991,"MAE_30D_pct":0.0,"peak_30D_date":"2024-05-21","peak_30D_high":19950.0,"trough_30D_date":"2024-04-25","trough_30D_low":16050.0,"MFE_90D_pct":24.2991,"MAE_90D_pct":-34.5794,"peak_90D_date":"2024-05-21","peak_90D_high":19950.0,"trough_90D_date":"2024-08-05","trough_90D_low":10500.0,"MFE_180D_pct":24.2991,"MAE_180D_pct":-36.3863,"peak_180D_date":"2024-05-21","peak_180D_high":19950.0,"trough_180D_date":"2024-12-09","trough_180D_low":10210.0,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_MFE_MAE_clean_180D_window","source_proxy_only":false,"evidence_url_pending":false,"evidence_family":"SKHYNIX_DRAM_FAB_INVESTMENT_PLUS_CLEANING_EQUIPMENT_MAP_AFTER_POST_SPLIT_WINDOW","trigger_family":"customer_capex_headline_without_order_conversion","evidence_urls":["https://www.reuters.com/technology/sk-hynix-invest-386-bln-dram-chip-production-base-korea-2024-04-24/","https://www.globalzeus.com/en/sub/products/list.asp?p_cate=10"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/079/079370.json","corporate_action_candidate_dates":["2024-01-16","2024-02-08"],"window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C10_20240425_customer_capex_headline_without_order_conversion","representative_for_aggregate":true,"independent_evidence_weight":1.0,"outcome_label":"counterexample_high_MAE_after_local_MFE","current_profile_verdict":"current_profile_false_positive_if_cleaning_equipment_map_treated_as_order"}
{"row_type":"trigger","round":"R2","loop":"129","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_VS_BETA_CHASE","case_id":"C10_UNITEST_2024_SKHYNIX_AI_MEMORY_CAPEX_LATE_TESTER_BETA","trigger_id":"T6","symbol":"086390","company":"유니테스트","trigger_type":"Stage4C","trigger_date":"2024-06-30","entry_date":"2024-07-01","entry_price":14470.0,"entry_open":14520.0,"entry_high":14600.0,"entry_low":14340.0,"entry_close":14470.0,"entry_volume":110403,"entry_amount":1596661580.0,"entry_market_cap":305810803220.0,"entry_market":"KOSDAQ","MFE_30D_pct":1.5895,"MAE_30D_pct":-36.6275,"peak_30D_date":"2024-07-03","peak_30D_high":14700.0,"trough_30D_date":"2024-08-05","trough_30D_low":9170.0,"MFE_90D_pct":1.5895,"MAE_90D_pct":-42.2944,"peak_90D_date":"2024-07-03","peak_90D_high":14700.0,"trough_90D_date":"2024-09-11","trough_90D_low":8350.0,"MFE_180D_pct":4.5612,"MAE_180D_pct":-48.376,"peak_180D_date":"2025-01-22","peak_180D_high":15130.0,"trough_180D_date":"2024-12-09","trough_180D_low":7470.0,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_MFE_MAE_clean_180D_window","source_proxy_only":false,"evidence_url_pending":false,"evidence_family":"SKHYNIX_LONG_TERM_AI_MEMORY_CAPEX_PLUS_MEMORY_TESTER_MAP_WITHOUT_NEAR_TERM_ORDER","trigger_family":"long_term_ai_memory_capex_late_chase","evidence_urls":["https://www.reuters.com/technology/south-koreas-sk-hynix-invest-75-bln-by-2028-ai-chips-2024-06-30/","https://www.uni-test.com/en/semiconductor/semiconductor_list.php?part1_idx=2&part2_idx=5"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/086/086390.json","corporate_action_candidate_dates":["2007-07-16","2010-05-03"],"window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C10_20240701_long_term_ai_memory_capex_late_chase","representative_for_aggregate":true,"independent_evidence_weight":1.0,"outcome_label":"counterexample_long_term_capex_no_near_term_order_high_MAE","current_profile_verdict":"current_profile_thesis_break_if_long_term_capex_fails_near_term_order_conversion"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_candidate","case_id":"C10_KCTECH_2023_SEMI_MEMORY_CAPEX_RECOVERY","trigger_id":"T1","symbol":"281820","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"eps_fcf_explosion":5,"earnings_visibility":6,"bottleneck_pricing":5,"market_mispricing":6,"valuation_rerating":5,"capital_allocation":2,"information_confidence":7},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"eps_fcf_explosion":6,"earnings_visibility":7,"bottleneck_pricing":6,"market_mispricing":6,"valuation_rerating":5,"capital_allocation":2,"information_confidence":8},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["earnings_visibility","information_confidence","order_conversion_gap","drawdown_guard"],"component_delta_explanation":"C10 signal is upgraded only when memory recovery evidence maps into current-year equipment order/revenue conversion; otherwise market/customer capex headlines are capped as 4B/4C risk.","MFE_90D_pct":56.8129,"MAE_90D_pct":-14.4573,"MFE_180D_pct":149.8845,"MAE_180D_pct":-14.4573,"score_return_alignment_label":"positive_memory_capex_equipment_follow_through","current_profile_verdict":"current_profile_correct_but_order_conversion_gate_needed"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_candidate","case_id":"C10_TCK_2023_MEMORY_FAB_RECOVERY_SIC_COMPONENTS","trigger_id":"T2","symbol":"064760","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"eps_fcf_explosion":4,"earnings_visibility":5,"bottleneck_pricing":5,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":3,"information_confidence":7},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":5,"earnings_visibility":6,"bottleneck_pricing":6,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":3,"information_confidence":8},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["earnings_visibility","information_confidence","order_conversion_gap","drawdown_guard"],"component_delta_explanation":"C10 signal is upgraded only when memory recovery evidence maps into current-year equipment order/revenue conversion; otherwise market/customer capex headlines are capped as 4B/4C risk.","MFE_90D_pct":27.2532,"MAE_90D_pct":-13.6266,"MFE_180D_pct":51.3948,"MAE_180D_pct":-13.6266,"score_return_alignment_label":"positive_process_component_follow_through","current_profile_verdict":"current_profile_too_late_if_consumable_component_quality_underweighted"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_candidate","case_id":"C10_FST_2024_SEMI_Q1_MEMORY_CAPEX_UTILIZATION_RECOVERY","trigger_id":"T3","symbol":"036810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"eps_fcf_explosion":6,"earnings_visibility":7,"bottleneck_pricing":6,"market_mispricing":6,"valuation_rerating":5,"capital_allocation":2,"information_confidence":8},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"eps_fcf_explosion":6,"earnings_visibility":7,"bottleneck_pricing":6,"market_mispricing":6,"valuation_rerating":5,"capital_allocation":2,"information_confidence":8,"drawdown_guard":6},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["earnings_visibility","information_confidence","order_conversion_gap","drawdown_guard"],"component_delta_explanation":"C10 signal is upgraded only when memory recovery evidence maps into current-year equipment order/revenue conversion; otherwise market/customer capex headlines are capped as 4B/4C risk.","MFE_90D_pct":91.5332,"MAE_90D_pct":-2.5172,"MFE_180D_pct":91.5332,"MAE_180D_pct":-21.968,"score_return_alignment_label":"positive_equipment_component_recovery_with_drawdown_guard","current_profile_verdict":"current_profile_correct_stage3_yellow_not_green_due_180D_MAE"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_candidate","case_id":"C10_CYMECHS_2024_SKHYNIX_DRAM_INVESTMENT_LATE_BETA_CHASE","trigger_id":"T4","symbol":"160980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"eps_fcf_explosion":5,"earnings_visibility":5,"bottleneck_pricing":5,"market_mispricing":6,"valuation_rerating":6,"capital_allocation":2,"information_confidence":7},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":3,"earnings_visibility":3,"bottleneck_pricing":4,"market_mispricing":4,"valuation_rerating":4,"capital_allocation":2,"information_confidence":8,"order_conversion_gap":9},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_components":["earnings_visibility","information_confidence","order_conversion_gap","drawdown_guard"],"component_delta_explanation":"C10 signal is upgraded only when memory recovery evidence maps into current-year equipment order/revenue conversion; otherwise market/customer capex headlines are capped as 4B/4C risk.","MFE_90D_pct":7.2235,"MAE_90D_pct":-50.3837,"MFE_180D_pct":7.2235,"MAE_180D_pct":-66.5463,"score_return_alignment_label":"counterexample_late_beta_chase_high_MAE","current_profile_verdict":"current_profile_false_positive_if_customer_capex_headline_overcredited"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_candidate","case_id":"C10_ZEUS_2024_SKHYNIX_DRAM_INVESTMENT_CLEANING_EQUIPMENT_4B","trigger_id":"T5","symbol":"079370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"eps_fcf_explosion":5,"earnings_visibility":5,"bottleneck_pricing":6,"market_mispricing":6,"valuation_rerating":5,"capital_allocation":2,"information_confidence":7},"weighted_score_before":71,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":3,"earnings_visibility":4,"bottleneck_pricing":5,"market_mispricing":4,"valuation_rerating":4,"capital_allocation":2,"information_confidence":8,"order_conversion_gap":8},"weighted_score_after":60,"stage_label_after":"Stage4B","changed_components":["earnings_visibility","information_confidence","order_conversion_gap","drawdown_guard"],"component_delta_explanation":"C10 signal is upgraded only when memory recovery evidence maps into current-year equipment order/revenue conversion; otherwise market/customer capex headlines are capped as 4B/4C risk.","MFE_90D_pct":24.2991,"MAE_90D_pct":-34.5794,"MFE_180D_pct":24.2991,"MAE_180D_pct":-36.3863,"score_return_alignment_label":"counterexample_high_MAE_after_local_MFE","current_profile_verdict":"current_profile_false_positive_if_cleaning_equipment_map_treated_as_order"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C10_candidate","case_id":"C10_UNITEST_2024_SKHYNIX_AI_MEMORY_CAPEX_LATE_TESTER_BETA","trigger_id":"T6","symbol":"086390","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"eps_fcf_explosion":4,"earnings_visibility":4,"bottleneck_pricing":5,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":2,"information_confidence":8},"weighted_score_before":67,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":2,"earnings_visibility":2,"bottleneck_pricing":3,"market_mispricing":3,"valuation_rerating":3,"capital_allocation":2,"information_confidence":8,"thesis_break_risk":10},"weighted_score_after":49,"stage_label_after":"Stage4C","changed_components":["earnings_visibility","information_confidence","order_conversion_gap","drawdown_guard"],"component_delta_explanation":"C10 signal is upgraded only when memory recovery evidence maps into current-year equipment order/revenue conversion; otherwise market/customer capex headlines are capped as 4B/4C risk.","MFE_90D_pct":1.5895,"MAE_90D_pct":-42.2944,"MFE_180D_pct":4.5612,"MAE_180D_pct":-48.376,"score_return_alignment_label":"counterexample_long_term_capex_no_near_term_order_high_MAE","current_profile_verdict":"current_profile_thesis_break_if_long_term_capex_fails_near_term_order_conversion"}
{"row_type":"aggregate","round":"R2","loop":"129","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_VS_BETA_CHASE","representative_trigger_count":6,"positive_case_count":3,"counterexample_count":3,"stage4b_or_4c_case_count":3,"source_proxy_only_count":0,"evidence_url_pending_count":0,"avg_MFE_90D_pct":34.7852,"avg_MAE_90D_pct":-26.3098,"avg_MFE_180D_pct":54.816,"avg_MAE_180D_pct":-33.5601,"profile_error_count":3,"aggregate_verdict":"C10 memory recovery equipment cases need current-year order/revenue conversion gate; broad memory capex or customer capex headlines alone create late beta and high-MAE errors."}
{"row_type":"shadow_weight","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","axis":"C10_memory_capex_recovery_order_conversion_gate","scope":"canonical_archetype_specific","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","earlier_thesis_break_watch","full_4b_requires_non_price_evidence"],"existing_axis_weakened":[],"new_axis_proposed":"C10_MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_GATE","production_scoring_changed":false,"shadow_weight_only":true,"proposed_effect":"Require at least two of memory capex/utilization recovery, explicit customer/fab equipment linkage, current-year order/revenue conversion, and company-specific revision before Stage2-Actionable; cap long-dated capex headlines at 4B watch and route high-MAE/no-order cases to 4C review.","candidate_delta":{"earnings_visibility":1,"information_confidence":1,"bottleneck_pricing":0,"valuation_rerating":-1,"order_conversion_gap_gate":2},"confidence":"medium","evidence_count":6,"counterexample_count":3}
{"row_type":"residual_contribution","round":"R2","loop":"129","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_required_bridge","stage3_yellow_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","earlier_thesis_break_watch"],"residual_error_types_found":["broad_memory_recovery_forecast_overcredit","customer_capex_headline_without_company_order","long_dated_AI_memory_capex_late_chase","process_component_quality_undercredit"],"loop_contribution_label":"C10_memory_recovery_order_conversion_positive_counter_4B_4C_guard","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C10_SAMSUNG_SKHYNIX_MEMORY_PRICE_RECOVERY_CONTEXT_ONLY","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reason":"General memory recovery news is useful context, but without symbol-specific equipment/order conversion it must not be counted as a standalone trigger row.","usage":"context_only_not_representative_weight","evidence_source":"SEMI/Reuters market context only"}
```

## 9. Batch Ingest Self-Audit

```yaml
filename: e2r_stock_web_v12_residual_round_R2_loop_129_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
filename_matches_required_v12_regex: true
metadata_round_matches_filename_round: true
metadata_loop_matches_filename_loop: true
round_sector_consistency: pass
compact_filename_forbidden: pass
trigger_type_canonical_stage_labels_only: pass
all_trigger_rows_have_MFE_30D_pct: true
all_trigger_rows_have_MFE_90D_pct: true
all_trigger_rows_have_MFE_180D_pct: true
all_trigger_rows_have_MAE_30D_pct: true
all_trigger_rows_have_MAE_90D_pct: true
all_trigger_rows_have_MAE_180D_pct: true
same_entry_group_deduplicated: true
all_calibration_usable_rows_have_clean_180D_corporate_action_window: true
source_proxy_only_count: 0
evidence_url_pending_count: 0
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this during the research session. In a separate implementation session, ingest v12 MD files under docs/round, parse the JSONL rows, validate that filename/metadata round and loop match, reject rows missing complete 30D/90D/180D MFE/MAE, deduplicate by same_entry_group_id, and evaluate whether the canonical-specific shadow rule C10_MEMORY_CAPEX_RECOVERY_ORDER_CONVERSION_GATE improves C10 representative trigger alignment without changing global E2R thresholds. Keep production_scoring_changed=false unless a separate promotion report passes validation.
```

## 11. Next Research State

```yaml
completed_round: R2
completed_loop: 129
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C10 recovery-cycle early false positives and order-conversion confirmation
next_recommended_archetypes:
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP direct URL replacement / working-capital 4C confirmation
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE backlog-to-FCF counterexample repair
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA utilization failure direct-source repair
  - C15_MATERIAL_SPREAD_SUPERCYCLE direct URL replacement for proxy rows
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE additional tester/socket late-chase 4B/4C compression
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
