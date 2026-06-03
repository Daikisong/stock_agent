# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C07 — HBM equipment order relative-strength guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: DEPOSITION_QUARTZ_VACUUM_ORDER_RELATIVE_STRENGTH_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_deposition_quartz_vacuum_order_guard_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH current coverage:
rows=8, symbols=5, date range=2024-01-19~2024-06-13, good/bad S2=2/0, 4B/4C=1/0
top covered symbols: 042700(3), 089030(2), 039030(1), 058470(1), 095340(1)
```

This run avoids those top-covered C07 symbols and adds 036930, 074600, and 083310.  
Each row uses a new `C07 + symbol + trigger_type + entry_date` hard key.

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
036930 주성엔지니어링: 2024 forward window clean; corporate-action candidate is 2000-06-22, outside the selected test window.
074600 원익QnC: 2024 forward window clean; corporate-action candidates are 2004 and 2017, outside the selected test window.
083310 엘오티베큠: 2024 forward window clean; corporate-action candidates are 2007, outside the selected test window.
```

## 3. Research thesis

C07 should not treat every HBM-equipment relative-strength burst as order conversion. It should test whether relative strength is tied to fresh order evidence rather than only to theme rotation:

```text
HBM equipment / deposition / quartz / vacuum relative strength
→ fresh backlog or customer allocation
→ delivery schedule and customer order quality
→ ASP/mix, utilization and margin bridge
→ revision confirmation
→ rerating
```

Relative strength is the smoke. Orders are the fire. C07 should follow smoke early, but Green should require heat from actual backlog, delivery and margin.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C07_036930_JUSUNG_20240223_HBM_DEP_EQUIP_ORDER_RS_STAGE2 | 036930 | positive_hbm_deposition_equipment_order_relative_strength_stage2_success_with_later_4b | 2024-02-23 | 32450 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 27.73% | 27.73% | 27.73% | -32.05% | -46.8% |
| C07_074600_WONIKQNC_20240607_QUARTZ_HBM_SUPPLY_PRICE_PREMIUM_4B | 074600 | quartz_hbm_supply_order_relative_strength_price_premium_counterexample | 2024-06-07 | 40950 | 41000 on 2024-06-07 | 17820 on 2024-12-02 | 0.12% | 0.12% | 0.12% | -56.48% | -56.54% |
| C07_083310_LOTVACUUM_20240222_VACUUM_HBM_ORDER_FALSE_GREEN | 083310 | vacuum_equipment_order_relative_strength_false_green_counterexample | 2024-02-22 | 23350 | 24450 on 2024-02-23 | 7660 on 2024-12-06 | 4.71% | 4.71% | 4.71% | -67.19% | -68.67% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- HBM-equipment order relative strength can be a valid Stage2 route when it appears before order/backlog expectations are fully capitalized.
- 036930 is the positive anchor: the February 2024 deposition-equipment route produced a usable MFE, but the same row later required 4B discipline when evidence stopped expanding and the stock entered a deep post-peak drawdown.

### Stage3 / Green
- C07 Green should require fresh backlog, customer allocation, delivery schedule, customer order quality, ASP/mix margin and revision confirmation.
- 083310 shows why a vacuum-equipment/HBM order label should stay Yellow if price confirmation is not followed by order and margin evidence. The forward path had small MFE and large MAE.

### 4B
- 074600 fills the local 4B pocket. The quartz/HBM supply-chain premium peaked on the trigger day and then unwound as incremental order, utilization and margin evidence did not support valuation.
- 036930 also matured from a valid Stage2 into 4B watch after the April 2024 price run.

### 4C
- No hard order cancellation or accounting break is asserted.
- The C07 break mode is order-evidence exhaustion: the HBM equipment story remains plausible, but backlog, customer allocation, delivery cadence, utilization, margin and revisions do not keep widening.

## 6. Raw component score breakdown

```json
{
  "C07_036930_JUSUNG_20240223_HBM_DEP_EQUIP_ORDER_RS_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 54,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  },
  "C07_074600_WONIKQNC_20240607_QUARTZ_HBM_SUPPLY_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 30,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C07_083310_LOTVACUUM_20240222_VACUUM_HBM_ORDER_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 28,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C07 guard:
```text
if hbm_equipment_relative_strength and fresh_backlog_delivery_visibility:
    allow_stage2_actionable = true

if hbm_equipment_price_premium and no incremental_order_customer_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and order_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 074600 / 2024-06-07: quartz/HBM equipment supply premium can be over-promoted if the model treats price strength as fresh customer/order evidence.
- 083310 / 2024-02-22: vacuum-equipment order relative strength can look like Green, but the later path argues for Yellow/counterexample unless delivery and margin revisions close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -32.05, "MAE_30D_pct": -4.31, "MAE_90D_pct": -4.31, "MFE_180D_pct": 27.73, "MFE_30D_pct": 27.73, "MFE_90D_pct": 27.73, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_036930_JUSUNG_20240223_HBM_DEP_EQUIP_ORDER_RS_STAGE2", "case_role": "positive_hbm_deposition_equipment_order_relative_strength_stage2_success_with_later_4b", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when deposition/HBM-equipment relative strength appeared before the valuation had fully capitalized order visibility, but Green still requires fresh order/backlog, customer allocation, delivery schedule, margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-02-23", "entry_price": 32450, "evidence_family": "advanced_deposition_hbm_equipment_order_relative_strength_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_QUARTZ_VACUUM_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 22050, "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/036/036930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 54, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C07_036930_JUSUNG_20240223_HBM_DEP_EQUIP_ORDER_RS_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_order_relative_strength_attention", "customer_allocation_or_backlog_visibility_claim", "delivery_schedule_or_margin_revision_signal"], "stage3_evidence_fields": ["fresh_order_backlog_required", "customer_allocation_and_delivery_schedule_required", "ASP_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_order_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_or_customer_allocation_gap", "delivery_schedule_or_utilization_failure", "margin_revision_bridge_failure"], "symbol": "036930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "trigger_date": "2024-02-23", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -56.48, "MAE_30D_pct": -16.36, "MAE_90D_pct": -45.18, "MFE_180D_pct": 0.12, "MFE_30D_pct": 0.12, "MFE_90D_pct": 0.12, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_074600_WONIKQNC_20240607_QUARTZ_HBM_SUPPLY_PRICE_PREMIUM_4B", "case_role": "quartz_hbm_supply_order_relative_strength_price_premium_counterexample", "company_name": "원익QnC", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Quartz/HBM-equipment supply relative strength should route to local 4B once price has capitalized order optionality and incremental customer order, delivery, utilization, ASP/mix margin and revision evidence are not refreshed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -56.54, "entry_date": "2024-06-07", "entry_price": 40950, "evidence_family": "quartz_parts_hbm_equipment_supply_price_premium_without_incremental_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_QUARTZ_VACUUM_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-02", "low_price_180d": 17820, "peak_date": "2024-06-07", "peak_price": 41000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/074/074600.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 30, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C07_074600_WONIKQNC_20240607_QUARTZ_HBM_SUPPLY_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_order_relative_strength_attention", "customer_allocation_or_backlog_visibility_claim", "delivery_schedule_or_margin_revision_signal"], "stage3_evidence_fields": ["fresh_order_backlog_required", "customer_allocation_and_delivery_schedule_required", "ASP_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_order_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_or_customer_allocation_gap", "delivery_schedule_or_utilization_failure", "margin_revision_bridge_failure"], "symbol": "074600", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv", "trigger_date": "2024-06-07", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -67.19, "MAE_30D_pct": -11.13, "MAE_90D_pct": -51.69, "MFE_180D_pct": 4.71, "MFE_30D_pct": 4.71, "MFE_90D_pct": 4.71, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_083310_LOTVACUUM_20240222_VACUUM_HBM_ORDER_FALSE_GREEN", "case_role": "vacuum_equipment_order_relative_strength_false_green_counterexample", "company_name": "엘오티베큠", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Vacuum-equipment/HBM order relative strength should stay Yellow when customer allocation, delivery schedule, ASP/mix margin and revision duration do not improve after the spike; price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -68.67, "entry_date": "2024-02-22", "entry_price": 23350, "evidence_family": "vacuum_pump_hbm_equipment_order_theme_without_customer_delivery_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_QUARTZ_VACUUM_ORDER_RELATIVE_STRENGTH_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-06", "low_price_180d": 7660, "peak_date": "2024-02-23", "peak_price": 24450, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/083/083310.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 28, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C07_083310_LOTVACUUM_20240222_VACUUM_HBM_ORDER_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_order_relative_strength_attention", "customer_allocation_or_backlog_visibility_claim", "delivery_schedule_or_margin_revision_signal"], "stage3_evidence_fields": ["fresh_order_backlog_required", "customer_allocation_and_delivery_schedule_required", "ASP_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["HBM_equipment_order_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_or_customer_allocation_gap", "delivery_schedule_or_utilization_failure", "margin_revision_bridge_failure"], "symbol": "083310", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv", "trigger_date": "2024-02-22", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "DEPOSITION_QUARTZ_VACUUM_ORDER_RELATIVE_STRENGTH_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "hbm_equipment_order_relative_strength_new_symbols_and_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C07 HBM-equipment order-relative-strength rows should allow Stage2 on early relative strength tied to fresh order/backlog and customer allocation, but Stage3 Green requires fresh backlog, delivery schedule, customer quality, ASP/mix margin and revision bridge; equipment price premium without incremental order proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C07 + symbol + trigger_type + entry_date.
3. Add C07-specific HBM-equipment order relative-strength / backlog-delivery / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C07_STAGE2_ALLOWED_ON_EARLY_HBM_EQUIPMENT_ORDER_RS_WITH_BACKLOG_VISIBILITY
- C07_GREEN_REQUIRES_FRESH_BACKLOG_CUSTOMER_ALLOCATION_DELIVERY_MARGIN_REVISION
- C07_HBM_EQUIPMENT_PRICE_PREMIUM_LOCAL_4B
- C07_EQUIPMENT_RS_WITHOUT_INCREMENTAL_ORDER_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

