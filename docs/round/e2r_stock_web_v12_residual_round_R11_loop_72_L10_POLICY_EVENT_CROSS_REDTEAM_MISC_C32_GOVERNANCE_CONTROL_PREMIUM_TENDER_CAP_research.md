# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R11
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R12
computed_next_loop: 72
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: C32_CONTROL_NAV_MINORITY_VALUE_BRIDGE_GUARD
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

R11 can use the L10 policy/event/governance branch or the L1 policy-defense/infra branch. This run uses the L10 governance branch and avoids repeating the prior R11 C31 policy/cashflow run. The C32 residual is simple: a governance headline is not a premium by itself. It becomes useful only when it turns into control premium, NAV discount narrowing, tender/control terms quality, shareholder-return execution, or minority shareholder value.

| layer | id | definition |
|---|---|---|
| round | R11 | policy/event/governance bridge |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy, event, governance, control premium |
| canonical | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | governance, control premium, tender/event cap |
| fine | C32_CONTROL_NAV_MINORITY_VALUE_BRIDGE_GUARD | governance event must become control/NAV/minority-value bridge |
| deep | HOLDCO_CONTROL_CONTEST_NAV_PREMIUM_WITH_VOLATILITY_GUARD | control contest premium success |
| deep | GROUP_RESTRUCTURING_NAV_DISCOUNT_NARROWING_WITH_CAPITAL_MARKET_OPTIONALITY | holdco restructuring/NAV success |
| deep | RESTRUCTURING_RATIO_CONTROVERSY_WITHOUT_MINORITY_VALUE_BRIDGE | governance ratio event false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C32 top-covered symbols are `010130`, `041510`, `008930`, `011200`, `UNKNOWN_SYMBOL`, and `003920`. This run avoids that top cluster and uses non-top-covered control/NAV/governance-ratio rows.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C32 | 180640 | new independent | not top-covered C32 symbol; control premium contest |
| C32 | 000150 | new independent | not top-covered C32 symbol; holdco/NAV restructuring rerating |
| C32 | 241560 | new independent | not top-covered C32 symbol; governance ratio/minority-value counterexample |

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

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_high_volatility_4B_watch | 180640 | 한진칼 | Stage2-Actionable | 2020-02-12 | 43500 | control premium contest worked but volatility guard required |
| structural_success_then_4B_watch | 000150 | 두산 | Stage2-Actionable | 2024-03-07 | 107900 | holdco/NAV restructuring bridge worked |
| failed_rerating_high_MAE_governance_ratio_counterexample | 241560 | 두산밥캣 | Stage2-Actionable | 2024-07-12 | 54600 | governance ratio/minority-value bridge absent failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 180640 | 한진칼 | Stage2-Actionable | 2020-02-12 | 43500 | 120.69 | 155.17 | 155.17 | -10.57 | -10.57 | -10.57 | 2020-04-20 | 111000 | -34.77 |
| 000150 | 두산 | Stage2-Actionable | 2024-03-07 | 107900 | 65.15 | 65.15 | 123.35 | -14.64 | -14.64 | -14.64 | 2024-07-11 | 241000 | -43.94 |
| 241560 | 두산밥캣 | Stage2-Actionable | 2024-07-12 | 54600 | 8.97 | 8.97 | 8.97 | -38.92 | -38.92 | -38.92 | 2024-07-12 | 59500 | -43.95 |

## 9. Case-by-Case Notes

### 9.1 180640 / 한진칼 — control premium contest with volatility guard

The entry row is 2020-02-12 at 43,500. The 90D path reaches 111,000, but the drawdown and COVID-era volatility are large enough that this is not a Green-loosening case. It validates C32 only when the non-price bridge is clear: control premium, shareholder optionality, and NAV premium. Governance here behaves like a bidding room; the price can move fast, but the exit door gets crowded.

### 9.2 000150 / 두산 — holdco restructuring and NAV discount narrowing

The entry row is 2024-03-07 at 107,900. The 30D path reaches 178,200 and the wider path reaches a higher restructuring/NAV rerating zone. This is a valid C32 positive because the event is not only “governance news”; it has holdco restructuring, NAV discount narrowing, and capital-market optionality.

### 9.3 241560 / 두산밥캣 — governance ratio event without minority-value bridge

The entry row is 2024-07-12 at 54,600. The same event window reaches 59,500, then the path falls to 33,350. This is the C32 trap: restructuring can create a premium for one part of a group while widening the discount for another if minority shareholder value and event terms quality are unclear.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C32 treats governance/restructuring headline or price spike as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C32 needs control/NAV/minority-value bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for governance-ratio and minority-value-risk rows. |
| Full 4B non-price requirement appropriate? | Yes. 180640/000150 have stronger non-price bridges; 241560 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
180640:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after control premium / shareholder optionality bridge
  Stage3-Green = reject unless volatility, terms, and exit-risk guards clear

000150:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after NAV/restructuring bridge
  Stage3-Green = wait for event terms and shareholder-value durability

241560:
  Stage2-Actionable = too generous if based only on restructuring headline and price spike
  Stage3-Yellow = reject without minority shareholder value / terms-quality bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 180640 | 0.86 | 1.00 | good full-window 4B watch after control premium bridge |
| 000150 | 0.94 | 1.00 | good full-window 4B watch after holdco/NAV bridge |
| 241560 | 1.00 | 1.00 | price/event local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c32_requires_control_NAV_minority_value_bridge

rule:
  For C32 governance/control-premium/tender rows, do not promote governance, tender,
  restructuring, or control-event Stage2 signals into Stage3-Yellow/Green unless at least
  one non-price bridge is visible:
  control premium durability, NAV discount narrowing, tender/control terms quality,
  shareholder-return execution, minority shareholder value protection,
  legal/board clarity, or FCF/capital allocation improvement after the event.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 76.43 | -21.38 | 33.3% | useful but can over-credit governance-ratio headlines |
| P0b e2r_2_0_baseline_reference | 3 | 76.43 | -21.38 | 0% | safer but may miss control/NAV premium winners |
| P1 sector_specific_candidate_profile | 3 | 76.43 | -21.38 | 33.3% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 110.16 | -12.61 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 8.97 | -38.92 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 180640 | current_profile_correct_but_needs_volatility_guard | control premium bridge aligned with high MFE but also high volatility |
| 000150 | current_profile_correct | holdco/NAV restructuring bridge aligned with strong MFE |
| 241560 | current_profile_false_positive | governance ratio event produced high MAE without minority-value bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32_CONTROL_NAV_MINORITY_VALUE_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C32 non-top-covered governance/control/NAV residual reduced |

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
- governance ratio event without minority value bridge
- control premium winner needs 4B watch
- holdco NAV restructuring success with peak guard
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
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
shadow_weight,c32_requires_control_NAV_minority_value_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"C32 governance rows should not promote toward Stage3-Yellow/Green unless governance event converts into control premium, NAV discount narrowing, tender/control terms quality, shareholder-return execution, or minority shareholder value bridge","180640 and 000150 survive with large MFE after control/NAV bridge; 241560 fails when restructuring ratio event lacks minority value bridge","TRG_R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE|TRG_R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING|TRG_R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_governance_event_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,1,1,0,"Governance/control-premium winners and ratio-event failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 180640/000150 positives while preventing 241560 governance-ratio false positive","TRG_R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE|TRG_R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING|TRG_R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE","symbol":"180640","company_name":"한진칼","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_CONTROL_PREMIUM_CONTEST_WITH_SHAREHOLDER_OPTIONALITY","deep_sub_archetype_id":"HOLDCO_CONTROL_CONTEST_NAV_PREMIUM_WITH_VOLATILITY_GUARD","case_type":"structural_success_high_volatility_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_needs_volatility_guard","price_source":"Songdaiki/stock-web","notes":"C32 governance rows require control premium, NAV discount narrowing, tender/control terms, or minority shareholder value bridge; governance headline alone is insufficient."}
{"row_type":"case","case_id":"R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING","symbol":"000150","company_name":"두산","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_HOLDCO_RESTRUCTURING_NAV_RERATING_BRIDGE","deep_sub_archetype_id":"GROUP_RESTRUCTURING_NAV_DISCOUNT_NARROWING_WITH_CAPITAL_MARKET_OPTIONALITY","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C32 governance rows require control premium, NAV discount narrowing, tender/control terms, or minority shareholder value bridge; governance headline alone is insufficient."}
{"row_type":"case","case_id":"R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING","symbol":"241560","company_name":"두산밥캣","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_GOVERNANCE_RATIO_EVENT_PREMIUM_CAP_GUARD","deep_sub_archetype_id":"RESTRUCTURING_RATIO_CONTROVERSY_WITHOUT_MINORITY_VALUE_BRIDGE","case_type":"failed_rerating_high_MAE_governance_ratio_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C32 governance rows require control premium, NAV discount narrowing, tender/control terms, or minority shareholder value bridge; governance headline alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE","case_id":"R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE","symbol":"180640","company_name":"한진칼","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_CONTROL_PREMIUM_CONTEST_WITH_SHAREHOLDER_OPTIONALITY","deep_sub_archetype_id":"HOLDCO_CONTROL_CONTEST_NAV_PREMIUM_WITH_VOLATILITY_GUARD","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2020-02-12","entry_date":"2020-02-12","entry_price":43500,"evidence_available_at_that_date":"source_proxy_control_premium_contest_and_shareholder_optionality; evidence_url_pending","evidence_source":"source_proxy_control_premium_contest_and_shareholder_optionality; evidence_url_pending","bridge_summary":"control-premium contest and shareholder optionality created a genuine governance premium path, but volatility required 4B/high-MAE watch rather than Green loosening","stage2_evidence_fields":["control_premium_contest","shareholder_optionality","relative_strength","NAV_premium_optional_bridge"],"stage3_evidence_fields":["control_premium_durability","governance_event_visibility","non_price_control_bridge"],"stage4b_evidence_fields":["control_premium_crowding","post_MFE_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv","profile_path":"atlas/symbol_profiles/180/180640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":120.69,"MFE_90D_pct":155.17,"MFE_180D_pct":155.17,"MFE_1Y_pct":155.17,"MFE_2Y_pct":155.17,"MAE_30D_pct":-10.57,"MAE_90D_pct":-10.57,"MAE_180D_pct":-10.57,"MAE_1Y_pct":-10.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-04-20","peak_price":111000,"drawdown_after_peak_pct":-34.77,"green_lateness_ratio":"0.29","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_control_premium_bridge","four_b_evidence_type":"non_price_control_NAV_value_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_high_volatility_then_4B_watch","current_profile_verdict":"current_profile_correct_but_needs_volatility_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING","case_id":"R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING","symbol":"000150","company_name":"두산","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_HOLDCO_RESTRUCTURING_NAV_RERATING_BRIDGE","deep_sub_archetype_id":"GROUP_RESTRUCTURING_NAV_DISCOUNT_NARROWING_WITH_CAPITAL_MARKET_OPTIONALITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":107900,"evidence_available_at_that_date":"source_proxy_holdco_restructuring_NAV_discount_narrowing_and_capital_market_optionality; evidence_url_pending","evidence_source":"source_proxy_holdco_restructuring_NAV_discount_narrowing_and_capital_market_optionality; evidence_url_pending","bridge_summary":"holdco restructuring/NAV rerating worked when the governance event was accompanied by capital-market optionality and discount-narrowing evidence","stage2_evidence_fields":["holdco_restructuring","NAV_discount_narrowing","relative_strength","capital_market_optionality"],"stage3_evidence_fields":["restructuring_visibility","NAV_value_bridge","shareholder_value_optionality"],"stage4b_evidence_fields":["post_MFE_peak_watch","governance_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000150/2024.csv","profile_path":"atlas/symbol_profiles/000/000150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":65.15,"MFE_90D_pct":65.15,"MFE_180D_pct":123.35,"MFE_1Y_pct":123.35,"MFE_2Y_pct":123.35,"MAE_30D_pct":-14.64,"MAE_90D_pct":-14.64,"MAE_180D_pct":-14.64,"MAE_1Y_pct":-14.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":241000,"drawdown_after_peak_pct":-43.94,"green_lateness_ratio":"0.37","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_holdco_NAV_restructuring_bridge","four_b_evidence_type":"non_price_control_NAV_value_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING","case_id":"R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING","symbol":"241560","company_name":"두산밥캣","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_GOVERNANCE_RATIO_EVENT_PREMIUM_CAP_GUARD","deep_sub_archetype_id":"RESTRUCTURING_RATIO_CONTROVERSY_WITHOUT_MINORITY_VALUE_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-12","entry_date":"2024-07-12","entry_price":54600,"evidence_available_at_that_date":"source_proxy_group_restructuring_ratio_event_without_minority_shareholder_value_bridge; evidence_url_pending","evidence_source":"source_proxy_group_restructuring_ratio_event_without_minority_shareholder_value_bridge; evidence_url_pending","bridge_summary":"governance/restructuring headline lacked minority shareholder value bridge and discount narrowing; local premium became high-MAE governance discount widening","stage2_evidence_fields":["governance_restructuring_event","ratio_or_terms_uncertainty","price_spike"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","minority_value_bridge_absent","governance_discount_widening"],"stage4c_evidence_fields":["high_MAE_after_governance_terms_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv","profile_path":"atlas/symbol_profiles/241/241560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.97,"MFE_90D_pct":8.97,"MFE_180D_pct":8.97,"MFE_1Y_pct":8.97,"MFE_2Y_pct":8.97,"MAE_30D_pct":-38.92,"MAE_90D_pct":-38.92,"MAE_180D_pct":-38.92,"MAE_1Y_pct":-38.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-12","peak_price":59500,"drawdown_after_peak_pct":-43.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_event_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_event_without_minority_value_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE","trigger_id":"TRG_R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE","symbol":"180640","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"control_premium_score":12,"NAV_discount_bridge_score":10,"shareholder_value_bridge_score":9,"event_terms_quality_score":8,"relative_strength_score":10,"governance_terms_risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"control_premium_score":15,"NAV_discount_bridge_score":13,"shareholder_value_bridge_score":12,"event_terms_quality_score":10,"relative_strength_score":8,"governance_terms_risk_penalty":5},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["control_premium_score","NAV_discount_bridge_score","shareholder_value_bridge_score","event_terms_quality_score","relative_strength_score","governance_terms_risk_penalty"],"component_delta_explanation":"C32 row is promoted only because governance event converts into control premium, NAV discount narrowing, or shareholder value bridge.","MFE_90D_pct":155.17,"MAE_90D_pct":-10.57,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_needs_volatility_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING","trigger_id":"TRG_R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING","symbol":"000150","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"control_premium_score":12,"NAV_discount_bridge_score":10,"shareholder_value_bridge_score":9,"event_terms_quality_score":8,"relative_strength_score":10,"governance_terms_risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"control_premium_score":15,"NAV_discount_bridge_score":13,"shareholder_value_bridge_score":12,"event_terms_quality_score":10,"relative_strength_score":8,"governance_terms_risk_penalty":5},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["control_premium_score","NAV_discount_bridge_score","shareholder_value_bridge_score","event_terms_quality_score","relative_strength_score","governance_terms_risk_penalty"],"component_delta_explanation":"C32 row is promoted only because governance event converts into control premium, NAV discount narrowing, or shareholder value bridge.","MFE_90D_pct":65.15,"MAE_90D_pct":-14.64,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING","trigger_id":"TRG_R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING","symbol":"241560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"control_premium_score":6,"NAV_discount_bridge_score":1,"shareholder_value_bridge_score":0,"event_terms_quality_score":1,"relative_strength_score":12,"governance_terms_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"control_premium_score":3,"NAV_discount_bridge_score":0,"shareholder_value_bridge_score":0,"event_terms_quality_score":0,"relative_strength_score":5,"governance_terms_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["control_premium_score","NAV_discount_bridge_score","shareholder_value_bridge_score","event_terms_quality_score","relative_strength_score","governance_terms_risk_penalty"],"component_delta_explanation":"C32 guard demotes governance/restructuring price spikes when minority value, NAV, tender/control terms, or shareholder-return bridge is absent.","MFE_90D_pct":8.97,"MAE_90D_pct":-38.92,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_requires_control_NAV_minority_value_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"C32 governance rows should not promote toward Stage3-Yellow/Green unless governance event converts into control premium, NAV discount narrowing, tender/control terms quality, shareholder-return execution, or minority shareholder value bridge","180640 and 000150 survive with large MFE after control/NAV bridge; 241560 fails when restructuring ratio event lacks minority value bridge","TRG_R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE|TRG_R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING|TRG_R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_governance_event_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,1,1,0,"Governance/control-premium winners and ratio-event failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 180640/000150 positives while preventing 241560 governance-ratio false positive","TRG_R11L72_C32_180640_20200212_CONTROL_PREMIUM_CONTEST_BRIDGE|TRG_R11L72_C32_000150_20240307_HOLDCO_RESTRUCTURING_NAV_RERATING|TRG_R11L72_C32_241560_20240712_GOVERNANCE_RATIO_EVENT_DISCOUNT_WIDENING",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["governance_ratio_event_without_minority_value_bridge","control_premium_winner_needs_4B_watch","holdco_NAV_restructuring_success_with_peak_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
11. Add validation that C32 price-only governance headlines cannot promote without terms-quality or minority-value bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R11
completed_loop = 72
next_round = R12
next_loop = 72
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
atlas/symbol_profiles/180/180640.json
atlas/symbol_profiles/000/000150.json
atlas/symbol_profiles/241/241560.json
atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv
atlas/ohlcv_tradable_by_symbol_year/000/000150/2024.csv
atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv
```

This loop adds 3 new independent C32 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R11/L10.
