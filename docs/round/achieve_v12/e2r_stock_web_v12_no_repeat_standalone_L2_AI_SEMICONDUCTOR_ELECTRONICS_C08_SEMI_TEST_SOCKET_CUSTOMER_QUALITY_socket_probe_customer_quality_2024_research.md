# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semi test socket customer-quality / socket-probe 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: SOCKET_PROBE_CUSTOMER_QUALITY_VOLUME_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|false_green_customer_quality_optional_value_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_socket_probe_customer_quality_2024_research.md
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

This run avoids those top-covered C08 symbols and adds 252990, 080580, and 098120.  
Each row uses a new `C08 + symbol + trigger_type + entry_date` hard key.

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
252990 샘씨엔에스: corporate_action_candidate_count=0; clean 2024 forward window.
080580 오킨스전자: selected 2024 forward window clean; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window.
098120 마이크로컨텍솔: selected 2024 forward window clean; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window.
```

## 3. Research thesis

C08 should separate fresh socket/probe-card customer-quality evidence from customer-quality optionality that is already capitalized:

```text
test socket / probe-card customer quality attention
→ named customer qualification or sample approval
→ sample-to-volume conversion and delivery cadence
→ yield/defect quality and ASP/mix
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A socket-quality headline is a sample on the engineer's bench. Stage2 can buy the sample becoming a production slot; Green should require the bench result to become volume, delivery, yield and revision.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C08_252990_SAMCNS_20240123_PROBE_CARD_CUSTOMER_QUALITY_STAGE2 | 252990 | positive_probe_card_customer_quality_stage2_success_with_later_4b_refresh | 2024-01-23 | 6860 | 9280 on 2024-04-18 | 5430 on 2024-10-23 | 28.86% | 35.28% | 35.28% | -20.85% | -41.49% |
| C08_080580_OKINS_20240123_SOCKET_THEME_FALSE_GREEN | 080580 | socket_customer_quality_theme_false_green_counterexample | 2024-01-23 | 13770 | 14910 on 2024-01-23 | 5470 on 2024-09-25 | 8.28% | 8.28% | 8.28% | -60.28% | -63.31% |
| C08_098120_MCS_20240426_TEST_SOCKET_PRICE_PREMIUM_4B | 098120 | test_socket_customer_quality_price_premium_counterexample | 2024-04-26 | 10700 | 11130 on 2024-04-29 | 4245 on 2024-12-09 | 4.02% | 4.02% | 4.02% | -60.33% | -61.86% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 252990 is the positive anchor. The January 2024 probe-card/substrate route produced meaningful MFE before the April premium required 4B refresh discipline.
- Stage2 is allowed only when non-price evidence connects customer-quality attention to qualification, sample-to-volume conversion, delivery cadence, yield/defect quality and revision visibility.

### Stage3 / Green
- C08 Green should require named customer qualification, volume conversion, quality/yield evidence, delivery cadence, ASP/mix and margin/revision confirmation.
- 080580 is the false-Green guard: socket theme price confirmation did not protect the forward path once qualification-to-volume and margin evidence failed to refresh.

### 4B
- 098120 fills the test-socket price-premium 4B pocket. The April 2024 trigger had small residual upside and then a much larger forward drawdown.
- 080580 shows the theme-stock version of the same failure: a quality narrative can remain plausible while the price already paid for too much without volume and margin proof.
- 252990 also shows that valid Stage2 can become local 4B after the rerating has already capitalized the customer-quality option.

### 4C
- No hard customer loss, tool rejection or accounting break is asserted.
- The C08 break mode is qualification-to-volume exhaustion: the customer-quality story may remain real, but incremental qualification, delivery cadence, yield and margin evidence no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C08_080580_OKINS_20240123_SOCKET_THEME_FALSE_GREEN": {
    "ASP_mix_bridge": 3,
    "capacity_delivery_cadence": 3,
    "customer_qualification_visibility": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "sample_to_volume_conversion": 3,
    "total": 26,
    "valuation_rerating_runway": 1,
    "yield_defect_quality": 3
  },
  "C08_098120_MCS_20240426_TEST_SOCKET_PRICE_PREMIUM_4B": {
    "ASP_mix_bridge": 3,
    "capacity_delivery_cadence": 3,
    "customer_qualification_visibility": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "sample_to_volume_conversion": 3,
    "total": 25,
    "valuation_rerating_runway": 1,
    "yield_defect_quality": 3
  },
  "C08_252990_SAMCNS_20240123_PROBE_CARD_CUSTOMER_QUALITY_STAGE2": {
    "ASP_mix_bridge": 7,
    "capacity_delivery_cadence": 8,
    "customer_qualification_visibility": 9,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 9,
    "sample_to_volume_conversion": 8,
    "total": 67,
    "valuation_rerating_runway": 7,
    "yield_defect_quality": 8
  }
}
```

## 7. Current calibrated profile stress test

Suggested C08 guard:
```text
if socket_probe_customer_quality and qualification_volume_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if socket_probe_price_premium and no incremental_qualification_volume_delivery_margin_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and qualification_to_volume_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 080580 / 2024-01-23: socket theme price confirmation can be over-promoted if the model treats price heat as qualification, volume and margin proof.
- 098120 / 2024-04-26: test-socket price premium can become price-only when incremental customer-quality and margin evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -20.85, "MAE_30D_pct": -2.33, "MAE_90D_pct": -7.0, "MFE_180D_pct": 35.28, "MFE_30D_pct": 28.86, "MFE_90D_pct": 35.28, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_252990_SAMCNS_20240123_PROBE_CARD_CUSTOMER_QUALITY_STAGE2", "case_role": "positive_probe_card_customer_quality_stage2_success_with_later_4b_refresh", "company_name": "샘씨엔에스", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when probe-card/substrate customer-quality and capacity/order visibility appeared before the rerating was fully capitalized. Green still requires named customer qualification, sample-to-volume conversion, delivery cadence, yield/defect quality, ASP/mix and margin/revision bridge; after the April 2024 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.49, "entry_date": "2024-01-23", "entry_price": 6860, "evidence_family": "probe_card_substrate_customer_quality_capacity_order_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "SOCKET_PROBE_CUSTOMER_QUALITY_VOLUME_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-10-23", "low_price_180d": 5430, "peak_date": "2024-04-18", "peak_price": 9280, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/252/252990.json", "raw_component_score_breakdown": {"ASP_mix_bridge": 7, "capacity_delivery_cadence": 8, "customer_qualification_visibility": 9, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 9, "sample_to_volume_conversion": 8, "total": 67, "valuation_rerating_runway": 7, "yield_defect_quality": 8}, "reuse_reason": null, "same_entry_group_id": "C08_252990_SAMCNS_20240123_PROBE_CARD_CUSTOMER_QUALITY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_card_customer_quality_attention", "named_customer_qualification_or_sample_to_volume_visibility", "yield_delivery_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_volume_conversion_required", "quality_yield_defect_and_delivery_cadence_required", "ASP_mix_capacity_margin_revision_bridge_required"], "stage4b_evidence_fields": ["socket_probe_customer_quality_price_premium", "quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_volume_conversion_gap", "quality_yield_or_delivery_disappointment", "margin_revision_bridge_failure"], "symbol": "252990", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv", "trigger_date": "2024-01-23", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -60.28, "MAE_30D_pct": -27.74, "MAE_90D_pct": -52.14, "MFE_180D_pct": 8.28, "MFE_30D_pct": 8.28, "MFE_90D_pct": 8.28, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_080580_OKINS_20240123_SOCKET_THEME_FALSE_GREEN", "case_role": "socket_customer_quality_theme_false_green_counterexample", "company_name": "오킨스전자", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2021-01-07 and 2021-01-29, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Socket/customer-quality price confirmation should stay Yellow or route to local 4B when the move is not backed by named customer qualification, volume conversion, delivery cadence, quality/yield evidence and margin/revision bridge. The January 2024 spike produced limited residual upside and a large forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.31, "entry_date": "2024-01-23", "entry_price": 13770, "evidence_family": "smallcap_socket_theme_price_confirmation_without_customer_quality_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SOCKET_PROBE_CUSTOMER_QUALITY_VOLUME_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-25", "low_price_180d": 5470, "peak_date": "2024-01-23", "peak_price": 14910, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/080/080580.json", "raw_component_score_breakdown": {"ASP_mix_bridge": 3, "capacity_delivery_cadence": 3, "customer_qualification_visibility": 4, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "sample_to_volume_conversion": 3, "total": 26, "valuation_rerating_runway": 1, "yield_defect_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C08_080580_OKINS_20240123_SOCKET_THEME_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_card_customer_quality_attention", "named_customer_qualification_or_sample_to_volume_visibility", "yield_delivery_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_volume_conversion_required", "quality_yield_defect_and_delivery_cadence_required", "ASP_mix_capacity_margin_revision_bridge_required"], "stage4b_evidence_fields": ["socket_probe_customer_quality_price_premium", "quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_volume_conversion_gap", "quality_yield_or_delivery_disappointment", "margin_revision_bridge_failure"], "symbol": "080580", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "trigger_date": "2024-01-23", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -60.33, "MAE_30D_pct": -16.64, "MAE_90D_pct": -28.97, "MFE_180D_pct": 4.02, "MFE_30D_pct": 4.02, "MFE_90D_pct": 4.02, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_098120_MCS_20240426_TEST_SOCKET_PRICE_PREMIUM_4B", "case_role": "test_socket_customer_quality_price_premium_counterexample", "company_name": "마이크로컨텍솔", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2011-04-19 and 2011-05-17, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Test-socket price premium should route to local 4B or counterexample when the stock has already capitalized customer-quality optionality and incremental qualification, volume, delivery cadence, ASP/mix and margin/revision evidence do not refresh.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.86, "entry_date": "2024-04-26", "entry_price": 10700, "evidence_family": "test_socket_price_premium_without_incremental_customer_quality_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SOCKET_PROBE_CUSTOMER_QUALITY_VOLUME_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 4245, "peak_date": "2024-04-29", "peak_price": 11130, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/098/098120.json", "raw_component_score_breakdown": {"ASP_mix_bridge": 3, "capacity_delivery_cadence": 3, "customer_qualification_visibility": 4, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "sample_to_volume_conversion": 3, "total": 25, "valuation_rerating_runway": 1, "yield_defect_quality": 3}, "reuse_reason": null, "same_entry_group_id": "C08_098120_MCS_20240426_TEST_SOCKET_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_or_probe_card_customer_quality_attention", "named_customer_qualification_or_sample_to_volume_visibility", "yield_delivery_ASP_mix_margin_revision_route"], "stage3_evidence_fields": ["customer_qualification_and_volume_conversion_required", "quality_yield_defect_and_delivery_cadence_required", "ASP_mix_capacity_margin_revision_bridge_required"], "stage4b_evidence_fields": ["socket_probe_customer_quality_price_premium", "quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_qualification_or_volume_conversion_gap", "quality_yield_or_delivery_disappointment", "margin_revision_bridge_failure"], "symbol": "098120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "trigger_date": "2024-04-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SOCKET_PROBE_CUSTOMER_QUALITY_VOLUME_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "semi_test_socket_customer_quality_probe_socket_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 socket/probe-card rows should allow Stage2 when customer-quality evidence is backed by named qualification, sample-to-volume conversion, delivery cadence, yield/defect quality, ASP/mix and margin-revision bridge, but should route to local 4B/Yellow when price already capitalizes quality optionality and incremental volume/margin evidence has not refreshed.",
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
3. Add C08-specific socket/probe-card customer-quality / qualification / sample-to-volume / delivery-cadence / yield-quality / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C08_STAGE2_ALLOWED_ON_QUALIFICATION_VOLUME_DELIVERY_MARGIN_REVISION_BRIDGE
- C08_GREEN_REQUIRES_CUSTOMER_QUALIFICATION_VOLUME_YIELD_ASP_MIX_REVISION
- C08_SOCKET_PROBE_CUSTOMER_QUALITY_PRICE_PREMIUM_LOCAL_4B
- C08_PRICE_CONFIRMATION_WITHOUT_QUALIFICATION_TO_VOLUME_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

