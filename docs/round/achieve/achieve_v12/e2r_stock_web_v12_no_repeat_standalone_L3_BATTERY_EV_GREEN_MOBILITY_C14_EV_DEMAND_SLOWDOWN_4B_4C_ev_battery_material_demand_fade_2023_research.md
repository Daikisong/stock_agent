# E2R V12 No-Repeat Standalone Residual Research
## R3 / L3 / C14 — EV demand slowdown 4B/4C guard

metadata:
```text
selected_round: R3
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_BATTERY_MATERIAL_DEMAND_SLOWDOWN_4B_4C_GUARD
loop_objective: counterexample_mining|4B_4C_guard_validation|green_strictness_stress_test|coverage_gap_fill
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_ev_battery_material_demand_fade_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C14_EV_DEMAND_SLOWDOWN_4B_4C current coverage:
rows=23, symbols=5, date range=2023-07-26~2024-12-20, good/bad S2=0/0, 4B/4C=3/5
top covered symbols: 066970(6), 247540(6), 003670(5), 373220(4), 006400(2)
```

This run avoids the top repeated C14 symbols and adds 121600, 336370, and 393890.  
Each row uses a new `C14 + symbol + trigger_type + entry_date` hard key.

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

C14 is the battery-cycle guardrail archetype. It asks a different question from C11/C12:

```text
has the market already capitalized the battery orderbook story?
→ is EV demand / utilization / margin revision still strengthening?
→ if not, late relative strength should become 4B/4C watch, not a fresh Green
```

The useful signal is not a new buy thesis. It is the point where the orderbook narrative becomes a brittle shell: still shiny on the outside, but hollowing out from demand and utilization.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| C14_121600_NANOSINSO_20230410_CNT_BATTERY_MATERIAL_LATE_4B_DEMAND_FADE | 121600 | protective_4b_success | 2023-04-10 | 184800 | 193700 on 2023-04-10 | 114400 on 2023-10-26 | 4.82% | -38.1% | -40.94% |
| C14_336370_SOLUS_20230222_COPPERFOIL_EV_DEMAND_SLOWDOWN_FALSE_GREEN | 336370 | false_green_counterexample | 2023-02-22 | 52200 | 54000 on 2023-02-22 | 33750 on 2023-07-19 | 3.45% | -35.34% | -37.5% |
| C14_393890_WCP_20230704_SEPARATOR_LATE_RERATING_4C_WATCH | 393890 | demand_slowdown_4c_watch_counterexample | 2023-07-04 | 73800 | 78700 on 2023-07-04 | 38300 on 2023-11-13 | 6.64% | -48.1% | -51.33% |

## 5. Stage evidence split

### Stage2 / Stage3
- These are not clean Stage3-Green positive rows.
- They are late-cycle battery-material rows where earlier orderbook/capacity stories had already been heavily priced.

### 4B
- 121600 is the protective success case: local 4B discipline would have mattered because the price path quickly shifted from peak proximity to a deep drawdown.
- 336370 and 393890 show why relative strength after a battery-material run should not be counted as fresh Green evidence.

### 4C
- The break is not necessarily an accounting scandal.
- C14 detects demand/utilization/margin fade: the customer pipeline no longer pulls the same way, and the once-full orderbook story starts breathing like an empty bellows.

## 6. Raw component score breakdown

```json
{
  "C14_121600_NANOSINSO_20230410_CNT_BATTERY_MATERIAL_LATE_4B_DEMAND_FADE": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 8,
    "information_confidence": 4,
    "market_mispricing": 4,
    "total": 37,
    "valuation_rerating_runway": 3,
    "visibility_quality": 7
  },
  "C14_336370_SOLUS_20230222_COPPERFOIL_EV_DEMAND_SLOWDOWN_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 33,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  },
  "C14_393890_WCP_20230704_SEPARATOR_LATE_RERATING_4C_WATCH": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 32,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C14 guard:
```text
if battery_material_late_rerating and demand_or_utilization_risk_unresolved:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and margin_revision_bridge_fades:
    escalate_to_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 336370 / 2023-02-22: copperfoil/battery-supply relative strength could be over-promoted if EV demand and margin bridge are not required.
- 393890 / 2023-07-04: separator late rerating should be 4B/4C watch, not fresh Green.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -38.1, "MAE_30D_pct": -23.65, "MAE_90D_pct": -35.77, "MFE_180D_pct": 4.82, "MFE_30D_pct": 4.82, "MFE_90D_pct": 4.82, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_121600_NANOSINSO_20230410_CNT_BATTERY_MATERIAL_LATE_4B_DEMAND_FADE", "case_role": "protective_4b_success", "company_name": "나노신소재", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "C14 guard should convert late battery-material rerating into local 4B watch; not a fresh Green after demand/rerating saturation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.94, "entry_date": "2023-04-10", "entry_price": 184800, "evidence_family": "cnt_battery_material_late_rerating_ev_demand_fade_guard", "evidence_url_pending": false, "fine_archetype_id": "EV_BATTERY_MATERIAL_DEMAND_SLOWDOWN_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-26", "low_price_180d": 114400, "peak_date": "2023-04-10", "peak_price": 193700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/121/121600.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 8, "information_confidence": 4, "market_mispricing": 4, "total": 37, "valuation_rerating_runway": 3, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C14_121600_NANOSINSO_20230410_CNT_BATTERY_MATERIAL_LATE_4B_DEMAND_FADE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_material_relative_strength", "ev_supply_chain_attention", "prior_orderbook_or_capacity_story"], "stage3_evidence_fields": ["fresh_green_blocked_by_late_rerating", "demand_visibility_required", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["late_price_strength_after_large_battery_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ev_demand_slowdown", "customer_utilization_fade", "margin_or_revision_break_watch"], "symbol": "121600", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2023.csv", "trigger_date": "2023-04-10", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -35.34, "MAE_30D_pct": -23.75, "MAE_90D_pct": -30.46, "MFE_180D_pct": 3.45, "MFE_30D_pct": 3.45, "MFE_90D_pct": 3.45, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_336370_SOLUS_20230222_COPPERFOIL_EV_DEMAND_SLOWDOWN_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "솔루스첨단소재", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Battery supply-chain relative strength should not become Green when EV demand, utilization, and margin bridge are unresolved.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.5, "entry_date": "2023-02-22", "entry_price": 52200, "evidence_family": "copperfoil_battery_supply_chain_relative_strength_without_demand_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "EV_BATTERY_MATERIAL_DEMAND_SLOWDOWN_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-07-19", "low_price_180d": 33750, "peak_date": "2023-02-22", "peak_price": 54000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/336/336370.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 33, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C14_336370_SOLUS_20230222_COPPERFOIL_EV_DEMAND_SLOWDOWN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_material_relative_strength", "ev_supply_chain_attention", "prior_orderbook_or_capacity_story"], "stage3_evidence_fields": ["fresh_green_blocked_by_late_rerating", "demand_visibility_required", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["late_price_strength_after_large_battery_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ev_demand_slowdown", "customer_utilization_fade", "margin_or_revision_break_watch"], "symbol": "336370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv", "trigger_date": "2023-02-22", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -48.1, "MAE_30D_pct": -10.3, "MAE_90D_pct": -27.37, "MFE_180D_pct": 6.64, "MFE_30D_pct": 6.64, "MFE_90D_pct": 6.64, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_393890_WCP_20230704_SEPARATOR_LATE_RERATING_4C_WATCH", "case_role": "demand_slowdown_4c_watch_counterexample", "company_name": "더블유씨피", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Late separator rerating should trigger 4B/4C watch when demand utilization evidence weakens; fresh Green would be an error.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.33, "entry_date": "2023-07-04", "entry_price": 73800, "evidence_family": "separator_late_rerating_ev_demand_customer_utilization_fade", "evidence_url_pending": false, "fine_archetype_id": "EV_BATTERY_MATERIAL_DEMAND_SLOWDOWN_4B_4C_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-11-13", "low_price_180d": 38300, "peak_date": "2023-07-04", "peak_price": 78700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/393/393890.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 32, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C14_393890_WCP_20230704_SEPARATOR_LATE_RERATING_4C_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R3", "source_proxy_only": false, "stage2_evidence_fields": ["battery_material_relative_strength", "ev_supply_chain_attention", "prior_orderbook_or_capacity_story"], "stage3_evidence_fields": ["fresh_green_blocked_by_late_rerating", "demand_visibility_required", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["late_price_strength_after_large_battery_run", "valuation_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["ev_demand_slowdown", "customer_utilization_fade", "margin_or_revision_break_watch"], "symbol": "393890", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "trigger_date": "2023-07-04", "trigger_type": "Stage4C-Watch", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "EV_BATTERY_MATERIAL_DEMAND_SLOWDOWN_4B_4C_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "4b_4c_guard_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R3",
  "shadow_rule_candidate": "C14 should convert late battery-material relative strength into 4B/4C watch when EV demand, utilization, or margin/revision bridge weakens; do not allow fresh Green after price has already capitalized the orderbook story.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C14 + symbol + trigger_type + entry_date.
3. Treat C14 as a guardrail archetype: it should protect against fresh Green after late battery-material rerating, not create new positive promotion.

Candidate rule:
- C14_BATTERY_LATE_RERATING_BLOCKS_GREEN
- C14_EV_DEMAND_UTILIZATION_FADE_4C_WATCH
- C14_PRICE_PEAK_PROXIMITY_LOCAL_4B

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

