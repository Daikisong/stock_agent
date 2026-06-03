# E2R V12 No-Repeat Standalone Residual Research
## R2 / L2 / C09 — Advanced equipment valuation blowoff guard

metadata:
```text
selected_round: R2
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: HBM_ADVANCED_EQUIPMENT_BLOWOFF_GREEN_STRICTNESS_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_hbm_equipment_blowoff_2024_research.md
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

This run avoids those top-covered C09 symbols and adds 232140, 240810, and 036930.  
Each row uses a new `C09 + symbol + trigger_type + entry_date` hard key. The same symbols may appear in other canonical archetypes, but this run is not a hard duplicate because the C09 valuation-blowoff purpose, trigger dates, and stage transitions are different.

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
232140 와이씨: 2024 forward window clean; corporate-action candidate is 2017-04-05.
240810 원익IPS: corporate_action_candidate_count=0.
036930 주성엔지니어링: 2024 forward window clean; corporate-action candidate is 2000-06-22.
```

## 3. Research thesis

C09 should not treat every HBM or advanced-equipment price run as a new Green. It is the point where the model asks whether the rerating has already eaten the evidence:

```text
advanced equipment / HBM capex attention
→ order or customer visibility claim
→ valuation expands faster than delivery and revision bridge
→ local 4B should activate
→ Green is blocked unless fresh backlog, delivery, margin, and revision keep runway open
```

The important residual is the second half of the equipment cycle. In C07, order relative strength can be useful early. In C09, the same signal becomes dangerous when the price has already capitalized the order story. A good telescope becomes a bad compass if the investor keeps staring at yesterday's star.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C09_232140_YC_20240613_HBM_TESTER_VALUATION_BLOWOFF_4B | 232140 | protective_4b_success | 2024-06-13 | 21900 | 22950 on 2024-06-13 | 8290 on 2024-12-09 | 4.79% | 4.79% | 4.79% | -62.15% | -63.88% |
| C09_240810_WONIKIPS_20240408_MEMORY_EQUIPMENT_PRICE_RUN_FALSE_GREEN | 240810 | advanced_equipment_false_green_counterexample | 2024-04-08 | 41650 | 44850 on 2024-04-08 | 27800 on 2024-09-11 | 7.68% | 7.68% | 7.68% | -33.25% | -38.02% |
| C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF | 036930 | deposition_equipment_false_green_counterexample | 2024-04-08 | 36500 | 41450 on 2024-04-08 | 22050 on 2024-09-09 | 13.56% | 13.56% | 13.56% | -39.59% | -46.8% |

## 5. Stage evidence split

### Stage2 / Stage3
- Advanced equipment and HBM-capex attention are valid routing signals.
- They are not automatically positive once valuation has already expanded.

### Stage3 / Green
- C09 Green should require fresh order/backlog, delivery schedule, margin bridge, and revision evidence after the price run.
- 240810 and 036930 show why relative strength alone is insufficient: the subsequent path had large drawdowns before the non-price bridge could justify the valuation.

### 4B
- 232140 is the protective 4B anchor. The HBM tester thesis had already been capitalized into a sharp June 2024 peak; local 4B discipline was more useful than fresh Green.
- 240810 and 036930 are softer but still clear valuation-blowoff rows: equipment beta became stale before delivery/revision evidence could expand runway.

### 4C
- No hard accounting break is asserted.
- The C09 break mode is valuation exhaustion: order language stays alive, but the stock no longer has enough evidence-weighted runway.

## 6. Raw component score breakdown

```json
{
  "C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 31,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C09_232140_YC_20240613_HBM_TESTER_VALUATION_BLOWOFF_4B": {
    "bottleneck_pricing_power": 11,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 4,
    "total": 43,
    "valuation_rerating_runway": 2,
    "visibility_quality": 10
  },
  "C09_240810_WONIKIPS_20240408_MEMORY_EQUIPMENT_PRICE_RUN_FALSE_GREEN": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 35,
    "valuation_rerating_runway": 3,
    "visibility_quality": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C09 guard:
```text
if advanced_equipment_price_run and no_fresh_order_delivery_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if hbm_equipment_order_story_already_capitalized:
    reduce_valuation_rerating_runway_score = true

if post_peak_drawdown and revision_bridge_fails_to_expand:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 240810 / 2024-04-08: memory equipment beta can be over-promoted if order/revision duration is not required after the price run.
- 036930 / 2024-04-08: advanced deposition equipment strength can look like Green, but the later drawdown argues for C09 local 4B / counterexample treatment.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -62.15, "MAE_30D_pct": -36.99, "MAE_90D_pct": -51.42, "MFE_180D_pct": 4.79, "MFE_30D_pct": 4.79, "MFE_90D_pct": 4.79, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_232140_YC_20240613_HBM_TESTER_VALUATION_BLOWOFF_4B", "case_role": "protective_4b_success", "company_name": "와이씨", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "C09 should treat the June blowoff as local 4B after HBM tester order visibility had been capitalized; it is not fresh Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.88, "entry_date": "2024-06-13", "entry_price": 21900, "evidence_family": "hbm_tester_equipment_valuation_blowoff_after_order_theme", "evidence_url_pending": false, "fine_archetype_id": "HBM_ADVANCED_EQUIPMENT_BLOWOFF_GREEN_STRICTNESS_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-12-09", "low_price_180d": 8290, "peak_date": "2024-06-13", "peak_price": 22950, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/232/232140.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 11, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 4, "total": 43, "valuation_rerating_runway": 2, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C09_232140_YC_20240613_HBM_TESTER_VALUATION_BLOWOFF_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_or_hbm_capex_attention", "relative_strength", "order_or_customer_visibility_claim"], "stage3_evidence_fields": ["fresh_order_or_backlog_confirmation_required", "delivery_and_margin_revision_bridge_required", "valuation_runway_after_price_run_required"], "stage4b_evidence_fields": ["equipment_valuation_blowoff", "price_premium_after_order_theme_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "capex_beta_mean_reversion", "valuation_without_delivery_margin_bridge"], "symbol": "232140", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "trigger_date": "2024-06-13", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -33.25, "MAE_30D_pct": -19.57, "MAE_90D_pct": -28.33, "MFE_180D_pct": 7.68, "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_240810_WONIKIPS_20240408_MEMORY_EQUIPMENT_PRICE_RUN_FALSE_GREEN", "case_role": "advanced_equipment_false_green_counterexample", "company_name": "원익IPS", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Memory/HBM equipment beta should stay Yellow or local 4B unless fresh backlog, delivery, and revision evidence justify further runway.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.02, "entry_date": "2024-04-08", "entry_price": 41650, "evidence_family": "memory_equipment_hbm_capex_beta_without_order_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "HBM_ADVANCED_EQUIPMENT_BLOWOFF_GREEN_STRICTNESS_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-11", "low_price_180d": 27800, "peak_date": "2024-04-08", "peak_price": 44850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/240/240810.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 5, "total": 35, "valuation_rerating_runway": 3, "visibility_quality": 7}, "reuse_reason": null, "same_entry_group_id": "C09_240810_WONIKIPS_20240408_MEMORY_EQUIPMENT_PRICE_RUN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_or_hbm_capex_attention", "relative_strength", "order_or_customer_visibility_claim"], "stage3_evidence_fields": ["fresh_order_or_backlog_confirmation_required", "delivery_and_margin_revision_bridge_required", "valuation_runway_after_price_run_required"], "stage4b_evidence_fields": ["equipment_valuation_blowoff", "price_premium_after_order_theme_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "capex_beta_mean_reversion", "valuation_without_delivery_margin_bridge"], "symbol": "240810", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.59, "MAE_30D_pct": -12.74, "MAE_90D_pct": -39.32, "MFE_180D_pct": 13.56, "MFE_30D_pct": 13.56, "MFE_90D_pct": 13.56, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "case_id": "C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF", "case_role": "deposition_equipment_false_green_counterexample", "company_name": "주성엔지니어링", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Advanced deposition/equipment relative strength should not become Green when valuation already capitalizes the capex story and revision evidence is insufficient.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.8, "entry_date": "2024-04-08", "entry_price": 36500, "evidence_family": "advanced_deposition_equipment_ai_memory_beta_without_revision_runway", "evidence_url_pending": false, "fine_archetype_id": "HBM_ADVANCED_EQUIPMENT_BLOWOFF_GREEN_STRICTNESS_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "low_date_180d": "2024-09-09", "low_price_180d": 22050, "peak_date": "2024-04-08", "peak_price": 41450, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/036/036930.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 31, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C09_036930_JUSUNG_20240408_DEPOSITION_EQUIPMENT_VALUATION_BLOWOFF", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R2", "source_proxy_only": false, "stage2_evidence_fields": ["advanced_equipment_or_hbm_capex_attention", "relative_strength", "order_or_customer_visibility_claim"], "stage3_evidence_fields": ["fresh_order_or_backlog_confirmation_required", "delivery_and_margin_revision_bridge_required", "valuation_runway_after_price_run_required"], "stage4b_evidence_fields": ["equipment_valuation_blowoff", "price_premium_after_order_theme_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["order_revision_gap", "capex_beta_mean_reversion", "valuation_without_delivery_margin_bridge"], "symbol": "036930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "trigger_date": "2024-04-08", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "HBM_ADVANCED_EQUIPMENT_BLOWOFF_GREEN_STRICTNESS_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "loop_contribution_label": "advanced_equipment_valuation_blowoff_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R2",
  "shadow_rule_candidate": "C09 advanced-equipment/HBM-capex rows should route late price-run entries to local 4B unless fresh order/backlog, delivery, margin and revision bridge keep valuation runway open; relative strength alone should not become Green.",
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
3. Add C09-specific valuation-blowoff guard only as a shadow candidate until more rows exist.

Candidate rule:
- C09_ADVANCED_EQUIPMENT_GREEN_REQUIRES_FRESH_ORDER_DELIVERY_MARGIN_REVISION
- C09_EQUIPMENT_PRICE_RUN_LOCAL_4B
- C09_ORDER_STORY_ALREADY_CAPITALIZED_RUNWAY_PENALTY
- C09_EQUIPMENT_BETA_WITHOUT_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

