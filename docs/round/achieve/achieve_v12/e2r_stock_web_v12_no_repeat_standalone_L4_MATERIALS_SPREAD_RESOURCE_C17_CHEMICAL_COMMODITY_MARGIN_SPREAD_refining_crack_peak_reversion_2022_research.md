# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C17 — Chemical commodity margin spread / refining crack peak-reversion 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: REFINING_CRACK_PEAK_REVERSION_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_date_trigger_family|counterexample_mining|positive_counterexample_balance|4B_gap_fill|peakcycle_refining_crack_spread_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_refining_crack_peak_reversion_2022_research.md
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

This run avoids those top-covered C17 symbols and uses new symbol/date/trigger-family combinations:
```text
C17 + 078930 + Stage2-Actionable + 2022-03-31
C17 + 096770 + 4B-local-price-only + 2022-06-03
C17 + 010950 + Stage3-Yellow + 2022-06-13
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
078930 GS: corporate_action_candidate_count=0; clean 2022 forward window.
096770 SK이노베이션: selected 2022 forward window clean; profile corporate-action candidate is 2024-11-20 and outside selected trigger window.
010950 S-Oil: selected post-2001 forward window clean; profile corporate-action candidate is 2001-12-03 and outside selected trigger window.
```

## 3. Research thesis

C17 should split real refining spread discovery from peak-cycle crack-spread optionality already paid in price:

```text
refining / chemical commodity spread and energy dislocation
→ realized crack-spread duration
→ utilization, volume and product-mix bridge
→ ASP/input-cost pass-through
→ inventory and working-capital quality
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A refining spread is a valve opening in the margin pipe. Stage2 can buy the first pressure when cracks, utilization and revisions are still rising. Green should not keep buying after the market has already priced the pressure and the next spread-to-margin proof has stopped arriving.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C17_078930_GS_20220331_REFINING_HOLDCO_SPREAD_STAGE2 | 078930 | positive_refining_holdco_spread_stage2_success_with_later_4b_refresh | 2022-03-31 | 43900 | 49350 on 2022-05-09 | 38300 on 2022-07-06 | 12.41% | 12.41% | 12.41% | -12.76% | -22.39% |
| C17_096770_SKINNO_20220603_REFINING_SPREAD_PEAK_4B | 096770 | integrated_refiner_crack_spread_peak_price_premium_counterexample | 2022-06-03 | 225500 | 246000 on 2022-06-09 | 142500 on 2022-09-30 | 9.09% | 9.09% | 9.09% | -36.81% | -42.07% |
| C17_010950_SOIL_20220613_REFINING_CRACK_PEAK_FALSE_GREEN | 010950 | pure_refiner_crack_spread_peak_false_green_counterexample | 2022-06-13 | 119000 | 123000 on 2022-06-13 | 77500 on 2022-09-28 | 3.36% | 3.36% | 3.36% | -34.87% | -36.99% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 078930 is the positive anchor. The March 2022 refining crack-spread/holdco route produced useful MFE before the May 2022 premium required 4B refresh discipline.
- Stage2 is allowed only when commodity-spread salience maps to realized spread duration, utilization/product mix, ASP/input-cost pass-through, inventory/working-capital quality and margin/revision visibility.

### Stage3 / Green
- C17 Green should require realized spread duration, utilization and product-mix persistence, input-cost pass-through, inventory discipline and margin/revision confirmation.
- 010950 is the false-Green/Yellow guard: peak-cycle refining spread confirmation was visible, but the June 2022 price had tiny residual upside and a much larger forward drawdown when new spread-to-margin evidence did not refresh.

### 4B
- 096770 fills the integrated-refiner crack-spread peak 4B pocket. The June 2022 trigger had limited MFE but a much larger full-window MAE.
- 010950 shows the same failure in pure refiner form: crack-spread optionality can remain directionally real while the listed-company earnings bridge is too stale for Green.
- 078930 also demonstrates that valid Stage2 evidence can become local 4B after the rerating capitalizes the refining-spread pipeline.

### 4C
- No hard refinery outage, inventory loss, liquidity break, customer loss or accounting break is asserted.
- The C17 break mode here is spread-to-margin exhaustion: the refining spread story may remain directionally real, but incremental spread duration, utilization, inventory and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C17_010950_SOIL_20220613_REFINING_CRACK_PEAK_FALSE_GREEN": {
    "ASP_input_cost_bridge": 4,
    "commodity_margin_spread_visibility": 8,
    "information_confidence": 3,
    "inventory_working_capital_quality": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "realized_spread_duration": 4,
    "total": 33,
    "utilization_or_volume_bridge": 4,
    "valuation_rerating_runway": 1
  },
  "C17_078930_GS_20220331_REFINING_HOLDCO_SPREAD_STAGE2": {
    "ASP_input_cost_bridge": 8,
    "commodity_margin_spread_visibility": 9,
    "information_confidence": 4,
    "inventory_working_capital_quality": 7,
    "margin_revision_bridge": 7,
    "market_mispricing": 8,
    "realized_spread_duration": 8,
    "total": 65,
    "utilization_or_volume_bridge": 7,
    "valuation_rerating_runway": 7
  },
  "C17_096770_SKINNO_20220603_REFINING_SPREAD_PEAK_4B": {
    "ASP_input_cost_bridge": 4,
    "commodity_margin_spread_visibility": 8,
    "information_confidence": 3,
    "inventory_working_capital_quality": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "realized_spread_duration": 4,
    "total": 33,
    "utilization_or_volume_bridge": 4,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C17 guard:
```text
if commodity_margin_spread and realized_spread_utilization_inventory_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if peakcycle_refining_spread_price_premium and no incremental_spread_duration_utilization_inventory_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 096770 / 2022-06-03: refining spread peak premium can be over-promoted if price strength substitutes for renewed spread duration, inventory quality and margin proof.
- 010950 / 2022-06-13: peak-cycle refining spread confirmation can look like Yellow-to-Green, but fails without refreshed spread-to-margin and revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.76, "MAE_30D_pct": -2.73, "MAE_90D_pct": -12.76, "MFE_180D_pct": 12.41, "MFE_30D_pct": 12.41, "MFE_90D_pct": 12.41, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_078930_GS_20220331_REFINING_HOLDCO_SPREAD_STAGE2", "case_role": "positive_refining_holdco_spread_stage2_success_with_later_4b_refresh", "company_name": "GS", "corporate_action_window_status": "corporate_action_candidate_count=0; clean 2022 forward window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when refining crack-spread expansion, oil-product supply dislocation and affiliate margin optionality were visible before the holdco spread option was fully capitalized. Green still requires realized crack-spread duration, product mix, utilization, inventory/working-capital quality and margin/revision confirmation; after the May 2022 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -22.39, "entry_date": "2022-03-31", "entry_price": 43900, "evidence_family": "refining_holdco_crack_spread_energy_dislocation_affiliate_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "REFINING_CRACK_PEAK_REVERSION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-07-06", "low_price_180d": 38300, "peak_date": "2022-05-09", "peak_price": 49350, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/078/078930.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 8, "commodity_margin_spread_visibility": 9, "information_confidence": 4, "inventory_working_capital_quality": 7, "margin_revision_bridge": 7, "market_mispricing": 8, "realized_spread_duration": 8, "total": 65, "utilization_or_volume_bridge": 7, "valuation_rerating_runway": 7}, "reuse_reason": null, "same_entry_group_id": "C17_078930_GS_20220331_REFINING_HOLDCO_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_margin_spread_visibility", "realized_spread_duration_and_utilization_bridge", "ASP_input_cost_inventory_working_capital_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "utilization_and_product_mix_persistence_required", "inventory_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["refining_crack_spread_peak_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["crack_spread_mean_reversion_or_inventory_loss", "working_capital_or_input_cost_pressure", "margin_revision_bridge_failure"], "symbol": "078930", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078930/2022.csv", "trigger_date": "2022-03-31", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -36.81, "MAE_30D_pct": -29.71, "MAE_90D_pct": -36.81, "MFE_180D_pct": 9.09, "MFE_30D_pct": 9.09, "MFE_90D_pct": 9.09, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_096770_SKINNO_20220603_REFINING_SPREAD_PEAK_4B", "case_role": "integrated_refiner_crack_spread_peak_price_premium_counterexample", "company_name": "SK이노베이션", "corporate_action_window_status": "selected 2022 forward window clean; profile corporate-action candidate is 2024-11-20 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Refining spread peak premium should route to local 4B/counterexample when the market has already capitalized product-spread optionality and fresh realized spread duration, utilization, inventory quality, working-capital and margin/revision evidence do not refresh. The June 2022 trigger had limited local MFE and a much larger full-window MAE.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.07, "entry_date": "2022-06-03", "entry_price": 225500, "evidence_family": "integrated_refiner_crack_spread_peak_premium_without_incremental_spread_duration_inventory_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "REFINING_CRACK_PEAK_REVERSION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-09-30", "low_price_180d": 142500, "peak_date": "2022-06-09", "peak_price": 246000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/096/096770.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 4, "commodity_margin_spread_visibility": 8, "information_confidence": 3, "inventory_working_capital_quality": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "realized_spread_duration": 4, "total": 33, "utilization_or_volume_bridge": 4, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C17_096770_SKINNO_20220603_REFINING_SPREAD_PEAK_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_margin_spread_visibility", "realized_spread_duration_and_utilization_bridge", "ASP_input_cost_inventory_working_capital_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "utilization_and_product_mix_persistence_required", "inventory_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["refining_crack_spread_peak_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["crack_spread_mean_reversion_or_inventory_loss", "working_capital_or_input_cost_pressure", "margin_revision_bridge_failure"], "symbol": "096770", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2022.csv", "trigger_date": "2022-06-03", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -34.87, "MAE_30D_pct": -27.23, "MAE_90D_pct": -34.87, "MFE_180D_pct": 3.36, "MFE_30D_pct": 3.36, "MFE_90D_pct": 3.36, "calibration_caveat": "", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_010950_SOIL_20220613_REFINING_CRACK_PEAK_FALSE_GREEN", "case_role": "pure_refiner_crack_spread_peak_false_green_counterexample", "company_name": "S-Oil", "corporate_action_window_status": "selected post-2001 forward window clean; profile corporate-action candidate is 2001-12-03 and outside selected trigger window", "current_profile_error": true, "current_profile_verdict": "Refining crack-spread peak confirmation should remain Yellow or local 4B when price strength is not backed by renewed realized spread duration, utilization, product mix, inventory discipline and margin/revision evidence. The June 2022 trigger had tiny residual upside and a much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -36.99, "entry_date": "2022-06-13", "entry_price": 119000, "evidence_family": "pure_refiner_crack_spread_peak_price_confirmation_without_incremental_spread_duration_inventory_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "REFINING_CRACK_PEAK_REVERSION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-09-28", "low_price_180d": 77500, "peak_date": "2022-06-13", "peak_price": 123000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010950.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 4, "commodity_margin_spread_visibility": 8, "information_confidence": 3, "inventory_working_capital_quality": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "realized_spread_duration": 4, "total": 33, "utilization_or_volume_bridge": 4, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C17_010950_SOIL_20220613_REFINING_CRACK_PEAK_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_margin_spread_visibility", "realized_spread_duration_and_utilization_bridge", "ASP_input_cost_inventory_working_capital_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "utilization_and_product_mix_persistence_required", "inventory_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["refining_crack_spread_peak_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["crack_spread_mean_reversion_or_inventory_loss", "working_capital_or_input_cost_pressure", "margin_revision_bridge_failure"], "symbol": "010950", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010950/2022.csv", "trigger_date": "2022-06-13", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "REFINING_CRACK_PEAK_REVERSION_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "chemical_commodity_margin_spread_refining_crack_peak_reversion_new_dates_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C17 refining/chemical commodity rows should allow Stage2 when realized crack-spread duration is backed by utilization, product mix, ASP-input-cost pass-through, inventory/working-capital quality and margin-revision bridge, but route peak-cycle refining spread premiums to Yellow/local 4B when incremental spread-to-margin evidence has not refreshed.",
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
3. Add C17-specific refining/chemical commodity spread / first-wave vs peak-cycle split / realized spread duration / utilization-product-mix / ASP-input-cost / inventory-working-capital / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C17_STAGE2_ALLOWED_ON_REALIZED_SPREAD_UTILIZATION_INVENTORY_MARGIN_REVISION_BRIDGE
- C17_GREEN_REQUIRES_SPREAD_DURATION_PRODUCT_MIX_INPUT_COST_INVENTORY_REVISION
- C17_PEAKCYCLE_REFINING_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C17_SPREAD_OPTIONALITY_WITHOUT_SPREAD_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

