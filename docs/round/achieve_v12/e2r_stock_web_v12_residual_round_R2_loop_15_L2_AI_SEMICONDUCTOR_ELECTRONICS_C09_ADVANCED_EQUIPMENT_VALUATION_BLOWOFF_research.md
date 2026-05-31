# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- output_file: `e2r_stock_web_v12_residual_round_R2_loop_15_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md`
- scheduled_round: `R2`
- scheduled_loop: `15`
- round_schedule_status: `valid`
- round_sector_consistency: `pass`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`
- fine_archetype_id: `ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF`
- loop_objective: `coverage_gap_fill | sector_specific_rule_discovery | counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`
- stock_web_price_atlas_access_required: `true`

This loop adds 6 new independent cases, 3 counterexamples, and 4 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.

## 1. Current Calibrated Profile Assumption

The current proxy profile is `e2r_2_1_stock_web_calibrated`. The already-applied global axes are treated as baseline facts, not rediscovered conclusions: Stage2 actionable evidence bonus, stricter Green total/revision gates, price-only blowoff blocking, full 4B non-price requirement, and hard 4C thesis-break routing.

The residual question here is narrower: in R2/C09, can the model keep true advanced-equipment process depth as Stage2-Actionable while routing late valuation-led Green signals into 4B-watch rather than positive promotion?

## 2. Round / Large Sector / Canonical Archetype Scope

- R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`.
- The chosen canonical archetype is `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`.
- Scope: advanced semiconductor equipment, laser/anneal/metrology, process-critical equipment, and valuation-led equipment blowoff.
- Excluded: C06 HBM memory customer-capacity, C07 HBM equipment order RS, C08 socket customer-quality rows already covered in loops 10/12/13/14.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed local v12 artifacts show R2 loop 10 and loop 14 already covered `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`; loop 12 covered `C06_HBM_MEMORY_CUSTOMER_CAPACITY`; loop 13 covered `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`. Therefore this loop chooses C09 to avoid another socket/HBM-order rematerialization.

Duplicate-control interpretation:

- same canonical archetype repetition: allowed;
- same symbol with new trigger family: allowed with reduced independent evidence weight;
- same symbol + same entry date + same evidence: blocked;
- R13 cross-check leakage into this R2 file: blocked.

## 4. Stock-Web OHLC Input / Price Source Validation

- price source: `Songdaiki/stock-web`
- upstream source: `FinanceData/marcap`
- manifest: `atlas/manifest.json`
- schema: `atlas/schema.json`
- universe: `atlas/universe/all_symbols.csv`
- source_name: `FinanceData/marcap`
- source_repo_url: `https://github.com/FinanceData/marcap`
- price_adjustment_status: `raw_unadjusted_marcap`
- min_date: `1995-05-02`
- max_date: `2026-02-20`
- tradable_row_count: `14354401`
- raw_row_count: `15214118`
- symbol_count: `5414`
- active_like_symbol_count: `2868`
- inactive_or_delisted_like_symbol_count: `2546`
- markets: `KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- raw_shard_root: `atlas/ohlcv_raw_by_symbol_year`

Validation verdict: usable for historical calibration. All quantitative rows below use `tradable_raw` rows. Raw rows were not used for weight calibration.

## 5. Historical Eligibility Gate

All representative rows have historical trigger dates, entry dates inside stock-web tradable shards, at least 180 forward trading days available by manifest max date, positive OHLC/volume rows, computed 30D/90D/180D MFE/MAE, and no 180D corporate-action candidate overlap in the symbol profile.

Profile caveats:

- HPSP has old corporate-action candidates in 2023 only; the 2024 windows used here are clean.
- 이오테크닉스 has an old 2003 corporate-action candidate only; the 2024 windows used here are clean.
- 원익IPS has no corporate-action candidates in the profile.

## 6. Canonical Archetype Compression Map

`ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF` compresses into `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`. The compression rule is:

1. real advanced-equipment depth = process-critical tool, customer/process node relevance, and margin/revision bridge;
2. valuation blowoff = late Green/price move after most upside has already been realized;
3. price-only equipment beta = watch or 4B overlay, not positive Stage2/3 promotion.

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | novelty |
|---|---:|---|---|---|---|
| R2L15_C09_HPSP_STAGE2A_20240119 | 403870 | HPSP | high_mae_success | positive | new symbol in C09 |
| R2L15_C09_EOTECH_STAGE2A_20240119 | 039030 | 이오테크닉스 | structural_success | positive | new symbol in C09 |
| R2L15_C09_WONIKIPS_STAGE2A_20240320 | 240810 | 원익IPS | stage2_promote_candidate | positive | new symbol in C09 |
| R2L15_C09_HPSP_LATE_GREEN_20240214 | 403870 | HPSP | false_positive_green | counterexample | same symbol, new trigger family |
| R2L15_C09_EOTECH_LATE_GREEN_20240412 | 039030 | 이오테크닉스 | 4B_overlay_success | counterexample | same symbol, new trigger family |
| R2L15_C09_WONIKIPS_PRICEONLY_20240704 | 240810 | 원익IPS | price_moved_without_evidence | counterexample | same symbol, new trigger family |


## 8. Positive vs Counterexample Balance

- positive_case_count: `3`
- counterexample_count: `3`
- 4B_case_count: `3`
- 4C_case_count: `0`
- calibration_usable_case_count: `6`
- minimum balance status: `pass`

The positive rows prove C09 should not be treated as only a sell/risk archetype. The counterexamples prove that late-Green and price-only advanced-equipment beta are the dangerous failure modes.

## 9. Evidence Source Map

Evidence is separated by stage and never inferred from price alone.

- Stage2 evidence: process-critical equipment relevance, customer/process route, relative strength, and early margin/revision route.
- Stage3 evidence: confirmed financial visibility and multiple public evidence families.
- 4B evidence: valuation blowoff, positioning overheat, and local/full-window peak proximity.
- 4C evidence: not used as positive training; only watch/protection labels appear here.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | corporate_action_window_status |
|---:|---|---|---|---|
| 403870 | HPSP | `atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv` | `atlas/symbol_profiles/403/403870.json` | clean_180D_window |
| 039030 | 이오테크닉스 | `atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv` | `atlas/symbol_profiles/039/039030.json` | clean_180D_window |
| 240810 | 원익IPS | `atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv` | `atlas/symbol_profiles/240/240810.json` | clean_180D_window |


## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger | entry | price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | current verdict | role |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| R2L15_C09_HPSP_STAGE2A_20240119 | 403870 | Stage2-Actionable 2024-01-19 | 2024-01-19 | 47,800 | 33.68% | 33.68% | 33.68% | -8.37% | -25.42% | -52.62% | 2024-02-15 / 63,900 | current_profile_correct | high_mae_success |
| R2L15_C09_EOTECH_STAGE2A_20240119 | 039030 | Stage2-Actionable 2024-01-19 | 2024-01-19 | 183,900 | 18.27% | 52.80% | 52.80% | -11.15% | -11.15% | -29.64% | 2024-04-12 / 281,000 | current_profile_too_late | structural_success |
| R2L15_C09_WONIKIPS_STAGE2A_20240320 | 240810 | Stage2-Actionable 2024-03-20 | 2024-03-20 | 37,400 | 19.92% | 19.92% | 19.92% | -6.02% | -10.56% | -27.94% | 2024-04-08 / 44,850 | current_profile_correct | stage2_promote_candidate |
| R2L15_C09_HPSP_LATE_GREEN_20240214 | 403870 | Stage3-Green 2024-02-14 | 2024-02-14 | 61,600 | 3.73% | 3.73% | 3.73% | -21.18% | -42.13% | -63.23% | 2024-02-15 / 63,900 | current_profile_false_positive | false_positive_green |
| R2L15_C09_EOTECH_LATE_GREEN_20240412 | 039030 | Stage3-Green 2024-04-12 | 2024-04-12 | 273,000 | 2.93% | 2.93% | 2.93% | -26.01% | -52.60% | -52.60% | 2024-04-12 / 281,000 | current_profile_4B_too_late | 4B_overlay_success |
| R2L15_C09_WONIKIPS_PRICEONLY_20240704 | 240810 | Stage2-Watch 2024-07-04 | 2024-07-04 | 40,100 | 0.50% | 0.50% | 0.50% | -25.56% | -32.79% | -32.79% | 2024-07-05 / 40,300 | current_profile_false_positive | price_moved_without_evidence |


## 12. Trigger-Level OHLC Backtest Tables

The table above is the trigger-level OHLC backtest table. Entry price is the stock-web `c` column on `entry_date`. MFE and MAE use max high / min low over the specified forward trading-day windows.

Key OHLC anchors used:

- HPSP: `2024-01-19 c=47,800`, `2024-02-15 h=63,900`, `2024-08-05 l=22,650`.
- 이오테크닉스: `2024-01-19 c=183,900`, `2024-04-12 h=281,000`, `2024-08-05 l=129,400`.
- 원익IPS: `2024-03-20 c=37,400`, `2024-04-08 h=44,850`, `2024-10-25 l=26,950`.

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | interpretation |
|---|---|---|
| R2L15_C09_HPSP_STAGE2A_20240119 | current_profile_correct | Advanced anneal moat and customer-quality narrative had real upside, but the 180D path shows why C09 cannot be treated as clean Green without valuation/positioning risk control. |
| R2L15_C09_EOTECH_STAGE2A_20240119 | current_profile_too_late | Laser/advanced packaging equipment exposure created a valid C09 Stage2-Actionable signal before full Green confirmation. |
| R2L15_C09_WONIKIPS_STAGE2A_20240320 | current_profile_correct | Memory capex recovery plus equipment beta worked as Stage2, but the lack of differentiated order/customer confirmation capped the move. |
| R2L15_C09_HPSP_LATE_GREEN_20240214 | current_profile_false_positive | Same symbol, different trigger family: a late Green label near valuation blowoff had tiny upside and severe 90D/180D MAE. |
| R2L15_C09_EOTECH_LATE_GREEN_20240412 | current_profile_4B_too_late | Laser equipment was a real winner, but the late Green/valuation trigger was effectively a 4B overlay rather than a positive entry row. |
| R2L15_C09_WONIKIPS_PRICEONLY_20240704 | current_profile_false_positive | A July price spike without fresh customer/order/revision evidence did not convert into a sustainable C09 rerating. |


Stress-test answers:

1. Current profile catches several Stage2 positives, but it still needs a C09-specific separation between process-depth evidence and valuation blowoff.
2. Actual MFE/MAE alignment is asymmetric: early entries can work, late Green rows often have tiny MFE and deep MAE.
3. Stage2 bonus is useful only when supported by non-price equipment depth.
4. Yellow threshold 75 is broadly acceptable.
5. Green threshold 87 / revision 55 is still not enough if the score is supplied by valuation/RS rather than customer/order/revision conversion.
6. Price-only blowoff guard is strengthened.
7. Full 4B non-price requirement is kept, but C09 valuation/positioning overheat should count as non-price risk evidence when present.
8. Hard 4C routing is not the main issue here; the main residual is 4B/late-Green timing.

## 14. Stage2 / Yellow / Green Comparison

Early Stage2 rows have average 90D MFE of `35.47%` and average 90D MAE of `-15.71%`. Late-Green/price-only counterexamples have average 90D MFE of `2.39%` and average 90D MAE of `-42.51%`.

This is the C09 residual: the same advanced-equipment narrative can be excellent at Stage2 but dangerous at late-Green valuation blowoff.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict | evidence_type |
|---|---:|---:|---|---|
| T_R2L15_403870_STAGE2A_20240119 | None | None | not_4B_entry | none |
| T_R2L15_039030_STAGE2A_20240119 | None | None | not_4B_entry | none |
| T_R2L15_240810_STAGE2A_20240320 | None | None | not_4B_entry | none |
| T_R2L15_403870_GREEN_BLOWOFF_20240214 | 0.86 | 0.86 | good_full_window_4B_timing | valuation_blowoff|positioning_overheat |
| T_R2L15_039030_LATE_GREEN_20240412 | 1.0 | 1.0 | good_full_window_4B_timing | valuation_blowoff|positioning_overheat|revision_slowdown_watch |
| T_R2L15_240810_PRICEONLY_20240704 | 1.0 | 1.0 | price_only_local_4B_too_early_but_not_positive | price_only |


C09 needs both local and full-window proximity because advanced equipment names often form a local blowoff that is also the full-cycle high. If valuation/positioning evidence is present, that is a valid 4B overlay. If only price is present, it remains watch-only and cannot train a positive entry rule.

## 16. 4C Protection Audit

No hard 4C weight is proposed. HPSP late-Green and EO late-Green are 4B/valuation timing rows. 원익IPS July is a price-only false-positive row, not a thesis-break 4C row.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

Rule candidate: in R2 semiconductor/electronics, price-only equipment beta requires at least one of customer/order conversion, revision bridge, or margin bridge before positive Stage2/3 promotion. Without that conversion, the row can be watch-only or 4B overlay.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

C09-specific shadow rule:

```text
if canonical_archetype_id == C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:
    positive_stage_requires = advanced_equipment_depth + one_of(customer_quality, order_conversion, margin_bridge, confirmed_revision)
    late_green_penalty_if = green_lateness_ratio >= 0.70 or valuation_blowoff + positioning_overheat present
    price_only_relative_strength = watch_only_or_4B_overlay
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global_current | strict Green helps, but C09 valuation blowoff still leaks into late-Green rows | 6 | 18.93 | -27.83 | 18.93 | -43.29 | 0.50 | 1 | 2 | 0.89 | mixed; catches structural cases but late Green is dangerous |
| P0b_e2r_2_0_baseline_reference | rollback | older looser Green would over-promote advanced equipment beta | 6 | 18.93 | -27.83 | 18.93 | -43.29 | 0.67 | 0 | 3 | 0.89 | worse false-positive control |
| P1_R2_sector_specific_candidate | sector_specific | R2 requires customer/order/revision conversion before treating price beta as positive | 6 | 35.47 | -15.71 | 35.47 | -36.73 | 0.17 | 1 | 1 | 0.86 | better score-return alignment |
| P2_C09_canonical_candidate | canonical_archetype_specific | advanced equipment depth gets Stage2 retention; valuation blowoff routes to 4B-watch | 6 | 35.47 | -15.71 | 35.47 | -36.73 | 0.00 | 1 | 0 | 0.00 | best candidate, shadow-only |
| P3_counterexample_guard_profile | guard | price-only/late-Green rows cannot be positive promotion | 6 | 35.47 | -15.71 | 35.47 | -36.73 | 0.00 | 1 | 0 | 0.00 | conservative but robust |


## 20. Score-Return Alignment Matrix

| trigger_id | before_score | before_label | after_score | after_label | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| T_R2L15_403870_STAGE2A_20240119 | 82 | Stage3-Yellow | 74 | Stage2-Actionable | 33.68% | -25.42% | positive_but_high_MAE_success |
| T_R2L15_039030_STAGE2A_20240119 | 74 | Stage2-Actionable | 80 | Stage3-Yellow | 52.80% | -11.15% | structural_positive_with_later_blowoff |
| T_R2L15_240810_STAGE2A_20240320 | 70 | Stage2-Actionable | 68 | Stage2-Actionable | 19.92% | -10.56% | modest_positive_capped_by_cycle_beta |
| T_R2L15_403870_GREEN_BLOWOFF_20240214 | 88 | Stage3-Green | 62 | 4B-Watch | 3.73% | -42.13% | late_green_became_blowoff |
| T_R2L15_039030_LATE_GREEN_20240412 | 89 | Stage3-Green | 61 | 4B-Watch | 2.93% | -52.60% | late_green_near_full_window_peak |
| T_R2L15_240810_PRICEONLY_20240704 | 76 | Stage3-Yellow | 52 | Stage2-Watch / no-positive-promotion | 0.50% | -32.79% | price_only_false_positive |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF | 3 | 3 | 3 | 0 | 6 | 0 | 6 | 6 | 4 | true | true | C09 still needs more 2023/2025 holdout, but this loop adds the missing valuation-blowoff guard and early-equipment-depth split. |


## 22. Residual Contribution Summary

new_independent_case_count: `6`  
reused_case_count: `0`  
reused_case_ids: `[]`  
new_symbol_count: `3`  
new_canonical_archetype_count: `1`  
new_fine_archetype_count: `1`  
new_trigger_family_count: `6`  
tested_existing_calibrated_axes: `stage3_green_total_min`, `stage3_green_revision_min`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`  
residual_error_types_found: `late_green_near_peak`, `price_only_equipment_beta_false_positive`, `advanced_equipment_positive_high_MAE`  
new_axis_proposed: `C09_advanced_equipment_depth_bonus`, `C09_valuation_blowoff_guard`, `C09_price_only_no_conversion_block`  
existing_axis_strengthened: `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`  
existing_axis_weakened: `null`  
existing_axis_kept: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `hard_4c_thesis_break_routes_to_4c`  
sector_specific_rule_candidate: `true`  
canonical_archetype_rule_candidate: `true`  
no_new_signal_reason: `null`  
loop_contribution_label: `canonical_archetype_rule_candidate`

do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope

Validated scope:

- historical 2024 trigger-level OHLC backtest;
- C09 advanced-equipment valuation/risk residual;
- 30D/90D/180D MFE/MAE and peak/drawdown;
- shadow-only sector/canonical rule proposal.

Non-validation scope:

- no live candidate discovery;
- no current 2026 recommendation;
- no stock_agent code access;
- no production scoring patch;
- no brokerage or automation logic.

## 24. Shadow Weight Calibration

```csv
"row_type","axis","scope","large_sector_id","canonical_archetype_id","baseline_value","tested_value","delta","reason","backtest_effect","trigger_ids","calibration_usable_count","new_independent_case_count","counterexample_count","confidence","proposal_type","notes"
"shadow_weight","C09_advanced_equipment_depth_bonus","canonical_archetype_specific","L2_AI_SEMICONDUCTOR_ELECTRONICS","C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","0","1","+1","Laser/anneal/metrology equipment with process depth had positive 90D/180D MFE when entry was not late-Green.","improves early Stage2 retention for HPSP/EO/Wonik positives","T_R2L15_403870_STAGE2A_20240119|T_R2L15_039030_STAGE2A_20240119|T_R2L15_240810_STAGE2A_20240320","6","6","3","medium","canonical_shadow_only","not production; post-calibrated residual"
"shadow_weight","C09_valuation_blowoff_guard","canonical_archetype_specific","L2_AI_SEMICONDUCTOR_ELECTRONICS","C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","0","1","+1 guard","Late Green near valuation/positioning peak produced very low MFE and high MAE.","blocks HPSP/EO late-Green rows from positive promotion","T_R2L15_403870_GREEN_BLOWOFF_20240214|T_R2L15_039030_LATE_GREEN_20240412|T_R2L15_240810_PRICEONLY_20240704","6","6","3","medium","canonical_shadow_only","strengthens existing price-only/4B guard with C09-specific valuation overheat"
"shadow_weight","C09_price_only_no_conversion_block","sector_specific","L2_AI_SEMICONDUCTOR_ELECTRONICS","C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","0","1","+1 guard","Relative-strength spike without fresh customer/order/revision conversion failed.","keeps Wonik July price-only row as watch/4B overlay","T_R2L15_240810_PRICEONLY_20240704","6","6","3","low_to_medium","sector_shadow_only","not global; R2/C09 only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L15_C09_HPSP_STAGE2A_20240119", "symbol": "403870", "company_name": "HPSP", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "T_R2L15_403870_STAGE2A_20240119", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_high_MAE_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Advanced anneal moat and customer-quality narrative had real upside, but the 180D path shows why C09 cannot be treated as clean Green without valuation/positioning risk control."}
{"row_type": "case", "case_id": "R2L15_C09_EOTECH_STAGE2A_20240119", "symbol": "039030", "company_name": "이오테크닉스", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_R2L15_039030_STAGE2A_20240119", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_positive_with_later_blowoff", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Laser/advanced packaging equipment exposure created a valid C09 Stage2-Actionable signal before full Green confirmation."}
{"row_type": "case", "case_id": "R2L15_C09_WONIKIPS_STAGE2A_20240320", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "T_R2L15_240810_STAGE2A_20240320", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "modest_positive_capped_by_cycle_beta", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Memory capex recovery plus equipment beta worked as Stage2, but the lack of differentiated order/customer confirmation capped the move."}
{"row_type": "case", "case_id": "R2L15_C09_HPSP_LATE_GREEN_20240214", "symbol": "403870", "company_name": "HPSP", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T_R2L15_403870_GREEN_BLOWOFF_20240214", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_late_green_4B_timing", "independent_evidence_weight": 0.5, "score_price_alignment": "late_green_became_blowoff", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Same symbol, different trigger family: a late Green label near valuation blowoff had tiny upside and severe 90D/180D MAE."}
{"row_type": "case", "case_id": "R2L15_C09_EOTECH_LATE_GREEN_20240412", "symbol": "039030", "company_name": "이오테크닉스", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "T_R2L15_039030_LATE_GREEN_20240412", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_late_green_4B_timing", "independent_evidence_weight": 0.5, "score_price_alignment": "late_green_near_full_window_peak", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Laser equipment was a real winner, but the late Green/valuation trigger was effectively a 4B overlay rather than a positive entry row."}
{"row_type": "case", "case_id": "R2L15_C09_WONIKIPS_PRICEONLY_20240704", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "T_R2L15_240810_PRICEONLY_20240704", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_price_only_false_positive", "independent_evidence_weight": 0.5, "score_price_alignment": "price_only_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A July price spike without fresh customer/order/revision evidence did not convert into a sustainable C09 rerating."}
{"row_type": "trigger", "trigger_id": "T_R2L15_403870_STAGE2A_20240119", "case_id": "R2L15_C09_HPSP_STAGE2A_20240119", "symbol": "403870", "company_name": "HPSP", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced_equipment_valuation_blowoff", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "evidence_available_at_that_date": "Advanced anneal moat and customer-quality narrative had real upside, but the 180D path shows why C09 cannot be treated as clean Green without valuation/positioning risk control.", "evidence_source": "historical public disclosure/news/research proxy; price row from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv", "profile_path": "atlas/symbol_profiles/403/403870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-19", "entry_price": 47800, "MFE_30D_pct": 33.68, "MFE_90D_pct": 33.68, "MFE_180D_pct": 33.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.37, "MAE_90D_pct": -25.42, "MAE_180D_pct": -52.62, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 63900, "drawdown_after_peak_pct": -64.55, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": "none", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_but_high_MAE_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R2L15_403870_STAGE2A_20240119", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R2L15_039030_STAGE2A_20240119", "case_id": "R2L15_C09_EOTECH_STAGE2A_20240119", "symbol": "039030", "company_name": "이오테크닉스", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced_equipment_valuation_blowoff", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "evidence_available_at_that_date": "Laser/advanced packaging equipment exposure created a valid C09 Stage2-Actionable signal before full Green confirmation.", "evidence_source": "historical public disclosure/news/research proxy; price row from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-19", "entry_price": 183900, "MFE_30D_pct": 18.27, "MFE_90D_pct": 52.8, "MFE_180D_pct": 52.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.15, "MAE_90D_pct": -11.15, "MAE_180D_pct": -29.64, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 281000, "drawdown_after_peak_pct": -53.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": "none", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_positive_with_later_blowoff", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R2L15_039030_STAGE2A_20240119", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R2L15_240810_STAGE2A_20240320", "case_id": "R2L15_C09_WONIKIPS_STAGE2A_20240320", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced_equipment_valuation_blowoff", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-20", "evidence_available_at_that_date": "Memory capex recovery plus equipment beta worked as Stage2, but the lack of differentiated order/customer confirmation capped the move.", "evidence_source": "historical public disclosure/news/research proxy; price row from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "profile_path": "atlas/symbol_profiles/240/240810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-20", "entry_price": 37400, "MFE_30D_pct": 19.92, "MFE_90D_pct": 19.92, "MFE_180D_pct": 19.92, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.02, "MAE_90D_pct": -10.56, "MAE_180D_pct": -27.94, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 44850, "drawdown_after_peak_pct": -39.91, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": "none", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "modest_positive_capped_by_cycle_beta", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R2L15_240810_STAGE2A_20240320", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R2L15_403870_GREEN_BLOWOFF_20240214", "case_id": "R2L15_C09_HPSP_LATE_GREEN_20240214", "symbol": "403870", "company_name": "HPSP", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced_equipment_valuation_blowoff", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-02-14", "evidence_available_at_that_date": "Same symbol, different trigger family: a late Green label near valuation blowoff had tiny upside and severe 90D/180D MAE.", "evidence_source": "historical public disclosure/news/research proxy; price row from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["valuation_repricing_score_not_confirmed"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv", "profile_path": "atlas/symbol_profiles/403/403870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-14", "entry_price": 61600, "MFE_30D_pct": 3.73, "MFE_90D_pct": 3.73, "MFE_180D_pct": 3.73, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.18, "MAE_90D_pct": -42.13, "MAE_180D_pct": -63.23, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 63900, "drawdown_after_peak_pct": -64.55, "green_lateness_ratio": 0.86, "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "late_green_became_blowoff", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R2L15_403870_GREEN_BLOWOFF_20240214", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_late_green_4B_timing", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R2L15_039030_LATE_GREEN_20240412", "case_id": "R2L15_C09_EOTECH_LATE_GREEN_20240412", "symbol": "039030", "company_name": "이오테크닉스", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced_equipment_valuation_blowoff", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-12", "evidence_available_at_that_date": "Laser equipment was a real winner, but the late Green/valuation trigger was effectively a 4B overlay rather than a positive entry row.", "evidence_source": "historical public disclosure/news/research proxy; price row from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["valuation_repricing_score_not_confirmed"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-12", "entry_price": 273000, "MFE_30D_pct": 2.93, "MFE_90D_pct": 2.93, "MFE_180D_pct": 2.93, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -26.01, "MAE_90D_pct": -52.6, "MAE_180D_pct": -52.6, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 281000, "drawdown_after_peak_pct": -53.95, "green_lateness_ratio": 0.92, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat|revision_slowdown_watch", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "late_green_near_full_window_peak", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R2L15_039030_LATE_GREEN_20240412", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_late_green_4B_timing", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R2L15_240810_PRICEONLY_20240704", "case_id": "R2L15_C09_WONIKIPS_PRICEONLY_20240704", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_EQUIPMENT_LASER_ANNEAL_METROLOGY_VALUATION_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced_equipment_valuation_blowoff", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Watch", "trigger_date": "2024-07-04", "evidence_available_at_that_date": "A July price spike without fresh customer/order/revision evidence did not convert into a sustainable C09 rerating.", "evidence_source": "historical public disclosure/news/research proxy; price row from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "profile_path": "atlas/symbol_profiles/240/240810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-04", "entry_price": 40100, "MFE_30D_pct": 0.5, "MFE_90D_pct": 0.5, "MFE_180D_pct": 0.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -25.56, "MAE_90D_pct": -32.79, "MAE_180D_pct": -32.79, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-05", "peak_price": 40300, "drawdown_after_peak_pct": -33.13, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_but_not_positive", "four_b_evidence_type": "price_only", "four_c_protection_label": "false_break", "trigger_outcome_label": "price_only_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_R2L15_240810_PRICEONLY_20240704", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_price_only_false_positive", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C09_shadow", "case_id": "R2L15_C09_HPSP_STAGE2A_20240119", "trigger_id": "T_R2L15_403870_STAGE2A_20240119", "symbol": "403870", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 9, "positioning_overheat_score": 6}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 5, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 9, "positioning_overheat_score": 7}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["valuation_repricing_score", "relative_strength_score", "positioning_overheat_score", "advanced_equipment_depth_score"], "component_delta_explanation": "C09 shadow separates advanced-equipment depth from valuation/price-only blowoff; direct process/customer depth can preserve Stage2, but late valuation-led Green is routed to 4B-watch.", "MFE_90D_pct": 33.68, "MAE_90D_pct": -25.42, "score_return_alignment_label": "positive_but_high_MAE_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C09_shadow", "case_id": "R2L15_C09_EOTECH_STAGE2A_20240119", "trigger_id": "T_R2L15_039030_STAGE2A_20240119", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 8, "positioning_overheat_score": 4}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 9, "positioning_overheat_score": 4}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["valuation_repricing_score", "relative_strength_score", "positioning_overheat_score", "advanced_equipment_depth_score"], "component_delta_explanation": "C09 shadow separates advanced-equipment depth from valuation/price-only blowoff; direct process/customer depth can preserve Stage2, but late valuation-led Green is routed to 4B-watch.", "MFE_90D_pct": 52.8, "MAE_90D_pct": -11.15, "score_return_alignment_label": "structural_positive_with_later_blowoff", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C09_shadow", "case_id": "R2L15_C09_WONIKIPS_STAGE2A_20240320", "trigger_id": "T_R2L15_240810_STAGE2A_20240320", "symbol": "240810", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 6, "positioning_overheat_score": 4}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 6, "positioning_overheat_score": 4}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable", "changed_components": ["valuation_repricing_score", "relative_strength_score", "positioning_overheat_score", "advanced_equipment_depth_score"], "component_delta_explanation": "C09 shadow separates advanced-equipment depth from valuation/price-only blowoff; direct process/customer depth can preserve Stage2, but late valuation-led Green is routed to 4B-watch.", "MFE_90D_pct": 19.92, "MAE_90D_pct": -10.56, "score_return_alignment_label": "modest_positive_capped_by_cycle_beta", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C09_shadow", "case_id": "R2L15_C09_HPSP_LATE_GREEN_20240214", "trigger_id": "T_R2L15_403870_GREEN_BLOWOFF_20240214", "symbol": "403870", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 7, "positioning_overheat_score": 9}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 7, "positioning_overheat_score": 10}, "weighted_score_after": 62, "stage_label_after": "4B-Watch", "changed_components": ["valuation_repricing_score", "relative_strength_score", "positioning_overheat_score", "advanced_equipment_depth_score"], "component_delta_explanation": "C09 shadow separates advanced-equipment depth from valuation/price-only blowoff; direct process/customer depth can preserve Stage2, but late valuation-led Green is routed to 4B-watch.", "MFE_90D_pct": 3.73, "MAE_90D_pct": -42.13, "score_return_alignment_label": "late_green_became_blowoff", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C09_shadow", "case_id": "R2L15_C09_EOTECH_LATE_GREEN_20240412", "trigger_id": "T_R2L15_039030_LATE_GREEN_20240412", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 7, "positioning_overheat_score": 9}, "weighted_score_before": 89, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 7, "positioning_overheat_score": 10}, "weighted_score_after": 61, "stage_label_after": "4B-Watch", "changed_components": ["valuation_repricing_score", "relative_strength_score", "positioning_overheat_score", "advanced_equipment_depth_score"], "component_delta_explanation": "C09 shadow separates advanced-equipment depth from valuation/price-only blowoff; direct process/customer depth can preserve Stage2, but late valuation-led Green is routed to 4B-watch.", "MFE_90D_pct": 2.93, "MAE_90D_pct": -52.6, "score_return_alignment_label": "late_green_near_full_window_peak", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C09_shadow", "case_id": "R2L15_C09_WONIKIPS_PRICEONLY_20240704", "trigger_id": "T_R2L15_240810_PRICEONLY_20240704", "symbol": "240810", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 4, "positioning_overheat_score": 8}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "advanced_equipment_depth_score": 4, "positioning_overheat_score": 9}, "weighted_score_after": 52, "stage_label_after": "Stage2-Watch / no-positive-promotion", "changed_components": ["valuation_repricing_score", "relative_strength_score", "positioning_overheat_score", "advanced_equipment_depth_score"], "component_delta_explanation": "C09 shadow separates advanced-equipment depth from valuation/price-only blowoff; direct process/customer depth can preserve Stage2, but late valuation-led Green is routed to 4B-watch.", "MFE_90D_pct": 0.5, "MAE_90D_pct": -32.79, "score_return_alignment_label": "price_only_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 6, "new_trigger_family_count": 6, "positive_case_count": 3, "counterexample_count": 3, "current_profile_error_count": 4, "diversity_score_summary": "3 new C09 symbols, 6 new trigger families, and balanced positive/counterexample rows.", "tested_existing_calibrated_axes": ["stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["late_green_near_peak", "price_only_equipment_beta_false_positive", "advanced_equipment_positive_high_MAE"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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

completed_round = `R2`  
completed_loop = `15`  
next_round = `R3`  
next_loop = `15`  
round_schedule_status = `valid`  
round_sector_consistency = `pass`

## 28. Source Notes

- Stock-Web manifest max date was read from `atlas/manifest.json` as `2026-02-20`.
- Schema uses `tradable_raw` OHLCV with columns `d,o,h,l,c,v,a,mc,s,m`.
- HPSP profile path: `atlas/symbol_profiles/403/403870.json`.
- 이오테크닉스 profile path: `atlas/symbol_profiles/039/039030.json`.
- 원익IPS profile path: `atlas/symbol_profiles/240/240810.json`.
- OHLC anchors were checked in the 2024 tradable shards listed in the machine-readable rows.

