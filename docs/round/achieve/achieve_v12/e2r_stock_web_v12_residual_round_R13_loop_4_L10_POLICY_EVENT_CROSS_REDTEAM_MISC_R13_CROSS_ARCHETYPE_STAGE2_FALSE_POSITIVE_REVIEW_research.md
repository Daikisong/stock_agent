# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 4
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_VS_DIRECT_CONTRACT_OR_REAL_PROCESSING_ESCAPE_HATCH
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13 is a cross-archetype checkpoint, not a new sector-positive discovery round. This loop specifically retests `Stage2 false-positive` routing after the recent C15/C16/C04/C03 runs.

The prior local R13 Stage2 false-positive pair reached loop 3, so this same canonical pair continues as loop 4.

---

## 1. Research thesis

Stage2 is the “enter the workshop” gate. It should open when there is a real mechanical coupling between the event and listed-company revenue, margin, cash flow, or legally defined cash exit. It should stay shut when the signal is only a label.

This loop separates two families:

```text
False-positive family:
theme label + low MFE + deep MAE + no company-specific bridge
→ Stage2_FalsePositive_Block

Escape-hatch family:
direct signed contract / actual processing + cash bridge + sufficient MFE
→ keep Stage2-Actionable, but add 4B watch if MAE is high
```

Cases used:

- `025820 / C15-C16`: copper-processing label false positive.
- `021050 / C15-C16`: copper-alloy label false positive.
- `004020 / C15-C16`: large-cap steel/material label false positive.
- `457550 / C04`: nuclear supplier blowoff without contract/cash bridge.
- `103140 / C16`: actual dual-use copper/non-ferrous + ammunition bridge; positive-with-watch control.
- `064350 / C03`: foreign government signed K2 contract; direct-contract positive-control.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_cases: 6
  source_archetypes:
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
    - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - false-positive guardrail calibration
    - escape-hatch calibration
    - no production scoring changes
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"COPPER_PROCESSING_LABEL_LOW_MFE_HIGH_MAE_FALSE_POSITIVE","source_archetype_id":"C15_C16_SHARED","symbol":"025820","name":"이구산업","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":7880,"price_basis":"tradable_raw","mfe_30d_pct":6.85,"mae_30d_pct":-33.88,"mfe_90d_pct":6.85,"mae_90d_pct":-51.84,"mfe_180d_pct":6.85,"mae_180d_pct":-55.01,"forward_high_30d":8420,"forward_low_30d":5210,"forward_high_90d":8420,"forward_low_90d":3795,"forward_high_180d":8420,"forward_low_180d":3545,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|025820|Stage2-FalsePositive|2024-05-20","stage2_error":"commodity label without company-specific spread/cash bridge","route":"Stage2_FalsePositive_Block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"COPPER_ALLOY_LABEL_LOW_MFE_HIGH_MAE_FALSE_POSITIVE","source_archetype_id":"C15_C16_SHARED","symbol":"021050","name":"서원","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":1916,"price_basis":"tradable_raw","mfe_30d_pct":4.65,"mae_30d_pct":-28.18,"mfe_90d_pct":4.65,"mae_90d_pct":-43.95,"mfe_180d_pct":4.65,"mae_180d_pct":-48.17,"forward_high_30d":2005,"forward_low_30d":1377,"forward_high_90d":2005,"forward_low_90d":1074,"forward_high_180d":2005,"forward_low_180d":993,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|021050|Stage2-FalsePositive|2024-05-20","stage2_error":"copper-alloy theme without strategic customer/offtake/margin bridge","route":"Stage2_FalsePositive_Block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LARGECAP_STEEL_LABEL_WITHOUT_DEMAND_MARGIN_BRIDGE_FALSE_POSITIVE","source_archetype_id":"C15_C16_SHARED","symbol":"004020","name":"현대제철","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":32350,"price_basis":"tradable_raw","mfe_30d_pct":0.62,"mae_30d_pct":-11.90,"mfe_90d_pct":0.62,"mae_90d_pct":-24.73,"mfe_180d_pct":0.62,"mae_180d_pct":-38.49,"forward_high_30d":32550,"forward_low_30d":28500,"forward_high_90d":32550,"forward_low_90d":24350,"forward_high_180d":32550,"forward_low_180d":19900,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|004020|Stage2-FalsePositive|2024-05-20","stage2_error":"large-cap material importance without demand/margin/inventory bridge","route":"Stage2_FalsePositive_Block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"NUCLEAR_SUPPLIER_BLOWOFF_WITHOUT_FINAL_CONTRACT_CASH_BRIDGE_FALSE_POSITIVE","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":31500,"price_basis":"tradable_raw","mfe_30d_pct":32.06,"mae_30d_pct":-50.83,"mfe_90d_pct":32.06,"mae_90d_pct":-50.83,"mfe_180d_pct":32.06,"mae_180d_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":15490,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"case_role":"vertical_MFE_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|457550|Stage2-FalsePositive|2024-07-18","stage2_error":"intraday nuclear supplier blowoff without final contract or listed-company cash bridge","route":"Stage2_FalsePositive_Block_after_4B_watch"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"DUAL_USE_MATERIAL_REAL_PROCESSING_ESCAPE_HATCH_WITH_4B_WATCH","source_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable","entry_date":"2024-04-26","entry_close":62900,"price_basis":"tradable_raw","mfe_30d_pct":25.44,"mae_30d_pct":-10.17,"mfe_90d_pct":25.44,"mae_90d_pct":-25.28,"mfe_180d_pct":25.44,"mae_180d_pct":-26.63,"forward_high_30d":78900,"forward_low_30d":56500,"forward_high_90d":78900,"forward_low_90d":47000,"forward_high_180d":78900,"forward_low_180d":46150,"calibration_usable":true,"case_role":"positive_with_watch_control","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|103140|Stage2-Actionable|2024-04-26","stage2_escape":"actual non-ferrous processing plus defense/ammunition dual-use relevance","route":"Keep_Stage2_Actionable_with_4B_watch"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"FOREIGN_GOVERNMENT_SIGNED_CONTRACT_DIRECT_REVENUE_ESCAPE_HATCH","source_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"064350","name":"현대로템","trigger_type":"Stage2-Actionable","entry_date":"2025-08-01","entry_close":194000,"price_basis":"tradable_raw","mfe_30d_pct":6.96,"mae_30d_pct":-14.95,"mfe_90d_pct":28.61,"mae_90d_pct":-14.95,"mfe_180d_pct":28.61,"mae_180d_pct":-14.95,"forward_high_30d":207500,"forward_low_30d":165000,"forward_high_90d":249500,"forward_low_90d":165000,"forward_high_180d":249500,"forward_low_180d":165000,"calibration_usable":true,"case_role":"positive_control","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|064350|Stage2-Actionable|2025-08-01","stage2_escape":"foreign government signed K2 second-batch contract with local production component","route":"Keep_Stage2_Actionable"}
```

---

## 4. Case analysis

### Case A — 025820 이구산업: copper-processing label false positive

This is a pure Stage2 false-positive block. The entry-day high was not enough to build a real trend, and MAE expanded quickly. The core error is treating copper vocabulary as if it were margin conversion.

```text
MFE_90D < +10
MAE_90D <= -25
company-specific cash bridge absent
→ Stage2_FalsePositive_Block
```

### Case B — 021050 서원: copper-alloy label false positive

This is the same failure in a cleaner small-cap form. MFE stayed below +5, while MAE expanded to almost -50 by the full window. No Stage2-Actionable bonus should survive.

### Case C — 004020 현대제철: large-cap material label false positive

This case prevents an overly simple “small-cap theme only” guardrail. Even a large-cap steel/material company should be blocked if the event label does not translate into demand, spread, margin, utilization, or cash-flow bridge.

### Case D — 457550 우진엔텍: vertical MFE is not enough

This is the dangerous case: MFE was high, but the signal was a supplier blowoff without final contract/cash bridge. The model must not say “+32% MFE, therefore Stage2 worked.” The right sequence is local 4B watch, then false-positive block if bridge is not refreshed.

### Case E — 103140 풍산: real processing/dual-use escape hatch

`풍산` is not a blanket false positive. It has real non-ferrous/copper processing and defense/ammunition relevance, so Stage2 can remain open. However, because MAE crossed -25 by 90D/180D, it must be a Stage2-with-watch case, not Stage3-Green.

### Case F — 064350 현대로템: direct signed contract escape hatch

`현대로템` is the cleanest escape hatch. A foreign government signed contract with named platform, named supplier, and local-production component is not a theme label. Even with MAE near -15, this should remain Stage2-Actionable unless delivery/local-production economics break.

---

## 5. Aggregate score-return alignment

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_control_count: 2
counterexample_count: 4
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | reason |
|---|---:|---:|---:|---|
| 025820 | C15/C16 | hard block | +6.85 / -51.84 | label without bridge |
| 021050 | C15/C16 | hard block | +4.65 / -43.95 | label without bridge |
| 004020 | C15/C16 | hard block | +0.62 / -24.73 | large-cap material label fails |
| 457550 | C04 | 4B then block | +32.06 / -50.83 | blowoff without final cash bridge |
| 103140 | C16 | keep Stage2 + 4B watch | +25.44 / -25.28 | real processing/dual-use bridge |
| 064350 | C03 | keep Stage2 | +28.61 / -14.95 | direct signed contract |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"025820","raw_EPS_revision_bridge":0,"raw_visibility":1,"raw_bottleneck_supply":1,"raw_mispricing":1,"raw_validation":0,"raw_capital_return":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive"}
{"row_type":"score_simulation","symbol":"021050","raw_EPS_revision_bridge":0,"raw_visibility":1,"raw_bottleneck_supply":1,"raw_mispricing":1,"raw_validation":0,"raw_capital_return":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive"}
{"row_type":"score_simulation","symbol":"004020","raw_EPS_revision_bridge":0,"raw_visibility":1,"raw_bottleneck_supply":1,"raw_mispricing":1,"raw_validation":0,"raw_capital_return":0,"raw_info_edge":0,"stage2_actionable_bonus_before":1.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive"}
{"row_type":"score_simulation","symbol":"457550","raw_EPS_revision_bridge":0,"raw_visibility":1,"raw_bottleneck_supply":1,"raw_mispricing":2,"raw_validation":0,"raw_capital_return":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"4B-then-Stage2-FalsePositive"}
{"row_type":"score_simulation","symbol":"103140","raw_EPS_revision_bridge":2,"raw_visibility":3,"raw_bottleneck_supply":3,"raw_mispricing":1,"raw_validation":2,"raw_capital_return":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"064350","raw_EPS_revision_bridge":3,"raw_visibility":4,"raw_bottleneck_supply":2,"raw_mispricing":1,"raw_validation":3,"raw_capital_return":0,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The calibrated profile can still over-score:

```text
theme label + early spike + broad macro tailwind
```

That is too permissive when MFE is small or when MFE is only an intraday blowoff that collapses immediately.

### Main guardrail candidate

```text
R13_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_V4

if trigger_type in ["Stage2-Like", "Stage2-Actionable"]
and MFE_90D_pct < +10
and MAE_90D_pct <= -25
and company_specific_revenue_margin_cash_bridge == false:
    route = Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

### Blowoff guard

```text
if MFE_30D_pct >= +25
and MAE_30D_pct <= -25
and final_contract_or_direct_cash_bridge == false:
    route = 4B_watch_then_Stage2_FalsePositive_Block
    block_stage3_green = true
```

### Escape hatch

```text
if direct_signed_contract_or_actual_processing_capacity == true
and company_specific_revenue_margin_cash_bridge == true
and MFE_90D_pct >= +20:
    keep_stage2_actionable_bonus = true
    if MAE_90D_pct <= -20:
        local_4B_watch = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_stage2_false_positive_guardrail_candidate
new_axis_proposed: R13_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_V4
existing_axis_strengthened:
  - low_MFE_high_MAE_stage2_false_positive_block
  - vertical_MFE_without_bridge_4B_then_block
  - direct_contract_escape_hatch
  - real_processing_dual_use_escape_hatch_with_4B_watch
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C18_CONSUMER_EXPORT_CHANNEL_REORDER
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```
