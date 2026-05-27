# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R10
loop = 10
sector = 건설·부동산·건자재
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN
loop_objective = counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R10_loop_10_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is a post-calibrated residual research artifact. It is not a live candidate list, not an implementation patch, and not an investment recommendation. The only quantitative price source used here is Songdaiki/stock-web tradable raw OHLC.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
```

Applied global axes treated as already active:

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

This loop does not re-propose those axes globally. It stress-tests them inside C30, where balance-sheet/PF, completion-liability, and legal/quality-cost evidence often dominate short-term price momentum.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R10 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| fine_archetype_id | PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN |
| primary_archetype | construction_pf_balance_sheet_break |
| cases | HDC현대산업개발(294870), GS건설(006360), DL이앤씨(375500) |

C30 is treated as a balance-sheet and liability archetype, not as a simple order/backlog archetype. Price can rally on policy relief or housing sentiment, but Stage3-Green should require visible PF/liability containment, margin stabilization, and revision confirmation.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show broad R1~R13 coverage in the prior ingest snapshot: 398 discovered MDs, 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows. The same snapshot covers R10 at sector level, but visible md_registry lookup around the later rows did not surface a clean R10/C30 file in the accessible slice, so this loop is treated as C30 coverage-gap fill rather than a duplicate rematerialization.

Applied scoring diff already includes global Stage2 bonus, Yellow relaxation, Green strictness, Green revision strictness, full-4B non-price requirement, and hard-4C routing. Therefore this research does not propose global relaxation or global 4B/4C rules.

Novelty gate:

```text
selection_mode = auto_coverage_gap_fill
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 0
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields verified for this run:

| field | value |
|---|---|
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

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | entry_date | 180D forward window | corporate-action window | calibration_usable |
|---|---:|---|---|---:|---|---|
| R10L10_C30_HDC_POS | 294870 | atlas/symbol_profiles/294/294870.json | 2024-01-26 | >=180 | clean_180D_window | true |
| R10L10_C30_GS_POS_4B | 006360 | atlas/symbol_profiles/006/006360.json | 2024-02-28 | >=180 | clean_180D_window | true |
| R10L10_C30_DL_FALSE_GREEN | 375500 | atlas/symbol_profiles/375/375500.json | 2024-01-30 | >=180 | clean_180D_window | true |

Profile caveats: all three symbols have historical corporate-action candidates outside the tested 2024 180D windows. Those older windows are not used for weight calibration.

## 6. Canonical Archetype Compression Map

| fine trigger family | canonical_archetype_id | why compressed here |
|---|---|---|
| PF overhang relief + housing sentiment recovery | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | balance-sheet/liability relief drives rerating more than raw sales backlog |
| quality-cost/legal liability cap after construction defect issue | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | hard-cost/brand-liability break changes equity-risk premium |
| low-PF narrative but unclosed margin/revision bridge | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | strong balance-sheet language alone is insufficient when cost/revision fails |

## 7. Case Selection Summary

| case_id | symbol | company | role | best trigger | entry_date | representative? | rationale |
|---|---:|---|---|---|---|---|---|
| R10L10_C30_HDC_POS | 294870 | HDC현대산업개발 | structural_success | Stage2-Actionable | 2024-01-26 | yes | legal/quality overhang had already been repriced, and housing/PF relief beta plus balance-sheet survival translated into a large but volatile rerating path |
| R10L10_C30_GS_POS_4B | 006360 | GS건설 | high_mae_success + 4B_overlay_success | Stage2-Actionable | 2024-02-28 | yes | recovery trade worked only after quality-cost risk became bounded; 4B required non-price risk overlay near late-August rally |
| R10L10_C30_DL_FALSE_GREEN | 375500 | DL이앤씨 | false_positive_green | Stage3-Yellow false positive | 2024-01-30 | yes | apparently conservative balance-sheet/PF profile failed to close margin/revision bridge, so price path underperformed despite early apparent quality |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 6
```

The positive cases are not “clean Green” examples. They are high-MAE construction reratings where a Stage2-Actionable label is often safer than a Green label until liability/PF/margin evidence closes. The counterexample shows why C30 needs a cap on Green when the balance sheet looks better than the income-statement bridge.

## 9. Evidence Source Map

| case_id | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence | validation stance |
|---|---|---|---|---|---|
| R10L10_C30_HDC_POS | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength; PF/housing beta relief | partial financial_visibility; not enough for immediate Green | valuation_blowoff; positioning_overheat; event-cap after fast rerating | none | positive Stage2, delayed Green |
| R10L10_C30_GS_POS_4B | quality-cost risk cap; relative_strength; housing/PF sentiment recovery | partial margin_bridge; financial_visibility still noisy | non-price quality/legal overhang + valuation recovery; not price-only | thesis_break_watch_only from prior quality-liability history | positive but 4B overlay required |
| R10L10_C30_DL_FALSE_GREEN | low-PF narrative; conservative balance sheet | margin_bridge weak; revision weak; financial visibility not enough | none | thesis_evidence_broken via cost/revision underdelivery | counterexample / false positive Green |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry row source |
|---:|---|---|---|---|
| 294870 | HDC현대산업개발 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv | atlas/symbol_profiles/294/294870.json | c=17,530 on 2024-01-26 |
| 006360 | GS건설 | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv | atlas/symbol_profiles/006/006360.json | c=16,210 on 2024-02-28 |
| 375500 | DL이앤씨 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv | atlas/symbol_profiles/375/375500.json | c=41,850 on 2024-01-30 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence split | current_profile_verdict | aggregate_role |
|---|---|---|---|---|---:|---|---|---|
| R10L10_C30_HDC_T1 | R10L10_C30_HDC_POS | Stage2-Actionable | 2024-01-26 | 2024-01-26 | 17530 | PF/housing beta relief + overhang cap | current_profile_correct | representative |
| R10L10_C30_HDC_T2 | R10L10_C30_HDC_POS | 4B-overlay | 2024-08-26 | 2024-08-26 | 26700 | non-price valuation/event cap after +60% MFE path | current_profile_4B_too_late | 4B_overlay_only |
| R10L10_C30_GS_T1 | R10L10_C30_GS_POS_4B | Stage2-Actionable | 2024-02-28 | 2024-02-28 | 16210 | quality-cost cap + PF sentiment relief | current_profile_correct | representative |
| R10L10_C30_GS_T2 | R10L10_C30_GS_POS_4B | 4B-overlay | 2024-08-27 | 2024-08-27 | 21550 | late-August recovery with still-present quality/legal discount | current_profile_correct | 4B_overlay_only |
| R10L10_C30_DL_T1 | R10L10_C30_DL_FALSE_GREEN | Stage3-Yellow/false-Green-test | 2024-01-30 | 2024-01-30 | 41850 | low-PF narrative without margin/revision closure | current_profile_false_positive | representative |
| R10L10_C30_DL_T2 | R10L10_C30_DL_FALSE_GREEN | 4C-watch | 2024-04-17 | 2024-04-17 | 32500 | margin/revision bridge failed; downside persisted | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate triggers

| trigger_id | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R10L10_C30_HDC_T1 | 2024-01-26 | 17530 | 18.37 | -5.53 | 18.37 | -11.58 | 60.87 | -11.58 | 2024-08-26 | 28200 | -39.01 |
| R10L10_C30_GS_T1 | 2024-02-28 | 16210 | 2.10 | -11.29 | 2.65 | -13.39 | 34.18 | -13.39 | 2024-08-27 | 21750 | -21.70 |
| R10L10_C30_DL_T1 | 2024-01-30 | 41850 | 5.50 | -19.35 | 5.50 | -23.66 | 5.50 | -25.81 | 2024-02-02 | 44150 | -34.66 |

### Overlay triggers

| trigger_id | overlay_type | entry_date | entry_price | reference_stage2_entry | local/full peak reference | verdict |
|---|---|---|---:|---:|---|---|
| R10L10_C30_HDC_T2 | 4B-overlay | 2024-08-26 | 26700 | 17530 | 28200 full observed high | good_full_window_4B_timing_but_late |
| R10L10_C30_GS_T2 | 4B-overlay | 2024-08-27 | 21550 | 16210 | 21750 full observed high | good_full_window_4B_timing |
| R10L10_C30_DL_T2 | 4C-watch | 2024-04-17 | 32500 | 41850 | prior 44150 high | hard_4c_late |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely label | actual path | verdict | stress conclusion |
|---|---|---|---|---|
| R10L10_C30_HDC_POS | Stage2-Actionable, Yellow wait | +60.87% 180D MFE but -11.58% MAE and -39.01% post-peak drawdown | current_profile_correct | Stage2 bonus works; Green should wait for liability/PF/margin evidence |
| R10L10_C30_GS_POS_4B | Stage2-Actionable, 4B overlay near Aug | +34.18% 180D MFE; -13.39% MAE | current_profile_correct | non-price 4B requirement is useful because price-only local peaks were too noisy |
| R10L10_C30_DL_FALSE_GREEN | Potential Yellow/Green if balance-sheet quality overweighed | only +5.50% MFE vs -25.81% 180D MAE | current_profile_false_positive | C30 needs Green cap when margin/revision bridge is not closed |

Answers to required stress questions:

1. P0 mostly identifies HDC/GS as Stage2 rather than clean Green; this matches price path better than immediate Green.
2. P0 would be vulnerable on DL if it overweights low-PF/balance-sheet quality without margin/revision closure.
3. Stage2 bonus is not too high for HDC/GS; it is too blunt if applied to DL without a margin/revision guard.
4. Yellow 75 is acceptable, but in C30 Yellow should not be treated as de facto Green.
5. Green 87/revision 55 should be strengthened inside C30 supplier/contractor names with unresolved cost/PF evidence.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement is appropriate and strengthened by HDC/GS overlay timing.
8. Hard 4C routing should become earlier when cost/revision evidence breaks after a balance-sheet-quality narrative.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green test entry | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| R10L10_C30_HDC_POS | 17,530 | no confirmed Green before 4B | not_applicable | no_confirmed_Stage3_Green_trigger; Stage2 captured most useful entry but required high-MAE tolerance |
| R10L10_C30_GS_POS_4B | 16,210 | no confirmed Green before 4B | not_applicable | no_confirmed_Stage3_Green_trigger; price path was a recovery trade not a clean Green |
| R10L10_C30_DL_FALSE_GREEN | 41,850 | 41,850 false-Green-test | 0.00 | Green-at-entry would be false because upside was only 5.50% and downside reached -25.81% |

C30’s problem is not classic Green lateness. It is Green contamination: balance-sheet/PF quality language can pull a contractor into Yellow/Green before margin and revision reality are safe.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | timing verdict |
|---|---|---:|---:|---|
| R10L10_C30_HDC_T2 | valuation_blowoff; positioning_overheat; event_cap | 0.944 | 0.944 | good_full_window_4B_timing_but_late |
| R10L10_C30_GS_T2 | valuation_recovery; quality/legal overhang; positioning_overheat | 0.964 | 0.964 | good_full_window_4B_timing |
| R10L10_C30_DL_T2 | thesis_break_watch_only | null | null | not_4B; treat as 4C/protection audit |

The key C30 lesson is that 4B should be an overlay, not a mechanical exit. HDC/GS had real non-price risk context near the full-window peak; DL was not a 4B case, because it never produced a full rerating window.

## 16. 4C Protection Audit

| trigger_id | prior peak | 4C/watch entry | post-watch MAE proxy | label | interpretation |
|---|---:|---:|---:|---|---|
| R10L10_C30_DL_T2 | 44,150 | 32,500 | -11.23 from watch to 28,850 low | hard_4c_late | waiting for formal break after the margin bridge failed sacrificed much of the protection value |
| R10L10_C30_GS_T2 | 21,750 | 21,550 | -21.70 from peak to Dec low | thesis_break_watch_only | 4B overlay protected risk better than hard 4C routing |
| R10L10_C30_HDC_T2 | 28,200 | 26,700 | -39.01 from peak to Dec low | thesis_break_watch_only | non-price 4B overlay was needed before hard thesis break evidence appeared |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c30_pf_liability_green_cap
baseline_value = absent
tested_value = cap Stage3-Green unless PF/liability/margin/revision evidence is closed
proposal_type = sector_shadow_only
confidence = low_to_medium
```

Rule candidate:

```text
For L9/C30 construction and housing names, Stage3-Green should require at least two of:
1. visible PF exposure containment or refinancing completion,
2. legal/quality-cost liability bounded,
3. margin bridge improvement in reported or consensus evidence,
4. revision score above Green floor,
5. cash-flow/receivable/inventory stress not worsening.

If only price recovery + policy/housing beta exists, cap at Stage2-Actionable or Stage3-Yellow.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
axis = c30_margin_revision_bridge_required_for_green
delta = +1 guard / no global delta
```

C30 should split contractor positives into two branches:

| branch | allowed label | required evidence |
|---|---|---|
| PF/housing beta recovery | Stage2-Actionable / Yellow | policy option + price/RS + overhang relief, but not Green |
| balance-sheet repair + margin bridge | Stage3-Green | PF/liability bounded + margin/revision confirmation |
| cost/PF thesis break | 4C watch/hard 4C | cost/revision failure, refinancing failure, accounting/trust break |

## 19. Before / After Backtest Comparison

| profile_id | scope | selected triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | score_return_alignment |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | 3 | 8.84 | -16.21 | 33.52 | -16.93 | 0.33 | mixed_good_stage2_bad_false_green |
| P0b_e2r_2_0_baseline_reference | rollback | 3 | 8.84 | -16.21 | 33.52 | -16.93 | 0.33 | weaker_green_guard |
| P1_L9_sector_candidate | L9 sector | 3 | 8.84 | -16.21 | 33.52 | -16.93 | 0.00 after Green cap | improved_by_capping_unclosed_margin_bridge |
| P2_C30_archetype_candidate | C30 archetype | 3 | 8.84 | -16.21 | 33.52 | -16.93 | 0.00 after C30 Green branch split | best_alignment |
| P3_counterexample_guard_profile | C30 guard | 3 | 8.84 | -16.21 | 33.52 | -16.93 | 0.00 | DL false-Green blocked |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_180D | MAE_180D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R10L10_C30_HDC_POS | 74 | Stage2-Actionable/Yellow | 76 | Stage2-Actionable/Yellow | 60.87 | -11.58 | good; high upside but high drawdown means not clean Green |
| R10L10_C30_GS_POS_4B | 73 | Stage2-Actionable | 75 | Stage2-Actionable/Yellow | 34.18 | -13.39 | good; positive but 4B overlay needed |
| R10L10_C30_DL_FALSE_GREEN | 78 | Stage3-Yellow / false-Green risk | 67 | Stage2-watch / 4C-watch | 5.50 | -25.81 | improved; counterexample guard blocks bad Green |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN | 2 | 1 | 2 | 1 | 3 | 0 | 6 | 3 | 1 | true | true | reduced but needs more builder/PF lender cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [false_positive_green_from_balance_sheet_quality_without_margin_bridge, late_4C_watch_after_margin_revision_failure, high_MAE_success_in_construction_recovery]
new_axis_proposed: [c30_pf_liability_green_cap, c30_margin_revision_bridge_required_for_green]
existing_axis_strengthened: [stage3_green_revision_min in C30 only, full_4b_requires_non_price_evidence]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema fields
- symbol profiles for 294870, 006360, 375500
- entry_date and entry_price from tradable shards
- 30D/90D/180D MFE/MAE using visible tradable OHLC rows
- clean 180D corporate-action status based on profile candidate dates
- same_entry_group_id / representative trigger dedupe
```

Not validated in this loop:

```text
- exact production score from stock_agent code
- live/current candidate status
- brokerage execution or position sizing
- final promotion into production scoring
- full fundamental source extraction from every broker/DART document
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_pf_liability_green_cap,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"PF/liability/margin/revision evidence must close before Green","DL false-Green blocked while HDC/GS remain Stage2/Yellows","R10L10_C30_HDC_T1|R10L10_C30_GS_T1|R10L10_C30_DL_T1",3,3,1,low_to_medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c30_margin_revision_bridge_required_for_green,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"DL showed low-PF quality narrative without return alignment","false_positive_rate improves from 0.33 to 0.00 in this sample","R10L10_C30_DL_T1",1,1,1,low,archetype_shadow_only,"requires more holdout cases"
shadow_weight,full_4b_requires_non_price_evidence,existing_axis_strengthened,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,true,true,0,"HDC/GS 4B overlays align near full peaks only when non-price risk exists","kept/strengthened for C30","R10L10_C30_HDC_T2|R10L10_C30_GS_T2",2,2,0,medium,existing_axis_test,"no global change"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L10_C30_HDC_POS","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R10L10_C30_HDC_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 captured high-MAE recovery; Green should wait","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Large upside with large post-peak drawdown; C30 needs 4B overlay."}
{"row_type":"case","case_id":"R10L10_C30_GS_POS_4B","symbol":"006360","company_name":"GS건설","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R10L10_C30_GS_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Recovery trade worked, but non-price 4B overlay was required near late-August peak","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Quality/legal overhang makes this Stage2/Yellows rather than clean Green."}
{"row_type":"case","case_id":"R10L10_C30_DL_FALSE_GREEN","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R10L10_C30_DL_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Low-PF quality narrative failed because margin/revision bridge did not close","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample for C30 Green without margin/revision confirmation."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R10L10_C30_HDC_T1","case_id":"R10L10_C30_HDC_POS","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","sector":"건설·부동산·건자재","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","evidence_available_at_that_date":"PF/housing beta relief and legal/quality overhang repricing visible before clean Green confirmation","evidence_source":"historical public event/disclosure family; price verified by stock-web","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["partial_financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":17530,"MFE_30D_pct":18.37,"MFE_90D_pct":18.37,"MFE_180D_pct":60.87,"MFE_1Y_pct":60.87,"MFE_2Y_pct":null,"MAE_30D_pct":-5.53,"MAE_90D_pct":-11.58,"MAE_180D_pct":-11.58,"MAE_1Y_pct":-11.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":28200,"drawdown_after_peak_pct":-39.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L10_C30_HDC_2024-01-26_17530","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L10_C30_HDC_T2","case_id":"R10L10_C30_HDC_POS","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","sector":"건설·부동산·건자재","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-08-26","evidence_available_at_that_date":"Fast rerating plus event-cap/positioning overheat after PF/housing beta recovery","evidence_source":"historical public event/disclosure family; price verified by stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-26","entry_price":26700,"MFE_30D_pct":5.62,"MFE_90D_pct":5.62,"MFE_180D_pct":5.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.92,"MAE_90D_pct":-37.08,"MAE_180D_pct":-39.01,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":28200,"drawdown_after_peak_pct":-39.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.944,"four_b_full_window_peak_proximity":0.944,"four_b_timing_verdict":"good_full_window_4B_timing_but_late","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L10_C30_HDC_2024-08-26_26700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L10_C30_GS_T1","case_id":"R10L10_C30_GS_POS_4B","symbol":"006360","company_name":"GS건설","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","sector":"건설·부동산·건자재","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-28","evidence_available_at_that_date":"quality/legal cost risk started to be bounded; PF/housing relief trade visible but not clean Green","evidence_source":"historical public event/disclosure family; price verified by stock-web","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["partial_margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-28","entry_price":16210,"MFE_30D_pct":2.10,"MFE_90D_pct":2.65,"MFE_180D_pct":34.18,"MFE_1Y_pct":34.18,"MFE_2Y_pct":null,"MAE_30D_pct":-11.29,"MAE_90D_pct":-13.39,"MAE_180D_pct":-13.39,"MAE_1Y_pct":-13.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750,"drawdown_after_peak_pct":-21.70,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L10_C30_GS_2024-02-28_16210","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L10_C30_GS_T2","case_id":"R10L10_C30_GS_POS_4B","symbol":"006360","company_name":"GS건설","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","sector":"건설·부동산·건자재","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-08-27","evidence_available_at_that_date":"late-August recovery near full observed peak, while quality/legal overhang remained non-price risk","evidence_source":"historical public event/disclosure family; price verified by stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","legal_or_regulatory_block"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-27","entry_price":21550,"MFE_30D_pct":0.93,"MFE_90D_pct":0.93,"MFE_180D_pct":0.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.10,"MAE_90D_pct":-21.72,"MAE_180D_pct":-21.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750,"drawdown_after_peak_pct":-21.70,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.964,"four_b_full_window_peak_proximity":0.964,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","legal_or_regulatory_block"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L10_C30_GS_2024-08-27_21550","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L10_C30_DL_T1","case_id":"R10L10_C30_DL_FALSE_GREEN","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","sector":"건설·부동산·건자재","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage3-Yellow/false-Green-test","trigger_date":"2024-01-30","evidence_available_at_that_date":"low-PF/conservative balance-sheet narrative but margin/revision bridge not confirmed","evidence_source":"historical public event/disclosure family; price verified by stock-web","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-30","entry_price":41850,"MFE_30D_pct":5.50,"MFE_90D_pct":5.50,"MFE_180D_pct":5.50,"MFE_1Y_pct":5.50,"MFE_2Y_pct":null,"MAE_30D_pct":-19.35,"MAE_90D_pct":-23.66,"MAE_180D_pct":-25.81,"MAE_1Y_pct":-31.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":44150,"drawdown_after_peak_pct":-34.66,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L10_C30_DL_2024-01-30_41850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L10_C30_DL_T2","case_id":"R10L10_C30_DL_FALSE_GREEN","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_OVERHANG_RESOLUTION_AND_QUALITY_COST_CAP_VS_MARGIN_FALSE_GREEN","sector":"건설·부동산·건자재","primary_archetype":"construction_pf_balance_sheet_break","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C-watch","trigger_date":"2024-04-17","evidence_available_at_that_date":"margin/revision bridge had failed after low-PF quality narrative; price made lower lows","evidence_source":"historical public event/disclosure family; price verified by stock-web","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-17","entry_price":32500,"MFE_30D_pct":10.15,"MFE_90D_pct":21.54,"MFE_180D_pct":21.54,"MFE_1Y_pct":21.54,"MFE_2Y_pct":null,"MAE_30D_pct":-1.54,"MAE_90D_pct":-11.23,"MAE_180D_pct":-11.23,"MAE_1Y_pct":-11.23,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":39500,"drawdown_after_peak_pct":-26.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L10_C30_DL_2024-04-17_32500","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L10_C30_HDC_POS","trigger_id":"R10L10_C30_HDC_T1","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"roe_pbr_capital_return_score":"unknown_or_not_supported"},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Stage3-Yellow","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":3,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"c30_pf_liability_green_cap":1},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable/Stage3-Yellow","changed_components":["c30_pf_liability_green_cap"],"component_delta_explanation":"Positive recovery remains Stage2/Yellow until margin/revision and liability evidence close.","MFE_90D_pct":18.37,"MAE_90D_pct":-11.58,"score_return_alignment_label":"good_stage2_high_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L10_C30_GS_POS_4B","trigger_id":"R10L10_C30_GS_T1","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":7,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":7,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2,"c30_4b_non_price_overlay":1},"weighted_score_after":75,"stage_label_after":"Stage2-Actionable/Stage3-Yellow with 4B watch","changed_components":["c30_4b_non_price_overlay"],"component_delta_explanation":"Recovery worked, but legal/quality risk keeps Green capped and supports non-price 4B overlay near full peak.","MFE_90D_pct":2.65,"MAE_90D_pct":-13.39,"score_return_alignment_label":"late_payoff_high_mae_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L10_C30_DL_FALSE_GREEN","trigger_id":"R10L10_C30_DL_T1","symbol":"375500","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow / false-Green-risk","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1,"c30_margin_revision_bridge_required_for_green":-1,"c30_pf_liability_green_cap":-1},"weighted_score_after":67,"stage_label_after":"Stage2-watch / 4C-watch","changed_components":["c30_margin_revision_bridge_required_for_green","c30_pf_liability_green_cap"],"component_delta_explanation":"Balance-sheet quality narrative is capped when margin and revision evidence fail to close.","MFE_90D_pct":5.50,"MAE_90D_pct":-23.66,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See section 24 CSV.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":0,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"diversity_score_summary":"high_total_58_avg_19.3","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["false_positive_green_from_balance_sheet_quality_without_margin_bridge","late_4C_watch_after_margin_revision_failure","high_MAE_success_in_construction_recovery"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R10/C30 construction PF-balance-sheet break undercovered in accessible md_registry; needs positive/counterexample/4B-4C split"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R10_C30_TAEYOUNG_PF_WORKOUT_REFERENCE","symbol":"009410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"workout/PF reference is archetype context only; not included in weight calibration in this MD","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R10 holdout or R11
recommended_next_scope = L9_CONSTRUCTION_REALESTATE_HOUSING / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK holdout with additional PF lender-builder or mid-cap builder examples
avoid_next = repeating HDC 2024-01-26, GS 2024-02-28, DL 2024-01-30 without new trigger family
```

## 28. Source Notes

- Stock-Web manifest/schema and all price rows are from Songdaiki/stock-web.
- The quantitative OHLC values are based on tradable raw shards, not adjusted prices.
- The research evidence labels are historical trigger-family proxies for calibration; they are not live recommendations.
- No stock_agent source code was opened or patched in this loop.
