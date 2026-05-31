# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C09 — Advanced equipment valuation blowoff guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: DEPOSITION_PARTS_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_deposition_parts_valuation_blowoff_2024_research.md
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

This run avoids those top-covered C09 symbols and adds 036930, 240810, and 064760.  
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
036930 주성엔지니어링: 2024 forward window clean; corporate-action candidate is 2000-06-22 and outside selected test window.
240810 원익IPS: corporate_action_candidate_count=0.
064760 티씨케이: corporate_action_candidate_count=0.
```

## 3. Research thesis

C09 should not treat advanced-equipment valuation heat as fresh earnings evidence. It should detect when the market has already paid for the order cycle:

```text
advanced equipment / deposition / parts price premium
→ fresh order or customer allocation proof required
→ delivery schedule and utilization
→ ASP/mix and gross-margin bridge
→ revision confirmation
→ rerating or 4B cap
```

Equipment momentum is the sound of the factory floor waking up. C09 should not buy the echo; it should ask whether the next purchase order, delivery slot and margin invoice are already visible.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C09_036930_JUSUNG_20240408_ADVANCED_DEP_VALUATION_BLOWOFF_4B | 036930 | protective_advanced_deposition_valuation_blowoff_4b_success | 2024-04-08 | 36500 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 13.56% | 13.56% | 13.56% | -39.59% | -46.8% |
| C09_240810_WONIKIPS_20240408_ADVANCED_EQUIPMENT_BLOWOFF_FALSE_GREEN | 240810 | advanced_equipment_order_expectation_false_green_counterexample | 2024-04-08 | 41650 | 44850 on 2024-04-08 | 21150 on 2024-12-09 | 7.68% | 7.68% | 7.68% | -49.22% | -52.84% |
| C09_064760_TCK_20240614_PARTS_VALUATION_BLOWOFF_4B | 064760 | advanced_parts_price_premium_counterexample | 2024-06-14 | 141400 | 149900 on 2024-06-14 | 66500 on 2024-12-09 | 6.01% | 6.01% | 6.01% | -52.97% | -55.64% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as Stage2/Green positive research.
- Advanced equipment can be a valid Stage2 route in other rows, but these selected rows are valuation-blowoff / false-Green guards. Price strength alone is not a non-price evidence bridge.

### 4B
- 036930 is the protective 4B anchor. The April 2024 high was made on the trigger day, while the later path showed a large post-peak drawdown.
- 240810 is the false-Green guard: advanced-equipment order expectation was plausible, but order, delivery, utilization, margin and revision evidence did not keep expanding after price confirmation.
- 064760 is the parts-cycle version: high-quality parts exposure did not prevent a deep drawdown once the price had already capitalized recovery and customer reorder evidence failed to refresh.

### 4C
- No hard order cancellation, accounting failure or customer loss is asserted.
- The C09 break mode is valuation exhaustion: the equipment story remains plausible, but backlog, delivery, utilization, ASP/mix, margin and revisions do not carry the price already paid.

## 6. Raw component score breakdown

```json
{
  "C09_036930_JUSUNG_20240408_ADVANCED_DEP_VALUATION_BLOWOFF_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 29,
    "valuation_rerating_runway": 1,
    "visibility_quality": 6
  },
  "C09_064760_TCK_20240614_PARTS_VALUATION_BLOWOFF_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  },
  "C09_240810_WONIKIPS_20240408_ADVANCED_EQUIPMENT_BLOWOFF_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 27,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C09 guard:
```text
if advanced_equipment_price_premium and no incremental_order_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if parts_or_equipment_theme_confirmation and utilization_or_customer_allocation_bridge_fails:
    route_to_counterexample_or_4C_watch = true

if post_peak_drawdown confirms:
    require_non_price_recovery_evidence_before_reentry = true
```

Residual errors:
```text
current_profile_error_count = 2
- 240810 / 2024-04-08: advanced-equipment order expectation can be over-promoted if price confirmation substitutes for order, delivery and margin proof.
- 064760 / 2024-06-14: advanced parts valuation premium can look structurally high quality, but still fail if reorder, utilization and revision evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -39.59, "MAE_30D_pct": -13.29, "MAE_90D_pct": -39.32, "MFE_180D_pct": 13.56, "MFE_30D_pct": 13.56, "MFE_90D_pct": 13.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_036930_JUSUNG_20240408_ADVANCED_DEP_VALUATION_BLOWOFF_4B", "case_role": "protective_advanced_deposition_valuation_blowoff_4b_success", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2000-06-22 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when advanced deposition/HBM-equipment enthusiasm had already been capitalized in price but fresh order, customer allocation, delivery, margin and revision evidence had not expanded enough to support the premium.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-04-08", "entry_price": 36500, "evidence_family": "advanced_deposition_equipment_price_premium_without_incremental_order_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PARTS_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 22050, "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/036/036930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 29, "valuation_rerating_runway": 1, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C09_036930_JUSUNG_20240408_ADVANCED_DEP_VALUATION_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_attention", "fresh_order_or_customer_allocation_signal_required", "delivery_schedule_utilization_margin_revision_visibility_required"], "stage3_evidence_fields": ["fresh_backlog_and_delivery_schedule_required", "customer_allocation_utilization_ASP_mix_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_or_parts_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_expectation_to_delivery_gap", "utilization_or_customer_allocation_disappointment", "margin_revision_bridge_failure"], "symbol": "036930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -49.22, "MAE_30D_pct": -15.61, "MAE_90D_pct": -28.33, "MFE_180D_pct": 7.68, "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_240810_WONIKIPS_20240408_ADVANCED_EQUIPMENT_BLOWOFF_FALSE_GREEN", "case_role": "advanced_equipment_order_expectation_false_green_counterexample", "company_name": "원익IPS", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Advanced-equipment order expectation should stay Yellow or local 4B when price confirmation is not followed by fresh customer order, delivery schedule, utilization, margin and revision evidence. The April 2024 premium had limited forward upside and large later MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.84, "entry_date": "2024-04-08", "entry_price": 41650, "evidence_family": "advanced_equipment_hbm_order_expectation_price_confirmation_without_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PARTS_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 21150, "peak_date": "2024-04-08", "peak_price": 44850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/240/240810.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 27, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C09_240810_WONIKIPS_20240408_ADVANCED_EQUIPMENT_BLOWOFF_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_attention", "fresh_order_or_customer_allocation_signal_required", "delivery_schedule_utilization_margin_revision_visibility_required"], "stage3_evidence_fields": ["fresh_backlog_and_delivery_schedule_required", "customer_allocation_utilization_ASP_mix_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_or_parts_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_expectation_to_delivery_gap", "utilization_or_customer_allocation_disappointment", "margin_revision_bridge_failure"], "symbol": "240810", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -52.97, "MAE_30D_pct": -17.96, "MAE_90D_pct": -38.68, "MFE_180D_pct": 6.01, "MFE_30D_pct": 6.01, "MFE_90D_pct": 6.01, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_064760_TCK_20240614_PARTS_VALUATION_BLOWOFF_4B", "case_role": "advanced_parts_price_premium_counterexample", "company_name": "티씨케이", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Advanced semiconductor parts premium should route to local 4B or counterexample when the parts-cycle narrative is already priced and customer reorder, utilization, ASP/mix, gross margin and revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.64, "entry_date": "2024-06-14", "entry_price": 141400, "evidence_family": "sic_ring_parts_hbm_equipment_cycle_price_premium_without_utilization_reorder_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PARTS_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 66500, "peak_date": "2024-06-14", "peak_price": 149900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/064/064760.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C09_064760_TCK_20240614_PARTS_VALUATION_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_attention", "fresh_order_or_customer_allocation_signal_required", "delivery_schedule_utilization_margin_revision_visibility_required"], "stage3_evidence_fields": ["fresh_backlog_and_delivery_schedule_required", "customer_allocation_utilization_ASP_mix_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_or_parts_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_expectation_to_delivery_gap", "utilization_or_customer_allocation_disappointment", "margin_revision_bridge_failure"], "symbol": "064760", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv", "trigger_date": "2024-06-14", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "DEPOSITION_PARTS_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "advanced_equipment_valuation_blowoff_deposition_parts_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C09 advanced-equipment valuation-blowoff rows should route equipment/parts price premiums to local 4B or counterexample unless fresh order/backlog, customer allocation, delivery schedule, utilization, ASP/mix, gross margin and revision evidence keep expanding after the price run.",
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
3. Add C09-specific advanced-equipment valuation blowoff / order-delivery-margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C09_BLOCK_GREEN_WHEN_ADVANCED_EQUIPMENT_PREMIUM_LACKS_INCREMENTAL_ORDER_BRIDGE
- C09_LOCAL_4B_ON_EQUIPMENT_OR_PARTS_PRICE_PREMIUM
- C09_REQUIRE_ORDER_DELIVERY_UTILIZATION_ASP_MIX_MARGIN_REVISION_FOR_REENTRY
- C09_EQUIPMENT_VALUATION_EXHAUSTION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

