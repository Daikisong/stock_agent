# E2R Stock-Web v12 Residual Research — R13 Loop 83 / L10 / Cross-Archetype 4B/4C RedTeam

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 83,
  "computed_next_round": "R1",
  "computed_next_loop": 84,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
  "fine_archetype_id": "LOOP83_CROSS_ARCHETYPE_PRICE_ONLY_BLOWOFF_HIGH_MAE_SOURCE_REPAIR_4B_4C_GUARDRAIL",
  "loop_objective": [
    "cross_archetype_redteam_checkpoint",
    "stage2_false_positive_review",
    "4B_local_vs_full_window_audit",
    "hard_4C_non_price_thesis_break_protection",
    "high_MAE_guardrail_review",
    "source_proxy_evidence_url_pending_blocker_review",
    "do_not_count_as_new_sector_case",
    "do_not_propose_new_weight_delta"
  ],
  "source_round_span": "R1~R12 loop 83",
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true,
  "do_not_count_as_new_sector_case": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / cross-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. R13 Scope Resolution

```text
scheduled_round = R13
scheduled_loop = 83
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC only
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
computed_next_round = R1
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R13 is not a new sector research round. It is a cross-archetype checkpoint. Therefore this MD does not add new positive cases, does not add new symbols, and does not count source cases again.

```text
new_independent_case_count = 0
new_symbol_count = 0
do_not_count_as_new_sector_case = true
do_not_propose_new_weight_delta = true
```

## 3. No-Repeat / Duplicate Handling

R13 source rows are reused only as checkpoint evidence.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
R13_cross_case_policy = do_not_count_as_new_case=true
```

This MD deliberately avoids creating fresh sector rows such as C20/C21/C23 etc. Every machine-readable `trigger` row is marked as an R13 cross checkpoint and has `independent_evidence_weight = 0.0`.

## 4. Stock-Web Price Source Context

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

R13 does not recompute new entry windows. It inherits the Stock-Web price validations and trigger-level OHLC calculations from the R1~R12 source MDs.

## 5. Source MD Inventory — Loop 83

| round | large_sector_id | source canonical | source axis | checkpoint role |
|---|---|---|---|---|
| R1 | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | `industrial_order_backlog_margin_bridge_guardrail` | order/backlog/delivery/margin bridge; avoid cycle-fade positives |
| R2 | L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | `C10_order_refresh_required_after_memory_recovery_beta` | memory-recovery beta needs order refresh after initial cycle turn |
| R3 | L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | `C12_customer_calloff_bridge_required_for_upstream_supplier_stage2_actionable` | upstream battery supplier requires OEM call-off/utilization bridge |
| R4 | L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | `C16_customer_offtake_utilization_margin_bridge_required` | resource policy headline needs offtake/utilization/repricing/margin bridge |
| R5 | L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | `C19_inventory_margin_bridge_required` | traffic/reopening/destocking headline needs inventory-turn/sell-through/reorder/gross-margin bridge |
| R6 | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | `C21_capital_return_execution_and_capital_buffer_bridge_required` | value-up/low-PBR headline needs CET1/capital buffer and buyback/dividend execution |
| R7 | L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | `C24_trial_data_partner_milestone_cash_runway_bridge_required` | trial/platform MFE needs data-quality/partner/milestone/cash-runway bridge |
| R8 | L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | `C27_liveops_retention_global_monetization_bridge_required` | IP/global launch headline needs sales ranking/live-ops/retention/ARPU bridge |
| R9 | L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | `C29_volume_yield_cost_margin_bridge_required` | traffic/capacity recovery needs yield/cost/load-factor/contract-mix/margin bridge |
| R10 | L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | `C30_PF_refinancing_debt_margin_bridge_required` | housing recovery needs PF refinancing/debt/project-loss/orderbook/margin bridge |
| R11 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | `C31_policy_direct_beneficiary_tariff_margin_bridge_required` | utility policy needs direct beneficiary and tariff/subsidy/revenue/margin/FCF bridge |
| R12 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | `C31_tourism_policy_visitor_drop_margin_bridge_required` | tourism policy/reopening needs visitor/drop/sales/occupancy/margin bridge |

## 6. Cross-Archetype RedTeam Rows

| cross_case_id | cross_scope | source rounds | decision | verdict |
|---|---|---|---|---|
| R13L83-X01 | source_proxy_evidence_url_pending_blocker | R2, R3, R4, R5, R7, R8, R9, R10, R11, R12 | hold_shadow_only_do_not_promote | block_runtime_promotion_until_source_repair |
| R13L83-X02 | local_4B_vs_full_window_4B_timing | R7, R8, R9, R11, R12 | keep_full_4B_requires_non_price_evidence_but_add_local_watch | local_watch_yes_full_4B_no_without_non_price_evidence |
| R13L83-X03 | high_MAE_positive_riskwatch | R6, R9, R10 | positive_allowed_only_with_RiskWatch | do_not_green_high_MAE_without_extra_bridge |
| R13L83-X04 | theme_headline_false_positive_review | R5, R8, R10, R11, R12 | demote_theme_only_stage2 | theme_only_not_actionable |
| R13L83-X05 | hard_4C_non_price_thesis_break_protection | R3, R10, R13 | hard_4C_requires_non_price_thesis_break_keep_price_only_as_watch | hard_4C_blocked_without_non_price_break |
| R13L83-X06 | canonical_specific_bridge_compression_review | R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12 | compress_into_bridge_required_family_not_new_global_weight | do_not_apply_new_global_weight |

## 7. R13 Finding 1 — Source Repair Blocks Runtime Promotion

Loop83 produced many useful shadow candidates, but most of them are still marked `source_proxy_only / evidence_url_pending`.

The cross-rule is:

```text
If primary evidence URL is missing, keep the row for calibration ledger / source-repair queue.
Do not promote it into runtime scoring.
Do not convert price alignment alone into Stage2-Actionable.
```

This keeps the research corpus useful without letting unverified narratives leak into production behavior.

## 8. R13 Finding 2 — Local 4B Watch Can Be Earlier Than Full 4B

Across C24, C27, C29, C31 and tourism-policy C31, there are cases where MFE came quickly and then drawdown followed. Full 4B still requires non-price evidence, but local 4B watch is useful when price outruns the bridge.

```text
local_4B_watch = allowed when MFE outruns evidence bridge
full_4B = still requires non-price evidence
hard_4C = never price-only
```

This preserves the existing calibrated principle while making timing less blind.

## 9. R13 Finding 3 — High-MAE Positives Are Not Clean Green

R6/C21, R9/C29 and R10/C30 show the same shape in different costumes: the thesis can be partly right, but the entry path has enough MAE that the model should keep the case under RiskWatch.

```text
positive_MFE + high_MAE = Stage2-Actionable with RiskWatch
positive_MFE + high_MAE != Stage3-Green
```

The mechanism is simple. A bridge can point in the right direction and still shake too much for a fully loaded truck.

## 10. R13 Finding 4 — Theme-Only Stage2 Remains the Largest False-Positive Family

Consumer reopening, content IP, housing/PF, utility policy and tourism reopening all show the same false-positive contour:

```text
headline / narrative / theme beta
→ short or low MFE
→ high MAE
→ no durable rerating
```

The fix should not be one global penalty. Each canonical needs its own bridge:

```text
C19 = inventory-turn / sell-through / reorder / gross-margin bridge
C27 = launch / live-ops / sales ranking / retention / ARPU bridge
C30 = PF refinancing / debt / project-loss / margin bridge
C31 utility = direct beneficiary / tariff / pass-through / FCF bridge
C31 tourism = visitor / drop / sales / occupancy / margin bridge
```

## 11. R13 Finding 5 — Hard 4C Needs Non-Price Thesis Break

C12 and C30-style cases can show very deep MAE or post-peak drawdown. That is not enough for hard 4C.

```text
price-only crash = watch / risk flag
hard_4C = non-price thesis break required
```

Examples of non-price evidence needed before hard 4C:

```text
- confirmed OEM call-off collapse
- financing / covenant / debt liquidity failure
- project-loss or impairment path
- policy reversal
- regulatory or legal block
- cash-runway break
```

## 12. Stage2 / Yellow / Green / 4B / 4C Cross Comparison

| gate | loop83 cross result | R13 decision |
|---|---|---|
| Stage2-Actionable | works when bridge evidence exists | keep, but require canonical bridge |
| Stage3-Yellow | useful as intermediate evidence state | keep |
| Stage3-Green | too dangerous under high-MAE/source-proxy conditions | block unless bridge + low MAE + source quality pass |
| Local 4B Watch | often needed before full 4B | allow as watch-only state |
| Full 4B | still needs non-price evidence | keep requirement |
| Hard 4C | price-only drawdown is not enough | keep non-price thesis-break requirement |

## 13. Before / After Cross-Checkpoint Comparison

| checkpoint profile | new independent cases | false-positive handling | 4B timing | 4C routing | production impact |
|---|---:|---|---|---|---|
| P0 current calibrated proxy | 0 | good but source-proxy can still tempt promotion | full 4B can be late | mostly protected | none |
| P1 R13 cross-checkpoint shadow | 0 | source-proxy blocked, theme-only demoted | local watch added, full 4B unchanged | hard 4C non-price only | none |

## 14. Score-Return Alignment Matrix

| cross_case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R13L83-X01 | 62 | Stage2-Watch/Actionable candidate | 49 | Hold: source-repair queue | improved |
| R13L83-X02 | 70 | Stage2/Stage3 with late 4B | 76 | Stage2/Stage3 + Local 4B Watch | improved |
| R13L83-X03 | 68 | Stage2-Actionable or Yellow candidate | 72 | Stage2-Actionable + high-MAE RiskWatch; Green blocked | improved |
| R13L83-X04 | 60 | Stage2-Watch/FalsePositive | 45 | Rejected-Stage2 / RiskWatch | improved |
| R13L83-X05 | 64 | possible hard 4C | 70 | 4C-watch only until non-price thesis break | improved |
| R13L83-X06 | 58 | possible new global rule | 72 | canonical-specific shadow family only | improved |

## 15. Coverage Matrix

| large_sector_id | canonical_archetype_id | positive | counterexample | 4B | 4C | new cases | reused source MDs | usable cross triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 0 | 0 | 1-watch family | 1-watch family | 0 | 12 | 6 | 6 | no | cross checkpoint only | source repair / evidence URL repair |

## 16. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 12
reused_case_ids: R1~R12 loop83 source MDs
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 0
new_trigger_family_count: 0
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
residual_error_types_found:
  - source_proxy_runtime_promotion_risk
  - local_4B_late_when_MFE_outruns_bridge
  - high_MAE_positive_Green_blocker
  - theme_headline_false_positive
  - price_only_hard_4C_misroute_risk
  - global_weight_overfit_risk
new_axis_proposed: false
existing_axis_strengthened:
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: R13_cross_checkpoint_only
no_new_signal_reason: R13 is cross-archetype checkpoint, not sector research
loop_contribution_label: cross_archetype_redteam_checkpoint
do_not_propose_new_weight_delta: true
do_not_count_as_new_case: true
```

## 17. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- R13 scheduled round/loop consistency
- R13 large_sector_id hard gate
- R13 canonical scope
- source MD inventory for loop83 R1~R12
- do_not_count_as_new_case policy
- cross-checkpoint machine-readable rows
- hard 4C protection principle
- local-vs-full 4B distinction
```

Not validated in this MD:

```text
- new primary evidence URL
- new OHLC entry window
- new independent case
- new stock symbol
- production scoring implementation
- code patch
```

## 18. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_loop83_cross_archetype_4B_4C_high_MAE_source_repair_guardrail,cross_archetype_checkpoint_only,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Loop83 R1~R12 cases repeatedly show source-proxy rows must not promote, local 4B watch can precede full 4B, hard 4C requires non-price thesis break, and high-MAE positives remain RiskWatch","no production weight; reinforces existing axes","R13L83-X01-S2FP-SOURCE-REPAIR|R13L83-X02-4B-LOCAL-FULL|R13L83-X03-HIGH-MAE-GUARD|R13L83-X04-THEME-FALSEPOS|R13L83-X05-4C-PROTECT|R13L83-X06-CANONICAL-COMPRESSION",6,0,0,medium,r13_cross_checkpoint_shadow_only,"do_not_count_as_new_case=true; source repair required; not production"
```

## 19. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "cross_checkpoint_uses_source_MD_price_validations"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R1", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R1", "source_file": "docs/round/e2r_stock_web_v12_residual_round_R1_loop_83_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "source_axis": "industrial_order_backlog_margin_bridge_guardrail", "checkpoint": "order/backlog/delivery/margin bridge; avoid cycle-fade positives", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R2", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R2", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "source_axis": "C10_order_refresh_required_after_memory_recovery_beta", "checkpoint": "memory-recovery beta needs order refresh after initial cycle turn", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R3", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R3", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "source_axis": "C12_customer_calloff_bridge_required_for_upstream_supplier_stage2_actionable", "checkpoint": "upstream battery supplier requires OEM call-off/utilization bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R4", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R4", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_83_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "source_canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "source_axis": "C16_customer_offtake_utilization_margin_bridge_required", "checkpoint": "resource policy headline needs offtake/utilization/repricing/margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R5", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R5", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_83_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "source_axis": "C19_inventory_margin_bridge_required", "checkpoint": "traffic/reopening/destocking headline needs inventory-turn/sell-through/reorder/gross-margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R6", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R6", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_83_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "source_canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "source_axis": "C21_capital_return_execution_and_capital_buffer_bridge_required", "checkpoint": "value-up/low-PBR headline needs CET1/capital buffer and buyback/dividend execution", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R7", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R7", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_83_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "source_axis": "C24_trial_data_partner_milestone_cash_runway_bridge_required", "checkpoint": "trial/platform MFE needs data-quality/partner/milestone/cash-runway bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R8", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R8", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_83_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "source_axis": "C27_liveops_retention_global_monetization_bridge_required", "checkpoint": "IP/global launch headline needs sales ranking/live-ops/retention/ARPU bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R9", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R9", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "source_axis": "C29_volume_yield_cost_margin_bridge_required", "checkpoint": "traffic/capacity recovery needs yield/cost/load-factor/contract-mix/margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R10", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R10", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_83_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "source_axis": "C30_PF_refinancing_debt_margin_bridge_required", "checkpoint": "housing recovery needs PF refinancing/debt/project-loss/orderbook/margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R11", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R11", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_83_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_axis": "C31_policy_direct_beneficiary_tariff_margin_bridge_required", "checkpoint": "utility policy needs direct beneficiary and tariff/subsidy/revenue/margin/FCF bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L83-SOURCE-R12", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "source_round": "R12", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_83_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_axis": "C31_tourism_policy_visitor_drop_margin_bridge_required", "checkpoint": "tourism policy/reopening needs visitor/drop/sales/occupancy/margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "trigger", "trigger_id": "R13L83-X01-S2FP-SOURCE-REPAIR", "case_id": "R13L83-X01", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop83 checkpoint", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP83_CROSS_ARCHETYPE_PRICE_ONLY_BLOWOFF_HIGH_MAE_SOURCE_REPAIR_4B_4C_GUARDRAIL", "loop_objective": "cross_archetype_redteam_checkpoint|stage2_false_positive_review|4B_4C_redteam|high_MAE_guardrail|source_repair_review", "trigger_type": "R13_CROSS_SOURCE_REPAIR_BLOCKER", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "non-price bridge cannot be trusted until primary evidence URLs repair the row", "evidence_source": "derived_from_loop83_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R2", "R3", "R4", "R5", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_group": "C10|C12|C16|C19|C24|C27|C29|C30|C31", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MFE_proxy_label": "mixed", "MAE_proxy_label": "mixed", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "block_runtime_promotion_until_source_repair", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "hold_shadow_only_do_not_promote", "current_profile_verdict": "block_runtime_promotion_until_source_repair", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "source_proxy_evidence_url_pending_blocker", "residual_error": "source_proxy_only/evidence_url_pending remains too common in loop83"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L83-X01", "trigger_id": "R13L83-X01-S2FP-SOURCE-REPAIR", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"direct_evidence_confidence": 20, "price_alignment_score": 60, "bridge_confirmation_score": 25, "source_quality_score": 20, "runtime_promotion_score": 45, "false_positive_risk_score": 65}, "weighted_score_before": 62, "stage_label_before": "Stage2-Watch/Actionable candidate", "raw_component_scores_after": {"direct_evidence_confidence": 10, "price_alignment_score": 60, "bridge_confirmation_score": 15, "source_quality_score": 5, "runtime_promotion_score": 0, "false_positive_risk_score": 80}, "weighted_score_after": 49, "stage_label_after": "Hold: source-repair queue", "changed_components": ["source_quality_score", "bridge_confirmation_score", "riskwatch_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "non-price bridge cannot be trusted until primary evidence URLs repair the row", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "hold_shadow_only_do_not_promote", "current_profile_verdict": "block_runtime_promotion_until_source_repair", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L83-X02-4B-LOCAL-FULL", "case_id": "R13L83-X02", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop83 checkpoint", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP83_CROSS_ARCHETYPE_PRICE_ONLY_BLOWOFF_HIGH_MAE_SOURCE_REPAIR_4B_4C_GUARDRAIL", "loop_objective": "cross_archetype_redteam_checkpoint|stage2_false_positive_review|4B_4C_redteam|high_MAE_guardrail|source_repair_review", "trigger_type": "R13_CROSS_4B_TIMING_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "local 4B watch is needed when price runs ahead of milestone/liveops/yield/policy bridge", "evidence_source": "derived_from_loop83_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R7", "R8", "R9", "R11", "R12"], "source_canonical_group": "C24|C27|C29|C31", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MFE_proxy_label": "high_MFE_positive_but_later_drawdown", "MAE_proxy_label": "controlled_to_high", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_watch_yes_full_4B_no_without_non_price_evidence", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "keep_full_4B_requires_non_price_evidence_but_add_local_watch", "current_profile_verdict": "local_watch_yes_full_4B_no_without_non_price_evidence", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "local_4B_vs_full_window_4B_timing", "residual_error": "large MFE followed by drawdown can make full 4B late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L83-X02", "trigger_id": "R13L83-X02-4B-LOCAL-FULL", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"price_mfe_overextension_score": 70, "non_price_bridge_score": 35, "local_peak_proximity_score": 80, "full_peak_confirmation_score": 45, "thesis_break_evidence_score": 20, "timing_error_risk_score": 70}, "weighted_score_before": 70, "stage_label_before": "Stage2/Stage3 with late 4B", "raw_component_scores_after": {"price_mfe_overextension_score": 70, "non_price_bridge_score": 35, "local_peak_proximity_score": 90, "full_peak_confirmation_score": 45, "thesis_break_evidence_score": 20, "timing_error_risk_score": 45}, "weighted_score_after": 76, "stage_label_after": "Stage2/Stage3 + Local 4B Watch", "changed_components": ["source_quality_score", "bridge_confirmation_score", "riskwatch_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "local 4B watch is needed when price runs ahead of milestone/liveops/yield/policy bridge", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "keep_full_4B_requires_non_price_evidence_but_add_local_watch", "current_profile_verdict": "local_watch_yes_full_4B_no_without_non_price_evidence", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L83-X03-HIGH-MAE-GUARD", "case_id": "R13L83-X03", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop83 checkpoint", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP83_CROSS_ARCHETYPE_PRICE_ONLY_BLOWOFF_HIGH_MAE_SOURCE_REPAIR_4B_4C_GUARDRAIL", "loop_objective": "cross_archetype_redteam_checkpoint|stage2_false_positive_review|4B_4C_redteam|high_MAE_guardrail|source_repair_review", "trigger_type": "R13_CROSS_HIGH_MAE_GUARDRAIL", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "capital-return, airline capacity, and construction recovery cases can be right but still too volatile for clean Green", "evidence_source": "derived_from_loop83_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R6", "R9", "R10"], "source_canonical_group": "C21|C29|C30", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MFE_proxy_label": "positive", "MAE_proxy_label": "high", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "do_not_green_high_MAE_without_extra_bridge", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "positive_allowed_only_with_RiskWatch", "current_profile_verdict": "do_not_green_high_MAE_without_extra_bridge", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "high_MAE_positive_riskwatch", "residual_error": "positive MFE does not neutralize early high-MAE risk"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L83-X03", "trigger_id": "R13L83-X03-HIGH-MAE-GUARD", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"mfe_quality_score": 55, "mae_control_score": 20, "bridge_confirmation_score": 35, "riskwatch_score": 30, "green_readiness_score": 55, "drawdown_risk_score": 75}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable or Yellow candidate", "raw_component_scores_after": {"mfe_quality_score": 55, "mae_control_score": 20, "bridge_confirmation_score": 35, "riskwatch_score": 80, "green_readiness_score": 40, "drawdown_risk_score": 75}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + high-MAE RiskWatch; Green blocked", "changed_components": ["source_quality_score", "bridge_confirmation_score", "riskwatch_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "capital-return, airline capacity, and construction recovery cases can be right but still too volatile for clean Green", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "positive_allowed_only_with_RiskWatch", "current_profile_verdict": "do_not_green_high_MAE_without_extra_bridge", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L83-X04-THEME-FALSEPOS", "case_id": "R13L83-X04", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop83 checkpoint", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP83_CROSS_ARCHETYPE_PRICE_ONLY_BLOWOFF_HIGH_MAE_SOURCE_REPAIR_4B_4C_GUARDRAIL", "loop_objective": "cross_archetype_redteam_checkpoint|stage2_false_positive_review|4B_4C_redteam|high_MAE_guardrail|source_repair_review", "trigger_type": "R13_CROSS_STAGE2_FALSE_POSITIVE_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "reopening, IP, housing, utility-policy and tourism headlines fail without bridge-to-economics", "evidence_source": "derived_from_loop83_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R5", "R8", "R10", "R11", "R12"], "source_canonical_group": "C19|C27|C30|C31", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MFE_proxy_label": "low_or_short_lived", "MAE_proxy_label": "high", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "theme_only_not_actionable", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "demote_theme_only_stage2", "current_profile_verdict": "theme_only_not_actionable", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "theme_headline_false_positive_review", "residual_error": "theme narratives repeatedly produce low-MFE/high-MAE profiles"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L83-X04", "trigger_id": "R13L83-X04-THEME-FALSEPOS", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"headline_strength_score": 65, "bridge_confirmation_score": 15, "price_momentum_score": 45, "evidence_quality_score": 20, "stage2_actionable_score": 60, "false_positive_risk_score": 75}, "weighted_score_before": 60, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"headline_strength_score": 20, "bridge_confirmation_score": 5, "price_momentum_score": 30, "evidence_quality_score": 10, "stage2_actionable_score": 25, "false_positive_risk_score": 85}, "weighted_score_after": 45, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["source_quality_score", "bridge_confirmation_score", "riskwatch_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "reopening, IP, housing, utility-policy and tourism headlines fail without bridge-to-economics", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "demote_theme_only_stage2", "current_profile_verdict": "theme_only_not_actionable", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L83-X05-4C-PROTECT", "case_id": "R13L83-X05", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop83 checkpoint", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP83_CROSS_ARCHETYPE_PRICE_ONLY_BLOWOFF_HIGH_MAE_SOURCE_REPAIR_4B_4C_GUARDRAIL", "loop_objective": "cross_archetype_redteam_checkpoint|stage2_false_positive_review|4B_4C_redteam|high_MAE_guardrail|source_repair_review", "trigger_type": "R13_CROSS_4C_PROTECTION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "battery call-off and PF/debt cases need non-price demand, financing, covenant or project-loss break evidence", "evidence_source": "derived_from_loop83_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R3", "R10", "R13"], "source_canonical_group": "C12|C30|R13", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MFE_proxy_label": "not_primary", "MAE_proxy_label": "very_high", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4C_blocked_without_non_price_break", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "hard_4C_requires_non_price_thesis_break_keep_price_only_as_watch", "current_profile_verdict": "hard_4C_blocked_without_non_price_break", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "hard_4C_non_price_thesis_break_protection", "residual_error": "large drawdown can tempt hard 4C, but price-only hard 4C is prohibited"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L83-X05", "trigger_id": "R13L83-X05-4C-PROTECT", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"price_drawdown_score": 85, "thesis_break_evidence_score": 20, "non_price_confirmation_score": 20, "hard_4c_score": 70, "watch_score": 40, "misroute_risk_score": 75}, "weighted_score_before": 64, "stage_label_before": "possible hard 4C", "raw_component_scores_after": {"price_drawdown_score": 85, "thesis_break_evidence_score": 20, "non_price_confirmation_score": 20, "hard_4c_score": 25, "watch_score": 85, "misroute_risk_score": 35}, "weighted_score_after": 70, "stage_label_after": "4C-watch only until non-price thesis break", "changed_components": ["source_quality_score", "bridge_confirmation_score", "riskwatch_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "battery call-off and PF/debt cases need non-price demand, financing, covenant or project-loss break evidence", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "hard_4C_requires_non_price_thesis_break_keep_price_only_as_watch", "current_profile_verdict": "hard_4C_blocked_without_non_price_break", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L83-X06-CANONICAL-COMPRESSION", "case_id": "R13L83-X06", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop83 checkpoint", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP83_CROSS_ARCHETYPE_PRICE_ONLY_BLOWOFF_HIGH_MAE_SOURCE_REPAIR_4B_4C_GUARDRAIL", "loop_objective": "cross_archetype_redteam_checkpoint|stage2_false_positive_review|4B_4C_redteam|high_MAE_guardrail|source_repair_review", "trigger_type": "R13_CROSS_CANONICAL_RULE_COMPRESSION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "same global weight would overfit; each canonical needs its own economic bridge", "evidence_source": "derived_from_loop83_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_group": "all_loop83_canonicals", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MFE_proxy_label": "cross_mixed", "MAE_proxy_label": "cross_mixed", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "do_not_apply_new_global_weight", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "compress_into_bridge_required_family_not_new_global_weight", "current_profile_verdict": "do_not_apply_new_global_weight", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "canonical_specific_bridge_compression_review", "residual_error": "each sector has a different bridge, but the shared failure is headline-to-economics gap"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L83-X06", "trigger_id": "R13L83-X06-CANONICAL-COMPRESSION", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "raw_component_scores_before": {"global_rule_simplicity_score": 70, "canonical_specificity_score": 35, "overfit_risk_score": 70, "bridge_family_score": 60, "production_readiness_score": 35, "source_repair_need_score": 70}, "weighted_score_before": 58, "stage_label_before": "possible new global rule", "raw_component_scores_after": {"global_rule_simplicity_score": 35, "canonical_specificity_score": 75, "overfit_risk_score": 35, "bridge_family_score": 80, "production_readiness_score": 25, "source_repair_need_score": 70}, "weighted_score_after": 72, "stage_label_after": "canonical-specific shadow family only", "changed_components": ["source_quality_score", "bridge_confirmation_score", "riskwatch_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "same global weight would overfit; each canonical needs its own economic bridge", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "compress_into_bridge_required_family_not_new_global_weight", "current_profile_verdict": "do_not_apply_new_global_weight", "do_not_count_as_new_case": true}
{"row_type": "shadow_weight", "axis": "R13_loop83_cross_archetype_4B_4C_high_MAE_source_repair_guardrail", "scope": "cross_archetype_checkpoint_only", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Loop83 R1~R12 cases repeatedly show that source_proxy rows must not promote, local 4B watch can precede full 4B, hard 4C requires non-price thesis break, and high-MAE positives must remain RiskWatch.", "backtest_effect": "no new production weight; cross-checkpoint reinforces existing calibrated axes", "trigger_ids": "R13L83-X01-S2FP-SOURCE-REPAIR|R13L83-X02-4B-LOCAL-FULL|R13L83-X03-HIGH-MAE-GUARD|R13L83-X04-THEME-FALSEPOS|R13L83-X05-4C-PROTECT|R13L83-X06-CANONICAL-COMPRESSION", "calibration_usable_count": 6, "new_independent_case_count": 0, "counterexample_count": 0, "confidence": "medium", "proposal_type": "r13_cross_checkpoint_shadow_only", "notes": "do_not_count_as_new_case=true; not production; source repair still required"}
{"row_type": "residual_contribution", "round": "R13", "loop": 83, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "new_independent_case_count": 0, "reused_case_count": 12, "new_symbol_count": 0, "new_trigger_family_count": 0, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["source_proxy_runtime_promotion_risk", "local_4B_late_when_MFE_outruns_bridge", "high_MAE_positive_Green_blocker", "theme_headline_false_positive", "price_only_hard_4C_misroute_risk", "global_weight_overfit_risk"], "loop_contribution_label": "cross_archetype_redteam_checkpoint", "do_not_propose_new_weight_delta": true, "do_not_count_as_new_case": true}
```

## 20. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

This R13 file is not live candidate research and is not a new sector-positive source. It is a cross-archetype checkpoint over loop83 R1~R12 source MDs.

### Rules

- Treat every R13 `trigger` row as `do_not_count_as_new_case=true`.
- Do not add R13 rows to new independent case counts.
- Do not infer new runtime weights from R13 alone.
- Use R13 rows to validate guardrails:
  - source_proxy_only/evidence_url_pending blocks runtime promotion
  - local 4B watch can exist before full 4B
  - full 4B requires non-price evidence
  - hard 4C requires non-price thesis break
  - high-MAE positives should not go clean Green
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.

## 21. Next Round State

```text
completed_round = R13
completed_loop = 83
next_round = R1
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

## 22. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
