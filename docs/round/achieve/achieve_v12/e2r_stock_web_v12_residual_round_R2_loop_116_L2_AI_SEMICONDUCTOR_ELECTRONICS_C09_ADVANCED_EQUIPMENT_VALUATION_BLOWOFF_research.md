# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```yaml
completed_round: R2
completed_loop: 116
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows / C09 static rows 10, need-to-30 20
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass
loop_objective: "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | C09_order_revenue_bridge_boundary_validation | canonical_archetype_compression"
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 2 counterexamples, and 5 residual errors for R2/L2/C09.

## 1. Current Calibrated Profile Assumption
- before_profile_id: `e2r_2_1_stock_web_calibrated_proxy`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- after_profile_id: `proposed_C09_advanced_equipment_shadow_profile`
- Existing global axes are not re-proposed as global rules. They are stress-tested inside C09 only.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| selected_round | R2 |
| selected_loop | 116 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF |
| fine_archetype_id | mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass |
| scope verdict | pass: C06~C10 maps to R2/L2 |

## 3. Previous Coverage / Duplicate Avoidance Check
- No-Repeat Index static snapshot marks `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` as Priority 0 with 10 representative rows and need-to-30 of 20.
- This conversation already produced C09 loop 113/114/115; this file uses loop 116 and avoids the prior C09 symbols: `322310`, `348210`, `240810`, `319660`, `101490`, `036930`, `140860`, `064290`, `036810`, `098460`, `095610`, `089970`, `084370`, `092870`, `033160`.
- New C09 symbol set: `039030`, `217190`, `396470`, `403870`, `122640`.
- Hard duplicate key check: no repeated `{canonical_archetype_id + symbol + trigger_type + entry_date}` within the current C09 session chain.

## 4. Stock-Web OHLC Input / Price Source Validation
- manifest_path: `atlas/manifest.json`
- schema_path: `atlas/schema.json`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- raw_shard_root: `atlas/ohlcv_raw_by_symbol_year`
- manifest_max_date: `2026-02-20`
- price basis: `tradable_raw`, raw/unadjusted, corporate-action windows blocked by default.

## 5. Historical Eligibility Gate
| symbol | company | entry_date | forward_window_trading_days | corporate_action_window_status | calibration_usable | price_shard_path | profile_path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 039030 | 이오테크닉스 | 2023-09-07 | 180 | clean_180D_window | True | atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv | atlas/symbol_profiles/039/039030.json |
| 217190 | 제너셈 | 2023-12-08 | 180 | clean_180D_window | True | atlas/ohlcv_tradable_by_symbol_year/217/217190/2023.csv | atlas/symbol_profiles/217/217190.json |
| 396470 | 워트 | 2024-05-13 | 180 | clean_180D_window | True | atlas/ohlcv_tradable_by_symbol_year/396/396470/2024.csv | atlas/symbol_profiles/396/396470.json |
| 403870 | HPSP | 2024-02-02 | 180 | clean_180D_window | True | atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv | atlas/symbol_profiles/403/403870.json |
| 122640 | 예스티 | 2024-06-04 | 180 | clean_180D_window | True | atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv | atlas/symbol_profiles/122/122640.json |

## 6. Canonical Archetype Compression Map
| fine trigger family | compressed canonical | rule interpretation |
|---|---|---|
| HPA / high-pressure anneal monopoly | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | equipment quality alone is not enough when valuation is already blown out |
| laser annealing / grooving / stealth dicing | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | customer and application quality can support Stage3 only when revenue conversion is visible |
| HBM wafer mounter signed order | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | signed order is positive, but smallcap post-peak drawdown still needs 4B watch |
| THC/environment-control direct vendor | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | named customer route can create MFE, but weak contract amount/margin bridge caps Green |
| cumulative HBM equipment order headline | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | cumulative order headline without margin/revenue bridge becomes high-MAE counterexample |

## 7. Case Selection Summary
| case_id | symbol | company_name | case_type | positive_or_counterexample | trigger_date | entry_date | evidence_family | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C09_R2_L116_039030_EOTECH_LASER_ANNEALING_POSITIVE_WITH_4B | 039030 | 이오테크닉스 | structural_success | positive | 2023-09-06 | 2023-09-07 | laser_annealing_hbm_optional_growth_positive_with_late_4b_watch | current_profile_4B_too_late |
| C09_R2_L116_217190_GENESEM_HBM_WAFER_MOUNTER_POSITIVE_HIGH_MAE | 217190 | 제너셈 | high_mae_success | positive | 2023-12-08 | 2023-12-08 | signed_hbm_equipment_order_positive_but_180d_high_mae | current_profile_4B_too_late |
| C09_R2_L116_396470_WOT_TAYLOR_THC_DIRECT_VENDOR_PRICE_BLOWOFF | 396470 | 워트 | price_moved_without_evidence | positive | 2024-05-10 | 2024-05-13 | direct_vendor_grid_like_equipment_mfe_but_theme_blowoff | current_profile_false_positive |
| C09_R2_L116_403870_HPSP_HPA_MONOPOLY_VALUATION_BLOWOFF | 403870 | HPSP | failed_rerating | counterexample | 2024-02-01 | 2024-02-02 | hpa_monopoly_quality_but_entry_after_theme_blowoff_failed_rerating | current_profile_false_positive |
| C09_R2_L116_122640_YEST_HBM_ORDER_REVENUE_GAP_BLOWOFF | 122640 | 예스티 | false_positive_green | counterexample | 2024-06-03 | 2024-06-04 | hbm_equipment_cumulative_order_but_revenue_bridge_gap_high_mae | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
- positive_case_count: 3
- counterexample_count: 2
- 4B_case_count: 5
- 4C_case_count: 0
- balance verdict: pass. C09 shows both structural positives and high-MAE optionality blowoff cases.

## 9. Evidence Source Map
| symbol | trigger_date | source_name | source_url | evidence_available_at_that_date |
| --- | --- | --- | --- | --- |
| 039030 | 2023-09-06 | 아시아경제, 2023-09-06, HBM 수혜 이오테크닉스 구조적 성장 기대 | https://view.asiae.co.kr/article/2023082913041816228 | 삼성전자향 레이저 어닐링 공급, HBM3/HBM3e CAPA 확대 시 레이저 어닐링 수요 증가, 스텔스 다이싱/그루빙 장비 시양산 및 수주 가능성 |
| 217190 | 2023-12-08 | 대신증권 Issue Comment, 2023-12-08, HBM 제조용 장비 수주 코멘트 | https://money2.daishin.com/PDF/Out/intranet_data/product/researchcenter/report/2023/12/48602_genesem_issue_comment.pdf | SK하이닉스향 HBM 제조용 Wafer Mounter 장비 75.8억원 수주, 2022년 매출 대비 12.7%, 계약기간 2023-12-06~2024-04-26 |
| 396470 | 2024-05-10 | 아이뉴스24/다음, 2024-05-10, 삼성 테일러 공장 THC 직접 공급 | https://v.daum.net/v/bL11mgGkMB?f=p | 삼성전자 USA 오스틴/Taylor 팹 THC 직접 납품 1차 벤더 전환 예정, 삼성전자·SK하이닉스 국내외 공장 THC 납품 확대와 HBM 공정 영역 확장 기대 |
| 403870 | 2024-02-01 | 매일경제 영문, 2024-02-01, 고압 수소 어닐링 장비 양산 성공 | https://www.mk.co.kr/en/economy/10934475 | 세계 최초 고압 수소 어닐링 장비 양산, 고객 CAPA가 non-memory에서 memory로 확대, 신공장 완공으로 연간 생산능력 증가 기대 |
| 122640 | 2024-06-03 | 이데일리, 2024-06-03, HBM 핵심 장비 누적 수주액 380억원 돌파 | https://marketin.edaily.co.kr/News/ReadE?newsId=02794566638918112 | 60억원 HBM 핵심 장비 공급계약과 누적 HBM 장비 수주 380억원 돌파, 신규 상압장비 초도 물량 및 EDS 퍼니스 공급 이력, 고압어닐링 장비 수주 논의 |

## 10. Price Data Source Map
| symbol | entry_date | price_shard_path | profile_path | price_basis | price_adjustment_status | stock_web_manifest_max_date |
| --- | --- | --- | --- | --- | --- | --- |
| 039030 | 2023-09-07 | atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv | atlas/symbol_profiles/039/039030.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| 217190 | 2023-12-08 | atlas/ohlcv_tradable_by_symbol_year/217/217190/2023.csv | atlas/symbol_profiles/217/217190.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| 396470 | 2024-05-13 | atlas/ohlcv_tradable_by_symbol_year/396/396470/2024.csv | atlas/symbol_profiles/396/396470.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| 403870 | 2024-02-02 | atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv | atlas/symbol_profiles/403/403870.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| 122640 | 2024-06-04 | atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv | atlas/symbol_profiles/122/122640.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |

## 11. Case-by-Case Trigger Grid
| symbol | trigger_type | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields | trigger_outcome_label |
| --- | --- | --- | --- | --- | --- | --- |
| 039030 | Stage2-Actionable | public_event_or_disclosure,customer_or_order_quality,capacity_or_volume_route,early_revision_signal | durable_customer_confirmation,repeat_order_or_conversion | valuation_blowoff,positioning_overheat,price_only_local_peak |  | laser_annealing_hbm_optional_growth_positive_with_late_4b_watch |
| 217190 | Stage2-Actionable | public_event_or_disclosure,customer_or_order_quality,backlog_or_delivery_visibility | durable_customer_confirmation,repeat_order_or_conversion | valuation_blowoff,positioning_overheat,price_only_local_peak |  | signed_hbm_equipment_order_positive_but_180d_high_mae |
| 396470 | Stage2-Actionable | public_event_or_disclosure,customer_or_order_quality,capacity_or_volume_route | durable_customer_confirmation | valuation_blowoff,positioning_overheat,price_only_local_peak |  | direct_vendor_grid_like_equipment_mfe_but_theme_blowoff |
| 403870 | Stage2-Actionable | public_event_or_disclosure,customer_or_order_quality,capacity_or_volume_route,relative_strength | durable_customer_confirmation | valuation_blowoff,positioning_overheat,price_only_local_peak |  | hpa_monopoly_quality_but_entry_after_theme_blowoff_failed_rerating |
| 122640 | Stage2-Actionable | public_event_or_disclosure,customer_or_order_quality,backlog_or_delivery_visibility | repeat_order_or_conversion | valuation_blowoff,contract_delay,price_only_local_peak |  | hbm_equipment_cumulative_order_but_revenue_bridge_gap_high_mae |

## 12. Trigger-Level OHLC Backtest Tables
| symbol | company_name | trigger_date | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | positive_or_counterexample | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 039030 | 이오테크닉스 | 2023-09-06 | 2023-09-07 | 163900.00 | 1.59 | -20.01 | 26.60 | -20.01 | 71.45 | -20.01 | 2024-04-12 | 281000.00 | -30.82 | positive | current_profile_4B_too_late |
| 217190 | 제너셈 | 2023-12-08 | 2023-12-08 | 12600.00 | 17.06 | -1.98 | 37.30 | -4.60 | 37.30 | -40.56 | 2024-03-07 | 17300.00 | -56.71 | positive | current_profile_4B_too_late |
| 396470 | 워트 | 2024-05-10 | 2024-05-13 | 9870.00 | 67.68 | -9.42 | 85.31 | -9.42 | 85.31 | -34.45 | 2024-06-26 | 18290.00 | -64.63 | positive | current_profile_false_positive |
| 403870 | HPSP | 2024-02-01 | 2024-02-02 | 46850.00 | 36.39 | -6.51 | 36.39 | -23.91 | 36.39 | -51.65 | 2024-02-15 | 63900.00 | -64.55 | counterexample | current_profile_false_positive |
| 122640 | 예스티 | 2024-06-03 | 2024-06-04 | 17840.00 | 25.84 | -3.81 | 25.84 | -19.73 | 25.84 | -56.78 | 2024-07-16 | 22450.00 | -65.66 | counterexample | current_profile_false_positive |

## 13. Current Calibrated Profile Stress Test
### 039030 이오테크닉스
- Current profile expected behavior: Stage3-Yellow from strong C09 equipment evidence and relative strength.
- Actual path: MFE90 26.6%, MAE90 -20.01%, MFE180 71.45%, MAE180 -20.01%, peak 2024-04-12 then drawdown -30.82%.
- Stress verdict: `current_profile_4B_too_late`. Stage2 bonus is acceptable, but Stage3/Green requires a stricter signed-order/revenue/margin bridge and local 4B overlay.

### 217190 제너셈
- Current profile expected behavior: Stage3-Yellow from strong C09 equipment evidence and relative strength.
- Actual path: MFE90 37.3%, MAE90 -4.6%, MFE180 37.3%, MAE180 -40.56%, peak 2024-03-07 then drawdown -56.71%.
- Stress verdict: `current_profile_4B_too_late`. Stage2 bonus is acceptable, but Stage3/Green requires a stricter signed-order/revenue/margin bridge and local 4B overlay.

### 396470 워트
- Current profile expected behavior: Stage2-Actionable borderline Stage3 from strong C09 equipment evidence and relative strength.
- Actual path: MFE90 85.31%, MAE90 -9.42%, MFE180 85.31%, MAE180 -34.45%, peak 2024-06-26 then drawdown -64.63%.
- Stress verdict: `current_profile_false_positive`. Stage2 bonus is acceptable, but Stage3/Green requires a stricter signed-order/revenue/margin bridge and local 4B overlay.

### 403870 HPSP
- Current profile expected behavior: Stage3-Yellow from strong C09 equipment evidence and relative strength.
- Actual path: MFE90 36.39%, MAE90 -23.91%, MFE180 36.39%, MAE180 -51.65%, peak 2024-02-15 then drawdown -64.55%.
- Stress verdict: `current_profile_false_positive`. Stage2 bonus is acceptable, but Stage3/Green requires a stricter signed-order/revenue/margin bridge and local 4B overlay.

### 122640 예스티
- Current profile expected behavior: Stage3-Yellow from strong C09 equipment evidence and relative strength.
- Actual path: MFE90 25.84%, MAE90 -19.73%, MFE180 25.84%, MAE180 -56.78%, peak 2024-07-16 then drawdown -65.66%.
- Stress verdict: `current_profile_false_positive`. Stage2 bonus is acceptable, but Stage3/Green requires a stricter signed-order/revenue/margin bridge and local 4B overlay.

## 14. Stage2 / Yellow / Green Comparison
- Stage2-Actionable is still useful because all five cases had non-price evidence: public event/disclosure, customer/order quality, or capacity route.
- Stage3-Yellow is too permissive when C09 evidence is only technology optionality or market-share quality without signed/named order, delivery timing, revenue recognition, or margin bridge.
- Stage3-Green remains intentionally rare in this loop. No case receives a clean Green trigger because all observed paths need local 4B watch or revenue-bridge confirmation.
- green_lateness_ratio: `not_applicable` for all representative rows because no confirmed Stage3-Green trigger is emitted.

## 15. 4B Local vs Full-window Timing Audit
| symbol | local/full peak proxy | peak_date | peak_price | post_peak_trough_date | drawdown_after_peak_pct | 4B verdict |
|---|---:|---|---:|---|---:|---|
| 039030 | price path peak in 180D window | 2024-04-12 | 281000 | 2024-05-31 | -30.82 | local_4B_watch_required; do not treat price-only local peak as full 4B without non-price slowdown evidence |
| 217190 | price path peak in 180D window | 2024-03-07 | 17300 | 2024-08-05 | -56.71 | local_4B_watch_required; do not treat price-only local peak as full 4B without non-price slowdown evidence |
| 396470 | price path peak in 180D window | 2024-06-26 | 18290 | 2024-12-02 | -64.63 | local_4B_watch_required; do not treat price-only local peak as full 4B without non-price slowdown evidence |
| 403870 | price path peak in 180D window | 2024-02-15 | 63900 | 2024-08-05 | -64.55 | local_4B_watch_required; do not treat price-only local peak as full 4B without non-price slowdown evidence |
| 122640 | price path peak in 180D window | 2024-07-16 | 22450 | 2024-12-09 | -65.66 | local_4B_watch_required; do not treat price-only local peak as full 4B without non-price slowdown evidence |

## 16. 4C Protection Audit
- No hard 4C trigger is emitted in this loop.
- None of the five cases has contract cancellation, qualification failure, accounting/trust break, or regulatory rejection at trigger date.
- Protection label: `thesis_break_watch_only`, not `hard_4c_success`.

## 17. Sector-Specific Rule Candidate
```text
L2_C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_BRIDGE_AND_OPTIONALITY_4B_SPLIT
```
Rule meaning: in L2, advanced semiconductor equipment evidence should be split into (a) named/signed order with delivery and revenue bridge, (b) customer/technology optionality with Stage2 only, and (c) valuation/positioning blowoff requiring local 4B watch.

## 18. Canonical-Archetype Rule Candidate
```text
C09_ADVANCED_EQUIPMENT_REQUIRES_NAMED_ORDER_REVENUE_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP_FOURTH_PASS
```
C09 must not promote to Stage3-Yellow solely from HBM/EUV/HPA/laser-equipment optionality. Promotion requires named customer/order, delivery timing, revenue recognition, and at least preliminary margin bridge. Fast MFE followed by large MAE becomes local 4B watch, not a clean Green.

## 19. Before / After Backtest Comparison
| profile_id | scope | hypothesis | eligible | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | existing calibrated profile with general price-only blowoff guard | 5 | 42.29 | -15.53 | 51.26 | -40.69 | 0.40 | 0 | 0 | directionally useful but still too permissive for C09 optionality |
| P0b_e2r_2_0_baseline_reference | rollback_reference | old broad rerating proxy; too much weight on relative strength/valuation | 5 | 42.29 | -15.53 | 51.26 | -40.69 | 0.80 | 0 | 0 | too early and too valuation-sensitive |
| P1_L2_sector_specific_candidate | sector_specific | L2 advanced equipment needs named customer/order and revenue timing before Stage3 | 5 | 42.29 | -15.53 | 51.26 | -40.69 | 0.20 | 1 | 1 | better balance; EO/Genesem remain eligible, HPSP/YEST capped |
| P2_C09_canonical_candidate | canonical_archetype_specific | C09 splits signed-order/revenue bridge positives from optionality blowoff | 5 | 42.29 | -15.53 | 51.26 | -40.69 | 0.20 | 0 | 0 | best fit for this loop |
| P3_counterexample_guard_profile | guard_profile | if 30D MFE is fast and 180D drawdown risk is high, cap at Stage2+4B watch unless non-price evidence confirms revenue bridge | 5 | 42.29 | -15.53 | 51.26 | -40.69 | 0.00 | 2 | 2 | safe but can overblock EO/Genesem/WOT |

## 20. Score-Return Alignment Matrix
| symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 039030 | 77.00 | Stage3-Yellow | 79.00 | Stage3-Yellow + local_4B_watch | 26.60 | -20.01 | positive_with_4B_watch |
| 217190 | 76.00 | Stage3-Yellow | 77.00 | Stage3-Yellow + local_4B_watch | 37.30 | -4.60 | positive_with_4B_watch |
| 396470 | 74.00 | Stage2-Actionable borderline Stage3 | 67.00 | Stage2-Actionable + local_4B_watch | 85.31 | -9.42 | positive_with_4B_watch |
| 403870 | 78.00 | Stage3-Yellow | 65.00 | Stage2-Actionable + valuation_4B_cap | 36.39 | -23.91 | counterexample_capped |
| 122640 | 75.00 | Stage3-Yellow | 63.00 | Stage2-Actionable + contract_delay_4B_watch | 25.84 | -19.73 | counterexample_capped |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass | 3 | 2 | 5 | 0 | 5 | 0 | 5 | 5 | 5 | L2_C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_BRIDGE_AND_OPTIONALITY_4B_SPLIT | C09_ADVANCED_EQUIPMENT_REQUIRES_NAMED_ORDER_REVENUE_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP_FOURTH_PASS | static C09 10→15; session-adjusted C09 25→30 |

## 22. Residual Contribution Summary
```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: [stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage]
residual_error_types_found: [C09_optional_equipment_false_positive, signed_order_positive_but_high_MAE, local_4B_too_late_after_fast_MFE, revenue_bridge_gap_after_equipment_headline]
new_axis_proposed: C09_ADVANCED_EQUIPMENT_REQUIRES_NAMED_ORDER_REVENUE_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP_FOURTH_PASS
existing_axis_strengthened: [stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage]
existing_axis_weakened: null
existing_axis_kept: [hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: L2_C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_BRIDGE_AND_OPTIONALITY_4B_SPLIT
canonical_archetype_rule_candidate: C09_ADVANCED_EQUIPMENT_REQUIRES_NAMED_ORDER_REVENUE_MARGIN_BRIDGE_WITH_LOCAL_4B_CAP_FOURTH_PASS
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope
Validation scope: historical trigger-level OHLC path using stock-web tradable shards, clean 180D windows, C09 canonical residual rule discovery.
Non-validation scope: live screening, investment recommendation, production scoring patch, stock_agent source-code inspection, brokerage integration, or current candidate discovery.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C09_named_order_revenue_margin_bridge_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"separates signed/named order and revenue bridge from technology optionality","reduces HPSP/YEST/WOT false-positive Green risk while retaining EO/Genesem positives","TRG_C09_R2_L116_039030_20230907|TRG_C09_R2_L116_217190_20231208|TRG_C09_R2_L116_396470_20240513|TRG_C09_R2_L116_403870_20240202|TRG_C09_R2_L116_122640_20240604",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C09_local_4B_watch_after_fast_MFE_high_MAE,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"all five cases require local 4B watch after fast MFE/high post-peak drawdown","improves risk overlay without treating price-only local peaks as full 4B","TRG_C09_R2_L116_039030_20230907|TRG_C09_R2_L116_217190_20231208|TRG_C09_R2_L116_396470_20240513|TRG_C09_R2_L116_403870_20240202|TRG_C09_R2_L116_122640_20240604",5,5,2,medium,guardrail_shadow_only,"not production; overlay calibration"
```

## 25. Machine-Readable Rows
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C09_R2_L116_039030_EOTECH_LASER_ANNEALING_POSITIVE_WITH_4B","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C09_R2_L116_039030_20230907","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_with_4B_watch","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"180D MFE가 매우 크지만 peak 이후 -30% 이상 drawdown이 발생해 Green 승격 뒤 local 4B watch가 필요했다."}
{"row_type":"case","case_id":"C09_R2_L116_217190_GENESEM_HBM_WAFER_MOUNTER_POSITIVE_HIGH_MAE","symbol":"217190","company_name":"제너셈","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRG_C09_R2_L116_217190_20231208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_with_4B_watch","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"90D까지는 낮은 MAE와 양호한 MFE가 확인되나 180D에는 하락폭이 커져 수주-매출 전환 확인 뒤에도 4B overlay가 필요했다."}
{"row_type":"case","case_id":"C09_R2_L116_396470_WOT_TAYLOR_THC_DIRECT_VENDOR_PRICE_BLOWOFF","symbol":"396470","company_name":"워트","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","case_type":"price_moved_without_evidence","positive_or_counterexample":"positive","best_trigger":"TRG_C09_R2_L116_396470_20240513","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_with_4B_watch","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"주가는 빠르게 크게 움직였지만 구체 수주금액·납품일정·마진 bridge가 약해 C09 Green이 아니라 Stage2 + 4B watch가 맞았다."}
{"row_type":"case","case_id":"C09_R2_L116_403870_HPSP_HPA_MONOPOLY_VALUATION_BLOWOFF","symbol":"403870","company_name":"HPSP","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C09_R2_L116_403870_20240202","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_without_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"좋은 장비 품질과 고객 CAPA thesis에도 entry 직후 peak 이후 180D MAE가 -50%를 넘는 C09 valuation blowoff 반례다."}
{"row_type":"case","case_id":"C09_R2_L116_122640_YEST_HBM_ORDER_REVENUE_GAP_BLOWOFF","symbol":"122640","company_name":"예스티","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_C09_R2_L116_122640_20240604","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_without_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"누적 수주 headline은 Stage2-Actionable에 충분하지만 매출 인식·마진 bridge가 확인되기 전 Stage3로 올리면 180D MAE가 크게 훼손된다."}
{"row_type":"trigger","trigger_id":"TRG_C09_R2_L116_039030_20230907","case_id":"C09_R2_L116_039030_EOTECH_LASER_ANNEALING_POSITIVE_WITH_4B","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","sector":"AI/semiconductor/electronics","primary_archetype":"advanced equipment valuation blowoff","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | C09_order_revenue_bridge_boundary_validation | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-06","entry_date":"2023-09-07","entry_price":163900.0,"evidence_available_at_that_date":"삼성전자향 레이저 어닐링 공급, HBM3/HBM3e CAPA 확대 시 레이저 어닐링 수요 증가, 스텔스 다이싱/그루빙 장비 시양산 및 수주 가능성","evidence_source":"https://view.asiae.co.kr/article/2023082913041816228","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["durable_customer_confirmation","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv","profile_path":"atlas/symbol_profiles/039/039030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.59,"MFE_90D_pct":26.6,"MFE_180D_pct":71.45,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.01,"MAE_90D_pct":-20.01,"MAE_180D_pct":-20.01,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-12","peak_price":281000.0,"drawdown_after_peak_pct":-30.82,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required_after_fast_mfe_high_drawdown","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"laser_annealing_hbm_optional_growth_positive_with_late_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_039030_2023-09-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C09_R2_L116_217190_20231208","case_id":"C09_R2_L116_217190_GENESEM_HBM_WAFER_MOUNTER_POSITIVE_HIGH_MAE","symbol":"217190","company_name":"제너셈","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","sector":"AI/semiconductor/electronics","primary_archetype":"advanced equipment valuation blowoff","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | C09_order_revenue_bridge_boundary_validation | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-08","entry_date":"2023-12-08","entry_price":12600.0,"evidence_available_at_that_date":"SK하이닉스향 HBM 제조용 Wafer Mounter 장비 75.8억원 수주, 2022년 매출 대비 12.7%, 계약기간 2023-12-06~2024-04-26","evidence_source":"https://money2.daishin.com/PDF/Out/intranet_data/product/researchcenter/report/2023/12/48602_genesem_issue_comment.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["durable_customer_confirmation","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/217/217190/2023.csv","profile_path":"atlas/symbol_profiles/217/217190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.06,"MFE_90D_pct":37.3,"MFE_180D_pct":37.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.98,"MAE_90D_pct":-4.6,"MAE_180D_pct":-40.56,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":17300.0,"drawdown_after_peak_pct":-56.71,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required_after_fast_mfe_high_drawdown","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"signed_hbm_equipment_order_positive_but_180d_high_mae","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_217190_2023-12-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C09_R2_L116_396470_20240513","case_id":"C09_R2_L116_396470_WOT_TAYLOR_THC_DIRECT_VENDOR_PRICE_BLOWOFF","symbol":"396470","company_name":"워트","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","sector":"AI/semiconductor/electronics","primary_archetype":"advanced equipment valuation blowoff","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | C09_order_revenue_bridge_boundary_validation | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":9870.0,"evidence_available_at_that_date":"삼성전자 USA 오스틴/Taylor 팹 THC 직접 납품 1차 벤더 전환 예정, 삼성전자·SK하이닉스 국내외 공장 THC 납품 확대와 HBM 공정 영역 확장 기대","evidence_source":"https://v.daum.net/v/bL11mgGkMB?f=p","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/396/396470/2024.csv","profile_path":"atlas/symbol_profiles/396/396470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":67.68,"MFE_90D_pct":85.31,"MFE_180D_pct":85.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.42,"MAE_90D_pct":-9.42,"MAE_180D_pct":-34.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":18290.0,"drawdown_after_peak_pct":-64.63,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required_after_fast_mfe_high_drawdown","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"direct_vendor_grid_like_equipment_mfe_but_theme_blowoff","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_396470_2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C09_R2_L116_403870_20240202","case_id":"C09_R2_L116_403870_HPSP_HPA_MONOPOLY_VALUATION_BLOWOFF","symbol":"403870","company_name":"HPSP","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","sector":"AI/semiconductor/electronics","primary_archetype":"advanced equipment valuation blowoff","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | C09_order_revenue_bridge_boundary_validation | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":46850.0,"evidence_available_at_that_date":"세계 최초 고압 수소 어닐링 장비 양산, 고객 CAPA가 non-memory에서 memory로 확대, 신공장 완공으로 연간 생산능력 증가 기대","evidence_source":"https://www.mk.co.kr/en/economy/10934475","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv","profile_path":"atlas/symbol_profiles/403/403870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.39,"MFE_90D_pct":36.39,"MFE_180D_pct":36.39,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.51,"MAE_90D_pct":-23.91,"MAE_180D_pct":-51.65,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":63900.0,"drawdown_after_peak_pct":-64.55,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required_after_fast_mfe_high_drawdown","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"hpa_monopoly_quality_but_entry_after_theme_blowoff_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_403870_2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C09_R2_L116_122640_20240604","case_id":"C09_R2_L116_122640_YEST_HBM_ORDER_REVENUE_GAP_BLOWOFF","symbol":"122640","company_name":"예스티","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"mixed_C09_hpa_laser_environment_hbm_order_revenue_bridge_fourth_pass","sector":"AI/semiconductor/electronics","primary_archetype":"advanced equipment valuation blowoff","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | C09_order_revenue_bridge_boundary_validation | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":17840.0,"evidence_available_at_that_date":"60억원 HBM 핵심 장비 공급계약과 누적 HBM 장비 수주 380억원 돌파, 신규 상압장비 초도 물량 및 EDS 퍼니스 공급 이력, 고압어닐링 장비 수주 논의","evidence_source":"https://marketin.edaily.co.kr/News/ReadE?newsId=02794566638918112","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","contract_delay","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv","profile_path":"atlas/symbol_profiles/122/122640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.84,"MFE_90D_pct":25.84,"MFE_180D_pct":25.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.81,"MAE_90D_pct":-19.73,"MAE_180D_pct":-56.78,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":22450.0,"drawdown_after_peak_pct":-65.66,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required_after_fast_mfe_high_drawdown","four_b_evidence_type":["valuation_blowoff","contract_delay","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"hbm_equipment_cumulative_order_but_revenue_bridge_gap_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_122640_2024-06-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2_L116_039030_EOTECH_LASER_ANNEALING_POSITIVE_WITH_4B","trigger_id":"TRG_C09_R2_L116_039030_20230907","symbol":"039030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":40,"margin_bridge_score":45,"revision_score":60,"relative_strength_score":70,"customer_quality_score":75,"policy_or_regulatory_score":0,"valuation_repricing_score":80,"execution_risk_score":45,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":42,"margin_bridge_score":52,"revision_score":62,"relative_strength_score":70,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":42,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":79.0,"stage_label_after":"Stage3-Yellow + local_4B_watch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score"],"component_delta_explanation":"C09 fourth pass separates advanced equipment optionality from signed/named order, delivery timing, revenue recognition and margin bridge. High post-peak drawdown compresses valuation score and raises local 4B watch.","MFE_90D_pct":26.6,"MAE_90D_pct":-20.01,"score_return_alignment_label":"positive_with_4B_watch","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2_L116_217190_GENESEM_HBM_WAFER_MOUNTER_POSITIVE_HIGH_MAE","trigger_id":"TRG_C09_R2_L116_217190_20231208","symbol":"217190","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":76,"backlog_visibility_score":65,"margin_bridge_score":45,"revision_score":52,"relative_strength_score":62,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":68,"execution_risk_score":45,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":78,"backlog_visibility_score":68,"margin_bridge_score":50,"revision_score":54,"relative_strength_score":60,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":48,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":77.0,"stage_label_after":"Stage3-Yellow + local_4B_watch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score"],"component_delta_explanation":"C09 fourth pass separates advanced equipment optionality from signed/named order, delivery timing, revenue recognition and margin bridge. High post-peak drawdown compresses valuation score and raises local 4B watch.","MFE_90D_pct":37.3,"MAE_90D_pct":-4.6,"score_return_alignment_label":"positive_with_4B_watch","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2_L116_396470_WOT_TAYLOR_THC_DIRECT_VENDOR_PRICE_BLOWOFF","trigger_id":"TRG_C09_R2_L116_396470_20240513","symbol":"396470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":52,"backlog_visibility_score":38,"margin_bridge_score":28,"revision_score":42,"relative_strength_score":82,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":86,"execution_risk_score":62,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable borderline Stage3","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":38,"relative_strength_score":65,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":66,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":67.0,"stage_label_after":"Stage2-Actionable + local_4B_watch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score"],"component_delta_explanation":"C09 fourth pass separates advanced equipment optionality from signed/named order, delivery timing, revenue recognition and margin bridge. High post-peak drawdown compresses valuation score and raises local 4B watch.","MFE_90D_pct":85.31,"MAE_90D_pct":-9.42,"score_return_alignment_label":"positive_with_4B_watch","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2_L116_403870_HPSP_HPA_MONOPOLY_VALUATION_BLOWOFF","trigger_id":"TRG_C09_R2_L116_403870_20240202","symbol":"403870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":42,"margin_bridge_score":48,"revision_score":58,"relative_strength_score":80,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":92,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":40,"margin_bridge_score":45,"revision_score":54,"relative_strength_score":58,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":64,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":65.0,"stage_label_after":"Stage2-Actionable + valuation_4B_cap","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score"],"component_delta_explanation":"C09 fourth pass separates advanced equipment optionality from signed/named order, delivery timing, revenue recognition and margin bridge. High post-peak drawdown compresses valuation score and raises local 4B watch.","MFE_90D_pct":36.39,"MAE_90D_pct":-23.91,"score_return_alignment_label":"false_positive_blocked_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2_L116_122640_YEST_HBM_ORDER_REVENUE_GAP_BLOWOFF","trigger_id":"TRG_C09_R2_L116_122640_20240604","symbol":"122640","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":66,"backlog_visibility_score":60,"margin_bridge_score":32,"revision_score":45,"relative_strength_score":72,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":88,"execution_risk_score":60,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_before":75.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":62,"backlog_visibility_score":58,"margin_bridge_score":30,"revision_score":42,"relative_strength_score":55,"customer_quality_score":64,"policy_or_regulatory_score":0,"valuation_repricing_score":42,"execution_risk_score":66,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":5},"weighted_score_after":63.0,"stage_label_after":"Stage2-Actionable + contract_delay_4B_watch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score","contract_score"],"component_delta_explanation":"C09 fourth pass separates advanced equipment optionality from signed/named order, delivery timing, revenue recognition and margin bridge. High post-peak drawdown compresses valuation score and raises local 4B watch.","MFE_90D_pct":25.84,"MAE_90D_pct":-19.73,"score_return_alignment_label":"false_positive_blocked_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"116","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["C09_optional_equipment_false_positive","signed_order_positive_but_high_MAE","local_4B_too_late_after_fast_MFE","revenue_bridge_gap_after_equipment_headline"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State
```yaml
completed_round: R2
completed_loop: 116
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes: [C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_if_still_below_30, C14_EV_DEMAND_SLOWDOWN_4B_4C_followup_if_still_below_30, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_holdout_if_still_below_50, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_followup_if_below_50]
```

## 28. Source Notes
- Stock-Web manifest/schema are used only for historical OHLC calibration, not for current/live stock discovery.
- Evidence sources are used at or after historical publication date only. Entry dates use same-day close only when timing is clear; otherwise next tradable close is used.
- No production code patch or scoring change is included in this research MD.

## Batch Ingest Self-Audit
```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```