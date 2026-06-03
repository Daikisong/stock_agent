# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R3
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R4
computed_next_loop: 74
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: C14_EV_MATERIAL_DEMAND_SLOWDOWN_HIGH_MAE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`. The previous R3 loop used C13 battery JV/utilization/AMPC/IRA, so this run shifts to C14. C14 is a protection archetype: it asks whether earlier EV material MFE should be overridden when demand slowdown, utilization pressure, inventory pressure, margin risk, and high-MAE path appear.

| layer | id | definition |
|---|---|---|
| round | R3 | battery / EV / green mobility |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | battery, EV, green mobility, materials and supply chain |
| canonical | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV demand slowdown / 4B / 4C protection |
| fine | C14_EV_MATERIAL_DEMAND_SLOWDOWN_HIGH_MAE_GUARD | EV material MFE must not become Green when demand/margin risk dominates |
| deep | BATTERY_FOIL_CAPACITY_CUSTOMER_THEME_PEAK_TO_DEMAND_SLOWDOWN_DRAWNDOWN | aluminum foil blowoff to high-MAE watch |
| deep | COPPER_FOIL_CAPACITY_OPTIONALITY_TO_UTILIZATION_MARGIN_AND_EV_DEMAND_RESET | copper foil late MFE but no Green |
| deep | LITHIUM_CATHODE_MATERIAL_OPTIONALITY_WITHOUT_DEMAND_MARGIN_BRIDGE | lithium/cathode material false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C14 top-covered symbols are `247540`, `003670`, `066970`, `361610`, `373220`, and `393890`. This run avoids that top-covered cluster and also avoids the immediately prior R3/C13 symbols.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C14 | 006110 | new independent | not top-covered C14 symbol; battery foil MFE to EV demand-slowdown high-MAE |
| C14 | 011790 | new independent | not top-covered C14 symbol; copper foil utilization/margin slowdown watch |
| C14 | 095500 | new independent | not top-covered C14 symbol; lithium/cathode theme low-quality MFE to high-MAE |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
006110 has a 2023-02-09 corporate-action candidate, before the selected 2023-07-25 representative window.
011790 has only old corporate-action candidates from 1998/2001, outside the selected 2023 window.
095500 has only old corporate-action candidates from 2007~2009, outside the selected 2023 window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| MFE_then_high_MAE_after_EV_material_blowoff | 006110 | 삼아알미늄 | Stage2-Actionable | 2023-07-25 | 135600 | foil/capacity MFE later became 4B/high-MAE watch |
| copper_foil_MFE_then_demand_slowdown_high_MAE | 011790 | SKC | Stage2-Actionable | 2023-07-26 | 103000 | late MFE existed, but utilization/margin and EV slowdown risk blocked Green |
| failed_rerating_high_MAE_after_lithium_cathode_theme | 095500 | 미래나노텍 | Stage2-Actionable | 2023-07-25 | 28600 | lithium/cathode material theme produced high-MAE false start |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 0
counterexample_count: 3
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 3
```

C14 is intentionally a protection archetype, so a zero-positive set is acceptable here. The point is not to loosen Stage3; it is to prevent MFE-led false promotion after EV demand slowdown evidence appears.

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 006110 | 삼아알미늄 | Stage2-Actionable | 2023-07-25 | 135600 | 2.88 | 17.18 | 17.18 | -32.6 | -32.6 | -45.58 | 2023-10-17 | 158900 | -53.56 |
| 011790 | SKC | Stage2-Actionable | 2023-07-26 | 103000 | 7.77 | 7.77 | 45.34 | -12.62 | -32.82 | -32.82 | 2024-04-09 | 149700 | -19.84 |
| 095500 | 미래나노텍 | Stage2-Actionable | 2023-07-25 | 28600 | 7.17 | 7.17 | 7.17 | -33.43 | -41.54 | -54.58 | 2023-07-25 | 30650 | -57.62 |

## 9. Case-by-Case Notes

### 9.1 006110 / 삼아알미늄 — foil theme MFE, then slowdown-driven high-MAE watch

The entry row is 2023-07-25 at 135,600. The stock later reached 158,900, but the forward low reached 73,800. The lesson is that aluminum-foil capacity/customer optionality can generate MFE, yet once EV demand slowdown and material multiple compression arrive, the row should route to 4B/high-MAE watch.

### 9.2 011790 / SKC — copper foil late MFE does not erase earlier MAE risk

The entry row is 2023-07-26 at 103,000. It eventually produced a later MFE path, but it also printed deep adverse movement before the late rally. For C14, this is exactly the guardrail: a late peak does not rewrite the need to monitor utilization, margin, and demand reset.

### 9.3 095500 / 미래나노텍 — lithium/cathode theme false start

The entry row is 2023-07-25 at 28,600. The early upside was shallow, and the broader forward low reached 12,990. This is a straightforward C14 false positive: EV material optionality without demand, margin, inventory, and cashflow bridge should not remain Stage3-eligible.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C14 lets EV material MFE survive after demand slowdown and high-MAE evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C14 should intercept before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 006110 and 095500. |
| Full 4B non-price requirement appropriate? | Yes. MFE alone cannot make these rows positive. |
| 4C timing issue? | High-MAE watch is enough for these representatives; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
006110:
  Stage2-Actionable = acceptable only as event/theme watch
  Stage3-Yellow = reject once EV demand slowdown and high-MAE path appear
  Stage3-Green = reject despite prior MFE

011790:
  Stage2-Actionable = acceptable only with active utilization/margin guard
  Stage3-Yellow = reject unless demand and margin recovery are re-confirmed
  Stage3-Green = reject despite late MFE

095500:
  Stage2-Actionable = too generous if based on lithium/cathode theme only
  Stage3-Yellow = reject without demand, inventory, margin or cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 006110 | 0.85 | 1.00 | MFE existed, but EV slowdown routes to 4B/high-MAE watch |
| 011790 | 0.74 | 1.00 | late MFE exists, but utilization/margin risk blocks Green |
| 095500 | 1.00 | 1.00 | local material theme 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c14_ev_demand_slowdown_overrides_prior_mfe

rule:
  For C14 EV demand-slowdown rows, do not promote battery material,
  EV supply-chain, capacity, customer optionality, lithium/cathode, foil, or copper-foil
  Stage2 signals into Stage3-Yellow/Green when EV demand slowdown, utilization risk,
  inventory/margin pressure, customer call-off weakness, or high-MAE path appears.
  Prior MFE is kept as 4B evidence only, not positive stage evidence.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | Green false-positive risk | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 10.71 | -35.65 | high if MFE is over-read | needs C14 guard overlay |
| P0b e2r_2_0_baseline_reference | 3 | 10.71 | -35.65 | medium | safer but less explanatory |
| P2 canonical_guard_profile | 3 rejected/watch | 10.71 | -35.65 | 0% after no-Green routing | preferred shadow |
| P3 hard_4C_profile | 0 hard routes | 0 | 0 | not applicable | high-MAE watch enough here |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 006110 | current_profile_false_positive_if_green | prior MFE does not survive EV demand slowdown/high-MAE evidence |
| 011790 | current_profile_false_positive_if_green | late MFE exists, but utilization/margin risk blocks Green |
| 095500 | current_profile_false_positive | shallow MFE and high MAE confirm material-theme failure |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | C14_EV_MATERIAL_DEMAND_SLOWDOWN_HIGH_MAE_GUARD | 0 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | false | true | C14 non-top-covered EV-material slowdown residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
- hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
- EV material MFE over-read as positive
- demand slowdown high-MAE after blowoff
- capacity/customer optionality without margin-utilization bridge
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- round/sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean forward windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_ev_demand_slowdown_overrides_prior_mfe,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"C14 EV demand-slowdown rows should demote Stage2/Green when EV material MFE is followed by utilization risk, inventory/margin pressure, customer call-off weakness, or high MAE","006110/011790/095500 all show prior MFE cannot be treated as durable positive evidence when EV demand slowdown and high-MAE path dominate","TRG_R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B|TRG_R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B|TRG_R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START",3,3,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_full_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,1,1,0,"Battery material/theme rows can create MFE before demand slowdown is fully priced; full-window 4B/high-MAE watch must stay active","prevents EV material theme rows from becoming Green on MFE alone","TRG_R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B|TRG_R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B|TRG_R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START",3,3,3,medium,existing_axis_kept,"strengthens full 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B","symbol":"006110","company_name":"삼아알미늄","round":"R3","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B_GUARD","deep_sub_archetype_id":"BATTERY_FOIL_CAPACITY_CUSTOMER_THEME_PEAK_TO_DEMAND_SLOWDOWN_DRAWNDOWN","case_type":"MFE_then_high_MAE_after_EV_material_blowoff","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C14 is a protection archetype: EV demand slowdown, utilization risk, inventory/margin pressure and post-peak high MAE should block Green even when MFE existed."}
{"row_type":"case","case_id":"R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B","symbol":"011790","company_name":"SKC","round":"R3","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_COPPER_FOIL_CAPACITY_EV_DEMAND_SLOWDOWN_4B_GUARD","deep_sub_archetype_id":"COPPER_FOIL_CAPACITY_OPTIONALITY_TO_UTILIZATION_MARGIN_AND_EV_DEMAND_RESET","case_type":"copper_foil_MFE_then_demand_slowdown_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C14 is a protection archetype: EV demand slowdown, utilization risk, inventory/margin pressure and post-peak high MAE should block Green even when MFE existed."}
{"row_type":"case","case_id":"R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START","symbol":"095500","company_name":"미래나노텍","round":"R3","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_LITHIUM_CATHODE_THEME_EV_DEMAND_SLOWDOWN_FALSE_START","deep_sub_archetype_id":"LITHIUM_CATHODE_MATERIAL_OPTIONALITY_WITHOUT_DEMAND_MARGIN_BRIDGE","case_type":"failed_rerating_high_MAE_after_lithium_cathode_theme","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C14 is a protection archetype: EV demand slowdown, utilization risk, inventory/margin pressure and post-peak high MAE should block Green even when MFE existed."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B","case_id":"R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B","symbol":"006110","company_name":"삼아알미늄","round":"R3","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B_GUARD","deep_sub_archetype_id":"BATTERY_FOIL_CAPACITY_CUSTOMER_THEME_PEAK_TO_DEMAND_SLOWDOWN_DRAWNDOWN","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-25","entry_date":"2023-07-25","entry_price":135600,"evidence_available_at_that_date":"source_proxy_battery_aluminum_foil_customer_capacity_theme_followed_by_EV_material_demand_slowdown; evidence_url_pending","evidence_source":"source_proxy_battery_aluminum_foil_customer_capacity_theme_followed_by_EV_material_demand_slowdown; evidence_url_pending","bridge_summary":"battery foil capacity/customer theme produced MFE, but EV demand slowdown and material multiple compression turned it into 4B/high-MAE rather than Green evidence","stage2_evidence_fields":["battery_foil_capacity_theme","customer_capacity_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["battery_material_blowoff_peak","EV_demand_slowdown_watch","capacity_multiple_compression"],"stage4c_evidence_fields":["high_MAE_after_EV_material_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv|atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv","profile_path":"atlas/symbol_profiles/006/006110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.88,"MFE_90D_pct":17.18,"MFE_180D_pct":17.18,"MFE_1Y_pct":17.18,"MFE_2Y_pct":17.18,"MAE_30D_pct":-32.6,"MAE_90D_pct":-32.6,"MAE_180D_pct":-45.58,"MAE_1Y_pct":-45.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-17","peak_price":158900,"drawdown_after_peak_pct":-53.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"MFE_existed_but_EV_material_slowdown_routes_to_4B_high_MAE_watch","four_b_evidence_type":"EV_demand_slowdown_high_MAE_guard","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B","case_id":"R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B","symbol":"011790","company_name":"SKC","round":"R3","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_COPPER_FOIL_CAPACITY_EV_DEMAND_SLOWDOWN_4B_GUARD","deep_sub_archetype_id":"COPPER_FOIL_CAPACITY_OPTIONALITY_TO_UTILIZATION_MARGIN_AND_EV_DEMAND_RESET","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-26","entry_date":"2023-07-26","entry_price":103000,"evidence_available_at_that_date":"source_proxy_copper_foil_capacity_EV_demand_slowdown_margin_utilization_risk; evidence_url_pending","evidence_source":"source_proxy_copper_foil_capacity_EV_demand_slowdown_margin_utilization_risk; evidence_url_pending","bridge_summary":"copper foil capacity optionality and EV supply-chain beta produced later MFE, but utilization/margin demand risk kept the row as 4B/high-MAE watch instead of Stage3-Green","stage2_evidence_fields":["copper_foil_capacity_optionality","EV_supply_chain_beta","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["EV_demand_slowdown_watch","utilization_margin_risk","post_MFE_peak_watch"],"stage4c_evidence_fields":["high_MAE_before_late_MFE"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv|atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.77,"MFE_90D_pct":7.77,"MFE_180D_pct":45.34,"MFE_1Y_pct":45.34,"MFE_2Y_pct":45.34,"MAE_30D_pct":-12.62,"MAE_90D_pct":-32.82,"MAE_180D_pct":-32.82,"MAE_1Y_pct":-32.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-09","peak_price":149700,"drawdown_after_peak_pct":-19.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_MFE_but_utilization_margin_risk_blocks_Green","four_b_evidence_type":"EV_demand_slowdown_high_MAE_guard","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"late_MFE_but_4B_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START","case_id":"R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START","symbol":"095500","company_name":"미래나노텍","round":"R3","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_LITHIUM_CATHODE_THEME_EV_DEMAND_SLOWDOWN_FALSE_START","deep_sub_archetype_id":"LITHIUM_CATHODE_MATERIAL_OPTIONALITY_WITHOUT_DEMAND_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-25","entry_date":"2023-07-25","entry_price":28600,"evidence_available_at_that_date":"source_proxy_lithium_cathode_material_theme_without_demand_margin_inventory_bridge; evidence_url_pending","evidence_source":"source_proxy_lithium_cathode_material_theme_without_demand_margin_inventory_bridge; evidence_url_pending","bridge_summary":"lithium/cathode material optionality lacked demand, margin, inventory and cashflow bridge as EV slowdown pressure expanded","stage2_evidence_fields":["lithium_cathode_material_theme","EV_material_relative_strength","price_spike"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_peak","demand_slowdown","inventory_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_demand_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv|atlas/ohlcv_tradable_by_symbol_year/095/095500/2024.csv","profile_path":"atlas/symbol_profiles/095/095500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.17,"MFE_90D_pct":7.17,"MFE_180D_pct":7.17,"MFE_1Y_pct":7.17,"MFE_2Y_pct":7.17,"MAE_30D_pct":-33.43,"MAE_90D_pct":-41.54,"MAE_180D_pct":-54.58,"MAE_1Y_pct":-54.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-25","peak_price":30650,"drawdown_after_peak_pct":-57.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_material_theme_4B_watch_not_positive_stage","four_b_evidence_type":"EV_demand_slowdown_high_MAE_guard","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B","trigger_id":"TRG_R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B","symbol":"006110","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"EV_material_theme_score":12,"capacity_customer_optionality_score":8,"demand_slowdown_risk_score":4,"inventory_margin_pressure_score":3,"relative_strength_score":12,"4B_4C_guard_penalty":5},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"EV_material_theme_score":5,"capacity_customer_optionality_score":2,"demand_slowdown_risk_score":15,"inventory_margin_pressure_score":14,"relative_strength_score":5,"4B_4C_guard_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["EV_material_theme_score","capacity_customer_optionality_score","demand_slowdown_risk_score","inventory_margin_pressure_score","relative_strength_score","4B_4C_guard_penalty"],"component_delta_explanation":"C14 guard demotes EV material Stage2 rows when demand slowdown, utilization risk, inventory/margin pressure and high MAE dominate despite earlier MFE.","MFE_90D_pct":17.18,"MAE_90D_pct":-32.6,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B","trigger_id":"TRG_R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"EV_material_theme_score":12,"capacity_customer_optionality_score":8,"demand_slowdown_risk_score":4,"inventory_margin_pressure_score":3,"relative_strength_score":12,"4B_4C_guard_penalty":5},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"EV_material_theme_score":5,"capacity_customer_optionality_score":2,"demand_slowdown_risk_score":15,"inventory_margin_pressure_score":14,"relative_strength_score":5,"4B_4C_guard_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["EV_material_theme_score","capacity_customer_optionality_score","demand_slowdown_risk_score","inventory_margin_pressure_score","relative_strength_score","4B_4C_guard_penalty"],"component_delta_explanation":"C14 guard demotes EV material Stage2 rows when demand slowdown, utilization risk, inventory/margin pressure and high MAE dominate despite earlier MFE.","MFE_90D_pct":7.77,"MAE_90D_pct":-32.82,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START","trigger_id":"TRG_R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START","symbol":"095500","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"EV_material_theme_score":12,"capacity_customer_optionality_score":8,"demand_slowdown_risk_score":4,"inventory_margin_pressure_score":3,"relative_strength_score":12,"4B_4C_guard_penalty":5},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"EV_material_theme_score":5,"capacity_customer_optionality_score":2,"demand_slowdown_risk_score":15,"inventory_margin_pressure_score":14,"relative_strength_score":5,"4B_4C_guard_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["EV_material_theme_score","capacity_customer_optionality_score","demand_slowdown_risk_score","inventory_margin_pressure_score","relative_strength_score","4B_4C_guard_penalty"],"component_delta_explanation":"C14 guard demotes EV material Stage2 rows when demand slowdown, utilization risk, inventory/margin pressure and high MAE dominate despite earlier MFE.","MFE_90D_pct":7.17,"MAE_90D_pct":-41.54,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_ev_demand_slowdown_overrides_prior_mfe,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"C14 EV demand-slowdown rows should demote Stage2/Green when EV material MFE is followed by utilization risk, inventory/margin pressure, customer call-off weakness, or high MAE","006110/011790/095500 all show prior MFE cannot be treated as durable positive evidence when EV demand slowdown and high-MAE path dominate","TRG_R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B|TRG_R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B|TRG_R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START",3,3,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_full_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,1,1,0,"Battery material/theme rows can create MFE before demand slowdown is fully priced; full-window 4B/high-MAE watch must stay active","prevents EV material theme rows from becoming Green on MFE alone","TRG_R3L74_C14_006110_20230725_ALUMINUM_FOIL_EV_DEMAND_SLOWDOWN_4B|TRG_R3L74_C14_011790_20230726_COPPER_FOIL_EV_DEMAND_SLOWDOWN_4B|TRG_R3L74_C14_095500_20230725_CATHODE_LITHIUM_THEME_DEMAND_SLOWDOWN_FALSE_START",3,3,3,medium,existing_axis_kept,"strengthens full 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["EV_material_MFE_overread_as_positive","demand_slowdown_high_MAE_after_blowoff","capacity_customer_optionality_without_margin_utilization_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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
- price-only/EV-material-theme-only rows cannot promote Stage2/Stage3.
- Prior MFE cannot block C14 high-MAE/EV-demand-slowdown routing.
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
11. Add validation that C14 EV demand-slowdown rows cannot promote when demand slowdown, utilization risk, inventory/margin pressure, customer call-off weakness, or high-MAE evidence appears.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R3
completed_loop = 74
next_round = R4
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/006/006110.json
atlas/symbol_profiles/011/011790.json
atlas/symbol_profiles/095/095500.json
atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv
atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv
atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv
atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv
atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv
atlas/ohlcv_tradable_by_symbol_year/095/095500/2024.csv
```

This loop continues loop 74 with R3 and adds 3 new independent C14 protection/counterexample cases for R3/L3.
