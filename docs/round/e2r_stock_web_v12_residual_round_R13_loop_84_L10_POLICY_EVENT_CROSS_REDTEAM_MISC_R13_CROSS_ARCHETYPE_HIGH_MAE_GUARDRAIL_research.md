# E2R Stock-Web v12 Residual Research — R13 Loop 84 / L10 / High-MAE Guardrail Checkpoint

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 84,
  "computed_next_round": "R1",
  "computed_next_loop": 85,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "fine_archetype_id": "LOOP84_HIGH_MAE_POSITIVE_GREEN_BLOCKER_SOURCE_REPAIR_LOCAL_4B_HARD_4C_CHECKPOINT",
  "loop_objective": [
    "cross_archetype_high_MAE_guardrail_checkpoint",
    "stage2_positive_with_high_MAE_review",
    "clean_Green_blocker_review",
    "local_4B_timing_review",
    "hard_4C_non_price_thesis_break_protection",
    "source_proxy_runtime_promotion_blocker_review",
    "canonical_bridge_family_compression",
    "do_not_count_as_new_sector_case",
    "do_not_propose_new_weight_delta"
  ],
  "source_round_span": "R1~R12 loop 84",
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true,
  "do_not_count_as_new_case": true,
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
scheduled_loop = 84
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC only
selected_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
computed_next_round = R1
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R13 is not a new sector research round. It is a cross-archetype checkpoint. Therefore this MD does not add new positive cases, does not add new symbols, and does not count source cases again.

```text
new_independent_case_count = 0
new_symbol_count = 0
do_not_count_as_new_case = true
do_not_count_as_new_sector_case = true
```

## 3. No-Repeat / Duplicate Handling

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
R13_cross_case_policy = do_not_count_as_new_case=true
```

This file deliberately avoids creating a new C18/C22/C25/C28 sector row under R13. Every machine-readable R13 `trigger` row is a cross-checkpoint with `independent_evidence_weight = 0.0`.

## 4. Stock-Web Price Source Context

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

R13 does not compute a fresh OHLC entry window. It inherits the Stock-Web validations and trigger-level MFE/MAE calculations from R1~R12 loop84 source MDs.

## 5. Source MD Inventory — Loop 84

| round | large_sector_id | source canonical | source axis | checkpoint role |
|---|---|---|---|---|
| R1 | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | `C05_engineering_EPC_contract_backlog_margin_bridge_required` | engineering/EPC theme needs named contract, backlog/fee duration, cost pass-through and margin bridge |
| R2 | L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | `C09_advanced_equipment_order_qualification_revenue_bridge_required` | advanced-equipment MFE needs named order, qualification, tool acceptance and revenue/margin bridge |
| R3 | L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | `C13_AMPC_JV_customer_calloff_utilization_margin_bridge_required` | AMPC/JV/localization MFE needs call-off, utilization, subsidy capture and margin bridge |
| R4 | L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | `C15_material_price_to_product_spread_margin_bridge_required` | commodity/material MFE needs realized product spread, inventory valuation, customer volume and margin conversion |
| R5 | L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | `C18_export_channel_sellthrough_reorder_margin_bridge_required` | export-channel MFE needs sell-through, reorder cadence, capacity fulfillment and gross-margin bridge |
| R6 | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | `C22_rate_cycle_CSM_reserve_capital_return_bridge_required` | insurance MFE needs CSM quality, reserve adequacy, solvency buffer and capital-return execution |
| R7 | L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | `C25_device_export_installbase_reorder_reimbursement_margin_bridge_required` | medical-device MFE needs install-base utilization, distributor reorder, reimbursement/regulatory and margin bridge |
| R8 | L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | `C28_contract_retention_ARR_renewal_churn_margin_bridge_required` | software/security MFE needs recurring base, ARR/maintenance, renewal quality, churn control and margin conversion |
| R9 | L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | `C29_mobility_volume_utilization_cost_spread_margin_bridge_required` | tire/auto-parts MFE needs shipment volume, utilization, ASP/raw-material spread and margin conversion |
| R10 | L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | `C30_PF_debt_orderbook_project_margin_bridge_required` | construction/PF MFE needs PF refinancing, debt control, orderbook quality and project-margin bridge |
| R11 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | `C32_tender_transaction_floor_binding_terms_closing_bridge_required` | governance/control-premium MFE needs tender/transaction floor, binding terms and closing/capital-return bridge |
| R12 | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | `C31_agri_food_policy_input_cost_inventory_margin_bridge_required` | agri-food policy MFE needs input-cost, inventory, ASP pass-through, demand and gross-margin bridge |

## 6. Cross-Archetype High-MAE Checkpoint Rows

| cross_case_id | cross_scope | source rounds | decision | verdict |
|---|---|---|---|---|
| R13L84-HM01 | high_MAE_positive_clean_Green_blocker | R1, R5, R6, R7, R8, R9, R10 | positive_allowed_only_with_RiskWatch_Green_blocked | do_not_green_high_MAE_positive_without_extra_bridge |
| R13L84-HM02 | local_4B_before_full_4B_when_MFE_outruns_bridge | R2, R3, R5, R7, R11 | local_4B_watch_allowed_full_4B_still_non_price_required | local_watch_yes_full_4B_no_without_non_price_evidence |
| R13L84-HM03 | theme_headline_false_positive_high_MAE_review | R1, R4, R8, R10, R12 | demote_theme_only_stage2 | theme_only_MFE_not_stage2_actionable |
| R13L84-HM04 | source_proxy_evidence_url_pending_runtime_blocker | R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12 | hold_shadow_only_do_not_promote | block_runtime_promotion_until_source_repair |
| R13L84-HM05 | hard_4C_non_price_thesis_break_protection | R3, R10, R11, R12 | hard_4C_requires_non_price_break_keep_price_drawdown_as_watch | hard_4C_blocked_without_non_price_break |
| R13L84-HM06 | canonical_specific_bridge_family_compression | R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12 | compress_into_canonical_bridge_family_not_global_weight | do_not_apply_new_global_weight |

## 7. R13 Finding 1 — High-MAE Positives Are Not Clean Green

Loop84 repeatedly produced the same contour:

```text
positive MFE
+ high MAE or deep post-peak drawdown
+ source_proxy_only evidence
= Stage2-Actionable may survive, but clean Green is blocked
```

This appeared across engineering, consumer export, insurance, medical devices, software, mobility and construction/PF. The correct behavior is not to throw away every positive. It is to put a shock absorber between Stage2 and Green.

## 8. R13 Finding 2 — Local 4B Watch Is Earlier Than Full 4B

The loop84 positive cases often had MFE before the evidence bridge could be source-repaired. Full 4B still needs non-price evidence, but local 4B watch is appropriate when price outruns the bridge.

```text
local_4B_watch = allowed when MFE outruns evidence bridge
full_4B = still requires non-price evidence
hard_4C = never price-only
```

A local 4B watch is the yellow light before the intersection. It does not say the road is closed; it says speed has outrun visibility.

## 9. R13 Finding 3 — Source Proxy Blocks Runtime Promotion

Every loop84 sector MD still carries `source_proxy_only / evidence_url_pending` on the selected evidence rows.

```text
source_proxy_only = calibration ledger allowed
source_proxy_only != runtime scoring promotion
evidence_url_pending = source-repair queue
```

Price can confirm that a trigger was interesting. It cannot prove the original non-price bridge by itself.

## 10. R13 Finding 4 — Theme-Only Stage2 Remains the Recurrent False-Positive Shape

Across loop84, the false positives share a simple shape:

```text
headline or theme beta
→ short MFE
→ high MAE or post-peak drawdown
→ missing bridge-to-economics
```

But the bridge is different by canonical:

```text
C05 = named EPC/engineering contract + backlog/fee duration + margin bridge
C09 = named order + customer qualification + tool acceptance + revenue bridge
C13 = customer call-off + utilization + subsidy capture + margin bridge
C15 = realized product spread + inventory valuation + customer volume + gross-margin bridge
C18 = sell-through + reorder cadence + capacity fulfillment + gross-margin bridge
C22 = CSM quality + reserve adequacy + solvency buffer + capital-return execution
C25 = install-base utilization + distributor reorder + reimbursement/regulatory + margin bridge
C28 = ARR/maintenance + renewal quality + churn control + margin conversion
C29 = shipment volume + utilization + ASP/raw-material spread + margin conversion
C30 = PF refinancing + debt/liquidity + orderbook quality + project-margin bridge
C31 = input-cost + inventory + ASP pass-through + volume/demand + gross-margin bridge
C32 = tender/transaction floor + binding terms + closing/capital-return bridge
```

## 11. R13 Finding 5 — Hard 4C Requires Non-Price Thesis Break

Loop84 had several deep drawdowns, but hard 4C cannot be assigned by price alone.

```text
price-only crash = watch / risk flag
hard_4C = non-price thesis break required
```

Examples of non-price breaks that would be required:

```text
- customer call-off collapse
- subsidy or policy reversal
- debt liquidity / PF refinancing failure
- project-loss or impairment confirmation
- tender withdrawal or deal break
- churn / contract loss
- raw-material spread break
```

## 12. Stage2 / Yellow / Green / 4B / 4C Cross Comparison

| gate | loop84 cross result | R13 decision |
|---|---|---|
| Stage2-Actionable | allowed when bridge-positive, but source repair still pending | keep as shadow only |
| Stage3-Yellow | useful intermediate state when bridge quality is partial | keep |
| Stage3-Green | unsafe under high-MAE or source-proxy conditions | block until bridge + source quality + MAE control pass |
| Local 4B Watch | frequently needed when MFE outruns bridge | allow |
| Full 4B | still needs non-price deterioration evidence | keep requirement |
| Hard 4C | price drawdown alone is insufficient | keep non-price thesis-break requirement |

## 13. Before / After Cross-Checkpoint Comparison

| checkpoint profile | new independent cases | false-positive handling | high-MAE handling | 4B timing | 4C routing | production impact |
|---|---:|---|---|---|---|---|
| P0 current calibrated proxy | 0 | theme-only may still tempt Stage2 | positives can drift toward Green | full 4B can be late | mostly protected | none |
| P1 R13 high-MAE checkpoint | 0 | theme-only demoted | clean Green blocked under high-MAE/source-proxy | local watch added, full 4B unchanged | hard 4C non-price only | none |

## 14. Score-Return Alignment Matrix

| cross_case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R13L84-HM01 | 72 | Stage2-Actionable or Green candidate | 76 | Stage2-Actionable + high-MAE RiskWatch; Green blocked | improved |
| R13L84-HM02 | 69 | Stage2/Stage3 with late full 4B | 78 | Stage2/Stage3 + Local 4B Watch | improved |
| R13L84-HM03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / RiskWatch | improved |
| R13L84-HM04 | 63 | Stage2-Actionable candidate | 48 | Hold: source-repair queue | improved |
| R13L84-HM05 | 64 | possible hard 4C | 72 | 4C-watch only until non-price thesis break | improved |
| R13L84-HM06 | 58 | possible new global rule | 74 | canonical-specific shadow family only | improved |

## 15. Coverage Matrix

| large_sector_id | canonical_archetype_id | positive | counterexample | 4B | 4C | new cases | reused source MDs | usable cross triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 0 | 0 | 1-watch family | 1-watch family | 0 | 12 | 6 | 6 | no | cross checkpoint only | source repair / high-MAE threshold audit |

## 16. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 12
reused_case_ids: R1~R12 loop84 source MDs
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
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - high_MAE_positive_clean_Green_blocker
  - source_proxy_runtime_promotion_risk
  - local_4B_late_when_MFE_outruns_bridge
  - theme_headline_false_positive_high_MAE
  - price_only_hard_4C_misroute_risk
  - global_weight_overfit_risk
new_axis_proposed: false
existing_axis_strengthened:
  - high_MAE_blocks_clean_Green
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: R13_cross_checkpoint_only
no_new_signal_reason: R13 is cross-archetype checkpoint, not sector research
loop_contribution_label: cross_archetype_high_MAE_guardrail_checkpoint
do_not_propose_new_weight_delta: true
do_not_count_as_new_case: true
```

## 17. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- R13 scheduled round/loop consistency
- R13 large_sector_id hard gate
- R13 canonical scope
- source MD inventory for loop84 R1~R12
- do_not_count_as_new_case policy
- cross-checkpoint machine-readable rows
- high-MAE Green blocker principle
- source-proxy runtime blocker principle
- local-vs-full 4B distinction
- hard 4C non-price thesis-break principle
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
shadow_weight,R13_loop84_cross_archetype_high_MAE_source_repair_local_4B_guardrail,cross_archetype_checkpoint_only,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,1,+1,"Loop84 R1~R12 cases repeatedly show high-MAE positives should not become clean Green, source-proxy rows must not promote, local 4B can precede full 4B, and hard 4C requires non-price thesis break","no production weight; reinforces existing axes","R13L84-HM01-HIGH-MAE-GREEN-BLOCKER|R13L84-HM02-LOCAL-4B-MFE-OUTRUNS-BRIDGE|R13L84-HM03-THEME-FALSEPOS-HIGH-MAE|R13L84-HM04-SOURCE-PROXY-BLOCKER|R13L84-HM05-HARD-4C-NONPRICE|R13L84-HM06-BRIDGE-FAMILY-COMPRESSION",6,0,0,medium,r13_cross_checkpoint_shadow_only,"do_not_count_as_new_case=true; source repair required; not production"
```

## 19. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "cross_checkpoint_uses_source_MD_price_validations"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R1", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R1", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_84_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "source_axis": "C05_engineering_EPC_contract_backlog_margin_bridge_required", "checkpoint": "engineering/EPC theme needs named contract, backlog/fee duration, cost pass-through and margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R2", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R2", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_84_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "source_axis": "C09_advanced_equipment_order_qualification_revenue_bridge_required", "checkpoint": "advanced-equipment MFE needs named order, qualification, tool acceptance and revenue/margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R3", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R3", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_84_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "source_axis": "C13_AMPC_JV_customer_calloff_utilization_margin_bridge_required", "checkpoint": "AMPC/JV/localization MFE needs call-off, utilization, subsidy capture and margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R4", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R4", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_84_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "source_large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "source_canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "source_axis": "C15_material_price_to_product_spread_margin_bridge_required", "checkpoint": "commodity/material MFE needs realized product spread, inventory valuation, customer volume and margin conversion", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R5", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R5", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_84_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "source_canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "source_axis": "C18_export_channel_sellthrough_reorder_margin_bridge_required", "checkpoint": "export-channel MFE needs sell-through, reorder cadence, capacity fulfillment and gross-margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R6", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R6", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_84_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "source_canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_axis": "C22_rate_cycle_CSM_reserve_capital_return_bridge_required", "checkpoint": "insurance MFE needs CSM quality, reserve adequacy, solvency buffer and capital-return execution", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R7", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R7", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_84_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "source_canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "source_axis": "C25_device_export_installbase_reorder_reimbursement_margin_bridge_required", "checkpoint": "medical-device MFE needs install-base utilization, distributor reorder, reimbursement/regulatory and margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R8", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R8", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_84_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "source_axis": "C28_contract_retention_ARR_renewal_churn_margin_bridge_required", "checkpoint": "software/security MFE needs recurring base, ARR/maintenance, renewal quality, churn control and margin conversion", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R9", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R9", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_84_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "source_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "source_axis": "C29_mobility_volume_utilization_cost_spread_margin_bridge_required", "checkpoint": "tire/auto-parts MFE needs shipment volume, utilization, ASP/raw-material spread and margin conversion", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R10", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R10", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_84_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "source_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "source_axis": "C30_PF_debt_orderbook_project_margin_bridge_required", "checkpoint": "construction/PF MFE needs PF refinancing, debt control, orderbook quality and project-margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R11", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R11", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_84_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "source_axis": "C32_tender_transaction_floor_binding_terms_closing_bridge_required", "checkpoint": "governance/control-premium MFE needs tender/transaction floor, binding terms and closing/capital-return bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "narrative_only", "narrative_id": "R13L84-SOURCE-R12", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_round": "R12", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_84_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_axis": "C31_agri_food_policy_input_cost_inventory_margin_bridge_required", "checkpoint": "agri-food policy MFE needs input-cost, inventory, ASP pass-through, demand and gross-margin bridge", "do_not_count_as_new_case": true, "calibration_usable": false, "notes": "R13 source inventory row; used for cross-checkpoint only"}
{"row_type": "trigger", "trigger_id": "R13L84-HM01-HIGH-MAE-GREEN-BLOCKER", "case_id": "R13L84-HM01", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop84 high-MAE checkpoint", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "LOOP84_HIGH_MAE_POSITIVE_GREEN_BLOCKER_SOURCE_REPAIR_LOCAL_4B_HARD_4C_CHECKPOINT", "loop_objective": "cross_archetype_high_MAE_guardrail|stage2_positive_review|local_4B_review|hard_4C_protection|source_repair_review", "trigger_type": "R13_CROSS_HIGH_MAE_GUARDRAIL", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "A case can be directionally right while still too unstable for clean Stage3-Green.", "evidence_source": "derived_from_loop84_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R5", "R6", "R7", "R8", "R9", "R10"], "source_canonical_group": "C05|C18|C22|C25|C28|C29|C30", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "do_not_green_high_MAE_positive_without_extra_bridge", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "positive_allowed_only_with_RiskWatch_Green_blocked", "current_profile_verdict": "do_not_green_high_MAE_positive_without_extra_bridge", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "high_MAE_positive_clean_Green_blocker", "residual_error": "positive MFE frequently coexists with high MAE or late drawdown"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L84-HM01", "trigger_id": "R13L84-HM01-HIGH-MAE-GREEN-BLOCKER", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "raw_component_scores_before": {"MFE_quality_score": 60, "MAE_control_score": 25, "bridge_confirmation_score": 35, "riskwatch_score": 30, "green_readiness_score": 60, "drawdown_risk_score": 75}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable or Green candidate", "raw_component_scores_after": {"MFE_quality_score": 60, "MAE_control_score": 25, "bridge_confirmation_score": 35, "riskwatch_score": 85, "green_readiness_score": 35, "drawdown_risk_score": 75}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable + high-MAE RiskWatch; Green blocked", "changed_components": ["MAE_control_score", "riskwatch_score", "source_quality_score", "bridge_confirmation_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "A case can be directionally right while still too unstable for clean Stage3-Green.", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "positive_allowed_only_with_RiskWatch_Green_blocked", "current_profile_verdict": "do_not_green_high_MAE_positive_without_extra_bridge", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L84-HM02-LOCAL-4B-MFE-OUTRUNS-BRIDGE", "case_id": "R13L84-HM02", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop84 high-MAE checkpoint", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "LOOP84_HIGH_MAE_POSITIVE_GREEN_BLOCKER_SOURCE_REPAIR_LOCAL_4B_HARD_4C_CHECKPOINT", "loop_objective": "cross_archetype_high_MAE_guardrail|stage2_positive_review|local_4B_review|hard_4C_protection|source_repair_review", "trigger_type": "R13_CROSS_LOCAL_4B_TIMING_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "When price outruns named orders, call-off/utilization, reorder, reimbursement or tender floor, local 4B is the seatbelt before full 4B.", "evidence_source": "derived_from_loop84_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R2", "R3", "R5", "R7", "R11"], "source_canonical_group": "C09|C13|C18|C25|C32", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_watch_yes_full_4B_no_without_non_price_evidence", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "local_4B_watch_allowed_full_4B_still_non_price_required", "current_profile_verdict": "local_watch_yes_full_4B_no_without_non_price_evidence", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "local_4B_before_full_4B_when_MFE_outruns_bridge", "residual_error": "MFE can peak before evidence bridge catches up"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L84-HM02", "trigger_id": "R13L84-HM02-LOCAL-4B-MFE-OUTRUNS-BRIDGE", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "raw_component_scores_before": {"MFE_overextension_score": 75, "bridge_lag_score": 70, "local_peak_proximity_score": 45, "full_4B_evidence_score": 25, "timing_error_risk_score": 80}, "weighted_score_before": 69, "stage_label_before": "Stage2/Stage3 with late full 4B", "raw_component_scores_after": {"MFE_overextension_score": 75, "bridge_lag_score": 70, "local_peak_proximity_score": 85, "full_4B_evidence_score": 25, "timing_error_risk_score": 40}, "weighted_score_after": 78, "stage_label_after": "Stage2/Stage3 + Local 4B Watch", "changed_components": ["MAE_control_score", "riskwatch_score", "source_quality_score", "bridge_confirmation_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "When price outruns named orders, call-off/utilization, reorder, reimbursement or tender floor, local 4B is the seatbelt before full 4B.", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "local_4B_watch_allowed_full_4B_still_non_price_required", "current_profile_verdict": "local_watch_yes_full_4B_no_without_non_price_evidence", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L84-HM03-THEME-FALSEPOS-HIGH-MAE", "case_id": "R13L84-HM03", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop84 high-MAE checkpoint", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "LOOP84_HIGH_MAE_POSITIVE_GREEN_BLOCKER_SOURCE_REPAIR_LOCAL_4B_HARD_4C_CHECKPOINT", "loop_objective": "cross_archetype_high_MAE_guardrail|stage2_positive_review|local_4B_review|hard_4C_protection|source_repair_review", "trigger_type": "R13_CROSS_STAGE2_FALSE_POSITIVE_HIGH_MAE_REVIEW", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "A headline can ignite a candle, but only an economics bridge keeps the room warm.", "evidence_source": "derived_from_loop84_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R4", "R8", "R10", "R12"], "source_canonical_group": "C05|C15|C28|C30|C31", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "theme_only_MFE_not_stage2_actionable", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "demote_theme_only_stage2", "current_profile_verdict": "theme_only_MFE_not_stage2_actionable", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "theme_headline_false_positive_high_MAE_review", "residual_error": "theme-only triggers repeatedly produce short MFE and high MAE"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L84-HM03", "trigger_id": "R13L84-HM03-THEME-FALSEPOS-HIGH-MAE", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "raw_component_scores_before": {"headline_strength_score": 65, "bridge_confirmation_score": 15, "price_momentum_score": 45, "evidence_quality_score": 20, "false_positive_risk_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"headline_strength_score": 25, "bridge_confirmation_score": 5, "price_momentum_score": 30, "evidence_quality_score": 10, "false_positive_risk_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["MAE_control_score", "riskwatch_score", "source_quality_score", "bridge_confirmation_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "A headline can ignite a candle, but only an economics bridge keeps the room warm.", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "demote_theme_only_stage2", "current_profile_verdict": "theme_only_MFE_not_stage2_actionable", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L84-HM04-SOURCE-PROXY-BLOCKER", "case_id": "R13L84-HM04", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop84 high-MAE checkpoint", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "LOOP84_HIGH_MAE_POSITIVE_GREEN_BLOCKER_SOURCE_REPAIR_LOCAL_4B_HARD_4C_CHECKPOINT", "loop_objective": "cross_archetype_high_MAE_guardrail|stage2_positive_review|local_4B_review|hard_4C_protection|source_repair_review", "trigger_type": "R13_CROSS_SOURCE_REPAIR_BLOCKER", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "Price alignment cannot substitute for primary evidence URL, publication timing, and bridge confirmation.", "evidence_source": "derived_from_loop84_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_group": "all_loop84_canonicals", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "block_runtime_promotion_until_source_repair", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "hold_shadow_only_do_not_promote", "current_profile_verdict": "block_runtime_promotion_until_source_repair", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "source_proxy_evidence_url_pending_runtime_blocker", "residual_error": "source_proxy_only/evidence_url_pending appears across the full loop"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L84-HM04", "trigger_id": "R13L84-HM04-SOURCE-PROXY-BLOCKER", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "raw_component_scores_before": {"price_alignment_score": 60, "source_quality_score": 20, "bridge_confirmation_score": 25, "runtime_promotion_score": 45, "false_positive_risk_score": 65}, "weighted_score_before": 63, "stage_label_before": "Stage2-Actionable candidate", "raw_component_scores_after": {"price_alignment_score": 60, "source_quality_score": 5, "bridge_confirmation_score": 15, "runtime_promotion_score": 0, "false_positive_risk_score": 80}, "weighted_score_after": 48, "stage_label_after": "Hold: source-repair queue", "changed_components": ["MAE_control_score", "riskwatch_score", "source_quality_score", "bridge_confirmation_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "Price alignment cannot substitute for primary evidence URL, publication timing, and bridge confirmation.", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "hold_shadow_only_do_not_promote", "current_profile_verdict": "block_runtime_promotion_until_source_repair", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L84-HM05-HARD-4C-NONPRICE", "case_id": "R13L84-HM05", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop84 high-MAE checkpoint", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "LOOP84_HIGH_MAE_POSITIVE_GREEN_BLOCKER_SOURCE_REPAIR_LOCAL_4B_HARD_4C_CHECKPOINT", "loop_objective": "cross_archetype_high_MAE_guardrail|stage2_positive_review|local_4B_review|hard_4C_protection|source_repair_review", "trigger_type": "R13_CROSS_4C_PROTECTION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "Call-off collapse, debt/project-loss break, policy reversal, deal break or cost-spread break is required before hard 4C.", "evidence_source": "derived_from_loop84_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R3", "R10", "R11", "R12"], "source_canonical_group": "C13|C30|C31|C32", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4C_blocked_without_non_price_break", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "hard_4C_requires_non_price_break_keep_price_drawdown_as_watch", "current_profile_verdict": "hard_4C_blocked_without_non_price_break", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "hard_4C_non_price_thesis_break_protection", "residual_error": "large drawdown tempts hard 4C, but price-only hard 4C is prohibited"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L84-HM05", "trigger_id": "R13L84-HM05-HARD-4C-NONPRICE", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "raw_component_scores_before": {"price_drawdown_score": 85, "non_price_break_score": 20, "hard_4c_score": 70, "watch_score": 40, "misroute_risk_score": 75}, "weighted_score_before": 64, "stage_label_before": "possible hard 4C", "raw_component_scores_after": {"price_drawdown_score": 85, "non_price_break_score": 20, "hard_4c_score": 25, "watch_score": 90, "misroute_risk_score": 35}, "weighted_score_after": 72, "stage_label_after": "4C-watch only until non-price thesis break", "changed_components": ["MAE_control_score", "riskwatch_score", "source_quality_score", "bridge_confirmation_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "Call-off collapse, debt/project-loss break, policy reversal, deal break or cost-spread break is required before hard 4C.", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "hard_4C_requires_non_price_break_keep_price_drawdown_as_watch", "current_profile_verdict": "hard_4C_blocked_without_non_price_break", "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L84-HM06-BRIDGE-FAMILY-COMPRESSION", "case_id": "R13L84-HM06", "symbol": "R13_CROSS_ARCHETYPE", "company_name": "Cross-archetype loop84 high-MAE checkpoint", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "LOOP84_HIGH_MAE_POSITIVE_GREEN_BLOCKER_SOURCE_REPAIR_LOCAL_4B_HARD_4C_CHECKPOINT", "loop_objective": "cross_archetype_high_MAE_guardrail|stage2_positive_review|local_4B_review|hard_4C_protection|source_repair_review", "trigger_type": "R13_CROSS_CANONICAL_COMPRESSION", "trigger_date": "2026-06-02", "entry_date": null, "entry_price": null, "evidence_available_at_that_date": "A global penalty would be blunt; the bridge must speak the sector’s grammar.", "evidence_source": "derived_from_loop84_source_MDs; source_proxy_only_rows_not_promoted", "source_rounds": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_group": "all_loop84_canonicals", "price_data_source": "Songdaiki/stock-web via source MDs", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "do_not_apply_new_global_weight", "four_b_evidence_type": ["cross_checkpoint", "non_price_bridge_required"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "compress_into_canonical_bridge_family_not_global_weight", "current_profile_verdict": "do_not_apply_new_global_weight", "calibration_usable": true, "do_not_count_as_new_case": true, "dedupe_for_aggregate": true, "aggregate_group_role": "r13_cross_checkpoint", "is_new_independent_case": false, "reuse_reason": "R13 cross checkpoint; source cases already counted in R1~R12", "independent_evidence_weight": 0.0, "cross_scope": "canonical_specific_bridge_family_compression", "residual_error": "every sector has a different bridge, but the shared failure is headline-to-economics gap"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L84-HM06", "trigger_id": "R13L84-HM06-BRIDGE-FAMILY-COMPRESSION", "symbol": "R13_CROSS_ARCHETYPE", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "raw_component_scores_before": {"global_rule_simplicity_score": 70, "canonical_specificity_score": 35, "overfit_risk_score": 70, "bridge_family_score": 60, "source_repair_need_score": 75}, "weighted_score_before": 58, "stage_label_before": "possible new global rule", "raw_component_scores_after": {"global_rule_simplicity_score": 35, "canonical_specificity_score": 80, "overfit_risk_score": 35, "bridge_family_score": 85, "source_repair_need_score": 75}, "weighted_score_after": 74, "stage_label_after": "canonical-specific shadow family only", "changed_components": ["MAE_control_score", "riskwatch_score", "source_quality_score", "bridge_confirmation_score", "hard_4c_score", "canonical_specificity_score"], "component_delta_explanation": "A global penalty would be blunt; the bridge must speak the sector’s grammar.", "MFE_90D_pct": null, "MAE_90D_pct": null, "score_return_alignment_label": "compress_into_canonical_bridge_family_not_global_weight", "current_profile_verdict": "do_not_apply_new_global_weight", "do_not_count_as_new_case": true}
{"row_type": "shadow_weight", "axis": "R13_loop84_cross_archetype_high_MAE_source_repair_local_4B_guardrail", "scope": "cross_archetype_checkpoint_only", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Loop84 R1~R12 cases repeatedly show high-MAE positives should not become clean Green, source-proxy rows must not promote, local 4B can precede full 4B, and hard 4C requires non-price thesis break.", "backtest_effect": "no production weight; cross-checkpoint reinforces existing axes and compresses canonical bridge family", "trigger_ids": "R13L84-HM01-HIGH-MAE-GREEN-BLOCKER|R13L84-HM02-LOCAL-4B-MFE-OUTRUNS-BRIDGE|R13L84-HM03-THEME-FALSEPOS-HIGH-MAE|R13L84-HM04-SOURCE-PROXY-BLOCKER|R13L84-HM05-HARD-4C-NONPRICE|R13L84-HM06-BRIDGE-FAMILY-COMPRESSION", "calibration_usable_count": 6, "new_independent_case_count": 0, "counterexample_count": 0, "confidence": "medium", "proposal_type": "r13_cross_checkpoint_shadow_only", "notes": "do_not_count_as_new_case=true; source repair required; not production"}
{"row_type": "residual_contribution", "round": "R13", "loop": 84, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "new_independent_case_count": 0, "reused_case_count": 12, "new_symbol_count": 0, "new_trigger_family_count": 0, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["high_MAE_positive_clean_Green_blocker", "source_proxy_runtime_promotion_risk", "local_4B_late_when_MFE_outruns_bridge", "theme_headline_false_positive_high_MAE", "price_only_hard_4C_misroute_risk", "global_weight_overfit_risk"], "loop_contribution_label": "cross_archetype_high_MAE_guardrail_checkpoint", "do_not_propose_new_weight_delta": true, "do_not_count_as_new_case": true}
```

## 20. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

This R13 file is not live candidate research and is not a new sector-positive source. It is a cross-archetype high-MAE checkpoint over loop84 R1~R12 source MDs.

### Rules

- Treat every R13 `trigger` row as `do_not_count_as_new_case=true`.
- Do not add R13 rows to new independent case counts.
- Do not infer new runtime weights from R13 alone.
- Use R13 rows to validate guardrails:
  - high-MAE positives cannot become clean Green
  - source_proxy_only/evidence_url_pending blocks runtime promotion
  - local 4B watch can exist before full 4B
  - full 4B requires non-price evidence
  - hard 4C requires non-price thesis break
  - bridge rules should remain canonical-specific, not global blunt weights
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.

## 21. Next Round State

```text
completed_round = R13
completed_loop = 84
next_round = R1
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

## 22. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
