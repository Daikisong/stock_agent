# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 22
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION | KPOP_MULTI_LABEL_PORTFOLIO_IP_MONETIZATION | K_DRAMA_OTT_DISTRIBUTION_WITHOUT_MARGIN_CONVERSION
output_file = e2r_stock_web_v12_residual_round_R8_loop_22_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

This file is historical calibration research only. It is not a live watchlist, a recommendation list, a production patch, or a broker/API workflow.

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

The purpose is not to prove these global axes again. The residual question is narrower: in C27, does content/IP monetization need a distinct distinction between (a) global demand that converts into margin/revision and (b) global distribution/narrative that does not?

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R8 |
| loop | 22 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| selected objective | coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression |
| selected symbols | 035900 JYP Ent.; 352820 하이브; 253450 스튜디오드래곤 |
| positive/counterexample balance | 2 positive / 1 counterexample / 1 4B overlay |

## 3. Previous Coverage / Duplicate Avoidance Check

Artifact/code-search duplicate scan result:

```text
searched stock_agent research artifacts for:
- C27_CONTENT_IP_GLOBAL_MONETIZATION
- 035900
- 352820
- 253450
result = no direct duplicate hit
```

The immediately previous generated loop was C28 software/security contract-retention, so this loop deliberately moves to C27 content/IP global monetization. The same R8 sector is allowed; the canonical archetype, symbols, trigger families, and failure mode are new relative to the previous output.

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 1
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

| Manifest field | Value |
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

Price basis is `tradable_raw`. It is raw/unadjusted marcap OHLC and not split/dividend adjusted. Corporate-action candidate windows are blocked when they overlap the 180D window.

## 5. Historical Eligibility Gate

| Symbol | Profile path | First/last date | Corporate action candidate status | 180D calibration status |
|---|---:|---|---|---|
| 035900 JYP Ent. | atlas/symbol_profiles/035/035900.json | 2001-08-30 / 2026-02-20 | candidates exist historically, latest 2013-10-31; no overlap with 2023 trigger windows | usable |
| 352820 하이브 | atlas/symbol_profiles/352/352820.json | 2020-10-15 / 2026-02-20 | 0 candidates | usable |
| 253450 스튜디오드래곤 | atlas/symbol_profiles/253/253450.json | 2017-11-24 / 2026-02-20 | 0 candidates | usable |

## 6. Canonical Archetype Compression Map

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
├── KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION
│   └── JYP Ent.: global album/tour demand converts to high MFE and low MAE.
├── KPOP_MULTI_LABEL_PORTFOLIO_IP_MONETIZATION
│   └── HYBE: multi-label artist/IP portfolio reduces single-IP concentration risk.
└── K_DRAMA_OTT_DISTRIBUTION_WITHOUT_MARGIN_CONVERSION
    └── Studio Dragon: global OTT/K-content narrative does not convert to margin/revision; false-positive guard needed.
```

The compression is not “all content is good.” It is “repeatable IP monetization with visible unit demand and margin bridge is good; distribution attention without owned-IP economics is fragile.”

## 7. Case Selection Summary

| case_id | Symbol | Role | Trigger family | Why selected |
|---|---:|---|---|---|
| C27_JYP_2023_GLOBAL_ALBUMS | 035900 | structural_success + 4B overlay | global album/tour IP monetization; late Green; valuation 4B | Positive C27 where Stage2 captured large upside before Green. |
| C27_HYBE_2023_PORTFOLIO_MONETIZATION | 352820 | structural_success | multi-label IP portfolio | Positive C27 where portfolio breadth offset BTS hiatus concern. |
| C27_STUDIO_DRAGON_2021_OTT_NARRATIVE | 253450 | failed_rerating / false positive | OTT/K-drama global narrative without margin conversion | Counterexample: content narrative did not close into stock-return alignment. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 6
```

The gap after this loop is not “more K-pop positives.” The gap is C27 4C: content/IP thesis breaks caused by contract loss, artist departure, regulatory/accounting trust break, or platform take-rate deterioration.

## 9. Evidence Source Map

| Case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| JYP | public artist release cadence; global album/tour demand; relative strength | later demand/revision/margin visibility | 2023-07-25 valuation/positioning blowoff | none |
| HYBE | multi-label artist portfolio; album/tour cadence; known BTS hiatus already priced | later portfolio/revision confirmation | watch only | none |
| Studio Dragon | K-content/OTT visibility after global drama momentum | insufficient margin/revision bridge | none | late thesis-break / false-positive narrative |

External source notes used for narrative mapping:
- Stray Kids/JYP: 2023 `5-Star` public demand milestones and global album sales context.
- HYBE/K-pop sector: 2023 album-sales sector strength and later IP/governance risk context.
- Studio Dragon: public K-content/OTT success narrative, contrasted against weak price-return alignment.

## 10. Price Data Source Map

| Symbol | Representative price shard | Profile path |
|---:|---|---|
| 035900 | atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv | atlas/symbol_profiles/035/035900.json |
| 352820 | atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv | atlas/symbol_profiles/352/352820.json |
| 253450 | atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv; atlas/ohlcv_tradable_by_symbol_year/253/253450/2022.csv | atlas/symbol_profiles/253/253450.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | Symbol | Type | trigger_date | entry_date | entry_price | Role | Aggregate? |
|---|---:|---|---:|---:|---:|---|---|
| T_C27_JYP_2023_STAGE2_20230113 | 035900 | Stage2-Actionable | 2023-01-13 | 2023-01-13 | 63,900 | representative positive | yes |
| T_C27_JYP_2023_GREEN_20230516 | 035900 | Stage3-Green | 2023-05-16 | 2023-05-16 | 115,400 | label comparison | no |
| T_C27_JYP_2023_4B_20230725 | 035900 | Stage4B | 2023-07-25 | 2023-07-25 | 141,100 | 4B overlay | no |
| T_C27_HYBE_2023_STAGE2_20230113 | 352820 | Stage2-Actionable | 2023-01-13 | 2023-01-13 | 174,500 | representative positive | yes |
| T_C27_HYBE_2023_GREEN_20230413 | 352820 | Stage3-Green | 2023-04-13 | 2023-04-13 | 245,000 | label comparison | no |
| T_C27_STUDIO_2021_STAGE2_20211119 | 253450 | Stage2-Actionable | 2021-11-19 | 2021-11-19 | 96,400 | representative counterexample | yes |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | peak | drawdown after peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| T_C27_JYP_2023_STAGE2_20230113 | 63,900 | 21.44% | -1.10% | 89.20% | -1.10% | 129.42% | -1.10% | 2023-07-25 / 146,600 | -31.04% |
| T_C27_JYP_2023_GREEN_20230516 | 115,400 | 20.10% | -4.16% | 27.04% | -12.39% | 27.04% | -12.39% | 2023-07-25 / 146,600 | -31.04% |
| T_C27_JYP_2023_4B_20230725 | 141,100 | 3.90% | -26.29% | 3.90% | -28.35% | 3.90% | -28.35% | 2023-07-25 / 146,600 | -31.04% |
| T_C27_HYBE_2023_STAGE2_20230113 | 174,500 | 25.21% | -0.86% | 73.64% | -2.41% | 79.08% | -2.41% | 2023-06-22 / 312,500 | -29.28% |
| T_C27_HYBE_2023_GREEN_20230413 | 245,000 | 23.67% | -5.51% | 27.55% | -5.51% | 27.55% | -17.55% | 2023-06-22 / 312,500 | -29.28% |
| T_C27_STUDIO_2021_STAGE2_20211119 | 96,400 | 2.59% | -13.28% | 2.59% | -25.00% | 2.59% | -34.44% | 2021-11-22 / 98,900 | -36.10% |

## 13. Current Calibrated Profile Stress Test

| Case | Current profile likely behavior | Backtest alignment | Verdict |
|---|---|---|---|
| JYP | Requires full Green-like confirmation before strong promotion because revision/margin proof is not initially complete. | Stage2 produced +89.20% 90D MFE with only -1.10% MAE; Green entered after 62.3% of available upside had elapsed. | current_profile_too_late |
| HYBE | Allows Stage2/Yellow and later Green as portfolio demand confirmation arrives. | Stage2 produced +73.64% 90D MFE with -2.41% MAE. | current_profile_correct |
| Studio Dragon | May over-credit K-content/OTT narrative if customer-quality/distribution attention is scored like monetization. | Stage2 produced only +2.59% MFE with -34.44% 180D MAE. | current_profile_false_positive |

Specific calibrated-axis answers:

```text
stage2_actionable_evidence_bonus: useful, but in C27 must require non-price unit-demand evidence.
yellow_threshold_75: appropriate as a watch label for narrative-only content exposure.
green_threshold_87 / revision_55: too strict for JYP-style public unit-demand inflection if applied mechanically, but not globally wrong.
price_only_blowoff_blocks_positive_stage: strengthened; JYP 4B works as overlay only, not positive promotion.
full_4b_requires_non_price_evidence: kept; valuation/positioning overheat works better than price-only local peak.
hard_4c_thesis_break_routes_to_4c: kept, but C27 needs earlier watch when monetization fails to bridge into margin/revision.
```

## 14. Stage2 / Yellow / Green Comparison

| Case | Stage2 entry | Stage3-Green entry | Peak after Stage2 | green_lateness_ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| JYP | 63,900 | 115,400 | 146,600 | 0.623 | Green missed most early upside; Stage2 should be promoted when public unit-demand evidence is strong. |
| HYBE | 174,500 | 245,000 | 312,500 | 0.511 | Green valid but meaningfully late; Stage2 with portfolio breadth was adequate. |
| Studio Dragon | 96,400 | n/a | 98,900 | n/a | No valid Green because margin/revision bridge never closed. |

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | Stage2 ref | 4B entry | local peak | full-window peak | local proximity | full-window proximity | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| JYP 2023-07-25 | 63,900 | 141,100 | 146,600 | 146,600 | 0.93 | 0.93 | good_full_window_4B_timing |

The 4B result strengthens the calibrated distinction: C27 positive promotion should require non-price demand/margin evidence, but 4B should not be blocked when valuation and positioning are stretched after a fast successful rerating.

## 16. 4C Protection Audit

No hard 4C case is counted as calibration-usable 4C in this loop. Studio Dragon is labeled `hard_4c_late` because the false-positive narrative became clear only after price damage. C27 still needs future 4C examples involving artist/contract loss, cancellation, trust break, or platform take-rate deterioration.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_sector_specific_rule
reason = This loop has only one large_sector_id and the proposed rule is better expressed at C27 canonical-archetype scope.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
candidate_rule_1 = C27 unit-demand bridge
if public global unit-demand evidence exists
AND evidence maps to monetizable IP rather than mere distribution attention
AND margin/revision risk is not negative
then Stage2-Actionable may receive a C27 shadow promotion buffer.

candidate_rule_2 = C27 narrative-only guard
if content/IP narrative is based mainly on OTT/global visibility
AND owned-IP economics, margin bridge, or repeat monetization is not visible
then cap positive promotion at Watch/Yellow even if price relative strength is present.

candidate_rule_3 = C27 4B overlay
if fast rerating follows validated unit-demand evidence
AND valuation/positioning becomes stretched near observed peak
then 4B overlay is valid even without a thesis break;
do not route to 4C unless monetization evidence breaks.
```

## 19. Before / After Backtest Comparison

| Profile | Scope | Eligible representative triggers | Avg MFE 90D | Avg MAE 90D | Avg MFE 180D | Avg MAE 180D | False positive rate | Missed structural count | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 55.14% | -9.50% | 70.36% | -12.65% | 33.3% | 1 | mixed; JYP early signal late and Studio Dragon over-credit risk |
| P0b e2r_2_0_baseline_reference | rollback | 3 | lower quality | worse | worse | worse | likely higher | 0 | too loose on narrative-only content |
| P1 sector_specific_candidate_profile | L8 | 3 | same as P2 | same as P2 | same as P2 | same as P2 | lower than P0 | 0 | usable but overbroad |
| P2 C27_candidate_profile | C27 | 3 | improves selection quality | improves | improves | improves | reduced | 0 | preferred |
| P3 counterexample_guard_profile | C27 guard | 3 | caps false positives | improves | improves | improves | lowest | may miss borderline positives | use as guard, not main profile |

## 20. Score-Return Alignment Matrix

| Case | Score before | Label before | Score after | Label after | 90D/180D path | Alignment |
|---|---:|---|---:|---|---|---|
| JYP Stage2 | 50 | Stage2-Actionable | 58 | Stage2-Actionable+ | +89.20% / +129.42% MFE, low MAE | aligned; current profile too late |
| HYBE Stage2 | 48 | Stage2-Actionable | 57 | Stage2-Actionable+ | +73.64% / +79.08% MFE, low MAE | aligned |
| Studio Dragon Stage2 | 38 | Stage2-Actionable | 20 | Watch/No-Promotion | +2.59% MFE, -34.44% 180D MAE | current profile false-positive risk |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION; KPOP_MULTI_LABEL_PORTFOLIO_IP_MONETIZATION; K_DRAMA_OTT_DISTRIBUTION_WITHOUT_MARGIN_CONVERSION | 2 | 1 | 1 | 0 | 3 | 0 | 6 | 3 | 2 | false | true | C27 needs additional 4C thesis-break cases and non-K-pop IP cases. |

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
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - green_late_in_high_quality_kpop_ip_success
  - ott_distribution_narrative_false_positive_without_margin_bridge
new_axis_proposed:
  - c27_unit_demand_bridge_bonus
  - c27_narrative_only_distribution_guard
  - c27_successful_rerating_4b_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C27
  - full_4b_requires_non_price_evidence within C27
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date = 2026-02-20
- representative entry_date/entry_price from tradable shards
- 30D/90D/180D MFE and MAE from tradable_raw OHLC
- corporate-action window status from symbol profiles
- positive/counterexample balance
- 4B local vs full-window proximity for JYP
```

Not validated:

```text
- production scoring code
- live candidates
- any 2026 watchlist
- brokerage/API execution
- portfolio recommendation suitability
- full global rule promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_unit_demand_bridge_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,+2,+2,"public global unit-demand evidence with margin/revision not negative captured JYP/HYBE earlier than Green","improves missed structural timing; JYP/HYBE Stage2 MFE90 89.20/73.64","T_C27_JYP_2023_STAGE2_20230113|T_C27_HYBE_2023_STAGE2_20230113",2,2,0,medium,canonical_shadow_only,"not production; requires batch ledger confirmation"
shadow_weight,c27_narrative_only_distribution_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,-4,-4,"OTT/global distribution narrative without owned-IP margin conversion created Studio Dragon false positive","reduces false positives; Studio Dragon MFE180 2.59 / MAE180 -34.44","T_C27_STUDIO_2021_STAGE2_20211119",1,1,1,medium,canonical_shadow_only,"not production; cap at Watch/Yellow"
shadow_weight,c27_successful_rerating_4b_overlay,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,+1,+1,"validated C27 success can need valuation/positioning 4B overlay after fast rerating","JYP 4B proximity 0.93 and post-peak drawdown -31.04","T_C27_JYP_2023_4B_20230725",1,1,0,low,overlay_shadow_only,"risk overlay only; not positive promotion"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "symbol": "035900", "company_name": "JYP Ent.", "fine_archetype_id": "KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION", "case_id": "C27_JYP_2023_GLOBAL_ALBUMS", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_C27_JYP_2023_STAGE2_20230113", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Global album/tour monetization was already visible before full revision confirmation; Green confirmation captured quality but entered after a large share of upside."}
{"row_type": "case", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "symbol": "352820", "company_name": "하이브", "fine_archetype_id": "KPOP_MULTI_LABEL_PORTFOLIO_IP_MONETIZATION", "case_id": "C27_HYBE_2023_PORTFOLIO_MONETIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_C27_HYBE_2023_STAGE2_20230113", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Multi-label artist portfolio and album/tour cadence reduced single-artist concentration risk enough for C27 structural promotion."}
{"row_type": "case", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "symbol": "253450", "company_name": "스튜디오드래곤", "fine_archetype_id": "K_DRAMA_OTT_DISTRIBUTION_WITHOUT_MARGIN_CONVERSION", "case_id": "C27_STUDIO_DRAGON_2021_OTT_NARRATIVE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T_C27_STUDIO_2021_STAGE2_20211119", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Global OTT/K-content narrative had public proof, but margin/revision and owned-IP economics did not close; price path delivered almost no MFE with large MAE."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "T_C27_JYP_2023_STAGE2_20230113", "case_id": "C27_JYP_2023_GLOBAL_ALBUMS", "symbol": "035900", "company_name": "JYP Ent.", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-13", "entry_date": "2023-01-13", "entry_price": 63900, "evidence_available_at_that_date": "pre-confirmation global fanbase monetization: Stray Kids/TWICE album and tour cadence was visible, but full quarterly revision/margin proof was not yet complete.", "evidence_source": "public artist release/order cadence; later confirmed by 2023 Circle/IFPI album data and stock-web OHLC row.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 21.44, "MFE_90D_pct": 89.2, "MFE_180D_pct": 129.42, "MFE_1Y_pct": 129.42, "MFE_2Y_pct": 129.42, "MAE_30D_pct": -1.1, "MAE_90D_pct": -1.1, "MAE_180D_pct": -1.1, "MAE_1Y_pct": -1.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -31.04, "green_lateness_ratio": "0.623_vs_Stage3_Green_2023-05-16", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_mfe_low_mae", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "G_C27_JYP_20230113_63900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "fine_archetype_id": "KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "T_C27_JYP_2023_GREEN_20230516", "case_id": "C27_JYP_2023_GLOBAL_ALBUMS", "symbol": "035900", "company_name": "JYP Ent.", "trigger_type": "Stage3-Green", "trigger_date": "2023-05-16", "entry_date": "2023-05-16", "entry_price": 115400, "evidence_available_at_that_date": "large public album demand and revision/margin confirmation became hard enough for Green, but the price had already repriced materially.", "evidence_source": "stock-web OHLC row around 2023-05-16 and public album demand milestones.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 20.1, "MFE_90D_pct": 27.04, "MFE_180D_pct": 27.04, "MFE_1Y_pct": 27.04, "MFE_2Y_pct": 27.04, "MAE_30D_pct": -4.16, "MAE_90D_pct": -12.39, "MAE_180D_pct": -12.39, "MAE_1Y_pct": -12.39, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -31.04, "green_lateness_ratio": 0.623, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_late_but_valid", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "G_C27_JYP_20230516_115400", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "fine_archetype_id": "KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "T_C27_JYP_2023_4B_20230725", "case_id": "C27_JYP_2023_GLOBAL_ALBUMS", "symbol": "035900", "company_name": "JYP Ent.", "trigger_type": "Stage4B", "trigger_date": "2023-07-25", "entry_date": "2023-07-25", "entry_price": 141100, "evidence_available_at_that_date": "price was at/near observed cycle peak; valuation and positioning were stretched after a rapid rerating.", "evidence_source": "stock-web OHLC row: 2023-07-25 high 146600 close 141100.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "MFE_30D_pct": 3.9, "MFE_90D_pct": 3.9, "MFE_180D_pct": 3.9, "MFE_1Y_pct": 3.9, "MFE_2Y_pct": 3.9, "MAE_30D_pct": -26.29, "MAE_90D_pct": -28.35, "MAE_180D_pct": -28.35, "MAE_1Y_pct": -28.35, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -31.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "G_C27_JYP_20230725_141100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "fine_archetype_id": "KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "T_C27_HYBE_2023_STAGE2_20230113", "case_id": "C27_HYBE_2023_PORTFOLIO_MONETIZATION", "symbol": "352820", "company_name": "하이브", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-13", "entry_date": "2023-01-13", "entry_price": 174500, "evidence_available_at_that_date": "portfolio-level IP monetization was visible through multi-label album cadence and non-BTS artist growth, while BTS hiatus risk was already partly known.", "evidence_source": "public artist portfolio/album cadence; later confirmed by sector album sales and stock-web OHLC row.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 25.21, "MFE_90D_pct": 73.64, "MFE_180D_pct": 79.08, "MFE_1Y_pct": 79.08, "MFE_2Y_pct": 128.37, "MAE_30D_pct": -0.86, "MAE_90D_pct": -2.41, "MAE_180D_pct": -2.41, "MAE_1Y_pct": -2.41, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-22", "peak_price": 312500, "drawdown_after_peak_pct": -29.28, "green_lateness_ratio": "0.511_vs_Stage3_Green_2023-04-13", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_mfe_low_mae", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "G_C27_HYBE_20230113_174500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "fine_archetype_id": "KPOP_MULTI_LABEL_PORTFOLIO_IP_MONETIZATION", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv", "profile_path": "atlas/symbol_profiles/352/352820.json", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "T_C27_HYBE_2023_GREEN_20230413", "case_id": "C27_HYBE_2023_PORTFOLIO_MONETIZATION", "symbol": "352820", "company_name": "하이브", "trigger_type": "Stage3-Green", "trigger_date": "2023-04-13", "entry_date": "2023-04-13", "entry_price": 245000, "evidence_available_at_that_date": "revision and portfolio confirmation became stronger; Green was valid but entered halfway through the available upside from the Stage2 reference.", "evidence_source": "stock-web OHLC row around 2023-04-13.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 23.67, "MFE_90D_pct": 27.55, "MFE_180D_pct": 27.55, "MFE_1Y_pct": 27.55, "MFE_2Y_pct": 62.65, "MAE_30D_pct": -5.51, "MAE_90D_pct": -5.51, "MAE_180D_pct": -17.55, "MAE_1Y_pct": -23.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-22", "peak_price": 312500, "drawdown_after_peak_pct": -29.28, "green_lateness_ratio": 0.511, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_valid_but_partially_late", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "G_C27_HYBE_20230413_245000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "fine_archetype_id": "KPOP_MULTI_LABEL_PORTFOLIO_IP_MONETIZATION", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv", "profile_path": "atlas/symbol_profiles/352/352820.json", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
{"row_type": "trigger", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "T_C27_STUDIO_2021_STAGE2_20211119", "case_id": "C27_STUDIO_DRAGON_2021_OTT_NARRATIVE", "symbol": "253450", "company_name": "스튜디오드래곤", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-11-19", "entry_date": "2021-11-19", "entry_price": 96400, "evidence_available_at_that_date": "K-content/OTT narrative was highly visible after global Korean drama momentum, but margin bridge and owned-IP monetization visibility were weak.", "evidence_source": "public K-content/OTT narrative and stock-web OHLC row; later path shows narrative without margin conversion.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "MFE_30D_pct": 2.59, "MFE_90D_pct": 2.59, "MFE_180D_pct": 2.59, "MFE_1Y_pct": 2.59, "MFE_2Y_pct": 2.59, "MAE_30D_pct": -13.28, "MAE_90D_pct": -25.0, "MAE_180D_pct": -34.44, "MAE_1Y_pct": -39.63, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-22", "peak_price": 98900, "drawdown_after_peak_pct": -36.1, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating_false_positive_stage2", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "G_C27_STUDIO_20211119_96400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "fine_archetype_id": "K_DRAMA_OTT_DISTRIBUTION_WITHOUT_MARGIN_CONVERSION", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv", "profile_path": "atlas/symbol_profiles/253/253450.json", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": []}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_JYP_2023_GLOBAL_ALBUMS", "trigger_id": "T_C27_JYP_2023_STAGE2_20230113", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 7, "revision_score": 10, "relative_strength_score": 13, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 50, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 9, "revision_score": 13, "relative_strength_score": 15, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 60, "stage_label_after": "Stage2-Actionable+", "changed_components": ["customer_quality_score", "relative_strength_score", "revision_score", "margin_bridge_score"], "component_delta_explanation": "C27 adds earlier credit when global album/order data is public and not merely price-only.", "MFE_90D_pct": 89.2, "MAE_90D_pct": -1.1, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_JYP_2023_GLOBAL_ALBUMS", "trigger_id": "T_C27_JYP_2023_GREEN_20230516", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 59, "stage_label_before": "Stage3/Overlay", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 59, "stage_label_after": "Stage3/Overlay", "changed_components": [], "component_delta_explanation": "Label comparison or 4B overlay; not a new entry promotion row.", "MFE_90D_pct": 27.04, "MAE_90D_pct": -12.39, "score_return_alignment_label": "mixed", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_JYP_2023_GLOBAL_ALBUMS", "trigger_id": "T_C27_JYP_2023_4B_20230725", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 59, "stage_label_before": "Stage3/Overlay", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 59, "stage_label_after": "Stage3/Overlay", "changed_components": [], "component_delta_explanation": "Label comparison or 4B overlay; not a new entry promotion row.", "MFE_90D_pct": 3.9, "MAE_90D_pct": -28.35, "score_return_alignment_label": "false_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_HYBE_2023_PORTFOLIO_MONETIZATION", "trigger_id": "T_C27_HYBE_2023_STAGE2_20230113", "symbol": "352820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 8, "revision_score": 11, "relative_strength_score": 10, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 49, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 10, "revision_score": 14, "relative_strength_score": 10, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 59, "stage_label_after": "Stage2-Actionable+", "changed_components": ["customer_quality_score", "revision_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Multi-label portfolio reduces single IP concentration risk; C27 permits promotion before final Green.", "MFE_90D_pct": 73.64, "MAE_90D_pct": -2.41, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_HYBE_2023_PORTFOLIO_MONETIZATION", "trigger_id": "T_C27_HYBE_2023_GREEN_20230413", "symbol": "352820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 59, "stage_label_before": "Stage3/Overlay", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 8, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 59, "stage_label_after": "Stage3/Overlay", "changed_components": [], "component_delta_explanation": "Label comparison or 4B overlay; not a new entry promotion row.", "MFE_90D_pct": 27.55, "MAE_90D_pct": -5.51, "score_return_alignment_label": "mixed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C27_counterexample_guard_profile", "case_id": "C27_STUDIO_DRAGON_2021_OTT_NARRATIVE", "trigger_id": "T_C27_STUDIO_2021_STAGE2_20211119", "symbol": "253450", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 9, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 38, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 3, "valuation_repricing_score": 3, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 17, "stage_label_after": "Watch/No-Promotion", "changed_components": ["customer_quality_score", "margin_bridge_score", "revision_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "OTT distribution narrative is down-weighted without owned-IP margin conversion and revision bridge.", "MFE_90D_pct": 2.59, "MAE_90D_pct": -25.0, "score_return_alignment_label": "false_positive", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_unit_demand_bridge_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,+2,+2,"public global unit-demand evidence with margin/revision not negative captured JYP/HYBE earlier than Green","improves missed structural timing","T_C27_JYP_2023_STAGE2_20230113|T_C27_HYBE_2023_STAGE2_20230113",2,2,0,medium,canonical_shadow_only,"not production"
shadow_weight,c27_narrative_only_distribution_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,-4,-4,"OTT/global distribution narrative without owned-IP margin conversion created false positive","reduces false positives","T_C27_STUDIO_2021_STAGE2_20211119",1,1,1,medium,canonical_shadow_only,"not production"
shadow_weight,c27_successful_rerating_4b_overlay,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,+1,+1,"valuation/positioning overlay after validated successful rerating","improves 4B timing","T_C27_JYP_2023_4B_20230725",1,1,0,low,overlay_shadow_only,"not production"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "22", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 1, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["green_late_in_high_quality_kpop_ip_success", "ott_distribution_narrative_false_positive_without_margin_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R8 C27 had no direct duplicate in artifact search and needed positive/counterexample/4B coverage."}
```

### 25.7 narrative_only rows

```jsonl
```

No narrative-only rows were used. Every selected case had an available 180D stock-web forward window.

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
next_round = R13_C32_HARD_4C_AFTERPATH or R5_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
reason = C27 now has positive/counterexample/4B coverage, but still lacks true 4C thesis-break cases. A separate 4C loop should use contract/artist/regulatory/accounting break evidence.
```

## 28. Source Notes

```text
Stock-web source files inspected:
- atlas/manifest.json
- atlas/symbol_profiles/035/035900.json
- atlas/symbol_profiles/352/352820.json
- atlas/symbol_profiles/253/253450.json
- atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/253/253450/2022.csv

Stock_agent artifact access:
- search only; no stock_agent code opened
- no src/e2r access
- no production patch
```
