# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semi test socket / customer-quality guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_SMALLCAP_CUSTOMER_QUALITY_ORDER_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_test_socket_smallcap_customer_quality_2024_research.md
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

This run avoids those top-covered C08 symbols and adds 219130, 080580, and 098120.  
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
219130 타이거일렉: corporate_action_candidate_count=0.
080580 오킨스전자: 2024 forward window clean; corporate-action candidates are in 2021, outside the selected test window.
098120 마이크로컨텍솔: 2024 forward window clean; corporate-action candidates are in 2011, outside the selected test window.
```

## 3. Research thesis

C08 should not be a generic semiconductor small-cap momentum bucket. It should test whether customer-quality language becomes confirmed socket/order economics:

```text
test socket / probe PCB / customer-quality attention
→ customer qualification and socket demand
→ order conversion and delivery schedule
→ ASP, mix, margin and revision bridge
→ rerating
```

The key distinction is between a sample pass and a production socket. A sample can make the stock glow; production orders and margin are what keep the socket warm.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C08_219130_TIGERIL_20240213_TEST_SOCKET_PCB_CUSTOMER_QUALITY_STAGE2 | 219130 | positive_test_socket_pcb_customer_quality_stage2_success_with_later_4b | 2024-02-13 | 28250 | 45300 on 2024-05-14 | 12470 on 2024-11-19 | 51.86% | 60.35% | 60.35% | -55.86% | -72.47% |
| C08_080580_OKINS_20240122_TEST_SOCKET_THEME_PRICE_PREMIUM_4B | 080580 | test_socket_theme_price_premium_counterexample | 2024-01-22 | 12930 | 14910 on 2024-01-23 | 4945 on 2024-09-09 | 15.31% | 15.31% | 15.31% | -61.76% | -73.61% |
| C08_098120_MICROCONTACT_20240426_SOCKET_CUSTOMER_QUALITY_FALSE_GREEN | 098120 | socket_customer_quality_false_green_counterexample | 2024-04-26 | 10700 | 11130 on 2024-04-29 | 4315 on 2024-12-06 | 4.02% | 4.02% | 4.02% | -59.67% | -61.23% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Test socket, probe-PCB and customer-quality attention can be valid Stage2 routes.
- 219130 is the positive anchor: the February 2024 route produced a strong MFE before the later unwind. The useful signal was relative strength tied to customer-quality/socket demand, not generic semiconductor beta.

### Stage3 / Green
- C08 Green should require confirmed customer quality, order conversion, delivery schedule, ASP/mix margin and revision evidence.
- 098120 shows why a socket/customer-quality label should not be promoted when the order and margin bridge is not improving. The forward path had little additional MFE and large MAE.

### 4B
- 080580 fills the missing local 4B pocket. The HBM/test-socket theme premium was already capitalized by the January spike, and the following path argues for risk control rather than fresh Green.
- 219130 also required later 4B discipline after the Stage2 success matured into a price-premium state.

### 4C
- No hard accounting or customer-cancellation break is asserted.
- The C08 break mode is conversion failure: customer-quality language remains plausible, but production order, delivery cadence, ASP/mix margin and revisions do not support the valuation.

## 6. Raw component score breakdown

```json
{
  "C08_080580_OKINS_20240122_TEST_SOCKET_THEME_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C08_098120_MICROCONTACT_20240426_SOCKET_CUSTOMER_QUALITY_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 28,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C08_219130_TIGERIL_20240213_TEST_SOCKET_PCB_CUSTOMER_QUALITY_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 56,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C08 guard:
```text
if test_socket_customer_quality_attention and early_order_quality_visibility:
    allow_stage2_actionable = true

if socket_theme_price_premium and no confirmed_customer_quality_order_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and order_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 080580 / 2024-01-22: small-cap HBM/test-socket price premium can be over-promoted if the model treats theme heat as customer-quality/order evidence.
- 098120 / 2024-04-26: socket customer-quality claims can look like Green, but the later path argues for Yellow/counterexample unless order conversion and margin revision close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -55.86, "MAE_30D_pct": -6.9, "MAE_90D_pct": -6.9, "MFE_180D_pct": 60.35, "MFE_30D_pct": 51.86, "MFE_90D_pct": 60.35, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_219130_TIGERIL_20240213_TEST_SOCKET_PCB_CUSTOMER_QUALITY_STAGE2", "case_role": "positive_test_socket_pcb_customer_quality_stage2_success_with_later_4b", "company_name": "타이거일렉", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when test-socket/PCB customer-quality attention separated from generic semiconductor beta, but Green still requires confirmed customer quality, order conversion, margin and revision evidence; later local 4B was required after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -72.47, "entry_date": "2024-02-13", "entry_price": 28250, "evidence_family": "test_socket_pcb_hbm_customer_quality_relative_strength_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_SMALLCAP_CUSTOMER_QUALITY_ORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-19", "low_price_180d": 12470, "peak_date": "2024-05-14", "peak_price": 45300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/219/219130.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 56, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C08_219130_TIGERIL_20240213_TEST_SOCKET_PCB_CUSTOMER_QUALITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_pcb_customer_quality_attention", "hbm_memory_customer_qualification_or_socket_demand_claim", "relative_strength_after_customer_quality_signal"], "stage3_evidence_fields": ["confirmed_customer_quality_required", "order_conversion_and_delivery_schedule_required", "ASP_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_hbm_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_gap", "order_or_delivery_conversion_failure", "margin_revision_bridge_failure"], "symbol": "219130", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv", "trigger_date": "2024-02-13", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -61.76, "MAE_30D_pct": -29.54, "MAE_90D_pct": -52.98, "MFE_180D_pct": 15.31, "MFE_30D_pct": 15.31, "MFE_90D_pct": 15.31, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_080580_OKINS_20240122_TEST_SOCKET_THEME_PRICE_PREMIUM_4B", "case_role": "test_socket_theme_price_premium_counterexample", "company_name": "오킨스전자", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Small-cap test-socket/HBM theme premium should route to local 4B or counterexample unless customer qualification, socket order quality, delivery and margin/revision evidence are explicit.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -73.61, "entry_date": "2024-01-22", "entry_price": 12930, "evidence_family": "test_socket_hbm_theme_price_premium_without_customer_quality_order_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_SMALLCAP_CUSTOMER_QUALITY_ORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 4945, "peak_date": "2024-01-23", "peak_price": 14910, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/080/080580.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C08_080580_OKINS_20240122_TEST_SOCKET_THEME_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_pcb_customer_quality_attention", "hbm_memory_customer_qualification_or_socket_demand_claim", "relative_strength_after_customer_quality_signal"], "stage3_evidence_fields": ["confirmed_customer_quality_required", "order_conversion_and_delivery_schedule_required", "ASP_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_hbm_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_gap", "order_or_delivery_conversion_failure", "margin_revision_bridge_failure"], "symbol": "080580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "trigger_date": "2024-01-22", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -59.67, "MAE_30D_pct": -16.64, "MAE_90D_pct": -52.52, "MFE_180D_pct": 4.02, "MFE_30D_pct": 4.02, "MFE_90D_pct": 4.02, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_098120_MICROCONTACT_20240426_SOCKET_CUSTOMER_QUALITY_FALSE_GREEN", "case_role": "socket_customer_quality_false_green_counterexample", "company_name": "마이크로컨텍솔", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Socket/customer-quality claims should stay Yellow if order conversion, delivery quality, ASP/mix margin and revision duration are not improving; price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.23, "entry_date": "2024-04-26", "entry_price": 10700, "evidence_family": "memory_test_socket_customer_quality_claim_without_order_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "TEST_SOCKET_SMALLCAP_CUSTOMER_QUALITY_ORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-06", "low_price_180d": 4315, "peak_date": "2024-04-29", "peak_price": 11130, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/098/098120.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 28, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C08_098120_MICROCONTACT_20240426_SOCKET_CUSTOMER_QUALITY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_pcb_customer_quality_attention", "hbm_memory_customer_qualification_or_socket_demand_claim", "relative_strength_after_customer_quality_signal"], "stage3_evidence_fields": ["confirmed_customer_quality_required", "order_conversion_and_delivery_schedule_required", "ASP_mix_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_hbm_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_gap", "order_or_delivery_conversion_failure", "margin_revision_bridge_failure"], "symbol": "098120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "trigger_date": "2024-04-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TEST_SOCKET_SMALLCAP_CUSTOMER_QUALITY_ORDER_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "semi_test_socket_customer_quality_new_symbols_and_4b_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 semi test-socket/customer-quality rows should allow Stage2 when customer qualification and socket demand relative strength appears early, but Stage3 Green requires confirmed customer quality, order conversion, delivery schedule, ASP/mix margin and revision bridge; small-cap HBM/socket price premium without customer-quality proof should route to local 4B or counterexample.",
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
3. Add C08-specific test-socket/customer-quality/order-conversion/margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C08_STAGE2_ALLOWED_ON_EARLY_CUSTOMER_QUALITY_SOCKET_ORDER_VISIBILITY
- C08_GREEN_REQUIRES_CUSTOMER_QUALITY_ORDER_DELIVERY_MARGIN_REVISION
- C08_SOCKET_THEME_PRICE_PREMIUM_LOCAL_4B
- C08_SOCKET_QUALITY_WITHOUT_ORDER_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

