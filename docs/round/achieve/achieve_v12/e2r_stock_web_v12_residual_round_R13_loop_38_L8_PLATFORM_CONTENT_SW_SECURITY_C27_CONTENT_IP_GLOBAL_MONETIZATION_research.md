# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 38
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = K_DRAMA_WEBTOON_SINGLE_TITLE_TO_REPEATABLE_IP_MONETIZATION
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This file is historical calibration research only. It is not a current stock scan, not a live watchlist, and not an investment recommendation.

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

This loop does not re-propose those global axes. It stress-tests them inside C27 and proposes only shadow sector/canonical rules.

## 2. Round / Large Sector / Canonical Archetype Scope

- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C27_CONTENT_IP_GLOBAL_MONETIZATION`
- fine_archetype_id: `K_DRAMA_WEBTOON_SINGLE_TITLE_TO_REPEATABLE_IP_MONETIZATION`
- selected loop objectives: `holdout_validation | residual_false_positive_mining | residual_missed_structural_mining | yellow_threshold_stress_test | green_strictness_stress_test | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill`

C27 here means the market is not merely buying “content buzz.” It is trying to decide whether a title can become a monetization engine: rights ownership, platform customer quality, recurring slate, anime/game/webtoon extension, and post-hit margin bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for coverage and duplicate avoidance. The ingest summary indicates 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 representative rows across R1~R13. Existing C27 work already covered broad K-content/music/game cases such as Studio Dragon, Kakao Games, Contentree, NEW, JYP, HYBE, YG, SM and related guardrails. This loop therefore uses four new independent symbols in a narrower residual pocket:

```text
new_independent_case_ratio = 1.00
reused_case_count = 0
new_symbols = 241840 | 200350 | 263720 | 066410
novel residual pocket = single-title hit / webtoon-to-anime/game route / association-only false Green
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields confirmed for this loop:

| field | value |
|---|---:|
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
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema basis:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative rows satisfy the 180-trading-day forward-window check against `stock_web_manifest_max_date = 2026-02-20`. Corporate-action candidates were checked at profile level; none overlaps the representative 180D calibration windows used here.

|symbol|company_name|profile_path|corporate_action_window_status|profile_caveat|
|---|---|---|---|---|
|241840|에이스토리|atlas/symbol_profiles/241/241840.json|clean_180D_window|none|
|200350|래몽래인/아티스트스튜디오|atlas/symbol_profiles/200/200350.json|clean_180D_window|profile-level caveat exists but tested 180D window clean|
|263720|디앤씨미디어|atlas/symbol_profiles/263/263720.json|clean_180D_window|none|
|066410|버킷스튜디오|atlas/symbol_profiles/066/066410.json|clean_180D_window|profile-level caveat exists but tested 180D window clean|


## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| K_DRAMA_SINGLE_TITLE_GLOBAL_HIT_WITH_PRODUCTION_RIGHTS | C27_CONTENT_IP_GLOBAL_MONETIZATION | rights-owning drama producer with global platform route |
| K_DRAMA_RATINGS_HIT_SINGLE_TITLE_EVENT_CAP | C27_CONTENT_IP_GLOBAL_MONETIZATION | domestic ratings hit with high MFE but high MAE and event-cap risk |
| WEBTOON_IP_GLOBAL_ANIME_GAME_OPTIONALITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | webtoon/IP extension into anime/game; needs conversion evidence |
| ASSOCIATION_ONLY_CONTENT_THEME_FALSE_POSITIVE | C27_CONTENT_IP_GLOBAL_MONETIZATION | price-only association with no verified monetization bridge |

Compression rule: direct rights and repeatable monetization can promote Stage2/Yellow, but single-title event caps require fast 4B overlay, and association-only price action is blocked from Stage3-Green.

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|
|---|---|---|---|---|---|---|
|C27_241840_ASTORY_WOOYOUNGWOO_2022|241840|에이스토리|structural_success|positive|C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL|current_profile_too_late|
|C27_200350_RAEMONG_REBORN_RICH_2022|200350|래몽래인/아티스트스튜디오|high_mae_success|positive|C27_200350_20221121_S2_REBORN_RICH_RATINGS_ROUTE|current_profile_4B_too_late|
|C27_263720_DNC_SOLO_LEVELING_2024|263720|디앤씨미디어|stage2_promote_candidate|positive|C27_263720_20240108_S2_SOLO_LEVELING_ANIME_ROUTE|current_profile_too_early|
|C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021|066410|버킷스튜디오|false_positive_green|counterexample|C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN|current_profile_false_positive|


## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 3
counterexample_or_failed_rerating = 1
4B_or_4C_case_count = 7
minimum_calibration_usable_case_count = 4
new_independent_case_ratio = 1.00
```

The positive cases are intentionally not all “clean winners.” C27 is a furnace only when the title can keep producing heat. Without rights, repeatability, or customer/margin conversion, the same spark becomes a firework: bright, loud, and gone.

## 9. Evidence Source Map

| case_id | evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence | source type |
|---|---|---|---|---|---|
| C27_241840_ASTORY_WOOYOUNGWOO_2022 | Netflix/ENA drama hit | first broadcast, production company, Netflix availability, early ratings | Netflix global ranking / viewing-hour confirmation | single-title valuation/positioning cap | public historical web sources + stock-web OHLC |
| C27_200350_RAEMONG_REBORN_RICH_2022 | JTBC ratings hit | first broadcast and ratings ramp | multiple ratings reports | event cap and post-series fade | public historical web sources + stock-web OHLC |
| C27_263720_DNC_SOLO_LEVELING_2024 | webtoon→anime/game IP | anime broadcast and global IP route | multi-format optionality but monetization still episodic | anime/game release-week event cap | public historical web sources + stock-web OHLC |
| C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021 | association-only theme | relative strength only | no direct rights/margin bridge | price-only blowoff and reversal | public historical web sources + stock-web OHLC |

## 10. Price Data Source Map

|trigger_id|symbol|entry_date|entry_price|price_shard_path|profile_path|corporate_action_window_status|
|---|---|---|---|---|---|---|
|C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL|241840|2022-06-30|18000|atlas/ohlcv_tradable_by_symbol_year/241/241840/2022.csv|atlas/symbol_profiles/241/241840.json|clean_180D_window|
|C27_241840_20220713_GREEN_WOO_GLOBAL_RANKING_CONFIRMATION|241840|2022-07-13|32650|atlas/ohlcv_tradable_by_symbol_year/241/241840/2022.csv|atlas/symbol_profiles/241/241840.json|clean_180D_window|
|C27_241840_20220713_4B_SINGLE_TITLE_EVENT_CAP|241840|2022-07-13|32650|atlas/ohlcv_tradable_by_symbol_year/241/241840/2022.csv|atlas/symbol_profiles/241/241840.json|clean_180D_window|
|C27_200350_20221121_S2_REBORN_RICH_RATINGS_ROUTE|200350|2022-11-21|27200|atlas/ohlcv_tradable_by_symbol_year/200/200350/2022.csv|atlas/symbol_profiles/200/200350.json|clean_180D_window|
|C27_200350_20221125_4B_RATINGS_EVENT_CAP|200350|2022-11-25|38400|atlas/ohlcv_tradable_by_symbol_year/200/200350/2022.csv|atlas/symbol_profiles/200/200350.json|clean_180D_window|
|C27_200350_20221226_4C_POST_EVENT_FADE|200350|2022-12-26|22550|atlas/ohlcv_tradable_by_symbol_year/200/200350/2022.csv|atlas/symbol_profiles/200/200350.json|clean_180D_window|
|C27_263720_20240108_S2_SOLO_LEVELING_ANIME_ROUTE|263720|2024-01-08|29850|atlas/ohlcv_tradable_by_symbol_year/263/263720/2024.csv|atlas/symbol_profiles/263/263720.json|clean_180D_window|
|C27_263720_20240124_4B_PRICE_ONLY_LOCAL_PEAK|263720|2024-01-24|33400|atlas/ohlcv_tradable_by_symbol_year/263/263720/2024.csv|atlas/symbol_profiles/263/263720.json|clean_180D_window|
|C27_263720_20240510_4B_GAME_RELEASE_EVENT_CAP|263720|2024-05-10|34250|atlas/ohlcv_tradable_by_symbol_year/263/263720/2024.csv|atlas/symbol_profiles/263/263720.json|clean_180D_window|
|C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN|066410|2021-09-24|4665|atlas/ohlcv_tradable_by_symbol_year/066/066410/2021.csv|atlas/symbol_profiles/066/066410.json|clean_180D_window|
|C27_066410_20211119_4B_PRICE_ONLY_ASSOCIATION_BLOWOFF|066410|2021-11-19|7320|atlas/ohlcv_tradable_by_symbol_year/066/066410/2021.csv|atlas/symbol_profiles/066/066410.json|clean_180D_window|
|C27_066410_20211122_4C_ASSOCIATION_REVERSAL|066410|2021-11-22|6600|atlas/ohlcv_tradable_by_symbol_year/066/066410/2021.csv|atlas/symbol_profiles/066/066410.json|clean_180D_window|


## 11. Case-by-Case Trigger Grid

|trigger_id|case_id|symbol|trigger_type|trigger_date|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|outcome|current_profile_verdict|role|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL|C27_241840_ASTORY_WOOYOUNGWOO_2022|241840|Stage2-Actionable|2022-06-30|2022-06-30|18000|94.44|-2.78|structural_upside_realized_but_fast_event_cap|current_profile_too_late|representative|
|C27_241840_20220713_GREEN_WOO_GLOBAL_RANKING_CONFIRMATION|C27_241840_ASTORY_WOOYOUNGWOO_2022|241840|Stage3-Green|2022-07-13|2022-07-13|32650|7.2|-45.94|late_green_low_forward_upside|current_profile_too_late|label_comparison_only|
|C27_241840_20220713_4B_SINGLE_TITLE_EVENT_CAP|C27_241840_ASTORY_WOOYOUNGWOO_2022|241840|Stage4B|2022-07-13|2022-07-13|32650|7.2|-45.94|4B_overlay_success|current_profile_correct|4B_overlay_only|
|C27_200350_20221121_S2_REBORN_RICH_RATINGS_ROUTE|C27_200350_RAEMONG_REBORN_RICH_2022|200350|Stage2-Actionable|2022-11-18|2022-11-21|27200|45.59|-33.46|high_MFE_high_MAE_success|current_profile_correct_for_entry_but_4B_late|representative|
|C27_200350_20221125_4B_RATINGS_EVENT_CAP|C27_200350_RAEMONG_REBORN_RICH_2022|200350|Stage4B|2022-11-25|2022-11-25|38400|3.13|-52.86|4B_overlay_success_high_MAE_protection|current_profile_4B_too_late|4B_overlay_only|
|C27_200350_20221226_4C_POST_EVENT_FADE|C27_200350_RAEMONG_REBORN_RICH_2022|200350|Stage4C|2022-12-26|2022-12-26|22550|16.85|-19.73|4C_protection_after_event_cap|current_profile_4C_too_late|4C_overlay_only|
|C27_263720_20240108_S2_SOLO_LEVELING_ANIME_ROUTE|C27_263720_DNC_SOLO_LEVELING_2024|263720|Stage2-Actionable|2024-01-07|2024-01-08|29850|29.31|-27.81|positive_MFE_but_high_MAE_after_IP_event|current_profile_too_early|representative|
|C27_263720_20240124_4B_PRICE_ONLY_LOCAL_PEAK|C27_263720_DNC_SOLO_LEVELING_2024|263720|Stage4B|2024-01-24|2024-01-24|33400|15.57|-35.48|price_only_4B_watch_needed|current_profile_correct|4B_overlay_only|
|C27_263720_20240510_4B_GAME_RELEASE_EVENT_CAP|C27_263720_DNC_SOLO_LEVELING_2024|263720|Stage4B|2024-05-10|2024-05-10|34250|8.76|-53.26|4B_late_but_drawdown_protection|current_profile_4B_too_late|4B_overlay_only|
|C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN|C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021|066410|Stage3-Green|2021-09-24|2021-09-24|4665|80.49|-26.58|false_positive_green_association_only|current_profile_false_positive|representative|
|C27_066410_20211119_4B_PRICE_ONLY_ASSOCIATION_BLOWOFF|C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021|066410|Stage4B|2021-11-19|2021-11-19|7320|15.03|-53.21|price_only_4B_overlay_success_but_not_positive_signal|current_profile_correct|4B_overlay_only|
|C27_066410_20211122_4C_ASSOCIATION_REVERSAL|C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021|066410|Stage4C|2021-11-22|2021-11-22|6600|10.61|-48.11|4C_protection_association_break|current_profile_4C_too_late|4C_overlay_only|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak|DD_after_peak|
|---|---|---|---|---|---|---|---|---|---|
|C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL|2022-06-30 @ 18000|94.44|-2.78|94.44|-2.78|94.44|-2.78|2022-07-13 @ 35000|-49.57|
|C27_241840_20220713_GREEN_WOO_GLOBAL_RANKING_CONFIRMATION|2022-07-13 @ 32650|7.2|-14.55|7.2|-45.94|7.2|-45.94|2022-07-13 @ 35000|-49.57|
|C27_241840_20220713_4B_SINGLE_TITLE_EVENT_CAP|2022-07-13 @ 32650|7.2|-14.55|7.2|-45.94|7.2|-45.94|2022-07-13 @ 35000|-49.57|
|C27_200350_20221121_S2_REBORN_RICH_RATINGS_ROUTE|2022-11-21 @ 27200|45.59|-24.63|45.59|-33.46|45.59|-33.46|2022-11-28 @ 39600|-54.29|
|C27_200350_20221125_4B_RATINGS_EVENT_CAP|2022-11-25 @ 38400|3.13|-45.57|3.13|-52.86|3.13|-52.86|2022-11-28 @ 39600|-54.29|
|C27_200350_20221226_4C_POST_EVENT_FADE|2022-12-26 @ 22550|16.85|-9.09|16.85|-19.73|16.85|-19.73|2023-01-17 @ 26350|-31.31|
|C27_263720_20240108_S2_SOLO_LEVELING_ANIME_ROUTE|2024-01-08 @ 29850|29.31|-19.26|29.31|-27.81|29.31|-46.37|2024-01-24 @ 38600|-58.52|
|C27_263720_20240124_4B_PRICE_ONLY_LOCAL_PEAK|2024-01-24 @ 33400|15.57|-27.69|15.57|-35.48|15.57|-52.07|2024-01-24 @ 38600|-58.52|
|C27_263720_20240510_4B_GAME_RELEASE_EVENT_CAP|2024-05-10 @ 34250|8.76|-27.3|8.76|-53.26|8.76|-53.26|2024-05-10 @ 37250|-57.02|
|C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN|2021-09-24 @ 4665|80.49|-18.76|80.49|-26.58|80.49|-26.58|2021-11-19 @ 8420|-59.32|
|C27_066410_20211119_4B_PRICE_ONLY_ASSOCIATION_BLOWOFF|2021-11-19 @ 7320|15.03|-31.28|15.03|-53.21|15.03|-53.21|2021-11-19 @ 8420|-59.32|
|C27_066410_20211122_4C_ASSOCIATION_REVERSAL|2021-11-22 @ 6600|10.61|-23.79|10.61|-48.11|10.61|-48.11|2021-12-13 @ 7300|-53.08|


## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated profile judgment | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| C27_241840_ASTORY_WOOYOUNGWOO_2022 | Stage2 likely correct, Green confirmation late | Stage2 captured +94.44% MFE; Green after ranking captured only +7.20% | current_profile_too_late |
| C27_200350_RAEMONG_REBORN_RICH_2022 | Entry okay, but 4B event cap too late | +45.59% MFE with -33.46% 90D MAE; 4B was necessary near peak | current_profile_4B_too_late |
| C27_263720_DNC_SOLO_LEVELING_2024 | Stage2/Yellow okay, Green would be too early | +29.31% MFE but -46.37% 180D MAE | current_profile_too_early |
| C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021 | Would be false Green if price/association dominates | +80.49% MFE but no direct monetization bridge and -59.32% post-peak drawdown | current_profile_false_positive |

Stress-test answers:

1. Stage2 bonus was useful for rights-backed early signals, but too permissive if the only evidence is association/price.
2. Yellow threshold 75 is acceptable for C27 only with direct rights or platform/customer evidence.
3. Green 87 / revision 55 remains appropriate; in C27 the missing piece is often not total score but repeatability and margin conversion.
4. price-only blowoff guard is strengthened by Bucket and D&C local peak rows.
5. full 4B non-price requirement is kept; price-only 4B remains overlay/watch, not thesis evidence.
6. hard 4C routing is kept; event-cap thesis breaks should protect from post-peak drawdown.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green/comparison entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| C27_241840_ASTORY_WOOYOUNGWOO_2022 | 18,000 | 32,650 | 0.862 | Green after global confirmation captured upside too late |
| C27_200350_RAEMONG_REBORN_RICH_2022 | 27,200 | no confirmed repeatable Green | not_applicable | Stage2/Yellow only; 4B needed after event cap |
| C27_263720_DNC_SOLO_LEVELING_2024 | 29,850 | no confirmed repeatable Green | not_applicable | anime/game optionality needs conversion proof before Green |
| C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021 | 4,665 | false Green if association treated as evidence | 0.000 | price moved, but no direct C27 evidence |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| C27_241840_20220713_4B_SINGLE_TITLE_EVENT_CAP | valuation_blowoff / positioning / event_cap | 0.862 | 0.862 | good_full_window_4B_timing |
| C27_200350_20221125_4B_RATINGS_EVENT_CAP | valuation_blowoff / positioning / event_cap | 0.903 | 0.903 | good_full_window_4B_timing |
| C27_263720_20240124_4B_PRICE_ONLY_LOCAL_PEAK | price_only / valuation / positioning | 0.406 | 0.406 | price_only_local_4B_too_early |
| C27_263720_20240510_4B_GAME_RELEASE_EVENT_CAP | valuation / positioning / event_cap | 0.595 | 0.503 | non_price_4B_but_full_window_peak_already_passed |
| C27_066410_20211119_4B_PRICE_ONLY_ASSOCIATION_BLOWOFF | price_only / valuation / positioning | 0.707 | 0.707 | price_only_local_4B_too_early_for_full_4B |

## 16. 4C Protection Audit

| trigger_id | four_c_protection_label | protection interpretation |
|---|---|---|
| C27_200350_20221226_4C_POST_EVENT_FADE | hard_4c_success | after the title cycle faded, 4C/watch-only prevented treating the event as repeatable thesis |
| C27_066410_20211122_4C_ASSOCIATION_REVERSAL | hard_4c_success | association-only rerating broke quickly; 4C prevents positive-weight contamination |
| C27_263720_20240510_4B_GAME_RELEASE_EVENT_CAP | hard_4c_success | game-release event had non-price evidence but still needed post-event thesis-break monitoring |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
candidate_axis = L8_content_hit_requires_monetization_bridge
```

Candidate rule:

- Add an L8 shadow gate that separates **audience evidence** from **monetization evidence**.
- Stage2 may accept first-broadcast / release / ranking evidence if direct rights or customer/platform route is present.
- Stage3-Green should require at least one of: repeatable slate, contract/customer confirmation, margin/revision bridge, or platform economics beyond the single event.
- Association-only price action gets no positive promotion even if MFE is large.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
new_axis_proposed = c27_direct_rights_or_owned_ip_bonus | c27_single_title_event_cap_4b_overlay | c27_association_only_green_block
```

C27-specific logic:

1. **Direct rights / owned IP bonus**: small positive shadow bonus when the company is the producer/publisher or rights holder and the global platform route is public.
2. **Single-title event-cap 4B overlay**: fast 4B overlay when the same title drives most of the re-rating and price nears the local/full peak.
3. **Association-only Green block**: relative strength without direct rights, customer economics, or margin bridge cannot promote Stage3-Green.

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|
|P0|current calibrated|12|62.46|-22.66|1/4|1|1|mixed; catches early winners but mislabels association-only and late 4B|
|P0b|old baseline reference|12|62.46|-22.66|2/4|2|2|weaker than current profile|
|P1|sector shadow|12|62.46|-22.66|0/4 after guard|0|1|better; promotes Stage2 while forcing 4B for event cap|
|P2|canonical C27 shadow|12|62.46|-22.66|0/4 after association guard|0|0|best; direct rights + repeatability bridge + event-cap overlay|
|P3|counterexample guard|12|62.46|-22.66|0/4|1|0|strong guard but may under-promote early C27 winners|


## 20. Score-Return Alignment Matrix

| alignment label | trigger examples | score-return read |
|---|---|---|
| structural_upside_realized_but_fast_event_cap | AStory Stage2 | Stage2 worked, Green too late, 4B should be quick |
| high_MFE_high_MAE_success | Raemong Stage2 | entry worked but without 4B the investor sits through a cliff |
| positive_MFE_but_high_MAE_after_IP_event | D&C Stage2 | IP extension is real, but conversion timing is not enough for Green |
| false_positive_green_association_only | Bucket Stage3 false Green | price move alone contaminates positive calibration |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L8_PLATFORM_CONTENT_SW_SECURITY|C27_CONTENT_IP_GLOBAL_MONETIZATION|K_DRAMA_WEBTOON_SINGLE_TITLE_TO_REPEATABLE_IP_MONETIZATION|3|1|5|2|4|0|12|4|4|true|true|C27 still needs broader holdout across animation/game/webtoon IP, but single-title/association residual is now covered.|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: single_title_event_cap_high_MAE, association_only_false_green, green_confirmation_lateness_in_content_IP, price_only_4B_must_not_be_full_4B, 4C_needed_after_event_thesis_fades
new_axis_proposed: c27_direct_rights_or_owned_ip_bonus, c27_single_title_event_cap_4b_overlay, c27_association_only_green_block
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest/schema/profile fields
- actual tradable_raw OHLC rows for entry windows
- 30D/90D/180D MFE/MAE proxy calculations
- same-entry dedupe and representative-trigger separation
- current calibrated profile stress test
- C27 single-title / association-only residual rule proposal

Not validated:

- no live 2026 candidate scan
- no brokerage or auto-trading logic
- no `stock_agent` source-code read
- no production scoring patch
- no assertion that any current stock is investable

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_direct_rights_or_owned_ip_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,Rights-owning/production-backed hit behaves better than association-only hit.,ASTORY and Raemong had strong MFE but required 4B event cap; association-only Bucket false Green is blocked.,C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL|C27_200350_20221121_S2_REBORN_RICH_RATINGS_ROUTE|C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN,4,4,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c27_single_title_event_cap_4b_overlay,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,Single-title content cycles can be right on entry and still need fast 4B overlay.,AStory/Raemong/DNC show high MFE but sharp post-peak drawdowns.,C27_241840_20220713_4B_SINGLE_TITLE_EVENT_CAP|C27_200350_20221125_4B_RATINGS_EVENT_CAP|C27_263720_20240510_4B_GAME_RELEASE_EVENT_CAP,4,4,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c27_association_only_green_block,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,Price-only content-theme association must not promote Stage3/Green.,Bucket case shows high MFE but no durable monetization evidence and large drawdown.,C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN,1,1,1,medium,counterexample_guard,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C27_241840_ASTORY_WOOYOUNGWOO_2022", "symbol": "241840", "company_name": "에이스토리", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_DRAMA_SINGLE_TITLE_GLOBAL_HIT_WITH_PRODUCTION_RIGHTS", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "우영우 첫 방영 직후 Stage2-Actionable은 빠르게 작동했지만, Netflix global ranking/시청시간 확인 이후 Green으로만 진입하면 대부분의 단기 upside를 놓치는 케이스. 단일 히트이지만 제작사/공동제작/Netflix 동시유통이 확인되어 price-only가 아니다.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "우영우 첫 방영 직후 Stage2-Actionable은 빠르게 작동했지만, Netflix global ranking/시청시간 확인 이후 Green으로만 진입하면 대부분의 단기 upside를 놓치는 케이스. 단일 히트이지만 제작사/공동제작/Netflix 동시유통이 확인되어 price-only가 아니다."}
{"row_type": "case", "case_id": "C27_200350_RAEMONG_REBORN_RICH_2022", "symbol": "200350", "company_name": "래몽래인/아티스트스튜디오", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_DRAMA_RATINGS_HIT_SINGLE_TITLE_EVENT_CAP", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "C27_200350_20221121_S2_REBORN_RICH_RATINGS_ROUTE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "재벌집 막내아들 방영·시청률 모멘텀은 강했지만, 소형 제작사의 단일 타이틀 이벤트는 빠른 4B overlay가 없으면 MAE가 매우 커졌다.", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "재벌집 막내아들 방영·시청률 모멘텀은 강했지만, 소형 제작사의 단일 타이틀 이벤트는 빠른 4B overlay가 없으면 MAE가 매우 커졌다."}
{"row_type": "case", "case_id": "C27_263720_DNC_SOLO_LEVELING_2024", "symbol": "263720", "company_name": "디앤씨미디어", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_ANIME_GAME_OPTIONALITY", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "C27_263720_20240108_S2_SOLO_LEVELING_ANIME_ROUTE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "나 혼자만 레벨업 anime/game route는 global IP 확장성은 보였지만, stock-web 180D에서는 peak 이후 큰 drawdown이 확인되어 C27에는 hit→repeatable monetization bridge 확인 전 Green 보류가 필요하다.", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "나 혼자만 레벨업 anime/game route는 global IP 확장성은 보였지만, stock-web 180D에서는 peak 이후 큰 drawdown이 확인되어 C27에는 hit→repeatable monetization bridge 확인 전 Green 보류가 필요하다."}
{"row_type": "case", "case_id": "C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021", "symbol": "066410", "company_name": "버킷스튜디오", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ASSOCIATION_ONLY_CONTENT_THEME_FALSE_POSITIVE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "오징어게임 관련주로 가격은 폭발했지만 직접 제작권/반복 monetization bridge가 검증되지 않은 association trade. C27에서 price-only/association-only를 Stage3로 올리면 위험하다는 반례.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "오징어게임 관련주로 가격은 폭발했지만 직접 제작권/반복 monetization bridge가 검증되지 않은 association trade. C27에서 price-only/association-only를 Stage3로 올리면 위험하다는 반례."}
{"row_type": "trigger", "trigger_id": "C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL", "case_id": "C27_241840_ASTORY_WOOYOUNGWOO_2022", "symbol": "241840", "company_name": "에이스토리", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_DRAMA_SINGLE_TITLE_GLOBAL_HIT_WITH_PRODUCTION_RIGHTS", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-06-30", "evidence_available_at_that_date": "첫 방영 후 제작사/Netflix 동시유통/ENA ratings ramp가 공개적으로 확인되기 시작한 Stage2. 실제 row: 2022-06-30 close 18,000, high 19,500.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241840/2022.csv", "profile_path": "atlas/symbol_profiles/241/241840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-06-30", "entry_price": 18000, "MFE_30D_pct": 94.44, "MFE_90D_pct": 94.44, "MFE_180D_pct": 94.44, "MFE_1Y_pct": 94.44, "MFE_2Y_pct": 94.44, "MAE_30D_pct": -2.78, "MAE_90D_pct": -2.78, "MAE_180D_pct": -2.78, "MAE_1Y_pct": -2.78, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-07-13", "peak_price": 35000, "drawdown_after_peak_pct": -49.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_upside_realized_but_fast_event_cap", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_241840_20220630", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_241840_20220713_GREEN_WOO_GLOBAL_RANKING_CONFIRMATION", "case_id": "C27_241840_ASTORY_WOOYOUNGWOO_2022", "symbol": "241840", "company_name": "에이스토리", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_DRAMA_SINGLE_TITLE_GLOBAL_HIT_WITH_PRODUCTION_RIGHTS", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2022-07-13", "evidence_available_at_that_date": "Netflix/global ranking and domestic ratings confirmation after the move; actual row close 32,650, high 35,000.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241840/2022.csv", "profile_path": "atlas/symbol_profiles/241/241840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-07-13", "entry_price": 32650, "MFE_30D_pct": 7.2, "MFE_90D_pct": 7.2, "MFE_180D_pct": 7.2, "MFE_1Y_pct": 7.2, "MFE_2Y_pct": 7.2, "MAE_30D_pct": -14.55, "MAE_90D_pct": -45.94, "MAE_180D_pct": -45.94, "MAE_1Y_pct": -45.94, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-07-13", "peak_price": 35000, "drawdown_after_peak_pct": -49.57, "green_lateness_ratio": 0.862, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "green_after_most_upside_realized", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_low_forward_upside", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_241840_20220713", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_241840_20220713_4B_SINGLE_TITLE_EVENT_CAP", "case_id": "C27_241840_ASTORY_WOOYOUNGWOO_2022", "symbol": "241840", "company_name": "에이스토리", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_DRAMA_SINGLE_TITLE_GLOBAL_HIT_WITH_PRODUCTION_RIGHTS", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2022-07-13", "evidence_available_at_that_date": "Same-day 4B overlay: valuation/positioning overheated around a single-title event; not a thesis cancellation.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241840/2022.csv", "profile_path": "atlas/symbol_profiles/241/241840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-07-13", "entry_price": 32650, "MFE_30D_pct": 7.2, "MFE_90D_pct": 7.2, "MFE_180D_pct": 7.2, "MFE_1Y_pct": 7.2, "MFE_2Y_pct": 7.2, "MAE_30D_pct": -14.55, "MAE_90D_pct": -45.94, "MAE_180D_pct": -45.94, "MAE_1Y_pct": -45.94, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-07-13", "peak_price": 35000, "drawdown_after_peak_pct": -49.57, "green_lateness_ratio": 0.862, "four_b_local_peak_proximity": 0.862, "four_b_full_window_peak_proximity": 0.862, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_241840_20220713", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_200350_20221121_S2_REBORN_RICH_RATINGS_ROUTE", "case_id": "C27_200350_RAEMONG_REBORN_RICH_2022", "symbol": "200350", "company_name": "래몽래인/아티스트스튜디오", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_DRAMA_RATINGS_HIT_SINGLE_TITLE_EVENT_CAP", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-11-18", "evidence_available_at_that_date": "재벌집 막내아들 첫 방영 후 다음 거래일 entry. Stock-web row 2022-11-21 close 27,200; show company includes RaemongRaein.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/200/200350/2022.csv", "profile_path": "atlas/symbol_profiles/200/200350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-21", "entry_price": 27200, "MFE_30D_pct": 45.59, "MFE_90D_pct": 45.59, "MFE_180D_pct": 45.59, "MFE_1Y_pct": 45.59, "MFE_2Y_pct": 45.59, "MAE_30D_pct": -24.63, "MAE_90D_pct": -33.46, "MAE_180D_pct": -33.46, "MAE_1Y_pct": -33.46, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-28", "peak_price": 39600, "drawdown_after_peak_pct": -54.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_MFE_high_MAE_success", "current_profile_verdict": "current_profile_correct_for_entry_but_4B_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_200350_20221121", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_200350_20221125_4B_RATINGS_EVENT_CAP", "case_id": "C27_200350_RAEMONG_REBORN_RICH_2022", "symbol": "200350", "company_name": "래몽래인/아티스트스튜디오", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_DRAMA_RATINGS_HIT_SINGLE_TITLE_EVENT_CAP", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2022-11-25", "evidence_available_at_that_date": "Rapid re-rating after ratings momentum; actual row close 38,400, next peak high 39,600. Strong 4B overlay rather than new Green.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/200/200350/2022.csv", "profile_path": "atlas/symbol_profiles/200/200350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-11-25", "entry_price": 38400, "MFE_30D_pct": 3.13, "MFE_90D_pct": 3.13, "MFE_180D_pct": 3.13, "MFE_1Y_pct": 3.13, "MFE_2Y_pct": 3.13, "MAE_30D_pct": -45.57, "MAE_90D_pct": -52.86, "MAE_180D_pct": -52.86, "MAE_1Y_pct": -52.86, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-28", "peak_price": 39600, "drawdown_after_peak_pct": -54.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.903, "four_b_full_window_peak_proximity": 0.903, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_high_MAE_protection", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_200350_20221125", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_200350_20221226_4C_POST_EVENT_FADE", "case_id": "C27_200350_RAEMONG_REBORN_RICH_2022", "symbol": "200350", "company_name": "래몽래인/아티스트스튜디오", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "K_DRAMA_RATINGS_HIT_SINGLE_TITLE_EVENT_CAP", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C", "trigger_date": "2022-12-26", "evidence_available_at_that_date": "Post-event fade after the drama cycle; not a cancellation, but single-title rerating thesis broke.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/200/200350/2022.csv", "profile_path": "atlas/symbol_profiles/200/200350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-12-26", "entry_price": 22550, "MFE_30D_pct": 16.85, "MFE_90D_pct": 16.85, "MFE_180D_pct": 16.85, "MFE_1Y_pct": 16.85, "MFE_2Y_pct": 16.85, "MAE_30D_pct": -9.09, "MAE_90D_pct": -19.73, "MAE_180D_pct": -19.73, "MAE_1Y_pct": -19.73, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-01-17", "peak_price": 26350, "drawdown_after_peak_pct": -31.31, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_protection_after_event_cap", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_200350_20221226", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_263720_20240108_S2_SOLO_LEVELING_ANIME_ROUTE", "case_id": "C27_263720_DNC_SOLO_LEVELING_2024", "symbol": "263720", "company_name": "디앤씨미디어", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_ANIME_GAME_OPTIONALITY", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-07", "evidence_available_at_that_date": "Solo Leveling anime first broadcast weekend and next tradable day entry; row 2024-01-08 close 29,850.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263720/2024.csv", "profile_path": "atlas/symbol_profiles/263/263720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-08", "entry_price": 29850, "MFE_30D_pct": 29.31, "MFE_90D_pct": 29.31, "MFE_180D_pct": 29.31, "MFE_1Y_pct": 29.31, "MFE_2Y_pct": 29.31, "MAE_30D_pct": -19.26, "MAE_90D_pct": -27.81, "MAE_180D_pct": -46.37, "MAE_1Y_pct": -46.37, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 38600, "drawdown_after_peak_pct": -58.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_MFE_but_high_MAE_after_IP_event", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_263720_20240108", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_263720_20240124_4B_PRICE_ONLY_LOCAL_PEAK", "case_id": "C27_263720_DNC_SOLO_LEVELING_2024", "symbol": "263720", "company_name": "디앤씨미디어", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_ANIME_GAME_OPTIONALITY", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2024-01-24", "evidence_available_at_that_date": "Local price spike without sufficient non-price monetization conversion; should remain 4B-watch, not full 4B if price-only.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263720/2024.csv", "profile_path": "atlas/symbol_profiles/263/263720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-24", "entry_price": 33400, "MFE_30D_pct": 15.57, "MFE_90D_pct": 15.57, "MFE_180D_pct": 15.57, "MFE_1Y_pct": 15.57, "MFE_2Y_pct": 15.57, "MAE_30D_pct": -27.69, "MAE_90D_pct": -35.48, "MAE_180D_pct": -52.07, "MAE_1Y_pct": -52.07, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 38600, "drawdown_after_peak_pct": -58.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.406, "four_b_full_window_peak_proximity": 0.406, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_4B_watch_needed", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_263720_20240124", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_263720_20240510_4B_GAME_RELEASE_EVENT_CAP", "case_id": "C27_263720_DNC_SOLO_LEVELING_2024", "symbol": "263720", "company_name": "디앤씨미디어", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "WEBTOON_IP_GLOBAL_ANIME_GAME_OPTIONALITY", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2024-05-10", "evidence_available_at_that_date": "Solo Leveling: Arise release-week monetization event; stock-web row close 34,250, followed by large drawdown. Non-price event exists, but still single-IP event cap.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263720/2024.csv", "profile_path": "atlas/symbol_profiles/263/263720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-10", "entry_price": 34250, "MFE_30D_pct": 8.76, "MFE_90D_pct": 8.76, "MFE_180D_pct": 8.76, "MFE_1Y_pct": 8.76, "MFE_2Y_pct": 8.76, "MAE_30D_pct": -27.3, "MAE_90D_pct": -53.26, "MAE_180D_pct": -53.26, "MAE_1Y_pct": -53.26, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-10", "peak_price": 37250, "drawdown_after_peak_pct": -57.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.595, "four_b_full_window_peak_proximity": 0.503, "four_b_timing_verdict": "non_price_4B_but_full_window_peak_already_passed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4B_late_but_drawdown_protection", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_263720_20240510", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN", "case_id": "C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021", "symbol": "066410", "company_name": "버킷스튜디오", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ASSOCIATION_ONLY_CONTENT_THEME_FALSE_POSITIVE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage3-Green", "trigger_date": "2021-09-24", "evidence_available_at_that_date": "Squid Game association trade; actual row close 4,665. Price moved, but direct content-IP monetization evidence was not established for the company.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066410/2021.csv", "profile_path": "atlas/symbol_profiles/066/066410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-09-24", "entry_price": 4665, "MFE_30D_pct": 80.49, "MFE_90D_pct": 80.49, "MFE_180D_pct": 80.49, "MFE_1Y_pct": 80.49, "MFE_2Y_pct": 80.49, "MAE_30D_pct": -18.76, "MAE_90D_pct": -26.58, "MAE_180D_pct": -26.58, "MAE_1Y_pct": -26.58, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-19", "peak_price": 8420, "drawdown_after_peak_pct": -59.32, "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "false_positive_green_association_only", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_066410_20210924", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_066410_20211119_4B_PRICE_ONLY_ASSOCIATION_BLOWOFF", "case_id": "C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021", "symbol": "066410", "company_name": "버킷스튜디오", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ASSOCIATION_ONLY_CONTENT_THEME_FALSE_POSITIVE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B", "trigger_date": "2021-11-19", "evidence_available_at_that_date": "Association trade blowoff near the 8,420 high; price-only 4B cannot be treated as thesis evidence.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066410/2021.csv", "profile_path": "atlas/symbol_profiles/066/066410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-19", "entry_price": 7320, "MFE_30D_pct": 15.03, "MFE_90D_pct": 15.03, "MFE_180D_pct": 15.03, "MFE_1Y_pct": 15.03, "MFE_2Y_pct": 15.03, "MAE_30D_pct": -31.28, "MAE_90D_pct": -53.21, "MAE_180D_pct": -53.21, "MAE_1Y_pct": -53.21, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-11-19", "peak_price": 8420, "drawdown_after_peak_pct": -59.32, "green_lateness_ratio": 0.707, "four_b_local_peak_proximity": 0.707, "four_b_full_window_peak_proximity": 0.707, "four_b_timing_verdict": "price_only_local_4B_too_early_for_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_4B_overlay_success_but_not_positive_signal", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_066410_20211119", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C27_066410_20211122_4C_ASSOCIATION_REVERSAL", "case_id": "C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021", "symbol": "066410", "company_name": "버킷스튜디오", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "ASSOCIATION_ONLY_CONTENT_THEME_FALSE_POSITIVE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "content_IP_global_monetization", "loop_objective": "holdout_validation|residual_false_positive_mining|residual_missed_structural_mining|yellow_threshold_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4C", "trigger_date": "2021-11-22", "evidence_available_at_that_date": "Immediate post-blowoff reversal; association-only thesis no longer protected. Route to 4C/watch-only.", "evidence_source": "public historical news/OTT ranking pages + Songdaiki/stock-web OHLC rows", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066410/2021.csv", "profile_path": "atlas/symbol_profiles/066/066410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-22", "entry_price": 6600, "MFE_30D_pct": 10.61, "MFE_90D_pct": 10.61, "MFE_180D_pct": 10.61, "MFE_1Y_pct": 10.61, "MFE_2Y_pct": 10.61, "MAE_30D_pct": -23.79, "MAE_90D_pct": -48.11, "MAE_180D_pct": -48.11, "MAE_1Y_pct": -48.11, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-12-13", "peak_price": 7300, "drawdown_after_peak_pct": -53.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_protection_association_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C27_066410_20211122", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_241840_ASTORY_WOOYOUNGWOO_2022", "trigger_id": "C27_241840_20220630_S2_WOO_YOUNG_WOO_FIRST_SIGNAL", "symbol": "241840", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow shadow", "changed_components": ["customer_quality_score", "valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C27 shadow-only adjustment: reward direct production/IP ownership and repeatable monetization bridge; penalize association-only price moves and single-title event-cap without backlog/margin bridge.", "MFE_90D_pct": 94.44, "MAE_90D_pct": -2.78, "score_return_alignment_label": "structural_upside_realized_but_fast_event_cap", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_241840_ASTORY_WOOYOUNGWOO_2022", "trigger_id": "C27_241840_20220713_GREEN_WOO_GLOBAL_RANKING_CONFIRMATION", "symbol": "241840", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 89, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 10, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage4B-watch / no new Green", "changed_components": ["customer_quality_score", "valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C27 shadow-only adjustment: reward direct production/IP ownership and repeatable monetization bridge; penalize association-only price moves and single-title event-cap without backlog/margin bridge.", "MFE_90D_pct": 7.2, "MAE_90D_pct": -45.94, "score_return_alignment_label": "late_green_low_forward_upside", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_200350_RAEMONG_REBORN_RICH_2022", "trigger_id": "C27_200350_20221121_S2_REBORN_RICH_RATINGS_ROUTE", "symbol": "200350", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 9, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow shadow", "changed_components": ["customer_quality_score", "valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C27 shadow-only adjustment: reward direct production/IP ownership and repeatable monetization bridge; penalize association-only price moves and single-title event-cap without backlog/margin bridge.", "MFE_90D_pct": 45.59, "MAE_90D_pct": -33.46, "score_return_alignment_label": "high_MFE_high_MAE_success", "current_profile_verdict": "current_profile_correct_for_entry_but_4B_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_200350_RAEMONG_REBORN_RICH_2022", "trigger_id": "C27_200350_20221125_4B_RATINGS_EVENT_CAP", "symbol": "200350", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green risk", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage4B-overlay", "changed_components": ["customer_quality_score", "valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C27 shadow-only adjustment: reward direct production/IP ownership and repeatable monetization bridge; penalize association-only price moves and single-title event-cap without backlog/margin bridge.", "MFE_90D_pct": 3.13, "MAE_90D_pct": -52.86, "score_return_alignment_label": "4B_overlay_success_high_MAE_protection", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_263720_DNC_SOLO_LEVELING_2024", "trigger_id": "C27_263720_20240108_S2_SOLO_LEVELING_ANIME_ROUTE", "symbol": "263720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable / wait repeatability", "changed_components": ["customer_quality_score", "valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C27 shadow-only adjustment: reward direct production/IP ownership and repeatable monetization bridge; penalize association-only price moves and single-title event-cap without backlog/margin bridge.", "MFE_90D_pct": 29.31, "MAE_90D_pct": -27.81, "score_return_alignment_label": "positive_MFE_but_high_MAE_after_IP_event", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_263720_DNC_SOLO_LEVELING_2024", "trigger_id": "C27_263720_20240124_4B_PRICE_ONLY_LOCAL_PEAK", "symbol": "263720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 9, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Green risk", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 3, "relative_strength_score": 9, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 69, "stage_label_after": "Stage4B-watch", "changed_components": ["customer_quality_score", "valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C27 shadow-only adjustment: reward direct production/IP ownership and repeatable monetization bridge; penalize association-only price moves and single-title event-cap without backlog/margin bridge.", "MFE_90D_pct": 15.57, "MAE_90D_pct": -35.48, "score_return_alignment_label": "price_only_4B_watch_needed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021", "trigger_id": "C27_066410_20210924_PRICE_ASSOCIATION_FALSE_GREEN", "symbol": "066410", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 10, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 87, "stage_label_before": "Stage3-Green false-positive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 10, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "No positive stage / 4B-watch", "changed_components": ["customer_quality_score", "valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C27 shadow-only adjustment: reward direct production/IP ownership and repeatable monetization bridge; penalize association-only price moves and single-title event-cap without backlog/margin bridge.", "MFE_90D_pct": 80.49, "MAE_90D_pct": -26.58, "score_return_alignment_label": "false_positive_green_association_only", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C27_066410_BUCKET_SQUIDGAME_ASSOCIATION_2021", "trigger_id": "C27_066410_20211122_4C_ASSOCIATION_REVERSAL", "symbol": "066410", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 48, "stage_label_after": "Stage4C", "changed_components": ["customer_quality_score", "valuation_repricing_score", "execution_risk_score", "margin_bridge_score"], "component_delta_explanation": "C27 shadow-only adjustment: reward direct production/IP ownership and repeatable monetization bridge; penalize association-only price moves and single-title event-cap without backlog/margin bridge.", "MFE_90D_pct": 10.61, "MAE_90D_pct": -48.11, "score_return_alignment_label": "4C_protection_association_break", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "residual_contribution", "round": "R13", "loop": "38", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["single_title_event_cap_high_MAE", "association_only_false_green", "green_confirmation_lateness_in_content_IP", "price_only_4B_must_not_be_full_4B", "4C_needed_after_event_thesis_fades"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = R13_loop_39
suggested_large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
suggested_canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
suggested_loop_objective = coverage_gap_fill | counterexample_mining | retention_vs_one_time_contract_residual
```

## 28. Source Notes

- Stock-Web manifest/schema/profile/shard data were read from Songdaiki/stock-web.
- Evidence references used for narrative classification include historical public pages on Extraordinary Attorney Woo, Reborn Rich, Solo Leveling, and Squid Game-related association trades. The quantitative rows rely only on stock-web OHLC values.
- All price rows are raw/unadjusted. Corporate-action contaminated windows are blocked by default; the tested 180D windows above are marked clean at the profile-window level.
