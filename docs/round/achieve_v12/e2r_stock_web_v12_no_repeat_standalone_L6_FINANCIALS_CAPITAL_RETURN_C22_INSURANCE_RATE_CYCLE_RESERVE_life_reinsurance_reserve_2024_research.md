# E2R V12 No-Repeat Standalone Residual Research
## R6 / L6 / C22 — Insurance rate-cycle / reserve quality guard

metadata:
```text
selected_round: R6
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L6_FINANCIALS_CAPITAL_RETURN
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_REINSURANCE_RATE_RESERVE_CAPITAL_RETURN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L6_FINANCIALS_CAPITAL_RETURN_C22_INSURANCE_RATE_CYCLE_RESERVE_life_reinsurance_reserve_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C22_INSURANCE_RATE_CYCLE_RESERVE current coverage:
rows=103, symbols=8, date range=2023-05-15~2025-05-30, good/bad S2=35/16, 4B/4C=5/1
top covered symbols: 000810(28), 005830(28), 088350(15), 001450(12), 000400(8)
```

This run avoids those top-covered C22 symbols and adds 032830, 003690, and 082640.  
Each row uses a new `C22 + symbol + trigger_type + entry_date` hard key.

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
032830 삼성생명: corporate_action_candidate_count=0.
003690 코리안리: selected entry window is clean; historical corporate-action candidates are 1997-03-29 and 2004-07-20, but a later 2024 share-count/capital-event caveat should be handled before production use.
082640 동양생명: 2024 forward window clean; corporate-action candidate is 2017-04-11 and outside selected test window.
```

## 3. Research thesis

C22 should not treat every low-PBR insurer move as C21-style capital-return beta. It has its own insurance-specific chain:

```text
rate cycle / reinsurance pricing / reserve attention
→ reserve adequacy and CSM quality
→ loss-ratio or underwriting-margin discipline
→ solvency and capital-return room
→ payout execution and revision bridge
→ rerating
```

The insurer balance sheet is a reservoir. Higher rates can raise the waterline, but Green should ask whether the dam is sound: reserves, CSM, loss ratio, solvency and payout capacity must hold together.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C22_032830_SAMSUNGLIFE_20240201_RATE_RESERVE_CSM_STAGE2 | 032830 | positive_life_insurer_rate_reserve_csm_stage2_success_with_later_4b | 2024-02-01 | 76000 | 108500 on 2024-03-08 | 68900 on 2024-02-01 | 42.76% | 42.76% | 42.76% | -9.34% | -28.76% |
| C22_003690_KOREANRE_20240201_REINSURANCE_RATE_CYCLE_STAGE2 | 003690 | positive_reinsurance_rate_cycle_stage2_success_with_capital_event_caveat | 2024-02-01 | 7810 | 9440 on 2024-10-31 | 7470 on 2024-02-01 | 7.81% | 9.48% | 20.87% | -4.35% | -17.06% |
| C22_082640_DONGLIFE_20241031_LIFE_RATE_RESERVE_PRICE_PREMIUM_4B | 082640 | life_insurer_reserve_capital_return_price_premium_counterexample | 2024-10-31 | 6110 | 6390 on 2024-11-01 | 4450 on 2024-12-20 | 4.58% | 4.58% | 4.58% | -27.17% | -30.36% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Insurance rate-cycle, reinsurance pricing, reserve/CSM visibility and solvency-capital room can be valid Stage2 routes.
- 032830 is the life-insurance anchor: the February 2024 row produced a large early MFE when reserve/CSM quality and capital-return optionality were repriced.
- 003690 adds the reinsurance route: underwriting rate cycle and reserve quality created a slower but usable rerating path.

### Stage3 / Green
- C22 Green should require reserve adequacy, CSM quality, loss-ratio or underwriting-margin discipline, solvency room, payout policy and revision confirmation.
- The guard should not let generic low-PBR/value-up logic substitute for insurance-specific evidence.

### 4B
- 082640 is the local 4B/counterexample row. The rate/reserve/capital-return price premium had limited forward upside and then drew down once solvency, payout and revision evidence did not keep expanding.
- 032830 also required later 4B discipline after the February/March rerating moved from underpriced evidence to widely capitalized premium.

### 4C
- No hard reserve adequacy break is asserted.
- The C22 break mode is insurance evidence exhaustion: rate-cycle or low-PBR attention remains plausible, but reserve, CSM, solvency, loss-ratio, payout and revision evidence no longer carries the price.

## 6. Raw component score breakdown

```json
{
  "C22_003690_KOREANRE_20240201_REINSURANCE_RATE_CYCLE_STAGE2": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 4,
    "eps_fcf_explosion": 8,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 51,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  },
  "C22_032830_SAMSUNGLIFE_20240201_RATE_RESERVE_CSM_STAGE2": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 5,
    "eps_fcf_explosion": 9,
    "information_confidence": 4,
    "market_mispricing": 12,
    "total": 57,
    "valuation_rerating_runway": 10,
    "visibility_quality": 11
  },
  "C22_082640_DONGLIFE_20241031_LIFE_RATE_RESERVE_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 3,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C22 guard:
```text
if insurance_rate_cycle_attention and reserve_CSM_capital_room_revision_bridge_visible:
    allow_stage2_actionable = true

if insurance_rate_reserve_price_premium and no incremental_reserve_CSM_solvency_payout_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and reserve_or_capital_return_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 082640 / 2024-10-31: life-insurer rate/reserve price premium can be over-promoted if the model treats price strength as solvency, payout and reserve-quality proof.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -9.34, "MAE_30D_pct": -9.34, "MAE_90D_pct": -9.34, "MFE_180D_pct": 42.76, "MFE_30D_pct": 42.76, "MFE_90D_pct": 42.76, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "case_id": "C22_032830_SAMSUNGLIFE_20240201_RATE_RESERVE_CSM_STAGE2", "case_role": "positive_life_insurer_rate_reserve_csm_stage2_success_with_later_4b", "company_name": "삼성생명", "corporate_action_window_status": "corporate_action_candidate_count=0", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when life-insurer rate-cycle, reserve/CSM visibility and capital-return optionality converged before the valuation had fully rerated. Green still requires reserve adequacy, CSM quality, new-business margin, solvency/capital room, payout execution and revision bridge; after the March 2024 premium, the same evidence needed 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -28.76, "entry_date": "2024-02-01", "entry_price": 76000, "evidence_family": "life_insurance_rate_cycle_reserve_csm_capital_return_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "LIFE_REINSURANCE_RATE_RESERVE_CAPITAL_RETURN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L6_FINANCIALS_CAPITAL_RETURN", "low_date_180d": "2024-02-01", "low_price_180d": 68900, "peak_date": "2024-03-08", "peak_price": 108500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/032/032830.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 5, "eps_fcf_explosion": 9, "information_confidence": 4, "market_mispricing": 12, "total": 57, "valuation_rerating_runway": 10, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C22_032830_SAMSUNGLIFE_20240201_RATE_RESERVE_CSM_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R6", "source_proxy_only": false, "stage2_evidence_fields": ["insurance_rate_cycle_or_reinsurance_pricing_attention", "reserve_CSM_or_loss_ratio_quality_signal", "capital_room_or_payout_revision_visibility"], "stage3_evidence_fields": ["reserve_adequacy_and_CSM_quality_required", "solvency_capital_room_and_payout_policy_required", "loss_ratio_or_underwriting_margin_revision_bridge_required"], "stage4b_evidence_fields": ["insurance_rate_reserve_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["reserve_adequacy_or_loss_ratio_break", "solvency_or_capital_return_constraint", "CSM_underwriting_margin_revision_bridge_failure"], "symbol": "032830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "trigger_date": "2024-02-01", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -4.35, "MAE_30D_pct": -4.35, "MAE_90D_pct": -4.35, "MFE_180D_pct": 20.87, "MFE_30D_pct": 7.81, "MFE_90D_pct": 9.48, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "case_id": "C22_003690_KOREANRE_20240201_REINSURANCE_RATE_CYCLE_STAGE2", "case_role": "positive_reinsurance_rate_cycle_stage2_success_with_capital_event_caveat", "company_name": "코리안리", "corporate_action_window_status": "clean selected entry window; profile corporate-action candidates are 1997/2004; later 2024 share-count change visible and should be handled as capital-event caveat for post-peak validation", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when reinsurance-rate cycle, underwriting margin and reserve-quality evidence could connect to a valuation rerating. Green still requires loss-ratio discipline, catastrophe reserve quality, premium renewal pricing, capital adequacy and revision bridge; later capital/share-count event risk requires separate 4B/validation handling.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -17.06, "entry_date": "2024-02-01", "entry_price": 7810, "evidence_family": "reinsurance_rate_cycle_reserve_quality_underwriting_margin_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "LIFE_REINSURANCE_RATE_RESERVE_CAPITAL_RETURN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L6_FINANCIALS_CAPITAL_RETURN", "low_date_180d": "2024-02-01", "low_price_180d": 7470, "peak_date": "2024-10-31", "peak_price": 9440, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003690.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 4, "eps_fcf_explosion": 8, "information_confidence": 4, "market_mispricing": 10, "total": 51, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C22_003690_KOREANRE_20240201_REINSURANCE_RATE_CYCLE_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R6", "source_proxy_only": false, "stage2_evidence_fields": ["insurance_rate_cycle_or_reinsurance_pricing_attention", "reserve_CSM_or_loss_ratio_quality_signal", "capital_room_or_payout_revision_visibility"], "stage3_evidence_fields": ["reserve_adequacy_and_CSM_quality_required", "solvency_capital_room_and_payout_policy_required", "loss_ratio_or_underwriting_margin_revision_bridge_required"], "stage4b_evidence_fields": ["insurance_rate_reserve_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["reserve_adequacy_or_loss_ratio_break", "solvency_or_capital_return_constraint", "CSM_underwriting_margin_revision_bridge_failure"], "symbol": "003690", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv", "trigger_date": "2024-02-01", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -27.17, "MAE_30D_pct": -9.98, "MAE_90D_pct": -27.17, "MFE_180D_pct": 4.58, "MFE_30D_pct": 4.58, "MFE_90D_pct": 4.58, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "case_id": "C22_082640_DONGLIFE_20241031_LIFE_RATE_RESERVE_PRICE_PREMIUM_4B", "case_role": "life_insurer_reserve_capital_return_price_premium_counterexample", "company_name": "동양생명", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2017-04-11 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Life-insurer rate/reserve price premium should route to local 4B or counterexample unless reserve adequacy, CSM quality, solvency/capital room, payout policy and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.36, "entry_date": "2024-10-31", "entry_price": 6110, "evidence_family": "life_insurance_rate_reserve_capital_return_price_premium_without_solvency_payout_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "LIFE_REINSURANCE_RATE_RESERVE_CAPITAL_RETURN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L6_FINANCIALS_CAPITAL_RETURN", "low_date_180d": "2024-12-20", "low_price_180d": 4450, "peak_date": "2024-11-01", "peak_price": 6390, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/082/082640.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 3, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C22_082640_DONGLIFE_20241031_LIFE_RATE_RESERVE_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R6", "source_proxy_only": false, "stage2_evidence_fields": ["insurance_rate_cycle_or_reinsurance_pricing_attention", "reserve_CSM_or_loss_ratio_quality_signal", "capital_room_or_payout_revision_visibility"], "stage3_evidence_fields": ["reserve_adequacy_and_CSM_quality_required", "solvency_capital_room_and_payout_policy_required", "loss_ratio_or_underwriting_margin_revision_bridge_required"], "stage4b_evidence_fields": ["insurance_rate_reserve_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["reserve_adequacy_or_loss_ratio_break", "solvency_or_capital_return_constraint", "CSM_underwriting_margin_revision_bridge_failure"], "symbol": "082640", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv", "trigger_date": "2024-10-31", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "LIFE_REINSURANCE_RATE_RESERVE_CAPITAL_RETURN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L6_FINANCIALS_CAPITAL_RETURN",
  "loop_contribution_label": "insurance_rate_cycle_reserve_life_reinsurance_new_symbols_and_4b_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R6",
  "shadow_rule_candidate": "C22 insurance rate-cycle/reserve rows should allow Stage2 when rate-cycle/reinsurance pricing, reserve or CSM quality, solvency/capital room and payout/revision evidence align, but Stage3 Green requires reserve adequacy, CSM quality, loss-ratio/underwriting margin discipline, solvency room, payout execution and revision bridge; insurer price premium without reserve-capital evidence should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C22 + symbol + trigger_type + entry_date.
3. Treat 003690's later 2024 share-count/capital-event caveat conservatively before production scoring.
4. Add C22-specific insurance rate-cycle / reserve / CSM / solvency / payout guard only as a shadow candidate until more rows exist.

Candidate rule:
- C22_STAGE2_ALLOWED_ON_RATE_RESERVE_CSM_CAPITAL_ROOM_REVISION_BRIDGE
- C22_GREEN_REQUIRES_RESERVE_ADEQUACY_CSM_LOSS_RATIO_SOLVENCY_PAYOUT_REVISION
- C22_INSURANCE_RATE_RESERVE_PRICE_PREMIUM_LOCAL_4B
- C22_INSURER_PREMIUM_WITHOUT_SOLVENCY_PAYOUT_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R6/L6_FINANCIALS_CAPITAL_RETURN/C22_INSURANCE_RATE_CYCLE_RESERVE.

