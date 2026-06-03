# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R8
scheduled_loop: 11
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: CONTENT_IP_GLOBAL_MONETIZATION_ALBUM_TOUR_PLATFORM_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R8_loop_11_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 3 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption

The baseline profile for stress testing is `e2r_2_1_stock_web_calibrated_proxy`. The previous profile `e2r_2_0_baseline_reference` is only a rollback/reference comparison. This file does not re-propose the global Stock-Web calibrated axes. It asks a narrower C27 question: when does platform/content/IP evidence become a durable monetization bridge, and when is the price path merely governance premium, one-off buzz, or content-cost leverage in reverse?

Current global axes tested:

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

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R8`
- Loop: `11`
- Large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- Canonical archetype: `C27_CONTENT_IP_GLOBAL_MONETIZATION`
- Fine archetype: `CONTENT_IP_GLOBAL_MONETIZATION_ALBUM_TOUR_PLATFORM_MARGIN_BRIDGE`
- Loop objectives: `coverage_gap_fill`, `counterexample_mining`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `4B_non_price_requirement_stress_test`, `4C_thesis_break_timing_test`

C27 is not simply “K-pop good,” “drama globally popular,” or “platform story.” It needs conversion. The trigger must show that IP attention becomes money: albums, tours, licenses, paid platform distribution, repeatable fanbase demand, or margin/revision visibility. Without that bridge, the story is just a loud poster outside the theater.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact checked: `reports/e2r_calibration/by_round/R8.md`. R8 already has broad representative trigger coverage, so this loop avoids C28 software/security contract-retention repetition and targets C27 content/IP monetization residuals.

```text
scheduled_round = R8
scheduled_loop = 11
wrong_round_penalty = 0
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
positive_case_count = 2
counterexample_count = 3
current_profile_error_count = 3
```

Previous local file avoided: `e2r_stock_web_v12_residual_round_R8_loop_10_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md`. This R8 loop is C27, not C28.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

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

Schema confirmation:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative triggers are historical, use stock-web tradable shards, have at least 180 forward trading days available by the manifest max date, and do not overlap corporate-action candidate dates in the 180D window.

| symbol | company | profile path | entry date | 180D usable | corporate-action window status |
|---:|---|---|---|---|---|
| 035900 | JYP Ent. | `atlas/symbol_profiles/035/035900.json` | 2023-05-15 | true | clean_180D_window |
| 352820 | 하이브 | `atlas/symbol_profiles/352/352820.json` | 2023-04-03 | true | clean_180D_window |
| 041510 | 에스엠 | `atlas/symbol_profiles/041/041510.json` | 2023-02-10 | true | clean_180D_window |
| 253450 | 스튜디오드래곤 | `atlas/symbol_profiles/253/253450.json` | 2021-09-27 | true | clean_180D_window |
| 035760 | CJ ENM | `atlas/symbol_profiles/035/035760.json` | 2021-09-23 | true | clean_180D_window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rule |
|---|---|---|
| KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION | C27_CONTENT_IP_GLOBAL_MONETIZATION | Keep when album preorder/sales, tour, fanbase, or platform demand converts into revenue visibility. |
| KPOP_MULTI_ARTIST_PLATFORM_IP_MONETIZATION | C27_CONTENT_IP_GLOBAL_MONETIZATION | Keep when multi-artist IP plus platform distribution has measurable conversion and low one-artist concentration risk. |
| KPOP_CONTROL_PREMIUM_NOT_CONTENT_IP | C27_CONTENT_IP_GLOBAL_MONETIZATION | Cap or exclude from C27 Green; route to C32/control-premium or 4B overlay. |
| KDRAMA_GLOBAL_BUZZ_WITHOUT_MARGIN_BRIDGE | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage2/watch only until global attention becomes margin, owned-IP, or licensing evidence. |
| CONTENT_PLATFORM_SCALE_WITH_COST_DRAG | C27_CONTENT_IP_GLOBAL_MONETIZATION | Penalize if platform/content investment expands revenue but compresses operating leverage. |

## 7. Case Selection Summary

| case_id | symbol | company | polarity | role | fine_archetype |
|---|---:|---|---|---|---|
| R8L11_C27_CASE_001_JYP_2023_GLOBAL_ALBUM_TOUR_CONVERSION | 035900 | JYP Ent. | positive | structural_success | KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION |
| R8L11_C27_CASE_002_HYBE_2023_WEVERSE_MULTI_ARTIST_IP_SCALE | 352820 | 하이브 | positive | structural_success | KPOP_MULTI_ARTIST_PLATFORM_IP_MONETIZATION |
| R8L11_C27_CASE_003_SM_2023_CONTROL_PREMIUM_FALSE_C27 | 041510 | 에스엠 | counterexample | false_positive_green | KPOP_CONTROL_PREMIUM_NOT_CONTENT_IP |
| R8L11_C27_CASE_004_STUDIO_DRAGON_2021_GLOBAL_KDRAMA_BUZZ_NO_OPERATING_LEVERAGE | 253450 | 스튜디오드래곤 | counterexample | failed_rerating | KDRAMA_GLOBAL_BUZZ_WITHOUT_MARGIN_BRIDGE |
| R8L11_C27_CASE_005_CJENM_2021_CONTENT_PLATFORM_INVESTMENT_MARGIN_DRAG | 035760 | CJ ENM | counterexample | failed_rerating | CONTENT_PLATFORM_SCALE_WITH_COST_DRAG |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 3
4B_or_4C_case = 3
calibration_usable_case_count = 5
calibration_usable_trigger_count = 7
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The positive side is JYP and HYBE: global fanbase/IP demand had observable conversion. The counterexample side is SM, Studio Dragon, and CJ ENM: price strength or content buzz did not by itself create a durable C27 Green.

## 9. Evidence Source Map

Evidence is historical proxy evidence for calibration research, not production ingestion. Quantitative returns use only stock-web OHLC.

- JYP: Stray Kids album preorder/sales signal and TWICE global tour route; conversion evidence exists, but the Green trigger loses part of the upside after the gap.
- HYBE: multi-artist release cycle and platform/IP monetization route; strongest Stage2-actionable alignment in this loop.
- SM: HYBE/Kakao tender-control premium; use as event/control-premium counterexample, not content-IP Green.
- Studio Dragon: K-drama global buzz; attention did not become owned-IP/margin proof at the trigger.
- CJ ENM: global studio/platform investment narrative; cost drag and operating leverage risk dominated after the peak.

## 10. Price Data Source Map

| symbol | tradable shard | profile |
|---:|---|---|
| 035900 | `atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv` | `atlas/symbol_profiles/035/035900.json` |
| 352820 | `atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv` | `atlas/symbol_profiles/352/352820.json` |
| 041510 | `atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv` | `atlas/symbol_profiles/041/041510.json` |
| 253450 | `atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv` and `2022.csv` | `atlas/symbol_profiles/253/253450.json` |
| 035760 | `atlas/ohlcv_tradable_by_symbol_year/035/035760/2021.csv` and `2022.csv` | `atlas/symbol_profiles/035/035760.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current verdict | dedupe |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|---|
| `R8L11_C27_TRG_001A_JYP_STAGE2_ACTIONABLE_2023_05_15` | 035900 | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 95,500 | 53.51 | -3.46 | 53.51 | -6.28 | current_profile_correct | true |
| `R8L11_C27_TRG_001B_JYP_STAGE3_GREEN_2023_05_16` | 035900 | Stage3-Green | 2023-05-16 | 2023-05-16 | 115,400 | 27.04 | -12.39 | 27.04 | -22.44 | current_profile_correct | false |
| `R8L11_C27_TRG_001C_JYP_4B_OVERLAY_2023_07_25` | 035900 | Stage4B | 2023-07-25 | 2023-07-25 | 141,100 | 3.9 | -29.27 | 3.9 | -36.57 | current_profile_correct | false |
| `R8L11_C27_TRG_002A_HYBE_STAGE2_ACTIONABLE_2023_04_03` | 352820 | Stage2-Actionable | 2023-04-03 | 2023-04-03 | 184,000 | 69.84 | -0.16 | 69.84 | -0.16 | current_profile_correct | true |
| `R8L11_C27_TRG_003A_SM_STAGE2_EVENT_2023_02_10` | 041510 | Stage2-Event | 2023-02-10 | 2023-02-10 | 114,700 | 40.54 | -23.63 | 40.54 | -23.63 | current_profile_false_positive | true |
| `R8L11_C27_TRG_003B_SM_4B_CONTROL_PREMIUM_2023_03_08` | 041510 | Stage4B | 2023-03-08 | 2023-03-08 | 158,500 | 1.7 | -44.73 | 1.7 | -44.73 | current_profile_correct | false |
| `R8L11_C27_TRG_004A_STUDIO_DRAGON_STAGE2_WATCH_2021_09_27` | 253450 | Stage2-Watch | 2021-09-27 | 2021-09-27 | 89,500 | 10.5 | -6.59 | 10.5 | -19.22 | current_profile_false_positive | true |
| `R8L11_C27_TRG_005A_CJENM_STAGE2_WATCH_2021_09_23` | 035760 | Stage2-Watch | 2021-09-23 | 2021-09-23 | 155,900 | 22.9 | -24.31 | 22.9 | -39.26 | current_profile_4B_too_late | true |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger averages, deduped by same-entry group:

```text
representative_trigger_count = 5
avg_MFE_30D_pct = 36.65
avg_MFE_90D_pct = 39.46
avg_MFE_180D_pct = 39.46
avg_MAE_30D_pct = -6.87
avg_MAE_90D_pct = -11.63
avg_MAE_180D_pct = -17.71
```

The average MFE looks decent because C27 contains explosive narratives. But this is exactly where the residual hides: the price path of a control-premium fight or content-buzz episode can resemble true IP monetization until the conversion bridge is asked to show its invoice.

## 13. Current Calibrated Profile Stress Test

| case | current profile verdict | stress result |
|---|---|---|
| JYP Ent. | current_profile_correct | Stage2-actionable captured most of the move; Green after the gap remained valid but later. |
| 하이브 | current_profile_correct | Stage2-actionable was aligned; very low MAE suggests evidence arrived before the rerating leg. |
| 에스엠 | current_profile_false_positive | Current profile can over-score content labels if governance/tender premium is not excluded. |
| 스튜디오드래곤 | current_profile_false_positive | Global content buzz without owned-IP/margin bridge should not become C27 Green. |
| CJ ENM | current_profile_4B_too_late | Content/platform scale narrative needed earlier cost-drag 4B overlay. |

Required questions:

1. Current calibrated profile is directionally right on price-only blowoff, but C27 needs a stricter non-price definition of content conversion.
2. Judgments match MFE/MAE only when IP conversion is measurable. They fail for SM, Studio Dragon, and CJ ENM if buzz/control premium is scored as content monetization.
3. Stage2 bonus is useful but too generous when the evidence is only popularity or event premium.
4. Yellow threshold 75 is adequate only after a revenue-conversion bridge exists.
5. Green threshold 87/revision 55 should remain, but C27 should allow earlier Green only when direct conversion evidence is unusually strong.
6. Price-only blowoff guard is appropriate and kept.
7. Full 4B non-price requirement is strengthened: C27 non-price 4B can be tender-cap, content-cost drag, or valuation/positioning overheat.
8. Hard 4C routing is kept; CJ ENM suggests earlier 4B-watch before hard 4C, not a global 4C change.

## 14. Stage2 / Yellow / Green Comparison

C27 Stage2 can start when fandom, content, or platform distribution becomes visible. C27 Yellow requires a conversion clue. C27 Green requires conversion plus margin/revision support.

```text
C27 Stage2 = IP/fandom/content/platform narrative + relative strength + plausible conversion route
C27 Yellow = Stage2 + measurable preorders/tour/platform/licensing/distribution evidence
C27 Green = Yellow + financial visibility or revision/margin bridge + low event/control-premium risk
```

JYP Green lateness audit:

```text
Stage2_Actionable_entry_price = 95,500
Stage3_Green_entry_price = 115,400
peak_price_after_Stage2 = 146,600
green_lateness_ratio = (115,400 - 95,500) / (146,600 - 95,500) = 0.39
verdict = Green 다소 늦음, but not fatal because Stage2-actionable captured the early leg.
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| JYP 2023-07-25 | valuation_blowoff / positioning_overheat | 1.00 | 1.00 | good_full_window_4B_timing |
| SM 2023-03-08 | control_premium_or_event_premium / tender cap | 0.94 | 0.94 | good_full_window_4B_timing |
| CJ ENM 2021-09-23 | content-cost drag watch | n/a | n/a | 4B_too_late_if_cost_drag_ignored |

4B here is not “sell because the chart is high.” It is the moment the non-price evidence says the stage has changed: valuation stretched, tender cap visible, or content/platform costs are eating the operating leverage that the story promised.

## 16. 4C Protection Audit

| case | 4C label | comment |
|---|---|---|
| SM | hard_4c_success | Tender/control-premium resolved into event unwind; hard 4C protected against confusing governance premium with C27. |
| CJ ENM | hard_4c_late | The break was not one dramatic cancellation; it was cost-drag evidence accumulating after the initial content-platform enthusiasm. |
| Studio Dragon | thesis_break_watch_only | Buzz did not become a durable conversion bridge, but hard 4C would be too harsh without explicit thesis-break evidence. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L8_event_or_buzz_exclusion_guard
proposal = If price strength is driven primarily by governance/control premium, viral content buzz, or event cap rather than monetization bridge, do not allow Stage3-Green in L8. Route to Stage2-watch or 4B overlay.
confidence = medium
production_scoring_changed = false
shadow_weight_only = true
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C27_content_ip_conversion_bridge
proposal = C27 Green requires measurable IP conversion evidence: album/tour/platform/license/distribution conversion plus margin/revision visibility. Popularity without conversion remains Stage2/Yellow at most.
confidence = medium
production_scoring_changed = false
shadow_weight_only = true
```

C27 shadow components:

```text
global_ip_conversion_score: +1 candidate when conversion is measurable
content_cost_burden_guard: +1 risk guard when platform/content investment expands costs faster than monetization
control_premium_exclusion_guard: +1 sector guard to prevent SM-like governance events from becoming C27 Green
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | score_return_alignment |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current_proxy | 5 | 39.46 | -11.63 | 39.46 | -17.71 | 0.6 | mixed_false_positive_in_content_buzz_and_control_premium |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 5 | 39.46 | -11.63 | 39.46 | -17.71 | 0.8 | weak |
| P1_L8_sector_specific_candidate_profile | sector_specific | 5 | 39.46 | -11.63 | 39.46 | -17.71 | 0.2 | improved |
| P2_C27_canonical_archetype_candidate_profile | canonical_archetype_specific | 5 | 39.46 | -11.63 | 39.46 | -17.71 | 0.0 | best |
| P3_counterexample_guard_profile | guard_profile | 5 | 39.46 | -11.63 | 39.46 | -17.71 | 0.0 | good_but_conservative |

## 20. Score-Return Alignment Matrix

| case | before label | after label | MFE180 | MAE180 | alignment verdict |
|---|---|---|---:|---:|---|
| JYP | Stage3-Yellow / Green comparison | Stage3-Yellow-high / Green valid | 53.51 | -6.28 | aligned_positive |
| HYBE | Stage3-Yellow | Stage3-Yellow-high | 69.84 | -0.16 | aligned_positive |
| SM | Stage3-Yellow | Stage2-event/4B-watch | 40.54 | -23.63 | after_profile_improves_false_positive |
| Studio Dragon | Stage2-Actionable | Stage2-Watch | 10.50 | -19.22 | after_profile_improves_buzz_false_positive |
| CJ ENM | Stage3-Yellow | Stage2-Watch/4B-risk | 22.90 | -39.26 | after_profile_improves_4B_lateness |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | CONTENT_IP_GLOBAL_MONETIZATION_ALBUM_TOUR_PLATFORM_MARGIN_BRIDGE | 2 | 3 | 3 | 2 | 5 | 0 | 7 | 5 | 3 | true | true | C27 now has positive/counterexample/4B balance; still needs more non-K-pop platform cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: content_buzz_false_green, control_premium_false_c27, content_cost_drag_4B_late
new_axis_proposed: null
existing_axis_strengthened: full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: stage3_green_revision_min only as C27-specific patience exception when conversion evidence is direct
existing_axis_kept: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Scheduled round R8 / loop 11.
- L8 large-sector consistency.
- C27 canonical archetype mapping.
- Actual stock-web tradable OHLC paths for entry/peak/drawdown estimates.
- Positive/counterexample balance.
- Same-entry dedupe for aggregate representatives.
- 4B local vs full-window split for JYP/SM overlays.
```

Not validated:

```text
- No stock_agent source code opened.
- No production scoring changed.
- No live 2026 candidate scan.
- No brokerage/auto-trading logic.
- No current investment recommendation.
- Evidence-source parsing is narrative/proxy only; quantitative calibration is stock-web only.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,global_ip_conversion_score,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"measurable album/tour/platform/license conversion separates JYP/HYBE from buzz-only cases","false_positive_rate 0.60 -> 0.00 in P2",R8L11_C27_TRG_001A_JYP_STAGE2_ACTIONABLE_2023_05_15|R8L11_C27_TRG_002A_HYBE_STAGE2_ACTIONABLE_2023_04_03,5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,content_cost_burden_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"global content buzz without margin bridge caused Studio Dragon/CJ ENM residuals","reduces false Green from content-cost drag",R8L11_C27_TRG_004A_STUDIO_DRAGON_STAGE2_WATCH_2021_09_27|R8L11_C27_TRG_005A_CJENM_STAGE2_WATCH_2021_09_23,5,5,3,medium,canonical_shadow_only,"4B/4C overlay only"
shadow_weight,control_premium_exclusion_guard,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"SM 2023 price path was governance/tender cap, not content IP monetization","routes event premium to 4B/C32 rather than C27 Green",R8L11_C27_TRG_003A_SM_STAGE2_EVENT_2023_02_10|R8L11_C27_TRG_003B_SM_4B_CONTROL_PREMIUM_2023_03_08,5,5,3,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L11_C27_CASE_001_JYP_2023_GLOBAL_ALBUM_TOUR_CONVERSION", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L11_C27_TRG_001A_JYP_STAGE2_ACTIONABLE_2023_05_15", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Stray Kids global album demand and TWICE tour bridge converted fandom/IP into measurable revenue route; later 4B overlay needed after vertical rerating."}
{"row_type": "case", "case_id": "R8L11_C27_CASE_002_HYBE_2023_WEVERSE_MULTI_ARTIST_IP_SCALE", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_MULTI_ARTIST_PLATFORM_IP_MONETIZATION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L11_C27_TRG_002A_HYBE_STAGE2_ACTIONABLE_2023_04_03", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Multi-artist release cycle plus platform/IP monetization formed a cleaner C27 path; very low MAE because entry preceded the rerating leg."}
{"row_type": "case", "case_id": "R8L11_C27_CASE_003_SM_2023_CONTROL_PREMIUM_FALSE_C27", "symbol": "041510", "company_name": "에스엠", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_CONTROL_PREMIUM_NOT_CONTENT_IP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R8L11_C27_TRG_003A_SM_STAGE2_EVENT_2023_02_10", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "HYBE/Kakao control-premium battle produced C27-looking price strength but the dominant driver was governance/tender cap, not content-IP monetization."}
{"row_type": "case", "case_id": "R8L11_C27_CASE_004_STUDIO_DRAGON_2021_GLOBAL_KDRAMA_BUZZ_NO_OPERATING_LEVERAGE", "symbol": "253450", "company_name": "스튜디오드래곤", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KDRAMA_GLOBAL_BUZZ_WITHOUT_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L11_C27_TRG_004A_STUDIO_DRAGON_STAGE2_WATCH_2021_09_27", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Global K-drama attention moved the stock, but without incremental IP ownership/margin proof the move failed to become a durable C27 Green."}
{"row_type": "case", "case_id": "R8L11_C27_CASE_005_CJENM_2021_CONTENT_PLATFORM_INVESTMENT_MARGIN_DRAG", "symbol": "035760", "company_name": "CJ ENM", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_PLATFORM_SCALE_WITH_COST_DRAG", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L11_C27_TRG_005A_CJENM_STAGE2_WATCH_2021_09_23", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_needed", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Content/platform investment and global studio ambition created a short rerating, but cost/margin burden and lack of clean operating leverage reversed it."}
{"row_type": "trigger", "trigger_id": "R8L11_C27_TRG_001A_JYP_STAGE2_ACTIONABLE_2023_05_15", "case_id": "R8L11_C27_CASE_001_JYP_2023_GLOBAL_ALBUM_TOUR_CONVERSION", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-15", "evidence_available_at_that_date": "global album/tour demand visible before earnings-price gap; fanbase monetization route existed but Green needed conversion proof", "evidence_source": "historical public event / stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": ["repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-15", "entry_price": 95500, "MFE_30D_pct": 47.23, "MFE_90D_pct": 53.51, "MFE_180D_pct": 53.51, "MFE_1Y_pct": 53.51, "MFE_2Y_pct": 53.51, "MAE_30D_pct": -3.46, "MAE_90D_pct": -3.46, "MAE_180D_pct": -6.28, "MAE_1Y_pct": -42.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -38.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C27_CASE_001_GRP_STAGE2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L11_C27_TRG_001B_JYP_STAGE3_GREEN_2023_05_16", "case_id": "R8L11_C27_CASE_001_JYP_2023_GLOBAL_ALBUM_TOUR_CONVERSION", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage3-Green", "trigger_date": "2023-05-16", "evidence_available_at_that_date": "gap-up after stronger conversion evidence; Green less early than Stage2 and loses part of available upside", "evidence_source": "historical public event / stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-16", "entry_price": 115400, "MFE_30D_pct": 21.84, "MFE_90D_pct": 27.04, "MFE_180D_pct": 27.04, "MFE_1Y_pct": 27.04, "MFE_2Y_pct": 27.04, "MAE_30D_pct": -9.01, "MAE_90D_pct": -12.39, "MAE_180D_pct": -22.44, "MAE_1Y_pct": -52.35, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -38.95, "green_lateness_ratio": 0.39, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_but_valid_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C27_CASE_001_GRP_GREEN", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R8L11_C27_TRG_001C_JYP_4B_OVERLAY_2023_07_25", "case_id": "R8L11_C27_CASE_001_JYP_2023_GLOBAL_ALBUM_TOUR_CONVERSION", "symbol": "035900", "company_name": "JYP Ent.", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_GLOBAL_ALBUM_TOUR_IP_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-07-25", "evidence_available_at_that_date": "valuation/positioning overheat after visible album/tour demand; non-price 4B overlay rather than thesis break", "evidence_source": "historical public event / stock-web OHLC validation", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv", "profile_path": "atlas/symbol_profiles/035/035900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-25", "entry_price": 141100, "MFE_30D_pct": 3.9, "MFE_90D_pct": 3.9, "MFE_180D_pct": 3.9, "MFE_1Y_pct": 3.9, "MFE_2Y_pct": 3.9, "MAE_30D_pct": -13.04, "MAE_90D_pct": -29.27, "MAE_180D_pct": -36.57, "MAE_1Y_pct": -60.74, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-25", "peak_price": 146600, "drawdown_after_peak_pct": -38.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C27_CASE_001_GRP_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R8L11_C27_TRG_002A_HYBE_STAGE2_ACTIONABLE_2023_04_03", "case_id": "R8L11_C27_CASE_002_HYBE_2023_WEVERSE_MULTI_ARTIST_IP_SCALE", "symbol": "352820", "company_name": "하이브", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_MULTI_ARTIST_PLATFORM_IP_MONETIZATION", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-03", "evidence_available_at_that_date": "multi-artist release cycle, platform monetization, and global fandom demand before full revision confirmation", "evidence_source": "historical public event / stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv", "profile_path": "atlas/symbol_profiles/352/352820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-03", "entry_price": 184000, "MFE_30D_pct": 64.67, "MFE_90D_pct": 69.84, "MFE_180D_pct": 69.84, "MFE_1Y_pct": 69.84, "MFE_2Y_pct": 116.58, "MAE_30D_pct": -0.16, "MAE_90D_pct": -0.16, "MAE_180D_pct": -0.16, "MAE_1Y_pct": -1.36, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-22", "peak_price": 312500, "drawdown_after_peak_pct": -35.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C27_CASE_002_GRP_STAGE2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L11_C27_TRG_003A_SM_STAGE2_EVENT_2023_02_10", "case_id": "R8L11_C27_CASE_003_SM_2023_CONTROL_PREMIUM_FALSE_C27", "symbol": "041510", "company_name": "에스엠", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_CONTROL_PREMIUM_NOT_CONTENT_IP", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Event", "trigger_date": "2023-02-10", "evidence_available_at_that_date": "HYBE stake/tender route changed price regime; should be C32/control-premium overlay, not C27 Green", "evidence_source": "historical public event / stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-10", "entry_price": 114700, "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": 40.54, "MFE_2Y_pct": 40.54, "MAE_30D_pct": -21.1, "MAE_90D_pct": -23.63, "MAE_180D_pct": -23.63, "MAE_1Y_pct": -38.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "event_premium_requires_4B_overlay_not_c27_green", "four_b_evidence_type": ["control_premium_or_event_premium"], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C27_CASE_003_GRP_EVENT", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L11_C27_TRG_003B_SM_4B_CONTROL_PREMIUM_2023_03_08", "case_id": "R8L11_C27_CASE_003_SM_2023_CONTROL_PREMIUM_FALSE_C27", "symbol": "041510", "company_name": "에스엠", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KPOP_CONTROL_PREMIUM_NOT_CONTENT_IP", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-03-08", "evidence_available_at_that_date": "Kakao 150,000 won tender cap/control-premium ceiling; non-price 4B evidence existed near peak", "evidence_source": "historical public event / stock-web OHLC validation", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "explicit_event_cap", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-08", "entry_price": 158500, "MFE_30D_pct": 1.7, "MFE_90D_pct": 1.7, "MFE_180D_pct": 1.7, "MFE_1Y_pct": 1.7, "MFE_2Y_pct": 1.7, "MAE_30D_pct": -44.73, "MAE_90D_pct": -44.73, "MAE_180D_pct": -44.73, "MAE_1Y_pct": -54.7, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C27_CASE_003_GRP_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R8L11_C27_TRG_004A_STUDIO_DRAGON_STAGE2_WATCH_2021_09_27", "case_id": "R8L11_C27_CASE_004_STUDIO_DRAGON_2021_GLOBAL_KDRAMA_BUZZ_NO_OPERATING_LEVERAGE", "symbol": "253450", "company_name": "스튜디오드래곤", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "KDRAMA_GLOBAL_BUZZ_WITHOUT_MARGIN_BRIDGE", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Watch", "trigger_date": "2021-09-27", "evidence_available_at_that_date": "global K-drama buzz created attention, but no decisive incremental IP ownership/margin bridge at trigger date", "evidence_source": "historical public event / stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253450/2021.csv", "profile_path": "atlas/symbol_profiles/253/253450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-27", "entry_price": 89500, "MFE_30D_pct": 7.93, "MFE_90D_pct": 10.5, "MFE_180D_pct": 10.5, "MFE_1Y_pct": 10.5, "MFE_2Y_pct": 10.5, "MAE_30D_pct": -4.25, "MAE_90D_pct": -6.59, "MAE_180D_pct": -19.22, "MAE_1Y_pct": -33.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-22", "peak_price": 98900, "drawdown_after_peak_pct": -26.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "no_full_4B_without_cost_or_margin_evidence", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C27_CASE_004_GRP_STAGE2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R8L11_C27_TRG_005A_CJENM_STAGE2_WATCH_2021_09_23", "case_id": "R8L11_C27_CASE_005_CJENM_2021_CONTENT_PLATFORM_INVESTMENT_MARGIN_DRAG", "symbol": "035760", "company_name": "CJ ENM", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_PLATFORM_SCALE_WITH_COST_DRAG", "sector": "platform_content_sw_security", "primary_archetype": "content_ip_global_monetization", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Watch", "trigger_date": "2021-09-23", "evidence_available_at_that_date": "global studio/platform investment narrative; conversion evidence was offset by content cost and platform investment burden", "evidence_source": "historical public event / stock-web OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035760/2021.csv", "profile_path": "atlas/symbol_profiles/035/035760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-23", "entry_price": 155900, "MFE_30D_pct": 22.9, "MFE_90D_pct": 22.9, "MFE_180D_pct": 22.9, "MFE_1Y_pct": 22.9, "MFE_2Y_pct": 22.9, "MAE_30D_pct": -5.39, "MAE_90D_pct": -24.31, "MAE_180D_pct": -39.26, "MAE_1Y_pct": -47.59, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-10-25", "peak_price": 191600, "drawdown_after_peak_pct": -51.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "4B_too_late_if_cost_drag_ignored", "four_b_evidence_type": ["margin_or_backlog_slowdown", "valuation_blowoff"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C27_CASE_005_GRP_STAGE2", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C27_CASE_001_JYP_2023_GLOBAL_ALBUM_TOUR_CONVERSION", "trigger_id": "R8L11_C27_TRG_001A_JYP_STAGE2_ACTIONABLE_2023_05_15", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 14, "fanbase_demand_score": 16, "platform_distribution_score": 4, "content_cost_burden_score": 0, "control_premium_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 18, "fanbase_demand_score": 16, "platform_distribution_score": 4, "content_cost_burden_score": 0, "control_premium_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["global_ip_conversion_score", "content_cost_burden_score", "control_premium_risk_score"], "component_delta_explanation": "C27 shadow profile rewards measurable IP conversion and penalizes control-premium/event-only or content-cost-drag cases.", "MFE_90D_pct": 53.51, "MAE_90D_pct": -3.46, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C27_CASE_001_JYP_2023_GLOBAL_ALBUM_TOUR_CONVERSION", "trigger_id": "R8L11_C27_TRG_001B_JYP_STAGE3_GREEN_2023_05_16", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 16, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 18, "fanbase_demand_score": 16, "platform_distribution_score": 4, "content_cost_burden_score": 0, "control_premium_risk_score": 0, "financial_visibility_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 18, "fanbase_demand_score": 16, "platform_distribution_score": 4, "content_cost_burden_score": 0, "control_premium_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["global_ip_conversion_score", "content_cost_burden_score", "control_premium_risk_score"], "component_delta_explanation": "C27 shadow profile rewards measurable IP conversion and penalizes control-premium/event-only or content-cost-drag cases.", "MFE_90D_pct": 27.04, "MAE_90D_pct": -12.39, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C27_CASE_001_JYP_2023_GLOBAL_ALBUM_TOUR_CONVERSION", "trigger_id": "R8L11_C27_TRG_001C_JYP_4B_OVERLAY_2023_07_25", "symbol": "035900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 12, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 18, "fanbase_demand_score": 14, "platform_distribution_score": 0, "content_cost_burden_score": 0, "control_premium_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 18, "fanbase_demand_score": 14, "platform_distribution_score": 0, "content_cost_burden_score": 0, "control_premium_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage4B-overlay", "changed_components": ["global_ip_conversion_score", "content_cost_burden_score", "control_premium_risk_score"], "component_delta_explanation": "C27 shadow profile rewards measurable IP conversion and penalizes control-premium/event-only or content-cost-drag cases.", "MFE_90D_pct": 3.9, "MAE_90D_pct": -29.27, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C27_CASE_002_HYBE_2023_WEVERSE_MULTI_ARTIST_IP_SCALE", "trigger_id": "R8L11_C27_TRG_002A_HYBE_STAGE2_ACTIONABLE_2023_04_03", "symbol": "352820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 16, "fanbase_demand_score": 15, "platform_distribution_score": 4, "content_cost_burden_score": 0, "control_premium_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 18, "fanbase_demand_score": 16, "platform_distribution_score": 4, "content_cost_burden_score": 0, "control_premium_risk_score": 0}, "weighted_score_after": 85, "stage_label_after": "Stage3-Yellow-high", "changed_components": ["global_ip_conversion_score", "content_cost_burden_score", "control_premium_risk_score"], "component_delta_explanation": "C27 shadow profile rewards measurable IP conversion and penalizes control-premium/event-only or content-cost-drag cases.", "MFE_90D_pct": 69.84, "MAE_90D_pct": -0.16, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C27_CASE_003_SM_2023_CONTROL_PREMIUM_FALSE_C27", "trigger_id": "R8L11_C27_TRG_003A_SM_STAGE2_EVENT_2023_02_10", "symbol": "041510", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 8, "fanbase_demand_score": 10, "platform_distribution_score": 0, "content_cost_burden_score": 0, "control_premium_risk_score": 18}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 0, "fanbase_demand_score": 6, "platform_distribution_score": 0, "content_cost_burden_score": 0, "control_premium_risk_score": 24}, "weighted_score_after": 63, "stage_label_after": "Stage2-event/4B-watch", "changed_components": ["global_ip_conversion_score", "content_cost_burden_score", "control_premium_risk_score"], "component_delta_explanation": "C27 shadow profile rewards measurable IP conversion and penalizes control-premium/event-only or content-cost-drag cases.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -23.63, "score_return_alignment_label": "residual_error", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C27_CASE_003_SM_2023_CONTROL_PREMIUM_FALSE_C27", "trigger_id": "R8L11_C27_TRG_003B_SM_4B_CONTROL_PREMIUM_2023_03_08", "symbol": "041510", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 0, "fanbase_demand_score": 0, "platform_distribution_score": 0, "content_cost_burden_score": 0, "control_premium_risk_score": 20}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 22, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 0, "fanbase_demand_score": 0, "platform_distribution_score": 0, "content_cost_burden_score": 0, "control_premium_risk_score": 28}, "weighted_score_after": 58, "stage_label_after": "Stage4B-overlay", "changed_components": ["global_ip_conversion_score", "content_cost_burden_score", "control_premium_risk_score"], "component_delta_explanation": "C27 shadow profile rewards measurable IP conversion and penalizes control-premium/event-only or content-cost-drag cases.", "MFE_90D_pct": 1.7, "MAE_90D_pct": -44.73, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C27_CASE_004_STUDIO_DRAGON_2021_GLOBAL_KDRAMA_BUZZ_NO_OPERATING_LEVERAGE", "trigger_id": "R8L11_C27_TRG_004A_STUDIO_DRAGON_STAGE2_WATCH_2021_09_27", "symbol": "253450", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 12, "fanbase_demand_score": 4, "platform_distribution_score": 8, "content_cost_burden_score": 10, "control_premium_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 6, "fanbase_demand_score": 3, "platform_distribution_score": 8, "content_cost_burden_score": 18, "control_premium_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "Stage2-Watch", "changed_components": ["global_ip_conversion_score", "content_cost_burden_score", "control_premium_risk_score"], "component_delta_explanation": "C27 shadow profile rewards measurable IP conversion and penalizes control-premium/event-only or content-cost-drag cases.", "MFE_90D_pct": 10.5, "MAE_90D_pct": -6.59, "score_return_alignment_label": "residual_error", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C27_CASE_005_CJENM_2021_CONTENT_PLATFORM_INVESTMENT_MARGIN_DRAG", "trigger_id": "R8L11_C27_TRG_005A_CJENM_STAGE2_WATCH_2021_09_23", "symbol": "035760", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 12, "fanbase_demand_score": 0, "platform_distribution_score": 12, "content_cost_burden_score": 8, "control_premium_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "global_ip_conversion_score": 6, "fanbase_demand_score": 0, "platform_distribution_score": 10, "content_cost_burden_score": 22, "control_premium_risk_score": 0}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch/4B-risk", "changed_components": ["global_ip_conversion_score", "content_cost_burden_score", "control_premium_risk_score"], "component_delta_explanation": "C27 shadow profile rewards measurable IP conversion and penalizes control-premium/event-only or content-cost-drag cases.", "MFE_90D_pct": 22.9, "MAE_90D_pct": -24.31, "score_return_alignment_label": "residual_error", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "scheduled_round": "R8", "scheduled_loop": 11, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["content_buzz_false_green", "control_premium_false_c27", "content_cost_drag_4B_late"], "diversity_score_summary": "new_symbols=5; new_trigger_families=5; counterexamples=3; residual_errors=3; wrong_round_penalty=0", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop = 11
next_round = R9
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Stock-Web manifest: atlas/manifest.json
Stock-Web schema: atlas/schema.json
R8 calibration artifact: reports/e2r_calibration/by_round/R8.md
JYP profile: atlas/symbol_profiles/035/035900.json
HYBE profile: atlas/symbol_profiles/352/352820.json
SM profile: atlas/symbol_profiles/041/041510.json
Studio Dragon profile: atlas/symbol_profiles/253/253450.json
CJ ENM profile: atlas/symbol_profiles/035/035760.json
JYP OHLC rows checked around 2023-05-15, 2023-07-25, 2023-11-17.
HYBE OHLC rows checked around 2023-04-03, 2023-06-22, 2023-10~11 drawdown.
SM OHLC rows checked around 2023-02-10, 2023-03-08, 2023-03-27~28, and later range.
Studio Dragon OHLC rows checked around 2021-09-27, 2021-11-22, 2022-01-27.
CJ ENM OHLC rows checked around 2021-09-23, 2021-10-25, 2022-06~07 drawdown.
```

