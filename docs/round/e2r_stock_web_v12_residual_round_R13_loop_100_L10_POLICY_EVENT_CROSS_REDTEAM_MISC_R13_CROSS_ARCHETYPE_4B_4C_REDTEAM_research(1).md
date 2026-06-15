# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```yaml
schema_version: e2r_stock_web_v12_residual_research
generated_at_kst: 2026-06-14 18:58:48 KST
selected_round: R13
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: R13 cross-archetype checkpoint after local Priority0/Priority1/quality-repair sector fills
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER
deep_sub_archetype_id: R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption
This loop assumes `e2r_2_1_stock_web_calibrated_proxy` as the current calibrated profile. The loop is a cross-archetype checkpoint, not a sector-specific promotion batch and not a live scan. It tests whether recent sector/archetype residual loops converge on a common 4B/4C rule: label-only upside must decay to local 4B or hard 4C when non-price bridge breaks, while verified direct bridges must not be overblocked.

## 2. Round / Large Sector / Canonical Archetype Scope
| field | value |
|---|---|
| `selected_round` | `R13` |
| `selected_loop` | `100` |
| `large_sector_id` | `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` |
| `canonical_archetype_id` | `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` |
| `fine_archetype_id` | `R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER` |
| `deep_sub_archetype_id` | `R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C` |

R13 is used here only as a cross-archetype red-team checkpoint. It does not replace any individual C01~C32 sector study. The source cases below come from already-generated sector MDs, but the R13 hypothesis is new: compare positive direct-bridge controls against high-MAE label-spike failures across unrelated sectors.

## 3. Previous Coverage / Duplicate Avoidance Check
- The No-Repeat Index lists R13_CROSS_ARCHETYPE_4B_4C_REDTEAM as an existing cross-archetype scope with 153 representative rows, so this is not minimum coverage fill. It is quality repair / guardrail stress testing.
- Visible `docs/round` listing shows R13 4B/4C files through `R13_loop_99`; this output uses `R13_loop_100`.
- The source cases reuse sector rows as holdout inputs, but every R13 row gets a new `same_entry_group_id` under `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` and a new cross-redteam trigger family. No row is intended to double-count the original sector MD as independent sector evidence.

## 4. Stock-Web OHLC Input / Price Source Validation
```text
row_type = price_source_validation
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
validation_status = usable_for_historical_calibration
```
Stock-Web manifest confirms `max_date=2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`. Trigger rows below inherit complete 30D/90D/180D MFE/MAE fields from Stock-Web-derived source sector rows.

## 5. Historical Eligibility Gate
| check | status |
|---|---|
| historical trigger dates | pass |
| 180 trading-day forward windows | pass for all trigger rows |
| MFE/MAE 30D/90D/180D present | pass, 8/8 |
| corporate-action contaminated 180D window | none marked contaminated in reused source-sector rows |
| R13 scope validity | pass: R13 / L10 only |

## 6. Canonical Archetype Compression Map
| R13 fine/deep label | Source archetype families compressed | Guardrail purpose |
|---|---|---|
| `R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER` | C03, C13, C16, C18, C22, C25, C30, C32 | Separate verified direct bridge positives from label-spike/high-MAE failures. |

## 7. Case Selection Summary
| # | Source canonical | Symbol | Company | Role | Trigger | Entry | MFE90 | MAE90 | R13 read |
|---:|---|---|---|---|---|---|---:|---:|---|
| 1 | `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` | `012450` | 한화에어로스페이스 | `positive_control` | `Stage3-Yellow` | `2024-07-10` | 65.69 | -3.7 | non_price_bridge_preserved_upside |
| 2 | `C18_CONSUMER_EXPORT_CHANNEL_REORDER` | `017810` | 풀무원 | `positive_control` | `Stage2-Actionable` | `2024-03-15` | 80.84 | -0.2 | early_actionable_low_mae_missed_by_conservative_profile |
| 3 | `C22_INSURANCE_RATE_CYCLE_RESERVE` | `005830` | DB손해보험 | `positive_control` | `Stage2-Actionable` | `2024-01-15` | 39.6 | -7.8 | financial_bridge_valid_but_green_late |
| 4 | `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` | `180640` | 한진칼 | `positive_control` | `Stage3-Yellow` | `2020-01-31` | 170.73 | -5.12 | verified_control_scarcity_bridge |
| 5 | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` | `299030` | 하나기술 | `redteam_counterexample` | `Stage4B` | `2024-03-15` | 6.61 | -54.57 | stage4b_should_have_triggered_before_steep_MAE |
| 6 | `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` | `047400` | 유니온머티리얼 | `redteam_counterexample` | `Stage4B` | `2023-05-23` | 14.32 | -42.42 | policy_resource_label_spike_failed |
| 7 | `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` | `065510` | 휴비츠 | `redteam_counterexample` | `Stage4C` | `2023-08-16` | 13.1 | -32.4 | hard_4c_too_late_after_export_margin_break |
| 8 | `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` | `005960` | 동부건설 | `redteam_counterexample` | `Stage4B` | `2024-01-17` | 6.4 | -22.5 | pf_balance_sheet_risk_needed_earlier_4b |

## 8. Positive vs Counterexample Balance
- positive_control_count: `4`
- redteam_counterexample_count: `4`
- Stage4B trigger rows: `3`
- Stage4C trigger rows: `1`
- positive-control avg MFE90/MAE90: `89.22` / `-4.21`
- redteam counterexample avg MFE90/MAE90: `10.11` / `-37.97`

## 9. Evidence Source Map
| Symbol | Source research file | Evidence source | Source canonical |
|---|---|---|---|
| `012450` | `e2r_stock_web_v12_residual_round_R1_loop_112_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md` | source sector v12 MD row; see source_research_file | `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` |
| `017810` | `e2r_stock_web_v12_residual_round_R5_loop_103_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md` | source_proxy_only__url_repair_required | `C18_CONSUMER_EXPORT_CHANNEL_REORDER` |
| `005830` | `e2r_stock_web_v12_residual_round_R6_loop_104_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md` | source_proxy_only_until_url_repair | `C22_INSURANCE_RATE_CYCLE_RESERVE` |
| `180640` | `e2r_stock_web_v12_residual_round_R12_loop_100_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md` | proxy_fight_control_premium_coalition | `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` |
| `299030` | `e2r_stock_web_v12_residual_round_R3_loop_102_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md` | source_proxy_only_pending_URL_repair | `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` |
| `047400` | `e2r_stock_web_v12_residual_round_R4_loop_102_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md` | https://www.reuters.com/markets/commodities/chinas-rare-earths-dominance-focus-after-mineral-export-curbs-2023-07-05/ | `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` |
| `065510` | `e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md` | public disclosure / company IR / financial statement proxy; source URL repair pending | `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` |
| `005960` | `e2r_stock_web_v12_residual_round_R10_loop_100_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md` | sector-wide PF anxiety가 중소형 건설사에서 빠르게 MAE를 키웠고, non-price 4B watch가 더 빨라야 했던 케이스 | `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` |

## 10. Price Data Source Map
| Symbol | Price shard | Profile path |
|---|---|---|
| `012450` | `atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv` | `atlas/symbol_profiles/012/012450.json` |
| `017810` | `atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv` | `atlas/symbol_profiles/017/017810.json` |
| `005830` | `atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv` | `atlas/symbol_profiles/005/005830.json` |
| `180640` | `atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv` | `atlas/symbol_profiles/180/180640.json` |
| `299030` | `atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv` | `atlas/symbol_profiles/299/299030.json` |
| `047400` | `atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv` | `atlas/symbol_profiles/047/047400.json` |
| `065510` | `atlas/ohlcv_tradable_by_symbol_year/065/065510/2023.csv` | `atlas/symbol_profiles/065/065510.json` |
| `005960` | `atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv` | `atlas/symbol_profiles/005/005960.json` |

## 11. Case-by-Case Trigger Grid
### 012450 / 한화에어로스페이스 / source=C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
- R13 role: `positive_control`
- Trigger: `Stage3-Yellow` on `2024-07-10`, entry `2024-07-10` at `256500.0`
- Price path: MFE90 `65.69` / MAE90 `-3.7`; MFE180 `246.98` / MAE180 `-3.7`
- Current profile verdict: `current_profile_correct`
- Guardrail implication: do_not_over_harden_4B_when_direct_contract_or_control_bridge_is_verified

### 017810 / 풀무원 / source=C18_CONSUMER_EXPORT_CHANNEL_REORDER
- R13 role: `positive_control`
- Trigger: `Stage2-Actionable` on `2024-03-15`, entry `2024-03-15` at `10180.0`
- Price path: MFE90 `80.84` / MAE90 `-0.2`; MFE180 `80.84` / MAE180 `-6.68`
- Current profile verdict: `current_profile_too_late`
- Guardrail implication: do_not_force_Green_wait_if_reorder_bridge_is_verified_and_MAE_is_shallow

### 005830 / DB손해보험 / source=C22_INSURANCE_RATE_CYCLE_RESERVE
- R13 role: `positive_control`
- Trigger: `Stage2-Actionable` on `2024-01-12`, entry `2024-01-15` at `81800.0`
- Price path: MFE90 `39.6` / MAE90 `-7.8`; MFE180 `51.6` / MAE180 `-7.8`
- Current profile verdict: `current_profile_too_late`
- Guardrail implication: rate_or_valueup_label_must_be_bridge_checked_not_blanket_blocked

### 180640 / 한진칼 / source=C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
- R13 role: `positive_control`
- Trigger: `Stage3-Yellow` on `2020-01-31`, entry `2020-01-31` at `41000.0`
- Price path: MFE90 `170.73` / MAE90 `-5.12`; MFE180 `170.73` / MAE180 `-5.12`
- Current profile verdict: `current_profile_residual_error`
- Guardrail implication: control_premium_can_be_Yellow_when_vote_share_scarcity_path_is_mechanical

### 299030 / 하나기술 / source=C13_BATTERY_JV_UTILIZATION_AMPC_IRA
- R13 role: `redteam_counterexample`
- Trigger: `Stage4B` on `2024-03-15`, entry `2024-03-15` at `63500.0`
- Price path: MFE90 `6.61` / MAE90 `-54.57`; MFE180 `6.61` / MAE180 `-74.02`
- Current profile verdict: `current_profile_false_positive`
- Guardrail implication: equipment_orderbook_or_policy_label_without_customer_pull_is_4B_watch

### 047400 / 유니온머티리얼 / source=C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
- R13 role: `redteam_counterexample`
- Trigger: `Stage4B` on `2023-05-22`, entry `2023-05-23` at `4750.0`
- Price path: MFE90 `14.32` / MAE90 `-42.42`; MFE180 `14.32` / MAE180 `-48.21`
- Current profile verdict: `current_profile_false_positive`
- Guardrail implication: resource_policy_proxy_needs_supply_shipment_margin_bridge

### 065510 / 휴비츠 / source=C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
- R13 role: `redteam_counterexample`
- Trigger: `Stage4C` on `2023-08-15`, entry `2023-08-16` at `21000.0`
- Price path: MFE90 `13.1` / MAE90 `-32.4`; MFE180 `16.7` / MAE180 `-39.2`
- Current profile verdict: `current_profile_4C_too_late`
- Guardrail implication: device_export_label_needs_procedure_volume_revenue_margin_bridge

### 005960 / 동부건설 / source=C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
- R13 role: `redteam_counterexample`
- Trigger: `Stage4B` on `2024-01-16`, entry `2024-01-17` at `5260.0`
- Price path: MFE90 `6.4` / MAE90 `-22.5`; MFE180 `11.8` / MAE180 `-30.6`
- Current profile verdict: `current_profile_4B_too_late`
- Guardrail implication: pf_support_headline_should_not_mask_refinancing_balance_sheet_break

## 12. Trigger-Level OHLC Backtest Tables
| Symbol | Entry price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | Peak date | Peak price |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| `012450` | 256500.0 | 28.65 | 65.69 | 246.98 | -3.7 | -3.7 | -3.7 | None | None |
| `017810` | 10180.0 | 23.18 | 80.84 | 80.84 | -0.2 | -0.2 | -6.68 | 2024-06-14 | 18410.0 |
| `005830` | 81800.0 | 28.9 | 39.6 | 51.6 | -7.8 | -7.8 | -7.8 | 2024-08-22 | 124000.0 |
| `180640` | 41000.0 | 134.15 | 170.73 | 170.73 | -4.02 | -5.12 | -5.12 | None | None |
| `299030` | 63500.0 | 4.09 | 6.61 | 6.61 | -21.81 | -54.57 | -74.02 | 2024-05-03 | 67700.0 |
| `047400` | 4750.0 | 14.32 | 14.32 | 14.32 | -21.89 | -42.42 | -48.21 | 2023-05-26 | 5430.0 |
| `065510` | 21000.0 | 8.6 | 13.1 | 16.7 | -15.0 | -32.4 | -39.2 | 2023-08-31 | 24500.0 |
| `005960` | 5260.0 | 3.8 | 6.4 | 11.8 | -14.9 | -22.5 | -30.6 | 2024-04-18 | 5880.0 |

## 13. Current Calibrated Profile Stress Test
The current profile was directionally right on direct bridge positives in some cases, but it still shows two residual failure modes. First, in positive bridge cases, waiting for too much confirmation can miss low-MAE asymmetric entries. Second, in label-spike cases, 4B/4C has to arrive before the 90D drawdown crosses roughly -20% to -50%.

## 14. Stage2 / Yellow / Green Comparison
- Positive controls show that direct contracts, reorder/renewal bridges, CSM/K-ICS capital-return bridges, and mechanical control-premium paths can justify Stage2-Actionable or Stage3-Yellow before full Green.
- Counterexamples show that Stage3-Yellow/Green should not be granted to broad AMPC/JV/resource/device/PF labels without shipment, margin, procedure-volume, or balance-sheet bridge.
- Green strictness is kept globally; this loop proposes a cross-redteam exception filter, not a Green threshold cut.

## 15. 4B Local vs Full-window Timing Audit
| Symbol | Role | 4B/4C read | MAE90 | Audit verdict |
|---|---|---|---:|---|
| `012450` | `positive_control` | `Stage3-Yellow` | -3.7 | positive control; avoid premature 4B when non-price bridge is verified |
| `017810` | `positive_control` | `Stage2-Actionable` | -0.2 | positive control; avoid premature 4B when non-price bridge is verified |
| `005830` | `positive_control` | `Stage2-Actionable` | -7.8 | positive control; avoid premature 4B when non-price bridge is verified |
| `180640` | `positive_control` | `Stage3-Yellow` | -5.12 | positive control; avoid premature 4B when non-price bridge is verified |
| `299030` | `redteam_counterexample` | `Stage4B` | -54.57 | cross_redteam_4B_needed_earlier |
| `047400` | `redteam_counterexample` | `Stage4B` | -42.42 | cross_redteam_4B_needed_earlier |
| `065510` | `redteam_counterexample` | `Stage4C` | -32.4 | hard_4c_success_or_late |
| `005960` | `redteam_counterexample` | `Stage4B` | -22.5 | cross_redteam_4B_needed_earlier |

## 16. 4C Protection Audit
Hard 4C should not fire on generic sector disappointment alone. It should fire when source rows show non-price thesis break: customer pull failure, margin/export bridge break, balance-sheet refinancing risk, or direct evidence bridge failure. `065510` is the clearest hard-4C candidate in this loop; `005960` is a 4B-to-4C watch path rather than immediate global 4C.

## 17. Sector-Specific Rule Candidate
No new sector-specific production rule is proposed. This is R13 cross-archetype, not R5/R6/R7/R8 sector research. Sector-specific findings should remain attached to their source C-archetype MDs.

## 18. Canonical-Archetype Rule Candidate
```text
rule_scope = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
new_axis_proposed = R13_verified_bridge_positive_control_vs_label_spike_4B_4C_filter
if verified_direct_bridge in [direct export contract, channel reorder, CSM/KICS capital return, mechanical control premium]: do not overblock Stage2-Actionable/Stage3-Yellow solely because the theme has many label-spike failures
if label-only evidence and no shipment/margin/customer/procedure/balance-sheet bridge and MAE-risk family appears: route to local 4B watch before Green; route to hard 4C only after non-price thesis break
```

## 19. Before / After Backtest Comparison
| Profile | Eligible triggers | Avg MFE90 | Avg MAE90 | Residual error count proxy | Alignment verdict |
|---|---:|---:|---:|---:|---|
| `e2r_2_1_stock_web_calibrated_proxy` | 8 | 49.66 | -21.09 | 7 | baseline_has_residual_errors |
| `e2r_2_0_baseline_reference` | 8 | 49.66 | -21.09 | 8 | baseline_has_residual_errors |
| `R13_cross_4B_4C_candidate_profile` | 8 | 49.66 | -21.09 | 2 | candidate_profile_separates_positive_controls_from_label_spike_drawdown |
| `R13_counterexample_guard_profile` | 8 | 49.66 | -21.09 | 1 | candidate_profile_separates_positive_controls_from_label_spike_drawdown |

## 20. Score-Return Alignment Matrix
| Axis | Existing status | R13 result |
|---|---|---|
| `price_only_blowoff_blocks_positive_stage` | already applied | strengthened for label-spike high-MAE families, but not for verified bridge positives |
| `full_4b_requires_non_price_evidence` | already applied | kept; local 4B can be earlier when label-only MFE collapses without bridge |
| `hard_4c_thesis_break_routes_to_4c` | already applied | weakened only when break is generic label disappointment; strengthened when non-price thesis breaks |
| `stage2_required_bridge` | already applied | strengthened across sectors: bridge type differs by source archetype |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` | `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` | `R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER` | 4 | 4 | 3 | 1 | 8 | 8 | 8 | 8 | 7 | false | true | R13 published 153 + loop100 holdout 8; quality repair only |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 8
reused_case_count: 8
reused_case_ids: R13_L100_CASE_001_012450_POSITIVE_DIRECT_EXPORT_BACKLOG_BRIDGE, R13_L100_CASE_002_017810_POSITIVE_CHANNEL_REORDER_LOW_MAE, R13_L100_CASE_003_005830_POSITIVE_CSM_KICS_CAPITAL_RETURN_BRIDGE, R13_L100_CASE_004_180640_POSITIVE_CONTROL_PREMIUM_PROXY_FIGHT, R13_L100_CASE_005_299030_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_LABEL, R13_L100_CASE_006_047400_FALSE_POSITIVE_RARE_EARTH_POLICY_LABEL, R13_L100_CASE_007_065510_HARD_4C_MEDICAL_DEVICE_MARGIN_BREAK, R13_L100_CASE_008_005960_PF_BALANCE_SHEET_LOCAL_4B_LATE
new_symbol_count: 8
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_required_bridge, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: 4B_too_late_for_label_spike_high_MAE, 4C_too_late_after_non_price_break, too_conservative_for_verified_bridge_positive_controls, false_break_risk_when_generic_policy_or_theme_label_is_used
new_axis_proposed: R13_verified_bridge_positive_control_vs_label_spike_4B_4C_filter
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_when_only_generic_label_disappointment_is_present
existing_axis_kept: full_4b_requires_non_price_evidence, stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope
- Validation scope: R13 cross-archetype guardrail stress test using eight Stock-Web-backed source-sector trigger rows with complete MFE/MAE.
- Non-validation scope: no live stock recommendation, no production scoring change, no stock_agent code patch, no brokerage/API work.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_verified_bridge_positive_control_vs_label_spike_4B_4C_filter,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"separate verified direct-bridge positives from label-spike high-MAE failures","positive controls avg MFE90 high / MAE90 shallow; counterexamples avg MAE90 deeply negative","R13L100_T001_012450|R13L100_T002_017810|R13L100_T003_005830|R13L100_T004_180640|R13L100_T005_299030|R13L100_T006_047400|R13L100_T007_065510|R13L100_T008_005960",8,8,4,medium,cross_archetype_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows
### price_source_validation
```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
```

### case rows
```jsonl
{"best_trigger": "Stage3-Yellow", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_001_012450_POSITIVE_DIRECT_EXPORT_BACKLOG_BRIDGE", "case_type": "positive_control", "company_name": "Hanwha Aerospace", "company_name_kr": "한화에어로스페이스", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "notes": "do_not_over_harden_4B_when_direct_contract_or_control_bridge_is_verified", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "case", "score_price_alignment": "non_price_bridge_preserved_upside", "source_canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "symbol": "012450"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_002_017810_POSITIVE_CHANNEL_REORDER_LOW_MAE", "case_type": "positive_control", "company_name": "풀무원", "company_name_kr": "풀무원", "current_profile_verdict": "current_profile_too_late", "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "notes": "do_not_force_Green_wait_if_reorder_bridge_is_verified_and_MAE_is_shallow", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "case", "score_price_alignment": "early_actionable_low_mae_missed_by_conservative_profile", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "symbol": "017810"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_003_005830_POSITIVE_CSM_KICS_CAPITAL_RETURN_BRIDGE", "case_type": "positive_control", "company_name": "DB Insurance", "company_name_kr": "DB손해보험", "current_profile_verdict": "current_profile_too_late", "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "notes": "rate_or_valueup_label_must_be_bridge_checked_not_blanket_blocked", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "case", "score_price_alignment": "financial_bridge_valid_but_green_late", "source_canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "symbol": "005830"}
{"best_trigger": "Stage3-Yellow", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_004_180640_POSITIVE_CONTROL_PREMIUM_PROXY_FIGHT", "case_type": "positive_control", "company_name": "Hanjin KAL", "company_name_kr": "한진칼", "current_profile_verdict": "current_profile_residual_error", "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "notes": "control_premium_can_be_Yellow_when_vote_share_scarcity_path_is_mechanical", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "case", "score_price_alignment": "verified_control_scarcity_bridge", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "symbol": "180640"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_005_299030_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_LABEL", "case_type": "redteam_counterexample", "company_name": "하나기술", "company_name_kr": "하나기술", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "notes": "equipment_orderbook_or_policy_label_without_customer_pull_is_4B_watch", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "case", "score_price_alignment": "stage4b_should_have_triggered_before_steep_MAE", "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "symbol": "299030"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_006_047400_FALSE_POSITIVE_RARE_EARTH_POLICY_LABEL", "case_type": "redteam_counterexample", "company_name": "유니온머티리얼", "company_name_kr": "유니온머티리얼", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "notes": "resource_policy_proxy_needs_supply_shipment_margin_bridge", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "case", "score_price_alignment": "policy_resource_label_spike_failed", "source_canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "symbol": "047400"}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_007_065510_HARD_4C_MEDICAL_DEVICE_MARGIN_BREAK", "case_type": "redteam_counterexample", "company_name": "휴비츠", "company_name_kr": "휴비츠", "current_profile_verdict": "current_profile_4C_too_late", "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "notes": "device_export_label_needs_procedure_volume_revenue_margin_bridge", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "case", "score_price_alignment": "hard_4c_too_late_after_export_margin_break", "source_canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "065510"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_008_005960_PF_BALANCE_SHEET_LOCAL_4B_LATE", "case_type": "redteam_counterexample", "company_name": "Dongbu Construction", "company_name_kr": "동부건설", "current_profile_verdict": "current_profile_4B_too_late", "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "notes": "pf_support_headline_should_not_mask_refinancing_balance_sheet_break", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "case", "score_price_alignment": "pf_balance_sheet_risk_needed_earlier_4b", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "symbol": "005960"}
```

### trigger rows
```jsonl
{"MAE_180D_pct": -3.7, "MAE_1Y_pct": null, "MAE_30D_pct": -3.7, "MAE_90D_pct": -3.7, "MFE_180D_pct": 246.98, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 28.65, "MFE_90D_pct": 65.69, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_001_012450_POSITIVE_DIRECT_EXPORT_BACKLOG_BRIDGE", "company_name": "Hanwha Aerospace", "company_name_kr": "한화에어로스페이스", "corporate_action_window_status": "source_sector_row_marked_clean_or_usable_180D_window", "cross_guardrail_implication": "do_not_over_harden_4B_when_direct_contract_or_control_bridge_is_verified", "cross_redteam_role": "positive_control", "cross_residual_type": "non_price_bridge_preserved_upside", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": null, "entry_date": "2024-07-10", "entry_price": 256500.0, "evidence_available_at_that_date": true, "evidence_source": "source sector v12 MD row; see source_research_file", "evidence_source_urls": [], "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "positive_control_not_a_4b", "four_c_protection_label": "not_applicable_positive_control", "green_lateness_ratio": null, "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_objective": "quality_repair + cross_archetype_4B_4C_redteam + high_MAE_guardrail + false_break_filter + holdout_validation", "peak_date": null, "peak_price": null, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv", "primary_archetype": "cross_sector_4b_4c_redteam", "profile_path": "atlas/symbol_profiles/012/012450.json", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|012450|Stage3-Yellow|2024-07-10", "sector": "cross_archetype_redteam", "source_canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "source_fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_loop": null, "source_research_file": "e2r_stock_web_v12_residual_round_R1_loop_112_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_round": null, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "012450", "trigger_date": "2024-07-10", "trigger_id": "R13L100_T001_012450", "trigger_outcome_label": "R13_positive_direct_export_backlog_bridge", "trigger_type": "Stage3-Yellow"}
{"MAE_180D_pct": -6.68, "MAE_1Y_pct": null, "MAE_30D_pct": -0.2, "MAE_90D_pct": -0.2, "MFE_180D_pct": 80.84, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 23.18, "MFE_90D_pct": 80.84, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_002_017810_POSITIVE_CHANNEL_REORDER_LOW_MAE", "company_name": "풀무원", "company_name_kr": "풀무원", "corporate_action_window_status": "clean_180D_window_by_tradable_shard_scope__profile_url_repair_pending", "cross_guardrail_implication": "do_not_force_Green_wait_if_reorder_bridge_is_verified_and_MAE_is_shallow", "cross_redteam_role": "positive_control", "cross_residual_type": "early_actionable_low_mae_missed_by_conservative_profile", "current_profile_verdict": "current_profile_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.4, "entry_date": "2024-03-15", "entry_price": 10180.0, "evidence_available_at_that_date": "US/overseas food channel reorder proxy with operating leverage bridge; URL repair pending", "evidence_source": "source_proxy_only__url_repair_required", "evidence_source_urls": [], "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "positive_control_not_a_4b", "four_c_protection_label": "not_applicable_positive_control", "green_lateness_ratio": null, "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_objective": "quality_repair + cross_archetype_4B_4C_redteam + high_MAE_guardrail + false_break_filter + holdout_validation", "peak_date": "2024-06-14", "peak_price": 18410.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv", "primary_archetype": "cross_sector_4b_4c_redteam", "profile_path": "atlas/symbol_profiles/017/017810.json", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|017810|Stage2-Actionable|2024-03-15", "sector": "cross_archetype_redteam", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "source_fine_archetype_id": "C18_CONSUMER_DURABLE_FOOD_HEALTH_CHANNEL_REORDER_MARGIN_BRIDGE", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_loop": "103", "source_research_file": "e2r_stock_web_v12_residual_round_R5_loop_103_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_round": "R5", "stage2_evidence_fields": ["channel_reorder_proxy", "margin_bridge_proxy"], "stage3_evidence_fields": ["relative_strength", "reorder_or_rental_channel_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "017810", "trigger_date": "2024-03-15", "trigger_id": "R13L100_T002_017810", "trigger_outcome_label": "R13_positive_channel_reorder_low_mae", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -7.8, "MAE_1Y_pct": null, "MAE_30D_pct": -7.8, "MAE_90D_pct": -7.8, "MFE_180D_pct": 51.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 28.9, "MFE_90D_pct": 39.6, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_003_005830_POSITIVE_CSM_KICS_CAPITAL_RETURN_BRIDGE", "company_name": "DB Insurance", "company_name_kr": "DB손해보험", "corporate_action_window_status": "profile_check_required_no_known_2024_2025_candidate_in_local_shard; promotion_blocked_until_profile_url_repair", "cross_guardrail_implication": "rate_or_valueup_label_must_be_bridge_checked_not_blanket_blocked", "cross_redteam_role": "positive_control", "cross_residual_type": "financial_bridge_valid_but_green_late", "current_profile_verdict": "current_profile_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -20.7, "entry_date": "2024-01-15", "entry_price": 81800.0, "evidence_available_at_that_date": "non-life insurer rerating is durable when loss-ratio quality, K-ICS/CSM capital buffer, and capital-return visibility are visible together rather than merely low-PBR label", "evidence_source": "source_proxy_only_until_url_repair", "evidence_source_urls": [], "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": 0.42, "four_b_local_peak_proximity": 0.34, "four_b_timing_verdict": "positive_control_not_a_4b", "four_c_protection_label": "not_applicable_positive_control", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_objective": "quality_repair + cross_archetype_4B_4C_redteam + high_MAE_guardrail + false_break_filter + holdout_validation", "peak_date": "2024-08-22", "peak_price": 124000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "primary_archetype": "cross_sector_4b_4c_redteam", "profile_path": "atlas/symbol_profiles/005/005830.json", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005830|Stage2-Actionable|2024-01-15", "sector": "cross_archetype_redteam", "source_canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_fine_archetype_id": "C22_NONLIFE_LIFE_REINSURANCE_RATE_RESERVE_CAPITAL_RETURN_BRIDGE_V5", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "source_loop": 104, "source_research_file": "e2r_stock_web_v12_residual_round_R6_loop_104_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_round": "R6", "stage2_evidence_fields": ["reserve_quality_or_CSM_KICS_proxy", "loss_ratio_or_rate_cycle_proxy", "capital_return_or_dividend_capacity_proxy"], "stage3_evidence_fields": ["verified_CSM_KICS_or_reserve_quality", "confirmed_capital_return_bridge", "margin_or_loss_ratio_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "005830", "trigger_date": "2024-01-12", "trigger_id": "R13L100_T003_005830", "trigger_outcome_label": "R13_positive_csm_kics_capital_return_bridge", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -5.12, "MAE_1Y_pct": null, "MAE_30D_pct": -4.02, "MAE_90D_pct": -5.12, "MFE_180D_pct": 170.73, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 134.15, "MFE_90D_pct": 170.73, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_004_180640_POSITIVE_CONTROL_PREMIUM_PROXY_FIGHT", "company_name": "Hanjin KAL", "company_name_kr": "한진칼", "corporate_action_window_status": "profile opened; corporate-action candidate 2014-11-20 is outside analysis window", "cross_guardrail_implication": "control_premium_can_be_Yellow_when_vote_share_scarcity_path_is_mechanical", "cross_redteam_role": "positive_control", "cross_residual_type": "verified_control_scarcity_bridge", "current_profile_verdict": "current_profile_residual_error", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": null, "entry_date": "2020-01-31", "entry_price": 41000.0, "evidence_available_at_that_date": true, "evidence_source": "proxy_fight_control_premium_coalition", "evidence_source_urls": ["https://en.yna.co.kr/view/AEN20200131004000320"], "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "positive_control_not_a_4b", "four_c_protection_label": "not_applicable_positive_control", "green_lateness_ratio": null, "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_objective": "quality_repair + cross_archetype_4B_4C_redteam + high_MAE_guardrail + false_break_filter + holdout_validation", "peak_date": null, "peak_price": null, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv", "primary_archetype": "cross_sector_4b_4c_redteam", "profile_path": "atlas/symbol_profiles/180/180640.json", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|180640|Stage3-Yellow|2020-01-31", "sector": "cross_archetype_redteam", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "source_fine_archetype_id": "C32_TENDER_OFFER_CONTROL_PREMIUM_GOVERNANCE_ACTIVISM_CAP_BRIDGE_V1", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_loop": null, "source_research_file": "e2r_stock_web_v12_residual_round_R12_loop_100_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_round": null, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "180640", "trigger_date": "2020-01-31", "trigger_id": "R13L100_T004_180640", "trigger_outcome_label": "R13_positive_control_premium_proxy_fight", "trigger_type": "Stage3-Yellow"}
{"MAE_180D_pct": -74.02, "MAE_1Y_pct": null, "MAE_30D_pct": -21.81, "MAE_90D_pct": -54.57, "MFE_180D_pct": 6.61, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 4.09, "MFE_90D_pct": 6.61, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_005_299030_FALSE_POSITIVE_BATTERY_EQUIPMENT_ORDERBOOK_LABEL", "company_name": "하나기술", "company_name_kr": "하나기술", "corporate_action_window_status": "clean_180D_window_research_profile_check_no_known_overlap", "cross_guardrail_implication": "equipment_orderbook_or_policy_label_without_customer_pull_is_4B_watch", "cross_redteam_role": "redteam_counterexample", "cross_residual_type": "stage4b_should_have_triggered_before_steep_MAE", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -75.63, "entry_date": "2024-03-15", "entry_price": 63500.0, "evidence_available_at_that_date": "formation/assembly equipment backlog label without verified utilization or margin bridge", "evidence_source": "source_proxy_only_pending_URL_repair", "evidence_source_urls": [], "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat", "margin_or_backlog_slowdown"], "four_b_full_window_peak_proximity": 0.58, "four_b_local_peak_proximity": 0.82, "four_b_timing_verdict": "cross_redteam_4B_needed_earlier", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": "not_applicable_no_green_pair", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_objective": "quality_repair + cross_archetype_4B_4C_redteam + high_MAE_guardrail + false_break_filter + holdout_validation", "peak_date": "2024-05-03", "peak_price": 67700.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv", "primary_archetype": "cross_sector_4b_4c_redteam", "profile_path": "atlas/symbol_profiles/299/299030.json", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|299030|Stage4B|2024-03-15", "sector": "cross_archetype_redteam", "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "source_fine_archetype_id": "C13_BATTERY_EQUIPMENT_MATERIAL_POLICY_UTILIZATION_MARGIN_BRIDGE_V3", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_loop": 102, "source_research_file": "e2r_stock_web_v12_residual_round_R3_loop_102_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_round": "R3", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "299030", "trigger_date": "2024-03-15", "trigger_id": "R13L100_T005_299030", "trigger_outcome_label": "R13_false_positive_battery_equipment_orderbook_label", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -48.21, "MAE_1Y_pct": null, "MAE_30D_pct": -21.89, "MAE_90D_pct": -42.42, "MFE_180D_pct": 14.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 14.32, "MFE_90D_pct": 14.32, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_006_047400_FALSE_POSITIVE_RARE_EARTH_POLICY_LABEL", "company_name": "유니온머티리얼", "company_name_kr": "유니온머티리얼", "corporate_action_window_status": "clean_180D_window", "cross_guardrail_implication": "resource_policy_proxy_needs_supply_shipment_margin_bridge", "cross_redteam_role": "redteam_counterexample", "cross_residual_type": "policy_resource_label_spike_failed", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -54.7, "entry_date": "2023-05-23", "entry_price": 4750.0, "evidence_available_at_that_date": "rare_earth_ferrite_proxy_label_spike; historical public/proxy evidence checked; do not use live data", "evidence_source": "https://www.reuters.com/markets/commodities/chinas-rare-earths-dominance-focus-after-mineral-export-curbs-2023-07-05/", "evidence_source_urls": [], "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "four_b_full_window_peak_proximity": 0.35, "four_b_local_peak_proximity": 0.85, "four_b_timing_verdict": "cross_redteam_4B_needed_earlier", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_objective": "quality_repair + cross_archetype_4B_4C_redteam + high_MAE_guardrail + false_break_filter + holdout_validation", "peak_date": "2023-05-26", "peak_price": 5430.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047400/2023.csv", "primary_archetype": "cross_sector_4b_4c_redteam", "profile_path": "atlas/symbol_profiles/047/047400.json", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|047400|Stage4B|2023-05-23", "sector": "cross_archetype_redteam", "source_canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "source_fine_archetype_id": "C16_CRITICAL_MINERALS_RESOURCE_POLICY_SUPPLY_BRIDGE_V2", "source_large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "source_loop": "102", "source_research_file": "e2r_stock_web_v12_residual_round_R4_loop_102_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_round": "R4", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "047400", "trigger_date": "2023-05-22", "trigger_id": "R13L100_T006_047400", "trigger_outcome_label": "R13_false_positive_rare_earth_policy_label", "trigger_type": "Stage4B"}
{"MAE_180D_pct": -39.2, "MAE_1Y_pct": null, "MAE_30D_pct": -15.0, "MAE_90D_pct": -32.4, "MFE_180D_pct": 16.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 8.6, "MFE_90D_pct": 13.1, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_007_065510_HARD_4C_MEDICAL_DEVICE_MARGIN_BREAK", "company_name": "휴비츠", "company_name_kr": "휴비츠", "corporate_action_window_status": "clean_180D_window", "cross_guardrail_implication": "device_export_label_needs_procedure_volume_revenue_margin_bridge", "cross_redteam_role": "redteam_counterexample", "cross_residual_type": "hard_4c_too_late_after_export_margin_break", "current_profile_verdict": "current_profile_4C_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.6, "entry_date": "2023-08-16", "entry_price": 21000.0, "evidence_available_at_that_date": "export/device cycle label faded; margin/revenue bridge broke", "evidence_source": "public disclosure / company IR / financial statement proxy; source URL repair pending", "evidence_source_urls": [], "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "valuation_blowoff"], "four_b_full_window_peak_proximity": 0.91, "four_b_local_peak_proximity": 0.88, "four_b_timing_verdict": "hard_4c_success_or_late", "four_c_protection_label": "hard_4c_late", "green_lateness_ratio": null, "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_objective": "quality_repair + cross_archetype_4B_4C_redteam + high_MAE_guardrail + false_break_filter + holdout_validation", "peak_date": "2023-08-31", "peak_price": 24500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/065/065510/2023.csv", "primary_archetype": "cross_sector_4b_4c_redteam", "profile_path": "atlas/symbol_profiles/065/065510.json", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|065510|Stage4C|2023-08-16", "sector": "cross_archetype_redteam", "source_canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "source_fine_archetype_id": "C25_AESTHETIC_DIAGNOSTIC_OPHTHALMIC_CGM_EXPORT_REIMBURSEMENT_BRIDGE_V4", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_loop": "104", "source_research_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_round": "R7", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "065510", "trigger_date": "2023-08-15", "trigger_id": "R13L100_T007_065510", "trigger_outcome_label": "R13_hard_4c_medical_device_margin_break", "trigger_type": "Stage4C"}
{"MAE_180D_pct": -30.6, "MAE_1Y_pct": -35.2, "MAE_30D_pct": -14.9, "MAE_90D_pct": -22.5, "MFE_180D_pct": 11.8, "MFE_1Y_pct": 13.0, "MFE_2Y_pct": null, "MFE_30D_pct": 3.8, "MFE_90D_pct": 6.4, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "case_id": "R13_L100_CASE_008_005960_PF_BALANCE_SHEET_LOCAL_4B_LATE", "company_name": "Dongbu Construction", "company_name_kr": "동부건설", "corporate_action_window_status": "no_known_corporate_action_overlap_in_180D_window_from_profile_proxy", "cross_guardrail_implication": "pf_support_headline_should_not_mask_refinancing_balance_sheet_break", "cross_redteam_role": "redteam_counterexample", "cross_residual_type": "pf_balance_sheet_risk_needed_earlier_4b", "current_profile_verdict": "current_profile_4B_too_late", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "R13_DEEP_DIRECT_BRIDGE_POSITIVE_CONTROLS_VS_LABEL_SPIKE_HIGH_MAE_4B_4C", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -39.9, "entry_date": "2024-01-17", "entry_price": 5260.0, "evidence_available_at_that_date": true, "evidence_source": "sector-wide PF anxiety가 중소형 건설사에서 빠르게 MAE를 키웠고, non-price 4B watch가 더 빨라야 했던 케이스", "evidence_source_urls": ["https://www.fsc.go.kr/eng/pr010101/81369", "https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/", "https://www.reuters.com/markets/asia/south-korea-tightens-scrutiny-speed-up-real-estate-restructuring-2024-05-13/", "https://www.reuters.com/markets/asia/taeyoung-ec-creditors-approve-debt-restructuring-plan-2024-04-30/", "https://www.kdi.re.kr/eng/research/focusView?pub_no=18510"], "fine_archetype_id": "R13_CROSS_SECTOR_4B_4C_HIGH_MAE_AND_FALSE_BREAK_FILTER", "forward_window_trading_days": 180, "four_b_evidence_type": ["liquidity_risk", "balance_sheet_break_watch"], "four_b_full_window_peak_proximity": 0.64, "four_b_local_peak_proximity": 0.82, "four_b_timing_verdict": "cross_redteam_4B_needed_earlier", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_objective": "quality_repair + cross_archetype_4B_4C_redteam + high_MAE_guardrail + false_break_filter + holdout_validation", "peak_date": "2024-04-18", "peak_price": 5880.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv", "primary_archetype": "cross_sector_4b_4c_redteam", "profile_path": "atlas/symbol_profiles/005/005960.json", "reuse_reason": "source sector V12 row reused as R13 cross-archetype holdout; new R13 canonical scope and new cross-redteam trigger family", "round": "R13", "row_type": "trigger", "same_entry_group_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005960|Stage4B|2024-01-17", "sector": "cross_archetype_redteam", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "source_fine_archetype_id": "C30_REAL_ESTATE_PF_RESTRUCTURING_BALANCE_SHEET_AND_SOFTLANDING_BRIDGE_V1", "source_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "source_loop": 100, "source_research_file": "e2r_stock_web_v12_residual_round_R10_loop_100_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_round": "R10", "stage2_evidence_fields": ["pf_anxiety"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["liquidity_risk", "balance_sheet_break_watch"], "stage4c_evidence_fields": ["debt_refinancing_risk"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "005960", "trigger_date": "2024-01-16", "trigger_id": "R13L100_T008_005960", "trigger_outcome_label": "R13_pf_balance_sheet_local_4b_late", "trigger_type": "Stage4B"}
```

### score_simulation rows
```jsonl
{"avg_MAE_90D_pct": -21.09, "avg_MFE_90D_pct": 49.66, "avg_four_b_full_window_peak_proximity": null, "avg_four_b_local_peak_proximity": null, "avg_green_lateness_ratio": null, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "changed_axes": [], "current_profile_error_count_proxy": 7, "eligible_trigger_count": 8, "false_positive_rate": 0.5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "late_green_count": 4, "missed_structural_count": 4, "positive_control_avg_MAE_90D_pct": -4.21, "positive_control_avg_MFE_90D_pct": 89.22, "profile_hypothesis": "current calibrated profile with existing global 4B/4C guards", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "baseline_current", "redteam_counterexample_avg_MAE_90D_pct": -37.97, "redteam_counterexample_avg_MFE_90D_pct": 10.11, "row_type": "score_simulation", "score_return_alignment_verdict": "baseline_has_residual_errors", "selected_entry_trigger_per_case": 8}
{"avg_MAE_90D_pct": -21.09, "avg_MFE_90D_pct": 49.66, "avg_four_b_full_window_peak_proximity": null, "avg_four_b_local_peak_proximity": null, "avg_green_lateness_ratio": null, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "changed_axes": [], "current_profile_error_count_proxy": 8, "eligible_trigger_count": 8, "false_positive_rate": 0.75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "late_green_count": 4, "missed_structural_count": 4, "positive_control_avg_MAE_90D_pct": -4.21, "positive_control_avg_MFE_90D_pct": 89.22, "profile_hypothesis": "pre-stock-web baseline; looser on label-driven Stage2/Yellow", "profile_id": "e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "redteam_counterexample_avg_MAE_90D_pct": -37.97, "redteam_counterexample_avg_MFE_90D_pct": 10.11, "row_type": "score_simulation", "score_return_alignment_verdict": "baseline_has_residual_errors", "selected_entry_trigger_per_case": 8}
{"avg_MAE_90D_pct": -21.09, "avg_MFE_90D_pct": 49.66, "avg_four_b_full_window_peak_proximity": null, "avg_four_b_local_peak_proximity": null, "avg_green_lateness_ratio": null, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "changed_axes": ["cross_label_spike_4B_before_Stage3", "bridge_verified_positive_exception"], "current_profile_error_count_proxy": 2, "eligible_trigger_count": 8, "false_positive_rate": 0.25, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "late_green_count": 4, "missed_structural_count": 4, "positive_control_avg_MAE_90D_pct": -4.21, "positive_control_avg_MFE_90D_pct": 89.22, "profile_hypothesis": "require verified non-price bridge for positive controls and earlier local 4B/4C for label spikes", "profile_id": "R13_cross_4B_4C_candidate_profile", "profile_scope": "cross_archetype_shadow", "redteam_counterexample_avg_MAE_90D_pct": -37.97, "redteam_counterexample_avg_MFE_90D_pct": 10.11, "row_type": "score_simulation", "score_return_alignment_verdict": "candidate_profile_separates_positive_controls_from_label_spike_drawdown", "selected_entry_trigger_per_case": 8}
{"avg_MAE_90D_pct": -21.09, "avg_MFE_90D_pct": 49.66, "avg_four_b_full_window_peak_proximity": null, "avg_four_b_local_peak_proximity": null, "avg_green_lateness_ratio": null, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "changed_axes": ["high_MAE_label_spike_guard", "hard_4C_false_break_filter"], "current_profile_error_count_proxy": 1, "eligible_trigger_count": 8, "false_positive_rate": 0.125, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "late_green_count": 4, "missed_structural_count": 4, "positive_control_avg_MAE_90D_pct": -4.21, "positive_control_avg_MFE_90D_pct": 89.22, "profile_hypothesis": "block Stage3 promotion when MAE-risk family has label-only evidence and no bridge", "profile_id": "R13_counterexample_guard_profile", "profile_scope": "guardrail_shadow", "redteam_counterexample_avg_MAE_90D_pct": -37.97, "redteam_counterexample_avg_MFE_90D_pct": 10.11, "row_type": "score_simulation", "score_return_alignment_verdict": "candidate_profile_separates_positive_controls_from_label_spike_drawdown", "selected_entry_trigger_per_case": 8}
```

### residual_contribution row
```jsonl
{"canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "do_not_propose_new_weight_delta": false, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 8, "new_symbol_count": 8, "new_trigger_family_count": 8, "residual_error_types_found": ["4B_too_late_for_label_spike_high_MAE", "4C_too_late_after_non_price_break", "too_conservative_for_verified_bridge_positive_controls", "false_break_risk_when_generic_policy_or_theme_label_is_used"], "reused_case_count": 8, "round": "R13", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage2_required_bridge"]}
```

## Batch Ingest Self-Audit
```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. This R13 file is not live candidate research and not a sector-specific promotion batch. It is a cross-archetype 4B/4C guardrail checkpoint.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Treat this R13 file as cross-archetype guardrail evidence, not as new sector coverage for source C03/C13/C16/C18/C22/C25/C30/C32.
- Do not double-count source-sector rows and this R13 holdout as independent sector evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction and counterexamples are preserved.
- Positive score promotion still requires non-price bridge evidence and clean MFE/MAE.
- 4B rows are overlay/risk calibration only; 4C rows are thesis-break/protection calibration only.
- If this R13 weakens hard_4c routing for generic label disappointment, log it as a false-break filter rather than reverting hard 4C globally.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R13/L10 scope consistency.
4. Preserve source_canonical_archetype_id as lineage, but aggregate this MD under R13_CROSS_ARCHETYPE_4B_4C_REDTEAM.
5. Deduplicate by same_entry_group_id under the R13 canonical scope.
6. Update cross-archetype guardrail ledger only.
7. Preserve production calibrated profile unless the user explicitly asks for promotion batch.

## 27. Next Round State
```text
completed_round = R13
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = R13 cross-archetype checkpoint after local Priority0/Priority1/quality-repair sector fills
next_recommended_archetypes = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C27_CONTENT_IP_GLOBAL_MONETIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes
- MAIN_EXECUTION_PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO_REPEAT_INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- STOCK_WEB_MANIFEST: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- This loop uses local source-sector V12 MDs generated earlier in the same session as lineage inputs and preserves their Stock-Web MFE/MAE fields.