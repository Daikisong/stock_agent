# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R4
scheduled_loop = 71
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = COPPER_RECORD_HIGH_POSITIONING_OVERHEAT_MARGIN_BRIDGE_SPLIT
loop_objective = counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R4_loop_71_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **3** new independent cases, **2** counterexamples, and **2** residual 4B-timing errors for **R4 / L4_MATERIALS_SPREAD_RESOURCE / C15_MATERIAL_SPREAD_SUPERCYCLE**.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
```

Existing applied axes are treated as already active: Stage2 actionable evidence bonus, Yellow/Green thresholds, price-only blowoff guard, full 4B non-price requirement, and hard 4C routing. This loop does not re-prove those general rules. It stress-tests whether **C15 copper/material spread spikes** need a narrower rule: macro positioning/speculative evidence may count as **4B-watch evidence**, but not as Stage2/Stage3 promotion evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = COPPER_RECORD_HIGH_POSITIONING_OVERHEAT_MARGIN_BRIDGE_SPLIT
```

R4 is mapped to L4 materials/spread/resource. The selected canonical archetype is C15 because the no-repeat coverage ledger leaves C15 `stage2_bonus_candidate_delta` in hold status, needing more non-overlapping positive/counterexample/transition evidence before promotion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot before this loop:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE = 10 rows / 7 symbols / 2020-08-10~2024-05-21
existing top covered symbols = 006260, 011170, 103140, 006650, 011780
hold/block = C15 stage2_bonus_candidate_delta hold_for_more_evidence
hard duplicate key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Duplicate handling:

- `103140` is reused only as a structural/high-MAE comparator and is not counted as a new independent case.
- `025820`, `012800`, and `021050` are treated as new C15 symbols for this loop.
- The new trigger family is not a repeated Stage2-positive promotion study; it is a **copper record high / positioning-overheat 4B-watch stress test**.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "source_basis": "FinanceData/marcap transformed into assistant-readable symbol-year CSV shards",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ]
}
```

Price-source validation status: `usable_for_historical_calibration`.

## 5. Historical Eligibility Gate

All representative and overlay rows use stock-web tradable shards. The 180 trading-day forward windows are available before the stock-web manifest max date of 2026-02-20. Symbol profile corporate-action dates do not overlap the 2024 entry-date through D+180 windows used here.

| symbol | company | profile_path | profile status | 2024 180D window |
|---|---|---|---|---|
| 103140 | 풍산 | atlas/symbol_profiles/103/103140.json | corporate_action_candidate_count=0 | clean_180D_window |
| 025820 | 이구산업 | atlas/symbol_profiles/025/025820.json | old corporate-action candidates only | clean_180D_window |
| 012800 | 대창 | atlas/symbol_profiles/012/012800.json | old corporate-action candidates only | clean_180D_window |
| 021050 | 서원 | atlas/symbol_profiles/021/021050.json | old corporate-action candidates only | clean_180D_window |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id candidates:
  - COPPER_MARGIN_BRIDGE_STRUCTURAL_COMPARATOR
  - COPPER_RECORD_HIGH_PRICE_ONLY_FALSE_PROMOTION
  - COPPER_RECORD_HIGH_POSITIONING_4B_OVERLAY
  - COPPER_RECORD_HIGH_POSITIONING_OVERHEAT_MARGIN_BRIDGE_SPLIT
```

Compression rule: all fine/deep variants remain inside C15. The canonical lesson is not “copper rose, buy copper beta.” The useful split is:

```text
C15 positive path:
  commodity upcycle + company-level margin bridge / supply discipline / FCF route

C15 counterexample path:
  commodity record price + stock relative strength only + no company-level margin bridge

C15 4B-watch path:
  commodity record high + speculative/positioning squeeze evidence + full-window peak proximity
```

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | is_new_independent_case | independent_evidence_weight | current_profile_verdict |
|---|---|---|---|---|---|---|---|
| CASE_R4L71_C15_103140_POONGSAN_STRUCTURAL_HIGH_MAE | 103140 | 풍산 | high_mae_success | positive | False | 0.25 | current_profile_correct |
| CASE_R4L71_C15_025820_IGUSANDUP_COPPER_PRICE_ONLY | 025820 | 이구산업 | false_positive_green | counterexample | True | 1.0 | current_profile_4B_too_late |
| CASE_R4L71_C15_012800_DAECHANG_COPPER_4B_OVERLAY | 012800 | 대창 | 4B_overlay_success | positive_and_counterexample | True | 1.0 | current_profile_4B_too_late |
| CASE_R4L71_C15_021050_SEOWON_COPPER_4B_OVERLAY | 021050 | 서원 | 4B_overlay_success | positive_and_counterexample | True | 1.0 | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count = 4
new_independent_case_count = 3
reused_case_count = 1
positive_case_count = 2
counterexample_count = 2
4B_case_count = 3
4C_case_count = 0
```

The balance is intentionally tilted toward counterexample and 4B timing, because C15 already had good Stage2 rows but lacked enough guardrail/transition evidence.

## 9. Evidence Source Map

| evidence family | used for | source note | scoring usage |
|---|---|---|---|
| Copper/data-center demand narrative | Stage2-watch context | 2024-05-10 broad copper demand narrative | not enough for Stage3 |
| Copper record high / speculative run / US shipment calming squeeze | 4B-watch context | 2024-05-20 Reuters-style macro positioning evidence | can support 4B-watch overlay |
| Company business exposure / margin bridge | structural comparator | public profile proxy for 103140 | needs IR/filing replacement before promotion |
| Stock-web OHLC | all MFE/MAE/peak/drawdown | tradable_raw shards | quantitative calibration |

## 10. Price Data Source Map

| symbol | shard | profile | entry rows used |
|---|---|---|---|
| 103140 | atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv | atlas/symbol_profiles/103/103140.json | 2024-04-26 |
| 025820 | atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv | atlas/symbol_profiles/025/025820.json | 2024-05-13, 2024-05-20 |
| 012800 | atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv | atlas/symbol_profiles/012/012800.json | 2024-05-13, 2024-05-20 |
| 021050 | atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv | atlas/symbol_profiles/021/021050.json | 2024-05-13, 2024-05-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | peak_date | peak_price | drawdown_after_peak_pct | current_profile_verdict | aggregate_group_role |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T103140_STAGE2_20240426 | 103140 | 풍산 | Stage2-Actionable | 2024-04-26 | 2024-04-26 | 62900 | 25.44 | -25.28 | 2024-05-14 | 78900 | -40.43 | current_profile_correct | representative |
| T025820_STAGE2_PRICEONLY_20240513 | 025820 | 이구산업 | Stage2-PriceOnlyWatch | 2024-05-10 | 2024-05-13 | 7110 | 18.42 | -46.62 | 2024-05-20 | 8420 | -55.82 | current_profile_correct | representative |
| T025820_4B_OVERLAY_20240520 | 025820 | 이구산업 | Stage4B-Overlay | 2024-05-20 | 2024-05-20 | 7880 | 6.85 | -51.84 | 2024-05-20 | 8420 | -55.82 | current_profile_4B_too_late | 4B_overlay_only |
| T012800_STAGE2_PRICEONLY_20240513 | 012800 | 대창 | Stage2-PriceOnlyWatch | 2024-05-10 | 2024-05-13 | 1602 | 44.82 | -31.34 | 2024-05-21 | 2320 | -53.02 | current_profile_correct | representative |
| T012800_4B_OVERLAY_20240520 | 012800 | 대창 | Stage4B-Overlay | 2024-05-20 | 2024-05-20 | 2080 | 11.54 | -47.12 | 2024-05-21 | 2320 | -53.02 | current_profile_4B_too_late | 4B_overlay_only |
| T021050_STAGE2_PRICEONLY_20240513 | 021050 | 서원 | Stage2-PriceOnlyWatch | 2024-05-10 | 2024-05-13 | 1396 | 43.62 | -23.07 | 2024-05-21 | 2005 | -47.63 | current_profile_correct | representative |
| T021050_4B_OVERLAY_20240520 | 021050 | 서원 | Stage4B-Overlay | 2024-05-20 | 2024-05-20 | 1916 | 4.65 | -43.95 | 2024-05-21 | 2005 | -47.63 | current_profile_4B_too_late | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T103140_STAGE2_20240426 | 62900 | 25.44 | -11.61 | 25.44 | -25.28 | 25.44 | -25.28 | 2024-05-14 | 78900 | -40.43 |
| T025820_STAGE2_PRICEONLY_20240513 | 7110 | 18.42 | -27.29 | 18.42 | -46.62 | 18.42 | -47.68 | 2024-05-20 | 8420 | -55.82 |
| T025820_4B_OVERLAY_20240520 | 7880 | 6.85 | -34.9 | 6.85 | -51.84 | 6.85 | -52.79 | 2024-05-20 | 8420 | -55.82 |
| T012800_STAGE2_PRICEONLY_20240513 | 1602 | 44.82 | -10.67 | 44.82 | -31.34 | 44.82 | -31.96 | 2024-05-21 | 2320 | -53.02 |
| T012800_4B_OVERLAY_20240520 | 2080 | 11.54 | -33.89 | 11.54 | -47.12 | 11.54 | -47.6 | 2024-05-21 | 2320 | -53.02 |
| T021050_STAGE2_PRICEONLY_20240513 | 1396 | 43.62 | -5.44 | 43.62 | -23.07 | 43.62 | -24.79 | 2024-05-21 | 2005 | -47.63 |
| T021050_4B_OVERLAY_20240520 | 1916 | 4.65 | -31.11 | 4.65 | -43.95 | 4.65 | -45.2 | 2024-05-21 | 2005 | -47.63 |


## 13. Current Calibrated Profile Stress Test

1. Current calibrated profile should block price-only copper beta from Stage3/Green. That was correct for `025820`, `012800`, and `021050` representative Stage2-watch rows.
2. The residual issue is 4B timing: if the model requires only company-level non-price evidence for full 4B, it may miss a C15-specific macro non-price risk signal: record commodity price plus speculative/short-covering positioning evidence.
3. The Stage2 bonus is **not** weakened globally. It is kept but should remain bridge-dependent in C15.
4. Yellow 75 and Green 87/55 are kept. No Green relaxation is proposed.
5. Price-only blowoff guard is strengthened.
6. Full 4B non-price requirement is kept, but C15 should allow `positioning_overheat` as a valid non-price 4B-watch evidence family when the commodity itself is in a record/speculative squeeze.

```text
existing_axis_tested = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened = null
new_axis_proposed = C15_positioning_overheat_counts_as_4B_watch_evidence_not_stage3_promotion
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is assigned in this loop. Stage2-watch rows had large short-term MFE in two small copper processors, but the same windows also produced severe 90D/180D MAE and post-peak drawdowns. Therefore:

```text
Stage2-watch = allowed as monitoring label
Stage2-Actionable = requires company-level margin bridge / spread capture / FCF route
Stage3-Yellow = not assigned from commodity price alone
Stage3-Green = not assigned
Green lateness audit = not_applicable
```

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | symbol | Stage2 entry | 4B entry | peak | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| T025820_4B_OVERLAY_20240520 | 025820 | 7110 | 7880 | 8420 | 0.59 | 0.59 | good_local_4B_watch_but_not_full_stage_promotion |
| T012800_4B_OVERLAY_20240520 | 012800 | 1602 | 2080 | 2320 | 0.67 | 0.67 | good_full_window_4B_timing |
| T021050_4B_OVERLAY_20240520 | 021050 | 1396 | 1916 | 2005 | 0.85 | 0.85 | good_full_window_4B_timing |

Interpretation: C15 small-cap copper beta can have strong Stage2-watch MFE, but the useful residual signal is not early positive promotion. It is near-peak risk recognition when macro-positioning evidence appears.

## 16. 4C Protection Audit

No hard 4C row is assigned. The post-peak drawdown was large, but the evidence available at the May 2024 peak was better categorized as 4B-watch / thesis-break watch, not a confirmed 4C thesis break.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_confirmation = not_proposed
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
rule = Commodity record-price + broad thematic demand narrative should not raise Stage2/Stage3 without company-level spread capture evidence.
backtest_effect = reduces false positive Green/Yellow promotion risk in high-MAE copper beta cases.
confidence = medium_low
production_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
rule = C15 can count macro positioning/speculative squeeze evidence as valid 4B-watch evidence, but not as Stage2/Stage3 promotion evidence.
changed_axis = C15_positioning_overheat_4B_watch_guard
existing_axis_strengthened = full_4b_requires_non_price_evidence
new_axis_proposed = C15_positioning_overheat_counts_as_4B_watch_evidence_not_stage3_promotion
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg_MFE_90D | avg_MAE_90D | false_positive_rate | late_4B_count | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 4 representative | 33.08 | -31.58 | low if price-only guard works | 2 | broadly correct but 4B timing under-specified |
| P0b e2r_2_0_baseline_reference | rollback | 4 representative | 33.08 | -31.58 | high | 3 | too permissive for price-only commodity beta |
| P1 L4 sector shadow | sector | 4 representative + 3 overlay | 23.42 | -37.03 | lower | 1 | keeps Stage2 watch, adds 4B watch |
| P2 C15 canonical shadow | canonical | 4 representative + 3 overlay | 23.42 | -37.03 | lower | 0 | best explanatory fit |
| P3 counterexample guard | guard | 3 price-only symbols | 35.62 | -33.68 | lowest | 0 | blocks false Green, preserves monitoring |

## 20. Score-Return Alignment Matrix

| case | current score-return alignment | residual lesson |
|---|---|---|
| 103140 | positive but high-MAE | structural C15 names still need margin bridge; Green not relaxed |
| 025820 | price-only MFE followed by large MAE | Stage2/Green promotion blocked; 4B watch needed near record price |
| 012800 | strong MFE but 4B timing mattered | macro positioning evidence improved peak-risk recognition |
| 021050 | strong MFE but 4B timing mattered | full-window 4B proximity was strong when using 2024-05-20 evidence |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_RECORD_HIGH_POSITIONING_OVERHEAT_MARGIN_BRIDGE_SPLIT | 2 | 2 | 3 | 0 | 3 | 1 | 7 | 4 | 2 | true | true | C15 still needs more verified company-level positive cases and hard 4C examples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: CASE_R4L71_C15_103140_POONGSAN_STRUCTURAL_HIGH_MAE
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 2
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: C15_macro_positioning_overheat_not_explicit_as_4B_watch_evidence; price_only_copper_beta_false_green_risk
new_axis_proposed: C15_positioning_overheat_counts_as_4B_watch_evidence_not_stage3_promotion
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Stock-web OHLC entry, MFE, MAE, peak, and drawdown for 103140, 025820, 012800, and 021050.
- Corporate-action contamination screen using stock-web symbol profiles.
- C15 duplicate/coverage context using No-Repeat Index snapshot.

Non-validation scope:

- No live/current recommendation.
- No production scoring patch.
- No stock_agent code access or implementation.
- Company-level source replacement for 103140 remains a later data-quality task before promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C15_positioning_overheat_4B_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,macro_positioning_not_explicit,positioning_overheat_counts_as_4B_watch_not_stage3,+guard,Reuters-style speculative copper record evidence improved 4B timing without promoting Green,lowered post-peak MAE exposure in 012800/021050 overlay audit,T025820_4B_OVERLAY_20240520|T012800_4B_OVERLAY_20240520|T021050_4B_OVERLAY_20240520,7,3,2,medium_low,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"case_id":"CASE_R4L71_C15_103140_POONGSAN_STRUCTURAL_HIGH_MAE","symbol":"103140","company_name":"풍산","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_MARGIN_BRIDGE_STRUCTURAL_COMPARATOR","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T103140_STAGE2_20240426","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"C15 top-covered symbol reused only as structural comparator / high-MAE success anchor; not counted as new independent case.","independent_evidence_weight":0.25,"score_price_alignment":"positive MFE but high MAE; company-level margin bridge is needed before any Green relaxation.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Clean stock-web 180D window; corporate-action candidate count is zero in symbol profile.","row_type":"case"}
{"case_id":"CASE_R4L71_C15_025820_IGUSANDUP_COPPER_PRICE_ONLY","symbol":"025820","company_name":"이구산업","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_PRICE_ONLY_FALSE_PROMOTION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T025820_STAGE2_PRICEONLY_20240513","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Large MFE existed, but 90D/180D MAE and post-peak drawdown show price-only copper beta should not promote Stage3.","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"New C15 symbol in no-repeat index context; used as counterexample and 4B timing stress case.","row_type":"case"}
{"case_id":"CASE_R4L71_C15_012800_DAECHANG_COPPER_4B_OVERLAY","symbol":"012800","company_name":"대창","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_POSITIONING_4B_OVERLAY","case_type":"4B_overlay_success","positive_or_counterexample":"positive_and_counterexample","best_trigger":"T012800_4B_OVERLAY_20240520","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2-watch had high MFE, but Reuters-style speculative copper record evidence near peak improved 4B timing.","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"New C15 symbol; 4B overlay row is not positive Stage promotion evidence.","row_type":"case"}
{"case_id":"CASE_R4L71_C15_021050_SEOWON_COPPER_4B_OVERLAY","symbol":"021050","company_name":"서원","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_POSITIONING_4B_OVERLAY","case_type":"4B_overlay_success","positive_or_counterexample":"positive_and_counterexample","best_trigger":"T021050_4B_OVERLAY_20240520","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2-watch captured upside; 4B overlay near copper record peak reduced later drawdown exposure in audit terms.","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"New C15 symbol; used to refine macro-positioning evidence as 4B-watch, not Green promotion.","row_type":"case"}
{"row_type":"trigger","trigger_id":"T103140_STAGE2_20240426","case_id":"CASE_R4L71_C15_103140_POONGSAN_STRUCTURAL_HIGH_MAE","symbol":"103140","company_name":"풍산","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_MARGIN_BRIDGE_STRUCTURAL_COMPARATOR","sector":"materials_copper_defense","primary_archetype":"copper_margin_bridge","loop_objective":"holdout_validation|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":62900,"evidence_available_at_that_date":"Company business exposure to copper/alloy materials plus visible copper price upcycle; used as structural comparator, not new independent evidence.","evidence_source":"Public company/business profile proxy + stock-web price path; replace with IR/filing URL before promotion.","stage2_evidence_fields":["capacity_or_volume_route","relative_strength","margin_bridge_watch"],"stage3_evidence_fields":["margin_bridge_watch","financial_visibility_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","profile_path":"atlas/symbol_profiles/103/103140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.44,"MFE_90D_pct":25.44,"MFE_180D_pct":25.44,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.61,"MAE_90D_pct":-25.28,"MAE_180D_pct":-25.28,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":78900,"drawdown_after_peak_pct":-40.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G103140_20240426_62900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"Covered C15 symbol reused as comparator only.","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T025820_STAGE2_PRICEONLY_20240513","case_id":"CASE_R4L71_C15_025820_IGUSANDUP_COPPER_PRICE_ONLY","symbol":"025820","company_name":"이구산업","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_PRICE_ONLY_FALSE_PROMOTION","sector":"materials_copper_processor","primary_archetype":"copper_beta_price_only","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-PriceOnlyWatch","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":7110,"evidence_available_at_that_date":"Copper price narrative around AI/data-center demand and broad copper rally; no company-level margin bridge at trigger.","evidence_source":"Investopedia 2024-05-10 copper/data-center narrative + stock-web OHLC; company-level bridge absent.","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv","profile_path":"atlas/symbol_profiles/025/025820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.42,"MFE_90D_pct":18.42,"MFE_180D_pct":18.42,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.29,"MAE_90D_pct":-46.62,"MAE_180D_pct":-47.68,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-20","peak_price":8420,"drawdown_after_peak_pct":-55.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_stage2_should_not_promote","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_false_promotion","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G025820_20240513_7110","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T025820_4B_OVERLAY_20240520","case_id":"CASE_R4L71_C15_025820_IGUSANDUP_COPPER_PRICE_ONLY","symbol":"025820","company_name":"이구산업","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_POSITIONING_4B_OVERLAY","sector":"materials_copper_processor","primary_archetype":"copper_positioning_overheat","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":7880,"evidence_available_at_that_date":"Reuters reported copper record run and speculative/short-covering risk around 2024-05-20; evidence supports 4B-watch, not Stage3 promotion.","evidence_source":"Reuters 2024-05-20 copper record / US shipments / speculator frenzy article + stock-web OHLC.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv","profile_path":"atlas/symbol_profiles/025/025820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.85,"MFE_90D_pct":6.85,"MFE_180D_pct":6.85,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-34.9,"MAE_90D_pct":-51.84,"MAE_180D_pct":-52.79,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-20","peak_price":8420,"drawdown_after_peak_pct":-55.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.59,"four_b_full_window_peak_proximity":0.59,"four_b_timing_verdict":"good_local_4B_watch_but_not_full_stage_promotion","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_watch_after_speculative_copper_peak","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G025820_20240520_7880","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T012800_STAGE2_PRICEONLY_20240513","case_id":"CASE_R4L71_C15_012800_DAECHANG_COPPER_4B_OVERLAY","symbol":"012800","company_name":"대창","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_PRICE_ONLY_FALSE_PROMOTION","sector":"materials_copper_processor","primary_archetype":"copper_beta_price_only","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-PriceOnlyWatch","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":1602,"evidence_available_at_that_date":"Broad copper/data-center demand narrative and relative strength; no company-specific margin conversion evidence at trigger.","evidence_source":"Investopedia 2024-05-10 copper/data-center narrative + stock-web OHLC.","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv","profile_path":"atlas/symbol_profiles/012/012800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":44.82,"MFE_90D_pct":44.82,"MFE_180D_pct":44.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.67,"MAE_90D_pct":-31.34,"MAE_180D_pct":-31.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":2320,"drawdown_after_peak_pct":-53.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_stage2_should_not_promote","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mfe_but_false_green_without_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G012800_20240513_1602","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T012800_4B_OVERLAY_20240520","case_id":"CASE_R4L71_C15_012800_DAECHANG_COPPER_4B_OVERLAY","symbol":"012800","company_name":"대창","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_POSITIONING_4B_OVERLAY","sector":"materials_copper_processor","primary_archetype":"copper_positioning_overheat","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":2080,"evidence_available_at_that_date":"Copper record-high / speculative run evidence available near local/full price peak.","evidence_source":"Reuters 2024-05-20 copper record / US shipments / speculator frenzy article + stock-web OHLC.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv","profile_path":"atlas/symbol_profiles/012/012800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.54,"MFE_90D_pct":11.54,"MFE_180D_pct":11.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-33.89,"MAE_90D_pct":-47.12,"MAE_180D_pct":-47.6,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":2320,"drawdown_after_peak_pct":-53.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.67,"four_b_full_window_peak_proximity":0.67,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G012800_20240520_2080","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T021050_STAGE2_PRICEONLY_20240513","case_id":"CASE_R4L71_C15_021050_SEOWON_COPPER_4B_OVERLAY","symbol":"021050","company_name":"서원","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_PRICE_ONLY_FALSE_PROMOTION","sector":"materials_copper_processor","primary_archetype":"copper_beta_price_only","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-PriceOnlyWatch","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":1396,"evidence_available_at_that_date":"Broad copper/data-center demand narrative and relative strength; no company-specific durable margin bridge.","evidence_source":"Investopedia 2024-05-10 copper/data-center narrative + stock-web OHLC.","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv","profile_path":"atlas/symbol_profiles/021/021050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":43.62,"MFE_90D_pct":43.62,"MFE_180D_pct":43.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.44,"MAE_90D_pct":-23.07,"MAE_180D_pct":-24.79,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":2005,"drawdown_after_peak_pct":-47.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_stage2_should_not_promote","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mfe_but_false_green_without_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G021050_20240513_1396","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T021050_4B_OVERLAY_20240520","case_id":"CASE_R4L71_C15_021050_SEOWON_COPPER_4B_OVERLAY","symbol":"021050","company_name":"서원","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_RECORD_HIGH_POSITIONING_4B_OVERLAY","sector":"materials_copper_processor","primary_archetype":"copper_positioning_overheat","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":1916,"evidence_available_at_that_date":"Copper record-high / speculative run evidence available near local/full price peak.","evidence_source":"Reuters 2024-05-20 copper record / US shipments / speculator frenzy article + stock-web OHLC.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv","profile_path":"atlas/symbol_profiles/021/021050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.65,"MFE_90D_pct":4.65,"MFE_180D_pct":4.65,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-31.11,"MAE_90D_pct":-43.95,"MAE_180D_pct":-45.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":2005,"drawdown_after_peak_pct":-47.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.85,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G021050_20240520_1916","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R4L71_C15_103140_POONGSAN_STRUCTURAL_HIGH_MAE","trigger_id":"T103140_STAGE2_20240426","symbol":"103140","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":0,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":0,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable-high-MAE-guard","changed_components":["margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C15 structural comparator keeps Stage2 but does not loosen Green without margin/FCF confirmation.","MFE_90D_pct":25.44,"MAE_90D_pct":-25.28,"score_return_alignment_label":"mixed_positive_high_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"CASE_R4L71_C15_025820_IGUSANDUP_COPPER_PRICE_ONLY","trigger_id":"T025820_STAGE2_PRICEONLY_20240513","symbol":"025820","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":6,"execution_risk_score":24,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-Watch-price-only-blocked","changed_components":["relative_strength_score","execution_risk_score"],"component_delta_explanation":"Copper beta price action is not enough for Stage2 promotion without margin bridge; 4B watch is preferred near record/positioning evidence.","MFE_90D_pct":18.42,"MAE_90D_pct":-46.62,"score_return_alignment_label":"false_promotion_risk","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C15_positioning_overheat_4B_watch_shadow","case_id":"CASE_R4L71_C15_012800_DAECHANG_COPPER_4B_OVERLAY","trigger_id":"T012800_4B_OVERLAY_20240520","symbol":"012800","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":13,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"4B-Watch-overlay-not-Green","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Reuters-style macro positioning evidence counts as 4B-watch evidence in C15 but not Stage3 evidence.","MFE_90D_pct":11.54,"MAE_90D_pct":-47.12,"score_return_alignment_label":"4B_overlay_improves_risk_timing","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C15_positioning_overheat_4B_watch_shadow","case_id":"CASE_R4L71_C15_021050_SEOWON_COPPER_4B_OVERLAY","trigger_id":"T021050_4B_OVERLAY_20240520","symbol":"021050","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":17,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":12,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"4B-Watch-overlay-not-Green","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Full-window proximity near 0.85 after Reuters copper record evidence supports 4B watch.","MFE_90D_pct":4.65,"MAE_90D_pct":-43.95,"score_return_alignment_label":"4B_overlay_improves_risk_timing","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":3,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C15_macro_positioning_overheat_not_explicit_as_4B_watch_evidence","price_only_copper_beta_false_green_risk"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R4
completed_loop = 71
next_round = R5
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest: `Songdaiki/stock-web/atlas/manifest.json`; manifest max date used here is `2026-02-20`.
- Stock-Web tradable shards used: `103/103140/2024.csv`, `025/025820/2024.csv`, `012/012800/2024.csv`, `021/021050/2024.csv`.
- Stock-Web symbol profiles used: `103140`, `025820`, `012800`, `021050`.
- External evidence mapped for historical event context only: 2024-05-10 copper/data-center demand narrative and 2024-05-20 copper record/speculative-run/US shipment risk narrative.
- This document is not an investment recommendation and does not generate live candidates.

