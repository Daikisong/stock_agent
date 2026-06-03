# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semiconductor test socket customer-quality guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_CUSTOMER_QUALITY_UTILIZATION_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_test_socket_customer_quality_2023_2024_research.md
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

This run avoids those top-covered C08 symbols and adds 098120, 080580, and 131970.  
Each row uses a new `C08 + symbol + trigger_type + entry_date` hard key.

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
098120 마이크로컨텍솔: 2023/2024 forward window clean; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window.
080580 오킨스전자: 2024 forward window clean; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window.
131970 두산테스나: 2024 forward window clean; corporate-action candidates are 2020-09-15 and 2020-10-07, outside selected test window.
```

## 3. Research thesis

C08 should not treat every semiconductor test/socket move as high-quality customer conversion. It should test whether test exposure becomes repeat qualified demand:

```text
test socket / semiconductor test customer-quality attention
→ high-end customer qualification
→ repeat order or utilization cadence
→ ASP/mix and gross-margin bridge
→ revision confirmation
→ rerating
```

A socket is small, but the gate is narrow. Stage2 can follow the first evidence that the customer has entered the gate. Green should require repeat passage: qualified sockets, utilization, ASP/mix and margin revisions.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C08_098120_MCS_20230522_TEST_SOCKET_CUSTOMER_QUALITY_STAGE2 | 098120 | positive_test_socket_customer_quality_stage2_success_with_later_4b | 2023-05-22 | 7530 | 15020 on 2023-12-22 | 6560 on 2023-08-17 | 19.65% | 51.26% | 99.47% | -12.88% | -30.69% |
| C08_080580_OKINS_20240123_TEST_SOCKET_PRICE_PREMIUM_4B | 080580 | test_socket_smallcap_price_premium_counterexample | 2024-01-23 | 13770 | 14910 on 2024-01-23 | 4865 on 2024-08-05 | 8.28% | 8.28% | 8.28% | -64.67% | -67.37% |
| C08_131970_DOOSANTESNA_20240405_TEST_SERVICE_CUSTOMER_QUALITY_FALSE_GREEN | 131970 | test_service_customer_quality_false_green_counterexample | 2024-04-05 | 51500 | 53300 on 2024-04-05 | 22750 on 2024-12-06 | 3.5% | 3.5% | 3.5% | -55.83% | -57.32% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Test socket customer-quality signals can be valid Stage2 routes when customer qualification, memory-cycle recovery and order/reorder visibility appear before the valuation fully capitalizes the cycle.
- 098120 is the positive anchor: the May 2023 test-socket route produced a large forward MFE with moderate early MAE. The December 2023 premium then required 4B discipline because the same evidence had to be refreshed with customer mix, repeat orders and margin revisions.

### Stage3 / Green
- C08 Green should require high-end socket customer mix, repeat orders, utilization, ASP/mix, gross margin and revision confirmation.
- 131970 shows the test-service variant: price confirmation after a semiconductor test-quality story was not enough when utilization, capex burden, customer concentration and revision evidence did not keep improving.

### 4B
- 080580 fills the missing C08 local 4B pocket. The January 2024 test-socket small-cap spike had little forward upside and then fell sharply as customer/reorder evidence did not carry the price.
- 098120 also moved from valid Stage2 into 4B watch after the December 2023 rerating became a fully capitalized socket/customer-quality story.

### 4C
- No hard customer cancellation or accounting break is asserted.
- The C08 break mode is evidence exhaustion: the test/socket story remains plausible, but customer qualification, repeat orders, utilization, ASP/mix, margin and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C08_080580_OKINS_20240123_TEST_SOCKET_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C08_098120_MCS_20230522_TEST_SOCKET_CUSTOMER_QUALITY_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 52,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  },
  "C08_131970_DOOSANTESNA_20240405_TEST_SERVICE_CUSTOMER_QUALITY_FALSE_GREEN": {
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

Suggested C08 guard:
```text
if test_socket_customer_quality_attention and repeat_order_utilization_margin_bridge_visible:
    allow_stage2_actionable = true

if test_socket_price_premium and no incremental_customer_mix_reorder_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and customer_or_utilization_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 080580 / 2024-01-23: test-socket small-cap price premium can be over-promoted if the model treats theme heat as customer qualification and repeat-order proof.
- 131970 / 2024-04-05: test-service customer-quality confirmation can look like Green, but the forward path argues for Yellow/counterexample unless utilization, ASP/mix and revision evidence close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.88, "MAE_30D_pct": -4.91, "MAE_90D_pct": -12.88, "MFE_180D_pct": 99.47, "MFE_30D_pct": 19.65, "MFE_90D_pct": 51.26, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_098120_MCS_20230522_TEST_SOCKET_CUSTOMER_QUALITY_STAGE2", "case_role": "positive_test_socket_customer_quality_stage2_success_with_later_4b", "company_name": "마이크로컨텍솔", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when test-socket customer quality, memory-cycle recovery and order/reorder visibility began to separate from generic semiconductor beta. Green still requires customer mix, high-end socket qualification, repeat orders, utilization, gross margin and revision bridge; after the December 2023 premium, the same evidence required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.69, "entry_date": "2023-05-22", "entry_price": 7530, "evidence_family": "test_socket_customer_quality_memory_recovery_smallcap_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_CUSTOMER_QUALITY_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2023-08-17", "low_price_180d": 6560, "peak_date": "2023-12-22", "peak_price": 15020, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/098/098120.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 52, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C08_098120_MCS_20230522_TEST_SOCKET_CUSTOMER_QUALITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_semiconductor_test_customer_quality_attention", "customer_qualification_or_repeat_order_signal", "utilization_ASP_mix_or_margin_revision_visibility"], "stage3_evidence_fields": ["high_end_socket_customer_mix_required", "repeat_order_and_utilization_required", "ASP_mix_gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_customer_quality_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_reorder_gap", "utilization_or_capex_burden_disappointment", "ASP_mix_margin_revision_bridge_failure"], "symbol": "098120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2023.csv", "trigger_date": "2023-05-22", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -64.67, "MAE_30D_pct": -27.74, "MAE_90D_pct": -44.88, "MFE_180D_pct": 8.28, "MFE_30D_pct": 8.28, "MFE_90D_pct": 8.28, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_080580_OKINS_20240123_TEST_SOCKET_PRICE_PREMIUM_4B", "case_role": "test_socket_smallcap_price_premium_counterexample", "company_name": "오킨스전자", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Test-socket small-cap price premium should route to local 4B or counterexample unless customer qualification, repeat order, utilization, ASP/mix margin and revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.37, "entry_date": "2024-01-23", "entry_price": 13770, "evidence_family": "test_socket_theme_price_premium_without_customer_quality_reorder_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_CUSTOMER_QUALITY_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-08-05", "low_price_180d": 4865, "peak_date": "2024-01-23", "peak_price": 14910, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/080/080580.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C08_080580_OKINS_20240123_TEST_SOCKET_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_semiconductor_test_customer_quality_attention", "customer_qualification_or_repeat_order_signal", "utilization_ASP_mix_or_margin_revision_visibility"], "stage3_evidence_fields": ["high_end_socket_customer_mix_required", "repeat_order_and_utilization_required", "ASP_mix_gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_customer_quality_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_reorder_gap", "utilization_or_capex_burden_disappointment", "ASP_mix_margin_revision_bridge_failure"], "symbol": "080580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "trigger_date": "2024-01-23", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -55.83, "MAE_30D_pct": -13.79, "MAE_90D_pct": -43.2, "MFE_180D_pct": 3.5, "MFE_30D_pct": 3.5, "MFE_90D_pct": 3.5, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_131970_DOOSANTESNA_20240405_TEST_SERVICE_CUSTOMER_QUALITY_FALSE_GREEN", "case_role": "test_service_customer_quality_false_green_counterexample", "company_name": "두산테스나", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2020-09-15 and 2020-10-07, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Semiconductor test-service customer-quality claims should stay Yellow when utilization, customer concentration quality, ASP/mix, capex burden, margin and revision evidence do not keep improving after the price confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -57.32, "entry_date": "2024-04-05", "entry_price": 51500, "evidence_family": "semiconductor_test_service_customer_quality_price_confirmation_without_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_CUSTOMER_QUALITY_UTILIZATION_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-06", "low_price_180d": 22750, "peak_date": "2024-04-05", "peak_price": 53300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/131/131970.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 28, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C08_131970_DOOSANTESNA_20240405_TEST_SERVICE_CUSTOMER_QUALITY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_semiconductor_test_customer_quality_attention", "customer_qualification_or_repeat_order_signal", "utilization_ASP_mix_or_margin_revision_visibility"], "stage3_evidence_fields": ["high_end_socket_customer_mix_required", "repeat_order_and_utilization_required", "ASP_mix_gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_customer_quality_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_reorder_gap", "utilization_or_capex_burden_disappointment", "ASP_mix_margin_revision_bridge_failure"], "symbol": "131970", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/131/131970/2024.csv", "trigger_date": "2024-04-05", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TEST_SOCKET_CUSTOMER_QUALITY_UTILIZATION_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "semi_test_socket_customer_quality_new_symbols_and_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 semiconductor test-socket/customer-quality rows should allow Stage2 on early test socket or test-service customer qualification and repeat-order visibility, but Stage3 Green requires high-end customer mix, utilization, ASP/mix, gross margin and revision bridge; test-socket price premium without customer/reorder proof should route to local 4B or counterexample.",
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
3. Add C08-specific semiconductor test-socket / customer-quality / utilization / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C08_STAGE2_ALLOWED_ON_CUSTOMER_QUALITY_REPEAT_ORDER_UTILIZATION_MARGIN_BRIDGE
- C08_GREEN_REQUIRES_HIGH_END_CUSTOMER_MIX_REPEAT_ORDER_ASP_MIX_MARGIN_REVISION
- C08_TEST_SOCKET_PRICE_PREMIUM_LOCAL_4B
- C08_TEST_SERVICE_WITHOUT_UTILIZATION_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

