# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R2_loop_10_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
scheduled_round = R2
scheduled_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE
loop_objective = coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
stock_web_price_atlas_access_required = true
```

This loop follows the prior next-state handoff from R1 Loop 10: `next_round = R2`, `next_loop = 10`. It does not scan current/live candidates. It is historical calibration research only.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove those global axes. It asks whether C08 needs a narrower canonical-archetype rule: generic test-socket/HBM theme exposure should not equal qualified customer-quality evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R2
loop = 10
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE
sector = AI·반도체·전자부품
```

R2 is the AI / semiconductor / electronics round. C08 is selected because this specific test-socket/customer-quality archetype needs separation from C06 HBM memory, C07 HBM equipment/order strength, and C09 advanced-equipment valuation blowoff.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact check:

- `reports/e2r_calibration/by_round/R2.md` reports `representative_triggers = 155` and `unique_cases = 40`, but the round summary does not isolate C08-specific positive/counterexample balance.
- The previous generated v12 state in this session completed `R1 / Loop 10`, so this run must use `R2 / Loop 10`.
- Same canonical archetype repetition is allowed; repeated symbol + trigger_date + entry_date is not. This loop uses four symbols and one reused symbol only for a different 4B trigger family.

Duplicate policy:

```text
new_symbol_count = 4
reused_case_count = 1
same_symbol_same_trigger_date_research = avoided
same_symbol_new_trigger_family = allowed for ISC 4B timing audit
minimum_new_independent_case_ratio = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest and schema fields used:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Tradable rows use `d,o,h,l,c,v,a,mc,s,m`. Raw rows additionally include `rs = row_status`. This research uses tradable shards for calibration and only reads profile caveats for corporate-action contamination.

## 5. Historical Eligibility Gate

All representative rows in this MD satisfy:

```text
entry row exists = true
forward_180D_available_by_manifest_max_date = true
MFE_30D/90D/180D computed = true
MAE_30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

Corporate-action notes:

- `058470` has a future profile corporate-action candidate in 2025, outside the selected 2024 180D window.
- `095340` has profile candidate dates in 2014 and 2023; selected 2024 windows are clean for 180D calibration.
- `098120` corporate-action profile dates are 2011, outside selected windows.
- `425420` has no corporate-action candidate dates in profile.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| IC_TEST_SOCKET_CUSTOMER_QUALITY | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Customer qualification and recurring socket demand matter more than generic semiconductor theme. |
| HBM_TEST_SOCKET_PROXY | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | HBM linkage is useful only if customer-quality and revision/margin bridge are present. |
| TEST_INTERFACE_SMALL_SUPPLIER_THEME | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Small-cap test-interface names require stronger guardrails against theme-only Stage2 promotion. |
| PRICE_ONLY_SOCKET_LOCAL_PEAK | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 4B watch-only overlay unless non-price deterioration appears. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | entry_date | entry_price | MFE90 | MAE90 | current_profile_verdict |
|---|---|---|---|---|---|---|---|---|---|
| R2L10_C08_RINO_20240103_STAGE2 | 058470 | 리노공업 | structural_success | positive | 2024-01-03 | 214000 | 44.39 | -12.2 | current_profile_too_late |
| R2L10_C08_ISC_20240103_STAGE2 | 095340 | ISC | high_mae_success | positive | 2024-01-03 | 79400 | 36.02 | -13.73 | current_profile_correct |
| R2L10_C08_MICROCONTACT_20240103_STAGE2 | 098120 | 마이크로컨텍솔 | failed_rerating | counterexample | 2024-01-03 | 14400 | 3.13 | -38.54 | current_profile_false_positive |
| R2L10_C08_TFE_20240103_STAGE2 | 425420 | 티에프이 | failed_rerating | counterexample | 2024-01-03 | 36800 | 19.16 | -22.96 | current_profile_false_positive |
| R2L10_C08_ISC_20240328_4B_LOCAL | 095340 | ISC | 4B_overlay_success | counterexample | 2024-03-28 | 99400 | 0.6 | -51.66 | current_profile_correct |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
calibration_usable_case_count = 5
new_independent_case_count = 4
reused_case_count = 1
```

The loop deliberately pairs two qualified C08 examples with two weak/generic test-socket counterexamples. This avoids the common false comfort of treating every socket/test-interface name as a miniature HBM-equipment winner.

## 9. Evidence Source Map

| evidence family | used for Stage2/3? | used for 4B/4C? | note |
|---|---:|---:|---|
| customer_quality_proxy | yes | no | Required for qualified C08 Stage2-Actionable. |
| relative_strength | yes | watch only | Cannot by itself promote Stage2/3. |
| margin_or_revision_bridge | yes | yes if slowdown appears | Missing bridge downgrades weak names to watch/reject. |
| price_only_local_peak | no | 4B watch only | Cannot create full 4B without non-price evidence. |
| stock-web OHLC | validation only | validation only | Not used as standalone positive evidence. |

## 10. Price Data Source Map

| symbol | company | profile_path | price_shard_path | profile caveat |
|---|---|---|---|---|
| 058470 | 리노공업 | atlas/symbol_profiles/058/058470.json | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | corporate-action candidate exists in 2025; selected 2024 180D window clean |
| 095340 | ISC | atlas/symbol_profiles/095/095340.json | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | 2023 corporate-action candidate outside selected 2024 window |
| 098120 | 마이크로컨텍솔 | atlas/symbol_profiles/098/098120.json | atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv | old 2011 candidates outside window |
| 425420 | 티에프이 | atlas/symbol_profiles/425/425420.json | atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv | no candidate dates |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | current_profile_verdict | aggregate_role |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R2L10_C08_RINO_T1 | 058470 | Stage2-Actionable | 2024-01-03 | 214000 | 11.45 | 44.39 | 44.39 | -12.2 | -12.2 | -23.36 | current_profile_too_late | representative |
| R2L10_C08_ISC_T1 | 095340 | Stage2-Actionable | 2024-01-03 | 79400 | 14.11 | 36.02 | 36.02 | -13.73 | -13.73 | -39.48 | current_profile_correct | representative |
| R2L10_C08_MICROCONTACT_T1 | 098120 | Stage2-Actionable_candidate_rejected | 2024-01-03 | 14400 | 3.13 | 3.13 | 3.13 | -29.65 | -38.54 | -61.74 | current_profile_false_positive | representative |
| R2L10_C08_TFE_T1 | 425420 | Stage2-Actionable_candidate_rejected | 2024-01-03 | 36800 | 0.95 | 19.16 | 19.16 | -22.96 | -22.96 | -55.11 | current_profile_false_positive | representative |
| R2L10_C08_ISC_T4B | 095340 | Stage4B-local-watch | 2024-03-28 | 99400 | 0.6 | 0.6 | 0.6 | -16.5 | -51.66 | -51.66 | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

Interpretation:

- RINO and ISC validate qualified C08 Stage2-Actionable: customer-quality proxy + early relative strength can work before full Green evidence.
- Microcontact and TFE reject generic socket theme promotion: weak evidence had low MFE and severe MAE.
- ISC 4B overlay validates price-only peak as watch-only risk row, not full 4B production logic.

| group | representative triggers | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | verdict |
|---|---:|---:|---:|---:|---:|---|
| qualified C08 positives | 2 | 40.21 | -12.97 | 40.21 | -31.42 | Stage2-Actionable allowed; Green still strict |
| generic C08 counterexamples | 2 | 11.15 | -30.75 | 11.15 | -58.43 | Stage2 candidate should be rejected or watch-only |
| price-only C08 4B overlay | 1 | 0.60 | -51.66 | 0.60 | -51.66 | risk watch useful, full 4B requires non-price evidence |

## 13. Current Calibrated Profile Stress Test

1. Current profile likely catches some C08 cases through general R2 evidence, but it lacks a clean C08 bridge between generic test-socket theme and qualified customer-quality evidence.
2. The positive rows support early Stage2-Actionable but not immediate Green.
3. Stage2 bonus is useful for RINO/ISC but too generous for Microcontact/TFE unless guarded.
4. Yellow threshold 75 is acceptable only when customer quality and revision/margin bridge are present.
5. Green threshold 87 / revision 55 should be kept; C08 has violent drawdown risk even in winners.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate; ISC 4B row is watch-only.
8. Hard 4C routing is not the main issue here; earlier thesis-break watch is enough for generic failed cases.

Verdicts:

```text
RINO = current_profile_too_late
ISC Stage2 = current_profile_correct
Microcontact = current_profile_false_positive
TFE = current_profile_false_positive
ISC 4B = current_profile_correct
```

## 14. Stage2 / Yellow / Green Comparison

C08 should behave like a quality filter, not a theme filter.

```text
Stage2-Actionable allowed when:
- customer_quality_score >= 65
- relative_strength_score >= 60
- margin_bridge_score or revision_score is at least partially supported
- execution_risk_score is not high

Stage3-Yellow allowed when:
- Stage2 criteria pass
- at least one explicit revision/margin/customer confirmation appears

Stage3-Green allowed only when:
- revision_score >= 55 equivalent
- margin_bridge_score >= 60 equivalent
- customer quality is confirmed by durable demand, not just theme naming
```

Green lateness ratio is not numerically assigned because no representative confirmed C08 Green trigger was selected. The qualitative result is `not_applicable: no_confirmed_Stage3_Green_trigger`.

## 15. 4B Local vs Full-window Timing Audit

ISC 2024-03-28 local peak row:

```text
entry_price = 99,400
local_peak_price = 108,000
full_observed_180D_peak_price = 108,000
four_b_local_peak_proximity = 1.0
four_b_full_window_peak_proximity = 1.0
four_b_evidence_type = price_only|valuation_blowoff|positioning_overheat
four_b_timing_verdict = price_only_local_4B_watch_not_full_4B
```

The row protected against a large subsequent drawdown, but it does not weaken the non-price 4B requirement. It strengthens the distinction between risk watch and full 4B.

## 16. 4C Protection Audit

Hard 4C is not proposed. For Microcontact and TFE, the correct treatment is `thesis_break_watch_only` or `Stage1/watch rejection`, not hard 4C.

| case | label | reason |
|---|---|---|
| R2L10_C08_MICROCONTACT_20240103_STAGE2 | thesis_break_watch_only | Theme evidence failed to convert into price strength; no hard accounting/contract break used. |
| R2L10_C08_TFE_20240103_STAGE2 | thesis_break_watch_only | High MAE and low MFE argue for early rejection, not automatic 4C. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
rule_candidate = generic_semiconductor_theme_is_not_enough_for_C08_stage2_actionable
```

Within R2, C08 needs a different evidence gate from C06/C07/C09. The semi-test-socket route is closer to quality/customer qualification than to pure order-backlog or advanced-equipment scarcity.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
candidate_rule = require_customer_quality_plus_revision_or_margin_bridge
```

Proposed shadow condition:

```text
if canonical_archetype_id == C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY:
    Stage2_Actionable requires:
        customer_quality_score >= 65
        AND relative_strength_score >= 60
        AND (revision_score >= 45 OR margin_bridge_score >= 45)
    generic theme/price-only socket exposure routes to Stage1/watch
    Green remains strict; no relaxation of stage3_green_total_min or revision_min
```

## 19. Before / After Backtest Comparison

| profile_key | profile_id | scope | changed_axes | eligible_triggers | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | late_green | alignment |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current proxy | no C08-specific bridge | 4 | 25.68 | -22.86 | 25.68 | -44.92 | 50% | 0 | 0 | mixed; too permissive for weak C08, too late for strong C08 |
| P0b | e2r_2_0_baseline_reference | rollback reference | no post-calibrated guards | 4 | 25.68 | -22.86 | 25.68 | -44.92 | 50%+ | 1 | 0 | worse; generic semiconductor enthusiasm over-promotes weak cases |
| P1 | L2_sector_specific_candidate_profile | sector-specific | +customer_quality bridge; +generic theme block | 4 | 40.21 | -12.97 | 40.21 | -31.42 | 0% on selected entries | 0 | 0 | better positive/counterexample separation |
| P2 | C08_canonical_archetype_candidate_profile | canonical-specific | require customer_quality + revision/margin bridge | 4 | 40.21 | -12.97 | 40.21 | -31.42 | 0% on qualified C08 | 0 | 0 | best scope for this loop |
| P3 | C08_counterexample_guard_profile | counterexample guard | block generic socket theme; 4B price-only watch | 3 | 0.6 | -37.72 | 0.6 | -56.17 | watch-only | 0 | 0 | risk overlay; not positive calibration |

## 20. Score-Return Alignment Matrix

| case | P0 behavior | proposed C08 behavior | return alignment |
|---|---|---|---|
| RINO | may wait for broader confirmation | Stage2-Actionable with Green still strict | improves early recognition |
| ISC Stage2 | Stage2/Yellow acceptable | keep Stage2; avoid Green | preserves upside while respecting drawdown |
| Microcontact | vulnerable to false Stage2 if generic theme counts | reject to watch | prevents deep MAE |
| TFE | vulnerable to false Stage2 if generic theme counts | reject to watch | prevents low-MFE/high-MAE entry |
| ISC 4B | price-only watch acceptable | watch-only, not full 4B | preserves global 4B guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE | 2 | 2 | 1 | 0 | 4 | 1 | 5 | 4 | 3 | True | True | C08 no longer blank; still needs source-url hardening and more non-KOSDAQ-large holdout rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: R2L10_C08_ISC_20240328_4B_LOCAL
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_false_positive, current_profile_too_late, price_only_4B_watch_not_full_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_actionable_evidence_bonus scoped by C08 customer-quality bridge; full_4b_requires_non_price_evidence kept and C08 price-only watch clarified
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest/schema basis.
- Tradable OHLC rows for selected symbols and years.
- 30D/90D/180D MFE/MAE path labels.
- Corporate-action profile windows for selected symbols.
- C08-specific positive/counterexample split.

Not validated:

- This MD does not claim current/live candidate validity.
- This MD does not patch `stock_agent`.
- This MD does not promote production weights.
- Company-specific source URLs are marked for future hardening before any promotion batch.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_required_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,false,true,+1,"C08 should not inherit HBM equipment or generic semiconductor theme credit unless customer-quality plus margin/revision bridge exists","Positive rows with customer-quality proxies had usable 90D MFE; weak generic socket rows had poor MFE and severe MAE","R2L10_C08_RINO_T1|R2L10_C08_ISC_T1|R2L10_C08_MICROCONTACT_T1|R2L10_C08_TFE_T1",4,4,2,medium,canonical_shadow_only,"not production; company-specific source URL hardening required"
shadow_weight,C08_generic_socket_theme_stage2_block,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,false,true,+1,"Generic test-socket theme participation without quality/revision proof should be Stage1/watch rather than Stage2-Actionable","Two counterexamples generated MFE90 below 20% with MAE90 worse than -20%","R2L10_C08_MICROCONTACT_T1|R2L10_C08_TFE_T1",2,2,2,medium,canonical_shadow_only,"strengthens guardrail against price/theme-only promotion"
shadow_weight,C08_price_only_4B_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,false,true,+1,"Price-only local peak is useful as 4B watch, but full 4B needs non-price evidence such as revision slowdown or customer/order deterioration","ISC 2024 local peak protected drawdown, but row remains overlay-only because evidence type was price-only","R2L10_C08_ISC_T4B",1,0,1,low_medium,canonical_shadow_only,"do not weaken full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

### price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type":"case","case_id":"R2L10_C08_RINO_20240103_STAGE2","symbol":"058470","company_name":"리노공업","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L10_C08_RINO_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_asymmetry","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"RINO behaved like a high-quality C08 winner: the 90D upside was strong while the later 180D drawdown warns against jumping directly to Green without revision/margin confirmation."}
{"row_type":"case","case_id":"R2L10_C08_ISC_20240103_STAGE2","symbol":"095340","company_name":"ISC","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L10_C08_ISC_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_asymmetry","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"ISC supports Stage2-Actionable, not automatic Green: it produced a valid 90D MFE but suffered a large 180D drawdown after a local peak."}
{"row_type":"case","case_id":"R2L10_C08_MICROCONTACT_20240103_STAGE2","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R2L10_C08_MICROCONTACT_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_counterexample_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"This is the cleanest C08 counterexample: the same test-socket label without customer-quality/margin evidence did not produce even a 20% 90D MFE and created deep MAE."}
{"row_type":"case","case_id":"R2L10_C08_TFE_20240103_STAGE2","symbol":"425420","company_name":"티에프이","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R2L10_C08_TFE_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_counterexample_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"TFE shows why C08 should not inherit HBM equipment weights mechanically. Theme exposure without customer-quality evidence had poor score-return alignment."}
{"row_type":"case","case_id":"R2L10_C08_ISC_20240328_4B_LOCAL","symbol":"095340","company_name":"ISC","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R2L10_C08_ISC_T4B","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_4B_timing_audit","independent_evidence_weight":0.5,"score_price_alignment":"risk_overlay_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"This validates a C08 4B watch overlay: local peak proximity was high and subsequent 90D MAE was severe, but the row remains overlay-only because evidence was price-only."}
```

### trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R2L10_C08_RINO_T1","case_id":"R2L10_C08_RINO_20240103_STAGE2","symbol":"058470","company_name":"리노공업","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","evidence_available_at_that_date":"2024 opening-year C08 proxy: high-quality IC test socket/probe exposure, durable customer quality, sector AI/HBM demand, and early relative strength; company-specific Green revision still incomplete.","evidence_source":"historical public research-report/news proxy; stock-web OHLC validation; company-specific source URL hardening pending before promotion","stage2_evidence_fields":["relative_strength","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-03","entry_price":214000,"MFE_30D_pct":11.45,"MFE_90D_pct":44.39,"MFE_180D_pct":44.39,"MFE_1Y_pct":44.39,"MFE_2Y_pct":null,"MAE_30D_pct":-12.2,"MAE_90D_pct":-12.2,"MAE_180D_pct":-23.36,"MAE_1Y_pct":-23.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-46.93,"green_lateness_ratio":"not_applicable: no confirmed C08 Stage3-Green trigger used as representative","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L10_C08_RINO_20240103_STAGE2::2024-01-03::214000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L10_C08_ISC_T1","case_id":"R2L10_C08_ISC_20240103_STAGE2","symbol":"095340","company_name":"ISC","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","evidence_available_at_that_date":"2024 opening-year test-socket/HBM exposure and relative-strength proxy; positive 90D path but later de-rating shows C08 needs customer-quality and margin-bridge proof before Green.","evidence_source":"historical public research-report/news proxy; stock-web OHLC validation; company-specific source URL hardening pending before promotion","stage2_evidence_fields":["relative_strength","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-03","entry_price":79400,"MFE_30D_pct":14.11,"MFE_90D_pct":36.02,"MFE_180D_pct":36.02,"MFE_1Y_pct":36.02,"MFE_2Y_pct":null,"MAE_30D_pct":-13.73,"MAE_90D_pct":-13.73,"MAE_180D_pct":-39.48,"MAE_1Y_pct":-39.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-55.51,"green_lateness_ratio":"not_applicable: no confirmed C08 Stage3-Green trigger used as representative","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L10_C08_ISC_20240103_STAGE2::2024-01-03::79400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L10_C08_MICROCONTACT_T1","case_id":"R2L10_C08_MICROCONTACT_20240103_STAGE2","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable_candidate_rejected","trigger_date":"2024-01-02","evidence_available_at_that_date":"Generic test-socket theme participation without durable customer-quality/revision/margin bridge; price path failed almost immediately after the candidate trigger.","evidence_source":"historical public theme proxy; stock-web OHLC validation; explicit company-specific Green evidence not confirmed in this research run","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv","profile_path":"atlas/symbol_profiles/098/098120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-03","entry_price":14400,"MFE_30D_pct":3.13,"MFE_90D_pct":3.13,"MFE_180D_pct":3.13,"MFE_1Y_pct":3.13,"MFE_2Y_pct":null,"MAE_30D_pct":-29.65,"MAE_90D_pct":-38.54,"MAE_180D_pct":-61.74,"MAE_1Y_pct":-61.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-09","peak_price":14850,"drawdown_after_peak_pct":-62.9,"green_lateness_ratio":"not_applicable: no confirmed C08 Stage3-Green trigger used as representative","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L10_C08_MICROCONTACT_20240103_STAGE2::2024-01-03::14400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L10_C08_TFE_T1","case_id":"R2L10_C08_TFE_20240103_STAGE2","symbol":"425420","company_name":"티에프이","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable_candidate_rejected","trigger_date":"2024-01-02","evidence_available_at_that_date":"Newer test-socket/test-interface supplier with theme participation but insufficient confirmed customer-quality/margin conversion; 90D MFE stayed below 20% while MAE was already large.","evidence_source":"historical public theme proxy; stock-web OHLC validation; company-specific source URL hardening pending","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-03","entry_price":36800,"MFE_30D_pct":0.95,"MFE_90D_pct":19.16,"MFE_180D_pct":19.16,"MFE_1Y_pct":19.16,"MFE_2Y_pct":null,"MAE_30D_pct":-22.96,"MAE_90D_pct":-22.96,"MAE_180D_pct":-55.11,"MAE_1Y_pct":-55.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":43850,"drawdown_after_peak_pct":-62.33,"green_lateness_ratio":"not_applicable: no confirmed C08 Stage3-Green trigger used as representative","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L10_C08_TFE_20240103_STAGE2::2024-01-03::36800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L10_C08_ISC_T4B","case_id":"R2L10_C08_ISC_20240328_4B_LOCAL","symbol":"095340","company_name":"ISC","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REVISION_MARGIN_BRIDGE","sector":"AI·반도체·전자부품","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage4B-local-watch","trigger_date":"2024-03-28","evidence_available_at_that_date":"Price-only local peak after the Stage2/Yellow rally. Useful as risk watch, but no non-price 4B evidence was confirmed at that date.","evidence_source":"stock-web OHLC validation; no non-price 4B evidence used for full 4B promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-28","entry_price":99400,"MFE_30D_pct":0.6,"MFE_90D_pct":0.6,"MFE_180D_pct":0.6,"MFE_1Y_pct":96.38,"MFE_2Y_pct":null,"MAE_30D_pct":-16.5,"MAE_90D_pct":-51.66,"MAE_180D_pct":-51.66,"MAE_1Y_pct":-51.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-55.51,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":"price_only|valuation_blowoff|positioning_overheat","four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L10_C08_ISC_20240328_4B_LOCAL::2024-03-28::99400","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_4B_timing_audit","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
```

### score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L10_C08_RINO_20240103_STAGE2","trigger_id":"R2L10_C08_RINO_T1","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":65,"customer_quality_score":50,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2_or_Yellow_watch","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":62,"revision_score":58,"relative_strength_score":72,"customer_quality_score":78,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"C08_Stage2_Actionable_qualified","changed_components":["customer_quality_score","margin_bridge_score","revision_score","relative_strength_score"],"component_delta_explanation":"C08 should reward customer-quality and margin/revision bridge more than generic HBM/test-socket labeling.","MFE_90D_pct":44.39,"MAE_90D_pct":-12.2,"score_return_alignment_label":"qualified_C08_positive_alignment","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L10_C08_ISC_20240103_STAGE2","trigger_id":"R2L10_C08_ISC_T1","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":65,"customer_quality_score":50,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2_or_Yellow_watch","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":62,"revision_score":58,"relative_strength_score":72,"customer_quality_score":78,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"C08_Stage2_Actionable_qualified","changed_components":["customer_quality_score","margin_bridge_score","revision_score","relative_strength_score"],"component_delta_explanation":"C08 should reward customer-quality and margin/revision bridge more than generic HBM/test-socket labeling.","MFE_90D_pct":36.02,"MAE_90D_pct":-13.73,"score_return_alignment_label":"qualified_C08_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L10_C08_MICROCONTACT_20240103_STAGE2","trigger_id":"R2L10_C08_MICROCONTACT_T1","symbol":"098120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":65,"customer_quality_score":50,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2_candidate","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":65,"customer_quality_score":30,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":57,"stage_label_after":"Rejected_or_Stage1_watch","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Generic test-socket exposure without customer-quality/revision/margin proof should be blocked from Stage2-Actionable.","MFE_90D_pct":3.13,"MAE_90D_pct":-38.54,"score_return_alignment_label":"counterexample_guard_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L10_C08_TFE_20240103_STAGE2","trigger_id":"R2L10_C08_TFE_T1","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":65,"customer_quality_score":50,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2_candidate","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":65,"customer_quality_score":30,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":65,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":57,"stage_label_after":"Rejected_or_Stage1_watch","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Generic test-socket exposure without customer-quality/revision/margin proof should be blocked from Stage2-Actionable.","MFE_90D_pct":19.16,"MAE_90D_pct":-22.96,"score_return_alignment_label":"counterexample_guard_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C08_counterexample_guard_profile","case_id":"R2L10_C08_ISC_20240328_4B_LOCAL","trigger_id":"R2L10_C08_ISC_T4B","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":62,"revision_score":58,"relative_strength_score":72,"customer_quality_score":78,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage4B_price_only_candidate","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":25,"margin_bridge_score":62,"revision_score":58,"relative_strength_score":72,"customer_quality_score":78,"policy_or_regulatory_score":10,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage4B_watch_only_overlay","changed_components":["four_b_evidence_type","full_4b_non_price_requirement"],"component_delta_explanation":"C08 price-only peak can be a risk watch, but it must not graduate to full 4B without revision/customer/order slowdown.","MFE_90D_pct":0.6,"MAE_90D_pct":-51.66,"score_return_alignment_label":"4B_watch_alignment","current_profile_verdict":"current_profile_correct"}
```

### shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_customer_quality_required_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,false,true,+1,"C08 should not inherit HBM equipment or generic semiconductor theme credit unless customer-quality plus margin/revision bridge exists","Positive rows with customer-quality proxies had usable 90D MFE; weak generic socket rows had poor MFE and severe MAE","R2L10_C08_RINO_T1|R2L10_C08_ISC_T1|R2L10_C08_MICROCONTACT_T1|R2L10_C08_TFE_T1",4,4,2,medium,canonical_shadow_only,"not production; company-specific source URL hardening required"
shadow_weight,C08_generic_socket_theme_stage2_block,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,false,true,+1,"Generic test-socket theme participation without quality/revision proof should be Stage1/watch rather than Stage2-Actionable","Two counterexamples generated MFE90 below 20% with MAE90 worse than -20%","R2L10_C08_MICROCONTACT_T1|R2L10_C08_TFE_T1",2,2,2,medium,canonical_shadow_only,"strengthens guardrail against price/theme-only promotion"
shadow_weight,C08_price_only_4B_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,false,true,+1,"Price-only local peak is useful as 4B watch, but full 4B needs non-price evidence such as revision slowdown or customer/order deterioration","ISC 2024 local peak protected drawdown, but row remains overlay-only because evidence type was price-only","R2L10_C08_ISC_T4B",1,0,1,low_medium,canonical_shadow_only,"do not weaken full_4b_requires_non_price_evidence"
```

### residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":4,"reused_case_count":1,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_false_positive","current_profile_too_late","price_only_4B_watch_not_full_4B"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R2L10_C08_SOURCE_URL_HARDENING","symbol":null,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reason":"company_specific_historical_evidence_urls_pending_for_promotion_batch","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R2
completed_loop = 10
next_round = R3
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest max_date used for forward-window eligibility: `2026-02-20`.
- Stock-Web schema confirms `tradable_raw`, `raw_unadjusted_marcap`, MFE/MAE formulas, and corporate-action contamination flags.
- Selected 2024 price shards were read for `058470`, `095340`, `098120`, and `425420`.
- This MD intentionally does not include live candidate language.

