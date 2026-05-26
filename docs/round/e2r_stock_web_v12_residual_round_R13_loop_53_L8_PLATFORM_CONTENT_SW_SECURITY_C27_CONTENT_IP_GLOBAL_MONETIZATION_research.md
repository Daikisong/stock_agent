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
- round: `R13`
- loop: `53`
- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C27_CONTENT_IP_GLOBAL_MONETIZATION`
- fine_archetype_id: `K_GAME_IP_GLOBAL_LAUNCH_TO_RECURRING_MONETIZATION_AND_TOKENIZED_IP_4B_GUARD`
- loop_objective: `auto_coverage_gap_fill, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test, stage2_actionable_bonus_stress_test`
- investment recommendation language: intentionally excluded.
- live scan: not performed.
- brokerage API / auto-trading: not touched.
- stock_agent code: not opened.

This file is historical calibration research only. It is not a live watchlist, investment recommendation, or repository patch.
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
This loop does not re-propose the existing global axes. It stress-tests the C27 residual where **a content/IP event looks large, but the market later asks whether the IP is recurring, owned, margin-accretive, and legally durable**. A game IP is a forge: if the launch heat becomes repeat revenue, the metal holds; if it is only a spark, the price cools before the score should turn Green.
## 2. Round / Large Sector / Canonical Archetype Scope
| Field | Value |
|---|---|
| large_sector_id | `L8_PLATFORM_CONTENT_SW_SECURITY` |
| canonical_archetype_id | `C27_CONTENT_IP_GLOBAL_MONETIZATION` |
| fine_archetype_id | `K_GAME_IP_GLOBAL_LAUNCH_TO_RECURRING_MONETIZATION_AND_TOKENIZED_IP_4B_GUARD` |
| sector | 플랫폼·콘텐츠·SW·보안 |
| primary_archetype | Content/IP global monetization with game-IP retention conversion |
| excluded adjacent archetypes | C26 platform ad revenue; C28 software/security contracts |

Compression thesis: C27 should promote **owned IP + global distribution + repeat monetization / retention / earnings bridge**. It should discount **single premium-title launches**, **tokenized event-premium loops**, and **existing-IP extensions that lack durable rank or revision conversion**.
## 3. Previous Coverage / Duplicate Avoidance Check
Allowed research artifacts or already generated local research MDs were used only for coverage and duplicate avoidance. No production code was opened.

Observed C27 prior coverage in local artifact set:

- R8 loop 11: JYP, SM, YG, Studio Dragon, HYBE.
- R13 loop 35: 콘텐트리중앙, NEW, Studio Dragon, KakaoGames.
- R13 loop 38: 버킷스튜디오, 래몽래인/아티스트스튜디오, 에이스토리, 디앤씨미디어.

Repeated symbols excluded for this loop: `035900`, `041510`, `122870`, `253450`, `352820`, `036420`, `160550`, `293490`, `066410`, `200350`, `241840`, `263720`.

Auto-selected coverage gap:

```text
auto_selected_coverage_gap = Prior C27 coverage was concentrated in music labels, drama/webtoon production, and KakaoGames. It lacked a game-IP focused loop separating mobile/live-service retention success, tokenized-IP blowoff, premium-title sell-the-news, and existing-IP global extension failure.
```

Novelty classification:

```text
required_new_independent_case_ratio = 0.60
calibration_usable_case_count = 5
new_independent_case_count = 5
new_independent_case_ratio = 1.00
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
loop_contribution_label = canonical_archetype_rule_candidate
```
## 4. Stock-Web OHLC Input / Price Source Validation
| Field | Value |
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
| markets | `['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| schema_path | `atlas/schema.json` |
| universe_path | `atlas/universe/all_symbols.csv` |

Price source status: usable for historical calibration. The atlas is raw/unadjusted. Corporate-action-contaminated windows are blocked by default; this loop uses trigger windows that do not overlap the listed corporate-action candidate dates for each case.
## 5. Historical Eligibility Gate
| Symbol | Company | Profile first-last | Trading days | Corporate-action candidate dates | 180D calibration status |
|---|---:|---:|---:|---|---|
| `194480` | 데브시스터즈 | 2014-10-06 ~ 2026-02-20 | 2793 | none | clean_180D_window_for_selected_trigger |
| `112040` | 위메이드 | 2009-12-18 ~ 2026-02-20 | 3965 | 2012-05-23, 2012-06-14, 2021-09-13, 2021-10-06 | clean_180D_window_for_selected_trigger |
| `063080` | 컴투스홀딩스 | 2009-07-30 ~ 2026-02-20 | 4080 | none | clean_180D_window_for_selected_trigger |
| `095660` | 네오위즈 | 2007-07-02 ~ 2026-02-20 | 4595 | 2007-11-09, 2007-12-05, 2009-06-16, 2009-07-14 | clean_180D_window_for_selected_trigger |
| `078340` | 컴투스 | 2007-07-06 ~ 2026-02-20 | 4591 | 2007-07-18 | clean_180D_window_for_selected_trigger |

All representative triggers are historical, have stock-web tradable entry rows, have at least 180 forward trading days available before the manifest max date `2026-02-20`, and have high/low/close/volume fields.
## 6. Canonical Archetype Compression Map
| fine_archetype_id | canonical_archetype_id | Compression reason |
|---|---|---|
| `MOBILE_GAME_IP_GLOBAL_LAUNCH_RETENTION_RERATING` | `C27_CONTENT_IP_GLOBAL_MONETIZATION` | Cookie Run: Kingdom launched globally and very quickly converted a known CookieRun IP into mobile RPG revenue rank momentum; the key difference was IP ownership plus in-app monetization, not a one-off licensing headline. |
| `TOKENIZED_GAME_IP_GLOBAL_P2E_4B_GUARD` | `C27_CONTENT_IP_GLOBAL_MONETIZATION` | MIR4/WEMIX turned an owned MMORPG IP into a global tokenized play-to-earn narrative; price accepted the thesis fast, but token/regulatory/platform risk made non-price 4B gating essential. |
| `GROUP_GAME_TOKEN_PLATFORM_OPTIONALITY_4B_COUNTEREXAMPLE` | `C27_CONTENT_IP_GLOBAL_MONETIZATION` | The renamed Gamevil/Com2uS Holdings cycle was driven by token-platform/P2E optionality around group IP rather than clearly proven repeat revenue conversion; it produced a large MFE but an even more important 4B/4C calibration case. |
| `SINGLE_PREMIUM_GAME_GLOBAL_LAUNCH_SELL_THE_NEWS_GUARD` | `C27_CONTENT_IP_GLOBAL_MONETIZATION` | Lies of P was a real global console/PC IP event, but one premium title launch did not immediately prove repeat revenue, live-ops retention, or durable margin bridge; post-launch price behaved like sell-the-news. |
| `EXISTING_GAME_IP_GLOBAL_EXTENSION_RETENTION_GUARD` | `C27_CONTENT_IP_GLOBAL_MONETIZATION` | Summoners War IP extension gave a credible global-launch hook, but the price path argues for discounting launches that do not quickly close into durable rank retention and earnings revision. |

## 7. Case Selection Summary
| Case | Symbol | Company | Role | Positive / counterexample | Trigger family | Current profile verdict |
|---|---:|---|---|---|---|---|
| R13L53_C27_194480_DEV_COOKIE_RUN_KINGDOM_2021_GLOBAL_IP_SUCCESS | `194480` | 데브시스터즈 | structural_success | positive | global_mobile_ip_launch_to_retention | current_profile_too_late |
| R13L53_C27_112040_WEMADE_MIR4_WEMIX_2021_TOKENIZED_IP_SUCCESS_4B | `112040` | 위메이드 | 4B_overlay_success | positive | tokenized_ip_global_launch_to_4b_4c | current_profile_4B_too_late |
| R13L53_C27_063080_COM2US_HOLDINGS_2021_P2E_TOKEN_PLATFORM_BLOWOFF | `063080` | 컴투스홀딩스 | 4B_overlay_success | counterexample | token_platform_event_premium_to_drawdown | current_profile_4B_too_late |
| R13L53_C27_095660_NEOWIZ_LIES_OF_P_LAUNCH_SELL_THE_NEWS | `095660` | 네오위즈 | failed_rerating | counterexample | premium_game_launch_to_sell_the_news | current_profile_false_positive |
| R13L53_C27_078340_COM2US_SUMMONERS_CHRONICLES_GLOBAL_EXTENSION_FAILED_RERATING | `078340` | 컴투스 | failed_rerating | counterexample | existing_ip_global_extension_without_repeat_rank | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
```text
positive_structural_success = 2
counterexample_or_failed_rerating = 3
4B_or_4C_case = 2
minimum_positive_case_count = 1 satisfied
minimum_counterexample_count = 1 satisfied
minimum_calibration_usable_case_count = 3 satisfied
```

Positive cases are not repeated C27 entertainment-label examples. The counterexamples are not merely failed prices; they identify specific missing bridges: repeat monetization, rank retention, legal durability, and post-launch revision.
## 9. Evidence Source Map
| Symbol | Trigger date | Stage2 evidence | Stage3 evidence | 4B / 4C evidence | Source note |
|---|---:|---|---|---|---|
| `194480` | 2021-01-21 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, financial_visibility, repeat_order_or_conversion, durable_customer_confirmation, low_red_team_risk | valuation_blowoff, positioning_overheat | Cookie Run: Kingdom launched globally and very quickly converted a known CookieRun IP into mobile RPG revenue rank momentum; the key difference was IP ownership plus in-app monetization, not a one-off licensing headline. |
| `112040` | 2021-10-14 | public_event_or_disclosure, customer_or_order_quality, relative_strength, policy_or_regulatory_optionality, early_revision_signal | multiple_public_sources, financial_visibility, repeat_order_or_conversion | valuation_blowoff, positioning_overheat, legal_or_regulatory_block, explicit_event_cap, thesis_evidence_broken, regulatory_rejection | MIR4/WEMIX turned an owned MMORPG IP into a global tokenized play-to-earn narrative; price accepted the thesis fast, but token/regulatory/platform risk made non-price 4B gating essential. |
| `063080` | 2021-11-02 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | multiple_public_sources | valuation_blowoff, positioning_overheat, legal_or_regulatory_block, explicit_event_cap, thesis_evidence_broken, regulatory_rejection | The renamed Gamevil/Com2uS Holdings cycle was driven by token-platform/P2E optionality around group IP rather than clearly proven repeat revenue conversion; it produced a large MFE but an even more important 4B/4C calibration case. |
| `095660` | 2023-09-19 | public_event_or_disclosure, customer_or_order_quality, relative_strength | multiple_public_sources | explicit_event_cap, margin_or_backlog_slowdown, price_only_local_peak, thesis_evidence_broken | Lies of P was a real global console/PC IP event, but one premium title launch did not immediately prove repeat revenue, live-ops retention, or durable margin bridge; post-launch price behaved like sell-the-news. |
| `078340` | 2023-03-09 | public_event_or_disclosure, customer_or_order_quality | multiple_public_sources | margin_or_backlog_slowdown, explicit_event_cap, thesis_evidence_broken | Summoners War IP extension gave a credible global-launch hook, but the price path argues for discounting launches that do not quickly close into durable rank retention and earnings revision. |

## 10. Price Data Source Map
| Symbol | Entry date | Entry price | Price shard | Profile path | Stock-web manifest max date |
|---|---:|---:|---|---|---:|
| `194480` | 2021-01-21 | 17,250 | `atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv` | `atlas/symbol_profiles/194/194480.json` | 2026-02-20 |
| `112040` | 2021-10-14 | 117,200 | `atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv` | `atlas/symbol_profiles/112/112040.json` | 2026-02-20 |
| `063080` | 2021-11-02 | 88,200 | `atlas/ohlcv_tradable_by_symbol_year/063/063080/2021.csv` | `atlas/symbol_profiles/063/063080.json` | 2026-02-20 |
| `095660` | 2023-09-19 | 34,500 | `atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv` | `atlas/symbol_profiles/095/095660.json` | 2026-02-20 |
| `078340` | 2023-03-09 | 68,000 | `atlas/ohlcv_tradable_by_symbol_year/078/078340/2023.csv` | `atlas/symbol_profiles/078/078340.json` | 2026-02-20 |

## 11. Case-by-Case Trigger Grid
| Trigger | Symbol | Type | Trigger date | Entry date | Entry price | Stage2 fields | Stage3 fields | 4B fields | 4C fields |
|---|---:|---|---:|---:|---:|---|---|---|---|
| TRG_DEV_2021_COOKIE_RUN_STAGE2_2021_01_21 | `194480` | Stage2-Actionable | 2021-01-21 | 2021-01-21 | 17,250 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, financial_visibility, repeat_order_or_conversion, durable_customer_confirmation, low_red_team_risk | valuation_blowoff, positioning_overheat | none |
| TRG_WEMADE_2021_MIR4_WEMIX_STAGE2_2021_10_14 | `112040` | Stage2-Actionable | 2021-10-14 | 2021-10-14 | 117,200 | public_event_or_disclosure, customer_or_order_quality, relative_strength, policy_or_regulatory_optionality, early_revision_signal | multiple_public_sources, financial_visibility, repeat_order_or_conversion | valuation_blowoff, positioning_overheat, legal_or_regulatory_block, explicit_event_cap | thesis_evidence_broken, regulatory_rejection |
| TRG_COM2USHOLDINGS_2021_P2E_TOKEN_4B_2021_11_02 | `063080` | Stage2-Actionable | 2021-11-02 | 2021-11-02 | 88,200 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | multiple_public_sources | valuation_blowoff, positioning_overheat, legal_or_regulatory_block, explicit_event_cap | thesis_evidence_broken, regulatory_rejection |
| TRG_NEOWIZ_2023_LIES_OF_P_LAUNCH_2023_09_19 | `095660` | Stage3-Yellow | 2023-09-19 | 2023-09-19 | 34,500 | public_event_or_disclosure, customer_or_order_quality, relative_strength | multiple_public_sources | explicit_event_cap, margin_or_backlog_slowdown, price_only_local_peak | thesis_evidence_broken |
| TRG_COM2US_2023_SUMMONERS_CHRONICLES_GLOBAL_2023_03_09 | `078340` | Stage2-Actionable | 2023-03-09 | 2023-03-09 | 68,000 | public_event_or_disclosure, customer_or_order_quality | multiple_public_sources | margin_or_backlog_slowdown, explicit_event_cap | thesis_evidence_broken |

## 12. Trigger-Level OHLC Backtest Tables
| Trigger | Entry | MFE 30D | MFE 90D | MFE 180D | MAE 30D | MAE 90D | MAE 180D | Peak date | Peak price | Drawdown after peak | Outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| TRG_DEV_2021_COOKIE_RUN_STAGE2_2021_01_21 | 17,250 | 300.0% | 833.33% | 1056.52% | -12.75% | -12.75% | -12.75% | 2021-09-27 | 199,500 | -56.79% | structural_success_with_high_retention_ip_repricing |
| TRG_WEMADE_2021_MIR4_WEMIX_STAGE2_2021_10_14 | 117,200 | 109.64% | 109.64% | 109.64% | -22.35% | -22.35% | -55.63% | 2021-11-22 | 245,700 | -78.84% | tokenized_ip_success_then_hard_4b_4c_drawdown |
| TRG_COM2USHOLDINGS_2021_P2E_TOKEN_4B_2021_11_02 | 88,200 | 126.53% | 173.81% | 173.81% | -15.19% | -15.19% | -47.05% | 2022-01-03 | 241,500 | -80.66% | token_platform_blowoff_not_durable_ip_monetization |
| TRG_NEOWIZ_2023_LIES_OF_P_LAUNCH_2023_09_19 | 34,500 | 3.04% | 3.04% | 3.04% | -32.32% | -32.32% | -44.64% | 2023-09-19 | 35,550 | -46.27% | single_global_launch_sold_down_without_repeat_revenue_bridge |
| TRG_COM2US_2023_SUMMONERS_CHRONICLES_GLOBAL_2023_03_09 | 68,000 | 17.21% | 17.21% | 17.21% | -4.26% | -18.38% | -41.18% | 2023-04-04 | 79,700 | -49.81% | global_ip_extension_without_recurring_rank_conversion |

Interpretation: The loop deliberately includes both massive MFE winners and hard drawdown cases. C27 is not merely a “price goes up when IP launches” archetype. The usable rule is more surgical: **owned IP plus repeat monetization is promotable; single-launch or tokenized-event premium requires a guard rail before Green.**
## 13. Current Calibrated Profile Stress Test
| Symbol | Current profile likely judgement | Actual MFE/MAE alignment | Verdict | Axis implication |
|---|---|---|---|---|
| `194480` | Stage3-Yellow / score 78 | MFE90 833.33%, MAE180 -12.75% | current_profile_too_late | Stage2 bonus useful; Green confirmation likely too late if retention/ranking evidence already present. |
| `112040` | Stage3-Yellow / score 85 | MFE90 109.64%, MAE180 -55.63% | current_profile_4B_too_late | Stage2 captured upside, but non-price 4B requirement must fire earlier on token/legal risk. |
| `063080` | Stage3-Yellow / score 82 | MFE90 173.81%, MAE180 -47.05% | current_profile_4B_too_late | Existing price-only blowoff guard is right; tokenized-IP evidence should block full positive Green. |
| `095660` | Stage3-Yellow / score 79 | MFE90 3.04%, MAE180 -44.64% | current_profile_false_positive | Yellow threshold is too permissive for one premium title without repeat monetization bridge. |
| `078340` | Stage2-Actionable / score 76 | MFE90 17.21%, MAE180 -41.18% | current_profile_false_positive | Stage2 bonus too generous when existing-IP global extension lacks retention/revision conversion. |

Required stress-test answers:

1. Current calibrated profile would catch the high-MFE game-IP cycles, but it still confuses some launch events with durable rerating.
2. MFE/MAE alignment is correct for Devsisters, mixed for Wemade, and poor for Com2uS Holdings / Neowiz / Com2uS unless 4B and launch guards are active.
3. Stage2 bonus is useful for owned IP + retention but too generous for single-title event launches.
4. Yellow 75 is too low for C27 when evidence is only launch/review/news without repeat revenue or rank retention.
5. Green 87 / revision 55 is directionally right, but C27 needs retention/rank monetization as a substitute bridge before full financial revision arrives.
6. price-only blowoff guard remains correct.
7. full 4B non-price requirement is strengthened: token/legal/platform risk and sell-the-news launch caps are non-price evidence.
8. hard 4C routing should activate when token listing/regulatory trust or game revenue retention breaks, not after the full drawdown is already visible.
## 14. Stage2 / Yellow / Green Comparison
| Symbol | Stage2 signal | Yellow/Green issue | Green lateness ratio | Comment |
|---|---|---|---:|---|
| `194480` | Stage2-Actionable | Stage3-Yellow → Stage3-Green-shadow | not_applicable | Stage2-Actionable worked because the IP was owned and repeat mobile monetization became visible before formal annual revision. |
| `112040` | Stage2-Actionable | Stage3-Yellow → Stage3-Yellow-with-4B-watch | not_applicable | Stage2 worked, but the later 4B overlay mattered more than Green label purity. |
| `063080` | Stage2-Actionable | Stage3-Yellow → Stage2-watch-with-4B-overlay | not_applicable | Yellow-like promotion would be dangerous without tokenized-IP 4B guard. |
| `095660` | Stage3-Yellow | Stage3-Yellow → Stage2-watch-only | not_applicable | Yellow based on a premium title launch was not enough; outcome was sell-the-news. |
| `078340` | Stage2-Actionable | Stage2-Actionable → Stage2-watch-only | not_applicable | Existing IP global extension needed rank/retention proof before promotion. |

No separate Stage3-Green row was used for aggregate because the loop’s purpose is not to prove Green lateness again. It identifies C27-specific evidence that should decide whether Yellow is upgraded, held, or overlaid with 4B.
## 15. 4B Local vs Full-window Timing Audit
| Symbol | 4B evidence type | Local peak proximity | Full-window peak proximity | Timing verdict |
|---|---|---:|---:|---|
| `194480` | valuation_blowoff|positioning_overheat | None | None | not_applicable |
| `112040` | valuation_blowoff|positioning_overheat|legal_or_regulatory_block | 0.94 | 0.94 | good_full_window_4B_timing |
| `063080` | valuation_blowoff|positioning_overheat|legal_or_regulatory_block | 0.88 | 0.88 | good_full_window_4B_timing |
| `095660` | explicit_event_cap|margin_or_backlog_slowdown | 1.0 | 1.0 | good_full_window_4B_timing |
| `078340` | explicit_event_cap|margin_or_backlog_slowdown | 1.0 | 1.0 | good_full_window_4B_timing |

C27 needs two 4B gates. A normal IP launch can have price-only local peaks; that alone should not end a thesis. Tokenized IP, legal/regulatory dependence, or a known single-launch event cap is different: it is a non-price 4B overlay because the business proof can vanish even while price is still strong.
## 16. 4C Protection Audit
| Symbol | 4C label | Approximate protection logic | Verdict |
|---|---|---|---|
| `112040` | hard_4c_success | Token/legal thesis risk was visible before the full 78% peak-to-trough drawdown. | Current profile too late without tokenized-IP thesis-break routing. |
| `063080` | hard_4c_success | Token-platform premium collapsed into a >80% peak-to-trough move. | 4C should be available once token/platform proof fails, not only after price collapse. |
| `095660` | thesis_break_watch_only | Premium game launch did not become recurring earnings bridge. | Watch-only or Stage2 downgrade is preferred. |
| `078340` | thesis_break_watch_only | Global extension did not preserve rank/revision strength. | Watch-only or Stage2 downgrade is preferred. |
| `194480` | not_applicable | Structural success, but later valuation drawdown belongs to 4B rather than thesis break. | 4B overlay, not 4C. |
## 17. Sector-Specific Rule Candidate
```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
axis = l8_content_ip_repeat_monetization_required_for_green
shadow_delta = +2 for owned IP + repeat monetization / retention evidence
shadow_delta = -4 to -8 for single-launch or tokenized-event premium without repeat revenue bridge
proposal_type = sector_shadow_only
```

Rule candidate: In L8, an IP event should not be treated like a contract backlog. Content monetization is more like a fire that needs fuel: launch heat must be fed by retention, repeat revenue, margin bridge, or measurable global distribution conversion. Without that fuel, the signal is an event cap rather than a rerating engine.
## 18. Canonical-Archetype Rule Candidate
```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
new_axis_proposed = c27_game_ip_retention_monetization_bridge
new_axis_proposed = c27_single_launch_sell_the_news_guard
new_axis_proposed = c27_tokenized_ip_4b_overlay_guard
new_axis_proposed = c27_global_launch_without_repeat_revenue_discount
```

Promotion path: `owned IP + global launch + repeat monetization/rank retention + margin/revision bridge` may receive Stage2/Yellow support before full reported earnings. Guard path: `single premium-title launch`, `tokenized/P2E platform option`, or `existing IP extension without retention proof` should be capped below Green or converted into a 4B/4C watch.
## 19. Before / After Backtest Comparison
| Profile | Scope | Eligible triggers | Avg MFE90 | Avg MAE90 | Avg MFE180 | Avg MAE180 | False positive rate | Verdict |
|---|---|---:|---:|---:|---:|---:|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | 5 | 227.99% | -20.8% | 230.44% | -40.25% | 3/5 | mixed; strong MFE but poor drawdown discrimination |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 5 | 227.99% | -20.8% | 230.44% | -40.25% | 4/5 | worse; token and launch narratives overfit |
| P1_sector_specific_candidate_profile | L8 sector_specific | 5 | 227.99% | -20.8% | 230.44% | -40.25% | 1/5 | improves false-positive control and keeps Devsisters early |
| P2_canonical_archetype_candidate_profile | C27 canonical_archetype_specific | 5 | 227.99% | -20.8% | 230.44% | -40.25% | 1/5 | best explanatory compression for this loop |
| P3_counterexample_guard_profile | counterexample_guard | 3 | 64.16% | -21.96% | 64.16% | -43.02% | 0/3 after guard | strong guard profile |

## 20. Score-Return Alignment Matrix
| Symbol | Before score / label | After score / label | MFE90 | MAE90 | Alignment |
|---|---|---|---:|---:|---|
| `194480` | 78 / Stage3-Yellow | 88 / Stage3-Green-shadow | 833.33% | -12.75% | strong_positive_alignment |
| `112040` | 85 / Stage3-Yellow | 79 / Stage3-Yellow-with-4B-watch | 109.64% | -22.35% | positive_entry_but_4b_required |
| `063080` | 82 / Stage3-Yellow | 66 / Stage2-watch-with-4B-overlay | 173.81% | -15.19% | mfe_positive_but_guard_needed |
| `095660` | 79 / Stage3-Yellow | 63 / Stage2-watch-only | 3.04% | -32.32% | false_positive_reduced |
| `078340` | 76 / Stage2-Actionable | 68 / Stage2-watch-only | 17.21% | -18.38% | false_positive_reduced |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | K_GAME_IP_GLOBAL_LAUNCH_TO_RECURRING_MONETIZATION_AND_TOKENIZED_IP_4B_GUARD | 2 | 3 | 3 | 2 | 5 | 0 | 5 | 5 | 5 | true | true | C27 now has game-IP coverage across retention success, tokenized 4B/4C, premium-title sell-the-news, and existing-IP extension failure. |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: single_launch_false_positive, tokenized_ip_4b_too_late, global_launch_without_retention_bridge, premium_title_sell_the_news
new_axis_proposed: c27_game_ip_retention_monetization_bridge, c27_single_launch_sell_the_news_guard, c27_tokenized_ip_4b_overlay_guard, c27_global_launch_without_repeat_revenue_discount
existing_axis_strengthened: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: avg=24.8; same_archetype_new_symbol_count=5; repeated_same_symbol_penalty=0; repeated_same_trigger_date_penalty=0; schema_rematerialization_penalty=0
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: Prior C27 coverage lacked game-IP / tokenized-IP / premium-launch residual split.
loop_contribution_label: canonical_archetype_rule_candidate
```
## 23. Validation Scope / Non-Validation Scope
Validated scope:

- Stock-web manifest and price basis.
- Symbol profile availability and selected corporate-action caveats.
- Entry-date close, forward high/low, MFE/MAE, peak date, and peak-to-trough drawdown from stock-web tradable rows.
- C27-specific residual rule proposal as shadow-only research.

Non-validation scope:

- No live candidate discovery.
- No present-day investment conclusion.
- No stock_agent source-code inspection or patch.
- No production scoring change.
- No brokerage, auto-trading, or current watchlist language.
## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_game_ip_retention_monetization_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+2,Owned IP plus repeat monetization/rank retention separated Devsisters from launch-only cases.,Keeps structural success while reducing false positives.,TRG_DEV_2021_COOKIE_RUN_STAGE2_2021_01_21,5,5,3,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c27_single_launch_sell_the_news_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,-6,Premium title launch alone did not convert to rerating for Neowiz.,Reduces false positive Stage3-Yellow/Green.,TRG_NEOWIZ_2023_LIES_OF_P_LAUNCH_2023_09_19,5,5,3,medium,archetype_shadow_only,not production
shadow_weight,c27_tokenized_ip_4b_overlay_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,-8 risk overlay,Token/P2E legal and platform risk produced large drawdowns after high MFE.,Strengthens full_4b_requires_non_price_evidence and hard_4c routing.,TRG_WEMADE_2021_MIR4_WEMIX_STAGE2_2021_10_14|TRG_COM2USHOLDINGS_2021_P2E_TOKEN_4B_2021_11_02,5,5,3,medium,archetype_shadow_only,not production
shadow_weight,c27_global_launch_without_repeat_revenue_discount,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,-4,Global launch / existing IP extension without retention or revision bridge underperformed.,Reduces Com2uS false positive.,TRG_COM2US_2023_SUMMONERS_CHRONICLES_GLOBAL_2023_03_09,5,5,3,low_to_medium,archetype_shadow_only,not production
```
## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```
### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R13L53_C27_194480_DEV_COOKIE_RUN_KINGDOM_2021_GLOBAL_IP_SUCCESS", "symbol": "194480", "company_name": "데브시스터즈", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "MOBILE_GAME_IP_GLOBAL_LAUNCH_RETENTION_RERATING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_DEV_2021_COOKIE_RUN_STAGE2_2021_01_21", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_alignment", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Cookie Run: Kingdom launched globally and very quickly converted a known CookieRun IP into mobile RPG revenue rank momentum; the key difference was IP ownership plus in-app monetization, not a one-off licensing headline."}
{"row_type": "case", "case_id": "R13L53_C27_112040_WEMADE_MIR4_WEMIX_2021_TOKENIZED_IP_SUCCESS_4B", "symbol": "112040", "company_name": "위메이드", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "TOKENIZED_GAME_IP_GLOBAL_P2E_4B_GUARD", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_WEMADE_2021_MIR4_WEMIX_STAGE2_2021_10_14", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_entry_but_4b_required", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "MIR4/WEMIX turned an owned MMORPG IP into a global tokenized play-to-earn narrative; price accepted the thesis fast, but token/regulatory/platform risk made non-price 4B gating essential."}
{"row_type": "case", "case_id": "R13L53_C27_063080_COM2US_HOLDINGS_2021_P2E_TOKEN_PLATFORM_BLOWOFF", "symbol": "063080", "company_name": "컴투스홀딩스", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GROUP_GAME_TOKEN_PLATFORM_OPTIONALITY_4B_COUNTEREXAMPLE", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_COM2USHOLDINGS_2021_P2E_TOKEN_4B_2021_11_02", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "mfe_positive_but_guard_needed", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "The renamed Gamevil/Com2uS Holdings cycle was driven by token-platform/P2E optionality around group IP rather than clearly proven repeat revenue conversion; it produced a large MFE but an even more important 4B/4C calibration case."}
{"row_type": "case", "case_id": "R13L53_C27_095660_NEOWIZ_LIES_OF_P_LAUNCH_SELL_THE_NEWS", "symbol": "095660", "company_name": "네오위즈", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "SINGLE_PREMIUM_GAME_GLOBAL_LAUNCH_SELL_THE_NEWS_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_NEOWIZ_2023_LIES_OF_P_LAUNCH_2023_09_19", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Lies of P was a real global console/PC IP event, but one premium title launch did not immediately prove repeat revenue, live-ops retention, or durable margin bridge; post-launch price behaved like sell-the-news."}
{"row_type": "case", "case_id": "R13L53_C27_078340_COM2US_SUMMONERS_CHRONICLES_GLOBAL_EXTENSION_FAILED_RERATING", "symbol": "078340", "company_name": "컴투스", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "EXISTING_GAME_IP_GLOBAL_EXTENSION_RETENTION_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_COM2US_2023_SUMMONERS_CHRONICLES_GLOBAL_2023_03_09", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Summoners War IP extension gave a credible global-launch hook, but the price path argues for discounting launches that do not quickly close into durable rank retention and earnings revision."}
```
### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "TRG_DEV_2021_COOKIE_RUN_STAGE2_2021_01_21", "case_id": "R13L53_C27_194480_DEV_COOKIE_RUN_KINGDOM_2021_GLOBAL_IP_SUCCESS", "symbol": "194480", "company_name": "데브시스터즈", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "MOBILE_GAME_IP_GLOBAL_LAUNCH_RETENTION_RERATING", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "Content/IP global monetization and game-IP retention conversion", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-21", "evidence_available_at_that_date": "Cookie Run: Kingdom launched globally and very quickly converted a known CookieRun IP into mobile RPG revenue rank momentum; the key difference was IP ownership plus in-app monetization, not a one-off licensing headline.", "evidence_source": "public historical launch/ranking/report evidence mapped to trigger date; price verified from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-01-21", "entry_price": 17250, "MFE_30D_pct": 300.0, "MFE_90D_pct": 833.33, "MFE_180D_pct": 1056.52, "MFE_1Y_pct": 1056.52, "MFE_2Y_pct": 1056.52, "MAE_30D_pct": -12.75, "MAE_90D_pct": -12.75, "MAE_180D_pct": -12.75, "MAE_1Y_pct": -56.79, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-09-27", "peak_price": 199500, "drawdown_after_peak_pct": -56.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "valuation_blowoff|positioning_overheat", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_high_retention_ip_repricing", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L53_C27_194480_DEV_COOKIE_RUN_KINGDOM_2021_GLOBAL_IP_SUCCESS::2021-01-21::17250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_WEMADE_2021_MIR4_WEMIX_STAGE2_2021_10_14", "case_id": "R13L53_C27_112040_WEMADE_MIR4_WEMIX_2021_TOKENIZED_IP_SUCCESS_4B", "symbol": "112040", "company_name": "위메이드", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "TOKENIZED_GAME_IP_GLOBAL_P2E_4B_GUARD", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "Content/IP global monetization and game-IP retention conversion", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-10-14", "evidence_available_at_that_date": "MIR4/WEMIX turned an owned MMORPG IP into a global tokenized play-to-earn narrative; price accepted the thesis fast, but token/regulatory/platform risk made non-price 4B gating essential.", "evidence_source": "public historical launch/ranking/report evidence mapped to trigger date; price verified from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken", "regulatory_rejection"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv", "profile_path": "atlas/symbol_profiles/112/112040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-10-14", "entry_price": 117200, "MFE_30D_pct": 109.64, "MFE_90D_pct": 109.64, "MFE_180D_pct": 109.64, "MFE_1Y_pct": 109.64, "MFE_2Y_pct": 109.64, "MAE_30D_pct": -22.35, "MAE_90D_pct": -22.35, "MAE_180D_pct": -55.63, "MAE_1Y_pct": -55.63, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-22", "peak_price": 245700, "drawdown_after_peak_pct": -78.84, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat|legal_or_regulatory_block", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "tokenized_ip_success_then_hard_4b_4c_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L53_C27_112040_WEMADE_MIR4_WEMIX_2021_TOKENIZED_IP_SUCCESS_4B::2021-10-14::117200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_COM2USHOLDINGS_2021_P2E_TOKEN_4B_2021_11_02", "case_id": "R13L53_C27_063080_COM2US_HOLDINGS_2021_P2E_TOKEN_PLATFORM_BLOWOFF", "symbol": "063080", "company_name": "컴투스홀딩스", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GROUP_GAME_TOKEN_PLATFORM_OPTIONALITY_4B_COUNTEREXAMPLE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "Content/IP global monetization and game-IP retention conversion", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-11-02", "evidence_available_at_that_date": "The renamed Gamevil/Com2uS Holdings cycle was driven by token-platform/P2E optionality around group IP rather than clearly proven repeat revenue conversion; it produced a large MFE but an even more important 4B/4C calibration case.", "evidence_source": "public historical launch/ranking/report evidence mapped to trigger date; price verified from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "legal_or_regulatory_block", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken", "regulatory_rejection"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/063/063080/2021.csv", "profile_path": "atlas/symbol_profiles/063/063080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-02", "entry_price": 88200, "MFE_30D_pct": 126.53, "MFE_90D_pct": 173.81, "MFE_180D_pct": 173.81, "MFE_1Y_pct": 173.81, "MFE_2Y_pct": 173.81, "MAE_30D_pct": -15.19, "MAE_90D_pct": -15.19, "MAE_180D_pct": -47.05, "MAE_1Y_pct": -47.05, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-01-03", "peak_price": 241500, "drawdown_after_peak_pct": -80.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "valuation_blowoff|positioning_overheat|legal_or_regulatory_block", "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "token_platform_blowoff_not_durable_ip_monetization", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L53_C27_063080_COM2US_HOLDINGS_2021_P2E_TOKEN_PLATFORM_BLOWOFF::2021-11-02::88200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_NEOWIZ_2023_LIES_OF_P_LAUNCH_2023_09_19", "case_id": "R13L53_C27_095660_NEOWIZ_LIES_OF_P_LAUNCH_SELL_THE_NEWS", "symbol": "095660", "company_name": "네오위즈", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "SINGLE_PREMIUM_GAME_GLOBAL_LAUNCH_SELL_THE_NEWS_GUARD", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "Content/IP global monetization and game-IP retention conversion", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-09-19", "evidence_available_at_that_date": "Lies of P was a real global console/PC IP event, but one premium title launch did not immediately prove repeat revenue, live-ops retention, or durable margin bridge; post-launch price behaved like sell-the-news.", "evidence_source": "public historical launch/ranking/report evidence mapped to trigger date; price verified from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["explicit_event_cap", "margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv", "profile_path": "atlas/symbol_profiles/095/095660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-19", "entry_price": 34500, "MFE_30D_pct": 3.04, "MFE_90D_pct": 3.04, "MFE_180D_pct": 3.04, "MFE_1Y_pct": 3.04, "MFE_2Y_pct": 3.04, "MAE_30D_pct": -32.32, "MAE_90D_pct": -32.32, "MAE_180D_pct": -44.64, "MAE_1Y_pct": -44.64, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-19", "peak_price": 35550, "drawdown_after_peak_pct": -46.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "explicit_event_cap|margin_or_backlog_slowdown", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "single_global_launch_sold_down_without_repeat_revenue_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L53_C27_095660_NEOWIZ_LIES_OF_P_LAUNCH_SELL_THE_NEWS::2023-09-19::34500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_COM2US_2023_SUMMONERS_CHRONICLES_GLOBAL_2023_03_09", "case_id": "R13L53_C27_078340_COM2US_SUMMONERS_CHRONICLES_GLOBAL_EXTENSION_FAILED_RERATING", "symbol": "078340", "company_name": "컴투스", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "EXISTING_GAME_IP_GLOBAL_EXTENSION_RETENTION_GUARD", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "Content/IP global monetization and game-IP retention conversion", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-09", "evidence_available_at_that_date": "Summoners War IP extension gave a credible global-launch hook, but the price path argues for discounting launches that do not quickly close into durable rank retention and earnings revision.", "evidence_source": "public historical launch/ranking/report evidence mapped to trigger date; price verified from Songdaiki/stock-web tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078340/2023.csv", "profile_path": "atlas/symbol_profiles/078/078340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-09", "entry_price": 68000, "MFE_30D_pct": 17.21, "MFE_90D_pct": 17.21, "MFE_180D_pct": 17.21, "MFE_1Y_pct": 17.21, "MFE_2Y_pct": 17.21, "MAE_30D_pct": -4.26, "MAE_90D_pct": -18.38, "MAE_180D_pct": -41.18, "MAE_1Y_pct": -41.18, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-04", "peak_price": 79700, "drawdown_after_peak_pct": -49.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": "explicit_event_cap|margin_or_backlog_slowdown", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "global_ip_extension_without_recurring_rank_conversion", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L53_C27_078340_COM2US_SUMMONERS_CHRONICLES_GLOBAL_EXTENSION_FAILED_RERATING::2023-03-09::68000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```
### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L53_C27_194480_DEV_COOKIE_RUN_KINGDOM_2021_GLOBAL_IP_SUCCESS", "trigger_id": "TRG_DEV_2021_COOKIE_RUN_STAGE2_2021_01_21", "symbol": "194480", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 15, "relative_strength_score": 24, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 18, "relative_strength_score": 24, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 17, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["ip_ownership_score", "retention_revenue_rank_score", "single_launch_sell_the_news_guard", "tokenized_ip_overheat_score"], "component_delta_explanation": "C27 shadow simulation separates owned IP + recurring retention conversion from single launch, tokenized event-premium, or platform narrative without earnings bridge.", "MFE_90D_pct": 833.33, "MAE_90D_pct": -12.75, "score_return_alignment_label": "strong_positive_alignment", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L53_C27_112040_WEMADE_MIR4_WEMIX_2021_TOKENIZED_IP_SUCCESS_4B", "trigger_id": "TRG_WEMADE_2021_MIR4_WEMIX_STAGE2_2021_10_14", "symbol": "112040", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 24, "customer_quality_score": 13, "policy_or_regulatory_score": 12, "valuation_repricing_score": 22, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 85, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 24, "customer_quality_score": 13, "policy_or_regulatory_score": 7, "valuation_repricing_score": 18, "execution_risk_score": -8, "legal_or_contract_risk_score": -8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow-with-4B-watch", "changed_components": ["ip_ownership_score", "retention_revenue_rank_score", "single_launch_sell_the_news_guard", "tokenized_ip_overheat_score"], "component_delta_explanation": "C27 shadow simulation separates owned IP + recurring retention conversion from single launch, tokenized event-premium, or platform narrative without earnings bridge.", "MFE_90D_pct": 109.64, "MAE_90D_pct": -22.35, "score_return_alignment_label": "positive_entry_but_4b_required", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L53_C27_063080_COM2US_HOLDINGS_2021_P2E_TOKEN_PLATFORM_BLOWOFF", "trigger_id": "TRG_COM2USHOLDINGS_2021_P2E_TOKEN_4B_2021_11_02", "symbol": "063080", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 23, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 24, "execution_risk_score": -5, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 23, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 12, "execution_risk_score": -12, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage2-watch-with-4B-overlay", "changed_components": ["ip_ownership_score", "retention_revenue_rank_score", "single_launch_sell_the_news_guard", "tokenized_ip_overheat_score"], "component_delta_explanation": "C27 shadow simulation separates owned IP + recurring retention conversion from single launch, tokenized event-premium, or platform narrative without earnings bridge.", "MFE_90D_pct": 173.81, "MAE_90D_pct": -15.19, "score_return_alignment_label": "mfe_positive_but_guard_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L53_C27_095660_NEOWIZ_LIES_OF_P_LAUNCH_SELL_THE_NEWS", "trigger_id": "TRG_NEOWIZ_2023_LIES_OF_P_LAUNCH_2023_09_19", "symbol": "095660", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 16, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-watch-only", "changed_components": ["ip_ownership_score", "retention_revenue_rank_score", "single_launch_sell_the_news_guard", "tokenized_ip_overheat_score"], "component_delta_explanation": "C27 shadow simulation separates owned IP + recurring retention conversion from single launch, tokenized event-premium, or platform narrative without earnings bridge.", "MFE_90D_pct": 3.04, "MAE_90D_pct": -32.32, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L53_C27_078340_COM2US_SUMMONERS_CHRONICLES_GLOBAL_EXTENSION_FAILED_RERATING", "trigger_id": "TRG_COM2US_2023_SUMMONERS_CHRONICLES_GLOBAL_2023_03_09", "symbol": "078340", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": -7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-watch-only", "changed_components": ["ip_ownership_score", "retention_revenue_rank_score", "single_launch_sell_the_news_guard", "tokenized_ip_overheat_score"], "component_delta_explanation": "C27 shadow simulation separates owned IP + recurring retention conversion from single launch, tokenized event-premium, or platform narrative without earnings bridge.", "MFE_90D_pct": 17.21, "MAE_90D_pct": -18.38, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive"}
```
### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_game_ip_retention_monetization_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+2,Owned IP plus repeat monetization/rank retention separated Devsisters from launch-only cases.,Keeps structural success while reducing false positives.,TRG_DEV_2021_COOKIE_RUN_STAGE2_2021_01_21,5,5,3,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c27_single_launch_sell_the_news_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,-6,Premium title launch alone did not convert to rerating for Neowiz.,Reduces false positive Stage3-Yellow/Green.,TRG_NEOWIZ_2023_LIES_OF_P_LAUNCH_2023_09_19,5,5,3,medium,archetype_shadow_only,not production
shadow_weight,c27_tokenized_ip_4b_overlay_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,-8 risk overlay,Token/P2E legal and platform risk produced large drawdowns after high MFE.,Strengthens full_4b_requires_non_price_evidence and hard_4c routing.,TRG_WEMADE_2021_MIR4_WEMIX_STAGE2_2021_10_14|TRG_COM2USHOLDINGS_2021_P2E_TOKEN_4B_2021_11_02,5,5,3,medium,archetype_shadow_only,not production
shadow_weight,c27_global_launch_without_repeat_revenue_discount,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,-4,Global launch / existing IP extension without retention or revision bridge underperformed.,Reduces Com2uS false positive.,TRG_COM2US_2023_SUMMONERS_CHRONICLES_GLOBAL_2023_03_09,5,5,3,low_to_medium,archetype_shadow_only,not production
```
### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "53", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_canonical_archetype_count": 0, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["single_launch_false_positive", "tokenized_ip_4b_too_late", "global_launch_without_retention_bridge", "premium_title_sell_the_news"], "new_axis_proposed": ["c27_game_ip_retention_monetization_bridge", "c27_single_launch_sell_the_news_guard", "c27_tokenized_ip_4b_overlay_guard", "c27_global_launch_without_repeat_revenue_discount"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "avg=24.8; repeated_same_symbol_penalty=0; repeated_same_trigger_date_penalty=0; schema_rematerialization_penalty=0", "auto_selected_coverage_gap": "Prior C27 coverage over-indexed on entertainment labels, drama/webtoon, and KakaoGames; this loop adds new game-IP / tokenized-IP / premium-launch / existing-IP-extension symbols."}
```
### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": null, "symbol": null, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "reason": "none_all_selected_cases_have_clean_180D_stock_web_window", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration_placeholder"}
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
next_round = R13_loop_54
next_large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
next_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
reason = complete L8 sweep by moving from platform/ads and content/IP into software/security contract retention; avoid repeating C27 game-IP cases.
```
## 28. Source Notes
Stock-web rows inspected for this loop include:

- `atlas/manifest.json` from Songdaiki/stock-web, generated 2026-05-21, max_date `2026-02-20`.
- `atlas/symbol_profiles/194/194480.json`, `112/112040.json`, `063/063080.json`, `095/095660.json`, `078/078340.json`.
- Representative tradable shards: `194/194480/2021.csv`, `112/112040/2021.csv`, `112/112040/2022.csv`, `063/063080/2021.csv`, `063/063080/2022.csv`, `095/095660/2023.csv`, `095/095660/2024.csv`, `078/078340/2023.csv`.

All price calculations use raw/unadjusted tradable rows. This MD does not use raw shards for calibration; raw shards are reserved for row-status diagnostics only.
