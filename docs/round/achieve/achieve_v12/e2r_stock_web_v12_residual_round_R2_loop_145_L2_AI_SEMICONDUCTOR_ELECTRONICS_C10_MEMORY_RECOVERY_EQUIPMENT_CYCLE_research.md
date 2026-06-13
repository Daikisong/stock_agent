# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R2
selected_loop = 145
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = mixed_c10_materials_parts_substrate_confirmed_recovery_vs_late_cycle_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
live_candidate_mode = false
```

One-line contribution: This loop adds **6** new independent C10 cases, **3** counterexamples, and **5** residual errors for **R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE**.

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_1_stock_web_calibrated`. The existing global profile already has Stage2 actionable evidence bonus, stricter Stage3 Yellow/Green, price-only blowoff block, full-4B non-price evidence requirement, and hard 4C thesis-break routing. This loop does **not** re-prove those global rules. It tests a C10-specific residual: memory recovery in equipment is not identical to memory recovery in **materials / consumables / PCB substrates / specialty gases**. These suppliers often move on run-rate, utilization, replacement, and margin bridges before or without a named equipment order.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R2`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`
- selected mapping: C06~C10 -> R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS
- invalid_round_sector_pair: false

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index baseline still marks C10 as Priority 0:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE baseline rows = 13
need_to_30 = 17
need_to_50 = 37
```

Session-aware duplicate check avoided prior C10 symbols from loop128 and loop137:

```text
previous C10 loop128 avoided = 319660, 281820, 240810, 036200, 160980
previous C10 loop137 avoided = 064760, 166090, 101160, 086390, 114810
new C10 symbols in this loop = 074600, 102710, 092070, 222800, 104830, 357780
hard_duplicate_count = 0
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
profile_path_template = atlas/symbol_profiles/<prefix>/<ticker>.json
```

All trigger rows below use actual stock-web 1D OHLCV tradable shards. No forward price beyond stock-web manifest max date was created.

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| actual stock-web 1D OHLC used | pass |
| trigger rows have MFE/MAE 30D/90D/180D six fields | pass |
| forward 180 trading rows available | pass for all 6 rows |
| corporate action candidate within entry~D180 | none detected for selected 2024~2025 windows |
| current/live candidate discovery | not performed |
| production scoring changed | false |

## 6. Canonical Archetype Compression Map

| fine leaf | canonical compression | interpretation |
|---|---|---|
| QUARTZ_CONSUMABLE_NAND_DRAM_CAPA_RESTART | C10 | consumable replacement demand after utilization/CAPA recovery |
| PROCESS_CHEMICAL_MEMORY_DEMAND_PRICE_RECOVERY | C10 | process chemical run-rate and margin bridge after memory price recovery |
| PRECURSOR_PARENT_INTEGRATION_FUTURE_PRODUCT_LADDER | C10 | future precursor product ladder; watch credit, not immediate actionable |
| SUBSTRATE_MEMORY_BOTTOM_CALL_TOO_EARLY | C10 | PCB substrate bottom-call requires realized shipment/margin bridge |
| SPECIAL_GAS_MEMORY_RECOVERY_REVENUE_MISMATCH | C10 | specialty gas OP improvement can fail if revenue/run-rate bridge is absent |
| MATERIALS_VALUATION_WITH_DELAYED_NAND_UTILIZATION | C10 | valuation attractiveness is not enough when NAND utilization is explicitly delayed |

## 7. Case Selection Summary

| case_id | symbol | company | type | trigger_date | entry_date | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|
| C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA | 074600 | 원익QnC | positive | 2025-03-05 | 2025-03-05 | 17.44 | -16.89 | 51.77 | -16.89 | current_profile_too_late_or_too_order-centric_for_consumable_recovery |
| C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY | 102710 | 이엔에프테크놀로지 | positive | 2025-03-21 | 2025-03-21 | 65.49 | -11.69 | 137.48 | -11.69 | current_profile_missed_structural_if_equipment_order_is_required |
| C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION | 092070 | 디엔에프 | positive | 2025-01-22 | 2025-01-22 | 18.05 | -20.85 | 58.84 | -20.85 | mixed_current_profile_should_watch_not_actionable |
| C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL | 222800 | 심텍 | counterexample | 2024-05-07 | 2024-05-07 | 14.79 | -47.92 | 14.79 | -70.14 | current_profile_false_positive_if_bottom_call_treated_as_actionable |
| C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH | 104830 | 원익머트리얼즈 | counterexample | 2024-05-23 | 2024-05-23 | 13.86 | -29.06 | 13.86 | -50.97 | current_profile_false_positive_if_OP_growth_without_revenue_bridge_is_overweighted |
| C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE | 357780 | 솔브레인 | counterexample | 2024-08-16 | 2024-08-16 | 0.97 | -37.78 | 0.97 | -38.01 | current_profile_false_positive_if_valuation_and_profitability_ignore_utilization_delay |


## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count = 6
calibration_usable_trigger_count = 6
representative_trigger_count = 6
positive_case_count = 3
counterexample_count = 3
4B_watch_or_overlay_count = 5
4C_watch_case_count = 3
current_profile_error_count = 5
new_independent_case_count = 6
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
```

Balance is intentionally split into three structural positives and three high-MAE / failed-rerating counterexamples. The point is not to say “memory recovery is good.” The point is to distinguish a real material run-rate bridge from a forecast-only bottom call.

## 9. Case Notes

### 9.1 원익QnC / 074600 / quartz consumable recovery positive with staged-entry guard

The KIRS report dated 2025-03-05 framed 2025 quartz demand through NAND transition demand in the first half and DRAM CAPA / NAND utilization recovery later in the year. Stock-web entry on 2025-03-05 produced MFE_180D +51.77%, but the same row also had MAE_30D -16.89%. This is a C10 positive, but the high early drawdown says the rule should be **Stage2-Actionable with staged-entry/high-MAE guard**, not Green.

### 9.2 이엔에프테크놀로지 / 102710 / confirmed process-chemical run-rate positive

The 2025-03-21 annual earnings material is the clean positive in this loop. It explicitly ties semiconductor segment improvement to AI/server demand-driven memory recovery, says memory demand and price recovery raised semiconductor revenue, and shows operating profit +140.1% YoY. Price path aligned: MFE_90D +65.49%, MFE_180D +137.48%, MAE_180D -11.69%.

### 9.3 디엔에프 / 092070 / parent integration + Hf precursor ladder, watch-only positive

The 2025-01-22 article describes Soulbrain's acquisition, DNF's Hf precursor development, and commercialization timing linked to a later patent-expiry window. Price path later produced MFE_180D +58.84%, but MAE_90D was -20.85% and near-term revenue bridge was not confirmed. This should become a C10 **watch-credit** leaf, not immediate Stage2-Actionable.

### 9.4 심텍 / 222800 / bottom-call false positive

The 2024-05-07 report argued the 1Q loss was the trough, 2Q operating profit would turn positive, and memory shipment recovery would raise PCB utilization. The price path briefly gave MFE_30D +14.79%, then collapsed to MAE_90D -47.92% and MAE_180D -70.14%. This is the strongest evidence that **forecasted bottom** is not the same as realized memory recovery.

### 9.5 원익머트리얼즈 / 104830 / special-gas OP improvement without revenue bridge

The May 2024 evidence set contained positive language around memory recovery and 1Q operating-profit improvement, but also showed revenue contraction. The stock-web path had MFE_180D only +13.86% against MAE_180D -50.97%. C10 should not over-credit margin improvement when revenue/run-rate and customer demand bridge are absent.

### 9.6 솔브레인 / 357780 / attractive valuation but delayed NAND utilization counterexample

The 2024-08-16 report said 2Q profitability beat and semiconductor materials profit was robust, but explicitly stated NAND utilization recovery was slower than expected and target price was cut. Price path was nearly flat on upside, MFE_90D +0.97%, while MAE_90D reached -37.78%. Valuation attractiveness should not unlock C10 actionable when utilization delay is written in the evidence.

## 10. Current Profile Stress Test

| tested axis | result |
|---|---|
| stage2_actionable_evidence_bonus | kept; but C10 needs material-specific bridge definitions |
| price_only_blowoff_blocks_positive_stage | kept; not the main issue here |
| full_4b_requires_non_price_evidence | strengthened for C10 via revenue decline, utilization delay, target cut, high MAE |
| hard_4c_thesis_break_routes_to_4c | kept; most rows are 4B-watch or thesis-break-watch, not immediate hard 4C |

Residual error types found:

```text
forecast_only_bottom_call_false_positive
valuation_plus_profitability_without_utilization_false_positive
margin_only_without_revenue_bridge_false_positive
materials_runrate_recovery_missed_if_equipment_order_required
future_product_ladder_should_be_watch_not_actionable
```

## 11. Proposed Shadow Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_rule_candidate = C10_CONFIRMED_RUNRATE_UTILIZATION_AND_ORDER_REVENUE_BRIDGE_V3
sector_rule_candidate = L2_MATERIALS_PARTS_RUNRATE_RECOVERY_GATE_V3
production_scoring_changed = false
shadow_weight_only = true
```

Candidate rule:

> For C10, Stage2-Actionable should require at least one confirmed bridge among named order / shipment / utilization recovery / run-rate revenue / margin-revision bridge / consumable replacement demand. Forecast-only bottom calls, valuation-only recovery, target cuts, delayed NAND utilization, revenue contraction, or future commercialization ladders stay at Stage2-Watch or 4B-Watch even when the memory-cycle vocabulary is positive.

Rule impact in this loop:

```text
kept / upgraded = 074600, 102710, 092070 watch-credit
filtered / demoted = 222800, 104830, 357780
```

## 12. Score Simulation Profile Comparison

| profile | selected triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 current proxy | 6 | 21.77 | -27.36 | 46.28 | -34.76 | mixed; false positives too costly |
| P1 sector candidate | 3 positives | 33.66 | -16.48 | 82.7 | -16.48 | better L2 material/parts filter |
| P2 C10 canonical candidate | 3 positives | 33.66 | -16.48 | 82.7 | -16.48 | best shadow-only candidate |
| P3 counterexample guard | 3 counters | 9.87 | -38.25 | 9.87 | -53.04 | blocks high-MAE false positives |

## 13. 4B / 4C Timing Audit

- 심텍, 원익머트리얼즈, 솔브레인은 full 4C보다는 4B/Stage2-Watch demotion이 먼저다. evidence had warning signs, but not all had permanent thesis destruction at trigger date.
- 디엔에프 has positive 180D MFE but lacks near-term commercialization; it should be watch-only, avoiding both false 4C and false actionable.
- 원익QnC has positive 180D MFE but a meaningful early MAE. This suggests staged-entry guard rather than Green unlock.

## 14. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | mixed_c10_materials_parts_substrate_confirmed_recovery_vs_late_cycle_leaf_set | 3 | 3 | 5 | 3 | 6 | 0 | 6 | 6 | 5 | L2_MATERIALS_PARTS_RUNRATE_RECOVERY_GATE_V3 | C10_CONFIRMED_RUNRATE_UTILIZATION_AND_ORDER_REVENUE_BRIDGE_V3 | index baseline C10 13 -> 19; session-aware after loop128+loop137+loop145 about 30 |


## 15. Machine-readable rows

### 15.1 case rows

```jsonl
{"row_type":"case","case_id":"C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","symbol":"074600","company_name":"원익QnC","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_CONSUMABLE_NAND_DRAM_CAPA_RESTART","case_type":"structural_success_with_high_mae_guard","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"confirmed_quartz_consumable_recovery_positive_but_requires_staged_entry","current_profile_verdict":"current_profile_too_late_or_too_order-centric_for_consumable_recovery","price_source":"Songdaiki/stock-web","notes":"C10 should not only wait for equipment PO. Quartz/parts demand restocking can be a valid memory recovery bridge, but early MAE requires staged-entry guard."}
{"row_type":"case","case_id":"C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","symbol":"102710","company_name":"이엔에프테크놀로지","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"PROCESS_CHEMICAL_MEMORY_DEMAND_PRICE_RECOVERY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"confirmed_materials_runrate_recovery_positive","current_profile_verdict":"current_profile_missed_structural_if_equipment_order_is_required","price_source":"Songdaiki/stock-web","notes":"Cleanest C10 positive in this loop: actual 2024 earnings bridge preceded a 90D/180D price path."}
{"row_type":"case","case_id":"C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION","symbol":"092070","company_name":"디엔에프","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"PRECURSOR_PARENT_INTEGRATION_FUTURE_PRODUCT_LADDER","case_type":"watch_positive_with_execution_lag","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"future_product_ladder_positive_price_path_but_not_near_term_actionable","current_profile_verdict":"mixed_current_profile_should_watch_not_actionable","price_source":"Songdaiki/stock-web","notes":"Price path was positive by D180, but evidence was not near-term revenue. C10 needs a watch state between zero-credit and full actionable."}
{"row_type":"case","case_id":"C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL","symbol":"222800","company_name":"심텍","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SUBSTRATE_MEMORY_BOTTOM_CALL_TOO_EARLY","case_type":"counterexample_high_mae","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"substrate_bottom_call_false_positive_high_drawdown","current_profile_verdict":"current_profile_false_positive_if_bottom_call_treated_as_actionable","price_source":"Songdaiki/stock-web","notes":"The words were right, timing was wrong. C10 must separate forecasted recovery from observed shipment/margin bridge."}
{"row_type":"case","case_id":"C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH","symbol":"104830","company_name":"원익머트리얼즈","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SPECIAL_GAS_MEMORY_RECOVERY_REVENUE_MISMATCH","case_type":"counterexample_revenue_mismatch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"special_gas_profit_rebound_did_not_convert_to_rerating","current_profile_verdict":"current_profile_false_positive_if_OP_growth_without_revenue_bridge_is_overweighted","price_source":"Songdaiki/stock-web","notes":"Operating profit recovery without sales/run-rate bridge was not enough. This is the cleanest counterexample against margin-only C10 promotion."}
{"row_type":"case","case_id":"C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE","symbol":"357780","company_name":"솔브레인","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MATERIALS_VALUATION_WITH_DELAYED_NAND_UTILIZATION","case_type":"counterexample_delayed_nand_recovery","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"attractive_valuation_but_NAND_delay_counterexample","current_profile_verdict":"current_profile_false_positive_if_valuation_and_profitability_ignore_utilization_delay","price_source":"Songdaiki/stock-web","notes":"This separates valuation attractiveness from true C10 memory recovery. NAND utilization delay should throttle Stage2-Actionable."}
```

### 15.2 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","case_id":"C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","symbol":"074600","company_name":"원익QnC","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_CONSUMABLE_NAND_DRAM_CAPA_RESTART","sector":"semiconductor_materials_parts_memory_recovery","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-03-05","evidence_available_at_that_date":"KIRS 2025-03-05 report: H1 NAND transition demand, H2 DRAM new CAPA and NAND utilization recovery can expand quartz parts demand.","evidence_source":"https://w4.kirs.or.kr/download/research/250305_%EC%9B%90%EC%9D%B5QnC%28%EA%B8%80%EC%84%B8-%EB%9D%BC%EC%9D%B4%EC%A7%95%29.pdf","stage2_evidence_fields":["quartz_consumable_demand_bridge","NAND_transition_demand","DRAM_CAPA_and_NAND_utilization_recovery","customer_fab_cycle_link"],"stage3_evidence_fields":["2025_quartz_demand_expansion_expected","replacement_demand_after_tool_install"],"stage4b_evidence_fields":["MAE30_high_before_full_180D_upside","cycle_timing_volatility"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/074/074600/2025.csv","profile_path":"atlas/symbol_profiles/074/074600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-05","entry_price":18350.0,"MFE_30D_pct":17.44,"MFE_90D_pct":17.44,"MFE_180D_pct":51.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.89,"MAE_90D_pct":-16.89,"MAE_180D_pct":-16.89,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-10","peak_price":27850.0,"drawdown_after_peak_pct":-33.39,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_watch_if_high_MAE_or_explicit_utilization_delay","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"confirmed_quartz_consumable_recovery_positive_but_requires_staged_entry","current_profile_verdict":"current_profile_too_late_or_too_order-centric_for_consumable_recovery","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|074600|2025-03-05|Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","case_id":"C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","symbol":"102710","company_name":"이엔에프테크놀로지","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"PROCESS_CHEMICAL_MEMORY_DEMAND_PRICE_RECOVERY","sector":"semiconductor_materials_parts_memory_recovery","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-03-21","evidence_available_at_that_date":"2024 annual IR: semiconductor segment improved on AI/server demand-driven memory recovery; operating profit rose 140.1% YoY; utilization and raw material stabilization improved profitability.","evidence_source":"https://file.alphasquare.co.kr/media/pdfs/company-ir/20250321%EC%9D%B4%EC%97%94%EC%97%90%ED%94%84%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80_2024%EB%85%84_%EC%97%B0%EA%B0%84_%EA%B2%BD%EC%98%81%EC%8B%A4%EC%A0%81_%EB%B0%9C%ED%91%9C.pdf","stage2_evidence_fields":["confirmed_annual_profit_recovery","memory_demand_and_price_recovery","utilization_increase","process_chemical_revenue_bridge"],"stage3_evidence_fields":["operating_margin_expansion","semiconductor_segment_growth","customer_demand_increase"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/102/102710/2025.csv","profile_path":"atlas/symbol_profiles/102/102710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-21","entry_price":26950.0,"MFE_30D_pct":3.15,"MFE_90D_pct":65.49,"MFE_180D_pct":137.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.69,"MAE_90D_pct":-11.69,"MAE_180D_pct":-11.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-10","peak_price":64000.0,"drawdown_after_peak_pct":-35.86,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"confirmed_materials_runrate_recovery_positive","current_profile_verdict":"current_profile_missed_structural_if_equipment_order_is_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|102710|2025-03-21|Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION","case_id":"C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION","symbol":"092070","company_name":"디엔에프","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"PRECURSOR_PARENT_INTEGRATION_FUTURE_PRODUCT_LADDER","sector":"semiconductor_materials_parts_memory_recovery","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2025-01-22","evidence_available_at_that_date":"The Bell 2025-01-22: Soulbrain acquired DNF, DNF has developed Hf precursor and is targeting commercialization around the TCLC patent expiry window; DNF is a precursor specialist with Samsung Electronics also a shareholder.","evidence_source":"https://www.thebell.co.kr/front/newsview.asp?key=202501221511325280108669","stage2_evidence_fields":["parent_integration","Hf_precursor_development","Samsung_shareholder_customer_context","precursor_product_ladder"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["commercialization_target_after_2026","no_near_term_runrate_confirmation","MAE90_below_minus20"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092070/2025.csv","profile_path":"atlas/symbol_profiles/092/092070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-01-22","entry_price":11080.0,"MFE_30D_pct":17.24,"MFE_90D_pct":18.05,"MFE_180D_pct":58.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.25,"MAE_90D_pct":-20.85,"MAE_180D_pct":-20.85,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-16","peak_price":17600.0,"drawdown_after_peak_pct":-12.27,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_watch_if_high_MAE_or_explicit_utilization_delay","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"future_product_ladder_positive_price_path_but_not_near_term_actionable","current_profile_verdict":"mixed_current_profile_should_watch_not_actionable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|092070|2025-01-22|Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL","case_id":"C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL","symbol":"222800","company_name":"심텍","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SUBSTRATE_MEMORY_BOTTOM_CALL_TOO_EARLY","sector":"semiconductor_materials_parts_memory_recovery","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-07","evidence_available_at_that_date":"Daishin 2024-05-07 expected 2Q24 operating profit turnaround after 1Q loss and argued memory shipment recovery would raise PCB utilization and sales.","evidence_source":"https://money2.daishin.com/PDF/Out/intranet_data/Product/ResearchCenter/Report/2024/05/49904_1Q24_Review_Simmteck_240507.pdf","stage2_evidence_fields":["bottom_call","2Q24_turnaround_forecast","memory_shipment_recovery_expectation","DDR5_server_PCB_qoq_growth"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["MFE_capped_at_14_79","MAE90_minus47_92","MAE180_minus70_14","bottom_call_without_realized_margin_bridge"],"stage4c_evidence_fields":["thesis_break_if_turnaround_not_realized_within_90D"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv","profile_path":"atlas/symbol_profiles/222/222800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-07","entry_price":32450.0,"MFE_30D_pct":14.79,"MFE_90D_pct":14.79,"MFE_180D_pct":14.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.01,"MAE_90D_pct":-47.92,"MAE_180D_pct":-70.14,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":37250.0,"drawdown_after_peak_pct":-73.99,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_watch_if_high_MAE_or_explicit_utilization_delay","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"substrate_bottom_call_false_positive_high_drawdown","current_profile_verdict":"current_profile_false_positive_if_bottom_call_treated_as_actionable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|222800|2024-05-07|Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH","case_id":"C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH","symbol":"104830","company_name":"원익머트리얼즈","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SPECIAL_GAS_MEMORY_RECOVERY_REVENUE_MISMATCH","sector":"semiconductor_materials_parts_memory_recovery","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-23","evidence_available_at_that_date":"KIRS 2024-05-23 described Wonik Materials as a semiconductor/display process specialty-gas leader. Contemporaneous news noted 1Q24 OP +30.57% YoY but revenue -43.33% YoY, and prior DB view expected profitability improvement from memory recovery.","evidence_source":"https://w4.kirs.or.kr/download/research/240523_%ED%99%94%ED%95%99_%EC%9B%90%EC%9D%B5%EB%A8%B8%ED%8A%B8%EB%A6%AC%EC%96%BC%EC%A6%88%28104830%29_%EB%B0%98%EB%8F%84%EC%B2%B4%20%EA%B3%B5%EC%A0%95%EC%9A%A9%20%ED%8A%B9%EC%88%98%EA%B0%80%EC%8A%A4%20%EB%B6%84%EC%95%BC%20%EC%84%A0%EB%8F%84%EA%B8%B0%EC%97%85_%EB%82%98%EC%9D%B4%EC%8A%A4%EB%94%94%EC%95%A4%EB%B9%84.pdf","stage2_evidence_fields":["special_gas_leader","1Q_operating_profit_growth","memory_recovery_profitability_expectation"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["revenue_down_43pct_YoY","MFE90_only_13_86","MAE180_minus50_97","customer_concentration_recovery_gap"],"stage4c_evidence_fields":["if_revenue_bridge_absent_after_90D"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/104/104830/2024.csv","profile_path":"atlas/symbol_profiles/104/104830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-23","entry_price":33550.0,"MFE_30D_pct":13.86,"MFE_90D_pct":13.86,"MFE_180D_pct":13.86,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.0,"MAE_90D_pct":-29.06,"MAE_180D_pct":-50.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":38200.0,"drawdown_after_peak_pct":-56.94,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_watch_if_high_MAE_or_explicit_utilization_delay","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"special_gas_profit_rebound_did_not_convert_to_rerating","current_profile_verdict":"current_profile_false_positive_if_OP_growth_without_revenue_bridge_is_overweighted","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|104830|2024-05-23|Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE","case_id":"C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE","symbol":"357780","company_name":"솔브레인","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MATERIALS_VALUATION_WITH_DELAYED_NAND_UTILIZATION","sector":"semiconductor_materials_parts_memory_recovery","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-16","evidence_available_at_that_date":"Samsung Securities 2024-08-16: 2Q profitability beat, semiconductor materials earnings robust, but NAND utilization recovery was slower than expected; buy kept with target cut.","evidence_source":"https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024081607093286K_02_03.pdf&inlineYn=Y&saveKey=research.pdf","stage2_evidence_fields":["profitability_beat","semiconductor_materials_profit_resilience","valuation_attractiveness"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_slow_NAND_recovery","target_price_cut","MFE90_below_1pct","MAE90_minus37_78"],"stage4c_evidence_fields":["thesis_break_watch_if_NAND_recovery_lags"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/357/357780/2024.csv","profile_path":"atlas/symbol_profiles/357/357780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-16","entry_price":256500.0,"MFE_30D_pct":0.97,"MFE_90D_pct":0.97,"MFE_180D_pct":0.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.91,"MAE_90D_pct":-37.78,"MAE_180D_pct":-38.01,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-20","peak_price":259000.0,"drawdown_after_peak_pct":-38.61,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_watch_if_high_MAE_or_explicit_utilization_delay","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"attractive_valuation_but_NAND_delay_counterexample","current_profile_verdict":"current_profile_false_positive_if_valuation_and_profitability_ignore_utilization_delay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|357780|2024-08-16|Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 15.3 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","trigger_id":"TRG_C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","symbol":"074600","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":50,"revision_score":45,"relative_strength_score":48,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":60,"revision_score":45,"relative_strength_score":48,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["utilization_score","consumable_replacement_score","margin_bridge_score"],"component_delta_explanation":"C10 candidate adds consumable restocking/replacement demand bridge, not just named equipment order.","MFE_90D_pct":17.44,"MAE_90D_pct":-16.89,"score_return_alignment_label":"confirmed_quartz_consumable_recovery_positive_but_requires_staged_entry","current_profile_verdict":"current_profile_too_late_or_too_order-centric_for_consumable_recovery"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","trigger_id":"TRG_C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","symbol":"102710","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":20,"margin_bridge_score":65,"revision_score":55,"relative_strength_score":45,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":20,"margin_bridge_score":75,"revision_score":55,"relative_strength_score":45,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable","changed_components":["runrate_recovery_score","utilization_score","margin_bridge_score"],"component_delta_explanation":"Confirmed utilization and margin bridge should unlock C10 even without a signed tool order.","MFE_90D_pct":65.49,"MAE_90D_pct":-11.69,"score_return_alignment_label":"confirmed_materials_runrate_recovery_positive","current_profile_verdict":"current_profile_missed_structural_if_equipment_order_is_required"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION","trigger_id":"TRG_C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION","symbol":"092070","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":35,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage1/Stage2-Watch","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":35,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":50,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Watch","changed_components":["future_product_ladder_score","customer_quality_score","execution_risk_guard"],"component_delta_explanation":"Parent/customer/product ladder deserves watch credit but execution lag prevents Stage2-Actionable.","MFE_90D_pct":18.05,"MAE_90D_pct":-20.85,"score_return_alignment_label":"future_product_ladder_positive_price_path_but_not_near_term_actionable","current_profile_verdict":"mixed_current_profile_should_watch_not_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL","trigger_id":"TRG_C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL","symbol":"222800","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":15,"margin_bridge_score":35,"revision_score":40,"relative_strength_score":55,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":60,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":15,"margin_bridge_score":20,"revision_score":40,"relative_strength_score":55,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-Watch/4B-Watch","changed_components":["forecast_only_penalty","realized_margin_bridge_required","high_mae_guard"],"component_delta_explanation":"Forecasted turnaround without confirmed revenue/margin bridge should not be actionable; high MAE validates guard.","MFE_90D_pct":14.79,"MAE_90D_pct":-47.92,"score_return_alignment_label":"substrate_bottom_call_false_positive_high_drawdown","current_profile_verdict":"current_profile_false_positive_if_bottom_call_treated_as_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH","trigger_id":"TRG_C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH","symbol":"104830","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":55,"revision_score":40,"relative_strength_score":45,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":50,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":40,"revision_score":40,"relative_strength_score":45,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-Watch/4B-Watch","changed_components":["revenue_bridge_required","runrate_confirmation_required","customer_concentration_risk"],"component_delta_explanation":"Margin-only improvement is cut unless revenue/run-rate/customer bridge confirms actual cycle recovery.","MFE_90D_pct":13.86,"MAE_90D_pct":-29.06,"score_return_alignment_label":"special_gas_profit_rebound_did_not_convert_to_rerating","current_profile_verdict":"current_profile_false_positive_if_OP_growth_without_revenue_bridge_is_overweighted"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE","trigger_id":"TRG_C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE","symbol":"357780","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":55,"revision_score":30,"relative_strength_score":25,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":40,"revision_score":30,"relative_strength_score":25,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-Watch/4B-Watch","changed_components":["utilization_delay_penalty","valuation_only_cut","target_cut_guard"],"component_delta_explanation":"Explicit delayed NAND utilization and target cut should override valuation attractiveness.","MFE_90D_pct":0.97,"MAE_90D_pct":-37.78,"score_return_alignment_label":"attractive_valuation_but_NAND_delay_counterexample","current_profile_verdict":"current_profile_false_positive_if_valuation_and_profitability_ignore_utilization_delay"}
```

### 15.4 aggregate / shadow_weight / residual rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"aggregate_profile","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"Generic C10 memory recovery credit without material-specific run-rate guard","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":6,"selected_entry_trigger_per_case":["C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION","C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL","C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH","C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE"],"avg_MFE_90D_pct":21.77,"avg_MAE_90D_pct":-27.36,"avg_MFE_180D_pct":46.28,"avg_MAE_180D_pct":-34.76,"false_positive_rate":0.5,"missed_structural_count":2,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"mixed; high false positives from forecast-only/valuation-only triggers"}
{"row_type":"aggregate_profile","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Older broad memory-cycle vocabulary gives too much credit to bottom calls","changed_axes":["none_reference"],"changed_thresholds":{},"eligible_trigger_count":6,"selected_entry_trigger_per_case":["C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION","C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL","C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH","C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE"],"avg_MFE_90D_pct":21.77,"avg_MAE_90D_pct":-27.36,"avg_MFE_180D_pct":46.28,"avg_MAE_180D_pct":-34.76,"false_positive_rate":0.5,"missed_structural_count":3,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"worse due to bottom-call false positives"}
{"row_type":"aggregate_profile","profile_id":"P1_L2_materials_parts_recovery_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 materials/parts get early credit only with utilization/run-rate/profit bridge","changed_axes":["utilization_runrate_bridge_required","forecast_only_penalty"],"changed_thresholds":{"Stage2_Actionable_materials_bridge_min":2},"eligible_trigger_count":6,"selected_entry_trigger_per_case":["C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION"],"avg_MFE_90D_pct":33.66,"avg_MAE_90D_pct":-16.48,"avg_MFE_180D_pct":82.7,"avg_MAE_180D_pct":-16.48,"false_positive_rate":0.0,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"better: filters three large-MAE false positives while keeping material recovery winners"}
{"row_type":"aggregate_profile","profile_id":"P2_C10_material_recovery_canonical_candidate","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C10 accepts consumable/material run-rate bridges but blocks bottom-call/valuation-only triggers","changed_axes":["C10_CONFIRMED_RUNRATE_UTILIZATION_AND_ORDER_REVENUE_BRIDGE_V3"],"changed_thresholds":{"forecast_only_to_actionable_block":true,"explicit_utilization_delay_guard":true,"consumable_replacement_bridge_credit":true},"eligible_trigger_count":6,"selected_entry_trigger_per_case":["C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA","C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY","C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION"],"avg_MFE_90D_pct":33.66,"avg_MAE_90D_pct":-16.48,"avg_MFE_180D_pct":82.7,"avg_MAE_180D_pct":-16.48,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"best candidate for shadow-only C10 refinement"}
{"row_type":"aggregate_profile","profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"If evidence says slow NAND recovery, revenue decline, forecast-only turnaround, or target cut, keep Stage2-Watch/4B-Watch","changed_axes":["high_mae_guard","utilization_delay_penalty","revenue_bridge_required"],"changed_thresholds":{"MAE90_below_minus20_demotes_actionable":true},"eligible_trigger_count":6,"selected_entry_trigger_per_case":["C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL","C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH","C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE"],"avg_MFE_90D_pct":9.87,"avg_MAE_90D_pct":-38.25,"avg_MFE_180D_pct":9.87,"avg_MAE_180D_pct":-53.04,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"blocks false positives with extreme 90D/180D MAE"}
{"row_type":"shadow_weight","axis":"C10_CONFIRMED_RUNRATE_UTILIZATION_AND_ORDER_REVENUE_BRIDGE_V3","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","baseline_value":0,"tested_value":1,"delta":"+1 shadow-only","reason":"C10 materials/parts/substrate recovery needs confirmed run-rate/utilization/revenue/margin bridge; forecast-only or valuation-only triggers caused large MAE.","backtest_effect":"keeps 3 positives with avg MFE180 >80 while filtering 3 high-drawdown false positives","trigger_ids":"TRG_C10L145_074600_20250305_QNC_QUARTZ_NAND_DRAM_CAPA|TRG_C10L145_102710_20250321_ENF_CONFIRMED_MEMORY_RECOVERY|TRG_C10L145_092070_20250122_DNF_PRECURSOR_PARENT_INTEGRATION|TRG_C10L145_222800_20240507_SIMMTECH_BOTTOM_CALL_FAIL|TRG_C10L145_104830_20240523_WONIK_MATERIALS_RECOVERY_MISMATCH|TRG_C10L145_357780_20240816_SOULBRAIN_NAND_DELAY_FALSE_POSITIVE","calibration_usable_count":6,"new_independent_case_count":6,"counterexample_count":3,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual research only"}
{"row_type":"residual_contribution","round":"R2","loop":145,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["forecast_only_bottom_call_false_positive","valuation_plus_profitability_without_utilization_false_positive","margin_only_without_revenue_bridge_false_positive","materials_runrate_recovery_missed_if_equipment_order_required"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 16. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 6
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: forecast_only_bottom_call_false_positive|valuation_plus_profitability_without_utilization_false_positive|margin_only_without_revenue_bridge_false_positive|materials_runrate_recovery_missed_if_equipment_order_required|future_product_ladder_should_be_watch_not_actionable
new_axis_proposed: C10_CONFIRMED_RUNRATE_UTILIZATION_AND_ORDER_REVENUE_BRIDGE_V3
existing_axis_strengthened: full_4b_requires_non_price_evidence|stage2_actionable_evidence_bonus_scope_definition_for_C10
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage|hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_MATERIALS_PARTS_RUNRATE_RECOVERY_GATE_V3
canonical_archetype_rule_candidate: C10_CONFIRMED_RUNRATE_UTILIZATION_AND_ORDER_REVENUE_BRIDGE_V3
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 17. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during the research session.

When running the later coding-agent batch, ingest this MD as a V12 result file. Validate that all trigger rows contain canonical MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct. Use the trigger rows only if calibration_usable=true and aggregate_group_role=representative.

Candidate patch is shadow-only unless enough follow-up C10 rows confirm it:
- scope: canonical_archetype_specific
- canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- candidate_axis: C10_CONFIRMED_RUNRATE_UTILIZATION_AND_ORDER_REVENUE_BRIDGE_V3
- expected behavior: accept materials/consumables/process chemical/substrate recovery only when run-rate, utilization, revenue, margin, or replacement-demand bridge is confirmed; demote forecast-only bottom calls, valuation-only recovery, explicit utilization delay, target cut, or revenue mismatch.

Do not change production scoring directly from this single MD. Add it to the batch evidence set and compare against existing v12 aggregate metrics.
```

## 18. Next Research State

```text
completed_round = R2
completed_loop = 145
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
coverage_after_if_accepted_index_baseline = C10 rows 13 -> 19
session_aware_after_loop128_loop137_loop145_if_accepted = about C10 rows 30
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY|C11_BATTERY_ORDERBOOK_RERATING|C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|C14_EV_DEMAND_SLOWDOWN_4B_4C|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
