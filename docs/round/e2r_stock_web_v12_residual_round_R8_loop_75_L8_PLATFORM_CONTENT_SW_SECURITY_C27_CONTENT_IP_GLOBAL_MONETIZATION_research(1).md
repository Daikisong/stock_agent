# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R8
scheduled_loop: 75
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE
output_file: e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`, with the first Stock-Web calibration assumed already applied:

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

This MD does not re-propose those global axes. It stress-tests them inside a content/game IP monetization archetype and proposes shadow-only canonical guards.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R8 |
| scheduled_loop | 75 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| fine_archetype_id | MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; 4B_non_price_requirement_stress_test; coverage_gap_fill |

R8 is locked to platform/content/software security. C27 is used because the cleanest residual in this round is not “content attention exists,” but whether the attention becomes owned-IP or publisher-economics monetization.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were used only for coverage and duplicate avoidance. No `src/e2r` code was opened. The immediate prior user-visible state ended at R7/Loop75, so the valid next scheduled state is R8/Loop75.

Duplicate gate:

| Check | Result |
|---|---|
| same canonical archetype reuse | allowed |
| same symbol + same trigger date reuse | none |
| same entry group reuse | none |
| minimum new independent case ratio | 4/4 = 100% |
| minimum new symbol count | 4 |
| counterexample minimum | pass |
| positive minimum | pass |
| schema rematerialization risk | low |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`. Raw shards add `rs=row_status`. The calibration basis is raw, unadjusted, tradable-only OHLCV.

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative triggers are historical and have at least 180 forward stock-web tradable rows. Corporate-action windows were checked against symbol profiles.

| Symbol | Company | Profile caveat | Corporate action overlap in entry~D+180 | Calibration usable |
|---|---|---|---|---|
| 194480 | 데브시스터즈 | no corporate-action candidates | none | true |
| 293490 | 카카오게임즈 | no corporate-action candidates | none | true |
| 263750 | 펄어비스 | one historical corporate-action candidate on 2021-04-16 | before entry, no 180D overlap | true |
| 253450 | 스튜디오드래곤 | no corporate-action candidates | none | true |

## 6. Canonical Archetype Compression Map

| Fine route | Canonical compression | Promotion condition | Guard condition |
|---|---|---|---|
| Mobile game launch with owned IP | C27_CONTENT_IP_GLOBAL_MONETIZATION | Launch + revenue rank/download persistence + revision bridge | demote if only one-day attention |
| Publisher economics from new title | C27_CONTENT_IP_GLOBAL_MONETIZATION | Publisher share/economics visible and repeat revenue ranking | Green can still be late if waiting for full financial print |
| Trailer or gameplay showcase | C27_CONTENT_IP_GLOBAL_MONETIZATION | no Green unless launch/preorder/revenue visibility appears | price-only local 4B likely too early |
| Global streaming hit | C27_CONTENT_IP_GLOBAL_MONETIZATION | contract economics/margin bridge required | title attention alone is false-positive prone |

## 7. Case Selection Summary

| Case | Symbol | Company | Role | Trigger | Entry | Outcome |
|---|---:|---|---|---|---|---|
| R8L75_C27_194480_COOKIE_RUN_KINGDOM_LAUNCH | 194480 | 데브시스터즈 | structural_success | Cookie Run: Kingdom launch / early monetization | 2021-01-22 @ 22,400 | +790.62% 180D MFE |
| R8L75_C27_293490_ODIN_LAUNCH | 293490 | 카카오게임즈 | structural_success | Odin launch / revenue-rank conversion | 2021-06-30 @ 57,800 | +100.69% 180D MFE |
| R8L75_C27_263750_DOKEV_TRAILER | 263750 | 펄어비스 | failed_rerating | DokeV trailer visibility, no revenue timing | 2021-08-27 @ 89,000 | +63.15% peak but -27.42% 180D MAE and later collapse |
| R8L75_C27_253450_THE_GLORY_HIT | 253450 | 스튜디오드래곤 | false_positive_green | The Glory Netflix hit, no margin bridge | 2023-01-02 @ 83,800 | +6.21% MFE, -42.06% 180D MAE |

## 8. Positive vs Counterexample Balance

| Bucket | Count | Cases |
|---|---:|---|
| positive_structural_success | 2 | 194480, 293490 |
| counterexample_or_failed_rerating | 2 | 263750, 253450 |
| 4B / 4C audit rows | 2 | 263750 local price-only 4B, 253450 thesis-break watch |
| calibration_usable_case_count | 4 | all representative cases |

The central residual is simple: content IP events are not a single species. A launch with observable monetization is a cash register; a trailer or hit title without economics is a movie poster. Both create attention, but only one can ring the register.

## 9. Evidence Source Map

| Case | Evidence available at trigger date | Evidence source class | Stage2 evidence | Stage3 evidence |
|---|---|---|---|---|
| 194480 | Cookie Run: Kingdom public launch and immediate app-store monetization route | public release / app-store rank / company-owned IP | public_event_or_disclosure; customer_or_order_quality; relative_strength; capacity_or_volume_route | confirmed_revision; financial_visibility; repeat_order_or_conversion |
| 293490 | Odin launch and domestic revenue-ranking conversion | public launch / publisher economics / revenue rank | public_event_or_disclosure; customer_or_order_quality; relative_strength | confirmed_revision; financial_visibility |
| 263750 | DokeV trailer at Gamescom / Opening Night Live | trailer / visibility only | public_event_or_disclosure; relative_strength | none at trigger |
| 253450 | The Glory Part 1 Netflix release and global attention | streaming release / audience hit | public_event_or_disclosure; customer_or_order_quality | none at trigger |

## 10. Price Data Source Map

| Symbol | Tradable shard | Profile path | Entry row validation |
|---:|---|---|---|
| 194480 | atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv | atlas/symbol_profiles/194/194480.json | 2021-01-22 close 22,400 |
| 293490 | atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv | atlas/symbol_profiles/293/293490.json | 2021-06-30 close 57,800 |
| 263750 | atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv | atlas/symbol_profiles/263/263750.json | 2021-08-27 close 89,000 |
| 253450 | atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv | atlas/symbol_profiles/253/253450.json | 2023-01-02 close 83,800 |

## 11. Case-by-Case Trigger Grid

| Trigger ID | Symbol | Trigger type | Trigger date | Entry date | Entry price | Current profile verdict | Aggregate role |
|---|---:|---|---|---|---:|---|---|
| R8L75_T01_194480_STAGE2_ACTIONABLE_20210121 | 194480 | Stage2-Actionable | 2021-01-21 | 2021-01-22 | 22,400 | current_profile_correct | representative |
| R8L75_T02_293490_STAGE2_ACTIONABLE_20210629 | 293490 | Stage2-Actionable | 2021-06-29 | 2021-06-30 | 57,800 | current_profile_too_late | representative |
| R8L75_T03_263750_STAGE2_TRAILER_20210825 | 263750 | Stage2-Actionable | 2021-08-25 | 2021-08-27 | 89,000 | current_profile_too_early | representative |
| R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230 | 253450 | Stage2-Actionable | 2022-12-30 | 2023-01-02 | 83,800 | current_profile_false_positive | representative |
| R8L75_T03B_263750_PRICE_ONLY_LOCAL_4B_20210830 | 263750 | 4B-overlay | 2021-08-30 | 2021-08-30 | 102,000 | current_profile_4B_too_early | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger metrics:

| Case | Entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | Peak date | Peak price | Drawdown after peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R8L75_C27_194480_COOKIE_RUN_KINGDOM_LAUNCH | 22,400 | 208.04% | -18.08% | 618.75% | -18.08% | 790.62% | -18.08% | 2021-09-27 | 199,500 | -73.43% |
| R8L75_C27_293490_ODIN_LAUNCH | 57,800 | 83.39% | -1.04% | 83.39% | -1.04% | 100.69% | -1.04% | 2021-11-17 | 116,000 | -86.46% |
| R8L75_C27_263750_DOKEV_TRAILER | 89,000 | 14.61% | -12.81% | 63.15% | -12.81% | 63.15% | -27.42% | 2021-11-17 | 145,200 | -74.28% |
| R8L75_C27_253450_THE_GLORY_HIT | 83,800 | 6.21% | -6.92% | 6.21% | -25.18% | 6.21% | -42.06% | 2023-01-02 | 89,000 | -48.31% |

Key raw OHLC anchor rows used in the calculations:

```text
194480 2021-01-22 c=22400 h=22400 l=18350; 2021-02-24 h=69000; 2021-03-26 h=161000; 2021-09-27 h=199500; 2022-03-08 l=53000 after peak
293490 2021-06-30 c=57800 h=60400 l=57500; 2021-07-26 h=106000; 2021-11-17 h=116000
263750 2021-08-27 c=89000 h=100100 l=87200; 2021-08-30 h=102000; 2021-11-17 h=145200; 2022-04-14 l=64600; 2022-10-13 l=37350
253450 2023-01-02 c=83800 h=89000 l=82100; 2023-02-09 h=84500; 2023-05-15 l=62700; 2023-07-10 l=48550; 2023-10-26 l=46000
```

## 13. Current Calibrated Profile Stress Test

| Case | Current profile likely judgment | Actual alignment | Residual |
|---|---|---|---|
| 194480 | Stage3-Yellow to Green after monetization evidence | correct | existing axis kept |
| 293490 | Stage3-Yellow first, Green only after later confirmation | direction correct but late | green_lateness_on_revenue_rank_conversion |
| 263750 | Stage2/Yellow from visibility and RS if monetization guard is weak | too early structurally | trailer_hype_false_positive |
| 253450 | Stage2/Yellow or weak Green from global title quality | false positive | global_hit_without_margin_bridge |

Answers to required stress-test questions:

1. Current calibrated profile separates price-only blowoff from non-price evidence, but C27 still needs a finer evidence taxonomy.
2. MFE/MAE alignment is strong for owned/publisher launch monetization and weak for visibility-only content attention.
3. The Stage2 bonus is useful for 194480 and 293490; too generous for 263750 and 253450 if applied to title attention alone.
4. Yellow threshold 75 is not the main problem; the component mix entering 75 is the problem.
5. Green threshold 87/revision 55 is directionally right, but revenue-rank conversion in games can justify earlier Green than formal accounting revision.
6. Price-only blowoff guard is appropriate and strengthened.
7. Full 4B non-price requirement is appropriate; price-only local peaks are too early in C27.
8. Hard 4C routing should remain hard, but thesis-break watch should start when monetization dates slip or hit-title economics fail to bridge into margin.

## 14. Stage2 / Yellow / Green Comparison

| Case | Stage2 entry | Stage3-Green proxy | Peak | green_lateness_ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| 194480 | 22,400 | 100,500 | 199,500 | 0.443 | Green was somewhat late, but still captured large upside |
| 293490 | 57,800 | 100,200 | 116,000 | 0.729 | Green waited for too much confirmation; most upside already gone |
| 263750 | 89,000 | n/a | 145,200 | not_applicable | no confirmed Stage3-Green; trailer was not monetization |
| 253450 | 83,800 | n/a | 89,000 | not_applicable | no Green should be issued without margin bridge |

## 15. 4B Local vs Full-window Timing Audit

| Case | 4B trigger | Local proximity | Full-window proximity | Verdict |
|---|---|---:|---:|---|
| 263750 | 2021-08-30 local trailer peak | 1.000 | 0.231 | price_only_local_4B_too_early |
| 263750 | 2021-11-17 full peak | n/a | 0.925 using close-vs-full-peak proxy | good price timing but still not full 4B without non-price evidence |
| 194480 | 2021-09-27 peak | n/a | n/a | post-success valuation blowoff; separate overlay, not entry scoring |
| 253450 | no full 4B | n/a | n/a | event did not create enough upside for 4B usefulness |

## 16. 4C Protection Audit

| Case | 4C label | Interpretation |
|---|---|---|
| 194480 | not_applicable | Later drawdown is a cycle/valuation issue after huge structural success |
| 293490 | not_applicable | Later two-year drawdown is not a trigger-date thesis break |
| 263750 | thesis_break_watch_only | Trailer-to-launch delay and no monetization route should start a watch state |
| 253450 | hard_4c_late_if_margin_disappointment_ignored | Global hit without margin bridge becomes a late-protection problem |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
rule = In content/game sectors, Stage2 can recognize IP attention, but Stage3 promotion requires direct monetization bridge.
```

Sector-specific shadow rule:

```text
if large_sector_id == L8_PLATFORM_CONTENT_SW_SECURITY
and event_type in [game_launch, owned_ip_launch, publisher_new_title_launch]
and revenue_rank_or_download_rank_persistence == true:
    allow Stage2-Actionable and earlier Stage3-Yellow
    permit Green only when revision/margin/customer-quality bridge appears

if event_type in [trailer, teaser, global_title_hit]
and no direct economics bridge:
    cap at Stage2-Actionable
    apply trailer_hype_decay_guard
    do_not_allow Stage3-Green
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
canonical rule = Separate content visibility from monetization visibility.
```

Canonical compression:

```text
C27_launch_monetization_positive:
  required = launch/release + revenue-rank/download-rank persistence or direct contract economics
  optional = relative strength
  Green requires = revision/margin/financial visibility

C27_visibility_only_counterexample:
  trigger = trailer/viral title/global attention
  block = no revenue timing, no contract economics, no margin bridge
  action = cap at Stage2 and decay if no follow-through evidence
```

## 19. Before / After Backtest Comparison

| Profile | Scope | Hypothesis | Eligible triggers | Avg MFE90 | Avg MAE90 | Avg MFE180 | Avg MAE180 | FP rate | Alignment |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current default proxy | none | 4 | 192.88% | -14.28% | 254.65% | -22.15% | 50% | mixed: good for launch monetization, weak for visibility-only IP |
| P0b e2r_2_0_baseline_reference | rollback reference | none | 4 | 192.88% | -14.28% | 254.65% | -22.15% | 50% | too permissive on visibility-only IP |
| P1 L8_content_ip_sector_shadow_profile | sector-specific monetization gate | require monetization bridge; decay trailer-only | 3 | 255.1% | -10.64% | 317.82% | -15.51% | 33% | improves false positive rate with limited coverage |
| P2 C27_content_ip_monetization_shadow_profile | canonical owned/publisher IP gate | launch/revenue rank/contract economics required for Green | 2 | 351.07% | -9.56% | 445.66% | -9.56% | 0% | best score-return alignment; rejects trailer/global-hit without financial bridge |
| P3 C27_counterexample_guard_profile | guard profile | price-only local 4B and visibility-only demotion | 2 | 34.68% | -19.0% | 34.68% | -34.74% | 100% | counterexample guard; not a long-entry profile |

## 20. Score-Return Alignment Matrix

| Case | Before score/stage | After score/stage | MFE90 | MAE90 | Alignment verdict |
|---|---|---|---:|---:|---|
| R8L75_C27_194480_COOKIE_RUN_KINGDOM_LAUNCH | 84 / Stage3-Yellow | 88 / Stage3-Green | 618.75% | -18.08% | improved |
| R8L75_C27_293490_ODIN_LAUNCH | 82 / Stage3-Yellow | 87.5 / Stage3-Green | 83.39% | -1.04% | improved |
| R8L75_C27_263750_DOKEV_TRAILER | 78 / Stage3-Yellow | 69 / Stage2-Actionable | 63.15% | -12.81% | guarded |
| R8L75_C27_253450_THE_GLORY_HIT | 76 / Stage3-Yellow | 68 / Stage2-Actionable | 6.21% | -25.18% | guarded |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE | 2 | 2 | 1 | 1 | 4 | 0 | 5 | 4 | 2 | true | true | C27 still needs non-game streaming economics cases and software/IP retention cases |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - visibility_only_false_positive
  - green_lateness_on_revenue_rank_conversion
  - price_only_local_4B_too_early
new_axis_proposed:
  - C27_partner_or_owned_ip_monetization_gate
  - C27_trailer_hype_decay_guard
  - C27_green_requires_financial_bridge
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Actual Songdaiki/stock-web tradable_raw 1D OHLC rows.
- Entry-date close, peak high, MFE/MAE, drawdown after peak.
- C27 content/game IP monetization vs visibility-only residual classification.
- Shadow-only sector/canonical rule proposal.
```

Non-validation scope:

```text
- No current/live candidate scan.
- No investment recommendation.
- No stock_agent code inspection.
- No production scoring patch.
- No broker/API/autotrading work.
- No adjustment for corporate actions beyond stock-web profile caveat blocking.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_partner_or_owned_ip_monetization_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Promote only when content/game IP event has monetization bridge: launch/revenue rank/contract economics/revision path.","Selected positives keep high MFE while trailer/global-hit false positives are demoted.",R8L75_T01_194480_STAGE2_ACTIONABLE_20210121|R8L75_T02_293490_STAGE2_ACTIONABLE_20210629|R8L75_T03_263750_STAGE2_TRAILER_20210825|R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_trailer_hype_decay_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Trailer-only or global attention without revenue timing must decay before Stage3-Green.","Pearl Abyss and Studio Dragon reduce false positive Green pressure.",R8L75_T03_263750_STAGE2_TRAILER_20210825|R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230,2,2,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,C27_green_requires_financial_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Stage3-Green should require margin/revision/financial visibility, not title awareness alone.","Kakao Games Green lateness improves when revenue-rank conversion is accepted; Studio Dragon false positive is blocked.",R8L75_T02_293490_STAGE2_ACTIONABLE_20210629|R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230,2,2,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type":"case","case_id":"R8L75_C27_194480_COOKIE_RUN_KINGDOM_LAUNCH","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L75_T01_194480_STAGE2_ACTIONABLE_20210121","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Owned-IP launch with app-store monetization evidence deserves Stage3 promotion only after monetization/revision confirmation."}
{"row_type":"case","case_id":"R8L75_C27_293490_ODIN_LAUNCH","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L75_T02_293490_STAGE2_ACTIONABLE_20210629","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Revenue-rank conversion and publisher economics reduce Green lateness compared with waiting for later financial prints."}
{"row_type":"case","case_id":"R8L75_C27_263750_DOKEV_TRAILER","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R8L75_T03_263750_STAGE2_TRAILER_20210825","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_to_visibility_only_scoring","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Trailer-only visibility should decay unless launch-date, preorder, revenue-rank, or platform-contract evidence appears."}
{"row_type":"case","case_id":"R8L75_C27_253450_THE_GLORY_HIT","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_to_visibility_only_scoring","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Streaming-hit visibility is not enough; platform contract economics and margin bridge are required for Green."}
```

### trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R8L75_T01_194480_STAGE2_ACTIONABLE_20210121","case_id":"R8L75_C27_194480_COOKIE_RUN_KINGDOM_LAUNCH","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","sector":"게임·모바일 IP","primary_archetype":"mobile_game_ip_global_monetization","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-21","evidence_available_at_that_date":"Cookie Run: Kingdom release / early app-store monetization signal; same IP, publisher-owned global mobile game.","evidence_source":"Public release date sources; Devsisters/Cookie Run public release history.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-22","entry_price":22400,"MFE_30D_pct":208.04,"MFE_90D_pct":618.75,"MFE_180D_pct":790.62,"MFE_1Y_pct":790.62,"MFE_2Y_pct":790.62,"MAE_30D_pct":-18.08,"MAE_90D_pct":-18.08,"MAE_180D_pct":-18.08,"MAE_1Y_pct":-18.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-73.43,"green_lateness_ratio":0.443,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4B_row","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_mfe_high_later_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L75_C27_194480_COOKIE_RUN_KINGDOM_LAUNCH_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L75_T02_293490_STAGE2_ACTIONABLE_20210629","case_id":"R8L75_C27_293490_ODIN_LAUNCH","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","sector":"게임·퍼블리싱 IP","primary_archetype":"new_title_revenue_rank_monetization","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2021-06-29","evidence_available_at_that_date":"Odin: Valhalla Rising domestic launch / top-grossing transition signal; publisher economics visible via Kakao Games and Lionheart route.","evidence_source":"Public launch-date and game-release sources; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-06-30","entry_price":57800,"MFE_30D_pct":83.39,"MFE_90D_pct":83.39,"MFE_180D_pct":100.69,"MFE_1Y_pct":100.69,"MFE_2Y_pct":100.69,"MAE_30D_pct":-1.04,"MAE_90D_pct":-1.04,"MAE_180D_pct":-1.04,"MAE_1Y_pct":-1.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":116000,"drawdown_after_peak_pct":-86.46,"green_lateness_ratio":0.729,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_4B_row","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_but_green_late","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L75_C27_293490_ODIN_LAUNCH_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L75_T03_263750_STAGE2_TRAILER_20210825","case_id":"R8L75_C27_263750_DOKEV_TRAILER","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","sector":"게임·트레일러 IP","primary_archetype":"trailer_hype_without_monetization_window","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2021-08-25","evidence_available_at_that_date":"DokeV gameplay trailer at Gamescom/Opening Night Live generated visibility, but the event was not a revenue launch and monetization timing remained unconfirmed.","evidence_source":"Gamescom/DokeV public trailer source; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-27","entry_price":89000,"MFE_30D_pct":14.61,"MFE_90D_pct":63.15,"MFE_180D_pct":63.15,"MFE_1Y_pct":63.15,"MFE_2Y_pct":63.15,"MAE_30D_pct":-12.81,"MAE_90D_pct":-12.81,"MAE_180D_pct":-27.42,"MAE_1Y_pct":-58.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-74.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.231,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_structural_rerating_after_trailer_hype","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L75_C27_263750_DOKEV_TRAILER_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230","case_id":"R8L75_C27_253450_THE_GLORY_HIT","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","sector":"드라마·스트리밍 IP","primary_archetype":"global_streaming_hit_without_margin_bridge","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2022-12-30","evidence_available_at_that_date":"The Glory Part 1 Netflix release and global attention; strong title visibility but no direct margin/retention bridge at the entry date.","evidence_source":"Netflix/The Glory public release and global top-10 sources; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-02","entry_price":83800,"MFE_30D_pct":6.21,"MFE_90D_pct":6.21,"MFE_180D_pct":6.21,"MFE_1Y_pct":6.21,"MFE_2Y_pct":6.21,"MAE_30D_pct":-6.92,"MAE_90D_pct":-25.18,"MAE_180D_pct":-42.06,"MAE_1Y_pct":-45.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-01-02","peak_price":89000,"drawdown_after_peak_pct":-48.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"no_full_4B_without_margin_evidence","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"hard_4c_late_if_margin_disappointment_ignored","trigger_outcome_label":"false_positive_global_hit_without_financial_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L75_C27_253450_THE_GLORY_HIT_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L75_T03B_263750_PRICE_ONLY_LOCAL_4B_20210830","case_id":"R8L75_C27_263750_DOKEV_TRAILER","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MOBILE_GAME_AND_STREAMING_CONTENT_IP_MONETIZATION_VS_TRAILER_HYPE","sector":"게임·트레일러 IP","primary_archetype":"trailer_hype_without_monetization_window","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill","trigger_type":"4B-overlay","trigger_date":"2021-08-30","evidence_available_at_that_date":"First post-trailer local price high without launch/revenue evidence.","evidence_source":"Gamescom/DokeV public trailer source; stock-web OHLC rows.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-30","entry_price":102000,"MFE_30D_pct":-1.86,"MFE_90D_pct":42.35,"MFE_180D_pct":42.35,"MFE_1Y_pct":42.35,"MFE_2Y_pct":42.35,"MAE_30D_pct":-23.92,"MAE_90D_pct":-23.92,"MAE_180D_pct":-36.67,"MAE_1Y_pct":-63.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-74.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.231,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_structural_rerating_after_trailer_hype","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L75_C27_263750_DOKEV_TRAILER_ENTRY","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L75_C27_194480_COOKIE_RUN_KINGDOM_LAUNCH","trigger_id":"R8L75_T01_194480_STAGE2_ACTIONABLE_20210121","symbol":"194480","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":16,"relative_strength_score":20,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":16,"relative_strength_score":20,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Current proxy stress-test row; no production scoring change.","MFE_90D_pct":618.75,"MAE_90D_pct":-18.08,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C27_content_ip_monetization_shadow_profile","case_id":"R8L75_C27_194480_COOKIE_RUN_KINGDOM_LAUNCH","trigger_id":"R8L75_T01_194480_STAGE2_ACTIONABLE_20210121","symbol":"194480","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":16,"relative_strength_score":20,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Owned-IP launch with app-store monetization evidence deserves Stage3 promotion only after monetization/revision confirmation.","MFE_90D_pct":618.75,"MAE_90D_pct":-18.08,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L75_C27_293490_ODIN_LAUNCH","trigger_id":"R8L75_T02_293490_STAGE2_ACTIONABLE_20210629","symbol":"293490","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":14,"relative_strength_score":18,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":14,"relative_strength_score":18,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Current proxy stress-test row; no production scoring change.","MFE_90D_pct":83.39,"MAE_90D_pct":-1.04,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"C27_content_ip_monetization_shadow_profile","case_id":"R8L75_C27_293490_ODIN_LAUNCH","trigger_id":"R8L75_T02_293490_STAGE2_ACTIONABLE_20210629","symbol":"293490","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":14,"relative_strength_score":18,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":11,"revision_score":18,"relative_strength_score":19,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":87.5,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Revenue-rank conversion and publisher economics reduce Green lateness compared with waiting for later financial prints.","MFE_90D_pct":83.39,"MAE_90D_pct":-1.04,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L75_C27_263750_DOKEV_TRAILER","trigger_id":"R8L75_T03_263750_STAGE2_TRAILER_20210825","symbol":"263750","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":20,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":20,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Current proxy stress-test row; no production scoring change.","MFE_90D_pct":63.15,"MAE_90D_pct":-12.81,"score_return_alignment_label":"misaligned_current_false_positive","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"C27_content_ip_monetization_shadow_profile","case_id":"R8L75_C27_263750_DOKEV_TRAILER","trigger_id":"R8L75_T03_263750_STAGE2_TRAILER_20210825","symbol":"263750","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":20,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":18,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Trailer-only visibility should decay unless launch-date, preorder, revenue-rank, or platform-contract evidence appears.","MFE_90D_pct":63.15,"MAE_90D_pct":-12.81,"score_return_alignment_label":"guarded","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L75_C27_253450_THE_GLORY_HIT","trigger_id":"R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Current proxy stress-test row; no production scoring change.","MFE_90D_pct":6.21,"MAE_90D_pct":-25.18,"score_return_alignment_label":"misaligned_current_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C27_content_ip_monetization_shadow_profile","case_id":"R8L75_C27_253450_THE_GLORY_HIT","trigger_id":"R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":8,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":6,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Streaming-hit visibility is not enough; platform contract economics and margin bridge are required for Green.","MFE_90D_pct":6.21,"MAE_90D_pct":-25.18,"score_return_alignment_label":"guarded","current_profile_verdict":"current_profile_false_positive"}
```

### shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_partner_or_owned_ip_monetization_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Promote only when content/game IP event has monetization bridge: launch/revenue rank/contract economics/revision path.","Selected positives keep high MFE while trailer/global-hit false positives are demoted.",R8L75_T01_194480_STAGE2_ACTIONABLE_20210121|R8L75_T02_293490_STAGE2_ACTIONABLE_20210629|R8L75_T03_263750_STAGE2_TRAILER_20210825|R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C27_trailer_hype_decay_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Trailer-only or global attention without revenue timing must decay before Stage3-Green.","Pearl Abyss and Studio Dragon reduce false positive Green pressure.",R8L75_T03_263750_STAGE2_TRAILER_20210825|R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230,2,2,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,C27_green_requires_financial_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Stage3-Green should require margin/revision/financial visibility, not title awareness alone.","Kakao Games Green lateness improves when revenue-rank conversion is accepted; Studio Dragon false positive is blocked.",R8L75_T02_293490_STAGE2_ACTIONABLE_20210629|R8L75_T04_253450_STAGE2_GLOBAL_HIT_20221230,2,2,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["visibility_only_false_positive","green_lateness_on_revenue_rank_conversion","price_only_local_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 75
next_round = R9
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Price-source files directly checked:

```text
Songdaiki/stock-web atlas/manifest.json
Songdaiki/stock-web atlas/schema.json
Songdaiki/stock-web atlas/symbol_profiles/194/194480.json
Songdaiki/stock-web atlas/symbol_profiles/293/293490.json
Songdaiki/stock-web atlas/symbol_profiles/263/263750.json
Songdaiki/stock-web atlas/symbol_profiles/253/253450.json
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/194/194480/2022.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv
```

Event-source notes used only for historical trigger dating:

```text
Cookie Run: Kingdom public release date and Devsisters release history.
Kakao Games / Odin: Valhalla Rising public launch history.
DokeV gameplay trailer world premiere at Gamescom Opening Night Live, 2021-08-25.
The Glory Netflix Part 1 release date, 2022-12-30, and Studio Dragon production link.
```

