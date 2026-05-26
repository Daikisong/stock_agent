# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R7
loop = 10
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_DEMAND_QUALITY
output_file = e2r_stock_web_v12_residual_round_R7_loop_10_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop studies approval-to-commercialization residuals after the global stock-web calibration. The target is not to repeat the global Stage2/Green/4B rules, but to isolate a C23-specific separator: **approval headlines only work when the approval is tied to a credible commercialization route**.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Existing applied global axes are treated as the baseline. This MD proposes **shadow-only C23 refinements**, not production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION |
| fine_archetype_id | BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_DEMAND_QUALITY |
| loop_objective | residual_missed_structural_mining; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4C_thesis_break_timing_test; coverage_gap_fill |
| cases | 4 calibration-usable cases + 2 overlay trigger rows |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show R1-R13 and loops 1-9 already covered broad sectors, with 107 result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative rows. The applied global axes already include Stage2 actionable bonus, stricter Green, cross-evidence buffer, non-price 4B requirement and hard 4C routing. This loop avoids re-proposing those global rules and instead adds C23-specific residual separation.

Novelty check:

| metric | value |
|---|---:|
| calibration_usable_case_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| new_independent_case_ratio | 1.00 |
| new_symbol_count | 4 |
| new_trigger_family_count | 4 |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest was read as the price atlas basis.

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Manifest facts used by this MD:

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
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available | corp-action contamination in 180D | calibration_usable |
|---|---:|---|---:|---:|---:|
| R7L10_C23_000100_LAZCLUZE_FDA | 000100 | 2024-08-21 | true | false | true |
| R7L10_C23_196170_KEYTRUDA_SC_ROUTE | 196170 | 2024-02-23 | true | false | true |
| R7L10_C23_028300_HLB_FDA_CRL | 028300 | 2024-04-30 | true | false | true |
| R7L10_C23_302440_SKY_COVIONE_DEMAND_FADE | 302440 | 2022-06-29 | true | false | true |

Notes: 메지온 140410 was considered as an additional FDA-response counterexample, but symbol profile flags 2022-04-05 and 2022-04-25 corporate-action candidates overlapping the post-CRL window, so it is excluded from weight calibration in this loop.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | mapping reason |
|---|---|---|
| LAZERTINIB_US_FDA_APPROVAL_ROYALTY_COMMERCIALIZATION | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | approval plus global partner commercialization/royalty economics |
| GLOBAL_PHARMA_SC_FORMULATION_ROYALTY_OPTION | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | regulatory route and commercialization royalty option, not generic platform hype |
| FDA_BINARY_APPROVAL_EVENT_WITH_WEAK_COMMERCIAL_VISIBILITY | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | approval event premium without confirmed approval/commercial route |
| DOMESTIC_APPROVAL_WITH_WEAK_REORDER_DEMAND | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | approval headline but weak durable demand/reorder conversion |

## 7. Case Selection Summary

| case_id | symbol | role | positive_or_counterexample | best trigger | current_profile_verdict |
|---|---:|---|---|---|---|
| R7L10_C23_000100_LAZCLUZE_FDA | 000100 | structural_success | positive | FDA approval with launch economics | current_profile_missed_structural |
| R7L10_C23_196170_KEYTRUDA_SC_ROUTE | 196170 | structural_success | positive | Merck/Keytruda SC commercial route | current_profile_too_late |
| R7L10_C23_028300_HLB_FDA_CRL | 028300 | false_positive_green | counterexample | pre-PDUFA event premium | current_profile_false_positive |
| R7L10_C23_302440_SKY_COVIONE_DEMAND_FADE | 302440 | failed_rerating | counterexample | domestic vaccine approval | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| type | count |
|---|---:|
| positive_structural_success | 2 |
| counterexample_or_failed_rerating | 2 |
| 4B_or_4C_overlay_rows | 2 |
| calibration_usable_representative_rows | 4 |

## 9. Evidence Source Map

| symbol | event | evidence source note |
|---:|---|---|
| 000100 | FDA approval of Rybrevant + Lazcluze/lazertinib combination | Reuters 2024-08-20 and FDA/J&J approval materials; approval linked to launch and peak-sales frame |
| 196170 | Merck/Keytruda SC route and exclusivity/commercialization option | Merck/Alteogen license route; Reuters coverage of Keytruda SC development and launch economics |
| 028300 | FDA Complete Response Letter / failed approval route | Public CRL event; stock-web shows crash from pre-event premium |
| 302440 | SK bioscience SkyCovione domestic approval but later low-demand fade | MFDS/Korean approval and later suspension/low-demand reports |

## 10. Price Data Source Map

| symbol | profile_path | shard(s) used | corporate_action_window_status |
|---:|---|---|---|
| 000100 | atlas/symbol_profiles/000/000100.json | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv; 2025.csv | clean_180D_window |
| 196170 | atlas/symbol_profiles/196/196170.json | atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv | clean_180D_window |
| 028300 | atlas/symbol_profiles/028/028300.json | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | clean_180D_window |
| 302440 | atlas/symbol_profiles/302/302440.json | atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence | verdict |
|---|---:|---|---|---|---:|---|---|---|---|
| TR_R7L10_000100_2024-08-20_FDA_APPROVAL | 000100 | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94,300 | approval; global partner; regulatory optionality | revision; commercial launch; durable partner | none | missed structural |
| TR_R7L10_000100_2024-10-15_LOCAL_4B | 000100 | 4B-watch | 2024-10-15 | 2024-10-15 | 163,700 | none | none | valuation/positioning price-only local peak | correct 4B-watch |
| TR_R7L10_196170_2024-02-22_MERCK_EXCLUSIVE_AMENDMENT | 196170 | Stage2-Actionable | 2024-02-22 | 2024-02-23 | 131,200 | global partner route; commercialization optionality | durable customer; multiple public sources | none | too late under generic profile |
| TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM | 028300 | Stage2-Event-Premium | 2024-04-30 | 2024-04-30 | 111,200 | event premium; regulatory optionality | none | binary event cap | false positive risk |
| TR_R7L10_028300_2024-05-17_FDA_CRL_4C | 028300 | 4C | 2024-05-17 | 2024-05-17 | 67,100 | none | none | regulatory rejection; thesis break | hard 4C success |
| TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL | 302440 | Stage2-Approval | 2022-06-29 | 2022-06-29 | 109,000 | approval; policy optionality | none | demand/reorder weakness | failed rerating |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TR_R7L10_000100_2024-08-20_FDA_APPROVAL | 94,300 | 70.0% | -3.0% | 77.0% | -3.0% | 77.0% | -3.0% | 2024-10-15 | 166,900 | -39.8% |
| TR_R7L10_196170_2024-02-22_MERCK_EXCLUSIVE_AMENDMENT | 131,200 | 71.9% | -9.3% | 127.5% | -9.3% | 247.2% | -9.3% | 2024-11-11 | 455,500 | -39.8% |
| TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM | 111,200 | 2.8% | -59.4% | 2.8% | -59.4% | 2.8% | -59.4% | 2024-04-30 | 114,300 | -60.5% |
| TR_R7L10_028300_2024-05-17_FDA_CRL_4C | 67,100 | 10.0% | -32.7% | 46.2% | -32.7% | 46.2% | -32.7% | 2024-07-08 | 98,100 | -33.9% |
| TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL | 109,000 | 43.6% | -11.7% | 43.6% | -26.3% | 43.6% | -38.5% | 2022-07-13 | 156,500 | -56.4% |

## 13. Current Calibrated Profile Stress Test

| case | likely current profile action | outcome alignment | residual diagnosis |
|---|---|---|---|
| 000100 | Yellow/late Green unless revision gates quickly fill | too late/missed structural | C23 needs commercialization-quality boost when approval is tied to global launch economics |
| 196170 | Yellow due indirect regulatory route | too late | platform/royalty route can be real C23 when a mega-pharma product lifecycle is visible |
| 028300 | could over-score event momentum if approval expectation treated as event quality | false positive | approval expectation must not equal approval evidence |
| 302440 | approval headline may pass Yellow but not durable Green | false positive if Green | domestic approval without reorder visibility should be capped |

Answers to required v12 questions:

1. Current profile is broadly correct on price-only 4B/4C guardrails but too generic on C23 commercialization quality.
2. MFE/MAE shows two positive routes had strong 90D/180D MFE, while approval-only counterexamples had large adverse paths.
3. Stage2 bonus is not the issue; the issue is **which Stage2 approval events deserve promotion**.
4. Yellow 75 is acceptable as watch state.
5. Green 87/revision 55 is directionally right but needs a C23-specific commercialization bridge.
6. Price-only blowoff guard is appropriate and should be strengthened for binary biotech approval events.
7. Full 4B non-price requirement is appropriate.
8. Hard 4C routing is appropriate and timely for CRL/regulatory rejection.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3/Green proxy | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 000100 | 94,300 | about 114,000~120,000 | 0.28 | Green not extremely late if commercialization route recognized quickly |
| 196170 | 131,200 | about 190,000 | 0.18 | generic Green would be too late if it waited for full clinical/regulatory confirmation |
| 028300 | 111,200 | no valid Green | n/a | event premium should not be Green |
| 302440 | 109,000 | no valid Green | n/a | approval pop lacked durable demand conversion |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| TR_R7L10_000100_2024-10-15_LOCAL_4B | 1.00 | 1.00 | price_only; valuation_blowoff; positioning_overheat | 4B-watch, not automatic thesis break |
| TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM | 0.97 | 0.97 | valuation_blowoff; event premium | should cap positive promotion before approval |
| TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL | 0.35 | 0.35 | event premium; positioning | approval pop did not justify full Green |

## 16. 4C Protection Audit

| trigger_id | 4C evidence | protection label | comment |
|---|---|---|---|
| TR_R7L10_028300_2024-05-17_FDA_CRL_4C | regulatory_rejection; thesis_evidence_broken | hard_4c_success | CRL breaks approval-commercialization thesis and must route to 4C, not retrain positive entry weight |
| TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL | later demand fade | thesis_break_watch_only | not immediate 4C, but weak demand should cap Green promotion |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = biotech_binary_event_premium_cap
candidate = if approval is not yet granted and event premium is mostly PDUFA/binary expectation, cap at Stage2/Stage3-Yellow and attach 4B-watch overlay.
positive promotion requires non-price evidence: approval granted + commercial route + partner/reimbursement/demand visibility.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
axis = c23_commercialization_quality_gate
proposal = Add a C23-specific commercialization quality gate and optional boost.

Positive components:
- global pharma launch partner
- royalty/profit-share or product sales participation
- explicit peak-sales or market-size frame
- reimbursement / demand / reorder visibility
- regulator approval already granted, not merely expected

Negative/cap components:
- binary approval expectation only
- domestic approval without durable demand conversion
- CRL / regulatory rejection
- no reimbursement or reorder visibility
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE_90D | avg MAE_90D | false_positive_rate | missed_structural_count | score-return alignment |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 63.4% | -24.5% | 50% | 2 | mixed: generic approval events not separated |
| P0b e2r_2_0_baseline_reference | 4 | 63.4% | -24.5% | 50%+ | 2 | weaker due price/event vulnerability |
| P1 sector_specific_candidate_profile | 4 | 98.3% selected positives | -6.2% selected positives | 25% | 1 | improved |
| P2 canonical_archetype_candidate_profile | 4 | 98.3% selected positives | -6.2% selected positives | 0~25% | 0~1 | best C23 alignment |
| P3 counterexample_guard_profile | 4 | lower positive recall | better downside control | 0% | 1 | conservative but safe |

## 20. Score-Return Alignment Matrix

| trigger_id | score before | stage before | score after | stage after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| TR_R7L10_000100_2024-08-20_FDA_APPROVAL | 82 | Stage3-Yellow | 88 | Stage3-Green | 77.0% | -3.0% | improved by commercialization boost |
| TR_R7L10_196170_2024-02-22_MERCK_EXCLUSIVE_AMENDMENT | 80 | Stage3-Yellow | 88 | Stage3-Green | 127.5% | -9.3% | improved by global-pharma route recognition |
| TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM | 76 | Stage3-Yellow | 66 | Stage2/4B-watch | 2.8% | -59.4% | improved by binary event cap |
| TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL | 78 | Stage3-Yellow | 68 | Stage2/4B-watch | 43.6% | -26.3% | improved by demand/reorder cap |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_DEMAND_QUALITY | 2 | 2 | 2 | 1 | 4 | 0 | 6 | 4 | 3 | true | true | remaining gap: C24 trial-data event risk and C25 medical-device reimbursement |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage3_green_revision_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: approval_without_commercialization_false_positive; global_partner_royalty_route_missed_structural; binary_event_premium_false_green_risk
new_axis_proposed: c23_commercialization_quality_gate; biotech_binary_event_premium_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest/schema fields.
- symbol profiles for 000100, 196170, 028300, 302440, plus excluded 140410 caveat.
- 30D/90D/180D MFE/MAE using stock-web tradable raw OHLC rows.
- C23 positive/counterexample balance.

Not validated:

- No live scan.
- No current candidate recommendation.
- No production code or scoring implementation.
- No adjusted-price normalization.
- No broker API, no trading instruction.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_commercialization_quality_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Approval should promote only when paired with global partner launch economics, royalty/profit-share, durable demand or reimbursement visibility.","Separates 000100/196170 positives from 028300/302440 false positives.","TR_R7L10_000100_2024-08-20_FDA_APPROVAL|TR_R7L10_196170_2024-02-22_MERCK_EXCLUSIVE_AMENDMENT|TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM|TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,binary_fda_event_premium_cap,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"PDUFA/approval expectation alone is a 4B-watch overlay, not Stage3-Green evidence.","HLB pre-CRL row shows high MAE and poor score-return alignment when approval is not yet confirmed.","TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM",1,1,1,medium,sector_shadow_only,"strengthens price-only/event-premium guard for biotech approvals"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L10_C23_000100_LAZCLUZE_FDA", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_US_FDA_APPROVAL_ROYALTY_COMMERCIALIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R7L10_000100_2024-08-20_FDA_APPROVAL", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "approval_plus_partner_peak_sales_and_royalty_route_aligned_with_large_30D_90D_MFE", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Approval was not a pure binary pop; J&J launch/peak-sales frame made the commercialization route investable."}
{"row_type": "case", "case_id": "R7L10_C23_196170_KEYTRUDA_SC_ROUTE", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "GLOBAL_PHARMA_SC_FORMULATION_ROYALTY_OPTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR_R7L10_196170_2024-02-22_MERCK_EXCLUSIVE_AMENDMENT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "global_partner_exclusivity_and_regulatory_route_created_multi_month_rerating", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Regulatory/commercialization route was indirect but tied to Keytruda SC filing/launch economics rather than domestic approval headline only."}
{"row_type": "case", "case_id": "R7L10_C23_028300_HLB_FDA_CRL", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_BINARY_APPROVAL_EVENT_WITH_WEAK_COMMERCIAL_VISIBILITY", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "approval_expectation_without_hard_approval_and_commercial_quality_failed_with_large_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Pre-approval event premium should remain Yellow/4B-watch unless approval and commercialization evidence are both present."}
{"row_type": "case", "case_id": "R7L10_C23_302440_SKY_COVIONE_DEMAND_FADE", "symbol": "302440", "company_name": "SK바이오사이언스", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "DOMESTIC_APPROVAL_WITH_WEAK_REORDER_DEMAND", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "approval_pop_reversed_when_reorder_and_durable_demand_visibility_failed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Regulatory approval alone did not become durable commercialization; demand fade became the residual separator."}
{"row_type": "trigger", "trigger_id": "TR_R7L10_000100_2024-08-20_FDA_APPROVAL", "case_id": "R7L10_C23_000100_LAZCLUZE_FDA", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_US_FDA_APPROVAL_ROYALTY_COMMERCIALIZATION", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "approval_to_commercialization_royalty", "loop_objective": "residual_missed_structural_mining|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 94300, "evidence_available_at_that_date": "US FDA approval of J&J Rybrevant + lazertinib/Lazcluze combination; Yuhan royalty/commercialization exposure visible", "evidence_source": "Reuters 2024-08-20; FDA/J&J approval announcement; stock-web 000100 2024/2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv|atlas/ohlcv_tradable_by_symbol_year/000/000100/2025.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 70.0, "MFE_90D_pct": 77.0, "MFE_180D_pct": 77.0, "MFE_1Y_pct": 77.0, "MFE_2Y_pct": null, "MAE_30D_pct": -3.0, "MAE_90D_pct": -3.0, "MAE_180D_pct": -3.0, "MAE_1Y_pct": -3.0, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -39.8, "green_lateness_ratio": 0.28, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000100_2024-08-21_94300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R7L10_000100_2024-10-15_LOCAL_4B", "case_id": "R7L10_C23_000100_LAZCLUZE_FDA", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "LAZERTINIB_US_FDA_APPROVAL_ROYALTY_COMMERCIALIZATION", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "approval_to_commercialization_royalty", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "4B-watch", "trigger_date": "2024-10-15", "entry_date": "2024-10-15", "entry_price": 163700, "evidence_available_at_that_date": "local price blowoff after FDA approval; no hard non-price 4B thesis break at trigger", "evidence_source": "stock-web 000100 2024 shard; price-only overlay review", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.0, "MFE_90D_pct": 2.0, "MFE_180D_pct": 2.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.4, "MAE_90D_pct": -33.4, "MAE_180D_pct": -38.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -39.8, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000100_2024-10-15_163700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_4B_overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TR_R7L10_196170_2024-02-22_MERCK_EXCLUSIVE_AMENDMENT", "case_id": "R7L10_C23_196170_KEYTRUDA_SC_ROUTE", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "GLOBAL_PHARMA_SC_FORMULATION_ROYALTY_OPTION", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "commercialization_royalty_option", "loop_objective": "residual_missed_structural_mining|canonical_archetype_compression|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 131200, "evidence_available_at_that_date": "Merck/Keytruda SC route became more exclusive and commercially legible; later trial/regulatory path confirmed route quality", "evidence_source": "public Merck/Alteogen license news; Reuters 2024/2025 Keytruda SC coverage; stock-web 196170 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation", "confirmed_revision"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 71.9, "MFE_90D_pct": 127.5, "MFE_180D_pct": 247.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.3, "MAE_90D_pct": -9.3, "MAE_180D_pct": -9.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-11-11", "peak_price": 455500, "drawdown_after_peak_pct": -39.8, "green_lateness_ratio": 0.18, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "196170_2024-02-23_131200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM", "case_id": "R7L10_C23_028300_HLB_FDA_CRL", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_BINARY_APPROVAL_EVENT_WITH_WEAK_COMMERCIAL_VISIBILITY", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "binary_approval_event_risk", "loop_objective": "counterexample_mining|residual_false_positive_mining|4C_thesis_break_timing_test", "trigger_type": "Stage2-Event-Premium", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 111200, "evidence_available_at_that_date": "approval expectation and event premium before FDA decision; hard approval and commercialization not yet confirmed", "evidence_source": "stock-web 028300 2024 shard; FDA CRL public event on 2024-05-17", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.8, "MFE_90D_pct": 2.8, "MFE_180D_pct": 2.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -59.4, "MAE_90D_pct": -59.4, "MAE_180D_pct": -59.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-30", "peak_price": 114300, "drawdown_after_peak_pct": -60.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "event_premium_should_be_4B_watch_not_positive_green", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_success_after_CRL", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "028300_2024-04-30_111200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR_R7L10_028300_2024-05-17_FDA_CRL_4C", "case_id": "R7L10_C23_028300_HLB_FDA_CRL", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_BINARY_APPROVAL_EVENT_WITH_WEAK_COMMERCIAL_VISIBILITY", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "binary_approval_event_risk", "loop_objective": "4C_thesis_break_timing_test", "trigger_type": "4C", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 67100, "evidence_available_at_that_date": "Complete Response Letter / approval failure breaks the approval-commercialization thesis", "evidence_source": "public CRL event; stock-web 028300 2024 shard", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken", "forced_liquidation_or_crash"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.0, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.7, "MAE_90D_pct": -32.7, "MAE_180D_pct": -32.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -33.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "028300_2024-05-17_67100", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_4C_overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL", "case_id": "R7L10_C23_302440_SKY_COVIONE_DEMAND_FADE", "symbol": "302440", "company_name": "SK바이오사이언스", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "DOMESTIC_APPROVAL_WITH_WEAK_REORDER_DEMAND", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "approval_without_durable_demand", "loop_objective": "counterexample_mining|sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage2-Approval", "trigger_date": "2022-06-29", "entry_date": "2022-06-29", "entry_price": 109000, "evidence_available_at_that_date": "Korea approval of first homegrown COVID vaccine; durable global reorder and demand visibility not confirmed", "evidence_source": "MFDS/SK Bioscience public approval; stock-web 302440 2022 shard; later demand-fade news", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv", "profile_path": "atlas/symbol_profiles/302/302440.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 43.6, "MFE_90D_pct": 43.6, "MFE_180D_pct": 43.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.7, "MAE_90D_pct": -26.3, "MAE_180D_pct": -38.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-07-13", "peak_price": 156500, "drawdown_after_peak_pct": -56.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.35, "four_b_timing_verdict": "approval_pop_without_reorder_visibility_not_full_green", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "302440_2022-06-29_109000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C23_shadow", "case_id": "R7L10_C23_000100_LAZCLUZE_FDA", "trigger_id": "TR_R7L10_000100_2024-08-20_FDA_APPROVAL", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 72, "relative_strength_score": 65, "customer_quality_score": 86, "policy_or_regulatory_score": 95, "valuation_repricing_score": 68, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 78, "relative_strength_score": 65, "customer_quality_score": 90, "policy_or_regulatory_score": 95, "valuation_repricing_score": 70, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "commercialization_score": 88, "royalty_route_score": 82}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score", "commercialization_score", "royalty_route_score"], "component_delta_explanation": "Add commercialization/royalty route score when approval belongs to a global pharma launch with explicit peak-sales framing.", "MFE_90D_pct": 77.0, "MAE_90D_pct": -3.0, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C23_shadow", "case_id": "R7L10_C23_196170_KEYTRUDA_SC_ROUTE", "trigger_id": "TR_R7L10_196170_2024-02-22_MERCK_EXCLUSIVE_AMENDMENT", "symbol": "196170", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 58, "relative_strength_score": 78, "customer_quality_score": 92, "policy_or_regulatory_score": 70, "valuation_repricing_score": 70, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 70, "relative_strength_score": 78, "customer_quality_score": 95, "policy_or_regulatory_score": 78, "valuation_repricing_score": 74, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "commercialization_score": 86, "royalty_route_score": 92}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["revision_score", "customer_quality_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "commercialization_score", "royalty_route_score"], "component_delta_explanation": "Treat global-pharma exclusive SC formulation route as C23 commercialization option, not generic biotech theme.", "MFE_90D_pct": 127.5, "MAE_90D_pct": -9.3, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C23_shadow", "case_id": "R7L10_C23_028300_HLB_FDA_CRL", "trigger_id": "TR_R7L10_028300_2024-04-30_PRE_PDUFA_EVENT_PREMIUM", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 42, "relative_strength_score": 88, "customer_quality_score": 35, "policy_or_regulatory_score": 72, "valuation_repricing_score": 28, "execution_risk_score": 75, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 42, "relative_strength_score": 88, "customer_quality_score": 35, "policy_or_regulatory_score": 72, "valuation_repricing_score": 28, "execution_risk_score": 85, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "binary_event_risk_score": 95}, "weighted_score_after": 66, "stage_label_after": "Stage2/4B-watch", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score", "binary_event_risk_score"], "component_delta_explanation": "Counterexample guard: binary approval expectation cannot become Green without approval + commercialization quality.", "MFE_90D_pct": 2.8, "MAE_90D_pct": -59.4, "score_return_alignment_label": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_vs_C23_shadow", "case_id": "R7L10_C23_302440_SKY_COVIONE_DEMAND_FADE", "trigger_id": "TR_R7L10_302440_2022-06-29_DOMESTIC_APPROVAL", "symbol": "302440", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 90, "valuation_repricing_score": 38, "execution_risk_score": 48, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 42, "relative_strength_score": 70, "customer_quality_score": 38, "policy_or_regulatory_score": 90, "valuation_repricing_score": 30, "execution_risk_score": 62, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reorder_demand_score": 18}, "weighted_score_after": 68, "stage_label_after": "Stage2/4B-watch", "changed_components": ["revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score", "reorder_demand_score"], "component_delta_explanation": "Domestic approval without durable demand/reorder evidence should be capped below positive Green.", "MFE_90D_pct": 43.6, "MAE_90D_pct": -26.3, "score_return_alignment_label": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["approval_without_commercialization_false_positive", "global_partner_royalty_route_missed_structural", "binary_event_premium_false_green_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = R7_loop_11_or_C24_BIO_TRIAL_DATA_EVENT_RISK
preferred_next_scope = L7_BIO_HEALTHCARE_MEDICAL / C24_BIO_TRIAL_DATA_EVENT_RISK
reason = C23 approval-commercialization quality has positive/counterexample balance; next gap is trial-data binary event risk.
```

## 28. Source Notes

- Stock-Web manifest/schema: Songdaiki/stock-web atlas/manifest.json and atlas/schema.json.
- 000100 OHLC: atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv and 2025.csv.
- 196170 OHLC: atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv.
- 028300 OHLC: atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv.
- 302440 OHLC: atlas/ohlcv_tradable_by_symbol_year/302/302440/2022.csv.
- Evidence notes: Reuters 2024-08-20 FDA approval coverage for Rybrevant + Lazcluze; Reuters Merck Keytruda SC development coverage; public HLB CRL event; MFDS/SK Bioscience SkyCovione approval and later demand-fade reports.
