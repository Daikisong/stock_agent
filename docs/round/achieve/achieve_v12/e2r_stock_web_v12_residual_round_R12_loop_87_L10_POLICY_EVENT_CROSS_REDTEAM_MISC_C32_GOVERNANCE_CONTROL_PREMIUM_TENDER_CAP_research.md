# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test
output_file = e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

This loop adds 3 new independent C32 cases, 2 counterexamples, and 2 current-profile residual errors for R12 / L10 / C32.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 87
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
round_sector_consistency = pass
computed_next_round = R13
computed_next_loop = 87
```

R12 permits L10 policy/event/gov-governance reinforcement. This loop focuses on C32: control premium / tender / PE-control event caps. The central split is:

```text
1. Active control-premium escalation can be a real Stage2 path.
2. Once the premium becomes a capped tender/control-sale event, it should route to 4B overlay.
3. A control-premium spike without durable operating rerating should not become structural Green.
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

The No-Repeat snapshot marks C32 top-covered symbols as `010130`, `036560`, `000150`, `041510`, `241560`, and `000990`. This loop avoids those repeated combinations and adds:

```text
180640 / Stage2-Actionable / 2020-02-12
003920 / Stage4B / 2021-07-01
009240 / Stage4B / 2021-07-14
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | corporate-action status |
|---|---|---|
| 180640 | atlas/symbol_profiles/180/180640.json | CA candidate is 2014-11-20; selected 2020 window clean |
| 003920 | atlas/symbol_profiles/003/003920.json | CA candidate is 2024-11-20; selected 2021 window clean |
| 009240 | atlas/symbol_profiles/009/009240.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R12L87_C32_HANJINKAL_2020_CONTROL_PREMIUM_ESCALATION | 180640 | 2020-02-12 | yes | 180 | yes | yes | true |
| R12L87_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B | 003920 | 2021-07-01 | yes | 180 | yes | yes | true |
| R12L87_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B | 009240 | 2021-07-14 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_PREMIUM_ESCALATION | Active governance/control contest can create real Stage2 asymmetry while the premium is still expanding. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | CONTROL_SALE_EVENT_CAP | Once the event premium is capped, full positive-stage promotion is risky; route to 4B overlay. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | PE_CONTROL_PREMIUM_FADE | PE/tender premium without operating rerating often has little forward MFE and heavy MAE. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R12L87_C32_HANJINKAL_2020_CONTROL_PREMIUM_ESCALATION | 180640 | 한진칼 | positive | Active control contest produced high 30D/90D MFE. |
| R12L87_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B | 003920 | 남양유업 | counterexample / 4B | Control-sale premium later had severe post-peak drawdown. |
| R12L87_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B | 009240 | 한샘 | counterexample / 4B | PE-control premium spike had weak forward upside and large MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| HanjinKAL control contest | historical public/news proxy | true | true | shadow-only positive |
| Namyang control sale | historical public/news proxy | true | true | 4B overlay counterexample |
| Hanssem PE control premium | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 180640 | atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv | atlas/symbol_profiles/180/180640.json |
| 003920 | atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv | atlas/symbol_profiles/003/003920.json |
| 009240 | atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv; 2022.csv | atlas/symbol_profiles/009/009240.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R12L87_C32_HANJINKAL_2020_STAGE2_ACTIONABLE_CONTROL_PREMIUM | 180640 | Stage2-Actionable | 2020-02-12 | 43500 | positive | control premium escalation worked |
| R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP | 003920 | Stage4B | 2021-07-01 | 760000 | counterexample/4B | control sale event cap |
| R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE | 009240 | Stage4B | 2021-07-14 | 146500 | counterexample/4B | PE control premium fade |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R12L87_C32_HANJINKAL_2020_STAGE2_ACTIONABLE_CONTROL_PREMIUM | 43500 | 120.69 | -10.57 | 155.17 | -10.57 | 155.17 | -10.57 | 2020-04-20 | 111000 | -34.77 |
| R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP | 760000 | 6.97 | -27.89 | 6.97 | -49.74 | 6.97 | -49.74 | 2021-07-01 | 813000 | -53.01 |
| R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE | 146500 | 1.71 | -27.99 | 1.71 | -27.99 | 1.71 | -52.97 | 2021-07-14 | 149000 | -53.76 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C32 Stage2 requires active escalation/tender spread, not event premium already capped |
| local_4b_watch_guard | strengthen: control-sale and PE premium caps should route to 4B |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is event-stage quality:

| symbol | stage quality | explanation |
|---|---|---|
| 180640 | good_stage2 | Control premium was still expanding; high MFE followed. |
| 003920 | good_4B | Event premium became capped; forward MAE dominated. |
| 009240 | good_4B | PE premium spike had minimal further upside and heavy drawdown. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 003920 control sale event cap | 1.00 | 1.00 | good_full_window_4B_timing_control_sale_event_cap |
| 009240 PE control premium fade | 1.00 | 1.00 | good_full_window_4B_timing_PE_control_premium_event_cap |
| 180640 control contest | n/a | n/a | positive Stage2, but later event-premium 4B watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 003920 / 009240
```

No hard 4C candidate is proposed. The residual contribution is 4B timing and Stage2 bridge quality, not hard thesis-break routing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 governance/event cases, Stage2 requires active control-premium expansion or tender-spread asymmetry. Once a tender/control-sale/PE premium is capped, the event should route to 4B overlay unless an independent operating rerating bridge exists.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rule = C32 should split active control-premium escalation positives from capped tender/control-sale/PE event premiums. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 54.62 | -29.43 | 0.67 | mixed, event cap split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 54.62 | -29.43 | 0.67 | weaker 4B cap |
| P1 sector_specific_candidate_profile | L10 active escalation vs cap split | 2 | 81.07 | -30.16 | 0.50 | better explanatory separation |
| P2 canonical_archetype_candidate_profile | C32 active premium / tender cap compression | 2 | 81.07 | -30.16 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject capped event premiums as positive | 1 | 155.17 | -10.57 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 180640 control contest | 66 | Stage2-Watch | 72 | Stage2-Actionable | 155.17 | -10.57 | control_premium_escalation_positive |
| 003920 control sale | 71 | Stage3-Yellow-like | 56 | Stage4B-watch | 6.97 | -49.74 | control_sale_event_cap_4B_guard |
| 009240 PE premium | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.71 | -27.99 | PE_control_premium_fade_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 1, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C32 control-premium escalation positive plus control-sale/PE event-cap 4B guardrails."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: control_premium_positive_exception, control_sale_event_cap_4B, PE_control_premium_fade_false_stage3
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C32 active control-premium escalation vs capped tender/control-sale/PE event premium split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,control_premium_escalation_requires_active_contest_or_tender_spread,0,"C32 Stage2 can work while control premium is still escalating, but not after tender/event cap is visible","HanjinKAL worked; Namyang/Hanssem are cap/fade cases","R12L87_C32_HANJINKAL_2020_STAGE2_ACTIONABLE_CONTROL_PREMIUM|R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP|R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,cap_control_sale_PE_premium_as_4B_watch,0,"Control-sale/PE premium can form full-window peak with poor forward MFE and heavy MAE","Namyang and Hanssem both showed event-cap drawdown after peak","R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP|R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE",2,2,2,low,guardrail_shadow_only,"event premium belongs in 4B overlay calibration"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R12L87_C32_HANJINKAL_2020_CONTROL_PREMIUM_ESCALATION", "symbol": "180640", "company_name": "한진칼", "round": "R12", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE", "case_type": "structural_event_success", "positive_or_counterexample": "positive", "best_trigger": "R12L87_C32_HANJINKAL_2020_STAGE2_ACTIONABLE_CONTROL_PREMIUM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Control-premium escalation produced very high 30D/90D/180D MFE with manageable entry MAE; C32 can be a real event-rerating path when the control contest is still escalating.", "current_profile_verdict": "current_profile_kept_but_requires_4B_overlay_after_event_premium_run", "price_source": "Songdaiki/stock-web", "notes": "Historical control-contest proxy; exact as-of evidence URL verification remains pending, so shadow-only."}
{"row_type": "case", "case_id": "R12L87_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B", "symbol": "003920", "company_name": "남양유업", "round": "R12", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Control-sale premium eventually became an event cap with severe post-peak drawdown; tender/control premium is not structural Green after the cap is visible.", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_cap_not_detected", "price_source": "Songdaiki/stock-web", "notes": "C32 event-cap path, source-proxy only."}
{"row_type": "case", "case_id": "R12L87_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B", "symbol": "009240", "company_name": "한샘", "round": "R12", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "PE/control premium spike had little forward upside and heavy 30D/180D MAE; after event premium appears, full positive-stage promotion should be blocked.", "current_profile_verdict": "current_profile_false_positive_if_control_premium_spike_counts_as_stage3_without_tender_cap_guard", "price_source": "Songdaiki/stock-web", "notes": "C32 event-premium fade, source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R12L87_C32_HANJINKAL_2020_STAGE2_ACTIONABLE_CONTROL_PREMIUM", "case_id": "R12L87_C32_HANJINKAL_2020_CONTROL_PREMIUM_ESCALATION", "symbol": "180640", "company_name": "한진칼", "round": "R12", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE", "sector": "governance_control_premium", "primary_archetype": "control_contest_escalation", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-02-12", "entry_date": "2020-02-12", "entry_price": 43500.0, "evidence_available_at_that_date": "control contest / governance premium escalation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["control_premium_escalation", "shareholder_contest", "event_premium_not_yet_capped", "relative_strength"], "stage3_evidence_fields": ["high_30D_MFE", "sustained_control_premium_bid_dynamics"], "stage4b_evidence_fields": ["event_premium_watch_after_parabolic_run", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv", "profile_path": "atlas/symbol_profiles/180/180640.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 120.69, "MFE_90D_pct": 155.17, "MFE_180D_pct": 155.17, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.57, "MAE_90D_pct": -10.57, "MAE_180D_pct": -10.57, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-04-20", "peak_price": 111000.0, "drawdown_after_peak_pct": -34.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "stage2_positive_but_requires_later_event_premium_4B_watch", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_control_premium_escalation_success", "current_profile_verdict": "current_profile_kept_but_4B_overlay_needed_after_fast_event_run", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L87_C32_HANJINKAL_2020_2020-02-12_43500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP", "case_id": "R12L87_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B", "symbol": "003920", "company_name": "남양유업", "round": "R12", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE", "sector": "governance_control_sale", "primary_archetype": "control_sale_event_cap", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test", "trigger_type": "Stage4B", "trigger_date": "2021-07-01", "entry_date": "2021-07-01", "entry_price": 760000.0, "evidence_available_at_that_date": "control-sale premium stretched / post-deal uncertainty proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["control_sale_premium", "ownership_change_expectation"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "control_sale_execution_uncertainty", "post_peak_drawdown"], "stage4c_evidence_fields": ["contract_or_control_transfer_uncertainty_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003920/2021.csv", "profile_path": "atlas/symbol_profiles/003/003920.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.97, "MFE_90D_pct": 6.97, "MFE_180D_pct": 6.97, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.89, "MAE_90D_pct": -49.74, "MAE_180D_pct": -49.74, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-01", "peak_price": 813000.0, "drawdown_after_peak_pct": -53.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_control_sale_event_cap", "four_b_evidence_type": ["control_premium_or_event_premium", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_cap_not_detected", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L87_C32_NAMYANG_2021_2021-07-01_760000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE", "case_id": "R12L87_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B", "symbol": "009240", "company_name": "한샘", "round": "R12", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE", "sector": "governance_PE_control_premium", "primary_archetype": "PE_control_premium_event_cap", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | stage2_actionable_bonus_stress_test", "trigger_type": "Stage4B", "trigger_date": "2021-07-14", "entry_date": "2021-07-14", "entry_price": 146500.0, "evidence_available_at_that_date": "PE/control premium spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["control_premium_bid", "ownership_change_expectation"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["post_deal_fundamental_fade_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009240/2021.csv|atlas/ohlcv_tradable_by_symbol_year/009/009240/2022.csv", "profile_path": "atlas/symbol_profiles/009/009240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.71, "MFE_90D_pct": 1.71, "MFE_180D_pct": 1.71, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.99, "MAE_90D_pct": -27.99, "MAE_180D_pct": -52.97, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-14", "peak_price": 149000.0, "drawdown_after_peak_pct": -53.76, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_PE_control_premium_event_cap", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_false_positive_if_control_premium_spike_counts_as_structural_green", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L87_C32_HANSSEM_2021_2021-07-14_146500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L87_C32_HANJINKAL_2020_CONTROL_PREMIUM_ESCALATION", "trigger_id": "R12L87_C32_HANJINKAL_2020_STAGE2_ACTIONABLE_CONTROL_PREMIUM", "symbol": "180640", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 80, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 70, "execution_risk_score": 45, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 75, "execution_risk_score": 40, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "control_premium_escalation_positive", "MFE_90D_pct": 155.17, "MAE_90D_pct": -10.57, "score_return_alignment_label": "control_premium_escalation_positive", "current_profile_verdict": "current_profile_kept_but_4B_overlay_needed_after_fast_event_run"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L87_C32_NAMYANG_2021_CONTROL_SALE_EVENT_CAP_4B", "trigger_id": "R12L87_C32_NAMYANG_2021_STAGE4B_CONTROL_SALE_EVENT_CAP", "symbol": "003920", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 75, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 80, "execution_risk_score": 55, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_before": 71, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 35, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 45, "execution_risk_score": 75, "legal_or_contract_risk_score": 75, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 25}, "weighted_score_after": 56, "stage_label_after": "Stage4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "control_sale_event_cap_4B_guard", "MFE_90D_pct": 6.97, "MAE_90D_pct": -49.74, "score_return_alignment_label": "control_sale_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_control_premium_cap_not_detected"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L87_C32_HANSSEM_2021_PE_CONTROL_PREMIUM_FADE_4B", "trigger_id": "R12L87_C32_HANSSEM_2021_STAGE4B_PE_CONTROL_PREMIUM_FADE", "symbol": "009240", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 80, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 75, "execution_risk_score": 50, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 75, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "PE_control_premium_fade_4B_guard", "MFE_90D_pct": 1.71, "MAE_90D_pct": -27.99, "score_return_alignment_label": "PE_control_premium_fade_4B_guard", "current_profile_verdict": "current_profile_false_positive_if_control_premium_spike_counts_as_structural_green"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_PREMIUM_ESCALATION_VS_TENDER_EVENT_CAP_AND_POST_DEAL_FADE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["control_premium_positive_exception", "control_sale_event_cap_4B", "PE_control_premium_fade_false_stage3"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 87
next_round = R13
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
