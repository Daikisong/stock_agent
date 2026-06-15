---
research_file: e2r_stock_web_v12_residual_round_R2_loop_107_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
selected_round: R2
selected_loop: 107
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: mixed_C07_hbm_equipment_order_relative_strength_set
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: '2026-02-20'
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
coverage_selection_mode: coverage_index_selected
production_code_patch_included: false
production_scoring_patch_applied: false
---

# E2R stock-web V12 residual research — R2 loop 107 / C07 HBM equipment order relative strength

## 0. Execution contract
This standalone Markdown follows the V12 research contract. The No-Repeat Index is used only as a duplicate-avoidance ledger; `stock_agent` production code is not modified; every representative trigger row uses actual `Songdaiki/stock-web` tradable OHLCV rows and includes entry_date, entry_price, and 30D/90D/180D MFE·MAE fields.

## 1. Scheduler and No-Repeat interpretation
Selected canonical: `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`. It belongs to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`. The coverage-first scheduler selected C07 because it remained below the 30-row target, while this session had already produced C06, C09 and C10. Existing standard C07 file was observed up to `R2_loop_106`; this file uses `R2_loop_107`.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 2. Selected archetype definition
C07 captures HBM-specific equipment rerating paths where public evidence suggests that a supplier moved from general semiconductor beta into customer-qualified, order-backed, revenue-converting HBM equipment demand.

## 3. Fine/deep sub-archetype map
1. `HBM_CUBE_PROBER_UNIT_FORECAST_AND_CUSTOMER_EXPANSION`
2. `SK_HYNIX_LASER_ANNEAL_REPEAT_ORDER`
3. `SAMSUNG_HBM_WAFER_TESTER_CONTRACT_POST_HYPE_ENTRY`
4. `HBM_CLEANING_REVENUE_RECOGNITION_WITH_WEAK_PRICE_PATH`
5. `HBM_REFLOW_ORDER_REVENUE_RECOGNITION_BUT_SCALE_GAP`

## 4. Case universe
| symbol | name | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 089030 | 테크윙 | Stage3-Yellow | 2024-12-13 | 34350 | 52.84 | -6.84 | 52.84 | -23.14 | 52.84 | -24.16 | positive |
| 110990 | 디아이티 | Stage3-Yellow | 2025-01-14 | 14500 | 34.28 | -2.9 | 34.28 | -20.34 | 34.28 | -23.66 | positive |
| 232140 | 와이씨 | Stage4B | 2024-07-30 | 16500 | 16.24 | -34.36 | 16.24 | -49.88 | 16.24 | -49.88 | counterexample |
| 079370 | 제우스 | Stage2-Actionable | 2025-03-20 | 15460 | 2.52 | -24.97 | 2.52 | -24.97 | 11.0 | -25.55 | counterexample |
| 039440 | 에스티아이 | Stage2-Actionable | 2024-05-21 | 34800 | 20.98 | -10.92 | 20.98 | -46.55 | 20.98 | -60.86 | counterexample |

## 5. Evidence note — 089030 테크윙
Trigger: 2024-12-13 Cube Prober/HBM test handler forecast revision. The price path validates positive C07 evidence, but the post-peak drawdown argues for Stage3-Yellow rather than immediate Green.

Evidence URL: https://www.yna.co.kr/view/AKR20241213023200008

## 6. Evidence note — 110990 디아이티
Trigger: 2025-01-14 SK Hynix laser annealing repeat order. This is named customer/order evidence, not just theme beta. The path validates a positive C07 route while requiring a fast-MFE 4B watch.

Evidence URL: https://www.thelec.kr/news/articleView.html?idxno=32286

## 7. Evidence note — 232140 와이씨
Trigger: 2024-07-30 Samsung HBM wafer tester contract. This is the core counterexample: the order was real, but public contract entry after hype expansion produced much larger MAE than MFE.

Evidence URL: https://www.smedaily.co.kr/news/articleView.html?idxno=299017

## 8. Evidence note — 079370 제우스
Trigger: 2025-03-20 HBM cleaning equipment order-to-revenue recognition. The HBM equipment story was real, but the forward path was weak, supporting Stage2/watch unless customer scale and margin delivery improve.

Evidence URL: https://www.newspim.com/news/view/20250318000815

## 9. Evidence note — 039440 에스티아이
Trigger: 2024-05-21 HBM reflow equipment revenue recognition. The story had concrete order/revenue expectations, but the contribution scale and subsequent high-MAE path do not justify automatic Stage3 promotion.

Evidence URL: https://www.dailyinvest.kr/news/articleView.html?idxno=58804

## 10. Price-path methodology
- Entry rule: trigger date if tradable; otherwise next tradable day.
- Entry price: stock-web tradable close on entry_date.
- MFE: `(max high from entry_date through N tradable rows / entry_price - 1) * 100`.
- MAE: `(min low from entry_date through N tradable rows / entry_price - 1) * 100`.
- Usability: entry row exists, 180 forward tradable rows exist, and 180D corporate-action contamination is absent.

## 11. Positive/counterexample balance
```yaml
positive_case_count: 2
counterexample_count: 3
stage4b_case_count: 1
stage4c_case_count: 0
current_profile_error_count: 3
calibration_usable_rows: 5
representative_rows: 5
```

## 12. Residual error interpretation
C07 residual error is not that HBM equipment evidence is weak. The error is that HBM equipment evidence is heterogeneous. A repeat named customer order for a bottleneck tool behaves differently from a post-hype contract headline or a small optional equipment contribution.

## 13. Proposed canonical rule candidate
```text
C07_CONFIRMED_ORDER_REVENUE_CONVERSION_GATE_WITH_HYPE_MAE_CAP
```
Promotion toward Stage3-Yellow should require at least two of: named customer qualification/repeat order, material order amount, explicit revenue-recognition period, margin/bottleneck-pricing bridge, and multi-source confirmation. Route to Stage4B/watch or cap at Stage2 when post-hype MAE risk dominates or revenue/margin conversion is not visible.

## 14. Sector-specific rule candidate
```text
L2_C07_HBM_EQUIPMENT_ORDER_TO_REVENUE_CONVERSION_AND_4B_OVERHEAT_SPLIT
```
Tester/prober/laser anneal bottleneck tools with customer qualification should be separated from optional/reflow/cleaning equipment where HBM contribution is real but smaller or later.

## 15. Stage transition interpretation
- `Stage2-Actionable`: HBM equipment order/revenue evidence exists, but scale/margin/customer bridge is incomplete.
- `Stage3-Yellow`: named customer/order evidence and revenue visibility are credible, but delivery/margin risk remains.
- `Stage3-Green`: not assigned in this loop.
- `Stage4B`: signed-order or HBM hype is real, but entry follows sharp rerating and high-MAE risk dominates.
- `Stage4C`: not assigned; no order cancellation, qualification failure, accounting break or hard demand collapse appeared in this sample.

## 16. 4B/4C audit
Only 와이씨 is labeled `Stage4B`. It had real order evidence but entered after prior HBM tester hype and produced severe MAE. This strengthens `full_4b_requires_non_price_evidence`: price alone is not enough, but price plus post-hype contract timing plus absent margin conversion is enough.

## 17. Corporate-action audit
```yaml
entry_row_exists: true
forward_180_tradable_days_available: true
corporate_action_window_status: clean_180D_window
corporate_action_contaminated_rows: 0
```
The 2024 Zeus event family had nearby corporate-action risk, so this run uses the 2025-03-20 trigger instead.

## 18. Source quality audit
```yaml
evidence_url_pending_rows: 0
source_proxy_only_rows: 0
narrative_only_rows: 0
stock_web_price_rows_used: 5
```

## 19. Profile comparison
| profile | rule setting | eligible/promoted rows | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 current | current e2r_2_2 C07 treatment | 5 | 25.37 | -32.98 | 27.07 | -36.82 | 60% | signed-order/theme can over-promote YC/Zeus/STI |
| P0b current+local4B | current plus existing price/local 4B guard | 4 | 27.31 | -28.75 | 29.77 | -33.56 | 50% | YC blocked, Zeus/STI still slip through |
| P1 sector shadow | L2 order/revenue conversion check | 3 | 34.45 | -31.12 | 34.45 | -32.57 | 33% | accepts Techwing/DIT, routes YC to 4B |
| P2 canonical shadow | C07 confirmed order + revenue/margin bridge gate | 2 | 43.56 | -21.74 | 43.56 | -23.91 | 0% | keeps only two structural positives |
| P3 guardrail shadow | P2 plus high-MAE cap for HBM equipment theme | 2 | 43.56 | -21.74 | 43.56 | -23.91 | 0% | best precision; needs more C07 samples |

## 20. Shadow weight CSV
```csv
profile_id,scope,weight_delta_candidate,condition,expected_effect,apply_now
C07_shadow_P2,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,+earnings_visibility,+confirmed_order_revenue_conversion_or_customer_capacity_allocation,raise precision for real HBM equipment winners,false
C07_shadow_P2,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,+information_confidence,+named_customer_contract_or_repeated_order,block theme-only supplier beta,false
C07_shadow_P2,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,-valuation_rerating,+MFE_fast_and_MAE90_worse_than_20pct_without_margin_bridge,route to 4B/watch,false
C07_shadow_P2,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,+bottleneck_pricing,+bottleneck_equipment_with_revenue_conversion,distinguish tester/prober/laser anneal from generic equipment,false
```

## 21. Batch-ingest machine-readable JSONL
```jsonl
{"row_type": "case_header", "case_id": "C07_R2L107_089030_20241213", "symbol": "089030", "symbol_name": "테크윙", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_CUBE_PROBER_HBM_TEST_HANDLER_CUSTOMER_EXPANSION", "deep_sub_archetype_id": "HBM_CUBE_PROBER_UNIT_FORECAST_AND_CUSTOMER_EXPANSION", "case_role": "positive", "case_type": "positive_structural_hbm_test_equipment_order_to_forecast_revision", "trigger_family": "HBM_CUBE_PROBER_UNIT_FORECAST_AND_CUSTOMER_EXPANSION", "evidence_url": "https://www.yna.co.kr/view/AKR20241213023200008", "evidence_note": "Cube Prober 판매대수/2025 실적 전망 상향 및 HBM 수요 지속 코멘트.", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|Stage3-Yellow|2024-12-13", "no_repeat_status": "new_symbol_and_new_trigger_family_within_current_session", "calibration_usable": true}
{"row_type": "case_header", "case_id": "C07_R2L107_110990_20250114", "symbol": "110990", "symbol_name": "디아이티", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_LASER_ANNEAL_HBM_CUSTOMER_ORDER_CONVERSION", "deep_sub_archetype_id": "SK_HYNIX_LASER_ANNEAL_REPEAT_ORDER", "case_role": "positive", "case_type": "positive_actual_hbm_laser_anneal_order_with_fast_peak_watch", "trigger_family": "SK_HYNIX_LASER_ANNEAL_REPEAT_ORDER", "evidence_url": "https://www.thelec.kr/news/articleView.html?idxno=32286", "evidence_note": "SK하이닉스향 레이저 어닐링 장비 추가 수주, 계약금액 205.2억원 및 매출액 대비 19.17%.", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|110990|Stage3-Yellow|2025-01-14", "no_repeat_status": "new_symbol_and_new_trigger_family_within_current_session", "calibration_usable": true}
{"row_type": "case_header", "case_id": "C07_R2L107_232140_20240730", "symbol": "232140", "symbol_name": "와이씨", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_HBM_WAFER_TESTER_CONTRACT_OVERHEAT", "deep_sub_archetype_id": "SAMSUNG_HBM_WAFER_TESTER_CONTRACT_POST_HYPE_ENTRY", "case_role": "counterexample", "case_type": "counterexample_actual_hbm_wafer_tester_contract_high_mae", "trigger_family": "SAMSUNG_HBM_WAFER_TESTER_CONTRACT_POST_HYPE_ENTRY", "evidence_url": "https://www.smedaily.co.kr/news/articleView.html?idxno=299017", "evidence_note": "삼성전자 HBM 웨이퍼 테스터 공급업체 선정 및 2025년 3월까지 계약 보도.", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|232140|Stage4B|2024-07-30", "no_repeat_status": "new_symbol_and_new_trigger_family_within_current_session", "calibration_usable": true}
{"row_type": "case_header", "case_id": "C07_R2L107_079370_20250320", "symbol": "079370", "symbol_name": "제우스", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_HBM_TSV_CLEANING_ORDER_TO_REVENUE_DELAY", "deep_sub_archetype_id": "HBM_CLEANING_REVENUE_RECOGNITION_WITH_WEAK_PRICE_PATH", "case_role": "counterexample", "case_type": "counterexample_hbm_cleaning_order_revenue_recognition_underperforms", "trigger_family": "HBM_CLEANING_REVENUE_RECOGNITION_WITH_WEAK_PRICE_PATH", "evidence_url": "https://www.newspim.com/news/view/20250318000815", "evidence_note": "HBM 세정장비 수주분이 2025년부터 매출 인식되고 ASP가 높다는 회사 관계자 코멘트.", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|079370|Stage2-Actionable|2025-03-20", "no_repeat_status": "new_symbol_and_new_trigger_family_within_current_session", "calibration_usable": true}
{"row_type": "case_header", "case_id": "C07_R2L107_039440_20240521", "symbol": "039440", "symbol_name": "에스티아이", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "C07_HBM_REFLOW_EQUIPMENT_REVENUE_SCALE_GAP", "deep_sub_archetype_id": "HBM_REFLOW_ORDER_REVENUE_RECOGNITION_BUT_SCALE_GAP", "case_role": "counterexample", "case_type": "counterexample_hbm_reflow_order_revenue_high_mae", "trigger_family": "HBM_REFLOW_ORDER_REVENUE_RECOGNITION_BUT_SCALE_GAP", "evidence_url": "https://www.dailyinvest.kr/news/articleView.html?idxno=58804", "evidence_note": "HBM 리플로우 장비 수주분의 2024년 4분기/2025년 1분기 매출 인식 전망.", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039440|Stage2-Actionable|2024-05-21", "no_repeat_status": "new_symbol_and_new_trigger_family_within_current_session", "calibration_usable": true}
{"row_type": "trigger_row", "trigger_id": "C07_R2L107_089030_20241213_Stage3_Yellow", "case_id": "C07_R2L107_089030_20241213", "symbol": "089030", "symbol_name": "테크윙", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-12-13", "entry_date": "2024-12-13", "entry_price": 34350.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv|atlas/ohlcv_tradable_by_symbol_year/089/089030/2025.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "MFE_30D_pct": 52.84, "MAE_30D_pct": -6.84, "MFE_90D_pct": 52.84, "MAE_90D_pct": -23.14, "MFE_180D_pct": 52.84, "MAE_180D_pct": -24.16, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date_180D": "2025-01-20", "peak_price_180D": 52500.0, "drawdown_after_peak_180D_pct": -50.38, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "positive_or_counterexample": "positive", "current_profile_verdict": "current_profile_correct_but_green_should_wait_for_delivery_margin_confirmation", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger"}
{"row_type": "trigger_row", "trigger_id": "C07_R2L107_110990_20250114_Stage3_Yellow", "case_id": "C07_R2L107_110990_20250114", "symbol": "110990", "symbol_name": "디아이티", "trigger_type": "Stage3-Yellow", "trigger_date": "2025-01-14", "entry_date": "2025-01-14", "entry_price": 14500.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/110/110990/2025.csv", "profile_path": "atlas/symbol_profiles/110/110990.json", "MFE_30D_pct": 34.28, "MAE_30D_pct": -2.9, "MFE_90D_pct": 34.28, "MAE_90D_pct": -20.34, "MFE_180D_pct": 34.28, "MAE_180D_pct": -23.66, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date_180D": "2025-01-22", "peak_price_180D": 19470.0, "drawdown_after_peak_180D_pct": -43.14, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "positive_or_counterexample": "positive", "current_profile_verdict": "current_profile_mostly_correct_with_fast_mfe_4b_watch", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger"}
{"row_type": "trigger_row", "trigger_id": "C07_R2L107_232140_20240730_Stage4B", "case_id": "C07_R2L107_232140_20240730", "symbol": "232140", "symbol_name": "와이씨", "trigger_type": "Stage4B", "trigger_date": "2024-07-30", "entry_date": "2024-07-30", "entry_price": 16500.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv|atlas/ohlcv_tradable_by_symbol_year/232/232140/2025.csv", "profile_path": "atlas/symbol_profiles/232/232140.json", "MFE_30D_pct": 16.24, "MAE_30D_pct": -34.36, "MFE_90D_pct": 16.24, "MAE_90D_pct": -49.88, "MFE_180D_pct": 16.24, "MAE_180D_pct": -49.88, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date_180D": "2024-07-31", "peak_price_180D": 19180.0, "drawdown_after_peak_180D_pct": -56.88, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "positive_or_counterexample": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_signed_order_alone_promotes_stage3", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.59, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger"}
{"row_type": "trigger_row", "trigger_id": "C07_R2L107_079370_20250320_Stage2_Actionable", "case_id": "C07_R2L107_079370_20250320", "symbol": "079370", "symbol_name": "제우스", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-03-20", "entry_date": "2025-03-20", "entry_price": 15460.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/079/079370/2025.csv", "profile_path": "atlas/symbol_profiles/079/079370.json", "MFE_30D_pct": 2.52, "MAE_30D_pct": -24.97, "MFE_90D_pct": 2.52, "MAE_90D_pct": -24.97, "MFE_180D_pct": 11.0, "MAE_180D_pct": -25.55, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date_180D": "2025-10-14", "peak_price_180D": 17160.0, "drawdown_after_peak_180D_pct": -26.57, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "positive_or_counterexample": "counterexample", "current_profile_verdict": "current_profile_too_early_without_customer_scale_and_margin_delivery", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger"}
{"row_type": "trigger_row", "trigger_id": "C07_R2L107_039440_20240521_Stage2_Actionable", "case_id": "C07_R2L107_039440_20240521", "symbol": "039440", "symbol_name": "에스티아이", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-21", "entry_date": "2024-05-21", "entry_price": 34800.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw_unadjusted_marcap", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv|atlas/ohlcv_tradable_by_symbol_year/039/039440/2025.csv", "profile_path": "atlas/symbol_profiles/039/039440.json", "MFE_30D_pct": 20.98, "MAE_30D_pct": -10.92, "MFE_90D_pct": 20.98, "MAE_90D_pct": -46.55, "MFE_180D_pct": 20.98, "MAE_180D_pct": -60.86, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date_180D": "2024-06-26", "peak_price_180D": 42100.0, "drawdown_after_peak_180D_pct": -67.65, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "positive_or_counterexample": "counterexample", "current_profile_verdict": "current_profile_false_positive_without_revenue_scale_and_sustained_margin_bridge", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "green_lateness_ratio": "not_applicable_no_stage3_green_trigger"}
{"row_type": "score_simulation", "trigger_id": "C07_R2L107_089030_20241213_Stage3_Yellow", "case_id": "C07_R2L107_089030_20241213", "symbol": "089030", "profile_before": "e2r_2_2_rolling_calibrated_current_C07", "profile_after": "C07_CONFIRMED_ORDER_REVENUE_CONVERSION_GATE_WITH_HYPE_MAE_CAP_shadow", "raw_component_scores": {"eps_fcf_explosion": 74, "earnings_visibility": 76, "bottleneck_pricing": 82, "market_mispricing": 70, "valuation_rerating": 66, "capital_allocation": 45, "information_confidence": 78}, "weighted_total_before": 82, "weighted_total_after_shadow": 83, "stage_before_shadow": "Stage3-Yellow", "stage_after_shadow": "Stage3-Yellow", "stage_delta_reason": "current_profile_correct_but_green_should_wait_for_delivery_margin_confirmation"}
{"row_type": "score_simulation", "trigger_id": "C07_R2L107_110990_20250114_Stage3_Yellow", "case_id": "C07_R2L107_110990_20250114", "symbol": "110990", "profile_before": "e2r_2_2_rolling_calibrated_current_C07", "profile_after": "C07_CONFIRMED_ORDER_REVENUE_CONVERSION_GATE_WITH_HYPE_MAE_CAP_shadow", "raw_component_scores": {"eps_fcf_explosion": 70, "earnings_visibility": 72, "bottleneck_pricing": 78, "market_mispricing": 68, "valuation_rerating": 64, "capital_allocation": 42, "information_confidence": 80}, "weighted_total_before": 79, "weighted_total_after_shadow": 82, "stage_before_shadow": "Stage3-Yellow", "stage_after_shadow": "Stage3-Yellow", "stage_delta_reason": "current_profile_mostly_correct_with_fast_mfe_4b_watch"}
{"row_type": "score_simulation", "trigger_id": "C07_R2L107_232140_20240730_Stage4B", "case_id": "C07_R2L107_232140_20240730", "symbol": "232140", "profile_before": "e2r_2_2_rolling_calibrated_current_C07", "profile_after": "C07_CONFIRMED_ORDER_REVENUE_CONVERSION_GATE_WITH_HYPE_MAE_CAP_shadow", "raw_component_scores": {"eps_fcf_explosion": 61, "earnings_visibility": 58, "bottleneck_pricing": 76, "market_mispricing": 52, "valuation_rerating": 38, "capital_allocation": 40, "information_confidence": 72}, "weighted_total_before": 84, "weighted_total_after_shadow": 64, "stage_before_shadow": "Stage3-Yellow", "stage_after_shadow": "Stage4B", "stage_delta_reason": "current_profile_false_positive_if_signed_order_alone_promotes_stage3"}
{"row_type": "score_simulation", "trigger_id": "C07_R2L107_079370_20250320_Stage2_Actionable", "case_id": "C07_R2L107_079370_20250320", "symbol": "079370", "profile_before": "e2r_2_2_rolling_calibrated_current_C07", "profile_after": "C07_CONFIRMED_ORDER_REVENUE_CONVERSION_GATE_WITH_HYPE_MAE_CAP_shadow", "raw_component_scores": {"eps_fcf_explosion": 55, "earnings_visibility": 52, "bottleneck_pricing": 68, "market_mispricing": 49, "valuation_rerating": 45, "capital_allocation": 38, "information_confidence": 62}, "weighted_total_before": 73, "weighted_total_after_shadow": 61, "stage_before_shadow": "Stage2-Actionable", "stage_after_shadow": "Stage2", "stage_delta_reason": "current_profile_too_early_without_customer_scale_and_margin_delivery"}
{"row_type": "score_simulation", "trigger_id": "C07_R2L107_039440_20240521_Stage2_Actionable", "case_id": "C07_R2L107_039440_20240521", "symbol": "039440", "profile_before": "e2r_2_2_rolling_calibrated_current_C07", "profile_after": "C07_CONFIRMED_ORDER_REVENUE_CONVERSION_GATE_WITH_HYPE_MAE_CAP_shadow", "raw_component_scores": {"eps_fcf_explosion": 54, "earnings_visibility": 51, "bottleneck_pricing": 70, "market_mispricing": 46, "valuation_rerating": 34, "capital_allocation": 36, "information_confidence": 65}, "weighted_total_before": 76, "weighted_total_after_shadow": 60, "stage_before_shadow": "Stage3-Yellow", "stage_after_shadow": "Stage2", "stage_delta_reason": "current_profile_false_positive_without_revenue_scale_and_sustained_margin_bridge"}
{"row_type": "price_source_validation", "case_id": "C07_R2L107_089030_20241213", "symbol": "089030", "entry_date": "2024-12-13", "entry_price": 34350.0, "forward_window_tradable_days": 180, "schema_rule": "MFE_N=(max high entry-through-N-tradable-rows/entry_price-1)*100; MAE_N=(min low/entry_price-1)*100", "corporate_action_candidates_180D": [], "validation_status": "pass"}
{"row_type": "price_source_validation", "case_id": "C07_R2L107_110990_20250114", "symbol": "110990", "entry_date": "2025-01-14", "entry_price": 14500.0, "forward_window_tradable_days": 180, "schema_rule": "MFE_N=(max high entry-through-N-tradable-rows/entry_price-1)*100; MAE_N=(min low/entry_price-1)*100", "corporate_action_candidates_180D": [], "validation_status": "pass"}
{"row_type": "price_source_validation", "case_id": "C07_R2L107_232140_20240730", "symbol": "232140", "entry_date": "2024-07-30", "entry_price": 16500.0, "forward_window_tradable_days": 180, "schema_rule": "MFE_N=(max high entry-through-N-tradable-rows/entry_price-1)*100; MAE_N=(min low/entry_price-1)*100", "corporate_action_candidates_180D": [], "validation_status": "pass"}
{"row_type": "price_source_validation", "case_id": "C07_R2L107_079370_20250320", "symbol": "079370", "entry_date": "2025-03-20", "entry_price": 15460.0, "forward_window_tradable_days": 180, "schema_rule": "MFE_N=(max high entry-through-N-tradable-rows/entry_price-1)*100; MAE_N=(min low/entry_price-1)*100", "corporate_action_candidates_180D": [], "validation_status": "pass"}
{"row_type": "price_source_validation", "case_id": "C07_R2L107_039440_20240521", "symbol": "039440", "entry_date": "2024-05-21", "entry_price": 34800.0, "forward_window_tradable_days": 180, "schema_rule": "MFE_N=(max high entry-through-N-tradable-rows/entry_price-1)*100; MAE_N=(min low/entry_price-1)*100", "corporate_action_candidates_180D": [], "validation_status": "pass"}
{"row_type": "residual_contribution", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "loop": "107", "new_rows": 5, "expected_canonical_rows_after_acceptance": 23, "rule_candidate": "C07_CONFIRMED_ORDER_REVENUE_CONVERSION_GATE_WITH_HYPE_MAE_CAP", "positive_case_count": 2, "counterexample_count": 3, "stage4b_case_count": 1, "stage4c_case_count": 0, "current_profile_error_count": 3, "residual_error_pattern": "signed_order_or_hbm_equipment_theme_can_overpromote_when_revenue_conversion_margin_bridge_and_high_mae_guard_are_missing"}
```

## 22. Duplicate ledger rows
```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|Stage3-Yellow|2024-12-13
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|110990|Stage3-Yellow|2025-01-14
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|232140|Stage4B|2024-07-30
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|079370|Stage2-Actionable|2025-03-20
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039440|Stage2-Actionable|2024-05-21
```

## 23. Residual contribution summary
```yaml
auto_selected_coverage_gap: C07 rows 18 -> expected 23 after acceptance
new_independent_case_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
current_profile_error_count: 3
new_axis_proposed:
  - C07_ORDER_TO_REVENUE_CONVERSION_GATE
  - C07_HBM_TEST_EQUIPMENT_HIGH_MAE_4B_CAP
  - C07_CUSTOMER_QUALIFICATION_WITH_TIMING_BUFFER
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
  - stage2_required_bridge
existing_axis_weakened: null
```

## 24. Why no production patch is applied now
This file is research evidence only. It proposes a shadow rule candidate but does not change production scoring, staging, configs, or registry files.

## 25. Rejected/narrative-only candidates
`092870 엑시콘` was considered for C07 HBM tester evidence but rejected for representative-row use because the stronger 2024 trigger window had nearby corporate-action contamination and later clean triggers lacked enough forward window under stock-web `max_date=2026-02-20`.

## 26. Recommended follow-up archetypes
```yaml
next_recommended_archetype: C11_BATTERY_ORDERBOOK_RERATING
supplementary_next:
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_followup_if_still_below_30
```

## 27. Deferred Coding Agent Handoff Prompt
```text
You are the coding agent for Songdaiki/stock_agent. Do not use this handoff until multiple V12 research MDs are ready for batch ingestion.

Goal:
Ingest the new standalone MD:
e2r_stock_web_v12_residual_round_R2_loop_107_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md

Tasks:
1. Parse JSONL rows under Batch-ingest machine-readable JSONL.
2. Validate filename/metadata consistency.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Verify entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
5. Confirm calibration_usable and clean 180D corporate-action windows.
6. Evaluate the shadow rule C07_CONFIRMED_ORDER_REVENUE_CONVERSION_GATE_WITH_HYPE_MAE_CAP.
7. Do not directly change production scoring unless aggregate batch evidence supports safe patch promotion.
```

## 28. Final self-audit
```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
