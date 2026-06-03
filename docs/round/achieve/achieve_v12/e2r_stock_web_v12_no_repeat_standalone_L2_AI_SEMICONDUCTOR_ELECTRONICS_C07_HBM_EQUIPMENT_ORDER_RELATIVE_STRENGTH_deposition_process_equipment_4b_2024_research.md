# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C07 — HBM equipment order relative strength / deposition-process equipment 4B guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: DEPOSITION_PROCESS_EQUIPMENT_ORDER_RS_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|equipment_RS_to_order_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_deposition_process_equipment_4b_2024_research.md
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

This run avoids those top-covered C07 symbols and adds 084370, 240810, and 036930.  
Each row uses a new `C07 + symbol + trigger_type + entry_date` hard key:
```text
C07 + 084370 + Stage2-Actionable + 2024-03-21
C07 + 240810 + 4B-local-price-only + 2024-04-08
C07 + 036930 + Stage3-Yellow + 2024-04-08
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

C07 should distinguish equipment relative strength that converts into customer order/backlog and margin revision from equipment beta already capitalized by the HBM cycle:

```text
HBM / memory capex salience
→ direct equipment customer order or backlog quality
→ delivery cadence and capacity/tool acceptance
→ relative strength versus semi equipment peers
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

Equipment relative strength is a smoke signal from the fab. Stage2 can buy it when the smoke is tied to a purchase order, delivery slot and margin revision. Green should not pay for smoke alone after the whole equipment group has already rerated.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C07_084370_EUGENETECH_20240321_HBM_DEPOSITION_ORDER_RS_STAGE2 | 084370 | positive_deposition_equipment_order_relative_strength_stage2_success_with_later_4b_refresh | 2024-03-21 | 41450 | 60000 on 2024-05-28 | 32450 on 2024-11-19 | 41.62% | 44.75% | 44.75% | -21.71% | -45.92% |
| C07_240810_WONIKIPS_20240408_HBM_EQUIPMENT_RS_PRICE_PREMIUM_4B | 240810 | HBM_equipment_relative_strength_price_premium_counterexample | 2024-04-08 | 41650 | 44850 on 2024-04-08 | 22200 on 2024-11-14 | 7.68% | 7.68% | 7.68% | -46.7% | -50.5% |
| C07_036930_JUSUNG_20240408_DEPOSITION_RS_FALSE_GREEN | 036930 | deposition_equipment_relative_strength_false_green_counterexample | 2024-04-08 | 36500 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 13.56% | 13.56% | 13.56% | -39.59% | -46.8% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 084370 is the positive anchor. The March 2024 deposition-equipment RS route produced strong 30D/90D MFE before the May 2024 premium required 4B refresh discipline.
- Stage2 is allowed only when HBM/memory capex salience maps to direct order/backlog, customer quality, delivery cadence and margin/revision visibility.

### Stage3 / Green
- C07 Green should require direct customer order conversion, delivery schedule/backlog quality, memory-node or HBM capacity relevance, margin/revision bridge and valuation runway.
- 036930 is the false-Green/Yellow guard: process-equipment RS was visible, but the April 2024 price confirmation had small residual upside and much larger forward MAE when order-to-margin evidence did not refresh.

### 4B
- 240810 fills the HBM/equipment RS price-premium 4B pocket. The April 2024 trigger had a high local peak but weak residual runway and a much larger drawdown.
- 036930 shows the same failure in deposition/process-equipment beta: strong theme RS can become local 4B when the market has already capitalized memory capex recovery.
- 084370 also demonstrates that valid Stage2 can become local 4B after the rerating capitalizes the equipment order pipeline.

### 4C
- No hard customer cancellation, capex cut, delivery failure, or accounting break is asserted.
- The C07 break mode is order-to-margin exhaustion: HBM equipment salience may remain real, but incremental customer order, delivery cadence and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C07_036930_JUSUNG_20240408_DEPOSITION_RS_FALSE_GREEN": {
    "HBM_or_memory_capex_visibility": 8,
    "customer_quality_and_delivery_cadence": 4,
    "equipment_order_or_backlog_quality": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "relative_strength_quality": 6,
    "total": 33,
    "valuation_rerating_runway": 1
  },
  "C07_084370_EUGENETECH_20240321_HBM_DEPOSITION_ORDER_RS_STAGE2": {
    "HBM_or_memory_capex_visibility": 9,
    "customer_quality_and_delivery_cadence": 7,
    "equipment_order_or_backlog_quality": 8,
    "information_confidence": 4,
    "margin_revision_bridge": 7,
    "market_mispricing": 8,
    "relative_strength_quality": 9,
    "total": 59,
    "valuation_rerating_runway": 7
  },
  "C07_240810_WONIKIPS_20240408_HBM_EQUIPMENT_RS_PRICE_PREMIUM_4B": {
    "HBM_or_memory_capex_visibility": 8,
    "customer_quality_and_delivery_cadence": 4,
    "equipment_order_or_backlog_quality": 4,
    "information_confidence": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "relative_strength_quality": 6,
    "total": 33,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C07 guard:
```text
if HBM_equipment_RS and customer_order_delivery_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if equipment_RS_price_premium and no incremental_order_backlog_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and order_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 240810 / 2024-04-08: HBM equipment RS premium can be over-promoted if price heat substitutes for direct order/backlog and margin proof.
- 036930 / 2024-04-08: deposition/process-equipment confirmation can look like Yellow-to-Green, but fails without renewed customer order and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -21.71, "MAE_30D_pct": -6.15, "MAE_90D_pct": -6.15, "MFE_180D_pct": 44.75, "MFE_30D_pct": 41.62, "MFE_90D_pct": 44.75, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_084370_EUGENETECH_20240321_HBM_DEPOSITION_ORDER_RS_STAGE2", "case_role": "positive_deposition_equipment_order_relative_strength_stage2_success_with_later_4b_refresh", "company_name": "유진테크", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when deposition/process-equipment relative strength appeared with memory capex recovery, customer order visibility and margin/revision optionality before the rerating was fully capitalized. Green still requires named customer/order conversion, backlog delivery cadence, memory-node/HBM capacity relevance, margin/revision bridge and valuation runway; after the May 2024 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -45.92, "entry_date": "2024-03-21", "entry_price": 41450, "evidence_family": "HBM_DRAM_deposition_equipment_customer_order_relative_strength_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PROCESS_EQUIPMENT_ORDER_RS_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-19", "low_price_180d": 32450, "peak_date": "2024-05-28", "peak_price": 60000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/084/084370.json", "raw_component_score_breakdown": {"HBM_or_memory_capex_visibility": 9, "customer_quality_and_delivery_cadence": 7, "equipment_order_or_backlog_quality": 8, "information_confidence": 4, "margin_revision_bridge": 7, "market_mispricing": 8, "relative_strength_quality": 9, "total": 59, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C07_084370_EUGENETECH_20240321_HBM_DEPOSITION_ORDER_RS_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_or_memory_capex_visibility", "equipment_order_or_backlog_quality", "relative_strength_with_margin_revision_route"], "stage3_evidence_fields": ["direct_customer_order_conversion_required", "delivery_schedule_and_backlog_quality_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["HBM_equipment_relative_strength_price_premium", "equipment_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_backlog_gap", "delivery_schedule_delay_or_capex_cut", "margin_revision_bridge_failure"], "symbol": "084370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv", "trigger_date": "2024-03-21", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -46.7, "MAE_30D_pct": -19.57, "MAE_90D_pct": -19.57, "MFE_180D_pct": 7.68, "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_240810_WONIKIPS_20240408_HBM_EQUIPMENT_RS_PRICE_PREMIUM_4B", "case_role": "HBM_equipment_relative_strength_price_premium_counterexample", "company_name": "원익IPS", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2024_forward_window", "current_profile_error": true, "current_profile_verdict": "HBM/equipment relative-strength price premium should route to local 4B or counterexample when the market has already capitalized memory capex recovery and incremental order conversion, delivery schedule, backlog quality and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.5, "entry_date": "2024-04-08", "entry_price": 41650, "evidence_family": "HBM_DRAM_equipment_price_premium_without_incremental_order_backlog_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PROCESS_EQUIPMENT_ORDER_RS_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-11-14", "low_price_180d": 22200, "peak_date": "2024-04-08", "peak_price": 44850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/240/240810.json", "raw_component_score_breakdown": {"HBM_or_memory_capex_visibility": 8, "customer_quality_and_delivery_cadence": 4, "equipment_order_or_backlog_quality": 4, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "relative_strength_quality": 6, "total": 33, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C07_240810_WONIKIPS_20240408_HBM_EQUIPMENT_RS_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_or_memory_capex_visibility", "equipment_order_or_backlog_quality", "relative_strength_with_margin_revision_route"], "stage3_evidence_fields": ["direct_customer_order_conversion_required", "delivery_schedule_and_backlog_quality_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["HBM_equipment_relative_strength_price_premium", "equipment_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_backlog_gap", "delivery_schedule_delay_or_capex_cut", "margin_revision_bridge_failure"], "symbol": "240810", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.59, "MAE_30D_pct": -13.29, "MAE_90D_pct": -13.7, "MFE_180D_pct": 13.56, "MFE_30D_pct": 13.56, "MFE_90D_pct": 13.56, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07_036930_JUSUNG_20240408_DEPOSITION_RS_FALSE_GREEN", "case_role": "deposition_equipment_relative_strength_false_green_counterexample", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2000-06-22 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Deposition/process-equipment relative-strength confirmation should stay Yellow or route to local 4B when price strength is not followed by fresh customer order conversion, delivery cadence, backlog quality and margin/revision evidence. The April 2024 spike had limited residual upside and a much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-04-08", "entry_price": 36500, "evidence_family": "deposition_equipment_relative_strength_price_confirmation_without_incremental_customer_order_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "DEPOSITION_PROCESS_EQUIPMENT_ORDER_RS_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 22050, "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/036/036930.json", "raw_component_score_breakdown": {"HBM_or_memory_capex_visibility": 8, "customer_quality_and_delivery_cadence": 4, "equipment_order_or_backlog_quality": 4, "information_confidence": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "relative_strength_quality": 6, "total": 33, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C07_036930_JUSUNG_20240408_DEPOSITION_RS_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["HBM_or_memory_capex_visibility", "equipment_order_or_backlog_quality", "relative_strength_with_margin_revision_route"], "stage3_evidence_fields": ["direct_customer_order_conversion_required", "delivery_schedule_and_backlog_quality_required", "margin_revision_and_valuation_runway_required"], "stage4b_evidence_fields": ["HBM_equipment_relative_strength_price_premium", "equipment_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_order_or_backlog_gap", "delivery_schedule_delay_or_capex_cut", "margin_revision_bridge_failure"], "symbol": "036930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "DEPOSITION_PROCESS_EQUIPMENT_ORDER_RS_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "HBM_equipment_order_relative_strength_deposition_process_equipment_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C07 HBM/equipment relative-strength rows should allow Stage2 when equipment RS is tied to direct customer order/backlog, delivery cadence, HBM/memory capex relevance and margin/revision bridge, but route late-cycle equipment RS price premiums to Yellow/local 4B when order-to-margin evidence has not refreshed.",
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
3. Add C07-specific HBM equipment RS / customer order / delivery cadence / backlog quality / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C07_STAGE2_ALLOWED_ON_CUSTOMER_ORDER_DELIVERY_MARGIN_REVISION_BRIDGE
- C07_GREEN_REQUIRES_DIRECT_BACKLOG_HBM_CAPACITY_RELEVANCE_REVISION
- C07_EQUIPMENT_RS_PRICE_PREMIUM_LOCAL_4B
- C07_RELATIVE_STRENGTH_WITHOUT_ORDER_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

