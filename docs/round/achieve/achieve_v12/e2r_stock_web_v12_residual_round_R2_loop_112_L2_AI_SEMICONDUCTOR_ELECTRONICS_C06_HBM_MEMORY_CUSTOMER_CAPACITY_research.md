# E2R Stock-Web V12 Residual Research — C06_HBM_MEMORY_CUSTOMER_CAPACITY loop 112
## Metadata
```yaml
completed_round: R2
completed_loop: 112
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger C06 rows=17 / need-to-30=13 / need-to-50=33; current-session C06 already above 30 but this is a new-symbol boundary quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: mixed_C06_hbm_proxy_capacity_allocation_boundary_fourth_pass_v112
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: '2026-02-20'
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
research_mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
## Selection rationale
C06 remains a static Priority 0 archetype in the No-Repeat ledger. Current-session C06 files already covered pure HBM and HBM-adjacent substrate/OSAT cases, so this pass deliberately avoids the earlier C06 symbol set and tests a narrower boundary: when an equipment, consumable, precursor, or robot supplier says Samsung/SK Hynix/HBM, does it deserve C06 customer-capacity treatment?

This file is a **cross-canonical boundary replay** from C09/C10 source rows into C06. It should not be read as fresh C09/C10 sector coverage. It tests whether C06 should require direct memory customer allocation, shipment, revenue recognition, and margin bridge before Stage3-Yellow/Green.

## Stock-Web price validation
```yaml
source_name: FinanceData/marcap
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: '2026-02-20'
required_mfe_mae_fields: [MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct]
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
```
## Representative trigger table
| symbol | name | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | stance |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 272110 | 케이엔제이 | Stage2-Actionable | 2024-03-06 | 17050 | 55.1320 | -3.4604 | 55.1320 | -3.4604 | 55.1320 | -29.9120 | positive_with_proxy_cap |
| 232680 | 라온테크 | Stage2-Actionable | 2024-12-19 | 6460 | 55.4180 | -5.2632 | 82.0433 | -5.2632 | 82.0433 | -5.2632 | positive_with_local_4B_watch |
| 086390 | 유니테스트 | Stage4B-LocalWatch | 2025-04-03 | 10480 | 13.4542 | -18.2252 | 33.7786 | -18.2252 | 112.7863 | -18.2252 | counterexample_optional_equipment_not_customer_capacity |
| 160980 | 싸이맥스 | Stage4B-LocalWatch | 2024-03-20 | 20400 | 12.0098 | -18.4804 | 16.4216 | -26.0784 | 16.4216 | -63.6765 | counterexample_hbm_tool_automation_proxy_high_MAE |
| 317330 | 덕산테코피아 | Stage4B-LocalWatch | 2024-11-15 | 29950 | 24.8748 | -11.1853 | 32.5543 | -34.5242 | 32.5543 | -50.4508 | counterexample_material_beta_contaminated |
| 187870 | 디바이스이엔지 | Stage2-Watch | 2024-02-19 | 15120 | 5.8201 | -4.1667 | 16.2037 | -4.1667 | 16.2037 | -25.5952 | counterexample_low_MFE_delayed_revenue_bridge |

## Case notes
### 272110 케이엔제이 — positive_with_proxy_cap
- Source canonical replayed into C06: `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`.
- Evidence family: SiC focus ring aftermarket route to Samsung/SK Hynix memory customers, but not direct HBM capacity allocation.
- Evidence URL: https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/05/240306_KNJ_f.pdf
- Price path: entry `2024-03-06` at `17050.0`, MFE90 `55.132`, MAE90 `-3.4604`, MFE180 `55.132`, MAE180 `-29.912`. Peak `2024-04-08` at `26450.0`, post-peak drawdown `-54.8204`.
- Interpretation: price path and customer exposure justify Stage2-Actionable or narrow positive-with-watch, but it is still not a pure C06 Green unlock unless direct HBM/customer capacity allocation and revenue/margin conversion are confirmed.

### 232680 라온테크 — positive_with_local_4B_watch
- Source canonical replayed into C06: `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`.
- Evidence family: wafer-transfer robot/module expansion; HBM/memory tool automation proxy but direct customer capacity allocation remains unconfirmed.
- Evidence URL: https://w4.kirs.or.kr/download/research/241219_%EA%B8%B0%EA%B3%84%EC%9E%A5%EB%B9%84_%EB%9D%BC%EC%98%A8%ED%85%8C%ED%81%AC%28232680%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EC%A0%9C%EC%A1%B0%EC%9A%A9%20%EC%9B%A8%EC%9D%B4%ED%8D%BC%20%EC%9D%B4%EC%86%A1%20%EB%A1%9C%EB%B4%87%20%EB%B0%8F%20%EB%AA%A8%EB%93%88%20%EC%A0%9C%EC%A1%B0%20%EC%A0%84%EB%AC%B8%20%EC%97%85%EC%B2%B4_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf
- Price path: entry `2024-12-19` at `6460.0`, MFE90 `82.0433`, MAE90 `-5.2632`, MFE180 `82.0433`, MAE180 `-5.2632`. Peak `2025-02-19` at `11760.0`, post-peak drawdown `-43.7925`.
- Interpretation: price path and customer exposure justify Stage2-Actionable or narrow positive-with-watch, but it is still not a pure C06 Green unlock unless direct HBM/customer capacity allocation and revenue/margin conversion are confirmed.

### 086390 유니테스트 — counterexample_optional_equipment_not_customer_capacity
- Source canonical replayed into C06: `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`.
- Evidence family: HBM4 burn-in tester qualification optionality, but order failure/inventory/cashflow risk remained before direct C06 allocation bridge.
- Evidence URL: https://dealsite.co.kr/articles/139224
- Price path: entry `2025-04-03` at `10480.0`, MFE90 `33.7786`, MAE90 `-18.2252`, MFE180 `112.7863`, MAE180 `-18.2252`. Peak `2025-10-01` at `22300.0`, post-peak drawdown `-40.8072`.
- Interpretation: the HBM/memory language is a proxy; without direct capacity allocation, shipment, revenue recognition, and margin bridge, C06 should cap this to Stage2-Watch or local 4B.

### 160980 싸이맥스 — counterexample_hbm_tool_automation_proxy_high_MAE
- Source canonical replayed into C06: `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`.
- Evidence family: wafer-transfer equipment supplies through major equipment makers to Samsung/SK Hynix, but no direct HBM capacity/revenue timing bridge.
- Evidence URL: https://ssl.pstatic.net/imgstock/upload/research/company/1710895255135.pdf
- Price path: entry `2024-03-20` at `20400.0`, MFE90 `16.4216`, MAE90 `-26.0784`, MFE180 `16.4216`, MAE180 `-63.6765`. Peak `2024-05-29` at `23750.0`, post-peak drawdown `-68.8`.
- Interpretation: the HBM/memory language is a proxy; without direct capacity allocation, shipment, revenue recognition, and margin bridge, C06 should cap this to Stage2-Watch or local 4B.

### 317330 덕산테코피아 — counterexample_material_beta_contaminated
- Source canonical replayed into C06: `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`.
- Evidence family: semiconductor/OLED precursor base exists, but battery-material optionality and weak earnings bridge contaminate pure HBM memory capacity interpretation.
- Evidence URL: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20241114002294&docno=&method=search&viewerhost=
- Price path: entry `2024-11-15` at `29950.0`, MFE90 `32.5543`, MAE90 `-34.5242`, MFE180 `32.5543`, MAE180 `-50.4508`. Peak `2025-02-20` at `39700.0`, post-peak drawdown `-62.6196`.
- Interpretation: the HBM/memory language is a proxy; without direct capacity allocation, shipment, revenue recognition, and margin bridge, C06 should cap this to Stage2-Watch or local 4B.

### 187870 디바이스이엔지 — counterexample_low_MFE_delayed_revenue_bridge
- Source canonical replayed into C06: `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`.
- Evidence family: FOUP cleaning / contamination-control semiconductor equipment mix shift, but no HBM customer capacity allocation or margin bridge.
- Evidence URL: https://ssl.pstatic.net/imgstock/upload/research/company/1708297940818.pdf
- Price path: entry `2024-02-19` at `15120.0`, MFE90 `16.2037`, MAE90 `-4.1667`, MFE180 `16.2037`, MAE180 `-25.5952`. Peak `2024-06-18` at `17570.0`, post-peak drawdown `-35.9704`.
- Interpretation: the HBM/memory language is a proxy; without direct capacity allocation, shipment, revenue recognition, and margin bridge, C06 should cap this to Stage2-Watch or local 4B.

## Aggregate result
```yaml
new_independent_case_count: 6
reused_case_count: 6
# reused_case_count means price/evidence source rows are boundary-replayed from C09/C10; they are not counted again as C09/C10 sector coverage.
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
calibration_usable_rows: 6
representative_rows: 6
positive_case_count: 2
counterexample_count: 4
4B_case_count: 3
4C_case_count: 0
current_profile_error_count: 5
avg_MFE_30D_pct: 27.7848
avg_MAE_30D_pct: -10.1302
avg_MFE_90D_pct: 39.3556
avg_MAE_90D_pct: -15.2863
avg_MFE_180D_pct: 52.5235
avg_MAE_180D_pct: -32.1871
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
cross_canonical_boundary_replay: true
source_row_canonical_archetypes: [C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE]
independent_evidence_weight: 0.5
do_not_count_as_new_source_sector_case: true
```
## Shadow rule candidate
```text
C06_HBM_CUSTOMER_CAPACITY_REQUIRES_DIRECT_MEMORY_CUSTOMER_ALLOCATION_SHIPMENT_REVENUE_MARGIN_BRIDGE_WITH_PROXY_4B_CAP_V112
```

Rule meaning: C06 should reward true HBM customer/capacity cases only when direct memory customer allocation, shipment visibility, revenue recognition, and margin/ASP bridge are visible. HBM-adjacent equipment, consumable, precursor, robot, and contamination-control suppliers can remain Stage2-Actionable or local 4B positives, but they should not become C06 Stage3-Yellow/Green merely because Samsung/SK Hynix/HBM appears in the narrative.

## Machine-readable trigger rows
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "mixed_C06_hbm_proxy_capacity_allocation_boundary_fourth_pass_v112", "symbol": "272110", "name": "케이엔제이", "source_row_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "cross_canonical_boundary_replay": true, "independent_evidence_weight": 0.5, "trigger_date": "2024-03-06", "entry_date": "2024-03-06", "entry_price": 17050.0, "trigger_type": "Stage2-Actionable", "evidence_family": "SiC focus ring aftermarket route to Samsung/SK Hynix memory customers, but not direct HBM capacity allocation", "evidence_url": "https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/05/240306_KNJ_f.pdf", "MFE_30D_pct": 55.132, "MAE_30D_pct": -3.4604, "MFE_90D_pct": 55.132, "MAE_90D_pct": -3.4604, "MFE_180D_pct": 55.132, "MAE_180D_pct": -29.912, "peak_date": "2024-04-08", "peak_price": 26450.0, "drawdown_after_peak_pct": -54.8204, "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": false, "profile_error_type": "boundary_positive_but_not_pure_C06", "raw_component_score_breakdown": {"eps_fcf_explosion": 64, "earnings_visibility": 58, "bottleneck_pricing": 68, "market_mispricing": 66, "valuation_rerating": 62, "capital_allocation": 42, "information_confidence": 75}, "score_total_proxy": 62.14, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "mixed_C06_hbm_proxy_capacity_allocation_boundary_fourth_pass_v112", "symbol": "232680", "name": "라온테크", "source_row_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "cross_canonical_boundary_replay": true, "independent_evidence_weight": 0.5, "trigger_date": "2024-12-19", "entry_date": "2024-12-19", "entry_price": 6460.0, "trigger_type": "Stage2-Actionable", "evidence_family": "wafer-transfer robot/module expansion; HBM/memory tool automation proxy but direct customer capacity allocation remains unconfirmed", "evidence_url": "https://w4.kirs.or.kr/download/research/241219_%EA%B8%B0%EA%B3%84%EC%9E%A5%EB%B9%84_%EB%9D%BC%EC%98%A8%ED%85%8C%ED%81%AC%28232680%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EC%A0%9C%EC%A1%B0%EC%9A%A9%20%EC%9B%A8%EC%9D%B4%ED%8D%BC%20%EC%9D%B4%EC%86%A1%20%EB%A1%9C%EB%B4%87%20%EB%B0%8F%20%EB%AA%A8%EB%93%88%20%EC%A0%9C%EC%A1%B0%20%EC%A0%84%EB%AC%B8%20%EC%97%85%EC%B2%B4_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf", "MFE_30D_pct": 55.418, "MAE_30D_pct": -5.2632, "MFE_90D_pct": 82.0433, "MAE_90D_pct": -5.2632, "MFE_180D_pct": 82.0433, "MAE_180D_pct": -5.2632, "peak_date": "2025-02-19", "peak_price": 11760.0, "drawdown_after_peak_pct": -43.7925, "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "profile_error_type": "C06_too_strict_if_proxy_becomes_order_revenue_positive", "raw_component_score_breakdown": {"eps_fcf_explosion": 62, "earnings_visibility": 56, "bottleneck_pricing": 65, "market_mispricing": 70, "valuation_rerating": 64, "capital_allocation": 38, "information_confidence": 72}, "score_total_proxy": 61.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "mixed_C06_hbm_proxy_capacity_allocation_boundary_fourth_pass_v112", "symbol": "086390", "name": "유니테스트", "source_row_canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "cross_canonical_boundary_replay": true, "independent_evidence_weight": 0.5, "trigger_date": "2025-04-03", "entry_date": "2025-04-03", "entry_price": 10480.0, "trigger_type": "Stage4B-LocalWatch", "evidence_family": "HBM4 burn-in tester qualification optionality, but order failure/inventory/cashflow risk remained before direct C06 allocation bridge", "evidence_url": "https://dealsite.co.kr/articles/139224", "MFE_30D_pct": 13.4542, "MAE_30D_pct": -18.2252, "MFE_90D_pct": 33.7786, "MAE_90D_pct": -18.2252, "MFE_180D_pct": 112.7863, "MAE_180D_pct": -18.2252, "peak_date": "2025-10-01", "peak_price": 22300.0, "drawdown_after_peak_pct": -40.8072, "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "profile_error_type": "HBM_optional_equipment_should_not_unlock_C06", "raw_component_score_breakdown": {"eps_fcf_explosion": 50, "earnings_visibility": 42, "bottleneck_pricing": 58, "market_mispricing": 70, "valuation_rerating": 62, "capital_allocation": 28, "information_confidence": 62}, "score_total_proxy": 53.14, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "mixed_C06_hbm_proxy_capacity_allocation_boundary_fourth_pass_v112", "symbol": "160980", "name": "싸이맥스", "source_row_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "cross_canonical_boundary_replay": true, "independent_evidence_weight": 0.5, "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 20400.0, "trigger_type": "Stage4B-LocalWatch", "evidence_family": "wafer-transfer equipment supplies through major equipment makers to Samsung/SK Hynix, but no direct HBM capacity/revenue timing bridge", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1710895255135.pdf", "MFE_30D_pct": 12.0098, "MAE_30D_pct": -18.4804, "MFE_90D_pct": 16.4216, "MAE_90D_pct": -26.0784, "MFE_180D_pct": 16.4216, "MAE_180D_pct": -63.6765, "peak_date": "2024-05-29", "peak_price": 23750.0, "drawdown_after_peak_pct": -68.8, "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "profile_error_type": "proxy_equipment_high_MAE_requires_4B_cap", "raw_component_score_breakdown": {"eps_fcf_explosion": 48, "earnings_visibility": 38, "bottleneck_pricing": 56, "market_mispricing": 63, "valuation_rerating": 50, "capital_allocation": 30, "information_confidence": 60}, "score_total_proxy": 49.29, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "mixed_C06_hbm_proxy_capacity_allocation_boundary_fourth_pass_v112", "symbol": "317330", "name": "덕산테코피아", "source_row_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "cross_canonical_boundary_replay": true, "independent_evidence_weight": 0.5, "trigger_date": "2024-11-14", "entry_date": "2024-11-15", "entry_price": 29950.0, "trigger_type": "Stage4B-LocalWatch", "evidence_family": "semiconductor/OLED precursor base exists, but battery-material optionality and weak earnings bridge contaminate pure HBM memory capacity interpretation", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20241114002294&docno=&method=search&viewerhost=", "MFE_30D_pct": 24.8748, "MAE_30D_pct": -11.1853, "MFE_90D_pct": 32.5543, "MAE_90D_pct": -34.5242, "MFE_180D_pct": 32.5543, "MAE_180D_pct": -50.4508, "peak_date": "2025-02-20", "peak_price": 39700.0, "drawdown_after_peak_pct": -62.6196, "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "profile_error_type": "mixed_material_beta_should_not_count_as_C06_capacity", "raw_component_score_breakdown": {"eps_fcf_explosion": 45, "earnings_visibility": 35, "bottleneck_pricing": 52, "market_mispricing": 65, "valuation_rerating": 55, "capital_allocation": 30, "information_confidence": 58}, "score_total_proxy": 48.57, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "mixed_C06_hbm_proxy_capacity_allocation_boundary_fourth_pass_v112", "symbol": "187870", "name": "디바이스이엔지", "source_row_canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "cross_canonical_boundary_replay": true, "independent_evidence_weight": 0.5, "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 15120.0, "trigger_type": "Stage2-Watch", "evidence_family": "FOUP cleaning / contamination-control semiconductor equipment mix shift, but no HBM customer capacity allocation or margin bridge", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1708297940818.pdf", "MFE_30D_pct": 5.8201, "MAE_30D_pct": -4.1667, "MFE_90D_pct": 16.2037, "MAE_90D_pct": -4.1667, "MFE_180D_pct": 16.2037, "MAE_180D_pct": -25.5952, "peak_date": "2024-06-18", "peak_price": 17570.0, "drawdown_after_peak_pct": -35.9704, "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "profile_error_type": "Stage2_proxy_cap_until_revenue_margin_bridge", "raw_component_score_breakdown": {"eps_fcf_explosion": 44, "earnings_visibility": 40, "bottleneck_pricing": 50, "market_mispricing": 55, "valuation_rerating": 48, "capital_allocation": 35, "information_confidence": 63}, "score_total_proxy": 47.86, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
## Machine-readable score simulation rows
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "symbol": "272110", "name": "케이엔제이", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "baseline_current_proxy_stage": "Stage2-Actionable", "score_total_proxy_before": 62.14, "recommended_stage_after_shadow_rule": "Stage2-Actionable", "price_path_alignment": "positive_with_guardrail", "component_scores": {"eps_fcf_explosion": 64, "earnings_visibility": 58, "bottleneck_pricing": 68, "market_mispricing": 66, "valuation_rerating": 62, "capital_allocation": 42, "information_confidence": 75}, "changed_components": ["customer_capacity_allocation_gate", "shipment_revenue_margin_bridge", "proxy_4B_cap"], "MFE_90D_pct": 55.132, "MAE_90D_pct": -3.4604, "MFE_180D_pct": 55.132, "MAE_180D_pct": -29.912}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "symbol": "232680", "name": "라온테크", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "baseline_current_proxy_stage": "Stage2-Actionable", "score_total_proxy_before": 61.0, "recommended_stage_after_shadow_rule": "Stage2-Actionable", "price_path_alignment": "positive_with_guardrail", "component_scores": {"eps_fcf_explosion": 62, "earnings_visibility": 56, "bottleneck_pricing": 65, "market_mispricing": 70, "valuation_rerating": 64, "capital_allocation": 38, "information_confidence": 72}, "changed_components": ["customer_capacity_allocation_gate", "shipment_revenue_margin_bridge", "proxy_4B_cap"], "MFE_90D_pct": 82.0433, "MAE_90D_pct": -5.2632, "MFE_180D_pct": 82.0433, "MAE_180D_pct": -5.2632}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "symbol": "086390", "name": "유니테스트", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "baseline_current_proxy_stage": "Stage4B-LocalWatch", "score_total_proxy_before": 53.14, "recommended_stage_after_shadow_rule": "Stage2-Watch/Stage4B overlay", "price_path_alignment": "bad_or_requires_guardrail", "component_scores": {"eps_fcf_explosion": 50, "earnings_visibility": 42, "bottleneck_pricing": 58, "market_mispricing": 70, "valuation_rerating": 62, "capital_allocation": 28, "information_confidence": 62}, "changed_components": ["customer_capacity_allocation_gate", "shipment_revenue_margin_bridge", "proxy_4B_cap"], "MFE_90D_pct": 33.7786, "MAE_90D_pct": -18.2252, "MFE_180D_pct": 112.7863, "MAE_180D_pct": -18.2252}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "symbol": "160980", "name": "싸이맥스", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "baseline_current_proxy_stage": "Stage4B-LocalWatch", "score_total_proxy_before": 49.29, "recommended_stage_after_shadow_rule": "Stage2-Watch/Stage4B overlay", "price_path_alignment": "bad_or_requires_guardrail", "component_scores": {"eps_fcf_explosion": 48, "earnings_visibility": 38, "bottleneck_pricing": 56, "market_mispricing": 63, "valuation_rerating": 50, "capital_allocation": 30, "information_confidence": 60}, "changed_components": ["customer_capacity_allocation_gate", "shipment_revenue_margin_bridge", "proxy_4B_cap"], "MFE_90D_pct": 16.4216, "MAE_90D_pct": -26.0784, "MFE_180D_pct": 16.4216, "MAE_180D_pct": -63.6765}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "symbol": "317330", "name": "덕산테코피아", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "baseline_current_proxy_stage": "Stage4B-LocalWatch", "score_total_proxy_before": 48.57, "recommended_stage_after_shadow_rule": "Stage2-Watch/Stage4B overlay", "price_path_alignment": "bad_or_requires_guardrail", "component_scores": {"eps_fcf_explosion": 45, "earnings_visibility": 35, "bottleneck_pricing": 52, "market_mispricing": 65, "valuation_rerating": 55, "capital_allocation": 30, "information_confidence": 58}, "changed_components": ["customer_capacity_allocation_gate", "shipment_revenue_margin_bridge", "proxy_4B_cap"], "MFE_90D_pct": 32.5543, "MAE_90D_pct": -34.5242, "MFE_180D_pct": 32.5543, "MAE_180D_pct": -50.4508}
{"row_type": "score_simulation", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "symbol": "187870", "name": "디바이스이엔지", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "baseline_current_proxy_stage": "Stage2-Watch", "score_total_proxy_before": 47.86, "recommended_stage_after_shadow_rule": "Stage2-Watch/Stage4B overlay", "price_path_alignment": "bad_or_requires_guardrail", "component_scores": {"eps_fcf_explosion": 44, "earnings_visibility": 40, "bottleneck_pricing": 50, "market_mispricing": 55, "valuation_rerating": 48, "capital_allocation": 35, "information_confidence": 63}, "changed_components": ["customer_capacity_allocation_gate", "shipment_revenue_margin_bridge", "proxy_4B_cap"], "MFE_90D_pct": 16.2037, "MAE_90D_pct": -4.1667, "MFE_180D_pct": 16.2037, "MAE_180D_pct": -25.5952}
## Aggregate JSON
{"row_type": "aggregate", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "calibration_usable_rows": 6, "representative_rows": 6, "positive_case_count": 2, "counterexample_count": 4, "current_profile_error_count": 5, "avg_MFE_180D_pct": 52.5235, "avg_MAE_180D_pct": -32.1871, "shadow_rule_candidate": "C06_HBM_CUSTOMER_CAPACITY_REQUIRES_DIRECT_MEMORY_CUSTOMER_ALLOCATION_SHIPMENT_REVENUE_MARGIN_BRIDGE_WITH_PROXY_4B_CAP_V112", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": ["C06_proxy_decontamination_gate"], "ready_for_batch_ingest": true}
## Batch Ingest Self-Audit
```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
cross_canonical_boundary_replay: true
do_not_count_as_new_source_sector_case: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 6
representative_rows: 6
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
## Residual contribution summary
This loop does not argue that every HBM-adjacent tool or material supplier belongs in C06. It does the opposite: it separates pure HBM customer-capacity rerating from proxy narratives. The residual error is a cross-canonical boundary error: when C09/C10 equipment or consumable rows are mistakenly interpreted as C06, Stage3 can open too early unless direct allocation, shipment, revenue, and margin bridge are visible.

## Deferred Coding Agent Handoff Prompt
```text
Do not execute during research. In the later coding-agent batch implementation session, ingest this MD with the rest of docs/round V12 outputs. Treat trigger rows as cross-canonical boundary replay from C09/C10 into C06 with independent_evidence_weight=0.5. Do not double-count these rows as new C09/C10 source-sector coverage. Evaluate whether C06 runtime profile needs a proxy-decontamination gate: HBM-adjacent equipment/material/robot/contamination-control narratives should require direct memory customer allocation, shipment, revenue recognition, and margin bridge before Stage3-Yellow/Green.
```

## Next research state
```yaml
completed_round: R2
completed_loop: 112
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger C06 rows=17 / need-to-30=13 / need-to-50=33
next_recommended_archetypes:
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
  - C11_BATTERY_ORDERBOOK_RERATING
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
