# stock-web v12 residual research — R1 / loop 112 / C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 112
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_DUKOVANY_REHEATED_SUPPLIER_THEME_SPIKE_AND_LEGAL_DELAY_RETEST
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
output_file: e2r_stock_web_v12_residual_round_R1_loop_112_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
```

## 1. Selection / novelty

C04 remains a low-coverage archetype in the repository index: 6 rows / 5 symbols, with visible top-covered symbols concentrated in `046120`, `019990`, `034020`, `083650`, and `126720`.

This loop retests the same canonical problem from a different trigger family: not the first Czech preferred-bidder reaction itself, but a later repeated supplier-theme reaction and the local 4B/Stage2-cap logic after legal-clearance risk became more visible.

Novelty rule:

```text
same canonical_archetype_id may be studied again
but same symbol + trigger_type + entry_date is not counted as a new independent case
```

Applied novelty:

| symbol | name | entry_date | novelty note |
|---|---|---:|---|
| 457550 | 우진엔텍 | 2024-07-18 | new visible C04 symbol |
| 032820 | 우리기술 | 2024-09-12 | reused symbol, new entry_date / reheated trigger family |
| 105840 | 우진 | 2024-09-12 | reused symbol, new entry_date / reheated trigger family |
| 006910 | 보성파워텍 | 2024-09-12 | reused symbol, new entry_date / reheated trigger family |
| 051600 | 한전KPS | 2024-09-12 | reused positive-control symbol, new entry_date |

## 2. External event frame

The C04 mechanism is not "nuclear headline = buy." It is:

```text
nuclear policy / preferred bidder headline
→ final contract and legal clearance
→ named listed-company scope
→ revenue / margin / cash bridge
→ price-return alignment
```

The external event frame remains the Czech Dukovany project. KHNP was selected as preferred bidder in July 2024, but EDF/Westinghouse appeals and later Czech antitrust/court steps created a legal-clearance path that had to be checked before supplier-theme spikes could be upgraded to Stage3/Green.

## 3. Trigger-level price-path table

| symbol | name | route | entry | entry_close | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 457550 | 우진엔텍 | counterexample | 2024-07-18 | 31,500 | 32.06% | -50.83% | 32.06% | -58.25% | 32.06% | -58.25% |
| 032820 | 우리기술 | counterexample | 2024-09-12 | 2,335 | 13.49% | -12.63% | 13.49% | -30.11% | 13.49% | -37.77% |
| 105840 | 우진 | counterexample | 2024-09-12 | 8,130 | 2.46% | -6.77% | 9.1% | -30.75% | 9.1% | -30.75% |
| 006910 | 보성파워텍 | counterexample | 2024-09-12 | 3,580 | 8.52% | -12.15% | 8.52% | -36.03% | 8.52% | -36.59% |
| 051600 | 한전KPS | positive_control | 2024-09-12 | 42,150 | 14.47% | -4.39% | 16.49% | -4.39% | 16.49% | -9.85% |


## 4. Case diagnostics

### 4.1 우진엔텍 / 457550 — new-symbol supplier spike counterexample

`457550` is useful because it is a newer listed nuclear-service/supplier theme vehicle and therefore not in the old visible C04 coverage list. It produced a large intraday MFE on 2024-07-18 but then showed a severe 90D/180D drawdown.

Interpretation:

```text
intraday supplier spike
without final contract / named scope / cash bridge
→ Stage2-Watch only
→ local 4B after spike
→ block Stage3-Green
```

### 4.2 우리기술 / 032820 — reheated supplier-theme false positive

`032820` showed a new 2024-09-12 reheated trigger rather than the earlier July trigger. MFE was small-to-moderate, while 90D/180D MAE expanded sharply. This is a clear Stage2 cap case.

### 4.3 우진 / 105840 — instrumentation vocabulary is insufficient

`105840` had instrumentation / nuclear supplier vocabulary, but price-return alignment was weak. A tiny 30D MFE and deep 90D MAE argue for a hard Stage2 cap unless a named listed-company cash bridge appears.

### 4.4 보성파워텍 / 006910 — grid/nuclear supplier label fade

`006910` behaved like a grid/nuclear supplier label spike. Without final contract scope and revenue bridge, the supplier label does not deserve C04 Stage2-Actionable bonus.

### 4.5 한전KPS / 051600 — positive-control escape hatch

`051600` is kept as an escape hatch. It did not deliver explosive MFE from the 2024-09-12 retest entry, but its low MAE and O&M/service visibility make it the cleanest C04 positive-control among the group.

## 5. Representative trigger rows JSONL

```jsonl
{"symbol": "457550", "name": "우진엔텍", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "CZECH_DUKOVANY_REHEATED_SUPPLIER_SPIKE_WITHOUT_LISTED_CASH_BRIDGE", "trigger_type": "Stage2-Watch", "entry_date": "2024-07-18", "entry_close": 31500, "high_30d": 41600, "low_30d": 15490, "high_90d": 41600, "low_90d": 13150, "high_180d": 41600, "low_180d": 13150, "route": "counterexample", "note": "new C04 symbol; intraday/new-nuclear-supplier spike with no named listed-company contract scope", "mfe_30d_pct": 32.06, "mae_30d_pct": -50.83, "mfe_90d_pct": 32.06, "mae_90d_pct": -58.25, "mfe_180d_pct": 32.06, "mae_180d_pct": -58.25, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true}
{"symbol": "032820", "name": "우리기술", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "SMALL_NUCLEAR_CONTROL_SUPPLIER_REHEATED_THEME_SPIKE", "trigger_type": "Stage2-Watch", "entry_date": "2024-09-12", "entry_close": 2335, "high_30d": 2650, "low_30d": 2040, "high_90d": 2650, "low_90d": 1632, "high_180d": 2650, "low_180d": 1453, "route": "counterexample", "note": "same symbol as prior session but new entry_date/trigger family; supplier theme re-spike faded without final contract/cash bridge", "mfe_30d_pct": 13.49, "mae_30d_pct": -12.63, "mfe_90d_pct": 13.49, "mae_90d_pct": -30.11, "mfe_180d_pct": 13.49, "mae_180d_pct": -37.77, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true}
{"symbol": "105840", "name": "우진", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_INSTRUMENTATION_SUPPLIER_THEME_LOW_MFE_HIGH_MAE", "trigger_type": "Stage2-Watch", "entry_date": "2024-09-12", "entry_close": 8130, "high_30d": 8330, "low_30d": 7580, "high_90d": 8870, "low_90d": 5630, "high_180d": 8870, "low_180d": 5630, "route": "counterexample", "note": "instrumentation vocabulary did not create durable price-return alignment", "mfe_30d_pct": 2.46, "mae_30d_pct": -6.77, "mfe_90d_pct": 9.1, "mae_90d_pct": -30.75, "mfe_180d_pct": 9.1, "mae_180d_pct": -30.75, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true}
{"symbol": "006910", "name": "보성파워텍", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "GRID_NUCLEAR_SUPPLIER_THEME_SPIKE_HIGH_MAE", "trigger_type": "Stage2-Watch", "entry_date": "2024-09-12", "entry_close": 3580, "high_30d": 3885, "low_30d": 3145, "high_90d": 3885, "low_90d": 2290, "high_180d": 3885, "low_180d": 2270, "route": "counterexample", "note": "grid/nuclear supplier label faded without listed-company scope/cash bridge", "mfe_30d_pct": 8.52, "mae_30d_pct": -12.15, "mfe_90d_pct": 8.52, "mae_90d_pct": -36.03, "mfe_180d_pct": 8.52, "mae_180d_pct": -36.59, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true}
{"symbol": "051600", "name": "한전KPS", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_SERVICE_OM_SCOPE_LOW_MAE_ESCAPE_HATCH_RETEST", "trigger_type": "Stage2-Actionable", "entry_date": "2024-09-12", "entry_close": 42150, "high_30d": 48250, "low_30d": 40300, "high_90d": 49100, "low_90d": 40300, "high_180d": 49100, "low_180d": 38000, "route": "positive_control", "note": "reused symbol with new entry_date; O&M/service visibility preserved low-MAE escape hatch", "mfe_30d_pct": 14.47, "mae_30d_pct": -4.39, "mfe_90d_pct": 16.49, "mae_90d_pct": -4.39, "mfe_180d_pct": 16.49, "mae_180d_pct": -9.85, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true}
```

## 6. Current calibrated profile stress test

Current calibrated profile behavior under this loop:

```text
Problem:
    C04 still overreacts to supplier-theme vocabulary when a nuclear preferred-bidder/policy headline is present.

Observed errors:
    - 457550: intraday spike looked actionable, but 90D/180D MAE was too deep.
    - 032820: reheated supplier theme did not convert into durable price-return alignment.
    - 105840: instrumentation/nuclear vocabulary did not provide a listed-company cash bridge.
    - 006910: grid/nuclear supplier label faded without final scope.

Validated escape:
    - 051600: O&M / service visibility and low-MAE profile should avoid a blanket C04 hard block.
```

## 7. Raw component score breakdown proposal

```json
{
  "rule_candidate": "C04_REHEATED_SUPPLIER_THEME_STAGE2_CAP",
  "eps_revision_bridge": 0,
  "visibility": 6,
  "bottleneck_specificity": 4,
  "mispricing": 4,
  "validation": 3,
  "capital_return": 0,
  "information_edge": 8,
  "stage2_actionable_bonus_default": 0,
  "escape_hatch": "named_final_contract_or_OM_service_cash_bridge_with_low_MAE"
}
```

## 8. Proposed rule candidate

```text
if canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
and nuclear_policy_or_preferred_bidder_headline == true
and final_contract_signed_or_legal_clearance == false
and listed_company_named_scope_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
and supplier_theme_reheated_spike == true
and MFE_30D_pct < +15
and MAE_90D_pct <= -25:
    Stage2_FalsePositive_Block = true
```

```text
escape_hatch:
if named_OM_service_scope_or_contract_cash_bridge == true
and MAE_90D_pct > -15:
    keep_stage2_watch_or_actionable = true
    do_not_apply_blanket_supplier_theme_block = true
```

## 9. Residual contribution summary

```yaml
new_independent_case_count: 5
reused_symbol_count: 4
new_visible_C04_symbol_count: 1
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 1
counterexample_count: 4
current_profile_error_count: 4
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C04_REHEATED_SUPPLIER_THEME_STAGE2_CAP
existing_axis_strengthened:
  - C04_final_contract_legal_clearance_requirement
  - C04_supplier_theme_stage2_block_without_listed_company_cash_bridge
  - C04_reheated_supplier_theme_low_MFE_high_MAE_false_positive_block
  - C04_OM_service_low_MAE_escape_hatch
next_recommended_archetypes:
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

## 10. Handoff note

This MD is intended as a calibration artifact only. It does not change production scoring. Any weight impact should remain shadow-only until aggregated with additional C04 loops and R13 cross-archetype checks.
