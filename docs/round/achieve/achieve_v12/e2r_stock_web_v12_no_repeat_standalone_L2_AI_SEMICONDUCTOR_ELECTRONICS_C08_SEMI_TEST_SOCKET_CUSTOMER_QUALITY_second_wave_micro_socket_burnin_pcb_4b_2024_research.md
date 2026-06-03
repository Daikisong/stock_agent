# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semi test socket customer quality / second-wave micro-socket·burn-in·test-PCB 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: SECOND_WAVE_MICRO_SOCKET_BURNIN_PCB_CUSTOMER_QUALITY_4B_GUARD
loop_objective: coverage_gap_fill|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_gap_fill|second_wave_customer_quality_to_order_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_second_wave_micro_socket_burnin_pcb_4b_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY current coverage:
rows=10, symbols=3, date range=2024-03-08~2024-04-26, good/bad S2=4/0, 4B/4C=0/0
top covered symbols: 058470(2), 131290(2), 리노공업(2), 티에스이(2), 095340(1)
```

This run avoids those top-covered C08 symbols and uses new second-wave hard keys:
```text
C08 + 219130 + 4B-local-price-only + 2024-05-14
C08 + 080580 + 4B-local-price-only + 2024-07-01
C08 + 098120 + Stage3-Yellow + 2024-04-26
```

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
219130 타이거일렉: corporate_action_candidate_count=0; clean 2024/2025 forward window.
080580 오킨스전자: selected post-2021 forward window clean; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window.
098120 마이크로컨텍솔: selected post-2011 forward window clean; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window.
```

## 3. Research thesis

C08 should distinguish fresh semi test-socket customer quality from second-wave customer-quality optionality already paid in price:

```text
semi test socket / burn-in socket / test PCB customer-quality signal
→ direct customer order or design-win visibility
→ delivery cadence and utilization
→ memory/HBM test-demand relevance
→ ASP/mix and gross margin bridge
→ Stage2/Green or local 4B cap
```

A test socket story is a probe touching the chip. Stage2 can buy it when the signal reaches customer order and margin revision. In the second wave, Green should require a new signal, not just the echo of the first spark.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C08_219130_TIGERELEC_20240514_TEST_PCB_CUSTOMER_QUALITY_4B_REFRESH | 219130 | protective_second_wave_test_pcb_customer_quality_4b_success | 2024-05-14 | 41500 | 45300 on 2024-05-14 | 9700 on 2025-04-07 | 9.16% | 9.16% | 9.16% | -76.63% | -78.59% |
| C08_080580_OKINS_20240701_SECOND_WAVE_BURNIN_SOCKET_4B | 080580 | second_wave_burnin_socket_customer_quality_price_premium_counterexample | 2024-07-01 | 8580 | 9170 on 2024-07-01 | 3685 on 2024-12-09 | 6.88% | 6.88% | 6.88% | -57.05% | -59.81% |
| C08_098120_MICROCONTACT_20240426_SECOND_WAVE_TEST_SOCKET_FALSE_GREEN | 098120 | second_wave_micro_test_socket_relative_strength_false_green_counterexample | 2024-04-26 | 10700 | 11130 on 2024-04-29 | 4245 on 2024-12-09 | 4.02% | 4.02% | 4.02% | -60.33% | -61.86% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a fresh clean Stage2/Green positive.
- C08 Green should require customer quality, order/design-win conversion, test-board/socket delivery cadence, utilization, margin revision and valuation runway.
- 098120 is the false-Green/Yellow guard: second-wave test-socket price confirmation was visible, but direct customer/order and margin evidence did not refresh; residual upside was tiny compared with forward MAE.

### 4B
- 219130 is the protective 4B anchor. It had valid earlier Stage2 behavior, but by 2024-05-14 the rerating already demanded fresh order-to-margin evidence.
- 080580 fills the second-wave burn-in socket theme price-premium 4B pocket. The July 2024 spike had little residual runway and then a large forward drawdown.
- The core 4B rule is that price-only continuation after the customer-quality rerating must not be promoted to Green unless fresh customer evidence appears.

### 4C
- No hard customer cancellation, design-win loss, accounting break or shipment collapse is asserted.
- The C08 break mode is customer-quality exhaustion: the test-socket theme may remain directionally relevant, but incremental customer order, delivery cadence, utilization and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C08_080580_OKINS_20240701_SECOND_WAVE_BURNIN_SOCKET_4B": {
    "customer_order_or_design_win_visibility": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "memory_HBM_test_demand_relevance": 6,
    "relative_strength_quality": 5,
    "test_socket_customer_quality": 6,
    "total": 33,
    "utilization_delivery_cadence": 3,
    "valuation_rerating_runway": 1
  },
  "C08_098120_MICROCONTACT_20240426_SECOND_WAVE_TEST_SOCKET_FALSE_GREEN": {
    "customer_order_or_design_win_visibility": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "memory_HBM_test_demand_relevance": 5,
    "relative_strength_quality": 4,
    "test_socket_customer_quality": 5,
    "total": 30,
    "utilization_delivery_cadence": 3,
    "valuation_rerating_runway": 1
  },
  "C08_219130_TIGERELEC_20240514_TEST_PCB_CUSTOMER_QUALITY_4B_REFRESH": {
    "customer_order_or_design_win_visibility": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "memory_HBM_test_demand_relevance": 7,
    "relative_strength_quality": 7,
    "test_socket_customer_quality": 7,
    "total": 40,
    "utilization_delivery_cadence": 4,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C08 guard:
```text
if semi_test_socket_customer_quality and direct_order_designwin_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if second_wave_test_socket_price_premium and no incremental_customer_order_utilization_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and customer_quality_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 080580 / 2024-07-01: second-wave burn-in socket theme premium can be over-promoted if price heat substitutes for direct customer order and margin proof.
- 098120 / 2024-04-26: micro test-socket confirmation can look like Yellow-to-Green, but fails without renewed customer-quality and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -76.63, "MAE_30D_pct": -35.78, "MAE_90D_pct": -63.95, "MFE_180D_pct": 9.16, "MFE_30D_pct": 9.16, "MFE_90D_pct": 9.16, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_219130_TIGERELEC_20240514_TEST_PCB_CUSTOMER_QUALITY_4B_REFRESH", "case_role": "protective_second_wave_test_pcb_customer_quality_4b_success", "company_name": "타이거일렉", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_2025_forward_window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful after the test-interface PCB/customer-quality rerating had already capitalized memory/HBM test demand. The stock had valid earlier Stage2 behavior, but at the 2024-05-14 premium residual upside was small relative to the subsequent drawdown unless fresh customer order, delivery cadence, utilization and margin/revision evidence expanded.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -78.59, "entry_date": "2024-05-14", "entry_price": 41500, "evidence_family": "second_wave_test_pcb_customer_quality_price_premium_without_incremental_order_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_MICRO_SOCKET_BURNIN_PCB_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2025-04-07", "low_price_180d": 9700, "peak_date": "2024-05-14", "peak_price": 45300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/219/219130.json", "raw_component_score_breakdown": {"customer_order_or_design_win_visibility": 4, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "memory_HBM_test_demand_relevance": 7, "relative_strength_quality": 7, "test_socket_customer_quality": 7, "total": 40, "utilization_delivery_cadence": 4, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_219130_TIGERELEC_20240514_TEST_PCB_CUSTOMER_QUALITY_4B_REFRESH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_customer_quality", "customer_order_or_design_win_visibility", "utilization_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_quality_and_order_conversion_required", "test_socket_or_test_board_delivery_cadence_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["second_wave_test_socket_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_design_win_gap", "utilization_or_delivery_gap", "margin_revision_bridge_failure"], "symbol": "219130", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv", "trigger_date": "2024-05-14", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -57.05, "MAE_30D_pct": -43.3, "MAE_90D_pct": -43.3, "MFE_180D_pct": 6.88, "MFE_30D_pct": 6.88, "MFE_90D_pct": 6.88, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_080580_OKINS_20240701_SECOND_WAVE_BURNIN_SOCKET_4B", "case_role": "second_wave_burnin_socket_customer_quality_price_premium_counterexample", "company_name": "오킨스전자", "corporate_action_window_status": "clean post-2021 corporate-action forward window; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Second-wave burn-in socket/customer-quality price premium should route to local 4B or counterexample when HBM/test salience is not backed by direct customer order conversion, delivery cadence, utilization and margin/revision evidence. The July 2024 trigger had little residual runway after the spike and a much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -59.81, "entry_date": "2024-07-01", "entry_price": 8580, "evidence_family": "second_wave_burnin_socket_HBM_test_theme_price_premium_without_customer_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_MICRO_SOCKET_BURNIN_PCB_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 3685, "peak_date": "2024-07-01", "peak_price": 9170, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/080/080580.json", "raw_component_score_breakdown": {"customer_order_or_design_win_visibility": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "memory_HBM_test_demand_relevance": 6, "relative_strength_quality": 5, "test_socket_customer_quality": 6, "total": 33, "utilization_delivery_cadence": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_080580_OKINS_20240701_SECOND_WAVE_BURNIN_SOCKET_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_customer_quality", "customer_order_or_design_win_visibility", "utilization_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_quality_and_order_conversion_required", "test_socket_or_test_board_delivery_cadence_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["second_wave_test_socket_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_design_win_gap", "utilization_or_delivery_gap", "margin_revision_bridge_failure"], "symbol": "080580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "trigger_date": "2024-07-01", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -60.33, "MAE_30D_pct": -18.5, "MAE_90D_pct": -48.5, "MFE_180D_pct": 4.02, "MFE_30D_pct": 4.02, "MFE_90D_pct": 4.02, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_098120_MICROCONTACT_20240426_SECOND_WAVE_TEST_SOCKET_FALSE_GREEN", "case_role": "second_wave_micro_test_socket_relative_strength_false_green_counterexample", "company_name": "마이크로컨텍솔", "corporate_action_window_status": "clean post-2011 corporate-action forward window; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Second-wave micro test-socket price confirmation should remain Yellow or local 4B when the stock lacks fresh customer-quality, direct order conversion, utilization and margin/revision evidence. The April 2024 trigger had very small residual upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.86, "entry_date": "2024-04-26", "entry_price": 10700, "evidence_family": "second_wave_micro_test_socket_price_confirmation_without_customer_quality_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SECOND_WAVE_MICRO_SOCKET_BURNIN_PCB_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 4245, "peak_date": "2024-04-29", "peak_price": 11130, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/098/098120.json", "raw_component_score_breakdown": {"customer_order_or_design_win_visibility": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "memory_HBM_test_demand_relevance": 5, "relative_strength_quality": 4, "test_socket_customer_quality": 5, "total": 30, "utilization_delivery_cadence": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_098120_MICROCONTACT_20240426_SECOND_WAVE_TEST_SOCKET_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_customer_quality", "customer_order_or_design_win_visibility", "utilization_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_quality_and_order_conversion_required", "test_socket_or_test_board_delivery_cadence_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["second_wave_test_socket_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_design_win_gap", "utilization_or_delivery_gap", "margin_revision_bridge_failure"], "symbol": "098120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "trigger_date": "2024-04-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SECOND_WAVE_MICRO_SOCKET_BURNIN_PCB_CUSTOMER_QUALITY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "semi_test_socket_customer_quality_second_wave_micro_socket_burnin_pcb_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 second-wave test-socket rows should preserve local 4B/Yellow after customer-quality optionality is capitalized: Green requires renewed customer order/design-win evidence, delivery cadence, utilization and margin-revision bridge, not price continuation or theme recall.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C08 + symbol + trigger_type + entry_date.
3. Preserve local 4B/Yellow discipline for second-wave test-socket moves after customer-quality optionality is capitalized.
4. Add C08-specific semi test-socket / customer-quality / direct order-design-win / delivery cadence / utilization / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C08_STAGE2_ALLOWED_ON_CUSTOMER_ORDER_DESIGNWIN_DELIVERY_MARGIN_REVISION_BRIDGE
- C08_GREEN_REQUIRES_CUSTOMER_QUALITY_UTILIZATION_MARGIN_AND_VALUATION_RUNWAY
- C08_SECOND_WAVE_TEST_SOCKET_PRICE_PREMIUM_LOCAL_4B
- C08_PRICE_CONFIRMATION_WITHOUT_CUSTOMER_QUALITY_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

