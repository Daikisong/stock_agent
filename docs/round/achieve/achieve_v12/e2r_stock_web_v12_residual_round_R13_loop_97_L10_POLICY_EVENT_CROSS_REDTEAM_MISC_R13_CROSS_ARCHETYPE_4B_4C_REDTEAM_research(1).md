# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R13
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id = LOOP97_FALSE_STAGE2_4B_HIGH_MAE_GUARDRAIL_REVIEW
loop_objective = cross_archetype_redteam | stage2_false_positive_review | 4B_4C_redteam | high_MAE_guardrail | bridge_requirement_stress_test | no_new_case_reuse_only
output_file = e2r_stock_web_v12_residual_round_R13_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

This is the R13 loop 97 cross-archetype red-team review. It reuses the R1~R12 loop 97 research outputs as review material only. No new independent cases are introduced, no production scoring is changed, and every machine-readable review row is marked `do_not_count_as_new_case=true`.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes reviewed:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
low_MFE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R13
scheduled_loop = 97
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_sector_consistency = pass
computed_next_round = R1
computed_next_loop = 98
```

R13 is not a new case-mining round. It is the circuit breaker: it checks whether the loop’s false positives and 4B event caps are trying to sneak back into positive-stage promotion through another door.

## 3. Source Coverage / Duplicate Avoidance Check

```text
new_independent_case_count = 0
reused_case_count = 24
reviewed_loop97_source_files = 12
reviewed_total_trigger_count = 36
reviewed_redteam_trigger_count = 24
positive_contrast_count = 12
```

No-Repeat hard key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 4. Source File Matrix

| round | source_file | positive contrast | false Stage2 review | 4B event-cap review | positive canonical |
|---|---|---|---|---|---|
| R1 | `e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md` | 100840 SNT에너지 | 028050 삼성E&A | 045100 한양이엔지 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP |
| R2 | `e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md` | 031980 피에스케이홀딩스 | 036540 SFA반도체 | 080220 제주반도체 | C06_HBM_MEMORY_CUSTOMER_CAPACITY |
| R3 | `e2r_stock_web_v12_residual_round_R3_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md` | 011790 SKC | 243840 신흥에스이씨 | 419050 삼기이브이 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK |
| R4 | `e2r_stock_web_v12_residual_round_R4_loop_97_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md` | 001340 백광산업 | 010060 OCI홀딩스 | 006890 태경케미컬 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD |
| R5 | `e2r_stock_web_v12_residual_round_R5_loop_97_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md` | 023530 롯데쇼핑 | 383220 F&F | 008770 호텔신라 | C19_BRAND_RETAIL_INVENTORY_MARGIN |
| R6 | `e2r_stock_web_v12_residual_round_R6_loop_97_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md` | 032830 삼성생명 | 088350 한화생명 | 000400 롯데손해보험 | C22_INSURANCE_RATE_CYCLE_RESERVE |
| R7 | `e2r_stock_web_v12_residual_round_R7_loop_97_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md` | 335890 비올 | 065510 휴비츠 | 294090 이오플로우 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT |
| R8 | `e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md` | 047560 이스트소프트 | 263860 지니언스 | 356680 엑스게이트 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION |
| R9 | `e2r_stock_web_v12_residual_round_R9_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md` | 064960 SNT모티브 | 092200 디아이씨 | 370090 퓨런티어 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| R10 | `e2r_stock_web_v12_residual_round_R10_loop_97_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md` | 097230 HJ중공업 | 016250 SGC E&C | 046940 우원개발 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| R11 | `e2r_stock_web_v12_residual_round_R11_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md` | 077970 STX엔진 | 361390 제노코 | 024740 한일단조 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG |
| R12 | `e2r_stock_web_v12_residual_round_R12_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md` | 115500 케이씨에스 | 032850 비트컴퓨터 | 094480 갤럭시아머니트리 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |

## 5. Cross-Archetype Review Summary

```text
stage2_false_positive_review_count = 12
event_cap_review_count = 12
hard_4C_review_count = 0
high_MAE_review_count = 21
low_MFE90_review_count = 19
new_independent_case_count = 0
do_not_propose_new_weight_delta = true
```

The dominant failure mode is bridge absence. Across loop97, weak rows often had a label that sounded investable—EPC, HBM, battery contract, policy, medical-device export, software security, defense export—but the missing object was the same gear inside the machine: contract/order quality, customer adoption, delivery, utilization, revenue conversion, margin, and revision.

## 6. Red-Team Review Rows

| source_round | symbol | company | canonical_archetype_id | review_role | MFE90 | MAE90 | severity |
|---|---|---|---|---|---:|---:|---|
| R1 | 028050 | 삼성E&A | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | stage2_false_positive_review | 6.72 | -14.62 | high |
| R2 | 036540 | SFA반도체 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | stage2_false_positive_review | 8.96 | -28.88 | high |
| R3 | 243840 | 신흥에스이씨 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | stage2_false_positive_review | 13.43 | -30.88 | high |
| R4 | 010060 | OCI홀딩스 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | stage2_false_positive_review | 2.54 | -21.87 | very_high |
| R5 | 383220 | F&F | C19_BRAND_RETAIL_INVENTORY_MARGIN | stage2_false_positive_review | 1.18 | -24.58 | very_high |
| R6 | 088350 | 한화생명 | C22_INSURANCE_RATE_CYCLE_RESERVE | stage2_false_positive_review | 7.62 | -27.22 | high |
| R7 | 065510 | 휴비츠 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | stage2_false_positive_review | 20.2 | -32.6 | high |
| R8 | 263860 | 지니언스 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | stage2_false_positive_review | 2.89 | -27.97 | very_high |
| R9 | 092200 | 디아이씨 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | stage2_false_positive_review | 11.97 | -25.89 | high |
| R10 | 016250 | SGC E&C | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | stage2_false_positive_review | 1.23 | -21.11 | very_high |
| R11 | 361390 | 제노코 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | stage2_false_positive_review | 2.37 | -17.4 | very_high |
| R12 | 032850 | 비트컴퓨터 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | stage2_false_positive_review | 10.86 | -30.43 | high |
| R1 | 045100 | 한양이엔지 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | event_cap_review | 7.18 | -13.92 | high |
| R2 | 080220 | 제주반도체 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | event_cap_review | 13.38 | -39.26 | very_high |
| R3 | 419050 | 삼기이브이 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | event_cap_review | 3.31 | -24.4 | high |
| R4 | 006890 | 태경케미컬 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | event_cap_review | 8.09 | -33.08 | high |
| R5 | 008770 | 호텔신라 | C19_BRAND_RETAIL_INVENTORY_MARGIN | event_cap_review | 0.16 | -18.92 | very_high |
| R6 | 000400 | 롯데손해보험 | C22_INSURANCE_RATE_CYCLE_RESERVE | event_cap_review | 1.24 | -37.99 | very_high |
| R7 | 294090 | 이오플로우 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | event_cap_review | 1.72 | -43.42 | very_high |
| R8 | 356680 | 엑스게이트 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | event_cap_review | 5.31 | -26.84 | high |
| R9 | 370090 | 퓨런티어 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | event_cap_review | 6.51 | -27.28 | high |
| R10 | 046940 | 우원개발 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | event_cap_review | 0.14 | -22.6 | very_high |
| R11 | 024740 | 한일단조 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | event_cap_review | 7.08 | -17.79 | high |
| R12 | 094480 | 갤럭시아머니트리 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | event_cap_review | 2.92 | -47.75 | very_high |

## 7. Positive Contrast Rows

These rows are contrast anchors only. They are not counted as new R13 evidence.

| source_round | symbol | company | canonical_archetype_id | MFE90 | MAE90 | bridge quality |
|---|---|---|---|---:|---:|---|
| R1 | 100840 | SNT에너지 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 60.2 | -4.28 | order_quality_delivery_cost_to_complete_margin_revision_bridge |
| R2 | 031980 | 피에스케이홀딩스 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 167.3 | -4.31 | customer_capacity_order_utilization_margin_revision_bridge |
| R3 | 011790 | SKC | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 146.61 | -3.45 | customer_quality_calloff_delivery_utilization_margin_revision_bridge |
| R4 | 001340 | 백광산업 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 131.37 | -10.04 | realized_spread_capacity_customer_margin_revision_bridge |
| R5 | 023530 | 롯데쇼핑 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 28.27 | -11.0 | inventory_turn_category_mix_traffic_markdown_margin_revision_bridge |
| R6 | 032830 | 삼성생명 | C22_INSURANCE_RATE_CYCLE_RESERVE | 70.06 | -2.35 | CSM_reserve_capital_buffer_return_policy_revision_bridge |
| R7 | 335890 | 비올 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 23.08 | -12.01 | installed_base_consumable_distributor_regulatory_margin_revision_bridge |
| R8 | 047560 | 이스트소프트 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 94.15 | -14.81 | recurring_license_retention_enterprise_customer_ARR_margin_revision_bridge |
| R9 | 064960 | SNT모티브 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 12.43 | -2.49 | OEM_volume_powertrain_mix_utilization_margin_revision_bridge |
| R10 | 097230 | HJ중공업 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 25.96 | -10.15 | order_quality_cashflow_funding_balance_sheet_margin_revision_bridge |
| R11 | 077970 | STX엔진 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 49.83 | -0.85 | framework_contract_backlog_delivery_prime_customer_margin_revision_bridge |
| R12 | 115500 | 케이씨에스 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 32.01 | -12.18 | institutional_pilot_procurement_legislation_scope_margin_revision_bridge |

## 8. Red-Team Findings

### 8.1 Stage2 false-positive cluster

The 12 false Stage2 rows show the same mechanism across different sectors:

```text
theme_label_present = true
bridge_evidence_missing = true
promotion_allowed = false
recommended_route = Stage1/Watch or 4B-watch
```

The profile should keep refusing Stage2/Stage3 promotion when the row lacks the sector’s required bridge.

### 8.2 4B event-cap cluster

The 12 event-cap rows support the existing 4B overlay logic:

```text
event_premium_present = true
non_price_bridge_missing = true
event_cap_or_mean_reversion = true
recommended_route = 4B overlay / risk calibration
```

Price-only spikes should not be upgraded into positive evidence unless a durable non-price bridge appears.

### 8.3 4C audit

```text
hard_4C_review_count = 0
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

Loop97 did not introduce a confirmed hard 4C row. Several rows carry thesis-break watch labels, but they remain watch-only rather than hard 4C confirmations.

## 9. Current Calibrated Profile Stress Test

| axis | R13 verdict |
|---|---|
| stage2_required_bridge | strengthened across 12 false Stage2 reviews |
| local_4b_watch_guard | strengthened across 12 event-cap reviews |
| high_MAE_guardrail | strengthened; 21 / 24 review rows meet high-MAE condition |
| low_MFE_guardrail | strengthened; 19 / 24 review rows have MFE90 <= 10 |
| full_4b_requires_non_price_evidence | kept |
| price_only_blowoff_blocks_positive_stage | kept |
| hard_4c_thesis_break_routes_to_4c | kept |

## 10. Before / After Backtest Comparison

| profile | hypothesis | reviewed rows | false-positive/event-cap rows retained as negative | new positive rows | verdict |
|---|---|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current calibrated profile | 24 | 24 | 0 | passes R13 review |
| P1 relaxed-theme-label profile | theme label can promote without bridge | 24 | 0 | 24 incorrectly promoted | rejected |
| P2 bridge-required profile | non-price bridge required before promotion | 24 | 24 | 0 | preferred |
| P3 hard-4C aggressive profile | convert watch-only thesis breaks into 4C | 24 | n/a | 0 | rejected for loop97 because no hard 4C confirmation |

## 11. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "round": "R13", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "reviewed_loop97_source_files": 12, "reviewed_total_trigger_count": 36, "reviewed_redteam_trigger_count": 24, "positive_contrast_count": 12, "stage2_false_positive_review_count": 12, "event_cap_review_count": 12, "hard_4C_review_count": 0, "high_MAE_review_count": 21, "low_MFE90_review_count": 19, "new_independent_case_count": 0, "reused_case_count": 24, "do_not_propose_new_weight_delta": true, "coverage_gap_after_this_loop": "R13 loop97 cross-archetype review confirms Stage2 bridge requirements and 4B event-cap guardrails across all R1~R12 loop97 source files; no new cases are counted."}
```

## 12. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 24
reused_case_ids: loop97 R1~R12 false Stage2 and 4B event-cap rows
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 0
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, low_MFE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: bridge_missing_false_stage2, event_cap_4B, high_MAE_after_bridge_missing_entry, low_MFE_after_policy_or_theme_label_only
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, low_MFE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: R13 is review-only and reuses loop97 rows
loop_contribution_label: axis_stress_test_passed
do_not_propose_new_weight_delta: true
```

## 13. Validation Scope / Non-Validation Scope

Validation scope:

```text
- R1~R12 loop97 source Markdown files generated in this run sequence
- machine-readable trigger rows from those source files
- false Stage2 review rows
- 4B event-cap review rows
- positive rows as contrast only
```

Non-validation scope:

```text
- No new OHLC case selection
- No new independent evidence count
- No production scoring update
- No live candidate scan
- No investment recommendation
```

## 14. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,configured,keep_or_strengthen_bridge_required_before_stage2_promotion,0,"Loop97 false Stage2 rows repeatedly failed when theme labels were not tied to contract/order/customer/adoption/revenue/margin/revision evidence","12 false Stage2 rows reviewed; all remain reject/watch rather than positive-stage promotion","MULTI_LOOP97_FALSE_STAGE2_ROWS",12,0,12,medium,cross_redteam_review_only,"review-only; no production delta"
shadow_weight,local_4b_watch_guard,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,configured,keep_or_strengthen_event_cap_4B_overlay,0,"Loop97 event-premium rows repeatedly capped before durable non-price bridge evidence appeared","12 event-cap rows reviewed; all remain 4B overlay/risk calibration","MULTI_LOOP97_4B_EVENT_CAP_ROWS",12,0,12,medium,cross_redteam_review_only,"review-only; no production delta"
shadow_weight,high_MAE_guardrail,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,configured,keep_or_strengthen_high_MAE_blocks_positive_stage,0,"High or persistent MAE remained the common failure signature across bridge-missing Stage2 and event-cap rows","21 of 24 review rows meet high-MAE review condition using MAE90<=-20 or MAE180<=-20","MULTI_LOOP97_HIGH_MAE_ROWS",24,0,21,medium,cross_redteam_review_only,"review-only; no production delta"
```

## 15. Machine-Readable Rows

### 15.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "review_only_inherited_from_loop97_source_files", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 15.2 redteam_review rows

```jsonl
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_01_R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH", "round": "R13", "loop": "97", "source_round": "R1", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "source_trigger_id": "R1L97_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_GLOBAL_EPC_MARGIN_GAP_WATCH", "source_case_id": "R1L97_C05_SAMSUNGEA_2024_GLOBAL_EPC_MARGIN_GAP_FALSE_STAGE2", "symbol": "028050", "company_name": "삼성E&A", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "high", "MFE_90D_pct": 6.72, "MAE_90D_pct": -14.62, "MAE_180D_pct": -18.18, "four_b_timing_verdict": "global_EPC_contract_watch_was_false_stage2_due_missing_cost_to_complete_margin_revision_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_global_EPC_contract_watch_counts_without_cost_to_complete_change_order_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_02_R2L97_C06_SFASEMI_2024_STAGE2_FALSE_POSITIVE_MEMORY_OSAT_CAPACITY_WATCH", "round": "R13", "loop": "97", "source_round": "R2", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "source_trigger_id": "R2L97_C06_SFASEMI_2024_STAGE2_FALSE_POSITIVE_MEMORY_OSAT_CAPACITY_WATCH", "source_case_id": "R2L97_C06_SFASEMI_2024_MEMORY_OSAT_CAPACITY_FALSE_STAGE2", "symbol": "036540", "company_name": "SFA반도체", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "high", "MFE_90D_pct": 8.96, "MAE_90D_pct": -28.88, "MAE_180D_pct": -35.43, "four_b_timing_verdict": "memory_OSAT_capacity_watch_was_false_stage2_due_missing_customer_order_utilization_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_memory_OSAT_capacity_watch_counts_without_customer_capacity_order_utilization_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_03_R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA", "round": "R13", "loop": "97", "source_round": "R3", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_trigger_id": "R3L97_C12_SHINHEUNGSEC_2024_STAGE2_FALSE_POSITIVE_BATTERY_CAP_CALLOFF_WATCH_POST_CA", "source_case_id": "R3L97_C12_SHINHEUNGSEC_2024_BATTERY_CAP_CALLOFF_FALSE_STAGE2_POST_CA", "symbol": "243840", "company_name": "신흥에스이씨", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "high", "MFE_90D_pct": 13.43, "MAE_90D_pct": -30.88, "MAE_180D_pct": -30.88, "four_b_timing_verdict": "battery_cap_calloff_watch_was_false_stage2_due_missing_customer_delivery_utilization_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_battery_cap_calloff_watch_counts_without_customer_calloff_delivery_utilization_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_04_R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH", "round": "R13", "loop": "97", "source_round": "R4", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_97_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_trigger_id": "R4L97_C17_OCIHOLDINGS_2024_STAGE2_FALSE_POSITIVE_POLYSILICON_SPREAD_WATCH", "source_case_id": "R4L97_C17_OCIHOLDINGS_2024_POLYSILICON_SPREAD_FALSE_STAGE2", "symbol": "010060", "company_name": "OCI홀딩스", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "very_high", "MFE_90D_pct": 2.54, "MAE_90D_pct": -21.87, "MAE_180D_pct": -41.74, "four_b_timing_verdict": "polysilicon_spread_watch_was_false_stage2_due_missing_realized_spread_inventory_margin_revision_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_polysilicon_spread_watch_counts_without_realized_spread_inventory_cost_curve_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_05_R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH", "round": "R13", "loop": "97", "source_round": "R5", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_97_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_trigger_id": "R5L97_C19_FNF_2024_STAGE2_FALSE_POSITIVE_APPAREL_CHINA_INVENTORY_WATCH", "source_case_id": "R5L97_C19_FNF_2024_APPAREL_CHINA_INVENTORY_FALSE_STAGE2", "symbol": "383220", "company_name": "F&F", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "very_high", "MFE_90D_pct": 1.18, "MAE_90D_pct": -24.58, "MAE_180D_pct": -38.37, "four_b_timing_verdict": "apparel_inventory_watch_was_false_stage2_due_missing_sellthrough_markdown_margin_revision_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_apparel_inventory_watch_counts_without_sellthrough_markdown_inventory_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_06_R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH", "round": "R13", "loop": "97", "source_round": "R6", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_97_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_trigger_id": "R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH", "source_case_id": "R6L97_C22_HANWHALIFE_2024_LIFE_RATE_SENSITIVITY_FALSE_STAGE2", "symbol": "088350", "company_name": "한화생명", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "high", "MFE_90D_pct": 7.62, "MAE_90D_pct": -27.22, "MAE_180D_pct": -27.22, "four_b_timing_verdict": "life_insurer_rate_cycle_watch_was_false_stage2_due_missing_CSM_reserve_capital_return_revision_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_life_insurer_rate_sensitivity_watch_counts_without_CSM_reserve_capital_return_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_07_R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH", "round": "R13", "loop": "97", "source_round": "R7", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_97_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_trigger_id": "R7L97_C25_HUVITZ_2024_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_EXPORT_WATCH", "source_case_id": "R7L97_C25_HUVITZ_2024_OPHTHALMIC_DEVICE_EXPORT_FALSE_STAGE2", "symbol": "065510", "company_name": "휴비츠", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "high", "MFE_90D_pct": 20.2, "MAE_90D_pct": -32.6, "MAE_180D_pct": -49.12, "four_b_timing_verdict": "ophthalmic_device_export_watch_was_false_stage2_due_missing_distributor_sellthrough_regulatory_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_ophthalmic_device_export_watch_counts_without_distributor_sellthrough_regulatory_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_08_R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH", "round": "R13", "loop": "97", "source_round": "R8", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_trigger_id": "R8L97_C28_GENIANS_2024_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY_CONTRACT_WATCH", "source_case_id": "R8L97_C28_GENIANS_2024_ENDPOINT_SECURITY_CONTRACT_FALSE_STAGE2", "symbol": "263860", "company_name": "지니언스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "very_high", "MFE_90D_pct": 2.89, "MAE_90D_pct": -27.97, "MAE_180D_pct": -46.56, "four_b_timing_verdict": "endpoint_security_contract_watch_was_false_stage2_due_missing_ARR_retention_margin_revision_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_endpoint_security_watch_counts_without_contract_renewal_ARR_retention_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_09_R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH", "round": "R13", "loop": "97", "source_round": "R9", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_trigger_id": "R9L97_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_EXPORT_VOLUME_WATCH", "source_case_id": "R9L97_C29_DIC_2024_EV_REDUCER_EXPORT_VOLUME_FALSE_STAGE2", "symbol": "092200", "company_name": "디아이씨", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "high", "MFE_90D_pct": 11.97, "MAE_90D_pct": -25.89, "MAE_180D_pct": -25.89, "four_b_timing_verdict": "EV_reducer_export_watch_was_false_stage2_due_missing_OEM_calloff_mix_utilization_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_EV_reducer_export_watch_counts_without_OEM_calloff_mix_utilization_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_10_R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH", "round": "R13", "loop": "97", "source_round": "R10", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_97_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_trigger_id": "R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH", "source_case_id": "R10L97_C30_SGCEC_2024_MIDCAP_EPC_PF_FALSE_STAGE2", "symbol": "016250", "company_name": "SGC E&C", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "very_high", "MFE_90D_pct": 1.23, "MAE_90D_pct": -21.11, "MAE_180D_pct": -25.17, "four_b_timing_verdict": "midcap_EPC_PF_recovery_watch_was_false_stage2_due_missing_cashflow_funding_order_quality_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_midcap_EPC_PF_watch_counts_without_cashflow_funding_order_quality_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_11_R11L97_C03_GENOHCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_WATCH", "round": "R13", "loop": "97", "source_round": "R11", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_trigger_id": "R11L97_C03_GENOHCO_2024_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_COMPONENT_WATCH", "source_case_id": "R11L97_C03_GENOHCO_2024_SPACE_DEFENSE_COMPONENT_FALSE_STAGE2", "symbol": "361390", "company_name": "제노코", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "very_high", "MFE_90D_pct": 2.37, "MAE_90D_pct": -17.4, "MAE_180D_pct": -17.4, "four_b_timing_verdict": "space_defense_component_watch_was_false_stage2_due_missing_prime_contract_export_backlog_delivery_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_space_defense_component_watch_counts_without_prime_contract_export_backlog_delivery_margin_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_12_R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH", "round": "R13", "loop": "97", "source_round": "R12", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_trigger_id": "R12L97_C31_BITCOMPUTER_2024_STAGE2_FALSE_POSITIVE_TELEMEDICINE_POLICY_WATCH", "source_case_id": "R12L97_C31_BITCOMPUTER_2024_TELEMEDICINE_POLICY_FALSE_STAGE2", "symbol": "032850", "company_name": "비트컴퓨터", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_trigger_type": "Stage2-Actionable", "review_role": "stage2_false_positive_review", "review_severity": "high", "MFE_90D_pct": 10.86, "MAE_90D_pct": -30.43, "MAE_180D_pct": -34.61, "four_b_timing_verdict": "telemedicine_policy_watch_was_false_stage2_due_missing_implementation_reimbursement_revenue_bridge", "four_c_protection_label": "policy_implementation_thesis_break_watch_only", "current_profile_verdict": "current_profile_false_positive_if_telemedicine_policy_watch_counts_without_implementation_reimbursement_adoption_revenue_revision_bridge", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_13_R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R1", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "source_trigger_id": "R1L97_C05_HANYANGENG_2024_STAGE4B_SEMICON_FACILITY_EPC_EVENT_CAP", "source_case_id": "R1L97_C05_HANYANGENG_2024_SEMICON_FACILITY_EPC_EVENT_CAP_4B", "symbol": "045100", "company_name": "한양이엔지", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "high", "MFE_90D_pct": 7.18, "MAE_90D_pct": -13.92, "MAE_180D_pct": -13.92, "four_b_timing_verdict": "acceptable_4B_timing_semicon_facility_EPC_event_cap_due_missing_order_execution_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_semicon_facility_EPC_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_14_R2L97_C06_JEJUSEMI_2024_STAGE4B_EDGE_AI_MEMORY_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R2", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "source_trigger_id": "R2L97_C06_JEJUSEMI_2024_STAGE4B_EDGE_AI_MEMORY_EVENT_CAP", "source_case_id": "R2L97_C06_JEJUSEMI_2024_EDGE_AI_MEMORY_EVENT_CAP_4B", "symbol": "080220", "company_name": "제주반도체", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "very_high", "MFE_90D_pct": 13.38, "MAE_90D_pct": -39.26, "MAE_180D_pct": -52.82, "four_b_timing_verdict": "good_full_window_4B_timing_edge_AI_memory_capacity_event_cap", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_edge_AI_memory_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_15_R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R3", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_trigger_id": "R3L97_C12_SAMGIEV_2024_STAGE4B_BATTERY_CASE_CUSTOMER_CONTRACT_EVENT_CAP", "source_case_id": "R3L97_C12_SAMGIEV_2024_BATTERY_CASE_EVENT_CAP_4B", "symbol": "419050", "company_name": "삼기이브이", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "high", "MFE_90D_pct": 3.31, "MAE_90D_pct": -24.4, "MAE_180D_pct": -32.23, "four_b_timing_verdict": "good_full_window_4B_timing_battery_case_contract_event_cap", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_battery_case_contract_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_16_R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R4", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_97_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_trigger_id": "R4L97_C17_TAEKYUNGCHEM_2024_STAGE4B_INDUSTRIAL_GAS_DRYICE_SPREAD_EVENT_CAP", "source_case_id": "R4L97_C17_TAEKYUNGCHEM_2024_INDUSTRIAL_GAS_DRYICE_EVENT_CAP_4B", "symbol": "006890", "company_name": "태경케미컬", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "high", "MFE_90D_pct": 8.09, "MAE_90D_pct": -33.08, "MAE_180D_pct": -33.08, "four_b_timing_verdict": "acceptable_4B_timing_industrial_gas_dryice_spread_event_cap_due_missing_volume_contract_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_industrial_gas_spread_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_17_R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R5", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_97_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_trigger_id": "R5L97_C19_HOTELSHILLA_2024_STAGE4B_DUTY_FREE_RETAIL_INVENTORY_EVENT_CAP", "source_case_id": "R5L97_C19_HOTELSHILLA_2024_DUTY_FREE_RETAIL_EVENT_CAP_4B", "symbol": "008770", "company_name": "호텔신라", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "very_high", "MFE_90D_pct": 0.16, "MAE_90D_pct": -18.92, "MAE_180D_pct": -28.85, "four_b_timing_verdict": "good_full_window_4B_timing_duty_free_retail_inventory_event_cap", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_duty_free_retail_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_18_R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R6", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_97_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_trigger_id": "R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP", "source_case_id": "R6L97_C22_LOTTEINS_2024_INSURANCE_SALE_RESERVE_EVENT_CAP_4B", "symbol": "000400", "company_name": "롯데손해보험", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "very_high", "MFE_90D_pct": 1.24, "MAE_90D_pct": -37.99, "MAE_180D_pct": -37.99, "four_b_timing_verdict": "good_full_window_4B_timing_insurance_sale_reserve_event_cap", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_sale_reserve_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_19_R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R7", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_97_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_trigger_id": "R7L97_C25_EOFLOW_2024_STAGE4B_WEARABLE_INSULIN_DEVICE_EVENT_CAP", "source_case_id": "R7L97_C25_EOFLOW_2024_WEARABLE_INSULIN_DEVICE_EVENT_CAP_4B", "symbol": "294090", "company_name": "이오플로우", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "very_high", "MFE_90D_pct": 1.72, "MAE_90D_pct": -43.42, "MAE_180D_pct": -57.99, "four_b_timing_verdict": "good_full_window_4B_timing_wearable_insulin_device_event_cap", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_wearable_insulin_device_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_20_R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R8", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_trigger_id": "R8L97_C28_XGATE_2024_STAGE4B_NETWORK_SECURITY_GATEWAY_EVENT_CAP", "source_case_id": "R8L97_C28_XGATE_2024_NETWORK_SECURITY_GATEWAY_EVENT_CAP_4B", "symbol": "356680", "company_name": "엑스게이트", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "high", "MFE_90D_pct": 5.31, "MAE_90D_pct": -26.84, "MAE_180D_pct": -39.68, "four_b_timing_verdict": "good_full_window_4B_timing_network_security_gateway_event_cap_due_missing_contract_retention_margin_bridge", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_network_security_gateway_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_21_R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R9", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_trigger_id": "R9L97_C29_FUTURENURI_2024_STAGE4B_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP", "source_case_id": "R9L97_C29_FUTURENURI_2024_AUTONOMOUS_CAMERA_MODULE_EVENT_CAP_4B", "symbol": "370090", "company_name": "퓨런티어", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "high", "MFE_90D_pct": 6.51, "MAE_90D_pct": -27.28, "MAE_180D_pct": -35.0, "four_b_timing_verdict": "good_full_window_4B_timing_autonomous_camera_module_event_cap", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_autonomous_camera_module_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_22_R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R10", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_97_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_trigger_id": "R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP", "source_case_id": "R10L97_C30_WOOWONDEV_2024_LOCAL_CIVIL_INFRA_EVENT_CAP_4B", "symbol": "046940", "company_name": "우원개발", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "very_high", "MFE_90D_pct": 0.14, "MAE_90D_pct": -22.6, "MAE_180D_pct": -22.6, "four_b_timing_verdict": "good_full_window_4B_timing_local_civil_infra_event_cap", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_local_civil_infra_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_23_R11L97_C03_HANILFORGING_2024_STAGE4B_MUNITION_ARTILLERY_EXPORT_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R11", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_trigger_id": "R11L97_C03_HANILFORGING_2024_STAGE4B_MUNITION_ARTILLERY_EXPORT_EVENT_CAP", "source_case_id": "R11L97_C03_HANILFORGING_2024_MUNITION_ARTILLERY_EVENT_CAP_4B", "symbol": "024740", "company_name": "한일단조", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "high", "MFE_90D_pct": 7.08, "MAE_90D_pct": -17.79, "MAE_180D_pct": -23.23, "four_b_timing_verdict": "good_full_window_4B_timing_munition_artillery_export_event_cap", "four_c_protection_label": "thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_munition_artillery_export_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "redteam_review", "review_id": "R13L97_REVIEW_24_R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP", "round": "R13", "loop": "97", "source_round": "R12", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_trigger_id": "R12L97_C31_GALAXIAMONEYTREE_2024_STAGE4B_STO_DIGITAL_ASSET_LEGISLATION_EVENT_CAP", "source_case_id": "R12L97_C31_GALAXIAMONEYTREE_2024_STO_DIGITAL_ASSET_EVENT_CAP_4B", "symbol": "094480", "company_name": "갤럭시아머니트리", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_trigger_type": "Stage4B", "review_role": "event_cap_review", "review_severity": "very_high", "MFE_90D_pct": 2.92, "MAE_90D_pct": -47.75, "MAE_180D_pct": -54.0, "four_b_timing_verdict": "good_full_window_4B_timing_STO_digital_asset_legislation_event_cap", "four_c_protection_label": "legislation_thesis_break_watch_only", "current_profile_verdict": "current_profile_4B_too_late_if_STO_digital_asset_legislation_event_premium_not_capped", "redteam_verdict": "keep_as_negative_or_4B_guardrail; do_not_promote_positive_stage", "axis_reviewed": ["stage2_required_bridge", "local_4b_watch_guard", "high_MAE_guardrail", "price_only_blowoff_blocks_positive_stage"], "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13_cross_archetype_review_only_reuses_loop97_source_rows", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "source_proxy_only": true, "evidence_url_pending": true}
```

### 15.3 positive_contrast_review rows

```jsonl
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_01_R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE", "round": "R13", "loop": "97", "source_round": "R1", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "source_trigger_id": "R1L97_C05_SNTENERGY_2024_STAGE2_ACTIONABLE_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_BRIDGE", "source_case_id": "R1L97_C05_SNTENERGY_2024_HEAT_EXCHANGER_PLANT_EPC_ORDER_MARGIN_POSITIVE", "symbol": "100840", "company_name": "SNT에너지", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "MFE_90D_pct": 60.2, "MAE_90D_pct": -4.28, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "order_quality_delivery_cost_to_complete_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_02_R2L97_C06_PSKHOLDINGS_2024_STAGE2_ACTIONABLE_HBM_PACKAGING_CAPACITY_CUSTOMER_BRIDGE", "round": "R13", "loop": "97", "source_round": "R2", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "source_trigger_id": "R2L97_C06_PSKHOLDINGS_2024_STAGE2_ACTIONABLE_HBM_PACKAGING_CAPACITY_CUSTOMER_BRIDGE", "source_case_id": "R2L97_C06_PSKHOLDINGS_2024_HBM_PACKAGING_CAPACITY_CUSTOMER_BRIDGE_POSITIVE", "symbol": "031980", "company_name": "피에스케이홀딩스", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "MFE_90D_pct": 167.3, "MAE_90D_pct": -4.31, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "customer_capacity_order_utilization_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_03_R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE", "round": "R13", "loop": "97", "source_round": "R3", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_trigger_id": "R3L97_C12_SKC_2024_STAGE2_ACTIONABLE_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE", "source_case_id": "R3L97_C12_SKC_2024_COPPER_FOIL_CUSTOMER_CONTRACT_BRIDGE_POSITIVE", "symbol": "011790", "company_name": "SKC", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "MFE_90D_pct": 146.61, "MAE_90D_pct": -3.45, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "customer_quality_calloff_delivery_utilization_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_04_R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE", "round": "R13", "loop": "97", "source_round": "R4", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_97_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_trigger_id": "R4L97_C17_PKC_2024_STAGE2_ACTIONABLE_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE", "source_case_id": "R4L97_C17_PKC_2024_CHLORALKALI_SEMICON_CHEMICAL_MARGIN_BRIDGE_POSITIVE", "symbol": "001340", "company_name": "백광산업", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "MFE_90D_pct": 131.37, "MAE_90D_pct": -10.04, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "realized_spread_capacity_customer_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_05_R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE", "round": "R13", "loop": "97", "source_round": "R5", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_97_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_trigger_id": "R5L97_C19_LOTTESHOPPING_2024_STAGE2_ACTIONABLE_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_BRIDGE", "source_case_id": "R5L97_C19_LOTTESHOPPING_2024_DEPARTMENT_STORE_RETAIL_INVENTORY_MARGIN_POSITIVE", "symbol": "023530", "company_name": "롯데쇼핑", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "MFE_90D_pct": 28.27, "MAE_90D_pct": -11.0, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "inventory_turn_category_mix_traffic_markdown_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_06_R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE", "round": "R13", "loop": "97", "source_round": "R6", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_97_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_trigger_id": "R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE", "source_case_id": "R6L97_C22_SAMSUNGLIFE_2024_LIFE_CSM_RESERVE_VALUEUP_BRIDGE_POSITIVE", "symbol": "032830", "company_name": "삼성생명", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "MFE_90D_pct": 70.06, "MAE_90D_pct": -2.35, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "CSM_reserve_capital_buffer_return_policy_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_07_R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE", "round": "R13", "loop": "97", "source_round": "R7", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_97_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_trigger_id": "R7L97_C25_VIOL_2024_STAGE2_ACTIONABLE_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_BRIDGE", "source_case_id": "R7L97_C25_VIOL_2024_AESTHETIC_DEVICE_EXPORT_CONSUMABLE_MARGIN_POSITIVE", "symbol": "335890", "company_name": "비올", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "MFE_90D_pct": 23.08, "MAE_90D_pct": -12.01, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "installed_base_consumable_distributor_regulatory_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_08_R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE", "round": "R13", "loop": "97", "source_round": "R8", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_trigger_id": "R8L97_C28_ESTSOFT_2024_STAGE2_ACTIONABLE_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_BRIDGE", "source_case_id": "R8L97_C28_ESTSOFT_2024_AI_SOFTWARE_LICENSE_CONTRACT_RETENTION_POSITIVE", "symbol": "047560", "company_name": "이스트소프트", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "MFE_90D_pct": 94.15, "MAE_90D_pct": -14.81, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "recurring_license_retention_enterprise_customer_ARR_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_09_R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE", "round": "R13", "loop": "97", "source_round": "R9", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_trigger_id": "R9L97_C29_SNTMOTIVE_2024_STAGE2_ACTIONABLE_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE", "source_case_id": "R9L97_C29_SNTMOTIVE_2024_EV_POWERTRAIN_AUTO_PARTS_MARGIN_BRIDGE_POSITIVE", "symbol": "064960", "company_name": "SNT모티브", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "MFE_90D_pct": 12.43, "MAE_90D_pct": -2.49, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "OEM_volume_powertrain_mix_utilization_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_10_R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE", "round": "R13", "loop": "97", "source_round": "R10", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_97_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_trigger_id": "R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE", "source_case_id": "R10L97_C30_HJSC_2024_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_POSITIVE", "symbol": "097230", "company_name": "HJ중공업", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "MFE_90D_pct": 25.96, "MAE_90D_pct": -10.15, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "order_quality_cashflow_funding_balance_sheet_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_11_R11L97_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_DEFENSE_EXPORT_BACKLOG_DELIVERY_BRIDGE", "round": "R13", "loop": "97", "source_round": "R11", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_trigger_id": "R11L97_C03_STXENGINE_2024_STAGE2_ACTIONABLE_NAVAL_ENGINE_DEFENSE_EXPORT_BACKLOG_DELIVERY_BRIDGE", "source_case_id": "R11L97_C03_STXENGINE_2024_NAVAL_ENGINE_DEFENSE_EXPORT_BACKLOG_DELIVERY_POSITIVE", "symbol": "077970", "company_name": "STX엔진", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "MFE_90D_pct": 49.83, "MAE_90D_pct": -0.85, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "framework_contract_backlog_delivery_prime_customer_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "positive_contrast_review", "review_id": "R13L97_POSITIVE_CONTRAST_12_R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE", "round": "R13", "loop": "97", "source_round": "R12", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_trigger_id": "R12L97_C31_KCS_2024_STAGE2_ACTIONABLE_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE", "source_case_id": "R12L97_C31_KCS_2024_CBDC_DIGITAL_INFRA_POLICY_LEGISLATION_BRIDGE_POSITIVE", "symbol": "115500", "company_name": "케이씨에스", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "MFE_90D_pct": 32.01, "MAE_90D_pct": -12.18, "redteam_use": "contrast_only_positive_bridge_examples; do_not_count_as_new_case", "bridge_quality": "institutional_pilot_procurement_legislation_scope_margin_revision_bridge", "calibration_usable": true, "is_new_independent_case": false, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 15.4 coverage_matrix row

```jsonl
{"row_type": "coverage_matrix", "round": "R13", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "reviewed_loop97_source_files": 12, "reviewed_total_trigger_count": 36, "reviewed_redteam_trigger_count": 24, "positive_contrast_count": 12, "stage2_false_positive_review_count": 12, "event_cap_review_count": 12, "hard_4C_review_count": 0, "high_MAE_review_count": 21, "low_MFE90_review_count": 19, "new_independent_case_count": 0, "reused_case_count": 24, "do_not_propose_new_weight_delta": true, "coverage_gap_after_this_loop": "R13 loop97 cross-archetype review confirms Stage2 bridge requirements and 4B event-cap guardrails across all R1~R12 loop97 source files; no new cases are counted."}
```

### 15.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "97", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP97_FALSE_STAGE2_4B_HIGH_MAE_GUARDRAIL_REVIEW", "new_independent_case_count": 0, "reused_case_count": 24, "new_symbol_count": 0, "same_archetype_new_symbol_count": 0, "same_archetype_new_trigger_family_count": 0, "positive_case_count": 0, "counterexample_count": 24, "4B_case_count": 12, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["bridge_missing_false_stage2", "event_cap_4B", "high_MAE_after_bridge_missing_entry", "low_MFE_after_policy_or_theme_label_only"], "loop_contribution_label": "axis_stress_test_passed", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 24, "evidence_url_pending_count": 24}
```

### 15.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","reason":"R13 loop97 is a cross-archetype red-team review. No new independent cases are created; all rows are review-only reuses of loop97 R1~R12 outputs.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 16. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

This R13 file is a review-only cross-archetype red-team audit. It does not add new independent cases. Use it to strengthen tests and guardrails around bridge-missing Stage2 false positives and 4B event caps.

### Rules

- Do not count any R13 redteam_review row as new independent evidence.
- Every R13 review row has `do_not_count_as_new_case=true` and `independent_evidence_weight=0.0`.
- Preserve production scoring unless explicitly promoted in a separate batch.
- Use R13 to test that bridge-missing rows remain Watch/4B rather than Stage2/Stage3.
- Keep hard 4C unchanged because loop97 did not include confirmed hard 4C thesis-break rows.
- Do not create live candidates from this file.
- Do not make investment recommendations.

### Expected repository tasks

1. Parse redteam_review / positive_contrast_review / coverage_matrix / residual_contribution rows.
2. Verify that all R13 rows are review-only and not counted as new cases.
3. Add or strengthen tests for Stage2 bridge requirements across C03, C05, C06, C12, C17, C19, C22, C25, C28, C29, C30, C31.
4. Add or strengthen tests for 4B event-cap overlay behavior.
5. Report high-MAE and low-MFE failure clusters.
6. Preserve global calibrated profile unless explicitly promoted.

### Expected output

- Concise implementation summary.
- Rows accepted as review-only.
- Rows rejected from independent evidence counts.
- Existing axes strengthened/kept.
- No investment recommendation language.

## 17. Next Round State

```text
completed_round = R13
completed_loop = 97
next_round = R1
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

## 18. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Source files: loop97 R1~R12 local Markdown artifacts in /mnt/data.
- This file contains no investment recommendation and no production scoring change.
