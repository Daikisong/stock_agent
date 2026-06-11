# E2R stock-web v12 residual research — R9 / loop 101 / C29 mobility volume-margin operating leverage

```text
completed_round = R9
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 1. Run metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R9
selected_loop: 101
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_MODULE_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_LABEL_LOW_MFE_HIGH_MAE
output_filename: e2r_stock_web_v12_residual_round_R9_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 2. Selection rationale

`C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` remains a thin canonical bucket in the repository index.  
The visible index snapshot shows only 3 rows / 3 symbols for C29, concentrated in prior complete-vehicle or mobility-label cases.  
This loop therefore avoids the previous local C29 first pass symbols and adds three fresh C29 visible-basis symbols:

- `012330` 현대모비스
- `086280` 현대글로비스
- `011210` 현대위아

The objective is not to prove that “auto/mobility” works. The objective is to separate:

```text
durable company-specific volume/mix/margin bridge
vs
generic auto-parts / mobility / machine-tool vocabulary
```

## 3. Price source validation

The price atlas is `Songdaiki/stock-web`, generated from `FinanceData/marcap`, with calibration shards under:

```text
atlas/ohlcv_tradable_by_symbol_year
```

Manifest constraints used in this MD:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
price_basis = tradable_raw
max_date = 2026-02-20
```

All three trigger rows below use actual stock-web 1D OHLC rows.  
No post-manifest price is invented.

## 4. Case design

### 4.1 Positive-control: 012330 현대모비스

`현대모비스` is a better C29 case than a generic finished-car beta because the bridge is not simply “Hyundai/Kia sold cars.”  
The desired C29 bridge is:

```text
module/core-parts volume
+ after-service parts margin
+ mix/operating leverage
+ company-specific profitability visibility
```

Selected trigger:

```text
symbol = 012330
trigger_type = Stage2
trigger_date = 2024-10-16
entry_date = 2024-10-16
entry_price = 241500
```

Observed forward path:

```text
30D high = 267000
30D low  = 235000
90D high = 268500
90D low  = 235000
180D high = 289000
180D low  = 233000
```

Interpretation:

```text
case_label = positive_control
profile_verdict = current_profile_ok_but_requires_volume_mix_margin_bridge
```

This case supports allowing C29 Stage2 only when the auto-parts bridge is visible at the company level.  
It should not loosen C29 for generic auto-component nouns.

### 4.2 Positive-with-watch: 086280 현대글로비스

`현대글로비스` is a C29-adjacent logistics case.  
The useful bridge is:

```text
finished-vehicle logistics / PCC shipping volume
+ group vehicle export/logistics flow
+ logistics margin bridge
```

It is not a pure OEM sales-volume case and not a generic transport label.

Selected trigger:

```text
symbol = 086280
trigger_type = Stage2
trigger_date = 2024-10-16
entry_date = 2024-10-16
entry_price = 123900
```

Observed forward path:

```text
30D high = 127400
30D low  = 112100
90D high = 151000
90D low  = 111600
180D high = 151000
180D low  = 105000
```

Interpretation:

```text
case_label = positive_with_high_MAE_watch
profile_verdict = current_profile_partially_ok_but_needs_corporate_action_boundary_and_logistics_margin_bridge
```

Important caveat:

`stock-web` flags 2024-07-12 and 2024-08-02 as corporate-action candidate dates for `086280`.  
This MD uses a 2024-10-16 entry, after the contaminated boundary, so the selected forward window is retained as calibration-usable.  
However, this case strengthens the rule that C29 logistics positive rows require clean price-window validation.

### 4.3 Counterexample: 011210 현대위아

`현대위아` is the guardrail case.  
It has mobility-adjacent vocabulary:

```text
automotive engines/modules
CV joints
four-wheel drive systems
machine tools
```

But the 2024 path shows that generic auto-parts wording without durable margin/revision/cash evidence can become a low-MFE/high-MAE Stage2 false positive.

Selected trigger:

```text
symbol = 011210
trigger_type = Stage2
trigger_date = 2024-09-13
entry_date = 2024-09-13
entry_price = 51600
```

Observed forward path:

```text
30D high = 53800
30D low  = 47150
90D high = 53800
90D low  = 37050
180D high = 53800
180D low  = 36900
```

Interpretation:

```text
case_label = counterexample
profile_verdict = current_profile_error_if_generic_parts_label_receives_stage2_actionable_bonus
```

This is the main rule contribution of the loop.

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R9", "selected_loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_LABEL_LOW_MFE_HIGH_MAE", "symbol": "012330", "company_name": "현대모비스", "trigger_type": "Stage2", "trigger_date": "2024-10-16", "entry_date": "2024-10-16", "entry_price": 241500.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 10.56, "MAE_30D_pct": -2.69, "MFE_90D_pct": 11.18, "MAE_90D_pct": -2.69, "MFE_180D_pct": 19.67, "MAE_180D_pct": -3.52, "forward_window_complete_asof_manifest": true, "calibration_usable": true, "case_label": "positive_control", "profile_verdict": "current_profile_ok_but_requires_volume_mix_margin_bridge", "evidence_family": "module_core_parts_afterservice_margin_bridge", "non_price_bridge": "auto parts/modules + A/S profitability + future mobility parts; not pure completed-vehicle beta", "guardrail_note": "keep Stage2 only when margin/revision bridge is company-specific"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R9", "selected_loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_LABEL_LOW_MFE_HIGH_MAE", "symbol": "086280", "company_name": "현대글로비스", "trigger_type": "Stage2", "trigger_date": "2024-10-16", "entry_date": "2024-10-16", "entry_price": 123900.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 2.82, "MAE_30D_pct": -9.52, "MFE_90D_pct": 21.87, "MAE_90D_pct": -9.93, "MFE_180D_pct": 21.87, "MAE_180D_pct": -15.25, "forward_window_complete_asof_manifest": true, "calibration_usable": true, "case_label": "positive_with_high_MAE_watch", "profile_verdict": "current_profile_partially_ok_but_needs_corporate_action_boundary_and_logistics_margin_bridge", "evidence_family": "finished_vehicle_logistics_pcc_volume_margin_bridge", "non_price_bridge": "finished vehicle logistics/shipping leverage plus auto volume mix, but not a pure auto OEM rerating", "guardrail_note": "entry after stock-web corporate-action candidate boundary; local 4B watch if logistics margin bridge fades"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R9", "selected_loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_LABEL_LOW_MFE_HIGH_MAE", "symbol": "011210", "company_name": "현대위아", "trigger_type": "Stage2", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 51600.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 4.26, "MAE_30D_pct": -8.62, "MFE_90D_pct": 4.26, "MAE_90D_pct": -28.2, "MFE_180D_pct": 4.26, "MAE_180D_pct": -28.49, "forward_window_complete_asof_manifest": true, "calibration_usable": true, "case_label": "counterexample", "profile_verdict": "current_profile_error_if_generic_parts_label_receives_stage2_actionable_bonus", "evidence_family": "engine_module_machine_tool_parts_label_without_margin_revisions", "non_price_bridge": "missing durable margin/revision/cash bridge despite mobility parts vocabulary", "guardrail_note": "low-MFE/high-MAE Stage2 false-positive block candidate"}
```

## 6. Score-return alignment summary

| symbol | name | case | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | alignment |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 012330 | 현대모비스 | positive_control | 241500 | 10.56 | -2.69 | 11.18 | -2.69 | 19.67 | -3.52 | Stage2 acceptable if module/parts margin bridge exists |
| 086280 | 현대글로비스 | positive_watch | 123900 | 2.82 | -9.52 | 21.87 | -9.93 | 21.87 | -15.25 | Stage2 acceptable but requires clean CA boundary and logistics margin bridge |
| 011210 | 현대위아 | counterexample | 51600 | 4.26 | -8.62 | 4.26 | -28.20 | 4.26 | -28.49 | Stage2 false-positive if generic parts/mobility label gets bonus |

## 7. Current calibrated profile stress test

The existing calibrated profile should not be changed globally.

This loop does **not** propose:

```text
C29 global positive weight increase
Stage2 bonus increase
Green threshold reduction
price-only mobility rerating allowance
```

Instead it proposes a canonical guardrail:

```text
if canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
and trigger_type == Stage2
and mobility_or_auto_parts_label == true
and company_specific_volume_mix_margin_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
    low_MFE_high_MAE_false_positive_flag = true
```

Escape hatch:

```text
if canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
and (
    module_core_parts_margin_bridge == true
    or finished_vehicle_logistics_margin_bridge == true
)
and MFE_90D_pct >= +10
and MAE_90D_pct > -15:
    allow_stage2_actionable = true
    do_not_apply_generic_parts_block = true
```

Corporate-action boundary guard:

```text
if corporate_action_candidate_inside_forward_window == true:
    calibration_usable = false
else if trigger_date > last_corporate_action_candidate_date:
    calibration_usable = true
```

## 8. Residual contribution summary

```yaml
new_independent_case_count: 3
reused_case_count_within_C29_visible_basis: 0
same_archetype_new_symbol_count_visible_index_basis: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: null
existing_axis_strengthened:
  - C29_company_specific_volume_mix_margin_bridge_requirement
  - C29_generic_auto_parts_label_stage2_block
  - C29_logistics_margin_bridge_escape_hatch
  - C29_corporate_action_boundary_validation
```

## 9. Shadow rule candidate

```yaml
rule_id: C29_VOLUME_MIX_MARGIN_BRIDGE_VS_GENERIC_PARTS_LABEL_GUARD
scope:
  large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
  canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
action:
  positive_bridge:
    require_any:
      - module_core_parts_margin_bridge
      - finished_vehicle_logistics_margin_bridge
      - model_mix_operating_leverage_bridge
      - shareholder_return_plus_margin_bridge
  block:
    condition:
      - generic_auto_parts_or_mobility_label_only
      - no_company_specific_margin_revision_cash_bridge
      - MFE_90D_pct < 10
      - MAE_90D_pct <= -20
    effect:
      stage2_actionable_bonus: 0
      max_stage: Stage2-Watch
  watch:
    condition:
      - MFE_30D_pct >= 10
      - refreshed_margin_bridge == false
    effect:
      local_4B_watch: true
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this section in this research session.

```text
You are a later coding agent applying accumulated E2R v12 research artifacts.

Input MD:
e2r_stock_web_v12_residual_round_R9_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
- Parse trigger_rows JSONL.
- Validate that all rows include price_source, price_basis, price_adjustment_status, entry_date, entry_price, MFE/MAE 30/90/180 fields.
- Do not apply global scoring changes.
- Consider a shadow-only canonical rule for C29:
  generic auto-parts or mobility label without company-specific volume/mix/margin bridge should not receive Stage2-Actionable bonus.
- Treat 086280 as calibration-usable only because the entry date is after the stock-web corporate-action candidate boundary.
- Do not patch production scoring unless multiple later C29 loops confirm the rule.
```

## 11. Next research state

```text
completed_round = R9
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C15_MATERIAL_SPREAD_SUPERCYCLE, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
