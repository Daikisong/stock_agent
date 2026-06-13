# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
completed_round: R2
completed_loop: 112
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger: C10 rows=13 / need_to_30=17 / need_to_50=37
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - holdout_validation
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption

The current working profile is treated as `e2r_2_1_stock_web_calibrated_proxy` with the already-applied global axes kept intact: Stage2 actionable bridge, strict Stage3-Yellow/Green thresholds, price-only blowoff block, non-price 4B requirement, and hard 4C thesis-break routing. This loop does not propose a production patch. It proposes a C10 shadow gate for memory-recovery equipment and consumable-cycle cases.

## 2. Round / Large Sector / Canonical Archetype Scope

`C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`. The scope is not HBM pure capacity (`C06`), HBM equipment order strength (`C07`), or advanced equipment valuation blowoff (`C09`). The test is narrower: when does memory-cycle recovery language become actual reorder / utilization / revenue / margin conversion for equipment, transfer modules, test handlers, cleaning equipment, or consumables?

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat ledger still lists C10 as Priority 0 with 13 representative rows, 17 short of the 30-row minimum stability band. This pass avoids the prior C10 core set used earlier in the session: `064760`, `083310`, `074600`, `036200`, `281820`, `095610`, `089970`, `084370`, `092870`, `033160`, `183300`, `166090`, `101160`, `104830`, `005290`, `357780`, `059090`. It adds six C10-boundary or C10-pure rows with clean 180D price paths.

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

The six representative rows use `tradable_raw` OHLCV. All rows have entry date, entry price, 30D/90D/180D MFE and MAE, and clean 180D corporate-action windows.

## 5. Historical Eligibility Gate

```yaml
historical_trigger_dates: true
entry_dates_in_tradable_shards: true
forward_window_trading_days_minimum: 180
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
calibration_usable_rows: 6
```

`083450 GST` was considered for the same C10 theme but not used in this MD because the symbol profile lists 2024 corporate-action candidate dates in the relevant window. It should be used only with a clean post-action window in a later pass.

## 6. Canonical Archetype Compression Map

```text
C10 positive path:
memory recovery -> reorder or replacement-cycle visibility -> shipment/revenue recognition -> margin bridge -> Stage3-Yellow candidate

C10 counterexample path:
memory beta / HBM-adjacent narrative -> no named order or delayed revenue conversion -> local MFE only -> high 90D/180D MAE -> Stage2-Watch or Stage4B overlay
```

## 7. Case Selection Summary

|symbol|name|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|classification|
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
|272110|케이엔제이|Stage3-Yellow|2024-03-06|17050.0|55.132|-3.4604|55.132|-3.4604|55.132|-29.912|positive_with_local_4B_watch|
|232680|라온테크|Stage3-Yellow|2024-12-19|6460.0|55.418|-5.2632|82.0433|-5.2632|82.0433|-5.2632|positive_with_local_4B_watch|
|187870|디바이스이엔지|Stage2-Actionable|2024-02-19|15120.0|5.8201|-4.1667|16.2037|-4.1667|16.2037|-25.5952|counterexample_low_MFE_delayed_margin_bridge|
|089790|제이티|Stage4B|2024-03-11|9830.0|15.5646|-7.8332|15.5646|-30.7223|15.5646|-66.5819|counterexample_high_MAE|
|160980|싸이맥스|Stage4B|2024-03-20|20400.0|12.0098|-18.4804|16.4216|-26.0784|16.4216|-63.6765|counterexample_high_MAE|
|317330|덕산테코피아|Stage4B|2024-11-15|29950.0|24.8748|-11.1853|32.5543|-34.5242|32.5543|-50.4508|counterexample_mixed_material_beta_high_MAE|


## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 2
counterexample_count: 4
4B_case_count: 6
4C_case_count: 0
current_profile_error_count: 5
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
```

`케이엔제이` and `라온테크` preserve the positive side of C10: real consumable or transfer-module exposure can generate strong MFE when the market sees replacement-cycle or equipment-cycle conversion. `디바이스이엔지`, `제이티`, `싸이맥스`, and `덕산테코피아` are the guardrail side: credible memory/HBM-adjacent language is insufficient when the order, shipment, revenue, and margin bridge is not yet visible.

## 9. Evidence Source Map

|symbol|evidence source|evidence summary|
|---|---|---|
|272110 케이엔제이|https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/05/240306_KNJ_f.pdf|SiC focus ring report; aftermarket direct-to-memory-customer consumable route; 삼성전자/SK하이닉스 memory exposure and replacement-cycle demand.|
|232680 라온테크|https://w4.kirs.or.kr/download/research/241219_%EA%B8%B0%EA%B3%84%EC%9E%A5%EB%B9%84_%EB%9D%BC%EC%98%A8%ED%85%8C%ED%81%AC%28232680%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EC%A0%9C%EC%A1%B0%EC%9A%A9%20%EC%9B%A8%EC%9D%B4%ED%8D%BC%20%EC%9D%B4%EC%86%A1%20%EB%A1%9C%EB%B4%87%20%EB%B0%8F%20%EB%AA%A8%EB%93%88%20%EC%A0%9C%EC%A1%B0%20%EC%A0%84%EB%AC%B8%20%EC%97%85%EC%B2%B4_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf|Wafer-transfer robot/module report; semiconductor equipment market expansion and process automation demand, but order/revenue conversion timing remains the gate.|
|187870 디바이스이엔지|https://ssl.pstatic.net/imgstock/upload/research/company/1708297940818.pdf|FOUP contamination-control equipment and OLED FMM cleaning report; semiconductor FOUP exposure exists, but near-term order/revenue bridge was weak.|
|089790 제이티|https://www.theinvest.co.kr/brdview.php?ud=IC0722080008561a315eirn_45|IR Q&A/article on HBM and DDR5 burn-in handler optionality; high-performance memory handler route exists, but qualification/order bridge was not yet confirmed.|
|160980 싸이맥스|https://ssl.pstatic.net/imgstock/upload/research/company/1710895255135.pdf|Hidden HBM beneficiary report; wafer-transfer equipment supplies through major equipment makers to Samsung/SK Hynix, but the entry still lacked firm revenue timing.|
|317330 덕산테코피아|https://kind.krx.co.kr/common/disclsviewer.do?acptno=20241114002294&docno=&method=search&viewerhost=|Quarterly filing; semiconductor/OLED precursor base exists, but 2차전지 electrolyte optionality and weak earnings bridge contaminate pure memory-recovery interpretation.|


## 10. Price Data Source Map

|symbol|price shard path|profile path|corporate-action status|
|---|---|---|---|
|272110|atlas/ohlcv_tradable_by_symbol_year/272/272110/{year}.csv|atlas/symbol_profiles/272/272110.json|clean_180D_window|
|232680|atlas/ohlcv_tradable_by_symbol_year/232/232680/{year}.csv|atlas/symbol_profiles/232/232680.json|clean_180D_window|
|187870|atlas/ohlcv_tradable_by_symbol_year/187/187870/{year}.csv|atlas/symbol_profiles/187/187870.json|clean_180D_window|
|089790|atlas/ohlcv_tradable_by_symbol_year/089/089790/{year}.csv|atlas/symbol_profiles/089/089790.json|clean_180D_window|
|160980|atlas/ohlcv_tradable_by_symbol_year/160/160980/{year}.csv|atlas/symbol_profiles/160/160980.json|clean_180D_window|
|317330|atlas/ohlcv_tradable_by_symbol_year/317/317330/{year}.csv|atlas/symbol_profiles/317/317330.json|clean_180D_window|


## 11. Case-by-Case Trigger Grid

### 272110 케이엔제이
SiC focus ring is the cleanest C10 consumable route in this set. The report tied the company to SiC ring replacement demand and major Korean memory customers. The price path delivered a 55.1320% 180D MFE, but the peak drawdown after April 2024 was -54.8204%, so the correct profile is `Stage3-Yellow + local 4B watch`, not free Green.

### 232680 라온테크
The wafer-transfer robot / module report is a genuine memory-equipment-cycle positive. The 180D MFE reached 82.0433% with shallow MAE, but the post-peak drawdown reached -43.7925%. The case strengthens the rule that C10 can promote when equipment-cycle visibility is real, while still forcing a local 4B overlay after vertical rerating.

### 187870 디바이스이엔지
FOUP cleaning and contamination-control equipment belongs near C10, but this row lacked a fresh named order or memory-customer revenue bridge. 180D MFE was only 16.2037%, while 180D MAE reached -25.5952%. This is a Stage2-actionable exposure, not a Stage3 rerating.

### 089790 제이티
HBM/DDR5 handler optionality created a plausible Stage2 story, but without qualification or named order confirmation the 180D MAE reached -66.5819%. The row should be capped at Stage4B local watch until order/revenue conversion is visible.

### 160980 싸이맥스
The wafer-transfer equipment thesis was real, but the March 2024 entry carried C09/C10 optionality more than confirmed C10 conversion. MFE was modest and MAE became severe. It is a good counterexample to treating HBM-adjacent transfer equipment language as automatic C10 Stage3.

### 317330 덕산테코피아
The company has semiconductor precursor exposure, but the 2024 trigger mixed semiconductor material, OLED, and 2차전지 optionality. The 180D MAE of -50.4508% shows why C10 needs decontamination before treating material beta as memory-cycle recovery.

## 12. Trigger-Level OHLC Backtest Tables

|symbol|name|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|classification|
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
|272110|케이엔제이|Stage3-Yellow|2024-03-06|17050.0|55.132|-3.4604|55.132|-3.4604|55.132|-29.912|positive_with_local_4B_watch|
|232680|라온테크|Stage3-Yellow|2024-12-19|6460.0|55.418|-5.2632|82.0433|-5.2632|82.0433|-5.2632|positive_with_local_4B_watch|
|187870|디바이스이엔지|Stage2-Actionable|2024-02-19|15120.0|5.8201|-4.1667|16.2037|-4.1667|16.2037|-25.5952|counterexample_low_MFE_delayed_margin_bridge|
|089790|제이티|Stage4B|2024-03-11|9830.0|15.5646|-7.8332|15.5646|-30.7223|15.5646|-66.5819|counterexample_high_MAE|
|160980|싸이맥스|Stage4B|2024-03-20|20400.0|12.0098|-18.4804|16.4216|-26.0784|16.4216|-63.6765|counterexample_high_MAE|
|317330|덕산테코피아|Stage4B|2024-11-15|29950.0|24.8748|-11.1853|32.5543|-34.5242|32.5543|-50.4508|counterexample_mixed_material_beta_high_MAE|


Aggregate price-path metrics:

```yaml
avg_MFE_30D_pct: 28.1366
avg_MAE_30D_pct: -8.3982
avg_MFE_90D_pct: 36.3199
avg_MAE_90D_pct: -17.3692
avg_MFE_180D_pct: 36.3199
avg_MAE_180D_pct: -40.2466
```

## 13. Current Calibrated Profile Stress Test

The current calibrated profile is directionally correct in requiring non-price evidence. The residual error is narrower: C10 still needs a stricter split between pure memory-cycle conversion and HBM-adjacent or equipment-optionality beta. For positive C10 cases, the profile can still be too late if it waits for fully printed earnings. For counterexamples, the profile can still be too early if it accepts product exposure without a named order/revenue bridge.

```yaml
current_profile_correct: 1
current_profile_too_late: 1
current_profile_false_positive: 4
stage2_bonus_too_high_for_counterexamples: true
yellow_threshold_generally_adequate: true
green_threshold_adequate_but_bridge_filter_needed: true
price_only_blowoff_guard_appropriate: true
full_4B_non_price_requirement_appropriate: true
hard_4C_routing_not_triggered: true
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used. `green_lateness_ratio = not_applicable` for all rows. Stage2/Stage2-Actionable is enough for credible exposure, but Stage3-Yellow should require at least two of the following: named customer/order, repeat consumable replacement, shipment timing, revenue recognition, and margin bridge.

## 15. 4B Local vs Full-window Timing Audit

Local 4B is required in five rows. The main failure mode is not hard thesis break; it is peak-to-trough damage after fast MFE without second bridge confirmation. This supports `local_4b_watch_guard` rather than a full Stage4C route.

## 16. 4C Protection Audit

No row has explicit order cut, qualification failure, accounting break, or hard cancellation evidence. Therefore `hard_4c_thesis_break_routes_to_4c` is kept but not newly strengthened by this loop.

## 17. Sector-Specific Rule Candidate

```text
L2_C10_MEMORY_RECOVERY_EQUIPMENT_REORDER_UTILIZATION_REVENUE_MARGIN_GATE
```

## 18. Canonical-Archetype Rule Candidate

```text
C10_MEMORY_RECOVERY_REQUIRES_REORDER_SHIPMENT_REVENUE_AND_MARGIN_BRIDGE_WITH_HBM_ADJACENT_DECONTAMINATION_V112
```

Rule mechanism: C10 promotion should require a concrete conversion bridge. If a case only has memory beta, HBM-adjacent product exposure, or general equipment-cycle narrative, cap it at Stage2-Watch or Stage4B until order/revenue/margin confirmation appears.

## 19. Before / After Backtest Comparison

|profile|eligible rows|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|verdict|
|---|---:|---:|---:|---:|---:|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|6|36.3199|-17.3692|36.3199|-40.2466|too many Stage2/Yellow candidates survive without bridge|
|P0b e2r_2_0_baseline_reference|6|36.3199|-17.3692|36.3199|-40.2466|would over-promote product-exposure narratives|
|P1 sector_specific_candidate_profile|6|36.3199|-17.3692|36.3199|-40.2466|requires non-price conversion bridge for L2 equipment cycle|
|P2 canonical_archetype_candidate_profile|6|36.3199|-17.3692|36.3199|-40.2466|best fit; separates C10 from C06/C07/C09|
|P3 counterexample_guard_profile|4|20.1861|-23.8729|20.1861|-51.5761|best at blocking false positives|

## 20. Score-Return Alignment Matrix

The score-return alignment improves when `customer_quality_score`, `contract_score`, and `margin_bridge_score` are not inferred from product exposure alone. `relative_strength_score` is useful only as a supporting field. In C10, high relative strength without reorder/revenue confirmation is frequently a local 4B trap.

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L2_AI_SEMICONDUCTOR_ELECTRONICS|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass|2|4|6|0|6|0|6|6|5|L2_C10_MEMORY_RECOVERY_EQUIPMENT_REORDER_UTILIZATION_REVENUE_MARGIN_GATE|C10_MEMORY_RECOVERY_REQUIRES_REORDER_SHIPMENT_REVENUE_AND_MARGIN_BRIDGE_WITH_HBM_ADJACENT_DECONTAMINATION_V112|static 13 → 19; session-adjusted holdout strengthened|

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - memory_beta_false_positive
  - HBM_adjacent_proxy_without_revenue_bridge
  - local_4B_after_fast_MFE
  - consumable_reorder_positive_but_drawdown_watch
new_axis_proposed: C10_MEMORY_RECOVERY_REQUIRES_REORDER_SHIPMENT_REVENUE_AND_MARGIN_BRIDGE_WITH_HBM_ADJACENT_DECONTAMINATION_V112
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_C10_MEMORY_RECOVERY_EQUIPMENT_REORDER_UTILIZATION_REVENUE_MARGIN_GATE
canonical_archetype_rule_candidate: C10_MEMORY_RECOVERY_REQUIRES_REORDER_SHIPMENT_REVENUE_AND_MARGIN_BRIDGE_WITH_HBM_ADJACENT_DECONTAMINATION_V112
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 6 new independent cases, 4 counterexamples, and 5 residual errors for L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE/mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass.

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger rows, stock-web entry/forward OHLC paths, clean 180D windows, positive/counterexample split, C10-specific shadow rule. Not validated: live candidates, production scoring patch, current watchlist, adjusted-price total return, or brokerage/execution behavior.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_order_revenue_margin_bridge_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Require reorder/shipment/revenue/margin bridge before C10 Stage3 promotion","Blocks 4 high-MAE false positives while preserving 2 positives","C10_L112_272110|C10_L112_232680|C10_L112_187870|C10_L112_089790|C10_L112_160980|C10_L112_317330",6,6,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C10_L112_272110","symbol":"272110","company_name":"케이엔제이","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C10_L112_272110_2024-03-06_Stage3_Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_with_local_4B_watch","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"SiC ring reorder/consumable logic is real, but local peak drawdown argues against Green without replacement-volume/margin confirmation."}
{"row_type":"trigger","trigger_id":"C10_L112_272110_2024-03-06_Stage3_Yellow","case_id":"C10_L112_272110","symbol":"272110","company_name":"케이엔제이","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":17050.0,"evidence_available_at_that_date":"SiC focus ring report; aftermarket direct-to-memory-customer consumable route; 삼성전자/SK하이닉스 memory exposure and replacement-cycle demand.","evidence_source":"https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2024/03/05/240306_KNJ_f.pdf","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/272/272110/{year}.csv","profile_path":"atlas/symbol_profiles/272/272110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":55.132,"MFE_90D_pct":55.132,"MFE_180D_pct":55.132,"MAE_30D_pct":-3.4604,"MAE_90D_pct":-3.4604,"MAE_180D_pct":-29.912,"peak_date":"2024-04-08","peak_price":26450.0,"drawdown_after_peak_pct":-54.8204,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"sic_focus_ring_memory_consumable_positive_but_peak_drawdown_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_272110_2024-03-06","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_L112_272110","trigger_id":"C10_L112_272110_2024-03-06_Stage3_Yellow","symbol":"272110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":45,"margin_bridge_score":55,"revision_score":45,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":42.9,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":55,"margin_bridge_score":65,"revision_score":45,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":44.6,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","execution_risk_score","contract_score"],"component_delta_explanation":"C10 shadow gate rewards repeat consumable/order conversion but caps memory-beta optionality lacking named order, revenue recognition, and margin bridge.","MFE_90D_pct":55.132,"MAE_90D_pct":-3.4604,"score_return_alignment_label":"positive_with_local_4B_watch","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C10_L112_232680","symbol":"232680","company_name":"라온테크","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C10_L112_232680_2024-12-19_Stage3_Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_with_local_4B_watch","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Price path gives very strong MFE with shallow early MAE, but later peak drawdown requires local 4B overlay after rerating."}
{"row_type":"trigger","trigger_id":"C10_L112_232680_2024-12-19_Stage3_Yellow","case_id":"C10_L112_232680","symbol":"232680","company_name":"라온테크","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-12-19","entry_date":"2024-12-19","entry_price":6460.0,"evidence_available_at_that_date":"Wafer-transfer robot/module report; semiconductor equipment market expansion and process automation demand, but order/revenue conversion timing remains the gate.","evidence_source":"https://w4.kirs.or.kr/download/research/241219_%EA%B8%B0%EA%B3%84%EC%9E%A5%EB%B9%84_%EB%9D%BC%EC%98%A8%ED%85%8C%ED%81%AC%28232680%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EC%A0%9C%EC%A1%B0%EC%9A%A9%20%EC%9B%A8%EC%9D%B4%ED%8D%BC%20%EC%9D%B4%EC%86%A1%20%EB%A1%9C%EB%B4%87%20%EB%B0%8F%20%EB%AA%A8%EB%93%88%20%EC%A0%9C%EC%A1%B0%20%EC%A0%84%EB%AC%B8%20%EC%97%85%EC%B2%B4_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232680/{year}.csv","profile_path":"atlas/symbol_profiles/232/232680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":55.418,"MFE_90D_pct":82.0433,"MFE_180D_pct":82.0433,"MAE_30D_pct":-5.2632,"MAE_90D_pct":-5.2632,"MAE_180D_pct":-5.2632,"peak_date":"2025-02-19","peak_price":11760.0,"drawdown_after_peak_pct":-43.7925,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"wafer_transfer_robot_positive_but_conversion_gate_needed","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_232680_2024-12-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_L112_232680","trigger_id":"C10_L112_232680_2024-12-19_Stage3_Yellow","symbol":"232680","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":45,"margin_bridge_score":55,"revision_score":45,"relative_strength_score":70,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":38.8,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":55,"margin_bridge_score":65,"revision_score":45,"relative_strength_score":70,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":40.4,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","execution_risk_score","contract_score"],"component_delta_explanation":"C10 shadow gate rewards repeat consumable/order conversion but caps memory-beta optionality lacking named order, revenue recognition, and margin bridge.","MFE_90D_pct":82.0433,"MAE_90D_pct":-5.2632,"score_return_alignment_label":"positive_with_local_4B_watch","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C10_L112_187870","symbol":"187870","company_name":"디바이스이엔지","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10_L112_187870_2024-02-19_Stage2_Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_delayed_margin_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Exposure is real, but memory-cycle demand did not translate into a clean order/revenue/margin path within 180D."}
{"row_type":"trigger","trigger_id":"C10_L112_187870_2024-02-19_Stage2_Actionable","case_id":"C10_L112_187870","symbol":"187870","company_name":"디바이스이엔지","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":15120.0,"evidence_available_at_that_date":"FOUP contamination-control equipment and OLED FMM cleaning report; semiconductor FOUP exposure exists, but near-term order/revenue bridge was weak.","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1708297940818.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/187/187870/{year}.csv","profile_path":"atlas/symbol_profiles/187/187870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.8201,"MFE_90D_pct":16.2037,"MFE_180D_pct":16.2037,"MAE_30D_pct":-4.1667,"MAE_90D_pct":-4.1667,"MAE_180D_pct":-25.5952,"peak_date":"2024-06-18","peak_price":17570.0,"drawdown_after_peak_pct":-35.9704,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"foup_cleaning_equipment_low_mfe_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_187870_2024-02-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_L112_187870","trigger_id":"C10_L112_187870_2024-02-19_Stage2_Actionable","symbol":"187870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":30,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":45,"customer_quality_score":65,"policy_or_regulatory_score":10,"valuation_repricing_score":40,"execution_risk_score":75,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":35},"weighted_score_before":39.6,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":30,"margin_bridge_score":15,"revision_score":25,"relative_strength_score":45,"customer_quality_score":65,"policy_or_regulatory_score":10,"valuation_repricing_score":40,"execution_risk_score":85,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":35},"weighted_score_after":38.8,"stage_label_after":"Stage2-Watch/Stage4B overlay","changed_components":["margin_bridge_score","execution_risk_score","contract_score"],"component_delta_explanation":"C10 shadow gate rewards repeat consumable/order conversion but caps memory-beta optionality lacking named order, revenue recognition, and margin bridge.","MFE_90D_pct":16.2037,"MAE_90D_pct":-4.1667,"score_return_alignment_label":"counterexample_low_MFE_delayed_margin_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10_L112_089790","symbol":"089790","company_name":"제이티","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10_L112_089790_2024-03-11_Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"HBM/DDR5 language can open Stage2 watch, but without signed order or revenue conversion it becomes high-MAE 4B."}
{"row_type":"trigger","trigger_id":"C10_L112_089790_2024-03-11_Stage4B","case_id":"C10_L112_089790","symbol":"089790","company_name":"제이티","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":9830.0,"evidence_available_at_that_date":"IR Q&A/article on HBM and DDR5 burn-in handler optionality; high-performance memory handler route exists, but qualification/order bridge was not yet confirmed.","evidence_source":"https://www.theinvest.co.kr/brdview.php?ud=IC0722080008561a315eirn_45","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","contract_delay"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089790/{year}.csv","profile_path":"atlas/symbol_profiles/089/089790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.5646,"MFE_90D_pct":15.5646,"MFE_180D_pct":15.5646,"MAE_30D_pct":-7.8332,"MAE_90D_pct":-30.7223,"MAE_180D_pct":-66.5819,"peak_date":"2024-04-12","peak_price":11360.0,"drawdown_after_peak_pct":-71.0827,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["price_only_local_peak","positioning_overheat","contract_delay"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_ddr5_handler_optionality_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_089790_2024-03-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_L112_089790","trigger_id":"C10_L112_089790_2024-03-11_Stage4B","symbol":"089790","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":30,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":45,"customer_quality_score":65,"policy_or_regulatory_score":10,"valuation_repricing_score":40,"execution_risk_score":75,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":35},"weighted_score_before":39.6,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":30,"margin_bridge_score":15,"revision_score":25,"relative_strength_score":45,"customer_quality_score":65,"policy_or_regulatory_score":10,"valuation_repricing_score":40,"execution_risk_score":85,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":35},"weighted_score_after":38.8,"stage_label_after":"Stage2-Watch/Stage4B overlay","changed_components":["margin_bridge_score","execution_risk_score","contract_score"],"component_delta_explanation":"C10 shadow gate rewards repeat consumable/order conversion but caps memory-beta optionality lacking named order, revenue recognition, and margin bridge.","MFE_90D_pct":15.5646,"MAE_90D_pct":-30.7223,"score_return_alignment_label":"counterexample_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10_L112_160980","symbol":"160980","company_name":"싸이맥스","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10_L112_160980_2024-03-20_Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C10/C09 boundary: transfer-robot exposure is credible, but no named order/revenue bridge created a sharp MAE path."}
{"row_type":"trigger","trigger_id":"C10_L112_160980_2024-03-20_Stage4B","case_id":"C10_L112_160980","symbol":"160980","company_name":"싸이맥스","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":20400.0,"evidence_available_at_that_date":"Hidden HBM beneficiary report; wafer-transfer equipment supplies through major equipment makers to Samsung/SK Hynix, but the entry still lacked firm revenue timing.","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1710895255135.pdf","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","contract_delay"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/160/160980/{year}.csv","profile_path":"atlas/symbol_profiles/160/160980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.0098,"MFE_90D_pct":16.4216,"MFE_180D_pct":16.4216,"MAE_30D_pct":-18.4804,"MAE_90D_pct":-26.0784,"MAE_180D_pct":-63.6765,"peak_date":"2024-05-29","peak_price":23750.0,"drawdown_after_peak_pct":-68.8,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["price_only_local_peak","positioning_overheat","contract_delay"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_transfer_robot_optional_path_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_160980_2024-03-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_L112_160980","trigger_id":"C10_L112_160980_2024-03-20_Stage4B","symbol":"160980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":30,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":45,"customer_quality_score":65,"policy_or_regulatory_score":10,"valuation_repricing_score":40,"execution_risk_score":75,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":35},"weighted_score_before":39.6,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":30,"margin_bridge_score":15,"revision_score":25,"relative_strength_score":45,"customer_quality_score":65,"policy_or_regulatory_score":10,"valuation_repricing_score":40,"execution_risk_score":85,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":35},"weighted_score_after":38.8,"stage_label_after":"Stage2-Watch/Stage4B overlay","changed_components":["margin_bridge_score","execution_risk_score","contract_score"],"component_delta_explanation":"C10 shadow gate rewards repeat consumable/order conversion but caps memory-beta optionality lacking named order, revenue recognition, and margin bridge.","MFE_90D_pct":16.4216,"MAE_90D_pct":-26.0784,"score_return_alignment_label":"counterexample_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C10_L112_317330","symbol":"317330","company_name":"덕산테코피아","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C10_L112_317330_2024-11-15_Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_mixed_material_beta_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The memory-material thesis was not clean enough; battery-material optionality and delayed margin bridge dominated the risk path."}
{"row_type":"trigger","trigger_id":"C10_L112_317330_2024-11-15_Stage4B","case_id":"C10_L112_317330","symbol":"317330","company_name":"덕산테코피아","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_consumable_transfer_robot_boundary_fourth_pass","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-11-14","entry_date":"2024-11-15","entry_price":29950.0,"evidence_available_at_that_date":"Quarterly filing; semiconductor/OLED precursor base exists, but 2차전지 electrolyte optionality and weak earnings bridge contaminate pure memory-recovery interpretation.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20241114002294&docno=&method=search&viewerhost=","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/317/317330/{year}.csv","profile_path":"atlas/symbol_profiles/317/317330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.8748,"MFE_90D_pct":32.5543,"MFE_180D_pct":32.5543,"MAE_30D_pct":-11.1853,"MAE_90D_pct":-34.5242,"MAE_180D_pct":-50.4508,"peak_date":"2025-02-20","peak_price":39700.0,"drawdown_after_peak_pct":-62.6196,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"precursor_memory_beta_contaminated_by_battery_optionality_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_317330_2024-11-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_L112_317330","trigger_id":"C10_L112_317330_2024-11-15_Stage4B","symbol":"317330","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":70,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":75,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":35},"weighted_score_before":39.6,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":15,"revision_score":25,"relative_strength_score":70,"customer_quality_score":35,"policy_or_regulatory_score":10,"valuation_repricing_score":65,"execution_risk_score":85,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":35},"weighted_score_after":38.8,"stage_label_after":"Stage2-Watch/Stage4B overlay","changed_components":["margin_bridge_score","execution_risk_score","contract_score"],"component_delta_explanation":"C10 shadow gate rewards repeat consumable/order conversion but caps memory-beta optionality lacking named order, revenue recognition, and margin bridge.","MFE_90D_pct":32.5543,"MAE_90D_pct":-34.5242,"score_return_alignment_label":"counterexample_mixed_material_beta_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"112","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"residual_error_types_found":["memory_beta_false_positive","order_revenue_bridge_gap","local_4B_after_fast_MFE","pure_memory_cycle_decontamination"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

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
completed_loop: 112
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger: C10 rows=13 / need_to_30=17 / need_to_50=37
next_recommended_archetypes:
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
  - C11_BATTERY_ORDERBOOK_RERATING
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Evidence sources are embedded per case in the Evidence Source Map and JSONL rows.

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 10
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
