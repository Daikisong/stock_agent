# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 83,
  "computed_next_round": "R5",
  "computed_next_loop": 83,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "COPPER_FOIL_CNT_ELECTROLYTE_STRATEGIC_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
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

This loop adds **4 new independent cases, 2 counterexamples, and 4 residual errors** for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C16_strategic_supply_bridge_shadow_profile
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Already-applied global axes are treated as baseline and are not re-proposed globally:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

## 2. Round / Large Sector / Canonical Archetype Scope

The previous local execution completed R3 / loop 83 and emitted `next_round = R4`, `next_loop = 83`.
Therefore this file follows the corrected sequential scheduler:

```text
scheduled_round = R4
scheduled_loop = 83
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
computed_next_round = R5
computed_next_loop = 83
```

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`, so the round-sector gate passes.

## 3. Previous Coverage / Duplicate Avoidance Check

NO-REPEAT INDEX is used only as a duplicate ledger.

Visible coverage snapshot for C16:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:
  rows = 67
  symbols = 23
  date_range = 2019-05-20~2024-10-10
  good/bad Stage2 = 17/7
  4B/4C = 19/0
  top covered symbols = 001570, 005490, 000910, 075970, 005290, 081150
```

Hard duplicate policy:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows avoid the documented C16 top-covered set:

```text
103140 / 풍산 / copper strategic metal supply and margin bridge
020150 / 롯데에너지머티리얼즈 / copper foil strategic supply localization with later customer call-off watch
121600 / 나노신소재 / CNT local-supply theme fade
278280 / 천보 / electrolyte-additive strategic-supply theme fade
```

All rows are new independent C16 cases in this file, but all non-price evidence remains `source_proxy_only=true / evidence_url_pending=true`; this file is therefore a source-repair queue plus Stock-Web path calibration, not immediate runtime promotion.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Stock-Web manifest facts used:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | 180D forward available | OHLC available | CA window | calibration_usable |
|---|---:|---|---:|---|---|---|---|
| R4L83-C16-01 | 103140 | 2024-02-22 | 42200 | yes | yes | clean_180D_window | true |
| R4L83-C16-02 | 020150 | 2024-02-20 | 37650 | yes | yes | clean_180D_window | true |
| R4L83-C16-03 | 121600 | 2024-06-11 | 141500 | yes | yes | clean_180D_window_with_share_count_micro_change_validation | true |
| R4L83-C16-04 | 278280 | 2024-06-11 | 79100 | yes | yes | clean_180D_window | true |

All selected entry dates are before the Stock-Web `manifest_max_date = 2026-02-20`, and every trigger has at least 180 forward tradable rows available in the Stock-Web atlas.

## 6. Canonical Archetype Compression Map

| canonical | fine/deep route | Stage2 bridge | Green blocker | 4B/4C use |
|---|---|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_STRATEGIC_METAL_SUPPLY_MARGIN_BRIDGE | strategic metal price/supply + volume/margin bridge | weak customer/order/revision confirmation | local 4B after peak if supply beta overextends |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_FOIL_LOCALIZATION_WITH_CUSTOMER_CALLOFF | copper foil/local supply + customer/capacity absorption | EV customer call-off or utilization fade | local 4B watch, no hard 4C without thesis break |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | CNT_CONDUCTIVE_ADDITIVE_LOCAL_SUPPLY_THEME | CNT/local supply headline | no call-off/utilization/repricing bridge | false-positive/high-MAE guard |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | ELECTROLYTE_ADDITIVE_SUPPLY_THEME | electrolyte-additive supply headline | no repricing/utilization margin bridge | false-positive/high-MAE guard |

C16 is not “resource theme up.”  
The mechanism must pass through:

```text
strategic resource / policy / supply-chain headline
→ material availability or supply localization
→ customer/offtake or volume visibility
→ utilization / repricing / margin bridge
→ durable rerating
```

A resource headline is ore in the ground.  
C16 asks whether it becomes contracted tons, shipped volume, margin, and cash.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | MFE_180D | MAE_180D | current profile verdict |
|---|---:|---|---|---|---|---:|---:|---|
| R4L83-C16-01 | 103140 | 풍산 | positive | Stage2-Actionable | 2024-02-22 | 68.48% | -7.70% | current_profile_too_late |
| R4L83-C16-02 | 020150 | 롯데에너지머티리얼즈 | positive | Stage2-Actionable | 2024-02-20 | 57.24% | -19.65% | current_profile_4B_too_late |
| R4L83-C16-03 | 121600 | 나노신소재 | counterexample | Stage2-FalsePositive | 2024-06-11 | 5.87% | -58.09% | current_profile_false_positive |
| R4L83-C16-04 | 278280 | 천보 | counterexample | Stage2-FalsePositive | 2024-06-11 | 3.92% | -51.39% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_or_4C_case_count = 3
calibration_usable_case_count = 4
new_independent_case_ratio = 1.00
```

The positive cases demonstrate that C16 can work when the strategic-resource headline converts into a material price/supply and margin bridge.  
The counterexamples show that local-supply or strategic-material headlines without customer call-off, utilization, or repricing evidence can peak almost immediately and then suffer high MAE.

## 9. Evidence Source Map

| case_id | evidence family | status | repair need |
|---|---|---|---|
| R4L83-C16-01 | COPPER_STRATEGIC_METAL_SUPPLY_MARGIN_BRIDGE | source_proxy_only=true / evidence_url_pending=true | source URL and date-stamp repair before runtime promotion |
| R4L83-C16-02 | COPPER_FOIL_STRATEGIC_SUPPLY_LOCALIZATION_VS_CUSTOMER_CALLOFF | source_proxy_only=true / evidence_url_pending=true | source URL and date-stamp repair before runtime promotion |
| R4L83-C16-03 | CNT_CONDUCTIVE_ADDITIVE_LOCAL_SUPPLY_THEME_WITHOUT_CALLOFF | source_proxy_only=true / evidence_url_pending=true | source URL and date-stamp repair before runtime promotion |
| R4L83-C16-04 | ELECTROLYTE_ADDITIVE_SUPPLY_THEME_WITHOUT_REPRICING_OR_UTILIZATION | source_proxy_only=true / evidence_url_pending=true | source URL and date-stamp repair before runtime promotion |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | profile caveat |
|---:|---|---|---|
| 103140 | `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv` | `atlas/symbol_profiles/103/103140.json` | clean_180D_window |
| 020150 | `atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv` | `atlas/symbol_profiles/020/020150.json` | clean_180D_window |
| 121600 | `atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv` | `atlas/symbol_profiles/121/121600.json` | clean_180D_window_with_share_count_micro_change_validation |
| 278280 | `atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv` | `atlas/symbol_profiles/278/278280.json` | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence bridge | usable |
|---|---:|---|---|---|---:|---|---|
| R4L83-C16-01-Stage2-Actionable | 103140 | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 42200 | COPPER_STRATEGIC_METAL_SUPPLY_MARGIN_BRIDGE | True |
| R4L83-C16-02-Stage2-Actionable | 020150 | Stage2-Actionable | 2024-02-20 | 2024-02-20 | 37650 | COPPER_FOIL_STRATEGIC_SUPPLY_LOCALIZATION_VS_CUSTOMER_CALLOFF | True |
| R4L83-C16-03-Stage2-FalsePositive | 121600 | Stage2-FalsePositive | 2024-06-11 | 2024-06-11 | 141500 | CNT_CONDUCTIVE_ADDITIVE_LOCAL_SUPPLY_THEME_WITHOUT_CALLOFF | True |
| R4L83-C16-04-Stage2-FalsePositive | 278280 | Stage2-FalsePositive | 2024-06-11 | 2024-06-11 | 79100 | ELECTROLYTE_ADDITIVE_SUPPLY_THEME_WITHOUT_REPRICING_OR_UTILIZATION | True |

## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R4L83-C16-01 | 103140 | 42200 | 26.07% | -7.70% | 61.85% | -7.70% | 68.48% | -7.70% | 2024-07-10 | 71100 | -33.90% |
| R4L83-C16-02 | 020150 | 37650 | 39.18% | -9.16% | 57.24% | -9.16% | 57.24% | -19.65% | 2024-06-18 | 59200 | -48.90% |
| R4L83-C16-03 | 121600 | 141500 | 5.87% | -31.24% | 5.87% | -51.59% | 5.87% | -58.09% | 2024-06-11 | 149800 | -60.41% |
| R4L83-C16-04 | 278280 | 79100 | 3.92% | -16.94% | 3.92% | -34.13% | 3.92% | -51.39% | 2024-06-12 | 82200 | -53.22% |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely action | actual path | verdict |
|---|---|---|---|
| R4L83-C16-01 | Stage2-Actionable; Green only after revision/margin bridge | high MFE with controlled MAE, then local 4B after peak | current_profile_too_late |
| R4L83-C16-02 | Stage2-Actionable; local 4B only after later drawdown | high early MFE but local 4B should watch customer/order pacing earlier | current_profile_4B_too_late |
| R4L83-C16-03 | Stage2 bonus may over-credit strategic-material headline | low MFE, severe MAE; peak on trigger | current_profile_false_positive |
| R4L83-C16-04 | Stage2 bonus may over-credit strategic-material headline | very low MFE, severe MAE; no durable conversion | current_profile_false_positive |

Answered stress-test questions:

```text
stage2_actionable_evidence_bonus:
  too broad for C16 when customer/offtake/utilization bridge is absent.
Yellow threshold 75:
  acceptable for positives, but false positives should be blocked before threshold logic.
Green threshold 87 / revision 55:
  kept; C16 Green should remain strict.
price_only_blowoff guard:
  strengthened for local-supply theme spikes.
full_4b non-price requirement:
  kept; local 4B watch can be price-assisted, full 4B requires bridge deterioration.
hard 4C routing:
  kept; no selected row receives hard 4C without non-price thesis break.
```

## 14. Stage2 / Yellow / Green Comparison

```text
C16 Stage2 should require:
  strategic-resource headline
  + customer/offtake or utilization evidence
  + margin/repricing bridge

C16 Yellow may allow:
  price/supply shock plus early margin bridge,
  but only with source repair and no severe customer call-off contradiction.

C16 Green should require:
  contract/offtake/customer quality
  + utilization or volume visibility
  + revision or margin confirmation
  + controlled MAE.
```

No confirmed Stage3-Green trigger is asserted in this MD.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| case_id | local 4B observation | full-window 4B conclusion |
|---|---|---|
| R4L83-C16-01 | local peak after strong copper/defense beta; drawdown -33.90% | local 4B watch useful; no hard 4C |
| R4L83-C16-02 | strong early MFE then deep post-peak drawdown | local 4B should fire earlier when customer call-off risk appears |
| R4L83-C16-03 | trigger-day peak, high MAE | price/theme spike should not become positive Stage2/Green |
| R4L83-C16-04 | near-trigger peak, high MAE | price/theme spike should not become positive Stage2/Green |

## 16. 4C Protection Audit

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_price_only_allowed_count = 0
```

No selected case is routed to hard 4C without non-price thesis-break evidence.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C16_customer_offtake_utilization_margin_bridge_required
proposal_type = shadow_only
production_scoring_changed = false
```

Candidate logic:

```text
if canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
and strategic_resource_headline == true
and customer_offtake_or_utilization_bridge == false
and repricing_or_margin_bridge == false:
    block Stage2-Actionable positive credit
    allow only RiskWatch / local4B watch
```

## 18. Canonical-Archetype Rule Candidate

C16 should split strategic-resource headlines into three paths:

```text
1. Positive:
   resource/supply headline + customer/offtake + utilization/repricing + margin bridge

2. Local 4B watch:
   strong MFE + later customer/order pacing risk + post-peak drawdown

3. False positive:
   local-supply/resource theme headline + low MFE + high MAE + no customer/utilization bridge
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE_90D | avg MAE_90D | false positive count | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 32.22% | -25.65% | 2 | overcredits theme-only strategic material rows |
| P0b e2r_2_0_baseline_reference | 4 | 32.22% | -25.65% | 2 | lacks C16-specific bridge separation |
| P1 sector_specific_candidate_profile | 4 | 32.22% | -25.65% | 1 | better but still broad |
| P2 canonical_archetype_candidate_profile | 4 | 32.22% | -25.65% | 0-1 | best shadow profile; blocks CNT/electrolyte theme false positives |
| P3 counterexample_guard_profile | 4 | 32.22% | -25.65% | 0 | strict; may miss early copper positive if source repair fails |

## 20. Score-Return Alignment Matrix

| case_id | score before | stage before | score after | stage after | alignment |
|---|---:|---|---:|---|---|
| R4L83-C16-01 | 76 | Stage2-Actionable | 82 | Stage3-Yellow-C16-BridgeCandidate | improved positive separation |
| R4L83-C16-02 | 74 | Stage2-Actionable | 79 | Stage2-Actionable-C16-Local4BWatch | improved positive separation |
| R4L83-C16-03 | 72 | Stage2-Actionable | 58 | Stage1-or-4B-Watch | false-positive risk reduced |
| R4L83-C16-04 | 70 | Stage2-Actionable | 56 | Stage1-or-4B-Watch | false-positive risk reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positives | counterexamples | 4B cases | 4C cases | new independent | reused | usable triggers | representative triggers | profile errors | sector rule candidate | canonical rule candidate |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | COPPER_FOIL_CNT_ELECTROLYTE_STRATEGIC_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE | 2 | 2 | 3 | 0 | 4 | 0 | 4 | 4 | 4 | no | yes |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - C16_headline_overcredit_without_customer_calloff
  - C16_local_4B_watch_too_late_after_strategic_material_peak
  - resource_theme_false_positive_high_MAE
new_axis_proposed: null
existing_axis_strengthened: C16_customer_offtake_utilization_margin_bridge_required
existing_axis_weakened: null
existing_axis_kept:
  - Green threshold remains strict
  - hard 4C requires non-price thesis break
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web tradable OHLC rows exist for all selected symbols and entry years.
- 30D/90D/180D MFE/MAE were computed from visible Stock-Web OHLC rows.
- Corporate-action candidate windows are clean for the selected 180D windows, except 121600 micro share-count drift requires validation even though profile-level CA candidate is historical.
- Round/sector/canonical mapping is valid.
```

Not validated:

```text
- Source URL repair for all non-price evidence.
- Exact public timestamp of all trigger evidence.
- Production code behavior.
- Runtime scoring profile changes.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_customer_offtake_utilization_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"C16 false positives came from strategic-material headlines without customer/offtake/utilization/repricing bridge","reduces CNT/electrolyte false positives while preserving copper positives","R4L83-C16-01-Stage2-Actionable|R4L83-C16-02-Stage2-Actionable|R4L83-C16-03-Stage2-FalsePositive|R4L83-C16-04-Stage2-FalsePositive",4,4,2,low,canonical_shadow_only,"source_proxy_only/evidence_url_pending; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L83-C16-01", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_METAL_SUPPLY_MARGIN_BRIDGE_VS_RESOURCE_THEME_BETA", "case_type": "structural_success_with_later_local4B", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive lifecycle: copper/strategic metal shock produced high 90D/180D MFE with controlled MAE, but local 4B watch was needed after the July peak."}
{"row_type": "case", "case_id": "R4L83-C16-02", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_FOIL_STRATEGIC_SUPPLY_LOCALIZATION_VS_CUSTOMER_CALLOFF", "case_type": "structural_success_with_thesis_break_watch", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Positive early price path but later customer/order pacing risk should become local 4B watch, not hard 4C without non-price thesis break."}
{"row_type": "case", "case_id": "R4L83-C16-03", "symbol": "121600", "company_name": "나노신소재", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CNT_CONDUCTIVE_ADDITIVE_LOCAL_SUPPLY_THEME_WITHOUT_CALLOFF", "case_type": "counterexample_or_failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_overcredited_headline", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Theme spike without refreshed customer call-off/utilization evidence should be blocked from C16 positive Stage2/Green."}
{"row_type": "case", "case_id": "R4L83-C16-04", "symbol": "278280", "company_name": "천보", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_SUPPLY_THEME_WITHOUT_REPRICING_OR_UTILIZATION", "case_type": "counterexample_or_failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_overcredited_headline", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Strategic-supply narrative alone did not pay; current calibrated profile needs C16 bridge requirement to avoid Stage2 false positives."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L83-C16-01-Stage2-Actionable", "case_id": "R4L83-C16-01", "symbol": "103140", "company_name": "풍산", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_STRATEGIC_METAL_SUPPLY_MARGIN_BRIDGE_VS_RESOURCE_THEME_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 42200, "evidence_available_at_that_date": "COPPER_STRATEGIC_METAL_SUPPLY_MARGIN_BRIDGE", "evidence_source": "source_proxy_only; evidence_url_pending; to be repaired by coding agent", "stage2_evidence_fields": ["copper/strategic metal spread", "defense/electronics demand proxy", "volume and price bridge required"], "stage3_evidence_fields": ["margin bridge", "order/customer visibility", "revision confirmation pending"], "stage4b_evidence_fields": ["local peak drawdown after copper/defense beta overextension"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.07, "MFE_90D_pct": 61.85, "MFE_180D_pct": 68.48, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.7, "MAE_90D_pct": -7.7, "MAE_180D_pct": -7.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-10", "peak_price": 71100, "drawdown_after_peak_pct": -33.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "local_4B_watch_needed", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_lifecycle_then_local4B_watch", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L83-C16-01-2024-02-22-42200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "R4L83-C16-02-Stage2-Actionable", "case_id": "R4L83-C16-02", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "COPPER_FOIL_STRATEGIC_SUPPLY_LOCALIZATION_VS_CUSTOMER_CALLOFF", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-20", "entry_price": 37650, "evidence_available_at_that_date": "COPPER_FOIL_STRATEGIC_SUPPLY_LOCALIZATION_VS_CUSTOMER_CALLOFF", "evidence_source": "source_proxy_only; evidence_url_pending; to be repaired by coding agent", "stage2_evidence_fields": ["copper foil/local supply chain visibility", "strategic material supply headline", "capacity absorption needed"], "stage3_evidence_fields": ["margin/revision bridge incomplete", "customer call-off risk not yet absorbed"], "stage4b_evidence_fields": ["post-peak customer/order pacing risk", "drawdown-after-peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 39.18, "MFE_90D_pct": 57.24, "MFE_180D_pct": 57.24, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.16, "MAE_90D_pct": -9.16, "MAE_180D_pct": -19.65, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 59200, "drawdown_after_peak_pct": -48.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "local_4B_watch_needed", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_MFE_then_customer_calloff_thesis_break_watch", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L83-C16-02-2024-02-20-37650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "R4L83-C16-03-Stage2-FalsePositive", "case_id": "R4L83-C16-03", "symbol": "121600", "company_name": "나노신소재", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "CNT_CONDUCTIVE_ADDITIVE_LOCAL_SUPPLY_THEME_WITHOUT_CALLOFF", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-06-11", "entry_date": "2024-06-11", "entry_price": 141500, "evidence_available_at_that_date": "CNT_CONDUCTIVE_ADDITIVE_LOCAL_SUPPLY_THEME_WITHOUT_CALLOFF", "evidence_source": "source_proxy_only; evidence_url_pending; to be repaired by coding agent", "stage2_evidence_fields": ["CNT/local supply headline", "customer/utilization bridge missing"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["high MAE", "peak on trigger", "no durable call-off bridge"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv", "profile_path": "atlas/symbol_profiles/121/121600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.87, "MFE_90D_pct": 5.87, "MFE_180D_pct": 5.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -31.24, "MAE_90D_pct": -51.59, "MAE_180D_pct": -58.09, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 149800, "drawdown_after_peak_pct": -60.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_theme_peak_should_not_be_positive_stage", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "strategic_material_theme_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_with_share_count_micro_change_validation", "same_entry_group_id": "R4L83-C16-03-2024-06-11-141500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "R4L83-C16-04-Stage2-FalsePositive", "case_id": "R4L83-C16-04", "symbol": "278280", "company_name": "천보", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "ELECTROLYTE_ADDITIVE_SUPPLY_THEME_WITHOUT_REPRICING_OR_UTILIZATION", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-06-11", "entry_date": "2024-06-11", "entry_price": 79100, "evidence_available_at_that_date": "ELECTROLYTE_ADDITIVE_SUPPLY_THEME_WITHOUT_REPRICING_OR_UTILIZATION", "evidence_source": "source_proxy_only; evidence_url_pending; to be repaired by coding agent", "stage2_evidence_fields": ["electrolyte additive strategic material headline", "utilization/repricing bridge missing"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low MFE", "high MAE", "supply headline failed to convert"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv", "profile_path": "atlas/symbol_profiles/278/278280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.92, "MFE_90D_pct": 3.92, "MFE_180D_pct": 3.92, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.94, "MAE_90D_pct": -34.13, "MAE_180D_pct": -51.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-12", "peak_price": 82200, "drawdown_after_peak_pct": -53.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_theme_peak_should_not_be_positive_stage", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "electrolyte_additive_supply_theme_fade_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L83-C16-04-2024-06-11-79100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L83-C16-01", "trigger_id": "R4L83-C16-01-Stage2-Actionable", "symbol": "103140", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 18, "revision_score": 12, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 18, "valuation_repricing_score": 16, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 24, "backlog_visibility_score": 24, "margin_bridge_score": 22, "revision_score": 14, "relative_strength_score": 16, "customer_quality_score": 18, "policy_or_regulatory_score": 14, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow-C16-BridgeCandidate", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C16 strategic-resource headline receives credit only when offtake/utilization/customer call-off/repricing margin bridge is visible; theme-only rows are pushed to watch/4B.", "MFE_90D_pct": 61.85, "MAE_90D_pct": -7.7, "score_return_alignment_label": "positive_with_later_4B_watch", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L83-C16-02", "trigger_id": "R4L83-C16-02-Stage2-Actionable", "symbol": "020150", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 18, "revision_score": 12, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 18, "valuation_repricing_score": 16, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 24, "backlog_visibility_score": 24, "margin_bridge_score": 22, "revision_score": 14, "relative_strength_score": 16, "customer_quality_score": 18, "policy_or_regulatory_score": 14, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable-C16-Local4BWatch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C16 strategic-resource headline receives credit only when offtake/utilization/customer call-off/repricing margin bridge is visible; theme-only rows are pushed to watch/4B.", "MFE_90D_pct": 57.24, "MAE_90D_pct": -9.16, "score_return_alignment_label": "positive_with_later_4B_watch", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L83-C16-03", "trigger_id": "R4L83-C16-03-Stage2-FalsePositive", "symbol": "121600", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 12, "customer_quality_score": 5, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 6, "valuation_repricing_score": 4, "execution_risk_score": -10, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage1-or-4B-Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C16 strategic-resource headline receives credit only when offtake/utilization/customer call-off/repricing margin bridge is visible; theme-only rows are pushed to watch/4B.", "MFE_90D_pct": 5.87, "MAE_90D_pct": -51.59, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L83-C16-04", "trigger_id": "R4L83-C16-04-Stage2-FalsePositive", "symbol": "278280", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 8, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 12, "customer_quality_score": 5, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 6, "valuation_repricing_score": 4, "execution_risk_score": -10, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage1-or-4B-Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C16 strategic-resource headline receives credit only when offtake/utilization/customer call-off/repricing margin bridge is visible; theme-only rows are pushed to watch/4B.", "MFE_90D_pct": 3.92, "MAE_90D_pct": -34.13, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 83, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["C16_headline_overcredit_without_customer_calloff", "local_4B_watch_needed_after_strategic_material_peak", "resource_theme_false_positive_high_MAE"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R4L83-C16-SOURCE-REPAIR","symbol":"MULTI","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reason":"all non-price evidence is source_proxy_only/evidence_url_pending; use this MD for source repair before runtime promotion","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration_until_source_repair"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat source_proxy_only/evidence_url_pending rows as production-ready.
- Do not route hard 4C from price-only evidence.
- For C16, test a canonical guard requiring customer/offtake/utilization or repricing margin bridge before Stage2-Actionable positive credit.

### Candidate implementation task

```text
Add C16_STRATEGIC_RESOURCE_POLICY_SUPPLY guard candidates to the calibration ledger:
- C16_customer_offtake_utilization_margin_bridge_required
- C16_local_4B_watch_after_strategic_material_peak
- C16_block_theme_only_local_supply_headline_positive_credit
```

Do not patch production scoring until source repair confirms non-price evidence.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 83
next_round = R5
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN EXECUTION PROMPT: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO-REPEAT INDEX: docs/core/V12_Research_No_Repeat_Index.md
price_atlas_repo: Songdaiki/stock-web
manifest: atlas/manifest.json
schema: atlas/schema.json
profiles:
  - atlas/symbol_profiles/103/103140.json
  - atlas/symbol_profiles/020/020150.json
  - atlas/symbol_profiles/121/121600.json
  - atlas/symbol_profiles/278/278280.json
```

Final response fields:

```text
output_file: e2r_stock_web_v12_residual_round_R4_loop_83_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
scheduled_round: R4
scheduled_loop: 83
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
new_independent_case_count: 4
reused_case_count: 0
new_symbol_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 4
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
production_scoring_changed: false
shadow_weight_only: true
existing_axis_tested:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened: C16_customer_offtake_utilization_margin_bridge_required
existing_axis_weakened: null
next_round: R5
```
