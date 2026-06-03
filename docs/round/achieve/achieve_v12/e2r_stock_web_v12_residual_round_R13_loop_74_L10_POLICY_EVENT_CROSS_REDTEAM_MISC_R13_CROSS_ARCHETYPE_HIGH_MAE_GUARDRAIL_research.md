# E2R Stock-Web v12 R13 Cross-Archetype High-MAE Guardrail — Loop 74

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R13",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R13",
  "completed_loop": 74,
  "computed_next_round": "R1",
  "computed_next_loop": 75,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "fine_archetype_id": "LOOP74_HIGH_MAE_STAGE2_FALSE_POSITIVE_LOCAL4B_SOURCE_REPAIR_CHECKPOINT",
  "loop_objective": [
    "high_MAE_guardrail",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "stage2_false_positive_review",
    "delayed_positive_protection",
    "share_count_validation_queue_prioritization",
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

This is the R13 cross-archetype checkpoint for loop 74.  
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

Previous completed state in this interactive run: R12 / loop 74.

Therefore:

```text
scheduled_round = R13
scheduled_loop = 74
selected_large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
selected_canonical_scope = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
computed_next_round = R1
computed_next_loop = 75
```

R13 is a cross-archetype checkpoint, not an individual sector research round.  
The output file therefore uses `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` and `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`.

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

Loop 74 shows a recurring error mode:

```text
sector story or event heat
→ price MFE appears
→ bridge evidence remains source_proxy_only / evidence_url_pending / share-count validation pending
→ MAE opens or post-peak drawdown expands
→ local 4B-watch should activate before the model calls it durable Green
```

But the opposite error also matters:

```text
some controlled-MAE positives and delayed winners should not be permanently blocked
once the actual non-price bridge is repaired and verified.
```

The guardrail is a two-way valve:

```text
price-only MFE cannot become Green
price-only drawdown cannot become hard 4C
verified bridge evidence can still save delayed positives
```

## Cross-case checkpoint table

| src | symbol | archetype | role | MFE180 | MAE180 | DD after peak | R13 flags |
|---|---:|---|---|---:|---:|---:|---|
| R1 | 064350 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | positive | 124.92 | -3.24 | -36.26 | high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |
| R1 | 003570 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | positive | 93.02 | -0.62 | -42.34 | high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |
| R1 | 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | counterexample | 14.99 | -26.37 | -35.96 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R2 | 084370 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | positive | 58.94 | -16.29 | -47.33 | high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |
| R2 | 036810 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | positive | 66.73 | -43.47 | -66.09 | high_mae_180_guardrail,high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |
| R2 | 095610 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | counterexample | 40.0 | -44.3 | -60.21 | high_mae_180_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R3 | 137400 | C11_BATTERY_ORDERBOOK_RERATING | positive | 115.14 | -12.74 | -58.94 | positive_anchor_lifecycle_4b_watch,post_peak_drawdown_guard,share_count_validation_required,source_repair_required,winner_lifecycle_later_4b_required |
| R3 | 121600 | C11_BATTERY_ORDERBOOK_RERATING | positive | 50.29 | -44.0 | -62.74 | high_mae_180_guardrail,high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,share_count_validation_required,source_repair_required,winner_lifecycle_later_4b_required |
| R3 | 222080 | C11_BATTERY_ORDERBOOK_RERATING | counterexample | 49.01 | -30.47 | -53.34 | high_mae_180_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,share_count_validation_required,source_repair_required,stage2_false_positive_bridge_gap |
| R4 | 025820 | C15_MATERIAL_SPREAD_SUPERCYCLE | positive | 47.98 | -37.7 | -57.9 | high_mae_180_guardrail,high_mae_90_guardrail,high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,post_peak_drawdown_guard,source_repair_required |
| R4 | 012800 | C15_MATERIAL_SPREAD_SUPERCYCLE | counterexample | 57.82 | -25.85 | -53.02 | high_mae_180_guardrail,high_mae_90_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap,winner_lifecycle_later_4b_required |
| R4 | 001780 | C15_MATERIAL_SPREAD_SUPERCYCLE | counterexample | 13.53 | -45.41 | -51.92 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,share_count_validation_required,source_repair_required,stage2_false_positive_bridge_gap |
| R5 | 069960 | C19_BRAND_RETAIL_INVENTORY_MARGIN | positive | 15.27 | -17.97 | -28.84 | source_repair_required |
| R5 | 004170 | C19_BRAND_RETAIL_INVENTORY_MARGIN | riskwatch_boundary | 11.35 | -18.78 | -27.06 | riskwatch_or_overbearish_boundary,source_repair_required |
| R5 | 139480 | C19_BRAND_RETAIL_INVENTORY_MARGIN | counterexample | 16.29 | -27.2 | -37.4 | high_mae_180_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R6 | 000370 | C22_INSURANCE_RATE_CYCLE_RESERVE | positive | 44.21 | -3.94 | -21.91 | positive_anchor_not_to_overblock,source_repair_required |
| R6 | 003690 | C22_INSURANCE_RATE_CYCLE_RESERVE | positive | 25.99 | -1.45 | -19.37 | positive_anchor_not_to_overblock,share_count_validation_required,source_repair_required |
| R6 | 085620 | C22_INSURANCE_RATE_CYCLE_RESERVE | counterexample | 14.64 | -20.63 | -30.77 | high_mae_90_guardrail,source_repair_required,stage2_false_positive_bridge_gap |
| R7 | 141080 | C24_BIO_TRIAL_DATA_EVENT_RISK | delayed_positive | 111.18 | -10.88 | -36.42 | bad_entry_not_stage2,delayed_positive_requires_source_repair,post_peak_drawdown_guard,share_count_validation_required,source_repair_required,winner_lifecycle_later_4b_required |
| R7 | 298380 | C24_BIO_TRIAL_DATA_EVENT_RISK | delayed_positive | 76.37 | -12.42 | -39.15 | bad_entry_not_stage2,delayed_positive_requires_source_repair,high_mfe_then_drawdown,post_peak_drawdown_guard,share_count_validation_required,source_repair_required,winner_lifecycle_later_4b_required |
| R7 | 950220 | C24_BIO_TRIAL_DATA_EVENT_RISK | counterexample | 46.51 | -30.27 | -52.41 | high_mae_180_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R8 | 259960 | C27_CONTENT_IP_GLOBAL_MONETIZATION | positive | 61.73 | -0.91 | -20.85 | positive_anchor_not_to_overblock,share_count_validation_required,source_repair_required |
| R8 | 225570 | C27_CONTENT_IP_GLOBAL_MONETIZATION | positive | 66.58 | -32.51 | -59.48 | delayed_or_volatile_winner_after_bad_entry,high_mae_180_guardrail,high_mfe_then_drawdown,positive_anchor_lifecycle_4b_watch,post_peak_drawdown_guard,share_count_validation_required,source_repair_required,winner_lifecycle_later_4b_required |
| R8 | 263750 | C27_CONTENT_IP_GLOBAL_MONETIZATION | counterexample | 6.24 | -39.8 | -43.34 | high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R9 | 012330 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | positive | 29.33 | -3.61 | -25.47 | positive_anchor_not_to_overblock,share_count_validation_required,source_repair_required |
| R9 | 005850 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | positive | 47.98 | -8.54 | -35.36 | positive_anchor_lifecycle_4b_watch,positive_anchor_not_to_overblock,post_peak_drawdown_guard,source_repair_required |
| R9 | 033530 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | counterexample | 23.69 | -26.13 | -40.28 | high_mae_180_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R10 | 002990 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | riskwatch_boundary | 0.57 | -45.71 | -46.02 | high_mae_180_guardrail,high_mae_90_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,riskwatch_or_overbearish_boundary,source_repair_required |
| R10 | 021320 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | counterexample | 18.56 | -14.02 | -27.48 | riskwatch_or_overbearish_boundary,source_repair_required,stage2_false_positive_bridge_gap |
| R10 | 002410 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | riskwatch_boundary | 2.04 | -43.41 | -44.54 | high_mae_180_guardrail,high_mae_90_guardrail,local_4b_watch_candidate,post_peak_drawdown_guard,riskwatch_or_overbearish_boundary,source_repair_required |
| R11 | 039610 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | delayed_positive | 65.7 | -21.21 | -51.19 | bad_entry_not_stage2,delayed_or_volatile_winner_after_bad_entry,delayed_positive_requires_source_repair,early_mae_shock_20,high_mae_90_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |
| R11 | 008970 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | counterexample | 42.81 | -50.64 | -65.44 | early_mae_shock_20,high_mae_180_guardrail,high_mae_90_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,share_count_validation_required,source_repair_required,stage2_false_positive_bridge_gap |
| R11 | 004090 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | counterexample | 29.79 | -43.46 | -56.44 | early_mae_shock_20,high_mae_180_guardrail,high_mae_90_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R12 | 003920 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | counterexample | 4.71 | -23.38 | -26.82 | source_repair_required,stage2_false_positive_bridge_gap |
| R12 | 040300 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | counterexample | 16.87 | -55.15 | -61.63 | high_mae_180_guardrail,high_mae_90_guardrail,post_peak_drawdown_guard,source_repair_required,stage2_false_positive_bridge_gap |
| R12 | 091810 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | delayed_positive | 65.14 | -28.99 | -57.0 | delayed_positive_requires_source_repair,high_mae_180_guardrail,high_mfe_then_drawdown,post_peak_drawdown_guard,source_repair_required,winner_lifecycle_later_4b_required |

---

## R13 clusters

### stage2_false_positive_bridge_gap

```json
[
  "TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA",
  "TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE",
  "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE",
  "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE",
  "TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B",
  "TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA",
  "TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE",
  "TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE",
  "TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE",
  "TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE",
  "TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C",
  "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE",
  "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE",
  "TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP",
  "TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE"
]
```
### early_mae_shock_20

```json
[
  "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE",
  "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE",
  "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE"
]
```
### early_mae_shock_25

```json
[]
```
### high_mae_90_guardrail

```json
[
  "TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE",
  "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE",
  "TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE",
  "TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE",
  "TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B",
  "TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE",
  "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE",
  "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE",
  "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE",
  "TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE"
]
```
### high_mae_180_guardrail

```json
[
  "TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA",
  "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS",
  "TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE",
  "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE",
  "TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE",
  "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE",
  "TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B",
  "TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA",
  "TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE",
  "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE",
  "TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE",
  "TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE",
  "TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B",
  "TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE",
  "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE",
  "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE",
  "TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE",
  "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE"
]
```
### post_peak_drawdown_guard

```json
[
  "TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG",
  "TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG",
  "TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA",
  "TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS",
  "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS",
  "TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE",
  "TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE",
  "TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE",
  "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE",
  "TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B",
  "TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA",
  "TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING",
  "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING",
  "TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE",
  "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE",
  "TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE",
  "TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN",
  "TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE",
  "TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B",
  "TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE",
  "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE",
  "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE",
  "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE",
  "TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE",
  "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE"
]
```
### high_mfe_then_drawdown

```json
[
  "TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG",
  "TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG",
  "TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS",
  "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS",
  "TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE",
  "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE",
  "TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE",
  "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE",
  "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING",
  "TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE",
  "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE",
  "TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE",
  "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE",
  "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE",
  "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE",
  "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE"
]
```
### winner_lifecycle_later_4b_required

```json
[
  "TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG",
  "TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG",
  "TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS",
  "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS",
  "TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE",
  "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE",
  "TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING",
  "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING",
  "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE",
  "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE",
  "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE"
]
```
### positive_anchor_not_to_overblock

```json
[
  "TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG",
  "TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG",
  "TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS",
  "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS",
  "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE",
  "TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN",
  "TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER",
  "TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION",
  "TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN",
  "TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN"
]
```
### delayed_positive_requires_source_repair

```json
[
  "TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING",
  "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING",
  "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE",
  "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE"
]
```
### riskwatch_or_overbearish_boundary

```json
[
  "TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH",
  "TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B",
  "TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C",
  "TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE"
]
```
### share_count_validation_required

```json
[
  "TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE",
  "TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B",
  "TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER",
  "TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING",
  "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING",
  "TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION",
  "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE",
  "TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN",
  "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE"
]
```
### source_repair_required

```json
[
  "TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG",
  "TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG",
  "TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA",
  "TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS",
  "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS",
  "TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE",
  "TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE",
  "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE",
  "TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE",
  "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE",
  "TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B",
  "TRG_R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN",
  "TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH",
  "TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA",
  "TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN",
  "TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER",
  "TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE",
  "TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING",
  "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING",
  "TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE",
  "TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION",
  "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE",
  "TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE",
  "TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN",
  "TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN",
  "TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE",
  "TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B",
  "TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C",
  "TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE",
  "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE",
  "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE",
  "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE",
  "TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP",
  "TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE",
  "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE"
]
```

---

## R13 guardrail candidate

```json
{
  "row_type": "r13_guardrail_candidate",
  "round": "R13",
  "loop": 74,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "axis": "high_mae_stage2_false_positive_local4b_vs_delayed_positive_protection",
  "decision": "candidate_guardrail_observe_more",
  "do_not_propose_new_weight_delta": true,
  "proposed_runtime_effect": "Keep Stage2 bridge-based and hard 4C non-price-evidence-based. Use high-MAE and post-peak drawdown as local 4B diagnostics when a sector thesis is price-only, source_proxy_only or evidence_url_pending. Protect controlled-MAE positives and delayed winners only after source repair confirms the non-price bridge.",
  "stage2_bridge_requirement_sketch": [
    "positive Stage2 requires non-price bridge evidence",
    "bridge examples: export backlog, order/customer bridge, margin conversion, CSM/reserve/capital return, trial endpoint/partner validation, retention/monetization, PF/refinancing, tender/minority economics",
    "price-only MFE cannot become Green"
  ],
  "local_4b_watch_condition_sketch": [
    "MAE_30D <= -20% or MAE_90D <= -20% or MAE_180D <= -25%",
    "or post_peak_drawdown <= -35%",
    "and bridge evidence is absent, stale, source_proxy_only, evidence_url_pending, or validation pending",
    "local 4B is not hard 4C"
  ],
  "hard_4c_condition_sketch": [
    "explicit non-price thesis break",
    "examples: default, court rehabilitation, contract cancellation, clinical/regulatory failure, insolvency, control/auditor break, project cancellation, financing break",
    "price collapse alone is insufficient"
  ],
  "delayed_positive_protection": [
    "delayed winners with bad initial entry should not be labeled immediate Green at the event gap",
    "but they should not be permanently blocked if later non-price bridge evidence becomes real",
    "promote only after source repair, share-count validation and lifecycle diagnostics"
  ],
  "share_count_validation_rule": [
    "if share_count_change_inside_window is true, keep the row calibration-usable for research shape but block runtime promotion until validated",
    "avoid extended windows that cross corporate-action candidate dates without adjustment"
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
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R1", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_74_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_case_id": "R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG", "source_trigger_id": "TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG", "symbol": "064350", "company_name": "현대로템", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "trigger_type": "Stage2-Actionable-GroundSystemsExportBacklog", "entry_date": "2024-02-22", "entry_price": 30900.0, "mfe_30_pct": 28.16, "mae_30_pct": -3.24, "mfe_90_pct": 56.31, "mae_90_pct": -3.24, "mfe_180_pct": 124.92, "mae_180_pct": -3.24, "peak_date": "2024-11-20", "peak_price": 69500.0, "drawdown_after_peak_pct": -36.26, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C03 should allow Stage2 when defense-export attention is tied to a named ground-systems framework, backlog visibility, production cadence and margin bridge. Hyundai Rotem's stock-web path had large MFE and limited entry-basis MAE; after the late-2024 peak, a local 4B lifecycle guard is still needed if export/backlog evidence stops refreshing.", "r13_flags": ["high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R1", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_74_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_case_id": "R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG", "source_trigger_id": "TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG", "symbol": "003570", "company_name": "SNT다이내믹스", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "trigger_type": "Stage2-Actionable-DefensePowertrainExportBacklog", "entry_date": "2024-02-01", "entry_price": 14610.0, "mfe_30_pct": 31.69, "mae_30_pct": -0.62, "mfe_90_pct": 54.0, "mae_90_pct": -0.62, "mfe_180_pct": 93.02, "mae_180_pct": -0.62, "peak_date": "2024-10-23", "peak_price": 28200.0, "drawdown_after_peak_pct": -42.34, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C03 should include defense powertrain and transmission suppliers when export programs convert into backlog and margin. SNT Dynamics produced a strong 180D MFE with very controlled entry MAE, but later drawdown after the October peak requires lifecycle local 4B if backlog/margin evidence fades.", "r13_flags": ["high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R1", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_74_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md", "source_case_id": "R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA", "source_trigger_id": "TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA", "symbol": "010820", "company_name": "퍼스텍", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "trigger_type": "Stage2-FalsePositive / DefenseElectronicsPriceBetaLocal4B", "entry_date": "2024-01-17", "entry_price": 3470.0, "mfe_30_pct": 14.99, "mae_30_pct": -8.79, "mfe_90_pct": 14.99, "mae_90_pct": -8.79, "mfe_180_pct": 14.99, "mae_180_pct": -26.37, "peak_date": "2024-01-17", "peak_price": 3990.0, "drawdown_after_peak_pct": -35.96, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C03 should not treat defense electronics or drone-theme price beta as durable Stage2 unless named export order, customer framework, backlog conversion or margin bridge is visible. Firstec had a same-day spike but later MAE and drawdown opened, so it is a local 4B-watch / false Stage2 row.", "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R2", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_74_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_case_id": "R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "source_trigger_id": "TRG_R2L74-C07-084370-EUGENE-TECH-DEPOSITION-EQUIPMENT-RS", "symbol": "084370", "company_name": "유진테크", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "trigger_type": "Stage2-Actionable-DepositionEquipmentRelativeStrength", "entry_date": "2024-03-21", "entry_price": 37750.0, "mfe_30_pct": 49.93, "mae_30_pct": -0.93, "mfe_90_pct": 58.94, "mae_90_pct": -0.93, "mfe_180_pct": 58.94, "mae_180_pct": -16.29, "peak_date": "2024-05-28", "peak_price": 60000.0, "drawdown_after_peak_pct": -47.33, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C07 should allow Stage2 when front-end deposition equipment relative strength connects to HBM/DRAM capex, customer order visibility and margin bridge. Eugene Tech produced high MFE with limited entry MAE, but later post-peak drawdown means a lifecycle local 4B guard is needed if order/margin evidence stops refreshing.", "r13_flags": ["high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R2", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_74_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_case_id": "R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS", "source_trigger_id": "TRG_R2L74-C07-036810-FST-EUV-CHILLER-ANCILLARY-EQUIPMENT-RS", "symbol": "036810", "company_name": "에프에스티", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "trigger_type": "Stage2-Actionable-AncillaryEquipmentRelativeStrength", "entry_date": "2024-04-09", "entry_price": 25100.0, "mfe_30_pct": 52.99, "mae_30_pct": 0.0, "mfe_90_pct": 66.73, "mae_90_pct": 0.0, "mfe_180_pct": 66.73, "mae_180_pct": -43.47, "peak_date": "2024-06-11", "peak_price": 41850.0, "drawdown_after_peak_pct": -66.09, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C07 can include ancillary equipment when relative strength is tied to customer adoption, capex timing and margin conversion. FST had strong early MFE, but the later collapse shows that price strength must decay into local 4B if order/customer bridge evidence fails to refresh.", "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R2", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_74_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_case_id": "R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE", "source_trigger_id": "TRG_R2L74-C07-095610-TES-HBM-EQUIPMENT-BETA-BRIDGE-FADE", "symbol": "095610", "company_name": "테스", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "FRONTEND_DEPOSITION_CHILLER_EQUIPMENT_RELATIVE_STRENGTH_VS_HBM_EQUIPMENT_BETA_FADE", "trigger_type": "Stage2-FalsePositive / EquipmentBetaBridgeFade", "entry_date": "2024-04-02", "entry_price": 23500.0, "mfe_30_pct": 40.0, "mae_30_pct": -4.04, "mfe_90_pct": 40.0, "mae_90_pct": -9.79, "mfe_180_pct": 40.0, "mae_180_pct": -44.3, "peak_date": "2024-04-17", "peak_price": 32900.0, "drawdown_after_peak_pct": -60.21, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C07 should not treat a one-month equipment beta spike as durable Stage2 unless named customer order, HBM-related capex, backlog or margin bridge refreshes. TES had strong initial MFE but later opened severe MAE and drawdown, making it a local 4B-watch / false Stage2 row.", "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R3", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "source_case_id": "R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE", "source_trigger_id": "TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE", "symbol": "137400", "company_name": "피엔티", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "trigger_type": "Stage2-Actionable-BatteryEquipmentOrderbookBridge", "entry_date": "2024-02-21", "entry_price": 41600.0, "mfe_30_pct": 15.87, "mae_30_pct": -4.57, "mfe_90_pct": 115.14, "mae_90_pct": -12.74, "mfe_180_pct": 115.14, "mae_180_pct": -12.74, "peak_date": "2024-06-19", "peak_price": 89500.0, "drawdown_after_peak_pct": -58.94, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C11 should allow Stage2 when equipment orderbook and delivery-slot visibility convert into margin/revision bridge. PNT produced very high MFE after the trigger, but later post-peak drawdown and an in-window share-count change require lifecycle local 4B and coding-agent validation.", "r13_flags": ["positive_anchor_lifecycle_4b_watch", "post_peak_drawdown_guard", "share_count_validation_required", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R3", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "source_case_id": "R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE", "source_trigger_id": "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE", "symbol": "121600", "company_name": "나노신소재", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "trigger_type": "Stage2-Actionable-CNTMaterialOrderbookBridge", "entry_date": "2024-02-21", "entry_price": 105000.0, "mfe_30_pct": 50.29, "mae_30_pct": 0.0, "mfe_90_pct": 50.29, "mae_90_pct": -4.57, "mfe_180_pct": 50.29, "mae_180_pct": -44.0, "peak_date": "2024-02-22", "peak_price": 157800.0, "drawdown_after_peak_pct": -62.74, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C11 should include battery material orderbook rerating when CNT additive capacity, customer qualification, order visibility and margin bridge are visible. Nano New Materials had a strong event-window MFE, but the later 2024 collapse shows lifecycle local 4B is necessary if customer/order evidence stops refreshing.", "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "share_count_validation_required", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R3", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R3_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "source_case_id": "R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE", "source_trigger_id": "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE", "symbol": "222080", "company_name": "씨아이에스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "trigger_type": "Stage2-FalsePositive / BatteryEquipmentCapexBetaFade", "entry_date": "2024-02-15", "entry_price": 10140.0, "mfe_30_pct": 49.01, "mae_30_pct": -1.38, "mfe_90_pct": 49.01, "mae_90_pct": -9.66, "mfe_180_pct": 49.01, "mae_180_pct": -30.47, "peak_date": "2024-03-11", "peak_price": 15110.0, "drawdown_after_peak_pct": -53.34, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C11 should not treat battery equipment or solid-state capex beta as durable Stage2 unless orderbook, delivery, customer or margin evidence refreshes. CIS generated a sharp MFE but later gave it back and opened large MAE, making it a false Stage2 / local 4B-watch row.", "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "share_count_validation_required", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R4", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_74_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "source_case_id": "R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE", "source_trigger_id": "TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE", "symbol": "025820", "company_name": "이구산업", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "trigger_type": "Stage2-Actionable-CopperFabricatorSpreadBridge", "entry_date": "2024-04-12", "entry_price": 5690.0, "mfe_30_pct": 47.98, "mae_30_pct": -4.04, "mfe_90_pct": 47.98, "mae_90_pct": -33.3, "mfe_180_pct": 47.98, "mae_180_pct": -37.7, "peak_date": "2024-05-20", "peak_price": 8420.0, "drawdown_after_peak_pct": -57.9, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C15 should allow Stage2 when copper rally is tied to product-specific spread, inventory effect, export price and margin bridge. Igu Industry produced a strong copper-cycle MFE, but the late-2024 collapse requires local 4B-watch if spread/margin evidence stops refreshing.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "post_peak_drawdown_guard", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R4", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_74_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "source_case_id": "R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE", "source_trigger_id": "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE", "symbol": "012800", "company_name": "대창", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "trigger_type": "Stage2-FalsePositive / CopperBrassPriceBetaFade", "entry_date": "2024-04-12", "entry_price": 1470.0, "mfe_30_pct": 57.82, "mae_30_pct": -4.49, "mfe_90_pct": 57.82, "mae_90_pct": -25.17, "mfe_180_pct": 57.82, "mae_180_pct": -25.85, "peak_date": "2024-05-21", "peak_price": 2320.0, "drawdown_after_peak_pct": -53.02, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C15 should not treat copper/brass price beta as durable Stage2 unless spread-to-margin and inventory/export bridge refreshes. Daechang produced a large MFE but quickly fell into high MAE and post-peak drawdown, so it is a false Stage2 / local 4B-watch row.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R4", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_74_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md", "source_case_id": "R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B", "source_trigger_id": "TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B", "symbol": "001780", "company_name": "알루코", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "trigger_type": "Stage2-FalsePositive / AluminumPriceBetaLocal4B", "entry_date": "2024-04-12", "entry_price": 3215.0, "mfe_30_pct": 13.53, "mae_30_pct": -4.51, "mfe_90_pct": 13.53, "mae_90_pct": -15.86, "mfe_180_pct": 13.53, "mae_180_pct": -45.41, "peak_date": "2024-04-18", "peak_price": 3650.0, "drawdown_after_peak_pct": -51.92, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C15 should not treat aluminum or battery-material profile beta as Green unless product mix, customer order, spread and margin bridge are explicit. Aluko produced only small MFE and then severe late-2024 MAE, making it local 4B-watch rather than durable Stage2.", "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "share_count_validation_required", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R5", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_74_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN", "source_trigger_id": "TRG_R5L74-C19-069960-HYUNDAI-DS-VALUEUP-TRAFFIC-MARGIN", "symbol": "069960", "company_name": "현대백화점", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "trigger_type": "Stage2-Actionable-DepartmentStoreValueupMarginBridge", "entry_date": "2024-02-01", "entry_price": 53700.0, "mfe_30_pct": 15.27, "mae_30_pct": -6.52, "mfe_90_pct": 15.27, "mae_90_pct": -10.52, "mfe_180_pct": 15.27, "mae_180_pct": -17.97, "peak_date": "2024-02-07", "peak_price": 61900.0, "drawdown_after_peak_pct": -28.84, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C19 should allow Stage2 only when low-PBR/value-up retail attention connects to traffic, inventory discipline, duty-free recovery or margin conversion. Hyundai Department Store produced a controlled-MAE positive path, but later drawdown still needs local 4B-watch if the margin bridge stops refreshing.", "r13_flags": ["source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R5", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_74_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH", "source_trigger_id": "TRG_R5L74-C19-004170-SHINSEGAE-DS-MARGIN-RISKWATCH", "symbol": "004170", "company_name": "신세계", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "trigger_type": "Stage2-RiskWatch / DepartmentStoreMarginBridgeWeak", "entry_date": "2024-02-01", "entry_price": 170900.0, "mfe_30_pct": 11.35, "mae_30_pct": -4.51, "mfe_90_pct": 11.35, "mae_90_pct": -12.52, "mfe_180_pct": 11.35, "mae_180_pct": -18.78, "peak_date": "2024-02-19", "peak_price": 190300.0, "drawdown_after_peak_pct": -27.06, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C19 should distinguish stable department-store value-up from durable inventory/margin rerating. Shinsegae had early MFE but later MAE opened and the return path was not strong enough to qualify as durable Green without stronger traffic/duty-free/margin evidence.", "r13_flags": ["riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R5", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R5_loop_74_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md", "source_case_id": "R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA", "source_trigger_id": "TRG_R5L74-C19-139480-EMART-GROCERY-TURNAROUND-PRICE-BETA", "symbol": "139480", "company_name": "이마트", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DEPARTMENT_STORE_VALUEUP_TRAFFIC_MARGIN_VS_GROCERY_TURNAROUND_PRICE_BETA", "trigger_type": "Stage2-FalsePositive / GroceryTurnaroundPriceBetaLocal4B", "entry_date": "2024-02-01", "entry_price": 76100.0, "mfe_30_pct": 16.29, "mae_30_pct": -9.2, "mfe_90_pct": 16.29, "mae_90_pct": -16.95, "mfe_180_pct": 16.29, "mae_180_pct": -27.2, "peak_date": "2024-02-02", "peak_price": 88500.0, "drawdown_after_peak_pct": -37.4, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C19 should not treat grocery retail/value-up price beta as durable Stage2 unless inventory turns, SSG/online losses, store traffic and margin bridge improve. E-Mart had early MFE but then opened deep MAE and a large post-peak drawdown, so the first signal should be local 4B-watch rather than Green.", "r13_flags": ["high_mae_180_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R6", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_74_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN", "source_trigger_id": "TRG_R6L74-C22-000370-HANWHA-GI-RESERVE-CAPITAL-RETURN", "symbol": "000370", "company_name": "한화손해보험", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "trigger_type": "Stage2-Actionable-GIReserveCapitalReturnBridge", "entry_date": "2024-02-01", "entry_price": 4320.0, "mfe_30_pct": 42.82, "mae_30_pct": -3.94, "mfe_90_pct": 42.82, "mae_90_pct": -3.94, "mfe_180_pct": 44.21, "mae_180_pct": -3.94, "peak_date": "2024-08-20", "peak_price": 6230.0, "drawdown_after_peak_pct": -21.91, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C22 should allow Stage2 when non-top P&C insurers show CSM, reserve release, loss-ratio improvement, K-ICS/capital return or shareholder-return bridge. Hanwha General Insurance produced high MFE with controlled entry-basis MAE, but later local 4B-watch is needed if the reserve/capital-return evidence stops refreshing.", "r13_flags": ["positive_anchor_not_to_overblock", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R6", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_74_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER", "source_trigger_id": "TRG_R6L74-C22-003690-KOREANRE-REINSURANCE-CYCLE-CAPITAL-BUFFER", "symbol": "003690", "company_name": "코리안리", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "trigger_type": "Stage2-Actionable-ReinsuranceRateCycleCapitalBuffer", "entry_date": "2024-02-01", "entry_price": 7580.0, "mfe_30_pct": 9.89, "mae_30_pct": -1.45, "mfe_90_pct": 12.8, "mae_90_pct": -1.45, "mfe_180_pct": 25.99, "mae_180_pct": -1.45, "peak_date": "2024-11-05", "peak_price": 9550.0, "drawdown_after_peak_pct": -19.37, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C22 should include reinsurers when pricing cycle, reserve adequacy and capital buffer translate into low-MAE rerating. Korean Re produced slow but durable MFE; however a late-2024 share-count change in the shard requires validation before runtime promotion.", "r13_flags": ["positive_anchor_not_to_overblock", "share_count_validation_required", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R6", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R6_loop_74_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md", "source_case_id": "R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE", "source_trigger_id": "TRG_R6L74-C22-085620-MIRAE-LIFE-BETA-BRIDGE-FADE", "symbol": "085620", "company_name": "미래에셋생명", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NON_TOP_INSURER_CSM_RESERVE_CAPITAL_RETURN_VS_LIFE_INSURANCE_BETA_FADE", "trigger_type": "Stage2-FalsePositive / LifeInsuranceBetaBridgeFade", "entry_date": "2024-02-01", "entry_price": 5670.0, "mfe_30_pct": 14.64, "mae_30_pct": -11.82, "mfe_90_pct": 14.64, "mae_90_pct": -20.63, "mfe_180_pct": 14.64, "mae_180_pct": -20.63, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -30.77, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C22 should not treat life-insurance/value-up beta as durable Stage2 unless CSM quality, reserve sensitivity, K-ICS and capital-return evidence refreshes. Mirae Asset Life had an early MFE but quickly opened 90D MAE and never produced a strong rerating path.", "r13_flags": ["high_mae_90_guardrail", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R7", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_74_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "source_case_id": "R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING", "source_trigger_id": "TRG_R7L74-C24-141080-LCB-ADC-PLATFORM-DATA-DERISKING", "symbol": "141080", "company_name": "리가켐바이오", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "trigger_type": "Stage2-DelayedPositive-ADCPlatformDataDeriskingPostCA", "entry_date": "2024-04-24", "entry_price": 68000.0, "mfe_30_pct": 5.59, "mae_30_pct": -10.88, "mfe_90_pct": 28.24, "mae_90_pct": -10.88, "mfe_180_pct": 111.18, "mae_180_pct": -10.88, "peak_date": "2024-11-11", "peak_price": 143600.0, "drawdown_after_peak_pct": -36.42, "case_role_in_source": "delayed_positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C24 should not treat a biotech data/platform event as instant Green at the first gap, but it should allow delayed Stage2 when clinical/platform derisking and partner validation become real. LigaChem Bio required post-CA validation and later lifecycle 4B after the November peak.", "r13_flags": ["bad_entry_not_stage2", "delayed_positive_requires_source_repair", "post_peak_drawdown_guard", "share_count_validation_required", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R7", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_74_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "source_case_id": "R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING", "source_trigger_id": "TRG_R7L74-C24-298380-ABL-BISPECIFIC-PLATFORM-DATA-RERATING", "symbol": "298380", "company_name": "에이비엘바이오", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "trigger_type": "Stage2-DelayedPositive-BispecificPlatformDataRerating", "entry_date": "2024-03-06", "entry_price": 24550.0, "mfe_30_pct": 24.24, "mae_30_pct": -10.39, "mfe_90_pct": 26.27, "mae_90_pct": -12.42, "mfe_180_pct": 76.37, "mae_180_pct": -12.42, "peak_date": "2024-10-17", "peak_price": 43300.0, "drawdown_after_peak_pct": -39.15, "case_role_in_source": "delayed_positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C24 should distinguish platform-data derisking from simple biotech beta. ABL Bio had an early tradable MFE, then later re-accelerated into a larger 180D MFE; however later drawdown and share-count change require lifecycle and validation controls.", "r13_flags": ["bad_entry_not_stage2", "delayed_positive_requires_source_repair", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "share_count_validation_required", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R7", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R7_loop_74_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md", "source_case_id": "R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE", "source_trigger_id": "TRG_R7L74-C24-950220-NEOIMMUNETECH-IMMUNOTHERAPY-TRIAL-HEADLINE-FADE", "symbol": "950220", "company_name": "네오이뮨텍", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "ADC_BISPECIFIC_PLATFORM_DATA_DERISKING_VS_IMMUNOTHERAPY_TRIAL_HEADLINE_FADE", "trigger_type": "Stage2-FalsePositive / ImmunotherapyTrialHeadlineFade", "entry_date": "2024-04-11", "entry_price": 1447.0, "mfe_30_pct": 46.51, "mae_30_pct": -10.23, "mfe_90_pct": 46.51, "mae_90_pct": -10.23, "mfe_180_pct": 46.51, "mae_180_pct": -30.27, "peak_date": "2024-05-14", "peak_price": 2120.0, "drawdown_after_peak_pct": -52.41, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C24 should not treat immunotherapy trial/headline spikes as durable Stage2 unless data quality, endpoint durability, partner path or commercialization bridge is visible. NeoImmuneTech had large MFE but later collapsed into high MAE and post-peak drawdown.", "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R8", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_74_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "source_case_id": "R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION", "source_trigger_id": "TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION", "symbol": "259960", "company_name": "크래프톤", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "trigger_type": "Stage2-Actionable-GlobalGameIPMonetizationBridge", "entry_date": "2024-02-13", "entry_price": 219500.0, "mfe_30_pct": 20.73, "mae_30_pct": -0.91, "mfe_90_pct": 37.59, "mae_90_pct": -0.91, "mfe_180_pct": 61.73, "mae_180_pct": -0.91, "peak_date": "2024-08-22", "peak_price": 355000.0, "drawdown_after_peak_pct": -20.85, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C27 should allow Stage2 when global game IP monetization is tied to live-ops, regional monetization, MAU/ARPU and margin bridge. Krafton produced a large, low-MAE rerating path; this is a positive anchor that should not be overblocked by generic content-beta guards.", "r13_flags": ["positive_anchor_not_to_overblock", "share_count_validation_required", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R8", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_74_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "source_case_id": "R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE", "source_trigger_id": "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE", "symbol": "225570", "company_name": "넥슨게임즈", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "trigger_type": "Stage2-Actionable-GlobalLaunchRetentionBridgeWithLifecycle4B", "entry_date": "2024-07-03", "entry_price": 18610.0, "mfe_30_pct": 66.58, "mae_30_pct": -11.39, "mfe_90_pct": 66.58, "mae_90_pct": -19.67, "mfe_180_pct": 66.58, "mae_180_pct": -32.51, "peak_date": "2024-08-09", "peak_price": 31000.0, "drawdown_after_peak_pct": -59.48, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C27 should allow a global launch name only if launch traction converts into retention, paying-user monetization, live-ops cadence and revenue bridge. Nexon Games produced a huge launch-window MFE, but later drawdown makes lifecycle local 4B mandatory unless retention/monetization evidence refreshes.", "r13_flags": ["delayed_or_volatile_winner_after_bad_entry", "high_mae_180_guardrail", "high_mfe_then_drawdown", "positive_anchor_lifecycle_4b_watch", "post_peak_drawdown_guard", "share_count_validation_required", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R8", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_74_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "source_case_id": "R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE", "source_trigger_id": "TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE", "symbol": "263750", "company_name": "펄어비스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "trigger_type": "Stage2-FalsePositive / TrailerAnticipationBetaFade", "entry_date": "2024-07-09", "entry_price": 44850.0, "mfe_30_pct": 6.24, "mae_30_pct": -15.83, "mfe_90_pct": 6.24, "mae_90_pct": -25.08, "mfe_180_pct": 6.24, "mae_180_pct": -39.8, "peak_date": "2024-07-10", "peak_price": 47650.0, "drawdown_after_peak_pct": -43.34, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C27 should not treat trailer/release-expectation beta as durable Stage2 unless release date, preorder/wishlist conversion, monetization model and revenue timing are visible. Pearl Abyss had limited MFE and then large MAE, so this is a false Stage2/local 4B row.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R9", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN", "source_trigger_id": "TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN", "symbol": "012330", "company_name": "현대모비스", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "trigger_type": "Stage2-Actionable-AutoModuleElectrificationMarginBridge", "entry_date": "2024-02-01", "entry_price": 208000.0, "mfe_30_pct": 29.33, "mae_30_pct": 0.0, "mfe_90_pct": 29.33, "mae_90_pct": 0.0, "mfe_180_pct": 29.33, "mae_180_pct": -3.61, "peak_date": "2024-03-15", "peak_price": 269000.0, "drawdown_after_peak_pct": -25.47, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C29 should allow Stage2 for non-OEM auto modules when value-up attention connects to A/S parts, electrification module mix, capital return and margin bridge. Hyundai Mobis produced controlled MAE and a clean MFE path, but shard share-count changes need validation.", "r13_flags": ["positive_anchor_not_to_overblock", "share_count_validation_required", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R9", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN", "source_trigger_id": "TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN", "symbol": "005850", "company_name": "에스엘", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "trigger_type": "Stage2-Actionable-AutoLightingADASMarginBridge", "entry_date": "2024-02-01", "entry_price": 32200.0, "mfe_30_pct": 13.2, "mae_30_pct": -0.93, "mfe_90_pct": 47.98, "mae_90_pct": -8.54, "mfe_180_pct": 47.98, "mae_180_pct": -8.54, "peak_date": "2024-06-17", "peak_price": 47650.0, "drawdown_after_peak_pct": -35.36, "case_role_in_source": "positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C29 should include lighting/ADAS suppliers when OEM mix, order cadence and margin conversion drive rerating. SL had strong MFE, but post-peak drawdown says lifecycle local 4B should fire if OEM mix or margin evidence fades.", "r13_flags": ["positive_anchor_lifecycle_4b_watch", "positive_anchor_not_to_overblock", "post_peak_drawdown_guard", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R9", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R9_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_case_id": "R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE", "source_trigger_id": "TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE", "symbol": "033530", "company_name": "SJG세종", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "trigger_type": "Stage2-FalsePositive / HydrogenExhaustPartsBetaFade", "entry_date": "2024-02-01", "entry_price": 5530.0, "mfe_30_pct": 23.69, "mae_30_pct": 0.0, "mfe_90_pct": 23.69, "mae_90_pct": 0.0, "mfe_180_pct": 23.69, "mae_180_pct": -26.13, "peak_date": "2024-03-06", "peak_price": 6840.0, "drawdown_after_peak_pct": -40.28, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C29 should not treat hydrogen/exhaust/auto-parts theme beta as durable Stage2 unless customer volume, OEM program, pricing or margin bridge is visible. SJG Sejong had a tradable spike but later MAE and post-peak drawdown opened.", "r13_flags": ["high_mae_180_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R10", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_74_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B", "source_trigger_id": "TRG_R10L74-C30-002990-KUMHO-PF-LIQUIDITY-ORDERBOOK-LOCAL4B", "symbol": "002990", "company_name": "금호건설", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "trigger_type": "Stage4B-Local-PFOrderbookLiquidityRisk", "entry_date": "2024-02-01", "entry_price": 5250.0, "mfe_30_pct": 0.57, "mae_30_pct": -12.1, "mfe_90_pct": 0.57, "mae_90_pct": -30.57, "mfe_180_pct": 0.57, "mae_180_pct": -45.71, "peak_date": "2024-02-01", "peak_price": 5280.0, "drawdown_after_peak_pct": -46.02, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C30 local 4B-watch should fire when mid-builder PF/orderbook/liquidity risk produces weak MFE and persistent MAE, but hard 4C still requires explicit non-price default, refinancing failure, court rehabilitation, auditor/control or solvency break.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R10", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_74_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C", "source_trigger_id": "TRG_R10L74-C30-021320-KCC-CONSTRUCTION-RISKWATCH-NO-HARD4C", "symbol": "021320", "company_name": "KCC건설", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "trigger_type": "Stage2-RiskWatch / BufferedBuilderNoHard4C", "entry_date": "2024-02-01", "entry_price": 4850.0, "mfe_30_pct": 4.54, "mae_30_pct": -5.88, "mfe_90_pct": 18.56, "mae_90_pct": -8.87, "mfe_180_pct": 18.56, "mae_180_pct": -14.02, "peak_date": "2024-04-08", "peak_price": 5750.0, "drawdown_after_peak_pct": -27.48, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C30 should not convert every regional-builder PF fear into full 4B or hard 4C when the price path has moderate MAE, tradable MFE and no confirmed non-price break. KCC Construction is a RiskWatch/no-hard-4C boundary row.", "r13_flags": ["riskwatch_or_overbearish_boundary", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R10", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R10_loop_74_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md", "source_case_id": "R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE", "source_trigger_id": "TRG_R10L74-C30-002410-BUMYANG-PF-LIQUIDITY-LOCAL4B-SEVERE", "symbol": "002410", "company_name": "범양건영", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_SMALL_BUILDER_PF_ORDERBOOK_LIQUIDITY_LOCAL4B_VS_BUFFERED_NO_HARD4C", "trigger_type": "Stage4B-Local-SeverePFLiquidityRiskNoHard4C", "entry_date": "2024-02-01", "entry_price": 1767.0, "mfe_30_pct": 2.04, "mae_30_pct": -9.11, "mfe_90_pct": 2.04, "mae_90_pct": -22.64, "mfe_180_pct": 2.04, "mae_180_pct": -43.41, "peak_date": "2024-02-02", "peak_price": 1803.0, "drawdown_after_peak_pct": -44.54, "case_role_in_source": "riskwatch_boundary", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C30 should catch severe small-builder PF/liquidity/local 4B risk when MAE and drawdown become large, but hard 4C still needs non-price proof. Bumyang Construction shows the price-path severity that should raise local 4B-watch, not a price-only hard 4C.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "local_4b_watch_candidate", "post_peak_drawdown_guard", "riskwatch_or_overbearish_boundary", "source_repair_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R11", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE", "source_trigger_id": "TRG_R11L74-C31-039610-HWASUNG-VALVE-GAS-POLICY-CONTRACT-BRIDGE", "symbol": "039610", "company_name": "화성밸브", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "trigger_type": "Stage2-PolicyLifecycle / GasValveContractBridgeCandidate", "entry_date": "2024-06-04", "entry_price": 8630.0, "mfe_30_pct": 28.39, "mae_30_pct": -21.21, "mfe_90_pct": 65.7, "mae_90_pct": -21.21, "mfe_180_pct": 65.7, "mae_180_pct": -21.21, "peak_date": "2024-09-25", "peak_price": 14300.0, "drawdown_after_peak_pct": -51.19, "case_role_in_source": "delayed_positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C31 can allow a policy-event lifecycle candidate when a valve or pipeline-infra name later connects to named procurement, order, EPC, utility or offshore infrastructure bridge. Hwasung Valve had a large MFE and later secondary peak, but still needs source repair and lifecycle local 4B after the peak.", "r13_flags": ["bad_entry_not_stage2", "delayed_or_volatile_winner_after_bad_entry", "delayed_positive_requires_source_repair", "early_mae_shock_20", "high_mae_90_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R11", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE", "source_trigger_id": "TRG_R11L74-C31-008970-DONGYANG-PIPELINE-POLICY-PROXY-FADE", "symbol": "008970", "company_name": "KBI동양철관", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "trigger_type": "Stage2-FalsePositive / PipelinePolicyProxyFade", "entry_date": "2024-06-04", "entry_price": 1175.0, "mfe_30_pct": 42.81, "mae_30_pct": -21.62, "mfe_90_pct": 42.81, "mae_90_pct": -31.49, "mfe_180_pct": 42.81, "mae_180_pct": -50.64, "peak_date": "2024-06-07", "peak_price": 1678.0, "drawdown_after_peak_pct": -65.44, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": true, "current_profile_verdict": "C31 should not convert a pipeline/steel-pipe policy proxy into durable Stage2 unless project ownership, procurement scope, actual order, EPC participation or revenue timing is visible. KBI Dongyang Steel Pipe had a large initial MFE but then deep MAE and post-peak drawdown.", "r13_flags": ["early_mae_shock_20", "high_mae_180_guardrail", "high_mae_90_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "share_count_validation_required", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R11", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_case_id": "R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE", "source_trigger_id": "TRG_R11L74-C31-004090-KOREA-PETROLEUM-POLICY-THEME-BETA-FADE", "symbol": "004090", "company_name": "한국석유", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "EAST_SEA_DEEPSEA_GAS_POLICY_RESOURCE_INFRA_CONTRACT_BRIDGE_VS_PROXY_HEADLINE_CHASE", "trigger_type": "Stage2-FalsePositive / OilGasPolicyThemeBetaFade", "entry_date": "2024-06-04", "entry_price": 21650.0, "mfe_30_pct": 29.79, "mae_30_pct": -22.54, "mfe_90_pct": 29.79, "mae_90_pct": -28.22, "mfe_180_pct": 29.79, "mae_180_pct": -43.46, "peak_date": "2024-06-05", "peak_price": 28100.0, "drawdown_after_peak_pct": -56.44, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C31 should not treat oil/gas policy attention as a durable Stage2 signal for an oil-product proxy without direct concession, supply, infrastructure, procurement or earnings bridge. Korea Petroleum produced strong event MFE but later opened high MAE and a large post-peak drawdown.", "r13_flags": ["early_mae_shock_20", "high_mae_180_guardrail", "high_mae_90_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R12", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP", "source_trigger_id": "TRG_R12L74-C32-003920-NAMYANG-CONTROL-TRANSFER-PREMIUM-CAP", "symbol": "003920", "company_name": "남양유업", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "trigger_type": "Stage2-FalsePositive / ControlTransferPremiumCap", "entry_date": "2024-01-05", "entry_price": 616000.0, "mfe_30_pct": 4.71, "mae_30_pct": -10.71, "mfe_90_pct": 4.71, "mae_90_pct": -18.99, "mfe_180_pct": 4.71, "mae_180_pct": -23.38, "peak_date": "2024-01-05", "peak_price": 645000.0, "drawdown_after_peak_pct": -26.82, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C32 should not treat legal/control-transfer resolution as durable Green unless minority economics, tender floor, capital policy, operational turnaround or closing economics bridge is visible. Namyang had small MFE and persistent MAE before the later share-split/corporate-action area, so it is a control-transfer premium-cap counterexample.", "r13_flags": ["source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R12", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE", "source_trigger_id": "TRG_R12L74-C32-040300-YTN-PRIVATIZATION-CONTROL-SALE-FADE", "symbol": "040300", "company_name": "YTN", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "trigger_type": "Stage2-FalsePositive / PrivatizationControlSaleFade", "entry_date": "2024-02-05", "entry_price": 5630.0, "mfe_30_pct": 16.87, "mae_30_pct": -13.77, "mfe_90_pct": 16.87, "mae_90_pct": -29.75, "mfe_180_pct": 16.87, "mae_180_pct": -55.15, "peak_date": "2024-02-07", "peak_price": 6580.0, "drawdown_after_peak_pct": -61.63, "case_role_in_source": "counterexample", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C32 should not treat privatization or control-sale approval as durable Stage2 unless minority tender economics, closing certainty, capital policy or earnings bridge is explicit. YTN had a short control-sale pop but then suffered high MAE and post-peak drawdown.", "r13_flags": ["high_mae_180_guardrail", "high_mae_90_guardrail", "post_peak_drawdown_guard", "source_repair_required", "stage2_false_positive_bridge_gap"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
{"row_type": "r13_cross_case", "round": "R13", "loop": 74, "source_round": "R12", "source_loop": "74", "source_file": "e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md", "source_case_id": "R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE", "source_trigger_id": "TRG_R12L74-C32-091810-TWAY-AIR-CONTROL-PREMIUM-DISPUTE-LIFECYCLE", "symbol": "091810", "company_name": "티웨이항공", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "CONTROL_TRANSFER_PRIVATIZATION_AIRLINE_STAKE_DISPUTE_ECONOMIC_BENEFICIARY_BRIDGE", "trigger_type": "Stage2-DelayedPositive / AirlineControlPremiumDisputeLifecycle", "entry_date": "2024-08-27", "entry_price": 2725.0, "mfe_30_pct": 42.39, "mae_30_pct": -0.55, "mfe_90_pct": 46.42, "mae_90_pct": -0.55, "mfe_180_pct": 65.14, "mae_180_pct": -28.99, "peak_date": "2025-01-31", "peak_price": 4500.0, "drawdown_after_peak_pct": -57.0, "case_role_in_source": "delayed_positive", "source_proxy_only": true, "evidence_url_pending": true, "share_count_change_inside_window": false, "current_profile_verdict": "C32 should allow a delayed control-premium dispute candidate when stake accumulation, management-rights pressure and strategic airline-route economics become credible. T'way produced a large MFE into early 2025, but the later collapse requires lifecycle local 4B if control-premium or route/capacity execution evidence fades.", "r13_flags": ["delayed_positive_requires_source_repair", "high_mae_180_guardrail", "high_mfe_then_drawdown", "post_peak_drawdown_guard", "source_repair_required", "winner_lifecycle_later_4b_required"], "r13_use": "guardrail_checkpoint_only_not_new_sector_case"}
```

### R13 summary row

```jsonl
{"row_type": "r13_cross_summary", "round": "R13", "loop": 74, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "LOOP74_HIGH_MAE_STAGE2_FALSE_POSITIVE_LOCAL4B_SOURCE_REPAIR_CHECKPOINT", "selected_cross_case_count": 36, "source_rounds_covered": ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"], "source_canonical_count": 12, "source_canonicals": ["C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "C11_BATTERY_ORDERBOOK_RERATING", "C15_MATERIAL_SPREAD_SUPERCYCLE", "C19_BRAND_RETAIL_INVENTORY_MARGIN", "C22_INSURANCE_RATE_CYCLE_RESERVE", "C24_BIO_TRIAL_DATA_EVENT_RISK", "C27_CONTENT_IP_GLOBAL_MONETIZATION", "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"], "role_counts": {"positive": 14, "counterexample": 15, "riskwatch_boundary": 3, "delayed_positive": 4}, "stage2_false_positive_bridge_gap_count": 15, "early_mae_shock_20_count": 3, "early_mae_shock_25_count": 0, "high_mae_90_guardrail_count": 10, "high_mae_180_guardrail_count": 19, "post_peak_drawdown_guard_count": 27, "high_mfe_then_drawdown_count": 17, "winner_lifecycle_later_4b_required_count": 12, "positive_anchor_not_to_overblock_count": 10, "delayed_positive_requires_source_repair_count": 4, "riskwatch_or_overbearish_boundary_count": 4, "share_count_validation_required_count": 11, "source_repair_required_count": 36, "new_sector_positive_case_count": 0, "do_not_count_as_new_sector_case": true, "do_not_propose_new_weight_delta": true, "r13_decision": "guardrail_checkpoint_only"}
```

### R13 guardrail row

```jsonl
{"row_type": "r13_guardrail_candidate", "round": "R13", "loop": 74, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "axis": "high_mae_stage2_false_positive_local4b_vs_delayed_positive_protection", "decision": "candidate_guardrail_observe_more", "do_not_propose_new_weight_delta": true, "proposed_runtime_effect": "Keep Stage2 bridge-based and hard 4C non-price-evidence-based. Use high-MAE and post-peak drawdown as local 4B diagnostics when a sector thesis is price-only, source_proxy_only or evidence_url_pending. Protect controlled-MAE positives and delayed winners only after source repair confirms the non-price bridge.", "stage2_bridge_requirement_sketch": ["positive Stage2 requires non-price bridge evidence", "bridge examples: export backlog, order/customer bridge, margin conversion, CSM/reserve/capital return, trial endpoint/partner validation, retention/monetization, PF/refinancing, tender/minority economics", "price-only MFE cannot become Green"], "local_4b_watch_condition_sketch": ["MAE_30D <= -20% or MAE_90D <= -20% or MAE_180D <= -25%", "or post_peak_drawdown <= -35%", "and bridge evidence is absent, stale, source_proxy_only, evidence_url_pending, or validation pending", "local 4B is not hard 4C"], "hard_4c_condition_sketch": ["explicit non-price thesis break", "examples: default, court rehabilitation, contract cancellation, clinical/regulatory failure, insolvency, control/auditor break, project cancellation, financing break", "price collapse alone is insufficient"], "delayed_positive_protection": ["delayed winners with bad initial entry should not be labeled immediate Green at the event gap", "but they should not be permanently blocked if later non-price bridge evidence becomes real", "promote only after source repair, share-count validation and lifecycle diagnostics"], "share_count_validation_rule": ["if share_count_change_inside_window is true, keep the row calibration-usable for research shape but block runtime promotion until validated", "avoid extended windows that cross corporate-action candidate dates without adjustment"]}
```

---

## Score / return alignment summary

The cross-archetype alignment is:

```text
1. MFE is not enough when the bridge is missing.
2. Early MAE shock is a local 4B timing clue, not a hard 4C verdict.
3. High 90D/180D MAE should demote source-proxy Stage2 attempts.
4. Post-peak drawdown <= -35% should trigger lifecycle 4B diagnostics.
5. Hard 4C remains non-price evidence based.
6. Controlled-MAE positives should not be overblocked.
7. Delayed winners require source repair and lifecycle decay logic.
8. Share-count validation gates runtime promotion.
```

## Loop 74 residual decision

```text
r13_decision = guardrail_checkpoint_only
new_sector_positive_case_count = 0
do_not_propose_new_weight_delta = true
```

The useful candidate is a scoped diagnostic, not an immediate weight change:

```text
high_mae_stage2_false_positive_local4b_vs_delayed_positive_protection
```

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this R13 standalone v12 cross-archetype high-MAE guardrail MD.
Do not patch production scoring blindly.

Scope:
canonical_scope = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
axis = high_mae_stage2_false_positive_local4b_vs_delayed_positive_protection

Required checks:
1. Ingest only price_source_validation, r13_cross_case, r13_cross_summary and r13_guardrail_candidate rows.
2. Do not count these rows as new sector-positive coverage.
3. Validate each source trigger row against its original loop-74 MD and stock-web tradable_raw OHLC shard.
4. Keep Stage2 bridge-based.
5. Keep full 4B non-price evidence based.
6. Keep hard 4C evidence-based.
7. Consider local_4b_watch diagnostic when:
   - MAE_30D <= -20%, MAE_90D <= -20%, MAE_180D <= -25%, or post-peak drawdown <= -35%,
   - and bridge evidence is absent, stale, source_proxy_only, evidence_url_pending, or validation pending.
8. Do not convert local_4b_watch into hard 4C.
9. Protect controlled-MAE positives and delayed winners if source repair confirms the bridge.
10. Block runtime promotion when share_count_change_inside_window=true until validation is complete.
11. Reject implementation if controlled-MAE positives or verified delayed structural positives are overblocked.
12. Emit before/after diagnostics:
   - false positive reduction
   - missed structural positives
   - local 4B timing lead
   - hard 4C precision
   - delayed-winner protection
   - share-count validation dependency
   - source-repair dependency.
```

---

## Final round state

```text
completed_round = R13
completed_loop = 74
next_round = R1
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

