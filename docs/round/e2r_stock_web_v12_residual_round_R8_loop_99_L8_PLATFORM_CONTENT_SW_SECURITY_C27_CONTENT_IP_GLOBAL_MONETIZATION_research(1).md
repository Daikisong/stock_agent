---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 99
selected_priority_bucket: Priority 1
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: C27_GLOBAL_CONTENT_IP_MONETIZATION_REVENUE_MARGIN_PLATFORM_BRIDGE
deep_sub_archetype_id: C27_DEEP_KPOP_WEBTOON_GAME_DRAMA_IP_GLOBAL_PLATFORM_MONETIZATION_VS_ONE_HIT_OR_PRODUCTION_COST_FADE
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
output_file: e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
status: completed
---

# E2R Stock-Web V12 Residual Research — R8 / L8 / C27_CONTENT_IP_GLOBAL_MONETIZATION / loop 99

## 0. Execution compliance

This Markdown is a standalone historical calibration / sector-archetype residual research file. It is not a live stock scan, not a recommendation list, not a brokerage/API workflow, and not a `stock_agent` code patch.

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R8
selected_loop = 99
selected_priority_bucket = Priority 1
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = C27_GLOBAL_CONTENT_IP_MONETIZATION_REVENUE_MARGIN_PLATFORM_BRIDGE
deep_sub_archetype_id = C27_DEEP_KPOP_WEBTOON_GAME_DRAMA_IP_GLOBAL_PLATFORM_MONETIZATION_VS_ONE_HIT_OR_PRODUCTION_COST_FADE
stock_agent_code_accessed = false
stock_agent_src_e2r_accessed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Coverage-index selection

The No-Repeat Index still marks C27 as a Priority 1 canonical archetype: 48 rows, 2 rows short of the 50-row practical calibration band. In this session, the previously selected under-covered or near-threshold C02, C09, C14, C10, C06, C07, C11, C01, C28, C12, C05, and C23 buckets have already been handled. Therefore the remaining near-threshold L8 bucket is C27.

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
selection_reason = remaining Priority 1 gap after current-session Priority 0 / near-threshold passes
current_index_rows_before_this_loop = 48
need_to_50_before_this_loop = 2
estimated_rows_after_this_loop = 55
```

Loop selection follows the v12 output identifier rule. The visible `docs/round` listing contains `c27_r8_loop98_content_ip_global_monetization_77f57117.md`; therefore the next C27/R8 loop identifier is 99.

```text
selected_loop = 99
loop_basis = max(visible existing C27/R8 loop 98) + 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 2. Stock-Web manifest and validation scope

Manifest snapshot used for this run:

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
if entry_date not in tradable shard -> use next tradable date only when evidence timing allows
if forward 180D unavailable by manifest max_date -> calibration_usable = false
if corporate_action_candidate_dates overlap entry_date~D+180 -> calibration_usable = false
if corporate_action_candidate_dates are outside the 180D window -> 30D/90D/180D remain usable
MFE/MAE = high/low excursion from entry_price over Stock-Web tradable rows, rounded to 0.1 percentage point
```

## 3. Canonical archetype definition for this loop

C27 is not just “content stock went up.” It is a bridge test: whether an owned or controlled IP asset becomes repeatable global monetization through albums/tours, streaming, games, platforms, licensing, subscriptions, distribution, or durable operating leverage. The failure mode is equally important: one-hit launch revenue, trailer excitement, celebrity/label conflict, production-cost drag, weak replacement pipeline, or delayed release can make the price look like Stage3 before the business earns the right to be Stage3.

Mechanism chain:

```text
IP asset / fandom / title library
  -> global distribution or platform channel
  -> repeat revenue or royalty visibility
  -> margin / OP / cash-flow bridge
  -> revision durability
  -> Stage2-Actionable / Stage3-Yellow eligibility
```

Residual error pattern being tested:

```text
price-only IP excitement or one-quarter hit
  -> current profile may over-promote to Yellow
  -> later weak repeat monetization / dispute / production-cost drag
  -> local 4B watch or hard thesis-break path
```

## 4. Source universe and novelty check

No live discovery was performed. These are historical trigger cases selected to diversify C27 evidence families and avoid the hard duplicate key:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty summary:

```text
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 7
calibration_usable_case_count = 7
calibration_usable_trigger_count = 7
representative_trigger_count = 7
positive_case_count = 2
counterexample_count = 5
stage4b_case_count = 4
stage4c_case_count = 0
current_profile_error_count = 5
source_proxy_only_count = 0
evidence_url_pending_count = 0
```

Evidence families:

```text
035900 / JYP Ent. / K-pop global album-tour-pipeline monetization
352820 / HYBE / K-pop label portfolio monetization vs ADOR/NewJeans governance-IP dispute
259960 / Krafton / global game IP live-service monetization and mobile recurrence
251270 / Netmarble / webtoon-to-game one-hit launch vs repeat portfolio bridge
253450 / Studio Dragon / drama studio global platform IP vs production-cost and earnings cut drag
293490 / Kakao Games / MMORPG IP pipeline vs PC/sports weakness and estimate cuts
263750 / Pearl Abyss / trailer-driven global console IP expectation vs no release-date / delay path
```

## 5. Evidence sources used

```jsonl
{"source_id":"SRC_JYP_20230530_KB","type":"analyst_pdf","date":"2023-05-30","url":"https://rdata.kbsec.com/pdf_data/20230522092633450E.pdf","use":"JYP global artist pipeline, A2K, Twice/Stray Kids cash generation evidence; pre/post trigger business bridge context"}
{"source_id":"SRC_HYBE_20240226_JOONGANG","type":"news","date":"2024-02-26","url":"https://koreajoongangdaily.joins.com/news/2024-02-26/business/industry/HYBE-posts-record-revenue-of-218-trillion-won-with-huge-year-for-stars/1989364","use":"HYBE 2023 record revenue and artist portfolio monetization evidence"}
{"source_id":"SRC_HYBE_20240424_REUTERS","type":"news","date":"2024-04-24","url":"https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/","use":"ADOR/NewJeans dispute as IP governance and label-risk thesis break watch"}
{"source_id":"SRC_KRAFTON_20240508_GWO","type":"news","date":"2024-05-08","url":"https://gameworldobserver.com/2024/05/08/krafton-q1-2024-results-mobile-revenue-pubg-battlegrounds","use":"Q1 2024 PUBG/Battlegrounds revenue and operating profit bridge"}
{"source_id":"SRC_KRAFTON_20250211_OFFICIAL","type":"company_ir","date":"2025-02-11","url":"https://www.krafton.com/en/news/press/krafton-achieves-all-time-high-sales-and-operating-profit-in-2024/","use":"2024 full-year monetization persistence confirmation"}
{"source_id":"SRC_NETMARBLE_20240809_OFFICIAL","type":"company_ir","date":"2024-08-09","url":"https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=5044","use":"Q2 2024 Solo Leveling: ARISE contribution and profit turnaround evidence"}
{"source_id":"SRC_NETMARBLE_20240808_YONHAP","type":"news","date":"2024-08-08","url":"https://en.yna.co.kr/view/AEN20240808009400320","use":"Q2 2024 profit swing from Solo Leveling: ARISE; one-hit/repeat-risk framing"}
{"source_id":"SRC_STUDIODRAGON_20240415_SAMSUNG","type":"analyst_report","date":"2024-04-15","url":"https://www.samsungpop.com/common.do?cmd=down&saveKey=research.pdf&contentType=application/pdf&inlineYn=Y&fileName=2020/2024041508260461K_02_04.pdf","use":"Studio Dragon 2024 earnings forecast cut and weak 1Q setup"}
{"source_id":"SRC_KAKAOGAMES_20230802_MIRAE","type":"analyst_pdf","date":"2023-08-02","url":"https://securities.miraeasset.com/bbs/download/2111804.pdf?attachmentId=2111804","use":"Kakao Games earnings estimate cuts despite global story option"}
{"source_id":"SRC_PEARLABYSS_20230822_OFFICIAL","type":"company_pr","date":"2023-08-22","url":"https://www.pearlabyss.com/en-US/Board/Detail?_boardNo=14001","use":"Crimson Desert Gamescom 2023 trailer event"}
{"source_id":"SRC_PEARLABYSS_20230822_WINDOWS_CENTRAL","type":"news","date":"2023-08-22","url":"https://www.windowscentral.com/gaming/crimson-desert-gets-a-new-trailer-at-gamescom-2023-and-still-no-release-date","use":"Crimson Desert trailer with no confirmed release date; price-only IP event risk"}
```

## 6. Machine-readable case rows JSONL

```jsonl
{"case_id":"C27-R8-L99-035900-20230530","symbol":"035900","name":"JYP Ent.","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_GLOBAL_ARTIST_PIPELINE_MONETIZATION","trigger_family":"artist_pipeline_album_tour_cash_generation","primary_trigger_type":"Stage3-Yellow","evidence_date":"2023-05-30","entry_date":"2023-05-30","entry_price":122200.0,"outcome_class":"positive_then_local_4b_watch","calibration_usable":true,"novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|035900|Stage3-Yellow|2023-05-30","duplicate_check":"pass_new_symbol_trigger_family_for_this_loop","residual_failure_mode":"album_tour_cash_generation_positive_but_peak_multiple_and_physical_album_cycle_requires_repeat_streaming_or_platform_bridge","source_ids":["SRC_JYP_20230530_KB"]}
{"case_id":"C27-R8-L99-352820-20240226","symbol":"352820","name":"HYBE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_LABEL_PORTFOLIO_MONETIZATION_VS_IP_GOVERNANCE_DISPUTE","trigger_family":"record_revenue_artist_portfolio_then_label_dispute","primary_trigger_type":"Stage3-Yellow","evidence_date":"2024-02-26","entry_date":"2024-02-26","entry_price":217500.0,"outcome_class":"counterexample_local_4b_watch","calibration_usable":true,"novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|352820|Stage3-Yellow|2024-02-26","duplicate_check":"pass_new_symbol_trigger_family_for_this_loop","residual_failure_mode":"record_revenue_not_enough_when_label_control_and_artist_contract_trust_break_emerge","source_ids":["SRC_HYBE_20240226_JOONGANG","SRC_HYBE_20240424_REUTERS"]}
{"case_id":"C27-R8-L99-259960-20240508","symbol":"259960","name":"Krafton","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_LIVE_SERVICE_GLOBAL_REVENUE_MARGIN_BRIDGE","trigger_family":"pubg_mobile_live_service_operating_leverage","primary_trigger_type":"Stage2-Actionable","evidence_date":"2024-05-08","entry_date":"2024-05-08","entry_price":260000.0,"outcome_class":"positive_missed_structural","calibration_usable":true,"novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|259960|Stage2-Actionable|2024-05-08","duplicate_check":"pass_new_symbol_trigger_family_for_this_loop","residual_failure_mode":"current_profile_may_be_too_slow_when_live_service_revenue_and_margin_bridge_are_both_verified","source_ids":["SRC_KRAFTON_20240508_GWO","SRC_KRAFTON_20250211_OFFICIAL"]}
{"case_id":"C27-R8-L99-251270-20240809","symbol":"251270","name":"Netmarble","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_WEBTOON_TO_GAME_ONE_HIT_VS_REPEAT_PORTFOLIO_BRIDGE","trigger_family":"solo_leveling_launch_profit_turnaround","primary_trigger_type":"Stage2-Actionable","evidence_date":"2024-08-09","entry_date":"2024-08-09","entry_price":61900.0,"outcome_class":"counterexample_one_hit_fade","calibration_usable":true,"novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|251270|Stage2-Actionable|2024-08-09","duplicate_check":"pass_new_symbol_trigger_family_for_this_loop","residual_failure_mode":"launch_quarter_profit_without_repeat_retention_or_next_title_bridge_fades_into_high_MAE","source_ids":["SRC_NETMARBLE_20240809_OFFICIAL","SRC_NETMARBLE_20240808_YONHAP"]}
{"case_id":"C27-R8-L99-253450-20240415","symbol":"253450","name":"Studio Dragon","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_DRAMA_STUDIO_GLOBAL_PLATFORM_IP_COST_MARGIN_BRIDGE","trigger_family":"earnings_cut_production_cost_platform_gap","primary_trigger_type":"4B","evidence_date":"2024-04-15","entry_date":"2024-04-15","entry_price":40800.0,"outcome_class":"counterexample_to_hard_4B_false_negative_risk","calibration_usable":true,"novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|253450|4B|2024-04-15","duplicate_check":"pass_new_symbol_trigger_family_for_this_loop","residual_failure_mode":"earnings_cut_and_weak_drama_margin_are_real_but_price_path_recovered_enough_to_require_local_4B_not_hard_4C","source_ids":["SRC_STUDIODRAGON_20240415_SAMSUNG"]}
{"case_id":"C27-R8-L99-293490-20230802","symbol":"293490","name":"Kakao Games","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_PIPELINE_IP_OPTION_VS_CORE_SEGMENT_DECAY","trigger_family":"earnings_cut_despite_global_story_option","primary_trigger_type":"4B","evidence_date":"2023-08-02","entry_date":"2023-08-02","entry_price":31450.0,"outcome_class":"counterexample_confirmed_local_4B","calibration_usable":true,"novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|293490|4B|2023-08-02","duplicate_check":"pass_new_symbol_trigger_family_for_this_loop","residual_failure_mode":"global_story_option_not_sufficient_when_PC_and_sports_segments_force_estimate_cuts","source_ids":["SRC_KAKAOGAMES_20230802_MIRAE"]}
{"case_id":"C27-R8-L99-263750-20230823","symbol":"263750","name":"Pearl Abyss","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_CONSOLE_GAME_TRAILER_IP_EVENT_VS_RELEASE_DATE_BRIDGE","trigger_family":"crimson_desert_trailer_without_release_date","primary_trigger_type":"4B","evidence_date":"2023-08-22","entry_date":"2023-08-23","entry_price":46300.0,"outcome_class":"counterexample_high_MAE_4B_watch","calibration_usable":true,"novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|263750|4B|2023-08-23","duplicate_check":"pass_new_symbol_trigger_family_for_this_loop","residual_failure_mode":"trailer_event_and_global_IP_option_without_release_date_or_booking_bridge_creates_high_MAE_path","source_ids":["SRC_PEARLABYSS_20230822_OFFICIAL","SRC_PEARLABYSS_20230822_WINDOWS_CENTRAL"]}
```

## 7. Machine-readable trigger rows JSONL

Every row below includes complete 30/90/180D MFE/MAE fields. Percentages are rounded to 0.1pp from Stock-Web tradable OHLC rows.

```jsonl
{"row_type":"trigger","case_id":"C27-R8-L99-035900-20230530","symbol":"035900","name":"JYP Ent.","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_GLOBAL_ARTIST_PIPELINE_MONETIZATION","trigger_type":"Stage3-Yellow","trigger_date":"2023-05-30","entry_date":"2023-05-30","entry_price":122200.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/035/035900/2023.csv:2023-05-30 close=122200","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":15.1,"MAE_30D_pct":-7.3,"MFE_90D_pct":15.1,"MAE_90D_pct":-17.3,"MFE_180D_pct":15.1,"MAE_180D_pct":-18.5,"peak_30D_date":"2023-06-21","peak_90D_date":"2023-06-21","peak_180D_date":"2023-06-21","trough_30D_date":"2023-05-30/forward_window_low_113300","trough_90D_date":"2023-09-xx","trough_180D_date":"2023-10-26","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass; latest candidate 2013-10-31 outside entry~D+180","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"Stage3-Yellow","e2r_observed_alignment":"partly_correct_but_should_attach_local_4B_watch_after_peak_if_no_repeat_platform_bridge","current_profile_error":true,"residual_contribution":"C27_positive_but_peak_multiple_requires_repeat_monetization_bridge"}
{"row_type":"trigger","case_id":"C27-R8-L99-352820-20240226","symbol":"352820","name":"HYBE","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_KPOP_LABEL_PORTFOLIO_MONETIZATION_VS_IP_GOVERNANCE_DISPUTE","trigger_type":"Stage3-Yellow","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":217500.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv:2024-02-26 close=217500","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":6.7,"MAE_30D_pct":-13.6,"MFE_90D_pct":9.7,"MAE_90D_pct":-13.6,"MFE_180D_pct":9.7,"MAE_180D_pct":-23.9,"peak_30D_date":"2024-04-19","peak_90D_date":"2024-04-22","peak_180D_date":"2024-04-22","trough_30D_date":"2024-03-05","trough_90D_date":"2024-03-05","trough_180D_date":"2024-10-02","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass; no candidate dates","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"Stage3-Yellow","e2r_observed_alignment":"false_positive_to_local_4B_watch","current_profile_error":true,"residual_contribution":"label_control_and_artist_contract_trust_break_should_cap_C27_green_even_after_record_revenue"}
{"row_type":"trigger","case_id":"C27-R8-L99-259960-20240508","symbol":"259960","name":"Krafton","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_LIVE_SERVICE_GLOBAL_REVENUE_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-08","entry_date":"2024-05-08","entry_price":260000.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv:2024-05-08 close=260000","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.2,"MAE_30D_pct":-7.5,"MFE_90D_pct":36.5,"MAE_90D_pct":-7.5,"MFE_180D_pct":36.5,"MAE_180D_pct":-7.5,"peak_30D_date":"2024-06-13","peak_90D_date":"2024-08-22","peak_180D_date":"2024-08-22","trough_30D_date":"2024-05-28","trough_90D_date":"2024-05-28","trough_180D_date":"2024-05-28","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass; no candidate dates","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"Stage2-Actionable","e2r_observed_alignment":"missed_structural_positive_if_profile_waits_for_too_many_new_IP_signals","current_profile_error":true,"residual_contribution":"verified_live_service_revenue_margin_bridge_can_deserve_C27_Actionable_before_new_title_release"}
{"row_type":"trigger","case_id":"C27-R8-L99-251270-20240809","symbol":"251270","name":"Netmarble","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_WEBTOON_TO_GAME_ONE_HIT_VS_REPEAT_PORTFOLIO_BRIDGE","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-09","entry_date":"2024-08-09","entry_price":61900.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv:2024-08-09 close=61900","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.7,"MAE_30D_pct":-11.1,"MFE_90D_pct":3.7,"MAE_90D_pct":-25.5,"MFE_180D_pct":3.7,"MAE_180D_pct":-25.5,"peak_30D_date":"2024-08-16","peak_90D_date":"2024-08-16","peak_180D_date":"2024-08-16","trough_30D_date":"2024-09-09","trough_90D_date":"2024-11-15","trough_180D_date":"2024-11-15","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass; no candidate dates","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"Stage2-Actionable","e2r_observed_alignment":"false_positive_one_hit_launch_fade","current_profile_error":true,"residual_contribution":"profit_turnaround_from_one_title_needs_retention_or_next_title_bridge_before_Yellow"}
{"row_type":"trigger","case_id":"C27-R8-L99-253450-20240415","symbol":"253450","name":"Studio Dragon","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_DRAMA_STUDIO_GLOBAL_PLATFORM_IP_COST_MARGIN_BRIDGE","trigger_type":"4B","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":40800.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv:2024-04-15 close=40800","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":13.8,"MAE_30D_pct":-2.2,"MFE_90D_pct":16.1,"MAE_90D_pct":-15.9,"MFE_180D_pct":23.5,"MAE_180D_pct":-16.2,"peak_30D_date":"2024-05-14","peak_90D_date":"2024-05-27","peak_180D_date":"2024-12-02","trough_30D_date":"2024-04-16","trough_90D_date":"2024-08-14","trough_180D_date":"2024-08-14","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass; no candidate dates in profile window","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"4B","e2r_observed_alignment":"4B_should_be_local_not_hard_because_price_recovered_before_hard_4C_confirmation","current_profile_error":true,"residual_contribution":"earnings_cut_drama_IP_case_requires_4B_local_vs_full_split_not_automatic_hard_4C"}
{"row_type":"trigger","case_id":"C27-R8-L99-293490-20230802","symbol":"293490","name":"Kakao Games","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_PIPELINE_IP_OPTION_VS_CORE_SEGMENT_DECAY","trigger_type":"4B","trigger_date":"2023-08-02","entry_date":"2023-08-02","entry_price":31450.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2023.csv:2023-08-02 close=31450","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.7,"MAE_30D_pct":-12.2,"MFE_90D_pct":1.7,"MAE_90D_pct":-26.7,"MFE_180D_pct":1.7,"MAE_180D_pct":-36.5,"peak_30D_date":"2023-08-07","peak_90D_date":"2023-08-07","peak_180D_date":"2023-08-07","trough_30D_date":"2023-08-18","trough_90D_date":"2023-11-01","trough_180D_date":"2024-04-15","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass; no candidate dates","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"4B","e2r_observed_alignment":"correct_local_4B_counterexample_to_global_story_hype","current_profile_error":false,"residual_contribution":"C27_pipeline_story_must_not_offset_confirmed_core_segment_estimate_cuts_without_bookings_or_revenue_bridge"}
{"row_type":"trigger","case_id":"C27-R8-L99-263750-20230823","symbol":"263750","name":"Pearl Abyss","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_CONSOLE_GAME_TRAILER_IP_EVENT_VS_RELEASE_DATE_BRIDGE","trigger_type":"4B","trigger_date":"2023-08-22","entry_date":"2023-08-23","entry_price":46300.0,"entry_price_source_row":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2023.csv:2023-08-23 close=46300","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":6.9,"MAE_30D_pct":-3.5,"MFE_90D_pct":15.8,"MAE_90D_pct":-18.5,"MFE_180D_pct":15.8,"MAE_180D_pct":-41.3,"peak_30D_date":"2023-09-04","peak_90D_date":"2023-11-08","peak_180D_date":"2023-11-08","trough_30D_date":"2023-08-25","trough_90D_date":"2023-11-30","trough_180D_date":"2024-04-15","calibration_usable":true,"representative_for_aggregate":true,"corporate_action_window_check":"pass; only profile candidate 2021-04-16, outside entry~D+180","source_proxy_only":false,"evidence_url_pending":false,"e2r_current_profile_expected_stage":"4B","e2r_observed_alignment":"high_MAE_4B_watch_correct_but_full_4B_needs_release_date_or_preorder_booking_bridge","current_profile_error":false,"residual_contribution":"trailer_without_release_date_is_not_C27_positive_bridge_even_when_IP_quality_looks_global"}
```

## 8. Raw component score simulation JSONL

The rows below are shadow simulations only. They do not change production scoring.

```jsonl
{"row_type":"score_simulation","case_id":"C27-R8-L99-035900-20230530","symbol":"035900","trigger_type":"Stage3-Yellow","baseline_total_proxy":79.0,"current_profile_total_proxy":76.5,"evidence_quality":78,"revenue_bridge":82,"margin_bridge":72,"revision_visibility":66,"valuation_risk":54,"price_momentum":88,"red_team_risk":58,"suggested_stage":"Stage3-Yellow_with_local_4B_watch_if_repeat_platform_bridge_missing","score_return_alignment":"mixed_positive_then_drawdown"}
{"row_type":"score_simulation","case_id":"C27-R8-L99-352820-20240226","symbol":"352820","trigger_type":"Stage3-Yellow","baseline_total_proxy":81.0,"current_profile_total_proxy":75.5,"evidence_quality":82,"revenue_bridge":84,"margin_bridge":65,"revision_visibility":60,"valuation_risk":52,"price_momentum":68,"red_team_risk":78,"suggested_stage":"Stage2-Actionable_or_Yellow_capped_by_IP_governance_watch","score_return_alignment":"false_positive_high_MAE"}
{"row_type":"score_simulation","case_id":"C27-R8-L99-259960-20240508","symbol":"259960","trigger_type":"Stage2-Actionable","baseline_total_proxy":73.0,"current_profile_total_proxy":78.0,"evidence_quality":86,"revenue_bridge":88,"margin_bridge":87,"revision_visibility":76,"valuation_risk":62,"price_momentum":70,"red_team_risk":45,"suggested_stage":"Stage2-Actionable_to_Yellow_when_margin_revision_confirms","score_return_alignment":"positive_missed_structural"}
{"row_type":"score_simulation","case_id":"C27-R8-L99-251270-20240809","symbol":"251270","trigger_type":"Stage2-Actionable","baseline_total_proxy":76.0,"current_profile_total_proxy":72.0,"evidence_quality":79,"revenue_bridge":75,"margin_bridge":73,"revision_visibility":49,"valuation_risk":55,"price_momentum":82,"red_team_risk":72,"suggested_stage":"Stage2-Actionable_only; Yellow_blocked_without_retention_or_next_title_bridge","score_return_alignment":"one_hit_fade_high_MAE"}
{"row_type":"score_simulation","case_id":"C27-R8-L99-253450-20240415","symbol":"253450","trigger_type":"4B","baseline_total_proxy":61.0,"current_profile_total_proxy":59.0,"evidence_quality":72,"revenue_bridge":46,"margin_bridge":38,"revision_visibility":34,"valuation_risk":61,"price_momentum":42,"red_team_risk":69,"suggested_stage":"local_4B_watch_not_hard_4C_until_cashflow_or_orderbook_thesis_break_confirms","score_return_alignment":"4B_too_hard_risk"}
{"row_type":"score_simulation","case_id":"C27-R8-L99-293490-20230802","symbol":"293490","trigger_type":"4B","baseline_total_proxy":58.0,"current_profile_total_proxy":57.0,"evidence_quality":76,"revenue_bridge":42,"margin_bridge":36,"revision_visibility":31,"valuation_risk":63,"price_momentum":36,"red_team_risk":74,"suggested_stage":"4B_watch_confirmed; block_positive_stage_until_core_decay_reverses","score_return_alignment":"correct_counterexample"}
{"row_type":"score_simulation","case_id":"C27-R8-L99-263750-20230823","symbol":"263750","trigger_type":"4B","baseline_total_proxy":68.0,"current_profile_total_proxy":61.0,"evidence_quality":70,"revenue_bridge":28,"margin_bridge":25,"revision_visibility":35,"valuation_risk":59,"price_momentum":75,"red_team_risk":82,"suggested_stage":"4B_watch; trailer_event_without_release_date_not_positive_bridge","score_return_alignment":"high_MAE_after_event_hype"}
```

## 9. Aggregate rows JSONL

```jsonl
{"row_type":"aggregate","selected_round":"R8","selected_loop":99,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GLOBAL_CONTENT_IP_MONETIZATION_REVENUE_MARGIN_PLATFORM_BRIDGE","usable_trigger_rows":7,"representative_trigger_rows":7,"positive_cases":2,"counterexample_cases":5,"stage4b_cases":4,"stage4c_cases":0,"current_profile_error_count":5,"median_MFE_30D_pct":4.2,"median_MAE_30D_pct":-7.5,"median_MFE_90D_pct":9.7,"median_MAE_90D_pct":-17.3,"median_MFE_180D_pct":15.1,"median_MAE_180D_pct":-23.9,"main_residual":"C27 needs verified repeat monetization, release/booking, retention, or margin bridge before Yellow/Green; price-only IP events should stay local 4B watch.","calibration_contribution":"canonical_archetype_rule_candidate"}
```

## 10. Shadow weight / rule candidate JSONL

```jsonl
{"row_type":"shadow_weight","axis":"stage2_required_bridge","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","proposal":"For C27 Stage2-Actionable, require at least one verified bridge among recurring revenue retention, launch revenue plus margin, platform distribution monetization, royalty/booking visibility, or contract/artist-rights stability.","suggested_delta":0.0,"production_change_now":false,"evidence_cases":["259960","251270","293490","263750"]}
{"row_type":"shadow_weight","axis":"local_4b_watch_guard","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","proposal":"For C27, price-only trailer, single title launch, or record revenue without governance/retention stability should route to local 4B watch rather than full positive stage.","suggested_delta":0.0,"production_change_now":false,"evidence_cases":["352820","251270","253450","263750"]}
{"row_type":"shadow_weight","axis":"price_only_blowoff_blocks_positive_stage","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","proposal":"Block Stage3-Yellow/Green if IP excitement is not accompanied by monetization bridge; upgrade only after repeat revenue, retention, or margin revision is visible.","suggested_delta":0.0,"production_change_now":false,"evidence_cases":["035900","251270","263750"]}
{"row_type":"shadow_weight","axis":"C27_verified_recurring_monetization_bridge","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","proposal":"New C27-specific axis: verified recurring monetization bridge required before Yellow or Green, with exception for Krafton-like live-service margin bridge already proven in quarterly results.","suggested_delta":0.15,"production_change_now":false,"evidence_cases":["259960","035900","352820","251270","293490"]}
```

## 11. Interpretation

C27 behaves like a theater where the applause can arrive before the box office is counted. The price often hears the trailer, the fandom, the headline, or the record revenue first. E2R should not confuse that first roar with durable monetization. The durable version has a machine behind the stage: distribution, retention, artist/IP rights, margin, release schedule, and repeat title pipeline.

### Positive patterns

1. **Krafton** is the cleanest positive. The Q1 2024 trigger had live-service revenue and operating-profit evidence, not just new-title hope. The 90D/180D MFE path shows why C27 should allow Actionable-to-Yellow progression when a proven IP is already producing revenue and margin.
2. **JYP** was initially positive because the cash-cow artist and global pipeline evidence was real. But the drawdown after the 2023 peak shows that even successful K-pop IP needs a repeat monetization bridge and valuation guard. C27 Green should not be unlocked by fandom scale alone.

### Counterexample patterns

1. **HYBE** had record revenue, but ADOR/NewJeans label conflict turned IP ownership/control into a risk factor. C27 needs an explicit artist-rights / label-governance red-team gate.
2. **Netmarble** shows the one-hit launch problem. A single webtoon-to-game success can swing profit, but without retention, next-title, or platform portfolio bridge, the price path becomes high-MAE.
3. **Studio Dragon** shows why a 4B trigger should often remain local. Earnings cuts matter, but hard 4C needs a thesis break beyond one forecast reset.
4. **Kakao Games** confirms that “global story later” is not a bridge when core PC/sports weakness is already cutting estimates.
5. **Pearl Abyss** shows that trailer excitement without release date / booking / preorder bridge creates a high-MAE path. This is not a positive C27 signal; it is a local 4B watch.

## 12. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C27_verified_recurring_monetization_bridge_required_before_Yellow_or_Green_plus_one_hit_event_and_label_dispute_to_4B_watch
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
existing_axis_weakened = null
stage3_green_global_threshold_change = forbidden_not_proposed
production_scoring_changed = false
```

Practical rule candidate:

```text
For C27_CONTENT_IP_GLOBAL_MONETIZATION:
  Stage2-Actionable may be allowed when at least one verified non-price bridge exists:
    - repeat revenue or live-service retention
    - platform/distribution monetization evidence
    - royalty / license / booking visibility
    - margin or OP revision tied to IP monetization
    - artist/IP-rights stability for K-pop/label cases

  Stage3-Yellow requires at least two bridges, one of which must be revenue/margin/revision or retention.

  Stage3-Green must not be unlocked by trailer, fandom, record sales, ranking, or title launch alone.

  If the case is single-title launch, trailer-only, label-dispute, delayed-release, or estimate-cut driven:
    route to local_4B_watch unless a hard non-price thesis break is confirmed.
```

## 13. Narrative-only / rejected rows JSONL

No additional narrative-only rows were used for aggregate.

```jsonl
{"row_type":"narrative_only","status":"none","reason":"all seven selected trigger rows have entry_date, entry_price, complete 30/90/180D MFE/MAE, profile caveat check, and non-price evidence URL."}
```

## 14. Deferred Coding Agent Handoff Prompt — not executed

```text
You are the later batch implementation agent for Songdaiki/stock_agent.
Do not treat this MD as a live trading signal. Do not scan current candidates.
Read this file only as one v12 historical calibration artifact.

Input file:
e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md

Tasks:
1. Ingest the machine-readable case / trigger / score_simulation / aggregate / shadow_weight rows.
2. Revalidate all MFE/MAE from Songdaiki/stock-web tradable shards, using price_basis=tradable_raw and price_adjustment_status=raw_unadjusted_marcap.
3. Confirm no hard duplicate key exists:
   canonical_archetype_id + symbol + trigger_type + entry_date.
4. Do not alter global Stage3-Green thresholds based on this single loop.
5. Consider a C27-specific bridge axis only if multiple independent C27 loops confirm it:
   C27_verified_recurring_monetization_bridge_required_before_Yellow_or_Green_plus_one_hit_event_and_label_dispute_to_4B_watch.
6. If accepted, encode as a scope-limited C27 rule candidate under shadow/promotion review, not as a production patch by default.
7. Preserve the distinction between local 4B watch and full 4B/4C.
```

## 15. Next research state

```text
completed_round = R8
completed_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

