# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C17 — Chemical commodity margin spread / late-cycle 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: PETROCHEMICAL_CHLORALKALI_LATE_CYCLE_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|late_cycle_spread_premium_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_petrochemical_chloralkali_late_cycle_4b_2021_research.md
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

This run avoids the top-covered C17 symbols and adds 006650, 298000, and 014830.  
Each row uses a new `C17 + symbol + trigger_type + entry_date` hard key.

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
006650 대한유화: selected 2021 forward window clean; corporate-action candidate is 2010-07-13, outside selected test window.
298000 효성화학: corporate_action_candidate_count=0.
014830 유니드: selected 2021 forward window clean; corporate-action candidates are 2015-08-18 and 2022-11-28, outside selected test window.
```

## 3. Research thesis

C17 should split fresh chemical spread expansion from late-cycle spread premium:

```text
chemical commodity spread attention
→ realized spread duration
→ shipment volume and utilization
→ raw-material/input-cost pass-through
→ inventory and working-capital quality
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A chemical spread is a tide running through pipes. Stage2 can ride the first tide when utilization and margins are rising, but Green should not keep buying the pipe after the tide is already priced and the feedstock bill is waiting.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C17_006650_DAEHANPETRO_20210106_PETROCHEMICAL_SPREAD_STAGE2 | 006650 | positive_petrochemical_spread_stage2_success_with_later_4b_refresh | 2021-01-06 | 277000 | 405500 on 2021-02-17 | 214500 on 2021-09-30 | 46.39% | 46.39% | 46.39% | -22.56% | -47.1% |
| C17_298000_HYOSUNGCHEM_20210916_PP_SPREAD_PRICE_PREMIUM_4B | 298000 | pp_spread_late_cycle_price_premium_counterexample | 2021-09-16 | 419500 | 426000 on 2021-09-17 | 257000 on 2021-11-03 | 1.55% | 1.55% | 1.55% | -38.74% | -39.67% |
| C17_014830_UNID_20210902_CHLORALKALI_SPREAD_FALSE_GREEN | 014830 | chloralkali_potash_spread_false_green_counterexample | 2021-09-02 | 145500 | 159000 on 2021-09-16 | 116000 on 2021-10-29 | 9.28% | 9.28% | 9.28% | -20.27% | -27.04% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 006650 is the positive anchor. Early 2021 petrochemical spread expansion produced a strong MFE before the premium required local 4B refresh discipline.
- Stage2 is allowed only when spread expansion is backed by actual utilization, shipment volume, input-cost pass-through and margin/revision visibility.

### Stage3 / Green
- C17 Green should require realized spread duration, downstream demand, shipment volume, utilization, raw-material cost bridge, inventory quality and margin/revision confirmation.
- 014830 is the false-Green guard: chlor-alkali/potash price confirmation did not provide enough renewed spread-duration, volume and margin bridge to protect the forward path.

### 4B
- 298000 fills the late-cycle PP/propane spread 4B pocket. The entry was very close to the peak and the later drawdown was much larger than residual upside.
- 014830 shows the same pattern in chlor-alkali/potash: a late-cycle spread rally can keep a real commodity story alive while the stock no longer has Green-quality evidence.
- 006650 also demonstrates that a valid Stage2 spread rerating can become local 4B once the spread cycle is capitalized.

### 4C
- No hard plant shutdown, feedstock procurement failure or accounting break is asserted.
- The C17 break mode is spread mean-reversion/evidence exhaustion: the spread may remain cyclically real, but incremental volume, feedstock pass-through, inventory quality and margin revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C17_006650_DAEHANPETRO_20210106_PETROCHEMICAL_SPREAD_STAGE2": {
    "downstream_demand_quality": 8,
    "information_confidence": 4,
    "input_cost_pass_through": 8,
    "inventory_working_capital_quality": 7,
    "margin_revision_bridge": 9,
    "market_mispricing": 9,
    "spread_duration_quality": 10,
    "total": 71,
    "valuation_rerating_runway": 7,
    "volume_utilization": 9
  },
  "C17_014830_UNID_20210902_CHLORALKALI_SPREAD_FALSE_GREEN": {
    "downstream_demand_quality": 4,
    "information_confidence": 3,
    "input_cost_pass_through": 3,
    "inventory_working_capital_quality": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "spread_duration_quality": 5,
    "total": 30,
    "valuation_rerating_runway": 1,
    "volume_utilization": 4
  },
  "C17_298000_HYOSUNGCHEM_20210916_PP_SPREAD_PRICE_PREMIUM_4B": {
    "downstream_demand_quality": 3,
    "information_confidence": 3,
    "input_cost_pass_through": 3,
    "inventory_working_capital_quality": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "spread_duration_quality": 5,
    "total": 28,
    "valuation_rerating_runway": 1,
    "volume_utilization": 4
  }
}
```

## 7. Current calibrated profile stress test

Suggested C17 guard:
```text
if chemical_spread_expansion and realized_spread_volume_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if late_cycle_chemical_spread_price_premium and no incremental_spread_duration_volume_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 298000 / 2021-09-16: late-cycle PP/propane spread premium can be over-promoted if the model treats price heat as fresh spread-duration and margin-revision proof.
- 014830 / 2021-09-02: chlor-alkali/potash spread confirmation can look like Yellow-to-Green, but fails without renewed volume and margin bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -22.56, "MAE_30D_pct": -9.93, "MAE_90D_pct": -9.93, "MFE_180D_pct": 46.39, "MFE_30D_pct": 46.39, "MFE_90D_pct": 46.39, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_006650_DAEHANPETRO_20210106_PETROCHEMICAL_SPREAD_STAGE2", "case_role": "positive_petrochemical_spread_stage2_success_with_later_4b_refresh", "company_name": "대한유화", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidate is 2010-07-13 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when petrochemical spread expansion, utilization and margin leverage were visible before the rerating was fully capitalized. Green still requires realized spread duration, shipment volume, naphtha/input-cost pass-through, downstream demand, inventory and revision confirmation; after the February 2021 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.1, "entry_date": "2021-01-06", "entry_price": 277000, "evidence_family": "petrochemical_naphtha_olefin_spread_utilization_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "PETROCHEMICAL_CHLORALKALI_LATE_CYCLE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-09-30", "low_price_180d": 214500, "peak_date": "2021-02-17", "peak_price": 405500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006650.json", "raw_component_score_breakdown": {"downstream_demand_quality": 8, "information_confidence": 4, "input_cost_pass_through": 8, "inventory_working_capital_quality": 7, "margin_revision_bridge": 9, "market_mispricing": 9, "spread_duration_quality": 10, "total": 71, "valuation_rerating_runway": 7, "volume_utilization": 9}, "reuse_reason": null, "same_entry_group_id": "C17_006650_DAEHANPETRO_20210106_PETROCHEMICAL_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "realized_spread_duration_and_utilization_visibility", "input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "shipment_volume_utilization_inventory_required", "naphtha_propane_raw_material_input_cost_and_margin_revision_required"], "stage4b_evidence_fields": ["chemical_spread_late_cycle_price_premium", "spread_supercycle_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "volume_or_downstream_demand_disappointment", "inventory_working_capital_or_margin_revision_bridge_failure"], "symbol": "006650", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "trigger_date": "2021-01-06", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -38.74, "MAE_30D_pct": -31.59, "MAE_90D_pct": -38.74, "MFE_180D_pct": 1.55, "MFE_30D_pct": 1.55, "MFE_90D_pct": 1.55, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_298000_HYOSUNGCHEM_20210916_PP_SPREAD_PRICE_PREMIUM_4B", "case_role": "pp_spread_late_cycle_price_premium_counterexample", "company_name": "효성화학", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2021_forward_window", "current_profile_error": true, "current_profile_verdict": "PP/propane spread price premium should route to local 4B or counterexample when the stock has already capitalized spread expansion and incremental realized spread duration, utilization, input-cost pass-through, working-capital and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -39.67, "entry_date": "2021-09-16", "entry_price": 419500, "evidence_family": "polypropylene_propane_spread_price_premium_without_incremental_spread_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "PETROCHEMICAL_CHLORALKALI_LATE_CYCLE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-03", "low_price_180d": 257000, "peak_date": "2021-09-17", "peak_price": 426000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/298/298000.json", "raw_component_score_breakdown": {"downstream_demand_quality": 3, "information_confidence": 3, "input_cost_pass_through": 3, "inventory_working_capital_quality": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "spread_duration_quality": 5, "total": 28, "valuation_rerating_runway": 1, "volume_utilization": 4}, "reuse_reason": null, "same_entry_group_id": "C17_298000_HYOSUNGCHEM_20210916_PP_SPREAD_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "realized_spread_duration_and_utilization_visibility", "input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "shipment_volume_utilization_inventory_required", "naphtha_propane_raw_material_input_cost_and_margin_revision_required"], "stage4b_evidence_fields": ["chemical_spread_late_cycle_price_premium", "spread_supercycle_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "volume_or_downstream_demand_disappointment", "inventory_working_capital_or_margin_revision_bridge_failure"], "symbol": "298000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298000/2021.csv", "trigger_date": "2021-09-16", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -20.27, "MAE_30D_pct": -19.93, "MAE_90D_pct": -20.27, "MFE_180D_pct": 9.28, "MFE_30D_pct": 9.28, "MFE_90D_pct": 9.28, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_014830_UNID_20210902_CHLORALKALI_SPREAD_FALSE_GREEN", "case_role": "chloralkali_potash_spread_false_green_counterexample", "company_name": "유니드", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidates are 2015-08-18 and 2022-11-28, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Chlor-alkali/potash spread confirmation should stay Yellow when price confirmation is not followed by renewed spread duration, volume/utilization, raw-material cost bridge, inventory quality and margin/revision evidence. The late-cycle price premium did not protect the forward path.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -27.04, "entry_date": "2021-09-02", "entry_price": 145500, "evidence_family": "chloralkali_potash_spread_price_confirmation_without_incremental_volume_inputcost_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "PETROCHEMICAL_CHLORALKALI_LATE_CYCLE_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-10-29", "low_price_180d": 116000, "peak_date": "2021-09-16", "peak_price": 159000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/014/014830.json", "raw_component_score_breakdown": {"downstream_demand_quality": 4, "information_confidence": 3, "input_cost_pass_through": 3, "inventory_working_capital_quality": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "spread_duration_quality": 5, "total": 30, "valuation_rerating_runway": 1, "volume_utilization": 4}, "reuse_reason": null, "same_entry_group_id": "C17_014830_UNID_20210902_CHLORALKALI_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "realized_spread_duration_and_utilization_visibility", "input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "shipment_volume_utilization_inventory_required", "naphtha_propane_raw_material_input_cost_and_margin_revision_required"], "stage4b_evidence_fields": ["chemical_spread_late_cycle_price_premium", "spread_supercycle_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "volume_or_downstream_demand_disappointment", "inventory_working_capital_or_margin_revision_bridge_failure"], "symbol": "014830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2021.csv", "trigger_date": "2021-09-02", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "PETROCHEMICAL_CHLORALKALI_LATE_CYCLE_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "chemical_commodity_margin_spread_late_cycle_4b_gap_fill",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C17 chemical commodity spread rows should allow Stage2 when realized spread duration is backed by utilization, shipment volume, input-cost pass-through, inventory quality and margin/revision bridge, but late-cycle chemical spread price premium should route to local 4B or Yellow when incremental spread, volume and margin evidence have not refreshed.",
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
3. Add C17-specific chemical commodity spread / late-cycle price premium / input-cost / inventory / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C17_STAGE2_ALLOWED_ON_REALIZED_SPREAD_VOLUME_MARGIN_REVISION_BRIDGE
- C17_GREEN_REQUIRES_SPREAD_DURATION_VOLUME_INPUT_COST_INVENTORY_REVISION
- C17_LATE_CYCLE_CHEMICAL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C17_SPREAD_PRICE_CONFIRMATION_WITHOUT_INCREMENTAL_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

