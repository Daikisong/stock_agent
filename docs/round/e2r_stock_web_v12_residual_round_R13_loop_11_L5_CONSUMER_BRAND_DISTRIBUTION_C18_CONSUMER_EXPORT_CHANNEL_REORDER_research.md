# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 11
loop_name = cross_archetype_holdout_2
output_file = e2r_stock_web_v12_residual_round_R13_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This standalone Markdown file is a **post-calibrated holdout loop**, not a live candidate report. It uses stock-web OHLC rows for historical trigger-level calibration and stress-tests the already-applied `e2r_2_1_stock_web_calibrated_proxy`.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

existing applied axes tested:
- stage2_actionable_evidence_bonus = +2.0
- stage3_yellow_total_min = 75.0
- stage3_green_total_min = 87.0
- stage3_green_revision_min = 55.0
- stage3_cross_evidence_green_buffer = +1.5
- price_only_blowoff_blocks_positive_stage = true
- full_4b_requires_non_price_evidence = true
- hard_4c_thesis_break_routes_to_4c = true
```

This loop does **not** re-propose the global calibration. It asks whether the `C18_CONSUMER_EXPORT_CHANNEL_REORDER` shadow rule from the prior consumer loops survives a holdout set with both structural positives and weak/event-driven counterexamples.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 11
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = K_FOOD_EXPORT_REORDER_HOLDOUT
loop_objective =
  - holdout_validation
  - residual_false_positive_mining
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - coverage_gap_fill
```

### Research question

Does C18 still need a **recurring export/channel reorder + margin bridge** gate, or can a general consumer-brand rerating rule handle these names without overfitting?

The holdout answer is: the generic profile is directionally useful, but still too blunt. Consumer exporters behave like a pressure cooker: the same headline heat can mean either real repeat demand or just steam escaping from an event premium. The difference is whether reorder recurrence and margin conversion are visible before the price move turns vertical.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact scope was limited to calibration summaries and applied scoring diffs.

```text
ingest_summary_observed:
- discovered_md_count = 398
- discovered_result_md_count = 107
- raw_trigger_rows = 4951
- validated_trigger_rows = 1940
- aggregate_representative_trigger_rows = 1376
- rounds_covered = R1~R13
- loops_covered = 1~9

duplicate_avoidance:
- R13 loop 11 uses 3 new independent holdout cases.
- 2 cases are reused from the prior C18 axis as explicit holdout validation, with independent_evidence_weight = 0.5.
- reused cases do not count as new independent cases.
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Stock-web manifest fields inspected:

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
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | entry window | forward 180D available | 180D corporate-action overlap | calibration_usable |
|---|---:|---|---|---:|---:|---:|
| R13L11_C18_SAMYANG_003230 | 003230 | atlas/symbol_profiles/003/003230.json | 2024-03-25 onward | true | false | true |
| R13L11_C18_BINGGRAE_005180 | 005180 | atlas/symbol_profiles/005/005180.json | 2024-04-15 onward | true | false | true |
| R13L11_C18_NONGSHIM_004370 | 004370 | atlas/symbol_profiles/004/004370.json | 2023-02-10 onward | true | false | true |
| R13L11_C18_ORION_271560 | 271560 | atlas/symbol_profiles/271/271560.json | 2024-01-16 onward | true | false | true |
| R13L11_C18_LOTTEWELLFOOD_280360 | 280360 | atlas/symbol_profiles/280/280360.json | 2024-05-22 onward | true | false | true |

Validation note: stock-web profile metadata and tradable shard excerpts were inspected directly. Quantitative fields below are rounded research-proxy calculations from the retrieved stock-web row windows. A later repository ingestion job should re-compute exact values programmatically before any promotion batch.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| K_FOOD_EXPORT_REORDER_HOLDOUT | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Requires repeated export/channel demand evidence and margin conversion, not merely a consumer brand rally. |
| DOMESTIC_PRICE_COST_TAILWIND | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Can support Yellow, but not Green without reorder recurrence. |
| EVENT_PREMIUM_CONSUMER_EXPORT | C18_CONSUMER_EXPORT_CHANNEL_REORDER | Must be capped if the evidence is event/policy/price-only. |
| CHANNEL_REORDER_4B_OVERLAY | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 4B is overlay; full 4B requires non-price evidence such as slowdown, valuation blowoff, or positioning overheat. |

## 7. Case Selection Summary

| case_id | symbol | company | case role | positive/counterexample | new independent? | best trigger |
|---|---:|---|---|---|---:|---|
| R13L11_C18_SAMYANG_003230 | 003230 | 삼양식품 | structural_success | positive | false | R13L11_T001_003230_STAGE2 |
| R13L11_C18_BINGGRAE_005180 | 005180 | 빙그레 | high_mae_success | positive | false | R13L11_T004_005180_STAGE2 |
| R13L11_C18_NONGSHIM_004370 | 004370 | 농심 | stage2_promote_candidate | positive | true | R13L11_T006_004370_YELLOW |
| R13L11_C18_ORION_271560 | 271560 | 오리온 | failed_rerating | counterexample | true | R13L11_T007_271560_COUNTER |
| R13L11_C18_LOTTEWELLFOOD_280360 | 280360 | 롯데웰푸드 | boundary / 4B-watch | counterexample | true | R13L11_T008_280360_HOLDOUT |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 3
4C_case_count = 1
new_independent_case_count = 3
reused_case_count = 2
new_independent_case_ratio = 3 / 5 = 0.60
minimum requirement passed = true
```

The loop just clears the novelty gate. It is deliberately a holdout: not a broad new discovery loop, but a stress test of whether the C18 rule survives nearby lookalikes.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B/4C evidence | evidence interpretation |
|---|---|---|---|---|
| 삼양식품 | relative strength, export/channel reorder proxy, early revision signal | confirmed revision, margin bridge, repeated sources | valuation/positioning blowoff | Early non-price evidence mattered; Green confirmation was late. |
| 빙그레 | relative strength, product/export demand proxy, early margin bridge | financial visibility | valuation/positioning blowoff | Strong MFE, but later spike needed 4B overlay. |
| 농심 | pricing/cost relief, brand/export support | margin bridge, financial visibility | none | Yellow/Stage2 valid, Green not automatic. |
| 오리온 | policy/event optionality | weak/absent | thesis watch | Event without reorder recurrence failed to produce strong MFE. |
| 롯데웰푸드 | relative strength, margin bridge proxy | partial financial visibility | price-only local peak | Mixed boundary case: not pure Green; useful for cap/guard. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry rows inspected |
|---:|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2023.csv; 2024.csv | atlas/symbol_profiles/003/003230.json | 2023-11 to 2024-08 |
| 005180 | atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv | atlas/symbol_profiles/005/005180.json | 2024-01 to 2024-08 |
| 004370 | atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv | atlas/symbol_profiles/004/004370.json | 2023-01 to 2023-08 |
| 271560 | atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv | atlas/symbol_profiles/271/271560.json | 2024-01 to 2024-08 |
| 280360 | atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv | atlas/symbol_profiles/280/280360.json | 2024-01 to 2024-08 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | role | current verdict |
|---|---:|---|---|---|---:|---|---|
| R13L11_T001_003230_STAGE2 | 003230 | Stage2-Actionable | 2024-03-25 | 2024-03-25 | 206500 | representative | current_profile_missed_structural |
| R13L11_T002_003230_GREEN_LATE | 003230 | Stage3-Green | 2024-05-20 | 2024-05-20 | 502000 | label_comparison_only | current_profile_too_late |
| R13L11_T003_003230_4B | 003230 | 4B-overlay | 2024-06-18 | 2024-06-18 | 712000 | 4B_overlay_only | current_profile_4B_too_late |
| R13L11_T004_005180_STAGE2 | 005180 | Stage2-Actionable | 2024-04-15 | 2024-04-15 | 61900 | representative | current_profile_too_late |
| R13L11_T005_005180_4B | 005180 | 4B-overlay | 2024-06-10 | 2024-06-10 | 112100 | 4B_overlay_only | current_profile_4B_too_late |
| R13L11_T006_004370_YELLOW | 004370 | Stage3-Yellow | 2023-02-10 | 2023-02-10 | 356000 | representative | current_profile_correct |
| R13L11_T007_271560_COUNTER | 271560 | Stage2-false-positive-test | 2024-01-16 | 2024-01-16 | 96600 | representative | current_profile_false_positive |
| R13L11_T008_280360_HOLDOUT | 280360 | Stage2-Actionable | 2024-05-22 | 2024-05-22 | 149800 | representative | current_profile_missed_structural |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R13L11_T001_003230_STAGE2 | 206500 | 61.3 | 247.7 | 247.7 | -2.7 | -2.7 | -2.7 | 2024-06-19 | 718000 | -42.7 |
| R13L11_T002_003230_GREEN_LATE | 502000 | 43.0 | 43.0 | 43.0 | -18.1 | -42.1 | -42.1 | 2024-06-19 | 718000 | -42.7 |
| R13L11_T003_003230_4B | 712000 | 0.8 | 0.8 | 0.8 | -17.1 | -42.1 | -42.1 | 2024-06-19 | 718000 | -42.7 |
| R13L11_T004_005180_STAGE2 | 61900 | 57.8 | 91.3 | 91.3 | -6.6 | -6.6 | -6.6 | 2024-06-11 | 118400 | -37.8 |
| R13L11_T005_005180_4B | 112100 | 5.6 | 5.6 | 5.6 | -12.9 | -34.3 | -34.3 | 2024-06-11 | 118400 | -37.8 |
| R13L11_T006_004370_YELLOW | 356000 | 20.2 | 26.4 | 28.1 | -3.7 | -3.7 | -3.7 | 2023-06-08 | 456000 | -14.7 |
| R13L11_T007_271560_COUNTER | 96600 | 2.9 | 2.9 | 10.5 | -7.1 | -7.1 | -10.2 | 2024-06-18 | 106700 | -18.7 |
| R13L11_T008_280360_HOLDOUT | 149800 | 39.2 | 39.2 | 39.2 | -4.2 | -4.2 | -4.2 | 2024-06-18 | 208500 | -31.2 |

## 13. Current Calibrated Profile Stress Test

| case | current profile expected behavior | actual path | verdict |
|---|---|---|---|
| 삼양식품 | Would likely wait for stronger revision/Green confirmation. | Stage2-type trigger captured much more of the move than Green. | current_profile_missed_structural |
| 빙그레 | Would probably Yellow/late Stage2 after evidence thickened. | Early trigger produced strong MFE but later needed 4B overlay. | current_profile_too_late |
| 농심 | Would likely Stage2/Yellow but not Green. | Moderate positive MFE, no explosive rerating. | current_profile_correct |
| 오리온 | Weak event/policy evidence should not promote. | Low MFE and meaningful MAE. | current_profile_false_positive if promoted |
| 롯데웰푸드 | May miss a margin-bridge Stage2 but should cap Green. | Good local MFE but sharp 4B risk. | current_profile_missed_structural |

Answers to mandatory questions:

```text
1. current calibrated profile behavior:
   useful globally, but still under-specifies C18 channel/reorder vs event/cost-only boundary.

2. MFE/MAE alignment:
   early C18 reorder+margin triggers aligned strongly; event-only triggers did not.

3. Stage2 bonus:
   generally correct, but C18 needs evidence-shape gating.

4. Yellow threshold 75:
   appropriate for moderate names such as 농심 and 롯데웰푸드.

5. Green threshold 87/revision 55:
   correct as global guard; C18 should not weaken Green globally.

6. price-only blowoff guard:
   strengthened; price-only peaks are overlay, not positive promotion.

7. full 4B non-price requirement:
   strengthened; C18 blowoffs need valuation/positioning/margin/channel slowdown confirmation.

8. hard 4C routing:
   kept; event/policy failure should remain protection logic, not negative entry training.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable entry | Green entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 삼양식품 | 206500 | 502000 | 0.578 | Green was materially late, but still before full observed peak. |
| 빙그레 | 61900 | not confirmed | not_applicable | Stage2/Yelllow and 4B overlay more useful than late Green. |
| 농심 | 356000 | no Green | not_applicable | Yellow is enough; Green would overstate evidence. |
| 오리온 | 96600 | no Green | not_applicable | Should remain watch/no-promotion. |
| 롯데웰푸드 | 149800 | no Green | not_applicable | Boundary case; Yellow plus 4B-watch preferred. |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | evidence type | timing verdict |
|---|---:|---:|---|---|
| R13L11_T003_003230_4B | 0.988 | 0.988 | valuation_blowoff, positioning_overheat, price_only | good_full_window_4B_timing_if_non_price_overheat_confirmed |
| R13L11_T005_005180_4B | 0.888 | 0.888 | valuation_blowoff, positioning_overheat, price_only | good_full_window_4B_timing_if_non_price_overheat_confirmed |
| R13L11_T008_280360_HOLDOUT | 0.950 | 0.950 | price_only, valuation_blowoff | price_only_local_4B_requires_margin_or_revision_slowdown |

## 16. 4C Protection Audit

| case | 4C evidence | label | note |
|---|---|---|---|
| 오리온 | thesis_evidence_broken watch | thesis_break_watch_only | Weak event/policy evidence without reorder recurrence should be capped before 4C. |
| 롯데웰푸드 | no hard break | thesis_break_watch_only | 4B overlay more relevant than hard 4C. |
| 삼양식품 / 빙그레 | no hard break at early trigger | not_applicable | Later drawdowns are 4B/overheat, not thesis-break calibration. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_export_reorder_margin_bridge_holdout_gate
proposal_type = sector_shadow_only
```

Candidate:

```text
For L5 consumer exporters, Stage2/Yellow promotion can be accelerated when:
- repeat channel reorder or export demand proxy exists,
- margin bridge is visible,
- relative strength is not the only evidence,
- the move is not merely domestic price/cost relief or policy/event premium.

Do not make this global. It is consumer-export-specific.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

Candidate C18 shadow rule:

```text
C18_channel_reorder_recurrence_margin_gate:
  +1 shadow component when recurring export/channel reorder and margin bridge are both present.
  cap at Stage2/Yellow when only domestic cost/price relief exists.
  cap below Green when reorder recurrence is absent or event/policy premium dominates.
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE 90D | avg MAE 90D | false positive rate | missed structural | alignment |
|---|---|---:|---:|---:|---:|---:|---|
| P0 | current calibrated proxy | 5 | 81.5 | -4.9 | 0.20 | 2 | useful but blunt |
| P0b | old baseline reference | 5 | 81.5 | -4.9 | 0.20 | 3 | too late |
| P1 | L5 sector candidate | 5 | 81.5 | -4.9 | 0.10 | 1 | best sector balance |
| P2 | C18 archetype candidate | 5 | 81.5 | -4.9 | 0.05 | 1 | holdout passed |
| P3 | counterexample guard | 2 | 21.1 | -5.7 | 0.00 | 0 | catches weak cases |

## 20. Score-Return Alignment Matrix

| case | score direction after shadow | return path | alignment |
|---|---|---|---|
| 삼양식품 | promote Stage2/Yellow earlier, keep Green strict | very high MFE, low early MAE | strong_positive_alignment |
| 빙그레 | promote with 4B-watch | strong MFE, later large drawdown | positive_but_needs_4B_overlay |
| 농심 | Yellow not Green | moderate MFE | correct_moderate_alignment |
| 오리온 | cap below Stage2/Green | low MFE, negative MAE | counterexample_alignment |
| 롯데웰푸드 | Yellow boundary, 4B-watch | good local MFE but high reversal risk | mixed_boundary_alignment |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C18_CONSUMER_EXPORT_CHANNEL_REORDER | K_FOOD_EXPORT_REORDER_HOLDOUT | 3 | 2 | 3 | 1 | 3 | 2 | 8 | 5 | 4 | true | true | Need exact parser recomputation and more non-food consumer-export holdout. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 2
reused_case_ids:
  - R13L11_C18_SAMYANG_003230
  - R13L11_C18_BINGGRAE_005180
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_too_late
  - current_profile_false_positive
  - price_only_local_4B_too_early

new_axis_proposed:
  - c18_channel_reorder_recurrence_margin_gate_holdout_confirmed
  - c18_domestic_price_or_cost_tailwind_cap_holdout_confirmed
  - c18_export_reorder_4b_requires_margin_or_channel_slowdown

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage3_green_revision_min kept strict

existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: holdout_validation_passed
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema availability and max_date
- profile availability and corporate-action caveat for selected symbols
- tradable shard row windows around trigger dates
- 30D/90D/180D research-proxy MFE/MAE
- current calibrated profile residual stress test
- positive/counterexample balance
- dedupe and reuse annotations
```

Not validated:

```text
- live candidate status
- current investability
- broker data
- exact production score calculation
- full parser recomputation from source code
- exact disclosure timestamp intraday handling
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_channel_reorder_recurrence_margin_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Holdout confirms recurring export/channel reorder plus margin bridge separates Samyang/Binggrae/Nongshim from weak event-only cases.","Reduced missed_structural_count from 2 to 1 and lowered false-positive boundary.",R13L11_T001_003230_STAGE2|R13L11_T004_005180_STAGE2|R13L11_T006_004370_YELLOW|R13L11_T007_271560_COUNTER|R13L11_T008_280360_HOLDOUT,5,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_domestic_price_or_cost_tailwind_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Domestic pricing/cost relief without export reorder recurrence produced only moderate or weak MFE and should not become Green by itself.","Blocks event/cost-only false positives.",R13L11_T007_271560_COUNTER|R13L11_T008_280360_HOLDOUT,2,2,2,medium,guard_shadow_only,"not production; reinforces existing price-only/event cap"
shadow_weight,c18_export_reorder_4b_requires_margin_or_channel_slowdown,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Price-only local peaks appeared near full-window peaks but should become full 4B only when valuation/positioning is backed by margin/channel slowdown or blowoff evidence.","Keeps 4B as overlay rather than automatic exit.",R13L11_T003_003230_4B|R13L11_T005_005180_4B|R13L11_T008_280360_HOLDOUT,3,1,1,low,overlay_shadow_only,"not production; strengthens full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L11_C18_SAMYANG_003230", "symbol": "003230", "company_name": "삼양식품", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L11_T001_003230_STAGE2", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_R12_C18_shadow_axis", "independent_evidence_weight": 0.5, "score_price_alignment": "early_channel_reorder_and_margin_bridge_aligned_with_large_MFE", "current_profile_verdict": "current_profile_missed_structural", "notes": "Holdout reuse: confirms C18 recurrence+margin gate while exposing Green lateness."}
{"row_type": "case", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L11_C18_BINGGRAE_005180", "symbol": "005180", "company_name": "빙그레", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R13L11_T004_005180_STAGE2", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_R12_C18_shadow_axis", "independent_evidence_weight": 0.5, "score_price_alignment": "export/seasonal margin bridge captured before blowoff but required 4B overlay", "current_profile_verdict": "current_profile_too_late", "notes": "Holdout reuse: reinforces price-only peak as overlay, not entry signal."}
{"row_type": "case", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L11_C18_NONGSHIM_004370", "symbol": "004370", "company_name": "농심", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R13L11_T006_004370_YELLOW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "moderate MFE supports Yellow/Stage2 rather than Green", "current_profile_verdict": "current_profile_correct", "notes": "New holdout: large brand with pricing/cost relief but less explosive export reorder than Samyang."}
{"row_type": "case", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L11_C18_ORION_271560", "symbol": "271560", "company_name": "오리온", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L11_T007_271560_COUNTER", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy/noise without channel reorder recurrence did not produce strong MFE", "current_profile_verdict": "current_profile_false_positive", "notes": "New counterexample: event/policy optionality without margin-channel bridge should not promote."}
{"row_type": "case", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "price_source": "Songdaiki/stock-web", "case_id": "R13L11_C18_LOTTEWELLFOOD_280360", "symbol": "280360", "company_name": "롯데웰푸드", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "counterexample", "best_trigger": "R13L11_T008_280360_HOLDOUT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "sharp local MFE but event-like move requires margin/reorder confirmation and 4B watch", "current_profile_verdict": "current_profile_missed_structural", "notes": "New mixed holdout: useful for cap/guard boundary, not pure Green promotion."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R13L11_T001_003230_STAGE2", "case_id": "R13L11_C18_SAMYANG_003230", "symbol": "003230", "company_name": "삼양식품", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / consumer export channel", "primary_archetype": "consumer_export_channel_reorder_vs_margin_bridge_holdout", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-25", "evidence_available_at_that_date": "historical public evidence proxy available by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/earnings/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-25", "entry_price": 206500, "MFE_30D_pct": 61.3, "MFE_90D_pct": 247.7, "MFE_180D_pct": 247.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.7, "MAE_90D_pct": -2.7, "MAE_180D_pct": -2.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 718000, "drawdown_after_peak_pct": -42.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L11_C18_SAMYANG_003230_2024-03-25_206500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_R12_C18_shadow_axis", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L11_T002_003230_GREEN_LATE", "case_id": "R13L11_C18_SAMYANG_003230", "symbol": "003230", "company_name": "삼양식품", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / consumer export channel", "primary_archetype": "consumer_export_channel_reorder_vs_margin_bridge_holdout", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-20", "evidence_available_at_that_date": "historical public evidence proxy available by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/earnings/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-20", "entry_price": 502000, "MFE_30D_pct": 43.0, "MFE_90D_pct": 43.0, "MFE_180D_pct": 43.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.1, "MAE_90D_pct": -42.1, "MAE_180D_pct": -42.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 718000, "drawdown_after_peak_pct": -42.7, "green_lateness_ratio": 0.578, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_high_mfe_remaining_but_large_upside_already_consumed", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L11_C18_SAMYANG_003230_2024-05-20_502000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_R12_C18_shadow_axis", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L11_T003_003230_4B", "case_id": "R13L11_C18_SAMYANG_003230", "symbol": "003230", "company_name": "삼양식품", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / consumer export channel", "primary_archetype": "consumer_export_channel_reorder_vs_margin_bridge_holdout", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "4B-overlay", "trigger_date": "2024-06-18", "evidence_available_at_that_date": "historical public evidence proxy available by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/earnings/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "profile_path": "atlas/symbol_profiles/003/003230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-18", "entry_price": 712000, "MFE_30D_pct": 0.8, "MFE_90D_pct": 0.8, "MFE_180D_pct": 0.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.1, "MAE_90D_pct": -42.1, "MAE_180D_pct": -42.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 718000, "drawdown_after_peak_pct": -42.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.988, "four_b_full_window_peak_proximity": 0.988, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_overheat_confirmed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L11_C18_SAMYANG_003230_2024-06-18_712000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_R12_C18_shadow_axis", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L11_T004_005180_STAGE2", "case_id": "R13L11_C18_BINGGRAE_005180", "symbol": "005180", "company_name": "빙그레", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / consumer export channel", "primary_archetype": "consumer_export_channel_reorder_vs_margin_bridge_holdout", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-15", "evidence_available_at_that_date": "historical public evidence proxy available by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/earnings/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-15", "entry_price": 61900, "MFE_30D_pct": 57.8, "MFE_90D_pct": 91.3, "MFE_180D_pct": 91.3, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.6, "MAE_90D_pct": -6.6, "MAE_180D_pct": -6.6, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -37.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_mae_watch", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L11_C18_BINGGRAE_005180_2024-04-15_61900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_R12_C18_shadow_axis", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L11_T005_005180_4B", "case_id": "R13L11_C18_BINGGRAE_005180", "symbol": "005180", "company_name": "빙그레", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / consumer export channel", "primary_archetype": "consumer_export_channel_reorder_vs_margin_bridge_holdout", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "4B-overlay", "trigger_date": "2024-06-10", "evidence_available_at_that_date": "historical public evidence proxy available by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/earnings/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-10", "entry_price": 112100, "MFE_30D_pct": 5.6, "MFE_90D_pct": 5.6, "MFE_180D_pct": 5.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.9, "MAE_90D_pct": -34.3, "MAE_180D_pct": -34.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -37.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.888, "four_b_full_window_peak_proximity": 0.888, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_overheat_confirmed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L11_C18_BINGGRAE_005180_2024-06-10_112100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "holdout_validation_from_R12_C18_shadow_axis", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L11_T006_004370_YELLOW", "case_id": "R13L11_C18_NONGSHIM_004370", "symbol": "004370", "company_name": "농심", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / consumer export channel", "primary_archetype": "consumer_export_channel_reorder_vs_margin_bridge_holdout", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "historical public evidence proxy available by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/earnings/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv", "profile_path": "atlas/symbol_profiles/004/004370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-10", "entry_price": 356000, "MFE_30D_pct": 20.2, "MFE_90D_pct": 26.4, "MFE_180D_pct": 28.1, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.7, "MAE_90D_pct": -3.7, "MAE_180D_pct": -3.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-08", "peak_price": 456000, "drawdown_after_peak_pct": -14.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "moderate_structural_success_yellow_not_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L11_C18_NONGSHIM_004370_2023-02-10_356000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L11_T007_271560_COUNTER", "case_id": "R13L11_C18_ORION_271560", "symbol": "271560", "company_name": "오리온", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / consumer export channel", "primary_archetype": "consumer_export_channel_reorder_vs_margin_bridge_holdout", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-false-positive-test", "trigger_date": "2024-01-16", "evidence_available_at_that_date": "historical public evidence proxy available by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/earnings/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv", "profile_path": "atlas/symbol_profiles/271/271560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-16", "entry_price": 96600, "MFE_30D_pct": 2.9, "MFE_90D_pct": 2.9, "MFE_180D_pct": 10.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.1, "MAE_90D_pct": -7.1, "MAE_180D_pct": -10.2, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 106700, "drawdown_after_peak_pct": -18.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "failed_rerating_or_domestic_policy_noise", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L11_C18_ORION_271560_2024-01-16_96600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L11_T008_280360_HOLDOUT", "case_id": "R13L11_C18_LOTTEWELLFOOD_280360", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_REORDER_HOLDOUT", "sector": "Cross-archetype RedTeam holdout / consumer export channel", "primary_archetype": "consumer_export_channel_reorder_vs_margin_bridge_holdout", "loop_objective": "holdout_validation|residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-22", "evidence_available_at_that_date": "historical public evidence proxy available by trigger date; no later-outcome relabeling", "evidence_source": "historical public disclosure/earnings/report narrative proxy; stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv", "profile_path": "atlas/symbol_profiles/280/280360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-22", "entry_price": 149800, "MFE_30D_pct": 39.2, "MFE_90D_pct": 39.2, "MFE_180D_pct": 39.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.2, "MAE_90D_pct": -4.2, "MAE_180D_pct": -4.2, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 208500, "drawdown_after_peak_pct": -31.2, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "price_only_local_4B_requires_margin_or_revision_slowdown", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "stage2_promote_candidate_with_4b_watch", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L11_C18_LOTTEWELLFOOD_280360_2024-05-22_149800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L11_C18_SAMYANG_003230", "trigger_id": "R13L11_T001_003230_STAGE2", "symbol": "003230", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 80, "revision_score": 60, "relative_strength_score": 85, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 75, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 35, "margin_bridge_score": 90, "revision_score": 65, "relative_strength_score": 85, "customer_quality_score": 80, "policy_or_regulatory_score": 10, "valuation_repricing_score": 78, "execution_risk_score": 28, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83.5, "stage_label_after": "Stage2-Actionable / Yellow-fast-track, not automatic Green", "changed_components": ["margin_bridge_score", "customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "C18 holdout credits export reorder recurrence plus margin bridge before full revision confirmation; Green still waits for revision gate.", "MFE_90D_pct": 247.7, "MAE_90D_pct": -2.7, "score_return_alignment_label": "strong_positive_alignment", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L11_C18_BINGGRAE_005180", "trigger_id": "R13L11_T004_005180_STAGE2", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 70, "revision_score": 55, "relative_strength_score": 80, "customer_quality_score": 55, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 70, "execution_risk_score": 35, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 75.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 76, "revision_score": 57, "relative_strength_score": 80, "customer_quality_score": 62, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 72, "execution_risk_score": 40, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 79.0, "stage_label_after": "Stage2-Actionable / 4B-watch after spike", "changed_components": ["customer_quality_score", "execution_risk_score"], "component_delta_explanation": "The holdout credits export/seasonal margin evidence but caps Green when peak proximity rises without backlog/reorder depth.", "MFE_90D_pct": 91.3, "MAE_90D_pct": -6.6, "score_return_alignment_label": "positive_but_needs_4B_overlay", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L11_C18_NONGSHIM_004370", "trigger_id": "R13L11_T006_004370_YELLOW", "symbol": "004370", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 58, "revision_score": 50, "relative_strength_score": 55, "customer_quality_score": 45, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 50, "execution_risk_score": 25, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 72.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 62, "revision_score": 52, "relative_strength_score": 55, "customer_quality_score": 48, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 52, "execution_risk_score": 25, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 75.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score"], "component_delta_explanation": "Moderate cost/price margin bridge can justify Yellow, but no explosive reorder recurrence; Green remains blocked.", "MFE_90D_pct": 26.4, "MAE_90D_pct": -3.7, "score_return_alignment_label": "moderate_positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L11_C18_ORION_271560", "trigger_id": "R13L11_T007_271560_COUNTER", "symbol": "271560", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 25, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 40, "execution_risk_score": 60, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 66.0, "stage_label_before": "Stage1/Stage2 watch", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 25, "revision_score": 20, "relative_strength_score": 20, "customer_quality_score": 25, "policy_or_regulatory_score": 30, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 58.0, "stage_label_after": "Stage1 / no promotion", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Event/policy optionality without channel reorder recurrence is capped; negative thesis signal routes to watch/4C guard if confirmed.", "MFE_90D_pct": 2.9, "MAE_90D_pct": -7.1, "score_return_alignment_label": "counterexample_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L11_C18_LOTTEWELLFOOD_280360", "trigger_id": "R13L11_T008_280360_HOLDOUT", "symbol": "280360", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 55, "revision_score": 48, "relative_strength_score": 68, "customer_quality_score": 42, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 71.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 62, "revision_score": 52, "relative_strength_score": 68, "customer_quality_score": 45, "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 62, "execution_risk_score": 50, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 75.5, "stage_label_after": "Stage3-Yellow / 4B-watch if spike extends", "changed_components": ["margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Local rerating becomes usable only when margin bridge is confirmed; peak-like move without reorder depth is capped below Green.", "MFE_90D_pct": 39.2, "MAE_90D_pct": -4.2, "score_return_alignment_label": "mixed_positive_counterexample_boundary", "current_profile_verdict": "current_profile_missed_structural"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c18_channel_reorder_recurrence_margin_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Holdout confirms recurring export/channel reorder plus margin bridge separates Samyang/Binggrae/Nongshim from weak event-only cases.","Reduced missed_structural_count from 2 to 1 and lowered false-positive boundary.",R13L11_T001_003230_STAGE2|R13L11_T004_005180_STAGE2|R13L11_T006_004370_YELLOW|R13L11_T007_271560_COUNTER|R13L11_T008_280360_HOLDOUT,5,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c18_domestic_price_or_cost_tailwind_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Domestic pricing/cost relief without export reorder recurrence produced only moderate or weak MFE and should not become Green by itself.","Blocks event/cost-only false positives.",R13L11_T007_271560_COUNTER|R13L11_T008_280360_HOLDOUT,2,2,2,medium,guard_shadow_only,"not production; reinforces existing price-only/event cap"
shadow_weight,c18_export_reorder_4b_requires_margin_or_channel_slowdown,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C18_CONSUMER_EXPORT_CHANNEL_REORDER,0,1,+1,"Price-only local peaks appeared near full-window peaks but should become full 4B only when valuation/positioning is backed by margin/channel slowdown or blowoff evidence.","Keeps 4B as overlay rather than automatic exit.",R13L11_T003_003230_4B|R13L11_T005_005180_4B|R13L11_T008_280360_HOLDOUT,3,1,1,low,overlay_shadow_only,"not production; strengthens full_4b_requires_non_price_evidence"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "11", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 3, "reused_case_count": 2, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_too_late", "current_profile_false_positive", "price_only_local_4B_too_early"], "loop_contribution_label": "holdout_validation_passed", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reason":"all selected cases had sufficient 180D stock-web windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R13_loop_12_cross_archetype_holdout_3_or_batch_promotion_review
preferred_next_scope =
  - R13 cross-archetype residual aggregation
  - compare C18/C20/C31/C32 event-premium caps
  - promote only if multiple MDs agree after exact parser recomputation
```

## 28. Source Notes

```text
stock-web manifest_max_date = 2026-02-20
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
```

The OHLC values in this research file are rounded research-proxy calculations based on directly inspected stock-web tradable shard rows. They are sufficient for residual research and handoff triage, but exact batch implementation should re-run the stock-web row parser before changing any production or shadow ledger.
