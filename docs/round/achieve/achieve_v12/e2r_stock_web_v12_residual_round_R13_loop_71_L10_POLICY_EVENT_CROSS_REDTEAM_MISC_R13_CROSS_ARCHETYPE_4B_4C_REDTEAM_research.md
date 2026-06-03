# E2R Stock-Web v12 R13 Cross-Archetype Red Team — Loop 71

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 71,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 71,
  "computed_next_round": "R1",
  "computed_next_loop": 72,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
  "fine_archetype_id": "HIGH_MFE_THEN_DRAWDOWN_LOCAL_4B_VS_FULL_4B_4C_GUARDRAIL",
  "loop_objective": [
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "residual_false_positive_mining",
    "yellow_threshold_stress_test",
    "green_strictness_stress_test",
    "holdout_validation",
    "counterexample_mining"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This is the R13 cross-archetype checkpoint for loop 71.  
It is not a new sector-specific positive research file. It does not patch `stock_agent`, does not change production scoring, and does not run live candidate discovery.

The execution mode follows the v12 historical calibration prompt:

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R12 / loop 71.

Therefore:

```text
scheduled_round = R13
scheduled_loop = 71
selected_large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_scope = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
computed_next_round = R1
computed_next_loop = 72
```

R13 is deliberately cross-archetype. It uses no individual sector canonical naming such as C20/C21/C24 as the output canonical scope.

## No-Repeat / novelty posture

R13 does not create new sector-positive evidence. It re-reads prior loop-71 rows as a checkpoint set.  
Therefore the relevant anti-repeat decision is:

```text
same sector case generation = false
same canonical positive mining = false
cross-case red-team aggregation = true
do_not_count_as_new_sector_case = true
```

The selected rows are used as **guardrail evidence**, not as new independent positive cases.

## R13 thesis

Across R4~R12, the repeated failure is not that the model misses every winner.  
The repeated failure is that **a fast MFE spike can wear the mask of a rerating**.

The same shape appears in unrelated rooms:

```text
C20 beauty/food distribution launch-channel enthusiasm
C24 bio trial/approval event risk
C27 game launch / content IP retention risk
C29 mobility beta without operating bridge
C30 PF rescue/recapitalization ambiguity
C31 policy event price-only squeeze
C32 governance control-premium scarcity
```

The R13 checkpoint rule is:

```text
Full 4B should still require non-price evidence.
But local 4B-watch should appear earlier when high MFE is followed by bridge failure, high MAE, or post-peak drawdown risk.
Hard 4C remains separate and should be reserved for explicit thesis-break evidence.
```

The guardrail behaves like a smoke alarm in a warehouse.  
It should not declare the building destroyed, but it also should not wait until the ceiling collapses.

---

## Cross-case checkpoint table

| source / archetype / symbol / trigger | MFE30 | MAE180 | post-peak DD | R13 flags | current profile verdict |
|---|---:|---:|---:|---|---|
| R4 / C15_MATERIAL_SPREAD_SUPERCYCLE / 005490 / Stage2-Actionable | 19.5 | -18.4 | -24.4 | stage2_false_positive_or_bridge_gap | current_profile_false_positive |
| R5 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 192820 / Stage4B | 1.77 | -44.96 | -45.92 | 4b_timing_test, high_mae_180_guardrail | current_profile_4B_too_late |
| R6 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN / 323410 / Stage4B | 4.73 | -27.23 | -27.23 | 4b_timing_test, high_mae_180_guardrail | current_profile_4B_too_late |
| R7 / C24_BIO_TRIAL_DATA_EVENT_RISK / 302440 / Stage2-Actionable | 11.44 | -52.03 | -59.87 | stage2_false_positive_or_bridge_gap, high_mae_180_guardrail | current_profile_false_positive |
| R7 / C24_BIO_TRIAL_DATA_EVENT_RISK / 084990 / Stage4C | 75.06 | -23.18 | -56.12 | 4c_timing_test, high_mfe_then_large_drawdown | current_profile_4C_too_late |
| R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / 225570 / Stage2-Actionable | 68.72 | -33.52 | -61.55 | stage2_false_positive_or_bridge_gap, 4b_timing_test, high_mfe_then_large_drawdown, high_mae_180_guardrail | current_profile_4B_too_late |
| R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 161390 / Stage2-Actionable | 14.62 | -21.83 | -35.78 | stage2_false_positive_or_bridge_gap | current_profile_false_positive |
| R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / 034300 / Stage2-Watch | 11.5 | -9.2 | -1.0 | stage2_false_positive_or_bridge_gap | current_profile_false_positive |
| R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 004090 / Stage4B-Local-PriceOnly-PolicyTheme | 29.79 | -33.72 | -48.93 | 4b_timing_test, high_mfe_then_large_drawdown, high_mae_180_guardrail | None |
| R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 247540 / Stage4B-Local-PriceOnly-PolicySqueeze | 30.87 | -35.23 | -50.51 | 4b_timing_test, high_mfe_then_large_drawdown, high_mae_180_guardrail | None |
| R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 003920 / Stage4B-GovernanceExecutionRisk | 42.63 | -34.91 | -54.37 | 4b_timing_test, high_mfe_then_large_drawdown, high_mae_180_guardrail | None |
| R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 180640 / Stage4B-Local-PriceOnly-GovernanceBlowoff | 146.67 | -0.33 | -45.77 | 4b_timing_test, high_mfe_then_large_drawdown | None |
| R7 / C24_BIO_TRIAL_DATA_EVENT_RISK / 000100 / Stage2-Actionable | 70.53 | -2.55 | -34.69 | positive_bridge_or_too_late_success | current_profile_too_late |
| R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / 259960 / Stage2-Actionable | 15.22 | -8.48 | -11.69 | positive_bridge_or_too_late_success | current_profile_missed_structural |
| R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE / 086280 / Stage2-Actionable | 12.98 | -4.76 | -30.46 | positive_bridge_or_too_late_success | current_profile_too_late |
| R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / 015760 / Stage2-Actionable | 14.46 | -9.28 | -26.06 | positive_bridge_or_too_late_success | None |
| R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / 042660 / Stage2-Actionable-GovernanceOverhangRelease | 5.1 | -12.26 | -31.73 | positive_bridge_or_too_late_success | None |

---

## Cluster 1 — high MFE followed by large drawdown: local 4B-watch timing

These rows had price paths that could seduce a Stage2/Green model.  
The problem is that the peak was not durable; after the first heat, the route cooled hard.

```json
[
  "R5L71-C20-01-T2",
  "T-KAKAOBANK-4B-20250624",
  "TRG_R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE",
  "TRG_R8L71_C27_225570_STAGE2_LAUNCH_SPIKE",
  "R11L71-C31-004090-EAST-SEA-OIL-GAS-ANNOUNCEMENT",
  "R11L71-C31-247540-SHORT-SELLING-BAN-SQUEEZE",
  "R12L71-C32-003920-NAMYANG-HAHNCONTROL-EXECUTION-LITIGATION-CAP",
  "R12L71-C32-180640-HANJINKAL-CONTROL-BATTLE-BLOWOFF"
]
```

Representative patterns:

```text
- C27 / 225570: launch spike without durable retention bridge
- C31 / 004090: policy/geology announcement without cash-flow bridge
- C31 / 247540: market-structure squeeze without company-level earnings bridge
- C32 / 180640: control battle scarcity without tender/cash bridge
- C32 / 003920: control premium with execution/litigation risk
```

R13 judgment:

```text
local_4b_watch_guard = strengthen
full_4b_requirement = keep_non_price_evidence_required
stage2_positive_weight = do_not_loosen
```

## Cluster 2 — Stage2 false positive / bridge gap

These rows were not all immediate collapses. Some produced respectable MFE.  
But they lacked the right evidence bridge for their archetype.

```json
[
  "TR-R4L71-C15-005490-STAGE2A-20250221",
  "R5L71-C20-01-T2",
  "T-KAKAOBANK-4B-20250624",
  "TRG_R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP",
  "TRG_R8L71_C27_225570_STAGE2_LAUNCH_SPIKE",
  "T_C29_161390_S2_20240201",
  "TR-C30-034300-S2WATCH",
  "R11L71-C31-004090-EAST-SEA-OIL-GAS-ANNOUNCEMENT",
  "R11L71-C31-247540-SHORT-SELLING-BAN-SQUEEZE",
  "R12L71-C32-003920-NAMYANG-HAHNCONTROL-EXECUTION-LITIGATION-CAP"
]
```

Representative failure modes:

```text
- C15: policy/spread or protection headline without durable demand revision
- C20: global distribution optimism after the channel was already priced
- C24: clinical/trial event with demand or endpoint bridge missing
- C29: margin/beta recovery without sustained operating leverage
- C30: rescue/recapitalization headline without PF balance-sheet repair
- C31: policy headline without named execution bridge
- C32: control premium without clean closing or tender clarity
```

R13 judgment:

```text
stage2_required_bridge = keep_or_strengthen
green_strictness = keep
yellow_threshold = allow watch, not Green
```

## Cluster 3 — hard 4C must remain evidence-based

Only the rows with explicit hard thesis-break evidence belong to 4C.  
A price collapse alone is not enough to make a thesis-break label reliable.

```json
[
  "TRG_R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE"
]
```

R13 judgment:

```text
hard_4c_confirmation = keep
relief_bounce_after_bad_news = do_not_reset_to_stage2
price_only_drawdown = local_4b_watch_not_4c
```

## Cluster 4 — positive anchors that should not be overblocked

The red-team guard must not become a net that catches every real winner.  
These rows have high MFE but also a real bridge.

```json
[
  "TRG_R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE",
  "TRG_R8L71_C27_259960_STAGE2_LIVE_SERVICE_MONETIZATION",
  "T_C29_086280_S2_20240807",
  "R11L71-C31-015760-CZECH-KHNP-PREFERRED-BIDDER-BRIDGE",
  "R12L71-C32-042660-KDB-OVERHANG-BLOCK-SALE-CONTROL-TRANSFER"
]
```

Representative positive anchors:

```text
- C24 / 000100: approval/commercialization bridge with strong post-entry MFE
- C27 / 259960: live-service monetization rather than one-off launch spike
- C29 / 086280: logistics operating leverage with external volume/margin bridge
- C31 / 015760: named project / preferred bidder policy bridge
- C32 / 042660: control-transfer and KDB overhang release with operating bridge
```

R13 judgment:

```text
Do not turn local 4B-watch into a universal volatility penalty.
The guard should fire when bridge evidence is absent or when the bridge breaks.
```

## Cluster 5 — source repair queue

Some rows are useful for price-path red-team purposes but not clean enough for runtime promotion.

```json
[
  "T-KAKAOBANK-4B-20250624",
  "R12L71-C32-003920-NAMYANG-HAHNCONTROL-EXECUTION-LITIGATION-CAP",
  "R12L71-C32-180640-HANJINKAL-CONTROL-BATTLE-BLOWOFF"
]
```

R13 judgment:

```text
source_proxy_only rows can inform the checkpoint narrative,
but coding-agent promotion must wait for non-proxy evidence repair.
```

---

## R13 guardrail candidate

```json
{
  "row_type": "r13_guardrail_candidate",
  "round": "R13",
  "loop": 71,
  "axis": "local_4b_watch_vs_full_4b_4c_timing",
  "decision": "candidate_guardrail_observe_more",
  "proposed_runtime_effect": "Do not loosen Stage2/Green. Keep full 4B non-price evidence requirement, but introduce/strengthen a local 4B-watch label for high-MFE price paths when the trigger has no durable bridge and post-peak drawdown risk is already visible. Hard 4C remains reserved for explicit thesis-break evidence.",
  "trigger_condition_sketch": {
    "local_4b_watch": [
      "MFE_30D >= 25%",
      "drawdown_after_peak <= -35% or MAE_180D <= -25%",
      "bridge evidence absent/weak OR execution/tender/litigation risk visible",
      "sector-specific full-4B evidence not yet available"
    ],
    "do_not_overblock_positive": [
      "named project / cash-flow / customer / order / regulatory-commercialization bridge exists",
      "positive anchor has high MFE and acceptable evidence quality",
      "drawdown is volatility after structural bridge, not pure blowoff"
    ],
    "hard_4c": [
      "explicit trial failure / PF break / insolvency / contract cancellation / thesis-break evidence",
      "relief bounce after bad news should not reset Stage2"
    ]
  },
  "do_not_propose_new_weight_delta": true
}
```

## Machine-readable rows

### R13 cross-case rows

```jsonl
{"row_type": "r13_cross_case", "source_round": "R4", "source_loop": "71", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "STEEL_ANTIDUMPING_SPREAD_PROTECTION_VS_DEMAND_WEAKNESS", "source_trigger_id": "TR-R4L71-C15-005490-STAGE2A-20250221", "case_id": "R4L71-C15-STEEL-ANTIDUMPING-005490-20250221", "symbol": "005490", "company_name": "POSCO홀딩스", "trigger_type": "Stage2-Actionable", "entry_date": "2025-02-21", "entry_price": 282000, "mfe_30_pct": 19.5, "mae_30_pct": -7.3, "mfe_180_pct": 21.3, "mae_180_pct": -18.4, "peak_price": 342000, "peak_date": "2025-07-23", "drawdown_after_peak_pct": -24.4, "current_profile_verdict": "current_profile_false_positive", "trigger_outcome_label": "stage2_high_mae_borderline_positive_counterexample", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["stage2_false_positive_or_bridge_gap"]}
{"row_type": "r13_cross_case", "source_round": "R5", "source_loop": "71", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_US_PHYSICAL_RETAIL_GLOBAL_DISTRIBUTION_VS_LEGACY_BRAND_PLATEAU", "source_trigger_id": "R5L71-C20-01-T2", "case_id": "R5L71-C20-01", "symbol": "192820", "company_name": "코스맥스", "trigger_type": "Stage4B", "entry_date": "2025-06-25", "entry_price": 282000, "mfe_30_pct": 1.77, "mae_30_pct": -16.67, "mfe_180_pct": 1.77, "mae_180_pct": -44.96, "peak_price": 287000, "peak_date": "2025-06-25", "drawdown_after_peak_pct": -45.92, "current_profile_verdict": "current_profile_4B_too_late", "trigger_outcome_label": "4B_overlay_success", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["4b_timing_test", "high_mae_180_guardrail"]}
{"row_type": "r13_cross_case", "source_round": "R6", "source_loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "PLATFORM_BANK_PRICE_ONLY_BETA_GUARD", "source_trigger_id": "T-KAKAOBANK-4B-20250624", "case_id": "C21-R6L71-KAKAOBANK-20250210", "symbol": "323410", "company_name": "카카오뱅크", "trigger_type": "Stage4B", "entry_date": "2025-06-24", "entry_price": 37000, "mfe_30_pct": 4.73, "mae_30_pct": -23.78, "mfe_180_pct": 4.73, "mae_180_pct": -27.23, "peak_price": 38750, "peak_date": "2025-06-24", "drawdown_after_peak_pct": -27.23, "current_profile_verdict": "current_profile_4B_too_late", "trigger_outcome_label": "4B_overlay_success_price_only", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "r13_flags": ["4b_timing_test", "high_mae_180_guardrail"]}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "source_trigger_id": "TRG_R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP", "case_id": "R7L71_C24_302440_SKY_COVIONE_PHASE3_DEMAND_TRAP", "symbol": "302440", "company_name": "SK바이오사이언스", "trigger_type": "Stage2-Actionable", "entry_date": "2022-04-29", "entry_price": 135500, "mfe_30_pct": 11.44, "mae_30_pct": -27.31, "mfe_180_pct": 15.5, "mae_180_pct": -52.03, "peak_price": 156500, "peak_date": "2022-07-13", "drawdown_after_peak_pct": -59.87, "current_profile_verdict": "current_profile_false_positive", "trigger_outcome_label": "stage2_false_positive_due_to_demand_bridge_failure", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["stage2_false_positive_or_bridge_gap", "high_mae_180_guardrail"]}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "source_trigger_id": "TRG_R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE", "case_id": "R7L71_C24_084990_ENGENSIS_DPN_PHASE3_FAILURE", "symbol": "084990", "company_name": "헬릭스미스", "trigger_type": "Stage4C", "entry_date": "2024-01-03", "entry_price": 4250, "mfe_30_pct": 75.06, "mae_30_pct": -23.06, "mfe_180_pct": 75.06, "mae_180_pct": -23.18, "peak_price": 7440, "peak_date": "2024-02-06", "drawdown_after_peak_pct": -56.12, "current_profile_verdict": "current_profile_4C_too_late", "trigger_outcome_label": "hard_4C_with_relief_bounce_false_positive_risk", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["4c_timing_test", "high_mfe_then_large_drawdown"]}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "71", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD", "source_trigger_id": "TRG_R8L71_C27_225570_STAGE2_LAUNCH_SPIKE", "case_id": "R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B", "symbol": "225570", "company_name": "넥슨게임즈", "trigger_type": "Stage2-Actionable", "entry_date": "2024-07-03", "entry_price": 17900, "mfe_30_pct": 68.72, "mae_30_pct": -7.88, "mfe_180_pct": 72.91, "mae_180_pct": -33.52, "peak_price": 30950, "peak_date": "2024-08-09", "drawdown_after_peak_pct": -61.55, "current_profile_verdict": "current_profile_4B_too_late", "trigger_outcome_label": "high_mfe_but_failed_retention_rerating", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["stage2_false_positive_or_bridge_gap", "4b_timing_test", "high_mfe_then_large_drawdown", "high_mae_180_guardrail"]}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "71", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA", "source_trigger_id": "T_C29_161390_S2_20240201", "case_id": "C29_TIRE_161390_2024_MARGIN_COUNTER", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-01", "entry_price": 52000, "mfe_30_pct": 14.62, "mae_30_pct": -4.04, "mfe_180_pct": 21.73, "mae_180_pct": -21.83, "peak_price": 63300, "peak_date": "2024-04-16", "drawdown_after_peak_pct": -35.78, "current_profile_verdict": "current_profile_false_positive", "trigger_outcome_label": "failed_rerating", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["stage2_false_positive_or_bridge_gap"]}
{"row_type": "r13_cross_case", "source_round": "R10", "source_loop": "71", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_BALANCE_SHEET_BREAK_VS_RECAPITALIZATION_RESCUE", "source_trigger_id": "TR-C30-034300-S2WATCH", "case_id": "C30-R10L71-034300-RECAP", "symbol": "034300", "company_name": "신세계건설", "trigger_type": "Stage2-Watch", "entry_date": "2024-02-07", "entry_price": 11460, "mfe_30_pct": 11.5, "mae_30_pct": -9.2, "mfe_180_pct": 60.0, "mae_180_pct": -9.2, "peak_price": 18340, "peak_date": "2024-09-30", "drawdown_after_peak_pct": -1.0, "current_profile_verdict": "current_profile_false_positive", "trigger_outcome_label": "rescue_recap_counterexample", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["stage2_false_positive_or_bridge_gap"]}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF", "source_trigger_id": null, "case_id": "R11L71-C31-004090-EAST-SEA-OIL-GAS-ANNOUNCEMENT", "symbol": "004090", "company_name": "한국석유", "trigger_type": "Stage4B-Local-PriceOnly-PolicyTheme", "entry_date": "2024-06-04", "entry_price": 21650.0, "mfe_30_pct": 29.79, "mae_30_pct": -23.23, "mfe_180_pct": 29.79, "mae_180_pct": -33.72, "peak_price": 28100.0, "peak_date": "2024-06-05", "drawdown_after_peak_pct": -48.93, "current_profile_verdict": null, "trigger_outcome_label": null, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["4b_timing_test", "high_mfe_then_large_drawdown", "high_mae_180_guardrail"]}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF", "source_trigger_id": null, "case_id": "R11L71-C31-247540-SHORT-SELLING-BAN-SQUEEZE", "symbol": "247540", "company_name": "에코프로비엠", "trigger_type": "Stage4B-Local-PriceOnly-PolicySqueeze", "entry_date": "2023-11-06", "entry_price": 270500.0, "mfe_30_pct": 30.87, "mae_30_pct": -16.82, "mfe_180_pct": 30.87, "mae_180_pct": -35.23, "peak_price": 354000.0, "peak_date": "2023-12-04", "drawdown_after_peak_pct": -50.51, "current_profile_verdict": null, "trigger_outcome_label": null, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["4b_timing_test", "high_mfe_then_large_drawdown", "high_mae_180_guardrail"]}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF", "source_trigger_id": null, "case_id": "R12L71-C32-003920-NAMYANG-HAHNCONTROL-EXECUTION-LITIGATION-CAP", "symbol": "003920", "company_name": "남양유업", "trigger_type": "Stage4B-GovernanceExecutionRisk", "entry_date": "2021-05-28", "entry_price": 570000.0, "mfe_30_pct": 42.63, "mae_30_pct": -5.26, "mfe_180_pct": 42.63, "mae_180_pct": -34.91, "peak_price": 813000.0, "peak_date": "2021-07-01", "drawdown_after_peak_pct": -54.37, "current_profile_verdict": null, "trigger_outcome_label": null, "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "r13_flags": ["4b_timing_test", "high_mfe_then_large_drawdown", "high_mae_180_guardrail"]}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF", "source_trigger_id": null, "case_id": "R12L71-C32-180640-HANJINKAL-CONTROL-BATTLE-BLOWOFF", "symbol": "180640", "company_name": "한진칼", "trigger_type": "Stage4B-Local-PriceOnly-GovernanceBlowoff", "entry_date": "2020-03-27", "entry_price": 45000.0, "mfe_30_pct": 146.67, "mae_30_pct": -0.33, "mfe_180_pct": 146.67, "mae_180_pct": -0.33, "peak_price": 111000.0, "peak_date": "2020-04-20", "drawdown_after_peak_pct": -45.77, "current_profile_verdict": null, "trigger_outcome_label": null, "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "r13_flags": ["4b_timing_test", "high_mfe_then_large_drawdown"]}
{"row_type": "r13_cross_case", "source_round": "R7", "source_loop": "71", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "CLINICAL_DATA_EVENT_POSITIVE_VS_BINARY_FAILURE_AND_DEMAND_BRIDGE_GUARD", "source_trigger_id": "TRG_R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE", "case_id": "R7L71_C24_000100_LAZERTINIB_MARIPOSA_APPROVAL_BRIDGE", "symbol": "000100", "company_name": "유한양행", "trigger_type": "Stage2-Actionable", "entry_date": "2024-08-20", "entry_price": 94000, "mfe_30_pct": 70.53, "mae_30_pct": -2.55, "mfe_180_pct": 77.55, "mae_180_pct": -2.55, "peak_price": 166900, "peak_date": "2024-10-15", "drawdown_after_peak_pct": -34.69, "current_profile_verdict": "current_profile_too_late", "trigger_outcome_label": "positive_structural_success_with_fast_4B_overlay", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["positive_bridge_or_too_late_success"]}
{"row_type": "r13_cross_case", "source_round": "R8", "source_loop": "71", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD", "source_trigger_id": "TRG_R8L71_C27_259960_STAGE2_LIVE_SERVICE_MONETIZATION", "case_id": "R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION", "symbol": "259960", "company_name": "크래프톤", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-13", "entry_price": 230000, "mfe_30_pct": 15.22, "mae_30_pct": -8.48, "mfe_180_pct": 54.35, "mae_180_pct": -8.48, "peak_price": 355000, "peak_date": "2024-08-22", "drawdown_after_peak_pct": -11.69, "current_profile_verdict": "current_profile_missed_structural", "trigger_outcome_label": "structural_success", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["positive_bridge_or_too_late_success"]}
{"row_type": "r13_cross_case", "source_round": "R9", "source_loop": "71", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "NON_OEM_AUTO_LOGISTICS_TIRE_THERMAL_OPERATING_LEVERAGE_VS_PRICE_ONLY_BETA", "source_trigger_id": "T_C29_086280_S2_20240807", "case_id": "C29_GL_086280_2024_LOGISTICS_LEVERAGE", "symbol": "086280", "company_name": "현대글로비스", "trigger_type": "Stage2-Actionable", "entry_date": "2024-08-07", "entry_price": 107100, "mfe_30_pct": 12.98, "mae_30_pct": -4.76, "mfe_180_pct": 40.99, "mae_180_pct": -4.76, "peak_price": 151000, "peak_date": "2025-01-31", "drawdown_after_peak_pct": -30.46, "current_profile_verdict": "current_profile_too_late", "trigger_outcome_label": "structural_success", "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["positive_bridge_or_too_late_success"]}
{"row_type": "r13_cross_case", "source_round": "R11", "source_loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "POLICY_EVENT_EXECUTION_BRIDGE_VS_PRICE_ONLY_THEME_BLOWOFF", "source_trigger_id": null, "case_id": "R11L71-C31-015760-CZECH-KHNP-PREFERRED-BIDDER-BRIDGE", "symbol": "015760", "company_name": "한국전력", "trigger_type": "Stage2-Actionable", "entry_date": "2024-07-18", "entry_price": 20050.0, "mfe_30_pct": 14.46, "mae_30_pct": -9.28, "mfe_180_pct": 22.69, "mae_180_pct": -9.28, "peak_price": 24600.0, "peak_date": "2024-11-26", "drawdown_after_peak_pct": -26.06, "current_profile_verdict": null, "trigger_outcome_label": null, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["positive_bridge_or_too_late_success"]}
{"row_type": "r13_cross_case", "source_round": "R12", "source_loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_OVERHANG_RELEASE_VS_TENDER_CAP_AND_PRICE_ONLY_GOVERNANCE_BLOWOFF", "source_trigger_id": null, "case_id": "R12L71-C32-042660-KDB-OVERHANG-BLOCK-SALE-CONTROL-TRANSFER", "symbol": "042660", "company_name": "한화오션", "trigger_type": "Stage2-Actionable-GovernanceOverhangRelease", "entry_date": "2025-04-29", "entry_price": 82400.0, "mfe_30_pct": 5.1, "mae_30_pct": -11.17, "mfe_180_pct": 83.98, "mae_180_pct": -12.26, "peak_price": 151600.0, "peak_date": "2025-10-30", "drawdown_after_peak_pct": -31.73, "current_profile_verdict": null, "trigger_outcome_label": null, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "r13_flags": ["positive_bridge_or_too_late_success"]}
```

### R13 summary row

```jsonl
{"row_type": "r13_cross_summary", "round": "R13", "loop": 71, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "selected_cross_case_count": 17, "source_rounds_covered": ["R10", "R11", "R12", "R4", "R5", "R6", "R7", "R8", "R9"], "source_canonical_count": 9, "local_4b_watch_should_precede_full_4b_count": 8, "stage2_false_positive_bridge_gap_count": 10, "hard_4c_relief_bounce_guard_count": 1, "positive_anchor_not_to_overblock_count": 5, "source_repair_required_count": 3, "do_not_propose_new_weight_delta": true, "r13_decision": "guardrail_checkpoint_only"}
```

### R13 guardrail row

```jsonl
{"row_type": "r13_guardrail_candidate", "round": "R13", "loop": 71, "axis": "local_4b_watch_vs_full_4b_4c_timing", "decision": "candidate_guardrail_observe_more", "proposed_runtime_effect": "Do not loosen Stage2/Green. Keep full 4B non-price evidence requirement, but introduce/strengthen a local 4B-watch label for high-MFE price paths when the trigger has no durable bridge and post-peak drawdown risk is already visible. Hard 4C remains reserved for explicit thesis-break evidence.", "trigger_condition_sketch": {"local_4b_watch": ["MFE_30D >= 25%", "drawdown_after_peak <= -35% or MAE_180D <= -25%", "bridge evidence absent/weak OR execution/tender/litigation risk visible", "sector-specific full-4B evidence not yet available"], "do_not_overblock_positive": ["named project / cash-flow / customer / order / regulatory-commercialization bridge exists", "positive anchor has high MFE and acceptable evidence quality", "drawdown is volatility after structural bridge, not pure blowoff"], "hard_4c": ["explicit trial failure / PF break / insolvency / contract cancellation / thesis-break evidence", "relief bounce after bad news should not reset Stage2"]}, "do_not_propose_new_weight_delta": true}
```

---

## Score / return alignment summary

The cross-archetype alignment is:

```text
1. High MFE alone is not a rerating.
2. High MFE + bridge absent + large post-peak drawdown = local 4B-watch.
3. High MFE + bridge present + no thesis-break evidence = do not overblock.
4. Hard 4C needs explicit non-price thesis-break evidence.
5. Full 4B still needs non-price evidence, but local 4B-watch can be earlier and lighter.
```

The current calibrated profile is directionally right on the global rules, but the R13 residual is timing:

```text
Full 4B is sometimes too late.
Stage2/Green is sometimes too generous when a theme has MFE but no bridge.
Hard 4C should not be inferred from price alone.
```

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
source_inputs = prior loop-71 standalone MD artifacts + stock-web rows embedded in those artifacts
production_scoring_changed = false
shadow_weight_only = true
```

This R13 file is a checkpoint and should not be counted as new sector-positive coverage.

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this R13 standalone v12 cross-archetype red-team MD.
Do not patch production scoring blindly.

Scope:
canonical_scope = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
axis = local_4b_watch_vs_full_4b_4c_timing

Required checks:
1. Ingest only r13_cross_case / r13_cross_summary / r13_guardrail_candidate rows.
2. Do not count these rows as new sector-positive coverage.
3. Validate each source trigger row against its original loop-71 MD and stock-web tradable_raw OHLC shard.
4. Keep full 4B non-price evidence requirement.
5. Consider a lighter local_4b_watch diagnostic when:
   - MFE_30D >= 25%
   - post-peak drawdown <= -35% or MAE_180D <= -25%
   - bridge evidence is absent/weak or execution/tender/litigation risk is visible
   - full non-price 4B evidence is not yet available.
6. Do not convert local_4b_watch into hard 4C.
7. Hard 4C requires explicit non-price thesis-break evidence.
8. Do not overblock positive anchors with named project, order, customer, commercialization, operating, or governance execution bridge.
9. Reject implementation if Stage2/Green false negatives increase on positive anchors.
10. Emit a before/after confusion table:
   - false positive reduction
   - missed structural positives
   - local 4B timing lead
   - hard 4C precision.
```

---

## Final round state

```text
completed_round = R13
completed_loop = 71
next_round = R1
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

