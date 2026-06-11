# e2r stock-web v12 residual research — R4 / loop 102 / C15

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 102
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_ALUMINIUM_PRICE_RALLY_TO_COMPANY_MARGIN_BRIDGE_VS_METAL_BETA_FALSE_STAGE2
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection rationale

`C15_MATERIAL_SPREAD_SUPERCYCLE` remains a low-coverage canonical archetype in the repository index. The previous local C15 pass ended at `R4 / loop 101`, so this run advances the same round/canonical pair to `loop 102`.

This run focuses on the gap between:

- **metal price rally / commodity beta**: copper, aluminium, zinc or related material-price headlines,
- and **company-level spread conversion**: ASP, inventory gain, pass-through, volume, margin revision, and cash conversion.

The calibration question is not whether the metal price rose. The question is whether the listed company could convert that price move into durable equity return without a later 4B or 4C break.

## 2. Price source validation

- Atlas: `Songdaiki/stock-web`
- Shard root: `atlas/ohlcv_tradable_by_symbol_year`
- Basis: `tradable_raw`
- Adjustment caveat: raw/unadjusted FinanceData/marcap OHLC, corporate-action-contaminated windows blocked by default.
- Symbols checked in this run:
  - `006260` LS
  - `006110` 삼아알미늄
  - `018470` 조일알미늄

All three selected forward windows are after each symbol's old corporate-action candidate dates. They are calibration-usable at the selected 2024 windows, with the raw/unadjusted caveat retained.

## 3. Case matrix

| symbol | name | trigger | entry | entry px | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | classification |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 006260 | LS | Stage2-Actionable | 2024-05-13 | 150,300 | +29.61 / -8.58 | +29.61 / -37.46 | +29.61 / -43.78 | positive with local 4B watch |
| 006110 | 삼아알미늄 | Stage2-Watch | 2024-05-20 | 75,500 | +28.34 / -8.87 | +28.34 / -47.55 | +28.34 / -53.58 | counterexample: aluminium label high-MFE/high-MAE |
| 018470 | 조일알미늄 | Stage2-Watch | 2024-05-20 | 2,470 | +7.29 / -18.83 | +7.29 / -30.65 | +7.29 / -48.83 | counterexample: low-MFE/high-MAE aluminium beta |

## 4. Case notes

### 4.1 LS — positive, but not Green without refreshed bridge

LS had the cleanest company-level bridge in this sample: copper/materials plus cable/electrification exposure. The price path confirmed strong initial alignment. Entry at 150,300 on 2024-05-13 reached 194,800 on 2024-05-21, a +29.61% MFE. But the same path later printed 94,000 on 2024-08-05 and 84,500 on 2024-11-18.

Interpretation: C15 can keep Stage2-Actionable when the company has a direct material/cable/spread channel, but if non-price evidence is not refreshed after a vertical commodity move, local 4B watch must cap the contribution.

### 4.2 삼아알미늄 — high-MFE does not equal durable spread conversion

삼아알미늄 rose from 75,500 on 2024-05-20 to 96,900 on 2024-06-11. That is enough to explain why a price-only engine might mark it as actionable. The problem is the later path: 39,600 on 2024-08-05 and 35,050 on 2024-11-15.

Interpretation: an aluminium or battery-foil label can produce a temporary MFE, but without evidence of ASP pass-through, volume, inventory gain, and margin revision, C15 should not award a full Stage2-Actionable bonus.

### 4.3 조일알미늄 — low-MFE / high-MAE false positive

조일알미늄 is the cleanest false-positive in this run. Entry at 2,470 on 2024-05-20 produced only 2,650 on 2024-05-21, then the stock faded to 2,005 by 2024-06-24, 1,713 by 2024-10-17, and 1,264 by 2024-12-09.

Interpretation: generic aluminium rolling / commodity beta vocabulary is not C15 by itself. Without a listed-company spread bridge, this should be blocked at Stage2-Watch.

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 102, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINIUM_PRICE_RALLY_TO_COMPANY_MARGIN_BRIDGE_VS_METAL_BETA_FALSE_STAGE2", "symbol": "006260", "name": "LS", "market": "KOSPI", "trigger_type": "Stage2-Actionable", "entry_date": "2024-05-13", "entry_price": 150300, "mfe_30d_pct": 29.61, "mae_30d_pct": -8.58, "mfe_90d_pct": 29.61, "mae_90d_pct": -37.46, "mfe_180d_pct": 29.61, "mae_180d_pct": -43.78, "path_high_date": "2024-05-21", "path_high_price": 194800, "path_low_30d_date": "2024-06-20", "path_low_30d_price": 137400, "path_low_90d_date": "2024-08-05", "path_low_90d_price": 94000, "path_low_180d_date": "2024-11-18", "path_low_180d_price": 84500, "classification": "positive_with_high_MAE_local_4B_watch", "calibration_usable": true, "dedupe_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|006260|Stage2-Actionable|2024-05-13", "score_alignment": "MFE confirms material/cable/copper bridge, but full-window drawdown requires local 4B cap after vertical commodity beta fades.", "non_price_bridge": "copper/materials plus cable/electrification operating exposure; requires company-specific margin/revision refresh before Green."}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 102, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINIUM_PRICE_RALLY_TO_COMPANY_MARGIN_BRIDGE_VS_METAL_BETA_FALSE_STAGE2", "symbol": "006110", "name": "삼아알미늄", "market": "KOSPI", "trigger_type": "Stage2-Watch", "entry_date": "2024-05-20", "entry_price": 75500, "mfe_30d_pct": 28.34, "mae_30d_pct": -8.87, "mfe_90d_pct": 28.34, "mae_90d_pct": -47.55, "mfe_180d_pct": 28.34, "mae_180d_pct": -53.58, "path_high_date": "2024-06-11", "path_high_price": 96900, "path_low_30d_date": "2024-05-23", "path_low_30d_price": 68800, "path_low_90d_date": "2024-08-05", "path_low_90d_price": 39600, "path_low_180d_date": "2024-11-15", "path_low_180d_price": 35050, "classification": "counterexample_high_MFE_high_MAE_aluminium_label", "calibration_usable": true, "dedupe_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|006110|Stage2-Watch|2024-05-20", "score_alignment": "Aluminium/battery-foil label produced MFE, but no durable spread/margin bridge; Stage2 bonus should be capped.", "non_price_bridge": "aluminium label; direct pass-through, volume, inventory gain, and OPM revision bridge not confirmed."}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R4", "loop": 102, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINIUM_PRICE_RALLY_TO_COMPANY_MARGIN_BRIDGE_VS_METAL_BETA_FALSE_STAGE2", "symbol": "018470", "name": "조일알미늄", "market": "KOSPI", "trigger_type": "Stage2-Watch", "entry_date": "2024-05-20", "entry_price": 2470, "mfe_30d_pct": 7.29, "mae_30d_pct": -18.83, "mfe_90d_pct": 7.29, "mae_90d_pct": -30.65, "mfe_180d_pct": 7.29, "mae_180d_pct": -48.83, "path_high_date": "2024-05-21", "path_high_price": 2650, "path_low_30d_date": "2024-06-24", "path_low_30d_price": 2005, "path_low_90d_date": "2024-10-17", "path_low_90d_price": 1713, "path_low_180d_date": "2024-12-09", "path_low_180d_price": 1264, "classification": "counterexample_low_MFE_high_MAE_aluminium_beta", "calibration_usable": true, "dedupe_key": "C15_MATERIAL_SPREAD_SUPERCYCLE|018470|Stage2-Watch|2024-05-20", "score_alignment": "Commodity-label rally failed to translate into sustained equity path; classic low-MFE/high-MAE Stage2 false-positive.", "non_price_bridge": "aluminium rolling label only; no confirmed company-specific ASP-volume-margin bridge."}
```

## 6. Shadow scoring stress test

```json
{
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "proposed_rule_candidate": "C15_company_specific_spread_margin_bridge_requirement_v2",
  "positive_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "score_direction": {
    "006260": "keep Stage2-Actionable but cap with local 4B if bridge not refreshed",
    "006110": "remove Stage2-Actionable bonus; keep Stage2-Watch or 4B",
    "018470": "Stage2-FalsePositive / Stage2-Watch block"
  }
}
```

## 7. Rule candidate

```text
if canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE
and metal_price_rally_or_commodity_beta == true
and company_specific_ASP_volume_margin_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE
and MFE_30D_pct >= +20
and MAE_90D_pct <= -25
and refreshed_margin_or_revision_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE
and company_specific_spread_margin_bridge == true
and MFE_30D_pct >= +20:
    keep_stage2_actionable_bonus = true
    require_4B_refresh_after_vertical_move = true
```

## 8. Residual contribution summary

```yaml
new_independent_case_count: 3
reused_case_count_within_C15_visible_basis: 0
same_archetype_new_symbol_count_visible_index_basis: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
existing_axis_strengthened:
  - C15_company_specific_spread_margin_bridge_requirement
  - C15_metal_price_beta_stage2_block_without_margin_conversion
  - C15_vertical_MFE_local_4B_watch_after_commodity_rally
new_axis_proposed: null
```

## 9. Next recommended archetypes

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW,
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG,
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
