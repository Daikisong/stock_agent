---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 104
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: CONTENT_IP_GAME_MUSIC_MONETIZATION_SECOND_PASS_TO_30_PLATFORM_MG_RECURRING_REVENUE_VS_ONE_OFF_LAUNCH_AND_LABEL_TRUST_BREAK
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R v12 Residual Research — R8 / C27 Content IP Global Monetization second pass to 30

## 1. Selection rationale

이번 loop는 `V12_Research_No_Repeat_Index.md`의 coverage-first rule을 따른다. Static index 기준 C27은 21 rows / need 9로 Priority 0이며, 직전 conversation-local ledger 기준으로는 C27이 26 rows까지 보강된 상태였다. 따라서 이번 실행의 목적은 **C27_CONTENT_IP_GLOBAL_MONETIZATION을 신규 symbol 4개로 30-row floor까지 채우는 것**이다.

C27은 “콘텐츠/IP가 있다”가 아니라, 그 IP가 **플랫폼 MG, 라이선스, 글로벌 매출, 반복 결제/사용자 지표, segment margin, 현금흐름**으로 바뀌는지를 검증해야 한다. 이번 pass는 직전 C27에서 이미 사용한 드라마/콘텐츠 제작사 계열을 피하고, 게임 IP와 음악 IP로 symbol universe를 넓혔다.

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
static_index_rows_before = 21
static_index_rows_after_if_accepted = 25
conversation_local_rows_before = 26
conversation_local_rows_after_if_accepted = 30
coverage_floor_status_after_this_run = C27 reaches 30-row Priority 0 floor
```

## 2. Price atlas validation scope

Stock-Web manifest check:

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year"
}
```

All price paths below use actual 1D OHLCV rows from:

```text
atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv
```

Corporate-action contamination rule:

```text
- 259960 / 크래프톤: corporate_action_candidate_count=0 -> usable
- 251270 / 넷마블: corporate_action_candidate_count=0 -> usable
- 225570 / 넥슨게임즈: corporate_action_candidate_dates=2017-06-12, 2018-05-09, 2022-04-15 -> outside 2024 180D windows -> usable
- 352820 / 하이브: corporate_action_candidate_count=0 -> usable
```

Non-price evidence caveat:

```text
source_proxy_only = true
evidence_url_pending = true
non_price_event_dates_are_used_as_proxy_labels_for_historical_calibration_only
```

## 3. Case set overview

| case_id | ticker | name | entry_date | entry_price | trigger_type | expected route | 180D result | classification |
|---|---:|---|---:|---:|---|---|---|---|
| C27-R8-L104-01 | 259960 | 크래프톤 | 2024-02-13 | 219500 | Stage3-Yellow | durable IP monetization / global live-service cash bridge | MFE +61.7%, MAE -4.3% | positive |
| C27-R8-L104-02 | 251270 | 넷마블 | 2024-05-08 | 59500 | Stage3-Yellow | launch hit requires revenue rank retention + margin bridge | MFE +21.7%, MAE -12.3% | mixed_positive |
| C27-R8-L104-03 | 225570 | 넥슨게임즈 | 2024-07-03 | 18610 | Stage3-Yellow | one-off launch momentum should stay local 4B unless retention bridge appears | MFE +23.1%, MAE -29.9% | counterexample |
| C27-R8-L104-04 | 352820 | 하이브 | 2024-04-22 | 233500 | 4C | label/IP governance break can override IP strength | MFE +2.1%, MAE -23.5% | counterexample |

Aggregate balance:

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4
```

## 4. Trigger-level price path notes

### 4.1 C27-R8-L104-01 — 크래프톤 / 259960

Price path anchor:

```text
entry_date = 2024-02-13
entry_price = 219500
near_entry_rows:
2024-02-13 o=219500 h=230000 l=219000 c=230000
2024-02-14 o=227500 h=243000 l=226500 c=239500
2024-03-27 o=250000 h=265000 l=248000 c=257000
2024-06-21 o=293000 h=297000 l=290000 c=297000
2024-08-22 o=346500 h=355000 l=337000 c=346000
```

Interpretation:

크래프톤은 단일 타이틀 테마가 아니라 live-service IP의 반복 monetization, 글로벌 매출 visibility, 비용 통제/마진 개선이 같이 붙은 케이스로 분류한다. 가격경로도 30D에서 이미 positive였고 90D/180D로 갈수록 MFE가 커졌다. 이 케이스는 C27에서 “콘텐츠/IP + 글로벌 매출 + recurring cash bridge”가 있으면 Stage3-Yellow 이상을 허용할 수 있음을 보강한다.

### 4.2 C27-R8-L104-02 — 넷마블 / 251270

Price path anchor:

```text
entry_date = 2024-05-08
entry_price = 59500
near_entry_rows:
2024-05-08 o=59500 h=62600 l=58700 c=60700
2024-05-09 o=65900 h=65900 l=61100 c=64800
2024-05-10 o=68500 h=72400 l=66500 c=69400
2024-06-24 o=53800 h=54500 l=52400 c=52800
2024-07-12 o=60800 h=64100 l=60800 c=63300
```

Interpretation:

신작 launch/event는 즉시 MFE를 만들었지만 이후 drawdown도 빠르게 커졌다. IP/title event 자체가 아니라 **매출 순위 유지, monetization 효율, marketing cost, segment margin**을 확인해야 full Stage3로 갈 수 있다. 이 케이스는 “one-off launch hit → local 4B 또는 Stage2-Actionable watch”로 먼저 두고, 2~3개 분기 확인 전 Green을 막는 쪽이 맞다.

### 4.3 C27-R8-L104-03 — 넥슨게임즈 / 225570

Price path anchor:

```text
entry_date = 2024-07-03
entry_price = 18610
near_entry_rows:
2024-07-03 o=18610 h=18950 l=16490 c=17900
2024-07-04 o=18700 h=19630 l=17720 c=19200
2024-07-08 o=20500 h=22400 l=20050 c=21500
2024-07-10 o=19980 h=22000 l=18040 c=21850
2024-07-16 o=18200 h=18200 l=17200 c=17550
```

Interpretation:

The First Descendant launch 주변의 가격반응은 매우 강한 local MFE를 만들었지만, 제목 단위 이벤트는 retention / ARPU / platform margin / live-ops endurance가 붙지 않으면 C27 durable monetization이 아니다. price-only launch strength를 full Stage3로 확장하면 high-MAE false positive가 발생한다.

### 4.4 C27-R8-L104-04 — 하이브 / 352820

Price path anchor:

```text
entry_date = 2024-04-22
entry_price = 233500
near_entry_rows:
2024-04-22 o=233500 h=238500 l=206000 c=212500
2024-04-23 o=209000 h=212500 l=202500 c=210000
2024-05-21 o=190300 h=191200 l=187900 c=188000
2024-07-17 o=185600 h=186500 l=182400 c=182500
2024-07-19 o=183500 h=184600 l=178700 c=182500
```

Interpretation:

음악 IP와 fandom monetization은 구조적으로 강한 C27 재료가 될 수 있지만, label governance / artist pipeline trust / internal conflict가 깨지면 IP premium이 곧바로 할인된다. 이 케이스는 C27의 hard 4C route를 보강한다. IP가 강해도 **권리·운영·계약 신뢰**가 깨지면 Stage3가 아니라 4C가 먼저다.

## 5. Machine-readable case rows

```jsonl
{"row_type":"case","case_id":"C27-R8-L104-01","ticker":"259960","name":"크래프톤","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_LIVE_SERVICE_GLOBAL_IP_MONETIZATION_CASH_BRIDGE","entry_date":"2024-02-13","entry_price":219500,"trigger_type":"Stage3-Yellow","classification":"positive","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"corporate_action_contaminated_180D_window":false}
{"row_type":"case","case_id":"C27-R8-L104-02","ticker":"251270","name":"넷마블","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_LAUNCH_MONETIZATION_RETENTION_BRIDGE_REQUIRED","entry_date":"2024-05-08","entry_price":59500,"trigger_type":"Stage3-Yellow","classification":"mixed_positive","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"corporate_action_contaminated_180D_window":false}
{"row_type":"case","case_id":"C27-R8-L104-03","ticker":"225570","name":"넥슨게임즈","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_ONE_OFF_LAUNCH_LOCAL_4B_FALSE_POSITIVE","entry_date":"2024-07-03","entry_price":18610,"trigger_type":"Stage3-Yellow","classification":"counterexample","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"corporate_action_contaminated_180D_window":false}
{"row_type":"case","case_id":"C27-R8-L104-04","ticker":"352820","name":"하이브","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MUSIC_LABEL_IP_GOVERNANCE_TRUST_BREAK_4C","entry_date":"2024-04-22","entry_price":233500,"trigger_type":"4C","classification":"counterexample","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"corporate_action_contaminated_180D_window":false}
```

## 6. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","case_id":"C27-R8-L104-01","ticker":"259960","trigger_type":"Stage3-Yellow","entry_date":"2024-02-13","entry_price":219500,"mfe_30d_pct":20.73,"mae_30d_pct":-4.33,"peak_30d_price":265000,"trough_30d_price":210000,"mfe_90d_pct":36.22,"mae_90d_pct":-4.33,"peak_90d_price":299000,"trough_90d_price":210000,"mfe_180d_pct":61.73,"mae_180d_pct":-4.33,"peak_180d_price":355000,"trough_180d_price":210000,"peak_date_180d":"2024-08-22","max_drawdown_from_peak_180d_pct":-13.24,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","validation_scope":"2024 daily tradable shard"}
{"row_type":"trigger","case_id":"C27-R8-L104-02","ticker":"251270","trigger_type":"Stage3-Yellow","entry_date":"2024-05-08","entry_price":59500,"mfe_30d_pct":21.68,"mae_30d_pct":-11.93,"peak_30d_price":72400,"trough_30d_price":52400,"mfe_90d_pct":21.68,"mae_90d_pct":-11.93,"peak_90d_price":72400,"trough_90d_price":52400,"mfe_180d_pct":21.68,"mae_180d_pct":-18.15,"peak_180d_price":72400,"trough_180d_price":48700,"peak_date_180d":"2024-05-10","max_drawdown_from_peak_180d_pct":-32.73,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","validation_scope":"2024 daily tradable shard"}
{"row_type":"trigger","case_id":"C27-R8-L104-03","ticker":"225570","trigger_type":"Stage3-Yellow","entry_date":"2024-07-03","entry_price":18610,"mfe_30d_pct":23.05,"mae_30d_pct":-5.43,"peak_30d_price":22900,"trough_30d_price":17600,"mfe_90d_pct":23.05,"mae_90d_pct":-21.01,"peak_90d_price":22900,"trough_90d_price":14700,"mfe_180d_pct":23.05,"mae_180d_pct":-29.93,"peak_180d_price":22900,"trough_180d_price":13040,"peak_date_180d":"2024-07-22","max_drawdown_from_peak_180d_pct":-43.06,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","validation_scope":"2024 daily tradable shard"}
{"row_type":"trigger","case_id":"C27-R8-L104-04","ticker":"352820","trigger_type":"4C","entry_date":"2024-04-22","entry_price":233500,"mfe_30d_pct":2.14,"mae_30d_pct":-20.04,"peak_30d_price":238500,"trough_30d_price":186700,"mfe_90d_pct":2.14,"mae_90d_pct":-23.47,"peak_90d_price":238500,"trough_90d_price":178700,"mfe_180d_pct":2.14,"mae_180d_pct":-23.47,"peak_180d_price":238500,"trough_180d_price":178700,"peak_date_180d":"2024-04-22","max_drawdown_from_peak_180d_pct":-25.07,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","validation_scope":"2024 daily tradable shard"}
```

## 7. Score / return alignment simulation

```jsonl
{"row_type":"score_simulation","case_id":"C27-R8-L104-01","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"theme_fit":18,"evidence_quality":15,"revision_visibility":15,"price_quality":14,"risk_penalty":-2,"total":60},"stage2_actionable_bonus":2.0,"simulated_total_after_bonus":62.0,"current_profile_stage":"Stage2-Actionable","proposed_c27_shadow_adjustment":"upgrade_allowed_only_if_global_live_service_cash_bridge_present","proposed_stage":"Stage3-Yellow_watch_to_green_if_margin_confirms","actual_180d_alignment":"positive"}
{"row_type":"score_simulation","case_id":"C27-R8-L104-02","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"theme_fit":18,"evidence_quality":13,"revision_visibility":8,"price_quality":16,"risk_penalty":-5,"total":50},"stage2_actionable_bonus":2.0,"simulated_total_after_bonus":52.0,"current_profile_stage":"Stage2-Actionable_or_Yellow_watch","proposed_c27_shadow_adjustment":"cap_full_stage3_until_retention_and_margin_bridge_confirmed","proposed_stage":"local_4B_or_Stage2_Actionable","actual_180d_alignment":"mixed_positive_high_MAE"}
{"row_type":"score_simulation","case_id":"C27-R8-L104-03","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"theme_fit":18,"evidence_quality":12,"revision_visibility":5,"price_quality":18,"risk_penalty":-8,"total":45},"stage2_actionable_bonus":2.0,"simulated_total_after_bonus":47.0,"current_profile_stage":"price_only_Stage3_risk","proposed_c27_shadow_adjustment":"one_off_launch_without_retention_bridge_routes_to_local_4B_not_full_Stage3","proposed_stage":"local_4B_watch","actual_180d_alignment":"counterexample_high_MAE"}
{"row_type":"score_simulation","case_id":"C27-R8-L104-04","current_profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"theme_fit":19,"evidence_quality":14,"revision_visibility":6,"price_quality":4,"risk_penalty":-18,"total":25},"stage2_actionable_bonus":0.0,"simulated_total_after_bonus":25.0,"current_profile_stage":"4C_if_trust_break_detected","proposed_c27_shadow_adjustment":"label_IP_governance_or_artist_pipeline_trust_break_overrides_IP_premium","proposed_stage":"4C","actual_180d_alignment":"counterexample_downside"}
```

## 8. Residual finding

The current global calibrated profile already blocks pure price-only blowoffs and requires non-price evidence for full 4B. C27 still needs a canonical-specific split because content/game/music IP has a uniquely dangerous shape:

```text
same visible pattern = title/platform/fandom/launch headline
actual economic paths = very different
```

Mechanism:

1. **Durable IP monetization** behaves like a toll bridge. Every existing user, season pass, platform contract, or live-service cycle sends cash through the same asset pipe. This can compound, as shown by 259960.
2. **One-off title launch** behaves like a single festival night. The street is crowded, the cameras flash, but if retention and paid conversion do not hold, the next morning the revenue bridge is gone. This explains 251270 and 225570.
3. **Label/IP governance break** is a bridge inspection failure. Even if the brand name is strong, rights, artist pipeline, and internal control are the steel beams. If those beams crack, C27 must route to 4C before IP premium is scored. This explains 352820.

## 9. Proposed C27 shadow rule candidates

```jsonl
{"row_type":"shadow_weight","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","rule_id":"C27_CONTENT_IP_MONETIZATION_BRIDGE_REQUIRED","action":"require_bridge","condition":"content_or_game_or_music_IP_headline_present","required_evidence":["platform_MG_or_license_revenue","revenue_rank_retention_or_live_service_ARPU","segment_margin_or_OPM_bridge","cash_conversion_or_repeat_sales"],"effect":"block_full_Stage3_without_bridge","production_scoring_changed":false}
{"row_type":"shadow_weight","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","rule_id":"C27_ONE_OFF_TITLE_EVENT_LOCAL_4B_CAP","action":"cap_stage","condition":"single_title_launch_or_single_hit_without_retention_evidence","max_stage":"local_4B_watch_or_Stage2_Actionable","effect":"prevent_price_only_title_launch_from_becoming_full_Stage3","production_scoring_changed":false}
{"row_type":"shadow_weight","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","rule_id":"C27_LABEL_AND_RIGHTS_TRUST_BREAK_4C_OVERRIDE","action":"route_to_4C","condition":"artist_pipeline_conflict_or_rights_control_or_label_governance_break_detected","effect":"override_IP_theme_score_and_force_4C_review","production_scoring_changed":false}
{"row_type":"shadow_weight","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","rule_id":"C27_HIGH_MAE_TITLE_EVENT_GUARD","action":"add_guardrail","condition":"30D_MFE_positive_but_90D_or_180D_MAE_exceeds_20pct_without_cash_bridge","effect":"mark_as_high_MAE_counterexample_for_stage3_strictness","production_scoring_changed":false}
```

## 10. Aggregate rows

```jsonl
{"row_type":"aggregate","selected_round":"R8","selected_loop":104,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":4,"calibration_usable_case_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":4,"conversation_local_rows_before":26,"conversation_local_rows_after_if_accepted":30,"priority_floor_reached":true}
{"row_type":"residual_contribution","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":["C27_CONTENT_IP_MONETIZATION_BRIDGE_REQUIRED","C27_ONE_OFF_TITLE_EVENT_LOCAL_4B_CAP","C27_LABEL_AND_RIGHTS_TRUST_BREAK_4C_OVERRIDE","C27_HIGH_MAE_TITLE_EVENT_GUARD"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[]}
```

## 11. Novelty / duplicate check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys in this file:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION|259960|Stage3-Yellow|2024-02-13
C27_CONTENT_IP_GLOBAL_MONETIZATION|251270|Stage3-Yellow|2024-05-08
C27_CONTENT_IP_GLOBAL_MONETIZATION|225570|Stage3-Yellow|2024-07-03
C27_CONTENT_IP_GLOBAL_MONETIZATION|352820|4C|2024-04-22
```

Conversation-local novelty check:

```text
previous_C27_symbols_observed_in_recent_pass = 253450, 035760, 036420, 160550, 241840
this_C27_symbols = 259960, 251270, 225570, 352820
symbol_overlap = 0
reused_case_count = 0
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation coding agent for Songdaiki/stock_agent.
Do not treat this MD as a production patch by itself.
Read this file together with other v12 residual research MDs.

Implement only after batch review:

1. Add C27-specific shadow rule tests around CONTENT_IP_MONETIZATION_BRIDGE_REQUIRED.
2. Add a one-off title launch cap: if content/game/music IP evidence is only a single launch/hit/headline and lacks retention/revenue-rank durability, MG/license/cash conversion, or segment margin evidence, cap at local 4B / Stage2-Actionable and block full Stage3.
3. Add a label/rights/governance trust break override for music/content IP cases. If artist pipeline, label governance, rights ownership, or contractual trust breaks, route to 4C review even if the IP theme score is high.
4. Add high-MAE title event guard: 30D MFE alone must not upgrade C27 if 90D/180D MAE exceeds 20% and non-price monetization bridge is missing.
5. Keep production_scoring_changed=false until these are batch-validated against all C27 and R13 high-MAE research files.
```

## 13. Completion state

```text
completed_round = R8
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = CONTENT_IP_GAME_MUSIC_MONETIZATION_SECOND_PASS_TO_30_PLATFORM_MG_RECURRING_REVENUE_VS_ONE_OFF_LAUNCH_AND_LABEL_TRUST_BREAK

new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable case 수 = 4
calibration_usable trigger 수 = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4

auto_selected_coverage_gap_static_index = C27 rows 21 -> 25 if accepted
auto_selected_coverage_gap_conversation_local = C27 rows 26 -> 30 if accepted; C27 30-row Priority 0 floor reached

sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false

new_axis_proposed = C27_CONTENT_IP_MONETIZATION_BRIDGE_REQUIRED | C27_ONE_OFF_TITLE_EVENT_LOCAL_4B_CAP | C27_LABEL_AND_RIGHTS_TRUST_BREAK_4C_OVERRIDE | C27_HIGH_MAE_TITLE_EVENT_GUARD
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null

next_recommended_archetypes = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```
