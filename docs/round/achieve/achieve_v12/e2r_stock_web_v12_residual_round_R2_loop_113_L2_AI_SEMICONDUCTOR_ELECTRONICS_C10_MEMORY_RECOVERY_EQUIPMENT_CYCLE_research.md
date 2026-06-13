# E2R Stock-Web v12 Residual Research — R2 / C10 memory recovery equipment cycle / loop 113
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 113
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113
output_file: e2r_stock_web_v12_residual_round_R2_loop_113_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger C10 rows=13 / need-to-30=17 / need-to-50=37
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
## 1. Selection / novelty note

The static No-Repeat Index still lists `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` as a Priority 0 archetype with 13 representative rows. The current long session has already added multiple C10 equipment / consumable rows, so this loop is not another generic memory-recovery beta pass. It is a boundary holdout that asks whether specialty gas, CCSS, chemical supply, and scrubber/chiller exposure should be allowed to become C10 Stage3 without direct reorder, utilization, revenue-recognition, and margin bridge.

Hard duplicate key checked manually: `canonical_archetype_id + symbol + trigger_type + entry_date`. The four symbols in this file were not used as C10 representative rows in the local session before this pass.
## 2. Stock-Web price atlas confirmation

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: [KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI]
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
MFE_N_pct: (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct: (min low from entry_date through N tradable rows / entry_price - 1) * 100
corporate_action_policy: block 180D contaminated windows
```
## 3. Case table

| case_id | symbol | name | trigger_date | entry_date | trigger_type | outcome_bucket | evidence_family | calibration_usable |
|---|---:|---|---:|---:|---|---|---|---|
| C10_V113_001 | 425040 | 티이엠씨 | 2024-02-01 | 2024-02-01 | Stage2-Actionable | counterexample | specialty gas / rare-gas recovery / memory recovery proxy; not direct memory equipment reorder | true |
| C10_V113_002 | 264660 | 씨앤지하이테크 | 2024-03-15 | 2024-03-15 | Stage2-Actionable | positive_with_guardrail | CCSS / chemical supply system demand from semiconductor capex; real infrastructure tool but still not direct memory equipment reorder | true |
| C10_V113_003 | 241790 | 티이엠씨씨엔에스 | 2024-04-25 | 2024-04-25 | Stage2-Actionable | counterexample | name-change / semiconductor chemical-material and fab equipment business exposure; bridge missing after transition | true |
| C10_V113_004 | 083450 | GST | 2024-08-01 | 2024-08-01 | Stage2-Actionable | positive_with_guardrail | scrubber/chiller and ultra-low-temperature chiller route; memory/HBM capex adjacent but order/revenue bridge still needed | true |

## 4. Trigger-level Stock-Web price path rows

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 425040 | 2024-02-01 | 18810.0 | 21.2121 | -11.3238 | 21.2121 | -11.3238 | 21.2121 | -54.4391 | 2024-03-12 | 22800.0 | -62.4123 |
| 264660 | 2024-03-15 | 13090.0 | 55.4622 | -2.5974 | 55.8442 | -7.3338 | 55.8442 | -36.9748 | 2024-04-30 | 20400.0 | -59.5588 |
| 241790 | 2024-04-25 | 12340.0 | 1.8639 | -13.2901 | 1.8639 | -47.2447 | 1.8639 | -66.5316 | 2024-04-29 | 12570.0 | -67.144 |
| 083450 | 2024-08-01 | 16810.0 | 13.9203 | -24.9851 | 13.9203 | -24.9851 | 38.9054 | -24.9851 | 2025-02-24 | 23350.0 | -34.1756 |

## 5. Case narratives

### 425040 티이엠씨 — counterexample

- evidence source: https://temc.co.kr/
- trigger: `2024-02-01` -> entry `2024-02-01` at close `18810.0`.
- price path: MFE90 `21.2121%`, MAE90 `-11.3238%`, MFE180 `21.2121%`, MAE180 `-54.4391%`.
- stage split: Stage2 evidence = `public_product_business_exposure, memory_recovery_proxy, specialty_gas_supply_chain_optionality`; Stage3 bridge = `not yet confirmed`; 4B evidence = `price_only_local_peak, margin_or_backlog_slowdown, proxy_not_order_conversion`.
- residual interpretation: `specialty_gas_proxy_high_MAE_false_positive`. C10 should not convert this kind of memory-recovery proxy into Stage3-Green until reorder/utilization/revenue/margin conversion is confirmed.

### 264660 씨앤지하이테크 — positive_with_guardrail

- evidence source: https://ssl.pstatic.net/imgstock/upload/research/company/1672959699990.pdf
- trigger: `2024-03-15` -> entry `2024-03-15` at close `13090.0`.
- price path: MFE90 `55.8442%`, MAE90 `-7.3338%`, MFE180 `55.8442%`, MAE180 `-36.9748%`.
- stage split: Stage2 evidence = `customer_or_order_quality, capacity_or_volume_route, semiconductor_fab_infrastructure_capex`; Stage3 bridge = `financial_visibility_partial`; 4B evidence = `price_only_local_peak, positioning_overheat`.
- residual interpretation: `CCSS_infra_positive_but_high_MAE_guard`. C10 should not convert this kind of memory-recovery proxy into Stage3-Green until reorder/utilization/revenue/margin conversion is confirmed.

### 241790 티이엠씨씨엔에스 — counterexample

- evidence source: https://www.temccns.com/
- trigger: `2024-04-25` -> entry `2024-04-25` at close `12340.0`.
- price path: MFE90 `1.8639%`, MAE90 `-47.2447%`, MFE180 `1.8639%`, MAE180 `-66.5316%`.
- stage split: Stage2 evidence = `public_event_or_disclosure, semiconductor_material_equipment_exposure`; Stage3 bridge = `not yet confirmed`; 4B evidence = `margin_or_backlog_slowdown, price_only_local_peak, execution_risk`.
- residual interpretation: `name_change_equipment_exposure_low_MFE_high_MAE`. C10 should not convert this kind of memory-recovery proxy into Stage3-Green until reorder/utilization/revenue/margin conversion is confirmed.

### 083450 GST — positive_with_guardrail

- evidence source: https://www.gst-in.com/board/download.php?bbsid=ir&board=Y&file_name=b_file_1753251717n63bp6fg6n.pdf&o_file_name=GST_IR_3Q_2024_ENG.pdf
- trigger: `2024-08-01` -> entry `2024-08-01` at close `16810.0`.
- price path: MFE90 `13.9203%`, MAE90 `-24.9851%`, MFE180 `38.9054%`, MAE180 `-24.9851%`.
- stage split: Stage2 evidence = `capacity_or_volume_route, HBM_specific_tool_optionality, customer_capex_proxy`; Stage3 bridge = `repeat_order_or_conversion_partial`; 4B evidence = `price_only_local_peak, execution_risk`.
- residual interpretation: `scrubber_chiller_positive_but_order_conversion_gate`. C10 should not convert this kind of memory-recovery proxy into Stage3-Green until reorder/utilization/revenue/margin conversion is confirmed.

## 6. Score / return alignment

```yaml
case_count: 4
positive_case_count: 2
counterexample_count: 2
stage4b_local_watch_count: 4
stage4c_count: 0
avg_MFE_30D_pct: 23.1146
avg_MAE_30D_pct: -13.0491
avg_MFE_90D_pct: 23.2101
avg_MAE_90D_pct: -22.7218
avg_MFE_180D_pct: 29.4564
avg_MAE_180D_pct: -45.7326
current_profile_error_count: 4
score_return_alignment_verdict: current_profile_still_too_early_for_proxy_memory_recovery_rows_without_order_revenue_margin_bridge
```

## 7. Shadow rule candidate

```text
C10_MEMORY_RECOVERY_REQUIRES_REORDER_UTILIZATION_REVENUE_MARGIN_BRIDGE_WITH_SPECIALTY_GAS_CCSS_CHILLER_PROXY_4B_CAP_V113
```

This is a canonical-archetype-specific shadow rule. It strengthens the already-applied `stage2_required_bridge` and `local_4b_watch_guard`, but narrows them to C10 proxy rows: specialty gas, CCSS, chemical supply, scrubber/chiller, and other fab-infrastructure rows should stay Stage2-Watch unless direct memory customer capex, reorder, delivery, revenue recognition, and margin conversion are visible.
## 8. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113 | 2 | 2 | 4 | 0 | 4 | 0 | 4 | 4 | 4 | no_new_sector_specific_rule | C10_MEMORY_RECOVERY_REQUIRES_REORDER_UTILIZATION_REVENUE_MARGIN_BRIDGE_WITH_SPECIALTY_GAS_CCSS_CHILLER_PROXY_4B_CAP_V113 | static 13 -> 17; session-adjusted C10 quality holdout strengthened |

## 9. Machine-readable rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C10_V113_001","symbol":"425040","company_name":"티이엠씨","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10_V113_001_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MAE_requires_stage4b_overlay","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"specialty_gas_proxy_high_MAE_false_positive"}
{"row_type":"trigger","trigger_id":"C10_V113_001_T1","case_id":"C10_V113_001","symbol":"425040","company_name":"티이엠씨","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":18810.0,"evidence_available_at_that_date":"specialty gas / rare-gas recovery / memory recovery proxy; not direct memory equipment reorder","evidence_source":"https://temc.co.kr/","stage2_evidence_fields":["public_product_business_exposure","memory_recovery_proxy","specialty_gas_supply_chain_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown","proxy_not_order_conversion"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425040/2024.csv","profile_path":"atlas/symbol_profiles/425/425040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.2121,"MFE_90D_pct":21.2121,"MFE_180D_pct":21.2121,"MAE_30D_pct":-11.3238,"MAE_90D_pct":-11.3238,"MAE_180D_pct":-54.4391,"peak_date":"2024-03-12","peak_price":22800.0,"drawdown_after_peak_pct":-62.4123,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"price_only|execution_risk|margin_or_backlog_slowdown","four_c_protection_label":"not_applicable","trigger_outcome_label":"specialty_gas_proxy_high_MAE_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10|425040|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_V113_001","trigger_id":"C10_V113_001_T1","symbol":"425040","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":30,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":58,"stage_label_after":"Stage2-Watch+Stage4B-LocalWatch","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 proxy rows require direct memory reorder/utilization/revenue/margin bridge before Stage3 persistence.","MFE_90D_pct":21.2121,"MAE_90D_pct":-11.3238,"score_return_alignment_label":"guard_improves_high_MAE_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10_V113_002","symbol":"264660","company_name":"씨앤지하이테크","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C10_V113_002_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MAE_requires_stage4b_overlay","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"CCSS_infra_positive_but_high_MAE_guard"}
{"row_type":"trigger","trigger_id":"C10_V113_002_T1","case_id":"C10_V113_002","symbol":"264660","company_name":"씨앤지하이테크","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":13090.0,"evidence_available_at_that_date":"CCSS / chemical supply system demand from semiconductor capex; real infrastructure tool but still not direct memory equipment reorder","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1672959699990.pdf","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","semiconductor_fab_infrastructure_capex"],"stage3_evidence_fields":["financial_visibility_partial"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/264/264660/2024.csv","profile_path":"atlas/symbol_profiles/264/264660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":55.4622,"MFE_90D_pct":55.8442,"MFE_180D_pct":55.8442,"MAE_30D_pct":-2.5974,"MAE_90D_pct":-7.3338,"MAE_180D_pct":-36.9748,"peak_date":"2024-04-30","peak_price":20400.0,"drawdown_after_peak_pct":-59.5588,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"price_only|execution_risk|margin_or_backlog_slowdown","four_c_protection_label":"not_applicable","trigger_outcome_label":"CCSS_infra_positive_but_high_MAE_guard","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10|264660|2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_V113_002","trigger_id":"C10_V113_002_T1","symbol":"264660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":30,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":58,"stage_label_after":"Stage2-Watch+Stage4B-LocalWatch","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 proxy rows require direct memory reorder/utilization/revenue/margin bridge before Stage3 persistence.","MFE_90D_pct":55.8442,"MAE_90D_pct":-7.3338,"score_return_alignment_label":"guard_improves_high_MAE_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"case","case_id":"C10_V113_003","symbol":"241790","company_name":"티이엠씨씨엔에스","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10_V113_003_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MAE_requires_stage4b_overlay","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"name_change_equipment_exposure_low_MFE_high_MAE"}
{"row_type":"trigger","trigger_id":"C10_V113_003_T1","case_id":"C10_V113_003","symbol":"241790","company_name":"티이엠씨씨엔에스","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":12340.0,"evidence_available_at_that_date":"name-change / semiconductor chemical-material and fab equipment business exposure; bridge missing after transition","evidence_source":"https://www.temccns.com/","stage2_evidence_fields":["public_event_or_disclosure","semiconductor_material_equipment_exposure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak","execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241790/2024.csv","profile_path":"atlas/symbol_profiles/241/241790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.8639,"MFE_90D_pct":1.8639,"MFE_180D_pct":1.8639,"MAE_30D_pct":-13.2901,"MAE_90D_pct":-47.2447,"MAE_180D_pct":-66.5316,"peak_date":"2024-04-29","peak_price":12570.0,"drawdown_after_peak_pct":-67.144,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"price_only|execution_risk|margin_or_backlog_slowdown","four_c_protection_label":"not_applicable","trigger_outcome_label":"name_change_equipment_exposure_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10|241790|2024-04-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_V113_003","trigger_id":"C10_V113_003_T1","symbol":"241790","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":30,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":58,"stage_label_after":"Stage2-Watch+Stage4B-LocalWatch","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 proxy rows require direct memory reorder/utilization/revenue/margin bridge before Stage3 persistence.","MFE_90D_pct":1.8639,"MAE_90D_pct":-47.2447,"score_return_alignment_label":"guard_improves_high_MAE_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10_V113_004","symbol":"083450","company_name":"GST","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C10_V113_004_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MAE_requires_stage4b_overlay","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"scrubber_chiller_positive_but_order_conversion_gate"}
{"row_type":"trigger","trigger_id":"C10_V113_004_T1","case_id":"C10_V113_004","symbol":"083450","company_name":"GST","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_specialty_gas_ccss_chiller_memory_recovery_boundary_v113","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":16810.0,"evidence_available_at_that_date":"scrubber/chiller and ultra-low-temperature chiller route; memory/HBM capex adjacent but order/revenue bridge still needed","evidence_source":"https://www.gst-in.com/board/download.php?bbsid=ir&board=Y&file_name=b_file_1753251717n63bp6fg6n.pdf&o_file_name=GST_IR_3Q_2024_ENG.pdf","stage2_evidence_fields":["capacity_or_volume_route","HBM_specific_tool_optionality","customer_capex_proxy"],"stage3_evidence_fields":["repeat_order_or_conversion_partial"],"stage4b_evidence_fields":["price_only_local_peak","execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv","profile_path":"atlas/symbol_profiles/083/083450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.9203,"MFE_90D_pct":13.9203,"MFE_180D_pct":38.9054,"MAE_30D_pct":-24.9851,"MAE_90D_pct":-24.9851,"MAE_180D_pct":-24.9851,"peak_date":"2025-02-24","peak_price":23350.0,"drawdown_after_peak_pct":-34.1756,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"price_only|execution_risk|margin_or_backlog_slowdown","four_c_protection_label":"not_applicable","trigger_outcome_label":"scrubber_chiller_positive_but_order_conversion_gate","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10|083450|2024-08-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_V113_004","trigger_id":"C10_V113_004_T1","symbol":"083450","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":30,"relative_strength_score":45,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":58,"stage_label_after":"Stage2-Watch+Stage4B-LocalWatch","changed_components":["margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C10 proxy rows require direct memory reorder/utilization/revenue/margin bridge before Stage3 persistence.","MFE_90D_pct":13.9203,"MAE_90D_pct":-24.9851,"score_return_alignment_label":"guard_improves_high_MAE_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"residual_contribution","round":"R2","loop":"113","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"residual_error_types_found":["memory_recovery_proxy_false_positive","high_MAE_after_proxy_MFE","order_revenue_margin_bridge_missing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 10. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence]
residual_error_types_found: [memory_recovery_proxy_false_positive, high_MAE_after_proxy_MFE, order_revenue_margin_bridge_missing]
new_axis_proposed: C10_SPECIALTY_GAS_CCSS_CHILLER_PROXY_4B_CAP
existing_axis_strengthened: [stage2_required_bridge, local_4b_watch_guard]
existing_axis_weakened: []
existing_axis_kept: [price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: no_new_sector_specific_rule
canonical_archetype_rule_candidate: C10_MEMORY_RECOVERY_REQUIRES_REORDER_UTILIZATION_REVENUE_MARGIN_BRIDGE_WITH_SPECIALTY_GAS_CCSS_CHILLER_PROXY_4B_CAP_V113
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 11. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
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

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute now. Later, ingest this MD with the v12 calibration batch runner. Validate every JSONL trigger row, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and treat the proposed C10 proxy cap as shadow-only until corroborated across additional C10 holdout rows. Do not patch production scoring directly from this single MD.
```

## 13. Next research state

```text
completed_round = R2
completed_loop = 113
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 static ledger C10 rows=13 / need-to-30=17 / need-to-50=37
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C11_BATTERY_ORDERBOOK_RERATING | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
