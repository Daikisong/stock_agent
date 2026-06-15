---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 100
selected_priority_bucket: Priority 2 quality_repair_after_local_priority1_fill; published index Priority 1
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: C27_REPEAT_MONETIZATION_BRIDGE_VS_ONE_HIT_OR_TRAILER_LABEL_SPIKE
deep_sub_archetype_id: C27_DEEP_KPOP_GAME_WEBTOON_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_VS_EVENT_SPIKE
primary_price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_agent_code_accessed: false
stock_agent_src_e2r_accessed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
output_file: e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
status: completed
---

# E2R Stock-Web V12 Residual Research — R8 / L8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / loop 100

## 0. Execution compliance

This Markdown is a standalone historical calibration / sector-archetype residual research file. It is not a live stock scan, not a current watchlist, not a recommendation list, not a brokerage/API workflow, and not a `stock_agent` code patch.

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R8
selected_loop = 100
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Coverage-index selection

The published No-Repeat Index still marks `C27_CONTENT_IP_GLOBAL_MONETIZATION` as a Priority 1 archetype with 48 rows, two rows short of the 50-row practical calibration band. In this running local session, `C27` loop 99 already supplied seven representative rows, so this loop is not a minimum-fill pass. It is a quality-repair pass: separate verified repeat monetization bridges from one-hit game launches, trailer/demo events, and broad K-content label spikes.

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority1_fill; published index Priority 1
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
current_index_rows_before_local_session = 48
local_session_C27_loop99_representative = 7
loop100_representative = 8
estimated_local_session_rows_after_this_loop = about 63
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

Loop selection follows the v12 output identifier rule. The local session already produced `R8_loop_99` for C27. Therefore this file uses `R8_loop_100`.

## 2. Stock-Web manifest and validation scope

```json
{
  "price_data_source": "Songdaiki/stock-web",
  "upstream_source": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "price_basis": "tradable_raw",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "manifest_caveat": "Raw/unadjusted OHLC; zero-volume and invalid OHLC excluded from calibration shards; corporate-action-contaminated windows blocked by default."
}
```

Validation policy applied:

```text
entry_price = entry_date close from tradable shard
MFE/MAE windows = first 30 / 90 / 180 tradable rows starting at entry_date
if trigger_date is non-trading or evidence timing requires next session -> next tradable date allowed
if forward 180D unavailable by manifest max_date -> calibration_usable = false
if corporate-action or discontinuity screen overlaps entry~D+180 -> calibration_usable = false or blocked for promotion
```

## 3. Source register

- `SRC_MAIN_PROMPT` — execution procedure; coverage-index-first scheduler and v12 output requirements — https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- `SRC_NO_REPEAT_INDEX` — duplicate avoidance and coverage priority ledger — https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- `SRC_STOCK_WEB_MANIFEST` — max_date, raw/unadjusted price basis, calibration shard root — https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- `SRC_NETMARBLE_SOLO_LAUNCH` — Netmarble announced global launch of Solo Leveling: ARISE on Android, iOS, and PC on 2024-05-08 — https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=4808
- `SRC_NETMARBLE_SOLO_REVENUE` — early revenue/geographic mix readthrough for Solo Leveling: ARISE — https://www.kedglobal.com/korean-games/newsView/ked202406180013
- `SRC_KRAFTON_2024_RECORD` — 2024 record sales/OP and PUBG/BGMI bridge — https://www.krafton.com/en/news/press/krafton-records-all-time-highs-in-sales-2-7098t-krw-and-operating-profit-1-1825t-krw-in-2024/
- `SRC_SM_3Q24_SCRIPT` — SM 3Q24 concert and 1Q25 aespa global tour pipeline — https://cdn2.smentertainment.com/wp-content/uploads/2024/11/3Q24_ScriptENG_%EC%8B%A4%EC%A0%81_20241105_vF-2.pdf
- `SRC_YG_BLACKPINK_2025_COMEBACK_TOUR` — YG/BLACKPINK 2025 comeback and world-tour option — https://hypebeast.com/2024/7/yg-announces-blackpink-2025-comeback-world-tour
- `SRC_PEARLABYSS_GAMESCOM_2024` — Crimson Desert Gamescom 2024 playable demo event — https://crimsondesert.pearlabyss.com/it-IT/News/Notice/Detail?_boardNo=27
- `SRC_CONTENTREE_Q2_2024` — Contentree 2Q24 revenue and operating-loss context — https://www.directmedialab.com/contentree-joongang-reports-q2-revenue-of-226-8b-sll-megabox-performance-improves/
- `SRC_DNC_SOLO_IP_PROXY` — D&C Media / Solo Leveling IP game adaptation proxy source — https://pulse.mk.co.kr/news/english/9830618
- `SRC_HYBE_EXPANDED_RIGHTS_Q3_2024_PROXY` — HYBE expanded-rights/platform diversification proxy after 2024 governance overhang — https://www.midiaresearch.com/blog/what-hybe-and-umgs-q3-earnings-tell-us-about-superfans
- `SRC_JYP_PIPELINE_PROXY` — JYP business mix / album, concert, MD proxy for global monetization bridge — https://w4.kirs.or.kr/download/research_eng/250428_JYP%20Ent%28%EA%B8%80%EC%84%B8%29_%EC%B5%9C%EC%A2%85_EN_0523_%EC%88%98%EC%A0%95%200529.pdf

## 4. Novelty and duplicate screen

Previous local C27 loop 99 used JYP 2023-05-30, HYBE 2024-02-26, Krafton 2024-05-08, Netmarble 2024-08-09, Studio Dragon 2024-04-15, Kakao Games 2023-08-02, and Pearl Abyss 2023-08-23. This loop avoids the exact duplicate key `canonical_archetype_id + symbol + trigger_type + entry_date`. It reuses some broad symbols only with new trigger families and new entry dates, while adding new C27 symbols in SM Entertainment, YG Entertainment, Contentree JoongAng, and D&C Media.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
minimum_new_symbol_count = 2
actual_new_symbol_count_vs_loop99 = 4
actual_new_trigger_family_count = 8
minimum_positive_case_count = 1
actual_positive_case_count = 4
minimum_counterexample_count = 1
actual_counterexample_count = 4
```

## 5. Case register

```jsonl
{"case_id":"C27-R8-L100-352820-20241202","symbol":"352820","name":"HYBE","trigger_family":"kpop_portfolio_tour_platform_recovery_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-02","entry_date":"2024-12-02","entry_price":189800.0,"outcome":"positive_recovery_after_governance_overhang","classification":"positive","residual":"C27 can miss structural recovery when global artist portfolio plus platform/tour bridge emerges after governance-discount reset","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_PORTFOLIO_TOUR_PLATFORM_IP_RECOVERY_BRIDGE","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","calibration_usable":true,"source_ids":["SRC_HYBE_EXPANDED_RIGHTS_Q3_2024_PROXY"]}
{"case_id":"C27-R8-L100-035900-20241114","symbol":"035900","name":"JYP Ent.","trigger_family":"kpop_global_tour_album_md_recovery_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-14","entry_date":"2024-11-14","entry_price":56800.0,"outcome":"positive_clean_low_MAE","classification":"positive","residual":"C27 should allow Actionable when K-pop label has repeat album/tour schedule plus low drawdown confirmation, but not Green without margin bridge","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_GLOBAL_TOUR_ALBUM_MD_MONETIZATION_BRIDGE","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","calibration_usable":true,"source_ids":["SRC_JYP_PIPELINE_PROXY"]}
{"case_id":"C27-R8-L100-041510-20241108","symbol":"041510","name":"SM Entertainment","trigger_family":"multi_artist_concert_pipeline_revenue_bridge","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-08","entry_date":"2024-11-08","entry_price":74800.0,"outcome":"positive_verified_pipeline","classification":"positive","residual":"verified tour schedule plus multi-artist pipeline is the C27 positive control; block only if margin/revision is absent after the pipeline","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_MULTI_ARTIST_CONCERT_PIPELINE_MONETIZATION_BRIDGE","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","calibration_usable":true,"source_ids":["SRC_SM_3Q24_SCRIPT"]}
{"case_id":"C27-R8-L100-122870-20241112","symbol":"122870","name":"YG Entertainment","trigger_family":"blackpink_world_tour_comeback_option_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-12","entry_date":"2024-11-12","entry_price":43150.0,"outcome":"positive_option_repricing","classification":"positive","residual":"C27 needs to treat comeback/tour option as Actionable first; Yellow only when schedule/ticketing/album economics become visible","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_WORLD_TOUR_COMEBACK_OPTION_BRIDGE","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","calibration_usable":true,"source_ids":["SRC_YG_BLACKPINK_2025_COMEBACK_TOUR"]}
{"case_id":"C27-R8-L100-251270-20240509","symbol":"251270","name":"Netmarble","trigger_family":"solo_leveling_global_launch_vs_retention_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":64800.0,"outcome":"counterexample_one_title_fade","classification":"counterexample","residual":"one-hit global game launch requires retention cohort, payer mix, or next-title bridge before positive stage promotion","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_WEBTOON_TO_GAME_ONE_TITLE_LAUNCH_RETENTION_BRIDGE","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","calibration_usable":true,"source_ids":["SRC_NETMARBLE_SOLO_LAUNCH","SRC_NETMARBLE_SOLO_REVENUE"]}
{"case_id":"C27-R8-L100-263750-20240822","symbol":"263750","name":"Pearl Abyss","trigger_family":"crimson_desert_gamescom_demo_without_revenue_bridge","trigger_type":"4B","trigger_date":"2024-08-22","entry_date":"2024-08-22","entry_price":42050.0,"outcome":"counterexample_event_demo_high_MAE","classification":"counterexample","residual":"trailer/playable-demo IP quality without launch economics remains 4B watch; full 4B/4C requires schedule or revenue thesis break","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_CONSOLE_GAME_EVENT_DEMO_RELEASE_DATE_REVENUE_BRIDGE","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","calibration_usable":true,"source_ids":["SRC_PEARLABYSS_GAMESCOM_2024"]}
{"case_id":"C27-R8-L100-036420-20240516","symbol":"036420","name":"Contentree JoongAng","trigger_family":"content_theater_recovery_without_margin_bridge","trigger_type":"4B","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":12830.0,"outcome":"counterexample_content_cost_high_MAE","classification":"counterexample","residual":"C27 drama/studio label must require production-cost discipline and SLL/Megabox margin bridge before Stage2/Yellow","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_DRAMA_THEATER_CONTENT_COST_MARGIN_BRIDGE","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","calibration_usable":true,"source_ids":["SRC_CONTENTREE_Q2_2024"]}
{"case_id":"C27-R8-L100-263720-20240509","symbol":"263720","name":"D&C Media","trigger_family":"solo_leveling_IP_owner_readthrough_without_economics_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":34450.0,"outcome":"counterexample_proxy_readthrough_high_MAE","classification":"counterexample","residual":"C27 webtoon IP owner requires explicit royalty/revenue-share/season monetization bridge before Yellow","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_WEBTOON_IP_OWNER_READTHROUGH_VS_ECONOMIC_BRIDGE","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","calibration_usable":true,"source_ids":["SRC_DNC_SOLO_IP_PROXY","SRC_NETMARBLE_SOLO_LAUNCH"]}
```

## 6. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","case_id":"C27-R8-L100-352820-20241202","symbol":"352820","name":"HYBE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_PORTFOLIO_TOUR_PLATFORM_IP_RECOVERY_BRIDGE","trigger_family":"kpop_portfolio_tour_platform_recovery_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-02","entry_date":"2024-12-02","entry_price":189800.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv:2024-12-02 close=189800","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":18.28,"MAE_30D_pct":-4.58,"MFE_90D_pct":38.57,"MAE_90D_pct":-4.58,"MFE_180D_pct":70.18,"MAE_180D_pct":-4.58,"peak_30D_date":"2025-01-15","trough_30D_date":"2024-12-09","peak_90D_date":"2025-02-20","trough_90D_date":"2024-12-09","peak_180D_date":"2025-07-02","trough_180D_date":"2024-12-09","end_30D_date":"2025-01-15","end_90D_date":"2025-04-16","end_180D_date":"2025-08-28","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass_no_entry_to_D180_overlap_detected; tradable_discontinuity_screen=pass","source_proxy_only":true,"evidence_url_pending":true,"e2r_current_profile_expected_stage":"Stage2-Actionable","e2r_observed_alignment":"positive_recovery_after_governance_overhang","current_profile_error":true,"residual_contribution":"C27 can miss structural recovery when global artist portfolio plus platform/tour bridge emerges after governance-discount reset","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|352820|Stage2-Actionable|2024-12-02","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","source_ids":["SRC_HYBE_EXPANDED_RIGHTS_Q3_2024_PROXY"]}
{"row_type":"trigger","case_id":"C27-R8-L100-035900-20241114","symbol":"035900","name":"JYP Ent.","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_GLOBAL_TOUR_ALBUM_MD_MONETIZATION_BRIDGE","trigger_family":"kpop_global_tour_album_md_recovery_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-14","entry_date":"2024-11-14","entry_price":56800.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2024.csv:2024-11-14 close=56800","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":42.61,"MAE_30D_pct":-1.06,"MFE_90D_pct":53.87,"MAE_90D_pct":-1.06,"MFE_180D_pct":53.87,"MAE_180D_pct":-1.06,"peak_30D_date":"2024-12-02","trough_30D_date":"2024-11-15","peak_90D_date":"2025-02-20","trough_90D_date":"2024-11-15","peak_180D_date":"2025-02-20","trough_180D_date":"2024-11-15","end_30D_date":"2024-12-26","end_90D_date":"2025-03-31","end_180D_date":"2025-08-11","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass_no_entry_to_D180_overlap_detected; tradable_discontinuity_screen=pass","source_proxy_only":true,"evidence_url_pending":true,"e2r_current_profile_expected_stage":"Stage2-Actionable","e2r_observed_alignment":"positive_clean_low_MAE","current_profile_error":true,"residual_contribution":"C27 should allow Actionable when K-pop label has repeat album/tour schedule plus low drawdown confirmation, but not Green without margin bridge","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|035900|Stage2-Actionable|2024-11-14","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","source_ids":["SRC_JYP_PIPELINE_PROXY"]}
{"row_type":"trigger","case_id":"C27-R8-L100-041510-20241108","symbol":"041510","name":"SM Entertainment","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_MULTI_ARTIST_CONCERT_PIPELINE_MONETIZATION_BRIDGE","trigger_family":"multi_artist_concert_pipeline_revenue_bridge","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-08","entry_date":"2024-11-08","entry_price":74800.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2024.csv:2024-11-08 close=74800","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.65,"MAE_30D_pct":-8.42,"MFE_90D_pct":44.12,"MAE_90D_pct":-10.16,"MFE_180D_pct":103.88,"MAE_180D_pct":-10.16,"peak_30D_date":"2024-11-28","trough_30D_date":"2024-11-12","peak_90D_date":"2025-02-20","trough_90D_date":"2025-01-10","peak_180D_date":"2025-07-02","trough_180D_date":"2025-01-10","end_30D_date":"2024-12-19","end_90D_date":"2025-03-25","end_180D_date":"2025-08-05","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass_no_entry_to_D180_overlap_detected; tradable_discontinuity_screen=pass","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"Stage3-Yellow","e2r_observed_alignment":"positive_verified_pipeline","current_profile_error":false,"residual_contribution":"verified tour schedule plus multi-artist pipeline is the C27 positive control; block only if margin/revision is absent after the pipeline","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|041510|Stage3-Yellow|2024-11-08","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","source_ids":["SRC_SM_3Q24_SCRIPT"]}
{"row_type":"trigger","case_id":"C27-R8-L100-122870-20241112","symbol":"122870","name":"YG Entertainment","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_WORLD_TOUR_COMEBACK_OPTION_BRIDGE","trigger_family":"blackpink_world_tour_comeback_option_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-12","entry_date":"2024-11-12","entry_price":43150.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/122/122870/2024.csv:2024-11-12 close=43150","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":19.12,"MAE_30D_pct":-1.51,"MFE_90D_pct":56.89,"MAE_90D_pct":-1.51,"MFE_180D_pct":124.57,"MAE_180D_pct":-1.51,"peak_30D_date":"2024-11-25","trough_30D_date":"2024-11-12","peak_90D_date":"2025-03-26","trough_90D_date":"2024-11-12","peak_180D_date":"2025-07-02","trough_180D_date":"2024-11-12","end_30D_date":"2024-12-23","end_90D_date":"2025-03-27","end_180D_date":"2025-08-07","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass_no_entry_to_D180_overlap_detected; tradable_discontinuity_screen=pass","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"Stage2-Actionable","e2r_observed_alignment":"positive_option_repricing","current_profile_error":true,"residual_contribution":"C27 needs to treat comeback/tour option as Actionable first; Yellow only when schedule/ticketing/album economics become visible","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|122870|Stage2-Actionable|2024-11-12","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","source_ids":["SRC_YG_BLACKPINK_2025_COMEBACK_TOUR"]}
{"row_type":"trigger","case_id":"C27-R8-L100-251270-20240509","symbol":"251270","name":"Netmarble","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_WEBTOON_TO_GAME_ONE_TITLE_LAUNCH_RETENTION_BRIDGE","trigger_family":"solo_leveling_global_launch_vs_retention_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":64800.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv:2024-05-09 close=64800","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":11.73,"MAE_30D_pct":-17.59,"MFE_90D_pct":11.73,"MAE_90D_pct":-19.14,"MFE_180D_pct":11.73,"MAE_180D_pct":-34.65,"peak_30D_date":"2024-05-10","trough_30D_date":"2024-06-21","peak_90D_date":"2024-05-10","trough_90D_date":"2024-06-24","peak_180D_date":"2024-05-10","trough_180D_date":"2025-02-03","end_30D_date":"2024-06-21","end_90D_date":"2024-09-19","end_180D_date":"2025-02-06","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass_no_entry_to_D180_overlap_detected; tradable_discontinuity_screen=pass","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"Stage2-Actionable","e2r_observed_alignment":"counterexample_one_title_fade","current_profile_error":true,"residual_contribution":"one-hit global game launch requires retention cohort, payer mix, or next-title bridge before positive stage promotion","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|251270|Stage2-Actionable|2024-05-09","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","source_ids":["SRC_NETMARBLE_SOLO_LAUNCH","SRC_NETMARBLE_SOLO_REVENUE"]}
{"row_type":"trigger","case_id":"C27-R8-L100-263750-20240822","symbol":"263750","name":"Pearl Abyss","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_CONSOLE_GAME_EVENT_DEMO_RELEASE_DATE_REVENUE_BRIDGE","trigger_family":"crimson_desert_gamescom_demo_without_revenue_bridge","trigger_type":"4B","trigger_date":"2024-08-22","entry_date":"2024-08-22","entry_price":42050.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv:2024-08-22 close=42050","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.04,"MAE_30D_pct":-24.14,"MFE_90D_pct":4.04,"MAE_90D_pct":-36.39,"MFE_180D_pct":4.04,"MAE_180D_pct":-36.39,"peak_30D_date":"2024-08-22","trough_30D_date":"2024-09-04","peak_90D_date":"2024-08-22","trough_90D_date":"2024-12-27","peak_180D_date":"2024-08-22","trough_180D_date":"2024-12-27","end_30D_date":"2024-10-10","end_90D_date":"2025-01-07","end_180D_date":"2025-05-23","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass_no_entry_to_D180_overlap_detected; tradable_discontinuity_screen=pass","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"4B","e2r_observed_alignment":"counterexample_event_demo_high_MAE","current_profile_error":false,"residual_contribution":"trailer/playable-demo IP quality without launch economics remains 4B watch; full 4B/4C requires schedule or revenue thesis break","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|263750|4B|2024-08-22","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","source_ids":["SRC_PEARLABYSS_GAMESCOM_2024"]}
{"row_type":"trigger","case_id":"C27-R8-L100-036420-20240516","symbol":"036420","name":"Contentree JoongAng","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_DRAMA_THEATER_CONTENT_COST_MARGIN_BRIDGE","trigger_family":"content_theater_recovery_without_margin_bridge","trigger_type":"4B","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":12830.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/036/036420/2024.csv:2024-05-16 close=12830","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.57,"MAE_30D_pct":-14.11,"MFE_90D_pct":2.57,"MAE_90D_pct":-37.33,"MFE_180D_pct":2.57,"MAE_180D_pct":-42.17,"peak_30D_date":"2024-05-27","trough_30D_date":"2024-06-27","peak_90D_date":"2024-05-27","trough_90D_date":"2024-08-05","peak_180D_date":"2024-05-27","trough_180D_date":"2025-02-05","end_30D_date":"2024-06-27","end_90D_date":"2024-09-25","end_180D_date":"2025-02-12","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass_no_entry_to_D180_overlap_detected; tradable_discontinuity_screen=pass","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"4B","e2r_observed_alignment":"counterexample_content_cost_high_MAE","current_profile_error":true,"residual_contribution":"C27 drama/studio label must require production-cost discipline and SLL/Megabox margin bridge before Stage2/Yellow","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|036420|4B|2024-05-16","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","source_ids":["SRC_CONTENTREE_Q2_2024"]}
{"row_type":"trigger","case_id":"C27-R8-L100-263720-20240509","symbol":"263720","name":"D&C Media","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_WEBTOON_IP_OWNER_READTHROUGH_VS_ECONOMIC_BRIDGE","trigger_family":"solo_leveling_IP_owner_readthrough_without_economics_bridge","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":34450.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/263/263720/2024.csv:2024-05-09 close=34450","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":8.13,"MAE_30D_pct":-32.22,"MFE_90D_pct":8.13,"MAE_90D_pct":-53.53,"MFE_180D_pct":8.13,"MAE_180D_pct":-53.53,"peak_30D_date":"2024-05-10","trough_30D_date":"2024-06-21","peak_90D_date":"2024-05-10","trough_90D_date":"2024-09-09","peak_180D_date":"2024-05-10","trough_180D_date":"2024-09-09","end_30D_date":"2024-06-21","end_90D_date":"2024-09-19","end_180D_date":"2025-02-06","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass_no_entry_to_D180_overlap_detected; tradable_discontinuity_screen=pass","source_proxy_only":true,"evidence_url_pending":true,"e2r_current_profile_expected_stage":"Stage2-Actionable","e2r_observed_alignment":"counterexample_proxy_readthrough_high_MAE","current_profile_error":true,"residual_contribution":"C27 webtoon IP owner requires explicit royalty/revenue-share/season monetization bridge before Yellow","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|263720|Stage2-Actionable|2024-05-09","duplicate_check":"pass_new_trigger_family_or_new_symbol_vs_C27_loop99","source_ids":["SRC_DNC_SOLO_IP_PROXY","SRC_NETMARBLE_SOLO_LAUNCH"]}
```

## 7. Score simulation rows

The following is a research-only proxy simulation. It does not inspect or patch production code. It only records how the current calibrated profile could still misclassify C27 bridges versus label spikes.

```jsonl
{"row_type":"score_simulation","case_id":"C27-R8-L100-352820-20241202","symbol":"352820","trigger_type":"Stage2-Actionable","baseline_total_proxy":69.1,"current_profile_total_proxy":65.6,"evidence_quality":82,"revenue_bridge":76,"margin_bridge":64,"revision_visibility":62,"valuation_risk":54,"price_momentum":75,"red_team_risk":46,"suggested_stage":"Stage2-Actionable_to_Yellow_when_platform_or_tour_revenue_revision_confirms","score_return_alignment":"positive_recovery_after_governance_overhang"}
{"row_type":"score_simulation","case_id":"C27-R8-L100-035900-20241114","symbol":"035900","trigger_type":"Stage2-Actionable","baseline_total_proxy":69.1,"current_profile_total_proxy":65.6,"evidence_quality":82,"revenue_bridge":76,"margin_bridge":64,"revision_visibility":62,"valuation_risk":54,"price_momentum":75,"red_team_risk":46,"suggested_stage":"Stage2-Actionable_to_Yellow_when_repeat_album_tour_margin_bridge_confirms","score_return_alignment":"positive_clean_low_MAE"}
{"row_type":"score_simulation","case_id":"C27-R8-L100-041510-20241108","symbol":"041510","trigger_type":"Stage3-Yellow","baseline_total_proxy":72.2,"current_profile_total_proxy":68.7,"evidence_quality":82,"revenue_bridge":84,"margin_bridge":74,"revision_visibility":70,"valuation_risk":54,"price_momentum":75,"red_team_risk":42,"suggested_stage":"Stage3-Yellow_allowed; Green only after margin/revision confirmation","score_return_alignment":"positive_verified_pipeline"}
{"row_type":"score_simulation","case_id":"C27-R8-L100-122870-20241112","symbol":"122870","trigger_type":"Stage2-Actionable","baseline_total_proxy":72.2,"current_profile_total_proxy":68.7,"evidence_quality":82,"revenue_bridge":84,"margin_bridge":74,"revision_visibility":70,"valuation_risk":54,"price_momentum":75,"red_team_risk":42,"suggested_stage":"Stage2-Actionable_with_option_bridge; upgrade to Yellow after schedule/ticketing evidence","score_return_alignment":"positive_option_repricing"}
{"row_type":"score_simulation","case_id":"C27-R8-L100-251270-20240509","symbol":"251270","trigger_type":"Stage2-Actionable","baseline_total_proxy":58.8,"current_profile_total_proxy":55.3,"evidence_quality":72,"revenue_bridge":44,"margin_bridge":35,"revision_visibility":38,"valuation_risk":62,"price_momentum":58,"red_team_risk":78,"suggested_stage":"Stage2-Actionable_only; Yellow_blocked_without_retention_or_next_title_bridge","score_return_alignment":"counterexample_one_title_fade"}
{"row_type":"score_simulation","case_id":"C27-R8-L100-263750-20240822","symbol":"263750","trigger_type":"4B","baseline_total_proxy":58.8,"current_profile_total_proxy":55.3,"evidence_quality":72,"revenue_bridge":44,"margin_bridge":35,"revision_visibility":38,"valuation_risk":62,"price_momentum":58,"red_team_risk":78,"suggested_stage":"local_4B_watch; no Yellow until release_date_or_booking_bridge","score_return_alignment":"counterexample_event_demo_high_MAE"}
{"row_type":"score_simulation","case_id":"C27-R8-L100-036420-20240516","symbol":"036420","trigger_type":"4B","baseline_total_proxy":58.8,"current_profile_total_proxy":55.3,"evidence_quality":72,"revenue_bridge":44,"margin_bridge":35,"revision_visibility":38,"valuation_risk":62,"price_momentum":58,"red_team_risk":78,"suggested_stage":"4B_watch_or_stage2_blocked_until_margin_bridge","score_return_alignment":"counterexample_content_cost_high_MAE"}
{"row_type":"score_simulation","case_id":"C27-R8-L100-263720-20240509","symbol":"263720","trigger_type":"Stage2-Actionable","baseline_total_proxy":58.8,"current_profile_total_proxy":55.3,"evidence_quality":72,"revenue_bridge":44,"margin_bridge":35,"revision_visibility":38,"valuation_risk":62,"price_momentum":58,"red_team_risk":78,"suggested_stage":"Stage2-Actionable_blocked_or_low_weight_proxy_until_royalty_bridge","score_return_alignment":"counterexample_proxy_readthrough_high_MAE"}
```

## 8. Aggregate and residual contribution

```jsonl
{"row_type":"aggregate","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","trigger_row_count":8,"calibration_usable_trigger_count":8,"representative_trigger_count":8,"new_independent_case_count":8,"reused_symbol_new_trigger_family_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":8,"positive_case_count":4,"counterexample_count":4,"stage4b_case_count":2,"stage4c_case_count":0,"current_profile_error_count":6,"source_proxy_only_count":3,"evidence_url_pending_count":3,"auto_selected_coverage_gap":"C27 published index 48 + local loop99 representative 7 + loop100 representative 8 = local-session adjusted about 63; current loop is quality repair after Priority 1 fill","new_axis_proposed":"C27_verified_repeat_monetization_bridge_required_before_Yellow_or_Green_plus_one_hit_or_trailer_label_to_local_4B_watch_v2"}
```

### Interpretation

C27 should not be treated as a single “K-content/global IP” factor. The price path separates into two very different engines.

The positive engine is repeat monetization: multi-artist tours, concert/MD/platform revenue, live-service game monetization, and recurring global fandom or game traffic. HYBE, JYP, SM, YG Entertainment, and the earlier Krafton control case show that when a global IP bridge has repeated monetization lanes, the current calibrated profile can be too slow or too conservative if it waits for a fully completed new-title cycle.

The failure engine is event-only optionality. Netmarble’s Solo Leveling launch had real initial demand, but the launch row faded when the bridge stayed one-title/retention-light. Pearl Abyss had a real playable demo, but no release-date or preorder booking bridge. Contentree JoongAng and D&C Media show the same idea in drama and webtoon IP: the label can be directionally correct while issuer-level economics remain too indirect.

```text
positive_case_count = 4
counterexample_count = 4
stage4b_case_count = 2
current_profile_error_count = 6
source_proxy_only_count = 3
evidence_url_pending_count = 3
```

## 9. Shadow rule candidate

```json
{
  "row_type": "shadow_rule_candidate",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "rule_id": "C27_verified_repeat_monetization_bridge_required_before_Yellow_or_Green_plus_one_hit_or_trailer_label_to_local_4B_watch_v2",
  "rule_type": "stage_gate_and_4b_watch_guard",
  "proposal": "For C27, allow Stage2-Actionable when global IP monetization has at least one verified recurring bridge such as tour schedule, subscription/platform revenue, live-service retention, or booked distribution. Require at least two of recurring revenue bridge, margin/revision bridge, platform/traffic retention, or ticketing/preorder evidence before Stage3-Yellow/Green. Route one-title launches, trailer/demo events, or broad K-content labels without issuer economics to local 4B watch rather than positive stage promotion.",
  "applies_to": [
    "K-pop portfolio/tour/platform",
    "game live-service monetization",
    "webtoon IP owner economics",
    "drama studio platform distribution",
    "console game trailer/demo events"
  ],
  "positive_controls": ["352820", "035900", "041510", "122870"],
  "counterexample_controls": ["251270", "263750", "036420", "263720"],
  "do_not_propose_new_weight_delta": false,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 10. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C27_verified_repeat_monetization_bridge_required_before_Yellow_or_Green_plus_one_hit_or_trailer_label_to_local_4B_watch_v2
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_when_only_generic_content_or_IP_label_is_present
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
production_scoring_changed = false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent operating later, not during this research run. Do not execute this prompt unless explicitly instructed in a separate implementation session.

Input MD: e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
Task: ingest the C27 loop100 rows only after normal v12 validation. Confirm required MFE/MAE fields, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and compare against existing C27 loop99 rows. If rows pass validation, consider a shadow-only C27 rule candidate requiring verified repeat monetization bridge before Yellow/Green and routing one-hit launches, trailer/demo events, or broad IP label spikes to local 4B watch. Do not make a global threshold relaxation from this file alone.
```

## 12. Next research state

```text
completed_round = R8
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority1_fill; published index Priority 1
next_recommended_archetypes = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C27_CONTENT_IP_GLOBAL_MONETIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
