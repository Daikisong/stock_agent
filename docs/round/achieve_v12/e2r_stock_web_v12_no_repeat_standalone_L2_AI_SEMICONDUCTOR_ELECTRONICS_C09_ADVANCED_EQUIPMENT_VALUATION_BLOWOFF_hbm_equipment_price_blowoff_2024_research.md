# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C09 — Advanced equipment valuation blowoff / HBM order optionality guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: HBM_EQUIPMENT_ORDER_OPTIONALITY_VALUATION_BLOWOFF_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|valuation_blowoff_green_block|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_hbm_equipment_price_blowoff_2024_research.md
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

This run avoids those top-covered C09 symbols and adds 003160, 232140, and 031980.  
Each row uses a new `C09 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
active_like_symbol_count: 2868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
003160 디아이: selected 2024 forward window clean; corporate-action candidates are historical and outside selected test window.
232140 와이씨/와이아이케이: selected 2024 forward window clean; corporate-action candidate is 2017-04-05 and outside selected test window.
031980 피에스케이홀딩스: selected 2024 forward window clean; corporate-action candidates are historical and latest 2020-02-21, outside selected test window.
```

## 3. Research thesis

C09 should not treat HBM equipment price acceleration as proof of order-to-revenue conversion. It should ask whether the blowoff is backed by fresh non-price evidence:

```text
advanced HBM equipment price acceleration
→ incremental customer order or allocation
→ delivery schedule and acceptance
→ revenue-recognition cadence and backlog conversion
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A blowoff is a flare. It can signal a hot equipment cycle, but Green should require the flare to become a purchase order, accepted tool, recognized revenue and margin revision.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C09_003160_DI_20240627_HBM_TESTER_VALUATION_BLOWOFF_4B | 003160 | protective_hbm_tester_valuation_blowoff_4b_success | 2024-06-27 | 27650 | 30800 on 2024-06-27 | 9860 on 2024-12-09 | 11.39% | 11.39% | 11.39% | -64.34% | -67.99% |
| C09_232140_YC_20240613_HBM_TESTER_ORDER_OPTION_BLOWOFF | 232140 | hbm_tester_order_option_blowoff_false_green_counterexample | 2024-06-13 | 21900 | 22950 on 2024-06-13 | 8290 on 2024-12-09 | 4.79% | 4.79% | 4.79% | -62.15% | -63.88% |
| C09_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_BLOWOFF | 031980 | hbm_packaging_equipment_valuation_blowoff_counterexample | 2024-06-14 | 80000 | 85300 on 2024-06-19 | 27700 on 2024-12-09 | 6.62% | 6.62% | 6.62% | -65.38% | -67.53% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C09 Green should require incremental customer order, delivery schedule, acceptance, revenue recognition, backlog conversion and margin/revision confirmation.
- 232140 is the false-Green/Yellow guard: order optionality and price confirmation existed, but residual upside was small and the later drawdown was much larger.

### 4B
- 003160 is the protective 4B anchor. The HBM tester thesis was real, but the June blowoff had already capitalized too much order optionality without enough fresh delivery and margin evidence.
- 232140 and 031980 are counterexamples where the market paid for order optionality before the order-to-revenue bridge refreshed.
- The key rule is that advanced-equipment price acceleration must not substitute for customer order, delivery acceptance, revenue cadence and margin revision.

### 4C
- No hard customer cancellation, tool rejection or accounting break is asserted.
- The failure mode is valuation blowoff / evidence exhaustion: the sector thesis can remain real while the stock price outruns the non-price evidence.

## 6. Raw component score breakdown

```json
{
  "C09_003160_DI_20240627_HBM_TESTER_VALUATION_BLOWOFF_4B": {
    "delivery_acceptance_revenue_cadence": 3,
    "downside_asymmetry": 11,
    "incremental_order_visibility": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 3,
    "price_acceleration_and_volume_heat": 12,
    "total": 49,
    "valuation_premium_vs_evidence": 11
  },
  "C09_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_BLOWOFF": {
    "delivery_acceptance_revenue_cadence": 3,
    "downside_asymmetry": 12,
    "incremental_order_visibility": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "price_acceleration_and_volume_heat": 11,
    "total": 52,
    "valuation_premium_vs_evidence": 12
  },
  "C09_232140_YC_20240613_HBM_TESTER_ORDER_OPTION_BLOWOFF": {
    "delivery_acceptance_revenue_cadence": 3,
    "downside_asymmetry": 12,
    "incremental_order_visibility": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "price_acceleration_and_volume_heat": 12,
    "total": 53,
    "valuation_premium_vs_evidence": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C09 guard:
```text
if advanced_equipment_price_acceleration and no incremental_customer_order_delivery_acceptance_margin_bridge:
    block_stage2_green_positive = true
    route_to_local_4B_or_counterexample = true

if residual_upside_small and forward_MAE_large:
    strengthen_blowoff_guard = true

if order_optionality_already_capitalized and revenue_cadence_not_visible:
    keep_stage3_yellow_or_4B_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 232140 / 2024-06-13: HBM tester order optionality can be over-promoted if price acceleration substitutes for order-to-revenue proof.
- 031980 / 2024-06-14: packaging-equipment valuation blowoff can look like Green, but fails without renewed order, delivery and margin bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -64.34, "MAE_30D_pct": -54.29, "MAE_90D_pct": -60.54, "MFE_180D_pct": 11.39, "MFE_30D_pct": 11.39, "MFE_90D_pct": 11.39, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_003160_DI_20240627_HBM_TESTER_VALUATION_BLOWOFF_4B", "case_role": "protective_hbm_tester_valuation_blowoff_4b_success", "company_name": "디아이", "corporate_action_window_status": "clean_2024_forward_window; profile corporate-action candidates are historical and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when HBM tester/equipment price momentum had already capitalized the order optionality. Without incremental customer order, delivery acceptance, revenue cadence and margin/revision evidence, the blowoff should not be treated as Stage2 or Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.99, "entry_date": "2024-06-27", "entry_price": 27650, "evidence_family": "hbm_tester_equipment_valuation_blowoff_without_incremental_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_EQUIPMENT_ORDER_OPTIONALITY_VALUATION_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 9860, "peak_date": "2024-06-27", "peak_price": 30800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003160.json", "raw_component_score_breakdown": {"delivery_acceptance_revenue_cadence": 3, "downside_asymmetry": 11, "incremental_order_visibility": 3, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 3, "price_acceleration_and_volume_heat": 12, "total": 49, "valuation_premium_vs_evidence": 11}, "reuse_reason": null, "same_entry_group_id": "C09_003160_DI_20240627_HBM_TESTER_VALUATION_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_order_attention", "customer_order_or_delivery_acceptance_required", "revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["incremental_customer_order_required", "delivery_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_valuation_blowoff", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_to_revenue_conversion_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "003160", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "trigger_date": "2024-06-27", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -62.15, "MAE_30D_pct": -36.07, "MAE_90D_pct": -46.21, "MFE_180D_pct": 4.79, "MFE_30D_pct": 4.79, "MFE_90D_pct": 4.79, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_232140_YC_20240613_HBM_TESTER_ORDER_OPTION_BLOWOFF", "case_role": "hbm_tester_order_option_blowoff_false_green_counterexample", "company_name": "와이씨", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2017-04-05 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "HBM tester order-option blowoff should remain Yellow/4B when price confirmation is not followed by incremental customer order, delivery acceptance, revenue recognition and margin-revision evidence. The residual upside after the trigger was small relative to the subsequent drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.88, "entry_date": "2024-06-13", "entry_price": 21900, "evidence_family": "hbm_tester_order_option_price_blowoff_without_delivery_acceptance_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_EQUIPMENT_ORDER_OPTIONALITY_VALUATION_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 8290, "peak_date": "2024-06-13", "peak_price": 22950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/232/232140.json", "raw_component_score_breakdown": {"delivery_acceptance_revenue_cadence": 3, "downside_asymmetry": 12, "incremental_order_visibility": 4, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "price_acceleration_and_volume_heat": 12, "total": 53, "valuation_premium_vs_evidence": 12}, "reuse_reason": null, "same_entry_group_id": "C09_232140_YC_20240613_HBM_TESTER_ORDER_OPTION_BLOWOFF", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_order_attention", "customer_order_or_delivery_acceptance_required", "revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["incremental_customer_order_required", "delivery_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_valuation_blowoff", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_to_revenue_conversion_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "232140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "trigger_date": "2024-06-13", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -65.38, "MAE_30D_pct": -28.75, "MAE_90D_pct": -49.75, "MFE_180D_pct": 6.62, "MFE_30D_pct": 6.62, "MFE_90D_pct": 6.62, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_BLOWOFF", "case_role": "hbm_packaging_equipment_valuation_blowoff_counterexample", "company_name": "피에스케이홀딩스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and latest 2020-02-21, outside selected test window", "current_profile_error": true, "current_profile_verdict": "HBM packaging-equipment valuation blowoff should route to local 4B or counterexample unless order backlog, delivery schedule, acceptance, revenue cadence and margin/revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.53, "entry_date": "2024-06-14", "entry_price": 80000, "evidence_family": "hbm_packaging_equipment_price_blowoff_without_incremental_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "HBM_EQUIPMENT_ORDER_OPTIONALITY_VALUATION_BLOWOFF_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 27700, "peak_date": "2024-06-19", "peak_price": 85300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/031/031980.json", "raw_component_score_breakdown": {"delivery_acceptance_revenue_cadence": 3, "downside_asymmetry": 12, "incremental_order_visibility": 4, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "price_acceleration_and_volume_heat": 11, "total": 52, "valuation_premium_vs_evidence": 12}, "reuse_reason": null, "same_entry_group_id": "C09_031980_PSKH_20240614_HBM_PACKAGING_EQUIPMENT_BLOWOFF", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_order_attention", "customer_order_or_delivery_acceptance_required", "revenue_cadence_margin_revision_route"], "stage3_evidence_fields": ["incremental_customer_order_required", "delivery_acceptance_and_revenue_recognition_required", "backlog_conversion_margin_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_valuation_blowoff", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_to_revenue_conversion_gap", "delivery_acceptance_or_revenue_recognition_delay", "margin_revision_bridge_failure"], "symbol": "031980", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "trigger_date": "2024-06-14", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_EQUIPMENT_ORDER_OPTIONALITY_VALUATION_BLOWOFF_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "advanced_equipment_valuation_blowoff_hbm_order_optionality_new_symbols",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C09 advanced-equipment valuation blowoff rows should block Stage2/Green when HBM equipment price acceleration is not backed by incremental customer order, delivery acceptance, revenue recognition cadence and margin revision; price blowoff should route to local 4B/counterexample even when the sector thesis remains real.",
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
3. Add C09-specific advanced equipment valuation blowoff / customer order / delivery acceptance / revenue cadence / margin revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C09_BLOCK_STAGE2_GREEN_WHEN_PRICE_BLOWOFF_LACKS_ORDER_TO_REVENUE_BRIDGE
- C09_GREEN_REQUIRES_CUSTOMER_ORDER_DELIVERY_ACCEPTANCE_REVENUE_CADENCE_REVISION
- C09_HBM_EQUIPMENT_ORDER_OPTIONALITY_PRICE_BLOWOFF_LOCAL_4B
- C09_SMALL_RESIDUAL_UPSIDE_LARGE_FORWARD_MAE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

