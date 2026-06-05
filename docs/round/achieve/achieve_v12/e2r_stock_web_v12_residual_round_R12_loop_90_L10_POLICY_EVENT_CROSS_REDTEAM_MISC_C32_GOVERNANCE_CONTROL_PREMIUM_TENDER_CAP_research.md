# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R12
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R12_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

This loop corrects the current run to the scheduled R12 / loop 90 state. It adds 3 C32 governance/control-premium cases: one governance capital-allocation bridge positive, one family-dispute false Stage2, and one proxy/control-premium 4B event-cap counterexample.

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
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 90
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
round_sector_consistency = pass
computed_next_round = R13
computed_next_loop = 90
```

R12 permits the L10 policy/event/misc route. Previous R12 loop 89 used C31, so this loop uses C32 and avoids the previous R12 C31 and earlier R12 C32 rows.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP = 41 rows / 22 symbols / good-bad Stage2 16-12 / 4B-4C 3-0
top covered symbols include 010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2)
previous R12 loop-88 C32 symbols avoided: 000400, 040300, 006040
previous R12 loop-89 C31 symbols avoided: 071320, 100220, 339950
previous R11 loop-90 C05 symbols avoided: 047040, 028050, 052690
```

Selected rows avoid those repeated combinations and top repeated C32 symbols:

```text
003240 / Stage2-Actionable / 2024-01-24
008930 / Stage2-Actionable / 2024-01-16
064850 / Stage4B / 2024-09-24
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

| symbol | profile path | CA window status |
|---|---|---|
| 003240 | atlas/symbol_profiles/003/003240.json | no corporate-action candidate |
| 008930 | atlas/symbol_profiles/008/008930.json | selected 2024 window clean; CA candidates are 2012 or earlier |
| 064850 | atlas/symbol_profiles/064/064850.json | selected 2024 window clean; CA candidate is 2018-11-13 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R12L90_C32_TAEKWANG_2024_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_POSITIVE | 003240 | 2024-01-24 | yes | 180 | yes | yes | true |
| R12L90_C32_HANMISCIENCE_2024_FAMILY_DISPUTE_FALSE_STAGE2 | 008930 | 2024-01-16 | yes | 180 | yes | yes | true |
| R12L90_C32_FNGUIDE_2024_PROXY_CONTROL_PREMIUM_EVENT_CAP_4B | 064850 | 2024-09-24 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE | Positive Stage2 requires governance pressure converting into capital allocation, asset monetization, tender/control, or shareholder return. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | FAMILY_DISPUTE_FALSE_STAGE2 | Family dispute/control-premium headline without transaction bridge can become false Stage2. |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | PROXY_CONTROL_PREMIUM_EVENT_CAP_4B | Proxy/control-premium event spike should route to 4B when premium is capped or unverified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R12L90_C32_TAEKWANG_2024_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_POSITIVE | 003240 | 태광산업 | positive | Governance/capital-allocation bridge produced very high MFE with shallow early MAE. |
| R12L90_C32_HANMISCIENCE_2024_FAMILY_DISPUTE_FALSE_STAGE2 | 008930 | 한미사이언스 | counterexample | Family-dispute control premium peaked at entry and then drew down. |
| R12L90_C32_FNGUIDE_2024_PROXY_CONTROL_PREMIUM_EVENT_CAP_4B | 064850 | 에프앤가이드 | counterexample / 4B | Proxy/control-premium premium capped at the September spike and collapsed. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Taekwang governance/capital allocation | historical public/news proxy | true | true | shadow-only positive |
| Hanmi Science family dispute | historical public/news proxy | true | true | false-Stage2 guardrail |
| FnGuide proxy/control premium cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003240 | atlas/ohlcv_tradable_by_symbol_year/003/003240/2024.csv | atlas/symbol_profiles/003/003240.json |
| 008930 | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | atlas/symbol_profiles/008/008930.json |
| 064850 | atlas/ohlcv_tradable_by_symbol_year/064/064850/2024.csv | atlas/symbol_profiles/064/064850.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R12L90_C32_TAEKWANG_2024_STAGE2_ACTIONABLE_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE | 003240 | Stage2-Actionable | 2024-01-24 | 618000 | positive | governance/capital allocation bridge worked |
| R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM | 008930 | Stage2-Actionable | 2024-01-16 | 56200 | counterexample | family dispute false Stage2 |
| R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP | 064850 | Stage4B | 2024-09-24 | 38450 | counterexample/4B | proxy control-premium event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R12L90_C32_TAEKWANG_2024_STAGE2_ACTIONABLE_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE | 618000 | 60.84 | -5.50 | 60.84 | -5.50 | 60.84 | -17.48 | 2024-01-30 | 994000 | -48.69 |
| R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM | 56200 | 0.00 | -31.14 | 0.00 | -43.59 | 0.00 | -45.46 | 2024-01-16 | 56200 | -46.09 |
| R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP | 38450 | 0.00 | -72.54 | 0.00 | -77.09 | 0.00 | -77.09 | 2024-09-24 | 38450 | -77.09 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C32 Stage2 needs transaction/capital allocation/tender/control bridge |
| local_4b_watch_guard | strengthen: family dispute and proxy/control-premium events should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE control-premium rows cannot promote without durable transaction bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is governance/control-premium conversion quality:

| symbol | stage quality | explanation |
|---|---|---|
| 003240 | good_stage2 | Governance/capital allocation bridge produced high MFE with manageable early drawdown. |
| 008930 | bad_stage2 | Family dispute/control-premium spike had no forward MFE after entry. |
| 064850 | good_4B | Proxy/control-premium event premium capped at the spike and collapsed. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 008930 family dispute false Stage2 | 1.00 | 1.00 | family-dispute control premium spike was false Stage2 event cap |
| 064850 proxy control-premium cap | 1.00 | 1.00 | good full-window 4B timing |
| 003240 governance capital-allocation bridge | n/a | n/a | positive Stage2, but later governance valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 008930 / 064850
```

No hard 4C candidate is proposed. R12 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 governance/control-premium cases, Stage2 requires verified transaction, tender, capital allocation, asset monetization, governance reform, shareholder return, or durable control-premium bridge. Family dispute, proxy fight, governance headline, or control-premium event label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rule = C32 should split governance/capital-allocation positives from family-dispute false Stage2 and proxy/control-premium event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 20.28 | -42.06 | 0.67 | mixed; C32 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 20.28 | -42.06 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L10 transaction/capital allocation bridge required | 2 | 30.42 | -24.55 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C32 bridge vs event-cap split | 2 | 30.42 | -24.55 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing control-premium themes as positive | 1 | 60.84 | -5.50 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 003240 governance bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 60.84 | -5.50 | governance_capital_allocation_bridge_positive |
| 008930 family dispute false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 0.00 | -43.59 | family_dispute_control_premium_false_stage2 |
| 064850 proxy cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 0.00 | -77.09 | proxy_control_premium_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C32 governance capital-allocation positive, family-dispute false Stage2, and proxy/control-premium event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: governance_capital_allocation_bridge_positive, family_dispute_control_premium_false_stage2, proxy_control_premium_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
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
- C32 governance/control-premium bridge vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,C32_requires_transaction_capital_allocation_or_control_bridge,0,"C32 Stage2 should require completed/credible transaction, tender, control premium, asset sale, capital allocation, governance reform, or shareholder-return bridge, not dispute/proxy headline alone","Taekwang positive worked; Hanmi Science and FnGuide event rows failed positive-stage promotion","R12L90_C32_TAEKWANG_2024_STAGE2_ACTIONABLE_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE|R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM|R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,cap_family_dispute_proxy_and_control_premium_events_as_4B_watch,0,"Family dispute, proxy fight, and control-premium event spikes can peak before durable transaction or capital-allocation bridge appears","Hanmi Science and FnGuide showed event-cap behavior with severe MAE after spike entries","R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM|R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,configured,block_positive_stage_when_control_premium_event_has_high_MAE_without_transaction_bridge,0,"High MAE after governance/control-premium event entry should block Stage2/Stage3 promotion unless transaction or capital-allocation evidence survives","Hanmi Science MAE90=-43.59 and FnGuide MAE90=-77.09","R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM|R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R12L90_C32_TAEKWANG_2024_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_POSITIVE", "symbol": "003240", "company_name": "태광산업", "round": "R12", "loop": "90", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L90_C32_TAEKWANG_2024_STAGE2_ACTIONABLE_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Governance/capital-allocation and asset-value discount repair produced very high MFE with shallow initial MAE; C32 works when governance pressure maps into concrete capital allocation, asset monetization, tender/control, or shareholder-return bridge.", "current_profile_verdict": "current_profile_kept_but_C32_positive_requires_governance_to_capital_allocation_or_control_premium_bridge_not_headline_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R12L90_C32_HANMISCIENCE_2024_FAMILY_DISPUTE_FALSE_STAGE2", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "90", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP", "case_type": "failed_rerating_family_dispute", "positive_or_counterexample": "counterexample", "best_trigger": "R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Family dispute/control-premium spike had no forward MFE after the spike entry and then large MAE; C32 Stage2 should not be granted without a durable transaction, tender, asset sale, governance reform, or capital-return bridge.", "current_profile_verdict": "current_profile_false_positive_if_family_dispute_control_premium_counts_without_durable_transaction_or_capital_allocation_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; corporate-action candidates are 2012 or earlier. Source-proxy only."}
{"row_type": "case", "case_id": "R12L90_C32_FNGUIDE_2024_PROXY_CONTROL_PREMIUM_EVENT_CAP_4B", "symbol": "064850", "company_name": "에프앤가이드", "round": "R12", "loop": "90", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Proxy/control-premium event premium capped near the September spike and then collapsed; control-premium theme should route to 4B unless a completed transaction, tender, governance reform, or capital-return bridge remains visible.", "current_profile_verdict": "current_profile_4B_too_late_if_proxy_control_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; old 2018 CA candidate outside selected window. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R12L90_C32_TAEKWANG_2024_STAGE2_ACTIONABLE_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE", "case_id": "R12L90_C32_TAEKWANG_2024_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_POSITIVE", "symbol": "003240", "company_name": "태광산업", "round": "R12", "loop": "90", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP", "sector": "governance_asset_value_capital_allocation", "primary_archetype": "governance_asset_value_capital_return_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 618000.0, "evidence_available_at_that_date": "governance pressure / asset-value discount repair / capital-allocation bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["governance_pressure_proxy", "asset_value_discount_repair", "capital_allocation_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "controlled_entry_MAE"], "stage4b_evidence_fields": ["valuation_watch_after_governance_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003240/2024.csv", "profile_path": "atlas/symbol_profiles/003/003240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 60.84, "MFE_90D_pct": 60.84, "MFE_180D_pct": 60.84, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.5, "MAE_90D_pct": -5.5, "MAE_180D_pct": -17.48, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-30", "peak_price": 994000.0, "drawdown_after_peak_pct": -48.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_governance_rerating_valuation_watch_needed", "four_b_evidence_type": ["governance_premium", "positioning_overheat", "asset_value_discount_repair"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_governance_capital_allocation_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L90_C32_003240_2024-01-24_618000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM", "case_id": "R12L90_C32_HANMISCIENCE_2024_FAMILY_DISPUTE_FALSE_STAGE2", "symbol": "008930", "company_name": "한미사이언스", "round": "R12", "loop": "90", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP", "sector": "family_dispute_control_premium", "primary_archetype": "family_dispute_without_completed_transaction_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-16", "entry_date": "2024-01-16", "entry_price": 56200.0, "evidence_available_at_that_date": "family dispute / control-premium and governance transaction expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["family_dispute_control_premium", "transaction_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["zero_forward_MFE_after_spike", "transaction_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -31.14, "MAE_90D_pct": -43.59, "MAE_180D_pct": -45.46, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 56200.0, "drawdown_after_peak_pct": -46.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "family_dispute_control_premium_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["control_premium", "positioning_overheat", "transaction_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_family_dispute_without_transaction_bridge", "current_profile_verdict": "current_profile_false_positive_if_family_dispute_control_premium_counts_without_durable_transaction_or_capital_allocation_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L90_C32_008930_2024-01-16_56200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP", "case_id": "R12L90_C32_FNGUIDE_2024_PROXY_CONTROL_PREMIUM_EVENT_CAP_4B", "symbol": "064850", "company_name": "에프앤가이드", "round": "R12", "loop": "90", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP", "sector": "proxy_control_premium_event", "primary_archetype": "proxy_control_premium_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-09-24", "entry_date": "2024-09-24", "entry_price": 38450.0, "evidence_available_at_that_date": "proxy fight / control-premium event premium after September spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["proxy_control_premium", "event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "zero_forward_MFE", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064850/2024.csv", "profile_path": "atlas/symbol_profiles/064/064850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -72.54, "MAE_90D_pct": -77.09, "MAE_180D_pct": -77.09, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-24", "peak_price": 38450.0, "drawdown_after_peak_pct": -77.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_proxy_control_premium_event_cap", "four_b_evidence_type": ["control_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_proxy_control_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2018_CA", "same_entry_group_id": "R12L90_C32_064850_2024-09-24_38450", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L90_C32_TAEKWANG_2024_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_POSITIVE", "trigger_id": "R12L90_C32_TAEKWANG_2024_STAGE2_ACTIONABLE_GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE", "symbol": "003240", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 10, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 55, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 50, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "governance_capital_allocation_bridge_positive", "MFE_90D_pct": 60.84, "MAE_90D_pct": -5.5, "score_return_alignment_label": "governance_capital_allocation_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L90_C32_HANMISCIENCE_2024_FAMILY_DISPUTE_FALSE_STAGE2", "trigger_id": "R12L90_C32_HANMISCIENCE_2024_STAGE2_FALSE_POSITIVE_FAMILY_DISPUTE_CONTROL_PREMIUM", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 10, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "family_dispute_control_premium_false_stage2", "MFE_90D_pct": 0.0, "MAE_90D_pct": -43.59, "score_return_alignment_label": "family_dispute_control_premium_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_family_dispute_control_premium_counts_without_durable_transaction_or_capital_allocation_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L90_C32_FNGUIDE_2024_PROXY_CONTROL_PREMIUM_EVENT_CAP_4B", "trigger_id": "R12L90_C32_FNGUIDE_2024_STAGE4B_PROXY_CONTROL_PREMIUM_CAP", "symbol": "064850", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 10, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "proxy_control_premium_event_cap_4B_guard", "MFE_90D_pct": 0.0, "MAE_90D_pct": -77.09, "score_return_alignment_label": "proxy_control_premium_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_proxy_control_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R12", "loop": "90", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CAPITAL_ALLOCATION_BRIDGE_VS_FAMILY_DISPUTE_AND_PROXY_CONTROL_PREMIUM_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["governance_capital_allocation_bridge_positive", "family_dispute_control_premium_false_stage2", "proxy_control_premium_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 90
next_round = R13
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
