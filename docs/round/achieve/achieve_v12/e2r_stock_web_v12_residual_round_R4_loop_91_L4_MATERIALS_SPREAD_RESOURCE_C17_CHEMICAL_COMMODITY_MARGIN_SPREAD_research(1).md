# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_protection_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R4_loop_91_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

This file is the corrected final output for this execution. The actual scheduler state after R3 loop 91 is R4 / loop 91. This round fills C17 chemical commodity margin-spread behavior: a spread-recovery positive with later cycle watch, a false Stage2, and a hard 4C margin-break row.

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
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
local_4b_watch_guard = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 91
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 91
```

R4 permits L4 materials/spread/resource research. Previous R4 loops used C17/C16/C15, but this loop returns to C17 with a fresh symbol set and a different fine split.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 21 rows / 15 symbols / good-bad Stage2 8-3 / 4B-4C 4-0
top covered symbols include 004000(3), 006650(2), 011780(2), 014680(2), 298020(2), 001390(1)
previous R4 loop-88 C17 symbols avoided: 120110, 069260, 161000
previous R4 loop-89 C16 symbols avoided: 009520, 011810, 037370
previous R4 loop-90 C15 symbols avoided: 024840, 018470, 006110
previous R3 loop-91 C14 symbols avoided: 066970, 089980, 336370
```

Selected rows avoid hard duplicates and top repeated C17 symbols:

```text
010060 / Stage2-Actionable / 2024-01-17
007690 / Stage2-Actionable / 2024-02-20
298000 / Stage4C / 2024-01-24
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
| 010060 | atlas/symbol_profiles/010/010060.json | selected 2024 window clean after 2023 name/split event |
| 007690 | atlas/symbol_profiles/007/007690.json | selected 2024 window clean after old 2021 CA candidates |
| 298000 | atlas/symbol_profiles/298/298000.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R4L91_C17_OCI_2024_POLYSILICON_CHEMICAL_SPREAD_RECOVERY_POSITIVE | 010060 | 2024-01-17 | yes | 180 | yes | yes | true |
| R4L91_C17_KUKDO_2024_EPOXY_SPREAD_FALSE_STAGE2 | 007690 | 2024-02-20 | yes | 180 | yes | yes | true |
| R4L91_C17_HYOSUNGCHEM_2024_PP_CHEMICAL_MARGIN_BREAK_4C | 298000 | 2024-01-24 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | POLYSILICON_CHEMICAL_SPREAD_RECOVERY | Positive Stage2 requires ASP-cost spread, inventory/repricing, margin, and revision bridge. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | EPOXY_SPREAD_FALSE_STAGE2 | Spread recovery watch without margin bridge can become low-MFE false Stage2. |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | PP_CHEMICAL_MARGIN_BREAK_4C | Deep commodity margin break plus leverage risk should route to 4C/protection. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R4L91_C17_OCI_2024_POLYSILICON_CHEMICAL_SPREAD_RECOVERY_POSITIVE | 010060 | OCI홀딩스 | positive | Early spread recovery produced MFE, but later drawdown requires commodity-cycle watch. |
| R4L91_C17_KUKDO_2024_EPOXY_SPREAD_FALSE_STAGE2 | 007690 | 국도화학 | counterexample | Epoxy spread watch had tiny MFE and no durable margin/revision bridge. |
| R4L91_C17_HYOSUNGCHEM_2024_PP_CHEMICAL_MARGIN_BREAK_4C | 298000 | 효성화학 | hard 4C | PP/chemical margin break had weak MFE and deep MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 0
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| OCI polysilicon/chemical spread recovery | historical public/report proxy | true | true | shadow-only positive |
| Kukdo epoxy spread false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| Hyosung Chemical PP margin break | historical public/report proxy | true | true | hard-4C protection |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 010060 | atlas/ohlcv_tradable_by_symbol_year/010/010060/2024.csv | atlas/symbol_profiles/010/010060.json |
| 007690 | atlas/ohlcv_tradable_by_symbol_year/007/007690/2024.csv | atlas/symbol_profiles/007/007690.json |
| 298000 | atlas/ohlcv_tradable_by_symbol_year/298/298000/2024.csv | atlas/symbol_profiles/298/298000.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R4L91_C17_OCI_2024_STAGE2_ACTIONABLE_POLYSILICON_CHEMICAL_SPREAD_RECOVERY | 010060 | Stage2-Actionable | 2024-01-17 | 93400 | positive | spread recovery worked but needed later 4B cycle watch |
| R4L91_C17_KUKDO_2024_STAGE2_FALSE_POSITIVE_EPOXY_SPREAD_RECOVERY | 007690 | Stage2-Actionable | 2024-02-20 | 40400 | counterexample | epoxy spread false Stage2 |
| R4L91_C17_HYOSUNGCHEM_2024_STAGE4C_PP_CHEMICAL_MARGIN_BREAK | 298000 | Stage4C | 2024-01-24 | 76200 | hard 4C | chemical margin break |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R4L91_C17_OCI_2024_STAGE2_ACTIONABLE_POLYSILICON_CHEMICAL_SPREAD_RECOVERY | 93400 | 20.99 | -1.93 | 20.99 | -9.31 | 20.99 | -30.51 | 2024-02-07 | 113000 | -42.57 |
| R4L91_C17_KUKDO_2024_STAGE2_FALSE_POSITIVE_EPOXY_SPREAD_RECOVERY | 40400 | 3.22 | -7.18 | 3.22 | -12.38 | 3.22 | -18.81 | 2024-02-20 | 41700 | -21.34 |
| R4L91_C17_HYOSUNGCHEM_2024_STAGE4C_PP_CHEMICAL_MARGIN_BREAK | 76200 | 3.81 | -12.99 | 3.81 | -27.82 | 3.81 | -34.91 | 2024-01-25 | 79100 | -37.42 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C17 Stage2 needs ASP-cost spread / inventory / margin / revision bridge |
| hard_4c_thesis_break_routes_to_4c | strengthen: deep commodity margin break with leverage risk routes to 4C |
| high_MAE_guardrail | strengthen: high MAE requires margin/revision recheck |
| local_4b_watch_guard | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is chemical margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 010060 | good_stage2_with_watch | Spread recovery produced early MFE but later drawdown requires cycle watch. |
| 007690 | bad_stage2 | Epoxy spread watch lacked margin/revision evidence. |
| 298000 | hard_4C | Commodity margin break plus leverage risk produced deep MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 010060 spread recovery | n/a | n/a | positive Stage2 but later commodity-cycle 4B watch needed |
| 007690 epoxy false Stage2 | 1.00 | 1.00 | false Stage2 due missing margin/revision bridge |
| 298000 PP margin break | 0.96 | 0.96 | hard 4C commodity margin break |

## 16. 4C Protection Audit

```text
4C_case_count = 1
hard_4C_success_count = 1
false_4C_recheck_count = 0
```

C17 receives one explicit hard-4C row because the issue is not merely price weakness; the intended non-price bridge is a margin/revision/leverage failure.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L4 chemical commodity spread cases, Stage2 requires verified ASP-cost spread, inventory/repricing, utilization, margin, or revision bridge. Chemical, polysilicon, epoxy, PP, or commodity-recovery label alone remains watch/4B. Deep margin failure plus leverage risk routes to 4C.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rule = C17 should split real spread/margin recovery positives from false Stage2 spread watches and hard chemical margin-break 4C cases. 4C rows are protection calibration, not positive-stage promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 9.34 | -16.50 | 0.67 | mixed; C17 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 9.34 | -16.50 | 0.67 | weaker margin/revision guard |
| P1 sector_specific_candidate_profile | L4 spread/margin bridge required | 2 | 12.11 | -10.85 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C17 bridge vs 4C split | 2 | 12.11 | -10.85 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing chemical themes as positive | 1 | 20.99 | -9.31 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 010060 polysilicon spread recovery | 66 | Stage2-Watch | 73 | Stage2-Actionable/watch | 20.99 | -9.31 | polysilicon_chemical_spread_recovery_positive_with_later_cycle_watch |
| 007690 epoxy false Stage2 | 66 | Stage2-Actionable | 54 | Stage1/Watch | 3.22 | -12.38 | epoxy_spread_false_stage2 |
| 298000 PP margin break | 70 | Stage2/Yellow-like | 42 | Stage4C-protection | 3.81 | -27.82 | PP_chemical_margin_break_4C_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 0, "4C_case_count": 1, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C17 polysilicon/chemical spread recovery positive-with-watch, epoxy spread false Stage2, and PP chemical commodity margin-break 4C split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, hard_4c_thesis_break_routes_to_4c, high_MAE_guardrail, price_only_blowoff_blocks_positive_stage
residual_error_types_found: polysilicon_spread_recovery_positive_with_cycle_watch, epoxy_spread_false_stage2, PP_chemical_margin_break_4C
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, hard_4c_thesis_break_routes_to_4c, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: local_4b_watch_guard, price_only_blowoff_blocks_positive_stage
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
- C17 chemical commodity margin-spread bridge vs false Stage2 / 4C split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,C17_requires_ASP_cost_spread_inventory_margin_revision_bridge,0,"C17 Stage2 should require ASP-cost spread, inventory/repricing, utilization, margin, or revision bridge, not chemical commodity recovery label alone","OCI positive worked only with later cycle watch; Kukdo Chemical false Stage2 failed without margin/revision bridge","R4L91_C17_OCI_2024_STAGE2_ACTIONABLE_POLYSILICON_CHEMICAL_SPREAD_RECOVERY|R4L91_C17_KUKDO_2024_STAGE2_FALSE_POSITIVE_EPOXY_SPREAD_RECOVERY",2,2,1,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,hard_4c_thesis_break_routes_to_4c,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,C17_hard_4C_when_margin_leverage_revision_bridge_breaks,0,"Chemical commodity margin-break rows with leverage risk and deep MAE should route to 4C/protection rather than Stage2 recovery","Hyosung Chemical had weak MFE and deep MAE after PP/chemical margin break","R4L91_C17_HYOSUNGCHEM_2024_STAGE4C_PP_CHEMICAL_MARGIN_BREAK",1,1,1,medium,guardrail_shadow_only,"4C protection only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,configured,high_MAE_requires_margin_revision_recheck,0,"High MAE in C17 after commodity spread entry should force margin/revision recheck before any positive promotion","Hyosung Chemical MAE90=-27.82; OCI later MAE180=-30.51 despite early MFE","R4L91_C17_HYOSUNGCHEM_2024_STAGE4C_PP_CHEMICAL_MARGIN_BREAK|R4L91_C17_OCI_2024_STAGE2_ACTIONABLE_POLYSILICON_CHEMICAL_SPREAD_RECOVERY",2,2,1,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L91_C17_OCI_2024_POLYSILICON_CHEMICAL_SPREAD_RECOVERY_POSITIVE", "symbol": "010060", "company_name": "OCI홀딩스", "round": "R4", "loop": "91", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP", "case_type": "structural_success_with_later_cycle_watch", "positive_or_counterexample": "positive", "best_trigger": "R4L91_C17_OCI_2024_STAGE2_ACTIONABLE_POLYSILICON_CHEMICAL_SPREAD_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.75, "score_price_alignment": "Polysilicon/chemical spread recovery produced a clean early MFE path, but later commodity downcycle pressure made 180D drawdown meaningful. C17 Stage2 is valid only when spread/margin/revision bridge remains observable and later 4B watch is enforced.", "current_profile_verdict": "current_profile_kept_but_C17_positive_requires_spread_margin_revision_bridge_and_later_cycle_watch", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window is clean after 2023 name/split event; reduced weight because later commodity drawdown makes this a positive-with-cycle-watch row."}
{"row_type": "case", "case_id": "R4L91_C17_KUKDO_2024_EPOXY_SPREAD_FALSE_STAGE2", "symbol": "007690", "company_name": "국도화학", "round": "R4", "loop": "91", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP", "case_type": "failed_rerating_margin_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R4L91_C17_KUKDO_2024_STAGE2_FALSE_POSITIVE_EPOXY_SPREAD_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Epoxy/chemical spread recovery watch produced tiny forward MFE and persistent drawdown. C17 Stage2 should not be awarded without ASP-cost spread, inventory, utilization, and margin/revision evidence.", "current_profile_verdict": "current_profile_false_positive_if_epoxy_chemical_spread_watch_counts_without_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2021 CA candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R4L91_C17_HYOSUNGCHEM_2024_PP_CHEMICAL_MARGIN_BREAK_4C", "symbol": "298000", "company_name": "효성화학", "round": "R4", "loop": "91", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP", "case_type": "hard_4c_commodity_margin_break", "positive_or_counterexample": "counterexample", "best_trigger": "R4L91_C17_HYOSUNGCHEM_2024_STAGE4C_PP_CHEMICAL_MARGIN_BREAK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "PP/chemical commodity margin-break path produced weak MFE and deep 90D/180D MAE. C17 should route this to 4C/protection when spread recovery, leverage, and margin bridge fail.", "current_profile_verdict": "current_profile_4C_needed_if_chemical_commodity_margin_break_has_deep_MAE_and_no_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in selected 2024 window; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L91_C17_OCI_2024_STAGE2_ACTIONABLE_POLYSILICON_CHEMICAL_SPREAD_RECOVERY", "case_id": "R4L91_C17_OCI_2024_POLYSILICON_CHEMICAL_SPREAD_RECOVERY_POSITIVE", "symbol": "010060", "company_name": "OCI홀딩스", "round": "R4", "loop": "91", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP", "sector": "polysilicon_chemical_spread_recovery", "primary_archetype": "spread_margin_revision_bridge_with_later_cycle_watch", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_protection_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-17", "entry_date": "2024-01-17", "entry_price": 93400.0, "evidence_available_at_that_date": "polysilicon / chemical spread recovery, cost-spread, inventory and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["chemical_spread_recovery_proxy", "inventory_repricing_watch", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["commodity_cycle_later_watch", "valuation_repricing_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010060/2024.csv", "profile_path": "atlas/symbol_profiles/010/010060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.99, "MFE_90D_pct": 20.99, "MFE_180D_pct": 20.99, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.93, "MAE_90D_pct": -9.31, "MAE_180D_pct": -30.51, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-07", "peak_price": 113000.0, "drawdown_after_peak_pct": -42.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_commodity_cycle_4B_watch_needed", "four_b_evidence_type": ["commodity_spread_premium", "valuation_repricing", "cycle_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_polysilicon_chemical_spread_recovery_with_later_cycle_watch", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023_name_split_event", "same_entry_group_id": "R4L91_C17_010060_2024-01-17_93400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L91_C17_KUKDO_2024_STAGE2_FALSE_POSITIVE_EPOXY_SPREAD_RECOVERY", "case_id": "R4L91_C17_KUKDO_2024_EPOXY_SPREAD_FALSE_STAGE2", "symbol": "007690", "company_name": "국도화학", "round": "R4", "loop": "91", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP", "sector": "epoxy_chemical_spread_recovery_watch", "primary_archetype": "epoxy_spread_watch_without_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_protection_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-20", "entry_price": 40400.0, "evidence_available_at_that_date": "epoxy/chemical spread recovery watch and commodity cost spread proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["epoxy_spread_recovery_watch", "chemical_margin_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "margin_revision_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007690/2024.csv", "profile_path": "atlas/symbol_profiles/007/007690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.22, "MFE_90D_pct": 3.22, "MFE_180D_pct": 3.22, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.18, "MAE_90D_pct": -12.38, "MAE_180D_pct": -18.81, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 41700.0, "drawdown_after_peak_pct": -21.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "epoxy_spread_recovery_watch_was_false_stage2_due_missing_margin_revision_bridge", "four_b_evidence_type": ["commodity_spread_watch", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_epoxy_spread_recovery_without_margin_revision_bridge", "current_profile_verdict": "current_profile_false_positive_if_epoxy_chemical_spread_watch_counts_without_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2021_CA", "same_entry_group_id": "R4L91_C17_007690_2024-02-20_40400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R4L91_C17_HYOSUNGCHEM_2024_STAGE4C_PP_CHEMICAL_MARGIN_BREAK", "case_id": "R4L91_C17_HYOSUNGCHEM_2024_PP_CHEMICAL_MARGIN_BREAK_4C", "symbol": "298000", "company_name": "효성화학", "round": "R4", "loop": "91", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP", "sector": "PP_chemical_commodity_margin_break", "primary_archetype": "chemical_margin_break_leverage_4C", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_protection_test | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 76200.0, "evidence_available_at_that_date": "PP/chemical commodity margin break, leverage and revision deterioration proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["chemical_margin_recovery_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "post_spike_drawdown"], "stage4c_evidence_fields": ["margin_bridge_break", "leverage_risk", "deep_MAE90", "deep_MAE180"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298000/2024.csv", "profile_path": "atlas/symbol_profiles/298/298000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.81, "MFE_90D_pct": 3.81, "MFE_180D_pct": 3.81, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.99, "MAE_90D_pct": -27.82, "MAE_180D_pct": -34.91, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-25", "peak_price": 79100.0, "drawdown_after_peak_pct": -37.42, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "hard_4C_chemical_commodity_margin_break", "four_b_evidence_type": ["commodity_margin_break", "positioning_overheat", "leverage_risk"], "four_c_protection_label": "hard_4C_thesis_break", "trigger_outcome_label": "hard_4C_success_PP_chemical_margin_break", "current_profile_verdict": "current_profile_4C_needed_if_chemical_commodity_margin_break_has_deep_MAE_and_no_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L91_C17_298000_2024-01-24_76200", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_protection", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L91_C17_OCI_2024_POLYSILICON_CHEMICAL_SPREAD_RECOVERY_POSITIVE", "trigger_id": "R4L91_C17_OCI_2024_STAGE2_ACTIONABLE_POLYSILICON_CHEMICAL_SPREAD_RECOVERY", "symbol": "010060", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 15, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 25, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 45, "execution_risk_score": 40, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable/watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "polysilicon_chemical_spread_recovery_positive_with_later_cycle_watch", "MFE_90D_pct": 20.99, "MAE_90D_pct": -9.31, "score_return_alignment_label": "polysilicon_chemical_spread_recovery_positive_with_later_cycle_watch", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L91_C17_KUKDO_2024_EPOXY_SPREAD_FALSE_STAGE2", "trigger_id": "R4L91_C17_KUKDO_2024_STAGE2_FALSE_POSITIVE_EPOXY_SPREAD_RECOVERY", "symbol": "007690", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 15, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "epoxy_spread_false_stage2", "MFE_90D_pct": 3.22, "MAE_90D_pct": -12.38, "score_return_alignment_label": "epoxy_spread_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_epoxy_chemical_spread_watch_counts_without_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L91_C17_HYOSUNGCHEM_2024_PP_CHEMICAL_MARGIN_BREAK_4C", "trigger_id": "R4L91_C17_HYOSUNGCHEM_2024_STAGE4C_PP_CHEMICAL_MARGIN_BREAK", "symbol": "298000", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 15, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 65, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2/Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage4C-protection", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "PP_chemical_margin_break_4C_guard", "MFE_90D_pct": 3.81, "MAE_90D_pct": -27.82, "score_return_alignment_label": "PP_chemical_margin_break_4C_guard", "current_profile_verdict": "current_profile_4C_needed_if_chemical_commodity_margin_break_has_deep_MAE_and_no_revision_bridge"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "91", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYSILICON_CHEMICAL_SPREAD_RECOVERY_VS_EPOXY_AND_PP_CHEMICAL_MARGIN_BREAK_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 0, "4C_case_count": 1, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_thesis_break_routes_to_4c", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["polysilicon_spread_recovery_positive_with_cycle_watch", "epoxy_spread_false_stage2", "PP_chemical_margin_break_4C"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
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
10. Add tests that C17 hard-4C rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R4
completed_loop = 91
next_round = R5
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
