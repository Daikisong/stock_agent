# E2R v12 Residual Research — R9 / Loop 101 / L3 / C29

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R9
selected_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_SUPPLIER_TIRE_OEM_VOLUME_MARGIN_OPERATING_LEVERAGE_BRIDGE

primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

stock_agent_code_accessed = false
stock_agent_code_patch_written = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection and novelty check

The static no-repeat index shows **C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE** at 3 rows / 3 symbols with weights `20/18/10/15/17/15/5` and top covered symbols `005710`, `007860`, `033530`. In this conversation, one earlier C29 pass already used `005380`, `000270`, `204320`, and `011210`, so this pass avoids all of them.

New symbols selected here:

| symbol | name | role in C29 | reason for inclusion |
|---|---|---|---|
| 012330 | 현대모비스 | OEM module / parts / value-up bridge | tests capital-return + module-margin bridge versus OEM beta |
| 005850 | 에스엘 | lighting supplier | strong supplier margin-revision / volume leverage positive with later 4B risk |
| 018880 | 한온시스템 | thermal-management supplier | event-spike false positive / high-MAE counterexample |
| 161390 | 한국타이어앤테크놀로지 | tire margin / spread / volume | margin-spread operating leverage positive with late reversal guard |

No row uses the same `canonical_archetype_id + symbol + trigger_type + entry_date` key as the index top set or the conversation-local C29 ledger.

## 2. Price source audit

All price-path checks use `Songdaiki/stock-web` 1D OHLCV shards:

| symbol | stock-web file | profile caveat |
|---|---|---|
| 012330 | `atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv` | old corporate-action candidate windows exist, but 2024 window is away from blocked dates |
| 005850 | `atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv` | 2019 corporate-action candidate, 2024 usable |
| 018880 | `atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv` | 2025/2026 corporate-action candidates, 2024 usable |
| 161390 | `atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv` | no major raw discontinuity in profile |

Non-price evidence in this MD is intentionally conservative: `source_proxy_only / evidence_url_pending=true`. Therefore, the MD should be used as a price-path and residual-rule calibration row first, and only promoted to production-weight evidence after a later ingestion pass attaches direct filings, calls, or verified event URLs.

## 3. Case table

| case | trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | result |
|---|---|---:|---:|---:|---:|---|
| 현대모비스 | 2024-02-19 Stage2_Actionable | 244,000 | +10.66 / -5.74 | +10.66 / -8.20 | +10.66 / -15.16 | mixed positive, bridge needed |
| 에스엘 | 2024-05-17 Stage3_Yellow | 35,500 | +25.21 / -5.07 | +34.23 / -9.30 | +34.23 / -15.49 | positive then late 4B watch |
| 한온시스템 | 2024-05-03 Stage2 false positive | 6,490 | +4.78 / -22.80 | +4.78 / -32.97 | +4.78 / -43.45 | counterexample |
| 한국타이어앤테크놀로지 | 2024-01-25 Stage3_Yellow | 49,450 | +20.53 / -6.47 | +28.01 / -6.47 | +28.01 / -17.80 | positive with reversal guard |

## 4. Current calibrated profile stress test

### 4.1 What still works

The calibrated profile’s existing safeguards still work in direction:

```text
stage2_actionable_evidence_bonus = useful
price_only_blowoff_blocks_positive_stage = useful
full_4b_requires_non_price_evidence = useful
hard_4c_thesis_break_routes_to_4c = useful
```

The SL and Hankook Tire paths show that when auto-related price action is attached to a plausible margin/mix bridge, the 30D/90D MFE can be large enough to justify a positive C29 row. SL’s 2024-05-17 row reaches +34.23% 90D MFE, and Hankook Tire’s 2024-01-25 row reaches +28.01% 90D MFE.

### 4.2 Residual error

C29 has a special trap: **mobility beta often looks like operating leverage before it proves margin conversion**. A car can sound fast while still sitting on a lift. The price can rev, but the model needs to see whether torque reaches the wheels: volume/mix, ASP, supplier margin, order delivery, capital return, or cash conversion.

The strongest counterexample is Hanon System. The 2024-05-03 entry produced only +4.78% MFE but reached -32.97% 90D MAE and -43.45% 180D MAE. That is not “mobility operating leverage”; it is an event spike without a robust company-level margin/cash bridge.

## 5. Shadow rule candidate

```text
new_axis_proposed =
  C29_company_level_volume_margin_cash_bridge_required
  C29_event_spike_and_price_only_high_MAE_guard
  C29_post_peak_4b_reversal_guard
```

Rule draft:

1. **Bridge requirement.** C29 Stage3-Yellow or higher needs at least one company-level bridge:
   - volume/mix improvement,
   - ASP or margin improvement,
   - supplier order/delivery visibility,
   - capital return / value-up execution,
   - FCF or cash-conversion bridge.

2. **Event-spike cap.** If the only non-price evidence is M&A rumor, policy/event label, or broad OEM beta, and 90D MAE is worse than -25%, cap the case at `4B_Watch` or `Stage2_Watch`.

3. **Post-peak local 4B guard.** If a valid positive C29 row later suffers a peak-to-trough drawdown worse than -30% within 180D, keep it as positive evidence for entry scoring but mark it as `local_4b_watch` for chase/exit calibration.

## 6. Machine-readable rows

### 6.1 case_rows_jsonl

```jsonl
{"row_type": "case", "case_id": "C29_012330_2024-02-19_auto_parts_valueup_capital_return_volume_mix_bridge", "symbol": "012330", "name": "현대모비스", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "entry_date": "2024-02-19", "representative_trigger_type": "Stage2_Actionable", "outcome_label": "mixed_positive_high_MAE", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2_Actionable|2024-02-19", "usable_for_calibration": true}
{"row_type": "case", "case_id": "C29_005850_2024-05-17_supplier_margin_revision_volume_mix_followthrough", "symbol": "005850", "name": "에스엘", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "entry_date": "2024-05-17", "representative_trigger_type": "Stage3_Yellow", "outcome_label": "positive_then_late_high_MAE", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005850|Stage3_Yellow|2024-05-17", "usable_for_calibration": true}
{"row_type": "case", "case_id": "C29_018880_2024-05-03_supplier_event_spike_margin_bridge_failure", "symbol": "018880", "name": "한온시스템", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "entry_date": "2024-05-03", "representative_trigger_type": "Stage2_False_Positive", "outcome_label": "counterexample_event_spike_high_MAE", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|018880|Stage2_False_Positive|2024-05-03", "usable_for_calibration": true}
{"row_type": "case", "case_id": "C29_161390_2024-01-25_tire_margin_spread_volume_operating_leverage", "symbol": "161390", "name": "한국타이어앤테크놀로지", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "entry_date": "2024-01-25", "representative_trigger_type": "Stage3_Yellow", "outcome_label": "positive_with_late_4b_watch", "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|161390|Stage3_Yellow|2024-01-25", "usable_for_calibration": true}
```

### 6.2 trigger_rows_jsonl

```jsonl
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R9", "selected_loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MODULES_VALUEUP_AND_CAPITAL_RETURN_BRIDGE_VS_PRICE_ONLY_OEM_BETA", "symbol": "012330", "name": "현대모비스", "trigger_type": "Stage2_Actionable", "trigger_family": "auto_parts_valueup_capital_return_volume_mix_bridge", "entry_date": "2024-02-19", "entry_price": 244000, "entry_basis": "close", "peak_30d_price": 270000, "trough_30d_price": 230000, "mfe_30d_pct": 10.66, "mae_30d_pct": -5.74, "peak_90d_price": 270000, "trough_90d_price": 224000, "mfe_90d_pct": 10.66, "mae_90d_pct": -8.2, "peak_180d_price": 270000, "trough_180d_price": 207000, "mfe_180d_pct": 10.66, "mae_180d_pct": -15.16, "max_drawdown_from_peak_180d_pct": -23.33, "outcome_label": "mixed_positive_high_MAE", "current_profile_error": "Stage2 is directionally right, but C29 should not Green without explicit module margin/capital-return bridge because 180D MAE overwhelms early MFE.", "price_path_source": "stock-web/atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv", "evidence_quality": "price_verified_nonprice_proxy_only", "evidence_url_pending": true}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R9", "selected_loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_LIGHTING_SUPPLIER_VOLUME_MARGIN_REVISION_BRIDGE", "symbol": "005850", "name": "에스엘", "trigger_type": "Stage3_Yellow", "trigger_family": "supplier_margin_revision_volume_mix_followthrough", "entry_date": "2024-05-17", "entry_price": 35500, "entry_basis": "close", "peak_30d_price": 44450, "trough_30d_price": 33700, "mfe_30d_pct": 25.21, "mae_30d_pct": -5.07, "peak_90d_price": 47650, "trough_90d_price": 32200, "mfe_90d_pct": 34.23, "mae_90d_pct": -9.3, "peak_180d_price": 47650, "trough_180d_price": 30000, "mfe_180d_pct": 34.23, "mae_180d_pct": -15.49, "max_drawdown_from_peak_180d_pct": -37.04, "outcome_label": "positive_then_late_high_MAE", "current_profile_error": "Good Stage3-Yellow candidate when supplier margin revision is present; Green should require repeat order/mix evidence because post-peak drawdown is severe.", "price_path_source": "stock-web/atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv", "evidence_quality": "price_verified_nonprice_proxy_only", "evidence_url_pending": true}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R9", "selected_loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "THERMAL_MANAGEMENT_EVENT_SPIKE_WITHOUT_MARGIN_CASH_BRIDGE", "symbol": "018880", "name": "한온시스템", "trigger_type": "Stage2_False_Positive", "trigger_family": "supplier_event_spike_margin_bridge_failure", "entry_date": "2024-05-03", "entry_price": 6490, "entry_basis": "close", "peak_30d_price": 6800, "trough_30d_price": 5010, "mfe_30d_pct": 4.78, "mae_30d_pct": -22.8, "peak_90d_price": 6800, "trough_90d_price": 4350, "mfe_90d_pct": 4.78, "mae_90d_pct": -32.97, "peak_180d_price": 6800, "trough_180d_price": 3670, "mfe_180d_pct": 4.78, "mae_180d_pct": -43.45, "max_drawdown_from_peak_180d_pct": -46.03, "outcome_label": "counterexample_event_spike_high_MAE", "current_profile_error": "Headline/event spike can masquerade as C29 volume leverage; absent margin/cash bridge should route to watch/4B guard, not positive Stage.", "price_path_source": "stock-web/atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "evidence_quality": "price_verified_nonprice_proxy_only", "evidence_url_pending": true}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R9", "selected_loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_SPREAD_AND_VOLUME_LEVERAGE_WITH_4B_REVERSAL_RISK", "symbol": "161390", "name": "한국타이어앤테크놀로지", "trigger_type": "Stage3_Yellow", "trigger_family": "tire_margin_spread_volume_operating_leverage", "entry_date": "2024-01-25", "entry_price": 49450, "entry_basis": "close", "peak_30d_price": 59600, "trough_30d_price": 46250, "mfe_30d_pct": 20.53, "mae_30d_pct": -6.47, "peak_90d_price": 63300, "trough_90d_price": 46250, "mfe_90d_pct": 28.01, "mae_90d_pct": -6.47, "peak_180d_price": 63300, "trough_180d_price": 40650, "mfe_180d_pct": 28.01, "mae_180d_pct": -17.8, "max_drawdown_from_peak_180d_pct": -35.78, "outcome_label": "positive_with_late_4b_watch", "current_profile_error": "Strong early C29 price fit, but tire margin spread should be separated from OEM volume beta and guarded after sharp post-peak reversal.", "price_path_source": "stock-web/atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "evidence_quality": "price_verified_nonprice_proxy_only", "evidence_url_pending": true}
```

### 6.3 score_simulation_jsonl

```jsonl
{"row_type": "score_simulation", "profile_proxy": "e2r_2_2_rolling_calibrated", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "symbol": "012330", "entry_date": "2024-02-19", "raw_component_score_breakdown": {"eps_revision": 14, "visibility": 18, "bottleneck": 6, "mispricing": 15, "valuation": 17, "capital_return": 15, "info_edge": 5}, "simulated_stage_before_shadow_rule": "Stage2_Actionable", "simulated_stage_after_shadow_rule": "Stage2_Actionable", "shadow_rule_delta": "require_company_level_volume_margin_cash_bridge; cap price-only/event-spike cases"}
{"row_type": "score_simulation", "profile_proxy": "e2r_2_2_rolling_calibrated", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "symbol": "005850", "entry_date": "2024-05-17", "raw_component_score_breakdown": {"eps_revision": 20, "visibility": 18, "bottleneck": 10, "mispricing": 15, "valuation": 17, "capital_return": 6, "info_edge": 5}, "simulated_stage_before_shadow_rule": "Stage3_Yellow", "simulated_stage_after_shadow_rule": "Stage3_Yellow", "shadow_rule_delta": "require_company_level_volume_margin_cash_bridge; cap price-only/event-spike cases"}
{"row_type": "score_simulation", "profile_proxy": "e2r_2_2_rolling_calibrated", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "symbol": "018880", "entry_date": "2024-05-03", "raw_component_score_breakdown": {"eps_revision": 14, "visibility": 10, "bottleneck": 6, "mispricing": 10, "valuation": 8, "capital_return": 6, "info_edge": 5}, "simulated_stage_before_shadow_rule": "Stage2_Watch", "simulated_stage_after_shadow_rule": "4B_Watch", "shadow_rule_delta": "require_company_level_volume_margin_cash_bridge; cap price-only/event-spike cases"}
{"row_type": "score_simulation", "profile_proxy": "e2r_2_2_rolling_calibrated", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "symbol": "161390", "entry_date": "2024-01-25", "raw_component_score_breakdown": {"eps_revision": 20, "visibility": 18, "bottleneck": 10, "mispricing": 10, "valuation": 17, "capital_return": 6, "info_edge": 5}, "simulated_stage_before_shadow_rule": "Stage3_Yellow", "simulated_stage_after_shadow_rule": "Stage3_Yellow", "shadow_rule_delta": "require_company_level_volume_margin_cash_bridge; cap price-only/event-spike cases"}
```

### 6.4 aggregate_json

```json
{
  "row_type": "aggregate",
  "selected_round": "R9",
  "selected_loop": 101,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "AUTO_SUPPLIER_TIRE_OEM_VOLUME_MARGIN_OPERATING_LEVERAGE_BRIDGE",
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 2,
  "mixed_positive_count": 1,
  "counterexample_count": 1,
  "local_4b_watch_count": 2,
  "current_profile_error_count": 4,
  "auto_selected_coverage_gap_static_index": "C29 rows 3 -> 7 if accepted in static V12 index; conversation-local C29 second pass continues previous 4-row fill.",
  "auto_selected_coverage_gap_conversation_local": "C29 rows 7 -> 11 if accepted; still Priority 0, need about 19 to 30 after local ledger.",
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "do_not_propose_new_weight_delta": false
}
```

### 6.5 shadow_weight_json

```json
{
  "row_type": "shadow_weight",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "baseline_weight_runtime_report": "20/18/10/15/17/15/5",
  "proposed_shadow_rule_not_production_patch": {
    "C29_company_level_volume_margin_cash_bridge_required": {
      "logic": "OEM/supplier/tire cases require at least one company-level bridge among volume/mix, ASP/margin, order backlog/delivery, capital return or FCF conversion.",
      "effect": "Allow Stage3-Yellow only when price strength is accompanied by a company-level margin/revision bridge."
    },
    "C29_event_spike_and_price_only_high_MAE_guard": {
      "logic": "If non-price evidence is only M&A/event/headline or sector beta and 90D MAE <= -25%, cap at 4B_Watch/Stage2_Watch unless hard delivery/cash evidence appears.",
      "effect": "Hanon-style event spike blocked from positive Stage promotion."
    },
    "C29_post_peak_4b_reversal_guard": {
      "logic": "If 180D drawdown from peak <= -30% after a valid Stage3-Yellow, preserve positive row but mark local_4B_watch for exit/risk calibration.",
      "effect": "SL/Hankook Tire stay useful positives but teach the model not to chase after peak."
    }
  }
}
```

### 6.6 residual_contribution_jsonl

```jsonl
{"row_type": "residual_contribution", "scope": "canonical_archetype", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_axis_proposed": "C29_company_level_volume_margin_cash_bridge_required | C29_event_spike_high_MAE_guard | C29_post_peak_4b_reversal_guard", "existing_axis_strengthened": "stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail", "existing_axis_weakened": null, "loop_contribution_label": "canonical_archetype_rule_candidate"}
```

## 7. Residual contribution summary

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 2
mixed_positive_count = 1
counterexample_count = 1
local_4b_watch_count = 2
current_profile_error_count = 4

auto_selected_coverage_gap_static_index = C29 rows 3 -> 7 if accepted
auto_selected_coverage_gap_conversation_local = C29 rows 7 -> 11 if accepted
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
```

## 8. Deferred Coding Agent Handoff Prompt

Do not execute this section during research generation.

```text
You are a coding agent working on Songdaiki/stock_agent after the research batch is collected.

Input MD:
e2r_stock_web_v12_residual_round_R9_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse case_rows_jsonl, trigger_rows_jsonl, score_simulation_jsonl, aggregate_json, shadow_weight_json, and residual_contribution_jsonl.
2. Validate that every trigger row has complete 30D/90D/180D MFE and MAE fields.
3. Deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
4. Keep non-price evidence as low-trust until direct evidence URLs or filings are attached.
5. Consider adding a C29 shadow rule only after a batch-level review confirms the pattern:
   - require company-level volume/margin/cash bridge,
   - cap event-spike-only cases with high MAE,
   - mark post-peak drawdown >30% as local_4B_watch.
6. Do not change production scoring from this single MD alone.
```
