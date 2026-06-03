# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C17 — Chemical commodity margin-spread duration guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: REFINING_AROMATIC_PP_SPREAD_DURATION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_refining_aromatic_chemical_spread_2022_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD current coverage:
rows=29, symbols=8, date range=2020-08-03~2024-07-15, good/bad S2=10/5, 4B/4C=0/0
top covered symbols: 298020(7), 011780(5), 010060(3), 011170(3), 004000(2)
```

This run avoids those top-covered C17 symbols and adds 010950, 120110, and 298000.  
Each row uses a new `C17 + symbol + trigger_type + entry_date` hard key.

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
010950 S-Oil: 2022 window clean; corporate-action candidate is 2001-12-03.
120110 코오롱인더: 2022 window clean; corporate-action candidate is 2010-12-27.
298000 효성화학: corporate_action_candidate_count=0.
```

## 3. Research thesis

C17 should not treat every chemical or refining rally as durable rerating. The mechanism must close:

```text
spread widening
→ margin bridge
→ revision confirmation
→ duration evidence
→ rerating
```

The positive anchor is S-Oil's 2022 refining spread window. The counterexamples show why C17 needs a duration guard: industrial-material and PP/propane stories can rally briefly, then collapse when cost, inventory, or balance-sheet pressure overwhelms the spread thesis.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C17_010950_SOIL_20220328_REFINING_SPREAD_STAGE2_4B | 010950 | positive_spread_success_but_4b_required | 2022-03-28 | 97900 | 123000 on 2022-06-13 | 77500 on 2022-09-28 | 12.87% | 25.64% | 25.64% | -20.84% | -36.99% |
| C17_120110_KOLONIND_20220504_AROMATIC_SPREAD_FALSE_GREEN | 120110 | false_green_counterexample | 2022-05-04 | 67200 | 69900 on 2022-05-06 | 40900 on 2022-10-26 | 4.02% | 4.02% | 4.02% | -39.14% | -41.49% |
| C17_298000_HYOSUNGCHEM_20220209_PP_PROPANE_SPREAD_FALSE_GREEN | 298000 | commodity_margin_4c_watch_counterexample | 2022-02-09 | 264500 | 306000 on 2022-02-17 | 99900 on 2022-10-31 | 13.42% | 15.69% | 15.69% | -62.23% | -67.35% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Spread widening and relative strength are valid early research routes.
- S-Oil shows that a refining spread window can produce a tradable Stage2-to-rerating move.

### Stage3 / Green
- C17 Green should require duration and transmission: the spread must reach margin and revision evidence.
- Price strength alone is not enough, because spread cycles can turn like a tide: the same water that lifts the boat can pull it back out.

### 4B
- S-Oil required local 4B discipline after the June 2022 peak.
- Chemical spread winners can become 4B even when the original thesis was valid.

### 4C
- 코오롱인더 and 효성화학 are false-Green / 4C-watch examples.
- The failure mode is spread mean reversion plus cost, inventory, cash-flow, or balance-sheet pressure.

## 6. Raw component score breakdown

```json
{
  "C17_010950_SOIL_20220328_REFINING_SPREAD_STAGE2_4B": {
    "bottleneck_pricing_power": 11,
    "capital_allocation": 3,
    "eps_fcf_explosion": 12,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 58,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  },
  "C17_120110_KOLONIND_20220504_AROMATIC_SPREAD_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 6,
    "total": 34,
    "valuation_rerating_runway": 4,
    "visibility_quality": 6
  },
  "C17_298000_HYOSUNGCHEM_20220209_PP_PROPANE_SPREAD_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 24,
    "valuation_rerating_runway": 3,
    "visibility_quality": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C17 guard:
```text
if chemical_or_refining_spread_signal and no margin_revision_duration_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if spread_price_run and duration_evidence_fades:
    route_to_local_4B_watch = true

if spread_mean_reversion plus cashflow_or_balance_sheet_pressure:
    escalate_to_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 120110 / 2022-05-04: short industrial-material spread strength could be over-promoted if duration is not required.
- 298000 / 2022-02-09: PP/chemical margin story became a deep drawdown path; Green should be blocked and 4C-watch should activate.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -20.84, "MAE_30D_pct": -3.78, "MAE_90D_pct": -3.78, "MFE_180D_pct": 25.64, "MFE_30D_pct": 12.87, "MFE_90D_pct": 25.64, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_010950_SOIL_20220328_REFINING_SPREAD_STAGE2_4B", "case_role": "positive_spread_success_but_4b_required", "company_name": "S-Oil", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was usable when refining spread widened, but Green must require margin/revision duration; after peak, local 4B discipline was needed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -36.99, "entry_date": "2022-03-28", "entry_price": 97900, "evidence_family": "refining_crack_spread_margin_rerating_then_mean_reversion", "evidence_url_pending": false, "fine_archetype_id": "REFINING_AROMATIC_PP_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-09-28", "low_price_180d": 77500, "peak_date": "2022-06-13", "peak_price": 123000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010950.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 11, "capital_allocation": 3, "eps_fcf_explosion": 12, "information_confidence": 4, "market_mispricing": 10, "total": 58, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C17_010950_SOIL_20220328_REFINING_SPREAD_STAGE2_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_or_refining_spread_signal", "relative_strength", "margin_expansion_claim"], "stage3_evidence_fields": ["spread_duration_evidence_required", "margin_or_revision_bridge_required", "raw_material_cost_pass_through_required"], "stage4b_evidence_fields": ["spread_cycle_saturation", "valuation_or_price_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "cost_pressure_or_inventory_loss", "balance_sheet_or_cashflow_pressure"], "symbol": "010950", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010950/2022.csv", "trigger_date": "2022-03-28", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.14, "MAE_30D_pct": -7.14, "MAE_90D_pct": -28.42, "MFE_180D_pct": 4.02, "MFE_30D_pct": 4.02, "MFE_90D_pct": 4.02, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_120110_KOLONIND_20220504_AROMATIC_SPREAD_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "코오롱인더", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "A spread/industrial-material rally should stay Yellow unless duration and revision bridge close; this path argues against Green on short relative strength.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.49, "entry_date": "2022-05-04", "entry_price": 67200, "evidence_family": "aromatic_film_industrial_material_spread_without_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "REFINING_AROMATIC_PP_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-10-26", "low_price_180d": 40900, "peak_date": "2022-05-06", "peak_price": 69900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/120/120110.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 6, "total": 34, "valuation_rerating_runway": 4, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C17_120110_KOLONIND_20220504_AROMATIC_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_or_refining_spread_signal", "relative_strength", "margin_expansion_claim"], "stage3_evidence_fields": ["spread_duration_evidence_required", "margin_or_revision_bridge_required", "raw_material_cost_pass_through_required"], "stage4b_evidence_fields": ["spread_cycle_saturation", "valuation_or_price_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "cost_pressure_or_inventory_loss", "balance_sheet_or_cashflow_pressure"], "symbol": "120110", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/120/120110/2022.csv", "trigger_date": "2022-05-04", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -62.23, "MAE_30D_pct": -10.02, "MAE_90D_pct": -25.14, "MFE_180D_pct": 15.69, "MFE_30D_pct": 13.42, "MFE_90D_pct": 15.69, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_298000_HYOSUNGCHEM_20220209_PP_PROPANE_SPREAD_FALSE_GREEN", "case_role": "commodity_margin_4c_watch_counterexample", "company_name": "효성화학", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Commodity spread improvement did not translate into durable EPS/FCF; Green should be blocked and 4C-watch should activate when spread and balance-sheet pressure worsen.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.35, "entry_date": "2022-02-09", "entry_price": 264500, "evidence_family": "pp_propane_or_commodity_margin_story_without_balance_sheet_cost_bridge", "evidence_url_pending": false, "fine_archetype_id": "REFINING_AROMATIC_PP_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-10-31", "low_price_180d": 99900, "peak_date": "2022-02-17", "peak_price": 306000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/298/298000.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 24, "valuation_rerating_runway": 3, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C17_298000_HYOSUNGCHEM_20220209_PP_PROPANE_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_or_refining_spread_signal", "relative_strength", "margin_expansion_claim"], "stage3_evidence_fields": ["spread_duration_evidence_required", "margin_or_revision_bridge_required", "raw_material_cost_pass_through_required"], "stage4b_evidence_fields": ["spread_cycle_saturation", "valuation_or_price_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "cost_pressure_or_inventory_loss", "balance_sheet_or_cashflow_pressure"], "symbol": "298000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298000/2022.csv", "trigger_date": "2022-02-09", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "REFINING_AROMATIC_PP_SPREAD_DURATION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "commodity_spread_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C17 chemical/refining spread rerating should permit Stage2 on spread widening, but Stage3 Green requires duration, margin/revision bridge, and cost-pass-through evidence; short spread rallies without bridge should remain Yellow or route to local 4B/4C-watch.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C17 + symbol + trigger_type + entry_date.
3. Add C17-specific spread-duration / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C17_SPREAD_GREEN_REQUIRES_MARGIN_REVISION_DURATION
- C17_SPREAD_PRICE_RUN_LOCAL_4B
- C17_SPREAD_MEAN_REVERSION_CASHFLOW_4C_WATCH

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

