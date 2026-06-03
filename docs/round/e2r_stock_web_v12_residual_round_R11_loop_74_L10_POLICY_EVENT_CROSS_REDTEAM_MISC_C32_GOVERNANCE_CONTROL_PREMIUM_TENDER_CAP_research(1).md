# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R11
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R12
computed_next_loop: 74
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: C32_TENDER_CASH_CAP_CONTROL_PREMIUM_RESOLUTION_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r11_branch: L10_policy_event_governance_branch
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

R11 allows either L10 policy/event cross-red-team or an L1 defense-linked branch. The previous R11 loop used the defense-linked C03 branch, so this run rotates to L10/C32. The target is governance/control premium: explicit tender/cash-price and control-premium bridges can work, but privatization, activism, or governance heat without a durable cash floor should be demoted.

| layer | id | definition |
|---|---|---|
| round | R11 | policy/event cross round |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy, governance, tender, control premium, special situations |
| canonical | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | governance/control premium/tender cap |
| fine | C32_TENDER_CASH_CAP_CONTROL_PREMIUM_RESOLUTION_BRIDGE_GUARD | governance signal must become tender/cash cap/control-premium evidence |
| deep | STRATEGIC_CONTROL_BATTLE_TENDER_PRICE_TO_CASH_CAP_AND_POST_PEAK_DECAY | tender bridge positive |
| deep | MEDIA_PRIVATIZATION_APPROVAL_THEME_WITHOUT_TENDER_CASH_PRICE_OR_EARNINGS_BRIDGE | privatization false positive |
| deep | SEMICONDUCTOR_HOLDCO_GOVERNANCE_OPTIONALITY_WITHOUT_CONTROL_PREMIUM_CAPITAL_RETURN_OR_EARNINGS_BRIDGE | activism/governance false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C32 top-covered symbols are `010130`, `041510`, `008930`, `011200`, `UNKNOWN_SYMBOL`, and `003920`. This run avoids that cluster and also avoids the prior R11/C03 defense-linked symbols.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C32 | 036560 | new independent | not top-covered C32 symbol; explicit tender/control-premium cash cap bridge |
| C32 | 040300 | new independent | not top-covered C32 symbol; privatization/control theme without incremental cash bridge |
| C32 | 000990 | new independent | not top-covered C32 symbol; activism/governance theme without tender/capital-return bridge |
| excluded | 000670 | blocked | control-battle candidate inspected, but 2025-04-25 corporate-action candidate contaminates 180D forward window |

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
036560 has only a 2008-04-14 corporate-action candidate, outside the selected 2024 representative window.
040300 has no corporate-action candidate dates.
000990 has no corporate-action candidate contamination in the selected 2024 representative window.
000670/영풍 was inspected as a control-battle peer, but its 2025-04-25 corporate-action candidate overlaps the post-2024-09-13 180D window, so it is excluded from representative calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| tender_control_premium_success_then_4B_cap_watch | 036560 | 영풍정밀/KZ정밀 | Stage2-Actionable | 2024-09-13 | 12180 | tender/control-premium cash cap bridge worked, then decayed |
| privatization_theme_failed_after_weak_control_premium_bridge | 040300 | YTN | Stage2-Actionable | 2024-02-05 | 5840 | privatization event MFE lacked incremental tender/cash bridge |
| activism_governance_theme_mfe_then_high_mae_counterexample | 000990 | DB하이텍 | Stage2-Actionable | 2024-04-01 | 46900 | activism/governance MFE lacked tender/capital-return bridge |

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
| 036560 | 영풍정밀/KZ정밀 | Stage2-Actionable | 2024-09-13 | 12180 | 201.31 | 201.31 | 201.31 | 0.0 | -2.38 | -14.12 | 2024-10-07 | 36700 | -71.5 |
| 040300 | YTN | Stage2-Actionable | 2024-02-05 | 5840 | 12.67 | 12.67 | 12.67 | -25.77 | -45.72 | -56.76 | 2024-02-07 | 6580 | -61.63 |
| 000990 | DB하이텍 | Stage2-Actionable | 2024-04-01 | 46900 | 1.92 | 18.34 | 20.47 | -8.42 | -8.42 | -24.95 | 2024-08-01 | 56500 | -37.7 |

## 9. Case-by-Case Notes

### 9.1 036560 / 영풍정밀-KZ정밀 — tender/control-premium bridge

The entry row is 2024-09-13 at 12,180. The price reached 36,700 as the control-premium and tender/cash-price bridge became explicit. This is a valid C32 positive, but the post-peak low reached 10,460. The tender price behaves like a ceiling/floor mechanism, not a perpetual earnings engine. Once the event probability resolves or the tender cap becomes visible, 4B watch must dominate.

### 9.2 040300 / YTN — privatization theme without incremental cash bridge

The entry row is 2024-02-05 at 5,840. The price reached 6,580, but later fell to 2,525. Privatization/control theme alone was not enough. Without incremental tender cash, a hard control-premium floor, capital return, or earnings bridge, the event became a short flare rather than a durable Stage3 case.

### 9.3 000990 / DB하이텍 — activism/governance theme without tender or capital-return bridge

The entry row is 2024-04-01 at 46,900. The later high reached 56,500, but the path subsequently fell to 35,200. Governance or activism optionality can create MFE, yet if no tender/cash-price floor, capital-return execution, ownership resolution, or durable earnings bridge appears, the move should remain 4B/high-MAE watch.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C32 treats governance/privatization/activism theme strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C32 needs tender/cash cap/control-premium/resolution bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for event peaks and tender-cap decays. |
| Full 4B non-price requirement appropriate? | Yes. 036560 has explicit bridge evidence; 040300/000990 do not. |
| 4C timing issue? | High-MAE and post-event decay watch are useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
036560:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after explicit tender/cash cap and control-premium bridge
  Stage3-Green = reject because tender cap and post-peak event decay require 4B watch

040300:
  Stage2-Actionable = acceptable only as event watch
  Stage3-Yellow = reject without incremental tender/cash-price or earnings bridge
  Stage3-Green = reject

000990:
  Stage2-Actionable = acceptable only as activism/governance watch
  Stage3-Yellow = reject without capital-return execution, tender floor, control premium, or ownership resolution
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 036560 | 0.97 | 1.00 | tender/control-premium positive but cash-cap 4B watch |
| 040300 | 1.00 | 1.00 | privatization event local 4B watch, not positive stage |
| 000990 | 0.84 | 1.00 | governance theme MFE but no control-premium bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c32_requires_tender_cash_cap_control_premium_resolution_bridge

rule:
  For C32 governance/control-premium/tender rows, do not promote governance,
  privatization, activism, ownership-dispute, value-up, or control-theme Stage2
  signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  explicit tender/cash-price floor, control-premium economics, capital-return execution,
  ownership resolution, legally durable transaction probability, shareholder-meeting outcome,
  or earnings/cashflow bridge tied to the governance event.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 77.44 | -18.84 | 66.7% | too generous to governance/event theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 77.44 | -18.84 | 33.3% | safer but may miss 036560 |
| P1 sector_specific_candidate_profile | 3 | 77.44 | -18.84 | 66.7% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 201.31 | -2.38 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 15.5 | -27.07 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 036560 | current_profile_correct_with_4B_cap_guard | explicit tender/control-premium bridge aligned with MFE, but cap/decay requires 4B |
| 040300 | current_profile_false_positive | privatization theme lacked incremental cash or earnings bridge |
| 000990 | current_profile_false_positive_if_green | activism/governance MFE lacked tender/capital-return bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | C32_TENDER_CASH_CAP_CONTROL_PREMIUM_RESOLUTION_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R11 L10/C32 non-top-covered governance/control-premium residual reduced |

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
- governance theme without tender/cash bridge
- tender control-premium winner needs 4B cap watch
- privatization theme high-MAE without incremental cash floor
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
- R11 allowed L10 policy-event governance branch consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure URLs
- exact tender document URLs
- production scoring behavior
- live candidate status
- 000670/영풍 as representative row because a 2025-04-25 corporate-action candidate overlaps the post-2024-09-13 180D window
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_requires_tender_cash_cap_control_premium_resolution_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"C32 governance/control-premium rows should not promote toward Stage3-Yellow/Green unless governance event converts into explicit tender/cash-price floor, control-premium, capital-return execution, ownership resolution, event-probability bridge, or legally durable transaction economics","036560 survives with strong MFE after tender/control-premium bridge; 040300 and 000990 fail when privatization/activism themes lack incremental cash-price or capital-return bridge","TRG_R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE|TRG_R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE|TRG_R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R11 L10 governance branch"
shadow_weight,c32_tender_cap_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,1,1,0,"Governance/control-premium winners and theme failures can peak before ownership resolution is completed; local/full-window 4B and high-MAE watch should remain active","preserves 036560 tender bridge positive while preventing 040300/000990 governance-theme false positives","TRG_R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE|TRG_R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE|TRG_R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE","symbol":"036560","company_name":"영풍정밀/KZ정밀","round":"R11","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_TENDER_CONTROL_PREMIUM_CASH_PRICE_CAP_BRIDGE","deep_sub_archetype_id":"STRATEGIC_CONTROL_BATTLE_TENDER_PRICE_TO_CASH_CAP_AND_POST_PEAK_DECAY","case_type":"tender_control_premium_success_then_4B_cap_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_4B_cap_guard","price_source":"Songdaiki/stock-web","notes":"R11 uses L10/C32 governance/control-premium branch. C32 rows require explicit tender/cash-price floor, control-premium, capital-return execution, ownership resolution, or event-probability bridge; governance/event theme alone is insufficient."}
{"row_type":"case","case_id":"R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE","symbol":"040300","company_name":"YTN","round":"R11","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_PRIVATIZATION_CONTROL_THEME_WITHOUT_INCREMENTAL_CASH_BRIDGE","deep_sub_archetype_id":"MEDIA_PRIVATIZATION_APPROVAL_THEME_WITHOUT_TENDER_CASH_PRICE_OR_EARNINGS_BRIDGE","case_type":"privatization_theme_failed_after_weak_control_premium_bridge","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R11 uses L10/C32 governance/control-premium branch. C32 rows require explicit tender/cash-price floor, control-premium, capital-return execution, ownership resolution, or event-probability bridge; governance/event theme alone is insufficient."}
{"row_type":"case","case_id":"R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE","symbol":"000990","company_name":"DB하이텍","round":"R11","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_ACTIVISM_GOVERNANCE_THEME_WITHOUT_TENDER_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"SEMICONDUCTOR_HOLDCO_GOVERNANCE_OPTIONALITY_WITHOUT_CONTROL_PREMIUM_CAPITAL_RETURN_OR_EARNINGS_BRIDGE","case_type":"activism_governance_theme_mfe_then_high_mae_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R11 uses L10/C32 governance/control-premium branch. C32 rows require explicit tender/cash-price floor, control-premium, capital-return execution, ownership resolution, or event-probability bridge; governance/event theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE","case_id":"R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE","symbol":"036560","company_name":"영풍정밀/KZ정밀","round":"R11","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_TENDER_CONTROL_PREMIUM_CASH_PRICE_CAP_BRIDGE","deep_sub_archetype_id":"STRATEGIC_CONTROL_BATTLE_TENDER_PRICE_TO_CASH_CAP_AND_POST_PEAK_DECAY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":12180,"evidence_available_at_that_date":"source_proxy_control_battle_tender_price_cash_cap_bridge; evidence_url_pending","evidence_source":"source_proxy_control_battle_tender_price_cash_cap_bridge; evidence_url_pending","bridge_summary":"control battle and tender/cash-price route converted into explicit control-premium bridge, but tender cap and post-peak decay required 4B watch","stage2_evidence_fields":["control_battle","tender_price_reference","cash_price_cap","relative_strength"],"stage3_evidence_fields":["tender_price_to_cash_cap_visibility","control_premium_bridge","event_probability_bridge"],"stage4b_evidence_fields":["tender_price_cap_watch","post_event_decay_watch","control_premium_crowding"],"stage4c_evidence_fields":["post_peak_decay_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv|atlas/ohlcv_tradable_by_symbol_year/036/036560/2025.csv","profile_path":"atlas/symbol_profiles/036/036560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":201.31,"MFE_90D_pct":201.31,"MFE_180D_pct":201.31,"MFE_1Y_pct":201.31,"MFE_2Y_pct":201.31,"MAE_30D_pct":0.0,"MAE_90D_pct":-2.38,"MAE_180D_pct":-14.12,"MAE_1Y_pct":-14.12,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-10-07","peak_price":36700,"drawdown_after_peak_pct":-71.5,"green_lateness_ratio":"0.29","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"tender_control_premium_positive_but_cash_cap_4B_watch","four_b_evidence_type":"non_price_tender_control_premium_cash_cap_bridge","four_c_protection_label":"post_peak_decay_watch","trigger_outcome_label":"tender_control_premium_success_then_decay","current_profile_verdict":"current_profile_correct_with_4B_cap_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE","case_id":"R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE","symbol":"040300","company_name":"YTN","round":"R11","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_PRIVATIZATION_CONTROL_THEME_WITHOUT_INCREMENTAL_CASH_BRIDGE","deep_sub_archetype_id":"MEDIA_PRIVATIZATION_APPROVAL_THEME_WITHOUT_TENDER_CASH_PRICE_OR_EARNINGS_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":5840,"evidence_available_at_that_date":"source_proxy_media_privatization_control_theme_without_incremental_tender_cash_price_or_earnings_bridge; evidence_url_pending","evidence_source":"source_proxy_media_privatization_control_theme_without_incremental_tender_cash_price_or_earnings_bridge; evidence_url_pending","bridge_summary":"privatization/control theme produced a short MFE spike, but incremental tender/cash-price, control-premium floor, capital return, or earnings bridge did not follow","stage2_evidence_fields":["privatization_control_theme","event_approval_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_local_peak","tender_cash_bridge_absent","control_premium_floor_absent"],"stage4c_evidence_fields":["high_MAE_without_cash_price_or_earnings_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv","profile_path":"atlas/symbol_profiles/040/040300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.67,"MFE_90D_pct":12.67,"MFE_180D_pct":12.67,"MFE_1Y_pct":12.67,"MFE_2Y_pct":12.67,"MAE_30D_pct":-25.77,"MAE_90D_pct":-45.72,"MAE_180D_pct":-56.76,"MAE_1Y_pct":-56.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-07","peak_price":6580,"drawdown_after_peak_pct":-61.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"privatization_event_local_4B_watch_not_positive_stage","four_b_evidence_type":"governance_theme_without_tender_cash_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_privatisation_control_theme_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE","case_id":"R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE","symbol":"000990","company_name":"DB하이텍","round":"R11","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_ACTIVISM_GOVERNANCE_THEME_WITHOUT_TENDER_CAPITAL_RETURN_BRIDGE","deep_sub_archetype_id":"SEMICONDUCTOR_HOLDCO_GOVERNANCE_OPTIONALITY_WITHOUT_CONTROL_PREMIUM_CAPITAL_RETURN_OR_EARNINGS_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":46900,"evidence_available_at_that_date":"source_proxy_activism_governance_theme_without_tender_capital_return_or_earnings_bridge; evidence_url_pending","evidence_source":"source_proxy_activism_governance_theme_without_tender_capital_return_or_earnings_bridge; evidence_url_pending","bridge_summary":"governance/activism optionality produced MFE, but no explicit tender, cash-price floor, capital-return execution, control premium, or durable earnings bridge followed","stage2_evidence_fields":["governance_activism_theme","valueup_or_holdco_discount_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["governance_theme_peak","tender_bridge_absent","capital_return_execution_absent"],"stage4c_evidence_fields":["high_MAE_without_tender_or_capital_return_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv","profile_path":"atlas/symbol_profiles/000/000990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.92,"MFE_90D_pct":18.34,"MFE_180D_pct":20.47,"MFE_1Y_pct":20.47,"MFE_2Y_pct":20.47,"MAE_30D_pct":-8.42,"MAE_90D_pct":-8.42,"MAE_180D_pct":-24.95,"MAE_1Y_pct":-24.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-01","peak_price":56500,"drawdown_after_peak_pct":-37.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"governance_theme_MFE_but_no_control_premium_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"governance_theme_without_tender_cash_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"activism_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE","trigger_id":"TRG_R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE","symbol":"036560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"governance_event_score":12,"tender_cash_cap_score":14,"control_premium_score":14,"capital_return_or_resolution_score":9,"relative_strength_score":12,"risk_penalty":6},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"governance_event_score":11,"tender_cash_cap_score":17,"control_premium_score":16,"capital_return_or_resolution_score":10,"relative_strength_score":9,"risk_penalty":10},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["governance_event_score","tender_cash_cap_score","control_premium_score","capital_return_or_resolution_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C32 row is promoted only because governance/control battle converts into explicit tender/cash-price and control-premium bridge; 4B cap watch blocks Green.","MFE_90D_pct":201.31,"MAE_90D_pct":-2.38,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_4B_cap_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE","trigger_id":"TRG_R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE","symbol":"040300","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"governance_event_score":12,"tender_cash_cap_score":1,"control_premium_score":2,"capital_return_or_resolution_score":1,"relative_strength_score":10,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"governance_event_score":5,"tender_cash_cap_score":0,"control_premium_score":0,"capital_return_or_resolution_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["governance_event_score","tender_cash_cap_score","control_premium_score","capital_return_or_resolution_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C32 guard demotes governance/privatization/activism theme rows when tender cash cap, control-premium floor, capital-return execution, or ownership resolution bridge is absent.","MFE_90D_pct":12.67,"MAE_90D_pct":-45.72,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE","trigger_id":"TRG_R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE","symbol":"000990","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"governance_event_score":12,"tender_cash_cap_score":1,"control_premium_score":2,"capital_return_or_resolution_score":1,"relative_strength_score":10,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"governance_event_score":5,"tender_cash_cap_score":0,"control_premium_score":0,"capital_return_or_resolution_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["governance_event_score","tender_cash_cap_score","control_premium_score","capital_return_or_resolution_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C32 guard demotes governance/privatization/activism theme rows when tender cash cap, control-premium floor, capital-return execution, or ownership resolution bridge is absent.","MFE_90D_pct":18.34,"MAE_90D_pct":-8.42,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_requires_tender_cash_cap_control_premium_resolution_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"C32 governance/control-premium rows should not promote toward Stage3-Yellow/Green unless governance event converts into explicit tender/cash-price floor, control-premium, capital-return execution, ownership resolution, event-probability bridge, or legally durable transaction economics","036560 survives with strong MFE after tender/control-premium bridge; 040300 and 000990 fail when privatization/activism themes lack incremental cash-price or capital-return bridge","TRG_R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE|TRG_R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE|TRG_R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R11 L10 governance branch"
shadow_weight,c32_tender_cap_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,1,1,0,"Governance/control-premium winners and theme failures can peak before ownership resolution is completed; local/full-window 4B and high-MAE watch should remain active","preserves 036560 tender bridge positive while preventing 040300/000990 governance-theme false positives","TRG_R11L74_C32_036560_20240913_TENDER_CONTROL_PREMIUM_CASH_CAP_BRIDGE|TRG_R11L74_C32_040300_20240205_PRIVATIZATION_CONTROL_THEME_NO_INCREMENTAL_CASH_BRIDGE|TRG_R11L74_C32_000990_20240401_ACTIVISM_GOVERNANCE_THEME_NO_TENDER_CAPITAL_RETURN_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["governance_theme_without_tender_cash_bridge","tender_control_premium_winner_needs_4B_cap_watch","privatization_theme_high_MAE_without_incremental_cash_floor"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R11-specific handling

- R11 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or an L1 defense-linked branch.
- This MD uses the L10 governance/control-premium branch.
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
- price-only/governance-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R11 allowed L10 branch.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C32 governance/control-premium rows cannot promote without explicit tender/cash-price floor, control-premium economics, capital-return execution, ownership resolution, durable transaction probability, shareholder-meeting outcome, or governance-linked earnings/cashflow bridge.
13. Add validation that corporate-action-contaminated candidates like 000670 after 2025-04-25 are blocked from representative calibration rows unless adjusted/clean.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R11
completed_loop = 74
next_round = R12
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
atlas/symbol_profiles/036/036560.json
atlas/symbol_profiles/040/040300.json
atlas/symbol_profiles/000/000990.json
atlas/symbol_profiles/000/000670.json
atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/036/036560/2025.csv
atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000670/2024.csv
```

This loop continues loop 74 with R11 and adds 3 new independent C32 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R11/L10.
