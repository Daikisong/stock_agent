# E2R Stock-Web v12 R13 Cross-Archetype Red Team — Loop 73

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 73,
  "computed_next_round": "R1",
  "computed_next_loop": 74,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
  "fine_archetype_id": "LOOP73_STAGE2_FALSE_POSITIVE_HIGH_MAE_LOCAL4B_SOURCE_REPAIR_CHECKPOINT",
  "loop_objective": [
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "residual_false_positive_mining",
    "high_MAE_guardrail",
    "delayed_positive_protection",
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

This is the R13 cross-archetype checkpoint for loop 73.  
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

Previous completed state in this interactive run: R12 / loop 73.

Therefore:

```text
scheduled_round = R13
scheduled_loop = 73
selected_large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_scope = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
computed_next_round = R1
computed_next_loop = 74
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

Loop 73 shows the same failure mode wearing different sector costumes.

```text
headline heat
→ initial MFE or attention
→ bridge evidence absent, stale, capped, source_proxy_only, or evidence_url_pending
→ early MAE shock or post-peak drawdown
→ local 4B-watch should fire
```

But there is a mirror-image risk:

```text
delayed winners and controlled-MAE positives should not be overblocked
if the non-price bridge later becomes real.
```

The guardrail is therefore a two-sided hinge:

```text
price-only heat cannot become Green
price-only drawdown cannot become hard 4C
verified delayed bridge must survive source repair
```

## Cross-case checkpoint table

| src | symbol | archetype | trigger | MFE180 | MAE180 | DD after peak | R13 flags |
|---|---:|---|---|---:|---:|---:|---|
| R1 | 329180 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | Stage2-Actionable-ShipbuildingBacklogMarginBridge | 185.77 | -2.15 | -26.65 | positive_anchor_not_to_overblock,source_repair_required |
| R1 | 010620 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | Stage2-Actionable-MidshipMarginRecovery | 79.25 | -0.75 | -31.05 | positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,source_repair_required |
| R1 | 097230 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | Stage2-FalsePositive / OrderBetaWeakMargin | 15.22 | -33.64 | -42.4 | high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R2 | 092870 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Stage2-Actionable-TesterAdoptionBridgeAfterCA | 47.01 | -8.68 | -37.88 | high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required |
| R2 | 064760 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Stage2-FalsePositive / ConsumableCustomerQualityLocal4B | 21.38 | -44.62 | -54.37 | high_mae_180_guardrail,high_mae_90_guardrail,high_mfe_then_drawdown,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R2 | 067310 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Stage2-FalsePositive / OSATPackagingBetaWeakUtilization | 7.04 | -69.75 | -71.74 | early_mae_shock,high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R3 | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | Stage4B-Local-SeparatorDemandSlowdown | 0.63 | -51.49 | -51.79 | early_mae_shock,high_mae_180_guardrail,high_mae_90_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,riskwatch_or_overbearish_boundary,source_repair_required |
| R3 | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | Stage4B-Local-SeparatorCustomerDemand | 19.84 | -50.46 | -58.66 | high_mae_180_guardrail,high_mae_90_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,riskwatch_or_overbearish_boundary,source_repair_required |
| R3 | 051910 | C14_EV_DEMAND_SLOWDOWN_4B_4C | Stage2-RiskWatch / NoHard4C | 9.28 | -30.11 | -36.04 | high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,riskwatch_or_overbearish_boundary,source_repair_required |
| R4 | 014830 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Stage2-Actionable-CausticPotashSpreadBridge | 28.9 | -35.99 | -50.34 | high_mae_180_guardrail,high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required |
| R4 | 010950 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Stage2-FalsePositive / RefiningSpreadBetaLocal4B | 1.2 | -36.05 | -36.8 | high_mae_180_guardrail,high_mae_90_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R4 | 120110 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Stage2-FalsePositive / IndustrialMaterialSpreadFade | 20.96 | -29.59 | -41.79 | high_mae_180_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,riskwatch_or_overbearish_boundary,source_repair_required,stage2_false_positive_bridge_gap |
| R5 | 214420 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage2-Actionable-KBeautyExportChannelReorder | 123.25 | -0.91 | -44.27 | high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |
| R5 | 192820 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage2-Actionable-ODMGlobalCustomerReorder | 51.6 | -15.45 | -44.23 | high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |
| R5 | 018250 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Stage2-FalsePositive / ExportChannelOneCandleFade | 28.74 | -41.45 | -54.52 | high_mae_180_guardrail,high_mae_90_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R6 | 316140 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable-BankValueupCapitalReturn | 21.93 | -2.23 | -18.99 | positive_anchor_not_to_overblock,source_repair_required |
| R6 | 024110 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-Actionable-HighDividendPBRBridge | 27.77 | 0.0 | -20.11 | positive_anchor_not_to_overblock,source_repair_required |
| R6 | 006800 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Stage2-FalsePositive / BrokerageValueupBetaFade | 17.5 | -15.71 | -28.26 | riskwatch_or_overbearish_boundary,source_repair_required,stage2_false_positive_bridge_gap |
| R7 | 068270 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Stage2-Actionable-BiologicCommercializationBridge | 18.21 | -7.17 | -21.47 | positive_anchor_not_to_overblock,source_repair_required |
| R7 | 950210 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Stage2-FalsePositive / ApprovalHeadlineChaseLocal4B | 15.15 | -27.6 | -37.13 | early_mae_shock,high_mae_180_guardrail,high_mae_90_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R7 | 195940 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Stage2-Actionable-DrugCommercializationRamp | 44.04 | -4.57 | -31.06 | positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,source_repair_required |
| R8 | 376300 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Stage2-Actionable-SubscriptionPlatformOperatingLeverage | 108.71 | -0.41 | -29.72 | positive_anchor_not_to_overblock,source_repair_required |
| R8 | 214270 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Stage2-FalsePositive / DigitalAdTechPriceBetaLocal4B | 33.39 | -45.23 | -58.94 | high_mae_180_guardrail,high_mae_90_guardrail,high_mfe_then_drawdown,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R8 | 214320 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Stage2-FalsePositive / AdAgencyOperatingLeverageWeak | 4.59 | -16.51 | -20.18 | riskwatch_or_overbearish_boundary,source_repair_required,stage2_false_positive_bridge_gap |
| R9 | 161390 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Stage2-Actionable-TirePriceMixMarginBridge | 32.15 | -16.08 | -36.49 | high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required |
| R9 | 086280 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Stage2-Actionable-LogisticsPCCMarginBridgePostCA | 39.04 | -2.3 | -29.74 | positive_anchor_not_to_overblock,source_repair_required |
| R9 | 018880 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Stage2-FalsePositive / ThermalEVPartsBetaLocal4B | 6.33 | -38.31 | -41.98 | high_mae_180_guardrail,high_mae_90_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R10 | 034300 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-RiskWatch / RecapitalizationBufferNoHard4C | 64.9 | -12.91 | -40.21 | post_peak_drawdown_guard,riskwatch_or_overbearish_boundary,source_repair_required,winner_lifecycle_later_4b_required |
| R10 | 004960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage4B-Local-PFOrderbookMarginRisk | 5.97 | -16.42 | -21.13 | local_4b_watch_candidate,riskwatch_or_overbearish_boundary,source_repair_required |
| R10 | 047040 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-RiskWatch / LargeBuilderNoFull4B | 26.98 | -9.34 | -28.6 | riskwatch_or_overbearish_boundary,source_repair_required |
| R11 | 052690 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-FalsePositive / NuclearEPCPolicyHeadlineChase | 3.26 | -47.58 | -49.24 | early_mae_shock,high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R11 | 051600 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-RiskWatch / NuclearServiceProxyNoFull4B | 10.57 | -17.59 | -20.99 | riskwatch_or_overbearish_boundary,source_repair_required |
| R11 | 083650 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-DelayedPositive / NuclearEquipmentBridgeWithEarlyMAE | 142.9 | -30.46 | -38.43 | bad_entry_not_stage2,delayed_positive_requires_source_repair,delayed_winner_after_bad_entry,early_mae_shock,high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |
| R12 | 241560 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage4B-Local-MergerRatioMinorityRisk | 15.53 | -35.24 | -43.95 | early_mae_shock,high_mae_180_guardrail,high_mae_90_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R12 | 454910 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-FalsePositive / RoboticsMergerValuationBeta | 15.05 | -58.37 | -63.82 | early_mae_shock,high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R12 | 000150 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-DelayedPositive / HoldcoControlPremiumAfterEarly4B | 46.49 | -53.7 | -38.73 | bad_entry_not_stage2,delayed_positive_requires_source_repair,early_mae_shock,high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,source_repair_required |

---

## R13 clusters

### stage2_false_positive_bridge_gap

```json
[
  "TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION",
  "TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B",
  "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION",
  "TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B",
  "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE",
  "TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE",
  "TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE",
  "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE",
  "TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B",
  "TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK",
  "TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B",
  "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE",
  "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK",
  "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B"
]
```
### early_mae_shock

```json
[
  "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION",
  "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B",
  "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE",
  "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE",
  "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE",
  "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK",
  "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B",
  "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM"
]
```
### high_mae_guardrail

```json
[
  "TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION",
  "TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B",
  "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION",
  "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B",
  "TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B",
  "TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C",
  "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE",
  "TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B",
  "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE",
  "TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE",
  "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE",
  "TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B",
  "TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B",
  "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE",
  "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE",
  "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK",
  "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B",
  "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM"
]
```
### post_peak_drawdown_guard

```json
[
  "TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION",
  "TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE",
  "TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B",
  "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION",
  "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B",
  "TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B",
  "TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C",
  "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE",
  "TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B",
  "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE",
  "TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER",
  "TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER",
  "TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE",
  "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE",
  "TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B",
  "TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE",
  "TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B",
  "TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER",
  "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE",
  "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE",
  "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK",
  "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B",
  "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM"
]
```
### local_4b_watch_guard

```json
[
  "TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION",
  "TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE",
  "TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B",
  "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION",
  "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B",
  "TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B",
  "TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C",
  "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE",
  "TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B",
  "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE",
  "TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER",
  "TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER",
  "TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE",
  "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE",
  "TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B",
  "TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE",
  "TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B",
  "TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER",
  "TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B",
  "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE",
  "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE",
  "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK",
  "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B",
  "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM"
]
```
### hard_4c_confirmation

```json
[]
```
### positive_anchor_not_to_overblock

```json
[
  "TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE",
  "TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE",
  "TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE",
  "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE",
  "TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER",
  "TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE",
  "TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE",
  "TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE",
  "TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP",
  "TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE",
  "TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE",
  "TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA"
]
```
### winner_lifecycle_later_4b

```json
[
  "TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE",
  "TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE",
  "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE",
  "TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER",
  "TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER",
  "TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP",
  "TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE",
  "TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER",
  "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE"
]
```
### delayed_positive_requires_source_repair

```json
[
  "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE",
  "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM"
]
```
### riskwatch_or_overbearish_boundary

```json
[
  "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B",
  "TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B",
  "TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C",
  "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE",
  "TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE",
  "TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK",
  "TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER",
  "TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B",
  "TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B",
  "TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH"
]
```
### source_repair_required

```json
[
  "TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE",
  "TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE",
  "TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION",
  "TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE",
  "TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B",
  "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION",
  "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B",
  "TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B",
  "TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C",
  "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE",
  "TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B",
  "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE",
  "TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER",
  "TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER",
  "TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE",
  "TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE",
  "TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE",
  "TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE",
  "TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE",
  "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE",
  "TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP",
  "TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE",
  "TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B",
  "TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK",
  "TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE",
  "TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA",
  "TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B",
  "TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER",
  "TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B",
  "TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B",
  "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE",
  "TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH",
  "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE",
  "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK",
  "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B",
  "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM"
]
```

---

## R13 guardrail candidate

```json
{
  "row_type": "r13_guardrail_candidate",
  "round": "R13",
  "loop": 73,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
  "axis": "stage2_false_positive_high_mae_local4b_vs_hard4c_and_delayed_positive_protection",
  "decision": "candidate_guardrail_observe_more",
  "do_not_propose_new_weight_delta": true,
  "proposed_runtime_effect": "Keep Stage2 bridge-based and hard 4C non-price-evidence-based. Strengthen local 4B-watch when price-only, policy, governance, beta, approval or demand-slowdown signals show early MAE shock, high 90/180D MAE, or post-peak drawdown without verified bridge refresh. Protect verified positives and delayed winners from overblocking, but require source repair before promotion.",
  "stage2_bridge_requirement_sketch": [
    "positive Stage2 requires non-price bridge evidence",
    "bridge examples: backlog/margin, customer adoption, utilization, reorder, capital return, reimbursement, contract scope, transaction economics",
    "price-only MFE cannot become Green"
  ],
  "local_4b_watch_condition_sketch": [
    "MAE_30D <= -25% or MAE_90D <= -20% or MAE_180D <= -25%",
    "or post_peak_drawdown <= -35%",
    "and bridge evidence is absent, stale, capped, source_proxy_only, or evidence_url_pending",
    "local 4B is not hard 4C"
  ],
  "hard_4c_condition_sketch": [
    "explicit non-price thesis break",
    "examples: default, court rehabilitation, contract cancellation, clinical/regulatory failure, insolvency, control/auditor break, project cancellation",
    "price collapse alone is insufficient"
  ],
  "delayed_positive_protection": [
    "delayed winners with bad initial entry should not be labeled Green at the event gap",
    "but they should not be permanently blocked if later non-price bridge evidence becomes real",
    "promote only after source repair and lifecycle diagnostics"
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
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R1", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "source_case_id": "R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE", "source_trigger_id": "TRG_R1L73-C01-329180-HDHHI-LNG-NAVAL-BACKLOG-MARGIN-BRIDGE", "symbol": "329180", "company_name": "HD현대중공업", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "trigger_type": "Stage2-Actionable-ShipbuildingBacklogMarginBridge", "entry_date": "2024-04-26", "entry_price": 130000.0, "mfe_30_pct": 12.31, "mae_30_pct": -2.15, "mfe_90_pct": 61.54, "mae_90_pct": -2.15, "mfe_180_pct": 185.77, "mae_180_pct": -2.15, "peak_date": "2025-02-13", "peak_price": 371500.0, "drawdown_after_peak_pct": -26.65, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C01 should allow Stage2 when shipbuilding backlog is not just order volume but connects to LNG/naval mix, rising newbuild prices and margin conversion. The stock-web path shows structural MFE with controlled early MAE, but source repair is needed before runtime weight promotion.", "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R1", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "source_case_id": "R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE", "source_trigger_id": "TRG_R1L73-C01-010620-HDMIPO-MIDSHIP_PRODUCT_MIX_MARGIN_BRIDGE", "symbol": "010620", "company_name": "HD현대미포", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "trigger_type": "Stage2-Actionable-MidshipMarginRecovery", "entry_date": "2024-06-24", "entry_price": 80500.0, "mfe_30_pct": 42.73, "mae_30_pct": -0.75, "mfe_90_pct": 52.55, "mae_90_pct": -0.75, "mfe_180_pct": 79.25, "mae_180_pct": -0.75, "peak_date": "2025-01-21", "peak_price": 144300.0, "drawdown_after_peak_pct": -31.05, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C01 should capture mid-size vessel backlog recovery when product mix and margin conversion are visible. But after the 2025 peak, a later local 4B-watch is needed if the margin bridge stops refreshing or drawdown opens.", "r13_flags": ["positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R1", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "source_case_id": "R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION", "source_trigger_id": "TRG_R1L73-C01-097230-HJSC-ORDER_BETA_WEAK_MARGIN_CONVERSION", "symbol": "097230", "company_name": "HJ중공업", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIPBUILDING_LNG_NAVAL_BACKLOG_MARGIN_BRIDGE_VS_ORDER_BETA_WITH_WEAK_MARGIN_CONVERSION", "trigger_type": "Stage2-FalsePositive / OrderBetaWeakMargin", "entry_date": "2024-06-03", "entry_price": 3285.0, "mfe_30_pct": 15.22, "mae_30_pct": -7.76, "mfe_90_pct": 15.22, "mae_90_pct": -21.31, "mfe_180_pct": 15.22, "mae_180_pct": -33.64, "peak_date": "2024-06-19", "peak_price": 3785.0, "drawdown_after_peak_pct": -42.4, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C01 should not treat shipbuilding/construction order beta as Stage2 unless backlog quality and margin conversion are explicit. HJ Heavy produced a short MFE but later opened drawdown, making it a false Stage2 / local 4B-watch candidate.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R2", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "source_case_id": "R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE", "source_trigger_id": "TRG_R2L73-C08-092870-EXICON-HBM-TESTER-POST-CA-ADOPTION-BRIDGE", "symbol": "092870", "company_name": "엑시콘", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "trigger_type": "Stage2-Actionable-TesterAdoptionBridgeAfterCA", "entry_date": "2024-09-06", "entry_price": 10720.0, "mfe_30_pct": 36.75, "mae_30_pct": -6.72, "mfe_90_pct": 36.75, "mae_90_pct": -6.72, "mfe_180_pct": 47.01, "mae_180_pct": -8.68, "peak_date": "2025-02-14", "peak_price": 15760.0, "drawdown_after_peak_pct": -37.88, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C08 can permit Stage2 when tester demand is tied to verified customer adoption/reorder and the entry window is after corporate-action contamination. Exicon's post-CA path had strong MFE with controlled MAE, but source repair is required before runtime promotion.", "r13_flags": ["high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R2", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "source_case_id": "R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B", "source_trigger_id": "TRG_R2L73-C08-064760-TCK-SIC-CONSUMABLE-CUSTOMER-QUALITY-LOCAL4B", "symbol": "064760", "company_name": "티씨케이", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "trigger_type": "Stage2-FalsePositive / ConsumableCustomerQualityLocal4B", "entry_date": "2024-06-12", "entry_price": 123500.0, "mfe_30_pct": 21.38, "mae_30_pct": -6.88, "mfe_90_pct": 21.38, "mae_90_pct": -29.47, "mfe_180_pct": 21.38, "mae_180_pct": -44.62, "peak_date": "2024-06-14", "peak_price": 149900.0, "drawdown_after_peak_pct": -54.37, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C08 should not treat high-quality semi consumables as Green when near-term customer utilization or margin bridge is absent. TCK had an initial MFE but later opened large MAE and drawdown, requiring local 4B-watch rather than durable Stage2.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "high_mfe_then_drawdown", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R2", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "source_case_id": "R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION", "source_trigger_id": "TRG_R2L73-C08-067310-HANAMICRON-OSAT-HBM-BETA-WEAK-UTILIZATION", "symbol": "067310", "company_name": "하나마이크론", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CONSUMABLE_CUSTOMER_QUALITY_VS_HBM_PACKAGING_BETA_WITH_WEAK_UTILIZATION", "trigger_type": "Stage2-FalsePositive / OSATPackagingBetaWeakUtilization", "entry_date": "2024-04-11", "entry_price": 29850.0, "mfe_30_pct": 7.04, "mae_30_pct": -29.31, "mfe_90_pct": 7.04, "mae_90_pct": -48.41, "mfe_180_pct": 7.04, "mae_180_pct": -69.75, "peak_date": "2024-04-11", "peak_price": 31950.0, "drawdown_after_peak_pct": -71.74, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C08 must not allow OSAT/HBM packaging beta to become durable Stage2 without utilization, customer quality, margin, or package mix evidence. Hana Micron generated only small MFE and then severe MAE.", "r13_flags": ["early_mae_shock", "high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R3", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "source_case_id": "R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B", "source_trigger_id": "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B", "symbol": "361610", "company_name": "SK아이이테크놀로지", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "trigger_type": "Stage4B-Local-SeparatorDemandSlowdown", "entry_date": "2024-04-25", "entry_price": 63800.0, "mfe_30_pct": 0.63, "mae_30_pct": -25.47, "mfe_90_pct": 0.63, "mae_90_pct": -51.49, "mfe_180_pct": 0.63, "mae_180_pct": -51.49, "peak_date": "2024-04-29", "peak_price": 64200.0, "drawdown_after_peak_pct": -51.79, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C14 should fire local 4B-watch when EV demand slowdown translates into separator utilization pressure and the stock path opens severe MAE. Hard 4C still requires non-price evidence such as plant impairment, contract cancellation, insolvency, or structural customer loss.", "r13_flags": ["early_mae_shock", "high_mae_180_guardrail", "high_mae_90_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R3", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "source_case_id": "R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B", "source_trigger_id": "TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B", "symbol": "393890", "company_name": "더블유씨피", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "trigger_type": "Stage4B-Local-SeparatorCustomerDemand", "entry_date": "2024-04-25", "entry_price": 31750.0, "mfe_30_pct": 19.84, "mae_30_pct": -0.0, "mfe_90_pct": 19.84, "mae_90_pct": -50.46, "mfe_180_pct": 19.84, "mae_180_pct": -50.46, "peak_date": "2024-05-03", "peak_price": 38050.0, "drawdown_after_peak_pct": -58.66, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "Separator suppliers need stricter C14 treatment than diversified cell or chemical names. WCP produced initial MFE, but the later 180D MAE and post-peak drawdown show customer demand/utilization risk converting into local 4B-watch.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R3", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "source_case_id": "R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C", "source_trigger_id": "TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C", "symbol": "051910", "company_name": "LG화학", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "trigger_type": "Stage2-RiskWatch / NoHard4C", "entry_date": "2024-04-25", "entry_price": 377000.0, "mfe_30_pct": 9.28, "mae_30_pct": -1.46, "mfe_90_pct": 9.28, "mae_90_pct": -30.11, "mfe_180_pct": 9.28, "mae_180_pct": -30.11, "peak_date": "2024-04-30", "peak_price": 412000.0, "drawdown_after_peak_pct": -36.04, "case_role_in_source": "overbearish_counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C14 should flag EV/material demand slowdown risk, but not convert diversified integrated chemical/cathode exposure into hard 4C when later rebound and business-buffer evidence can exist. The correct label is RiskWatch/local 4B boundary, not hard thesis break without non-price evidence.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R4", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_73_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_case_id": "R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE", "source_trigger_id": "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE", "symbol": "014830", "company_name": "유니드", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "trigger_type": "Stage2-Actionable-CausticPotashSpreadBridge", "entry_date": "2024-04-25", "entry_price": 91700.0, "mfe_30_pct": 28.9, "mae_30_pct": -0.65, "mfe_90_pct": 28.9, "mae_90_pct": -0.65, "mfe_180_pct": 28.9, "mae_180_pct": -35.99, "peak_date": "2024-05-22", "peak_price": 118200.0, "drawdown_after_peak_pct": -50.34, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C17 should allow Stage2 only when a commodity/spread move connects to product-specific spread, export price, cost pass-through, and margin conversion. 유니드 produced a real MFE path, but later collapse means local 4B-watch should activate if spread evidence stops refreshing.", "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R4", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_73_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_case_id": "R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B", "source_trigger_id": "TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B", "symbol": "010950", "company_name": "S-Oil", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "trigger_type": "Stage2-FalsePositive / RefiningSpreadBetaLocal4B", "entry_date": "2024-04-11", "entry_price": 83500.0, "mfe_30_pct": 1.2, "mae_30_pct": -17.6, "mfe_90_pct": 1.2, "mae_90_pct": -20.96, "mfe_180_pct": 1.2, "mae_180_pct": -36.05, "peak_date": "2024-04-11", "peak_price": 84500.0, "drawdown_after_peak_pct": -36.8, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C17 should not treat refinery spread beta as Green unless crack spread, inventory, utilization, and earnings revision bridge are visible. S-Oil produced almost no MFE and later severe 180D MAE, so local 4B-watch is more appropriate.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R4", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_73_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_case_id": "R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE", "source_trigger_id": "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE", "symbol": "120110", "company_name": "코오롱인더", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "trigger_type": "Stage2-FalsePositive / IndustrialMaterialSpreadFade", "entry_date": "2024-04-25", "entry_price": 36500.0, "mfe_30_pct": 20.96, "mae_30_pct": -0.68, "mfe_90_pct": 20.96, "mae_90_pct": -0.82, "mfe_180_pct": 20.96, "mae_180_pct": -29.59, "peak_date": "2024-05-22", "peak_price": 44150.0, "drawdown_after_peak_pct": -41.79, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C17 industrial materials should require spread-to-margin refresh. 코오롱인더 produced an initial MFE on industrial-material optimism, but later MAE and drawdown widened; this supports local 4B-watch unless aramid/tire-cord/film margin evidence refreshes.", "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "riskwatch_or_overbearish_boundary", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R5", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_73_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER", "source_trigger_id": "TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER", "symbol": "214420", "company_name": "토니모리", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "trigger_type": "Stage2-Actionable-KBeautyExportChannelReorder", "entry_date": "2024-04-30", "entry_price": 7700.0, "mfe_30_pct": 47.14, "mae_30_pct": -0.91, "mfe_90_pct": 123.25, "mae_90_pct": -0.91, "mfe_180_pct": 123.25, "mae_180_pct": -0.91, "peak_date": "2024-06-14", "peak_price": 17190.0, "drawdown_after_peak_pct": -44.27, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C18 should allow Stage2 when small-brand export/channel reorder connects to operating leverage, but should add local 4B-watch after a blowoff if reorder evidence stops refreshing.", "r13_flags": ["high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R5", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_73_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER", "source_trigger_id": "TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER", "symbol": "192820", "company_name": "코스맥스", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "trigger_type": "Stage2-Actionable-ODMGlobalCustomerReorder", "entry_date": "2024-04-29", "entry_price": 137200.0, "mfe_30_pct": 29.59, "mae_30_pct": -2.55, "mfe_90_pct": 51.6, "mae_90_pct": -15.45, "mfe_180_pct": 51.6, "mae_180_pct": -15.45, "peak_date": "2024-06-14", "peak_price": 208000.0, "drawdown_after_peak_pct": -44.23, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C18 should reward ODM/customer reorder only when global customer demand and margin conversion are visible. Cosmax shows a strong MFE path with manageable entry-basis MAE, but source repair is required before promotion.", "r13_flags": ["high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R5", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_73_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md", "source_case_id": "R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE", "source_trigger_id": "TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE", "symbol": "018250", "company_name": "애경산업", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "trigger_type": "Stage2-FalsePositive / ExportChannelOneCandleFade", "entry_date": "2024-04-25", "entry_price": 20700.0, "mfe_30_pct": 28.74, "mae_30_pct": -4.44, "mfe_90_pct": 28.74, "mae_90_pct": -22.71, "mfe_180_pct": 28.74, "mae_180_pct": -41.45, "peak_date": "2024-05-31", "peak_price": 26650.0, "drawdown_after_peak_pct": -54.52, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C18 should not treat a short export/channel rally as durable Green when reorder, sell-through or margin evidence fails to refresh. Aekyung generated MFE but later opened deep MAE and drawdown.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R6", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_73_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE", "source_trigger_id": "TRG_R6L73-C21-316140-WOORI-VALUEUP-CAPITAL-RETURN-BRIDGE", "symbol": "316140", "company_name": "우리금융지주", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "trigger_type": "Stage2-Actionable-BankValueupCapitalReturn", "entry_date": "2024-02-01", "entry_price": 13910.0, "mfe_30_pct": 11.43, "mae_30_pct": -2.23, "mfe_90_pct": 16.68, "mae_90_pct": -2.23, "mfe_180_pct": 21.93, "mae_180_pct": -2.23, "peak_date": "2024-07-29", "peak_price": 16960.0, "drawdown_after_peak_pct": -18.99, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C21 should allow Stage2 when low-PBR bank rerating is backed by shareholder-return, buyback/cancellation, dividend and ROE bridge. Woori produced controlled MAE and later MFE, but share-count change inside the window needs coding-agent validation.", "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R6", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_73_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE", "source_trigger_id": "TRG_R6L73-C21-024110-IBK-HIGH-DIVIDEND-PBR-ROE-BRIDGE", "symbol": "024110", "company_name": "기업은행", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "trigger_type": "Stage2-Actionable-HighDividendPBRBridge", "entry_date": "2024-02-01", "entry_price": 12530.0, "mfe_30_pct": 27.77, "mae_30_pct": 0.0, "mfe_90_pct": 27.77, "mae_90_pct": 0.0, "mfe_180_pct": 27.77, "mae_180_pct": 0.0, "peak_date": "2024-03-15", "peak_price": 16010.0, "drawdown_after_peak_pct": -20.11, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C21 should include slower high-dividend/value-up bank paths when dividend yield, low PBR, capital discipline and stable ROE support the rerating. IBK produced strong MFE with essentially no entry-basis MAE.", "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R6", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_73_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "source_case_id": "R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE", "source_trigger_id": "TRG_R6L73-C21-006800-MIRAESEC-BROKERAGE-VALUEUP-BETA-FADE", "symbol": "006800", "company_name": "미래에셋증권", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_AND_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_BROKERAGE_BETA", "trigger_type": "Stage2-FalsePositive / BrokerageValueupBetaFade", "entry_date": "2024-02-01", "entry_price": 7830.0, "mfe_30_pct": 17.5, "mae_30_pct": 0.0, "mfe_90_pct": 17.5, "mae_90_pct": -15.71, "mfe_180_pct": 17.5, "mae_180_pct": -15.71, "peak_date": "2024-02-23", "peak_price": 9200.0, "drawdown_after_peak_pct": -28.26, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C21 should not treat brokerage/value-up beta as durable Green unless recurring ROE, capital return, treasury-stock cancellation or distribution bridge is verified. Mirae generated MFE but later faded and needs local 4B/RiskWatch rather than durable Stage2.", "r13_flags": ["riskwatch_or_overbearish_boundary", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R7", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_73_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "source_case_id": "R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE", "source_trigger_id": "TRG_R7L73-C23-068270-CELLTRION-ZYMFENTRA-COMMERCIALIZATION-BRIDGE", "symbol": "068270", "company_name": "셀트리온", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "trigger_type": "Stage2-Actionable-BiologicCommercializationBridge", "entry_date": "2024-04-29", "entry_price": 178500.0, "mfe_30_pct": 10.36, "mae_30_pct": -1.34, "mfe_90_pct": 18.21, "mae_90_pct": -3.08, "mfe_180_pct": 18.21, "mae_180_pct": -7.17, "peak_date": "2024-07-30", "peak_price": 211000.0, "drawdown_after_peak_pct": -21.47, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C23 should reward regulatory approval only when it becomes commercialization evidence: launch, reimbursement access, channel uptake, direct sales or margin bridge. Celltrion has a slower but cleaner large-cap commercialization path with controlled MAE.", "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R7", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_73_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "source_case_id": "R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE", "source_trigger_id": "TRG_R7L73-C23-950210-PRESTIGE-BIOSIMILAR-APPROVAL-HEADLINE-CHASE", "symbol": "950210", "company_name": "프레스티지바이오파마", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "trigger_type": "Stage2-FalsePositive / ApprovalHeadlineChaseLocal4B", "entry_date": "2024-10-28", "entry_price": 18150.0, "mfe_30_pct": 15.15, "mae_30_pct": -27.6, "mfe_90_pct": 15.15, "mae_90_pct": -27.6, "mfe_180_pct": 15.15, "mae_180_pct": -27.6, "peak_date": "2024-10-28", "peak_price": 20900.0, "drawdown_after_peak_pct": -37.13, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C23 should not convert a late approval/regulatory headline chase into durable Stage2 unless reimbursement, launch timing, partner orders and sales bridge are visible. The stock showed same-day MFE but later MAE and drawdown widened.", "r13_flags": ["early_mae_shock", "high_mae_180_guardrail", "high_mae_90_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R7", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_73_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md", "source_case_id": "R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP", "source_trigger_id": "TRG_R7L73-C23-195940-HKINNO-KCAB-GLOBAL-COMMERCIALIZATION-RAMP", "symbol": "195940", "company_name": "HK이노엔", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_DRUG_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_HEADLINE_CHASE", "trigger_type": "Stage2-Actionable-DrugCommercializationRamp", "entry_date": "2024-06-17", "entry_price": 36100.0, "mfe_30_pct": 18.7, "mae_30_pct": -4.29, "mfe_90_pct": 44.04, "mae_90_pct": -4.57, "mfe_180_pct": 44.04, "mae_180_pct": -4.57, "peak_date": "2024-10-07", "peak_price": 52000.0, "drawdown_after_peak_pct": -31.06, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C23 should distinguish real prescription/export commercialization ramp from pure regulatory excitement. HK inno.N produced an attractive path, but later post-peak drawdown requires local 4B-watch if prescription/partner revenue evidence stops refreshing.", "r13_flags": ["positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R8", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_73_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_case_id": "R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE", "source_trigger_id": "TRG_R8L73-C26-376300-DEARU-SUBSCRIPTION-PLATFORM-OPERATING-LEVERAGE", "symbol": "376300", "company_name": "디어유", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "trigger_type": "Stage2-Actionable-SubscriptionPlatformOperatingLeverage", "entry_date": "2024-10-28", "entry_price": 24100.0, "mfe_30_pct": 74.07, "mae_30_pct": -0.41, "mfe_90_pct": 108.71, "mae_90_pct": -0.41, "mfe_180_pct": 108.71, "mae_180_pct": -0.41, "peak_date": "2025-02-20", "peak_price": 50300.0, "drawdown_after_peak_pct": -29.72, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C26 should allow Stage2 when a platform has subscription/user or ARPU expansion that can convert into operating leverage. DearU produced very high MFE with almost no entry-basis MAE, but later local 4B-watch is still needed if subscriber/artist expansion evidence stops refreshing after the peak.", "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R8", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_73_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_case_id": "R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B", "source_trigger_id": "TRG_R8L73-C26-214270-FSN-DIGITAL-ADTECH-PRICE-BETA-LOCAL4B", "symbol": "214270", "company_name": "FSN", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "trigger_type": "Stage2-FalsePositive / DigitalAdTechPriceBetaLocal4B", "entry_date": "2024-02-01", "entry_price": 2830.0, "mfe_30_pct": 33.39, "mae_30_pct": -4.59, "mfe_90_pct": 33.39, "mae_90_pct": -22.97, "mfe_180_pct": 33.39, "mae_180_pct": -45.23, "peak_date": "2024-02-02", "peak_price": 3775.0, "drawdown_after_peak_pct": -58.94, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C26 should not treat digital-adtech or platform theme MFE as durable Stage2 unless recurring ad revenue, take-rate, client retention and margin conversion are visible. FSN had a sharp MFE but later severe MAE and post-peak drawdown.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "high_mfe_then_drawdown", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R8", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_73_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md", "source_case_id": "R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK", "source_trigger_id": "TRG_R8L73-C26-214320-INNOCEAN-AD-AGENCY-OPERATING-LEVERAGE-WEAK", "symbol": "214320", "company_name": "이노션", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "SUBSCRIPTION_FANDOM_PLATFORM_AND_DIGITAL_AD_OPERATING_LEVERAGE_VS_PRICE_ONLY_ADTECH_BETA", "trigger_type": "Stage2-FalsePositive / AdAgencyOperatingLeverageWeak", "entry_date": "2024-02-01", "entry_price": 21800.0, "mfe_30_pct": 4.59, "mae_30_pct": -2.98, "mfe_90_pct": 4.59, "mae_90_pct": -2.98, "mfe_180_pct": 4.59, "mae_180_pct": -16.51, "peak_date": "2024-02-26", "peak_price": 22800.0, "drawdown_after_peak_pct": -20.18, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C26 should distinguish ad-agency campaign stability from true platform operating leverage. Innocean had limited MFE and later MAE; without client-budget, digital mix or margin revision evidence it should remain RiskWatch / no durable Green rather than Stage2.", "r13_flags": ["riskwatch_or_overbearish_boundary", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R9", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE", "source_trigger_id": "TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "trigger_type": "Stage2-Actionable-TirePriceMixMarginBridge", "entry_date": "2024-01-18", "entry_price": 45100.0, "mfe_30_pct": 32.15, "mae_30_pct": -2.0, "mfe_90_pct": 32.15, "mae_90_pct": -2.0, "mfe_180_pct": 32.15, "mae_180_pct": -16.08, "peak_date": "2024-02-23", "peak_price": 59600.0, "drawdown_after_peak_pct": -36.49, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C29 should include tire price/mix and replacement-demand margin leverage, not only OEM vehicle volume. 한국타이어 produced a strong MFE with controlled early MAE, but later post-peak drawdown means local 4B-watch is needed if margin/mix evidence stops refreshing.", "r13_flags": ["high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R9", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA", "source_trigger_id": "TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA", "symbol": "086280", "company_name": "현대글로비스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "trigger_type": "Stage2-Actionable-LogisticsPCCMarginBridgePostCA", "entry_date": "2024-08-23", "entry_price": 108600.0, "mfe_30_pct": 15.29, "mae_30_pct": -2.3, "mfe_90_pct": 39.04, "mae_90_pct": -2.3, "mfe_180_pct": 39.04, "mae_180_pct": -2.3, "peak_date": "2025-01-31", "peak_price": 151000.0, "drawdown_after_peak_pct": -29.74, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C29 should include logistics/PCC/CKD operating leverage when freight rate, capacity and capital-return bridge are visible. Because Hyundai Glovis had 2024 corporate-action candidates, the entry is placed after the 2024-08-02 candidate; the post-CA path is strong but needs source repair.", "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R9", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B", "source_trigger_id": "TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B", "symbol": "018880", "company_name": "한온시스템", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "trigger_type": "Stage2-FalsePositive / ThermalEVPartsBetaLocal4B", "entry_date": "2024-02-01", "entry_price": 6160.0, "mfe_30_pct": 6.33, "mae_30_pct": -9.25, "mfe_90_pct": 6.33, "mae_90_pct": -23.21, "mfe_180_pct": 6.33, "mae_180_pct": -38.31, "peak_date": "2024-02-02", "peak_price": 6550.0, "drawdown_after_peak_pct": -41.98, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C29 should not treat EV thermal-management or auto-parts theme beta as durable Stage2 when customer volume, pricing and margin conversion are weak. Hanon generated only small MFE and later severe MAE, making it a local 4B-watch / false Stage2 row.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R10", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_73_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER", "source_trigger_id": "TRG_R10L73-C30-034300-SHINSEGAE-CONSTRUCTION-PF-RECAP-BUFFER", "symbol": "034300", "company_name": "신세계건설", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "trigger_type": "Stage2-RiskWatch / RecapitalizationBufferNoHard4C", "entry_date": "2024-02-07", "entry_price": 11310.0, "mfe_30_pct": 13.0, "mae_30_pct": -7.96, "mfe_90_pct": 64.9, "mae_90_pct": -12.91, "mfe_180_pct": 64.9, "mae_180_pct": -12.91, "peak_date": "2024-05-30", "peak_price": 18650.0, "drawdown_after_peak_pct": -40.21, "case_role_in_source": "overbearish_counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C30 should not convert every PF-liquidity headline into hard 4C when parent recapitalization, tender/de-listing path, or capital buffer changes the equity path. The stock-web path had large MFE after the recapitalization candidate, so this is a no-hard-4C buffer row, not a hard break row.", "r13_flags": ["post_peak_drawdown_guard", "riskwatch_or_overbearish_boundary", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R10", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_73_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B", "source_trigger_id": "TRG_R10L73-C30-004960-HANSHIN-PF-ORDERBOOK-LOCAL4B", "symbol": "004960", "company_name": "한신공영", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "trigger_type": "Stage4B-Local-PFOrderbookMarginRisk", "entry_date": "2024-02-01", "entry_price": 7370.0, "mfe_30_pct": 5.97, "mae_30_pct": -3.12, "mfe_90_pct": 5.97, "mae_90_pct": -16.42, "mfe_180_pct": 5.97, "mae_180_pct": -16.42, "peak_date": "2024-02-02", "peak_price": 7810.0, "drawdown_after_peak_pct": -21.13, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C30 local 4B-watch should fire when PF/orderbook/margin risk prevents a durable MFE path, even if the stock does not show a hard 4C collapse. 한신공영 is a local-risk boundary row: MAE opens and MFE is small, but full 4B/4C still needs explicit non-price deterioration.", "r13_flags": ["local_4b_watch_candidate", "riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R10", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_73_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B", "source_trigger_id": "TRG_R10L73-C30-047040-DAEWOO-LARGE-BUILDER-BUFFER-NOFULL4B", "symbol": "047040", "company_name": "대우건설", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_LIQUIDITY_STRESS_RECAPITALIZATION_BUFFER_VS_LOCAL_RISKWATCH_NO_HARD4C", "trigger_type": "Stage2-RiskWatch / LargeBuilderNoFull4B", "entry_date": "2024-02-01", "entry_price": 3910.0, "mfe_30_pct": 5.37, "mae_30_pct": -7.29, "mfe_90_pct": 5.37, "mae_90_pct": -7.29, "mfe_180_pct": 26.98, "mae_180_pct": -9.34, "peak_date": "2024-07-18", "peak_price": 4965.0, "drawdown_after_peak_pct": -28.6, "case_role_in_source": "overbearish_counterexample", "source_proxy_only": true, "evidence_url_pending": true, "current_profile_verdict": "C30 should distinguish large-builder PF fear from a balance-sheet break. 대우건설 had bounded MAE and later tradable MFE, so it should remain RiskWatch/no-full-4B unless explicit impairment/refinancing/default evidence appears.", "r13_flags": ["riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R11", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE", "source_trigger_id": "TRG_R11L73-C31-052690-KEPCO-ENC-CZECH-NUCLEAR-EPC-PROXY-CHASE", "symbol": "052690", "company_name": "한전기술", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "trigger_type": "Stage2-FalsePositive / NuclearEPCPolicyHeadlineChase", "entry_date": "2024-07-18", "entry_price": 95000.0, "mfe_30_pct": 3.26, "mae_30_pct": -35.16, "mfe_90_pct": 3.26, "mae_90_pct": -35.16, "mfe_180_pct": 3.26, "mae_180_pct": -47.58, "peak_date": "2024-07-18", "peak_price": 98100.0, "drawdown_after_peak_pct": -49.24, "case_role_in_source": "counterexample", "source_proxy_only": false, "evidence_url_pending": true, "current_profile_verdict": "C31 should not treat the nuclear preferred-bidder headline as durable Stage2 for EPC/engineering proxies unless named scope, contract allocation, revenue timing, or backlog bridge is visible. KEPCO E&C gapped into the event but then opened severe MAE and drawdown.", "r13_flags": ["early_mae_shock", "high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R11", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH", "source_trigger_id": "TRG_R11L73-C31-051600-KEPCO-KPS-CZECH-NUCLEAR-SERVICE-PROXY-RISKWATCH", "symbol": "051600", "company_name": "한전KPS", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "trigger_type": "Stage2-RiskWatch / NuclearServiceProxyNoFull4B", "entry_date": "2024-07-18", "entry_price": 43500.0, "mfe_30_pct": 9.08, "mae_30_pct": -17.59, "mfe_90_pct": 9.08, "mae_90_pct": -17.59, "mfe_180_pct": 10.57, "mae_180_pct": -17.59, "peak_date": "2025-01-24", "peak_price": 48100.0, "drawdown_after_peak_pct": -20.99, "case_role_in_source": "overbearish_counterexample", "source_proxy_only": false, "evidence_url_pending": true, "current_profile_verdict": "C31 should flag nuclear service proxies as RiskWatch unless service scope, O&M participation, or backlog bridge is verified. KEPCO KPS had bounded MAE and later recovery, so it should not become full 4B or hard 4C from the policy headline alone.", "r13_flags": ["riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R11", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE", "source_trigger_id": "TRG_R11L73-C31-083650-BHI-CZECH-NUCLEAR-EQUIPMENT-DELAYED-BRIDGE", "symbol": "083650", "company_name": "비에이치아이", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "trigger_type": "Stage2-DelayedPositive / NuclearEquipmentBridgeWithEarlyMAE", "entry_date": "2024-07-18", "entry_price": 10210.0, "mfe_30_pct": 3.13, "mae_30_pct": -30.46, "mfe_90_pct": 95.1, "mae_90_pct": -30.46, "mfe_180_pct": 142.9, "mae_180_pct": -30.46, "peak_date": "2025-02-14", "peak_price": 24800.0, "drawdown_after_peak_pct": -38.43, "case_role_in_source": "delayed_positive", "source_proxy_only": false, "evidence_url_pending": true, "current_profile_verdict": "C31 should not overblock true nuclear equipment/backlog beneficiaries, but the entry should not be a blind policy-headline chase. BHI had severe early MAE before later rerating; Stage2 requires non-proxy equipment order/backlog evidence and a lifecycle local 4B after peak.", "r13_flags": ["bad_entry_not_stage2", "delayed_positive_requires_source_repair", "delayed_winner_after_bad_entry", "early_mae_shock", "high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R12", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK", "source_trigger_id": "TRG_R12L73-C32-241560-DOOSANBOBCAT-MERGER-RATIO-MINORITY-RISK", "symbol": "241560", "company_name": "두산밥캣", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "trigger_type": "Stage4B-Local-MergerRatioMinorityRisk", "entry_date": "2024-07-12", "entry_price": 51500.0, "mfe_30_pct": 15.53, "mae_30_pct": -35.24, "mfe_90_pct": 15.53, "mae_90_pct": -35.24, "mfe_180_pct": 15.53, "mae_180_pct": -35.24, "peak_date": "2024-07-12", "peak_price": 59500.0, "drawdown_after_peak_pct": -43.95, "case_role_in_source": "counterexample", "source_proxy_only": false, "evidence_url_pending": true, "current_profile_verdict": "C32 should not treat a chaebol restructuring headline as positive control-premium evidence for the operating subsidiary when merger-ratio and minority-shareholder dilution risk dominate. Bobcat showed a brief squeeze but then opened deep MAE.", "r13_flags": ["early_mae_shock", "high_mae_180_guardrail", "high_mae_90_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R12", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B", "source_trigger_id": "TRG_R12L73-C32-454910-DOOSANROBOTICS-VALUATION-BETA-LOCAL4B", "symbol": "454910", "company_name": "두산로보틱스", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "trigger_type": "Stage2-FalsePositive / RoboticsMergerValuationBeta", "entry_date": "2024-07-12", "entry_price": 95000.0, "mfe_30_pct": 15.05, "mae_30_pct": -43.26, "mfe_90_pct": 15.05, "mae_90_pct": -43.26, "mfe_180_pct": 15.05, "mae_180_pct": -58.37, "peak_date": "2024-07-12", "peak_price": 109300.0, "drawdown_after_peak_pct": -63.82, "case_role_in_source": "counterexample", "source_proxy_only": false, "evidence_url_pending": true, "current_profile_verdict": "C32 should cap the acquirer/beneficiary valuation beta when the proposed restructuring implies control benefit but no earnings or closing bridge. Doosan Robotics had a large first-day MFE and then severe MAE, so price-only governance beta should be local 4B-watch.", "r13_flags": ["early_mae_shock", "high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 73, "source_round": "R12", "source_loop": "73", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM", "source_trigger_id": "TRG_R12L73-C32-000150-DOOSAN-HOLDCO-DELAYED-CONTROL-PREMIUM", "symbol": "000150", "company_name": "두산", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "DOOSAN_RESTRUCTURING_MERGER_RATIO_CONTROL_PREMIUM_VS_MINORITY_EXECUTION_RISK", "trigger_type": "Stage2-DelayedPositive / HoldcoControlPremiumAfterEarly4B", "entry_date": "2024-07-12", "entry_price": 263500.0, "mfe_30_pct": 0.0, "mae_30_pct": -53.7, "mfe_90_pct": 0.0, "mae_90_pct": -53.7, "mfe_180_pct": 46.49, "mae_180_pct": -53.7, "peak_date": "2025-02-26", "peak_price": 386000.0, "drawdown_after_peak_pct": -38.73, "case_role_in_source": "delayed_positive", "source_proxy_only": false, "evidence_url_pending": true, "current_profile_verdict": "C32 should not blindly block the holding company if control-premium option value later becomes visible, but the entry cannot be pure event chase because early MAE was severe. Doosan is a delayed positive with early local 4B risk and later lifecycle drawdown.", "r13_flags": ["bad_entry_not_stage2", "delayed_positive_requires_source_repair", "early_mae_shock", "high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
```

### R13 summary row

```jsonl
{"row_type": "r13_cross_summary", "round": "R13", "loop": 73, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "LOOP73_STAGE2_FALSE_POSITIVE_HIGH_MAE_LOCAL4B_SOURCE_REPAIR_CHECKPOINT", "selected_cross_case_count": 36, "source_rounds_covered": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_count": 12, "source_canonicals": ["C01_ORDER_BACKLOG_MARGIN_BRIDGE", "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "C14_EV_DEMAND_SLOWDOWN_4B_4C", "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"], "role_counts": {"positive": 13, "counterexample": 11, "riskwatch_boundary": 6, "overbearish_counterexample": 4, "delayed_positive": 2}, "stage2_false_positive_bridge_gap_count": 14, "early_mae_shock_count": 8, "high_mae_guardrail_count": 18, "post_peak_drawdown_guard_count": 23, "local_4b_watch_guard_count": 24, "hard_4c_confirmation_count": 0, "positive_anchor_not_to_overblock_count": 12, "winner_lifecycle_later_4b_count": 9, "delayed_positive_requires_source_repair_count": 2, "riskwatch_or_overbearish_boundary_count": 10, "source_repair_required_count": 36, "new_sector_positive_case_count": 0, "do_not_count_as_new_sector_case": true, "do_not_propose_new_weight_delta": true, "r13_decision": "guardrail_checkpoint_only"}
```

### R13 guardrail row

```jsonl
{"row_type": "r13_guardrail_candidate", "round": "R13", "loop": 73, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "axis": "stage2_false_positive_high_mae_local4b_vs_hard4c_and_delayed_positive_protection", "decision": "candidate_guardrail_observe_more", "do_not_propose_new_weight_delta": true, "proposed_runtime_effect": "Keep Stage2 bridge-based and hard 4C non-price-evidence-based. Strengthen local 4B-watch when price-only, policy, governance, beta, approval or demand-slowdown signals show early MAE shock, high 90/180D MAE, or post-peak drawdown without verified bridge refresh. Protect verified positives and delayed winners from overblocking, but require source repair before promotion.", "stage2_bridge_requirement_sketch": ["positive Stage2 requires non-price bridge evidence", "bridge examples: backlog/margin, customer adoption, utilization, reorder, capital return, reimbursement, contract scope, transaction economics", "price-only MFE cannot become Green"], "local_4b_watch_condition_sketch": ["MAE_30D <= -25% or MAE_90D <= -20% or MAE_180D <= -25%", "or post_peak_drawdown <= -35%", "and bridge evidence is absent, stale, capped, source_proxy_only, or evidence_url_pending", "local 4B is not hard 4C"], "hard_4c_condition_sketch": ["explicit non-price thesis break", "examples: default, court rehabilitation, contract cancellation, clinical/regulatory failure, insolvency, control/auditor break, project cancellation", "price collapse alone is insufficient"], "delayed_positive_protection": ["delayed winners with bad initial entry should not be labeled Green at the event gap", "but they should not be permanently blocked if later non-price bridge evidence becomes real", "promote only after source repair and lifecycle diagnostics"]}
```

---

## Score / return alignment summary

The cross-archetype alignment is:

```text
1. High MFE alone is not rerating.
2. Event-gap MFE plus high early MAE is not Stage2.
3. Stage2 requires non-price bridge evidence.
4. Local 4B-watch can be price-path assisted, but full 4B requires non-price deterioration.
5. Hard 4C requires explicit thesis-break evidence.
6. Delayed winners need source repair, not permanent overblocking.
7. Source-proxy rows can shape guardrails but should not promote production weights.
```

## Loop 73 residual decision

```text
r13_decision = guardrail_checkpoint_only
new_sector_positive_case_count = 0
do_not_propose_new_weight_delta = true
```

The useful candidate is a scoped diagnostic, not an immediate weight change:

```text
stage2_false_positive_high_mae_local4b_vs_hard4c_and_delayed_positive_protection
```

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this R13 standalone v12 cross-archetype red-team MD.
Do not patch production scoring blindly.

Scope:
canonical_scope = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
axis = stage2_false_positive_high_mae_local4b_vs_hard4c_and_delayed_positive_protection

Required checks:
1. Ingest only price_source_validation, r13_cross_case, r13_cross_summary and r13_guardrail_candidate rows.
2. Do not count these rows as new sector-positive coverage.
3. Validate each source trigger row against its original loop-73 MD and stock-web tradable_raw OHLC shard.
4. Keep Stage2 bridge-based.
5. Keep full 4B non-price evidence based.
6. Keep hard 4C evidence-based.
7. Consider local_4b_watch diagnostic when:
   - MAE_30D <= -25%, MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35%,
   - and bridge evidence is absent, stale, capped, source_proxy_only, or evidence_url_pending.
8. Do not convert local_4b_watch into hard 4C.
9. Protect verified positives and delayed winners if source repair confirms the bridge.
10. Reject implementation if controlled-MAE positives or verified delayed structural positives are overblocked.
11. Emit before/after diagnostics:
   - false positive reduction
   - missed structural positives
   - local 4B timing lead
   - hard 4C precision
   - delayed-winner protection
   - source-repair dependency.
```

---

## Final round state

```text
completed_round = R13
completed_loop = 73
next_round = R1
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

