# E2R V12 No-Repeat Standalone Residual Research
## R9 / L3 / C29 — Mobility volume and margin operating leverage guard

metadata:
```text
selected_round: R9
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_LOGISTICS_VOLUME_MIX_MARGIN_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_auto_parts_logistics_margin_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE current coverage:
rows=36, symbols=15, date range=2020-08-14~2024-09-09, good/bad S2=10/7, 4B/4C=4/2
top covered symbols: 000270(10), 204320(6), 011210(5), 005380(4), 003490(1)
```

This run avoids the repeated top C29 symbols and adds 086280, 012330, and 018880.  
Each row uses a new `C29 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
086280 현대글로비스: 2023 window clean; corporate-action candidates are in 2024.
012330 현대모비스: 2023 window clean; corporate-action candidates are old, outside the test window.
018880 한온시스템: 2023 window clean; corporate-action candidates are old or future, outside the test window.
```

## 3. Research thesis

C29 should not be a generic auto-stock momentum bucket. It should test whether volume becomes operating leverage:

```text
mobility / auto / logistics volume signal
→ mix, export, ASP, logistics rate, or parts margin evidence
→ revision bridge
→ rerating
```

The residual failure mode is that a volume story can be loud while margin leverage stays silent. In that case, the price path may give a brief Stage2 signal, but Green is too loose.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C29_086280_GLOVIS_20230425_AUTO_LOGISTICS_VOLUME_MARGIN_LEVERAGE | 086280 | positive_operating_leverage_success | 2023-04-25 | 168100 | 203000 on 2023-07-05 | 160500 on 2023-05-16 | 8.03% | 20.76% | 20.76% | -4.52% | -19.8% |
| C29_012330_MOBIS_20230214_AUTO_PARTS_VOLUME_MARGIN_STAGE2 | 012330 | positive_stage2_but_green_requires_mix_margin | 2023-02-14 | 213000 | 250000 on 2023-07-17 | 207500 on 2023-10-31 | 4.23% | 11.5% | 17.37% | -2.58% | -17.0% |
| C29_018880_HANON_20230510_THERMAL_EV_VOLUME_MARGIN_FALSE_GREEN | 018880 | false_green_counterexample | 2023-05-10 | 9730 | 10170 on 2023-05-10 | 6710 on 2023-12-07 | 4.52% | 4.52% | 4.52% | -31.04% | -34.02% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Auto/logistics volume and export attention can create a valid Stage2 route.
- 086280 and 012330 show positive Stage2 behavior when volume/mix operating leverage is plausible.

### Stage3 / Green
- C29 Green should require mix, margin, revision, and cash-flow confirmation.
- A supplier or logistics stock should not inherit Green simply because OEM volume is strong.

### 4B
- 086280 and 012330 both show that after the price path validates the theme, later drawdown still requires watch discipline.
- C29 should distinguish healthy Stage2 from late volume-beta extrapolation.

### 4C
- 018880 is the core counterexample: EV/thermal volume language without margin/cash-flow leverage can fade hard.
- The break mode is not simply lower volume; it is the failure of volume to transmit into margin and cash flow.

## 6. Raw component score breakdown

```json
{
  "C29_012330_MOBIS_20230214_AUTO_PARTS_VOLUME_MARGIN_STAGE2": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 3,
    "eps_fcf_explosion": 9,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 53,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  },
  "C29_018880_HANON_20230510_THERMAL_EV_VOLUME_MARGIN_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 29,
    "valuation_rerating_runway": 4,
    "visibility_quality": 5
  },
  "C29_086280_GLOVIS_20230425_AUTO_LOGISTICS_VOLUME_MARGIN_LEVERAGE": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 58,
    "valuation_rerating_runway": 10,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C29 guard:
```text
if mobility_volume_signal and no mix_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if supplier_volume_story and margin_cashflow_leverage_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 018880 / 2023-05-10: EV thermal/volume story could be over-promoted if C29 treats volume as operating leverage without margin/cash-flow evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -4.52, "MAE_30D_pct": -4.52, "MAE_90D_pct": -4.52, "MFE_180D_pct": 20.76, "MFE_30D_pct": 8.03, "MFE_90D_pct": 20.76, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_086280_GLOVIS_20230425_AUTO_LOGISTICS_VOLUME_MARGIN_LEVERAGE", "case_role": "positive_operating_leverage_success", "company_name": "현대글로비스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when auto export/logistics volume and margin leverage improved; Green still requires volume/mix/margin confirmation, not just sector beta.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -19.8, "entry_date": "2023-04-25", "entry_price": 168100, "evidence_family": "auto_export_logistics_volume_margin_operating_leverage", "evidence_url_pending": false, "fine_archetype_id": "AUTO_PARTS_LOGISTICS_VOLUME_MIX_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-05-16", "low_price_180d": 160500, "peak_date": "2023-07-05", "peak_price": 203000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/086/086280.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 58, "valuation_rerating_runway": 10, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C29_086280_GLOVIS_20230425_AUTO_LOGISTICS_VOLUME_MARGIN_LEVERAGE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["auto_or_mobility_volume_attention", "mix_or_export_or_logistics_operating_leverage_claim", "relative_strength"], "stage3_evidence_fields": ["volume_mix_margin_confirmation_required", "revision_bridge_required", "cashflow_or_balance_sheet_quality_required"], "stage4b_evidence_fields": ["late_volume_beta_after_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["margin_leverage_failure", "working_capital_or_cashflow_gap", "customer_mix_or_volume_fade"], "symbol": "086280", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv", "trigger_date": "2023-04-25", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -2.58, "MAE_30D_pct": -1.41, "MAE_90D_pct": -1.41, "MFE_180D_pct": 17.37, "MFE_30D_pct": 4.23, "MFE_90D_pct": 11.5, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_012330_MOBIS_20230214_AUTO_PARTS_VOLUME_MARGIN_STAGE2", "case_role": "positive_stage2_but_green_requires_mix_margin", "company_name": "현대모비스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 attention was valid, but Green should wait for mix, AS margin, electrification-margin, and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -17.0, "entry_date": "2023-02-14", "entry_price": 213000, "evidence_family": "auto_parts_volume_mix_margin_operating_leverage", "evidence_url_pending": false, "fine_archetype_id": "AUTO_PARTS_LOGISTICS_VOLUME_MIX_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-31", "low_price_180d": 207500, "peak_date": "2023-07-17", "peak_price": 250000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/012/012330.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 3, "eps_fcf_explosion": 9, "information_confidence": 4, "market_mispricing": 10, "total": 53, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C29_012330_MOBIS_20230214_AUTO_PARTS_VOLUME_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["auto_or_mobility_volume_attention", "mix_or_export_or_logistics_operating_leverage_claim", "relative_strength"], "stage3_evidence_fields": ["volume_mix_margin_confirmation_required", "revision_bridge_required", "cashflow_or_balance_sheet_quality_required"], "stage4b_evidence_fields": ["late_volume_beta_after_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["margin_leverage_failure", "working_capital_or_cashflow_gap", "customer_mix_or_volume_fade"], "symbol": "012330", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012330/2023.csv", "trigger_date": "2023-02-14", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -31.04, "MAE_30D_pct": -6.27, "MAE_90D_pct": -9.46, "MFE_180D_pct": 4.52, "MFE_30D_pct": 4.52, "MFE_90D_pct": 4.52, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_018880_HANON_20230510_THERMAL_EV_VOLUME_MARGIN_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "한온시스템", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "EV thermal/volume narrative should not become Green without margin recovery and balance-sheet/cash-flow evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.02, "entry_date": "2023-05-10", "entry_price": 9730, "evidence_family": "thermal_ev_volume_story_without_margin_cashflow_leverage", "evidence_url_pending": false, "fine_archetype_id": "AUTO_PARTS_LOGISTICS_VOLUME_MIX_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-12-07", "low_price_180d": 6710, "peak_date": "2023-05-10", "peak_price": 10170, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/018/018880.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 29, "valuation_rerating_runway": 4, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C29_018880_HANON_20230510_THERMAL_EV_VOLUME_MARGIN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["auto_or_mobility_volume_attention", "mix_or_export_or_logistics_operating_leverage_claim", "relative_strength"], "stage3_evidence_fields": ["volume_mix_margin_confirmation_required", "revision_bridge_required", "cashflow_or_balance_sheet_quality_required"], "stage4b_evidence_fields": ["late_volume_beta_after_price_run", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["margin_leverage_failure", "working_capital_or_cashflow_gap", "customer_mix_or_volume_fade"], "symbol": "018880", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv", "trigger_date": "2023-05-10", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "AUTO_PARTS_LOGISTICS_VOLUME_MIX_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "mobility_volume_margin_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R9",
  "shadow_rule_candidate": "C29 mobility volume/margin rerating should permit Stage2 on volume/export/logistics attention, but Stage3 Green requires confirmed mix/margin/revision/cash-flow leverage; EV/thermal volume stories without margin evidence should stay Yellow or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C29 + symbol + trigger_type + entry_date.
3. Add C29-specific volume-to-margin bridge logic only as a shadow candidate until more rows exist.

Candidate rule:
- C29_MOBILITY_GREEN_REQUIRES_VOLUME_MIX_MARGIN_REVISION
- C29_SUPPLIER_VOLUME_WITHOUT_MARGIN_STAGE2_CAP
- C29_THERMAL_EV_VOLUME_FALSE_GREEN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

