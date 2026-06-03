# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semi test socket customer quality / late-2024 rerate decay 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: LATE_2024_TEST_SOCKET_RERATE_DECAY_4B_GUARD
loop_objective: coverage_gap_fill|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_gap_fill|late_cycle_customer_quality_to_order_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_late_2024_test_socket_rerate_decay_4b_research.md
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

This run avoids those top-covered C08 symbols and uses new late-2024 hard keys:
```text
C08 + 080580 + 4B-local-price-only + 2024-09-12
C08 + 098120 + Stage3-Yellow + 2024-09-26
C08 + 219130 + 4B-local-price-only + 2024-08-27
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
080580 오킨스전자: selected post-2021 forward window clean; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window.
098120 마이크로컨텍솔: selected post-2011 forward window clean; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window.
219130 타이거일렉: corporate_action_candidate_count=0; clean 2024/2025 forward window.
```

## 3. Research thesis

C08 should distinguish fresh semi test-socket customer quality from late-cycle customer-quality optionality already paid in price:

```text
semi test socket / burn-in socket / test PCB customer-quality signal
→ direct customer order or design-win visibility
→ delivery cadence and utilization
→ memory/HBM test-demand relevance
→ ASP/mix and gross margin bridge
→ Stage2/Green or local 4B cap
```

A test socket story is a probe touching the chip. Stage2 can buy it when the signal reaches customer order and margin revision. In the late cycle, Green should require a new signal, not just the echo of the first spark.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C08_080580_OKINS_20240912_LATE_TEST_SOCKET_THEME_4B | 080580 | protective_late_test_socket_theme_4b_success | 2024-09-12 | 5750 | 6800 on 2024-09-26 | 3685 on 2024-12-09 | 18.26% | 18.26% | 18.26% | -35.91% | -45.81% |
| C08_098120_MICROCONTACT_20240926_LATE_TEST_SOCKET_FALSE_GREEN | 098120 | late_micro_test_socket_false_green_counterexample | 2024-09-26 | 5920 | 6210 on 2024-09-27 | 4245 on 2024-12-09 | 4.9% | 4.9% | 4.9% | -28.29% | -31.64% |
| C08_219130_TIGERELEC_20240827_TEST_PCB_RERATE_DECAY_4B | 219130 | test_pcb_customer_quality_rerate_decay_counterexample | 2024-08-27 | 23150 | 23650 on 2024-08-30 | 9700 on 2025-04-07 | 2.16% | 2.16% | 2.16% | -58.1% | -58.99% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a fresh clean Stage2/Green positive.
- C08 Green should require customer quality, order/design-win conversion, test-board/socket delivery cadence, utilization, margin revision and valuation runway.
- 098120 is the false-Green/Yellow guard: late test-socket price confirmation was visible, but direct customer/order and margin evidence did not refresh; residual upside was small compared with forward MAE.

### 4B
- 080580 is the protective 4B anchor. The late theme rebound had brief MFE but still lacked fresh customer-order and margin evidence.
- 219130 shows a rerate-decay failure after earlier valid Stage2 behavior. The late-August trigger had almost no residual runway and a deep drawdown.
- The core 4B rule is that late price rebound after the customer-quality rerating must not be promoted to Green unless fresh customer evidence appears.

### 4C
- No hard customer cancellation, design-win loss, accounting break or shipment collapse is asserted.
- The C08 break mode is customer-quality exhaustion: the test-socket theme may remain directionally relevant, but incremental customer order, delivery cadence, utilization and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C08_080580_OKINS_20240912_LATE_TEST_SOCKET_THEME_4B": {
    "customer_order_or_design_win_visibility": 2,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "memory_HBM_test_demand_relevance": 5,
    "relative_strength_quality": 4,
    "test_socket_customer_quality": 5,
    "total": 27,
    "utilization_delivery_cadence": 2,
    "valuation_rerating_runway": 1
  },
  "C08_098120_MICROCONTACT_20240926_LATE_TEST_SOCKET_FALSE_GREEN": {
    "customer_order_or_design_win_visibility": 2,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "memory_HBM_test_demand_relevance": 4,
    "relative_strength_quality": 3,
    "test_socket_customer_quality": 4,
    "total": 25,
    "utilization_delivery_cadence": 2,
    "valuation_rerating_runway": 1
  },
  "C08_219130_TIGERELEC_20240827_TEST_PCB_RERATE_DECAY_4B": {
    "customer_order_or_design_win_visibility": 2,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "memory_HBM_test_demand_relevance": 5,
    "relative_strength_quality": 3,
    "test_socket_customer_quality": 5,
    "total": 27,
    "utilization_delivery_cadence": 2,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C08 guard:
```text
if semi_test_socket_customer_quality and direct_order_designwin_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if late_test_socket_price_premium and no incremental_customer_order_utilization_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and customer_quality_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 098120 / 2024-09-26: late micro test-socket confirmation can look like Yellow-to-Green, but fails without renewed customer-quality and revision bridge.
- 219130 / 2024-08-27: test-PCB rerate decay can be over-promoted if price rebound substitutes for fresh customer order and margin proof.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -35.91, "MAE_30D_pct": -10.43, "MAE_90D_pct": -35.91, "MFE_180D_pct": 18.26, "MFE_30D_pct": 18.26, "MFE_90D_pct": 18.26, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_080580_OKINS_20240912_LATE_TEST_SOCKET_THEME_4B", "case_role": "protective_late_test_socket_theme_4b_success", "company_name": "오킨스전자", "corporate_action_window_status": "clean post-2021 corporate-action forward window; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful on the late-2024 burn-in socket/test theme rebound. The move had non-price theme context but no fresh enough direct customer order, design-win, utilization, delivery cadence or margin/revision bridge. The forward path produced a brief local MFE and then a much larger drawdown, so the trigger should remain 4B rather than Stage2/Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.81, "entry_date": "2024-09-12", "entry_price": 5750, "evidence_family": "late_2024_burnin_socket_HBM_test_theme_price_premium_without_customer_order_margin_revision_refresh", "evidence_url_pending": false, "fine_archetype_id": "LATE_2024_TEST_SOCKET_RERATE_DECAY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 3685, "peak_date": "2024-09-26", "peak_price": 6800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/080/080580.json", "raw_component_score_breakdown": {"customer_order_or_design_win_visibility": 2, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "memory_HBM_test_demand_relevance": 5, "relative_strength_quality": 4, "test_socket_customer_quality": 5, "total": 27, "utilization_delivery_cadence": 2, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_080580_OKINS_20240912_LATE_TEST_SOCKET_THEME_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_customer_quality", "customer_order_or_design_win_visibility", "utilization_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_quality_and_order_conversion_required", "test_socket_or_test_board_delivery_cadence_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["late_test_socket_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_design_win_gap", "utilization_or_delivery_gap", "margin_revision_bridge_failure"], "symbol": "080580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "trigger_date": "2024-09-12", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -28.29, "MAE_30D_pct": -13.01, "MAE_90D_pct": -28.29, "MFE_180D_pct": 4.9, "MFE_30D_pct": 4.9, "MFE_90D_pct": 4.9, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_098120_MICROCONTACT_20240926_LATE_TEST_SOCKET_FALSE_GREEN", "case_role": "late_micro_test_socket_false_green_counterexample", "company_name": "마이크로컨텍솔", "corporate_action_window_status": "clean post-2011 corporate-action forward window; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late micro test-socket price confirmation should remain Yellow or local 4B when the stock lacks renewed customer-quality evidence, direct order conversion, utilization and margin/revision bridge. The late-September trigger had minimal residual upside and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.64, "entry_date": "2024-09-26", "entry_price": 5920, "evidence_family": "late_2024_micro_test_socket_price_confirmation_without_customer_quality_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "LATE_2024_TEST_SOCKET_RERATE_DECAY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 4245, "peak_date": "2024-09-27", "peak_price": 6210, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/098/098120.json", "raw_component_score_breakdown": {"customer_order_or_design_win_visibility": 2, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "memory_HBM_test_demand_relevance": 4, "relative_strength_quality": 3, "test_socket_customer_quality": 4, "total": 25, "utilization_delivery_cadence": 2, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_098120_MICROCONTACT_20240926_LATE_TEST_SOCKET_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_customer_quality", "customer_order_or_design_win_visibility", "utilization_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_quality_and_order_conversion_required", "test_socket_or_test_board_delivery_cadence_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["late_test_socket_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_design_win_gap", "utilization_or_delivery_gap", "margin_revision_bridge_failure"], "symbol": "098120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "trigger_date": "2024-09-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -58.1, "MAE_30D_pct": -22.98, "MAE_90D_pct": -39.96, "MFE_180D_pct": 2.16, "MFE_30D_pct": 2.16, "MFE_90D_pct": 2.16, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_219130_TIGERELEC_20240827_TEST_PCB_RERATE_DECAY_4B", "case_role": "test_pcb_customer_quality_rerate_decay_counterexample", "company_name": "타이거일렉", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_2025_forward_window", "current_profile_error": true, "current_profile_verdict": "Test-interface PCB/customer-quality rerate decay should route to local 4B/counterexample when the earlier customer-quality story has already been capitalized and no fresh direct order, design-win, delivery cadence, utilization or margin/revision evidence appears. The late-August trigger had almost no residual upside and a deep forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -58.99, "entry_date": "2024-08-27", "entry_price": 23150, "evidence_family": "test_pcb_customer_quality_rerate_decay_without_incremental_order_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "LATE_2024_TEST_SOCKET_RERATE_DECAY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2025-04-07", "low_price_180d": 9700, "peak_date": "2024-08-30", "peak_price": 23650, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/219/219130.json", "raw_component_score_breakdown": {"customer_order_or_design_win_visibility": 2, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "memory_HBM_test_demand_relevance": 5, "relative_strength_quality": 3, "test_socket_customer_quality": 5, "total": 27, "utilization_delivery_cadence": 2, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_219130_TIGERELEC_20240827_TEST_PCB_RERATE_DECAY_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_customer_quality", "customer_order_or_design_win_visibility", "utilization_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_quality_and_order_conversion_required", "test_socket_or_test_board_delivery_cadence_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["late_test_socket_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_design_win_gap", "utilization_or_delivery_gap", "margin_revision_bridge_failure"], "symbol": "219130", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv", "trigger_date": "2024-08-27", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "LATE_2024_TEST_SOCKET_RERATE_DECAY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "semi_test_socket_customer_quality_late_2024_rerate_decay_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 late-cycle test-socket rows should preserve local 4B/Yellow after customer-quality optionality has been capitalized: Green requires renewed customer order/design-win evidence, delivery cadence, utilization and margin-revision bridge, not late price rebound or theme recall.",
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
3. Preserve local 4B/Yellow discipline for late-cycle test-socket moves after customer-quality optionality is capitalized.
4. Add C08-specific semi test-socket / customer-quality / direct order-design-win / delivery cadence / utilization / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C08_STAGE2_ALLOWED_ON_CUSTOMER_ORDER_DESIGNWIN_DELIVERY_MARGIN_REVISION_BRIDGE
- C08_GREEN_REQUIRES_CUSTOMER_QUALITY_UTILIZATION_MARGIN_AND_VALUATION_RUNWAY
- C08_LATE_TEST_SOCKET_PRICE_PREMIUM_LOCAL_4B
- C08_RERATE_DECAY_WITHOUT_CUSTOMER_QUALITY_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

