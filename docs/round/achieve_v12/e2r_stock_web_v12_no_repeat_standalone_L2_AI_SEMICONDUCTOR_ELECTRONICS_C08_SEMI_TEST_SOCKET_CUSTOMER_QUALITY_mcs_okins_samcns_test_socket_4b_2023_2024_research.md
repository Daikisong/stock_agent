# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semi test socket customer-quality / smallcap 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: SMALLCAP_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_mcs_okins_samcns_test_socket_4b_2023_2024_research.md
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

This run avoids those top-covered C08 symbols and adds 098120, 080580, and 252990.  
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
098120 마이크로컨텍솔: selected 2023 forward window clean; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window.
080580 오킨스전자: selected 2024 forward window clean; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window.
252990 샘씨엔에스: corporate_action_candidate_count=0.
```

## 3. Research thesis

C08 should not treat every semi socket/probe-card price move as customer-quality proof. It should test whether the theme becomes qualified and recurring demand:

```text
test socket / probe-card customer-quality attention
→ customer qualification and repeat purchase
→ HBM or high-end device mix
→ utilization, ASP and gross margin
→ revision bridge
→ rerating or local 4B cap
```

A socket order is a fitting test. Green should not pay for the socket being tried; it should require the customer to keep ordering, the line to stay utilized, and the ASP/margin bridge to hold.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C08_098120_MCS_20230330_TEST_SOCKET_CUSTOMER_QUALITY_STAGE2 | 098120 | positive_test_socket_customer_quality_stage2_success_with_later_4b_watch | 2023-03-30 | 7580 | 14650 on 2023-11-17 | 6210 on 2023-05-15 | 8.05% | 29.29% | 93.27% | -18.07% | -18.7% |
| C08_080580_OKINS_20240123_TEST_SOCKET_THEME_PREMIUM_4B | 080580 | test_socket_theme_price_premium_counterexample | 2024-01-23 | 13770 | 14910 on 2024-01-23 | 4945 on 2024-09-09 | 8.28% | 8.28% | 8.28% | -64.09% | -66.83% |
| C08_252990_SAMCNS_20240206_PROBE_CARD_STF_FALSE_GREEN | 252990 | probe_card_stf_customer_quality_false_green_counterexample | 2024-02-06 | 8160 | 8840 on 2024-02-07 | 4750 on 2024-09-11 | 8.33% | 8.33% | 8.33% | -41.79% | -46.27% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 098120 is the positive anchor. The March 2023 test-socket route produced a large 180D MFE as the market began to price a smaller socket supplier's customer-quality and margin leverage.
- Stage2 is allowed only when the non-price bridge is visible: customer qualification, repeat order probability, product mix, utilization and margin revision.

### Stage3 / Green
- C08 Green should require customer qualification, repeat purchase, high-end device mix, utilization, ASP, gross margin and revision confirmation.
- 252990 is the false-Green guard. Probe-card ceramic STF price confirmation did not prevent a later drawdown because customer-quality and utilization/margin evidence had not kept expanding.

### 4B
- 080580 fills a clean 4B gap. The January 2024 socket/connector premium had its forward-window high on the trigger day and then suffered a deep post-peak drawdown.
- 252990 adds a Yellow-to-4B counterexample: the February 2024 spike had modest immediate upside but needed customer and utilization evidence before Green.
- 098120 also demonstrates the Stage2-to-4B transition after a successful rerating. Once the November premium was paid, fresh non-price proof was required.

### 4C
- No hard customer loss, product qualification failure or accounting break is asserted.
- The C08 break mode is customer-quality evidence exhaustion: the socket/probe-card story remains plausible, but qualification, repeat orders, utilization, ASP and gross-margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C08_080580_OKINS_20240123_TEST_SOCKET_THEME_PREMIUM_4B": {
    "customer_quality_visibility": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "socket_order_repeatability": 3,
    "total": 20,
    "utilization_product_mix": 3,
    "valuation_rerating_runway": 1
  },
  "C08_098120_MCS_20230330_TEST_SOCKET_CUSTOMER_QUALITY_STAGE2": {
    "customer_quality_visibility": 9,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 9,
    "socket_order_repeatability": 8,
    "total": 51,
    "utilization_product_mix": 7,
    "valuation_rerating_runway": 7
  },
  "C08_252990_SAMCNS_20240206_PROBE_CARD_STF_FALSE_GREEN": {
    "customer_quality_visibility": 5,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 5,
    "socket_order_repeatability": 4,
    "total": 25,
    "utilization_product_mix": 4,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C08 guard:
```text
if test_socket_attention and customer_qualification_repeat_order_margin_bridge_visible:
    allow_stage2_actionable = true

if socket_or_probe_card_price_premium and no incremental_customer_quality_utilization_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and customer_quality_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 080580 / 2024-01-23: socket/connector theme premium can be over-promoted if price heat substitutes for customer qualification and margin proof.
- 252990 / 2024-02-06: probe-card STF recovery can look like Green, but fails without repeat customer demand, utilization and gross-margin revision.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -18.07, "MAE_30D_pct": -18.07, "MAE_90D_pct": -18.07, "MFE_180D_pct": 93.27, "MFE_30D_pct": 8.05, "MFE_90D_pct": 29.29, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_098120_MCS_20230330_TEST_SOCKET_CUSTOMER_QUALITY_STAGE2", "case_role": "positive_test_socket_customer_quality_stage2_success_with_later_4b_watch", "company_name": "마이크로컨텍솔", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when test-socket/customer-quality attention attached to a smaller socket supplier before the November 2023 rerating. Green still requires customer qualification, repeat purchase, product mix, utilization, ASP and margin/revision bridge; after the November spike, the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -18.7, "entry_date": "2023-03-30", "entry_price": 7580, "evidence_family": "test_socket_customer_quality_smallcap_socket_order_margin_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "SMALLCAP_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2023-05-15", "low_price_180d": 6210, "peak_date": "2023-11-17", "peak_price": 14650, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/098/098120.json", "raw_component_score_breakdown": {"customer_quality_visibility": 9, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 9, "socket_order_repeatability": 8, "total": 51, "utilization_product_mix": 7, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C08_098120_MCS_20230330_TEST_SOCKET_CUSTOMER_QUALITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_or_probe_card_attention", "customer_quality_or_qualification_visibility", "repeat_order_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_repeat_purchase_required", "HBM_or_high_end_device_mix_required", "utilization_ASP_gross_margin_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_probe_card_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_repeat_order_gap", "utilization_or_product_mix_disappointment", "margin_revision_bridge_failure"], "symbol": "098120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2023.csv", "trigger_date": "2023-03-30", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -64.09, "MAE_30D_pct": -27.74, "MAE_90D_pct": -53.74, "MFE_180D_pct": 8.28, "MFE_30D_pct": 8.28, "MFE_90D_pct": 8.28, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_080580_OKINS_20240123_TEST_SOCKET_THEME_PREMIUM_4B", "case_role": "test_socket_theme_price_premium_counterexample", "company_name": "오킨스전자", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Test-socket/connector theme price premium should route to local 4B or counterexample unless customer qualification, repeat orders, HBM/device mix, utilization, ASP and margin/revision evidence refresh after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -66.83, "entry_date": "2024-01-23", "entry_price": 13770, "evidence_family": "test_socket_connector_price_premium_without_customer_qualification_repeat_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SMALLCAP_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 4945, "peak_date": "2024-01-23", "peak_price": 14910, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/080/080580.json", "raw_component_score_breakdown": {"customer_quality_visibility": 4, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "socket_order_repeatability": 3, "total": 20, "utilization_product_mix": 3, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_080580_OKINS_20240123_TEST_SOCKET_THEME_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_or_probe_card_attention", "customer_quality_or_qualification_visibility", "repeat_order_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_repeat_purchase_required", "HBM_or_high_end_device_mix_required", "utilization_ASP_gross_margin_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_probe_card_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_repeat_order_gap", "utilization_or_product_mix_disappointment", "margin_revision_bridge_failure"], "symbol": "080580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "trigger_date": "2024-01-23", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.79, "MAE_30D_pct": -21.81, "MAE_90D_pct": -26.72, "MFE_180D_pct": 8.33, "MFE_30D_pct": 8.33, "MFE_90D_pct": 8.33, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_252990_SAMCNS_20240206_PROBE_CARD_STF_FALSE_GREEN", "case_role": "probe_card_stf_customer_quality_false_green_counterexample", "company_name": "샘씨엔에스", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Probe-card ceramic STF/customer-quality recovery should stay Yellow or route to local 4B when price confirmation is not followed by customer qualification, socket/probe-card repeat demand, utilization, product mix, gross margin and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.27, "entry_date": "2024-02-06", "entry_price": 8160, "evidence_family": "probe_card_ceramic_stf_price_confirmation_without_customer_quality_utilization_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SMALLCAP_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-11", "low_price_180d": 4750, "peak_date": "2024-02-07", "peak_price": 8840, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/252/252990.json", "raw_component_score_breakdown": {"customer_quality_visibility": 5, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 5, "socket_order_repeatability": 4, "total": 25, "utilization_product_mix": 4, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_252990_SAMCNS_20240206_PROBE_CARD_STF_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["semi_test_socket_or_probe_card_attention", "customer_quality_or_qualification_visibility", "repeat_order_utilization_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_repeat_purchase_required", "HBM_or_high_end_device_mix_required", "utilization_ASP_gross_margin_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_probe_card_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_repeat_order_gap", "utilization_or_product_mix_disappointment", "margin_revision_bridge_failure"], "symbol": "252990", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv", "trigger_date": "2024-02-06", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SMALLCAP_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "semi_test_socket_customer_quality_smallcap_socket_probe_card_4b_gap",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 semi test-socket/customer-quality rows should allow Stage2 when socket/probe-card demand is backed by customer qualification, repeat orders, high-end device mix, utilization and margin/revision bridge; test-socket or probe-card price premium without fresh customer-quality evidence should route to local 4B or counterexample.",
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
3. Add C08-specific semi test-socket / probe-card customer-quality / repeat-order / utilization / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C08_STAGE2_ALLOWED_ON_CUSTOMER_QUALIFICATION_REPEAT_ORDER_MARGIN_BRIDGE
- C08_GREEN_REQUIRES_CUSTOMER_QUALITY_HIGH_END_MIX_UTILIZATION_ASP_REVISION
- C08_SOCKET_PROBE_CARD_PRICE_PREMIUM_LOCAL_4B
- C08_PRICE_CONFIRMATION_WITHOUT_CUSTOMER_QUALITY_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

