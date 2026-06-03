# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
scheduled_round: R10
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R11
computed_next_loop: 71
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE
loop_objective: coverage_gap_fill | counterexample_mining | 4C_balance_sheet_break_guard | sector_specific_rule_discovery | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent calibration-usable cases, 2 counterexamples, and 3 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
already_applied_axes_tested = [
  stage2_actionable_evidence_bonus,
  price_only_blowoff_blocks_positive_stage,
  full_4b_requires_non_price_evidence,
  hard_4c_thesis_break_routes_to_4c
]
production_scoring_changed = false
```

C30 should not reward price weakness alone. The residual test here asks whether PF stress plus visible balance-sheet/liquidity deterioration protects against drawdown, and whether recapitalization/support evidence should prevent over-routing every small builder into hard 4C.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R10 |
| scheduled_loop | 71 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| fine_archetype_id | MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE |
| valid round-sector pair | yes |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot shows C30 had 28 rows, 6 symbols, 2022-01-12~2024-08-27, with top covered symbols concentrated in 006360, 294870, 375500, UNKNOWN_SYMBOL, and 000720. This loop deliberately avoids those top repeated symbols and uses 034300, 002990, 014790 as new independent C30 symbol paths, with 009410 retained only as a narrative-only blocked exemplar because stock-web flags a later corporate-action/suspension-resumption issue.

Hard duplicate rule used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Profile checks:

| symbol | company | profile_path | relevant profile status | corporate-action caveat |
|---|---|---|---|---|
| 034300 | 신세계건설 | atlas/symbol_profiles/034/034300.json | inactive_or_delisted_like; last tradable 2025-01-24 | 2024-02-06 candidate; entries after 2024-02-07 treated clean |
| 002990 | 금호건설 | atlas/symbol_profiles/002/002990.json | active_like | no post-2013 corporate-action candidate inside 2024 test window |
| 014790 | HL D&I | atlas/symbol_profiles/014/014790.json | active_like | no post-2012 corporate-action candidate inside 2024 test window |
| 009410 | 태영건설 | atlas/symbol_profiles/009/009410.json | active_like but with 2024-10-31 corporate-action/resumption candidate | narrative-only; not weight calibration |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward 180D available | corporate action overlap | calibration_usable | block reason |
|---|---|---|---|---|---|---|
| C30-R10L71-034300-RECAP | 034300 | 2024-02-07 | yes | no, entry after 2024-02-06 candidate | true | null |
| C30-R10L71-002990-PF-DRAG | 002990 | 2024-01-02 | yes | no | true | null |
| C30-R10L71-014790-FALSEBREAK | 014790 | 2024-01-02 | yes | no | true | null |
| C30-R10L71-009410-WORKOUT | 009410 | 2024-01-02 | partially distorted by suspension/resumption | yes, 2024-10-31 | false | corporate_action_contaminated_180D_window / long_trading_gap |

## 6. Canonical Archetype Compression Map

C30 compresses four very different phenomena that must not be scored as the same signal:

1. **Hard balance-sheet break**: PF/workout/default/refinancing failure plus continued equity drawdown.
2. **Recapitalization rescue**: weak PF headline, but parent/group/asset support changes the path.
3. **Policy liquidity backstop**: government/bank support improves funding window without solving project economics.
4. **Price-only construction beta**: sector selloff without specific off-BS/PF evidence.

This loop proposes that C30 requires a stricter split between `hard_4c_balance_sheet_break` and `pf_watch_with_recapitalization_rescue`.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | selected trigger | calibration_usable |
|---|---|---|---|---|---|---|
| C30-R10L71-034300-RECAP | 034300 | 신세계건설 | counterexample / rescue path | parent-or-capital-support-after-PF-stress | Stage2-Watch / rescue bridge | true |
| C30-R10L71-002990-PF-DRAG | 002990 | 금호건설 | structural break / hard guard | small builder PF/credit-spread drag | Stage2-Actionable risk watch | true |
| C30-R10L71-014790-FALSEBREAK | 014790 | HL D&I | counterexample / false break | price-only PF beta vs balance-sheet confirmation | Stage2-Watch only | true |
| C30-R10L71-009410-WORKOUT | 009410 | 태영건설 | narrative-only hard 4C exemplar | workout/suspension/corporate-action contamination | narrative_only | false |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 4 |
| narrative_only_case_count | 1 |

Interpretation: C30 already has enough “PF stress exists” examples. The new value here is distinguishing which weak builders actually required hard 4C protection and which ones should have been kept at watch/Yellow because support or lack of confirmed balance-sheet break changed the path.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | source quality |
|---|---|---|---|
| C30-R10L71-034300-RECAP | PF/liquidity concern was already visible, but post-2024-02-06 capital/share profile changed; price path suggests rescue/recapitalization dominated the PF fear | stock-web profile + public filings/news proxy | source_proxy_only=false for price; evidence source proxy for narrative |
| C30-R10L71-002990-PF-DRAG | small/mid builder PF and credit-spread pressure in 2024 construction funding stress | sector news / credit-risk proxy + stock-web | source_proxy_only=true |
| C30-R10L71-014790-FALSEBREAK | small builder construction beta sold off, but no hard PF break evidence in profile window | sector news / stock-web | source_proxy_only=true |
| C30-R10L71-009410-WORKOUT | Taeyoung debt rescheduling/workout concern publicly triggered broader Korean builder liquidity worry | Reuters, 2024-03-27 South Korea construction support article | source_proxy_only=false; not quantitative due price contamination |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | entry_price |
|---|---|---|---|---:|
| 034300 | atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv | atlas/symbol_profiles/034/034300.json | 2024-02-07 | 11460 |
| 002990 | atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv | atlas/symbol_profiles/002/002990.json | 2024-01-02 | 5110 |
| 014790 | atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv | atlas/symbol_profiles/014/014790.json | 2024-01-02 | 2145 |
| 009410 | atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv | atlas/symbol_profiles/009/009410.json | 2024-01-02 | 2620 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | trigger_outcome_label | current_profile_verdict |
|---|---|---|---|---|---|---:|---|---|
| TR-C30-034300-S2WATCH | C30-R10L71-034300-RECAP | 034300 | Stage2-Watch | 2024-02-06 | 2024-02-07 | 11460 | rescue_recap_counterexample | current_profile_false_positive |
| TR-C30-002990-S2RISK | C30-R10L71-002990-PF-DRAG | 002990 | Stage2-Actionable-Risk | 2024-01-02 | 2024-01-02 | 5110 | hard_pf_drag_success | current_profile_too_late |
| TR-C30-014790-S2WATCH | C30-R10L71-014790-FALSEBREAK | 014790 | Stage2-Watch | 2024-01-02 | 2024-01-02 | 2145 | false_break_recovery | current_profile_false_positive |
| TR-C30-009410-NARR | C30-R10L71-009410-WORKOUT | 009410 | narrative_only | 2023-12-28 | 2024-01-02 | 2620 | hard_4c_exemplar_blocked | current_profile_data_insufficient |

## 12. Trigger-Level OHLC Backtest Tables

Calculated with raw/unadjusted `tradable_raw` OHLC rows from Songdaiki/stock-web. Values are rounded to one decimal point.

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | usable |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| TR-C30-034300-S2WATCH | 11460 | 11.5 | -9.2 | 17.4 | -9.2 | 60.0 | -9.2 | 2024-09-30 | 18340 | -1.0 | true |
| TR-C30-002990-S2RISK | 5110 | 3.3 | -2.5 | 3.3 | -16.0 | 3.3 | -37.3 | 2024-02-01 | 5280 | -39.3 | true |
| TR-C30-014790-S2WATCH | 2145 | 4.0 | -6.8 | 4.0 | -9.3 | 25.2 | -9.3 | 2024-09-05 | 2685 | -22.5 | true |
| TR-C30-009410-NARR | 2620 | 56.9 | -16.8 | contaminated | contaminated | contaminated | contaminated | 2024-01-11 | 4110 | contaminated | false |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected behavior | actual path | verdict |
|---|---|---|---|
| C30-R10L71-034300-RECAP | likely hard watch / possible 4C due PF stress | recap/support path produced +60% 180D MFE and shallow MAE after post-recap entry | current_profile_false_positive |
| C30-R10L71-002990-PF-DRAG | watch may have been too soft without specific break confirmation | low MFE, deep 180D MAE; hard risk guard was useful | current_profile_too_late |
| C30-R10L71-014790-FALSEBREAK | price weakness alone might over-route to 4C | later +25% 180D MFE; hard 4C would be too punitive | current_profile_false_positive |
| C30-R10L71-009410-WORKOUT | hard 4C likely correct narratively | stock-web 180D window contaminated by trading gap/corporate-action candidate | current_profile_data_insufficient |

## 14. Stage2 / Yellow / Green Comparison

C30 should not use normal Green logic. Green for a balance-sheet-break archetype means “risk thesis confirmed,” not “buy signal.”

| symbol | Stage2 / Watch | Stage3 confirmation | recommended routing |
|---|---|---|---|
| 034300 | PF stress watch | recap/support and share-profile change, price support | Watch/Yellow, not hard 4C |
| 002990 | sector PF stress + credit/liquidity drag | persistent drawdown and no recovery evidence in 180D window | hard 4C guard / avoid positive promotion |
| 014790 | sector stress and price weakness | no hard balance-sheet break confirmation | Watch only |
| 009410 | workout headline | hard break narrative, but unusable for 180D calibration | narrative hard 4C exemplar only |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
|---|---:|---:|---|---|
| TR-C30-034300-S2WATCH | not_applicable | not_applicable | not_4b; rescue/recap path | recapitalization_or_parent_support |
| TR-C30-002990-S2RISK | 0.30 | 0.30 | 4B not main; hard 4C risk dominates | price_only; credit_spread_drag |
| TR-C30-014790-S2WATCH | 0.15 | 0.16 | price_only_local_4B_too_early | price_only |
| TR-C30-009410-NARR | contaminated | contaminated | narrative_hard_4c_not_weight | workout; trading_gap |

## 16. 4C Protection Audit

| trigger_id | 4C label | protection verdict |
|---|---|---|
| TR-C30-034300-S2WATCH | false_break | hard 4C would have blocked a rescue/repricing path |
| TR-C30-002990-S2RISK | hard_4c_success | hard guard avoided a -37% 180D MAE path |
| TR-C30-014790-S2WATCH | false_break | hard 4C too early; watch-only better |
| TR-C30-009410-NARR | hard_4c_success_narrative_only | quantitative row blocked due contamination |

## 17. Sector-Specific Rule Candidate

```yaml
rule_scope: sector_specific
candidate_rule_id: L9_C30_PF_BALANCE_SHEET_BREAK_REQUIRES_BALANCE_SHEET_CONFIRMATION_OR_RECAP_SPLIT
hypothesis: >
  In Korean construction/real-estate PF cycles, price weakness plus sector stress is insufficient for hard 4C.
  Hard 4C needs either workout/default/refinancing failure/accounting impairment or persistent liquidity/credit deterioration.
  Conversely, recapitalization/parent support/asset-sale bridge should demote the case from hard 4C to Watch/Yellow until the support bridge fails.
changed_axes:
  - strengthen hard_4c_thesis_break_routes_to_4c only when balance_sheet_break_confirmation=true
  - add rescue_bridge_guard for recapitalization_or_parent_support=true
  - keep price_only_blowoff_blocks_positive_stage
```

## 18. Canonical-Archetype Rule Candidate

```yaml
rule_scope: canonical_archetype_specific
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule_candidate: >
  C30 should split PF stress into hard_break, rescue_bridge, and price_only_beta buckets.
  hard_break can route to 4C; rescue_bridge routes to Stage2-Watch/Yellow; price_only_beta cannot count as hard 4C.
minimum_support_this_loop:
  calibration_usable_cases: 3
  positives_or_hard_guards: 1
  counterexamples: 2
  narrative_only_hard_4c_exemplar: 1
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE_180D | avg MAE_180D | false positive count | missed hard guard count | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 29.5 | -18.6 | 2 | 1 | too blunt for C30 |
| P0b e2r_2_0_baseline_reference | 3 | 29.5 | -18.6 | 2 | 1 | same core weakness |
| P1 sector_specific_candidate_profile | 3 | 29.5 | -18.6 | 1 | 0 | better split by support bridge |
| P2 canonical_archetype_candidate_profile | 3 | 29.5 | -18.6 | 1 | 0 | preferred shadow profile |
| P3 counterexample_guard_profile | 3 | 29.5 | -18.6 | 0 | 1 | too forgiving for genuine break |

## 20. Score-Return Alignment Matrix

| trigger_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | alignment |
|---|---|---:|---|---|---:|---|---|
| TR-C30-034300-S2WATCH | credit_risk=65, support_bridge=20, price_damage=55 | 71 | Stage2-Watch/4C-risk | credit_risk=50, support_bridge=70, price_damage=40 | 62 | Watch/RescueBridge | improved |
| TR-C30-002990-S2RISK | credit_risk=60, support_bridge=10, price_damage=45 | 68 | Stage2-Watch | credit_risk=75, support_bridge=10, price_damage=65 | 78 | 4C-Guard | improved |
| TR-C30-014790-S2WATCH | credit_risk=50, support_bridge=30, price_damage=45 | 66 | Stage2-Watch/4C-risk | credit_risk=45, support_bridge=35, price_damage=35 | 58 | WatchOnly | improved |

Canonical component keys retained: `contract_score`, `backlog_visibility_score`, `margin_bridge_score`, `revision_score`, `relative_strength_score`, `customer_quality_score`, `policy_or_regulatory_score`, `valuation_repricing_score`, `execution_risk_score`, `legal_or_contract_risk_score`, `dilution_cb_risk_score`, `accounting_trust_risk_score`.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE | 1 | 2 | 1 | 1 | 3 | 0 | 4 | 3 | 3 | true | true | still needs more verified non-proxy builder credit/filing URLs |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - hard_4c_false_positive_when_recapitalization_bridge_exists
  - missed_hard_4c_when_pf_drag_persists
  - price_only_pf_beta_overrouting
new_axis_proposed: null
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c_with_balance_sheet_confirmation
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable rows only.
- Uses raw/unadjusted marcap OHLC.
- Uses 034300 / 002990 / 014790 as calibration-usable representative rows.
- Uses 009410 only as narrative-only hard 4C exemplar due trading gap/corporate-action contamination.

Non-validation scope:

- Does not patch production scoring.
- Does not run live scan.
- Does not claim current investability.
- Does not use broker/API data.

## 24. Shadow Weight Calibration

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"canonical_archetype_specific","candidate_rule_id":"C30_PF_BREAK_RECAP_SPLIT","component_delta":{"accounting_trust_risk_score":"+1 when verified impairment/workout/refinancing failure exists","legal_or_contract_risk_score":"+1 when workout/default/project cancellation is verified","policy_or_regulatory_score":"-1 hard_4c pressure when explicit liquidity support or recap bridge exists","execution_risk_score":"+1 only with persistent MAE and no support bridge"},"supporting_case_ids":["C30-R10L71-034300-RECAP","C30-R10L71-002990-PF-DRAG","C30-R10L71-014790-FALSEBREAK"],"positive_case_count":1,"counterexample_count":2,"risk_level":"medium","production_action":"sector_shadow_only"}
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"case","case_id":"C30-R10L71-034300-RECAP","symbol":"034300","company_name":"신세계건설","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE","case_type":"failed_rerating_counterexample","positive_or_counterexample":"counterexample","best_trigger":"TR-C30-034300-S2WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"support_bridge_dominated_pf_fear","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"PF stress alone would have over-routed to hard 4C; post-recap/support price path had strong MFE."}
{"row_type":"case","case_id":"C30-R10L71-002990-PF-DRAG","symbol":"002990","company_name":"금호건설","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"TR-C30-002990-S2RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_guard_aligned_with_drawdown","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Low 180D MFE and deep MAE supported stronger C30 risk guard."}
{"row_type":"case","case_id":"C30-R10L71-014790-FALSEBREAK","symbol":"014790","company_name":"HL D&I","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR-C30-014790-S2WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_only_pf_beta_false_break","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Price-only PF beta should stay watch-only without hard balance-sheet confirmation."}
{"row_type":"narrative_only","case_id":"C30-R10L71-009410-WORKOUT","symbol":"009410","company_name":"태영건설","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"corporate_action_contaminated_180D_window_and_long_trading_gap_after_workout","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"trigger","trigger_id":"TR-C30-034300-S2WATCH","case_id":"C30-R10L71-034300-RECAP","symbol":"034300","company_name":"신세계건설","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE","loop_objective":"canonical_archetype_compression","trigger_type":"Stage2-Watch","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":11460,"evidence_available_at_that_date":"PF/liquidity concern plus post-2024-02-06 capital/share profile change; rescue bridge observable after entry","evidence_source":"stock-web profile + public filing/news proxy","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv","profile_path":"atlas/symbol_profiles/034/034300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.5,"MFE_90D_pct":17.4,"MFE_180D_pct":60.0,"MFE_1Y_pct":60.0,"MFE_2Y_pct":null,"MAE_30D_pct":-9.2,"MAE_90D_pct":-9.2,"MAE_180D_pct":-9.2,"MAE_1Y_pct":-9.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":18340,"drawdown_after_peak_pct":-1.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_4b","four_b_evidence_type":["recapitalization_or_parent_support"],"four_c_protection_label":"false_break","trigger_outcome_label":"rescue_recap_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_after_2024_02_06","same_entry_group_id":"034300-2024-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C30-002990-S2RISK","case_id":"C30-R10L71-002990-PF-DRAG","symbol":"002990","company_name":"금호건설","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE","loop_objective":"hard_4c_guard_test","trigger_type":"Stage2-Actionable-Risk","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":5110,"evidence_available_at_that_date":"small/mid builder PF and credit-spread pressure visible in Korean construction funding cycle","evidence_source":"sector credit-risk proxy + stock-web","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv","profile_path":"atlas/symbol_profiles/002/002990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.3,"MFE_90D_pct":3.3,"MFE_180D_pct":3.3,"MFE_1Y_pct":3.3,"MFE_2Y_pct":null,"MAE_30D_pct":-2.5,"MAE_90D_pct":-16.0,"MAE_180D_pct":-37.3,"MAE_1Y_pct":-38.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-01","peak_price":5280,"drawdown_after_peak_pct":-39.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.3,"four_b_full_window_peak_proximity":0.3,"four_b_timing_verdict":"hard_4c_more_important_than_4b","four_b_evidence_type":["price_only","credit_spread_drag"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_pf_drag_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"002990-2024-01-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C30-014790-S2WATCH","case_id":"C30-R10L71-014790-FALSEBREAK","symbol":"014790","company_name":"HL D&I","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE","loop_objective":"price_only_beta_guard","trigger_type":"Stage2-Watch","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":2145,"evidence_available_at_that_date":"small builder sector stress and price weakness, but no verified hard balance-sheet break at trigger","evidence_source":"sector credit-risk proxy + stock-web","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv","profile_path":"atlas/symbol_profiles/014/014790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.0,"MFE_90D_pct":4.0,"MFE_180D_pct":25.2,"MFE_1Y_pct":25.2,"MFE_2Y_pct":null,"MAE_30D_pct":-6.8,"MAE_90D_pct":-9.3,"MAE_180D_pct":-9.3,"MAE_1Y_pct":-9.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-05","peak_price":2685,"drawdown_after_peak_pct":-22.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.15,"four_b_full_window_peak_proximity":0.16,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"false_break","trigger_outcome_label":"false_break_recovery","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"014790-2024-01-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P2_C30_PF_BREAK_RECAP_SPLIT","profile_scope":"canonical_archetype_specific","profile_hypothesis":"split hard balance-sheet break from recapitalization rescue and price-only beta","changed_axes":["hard_4c_requires_verified_balance_sheet_break","recapitalization_bridge_demotes_to_watch","price_only_beta_cannot_route_to_4c"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":["TR-C30-034300-S2WATCH","TR-C30-002990-S2RISK","TR-C30-014790-S2WATCH"],"avg_MFE_90D_pct":7.9,"avg_MAE_90D_pct":-11.5,"avg_MFE_180D_pct":29.5,"avg_MAE_180D_pct":-18.6,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.22,"avg_four_b_full_window_peak_proximity":0.23,"score_return_alignment_verdict":"improved_vs_P0"}
{"row_type":"residual_contribution","round":"R10","loop":"71","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["hard_4c_false_positive_when_recapitalization_bridge_exists","missed_hard_4c_when_pf_drag_persists","price_only_pf_beta_overrouting"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count narrative_only rows as calibration evidence.
- Do not treat price-only construction beta as hard 4C.
- Split C30 into hard balance-sheet break, recapitalization rescue bridge, and price-only beta watch.
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

## 27. Next Round State

```yaml
current_round_completed: R10
current_loop_completed: 71
computed_next_round: R11
computed_next_loop: 71
next_large_sector_allowed: L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
```

## 28. Source Notes

- Main execution prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price source: Songdaiki/stock-web, tradable_raw, raw_unadjusted_marcap.
- Public sector context: Reuters, South Korea prepares financial support for small businesses, builders, 2024-03-27.
- Quantitative rows are based on stock-web visible OHLC rows and rounded to one decimal point.

