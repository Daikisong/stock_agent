# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

This loop continues loop 89 after R3. It adds 3 C16 strategic-resource cases: one lithium/resource supply-chain positive, one resource-trading false Stage2, and one rare-earth policy-theme 4B event-cap counterexample.

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
scheduled_round = R4
scheduled_loop = 89
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 89
```

R4 permits L4 materials/spread/resource research. Previous R4 loop-88 used C17, so this loop moves to C16 and tests whether strategic-resource narratives are supported by supply-chain, offtake, capacity, contract, or margin conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY = 36 rows / 23 symbols / good-bad Stage2 14-9 / 4B-4C 2-0
top covered symbols include 047400(6), 005490(3), 012320(3), 001570(2), 081150(2), 101670(2)
previous R4 loop-88 C17 symbols avoided: 120110, 069260, 161000
```

Selected rows avoid those repeated combinations:

```text
009520 / Stage2-Actionable / 2023-03-03
011810 / Stage2-Actionable / 2024-01-09
037370 / Stage4B / 2024-04-12
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
| 009520 | atlas/symbol_profiles/009/009520.json | selected 2023 window clean; CA candidates are 2012 or earlier |
| 011810 | atlas/symbol_profiles/011/011810.json | selected 2024-01-09 post-2024-01-05 CA window |
| 037370 | atlas/symbol_profiles/037/037370.json | selected 2024 window clean; CA candidates are 2008 or earlier |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L89_C16_POSCOMTECH_2023_LITHIUM_RESOURCE_SUPPLY_POLICY_POSITIVE | 009520 | 2023-03-03 | yes | 180 | yes | yes | true |
| R4L89_C16_STX_2024_RESOURCE_TRADING_FALSE_STAGE2 | 011810 | 2024-01-09 | yes | 180 | yes | post-CA | true |
| R4L89_C16_EG_2024_RARE_EARTH_POLICY_THEME_EVENT_CAP_4B | 037370 | 2024-04-12 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | LITHIUM_RESOURCE_SUPPLY_CHAIN_BRIDGE | Positive Stage2 requires supply-chain, capacity, contract/offtake, or margin bridge. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | RESOURCE_TRADING_FALSE_STAGE2 | Resource-trading label without offtake/margin bridge can be weak-MFE, high-MAE false Stage2. |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | RARE_EARTH_POLICY_THEME_CAP | Rare-earth / strategic-resource theme premium should route to 4B unless conversion is verified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L89_C16_POSCOMTECH_2023_LITHIUM_RESOURCE_SUPPLY_POLICY_POSITIVE | 009520 | 포스코엠텍 | positive | Lithium/resource supply-chain bridge produced very high MFE with almost no entry MAE. |
| R4L89_C16_STX_2024_RESOURCE_TRADING_FALSE_STAGE2 | 011810 | STX | counterexample | Resource-trading theme had tiny forward MFE and severe MAE. |
| R4L89_C16_EG_2024_RARE_EARTH_POLICY_THEME_EVENT_CAP_4B | 037370 | EG | counterexample / 4B | Rare-earth policy theme premium capped and then drifted lower. |

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
| POSCO M-Tech lithium/resource bridge | historical public/report proxy | true | true | shadow-only positive |
| STX resource-trading false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| EG rare-earth theme cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 009520 | atlas/ohlcv_tradable_by_symbol_year/009/009520/2023.csv | atlas/symbol_profiles/009/009520.json |
| 011810 | atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv | atlas/symbol_profiles/011/011810.json |
| 037370 | atlas/ohlcv_tradable_by_symbol_year/037/037370/2024.csv | atlas/symbol_profiles/037/037370.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L89_C16_POSCOMTECH_2023_STAGE2_ACTIONABLE_LITHIUM_RESOURCE_SUPPLY_BRIDGE | 009520 | Stage2-Actionable | 2023-03-03 | 8890 | positive | lithium/resource supply bridge worked |
| R4L89_C16_STX_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING | 011810 | Stage2-Actionable | 2024-01-09 | 11600 | counterexample | resource-trading false Stage2 |
| R4L89_C16_EG_2024_STAGE4B_RARE_EARTH_POLICY_THEME_CAP | 037370 | Stage4B | 2024-04-12 | 9420 | counterexample/4B | rare-earth policy theme cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L89_C16_POSCOMTECH_2023_STAGE2_ACTIONABLE_LITHIUM_RESOURCE_SUPPLY_BRIDGE | 8890 | 231.27 | -0.90 | 345.44 | -0.90 | 345.44 | -0.90 | 2023-04-18 | 39600 | -50.98 |
| R4L89_C16_STX_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING | 11600 | 5.95 | -20.09 | 5.95 | -32.41 | 5.95 | -56.90 | 2024-01-09 | 12290 | -59.32 |
| R4L89_C16_EG_2024_STAGE4B_RARE_EARTH_POLICY_THEME_CAP | 9420 | 8.49 | -13.69 | 8.49 | -24.52 | 8.49 | -24.52 | 2024-04-12 | 10220 | -30.43 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C16 Stage2 needs supply-chain, offtake, contract, capacity, or margin bridge |
| local_4b_watch_guard | strengthen: resource-trading / rare-earth policy theme premium should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 009520 | good_stage2 | Resource policy narrative converted into supply-chain/group capacity bridge. |
| 011810 | bad_stage2 | Resource-trading label had tiny upside and severe drawdown. |
| 037370 | good_4B | Rare-earth policy theme spike capped almost immediately. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 011810 resource trading false Stage2 | 1.00 | 1.00 | resource_trading_theme_spike_was_false_stage2_event_cap |
| 037370 rare-earth policy cap | 1.00 | 1.00 | good_full_window_4B_timing_rare_earth_policy_theme_cap |
| 009520 lithium/resource bridge | n/a | n/a | positive Stage2, but later resource valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 011810 / 037370
```

No hard 4C candidate is proposed. R4 loop 89 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 strategic-resource cases, Stage2 requires policy-to-supply-chain conversion: contract/offtake, capacity, customer, inventory, margin, or revision bridge. Resource label, rare-earth theme, or trading optionality alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rule = C16 should split lithium/resource supply-chain positives from resource-trading false Stage2 and rare-earth policy theme caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 119.96 | -19.28 | 0.67 | mixed; C16 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 119.96 | -19.28 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L4 resource bridge required | 2 | 175.70 | -16.66 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C16 bridge vs event-cap split | 2 | 175.70 | -16.66 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing resource themes as positive | 1 | 345.44 | -0.90 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 009520 lithium/resource bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 345.44 | -0.90 | lithium_resource_supply_chain_positive |
| 011810 resource trading false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 5.95 | -32.41 | resource_trading_theme_false_stage2 |
| 037370 rare-earth cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 8.49 | -24.52 | rare_earth_policy_theme_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C16 lithium/resource supply-chain positive, resource-trading false Stage2, and rare-earth policy-theme event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: lithium_resource_supply_chain_positive, resource_trading_theme_false_stage2, rare_earth_policy_theme_event_cap_4B
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
- C16 strategic-resource policy supply bridge vs resource-theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,C16_requires_policy_to_supply_chain_contract_or_margin_bridge,0,"C16 Stage2 should require policy-to-supply-chain, offtake, contract, capacity, or margin bridge, not strategic-resource label alone","POSCO M-Tech positive worked; STX and EG theme/event rows failed positive-stage promotion","R4L89_C16_POSCOMTECH_2023_STAGE2_ACTIONABLE_LITHIUM_RESOURCE_SUPPLY_BRIDGE|R4L89_C16_STX_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING|R4L89_C16_EG_2024_STAGE4B_RARE_EARTH_POLICY_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,configured,cap_resource_policy_theme_premiums_as_4B_watch,0,"Resource-trading and rare-earth policy-theme premiums can peak before verified supply-chain or offtake bridge appears","STX and EG showed weak MFE90 and material/high MAE after theme spikes","R4L89_C16_STX_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING|R4L89_C16_EG_2024_STAGE4B_RARE_EARTH_POLICY_THEME_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L89_C16_POSCOMTECH_2023_LITHIUM_RESOURCE_SUPPLY_POLICY_POSITIVE", "symbol": "009520", "company_name": "포스코엠텍", "round": "R4", "loop": "89", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L89_C16_POSCOMTECH_2023_STAGE2_ACTIONABLE_LITHIUM_RESOURCE_SUPPLY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Lithium/resource supply-chain policy rerating produced very high 30D/90D MFE with almost no entry MAE; C16 works only when policy/resource narrative maps into a credible supply-chain or group capacity bridge.", "current_profile_verdict": "current_profile_kept_but_C16_positive_requires_supply_chain_capacity_or_contract_bridge_not_resource_label_only", "price_source": "Songdaiki/stock-web", "notes": "Modern window is clean relative to old CA candidates; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R4L89_C16_STX_2024_RESOURCE_TRADING_FALSE_STAGE2", "symbol": "011810", "company_name": "STX", "round": "R4", "loop": "89", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R4L89_C16_STX_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "2024-01-05 corporate-action candidate was blocked; selected 2024-01-09 post-CA window only.", "independent_evidence_weight": 0.5, "score_price_alignment": "Resource-trading / strategic material theme had tiny forward MFE and severe 90D/180D MAE; resource label alone should not earn Stage2 without contract, offtake, margin, or balance bridge.", "current_profile_verdict": "current_profile_false_positive_if_resource_trading_theme_counts_without_contract_offtake_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Reduced evidence weight because selected row is post-CA and source-proxy only."}
{"row_type": "case", "case_id": "R4L89_C16_EG_2024_RARE_EARTH_POLICY_THEME_EVENT_CAP_4B", "symbol": "037370", "company_name": "EG", "round": "R4", "loop": "89", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R4L89_C16_EG_2024_STAGE4B_RARE_EARTH_POLICY_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Rare-earth / strategic-resource policy theme spike capped quickly and drifted lower; theme premium should route to 4B unless confirmed supply, contract, or margin bridge appears.", "current_profile_verdict": "current_profile_4B_too_late_if_rare_earth_policy_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Old CA candidates only; selected 2024 window clean. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L89_C16_POSCOMTECH_2023_STAGE2_ACTIONABLE_LITHIUM_RESOURCE_SUPPLY_BRIDGE", "case_id": "R4L89_C16_POSCOMTECH_2023_LITHIUM_RESOURCE_SUPPLY_POLICY_POSITIVE", "symbol": "009520", "company_name": "포스코엠텍", "round": "R4", "loop": "89", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP", "sector": "strategic_resource_lithium_supply_chain", "primary_archetype": "lithium_resource_policy_supply_chain_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-03", "entry_date": "2023-03-03", "entry_price": 8890.0, "evidence_available_at_that_date": "lithium / strategic-resource policy supply-chain and group capacity bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["strategic_resource_policy", "lithium_supply_chain_bridge", "group_capacity_optionality", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "low_entry_MAE"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_resource_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009520/2023.csv", "profile_path": "atlas/symbol_profiles/009/009520.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 231.27, "MFE_90D_pct": 345.44, "MFE_180D_pct": 345.44, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.9, "MAE_90D_pct": -0.9, "MAE_180D_pct": -0.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-18", "peak_price": 39600.0, "drawdown_after_peak_pct": -50.98, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_resource_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "resource_policy_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_lithium_resource_supply_chain_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L89_C16_009520_2023-03-03_8890", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L89_C16_STX_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING", "case_id": "R4L89_C16_STX_2024_RESOURCE_TRADING_FALSE_STAGE2", "symbol": "011810", "company_name": "STX", "round": "R4", "loop": "89", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP", "sector": "resource_trading_strategic_supply", "primary_archetype": "resource_trading_theme_without_offtake_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-09", "entry_date": "2024-01-09", "entry_price": 11600.0, "evidence_available_at_that_date": "resource trading / strategic minerals theme and post-CA recovery proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["resource_trading_theme", "strategic_mineral_supply_expectation", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE90", "offtake_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv", "profile_path": "atlas/symbol_profiles/011/011810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.95, "MFE_90D_pct": 5.95, "MFE_180D_pct": 5.95, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.09, "MAE_90D_pct": -32.41, "MAE_180D_pct": -56.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-09", "peak_price": 12290.0, "drawdown_after_peak_pct": -59.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "resource_trading_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["resource_policy_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_resource_trading_theme_without_offtake_bridge", "current_profile_verdict": "current_profile_false_positive_if_resource_trading_theme_counts_without_contract_offtake_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-01-05_CA_window", "same_entry_group_id": "R4L89_C16_011810_2024-01-09_11600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "post-CA row only; 2024-01-05 corporate-action candidate blocked from entry selection", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L89_C16_EG_2024_STAGE4B_RARE_EARTH_POLICY_THEME_CAP", "case_id": "R4L89_C16_EG_2024_RARE_EARTH_POLICY_THEME_EVENT_CAP_4B", "symbol": "037370", "company_name": "EG", "round": "R4", "loop": "89", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP", "sector": "rare_earth_strategic_resource_policy", "primary_archetype": "rare_earth_policy_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-12", "entry_date": "2024-04-12", "entry_price": 9420.0, "evidence_available_at_that_date": "rare-earth / strategic-resource policy theme premium after April spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["rare_earth_policy_theme", "strategic_resource_supply_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/037/037370/2024.csv", "profile_path": "atlas/symbol_profiles/037/037370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.49, "MFE_90D_pct": 8.49, "MFE_180D_pct": 8.49, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.69, "MAE_90D_pct": -24.52, "MAE_180D_pct": -24.52, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 10220.0, "drawdown_after_peak_pct": -30.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_rare_earth_policy_theme_cap", "four_b_evidence_type": ["resource_policy_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_rare_earth_policy_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L89_C16_037370_2024-04-12_9420", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L89_C16_POSCOMTECH_2023_LITHIUM_RESOURCE_SUPPLY_POLICY_POSITIVE", "trigger_id": "R4L89_C16_POSCOMTECH_2023_STAGE2_ACTIONABLE_LITHIUM_RESOURCE_SUPPLY_BRIDGE", "symbol": "009520", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 55, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 75, "customer_quality_score": 30, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "lithium_resource_supply_chain_positive", "MFE_90D_pct": 345.44, "MAE_90D_pct": -0.9, "score_return_alignment_label": "lithium_resource_supply_chain_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L89_C16_STX_2024_RESOURCE_TRADING_FALSE_STAGE2", "trigger_id": "R4L89_C16_STX_2024_STAGE2_FALSE_POSITIVE_RESOURCE_TRADING", "symbol": "011810", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 45, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["policy_or_regulatory_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "resource_trading_theme_false_stage2", "MFE_90D_pct": 5.95, "MAE_90D_pct": -32.41, "score_return_alignment_label": "resource_trading_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_resource_trading_theme_counts_without_contract_offtake_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L89_C16_EG_2024_RARE_EARTH_POLICY_THEME_EVENT_CAP_4B", "trigger_id": "R4L89_C16_EG_2024_STAGE4B_RARE_EARTH_POLICY_THEME_CAP", "symbol": "037370", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 45, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["policy_or_regulatory_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "rare_earth_policy_theme_event_cap_4B_guard", "MFE_90D_pct": 8.49, "MAE_90D_pct": -24.52, "score_return_alignment_label": "rare_earth_policy_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_rare_earth_policy_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "89", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_BRIDGE_VS_RESOURCE_TRADING_AND_RARE_EARTH_THEME_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["lithium_resource_supply_chain_positive", "resource_trading_theme_false_stage2", "rare_earth_policy_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reason":"all selected rows have usable 180D stock-web windows; 011810 entry was shifted after the 2024-01-05 corporate-action candidate","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R4
completed_loop = 89
next_round = R5
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
