# E2R Stock-Web v12 Residual Research — R3 / C11 Battery Orderbook Rerating / Loop 109

## Research Metadata
```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R3_loop_109_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round: R3
selected_loop: 109
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: mixed_C11_precursor_electrolyte_emf_orderbook_bridge_holdout_v109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows; C11 static ledger rows=18, need_to_30=12, need_to_50=32
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check
C11_BATTERY_ORDERBOOK_RERATING remains a Priority 0 under-30 canonical in the static No-Repeat ledger. This pass avoids the recent C11 cell/cathode/copper-foil/can/component symbols and extends C11 into precursor, electrolyte, separator-material and EMF orderbook boundary cases.

Hard duplicate check uses `canonical_archetype_id + symbol + trigger_type + entry_date`. The selected rows are new for C11 in this session and are not counted as R13 replay rows. 101360 has a corporate-action candidate on 2024-08-01 in the local Stock-Web copy, so the usable trigger is intentionally placed on 2025-03-17 after that date; no selected row has 180D corporate-action contamination.

## 2. Stock-Web price validation
All usable trigger rows use Stock-Web tradable shards, raw/unadjusted marcap OHLC, entry-date close as entry price, and 30/90/180 trading-day high-low windows for MFE/MAE. No row in this file is marked corporate-action contaminated or insufficient-forward-window.

## 3. Core finding
C11에서 대형계약, 고객사 PO, 증설, 소재/장비 적용처 확대 headline 자체와 Stage3 orderbook rerating을 분리해야 한다. Stage3-Yellow 이상은 **shipment → revenue recognition → ASP/margin → FCF bridge**가 확인될 때만 열고, 초도물량·capacity·수요회복 expectation·가격 안정화 expectation만 있으면 Stage2-Watch 또는 local 4B로 눌러야 한다. 생산중단과 고객 재고조정이 함께 확인되는 경우에는 hard 4C route가 더 적합하다.

## 4. Trigger row summary
| symbol | company | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | assessment |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 101360 | 에코앤드림 | Stage2-Actionable | 2025-03-17 | 27700 | 6.3177 | -31.0469 | 6.3177 | -36.9675 | Stage2-Actionable-counterexample-with-local-4B-watch |
| 089980 | 상아프론테크 | Stage4B | 2024-07-08 | 25950 | 3.6609 | -34.4123 | 3.6609 | -47.3218 | Stage4B-local-watch-counterexample |
| 278280 | 천보 | Stage4B | 2023-11-21 | 103400 | 33.3656 | -21.6634 | 33.3656 | -52.6112 | Stage2-Actionable-positive-with-4B-watch |
| 093370 | 후성 | Stage4C | 2023-04-17 | 14890 | 4.0967 | -26.1249 | 4.0967 | -35.8630 | Stage4C-hard-thesis-break |
| 290670 | 대보마그네틱 | Stage4B | 2024-07-08 | 24950 | 13.0261 | -52.3046 | 13.0261 | -61.0822 | Stage4B-local-watch-counterexample |

## 5. Case notes

### 101360 에코앤드림 — precursor_long_term_contract_capacity_but_shipping_margin_gap
2024년 1월 고객사와 5년 장기공급계약을 체결하고 하이니켈 NCM 전구체 양산·공급을 진행한다는 사업보고서 근거. 그러나 entry 이후 가격경로는 MFE가 거의 열리지 않고 MAE가 커서, 장기계약 headline만으로 C11 Stage3를 열면 false positive가 된다.
- Evidence URL: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250317000833&docno=&method=search&viewerhost=
- Price path: entry `2025-03-17` close `27700`, MFE180 `6.3177%`, MAE180 `-36.9675%`, peak `2025-03-20` `29450`, drawdown_after_peak `-40.7131%`.
- Rule note: 전구체 장기계약은 shipment, ASP, margin, cash conversion이 확인되기 전까지 Stage2-Watch로 제한한다.

### 089980 상아프론테크 — separator_membrane_growth_theme_without_orderbook_conversion
2024년 들어 수소와 2차전지 부품 성장성이 다시 주목받는다는 리포트 근거. 하지만 실제 가격경로는 30D부터 MAE가 깊고 180D MFE가 거의 없어, C11 orderbook rerating이 아니라 theme-only 4B cap이 필요했다.
- Evidence URL: https://w4.kirs.or.kr/download/research/240708_%EC%83%81%EC%95%84%ED%94%84%EB%A1%A0%ED%85%8C%ED%81%AC.pdf
- Price path: entry `2024-07-08` close `25950`, MFE180 `3.6609%`, MAE180 `-47.3218%`, peak `2024-07-11` `26900`, drawdown_after_peak `-49.1822%`.
- Rule note: 분리막/소재 성장성 narrative는 named battery customer PO와 매출·마진 bridge 없이는 C11 positive로 압축하지 않는다.

### 278280 천보 — electrolyte_demand_recovery_but_price_margin_lag
배터리 소재 수요 회복과 판매가격 안정화를 통한 실적 개선 기대가 제시됐지만, 이전 실적 부진 원인이 판매가격 하락이라는 점도 함께 확인된다. 30D MFE는 컸으나 180D MAE가 깊어 C11 positive는 유지하되 local 4B가 필수다.
- Evidence URL: https://www.businesspost.co.kr/BP?command=article_view&num=333707
- Price path: entry `2023-11-21` close `103400`, MFE180 `33.3656%`, MAE180 `-52.6112%`, peak `2023-12-08` `137900`, drawdown_after_peak `-64.4670%`.
- Rule note: 전해질 소재 회복은 selling price stabilization과 가동률·OPM 회복이 확인되어야 Stage3-Yellow로 승격한다.

### 093370 후성 — lipf6_production_stop_customer_inventory_adjustment
고객사 재고조정과 소재 가격 하락으로 울산 LiPF6 생산 중단을 결정한 hard thesis-break 근거. MFE가 거의 열리지 않고 MAE가 지속되어 C11 orderbook persistence를 차단하는 4C route가 맞았다.
- Evidence URL: https://dealsite.co.kr/articles/102284/025116
- Price path: entry `2023-04-17` close `14890`, MFE180 `4.0967%`, MAE180 `-35.8630%`, peak `2023-04-18` `15500`, drawdown_after_peak `-38.3871%`.
- Rule note: 생산중단·고객 재고조정·가격 붕괴가 동시에 확인되면 C11 Stage2/3를 유지하지 않고 4C로 라우팅한다.

### 290670 대보마그네틱 — emf_initial_order_without_full_contract_revenue_bridge
중국 글로벌 2차전지 소재기업향 탈철기 초도물량 수주 및 향후 대규모 본계약 기대가 확인됐다. 그러나 entry 당일 peak 이후 MFE가 제한적이고 MAE가 깊어, 초도물량 수주와 본계약 기대만으로 C11 Stage3를 열면 안 된다.
- Evidence URL: https://m.newsprime.co.kr/section_view.html?menu=1&no=645643
- Price path: entry `2024-07-08` close `24950`, MFE180 `13.0261%`, MAE180 `-61.0822%`, peak `2024-07-08` `28200`, drawdown_after_peak `-65.5674%`.
- Rule note: 초도물량/샘플성 수주는 본계약, 반복 PO, revenue recognition, margin bridge가 확인되기 전까지 4B cap을 둔다.

## 6. Aggregate stress result
```yaml
selected_round: R3
selected_loop: 109
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
calibration_usable_rows: 5
representative_rows: 5
positive_case_count: 1
counterexample_count: 4
4B_case_count: 4
4C_case_count: 1
current_profile_error_count: 5
avg_MFE_30D_pct: 12.0934
avg_MAE_30D_pct: -20.5183
avg_MFE_90D_pct: 12.0934
avg_MAE_90D_pct: -33.1104
avg_MFE_180D_pct: 12.0934
avg_MAE_180D_pct: -46.7691
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
```

## 7. Score / return alignment
The current calibrated profile directionally blocks price-only blowoff and requires bridge evidence, but C11 still needs a sharper orderbook conversion gate. The return path shows average 180D MFE of only `12.0934%` against average 180D MAE of `-46.7691%`; the signal is asymmetric in the wrong direction when contract/capacity headlines are accepted without shipment and margin confirmation.

## 8. Machine-readable trigger rows JSONL
```jsonl
{"MAE_180D_pct": -36.9675, "MAE_30D_pct": -14.6209, "MAE_90D_pct": -31.0469, "MFE_180D_pct": 6.3177, "MFE_30D_pct": 6.3177, "MFE_90D_pct": 6.3177, "baseline_stage": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_role": "counterexample", "case_type": "precursor_long_term_contract_capacity_but_shipping_margin_gap", "company": "에코앤드림", "corporate_action_contaminated": false, "current_profile_error": "false_positive_if_contract_capacity_is_treated_as_shipments_and_margin_bridge", "drawdown_after_peak_pct": -40.7131, "entry_date": "2025-03-17", "entry_price": 27700.0, "evidence_family": "precursor_long_term_contract_capacity_expansion", "evidence_summary": "2024년 1월 고객사와 5년 장기공급계약을 체결하고 하이니켈 NCM 전구체 양산·공급을 진행한다는 사업보고서 근거. 그러나 entry 이후 가격경로는 MFE가 거의 열리지 않고 MAE가 커서, 장기계약 headline만으로 C11 Stage3를 열면 false positive가 된다.", "evidence_url_pending": false, "fine_archetype_id": "mixed_C11_precursor_electrolyte_emf_orderbook_bridge_holdout_v109", "future_data_leakage_detected": false, "insufficient_forward_window": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "peak_date": "2025-03-20", "peak_price": 29450.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 64, "capital_allocation": 48, "earnings_visibility": 60, "eps_fcf_explosion": 54, "information_confidence": 80, "market_mispricing": 52, "valuation_rerating": 45}, "representative": true, "revised_stage": "Stage2-Watch+4B-LocalWatch", "rule_note": "전구체 장기계약은 shipment, ASP, margin, cash conversion이 확인되기 전까지 Stage2-Watch로 제한한다.", "source_proxy_only": false, "source_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250317000833&docno=&method=search&viewerhost=", "stage_assessment": "Stage2-Actionable-counterexample-with-local-4B-watch", "stock_web_manifest_max_date": "2026-02-20", "symbol": "101360", "trigger_date": "2025-03-17", "trigger_row_type": "trigger", "trigger_type": "Stage2-Actionable", "window_180D_corporate_action_contaminated": false, "window_180D_end_date": "2025-12-09", "window_30D_end_date": "2025-04-28", "window_90D_end_date": "2025-07-28"}
{"MAE_180D_pct": -47.3218, "MAE_30D_pct": -30.6358, "MAE_90D_pct": -34.4123, "MFE_180D_pct": 3.6609, "MFE_30D_pct": 3.6609, "MFE_90D_pct": 3.6609, "baseline_stage": "Stage2-Actionable-false-positive", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_role": "counterexample", "case_type": "separator_membrane_growth_theme_without_orderbook_conversion", "company": "상아프론테크", "corporate_action_contaminated": false, "current_profile_error": "stage2_false_positive_if_theme_growth_is_not_decontaminated", "drawdown_after_peak_pct": -49.1822, "entry_date": "2024-07-08", "entry_price": 25950.0, "evidence_family": "separator_membrane_growth_theme", "evidence_summary": "2024년 들어 수소와 2차전지 부품 성장성이 다시 주목받는다는 리포트 근거. 하지만 실제 가격경로는 30D부터 MAE가 깊고 180D MFE가 거의 없어, C11 orderbook rerating이 아니라 theme-only 4B cap이 필요했다.", "evidence_url_pending": false, "fine_archetype_id": "mixed_C11_precursor_electrolyte_emf_orderbook_bridge_holdout_v109", "future_data_leakage_detected": false, "insufficient_forward_window": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "peak_date": "2024-07-11", "peak_price": 26900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 50, "capital_allocation": 45, "earnings_visibility": 42, "eps_fcf_explosion": 35, "information_confidence": 72, "market_mispricing": 44, "valuation_rerating": 35}, "representative": true, "revised_stage": "Stage4B-LocalWatch", "rule_note": "분리막/소재 성장성 narrative는 named battery customer PO와 매출·마진 bridge 없이는 C11 positive로 압축하지 않는다.", "source_proxy_only": false, "source_url": "https://w4.kirs.or.kr/download/research/240708_%EC%83%81%EC%95%84%ED%94%84%EB%A1%A0%ED%85%8C%ED%81%AC.pdf", "stage_assessment": "Stage4B-local-watch-counterexample", "stock_web_manifest_max_date": "2026-02-20", "symbol": "089980", "trigger_date": "2024-07-08", "trigger_row_type": "trigger", "trigger_type": "Stage4B", "window_180D_corporate_action_contaminated": false, "window_180D_end_date": "2025-04-07", "window_30D_end_date": "2024-08-20", "window_90D_end_date": "2024-11-20"}
{"MAE_180D_pct": -52.6112, "MAE_30D_pct": -2.5145, "MAE_90D_pct": -21.6634, "MFE_180D_pct": 33.3656, "MFE_30D_pct": 33.3656, "MFE_90D_pct": 33.3656, "baseline_stage": "Stage3-Yellow-too-early", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_role": "positive_with_guardrail", "case_type": "electrolyte_demand_recovery_but_price_margin_lag", "company": "천보", "corporate_action_contaminated": false, "current_profile_error": "overgreen_if_short_term_demand_recovery_ignores_price_margin_lag", "drawdown_after_peak_pct": -64.467, "entry_date": "2023-11-21", "entry_price": 103400.0, "evidence_family": "electrolyte_demand_recovery_and_selling_price_stabilization", "evidence_summary": "배터리 소재 수요 회복과 판매가격 안정화를 통한 실적 개선 기대가 제시됐지만, 이전 실적 부진 원인이 판매가격 하락이라는 점도 함께 확인된다. 30D MFE는 컸으나 180D MAE가 깊어 C11 positive는 유지하되 local 4B가 필수다.", "evidence_url_pending": false, "fine_archetype_id": "mixed_C11_precursor_electrolyte_emf_orderbook_bridge_holdout_v109", "future_data_leakage_detected": false, "insufficient_forward_window": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "peak_date": "2023-12-08", "peak_price": 137900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 58, "capital_allocation": 50, "earnings_visibility": 56, "eps_fcf_explosion": 62, "information_confidence": 78, "market_mispricing": 68, "valuation_rerating": 55}, "representative": true, "revised_stage": "Stage2-Actionable+4B-LocalWatch", "rule_note": "전해질 소재 회복은 selling price stabilization과 가동률·OPM 회복이 확인되어야 Stage3-Yellow로 승격한다.", "source_proxy_only": false, "source_url": "https://www.businesspost.co.kr/BP?command=article_view&num=333707", "stage_assessment": "Stage2-Actionable-positive-with-4B-watch", "stock_web_manifest_max_date": "2026-02-20", "symbol": "278280", "trigger_date": "2023-11-21", "trigger_row_type": "trigger", "trigger_type": "Stage4B", "window_180D_corporate_action_contaminated": false, "window_180D_end_date": "2024-08-14", "window_30D_end_date": "2024-01-05", "window_90D_end_date": "2024-04-03"}
{"MAE_180D_pct": -35.863, "MAE_30D_pct": -15.7824, "MAE_90D_pct": -26.1249, "MFE_180D_pct": 4.0967, "MFE_30D_pct": 4.0967, "MFE_90D_pct": 4.0967, "baseline_stage": "Stage2-Actionable-false-positive-if_price_only_rebound", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_role": "counterexample", "case_type": "lipf6_production_stop_customer_inventory_adjustment", "company": "후성", "corporate_action_contaminated": false, "current_profile_error": "late_4c_if_orderbook_legacy_not_cut_by_customer_inventory_and_production_stop", "drawdown_after_peak_pct": -38.3871, "entry_date": "2023-04-17", "entry_price": 14890.0, "evidence_family": "electrolyte_production_stop_due_to_customer_inventory_and_price_pressure", "evidence_summary": "고객사 재고조정과 소재 가격 하락으로 울산 LiPF6 생산 중단을 결정한 hard thesis-break 근거. MFE가 거의 열리지 않고 MAE가 지속되어 C11 orderbook persistence를 차단하는 4C route가 맞았다.", "evidence_url_pending": false, "fine_archetype_id": "mixed_C11_precursor_electrolyte_emf_orderbook_bridge_holdout_v109", "future_data_leakage_detected": false, "insufficient_forward_window": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "peak_date": "2023-04-18", "peak_price": 15500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 20, "capital_allocation": 45, "earnings_visibility": 15, "eps_fcf_explosion": 18, "information_confidence": 84, "market_mispricing": 40, "valuation_rerating": 22}, "representative": true, "revised_stage": "Stage4C", "rule_note": "생산중단·고객 재고조정·가격 붕괴가 동시에 확인되면 C11 Stage2/3를 유지하지 않고 4C로 라우팅한다.", "source_proxy_only": false, "source_url": "https://dealsite.co.kr/articles/102284/025116", "stage_assessment": "Stage4C-hard-thesis-break", "stock_web_manifest_max_date": "2026-02-20", "symbol": "093370", "trigger_date": "2023-04-17", "trigger_row_type": "trigger", "trigger_type": "Stage4C", "window_180D_corporate_action_contaminated": false, "window_180D_end_date": "2024-01-11", "window_30D_end_date": "2023-06-01", "window_90D_end_date": "2023-08-28"}
{"MAE_180D_pct": -61.0822, "MAE_30D_pct": -39.0381, "MAE_90D_pct": -52.3046, "MFE_180D_pct": 13.0261, "MFE_30D_pct": 13.0261, "MFE_90D_pct": 13.0261, "baseline_stage": "Stage2-Actionable-false-positive", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_role": "counterexample", "case_type": "emf_initial_order_without_full_contract_revenue_bridge", "company": "대보마그네틱", "corporate_action_contaminated": false, "current_profile_error": "stage2_false_positive_if_initial_order_is_treated_as_full_orderbook_conversion", "drawdown_after_peak_pct": -65.5674, "entry_date": "2024-07-08", "entry_price": 24950.0, "evidence_family": "electromagnetic_filter_initial_order_and_future_contract_optional", "evidence_summary": "중국 글로벌 2차전지 소재기업향 탈철기 초도물량 수주 및 향후 대규모 본계약 기대가 확인됐다. 그러나 entry 당일 peak 이후 MFE가 제한적이고 MAE가 깊어, 초도물량 수주와 본계약 기대만으로 C11 Stage3를 열면 안 된다.", "evidence_url_pending": false, "fine_archetype_id": "mixed_C11_precursor_electrolyte_emf_orderbook_bridge_holdout_v109", "future_data_leakage_detected": false, "insufficient_forward_window": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "peak_date": "2024-07-08", "peak_price": 28200.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_score_breakdown": {"bottleneck_pricing": 58, "capital_allocation": 45, "earnings_visibility": 42, "eps_fcf_explosion": 30, "information_confidence": 78, "market_mispricing": 44, "valuation_rerating": 32}, "representative": true, "revised_stage": "Stage4B-LocalWatch", "rule_note": "초도물량/샘플성 수주는 본계약, 반복 PO, revenue recognition, margin bridge가 확인되기 전까지 4B cap을 둔다.", "source_proxy_only": false, "source_url": "https://m.newsprime.co.kr/section_view.html?menu=1&no=645643", "stage_assessment": "Stage4B-local-watch-counterexample", "stock_web_manifest_max_date": "2026-02-20", "symbol": "290670", "trigger_date": "2024-07-08", "trigger_row_type": "trigger", "trigger_type": "Stage4B", "window_180D_corporate_action_contaminated": false, "window_180D_end_date": "2025-04-07", "window_30D_end_date": "2024-08-20", "window_90D_end_date": "2024-11-20"}
```

## 9. Machine-readable score simulation rows JSONL
```jsonl
{"alignment_note": "C11 score must be interpreted with shipment/revenue/margin/FCF bridge and call-off or price-lag guardrails.", "baseline_stage": "Stage2-Actionable", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "company": "에코앤드림", "entry_date": "2025-03-17", "profile_error": "false_positive_if_contract_capacity_is_treated_as_shipments_and_margin_bridge", "raw_component_scores": {"bottleneck_pricing": 64, "capital_allocation": 48, "earnings_visibility": 60, "eps_fcf_explosion": 54, "information_confidence": 80, "market_mispricing": 52, "valuation_rerating": 45}, "revised_stage": "Stage2-Watch+4B-LocalWatch", "row_type": "score_simulation", "symbol": "101360", "synthetic_total_score": 57.57, "trigger_type": "Stage2-Actionable"}
{"alignment_note": "C11 score must be interpreted with shipment/revenue/margin/FCF bridge and call-off or price-lag guardrails.", "baseline_stage": "Stage2-Actionable-false-positive", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "company": "상아프론테크", "entry_date": "2024-07-08", "profile_error": "stage2_false_positive_if_theme_growth_is_not_decontaminated", "raw_component_scores": {"bottleneck_pricing": 50, "capital_allocation": 45, "earnings_visibility": 42, "eps_fcf_explosion": 35, "information_confidence": 72, "market_mispricing": 44, "valuation_rerating": 35}, "revised_stage": "Stage4B-LocalWatch", "row_type": "score_simulation", "symbol": "089980", "synthetic_total_score": 46.14, "trigger_type": "Stage4B"}
{"alignment_note": "C11 score must be interpreted with shipment/revenue/margin/FCF bridge and call-off or price-lag guardrails.", "baseline_stage": "Stage3-Yellow-too-early", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "company": "천보", "entry_date": "2023-11-21", "profile_error": "overgreen_if_short_term_demand_recovery_ignores_price_margin_lag", "raw_component_scores": {"bottleneck_pricing": 58, "capital_allocation": 50, "earnings_visibility": 56, "eps_fcf_explosion": 62, "information_confidence": 78, "market_mispricing": 68, "valuation_rerating": 55}, "revised_stage": "Stage2-Actionable+4B-LocalWatch", "row_type": "score_simulation", "symbol": "278280", "synthetic_total_score": 61.0, "trigger_type": "Stage4B"}
{"alignment_note": "C11 score must be interpreted with shipment/revenue/margin/FCF bridge and call-off or price-lag guardrails.", "baseline_stage": "Stage2-Actionable-false-positive-if_price_only_rebound", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "company": "후성", "entry_date": "2023-04-17", "profile_error": "late_4c_if_orderbook_legacy_not_cut_by_customer_inventory_and_production_stop", "raw_component_scores": {"bottleneck_pricing": 20, "capital_allocation": 45, "earnings_visibility": 15, "eps_fcf_explosion": 18, "information_confidence": 84, "market_mispricing": 40, "valuation_rerating": 22}, "revised_stage": "Stage4C", "row_type": "score_simulation", "symbol": "093370", "synthetic_total_score": 34.86, "trigger_type": "Stage4C"}
{"alignment_note": "C11 score must be interpreted with shipment/revenue/margin/FCF bridge and call-off or price-lag guardrails.", "baseline_stage": "Stage2-Actionable-false-positive", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "company": "대보마그네틱", "entry_date": "2024-07-08", "profile_error": "stage2_false_positive_if_initial_order_is_treated_as_full_orderbook_conversion", "raw_component_scores": {"bottleneck_pricing": 58, "capital_allocation": 45, "earnings_visibility": 42, "eps_fcf_explosion": 30, "information_confidence": 78, "market_mispricing": 44, "valuation_rerating": 32}, "revised_stage": "Stage4B-LocalWatch", "row_type": "score_simulation", "symbol": "290670", "synthetic_total_score": 47.0, "trigger_type": "Stage4B"}
{"4B_case_count": 4, "4C_case_count": 1, "MAE_180D_pct": -46.7691, "MAE_30D_pct": -20.5183, "MAE_90D_pct": -33.1104, "MFE_180D_pct": 12.0934, "MFE_30D_pct": 12.0934, "MFE_90D_pct": 12.0934, "calibration_usable_rows": 5, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "counterexample_count": 4, "evidence_url_pending_rows": 0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "positive_case_count": 1, "production_scoring_patch_applied": false, "representative_rows": 5, "row_type": "aggregate", "selected_loop": 109, "selected_round": "R3", "source_proxy_only_rows": 0}
{"candidate_rule_id": "C11_ORDERBOOK_REQUIRES_SHIPMENT_REVENUE_MARGIN_FCF_AND_CALLOFF_PRICE_CLEARANCE_GATE_V109", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "production_scoring_changed": false, "row_type": "shadow_weight_candidate", "rule_summary": "Require shipment, revenue recognition, ASP/margin and FCF conversion before Stage3-Yellow/Green; route production stop/customer inventory/price collapse to hard 4C; cap initial order or capacity headlines with local 4B overlay.", "shadow_weight_only": true}
{"canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "new_axis_proposed": "C11_orderbook_conversion_gate_with_calloff_price_clearance", "residual_error_found": true, "residual_summary": "Contract/capacity/customer-order headlines without shipment/margin bridge produce high-MAE false positives. One hard 4C path is confirmed by LiPF6 production stop plus customer inventory adjustment.", "row_type": "residual_contribution"}
```

## 10. Proposed shadow rule
```text
C11_ORDERBOOK_REQUIRES_SHIPMENT_REVENUE_MARGIN_FCF_AND_CALLOFF_PRICE_CLEARANCE_GATE_V109
```

Rule candidate:
- Stage3-Yellow requires at least two of shipment visibility, revenue-recognition timing, ASP/margin bridge, FCF/cash conversion, or repeat PO.
- Stage3-Green requires those bridge signals plus low red-team risk and no MAE guardrail breach.
- Initial PO, sample quantity, capacity expansion, or future 본계약 expectation remains Stage2-Watch until bridge confirmation.
- Customer inventory adjustment plus production stop plus price collapse routes to hard 4C, not merely local 4B.

## 11. Deferred Coding Agent Handoff Prompt
```text
Do not execute during this research session. Later coding-agent task: ingest this V12 standalone MD with other docs/round V12 files; validate trigger_rows_jsonl; dedupe by canonical_archetype_id + symbol + trigger_type + entry_date; if accepted, test a C11 shadow rule named C11_ORDERBOOK_REQUIRES_SHIPMENT_REVENUE_MARGIN_FCF_AND_CALLOFF_PRICE_CLEARANCE_GATE_V109. Do not change production scoring unless the batch calibration promotion step accepts the rule candidate.
```

## 12. Final research state
```yaml
completed_round: R3
completed_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows; C11_BATTERY_ORDERBOOK_RERATING static ledger rows=18, need_to_30=12
next_recommended_archetypes:
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
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
ready_for_batch_ingest: true
```
