# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata
|field|value|
|---|---|
|mode|historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough|
|round|R8|
|loop|7|
|sector|플랫폼·콘텐츠·SW·보안|
|output_format|one_standalone_markdown_file|
|stock_agent_repo_access_allowed|false|
|production_scoring_changed|false|
|shadow_weight_only|true|
|created_at|2026-05-23 Asia/Seoul|

## 1. Round Scope
R8 Loop 7은 플랫폼·콘텐츠·SW·보안 중 **게임/콘텐츠 hit-cycle, launch-quality failure, event-premium software/security stock**을 V11 형식으로 재검증했다. 현재 후보 스캔이 아니라 과거 trigger-level calibration이다. `stock_agent` 레포는 열지 않았고 코드 패치도 작성하지 않았다.

## 2. Stock-Web OHLC Input / Price Source Validation
|field|value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|stock_web_repo|https://github.com/Songdaiki/stock-web|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|

Schema basis: tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`; `d=date`, `o=open`, `h=high`, `l=low`, `c=close`, `v=volume`, `a=amount`, `mc=marcap`, `s=stocks`, `m=market`. MFE/MAE are computed from actual stock-web high/low rows. The atlas is raw/unadjusted, so corporate-action-contaminated windows are blocked by default.

V11 refresh: manifest, schema, and universe headers were re-read for this loop; max_date remains 2026-02-20, and all forward windows are judged against that stock-web manifest date rather than the current calendar date.

## 3. Historical Eligibility Gate
|gate|status|
|---|---|
|entry_date in tradable shard|pass for all 5 calibration cases|
|minimum 180 forward trading days|pass for all 5 calibration cases under manifest max_date 2026-02-20|
|corporate-action contamination|pass for 5 calibration cases; 위메이드 narrative-only row blocked|
|MFE/MAE 30D/90D/180D|computed|
|1Y/2Y|computed when observed and uncontaminated; unavailable where IPO/window length or prompt-scope blocks exact 504D use|

## 4. Canonical Archetypes Tested
|archetype|cases|
|---|---|
|MOBILE_GAME_LAUNCH_TO_OPERATING_LEVERAGE|카카오게임즈 Odin|
|IP_GAME_HIT_TO_GLOBAL_RERATING|데브시스터즈 Cookie Run: Kingdom|
|TRAILER_OPTIONALITY_EVENT_PREMIUM|펄어비스 DokeV|
|LIVE_SERVICE_GAME_LAUNCH_FAILURE|엔씨소프트 Blade & Soul 2|
|POLITICAL_EVENT_PREMIUM_SOFTWARE_STOCK|안랩 political/event premium|

## 5. Case Selection Summary
|case_id|symbol|company_name|case_type|primary_archetype|best_trigger|score_price_alignment|
|---|---|---|---|---|---|---|
|R8L7_KG_ODIN_2021|293490|카카오게임즈|structural_success|MOBILE_GAME_LAUNCH_TO_OPERATING_LEVERAGE|R8L7_KG_T2_STAGE2A_ODIN_RANKING|Stage2_Actionable_beats_Green|
|R8L7_DEV_COOKIE_2021|194480|데브시스터즈|structural_success_and_4B|IP_GAME_HIT_TO_GLOBAL_RERATING|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|Stage2_Actionable_best_entry|
|R8L7_PEARL_DOKEV_2021|263750|펄어비스|event_premium_success_candidate|TRAILER_OPTIONALITY_EVENT_PREMIUM|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|event_premium_requires_guardrail|
|R8L7_NCSOFT_BNS2_2021|036570|엔씨소프트|4C_thesis_break|LIVE_SERVICE_GAME_LAUNCH_FAILURE|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL|prelaunch_Green_false_positive|
|R8L7_AHNLAB_EVENT_2022|053800|안랩|event_premium_false_positive|POLITICAL_EVENT_PREMIUM_SOFTWARE_STOCK|R8L7_AHN_T5_4B_BLOWOFF|price_moved_without_fundamental_evidence|

## 6. Evidence Source Map
|case_id|evidence_map|
|---|---|
|R8L7_KG_ODIN_2021|Odin launch day, visible ranking/traction, later earnings confirmation, 4B valuation/positioning risk.|
|R8L7_DEV_COOKIE_2021|Cookie Run: Kingdom launch, early app-market traction, download/ranking evidence, later earnings visibility, blowoff.|
|R8L7_PEARL_DOKEV_2021|Gamescom/DokeV trailer optionality, subsequent price/attention momentum, price-only blowoff watch.|
|R8L7_NCSOFT_BNS2_2021|Prelaunch franchise expectation, launch-quality/monetization disappointment, later event premium spike.|
|R8L7_AHNLAB_EVENT_2022|Founder-linked political/control premium, no EPS/OP bridge, post-event unwind.|
|R8L7_WEMADE_MIR4_2021_BLOCKED|MIR4/WEMIX narrative exists but stock-web raw window overlaps corporate-action candidates; blocked.|

## 7. Price Data Source Map
|symbol|company_name|profile_path|sample_shard_paths|
|---|---|---|---|
|293490|카카오게임즈|atlas/symbol_profiles/293/293490.json|atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv|
|194480|데브시스터즈|atlas/symbol_profiles/194/194480.json|atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv|
|263750|펄어비스|atlas/symbol_profiles/263/263750.json|atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv|
|036570|엔씨소프트|atlas/symbol_profiles/036/036570.json|atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv|
|053800|안랩|atlas/symbol_profiles/053/053800.json|atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv|

## 8. Case-by-Case Trigger Grid
|trigger_id|case_id|symbol|trigger_type|trigger_date|entry_date|entry_price|evidence_available_at_that_date|trigger_outcome_label|aggregate_group_role|
|---|---|---|---|---|---|---|---|---|---|
|R8L7_KG_T1_STAGE2_ODIN_LAUNCH|R8L7_KG_ODIN_2021|293490|Stage2|2021-06-29|2021-06-29|59700|Odin launch day and immediate launch interest were public; earnings bridge not yet confirmed.|missed_structural|representative|
|R8L7_KG_T2_STAGE2A_ODIN_RANKING|R8L7_KG_ODIN_2021|293490|Stage2-Actionable|2021-07-02|2021-07-02|71600|Launch plus visible market reaction/ranking traction; still before full quarterly confirmation.|excellent_entry|representative|
|R8L7_KG_T3_YELLOW_ODIN_SUSTAINED|R8L7_KG_ODIN_2021|293490|Stage3-Yellow|2021-08-26|2021-08-26|85400|Sustained Odin momentum was visible, but much of the repricing had already happened.|late_entry|representative|
|R8L7_KG_T4_GREEN_ODIN_CONFIRMED|R8L7_KG_ODIN_2021|293490|Stage3-Green|2021-11-16|2021-11-16|108700|Confirmed earnings/price strength arrived near the observed cycle peak.|late_green|representative|
|R8L7_KG_T5_4B_PEAK_WATCH|R8L7_KG_ODIN_2021|293490|4B|2021-11-17|2021-11-17|107900|Valuation/positioning blowoff risk after confirmed hit-game repricing.|good_full_window_4B_watch|4B_overlay_only|
|R8L7_DEV_T1_STAGE2_COOKIE_LAUNCH|R8L7_DEV_COOKIE_2021|194480|Stage2|2021-01-21|2021-01-21|17250|Cookie Run: Kingdom launch was public; early hit evidence began before earnings revision.|excellent_entry|representative|
|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|R8L7_DEV_COOKIE_2021|194480|Stage2-Actionable|2021-01-22|2021-01-22|22400|Launch plus immediate price/volume response and visible app-market traction.|excellent_entry|representative|
|R8L7_DEV_T3_YELLOW_DOWNLOADS|R8L7_DEV_COOKIE_2021|194480|Stage3-Yellow|2021-02-22|2021-02-22|58800|Download/ranking evidence was strong; profit path still not fully confirmed.|good_entry|representative|
|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE|R8L7_DEV_COOKIE_2021|194480|Stage3-Green|2021-03-25|2021-03-25|133000|By this point hit evidence and repricing were obvious, but early upside was already captured.|late_entry|representative|
|R8L7_DEV_T5_4B_BLOWOFF|R8L7_DEV_COOKIE_2021|194480|4B|2021-09-27|2021-09-27|186000|Full-window blowoff after extreme rerating and positioning heat.|good_full_window_4B_timing|4B_overlay_only|
|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|R8L7_PEARL_DOKEV_2021|263750|Stage2|2021-08-26|2021-08-26|87900|DokeV gameplay trailer created new-title optionality, but monetization/release timing remained open.|event_premium_good_entry|representative|
|R8L7_PEARL_T3_YELLOW_TRAILER_MOMENTUM|R8L7_PEARL_DOKEV_2021|263750|Stage3-Yellow|2021-10-21|2021-10-21|107500|Momentum persisted, but evidence was still option-value rather than confirmed EPS bridge.|good_entry_but_watch_only|representative|
|R8L7_PEARL_T5_4B_TRAILER_BLOWOFF|R8L7_PEARL_DOKEV_2021|263750|4B|2021-11-17|2021-11-17|141000|Price-only blowoff near full-window high without non-price slowdown confirmation.|price_only_4B_watch_not_full_exit|4B_overlay_only|
|R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|R8L7_NCSOFT_BNS2_2021|036570|Stage3-Green|2021-08-19|2021-08-19|853000|Pre-launch franchise/monetization expectation looked like Green, but launch-quality gate had not closed.|score_high_return_low_false_positive|representative|
|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL|R8L7_NCSOFT_BNS2_2021|036570|4C|2021-08-26|2021-08-26|709000|Launch-day disappointment/review and monetization-quality break damaged the original thesis.|hard_4c_success|4C_overlay_only|
|R8L7_NC_T5_NFT_METAVERSE_EVENT|R8L7_NCSOFT_BNS2_2021|036570|4B|2021-11-11|2021-11-11|786000|NFT/metaverse event spike after the core launch thesis was already damaged.|false_positive_score|4B_overlay_only|
|R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS|R8L7_AHNLAB_EVENT_2022|053800|Stage2|2022-01-05|2022-01-05|120500|Founder-linked political event premium was visible, but no software EPS rerating evidence was present.|price_moved_without_fundamental_evidence|representative|
|R8L7_AHN_T5_4B_BLOWOFF|R8L7_AHNLAB_EVENT_2022|053800|4B|2022-03-23|2022-03-23|175800|Event-premium blowoff immediately before/around observed peak; not an EPS signal.|event_premium_4B_watch|4B_overlay_only|
|R8L7_AHN_T6_EVENT_UNWIND|R8L7_AHNLAB_EVENT_2022|053800|4C|2022-03-30|2022-03-30|122800|Event premium unwind was visible, but only after intraday blowoff had already passed.|hard_4c_late|4C_overlay_only|

## 9. Trigger-Level OHLC Backtest Tables
|trigger_id|trigger_type|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MFE_1Y_pct|MFE_2Y_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|MAE_1Y_pct|peak_date|peak_price|drawdown_after_peak_pct|calibration_usable|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R8L7_KG_T1_STAGE2_ODIN_LAUNCH|Stage2|59700|77.6|77.6|94.3|94.3|94.3|-6.9|-6.9|-6.9|-22.8|2021-11-17|116000|-60.3|True|
|R8L7_KG_T2_STAGE2A_ODIN_RANKING|Stage2-Actionable|71600|48.0|48.0|62.0|62.0|62.0|-18.6|-13.7|-13.7|-35.6|2021-11-17|116000|-60.3|True|
|R8L7_KG_T3_YELLOW_ODIN_SUSTAINED|Stage3-Yellow|85400|2.6|35.8|35.8|35.8|35.8|-23.4|-27.6|-36.4|-46.0|2021-11-17|116000|-60.3|True|
|R8L7_KG_T4_GREEN_ODIN_CONFIRMED|Stage3-Green|108700|6.7|6.7|6.7|6.7|6.7|-40.8|-41.2|-57.6|-57.6|2021-11-17|116000|-60.3|True|
|R8L7_KG_T5_4B_PEAK_WATCH|4B|107900|7.5|7.5|7.5|7.5|7.5|-40.8|-40.8|-57.3|-57.3|2021-11-17|116000|-60.3|True|
|R8L7_DEV_T1_STAGE2_COOKIE_LAUNCH|Stage2|17250|300.0|833.3|1056.5|1056.5|unavailable|-12.8|-12.8|-12.8|-12.8|2021-09-27|199500|-55.6|True|
|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|Stage2-Actionable|22400|208.0|618.8|790.6|790.6|unavailable|-18.1|-18.1|-18.1|-18.1|2021-09-27|199500|-55.6|True|
|R8L7_DEV_T3_YELLOW_DOWNLOADS|Stage3-Yellow|58800|173.8|173.8|239.3|239.3|unavailable|-13.3|-13.3|-13.3|-13.3|2021-09-27|199500|-55.6|True|
|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE|Stage3-Green|133000|21.1|21.1|50.0|50.0|unavailable|-24.1|-24.1|-24.1|-33.5|2021-09-27|199500|-55.6|True|
|R8L7_DEV_T5_4B_BLOWOFF|4B|186000|7.3|7.3|7.3|7.3|unavailable|-52.4|-52.4|-55.6|-55.6|2021-09-27|199500|-55.6|True|
|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|Stage2|87900|16.0|65.2|65.2|65.2|unavailable|-11.7|-11.7|-34.9|-45.7|2021-11-17|145200|-67.1|True|
|R8L7_PEARL_T3_YELLOW_TRAILER_MOMENTUM|Stage3-Yellow|107500|35.1|35.1|35.1|35.1|unavailable|-6.0|-16.1|-46.8|-55.6|2021-11-17|145200|-67.1|True|
|R8L7_PEARL_T5_4B_TRAILER_BLOWOFF|4B|141000|3.0|3.0|3.0|3.0|unavailable|-35.7|-35.7|-59.4|-67.1|2021-11-17|145200|-67.1|True|
|R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|Stage3-Green|853000|0.8|0.8|0.8|0.8|0.8|-34.6|-34.9|-49.4|-59.3|2021-08-20|860000|-59.6|True|
|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL|4C|709000|11.1|11.1|11.1|11.1|11.1|-21.3|-21.7|-39.1|-51.0|2021-11-11|786000|-55.6|True|
|R8L7_NC_T5_NFT_METAVERSE_EVENT|4B|786000|0.0|0.0|0.0|0.0|0.0|-25.1|-33.6|-55.5|-55.5|2021-11-11|786000|-55.6|True|
|R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS|Stage2|120500|6.6|81.3|81.3|81.3|unavailable|-41.6|-47.3|-47.3|-47.3|2022-03-24|218500|-62.9|True|
|R8L7_AHN_T5_4B_BLOWOFF|4B|175800|24.3|24.3|24.3|24.3|unavailable|-44.0|-53.9|-53.9|-53.9|2022-03-24|218500|-62.9|True|
|R8L7_AHN_T6_EVENT_UNWIND|4C|122800|2.0|2.0|2.0|2.0|unavailable|-34.0|-34.0|-34.0|-34.0|2022-03-30|125300|-35.5|True|

## 10. 1D Price Path Summaries
### R8L7_KG_ODIN_2021
|offset|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+0|0.0|2.7|-18.6|
|D+10|13.3|48.0|-13.7|
|D+30|19.8|48.0|-13.7|
|D+60|-9.1|48.0|-13.7|
|D+90|21.6|48.0|-13.7|
|D+180|-32.0|62.0|-35.6|
|D+252|unavailable|unavailable|unavailable|

### R8L7_DEV_COOKIE_2021
|offset|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+0|0.0|0.0|-18.1|
|D+10|86.2|94.2|-18.1|
|D+30|162.5|208.0|-18.1|
|D+60|397.8|618.8|-18.1|
|D+90|399.6|618.8|-18.1|
|D+180|730.4|790.6|-18.1|
|D+252|unavailable|unavailable|unavailable|

### R8L7_PEARL_DOKEV_2021
|offset|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+0|0.0|1.7|-11.7|
|D+10|-6.9|16.0|-11.7|
|D+30|7.9|16.0|-11.7|
|D+60|21.7|35.1|-11.7|
|D+90|36.5|65.2|-11.7|
|D+180|-29.0|65.2|-34.9|
|D+252|unavailable|unavailable|unavailable|

### R8L7_NCSOFT_BNS2_2021
|offset|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+0|0.0|0.8|-8.6|
|D+5|-23.8|0.8|-25.7|
|D+30|-34.0|0.8|-34.9|
|D+90|-20.2|0.8|-34.9|
|D+180|-40.4|0.8|-49.4|
|D+252|-58.5|0.8|-59.3|
|D+504|-59.3|0.8|-59.3|

### R8L7_AHNLAB_EVENT_2022
|offset|close_return_pct|high_to_date_return_pct|low_to_date_return_pct|
|---|---|---|---|
|D+0|0.0|6.6|-41.6|
|D+20|-28.9|6.6|-41.6|
|D+40|-27.0|81.3|-47.3|
|D+60|-13.3|81.3|-47.3|
|D+90|-26.6|81.3|-47.3|
|D+180|-28.3|81.3|-47.3|
|D+252|unavailable|unavailable|unavailable|

## 11. Case Trigger Comparison
|case_id|symbol|best_actual_trigger|baseline_selected_trigger|after_selected_trigger|baseline_MFE_90D_pct|after_MFE_90D_pct|baseline_MAE_90D_pct|after_MAE_90D_pct|return_improvement_90D_pct|risk_change_90D_pct|
|---|---|---|---|---|---|---|---|---|---|---|
|R8L7_KG_ODIN_2021|293490|R8L7_KG_T2_STAGE2A_ODIN_RANKING|R8L7_KG_T4_GREEN_ODIN_CONFIRMED|R8L7_KG_T2_STAGE2A_ODIN_RANKING|6.7|48.0|-41.2|-13.7|41.3|27.5|
|R8L7_DEV_COOKIE_2021|194480|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|21.1|618.8|-24.1|-18.1|597.7|6.0|
|R8L7_PEARL_DOKEV_2021|263750|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|R8L7_PEARL_T3_YELLOW_TRAILER_MOMENTUM|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|35.1|65.2|-16.1|-11.7|30.1|4.4|
|R8L7_NCSOFT_BNS2_2021|036570|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL|R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|reject_long_after_launch_quality_gate|0.8|not_applicable|-34.9|not_applicable|risk_avoidance|34.9|
|R8L7_AHNLAB_EVENT_2022|053800|R8L7_AHN_T5_4B_BLOWOFF|R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS|reject_structural_entry_event_premium_only|81.3|not_applicable|-47.3|not_applicable|false_positive_removed|47.3|

## 12. Stage2 → Stage4 Audit
- 카카오게임즈와 데브시스터즈는 Stage2/Stage2-Actionable에서 이미 리레이팅 entry가 가능했다. Green은 증거가 더 닫혔지만, 그때는 가격이라는 엘리베이터가 이미 대부분 올라간 뒤였다.
- 펄어비스는 Stage2 trailer optionality가 좋은 MFE를 만들었지만, EPS/OP bridge가 닫힌 것이 아니므로 position sizing은 Stage2-Actionable이 아니라 event-premium watch 성격이 강하다.
- 엔씨소프트는 prelaunch Green이 실패했다. launch quality gate가 닫히기 전 Green을 주면 false_positive_score가 커진다.
- 안랩은 가격이 움직였지만 소프트웨어 EPS/OP/FCF 리레이팅 evidence가 아니었다. event-premium은 별도 overlay로 분리해야 한다.


## 13. Stage3 Yellow / Green Lateness Audit
|trigger_id|trigger_type|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|green_lateness_ratio|trigger_outcome_label|
|---|---|---|---|---|---|---|---|
|R8L7_KG_T3_YELLOW_ODIN_SUSTAINED|Stage3-Yellow|2021-08-26|85400|35.8|-27.6|not_applicable|late_entry|
|R8L7_KG_T4_GREEN_ODIN_CONFIRMED|Stage3-Green|2021-11-16|108700|6.7|-41.2|0.87|late_green|
|R8L7_DEV_T3_YELLOW_DOWNLOADS|Stage3-Yellow|2021-02-22|58800|173.8|-13.3|not_applicable|good_entry|
|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE|Stage3-Green|2021-03-25|133000|21.1|-24.1|0.63|late_entry|
|R8L7_PEARL_T3_YELLOW_TRAILER_MOMENTUM|Stage3-Yellow|2021-10-21|107500|35.1|-16.1|not_applicable|good_entry_but_watch_only|
|R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|Stage3-Green|2021-08-19|853000|0.8|-34.9|1.0|score_high_return_low_false_positive|

Interpretation: 카카오게임즈 Green lateness ratio 0.87, 데브시스터즈 Green lateness ratio 0.63으로 둘 다 upside 대부분을 놓친 편이다. Stage3-Yellow는 Green보다 낫지만, hit-game cycle에서는 Stage2-Actionable이 더 좋은 entry tier였다.

## 14. 4B Timing Audit
|trigger_id|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_timing_verdict|four_b_evidence_type|
|---|---|---|---|---|---|---|---|---|
|R8L7_KG_T5_4B_PEAK_WATCH|2021-11-17|107900|7.5|-40.8|0.86|0.86|good_full_window_4B_timing|valuation_blowoff|positioning_overheat|
|R8L7_DEV_T5_4B_BLOWOFF|2021-09-27|186000|7.3|-52.4|0.93|0.93|good_full_window_4B_timing|valuation_blowoff|positioning_overheat|
|R8L7_PEARL_T5_4B_TRAILER_BLOWOFF|2021-11-17|141000|3.0|-35.7|0.93|0.93|price_only_local_4B_requires_non_price_confirmation|price_only|positioning_overheat|
|R8L7_NC_T5_NFT_METAVERSE_EVENT|2021-11-11|786000|0.0|-33.6|1.0|1.0|late_price_only_4B_after_thesis_damage|price_only|event_premium|
|R8L7_AHN_T5_4B_BLOWOFF|2022-03-23|175800|24.3|-53.9|0.56|0.56|event_premium_4B_watch_but_intraday_peak_hard_to_capture|price_only|control_premium_or_event_premium|

4B는 가격만 보고 확정하지 않는다. 카카오게임즈/데브시스터즈는 valuation blowoff + positioning overheat가 함께 있었기 때문에 full-window 4B timing으로 쓸 수 있지만, 펄어비스/안랩은 price-only 또는 event-premium 성격이 강해 full exit rule이 아니라 watch overlay로 둔다.

## 15. 4C Protection Audit
|trigger_id|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|four_c_protection_label|trigger_outcome_label|
|---|---|---|---|---|---|---|
|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL|2021-08-26|709000|11.1|-21.7|hard_4c_success|hard_4c_success|
|R8L7_AHN_T6_EVENT_UNWIND|2022-03-30|122800|2.0|-34.0|hard_4c_late|hard_4c_late|

NCSoft launch failure is a hard 4C success candidate: the old thesis broke before the later deeper drawdown. AhnLab event unwind is late because the intraday blowoff had already occurred.

## 16. Baseline Score Simulation
Component values are research proxy scores. `0` means no public support was used in this proxy component, not a claim that the business variable is literally zero.
|trigger_id|profile_id|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|selected_by_profile|MFE_90D_pct|MAE_90D_pct|score_return_alignment_label|
|---|---|---|---|---|---|---|---|---|---|
|R8L7_KG_T2_STAGE2A_ODIN_RANKING|stage2_actionable_content_hit_plus_4b_evidence_guardrail|22.5|Watch/Reject|25.4|Stage2|True|48.0|-13.7|score_mid_return_high_promote_candidate|
|R8L7_KG_T4_GREEN_ODIN_CONFIRMED|stage2_actionable_content_hit_plus_4b_evidence_guardrail|34.9|Stage2|34.9|Stage2|False|6.7|-41.2|score_low_return_low_correct_reject|
|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|stage2_actionable_content_hit_plus_4b_evidence_guardrail|26.8|Stage2|29.3|Stage2|True|618.8|-18.1|score_mid_return_high_promote_candidate|
|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE|stage2_actionable_content_hit_plus_4b_evidence_guardrail|40.6|Stage2|40.6|Stage2|False|21.1|-24.1|score_low_return_low_correct_reject|
|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|stage2_actionable_content_hit_plus_4b_evidence_guardrail|21.7|Watch/Reject|24.6|Watch/Reject|True|65.2|-11.7|score_mid_return_high_promote_candidate|
|R8L7_PEARL_T3_YELLOW_TRAILER_MOMENTUM|stage2_actionable_content_hit_plus_4b_evidence_guardrail|23.0|Watch/Reject|23.0|Watch/Reject|False|35.1|-16.1|score_low_return_low_correct_reject|
|R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|stage2_actionable_content_hit_plus_4b_evidence_guardrail|26.7|Stage2|11.2|Watch/Reject|False|0.8|-34.9|score_high_return_low_false_positive|
|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL|stage2_actionable_content_hit_plus_4b_evidence_guardrail|0|4C|0|4C|False|11.1|-21.7|score_low_return_low_correct_reject|
|R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS|stage2_actionable_content_hit_plus_4b_evidence_guardrail|12.4|Watch/Reject|6.0|Watch/Reject|False|81.3|-47.3|score_low_return_low_correct_reject|

## 17. Shadow Profile Optimization Loop
|profile_id|case_count|selected_trigger_count|avg_MFE_90D_pct|median_MFE_90D_pct|avg_MAE_90D_pct|median_MAE_90D_pct|hit_rate_MFE90_gt_20pct|bad_entry_rate_MAE90_lt_minus_15pct|false_positive_rate|missed_structural_count|late_green_count|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|baseline_current_proxy|5|5|29.0|21.1|-32.7|-34.9|0.6|1.0|0.6|2|2|reference; catches obvious Green too late and admits event-premium false positives|
|stage2_actionable_early_evidence_plus|5|3|244.0|65.2|-14.5|-13.7|1.0|0.33|0.0|0|0|best; improves upside capture and rejects NC/Ahn event false positives|
|stage3_yellow_entry_relaxed|5|3|81.6|35.8|-19.0|-16.1|1.0|0.67|0.0|1|0|useful but later than Stage2-Actionable in hit-game cycles|
|green_confirmation_timing_relaxed|5|3|81.6|35.8|-19.0|-16.1|1.0|0.67|0.0|1|0|positive but inferior to Stage2-Actionable for content hits|
|four_b_peak_timing_tuned|5|5|8.4|7.3|-41.0|-40.8|0.2|1.0|0.4|0|0|4B overlay works only with non-price blowoff evidence; price-only local 4B remains watch-only|
|four_c_thesis_break_earlier|5|2|6.6|6.6|-27.9|-27.9|0.0|1.0|0.0|0|0|validates launch-quality 4C for NC; Ahn unwind was late event-premium exit|

Best shadow profile: `stage2_actionable_content_hit_plus_4b_evidence_guardrail`. It behaves like a good scout: it moves early when the launch hit is visible, but refuses to chase political/event premium or prelaunch hype without quality confirmation.

## 18. Before / After Backtest Comparison
|case_id|baseline_selected_trigger|after_selected_trigger|baseline_entry_date|after_entry_date|baseline_entry_price|after_entry_price|baseline_MFE_90D_pct|after_MFE_90D_pct|baseline_MAE_90D_pct|after_MAE_90D_pct|reason_after_profile_selected|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R8L7_KG_ODIN_2021|R8L7_KG_T4_GREEN_ODIN_CONFIRMED|R8L7_KG_T2_STAGE2A_ODIN_RANKING|2021-11-16|2021-07-02|108700|71600|6.7|48.0|-41.2|-13.7|Launch/ranking evidence was early and public; Green arrived near peak.|
|R8L7_DEV_COOKIE_2021|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|2021-03-25|2021-01-22|133000|22400|21.1|618.8|-24.1|-18.1|Hit-game evidence was visible far before earnings-confirmed Green.|
|R8L7_PEARL_DOKEV_2021|R8L7_PEARL_T3_YELLOW_TRAILER_MOMENTUM|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|2021-10-21|2021-08-26|107500|87900|35.1|65.2|-16.1|-11.7|Trailer optionality was public and price-confirmed; still size as watch-only due EPS uncertainty.|
|R8L7_NCSOFT_BNS2_2021|R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|reject_long_after_launch_quality_gate|2021-08-19|none|853000|none|0.8|not_applicable|-34.9|not_applicable|Prelaunch hype is blocked until launch-quality gate closes; 4C triggered after failure.|
|R8L7_AHNLAB_EVENT_2022|R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS|reject_structural_entry_event_premium_only|2022-01-05|none|120500|none|81.3|not_applicable|-47.3|not_applicable|Political/control event premium lacks EPS/OP/FCF bridge; keep as event overlay not E2R entry.|

## 19. Score-Return Alignment Matrix
|alignment_label|trigger_count|avg_weighted_score_before|avg_weighted_score_after|avg_MFE_90D_pct|avg_MAE_90D_pct|verdict|
|---|---|---|---|---|---|---|
|score_mid_return_high_promote_candidate|3|23.7|26.4|244.0|-14.5|promote|
|score_low_return_low_correct_reject|5|22.2|20.9|31.1|-30.1|reject/watch|
|score_high_return_low_false_positive|1|26.7|11.2|0.8|-34.9|reject/watch|

## 20. Weight Sensitivity Table
|axis|baseline_weight_or_threshold|tested_weight_or_threshold|delta|affected_trigger_ids|affected_case_count|avg_MFE_90D_before|avg_MFE_90D_after|avg_MAE_90D_before|avg_MAE_90D_after|false_positive_count_before|false_positive_count_after|missed_structural_count_before|missed_structural_count_after|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|content_hit_stage2_actionable|0|3|+3|R8L7_KG_T2_STAGE2A_ODIN_RANKING|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|3|see profile table|see profile table|see profile table|see profile table|3|0 to 1 depending overlay|2|0|positive adjustment|
|green_confirmation_lateness_penalty|0|2|+2|R8L7_KG_T4_GREEN_ODIN_CONFIRMED|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE|2|see profile table|see profile table|see profile table|see profile table|3|0 to 1 depending overlay|2|0|positive adjustment|
|launch_quality_negative_gate|0|3|+3|R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL|2|see profile table|see profile table|see profile table|see profile table|3|0 to 1 depending overlay|2|0|positive adjustment|
|event_premium_without_fundamental_revision|0|-3|-3|R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS|1|see profile table|see profile table|see profile table|see profile table|3|0 to 1 depending overlay|2|0|cautious negative guardrail|
|price_only_4b_requires_non_price_evidence|allow_price_only|watch_only_without_non_price|rule_change|R8L7_KG_T5_4B_PEAK_WATCH|R8L7_DEV_T5_4B_BLOWOFF|R8L7_PEARL_T5_4B_TRAILER_BLOWOFF|R8L7_AHN_T5_4B_BLOWOFF|4|see profile table|see profile table|see profile table|see profile table|3|0 to 1 depending overlay|2|0|positive adjustment|

## 21. Optimization Decision Log
|decision_id|hypothesis|accepted_or_rejected|delta_magnitude|backtest_result_summary|why_not_larger_delta|next_validation_needed|
|---|---|---|---|---|---|---|
|R8L7_DECISION_01|Content-hit early evidence deserves Stage2-Actionable promotion when launch quality, ranking/traction, and relative strength align.|accepted|+3|Selected early content-hit triggers improved avg MFE90 from 29.0 to 244.0 and avg MAE90 from -32.7 to -14.5.|Sample is concentrated in game/content cycles and one case is event-optionality rather than confirmed EPS.|Validate non-game platform/SaaS/subscription software cycles.|
|R8L7_DECISION_02|Prelaunch hype should not close Stage3-Green without launch-quality confirmation.|accepted|+3|NC prelaunch Green had MFE90 0.8 and MAE90 -34.9; launch-day 4C protected against deeper 1Y drawdown.|Only one hard launch-failure calibration case in this R8 file.|Find additional game/service launch failure cases.|
|R8L7_DECISION_03|Political/control/event premium without fundamental revision should not be treated as EPS rerating.|accepted|-3|AhnLab had high MFE but MAE90 -47.3 and no software EPS bridge; after profile rejects it as structural entry.|Single explicit event-premium case; keep as guardrail not universal penalty.|Compare with other event-premium software/security stocks.|

## 22. Overfitting / Robustness Check
Usable case count is 5 and usable trigger count is 19, but the sample is concentrated in Korean game/content cycles plus one political-event software stock. Therefore the largest accepted numeric deltas are capped at +3/-3. No +5 very-strong adjustment is proposed. The 위메이드 MIR4/WEMIX narrative was explicitly blocked by corporate-action contamination, preventing a tempting but unsafe success case from influencing weights.


## 23. Cross-case Aggregate Metrics
### Trigger-type aggregate
|trigger_type|usable_trigger_count|representative_trigger_count|avg_MFE_90D_pct|median_MFE_90D_pct|avg_MAE_90D_pct|median_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|below_entry_90D_rate|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Stage2|4|4|264.3|79.4|-19.7|-12.2|324.3|-25.5|1.0|not_applicable|not_applicable|not_applicable|representative rows only for entries; overlays remain overlay-only|
|Stage2-Actionable|2|2|333.4|333.4|-15.9|-15.9|426.3|-15.9|1.0|not_applicable|not_applicable|not_applicable|representative rows only for entries; overlays remain overlay-only|
|Stage3-Yellow|3|3|81.6|35.8|-19.0|-16.1|103.4|-32.2|1.0|not_applicable|not_applicable|not_applicable|representative rows only for entries; overlays remain overlay-only|
|Stage3-Green|3|3|9.5|6.7|-33.4|-34.9|19.2|-43.7|1.0|0.8|not_applicable|not_applicable|representative rows only for entries; overlays remain overlay-only|
|4B|5|0|8.4|7.3|-43.3|-40.8|8.4|-56.3|1.0|not_applicable|0.9|0.9|representative rows only for entries; overlays remain overlay-only|
|4C|2|0|6.5|6.5|-27.9|-27.9|6.5|-36.5|1.0|not_applicable|not_applicable|not_applicable|representative rows only for entries; overlays remain overlay-only|

### Profile aggregate
|profile_id|case_count|selected_trigger_count|selected_representative_trigger_count|avg_MFE_90D_pct|median_MFE_90D_pct|avg_MAE_90D_pct|median_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|hit_rate_MFE90_gt_20pct|bad_entry_rate_MAE90_lt_minus_15pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|baseline_current_proxy|5|5|5|29.0|21.1|-32.7|-34.9|29.0|-45.7|0.6|1.0|0.6|2|2|0.83|0.86|0.86|reference; catches obvious Green too late and admits event-premium false positives|
|stage2_actionable_early_evidence_plus|5|3|3|244.0|65.2|-14.5|-13.7|294.3|-22.1|1.0|0.33|0.0|0|0|0.0|not_applicable|not_applicable|best; improves upside capture and rejects NC/Ahn event false positives|
|stage3_yellow_entry_relaxed|5|3|3|81.6|35.8|-19.0|-16.1|82.4|-32.5|1.0|0.67|0.0|1|0|not_applicable|not_applicable|not_applicable|useful but later than Stage2-Actionable in hit-game cycles|
|green_confirmation_timing_relaxed|5|3|3|81.6|35.8|-19.0|-16.1|82.4|-32.5|1.0|0.67|0.0|1|0|0.5|not_applicable|not_applicable|positive but inferior to Stage2-Actionable for content hits|
|four_b_peak_timing_tuned|5|5|0|8.4|7.3|-41.0|-40.8|8.4|-56.4|0.2|1.0|0.4|0|0|not_applicable|0.86|0.86|4B overlay works only with non-price blowoff evidence; price-only local 4B remains watch-only|
|four_c_thesis_break_earlier|5|2|0|6.6|6.6|-27.9|-27.9|6.6|-36.6|0.0|1.0|0.0|0|0|not_applicable|not_applicable|not_applicable|validates launch-quality 4C for NC; Ahn unwind was late event-premium exit|

## 24. Score-Price Alignment Verdict
R8 loop 7 says the scoring system should treat content-hit evidence like a flame that can be seen before the quarterly furnace is measured. Waiting for Green can make the signal safer on paper but late in price. However, the same early-promotion logic must not be given to event-premium stocks or prelaunch game hype. The guardrail is: **public traction + launch quality + monetization bridge** for promotion; **event premium or price-only blowoff** stays overlay/watch-only.


## 25. Validation Scope / Non-Validation Scope
### this_round_validates
- Stage2-Actionable promotion for content-hit/game launch cycles when public ranking/traction and relative strength appear together.
- Stage3-Green lateness risk in hit-game cycles.
- Launch-quality failure as 4C protection in live-service game launches.
- Event premium guardrail for software/security stocks with no EPS/OP bridge.
- Price-only 4B split into local watch vs full-window 4B with non-price evidence.

### this_round_does_not_validate
- Broad SaaS/subscription software EPS rerating outside games/content.
- Cybersecurity fundamental rerating cycles driven by ARR, cloud, or enterprise contract backlog.
- Universal 4C hard gate outside launch-quality or event-premium unwinds.
- Production scoring changes. All proposals are shadow-only.

## 26. Shadow Weight Calibration
|axis|baseline_value|tested_value|delta|reason|backtest_effect|trigger_ids|calibration_usable_count|notes|
|---|---|---|---|---|---|---|---|---|
|content_hit_stage2_actionable|0|3|+3|Odin/Cookie/DokeV early content-hit triggers had materially better MFE than confirmed Green with tolerable MAE.|After selected KG/DEV/PEARL early triggers avg_MFE_90D=244.0 vs baseline 29.0; avg_MAE_90D improved from -32.7 to -14.5.|R8L7_KG_T2_STAGE2A_ODIN_RANKING|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER|3|shadow-only; content-hit must be public and observable, not pure rumor|
|green_confirmation_lateness_penalty|0|2|+2|KG and DEV Green arrived after most upside was already harvested.|KG Green MFE90 6.7 vs Stage2A 48.0; DEV Green MFE90 21.1 vs Stage2A 618.8.|R8L7_KG_T4_GREEN_ODIN_CONFIRMED|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE|2|shadow-only; do not relax Green without launch-quality/traction evidence|
|launch_quality_negative_gate|0|3|+3|NC prelaunch Green scored as false positive; launch-quality break produced a hard 4C.|NC prelaunch Green MFE90 0.8 and MAE90 -34.9; 4C after launch failure marked thesis break before deeper 1Y drawdown.|R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL|2|shadow-only; applies to game/service launch quality, not all platform software|
|event_premium_without_fundamental_revision|0|-3|-3|AhnLab political event premium had high MFE but no EPS/OP bridge and severe drawdown.|Ahn event trigger MFE90 81.3 but MAE90 -47.3; after profile rejects as EPS-rerating entry.|R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS|1|exploratory but strong qualitative guardrail; event premium remains separate overlay|
|price_only_4b_requires_non_price_evidence|allow_price_only|watch_only_without_non_price|rule_change|Pearl/Ahn price-only blowoffs were hard to convert into systematic full 4B exits without non-price evidence.|KG/DEV non-price blowoff 4B worked; Pearl/Ahn price-only 4B marked watch-only.|R8L7_KG_T5_4B_PEAK_WATCH|R8L7_DEV_T5_4B_BLOWOFF|R8L7_PEARL_T5_4B_TRAILER_BLOWOFF|R8L7_AHN_T5_4B_BLOWOFF|4|shadow-only; split local vs full-window proximity|

## 27. Machine-Readable Rows
### 27.1 Price source validation row JSONL
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_basis":"FinanceData/marcap transformed into assistant-readable symbol-year CSV shards","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"validation_status":"usable_for_historical_calibration"}
```

### 27.2 Case rows JSONL
```jsonl
{"row_type":"case","case_id":"R8L7_KG_ODIN_2021","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","case_type":"structural_success","primary_archetype":"MOBILE_GAME_LAUNCH_TO_OPERATING_LEVERAGE","best_trigger":"R8L7_KG_T2_STAGE2A_ODIN_RANKING","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"Stage2_Actionable_beats_Green","price_source":"Songdaiki/stock-web","notes":"Odin cycle shows Green confirmation arriving near the peak."}
{"row_type":"case","case_id":"R8L7_DEV_COOKIE_2021","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","case_type":"structural_success_and_4B","primary_archetype":"IP_GAME_HIT_TO_GLOBAL_RERATING","best_trigger":"R8L7_DEV_T2_STAGE2A_COOKIE_HIT","calibration_usable":true,"historical_window_status":"252D_available","score_price_alignment":"Stage2_Actionable_best_entry","price_source":"Songdaiki/stock-web","notes":"Cookie Run Kingdom shows extreme early hit evidence and later blowoff."}
{"row_type":"case","case_id":"R8L7_PEARL_DOKEV_2021","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","case_type":"event_premium_success_candidate","primary_archetype":"TRAILER_OPTIONALITY_EVENT_PREMIUM","best_trigger":"R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER","calibration_usable":true,"historical_window_status":"252D_available","score_price_alignment":"event_premium_requires_guardrail","price_source":"Songdaiki/stock-web","notes":"Trailer optionality produced returns but lacked confirmed EPS bridge."}
{"row_type":"case","case_id":"R8L7_NCSOFT_BNS2_2021","symbol":"036570","company_name":"엔씨소프트","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","case_type":"4C_thesis_break","primary_archetype":"LIVE_SERVICE_GAME_LAUNCH_FAILURE","best_trigger":"R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL","calibration_usable":true,"historical_window_status":"504D_available","score_price_alignment":"prelaunch_Green_false_positive","price_source":"Songdaiki/stock-web","notes":"Launch-quality failure should be a hard negative gate."}
{"row_type":"case","case_id":"R8L7_AHNLAB_EVENT_2022","symbol":"053800","company_name":"안랩","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","case_type":"event_premium_false_positive","primary_archetype":"POLITICAL_EVENT_PREMIUM_SOFTWARE_STOCK","best_trigger":"R8L7_AHN_T5_4B_BLOWOFF","calibration_usable":true,"historical_window_status":"252D_available","score_price_alignment":"price_moved_without_fundamental_evidence","price_source":"Songdaiki/stock-web","notes":"Event premium had high MFE but is not EPS rerating evidence."}
```

### 27.3 Trigger rows JSONL
```jsonl
{"row_type":"trigger","trigger_id":"R8L7_KG_T1_STAGE2_ODIN_LAUNCH","case_id":"R8L7_KG_ODIN_2021","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_LAUNCH_TO_OPERATING_LEVERAGE","trigger_type":"Stage2","trigger_date":"2021-06-29","evidence_available_at_that_date":"Odin launch day and immediate launch interest were public; earnings bridge not yet confirmed.","evidence_source":"company launch/news + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-06-29","entry_price":59700,"MFE_30D_pct":77.6,"MFE_90D_pct":77.6,"MFE_180D_pct":94.3,"MFE_1Y_pct":94.3,"MFE_2Y_pct":94.3,"MAE_30D_pct":-6.9,"MAE_90D_pct":-6.9,"MAE_180D_pct":-6.9,"MAE_1Y_pct":-22.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":116000,"drawdown_after_peak_pct":-60.3,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_KG_ODIN_2021|2021-06-29|59700","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_KG_T2_STAGE2A_ODIN_RANKING","case_id":"R8L7_KG_ODIN_2021","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_LAUNCH_TO_OPERATING_LEVERAGE","trigger_type":"Stage2-Actionable","trigger_date":"2021-07-02","evidence_available_at_that_date":"Launch plus visible market reaction/ranking traction; still before full quarterly confirmation.","evidence_source":"public ranking/news + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-07-02","entry_price":71600,"MFE_30D_pct":48.0,"MFE_90D_pct":48.0,"MFE_180D_pct":62.0,"MFE_1Y_pct":62.0,"MFE_2Y_pct":62.0,"MAE_30D_pct":-18.6,"MAE_90D_pct":-13.7,"MAE_180D_pct":-13.7,"MAE_1Y_pct":-35.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":116000,"drawdown_after_peak_pct":-60.3,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_KG_ODIN_2021|2021-07-02|71600","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_KG_T3_YELLOW_ODIN_SUSTAINED","case_id":"R8L7_KG_ODIN_2021","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_LAUNCH_TO_OPERATING_LEVERAGE","trigger_type":"Stage3-Yellow","trigger_date":"2021-08-26","evidence_available_at_that_date":"Sustained Odin momentum was visible, but much of the repricing had already happened.","evidence_source":"news/report + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-26","entry_price":85400,"MFE_30D_pct":2.6,"MFE_90D_pct":35.8,"MFE_180D_pct":35.8,"MFE_1Y_pct":35.8,"MFE_2Y_pct":35.8,"MAE_30D_pct":-23.4,"MAE_90D_pct":-27.6,"MAE_180D_pct":-36.4,"MAE_1Y_pct":-46.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":116000,"drawdown_after_peak_pct":-60.3,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_KG_ODIN_2021|2021-08-26|85400","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_KG_T4_GREEN_ODIN_CONFIRMED","case_id":"R8L7_KG_ODIN_2021","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_LAUNCH_TO_OPERATING_LEVERAGE","trigger_type":"Stage3-Green","trigger_date":"2021-11-16","evidence_available_at_that_date":"Confirmed earnings/price strength arrived near the observed cycle peak.","evidence_source":"earnings/report + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-16","entry_price":108700,"MFE_30D_pct":6.7,"MFE_90D_pct":6.7,"MFE_180D_pct":6.7,"MFE_1Y_pct":6.7,"MFE_2Y_pct":6.7,"MAE_30D_pct":-40.8,"MAE_90D_pct":-41.2,"MAE_180D_pct":-57.6,"MAE_1Y_pct":-57.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":116000,"drawdown_after_peak_pct":-60.3,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.87,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_KG_ODIN_2021|2021-11-16|108700","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_KG_T5_4B_PEAK_WATCH","case_id":"R8L7_KG_ODIN_2021","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"MOBILE_GAME_LAUNCH_TO_OPERATING_LEVERAGE","trigger_type":"4B","trigger_date":"2021-11-17","evidence_available_at_that_date":"Valuation/positioning blowoff risk after confirmed hit-game repricing.","evidence_source":"price + valuation/risk note + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-17","entry_price":107900,"MFE_30D_pct":7.5,"MFE_90D_pct":7.5,"MFE_180D_pct":7.5,"MFE_1Y_pct":7.5,"MFE_2Y_pct":7.5,"MAE_30D_pct":-40.8,"MAE_90D_pct":-40.8,"MAE_180D_pct":-57.3,"MAE_1Y_pct":-57.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":116000,"drawdown_after_peak_pct":-60.3,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_full_window_4B_watch","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_KG_ODIN_2021|2021-11-17|107900","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L7_DEV_T1_STAGE2_COOKIE_LAUNCH","case_id":"R8L7_DEV_COOKIE_2021","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"IP_GAME_HIT_TO_GLOBAL_RERATING","trigger_type":"Stage2","trigger_date":"2021-01-21","evidence_available_at_that_date":"Cookie Run: Kingdom launch was public; early hit evidence began before earnings revision.","evidence_source":"official release/news + stock-web 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-21","entry_price":17250,"MFE_30D_pct":300.0,"MFE_90D_pct":833.3,"MFE_180D_pct":1056.5,"MFE_1Y_pct":1056.5,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-12.8,"MAE_90D_pct":-12.8,"MAE_180D_pct":-12.8,"MAE_1Y_pct":-12.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-55.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_DEV_COOKIE_2021|2021-01-21|17250","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_DEV_T2_STAGE2A_COOKIE_HIT","case_id":"R8L7_DEV_COOKIE_2021","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"IP_GAME_HIT_TO_GLOBAL_RERATING","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-22","evidence_available_at_that_date":"Launch plus immediate price/volume response and visible app-market traction.","evidence_source":"news/ranking + stock-web 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-22","entry_price":22400,"MFE_30D_pct":208.0,"MFE_90D_pct":618.8,"MFE_180D_pct":790.6,"MFE_1Y_pct":790.6,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-18.1,"MAE_90D_pct":-18.1,"MAE_180D_pct":-18.1,"MAE_1Y_pct":-18.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-55.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_DEV_COOKIE_2021|2021-01-22|22400","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_DEV_T3_YELLOW_DOWNLOADS","case_id":"R8L7_DEV_COOKIE_2021","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"IP_GAME_HIT_TO_GLOBAL_RERATING","trigger_type":"Stage3-Yellow","trigger_date":"2021-02-22","evidence_available_at_that_date":"Download/ranking evidence was strong; profit path still not fully confirmed.","evidence_source":"news/report + stock-web 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-22","entry_price":58800,"MFE_30D_pct":173.8,"MFE_90D_pct":173.8,"MFE_180D_pct":239.3,"MFE_1Y_pct":239.3,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-13.3,"MAE_90D_pct":-13.3,"MAE_180D_pct":-13.3,"MAE_1Y_pct":-13.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-55.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_DEV_COOKIE_2021|2021-02-22|58800","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE","case_id":"R8L7_DEV_COOKIE_2021","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"IP_GAME_HIT_TO_GLOBAL_RERATING","trigger_type":"Stage3-Green","trigger_date":"2021-03-25","evidence_available_at_that_date":"By this point hit evidence and repricing were obvious, but early upside was already captured.","evidence_source":"news/report + stock-web 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-03-25","entry_price":133000,"MFE_30D_pct":21.1,"MFE_90D_pct":21.1,"MFE_180D_pct":50.0,"MFE_1Y_pct":50.0,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-24.1,"MAE_90D_pct":-24.1,"MAE_180D_pct":-24.1,"MAE_1Y_pct":-33.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-55.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":0.63,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_DEV_COOKIE_2021|2021-03-25|133000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_DEV_T5_4B_BLOWOFF","case_id":"R8L7_DEV_COOKIE_2021","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"IP_GAME_HIT_TO_GLOBAL_RERATING","trigger_type":"4B","trigger_date":"2021-09-27","evidence_available_at_that_date":"Full-window blowoff after extreme rerating and positioning heat.","evidence_source":"price + valuation/risk note + stock-web 2021 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-09-27","entry_price":186000,"MFE_30D_pct":7.3,"MFE_90D_pct":7.3,"MFE_180D_pct":7.3,"MFE_1Y_pct":7.3,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-52.4,"MAE_90D_pct":-52.4,"MAE_180D_pct":-55.6,"MAE_1Y_pct":-55.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-27","peak_price":199500,"drawdown_after_peak_pct":-55.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"valuation_blowoff|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_full_window_4B_timing","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_DEV_COOKIE_2021|2021-09-27|186000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER","case_id":"R8L7_PEARL_DOKEV_2021","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"TRAILER_OPTIONALITY_EVENT_PREMIUM","trigger_type":"Stage2","trigger_date":"2021-08-26","evidence_available_at_that_date":"DokeV gameplay trailer created new-title optionality, but monetization/release timing remained open.","evidence_source":"Gamescom/trailer news + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-26","entry_price":87900,"MFE_30D_pct":16.0,"MFE_90D_pct":65.2,"MFE_180D_pct":65.2,"MFE_1Y_pct":65.2,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-11.7,"MAE_90D_pct":-11.7,"MAE_180D_pct":-34.9,"MAE_1Y_pct":-45.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-67.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"event_premium_good_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_PEARL_DOKEV_2021|2021-08-26|87900","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_PEARL_T3_YELLOW_TRAILER_MOMENTUM","case_id":"R8L7_PEARL_DOKEV_2021","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"TRAILER_OPTIONALITY_EVENT_PREMIUM","trigger_type":"Stage3-Yellow","trigger_date":"2021-10-21","evidence_available_at_that_date":"Momentum persisted, but evidence was still option-value rather than confirmed EPS bridge.","evidence_source":"price/news + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-10-21","entry_price":107500,"MFE_30D_pct":35.1,"MFE_90D_pct":35.1,"MFE_180D_pct":35.1,"MFE_1Y_pct":35.1,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-6.0,"MAE_90D_pct":-16.1,"MAE_180D_pct":-46.8,"MAE_1Y_pct":-55.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-67.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"good_entry_but_watch_only","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_PEARL_DOKEV_2021|2021-10-21|107500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_PEARL_T5_4B_TRAILER_BLOWOFF","case_id":"R8L7_PEARL_DOKEV_2021","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"TRAILER_OPTIONALITY_EVENT_PREMIUM","trigger_type":"4B","trigger_date":"2021-11-17","evidence_available_at_that_date":"Price-only blowoff near full-window high without non-price slowdown confirmation.","evidence_source":"price-only + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-17","entry_price":141000,"MFE_30D_pct":3.0,"MFE_90D_pct":3.0,"MFE_180D_pct":3.0,"MFE_1Y_pct":3.0,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-35.7,"MAE_90D_pct":-35.7,"MAE_180D_pct":-59.4,"MAE_1Y_pct":-67.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-67.1,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"price_only_local_4B_requires_non_price_confirmation","four_b_evidence_type":"price_only|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"price_only_4B_watch_not_full_exit","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_PEARL_DOKEV_2021|2021-11-17|141000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L7_NC_T4_GREEN_PRELAUNCH_HYPE","case_id":"R8L7_NCSOFT_BNS2_2021","symbol":"036570","company_name":"엔씨소프트","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"LIVE_SERVICE_GAME_LAUNCH_FAILURE","trigger_type":"Stage3-Green","trigger_date":"2021-08-19","evidence_available_at_that_date":"Pre-launch franchise/monetization expectation looked like Green, but launch-quality gate had not closed.","evidence_source":"prelaunch/news + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv","profile_path":"atlas/symbol_profiles/036/036570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-19","entry_price":853000,"MFE_30D_pct":0.8,"MFE_90D_pct":0.8,"MFE_180D_pct":0.8,"MFE_1Y_pct":0.8,"MFE_2Y_pct":0.8,"MAE_30D_pct":-34.6,"MAE_90D_pct":-34.9,"MAE_180D_pct":-49.4,"MAE_1Y_pct":-59.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-08-20","peak_price":860000,"drawdown_after_peak_pct":-59.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":1.0,"four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"score_high_return_low_false_positive","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_NCSOFT_BNS2_2021|2021-08-19|853000","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL","case_id":"R8L7_NCSOFT_BNS2_2021","symbol":"036570","company_name":"엔씨소프트","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"LIVE_SERVICE_GAME_LAUNCH_FAILURE","trigger_type":"4C","trigger_date":"2021-08-26","evidence_available_at_that_date":"Launch-day disappointment/review and monetization-quality break damaged the original thesis.","evidence_source":"launch/news + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv","profile_path":"atlas/symbol_profiles/036/036570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-26","entry_price":709000,"MFE_30D_pct":11.1,"MFE_90D_pct":11.1,"MFE_180D_pct":11.1,"MFE_1Y_pct":11.1,"MFE_2Y_pct":11.1,"MAE_30D_pct":-21.3,"MAE_90D_pct":-21.7,"MAE_180D_pct":-39.1,"MAE_1Y_pct":-51.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-11","peak_price":786000,"drawdown_after_peak_pct":-55.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_NCSOFT_BNS2_2021|2021-08-26|709000","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L7_NC_T5_NFT_METAVERSE_EVENT","case_id":"R8L7_NCSOFT_BNS2_2021","symbol":"036570","company_name":"엔씨소프트","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"LIVE_SERVICE_GAME_LAUNCH_FAILURE","trigger_type":"4B","trigger_date":"2021-11-11","evidence_available_at_that_date":"NFT/metaverse event spike after the core launch thesis was already damaged.","evidence_source":"event news + stock-web 2021/2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036570/2021.csv","profile_path":"atlas/symbol_profiles/036/036570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-11","entry_price":786000,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":0.0,"MFE_2Y_pct":0.0,"MAE_30D_pct":-25.1,"MAE_90D_pct":-33.6,"MAE_180D_pct":-55.5,"MAE_1Y_pct":-55.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-11","peak_price":786000,"drawdown_after_peak_pct":-55.6,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_price_only_4B_after_thesis_damage","four_b_evidence_type":"price_only|event_premium","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_score","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_NCSOFT_BNS2_2021|2021-11-11|786000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS","case_id":"R8L7_AHNLAB_EVENT_2022","symbol":"053800","company_name":"안랩","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"POLITICAL_EVENT_PREMIUM_SOFTWARE_STOCK","trigger_type":"Stage2","trigger_date":"2022-01-05","evidence_available_at_that_date":"Founder-linked political event premium was visible, but no software EPS rerating evidence was present.","evidence_source":"election/news + stock-web 2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-05","entry_price":120500,"MFE_30D_pct":6.6,"MFE_90D_pct":81.3,"MFE_180D_pct":81.3,"MFE_1Y_pct":81.3,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-41.6,"MAE_90D_pct":-47.3,"MAE_180D_pct":-47.3,"MAE_1Y_pct":-47.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-62.9,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable","trigger_outcome_label":"price_moved_without_fundamental_evidence","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_AHNLAB_EVENT_2022|2022-01-05|120500","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","trigger_id":"R8L7_AHN_T5_4B_BLOWOFF","case_id":"R8L7_AHNLAB_EVENT_2022","symbol":"053800","company_name":"안랩","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"POLITICAL_EVENT_PREMIUM_SOFTWARE_STOCK","trigger_type":"4B","trigger_date":"2022-03-23","evidence_available_at_that_date":"Event-premium blowoff immediately before/around observed peak; not an EPS signal.","evidence_source":"election/news + stock-web 2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-23","entry_price":175800,"MFE_30D_pct":24.3,"MFE_90D_pct":24.3,"MFE_180D_pct":24.3,"MFE_1Y_pct":24.3,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-44.0,"MAE_90D_pct":-53.9,"MAE_180D_pct":-53.9,"MAE_1Y_pct":-53.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-62.9,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.56,"four_b_full_window_peak_proximity":0.56,"four_b_timing_verdict":"event_premium_4B_watch_but_intraday_peak_hard_to_capture","four_b_evidence_type":"price_only|control_premium_or_event_premium","four_c_protection_label":"not_applicable","trigger_outcome_label":"event_premium_4B_watch","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_AHNLAB_EVENT_2022|2022-03-23|175800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only"}
{"row_type":"trigger","trigger_id":"R8L7_AHN_T6_EVENT_UNWIND","case_id":"R8L7_AHNLAB_EVENT_2022","symbol":"053800","company_name":"안랩","round":"R8","loop":"7","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"POLITICAL_EVENT_PREMIUM_SOFTWARE_STOCK","trigger_type":"4C","trigger_date":"2022-03-30","evidence_available_at_that_date":"Event premium unwind was visible, but only after intraday blowoff had already passed.","evidence_source":"election/news + stock-web 2022 shard","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-30","entry_price":122800,"MFE_30D_pct":2.0,"MFE_90D_pct":2.0,"MFE_180D_pct":2.0,"MFE_1Y_pct":2.0,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-34.0,"MAE_90D_pct":-34.0,"MAE_180D_pct":-34.0,"MAE_1Y_pct":-34.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-30","peak_price":125300,"drawdown_after_peak_pct":-35.5,"market_relative_return_30D_pct":"unavailable","market_relative_return_90D_pct":"unavailable","sector_relative_return_90D_pct":"unavailable","green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"hard_4c_late","trigger_outcome_label":"hard_4c_late","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L7_AHNLAB_EVENT_2022|2022-03-30|122800","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only"}
```

### 27.4 Score simulation rows JSONL
```jsonl
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_KG_ODIN_2021","trigger_id":"R8L7_KG_T2_STAGE2A_ODIN_RANKING","symbol":"293490","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":65,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":72,"launch_quality_score":70,"platform_take_rate_score":40,"event_premium_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":22.5,"stage_label_before":"Watch/Reject","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":75,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":87,"launch_quality_score":80,"platform_take_rate_score":40,"event_premium_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":25.4,"stage_label_after":"Stage2","changed_components":["content_hit_score","launch_quality_score","relative_strength_score"],"component_delta_explanation":"After profile promotes early content-hit evidence only when launch quality and relative strength are already visible.","selected_by_profile":true,"MFE_90D_pct":48.0,"MAE_90D_pct":-13.7,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_KG_ODIN_2021","trigger_id":"R8L7_KG_T4_GREEN_ODIN_CONFIRMED","symbol":"293490","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":75,"relative_strength_score":80,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":80,"launch_quality_score":75,"platform_take_rate_score":55,"event_premium_score":0,"positioning_overheat_score":65,"thesis_break_score":0},"weighted_score_before":34.9,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":75,"relative_strength_score":80,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":80,"launch_quality_score":75,"platform_take_rate_score":55,"event_premium_score":0,"positioning_overheat_score":65,"thesis_break_score":0},"weighted_score_after":34.9,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"No after change; baseline reference row.","selected_by_profile":false,"MFE_90D_pct":6.7,"MAE_90D_pct":-41.2,"score_return_alignment_label":"score_low_return_low_correct_reject"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_DEV_COOKIE_2021","trigger_id":"R8L7_DEV_T2_STAGE2A_COOKIE_HIT","symbol":"194480","trigger_type":"Stage2-Actionable","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":80,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":90,"launch_quality_score":85,"platform_take_rate_score":45,"event_premium_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":26.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":90,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":100,"launch_quality_score":95,"platform_take_rate_score":45,"event_premium_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":29.3,"stage_label_after":"Stage2","changed_components":["content_hit_score","launch_quality_score","relative_strength_score"],"component_delta_explanation":"After profile promotes early content-hit evidence only when launch quality and relative strength are already visible.","selected_by_profile":true,"MFE_90D_pct":618.8,"MAE_90D_pct":-18.1,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_DEV_COOKIE_2021","trigger_id":"R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE","symbol":"194480","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":75,"revision_score":80,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":85,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":90,"launch_quality_score":85,"platform_take_rate_score":70,"event_premium_score":0,"positioning_overheat_score":75,"thesis_break_score":0},"weighted_score_before":40.6,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":75,"revision_score":80,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":85,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":90,"launch_quality_score":85,"platform_take_rate_score":70,"event_premium_score":0,"positioning_overheat_score":75,"thesis_break_score":0},"weighted_score_after":40.6,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"No after change; baseline reference row.","selected_by_profile":false,"MFE_90D_pct":21.1,"MAE_90D_pct":-24.1,"score_return_alignment_label":"score_low_return_low_correct_reject"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_PEARL_DOKEV_2021","trigger_id":"R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER","symbol":"263750","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":65,"launch_quality_score":35,"platform_take_rate_score":0,"event_premium_score":75,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":21.7,"stage_label_before":"Watch/Reject","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":80,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":80,"launch_quality_score":45,"platform_take_rate_score":0,"event_premium_score":75,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":24.6,"stage_label_after":"Watch/Reject","changed_components":["content_hit_score","launch_quality_score","relative_strength_score"],"component_delta_explanation":"After profile promotes early content-hit evidence only when launch quality and relative strength are already visible.","selected_by_profile":true,"MFE_90D_pct":65.2,"MAE_90D_pct":-11.7,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_PEARL_DOKEV_2021","trigger_id":"R8L7_PEARL_T3_YELLOW_TRAILER_MOMENTUM","symbol":"263750","trigger_type":"Stage3-Yellow","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":75,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":65,"launch_quality_score":35,"platform_take_rate_score":0,"event_premium_score":80,"positioning_overheat_score":40,"thesis_break_score":0},"weighted_score_before":23.0,"stage_label_before":"Watch/Reject","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":75,"customer_quality_score":65,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":65,"launch_quality_score":35,"platform_take_rate_score":0,"event_premium_score":80,"positioning_overheat_score":40,"thesis_break_score":0},"weighted_score_after":23.0,"stage_label_after":"Watch/Reject","changed_components":[],"component_delta_explanation":"No after change; baseline reference row.","selected_by_profile":false,"MFE_90D_pct":35.1,"MAE_90D_pct":-16.1,"score_return_alignment_label":"score_low_return_low_correct_reject"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_NCSOFT_BNS2_2021","trigger_id":"R8L7_NC_T4_GREEN_PRELAUNCH_HYPE","symbol":"036570","trigger_type":"Stage3-Green","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":55,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":55,"launch_quality_score":20,"platform_take_rate_score":55,"event_premium_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":26.7,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":55,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":80,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":55,"launch_quality_score":5,"platform_take_rate_score":55,"event_premium_score":0,"positioning_overheat_score":0,"thesis_break_score":75},"weighted_score_after":11.2,"stage_label_after":"Watch/Reject","changed_components":["launch_quality_score","thesis_break_score","execution_risk_score"],"component_delta_explanation":"After profile prevents pre-launch franchise expectation from becoming Green without launch-quality confirmation.","selected_by_profile":false,"MFE_90D_pct":0.8,"MAE_90D_pct":-34.9,"score_return_alignment_label":"score_high_return_low_false_positive"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_NCSOFT_BNS2_2021","trigger_id":"R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL","symbol":"036570","trigger_type":"4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":75,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":85,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":10,"launch_quality_score":5,"platform_take_rate_score":20,"event_premium_score":0,"positioning_overheat_score":0,"thesis_break_score":90},"weighted_score_before":0,"stage_label_before":"4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":75,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":85,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":10,"launch_quality_score":5,"platform_take_rate_score":20,"event_premium_score":0,"positioning_overheat_score":0,"thesis_break_score":90},"weighted_score_after":0,"stage_label_after":"4C","changed_components":[],"component_delta_explanation":"No after change; baseline reference row.","selected_by_profile":false,"MFE_90D_pct":11.1,"MAE_90D_pct":-21.7,"score_return_alignment_label":"score_low_return_low_correct_reject"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","case_id":"R8L7_AHNLAB_EVENT_2022","trigger_id":"R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS","symbol":"053800","trigger_type":"Stage2","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":75,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":0,"launch_quality_score":0,"platform_take_rate_score":0,"event_premium_score":90,"positioning_overheat_score":65,"thesis_break_score":0},"weighted_score_before":12.4,"stage_label_before":"Watch/Reject","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":75,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"content_hit_score":0,"launch_quality_score":0,"platform_take_rate_score":0,"event_premium_score":35,"positioning_overheat_score":85,"thesis_break_score":0},"weighted_score_after":6.0,"stage_label_after":"Watch/Reject","changed_components":["event_premium_score","positioning_overheat_score"],"component_delta_explanation":"After profile treats political/control event premium as watch-only unless EPS/OP evidence appears.","selected_by_profile":false,"MFE_90D_pct":81.3,"MAE_90D_pct":-47.3,"score_return_alignment_label":"score_low_return_low_correct_reject"}
```

### 27.5 Profile comparison rows CSV
```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
profile_comparison,baseline_current_proxy,5,5,5,29.0,21.1,-32.7,-34.9,29.0,-45.7,0.6,1.0,0.6,2,2,0.83,0.86,0.86,reference; catches obvious Green too late and admits event-premium false positives
profile_comparison,stage2_actionable_early_evidence_plus,5,3,3,244.0,65.2,-14.5,-13.7,294.3,-22.1,1.0,0.33,0.0,0,0,0.0,not_applicable,not_applicable,best; improves upside capture and rejects NC/Ahn event false positives
profile_comparison,stage3_yellow_entry_relaxed,5,3,3,81.6,35.8,-19.0,-16.1,82.4,-32.5,1.0,0.67,0.0,1,0,not_applicable,not_applicable,not_applicable,useful but later than Stage2-Actionable in hit-game cycles
profile_comparison,green_confirmation_timing_relaxed,5,3,3,81.6,35.8,-19.0,-16.1,82.4,-32.5,1.0,0.67,0.0,1,0,0.5,not_applicable,not_applicable,positive but inferior to Stage2-Actionable for content hits
profile_comparison,four_b_peak_timing_tuned,5,5,0,8.4,7.3,-41.0,-40.8,8.4,-56.4,0.2,1.0,0.4,0,0,not_applicable,0.86,0.86,4B overlay works only with non-price blowoff evidence; price-only local 4B remains watch-only
profile_comparison,four_c_thesis_break_earlier,5,2,0,6.6,6.6,-27.9,-27.9,6.6,-36.6,0.0,1.0,0.0,0,0,not_applicable,not_applicable,not_applicable,validates launch-quality 4C for NC; Ahn unwind was late event-premium exit
```

### 27.6 Shadow weight CSV
```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,content_hit_stage2_actionable,0,3,+3,Odin/Cookie/DokeV early content-hit triggers had materially better MFE than confirmed Green with tolerable MAE.,After selected KG/DEV/PEARL early triggers avg_MFE_90D=244.0 vs baseline 29.0; avg_MAE_90D improved from -32.7 to -14.5.,R8L7_KG_T2_STAGE2A_ODIN_RANKING|R8L7_DEV_T2_STAGE2A_COOKIE_HIT|R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER,3,"shadow-only; content-hit must be public and observable, not pure rumor"
shadow_weight,green_confirmation_lateness_penalty,0,2,+2,KG and DEV Green arrived after most upside was already harvested.,KG Green MFE90 6.7 vs Stage2A 48.0; DEV Green MFE90 21.1 vs Stage2A 618.8.,R8L7_KG_T4_GREEN_ODIN_CONFIRMED|R8L7_DEV_T4_GREEN_EARNINGS_VISIBLE,2,shadow-only; do not relax Green without launch-quality/traction evidence
shadow_weight,launch_quality_negative_gate,0,3,+3,NC prelaunch Green scored as false positive; launch-quality break produced a hard 4C.,NC prelaunch Green MFE90 0.8 and MAE90 -34.9; 4C after launch failure marked thesis break before deeper 1Y drawdown.,R8L7_NC_T4_GREEN_PRELAUNCH_HYPE|R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL,2,"shadow-only; applies to game/service launch quality, not all platform software"
shadow_weight,event_premium_without_fundamental_revision,0,-3,-3,AhnLab political event premium had high MFE but no EPS/OP bridge and severe drawdown.,Ahn event trigger MFE90 81.3 but MAE90 -47.3; after profile rejects as EPS-rerating entry.,R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS,1,exploratory but strong qualitative guardrail; event premium remains separate overlay
shadow_weight,price_only_4b_requires_non_price_evidence,allow_price_only,watch_only_without_non_price,rule_change,Pearl/Ahn price-only blowoffs were hard to convert into systematic full 4B exits without non-price evidence.,KG/DEV non-price blowoff 4B worked; Pearl/Ahn price-only 4B marked watch-only.,R8L7_KG_T5_4B_PEAK_WATCH|R8L7_DEV_T5_4B_BLOWOFF|R8L7_PEARL_T5_4B_TRAILER_BLOWOFF|R8L7_AHN_T5_4B_BLOWOFF,4,shadow-only; split local vs full-window proximity
```

### 27.7 Optimization decision rows JSONL
```jsonl
{"row_type":"optimization_decision","decision_id":"R8L7_DECISION_01","hypothesis":"Content-hit early evidence deserves Stage2-Actionable promotion when launch quality, ranking/traction, and relative strength align.","tested_trigger_ids":["R8L7_KG_T2_STAGE2A_ODIN_RANKING","R8L7_DEV_T2_STAGE2A_COOKIE_HIT","R8L7_PEARL_T1_STAGE2_DOKEV_TRAILER"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","backtest_result_summary":"Selected early content-hit triggers improved avg MFE90 from 29.0 to 244.0 and avg MAE90 from -32.7 to -14.5.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Sample is concentrated in game/content cycles and one case is event-optionality rather than confirmed EPS.","risks":"Hit-game cycles are fat-tailed; ranking data can decay quickly.","next_validation_needed":"Validate non-game platform/SaaS/subscription software cycles."}
{"row_type":"optimization_decision","decision_id":"R8L7_DECISION_02","hypothesis":"Prelaunch hype should not close Stage3-Green without launch-quality confirmation.","tested_trigger_ids":["R8L7_NC_T4_GREEN_PRELAUNCH_HYPE","R8L7_NC_T6_4C_BNS2_LAUNCH_FAIL"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_c_thesis_break_earlier","backtest_result_summary":"NC prelaunch Green had MFE90 0.8 and MAE90 -34.9; launch-day 4C protected against deeper 1Y drawdown.","accepted_or_rejected":"accepted","delta_magnitude":"+3","why_not_larger_delta":"Only one hard launch-failure calibration case in this R8 file.","risks":"Some launch disappointments recover after patch/operations; require follow-through confirmation.","next_validation_needed":"Find additional game/service launch failure cases."}
{"row_type":"optimization_decision","decision_id":"R8L7_DECISION_03","hypothesis":"Political/control/event premium without fundamental revision should not be treated as EPS rerating.","tested_trigger_ids":["R8L7_AHN_T0_EVENT_PREMIUM_AWARENESS","R8L7_AHN_T5_4B_BLOWOFF","R8L7_AHN_T6_EVENT_UNWIND"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_content_hit_plus_4b_evidence_guardrail","backtest_result_summary":"AhnLab had high MFE but MAE90 -47.3 and no software EPS bridge; after profile rejects it as structural entry.","accepted_or_rejected":"accepted","delta_magnitude":"-3","why_not_larger_delta":"Single explicit event-premium case; keep as guardrail not universal penalty.","risks":"Rare cases can convert event premium into actual capital allocation/control value.","next_validation_needed":"Compare with other event-premium software/security stocks."}
```

### 27.8 Narrative-only rows JSONL
```jsonl
{"row_type":"narrative_only","case_id":"R8L7_WEMADE_MIR4_2021_BLOCKED","symbol":"112040","company_name":"위메이드","reason":"MIR4/WEMIX 2021 window overlaps corporate_action_candidate_dates 2021-09-13 and 2021-10-06 in stock-web profile; raw-unadjusted 180D calibration is blocked by rule.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

### 27.9 Aggregate metric rows CSV
```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,4,4,264.3,79.4,-19.7,-12.2,324.3,-25.5,1.0,not_applicable,not_applicable,not_applicable,representative rows only for entries; overlays remain overlay-only
aggregate_metric,Stage2-Actionable,2,2,333.4,333.4,-15.9,-15.9,426.3,-15.9,1.0,not_applicable,not_applicable,not_applicable,representative rows only for entries; overlays remain overlay-only
aggregate_metric,Stage3-Yellow,3,3,81.6,35.8,-19.0,-16.1,103.4,-32.2,1.0,not_applicable,not_applicable,not_applicable,representative rows only for entries; overlays remain overlay-only
aggregate_metric,Stage3-Green,3,3,9.5,6.7,-33.4,-34.9,19.2,-43.7,1.0,0.8,not_applicable,not_applicable,representative rows only for entries; overlays remain overlay-only
aggregate_metric,4B,5,0,8.4,7.3,-43.3,-40.8,8.4,-56.3,1.0,not_applicable,0.9,0.9,representative rows only for entries; overlays remain overlay-only
aggregate_metric,4C,2,0,6.5,6.5,-27.9,-27.9,6.5,-36.5,1.0,not_applicable,not_applicable,not_applicable,representative rows only for entries; overlays remain overlay-only
```

## 28. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, aggregate deduplication, and shadow score profiles.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules
- Use only rows with calibration_usable=true for weight calibration.
- Reject narrative-only rows for score changes.
- Reject rows without OHLC-derived MFE/MAE.
- Reject rows without at least 180 trading days forward window.
- Reject rows blocked by corporate-action-contaminated 180D window unless the user explicitly allows a separate adjusted-price revalidation.
- Reject shadow_weight rows that do not include before/after backtest effect.
- Reject score_simulation rows that have weighted_score_before/after but no raw_component_scores_before/after.
- Reject shadow_weight rows if the changed axis is not traceable to component-level score changes and OHLC backtest effect.
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks
1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_local_peak_proximity.
6. Validate four_b_full_window_peak_proximity.
7. Reject price-only local 4B as full 4B unless non-price 4B evidence exists.
8. Validate 4C protection labels.
9. Validate calibration_usable filtering.
10. Validate same_entry_group_id.
11. Validate dedupe_for_aggregate.
12. Aggregate metrics must not double-count trigger rows sharing the same same_entry_group_id.
13. Validate raw_component_scores_before/after in score_simulation rows.
14. Validate before/after profile comparison rows.
15. Validate score-return alignment labels.
16. Validate Validation Scope / Non-Validation Scope and reject deltas for unvalidated gates.
17. Append valid case rows to abstract case library.
18. Append valid trigger rows to trigger calibration dataset.
19. Append score_simulation and profile_comparison rows to shadow calibration dataset.
20. Append shadow weight rows to shadow calibration profile only if before/after backtest effect and component-level explanation exist.
21. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
22. Add tests for optimization decision validation.
23. Add tests for aggregate deduplication by same_entry_group_id.
24. Produce checkpoint summary.

### Expected output
- Concise implementation summary.
- Files changed.
- Tests run.
- Rows accepted.
- Rows rejected and why.
- Shadow profile rows accepted.
- Shadow weight rows accepted.
- Shadow weight rows rejected.
- No investment recommendation language.


## 29. Next Round State
|field|value|
|---|---|
|current_round|R8|
|current_loop|7|
|next_round|R9|
|next_loop|7|
|next_sector|모빌리티·운송·레저|
|notes|R13 이후에는 다시 R1부터 반복.|

## 30. Source Notes
- Price source: Songdaiki/stock-web `atlas/manifest.json`, `atlas/schema.json`, symbol profiles, and `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv` rows.
- Stock-web manifest max_date used for all forward-window eligibility: 2026-02-20.
- Evidence source types: public company notices, launch/news reports, app-market/ranking reports, earnings/report commentary, and public event news. Evidence was used only if knowable at or before trigger_date.
- Relative market/sector returns were left `unavailable`; this round calibrates core trigger return using stock-web OHLC and does not invent sector index data.
- 위메이드 112040 was excluded from weight calibration because the stock-web profile lists corporate-action candidate dates 2021-09-13 and 2021-10-06, overlapping the MIR4/WEMIX calibration window.
