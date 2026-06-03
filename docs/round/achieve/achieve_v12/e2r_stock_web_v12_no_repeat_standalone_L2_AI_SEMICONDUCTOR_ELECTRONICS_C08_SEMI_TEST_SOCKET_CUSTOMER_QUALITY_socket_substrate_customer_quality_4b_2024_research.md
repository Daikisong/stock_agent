# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C08 — Semi test socket customer quality / socket-substrate 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: SOCKET_SUBSTRATE_CUSTOMER_QUALITY_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|socket_substrate_customer_quality_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_socket_substrate_customer_quality_4b_2024_research.md
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

This run avoids those top-covered C08 symbols and adds 219130, 252990, and 098120.  
Each row uses a new `C08 + symbol + trigger_type + entry_date` hard key:
```text
C08 + 219130 + Stage2-Actionable + 2024-01-22
C08 + 252990 + 4B-local-price-only + 2024-04-26
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
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
```

Selected profiles:
```text
219130 타이거일렉: corporate_action_candidate_count=0; clean 2024 forward window.
252990 샘씨엔에스: corporate_action_candidate_count=0; clean 2024 forward window.
098120 마이크로컨텍솔: selected post-2011 forward window clean; profile corporate-action candidates are 2011 and outside selected trigger window.
```

## 3. Research thesis

C08 should split genuine test-socket/customer-quality discovery from socket-substrate theme beta already paid in price:

```text
AI/HBM test-chain demand
→ socket/substrate customer mix quality
→ customer order durability and delivery cadence
→ utilization and ASP/mix bridge
→ gross margin and revision confirmation
→ Stage2/Green or local 4B cap
```

A test socket signal is like a probe touching the actual customer board. Stage2 can buy when that probe has current—customer quality, order durability and margin bridge. Green should not buy every spark after the socket basket has already rerated.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C08_219130_TIGERELEC_20240122_TEST_SOCKET_SUBSTRATE_STAGE2 | 219130 | positive_test_socket_substrate_customer_quality_stage2_success_with_later_4b_refresh | 2024-01-22 | 24050 | 45300 on 2024-05-14 | 18840 on 2024-09-24 | 47.19% | 88.36% | 88.36% | -21.66% | -58.41% |
| C08_252990_SAMCNES_20240426_CERAMIC_PROBE_SUBSTRATE_PRICE_PREMIUM_4B | 252990 | ceramic_probe_substrate_customer_quality_price_premium_counterexample | 2024-04-26 | 8800 | 8890 on 2024-04-26 | 3520 on 2024-12-09 | 1.02% | 1.02% | 1.02% | -60.0% | -60.4% |
| C08_098120_MICROCONTACT_20240426_TEST_SOCKET_PRICE_CONFIRMATION_FALSE_GREEN | 098120 | test_socket_customer_quality_false_green_counterexample | 2024-04-26 | 10700 | 11130 on 2024-04-29 | 4245 on 2024-12-09 | 4.02% | 4.02% | 4.02% | -60.33% | -61.86% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 219130 is the positive anchor. The January 2024 test-socket/substrate customer-quality route produced strong 30D/90D MFE before the May 2024 premium required 4B refresh discipline.
- Stage2 is allowed only when socket/substrate salience maps to customer mix quality, AI/HBM test-chain relevance, order durability, delivery cadence, utilization and margin/revision visibility.
- 가격만 있는 early entry는 금지된다. This positive row is included because the trigger family is customer-quality/test-chain evidence, not price-only momentum.

### Stage3 / Green
- C08 Green should require customer mix quality, order durability, delivery cadence, utilization, ASP/mix and margin/revision confirmation.
- 098120 is the false-Green/Yellow guard: test-socket price confirmation was visible, but the April 2024 price had small residual upside and much larger forward MAE when customer-quality-to-margin evidence did not refresh.

### 4B
- 252990 fills the ceramic probe-card substrate 4B pocket. The April 2024 trigger had almost no residual MFE and a large forward drawdown.
- 098120 shows the same failure in socket form: the AI/HBM test-chain story can remain directionally real while the listed-company earnings bridge is too stale for Green.
- 219130 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the customer-quality option.

### 4C
- No hard customer cancellation, delivery failure, utilization collapse, accounting break or shipment stop is asserted.
- The C08 break mode here is customer-quality-to-margin exhaustion: the socket/substrate story may remain directionally real, but incremental customer order, delivery cadence, utilization, ASP/mix and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C08_098120_MICROCONTACT_20240426_TEST_SOCKET_PRICE_CONFIRMATION_FALSE_GREEN": {
    "AI_HBM_test_chain_relevance": 5,
    "customer_mix_or_named_order_quality": 3,
    "delivery_cadence_backlog_conversion": 2,
    "information_confidence": 3,
    "market_mispricing": 4,
    "relative_strength_quality": 4,
    "test_socket_customer_quality_visibility": 6,
    "total": 30,
    "utilization_ASP_mix_margin_bridge": 2,
    "valuation_rerating_runway": 1
  },
  "C08_219130_TIGERELEC_20240122_TEST_SOCKET_SUBSTRATE_STAGE2": {
    "AI_HBM_test_chain_relevance": 8,
    "customer_mix_or_named_order_quality": 7,
    "delivery_cadence_backlog_conversion": 7,
    "information_confidence": 4,
    "market_mispricing": 8,
    "relative_strength_quality": 9,
    "test_socket_customer_quality_visibility": 10,
    "total": 67,
    "utilization_ASP_mix_margin_bridge": 7,
    "valuation_rerating_runway": 7
  },
  "C08_252990_SAMCNES_20240426_CERAMIC_PROBE_SUBSTRATE_PRICE_PREMIUM_4B": {
    "AI_HBM_test_chain_relevance": 6,
    "customer_mix_or_named_order_quality": 3,
    "delivery_cadence_backlog_conversion": 3,
    "information_confidence": 3,
    "market_mispricing": 4,
    "relative_strength_quality": 4,
    "test_socket_customer_quality_visibility": 7,
    "total": 33,
    "utilization_ASP_mix_margin_bridge": 2,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C08 guard:
```text
if semi_test_socket and customer_quality_order_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if socket_substrate_price_premium and no incremental_customer_order_delivery_utilization_ASP_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and customer_quality_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 252990 / 2024-04-26: ceramic probe-card substrate premium can be over-promoted if price strength substitutes for refreshed customer order and margin proof.
- 098120 / 2024-04-26: test-socket confirmation can look like Yellow-to-Green, but fails without renewed customer-quality and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -21.66, "MAE_30D_pct": -8.94, "MAE_90D_pct": -8.94, "MFE_180D_pct": 88.36, "MFE_30D_pct": 47.19, "MFE_90D_pct": 88.36, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_219130_TIGERELEC_20240122_TEST_SOCKET_SUBSTRATE_STAGE2", "case_role": "positive_test_socket_substrate_customer_quality_stage2_success_with_later_4b_refresh", "company_name": "타이거일렉", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2024 forward window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when semiconductor test-socket/substrate demand, AI/HBM test-chain relevance, customer-quality optionality and relative strength were visible before the rerating was fully capitalized. Green still requires customer mix quality, socket/substrate order durability, delivery cadence, utilization, ASP/mix and margin/revision bridge; after the May 2024 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -58.41, "entry_date": "2024-01-22", "entry_price": 24050, "evidence_family": "semi_test_socket_substrate_customer_quality_HBM_AI_test_demand_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "SOCKET_SUBSTRATE_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-24", "low_price_180d": 18840, "peak_date": "2024-05-14", "peak_price": 45300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/219/219130.json", "raw_component_score_breakdown": {"AI_HBM_test_chain_relevance": 8, "customer_mix_or_named_order_quality": 7, "delivery_cadence_backlog_conversion": 7, "information_confidence": 4, "market_mispricing": 8, "relative_strength_quality": 9, "test_socket_customer_quality_visibility": 10, "total": 67, "utilization_ASP_mix_margin_bridge": 7, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C08_219130_TIGERELEC_20240122_TEST_SOCKET_SUBSTRATE_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_customer_quality_visibility", "AI_HBM_test_chain_relevance", "customer_mix_order_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_mix_quality_required", "order_durability_and_delivery_cadence_required", "utilization_ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_substrate_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_ASP_mix_margin_revision_bridge_failure", "theme_decompression"], "symbol": "219130", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv", "trigger_date": "2024-01-22", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -60.0, "MAE_30D_pct": -20.91, "MAE_90D_pct": -34.32, "MFE_180D_pct": 1.02, "MFE_30D_pct": 1.02, "MFE_90D_pct": 1.02, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_252990_SAMCNES_20240426_CERAMIC_PROBE_SUBSTRATE_PRICE_PREMIUM_4B", "case_role": "ceramic_probe_substrate_customer_quality_price_premium_counterexample", "company_name": "샘씨엔에스", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2024 forward window", "current_profile_error": true, "current_profile_verdict": "Ceramic probe-card substrate price premium should route to local 4B/counterexample when the market has already capitalized AI/HBM test-chain optionality and fresh customer order, delivery cadence, utilization, ASP/mix and margin/revision evidence do not refresh. The April 2024 trigger had almost no residual MFE and a large forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.4, "entry_date": "2024-04-26", "entry_price": 8800, "evidence_family": "ceramic_probe_card_substrate_AI_test_theme_price_premium_without_customer_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SOCKET_SUBSTRATE_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 3520, "peak_date": "2024-04-26", "peak_price": 8890, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/252/252990.json", "raw_component_score_breakdown": {"AI_HBM_test_chain_relevance": 6, "customer_mix_or_named_order_quality": 3, "delivery_cadence_backlog_conversion": 3, "information_confidence": 3, "market_mispricing": 4, "relative_strength_quality": 4, "test_socket_customer_quality_visibility": 7, "total": 33, "utilization_ASP_mix_margin_bridge": 2, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_252990_SAMCNES_20240426_CERAMIC_PROBE_SUBSTRATE_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_customer_quality_visibility", "AI_HBM_test_chain_relevance", "customer_mix_order_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_mix_quality_required", "order_durability_and_delivery_cadence_required", "utilization_ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_substrate_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_ASP_mix_margin_revision_bridge_failure", "theme_decompression"], "symbol": "252990", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/252/252990/2024.csv", "trigger_date": "2024-04-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -60.33, "MAE_30D_pct": -16.64, "MAE_90D_pct": -28.97, "MFE_180D_pct": 4.02, "MFE_30D_pct": 4.02, "MFE_90D_pct": 4.02, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "case_id": "C08_098120_MICROCONTACT_20240426_TEST_SOCKET_PRICE_CONFIRMATION_FALSE_GREEN", "case_role": "test_socket_customer_quality_false_green_counterexample", "company_name": "마이크로컨텍솔", "corporate_action_window_status": "selected post-2011 forward window clean; profile corporate-action candidates are 2011 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Test-socket price confirmation should remain Yellow or local 4B when the price has already paid for AI/HBM test-chain optionality but customer-quality, order durability, delivery cadence, utilization, ASP/mix and margin/revision evidence do not refresh. The April 2024 trigger had small residual MFE and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.86, "entry_date": "2024-04-26", "entry_price": 10700, "evidence_family": "test_socket_price_confirmation_without_customer_quality_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "SOCKET_SUBSTRATE_CUSTOMER_QUALITY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 4245, "peak_date": "2024-04-29", "peak_price": 11130, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/098/098120.json", "raw_component_score_breakdown": {"AI_HBM_test_chain_relevance": 5, "customer_mix_or_named_order_quality": 3, "delivery_cadence_backlog_conversion": 2, "information_confidence": 3, "market_mispricing": 4, "relative_strength_quality": 4, "test_socket_customer_quality_visibility": 6, "total": 30, "utilization_ASP_mix_margin_bridge": 2, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C08_098120_MICROCONTACT_20240426_TEST_SOCKET_PRICE_CONFIRMATION_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["test_socket_customer_quality_visibility", "AI_HBM_test_chain_relevance", "customer_mix_order_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_mix_quality_required", "order_durability_and_delivery_cadence_required", "utilization_ASP_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["test_socket_substrate_price_premium", "customer_quality_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_ASP_mix_margin_revision_bridge_failure", "theme_decompression"], "symbol": "098120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "trigger_date": "2024-04-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "SOCKET_SUBSTRATE_CUSTOMER_QUALITY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "semi_test_socket_customer_quality_socket_substrate_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C08 test-socket/customer-quality rows should allow Stage2 when customer mix/order quality, AI-HBM test-chain relevance, delivery cadence, utilization, ASP/mix and margin-revision bridge are visible, but route socket/substrate price premiums to Yellow/local 4B when the customer-quality-to-margin evidence has not refreshed.",
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
3. Add C08-specific test-socket/substrate / customer quality / order durability / delivery cadence / utilization / ASP-mix / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C08_STAGE2_ALLOWED_ON_CUSTOMER_QUALITY_ORDER_DELIVERY_MARGIN_REVISION_BRIDGE
- C08_GREEN_REQUIRES_CUSTOMER_MIX_ORDER_DURABILITY_UTILIZATION_ASP_MIX_REVISION
- C08_SOCKET_SUBSTRATE_PRICE_PREMIUM_LOCAL_4B
- C08_PRICE_CONFIRMATION_WITHOUT_CUSTOMER_QUALITY_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

