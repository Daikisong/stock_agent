# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R7
scheduled_loop = 15
completed_round = R7
completed_loop = 15
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_BINARY_CRL_GUARD
output_file = e2r_stock_web_v12_residual_round_R7_loop_15_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This research does not re-prove the global rules. It asks whether C23 biotech regulatory approval/commercialization events need a more specific split between approved commercial pathways and unresolved binary regulatory events.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R7
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_sector_consistency = pass
```

Selected scope: regulatory approval-to-commercialization cases where the price path is shaped less by ordinary quarterly revision cadence and more by whether the approval already has a monetizable commercial route.

## 3. Previous Coverage / Duplicate Avoidance Check

Search against the allowed `stock_agent` research surface found no exact v12 R7 Loop 15 or `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` match during this run. The case set intentionally avoids the prior R6 financial samples and uses three new R7 symbols.

```text
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

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
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_basis = tradable_raw
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable | reason |
|---|---|---:|---|---|---|---|
| C23-YUHAN-LAZERTINIB-FDA-202408 | 000100 | 2024-08-21 | yes, manifest max_date 2026-02-20 | clean_180D_window | true | 2020 corporate-action candidate is outside the 2024 entry window |
| C23-HUGEL-LETYBO-FDA-202403 | 145020 | 2024-03-04 | yes | clean_180D_window | true | 2020 corporate-action candidates are outside the 2024 entry window |
| C23-HLB-CRL-202405 | 028300 | 2024-03-21 / 2024-05-17 | yes | clean_180D_window | true | latest corporate-action candidates are 2021, outside 2024 window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| FDA_APPROVAL_GLOBAL_PARTNER_FIRST_LINE_COMMERCIALIZATION | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | approved label + named global commercial partner + royalty/milestone route |
| FDA_APPROVAL_CONSUMER_AESTHETIC_EXPORT_LAUNCH | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | approval is real but launch and reorder bridge decide whether Green is justified |
| BINARY_PENDING_REGULATORY_APPROVAL_FALSE_POSITIVE_CRL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | same approval path, but unresolved binary event must be capped until approval is confirmed |

## 7. Case Selection Summary

| case_id | role | trigger family | independent? | why included |
|---|---|---|---|---|
| C23-YUHAN-LAZERTINIB-FDA-202408 | positive / missed structural | FDA approval + global partner commercialization | true | Green-by-revision alone was late versus actual MFE |
| C23-HUGEL-LETYBO-FDA-202403 | positive / high-MAE success | FDA approval + export launch | true | valid approval but MAE shows launch confirmation gate is still needed |
| C23-HLB-CRL-202405 | counterexample / 4C | binary regulatory decision failure | true | relative-strength + regulatory anticipation failed after CRL |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
```

The balance is intentionally asymmetric: two genuine approval-to-commercialization positives are paired with one severe binary-event failure. C23 should not become "FDA event = buy"; it should behave more like an airlock: approval opens the first door, but commercialization quality and unresolved binary risk decide whether the second door opens.

## 9. Evidence Source Map

| case_id | evidence at trigger date | source status | stage implication |
|---|---|---|---|
| Yuhan | J&J/FDA approval of lazertinib + amivantamab first-line EGFR-mutated NSCLC combination | Reuters/FDA/J&J public approval narrative checked in web search | Stage2-Actionable / C23 approval-quality promotion |
| Hugel | Letybo/letibotulinumtoxinA FDA approval for glabellar lines | FDA Drug Trials Snapshot / public coverage checked in web search | Stage2-Actionable but Green gated by launch/reorder bridge |
| HLB | CRL / regulatory non-approval event after strong pre-event RS | direct web article not retrieved by search tool; retained as counterexample/4C with stock-web OHLC | binary pending cap + hard 4C thesis-break route |

## 10. Price Data Source Map

| symbol | company | shard path | profile path | profile caveat |
|---|---|---|---|---|
| 000100 | 유한양행 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | corporate-action candidates exist historically, none in 2024 window |
| 145020 | 휴젤 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | atlas/symbol_profiles/145/145020.json | corporate-action candidates exist historically, none in 2024 window |
| 028300 | HLB | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | corporate-action candidates exist historically, none in 2024 window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol/company | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | outcome | current_profile_verdict | aggregate? |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| T-C23-YUHAN-STAGE2A-20240821 | 000100 유한양행 | Stage2-Actionable | 2024-08-20 | 2024-08-21 | 94300 | 69.99 | 76.99 | 76.99 | -2.97 | -2.97 | -2.97 | missed_structural | current_profile_too_late | True |
| T-C23-YUHAN-STAGE3G-20240924 | 000100 유한양행 | Stage3-Green-label-comparison | 2024-09-24 | 2024-09-24 | 157000 | 6.31 | 6.31 | 6.31 | -15.03 | -30.57 | -36.05 | late_green_label | current_profile_too_late | False |
| T-C23-HUGEL-STAGE2A-20240304 | 145020 휴젤 | Stage2-Actionable | 2024-02-29 | 2024-03-04 | 202500 | 8.15 | 29.63 | 60.99 | -14.91 | -14.91 | -14.91 | high_mae_success | current_profile_correct | True |
| T-C23-HUGEL-4B-20241106 | 145020 휴젤 | 4B-overlay | 2024-11-06 | 2024-11-06 | 321000 | 1.56 | 1.56 | 1.56 | -26.17 | -26.17 | -26.17 | 4B_overlay_success | current_profile_4B_too_late | False |
| T-C23-HLB-STAGE3Y-20240321 | 028300 HLB | Stage3-Yellow false-positive stress | 2024-03-21 | 2024-03-21 | 112700 | 14.46 | 14.46 | 14.46 | -24.49 | -58.3 | -58.3 | false_positive_green | current_profile_false_positive | True |
| T-C23-HLB-4C-20240517 | 028300 HLB | 4C-thesis-break | 2024-05-17 | 2024-05-17 | 67100 | 9.99 | 46.2 | 46.2 | -29.96 | -29.96 | -29.96 | 4C_success | current_profile_4C_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative triggers only

| case_id | entry_date | entry_price | 30D high/low | 90D high/low | 180D high/low | peak_date | peak_price | backtest interpretation |
|---|---:|---:|---|---|---|---:|---:|---|
| Yuhan | 2024-08-21 | 94,300 | high 160,300 / low 91,500 | high 166,900 / low 91,500 | high 166,900 / low 91,500 | 2024-10-15 | 166,900 | strong MFE with shallow early MAE |
| Hugel | 2024-03-04 | 202,500 | high 219,000 / low 172,300 | high 262,500 / low 172,300 | high 326,000 / low 172,300 | 2024-11-07 | 326,000 | eventual success but high-MAE path |
| HLB | 2024-03-21 | 112,700 | high 129,000 / low 85,100 | high 129,000 / low 47,000 | high 129,000 / low 47,000 | 2024-03-26 | 129,000 | false positive; CRL-style thesis break dominated |

### 12.2 Formula

```text
MFE_N_pct = (max(high from entry through N tradable rows) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry through N tradable rows) / entry_price - 1) * 100
drawdown_after_peak_pct = (min(low after peak_date) / peak_price - 1) * 100
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| Yuhan | Stage3-Yellow until revision/confirmation; Green likely late | Stage2 approval trigger captured 76.99% 90D MFE with -2.97% MAE | current_profile_too_late |
| Hugel | Yellow / watch-to-confirm launch | 60.99% 180D MFE, but -14.91% MAE before rerating | current_profile_correct |
| HLB | Yellow/possible Green if RS and public event are over-weighted | 14.46% MFE but -58.30% MAE after CRL | current_profile_false_positive |

Answers to the required stress questions:

```text
1. Current profile judgment: mixed. It is conservative enough for Hugel, late for Yuhan, too permissive if HLB-like binary pending events score on RS.
2. MFE/MAE fit: Yuhan positive fit, Hugel high-MAE success, HLB false positive.
3. Stage2 bonus: insufficient for Yuhan-like approved commercial paths; too high if applied to pending binary decisions.
4. Yellow threshold 75: acceptable as a staging buffer.
5. Green threshold 87 / revision 55: too late for C23 when approval + global partner + commercial route is already visible.
6. price-only blowoff guard: strengthened by HLB.
7. full 4B non-price requirement: kept; Hugel 4B only works with valuation/commercialization context, not price alone.
8. hard 4C routing: strengthened; HLB shows 4C must fire at thesis-break event, not after price damage completes.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2_Actionable_entry | Stage3_Green_proxy_entry | peak_after_stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| Yuhan | 94,300 | 157,000 | 166,900 | 0.86 | Green waited for most of the upside |
| Hugel | 202,500 | not confirmed | 326,000 | not_applicable | Yellow-first was appropriate because early MAE was deep |
| HLB | 112,700 | should be capped | 129,000 | not_applicable | binary-pending regulatory events should not Green on price/RS |

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B trigger | Stage2 entry | 4B entry | local peak | full-window peak | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Hugel | T-C23-HUGEL-4B-20241106 | 202,500 | 321,000 | 326,000 | 326,000 | 0.96 | 0.96 | good_full_window_4B_timing |
| HLB | none before CRL | 112,700 | n/a | 129,000 | 129,000 | n/a | n/a | should have been event-risk cap, not price-only 4B |
| Yuhan | none | 94,300 | n/a | 166,900 | 166,900 | n/a | n/a | no full 4B without non-price exhaustion evidence |

## 16. 4C Protection Audit

| case_id | 4C trigger | prior peak | 4C entry | post-4C low | protection score | label |
|---|---|---:|---:|---:|---:|---|
| HLB | T-C23-HLB-4C-20240517 | 129,000 | 67,100 | 47,000 | 0.53 | hard_4c_success |
| Yuhan | none | n/a | n/a | n/a | n/a | no thesis break |
| Hugel | none | n/a | n/a | n/a | n/a | 4B overlay, not 4C |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R7/L7 only has three cases in this MD, and the signal is more precise at C23 than at all bio/healthcare level.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

Proposed shadow logic:

```text
if C23 and approval_status == approved
   and commercialization_route includes named global partner or launched export product
   and approval label is material to addressable market:
       add C23_approval_commercialization_quality_gate +1.5 shadow score
       allow Stage3-Green even if revision confirmation is not yet fully visible
       only if legal/manufacturing/label risk is low

if C23 and approval_status == pending/unresolved
   and price/relative strength is the main evidence
   and binary regulatory decision is near:
       apply C23_binary_pending_regulatory_cap
       block Green until approval/CRL/label/manufacturing-risk status clears
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | general calibrated profile, no C23 nuance | none | 3 | Yuhan/Hugel/HLB representatives | 40.36 | -25.39 | 0.33 | 1 | 1 | 0.86 | 0.96 | 0.96 | mixed; Yuhan late and HLB false positive |
| P0b e2r_2_0_baseline_reference | rollback reference | looser pre-stock-web baseline | rollback only | 3 | same | 40.36 | -25.39 | 0.33+ | 1 | 1 | 0.86 | n/a | n/a | worse guardrail around HLB-like binary event |
| P1 sector_specific_candidate_profile | sector shadow | L7 approval events require commercialization quality | C23 approval quality gate | 3 | same | 40.36 | -25.39 | 0.33 | 0 | 0 | 0.43 | 0.96 | 0.96 | partial; sector still too broad |
| P2 canonical_archetype_candidate_profile | C23 shadow | promote approved global-commercial paths; cap pending binary decisions | approval_commercialization_quality_gate + binary_pending_cap | 2 accepted / 1 capped | Yuhan/Hugel accepted, HLB capped | 53.31 | -8.94 | 0.00 | 0 | 0 | 0.20 | 0.96 | 0.96 | best alignment |
| P3 counterexample_guard_profile | C23 guard | unresolved FDA/NDA binary event cannot Green on price/RS alone | binary_pending_regulatory_cap | 2 accepted / 1 watch-only | HLB removed from positive set | 53.31 | -8.94 | 0.00 | 1 | 0 | 0.20 | 0.96 | 0.96 | safer but may miss Yuhan without quality gate |


## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| Yuhan | 83.0 | Stage3-Yellow | 88.0 | Stage3-Green-shadow | 76.99 | -2.97 | improved |
| Hugel | 77.0 | Stage3-Yellow | 80.0 | Stage3-Yellow-shadow-not-Green | 29.63 | -14.91 | kept cautious |
| HLB | 79.0 | Stage3-Yellow-risky | 66.0 | Stage2-watch / 4B-risk-capped | 14.46 | -58.30 | false positive filtered |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | FDA_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_AND_BINARY_CRL_GUARD | 2 | 1 | 1 | 1 | 3 | 0 | 6 | 3 | 2 | false | true | still needs more ex-Korea commercialization and late-4C cases |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late
  - current_profile_false_positive
  - current_profile_4C_too_late
new_axis_proposed:
  - C23_approval_commercialization_quality_gate
  - C23_binary_pending_regulatory_cap
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened:
  - stage3_green_revision_min as C23-only shadow exception when approval+commercialization route is explicit
existing_axis_kept:
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema checked.
- Entry rows exist in tradable shards.
- 180D forward windows exist by manifest max_date.
- Representative trigger MFE/MAE computed from actual OHLC row values.
- Corporate-action candidate dates do not overlap the 2024 180D windows.
- R7/L7 sector consistency passes.
```

Not validated:

```text
- No stock_agent source code was opened.
- No production scoring patch was written.
- No live 2026 candidate scan was performed.
- HLB direct CRL article retrieval was incomplete in the web tool; it is used only as counterexample/4C stress context, not as positive promotion.
- 1Y/2Y fields are included but not used for weight proposal; 180D is the quantitative calibration basis.
```

## 24. Shadow Weight Calibration

| row_type | axis | scope | large_sector_id | canonical_archetype_id | baseline_value | tested_value | delta | reason | backtest_effect | trigger_ids | calibration_usable_count | new_independent_case_count | counterexample_count | confidence | proposal_type | notes |
|---|---|---|---|---|---|---|---|---|---|---|---:|---:|---:|---|---|---|
| shadow_weight | C23_approval_commercialization_quality_gate | canonical_archetype_specific | L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 0 | 1 | +1.5 shadow score | approval with named commercial route can outrun revision confirmation | promotes Yuhan earlier, keeps Hugel cautious | T-C23-YUHAN-STAGE2A-20240821\|T-C23-HUGEL-STAGE2A-20240304 | 2 | 2 | 1 | low_to_medium | canonical_shadow_only | not production |
| shadow_weight | C23_binary_pending_regulatory_cap | canonical_archetype_specific | L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | false | true | guardrail | pending binary event cannot Green on RS alone | filters HLB-like false positive | T-C23-HLB-STAGE3Y-20240321\|T-C23-HLB-4C-20240517 | 2 | 1 | 1 | medium | canonical_shadow_guard | strengthens existing guardrails |

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C23-YUHAN-LAZERTINIB-FDA-202408","symbol":"000100","company_name":"유한양행","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_GLOBAL_PARTNER_FIRST_LINE_COMMERCIALIZATION","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"T-C23-YUHAN-STAGE2A-20240821","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval + global partner commercialization mapped to large MFE with shallow early MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"FDA/J&J lazertinib+amivantamab approval created a commercialization-quality trigger; revision-confirmation-only Green would arrive late."}
{"row_type":"case","case_id":"C23-HUGEL-LETYBO-FDA-202403","symbol":"145020","company_name":"휴젤","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_CONSUMER_AESTHETIC_EXPORT_LAUNCH","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T-C23-HUGEL-STAGE2A-20240304","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"approval was valid but commercialization/launch confirmation mattered because MAE was deep before later rerating","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"FDA approval alone was useful but not enough for immediate Green without launch/reorder visibility."}
{"row_type":"case","case_id":"C23-HLB-CRL-202405","symbol":"028300","company_name":"HLB","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BINARY_PENDING_REGULATORY_APPROVAL_FALSE_POSITIVE_CRL","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T-C23-HLB-STAGE3Y-20240321","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"relative-strength and regulatory anticipation failed once CRL/thesis-break evidence arrived","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Regulatory binary pending setup needs explicit cap until approval/label/manufacturing inspection risk clears."}
{"round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":["coverage_gap_fill","counterexample_mining","residual_missed_structural_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"row_type":"trigger","trigger_id":"T-C23-YUHAN-STAGE2A-20240821","case_id":"C23-YUHAN-LAZERTINIB-FDA-202408","symbol":"000100","company_name":"유한양행","fine_archetype_id":"FDA_APPROVAL_GLOBAL_PARTNER_FIRST_LINE_COMMERCIALIZATION","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-20","entry_date":"2024-08-21","entry_price":94300,"evidence_available_at_that_date":"FDA/J&J approval of lazertinib + amivantamab first-line EGFR-mutated NSCLC regimen; Korea market reacted on 2024-08-21.","evidence_source":"Reuters 2024-08-20; FDA approval narrative; J&J/Rybrevant+Lazcluze release.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["durable_customer_confirmation","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","MFE_30D_pct":69.99,"MFE_90D_pct":76.99,"MFE_180D_pct":76.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.97,"MAE_90D_pct":-2.97,"MAE_180D_pct":-2.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"missed_structural","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C23-YUHAN-20240821","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":["coverage_gap_fill","counterexample_mining","residual_missed_structural_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"row_type":"trigger","trigger_id":"T-C23-YUHAN-STAGE3G-20240924","case_id":"C23-YUHAN-LAZERTINIB-FDA-202408","symbol":"000100","company_name":"유한양행","fine_archetype_id":"FDA_APPROVAL_GLOBAL_PARTNER_FIRST_LINE_COMMERCIALIZATION","trigger_type":"Stage3-Green-label-comparison","trigger_date":"2024-09-24","entry_date":"2024-09-24","entry_price":157000,"evidence_available_at_that_date":"post-approval market confirmation / price-relative strength after the initial approval surge.","evidence_source":"stock-web observed OHLC label comparison; later confirmation proxy only.","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","profile_path":"atlas/symbol_profiles/000/000100.json","MFE_30D_pct":6.31,"MFE_90D_pct":6.31,"MFE_180D_pct":6.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.03,"MAE_90D_pct":-30.57,"MAE_180D_pct":-36.05,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":166900,"drawdown_after_peak_pct":-39.84,"green_lateness_ratio":0.86,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green_label","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C23-YUHAN-20240924","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same case label comparison for Green lateness audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":["coverage_gap_fill","counterexample_mining","residual_missed_structural_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"row_type":"trigger","trigger_id":"T-C23-HUGEL-STAGE2A-20240304","case_id":"C23-HUGEL-LETYBO-FDA-202403","symbol":"145020","company_name":"휴젤","fine_archetype_id":"FDA_APPROVAL_CONSUMER_AESTHETIC_EXPORT_LAUNCH","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-29","entry_date":"2024-03-04","entry_price":202500,"evidence_available_at_that_date":"U.S. FDA approval of Letybo/letibotulinumtoxinA for glabellar lines; Korean market entry used next tradable day after weekend/holiday.","evidence_source":"FDA Drug Trials Snapshot / public Letybo approval coverage.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-27.3,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C23-HUGEL-20240304","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":["coverage_gap_fill","counterexample_mining","residual_missed_structural_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"row_type":"trigger","trigger_id":"T-C23-HUGEL-4B-20241106","case_id":"C23-HUGEL-LETYBO-FDA-202403","symbol":"145020","company_name":"휴젤","fine_archetype_id":"FDA_APPROVAL_CONSUMER_AESTHETIC_EXPORT_LAUNCH","trigger_type":"4B-overlay","trigger_date":"2024-11-06","entry_date":"2024-11-06","entry_price":321000,"evidence_available_at_that_date":"post-approval rerating reached full-window peak zone; non-price 4B proxy is launch/valuation overheating after commercialization expectations.","evidence_source":"stock-web OHLC + non-price commercialization-timing overlay proxy.","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","MFE_30D_pct":1.56,"MFE_90D_pct":1.56,"MFE_180D_pct":1.56,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-26.17,"MAE_90D_pct":-26.17,"MAE_180D_pct":-26.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000,"drawdown_after_peak_pct":-27.3,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C23-HUGEL-20241106","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B timing overlay","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":["coverage_gap_fill","counterexample_mining","residual_missed_structural_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"row_type":"trigger","trigger_id":"T-C23-HLB-STAGE3Y-20240321","case_id":"C23-HLB-CRL-202405","symbol":"028300","company_name":"HLB","fine_archetype_id":"BINARY_PENDING_REGULATORY_APPROVAL_FALSE_POSITIVE_CRL","trigger_type":"Stage3-Yellow false-positive stress","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":112700,"evidence_available_at_that_date":"strong relative strength into binary NDA/regulatory decision expectation before final approval decision.","evidence_source":"public NDA/regulatory anticipation context + stock-web OHLC; direct HLB CRL article not re-fetched by web tool in this run.","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","MFE_30D_pct":14.46,"MFE_90D_pct":14.46,"MFE_180D_pct":14.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.49,"MAE_90D_pct":-58.3,"MAE_180D_pct":-58.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":129000,"drawdown_after_peak_pct":-63.57,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"binary_pending_without_approval_cap_needed","four_b_evidence_type":["positioning_overheat","explicit_event_cap"],"four_c_protection_label":null,"trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C23-HLB-20240321","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","sector":"bio_healthcare_medical","primary_archetype":"regulatory_approval_to_commercialization","loop_objective":["coverage_gap_fill","counterexample_mining","residual_missed_structural_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"row_type":"trigger","trigger_id":"T-C23-HLB-4C-20240517","case_id":"C23-HLB-CRL-202405","symbol":"028300","company_name":"HLB","fine_archetype_id":"BINARY_PENDING_REGULATORY_APPROVAL_FALSE_POSITIVE_CRL","trigger_type":"4C-thesis-break","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":67100,"evidence_available_at_that_date":"CRL/regulatory non-approval thesis break day; stock-web shows limit-down style gap and subsequent low at 47,000.","evidence_source":"public CRL event context + stock-web OHLC; direct HLB CRL article not re-fetched by web tool in this run.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":["regulatory_rejection","thesis_evidence_broken","forced_liquidation_or_crash"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","MFE_30D_pct":9.99,"MFE_90D_pct":46.2,"MFE_180D_pct":46.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-29.96,"MAE_90D_pct":-29.96,"MAE_180D_pct":-29.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":98100,"drawdown_after_peak_pct":-52.09,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","four_c_protection_score":0.53,"trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C23-HLB-20240517","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4C protection overlay","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23-YUHAN-LAZERTINIB-FDA-202408","trigger_id":"T-C23-YUHAN-STAGE2A-20240821","symbol":"000100","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":0,"margin_bridge_score":30,"revision_score":45,"relative_strength_score":85,"customer_quality_score":95,"policy_or_regulatory_score":100,"valuation_repricing_score":70,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"commercialization_score":90},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":0,"margin_bridge_score":30,"revision_score":45,"relative_strength_score":85,"customer_quality_score":95,"policy_or_regulatory_score":100,"valuation_repricing_score":70,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"commercialization_score":100,"c23_approval_quality_gate":1},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green-shadow","changed_components":["c23_approval_quality_gate","commercialization_score"],"component_delta_explanation":"Named global partner + approved label + first-line commercial pathway offsets revision lag as C23-only shadow exception.","MFE_90D_pct":76.99,"MAE_90D_pct":-2.97,"score_return_alignment_label":"positive_alignment_after_c23_gate","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23-HUGEL-LETYBO-FDA-202403","trigger_id":"T-C23-HUGEL-STAGE2A-20240304","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":42,"relative_strength_score":55,"customer_quality_score":50,"policy_or_regulatory_score":100,"valuation_repricing_score":60,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"commercialization_score":55},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":35,"revision_score":42,"relative_strength_score":55,"customer_quality_score":55,"policy_or_regulatory_score":100,"valuation_repricing_score":60,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"commercialization_score":65,"c23_launch_confirmation_required":1},"weighted_score_after":80.0,"stage_label_after":"Stage3-Yellow-shadow-not-Green","changed_components":["commercialization_score","c23_launch_confirmation_required"],"component_delta_explanation":"Approval is real, but launch/reorder bridge not yet enough; keep Yellow until commercial confirmation because MAE was deep.","MFE_90D_pct":29.63,"MAE_90D_pct":-14.91,"score_return_alignment_label":"positive_but_high_mae_requires_launch_gate","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C23-HLB-CRL-202405","trigger_id":"T-C23-HLB-STAGE3Y-20240321","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":35,"relative_strength_score":95,"customer_quality_score":35,"policy_or_regulatory_score":65,"valuation_repricing_score":90,"execution_risk_score":75,"legal_or_contract_risk_score":80,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"binary_event_risk_score":95},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow-risky","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":35,"relative_strength_score":95,"customer_quality_score":35,"policy_or_regulatory_score":65,"valuation_repricing_score":90,"execution_risk_score":90,"legal_or_contract_risk_score":95,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"binary_event_risk_score":100,"c23_binary_pending_regulatory_cap":1},"weighted_score_after":66.0,"stage_label_after":"Stage2-watch / 4B-risk-capped","changed_components":["legal_or_contract_risk_score","execution_risk_score","c23_binary_pending_regulatory_cap"],"component_delta_explanation":"Relative strength into unresolved binary FDA decision cannot promote Green; cap until approval/manufacturing/label clears.","MFE_90D_pct":14.46,"MAE_90D_pct":-58.3,"score_return_alignment_label":"false_positive_filtered_by_c23_binary_cap","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"aggregate","round":"R7","loop":"15","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","representative_trigger_count":3,"avg_MFE_90D_pct":40.36,"avg_MAE_90D_pct":-25.39,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"false_positive_rate":0.33,"score_return_alignment_verdict":"C23 needs approval-quality promotion plus binary-pending cap"}
{"row_type":"shadow_weight","axis":"C23_approval_commercialization_quality_gate","scope":"canonical_archetype_specific","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","baseline_value":0,"tested_value":1,"delta":"+1.5 shadow score","reason":"When approval has named global partner, approved label, and plausible commercial royalty/milestone route, revision lag alone made Green too late in Yuhan.","backtest_effect":"Yuhan promoted earlier; Hugel stays Yellow because launch bridge weaker; HLB still capped.","trigger_ids":"T-C23-YUHAN-STAGE2A-20240821|T-C23-HUGEL-STAGE2A-20240304","calibration_usable_count":2,"new_independent_case_count":2,"counterexample_count":1,"confidence":"low_to_medium","proposal_type":"canonical_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"C23_binary_pending_regulatory_cap","scope":"canonical_archetype_specific","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","baseline_value":false,"tested_value":true,"delta":"guardrail","reason":"Unresolved binary FDA decision + price/RS into event showed severe MAE after CRL in HLB.","backtest_effect":"Blocks HLB-like pending approval setups from Green without approval/label/manufacturing-risk clearance.","trigger_ids":"T-C23-HLB-STAGE3Y-20240321|T-C23-HLB-4C-20240517","calibration_usable_count":2,"new_independent_case_count":1,"counterexample_count":1,"confidence":"medium","proposal_type":"canonical_shadow_guard","notes":"strengthens price_only_blowoff_blocks_positive_stage and hard_4c_thesis_break_routes_to_4c for C23"}
{"row_type":"residual_contribution","round":"R7","loop":"15","scheduled_round":"R7","scheduled_loop":"15","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4C_too_late"],"diversity_score_summary":"new_symbol_bonus=9; same_archetype_new_symbol_bonus=12; trigger_family_bonus=12; counterexample_gap=4; residual_error_bonus=10; total≈47","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C23-HLB-CRL-SOURCE-LIMITATION","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reason":"direct web source for HLB CRL article was not retrieved by search tool; case retained as counterexample/4C stress row using stock-web OHLC and public event label, not as positive promotion","price_source":"Songdaiki/stock-web","usage":"counterexample_context_only"}
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
completed_round = R7
completed_loop = 15
next_round = R8
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_schema = atlas/schema.json
selected_profiles:
  - atlas/symbol_profiles/000/000100.json
  - atlas/symbol_profiles/145/145020.json
  - atlas/symbol_profiles/028/028300.json
selected_price_shards:
  - atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv
external_event_sources_checked:
  - Reuters, 2024-08-20, U.S. FDA approves J&J's chemotherapy-free lung cancer regimen involving lazertinib.
  - FDA/Drug Trials Snapshot and public coverage for Letybo/letibotulinumtoxinA approval.
  - HLB CRL event label retained with source-retrieval limitation, used only for counterexample/4C stress.
```
