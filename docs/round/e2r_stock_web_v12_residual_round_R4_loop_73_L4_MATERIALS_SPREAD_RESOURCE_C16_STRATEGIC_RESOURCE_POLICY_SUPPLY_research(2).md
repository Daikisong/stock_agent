# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R4
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R5
computed_next_loop: 73
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: C16_RESOURCE_RIGHTS_SUPPLY_CUSTOMER_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
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

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`. The prior R4 loop used C17 chemical/commodity margin spread, so this run shifts to C16 strategic-resource/policy supply. The residual target is the gap between resource security narrative and actual economics: discovery, graphite, coke, graphene, and supply-chain policy can all ignite price; only resource rights, customer/offtake, supply conversion, margin, cashflow, or commercial production can carry the flame.

| layer | id | definition |
|---|---|---|
| round | R4 | materials / spread / resource |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | materials, resources, strategic minerals, commodity and supply-chain themes |
| canonical | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | strategic resource policy, supply security, resource optionality |
| fine | C16_RESOURCE_RIGHTS_SUPPLY_CUSTOMER_MARGIN_BRIDGE_GUARD | resource theme must become rights/supply/customer/margin evidence |
| deep | TITANIUM_MINE_RESOURCE_OPTIONALITY_TO_NAV_SUPPLY_OPTIONALITY | resource discovery MFE with 4B guard |
| deep | GRAPHITE_ANODE_SUPPLY_SECURITY_THEME_WITHOUT_VOLUME_MARGIN_CONVERSION | coke/graphite supply theme false positive |
| deep | GRAPHITE_GRAPHENE_OPTIONALITY_WITHOUT_CUSTOMER_CONTRACT_MARGIN_OR_CASHFLOW | graphite/graphene theme high-MAE watch |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C16 top-covered symbols are `001570`, `005490`, `000910`, `075970`, `005290`, and `081150`. This run avoids that top cluster and also avoids the previous R4/C17 chemical-spread representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C16 | 012320 | new independent | not top-covered C16 symbol; titanium/resource discovery 4B bridge |
| C16 | 014580 | new independent | not top-covered C16 symbol; coke/graphite supply theme counterexample |
| C16 | 900250 | new independent | not top-covered C16 symbol; graphite/graphene theme high-MAE counterexample |

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
012320 has old corporate-action candidate dates ending 2017, outside the 2022 representative window.
014580 has old corporate-action candidate dates ending 2015, outside the 2023 representative window.
900250 has 2022 and 2024 corporate-action candidate dates; the selected 2023 window avoids the blocked dates.
011810/STX was reviewed but excluded because a 2023-09-15 corporate-action candidate contaminates the 180D window.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| resource_discovery_success_then_4B_watch | 012320 | 경동인베스트 | Stage2-Actionable | 2022-10-20 | 37550 | titanium/resource discovery produced MFE but needed 4B guard |
| failed_rerating_high_MAE | 014580 | 태경비케이 | Stage2-Actionable | 2023-03-23 | 8890 | coke/graphite supply theme lacked customer/margin bridge |
| theme_success_then_high_MAE_counterexample | 900250 | 크리스탈신소재 | Stage2-Actionable | 2023-04-10 | 1615 | graphite/graphene theme produced MFE then high-MAE drawdown |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 012320 | 경동인베스트 | Stage2-Actionable | 2022-10-20 | 37550 | 272.84 | 272.84 | 272.84 | -23.57 | -23.57 | -23.57 | 2022-11-16 | 140000 | -66.07 |
| 014580 | 태경비케이 | Stage2-Actionable | 2023-03-23 | 8890 | 20.13 | 20.13 | 20.13 | -19.01 | -24.75 | -32.06 | 2023-04-04 | 10680 | -43.45 |
| 900250 | 크리스탈신소재 | Stage2-Actionable | 2023-04-10 | 1615 | 32.2 | 69.04 | 69.04 | -47.18 | -47.18 | -48.61 | 2023-05-12 | 2730 | -69.6 |

## 9. Case-by-Case Notes

### 9.1 012320 / 경동인베스트 — titanium/resource discovery with 4B guard

The entry row is 2022-10-20 at 37,550. The path reaches 140,000 by the 30D/90D window, so price confirms that resource-discovery optionality can create explosive MFE. The model, however, should not treat this as Green. The correct C16 route is guarded Yellow/4B watch unless resource rights, mine economics, offtake, commercialization, and cashflow conversion become clearer.

### 9.2 014580 / 태경비케이 — coke/graphite supply theme without bridge

The entry row is 2023-03-23 at 8,890. The local high reaches 10,680, but the path later degrades into high MAE. This is the C16 supply-chain theme trap: coke/graphite/resource-security language can lift the first candle, but without customer-volume, margin, and real supply conversion the move loses its engine.

### 9.3 900250 / 크리스탈신소재 — graphite/graphene theme high-MAE watch

The entry row is 2023-04-10 at 1,615. The path produced MFE, but the later drawdown was severe. This is exactly where full 4B non-price evidence matters. A graphite/graphene theme can be loud; a customer/offtake/margin bridge is the quiet machine that must actually run.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C16 treats resource-security or graphite/graphene theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C16 needs resource-rights/supply/customer/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 014580 and 900250. |
| Full 4B non-price requirement appropriate? | Yes. 012320 is a 4B/resource discovery watch, not a Green case. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
012320:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed only as guarded resource-discovery bridge
  Stage3-Green = reject unless commercialization/offtake/cashflow bridge clears

014580:
  Stage2-Actionable = too generous if based only on coke/graphite supply-security theme
  Stage3-Yellow = reject without customer-volume/margin bridge
  Stage3-Green = reject

900250:
  Stage2-Actionable = acceptable as watch if theme evidence exists
  Stage3-Yellow = reject without customer/offtake/margin/cashflow bridge
  Stage3-Green = reject despite MFE because bridge is absent
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 012320 | 0.98 | 1.00 | large MFE resource-discovery 4B watch, not Green |
| 014580 | 1.00 | 1.00 | resource-theme local 4B watch, not positive stage |
| 900250 | 0.78 | 1.00 | large theme MFE but no bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c16_requires_resource_rights_supply_customer_margin_bridge

rule:
  For C16 strategic-resource/policy-supply rows, do not promote resource discovery,
  graphite, rare earth, coke, lithium/nickel, strategic mineral, or supply-security Stage2
  signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  resource rights, reserve/mine economics, customer/offtake, supply conversion,
  margin conversion, cashflow, commercial production, or verified supply-chain contract.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 120.67 | -31.83 | 66.7% | too generous to resource-theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 120.67 | -31.83 | 33.3% | safer but may miss 012320 |
| P1 sector_specific_candidate_profile | 3 | 120.67 | -31.83 | 66.7% | no broad L4 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 272.84 | -23.57 | 0% after guarded bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 44.59 | -35.97 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 012320 | current_profile_correct_but_needs_4B_guard | resource-discovery optionality aligned with strong MFE but not Green |
| 014580 | current_profile_false_positive | resource-security theme produced local MFE then high MAE |
| 900250 | current_profile_false_positive_if_green | graphite/graphene theme produced MFE but no durable bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | C16_RESOURCE_RIGHTS_SUPPLY_CUSTOMER_MARGIN_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C16 non-top-covered resource/theme bridge residual reduced |

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
- resource policy theme without customer/margin bridge
- resource discovery winner needs 4B watch
- graphite/graphene theme high-MAE after MFE
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
- STX/011810 as representative row, because 2023-09-15 corporate-action candidate contaminates the 180D window
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c16_requires_resource_rights_supply_customer_margin_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"C16 strategic-resource rows should not promote toward Stage3-Yellow/Green unless resource/policy signal converts into resource rights, supply conversion, customer/offtake, margin, cashflow, or commercial production bridge","012320 survives as guarded resource-discovery MFE case; 014580 and 900250 fail when resource/security theme lacks customer/supply/margin bridge","TRG_R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE|TRG_R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE|TRG_R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c16_resource_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,1,1,0,"Strategic-resource winners and theme failures can peak quickly before commercialization is proven; local 4B/high-MAE watch should remain active after MFE","prevents 014580/900250 from positive routing and keeps 012320 as 4B-watch rather than Green","TRG_R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE|TRG_R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE|TRG_R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE","symbol":"012320","company_name":"경동인베스트","round":"R4","loop":"73","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_TITANIUM_RESOURCE_DISCOVERY_POLICY_SUPPLY_4B_GUARD","deep_sub_archetype_id":"TITANIUM_MINE_RESOURCE_OPTIONALITY_TO_NAV_SUPPLY_OPTIONALITY","case_type":"resource_discovery_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_needs_4B_guard","price_source":"Songdaiki/stock-web","notes":"C16 strategic-resource rows require resource-rights, customer/offtake, supply conversion, margin, or cashflow bridge; resource/security theme alone is insufficient."}
{"row_type":"case","case_id":"R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE","symbol":"014580","company_name":"태경비케이","round":"R4","loop":"73","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_COKE_GRAPHITE_SUPPLY_THEME_WITHOUT_CUSTOMER_MARGIN_BRIDGE","deep_sub_archetype_id":"GRAPHITE_ANODE_SUPPLY_SECURITY_THEME_WITHOUT_VOLUME_MARGIN_CONVERSION","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C16 strategic-resource rows require resource-rights, customer/offtake, supply conversion, margin, or cashflow bridge; resource/security theme alone is insufficient."}
{"row_type":"case","case_id":"R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE","symbol":"900250","company_name":"크리스탈신소재","round":"R4","loop":"73","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_GRAPHITE_GRAPHENE_SUPPLY_THEME_WITHOUT_ECONOMIC_BRIDGE","deep_sub_archetype_id":"GRAPHITE_GRAPHENE_OPTIONALITY_WITHOUT_CUSTOMER_CONTRACT_MARGIN_OR_CASHFLOW","case_type":"theme_success_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C16 strategic-resource rows require resource-rights, customer/offtake, supply conversion, margin, or cashflow bridge; resource/security theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE","case_id":"R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE","symbol":"012320","company_name":"경동인베스트","round":"R4","loop":"73","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_TITANIUM_RESOURCE_DISCOVERY_POLICY_SUPPLY_4B_GUARD","deep_sub_archetype_id":"TITANIUM_MINE_RESOURCE_OPTIONALITY_TO_NAV_SUPPLY_OPTIONALITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-10-20","entry_date":"2022-10-20","entry_price":37550,"evidence_available_at_that_date":"source_proxy_titanium_resource_discovery_supply_optionality; evidence_url_pending","evidence_source":"source_proxy_titanium_resource_discovery_supply_optionality; evidence_url_pending","bridge_summary":"resource-discovery optionality produced large MFE, but supply/NAV commercialization uncertainty requires 4B watch rather than Green loosening","stage2_evidence_fields":["strategic_resource_discovery","policy_supply_security_theme","relative_strength","resource_NAV_optionality"],"stage3_evidence_fields":["resource_rights_visibility_proxy","supply_optionality_bridge","non_price_resource_discovery_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","resource_discovery_crowding","commercialization_uncertainty"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012320/2022.csv","profile_path":"atlas/symbol_profiles/012/012320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":272.84,"MFE_90D_pct":272.84,"MFE_180D_pct":272.84,"MFE_1Y_pct":272.84,"MFE_2Y_pct":272.84,"MAE_30D_pct":-23.57,"MAE_90D_pct":-23.57,"MAE_180D_pct":-23.57,"MAE_1Y_pct":-23.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-11-16","peak_price":140000,"drawdown_after_peak_pct":-66.07,"green_lateness_ratio":"0.27","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"large_MFE_resource_discovery_4B_watch_not_green","four_b_evidence_type":"non_price_resource_rights_supply_bridge","four_c_protection_label":"none","trigger_outcome_label":"resource_discovery_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_needs_4B_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE","case_id":"R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE","symbol":"014580","company_name":"태경비케이","round":"R4","loop":"73","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_COKE_GRAPHITE_SUPPLY_THEME_WITHOUT_CUSTOMER_MARGIN_BRIDGE","deep_sub_archetype_id":"GRAPHITE_ANODE_SUPPLY_SECURITY_THEME_WITHOUT_VOLUME_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-23","entry_date":"2023-03-23","entry_price":8890,"evidence_available_at_that_date":"source_proxy_calcined_coke_graphite_supply_security_theme_without_customer_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_calcined_coke_graphite_supply_security_theme_without_customer_margin_bridge; evidence_url_pending","bridge_summary":"resource/supply-chain theme lifted price briefly, but customer-volume, margin, and actual supply bridge were too weak and path degraded into high MAE","stage2_evidence_fields":["graphite_or_coke_supply_theme","policy_supply_security","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","customer_volume_bridge_absent","margin_conversion_absent"],"stage4c_evidence_fields":["high_MAE_without_customer_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014580/2023.csv","profile_path":"atlas/symbol_profiles/014/014580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.13,"MFE_90D_pct":20.13,"MFE_180D_pct":20.13,"MFE_1Y_pct":20.13,"MFE_2Y_pct":20.13,"MAE_30D_pct":-19.01,"MAE_90D_pct":-24.75,"MAE_180D_pct":-32.06,"MAE_1Y_pct":-32.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-04","peak_price":10680,"drawdown_after_peak_pct":-43.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"resource_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_resource_theme_without_economic_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE","case_id":"R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE","symbol":"900250","company_name":"크리스탈신소재","round":"R4","loop":"73","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"C16_GRAPHITE_GRAPHENE_SUPPLY_THEME_WITHOUT_ECONOMIC_BRIDGE","deep_sub_archetype_id":"GRAPHITE_GRAPHENE_OPTIONALITY_WITHOUT_CUSTOMER_CONTRACT_MARGIN_OR_CASHFLOW","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-10","entry_date":"2023-04-10","entry_price":1615,"evidence_available_at_that_date":"source_proxy_graphite_graphene_supply_theme_without_customer_contract_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_graphite_graphene_supply_theme_without_customer_contract_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"graphite/graphene supply-chain optionality created MFE, but lacked customer contract, margin, and cashflow bridge; theme later behaved as high-MAE watch case","stage2_evidence_fields":["graphite_graphene_supply_theme","China_supply_chain_policy_risk","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_peak","customer_contract_bridge_absent","margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_contract_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/900/900250/2023.csv","profile_path":"atlas/symbol_profiles/900/900250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.2,"MFE_90D_pct":69.04,"MFE_180D_pct":69.04,"MFE_1Y_pct":69.04,"MFE_2Y_pct":69.04,"MAE_30D_pct":-47.18,"MAE_90D_pct":-47.18,"MAE_180D_pct":-48.61,"MAE_1Y_pct":-48.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-12","peak_price":2730,"drawdown_after_peak_pct":-69.6,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"large_theme_MFE_but_no_source_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"price_resource_theme_without_economic_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_success_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE","trigger_id":"TRG_R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE","symbol":"012320","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"resource_policy_score":12,"resource_rights_score":11,"supply_conversion_score":9,"customer_offtake_margin_score":7,"relative_strength_score":12,"commercialization_risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"resource_policy_score":11,"resource_rights_score":14,"supply_conversion_score":11,"customer_offtake_margin_score":8,"relative_strength_score":9,"commercialization_risk_penalty":9},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["resource_policy_score","resource_rights_score","supply_conversion_score","customer_offtake_margin_score","relative_strength_score","commercialization_risk_penalty"],"component_delta_explanation":"C16 resource-discovery row is promoted only to guarded Yellow because resource-rights/supply optionality exists, but commercialization and 4B risk prevent Green loosening.","MFE_90D_pct":272.84,"MAE_90D_pct":-23.57,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_needs_4B_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE","trigger_id":"TRG_R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE","symbol":"014580","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"resource_policy_score":10,"resource_rights_score":2,"supply_conversion_score":1,"customer_offtake_margin_score":1,"relative_strength_score":11,"commercialization_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"resource_policy_score":4,"resource_rights_score":0,"supply_conversion_score":0,"customer_offtake_margin_score":0,"relative_strength_score":5,"commercialization_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["resource_policy_score","resource_rights_score","supply_conversion_score","customer_offtake_margin_score","relative_strength_score","commercialization_risk_penalty"],"component_delta_explanation":"C16 guard demotes resource/supply-chain theme rows when customer, supply, margin, or cashflow bridge is absent.","MFE_90D_pct":20.13,"MAE_90D_pct":-24.75,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE","trigger_id":"TRG_R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE","symbol":"900250","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"resource_policy_score":10,"resource_rights_score":2,"supply_conversion_score":1,"customer_offtake_margin_score":1,"relative_strength_score":11,"commercialization_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"resource_policy_score":4,"resource_rights_score":0,"supply_conversion_score":0,"customer_offtake_margin_score":0,"relative_strength_score":5,"commercialization_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["resource_policy_score","resource_rights_score","supply_conversion_score","customer_offtake_margin_score","relative_strength_score","commercialization_risk_penalty"],"component_delta_explanation":"C16 guard demotes resource/supply-chain theme rows when customer, supply, margin, or cashflow bridge is absent.","MFE_90D_pct":69.04,"MAE_90D_pct":-47.18,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c16_requires_resource_rights_supply_customer_margin_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"C16 strategic-resource rows should not promote toward Stage3-Yellow/Green unless resource/policy signal converts into resource rights, supply conversion, customer/offtake, margin, cashflow, or commercial production bridge","012320 survives as guarded resource-discovery MFE case; 014580 and 900250 fail when resource/security theme lacks customer/supply/margin bridge","TRG_R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE|TRG_R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE|TRG_R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c16_resource_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,1,1,0,"Strategic-resource winners and theme failures can peak quickly before commercialization is proven; local 4B/high-MAE watch should remain active after MFE","prevents 014580/900250 from positive routing and keeps 012320 as 4B-watch rather than Green","TRG_R4L73_C16_012320_20221020_TITANIUM_RESOURCE_DISCOVERY_4B_BRIDGE|TRG_R4L73_C16_014580_20230323_CALCINED_COKE_GRAPHITE_SUPPLY_THEME_WEAK_BRIDGE|TRG_R4L73_C16_900250_20230410_GRAPHITE_GRAPHENE_SUPPLY_THEME_NO_DURABLE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"73","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["resource_policy_theme_without_customer_margin_bridge","resource_discovery_winner_needs_4B_watch","graphite_graphene_theme_high_MAE_after_MFE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/resource-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C16 resource-policy rows cannot promote without resource-rights, customer/offtake, supply conversion, margin, or cashflow bridge.
12. Add validation that blocked corporate-action windows, such as 011810's 2023-09-15 candidate contamination, do not become representative calibration rows.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R4
completed_loop = 73
next_round = R5
next_loop = 73
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
atlas/symbol_profiles/014/014580.json
atlas/symbol_profiles/900/900250.json
atlas/symbol_profiles/011/011810.json
atlas/ohlcv_tradable_by_symbol_year/012/012320/2022.csv
atlas/ohlcv_tradable_by_symbol_year/014/014580/2023.csv
atlas/ohlcv_tradable_by_symbol_year/900/900250/2023.csv
atlas/ohlcv_tradable_by_symbol_year/011/011810/2023.csv
```

This loop continues loop 73 with R4 and adds 3 new independent C16 representative cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R4/L4.
