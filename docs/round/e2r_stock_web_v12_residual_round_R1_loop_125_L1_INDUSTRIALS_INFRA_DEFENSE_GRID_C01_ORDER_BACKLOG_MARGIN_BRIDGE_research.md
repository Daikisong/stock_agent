# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
filename = e2r_stock_web_v12_residual_round_R1_loop_125_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round = R1
selected_loop = 125
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under_30_representative_rows / C01 rows 19 need_to_30 11
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK
loop_objective = coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery
production_scoring_changed = false
shadow_weight_only = true
```
This loop adds **6** new independent C01 cases, **2** counterexamples, and **5** residual errors for **L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C01_ORDER_BACKLOG_MARGIN_BRIDGE**.

## 1. Current Calibrated Profile Assumption
Current proxy: `e2r_2_1_stock_web_calibrated_proxy`. Already-applied global axes are treated as existing guardrails, not re-proposed as global rules. This MD tests a C01-specific backlog-quality bridge: backlog is Stage2 raw material; delivery/mix/productivity/margin/FCF bridge is the furnace that turns it into Stage2-Actionable or Yellow.

## 2. Round / Large Sector / Canonical Archetype Scope
`C01_ORDER_BACKLOG_MARGIN_BRIDGE` maps to `R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID`. This is not C02 grid/datacenter CAPEX and not C03 defense export framework. The scope is shipbuilding and marine-engine backlog where high-priced vessel recognition, old low-margin backlog roll-off, productivity, FX, and margin conversion determine rerating quality.

## 3. Previous Coverage / Duplicate Avoidance Check
`V12_Research_No_Repeat_Index.md` marks C01 as Priority 0 with 19 representative rows, `need_to_30 = 11`, `need_to_50 = 31`. Strict no-repeat key: `canonical_archetype_id + symbol + trigger_type + entry_date`. This loop avoids prior in-session C02/C09/C14/C10/C06/C07/C11 outputs and selects a new canonical.

## 4. Stock-Web OHLC Input / Price Source Validation
```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```
All representative trigger rows below use stock-web tradable shards and include complete 30D/90D/180D MFE and MAE fields.

## 5. Historical Eligibility Gate
|check|result|
|---|---|
|trigger_date historical|pass|
|entry_date in stock-web tradable shard|pass|
|forward 180 trading days available|pass for 6 trigger rows|
|MFE/MAE 30D/90D/180D complete|pass|
|corporate-action contaminated 180D window|none detected from tradable shard continuity; rows marked clean_180D_window|
|narrative-only item|Samsung Heavy Russia cancellation after 2025-06-18 has insufficient 180D forward window and is not a trigger row|

## 6. Canonical Archetype Compression Map
|fine_archetype_id|canonical_archetype_id|compression rule|
|---|---|---|
|SHIPBUILDING_HIGH_PRICED_VESSEL_MARGIN_BRIDGE|C01_ORDER_BACKLOG_MARGIN_BRIDGE|high-priced vessels and productivity convert backlog into margin|
|MARINE_ENGINE_LOW_MARGIN_BACKLOG_PURGE|C01_ORDER_BACKLOG_MARGIN_BRIDGE|old low-profit engine orders rolling off is a margin bridge|
|TURNAROUND_FORECAST_HIGH_MAE_GUARD|C01_ORDER_BACKLOG_MARGIN_BRIDGE|forecasted swing to profit can be Stage2, but high MAE blocks early Yellow|
|ONE_QUARTER_LOSS_4C_FALSE_BREAK|C01_ORDER_BACKLOG_MARGIN_BRIDGE|single-quarter loss is 4B/watch before hard 4C if backlog repair remains alive|

## 7. Case Selection Summary
|case|symbol|trigger_type|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|role|verdict|
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
|C01-R1-L125-HDKSOE-20241213|009540|Stage3-Yellow|2024-12-13|210,000|19.76|-3.57|30.95|-11.57|108.57|-11.57|positive|current_profile_missed_structural|
|C01-R1-L125-HHI-20250424|329180|Stage3-Yellow|2025-04-24|376,000|21.41|-3.99|42.29|-3.99|73.4|-3.99|positive|current_profile_too_late|
|C01-R1-L125-HANWHAENGINE-20250214|082740|Stage3-Yellow|2025-02-14|24,350|18.07|-16.02|32.85|-17.86|121.36|-17.86|positive|current_profile_missed_structural|
|C01-R1-L125-SHI-20250424|010140|Stage2-Actionable|2025-04-24|14,590|20.08|-3.91|50.79|-3.91|122.76|-3.91|positive|current_profile_correct|
|C01-R1-L125-MIPO-20250117|010620|Stage2-Actionable|2025-01-17|128,300|12.47|-18.86|59.78|-22.45|72.64|-22.45|counterexample|current_profile_false_positive|
|C01-R1-L125-HANWHAOCEAN-20240726|042660|Stage4C|2024-07-26|30,950|14.05|-17.93|32.63|-17.93|181.74|-17.93|counterexample|current_profile_4C_too_early|


## 8. Positive vs Counterexample Balance
```text
positive_case_count = 4
counterexample_count = 2
4B_case_count = 0
4C_case_count = 1
calibration_usable_case_count = 6
calibration_usable_trigger_count = 6
representative_trigger_count = 6
```
Positive controls are HD한국조선해양, HD현대중공업, 한화엔진, and 삼성중공업. Counterexamples are HD현대미포, where an expected profit swing still had a -22.45% MAE before paying off, and 한화오션, where a Q2 operating loss would have been an over-eager hard 4C despite later +181.74% 180D MFE.

## 9. Evidence Source Map
|source|used for|url|
|---|---|---|
|HDKSOE_VALUEUP|evidence source|https://www.hd-ksoe.com/data/HDKSOE%20Value-up_EN_241213_1.pdf|
|HDKSOE_1Q25|evidence source|https://www.hd-ksoe.com/data/25.1Q_KSOE%20Consolidated%20Earnings%20Release_fn.pdf|
|HHI_YNA_1Q25|evidence source|https://en.yna.co.kr/view/AEN20250424007700320|
|HANWHA_ENGINE_2024|evidence source|https://www.hanwha-engine.com/attach/download/1255184f-68f8-40aa-942c-8e0e50264cbf|
|MIPO_MIRAE_20250117|evidence source|https://securities.miraeasset.com/bbs/download/2133913.pdf?attachmentId=2133913|
|SHI_YNA_Q1_2025|evidence source|https://en.yna.co.kr/view/AEN20250424009851320|
|SHI_IMARINE_2024|evidence source|https://www.imarinenews.com/20846.html|
|HANWHA_OCEAN_ASIAE_Q2_2024|evidence source|https://www.asiae.co.kr/en/article/2024072614321195934|
|HANWHA_OCEAN_YNA_Q2_2024|evidence source|https://en.yna.co.kr/view/AEN20240726005551320|

## 10. Price Data Source Map
|symbol|company|price_shard_path|profile_path|entry_date|180D window end|
|---|---|---|---|---|---|
|009540|HD한국조선해양|atlas/ohlcv_tradable_by_symbol_year/009/009540/2024.csv|atlas/symbol_profiles/009/009540.json|2024-12-13|2025-09-10|
|329180|HD현대중공업|atlas/ohlcv_tradable_by_symbol_year/329/329180/2025.csv|atlas/symbol_profiles/329/329180.json|2025-04-24|2026-01-20|
|082740|한화엔진|atlas/ohlcv_tradable_by_symbol_year/082/082740/2025.csv|atlas/symbol_profiles/082/082740.json|2025-02-14|2025-11-10|
|010140|삼성중공업|atlas/ohlcv_tradable_by_symbol_year/010/010140/2025.csv|atlas/symbol_profiles/010/010140.json|2025-04-24|2026-01-20|
|010620|HD현대미포|atlas/ohlcv_tradable_by_symbol_year/010/010620/2025.csv|atlas/symbol_profiles/010/010620.json|2025-01-17|2025-10-17|
|042660|한화오션|atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv|atlas/symbol_profiles/042/042660.json|2024-07-26|2025-04-24|

## 11. Case-by-Case Trigger Grid
- **HD한국조선해양 / 009540**: Backlog quality plus mix/productivity bridge came before the large 180D rerating. MFE90=30.95%, MAE90=-11.57%, MFE180=108.57%.
- **HD현대중공업 / 329180**: Confirmed earnings bridge converted backlog into margin visibility. MFE90=42.29%, MAE90=-3.99%, MFE180=73.4%.
- **한화엔진 / 082740**: Engine supplier rerating appeared when old low-margin backlog rolled off. MFE90=32.85%, MAE90=-17.86%, MFE180=121.36%.
- **삼성중공업 / 010140**: Stage2-Actionable was enough; Green should wait for more revision confirmation. MFE90=50.79%, MAE90=-3.91%, MFE180=122.76%.
- **HD현대미포 / 010620**: Eventual MFE was strong, but -22% MAE means forecasted swing should not jump straight to Yellow/Green. MFE90=59.78%, MAE90=-22.45%, MFE180=72.64%.
- **한화오션 / 042660**: A single quarterly loss should be 4B/watch before hard 4C if backlog repair remains alive. MFE90=32.63%, MAE90=-17.93%, MFE180=181.74%.

## 12. Trigger-Level OHLC Backtest Tables
|case|symbol|trigger_type|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|role|verdict|
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
|C01-R1-L125-HDKSOE-20241213|009540|Stage3-Yellow|2024-12-13|210,000|19.76|-3.57|30.95|-11.57|108.57|-11.57|positive|current_profile_missed_structural|
|C01-R1-L125-HHI-20250424|329180|Stage3-Yellow|2025-04-24|376,000|21.41|-3.99|42.29|-3.99|73.4|-3.99|positive|current_profile_too_late|
|C01-R1-L125-HANWHAENGINE-20250214|082740|Stage3-Yellow|2025-02-14|24,350|18.07|-16.02|32.85|-17.86|121.36|-17.86|positive|current_profile_missed_structural|
|C01-R1-L125-SHI-20250424|010140|Stage2-Actionable|2025-04-24|14,590|20.08|-3.91|50.79|-3.91|122.76|-3.91|positive|current_profile_correct|
|C01-R1-L125-MIPO-20250117|010620|Stage2-Actionable|2025-01-17|128,300|12.47|-18.86|59.78|-22.45|72.64|-22.45|counterexample|current_profile_false_positive|
|C01-R1-L125-HANWHAOCEAN-20240726|042660|Stage4C|2024-07-26|30,950|14.05|-17.93|32.63|-17.93|181.74|-17.93|counterexample|current_profile_4C_too_early|


## 13. Current Calibrated Profile Stress Test
|case|current profile verdict|actual path|residual error|
|---|---|---|---|
|C01-R1-L125-HDKSOE-20241213|current_profile_missed_structural|MFE90 30.95 / MAE90 -11.57 / MFE180 108.57|Backlog quality plus mix/productivity bridge came before the large 180D rerating.|
|C01-R1-L125-HHI-20250424|current_profile_too_late|MFE90 42.29 / MAE90 -3.99 / MFE180 73.4|Confirmed earnings bridge converted backlog into margin visibility.|
|C01-R1-L125-HANWHAENGINE-20250214|current_profile_missed_structural|MFE90 32.85 / MAE90 -17.86 / MFE180 121.36|Engine supplier rerating appeared when old low-margin backlog rolled off.|
|C01-R1-L125-SHI-20250424|current_profile_correct|MFE90 50.79 / MAE90 -3.91 / MFE180 122.76|Stage2-Actionable was enough; Green should wait for more revision confirmation.|
|C01-R1-L125-MIPO-20250117|current_profile_false_positive|MFE90 59.78 / MAE90 -22.45 / MFE180 72.64|Eventual MFE was strong, but -22% MAE means forecasted swing should not jump straight to Yellow/Green.|
|C01-R1-L125-HANWHAOCEAN-20240726|current_profile_4C_too_early|MFE90 32.63 / MAE90 -17.93 / MFE180 181.74|A single quarterly loss should be 4B/watch before hard 4C if backlog repair remains alive.|

## 14. Stage2 / Yellow / Green Comparison
Stage2 is backlog visibility. Stage2-Actionable requires backlog quality, customer/order route, or early revision. Stage3-Yellow requires visible margin bridge through high-priced delivery mix, productivity, FX, low-margin backlog roll-off, or operating-profit confirmation. Stage3-Green is not proposed here; Green should wait for FCF/revision confirmation, not backlog scale alone. `green_lateness_ratio = not_applicable` because no matched Stage2→Green pair is emitted.

## 15. 4B Local vs Full-window Timing Audit
No representative Stage4B trigger is emitted. The C01-specific lesson is from the 4C false-break row: Hanwha Ocean Q2 loss should have been routed first to Stage4B/thesis-break watch rather than hard 4C. C01 backlog cycles can absorb one weak quarter if orderbook quality and high-value delivery remain intact.

## 16. 4C Protection Audit
|case|trigger_type|4C label|MFE_180D_pct|MAE_180D_pct|verdict|
|---|---|---|---:|---:|---|
|C01-R1-L125-HANWHAOCEAN-20240726|Stage4C|false_break|181.74|-17.93|hard 4C too early; use 4B/watch until persistent contract/order/margin break|

## 17. Sector-Specific Rule Candidate
```text
rule_scope = sector_specific
sector_specific_rule_candidate = L1_ORDER_BACKLOG_MARGIN_TO_FCF_BRIDGE_GATE
hypothesis = L1 backlog-heavy industrials should treat backlog as an inventory pipeline: Stage2 for backlog visibility, Actionable/Yellow only when delivery mix/productivity/margin/FCF bridge appears.
confidence = medium
production_scoring_changed = false
shadow_weight_only = true
```

## 18. Canonical-Archetype Rule Candidate
```text
canonical_archetype_rule_candidate = C01_BACKLOG_QUALITY_MARGIN_FCF_GATE
rule_scope = canonical_archetype_specific
positive_gate = require at least two of: delivery schedule, high-priced order recognition, low-margin backlog roll-off, margin bridge, confirmed operating profit revision, FCF/cash conversion.
counterexample_guard = forecasted profit swing or one-quarter loss alone cannot force Yellow/Green or hard 4C.
```

## 19. Before / After Backtest Comparison
|profile_id|scope|hypothesis|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global_current|global bridge gates applied but C01 rhythm still generic|6|41.55|-12.95|113.41|-12.95|0.33|2|1|mixed|
|P0b_e2r_2_0_baseline_reference|rollback_reference|older baseline over-promotes backlog headlines|6|41.55|-12.95|113.41|-12.95|0.50|3|1|worse|
|P1_L1_sector_candidate|sector_specific|industrial backlog needs delivery/mix/margin bridge before Yellow|6|41.55|-12.95|113.41|-12.95|0.17|1|1|better|
|P2_C01_canonical_candidate|canonical_archetype_specific|backlog-quality decay and margin/FCF bridge gate|6|41.55|-12.95|113.41|-12.95|0.17|1|0|best|
|P3_C01_counterexample_guard|guardrail|turnaround forecast/one-quarter loss remains watch until follow-up margin evidence|6|41.55|-12.95|113.41|-12.95|0.17|1|0|prevents false promotion/false 4C|

## 20. Score-Return Alignment Matrix
|case|role|MFE90|MAE90|alignment|
|---|---|---:|---:|---|
|C01-R1-L125-HDKSOE-20241213|positive|30.95|-11.57|aligned|
|C01-R1-L125-HHI-20250424|positive|42.29|-3.99|aligned|
|C01-R1-L125-HANWHAENGINE-20250214|positive|32.85|-17.86|aligned|
|C01-R1-L125-SHI-20250424|positive|50.79|-3.91|aligned|
|C01-R1-L125-MIPO-20250117|counterexample|59.78|-22.45|guardrail_required|
|C01-R1-L125-HANWHAOCEAN-20240726|counterexample|32.63|-17.93|guardrail_required|

## 21. Coverage Matrix
|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
|L1_INDUSTRIALS_INFRA_DEFENSE_GRID|C01_ORDER_BACKLOG_MARGIN_BRIDGE|SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK|4|2|0|1|6|0|6|6|5|L1_ORDER_BACKLOG_MARGIN_TO_FCF_BRIDGE_GATE|C01_BACKLOG_QUALITY_MARGIN_FCF_GATE|5 to 30-row floor if accepted|

## 22. Residual Contribution Summary
```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: current_profile_missed_structural, current_profile_false_positive, current_profile_too_late, current_profile_4C_too_early, high_mae_after_turnaround_forecast
new_axis_proposed: C01_BACKLOG_QUALITY_MARGIN_FCF_GATE
existing_axis_strengthened: stage2_required_bridge; full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c only for single-quarter C01 margin miss without persistent backlog/order break
existing_axis_kept: price_only_blowoff_blocks_positive_stage; stage3_green_revision_min
sector_specific_rule_candidate: L1_ORDER_BACKLOG_MARGIN_TO_FCF_BRIDGE_GATE
canonical_archetype_rule_candidate: C01_BACKLOG_QUALITY_MARGIN_FCF_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope
Validation scope: six historical trigger rows with stock-web tradable OHLC and complete 30D/90D/180D MFE/MAE for C01 shipbuilding/marine-engine backlog bridge. Non-validation scope: no live scan, no investment recommendation, no stock_agent code patch, no production scoring change, no global delta.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C01_margin_bridge_required_for_yellow,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"Backlog/orderbook headline should not become Yellow unless delivery/mix/productivity/margin bridge is visible","Separates HDKSOE/HHI/HanwhaEngine positives from Mipo/HanwhaOcean high-MAE guardrails","C01-R1-L125-009540-2024-12-13-Stage3Yellow|C01-R1-L125-329180-2025-04-24-Stage3Yellow|C01-R1-L125-082740-2025-02-14-Stage3Yellow|C01-R1-L125-010140-2025-04-24-Stage2Actionable|C01-R1-L125-010620-2025-01-17-Stage2Actionable|C01-R1-L125-042660-2024-07-26-Stage4C",6,6,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C01_single_quarter_loss_routes_to_4B_before_4C,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"One quarterly loss is 4B/thesis-break watch unless persistent order/cancel/accounting break appears","Prevents HanwhaOcean 2024 hard-4C false break","C01-R1-L125-042660-2024-07-26-Stage4C",6,6,2,low,canonical_shadow_only,"weakens over-eager hard 4C only in C01"
```

## 25. Machine-Readable Rows
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C01-R1-L125-HDKSOE-20241213","symbol":"009540","company_name":"HD한국조선해양","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C01-R1-L125-009540-2024-12-13-Stage3Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Backlog quality plus mix/productivity bridge came before the large 180D rerating."}
{"row_type":"case","case_id":"C01-R1-L125-HHI-20250424","symbol":"329180","company_name":"HD현대중공업","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C01-R1-L125-329180-2025-04-24-Stage3Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Confirmed earnings bridge converted backlog into margin visibility."}
{"row_type":"case","case_id":"C01-R1-L125-HANWHAENGINE-20250214","symbol":"082740","company_name":"한화엔진","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C01-R1-L125-082740-2025-02-14-Stage3Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Engine supplier rerating appeared when old low-margin backlog rolled off."}
{"row_type":"case","case_id":"C01-R1-L125-SHI-20250424","symbol":"010140","company_name":"삼성중공업","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C01-R1-L125-010140-2025-04-24-Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2-Actionable was enough; Green should wait for more revision confirmation."}
{"row_type":"case","case_id":"C01-R1-L125-MIPO-20250117","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","case_type":"high_mae_success_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C01-R1-L125-010620-2025-01-17-Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Eventual MFE was strong, but -22% MAE means forecasted swing should not jump straight to Yellow/Green."}
{"row_type":"case","case_id":"C01-R1-L125-HANWHAOCEAN-20240726","symbol":"042660","company_name":"한화오션","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","case_type":"4c_too_early_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C01-R1-L125-042660-2024-07-26-Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae_guardrail","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"A single quarterly loss should be 4B/watch before hard 4C if backlog repair remains alive."}
{"row_type":"trigger","trigger_id":"C01-R1-L125-009540-2024-12-13-Stage3Yellow","case_id":"C01-R1-L125-HDKSOE-20241213","symbol":"009540","company_name":"HD한국조선해양","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","sector":"shipbuilding_holdco_backlog_mix","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-12-13","entry_date":"2024-12-13","entry_price":210000,"evidence_available_at_that_date":"Value-up backlog/margin target and later 1Q25 productivity/product-mix operating-profit bridge.","evidence_source":"https://www.hd-ksoe.com/data/HDKSOE%20Value-up_EN_241213_1.pdf | https://www.hd-ksoe.com/data/25.1Q_KSOE%20Consolidated%20Earnings%20Release_fn.pdf","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009540/2024.csv","profile_path":"atlas/symbol_profiles/009/009540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.76,"MFE_90D_pct":30.95,"MFE_180D_pct":108.57,"MFE_1Y_pct":135.48,"MFE_2Y_pct":null,"MAE_30D_pct":-3.57,"MAE_90D_pct":-11.57,"MAE_180D_pct":-11.57,"MAE_1Y_pct":-11.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-09-05","peak_price":438000,"drawdown_after_peak_pct":-7.53,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"backlog_margin_bridge_structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1_L125_009540_20241213","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01-R1-L125-329180-2025-04-24-Stage3Yellow","case_id":"C01-R1-L125-HHI-20250424","symbol":"329180","company_name":"HD현대중공업","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","sector":"large_shipbuilder_high_priced_vessel_mix","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2025-04-24","entry_date":"2025-04-24","entry_price":376000,"evidence_available_at_that_date":"1Q25 revenue/operating income surge and group release citing FX, productivity, product mix and high-priced ship recognition.","evidence_source":"https://en.yna.co.kr/view/AEN20250424007700320 | https://www.hd-ksoe.com/data/25.1Q_KSOE%20Consolidated%20Earnings%20Release_fn.pdf","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/329/329180/2025.csv","profile_path":"atlas/symbol_profiles/329/329180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.41,"MFE_90D_pct":42.29,"MFE_180D_pct":73.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.99,"MAE_90D_pct":-3.99,"MAE_180D_pct":-3.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2026-01-20","peak_price":652000,"drawdown_after_peak_pct":-3.68,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"earnings_margin_bridge_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1_L125_329180_20250424","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01-R1-L125-082740-2025-02-14-Stage3Yellow","case_id":"C01-R1-L125-HANWHAENGINE-20250214","symbol":"082740","company_name":"한화엔진","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","sector":"marine_engine_backlog_margin_mix","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2025-02-14","entry_date":"2025-02-14","entry_price":24350,"evidence_available_at_that_date":"FY24 results described low-margin order roll-off, normal-profit order delivery, high-margin AM growth and DF-engine order quality.","evidence_source":"https://www.hanwha-engine.com/attach/download/1255184f-68f8-40aa-942c-8e0e50264cbf","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/082/082740/2025.csv","profile_path":"atlas/symbol_profiles/082/082740.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.07,"MFE_90D_pct":32.85,"MFE_180D_pct":121.36,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.02,"MAE_90D_pct":-17.86,"MAE_180D_pct":-17.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-03","peak_price":53900,"drawdown_after_peak_pct":-22.91,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"low_margin_backlog_purge_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1_L125_082740_20250214","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01-R1-L125-010140-2025-04-24-Stage2Actionable","case_id":"C01-R1-L125-SHI-20250424","symbol":"010140","company_name":"삼성중공업","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","sector":"shipbuilder_lng_offshore_orders_margin_target","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-24","entry_date":"2025-04-24","entry_price":14590,"evidence_available_at_that_date":"Q1 2025 order/target evidence and FY24 high-value LNG carrier operating profit context.","evidence_source":"https://en.yna.co.kr/view/AEN20250424009851320 | https://www.imarinenews.com/20846.html","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010140/2025.csv","profile_path":"atlas/symbol_profiles/010/010140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.08,"MFE_90D_pct":50.79,"MFE_180D_pct":122.76,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.91,"MAE_90D_pct":-3.91,"MAE_180D_pct":-3.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-30","peak_price":32500,"drawdown_after_peak_pct":-27.08,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"order_target_margin_bridge_positive_but_not_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1_L125_010140_20250424","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01-R1-L125-010620-2025-01-17-Stage2Actionable","case_id":"C01-R1-L125-MIPO-20250117","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","sector":"mid_sized_shipbuilder_turnaround_margin_bridge","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-17","entry_date":"2025-01-17","entry_price":128300,"evidence_available_at_that_date":"Mirae expected 4Q24 revenue W1.46tr and OP W63.4bn swing to profit, with efficiency/cost savings bridge.","evidence_source":"https://securities.miraeasset.com/bbs/download/2133913.pdf?attachmentId=2133913","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","backlog_or_delivery_visibility"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010620/2025.csv","profile_path":"atlas/symbol_profiles/010/010620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.47,"MFE_90D_pct":59.78,"MFE_180D_pct":72.64,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.86,"MAE_90D_pct":-22.45,"MAE_180D_pct":-22.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-31","peak_price":221500,"drawdown_after_peak_pct":-20.77,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_positive_but_yellow_too_early_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1_L125_010620_20250117","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C01-R1-L125-042660-2024-07-26-Stage4C","case_id":"C01-R1-L125-HANWHAOCEAN-20240726","symbol":"042660","company_name":"한화오션","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_TO_MARGIN_FCF_BRIDGE_VS_HEADLINE_ORDERBOOK","sector":"shipbuilder_op_loss_backlog_thesis_break_watch","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|4C_thesis_break_timing_test|sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":30950,"evidence_available_at_that_date":"Q2 operating loss around KRW 9.6/9.7bn despite higher sales; H1 context still showed broader recovery versus prior year.","evidence_source":"https://www.asiae.co.kr/en/article/2024072614321195934 | https://en.yna.co.kr/view/AEN20240726005551320","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","execution_risk_score"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv","profile_path":"atlas/symbol_profiles/042/042660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.05,"MFE_90D_pct":32.63,"MFE_180D_pct":181.74,"MFE_1Y_pct":285.78,"MFE_2Y_pct":null,"MAE_30D_pct":-17.93,"MAE_90D_pct":-17.93,"MAE_180D_pct":-17.93,"MAE_1Y_pct":-17.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-04","peak_price":87200,"drawdown_after_peak_pct":-28.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"hard_4c_too_early_use_4b_watch_first","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score"],"four_c_protection_label":"false_break","trigger_outcome_label":"hard_4c_too_early_after_single_quarter_loss","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_R1_L125_042660_20240726","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01-R1-L125-HDKSOE-20241213","trigger_id":"C01-R1-L125-009540-2024-12-13-Stage3Yellow","symbol":"009540","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":78,"margin_bridge_score":55,"revision_score":55,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":42,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":84,"margin_bridge_score":74,"revision_score":66,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":34,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Backlog quality plus mix/productivity bridge came before the large 180D rerating.","MFE_90D_pct":30.95,"MAE_90D_pct":-11.57,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01-R1-L125-HHI-20250424","trigger_id":"C01-R1-L125-329180-2025-04-24-Stage3Yellow","symbol":"329180","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":78,"margin_bridge_score":55,"revision_score":55,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":42,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":84,"margin_bridge_score":74,"revision_score":66,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":34,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Confirmed earnings bridge converted backlog into margin visibility.","MFE_90D_pct":42.29,"MAE_90D_pct":-3.99,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01-R1-L125-HANWHAENGINE-20250214","trigger_id":"C01-R1-L125-082740-2025-02-14-Stage3Yellow","symbol":"082740","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":78,"margin_bridge_score":55,"revision_score":55,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":42,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":84,"margin_bridge_score":74,"revision_score":66,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":34,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Engine supplier rerating appeared when old low-margin backlog rolled off.","MFE_90D_pct":32.85,"MAE_90D_pct":-17.86,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01-R1-L125-SHI-20250424","trigger_id":"C01-R1-L125-010140-2025-04-24-Stage2Actionable","symbol":"010140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":78,"margin_bridge_score":55,"revision_score":55,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":42,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":84,"margin_bridge_score":74,"revision_score":66,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":34,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Stage2-Actionable was enough; Green should wait for more revision confirmation.","MFE_90D_pct":50.79,"MAE_90D_pct":-3.91,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01-R1-L125-MIPO-20250117","trigger_id":"C01-R1-L125-010620-2025-01-17-Stage2Actionable","symbol":"010620","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":72,"margin_bridge_score":48,"revision_score":54,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":70,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":66,"margin_bridge_score":52,"revision_score":50,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":76,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":64,"stage_label_after":"Stage2-Actionable","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Eventual MFE was strong, but -22% MAE means forecasted swing should not jump straight to Yellow/Green.","MFE_90D_pct":59.78,"MAE_90D_pct":-22.45,"score_return_alignment_label":"guardrail_required","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01-R1-L125-HANWHAOCEAN-20240726","trigger_id":"C01-R1-L125-042660-2024-07-26-Stage4C","symbol":"042660","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":72,"margin_bridge_score":48,"revision_score":54,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":70,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":75,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":66,"margin_bridge_score":52,"revision_score":50,"relative_strength_score":50,"customer_quality_score":65,"policy_or_regulatory_score":25,"valuation_repricing_score":50,"execution_risk_score":76,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":64,"stage_label_after":"Stage4B","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"A single quarterly loss should be 4B/watch before hard 4C if backlog repair remains alive.","MFE_90D_pct":32.63,"MAE_90D_pct":-17.93,"score_return_alignment_label":"guardrail_required","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"residual_contribution","round":"R1","loop":"125","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive","current_profile_too_late","current_profile_4C_too_early","high_mae_after_turnaround_forecast"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C01-R1-L125-SHI-RUSSIA-CANCEL-20250618","symbol":"010140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","reason":"Large Russia icebreaker cancellation evidence exists but entry after 2025-06-18 leaves insufficient full 180D stock-web forward window by manifest max_date; use as narrative support only.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","evidence_source":"https://www.reuters.com/business/retail-consumer/samsung-heavy-says-354-billion-icebreaker-orders-russias-zvezda-cancelled-2025-06-18/"}
```

## 26. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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
- Production scoring must not change unless the user explicitly asks for another promotion batch.

## 27. Next Round State
```text
completed_round = R1
completed_loop = 125
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C01 rows 19 need_to_30 11
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C27_CONTENT_IP_GLOBAL_MONETIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
## 28. Source Notes
- Price source: Songdaiki/stock-web manifest max date `2026-02-20`, `tradable_raw`, `raw_unadjusted_marcap`.
- This artifact is historical calibration, not an investment recommendation.
- Every `row_type="trigger"` row contains six required MFE/MAE horizon fields.

## Batch Ingest Self-Audit
```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
