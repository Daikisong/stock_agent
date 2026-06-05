# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R13
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id = EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88
loop_objective = cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only
output_file = e2r_stock_web_v12_residual_round_R13_loop_88_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

R13 is a cross-archetype checkpoint, not a new sector round. This file reviews 8 reused loop-88 rows from R9~R12.

```text
is_new_independent_case = false for every row
independent_evidence_weight = 0.0 for every row
do_not_count_as_new_case = true for every row
dedupe_for_aggregate = false for every row
aggregate_group_role = r13_review_only
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes stress-tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R13
scheduled_loop = 88
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_sector_consistency = pass
computed_next_round = R1
computed_next_loop = 89
```

R13 scope is cross-archetype 4B/4C red-team review. The reviewed rows span:

```text
C29 mobility false Stage2 / auto-parts event cap
C30 construction PF false Stage2 / workout event cap
C31 policy false Stage2 / digital education event cap
C32 governance control-premium event cap / capital-structure false Stage2
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key is respected:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This file is not claiming new independent cases. It reuses prior loop-88 research rows to test whether the same failure pattern repeats across canonical archetypes. Because the rows are reused, every case/trigger row is explicitly marked as review-only.

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
| tradable_row_count | 14354401 |
| symbol_count | 5414 |

## 5. Historical Eligibility Gate

| review case | symbol | entry_date | forward 180D | OHLC valid | CA clean | calibration_usable | new independent? |
|---|---|---:|---:|---|---|---|---|
| C29 KG Mobility false Stage2 | 003620 | 2024-01-02 | 180 | yes | yes-after-2023-CA | true | false |
| C29 HL Mando event cap | 204320 | 2024-06-26 | 180 | yes | yes | true | false |
| C30 Dong-Ah false Stage2 | 028100 | 2024-01-30 | 180 | yes | yes | true | false |
| C30 Taeyoung workout event cap | 009410 | 2025-03-21 | 180 | yes | post-2024-10-31-CA | true | false |
| C31 NE Neungyule false Stage2 | 053290 | 2024-01-30 | 180 | yes | yes | true | false |
| C31 YBM Net event cap | 057030 | 2024-02-29 | 180 | yes | yes | true | false |
| C32 YTN control-sale cap | 040300 | 2023-10-25 | 180 | yes | yes | true | false |
| C32 Dongwon capital-structure false Stage2 | 006040 | 2024-05-16 | 180 | yes | post-2024-05-14-CA | true | false |

## 6. Canonical Archetype Compression Map

| R13 review bucket | source canonical | compression rule |
|---|---|---|
| bridge_missing_false_stage2 | C29/C30/C31/C32 | Stage2-like signal needs a durable non-price bridge before positive promotion. |
| event_premium_cap_4B | C29/C30/C31/C32 | Theme, policy, workout, control-sale, or mobility premium near local/full-window peak routes to 4B/watch. |
| conversion_required | C29/C30/C31/C32 | Each canonical has its own conversion bridge: margin/cashflow/PF/policy-to-revenue/control-premium spread. |

## 7. Case Selection Summary

| source round | original canonical | symbol | trigger_type | entry_date | entry_price | R13 label |
|---|---|---|---|---:|---:|---|
| R9 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 003620 | Stage2-Actionable | 2024-01-02 | 8740.0 | stage2_false_positive_bridge_missing |
| R9 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 204320 | Stage4B | 2024-06-26 | 45600.0 | event_cap_4B |
| R10 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 028100 | Stage2-Actionable | 2024-01-30 | 14980.0 | stage2_false_positive_event_cap |
| R10 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 009410 | Stage4B | 2025-03-21 | 3215.0 | event_cap_4B_high_MAE |
| R11 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 053290 | Stage2-Actionable | 2024-01-30 | 5510.0 | stage2_false_positive_policy_theme |
| R11 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 057030 | Stage4B | 2024-02-29 | 4905.0 | event_cap_4B_policy_theme |
| R12 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 040300 | Stage4B | 2023-10-25 | 7970.0 | event_cap_4B_control_sale |
| R12 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 006040 | Stage2-Actionable | 2024-05-16 | 37050.0 | stage2_false_positive_capital_structure_event |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 0
counterexample_count = 8
4B_case_count = 4
4C_case_count = 0
new_independent_case_count = 0
reused_case_count = 8
```

R13 intentionally contains no new sector positive case.

## 9. Evidence Source Map

| source round | symbol | evidence status | evidence_url_pending | source_proxy_only | R13 usage |
|---|---|---|---|---|---|
| R9 | 003620 | prior v12 source proxy | true | true | guardrail review |
| R9 | 204320 | prior v12 source proxy | true | true | event-cap review |
| R10 | 028100 | prior v12 source proxy | true | true | guardrail review |
| R10 | 009410 | prior v12 source proxy | true | true | event-cap review |
| R11 | 053290 | prior v12 source proxy | true | true | guardrail review |
| R11 | 057030 | prior v12 source proxy | true | true | event-cap review |
| R12 | 040300 | prior v12 source proxy | true | true | event-cap review |
| R12 | 006040 | prior v12 source proxy | true | true | guardrail review |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003620 | atlas/ohlcv_tradable_by_symbol_year/003/003620/2024.csv | atlas/symbol_profiles/003/003620.json |
| 204320 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv | atlas/symbol_profiles/204/204320.json |
| 028100 | atlas/ohlcv_tradable_by_symbol_year/028/028100/2024.csv | atlas/symbol_profiles/028/028100.json |
| 009410 | atlas/ohlcv_tradable_by_symbol_year/009/009410/2025.csv | atlas/symbol_profiles/009/009410.json |
| 053290 | atlas/ohlcv_tradable_by_symbol_year/053/053290/2024.csv | atlas/symbol_profiles/053/053290.json |
| 057030 | atlas/ohlcv_tradable_by_symbol_year/057/057030/2024.csv | atlas/symbol_profiles/057/057030.json |
| 040300 | atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv; 2024.csv | atlas/symbol_profiles/040/040300.json |
| 006040 | atlas/ohlcv_tradable_by_symbol_year/006/006040/2024.csv | atlas/symbol_profiles/006/006040.json |

## 11. Trigger-Level OHLC Backtest Tables

| symbol | original canonical | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 003620 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 8740.0 | 1.6 | -13.04 | 1.6 | -34.9 | 1.6 | -40.27 | 2024-01-02 | 8880.0 | -41.22 |
| 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 45600.0 | 1.75 | -15.57 | 1.75 | -30.81 | 1.75 | -32.35 | 2024-06-26 | 46400.0 | -33.51 |
| 028100 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 14980.0 | 4.27 | -14.22 | 4.27 | -16.56 | 4.27 | -24.37 | 2024-01-30 | 15620.0 | -25.8 |
| 009410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3215.0 | 26.91 | -28.46 | 26.91 | -42.3 | 26.91 | -44.82 | 2025-03-21 | 4080.0 | -45.54 |
| 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 5510.0 | 15.25 | -7.44 | 15.25 | -27.77 | 15.25 | -50.18 | 2024-01-30 | 6350.0 | -56.77 |
| 057030 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 4905.0 | 13.76 | -18.45 | 13.76 | -26.5 | 13.76 | -39.65 | 2024-02-29 | 5580.0 | -46.95 |
| 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 7970.0 | 20.45 | -32.12 | 20.45 | -39.08 | 20.45 | -50.19 | 2023-10-25 | 9600.0 | -58.65 |
| 006040 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 37050.0 | 3.64 | -9.04 | 3.64 | -21.32 | 3.64 | -23.08 | 2024-05-17 | 38400.0 | -24.09 |

```text
avg_MFE_90D_pct = 10.95
avg_MAE_90D_pct = -29.9
avg_MFE_180D_pct = 10.95
avg_MAE_180D_pct = -38.11
stage2_false_positive_review_count = 4
event_cap_review_count = 4
high_MAE_review_count = 7 / 8
```

## 12. Current Calibrated Profile Stress Test

| axis | R13 verdict |
|---|---|
| stage2_required_bridge | existing_axis_strengthened: Stage2-like signals require durable non-price bridge before positive promotion. |
| local_4b_watch_guard | existing_axis_strengthened: event premium / theme spike rows should route to 4B/watch near cap. |
| full_4b_requires_non_price_evidence | existing_axis_kept. |
| price_only_blowoff_blocks_positive_stage | existing_axis_kept. |
| hard_4c_thesis_break_routes_to_4c | existing_axis_kept; no hard 4C promoted. |

## 13. Stage2 / Yellow / Green Comparison

R13 does not add new Green cases. It reviews cases where Stage2/Yellow-like interpretation would have been dangerous.

| bucket | reviewed rows | interpretation |
|---|---:|---|
| Stage2 false positive | 4 | MFE was too weak or MAE too large without durable bridge. |
| Stage3/Yellow-like event cap | 4 | Event premium should be treated as 4B/watch rather than structural Green. |
| hard 4C | 0 | No new hard thesis-break route proposed. |

```text
green_lateness_ratio = not_applicable
reason = R13 4B/4C red-team review, no new Stage3-Green trigger
```

## 14. 4B Local vs Full-window Timing Audit

| symbol | original canonical | 4B local proximity | 4B full-window proximity | timing verdict |
|---|---|---:|---:|---|
| 204320 | C29 | 1.00 | 1.00 | auto-parts event cap |
| 028100 | C30 | 1.00 | 1.00 | contract beta spike was event cap |
| 009410 | C30 | 1.00 | 1.00 | workout event premium cap |
| 053290 | C31 | 1.00 | 1.00 | education policy theme cap |
| 057030 | C31 | 1.00 | 1.00 | digital education event cap |
| 040300 | C32 | 1.00 | 1.00 | broadcast control sale event cap |
| 006040 | C32 | 1.00 | 1.00 | capital-structure false Stage2 cap |
| 003620 | C29 | 0.00 | 0.00 | OEM rebound false Stage2 was peak-like from entry |

## 15. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for all review rows
```

This review supports watch/4B routing. It does not promote hard 4C.

## 16. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R13 cross-archetype checkpoint; not a sector-specific rule proposal.
```

## 17. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
rule = Across C29/C30/C31/C32, if the signal is an event premium, policy/theme spike, contract headline, capital-structure label, or OEM rebound without durable non-price bridge, block Stage2/Stage3 positive promotion and route to watch/4B.
proposal_status = guardrail_stress_test_only_not_production
```

## 18. Before / After Backtest Comparison

| profile | hypothesis | reviewed triggers | avg_MFE90 | avg_MAE90 | high_MAE_count | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 8 | 10.95 | -29.9 | 7/8 | guardrails needed |
| P0b e2r_2_0_baseline_reference | older baseline | 8 | 10.95 | -29.9 | 7/8 | weaker bridge/cap handling |
| P1 cross_guard_candidate_profile | cross event-cap guard | 8 | 10.95 | -29.9 | 7/8 | improves rejection alignment |
| P2 archetype_specific_candidate_profile | original canonical bridge requirements | 8 | 10.95 | -29.9 | 7/8 | best explanatory fit |
| P3 counterexample_guard_profile | reject all reviewed positives | 8 | 10.95 | -29.9 | 7/8 | safest but review-only |

## 19. Score-Return Alignment Matrix

| symbol | original canonical | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---|---:|---|---:|---|---:|---:|---|
| 003620 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 66 | Stage2-Actionable | 53 | Stage1/Watch | 1.6 | -34.9 | r13_event_cap_guardrail_improves_alignment |
| 204320 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.75 | -30.81 | r13_event_cap_guardrail_improves_alignment |
| 028100 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 66 | Stage2-Actionable | 53 | Stage1/Watch | 4.27 | -16.56 | r13_event_cap_guardrail_improves_alignment |
| 009410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 26.91 | -42.3 | r13_event_cap_guardrail_improves_alignment |
| 053290 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 66 | Stage2-Actionable | 53 | Stage1/Watch | 15.25 | -27.77 | r13_event_cap_guardrail_improves_alignment |
| 057030 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 13.76 | -26.5 | r13_event_cap_guardrail_improves_alignment |
| 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 20.45 | -39.08 | r13_event_cap_guardrail_improves_alignment |
| 006040 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 66 | Stage2-Actionable | 53 | Stage1/Watch | 3.64 | -21.32 | r13_event_cap_guardrail_improves_alignment |

## 20. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "positive_case_count": 0, "counterexample_count": 8, "4B_case_count": 4, "4C_case_count": 0, "new_independent_case_count": 0, "reused_case_count": 8, "calibration_usable_trigger_count": 8, "representative_trigger_count": 0, "current_profile_error_count": 8, "sector_rule_candidate": false, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "R13 cross-review validates event-premium and bridge-missing guardrails across C29/C30/C31/C32 using loop-88 reused rows only."}
```

## 21. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 8
reused_case_ids: R9L88_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2, R9L88_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B, R10L88_C30_DONGAH_2024_TUNNELING_CONTRACT_FALSE_STAGE2, R10L88_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B, R11L88_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2, R11L88_C31_YBMNET_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B, R12L88_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B, R12L88_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 0
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: bridge_missing_false_stage2, event_premium_cap_4B, policy_or_control_or_contract_theme_without_conversion
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: R13 review-only rows cannot add independent evidence weight
loop_contribution_label: axis_stress_test_passed
do_not_propose_new_weight_delta: true
```

## 22. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Reused stock-web tradable raw OHLC paths
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- 4B event-cap and false Stage2 cross-archetype guardrail
- R13 no-new-case enforcement
```

Non-validation scope:

```text
- No new sector-specific positive case.
- Exact as-of evidence URLs remain pending for reused rows.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 23. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,configured,keep_bridge_required_before_positive_stage,0,"Across C29/C30/C31/C32 loop-88 rows, Stage2-like signals without durable volume/margin/cashflow/policy-to-revenue/control-premium bridge were weak-MFE or high-MAE","avg_MFE90=10.95; avg_MAE90=-29.9; high_MAE_count=7/8","R13L88_REVIEW_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND|R13L88_REVIEW_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA|R13L88_REVIEW_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME|R13L88_REVIEW_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT",8,0,8,medium,r13_guardrail_review_only,"do_not_count_as_new_case=true; no production delta"
shadow_weight,local_4b_watch_guard,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,configured,keep_event_premium_cap_as_4B_watch,0,"Auto-parts, workout, digital-education, broadcast-control-sale event premiums reached local/full-window peaks near trigger and then drew down","Stage4B review rows=4; avg_MFE90=10.95; avg_MAE90=-29.9","R13L88_REVIEW_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP|R13L88_REVIEW_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP|R13L88_REVIEW_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP|R13L88_REVIEW_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP",8,0,8,medium,r13_guardrail_review_only,"R13 review rows must not add independent case weight"
```

## 24. Machine-Readable Rows

### 24.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 24.2 case rows

```jsonl
{"row_type": "case", "case_id": "R13L88_REVIEW_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2", "symbol": "003620", "company_name": "KG모빌리티", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "case_type": "r13_cross_archetype_4b_4c_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L88_REVIEW_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / R9L88_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge", "current_profile_verdict": "current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused prior loop-88 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L88_REVIEW_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B", "symbol": "204320", "company_name": "HL만도", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "case_type": "r13_cross_archetype_4b_4c_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L88_REVIEW_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / R9L88_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped", "current_profile_verdict": "current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused prior loop-88 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L88_REVIEW_C30_DONGAH_2024_CONTRACT_BETA_FALSE_STAGE2", "symbol": "028100", "company_name": "동아지질", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "case_type": "r13_cross_archetype_4b_4c_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L88_REVIEW_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / R10L88_C30_DONGAH_2024_TUNNELING_CONTRACT_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge", "current_profile_verdict": "current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused prior loop-88 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L88_REVIEW_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B", "symbol": "009410", "company_name": "태영건설", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "case_type": "r13_cross_archetype_4b_4c_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L88_REVIEW_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / R10L88_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_workout_event_premium_not_capped", "current_profile_verdict": "current_profile_4B_too_late_if_workout_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused prior loop-88 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L88_REVIEW_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2", "symbol": "053290", "company_name": "NE능률", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "case_type": "r13_cross_archetype_4b_4c_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L88_REVIEW_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / R11L88_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused prior loop-88 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L88_REVIEW_C31_YBMNET_2024_DIGITAL_EDU_EVENT_CAP_4B", "symbol": "057030", "company_name": "YBM넷", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "case_type": "r13_cross_archetype_4b_4c_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L88_REVIEW_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / R11L88_C31_YBMNET_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused prior loop-88 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L88_REVIEW_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B", "symbol": "040300", "company_name": "YTN", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "case_type": "r13_cross_archetype_4b_4c_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L88_REVIEW_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / R12L88_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_control_sale_premium_cap_not_detected", "current_profile_verdict": "current_profile_4B_too_late_if_control_sale_premium_cap_not_detected", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused prior loop-88 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L88_REVIEW_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2", "symbol": "006040", "company_name": "동원산업", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "case_type": "r13_cross_archetype_4b_4c_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L88_REVIEW_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / R12L88_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge", "current_profile_verdict": "current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 cross-review row; reused prior loop-88 evidence only; not a new independent case."}
```

### 24.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R13L88_REVIEW_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND", "case_id": "R13L88_REVIEW_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2", "symbol": "003620", "company_name": "KG모빌리티", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "sector": "cross_archetype_event_cap_redteam", "primary_archetype": "event_premium_cap_and_stage2_bridge_review", "original_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "original_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "original_case_id": "R9L88_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2", "original_trigger_id": "R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND", "loop_objective": "cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 8740.0, "evidence_available_at_that_date": "reused evidence from prior loop-88 v12 sector research; R13 red-team review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["OEM_rebound_watch", "volume_recovery_proxy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE", "deep_MAE", "margin_cashflow_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003620/2024.csv", "profile_path": "atlas/symbol_profiles/003/003620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.6, "MFE_90D_pct": 1.6, "MFE_180D_pct": 1.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.04, "MAE_90D_pct": -34.9, "MAE_180D_pct": -40.27, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 8880.0, "drawdown_after_peak_pct": -41.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "weak_MFE_high_MAE_false_stage2_OEM_turnaround_without_margin_bridge", "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_stage2_false_positive_bridge_missing", "current_profile_verdict": "current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023_relisting_CA", "same_entry_group_id": "R13L88_REVIEW_003620_2024-01-02_8740.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "stage2_false_positive_bridge_missing"}
{"row_type": "trigger", "trigger_id": "R13L88_REVIEW_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP", "case_id": "R13L88_REVIEW_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B", "symbol": "204320", "company_name": "HL만도", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "sector": "cross_archetype_event_cap_redteam", "primary_archetype": "event_premium_cap_and_stage2_bridge_review", "original_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "original_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "original_case_id": "R9L88_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B", "original_trigger_id": "R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP", "loop_objective": "cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only", "trigger_type": "Stage4B", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 45600.0, "evidence_available_at_that_date": "reused evidence from prior loop-88 v12 sector research; R13 red-team review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["auto_parts_theme", "ADAS_mobility_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv", "profile_path": "atlas/symbol_profiles/204/204320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.75, "MFE_90D_pct": 1.75, "MFE_180D_pct": 1.75, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.57, "MAE_90D_pct": -30.81, "MAE_180D_pct": -32.35, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 46400.0, "drawdown_after_peak_pct": -33.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_auto_parts_mobility_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_event_cap_4B", "current_profile_verdict": "current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L88_REVIEW_204320_2024-06-26_45600.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_4B"}
{"row_type": "trigger", "trigger_id": "R13L88_REVIEW_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA", "case_id": "R13L88_REVIEW_C30_DONGAH_2024_CONTRACT_BETA_FALSE_STAGE2", "symbol": "028100", "company_name": "동아지질", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "sector": "cross_archetype_event_cap_redteam", "primary_archetype": "event_premium_cap_and_stage2_bridge_review", "original_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "original_case_id": "R10L88_C30_DONGAH_2024_TUNNELING_CONTRACT_FALSE_STAGE2", "original_trigger_id": "R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA", "loop_objective": "cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-30", "entry_date": "2024-01-30", "entry_price": 14980.0, "evidence_available_at_that_date": "reused evidence from prior loop-88 v12 sector research; R13 red-team review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["infra_contract_headline", "relative_strength_spike", "construction_beta"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "cashflow_balance_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028100/2024.csv", "profile_path": "atlas/symbol_profiles/028/028100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.27, "MFE_90D_pct": 4.27, "MFE_180D_pct": 4.27, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -14.22, "MAE_90D_pct": -16.56, "MAE_180D_pct": -24.37, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-30", "peak_price": 15620.0, "drawdown_after_peak_pct": -25.8, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "contract_beta_spike_was_event_cap_false_stage2", "four_b_evidence_type": ["price_only", "positioning_overheat", "contract_headline_without_margin_bridge"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_stage2_false_positive_event_cap", "current_profile_verdict": "current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L88_REVIEW_028100_2024-01-30_14980.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R10L88_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "stage2_false_positive_event_cap"}
{"row_type": "trigger", "trigger_id": "R13L88_REVIEW_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP", "case_id": "R13L88_REVIEW_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B", "symbol": "009410", "company_name": "태영건설", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "sector": "cross_archetype_event_cap_redteam", "primary_archetype": "event_premium_cap_and_stage2_bridge_review", "original_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "original_case_id": "R10L88_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B", "original_trigger_id": "R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP", "loop_objective": "cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only", "trigger_type": "Stage4B", "trigger_date": "2025-03-21", "entry_date": "2025-03-21", "entry_price": 3215.0, "evidence_available_at_that_date": "reused evidence from prior loop-88 v12 sector research; R13 red-team review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["workout_event_premium", "PF_restructuring_headline", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "post_peak_drawdown", "balance_repair_uncertainty"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2025.csv", "profile_path": "atlas/symbol_profiles/009/009410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.91, "MFE_90D_pct": 26.91, "MFE_180D_pct": 26.91, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.46, "MAE_90D_pct": -42.3, "MAE_180D_pct": -44.82, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-21", "peak_price": 4080.0, "drawdown_after_peak_pct": -45.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_workout_event_premium_cap", "four_b_evidence_type": ["event_premium", "positioning_overheat", "balance_repair_uncertainty"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_event_cap_4B_high_MAE", "current_profile_verdict": "current_profile_4B_too_late_if_workout_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-10-31_CA_window", "same_entry_group_id": "R13L88_REVIEW_009410_2025-03-21_3215.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R10L88_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_4B_high_MAE"}
{"row_type": "trigger", "trigger_id": "R13L88_REVIEW_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "case_id": "R13L88_REVIEW_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2", "symbol": "053290", "company_name": "NE능률", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "sector": "cross_archetype_event_cap_redteam", "primary_archetype": "event_premium_cap_and_stage2_bridge_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "original_case_id": "R11L88_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2", "original_trigger_id": "R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "loop_objective": "cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-30", "entry_date": "2024-01-30", "entry_price": 5510.0, "evidence_available_at_that_date": "reused evidence from prior loop-88 v12 sector research; R13 red-team review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["education_policy_theme", "digital_textbook_or_curriculum_policy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_spike", "weak_conversion_bridge", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053290/2024.csv", "profile_path": "atlas/symbol_profiles/053/053290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.25, "MFE_90D_pct": 15.25, "MFE_180D_pct": 15.25, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.44, "MAE_90D_pct": -27.77, "MAE_180D_pct": -50.18, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-30", "peak_price": 6350.0, "drawdown_after_peak_pct": -56.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "policy_theme_spike_was_event_cap_false_stage2", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_stage2_false_positive_policy_theme", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L88_REVIEW_053290_2024-01-30_5510.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R11L88_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "stage2_false_positive_policy_theme"}
{"row_type": "trigger", "trigger_id": "R13L88_REVIEW_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "case_id": "R13L88_REVIEW_C31_YBMNET_2024_DIGITAL_EDU_EVENT_CAP_4B", "symbol": "057030", "company_name": "YBM넷", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "sector": "cross_archetype_event_cap_redteam", "primary_archetype": "event_premium_cap_and_stage2_bridge_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "original_case_id": "R11L88_C31_YBMNET_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B", "original_trigger_id": "R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "loop_objective": "cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only", "trigger_type": "Stage4B", "trigger_date": "2024-02-29", "entry_date": "2024-02-29", "entry_price": 4905.0, "evidence_available_at_that_date": "reused evidence from prior loop-88 v12 sector research; R13 red-team review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["digital_education_policy_theme", "relative_strength_spike", "policy_event_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/057/057030/2024.csv", "profile_path": "atlas/symbol_profiles/057/057030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.76, "MFE_90D_pct": 13.76, "MFE_180D_pct": 13.76, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.45, "MAE_90D_pct": -26.5, "MAE_180D_pct": -39.65, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-29", "peak_price": 5580.0, "drawdown_after_peak_pct": -46.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_digital_education_policy_event_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_event_cap_4B_policy_theme", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L88_REVIEW_057030_2024-02-29_4905.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R11L88_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_4B_policy_theme"}
{"row_type": "trigger", "trigger_id": "R13L88_REVIEW_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP", "case_id": "R13L88_REVIEW_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B", "symbol": "040300", "company_name": "YTN", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "sector": "cross_archetype_event_cap_redteam", "primary_archetype": "event_premium_cap_and_stage2_bridge_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "original_case_id": "R12L88_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B", "original_trigger_id": "R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP", "loop_objective": "cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only", "trigger_type": "Stage4B", "trigger_date": "2023-10-25", "entry_date": "2023-10-25", "entry_price": 7970.0, "evidence_available_at_that_date": "reused evidence from prior loop-88 v12 sector research; R13 red-team review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["control_sale_premium", "ownership_change_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "control_transfer_uncertainty", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv|atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv", "profile_path": "atlas/symbol_profiles/040/040300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.45, "MFE_90D_pct": 20.45, "MFE_180D_pct": 20.45, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -32.12, "MAE_90D_pct": -39.08, "MAE_180D_pct": -50.19, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-25", "peak_price": 9600.0, "drawdown_after_peak_pct": -58.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_broadcast_control_sale_event_cap", "four_b_evidence_type": ["control_premium_or_event_premium", "legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_event_cap_4B_control_sale", "current_profile_verdict": "current_profile_4B_too_late_if_control_sale_premium_cap_not_detected", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L88_REVIEW_040300_2023-10-25_7970.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R12L88_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_4B_control_sale"}
{"row_type": "trigger", "trigger_id": "R13L88_REVIEW_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT", "case_id": "R13L88_REVIEW_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2", "symbol": "006040", "company_name": "동원산업", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "sector": "cross_archetype_event_cap_redteam", "primary_archetype": "event_premium_cap_and_stage2_bridge_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "original_case_id": "R12L88_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2", "original_trigger_id": "R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT", "loop_objective": "cross_archetype_redteam | 4B_non_price_requirement_stress_test | stage2_false_positive_review | high_MAE_guardrail | no_new_case_reuse_only", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 37050.0, "evidence_available_at_that_date": "reused evidence from prior loop-88 v12 sector research; R13 red-team review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["capital_structure_event", "governance_discount_repair_watch", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE", "no_control_premium_spread", "post_event_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006040/2024.csv", "profile_path": "atlas/symbol_profiles/006/006040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.64, "MFE_90D_pct": 3.64, "MFE_180D_pct": 3.64, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.04, "MAE_90D_pct": -21.32, "MAE_180D_pct": -23.08, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-17", "peak_price": 38400.0, "drawdown_after_peak_pct": -24.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "capital_structure_event_was_false_stage2_event_cap", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_stage2_false_positive_capital_structure_event", "current_profile_verdict": "current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-05-14_CA_window", "same_entry_group_id": "R13L88_REVIEW_006040_2024-05-16_37050.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R12L88_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "stage2_false_positive_capital_structure_event"}
```

### 24.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L88_REVIEW_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2", "trigger_id": "R13L88_REVIEW_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND", "symbol": "003620", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "original_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: event premium or theme/contract headline is capped unless verified non-price bridge is durable.", "MFE_90D_pct": 1.6, "MAE_90D_pct": -34.9, "score_return_alignment_label": "r13_event_cap_guardrail_improves_alignment", "current_profile_verdict": "current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L88_REVIEW_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B", "trigger_id": "R13L88_REVIEW_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP", "symbol": "204320", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "original_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: event premium or theme/contract headline is capped unless verified non-price bridge is durable.", "MFE_90D_pct": 1.75, "MAE_90D_pct": -30.81, "score_return_alignment_label": "r13_event_cap_guardrail_improves_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L88_REVIEW_C30_DONGAH_2024_CONTRACT_BETA_FALSE_STAGE2", "trigger_id": "R13L88_REVIEW_C30_DONGAH_2024_STAGE2_FALSE_POSITIVE_CONTRACT_BETA", "symbol": "028100", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: event premium or theme/contract headline is capped unless verified non-price bridge is durable.", "MFE_90D_pct": 4.27, "MAE_90D_pct": -16.56, "score_return_alignment_label": "r13_event_cap_guardrail_improves_alignment", "current_profile_verdict": "current_profile_false_positive_if_contract_or_infra_beta_counts_without_cashflow_balance_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L88_REVIEW_C30_TAEYOUNG_2025_WORKOUT_EVENT_CAP_4B", "trigger_id": "R13L88_REVIEW_C30_TAEYOUNG_2025_STAGE4B_WORKOUT_EVENT_CAP", "symbol": "009410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: event premium or theme/contract headline is capped unless verified non-price bridge is durable.", "MFE_90D_pct": 26.91, "MAE_90D_pct": -42.3, "score_return_alignment_label": "r13_event_cap_guardrail_improves_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_workout_event_premium_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L88_REVIEW_C31_NEE_2024_EDUCATION_POLICY_FALSE_STAGE2", "trigger_id": "R13L88_REVIEW_C31_NEE_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "symbol": "053290", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: event premium or theme/contract headline is capped unless verified non-price bridge is durable.", "MFE_90D_pct": 15.25, "MAE_90D_pct": -27.77, "score_return_alignment_label": "r13_event_cap_guardrail_improves_alignment", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L88_REVIEW_C31_YBMNET_2024_DIGITAL_EDU_EVENT_CAP_4B", "trigger_id": "R13L88_REVIEW_C31_YBMNET_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "symbol": "057030", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: event premium or theme/contract headline is capped unless verified non-price bridge is durable.", "MFE_90D_pct": 13.76, "MAE_90D_pct": -26.5, "score_return_alignment_label": "r13_event_cap_guardrail_improves_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L88_REVIEW_C32_YTN_2023_BROADCAST_CONTROL_SALE_EVENT_CAP_4B", "trigger_id": "R13L88_REVIEW_C32_YTN_2023_STAGE4B_BROADCAST_CONTROL_SALE_CAP", "symbol": "040300", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "original_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: event premium or theme/contract headline is capped unless verified non-price bridge is durable.", "MFE_90D_pct": 20.45, "MAE_90D_pct": -39.08, "score_return_alignment_label": "r13_event_cap_guardrail_improves_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_control_sale_premium_cap_not_detected"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L88_REVIEW_C32_DONGWON_2024_CAPITAL_STRUCTURE_FALSE_STAGE2", "trigger_id": "R13L88_REVIEW_C32_DONGWON_2024_STAGE2_FALSE_POSITIVE_CAPITAL_STRUCTURE_EVENT", "symbol": "006040", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "original_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: event premium or theme/contract headline is capped unless verified non-price bridge is durable.", "MFE_90D_pct": 3.64, "MAE_90D_pct": -21.32, "score_return_alignment_label": "r13_event_cap_guardrail_improves_alignment", "current_profile_verdict": "current_profile_false_positive_if_capital_structure_event_counts_without_control_premium_or_cashflow_bridge"}
```

### 24.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "88", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "EVENT_PREMIUM_CAP_AND_STAGE2_BRIDGE_REVIEW_AFTER_R9_R12_LOOP88", "new_independent_case_count": 0, "reused_case_count": 8, "new_symbol_count": 0, "same_archetype_new_symbol_count": 0, "same_archetype_new_trigger_family_count": 0, "new_trigger_family_count": 0, "positive_case_count": 0, "counterexample_count": 8, "4B_case_count": 4, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["bridge_missing_false_stage2", "event_premium_cap_4B", "policy_or_control_or_contract_theme_without_conversion"], "loop_contribution_label": "axis_stress_test_passed", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 8, "evidence_url_pending_count": 8}
```

### 24.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","reason":"R13 review rows reuse already computed stock-web 180D windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 25. Deferred Coding Agent Handoff Prompt

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
- R13 review rows with `do_not_count_as_new_case=true` must not add weight.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
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
10. Add tests that R13 review-only rows cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 26. Next Round State

```text
completed_round = R13
completed_loop = 88
next_round = R1
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 27. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This R13 file contains no new independent case, no investment recommendation, and no production scoring change.
