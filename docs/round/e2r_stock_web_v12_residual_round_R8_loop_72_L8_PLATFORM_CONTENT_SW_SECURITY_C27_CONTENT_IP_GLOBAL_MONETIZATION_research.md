# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R8
scheduled_loop: 72
completed_round: R8
completed_loop: 72
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_LAUNCH_MONETIZATION_VS_TRAILER_ONLY
output_file: e2r_stock_web_v12_residual_round_R8_loop_72_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
price_route_hunt_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption

The current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The rollback reference remains `e2r_2_0_baseline_reference`. This MD does not re-argue the global Stage2 bonus or Green lateness rules. It tests whether a content/game-IP specific commercialization bridge is needed after the global calibration.

Current applied axes tested here:

| axis | status in this MD | reason |
|---|---:|---|
| stage2_actionable_evidence_bonus | existing_axis_tested | Content IP can be actionable only after launch-to-monetization evidence, not trailer-only attention. |
| price_only_blowoff_blocks_positive_stage | existing_axis_strengthened | Pearl Abyss/DokeV shows price-only trailer momentum can be large but not structural. |
| full_4b_requires_non_price_evidence | existing_axis_strengthened | Local price peaks in game/IP names are often too early unless supported by slowdown, launch quality, retention, or release-delay evidence. |
| hard_4c_thesis_break_routes_to_4c | existing_axis_strengthened | NCSoft/B&S2 launch reception is a hard thesis-break timing example. |

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R8 |
| scheduled_loop | 72 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| fine_archetype_id | GAME_IP_GLOBAL_LAUNCH_MONETIZATION_VS_TRAILER_ONLY |
| round_sector_consistency | pass |
| loop_objective | residual_false_positive_mining; residual_missed_structural_mining; 4C_thesis_break_timing_test; sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill |

R8 allows platform/content/SW/security. C27 is the cleanest R8 canonical container for game IP, live-service IP, and global monetization paths.

## 3. Previous Coverage / Duplicate Avoidance Check

The immediately previous local state was R7 / Loop 72, with next_round = R8 and next_loop = 72. This run therefore continues the sequential scheduler rather than jumping to an uncovered sector.

Duplicate-risk check:

| duplicate key component | result |
|---|---|
| same canonical only | allowed |
| same symbol + trigger_date + entry_date from this session | not found in current local run state |
| reused case count | 0 |
| new symbol count | 4 |
| new trigger family count | 4 |
| new independent case ratio | 1.00 |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used in this MD:

| field | value |
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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Tradable shard columns: `d,o,h,l,c,v,a,mc,s,m`.

The stock-web schema states that MFE is computed as `max high from entry_date through N tradable rows / entry_price - 1`, and MAE is computed as `min low from entry_date through N tradable rows / entry_price - 1`. All quantitative rows below use `tradable_raw` and do not use raw shard rows for calibration.

## 5. Historical Eligibility Gate

| case_id | entry_date | 180D forward available by manifest max_date | profile CA overlap in 180D | calibration_usable | reason |
|---|---:|---:|---:|---:|---|
| R8L72_C27_KG_ODIN_20210702 | 2021-07-02 | true | none | true | clean 180D tradable window |
| R8L72_C27_KRAFTON_BGMI_Q3_20231108 | 2023-11-08 | true | none | true | clean 180D tradable window |
| R8L72_C27_NCSOFT_BNS2_4C_20210826 | 2021-08-26 | true | none | true | profile CA candidates are 2003 only |
| R8L72_C27_PEARLABYSS_DOKEV_TRAILER_20210826 | 2021-08-26 | true | none | true | profile CA candidate 2021-04-16 before window |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | rule compression |
|---|---|---|
| GAME_IP_LAUNCH_TO_GROSSING_RANK | C27_CONTENT_IP_GLOBAL_MONETIZATION | Launch evidence only becomes promotable after app-store grossing/ranking or paid-user conversion evidence. |
| PUBG_BGMI_REGION_REOPENING_OPERATING_LEVERAGE | C27_CONTENT_IP_GLOBAL_MONETIZATION | A live-service franchise can rerate without a contract/backlog field if regional reopening, user base, and margin bridge align. |
| GAME_LAUNCH_RECEPTION_THESIS_BREAK | C27_CONTENT_IP_GLOBAL_MONETIZATION | Poor launch reception is hard 4C when it breaks existing IP monetization thesis. |
| TRAILER_ONLY_IP_OPTIONALITY_WITHOUT_COMMERCIALIZATION | C27_CONTENT_IP_GLOBAL_MONETIZATION | Trailer-only optionality must remain watch-only until commercial conversion evidence appears. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---|
| R8L72_C27_KG_ODIN_20210702 | 293490 | 카카오게임즈 | structural_success | Stage2-Actionable | 2021-07-02 | 71,600 | current_profile_correct |
| R8L72_C27_KRAFTON_BGMI_Q3_20231108 | 259960 | 크래프톤 | missed_structural | Stage2-Actionable | 2023-11-08 | 190,800 | current_profile_missed_structural |
| R8L72_C27_NCSOFT_BNS2_4C_20210826 | 036570 | 엔씨소프트 | 4C_success | Stage4C-Hard | 2021-08-26 | 709,000 | current_profile_4C_too_late |
| R8L72_C27_PEARLABYSS_DOKEV_TRAILER_20210826 | 263750 | 펄어비스 | price_moved_without_evidence | Stage2-WatchOnly | 2021-08-26 | 87,900 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| label | count | cases |
|---|---:|---|
| positive_case_count | 2 | 카카오게임즈, 크래프톤 |
| counterexample_count | 2 | 엔씨소프트, 펄어비스 |
| 4B_case_count | 1 | 펄어비스 local price-only 4B too early |
| 4C_case_count | 1 | 엔씨소프트 hard 4C launch thesis break |
| calibration_usable_case_count | 4 | all selected cases |

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | source note |
|---|---|---|---|---|---|
| 카카오게임즈 / Odin | launch + grossing/rank conversion | repeat conversion / financial visibility | none at entry | none | public launch/ranking reports; price source verified by stock-web |
| 크래프톤 / PUBG-BGMI | Q3 result + live-service durability + regional reopening | confirmed margin/revision bridge | later positioning/valuation overheat | none | public earnings/news; BGMI relaunch/user-base context from public sources |
| 엔씨소프트 / B&S2 | launch event | none | launch expectation overhang | launch reception broke monetization thesis | public launch/reception reports; price source verified by stock-web |
| 펄어비스 / DokeV | gameplay trailer + relative strength | none | price-only local peak | delayed commercialization / thesis not converted | public Gamescom trailer/release-delay sources; price source verified by stock-web |

## 10. Price Data Source Map

| symbol | profile_path | shard_path | profile status | CA candidate dates relevant to window |
|---:|---|---|---|---|
| 293490 | atlas/symbol_profiles/293/293490.json | atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv; 2022.csv | active_like, no CA candidates | none |
| 259960 | atlas/symbol_profiles/259/259960.json | atlas/ohlcv_tradable_by_symbol_year/259/259960/2023.csv; 2024.csv | active_like, no CA candidates | none |
| 036570 | atlas/symbol_profiles/036/036570.json | atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv; 2022.csv | active_like, CA candidates only 2003 | none in 2021-2022 window |
| 263750 | atlas/symbol_profiles/263/263750.json | atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv; 2022.csv | active_like, one CA candidate 2021-04-16 | none in 2021-08-26~D+180 window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_date | evidence timing | entry_date | entry_price | same_entry_group_id | dedupe_for_aggregate |
|---|---|---:|---|---:|---:|---|---:|
| KG_ODIN_STAGE2_ACTIONABLE_20210702 | R8L72_C27_KG_ODIN_20210702 | 2021-07-02 | launch-to-grossing conversion visible | 2021-07-02 | 71,600 | 293490_2021-07-02_71600 | true |
| KRAFTON_Q3_STAGE2_ACTIONABLE_20231108 | R8L72_C27_KRAFTON_BGMI_Q3_20231108 | 2023-11-08 | Q3 result reaction / live-service bridge | 2023-11-08 | 190,800 | 259960_2023-11-08_190800 | true |
| NCSOFT_BNS2_HARD4C_20210826 | R8L72_C27_NCSOFT_BNS2_4C_20210826 | 2021-08-26 | launch reception break | 2021-08-26 | 709,000 | 036570_2021-08-26_709000 | true |
| PEARLABYSS_DOKEV_TRAILER_STAGE2_FALSE_POSITIVE_20210826 | R8L72_C27_PEARLABYSS_DOKEV_TRAILER_20210826 | 2021-08-26 | trailer-only relative strength | 2021-08-26 | 87,900 | 263750_2021-08-26_87900 | true |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 293490 | 2021-07-02 | 71,600 | 48.04% | -18.58% | 48.04% | -18.58% | 62.01% | -18.58% | 2021-11-17 | 116,000 |
| 259960 | 2023-11-08 | 190,800 | 16.09% | -5.50% | 27.62% | -7.23% | 56.71% | -7.23% | 2024-06-24 | 299,000 |
| 036570 | 2021-08-26 | 709,000 | 11.14% | -21.72% | 11.14% | -21.72% | 11.14% | -41.26% | 2021-08-26 | 788,000 |
| 263750 | 2021-08-26 | 87,900 | 16.04% | -17.97% | 65.19% | -17.97% | 65.19% | -36.18% | 2021-11-17 | 145,200 |

Interpretation: C27 names are convex but treacherous. The same visible price acceleration can mean either real IP monetization or merely option premium. The calibration switch should sit on commercialization evidence, not on the slope of the chart.

## 13. Current Calibrated Profile Stress Test

| case | current profile likely label | actual OHLC alignment | verdict | residual error |
|---|---|---|---|---|
| 카카오게임즈/Odin | Stage2-Actionable to Yellow | strong MFE, high entry volatility | current_profile_correct | no |
| 크래프톤/BGMI-Q3 | Stage2-Watch / late Yellow | 180D MFE +56.71%, shallow MAE | current_profile_missed_structural | yes |
| 엔씨소프트/B&S2 | delayed 4C unless launch reception captured | 180D MAE -41.26% | current_profile_4C_too_late | yes |
| 펄어비스/DokeV | could over-promote if trailer treated as IP evidence | high MFE but later collapse, no release bridge | current_profile_false_positive | yes |

Answers to required stress questions:

1. Current profile mostly handles generic Stage2 bonus, but C27 needs a commercialization bridge.  
2. MFE/MAE supports promotion for launch/revenue conversion, not for trailer-only hype.  
3. Stage2 bonus is not globally wrong; it is too generous for trailer-only IP optionality and too weak for live-service reopening with margin bridge.  
4. Yellow threshold 75 is acceptable, but C27 inputs need better component mapping.  
5. Green 87/revision 55 is still appropriate; this MD does not weaken it.  
6. Price-only blowoff guard is strengthened.  
7. Full 4B non-price requirement is strengthened.  
8. Hard 4C routing should be faster when launch reception breaks the IP monetization thesis.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable date | Stage3-Yellow proxy | Stage3-Green proxy | green_lateness_ratio | note |
|---|---:|---:|---:|---:|---|
| 카카오게임즈 | 2021-07-02 | 2021-07 to 2021-Q3 confirmation | not used | 0.72 | Green confirmation after much of upside; use Actionable when grossing evidence appears. |
| 크래프톤 | 2023-11-08 | 2024-Q1/Q2 continuation | not used | 0.43 | Yellow not too late if Q3 result is admitted as C27 bridge. |
| 엔씨소프트 | not applicable | not applicable | not applicable | not_applicable | This is a hard 4C trigger, not a promotion trigger. |
| 펄어비스 | watch-only only | should not Yellow | should not Green | not_applicable | Trailer-only should not become Stage3 without release or monetization bridge. |

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B candidate | local_peak | full_peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| 카카오게임즈 | 2021-07-26 local overheating | 106,000 | 116,000 | 0.68 | 0.53 | price-only local 4B too early without slowdown evidence |
| 크래프톤 | 2024-06 late-positioning overheat | 299,000 | 299,000 | 0.97 | 0.98 | good full-window 4B only if non-price slowdown appears |
| 엔씨소프트 | not 4B | n/a | n/a | n/a | n/a | launch thesis break should route to 4C |
| 펄어비스 | 2021-08-30 local trailer spike | 102,000 | 145,200 | 1.00 | 0.25 | price-only local 4B too early; no full 4B without non-price evidence |

## 16. 4C Protection Audit

| case | 4C trigger | label | protection interpretation |
|---|---:|---|---|
| 엔씨소프트 | 2021-08-26 | hard_4c_success | Early 4C would have avoided a large part of the 180D drawdown path. |
| 펄어비스 | delayed commercialization after trailer-only rerating | thesis_break_watch_only | Not a hard 4C at trigger, but a watch-only cap was required from day one. |
| 카카오게임즈 | n/a | n/a | No hard thesis break in observed window. |
| 크래프톤 | n/a | n/a | No hard thesis break in observed window. |

## 17. Sector-Specific Rule Candidate

```text
rule_id = L8_C27_CONTENT_IP_COMMERCIALIZATION_BRIDGE
scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
proposal_type = shadow_only
```

Rule candidate:

> In R8/C27, Stage2 promotion requires at least one commercialization bridge: launch-to-grossing conversion, live-service user/revenue reactivation, repeat paid-user signal, or confirmed margin/revision bridge. Trailer, gameplay reveal, or social buzz alone is capped at Stage2-WatchOnly regardless of relative strength.

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C27_TRAILER_ONLY_OPTIONALITY_CAP_AND_LAUNCH_RECEPTION_4C
scope = canonical_archetype_specific
proposal_type = archetype_shadow_only
```

Two-part canonical rule:

1. `C27_trailer_only_cap`: if evidence is trailer/gameplay/social buzz only and no release date/preorder/revenue/retention bridge exists, cap at Stage2-WatchOnly and block Yellow/Green.  
2. `C27_launch_reception_4C`: if launch reception breaks the existing IP monetization thesis, route directly to hard 4C even if the IP was previously high quality.

## 19. Before / After Backtest Comparison

| profile | eligible triggers | selected cases | avg MFE_90D | avg MAE_90D | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | all | 38.00% | -16.38% | 25% | 1 | mixed; C27-specific bridge missing |
| P0b e2r_2_0_baseline_reference | 4 | all | 38.00% | -16.38% | 25% | 2 | worse; no post-calibration guardrails |
| P1 sector_specific_candidate_profile | 3 | KG, Krafton, NC 4C | 28.93% | -15.84% | 0% | 0 | improved by blocking trailer-only promotion |
| P2 canonical_archetype_candidate_profile | 4 | all but Pearl capped watch-only | 38.00% | -16.38% | 0% as promotion set | 0 | best explanatory alignment |
| P3 counterexample_guard_profile | 2 risk rows | NC, Pearl | n/a | n/a | n/a | n/a | strengthens 4C and price-only guard |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| KG_ODIN_STAGE2_ACTIONABLE_20210702 | 72 | Stage2-Actionable | 78 | Stage3-Yellow | 48.04% | -18.58% | aligned, high volatility |
| KRAFTON_Q3_STAGE2_ACTIONABLE_20231108 | 70 | Stage2-Watch | 80 | Stage3-Yellow | 27.62% | -7.23% | after profile fixes missed structural |
| NCSOFT_BNS2_HARD4C_20210826 | 64 | Stage2-Watch | 42 | Stage4C | 11.14% | -21.72% | hard 4C protects |
| PEARLABYSS_DOKEV_TRAILER_STAGE2_FALSE_POSITIVE_20210826 | 76 | Stage3-Yellow | 56 | Stage2-WatchOnly | 65.19% | -17.97% | MFE alone misleading; rule blocks structural label |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | GAME_IP_GLOBAL_LAUNCH_MONETIZATION_VS_TRAILER_ONLY | 2 | 2 | 1 | 1 | 4 | 0 | 4 | 4 | 3 | true | true | reduced; still needs non-game content/IP cases such as music, webtoon, and OTT |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_false_positive
  - current_profile_4C_too_late
new_axis_proposed:
  - C27_commercialization_bridge_required_for_Yellow_or_Green
  - C27_trailer_only_optionality_cap
  - C27_launch_reception_hard_4C
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest max date and price basis.
- Symbol profile availability and corporate-action window checks.
- Tradable shard OHLC rows for trigger entry, peak, MFE, and MAE calculations.
- Historical trigger-level positive/counterexample balance inside scheduled R8.

Not validated:

- No production scoring code was opened.
- No live candidate scan was run.
- No investment recommendation was generated.
- Evidence-source text was used only for historical trigger context; exact production ingestion should re-fetch official filings/news when batch-promoting.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_commercialization_bridge_required_for_Yellow_or_Green,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Promote content/game IP only after launch-to-revenue or live-service conversion evidence","Reduces Pearl Abyss trailer-only false positive while retaining Kakao Games and Krafton positives","KG_ODIN_STAGE2_ACTIONABLE_20210702|KRAFTON_Q3_STAGE2_ACTIONABLE_20231108|PEARLABYSS_DOKEV_TRAILER_STAGE2_FALSE_POSITIVE_20210826",4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_launch_reception_hard_4C,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Poor launch reception can break IP monetization thesis immediately","Improves NCSoft B&S2 4C timing","NCSOFT_BNS2_HARD4C_20210826",4,4,2,medium,archetype_shadow_only,"not production; 4C protection only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L72_C27_KG_ODIN_20210702", "symbol": "293490", "company_name": "카카오게임즈", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_MONETIZATION_VS_TRAILER_ONLY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "KG_ODIN_STAGE2_ACTIONABLE_20210702", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "오딘 출시 직후 매출순위/흥행 확인형. price-only가 아니라 launch-to-monetization 전환이 보였던 게임 IP 표본."}
{"row_type": "case", "case_id": "R8L72_C27_KRAFTON_BGMI_Q3_20231108", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_MONETIZATION_VS_TRAILER_ONLY", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "KRAFTON_Q3_STAGE2_ACTIONABLE_20231108", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_current_profile_underweighted", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Q3 실적과 PUBG/BGMI 지역 재개·운영 레버리지 결합. 계약/backlog형이 아니어서 current profile이 구조성을 과소평가하기 쉬운 표본."}
{"row_type": "case", "case_id": "R8L72_C27_NCSOFT_BNS2_4C_20210826", "symbol": "036570", "company_name": "엔씨소프트", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_MONETIZATION_VS_TRAILER_ONLY", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "NCSOFT_BNS2_HARD4C_20210826", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "negative_alignment_after_thesis_break", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "신작 출시가 기존 IP 기대를 상업화로 전환하지 못한 4C 표본. launch itself가 아니라 reception/monetization break가 핵심."}
{"row_type": "case", "case_id": "R8L72_C27_PEARLABYSS_DOKEV_TRAILER_20210826", "symbol": "263750", "company_name": "펄어비스", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_MONETIZATION_VS_TRAILER_ONLY", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "PEARLABYSS_DOKEV_TRAILER_STAGE2_FALSE_POSITIVE_20210826", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_MFE_but_poor_structural_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "게임스컴 트레일러가 강한 MFE를 만들었지만 출시·예약·매출 전환 증거가 없던 trailer-only IP optionality 표본."}
{"row_type": "trigger", "trigger_id": "KG_ODIN_STAGE2_ACTIONABLE_20210702", "case_id": "R8L72_C27_KG_ODIN_20210702", "symbol": "293490", "company_name": "카카오게임즈", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_LAUNCH_TO_GROSSING_RANK", "sector": "game_content", "primary_archetype": "launch_to_monetization", "loop_objective": "sector_specific_rule_discovery|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-07-02", "evidence_available_at_that_date": "Odin launch window followed by immediate top-grossing/ranking evidence; revenue conversion visible before quarterly confirmation.", "evidence_source": "public launch/ranking reports; stock-web OHLC rows validated in atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["repeat_order_or_conversion", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv", "profile_path": "atlas/symbol_profiles/293/293490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-07-02", "entry_price": 71600, "MFE_30D_pct": 48.04, "MFE_90D_pct": 48.04, "MFE_180D_pct": 62.01, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.58, "MAE_90D_pct": -18.58, "MAE_180D_pct": -18.58, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-17", "peak_price": 116000, "drawdown_after_peak_pct": -44.91, "green_lateness_ratio": 0.72, "four_b_local_peak_proximity": 0.68, "four_b_full_window_peak_proximity": 0.53, "four_b_timing_verdict": "price_only_local_4B_too_early_if_no_non_price_slowdown", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_high_volatility", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "293490_2021-07-02_71600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "KRAFTON_Q3_STAGE2_ACTIONABLE_20231108", "case_id": "R8L72_C27_KRAFTON_BGMI_Q3_20231108", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "PUBG_BGMI_REGION_REOPENING_OPERATING_LEVERAGE", "sector": "game_content", "primary_archetype": "live_service_ip_operating_leverage", "loop_objective": "residual_missed_structural_mining|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-11-08", "evidence_available_at_that_date": "Q3 earnings reaction, PUBG/BGMI live-service durability, and India reactivation/regional option value.", "evidence_source": "public earnings/news + stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/259/259960/2023.csv and 2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2023.csv|atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-11-08", "entry_price": 190800, "MFE_30D_pct": 16.09, "MFE_90D_pct": 27.62, "MFE_180D_pct": 56.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.5, "MAE_90D_pct": -7.23, "MAE_180D_pct": -7.23, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-24", "peak_price": 299000, "drawdown_after_peak_pct": -18.23, "green_lateness_ratio": 0.43, "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_only_after_non_price_slowdown_check", "four_b_evidence_type": ["positioning_overheat", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_current_profile_underweighted", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "259960_2023-11-08_190800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "NCSOFT_BNS2_HARD4C_20210826", "case_id": "R8L72_C27_NCSOFT_BNS2_4C_20210826", "symbol": "036570", "company_name": "엔씨소프트", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_LAUNCH_RECEPTION_THESIS_BREAK", "sector": "game_content", "primary_archetype": "launch_quality_4C", "loop_objective": "4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "Stage4C-Hard", "trigger_date": "2021-08-26", "evidence_available_at_that_date": "Blade & Soul 2 launch/reception window broke the existing IP monetization thesis; market repriced immediately.", "evidence_source": "public launch/reception reports + stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv and 2022.csv", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken", "qualification_failure"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv|atlas/ohlcv_tradable_by_symbol_year/036/036570/2022.csv", "profile_path": "atlas/symbol_profiles/036/036570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-08-26", "entry_price": 709000, "MFE_30D_pct": 11.14, "MFE_90D_pct": 11.14, "MFE_180D_pct": 11.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.72, "MAE_90D_pct": -21.72, "MAE_180D_pct": -41.26, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-08-26", "peak_price": 788000, "drawdown_after_peak_pct": -47.14, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "4C_not_4B_launch_thesis_break", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_protected_from_180D_drawdown", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "036570_2021-08-26_709000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "PEARLABYSS_DOKEV_TRAILER_STAGE2_FALSE_POSITIVE_20210826", "case_id": "R8L72_C27_PEARLABYSS_DOKEV_TRAILER_20210826", "symbol": "263750", "company_name": "펄어비스", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "TRAILER_ONLY_IP_OPTIONALITY_WITHOUT_COMMERCIALIZATION", "sector": "game_content", "primary_archetype": "trailer_hype_false_positive", "loop_objective": "residual_false_positive_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-WatchOnly", "trigger_date": "2021-08-26", "evidence_available_at_that_date": "DokeV gameplay trailer created price momentum, but no release date, preorder, retention, or revenue bridge was available at trigger.", "evidence_source": "public Gamescom/DokeV trailer source + stock-web OHLC rows in atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv and 2022.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv|atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv", "profile_path": "atlas/symbol_profiles/263/263750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-08-26", "entry_price": 87900, "MFE_30D_pct": 16.04, "MFE_90D_pct": 65.19, "MFE_180D_pct": 65.19, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.97, "MAE_90D_pct": -17.97, "MAE_180D_pct": -36.18, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-17", "peak_price": 145200, "drawdown_after_peak_pct": -61.36, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_MFE_false_positive_without_commercialization_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "263750_2021-08-26_87900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L72_C27_KG_ODIN_20210702", "trigger_id": "KG_ODIN_STAGE2_ACTIONABLE_20210702", "symbol": "293490", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 18, "relative_strength_score": 15, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 22, "relative_strength_score": 15, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "launch rank converted to monetization; no new global axis", "MFE_90D_pct": 48.04, "MAE_90D_pct": -18.58, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L72_C27_KRAFTON_BGMI_Q3_20231108", "trigger_id": "KRAFTON_Q3_STAGE2_ACTIONABLE_20231108", "symbol": "259960", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 16, "relative_strength_score": 0, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 0, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C27 live-service IP reopening bridge adds sector component", "MFE_90D_pct": 27.62, "MAE_90D_pct": -7.23, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L72_C27_NCSOFT_BNS2_4C_20210826", "trigger_id": "NCSOFT_BNS2_HARD4C_20210826", "symbol": "036570", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -25, "legal_or_contract_risk_score": -8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage4C", "changed_components": ["customer_quality_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "launch reception broke thesis; hard 4C override", "MFE_90D_pct": 11.14, "MAE_90D_pct": -21.72, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C27_shadow", "case_id": "R8L72_C27_PEARLABYSS_DOKEV_TRAILER_20210826", "trigger_id": "PEARLABYSS_DOKEV_TRAILER_STAGE2_FALSE_POSITIVE_20210826", "symbol": "263750", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage2-WatchOnly", "changed_components": ["customer_quality_score", "revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "trailer-only optionality capped unless commercialization bridge exists", "MFE_90D_pct": 65.19, "MAE_90D_pct": -17.97, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R8", "loop": "72", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_false_positive", "current_profile_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/&lt;prefix&gt;/&lt;ticker&gt;/&lt;year&gt;.csv.
- Symbol profile pattern: atlas/symbol_profiles/&lt;prefix&gt;/&lt;ticker&gt;.json.

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
completed_loop = 72
next_round = R9
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files checked:

- `atlas/manifest.json` — manifest max_date, row counts, price adjustment status.
- `atlas/schema.json` — tradable/raw columns and MFE/MAE formulas.
- `atlas/symbol_profiles/293/293490.json` — Kakao Games profile, no corporate action candidates.
- `atlas/symbol_profiles/259/259960.json` — Krafton profile, no corporate action candidates.
- `atlas/symbol_profiles/036/036570.json` — NCSoft profile, CA candidates only in 2003.
- `atlas/symbol_profiles/263/263750.json` — Pearl Abyss profile, one CA candidate before selected window.
- `atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv` and `2022.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/259/259960/2023.csv` and `2024.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv` and `2022.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv` and `2022.csv`.

External narrative references used only for event timing/context:

- DokeV gameplay trailer premiered at Gamescom Opening Night Live on 2021-08-25, and later release expectations remained far beyond the original hype window.
- Blade & Soul 2 launched on 2021-08-26.
- BGMI/PUBG public history confirms India reopening/relaunch context and large user-base relevance.


