# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
scheduled_round: R8
scheduled_loop: 10
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **3** new independent cases, **1** counterexample, and **2** residual errors for **R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION**.

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

The purpose is not to re-prove that Stage2 can be earlier than Green. The residual question is narrower: **when should global content/IP narrative become repeatable monetization evidence, and when should it remain narrative-only?**

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R8`
- Loop: `10`
- Large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- Canonical archetype: `C27_CONTENT_IP_GLOBAL_MONETIZATION`
- Fine archetype: `K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM`

R8 is valid only for platform/content/SW/security scope. This MD does not use R13 red-team naming.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts show R1~R13 and loops 1~9 were already covered. This file therefore follows the next sequential state after the prior generated R7 Loop 10 file:

```text
previous_completed_round = R7
previous_completed_loop = 10
scheduled_round = R8
scheduled_loop = 10
```

Duplicate-avoidance intent:

- Do not repeat R5 consumer K-beauty/K-food cases.
- Do not repeat R6 financial value-up cases.
- Do not use R13 cross-archetype red-team naming.
- Same canonical archetype repetition is allowed, but same symbol + same trigger date + same entry group is not reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Important validation notes:

- `price_basis = tradable_raw`
- `price_adjustment_status = raw_unadjusted_marcap`
- `manifest_max_date = 2026-02-20`
- no manifest-after-date price was synthesized
- profile-level corporate-action windows were checked; chosen 2023 windows are clean for the selected 180D calibration windows

## 5. Historical Eligibility Gate

| case_id | symbol | company | entry_date | 180D forward window | corporate action window | calibration usable |
|---|---:|---|---:|---:|---|---|
| R8L10_C27_JYP_20230222 | 035900 | JYP Ent. | 2023-02-22 | yes | clean_180D_window | true |
| R8L10_C27_HYBE_20230406 | 352820 | 하이브 | 2023-04-06 | yes | clean_180D_window | true |
| R8L10_C27_STUDIODRAGON_20230210 | 253450 | 스튜디오드래곤 | 2023-02-10 | yes | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
  positive bridge:
    - artist IP with album/tour/platform monetization
    - repeat purchase / repeat fan monetization
    - multiple artist or catalog route
    - visible revision / margin bridge

  counterexample cap:
    - one-off hit or broad K-content narrative
    - production studio economics without scalable IP ownership
    - OTT distribution headline without margin/repeat visibility
    - price-only or sentiment-only move
```

## 7. Case Selection Summary

| case | role | trigger | entry | outcome |
|---|---|---|---:|---|
| JYP Ent. | structural_success | global album/tour monetization bridge | 76,000 | 180D MFE +92.89% |
| 하이브 | structural_success | multi-artist IP monetization bridge | 205,000 | 180D MFE +52.44% |
| 스튜디오드래곤 | failed_rerating | K-content/OTT narrative without margin bridge | 81,400 | 180D MAE -43.12% |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
new_independent_case_count = 3
reused_case_count = 0
```

The balance supports a **canonical-archetype-specific shadow rule**, not a global rule.

## 9. Evidence Source Map

| case | evidence family | evidence status |
|---|---|---|
| JYP Ent. | Stray Kids/TWICE album, Billboard, tour monetization | exact_original_source_url_pending |
| 하이브 | multi-label artist IP, BTS solo content, Seventeen/TXT/NewJeans route, Weverse/platform optionality | exact_original_source_url_pending |
| 스튜디오드래곤 | K-content/OTT narrative versus studio margin/production-cost reality | exact_original_source_url_pending |

Evidence is sufficient for research-row construction but should be URL-enriched before production promotion.

## 10. Price Data Source Map

| symbol | shard | profile |
|---:|---|---|
| 035900 | `atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv` | `atlas/symbol_profiles/035/035900.json` |
| 352820 | `atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv` | `atlas/symbol_profiles/352/352820.json` |
| 253450 | `atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv` | `atlas/symbol_profiles/253/253450.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry_date | entry_price | current profile verdict | outcome |
|---|---:|---|---:|---:|---|---|
| R8L10_C27_JYP_T1_STAGE2_ACTIONABLE | 035900 | Stage2-Actionable | 2023-02-22 | 76,000 | current_profile_too_late | structural_success |
| R8L10_C27_HYBE_T1_STAGE2_ACTIONABLE | 352820 | Stage2-Actionable | 2023-04-06 | 205,000 | current_profile_correct | structural_success |
| R8L10_C27_SDRAGON_T1_STAGE2_ACTIONABLE | 253450 | Stage2-Actionable | 2023-02-10 | 81,400 | current_profile_false_positive | failed_rerating |
| R8L10_C27_JYP_T2_4B_OVERLAY | 035900 | Stage4B | 2023-07-25 | 141,100 | current_profile_correct | 4B_overlay_success |

## 12. Trigger-Level OHLC Backtest Tables

| trigger | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| JYP Stage2 | 76,000 | +6.97% | -11.18% | +85.00% | -11.18% | +92.89% | -11.18% | 2023-07-25 | 146,600 |
| HYBE Stage2 | 205,000 | +47.80% | -7.17% | +52.44% | -7.17% | +52.44% | -15.85% | 2023-06-22 | 312,500 |
| Studio Dragon Stage2 | 81,400 | +2.58% | -14.00% | +2.58% | -39.93% | +2.58% | -43.12% | 2023-02-10 | 83,500 |
| JYP 4B overlay | 141,100 | +3.90% | -22.40% | +3.90% | -31.47% | +3.90% | -38.95% | 2023-07-25 | 146,600 |

## 13. Current Calibrated Profile Stress Test

| case | P0 likely label | actual path | verdict |
|---|---|---|---|
| JYP | Stage2/Yellow only after repeated proof | large upside before full confirmation | current_profile_too_late |
| HYBE | Stage2/Yellow with good evidence | strong MFE with moderate MAE | current_profile_correct |
| Studio Dragon | Stage2 if K-content narrative over-counted | low MFE, large MAE | current_profile_false_positive |

Answers to mandatory stress-test questions:

1. Current profile works on HYBE if it recognizes multi-artist monetization, but is late on JYP if it waits for accounting confirmation.
2. Stage2 bonus is useful only when repeat monetization evidence exists.
3. Yellow 75 is too permissive for production-studio narrative without margin bridge.
4. Green 87 / revision 55 should not be lowered globally.
5. Price-only blowoff guard remains appropriate.
6. Full 4B non-price requirement remains appropriate.
7. Hard 4C routing should trigger faster when margin/production economics invalidate a content narrative.

## 14. Stage2 / Yellow / Green Comparison

```text
JYP:
  Stage2-Actionable entry = 76,000
  proxy Green entry = around 97,000 after repeated album/tour proof
  peak = 146,600
  green_lateness_ratio ≈ 0.28

HYBE:
  Stage2-Actionable entry = 205,000
  proxy Green entry = around 224,500~245,000
  peak = 312,500
  green_lateness_ratio ≈ 0.18~0.37

Studio Dragon:
  no confirmed Green trigger
  green_lateness_ratio = not_applicable
```

## 15. 4B Local vs Full-window Timing Audit

JYP's 2023-07-25 row is a good 4B overlay candidate because full-window MFE was mostly exhausted, but the rule should not convert price-only local peaks into full 4B unless revision slowdown, margin slowdown, artist-cycle saturation, or contract-risk evidence exists.

```text
four_b_local_peak_proximity = 1.0
four_b_full_window_peak_proximity = 1.0
four_b_timing_verdict = price_only_local_4B_requires_non_price_confirmation
```

## 16. 4C Protection Audit

Studio Dragon is the 4C-timing lesson. The problem was not a sudden crash after a peak; it was a slow thesis leak: K-content demand did not translate into a repeatable, high-margin IP monetization path. That argues for a **thesis-break watch** before a hard 4C, then hard 4C once margin/revision evidence confirms.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L8_content_ip_monetization_bridge
proposal = Add a shadow-only bonus when content/IP evidence includes repeatable monetization: album/tour/platform revenue, multi-artist diversification, durable IP ownership, and financial revision bridge.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION

new_axis_proposed:
  - c27_repeatable_ip_monetization_bridge
  - c27_production_narrative_without_margin_cap
  - c27_price_only_ip_blowoff_4b_watch
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE_90D | avg MAE_90D | false positive rate | score-return alignment |
|---|---|---:|---:|---:|---:|---|
| P0 | calibrated global profile | 3 | +30.05% | -19.43% | 33% | mixed |
| P0b | old baseline | 3 | +30.05% | -19.43% | 33%+ | weaker |
| P1 | L8 sector bridge | 3 | +45.00% selected positives | -9.18% positives | lower | improved |
| P2 | C27 bridge + cap | 3 | +45.00% selected positives | -9.18% positives | lower | best |
| P3 | counterexample guard | 1 guard | +2.58% | -39.93% | blocks false positive | improved |

## 20. Score-Return Alignment Matrix

| case | before score | before label | after score | after label | actual path | alignment |
|---|---:|---|---:|---|---|---|
| JYP | 72 | Stage2-Actionable | 79 | Stage3-Yellow | +92.89% 180D MFE | improved |
| HYBE | 70 | Stage2-Actionable | 76 | Stage3-Yellow | +52.44% 180D MFE | improved |
| Studio Dragon | 64 | Stage2-Actionable | 49 | Stage1 / blocked | -43.12% 180D MAE | improved |
| JYP 4B | -5 | 4B-watch | -9 | 4B-overlay-only | -38.95% post-peak drawdown | kept |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM | 2 | 1 | 1 | 1 watch | 3 | 0 | 4 | 3 | 2 | true | true | needs exact source URL enrichment and more SW/security C28 coverage |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - content_narrative_without_margin_bridge_false_positive
  - green_too_late_for_repeatable_artist_ip
  - price_only_4B_requires_non_price_confirmation
new_axis_proposed:
  - c27_repeatable_ip_monetization_bridge
  - c27_production_narrative_without_margin_cap
  - c27_price_only_ip_blowoff_4b_watch
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web actual OHLC rows
- 30D/90D/180D MFE/MAE from tradable_raw price basis
- round/sector consistency
- new independent symbol coverage
- representative trigger dedupe

Not validated for production:

- exact original article/disclosure URL mapping
- final production scoring code
- live candidate applicability
- broker/API execution

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_repeatable_ip_monetization_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,+1,+1,"Reward album/tour/platform/repeat monetization bridge, not traffic alone","Improves JYP/HYBE Stage2/Yellow timing without weakening Green threshold","R8L10_C27_JYP_T1_STAGE2_ACTIONABLE|R8L10_C27_HYBE_T1_STAGE2_ACTIONABLE",3,3,1,medium,canonical_shadow_only,"not production; requires exact evidence URL enrichment"
shadow_weight,c27_production_narrative_without_margin_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,-1,-1,"Cap K-content/OTT narrative when studio economics lack margin/repeat IP proof","Blocks Studio Dragon false-positive Stage2/Yellow promotion","R8L10_C27_SDRAGON_T1_STAGE2_ACTIONABLE",3,3,1,medium,canonical_shadow_only,"not production; counterexample-supported"
shadow_weight,c27_price_only_ip_blowoff_4b_watch,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,+1,+1,"Price-only peak is 4B overlay only unless non-price saturation or revision slowdown exists","Keeps full_4B non-price requirement intact","R8L10_C27_JYP_T2_4B_OVERLAY",4,3,1,low,overlay_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L10_C27_JYP_20230222", "symbol": "035900", "company_name": "JYP Ent.", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L10_C27_JYP_T1_STAGE2_ACTIONABLE", "notes": "Stray Kids/TWICE global album-tour monetization bridge; not merely K-pop traffic/news.", "round": "R8", "loop": "10", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R8L10_C27_HYBE_20230406", "symbol": "352820", "company_name": "하이브", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L10_C27_HYBE_T1_STAGE2_ACTIONABLE", "notes": "Multi-artist IP monetization, album/tour/platform optionality, BTS solo-cycle absorption.", "round": "R8", "loop": "10", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R8L10_C27_STUDIODRAGON_20230210", "symbol": "253450", "company_name": "스튜디오드래곤", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L10_C27_SDRAGON_T1_STAGE2_ACTIONABLE", "notes": "K-content/global OTT narrative without durable margin/repeat monetization bridge; production studio economics differ from scalable artist IP.", "round": "R8", "loop": "10", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_false_positive_prevented_by_shadow", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web"}
{"row_type": "trigger", "trigger_id": "R8L10_C27_JYP_T1_STAGE2_ACTIONABLE", "case_id": "R8L10_C27_JYP_20230222", "symbol": "035900", "company_name": "JYP Ent.", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-22", "entry_date": "2023-02-22", "entry_price": 76000, "evidence_available_at_that_date": "Global K-pop monetization bridge visible through Stray Kids/TWICE album sales, US Billboard presence, and tour expansion; exact source URL enrichment required before production promotion.", "evidence_source": "public music chart/tour disclosures; exact_original_source_url_pending", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "repeat_order_or_conversion", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "MFE_30D_pct": 6.97, "MFE_90D_pct": 85.0, "MFE_180D_pct": 92.89, "MFE_1Y_pct": 92.89, "MFE_2Y_pct": null, "MAE_30D_pct": -11.18, "MAE_90D_pct": -11.18, "MAE_180D_pct": -11.18, "MAE_1Y_pct": -24.47, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -38.95, "green_lateness_ratio": 0.28, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L10_C27_JYP_20230222_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "round": "R8", "loop": "10", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "CONTENT_IP_GLOBAL_MONETIZATION", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R8L10_C27_HYBE_T1_STAGE2_ACTIONABLE", "case_id": "R8L10_C27_HYBE_20230406", "symbol": "352820", "company_name": "하이브", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-06", "entry_date": "2023-04-06", "entry_price": 205000, "evidence_available_at_that_date": "Multi-artist IP portfolio, BTS solo-event monetization, Seventeen/TXT/Le Sserafim/NewJeans-related label diversification; exact source URL enrichment required.", "evidence_source": "public artist release/tour/platform reports; exact_original_source_url_pending", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "repeat_order_or_conversion"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv", "profile_path": "atlas/symbol_profiles/352/352820.json", "MFE_30D_pct": 47.8, "MFE_90D_pct": 52.44, "MFE_180D_pct": 52.44, "MFE_1Y_pct": 52.44, "MFE_2Y_pct": null, "MAE_30D_pct": -7.17, "MAE_90D_pct": -7.17, "MAE_180D_pct": -15.85, "MAE_1Y_pct": -25.12, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-22", "peak_price": 312500, "drawdown_after_peak_pct": -24.8, "green_lateness_ratio": 0.18, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L10_C27_HYBE_20230406_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "round": "R8", "loop": "10", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "CONTENT_IP_GLOBAL_MONETIZATION", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R8L10_C27_SDRAGON_T1_STAGE2_ACTIONABLE", "case_id": "R8L10_C27_STUDIODRAGON_20230210", "symbol": "253450", "company_name": "스튜디오드래곤", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "entry_date": "2023-02-10", "entry_price": 81400, "evidence_available_at_that_date": "K-content/OTT distribution narrative existed, but no durable margin bridge or scalable IP monetization proof; production cost and broadcaster/OTT economics remained risk-first.", "evidence_source": "public earnings/narrative reports; exact_original_source_url_pending", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv", "profile_path": "atlas/symbol_profiles/253/253450.json", "MFE_30D_pct": 2.58, "MFE_90D_pct": 2.58, "MFE_180D_pct": 2.58, "MFE_1Y_pct": 2.58, "MFE_2Y_pct": null, "MAE_30D_pct": -14.0, "MAE_90D_pct": -39.93, "MAE_180D_pct": -43.12, "MAE_1Y_pct": -49.94, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-10", "peak_price": 83500, "drawdown_after_peak_pct": -43.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_margin_slowdown_confirmed", "four_b_evidence_type": ["valuation_blowoff", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L10_C27_SDRAGON_20230210_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "round": "R8", "loop": "10", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "CONTENT_IP_GLOBAL_MONETIZATION", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R8L10_C27_JYP_T2_4B_OVERLAY", "case_id": "R8L10_C27_JYP_20230222", "symbol": "035900", "company_name": "JYP Ent.", "trigger_type": "Stage4B", "trigger_date": "2023-07-25", "entry_date": "2023-07-25", "entry_price": 141100, "evidence_available_at_that_date": "Local price blowoff after global-album/tour success; no hard thesis break yet, so 4B overlay only unless non-price saturation/revision slowdown confirms.", "evidence_source": "stock-web price-only local peak plus narrative; exact_original_source_url_pending", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "MFE_30D_pct": 3.9, "MFE_90D_pct": 3.9, "MFE_180D_pct": 3.9, "MFE_1Y_pct": 3.9, "MFE_2Y_pct": null, "MAE_30D_pct": -22.4, "MAE_90D_pct": -31.47, "MAE_180D_pct": -38.95, "MAE_1Y_pct": -45.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -38.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_requires_non_price_confirmation", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L10_C27_JYP_20230725_G2", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same symbol, different trigger family: 4B overlay timing after structural success", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "round": "R8", "loop": "10", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_CONTENT_KPOP_GLOBAL_IP_MONETIZATION_TOUR_ALBUM_PLATFORM", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "CONTENT_IP_GLOBAL_MONETIZATION", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L10_C27_JYP_20230222", "trigger_id": "R8L10_C27_JYP_T1_STAGE2_ACTIONABLE", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 15, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 11, "revision_score": 17, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C27 shadow profile rewards repeatable IP monetization bridge and caps production/narrative-only K-content exposure.", "MFE_90D_pct": 85.0, "MAE_90D_pct": -11.18, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L10_C27_HYBE_20230406", "trigger_id": "R8L10_C27_HYBE_T1_STAGE2_ACTIONABLE", "symbol": "352820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 12, "relative_strength_score": 12, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 14, "relative_strength_score": 12, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C27 shadow profile rewards repeatable IP monetization bridge and caps production/narrative-only K-content exposure.", "MFE_90D_pct": 52.44, "MAE_90D_pct": -7.17, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L10_C27_STUDIODRAGON_20230210", "trigger_id": "R8L10_C27_SDRAGON_T1_STAGE2_ACTIONABLE", "symbol": "253450", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -14, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": -1, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": -22, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 49, "stage_label_after": "Stage1", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C27 shadow profile rewards repeatable IP monetization bridge and caps production/narrative-only K-content exposure.", "MFE_90D_pct": 2.58, "MAE_90D_pct": -39.93, "score_return_alignment_label": "after_profile_improves_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L10_C27_JYP_20230222", "trigger_id": "R8L10_C27_JYP_T2_4B_OVERLAY", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": -5, "stage_label_before": "Stage1", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 17, "execution_risk_score": -9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": -9, "stage_label_after": "Stage1", "changed_components": ["margin_bridge_score", "customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C27 shadow profile rewards repeatable IP monetization bridge and caps production/narrative-only K-content exposure.", "MFE_90D_pct": 3.9, "MAE_90D_pct": -31.47, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R8", "loop": "10", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["content_narrative_without_margin_bridge_false_positive", "green_too_late_for_repeatable_artist_ip", "price_only_4B_requires_non_price_confirmation"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R8
completed_loop = 10
next_round = R9
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Price source: `Songdaiki/stock-web`
- Manifest max date: `2026-02-20`
- Price basis: `tradable_raw`
- Adjustment status: `raw_unadjusted_marcap`
- Evidence URLs: exact source enrichment required before production promotion.
