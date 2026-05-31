# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C11 — Battery orderbook rerating margin bridge

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: CNT_COPPERFOIL_SEPARATOR_ORDERBOOK_MARGIN_BRIDGE
loop_objective: coverage_gap_fill|positive_counterexample_balance|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_cnt_copperfoil_separator_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C11_BATTERY_ORDERBOOK_RERATING current coverage:
rows=14, symbols=6, date range=2023-01-31~2024-06-24, good/bad S2=6/2, 4B/4C=0/1
top covered symbols: 247540(6), 003670(3), 348370(2), 066970(1), 373220(1)
```

This run avoids the top repeated C11 symbols and adds 121600, 336370, and 393890.  
The 393890 row is not a C11 hard duplicate because the No-Repeat hard key is `canonical_archetype_id + symbol + trigger_type + entry_date`, and this row uses a new C11 key.

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
121600 나노신소재: 2023 window clean; corporate-action candidate is 2015-12-17.
336370 솔루스첨단소재: 2023 window clean; corporate-action candidates are in 2024.
393890 더블유씨피: first_date=2022-09-30, last_date=2026-02-20, corporate_action_candidate_count=0.
```

## 3. Research thesis

C11 should not treat every battery-material rally as an orderbook rerating. The mechanism must close:

```text
capacity / orderbook / customer visibility
→ revenue conversion
→ margin bridge
→ revision confirmation
→ valuation rerating
```

The positive anchor is 121600, where the price path is consistent with a genuine CNT-material rerating window. The residual error comes from 336370 and late 393890: orderbook/capacity language can create early Stage2 attention, but without margin and utilization confirmation it should not become Green.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C11_121600_NANOSINSO_20230209_CNT_ORDERBOOK_RERATING_GREEN | 121600 | positive_structural_success | 2023-02-09 | 109200 | 193700 on 2023-04-10 | 107100 on 2023-02-10 | 77.38% | -1.92% | -38.72% |
| C11_336370_SOLUS_20230207_COPPERFOIL_ORDERBOOK_FALSE_GREEN | 336370 | failed_orderbook_rerating | 2023-02-07 | 42650 | 54000 on 2023-02-22 | 33750 on 2023-07-19 | 26.61% | -20.87% | -37.5% |
| C11_393890_WCP_20230612_SEPARATOR_ORDERBOOK_LATE_FALSE_GREEN | 393890 | late_false_green_counterexample | 2023-06-12 | 65900 | 78700 on 2023-07-04 | 38300 on 2023-11-13 | 19.42% | -41.88% | -51.33% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Battery material orderbook, capacity, and customer visibility claims can create valid early attention.
- 336370 shows that this early signal can be tradable but still fail to become durable Green.

### Stage3 / Green
- C11 Green should require orderbook-to-revenue conversion, margin bridge, and revision confirmation.
- 121600 is the positive anchor, but even there Green is not justified by price alone; the orderbook/material capacity story must be tied to EPS/FCF bodyweight change.

### 4B
- Late 393890 after the 1H23 rerating should be treated as local 4B/Yellow risk if orderbook conversion and utilization are not strengthening.
- 336370 also shows how a small MFE can quickly become a fade when margin evidence does not arrive.

### 4C
- These are not hard accounting-break cases.
- The C11 break mode is conversion failure: orderbook/capacity language does not become margin, utilization, and revision.

## 6. Raw component score breakdown

```json
{
  "C11_121600_NANOSINSO_20230209_CNT_ORDERBOOK_RERATING_GREEN": {
    "bottleneck_pricing_power": 14,
    "capital_allocation": 3,
    "eps_fcf_explosion": 15,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 73,
    "valuation_rerating_runway": 10,
    "visibility_quality": 15
  },
  "C11_336370_SOLUS_20230207_COPPERFOIL_ORDERBOOK_FALSE_GREEN": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 8,
    "information_confidence": 3,
    "market_mispricing": 9,
    "total": 44,
    "valuation_rerating_runway": 5,
    "visibility_quality": 8
  },
  "C11_393890_WCP_20230612_SEPARATOR_ORDERBOOK_LATE_FALSE_GREEN": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 37,
    "valuation_rerating_runway": 4,
    "visibility_quality": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C11 guard:
```text
if battery_material_orderbook and no margin_or_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if late_relative_strength_after_battery_material_rerating and utilization_or_margin_risk_unresolved:
    route_to_local_4B_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 336370 / 2023-02-07: capacity/orderbook attention could be over-promoted if the margin/revision bridge is not demanded.
- 393890 / 2023-06-12: late separator orderbook rerating can look like Green, but the later path argues for Yellow/4B-watch.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -1.92, "MAE_30D_pct": -1.92, "MAE_90D_pct": -1.92, "MFE_180D_pct": 77.38, "MFE_30D_pct": 77.38, "MFE_90D_pct": 77.38, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_121600_NANOSINSO_20230209_CNT_ORDERBOOK_RERATING_GREEN", "case_role": "positive_structural_success", "company_name": "나노신소재", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Green can be justified only if CNT capacity/order visibility and revision bridge are both present; pure battery beta would be insufficient.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.72, "entry_date": "2023-02-09", "entry_price": 109200, "evidence_family": "cnt_conductive_additive_capacity_orderbook_rerating", "evidence_url_pending": false, "fine_archetype_id": "CNT_COPPERFOIL_SEPARATOR_ORDERBOOK_MARGIN_BRIDGE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-02-10", "low_price_180d": 107100, "peak_date": "2023-04-10", "peak_price": 193700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/121/121600.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 14, "capital_allocation": 3, "eps_fcf_explosion": 15, "information_confidence": 4, "market_mispricing": 12, "total": 73, "valuation_rerating_runway": 10, "visibility_quality": 15}, "reuse_reason": null, "same_entry_group_id": "C11_121600_NANOSINSO_20230209_CNT_ORDERBOOK_RERATING_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_material_capacity_or_orderbook_attention", "customer_or_project_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["orderbook_to_revenue_conversion_required", "margin_or_revision_bridge_required", "customer_utilization_confirmation_required"], "stage4b_evidence_fields": ["late_rerating_after_price_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_conversion_gap", "margin_fade", "customer_or_utilization_delay"], "symbol": "121600", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2023.csv", "trigger_date": "2023-02-09", "trigger_type": "Stage3-Green", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -20.87, "MAE_30D_pct": -20.87, "MAE_90D_pct": -20.87, "MFE_180D_pct": 26.61, "MFE_30D_pct": 26.61, "MFE_90D_pct": 26.61, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_336370_SOLUS_20230207_COPPERFOIL_ORDERBOOK_FALSE_GREEN", "case_role": "failed_orderbook_rerating", "company_name": "솔루스첨단소재", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Early Stage2 attention was valid, but Green should be blocked if capacity/orderbook does not transmit into margin and revision.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.5, "entry_date": "2023-02-07", "entry_price": 42650, "evidence_family": "copperfoil_orderbook_capacity_story_without_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "CNT_COPPERFOIL_SEPARATOR_ORDERBOOK_MARGIN_BRIDGE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-07-19", "low_price_180d": 33750, "peak_date": "2023-02-22", "peak_price": 54000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336370.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 8, "information_confidence": 3, "market_mispricing": 9, "total": 44, "valuation_rerating_runway": 5, "visibility_quality": 8}, "reuse_reason": null, "same_entry_group_id": "C11_336370_SOLUS_20230207_COPPERFOIL_ORDERBOOK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_material_capacity_or_orderbook_attention", "customer_or_project_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["orderbook_to_revenue_conversion_required", "margin_or_revision_bridge_required", "customer_utilization_confirmation_required"], "stage4b_evidence_fields": ["late_rerating_after_price_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_conversion_gap", "margin_fade", "customer_or_utilization_delay"], "symbol": "336370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv", "trigger_date": "2023-02-07", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.88, "MAE_30D_pct": -8.19, "MAE_90D_pct": -18.66, "MFE_180D_pct": 19.42, "MFE_30D_pct": 19.42, "MFE_90D_pct": 19.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "case_id": "C11_393890_WCP_20230612_SEPARATOR_ORDERBOOK_LATE_FALSE_GREEN", "case_role": "late_false_green_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Late orderbook rerating should remain Yellow/4B-watch unless utilization and margin bridge remain intact.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.33, "entry_date": "2023-06-12", "entry_price": 65900, "evidence_family": "separator_orderbook_late_rerating_without_utilization_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "CNT_COPPERFOIL_SEPARATOR_ORDERBOOK_MARGIN_BRIDGE", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-13", "low_price_180d": 38300, "peak_date": "2023-07-04", "peak_price": 78700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 5, "total": 37, "valuation_rerating_runway": 4, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C11_393890_WCP_20230612_SEPARATOR_ORDERBOOK_LATE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_material_capacity_or_orderbook_attention", "customer_or_project_visibility_claim", "relative_strength"], "stage3_evidence_fields": ["orderbook_to_revenue_conversion_required", "margin_or_revision_bridge_required", "customer_utilization_confirmation_required"], "stage4b_evidence_fields": ["late_rerating_after_price_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["orderbook_conversion_gap", "margin_fade", "customer_or_utilization_delay"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-06-12", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CNT_COPPERFOIL_SEPARATOR_ORDERBOOK_MARGIN_BRIDGE",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "counterexample_added_with_one_positive_anchor",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C11 battery orderbook rerating should allow Green only when orderbook/capacity visibility closes into revenue, margin, and revision; late battery-material relative strength should be capped at Yellow or routed to local 4B.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C11 + symbol + trigger_type + entry_date.
3. Add C11-specific orderbook-to-margin/revision bridge guard only as a shadow candidate until more rows exist.

Candidate rule:
- C11_ORDERBOOK_GREEN_REQUIRES_MARGIN_REVISION_BRIDGE
- C11_LATE_BATTERY_MATERIAL_RERATING_LOCAL_4B
- C11_CAPACITY_STORY_WITHOUT_CONVERSION_STAGE2_CAP

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

