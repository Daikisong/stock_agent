# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round = R4
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | sector_specific_rule_discovery | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_71_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 2 new independent cases, 1 counterexample, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C15_policy_spread_bridge_shadow_profile
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

This file does not propose a production global patch. It tests whether C15 material-spread policy triggers should receive a Stage2-actionable boost only when the policy event is linked to a concrete demand/repricing bridge.

## 2. Round / Large Sector / Canonical Archetype Scope

The latest coherent registry continuation observed before this run ended at R3 loop 71. Therefore this file follows the corrected sequential scheduler:

```text
completed_previous_round = R3
completed_previous_loop = 71
scheduled_round = R4
scheduled_loop = 71
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
```

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`, so the round-sector gate passes.

## 3. Previous Coverage / Duplicate Avoidance Check

NO-REPEAT INDEX shows C15 has limited coverage compared with later high-density archetypes:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE:
  rows = 10
  symbols = 7
  existing top covered symbols = 006260, 011170, 103140, 006650, 011780
  current hold/block issue = stage2_bonus_candidate_delta hold_for_more_evidence
```

This research adds two C15 symbols not listed in the C15 top-covered set:

```text
004020 Hyundai Steel
005490 POSCO Holdings
```

Novelty check:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
C15 + 004020 + Stage2-Actionable + 2025-02-21 = not in top-covered C15 set
C15 + 005490 + Stage2-Actionable + 2025-02-21 = not in top-covered C15 set
evidence_family = KOREA_STEEL_ANTIDUMPING_SPREAD_PROTECTION_2025
```

Because this environment used GitHub connector reads rather than a local clone, the full exact-key CLI against `v12_trigger_rows_validated.jsonl` was not executed. The selection avoids the documented top-covered C15 symbols and uses a new evidence family.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Symbol profile checks:

| symbol | profile | corporate_action_candidate_count | 2025 entry~180D window status |
|---|---|---:|---|
| 004020 | atlas/symbol_profiles/004/004020.json | 6, last candidate 2014-01-24 | clean for 2025-02-21~180D |
| 005490 | atlas/symbol_profiles/005/005490.json | 0 | clean |

## 5. Historical Eligibility Gate

| symbol | trigger_date | entry_date | 180D forward available | OHLC available | MFE/MAE 30/90/180D | corporate-action contaminated 180D | usable |
|---|---|---|---|---|---|---|---|
| 004020 | 2025-02-20 | 2025-02-21 | yes | yes | yes | no | true |
| 005490 | 2025-02-20 | 2025-02-21 | yes | yes | yes | no | true |

Entry rule: the Reuters evidence was dated 2025-02-20 and the market reacted on that date. To avoid intraday timestamp ambiguity, entry uses next tradable date close, 2025-02-21 close.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE

fine_archetype_id:
  STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS

deep sub-archetype family:
  - steel plate anti-dumping protection
  - domestic spread protection
  - demand/repricing bridge required
  - broad steel policy headline counterexample when demand/revision is weak
```

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---|---|---|---|
| R4L71-C15-STEEL-ANTIDUMPING-004020-20250221 | 004020 | Hyundai Steel | positive | policy protection created strong 90D/180D upside despite drawdown |
| R4L71-C15-STEEL-ANTIDUMPING-005490-20250221 | 005490 | POSCO Holdings | counterexample | same headline produced only borderline 90D upside and a large post-peak drawdown |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 1
4B_case_count = 0
4C_case_count = 0
calibration_usable_case_count = 2
minimum_calibration_usable_case_count_target = 3
do_not_propose_new_weight_delta = true
reason = below minimum usable-case target; keep as shadow evidence
```

This is intentionally conservative. It adds new evidence to the C15 hold-for-more-evidence bucket, but it does not claim enough support for immediate profile promotion.

## 9. Evidence Source Map

| evidence_family | date | source | non-price evidence | interpretation |
|---|---|---|---|---|
| KOREA_STEEL_ANTIDUMPING_SPREAD_PROTECTION_2025 | 2025-02-20 | Reuters | Korea provisionally decided anti-dumping duties on Chinese steel plate imports; Hyundai Steel and POSCO Holdings reacted | valid Stage2 policy/spread evidence, but Stage3 requires demand/repricing confirmation |

Stage evidence split:

```text
Stage2:
  public_event_or_disclosure = Reuters anti-dumping tariff report
  policy_or_regulatory_optionality = provisional duties of 27.91%~38.02%
  relative_strength = both stocks reacted positively on report date
  margin_bridge = potential domestic steel spread protection

Stage3:
  confirmed_revision = not confirmed in this file
  financial_visibility = not sufficient
  repeat_order_or_conversion = not applicable

4B:
  no explicit non-price 4B trigger
  observed post-peak drawdowns are used as risk evidence only

4C:
  no hard thesis-break trigger in this file
```

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 004020 | atlas/ohlcv_tradable_by_symbol_year/004/004020/2025.csv | atlas/symbol_profiles/004/004020.json |
| 005490 | atlas/ohlcv_tradable_by_symbol_year/005/005490/2025.csv | atlas/symbol_profiles/005/005490.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | role | current_profile_verdict |
|---|---|---|---|---|---:|---|---|
| TR-R4L71-C15-004020-STAGE2A-20250221 | 004020 | Stage2-Actionable | 2025-02-20 | 2025-02-21 | 26,450 | positive | current_profile_too_late |
| TR-R4L71-C15-005490-STAGE2A-20250221 | 005490 | Stage2-Actionable | 2025-02-20 | 2025-02-21 | 282,000 | counterexample | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | 180D peak | drawdown after peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 004020 | 26,450 | +21.7% | -12.5% | +39.7% | -19.1% | +45.4% | -19.1% | 38,450 on 2025-07-23 | -24.3% |
| 005490 | 282,000 | +19.5% | -7.3% | +19.5% | -18.4% | +21.3% | -18.4% | 342,000 on 2025-07-23 | -24.4% |

Interpretation:

- Hyundai Steel shows a genuine C15 policy-to-spread success path: the 90D and 180D upside were strong enough to justify a Stage2-actionable watch.
- POSCO Holdings is the counterexample: the same macro/policy headline was not enough to create a clean Stage3 path. It generated borderline 90D upside, meaningful MAE, and a large post-peak drawdown.

## 13. Current Calibrated Profile Stress Test

| question | 004020 | 005490 |
|---|---|---|
| How would current profile classify? | likely Stage2-Watch until demand/revision confirmation | likely Stage2-Watch; too risky for Green |
| Was that right? | too late if it required full revision before watch/actionable | correct to block Green, but still a false-positive risk if given blanket Stage2 bonus |
| Stage2 bonus too high/low? | slightly too low for direct beneficiary with policy+spread bridge | too high if applied to broad steel policy headline without demand bridge |
| Yellow threshold? | acceptable | acceptable |
| Green threshold/revision guard? | should stay strict | should stay strict |
| price-only blowoff guard? | keep | keep |
| full 4B non-price requirement? | keep | keep |
| hard 4C routing? | no hard 4C | no hard 4C |

Existing axis status:

```text
existing_axis_tested = stage2_actionable_evidence_bonus
existing_axis_strengthened = stage2_required_bridge_for_policy_spread_without_demand_revision
existing_axis_kept = stage3_green_strictness, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
new_axis_proposed = null
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Yellow or Stage3-Green trigger is assigned in this file.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

Suggested interpretation:

```text
004020:
  Stage2-Actionable = allowed when policy protection + beneficiary exposure + price confirmation are present.
  Stage3-Green = blocked until revision/margin bridge becomes visible.

005490:
  Stage2-Actionable = watch-only or lower confidence without demand/revision bridge.
  Stage3-Green = blocked.
```

## 15. 4B Local vs Full-window Timing Audit

No Stage4B trigger is proposed. Observed post-peak drawdowns are risk evidence only.

| symbol | local/full 4B label | local peak proximity | full-window peak proximity | verdict |
|---|---|---:|---:|---|
| 004020 | none | n/a | n/a | no non-price 4B evidence |
| 005490 | none | n/a | n/a | no non-price 4B evidence |

## 16. 4C Protection Audit

No hard 4C trigger is proposed.

```text
four_c_protection_label = not_applicable
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
proposal = For L4 materials/spread cases, policy protection can lift Stage2 confidence only when it directly improves spread economics for a named beneficiary. Broad commodity/policy headline without demand or repricing bridge should remain watch-only.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
canonical_archetype_rule_candidate = true
proposal = C15 Stage2 bonus should be conditional: policy/spread evidence + named beneficiary + tradable confirmation + no demand deterioration. If the event is policy-only or broad commodity sympathy, require Stage2 bridge and block Green.
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1 proxy | current calibrated profile | 2 | +29.6% | -18.8% | +33.4% | -18.8% | mixed |
| P1 sector shadow | L4 policy/spread bridge required | 2 | +29.6% | -18.8% | +33.4% | -18.8% | better label separation |
| P2 canonical shadow | C15 conditional Stage2 bonus | 2 | +29.6% | -18.8% | +33.4% | -18.8% | useful but insufficient sample size |
| P3 counterexample guard | no bonus without demand/revision bridge | 1 counterexample | +19.5% | -18.4% | +21.3% | -18.4% | guard retained |

## 20. Score-Return Alignment Matrix

| symbol | weighted score before | stage before | weighted score after | stage after | price outcome | alignment |
|---|---:|---|---:|---|---|---|
| 004020 | 74 | Stage2-Watch | 78 | Stage2-Actionable | +39.7% MFE90 / +45.4% MFE180 | improved |
| 005490 | 72 | Stage2-Watch | 70 | Stage2-Watch | +19.5% MFE90 / -18.4% MAE90 / -24.4% post-peak drawdown | guard useful |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B | 4C | new_independent_case_count | reused_case_count | usable triggers | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS | 1 | 1 | 0 | 0 | 2 | 0 | 2 | 2 | true | true |

## 22. Residual Contribution Summary

```text
new_independent_case_count = 2
reused_case_count = 0
reused_case_ids = []
new_symbol_count = 2
new_canonical_archetype_count = 0
new_fine_archetype_count = 1
new_trigger_family_count = 1
tested_existing_calibrated_axes = stage2_actionable_evidence_bonus, stage3_green_strictness, price_only_blowoff_blocks_positive_stage
residual_error_types_found = current_profile_too_late, current_profile_false_positive, high_mae_stage2
new_axis_proposed = null
existing_axis_strengthened = stage2_required_bridge_for_policy_spread_without_demand_revision
existing_axis_weakened = null
existing_axis_kept = stage3_green_strictness, full_4b_non_price_requirement, price_only_blowoff_guard
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
no_new_signal_reason = null
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = true
do_not_propose_global_delta = true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
validated:
  - stock-web manifest/schema
  - 004020 and 005490 2025 tradable shards
  - 004020 and 005490 symbol profiles
  - actual OHLC rows for entry, peak, drawdown
  - 30D/90D/180D MFE/MAE calculations
  - non-price evidence source

not validated in this run:
  - full local duplicate CLI over v12_trigger_rows_validated.jsonl
  - any production scoring code
  - any live candidate scan
  - any brokerage/API integration
```

## 24. Shadow Weight Calibration

```text
shadow_weight_candidate:
  scope = canonical_archetype_specific
  canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
  changed_axes = stage2_bonus_candidate_delta, stage2_required_bridge
  proposed_delta = conditional +0.5 max, only when policy/spread evidence has named beneficiary and demand/repricing bridge
  promotion_status = hold_for_more_evidence
  reason = calibration_usable_case_count is 2, below minimum target 3
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R4L71-C15-STEEL-ANTIDUMPING-004020-20250221","symbol":"004020","company_name":"현대제철","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-R4L71-C15-004020-STAGE2A-20250221","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"non_price_policy_spread_protection_aligned_with_MFE90_and_MFE180","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"new symbol for C15 top-covered set; anti-dumping policy-to-spread trigger family"}
{"row_type":"trigger","trigger_id":"TR-R4L71-C15-004020-STAGE2A-20250221","case_id":"R4L71-C15-STEEL-ANTIDUMPING-004020-20250221","symbol":"004020","company_name":"현대제철","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","sector":"L4_MATERIALS_SPREAD_RESOURCE","primary_archetype":"C15_MATERIAL_SPREAD_SUPERCYCLE","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-20","evidence_available_at_that_date":"Reuters reported Korea's provisional anti-dumping duties on Chinese steel plates; shares of Hyundai Steel and POSCO reacted on the announcement date.","evidence_source":"Reuters 2025-02-20 steel plate anti-dumping tariff report","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","margin_bridge"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004020/2025.csv","profile_path":"atlas/symbol_profiles/004/004020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-21","entry_price":26450,"MFE_30D_pct":21.7,"MFE_90D_pct":39.7,"MFE_180D_pct":45.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.5,"MAE_90D_pct":-19.1,"MAE_180D_pct":-19.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-23","peak_price":38450,"drawdown_after_peak_pct":-24.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_stage4b_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_positive_high_mfe_but_high_mae","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile candidate dates end at 2014-01-24","same_entry_group_id":"R4L71-C15-STEEL-ANTIDUMPING-004020-20250221::2025-02-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":false,"source_proxy_only":false}
{"row_type":"score_simulation","case_id":"R4L71-C15-STEEL-ANTIDUMPING-004020-20250221","trigger_id":"TR-R4L71-C15-004020-STAGE2A-20250221","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","profile_id":"P0_to_P2_shadow_comparison","profile_scope":"canonical_archetype_specific","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":13,"revision_score":6,"relative_strength_score":14,"customer_quality_score":4,"policy_or_regulatory_score":17,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":14},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":15,"revision_score":6,"relative_strength_score":14,"customer_quality_score":4,"policy_or_regulatory_score":18,"valuation_repricing_score":8,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":16},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"C15 steel anti-dumping trigger should not receive a blanket Stage2 bonus; it needs evidence of demand/repricing conversion to avoid POSCO-like high-MAE borderline outcomes."}
{"row_type":"case","case_id":"R4L71-C15-STEEL-ANTIDUMPING-005490-20250221","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TR-R4L71-C15-005490-STAGE2A-20250221","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_spread_headline_without_clean_demand_revision_created_borderline_MFE90_and_high_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new symbol for C15 top-covered set; anti-dumping policy-to-spread trigger family"}
{"row_type":"trigger","trigger_id":"TR-R4L71-C15-005490-STAGE2A-20250221","case_id":"R4L71-C15-STEEL-ANTIDUMPING-005490-20250221","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","sector":"L4_MATERIALS_SPREAD_RESOURCE","primary_archetype":"C15_MATERIAL_SPREAD_SUPERCYCLE","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-20","evidence_available_at_that_date":"Reuters reported Korea's provisional anti-dumping duties on Chinese steel plates; shares of Hyundai Steel and POSCO reacted on the announcement date.","evidence_source":"Reuters 2025-02-20 steel plate anti-dumping tariff report","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","margin_bridge"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2025.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-21","entry_price":282000,"MFE_30D_pct":19.5,"MFE_90D_pct":19.5,"MFE_180D_pct":21.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.3,"MAE_90D_pct":-18.4,"MAE_180D_pct":-18.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-23","peak_price":342000,"drawdown_after_peak_pct":-24.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_stage4b_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_high_mae_borderline_positive_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_count=0","same_entry_group_id":"R4L71-C15-STEEL-ANTIDUMPING-005490-20250221::2025-02-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":false,"source_proxy_only":false}
{"row_type":"score_simulation","case_id":"R4L71-C15-STEEL-ANTIDUMPING-005490-20250221","trigger_id":"TR-R4L71-C15-005490-STAGE2A-20250221","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","profile_id":"P0_to_P2_shadow_comparison","profile_scope":"canonical_archetype_specific","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":10,"revision_score":4,"relative_strength_score":11,"customer_quality_score":3,"policy_or_regulatory_score":17,"valuation_repricing_score":8,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":12},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":9,"revision_score":4,"relative_strength_score":11,"customer_quality_score":3,"policy_or_regulatory_score":16,"valuation_repricing_score":8,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":10},"weighted_score_after":70,"stage_label_after":"Stage2-Watch","component_delta_explanation":"C15 steel anti-dumping trigger should not receive a blanket Stage2 bonus; it needs evidence of demand/repricing conversion to avoid POSCO-like high-MAE borderline outcomes."}
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","new_independent_case_count":2,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":1,"new_trigger_family_count":1,"positive_case_count":1,"counterexample_count":1,"4B_case_count":0,"4C_case_count":0,"calibration_usable_case_count":2,"calibration_usable_trigger_count":2,"representative_trigger_count":2,"current_profile_error_count":2,"avg_MFE_90D_pct":29.6,"avg_MAE_90D_pct":-18.8,"avg_MFE_180D_pct":33.4,"avg_MAE_180D_pct":-18.8,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C15 still needs >=3 calibration-usable cases for full promotion; this file adds 2 clean new-symbol cases."}
{"row_type":"shadow_weight","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","rule_scope":"canonical_archetype_specific","changed_axes":["stage2_bonus_candidate_delta","stage2_required_bridge"],"proposed_delta":"conditional +0.5 only when policy protection is paired with demand/repricing bridge; otherwise keep watch","supporting_case_ids":"R4L71-C15-STEEL-ANTIDUMPING-004020-20250221|R4L71-C15-STEEL-ANTIDUMPING-005490-20250221","positive_case_count":1,"counterexample_count":1,"evidence_quality":"medium","usage":"sector_shadow_only","notes":"not production; post-calibrated residual research"}
{"row_type":"residual_contribution","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","scheduled_round":"R4","scheduled_loop":"71","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":2,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":1,"new_trigger_family_count":1,"positive_case_count":1,"counterexample_count":1,"current_profile_error_count":2,"diversity_score_summary":"+2 new symbols, +1 trigger family, +1 positive, +1 counterexample, no hard duplicate","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_strictness","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","high_mae_stage2"],"new_axis_proposed":null,"existing_axis_strengthened":"stage2_required_bridge_for_policy_spread_without_demand_revision","existing_axis_weakened":null,"existing_axis_kept":"stage3_green_strictness; full_4b_non_price_requirement","sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":true,"do_not_propose_global_delta":true,"reason":"minimum_calibration_usable_case_count target is 3; current file has 2 usable cases, so hold as shadow evidence."}
{"row_type":"narrative_only","case_id":"R4L71-C15-NARRATIVE-STEEL-DEMAND-WEAKNESS","symbol":"SECTOR_BASKET","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS","reason":"anti-dumping policy is non-price evidence, but steel spread supercycle still needs demand/repricing bridge; use only as narrative guard until more clean C15 cases are collected","price_source":"Songdaiki/stock-web","usage":"rule_explanation_not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_round = R4
completed_loop = 71
next_round = R5
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
- Duplicate ledger: `docs/core/V12_Research_No_Repeat_Index.md`
- Price atlas: `Songdaiki/stock-web`
- Evidence source: Reuters, 2025-02-20, “South Korea provisionally slaps tariffs on Chinese steel plates for dumping”
- Price rows used:
  - `atlas/ohlcv_tradable_by_symbol_year/004/004020/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/005/005490/2025.csv`
- Profiles used:
  - `atlas/symbol_profiles/004/004020.json`
  - `atlas/symbol_profiles/005/005490.json`

