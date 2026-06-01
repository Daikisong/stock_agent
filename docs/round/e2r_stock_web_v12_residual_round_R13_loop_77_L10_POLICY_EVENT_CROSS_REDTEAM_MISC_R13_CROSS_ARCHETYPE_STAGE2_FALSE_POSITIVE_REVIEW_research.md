# E2R Stock-Web v12 Residual Research — R13 Loop 77 / L10 / Stage2 False-Positive Review

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 77,
  "computed_next_round": "R1",
  "computed_next_loop": 78,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "LOOP77_STAGE2_BRIDGE_LOCAL4B_NO_HARD4C_GUARDRAIL_CHECKPOINT",
  "loop_objective": [
    "stage2_false_positive_review",
    "theme_policy_beta_bridge_gap_review",
    "high_MAE_local4B_guardrail",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "controlled_positive_protection",
    "policy_event_lifecycle_guard",
    "share_count_validation_queue_prioritization",
    "post_corporate_action_validation_queue_prioritization",
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

Previous completed state in this interactive run: R12 / loop 77.

Therefore:

```text
scheduled_round = R13
scheduled_loop = 77
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
computed_next_round = R1
computed_next_loop = 78
```

R13 is not a sector round.  
This file reuses completed loop 77 R1~R12 trigger rows and compresses them into a cross-archetype Stage2 false-positive review.

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
e2r_stock_web_v12_residual_round_R1_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
e2r_stock_web_v12_residual_round_R2_loop_77_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
e2r_stock_web_v12_residual_round_R3_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
e2r_stock_web_v12_residual_round_R4_loop_77_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
e2r_stock_web_v12_residual_round_R5_loop_77_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
e2r_stock_web_v12_residual_round_R6_loop_77_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
e2r_stock_web_v12_residual_round_R7_loop_77_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
e2r_stock_web_v12_residual_round_R8_loop_77_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
e2r_stock_web_v12_residual_round_R9_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
e2r_stock_web_v12_residual_round_R10_loop_77_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
e2r_stock_web_v12_residual_round_R11_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
e2r_stock_web_v12_residual_round_R12_loop_77_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

## Cross-case summary

```json
{
  "row_type": "r13_cross_summary",
  "round": "R13",
  "loop": 77,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "LOOP77_STAGE2_BRIDGE_LOCAL4B_NO_HARD4C_GUARDRAIL_CHECKPOINT",
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
    "C01_ORDER_BACKLOG_MARGIN_BRIDGE": 3,
    "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 3,
    "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH": 3,
    "C11_BATTERY_ORDERBOOK_RERATING": 3,
    "C15_MATERIAL_SPREAD_SUPERCYCLE": 3,
    "C18_CONSUMER_EXPORT_CHANNEL_REORDER": 3,
    "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN": 3,
    "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT": 3,
    "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE": 3,
    "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": 3,
    "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK": 3,
    "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": 3
  },
  "role_counts": {
    "positive_or_lifecycle": 17,
    "stage2_false_positive": 16,
    "risk_positive": 1,
    "riskwatch_boundary": 2
  },
  "stage2_false_positive_bridge_gap_count": 16,
  "risk_positive_local4b_count": 1,
  "riskwatch_or_overbearish_boundary_count": 2,
  "positive_or_lifecycle_count": 17,
  "early_MAE_30D_le_-20_count": 1,
  "high_MAE_90D_le_-20_count": 10,
  "high_MAE_180D_le_-25_count": 14,
  "post_peak_drawdown_le_-35_count": 20,
  "post_peak_drawdown_le_-25_count": 26,
  "high_MFE_then_drawdown_count": 15,
  "controlled_MAE_stage2_candidate_count": 13,
  "theme_policy_proxy_bridge_gap_count": 33,
  "tender_floor_or_event_lifecycle_count": 0,
  "share_count_validation_required_count": 4,
  "post_corporate_action_validation_required_count": 1,
  "source_repair_required_count": 36,
  "hard_4c_price_only_allowed_count": 0,
  "new_sector_positive_case_count": 0,
  "r13_decision": "guardrail_checkpoint_only",
  "r13_result": "do_not_change_runtime_weights_until_source_repair_and_validation"
}
```

## Main residual finding

Loop 77 repeats one mechanism across different sectors:

```text
theme / policy / operating-cycle / value-up / device / defense headline
→ MFE
→ source_proxy_only or stale bridge
→ MAE or post-peak drawdown
→ local 4B-watch, RiskWatch/no-hard-4C, or lifecycle exit
```

The safe rule is:

```text
MFE validates tradability.
Only archetype-specific non-price bridge validates durable Stage2.
```

## Guardrail 1 — Stage2 must have a bridge, not a headline

Loop 77 bridge examples:

```text
C01: order/backlog, customer quality, delivery slot, ASP/mix, utilization, margin
C03: defense export framework, named program, backlog, delivery, revenue recognition, margin
C07: HBM/AI customer capex, equipment order, delivery/backlog, tool adoption, margin
C11: customer orderbook, call-off, capacity absorption, price pass-through, utilization, margin
C15: copper/nonferrous spread, inventory, volume, price pass-through, margin
C18: overseas channel reorder, sell-through, distributor inventory, pricing/product mix, margin
C21: ROE/PBR, CET1/capital buffer, dividend/buyback, balance-sheet quality, shareholder return
C25: export/reimbursement/adoption, distributor sell-through, installed-base utilization, pricing, margin
C26: advertiser budget, ROAS, repeat spend/client retention, platform revenue, operating leverage
C29: customer volume, program/orderbook, product mix, utilization, pricing, margin
C30: PF/refinancing/orderbook/liquidity risk vs confirmed solvency break
C31: policy event, direct beneficiary mapping, direct demand/sell-through/reorder, inventory, margin
```

## Guardrail 2 — Theme/policy/beta rows route to local 4B when the bridge is absent

Counts:

```text
stage2_false_positive_bridge_gap_count = 16
theme_policy_proxy_bridge_gap_count = 33
early_MAE_30D <= -20% count = 1
MAE_90D <= -20% count = 10
MAE_180D <= -25% count = 14
post_peak_drawdown <= -35% count = 20
high_MFE_then_drawdown count = 15
```

Worst false-positive rows:

```text
R3 / C11_BATTERY_ORDERBOOK_RERATING / 006110 삼아알미늄 — counterexample_orderbook_material_beta_local4b: MFE180 34.57%, MAE180 -54.22%, DD -65.98%, action=stage2_false_positive_local_4b_watch
R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 407400 꿈비 — counterexample_babyproduct_policy_theme_local4b: MFE180 18.64%, MAE180 -52.54%, DD -60.0%, action=stage2_false_positive_local_4b_watch
R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH / 322310 오로스테크놀로지 — counterexample_equipment_theme_local4b: MFE180 31.24%, MAE180 -51.27%, DD -62.87%, action=stage2_false_positive_local_4b_watch
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 010100 한국무브넥스 — counterexample_auto_parts_theme_local4b: MFE180 24.64%, MAE180 -49.45%, DD -59.44%, action=stage2_false_positive_local_4b_watch
R8 / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE / 363260 모비데이즈 — counterexample_post_ca_adtech_theme_local4b: MFE180 10.92%, MAE180 -48.84%, DD -53.88%, action=stage2_false_positive_local_4b_watch
R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 159580 제로투세븐 — counterexample_low_birth_policy_beta_local4b: MFE180 27.64%, MAE180 -43.46%, DD -55.7%, action=stage2_false_positive_local_4b_watch
R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / 099190 아이센스 — counterexample_CGM_reimbursement_beta_local4b: MFE180 4.71%, MAE180 -40.49%, DD -43.17%, action=stage2_false_positive_local_4b_watch
R1 / C01_ORDER_BACKLOG_MARGIN_BRIDGE / 100090 SK오션플랜트 — counterexample_offshore_orderbook_beta_local4b: MFE180 5.27%, MAE180 -33.85%, DD -37.16%, action=stage2_false_positive_local_4b_watch
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 161390 한국타이어앤테크놀로지 — counterexample_tire_mix_margin_local4b: MFE180 23.63%, MAE180 -30.86%, DD -44.08%, action=stage2_false_positive_local_4b_watch
R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / 043150 바텍 — counterexample_dental_device_export_beta_local4b: MFE180 0.0%, MAE180 -30.46%, DD -30.46%, action=stage2_false_positive_local_4b_watch
R4 / C15_MATERIAL_SPREAD_SUPERCYCLE / 012800 대창 — counterexample_copper_spread_beta_local4b: MFE180 57.82%, MAE180 -25.17%, DD -52.59%, action=stage2_false_positive_local_4b_watch
R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 030210 다올투자증권 — counterexample_brokerage_valueup_beta_local4b: MFE180 10.44%, MAE180 -22.43%, DD -29.76%, action=stage2_false_positive_bridge_gap_watch
```

Worst MAE rows across all roles:

```text
R3 / C11_BATTERY_ORDERBOOK_RERATING / 006110 삼아알미늄 — counterexample_orderbook_material_beta_local4b: MFE180 34.57%, MAE180 -54.22%, DD -65.98%, action=stage2_false_positive_local_4b_watch
R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 407400 꿈비 — counterexample_babyproduct_policy_theme_local4b: MFE180 18.64%, MAE180 -52.54%, DD -60.0%, action=stage2_false_positive_local_4b_watch
R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH / 322310 오로스테크놀로지 — counterexample_equipment_theme_local4b: MFE180 31.24%, MAE180 -51.27%, DD -62.87%, action=stage2_false_positive_local_4b_watch
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 010100 한국무브넥스 — counterexample_auto_parts_theme_local4b: MFE180 24.64%, MAE180 -49.45%, DD -59.44%, action=stage2_false_positive_local_4b_watch
R8 / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE / 363260 모비데이즈 — counterexample_post_ca_adtech_theme_local4b: MFE180 10.92%, MAE180 -48.84%, DD -53.88%, action=stage2_false_positive_local_4b_watch
R3 / C11_BATTERY_ORDERBOOK_RERATING / 002710 TCC스틸 — positive_with_later_4b_watch: MFE180 73.71%, MAE180 -45.4%, DD -68.57%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 159580 제로투세븐 — counterexample_low_birth_policy_beta_local4b: MFE180 27.64%, MAE180 -43.46%, DD -55.7%, action=stage2_false_positive_local_4b_watch
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / 002410 범양건영 — risk_positive_local4b_no_hard4c: MFE180 2.04%, MAE180 -43.41%, DD -44.54%, action=local_4b_watch_no_hard_4c
R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / 099190 아이센스 — counterexample_CGM_reimbursement_beta_local4b: MFE180 4.71%, MAE180 -40.49%, DD -43.17%, action=stage2_false_positive_local_4b_watch
R1 / C01_ORDER_BACKLOG_MARGIN_BRIDGE / 100090 SK오션플랜트 — counterexample_offshore_orderbook_beta_local4b: MFE180 5.27%, MAE180 -33.85%, DD -37.16%, action=stage2_false_positive_local_4b_watch
R4 / C15_MATERIAL_SPREAD_SUPERCYCLE / 025820 이구산업 — positive_with_later_4b_watch: MFE180 47.98%, MAE180 -33.3%, DD -54.93%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 161390 한국타이어앤테크놀로지 — counterexample_tire_mix_margin_local4b: MFE180 23.63%, MAE180 -30.86%, DD -44.08%, action=stage2_false_positive_local_4b_watch
R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / 043150 바텍 — counterexample_dental_device_export_beta_local4b: MFE180 0.0%, MAE180 -30.46%, DD -30.46%, action=stage2_false_positive_local_4b_watch
R4 / C15_MATERIAL_SPREAD_SUPERCYCLE / 012800 대창 — counterexample_copper_spread_beta_local4b: MFE180 57.82%, MAE180 -25.17%, DD -52.59%, action=stage2_false_positive_local_4b_watch
R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 030210 다올투자증권 — counterexample_brokerage_valueup_beta_local4b: MFE180 10.44%, MAE180 -22.43%, DD -29.76%, action=stage2_false_positive_bridge_gap_watch
```

## Guardrail 3 — High MFE with later drawdown is lifecycle, not permanent Green

High-MFE / drawdown rows:

```text
R3 / C11_BATTERY_ORDERBOOK_RERATING / 002710 TCC스틸 — positive_with_later_4b_watch: MFE180 73.71%, MAE180 -45.4%, DD -68.57%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R3 / C11_BATTERY_ORDERBOOK_RERATING / 006110 삼아알미늄 — counterexample_orderbook_material_beta_local4b: MFE180 34.57%, MAE180 -54.22%, DD -65.98%, action=stage2_false_positive_local_4b_watch
R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH / 322310 오로스테크놀로지 — counterexample_equipment_theme_local4b: MFE180 31.24%, MAE180 -51.27%, DD -62.87%, action=stage2_false_positive_local_4b_watch
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 010100 한국무브넥스 — counterexample_auto_parts_theme_local4b: MFE180 24.64%, MAE180 -49.45%, DD -59.44%, action=stage2_false_positive_local_4b_watch
R8 / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE / 237820 플레이디 — positive_with_later_4b_watch: MFE180 90.36%, MAE180 -16.25%, DD -56.0%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 159580 제로투세븐 — counterexample_low_birth_policy_beta_local4b: MFE180 27.64%, MAE180 -43.46%, DD -55.7%, action=stage2_false_positive_local_4b_watch
R4 / C15_MATERIAL_SPREAD_SUPERCYCLE / 025820 이구산업 — positive_with_later_4b_watch: MFE180 47.98%, MAE180 -33.3%, DD -54.93%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH / 232140 와이아이케이/와이씨 — positive_with_later_4b_watch: MFE180 264.29%, MAE180 -0.32%, DD -53.64%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 013990 아가방컴퍼니 — policy_lifecycle_positive_with_later_4b_watch: MFE180 70.95%, MAE180 -19.05%, DD -52.65%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R4 / C15_MATERIAL_SPREAD_SUPERCYCLE / 012800 대창 — counterexample_copper_spread_beta_local4b: MFE180 57.82%, MAE180 -25.17%, DD -52.59%, action=stage2_false_positive_local_4b_watch
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 161390 한국타이어앤테크놀로지 — counterexample_tire_mix_margin_local4b: MFE180 23.63%, MAE180 -30.86%, DD -44.08%, action=stage2_false_positive_local_4b_watch
R5 / C18_CONSUMER_EXPORT_CHANNEL_REORDER / 280360 롯데웰푸드 — positive_with_later_4b_watch: MFE180 68.15%, MAE180 -5.56%, DD -43.84%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH / 084370 유진테크 — positive_with_later_4b_watch: MFE180 73.91%, MAE180 -1.45%, DD -42.92%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R4 / C15_MATERIAL_SPREAD_SUPERCYCLE / 021050 서원 — counterexample_copper_alloy_theme_local4b: MFE180 51.0%, MAE180 -10.92%, DD -40.99%, action=stage2_false_positive_local_4b_watch
R8 / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE / 273060 와이즈버즈 — counterexample_ad_platform_beta_local4b: MFE180 30.35%, MAE180 -20.54%, DD -39.04%, action=stage2_false_positive_local_4b_watch
```

Correct treatment:

```text
high MFE + verified bridge = historical Stage2 can be valid
high MFE + bridge stale + post-peak drawdown = lifecycle local 4B
high MFE + no bridge = false Stage2 / local 4B
```

## Guardrail 4 — Controlled-MAE positives must be protected after source repair

R13 must not become a blunt blocker.  
The following controlled-MAE positives should be protected if non-price bridge evidence is repaired:

```text
R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH / 232140 와이아이케이/와이씨 — positive_with_later_4b_watch: MFE180 264.29%, MAE180 -0.32%, DD -53.64%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 064350 현대로템 — positive_with_later_4b_watch: MFE180 141.99%, MAE180 -4.09%, DD -11.47%, action=protect_stage2_after_source_repair
R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / 214450 파마리서치 — positive_with_later_4b_watch: MFE180 138.72%, MAE180 -1.1%, DD -11.13%, action=protect_stage2_after_source_repair
R1 / C01_ORDER_BACKLOG_MARGIN_BRIDGE / 329180 HD현대중공업 — positive_with_later_4b_watch: MFE180 94.66%, MAE180 -5.6%, DD -23.64%, action=protect_stage2_after_source_repair
R11 / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG / 003570 SNT다이내믹스 — positive_with_later_4b_watch: MFE180 93.02%, MAE180 -0.62%, DD -15.07%, action=protect_stage2_after_source_repair
R3 / C11_BATTERY_ORDERBOOK_RERATING / 078600 대주전자재료 — positive_with_later_4b_watch: MFE180 84.07%, MAE180 -0.28%, DD -30.91%, action=protect_stage2_after_source_repair
R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH / 084370 유진테크 — positive_with_later_4b_watch: MFE180 73.91%, MAE180 -1.45%, DD -42.92%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R1 / C01_ORDER_BACKLOG_MARGIN_BRIDGE / 010140 삼성중공업 — positive_with_later_4b_watch: MFE180 68.91%, MAE180 -2.34%, DD -23.29%, action=protect_stage2_after_source_repair
R5 / C18_CONSUMER_EXPORT_CHANNEL_REORDER / 280360 롯데웰푸드 — positive_with_later_4b_watch: MFE180 68.15%, MAE180 -5.56%, DD -43.84%, action=stage2_after_source_repair_but_require_lifecycle_4b_after_peak
R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 175330 JB금융지주 — positive_with_later_lifecycle_watch: MFE180 62.41%, MAE180 0.0%, DD -7.43%, action=protect_stage2_after_source_repair
R11 / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG / 272210 한화시스템 — positive_with_later_4b_watch: MFE180 52.44%, MAE180 -2.54%, DD -29.36%, action=protect_stage2_after_source_repair
R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 138930 BNK금융지주 — positive_slow_with_sharecount_validation: MFE180 37.32%, MAE180 -2.79%, DD -12.57%, action=protect_stage2_after_source_repair
```

## Guardrail 5 — Policy event rows require direct beneficiary economics

Loop 77 includes low-birth/childcare policy and policy-defense linkage.  
The rule is not simply “policy headline rose.”

```text
policy headline
→ direct beneficiary mapping
→ direct order/demand/sell-through/reorder/backlog
→ margin or revenue bridge
→ only then Stage2
```

Rows requiring this guardrail are:

```text
R11 C03 defense framework rows: SNT다이내믹스, 한화시스템, 퍼스텍
R12 C31 low-birth/childcare rows: 아가방컴퍼니, 제로투세븐, 꿈비
```

## Guardrail 6 — Hard 4C remains non-price evidence based

No loop 77 row justifies price-only hard 4C.

```text
hard_4c_price_only_allowed_count = 0
```

Hard 4C requires non-price thesis break evidence:

```text
default / refinancing failure / court rehabilitation
contract cancellation / customer loss / order cut
clinical or regulatory failure
policy reversal / project cancellation
capital buffer break / covenant breach
insolvency / solvency break
```

C30 rows are the clearest boundary:

```text
002410 범양건영 = high-MAE local 4B, not price-only hard 4C
047040 대우건설 = large-cap/buffered RiskWatch no-hard-4C boundary
003070 코오롱글로벌 = recovery-spike RiskWatch no-hard-4C boundary
```

## Guardrail 7 — Validation queues

Share-count validation queue:

```text
R6:138930:BNK금융지주
R6:175330:JB금융지주
R7:099190:아이센스
R7:214450:파마리서치
```

Post-corporate-action validation queue:

```text
R8:363260:모비데이즈
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
  "loop": 77,
  "axis": "stage2_bridge_requirement_local4b_no_hard4c_policy_theme_beta_guardrail",
  "decision": "hold_for_coding_agent_validation",
  "do_not_propose_new_weight_delta": true,
  "candidate_rules": [
    "Stage2 requires archetype-specific non-price bridge evidence; MFE alone is not Green.",
    "Theme/policy/beta rows without direct order, backlog, call-off, sell-through, ROAS, adoption, capital-return, reimbursement, direct-demand, margin, or delivery bridge should be capped.",
    "Emit local 4B-watch when bridge is missing/stale and MAE_30D <= -20%, MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35%.",
    "Protect controlled-MAE positives after source repair when MFE_180D >= 20% and MAE_180D > -10%, but add lifecycle 4B after peak if bridge evidence fades.",
    "Policy-event rows need direct beneficiary mapping and direct economic transmission, not just headline sensitivity.",
    "C30 hard 4C remains evidence-based; price-only MAE/drawdown is not default/refinancing/solvency proof.",
    "Share-count and post-corporate-action validation block runtime ingestion until verified."
  ],
  "high_priority_false_positive_symbols": [
    "R3:006110:삼아알미늄",
    "R12:407400:꿈비",
    "R2:322310:오로스테크놀로지",
    "R9:010100:한국무브넥스",
    "R8:363260:모비데이즈",
    "R12:159580:제로투세븐",
    "R7:099190:아이센스",
    "R1:100090:SK오션플랜트",
    "R9:161390:한국타이어앤테크놀로지",
    "R7:043150:바텍",
    "R4:012800:대창",
    "R6:030210:다올투자증권"
  ],
  "protect_controlled_positive_symbols": [
    "R2:232140:와이아이케이/와이씨",
    "R9:064350:현대로템",
    "R7:214450:파마리서치",
    "R1:329180:HD현대중공업",
    "R11:003570:SNT다이내믹스",
    "R3:078600:대주전자재료",
    "R2:084370:유진테크",
    "R1:010140:삼성중공업",
    "R5:280360:롯데웰푸드",
    "R6:175330:JB금융지주",
    "R11:272210:한화시스템",
    "R6:138930:BNK금융지주"
  ],
  "high_MFE_lifecycle_watch_symbols": [
    "R3:002710:TCC스틸",
    "R3:006110:삼아알미늄",
    "R2:322310:오로스테크놀로지",
    "R9:010100:한국무브넥스",
    "R8:237820:플레이디",
    "R12:159580:제로투세븐",
    "R4:025820:이구산업",
    "R2:232140:와이아이케이/와이씨",
    "R12:013990:아가방컴퍼니",
    "R4:012800:대창",
    "R9:161390:한국타이어앤테크놀로지",
    "R5:280360:롯데웰푸드",
    "R2:084370:유진테크",
    "R4:021050:서원",
    "R8:273060:와이즈버즈"
  ],
  "share_count_validation_symbols": [
    "R6:138930:BNK금융지주",
    "R6:175330:JB금융지주",
    "R7:099190:아이센스",
    "R7:214450:파마리서치"
  ],
  "post_corporate_action_validation_symbols": [
    "R8:363260:모비데이즈"
  ]
}
```

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "validation_status": "usable_for_R13_cross_case_checkpoint", "source_round_files": ["e2r_stock_web_v12_residual_round_R1_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "e2r_stock_web_v12_residual_round_R2_loop_77_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "e2r_stock_web_v12_residual_round_R3_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "e2r_stock_web_v12_residual_round_R4_loop_77_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "e2r_stock_web_v12_residual_round_R5_loop_77_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "e2r_stock_web_v12_residual_round_R6_loop_77_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "e2r_stock_web_v12_residual_round_R7_loop_77_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "e2r_stock_web_v12_residual_round_R8_loop_77_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "e2r_stock_web_v12_residual_round_R9_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "e2r_stock_web_v12_residual_round_R10_loop_77_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "e2r_stock_web_v12_residual_round_R11_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "e2r_stock_web_v12_residual_round_R12_loop_77_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"]}
```

### R13 cross-case rows

```jsonl
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "source_case_id": "R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN", "source_trigger_id": "TRG_R1L77-C01-010140-SAMSUNG-HI-SHIPBUILDING-BACKLOG-MARGIN", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "symbol": "010140", "company_name": "삼성중공업", "trigger_type": "Stage2-Actionable-ShipbuildingOrderbookMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7270.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 29.16, "MFE_90D_pct": 41.68, "MFE_180D_pct": 68.91, "MAE_30D_pct": -2.34, "MAE_90D_pct": -2.34, "MAE_180D_pct": -2.34, "peak_date": "2024-07-26", "peak_price": 12280.0, "drawdown_after_peak_pct": -23.29, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "source_case_id": "R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE", "source_trigger_id": "TRG_R1L77-C01-100090-SK-OCEANPLANT-OFFSHORE-ORDERBOOK-BETA-FADE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "symbol": "100090", "company_name": "SK오션플랜트", "trigger_type": "Stage2-FalsePositive / OffshorePlantOrderbookBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 15570.0, "trigger_outcome_label": "counterexample_offshore_orderbook_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 5.27, "MFE_90D_pct": 5.27, "MFE_180D_pct": 5.27, "MAE_30D_pct": -17.66, "MAE_90D_pct": -20.1, "MAE_180D_pct": -33.85, "peak_date": "2024-02-16", "peak_price": 16390.0, "drawdown_after_peak_pct": -37.16, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "source_case_id": "R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN", "source_trigger_id": "TRG_R1L77-C01-329180-HD-HYUNDAI-HI-SHIPBUILDING-ORDERBOOK-MARGIN", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_OFFSHORE_ORDERBOOK_MIX_MARGIN_BRIDGE_VS_OFFSHORE_THEME_BACKLOG_FADE", "symbol": "329180", "company_name": "HD현대중공업", "trigger_type": "Stage2-Actionable-LargeShipbuildingOrderbookMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 114300.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 11.81, "MFE_90D_pct": 38.67, "MFE_180D_pct": 94.66, "MAE_30D_pct": -5.6, "MAE_90D_pct": -5.6, "MAE_180D_pct": -5.6, "peak_date": "2024-08-09", "peak_price": 222500.0, "drawdown_after_peak_pct": -23.64, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_77_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_case_id": "R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "source_trigger_id": "TRG_R2L77-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "symbol": "084370", "company_name": "유진테크", "trigger_type": "Stage2-Actionable-DepositionEquipmentOrderRSBridgeWithLifecycle4B", "trigger_date": "2024-02-19", "entry_date": "2024-02-20", "entry_price": 34500.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 29.57, "MFE_90D_pct": 73.91, "MFE_180D_pct": 73.91, "MAE_30D_pct": -1.45, "MAE_90D_pct": -1.45, "MAE_180D_pct": -1.45, "peak_date": "2024-05-28", "peak_price": 60000.0, "drawdown_after_peak_pct": -42.92, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_77_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_case_id": "R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE", "source_trigger_id": "TRG_R2L77-C07-232140-YC-HBM-TESTER-ORDER-RS-LIFECYCLE", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "symbol": "232140", "company_name": "와이아이케이/와이씨", "trigger_type": "Stage2-Actionable-HBMTesterOrderRelativeStrengthBridgeWithLifecycle4B", "trigger_date": "2024-04-16", "entry_date": "2024-04-17", "entry_price": 6300.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 180.32, "MFE_90D_pct": 264.29, "MFE_180D_pct": 264.29, "MAE_30D_pct": -0.32, "MAE_90D_pct": -0.32, "MAE_180D_pct": -0.32, "peak_date": "2024-06-13", "peak_price": 22950.0, "drawdown_after_peak_pct": -53.64, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_77_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_case_id": "R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE", "source_trigger_id": "TRG_R2L77-C07-322310-AUROS-METROLOGY-EQUIPMENT-THEME-FADE", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TESTER_DEPOSITION_METROLOGY_EQUIPMENT_ORDER_RS_BRIDGE_VS_EQUIPMENT_THEME_FADE", "symbol": "322310", "company_name": "오로스테크놀로지", "trigger_type": "Stage2-FalsePositive / MetrologyEquipmentThemeBetaFade", "trigger_date": "2024-01-23", "entry_date": "2024-01-24", "entry_price": 31050.0, "trigger_outcome_label": "counterexample_equipment_theme_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 31.24, "MFE_90D_pct": 31.24, "MFE_180D_pct": 31.24, "MAE_30D_pct": -14.01, "MAE_90D_pct": -22.22, "MAE_180D_pct": -51.27, "peak_date": "2024-02-27", "peak_price": 40750.0, "drawdown_after_peak_pct": -62.87, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "source_case_id": "R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE", "source_trigger_id": "TRG_R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "symbol": "002710", "company_name": "TCC스틸", "trigger_type": "Stage2-Actionable-BatteryCanMaterialOrderbookBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 49450.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 73.71, "MFE_90D_pct": 73.71, "MFE_180D_pct": 73.71, "MAE_30D_pct": -3.94, "MAE_90D_pct": -10.21, "MAE_180D_pct": -45.4, "peak_date": "2024-02-21", "peak_price": 85900.0, "drawdown_after_peak_pct": -68.57, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "source_case_id": "R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE", "source_trigger_id": "TRG_R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "symbol": "006110", "company_name": "삼아알미늄", "trigger_type": "Stage2-FalsePositive / AluminumFoilOrderbookThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 86500.0, "trigger_outcome_label": "counterexample_orderbook_material_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 34.57, "MFE_90D_pct": 34.57, "MFE_180D_pct": 34.57, "MAE_30D_pct": -7.28, "MAE_90D_pct": -40.35, "MAE_180D_pct": -54.22, "peak_date": "2024-02-21", "peak_price": 116400.0, "drawdown_after_peak_pct": -65.98, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "source_case_id": "R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN", "source_trigger_id": "TRG_R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "symbol": "078600", "company_name": "대주전자재료", "trigger_type": "Stage2-Actionable-SiliconAnodeCustomerOrderbookMarginBridge", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 70300.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 45.09, "MFE_90D_pct": 45.09, "MFE_180D_pct": 84.07, "MAE_30D_pct": -0.28, "MAE_90D_pct": -0.28, "MAE_180D_pct": -0.28, "peak_date": "2024-08-16", "peak_price": 129400.0, "drawdown_after_peak_pct": -30.91, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_77_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "source_case_id": "R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE", "source_trigger_id": "TRG_R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "symbol": "012800", "company_name": "대창", "trigger_type": "Stage2-FalsePositive / CopperBrassSpreadThemeFade", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 1470.0, "trigger_outcome_label": "counterexample_copper_spread_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 57.82, "MFE_90D_pct": 57.82, "MFE_180D_pct": 57.82, "MAE_30D_pct": -0.88, "MAE_90D_pct": -25.17, "MAE_180D_pct": -25.17, "peak_date": "2024-05-21", "peak_price": 2320.0, "drawdown_after_peak_pct": -52.59, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_77_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "source_case_id": "R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE", "source_trigger_id": "TRG_R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "symbol": "021050", "company_name": "서원", "trigger_type": "Stage2-FalsePositive / CopperAlloySpreadThemeFade", "trigger_date": "2024-04-12", "entry_date": "2024-04-15", "entry_price": 1328.0, "trigger_outcome_label": "counterexample_copper_alloy_theme_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 51.0, "MFE_90D_pct": 51.0, "MFE_180D_pct": 51.0, "MAE_30D_pct": -1.2, "MAE_90D_pct": -10.92, "MAE_180D_pct": -10.92, "peak_date": "2024-05-21", "peak_price": 2005.0, "drawdown_after_peak_pct": -40.99, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_77_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "source_case_id": "R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE", "source_trigger_id": "TRG_R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "symbol": "025820", "company_name": "이구산업", "trigger_type": "Stage2-Actionable-CopperSpreadInventoryMarginBridgeWithLifecycle4B", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 5690.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 47.98, "MFE_90D_pct": 47.98, "MFE_180D_pct": 47.98, "MAE_30D_pct": -4.04, "MAE_90D_pct": -33.3, "MAE_180D_pct": -33.3, "peak_date": "2024-05-20", "peak_price": 8420.0, "drawdown_after_peak_pct": -54.93, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_77_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE", "source_trigger_id": "TRG_R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "symbol": "097950", "company_name": "CJ제일제당", "trigger_type": "Stage2-SlowPositive-KFoodGlobalChannelMarginBridgeWithLifecycle4B", "trigger_date": "2024-03-29", "entry_date": "2024-04-01", "entry_price": 295000.0, "trigger_outcome_label": "positive_slow_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 10.85, "MFE_90D_pct": 32.54, "MFE_180D_pct": 32.54, "MAE_30D_pct": -3.39, "MAE_90D_pct": -3.39, "MAE_180D_pct": -9.32, "peak_date": "2024-07-31", "peak_price": 391000.0, "drawdown_after_peak_pct": -31.59, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_77_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE", "source_trigger_id": "TRG_R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "symbol": "271560", "company_name": "오리온", "trigger_type": "Stage2-FalsePositive / GlobalDistributionBetaFade", "trigger_date": "2024-04-01", "entry_date": "2024-04-02", "entry_price": 95400.0, "trigger_outcome_label": "counterexample_global_channel_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 3.35, "MFE_90D_pct": 6.39, "MFE_180D_pct": 7.86, "MAE_30D_pct": -5.56, "MAE_90D_pct": -6.92, "MAE_180D_pct": -14.26, "peak_date": "2024-10-11", "peak_price": 102900.0, "drawdown_after_peak_pct": -18.56, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_bridge_gap_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_77_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER", "source_trigger_id": "TRG_R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "symbol": "280360", "company_name": "롯데웰푸드", "trigger_type": "Stage2-Actionable-GlobalSnackChannelReorderMarginBridgeWithLifecycle4B", "trigger_date": "2024-04-18", "entry_date": "2024-04-19", "entry_price": 124000.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 22.18, "MFE_90D_pct": 68.15, "MFE_180D_pct": 68.15, "MAE_30D_pct": -0.73, "MAE_90D_pct": -0.73, "MAE_180D_pct": -5.56, "peak_date": "2024-06-18", "peak_price": 208500.0, "drawdown_after_peak_pct": -43.84, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_77_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE", "source_trigger_id": "TRG_R6L77-C21-030210-DAOL-SECURITIES-BROKERAGE-VALUEUP-BETA-FADE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "symbol": "030210", "company_name": "다올투자증권", "trigger_type": "Stage2-FalsePositive / BrokerageValueupBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3545.0, "trigger_outcome_label": "counterexample_brokerage_valueup_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 10.16, "MFE_90D_pct": 10.44, "MFE_180D_pct": 10.44, "MAE_30D_pct": -2.12, "MAE_90D_pct": -13.96, "MAE_180D_pct": -22.43, "peak_date": "2024-03-08", "peak_price": 3915.0, "drawdown_after_peak_pct": -29.76, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_bridge_gap_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_77_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "source_trigger_id": "TRG_R6L77-C21-138930-BNK-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "symbol": "138930", "company_name": "BNK금융지주", "trigger_type": "Stage2-SlowPositive-RegionalBankROEPBRCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7530.0, "trigger_outcome_label": "positive_slow_with_sharecount_validation", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 7.17, "MFE_90D_pct": 11.69, "MFE_180D_pct": 37.32, "MAE_30D_pct": -0.8, "MAE_90D_pct": -2.79, "MAE_180D_pct": -2.79, "peak_date": "2024-08-26", "peak_price": 10340.0, "drawdown_after_peak_pct": -12.57, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": true, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_77_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "source_trigger_id": "TRG_R6L77-C21-175330-JB-FINANCIAL-ROE-PBR-CAPITAL-RETURN", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_BETA_FADE", "symbol": "175330", "company_name": "JB금융지주", "trigger_type": "Stage2-Actionable-RegionalBankROEPBRCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11520.0, "trigger_outcome_label": "positive_with_later_lifecycle_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 20.92, "MFE_90D_pct": 22.4, "MFE_180D_pct": 62.41, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-10-25", "peak_price": 18710.0, "drawdown_after_peak_pct": -7.43, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": true, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_77_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE", "source_trigger_id": "TRG_R7L77-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-BETA-FADE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "symbol": "043150", "company_name": "바텍", "trigger_type": "Stage2-FalsePositive / DentalImagingExportBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32500.0, "trigger_outcome_label": "counterexample_dental_device_export_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MAE_30D_pct": -7.85, "MAE_90D_pct": -8.62, "MAE_180D_pct": -30.46, "peak_date": "2024-02-01", "peak_price": 32500.0, "drawdown_after_peak_pct": -30.46, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_77_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE", "source_trigger_id": "TRG_R7L77-C25-099190-ISENS-CGM-REIMBURSEMENT-EXPORT-BETA-FADE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "symbol": "099190", "company_name": "아이센스", "trigger_type": "Stage2-FalsePositive / CGMReimbursementExportBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 24400.0, "trigger_outcome_label": "counterexample_CGM_reimbursement_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 4.71, "MFE_90D_pct": 4.71, "MFE_180D_pct": 4.71, "MAE_30D_pct": -18.03, "MAE_90D_pct": -22.62, "MAE_180D_pct": -40.49, "peak_date": "2024-02-02", "peak_price": 25550.0, "drawdown_after_peak_pct": -43.17, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": true, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_77_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN", "source_trigger_id": "TRG_R7L77-C25-214450-PHARMARESEARCH-AESTHETIC-MEDDEVICE-EXPORT-MARGIN", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "AESTHETIC_CGM_DENTAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_DEVICE_THEME_FADE", "symbol": "214450", "company_name": "파마리서치", "trigger_type": "Stage2-Actionable-AestheticMedicalDeviceExportMarginBridgeWithLifecycle4B", "trigger_date": "2024-03-29", "entry_date": "2024-04-01", "entry_price": 99700.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 49.95, "MFE_90D_pct": 57.87, "MFE_180D_pct": 138.72, "MAE_30D_pct": -1.1, "MAE_90D_pct": -1.1, "MAE_180D_pct": -1.1, "peak_date": "2024-10-22", "peak_price": 238000.0, "drawdown_after_peak_pct": -11.13, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": true, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_77_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_case_id": "R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE", "source_trigger_id": "TRG_R8L77-C26-237820-PLAYD-ADTECH-ROAS-BUDGET-OPERATING-LEVERAGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "symbol": "237820", "company_name": "플레이디", "trigger_type": "Stage2-Actionable-AdTechROASBudgetOperatingLeverageBridgeWithLifecycle4B", "trigger_date": "2024-02-01", "entry_date": "2024-02-02", "entry_price": 5600.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 90.36, "MFE_90D_pct": 90.36, "MFE_180D_pct": 90.36, "MAE_30D_pct": -0.54, "MAE_90D_pct": -0.54, "MAE_180D_pct": -16.25, "peak_date": "2024-03-06", "peak_price": 10660.0, "drawdown_after_peak_pct": -56.0, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_77_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_case_id": "R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE", "source_trigger_id": "TRG_R8L77-C26-273060-WISEBIRDS-AD-PLATFORM-THEME-FADE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "symbol": "273060", "company_name": "와이즈버즈", "trigger_type": "Stage2-FalsePositive / AdPlatformROASBudgetThemeFade", "trigger_date": "2024-02-01", "entry_date": "2024-02-02", "entry_price": 1407.0, "trigger_outcome_label": "counterexample_ad_platform_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 30.35, "MFE_90D_pct": 30.35, "MFE_180D_pct": 30.35, "MAE_30D_pct": -6.11, "MAE_90D_pct": -18.41, "MAE_180D_pct": -20.54, "peak_date": "2024-03-06", "peak_price": 1834.0, "drawdown_after_peak_pct": -39.04, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_77_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_case_id": "R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE", "source_trigger_id": "TRG_R8L77-C26-363260-MOBIDAYS-POST-CA-ADTECH-THEME-FADE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "ADTECH_MEDIA_BUYING_PLATFORM_ROAS_BUDGET_OPERATING_LEVERAGE_BRIDGE_VS_AD_THEME_FADE", "symbol": "363260", "company_name": "모비데이즈", "trigger_type": "Stage2-FalsePositive / PostCAAdTechThemeFade", "trigger_date": "2024-05-24", "entry_date": "2024-05-27", "entry_price": 2885.0, "trigger_outcome_label": "counterexample_post_ca_adtech_theme_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 10.92, "MFE_90D_pct": 10.92, "MFE_180D_pct": 10.92, "MAE_30D_pct": -25.48, "MAE_90D_pct": -43.74, "MAE_180D_pct": -48.84, "peak_date": "2024-05-29", "peak_price": 3200.0, "drawdown_after_peak_pct": -53.88, "guardrail_flags": {"early_MAE_30D_le_-20": true, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": true}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE", "source_trigger_id": "TRG_R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "symbol": "010100", "company_name": "한국무브넥스", "trigger_type": "Stage2-FalsePositive / AutoPartsVolumeMarginThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6330.0, "trigger_outcome_label": "counterexample_auto_parts_theme_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 24.64, "MFE_90D_pct": 24.64, "MFE_180D_pct": 24.64, "MAE_30D_pct": -11.53, "MAE_90D_pct": -24.17, "MAE_180D_pct": -49.45, "peak_date": "2024-02-02", "peak_price": 7890.0, "drawdown_after_peak_pct": -59.44, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN", "source_trigger_id": "TRG_R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "symbol": "064350", "company_name": "현대로템", "trigger_type": "Stage2-Actionable-RailMobilityOrderbookMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 28100.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 22.78, "MFE_90D_pct": 54.63, "MFE_180D_pct": 141.99, "MAE_30D_pct": -4.09, "MAE_90D_pct": -4.09, "MAE_180D_pct": -4.09, "peak_date": "2024-10-18", "peak_price": 68000.0, "drawdown_after_peak_pct": -11.47, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_77_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE", "source_trigger_id": "TRG_R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "trigger_type": "Stage2-FalsePositive / TireOEMReplacementMixMarginFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 51200.0, "trigger_outcome_label": "counterexample_tire_mix_margin_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 16.41, "MFE_90D_pct": 23.63, "MFE_180D_pct": 23.63, "MAE_30D_pct": -6.35, "MAE_90D_pct": -17.68, "MAE_180D_pct": -30.86, "peak_date": "2024-04-16", "peak_price": 63300.0, "drawdown_after_peak_pct": -44.08, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_77_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B", "source_trigger_id": "TRG_R10L77-C30-002410-BEOMYANG-BUILDER-FINANCING-HIGH-MAE-LOCAL4B", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "symbol": "002410", "company_name": "범양건영", "trigger_type": "Stage4B-Local-SmallBuilderFinancingHighMAE", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1767.0, "trigger_outcome_label": "risk_positive_local4b_no_hard4c", "role_bucket": "risk_positive", "MFE_30D_pct": 2.04, "MFE_90D_pct": 2.04, "MFE_180D_pct": 2.04, "MAE_30D_pct": -5.66, "MAE_90D_pct": -22.64, "MAE_180D_pct": -43.41, "peak_date": "2024-02-02", "peak_price": 1803.0, "drawdown_after_peak_pct": -44.54, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": false, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "local_4b_watch_no_hard_4c", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_77_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C", "source_trigger_id": "TRG_R10L77-C30-003070-KOLON-GLOBAL-PF-RISKWATCH-RECOVERY-NO-HARD4C", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "symbol": "003070", "company_name": "코오롱글로벌", "trigger_type": "RiskWatch-BuilderPFRecoveryNoHard4CWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 9370.0, "trigger_outcome_label": "overbearish_counterexample_recovery_no_hard4c", "role_bucket": "riskwatch_boundary", "MFE_30D_pct": 9.28, "MFE_90D_pct": 9.28, "MFE_180D_pct": 37.57, "MAE_30D_pct": -3.95, "MAE_90D_pct": -9.5, "MAE_180D_pct": -9.5, "peak_date": "2024-08-27", "peak_price": 12890.0, "drawdown_after_peak_pct": -32.82, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": false, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "riskwatch_no_hard_4c_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_77_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C", "source_trigger_id": "TRG_R10L77-C30-047040-DAEWOO-E&C-LARGECAP-PF-RISKWATCH-NO-HARD4C", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_BUILDER_HIGH_MAE_LOCAL4B_VS_LARGECAP_BUFFERED_NO_HARD4C", "symbol": "047040", "company_name": "대우건설", "trigger_type": "RiskWatch-LargeCapBuilderPFBufferNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3910.0, "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "role_bucket": "riskwatch_boundary", "MFE_30D_pct": 5.37, "MFE_90D_pct": 5.37, "MFE_180D_pct": 10.49, "MAE_30D_pct": -0.13, "MAE_90D_pct": -6.01, "MAE_180D_pct": -9.34, "peak_date": "2024-08-26", "peak_price": 4320.0, "drawdown_after_peak_pct": -12.85, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": false, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "riskwatch_no_hard_4c_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_case_id": "R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG", "source_trigger_id": "TRG_R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "symbol": "003570", "company_name": "SNT다이내믹스", "trigger_type": "Stage2-Actionable-DefenseDrivetrainExportBacklogBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 14610.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 31.69, "MFE_90D_pct": 44.42, "MFE_180D_pct": 93.02, "MAE_30D_pct": -0.62, "MAE_90D_pct": -0.62, "MAE_180D_pct": -0.62, "peak_date": "2024-10-23", "peak_price": 28200.0, "drawdown_after_peak_pct": -15.07, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_case_id": "R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE", "source_trigger_id": "TRG_R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "symbol": "010820", "company_name": "퍼스텍", "trigger_type": "Stage2-FalsePositive / DefenseUnmannedThemeBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3200.0, "trigger_outcome_label": "counterexample_defense_theme_local4b_watch", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 8.44, "MFE_90D_pct": 10.94, "MFE_180D_pct": 22.5, "MAE_30D_pct": -0.63, "MAE_90D_pct": -13.75, "MAE_180D_pct": -20.16, "peak_date": "2024-10-24", "peak_price": 3920.0, "drawdown_after_peak_pct": -21.17, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": false, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_bridge_gap_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_77_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_case_id": "R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "source_trigger_id": "TRG_R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "symbol": "272210", "company_name": "한화시스템", "trigger_type": "Stage2-Actionable-DefenseElectronicsExportBacklogBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 15350.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 24.95, "MFE_90D_pct": 37.46, "MFE_180D_pct": 52.44, "MAE_30D_pct": -2.54, "MAE_90D_pct": -2.54, "MAE_180D_pct": -2.54, "peak_date": "2024-07-30", "peak_price": 23400.0, "drawdown_after_peak_pct": -29.36, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": true, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "protect_stage2_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_77_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE", "source_trigger_id": "TRG_R12L77-C31-013990-AGABANG-LOW-BIRTH-CHILDCARE-POLICY-LIFECYCLE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "symbol": "013990", "company_name": "아가방컴퍼니", "trigger_type": "Stage2-PolicyLifecycle-LowBirthChildcareDirectDemandBridgeWithLocal4B", "trigger_date": "2024-01-02", "entry_date": "2024-01-03", "entry_price": 4200.0, "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "role_bucket": "positive_or_lifecycle", "MFE_30D_pct": 70.95, "MFE_90D_pct": 70.95, "MFE_180D_pct": 70.95, "MAE_30D_pct": -1.67, "MAE_90D_pct": -1.67, "MAE_180D_pct": -19.05, "peak_date": "2024-01-18", "peak_price": 7180.0, "drawdown_after_peak_pct": -52.65, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_after_source_repair_but_require_lifecycle_4b_after_peak", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_77_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE", "source_trigger_id": "TRG_R12L77-C31-159580-ZEROTOSEVEN-LOW-BIRTH-POLICY-THEME-FADE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "symbol": "159580", "company_name": "제로투세븐", "trigger_type": "Stage2-FalsePositive / LowBirthChildcarePolicyThemeFade", "trigger_date": "2024-01-02", "entry_date": "2024-01-03", "entry_price": 6730.0, "trigger_outcome_label": "counterexample_low_birth_policy_beta_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 27.64, "MFE_90D_pct": 27.64, "MFE_180D_pct": 27.64, "MAE_30D_pct": -3.71, "MAE_90D_pct": -19.47, "MAE_180D_pct": -43.46, "peak_date": "2024-01-18", "peak_price": 8590.0, "drawdown_after_peak_pct": -55.7, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": true, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "77", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_77_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE", "source_trigger_id": "TRG_R12L77-C31-407400-GGUMBI-LOW-BIRTH-BABYPRODUCT-THEME-FADE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "LOW_BIRTH_CHILDCARE_POLICY_DIRECT_DEMAND_BRIDGE_VS_THEME_FADE", "symbol": "407400", "company_name": "꿈비", "trigger_type": "Stage2-FalsePositive / BabyProductLowBirthPolicyThemeFade", "trigger_date": "2024-01-02", "entry_date": "2024-01-03", "entry_price": 12390.0, "trigger_outcome_label": "counterexample_babyproduct_policy_theme_local4b", "role_bucket": "stage2_false_positive", "MFE_30D_pct": 18.64, "MFE_90D_pct": 18.64, "MFE_180D_pct": 18.64, "MAE_30D_pct": -18.89, "MAE_90D_pct": -35.92, "MAE_180D_pct": -52.54, "peak_date": "2024-01-03", "peak_price": 14700.0, "drawdown_after_peak_pct": -60.0, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "post_peak_drawdown_le_-25": true, "high_MFE_then_drawdown": false, "controlled_MAE_stage2_candidate": false, "theme_policy_proxy_bridge_gap": true, "tender_floor_or_event_lifecycle": false, "hard_4c_allowed_from_price_only": false, "source_repair_required": true, "share_count_validation_required": false, "post_corporate_action_validation_required": false}, "r13_guardrail_action": "stage2_false_positive_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
```

### R13 summary row

```jsonl
{"row_type": "r13_cross_summary", "round": "R13", "loop": 77, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "fine_archetype_id": "LOOP77_STAGE2_BRIDGE_LOCAL4B_NO_HARD4C_GUARDRAIL_CHECKPOINT", "selected_cross_case_count": 36, "source_rounds_covered": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_count": 12, "canonical_counts": {"C01_ORDER_BACKLOG_MARGIN_BRIDGE": 3, "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG": 3, "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH": 3, "C11_BATTERY_ORDERBOOK_RERATING": 3, "C15_MATERIAL_SPREAD_SUPERCYCLE": 3, "C18_CONSUMER_EXPORT_CHANNEL_REORDER": 3, "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN": 3, "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT": 3, "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE": 3, "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE": 3, "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK": 3, "C31_POLICY_SUBSIDY_LEGISLATION_EVENT": 3}, "role_counts": {"positive_or_lifecycle": 17, "stage2_false_positive": 16, "risk_positive": 1, "riskwatch_boundary": 2}, "stage2_false_positive_bridge_gap_count": 16, "risk_positive_local4b_count": 1, "riskwatch_or_overbearish_boundary_count": 2, "positive_or_lifecycle_count": 17, "early_MAE_30D_le_-20_count": 1, "high_MAE_90D_le_-20_count": 10, "high_MAE_180D_le_-25_count": 14, "post_peak_drawdown_le_-35_count": 20, "post_peak_drawdown_le_-25_count": 26, "high_MFE_then_drawdown_count": 15, "controlled_MAE_stage2_candidate_count": 13, "theme_policy_proxy_bridge_gap_count": 33, "tender_floor_or_event_lifecycle_count": 0, "share_count_validation_required_count": 4, "post_corporate_action_validation_required_count": 1, "source_repair_required_count": 36, "hard_4c_price_only_allowed_count": 0, "new_sector_positive_case_count": 0, "r13_decision": "guardrail_checkpoint_only", "r13_result": "do_not_change_runtime_weights_until_source_repair_and_validation"}
```

### R13 guardrail candidate row

```jsonl
{"row_type": "r13_guardrail_candidate", "round": "R13", "loop": 77, "axis": "stage2_bridge_requirement_local4b_no_hard4c_policy_theme_beta_guardrail", "decision": "hold_for_coding_agent_validation", "do_not_propose_new_weight_delta": true, "candidate_rules": ["Stage2 requires archetype-specific non-price bridge evidence; MFE alone is not Green.", "Theme/policy/beta rows without direct order, backlog, call-off, sell-through, ROAS, adoption, capital-return, reimbursement, direct-demand, margin, or delivery bridge should be capped.", "Emit local 4B-watch when bridge is missing/stale and MAE_30D <= -20%, MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35%.", "Protect controlled-MAE positives after source repair when MFE_180D >= 20% and MAE_180D > -10%, but add lifecycle 4B after peak if bridge evidence fades.", "Policy-event rows need direct beneficiary mapping and direct economic transmission, not just headline sensitivity.", "C30 hard 4C remains evidence-based; price-only MAE/drawdown is not default/refinancing/solvency proof.", "Share-count and post-corporate-action validation block runtime ingestion until verified."], "high_priority_false_positive_symbols": ["R3:006110:삼아알미늄", "R12:407400:꿈비", "R2:322310:오로스테크놀로지", "R9:010100:한국무브넥스", "R8:363260:모비데이즈", "R12:159580:제로투세븐", "R7:099190:아이센스", "R1:100090:SK오션플랜트", "R9:161390:한국타이어앤테크놀로지", "R7:043150:바텍", "R4:012800:대창", "R6:030210:다올투자증권"], "protect_controlled_positive_symbols": ["R2:232140:와이아이케이/와이씨", "R9:064350:현대로템", "R7:214450:파마리서치", "R1:329180:HD현대중공업", "R11:003570:SNT다이내믹스", "R3:078600:대주전자재료", "R2:084370:유진테크", "R1:010140:삼성중공업", "R5:280360:롯데웰푸드", "R6:175330:JB금융지주", "R11:272210:한화시스템", "R6:138930:BNK금융지주"], "high_MFE_lifecycle_watch_symbols": ["R3:002710:TCC스틸", "R3:006110:삼아알미늄", "R2:322310:오로스테크놀로지", "R9:010100:한국무브넥스", "R8:237820:플레이디", "R12:159580:제로투세븐", "R4:025820:이구산업", "R2:232140:와이아이케이/와이씨", "R12:013990:아가방컴퍼니", "R4:012800:대창", "R9:161390:한국타이어앤테크놀로지", "R5:280360:롯데웰푸드", "R2:084370:유진테크", "R4:021050:서원", "R8:273060:와이즈버즈"], "share_count_validation_symbols": ["R6:138930:BNK금융지주", "R6:175330:JB금융지주", "R7:099190:아이센스", "R7:214450:파마리서치"], "post_corporate_action_validation_symbols": ["R8:363260:모비데이즈"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": 77, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard", "corporate_action_validation_guard", "policy_direct_beneficiary_mapping_guard", "overbearish_no_hard4c_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": false, "canonical_archetype_rule_candidate": true, "narrative_summary": "Loop 77 cross-case review shows Stage2 false positives mostly come from theme/policy/beta rows without archetype-specific bridge evidence. R13 strengthens local 4B routing, controlled-positive protection, policy direct-beneficiary validation and no-hard-4C boundaries."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
source_round_files = R1~R12 loop 77 standalone MDs
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
All source loop-77 rows are still source_proxy_only / evidence_url_pending.
R13 is therefore a guardrail-shape checkpoint, not a runtime scoring patch.
Coding-agent promotion requires non-proxy evidence repair and share-count / corporate-action validation.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this R13 loop 77 cross-archetype residual research MD.

Do not patch production scoring blindly.
This file is a guardrail checkpoint only.

Candidate axis:
stage2_bridge_requirement_local4b_no_hard4c_policy_theme_beta_guardrail

Required checks before implementation:
1. Validate all R13 cross-case rows against their source R1~R12 loop 77 trigger rows.
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
8. Treat policy-event rows as valid only when direct beneficiary mapping and direct economic bridge are verified.
9. Do not convert local 4B into hard 4C without non-price thesis break evidence.
10. Run share-count and corporate-action validation for every cross row marked with those flags.
11. Emit before/after diagnostics and reject if the guardrail overblocks verified low-MAE positives.
```

---

## Final round state

```text
completed_round = R13
completed_loop = 77
next_round = R1
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

