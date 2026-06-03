# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R12
scheduled_loop = 75
completed_round = R12
completed_loop = 75
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT
output_file = e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP.

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

This round tests whether the C32 event engine can separate the equity receiving the control premium from the equity paying for it. A takeover headline is like a bridge: the target may be standing on the toll booth, while the bidder may be carrying the debt-financed concrete. One headline, two balance sheets.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R12 |
| scheduled_loop | 75 |
| selected large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| fine_archetype_id | HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test |
| next_round | R13 |
| next_loop | 75 |

## 3. Previous Coverage / Duplicate Avoidance Check

Prior R12 C32 local outputs already covered SM, 고려아연, 한미사이언스, YTN, 한진칼, 금호석유화학, DB하이텍, 남양유업, 카카오, and 영풍-style governance/control-premium paths. This file avoids those symbol/date groups and uses a new shipping privatization sample: HMM target, Pan Ocean bidder-financing vehicle, and Harim parent-company event squeeze.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 3
new_independent_case_count = 3
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

All representative rows use `tradable_raw` OHLC from the calibration shard. Raw shards are not used for weight calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | corporate_action_window_status | forward_window_trading_days | calibration_usable | block_reasons |
|---|---:|---|---|---:|---|---|
| R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C | 011200 | atlas/symbol_profiles/011/011200.json | clean_180D_window | 180 | true | [] |
| R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION | 028670 | atlas/symbol_profiles/028/028670.json | clean_180D_window | 180 | true | [] |
| R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF | 136480 | atlas/symbol_profiles/136/136480.json | clean_180D_window | 180 | true | [] |

Asiana/Korean Air was considered but blocked as narrative-only because the relevant 2020 acquisition entry windows overlap stock-web corporate-action candidate dates in 2021.

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
compression_reason = target-side control sale, bidder-side financing burden, and parent-company event squeeze all belong to C32 but require issuer-role split before score promotion.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | case_type | entry_date | entry_price | MFE90 / MAE90 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---|---|
| R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C | 011200 | HMM | positive | 4C_success | 2023-12-19 | 18,430 | 26.42 / -22.68 | current_profile_4C_too_late |
| R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION | 028670 | 팬오션 | counterexample | failed_rerating | 2023-12-19 | 4,095 | 23.57 / -14.53 | current_profile_false_positive |
| R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF | 136480 | 하림 | counterexample | 4B_overlay_success | 2023-12-19 | 3,775 | 66.89 / -22.65 | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
```

The positive is not a durable operating rerating. It is a valid target-side event premium that later needs 4C routing when the sale bridge breaks. The two counterexamples keep C32 from becoming a headline chaser.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|
| R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C | HMM privatization preferred-bidder selection created a target-side control-sale event premium. The price path validates the event premium, but later negotiation failure makes the same case a 4C timing audit rather than a durable operating rerating. | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | multiple_public_sources | valuation_blowoff, control_premium_or_event_premium, explicit_event_cap | legal_or_regulatory_block, thesis_evidence_broken |
| R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION | The HMM sale headline was not a target-side premium for Pan Ocean. It was bidder-side financing and balance-sheet burden. Later shipping-cycle recovery should not be attributed to C32 control premium. | public_event_or_disclosure, relative_strength | - | capital_raise_or_overhang, valuation_blowoff, margin_or_backlog_slowdown | thesis_evidence_broken |
| R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF | Harim received a parent-company event premium from being named the HMM preferred bidder. The stock-web path shows a violent event squeeze followed by a deep retracement, so the correct use is 4B overlay / event-cap, not Stage3 promotion. | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | multiple_public_sources | valuation_blowoff, positioning_overheat, capital_raise_or_overhang, explicit_event_cap | thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | profile caveat |
|---:|---|---|---|---|
| 011200 | HMM | atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv; atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv | atlas/symbol_profiles/011/011200.json | clean_180D_window; nearest profile candidate 2023-11-10 before entry |
| 028670 | 팬오션 | atlas/ohlcv_tradable_by_symbol_year/028/028670/2023.csv; atlas/ohlcv_tradable_by_symbol_year/028/028670/2024.csv | atlas/symbol_profiles/028/028670.json | clean_180D_window; profile candidates all before 2016 |
| 136480 | 하림 | atlas/ohlcv_tradable_by_symbol_year/136/136480/2023.csv; atlas/ohlcv_tradable_by_symbol_year/136/136480/2024.csv | atlas/symbol_profiles/136/136480.json | clean_180D_window; profile candidates 2017-12-22 and 2020-03-16 only |

## 11. Case-by-Case Trigger Grid

| case_id | representative_trigger | trigger_date | entry_date | aggregate_role | same_entry_group_id |
|---|---|---|---|---|---|
| R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C | TR_R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_20231219_STAGE2A | 2023-12-18 | 2023-12-19 | representative | R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_2023-12-19_18430 |
| R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION | TR_R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_20231219_STAGE2A | 2023-12-18 | 2023-12-19 | representative | R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_2023-12-19_4095 |
| R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF | TR_R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_20231219_STAGE2A | 2023-12-18 | 2023-12-19 | representative | R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_2023-12-19_3775 |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 011200 | 2023-12-19 | 18,430 | 26.42 | -10.2 | 26.42 | -22.68 | 26.42 | -22.68 | 2023-12-20 | 23,300 | -38.84 |
| 028670 | 2023-12-19 | 4,095 | 16.0 | -14.53 | 23.57 | -14.53 | 23.57 | -14.53 | 2024-02-29 | 5,060 | -25.79 |
| 136480 | 2023-12-19 | 3,775 | 66.89 | -12.45 | 66.89 | -22.65 | 66.89 | -22.65 | 2023-12-21 | 6,300 | -53.65 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | stress-test interpretation |
|---|---|---|
| R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C | current_profile_4C_too_late | Current profile can see the event premium, but stale positive risk remains if the negotiation break is routed late. |
| R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION | current_profile_false_positive | Bidder-side financing burden can be misread as positive C32 unless issuer-role split is explicit. |
| R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF | current_profile_4B_too_late | Parent-side event squeeze has huge MFE, but its retracement says 4B should dominate rather than Green promotion. |

Existing axis status:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
stage3_cross_evidence_green_buffer = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened_for_target_sale_breaks
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is assigned. The audit deliberately avoids using later price outcome to backfill a Green label.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | 4B verdict |
|---|---:|---:|---|
| R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C | 0.75 | 0.75 | good_local_event_cap_timing_but_requires_4C_on_negotiation_break |
| R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION | 1.0 | 0.68 | price_only_local_peak_was_too_early_for_full_cycle_but_valid_as_bidder_risk_overlay |
| R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF | 0.45 | 0.45 | non_price_bidder_financing_risk_should_have_capped_event_premium_before_stage3 |

## 16. 4C Protection Audit

HMM is the key 4C test: target-side premium was initially valid, but a failed negotiation/closing bridge should not wait for a deep price break before routing to 4C-watch. Harim and Pan Ocean are not target-side 4C cases; they are bidder/parent financing-burden guards.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule_name = shipping_privatization_target_vs_bidder_financing_split
hypothesis = In shipping privatization/acquisition events, the target can receive event-premium credit, but bidder/parent/financing vehicles require explicit funding clarity and accretion evidence before Stage2-Actionable or Stage3 promotion.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
rule_name = C32_issuer_role_split
new_axis_proposed = C32_issuer_role_split; C32_bidder_financing_burden_guard; C32_target_sale_4C_watch
```

C32 should ask a first question before scoring: who receives the control premium? If the answer is not the scored issuer, the event becomes a risk overlay unless financing clarity, accretion, or tender economics are explicit.

## 19. Before / After Backtest Comparison

| case_id | before score / label | after score / label | alignment |
|---|---|---|---|
| R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C | 82 / Stage3-Yellow if control-sale event is over-promoted | 76 / Stage2-Actionable + C32 4C-watch | aligned_after_4C_watch |
| R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION | 77 / Stage3-Yellow if event beta is misread as positive C32 | 62 / Watch/No-promote bidder financing guard | false_positive_avoided_after_guard |
| R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF | 81 / Stage3-Yellow if RS/event beta dominates | 65 / Stage2-watch + C32 4B event-cap overlay | 4B_overlay_alignment |

## 20. Score-Return Alignment Matrix

| profile_id | scope | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 | current_default | 3 | 38.96 | -19.95 | 0.67 | partially aligned but bidder-side false positives remain |
| P0b | rollback_reference | 3 | 38.96 | -19.95 | 0.33 | safer but misses target-side event premium |
| P1 | sector_specific_candidate_profile | 3 | 38.96 | -19.95 | 0.0 | best alignment for this loop |
| P2 | canonical_archetype_candidate_profile | 3 | 38.96 | -19.95 | 0.0 | canonical rule candidate |
| P3 | counterexample_guard_profile | 3 | 38.96 | -19.95 | 0.0 | guard passes counterexamples |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT | 1 | 2 | 2 | 1 | 3 | 0 | 5 | 3 | 3 | true | true | target/bidder split improved; still needs holdout beyond shipping privatization |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 1
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: bidder_side_financing_false_positive; parent_side_event_blowoff_4B_late; target_side_control_sale_4C_late; shipping_cycle_recovery_wrong_axis_attribution
new_axis_proposed: C32_issuer_role_split; C32_bidder_financing_burden_guard; C32_target_sale_4C_watch
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema fields
- profile-level corporate-action candidate windows for 011200, 028670, 136480
- entry_date / entry_price from tradable shard close rows
- 30D/90D/180D MFE and MAE from actual 1D OHLC high/low rows
- same_entry_group_id dedupe for representative versus 4B overlay rows
```

Not validated:

```text
- No current/live watchlist
- No investment recommendation
- No stock_agent production scoring code
- No brokerage/API execution
- No production patch
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_issuer_role_split,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Classify issuer as target/bidder/parent/financing vehicle before applying control-premium promotion.","Reduced bidder-side false positives while preserving HMM target premium",TR_R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_20231219_STAGE2A|TR_R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_20231219_STAGE2A|TR_R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_20231219_STAGE2A,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_bidder_financing_burden_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Bidder/parent stocks with funding burden cannot receive positive C32 promotion without visible accretion/financing clarity.","Pan Ocean/Harim entries become watch/4B overlays rather than false Stage3",TR_R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_20231219_STAGE2A|TR_R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_20231219_STAGE2A,2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_target_sale_4C_watch,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Target-side event premium remains valid until negotiation/closing failure appears; then route to 4C-watch quickly.","HMM target premium not erased, but stale positive is blocked after thesis break",TR_R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_20231219_STAGE2A|TR_R12L75_C32_011200_20231220_4B_EVENT_CAP,1,1,0,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C", "symbol": "011200", "company_name": "HMM", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_20231219_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_after_4C_watch", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "HMM privatization preferred-bidder selection created a target-side control-sale event premium. The price path validates the event premium, but later negotiation failure makes the same case a 4C timing audit rather than a durable operating rerating."}
{"row_type": "case", "case_id": "R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION", "symbol": "028670", "company_name": "팬오션", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_20231219_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_avoided_after_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The HMM sale headline was not a target-side premium for Pan Ocean. It was bidder-side financing and balance-sheet burden. Later shipping-cycle recovery should not be attributed to C32 control premium."}
{"row_type": "case", "case_id": "R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF", "symbol": "136480", "company_name": "하림", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_20231219_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "4B_overlay_alignment", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Harim received a parent-company event premium from being named the HMM preferred bidder. The stock-web path shows a violent event squeeze followed by a deep retracement, so the correct use is 4B overlay / event-cap, not Stage3 promotion."}
{"row_type": "trigger", "trigger_id": "TR_R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_20231219_STAGE2A", "case_id": "R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C", "symbol": "011200", "company_name": "HMM", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT", "sector": "shipping / acquisition financing / governance event", "primary_archetype": "control-premium target vs bidder financing split", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-18", "evidence_available_at_that_date": "HMM privatization preferred-bidder selection created a target-side control-sale event premium. The price path validates the event premium, but later negotiation failure makes the same case a 4C timing audit rather than a durable operating rerating.", "evidence_source": "public HMM privatization / preferred-bidder news; Songdaiki/stock-web tradable rows for 011200 2023-2024", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv; atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv", "profile_path": "atlas/symbol_profiles/011/011200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-19", "entry_price": 18430, "MFE_30D_pct": 26.42, "MFE_90D_pct": 26.42, "MFE_180D_pct": 26.42, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.2, "MAE_90D_pct": -22.68, "MAE_180D_pct": -22.68, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-20", "peak_price": 23300, "drawdown_after_peak_pct": -38.84, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "good_local_event_cap_timing_but_requires_4C_on_negotiation_break", "four_b_evidence_type": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "target_event_premium_success_but_legal_4C_needed", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; nearest profile candidate 2023-11-10 before entry", "same_entry_group_id": "R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_2023-12-19_18430", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_20231219_STAGE2A", "case_id": "R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION", "symbol": "028670", "company_name": "팬오션", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT", "sector": "shipping / acquisition financing / governance event", "primary_archetype": "control-premium target vs bidder financing split", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable-counterexample", "trigger_date": "2023-12-18", "evidence_available_at_that_date": "The HMM sale headline was not a target-side premium for Pan Ocean. It was bidder-side financing and balance-sheet burden. Later shipping-cycle recovery should not be attributed to C32 control premium.", "evidence_source": "public HMM/Harim-JKL preferred-bidder news; Songdaiki/stock-web tradable rows for 028670 2023-2024", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "valuation_blowoff", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028670/2023.csv; atlas/ohlcv_tradable_by_symbol_year/028/028670/2024.csv", "profile_path": "atlas/symbol_profiles/028/028670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-19", "entry_price": 4095, "MFE_30D_pct": 16.0, "MFE_90D_pct": 23.57, "MFE_180D_pct": 23.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.53, "MAE_90D_pct": -14.53, "MAE_180D_pct": -14.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-29", "peak_price": 5060, "drawdown_after_peak_pct": -25.79, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.68, "four_b_timing_verdict": "price_only_local_peak_was_too_early_for_full_cycle_but_valid_as_bidder_risk_overlay", "four_b_evidence_type": ["capital_raise_or_overhang", "valuation_blowoff", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bidder_side_financing_burden_confounded_by_shipping_recovery", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile candidates all before 2016", "same_entry_group_id": "R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_2023-12-19_4095", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_20231219_STAGE2A", "case_id": "R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF", "symbol": "136480", "company_name": "하림", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT", "sector": "shipping / acquisition financing / governance event", "primary_archetype": "control-premium target vs bidder financing split", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable-counterexample", "trigger_date": "2023-12-18", "evidence_available_at_that_date": "Harim received a parent-company event premium from being named the HMM preferred bidder. The stock-web path shows a violent event squeeze followed by a deep retracement, so the correct use is 4B overlay / event-cap, not Stage3 promotion.", "evidence_source": "public HMM/Harim-JKL preferred-bidder news; Songdaiki/stock-web tradable rows for 136480 2023-2024", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "capital_raise_or_overhang", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/136/136480/2023.csv; atlas/ohlcv_tradable_by_symbol_year/136/136480/2024.csv", "profile_path": "atlas/symbol_profiles/136/136480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-19", "entry_price": 3775, "MFE_30D_pct": 66.89, "MFE_90D_pct": 66.89, "MFE_180D_pct": 66.89, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.45, "MAE_90D_pct": -22.65, "MAE_180D_pct": -22.65, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-21", "peak_price": 6300, "drawdown_after_peak_pct": -53.65, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.45, "four_b_full_window_peak_proximity": 0.45, "four_b_timing_verdict": "non_price_bidder_financing_risk_should_have_capped_event_premium_before_stage3", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "capital_raise_or_overhang", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "parent_side_event_blowoff_then_deep_retrace", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile candidates 2017-12-22 and 2020-03-16 only", "same_entry_group_id": "R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_2023-12-19_3775", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R12L75_C32_011200_20231220_4B_EVENT_CAP", "case_id": "R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C", "symbol": "011200", "company_name": "HMM", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT", "sector": "shipping / acquisition financing / governance event", "primary_archetype": "4B event-cap overlay", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4B-overlay", "trigger_date": "2023-12-20", "entry_date": "2023-12-20", "entry_price": 22100, "evidence_available_at_that_date": "Local event-premium blowoff after preferred-bidder selection; overlay only, not a separate positive entry.", "evidence_source": "public HMM privatization / preferred-bidder news; Songdaiki/stock-web tradable rows for 011200 2023-2024", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011200/2023.csv; atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv", "profile_path": "atlas/symbol_profiles/011/011200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.43, "MFE_90D_pct": 5.43, "MFE_180D_pct": 5.43, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -35.52, "MAE_90D_pct": -35.52, "MAE_180D_pct": -35.52, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-20", "peak_price": 23300, "drawdown_after_peak_pct": -38.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "good_local_event_cap_timing_but_requires_4C_on_negotiation_break", "four_b_evidence_type": ["valuation_blowoff", "control_premium_or_event_premium", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4B_overlay_success_not_new_entry", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; nearest profile candidate 2023-11-10 before entry", "same_entry_group_id": "R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_2023-12-19_18430", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R12L75_C32_136480_20231221_4B_BLOWOFF_CAP", "case_id": "R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF", "symbol": "136480", "company_name": "하림", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT", "sector": "shipping / acquisition financing / governance event", "primary_archetype": "4B event-cap overlay", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4B-overlay", "trigger_date": "2023-12-21", "entry_date": "2023-12-21", "entry_price": 4910, "evidence_available_at_that_date": "Local event-premium blowoff after preferred-bidder selection; overlay only, not a separate positive entry.", "evidence_source": "public HMM/Harim-JKL preferred-bidder news; Songdaiki/stock-web tradable rows for 136480 2023-2024", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "capital_raise_or_overhang", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/136/136480/2023.csv; atlas/ohlcv_tradable_by_symbol_year/136/136480/2024.csv", "profile_path": "atlas/symbol_profiles/136/136480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.31, "MFE_90D_pct": 28.31, "MFE_180D_pct": 28.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -40.53, "MAE_90D_pct": -40.53, "MAE_180D_pct": -40.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-21", "peak_price": 6300, "drawdown_after_peak_pct": -53.65, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.45, "four_b_full_window_peak_proximity": 0.45, "four_b_timing_verdict": "non_price_bidder_financing_risk_should_have_capped_event_premium_before_stage3", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "capital_raise_or_overhang", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_not_new_entry", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile candidates 2017-12-22 and 2020-03-16 only", "same_entry_group_id": "R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_2023-12-19_3775", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C", "trigger_id": "TR_R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_20231219_STAGE2A", "symbol": "011200", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 18, "execution_risk_score": 8, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow if control-sale event is over-promoted", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": 12, "legal_or_contract_risk_score": 17, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "control_premium_or_event_premium_score": 18, "thesis_break_score": 14}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable + C32 4C-watch", "changed_components": ["target_vs_bidder_role_split", "bidder_financing_burden_score", "control_premium_or_event_premium_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "HMM privatization preferred-bidder selection created a target-side control-sale event premium. The price path validates the event premium, but later negotiation failure makes the same case a 4C timing audit rather than a durable operating rerating.", "MFE_90D_pct": 26.42, "MAE_90D_pct": -22.68, "score_return_alignment_label": "aligned_after_4C_watch", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION", "trigger_id": "TR_R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_20231219_STAGE2A", "symbol": "028670", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": 12, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow if event beta is misread as positive C32", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 5, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 14, "accounting_trust_risk_score": 0, "bidder_financing_burden_score": 18}, "weighted_score_after": 62, "stage_label_after": "Watch/No-promote bidder financing guard", "changed_components": ["target_vs_bidder_role_split", "bidder_financing_burden_score", "control_premium_or_event_premium_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "The HMM sale headline was not a target-side premium for Pan Ocean. It was bidder-side financing and balance-sheet burden. Later shipping-cycle recovery should not be attributed to C32 control premium.", "MFE_90D_pct": 23.57, "MAE_90D_pct": -14.53, "score_return_alignment_label": "false_positive_avoided_after_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF", "trigger_id": "TR_R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_20231219_STAGE2A", "symbol": "136480", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 16, "execution_risk_score": 10, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 6, "accounting_trust_risk_score": 0}, "weighted_score_before": 81, "stage_label_before": "Stage3-Yellow if RS/event beta dominates", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 8, "execution_risk_score": 22, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 12, "accounting_trust_risk_score": 0, "positioning_overheat_score": 20, "bidder_financing_burden_score": 18}, "weighted_score_after": 65, "stage_label_after": "Stage2-watch + C32 4B event-cap overlay", "changed_components": ["target_vs_bidder_role_split", "bidder_financing_burden_score", "control_premium_or_event_premium_score", "legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "Harim received a parent-company event premium from being named the HMM preferred bidder. The stock-web path shows a violent event squeeze followed by a deep retracement, so the correct use is 4B overlay / event-cap, not Stage3 promotion.", "MFE_90D_pct": 66.89, "MAE_90D_pct": -22.65, "score_return_alignment_label": "4B_overlay_alignment", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P0", "profile_scope": "current_default", "profile_hypothesis": "current e2r_2_1 calibrated profile, no C32 target/bidder role split", "changed_axes": "none", "changed_thresholds": "none", "eligible_trigger_count": 3, "selected_entry_trigger_per_case": "representative Stage2-Actionable rows", "avg_MFE_90D_pct": 38.96, "avg_MAE_90D_pct": -19.95, "avg_MFE_180D_pct": 38.96, "avg_MAE_180D_pct": -19.95, "false_positive_rate": 0.67, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.73, "avg_four_b_full_window_peak_proximity": 0.63, "score_return_alignment_verdict": "partially aligned but bidder-side false positives remain"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P0b", "profile_scope": "rollback_reference", "profile_hypothesis": "e2r_2_0 baseline reference with weaker Stage2 actionability", "changed_axes": "rollback only", "changed_thresholds": "rollback only", "eligible_trigger_count": 3, "selected_entry_trigger_per_case": "same representatives", "avg_MFE_90D_pct": 38.96, "avg_MAE_90D_pct": -19.95, "avg_MFE_180D_pct": 38.96, "avg_MAE_180D_pct": -19.95, "false_positive_rate": 0.33, "missed_structural_count": 1, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.73, "avg_four_b_full_window_peak_proximity": 0.63, "score_return_alignment_verdict": "safer but misses target-side event premium"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P1", "profile_scope": "sector_specific_candidate_profile", "profile_hypothesis": "shipping privatization/acquisition events split target premium from bidder financing burden", "changed_axes": "+target_vs_bidder_role_split; +bidder_financing_burden_penalty", "changed_thresholds": "no global threshold change", "eligible_trigger_count": 3, "selected_entry_trigger_per_case": "target-only Stage2A, bidder watch", "avg_MFE_90D_pct": 38.96, "avg_MAE_90D_pct": -19.95, "avg_MFE_180D_pct": 38.96, "avg_MAE_180D_pct": -19.95, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.73, "avg_four_b_full_window_peak_proximity": 0.63, "score_return_alignment_verdict": "best alignment for this loop"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P2", "profile_scope": "canonical_archetype_candidate_profile", "profile_hypothesis": "C32 requires issuer-role classification: target, bidder, parent, financing vehicle, or rumor-only", "changed_axes": "new_axis_proposed=C32_issuer_role_split", "changed_thresholds": "Stage3 cap for bidder/parent unless financing source and deal accretion are visible", "eligible_trigger_count": 3, "selected_entry_trigger_per_case": "issuer-role filtered representative rows", "avg_MFE_90D_pct": 38.96, "avg_MAE_90D_pct": -19.95, "avg_MFE_180D_pct": 38.96, "avg_MAE_180D_pct": -19.95, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.73, "avg_four_b_full_window_peak_proximity": 0.63, "score_return_alignment_verdict": "canonical rule candidate"}
{"row_type": "aggregate_profile_comparison", "profile_id": "P3", "profile_scope": "counterexample_guard_profile", "profile_hypothesis": "bidder-side cash/financing burden and parent-company squeeze are 4B overlays, not positive stage promotion", "changed_axes": "+financing_burden_guard +event_blowoff_guard", "changed_thresholds": "bidder-side positive stage capped below Yellow absent accretion evidence", "eligible_trigger_count": 3, "selected_entry_trigger_per_case": "HMM target + bidder guard", "avg_MFE_90D_pct": 38.96, "avg_MAE_90D_pct": -19.95, "avg_MFE_180D_pct": 38.96, "avg_MAE_180D_pct": -19.95, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.73, "avg_four_b_full_window_peak_proximity": 0.63, "score_return_alignment_verdict": "guard passes counterexamples"}
{"row_type": "residual_contribution", "round": "R12", "loop": "75", "scheduled_round": "R12", "scheduled_loop": "75", "round_schedule_status": "valid", "round_sector_consistency": "pass", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "new_trigger_family_count": 1, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "new_symbols=3; new_trigger_family=HMM_PRIVATIZATION_TARGET_VS_BIDDER_FINANCING_SPLIT; positives=1; counterexamples=2; residual_errors=3; wrong_round_penalty=0; duplicate_key_conflict=0", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["bidder_side_financing_false_positive", "parent_side_event_blowoff_4B_late", "target_side_control_sale_4C_late", "shipping_cycle_recovery_wrong_axis_attribution"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R12L75_C32_020560_003490_ASIANA_KOREANAIR_CA_BLOCKED", "symbol": "020560|003490", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "reason": "Asiana/Korean Air 2020 acquisition event was considered but blocked for weight calibration because stock-web symbol profiles show corporate-action candidate dates inside the 180D forward window: 020560 has 2021-01-15; 003490 has 2021-03-24.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C32_issuer_role_split,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Classify issuer as target/bidder/parent/financing vehicle before applying control-premium promotion.","Reduced bidder-side false positives while preserving HMM target premium",TR_R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_20231219_STAGE2A|TR_R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_20231219_STAGE2A|TR_R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_20231219_STAGE2A,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_bidder_financing_burden_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Bidder/parent stocks with funding burden cannot receive positive C32 promotion without visible accretion/financing clarity.","Pan Ocean/Harim entries become watch/4B overlays rather than false Stage3",TR_R12L75_C32_028670_PANOCEAN_BIDDER_FINANCING_CONFUSION_20231219_STAGE2A|TR_R12L75_C32_136480_HARIM_PARENT_EVENT_BLOWOFF_20231219_STAGE2A,2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C32_target_sale_4C_watch,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"Target-side event premium remains valid until negotiation/closing failure appears; then route to 4C-watch quickly.","HMM target premium not erased, but stale positive is blocked after thesis break",TR_R12L75_C32_011200_HMM_PRIVATIZATION_TARGET_4C_20231219_STAGE2A|TR_R12L75_C32_011200_20231220_4B_EVENT_CAP,1,1,0,low,canonical_shadow_only,"not production; post-calibrated residual"
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
completed_round = R12
completed_loop = 75
next_round = R13
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest/schema were read from `atlas/manifest.json` and `atlas/schema.json` in Songdaiki/stock-web.
- HMM rows used: `011/011200/2023.csv` around 2023-12-19/20 and `011/011200/2024.csv` through the 180D window.
- Pan Ocean rows used: `028/028670/2023.csv` around 2023-12-19 and `028/028670/2024.csv` through the 180D window.
- Harim rows used: `136/136480/2023.csv` around 2023-12-19/21 and `136/136480/2024.csv` through the 180D window.
- This file is standalone historical calibration research, not a stock recommendation and not a live scan.

