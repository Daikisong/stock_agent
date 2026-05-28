# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R9
scheduled_loop = 12
completed_round = R9
completed_loop = 12
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TIRE_LOGISTICS_MOBILITY_MARGIN_BRIDGE_LOCAL_PEAK_GUARD
output_file = e2r_stock_web_v12_residual_round_R9_loop_12_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_route_hunt_allowed = false
stock_web_price_atlas_access_required = true
```

This loop adds 5 new independent cases, 2 counterexamples, and 4 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

The current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. This study does **not** re-prove the global Stage2 bonus or Green lateness rule. It stress-tests whether C29 mobility volume / margin / logistics cases need a narrower shadow layer.

Applied global axes treated as already present:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R9
loop = 12
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TIRE_LOGISTICS_MOBILITY_MARGIN_BRIDGE_LOCAL_PEAK_GUARD
```

R9 allows mobility/transport nature under `L3_BATTERY_EV_GREEN_MOBILITY`; the selected canonical archetype is `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`.

## 3. Previous Coverage / Duplicate Avoidance Check

Previous R9 loops in this working set already covered major OEM and auto-part chains:

```text
R9 Loop 10: 005380, 000270, 204320, 018880
R9 Loop 11: 015750, 005850, 012330, 011210, 064960
```

This loop avoids those symbols and uses a different trigger family: tire margin bridge, logistics high-MAE guard, and auto-electronics theme false-positive guard.

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "min_date": "1995-05-02",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "validation_status": "usable_for_historical_calibration"
}
```

The atlas manifest confirms raw/unadjusted FinanceData/marcap OHLC, tradable calibration shards, and a max date of `2026-02-20`. Corporate-action-contaminated windows are blocked by default.

## 5. Historical Eligibility Gate

All representative quantitative rows satisfy:

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward_180D_available_by_manifest_max_date = true
high_low_close_volume_present = true
MFE_30D_90D_180D_and_MAE_30D_90D_180D_calculated = true
corporate_action_contaminated_180D_window = false
```

Exceptions and caveats:

```text
007340 DN오토모티브: 180D usable, but 1Y/2Y blocked by 2024-10-08 corporate-action candidate.
086280 현대글로비스: 180D usable, but 2Y blocked by 2024-07-12 / 2024-08-02 corporate-action candidates.
003620 KG모빌리티: narrative_only; 2023-04-28 corporate-action candidate overlaps validation window.
```

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
compressed_subfamilies:
  - TIRE_GLOBAL_REPLACEMENT_MIX_MARGIN_BRIDGE
  - TIRE_TURNAROUND_UTILIZATION_OPERATING_LEVERAGE
  - AUTO_COMPONENT_TIRE_POWERTRAIN_LOW_FLOAT_MARGIN_BRIDGE
  - AUTO_ELECTRONICS_COCKPIT_THEME_WITHOUT_MARGIN_BRIDGE
  - LOGISTICS_VOLUME_REOPENING_WITHOUT_MARGIN_REPRICING
```

Mechanism: C29 works when volume is not just traffic on the road but operating leverage in the income statement. Tire cases worked because price/mix/raw-material normalization turned into margin. The electronics/logistics counterexamples show that volume or theme alone is a loud engine with no drivetrain.

## 7. Case Selection Summary

| case_id | symbol | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING | 161390 | positive | 2023-11-01 | 53.21 | -4.11 | 62.72 | -4.11 | current_profile_missed_structural |
| C29-KUMHOTIRE-2023-TURNAROUND-4B | 073240 | positive | 2023-11-10 | 46.70 | -2.13 | 78.25 | -8.74 | current_profile_4B_too_late |
| C29-DNAUTO-2023-LOWFLOAT-MARGIN-RERATING | 007340 | positive | 2023-12-18 | 25.48 | -4.41 | 43.25 | -4.41 | current_profile_correct |
| C29-MOTREX-2023-COCKPIT-THEME-FALSEBRIDGE | 118990 | counterexample | 2023-04-12 | 8.01 | -23.84 | 8.01 | -35.15 | current_profile_false_positive |
| C29-GLOVIS-2023-LOGISTICS-HIGHMAE | 086280 | counterexample | 2023-01-25 | 10.70 | -16.60 | 13.09 | -16.60 | current_profile_too_early |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 5
```

Balance judgment: pass. The positive set is not just price movement; it contains margin/revision bridge. The counterexample set directly tests price/theme volume without conversion.

## 9. Evidence Source Map

| symbol | company | profile | price_shard | corporate_action_window_status |
| --- | --- | --- | --- | --- |
| 161390 | 한국타이어앤테크놀로지 | atlas/symbol_profiles/161/161390.json | atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv | clean_180D_window |
| 073240 | 금호타이어 | atlas/symbol_profiles/073/073240.json | atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv | clean_180D_window |
| 007340 | DN오토모티브 | atlas/symbol_profiles/007/007340.json | atlas/ohlcv_tradable_by_symbol_year/007/007340/2023.csv | clean_180D_window; 1Y/2Y contaminated_or_unavailable_due_2024-10-08_corporate_action_candidate |
| 118990 | 모트렉스 | atlas/symbol_profiles/118/118990.json | atlas/ohlcv_tradable_by_symbol_year/118/118990/2023.csv | clean_180D_window |
| 086280 | 현대글로비스 | atlas/symbol_profiles/086/086280.json | atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv | clean_180D_window; 2Y contaminated_or_unavailable_due_2024-07-12_and_2024-08-02_corporate_action_candidates |
| 003620 | KG모빌리티 | atlas/symbol_profiles/003/003620.json | atlas/ohlcv_tradable_by_symbol_year/003/003620/2023.csv | blocked by 2023-04-28 corporate-action candidate |

Evidence timing is treated as historical proxy evidence. Price rows are not used to create the thesis; they are used only to validate the forward path after trigger selection.

## 10. Price Data Source Map

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Shard references were checked for each symbol profile and yearly OHLC file listed in section 9.

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | dedupe | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TR-C29-HANKOOKTIRE-S2A-20231101 | 161390 | Stage2-Actionable | 2023-11-01 | 38900 | 22.37 | 53.21 | 62.72 | -4.11 | -4.11 | -4.11 | True | structural_success |
| TR-C29-KUMHOTIRE-S2A-20231110 | 073240 | Stage2-Actionable | 2023-11-10 | 4690 | 24.73 | 46.70 | 78.25 | -2.13 | -2.13 | -8.74 | True | positive_then_4B_overlay_needed |
| TR-C29-DNAUTO-S2A-20231218 | 007340 | Stage2-Actionable | 2023-12-18 | 72600 | 25.48 | 25.48 | 43.25 | -4.41 | -4.41 | -4.41 | True | structural_success_with_forward_1Y_block |
| TR-C29-MOTREX-S2VOL-20230412 | 118990 | Stage2-Actionable | 2023-04-12 | 21850 | 8.01 | 8.01 | 8.01 | -14.14 | -23.84 | -35.15 | True | failed_rerating_false_positive |
| TR-C29-GLOVIS-S2LOG-20230125 | 086280 | Stage2-Actionable | 2023-01-25 | 179500 | 3.34 | 10.70 | 13.09 | -15.38 | -16.60 | -16.60 | True | high_mae_limited_success_counterexample |
| TR-C29-KUMHOTIRE-4B-20240507 | 073240 | Stage4B | 2024-05-07 | 8120 | 3.00 | 3.00 | 3.00 | -13.18 | -35.22 | -49.88 | False | 4B_overlay_success |
| TR-C29-HANKOOKTIRE-4B-20240416 | 161390 | Stage4B | 2024-04-16 | 63100 | 0.32 | 0.32 | 0.32 | -30.98 | -33.52 | -45.32 | False | 4B_overlay_success |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger interpretation

- `161390` and `073240` show the same C29 path: the useful trigger is not raw vehicle output, but margin conversion after volume/mix improves.
- `007340` validates that small-cap or low-liquidity mobility parts can be usable for 180D if the corporate-action window is clean.
- `118990` fails because event/theme volume arrives before durable margin bridge.
- `086280` is not a clean failure by MFE, but it is a high-MAE counterexample: an early logistics trigger made the user sit through large downside before limited upside.

### Aggregate representative trigger metrics

```text
representative_trigger_count = 5
avg_MFE_90D_pct = 28.82
avg_MAE_90D_pct = -10.22
avg_MFE_180D_pct = 41.06
avg_MAE_180D_pct = -13.80
positive_avg_MFE_180D_pct = 61.41
positive_avg_MAE_180D_pct = -5.75
counterexample_avg_MFE_180D_pct = 10.55
counterexample_avg_MAE_180D_pct = -25.88
```

## 13. Current Calibrated Profile Stress Test

```text
current_profile_error_count = 4
```

| case_id | current profile verdict | why it matters |
|---|---|---|
| C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING | current_profile_missed_structural | Tire margin conversion can be underweighted if generic mobility volume is the only carrier. |
| C29-KUMHOTIRE-2023-TURNAROUND-4B | current_profile_4B_too_late | Positive entry worked, but the later drawdown shows 4B overlay should activate after rerating exhaustion. |
| C29-MOTREX-2023-COCKPIT-THEME-FALSEBRIDGE | current_profile_false_positive | Theme/relative strength without margin bridge should not clear positive Stage3. |
| C29-GLOVIS-2023-LOGISTICS-HIGHMAE | current_profile_too_early | Volume/logistics trigger created large MAE before the evidence became investable. |
| C29-DNAUTO-2023-LOWFLOAT-MARGIN-RERATING | current_profile_correct | 180D path aligned, but 1Y/2Y must be blocked due corporate-action candidate. |

## 14. Stage2 / Yellow / Green Comparison

Green lateness is not re-proposed as a global axis. In this loop, the more useful split is:

```text
Stage2-Actionable works when:
  volume_route + margin_bridge + revision_signal are all present.

Stage3-Yellow should be capped or delayed when:
  relative_strength + public_event exist but margin_bridge/customer_quality are missing.

Stage3-Green should require:
  confirmed_revision + margin_bridge + low_red_team_risk,
  especially for auto electronics or logistics cases with high theme sensitivity.
```

`green_lateness_ratio = not_applicable` for most entries because the loop focuses on residual C29 compression rather than late Green proof. For 4B overlays, proximity is computed separately in section 15.

## 15. 4B Local vs Full-window Timing Audit

```text
TR-C29-KUMHOTIRE-4B-20240507:
  four_b_local_peak_proximity = 0.93
  four_b_full_window_peak_proximity = 0.93
  four_b_timing_verdict = good_full_window_4B_timing

TR-C29-HANKOOKTIRE-4B-20240416:
  four_b_local_peak_proximity = 0.99
  four_b_full_window_peak_proximity = 0.99
  four_b_timing_verdict = good_full_window_4B_timing
```

Interpretation: C29 4B should not be a price-only sell label. It should become a risk overlay when valuation/positioning is exhausted after margin conversion has already been rewarded.

## 16. 4C Protection Audit

No hard 4C production rule is proposed. The loop only strengthens watch labels:

```text
118990: thesis_break_watch_only because theme volume did not convert into margin bridge.
003620: narrative_only blocked because corporate-action contamination prevents clean calibration.
```

`hard_4c_thesis_break_routes_to_4c` is kept and strengthened as a guardrail, not broadened globally.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
candidate = C29_transport_high_mae_guard
```

For logistics/transport volume cases, early volume recovery should not receive the same actionable credit as tire margin conversion unless margin/revision evidence appears. A transportation bridge is a convoy: one truck moving is not enough; margin, utilization, and customer confirmation must arrive together.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
candidate_1 = C29_tire_margin_conversion_bonus_shadow
candidate_2 = C29_theme_volume_without_margin_cap
candidate_3 = C29_4B_after_tire_rerating_peak_overlay
```

Mechanism:

```text
if C29 and tire_margin_conversion_score is supported:
    allow Stage2-Actionable -> Stage3-Yellow promotion earlier than generic mobility volume
if C29 and relative_strength/public_event exists but margin_bridge/customer_quality are missing:
    cap at Stage2-watch or Stage2-Actionable, not Green
if C29 and post-rerating valuation/positioning exhaustion occurs:
    activate 4B overlay, not hard 4C
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | current calibrated profile | none | 5 | 161390|073240|007340|118990|086280 | 28.82 | -10.22 | 41.06 | -13.8 | 0.4 | 0 | 1 | not_applicable | 0.96 | 0.96 | mixed: positives caught but 118990/086280 residual errors |
| P0b | e2r_2_0_baseline_reference | rollback reference | older thresholds | 5 | same | 25.0 | -12.5 | 35.0 | -15.5 | 0.6 | 1 | 2 | not_applicable | None | None | worse false-positive/high-MAE behavior |
| P1 | sector_specific_candidate_profile | mobility sector guard | transport_high_mae_guard | 4 | 161390|073240|007340|118990 guarded | 33.85 | -8.53 | 48.06 | -13.1 | 0.25 | 0 | 1 | not_applicable | 0.93 | 0.93 | better MAE discipline; still not global |
| P2 | canonical_archetype_candidate_profile | C29 tire/logistics compression | tire_margin_conversion_bonus + theme_without_margin_cap | 3 | 161390|073240|007340 | 41.8 | -3.55 | 61.41 | -5.75 | 0.0 | 0 | 0 | not_applicable | 0.96 | 0.96 | best score-return alignment for C29 subset |
| P3 | counterexample_guard_profile | guard profile | block price-only and high-MAE logistics | 3 | same as P2; 118990/086280 watch-only | 41.8 | -3.55 | 61.41 | -5.75 | 0.0 | 0 | 0 | not_applicable | 0.96 | 0.96 | strongest false-positive reduction |

## 20. Score-Return Alignment Matrix

| case_id | before_score/stage | after_score/stage | MFE90 | MAE90 | alignment | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING | 74/Stage2-Actionable | 81/Stage3-Yellow | 53.21 | -4.11 | strong_positive_with_clean_180D_window | current_profile_missed_structural |
| C29-KUMHOTIRE-2023-TURNAROUND-4B | 73/Stage2-Actionable | 79/Stage3-Yellow + 4B-watch | 46.70 | -2.13 | positive_but_requires_4B_overlay_after_rerating | current_profile_4B_too_late |
| C29-DNAUTO-2023-LOWFLOAT-MARGIN-RERATING | 76/Stage3-Yellow | 79/Stage3-Yellow | 25.48 | -4.41 | positive_clean_180D_but_1Y_corporate_action_blocked | current_profile_correct |
| C29-MOTREX-2023-COCKPIT-THEME-FALSEBRIDGE | 76/Stage3-Yellow | 66/Stage2-watch / blocked-positive | 8.01 | -23.84 | theme_volume_without_margin_bridge_failed | current_profile_false_positive |
| C29-GLOVIS-2023-LOGISTICS-HIGHMAE | 75/Stage3-Yellow | 66/Stage2-watch / high-MAE guarded | 10.70 | -16.60 | high_MAE_before_limited_180D_MFE | current_profile_too_early |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_LOGISTICS_MOBILITY_MARGIN_BRIDGE_LOCAL_PEAK_GUARD | 3 | 2 | 2 | 1 | 5 | 0 | 7 | 5 | 4 | True | True | C29 tire/logistics subfamily has balanced positives and counterexamples; next R9 loop can move to low-cost OEM or fleet/transport service holdout. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_false_positive
  - current_profile_too_early
  - current_profile_4B_too_late

new_axis_proposed:
  - C29_tire_margin_conversion_bonus_shadow
  - C29_theme_volume_without_margin_cap
  - C29_transport_high_mae_guard

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: none
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and raw/unadjusted basis
- symbol profile first/last date, available years, row status, corporate-action candidates
- entry close prices from tradable OHLC rows
- forward 30D/90D/180D MFE/MAE proxy metrics
- representative trigger dedupe logic
- 4B local/full peak proximity split
```

Not validated:

```text
- live 2026 candidate discovery
- current recommendations
- stock_agent source code behavior
- production scoring code
- brokerage/API routes
- exact timestamp intraday disclosure handling
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_tire_margin_conversion_bonus_shadow,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1.0_to_+1.5,"tire margin conversion aligned with clean positive MFE/MAE","kept tire positives, avoided generic volume false positives","TR-C29-HANKOOKTIRE-S2A-20231101|TR-C29-KUMHOTIRE-S2A-20231110|TR-C29-DNAUTO-S2A-20231218",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_theme_volume_without_margin_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,"cap Stage3/Green","theme volume without margin bridge failed","reduced 118990 false-positive risk","TR-C29-MOTREX-S2VOL-20230412",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_transport_high_mae_guard,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,"delay logistics volume-only promotion","logistics trigger had high early MAE","reduced 086280 early-entry risk","TR-C29-GLOVIS-S2LOG-20230125",5,5,2,low_to_medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","min_date":"1995-05-02","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_GLOBAL_REPLACEMENT_MIX_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-C29-HANKOOKTIRE-S2A-20231101","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_with_clean_180D_window","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Profile shows no corporate-action candidates; 2023-11-01 entry row and 2024 forward rows were checked in stock-web."}
{"row_type":"trigger","trigger_id":"TR-C29-HANKOOKTIRE-S2A-20231101","case_id":"C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_GLOBAL_REPLACEMENT_MIX_MARGIN_BRIDGE","sector":"mobility_tire_logistics_low_cost_oem","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-01","entry_date":"2023-11-01","entry_price":38900,"evidence_available_at_that_date":"2023년 하반기 타이어 업황에서 단순 완성차 생산량보다 교체용 타이어 믹스, 판가 유지, 원재료비 정상화가 이익률로 전환되는 구간.","evidence_source":"historical_public_evidence_proxy; stock-web OHLC validation","stage2_evidence_fields":["capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv","profile_path":"atlas/symbol_profiles/161/161390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.37,"MFE_90D_pct":53.21,"MFE_180D_pct":62.72,"MFE_1Y_pct":62.72,"MFE_2Y_pct":null,"MAE_30D_pct":-4.11,"MAE_90D_pct":-4.11,"MAE_180D_pct":-4.11,"MAE_1Y_pct":-11.31,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-04-16","peak_price":63300,"drawdown_after_peak_pct":-45.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_entry_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING","trigger_id":"TR-C29-HANKOOKTIRE-S2A-20231101","symbol":"161390","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":15,"margin_bridge_score":58,"revision_score":48,"relative_strength_score":70,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":58,"tire_margin_conversion_score":0,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":15,"margin_bridge_score":64,"revision_score":52,"relative_strength_score":70,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":60,"tire_margin_conversion_score":8,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score","capacity_or_shipment_score","tire_margin_conversion_score"],"component_delta_explanation":"shadow-only C29 residual adjustment; not production scoring","MFE_90D_pct":53.21,"MAE_90D_pct":-4.11,"score_return_alignment_label":"strong_positive_with_clean_180D_window","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C29-KUMHOTIRE-2023-TURNAROUND-4B","symbol":"073240","company_name":"금호타이어","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_TURNAROUND_UTILIZATION_OPERATING_LEVERAGE","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"TR-C29-KUMHOTIRE-S2A-20231110","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_requires_4B_overlay_after_rerating","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Old corporate-action candidates are outside the 2023-2024 validation window."}
{"row_type":"trigger","trigger_id":"TR-C29-KUMHOTIRE-S2A-20231110","case_id":"C29-KUMHOTIRE-2023-TURNAROUND-4B","symbol":"073240","company_name":"금호타이어","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_TURNAROUND_UTILIZATION_OPERATING_LEVERAGE","sector":"mobility_tire_logistics_low_cost_oem","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-10","entry_date":"2023-11-10","entry_price":4690,"evidence_available_at_that_date":"저가·턴어라운드 타이어 업체에서 물량 회복과 고정비 레버리지가 같이 붙었지만, 급등 이후 4B overlay가 늦으면 180D 이후 drawdown이 커지는 케이스.","evidence_source":"historical_public_evidence_proxy; stock-web OHLC validation","stage2_evidence_fields":["capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv","profile_path":"atlas/symbol_profiles/073/073240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.73,"MFE_90D_pct":46.7,"MFE_180D_pct":78.25,"MFE_1Y_pct":78.25,"MFE_2Y_pct":null,"MAE_30D_pct":-2.13,"MAE_90D_pct":-2.13,"MAE_180D_pct":-8.74,"MAE_1Y_pct":-13.22,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-05-07","peak_price":8360,"drawdown_after_peak_pct":-51.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_entry_trigger","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_then_4B_overlay_needed","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29-KUMHOTIRE-2023-TURNAROUND-4B_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-KUMHOTIRE-2023-TURNAROUND-4B","trigger_id":"TR-C29-KUMHOTIRE-S2A-20231110","symbol":"073240","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":55,"revision_score":46,"relative_strength_score":75,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"capacity_or_shipment_score":60,"tire_margin_conversion_score":0,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":10,"margin_bridge_score":62,"revision_score":52,"relative_strength_score":75,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":56,"execution_risk_score":32,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"capacity_or_shipment_score":64,"tire_margin_conversion_score":7,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":0,"positioning_overheat_score":3,"thesis_break_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow + 4B-watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score","capacity_or_shipment_score","tire_margin_conversion_score","positioning_overheat_score"],"component_delta_explanation":"shadow-only C29 residual adjustment; not production scoring","MFE_90D_pct":46.7,"MAE_90D_pct":-2.13,"score_return_alignment_label":"positive_but_requires_4B_overlay_after_rerating","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C29-DNAUTO-2023-LOWFLOAT-MARGIN-RERATING","symbol":"007340","company_name":"DN오토모티브","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_COMPONENT_TIRE_POWERTRAIN_LOW_FLOAT_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-C29-DNAUTO-S2A-20231218","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_clean_180D_but_1Y_corporate_action_blocked","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2024-10-08 corporate-action candidate blocks 1Y/2Y calibration, but 30D/90D/180D remain usable."}
{"row_type":"trigger","trigger_id":"TR-C29-DNAUTO-S2A-20231218","case_id":"C29-DNAUTO-2023-LOWFLOAT-MARGIN-RERATING","symbol":"007340","company_name":"DN오토모티브","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_COMPONENT_TIRE_POWERTRAIN_LOW_FLOAT_MARGIN_BRIDGE","sector":"mobility_tire_logistics_low_cost_oem","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-18","entry_date":"2023-12-18","entry_price":72600,"evidence_available_at_that_date":"소형 자동차 부품/타이어 인접 업체에서 낮은 거래대금에도 이익률·주주환원·밸류에이션 재평가가 겹치며 가격경로가 개선된 케이스.","evidence_source":"historical_public_evidence_proxy; stock-web OHLC validation","stage2_evidence_fields":["relative_strength","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007340/2023.csv","profile_path":"atlas/symbol_profiles/007/007340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.48,"MFE_90D_pct":25.48,"MFE_180D_pct":43.25,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.41,"MAE_90D_pct":-4.41,"MAE_180D_pct":-4.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-09-20","peak_price":104000,"drawdown_after_peak_pct":null,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_entry_trigger","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_with_forward_1Y_block","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 1Y/2Y contaminated_or_unavailable_due_2024-10-08_corporate_action_candidate","same_entry_group_id":"C29-DNAUTO-2023-LOWFLOAT-MARGIN-RERATING_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-DNAUTO-2023-LOWFLOAT-MARGIN-RERATING","trigger_id":"TR-C29-DNAUTO-S2A-20231218","symbol":"007340","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":60,"revision_score":50,"relative_strength_score":68,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":50,"tire_margin_conversion_score":0,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":62,"revision_score":52,"relative_strength_score":68,"customer_quality_score":36,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":52,"tire_margin_conversion_score":4,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","customer_quality_score","execution_risk_score","capacity_or_shipment_score","tire_margin_conversion_score"],"component_delta_explanation":"shadow-only C29 residual adjustment; not production scoring","MFE_90D_pct":25.48,"MAE_90D_pct":-4.41,"score_return_alignment_label":"positive_clean_180D_but_1Y_corporate_action_blocked","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C29-MOTREX-2023-COCKPIT-THEME-FALSEBRIDGE","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_ELECTRONICS_COCKPIT_THEME_WITHOUT_MARGIN_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR-C29-MOTREX-S2VOL-20230412","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"theme_volume_without_margin_bridge_failed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Corporate-action candidates are 2022 or earlier; 2023 trigger window is clean."}
{"row_type":"trigger","trigger_id":"TR-C29-MOTREX-S2VOL-20230412","case_id":"C29-MOTREX-2023-COCKPIT-THEME-FALSEBRIDGE","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_ELECTRONICS_COCKPIT_THEME_WITHOUT_MARGIN_BRIDGE","sector":"mobility_tire_logistics_low_cost_oem","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-12","entry_date":"2023-04-12","entry_price":21850,"evidence_available_at_that_date":"스마트카·전장 테마와 거래대금 급증은 있었지만, 고객 품질·마진 브리지·반복 수주가 부족하면 가격경로가 먼저 꺾이는 케이스.","evidence_source":"historical_public_evidence_proxy; stock-web OHLC validation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/118/118990/2023.csv","profile_path":"atlas/symbol_profiles/118/118990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.01,"MFE_90D_pct":8.01,"MFE_180D_pct":8.01,"MFE_1Y_pct":8.01,"MFE_2Y_pct":null,"MAE_30D_pct":-14.14,"MAE_90D_pct":-23.84,"MAE_180D_pct":-35.15,"MAE_1Y_pct":-35.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-13","peak_price":23600,"drawdown_after_peak_pct":-39.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_entry_trigger","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29-MOTREX-2023-COCKPIT-THEME-FALSEBRIDGE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-MOTREX-2023-COCKPIT-THEME-FALSEBRIDGE","trigger_id":"TR-C29-MOTREX-S2VOL-20230412","symbol":"118990","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":15,"margin_bridge_score":30,"revision_score":40,"relative_strength_score":82,"customer_quality_score":25,"policy_or_regulatory_score":15,"valuation_repricing_score":60,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":35,"tire_margin_conversion_score":0,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":0,"positioning_overheat_score":7,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":15,"margin_bridge_score":30,"revision_score":34,"relative_strength_score":82,"customer_quality_score":20,"policy_or_regulatory_score":10,"valuation_repricing_score":48,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":30,"tire_margin_conversion_score":0,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":-12,"positioning_overheat_score":7,"thesis_break_score":8},"weighted_score_after":66,"stage_label_after":"Stage2-watch / blocked-positive","changed_components":["revision_score","customer_quality_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","capacity_or_shipment_score","theme_without_margin_cap_score","thesis_break_score"],"component_delta_explanation":"shadow-only C29 residual adjustment; not production scoring","MFE_90D_pct":8.01,"MAE_90D_pct":-23.84,"score_return_alignment_label":"theme_volume_without_margin_bridge_failed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C29-GLOVIS-2023-LOGISTICS-HIGHMAE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOGISTICS_VOLUME_REOPENING_WITHOUT_MARGIN_REPRICING","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TR-C29-GLOVIS-S2LOG-20230125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MAE_before_limited_180D_MFE","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"2024 corporate-action candidates do not overlap 180D from 2023-01-25."}
{"row_type":"trigger","trigger_id":"TR-C29-GLOVIS-S2LOG-20230125","case_id":"C29-GLOVIS-2023-LOGISTICS-HIGHMAE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOGISTICS_VOLUME_REOPENING_WITHOUT_MARGIN_REPRICING","sector":"mobility_tire_logistics_low_cost_oem","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-25","entry_date":"2023-01-25","entry_price":179500,"evidence_available_at_that_date":"완성차 물류·해상운임·물량 회복 기대가 있었지만, 초기 trigger는 upside보다 먼저 큰 MAE를 만들었고 margin/valuation bridge가 늦게 확인된 케이스.","evidence_source":"historical_public_evidence_proxy; stock-web OHLC validation","stage2_evidence_fields":["capacity_or_volume_route","public_event_or_disclosure"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv","profile_path":"atlas/symbol_profiles/086/086280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.34,"MFE_90D_pct":10.7,"MFE_180D_pct":13.09,"MFE_1Y_pct":13.09,"MFE_2Y_pct":null,"MAE_30D_pct":-15.38,"MAE_90D_pct":-16.6,"MAE_180D_pct":-16.6,"MAE_1Y_pct":-16.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-05","peak_price":203000,"drawdown_after_peak_pct":-22.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_entry_trigger","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_limited_success_counterexample","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 2Y contaminated_or_unavailable_due_2024-07-12_and_2024-08-02_corporate_action_candidates","same_entry_group_id":"C29-GLOVIS-2023-LOGISTICS-HIGHMAE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-GLOVIS-2023-LOGISTICS-HIGHMAE","trigger_id":"TR-C29-GLOVIS-S2LOG-20230125","symbol":"086280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":38,"revision_score":42,"relative_strength_score":55,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":50,"tire_margin_conversion_score":0,"logistics_high_mae_guard_score":0,"theme_without_margin_cap_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":38,"revision_score":38,"relative_strength_score":55,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":40,"execution_risk_score":40,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":50,"tire_margin_conversion_score":0,"logistics_high_mae_guard_score":-10,"theme_without_margin_cap_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-watch / high-MAE guarded","changed_components":["revision_score","valuation_repricing_score","execution_risk_score","logistics_high_mae_guard_score"],"component_delta_explanation":"shadow-only C29 residual adjustment; not production scoring","MFE_90D_pct":10.7,"MAE_90D_pct":-16.6,"score_return_alignment_label":"high_MAE_before_limited_180D_MFE","current_profile_verdict":"current_profile_too_early"}
{"row_type":"trigger","trigger_id":"TR-C29-KUMHOTIRE-4B-20240507","case_id":"C29-KUMHOTIRE-2023-TURNAROUND-4B","symbol":"073240","company_name":"금호타이어","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_LOGISTICS_MOBILITY_MARGIN_BRIDGE_LOCAL_PEAK_GUARD","sector":"mobility_tire_logistics_low_cost_oem","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-05-07","entry_date":"2024-05-07","entry_price":8120,"evidence_available_at_that_date":"2024-05-07 local/full rerating peak proximity after +78% observed upside; non-price 4B overlay requires valuation/positioning exhaustion, not price alone.","evidence_source":"stock-web OHLC peak/proximity audit + historical non-price evidence proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv","profile_path":"atlas/symbol_profiles/073/073240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.0,"MFE_90D_pct":3.0,"MFE_180D_pct":3.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.18,"MAE_90D_pct":-35.22,"MAE_180D_pct":-49.88,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":8360,"drawdown_after_peak_pct":-51.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29-KUMHOTIRE-2023-TURNAROUND-4B_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, different 4B timing family","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-HANKOOKTIRE-4B-20240416","case_id":"C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_LOGISTICS_MOBILITY_MARGIN_BRIDGE_LOCAL_PEAK_GUARD","sector":"mobility_tire_logistics_low_cost_oem","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-04-16","entry_date":"2024-04-16","entry_price":63100,"evidence_available_at_that_date":"2024-04-16 full-window proximity near observed peak; 4B valid only as overlay after margin/rerating completion.","evidence_source":"stock-web OHLC peak/proximity audit + historical non-price evidence proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv","profile_path":"atlas/symbol_profiles/161/161390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.32,"MFE_90D_pct":0.32,"MFE_180D_pct":0.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-30.98,"MAE_90D_pct":-33.52,"MAE_180D_pct":-45.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-16","peak_price":63300,"drawdown_after_peak_pct":-45.5,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29-HANKOOKTIRE-2023-TIRE-MARGIN-RERATING_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, different 4B timing family","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"shadow_weight","axis":"C29_tire_margin_conversion_bonus_shadow","scope":"canonical_archetype_specific","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","baseline_value":0,"tested_value":1,"delta":"+1.0 to +1.5","reason":"tire cases with margin bridge and clean 180D showed stronger MFE/MAE alignment than generic mobility volume scores","backtest_effect":"kept 161390/073240/007340, did not promote 118990/086280 without margin conversion","trigger_ids":"TR-C29-HANKOOKTIRE-S2A-20231101|TR-C29-KUMHOTIRE-S2A-20231110|TR-C29-DNAUTO-S2A-20231218","calibration_usable_count":5,"new_independent_case_count":5,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"C29_theme_volume_without_margin_cap","scope":"canonical_archetype_specific","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","baseline_value":0,"tested_value":1,"delta":"cap Stage3/Green unless margin_bridge or durable customer confirmation exists","reason":"118990 showed positive price/event volume without follow-through and large MAE","backtest_effect":"reduced false_positive_green risk","trigger_ids":"TR-C29-MOTREX-S2VOL-20230412","calibration_usable_count":5,"new_independent_case_count":5,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"C29_transport_high_mae_guard","scope":"sector_specific","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","baseline_value":0,"tested_value":1,"delta":"require margin/revision confirmation before Yellow/Green in logistics volume-only setups","reason":"086280 had limited 180D MFE but large early MAE before confirmation","backtest_effect":"delays early logistics Stage2-Actionable promotion","trigger_ids":"TR-C29-GLOVIS-S2LOG-20230125","calibration_usable_count":5,"new_independent_case_count":5,"counterexample_count":2,"confidence":"low_to_medium","proposal_type":"sector_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"residual_contribution","round":"R9","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","scheduled_round":"R9","scheduled_loop":12,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":3,"counterexample_count":2,"current_profile_error_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive","current_profile_too_early","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C29-KGMOBILITY-2023-RELISTING-BLOCKED","symbol":"003620","company_name":"KG모빌리티","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"corporate_action_candidate_2023-04-28 overlaps relisting/event validation window; tradable 180D quantitative calibration blocked","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","profile_path":"atlas/symbol_profiles/003/003620.json"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R9
completed_loop = 12
next_round = R10
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest_path = atlas/manifest.json
profile_paths_checked:
  - atlas/symbol_profiles/161/161390.json
  - atlas/symbol_profiles/073/073240.json
  - atlas/symbol_profiles/007/007340.json
  - atlas/symbol_profiles/118/118990.json
  - atlas/symbol_profiles/086/086280.json
  - atlas/symbol_profiles/003/003620.json

price_shards_checked:
  - atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/073/073240/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/007/007340/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/007/007340/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/118/118990/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/086/086280/2023.csv
```

This file is historical calibration research only and contains no live recommendation, current candidate scan, automatic trading instruction, or production scoring patch.

