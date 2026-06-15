# stock-web v12 residual research — R13 Stage2 false-positive review v3

file_name: `e2r_stock_web_v12_residual_round_R13_loop_3_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md`

## Execution metadata

- selected_round: `R13`
- selected_loop: `3`
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- canonical_archetype_id: `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`
- fine_archetype_id: `LOW_MFE_HIGH_MAE_STAGE2_FALSE_POSITIVE_VS_DIRECT_CASH_REVENUE_BRIDGE_ESCAPE_HATCH`
- selection_basis: `docs/core/V12_Research_No_Repeat_Index.md`
- selected_priority_bucket: `Priority 0`
- round_schedule_status: `coverage_index_selected`
- round_sector_consistency: `pass`
- price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- stock_web_manifest_max_date: `2026-02-20`
- research_mode: `cross_archetype_guardrail_retest`
- artifact_type: `e2r_stock_web_v12_residual_round_md`

## Why this round

The immediately preceding local output strengthened `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`. The next recommended cross-check is `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`.

This is not a sector-positive mining round. It is a checkpoint that compares labels which looked Stage2-like at the trigger date but failed to translate into durable price alignment unless a direct company-specific revenue, margin, cash, tender, or contract bridge existed.

## Case table

| symbol | name | source archetype | entry date | entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | route |
|---|---|---|---:|---:|---:|---:|---:|---|
| 009830 | 한화솔루션 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 2024-05-20 | 31,800 | 7.86% / -11.79% | 7.86% / -30.35% | 7.86% / -37.11% | Stage2_FalsePositive_Block |
| 018470 | 조일알미늄 | C15_MATERIAL_SPREAD_SUPERCYCLE | 2024-05-20 | 2,470 | 7.29% / -18.83% | 7.29% / -41.3% | 7.29% / -48.83% | Stage2_FalsePositive_Block |
| 005380 | 현대차 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 2024-08-28 | 259,000 | 3.09% / -14.48% | 3.09% / -22.82% | 3.09% / -32.12% | Contribution_Cap_Or_Stage2_Watch |
| 011200 | HMM | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 2024-01-02 | 20,600 | 4.85% / -8.16% | 4.85% / -27.14% | 4.85% / -27.14% | Stage2_FalsePositive_Block |
| 011790 | SKC | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 2024-05-23 | 117,000 | 70.94% / -13.42% | 70.94% / -13.42% | 70.94% / -22.82% | Dominant_Driver_Contamination_Cap |
| 064350 | 현대로템 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 2025-02-26 | 85,600 | 36.45% / -8.64% | 157.59% / -8.64% | 157.59% / -8.64% | Keep_Stage2_Actionable_Escape_Hatch |

## Case notes

### 1) 한화솔루션 / C17 — petrochemical or solar label without margin bridge

- classification: `counterexample`
- route: `Stage2_FalsePositive_Block`
- entry: `2024-05-20 close 31,800`
- price path: high stayed near `34,300`, while the path later broke to `22,150` and then `20,000`.
- interpretation: low margins, oversupply, feedstock substitution, or solar/chemical vocabulary is not enough. Without segment-level margin revision or cash bridge, C17 Stage2-Actionable should be blocked.

### 2) 조일알미늄 / C15 — aluminium beta label without listed-company spread conversion

- classification: `counterexample`
- route: `Stage2_FalsePositive_Block`
- entry: `2024-05-20 close 2,470`
- price path: high reached only `2,650`, then broke to `1,450` and later `1,264`.
- interpretation: aluminium rolling or commodity-beta vocabulary does not equal company-specific ASP, volume, inventory gain, margin, or cash conversion.

### 3) 현대차 / C31 — real shareholder-return policy but failed price alignment

- classification: `counterexample`
- route: `Contribution_Cap_Or_Stage2_Watch`
- entry: `2024-08-28 close 259,000`
- price path: high stayed near `267,000`, while full-window low fell to `175,800`.
- interpretation: even a real shareholder-return plan can be overwhelmed by margin-cycle or auto-demand drivers. Policy-event score should be capped unless price alignment is confirmed.

### 4) HMM / C32 — control-sale process without minority cash exit

- classification: `counterexample`
- route: `Stage2_FalsePositive_Block`
- entry: `2024-01-02 close 20,600`
- price path: high reached only `21,600`, while low reached `15,010`.
- interpretation: control-sale headlines are not the same as a legally defined tender/buyback cash-exit path for minority shareholders.

### 5) SKC / C17 — large MFE but dominant-driver contamination

- classification: `counterexample`
- route: `Dominant_Driver_Contamination_Cap`
- entry: `2024-05-23 close 117,000`
- price path: high reached `200,000`, but the driver should not be credited as pure chemical feedstock-product spread. Later low reached `90,300`.
- interpretation: not every large MFE should be learned by the current canonical archetype. If the dominant driver belongs to another canonical family, cap the source-archetype contribution and require reclassification.

### 6) 현대로템 / C31 — positive-control escape hatch

- classification: `positive_control`
- route: `Keep_Stage2_Actionable_Escape_Hatch`
- entry: `2025-02-26 close 85,600`
- price path: high reached `116,800` within the early window and `220,500` in the extended window; low stayed around `78,200`.
- interpretation: a signed contract with direct revenue bridge and price-return alignment should not be blocked by the false-positive guardrail.

## Rule candidate

```text
R13_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_V3

if trigger_type in ["Stage2-Like", "Stage2-Actionable"]
and MFE_90D_pct < +10
and MAE_90D_pct <= -25
and company_specific_revenue_margin_cash_bridge == false:
    route = Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if trigger_type in ["Stage2-Like", "Stage2-Actionable"]
and event_is_real == true
and MFE_90D_pct < +10
and MAE_180D_pct <= -25
and price_return_alignment_confirmed == false:
    route = Contribution_Cap_Or_Stage2_Watch
```

```text
if MFE_30D_pct >= +30
and dominant_price_driver != selected_canonical_archetype_driver:
    route = Dominant_Driver_Contamination_Cap
    cap_source_archetype_contribution = true
    require_cross_archetype_reclassification = true
```

```text
escape_hatch:
if direct_contract_or_cash_transfer_or_tender_cash_exit == true
and company_specific_revenue_or_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    do_not_apply_false_positive_block = true
```

## Trigger rows JSONL

```jsonl
{"case_id": "R13_STAGE2_FP_V3_001", "symbol": "009830", "name": "한화솔루션", "source_archetype": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "trigger_type": "Stage2-Like", "entry_date": "2024-05-20", "entry_close": 31800, "high_30d": 34300, "low_30d": 28050, "high_90d": 34300, "low_90d": 22150, "high_180d": 34300, "low_180d": 20000, "classification": "counterexample", "route": "Stage2_FalsePositive_Block", "reason": "solar/petrochemical/feedstock label without company-specific segment margin and cash bridge; low MFE/high MAE.", "mfe_30d_pct": 7.86, "mae_30d_pct": -11.79, "mfe_90d_pct": 7.86, "mae_90d_pct": -30.35, "mfe_180d_pct": 7.86, "mae_180d_pct": -37.11}
{"case_id": "R13_STAGE2_FP_V3_002", "symbol": "018470", "name": "조일알미늄", "source_archetype": "C15_MATERIAL_SPREAD_SUPERCYCLE", "trigger_type": "Stage2-Like", "entry_date": "2024-05-20", "entry_close": 2470, "high_30d": 2650, "low_30d": 2005, "high_90d": 2650, "low_90d": 1450, "high_180d": 2650, "low_180d": 1264, "classification": "counterexample", "route": "Stage2_FalsePositive_Block", "reason": "aluminium rolling/commodity beta vocabulary without listed-company ASP-volume-margin bridge.", "mfe_30d_pct": 7.29, "mae_30d_pct": -18.83, "mfe_90d_pct": 7.29, "mae_90d_pct": -41.3, "mfe_180d_pct": 7.29, "mae_180d_pct": -48.83}
{"case_id": "R13_STAGE2_FP_V3_003", "symbol": "005380", "name": "현대차", "source_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "trigger_type": "Stage2-Like", "entry_date": "2024-08-28", "entry_close": 259000, "high_30d": 267000, "low_30d": 221500, "high_90d": 267000, "low_90d": 199900, "high_180d": 267000, "low_180d": 175800, "classification": "counterexample", "route": "Contribution_Cap_Or_Stage2_Watch", "reason": "shareholder-return policy was real but price-return alignment failed as margin/auto-cycle override dominated.", "mfe_30d_pct": 3.09, "mae_30d_pct": -14.48, "mfe_90d_pct": 3.09, "mae_90d_pct": -22.82, "mfe_180d_pct": 3.09, "mae_180d_pct": -32.12}
{"case_id": "R13_STAGE2_FP_V3_004", "symbol": "011200", "name": "HMM", "source_archetype": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "trigger_type": "Stage2-Like", "entry_date": "2024-01-02", "entry_close": 20600, "high_30d": 21600, "low_30d": 18920, "high_90d": 21600, "low_90d": 15010, "high_180d": 21600, "low_180d": 15010, "classification": "counterexample", "route": "Stage2_FalsePositive_Block", "reason": "control-sale process/headline without minority cash-exit tender path.", "mfe_30d_pct": 4.85, "mae_30d_pct": -8.16, "mfe_90d_pct": 4.85, "mae_90d_pct": -27.14, "mfe_180d_pct": 4.85, "mae_180d_pct": -27.14}
{"case_id": "R13_STAGE2_FP_V3_005", "symbol": "011790", "name": "SKC", "source_archetype": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "trigger_type": "Stage2-Like", "entry_date": "2024-05-23", "entry_close": 117000, "high_30d": 200000, "low_30d": 101300, "high_90d": 200000, "low_90d": 101300, "high_180d": 200000, "low_180d": 90300, "classification": "counterexample", "route": "Dominant_Driver_Contamination_Cap", "reason": "large MFE existed, but dominant driver was not pure feedstock-product chemical spread; cap C17 contribution.", "mfe_30d_pct": 70.94, "mae_30d_pct": -13.42, "mfe_90d_pct": 70.94, "mae_90d_pct": -13.42, "mfe_180d_pct": 70.94, "mae_180d_pct": -22.82}
{"case_id": "R13_STAGE2_FP_V3_006", "symbol": "064350", "name": "현대로템", "source_archetype": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "trigger_type": "Stage2-Actionable", "entry_date": "2025-02-26", "entry_close": 85600, "high_30d": 116800, "low_30d": 78200, "high_90d": 220500, "low_90d": 78200, "high_180d": 220500, "low_180d": 78200, "classification": "positive_control", "route": "Keep_Stage2_Actionable_Escape_Hatch", "reason": "signed export/rail order with direct revenue bridge and strong price-return alignment.", "mfe_30d_pct": 36.45, "mae_30d_pct": -8.64, "mfe_90d_pct": 157.59, "mae_90d_pct": -8.64, "mfe_180d_pct": 157.59, "mae_180d_pct": -8.64}
```

## Residual contribution summary

- new_independent_case_count: `6`
- reused_case_count_within_R13_STAGE2_FALSE_POSITIVE: `0`
- calibration_usable case 수: `6`
- calibration_usable trigger 수: `6`
- positive_control_count: `1`
- counterexample_count: `5`
- current_profile_error_count: `5`
- loop_contribution_label: `cross_archetype_stage2_false_positive_guardrail_candidate`
- new_axis_proposed: `R13_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_V3`
- existing_axis_strengthened:
  - `low_MFE_high_MAE_stage2_false_positive_block`
  - `real_event_price_alignment_contribution_cap`
  - `dominant_driver_contamination_cap`
  - `direct_contract_revenue_bridge_escape_hatch`
- next_recommended_archetypes:
  - `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM`
  - `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG`
  - `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY`
  - `C15_MATERIAL_SPREAD_SUPERCYCLE`
  - `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`

## Validation caveats

The stock-web atlas uses raw/unadjusted OHLC from FinanceData/marcap. Corporate-action contaminated windows are blocked by default; all selected case windows here are outside the listed corporate-action candidate dates for the specific trigger windows used.
