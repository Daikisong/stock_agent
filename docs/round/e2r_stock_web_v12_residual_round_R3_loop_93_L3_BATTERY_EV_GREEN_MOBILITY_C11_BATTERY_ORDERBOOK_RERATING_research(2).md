# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round: R3
selected_loop: 93
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: COPPER_FOIL_ORDERBOOK_CUSTOMER_CAPA_RERATING_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent C11 rows and moves C11 from static 23 rows to local projected 26 rows after loop80, then to projected 29 rows after this loop.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C11:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C11 -> C11_BATTERY_ORDERBOOK_RERATING
```

C11 is the battery orderbook rerating archetype. The orderbook is the invitation. The calibration question is whether customer volume, revenue conversion, margin bridge, revision, and FCF show up after the invitation.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C11 rows | 23 |
| static C11 symbols | 16 |
| static C11 good/bad Stage2 | 7 / 5 |
| static C11 4B/4C | 3 / 4 |
| static C11 URL pending/proxy | 23 / 15 |
| static top covered symbols | 006110, 382840, 008730, 078600, 290670, 020150 |
| local C11 loop 80 projected rows | 26 |
| this loop projected rows | 29 |

Selected symbols avoid the static C11 top-covered symbols and local loop80 C11 symbols `348370`, `078600`, and `003670`.

| symbol | company | status |
|---|---|---|
| 011790 | SKC | new C11 symbol versus static top-covered and local C11 loop |
| 336370 | 솔루스첨단소재 | new C11 symbol versus static top-covered and local C11 loop |
| 222080 | 씨아이에스 | new C11 symbol versus static top-covered and local C11 loop |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated loop memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 011790 / 2024-03-05 | true | true | clean_180D_window | true |
| 336370 / 2024-03-27 | true | true | clean_180D_window | true |
| 222080 / 2024-03-05 | true | true | clean_180D_window | true |

Corporate-action notes:

- SKC has corporate-action candidates only in 1998 and 2001; selected 2024 window is clean.
- 솔루스첨단소재 has corporate-action candidates in 2024-01, but selected entry is 2024-03-27, so the selected forward window is clean.
- 씨아이에스 has a corporate-action candidate in 2017 only; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| COPPER_FOIL_ORDERBOOK_CUSTOMER_CAPA_RERATING_4B_WATCH | C11 | customer/CAPA orderbook rerating can work, but margin/FCF conversion must follow |
| COPPER_FOIL_ORDERBOOK_RELIEF_RERATING_4B_HIGH_MAE | C11 | relief rerating can create MFE, but high MAE demands utilization/cash bridge |
| BATTERY_EQUIPMENT_ORDERBOOK_SPIKE_MARGIN_BRIDGE_FAIL | C11 | equipment/orderbook spike without margin/revision bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C11_SKC_011790_2024_03_05_COPPER_FOIL_ORDERBOOK_RERATING_4B | 011790 | SKC | 4B_overlay_success | positive | orderbook/CAPA rerating captured >100% MFE and then needed 4B audit |
| C11_SOLUS_336370_2024_03_27_COPPER_FOIL_ORDERBOOK_RERATING_HIGH_DRAWDOWN | 336370 | 솔루스첨단소재 | 4B_overlay_success | positive | orderbook relief captured MFE but later high MAE exposed utilization/cash gap |
| C11_CIS_222080_2024_03_05_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_POSITIVE | 222080 | 씨아이에스 | failed_rerating | counterexample | orderbook spike had mid-teens MFE but poor MAE without margin/revision bridge |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 011790 | source_proxy_only | copper foil customer/CAPA orderbook route; margin/FCF bridge pending | required before promotion |
| 336370 | source_proxy_only | copper foil relief/customer ramp route; utilization/cash bridge pending | required before promotion |
| 222080 | source_proxy_only | equipment orderbook spike but revenue/margin/revision bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 011790 | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv | atlas/symbol_profiles/011/011790.json |
| 336370 | atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv | atlas/symbol_profiles/336/336370.json |
| 222080 | atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv | atlas/symbol_profiles/222/222080.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| SKC_011790_2024_03_05_STAGE2A_COPPER_FOIL_ORDERBOOK_RERATING | Stage2-Actionable | 2024-03-05 | 2024-03-05 | 95800 | copper foil orderbook / CAPA route |
| SOLUS_336370_2024_03_27_STAGE2A_COPPER_FOIL_ORDERBOOK_RELIEF | Stage2-Actionable | 2024-03-27 | 2024-03-27 | 16970 | copper foil relief / customer ramp route |
| CIS_222080_2024_03_05_STAGE2_FALSE_POSITIVE_ORDERBOOK_SPIKE | Stage2 | 2024-03-05 | 2024-03-05 | 13150 | battery equipment orderbook spike without bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 011790 | 2024-03-05 | 95800 | 56.26 | -5.53 | 108.77 | -5.53 | 108.77 | -5.53 | 2024-06-18 | 200000 | -47.85 |
| 336370 | 2024-03-27 | 16970 | 27.87 | -11.37 | 38.48 | -11.37 | 38.48 | -33.99 | 2024-07-01 | 23500 | -52.34 |
| 222080 | 2024-03-05 | 13150 | 14.90 | -20.99 | 14.90 | -25.10 | 14.90 | -30.34 | 2024-03-11 | 15110 | -39.38 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 011790 | Stage2A/Yellow possible; 4B after rerating | extreme MFE, later peak drawdown | current_profile_4B_too_late |
| 336370 | Stage2A possible, but high utilization risk | useful MFE and high 180D MAE | current_profile_4B_too_late |
| 222080 | Stage2 risk if orderbook spike is over-credited | mid-MFE but high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C11 interpretation:

- Stage2A can work when orderbook/customer/CAPA evidence appears before price blowoff.
- Yellow/Green require revenue conversion, margin bridge, confirmed revision, and FCF conversion.
- Orderbook spike alone should not promote Stage2/Yellow when margin/revision bridge is absent.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 011790 | 1.00 | 1.00 | valuation rerating / positioning | extreme MFE requires 4B audit |
| 336370 | 1.00 | 1.00 | relief rerating / utilization pending | 4B utilization audit required |
| 222080 | 1.00 | 1.00 | orderbook spike / weak follow-through | not Stage3 without revenue/margin bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 011790 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 336370 | thesis_break_watch_only | not hard 4C, but utilization/cash bridge required |
| 222080 | hard_4c_late | revenue/margin/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = medium
```

Candidate:

> In L3 battery material and equipment names, orderbook or customer CAPA narratives can support Stage2A only when they are tied to revenue conversion, utilization, margin bridge, revision, or FCF. If the move is only an orderbook spike or relief rally, cap at Stage1/Stage2-watch and route to 4B/4C watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C11_BATTERY_ORDERBOOK_RERATING
confidence = medium
```

Candidate C11 rule:

```text
C11_orderbook_conversion_bridge_required =
  battery_orderbook_or_customer_route
  AND (revenue_conversion OR utilization_confirmation OR margin_bridge OR confirmed_revision OR fcf_conversion)

if orderbook_spike and conversion_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 35 and drawdown_after_peak < -35:
    add C11_peak_proximity_4B_audit = true

if MFE_90D < 20 and MAE_90D < -20:
    classify_as C11_orderbook_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 54.05 | -14.0 | 54.05 | -23.29 | 1 | useful but C11 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 54.05 | -14.0 | 54.05 | -23.29 | 1 | over-credits orderbook spikes |
| P1 sector_specific_candidate_profile | L3 | 2 promoted + 1 guard | 73.62 | -8.45 | 73.62 | -19.76 | 0 | better after conversion bridge gate |
| P2 canonical_archetype_candidate_profile | C11 | 2 promoted + 1 guard | 73.62 | -8.45 | 73.62 | -19.76 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C11 guard | 2 promoted + 1 guard | 73.62 | -8.45 | 73.62 | -19.76 | 0 | adds orderbook-spike false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 011790 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 336370 | Stage2A aligned but high-MAE; utilization audit needed | current_profile_4B_too_late |
| 222080 | Stage2 false positive if conversion bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | mixed C11 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 23 -> local projected 26 -> projected 29; still need 1 to reach 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C11_orderbook_conversion_bridge_required|C11_peak_proximity_4B_audit|C11_orderbook_false_positive_guardrail
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses clean 180D windows.
- Uses C11 Priority 0 coverage gap.
- Avoids static C11 top-covered symbols and local loop80 symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_conversion_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"222080 shows orderbook spike can fail without revenue/margin/revision bridge while 011790/336370 work only as Stage2A with 4B audit","blocks 222080 false positive while preserving 011790/336370 Stage2A","SKC_011790_2024_03_05_STAGE2A_COPPER_FOIL_ORDERBOOK_RERATING|SOLUS_336370_2024_03_27_STAGE2A_COPPER_FOIL_ORDERBOOK_RELIEF|CIS_222080_2024_03_05_STAGE2_FALSE_POSITIVE_ORDERBOOK_SPIKE",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C11_peak_proximity_4B_audit,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"011790/336370 orderbook reratings still needed 4B audit after peak and drawdown","adds 4B audit after large C11 MFE without converting price-only peaks into Green","SKC_011790_2024_03_05_STAGE2A_COPPER_FOIL_ORDERBOOK_RERATING|SOLUS_336370_2024_03_27_STAGE2A_COPPER_FOIL_ORDERBOOK_RELIEF",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C11_orderbook_false_positive_guardrail,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"222080 had mid-MFE but high MAE after orderbook spike","requires revenue/margin/revision bridge before Stage2/Yellow promotion","CIS_222080_2024_03_05_STAGE2_FALSE_POSITIVE_ORDERBOOK_SPIKE",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C11_SKC_011790_2024_03_05_COPPER_FOIL_ORDERBOOK_RERATING_4B","symbol":"011790","company_name":"SKC","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"COPPER_FOIL_ORDERBOOK_CUSTOMER_CAPA_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"SKC_011790_2024_03_05_STAGE2A_COPPER_FOIL_ORDERBOOK_RERATING","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"copper-foil/customer CAPA and orderbook rerating route captured >100% MFE, but peak-to-drawdown required 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C11 symbol versus top-covered C11 list and local loop80 C11 symbols; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C11_SOLUS_336370_2024_03_27_COPPER_FOIL_ORDERBOOK_RERATING_HIGH_DRAWDOWN","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"COPPER_FOIL_ORDERBOOK_RELIEF_RERATING_4B_HIGH_MAE","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"SOLUS_336370_2024_03_27_STAGE2A_COPPER_FOIL_ORDERBOOK_RELIEF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"copper-foil relief/orderbook route produced 38% MFE, then fell into high 180D MAE when utilization/cash bridge lagged","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"2024-01 corporate-action candidate is before selected entry window; selected 180D window is clean"}
{"row_type":"case","case_id":"C11_CIS_222080_2024_03_05_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_POSITIVE","symbol":"222080","company_name":"씨아이에스","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_SPIKE_MARGIN_BRIDGE_FAIL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"CIS_222080_2024_03_05_STAGE2_FALSE_POSITIVE_ORDERBOOK_SPIKE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"battery-equipment/orderbook spike produced mid-teens MFE but then persistent high MAE without margin/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C11 symbol; counterexample for orderbook spike without revenue/margin/revision conversion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"SKC_011790_2024_03_05_STAGE2A_COPPER_FOIL_ORDERBOOK_RERATING","case_id":"C11_SKC_011790_2024_03_05_COPPER_FOIL_ORDERBOOK_RERATING_4B","symbol":"011790","company_name":"SKC","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"COPPER_FOIL_ORDERBOOK_CUSTOMER_CAPA_RERATING_4B_WATCH","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":95800.0,"evidence_available_at_that_date":"source_proxy_only: copper foil customer/CAPA orderbook route, battery-material rerating, utilization expectation, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["copper_foil_orderbook_route","customer_capa_route","relative_strength","battery_material_rerating"],"stage3_evidence_fields":["customer_conversion_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":56.26,"MFE_90D_pct":108.77,"MFE_180D_pct":108.77,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-5.53,"MAE_90D_pct":-5.53,"MAE_180D_pct":-5.53,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":200000.0,"drawdown_after_peak_pct":-47.85,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"excellent_stage2a_but_extreme_peak_requires_C11_4B_audit","four_b_evidence_type":["valuation_rerating","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_011790_2024_03_05_95800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"SOLUS_336370_2024_03_27_STAGE2A_COPPER_FOIL_ORDERBOOK_RELIEF","case_id":"C11_SOLUS_336370_2024_03_27_COPPER_FOIL_ORDERBOOK_RERATING_HIGH_DRAWDOWN","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"COPPER_FOIL_ORDERBOOK_RELIEF_RERATING_4B_HIGH_MAE","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":16970.0,"evidence_available_at_that_date":"source_proxy_only: copper-foil orderbook relief, customer ramp expectation, battery-material rebound, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["copper_foil_orderbook_relief","customer_ramp_expectation","relative_strength"],"stage3_evidence_fields":["orderbook_conversion_partial","utilization_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["valuation_repricing","peak_proximity","utilization_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.87,"MFE_90D_pct":38.48,"MFE_180D_pct":38.48,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.37,"MAE_90D_pct":-11.37,"MAE_180D_pct":-33.99,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-01","peak_price":23500.0,"drawdown_after_peak_pct":-52.34,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"orderbook_relief_rerating_worked_but_high_mae_requires_4B_utilization_audit","four_b_evidence_type":["valuation_repricing","utilization_bridge_pending"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_high_mae_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_336370_2024_03_27_16970","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"CIS_222080_2024_03_05_STAGE2_FALSE_POSITIVE_ORDERBOOK_SPIKE","case_id":"C11_CIS_222080_2024_03_05_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_POSITIVE","symbol":"222080","company_name":"씨아이에스","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_SPIKE_MARGIN_BRIDGE_FAIL","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":13150.0,"evidence_available_at_that_date":"source_proxy_only: battery equipment/orderbook spike and relative strength visible, but revenue, margin, and revision bridge were unconfirmed","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["battery_equipment_orderbook_spike","relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_spike","weak_follow_through","margin_bridge_absent"],"stage4c_evidence_fields":["revenue_conversion_absent","margin_bridge_absent","revision_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv","profile_path":"atlas/symbol_profiles/222/222080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.9,"MFE_90D_pct":14.9,"MFE_180D_pct":14.9,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-20.99,"MAE_90D_pct":-25.1,"MAE_180D_pct":-30.34,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-11","peak_price":15110.0,"drawdown_after_peak_pct":-39.38,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"orderbook_spike_not_stage3_without_revenue_margin_revision_bridge","four_b_evidence_type":["price_spike","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_margin_bridge_fail","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_222080_2024_03_05_13150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_SKC_011790_2024_03_05_COPPER_FOIL_ORDERBOOK_RERATING_4B","trigger_id":"SKC_011790_2024_03_05_STAGE2A_COPPER_FOIL_ORDERBOOK_RERATING","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":9,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with mandatory C11 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Extreme copper-foil orderbook rerating worked, but Yellow/Green needs margin/FCF bridge and peak-proximity audit.","MFE_90D_pct":108.77,"MAE_90D_pct":-5.53,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_SOLUS_336370_2024_03_27_COPPER_FOIL_ORDERBOOK_RERATING_HIGH_DRAWDOWN","trigger_id":"SOLUS_336370_2024_03_27_STAGE2A_COPPER_FOIL_ORDERBOOK_RELIEF","symbol":"336370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable / 4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-watch / 4B utilization audit, not Yellow","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Relief rerating had usable MFE, but high 180D MAE says utilization/cash bridge must gate Yellow/Green.","MFE_90D_pct":38.48,"MAE_90D_pct":-11.37,"score_return_alignment_label":"positive_but_high_mae_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_CIS_222080_2024_03_05_BATTERY_EQUIPMENT_ORDERBOOK_FALSE_POSITIVE","trigger_id":"CIS_222080_2024_03_05_STAGE2_FALSE_POSITIVE_ORDERBOOK_SPIKE","symbol":"222080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Orderbook spike without revenue/margin/revision bridge produced mid-MFE but unacceptable MAE.","MFE_90D_pct":14.9,"MAE_90D_pct":-25.1,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

```text
completed_round = R3
completed_loop = 93
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

If this loop is accepted together with local loop80, C11 moves to projected 29 rows and still needs one more calibration row to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C11 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/011/011790.json
  - atlas/symbol_profiles/336/336370.json
  - atlas/symbol_profiles/222/222080.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
