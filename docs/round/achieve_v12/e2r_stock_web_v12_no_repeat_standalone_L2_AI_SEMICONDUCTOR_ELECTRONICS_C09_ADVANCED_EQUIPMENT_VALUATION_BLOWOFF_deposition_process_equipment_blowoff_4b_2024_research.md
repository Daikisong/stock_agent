# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C09 — Advanced equipment valuation blowoff / deposition-process equipment 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: DEPOSITION_PROCESS_EQUIPMENT_VALUATION_BLOWOFF_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|valuation_blowoff_to_order_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_deposition_process_equipment_blowoff_4b_2024_research.md
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

This run avoids those top-covered C09 symbols and adds 084370, 240810, and 036930.  
Each row uses a new `C09 + symbol + trigger_type + entry_date` hard key:
```text
C09 + 084370 + 4B-local-price-only + 2024-05-28
C09 + 240810 + 4B-local-price-only + 2024-04-08
C09 + 036930 + Stage3-Yellow + 2024-04-08
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
084370 유진테크: corporate_action_candidate_count=0; clean 2024 forward window.
240810 원익IPS: corporate_action_candidate_count=0; clean 2024 forward window.
036930 주성엔지니어링: selected 2024 forward window clean; corporate-action candidate is 2000-06-22, outside selected test window.
```

## 3. Research thesis

C09 should separate **equipment rerating discovery** from **equipment valuation blowoff**:

```text
advanced semi equipment / HBM memory capex salience
→ direct customer order or backlog refresh
→ delivery cadence and backlog quality
→ relative strength and valuation runway
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

An equipment rerating is a furnace heating up. Stage2 can buy the heat when new orders and margins are still being discovered. Green should not keep buying after the furnace is red-hot unless fresh order-to-margin fuel arrives.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C09_084370_EUGENETECH_20240528_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF_4B | 084370 | protective_deposition_equipment_valuation_blowoff_4b_success | 2024-05-28 | 56500 | 60000 on 2024-05-28 | 32450 on 2024-11-19 | 6.19% | 6.19% | 6.19% | -42.57% | -45.92% |
| C09_240810_WONIKIPS_20240408_PROCESS_EQUIPMENT_BLOWOFF_4B | 240810 | process_equipment_valuation_blowoff_counterexample | 2024-04-08 | 41650 | 44850 on 2024-04-08 | 22200 on 2024-11-14 | 7.68% | 7.68% | 7.68% | -46.7% | -50.5% |
| C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_FALSE_GREEN | 036930 | deposition_equipment_valuation_false_green_counterexample | 2024-04-08 | 36500 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 13.56% | 13.56% | 13.56% | -39.59% | -46.8% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a fresh clean Stage2/Green positive. 084370 is a protective 4B success, not a new Stage2 row.
- C09 Green should require fresh customer order/backlog, delivery cadence, margin revision and valuation runway after the RS move.
- 036930 is the false-Green/Yellow guard: deposition-equipment price confirmation was visible, but the April 2024 price already paid for much of the memory-capex recovery and later MAE overwhelmed residual upside.

### 4B
- 084370 is the protective 4B anchor. It had strong earlier Stage2 behavior, but at the May 2024 premium the forward path demanded 4B discipline.
- 240810 fills the process-equipment price-premium 4B pocket. The entry was near the local top and later drawdown was large.
- The core 4B rule is that equipment relative strength and HBM/memory capex salience should not substitute for fresh order, delivery and margin evidence after valuation has already rerated.

### 4C
- No hard customer cancellation, capex cut, delivery failure or accounting break is asserted.
- The C09 break mode is valuation exhaustion: equipment salience may remain directionally real, but incremental customer order, delivery cadence and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_FALSE_GREEN": {
    "advanced_equipment_theme_salience": 8,
    "customer_order_backlog_refresh": 3,
    "delivery_schedule_visibility": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "relative_strength_overextension": 8,
    "total": 33,
    "valuation_rerating_runway": 1
  },
  "C09_084370_EUGENETECH_20240528_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF_4B": {
    "advanced_equipment_theme_salience": 9,
    "customer_order_backlog_refresh": 4,
    "delivery_schedule_visibility": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 3,
    "relative_strength_overextension": 9,
    "total": 36,
    "valuation_rerating_runway": 1
  },
  "C09_240810_WONIKIPS_20240408_PROCESS_EQUIPMENT_BLOWOFF_4B": {
    "advanced_equipment_theme_salience": 8,
    "customer_order_backlog_refresh": 3,
    "delivery_schedule_visibility": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 3,
    "relative_strength_overextension": 8,
    "total": 32,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C09 guard:
```text
if advanced_equipment_RS and customer_order_delivery_margin_revision_bridge_visible and valuation_runway_remains:
    allow_stage2_actionable = true

if equipment_price_premium and no incremental_order_backlog_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and valuation_to_order_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 240810 / 2024-04-08: process-equipment valuation premium can be over-promoted if price strength substitutes for direct order/backlog and margin proof.
- 036930 / 2024-04-08: deposition-equipment confirmation can look like Yellow-to-Green, but fails without renewed customer order and revision bridge after valuation rerating.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -42.57, "MAE_30D_pct": -16.81, "MAE_90D_pct": -37.43, "MFE_180D_pct": 6.19, "MFE_30D_pct": 6.19, "MFE_90D_pct": 6.19, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_084370_EUGENETECH_20240528_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF_4B", "case_role": "protective_deposition_equipment_valuation_blowoff_4b_success", "company_name": "유진테크", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful after the deposition/process-equipment rerating had already capitalized HBM/memory capex recovery. The stock had valid earlier Stage2 evidence, but at the 2024-05-28 blowoff entry, residual upside was small relative to forward drawdown unless fresh customer order, backlog delivery and margin/revision evidence expanded.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.92, "entry_date": "2024-05-28", "entry_price": 56500, "evidence_family": "advanced_deposition_equipment_valuation_blowoff_after_HBM_memory_capex_RS_without_incremental_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PROCESS_EQUIPMENT_VALUATION_BLOWOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-19", "low_price_180d": 32450, "peak_date": "2024-05-28", "peak_price": 60000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/084/084370.json", "raw_component_score_breakdown": {"advanced_equipment_theme_salience": 9, "customer_order_backlog_refresh": 4, "delivery_schedule_visibility": 4, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 3, "relative_strength_overextension": 9, "total": 36, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C09_084370_EUGENETECH_20240528_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_theme_and_customer_order_visibility", "valuation_rerating_runway_required", "margin_revision_and_delivery_cadence_required"], "stage3_evidence_fields": ["fresh_customer_order_backlog_required", "valuation_runway_required_after_RS_move", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_price_premium", "relative_strength_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_delivery_gap", "valuation_mean_reversion", "margin_revision_bridge_failure"], "symbol": "084370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv", "trigger_date": "2024-05-28", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -46.7, "MAE_30D_pct": -19.57, "MAE_90D_pct": -19.57, "MFE_180D_pct": 7.68, "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_240810_WONIKIPS_20240408_PROCESS_EQUIPMENT_BLOWOFF_4B", "case_role": "process_equipment_valuation_blowoff_counterexample", "company_name": "원익IPS", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "Process-equipment valuation blowoff should route to local 4B/counterexample when HBM/memory capex recovery has already been capitalized and incremental order conversion, delivery schedule, backlog quality and margin/revision evidence do not refresh. The April 2024 trigger showed small residual upside and large forward MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.5, "entry_date": "2024-04-08", "entry_price": 41650, "evidence_family": "process_equipment_HBM_memory_capex_price_premium_without_incremental_order_backlog_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PROCESS_EQUIPMENT_VALUATION_BLOWOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-14", "low_price_180d": 22200, "peak_date": "2024-04-08", "peak_price": 44850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/240/240810.json", "raw_component_score_breakdown": {"advanced_equipment_theme_salience": 8, "customer_order_backlog_refresh": 3, "delivery_schedule_visibility": 3, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 3, "relative_strength_overextension": 8, "total": 32, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C09_240810_WONIKIPS_20240408_PROCESS_EQUIPMENT_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_theme_and_customer_order_visibility", "valuation_rerating_runway_required", "margin_revision_and_delivery_cadence_required"], "stage3_evidence_fields": ["fresh_customer_order_backlog_required", "valuation_runway_required_after_RS_move", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_price_premium", "relative_strength_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_delivery_gap", "valuation_mean_reversion", "margin_revision_bridge_failure"], "symbol": "240810", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.59, "MAE_30D_pct": -13.29, "MAE_90D_pct": -13.7, "MFE_180D_pct": 13.56, "MFE_30D_pct": 13.56, "MFE_90D_pct": 13.56, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_FALSE_GREEN", "case_role": "deposition_equipment_valuation_false_green_counterexample", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2000-06-22 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Deposition-equipment valuation confirmation should stay Yellow or route to local 4B when price strength is not followed by fresh customer order conversion, backlog quality, delivery cadence and margin/revision evidence. The April 2024 spike had limited residual upside and much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-04-08", "entry_price": 36500, "evidence_family": "deposition_equipment_valuation_price_confirmation_without_customer_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PROCESS_EQUIPMENT_VALUATION_BLOWOFF_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 22050, "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/036/036930.json", "raw_component_score_breakdown": {"advanced_equipment_theme_salience": 8, "customer_order_backlog_refresh": 3, "delivery_schedule_visibility": 3, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "relative_strength_overextension": 8, "total": 33, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_theme_and_customer_order_visibility", "valuation_rerating_runway_required", "margin_revision_and_delivery_cadence_required"], "stage3_evidence_fields": ["fresh_customer_order_backlog_required", "valuation_runway_required_after_RS_move", "margin_revision_bridge_required"], "stage4b_evidence_fields": ["advanced_equipment_price_premium", "relative_strength_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_delivery_gap", "valuation_mean_reversion", "margin_revision_bridge_failure"], "symbol": "036930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "DEPOSITION_PROCESS_EQUIPMENT_VALUATION_BLOWOFF_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "advanced_equipment_valuation_blowoff_deposition_process_equipment_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C09 advanced-equipment rows should route to local 4B/Yellow when RS and valuation premium have already capitalized memory/HBM capex recovery and no incremental customer order, delivery cadence, backlog quality, valuation runway or margin-revision bridge has refreshed.",
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
3. Add C09-specific advanced equipment valuation / RS overextension / customer order / delivery cadence / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C09_BLOCK_GREEN_AFTER_VALUATION_BLOWOFF_WITHOUT_INCREMENTAL_ORDER_MARGIN_REVISION
- C09_EQUIPMENT_RS_PRICE_PREMIUM_LOCAL_4B
- C09_GREEN_REQUIRES_ORDER_BACKLOG_DELIVERY_MARGIN_AND_VALUATION_RUNWAY
- C09_PRICE_CONFIRMATION_WITHOUT_FRESH_ORDER_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

