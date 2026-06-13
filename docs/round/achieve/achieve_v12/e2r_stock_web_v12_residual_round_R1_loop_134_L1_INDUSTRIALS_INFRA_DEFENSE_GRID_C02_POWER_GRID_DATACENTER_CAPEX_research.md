# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 134
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = mixed_c02_second_pass_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery
production_scoring_changed = false
shadow_weight_only = true
```
This loop adds 5 new independent cases, 3 counterexamples, and 3 residual errors for R1/L1/C02_POWER_GRID_DATACENTER_CAPEX.
## 1. Current Calibrated Profile Assumption
```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```
## 2. Round / Large Sector / Canonical Archetype Scope
C02 is mapped to R1 / L1. This file is not a live scan and does not produce trade recommendations. It is a second C02 pass after the earlier loop 125, but it uses a fresh set of symbols and trigger families: `033100`, `103590`, `062040`, `147830`, `017040`.
## 3. Previous Coverage / Duplicate Avoidance Check
The latest No-Repeat Index lists C02 as Priority 0 with 10 representative rows. In this active session, loop 125 already added a C02 set using `267260`, `298040`, `024840`, and `006340`. This loop avoids those symbols and avoids the earlier exact duplicate key pattern.

```text
known_session_c02_symbols_avoided = 267260|298040|024840|006340
new_symbols_this_loop = 033100|103590|062040|147830|017040
hard_duplicate_keys_reused = 0
```
## 4. Stock-Web OHLC Input / Price Source Validation
```text
price_source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```
| item | value |
|---|---:|
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |

## 5. Historical Eligibility Gate
| symbol | entry_date | forward_window_trading_days | corporate_action_window_status | calibration_usable |
|---|---:|---:|---|---|
| 033100 | 2024-03-22 | 180 | clean_180D_window | True |
| 103590 | 2024-03-22 | 180 | clean_180D_window | True |
| 062040 | 2024-07-29 | 180 | clean_180D_window | True |
| 147830 | 2024-07-18 | 180 | clean_180D_window | True |
| 017040 | 2024-08-01 | 180 | clean_180D_window | True |

All representative trigger rows use the six canonical MFE/MAE fields. No trigger row is emitted without `entry_date`, `entry_price`, `MFE_30D_pct`, `MAE_30D_pct`, `MFE_90D_pct`, `MAE_90D_pct`, `MFE_180D_pct`, and `MAE_180D_pct`.
## 6. Canonical Archetype Compression Map
| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| DISTRIBUTION_TRANSFORMER_US_EXPORT_BACKLOG_MARGIN_BRIDGE | C02_POWER_GRID_DATACENTER_CAPEX | orderbook/CAPA/margin bridge |
| HEAVY_ELECTRIC_TRANSFORMER_ORDERBOOK_CAPEX_EXPANSION | C02_POWER_GRID_DATACENTER_CAPEX | orderbook/CAPA/margin bridge |
| IPO_TRANSFORMER_BACKLOG_CAPA_EXPANSION_HIGH_MAE_GUARD | C02_POWER_GRID_DATACENTER_CAPEX | theme/policy/IPO high-MAE guardrail inside C02 |
| HVDC_POLICY_SPILLOVER_WITHOUT_COMPANY_SPECIFIC_ORDER | C02_POWER_GRID_DATACENTER_CAPEX | theme/policy/IPO high-MAE guardrail inside C02 |
| GENERIC_POWER_SHORTAGE_SWITCHGEAR_THEME_WITHOUT_BACKLOG | C02_POWER_GRID_DATACENTER_CAPEX | theme/policy/IPO high-MAE guardrail inside C02 |

## 7. Case Selection Summary
| symbol | company | case_type | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 033100 | 제룡전기 | structural_success | Stage2-Actionable | 2024-03-22 | 2024-03-22 | 33100 | 105.14 | -1.96 | 204.23 | -1.96 | 204.23 | -1.96 | current_profile_correct |
| 103590 | 일진전기 | structural_success | Stage2-Actionable | 2024-03-22 | 2024-03-22 | 19100 | 28.27 | -7.17 | 58.38 | -7.17 | 58.38 | -13.09 | current_profile_correct |
| 062040 | 산일전기 | high_mae_success | Stage2-Actionable | 2024-07-23 | 2024-07-29 | 50200 | 22.11 | -44.12 | 37.85 | -44.12 | 66.33 | -44.12 | current_profile_too_early |
| 147830 | 제룡산업 | failed_rerating | Stage4B | 2024-07-18 | 2024-07-18 | 8820 | 8.39 | -30.27 | 8.39 | -41.72 | 8.39 | -48.92 | current_profile_false_positive |
| 017040 | 광명전기 | failed_rerating | Stage4B | 2024-08-01 | 2024-08-01 | 2100 | 1.43 | -26.19 | 1.43 | -40.48 | 1.43 | -41.76 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 0
current_profile_error_count = 3
calibration_usable_case_count = 5
```
The positive side requires a company-specific bridge: orderbook/backlog, capacity, customer/export mix, and margin/revision visibility. The counterexample side shows that C02 still needs a finer valve: policy spillover, generic switchgear theme, and IPO overheat can look like C02 but behave like 4B/high-MAE risk.
## 9. Evidence Source Map
| case_id | source_url | secondary_url | source_quality | evidence summary |
|---|---|---|---|---|
| C02_R1_L134_033100_20240322_EXPORT_BACKLOG_MARGIN_POSITIVE | https://v.daum.net/v/20240322060139928 | https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23 | direct_article_or_report | 미국 변압기 수요 증가, 제룡전기 2023년 매출/영업이익 급증, 수출 비중과 수주잔고가 함께 확인된 early Stage2-Actionable bridge. |
| C02_R1_L134_103590_20240322_HEAVY_ELECTRIC_ORDERBOOK_CAPEX_POSITIVE | https://v.daum.net/v/20240322060139928 | https://www.dailyinvest.kr/news/articleView.html?idxno=65222 | direct_article_or_report | 중전기 매출·영업이익 개선, 해외 중심 수주잔고, 증설 자금 확보가 함께 확인되어 단순 전력망 테마가 아니라 orderbook→capacity→margin bridge로 압축된다. |
| C02_R1_L134_062040_20240729_IPO_BACKLOG_CAPA_HIGH_MAE | https://file.myasset.com/sitemanager/upload/2024/0722/135433/20240722135433477_0_ko.pdf | https://www.smedaily.co.kr/news/articleView.html?idxno=295250 | direct_article_or_report | 상장 직전 리포트에서 수주잔고, 신규수주 전망, 미국/유럽 전력망 교체, 데이터센터향 변압기 수요, CAPA 증설이 확인되지만 IPO entry는 -44% MAE를 동반했다. |
| C02_R1_L134_147830_20240718_HVDC_POLICY_SPILLOVER_COUNTER | https://www.thebigdata.co.kr/view.php?ud=202407180434263151cd1e7f0bdf_23 | https://www.thebigdata.co.kr/view.php?ud=202408010430473967cd1e7f0bdf_23 | theme_event_proxy_with_company_context | 한전-UAE HVDC 기대와 전력망 theme가 강했지만 제룡산업 자체의 확정 수주·고객·마진 bridge가 부족했고 entry 직후 peak 이후 큰 MAE가 발생했다. |
| C02_R1_L134_017040_20240801_GENERIC_POWER_SHORTAGE_COUNTER | https://www.thebigdata.co.kr/view.php?ud=20240801051258360cd1e7f0bdf_23 | https://alphasquare.co.kr/home/theme-factor?theme-id=44 | theme_event_proxy_with_company_context | 전력기기 수급 불균형/AI 데이터센터/전력망 테마 기사였지만 광명전기 자체의 수주잔고·고객·마진 bridge가 없었고 180D MFE 1.4% 대비 MAE -41.8%가 발생했다. |

## 10. Price Data Source Map
| symbol | price_shard_path | profile_path | profile CA caveat |
|---|---|---|---|
| 033100 | atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv | atlas/symbol_profiles/033/033100.json | corporate_action candidates end before 2015; 2024 window clean |
| 103590 | atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv | atlas/symbol_profiles/103/103590.json | candidate date 2024-02-13 avoided; entry after candidate date |
| 062040 | atlas/ohlcv_tradable_by_symbol_year/062/062040/2024.csv | atlas/symbol_profiles/062/062040.json | no corporate action candidate in profile |
| 147830 | atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv | atlas/symbol_profiles/147/147830.json | candidate dates end in 2021; 2024 window clean |
| 017040 | atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv | atlas/symbol_profiles/017/017040.json | candidate dates end in 2001; 2024 window clean |

## 11. Case-by-Case Trigger Grid
### C02_R1_L134_033100_20240322_EXPORT_BACKLOG_MARGIN_POSITIVE — 제룡전기 (033100)
- role: `structural_success` / `positive`
- trigger: `Stage2-Actionable` on `2024-03-22`, entry `2024-03-22` at `33100`
- evidence: 미국 변압기 수요 증가, 제룡전기 2023년 매출/영업이익 급증, 수출 비중과 수주잔고가 함께 확인된 early Stage2-Actionable bridge.
- current_profile_verdict: `current_profile_correct`
- path: MFE90 `204.23%`, MAE90 `-1.96%`, MFE180 `204.23%`, MAE180 `-1.96%`.

### C02_R1_L134_103590_20240322_HEAVY_ELECTRIC_ORDERBOOK_CAPEX_POSITIVE — 일진전기 (103590)
- role: `structural_success` / `positive`
- trigger: `Stage2-Actionable` on `2024-03-22`, entry `2024-03-22` at `19100`
- evidence: 중전기 매출·영업이익 개선, 해외 중심 수주잔고, 증설 자금 확보가 함께 확인되어 단순 전력망 테마가 아니라 orderbook→capacity→margin bridge로 압축된다.
- current_profile_verdict: `current_profile_correct`
- path: MFE90 `58.38%`, MAE90 `-7.17%`, MFE180 `58.38%`, MAE180 `-13.09%`.

### C02_R1_L134_062040_20240729_IPO_BACKLOG_CAPA_HIGH_MAE — 산일전기 (062040)
- role: `high_mae_success` / `counterexample`
- trigger: `Stage2-Actionable` on `2024-07-23`, entry `2024-07-29` at `50200`
- evidence: 상장 직전 리포트에서 수주잔고, 신규수주 전망, 미국/유럽 전력망 교체, 데이터센터향 변압기 수요, CAPA 증설이 확인되지만 IPO entry는 -44% MAE를 동반했다.
- current_profile_verdict: `current_profile_too_early`
- path: MFE90 `37.85%`, MAE90 `-44.12%`, MFE180 `66.33%`, MAE180 `-44.12%`.

### C02_R1_L134_147830_20240718_HVDC_POLICY_SPILLOVER_COUNTER — 제룡산업 (147830)
- role: `failed_rerating` / `counterexample`
- trigger: `Stage4B` on `2024-07-18`, entry `2024-07-18` at `8820`
- evidence: 한전-UAE HVDC 기대와 전력망 theme가 강했지만 제룡산업 자체의 확정 수주·고객·마진 bridge가 부족했고 entry 직후 peak 이후 큰 MAE가 발생했다.
- current_profile_verdict: `current_profile_false_positive`
- path: MFE90 `8.39%`, MAE90 `-41.72%`, MFE180 `8.39%`, MAE180 `-48.92%`.

### C02_R1_L134_017040_20240801_GENERIC_POWER_SHORTAGE_COUNTER — 광명전기 (017040)
- role: `failed_rerating` / `counterexample`
- trigger: `Stage4B` on `2024-08-01`, entry `2024-08-01` at `2100`
- evidence: 전력기기 수급 불균형/AI 데이터센터/전력망 테마 기사였지만 광명전기 자체의 수주잔고·고객·마진 bridge가 없었고 180D MFE 1.4% 대비 MAE -41.8%가 발생했다.
- current_profile_verdict: `current_profile_false_positive`
- path: MFE90 `1.43%`, MAE90 `-40.48%`, MFE180 `1.43%`, MAE180 `-41.76%`.

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C02_R1_L134_T01_033100_STAGE2A_20240322 | 033100 | 2024-03-22 | 33100 | 105.14 | -1.96 | 204.23 | -1.96 | 204.23 | -1.96 | 2024-07-11 | 100700 | -63.7 |
| C02_R1_L134_T02_103590_STAGE2A_20240322 | 103590 | 2024-03-22 | 19100 | 28.27 | -7.17 | 58.38 | -7.17 | 58.38 | -13.09 | 2024-05-29 | 30250 | -45.12 |
| C02_R1_L134_T03_062040_STAGE2A_20240729 | 062040 | 2024-07-29 | 50200 | 22.11 | -44.12 | 37.85 | -44.12 | 66.33 | -44.12 | 2025-01-15 | 83500 | -48.08 |
| C02_R1_L134_T04_147830_STAGE4B_20240718 | 147830 | 2024-07-18 | 8820 | 8.39 | -30.27 | 8.39 | -41.72 | 8.39 | -48.92 | 2024-07-18 | 9560 | -52.88 |
| C02_R1_L134_T05_017040_STAGE4B_20240801 | 017040 | 2024-08-01 | 2100 | 1.43 | -26.19 | 1.43 | -40.48 | 1.43 | -41.76 | 2024-08-01 | 2130 | -42.58 |

## 13. Current Calibrated Profile Stress Test
| case_id | expected current profile behavior | actual path verdict | residual error |
|---|---|---|---|
| C02_R1_L134_033100_20240322_EXPORT_BACKLOG_MARGIN_POSITIVE | allow Stage2-Actionable | good alignment | current_profile_correct |
| C02_R1_L134_103590_20240322_HEAVY_ELECTRIC_ORDERBOOK_CAPEX_POSITIVE | allow Stage2-Actionable | good alignment | current_profile_correct |
| C02_R1_L134_062040_20240729_IPO_BACKLOG_CAPA_HIGH_MAE | may over-promote unless bridge gate blocks theme spillover | needs C02 guard refinement | current_profile_too_early |
| C02_R1_L134_147830_20240718_HVDC_POLICY_SPILLOVER_COUNTER | may over-promote unless bridge gate blocks theme spillover | needs C02 guard refinement | current_profile_false_positive |
| C02_R1_L134_017040_20240801_GENERIC_POWER_SHORTAGE_COUNTER | may over-promote unless bridge gate blocks theme spillover | needs C02 guard refinement | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison
No Stage3-Green trigger is emitted in this loop. The useful comparison is Stage2-Actionable early bridge versus late/unsafe price extension. `033100` and `103590` justify Stage2-Actionable; `062040` says Stage2 can be correct structurally but unsafe without IPO/high-MAE guard; `147830` and `017040` should be kept as Stage4B-watch or blocked positive promotion.

## 15. 4B Local vs Full-window Timing Audit
| symbol | trigger_type | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict | evidence_type |
|---|---|---:|---:|---|---|
| 033100 | Stage2-Actionable | null | null | not_applicable_no_4b_trigger | none |
| 103590 | Stage2-Actionable | null | null | not_applicable_no_4b_trigger | none |
| 062040 | Stage2-Actionable | 0.82 | 0.6 | ipo_entry_needs_high_mae_guard_not_full_4b | valuation_blowoff|positioning_overheat |
| 147830 | Stage4B | 0.92 | 0.92 | good_local_4b_watch_theme_spillover_not_full_positive | explicit_event_cap|positioning_overheat |
| 017040 | Stage4B | 0.99 | 0.99 | good_local_4b_watch_no_company_specific_bridge | price_only|positioning_overheat |

## 16. 4C Protection Audit
No hard Stage4C row is emitted. The C02 problem here is not confirmed thesis collapse; it is false positive promotion before a company-specific orderbook/margin bridge. `147830` and `017040` are better treated as local 4B-watch / positive-stage block than hard 4C.

## 17. Sector-Specific Rule Candidate
```text
sector_specific_rule_candidate = L1_C02_POWER_GRID_ORDERBOOK_CAPA_MARGIN_VS_THEME_SPILLOVER_GATE_V2
rule_scope = sector_specific
proposal = In L1 power-grid/data-center-capex names, Stage2-Actionable requires at least two of: named customer/orderbook, backlog or delivery visibility, CAPA lock/expansion, margin/revision bridge. Theme-only policy spillover or peer-multiple rerating routes to Stage4B-watch.
```
## 18. Canonical-Archetype Rule Candidate
```text
canonical_archetype_rule_candidate = C02_ORDERBOOK_CAPA_MARGIN_BRIDGE_AND_HIGH_MAE_GUARD_V2
new_axis_proposed = c02_structural_orderbook_vs_theme_spillover_high_mae_gate
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened = null
```
## 19. Before / After Backtest Comparison
| profile_id | scope | hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | Global calibrated profile, no C02 leaf correction | none | 5 | all 5 | 62.06 | -27.09 | 67.75 | -29.97 | 0.6 | 0 | 0 | n/a | n/a | n/a | mixed; residual false positives remain |
| P0b | e2r_2_0_baseline_reference | Baseline before stock-web calibration | none | 5 | all 5 | 62.06 | -27.09 | 67.75 | -29.97 | 0.6 | 1 | 0 | n/a | n/a | n/a | too permissive to theme/RS |
| P1 | sector_specific_candidate_profile | L1 capex names require orderbook/capa/margin bridge | L1 bridge gate + high-MAE watch | 5 | 033100|103590 only for actionable | 131.31 | -4.56 | 131.31 | -7.53 | 0.2 | 0 | 0 | n/a | 0.91 | 0.84 | better alignment |
| P2 | canonical_archetype_candidate_profile | C02-specific orderbook/CAPA/margin bridge vs theme-spillover gate | canonical C02 bridge + IPO/high-MAE guard | 5 | 033100|103590; 062040 watch only | 131.31 | -4.56 | 131.31 | -7.53 | 0 | 0 | 0 | n/a | 0.95 | 0.84 | best alignment |
| P3 | counterexample_guard_profile | Theme/policy spillover and IPO overheat are 4B-watch until fresh order evidence | theme_spillover_block + ipo_high_mae_guard | 5 | 147830|017040 blocked; 062040 watch | 15.89 | -42.11 | 25.38 | -44.93 | 0 | 0 | 0 | n/a | 0.95 | 0.84 | guardrail improves bad-entry rate |

## 20. Score-Return Alignment Matrix
| symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | component_delta_explanation | MFE90 | MAE90 | verdict |
|---|---:|---|---:|---|---|---:|---:|---|
| 033100 | 78 | Stage2-Actionable | 81 | Stage3-Yellow-watch | keep Stage2-Actionable; allow Yellow-watch because backlog+margin bridge existed before full peak. | 204.23 | -1.96 | current_profile_correct |
| 103590 | 74 | Stage2-Actionable | 77 | Stage2-Actionable | keep Stage2-Actionable; cap Green until segment margin/revision confirms. | 58.38 | -7.17 | current_profile_correct |
| 062040 | 76 | Stage2-Actionable | 68 | Stage2-Watch | subtract IPO/high-MAE guard despite strong backlog/CAPA evidence; wait for post-listing stabilization or fresh order. | 37.85 | -44.12 | current_profile_too_early |
| 147830 | 62 | Stage2-or-local-4B | 49 | Stage4B-Watch | block positive promotion unless policy event becomes a company-specific order or margin bridge. | 8.39 | -41.72 | current_profile_false_positive |
| 017040 | 55 | Stage2-watch-or-theme | 42 | Stage4B-Watch | block Stage2-Actionable; require company-specific backlog/order bridge for switchgear theme names. | 1.43 | -40.48 | current_profile_false_positive |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | mixed_c02_second_pass_leaf_set | 2 | 3 | 2 | 0 | 5 | 0 | 5 | 5 | 3 | L1_C02_POWER_GRID_ORDERBOOK_CAPA_MARGIN_VS_THEME_SPILLOVER_GATE_V2 | C02_ORDERBOOK_CAPA_MARGIN_BRIDGE_AND_HIGH_MAE_GUARD_V2 | index_baseline_10_to_15; session_aware_14_to_19 |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
residual_error_types_found: c02_theme_spillover_false_positive|ipo_structural_case_high_mae|policy_event_without_company_specific_order
new_axis_proposed: c02_structural_orderbook_vs_theme_spillover_high_mae_gate
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min|stage3_green_revision_min|hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L1_C02_POWER_GRID_ORDERBOOK_CAPA_MARGIN_VS_THEME_SPILLOVER_GATE_V2
canonical_archetype_rule_candidate: C02_ORDERBOOK_CAPA_MARGIN_BRIDGE_AND_HIGH_MAE_GUARD_V2
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
## 23. Validation Scope / Non-Validation Scope
Validation scope: historical trigger-level calibration only; stock-web tradable raw OHLC; clean 180D window; canonical C02. Non-validation scope: live candidate discovery, investment recommendation, production scoring change, brokerage/API integration, price route discovery.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c02_structural_orderbook_vs_theme_spillover_high_mae_gate,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,Require two non-price bridge fields and route IPO/theme spillover to watch,Improves false-positive/high-MAE filtering without weakening positive 033100/103590,C02_R1_L134_T01_033100_STAGE2A_20240322|C02_R1_L134_T02_103590_STAGE2A_20240322|C02_R1_L134_T03_062040_STAGE2A_20240729|C02_R1_L134_T04_147830_STAGE4B_20240718|C02_R1_L134_T05_017040_STAGE4B_20240801,5,5,3,medium,canonical_shadow_only,not production; post-calibrated residual
```
## 25. Machine-Readable Rows
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C02_R1_L134_033100_20240322_EXPORT_BACKLOG_MARGIN_POSITIVE", "symbol": "033100", "company_name": "제룡전기", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "DISTRIBUTION_TRANSFORMER_US_EXPORT_BACKLOG_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "미국 변압기 수요 증가, 제룡전기 2023년 매출/영업이익 급증, 수출 비중과 수주잔고가 함께 확인된 early Stage2-Actionable bridge."}
{"row_type": "case", "case_id": "C02_R1_L134_103590_20240322_HEAVY_ELECTRIC_ORDERBOOK_CAPEX_POSITIVE", "symbol": "103590", "company_name": "일진전기", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "HEAVY_ELECTRIC_TRANSFORMER_ORDERBOOK_CAPEX_EXPANSION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "중전기 매출·영업이익 개선, 해외 중심 수주잔고, 증설 자금 확보가 함께 확인되어 단순 전력망 테마가 아니라 orderbook→capacity→margin bridge로 압축된다."}
{"row_type": "case", "case_id": "C02_R1_L134_062040_20240729_IPO_BACKLOG_CAPA_HIGH_MAE", "symbol": "062040", "company_name": "산일전기", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "IPO_TRANSFORMER_BACKLOG_CAPA_EXPANSION_HIGH_MAE_GUARD", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_guardrail_case", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "상장 직전 리포트에서 수주잔고, 신규수주 전망, 미국/유럽 전력망 교체, 데이터센터향 변압기 수요, CAPA 증설이 확인되지만 IPO entry는 -44% MAE를 동반했다."}
{"row_type": "case", "case_id": "C02_R1_L134_147830_20240718_HVDC_POLICY_SPILLOVER_COUNTER", "symbol": "147830", "company_name": "제룡산업", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "HVDC_POLICY_SPILLOVER_WITHOUT_COMPANY_SPECIFIC_ORDER", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_guardrail_case", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "한전-UAE HVDC 기대와 전력망 theme가 강했지만 제룡산업 자체의 확정 수주·고객·마진 bridge가 부족했고 entry 직후 peak 이후 큰 MAE가 발생했다."}
{"row_type": "case", "case_id": "C02_R1_L134_017040_20240801_GENERIC_POWER_SHORTAGE_COUNTER", "symbol": "017040", "company_name": "광명전기", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GENERIC_POWER_SHORTAGE_SWITCHGEAR_THEME_WITHOUT_BACKLOG", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_guardrail_case", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "전력기기 수급 불균형/AI 데이터센터/전력망 테마 기사였지만 광명전기 자체의 수주잔고·고객·마진 bridge가 없었고 180D MFE 1.4% 대비 MAE -41.8%가 발생했다."}
{"row_type": "trigger", "trigger_id": "C02_R1_L134_T01_033100_STAGE2A_20240322", "case_id": "C02_R1_L134_033100_20240322_EXPORT_BACKLOG_MARGIN_POSITIVE", "symbol": "033100", "company_name": "제룡전기", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "DISTRIBUTION_TRANSFORMER_US_EXPORT_BACKLOG_MARGIN_BRIDGE", "sector": "industrial_power_grid_datacenter_capex", "primary_archetype": "C02_POWER_GRID_DATACENTER_CAPEX", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-22", "evidence_available_at_that_date": "2024-03-22", "evidence_source": "https://v.daum.net/v/20240322060139928", "evidence_secondary": "https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv", "profile_path": "atlas/symbol_profiles/033/033100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-22", "entry_price": 33100.0, "MFE_30D_pct": 105.14, "MFE_90D_pct": 204.23, "MFE_180D_pct": 204.23, "MFE_1Y_pct": 204.23, "MFE_2Y_pct": null, "MAE_30D_pct": -1.96, "MAE_90D_pct": -1.96, "MAE_180D_pct": -1.96, "MAE_1Y_pct": -18.43, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-07-11", "peak_price": 100700.0, "drawdown_after_peak_pct": -63.7, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4b_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "c02_us_distribution_transformer_export_backlog_margin_positive", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C02_POWER_GRID_DATACENTER_CAPEX_033100_2024-03-22_Stage2Actionable", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C02_R1_L134_T02_103590_STAGE2A_20240322", "case_id": "C02_R1_L134_103590_20240322_HEAVY_ELECTRIC_ORDERBOOK_CAPEX_POSITIVE", "symbol": "103590", "company_name": "일진전기", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "HEAVY_ELECTRIC_TRANSFORMER_ORDERBOOK_CAPEX_EXPANSION", "sector": "industrial_power_grid_datacenter_capex", "primary_archetype": "C02_POWER_GRID_DATACENTER_CAPEX", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-22", "evidence_available_at_that_date": "2024-03-22", "evidence_source": "https://v.daum.net/v/20240322060139928", "evidence_secondary": "https://www.dailyinvest.kr/news/articleView.html?idxno=65222", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "capacity_or_volume_route", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv", "profile_path": "atlas/symbol_profiles/103/103590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-22", "entry_price": 19100.0, "MFE_30D_pct": 28.27, "MFE_90D_pct": 58.38, "MFE_180D_pct": 58.38, "MFE_1Y_pct": 96.6, "MFE_2Y_pct": null, "MAE_30D_pct": -7.17, "MAE_90D_pct": -7.17, "MAE_180D_pct": -13.09, "MAE_1Y_pct": -13.09, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-29", "peak_price": 30250.0, "drawdown_after_peak_pct": -45.12, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4b_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "c02_heavy_electric_orderbook_capacity_expansion_positive", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C02_POWER_GRID_DATACENTER_CAPEX_103590_2024-03-22_Stage2Actionable", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C02_R1_L134_T03_062040_STAGE2A_20240729", "case_id": "C02_R1_L134_062040_20240729_IPO_BACKLOG_CAPA_HIGH_MAE", "symbol": "062040", "company_name": "산일전기", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "IPO_TRANSFORMER_BACKLOG_CAPA_EXPANSION_HIGH_MAE_GUARD", "sector": "industrial_power_grid_datacenter_capex", "primary_archetype": "C02_POWER_GRID_DATACENTER_CAPEX", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-23", "evidence_available_at_that_date": "2024-07-23", "evidence_source": "https://file.myasset.com/sitemanager/upload/2024/0722/135433/20240722135433477_0_ko.pdf", "evidence_secondary": "https://www.smedaily.co.kr/news/articleView.html?idxno=295250", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "capacity_or_volume_route", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/062/062040/2024.csv", "profile_path": "atlas/symbol_profiles/062/062040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-29", "entry_price": 50200.0, "MFE_30D_pct": 22.11, "MFE_90D_pct": 37.85, "MFE_180D_pct": 66.33, "MFE_1Y_pct": 162.55, "MFE_2Y_pct": null, "MAE_30D_pct": -44.12, "MAE_90D_pct": -44.12, "MAE_180D_pct": -44.12, "MAE_1Y_pct": -44.12, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-15", "peak_price": 83500.0, "drawdown_after_peak_pct": -48.08, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "ipo_entry_needs_high_mae_guard_not_full_4b", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "false_break_high_mae_success", "trigger_outcome_label": "c02_ipo_backlog_capa_positive_but_high_mae_entry", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C02_POWER_GRID_DATACENTER_CAPEX_062040_2024-07-29_Stage2Actionable", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C02_R1_L134_T04_147830_STAGE4B_20240718", "case_id": "C02_R1_L134_147830_20240718_HVDC_POLICY_SPILLOVER_COUNTER", "symbol": "147830", "company_name": "제룡산업", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "HVDC_POLICY_SPILLOVER_WITHOUT_COMPANY_SPECIFIC_ORDER", "sector": "industrial_power_grid_datacenter_capex", "primary_archetype": "C02_POWER_GRID_DATACENTER_CAPEX", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2024-07-18", "evidence_available_at_that_date": "2024-07-18", "evidence_source": "https://www.thebigdata.co.kr/view.php?ud=202407180434263151cd1e7f0bdf_23", "evidence_secondary": "https://www.thebigdata.co.kr/view.php?ud=202408010430473967cd1e7f0bdf_23", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "valuation_blowoff", "positioning_overheat", "price_only_local_peak", "contract_delay"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv", "profile_path": "atlas/symbol_profiles/147/147830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-18", "entry_price": 8820.0, "MFE_30D_pct": 8.39, "MFE_90D_pct": 8.39, "MFE_180D_pct": 8.39, "MFE_1Y_pct": 8.39, "MFE_2Y_pct": null, "MAE_30D_pct": -30.27, "MAE_90D_pct": -41.72, "MAE_180D_pct": -48.92, "MAE_1Y_pct": -48.92, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 9560.0, "drawdown_after_peak_pct": -52.88, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_local_4b_watch_theme_spillover_not_full_positive", "four_b_evidence_type": ["explicit_event_cap", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "c02_hvdc_policy_spillover_false_positive_stage4b", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C02_POWER_GRID_DATACENTER_CAPEX_147830_2024-07-18_Stage4B", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C02_R1_L134_T05_017040_STAGE4B_20240801", "case_id": "C02_R1_L134_017040_20240801_GENERIC_POWER_SHORTAGE_COUNTER", "symbol": "017040", "company_name": "광명전기", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GENERIC_POWER_SHORTAGE_SWITCHGEAR_THEME_WITHOUT_BACKLOG", "sector": "industrial_power_grid_datacenter_capex", "primary_archetype": "C02_POWER_GRID_DATACENTER_CAPEX", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2024-08-01", "evidence_available_at_that_date": "2024-08-01", "evidence_source": "https://www.thebigdata.co.kr/view.php?ud=20240801051258360cd1e7f0bdf_23", "evidence_secondary": "https://alphasquare.co.kr/home/theme-factor?theme-id=44", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv", "profile_path": "atlas/symbol_profiles/017/017040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-01", "entry_price": 2100.0, "MFE_30D_pct": 1.43, "MFE_90D_pct": 1.43, "MFE_180D_pct": 1.43, "MFE_1Y_pct": 6.67, "MFE_2Y_pct": null, "MAE_30D_pct": -26.19, "MAE_90D_pct": -40.48, "MAE_180D_pct": -41.76, "MAE_1Y_pct": -53.24, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-01", "peak_price": 2130.0, "drawdown_after_peak_pct": -42.58, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "good_local_4b_watch_no_company_specific_bridge", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_not_needed_but_positive_stage_blocked", "trigger_outcome_label": "c02_generic_power_shortage_switchgear_false_positive_stage4b", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C02_POWER_GRID_DATACENTER_CAPEX_017040_2024-08-01_Stage4B", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C02_R1_L134_033100_20240322_EXPORT_BACKLOG_MARGIN_POSITIVE", "trigger_id": "C02_R1_L134_T01_033100_STAGE2A_20240322", "symbol": "033100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 76, "backlog_visibility_score": 83, "margin_bridge_score": 82, "revision_score": 72, "relative_strength_score": 84, "customer_quality_score": 78, "policy_or_regulatory_score": 66, "valuation_repricing_score": 70, "execution_risk_score": 22, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 8}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 76, "backlog_visibility_score": 83, "margin_bridge_score": 82, "revision_score": 72, "relative_strength_score": 84, "customer_quality_score": 78, "policy_or_regulatory_score": 66, "valuation_repricing_score": 70, "execution_risk_score": 22, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 8, "c02_specific_bridge_guard_adjustment": 3}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow-watch", "changed_components": ["c02_orderbook_capa_margin_bridge_gate", "theme_spillover_block", "ipo_high_mae_guard"], "component_delta_explanation": "keep Stage2-Actionable; allow Yellow-watch because backlog+margin bridge existed before full peak.", "MFE_90D_pct": 204.23, "MAE_90D_pct": -1.96, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C02_R1_L134_103590_20240322_HEAVY_ELECTRIC_ORDERBOOK_CAPEX_POSITIVE", "trigger_id": "C02_R1_L134_T02_103590_STAGE2A_20240322", "symbol": "103590", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 74, "backlog_visibility_score": 80, "margin_bridge_score": 71, "revision_score": 68, "relative_strength_score": 73, "customer_quality_score": 72, "policy_or_regulatory_score": 62, "valuation_repricing_score": 66, "execution_risk_score": 25, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 8}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 74, "backlog_visibility_score": 80, "margin_bridge_score": 71, "revision_score": 68, "relative_strength_score": 73, "customer_quality_score": 72, "policy_or_regulatory_score": 62, "valuation_repricing_score": 66, "execution_risk_score": 25, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 8, "c02_specific_bridge_guard_adjustment": 3}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["c02_orderbook_capa_margin_bridge_gate", "theme_spillover_block", "ipo_high_mae_guard"], "component_delta_explanation": "keep Stage2-Actionable; cap Green until segment margin/revision confirms.", "MFE_90D_pct": 58.38, "MAE_90D_pct": -7.17, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C02_R1_L134_062040_20240729_IPO_BACKLOG_CAPA_HIGH_MAE", "trigger_id": "C02_R1_L134_T03_062040_STAGE2A_20240729", "symbol": "062040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 78, "backlog_visibility_score": 82, "margin_bridge_score": 62, "revision_score": 54, "relative_strength_score": 65, "customer_quality_score": 76, "policy_or_regulatory_score": 69, "valuation_repricing_score": 72, "execution_risk_score": 58, "legal_or_contract_risk_score": 14, "dilution_cb_risk_score": 12, "accounting_trust_risk_score": 10}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 78, "backlog_visibility_score": 82, "margin_bridge_score": 62, "revision_score": 54, "relative_strength_score": 65, "customer_quality_score": 76, "policy_or_regulatory_score": 69, "valuation_repricing_score": 72, "execution_risk_score": 58, "legal_or_contract_risk_score": 14, "dilution_cb_risk_score": 12, "accounting_trust_risk_score": 10, "c02_specific_bridge_guard_adjustment": -8}, "weighted_score_after": 68, "stage_label_after": "Stage2-Watch", "changed_components": ["c02_orderbook_capa_margin_bridge_gate", "theme_spillover_block", "ipo_high_mae_guard"], "component_delta_explanation": "subtract IPO/high-MAE guard despite strong backlog/CAPA evidence; wait for post-listing stabilization or fresh order.", "MFE_90D_pct": 37.85, "MAE_90D_pct": -44.12, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C02_R1_L134_147830_20240718_HVDC_POLICY_SPILLOVER_COUNTER", "trigger_id": "C02_R1_L134_T04_147830_STAGE4B_20240718", "symbol": "147830", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 34, "backlog_visibility_score": 38, "margin_bridge_score": 26, "revision_score": 24, "relative_strength_score": 78, "customer_quality_score": 36, "policy_or_regulatory_score": 69, "valuation_repricing_score": 64, "execution_risk_score": 62, "legal_or_contract_risk_score": 36, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 12}, "weighted_score_before": 62, "stage_label_before": "Stage2-or-local-4B", "raw_component_scores_after": {"contract_score": 34, "backlog_visibility_score": 38, "margin_bridge_score": 26, "revision_score": 24, "relative_strength_score": 78, "customer_quality_score": 36, "policy_or_regulatory_score": 69, "valuation_repricing_score": 64, "execution_risk_score": 62, "legal_or_contract_risk_score": 36, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 12, "c02_specific_bridge_guard_adjustment": -13}, "weighted_score_after": 49, "stage_label_after": "Stage4B-Watch", "changed_components": ["c02_orderbook_capa_margin_bridge_gate", "theme_spillover_block", "ipo_high_mae_guard"], "component_delta_explanation": "block positive promotion unless policy event becomes a company-specific order or margin bridge.", "MFE_90D_pct": 8.39, "MAE_90D_pct": -41.72, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C02_R1_L134_017040_20240801_GENERIC_POWER_SHORTAGE_COUNTER", "trigger_id": "C02_R1_L134_T05_017040_STAGE4B_20240801", "symbol": "017040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 22, "backlog_visibility_score": 24, "margin_bridge_score": 18, "revision_score": 16, "relative_strength_score": 45, "customer_quality_score": 25, "policy_or_regulatory_score": 62, "valuation_repricing_score": 52, "execution_risk_score": 68, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 12}, "weighted_score_before": 55, "stage_label_before": "Stage2-watch-or-theme", "raw_component_scores_after": {"contract_score": 22, "backlog_visibility_score": 24, "margin_bridge_score": 18, "revision_score": 16, "relative_strength_score": 45, "customer_quality_score": 25, "policy_or_regulatory_score": 62, "valuation_repricing_score": 52, "execution_risk_score": 68, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 12, "c02_specific_bridge_guard_adjustment": -13}, "weighted_score_after": 42, "stage_label_after": "Stage4B-Watch", "changed_components": ["c02_orderbook_capa_margin_bridge_gate", "theme_spillover_block", "ipo_high_mae_guard"], "component_delta_explanation": "block Stage2-Actionable; require company-specific backlog/order bridge for switchgear theme names.", "MFE_90D_pct": 1.43, "MAE_90D_pct": -40.48, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R1", "loop": 134, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["c02_theme_spillover_false_positive", "ipo_structural_case_high_mae", "policy_event_without_company_specific_order"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```
## Batch Ingest Self-Audit
```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
## 26. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

## 27. Next Round State
```text
completed_round = R1
completed_loop = 134
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|C14_EV_DEMAND_SLOWDOWN_4B_4C|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
## 28. Source Notes
- `033100` / `103590`: https://v.daum.net/v/20240322060139928 and https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23
- `062040`: https://file.myasset.com/sitemanager/upload/2024/0722/135433/20240722135433477_0_ko.pdf
- `147830`: https://www.thebigdata.co.kr/view.php?ud=202407180434263151cd1e7f0bdf_23 and https://www.thebigdata.co.kr/view.php?ud=202408010430473967cd1e7f0bdf_23
- `017040`: https://www.thebigdata.co.kr/view.php?ud=20240801051258360cd1e7f0bdf_23
- Price atlas: https://github.com/Songdaiki/stock-web
