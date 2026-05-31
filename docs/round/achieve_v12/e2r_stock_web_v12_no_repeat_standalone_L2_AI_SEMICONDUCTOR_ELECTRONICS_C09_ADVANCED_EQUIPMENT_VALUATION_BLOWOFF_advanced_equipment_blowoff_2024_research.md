# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C09 — Advanced equipment valuation-blowoff guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_EQUIPMENT_BACKLOG_DELIVERY_MARGIN_BLOWOFF_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_advanced_equipment_blowoff_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF current coverage:
rows=16, symbols=5, date range=2024-01-19~2024-06-21, good/bad S2=3/0, 4B/4C=2/1
top covered symbols: 039030(2), 042700(2), 095340(2), 이오테크닉스(2), 한미반도체(2)
```

This run avoids those top-covered C09 symbols and adds 036930, 403870, and 084370.  
Each row uses a new `C09 + symbol + trigger_type + entry_date` hard key.

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
036930 주성엔지니어링: 2024 forward window clean; corporate-action candidate is 2000-06-22 and outside the selected test window.
403870 HPSP: 2024 forward window clean; corporate-action candidates are 2023-03-16 and 2023-04-11, outside the selected test window.
084370 유진테크: 2024 forward window clean; corporate-action candidates are 2007/2010/2012 and outside the selected test window.
```

## 3. Research thesis

C09 should not treat every advanced-equipment rerating as durable Green. It should test whether the equipment premium has enough fresh backlog and margin evidence left after the stock has already moved:

```text
advanced equipment / process tool relative strength
→ fresh order and backlog visibility
→ delivery schedule and customer allocation
→ ASP/mix and margin bridge
→ revision duration
→ rerating
```

The tool may be precise, but the stock can become blunt. Early relative strength can be a guide rail. Late valuation premium without incremental backlog is a cliff edge.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C09_036930_JUSUNG_20240223_ADV_EQUIP_ALD_STAGE2_SUCCESS_WITH_4B | 036930 | positive_advanced_equipment_stage2_success_with_later_4b | 2024-02-23 | 32450 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 27.73% | 27.73% | 27.73% | -32.05% | -46.8% |
| C09_403870_HPSP_20240215_HIGH_PRESSURE_EQUIP_VALUATION_BLOWOFF_4B | 403870 | high_pressure_equipment_blowoff_counterexample | 2024-02-15 | 63100 | 63900 on 2024-02-15 | 23700 on 2024-09-09 | 1.27% | 1.27% | 1.27% | -62.44% | -62.91% |
| C09_084370_EUGENETECH_20240528_ADV_EQUIP_ORDER_PREMIUM_FALSE_GREEN | 084370 | advanced_equipment_order_premium_false_green_counterexample | 2024-05-28 | 56500 | 60000 on 2024-05-28 | 31600 on 2024-12-02 | 6.19% | 6.19% | 6.19% | -44.07% | -47.33% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Advanced equipment relative strength can be a valid Stage2 route when it appears before the valuation has fully capitalized backlog and delivery expectations.
- 036930 is the positive anchor: the February 2024 equipment/ALD route produced a usable MFE before the evidence aged into an April 2024 local 4B problem.

### Stage3 / Green
- C09 Green should require fresh backlog, delivery schedule, customer concentration quality, ASP/mix margin and revision duration.
- 403870 and 084370 show why equipment price confirmation should not be treated as Green when the market has already paid for the order story.

### 4B
- 403870 is the clean local 4B blowoff row. The high-pressure equipment premium reached a high almost immediately, then fell into a deep drawdown.
- 084370 is a slower false-Green variant: price reached a premium on advanced equipment/order expectations, but backlog and margin duration did not carry the valuation.

### 4C
- No hard accounting or order-cancellation break is asserted.
- The C09 break mode is evidence exhaustion: the tool demand story remains plausible, but incremental backlog, delivery, margin and revisions do not continue to widen.

## 6. Raw component score breakdown

```json
{
  "C09_036930_JUSUNG_20240223_ADV_EQUIP_ALD_STAGE2_SUCCESS_WITH_4B": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 53,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  },
  "C09_084370_EUGENETECH_20240528_ADV_EQUIP_ORDER_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 31,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C09_403870_HPSP_20240215_HIGH_PRESSURE_EQUIP_VALUATION_BLOWOFF_4B": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 33,
    "valuation_rerating_runway": 2,
    "visibility_quality": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C09 guard:
```text
if advanced_equipment_relative_strength and early_backlog_delivery_visibility:
    allow_stage2_actionable = true

if advanced_equipment_price_premium and no incremental_backlog_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and order_margin_revision_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 403870 / 2024-02-15: high-pressure equipment premium can be over-promoted if the model treats price confirmation as incremental backlog evidence.
- 084370 / 2024-05-28: deposition equipment order premium can look like Green, but the later path argues for Yellow/local 4B unless backlog, delivery, ASP/mix and margin revisions continue to expand.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -32.05, "MAE_30D_pct": -4.31, "MAE_90D_pct": -2.47, "MFE_180D_pct": 27.73, "MFE_30D_pct": 27.73, "MFE_90D_pct": 27.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_036930_JUSUNG_20240223_ADV_EQUIP_ALD_STAGE2_SUCCESS_WITH_4B", "case_role": "positive_advanced_equipment_stage2_success_with_later_4b", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when advanced deposition/ALD equipment relative strength began to separate from generic semiconductor beta, but Green still requires fresh order/backlog, delivery schedule, customer mix, margin and revision bridge; after the April 2024 price run, the same evidence should shift to local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-02-23", "entry_price": 32450, "evidence_family": "advanced_deposition_equipment_relative_strength_order_visibility_to_valuation_blowoff_guard", "evidence_url_pending": false, "fine_archetype_id": "ADVANCED_EQUIPMENT_BACKLOG_DELIVERY_MARGIN_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 22050, "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/036/036930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 53, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C09_036930_JUSUNG_20240223_ADV_EQUIP_ALD_STAGE2_SUCCESS_WITH_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_relative_strength_attention", "order_backlog_or_customer_delivery_visibility_claim", "margin_or_revision_bridge_signal"], "stage3_evidence_fields": ["fresh_backlog_and_delivery_schedule_required", "customer_concentration_and_ASP_mix_quality_required", "margin_or_revision_duration_required"], "stage4b_evidence_fields": ["advanced_equipment_valuation_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["backlog_or_delivery_gap", "customer_order_quality_disappointment", "margin_revision_bridge_failure"], "symbol": "036930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "trigger_date": "2024-02-23", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -62.44, "MAE_30D_pct": -23.06, "MAE_90D_pct": -27.81, "MFE_180D_pct": 1.27, "MFE_30D_pct": 1.27, "MFE_90D_pct": 1.27, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_403870_HPSP_20240215_HIGH_PRESSURE_EQUIP_VALUATION_BLOWOFF_4B", "case_role": "high_pressure_equipment_blowoff_counterexample", "company_name": "HPSP", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "High-pressure advanced-equipment premium should route to local 4B or counterexample unless incremental order/backlog, delivery, customer-concentration quality, margin and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -62.91, "entry_date": "2024-02-15", "entry_price": 63100, "evidence_family": "high_pressure_anneal_equipment_price_premium_without_incremental_order_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "ADVANCED_EQUIPMENT_BACKLOG_DELIVERY_MARGIN_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 23700, "peak_date": "2024-02-15", "peak_price": 63900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/403/403870.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 4, "total": 33, "valuation_rerating_runway": 2, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C09_403870_HPSP_20240215_HIGH_PRESSURE_EQUIP_VALUATION_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_relative_strength_attention", "order_backlog_or_customer_delivery_visibility_claim", "margin_or_revision_bridge_signal"], "stage3_evidence_fields": ["fresh_backlog_and_delivery_schedule_required", "customer_concentration_and_ASP_mix_quality_required", "margin_or_revision_duration_required"], "stage4b_evidence_fields": ["advanced_equipment_valuation_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["backlog_or_delivery_gap", "customer_order_quality_disappointment", "margin_revision_bridge_failure"], "symbol": "403870", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv", "trigger_date": "2024-02-15", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.07, "MAE_30D_pct": -16.99, "MAE_90D_pct": -37.43, "MFE_180D_pct": 6.19, "MFE_30D_pct": 6.19, "MFE_90D_pct": 6.19, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_084370_EUGENETECH_20240528_ADV_EQUIP_ORDER_PREMIUM_FALSE_GREEN", "case_role": "advanced_equipment_order_premium_false_green_counterexample", "company_name": "유진테크", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Advanced equipment order premium should stay Yellow or local 4B when backlog, customer allocation, delivery cadence, ASP/mix margin and revision duration do not keep expanding after the valuation run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.33, "entry_date": "2024-05-28", "entry_price": 56500, "evidence_family": "advanced_deposition_equipment_order_premium_without_backlog_delivery_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "ADVANCED_EQUIPMENT_BACKLOG_DELIVERY_MARGIN_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-02", "low_price_180d": 31600, "peak_date": "2024-05-28", "peak_price": 60000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/084/084370.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 31, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C09_084370_EUGENETECH_20240528_ADV_EQUIP_ORDER_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_relative_strength_attention", "order_backlog_or_customer_delivery_visibility_claim", "margin_or_revision_bridge_signal"], "stage3_evidence_fields": ["fresh_backlog_and_delivery_schedule_required", "customer_concentration_and_ASP_mix_quality_required", "margin_or_revision_duration_required"], "stage4b_evidence_fields": ["advanced_equipment_valuation_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["backlog_or_delivery_gap", "customer_order_quality_disappointment", "margin_revision_bridge_failure"], "symbol": "084370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv", "trigger_date": "2024-05-28", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "ADVANCED_EQUIPMENT_BACKLOG_DELIVERY_MARGIN_BLOWOFF_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "advanced_equipment_valuation_blowoff_new_symbols_and_order_margin_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C09 advanced-equipment valuation-blowoff rows should allow Stage2 when early equipment relative strength is tied to backlog/delivery visibility, but Stage3 Green requires fresh backlog, delivery schedule, customer concentration quality, ASP/mix margin and revision duration; advanced-equipment price premium without incremental order and margin proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C09 + symbol + trigger_type + entry_date.
3. Add C09-specific advanced-equipment valuation-blowoff / backlog-delivery / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C09_STAGE2_ALLOWED_ON_EARLY_ADVANCED_EQUIPMENT_BACKLOG_DELIVERY_VISIBILITY
- C09_GREEN_REQUIRES_FRESH_BACKLOG_DELIVERY_CUSTOMER_QUALITY_MARGIN_REVISION
- C09_ADVANCED_EQUIPMENT_PRICE_PREMIUM_LOCAL_4B
- C09_EQUIPMENT_VALUATION_BLOWOFF_WITHOUT_INCREMENTAL_ORDERS_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

