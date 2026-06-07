# e2r stock-web v12 residual research — R8 loop 104 — C27_CONTENT_IP_GLOBAL_MONETIZATION

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R8
selected_loop = 104
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale

C27 is still a Priority 0 thin archetype. The no-repeat index lists C27 at 24 rows, 17 symbols, with top-covered symbols concentrated in `035760`, `251270`, `035900`, `194480`, `419530`, and `036420`.
This run avoids those crowded top-covered names and adds a fresh 2024 case set around K-pop label risk, paid fan-platform subscription monetization, and drama global-hit monetization.

This run also avoids repeating the older C27 loop 96 2023 set. It keeps the prior axis but tests a newer market regime: global K-pop labels entered a harder 2024 period where album/export weakness and BTS hiatus/NewJeans conflict created pressure, while platform/subscription and drama-hit evidence still needed company-level revenue and margin conversion.

## 2. Price source validation

`Songdaiki/stock-web` is used only as price atlas. No live scan and no `stock_agent` source-code read were performed.

| symbol | name | profile path | OHLC shard used | caveat |
|---|---|---|---|---|
| 041510 | 에스엠 | `atlas/symbol_profiles/041/041510.json` | `atlas/ohlcv_tradable_by_symbol_year/041/041510/2024.csv` | active_like; old corporate-action dates only |
| 122870 | 와이지엔터테인먼트 | `atlas/symbol_profiles/122/122870.json` | `atlas/ohlcv_tradable_by_symbol_year/122/122870/2024.csv` | active_like; old corporate-action dates only |
| 376300 | 디어유 | `atlas/symbol_profiles/376/376300.json` | `atlas/ohlcv_tradable_by_symbol_year/376/376300/2024.csv` | active_like; no corporate-action caveat |
| 253450 | 스튜디오드래곤 | `atlas/symbol_profiles/253/253450.json` | `atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv` | active_like; no corporate-action caveat |

## 3. External evidence spine

### 3.1 K-pop global label pressure

Reuters Breakingviews on 2024-05-31 framed the 2024 K-pop setup as more than a BTS issue: the large Korean music agencies had strong past sales, but market value had fallen sharply from peak levels, with pressure from BTS hiatus, falling physical CD/export demand, inflation, lower China exports, and Hybe's NewJeans-related conflict. This is a useful negative trigger family for C27 because it tests whether global fandom/IP labels still deserve Stage2/Stage3 treatment without repeat monetization evidence.

### 3.2 Platform and fan subscription route

DearU/Bubble is a clean C27 adjacent route because it is not only a label or artist schedule story. Its product axis is paid artist-to-fan messaging and subscription/community monetization. That route can support C27, but only if subscriber retention, paid ARPU, artist coverage, revenue growth, and margin/revision bridge are visible.

### 3.3 Drama global-hit route

Queen of Tears is a strong global-content hit source-proxy. It became tvN's highest-rated series and accumulated very large Netflix viewing hours. For C27, however, the residual question is whether a hit converts into repeatable library/platform sales and margin revision for the listed production company.

## 4. Case table

| case | symbol | classification | entry | peak/trough | MFE | MAE | C27 lesson |
|---|---:|---|---|---|---:|---:|---|
| SM global K-pop label weak bridge | 041510 | counterexample | 2024-05-31 close 91,300 | peak 2024-05-31 high 92,000 / trough 2024-09-09 low 55,100 | +0.77% | -39.65% | K-pop global IP label failed without repeat monetization and margin bridge. |
| YG artist schedule option high-MAE | 122870 | high-MFE/high-MAE boundary | 2024-05-31 close 43,650 | peak 2024-11-25 high 51,400 / trough 2024-09-09 low 29,950 | +17.75% | -31.39% | Artist-schedule option can rally later, but drawdown is too deep for Green without confirmed tour/release/revenue bridge. |
| DearU fan-platform subscription rerating | 376300 | positive with high-MAE 4B watch | 2024-05-31 close 25,650 | peak 2024-11-25 high 41,950 / trough 2024-09-09 low 17,640 | +63.55% | -31.23% | Paid fan-platform subscription can work, but subscriber retention/revision evidence is required before Green. |
| Studio Dragon Queen of Tears hit | 253450 | one-hit boundary counterexample | 2024-04-29 close 42,450 | peak 2024-11-27 high 49,650 / trough 2024-08-05 low 33,000 | +16.96% | -22.26% | A global drama hit is not enough without repeat platform/library margin bridge. |

## 5. Residual interpretation

C27 has two different engines that the current profile should keep separate:

1. **Repeat-monetization engine**: fan-platform subscription, recurring paid content, tour/release cadence, platform distribution plus margin/revision evidence.
2. **Headline engine**: global drama hit, K-pop label name, comeback option, album sales narrative, platform listing headline.

The first engine can deserve Stage2-Actionable or Stage3-Yellow, but the second should remain Stage2-watch/4B unless the non-price bridge is explicit. In 2024, global K-pop label visibility was like a bright storefront with thinner footfall inside: the sign still pulled attention, but the cash register needed proof.

## 6. Shadow rule candidate

```text
new_axis_proposed = c27_repeat_ip_monetization_subscriber_retention_and_margin_bridge_required

For C27 Stage2-Actionable:
  require at least two of:
    - repeatable IP monetization evidence
    - subscriber/retention/paid fandom metric
    - global platform or distribution deal with company-level revenue impact
    - tour/release cadence tied to revenue revision
    - margin or operating leverage bridge

Downgrade to Stage2-watch or 4B if:
  - one-off drama hit only
  - K-pop label/album headline but album/export slowdown present
  - artist comeback schedule option without confirmed tour/release/revenue bridge
  - fan-platform label without subscriber retention or ARPU evidence
  - MFE > 15% but MAE worse than -20% before evidence confirmation
```

## 7. Machine-readable rows

```jsonl
{"row_type":"price_source_validation","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":104,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","price_source":"Songdaiki/stock-web","manifest_path":"atlas/manifest.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","symbols_validated":["041510","122870","376300","253450"],"validation_scope":"symbol_profile + yearly OHLCV shard lines; no live scan; no stock_agent code access"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_SM_2024_KPOP_ALBUM_SLOWDOWN_GLOBAL_IP_WEAK_BRIDGE","symbol":"041510","name":"에스엠","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":91300,"trigger_type":"stage2_false_positive_kpop_global_ip_album_slowdown_no_repeat_margin_bridge","trigger_family":"KPOP_GLOBAL_FANDOM_MONETIZATION_ALBUM_SLOWDOWN_AND_CHINA_EXPORT_PRESSURE","classification":"counterexample","stage_proxy":"Stage2_false_positive_to_4B_watch","peak_date":"2024-05-31","peak_high":92000,"trough_date":"2024-09-09","trough_low":55100,"mfe_pct":0.77,"mae_pct":-39.65,"lesson":"K-pop global IP label alone failed when album/export slowdown and weak repeat monetization bridge dominated.","evidence_url_status":"source_proxy_only","calibration_usable":true,"novelty_status":"same_archetype_new_symbol_or_new_trigger_family"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_SM_2024_KPOP_ALBUM_SLOWDOWN_GLOBAL_IP_WEAK_BRIDGE","symbol":"041510","name":"에스엠","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":91300,"trigger_type":"stage2_false_positive_kpop_global_ip_album_slowdown_no_repeat_margin_bridge","trigger_family":"KPOP_GLOBAL_FANDOM_MONETIZATION_ALBUM_SLOWDOWN_AND_CHINA_EXPORT_PRESSURE","classification":"counterexample","stage_proxy":"Stage2_false_positive_to_4B_watch","peak_date":"2024-05-31","peak_high":92000,"trough_date":"2024-09-09","trough_low":55100,"mfe_pct":0.77,"mae_pct":-39.65,"lesson":"K-pop global IP label alone failed when album/export slowdown and weak repeat monetization bridge dominated.","evidence_url_status":"source_proxy_only","aggregate_representative":true,"hard_duplicate_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|041510|stage2_false_positive_kpop_global_ip_album_slowdown_no_repeat_margin_bridge|2024-05-31"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_YG_2024_ARTIST_SCHEDULE_AND_PLATFORM_OPTION_HIGH_MAE","symbol":"122870","name":"와이지엔터테인먼트","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":43650,"trigger_type":"stage2_content_ip_artist_schedule_option_without_confirmed_monetization","trigger_family":"KPOP_ARTIST_SCHEDULE_AND_GLOBAL_FANDOM_OPTION_VALUE","classification":"high_mfe_high_mae_boundary_counterexample","stage_proxy":"Stage2_watch_to_4B_watch","peak_date":"2024-11-25","peak_high":51400,"trough_date":"2024-09-09","trough_low":29950,"mfe_pct":17.75,"mae_pct":-31.39,"lesson":"Artist comeback/platform option can make a rally, but without schedule, release cadence, tour and margin bridge it remains a 4B watch.","evidence_url_status":"source_proxy_only","calibration_usable":true,"novelty_status":"same_archetype_new_symbol_or_new_trigger_family"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_YG_2024_ARTIST_SCHEDULE_AND_PLATFORM_OPTION_HIGH_MAE","symbol":"122870","name":"와이지엔터테인먼트","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":43650,"trigger_type":"stage2_content_ip_artist_schedule_option_without_confirmed_monetization","trigger_family":"KPOP_ARTIST_SCHEDULE_AND_GLOBAL_FANDOM_OPTION_VALUE","classification":"high_mfe_high_mae_boundary_counterexample","stage_proxy":"Stage2_watch_to_4B_watch","peak_date":"2024-11-25","peak_high":51400,"trough_date":"2024-09-09","trough_low":29950,"mfe_pct":17.75,"mae_pct":-31.39,"lesson":"Artist comeback/platform option can make a rally, but without schedule, release cadence, tour and margin bridge it remains a 4B watch.","evidence_url_status":"source_proxy_only","aggregate_representative":true,"hard_duplicate_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|122870|stage2_content_ip_artist_schedule_option_without_confirmed_monetization|2024-05-31"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_DEARU_2024_FAN_PLATFORM_SUBSCRIPTION_RERATING_HIGH_MAE","symbol":"376300","name":"디어유","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":25650,"trigger_type":"stage2_actionable_fan_platform_subscription_monetization_but_high_mae","trigger_family":"FAN_PLATFORM_SUBSCRIPTION_RECURRING_MONETIZATION","classification":"positive_with_high_mae_4b_watch","stage_proxy":"Stage3_Yellow_possible_but_4B_watch","peak_date":"2024-11-25","peak_high":41950,"trough_date":"2024-09-09","trough_low":17640,"mfe_pct":63.55,"mae_pct":-31.23,"lesson":"Recurring paid fan-message platform can rerate later, but the drawdown shows that subscriber/revenue/retention evidence is required before Green.","evidence_url_status":"source_proxy_only","calibration_usable":true,"novelty_status":"same_archetype_new_symbol_or_new_trigger_family"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_DEARU_2024_FAN_PLATFORM_SUBSCRIPTION_RERATING_HIGH_MAE","symbol":"376300","name":"디어유","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":25650,"trigger_type":"stage2_actionable_fan_platform_subscription_monetization_but_high_mae","trigger_family":"FAN_PLATFORM_SUBSCRIPTION_RECURRING_MONETIZATION","classification":"positive_with_high_mae_4b_watch","stage_proxy":"Stage3_Yellow_possible_but_4B_watch","peak_date":"2024-11-25","peak_high":41950,"trough_date":"2024-09-09","trough_low":17640,"mfe_pct":63.55,"mae_pct":-31.23,"lesson":"Recurring paid fan-message platform can rerate later, but the drawdown shows that subscriber/revenue/retention evidence is required before Green.","evidence_url_status":"source_proxy_only","aggregate_representative":true,"hard_duplicate_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|376300|stage2_actionable_fan_platform_subscription_monetization_but_high_mae|2024-05-31"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_STUDIODRAGON_2024_QUEEN_OF_TEARS_GLOBAL_HIT_NOT_ENOUGH_FOR_MARGIN_GREEN","symbol":"253450","name":"스튜디오드래곤","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":42450,"trigger_type":"stage2_content_ip_global_hit_without_repeat_margin_bridge","trigger_family":"DRAMA_GLOBAL_PLATFORM_HIT_AND_LIBRARY_MONETIZATION","classification":"boundary_counterexample","stage_proxy":"Stage2_watch_to_4B_watch","peak_date":"2024-11-27","peak_high":49650,"trough_date":"2024-08-05","trough_low":33000,"mfe_pct":16.96,"mae_pct":-22.26,"lesson":"A global drama hit can validate IP reach, but one hit is not enough unless library sales, repeat platform deals and margin/revision bridge appear.","evidence_url_status":"source_proxy_only","calibration_usable":true,"novelty_status":"same_archetype_new_symbol_or_new_trigger_family"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_STUDIODRAGON_2024_QUEEN_OF_TEARS_GLOBAL_HIT_NOT_ENOUGH_FOR_MARGIN_GREEN","symbol":"253450","name":"스튜디오드래곤","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":42450,"trigger_type":"stage2_content_ip_global_hit_without_repeat_margin_bridge","trigger_family":"DRAMA_GLOBAL_PLATFORM_HIT_AND_LIBRARY_MONETIZATION","classification":"boundary_counterexample","stage_proxy":"Stage2_watch_to_4B_watch","peak_date":"2024-11-27","peak_high":49650,"trough_date":"2024-08-05","trough_low":33000,"mfe_pct":16.96,"mae_pct":-22.26,"lesson":"A global drama hit can validate IP reach, but one hit is not enough unless library sales, repeat platform deals and margin/revision bridge appear.","evidence_url_status":"source_proxy_only","aggregate_representative":true,"hard_duplicate_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|253450|stage2_content_ip_global_hit_without_repeat_margin_bridge|2024-04-29"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_SM_2024_KPOP_ALBUM_SLOWDOWN_GLOBAL_IP_WEAK_BRIDGE","symbol":"041510","baseline_proxy_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage2_or_Yellow_false_positive","shadow_c27_stage":"4B_watch_only","raw_component_score_breakdown":{"global_ip_reach":12,"repeat_monetization":3,"platform_distribution":5,"operating_leverage":2,"revision_visibility":2,"risk_penalty":-18},"alignment":"current_profile_error","error_type":"global_kpop_label_without_repeat_monetization_margin_bridge"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_YG_2024_ARTIST_SCHEDULE_AND_PLATFORM_OPTION_HIGH_MAE","symbol":"122870","baseline_proxy_stage":"Stage2","current_calibrated_profile_stage":"Stage2_false_positive_or_4B_watch","shadow_c27_stage":"4B_watch","raw_component_score_breakdown":{"global_ip_reach":14,"repeat_monetization":5,"platform_distribution":6,"operating_leverage":4,"revision_visibility":3,"risk_penalty":-14},"alignment":"partial_current_profile_error","error_type":"artist_schedule_option_without_confirmed_revenue_bridge"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_DEARU_2024_FAN_PLATFORM_SUBSCRIPTION_RERATING_HIGH_MAE","symbol":"376300","baseline_proxy_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage3_Yellow_possible_but_late","shadow_c27_stage":"Stage3_Yellow_after_subscriber_retention_bridge + high_MAE_4B_watch","raw_component_score_breakdown":{"global_ip_reach":12,"repeat_monetization":19,"platform_distribution":17,"operating_leverage":9,"revision_visibility":6,"risk_penalty":-12},"alignment":"positive_but_requires_late_confirmation","error_type":"high_mae_before_subscription_platform_rerating"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_id":"C27_STUDIODRAGON_2024_QUEEN_OF_TEARS_GLOBAL_HIT_NOT_ENOUGH_FOR_MARGIN_GREEN","symbol":"253450","baseline_proxy_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage2_or_Yellow_false_positive","shadow_c27_stage":"4B_watch_until_repeat_platform_margin_bridge","raw_component_score_breakdown":{"global_ip_reach":20,"repeat_monetization":6,"platform_distribution":13,"operating_leverage":3,"revision_visibility":4,"risk_penalty":-13},"alignment":"current_profile_error","error_type":"one_off_global_hit_without_repeat_margin_bridge"}
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","case_count":4,"trigger_count":4,"positive_case_count":1,"counterexample_count":3,"boundary_case_count":2,"current_profile_error_count":4,"median_mfe_pct":17.36,"median_mae_pct":-31.31,"mean_mfe_pct":24.76,"mean_mae_pct":-31.13,"residual_axis":"repeat_ip_monetization_subscriber_retention_platform_margin_bridge_vs_global_hit_or_kpop_label","do_not_propose_new_weight_delta":false}
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","new_axis_proposed":"c27_repeat_ip_monetization_subscriber_retention_and_margin_bridge_required","shadow_rule_candidate":{"require_for_stage2_actionable":["repeatable_ip_monetization_evidence","subscriber_or_fandom_retention_metric_or_platform_distribution","margin_or_revenue_revision_bridge"],"downgrade_to_watch_only_if":["one_off_drama_hit_only","album_sales_or_china_export_slowdown","artist_schedule_option_without_confirmed_tour_release_revenue","platform_label_without_paid_subscriber_retention"],"force_4b_watch_if":["mfe_gt_15pct_but_mae_worse_than_minus_20pct","global_platform_headline_without_company_level_margin_conversion","structural_kpop_album_slowdown_present"]},"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c27_repeat_ip_monetization_subscriber_retention_and_margin_bridge_required","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C27 K-pop/global fandom/fan platform/drama global hit rallies","existing_axis_weakened":null,"next_recommended_archetypes":["C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","C13_BATTERY_JV_UTILIZATION_AMPC_IRA","C24_BIO_TRIAL_DATA_EVENT_RISK"]}
{"row_type":"coverage_matrix","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"104","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","selected_priority_bucket":"Priority 0","auto_selected_coverage_gap":"C27 rows 24, 30-row target까지 6 부족, 50-row target까지 26 부족","new_independent_case_count":4,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
Do not execute this in the research session.

You are a coding agent applying accumulated v12 residual research MDs to stock_agent.
Read this MD and extract only machine-readable rows from the JSONL block.
Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
Do not change production scoring directly.
Stage all proposed effects as shadow_weight_only unless a separate approved patch instruction exists.
For C27_CONTENT_IP_GLOBAL_MONETIZATION, consider adding a shadow guard:
  repeat IP monetization + subscriber/retention/platform distribution + margin/revision bridge required.
Downgrade one-off global drama hit, K-pop label headline, album-sales narrative, or artist-schedule option to Stage2-watch/4B unless company-level monetization and revision bridge are present.
```

## 9. Final execution summary

selected_round: R8
selected_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: KPOP_FAN_PLATFORM_AND_DRAMA_GLOBAL_IP_REPEAT_MONETIZATION_BRIDGE_VS_ONE_OFF_HIT_OR_ALBUM_LABEL_FALSE_POSITIVE

new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 4
positive_case_count: 1
counterexample_count: 3
boundary_case_count: 2
current_profile_error_count: 4
verified_url_repair_needed_count: 4

diversity_score_summary: C27 Priority 0 보강 + SM global K-pop label weak-bridge counterexample + YG artist-schedule option high-MFE/high-MAE boundary + DearU paid fan-platform subscription positive/high-MAE 4B watch + Studio Dragon Queen of Tears one-hit global drama boundary counterexample
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C27 rows 24, 30-row target까지 6 부족, 50-row target까지 26 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c27_repeat_ip_monetization_subscriber_retention_and_margin_bridge_required
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C27 K-pop/global fandom/fan platform/drama global hit rallies
existing_axis_weakened: null
next_recommended_archetypes: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK
