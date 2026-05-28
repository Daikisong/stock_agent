# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
repo_session = later_batch_implementation_only
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

- round: `R7`
- loop: `43`
- large_sector_id: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical_archetype_id: `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`
- fine_archetype_id:
  - `FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION`
  - `US_BIOLOGIC_APPROVAL_TO_COMMERCIAL_LAUNCH`
  - `REGULATORY_EXPECTATION_TO_CRL_4C`
- loop_objective:
  - `coverage_gap_fill`
  - `counterexample_mining`
  - `residual_false_positive_mining`
  - `sector_specific_rule_discovery`
  - `canonical_archetype_compression`
  - `4B_non_price_requirement_stress_test`
  - `4C_thesis_break_timing_test`

This MD is historical calibration research only. It is not current/live candidate discovery, not an investment recommendation, not a trading instruction, and not a `stock_agent` code patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
```

Assumed current calibrated axes:

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

The purpose here is not to re-prove those global axes. The residual question is narrower:

> In bio/healthcare, should the model distinguish **actual regulatory approval with commercialization bridge** from **pending approval / event premium without label clearance** more explicitly at the C23 canonical-archetype level?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| large_sector_id | `L7_BIO_HEALTHCARE_MEDICAL` |
| canonical_archetype_id | `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` |
| sector | 바이오·헬스케어·의료기기 |
| primary_archetype | regulatory approval / commercialization bridge |
| positive target | approval label + commercialization / royalty / launch path |
| counterexample target | regulatory expectation / PDUFA-like event premium without actual approval, later CRL or thesis break |

The canonical compression map intentionally keeps the rule at C23 rather than splitting every drug modality into its own production archetype. Fine archetypes are retained as research descriptors only.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifact read scope was limited to calibration reports and registry-style outputs. The ingest summary shows existing calibration material across R1-R13, 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows. This establishes that prior broad calibration exists, but exact search for `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` returned no direct match in the accessible search index.

```text
allowed_artifact_checked = reports/e2r_calibration/ingest_summary.md
stock_agent_code_accessed = false
src/e2r_accessed = false
production_patch_written = false
```

Duplicate avoidance conclusion:

```text
auto_selected_coverage_gap = L7/C23 regulatory approval commercialization bridge coverage; actual approval vs pending-review false positive separation
same_symbol_same_trigger_reuse = false
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

The price atlas validation is based on `Songdaiki/stock-web` manifest and symbol profiles.

| manifest field | observed value |
|---|---|
| source_name | `FinanceData/marcap` |
| source_repo_url | `https://github.com/FinanceData/marcap` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| min_date | `1995-05-02` |
| max_date | `2026-02-20` |
| tradable_row_count | `14354401` |
| raw_row_count | `15214118` |
| symbol_count | `5414` |
| active_like_symbol_count | `2868` |
| inactive_or_delisted_like_symbol_count | `2546` |
| markets | `KONEX`, `KOSDAQ`, `KOSDAQ GLOBAL`, `KOSPI` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| schema_path | `atlas/schema.json` |
| universe_path | `atlas/universe/all_symbols.csv` |

Important validation caveat:

```text
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_contaminated_window_policy = block_by_default
```

## 5. Historical Eligibility Gate

| case_id | symbol | company | trigger anchor | entry_date | 180D forward window | profile corporate-action overlap | calibration_usable |
|---|---:|---|---|---|---:|---|---|
| C23_YUHAN_FDA_APPROVAL_2024 | 000100 | 유한양행 | FDA approval / J&J Rybrevant+Lazcluze approval | 2024-08-21 | available | none in 2024-08~2025-05 | true |
| C23_HUGEL_LETYBO_FDA_2024 | 145020 | 휴젤 | U.S. Letybo approval / launch bridge | 2024-03-04 | available | none in 2024-03~2024-11 | true |
| C23_HLB_CRL_2024 | 028300 | HLB | FDA CRL / approval failure | 2024-05-17 | available | none in 2024-05~2025-02 | true |
| C23_CELLTRION_ZYMFENTRA_BLOCKED_2023 | 068270 | 셀트리온 | Zymfentra approval | 2023-10-23 | available | 2024-01-12 inside 180D window | false / narrative_only |

Celltrion is useful as a narrative-only validation warning: the event is relevant to C23, but the stock-web profile marks a corporate-action candidate inside the forward window, so the row is blocked from quantitative calibration.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Actual label approval can convert old R&D optionality into royalty/commercial launch evidence. |
| US_BIOLOGIC_APPROVAL_TO_COMMERCIAL_LAUNCH | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Biologic/aesthetic drug approval matters only if paired with credible launch/channel monetization. |
| REGULATORY_EXPECTATION_TO_CRL_4C | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | Pending review without label is not approval evidence; CRL is thesis break / 4C route. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | best_trigger | new independent? | notes |
|---|---:|---|---|---|---|---|---|
| C23_YUHAN_FDA_APPROVAL_2024 | 000100 | 유한양행 | structural_success | positive | YUHAN_STAGE2_APPROVAL_2024_08_21 | true | FDA-approved lazertinib combo created label + royalty/commercialization bridge. |
| C23_HUGEL_LETYBO_FDA_2024 | 145020 | 휴젤 | structural_success / high_mae_success | positive | HUGEL_STAGE2_APPROVAL_2024_03_04 | true | Approval worked, but early MAE was deep before launch/volume rerating closed. |
| C23_HLB_CRL_2024 | 028300 | HLB | failed_rerating / 4C_late | counterexample | HLB_4C_CRL_2024_05_17 | true | Pending approval/event premium is not approval evidence; CRL routes to 4C. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
counterexample_search_incomplete = false
positive_case_missing = false
```

Interpretation:

- Positive C23 examples were strongest when approval label was coupled with a believable monetization bridge: royalty economics, named partner, launch route, or already commercialized overseas product entering a new jurisdiction.
- Counterexample pressure came from approval expectation that looked large in market cap terms before the label was actually granted. A pending review is a door with a nameplate on it, not an open door.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | evidence class |
|---|---|---|---|
| C23_YUHAN_FDA_APPROVAL_2024 | U.S. FDA approved J&J's Rybrevant + lazertinib for first-line EGFR-mutated NSCLC; Reuters reported the decision on 2024-08-20 and described late-stage evidence versus Tagrisso plus J&J peak-sales expectations. | Reuters, 2024-08-20; Barron's, 2024-08-20 | actual approval + partner commercialization bridge |
| C23_HUGEL_LETYBO_FDA_2024 | Letybo / letibotulinumtoxinA was FDA-approved in the U.S. in February 2024; later consumer/dermatology coverage described U.S. availability and Hugel as manufacturer. | FDA-derived drug references; Allure, 2025-03-07 | actual approval + U.S. aesthetic launch bridge |
| C23_HLB_CRL_2024 | Market-recognized HLB regulatory failure/CRL event around 2024-05-17. This source line is marked for later ingestion validation because web search in this run did not retrieve a primary company/agency page. | source_validation_needed; stock-web price shock verified | CRL / thesis break / approval failure |
| C23_CELLTRION_ZYMFENTRA_BLOCKED_2023 | Celltrion USA announced FDA approval of Zymfentra on 2023-10-22. | Celltrion announcement summarized in public drug reference | narrative_only because stock-web corporate-action candidate overlaps 180D window |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | corporate_action_window_status |
|---:|---|---|---|---|
| 000100 | 유한양행 | `atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv`; `.../2025.csv` | `atlas/symbol_profiles/000/000100.json` | clean_180D_window |
| 145020 | 휴젤 | `atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv` | `atlas/symbol_profiles/145/145020.json` | clean_180D_window |
| 028300 | HLB | `atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv`; `.../2025.csv` | `atlas/symbol_profiles/028/028300.json` | clean_180D_window |
| 068270 | 셀트리온 | `atlas/ohlcv_tradable_by_symbol_year/068/068270/2023.csv`; `.../2024.csv` | `atlas/symbol_profiles/068/068270.json` | blocked: corporate-action candidate 2024-01-12 inside 180D |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence | aggregate role |
|---|---|---|---|---|---:|---|---|---|---|---|
| YUHAN_STAGE2_APPROVAL_2024_08_21 | C23_YUHAN_FDA_APPROVAL_2024 | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94,300 | public_event_or_disclosure; customer_or_order_quality; policy_or_regulatory_optionality; early_revision_signal | financial_visibility partial | none | none | representative |
| YUHAN_STAGE3_GREEN_2024_08_28 | C23_YUHAN_FDA_APPROVAL_2024 | Stage3-Green | 2024-08-28 | 2024-08-28 | 135,500 | same approval evidence | confirmed_revision proxy; multiple_public_sources; durable_customer_confirmation | none | none | label_comparison_only |
| YUHAN_4B_PRICE_ONLY_2024_10_15 | C23_YUHAN_FDA_APPROVAL_2024 | 4B-overlay | 2024-10-15 | 2024-10-15 | 163,700 | none | none | price_only; valuation_blowoff | none | 4B_overlay_only |
| HUGEL_STAGE2_APPROVAL_2024_03_04 | C23_HUGEL_LETYBO_FDA_2024 | Stage2-Actionable | 2024-02-29 | 2024-03-04 | 202,500 | public_event_or_disclosure; policy_or_regulatory_optionality | financial_visibility partial | none | none | representative |
| HUGEL_STAGE3_GREEN_2024_06_11 | C23_HUGEL_LETYBO_FDA_2024 | Stage3-Green | 2024-06-11 | 2024-06-11 | 242,000 | approval bridge | repeat_order_or_conversion proxy; financial_visibility; multiple_public_sources | none | none | label_comparison_only |
| HLB_4C_CRL_2024_05_17 | C23_HLB_CRL_2024 | 4C | 2024-05-17 | 2024-05-17 | 67,100 | none | none | positioning_overheat prior; event premium | regulatory_rejection; thesis_evidence_broken | representative |
| HLB_PRE_CRL_EXPECTATION_STRESS_2024_05_16 | C23_HLB_CRL_2024 | Stage3 false-positive stress | 2024-05-16 | 2024-05-16 | 95,800 | public_event_or_disclosure pending-review only; relative_strength | no actual approval label | positioning_overheat | none yet | label_comparison_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger rows

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | below_entry_30D | below_entry_90D |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---|
| YUHAN_STAGE2_APPROVAL_2024_08_21 | 2024-08-21 | 94,300 | 69.99 | -2.97 | 76.99 | -2.97 | 76.99 | -2.97 | 2024-10-15 | 166,900 | -39.84 | false | false |
| HUGEL_STAGE2_APPROVAL_2024_03_04 | 2024-03-04 | 202,500 | 8.15 | -14.91 | 29.63 | -14.91 | 60.99 | -14.91 | 2024-11-07 | 326,000 | -21.93 | true | true |
| HLB_4C_CRL_2024_05_17 | 2024-05-17 | 67,100 | 9.99 | -32.71 | 46.20 | -32.71 | 46.20 | -32.71 | 2024-07-08 | 98,100 | -40.06 | true | true |

### 12.2 Label comparison / overlay rows

| trigger_id | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | purpose |
|---|---|---:|---:|---:|---|
| YUHAN_STAGE3_GREEN_2024_08_28 | 2024-08-28 | 135,500 | 23.17 | -19.56 | Green lateness comparison; not aggregate representative. |
| YUHAN_4B_PRICE_ONLY_2024_10_15 | 2024-10-15 | 163,700 | 1.95 | -33.23 | 4B price-only/local peak stress; not full 4B without non-price evidence. |
| HUGEL_STAGE3_GREEN_2024_06_11 | 2024-06-11 | 242,000 | 10.12 | -11.16 | Green comparison; high-MAE but still structural. |
| HLB_PRE_CRL_EXPECTATION_STRESS_2024_05_16 | 2024-05-16 | 95,800 | 2.40 | -52.87 | Pending-review false-positive stress; not positive promotion. |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 expected judgment | actual price alignment | current_profile_verdict | residual lesson |
|---|---|---|---|---|
| C23_YUHAN_FDA_APPROVAL_2024 | Stage2-Actionable acceptable; Green only after cross evidence / revision bridge. | Strong 30D/90D/180D MFE with shallow representative MAE. | current_profile_correct | Actual approval plus named partner / commercial route deserves C23-specific positive shadow bonus. |
| C23_HUGEL_LETYBO_FDA_2024 | Stage2-Actionable acceptable, but high early MAE argues against immediate Green. | 30D MAE was deep, but 180D MFE reached +60.99%. | current_profile_too_late for full rerating, correct to avoid immediate Green | C23 approvals can be high-MAE successes before launch channel closes. |
| C23_HLB_CRL_2024 | Hard 4C should route to 4C once CRL appears; pending-review without approval should not be Green. | CRL day and subsequent window carried severe downside and volatile rebounds. | current_profile_false_positive risk before CRL; current_profile_4C_too_late on CRL day | Add C23 pending-review-without-label guard; pending regulatory event is not approval evidence. |

Stress-test answers:

```text
1. current profile handles actual approval reasonably but lacks explicit C23 pending-review guard.
2. actual MFE/MAE supports approval label + commercialization bridge as a distinct positive evidence cluster.
3. Stage2 bonus is appropriate for actual approval, risky for pending review only.
4. Yellow threshold 75 is broadly appropriate; C23 may need evidence composition not pure total relaxation.
5. Green threshold 87 / revision 55 is still useful, but C23 actual label + launch route can justify earlier Green than pure financial revision.
6. price-only blowoff guard remains appropriate.
7. full 4B non-price requirement remains appropriate.
8. hard 4C routing is correct but may be too late when the only preceding evidence is pending review/event premium.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3 Green entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| C23_YUHAN_FDA_APPROVAL_2024 | 94,300 | 135,500 | 166,900 | 0.57 | Green captured only after more than half the move from Stage2 to peak; not fatal, but somewhat late. |
| C23_HUGEL_LETYBO_FDA_2024 | 202,500 | 242,000 | 326,000 | 0.32 | Green was moderately late but still left meaningful upside. |
| C23_HLB_CRL_2024 | not applicable | not applicable | not applicable | not_applicable | no valid positive Green trigger; pending review is watch/risk, not approval. |

C23-specific implication:

```text
Do not lower global Green threshold. Instead, add a C23 composition bonus when approval_label_confirmed + commercialization_bridge_confirmed are both present.
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| YUHAN_4B_PRICE_ONLY_2024_10_15 | price_only; valuation_blowoff | 1.00 | 1.00 | price-only peak was close to full observed peak, but without non-price deterioration it remains overlay/watch, not automatic full 4B. |
| HLB_PRE_CRL_EXPECTATION_STRESS_2024_05_16 | positioning_overheat; event_premium | 0.98 | 0.98 | pending approval event premium should not be treated as positive Green; it is a 4B/4C watch state until label arrives or breaks. |

## 16. 4C Protection Audit

| case_id | 4C trigger | prior-stage price proxy | 4C entry price | worst low after 4C | four_c_protection_score | label |
|---|---|---:|---:|---:|---:|---|
| C23_HLB_CRL_2024 | HLB_4C_CRL_2024_05_17 | 95,800 | 67,100 | 45,150 | 0.38 | hard_4c_late |

Explanation:

The CRL did route to 4C, but the signal arrived with a gap-down already embedded. For C23, the earlier guard should be the absence of actual approval label despite event premium. In other words, the model needs a pre-CRL “do not call this Green” rail, not only a post-CRL thesis-break rail.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
axis = L7_regulatory_label_commercialization_bridge
baseline_value = 0
shadow_tested_value = +1.0 to +1.5
proposal_type = sector_shadow_only
```

Sector-specific rule candidate:

> In L7, actual regulatory label approval should receive positive shadow weight only when accompanied by at least one commercialization bridge: named partner economics, royalty/milestone route, U.S./EU launch route, reimbursement / channel preparation, or repeated post-approval public evidence.

Counter-rail:

> Pending review, PDUFA date, NDA/BLA acceptance, or advisory/event premium without label approval cannot by itself promote to Stage3-Green. It can be Stage2 watch or 4B risk overlay depending on price/positioning.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
axis_1 = C23_approval_label_confirmed_bonus
axis_2 = C23_pending_review_without_label_guard
axis_3 = C23_CRL_immediate_4C_thesis_break
```

Candidate C23 shadow profile:

| axis | direction | reason |
|---|---:|---|
| C23_approval_label_confirmed_bonus | +1.0 | Yuhan and Hugel show approval label can unlock non-price, non-price-only rerating. |
| C23_commercialization_bridge_bonus | +0.5 | Approval matters more when tied to named partner/launch/royalty/channel bridge. |
| C23_pending_review_without_label_guard | negative guard | HLB-like setups should not be Green before label. |
| C23_CRL_immediate_4C_thesis_break | strengthen existing 4C | CRL breaks the C23 thesis; route to 4C even if price later rebounds. |

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_trigger_count | selected representative triggers | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | none | 3 | Yuhan; Hugel; HLB | 50.94 | -16.86 | 61.39 | -16.86 | 0.33 | 1 | Good global guard, but C23 pending-review distinction incomplete. |
| P0b_e2r_2_0_baseline_reference | rollback | looser Stage2/Green; weaker 4C routing | 3 | same | 50.94 | -16.86 | 61.39 | -16.86 | 0.67 | 1 | More likely to over-promote HLB-style event premium. |
| P1_L7_sector_specific_candidate | sector shadow | label+commercial bridge +1; pending-review guard | 3 | Yuhan; Hugel; HLB as 4C | 50.94 | -16.86 | 61.39 | -16.86 | 0.00 | 0 | Better evidence composition; no global threshold change. |
| P2_C23_archetype_candidate | archetype shadow | approval label + commercialization bridge; CRL hard 4C | 3 | same | 50.94 | -16.86 | 61.39 | -16.86 | 0.00 | 0 | Best explanatory fit for C23. |
| P3_counterexample_guard_profile | guard | pending-review-without-label blocks Green | 3 | same | 50.94 | -16.86 | 61.39 | -16.86 | 0.00 | 0 | Keeps approval expectation in watch/risk mode until label arrives. |

## 20. Score-Return Alignment Matrix

| case_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | score_return_alignment_label |
|---|---|---:|---|---|---:|---|---|
| C23_YUHAN_FDA_APPROVAL_2024 | contract 45; backlog 10; margin 20; revision 50; RS 70; customer 85; regulatory 90; valuation 65; execution risk 25; legal risk 10; dilution 0; trust 0 | 84 | Stage3-Yellow / near Green | regulatory 95; customer 90; commercialization bridge +; revision 55 | 88 | Stage3-Green | aligned_positive |
| C23_HUGEL_LETYBO_FDA_2024 | contract 20; backlog 5; margin 35; revision 45; RS 55; customer 60; regulatory 90; valuation 45; execution risk 35; legal risk 10; dilution 0; trust 0 | 78 | Stage3-Yellow | regulatory 95; commercialization bridge +; channel launch + | 84 | Stage3-Yellow/Actionable | high_MAE_success_not_immediate_green |
| C23_HLB_CRL_2024 | contract 10; backlog 0; margin unknown; revision 40; RS 85; customer unknown; regulatory pending 50; valuation 85; execution risk 65; legal risk 35; dilution 0; trust 0 | 76 | false Stage3-Yellow risk | regulatory 0; thesis_break 100; legal/contract risk 80 | 38 | 4C | counterexample_guard_aligned |

Canonical component keys used in each score simulation row:

```text
contract_score
backlog_visibility_score
margin_bridge_score
revision_score
relative_strength_score
customer_quality_score
policy_or_regulatory_score
valuation_repricing_score
execution_risk_score
legal_or_contract_risk_score
dilution_cb_risk_score
accounting_trust_risk_score
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION; US_BIOLOGIC_APPROVAL_TO_COMMERCIAL_LAUNCH; REGULATORY_EXPECTATION_TO_CRL_4C | 2 | 1 | 1 | 1 | 3 | 0 | 7 | 3 | 1 | true | true | Still needs more C23 holdout cases and non-Korea approval/commercial launch examples; enough for shadow-only candidate, not global promotion. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
calibration_usable_case_count: 3
calibration_usable_trigger_count: 7
representative_trigger_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - pending_review_without_actual_approval_false_positive_risk
  - hard_4c_arrives_after_gap_down
new_axis_proposed:
  - C23_approval_label_confirmed_bonus
  - C23_commercialization_bridge_bonus
  - C23_pending_review_without_label_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: high; new sector/canonical focus relative to previous L5/C20 output, 3 new symbols, positive/counterexample balance satisfied
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L7/C23 regulatory approval commercialization bridge; actual approval vs pending-review false positive separation
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date, source, adjustment status, shard roots
- symbol profile availability and corporate-action candidate windows
- actual tradable OHLC rows for representative entry/peak/drawdown windows
- MFE/MAE calculations from stock-web tradable_raw rows
- C23 positive/counterexample balance
- same_entry_group / aggregate representative separation
```

Not validated in this research run:

```text
- production stock_agent scoring implementation
- src/e2r code behavior
- live candidate state
- current investment attractiveness
- broker/execution logic
- full source ingestion of HLB primary CRL document URL; marked source_validation_needed
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C23_approval_label_confirmed_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Actual FDA approval label separated Yuhan/Hugel positives from HLB pending-review failure","Improves positive selectivity without changing global Green threshold","YUHAN_STAGE2_APPROVAL_2024_08_21|HUGEL_STAGE2_APPROVAL_2024_03_04",3,3,1,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C23_commercialization_bridge_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,0.5,+0.5,"Approval label works best when tied to partner/royalty/launch bridge","Explains stronger Yuhan rerating and Hugel delayed but positive path","YUHAN_STAGE2_APPROVAL_2024_08_21|HUGEL_STAGE2_APPROVAL_2024_03_04",3,3,1,low_to_medium,archetype_shadow_only,"not production; needs more C23 holdout"
shadow_weight,C23_pending_review_without_label_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Pending review or event premium without actual approval label should not promote Green","Reduces HLB-style false positive risk before CRL","HLB_PRE_CRL_EXPECTATION_STRESS_2024_05_16|HLB_4C_CRL_2024_05_17",3,3,1,medium,counterexample_guard,"not production; complements price-only guard"
shadow_weight,C23_CRL_immediate_4C_thesis_break,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,1,1.25,+0.25,"CRL is a hard thesis break in approval commercialization archetype","Routes broken approval thesis to 4C even when rebounds occur","HLB_4C_CRL_2024_05_17",3,3,1,medium,existing_axis_strengthened,"strengthens hard_4c_thesis_break_routes_to_4c only within C23"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C23_YUHAN_FDA_APPROVAL_2024","symbol":"000100","company_name":"유한양행","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"YUHAN_STAGE2_APPROVAL_2024_08_21","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"actual approval label plus commercialization bridge aligned with strong 90D/180D MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C23 approval-label positive; Green somewhat late but acceptable."}
{"row_type":"case","case_id":"C23_HUGEL_LETYBO_FDA_2024","symbol":"145020","company_name":"휴젤","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_BIOLOGIC_APPROVAL_TO_COMMERCIAL_LAUNCH","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"HUGEL_STAGE2_APPROVAL_2024_03_04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval label worked over 180D but had high early MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C23 approval success but not immediate Green; needs high-MAE tolerance."}
{"row_type":"case","case_id":"C23_HLB_CRL_2024","symbol":"028300","company_name":"HLB","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"REGULATORY_EXPECTATION_TO_CRL_4C","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"HLB_4C_CRL_2024_05_17","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"pending approval/event premium failed; CRL route to 4C required","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Primary CRL source URL requires later ingestion validation; stock-web price shock and forward window validated."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"YUHAN_STAGE2_APPROVAL_2024_08_21","case_id":"C23_YUHAN_FDA_APPROVAL_2024","symbol":"000100","company_name":"유한양행","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION","sector":"바이오·헬스케어·의료기기","primary_archetype":"regulatory approval commercialization bridge","loop_objective":"coverage_gap_fill;sector_specific_rule_discovery;canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","evidence_available_at_that_date":"US FDA approval of Rybrevant plus lazertinib reported; actual approval label and partner commercialization bridge.","evidence_source":"Reuters 2024-08-20; Barron's 2024-08-20","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-21","entry_price":94300,"MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"approval_label_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"YUHAN_2024_08_21_94300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"YUHAN_STAGE3_GREEN_2024_08_28","case_id":"C23_YUHAN_FDA_APPROVAL_2024","symbol":"000100","company_name":"유한양행","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION","sector":"바이오·헬스케어·의료기기","primary_archetype":"regulatory approval commercialization bridge","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-08-28","evidence_available_at_that_date":"Approval label plus market confirmation; used for Green lateness audit, not aggregate representative.","evidence_source":"stock-web price confirmation plus public approval reports","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-28","entry_price":135500,"MFE_30D_pct":18.30,"MFE_90D_pct":23.17,"MFE_180D_pct":23.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.55,"MAE_90D_pct":-19.56,"MAE_180D_pct":-25.90,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.57,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_somewhat_late","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"YUHAN_2024_08_28_135500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"YUHAN_4B_PRICE_ONLY_2024_10_15","case_id":"C23_YUHAN_FDA_APPROVAL_2024","symbol":"000100","company_name":"유한양행","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_TO_ROYALTY_COMMERCIALIZATION","sector":"바이오·헬스케어·의료기기","primary_archetype":"regulatory approval commercialization bridge","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-10-15","evidence_available_at_that_date":"Price/valuation local peak only; no confirmed non-price thesis deterioration in this MD.","evidence_source":"stock-web OHLC only; narrative overlay","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-15","entry_price":163700,"MFE_30D_pct":1.96,"MFE_90D_pct":1.96,"MFE_180D_pct":1.96,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.65,"MAE_90D_pct":-38.67,"MAE_180D_pct":-39.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_peak_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"good_price_peak_but_insufficient_non_price_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"YUHAN_2024_10_15_163700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HUGEL_STAGE2_APPROVAL_2024_03_04","case_id":"C23_HUGEL_LETYBO_FDA_2024","symbol":"145020","company_name":"휴젤","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_BIOLOGIC_APPROVAL_TO_COMMERCIAL_LAUNCH","sector":"바이오·헬스케어·의료기기","primary_archetype":"regulatory approval commercialization bridge","loop_objective":"coverage_gap_fill;sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","evidence_available_at_that_date":"Letybo / letibotulinumtoxinA U.S. FDA approval; U.S. aesthetic launch bridge.","evidence_source":"FDA-derived drug references; Allure 2025 coverage of U.S. availability","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-04","entry_price":202500,"MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-21.93,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"high_MAE_structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HUGEL_2024_03_04_202500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HUGEL_STAGE3_GREEN_2024_06_11","case_id":"C23_HUGEL_LETYBO_FDA_2024","symbol":"145020","company_name":"휴젤","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"US_BIOLOGIC_APPROVAL_TO_COMMERCIAL_LAUNCH","sector":"바이오·헬스케어·의료기기","primary_archetype":"regulatory approval commercialization bridge","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-06-11","evidence_available_at_that_date":"Post-approval market confirmation / launch route proxy; used for lateness audit.","evidence_source":"stock-web price confirmation plus approval source map","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-11","entry_price":242000,"MFE_30D_pct":4.55,"MFE_90D_pct":21.69,"MFE_180D_pct":34.71,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.16,"MAE_90D_pct":-11.16,"MAE_180D_pct":-11.16,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-21.93,"green_lateness_ratio":0.32,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"green_moderately_late","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HUGEL_2024_06_11_242000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HLB_4C_CRL_2024_05_17","case_id":"C23_HLB_CRL_2024","symbol":"028300","company_name":"HLB","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"REGULATORY_EXPECTATION_TO_CRL_4C","sector":"바이오·헬스케어·의료기기","primary_archetype":"regulatory approval commercialization bridge","loop_objective":"counterexample_mining;4C_thesis_break_timing_test","trigger_type":"4C","trigger_date":"2024-05-17","evidence_available_at_that_date":"FDA CRL / approval failure event; primary URL not retrieved in this run, requires later source ingestion validation.","evidence_source":"source_validation_needed; stock-web price shock verified","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":67100,"MFE_30D_pct":9.99,"MFE_90D_pct":46.20,"MFE_180D_pct":46.20,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-32.71,"MAE_90D_pct":-32.71,"MAE_180D_pct":-32.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-40.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"CRL_thesis_break_counterexample","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HLB_2024_05_17_67100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HLB_PRE_CRL_EXPECTATION_STRESS_2024_05_16","case_id":"C23_HLB_CRL_2024","symbol":"028300","company_name":"HLB","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"REGULATORY_EXPECTATION_TO_CRL_4C","sector":"바이오·헬스케어·의료기기","primary_archetype":"regulatory approval commercialization bridge","loop_objective":"residual_false_positive_mining","trigger_type":"Stage3 false-positive stress","trigger_date":"2024-05-16","evidence_available_at_that_date":"Pending regulatory decision / event premium without actual approval label; used only as false-positive stress row.","evidence_source":"source_validation_needed; stock-web pre-CRL price verified","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":95800,"MFE_30D_pct":0.00,"MFE_90D_pct":2.40,"MFE_180D_pct":2.40,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-40.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"pending_review_event_premium_not_positive_green","four_b_evidence_type":["positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_pending_review_guard_needed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HLB_2024_05_16_95800","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_YUHAN_FDA_APPROVAL_2024","trigger_id":"YUHAN_STAGE2_APPROVAL_2024_08_21","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":50,"relative_strength_score":70,"customer_quality_score":85,"policy_or_regulatory_score":90,"valuation_repricing_score":65,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":50,"backlog_visibility_score":10,"margin_bridge_score":25,"revision_score":55,"relative_strength_score":75,"customer_quality_score":90,"policy_or_regulatory_score":95,"valuation_repricing_score":65,"execution_risk_score":20,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":80},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","customer_quality_score","revision_score","commercialization_score"],"component_delta_explanation":"Actual approval label plus partner commercialization bridge receives C23-specific bonus; not a global threshold change.","MFE_90D_pct":76.99,"MAE_90D_pct":-2.97,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_HUGEL_LETYBO_FDA_2024","trigger_id":"HUGEL_STAGE2_APPROVAL_2024_03_04","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":5,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":55,"customer_quality_score":60,"policy_or_regulatory_score":90,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":5,"margin_bridge_score":40,"revision_score":50,"relative_strength_score":60,"customer_quality_score":65,"policy_or_regulatory_score":95,"valuation_repricing_score":45,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":65},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow_Actionable","changed_components":["policy_or_regulatory_score","commercialization_score","margin_bridge_score"],"component_delta_explanation":"Approval label is real, but high early MAE means C23 should reward Stage2/Yellow, not force immediate Green.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"high_MAE_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"C23_HLB_CRL_2024","trigger_id":"HLB_PRE_CRL_EXPECTATION_STRESS_2024_05_16","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":40,"relative_strength_score":85,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":50,"valuation_repricing_score":85,"execution_risk_score":65,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"false_Stage3_Yellow_risk","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":"unknown_or_not_supported","revision_score":20,"relative_strength_score":85,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":0,"valuation_repricing_score":85,"execution_risk_score":80,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"thesis_break_score":100},"weighted_score_after":38,"stage_label_after":"4C","changed_components":["policy_or_regulatory_score","legal_or_contract_risk_score","execution_risk_score","thesis_break_score"],"component_delta_explanation":"Pending review without approval label receives guard; CRL routes to thesis break.","MFE_90D_pct":2.40,"MAE_90D_pct":-52.87,"score_return_alignment_label":"counterexample_guard_aligned","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

See `## 24. Shadow Weight Calibration` CSV block.

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"43","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["pending_review_without_actual_approval_false_positive_risk","hard_4c_arrives_after_gap_down"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L7/C23 approval label vs pending-review guard"}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"C23_CELLTRION_ZYMFENTRA_BLOCKED_2023","symbol":"068270","company_name":"셀트리온","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"FDA approval event relevant but 2024-01-12 corporate-action candidate overlaps 180D forward window from 2023-10-23 entry; blocked from weight calibration","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R7 or R8 holdout validation
recommended_next_scope = C23 holdout with additional actual-approval cases and primary CRL source ingestion; or C24 trial-data event risk split
next_priority = validate whether approval-label bonus survives more counterexamples and whether pending-review guard reduces false positives without killing true early Stage2s
```

## 28. Source Notes

Stock-web / artifact source notes:

- `Songdaiki/stock-web` manifest confirms `max_date = 2026-02-20`, `price_basis = tradable_raw`, `price_adjustment_status = raw_unadjusted_marcap`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.
- `stock_agent` ingest summary was used only for coverage/duplicate avoidance; no `src/e2r` code was opened.
- Yuhan, Hugel, and HLB symbol profiles show no corporate-action candidate dates inside each selected 180D window.
- Celltrion/Zymfentra was blocked as `narrative_only` because `068270` profile shows `2024-01-12` as a corporate-action candidate inside the 180D window from the October 2023 approval trigger.

Evidence notes:

- Yuhan/J&J approval event is supported by public reports of U.S. FDA approval of Rybrevant plus lazertinib for first-line EGFR-mutated NSCLC in August 2024.
- Hugel/Letybo event is supported by public drug-reference and market-availability coverage indicating U.S. FDA approval in February 2024 and later U.S. availability.
- HLB/CRL event requires primary-source URL validation in the later ingestion pass. This MD uses the event as a counterexample because the stock-web price discontinuity and forward path are directly verified, but it flags the source as `source_validation_needed` before production ingestion.
