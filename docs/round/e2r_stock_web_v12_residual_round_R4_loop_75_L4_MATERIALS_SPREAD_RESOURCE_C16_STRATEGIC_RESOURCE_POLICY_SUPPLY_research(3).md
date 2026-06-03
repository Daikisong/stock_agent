# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R4
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R5
computed_next_loop: 75
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: C16_POLICY_PROJECT_OFFTAKE_PRODUCTION_CASHFLOW_BRIDGE_GUARD
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

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`. The previous R4 loop used C15 material-spread/supercycle, so this run rotates to C16 strategic-resource/policy-supply. The target is the boundary between real domestic resource project option value and resource-theme price heat that never becomes offtake, production or cashflow.

| layer | id | definition |
|---|---|---|
| round | R4 | materials / spread / resource |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | commodity/material spread, resource, strategic supply, policy resource security |
| canonical | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | strategic resource, domestic supply, policy/project supply security |
| fine | C16_POLICY_PROJECT_OFFTAKE_PRODUCTION_CASHFLOW_BRIDGE_GUARD | resource signal must become policy/project/offtake/production/cashflow evidence |
| deep | DOMESTIC_TITANIUM_RESOURCE_PROJECT_POLICY_SUPPLY_TO_OPTION_VALUE_AND_RERATING_WITH_EXECUTION_RISK | domestic strategic resource guarded positive |
| deep | RARE_EARTH_MAGNET_SUPPLY_SECURITY_THEME_WITHOUT_CUSTOMER_OFFTAKE_MARGIN_OR_VOLUME_CONVERSION | rare-earth magnet false positive |
| deep | GOLD_SAFE_HAVEN_RESOURCE_OPTIONALITY_WITHOUT_PRODUCTION_VOLUME_MARGIN_CASHFLOW_CONVERSION | gold resource false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C16 top-covered symbols are `001570`, `005490`, `000910`, `075970`, `005290`, and `081150`. This run avoids that top-covered cluster and also avoids the immediately prior R4/C15 representatives `103140`, `004560`, and `001780`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C16 | 012320 | new independent | not top-covered C16 symbol; domestic titanium/resource policy-project bridge |
| C16 | 047400 | new independent | not top-covered C16 symbol; rare-earth/magnet theme without offtake/margin bridge |
| C16 | 037950 | new independent | not top-covered C16 symbol; gold/resource theme without production/cashflow bridge |
| excluded | 011810 | blocked/avoided | 2024-01-05 corporate-action candidate and major raw-discontinuity caveat reduced representative value |

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
012320 has corporate-action candidates ending 2017-08-25, outside the selected 2024 representative window.
047400 has a 2011-04-29 corporate-action candidate, outside the selected 2024 representative window.
037950 has corporate-action candidates ending 2013-11-22, outside the selected 2024 representative window.
011810/STX was inspected but excluded because a 2024-01-05 corporate-action candidate and has_major_raw_discontinuity caveat reduced calibration cleanliness.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| strategic_resource_project_success_then_4B_watch | 012320 | 경동인베스트 | Stage2-Actionable | 2024-03-21 | 80400 | domestic strategic-resource project/policy-supply bridge worked, but execution/offtake risk required 4B |
| rare_earth_theme_MFE_then_high_MAE_counterexample | 047400 | 유니온머티리얼 | Stage2-Actionable | 2024-01-18 | 3535 | rare-earth/magnet supply-security theme lacked offtake and margin bridge |
| gold_resource_theme_MFE_then_high_MAE_counterexample | 037950 | 엘컴텍 | Stage2-Actionable | 2024-01-15 | 1403 | gold/resource theme MFE lacked production/cashflow bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 012320 | 경동인베스트 | Stage2-Actionable | 2024-03-21 | 80400 | 54.1 | 54.1 | 54.1 | -17.79 | -17.79 | -17.79 | 2024-03-25 | 123900 | -46.65 |
| 047400 | 유니온머티리얼 | Stage2-Actionable | 2024-01-18 | 3535 | 3.96 | 3.96 | 3.96 | -18.95 | -30.41 | -42.29 | 2024-01-23 | 3675 | -44.49 |
| 037950 | 엘컴텍 | Stage2-Actionable | 2024-01-15 | 1403 | 8.34 | 24.59 | 24.59 | -13.11 | -14.47 | -20.81 | 2024-04-08 | 1748 | -36.44 |

## 9. Case-by-Case Notes

### 9.1 012320 / 경동인베스트 — domestic strategic-resource project bridge

The entry row is 2024-03-21 at 80,400. The path reached 123,900 within the early window. This is a valid C16 positive only as guarded Yellow: the domestic strategic-resource project and policy-supply-security bridge created option value, but the row still lacked enough offtake, production economics and cashflow evidence to justify Green. After the peak, the low reached 66,100, so 4B/high-MAE watch remains active.

### 9.2 047400 / 유니온머티리얼 — rare-earth/magnet theme without offtake bridge

The entry row is 2024-01-18 at 3,535. The local MFE reached 3,675, but the 180D low fell to 2,040. Rare-earth and magnet supply-security language can light the match, but without customer offtake, volume, margin and cash conversion, the flame becomes a 4B/high-MAE warning rather than Stage3 evidence.

### 9.3 037950 / 엘컴텍 — gold/resource theme without production and cashflow bridge

The entry row is 2024-01-15 at 1,403. MFE existed and later reached 1,748, but the 180D low fell to 1,111. Gold/resource optionality worked as theme beta, not as production, reserve-economics, margin or cashflow proof. This row is useful because it shows MFE alone cannot substitute for a source bridge.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C16 treats resource/rare-earth/gold theme strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C16 needs policy/project/offtake/production/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 012320 peak and 047400 local theme spike. |
| Full 4B non-price requirement appropriate? | Yes. MFE alone cannot make 047400/037950 positive. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
012320:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after domestic strategic-resource project/policy bridge
  Stage3-Green = reject unless offtake, production economics and cashflow durability are confirmed

047400:
  Stage2-Actionable = too generous if based only on rare-earth/magnet supply-security theme
  Stage3-Yellow = reject without customer offtake, volume, margin and cashflow bridge
  Stage3-Green = reject

037950:
  Stage2-Actionable = acceptable only as gold/resource watch
  Stage3-Yellow = reject without production volume, reserve economics, margin or cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 012320 | 1.00 | 1.00 | resource project positive but full-window 4B execution/economics watch |
| 047400 | 1.00 | 1.00 | rare-earth theme local 4B watch, not positive stage |
| 037950 | 0.87 | 1.00 | gold resource MFE but no production/cashflow bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c16_requires_policy_project_offtake_production_cashflow_bridge

rule:
  For C16 strategic-resource/policy-supply rows, do not promote rare earth,
  gold, titanium, domestic resource, critical mineral, supply-security, or resource-theme
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  policy/project visibility, legally durable project progress, customer offtake,
  domestic supply-chain security, reserve economics, production volume,
  margin conversion, FCF/cash conversion, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 27.55 | -20.89 | 66.7% | too generous to resource-theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 27.55 | -20.89 | 33.3% | safer but may miss 012320 |
| P1 sector_specific_candidate_profile | 3 | 27.55 | -20.89 | 66.7% | no broad L4 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 54.1 | -17.79 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 14.28 | -22.44 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 012320 | current_profile_correct_but_no_green | domestic project/policy bridge aligned with MFE, but high-MAE blocks Green |
| 047400 | current_profile_false_positive | rare-earth/magnet theme produced high MAE without offtake/margin bridge |
| 037950 | current_profile_false_positive_if_green | gold/resource MFE lacked production/cashflow bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16_POLICY_PROJECT_OFFTAKE_PRODUCTION_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R4/C16 non-top-covered strategic-resource residual reduced |

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
residual_error_types_found:
- resource theme without offtake/cashflow bridge
- strategic-resource project winner needs 4B watch
- rare-earth/gold theme high-MAE
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
- R4 direct L4 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact resource project or offtake announcement URLs
- production scoring behavior
- live candidate status
- 011810/STX as representative row because 2024-01-05 corporate-action and major raw-discontinuity caveat reduced cleanliness
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c16_requires_policy_project_offtake_production_cashflow_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"C16 strategic-resource rows should not promote toward Stage3-Yellow/Green unless resource or supply-security signal converts into policy/project visibility, customer offtake, domestic supply-chain security, reserve economics, production volume, margin, FCF or cashflow bridge","012320 survives only as guarded positive after domestic strategic-resource project/policy bridge; 047400 and 037950 are demoted because rare-earth/gold themes lacked offtake, production and cashflow bridge","TRG_R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE|TRG_R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE|TRG_R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c16_resource_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,1,1,0,"Strategic-resource winners and resource-theme false starts can peak before offtake/economics/cashflow durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 012320 guarded positive while preventing 047400/037950 resource-theme false positives","TRG_R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE|TRG_R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE|TRG_R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE","symbol":"012320","company_name":"경동인베스트","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_DOMESTIC_STRATEGIC_RESOURCE_POLICY_PROJECT_BRIDGE","deep_sub_archetype_id":"DOMESTIC_TITANIUM_RESOURCE_PROJECT_POLICY_SUPPLY_TO_OPTION_VALUE_AND_RERATING_WITH_EXECUTION_RISK","case_type":"strategic_resource_project_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C16 strategic-resource rows require policy/project visibility, customer offtake, domestic supply-chain security, reserve economics, production volume, margin, or cashflow bridge; resource/rare-earth/gold theme alone is insufficient."}
{"row_type":"case","case_id":"R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE","symbol":"047400","company_name":"유니온머티리얼","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE","deep_sub_archetype_id":"RARE_EARTH_MAGNET_SUPPLY_SECURITY_THEME_WITHOUT_CUSTOMER_OFFTAKE_MARGIN_OR_VOLUME_CONVERSION","case_type":"rare_earth_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C16 strategic-resource rows require policy/project visibility, customer offtake, domestic supply-chain security, reserve economics, production volume, margin, or cashflow bridge; resource/rare-earth/gold theme alone is insufficient."}
{"row_type":"case","case_id":"R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE","symbol":"037950","company_name":"엘컴텍","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_GOLD_RESOURCE_THEME_WITHOUT_PRODUCTION_CASHFLOW_BRIDGE","deep_sub_archetype_id":"GOLD_SAFE_HAVEN_RESOURCE_OPTIONALITY_WITHOUT_PRODUCTION_VOLUME_MARGIN_CASHFLOW_CONVERSION","case_type":"gold_resource_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C16 strategic-resource rows require policy/project visibility, customer offtake, domestic supply-chain security, reserve economics, production volume, margin, or cashflow bridge; resource/rare-earth/gold theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE","case_id":"R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE","symbol":"012320","company_name":"경동인베스트","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_DOMESTIC_STRATEGIC_RESOURCE_POLICY_PROJECT_BRIDGE","deep_sub_archetype_id":"DOMESTIC_TITANIUM_RESOURCE_PROJECT_POLICY_SUPPLY_TO_OPTION_VALUE_AND_RERATING_WITH_EXECUTION_RISK","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":80400,"evidence_available_at_that_date":"source_proxy_domestic_titanium_strategic_resource_policy_supply_project_option_value_bridge; evidence_url_pending","evidence_source":"source_proxy_domestic_titanium_strategic_resource_policy_supply_project_option_value_bridge; evidence_url_pending","bridge_summary":"domestic strategic-resource project and policy-supply optionality converted into sharp option-value rerating, but execution, permitting, economics and offtake proof remained 4B risk","stage2_evidence_fields":["domestic_strategic_resource_project","policy_supply_security","resource_option_value","relative_strength"],"stage3_evidence_fields":["policy_project_visibility","domestic_supply_chain_security_bridge","resource_option_value_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","resource_project_execution_risk","offtake_economics_unconfirmed"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012320/2024.csv","profile_path":"atlas/symbol_profiles/012/012320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":54.1,"MFE_90D_pct":54.1,"MFE_180D_pct":54.1,"MFE_1Y_pct":54.1,"MFE_2Y_pct":54.1,"MAE_30D_pct":-17.79,"MAE_90D_pct":-17.79,"MAE_180D_pct":-17.79,"MAE_1Y_pct":-17.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":123900,"drawdown_after_peak_pct":-46.65,"green_lateness_ratio":"0.22","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"resource_project_positive_but_full_window_4B_execution_economics_watch","four_b_evidence_type":"non_price_policy_project_supply_bridge","four_c_protection_label":"post_peak_high_MAE_watch","trigger_outcome_label":"strategic_resource_project_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE","case_id":"R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE","symbol":"047400","company_name":"유니온머티리얼","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE","deep_sub_archetype_id":"RARE_EARTH_MAGNET_SUPPLY_SECURITY_THEME_WITHOUT_CUSTOMER_OFFTAKE_MARGIN_OR_VOLUME_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":3535,"evidence_available_at_that_date":"source_proxy_rare_earth_magnet_supply_security_theme_without_customer_offtake_margin_volume_bridge; evidence_url_pending","evidence_source":"source_proxy_rare_earth_magnet_supply_security_theme_without_customer_offtake_margin_volume_bridge; evidence_url_pending","bridge_summary":"rare-earth/magnet supply-security theme produced a local MFE spike but did not convert into visible customer offtake, volume, margin, or cashflow bridge","stage2_evidence_fields":["rare_earth_policy_theme","magnet_supply_security","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_local_peak","offtake_bridge_absent","margin_volume_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_offtake_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv","profile_path":"atlas/symbol_profiles/047/047400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.96,"MFE_90D_pct":3.96,"MFE_180D_pct":3.96,"MFE_1Y_pct":3.96,"MFE_2Y_pct":3.96,"MAE_30D_pct":-18.95,"MAE_90D_pct":-30.41,"MAE_180D_pct":-42.29,"MAE_1Y_pct":-42.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-23","peak_price":3675,"drawdown_after_peak_pct":-44.49,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"rare_earth_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"resource_theme_without_offtake_economics_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"rare_earth_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE","case_id":"R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE","symbol":"037950","company_name":"엘컴텍","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_GOLD_RESOURCE_THEME_WITHOUT_PRODUCTION_CASHFLOW_BRIDGE","deep_sub_archetype_id":"GOLD_SAFE_HAVEN_RESOURCE_OPTIONALITY_WITHOUT_PRODUCTION_VOLUME_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-15","entry_date":"2024-01-15","entry_price":1403,"evidence_available_at_that_date":"source_proxy_gold_safe_haven_resource_theme_without_production_volume_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_gold_safe_haven_resource_theme_without_production_volume_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"gold/safe-haven resource optionality produced MFE, but production volume, reserve economics, margin and cashflow bridge did not become durable enough","stage2_evidence_fields":["gold_resource_theme","safe_haven_policy_risk","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["resource_theme_peak","production_volume_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_production_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/037/037950/2024.csv","profile_path":"atlas/symbol_profiles/037/037950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.34,"MFE_90D_pct":24.59,"MFE_180D_pct":24.59,"MFE_1Y_pct":24.59,"MFE_2Y_pct":24.59,"MAE_30D_pct":-13.11,"MAE_90D_pct":-14.47,"MAE_180D_pct":-20.81,"MAE_1Y_pct":-20.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":1748,"drawdown_after_peak_pct":-36.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"gold_resource_MFE_but_no_production_cashflow_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"resource_theme_without_offtake_economics_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"gold_resource_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE","trigger_id":"TRG_R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE","symbol":"012320","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"policy_supply_score":12,"resource_project_score":12,"offtake_economics_score":7,"production_cashflow_score":4,"relative_strength_score":13,"risk_penalty":7},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_supply_score":15,"resource_project_score":15,"offtake_economics_score":8,"production_cashflow_score":5,"relative_strength_score":9,"risk_penalty":11},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["policy_supply_score","resource_project_score","offtake_economics_score","production_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C16 row is promoted only because a domestic strategic-resource project and policy-supply bridge exists; execution/offtake/cashflow uncertainty and high MAE block Green.","MFE_90D_pct":54.1,"MAE_90D_pct":-17.79,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE","trigger_id":"TRG_R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE","symbol":"047400","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"policy_supply_score":11,"resource_project_score":4,"offtake_economics_score":1,"production_cashflow_score":0,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_supply_score":5,"resource_project_score":1,"offtake_economics_score":0,"production_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_supply_score","resource_project_score","offtake_economics_score","production_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C16 guard demotes strategic-resource/rare-earth/gold theme rows when offtake, reserve economics, volume, margin and cashflow bridge are absent.","MFE_90D_pct":3.96,"MAE_90D_pct":-30.41,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE","trigger_id":"TRG_R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE","symbol":"037950","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"policy_supply_score":11,"resource_project_score":4,"offtake_economics_score":1,"production_cashflow_score":0,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_supply_score":5,"resource_project_score":1,"offtake_economics_score":0,"production_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_supply_score","resource_project_score","offtake_economics_score","production_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C16 guard demotes strategic-resource/rare-earth/gold theme rows when offtake, reserve economics, volume, margin and cashflow bridge are absent.","MFE_90D_pct":24.59,"MAE_90D_pct":-14.47,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c16_requires_policy_project_offtake_production_cashflow_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"C16 strategic-resource rows should not promote toward Stage3-Yellow/Green unless resource or supply-security signal converts into policy/project visibility, customer offtake, domestic supply-chain security, reserve economics, production volume, margin, FCF or cashflow bridge","012320 survives only as guarded positive after domestic strategic-resource project/policy bridge; 047400 and 037950 are demoted because rare-earth/gold themes lacked offtake, production and cashflow bridge","TRG_R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE|TRG_R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE|TRG_R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c16_resource_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,1,1,0,"Strategic-resource winners and resource-theme false starts can peak before offtake/economics/cashflow durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 012320 guarded positive while preventing 047400/037950 resource-theme false positives","TRG_R4L75_C16_012320_20240321_DOMESTIC_TITANIUM_RESOURCE_POLICY_SUPPLY_BRIDGE|TRG_R4L75_C16_047400_20240118_RARE_EARTH_MAGNET_THEME_WITHOUT_OFFTAKE_MARGIN_BRIDGE|TRG_R4L75_C16_037950_20240115_GOLD_RESOURCE_THEME_NO_PRODUCTION_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"75","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["resource_theme_without_offtake_cashflow_bridge","strategic_resource_project_winner_needs_4B_watch","rare_earth_gold_theme_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R4-specific handling

- R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`.
- This MD uses `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/resource-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R4 direct L4 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C16 strategic-resource rows cannot promote without policy/project visibility, legally durable project progress, customer offtake, domestic supply-chain security, reserve economics, production volume, margin conversion, FCF/cash conversion, or earnings revision.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R4
completed_loop = 75
next_round = R5
next_loop = 75
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
atlas/symbol_profiles/012/012320.json
atlas/symbol_profiles/047/047400.json
atlas/symbol_profiles/037/037950.json
atlas/symbol_profiles/011/011810.json
atlas/ohlcv_tradable_by_symbol_year/012/012320/2024.csv
atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv
atlas/ohlcv_tradable_by_symbol_year/037/037950/2024.csv
```

This loop continues loop 75 with R4 and adds 3 new independent C16 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R4/L4.
