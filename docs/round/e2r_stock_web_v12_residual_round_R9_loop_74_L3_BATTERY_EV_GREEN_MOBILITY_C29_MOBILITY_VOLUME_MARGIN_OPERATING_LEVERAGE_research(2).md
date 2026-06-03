# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R9
scheduled_loop: 74
completed_round: R9
completed_loop: 74
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION
output_file: e2r_stock_web_v12_residual_round_R9_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
price_route_hunt_allowed: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

The current default profile proxy is `e2r_2_1_stock_web_calibrated_proxy`, with `e2r_2_0_baseline_reference` retained only as rollback/reference comparison.

Already-applied global axes are not re-proposed here: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`.

## 2. Round / Large Sector / Canonical Archetype Scope

- `scheduled_round`: R9
- `scheduled_loop`: 74
- `large_sector_id`: L3_BATTERY_EV_GREEN_MOBILITY
- `canonical_archetype_id`: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
- `fine_archetype_id`: AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION
- `loop_objective`: `sector_specific_rule_discovery`, `canonical_archetype_compression`, `counterexample_mining`, `coverage_gap_fill`, `4B_non_price_requirement_stress_test`

R9 permits L3 battery/EV/green mobility and mobility/transport-adjacent studies. This MD therefore uses complete-vehicle exporter positives and EV-supplier margin-conversion counterexamples inside the same canonical C29 map.

## 3. Previous Coverage / Duplicate Avoidance Check

Previous local chat state ended R8 / Loop 74 and declared `next_round=R9`, `next_loop=74`. The GitHub calibration registry was checked only as an allowed research artifact for duplicate avoidance and contained older historical calibration round entries, not the just-produced local R8 v12 MD. Therefore schedule resolution follows the previous local output state.

No case below repeats the just-produced R8/C27 content-IP set. Within R9/C29, the selected case set uses four symbols not used in the immediately prior MD and uses four distinct trigger families:

1. Hyundai Motor: full-year/Q4 record margin and export-mix rerating.
2. Kia: record profit, mix and capital-return rerating.
3. Hanon Systems: EV thermal narrative without confirmed margin conversion.
4. HL Mando: EV chassis/autonomous exposure without durable margin/FCF confirmation.

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest was checked before case construction.

| field | value |
|---|---:|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The schema uses tradable shard columns `d,o,h,l,c,v,a,mc,s,m`. The raw shard additionally has `rs`. The calibration basis for all quantitative rows here is `tradable_raw`; raw shards are not used for weight calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward_180D_available | 180D corporate-action window | calibration_usable | reason |
|---|---:|---:|---:|---|---:|---|
| C29_HMC_2023_Q4_EXPORT_MARGIN | 005380 | 2023-01-26 | true | clean | true | post-1999 corporate-action candidates not in window |
| C29_KIA_2023_RECORD_MARGIN | 000270 | 2023-01-26 | true | clean | true | post-1999 corporate-action candidates not in window |
| C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE | 018880 | 2021-01-08 | true | clean | true | no 2021 corporate-action candidate in window |
| C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP | 204320 | 2023-03-03 | true | clean | true | only 2018 candidate, outside window |

## 6. Canonical Archetype Compression Map

C29 is treated as a canonical mobility operating-leverage bucket with two sub-routes:

- **Complete-vehicle positive route**: vehicle volume, export mix, FX, SUV/hybrid/EV mix, and capital-return visibility combine into confirmed margin expansion.
- **Supplier false-positive route**: EV exposure and customer-name optionality exist, but component-level pricing, raw-material pass-through, customer concentration, and FCF conversion fail to confirm.

The compression result is that C29 should not reward “EV exposure” alone. It should reward volume/mix evidence only after a margin bridge becomes visible, and should penalize supplier cases that lack pricing power or verified FCF conversion.

## 7. Case Selection Summary

| case_id | symbol | company_name | role | primary trigger | entry_date | current_profile_verdict | calibration_usable |
|---|---:|---|---|---|---:|---|---:|
| C29_HMC_2023_Q4_EXPORT_MARGIN | 005380 | 현대차 | structural_success | Stage2-Actionable | 2023-01-26 | current_profile_correct | true |
| C29_KIA_2023_RECORD_MARGIN | 000270 | 기아 | structural_success | Stage2-Actionable | 2023-01-26 | current_profile_correct | true |
| C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE | 018880 | 한온시스템 | false_positive_green | Stage2-Actionable | 2021-01-08 | current_profile_false_positive | true |
| C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP | 204320 | HL만도 | failed_rerating | Stage2-Actionable | 2023-03-03 | current_profile_false_positive | true |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive structural success | 2 | 현대차, 기아 |
| counterexample / failed rerating | 2 | 한온시스템, HL만도 |
| 4B overlay rows | 2 | 현대차 2023-05-10, 기아 2023-05-11 |
| 4C rows | 0 | no hard thesis-break row used for quantitative scoring |

This balance supports a canonical-archetype-specific guard rather than a global promotion. The positive path exists, but only when margin bridge and vehicle mix are visible. EV supplier exposure alone repeatedly creates false positives.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence source type | Stage2 fields | Stage3 fields | 4B / 4C fields |
|---|---|---|---|---|---|
| C29_HMC_2023_Q4_EXPORT_MARGIN | 2023-01-26 earnings day | company earnings / market news / public financial result | public_event_or_disclosure, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, multiple_public_sources | 4B overlay later: price_only_local_peak |
| C29_KIA_2023_RECORD_MARGIN | 2023-01-26 earnings day | company earnings / market news / public financial result | public_event_or_disclosure, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, repeat_order_or_conversion | 4B overlay later: price_only_local_peak |
| C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE | 2021-01-08 EV thermal-management theme surge | market theme / customer optionality narrative | customer_or_order_quality, policy_or_regulatory_optionality, relative_strength | none confirmed at trigger date | execution_risk, margin_or_backlog_slowdown |
| C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP | 2023-03-03 EV/autonomous supplier rerating attempt | market theme / customer optionality narrative | customer_or_order_quality, policy_or_regulatory_optionality, relative_strength | none confirmed at trigger date | execution_risk, margin_or_backlog_slowdown |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | profile summary |
|---:|---|---|---|---|
| 005380 | 현대차 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv; 2024.csv | atlas/symbol_profiles/005/005380.json | first_date=1995-05-02; last_date=2026-02-20; tradable rows=7765; corporate_action_candidate_dates are historical 1998-1999 only |
| 000270 | 기아 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv; 2024.csv | atlas/symbol_profiles/000/000270.json | first_date=1995-05-02; last_date=2026-02-20; tradable rows=7743; corporate_action_candidate_dates are historical 1999 only |
| 018880 | 한온시스템 | atlas/ohlcv_tradable_by_symbol_year/018/018880/2021.csv | atlas/symbol_profiles/018/018880.json | first_date=1997-01-03; last_date=2026-02-20; tradable rows=7255; 2021 window clean |
| 204320 | HL만도 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv | atlas/symbol_profiles/204/204320.json | first_date=2014-10-06; last_date=2026-02-20; tradable rows=2790; 2023 window clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary | same_entry_group_id | aggregate role |
|---|---|---|---:|---:|---:|---|---|---|
| TR_C29_HMC_STAGE2_20230126 | C29_HMC_2023_Q4_EXPORT_MARGIN | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 174900 | record margin / export mix / earnings visibility | GRP_C29_HMC_20230126 | representative |
| TR_C29_HMC_4B_LOCAL_20230510 | C29_HMC_2023_Q4_EXPORT_MARGIN | Stage4B-Overlay | 2023-05-10 | 2023-05-10 | 210000 | price-only local peak after rerating | GRP_C29_HMC_20230510_4B | 4B_overlay_only |
| TR_C29_KIA_STAGE2_20230126 | C29_KIA_2023_RECORD_MARGIN | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 69300 | record profit / mix / capital-return visibility | GRP_C29_KIA_20230126 | representative |
| TR_C29_KIA_4B_LOCAL_20230511 | C29_KIA_2023_RECORD_MARGIN | Stage4B-Overlay | 2023-05-11 | 2023-05-11 | 90100 | price-only local peak after rerating | GRP_C29_KIA_20230511_4B | 4B_overlay_only |
| TR_C29_HANON_STAGE2_20210108 | C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE | Stage2-Actionable | 2021-01-08 | 2021-01-08 | 18450 | EV thermal-management theme without margin bridge | GRP_C29_HANON_20210108 | representative |
| TR_C29_HL_MANDO_STAGE2_20230303 | C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP | Stage2-Actionable | 2023-03-03 | 2023-03-03 | 51400 | EV/autonomous component exposure without durable conversion | GRP_C29_HL_MANDO_20230303 | representative |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger rows

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TR_C29_HMC_STAGE2_20230126 | 174900 | 3.14 | -4.52 | 20.93 | -4.52 | 20.93 | -4.52 | 49.23 | 70.95 | 2024-02-13 | 261000 | -17.43 | structural_success |
| TR_C29_KIA_STAGE2_20230126 | 69300 | 15.01 | -3.61 | 32.61 | -3.61 | 32.61 | -3.61 | 75.90 | 90.04 | 2024-03-11 | 131700 | -22.70 | structural_success |
| TR_C29_HANON_STAGE2_20210108 | 18450 | 9.49 | -17.62 | 9.49 | -17.62 | 9.49 | -20.33 | 9.49 | 9.49 | 2021-01-08 | 20200 | -36.39 | false_positive_green |
| TR_C29_HL_MANDO_STAGE2_20230303 | 51400 | 1.36 | -14.40 | 6.03 | -14.40 | 6.03 | -22.28 | 6.03 | 16.34 | 2023-06-30 | 54500 | -26.70 | failed_rerating |

### Local 4B overlay rows

| trigger_id | entry_price | stage2_entry_price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| TR_C29_HMC_4B_LOCAL_20230510 | 210000 | 174900 | 211500 | 261000 | 0.96 | 0.41 | price_only_local_4B_too_early |
| TR_C29_KIA_4B_LOCAL_20230511 | 90100 | 69300 | 91900 | 131700 | 0.92 | 0.33 | price_only_local_4B_too_early |

## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated profile likely decision | backtest alignment | verdict | residual interpretation |
|---|---|---|---|---|
| C29_HMC_2023_Q4_EXPORT_MARGIN | Stage2-Actionable, then Yellow/Green only after margin confirmation | aligned: positive MFE and low MAE | current_profile_correct | current global profile works when margin bridge is explicit |
| C29_KIA_2023_RECORD_MARGIN | Stage2-Actionable, then Yellow/Green after record margin/capital-return confirmation | aligned: strong MFE with modest early MAE | current_profile_correct | current profile works for complete-vehicle operating leverage |
| C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE | could over-score if EV customer optionality and RS are treated as Stage2 evidence | not aligned: large MAE and no durable upside | current_profile_false_positive | supplier exposure needs margin/FCF guard |
| C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP | could over-score if EV/autonomous exposure is promoted before margin conversion | not aligned: 90D upside small, MAE large | current_profile_false_positive | supplier route needs conversion and customer concentration guard |

Answers to the stress-test questions:

1. Current profile is directionally correct for Hyundai/Kia but too permissive for supplier EV theme cases.
2. Actual MFE/MAE confirms the distinction: complete-vehicle positives had acceptable MAE; suppliers had poor MFE/MAE symmetry.
3. Stage2 actionable bonus is not globally wrong, but C29 supplier cases need conditional gating.
4. Yellow threshold 75 is appropriate for complete-vehicle cases; insufficient for supplier cases if component margin is not explicitly tested.
5. Green threshold 87/revision 55 should remain strict for suppliers.
6. Price-only blowoff guard is strengthened by Hyundai/Kia local 4B overlays.
7. Full 4B non-price requirement is strengthened: local peaks were too early without thesis deterioration.
8. Hard 4C routing is not changed in this loop; no hard thesis-break row is used.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Yellow/Green proxy entry | peak used | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| C29_HMC_2023_Q4_EXPORT_MARGIN | 174900 | 201000 | 261000 | 0.30 | Green not fatally late; Stage2 captured early enough |
| C29_KIA_2023_RECORD_MARGIN | 69300 | 85700 | 131700 | 0.26 | Green not fatally late; Stage2 still useful |
| C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE | 18450 | n/a | 20200 | n/a | no confirmed Green trigger |
| C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP | 51400 | n/a | 54500 | n/a | no confirmed Green trigger |

The result does not re-prove “Stage2 is earlier than Green.” The residual point is narrower: in C29, Stage2 works when operating leverage is visible at the issuer level; it fails when Stage2 is only thematic EV exposure.

## 15. 4B Local vs Full-window Timing Audit

The Hyundai/Kia 2023 local peaks looked tempting as price-only 4B exits, but both were too early against the full observed rerating path. This strengthens the existing axis `full_4b_requires_non_price_evidence`.

| trigger_id | local proximity | full-window proximity | evidence type | timing verdict | action |
|---|---:|---:|---|---|---|
| TR_C29_HMC_4B_LOCAL_20230510 | 0.96 | 0.41 | price_only | price_only_local_4B_too_early | do_not_treat_as_full_4B |
| TR_C29_KIA_4B_LOCAL_20230511 | 0.92 | 0.33 | price_only | price_only_local_4B_too_early | do_not_treat_as_full_4B |

## 16. 4C Protection Audit

No hard 4C quantitative row is promoted here. Hanon and HL Mando are treated as supplier false positives / failed reratings rather than hard thesis-break 4C events. Their use is to calibrate Stage2/Green gating, not hard 4C crash protection.

| case_id | 4C label | reason |
|---|---|---|
| C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE | thesis_break_watch_only | margin bridge failed to confirm, but no discrete cancellation/rejection row used |
| C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP | thesis_break_watch_only | customer optionality did not convert into durable margin/FCF evidence |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = mobility_supplier_operating_leverage_conversion_guard
candidate_delta = -1.0 to -1.5 score-equivalent for supplier Stage2 promotion when margin bridge is absent
```

Rule candidate:

For L3 mobility supplier cases, do not let EV exposure, customer-name optionality, or relative strength alone reach Stage2-Actionable if the case lacks at least one of: confirmed margin bridge, contract pricing/pass-through visibility, FCF conversion, or multi-customer delivery visibility.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
axis_1 = complete_vehicle_volume_mix_margin_bonus
axis_2 = supplier_conversion_guard
```

C29 positive promotion should be stronger for complete-vehicle names when volume/mix/margin are simultaneously visible. C29 supplier promotion should be weaker unless margin conversion is explicit.

## 19. Before / After Backtest Comparison

| profile_id | eligible representative triggers | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 17.02 | -10.04 | 0.50 | 0 | 0 | mixed: supplier false positives remain |
| P0b e2r_2_0_baseline_reference | 4 | 17.02 | -10.04 | 0.50 | 1 | 1 | weaker early positive capture |
| P1 sector_specific_candidate_profile | 4 | 26.77 | -4.07 | 0.00 | 0 | 0 | improved by excluding supplier non-conversion |
| P2 canonical_archetype_candidate_profile | 4 | 26.77 | -4.07 | 0.00 | 0 | 0 | improved C29 compression |
| P3 counterexample_guard_profile | 2 | 26.77 | -4.07 | 0.00 | 0 | 0 | best precision, lower breadth |

Representative inclusion under P1/P2 keeps Hyundai and Kia, while Hanon and HL Mando are not allowed to promote without margin/FCF conversion.

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| TR_C29_HMC_STAGE2_20230126 | 78 | Stage2-Actionable | 80 | Stage2-Actionable | 20.93 | -4.52 | aligned_positive |
| TR_C29_KIA_STAGE2_20230126 | 80 | Stage2-Actionable | 82 | Stage2-Actionable | 32.61 | -3.61 | aligned_positive |
| TR_C29_HANON_STAGE2_20210108 | 76 | Stage2-Actionable | 68 | Watch/Yellow-blocked | 9.49 | -17.62 | corrected_false_positive |
| TR_C29_HL_MANDO_STAGE2_20230303 | 75 | Stage2-Actionable | 67 | Watch/Yellow-blocked | 6.03 | -14.40 | corrected_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 2 | true | true | C29 now has balanced complete-vehicle positive and supplier counterexample coverage |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - supplier_ev_theme_false_positive
  - price_only_local_4b_too_early
new_axis_proposed:
  - C29_complete_vehicle_volume_mix_margin_bonus
  - C29_supplier_operating_leverage_conversion_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- actual stock-web tradable OHLC rows were used for entry/peak/MAE/MFE proxies;
- manifest max date was taken from stock-web, not current date;
- all representative cases have at least 180 forward trading days;
- corporate-action candidate windows do not contaminate the 180D calibration window;
- same-entry dedupe is applied for aggregate representative rows;
- local 4B and full-window 4B proximity are split.

Not validated:

- production scoring code;
- live scan behavior;
- broker/API behavior;
- current stock recommendations;
- exact sell-side revision timestamps beyond public evidence-date proxies.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_complete_vehicle_volume_mix_margin_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"complete-vehicle cases with visible volume/mix/margin had strong 90D MFE and modest MAE","avg kept positives MFE90=26.77 / MAE90=-4.07","TR_C29_HMC_STAGE2_20230126|TR_C29_KIA_STAGE2_20230126",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_supplier_operating_leverage_conversion_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"supplier EV theme without margin/FCF conversion produced poor MFE/MAE","blocked false positives Hanon and HL Mando","TR_C29_HANON_STAGE2_20210108|TR_C29_HL_MANDO_STAGE2_20230303",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_only_local_4B_guard,existing_axis_strengthened,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"local price-only peaks were too early versus full window","supports existing 4B non-price requirement","TR_C29_HMC_4B_LOCAL_20230510|TR_C29_KIA_4B_LOCAL_20230511",2,2,0,medium,axis_stress_test,"do not change production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C29_HMC_2023_Q4_EXPORT_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_C29_HMC_STAGE2_20230126","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"complete vehicle volume/mix/margin evidence worked"}
{"row_type":"case","case_id":"C29_KIA_2023_RECORD_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_C29_KIA_STAGE2_20230126","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"complete vehicle margin/capital return evidence worked"}
{"row_type":"case","case_id":"C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR_C29_HANON_STAGE2_20210108","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"EV thermal exposure without margin bridge failed"}
{"row_type":"case","case_id":"C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP","symbol":"204320","company_name":"HL만도","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_C29_HL_MANDO_STAGE2_20230303","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"EV/autonomous supplier theme did not convert to durable margin"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TR_C29_HMC_STAGE2_20230126","case_id":"C29_HMC_2023_Q4_EXPORT_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","sector":"mobility","primary_archetype":"complete_vehicle_volume_mix_margin","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","evidence_available_at_that_date":"Q4/FY earnings, export mix and margin visibility","evidence_source":"public earnings and market news","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-26","entry_price":174900,"MFE_30D_pct":3.14,"MFE_90D_pct":20.93,"MFE_180D_pct":20.93,"MFE_1Y_pct":49.23,"MFE_2Y_pct":70.95,"MAE_30D_pct":-4.52,"MAE_90D_pct":-4.52,"MAE_180D_pct":-4.52,"MAE_1Y_pct":-4.52,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":261000,"drawdown_after_peak_pct":-17.43,"green_lateness_ratio":0.30,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GRP_C29_HMC_20230126","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C29_HMC_4B_LOCAL_20230510","case_id":"C29_HMC_2023_Q4_EXPORT_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","sector":"mobility","primary_archetype":"complete_vehicle_volume_mix_margin","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-05-10","evidence_available_at_that_date":"local price peak only","evidence_source":"stock-web OHLC local price path","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-10","entry_price":210000,"MFE_30D_pct":0.71,"MFE_90D_pct":0.71,"MFE_180D_pct":0.71,"MFE_1Y_pct":24.29,"MFE_2Y_pct":42.38,"MAE_30D_pct":-7.62,"MAE_90D_pct":-19.38,"MAE_180D_pct":-19.38,"MAE_1Y_pct":-19.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":261000,"drawdown_after_peak_pct":-17.43,"green_lateness_ratio":0.30,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.41,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GRP_C29_HMC_20230510_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B timing overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR_C29_KIA_STAGE2_20230126","case_id":"C29_KIA_2023_RECORD_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","sector":"mobility","primary_archetype":"complete_vehicle_volume_mix_margin","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","evidence_available_at_that_date":"record margin/profit and mix visibility","evidence_source":"public earnings and market news","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-26","entry_price":69300,"MFE_30D_pct":15.01,"MFE_90D_pct":32.61,"MFE_180D_pct":32.61,"MFE_1Y_pct":75.90,"MFE_2Y_pct":90.04,"MAE_30D_pct":-3.61,"MAE_90D_pct":-3.61,"MAE_180D_pct":-3.61,"MAE_1Y_pct":-3.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-11","peak_price":131700,"drawdown_after_peak_pct":-22.70,"green_lateness_ratio":0.26,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GRP_C29_KIA_20230126","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C29_KIA_4B_LOCAL_20230511","case_id":"C29_KIA_2023_RECORD_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","sector":"mobility","primary_archetype":"complete_vehicle_volume_mix_margin","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-05-11","evidence_available_at_that_date":"local price peak only","evidence_source":"stock-web OHLC local price path","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-11","entry_price":90100,"MFE_30D_pct":1.998,"MFE_90D_pct":1.998,"MFE_180D_pct":11.99,"MFE_1Y_pct":46.17,"MFE_2Y_pct":46.17,"MAE_30D_pct":-10.32,"MAE_90D_pct":-14.65,"MAE_180D_pct":-14.65,"MAE_1Y_pct":-14.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-11","peak_price":131700,"drawdown_after_peak_pct":-22.70,"green_lateness_ratio":0.26,"four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.33,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GRP_C29_KIA_20230511_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B timing overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR_C29_HANON_STAGE2_20210108","case_id":"C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","sector":"mobility supplier","primary_archetype":"supplier_ev_theme_without_margin_conversion","loop_objective":"counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-08","evidence_available_at_that_date":"EV thermal-management theme surge and RS","evidence_source":"market theme / customer optionality narrative","stage2_evidence_fields":["customer_or_order_quality","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018880/2021.csv","profile_path":"atlas/symbol_profiles/018/018880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-08","entry_price":18450,"MFE_30D_pct":9.49,"MFE_90D_pct":9.49,"MFE_180D_pct":9.49,"MFE_1Y_pct":9.49,"MFE_2Y_pct":9.49,"MAE_30D_pct":-17.62,"MAE_90D_pct":-17.62,"MAE_180D_pct":-20.33,"MAE_1Y_pct":-30.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-08","peak_price":20200,"drawdown_after_peak_pct":-36.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GRP_C29_HANON_20210108","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_C29_HL_MANDO_STAGE2_20230303","case_id":"C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP","symbol":"204320","company_name":"HL만도","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_AND_EV_SUPPLIER_CONVERSION","sector":"mobility supplier","primary_archetype":"supplier_ev_theme_without_margin_conversion","loop_objective":"counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-03","evidence_available_at_that_date":"EV/autonomous supplier rerating attempt and RS","evidence_source":"market theme / customer optionality narrative","stage2_evidence_fields":["customer_or_order_quality","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","execution_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-03","entry_price":51400,"MFE_30D_pct":1.36,"MFE_90D_pct":6.03,"MFE_180D_pct":6.03,"MFE_1Y_pct":6.03,"MFE_2Y_pct":16.34,"MAE_30D_pct":-14.40,"MAE_90D_pct":-14.40,"MAE_180D_pct":-22.28,"MAE_1Y_pct":-22.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-30","peak_price":54500,"drawdown_after_peak_pct":-26.70,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"GRP_C29_HL_MANDO_20230303","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_HMC_2023_Q4_EXPORT_MARGIN","trigger_id":"TR_C29_HMC_STAGE2_20230126","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":70,"revision_score":65,"relative_strength_score":40,"customer_quality_score":60,"policy_or_regulatory_score":20,"valuation_repricing_score":35,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":65,"fcf_conversion_score":55},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":75,"revision_score":65,"relative_strength_score":40,"customer_quality_score":60,"policy_or_regulatory_score":20,"valuation_repricing_score":35,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":70,"fcf_conversion_score":60},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","capacity_or_shipment_score","fcf_conversion_score"],"component_delta_explanation":"complete-vehicle mix/margin bridge gets small C29 bonus","MFE_90D_pct":20.93,"MAE_90D_pct":-4.52,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_KIA_2023_RECORD_MARGIN","trigger_id":"TR_C29_KIA_STAGE2_20230126","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":75,"revision_score":70,"relative_strength_score":45,"customer_quality_score":60,"policy_or_regulatory_score":20,"valuation_repricing_score":40,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":70,"fcf_conversion_score":60},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":80,"revision_score":70,"relative_strength_score":45,"customer_quality_score":60,"policy_or_regulatory_score":20,"valuation_repricing_score":40,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":75,"fcf_conversion_score":65},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","capacity_or_shipment_score","fcf_conversion_score"],"component_delta_explanation":"record margin plus capital-return visibility supports C29 bonus","MFE_90D_pct":32.61,"MAE_90D_pct":-3.61,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_HANON_2021_EV_THERMAL_FALSE_POSITIVE","trigger_id":"TR_C29_HANON_STAGE2_20210108","symbol":"018880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":75,"customer_quality_score":65,"policy_or_regulatory_score":55,"valuation_repricing_score":50,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":30,"fcf_conversion_score":10},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":65,"customer_quality_score":55,"policy_or_regulatory_score":50,"valuation_repricing_score":40,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":25,"fcf_conversion_score":5},"weighted_score_after":68,"stage_label_after":"Watch/Yellow-blocked","changed_components":["margin_bridge_score","revision_score","execution_risk_score","fcf_conversion_score"],"component_delta_explanation":"supplier conversion guard blocks EV theme without margin/FCF confirmation","MFE_90D_pct":9.49,"MAE_90D_pct":-17.62,"score_return_alignment_label":"corrected_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_HL_MANDO_2023_EV_SUPPLIER_MARGIN_GAP","trigger_id":"TR_C29_HL_MANDO_STAGE2_20230303","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":50,"valuation_repricing_score":45,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":35,"fcf_conversion_score":10},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":20,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":60,"customer_quality_score":55,"policy_or_regulatory_score":45,"valuation_repricing_score":35,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":30,"fcf_conversion_score":5},"weighted_score_after":67,"stage_label_after":"Watch/Yellow-blocked","changed_components":["margin_bridge_score","revision_score","execution_risk_score","fcf_conversion_score"],"component_delta_explanation":"supplier conversion guard blocks theme-only EV supplier promotion","MFE_90D_pct":6.03,"MAE_90D_pct":-14.40,"score_return_alignment_label":"corrected_false_positive","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See section 24 CSV.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"74","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","scheduled_round":"R9","scheduled_loop":"74","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["supplier_ev_theme_false_positive","price_only_local_4b_too_early"],"diversity_score_summary":"new_symbols=4; new_trigger_families=4; counterexamples=2; residual_errors=2; wrong_round_penalty=0; schema_rematerialization_penalty=0","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"C29_NO_HARD_4C_ROW","symbol":null,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"no discrete 4C thesis-break event was used for quantitative calibration in this loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
completed_loop = 74
next_round = R10
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- This MD uses Songdaiki/stock-web as the only quantitative price source.
- Stock-web manifest max date used: 2026-02-20.
- Evidence-source text is historical/narrative and not used to compute price metrics.
- No stock_agent source code was opened or patched.
- No investment recommendation is made.

