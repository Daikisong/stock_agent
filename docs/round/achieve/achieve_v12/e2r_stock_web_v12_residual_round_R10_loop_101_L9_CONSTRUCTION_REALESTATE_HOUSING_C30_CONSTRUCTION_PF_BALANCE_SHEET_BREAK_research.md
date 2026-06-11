# stock-web v12 residual calibration — R10 loop 101 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R10
selected_loop: 101
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: BUILDER_PF_LIQUIDITY_SUPPORT_BALANCE_SHEET_REPAIR_VS_GENERIC_BUILDER_VALUE_TRAP
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
generated_at_kst: 2026-06-07
```

## 0. selection / no-repeat rationale

Repository index snapshot still shows `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` at only `3 rows / 3 symbols` with visible covered symbols `009410`, `034300`, `183190`. A prior local run filled `R10 / loop 100` with `000720`, `002990`, `047040`. This loop therefore uses a fresh second-pass C30 set:

- `006360` GS건설
- `294870` HDC현대산업개발
- `375500` DL이앤씨

The goal is not generic construction-sector exposure. The goal is to distinguish:

1. **builder PF/liquidity support + balance-sheet repair path**, where Stage2 can survive,
2. **developer survivor rebound with later overhang**, where 4B watch is required,
3. **generic builder/value-trap label**, where Stage2 should be blocked when cash/margin repair is absent.

## 1. macro / policy background

South Korea’s real-estate PF stress was not a simple price headline. Reuters reported that the government prepared financial support for small businesses and builders hurt by high rates, including liquidity support, expanded guarantees, extra loans, and market-stabilization support for profitable real-estate projects. Reuters also reported that regulators tightened real-estate project assessments from June 2024 to accelerate restructuring, after PF delinquency rates rose sharply.

This means C30 should **not** reward the word “construction” by itself. It should reward only the case where the policy/liquidity action plausibly flows into survivable projects, refinancing capacity, cash conversion, and balance-sheet repair.

## 2. case matrix

| case_id | symbol | company | role | trigger_date | entry_close | fwd_high | fwd_low | MFE | MAE | label |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| C30_R10L101_01 | 006360 | GS건설 | builder liquidity / repair positive | 2024-04-03 | 15,630 | 21,750 | 14,870 | +39.16% | -4.86% | positive |
| C30_R10L101_02 | 294870 | HDC현대산업개발 | developer survivor rebound, high-MAE watch | 2024-07-26 | 21,550 | 28,200 | 17,200 | +30.86% | -20.19% | positive_watch |
| C30_R10L101_03 | 375500 | DL이앤씨 | generic builder/value-trap false positive | 2024-01-30 | 41,850 | 43,800 | 28,600 | +4.66% | -31.66% | counterexample |

## 3. case notes

### 3.1 GS건설 / 006360 — liquidity support + repair path positive

**Thesis tested:** C30 should allow Stage2 when the broad builder-liquidity support backdrop is joined by a price path that shows repair, not merely one-day PF panic relief.

- Entry: `2024-04-03 close 15,630`.
- Forward high: `2024-08-27 high 21,750`.
- Observed low: `2024-04-08 low 14,870`.
- MFE: `(21750 - 15630) / 15630 = +39.16%`.
- MAE: `(14870 - 15630) / 15630 = -4.86%`.

Interpretation: This is the cleanest positive of this loop. It is not “all builders are buys.” It is a case where a builder stock reacted to liquidity / balance-sheet repair conditions and then sustained a multi-month MFE while avoiding deep early drawdown. C30 can preserve Stage2 if non-price evidence shows refinancing/project liquidity relief and the price path does not immediately fail.

### 3.2 HDC현대산업개발 / 294870 — survivor rebound but later 4B watch

**Thesis tested:** Developer survivor rebounds can produce large MFE, but C30 should not auto-Green them if legal/safety/overhang or PF-quality concerns remain.

- Entry: `2024-07-26 close 21,550`.
- Forward high: `2024-08-26 high 28,200`.
- Forward low: `2024-12-09 low 17,200`.
- MFE: `(28200 - 21550) / 21550 = +30.86%`.
- MAE: `(17200 - 21550) / 21550 = -20.19%`.

Interpretation: This is a positive-with-watch. The stock produced a strong survivor rebound, but later drawdown shows why C30 needs a `local_4B_watch` after vertical MFE unless balance-sheet repair, project cash conversion, and overhang resolution are refreshed.

### 3.3 DL이앤씨 / 375500 — generic builder/value-trap false positive

**Thesis tested:** Low valuation, construction label, or sector-liquidity headlines are not enough if the company-specific margin/cash/PF bridge is absent.

- Entry: `2024-01-30 close 41,850`.
- Forward high: `2024-02-01 high 43,800`.
- Forward low: `2024-08-05 low 28,600`.
- MFE: `(43800 - 41850) / 41850 = +4.66%`.
- MAE: `(28600 - 41850) / 41850 = -31.66%`.

Interpretation: This is the important counterexample. C30 cannot let “builder + cheap valuation + sector support” produce Stage2-Actionable by itself. Without project-level cash conversion or margin/PF repair evidence, the path becomes low-MFE / high-MAE and should be blocked or capped.

## 4. residual rule candidate

```text
rule_id = C30_PF_BALANCE_SHEET_REPAIR_STAGE2_GATE

if canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
and trigger_type == Stage2
and (
    real_estate_PF_liquidity_support == true
    or builder_refinancing_relief == true
    or project_restructuring_soft_landing == true
)
and company_specific_balance_sheet_cash_bridge == true
and MFE_90D_pct >= +15
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
```

```text
rule_id = C30_GENERIC_BUILDER_VALUE_TRAP_BLOCK

if canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
and trigger_type == Stage2
and generic_builder_or_low_PBR_label == true
and company_specific_balance_sheet_cash_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
    block_stage3_green = true
```

```text
rule_id = C30_VERTICAL_SURVIVOR_REBOUND_4B_WATCH

if canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
and MFE_30D_pct >= +25
and refreshed_project_cash_or_overhang_resolution == false:
    local_4B_watch = true
    do_not_open_green_until_bridge_refresh = true
```

## 5. trigger rows

```jsonl
{"row_type":"trigger","case_id":"C30_R10L101_01","symbol":"006360","name":"GS건설","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"BUILDER_PF_LIQUIDITY_SUPPORT_BALANCE_SHEET_REPAIR","entry_date":"2024-04-03","entry_close":15630,"fwd_high":21750,"fwd_high_date":"2024-08-27","fwd_low":14870,"fwd_low_date":"2024-04-08","mfe_pct":39.16,"mae_pct":-4.86,"trigger_label":"positive","calibration_usable":true,"rule_contribution":"C30_PF_BALANCE_SHEET_REPAIR_STAGE2_GATE"}
{"row_type":"trigger","case_id":"C30_R10L101_02","symbol":"294870","name":"HDC현대산업개발","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DEVELOPER_SURVIVOR_REBOUND_WITH_OVERHANG_4B_WATCH","entry_date":"2024-07-26","entry_close":21550,"fwd_high":28200,"fwd_high_date":"2024-08-26","fwd_low":17200,"fwd_low_date":"2024-12-09","mfe_pct":30.86,"mae_pct":-20.19,"trigger_label":"positive_watch","calibration_usable":true,"rule_contribution":"C30_VERTICAL_SURVIVOR_REBOUND_4B_WATCH"}
{"row_type":"trigger","case_id":"C30_R10L101_03","symbol":"375500","name":"DL이앤씨","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"GENERIC_BUILDER_LOW_PBR_VALUE_TRAP_FALSE_STAGE2","entry_date":"2024-01-30","entry_close":41850,"fwd_high":43800,"fwd_high_date":"2024-02-01","fwd_low":28600,"fwd_low_date":"2024-08-05","mfe_pct":4.66,"mae_pct":-31.66,"trigger_label":"counterexample","calibration_usable":true,"rule_contribution":"C30_GENERIC_BUILDER_VALUE_TRAP_BLOCK"}
```

## 6. loop contribution summary

```yaml
new_independent_case_count: 3
same_archetype_new_symbol_count_visible_index_basis: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
existing_axis_strengthened:
  - C30_company_specific_balance_sheet_cash_bridge_requirement
  - C30_generic_builder_low_PBR_stage2_block
  - C30_vertical_survivor_rebound_local_4B_watch
existing_axis_weakened: []
do_not_propose_new_weight_delta: false
next_recommended_archetypes:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
