# E2R Stock-Web v12 Residual Research — R3 Loop 87 / L3 / C12

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 87,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 87,
  "computed_next_round": "R4",
  "computed_next_loop": 87,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "COPPER_FOIL_CNT_CONDUCTIVE_ELECTROLYTE_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "battery_customer_contract_calloff_guardrail",
    "customer_contract_to_calloff_utilization_margin_bridge_test",
    "battery_material_theme_MFE_vs_contract_volume_and_margin_bridge_test",
    "local_4B_timing_after_battery_material_MFE",
    "hard_4C_non_price_customer_calloff_or_contract_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 87
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
computed_next_round = R4
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R3 is the battery / EV / green mobility round. This run selects C12 because loop86 R3 used C11, loop85 R3 used C14, loop84 R3 used C13, and C12 is the remaining customer-contract / call-off risk route in this rotation.

The tested mechanism:

```text
battery material / customer contract headline
→ confirmed customer contract
→ customer call-off cadence
→ capacity utilization and inventory normalization
→ ASP or raw-material cost spread
→ gross / OP margin conversion
→ durable rerating or call-off-risk fade
```

C12 is the purchase order turning into actual shipment. A contract headline is the doorbell; call-off volume and margin decide whether the truck leaves the dock.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C12 top-covered symbols include `361610`, `393890`, `336370`, `006110`, `011790`, and `003670`. This run avoids that top-covered set and uses:

```text
020150 / 롯데에너지머티리얼즈
121600 / 나노신소재
278280 / 천보
```

All three are treated as new independent C12 battery-customer-contract / call-off-risk cases for this loop.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 020150 | 롯데에너지머티리얼즈 | `atlas/symbol_profiles/020/020150.json` | no profile-level CA candidate |
| 121600 | 나노신소재 | `atlas/symbol_profiles/121/121600.json` | old 2015 CA candidate; selected 2024 forward window clean |
| 278280 | 천보 | `atlas/symbol_profiles/278/278280.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R3L87-C12-01 | 020150 | 2024-02-13 | 35,350 | 180D | clean | true |
| R3L87-C12-02 | 121600 | 2024-02-13 | 100,400 | 180D | clean | true |
| R3L87-C12-03 | 278280 | 2024-02-13 | 88,700 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | COPPER_FOIL_CUSTOMER_CALLOFF_POSITIVE | keep Stage2 with call-off cadence, utilization, ASP/cost spread and margin bridge |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | CNT_CONDUCTIVE_MATERIAL_MFE_BLOWOFF | reject large MFE if call-off / utilization / margin bridge is absent and later MAE is deep |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | ELECTROLYTE_CONTRACT_LOW_MFE_HIGH_MAE | reject low-MFE electrolyte rebound without inventory/call-off/margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R3L87-C12-01 | 020150 | 롯데에너지머티리얼즈 | Stage2-Actionable | 2024-02-13 | 35,350 | 66.62 | -13.72 | current_profile_partially_correct_local_4B_calloff_margin_watch_needed |
| R3L87-C12-02 | 121600 | 나노신소재 | Stage2-FalsePositive | 2024-02-13 | 100,400 | 57.17 | -31.77 | current_profile_false_positive_theme_blowoff_high_MAE |
| R3L87-C12-03 | 278280 | 천보 | Stage2-FalsePositive | 2024-02-13 | 88,700 | 12.51 | -44.76 | current_profile_false_positive_low_MFE_high_MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C12 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: customer contract, call-off cadence, shipment/utilization, inventory normalization, ASP/cost spread, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 020150 | `atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv` | `atlas/symbol_profiles/020/020150.json` |
| 121600 | `atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv` | `atlas/symbol_profiles/121/121600.json` |
| 278280 | `atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv` | `atlas/symbol_profiles/278/278280.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 020150 / 롯데에너지머티리얼즈

C12 copper-foil customer call-off positive with local 4B watch. The February trigger produced a strong MFE into June, but the later August drawdown shows that clean Green requires customer call-off, utilization and margin evidence.

### Case 2 — 121600 / 나노신소재

C12 CNT conductive-material theme MFE / high-MAE false positive. The MFE was large, but the later collapse means it cannot be scored as clean Stage2 without customer call-off and utilization bridge.

### Case 3 — 278280 / 천보

C12 electrolyte contract/call-off low-MFE false positive. The February rebound was small and later drawdown was severe. This rejects electrolyte/customer-contract language without inventory and margin bridge.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 020150 | 35,350 | 48.23 | -2.55 | 66.62 | -2.55 | 66.62 | -13.72 | 2024-06-12 / 58,900 | -48.22 |
| 121600 | 100,400 | 57.17 | -2.19 | 57.17 | -2.19 | 57.17 | -31.77 | 2024-02-22 / 157,800 | -56.59 |
| 278280 | 88,700 | 12.51 | -1.58 | 12.51 | -9.36 | 12.51 | -44.76 | 2024-02-21 / 99,800 | -50.90 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R3L87-C12-01 | Stage2-Actionable if customer/call-off bridge exists | strong MFE, later drawdown | partially correct; local 4B/call-off margin watch needed |
| R3L87-C12-02 | risk of treating battery-material blowoff as Stage2 | large MFE then deep MAE | false positive / high-MAE guardrail |
| R3L87-C12-03 | risk of treating electrolyte rebound as Stage2 | low MFE / severe MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C12, the residual is whether customer-contract MFE becomes clean Stage2/Green before call-off cadence, utilization, inventory normalization and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R3L87-C12-01 | 0.80 | 0.70 | local 4B watch after copper-foil MFE if customer call-off / margin bridge stalls |
| R3L87-C12-02 | 0.35 | 0.30 | CNT material MFE rejected or local-4B-watched without call-off/utilization bridge |
| R3L87-C12-03 | 0.35 | 0.30 | electrolyte contract theme rejected without call-off/inventory/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_customer_calloff_loss_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C12 hard 4C requires confirmed customer call-off loss, order cancellation, inventory impairment, utilization collapse, ASP/cost-spread break or margin thesis break.

## 17. Sector / Canonical Rule Candidate

```text
rule_scope = no_new_global_rule
canonical_archetype_rule_candidate = C12_battery_customer_contract_calloff_utilization_margin_bridge_required
confidence = low
production_scoring_changed = false
shadow_weight_only = true
```

## 18. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 45.43 | -4.70 | may over-credit customer-contract or battery-material MFE | needs C12 call-off/margin bridge repair |
| P1 canonical shadow bridge profile | 3 | keeps 020150 with watch | demotes 121600/278280 | better alignment, source repair required |

## 19. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | canonical rule |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | COPPER_FOIL_CNT_CONDUCTIVE_ELECTROLYTE_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_THEME_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | yes |

## 20. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - battery_material_theme_false_positive_high_MAE
  - customer_contract_calloff_utilization_margin_bridge_required
  - large_MFE_then_calloff_MAE_false_positive
  - low_MFE_electrolyte_contract_false_positive
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_customer_calloff_or_margin_break
new_axis_proposed: false
existing_axis_strengthened:
  - C12_battery_customer_contract_calloff_utilization_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
do_not_propose_new_weight_delta: true
```

## 21. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- customer contract or call-off schedule
- shipment/utilization evidence
- inventory normalization
- ASP/cost spread and margin conversion
- production scoring implementation
```

## 22. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C12_battery_customer_contract_calloff_utilization_margin_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"Require confirmed customer contract, call-off cadence, capacity utilization, inventory normalization, ASP/cost spread and gross/OP margin conversion before clean Stage2/Green","keeps 020150 with local 4B/call-off margin watch; demotes 121600/278280 high-MAE call-off-risk false positives","R3L87-C12-01-S2A-20240213|R3L87-C12-02-S2FP-20240213|R3L87-C12-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 23. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L87-C12-01", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": 87, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CNT_CONDUCTIVE_ELECTROLYTE_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_THEME_FADE", "case_type": "copper_foil_customer_contract_calloff_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L87-C12-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "copper_foil_MFE_positive_but_customer_calloff_utilization_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_calloff_margin_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C12 copper-foil positives need customer contract, call-off cadence, utilization, ASP/copper-spread and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R3L87-C12-01-S2A-20240213", "case_id": "R3L87-C12-01", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": 87, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CNT_CONDUCTIVE_ELECTROLYTE_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail|calloff_utilization_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "copper foil / battery customer contract / call-off recovery and utilization proxy; primary customer call-off and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["customer_contract_proxy", "battery_material_theme_proxy", "calloff_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_customer_contract", "calloff_cadence", "capacity_utilization", "inventory_normalization", "ASP_or_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["battery_material_MFE_without_calloff_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_customer_calloff_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 35350, "MFE_30D_pct": 48.23, "MAE_30D_pct": -2.55, "MFE_90D_pct": 66.62, "MAE_90D_pct": -2.55, "MFE_180D_pct": 66.62, "MAE_180D_pct": -13.72, "peak_date": "2024-06-12", "peak_price": 58900, "drawdown_after_peak_pct": -48.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "local_4B_watch_after_copper_foil_MFE_if_customer_calloff_utilization_margin_bridge_stalls", "four_b_evidence_type": ["battery_material_MFE_without_customer_calloff_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_customer_calloff_loss_or_margin_break", "trigger_outcome_label": "copper_foil_MFE_positive_but_customer_calloff_utilization_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_calloff_margin_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R3L87-C12-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L87-C12-01", "trigger_id": "R3L87-C12-01-S2A-20240213", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_visibility_score": 50, "calloff_cadence_score": 40, "capacity_utilization_score": 40, "inventory_normalization_score": 35, "ASP_or_cost_spread_score": 35, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "relative_strength_score": 65, "valuation_blowoff_risk_score": 70, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"customer_contract_visibility_score": 50, "calloff_cadence_score": 40, "capacity_utilization_score": 40, "inventory_normalization_score": 35, "ASP_or_cost_spread_score": 35, "gross_margin_bridge_score": 40, "customer_quality_score": 45, "relative_strength_score": 65, "valuation_blowoff_risk_score": 82, "execution_risk_score": 60, "source_quality_score": 10, "4B_watch_score": 85, "4C_watch_score": 25}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/customer-calloff margin watch", "changed_components": ["customer_contract_visibility_score", "calloff_cadence_score", "capacity_utilization_score", "inventory_normalization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C12 requires battery customer-contract MFE to convert into customer call-off cadence, utilization, inventory normalization, ASP/cost spread and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 66.62, "MAE_90D_pct": -2.55, "score_return_alignment_label": "copper_foil_MFE_positive_but_customer_calloff_utilization_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_calloff_margin_watch_needed"}
{"row_type": "case", "case_id": "R3L87-C12-02", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": 87, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CNT_CONDUCTIVE_ELECTROLYTE_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_THEME_FADE", "case_type": "CNT_conductive_material_theme_MFE_then_calloff_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L87-C12-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_material_MFE_then_deep_MAE_customer_calloff_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Battery material MFE should not validate C12 unless customer call-off, shipment utilization, ASP/cost spread and margin conversion are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R3L87-C12-02-S2FP-20240213", "case_id": "R3L87-C12-02", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": 87, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CNT_CONDUCTIVE_ELECTROLYTE_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail|calloff_utilization_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "CNT conductive material / battery material customer expansion proxy without confirmed call-off, utilization and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["customer_contract_proxy", "battery_material_theme_proxy", "calloff_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_customer_contract", "calloff_cadence", "capacity_utilization", "inventory_normalization", "ASP_or_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["battery_material_MFE_without_calloff_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_customer_calloff_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv", "profile_path": "atlas/symbol_profiles/121/121600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 100400, "MFE_30D_pct": 57.17, "MAE_30D_pct": -2.19, "MFE_90D_pct": 57.17, "MAE_90D_pct": -2.19, "MFE_180D_pct": 57.17, "MAE_180D_pct": -31.77, "peak_date": "2024-02-22", "peak_price": 157800, "drawdown_after_peak_pct": -56.59, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "CNT_material_MFE_rejected_or_local_4B_watch_without_customer_calloff_utilization_margin_bridge", "four_b_evidence_type": ["battery_material_MFE_without_customer_calloff_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_customer_calloff_loss_or_margin_break", "trigger_outcome_label": "large_material_MFE_then_deep_MAE_customer_calloff_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2015_CA_candidate", "same_entry_group_id": "R3L87-C12-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L87-C12-02", "trigger_id": "R3L87-C12-02-S2FP-20240213", "symbol": "121600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_visibility_score": 20, "calloff_cadence_score": 5, "capacity_utilization_score": 5, "inventory_normalization_score": 10, "ASP_or_cost_spread_score": 5, "gross_margin_bridge_score": 5, "customer_quality_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 80, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"customer_contract_visibility_score": 20, "calloff_cadence_score": 0, "capacity_utilization_score": 0, "inventory_normalization_score": 0, "ASP_or_cost_spread_score": 0, "gross_margin_bridge_score": 0, "customer_quality_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 80, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 92, "4C_watch_score": 70}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Battery customer-calloff RiskWatch", "changed_components": ["customer_contract_visibility_score", "calloff_cadence_score", "capacity_utilization_score", "inventory_normalization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C12 requires battery customer-contract MFE to convert into customer call-off cadence, utilization, inventory normalization, ASP/cost spread and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 57.17, "MAE_90D_pct": -2.19, "score_return_alignment_label": "large_material_MFE_then_deep_MAE_customer_calloff_false_positive", "current_profile_verdict": "current_profile_false_positive_theme_blowoff_high_MAE"}
{"row_type": "case", "case_id": "R3L87-C12-03", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": 87, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CNT_CONDUCTIVE_ELECTROLYTE_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_THEME_FADE", "case_type": "electrolyte_customer_contract_calloff_low_MFE_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R3L87-C12-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_deep_MAE_electrolyte_contract_calloff_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Electrolyte/customer-contract rebound should remain RiskWatch unless call-off cadence, inventory normalization, utilization and margin bridge are source-repaired."}
{"row_type": "trigger", "trigger_id": "R3L87-C12-03-S2FP-20240213", "case_id": "R3L87-C12-03", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": 87, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CNT_CONDUCTIVE_ELECTROLYTE_CUSTOMER_CONTRACT_CALLOFF_UTILIZATION_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail|calloff_utilization_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "electrolyte/additive customer contract and EV demand recovery proxy without confirmed call-off, inventory and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["customer_contract_proxy", "battery_material_theme_proxy", "calloff_or_margin_proxy"], "stage3_evidence_fields": ["confirmed_customer_contract", "calloff_cadence", "capacity_utilization", "inventory_normalization", "ASP_or_cost_spread", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["battery_material_MFE_without_calloff_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_customer_calloff_loss_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv", "profile_path": "atlas/symbol_profiles/278/278280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 88700, "MFE_30D_pct": 12.51, "MAE_30D_pct": -1.58, "MFE_90D_pct": 12.51, "MAE_90D_pct": -9.36, "MFE_180D_pct": 12.51, "MAE_180D_pct": -44.76, "peak_date": "2024-02-21", "peak_price": 99800, "drawdown_after_peak_pct": -50.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "electrolyte_customer_contract_theme_rejected_without_calloff_inventory_margin_bridge", "four_b_evidence_type": ["battery_material_MFE_without_customer_calloff_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_customer_calloff_loss_or_margin_break", "trigger_outcome_label": "low_MFE_deep_MAE_electrolyte_contract_calloff_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R3L87-C12-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L87-C12-03", "trigger_id": "R3L87-C12-03-S2FP-20240213", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_visibility_score": 20, "calloff_cadence_score": 5, "capacity_utilization_score": 5, "inventory_normalization_score": 10, "ASP_or_cost_spread_score": 5, "gross_margin_bridge_score": 5, "customer_quality_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 80, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"customer_contract_visibility_score": 20, "calloff_cadence_score": 0, "capacity_utilization_score": 0, "inventory_normalization_score": 0, "ASP_or_cost_spread_score": 0, "gross_margin_bridge_score": 0, "customer_quality_score": 20, "relative_strength_score": 45, "valuation_blowoff_risk_score": 80, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 92, "4C_watch_score": 70}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Battery customer-calloff RiskWatch", "changed_components": ["customer_contract_visibility_score", "calloff_cadence_score", "capacity_utilization_score", "inventory_normalization_score", "ASP_or_cost_spread_score", "gross_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C12 requires battery customer-contract MFE to convert into customer call-off cadence, utilization, inventory normalization, ASP/cost spread and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 12.51, "MAE_90D_pct": -9.36, "score_return_alignment_label": "low_MFE_deep_MAE_electrolyte_contract_calloff_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE"}
{"row_type": "shadow_weight", "axis": "C12_battery_customer_contract_calloff_utilization_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Battery customer-contract rerating requires confirmed customer contract, call-off cadence, capacity utilization, inventory normalization, ASP/cost spread and gross/OP margin conversion; battery-material MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 020150 with local 4B/call-off margin watch; demotes 121600/278280 high-MAE call-off-risk false positives", "trigger_ids": "R3L87-C12-01-S2A-20240213|R3L87-C12-02-S2FP-20240213|R3L87-C12-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R3", "loop": 87, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["battery_material_theme_false_positive_high_MAE", "customer_contract_calloff_utilization_margin_bridge_required", "large_MFE_then_calloff_MAE_false_positive", "low_MFE_electrolyte_contract_false_positive", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_customer_calloff_or_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 24. Deferred Coding Agent Handoff Prompt

Use only `calibration_usable=true` rows. Do not treat `source_proxy_only/evidence_url_pending` rows as runtime promotion-ready. For C12, test a canonical guard requiring customer contract, call-off cadence, capacity utilization, inventory normalization, ASP/cost spread and gross/OP margin conversion before clean Stage2/Green.

## 25. Next Round State

```text
completed_round = R3
completed_loop = 87
next_round = R4
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 26. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
