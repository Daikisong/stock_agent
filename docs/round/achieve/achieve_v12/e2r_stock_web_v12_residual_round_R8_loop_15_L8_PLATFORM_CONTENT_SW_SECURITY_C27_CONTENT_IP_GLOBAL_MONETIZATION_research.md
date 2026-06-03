# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- scheduled_round: `R8`
- scheduled_loop: `15`
- completed_round: `R8`
- completed_loop: `15`
- output_file: `e2r_stock_web_v12_residual_round_R8_loop_15_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md`
- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C27_CONTENT_IP_GLOBAL_MONETIZATION`
- fine_archetype_id: `GLOBAL_IP_MONETIZATION_CONVERSION_BRIDGE`
- loop_objective: `coverage_gap_fill | counterexample_mining | residual_false_positive_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression`
- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- handoff_prompt_embedded: `true`
- handoff_prompt_executed_now: `false`

This loop adds 3 new independent cases, 1 counterexample, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption

The research assumes the already-applied calibrated proxy:

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

The purpose is not to re-prove these axes. The residual question for R8/C27 is narrower: in content/IP names, when does global attention become monetizable evidence, and when is it only a spectacular trailer-shaped fuse?

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R8 |
| scheduled_loop | 15 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| round_sector_consistency | pass |
| next_round | R9 |
| next_loop | 15 |

R8 hard gate is satisfied because R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`.

## 3. Previous Coverage / Duplicate Avoidance Check

The previous conversation state gave `next_round = R8`, `next_loop = 15`. `stock_agent` research-artifact lookup did not reveal a conflicting v12 R8 result under the exact filename pattern. To avoid the typical platform-ad repetition, this loop selects C27 content/IP instead of C26 platform advertising.

Duplicate-avoidance decisions:

| Candidate | Decision |
|---|---|
| NAVER/Kakao ad-recovery platform cases | skipped; too likely to repeat generic platform operating leverage |
| HYBE Ithaca acquisition | selected; cross-border IP/label acquisition route |
| JYP Maxident / Stray Kids global album evidence | selected; album-to-tour/earnings conversion route |
| Pearl Abyss DokeV trailer | selected; high-MFE false-positive counterexample without launch/revenue bridge |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields confirmed:

| Field | Value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema confirms tradable columns: `d,o,h,l,c,v,a,mc,s,m`. Raw columns add `rs`. No repaired OHLC is used.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available | corporate-action overlap | calibration_usable |
|---|---:|---:|---:|---:|---:|
| R8L15_C27_HYBE_ITHACA_202104 | 352820 | 2021-04-05 | true | none | true |
| R8L15_C27_JYP_MAXIDENT_202211 | 035900 | 2022-11-18 | true | none in 2022-2023 window | true |
| R8L15_C27_PEARLABYSS_DOKEV_202108 | 263750 | 2021-08-26 | true | profile candidate 2021-04-16 is before entry window | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | Compression note |
|---|---|---|
| C27_CONTENT_IP_GLOBAL_MONETIZATION | GLOBAL_LABEL_PLATFORM_ACQUISITION_MONETIZATION | Partner/acquisition route: real distribution and artist-IP surface expands. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | ALBUM_TOUR_GLOBAL_MONETIZATION_CONVERSION | Album sales, tour, Billboard/global fanbase signals convert into financial visibility. |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | GAMEPLAY_TRAILER_WITHOUT_COMMERCIALIZATION_BRIDGE | Attention route: strong trailer does not equal launch/revenue conversion. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best trigger | outcome |
|---|---:|---|---|---|---|
| R8L15_C27_HYBE_ITHACA_202104 | 352820 | 하이브 | positive_structural_success | Stage2-Actionable 2021-04-05 | +69.96% 180D MFE; later 4B near full peak |
| R8L15_C27_JYP_MAXIDENT_202211 | 035900 | JYP Ent. | positive_structural_success | Stage2-Actionable 2022-11-18 | +146.39% 180D MFE; Green label late |
| R8L15_C27_PEARLABYSS_DOKEV_202108 | 263750 | 펄어비스 | failed_rerating / counterexample | Stage2-Actionable 2021-08-26 | +65.19% MFE but -60.61% post-peak drawdown |

## 8. Positive vs Counterexample Balance

- positive_case_count: `2`
- counterexample_count: `1`
- 4B_case_count: `2`
- 4C_case_count: `1`
- calibration_usable_case_count: `3`

This is acceptable for a canonical-archetype-specific shadow rule candidate, not enough for a global rule.

## 9. Evidence Source Map

| case | evidence timing | evidence family | source note |
|---|---|---|---|
| HYBE | 2021-04-02 event, 2021-04-05 entry | acquisition / partner IP / global management route | HYBE acquisition of Ithaca Holdings was public on 2021-04-02; external reports describe the acquisition as valued at over $1bn and adding artists such as Justin Bieber and Ariana Grande to HYBE’s global orbit. |
| JYP | 2022-11-17 event, 2022-11-18 entry | album global proof / repeat conversion | Maxident evidence includes Billboard 200 No. 1 and triple-million/album-sales evidence; later tour and financial conversion validated the route. |
| Pearl Abyss | 2021-08-25 event, 2021-08-26 entry | gameplay trailer / attention without commercialization bridge | DokeV trailer premiered at Gamescom Opening Night Live, but later public reporting shows long delay/no near-term monetization bridge. |

## 10. Price Data Source Map

| symbol | shard(s) | profile |
|---:|---|---|
| 352820 | `atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv` | `atlas/symbol_profiles/352/352820.json` |
| 035900 | `atlas/ohlcv_tradable_by_symbol_year/035/035900/2022.csv`, `2023.csv` | `atlas/symbol_profiles/035/035900.json` |
| 263750 | `atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv`, `2022.csv` | `atlas/symbol_profiles/263/263750.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | symbol | trigger_date | entry_date | entry_price | evidence | representative |
|---|---|---:|---:|---:|---:|---|---:|
| R8L15_C27_HYBE_T1_STAGE2_ACTIONABLE | Stage2-Actionable | 352820 | 2021-04-02 | 2021-04-05 | 248000 | Ithaca acquisition/global label route | true |
| R8L15_C27_HYBE_T2_4B_OVERLAY | 4B | 352820 | 2021-11-04 | 2021-11-05 | 383500 | valuation/platform/NFT expansion overheat | false |
| R8L15_C27_JYP_T1_STAGE2_ACTIONABLE | Stage2-Actionable | 035900 | 2022-11-17 | 2022-11-18 | 59500 | Maxident / global album proof | true |
| R8L15_C27_JYP_T2_STAGE3_GREEN | Stage3-Green | 035900 | 2023-05-15 | 2023-05-16 | 115400 | financial/tour conversion visible | false |
| R8L15_C27_PEARL_T1_STAGE2_ACTIONABLE | Stage2-Actionable | 263750 | 2021-08-25 | 2021-08-26 | 87900 | DokeV trailer, no launch/revenue bridge | true |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L15_C27_HYBE_T1_STAGE2_ACTIONABLE | 248000 | 14.92% | -8.27% | 35.89% | -8.27% | 69.96% | -8.27% | 2021-11-17 | 421500 | -23.37% |
| R8L15_C27_HYBE_T2_4B_OVERLAY | 383500 | 9.91% | -15.78% | 9.91% | -30.25% | 9.91% | -40.55% | 2021-11-17 | 421500 | -23.37% |
| R8L15_C27_JYP_T1_STAGE2_ACTIONABLE | 59500 | 14.96% | -2.69% | 36.64% | -2.69% | 146.39% | -2.69% | 2023-07-25 | 146600 | -22.72% |
| R8L15_C27_JYP_T2_STAGE3_GREEN | 115400 | 21.84% | -5.03% | 27.04% | -12.48% | 27.04% | -13.69% | 2023-07-25 | 146600 | -22.72% |
| R8L15_C27_PEARL_T1_STAGE2_ACTIONABLE | 87900 | 16.04% | -11.72% | 65.19% | -11.72% | 65.19% | -34.93% | 2021-11-17 | 145200 | -60.61% |

## 13. Current Calibrated Profile Stress Test

| case | current_profile_verdict | Stress conclusion |
|---|---|---|
| HYBE | current_profile_correct | Stage2/Yellow promotion is justified; 4B overlay near 0.78 full-window proximity works. |
| JYP | current_profile_too_late | Green threshold is directionally safe but late; Stage2 evidence should retain more conviction in C27 when album/tour route is measurable. |
| Pearl Abyss | current_profile_false_positive | A trailer-only route can fool relative-strength and valuation repricing components. It requires launch/revenue bridge before Green. |

## 14. Stage2 / Yellow / Green Comparison

JYP is the main lateness audit.

```text
Stage2_Actionable_entry_price = 59,500
Stage3_Green_entry_price      = 115,400
peak_after_Stage2             = 146,600

green_lateness_ratio = (115400 - 59500) / (146600 - 59500) = 0.642
```

Interpretation: Green caught the monetization path, but after roughly 64% of the Stage2-to-peak upside had already been consumed.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| HYBE 4B | 0.78 | 0.78 | good_full_window_4B_timing |
| Pearl Abyss trailer hype | 0.88 | 0.88 | good price-risk overlay, but not a positive Green promotion |

The split matters. In content/IP, a local peak can be a warning flare, not a thesis break. Full 4B should require non-price evidence: valuation blowoff, platform strategy overreach, launch delay, or execution-risk evidence.

## 16. 4C Protection Audit

Pearl Abyss supplies the 4C lesson. The high in the window was 145,200 on 2021-11-17. The window later saw lows around 57,200 in May 2022, creating a roughly -60.61% drawdown from peak. If the system waited for hard evidence after the market had already priced the trailer as a launch-probability event, protection was late.

Protection label: `hard_4c_late`.

## 17. Sector-Specific Rule Candidate

No sector-wide L8 rule is proposed. The cases are all C27, and the observed behavior is archetype-specific rather than universal across platform advertising, software retention, and content IP.

```text
sector_specific_rule_candidate = false
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
```

Candidate rule:

```text
C27 Green requires at least one commercialization bridge:
- partner/distribution/acquisition route with identifiable global IP monetization;
- repeated album/tour/streaming conversion that is visible before or around trigger;
- contracted platform/license/launch route;
- financial revision or margin bridge that confirms conversion.

Trailer-only, teaser-only, or fandom-attention events can be Stage2-Actionable,
but should not become Stage3-Green without the conversion bridge.
```

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | late_green_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current calibrated profile | 45.91% | -7.56% | 93.85% | -15.30% | 33% | 1 | good but allows trailer false-positive |
| P0b e2r_2_0_baseline_reference | older looser profile | 45.91% | -7.56% | 93.85% | -15.30% | 33%+ | 0 | too much price/IP hype leakage |
| P1 sector_specific_candidate_profile | L8 blanket rule | 45.91% | -7.56% | 93.85% | -15.30% | unchanged | unchanged | not enough sector breadth |
| P2 canonical_archetype_candidate_profile | C27 conversion bridge rule | 45.91% | -7.56% | 93.85% | -15.30% | lower; Pearl blocked from Green | 1 retained | best explanatory fit |
| P3 counterexample_guard_profile | trailer-only Green block | 45.91% | -7.56% | 93.85% | -15.30% | lower | 1 | useful as guardrail |

Representative aggregate uses three deduped entries: HYBE Stage2, JYP Stage2, Pearl Stage2.

## 20. Score-Return Alignment Matrix

| case | P0 label | proposed shadow label | actual path | alignment |
|---|---|---|---|---|
| HYBE | Stage3-Yellow | Stage3-Yellow with 4B overlay later | strong 180D MFE, peak near 4B | aligned |
| JYP | Stage2/Yellow until confirmed Green | Stage2 conviction retained; Green still late | strong 180D MFE | P0 too late |
| Pearl Abyss | Stage3-Yellow risk | Stage2-Actionable/Watch, no Green | high MFE then severe drawdown | P0 false-positive risk |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | GLOBAL_IP_MONETIZATION_CONVERSION_BRIDGE | 2 | 1 | 2 | 1 | 3 | 0 | 5 | 3 | 3 | false | true | still needs pure streaming/platform-license and content-production cost inflation cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - trailer_without_commercialization_bridge_false_positive
  - stage3_green_late_after_album_tour_conversion
  - price_only_local_peak_requires_4B_overlay
new_axis_proposed:
  - C27_conversion_bridge_required_for_Green
  - C27_partner_or_platform_IP_bonus
  - C27_price_only_local_peak_4B_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- historical trigger-level backtest on stock-web tradable raw OHLC rows;
- entry-date close, 30D/90D/180D MFE and MAE;
- C27-specific positive/counterexample balance;
- current calibrated profile stress test;
- 4B local/full-window split;
- same-entry dedupe for aggregate.

Not validated:

- no current/live candidate scan;
- no recommendation;
- no production scoring change;
- no `src/e2r` code inspection;
- no brokerage or auto-trading integration.


Calculation caveat: quantitative calibration weight should use the 30D/90D/180D rows. The 1Y/2Y fields are carried as reference fields in the required schema and should be re-derived by the later batch implementation before any production promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_conversion_bridge_required_for_Green,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Trailer/attention-only IP events can produce large MFE but fail durability without launch/revenue conversion bridge","Pearl Abyss false positive blocked while HYBE/JYP remain Stage2/Yellow","R8L15_C27_PEARL_T1_STAGE2_ACTIONABLE|R8L15_C27_JYP_T2_STAGE3_GREEN",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_partner_or_platform_IP_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Cross-border partner or proven distribution route improves non-price evidence quality","HYBE/JYP positive cases keep early promotion while trailer-only hype is not promoted to Green","R8L15_C27_HYBE_T1_STAGE2_ACTIONABLE|R8L15_C27_JYP_T1_STAGE2_ACTIONABLE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_price_only_local_peak_4B_overlay,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Content IP names often create local peaks before revenue proof; 4B should be overlay unless non-price commercialization risk is visible","HYBE 4B timing near full peak; Pearl Abyss peak risk appears before thesis break","R8L15_C27_HYBE_T2_4B_OVERLAY|R8L15_C27_PEARL_T1_STAGE2_ACTIONABLE",3,3,1,low,canonical_shadow_only,"not production; post-calibrated residual"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L15_C27_HYBE_ITHACA_202104", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_LABEL_PLATFORM_ACQUISITION_MONETIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L15_C27_HYBE_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "partner/acquisition-backed global IP expansion aligned with strong 90D/180D MFE, but later platform/NFT overheat needed 4B overlay", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Ithaca acquisition created non-price global IP/management route; clean profile window, no corporate action candidate dates."}
{"row_type": "case", "case_id": "R8L15_C27_JYP_MAXIDENT_202211", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ALBUM_TOUR_GLOBAL_MONETIZATION_CONVERSION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L15_C27_JYP_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "album global proof and later financial/tour conversion produced very high 180D MFE; Stage3 Green was late", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Stray Kids global album evidence preceded earnings conversion; no corporate-action candidate window in 2022-2023."}
{"row_type": "case", "case_id": "R8L15_C27_PEARLABYSS_DOKEV_202108", "symbol": "263750", "company_name": "펄어비스", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAMEPLAY_TRAILER_WITHOUT_COMMERCIALIZATION_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L15_C27_PEARL_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "trailer-driven IP enthusiasm created high MFE but no launch/revenue bridge led to severe post-peak drawdown", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "DokeV trailer was a valid non-price IP awareness event but not sufficient for durable Green without launch schedule/commercial conversion."}
{"row_type": "trigger", "trigger_id": "R8L15_C27_HYBE_T1_STAGE2_ACTIONABLE", "case_id": "R8L15_C27_HYBE_ITHACA_202104", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_LABEL_PLATFORM_ACQUISITION_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-04-02", "entry_date": "2021-04-05", "entry_price": 248000, "evidence_available_at_that_date": "HYBE/Ithaca acquisition news created a cross-border artist-management and label IP route; timing assumed next trading day because exact market-time availability was not relied on.", "evidence_source": "HYBE/Ithaca acquisition public reports, April 2021; stock-web 2021 tradable shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["durable_customer_confirmation", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv", "profile_path": "atlas/symbol_profiles/352/352820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.92, "MFE_90D_pct": 35.89, "MFE_180D_pct": 69.96, "MFE_1Y_pct": 69.96, "MFE_2Y_pct": 69.96, "MAE_30D_pct": -8.27, "MAE_90D_pct": -8.27, "MAE_180D_pct": -8.27, "MAE_1Y_pct": -12.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-17", "peak_price": 421500, "drawdown_after_peak_pct": -23.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_high_MFE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L15_C27_HYBE_20210405", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L15_C27_HYBE_T2_4B_OVERLAY", "case_id": "R8L15_C27_HYBE_ITHACA_202104", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_LABEL_PLATFORM_ACQUISITION_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "4B", "trigger_date": "2021-11-04", "entry_date": "2021-11-05", "entry_price": 383500, "evidence_available_at_that_date": "Platform/NFT/webtoon expansion narrative and valuation overheat arrived near the full-cycle high after the acquisition rerating.", "evidence_source": "public strategy/NFT/platform reports around November 2021; stock-web 2021 tradable shard.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv", "profile_path": "atlas/symbol_profiles/352/352820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.91, "MFE_90D_pct": 9.91, "MFE_180D_pct": 9.91, "MFE_1Y_pct": 9.91, "MFE_2Y_pct": 9.91, "MAE_30D_pct": -15.78, "MAE_90D_pct": -30.25, "MAE_180D_pct": -40.55, "MAE_1Y_pct": -50.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-17", "peak_price": 421500, "drawdown_after_peak_pct": -23.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L15_C27_HYBE_20211105", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L15_C27_JYP_T1_STAGE2_ACTIONABLE", "case_id": "R8L15_C27_JYP_MAXIDENT_202211", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ALBUM_TOUR_GLOBAL_MONETIZATION_CONVERSION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|yellow_threshold_stress_test|green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-11-17", "entry_date": "2022-11-18", "entry_price": 59500, "evidence_available_at_that_date": "Stray Kids Maxident crossed triple-million evidence; the trigger is treated as next-trading-day close because publication timing is not used for intraday entry.", "evidence_source": "Maxident triple-million/Billboard 200 evidence; stock-web 2022-2023 tradable shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["repeat_order_or_conversion", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2022.csv|atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.96, "MFE_90D_pct": 36.64, "MFE_180D_pct": 146.39, "MFE_1Y_pct": 146.39, "MFE_2Y_pct": 146.39, "MAE_30D_pct": -2.69, "MAE_90D_pct": -2.69, "MAE_180D_pct": -2.69, "MAE_1Y_pct": -2.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -22.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success_high_MFE", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L15_C27_JYP_20221118", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L15_C27_JYP_T2_STAGE3_GREEN", "case_id": "R8L15_C27_JYP_MAXIDENT_202211", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ALBUM_TOUR_GLOBAL_MONETIZATION_CONVERSION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2023-05-15", "entry_date": "2023-05-16", "entry_price": 115400, "evidence_available_at_that_date": "Financial/tour conversion became visible; Green label is accurate but late against the earlier album evidence.", "evidence_source": "stock-web 2023 tradable shard; public earnings/tour monetization evidence.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.84, "MFE_90D_pct": 27.04, "MFE_180D_pct": 27.04, "MFE_1Y_pct": 27.04, "MFE_2Y_pct": 27.04, "MAE_30D_pct": -5.03, "MAE_90D_pct": -12.48, "MAE_180D_pct": -13.69, "MAE_1Y_pct": -13.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -22.72, "green_lateness_ratio": 0.642, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "green_late_but_valid", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L15_C27_JYP_20230516", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L15_C27_PEARL_T1_STAGE2_ACTIONABLE", "case_id": "R8L15_C27_PEARLABYSS_DOKEV_202108", "symbol": "263750", "company_name": "펄어비스", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAMEPLAY_TRAILER_WITHOUT_COMMERCIALIZATION_BRIDGE", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-08-25", "entry_date": "2021-08-26", "entry_price": 87900, "evidence_available_at_that_date": "DokeV gameplay trailer created global attention, but no launch-date/booking/revenue bridge was available at trigger.", "evidence_source": "Gamescom DokeV trailer reports; stock-web 2021-2022 tradable shards.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv|atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv", "profile_path": "atlas/symbol_profiles/263/263750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.04, "MFE_90D_pct": 65.19, "MFE_180D_pct": 65.19, "MFE_1Y_pct": 65.19, "MFE_2Y_pct": 65.19, "MAE_30D_pct": -11.72, "MAE_90D_pct": -11.72, "MAE_180D_pct": -34.93, "MAE_1Y_pct": -46.64, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-17", "peak_price": 145200, "drawdown_after_peak_pct": -60.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_price_risk_but_not_full_positive_green", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating_high_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L15_C27_PEARL_20210826", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L15_C27_HYBE_ITHACA_202104", "trigger_id": "R8L15_C27_HYBE_T1_STAGE2_ACTIONABLE", "symbol": "352820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 11, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 11, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "valuation_repricing_score"], "component_delta_explanation": "Research proxy only. C27 shadow adds conversion/launch bridge logic and blocks trailer-only Green promotion.", "MFE_90D_pct": 35.89, "MAE_90D_pct": -8.27, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L15_C27_JYP_MAXIDENT_202211", "trigger_id": "R8L15_C27_JYP_T1_STAGE2_ACTIONABLE", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 12, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 12, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "revision_score"], "component_delta_explanation": "Research proxy only. C27 shadow adds conversion/launch bridge logic and blocks trailer-only Green promotion.", "MFE_90D_pct": 36.64, "MAE_90D_pct": -2.69, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L15_C27_JYP_MAXIDENT_202211", "trigger_id": "R8L15_C27_JYP_T2_STAGE3_GREEN", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 56, "relative_strength_score": 0, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 54, "relative_strength_score": 0, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Green", "changed_components": ["revision_score"], "component_delta_explanation": "Research proxy only. C27 shadow adds conversion/launch bridge logic and blocks trailer-only Green promotion.", "MFE_90D_pct": 27.04, "MAE_90D_pct": -12.48, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L15_C27_PEARLABYSS_DOKEV_202108", "trigger_id": "R8L15_C27_PEARL_T1_STAGE2_ACTIONABLE", "symbol": "263750", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable/Watch", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Research proxy only. C27 shadow adds conversion/launch bridge logic and blocks trailer-only Green promotion.", "MFE_90D_pct": 65.19, "MAE_90D_pct": -11.72, "score_return_alignment_label": "misaligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R8", "loop": "15", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "scheduled_round": "R8", "scheduled_loop": "15", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["trailer_without_commercialization_bridge_false_positive", "stage3_green_late_after_album_tour_conversion", "price_only_local_peak_requires_4B_overlay"], "loop_contribution_label": "canonical_archetype_rule_candidate", "diversity_score_summary": "new_symbol_bonus=+9; counterexample_gap_bonus=+4; new_trigger_family_bonus=+20; residual_error_bonus=+10; wrong_round_penalty=0; net high", "do_not_propose_new_weight_delta": false}
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
completed_round = R8
completed_loop = 15
next_round = R9
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files read or referenced:

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/symbol_profiles/352/352820.json`
- `atlas/symbol_profiles/035/035900.json`
- `atlas/symbol_profiles/263/263750.json`
- `atlas/ohlcv_tradable_by_symbol_year/352/352820/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035900/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv`

Public evidence references used for narrative source mapping:

- HYBE/Ithaca acquisition reports from April 2021.
- JYP/Stray Kids `Maxident` global album sales and Billboard 200 evidence.
- Pearl Abyss/DokeV Gamescom 2021 trailer and later delay/non-commercialization references.

The numeric OHLC fields are derived from stock-web tradable shards only. They are research proxy calculations, not investment advice and not production scoring changes.

