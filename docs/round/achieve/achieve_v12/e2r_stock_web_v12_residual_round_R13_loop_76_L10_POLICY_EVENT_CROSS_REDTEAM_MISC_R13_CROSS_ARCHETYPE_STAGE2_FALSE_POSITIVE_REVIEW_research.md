# E2R Stock-Web v12 Residual Research — R13 Loop 76 / L10 / Stage2 False-Positive Review

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 76,
  "computed_next_round": "R1",
  "computed_next_loop": 77,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "LOOP76_STAGE2_BRIDGE_REQUIREMENT_LOCAL4B_TENDER_CAP_NO_HARD4C_CHECKPOINT",
  "loop_objective": [
    "stage2_false_positive_review",
    "theme_policy_proxy_bridge_gap_review",
    "high_MAE_local4B_guardrail",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "controlled_positive_protection",
    "tender_floor_event_lifecycle_exit_guard",
    "share_count_validation_queue_prioritization",
    "source_repair_queue_prioritization",
    "price_validation_checkpoint"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "selected_cross_case_count": 36,
  "source_rounds_covered": "R1~R12",
  "source_canonical_count": 12,
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true,
  "new_sector_positive_case_count": 0,
  "do_not_count_as_new_sector_case": true
}
```

## Execution compliance note

This file is a standalone R13 cross-archetype checkpoint.  
It does not patch `stock_agent`, does not run live discovery, does not create new sector-specific positive cases, and does not propose immediate production scoring changes.

```text
R13_special_rule = cross_archetype_checkpoint_only
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R12 / loop 76.

Therefore:

```text
scheduled_round = R13
scheduled_loop = 76
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
computed_next_round = R1
computed_next_loop = 77
```

R13 is not a sector round.  
This file reuses the completed loop 76 R1~R12 trigger rows and compresses them into a cross-archetype Stage2 false-positive review.

## Source coverage

```text
source_rounds_covered = R1~R12
source_round_file_count = 12
selected_cross_case_count = 36
source_canonical_count = 12
new_sector_positive_case_count = 0
do_not_count_as_new_sector_case = true
```

Source files:

```text
e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
e2r_stock_web_v12_residual_round_R3_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
e2r_stock_web_v12_residual_round_R4_loop_76_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
e2r_stock_web_v12_residual_round_R6_loop_76_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
e2r_stock_web_v12_residual_round_R7_loop_76_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
e2r_stock_web_v12_residual_round_R8_loop_76_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
e2r_stock_web_v12_residual_round_R10_loop_76_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
e2r_stock_web_v12_residual_round_R12_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

## Cross-case summary

```json
{
  "row_type": "r13_cross_summary",
  "round": "R13",
  "loop": 76,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "LOOP76_STAGE2_BRIDGE_REQUIREMENT_LOCAL4B_TENDER_CAP_NO_HARD4C_CHECKPOINT",
  "selected_cross_case_count": 36,
  "source_rounds_covered": [
    "R1",
    "R2",
    "R3",
    "R4",
    "R5",
    "R6",
    "R7",
    "R8",
    "R9",
    "R10",
    "R11",
    "R12"
  ],
  "source_canonical_count": 12,
  "canonical_counts": {
    "C02_POWER_GRID_DATACENTER_CAPEX": 3,
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": 3,
    "C13_BATTERY_JV_UTILIZATION_AMPC_IRA": 3,
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": 3,
    "C19_BRAND_RETAIL_INVENTORY_MARGIN": 3,
    "C22_INSURANCE_RATE_CYCLE_RESERVE": 3,
    "C24_BIO_TRIAL_DATA_EVENT_RISK": 3,
    "C27_CONTENT_IP_GLOBAL_MONETIZATION": 3,
    "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": 3,
    "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK": 3,
    "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": 3,
    "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP": 3
  },
  "role_counts": {
    "positive_or_lifecycle": 20,
    "stage2_false_positive": 13,
    "risk_positive": 1,
    "riskwatch_boundary": 2
  },
  "stage2_false_positive_bridge_gap_count": 13,
  "risk_positive_local4b_count": 1,
  "riskwatch_or_overbearish_boundary_count": 2,
  "positive_or_lifecycle_count": 20,
  "early_MAE_30D_le_-20_count": 0,
  "high_MAE_90D_le_-20_count": 7,
  "high_MAE_180D_le_-25_count": 10,
  "post_peak_drawdown_le_-35_count": 19,
  "high_MFE_then_drawdown_count": 14,
  "controlled_MAE_stage2_candidate_count": 14,
  "theme_or_policy_proxy_bridge_gap_count": 31,
  "tender_floor_or_event_lifecycle_count": 3,
  "share_count_validation_required_count": 11,
  "source_repair_required_count": 36,
  "hard_4c_price_only_allowed_count": 0,
  "new_sector_positive_case_count": 0,
  "r13_decision": "guardrail_checkpoint_only",
  "r13_result": "do_not_change_runtime_weights_until_source_repair_and_validation"
}
```

## Main residual finding

Loop 76 repeats one mechanism across different sectors:

```text
theme / policy / value-up / clinical / tender / operating-cycle headline
→ MFE
→ source_proxy_only or stale bridge
→ MAE or post-peak drawdown
→ local 4B-watch or event exit/cap
```

The safe rule is:

```text
MFE validates tradability.
Only archetype-specific non-price bridge validates durable Stage2.
```

## Guardrail 1 — Stage2 must have a bridge, not a headline

Loop 76 bridge examples:

```text
C02: transformer/cable order backlog, delivery slot, ASP/copper pass-through, margin
C10: equipment order, customer capex schedule, delivery/backlog, margin
C13: US/IRA/AMPC local supply, customer ramp, utilization/call-off, margin
C17: price-cost spread, inventory/order, utilization/volume, margin
C19: inventory normalization, sell-through, markdown control, channel productivity, margin
C22: reserve/CSM quality, K-ICS, loss-ratio/underwriting, capital return
C24: endpoint quality, safety, partner validation, regulatory path, financing runway
C27: DAU/MAU, IAP/paid-content, licensing, production backlog, margin
C29: OEM volume, program visibility, module/lamp/thermal mix, utilization, margin
C30: PF/refinancing/orderbook/liquidity risk vs confirmed solvency break
C31: direct beneficiary, actual project order, revenue, margin
C32: tender mechanics, closing certainty, minority economics, floor/cap terms
```

## Guardrail 2 — Theme/proxy/beta rows route to local 4B when the bridge is absent

Counts:

```text
stage2_false_positive_bridge_gap_count = 13
theme_or_policy_proxy_bridge_gap_count = 31
early_MAE_30D <= -20% count = 0
MAE_90D <= -20% count = 7
MAE_180D <= -25% count = 10
post_peak_drawdown <= -35% count = 19
high_MFE_then_drawdown count = 14
```

Worst false-positive rows:

```text
R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / 207760 미스터블루 — counterexample_webtoon_theme_local4b_with_sharecount_validation: MFE180 41.15%, MAE180 -47.35%, DD -62.7%, action=stage2_false_positive_local_4b_watch
R3 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / 278280 천보 — counterexample_utilization_local4b: MFE180 9.91%, MAE180 -46.04%, DD -50.9%, action=stage2_false_positive_local_4b_watch
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 018880 한온시스템 — counterexample_EV_thermal_beta_local4b: MFE180 10.39%, MAE180 -39.45%, DD -45.15%, action=stage2_false_positive_local_4b_watch
R2 / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE / 036930 주성엔지니어링 — counterexample_equipment_beta_local4b_with_sharecount_validation: MFE180 19.45%, MAE180 -36.46%, DD -46.8%, action=stage2_false_positive_local_4b_watch
R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 071090 하이스틸 — counterexample_policy_proxy_local4b: MFE180 18.44%, MAE180 -36.0%, DD -45.97%, action=stage2_false_positive_local_4b_watch
R4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD / 004430 송원산업 — counterexample_commodity_beta_local4b: MFE180 5.89%, MAE180 -34.69%, DD -38.32%, action=stage2_false_positive_local_4b_watch
R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 008970 동양철관 — counterexample_policy_proxy_local4b_with_sharecount_validation: MFE180 42.81%, MAE180 -29.7%, DD -50.77%, action=stage2_false_positive_local_4b_watch
R7 / C24_BIO_TRIAL_DATA_EVENT_RISK / 215600 신라젠 — counterexample_trial_beta_local4b_post_ca: MFE180 7.34%, MAE180 -26.88%, DD -31.88%, action=stage2_false_positive_local_4b_watch
R4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD / 120110 코오롱인더 — counterexample_industrial_material_beta_local4b: MFE180 4.43%, MAE180 -23.77%, DD -27.0%, action=stage2_false_positive_bridge_gap_watch
R6 / C22_INSURANCE_RATE_CYCLE_RESERVE / 085620 미래에셋생명 — counterexample_life_insurance_beta_local4b: MFE180 14.64%, MAE180 -20.63%, DD -30.77%, action=stage2_false_positive_local_4b_watch
```

Worst MAE rows across all roles:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / 001470 삼부토건 — risk_positive_local4b_no_hard4c_with_sharecount_validation: MFE180 32.95%, MAE180 -79.58%, DD -84.64%, action=local_4b_watch_no_hard_4c
R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / 207760 미스터블루 — counterexample_webtoon_theme_local4b_with_sharecount_validation: MFE180 41.15%, MAE180 -47.35%, DD -62.7%, action=stage2_false_positive_local_4b_watch
R3 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / 278280 천보 — counterexample_utilization_local4b: MFE180 9.91%, MAE180 -46.04%, DD -50.9%, action=stage2_false_positive_local_4b_watch
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 018880 한온시스템 — counterexample_EV_thermal_beta_local4b: MFE180 10.39%, MAE180 -39.45%, DD -45.15%, action=stage2_false_positive_local_4b_watch
R2 / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE / 036930 주성엔지니어링 — counterexample_equipment_beta_local4b_with_sharecount_validation: MFE180 19.45%, MAE180 -36.46%, DD -46.8%, action=stage2_false_positive_local_4b_watch
R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 071090 하이스틸 — counterexample_policy_proxy_local4b: MFE180 18.44%, MAE180 -36.0%, DD -45.97%, action=stage2_false_positive_local_4b_watch
R3 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / 121600 나노신소재 — positive_with_later_4b_watch_and_sharecount_validation: MFE180 50.29%, MAE180 -34.76%, DD -56.59%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD / 004430 송원산업 — counterexample_commodity_beta_local4b: MFE180 5.89%, MAE180 -34.69%, DD -38.32%, action=stage2_false_positive_local_4b_watch
R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 008970 동양철관 — counterexample_policy_proxy_local4b_with_sharecount_validation: MFE180 42.81%, MAE180 -29.7%, DD -50.77%, action=stage2_false_positive_local_4b_watch
R7 / C24_BIO_TRIAL_DATA_EVENT_RISK / 215600 신라젠 — counterexample_trial_beta_local4b_post_ca: MFE180 7.34%, MAE180 -26.88%, DD -31.88%, action=stage2_false_positive_local_4b_watch
R4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD / 120110 코오롱인더 — counterexample_industrial_material_beta_local4b: MFE180 4.43%, MAE180 -23.77%, DD -27.0%, action=stage2_false_positive_bridge_gap_watch
R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / 194480 데브시스터즈 — positive_with_later_4b_watch_and_sharecount_validation: MFE180 79.32%, MAE180 -20.68%, DD -55.77%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
```

## Guardrail 3 — High MFE with later drawdown is lifecycle, not permanent Green

High-MFE / drawdown rows:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / 001470 삼부토건 — risk_positive_local4b_no_hard4c_with_sharecount_validation: MFE180 32.95%, MAE180 -79.58%, DD -84.64%, action=local_4b_watch_no_hard_4c
R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / 207760 미스터블루 — counterexample_webtoon_theme_local4b_with_sharecount_validation: MFE180 41.15%, MAE180 -47.35%, DD -62.7%, action=stage2_false_positive_local_4b_watch
R3 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / 348370 엔켐 — positive_with_later_4b_watch_and_sharecount_validation: MFE180 333.52%, MAE180 -5.16%, DD -62.23%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R1 / C02_POWER_GRID_DATACENTER_CAPEX / 000500 가온전선 — positive_with_later_4b_watch_and_corporate_action_caveat: MFE180 243.32%, MAE180 -4.38%, DD -60.0%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R3 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / 121600 나노신소재 — positive_with_later_4b_watch_and_sharecount_validation: MFE180 50.29%, MAE180 -34.76%, DD -56.59%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R1 / C02_POWER_GRID_DATACENTER_CAPEX / 033100 제룡전기 — positive_with_later_4b_watch: MFE180 363.0%, MAE180 0.0%, DD -56.45%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / 194480 데브시스터즈 — positive_with_later_4b_watch_and_sharecount_validation: MFE180 79.32%, MAE180 -20.68%, DD -55.77%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R1 / C02_POWER_GRID_DATACENTER_CAPEX / 006340 대원전선 — counterexample_theme_spike_local4b: MFE180 189.28%, MAE180 -7.27%, DD -53.21%, action=stage2_false_positive_local_4b_watch
R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 039610 화성밸브 — policy_lifecycle_positive_with_later_4b_watch: MFE180 78.68%, MAE180 -18.31%, DD -51.43%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 008970 동양철관 — counterexample_policy_proxy_local4b_with_sharecount_validation: MFE180 42.81%, MAE180 -29.7%, DD -50.77%, action=stage2_false_positive_local_4b_watch
R4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD / 014830 유니드 — positive_with_later_4b_watch: MFE180 73.79%, MAE180 -4.83%, DD -45.24%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R2 / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE / 240810 원익IPS — positive_with_later_4b_watch: MFE180 56.27%, MAE180 -6.1%, DD -39.91%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
```

Correct treatment:

```text
high MFE + verified bridge = historical Stage2 can be valid
high MFE + bridge stale + post-peak drawdown = lifecycle local 4B
high MFE + tender floor = event exit/cap after floor
high MFE + no bridge = false Stage2 / local 4B
```

## Guardrail 4 — Controlled-MAE positives must be protected after source repair

R13 must not become a blunt blocker.  
The following controlled-MAE positives should be protected if non-price bridge evidence is repaired:

```text
R1 / C02_POWER_GRID_DATACENTER_CAPEX / 033100 제룡전기 — positive_with_later_4b_watch: MFE180 363.0%, MAE180 0.0%, DD -56.45%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R3 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / 348370 엔켐 — positive_with_later_4b_watch_and_sharecount_validation: MFE180 333.52%, MAE180 -5.16%, DD -62.23%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R1 / C02_POWER_GRID_DATACENTER_CAPEX / 000500 가온전선 — positive_with_later_4b_watch_and_corporate_action_caveat: MFE180 243.32%, MAE180 -4.38%, DD -60.0%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R7 / C24_BIO_TRIAL_DATA_EVENT_RISK / 298380 에이비엘바이오 — positive_with_lifecycle_4b_watch: MFE180 101.4%, MAE180 -0.23%, DD -18.59%, action=protect_stage2_after_source_repair
R4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD / 014830 유니드 — positive_with_later_4b_watch: MFE180 73.79%, MAE180 -4.83%, DD -45.24%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R2 / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE / 031980 피에스케이홀딩스 — positive_with_later_4b_watch: MFE180 72.23%, MAE180 -2.38%, DD -38.11%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R2 / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE / 240810 원익IPS — positive_with_later_4b_watch: MFE180 56.27%, MAE180 -6.1%, DD -39.91%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 115390 락앤락 — governance_tender_floor_positive_with_cap_watch: MFE180 48.48%, MAE180 -0.17%, DD -5.92%, action=event_lifecycle_stage2_with_floor_exit
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 005850 에스엘 — positive_with_later_4b_watch: MFE180 47.98%, MAE180 -6.83%, DD -35.05%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R6 / C22_INSURANCE_RATE_CYCLE_RESERVE / 000370 한화손해보험 — positive_with_later_4b_watch: MFE180 44.21%, MAE180 -3.94%, DD -25.84%, action=protect_stage2_after_source_repair
```

## Guardrail 5 — Tender-floor events are event-lifecycle rows

Tender/floor rows:

```text
R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 003410 쌍용C&E — governance_tender_floor_positive_no_operating_green: MFE180 16.75%, MAE180 0.0%, DD -0.57%, action=event_lifecycle_stage2_with_floor_exit
R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 115390 락앤락 — governance_tender_floor_positive_with_cap_watch: MFE180 48.48%, MAE180 -0.17%, DD -5.92%, action=event_lifecycle_stage2_with_floor_exit
R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 119860 커넥트웨이브 — counterexample_tender_cap_no_permanent_green: MFE180 47.27%, MAE180 -1.14%, DD -1.88%, action=event_lifecycle_exit_cap_no_permanent_green
```

Rule:

```text
tender mechanics + minority economics + closing path = event-lifecycle Stage2 possible
price pins near floor = exit/cap
no separate operating bridge = no permanent Green
```

## Guardrail 6 — Hard 4C remains non-price evidence based

No loop 76 row justifies price-only hard 4C.

```text
hard_4c_price_only_allowed_count = 0
```

Hard 4C requires non-price thesis break evidence:

```text
default / refinancing failure / court rehabilitation
contract cancellation / customer loss / order cut
clinical endpoint failure / safety signal / regulatory rejection
policy reversal / project cancellation
tender/deal failure or legal break
reserve impairment / K-ICS capital break / covenant breach
insolvency / solvency break
```

C30 rows are the clearest boundary:

```text
001470 삼부토건 = high-MAE local 4B, not price-only hard 4C
034300 신세계건설 = post-CA support/recovery no-hard-4C boundary
035890 서희건설 = bounded-MAE/orderbook buffer no-hard-4C boundary
```

## Guardrail 7 — Validation queues

Share-count validation queue:

```text
R10:001470:삼부토건
R11:008970:동양철관
R12:119860:커넥트웨이브
R2:036930:주성엔지니어링
R3:121600:나노신소재
R3:348370:엔켐
R5:020000:한섬
R5:081660:휠라홀딩스
R7:141080:리가켐바이오/레고켐바이오
R8:194480:데브시스터즈
R8:207760:미스터블루
```

Source repair is still required for every row:

```text
source_repair_required_count = 36
```

## Proposed cross-archetype decision

```json
{
  "row_type": "r13_guardrail_candidate",
  "round": "R13",
  "loop": 76,
  "axis": "stage2_bridge_requirement_local4b_tender_cap_no_hard4c",
  "decision": "hold_for_coding_agent_validation",
  "do_not_propose_new_weight_delta": true,
  "candidate_rules": [
    "Stage2 requires archetype-specific non-price bridge evidence; MFE alone is not Green.",
    "Theme/policy/beta/proxy rows without direct order, revenue, utilization, margin, endpoint, reserve, monetization, tender or capital-return bridge should be capped and routed to local 4B-watch when MAE or post-peak drawdown opens.",
    "Emit local 4B-watch when MAE_30D <= -20%, MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35% and bridge evidence is absent/stale.",
    "Protect controlled-MAE positives after source repair; especially MFE_180D >= 20% and MAE_180D > -10%.",
    "Tender-floor / voluntary-delisting rows may be event-lifecycle Stage2, but must exit/cap near the tender floor; do not leave permanent Green without separate operating bridge.",
    "C30 hard 4C remains evidence-based; price-only MAE/drawdown is not default/refinancing/solvency proof.",
    "Share-count or post-corporate-action validation blocks runtime ingestion until verified."
  ],
  "high_priority_false_positive_symbols": [
    "R8:207760:미스터블루",
    "R3:278280:천보",
    "R9:018880:한온시스템",
    "R2:036930:주성엔지니어링",
    "R11:071090:하이스틸",
    "R4:004430:송원산업",
    "R11:008970:동양철관",
    "R7:215600:신라젠",
    "R4:120110:코오롱인더",
    "R6:085620:미래에셋생명"
  ],
  "protect_controlled_positive_symbols": [
    "R1:033100:제룡전기",
    "R3:348370:엔켐",
    "R1:000500:가온전선",
    "R7:298380:에이비엘바이오",
    "R4:014830:유니드",
    "R2:031980:피에스케이홀딩스",
    "R2:240810:원익IPS",
    "R12:115390:락앤락",
    "R9:005850:에스엘",
    "R6:000370:한화손해보험"
  ],
  "tender_floor_event_lifecycle_symbols": [
    "R12:003410:쌍용C&E",
    "R12:115390:락앤락",
    "R12:119860:커넥트웨이브"
  ],
  "share_count_validation_symbols": [
    "R10:001470:삼부토건",
    "R11:008970:동양철관",
    "R12:119860:커넥트웨이브",
    "R2:036930:주성엔지니어링",
    "R3:121600:나노신소재",
    "R3:348370:엔켐",
    "R5:020000:한섬",
    "R5:081660:휠라홀딩스",
    "R7:141080:리가켐바이오/레고켐바이오",
    "R8:194480:데브시스터즈",
    "R8:207760:미스터블루"
  ]
}
```

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "validation_status": "usable_for_R13_cross_case_checkpoint", "source_round_files": ["e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "e2r_stock_web_v12_residual_round_R3_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "e2r_stock_web_v12_residual_round_R4_loop_76_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "e2r_stock_web_v12_residual_round_R6_loop_76_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "e2r_stock_web_v12_residual_round_R7_loop_76_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "e2r_stock_web_v12_residual_round_R8_loop_76_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "e2r_stock_web_v12_residual_round_R10_loop_76_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "e2r_stock_web_v12_residual_round_R12_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"]}
```

### R13 cross-case rows

```jsonl
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_case_id": "R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE", "source_trigger_id": "TRG_R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "symbol": "000500", "company_name": "가온전선", "trigger_type": "Stage2-Actionable-CableGridCapexLifecycleBridge", "trigger_date": "2024-01-24", "entry_date": "2024-01-25", "entry_price": 21700.0, "trigger_outcome_label": "positive_with_later_4b_watch_and_corporate_action_caveat", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 35.71, "MFE_90D_pct": 243.32, "MFE_180D_pct": 243.32, "MAE_30D_pct": -4.38, "MAE_90D_pct": -4.38, "MAE_180D_pct": -4.38, "peak_date": "2024-05-13", "peak_price": 74500.0, "drawdown_after_peak_pct": -60.0, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_case_id": "R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE", "source_trigger_id": "TRG_R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "symbol": "006340", "company_name": "대원전선", "trigger_type": "Stage2-FalsePositive / CopperCableGridThemeSpikeFade", "trigger_date": "2024-04-04", "entry_date": "2024-04-05", "entry_price": 1884.0, "trigger_outcome_label": "counterexample_theme_spike_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 189.28, "MFE_90D_pct": 189.28, "MFE_180D_pct": 189.28, "MAE_30D_pct": -7.27, "MAE_90D_pct": -7.27, "MAE_180D_pct": -7.27, "peak_date": "2024-05-13", "peak_price": 5450.0, "drawdown_after_peak_pct": -53.21, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_case_id": "R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG", "source_trigger_id": "TRG_R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "symbol": "033100", "company_name": "제룡전기", "trigger_type": "Stage2-Actionable-TransformerGridCapexBacklogBridge", "trigger_date": "2024-03-01", "entry_date": "2024-03-04", "entry_price": 21750.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 159.77, "MFE_90D_pct": 363.0, "MFE_180D_pct": 363.0, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-07-11", "peak_price": 100700.0, "drawdown_after_peak_pct": -56.45, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_case_id": "R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE", "source_trigger_id": "TRG_R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "symbol": "031980", "company_name": "피에스케이홀딩스", "trigger_type": "Stage2-Actionable-AdvancedPackagingEquipmentOrderCycleBridge", "trigger_date": "2024-02-21", "entry_date": "2024-02-22", "entry_price": 35650.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 38.57, "MFE_90D_pct": 72.23, "MFE_180D_pct": 72.23, "MAE_30D_pct": -2.38, "MAE_90D_pct": -2.38, "MAE_180D_pct": -2.38, "peak_date": "2024-07-24", "peak_price": 61400.0, "drawdown_after_peak_pct": -38.11, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_case_id": "R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE", "source_trigger_id": "TRG_R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "symbol": "036930", "company_name": "주성엔지니어링", "trigger_type": "Stage2-FalsePositive / ProcessEquipmentCycleBetaFade", "trigger_date": "2024-02-27", "entry_date": "2024-02-28", "entry_price": 34700.0, "trigger_outcome_label": "counterexample_equipment_beta_local4b_with_sharecount_validation", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 19.45, "MFE_90D_pct": 19.45, "MFE_180D_pct": 19.45, "MAE_30D_pct": -7.93, "MAE_90D_pct": -7.93, "MAE_180D_pct": -36.46, "peak_date": "2024-04-08", "peak_price": 41450.0, "drawdown_after_peak_pct": -46.8, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_case_id": "R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE", "source_trigger_id": "TRG_R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "symbol": "240810", "company_name": "원익IPS", "trigger_type": "Stage2-Actionable-MemoryProcessEquipmentRecoveryBridge", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 28700.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 56.27, "MFE_90D_pct": 56.27, "MFE_180D_pct": 56.27, "MAE_30D_pct": -0.35, "MAE_90D_pct": -0.35, "MAE_180D_pct": -6.1, "peak_date": "2024-04-08", "peak_price": 44850.0, "drawdown_after_peak_pct": -39.91, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_case_id": "R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION", "source_trigger_id": "TRG_R3L76-C13-121600-NANOSIN-CNT-CONDUCTIVE-ADDITIVE-US-UTILIZATION", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "symbol": "121600", "company_name": "나노신소재", "trigger_type": "Stage2-Actionable-CNTConductiveAdditiveUSUtilizationBridgeWithLater4B", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 105000.0, "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 50.29, "MFE_90D_pct": 50.29, "MFE_180D_pct": 50.29, "MAE_30D_pct": -0.86, "MAE_90D_pct": -3.9, "MAE_180D_pct": -34.76, "peak_date": "2024-02-22", "peak_price": 157800.0, "drawdown_after_peak_pct": -56.59, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_case_id": "R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE", "source_trigger_id": "TRG_R3L76-C13-278280-CHUNBO-ELECTROLYTE-ADDITIVE-UTILIZATION-FADE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "symbol": "278280", "company_name": "천보", "trigger_type": "Stage2-FalsePositive / ElectrolyteAdditiveUtilizationFade", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 90800.0, "trigger_outcome_label": "counterexample_utilization_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 9.91, "MFE_90D_pct": 9.91, "MFE_180D_pct": 9.91, "MAE_30D_pct": -5.07, "MAE_90D_pct": -21.7, "MAE_180D_pct": -46.04, "peak_date": "2024-02-21", "peak_price": 99800.0, "drawdown_after_peak_pct": -50.9, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_case_id": "R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE", "source_trigger_id": "TRG_R3L76-C13-348370-ENCHEM-US-ELECTROLYTE-IRA-LOCAL-SUPPLY-LIFECYCLE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "US_IRA_AMPC_ELECTROLYTE_CNT_LOCAL_SUPPLY_UTILIZATION_BRIDGE_VS_MATERIAL_UTILIZATION_FADE", "symbol": "348370", "company_name": "엔켐", "trigger_type": "Stage2-Actionable-USElectrolyteIRALocalSupplyBridgeWithLifecycle4B", "trigger_date": "2024-01-09", "entry_date": "2024-01-10", "entry_price": 91000.0, "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 293.96, "MFE_90D_pct": 333.52, "MFE_180D_pct": 333.52, "MAE_30D_pct": -5.16, "MAE_90D_pct": -5.16, "MAE_180D_pct": -5.16, "peak_date": "2024-04-08", "peak_price": 394500.0, "drawdown_after_peak_pct": -62.23, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_76_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_case_id": "R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE", "source_trigger_id": "TRG_R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "symbol": "004430", "company_name": "송원산업", "trigger_type": "Stage2-FalsePositive / SpecialtyAdditiveSpreadFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 15280.0, "trigger_outcome_label": "counterexample_commodity_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 5.89, "MFE_90D_pct": 5.89, "MFE_180D_pct": 5.89, "MAE_30D_pct": -6.81, "MAE_90D_pct": -20.55, "MAE_180D_pct": -34.69, "peak_date": "2024-02-16", "peak_price": 16180.0, "drawdown_after_peak_pct": -38.32, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_76_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_case_id": "R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE", "source_trigger_id": "TRG_R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "symbol": "014830", "company_name": "유니드", "trigger_type": "Stage2-Actionable-KOHCausticPotashSpreadMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-24", "entry_date": "2024-01-25", "entry_price": 68300.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 22.99, "MFE_90D_pct": 73.79, "MFE_180D_pct": 73.79, "MAE_30D_pct": -0.15, "MAE_90D_pct": -0.15, "MAE_180D_pct": -4.83, "peak_date": "2024-06-11", "peak_price": 118700.0, "drawdown_after_peak_pct": -45.24, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_76_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_case_id": "R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE", "source_trigger_id": "TRG_R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "symbol": "120110", "company_name": "코오롱인더", "trigger_type": "Stage2-FalsePositive / IndustrialChemicalMaterialSpreadFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 40600.0, "trigger_outcome_label": "counterexample_industrial_material_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 4.43, "MFE_90D_pct": 4.43, "MFE_180D_pct": 4.43, "MAE_30D_pct": -10.59, "MAE_90D_pct": -10.71, "MAE_180D_pct": -23.77, "peak_date": "2024-02-08", "peak_price": 42400.0, "drawdown_after_peak_pct": -27.0, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_bridge_gap_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE", "source_trigger_id": "TRG_R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "symbol": "020000", "company_name": "한섬", "trigger_type": "Stage2-FalsePositive / ApparelRetailInventoryBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 18600.0, "trigger_outcome_label": "counterexample_inventory_margin_fade_with_sharecount_validation", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 16.4, "MFE_90D_pct": 16.4, "MFE_180D_pct": 16.4, "MAE_30D_pct": 0.0, "MAE_90D_pct": -4.46, "MAE_180D_pct": -15.91, "peak_date": "2024-02-07", "peak_price": 21650.0, "drawdown_after_peak_pct": -27.76, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_bridge_gap_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN", "source_trigger_id": "TRG_R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "symbol": "081660", "company_name": "휠라홀딩스", "trigger_type": "Stage2-SlowPositive-GlobalBrandInventoryMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 39800.0, "trigger_outcome_label": "positive_slow_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 5.4, "MFE_90D_pct": 8.04, "MFE_180D_pct": 11.93, "MAE_30D_pct": -3.52, "MAE_90D_pct": -6.28, "MAE_180D_pct": -6.28, "peak_date": "2024-08-01", "peak_price": 44550.0, "drawdown_after_peak_pct": -14.7, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_yellow_after_source_repair_lifecycle_managed", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY", "source_trigger_id": "TRG_R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "symbol": "093050", "company_name": "LF", "trigger_type": "Stage2-SlowPositive-ApparelBrandInventoryMarginBridge", "trigger_date": "2024-02-29", "entry_date": "2024-03-04", "entry_price": 13170.0, "trigger_outcome_label": "positive_slow_boundary", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 20.88, "MFE_90D_pct": 20.88, "MFE_180D_pct": 20.88, "MAE_30D_pct": -0.84, "MAE_90D_pct": -0.84, "MAE_180D_pct": -0.84, "peak_date": "2024-03-28", "peak_price": 15920.0, "drawdown_after_peak_pct": -17.84, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_76_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN", "source_trigger_id": "TRG_R6L76-C22-000370-HANWHA-GENERAL-INSURANCE-LOSS-RATIO-CAPITAL-RETURN", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "symbol": "000370", "company_name": "한화손해보험", "trigger_type": "Stage2-Actionable-NonlifeLossRatioCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4320.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 42.82, "MFE_90D_pct": 42.82, "MFE_180D_pct": 44.21, "MAE_30D_pct": -3.94, "MAE_90D_pct": -3.94, "MAE_180D_pct": -3.94, "peak_date": "2024-08-20", "peak_price": 6230.0, "drawdown_after_peak_pct": -25.84, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_76_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN", "source_trigger_id": "TRG_R6L76-C22-003690-KOREANRE-REINSURANCE-RESERVE-CAPITAL-RETURN", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "symbol": "003690", "company_name": "코리안리", "trigger_type": "Stage2-SlowPositive-ReinsuranceReserveCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7580.0, "trigger_outcome_label": "positive_slow_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 9.89, "MFE_90D_pct": 12.8, "MFE_180D_pct": 26.0, "MAE_30D_pct": -1.45, "MAE_90D_pct": -1.45, "MAE_180D_pct": -1.45, "peak_date": "2024-11-05", "peak_price": 9550.0, "drawdown_after_peak_pct": -17.38, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_76_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE", "source_trigger_id": "TRG_R6L76-C22-085620-MIRAE-ASSET-LIFE-VALUEUP-BETA-RESERVE-FADE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_REINSURANCE_LIFE_CAPITAL_RETURN_RESERVE_BRIDGE_VS_VALUEUP_BETA_FADE", "symbol": "085620", "company_name": "미래에셋생명", "trigger_type": "Stage2-FalsePositive / LifeInsuranceValueupReserveBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5670.0, "trigger_outcome_label": "counterexample_life_insurance_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 14.64, "MFE_90D_pct": 14.64, "MFE_180D_pct": 14.64, "MAE_30D_pct": -11.82, "MAE_90D_pct": -20.63, "MAE_180D_pct": -20.63, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -30.77, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_76_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "source_case_id": "R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE", "source_trigger_id": "TRG_R7L76-C24-141080-LIGACHEM-ADC-TRIAL-DATA-POST-CA-LIFECYCLE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "symbol": "141080", "company_name": "리가켐바이오/레고켐바이오", "trigger_type": "Stage2-Actionable-ADCPipelineTrialDataPostCABridge", "trigger_date": "2024-04-23", "entry_date": "2024-04-24", "entry_price": 68000.0, "trigger_outcome_label": "positive_with_post_corporate_action_validation", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 5.88, "MFE_90D_pct": 45.44, "MFE_180D_pct": 105.29, "MAE_30D_pct": -4.41, "MAE_90D_pct": -10.88, "MAE_180D_pct": -10.88, "peak_date": "2024-10-22", "peak_price": 139600.0, "drawdown_after_peak_pct": -14.47, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_yellow_after_source_repair_lifecycle_managed", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_76_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "source_case_id": "R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE", "source_trigger_id": "TRG_R7L76-C24-215600-SILLAJEN-ONCOLOGY-TRIAL-DATA-POST-CA-BETA-FADE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "symbol": "215600", "company_name": "신라젠", "trigger_type": "Stage2-FalsePositive / OncologyTrialDataPostCABetaFade", "trigger_date": "2024-07-09", "entry_date": "2024-07-10", "entry_price": 3200.0, "trigger_outcome_label": "counterexample_trial_beta_local4b_post_ca", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 7.34, "MFE_90D_pct": 7.34, "MFE_180D_pct": 7.34, "MAE_30D_pct": -12.19, "MAE_90D_pct": -18.44, "MAE_180D_pct": -26.88, "peak_date": "2024-08-19", "peak_price": 3435.0, "drawdown_after_peak_pct": -31.88, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_76_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "source_case_id": "R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE", "source_trigger_id": "TRG_R7L76-C24-298380-ABL-BIO-BISPECIFIC-ADC-TRIAL-DATA-BRIDGE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BISPECIFIC_ADC_ONCOLOGY_TRIAL_DATA_EVENT_BRIDGE_VS_CLINICAL_BETA_FADE", "symbol": "298380", "company_name": "에이비엘바이오", "trigger_type": "Stage2-Actionable-BispecificADCTrialDataPartneringBridge", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 21500.0, "trigger_outcome_label": "positive_with_lifecycle_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 41.86, "MFE_90D_pct": 41.86, "MFE_180D_pct": 101.4, "MAE_30D_pct": -0.23, "MAE_90D_pct": -0.23, "MAE_180D_pct": -0.23, "peak_date": "2024-10-17", "peak_price": 43300.0, "drawdown_after_peak_pct": -18.59, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_76_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "source_case_id": "R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION", "source_trigger_id": "TRG_R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "symbol": "194480", "company_name": "데브시스터즈", "trigger_type": "Stage2-Actionable-GameIPGlobalLaunchMonetizationBridgeWithLifecycle4B", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 42550.0, "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 17.98, "MFE_90D_pct": 79.32, "MFE_180D_pct": 79.32, "MAE_30D_pct": -6.93, "MAE_90D_pct": -6.93, "MAE_180D_pct": -20.68, "peak_date": "2024-06-26", "peak_price": 76300.0, "drawdown_after_peak_pct": -55.77, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_76_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "source_case_id": "R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE", "source_trigger_id": "TRG_R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "symbol": "206560", "company_name": "덱스터", "trigger_type": "Stage2-BoundaryPositive-VFXContentProductionPipelineBridge", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 6000.0, "trigger_outcome_label": "positive_boundary_with_source_repair", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 37.33, "MFE_90D_pct": 37.33, "MFE_180D_pct": 37.33, "MAE_30D_pct": -3.5, "MAE_90D_pct": -3.5, "MAE_180D_pct": -3.5, "peak_date": "2024-09-27", "peak_price": 8240.0, "drawdown_after_peak_pct": -10.56, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_76_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "source_case_id": "R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE", "source_trigger_id": "TRG_R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "symbol": "207760", "company_name": "미스터블루", "trigger_type": "Stage2-FalsePositive / WebtoonIPThemeSpikeFade", "trigger_date": "2024-01-23", "entry_date": "2024-01-24", "entry_price": 2260.0, "trigger_outcome_label": "counterexample_webtoon_theme_local4b_with_sharecount_validation", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 41.15, "MFE_90D_pct": 41.15, "MFE_180D_pct": 41.15, "MAE_30D_pct": -3.76, "MAE_90D_pct": -3.76, "MAE_180D_pct": -47.35, "peak_date": "2024-02-20", "peak_price": 3190.0, "drawdown_after_peak_pct": -62.7, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE", "source_trigger_id": "TRG_R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "symbol": "005850", "company_name": "에스엘", "trigger_type": "Stage2-Actionable-LampModuleOEMMixMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32200.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 16.3, "MFE_90D_pct": 47.98, "MFE_180D_pct": 47.98, "MAE_30D_pct": -3.11, "MAE_90D_pct": -6.83, "MAE_180D_pct": -6.83, "peak_date": "2024-06-17", "peak_price": 47650.0, "drawdown_after_peak_pct": -35.05, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN", "source_trigger_id": "TRG_R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "symbol": "012330", "company_name": "현대모비스", "trigger_type": "Stage2-SlowPositive-ModuleASMixMarginCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 208000.0, "trigger_outcome_label": "positive_slow_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 29.81, "MFE_90D_pct": 29.81, "MFE_180D_pct": 29.81, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -3.61, "peak_date": "2024-03-18", "peak_price": 270000.0, "drawdown_after_peak_pct": -25.74, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE", "source_trigger_id": "TRG_R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "symbol": "018880", "company_name": "한온시스템", "trigger_type": "Stage2-FalsePositive / EVThermalUtilizationMarginFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6160.0, "trigger_outcome_label": "counterexample_EV_thermal_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 6.98, "MFE_90D_pct": 10.39, "MFE_180D_pct": 10.39, "MAE_30D_pct": -9.25, "MAE_90D_pct": -24.43, "MAE_180D_pct": -39.45, "peak_date": "2024-05-07", "peak_price": 6800.0, "drawdown_after_peak_pct": -45.15, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_76_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B", "source_trigger_id": "TRG_R10L76-C30-001470-SAMBU-CONSTRUCTION-FINANCING-RISK-LOCAL4B", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "symbol": "001470", "company_name": "삼부토건", "trigger_type": "Stage4B-Local-BuilderFinancingRiskHighMAE", "trigger_date": "2024-02-08", "entry_date": "2024-02-13", "entry_price": 2155.0, "trigger_outcome_label": "risk_positive_local4b_no_hard4c_with_sharecount_validation", "role_bucket": "risk_positive", "MFE_30D_pct": 32.95, "MFE_90D_pct": 32.95, "MFE_180D_pct": 32.95, "MAE_30D_pct": -6.73, "MAE_90D_pct": -29.93, "MAE_180D_pct": -79.58, "peak_date": "2024-03-15", "peak_price": 2865.0, "drawdown_after_peak_pct": -84.64, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "local_4b_watch_no_hard_4c", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_76_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C", "source_trigger_id": "TRG_R10L76-C30-034300-SHINSEGAE-CONSTRUCTION-POST-CA-SUPPORT-NO-HARD4C", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "symbol": "034300", "company_name": "신세계건설", "trigger_type": "RiskWatch-BufferedBuilderPostCASupportNoHard4C", "trigger_date": "2024-02-06", "entry_date": "2024-02-07", "entry_price": 11310.0, "trigger_outcome_label": "overbearish_counterexample_post_ca_no_hard4c", "role_bucket": "riskwatch_boundary", "MFE_30D_pct": 12.73, "MFE_90D_pct": 23.78, "MFE_180D_pct": 62.16, "MAE_30D_pct": -6.37, "MAE_90D_pct": -7.96, "MAE_180D_pct": -7.96, "peak_date": "2024-09-30", "peak_price": 18340.0, "drawdown_after_peak_pct": -1.42, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": false, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "riskwatch_no_hard_4c_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_76_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C", "source_trigger_id": "TRG_R10L76-C30-035890-SEOHEE-CONSTRUCTION-ORDERBOOK-BUFFER-NO-HARD4C", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "BUILDER_PF_FINANCING_RISK_LOCAL4B_VS_BUFFERED_SUPPORT_NO_HARD4C", "symbol": "035890", "company_name": "서희건설", "trigger_type": "RiskWatch-OrderbookBufferBoundedMAENoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1278.0, "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "role_bucket": "riskwatch_boundary", "MFE_30D_pct": 3.05, "MFE_90D_pct": 7.67, "MFE_180D_pct": 26.84, "MAE_30D_pct": -3.76, "MAE_90D_pct": -3.76, "MAE_180D_pct": -6.89, "peak_date": "2024-10-10", "peak_price": 1621.0, "drawdown_after_peak_pct": -13.76, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": false, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "riskwatch_no_hard_4c_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "source_trigger_id": "TRG_R11L76-C31-008970-DONGYANG-STEEL-PIPE-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "symbol": "008970", "company_name": "동양철관", "trigger_type": "Stage2-FalsePositive / EastSeaGasFieldPipePolicyBetaFade", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 1175.0, "trigger_outcome_label": "counterexample_policy_proxy_local4b_with_sharecount_validation", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 42.81, "MFE_90D_pct": 42.81, "MFE_180D_pct": 42.81, "MAE_30D_pct": -14.3, "MAE_90D_pct": -29.7, "MAE_180D_pct": -29.7, "peak_date": "2024-06-07", "peak_price": 1678.0, "drawdown_after_peak_pct": -50.77, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE", "source_trigger_id": "TRG_R11L76-C31-039610-HWASEONG-VALVE-EASTSEA-GAS-POLICY-LIFECYCLE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "symbol": "039610", "company_name": "화성밸브", "trigger_type": "Stage2-PolicyLifecycle-EastSeaGasFieldValveDirectBeneficiaryBridge", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 8630.0, "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 39.86, "MFE_90D_pct": 78.68, "MFE_180D_pct": 78.68, "MAE_30D_pct": -18.31, "MAE_90D_pct": -18.31, "MAE_180D_pct": -18.31, "peak_date": "2024-08-23", "peak_price": 15420.0, "drawdown_after_peak_pct": -51.43, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "source_trigger_id": "TRG_R11L76-C31-071090-HISTEEL-EASTSEA-GAS-POLICY-PIPE-BETA-FADE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_GAS_FIELD_PIPE_VALVE_INFRA_POLICY_EVENT_BRIDGE_VS_RESOURCE_THEME_FADE", "symbol": "071090", "company_name": "하이스틸", "trigger_type": "Stage2-FalsePositive / EastSeaGasFieldSteelPipePolicyBetaFade", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 4500.0, "trigger_outcome_label": "counterexample_policy_proxy_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 18.44, "MFE_90D_pct": 18.44, "MFE_180D_pct": 18.44, "MAE_30D_pct": -16.67, "MAE_90D_pct": -36.0, "MAE_180D_pct": -36.0, "peak_date": "2024-06-05", "peak_price": 5330.0, "drawdown_after_peak_pct": -45.97, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR", "source_trigger_id": "TRG_R12L76-C32-003410-SSANGYONGCNE-VOLUNTARY-DELISTING-TENDER-FLOOR", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "symbol": "003410", "company_name": "쌍용C&E", "trigger_type": "Stage2-GovernanceLifecycle / VoluntaryDelistingTenderFloorBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6030.0, "trigger_outcome_label": "governance_tender_floor_positive_no_operating_green", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 16.75, "MFE_90D_pct": 16.75, "MFE_180D_pct": 16.75, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-03-15", "peak_price": 7040.0, "drawdown_after_peak_pct": -0.57, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": false, "tender_floor_or_event_lifecycle": true, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "event_lifecycle_stage2_with_floor_exit", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR", "source_trigger_id": "TRG_R12L76-C32-115390-LOCKNLOCK-VOLUNTARY-DELISTING-TENDER-FLOOR", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "symbol": "115390", "company_name": "락앤락", "trigger_type": "Stage2-GovernanceLifecycle / TenderFloorMinorityEconomicsBridge", "trigger_date": "2024-02-16", "entry_date": "2024-02-19", "entry_price": 5920.0, "trigger_outcome_label": "governance_tender_floor_positive_with_cap_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 34.29, "MFE_90D_pct": 48.14, "MFE_180D_pct": 48.48, "MAE_30D_pct": -0.17, "MAE_90D_pct": -0.17, "MAE_180D_pct": -0.17, "peak_date": "2024-08-08", "peak_price": 8790.0, "drawdown_after_peak_pct": -5.92, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_or_policy_proxy_bridge_gap": false, "tender_floor_or_event_lifecycle": true, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "event_lifecycle_stage2_with_floor_exit", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "76", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN", "source_trigger_id": "TRG_R12L76-C32-119860-CONNECTWAVE-TENDER-CAP-NO-FURTHER-GREEN", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "VOLUNTARY_DELISTING_TENDER_FLOOR_MINORITY_ECONOMICS_BRIDGE_VS_TENDER_CAP_NO_FURTHER_GREEN", "symbol": "119860", "company_name": "커넥트웨이브", "trigger_type": "Stage2-Boundary / TenderFloorCapNoFurtherGreen", "trigger_date": "2024-03-13", "entry_date": "2024-03-14", "entry_price": 12250.0, "trigger_outcome_label": "counterexample_tender_cap_no_permanent_green", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 41.96, "MFE_90D_pct": 47.1, "MFE_180D_pct": 47.27, "MAE_30D_pct": -1.14, "MAE_90D_pct": -1.14, "MAE_180D_pct": -1.14, "peak_date": "2024-08-13", "peak_price": 18040.0, "drawdown_after_peak_pct": -1.88, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_or_policy_proxy_bridge_gap": false, "tender_floor_or_event_lifecycle": true, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "event_lifecycle_exit_cap_no_permanent_green", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
```

### R13 summary row

```jsonl
{"row_type": "r13_cross_summary", "round": "R13", "loop": 76, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "LOOP76_STAGE2_BRIDGE_REQUIREMENT_LOCAL4B_TENDER_CAP_NO_HARD4C_CHECKPOINT", "selected_cross_case_count": 36, "source_rounds_covered": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_count": 12, "canonical_counts": {"C02_POWER_GRID_DATACENTER_CAPEX": 3, "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": 3, "C13_BATTERY_JV_UTILIZATION_AMPC_IRA": 3, "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": 3, "C19_BRAND_RETAIL_INVENTORY_MARGIN": 3, "C22_INSURANCE_RATE_CYCLE_RESERVE": 3, "C24_BIO_TRIAL_DATA_EVENT_RISK": 3, "C27_CONTENT_IP_GLOBAL_MONETIZATION": 3, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": 3, "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK": 3, "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": 3, "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP": 3}, "role_counts": {"positive_or_lifecycle": 20, "stage2_false_positive": 13, "risk_positive": 1, "riskwatch_boundary": 2}, "stage2_false_positive_bridge_gap_count": 13, "risk_positive_local4b_count": 1, "riskwatch_or_overbearish_boundary_count": 2, "positive_or_lifecycle_count": 20, "early_MAE_30D_le_-20_count": 0, "high_MAE_90D_le_-20_count": 7, "high_MAE_180D_le_-25_count": 10, "post_peak_drawdown_le_-35_count": 19, "high_MFE_then_drawdown_count": 14, "controlled_MAE_stage2_candidate_count": 14, "theme_or_policy_proxy_bridge_gap_count": 31, "tender_floor_or_event_lifecycle_count": 3, "share_count_validation_required_count": 11, "source_repair_required_count": 36, "hard_4c_price_only_allowed_count": 0, "new_sector_positive_case_count": 0, "r13_decision": "guardrail_checkpoint_only", "r13_result": "do_not_change_runtime_weights_until_source_repair_and_validation"}
```

### R13 guardrail candidate row

```jsonl
{"row_type": "r13_guardrail_candidate", "round": "R13", "loop": 76, "axis": "stage2_bridge_requirement_local4b_tender_cap_no_hard4c", "decision": "hold_for_coding_agent_validation", "do_not_propose_new_weight_delta": true, "candidate_rules": ["Stage2 requires archetype-specific non-price bridge evidence; MFE alone is not Green.", "Theme/policy/beta/proxy rows without direct order, revenue, utilization, margin, endpoint, reserve, monetization, tender or capital-return bridge should be capped and routed to local 4B-watch when MAE or post-peak drawdown opens.", "Emit local 4B-watch when MAE_30D <= -20%, MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35% and bridge evidence is absent/stale.", "Protect controlled-MAE positives after source repair; especially MFE_180D >= 20% and MAE_180D > -10%.", "Tender-floor / voluntary-delisting rows may be event-lifecycle Stage2, but must exit/cap near the tender floor; do not leave permanent Green without separate operating bridge.", "C30 hard 4C remains evidence-based; price-only MAE/drawdown is not default/refinancing/solvency proof.", "Share-count or post-corporate-action validation blocks runtime ingestion until verified."], "high_priority_false_positive_symbols": ["R8:207760:미스터블루", "R3:278280:천보", "R9:018880:한온시스템", "R2:036930:주성엔지니어링", "R11:071090:하이스틸", "R4:004430:송원산업", "R11:008970:동양철관", "R7:215600:신라젠", "R4:120110:코오롱인더", "R6:085620:미래에셋생명"], "protect_controlled_positive_symbols": ["R1:033100:제룡전기", "R3:348370:엔켐", "R1:000500:가온전선", "R7:298380:에이비엘바이오", "R4:014830:유니드", "R2:031980:피에스케이홀딩스", "R2:240810:원익IPS", "R12:115390:락앤락", "R9:005850:에스엘", "R6:000370:한화손해보험"], "tender_floor_event_lifecycle_symbols": ["R12:003410:쌍용C&E", "R12:115390:락앤락", "R12:119860:커넥트웨이브"], "share_count_validation_symbols": ["R10:001470:삼부토건", "R11:008970:동양철관", "R12:119860:커넥트웨이브", "R2:036930:주성엔지니어링", "R3:121600:나노신소재", "R3:348370:엔켐", "R5:020000:한섬", "R5:081660:휠라홀딩스", "R7:141080:리가켐바이오/레고켐바이오", "R8:194480:데브시스터즈", "R8:207760:미스터블루"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": 76, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard", "corporate_action_validation_guard", "event_lifecycle_exit_guard", "overbearish_no_hard4c_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": false, "canonical_archetype_rule_candidate": true, "narrative_summary": "Loop 76 cross-case review shows that Stage2 false positives mostly come from theme/policy/proxy/beta rows without archetype-specific bridge evidence. R13 strengthens local 4B routing, controlled-positive protection, tender-floor exit/cap logic and no-hard-4C boundaries."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
source_round_files = R1~R12 loop 76 standalone MDs
selected_cross_case_count = 36
all_cross_cases_have_trigger_rows = true
production_scoring_changed = false
shadow_weight_only = true
```

R13-specific validation:

```text
no_new_sector_specific_positive_cases = true
do_not_count_as_new_sector_case = true
R13_large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
R13_canonical_scope = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

Data-quality caveat:

```text
All source loop-76 rows are still source_proxy_only / evidence_url_pending.
R13 is therefore a guardrail-shape checkpoint, not a runtime scoring patch.
Coding-agent promotion requires non-proxy evidence repair and share-count / corporate-action validation.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this R13 loop 76 cross-archetype residual research MD.

Do not patch production scoring blindly.
This file is a guardrail checkpoint only.

Candidate axis:
stage2_bridge_requirement_local4b_tender_cap_no_hard4c

Required checks before implementation:
1. Validate all R13 cross-case rows against their source R1~R12 loop 76 trigger rows.
2. Confirm R13 created no new sector-specific positive cases.
3. Keep R13 output under:
   L10_POLICY_EVENT_CROSS_REDTEAM_MISC
   R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
4. For each runtime Stage2 candidate, require archetype-specific non-price bridge evidence.
5. Emit local 4B-watch when:
   - bridge is missing or stale,
   - MAE_30D <= -20%, or
   - MAE_90D <= -20%, or
   - MAE_180D <= -25%, or
   - post-peak drawdown <= -35%.
6. Preserve controlled-MAE positives after source repair:
   - MFE_180D >= 20%,
   - MAE_180D > -10%,
   - non-price bridge exists.
7. Treat high-MFE/post-peak drawdown cases as lifecycle candidates, not permanent Green.
8. Treat tender-floor / voluntary-delisting cases as event-lifecycle rows and cap/exit after the floor unless a separate operating bridge exists.
9. Do not convert local 4B into hard 4C without non-price thesis break evidence.
10. Run share-count and corporate-action validation for every cross row marked with those flags.
11. Emit before/after diagnostics and reject if the guardrail overblocks verified low-MAE positives.
```

---

## Final round state

```text
completed_round = R13
completed_loop = 76
next_round = R1
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

