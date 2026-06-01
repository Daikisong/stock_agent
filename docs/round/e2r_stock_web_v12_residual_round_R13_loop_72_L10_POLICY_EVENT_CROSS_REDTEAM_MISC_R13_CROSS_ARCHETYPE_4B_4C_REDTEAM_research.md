# E2R Stock-Web v12 R13 Cross-Archetype Red Team — Loop 72

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 72,
  "computed_next_round": "R1",
  "computed_next_loop": 73,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
  "fine_archetype_id": "LOOP72_HIGH_MFE_HIGH_MAE_LOCAL4B_AND_HARD4C_SOURCE_REPAIR_CHECKPOINT",
  "loop_objective": [
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "residual_false_positive_mining",
    "yellow_threshold_stress_test",
    "green_strictness_stress_test",
    "holdout_validation",
    "source_repair_queue_prioritization"
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

This is the R13 cross-archetype checkpoint for loop 72.  
It is not a new sector-specific positive research file. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R12 / loop 72.

Therefore:

```text
scheduled_round = R13
scheduled_loop = 72
selected_large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_scope = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
computed_next_round = R1
computed_next_loop = 73
```

R13 is a cross-archetype checkpoint, not an individual sector research round.  
The output file therefore uses `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` and `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM`.

## No-Repeat / novelty posture

R13 does not add new sector-positive evidence.

```text
same sector case generation = false
same canonical positive mining = false
cross-case red-team aggregation = true
do_not_count_as_new_sector_case = true
```

Rows are reused as guardrail evidence only.  
No row in this R13 file should be counted as a new independent sector case.

## R13 thesis

Loop 72 repeats the same hidden shape across very different rooms.

```text
high MFE can be real
but high MFE is not the same as durable rerating
```

The repeated failure path is:

```text
theme / policy / governance / launch / value-up / resource / demand headline
→ price heat
→ bridge evidence absent, stale, capped, or source-proxy only
→ MAE or post-peak drawdown opens
→ local 4B-watch should fire before full 4B/4C
```

The mirror-image risk is overblocking:

```text
controlled-MAE positives with actual backlog, margin, retention, reimbursement, or operating bridge
should not be downgraded just because the sector has other false positives.
```

## Cross-case checkpoint table

| source | symbol | archetype | trigger | MFE180 | MAE180 | DD after peak | R13 flags |
|---|---:|---|---|---:|---:|---:|---|
| R1 | 267260 | C02_POWER_GRID_DATACENTER_CAPEX | Stage2-Actionable | 82.31 | -8.3 | -12.46 | positive_anchor_not_to_overblock,source_repair_required |
| R1 | 010120 | C02_POWER_GRID_DATACENTER_CAPEX | Stage4B-Local-PriceOnly-GridEquipmentBlowoff | 39.22 | -42.11 | -42.5 | high_mae_180_guardrail,high_mfe_then_large_drawdown,local_4b_watch_candidate,post_peak_drawdown_guard,stage2_false_positive_bridge_gap |
| R1 | 298040 | C02_POWER_GRID_DATACENTER_CAPEX | Stage2-Actionable | 69.55 | -17.3 | -14.29 | positive_anchor_not_to_overblock,source_repair_required |
| R2 | 240810 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Stage2-Actionable | 56.27 | -3.66 | -38.35 | high_mfe_then_large_drawdown,positive_anchor_with_later_4b,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_requires_later_4b |
| R2 | 036930 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Stage2-FalsePositive / Stage4B-Local-PriceOnly | 19.45 | -36.46 | -46.8 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R2 | 084370 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | Stage2-Actionable | 73.91 | -5.94 | -45.92 | high_mfe_then_large_drawdown,positive_anchor_with_later_4b,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_requires_later_4b |
| R3 | 373220 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Stage2-RiskWatch / NotFull4B | 16.84 | -17.63 | -22.86 | local_4b_watch_candidate,riskwatch_boundary_case |
| R3 | 006400 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Stage4B-Local-CustomerDemandRisk | 8.64 | -47.27 | -51.46 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,riskwatch_boundary_case |
| R3 | 003670 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Stage4B-Local-CathodeCustomerCallOffRisk | 2.24 | -51.9 | -52.95 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,riskwatch_boundary_case,source_repair_required |
| R4 | 005490 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | Stage2-FalsePositive / StrategicResourcePolicyWatch | 16.59 | -21.46 | -32.64 | stage2_false_positive_bridge_gap |
| R4 | 003670 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | Stage4B-Local-StrategicResourceSupplyRisk | 27.97 | -23.95 | -40.58 | local_4b_watch_candidate,post_peak_drawdown_guard,riskwatch_boundary_case |
| R4 | 010130 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | Stage2-Actionable / LaterLocal4B | 419.87 | -3.89 | -58.87 | local_4b_watch_candidate,positive_anchor_with_later_4b,post_peak_drawdown_guard |
| R5 | 081660 | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage2-Actionable-InventoryCleanup | 22.48 | -0.82 | -19.02 | positive_anchor_not_to_overblock,source_repair_required |
| R5 | 111770 | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage2-FalsePositive / InventoryDestockingWatch | 9.22 | -33.47 | -39.09 | high_mae_180_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R5 | 020000 | C19_BRAND_RETAIL_INVENTORY_MARGIN | Stage4B-Local-DomesticFashionInventoryMargin | 3.22 | -25.79 | -28.11 | high_mae_180_guardrail,local_4b_watch_candidate,riskwatch_boundary_case,source_repair_required |
| R6 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2-Actionable-InsuranceValueupCSM | 44.21 | -3.94 | -21.35 | positive_anchor_not_to_overblock,source_repair_required |
| R6 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2-Actionable-ReinsuranceRateCycle | 18.73 | -1.45 | -8.78 | positive_anchor_not_to_overblock,source_repair_required |
| R6 | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2-FalsePositive / LifeInsurerPriceOnlyValueupBeta | 14.64 | -21.96 | -31.92 | source_repair_required,stage2_false_positive_bridge_gap |
| R7 | 099190 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | Stage2-FalsePositive / CGMReimbursementLaunchBeta | 4.71 | -40.49 | -43.17 | high_mae_180_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R7 | 043150 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | Stage4B-Local-DentalImagingExportWeakness | 0.0 | -30.15 | -30.15 | high_mae_180_guardrail,local_4b_watch_candidate,riskwatch_boundary_case,source_repair_required |
| R7 | 226400 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | Stage2-Actionable-OrthopedicExportBridge | 93.89 | -9.39 | -25.56 | positive_anchor_not_to_overblock,source_repair_required |
| R8 | 079940 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Stage2-FalsePositive / CloudAIBetaLocal4B | 38.82 | -29.87 | -49.49 | high_mae_180_guardrail,high_mfe_then_large_drawdown,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R8 | 136540 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Stage2-Actionable-SecurityMaintenanceRetention | 20.56 | -3.79 | -19.73 | positive_anchor_not_to_overblock,source_repair_required |
| R8 | 294570 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Stage2-FalsePositive / DataAPIContractRetentionWeak | 4.09 | -53.73 | -55.55 | high_mae_180_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R9 | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Stage2-Actionable-AutoPartsMarginBridge | 29.81 | -3.61 | -25.74 | positive_anchor_not_to_overblock,source_repair_required |
| R9 | 089860 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Stage2-Actionable-FleetUtilizationMarginBridge | 20.71 | -0.93 | -7.88 | positive_anchor_not_to_overblock,source_repair_required |
| R9 | 089590 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Stage4B-Local-AirlinePassengerBeta | 15.27 | -29.6 | -38.93 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R10 | 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage4C-HardBalanceSheetBreak | 29.93 | -80.05 | -84.64 | hard_4c_confirmation_required,high_mae_180_guardrail,high_mfe_then_large_drawdown,post_peak_drawdown_guard,source_repair_required |
| R10 | 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage4B-Local-PFRisk | 2.8 | -21.96 | -24.09 | local_4b_watch_candidate,riskwatch_boundary_case,source_repair_required |
| R10 | 013580 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-RiskWatch / NoFull4B | 7.75 | -11.48 | -12.64 | local_4b_watch_candidate,riskwatch_boundary_case,source_repair_required |
| R11 | 024060 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage4B-Local-PolicyProxyBlowoff | 25.0 | -32.65 | -46.12 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,stage2_false_positive_bridge_gap |
| R11 | 128820 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-FalsePositive / PolicyProxyFade | 12.35 | -30.24 | -37.91 | high_mae_180_guardrail,post_peak_drawdown_guard,stage2_false_positive_bridge_gap |
| R11 | 053050 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage4B-Local-GasPolicyProxy | 22.18 | -35.56 | -47.26 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,stage2_false_positive_bridge_gap |
| R12 | 008930 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage4B-Local-ControlContestExecutionRisk | 21.25 | -34.2 | -45.73 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R12 | 036560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-Actionable-TenderBattleWithLater4B | 201.31 | -15.76 | -72.04 | high_mfe_then_large_drawdown,local_4b_watch_candidate,positive_anchor_with_later_4b,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_requires_later_4b |
| R12 | 001750 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-Actionable-SaleProcessTenderCap | 66.9 | -2.84 | -41.78 | high_mfe_then_large_drawdown,positive_anchor_with_later_4b,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_requires_later_4b |

---

## R13 clusters

### stage2_false_positive_bridge_gap

```json
[
  "R1L72-C02-010120-LS-ELECTRIC-US-DATACENTER-GROWTH-PRICE-ONLY-4B",
  "R2L72-C10-036930-JUSUNG-MEMORY-EQUIPMENT-PRICE-ONLY-BETA",
  "R4L72-C16-005490-POSCOHOLDINGS-CHINA-GRAPHITE-CONTROL-LITHIUM-BETA",
  "R5L72-C19-111770-YOUNGONE-APPAREL-DESTOCKING-FALSE-STAGE2",
  "R6L72-C22-085620-MIRAE-LIFE-PRICEONLY-VALUEUP-BETA",
  "R7L72-C25-099190-ISENS-CGM-REIMBURSEMENT-LAUNCH-BETA-FAIL",
  "R8L72-C28-079940-GABIA-CLOUD-AI-BETA-CONTRACT-BRIDGE-FAIL",
  "R8L72-C28-294570-COOCON-DATAAPI-PRICEONLY-RETENTION-BRIDGE-FAIL",
  "R9L72-C29-089590-JEJU-AIR-PASSENGER-RECOVERY-BETA-LOCAL4B",
  "TRG_R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF",
  "TRG_R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE",
  "TRG_R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B",
  "TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF"
]
```
### local_4b_watch_guard

```json
[
  "R1L72-C02-010120-LS-ELECTRIC-US-DATACENTER-GROWTH-PRICE-ONLY-4B",
  "R2L72-C10-240810-WONIKIPS-MEMORY-RECOVERY-EQUIPMENT-BRIDGE",
  "R2L72-C10-036930-JUSUNG-MEMORY-EQUIPMENT-PRICE-ONLY-BETA",
  "R2L72-C10-084370-EUGENETECH-MEMORY-RECOVERY-LP-CVD-ORDER-BRIDGE",
  "R3L72-C12-373220-LGES-Q1-SLOW-EV-DEMAND-CAPEX-CUT-NOT-4C",
  "R3L72-C12-006400-SAMSUNGSDI-RIVIAN-EUROPE-SLOW-EV-DEMAND",
  "R3L72-C12-003670-POSCOFUTUREM-CATHODE-CUSTOMER-CAPEX-CUT-RISK",
  "R4L72-C16-003670-POSCOFUTUREM-GRAPHITE-ANODE-SUPPLY-RISK",
  "R4L72-C16-010130-KOREAZINC-ZINC-SMELTER-CHARGE-SUPPLY-SQUEEZE",
  "R5L72-C19-111770-YOUNGONE-APPAREL-DESTOCKING-FALSE-STAGE2",
  "R5L72-C19-020000-HANSSEM-DOMESTIC-FASHION-DEMAND-INVENTORY-DECAY",
  "R7L72-C25-099190-ISENS-CGM-REIMBURSEMENT-LAUNCH-BETA-FAIL",
  "R7L72-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-SLOWDOWN",
  "R8L72-C28-079940-GABIA-CLOUD-AI-BETA-CONTRACT-BRIDGE-FAIL",
  "R8L72-C28-294570-COOCON-DATAAPI-PRICEONLY-RETENTION-BRIDGE-FAIL",
  "R9L72-C29-089590-JEJU-AIR-PASSENGER-RECOVERY-BETA-LOCAL4B",
  "R10L72-C30-001470-SAMBU-HARD-BALANCE-SHEET-BREAK",
  "R10L72-C30-005960-DONGBU-CONSTRUCTION-PF-RISK-LOCAL4B",
  "R10L72-C30-013580-KYERYONG-ORDERBOOK-BUFFER-OVERBEARISH",
  "TRG_R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF",
  "TRG_R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE",
  "TRG_R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B",
  "TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF",
  "TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP",
  "TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP"
]
```
### hard_4c_confirmation

```json
[
  "R10L72-C30-001470-SAMBU-HARD-BALANCE-SHEET-BREAK"
]
```
### positive_anchor_not_to_overblock

```json
[
  "R1L72-C02-267260-HDHE-US-TRANSFORMER-BACKLOG-MARGIN-BRIDGE",
  "R1L72-C02-298040-HYOSUNG-US-TRANSFORMER-HICO-BRIDGE",
  "R5L72-C19-081660-FILA-US-INVENTORY-CLEANUP-MARGIN-RECOVERY",
  "R6L72-C22-000370-HANWHA-GI-SMALL-PNC-VALUEUP-CSM-CAPITAL-RETURN",
  "R6L72-C22-003690-KOREANRE-REINSURANCE-RATE-CYCLE-RESERVE-BRIDGE",
  "R7L72-C25-226400-OSTEONIC-ORTHOPEDIC-EXPORT-IMPLANT-BRIDGE",
  "R8L72-C28-136540-WINS-SECURITY-MAINTENANCE-RETENTION-SLOW-POSITIVE",
  "R9L72-C29-012330-MOBIS-AS-MODULE-MARGIN-LEVERAGE",
  "R9L72-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-SLOW-POSITIVE"
]
```
### positive_anchor_with_later_4b

```json
[
  "R2L72-C10-240810-WONIKIPS-MEMORY-RECOVERY-EQUIPMENT-BRIDGE",
  "R2L72-C10-084370-EUGENETECH-MEMORY-RECOVERY-LP-CVD-ORDER-BRIDGE",
  "R4L72-C16-010130-KOREAZINC-ZINC-SMELTER-CHARGE-SUPPLY-SQUEEZE",
  "TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP",
  "TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP"
]
```
### riskwatch_boundary_case

```json
[
  "R3L72-C12-373220-LGES-Q1-SLOW-EV-DEMAND-CAPEX-CUT-NOT-4C",
  "R3L72-C12-006400-SAMSUNGSDI-RIVIAN-EUROPE-SLOW-EV-DEMAND",
  "R3L72-C12-003670-POSCOFUTUREM-CATHODE-CUSTOMER-CAPEX-CUT-RISK",
  "R4L72-C16-003670-POSCOFUTUREM-GRAPHITE-ANODE-SUPPLY-RISK",
  "R5L72-C19-020000-HANSSEM-DOMESTIC-FASHION-DEMAND-INVENTORY-DECAY",
  "R7L72-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-SLOWDOWN",
  "R10L72-C30-005960-DONGBU-CONSTRUCTION-PF-RISK-LOCAL4B",
  "R10L72-C30-013580-KYERYONG-ORDERBOOK-BUFFER-OVERBEARISH"
]
```
### source_repair_required

```json
[
  "R1L72-C02-267260-HDHE-US-TRANSFORMER-BACKLOG-MARGIN-BRIDGE",
  "R1L72-C02-298040-HYOSUNG-US-TRANSFORMER-HICO-BRIDGE",
  "R2L72-C10-240810-WONIKIPS-MEMORY-RECOVERY-EQUIPMENT-BRIDGE",
  "R2L72-C10-036930-JUSUNG-MEMORY-EQUIPMENT-PRICE-ONLY-BETA",
  "R2L72-C10-084370-EUGENETECH-MEMORY-RECOVERY-LP-CVD-ORDER-BRIDGE",
  "R3L72-C12-003670-POSCOFUTUREM-CATHODE-CUSTOMER-CAPEX-CUT-RISK",
  "R5L72-C19-081660-FILA-US-INVENTORY-CLEANUP-MARGIN-RECOVERY",
  "R5L72-C19-111770-YOUNGONE-APPAREL-DESTOCKING-FALSE-STAGE2",
  "R5L72-C19-020000-HANSSEM-DOMESTIC-FASHION-DEMAND-INVENTORY-DECAY",
  "R6L72-C22-000370-HANWHA-GI-SMALL-PNC-VALUEUP-CSM-CAPITAL-RETURN",
  "R6L72-C22-003690-KOREANRE-REINSURANCE-RATE-CYCLE-RESERVE-BRIDGE",
  "R6L72-C22-085620-MIRAE-LIFE-PRICEONLY-VALUEUP-BETA",
  "R7L72-C25-099190-ISENS-CGM-REIMBURSEMENT-LAUNCH-BETA-FAIL",
  "R7L72-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-SLOWDOWN",
  "R7L72-C25-226400-OSTEONIC-ORTHOPEDIC-EXPORT-IMPLANT-BRIDGE",
  "R8L72-C28-079940-GABIA-CLOUD-AI-BETA-CONTRACT-BRIDGE-FAIL",
  "R8L72-C28-136540-WINS-SECURITY-MAINTENANCE-RETENTION-SLOW-POSITIVE",
  "R8L72-C28-294570-COOCON-DATAAPI-PRICEONLY-RETENTION-BRIDGE-FAIL",
  "R9L72-C29-012330-MOBIS-AS-MODULE-MARGIN-LEVERAGE",
  "R9L72-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-SLOW-POSITIVE",
  "R9L72-C29-089590-JEJU-AIR-PASSENGER-RECOVERY-BETA-LOCAL4B",
  "R10L72-C30-001470-SAMBU-HARD-BALANCE-SHEET-BREAK",
  "R10L72-C30-005960-DONGBU-CONSTRUCTION-PF-RISK-LOCAL4B",
  "R10L72-C30-013580-KYERYONG-ORDERBOOK-BUFFER-OVERBEARISH",
  "TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF",
  "TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP",
  "TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP"
]
```

---

## R13 guardrail candidate

```json
{
  "row_type": "r13_guardrail_candidate",
  "round": "R13",
  "loop": 72,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
  "axis": "local_4b_watch_vs_full_4b_4c_and_positive_anchor_overblock",
  "decision": "candidate_guardrail_observe_more",
  "do_not_propose_new_weight_delta": true,
  "proposed_runtime_effect": "Keep full 4B and hard 4C evidence-based, but strengthen local 4B-watch when a high-MFE or price-only theme lacks a refreshed bridge and MAE/post-peak drawdown opens. Do not overblock verified positive anchors with controlled MAE or explicit execution bridge.",
  "local_4b_watch_condition_sketch": [
    "MFE_30D >= 20~25% or meaningful theme spike appears",
    "MAE_90D <= -20% or MAE_180D <= -25%",
    "or post_peak_drawdown <= -35%",
    "and bridge evidence is absent, stale, or source_proxy_only"
  ],
  "hard_4c_condition_sketch": [
    "explicit non-price thesis break",
    "default / court rehabilitation / trial failure / contract cancellation / insolvency / control break",
    "price collapse alone is insufficient"
  ],
  "positive_anchor_protection": [
    "do not penalize controlled-MAE positives",
    "do not turn later drawdown into hard 4C without non-price deterioration",
    "treat tender/event winners as lifecycle positives with later local 4B, not generic Green"
  ]
}
```

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### R13 cross-case rows

```jsonl
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R1", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R1_loop_72_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_case_id": "R1L72-C02-267260-HDHE-US-TRANSFORMER-BACKLOG-MARGIN-BRIDGE", "source_trigger_id": null, "symbol": "267260", "company_name": "HD현대일렉트릭", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF", "trigger_type": "Stage2-Actionable", "entry_date": "2024-04-23", "entry_price": 229000.0, "mfe_30_pct": 37.12, "mae_30_pct": -8.3, "mfe_90_pct": 63.54, "mae_90_pct": -8.3, "mfe_180_pct": 82.31, "mae_180_pct": -8.3, "peak_date": "2025-01-09", "peak_price": 417500.0, "drawdown_after_peak_pct": -12.46, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R1", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R1_loop_72_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_case_id": "R1L72-C02-010120-LS-ELECTRIC-US-DATACENTER-GROWTH-PRICE-ONLY-4B", "source_trigger_id": null, "symbol": "010120", "company_name": "LS ELECTRIC", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF", "trigger_type": "Stage4B-Local-PriceOnly-GridEquipmentBlowoff", "entry_date": "2024-07-01", "entry_price": 218000.0, "mfe_30_pct": 25.92, "mae_30_pct": -33.49, "mfe_90_pct": 25.92, "mae_90_pct": -42.11, "mfe_180_pct": 39.22, "mae_180_pct": -42.11, "peak_date": "2025-02-19", "peak_price": 303500.0, "drawdown_after_peak_pct": -42.5, "case_role_in_source": "counterexample", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_large_drawdown", "local_4b_watch_candidate", "post_peak_drawdown_guard", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R1", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R1_loop_72_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_case_id": "R1L72-C02-298040-HYOSUNG-US-TRANSFORMER-HICO-BRIDGE", "source_trigger_id": null, "symbol": "298040", "company_name": "효성중공업", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "US_GRID_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_VS_PRICE_ONLY_EQUIPMENT_BLOWOFF", "trigger_type": "Stage2-Actionable", "entry_date": "2024-04-29", "entry_price": 289000.0, "mfe_30_pct": 62.28, "mae_30_pct": -1.73, "mfe_90_pct": 62.28, "mae_90_pct": -17.3, "mfe_180_pct": 69.55, "mae_180_pct": -17.3, "peak_date": "2025-01-20", "peak_price": 490000.0, "drawdown_after_peak_pct": -14.29, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R2", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R2_loop_72_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_case_id": "R2L72-C10-240810-WONIKIPS-MEMORY-RECOVERY-EQUIPMENT-BRIDGE", "source_trigger_id": null, "symbol": "240810", "company_name": "원익IPS", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-29", "entry_price": 28700.0, "mfe_30_pct": 56.27, "mae_30_pct": -0.35, "mfe_90_pct": 56.27, "mae_90_pct": -0.7, "mfe_180_pct": 56.27, "mae_180_pct": -3.66, "peak_date": "2024-04-08", "peak_price": 44850.0, "drawdown_after_peak_pct": -38.35, "case_role_in_source": "positive_with_later_4b_watch", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mfe_then_large_drawdown", "positive_anchor_with_later_4b", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_requires_later_4b"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R2", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R2_loop_72_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_case_id": "R2L72-C10-036930-JUSUNG-MEMORY-EQUIPMENT-PRICE-ONLY-BETA", "source_trigger_id": null, "symbol": "036930", "company_name": "주성엔지니어링", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA", "trigger_type": "Stage2-FalsePositive / Stage4B-Local-PriceOnly", "entry_date": "2024-02-28", "entry_price": 34700.0, "mfe_30_pct": 19.45, "mae_30_pct": -4.18, "mfe_90_pct": 19.45, "mae_90_pct": -8.79, "mfe_180_pct": 19.45, "mae_180_pct": -36.46, "peak_date": "2024-04-08", "peak_price": 41450.0, "drawdown_after_peak_pct": -46.8, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R2", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R2_loop_72_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "source_case_id": "R2L72-C10-084370-EUGENETECH-MEMORY-RECOVERY-LP-CVD-ORDER-BRIDGE", "source_trigger_id": null, "symbol": "084370", "company_name": "유진테크", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-20", "entry_price": 34500.0, "mfe_30_pct": 29.57, "mae_30_pct": -0.43, "mfe_90_pct": 73.91, "mae_90_pct": -0.43, "mfe_180_pct": 73.91, "mae_180_pct": -5.94, "peak_date": "2024-05-28", "peak_price": 60000.0, "drawdown_after_peak_pct": -45.92, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mfe_then_large_drawdown", "positive_anchor_with_later_4b", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_requires_later_4b"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R3", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R3_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_case_id": "R3L72-C12-373220-LGES-Q1-SLOW-EV-DEMAND-CAPEX-CUT-NOT-4C", "source_trigger_id": null, "symbol": "373220", "company_name": "LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT", "trigger_type": "Stage2-RiskWatch / NotFull4B", "entry_date": "2024-04-25", "entry_price": 380000.0, "mfe_30_pct": 4.47, "mae_30_pct": -14.21, "mfe_90_pct": 10.26, "mae_90_pct": -17.63, "mfe_180_pct": 16.84, "mae_180_pct": -17.63, "peak_date": "2024-10-08", "peak_price": 444000.0, "drawdown_after_peak_pct": -22.86, "case_role_in_source": "overbearish_counterexample", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": null, "r13_flags": ["local_4b_watch_candidate", "riskwatch_boundary_case"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R3", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R3_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_case_id": "R3L72-C12-006400-SAMSUNGSDI-RIVIAN-EUROPE-SLOW-EV-DEMAND", "source_trigger_id": null, "symbol": "006400", "company_name": "삼성SDI", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT", "trigger_type": "Stage4B-Local-CustomerDemandRisk", "entry_date": "2024-06-28", "entry_price": 359000.0, "mfe_30_pct": 8.64, "mae_30_pct": -17.97, "mfe_90_pct": 8.64, "mae_90_pct": -17.97, "mfe_180_pct": 8.64, "mae_180_pct": -47.27, "peak_date": "2024-07-05", "peak_price": 390000.0, "drawdown_after_peak_pct": -51.46, "case_role_in_source": "risk_positive", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "riskwatch_boundary_case"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R3", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R3_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md", "source_case_id": "R3L72-C12-003670-POSCOFUTUREM-CATHODE-CUSTOMER-CAPEX-CUT-RISK", "source_trigger_id": null, "symbol": "003670", "company_name": "포스코퓨처엠", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "OEM_EV_DEMAND_SLOWDOWN_CAPEX_CUT_CUSTOMER_CONTRACT_RISK_VS_AMPC_BASE_SUPPORT", "trigger_type": "Stage4B-Local-CathodeCustomerCallOffRisk", "entry_date": "2024-04-25", "entry_price": 290000.0, "mfe_30_pct": 2.24, "mae_30_pct": -13.79, "mfe_90_pct": 2.24, "mae_90_pct": -32.59, "mfe_180_pct": 2.24, "mae_180_pct": -51.9, "peak_date": "2024-04-25", "peak_price": 296500.0, "drawdown_after_peak_pct": -52.95, "case_role_in_source": "risk_positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "riskwatch_boundary_case", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R4", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R4_loop_72_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_case_id": "R4L72-C16-005490-POSCOHOLDINGS-CHINA-GRAPHITE-CONTROL-LITHIUM-BETA", "source_trigger_id": null, "symbol": "005490", "company_name": "POSCO홀딩스", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA", "trigger_type": "Stage2-FalsePositive / StrategicResourcePolicyWatch", "entry_date": "2023-10-23", "entry_price": 452000.0, "mfe_30_pct": 16.59, "mae_30_pct": -11.61, "mfe_90_pct": 16.59, "mae_90_pct": -11.61, "mfe_180_pct": 16.59, "mae_180_pct": -21.46, "peak_date": "2023-11-06", "peak_price": 527000.0, "drawdown_after_peak_pct": -32.64, "case_role_in_source": "counterexample", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": null, "r13_flags": ["stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R4", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R4_loop_72_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_case_id": "R4L72-C16-003670-POSCOFUTUREM-GRAPHITE-ANODE-SUPPLY-RISK", "source_trigger_id": null, "symbol": "003670", "company_name": "포스코퓨처엠", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA", "trigger_type": "Stage4B-Local-StrategicResourceSupplyRisk", "entry_date": "2023-10-23", "entry_price": 298500.0, "mfe_30_pct": 20.94, "mae_30_pct": -22.45, "mfe_90_pct": 27.97, "mae_90_pct": -22.45, "mfe_180_pct": 27.97, "mae_180_pct": -23.95, "peak_date": "2023-12-21", "peak_price": 382000.0, "drawdown_after_peak_pct": -40.58, "case_role_in_source": "risk_positive", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": null, "r13_flags": ["local_4b_watch_candidate", "post_peak_drawdown_guard", "riskwatch_boundary_case"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R4", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R4_loop_72_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md", "source_case_id": "R4L72-C16-010130-KOREAZINC-ZINC-SMELTER-CHARGE-SUPPLY-SQUEEZE", "source_trigger_id": null, "symbol": "010130", "company_name": "고려아연", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "GRAPHITE_CRITICAL_MINERAL_EXPORT_CONTROL_AND_SMELTER_SUPPLY_SQUEEZE_VS_PRICE_ONLY_RESOURCE_BETA", "trigger_type": "Stage2-Actionable / LaterLocal4B", "entry_date": "2024-04-11", "entry_price": 463000.0, "mfe_30_pct": 17.93, "mae_30_pct": -2.7, "mfe_90_pct": 20.3, "mae_90_pct": -3.89, "mfe_180_pct": 419.87, "mae_180_pct": -3.89, "peak_date": "2024-12-06", "peak_price": 2407000.0, "drawdown_after_peak_pct": -58.87, "case_role_in_source": "positive_with_later_4b_watch", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": null, "r13_flags": ["local_4b_watch_candidate", "positive_anchor_with_later_4b", "post_peak_drawdown_guard"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R5", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R5_loop_72_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L72-C19-081660-FILA-US-INVENTORY-CLEANUP-MARGIN-RECOVERY", "source_trigger_id": null, "symbol": "081660", "company_name": "휠라홀딩스", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY", "trigger_type": "Stage2-Actionable-InventoryCleanup", "entry_date": "2024-04-11", "entry_price": 36700.0, "mfe_30_pct": 12.53, "mae_30_pct": -0.41, "mfe_90_pct": 21.39, "mae_90_pct": -0.41, "mfe_180_pct": 22.48, "mae_180_pct": -0.82, "peak_date": "2024-09-25", "peak_price": 44950.0, "drawdown_after_peak_pct": -19.02, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R5", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R5_loop_72_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L72-C19-111770-YOUNGONE-APPAREL-DESTOCKING-FALSE-STAGE2", "source_trigger_id": null, "symbol": "111770", "company_name": "영원무역", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY", "trigger_type": "Stage2-FalsePositive / InventoryDestockingWatch", "entry_date": "2024-02-01", "entry_price": 48250.0, "mfe_30_pct": 9.22, "mae_30_pct": -8.81, "mfe_90_pct": 9.22, "mae_90_pct": -33.47, "mfe_180_pct": 9.22, "mae_180_pct": -33.47, "peak_date": "2024-02-01", "peak_price": 52700.0, "drawdown_after_peak_pct": -39.09, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R5", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R5_loop_72_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L72-C19-020000-HANSSEM-DOMESTIC-FASHION-DEMAND-INVENTORY-DECAY", "source_trigger_id": null, "symbol": "020000", "company_name": "한섬", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_INVENTORY_CLEANUP_MARGIN_RECOVERY_VS_DISCOUNT_DEMAND_DECAY", "trigger_type": "Stage4B-Local-DomesticFashionInventoryMargin", "entry_date": "2024-04-11", "entry_price": 19230.0, "mfe_30_pct": 3.22, "mae_30_pct": -4.47, "mfe_90_pct": 3.22, "mae_90_pct": -11.75, "mfe_180_pct": 3.22, "mae_180_pct": -25.79, "peak_date": "2024-05-02", "peak_price": 19850.0, "drawdown_after_peak_pct": -28.11, "case_role_in_source": "risk_positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "riskwatch_boundary_case", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R6", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R6_loop_72_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L72-C22-000370-HANWHA-GI-SMALL-PNC-VALUEUP-CSM-CAPITAL-RETURN", "source_trigger_id": null, "symbol": "000370", "company_name": "한화손해보험", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA", "trigger_type": "Stage2-Actionable-InsuranceValueupCSM", "entry_date": "2024-02-01", "entry_price": 4320.0, "mfe_30_pct": 42.82, "mae_30_pct": -3.94, "mfe_90_pct": 42.82, "mae_90_pct": -3.94, "mfe_180_pct": 44.21, "mae_180_pct": -3.94, "peak_date": "2024-08-20", "peak_price": 6230.0, "drawdown_after_peak_pct": -21.35, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R6", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R6_loop_72_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L72-C22-003690-KOREANRE-REINSURANCE-RATE-CYCLE-RESERVE-BRIDGE", "source_trigger_id": null, "symbol": "003690", "company_name": "코리안리", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA", "trigger_type": "Stage2-Actionable-ReinsuranceRateCycle", "entry_date": "2024-02-01", "entry_price": 7580.0, "mfe_30_pct": 11.74, "mae_30_pct": -1.45, "mfe_90_pct": 12.8, "mae_90_pct": -1.45, "mfe_180_pct": 18.73, "mae_180_pct": -1.45, "peak_date": "2024-08-26", "peak_price": 9000.0, "drawdown_after_peak_pct": -8.78, "case_role_in_source": "positive_slow", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R6", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R6_loop_72_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L72-C22-085620-MIRAE-LIFE-PRICEONLY-VALUEUP-BETA", "source_trigger_id": null, "symbol": "085620", "company_name": "미래에셋생명", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_VALUEUP_CSM_CAPITAL_RETURN_VS_PRICE_ONLY_LIFE_INSURER_BETA", "trigger_type": "Stage2-FalsePositive / LifeInsurerPriceOnlyValueupBeta", "entry_date": "2024-02-01", "entry_price": 5670.0, "mfe_30_pct": 14.64, "mae_30_pct": -20.55, "mfe_90_pct": 14.64, "mae_90_pct": -21.96, "mfe_180_pct": 14.64, "mae_180_pct": -21.96, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -31.92, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R7", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R7_loop_72_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L72-C25-099190-ISENS-CGM-REIMBURSEMENT-LAUNCH-BETA-FAIL", "source_trigger_id": null, "symbol": "099190", "company_name": "아이센스", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA", "trigger_type": "Stage2-FalsePositive / CGMReimbursementLaunchBeta", "entry_date": "2024-02-01", "entry_price": 24400.0, "mfe_30_pct": 4.71, "mae_30_pct": -15.78, "mfe_90_pct": 4.71, "mae_90_pct": -22.62, "mfe_180_pct": 4.71, "mae_180_pct": -40.49, "peak_date": "2024-02-02", "peak_price": 25550.0, "drawdown_after_peak_pct": -43.17, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R7", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R7_loop_72_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L72-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-SLOWDOWN", "source_trigger_id": null, "symbol": "043150", "company_name": "바텍", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA", "trigger_type": "Stage4B-Local-DentalImagingExportWeakness", "entry_date": "2024-02-01", "entry_price": 32500.0, "mfe_30_pct": 0.0, "mae_30_pct": -8.31, "mfe_90_pct": 0.0, "mae_90_pct": -18.77, "mfe_180_pct": 0.0, "mae_180_pct": -30.15, "peak_date": "2024-02-01", "peak_price": 32500.0, "drawdown_after_peak_pct": -30.15, "case_role_in_source": "risk_positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "riskwatch_boundary_case", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R7", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R7_loop_72_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_case_id": "R7L72-C25-226400-OSTEONIC-ORTHOPEDIC-EXPORT-IMPLANT-BRIDGE", "source_trigger_id": null, "symbol": "226400", "company_name": "오스테오닉", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA", "trigger_type": "Stage2-Actionable-OrthopedicExportBridge", "entry_date": "2024-07-01", "entry_price": 4580.0, "mfe_30_pct": 23.14, "mae_30_pct": -9.39, "mfe_90_pct": 39.52, "mae_90_pct": -9.39, "mfe_180_pct": 93.89, "mae_180_pct": -9.39, "peak_date": "2025-02-10", "peak_price": 8880.0, "drawdown_after_peak_pct": -25.56, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R8", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R8_loop_72_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_case_id": "R8L72-C28-079940-GABIA-CLOUD-AI-BETA-CONTRACT-BRIDGE-FAIL", "source_trigger_id": null, "symbol": "079940", "company_name": "가비아", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA", "trigger_type": "Stage2-FalsePositive / CloudAIBetaLocal4B", "entry_date": "2024-02-22", "entry_price": 17540.0, "mfe_30_pct": 38.82, "mae_30_pct": -8.55, "mfe_90_pct": 38.82, "mae_90_pct": -17.96, "mfe_180_pct": 38.82, "mae_180_pct": -29.87, "peak_date": "2024-03-14", "peak_price": 24350.0, "drawdown_after_peak_pct": -49.49, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_large_drawdown", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R8", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R8_loop_72_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_case_id": "R8L72-C28-136540-WINS-SECURITY-MAINTENANCE-RETENTION-SLOW-POSITIVE", "source_trigger_id": null, "symbol": "136540", "company_name": "윈스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA", "trigger_type": "Stage2-Actionable-SecurityMaintenanceRetention", "entry_date": "2024-04-11", "entry_price": 12400.0, "mfe_30_pct": 7.02, "mae_30_pct": -3.79, "mfe_90_pct": 20.56, "mae_90_pct": -3.79, "mfe_180_pct": 20.56, "mae_180_pct": -3.79, "peak_date": "2024-06-28", "peak_price": 14950.0, "drawdown_after_peak_pct": -19.73, "case_role_in_source": "positive_slow", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R8", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R8_loop_72_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_case_id": "R8L72-C28-294570-COOCON-DATAAPI-PRICEONLY-RETENTION-BRIDGE-FAIL", "source_trigger_id": null, "symbol": "294570", "company_name": "쿠콘", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_SECURITY_CONTRACT_RETENTION_ARR_BRIDGE_VS_PRICE_ONLY_CLOUD_AI_BETA", "trigger_type": "Stage2-FalsePositive / DataAPIContractRetentionWeak", "entry_date": "2024-02-01", "entry_price": 22000.0, "mfe_30_pct": 4.09, "mae_30_pct": -15.0, "mfe_90_pct": 4.09, "mae_90_pct": -30.82, "mfe_180_pct": 4.09, "mae_180_pct": -53.73, "peak_date": "2024-02-02", "peak_price": 22900.0, "drawdown_after_peak_pct": -55.55, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R9", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R9_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L72-C29-012330-MOBIS-AS-MODULE-MARGIN-LEVERAGE", "source_trigger_id": null, "symbol": "012330", "company_name": "현대모비스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "trigger_type": "Stage2-Actionable-AutoPartsMarginBridge", "entry_date": "2024-02-01", "entry_price": 208000.0, "mfe_30_pct": 29.33, "mae_30_pct": 0.0, "mfe_90_pct": 29.81, "mae_90_pct": 0.0, "mfe_180_pct": 29.81, "mae_180_pct": -3.61, "peak_date": "2024-03-18", "peak_price": 270000.0, "drawdown_after_peak_pct": -25.74, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R9", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R9_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L72-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-SLOW-POSITIVE", "source_trigger_id": null, "symbol": "089860", "company_name": "롯데렌탈", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "trigger_type": "Stage2-Actionable-FleetUtilizationMarginBridge", "entry_date": "2024-02-23", "entry_price": 26800.0, "mfe_30_pct": 5.6, "mae_30_pct": -0.75, "mfe_90_pct": 17.54, "mae_90_pct": -0.75, "mfe_180_pct": 20.71, "mae_180_pct": -0.93, "peak_date": "2024-08-28", "peak_price": 32350.0, "drawdown_after_peak_pct": -7.88, "case_role_in_source": "positive_slow", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R9", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R9_loop_72_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L72-C29-089590-JEJU-AIR-PASSENGER-RECOVERY-BETA-LOCAL4B", "source_trigger_id": null, "symbol": "089590", "company_name": "제주항공", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "trigger_type": "Stage4B-Local-AirlinePassengerBeta", "entry_date": "2024-01-05", "entry_price": 11790.0, "mfe_30_pct": 15.27, "mae_30_pct": -4.07, "mfe_90_pct": 15.27, "mae_90_pct": -10.26, "mfe_180_pct": 15.27, "mae_180_pct": -29.6, "peak_date": "2024-01-18", "peak_price": 13590.0, "drawdown_after_peak_pct": -38.93, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R10", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R10_loop_72_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L72-C30-001470-SAMBU-HARD-BALANCE-SHEET-BREAK", "source_trigger_id": null, "symbol": "001470", "company_name": "삼부토건", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER", "trigger_type": "Stage4C-HardBalanceSheetBreak", "entry_date": "2024-01-05", "entry_price": 2205.0, "mfe_30_pct": 26.08, "mae_30_pct": -15.56, "mfe_90_pct": 29.93, "mae_90_pct": -31.52, "mfe_180_pct": 29.93, "mae_180_pct": -80.05, "peak_date": "2024-03-15", "peak_price": 2865.0, "drawdown_after_peak_pct": -84.64, "case_role_in_source": "hard_4c", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["hard_4c_confirmation_required", "high_mae_180_guardrail", "high_mfe_then_large_drawdown", "post_peak_drawdown_guard", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R10", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R10_loop_72_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L72-C30-005960-DONGBU-CONSTRUCTION-PF-RISK-LOCAL4B", "source_trigger_id": null, "symbol": "005960", "company_name": "동부건설", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER", "trigger_type": "Stage4B-Local-PFRisk", "entry_date": "2024-02-01", "entry_price": 5350.0, "mfe_30_pct": 2.8, "mae_30_pct": -6.64, "mfe_90_pct": 2.8, "mae_90_pct": -10.84, "mfe_180_pct": 2.8, "mae_180_pct": -21.96, "peak_date": "2024-02-19", "peak_price": 5500.0, "drawdown_after_peak_pct": -24.09, "case_role_in_source": "risk_positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["local_4b_watch_candidate", "riskwatch_boundary_case", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R10", "source_loop": 72, "source_file": "e2r_stock_web_v12_residual_round_R10_loop_72_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L72-C30-013580-KYERYONG-ORDERBOOK-BUFFER-OVERBEARISH", "source_trigger_id": null, "symbol": "013580", "company_name": "계룡건설", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_LIQUIDITY_BREAK_VS_RECAPITALIZATION_AND_ORDERBOOK_BUFFER", "trigger_type": "Stage2-RiskWatch / NoFull4B", "entry_date": "2024-02-01", "entry_price": 14460.0, "mfe_30_pct": 6.71, "mae_30_pct": -5.6, "mfe_90_pct": 6.71, "mae_90_pct": -11.48, "mfe_180_pct": 7.75, "mae_180_pct": -11.48, "peak_date": "2024-08-21", "peak_price": 15580.0, "drawdown_after_peak_pct": -12.64, "case_role_in_source": "overbearish_counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": null, "r13_flags": ["local_4b_watch_candidate", "riskwatch_boundary_case", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R11", "source_loop": "72", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF", "source_trigger_id": "TRG_R11L72-C31-024060-HEUNGGU-EAST-SEA-OIL-GAS-PROXY-BLOWOFF", "symbol": "024060", "company_name": "흥구석유", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "trigger_type": "Stage4B-Local-PolicyProxyBlowoff", "entry_date": "2024-06-04", "entry_price": 17520.0, "mfe_30_pct": 19.58, "mae_30_pct": -21.8, "mfe_90_pct": 25.0, "mae_90_pct": -29.45, "mfe_180_pct": 25.0, "mae_180_pct": -32.65, "peak_date": "2024-08-13", "peak_price": 21900.0, "drawdown_after_peak_pct": -46.12, "case_role_in_source": "counterexample", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": "local_4b_watch_should_precede_full_4b", "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R11", "source_loop": "72", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE", "source_trigger_id": "TRG_R11L72-C31-128820-DAESUNG-INDUSTRIAL-EAST-SEA-ENERGY-PROXY-FADE", "symbol": "128820", "company_name": "대성산업", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "trigger_type": "Stage2-FalsePositive / PolicyProxyFade", "entry_date": "2024-06-04", "entry_price": 4250.0, "mfe_30_pct": 12.35, "mae_30_pct": -12.47, "mfe_90_pct": 12.35, "mae_90_pct": -26.82, "mfe_180_pct": 12.35, "mae_180_pct": -30.24, "peak_date": "2024-06-04", "peak_price": 4775.0, "drawdown_after_peak_pct": -37.91, "case_role_in_source": "counterexample", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": "local_4b_watch_should_precede_full_4b", "r13_flags": ["high_mae_180_guardrail", "post_peak_drawdown_guard", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R11", "source_loop": "72", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B", "source_trigger_id": "TRG_R11L72-C31-053050-GSE-GAS-PROXY-PRICEONLY-LOCAL4B", "symbol": "053050", "company_name": "지에스이", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_OIL_GAS_EXPLORATION_POLICY_PROXY_BLOWOFF_VS_EXECUTION_BRIDGE_ABSENCE", "trigger_type": "Stage4B-Local-GasPolicyProxy", "entry_date": "2024-06-04", "entry_price": 4485.0, "mfe_30_pct": 22.18, "mae_30_pct": -22.97, "mfe_90_pct": 22.18, "mae_90_pct": -28.65, "mfe_180_pct": 22.18, "mae_180_pct": -35.56, "peak_date": "2024-06-04", "peak_price": 5480.0, "drawdown_after_peak_pct": -47.26, "case_role_in_source": "counterexample", "source_proxy_only": false, "evidence_url_pending": false, "current_profile_verdict": "local_4b_watch_should_precede_full_4b", "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R12", "source_loop": "72", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF", "source_trigger_id": "TRG_R12L72-C32-008930-HANMI-SCIENCE-OCI-CONTROL-CONTEST-BLOWOFF", "symbol": "008930", "company_name": "한미사이언스", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "trigger_type": "Stage4B-Local-ControlContestExecutionRisk", "entry_date": "2024-01-15", "entry_price": 46350.0, "mfe_30_pct": 21.25, "mae_30_pct": -16.5, "mfe_90_pct": 21.25, "mae_90_pct": -24.7, "mfe_180_pct": 21.25, "mae_180_pct": -34.2, "peak_date": "2024-01-16", "peak_price": 56200.0, "drawdown_after_peak_pct": -45.73, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C32 should not treat a control-contest / group-integration headline as durable Stage2 unless closing path, tender price, board/shareholder approval and execution certainty are visible. The price path had fast MFE but later MAE opened materially.", "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R12", "source_loop": "72", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "source_trigger_id": "TRG_R12L72-C32-036560-YOUNGPOONG-PRECISION-TENDER-BATTLE-CAP", "symbol": "036560", "company_name": "영풍정밀/KZ정밀", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "trigger_type": "Stage2-Actionable-TenderBattleWithLater4B", "entry_date": "2024-09-13", "entry_price": 12180.0, "mfe_30_pct": 201.31, "mae_30_pct": 0.0, "mfe_90_pct": 201.31, "mae_90_pct": 0.0, "mfe_180_pct": 201.31, "mae_180_pct": -15.76, "peak_date": "2024-10-07", "peak_price": 36700.0, "drawdown_after_peak_pct": -72.04, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C32 can allow Stage2 when a tender/control battle has explicit tender price and strategic control context, but extreme post-peak drawdown after the tender window requires local 4B-watch. Runtime must separate tender-cap math from open-ended governance rerating.", "r13_flags": ["high_mfe_then_large_drawdown", "local_4b_watch_candidate", "positive_anchor_with_later_4b", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_requires_later_4b"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 72, "source_round": "R12", "source_loop": "72", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP", "source_trigger_id": "TRG_R12L72-C32-001750-HANYANG-SECURITIES-SALE-PROCESS-CAP", "symbol": "001750", "company_name": "한양증권", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_CONTEST_TENDER_CAP_SALE_PROCESS_VS_EXECUTION_AND_CLOSING_BRIDGE", "trigger_type": "Stage2-Actionable-SaleProcessTenderCap", "entry_date": "2024-07-11", "entry_price": 11630.0, "mfe_30_pct": 66.9, "mae_30_pct": -0.17, "mfe_90_pct": 66.9, "mae_90_pct": -0.17, "mfe_180_pct": 66.9, "mae_180_pct": -2.84, "peak_date": "2024-08-05", "peak_price": 19410.0, "drawdown_after_peak_pct": -41.78, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C32 should support a sale-process Stage2 only when control-stake sale, buyer certainty and closing path are verified. The stock-web path had strong MFE but later reverted toward pre-event levels, so tender/sale-process cap logic is required.", "r13_flags": ["high_mfe_then_large_drawdown", "positive_anchor_with_later_4b", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_requires_later_4b"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
```

### R13 summary row

```jsonl
{"row_type": "r13_cross_summary", "round": "R13", "loop": 72, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP72_HIGH_MFE_HIGH_MAE_LOCAL4B_AND_HARD4C_SOURCE_REPAIR_CHECKPOINT", "selected_cross_case_count": 36, "source_rounds_covered": ["R1", "R10", "R11", "R12", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"], "source_canonical_count": 12, "stage2_false_positive_bridge_gap_count": 13, "local_4b_watch_guard_count": 25, "hard_4c_confirmation_count": 1, "positive_anchor_not_to_overblock_count": 9, "positive_anchor_with_later_4b_count": 5, "riskwatch_boundary_case_count": 8, "source_repair_required_count": 27, "new_sector_positive_case_count": 0, "do_not_count_as_new_sector_case": true, "do_not_propose_new_weight_delta": true, "r13_decision": "guardrail_checkpoint_only"}
```

### R13 guardrail row

```jsonl
{"row_type": "r13_guardrail_candidate", "round": "R13", "loop": 72, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "axis": "local_4b_watch_vs_full_4b_4c_and_positive_anchor_overblock", "decision": "candidate_guardrail_observe_more", "do_not_propose_new_weight_delta": true, "proposed_runtime_effect": "Keep full 4B and hard 4C evidence-based, but strengthen local 4B-watch when a high-MFE or price-only theme lacks a refreshed bridge and MAE/post-peak drawdown opens. Do not overblock verified positive anchors with controlled MAE or explicit execution bridge.", "local_4b_watch_condition_sketch": ["MFE_30D >= 20~25% or meaningful theme spike appears", "MAE_90D <= -20% or MAE_180D <= -25%", "or post_peak_drawdown <= -35%", "and bridge evidence is absent, stale, or source_proxy_only"], "hard_4c_condition_sketch": ["explicit non-price thesis break", "default / court rehabilitation / trial failure / contract cancellation / insolvency / control break", "price collapse alone is insufficient"], "positive_anchor_protection": ["do not penalize controlled-MAE positives", "do not turn later drawdown into hard 4C without non-price deterioration", "treat tender/event winners as lifecycle positives with later local 4B, not generic Green"]}
```

---

## Score / return alignment summary

The cross-archetype alignment is:

```text
1. High MFE alone is not a rerating.
2. High MFE + bridge absent/stale + MAE or post-peak drawdown = local 4B-watch.
3. Full 4B still requires non-price deterioration evidence.
4. Hard 4C requires explicit non-price thesis-break evidence.
5. Positive anchors with controlled MAE must not be overblocked.
6. Source-proxy rows can shape guardrails but should not promote production weights before source repair.
```

## Loop 72 residual decision

```text
r13_decision = guardrail_checkpoint_only
new_sector_positive_case_count = 0
do_not_propose_new_weight_delta = true
```

The useful candidate is a scoped diagnostic, not an immediate weight change:

```text
local_4b_watch_vs_full_4b_4c_and_positive_anchor_overblock
```

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this R13 standalone v12 cross-archetype red-team MD.
Do not patch production scoring blindly.

Scope:
canonical_scope = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
axis = local_4b_watch_vs_full_4b_4c_and_positive_anchor_overblock

Required checks:
1. Ingest only price_source_validation, r13_cross_case, r13_cross_summary and r13_guardrail_candidate rows.
2. Do not count these rows as new sector-positive coverage.
3. Validate each source trigger row against its original loop-72 MD and stock-web tradable_raw OHLC shard.
4. Keep full 4B non-price evidence requirement.
5. Keep hard 4C evidence-based.
6. Consider a local_4b_watch diagnostic when:
   - MFE_30D >= 20~25% or a strong theme spike appears,
   - and MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35%,
   - and bridge evidence is absent, stale, source_proxy_only, or capped by tender/execution window.
7. Do not convert local_4b_watch into hard 4C.
8. Protect positive anchors with controlled MAE or explicit backlog/order/customer/retention/reimbursement/operating/governance execution bridge.
9. Reject implementation if verified structural positives are overblocked.
10. Emit before/after diagnostics:
   - false positive reduction
   - missed structural positives
   - local 4B timing lead
   - hard 4C precision
   - source-repair dependency.
```

---

## Final round state

```text
completed_round = R13
completed_loop = 72
next_round = R1
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

