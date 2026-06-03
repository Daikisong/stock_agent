# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C09 — Advanced equipment valuation blowoff / YC-DI-PSKH 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: YC_DI_PSKH_ADVANCED_EQUIPMENT_PEAK_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|advanced_equipment_peak_valuation_blowoff_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_yc_di_pskh_advanced_equipment_peak_4b_2024_research.md
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

This run avoids those top-covered C09 symbols and adds 232140, 003160, and 031980.  
Each row uses a new `C09 + symbol + trigger_type + entry_date` hard key:
```text
C09 + 232140 + 4B-protective + 2024-06-13
C09 + 003160 + Stage3-Yellow + 2024-06-26
C09 + 031980 + 4B-local-price-only + 2024-06-14
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
232140 와이씨: selected post-2017 forward window clean; corporate-action candidate is 2017-04-05 and outside selected trigger window. Name changed from 와이아이케이 to 와이씨 during the 2024 research window.
003160 디아이: selected 2024 forward window clean; historical corporate-action candidates outside selected trigger window.
031980 피에스케이홀딩스: selected post-2019 forward window clean; name-change/corporate-action candidate is before selected trigger window.
```

## 3. Research thesis

C09 should distinguish advanced-equipment order discovery from advanced-equipment valuation blowoff:

```text
HBM / tester / advanced packaging equipment salience
→ customer order and delivery cadence
→ utilization and backlog conversion
→ margin and revision bridge
→ valuation runway
→ Stage2/Green or protective 4B / 4C-watch
```

An equipment order story is a booked tool slot. A blowoff is the whole fab paying for every future slot at once. Stage2 can buy the booking; Green should not buy the echo after valuation has already priced the order book and fresh evidence is missing.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C09_232140_YC_20240613_ADVANCED_TESTER_VALUATION_BLOWOFF_4B_PROTECTIVE | 232140 | protective_advanced_tester_valuation_blowoff_4B_success | 2024-06-13 | 21900 | 22950 on 2024-06-13 | 8840 on 2024-12-04 | 4.79% | 4.79% | 4.79% | -59.63% | -61.48% |
| C09_003160_DI_20240626_ADVANCED_TESTER_PRICE_CONFIRMATION_FALSE_GREEN | 003160 | advanced_tester_price_confirmation_false_green_counterexample | 2024-06-26 | 28650 | 30800 on 2024-06-27 | 9870 on 2024-12-09 | 7.5% | 7.5% | 7.5% | -65.55% | -67.95% |
| C09_031980_PSKH_20240614_ADVANCED_PACKAGING_EQUIPMENT_PREMIUM_4B | 031980 | advanced_packaging_equipment_valuation_premium_counterexample | 2024-06-14 | 80000 | 85300 on 2024-06-19 | 27700 on 2024-12-09 | 6.62% | 6.62% | 6.62% | -65.38% | -67.53% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- No row in this MD is counted as a clean Stage2/Green positive.
- C09 Stage2 is allowed only before valuation blowoff, when customer-order quality, delivery cadence, backlog conversion, utilization, margin/revision bridge and valuation runway are still visible.
- 가격만 있는 late entry는 Stage2/Green positive로 금지된다. This MD uses late price peaks as 4B/protective or counterexample rows.

### Stage3 / Green
- C09 Green should be blocked when relative strength is exhausted and valuation blowoff risk dominates.
- 003160 is the false-Green/Yellow guard: advanced tester price confirmation was visible, but the June 2024 trigger had small residual upside and a much larger forward drawdown when customer-order-to-margin evidence did not refresh.

### 4B
- 232140 is the protective 4B success anchor. The June 2024 peak had almost no residual runway and a large full-window drawdown.
- 031980 fills the advanced packaging/HBM equipment valuation-premium 4B pocket.
- The core 4B rule is that advanced-equipment theme salience and relative strength should not substitute for fresh customer-order, delivery, utilization and margin-revision evidence.

### 4C
- No hard customer cancellation, delivery failure, accounting break or shipment collapse is asserted.
- The C09 break mode here is valuation-to-evidence exhaustion: the HBM/advanced equipment story may remain directionally real, but incremental customer order, utilization and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C09_003160_DI_20240626_ADVANCED_TESTER_PRICE_CONFIRMATION_FALSE_GREEN": {
    "advanced_equipment_order_salience": 8,
    "customer_order_refresh": 3,
    "delivery_cadence_backlog_conversion": 3,
    "information_confidence": 3,
    "market_mispricing": 3,
    "relative_strength_exhaustion": 8,
    "total": 41,
    "utilization_margin_revision_bridge": 2,
    "valuation_blowoff_risk": 11,
    "valuation_rerating_runway": 0
  },
  "C09_031980_PSKH_20240614_ADVANCED_PACKAGING_EQUIPMENT_PREMIUM_4B": {
    "advanced_equipment_order_salience": 8,
    "customer_order_refresh": 4,
    "delivery_cadence_backlog_conversion": 3,
    "information_confidence": 3,
    "market_mispricing": 3,
    "relative_strength_exhaustion": 9,
    "total": 44,
    "utilization_margin_revision_bridge": 2,
    "valuation_blowoff_risk": 12,
    "valuation_rerating_runway": 0
  },
  "C09_232140_YC_20240613_ADVANCED_TESTER_VALUATION_BLOWOFF_4B_PROTECTIVE": {
    "advanced_equipment_order_salience": 9,
    "customer_order_refresh": 3,
    "delivery_cadence_backlog_conversion": 3,
    "information_confidence": 4,
    "market_mispricing": 2,
    "relative_strength_exhaustion": 9,
    "total": 44,
    "utilization_margin_revision_bridge": 2,
    "valuation_blowoff_risk": 12,
    "valuation_rerating_runway": 0
  }
}
```

## 7. Current calibrated profile stress test

Suggested C09 guard:
```text
if advanced_equipment_price_peak and no refreshed_customer_order_delivery_utilization_margin_revision_bridge:
    block_stage3_green = true
    route_to_protective_4B = true

if relative_strength_exhaustion and valuation_blowoff_risk_high:
    do_not_treat_price_confirmation_as_positive = true

if post_peak_drawdown and order_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 003160 / 2024-06-26: advanced tester confirmation can be over-promoted if relative strength substitutes for refreshed order and margin proof.
- 031980 / 2024-06-14: advanced packaging/HBM equipment premium can look actionable, but fails without renewed customer-order, utilization and revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -59.63, "MAE_30D_pct": -36.07, "MAE_90D_pct": -50.55, "MFE_180D_pct": 4.79, "MFE_30D_pct": 4.79, "MFE_90D_pct": 4.79, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_232140_YC_20240613_ADVANCED_TESTER_VALUATION_BLOWOFF_4B_PROTECTIVE", "case_role": "protective_advanced_tester_valuation_blowoff_4B_success", "company_name": "와이씨", "corporate_action_window_status": "selected post-2017 forward window clean; profile corporate-action candidate is 2017-04-05 and outside selected trigger window", "current_profile_error": false, "current_profile_verdict": "4B-protective routing was useful: after the HBM tester/order story was capitalized, the June 2024 peak had almost no residual runway and a large full-window drawdown. This should not be promoted to Stage2/Green without fresh customer order quality, delivery cadence, utilization, margin revision and valuation reset evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.48, "entry_date": "2024-06-13", "entry_price": 21900, "evidence_family": "HBM_tester_advanced_equipment_peak_valuation_blowoff_after_order_story_capitalized", "evidence_url_pending": false, "fine_archetype_id": "YC_DI_PSKH_ADVANCED_EQUIPMENT_PEAK_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "와이아이케이", "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-04", "low_price_180d": 8840, "peak_date": "2024-06-13", "peak_price": 22950, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/232/232140.json", "raw_component_score_breakdown": {"advanced_equipment_order_salience": 9, "customer_order_refresh": 3, "delivery_cadence_backlog_conversion": 3, "information_confidence": 4, "market_mispricing": 2, "relative_strength_exhaustion": 9, "total": 44, "utilization_margin_revision_bridge": 2, "valuation_blowoff_risk": 12, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C09_232140_YC_20240613_ADVANCED_TESTER_VALUATION_BLOWOFF_4B_PROTECTIVE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_order_salience", "customer_order_delivery_backlog_refresh", "utilization_margin_revision_and_valuation_reset_required"], "stage3_evidence_fields": ["Green_blocked_when_valuation_blowoff_risk_dominates", "fresh_customer_order_and_margin_revision_required", "relative_strength_exhaustion_must_not_substitute_for_evidence"], "stage4b_evidence_fields": ["advanced_equipment_valuation_blowoff", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_margin_revision_bridge_failure", "theme_decompression"], "symbol": "232140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "trigger_date": "2024-06-13", "trigger_type": "4B-protective", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -65.55, "MAE_30D_pct": -38.57, "MAE_90D_pct": -50.79, "MFE_180D_pct": 7.5, "MFE_30D_pct": 7.5, "MFE_90D_pct": 7.5, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_003160_DI_20240626_ADVANCED_TESTER_PRICE_CONFIRMATION_FALSE_GREEN", "case_role": "advanced_tester_price_confirmation_false_green_counterexample", "company_name": "디아이", "corporate_action_window_status": "selected 2024 forward window clean; historical corporate-action candidates outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Advanced tester/equipment price confirmation should remain Yellow or local 4B when price strength is not backed by fresh customer order, delivery cadence, backlog conversion, utilization and margin/revision evidence. The June 2024 trigger had small residual MFE and a much larger forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.95, "entry_date": "2024-06-26", "entry_price": 28650, "evidence_family": "advanced_tester_equipment_price_confirmation_without_incremental_customer_order_delivery_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "YC_DI_PSKH_ADVANCED_EQUIPMENT_PEAK_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "디아이", "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 9870, "peak_date": "2024-06-27", "peak_price": 30800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003160.json", "raw_component_score_breakdown": {"advanced_equipment_order_salience": 8, "customer_order_refresh": 3, "delivery_cadence_backlog_conversion": 3, "information_confidence": 3, "market_mispricing": 3, "relative_strength_exhaustion": 8, "total": 41, "utilization_margin_revision_bridge": 2, "valuation_blowoff_risk": 11, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C09_003160_DI_20240626_ADVANCED_TESTER_PRICE_CONFIRMATION_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_order_salience", "customer_order_delivery_backlog_refresh", "utilization_margin_revision_and_valuation_reset_required"], "stage3_evidence_fields": ["Green_blocked_when_valuation_blowoff_risk_dominates", "fresh_customer_order_and_margin_revision_required", "relative_strength_exhaustion_must_not_substitute_for_evidence"], "stage4b_evidence_fields": ["advanced_equipment_valuation_blowoff", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_margin_revision_bridge_failure", "theme_decompression"], "symbol": "003160", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "trigger_date": "2024-06-26", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -65.38, "MAE_30D_pct": -24.75, "MAE_90D_pct": -49.75, "MFE_180D_pct": 6.62, "MFE_30D_pct": 6.62, "MFE_90D_pct": 6.62, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_031980_PSKH_20240614_ADVANCED_PACKAGING_EQUIPMENT_PREMIUM_4B", "case_role": "advanced_packaging_equipment_valuation_premium_counterexample", "company_name": "피에스케이홀딩스", "corporate_action_window_status": "selected post-2019 forward window clean; name-change/corporate-action candidate is before selected trigger window", "current_profile_error": true, "current_profile_verdict": "Advanced packaging/HBM equipment premium should route to local 4B or counterexample when the market has already capitalized order optionality and fresh customer order, delivery cadence, utilization, ASP/mix and margin/revision evidence do not refresh. The June 2024 trigger had limited local MFE and a very large forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.53, "entry_date": "2024-06-14", "entry_price": 80000, "evidence_family": "advanced_packaging_HBM_equipment_price_premium_without_incremental_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "YC_DI_PSKH_ADVANCED_EQUIPMENT_PEAK_4B_GUARD", "forward_window_trading_days": 180, "historical_name": "피에스케이홀딩스", "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 27700, "peak_date": "2024-06-19", "peak_price": 85300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/031/031980.json", "raw_component_score_breakdown": {"advanced_equipment_order_salience": 8, "customer_order_refresh": 4, "delivery_cadence_backlog_conversion": 3, "information_confidence": 3, "market_mispricing": 3, "relative_strength_exhaustion": 9, "total": 44, "utilization_margin_revision_bridge": 2, "valuation_blowoff_risk": 12, "valuation_rerating_runway": 0}, "reuse_reason": null, "same_entry_group_id": "C09_031980_PSKH_20240614_ADVANCED_PACKAGING_EQUIPMENT_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_order_salience", "customer_order_delivery_backlog_refresh", "utilization_margin_revision_and_valuation_reset_required"], "stage3_evidence_fields": ["Green_blocked_when_valuation_blowoff_risk_dominates", "fresh_customer_order_and_margin_revision_required", "relative_strength_exhaustion_must_not_substitute_for_evidence"], "stage4b_evidence_fields": ["advanced_equipment_valuation_blowoff", "order_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_gap_or_delivery_slippage", "utilization_margin_revision_bridge_failure", "theme_decompression"], "symbol": "031980", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "trigger_date": "2024-06-14", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "YC_DI_PSKH_ADVANCED_EQUIPMENT_PEAK_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "advanced_equipment_valuation_blowoff_yc_di_pskh_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C09 advanced-equipment rows should route late HBM/tester/packaging equipment peaks to protective 4B when order optionality is already capitalized and there is no refreshed customer-order, delivery, utilization and margin-revision bridge; relative strength exhaustion must block Stage3-Green even when theme salience remains high.",
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
3. Add C09-specific advanced equipment / valuation blowoff / relative strength exhaustion / customer order / delivery cadence / utilization / margin-revision / protective-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C09_BLOCK_GREEN_WHEN_VALUATION_BLOWOFF_AND_NO_REFRESHED_ORDER_MARGIN_BRIDGE
- C09_ADVANCED_EQUIPMENT_PEAK_ROUTES_TO_PROTECTIVE_4B
- C09_RELATIVE_STRENGTH_EXHAUSTION_DOES_NOT_SUBSTITUTE_FOR_CUSTOMER_ORDER_EVIDENCE
- C09_POST_PEAK_DRAWDOWN_WITH_ORDER_TO_MARGIN_EXHAUSTION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

