# E2R Stock-Web v12 Residual Research — R13 Loop 75 / L10 / Cross-Archetype High-MAE Guardrail

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 75,
  "computed_next_round": "R1",
  "computed_next_loop": 76,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "fine_archetype_id": "LOOP75_HIGH_MAE_STAGE2_FALSE_POSITIVE_LOCAL4B_SOURCE_REPAIR_CHECKPOINT",
  "loop_objective": [
    "high_MAE_guardrail",
    "stage2_false_positive_review",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "delayed_positive_protection",
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
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R12 / loop 75.

Therefore:

```text
scheduled_round = R13
scheduled_loop = 75
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
computed_next_round = R1
computed_next_loop = 76
```

R13 is not a sector round.  
This file reuses the completed loop 75 R1~R12 trigger rows and compresses them into cross-archetype guardrails.

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
e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
e2r_stock_web_v12_residual_round_R4_loop_75_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
e2r_stock_web_v12_residual_round_R5_loop_75_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
e2r_stock_web_v12_residual_round_R6_loop_75_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
e2r_stock_web_v12_residual_round_R9_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
e2r_stock_web_v12_residual_round_R11_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

## Cross-case summary

```json
{
  "row_type": "r13_cross_summary",
  "round": "R13",
  "loop": 75,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "fine_archetype_id": "LOOP75_HIGH_MAE_STAGE2_FALSE_POSITIVE_LOCAL4B_SOURCE_REPAIR_CHECKPOINT",
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
  "role_counts": {
    "positive": 11,
    "counterexample": 19,
    "delayed_positive": 3,
    "riskwatch_boundary": 2,
    "risk_positive": 1
  },
  "stage2_false_positive_bridge_gap_count": 19,
  "risk_positive_local4b_count": 1,
  "riskwatch_or_overbearish_boundary_count": 2,
  "early_MAE_30D_le_-20_count": 3,
  "high_MAE_90D_le_-20_count": 9,
  "high_MAE_180D_le_-25_count": 18,
  "post_peak_drawdown_le_-35_count": 26,
  "high_MFE_then_drawdown_count": 17,
  "controlled_entry_MAE_positive_candidate_count": 10,
  "share_count_validation_required_count": 10,
  "source_repair_required_count": 36,
  "hard_4c_price_only_allowed_count": 0,
  "new_sector_positive_case_count": 0,
  "r13_decision": "guardrail_checkpoint_only",
  "r13_result": "do_not_change_runtime_weights_until_source_repair_and_validation"
}
```

## Main residual finding

Loop 75 repeats one mechanism across very different sectors:

```text
headline / policy / theme / value-up / contract attention
→ price MFE
→ source_proxy_only or stale bridge
→ MAE or post-peak drawdown
→ local 4B-watch
```

The safe rule is not “MFE means Green.”  
It is:

```text
MFE can validate tradability.
Only verified non-price bridge validates Stage2 durability.
```

## Guardrail 1 — Stage2 must have an archetype-specific bridge

Each archetype needs its own bridge:

```text
C04: nuclear project / O&M / I&C / instrumentation order
C06: AI/HBM customer capacity / order / utilization / ASP / margin
C12: battery customer contract / call-off / utilization / margin
C16: strategic-resource direct supply / processing / offtake / inventory / margin
C18: export channel / sell-through / reorder / product mix / margin
C21: ROE / capital buffer / dividend / buyback / treasury cancellation
C25: export/OEM channel / installed base / refill/reagent / reimbursement / margin
C28: ARR/license / contract renewal / paid-seat / retention / margin
C29: OEM volume / named program / mix / pricing / margin
C30: PF/orderbook/liquidity risk vs confirmed balance-sheet break
C31: policy direct beneficiary / paid demand / revenue / margin
C32: tender mechanics / minority economics / listed-entity beneficiary
```

## Guardrail 2 — High-MAE / drawdown should trigger local 4B-watch

Observed counts:

```text
early_MAE_30D <= -20% count = 3
MAE_90D <= -20% count = 9
MAE_180D <= -25% count = 18
post_peak_drawdown <= -35% count = 26
high_MFE_then_drawdown count = 17
```

Worst MAE false-positive rows:

```text
R3 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK / 361610 SK아이이테크놀로지 — counterexample_calloff_local4b: MFE180 10.08%, MAE180 -59.06%, DD -62.81%
R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 053290 NE능률 — counterexample_education_theme_local4b: MFE180 1.61%, MAE180 -55.73%, DD -56.43%
R4 / C16_STRATEGIC_RESOURCE_POLICY_SUPPLY / 011810 STX — counterexample_resource_trading_local4b: MFE180 13.66%, MAE180 -55.11%, DD -66.85%
R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 377300 카카오페이 — counterexample_digital_finance_beta_local4b: MFE180 24.12%, MAE180 -54.74%, DD -63.54%
R3 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK / 006110 삼아알미늄 — counterexample_calloff_local4b: MFE180 34.57%, MAE180 -54.22%, DD -70.79%
R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 133750 메가엠디 — counterexample_policy_proxy_local4b: MFE180 4.41%, MAE180 -53.14%, DD -55.12%
R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / 099190 아이센스 — counterexample_reimbursement_beta_local4b: MFE180 1.5%, MAE180 -49.85%, DD -50.59%
R2 / C06_HBM_MEMORY_CUSTOMER_CAPACITY / 222800 심텍 — counterexample: MFE180 14.45%, MAE180 -47.84%, DD -54.43%
```

High-MFE but dangerous lifecycle rows:

```text
R8 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION / 047560 이스트소프트 — counterexample_theme_spike_local4b_with_sharecount_validation: MFE180 227.0%, MAE180 -26.33%, DD -77.47%
R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 036560 영풍정밀/KZ정밀 — governance_lifecycle_positive_with_later_4b_watch: MFE180 201.31%, MAE180 -15.76%, DD -72.04%
R3 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK / 006110 삼아알미늄 — counterexample_calloff_local4b: MFE180 34.57%, MAE180 -54.22%, DD -70.79%
R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 377300 카카오페이 — counterexample_digital_finance_beta_local4b: MFE180 24.12%, MAE180 -54.74%, DD -63.54%
R2 / C06_HBM_MEMORY_CUSTOMER_CAPACITY / 007660 이수페타시스 — positive_with_later_4b_watch: MFE180 58.53%, MAE180 -33.01%, DD -57.75%
R3 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK / 020150 롯데에너지머티리얼즈 — positive_with_later_4b_watch: MFE180 57.44%, MAE180 -2.4%, DD -57.52%
R1 / C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY / 130660 한전산업 — positive_with_later_4b_watch: MFE180 121.59%, MAE180 -1.82%, DD -54.46%
R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 008930 한미사이언스 — counterexample_control_dispute_local4b_with_sharecount_validation: MFE180 21.25%, MAE180 -44.44%, DD -54.18%
R5 / C18_CONSUMER_EXPORT_CHANNEL_REORDER / 011150 CJ씨푸드 — counterexample_theme_spike_local4b: MFE180 145.16%, MAE180 0.0%, DD -53.1%
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 024900 덕양산업 — counterexample_theme_beta_local4b: MFE180 28.39%, MAE180 -37.58%, DD -51.38%
```

## Guardrail 3 — Controlled-MAE positives should not be overblocked

R13 must not become a blunt “drawdown blocker.”

The following rows had MFE with controlled entry-basis MAE and should be protected after source repair:

```text
R1 / C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY / 032820 우리기술 — positive_with_later_4b_watch_and_sharecount_validation: MFE180 95.24%, MAE180 -0.33%, DD -44.39%
R1 / C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY / 130660 한전산업 — positive_with_later_4b_watch: MFE180 121.59%, MAE180 -1.82%, DD -54.46%
R3 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK / 020150 롯데에너지머티리얼즈 — positive_with_later_4b_watch: MFE180 57.44%, MAE180 -2.4%, DD -57.52%
R4 / C16_STRATEGIC_RESOURCE_POLICY_SUPPLY / 081150 티플랙스 — positive_with_low_MAE_source_repair: MFE180 36.11%, MAE180 -2.04%, DD -17.01%
R5 / C18_CONSUMER_EXPORT_CHANNEL_REORDER / 017810 풀무원 — positive_with_later_4b_watch: MFE180 41.05%, MAE180 -6.18%, DD -33.49%
R5 / C18_CONSUMER_EXPORT_CHANNEL_REORDER / 280360 롯데웰푸드 — positive_with_later_4b_watch: MFE180 70.9%, MAE180 -1.31%, DD -38.13%
R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 138930 BNK금융지주 — positive_slow_with_sharecount_validation: MFE180 37.32%, MAE180 -2.79%, DD -12.57%
R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 175330 JB금융지주 — positive_with_sharecount_validation: MFE180 62.41%, MAE180 -1.13%, DD -2.51%
R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / 206640 바디텍메드 — positive_with_later_4b_watch: MFE180 50.36%, MAE180 -4.64%, DD -36.58%
R8 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION / 058970 엠로 — delayed_positive_with_sharecount_validation: MFE180 68.64%, MAE180 -4.76%, DD -18.73%
```

The useful distinction is:

```text
controlled MAE + verified bridge = Stage2 possible
high MFE + bridge stale + post-peak drawdown = lifecycle local 4B
high MAE + no bridge = false Stage2 / local 4B
```

## Guardrail 4 — hard 4C remains non-price evidence based

No loop 75 row justifies price-only hard 4C.

```text
hard_4c_price_only_allowed_count = 0
```

Hard 4C requires non-price thesis break evidence:

```text
default / refinancing failure / court rehabilitation
contract cancellation / customer loss / order cut
clinical or regulatory failure
policy reversal or project cancellation
tender/deal failure or legal break
capital impairment / covenant / auditor-control break
insolvency / solvency break
```

C30 construction rows are the cleanest boundary:

```text
005960 동부건설 = local 4B-watch, no hard 4C without refinancing/default evidence
013580 계룡건설 = RiskWatch / no hard 4C boundary
004960 한신공영 = bounded-MAE recovery / no hard 4C boundary
```

## Guardrail 5 — share-count validation queue

Share-count validation is a recurring blocking condition.  
These rows require validation before runtime promotion:

```text
R1:032820:우리기술
R6:138930:BNK금융지주
R6:175330:JB금융지주
R6:377300:카카오페이
R7:099190:아이센스
R7:214680:디알텍
R8:047560:이스트소프트
R8:058970:엠로
R10:005960:동부건설
R12:008930:한미사이언스
```

## Proposed cross-archetype decision

```json
{
  "row_type": "r13_guardrail_candidate",
  "round": "R13",
  "loop": 75,
  "axis": "high_mae_stage2_false_positive_local4b_vs_delayed_positive_protection",
  "decision": "hold_for_coding_agent_validation",
  "do_not_propose_new_weight_delta": true,
  "candidate_rules": [
    "Stage2 requires non-price bridge evidence specific to its archetype, not just MFE.",
    "If MAE_30D <= -20%, MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35% and bridge evidence is absent/stale, emit local 4B-watch.",
    "If MFE is high but post-peak drawdown <= -35%, preserve the historical MFE label but require lifecycle 4B after bridge fade.",
    "Do not convert local 4B-watch into hard 4C without non-price thesis break evidence.",
    "Protect controlled-MAE positives after source repair, especially where MAE_180D > -10% and MFE_180D >= 20%.",
    "Share-count changes inside the calibration window must block runtime promotion until validated."
  ],
  "high_priority_false_positive_symbols": [
    "R3:361610:SK아이이테크놀로지",
    "R11:053290:NE능률",
    "R4:011810:STX",
    "R6:377300:카카오페이",
    "R3:006110:삼아알미늄",
    "R11:133750:메가엠디",
    "R7:099190:아이센스",
    "R2:222800:심텍",
    "R4:000910:유니온",
    "R12:008930:한미사이언스",
    "R1:105840:우진",
    "R9:024900:덕양산업"
  ],
  "protect_positive_symbols": [
    "R1:032820:우리기술",
    "R1:130660:한전산업",
    "R3:020150:롯데에너지머티리얼즈",
    "R4:081150:티플랙스",
    "R5:017810:풀무원",
    "R5:280360:롯데웰푸드",
    "R6:138930:BNK금융지주",
    "R6:175330:JB금융지주",
    "R7:206640:바디텍메드",
    "R8:058970:엠로"
  ],
  "share_count_validation_symbols": [
    "R1:032820:우리기술",
    "R6:138930:BNK금융지주",
    "R6:175330:JB금융지주",
    "R6:377300:카카오페이",
    "R7:099190:아이센스",
    "R7:214680:디알텍",
    "R8:047560:이스트소프트",
    "R8:058970:엠로",
    "R10:005960:동부건설",
    "R12:008930:한미사이언스"
  ]
}
```

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "validation_status": "usable_for_R13_cross_case_checkpoint", "source_round_files": ["e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md", "e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "e2r_stock_web_v12_residual_round_R4_loop_75_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "e2r_stock_web_v12_residual_round_R5_loop_75_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "e2r_stock_web_v12_residual_round_R6_loop_75_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "e2r_stock_web_v12_residual_round_R9_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "e2r_stock_web_v12_residual_round_R11_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"]}
```

### R13 cross-case rows

```jsonl
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md", "source_case_id": "R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE", "source_trigger_id": "TRG_R1L75-C04-032820-WOORI-TECH-NUCLEAR-CONTROL-SYSTEM-BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "symbol": "032820", "company_name": "우리기술", "trigger_type": "Stage2-Actionable-NuclearControlSystemProjectBridge", "trigger_date": "2024-05-10", "entry_date": "2024-05-13", "entry_price": 1493.0, "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "role_bucket": "positive", "MFE_30D_pct": 77.49, "MFE_90D_pct": 95.24, "MFE_180D_pct": 95.24, "MAE_30D_pct": -0.33, "MAE_90D_pct": -0.33, "MAE_180D_pct": -0.33, "peak_date": "2024-07-09", "peak_price": 2915.0, "drawdown_after_peak_pct": -44.39, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair_but_require_lifecycle_4b", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md", "source_case_id": "R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE", "source_trigger_id": "TRG_R1L75-C04-105840-WOOJIN-INSTRUMENTATION-POLICY-PROXY-FADE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "symbol": "105840", "company_name": "우진", "trigger_type": "Stage2-FalsePositive / NuclearInstrumentationPolicyProxyFade", "trigger_date": "2024-05-24", "entry_date": "2024-05-27", "entry_price": 9580.0, "trigger_outcome_label": "counterexample_policy_proxy_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 16.91, "MFE_90D_pct": 16.91, "MFE_180D_pct": 16.91, "MAE_30D_pct": -7.1, "MAE_90D_pct": -25.68, "MAE_180D_pct": -41.23, "peak_date": "2024-05-27", "peak_price": 11200.0, "drawdown_after_peak_pct": -49.73, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R1", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md", "source_case_id": "R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE", "source_trigger_id": "TRG_R1L75-C04-130660-KEPCO-INDUSTRIAL-NUCLEAR-SERVICE-PROJECT-BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_CONTROL_INSTRUMENTATION_PROJECT_BRIDGE_VS_POLICY_PROXY_FADE", "symbol": "130660", "company_name": "한전산업", "trigger_type": "Stage2-Actionable-NuclearServiceProjectBridge", "trigger_date": "2024-05-24", "entry_date": "2024-05-27", "entry_price": 8800.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive", "MFE_30D_pct": 65.57, "MFE_90D_pct": 121.59, "MFE_180D_pct": 121.59, "MAE_30D_pct": -1.82, "MAE_90D_pct": -1.82, "MAE_180D_pct": -1.82, "peak_date": "2024-07-18", "peak_price": 19500.0, "drawdown_after_peak_pct": -54.46, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair_but_require_lifecycle_4b", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "source_case_id": "R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY", "source_trigger_id": "TRG_R2L75-C06-007660-ISU-PETASYS-AI-SERVER-MEMORY-SUBSTRATE-CAPACITY", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "symbol": "007660", "company_name": "이수페타시스", "trigger_type": "Stage2-Actionable-AIServerMemorySubstrateCapacityBridge", "trigger_date": "2024-03-01", "entry_date": "2024-03-04", "entry_price": 31350.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive", "MFE_30D_pct": 48.33, "MFE_90D_pct": 58.53, "MFE_180D_pct": 58.53, "MAE_30D_pct": -2.23, "MAE_90D_pct": -2.23, "MAE_180D_pct": -33.01, "peak_date": "2024-07-24", "peak_price": 49700.0, "drawdown_after_peak_pct": -57.75, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_possible_after_source_repair_but_lifecycle_managed", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "source_case_id": "R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE", "source_trigger_id": "TRG_R2L75-C06-222800-SIMMTECH-DDR5-HBM-SUBSTRATE-CYCLE-FADE", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "symbol": "222800", "company_name": "심텍", "trigger_type": "Stage2-FalsePositive / MemorySubstrateCycleFade", "trigger_date": "2024-03-20", "entry_date": "2024-03-21", "entry_price": 30100.0, "trigger_outcome_label": "counterexample", "role_bucket": "counterexample", "MFE_30D_pct": 14.45, "MFE_90D_pct": 14.45, "MFE_180D_pct": 14.45, "MAE_30D_pct": -6.31, "MAE_90D_pct": -12.13, "MAE_180D_pct": -47.84, "peak_date": "2024-04-02", "peak_price": 34450.0, "drawdown_after_peak_pct": -54.43, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R2", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "source_case_id": "R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE", "source_trigger_id": "TRG_R2L75-C06-353200-DAEDUCK-FCBGA-MEMORY-PACKAGE-SUBSTRATE-BETA-FADE", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "AI_SERVER_MEMORY_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_PACKAGE_SUBSTRATE_BETA_FADE", "symbol": "353200", "company_name": "대덕전자", "trigger_type": "Stage2-FalsePositive / PackageSubstrateBetaFade", "trigger_date": "2024-03-20", "entry_date": "2024-03-21", "entry_price": 24250.0, "trigger_outcome_label": "counterexample", "role_bucket": "counterexample", "MFE_30D_pct": 15.67, "MFE_90D_pct": 15.67, "MFE_180D_pct": 15.67, "MAE_30D_pct": -8.87, "MAE_90D_pct": -13.2, "MAE_180D_pct": -35.88, "peak_date": "2024-04-02", "peak_price": 28050.0, "drawdown_after_peak_pct": -44.56, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_case_id": "R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE", "source_trigger_id": "TRG_R3L75-C12-006110-SAMA-ALUMINIUM-ALFOIL-CONTRACT-BETA-FADE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "symbol": "006110", "company_name": "삼아알미늄", "trigger_type": "Stage2-FalsePositive / AluminumFoilContractBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 86500.0, "trigger_outcome_label": "counterexample_calloff_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 34.57, "MFE_90D_pct": 34.57, "MFE_180D_pct": 34.57, "MAE_30D_pct": -7.28, "MAE_90D_pct": -28.67, "MAE_180D_pct": -54.22, "peak_date": "2024-02-21", "peak_price": 116400.0, "drawdown_after_peak_pct": -70.79, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_case_id": "R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE", "source_trigger_id": "TRG_R3L75-C12-020150-LOTTE-ENERGY-MATERIALS-COPPER-FOIL-CONTRACT-BRIDGE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "trigger_type": "Stage2-Actionable-CopperFoilCustomerContractBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 31250.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive", "MFE_30D_pct": 31.04, "MFE_90D_pct": 57.44, "MFE_180D_pct": 57.44, "MAE_30D_pct": -0.8, "MAE_90D_pct": -0.8, "MAE_180D_pct": -2.4, "peak_date": "2024-03-21", "peak_price": 49200.0, "drawdown_after_peak_pct": -57.52, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair_but_require_lifecycle_4b", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R3", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_case_id": "R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK", "source_trigger_id": "TRG_R3L75-C12-361610-SK-IET-SEPARATOR-CUSTOMER-CALLOFF-RISK", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_SEPARATOR_AL_FOIL_CUSTOMER_CONTRACT_BRIDGE_VS_CALLOFF_BETA_FADE", "symbol": "361610", "company_name": "SK아이이테크놀로지", "trigger_type": "Stage2-FalsePositive / SeparatorCustomerCalloffRisk", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 73400.0, "trigger_outcome_label": "counterexample_calloff_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 10.08, "MFE_90D_pct": 10.08, "MFE_180D_pct": 10.08, "MAE_30D_pct": -11.31, "MAE_90D_pct": -48.84, "MAE_180D_pct": -59.06, "peak_date": "2024-02-02", "peak_price": 80800.0, "drawdown_after_peak_pct": -62.81, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_75_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_case_id": "R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE", "source_trigger_id": "TRG_R4L75-C16-000910-UNION-RARE-EARTH-POLICY-PROXY-FADE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "symbol": "000910", "company_name": "유니온", "trigger_type": "Stage2-FalsePositive / RareEarthPolicyProxyFade", "trigger_date": "2024-01-04", "entry_date": "2024-01-05", "entry_price": 6100.0, "trigger_outcome_label": "counterexample_policy_proxy_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 7.87, "MFE_90D_pct": 7.87, "MFE_180D_pct": 7.87, "MAE_30D_pct": -11.97, "MAE_90D_pct": -16.07, "MAE_180D_pct": -44.92, "peak_date": "2024-01-10", "peak_price": 6580.0, "drawdown_after_peak_pct": -48.94, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_75_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_case_id": "R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE", "source_trigger_id": "TRG_R4L75-C16-011810-STX-RESOURCE-TRADING-POLICY-BETA-FADE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "symbol": "011810", "company_name": "STX", "trigger_type": "Stage2-FalsePositive / ResourceTradingPolicyBetaFade", "trigger_date": "2024-02-15", "entry_date": "2024-02-16", "entry_price": 10470.0, "trigger_outcome_label": "counterexample_resource_trading_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 13.66, "MFE_90D_pct": 13.66, "MFE_180D_pct": 13.66, "MAE_30D_pct": -20.06, "MAE_90D_pct": -32.47, "MAE_180D_pct": -55.11, "peak_date": "2024-02-16", "peak_price": 11900.0, "drawdown_after_peak_pct": -66.85, "guardrail_flags": {"early_MAE_30D_le_-20": true, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_75_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_case_id": "R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE", "source_trigger_id": "TRG_R4L75-C16-081150-TFLEX-RARE-METAL-PROCESSING-SUPPLY-BRIDGE", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "RARE_METAL_PROCESSING_DIRECT_SUPPLY_BRIDGE_VS_RESOURCE_POLICY_PROXY_BETA_FADE", "symbol": "081150", "company_name": "티플랙스", "trigger_type": "Stage2-Actionable-RareMetalProcessingSupplyBridge", "trigger_date": "2024-10-09", "entry_date": "2024-10-10", "entry_price": 2700.0, "trigger_outcome_label": "positive_with_low_MAE_source_repair", "role_bucket": "positive", "MFE_30D_pct": 26.85, "MFE_90D_pct": 33.89, "MFE_180D_pct": 36.11, "MAE_30D_pct": -1.85, "MAE_90D_pct": -2.04, "MAE_180D_pct": -2.04, "peak_date": "2025-04-16", "peak_price": 3675.0, "drawdown_after_peak_pct": -17.01, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_75_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE", "source_trigger_id": "TRG_R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "symbol": "011150", "company_name": "CJ씨푸드", "trigger_type": "Stage2-FalsePositive / KFoodThemeSpikeFade", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 2635.0, "trigger_outcome_label": "counterexample_theme_spike_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 36.43, "MFE_90D_pct": 145.16, "MFE_180D_pct": 145.16, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-06-14", "peak_price": 6460.0, "drawdown_after_peak_pct": -53.1, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_75_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER", "source_trigger_id": "TRG_R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "symbol": "017810", "company_name": "풀무원", "trigger_type": "Stage2-Actionable-USChannelReorderMarginBridge", "trigger_date": "2024-03-29", "entry_date": "2024-04-01", "entry_price": 10670.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive", "MFE_30D_pct": 14.25, "MFE_90D_pct": 41.05, "MFE_180D_pct": 41.05, "MAE_30D_pct": -2.99, "MAE_90D_pct": -2.99, "MAE_180D_pct": -6.18, "peak_date": "2024-07-24", "peak_price": 15050.0, "drawdown_after_peak_pct": -33.49, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_75_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN", "source_trigger_id": "TRG_R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "symbol": "280360", "company_name": "롯데웰푸드", "trigger_type": "Stage2-Actionable-KFoodExportChannelMarginBridge", "trigger_date": "2024-04-10", "entry_date": "2024-04-11", "entry_price": 122000.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive", "MFE_30D_pct": 23.36, "MFE_90D_pct": 70.9, "MFE_180D_pct": 70.9, "MAE_30D_pct": -1.31, "MAE_90D_pct": -1.31, "MAE_180D_pct": -1.31, "peak_date": "2024-06-18", "peak_price": 208500.0, "drawdown_after_peak_pct": -38.13, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair_but_require_lifecycle_4b", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_75_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN", "source_trigger_id": "TRG_R6L75-C21-138930-BNK-FINANCIAL-REGIONAL-BANK-CAPITAL-RETURN", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "symbol": "138930", "company_name": "BNK금융지주", "trigger_type": "Stage2-Actionable-RegionalBankCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7530.0, "trigger_outcome_label": "positive_slow_with_sharecount_validation", "role_bucket": "positive", "MFE_30D_pct": 11.69, "MFE_90D_pct": 16.2, "MFE_180D_pct": 37.32, "MAE_30D_pct": -2.79, "MAE_90D_pct": -2.79, "MAE_180D_pct": -2.79, "peak_date": "2024-08-26", "peak_price": 10340.0, "drawdown_after_peak_pct": -12.57, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_75_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE", "source_trigger_id": "TRG_R6L75-C21-175330-JB-FINANCIAL-ROE-CAPITAL-RETURN-BRIDGE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "symbol": "175330", "company_name": "JB금융지주", "trigger_type": "Stage2-Actionable-RegionalFinancialROECapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11520.0, "trigger_outcome_label": "positive_with_sharecount_validation", "role_bucket": "positive", "MFE_30D_pct": 22.4, "MFE_90D_pct": 29.25, "MFE_180D_pct": 62.41, "MAE_30D_pct": 0.0, "MAE_90D_pct": -1.13, "MAE_180D_pct": -1.13, "peak_date": "2024-10-25", "peak_price": 18710.0, "drawdown_after_peak_pct": -2.51, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_75_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE", "source_trigger_id": "TRG_R6L75-C21-377300-KAKAOPAY-DIGITAL-FINANCE-PBR-BETA-FADE", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_FINANCIAL_HOLDING_ROE_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BETA_FADE", "symbol": "377300", "company_name": "카카오페이", "trigger_type": "Stage2-FalsePositive / DigitalFinancePBRBetaFade", "trigger_date": "2024-01-10", "entry_date": "2024-01-11", "entry_price": 48500.0, "trigger_outcome_label": "counterexample_digital_finance_beta_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 24.12, "MFE_90D_pct": 24.12, "MFE_180D_pct": 24.12, "MAE_30D_pct": -9.18, "MAE_90D_pct": -40.82, "MAE_180D_pct": -54.74, "peak_date": "2024-01-11", "peak_price": 60200.0, "drawdown_after_peak_pct": -63.54, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE", "source_trigger_id": "TRG_R7L75-C25-099190-ISENS-CGM-REIMBURSEMENT-ADOPTION-BETA-FADE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "symbol": "099190", "company_name": "아이센스", "trigger_type": "Stage2-FalsePositive / CGMReimbursementAdoptionBetaFade", "trigger_date": "2024-01-10", "entry_date": "2024-01-11", "entry_price": 29950.0, "trigger_outcome_label": "counterexample_reimbursement_beta_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 1.5, "MFE_90D_pct": 1.5, "MFE_180D_pct": 1.5, "MAE_30D_pct": -31.39, "MAE_90D_pct": -35.26, "MAE_180D_pct": -49.85, "peak_date": "2024-01-12", "peak_price": 30400.0, "drawdown_after_peak_pct": -50.59, "guardrail_flags": {"early_MAE_30D_le_-20": true, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE", "source_trigger_id": "TRG_R7L75-C25-206640-BODITECH-IVD-EXPORT-CHANNEL-MARGIN-BRIDGE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "symbol": "206640", "company_name": "바디텍메드", "trigger_type": "Stage2-Actionable-IVDExportChannelMarginBridge", "trigger_date": "2024-03-19", "entry_date": "2024-03-20", "entry_price": 14000.0, "trigger_outcome_label": "positive_with_later_4b_watch", "role_bucket": "positive", "MFE_30D_pct": 14.29, "MFE_90D_pct": 50.36, "MFE_180D_pct": 50.36, "MAE_30D_pct": -4.29, "MAE_90D_pct": -4.29, "MAE_180D_pct": -4.64, "peak_date": "2024-08-19", "peak_price": 21050.0, "drawdown_after_peak_pct": -36.58, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair_but_require_lifecycle_4b", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE", "source_trigger_id": "TRG_R7L75-C25-214680-DRTECH-XRAY-DETECTOR-EXPORT-ORDER-BETA-FADE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "IVD_CGM_XRAY_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DEVICE_THEME_BETA_FADE", "symbol": "214680", "company_name": "디알텍", "trigger_type": "Stage2-FalsePositive / XrayDetectorExportOrderBetaFade", "trigger_date": "2024-03-28", "entry_date": "2024-03-29", "entry_price": 3345.0, "trigger_outcome_label": "counterexample_device_export_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 14.5, "MFE_90D_pct": 22.27, "MFE_180D_pct": 22.27, "MAE_30D_pct": -11.81, "MAE_90D_pct": -12.26, "MAE_180D_pct": -17.49, "peak_date": "2024-07-30", "peak_price": 4090.0, "drawdown_after_peak_pct": -32.52, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_case_id": "R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE", "source_trigger_id": "TRG_R8L75-C28-047560-ESTSOFT-AI-AVATAR-SOFTWARE-THEME-SPIKE-FADE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "symbol": "047560", "company_name": "이스트소프트", "trigger_type": "Stage2-FalsePositive / AISoftwareThemeSpikeFade", "trigger_date": "2024-01-04", "entry_date": "2024-01-05", "entry_price": 15230.0, "trigger_outcome_label": "counterexample_theme_spike_local4b_with_sharecount_validation", "role_bucket": "counterexample", "MFE_30D_pct": 227.0, "MFE_90D_pct": 227.0, "MFE_180D_pct": 227.0, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -26.33, "peak_date": "2024-01-29", "peak_price": 49800.0, "drawdown_after_peak_pct": -77.47, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_case_id": "R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE", "source_trigger_id": "TRG_R8L75-C28-058970-EMRO-PROCUREMENT-SAAS-CONTRACT-RETENTION-BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "symbol": "058970", "company_name": "엠로", "trigger_type": "Stage2-DelayedPositive-ProcurementSaaSContractRetentionBridge", "trigger_date": "2024-08-12", "entry_date": "2024-08-13", "entry_price": 43050.0, "trigger_outcome_label": "delayed_positive_with_sharecount_validation", "role_bucket": "delayed_positive", "MFE_30D_pct": 26.83, "MFE_90D_pct": 68.64, "MFE_180D_pct": 68.64, "MAE_30D_pct": -4.76, "MAE_90D_pct": -4.76, "MAE_180D_pct": -4.76, "peak_date": "2024-11-18", "peak_price": 72600.0, "drawdown_after_peak_pct": -18.73, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": true, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "protect_positive_stage_after_source_repair", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_case_id": "R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE", "source_trigger_id": "TRG_R8L75-C28-067920-IGLOO-CYBERSECURITY-CONTRACT-RETENTION-BETA-FADE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "PROCUREMENT_SAAS_AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_VS_THEME_SPIKE_FADE", "symbol": "067920", "company_name": "이글루", "trigger_type": "Stage2-FalsePositive / CybersecurityContractRetentionBetaFade", "trigger_date": "2024-01-12", "entry_date": "2024-01-15", "entry_price": 6660.0, "trigger_outcome_label": "counterexample_security_theme_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 30.33, "MFE_90D_pct": 30.33, "MFE_180D_pct": 30.33, "MAE_30D_pct": -5.56, "MAE_90D_pct": -7.36, "MAE_180D_pct": -26.05, "peak_date": "2024-01-29", "peak_price": 8680.0, "drawdown_after_peak_pct": -43.26, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE", "source_trigger_id": "TRG_R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "symbol": "023800", "company_name": "인지컨트롤스", "trigger_type": "Stage2-FalsePositive / ThermalManagementThemeBetaFade", "trigger_date": "2024-02-14", "entry_date": "2024-02-15", "entry_price": 8340.0, "trigger_outcome_label": "counterexample_theme_beta_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 20.74, "MFE_90D_pct": 20.74, "MFE_180D_pct": 20.74, "MAE_30D_pct": -1.68, "MAE_90D_pct": -10.67, "MAE_180D_pct": -33.93, "peak_date": "2024-02-15", "peak_price": 10070.0, "drawdown_after_peak_pct": -45.28, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE", "source_trigger_id": "TRG_R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "symbol": "024900", "company_name": "덕양산업", "trigger_type": "Stage2-FalsePositive / BodyModuleBatteryHousingBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4790.0, "trigger_outcome_label": "counterexample_theme_beta_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 28.39, "MFE_90D_pct": 28.39, "MFE_180D_pct": 28.39, "MAE_30D_pct": -6.16, "MAE_90D_pct": -6.89, "MAE_180D_pct": -37.58, "peak_date": "2024-02-05", "peak_price": 6150.0, "drawdown_after_peak_pct": -51.38, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN", "source_trigger_id": "TRG_R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "symbol": "064960", "company_name": "SNT모티브", "trigger_type": "Stage2-SlowPositive / MotorModuleMixMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 44400.0, "trigger_outcome_label": "positive_slow_boundary_with_later_4b_watch", "role_bucket": "positive", "MFE_30D_pct": 5.97, "MFE_90D_pct": 8.67, "MFE_180D_pct": 13.29, "MAE_30D_pct": -2.82, "MAE_90D_pct": -2.82, "MAE_180D_pct": -11.04, "peak_date": "2024-06-28", "peak_price": 50300.0, "drawdown_after_peak_pct": -21.47, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_possible_after_source_repair_but_lifecycle_managed", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C", "source_trigger_id": "TRG_R10L75-C30-004960-HANSHIN-BUILDER-RISKWATCH-NO-HARD4C", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "symbol": "004960", "company_name": "한신공영", "trigger_type": "Stage2-RiskWatch / BuilderPFBoundedMAERecovery", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 7370.0, "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "role_bucket": "riskwatch_boundary", "MFE_30D_pct": 5.43, "MFE_90D_pct": 5.43, "MFE_180D_pct": 5.43, "MAE_30D_pct": -5.16, "MAE_90D_pct": -14.38, "MAE_180D_pct": -16.42, "peak_date": "2024-02-01", "peak_price": 7770.0, "drawdown_after_peak_pct": -20.72, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "riskwatch_no_hard_4c_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B", "source_trigger_id": "TRG_R10L75-C30-005960-DONGBU-PF-LIQUIDITY-LOCAL4B", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "symbol": "005960", "company_name": "동부건설", "trigger_type": "Stage4B-Local-PFOrderbookLiquidityWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5350.0, "trigger_outcome_label": "risk_positive_local4b_no_hard4c", "role_bucket": "risk_positive", "MFE_30D_pct": 2.8, "MFE_90D_pct": 2.8, "MFE_180D_pct": 2.8, "MAE_30D_pct": -5.79, "MAE_90D_pct": -9.53, "MAE_180D_pct": -25.79, "peak_date": "2024-02-19", "peak_price": 5500.0, "drawdown_after_peak_pct": -27.82, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "local_4b_watch_no_hard_4c", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C", "source_trigger_id": "TRG_R10L75-C30-013580-KYERYONG-BUFFERED-BUILDER-NO-HARD4C", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "symbol": "013580", "company_name": "계룡건설", "trigger_type": "Stage2-RiskWatch / BufferedBuilderNoHard4C", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 14460.0, "trigger_outcome_label": "overbearish_counterexample_no_hard4c", "role_bucket": "riskwatch_boundary", "MFE_30D_pct": 6.71, "MFE_90D_pct": 6.71, "MFE_180D_pct": 7.75, "MAE_30D_pct": -5.6, "MAE_90D_pct": -10.44, "MAE_180D_pct": -10.44, "peak_date": "2024-08-21", "peak_price": 15580.0, "drawdown_after_peak_pct": -15.28, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": false, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "riskwatch_no_hard_4c_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE", "source_trigger_id": "TRG_R11L75-C31-053290-NE-NEUNGYULE-MEDQUOTA-EDU-PROXY-FADE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "symbol": "053290", "company_name": "NE능률", "trigger_type": "Stage2-FalsePositive / EducationPolicyProxyFade", "trigger_date": "2024-02-05", "entry_date": "2024-02-06", "entry_price": 6200.0, "trigger_outcome_label": "counterexample_education_theme_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 1.61, "MFE_90D_pct": 1.61, "MFE_180D_pct": 1.61, "MAE_30D_pct": -26.94, "MAE_90D_pct": -27.34, "MAE_180D_pct": -55.73, "peak_date": "2024-02-06", "peak_price": 6300.0, "drawdown_after_peak_pct": -56.43, "guardrail_flags": {"early_MAE_30D_le_-20": true, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE", "source_trigger_id": "TRG_R11L75-C31-133750-MEGA-MD-MEDQUOTA-POLICY-PROXY-FADE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "symbol": "133750", "company_name": "메가엠디", "trigger_type": "Stage2-FalsePositive / MedicalQuotaPolicyProxyFade", "trigger_date": "2024-02-05", "entry_date": "2024-02-06", "entry_price": 3515.0, "trigger_outcome_label": "counterexample_policy_proxy_local4b", "role_bucket": "counterexample", "MFE_30D_pct": 4.41, "MFE_90D_pct": 4.41, "MFE_180D_pct": 4.41, "MAE_30D_pct": -18.78, "MAE_90D_pct": -29.59, "MAE_180D_pct": -53.14, "peak_date": "2024-02-06", "peak_price": 3670.0, "drawdown_after_peak_pct": -55.12, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": false, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE", "source_trigger_id": "TRG_R11L75-C31-339950-IVY-KIMYOUNG-MEDQUOTA-ADMISSION-DEMAND-LIFECYCLE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_ADMISSION_DEMAND_BRIDGE_VS_EDU_THEME_BETA_FADE", "symbol": "339950", "company_name": "아이비김영", "trigger_type": "Stage2-PolicyLifecycle / MedicalQuotaAdmissionDemandBridgeWithLater4B", "trigger_date": "2024-02-05", "entry_date": "2024-02-06", "entry_price": 1821.0, "trigger_outcome_label": "policy_lifecycle_positive_with_later_4b_watch", "role_bucket": "delayed_positive", "MFE_30D_pct": 62.82, "MFE_90D_pct": 62.82, "MFE_180D_pct": 62.82, "MAE_30D_pct": -6.64, "MAE_90D_pct": -7.91, "MAE_180D_pct": -18.73, "peak_date": "2024-02-26", "peak_price": 2965.0, "drawdown_after_peak_pct": -50.08, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_possible_after_source_repair_but_lifecycle_managed", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE", "source_trigger_id": "TRG_R12L75-C32-001750-HANYANG-SECURITIES-CONTROL-SALE-PREMIUM-FADE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "symbol": "001750", "company_name": "한양증권", "trigger_type": "Stage2-FalsePositive / SecuritiesControlSalePremiumFade", "trigger_date": "2024-07-23", "entry_date": "2024-07-24", "entry_price": 15650.0, "trigger_outcome_label": "counterexample_control_sale_premium_fade", "role_bucket": "counterexample", "MFE_30D_pct": 24.03, "MFE_90D_pct": 24.03, "MFE_180D_pct": 24.03, "MAE_30D_pct": -9.78, "MAE_90D_pct": -16.93, "MAE_180D_pct": -21.92, "peak_date": "2024-08-05", "peak_price": 19410.0, "drawdown_after_peak_pct": -37.04, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE", "source_trigger_id": "TRG_R12L75-C32-008930-HANMI-SCIENCE-CONTROL-DISPUTE-BENEFICIARY-FADE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "symbol": "008930", "company_name": "한미사이언스", "trigger_type": "Stage2-FalsePositive / FamilyControlDisputeBeneficiaryFade", "trigger_date": "2024-01-12", "entry_date": "2024-01-15", "entry_price": 46350.0, "trigger_outcome_label": "counterexample_control_dispute_local4b_with_sharecount_validation", "role_bucket": "counterexample", "MFE_30D_pct": 21.25, "MFE_90D_pct": 21.25, "MFE_180D_pct": 21.25, "MAE_30D_pct": -16.5, "MAE_90D_pct": -24.7, "MAE_180D_pct": -44.44, "peak_date": "2024-01-16", "peak_price": 56200.0, "drawdown_after_peak_pct": -54.18, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": true, "high_MAE_180D_le_-25": true, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": true, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "false_stage2_local_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": "75", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE", "source_trigger_id": "TRG_R12L75-C32-036560-YP-PRECISION-TENDER-CONTROL-PREMIUM-LIFECYCLE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "TENDER_OFFER_CONTROL_TRANSFER_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE_VS_HEADLINE_FADE", "symbol": "036560", "company_name": "영풍정밀/KZ정밀", "trigger_type": "Stage2-PolicyLifecycle / TenderOfferControlPremiumBridgeWithLater4B", "trigger_date": "2024-09-12", "entry_date": "2024-09-13", "entry_price": 12180.0, "trigger_outcome_label": "governance_lifecycle_positive_with_later_4b_watch", "role_bucket": "delayed_positive", "MFE_30D_pct": 201.31, "MFE_90D_pct": 201.31, "MFE_180D_pct": 201.31, "MAE_30D_pct": 0.0, "MAE_90D_pct": -2.38, "MAE_180D_pct": -15.76, "peak_date": "2024-10-07", "peak_price": 36700.0, "drawdown_after_peak_pct": -72.04, "guardrail_flags": {"early_MAE_30D_le_-20": false, "high_MAE_90D_le_-20": false, "high_MAE_180D_le_-25": false, "post_peak_drawdown_le_-35": true, "high_MFE_then_drawdown": true, "controlled_entry_MAE_positive_candidate": false, "source_repair_required": true, "share_count_validation_required": false, "hard_4c_allowed_from_price_only": false}, "r13_guardrail_action": "stage2_possible_after_source_repair_but_lifecycle_managed", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "hard_4c_requires_non_price_break": true, "do_not_count_as_new_sector_case": true}
```

### R13 summary row

```jsonl
{"row_type": "r13_cross_summary", "round": "R13", "loop": 75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "LOOP75_HIGH_MAE_STAGE2_FALSE_POSITIVE_LOCAL4B_SOURCE_REPAIR_CHECKPOINT", "selected_cross_case_count": 36, "source_rounds_covered": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_count": 12, "role_counts": {"positive": 11, "counterexample": 19, "delayed_positive": 3, "riskwatch_boundary": 2, "risk_positive": 1}, "stage2_false_positive_bridge_gap_count": 19, "risk_positive_local4b_count": 1, "riskwatch_or_overbearish_boundary_count": 2, "early_MAE_30D_le_-20_count": 3, "high_MAE_90D_le_-20_count": 9, "high_MAE_180D_le_-25_count": 18, "post_peak_drawdown_le_-35_count": 26, "high_MFE_then_drawdown_count": 17, "controlled_entry_MAE_positive_candidate_count": 10, "share_count_validation_required_count": 10, "source_repair_required_count": 36, "hard_4c_price_only_allowed_count": 0, "new_sector_positive_case_count": 0, "r13_decision": "guardrail_checkpoint_only", "r13_result": "do_not_change_runtime_weights_until_source_repair_and_validation"}
```

### R13 guardrail candidate row

```jsonl
{"row_type": "r13_guardrail_candidate", "round": "R13", "loop": 75, "axis": "high_mae_stage2_false_positive_local4b_vs_delayed_positive_protection", "decision": "hold_for_coding_agent_validation", "do_not_propose_new_weight_delta": true, "candidate_rules": ["Stage2 requires non-price bridge evidence specific to its archetype, not just MFE.", "If MAE_30D <= -20%, MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35% and bridge evidence is absent/stale, emit local 4B-watch.", "If MFE is high but post-peak drawdown <= -35%, preserve the historical MFE label but require lifecycle 4B after bridge fade.", "Do not convert local 4B-watch into hard 4C without non-price thesis break evidence.", "Protect controlled-MAE positives after source repair, especially where MAE_180D > -10% and MFE_180D >= 20%.", "Share-count changes inside the calibration window must block runtime promotion until validated."], "high_priority_false_positive_symbols": ["R3:361610:SK아이이테크놀로지", "R11:053290:NE능률", "R4:011810:STX", "R6:377300:카카오페이", "R3:006110:삼아알미늄", "R11:133750:메가엠디", "R7:099190:아이센스", "R2:222800:심텍", "R4:000910:유니온", "R12:008930:한미사이언스", "R1:105840:우진", "R9:024900:덕양산업"], "protect_positive_symbols": ["R1:032820:우리기술", "R1:130660:한전산업", "R3:020150:롯데에너지머티리얼즈", "R4:081150:티플랙스", "R5:017810:풀무원", "R5:280360:롯데웰푸드", "R6:138930:BNK금융지주", "R6:175330:JB금융지주", "R7:206640:바디텍메드", "R8:058970:엠로"], "share_count_validation_symbols": ["R1:032820:우리기술", "R6:138930:BNK금융지주", "R6:175330:JB금융지주", "R6:377300:카카오페이", "R7:099190:아이센스", "R7:214680:디알텍", "R8:047560:이스트소프트", "R8:058970:엠로", "R10:005960:동부건설", "R12:008930:한미사이언스"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": 75, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard", "delayed_positive_protection", "overbearish_no_hard4c_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": false, "canonical_archetype_rule_candidate": true, "narrative_summary": "Loop 75 cross-case review shows that high-MFE rows can still become false Green without archetype-specific non-price bridge evidence. Local 4B should catch bridge fade, high-MAE and post-peak drawdown; hard 4C remains non-price thesis-break based."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
source_round_files = R1~R12 loop 75 standalone MDs
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
R13_canonical_scope = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

Data-quality caveat:

```text
All source loop-75 rows are still source_proxy_only / evidence_url_pending.
R13 is therefore a guardrail-shape checkpoint, not a runtime scoring patch.
Coding-agent promotion requires non-proxy evidence repair and share-count validation.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this R13 loop 75 cross-archetype residual research MD.

Do not patch production scoring blindly.
This file is a guardrail checkpoint only.

Candidate axis:
high_mae_stage2_false_positive_local4b_vs_delayed_positive_protection

Required checks before implementation:
1. Validate all R13 cross-case rows against their source R1~R12 loop 75 trigger rows.
2. Confirm R13 created no new sector-specific positive cases.
3. Keep R13 output under:
   L10_POLICY_EVENT_CROSS_REDTEAM_MISC
   R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
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
8. Do not convert local 4B into hard 4C without non-price thesis break evidence.
9. Run share-count validation for every cross row marked share_count_change_inside_window=true.
10. Emit before/after diagnostics and reject if the guardrail overblocks verified low-MAE positives.
```

---

## Final round state

```text
completed_round = R13
completed_loop = 75
next_round = R1
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

