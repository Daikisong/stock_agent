# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C07 — HBM equipment order relative strength / YC-DI-PSKH tester 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: YC_DI_PSKH_HBM_TESTER_ORDER_RS_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|HBM_tester_order_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_yc_di_pskh_hbm_tester_4b_2024_research.md
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

This run avoids those top-covered C07 symbols and adds 232140, 003160, and 031980.  
Each row uses a new `C07 + symbol + trigger_type + entry_date` hard key:
```text
C07 + 232140 + Stage2-Actionable + 2024-04-17
C07 + 003160 + 4B-local-price-only + 2024-06-21
C07 + 031980 + Stage3-Yellow + 2024-06-07
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
232140 와이씨: selected post-2017 forward window clean; profile corporate-action candidate is 2017-04-05 and outside selected trigger window. Name changed from 와이아이케이 to 와이씨 during the 2024 research window.
003160 디아이: selected 2024 forward window clean; historical corporate-action candidates outside selected trigger window.
031980 피에스케이홀딩스: selected post-2019 forward window clean; name-change/corporate-action candidate is before selected trigger window.
```

## 3. Research thesis

C07 should distinguish HBM equipment order relative strength from tester/equipment theme beta already paid in price:

```text
HBM equipment / tester order signal
→ customer or named order quality
→ delivery cadence and backlog conversion
→ utilization and capacity loading
→ margin and revision bridge
→ relative strength quality
→ Stage2/Green or local 4B cap
```

HBM equipment order strength is a booked lane, not just a fast car. Stage2 can buy when the lane is visible—customer, delivery and margin bridge. Green should not treat every speed burst as a booked order after the tester basket has already rerated.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C07_232140_YC_20240417_HBM_TESTER_ORDER_RS_STAGE2 | 232140 | positive_HBM_tester_order_relative_strength_stage2_success_with_later_4b_refresh | 2024-04-17 | 7280 | 22950 on 2024-06-13 | 6280 on 2024-04-17 | 146.02% | 215.25% | 215.25% | -13.74% | -61.48% |
| C07_003160_DI_20240621_HBM_TESTER_PRICE_PREMIUM_4B | 003160 | HBM_tester_price_premium_local_4B_counterexample | 2024-06-21 | 25900 | 30300 on 2024-06-26 | 9870 on 2024-12-09 | 16.99% | 16.99% | 16.99% | -61.89% | -67.43% |
| C07_031980_PSKH_20240607_HBM_EQUIPMENT_RS_FALSE_GREEN | 031980 | HBM_equipment_relative_strength_false_green_counterexample | 2024-06-07 | 74600 | 85300 on 2024-06-19 | 27700 on 2024-12-09 | 14.34% | 14.34% | 14.34% | -62.87% | -67.53% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 232140 is the positive anchor. The April 2024 HBM tester/customer-order route produced very strong 30D/90D/180D MFE before the June 2024 premium required 4B refresh discipline.
- Stage2 is allowed only when HBM tester/equipment salience maps to customer-order quality, delivery cadence, backlog conversion, utilization and margin/revision visibility.
- 가격만 있는 early entry는 금지된다. This positive row is included because the trigger family is HBM tester customer-order/relative-strength evidence, not price-only momentum.

### Stage3 / Green
- C07 Green should require customer order quality, delivery cadence, backlog conversion, utilization, margin revision and valuation runway.
- 031980 is the false-Green/Yellow guard: HBM equipment relative strength was visible, but the June 2024 price had modest residual upside and a much larger forward drawdown when new customer-order-to-margin evidence did not refresh.

### 4B
- 003160 fills the HBM tester price-premium 4B pocket. The June 2024 trigger had limited local MFE and a large full-window drawdown.
- 031980 shows the same failure in advanced equipment relative-strength form: the HBM order theme can remain directionally real while the listed-company earnings bridge is too stale for Green.
- 232140 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the customer-order path.

### 4C
- No hard customer cancellation, delivery failure, accounting break or shipment collapse is asserted.
- The C07 break mode here is order-to-margin exhaustion: the HBM equipment story may remain directionally real, but incremental customer order, delivery cadence, utilization and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C07_003160_DI_20240621_HBM_TESTER_PRICE_PREMIUM_4B": {
    "HBM_equipment_order_visibility": 7,
    "customer_quality_or_named_order": 3,
    "delivery_cadence_backlog_conversion": 3,
    "information_confidence": 3,
    "market_mispricing": 4,
    "relative_strength_quality": 5,
    "total": 28,
    "utilization_margin_revision_bridge": 2,
    "valuation_rerating_runway": 1
  },
  "C07_031980_PSKH_20240607_HBM_EQUIPMENT_RS_FALSE_GREEN": {
    "HBM_equipment_order_visibility": 7,
    "customer_quality_or_named_order": 4,
    "delivery_cadence_backlog_conversion": 3,
    "information_confidence": 3,
    "market_mispricing": 4,
    "relative_strength_quality": 6,
    "total": 30,
    "utilization_margin_revision_bridge": 2,
    "valuation_rerating_runway": 1
  },
  "C07_232140_YC_20240417_HBM_TESTER_ORDER_RS_STAGE2": {
    "HBM_equipment_order_visibility": 10,
    "customer_quality_or_named_order": 8,
    "delivery_cadence_backlog_conversion": 7,
    "information_confidence": 4,
    "market_mispricing": 9,
    "relative_strength_quality": 10,
    "total": 63,
    "utilization_margin_revision_bridge": 7,
    "valuation_rerating_runway": 8
  }
}
```

## 7. Current calibrated profile stress test

Suggested C07 guard:
```text
if HBM_equipment_order and customer_order_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if HBM_tester_or_equipment_price_premium and no incremental_customer_order_delivery_utilization_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and order_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 003160 / 2024-06-21: HBM tester premium can be over-promoted if price strength substitutes for refreshed customer order, delivery cadence and margin proof.
- 031980 / 2024-06-07: HBM equipment relative strength can look like Yellow-to-Green, but fails without renewed customer-order and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -13.74, "MAE_30D_pct": -13.74, "MAE_90D_pct": -13.74, "MFE_180D_pct": 215.25, "MFE_30D_pct": 146.02, "MFE_90D_pct": 215.25, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_232140_YC_20240417_HBM_TESTER_ORDER_RS_STAGE2", "case_role": "positive_HBM_tester_order_relative_strength_stage2_success_with_later_4b_refresh", "company_name": "와이씨", "corporate_action_window_status": "selected post-2017 forward window clean; profile corporate-action candidate is 2017-04-05 and outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when HBM tester/customer-order salience, memory capex direction, tester supply-chain relevance and relative strength were visible before the rerating was fully capitalized. Green still requires named customer/order quality, delivery cadence, backlog conversion, utilization, margin/revision bridge and valuation runway; after the June 2024 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.48, "entry_date": "2024-04-17", "entry_price": 7280, "evidence_family": "HBM_memory_tester_customer_order_relative_strength_name_change_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "YC_DI_PSKH_HBM_TESTER_ORDER_RS_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "와이아이케이", "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-04-17", "low_price_180d": 6280, "peak_date": "2024-06-13", "peak_price": 22950, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/232/232140.json", "raw_component_score_breakdown": {"HBM_equipment_order_visibility": 10, "customer_quality_or_named_order": 8, "delivery_cadence_backlog_conversion": 7, "information_confidence": 4, "market_mispricing": 9, "relative_strength_quality": 10, "total": 63, "utilization_margin_revision_bridge": 7, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C07_232140_YC_20240417_HBM_TESTER_ORDER_RS_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_order_visibility", "customer_quality_or_named_order", "relative_strength_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_order_quality_required", "delivery_cadence_and_backlog_conversion_required", "utilization_margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "tester_order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_margin_revision_bridge_failure", "theme_decompression"], "symbol": "232140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "trigger_date": "2024-04-17", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -61.89, "MAE_30D_pct": -32.05, "MAE_90D_pct": -45.56, "MFE_180D_pct": 16.99, "MFE_30D_pct": 16.99, "MFE_90D_pct": 16.99, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_003160_DI_20240621_HBM_TESTER_PRICE_PREMIUM_4B", "case_role": "HBM_tester_price_premium_local_4B_counterexample", "company_name": "디아이", "corporate_action_window_status": "selected 2024 forward window clean; historical corporate-action candidates outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "HBM tester price premium should route to local 4B or counterexample when the market has already capitalized tester optionality and fresh customer order, delivery cadence, utilization, backlog conversion and margin/revision evidence do not refresh. The June 2024 trigger had limited local MFE and a large full-window drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.43, "entry_date": "2024-06-21", "entry_price": 25900, "evidence_family": "HBM_tester_theme_price_premium_without_incremental_customer_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "YC_DI_PSKH_HBM_TESTER_ORDER_RS_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "디아이", "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 9870, "peak_date": "2024-06-26", "peak_price": 30300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003160.json", "raw_component_score_breakdown": {"HBM_equipment_order_visibility": 7, "customer_quality_or_named_order": 3, "delivery_cadence_backlog_conversion": 3, "information_confidence": 3, "market_mispricing": 4, "relative_strength_quality": 5, "total": 28, "utilization_margin_revision_bridge": 2, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C07_003160_DI_20240621_HBM_TESTER_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_order_visibility", "customer_quality_or_named_order", "relative_strength_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_order_quality_required", "delivery_cadence_and_backlog_conversion_required", "utilization_margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "tester_order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_margin_revision_bridge_failure", "theme_decompression"], "symbol": "003160", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "trigger_date": "2024-06-21", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -62.87, "MAE_30D_pct": -23.59, "MAE_90D_pct": -46.11, "MFE_180D_pct": 14.34, "MFE_30D_pct": 14.34, "MFE_90D_pct": 14.34, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_031980_PSKH_20240607_HBM_EQUIPMENT_RS_FALSE_GREEN", "case_role": "HBM_equipment_relative_strength_false_green_counterexample", "company_name": "피에스케이홀딩스", "corporate_action_window_status": "selected post-2019 forward window clean; profile name-change/corporate-action candidate is before selected trigger window", "current_profile_error": true, "current_profile_verdict": "HBM equipment relative strength should remain Yellow or local 4B when the price has already paid for the HBM order story and the stock lacks refreshed customer order, delivery cadence, backlog conversion, utilization and margin/revision evidence. The June 2024 trigger had modest residual upside and a much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.53, "entry_date": "2024-06-07", "entry_price": 74600, "evidence_family": "HBM_equipment_relative_strength_without_incremental_customer_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "YC_DI_PSKH_HBM_TESTER_ORDER_RS_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "피에스케이홀딩스", "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 27700, "peak_date": "2024-06-19", "peak_price": 85300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/031/031980.json", "raw_component_score_breakdown": {"HBM_equipment_order_visibility": 7, "customer_quality_or_named_order": 4, "delivery_cadence_backlog_conversion": 3, "information_confidence": 3, "market_mispricing": 4, "relative_strength_quality": 6, "total": 30, "utilization_margin_revision_bridge": 2, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C07_031980_PSKH_20240607_HBM_EQUIPMENT_RS_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_equipment_order_visibility", "customer_quality_or_named_order", "relative_strength_delivery_margin_revision_route"], "stage3_evidence_fields": ["customer_order_quality_required", "delivery_cadence_and_backlog_conversion_required", "utilization_margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["HBM_equipment_price_premium", "tester_order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_margin_revision_bridge_failure", "theme_decompression"], "symbol": "031980", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "trigger_date": "2024-06-07", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "YC_DI_PSKH_HBM_TESTER_ORDER_RS_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "HBM_equipment_order_relative_strength_yc_di_pskh_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C07 HBM equipment/order rows should allow Stage2 when customer-order quality, delivery cadence, backlog conversion, relative strength and margin-revision bridge are visible, but route HBM tester/equipment price premiums to Yellow/local 4B when the customer-order-to-margin evidence has not refreshed.",
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
3. Add C07-specific HBM equipment/tester / customer order / delivery cadence / backlog conversion / utilization / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C07_STAGE2_ALLOWED_ON_CUSTOMER_ORDER_DELIVERY_MARGIN_REVISION_BRIDGE
- C07_GREEN_REQUIRES_CUSTOMER_ORDER_BACKLOG_UTILIZATION_REVISION
- C07_HBM_TESTER_EQUIPMENT_PRICE_PREMIUM_LOCAL_4B
- C07_RELATIVE_STRENGTH_WITHOUT_ORDER_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

