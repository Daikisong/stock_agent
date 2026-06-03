# E2R Stock-Web v12 Residual Research — R4 Loop 86 / L4 / C16

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 86,
  "computed_next_round": "R5",
  "computed_next_loop": 86,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "strategic_resource_policy_supply_guardrail",
    "resource_policy_theme_vs_direct_beneficiary_project_economics_test",
    "copper_defense_material_spread_positive_vs_rare_earth_nickel_theme_fade",
    "local_4B_timing_after_resource_policy_MFE",
    "hard_4C_non_price_policy_or_supply_break_protection",
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
scheduled_round = R4
scheduled_loop = 86
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
computed_next_round = R5
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R4 is the materials / spread / resource round. This run selects C16 because loop84 used C15, loop85 used C17, and C16 remains the strategic-resource policy/supply bridge slot for loop86.

The tested mechanism:

```text
strategic resource / copper / rare earth / nickel supply headline
→ direct beneficiary mapping
→ realized resource or product spread
→ inventory valuation and supply/customer demand
→ utilization
→ gross / OP margin conversion
→ durable rerating or theme fade
```

C16 is not a metal headline. It is the refinery gate: the policy signal must become spread, inventory, customers and margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C16 top-covered symbols include `001570`, `005490`, `000910`, `075970`, `005290`, and `081150`. This run avoids that top-covered set and uses:

```text
103140 / 풍산
047400 / 유니온머티리얼
032560 / 황금에스티
```

All three are treated as new independent C16 strategic-resource policy/supply cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 103140 | 풍산 | `atlas/symbol_profiles/103/103140.json` | no profile-level CA candidate |
| 047400 | 유니온머티리얼 | `atlas/symbol_profiles/047/047400.json` | old 2011 CA candidate; selected 2024 forward window clean |
| 032560 | 황금에스티 | `atlas/symbol_profiles/032/032560.json` | old CA candidates through 2010; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R4L86-C16-01 | 103140 | 2024-03-07 | 46,100 | 180D | clean | true |
| R4L86-C16-02 | 047400 | 2024-05-13 | 2,895 | 180D | clean | true |
| R4L86-C16-03 | 032560 | 2024-05-20 | 7,070 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_DEFENSE_MATERIAL_SPREAD_POSITIVE | keep Stage2 only with realized copper/product spread, inventory and margin bridge |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | RARE_EARTH_PERMANENT_MAGNET_THEME_FADE | reject low-MFE rare-earth theme without direct supply/customer/margin bridge |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | NICKEL_STAINLESS_RESOURCE_VALUE_TRAP | reject strategic-material theme spike without utilization, product spread and margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R4L86-C16-01 | 103140 | 풍산 | Stage2-Actionable | 2024-03-07 | 46,100 | 68.33 | -3.9 | current_profile_partially_correct_local_4B_watch_needed |
| R4L86-C16-02 | 047400 | 유니온머티리얼 | Stage2-FalsePositive | 2024-05-13 | 2,895 | 6.56 | -29.53 | current_profile_false_positive_low_MFE_high_MAE |
| R4L86-C16-03 | 032560 | 황금에스티 | Stage2-FalsePositive | 2024-05-20 | 7,070 | 9.48 | -25.88 | current_profile_false_positive_low_MFE_value_trap |

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

This MD creates a source-repair queue and a C16 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: strategic-resource policy source, resource price/spread data, inventory valuation, supply/customer contract, utilization, product-spread bridge, gross/OP margin bridge, disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 103140 | `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv` | `atlas/symbol_profiles/103/103140.json` |
| 047400 | `atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv` | `atlas/symbol_profiles/047/047400.json` |
| 032560 | `atlas/ohlcv_tradable_by_symbol_year/032/032560/2024.csv` | `atlas/symbol_profiles/032/032560.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 103140 / 풍산

C16 copper / strategic-material positive with local 4B watch. The March trigger produced a large MFE into the copper/material spread cycle, but it still needs product-spread, inventory and margin evidence before clean Green.

### Case 2 — 047400 / 유니온머티리얼

C16 rare-earth / permanent-magnet theme false positive. The MFE was small and the later MAE widened. Strategic supply-chain language without direct contract, price spread and margin bridge should not validate Stage2.

### Case 3 — 032560 / 황금에스티

C16 nickel/stainless material theme value trap. The spike was small and short, while the later drawdown was much larger. This rejects strategic-material theme heat without utilization and product-spread evidence.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 103140 | 46,100 | 46.42 | -3.90 | 68.33 | -3.90 | 68.33 | -3.90 | 2024-05-13 / 77,600 | -31.83 |
| 047400 | 2,895 | 6.56 | -10.88 | 6.56 | -29.53 | 6.56 | -29.53 | 2024-05-17 / 3,085 | -33.87 |
| 032560 | 7,070 | 9.48 | -10.18 | 9.48 | -24.47 | 9.48 | -25.88 | 2024-05-20 / 7,740 | -32.30 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R4L86-C16-01 | Stage2-Actionable if copper/spread bridge exists | large MFE, later drawdown | partially correct; local 4B/resource-spread watch needed |
| R4L86-C16-02 | risk of treating rare-earth policy theme as Stage2 | low MFE / high MAE | false positive |
| R4L86-C16-03 | risk of treating nickel/stainless strategic-material spike as Stage2 | low MFE / value trap MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C16, the residual is whether resource-policy MFE becomes clean Stage2/Green before direct beneficiary mapping, product spread, inventory and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R4L86-C16-01 | 0.82 | 0.72 | local 4B watch after copper resource MFE if product-spread/inventory/margin bridge stalls |
| R4L86-C16-02 | 0.35 | 0.30 | rare-earth policy theme rejected without direct supply/price/margin bridge |
| R4L86-C16-03 | 0.35 | 0.30 | nickel/stainless material theme rejected without inventory/utilization/product-spread bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_policy_supply_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C16 hard 4C requires confirmed policy reversal, resource-price spread collapse, supply contract break, utilization deterioration, inventory impairment or margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L4/C16 strategic-resource rows need direct beneficiary mapping, realized resource/product spread, inventory valuation, supply/customer demand, utilization and margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
candidate_axis = C16_strategic_resource_direct_beneficiary_spread_inventory_margin_bridge_required
effect = keep copper/resource positive with local 4B watch; demote rare-earth/nickel strategic-material theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 28.12 | -19.30 | may over-credit strategic-resource theme MFE | needs C16 spread/inventory/margin bridge repair |
| P1 canonical shadow bridge profile | 3 | 68.33 on kept positive | -3.90 on kept positive | demotes 047400/032560 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R4L86-C16-01 | 78 | Stage2-Actionable | 74 | Stage2-Actionable + local 4B/resource-spread watch | partially aligned |
| R4L86-C16-02 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Strategic-resource theme RiskWatch | improved |
| R4L86-C16-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Strategic-resource theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

## 22. Residual Contribution Summary

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
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - strategic_resource_theme_false_positive_high_MAE
  - direct_beneficiary_spread_inventory_margin_bridge_required
  - low_MFE_resource_theme_value_trap
  - source_proxy_runtime_promotion_risk
  - local_4B_late_after_resource_spread_MFE
new_axis_proposed: false
existing_axis_strengthened:
  - C16_strategic_resource_direct_beneficiary_spread_inventory_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C16_strategic_resource_direct_beneficiary_spread_inventory_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

## 23. Validation Scope / Non-Validation Scope

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
- strategic-resource policy source
- resource price / product spread source
- inventory valuation and utilization
- supply/customer contract evidence
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_strategic_resource_direct_beneficiary_spread_inventory_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"Require direct beneficiary mapping, realized resource/product spread, inventory valuation, supply/customer demand, utilization and gross/OP margin conversion before clean Stage2/Green","keeps 103140 with local 4B/resource-spread watch; demotes 047400/032560","R4L86-C16-01-S2A-20240307|R4L86-C16-02-S2FP-20240513|R4L86-C16-03-S2FP-20240520",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R4L86-C16-01", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": 86, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "copper_strategic_material_defense_supply_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L86-C16-01-S2A-20240307", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_MFE_but_resource_spread_project_economics_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C16 can keep Stage2 only when strategic-resource policy/supply evidence converts into realized product spread, inventory valuation, customer demand and margin bridge."}
{"row_type": "trigger", "trigger_id": "R4L86-C16-01-S2A-20240307", "case_id": "R4L86-C16-01", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": 86, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail|direct_beneficiary_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-07", "evidence_available_at_that_date": "copper / strategic material supply / defense-material spread proxy; primary copper-price, inventory and product-spread evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["strategic_resource_policy_proxy", "resource_price_or_supply_proxy", "direct_beneficiary_proxy"], "stage3_evidence_fields": ["realized_resource_or_product_spread", "inventory_valuation", "supply_contract_or_customer_demand", "utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["resource_policy_MFE_without_margin_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_supply_contract_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-07", "entry_price": 46100, "MFE_30D_pct": 46.42, "MFE_90D_pct": 68.33, "MFE_180D_pct": 68.33, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.9, "MAE_90D_pct": -3.9, "MAE_180D_pct": -3.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-13", "peak_price": 77600, "drawdown_after_peak_pct": -31.83, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_copper_resource_MFE_if_product_spread_inventory_margin_bridge_stalls", "four_b_evidence_type": ["resource_policy_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_supply_or_margin_break", "trigger_outcome_label": "large_positive_MFE_but_resource_spread_project_economics_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R4L86-C16-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L86-C16-01", "trigger_id": "R4L86-C16-01-S2A-20240307", "symbol": "103140", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_specificity_score": 45, "direct_beneficiary_mapping_score": 45, "resource_price_or_spread_score": 55, "inventory_valuation_score": 40, "supply_contract_or_customer_score": 40, "utilization_score": 40, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 65, "valuation_blowoff_risk_score": 65, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"policy_specificity_score": 45, "direct_beneficiary_mapping_score": 45, "resource_price_or_spread_score": 55, "inventory_valuation_score": 40, "supply_contract_or_customer_score": 40, "utilization_score": 40, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 65, "valuation_blowoff_risk_score": 75, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + local 4B/resource-spread watch", "changed_components": ["direct_beneficiary_mapping_score", "resource_price_or_spread_score", "inventory_valuation_score", "supply_contract_or_customer_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C16 requires strategic-resource policy/supply signal to convert into direct beneficiary mapping, realized product/resource spread, inventory valuation, supply contract/customer demand, utilization and margin bridge before clean Stage2/Green; strategic-resource theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 68.33, "MAE_90D_pct": -3.9, "score_return_alignment_label": "large_positive_MFE_but_resource_spread_project_economics_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R4L86-C16-02", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": 86, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "rare_earth_permanent_magnet_policy_theme_low_MFE_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L86-C16-02-S2FP-20240513", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_rare_earth_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Rare-earth/permanent magnet policy theme should remain RiskWatch unless direct beneficiary mapping, contract linkage, price spread and gross-margin bridge are explicit."}
{"row_type": "trigger", "trigger_id": "R4L86-C16-02-S2FP-20240513", "case_id": "R4L86-C16-02", "symbol": "047400", "company_name": "유니온머티리얼", "round": "R4", "loop": 86, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail|direct_beneficiary_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-05-13", "evidence_available_at_that_date": "rare-earth / permanent magnet / strategic supply-chain policy theme proxy without direct supply contract, price spread or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["strategic_resource_policy_proxy", "resource_price_or_supply_proxy", "direct_beneficiary_proxy"], "stage3_evidence_fields": ["realized_resource_or_product_spread", "inventory_valuation", "supply_contract_or_customer_demand", "utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["resource_policy_MFE_without_margin_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_supply_contract_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv", "profile_path": "atlas/symbol_profiles/047/047400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-13", "entry_price": 2895, "MFE_30D_pct": 6.56, "MFE_90D_pct": 6.56, "MFE_180D_pct": 6.56, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.88, "MAE_90D_pct": -29.53, "MAE_180D_pct": -29.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-17", "peak_price": 3085, "drawdown_after_peak_pct": -33.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "rare_earth_policy_theme_rejected_without_direct_supply_price_margin_bridge", "four_b_evidence_type": ["resource_policy_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_supply_or_margin_break", "trigger_outcome_label": "low_MFE_high_MAE_rare_earth_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2011_CA_candidate", "same_entry_group_id": "R4L86-C16-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L86-C16-02", "trigger_id": "R4L86-C16-02-S2FP-20240513", "symbol": "047400", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_specificity_score": 30, "direct_beneficiary_mapping_score": 10, "resource_price_or_spread_score": 10, "inventory_valuation_score": 5, "supply_contract_or_customer_score": 5, "utilization_score": 10, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 30, "valuation_blowoff_risk_score": 65, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_specificity_score": 30, "direct_beneficiary_mapping_score": 0, "resource_price_or_spread_score": 0, "inventory_valuation_score": 0, "supply_contract_or_customer_score": 0, "utilization_score": 10, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 30, "valuation_blowoff_risk_score": 65, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Strategic-resource theme RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "resource_price_or_spread_score", "inventory_valuation_score", "supply_contract_or_customer_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C16 requires strategic-resource policy/supply signal to convert into direct beneficiary mapping, realized product/resource spread, inventory valuation, supply contract/customer demand, utilization and margin bridge before clean Stage2/Green; strategic-resource theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 6.56, "MAE_90D_pct": -29.53, "score_return_alignment_label": "low_MFE_high_MAE_rare_earth_policy_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE"}
{"row_type": "case", "case_id": "R4L86-C16-03", "symbol": "032560", "company_name": "황금에스티", "round": "R4", "loop": 86, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "nickel_stainless_strategic_material_theme_low_MFE_value_trap", "positive_or_counterexample": "counterexample", "best_trigger": "R4L86-C16-03-S2FP-20240520", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_spike_low_MFE_later_MAE_strategic_material_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_value_trap", "price_source": "Songdaiki/stock-web", "notes": "Strategic nickel/stainless material theme is not Stage2 without inventory, utilization, customer demand, product spread and margin conversion."}
{"row_type": "trigger", "trigger_id": "R4L86-C16-03-S2FP-20240520", "case_id": "R4L86-C16-03", "symbol": "032560", "company_name": "황금에스티", "round": "R4", "loop": 86, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_RARE_EARTH_NICKEL_STRATEGIC_RESOURCE_POLICY_SUPPLY_PROJECT_ECONOMICS_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail|direct_beneficiary_spread_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-05-20", "evidence_available_at_that_date": "nickel/stainless strategic material and resource-supply theme proxy without realized spread, utilization or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["strategic_resource_policy_proxy", "resource_price_or_supply_proxy", "direct_beneficiary_proxy"], "stage3_evidence_fields": ["realized_resource_or_product_spread", "inventory_valuation", "supply_contract_or_customer_demand", "utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["resource_policy_MFE_without_margin_bridge", "theme_spike_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_policy_reversal_or_supply_contract_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032560/2024.csv", "profile_path": "atlas/symbol_profiles/032/032560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-20", "entry_price": 7070, "MFE_30D_pct": 9.48, "MFE_90D_pct": 9.48, "MFE_180D_pct": 9.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.18, "MAE_90D_pct": -24.47, "MAE_180D_pct": -25.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-20", "peak_price": 7740, "drawdown_after_peak_pct": -32.3, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "nickel_stainless_material_theme_rejected_without_inventory_utilization_product_spread_margin_bridge", "four_b_evidence_type": ["resource_policy_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_policy_supply_or_margin_break", "trigger_outcome_label": "theme_spike_low_MFE_later_MAE_strategic_material_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_value_trap", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2010_CA_candidates", "same_entry_group_id": "R4L86-C16-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L86-C16-03", "trigger_id": "R4L86-C16-03-S2FP-20240520", "symbol": "032560", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"policy_specificity_score": 30, "direct_beneficiary_mapping_score": 10, "resource_price_or_spread_score": 10, "inventory_valuation_score": 5, "supply_contract_or_customer_score": 5, "utilization_score": 10, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 30, "valuation_blowoff_risk_score": 65, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"policy_specificity_score": 30, "direct_beneficiary_mapping_score": 0, "resource_price_or_spread_score": 0, "inventory_valuation_score": 0, "supply_contract_or_customer_score": 0, "utilization_score": 10, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 30, "valuation_blowoff_risk_score": 65, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Strategic-resource theme RiskWatch", "changed_components": ["direct_beneficiary_mapping_score", "resource_price_or_spread_score", "inventory_valuation_score", "supply_contract_or_customer_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C16 requires strategic-resource policy/supply signal to convert into direct beneficiary mapping, realized product/resource spread, inventory valuation, supply contract/customer demand, utilization and margin bridge before clean Stage2/Green; strategic-resource theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 9.48, "MAE_90D_pct": -24.47, "score_return_alignment_label": "theme_spike_low_MFE_later_MAE_strategic_material_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_value_trap"}
{"row_type": "shadow_weight", "axis": "C16_strategic_resource_direct_beneficiary_spread_inventory_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Strategic-resource policy/supply rerating requires direct beneficiary mapping, realized resource or product spread, inventory valuation, supply/customer demand, utilization and gross/OP margin conversion; theme MFE without bridge fades into high MAE or low-MFE value trap.", "backtest_effect": "keeps 103140 with local 4B/resource-spread watch; demotes 047400/032560 strategic-resource theme false positives", "trigger_ids": "R4L86-C16-01-S2A-20240307|R4L86-C16-02-S2FP-20240513|R4L86-C16-03-S2FP-20240520", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R4", "loop": 86, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["strategic_resource_theme_false_positive_high_MAE", "direct_beneficiary_spread_inventory_margin_bridge_required", "low_MFE_resource_theme_value_trap", "source_proxy_runtime_promotion_risk", "local_4B_late_after_resource_spread_MFE"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion-ready.
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.
- For C16, test a canonical-archetype guard requiring direct beneficiary mapping, realized resource/product spread, inventory valuation, supply/customer demand, utilization and revenue/gross-margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 86
next_round = R5
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
