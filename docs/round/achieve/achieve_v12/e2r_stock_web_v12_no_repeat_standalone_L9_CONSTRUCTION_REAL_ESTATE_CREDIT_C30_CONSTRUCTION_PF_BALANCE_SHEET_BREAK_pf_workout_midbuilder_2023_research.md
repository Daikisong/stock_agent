# E2R V12 No-Repeat Standalone Residual Research
## R10 / L9 / C30 — Construction PF balance-sheet break guard

metadata:
```text
selected_round: R10
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L9_CONSTRUCTION_REAL_ESTATE_CREDIT
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_WORKOUT_MIDBUILDER_LIQUIDITY_REFINANCING_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|4B_4C_guard_validation|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L9_CONSTRUCTION_REAL_ESTATE_CREDIT_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_pf_workout_midbuilder_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK current coverage:
rows=28, symbols=6, date range=2022-01-12~2024-08-27, good/bad S2=5/0, 4B/4C=0/4
top covered symbols: 006360(6), 294870(5), 375500(4), UNKNOWN_SYMBOL(3), 000720(2)
```

This run avoids those top-covered C30 symbols and adds 009410, 002410, and 005960.  
Each row uses a new `C30 + symbol + trigger_type + entry_date` hard key.

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
009410 태영건설: 2023/2024 event window uses tradable rows; later 2024 trading interruption/restructuring caveat is noted.
002410 범양건영: 2023/2024 forward window clean relative to old corporate-action candidates.
005960 동부건설: 2023/2024 forward window clean relative to old corporate-action candidates.
```

## 3. Research thesis

C30 should not treat every construction rally as balance-sheet repair. It should separate three states:

```text
PF / credit stress appears
→ liquidity, refinancing, receivables, unsold inventory and guarantees must be checked
→ if workout/default risk becomes company-survival risk, hard 4C
→ if price rebounds without balance-sheet repair, local 4B or Yellow
```

The central mechanism is cash timing. Construction PF risk is not a normal demand slowdown. It is a bridge: if refinancing, project cash collection, and guarantees do not meet on the same day, the bridge can break even while the reported backlog still looks passable.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C30_009410_TAEYOUNG_20231213_PF_WORKOUT_HARD_4C | 009410 | hard_4c_protective_success | 2023-12-13 | 3270 | 4110 on 2024-01-11 | 1935 on 2023-12-28 | 25.69% | 25.69% | 25.69% | -40.83% | -46.96% |
| C30_002410_BUMYANG_20231208_PF_SMALLCAP_RELIEF_RALLY_LOCAL_4B | 002410 | pf_relief_rally_blowoff_counterexample | 2023-12-08 | 2445 | 2930 on 2023-12-11 | 1367 on 2024-04-08 | 19.84% | 19.84% | 19.84% | -44.09% | -53.34% |
| C30_005960_DONGBU_20231201_MIDBUILDER_PF_CREDIT_SPREAD_WATCH | 005960 | midbuilder_pf_credit_watch_false_green_counterexample | 2023-12-01 | 6070 | 6800 on 2023-12-01 | 4850 on 2024-04-12 | 12.03% | 12.03% | 12.03% | -20.1% | -28.68% |

## 5. Stage evidence split

### Stage2 / Stage3
- PF credit-spread or construction relief attention can be a research route, but it is not positive evidence by itself.
- Stage3 Green should require liquidity runway, refinancing, project cash collection, unsold-inventory improvement, and guarantee-exposure evidence.

### 4B
- 002410 is the relief-rally 4B/counterexample row: price spiked first, but without balance-sheet repair the following path was a deep drawdown.
- 005960 is a mid-builder credit-watch example: a modest price premium did not close into durable repair, so Green should stay blocked.

### 4C
- 009410 is the hard 4C anchor. Once PF liquidity and workout risk reached company-survival level, technical rebounds were no longer positive evidence.
- This is the C30 distinction: the market may still trade the stock, but the investment thesis has moved from rerating to solvency triage.

## 6. Raw component score breakdown

```json
{
  "C30_002410_BUMYANG_20231208_PF_SMALLCAP_RELIEF_RALLY_LOCAL_4B": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 1,
    "eps_fcf_explosion": 3,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 20,
    "valuation_rerating_runway": 2,
    "visibility_quality": 4
  },
  "C30_005960_DONGBU_20231201_MIDBUILDER_PF_CREDIT_SPREAD_WATCH": {
    "bottleneck_pricing_power": 3,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 25,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C30_009410_TAEYOUNG_20231213_PF_WORKOUT_HARD_4C": {
    "bottleneck_pricing_power": 1,
    "capital_allocation": 0,
    "eps_fcf_explosion": 0,
    "information_confidence": 5,
    "market_mispricing": 2,
    "total": 10,
    "valuation_rerating_runway": 0,
    "visibility_quality": 2
  }
}
```

## 7. Current calibrated profile stress test

Suggested C30 guard:
```text
if pf_workout_or_default_risk and liquidity_crunch:
    stage = Stage4C-Hard
    block_stage2_green = true

if construction_pf_relief_rally and no liquidity_refinancing_receivables_bridge:
    cap_stage = Stage3-Yellow
    route_to_local_4B_watch = true

if midbuilder_credit_watch and no unsold_inventory_or_pf_guarantee_improvement:
    block_stage3_green = true
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 002410 / 2023-12-08: small-cap construction relief rally can be over-promoted if refinancing and balance-sheet repair gates are not required.
- 005960 / 2023-12-01: mid-builder PF watch can look like ordinary valuation recovery, but the later path argues for Yellow/4B/counterexample treatment.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -40.83, "MAE_30D_pct": -40.83, "MAE_90D_pct": -40.83, "MFE_180D_pct": 25.69, "MFE_30D_pct": 25.69, "MFE_90D_pct": 25.69, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_009410_TAEYOUNG_20231213_PF_WORKOUT_HARD_4C", "case_role": "hard_4c_protective_success", "company_name": "태영건설", "corporate_action_window_status": "clean_forward_window_or_event_specific_trading_interruption_caveat", "current_profile_error": false, "current_profile_verdict": "Hard 4C should activate when PF liquidity, refinancing, and workout risk become company-survival issues; technical rebound after the break must not be treated as fresh Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.96, "entry_date": "2023-12-13", "entry_price": 3270, "evidence_family": "pf_workout_liquidity_crunch_balance_sheet_break", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_MIDBUILDER_LIQUIDITY_REFINANCING_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REAL_ESTATE_CREDIT", "low_date_180d": "2023-12-28", "low_price_180d": 1935, "peak_date": "2024-01-11", "peak_price": 4110, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/009/009410.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 1, "capital_allocation": 0, "eps_fcf_explosion": 0, "information_confidence": 5, "market_mispricing": 2, "total": 10, "valuation_rerating_runway": 0, "visibility_quality": 2}, "reuse_reason": null, "same_entry_group_id": "C30_009410_TAEYOUNG_20231213_PF_WORKOUT_HARD_4C", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_or_credit_spread_attention", "liquidity_or_refinancing_claim", "balance_sheet_repair_or_relief_rally_signal"], "stage3_evidence_fields": ["liquidity_runway_required", "refinancing_and_project_cash_collection_required", "unsold_inventory_or_pf_guarantee_exposure_required"], "stage4b_evidence_fields": ["pf_relief_rally_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["pf_workout_or_default_risk", "liquidity_crunch", "refinancing_failure_or_balance_sheet_break"], "symbol": "009410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv", "trigger_date": "2023-12-13", "trigger_type": "Stage4C-Hard", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.09, "MAE_30D_pct": -19.02, "MAE_90D_pct": -44.09, "MFE_180D_pct": 19.84, "MFE_30D_pct": 19.84, "MFE_90D_pct": 19.84, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_002410_BUMYANG_20231208_PF_SMALLCAP_RELIEF_RALLY_LOCAL_4B", "case_role": "pf_relief_rally_blowoff_counterexample", "company_name": "범양건영", "corporate_action_window_status": "clean_forward_window_or_event_specific_trading_interruption_caveat", "current_profile_error": true, "current_profile_verdict": "Small-cap construction/PF relief rallies should route to local 4B or Yellow unless refinancing, receivables, unsold inventory, and liquidity evidence close.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.34, "entry_date": "2023-12-08", "entry_price": 2445, "evidence_family": "smallcap_construction_pf_relief_rally_without_debt_refinancing_visibility", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_MIDBUILDER_LIQUIDITY_REFINANCING_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REAL_ESTATE_CREDIT", "low_date_180d": "2024-04-08", "low_price_180d": 1367, "peak_date": "2023-12-11", "peak_price": 2930, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/002/002410.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 1, "eps_fcf_explosion": 3, "information_confidence": 3, "market_mispricing": 4, "total": 20, "valuation_rerating_runway": 2, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C30_002410_BUMYANG_20231208_PF_SMALLCAP_RELIEF_RALLY_LOCAL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_or_credit_spread_attention", "liquidity_or_refinancing_claim", "balance_sheet_repair_or_relief_rally_signal"], "stage3_evidence_fields": ["liquidity_runway_required", "refinancing_and_project_cash_collection_required", "unsold_inventory_or_pf_guarantee_exposure_required"], "stage4b_evidence_fields": ["pf_relief_rally_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["pf_workout_or_default_risk", "liquidity_crunch", "refinancing_failure_or_balance_sheet_break"], "symbol": "002410", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002410/2023.csv", "trigger_date": "2023-12-08", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -20.1, "MAE_30D_pct": -12.69, "MAE_90D_pct": -20.1, "MFE_180D_pct": 12.03, "MFE_30D_pct": 12.03, "MFE_90D_pct": 12.03, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_005960_DONGBU_20231201_MIDBUILDER_PF_CREDIT_SPREAD_WATCH", "case_role": "midbuilder_pf_credit_watch_false_green_counterexample", "company_name": "동부건설", "corporate_action_window_status": "clean_forward_window_or_event_specific_trading_interruption_caveat", "current_profile_error": true, "current_profile_verdict": "A mid-builder PF watch row should stay Yellow unless liquidity runway, refinancing, receivables collection, and balance-sheet repair evidence are visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.68, "entry_date": "2023-12-01", "entry_price": 6070, "evidence_family": "mid_sized_builder_pf_credit_spread_watch_without_liquidity_refinancing_bridge", "evidence_url_pending": false, "fine_archetype_id": "PF_WORKOUT_MIDBUILDER_LIQUIDITY_REFINANCING_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L9_CONSTRUCTION_REAL_ESTATE_CREDIT", "low_date_180d": "2024-04-12", "low_price_180d": 4850, "peak_date": "2023-12-01", "peak_price": 6800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005960.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 3, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 25, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C30_005960_DONGBU_20231201_MIDBUILDER_PF_CREDIT_SPREAD_WATCH", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R10", "source_proxy_only": false, "stage2_evidence_fields": ["construction_pf_or_credit_spread_attention", "liquidity_or_refinancing_claim", "balance_sheet_repair_or_relief_rally_signal"], "stage3_evidence_fields": ["liquidity_runway_required", "refinancing_and_project_cash_collection_required", "unsold_inventory_or_pf_guarantee_exposure_required"], "stage4b_evidence_fields": ["pf_relief_rally_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["pf_workout_or_default_risk", "liquidity_crunch", "refinancing_failure_or_balance_sheet_break"], "symbol": "005960", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2023.csv", "trigger_date": "2023-12-01", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "PF_WORKOUT_MIDBUILDER_LIQUIDITY_REFINANCING_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L9_CONSTRUCTION_REAL_ESTATE_CREDIT",
  "loop_contribution_label": "construction_pf_workout_midbuilder_credit_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R10",
  "shadow_rule_candidate": "C30 construction/PF rows should hard-route to 4C when PF workout/liquidity/refinancing failure becomes company-survival risk; relief rallies or mid-builder credit-watch rows should cap at Yellow/local 4B unless liquidity runway, refinancing, receivables, unsold inventory, and PF guarantee exposure improve.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C30 + symbol + trigger_type + entry_date.
3. Add C30-specific PF workout/liquidity/refinancing/balance-sheet guard only as a shadow candidate until more rows exist.

Candidate rule:
- C30_PF_WORKOUT_LIQUIDITY_CRUNCH_HARD_4C
- C30_CONSTRUCTION_RELIEF_RALLY_STAGE3_CAP_LOCAL_4B
- C30_GREEN_REQUIRES_LIQUIDITY_REFINANCING_RECEIVABLES_UNSOLD_INVENTORY_BRIDGE
- C30_MIDBUILDER_CREDIT_WATCH_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R10/L9_CONSTRUCTION_REAL_ESTATE_CREDIT/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

