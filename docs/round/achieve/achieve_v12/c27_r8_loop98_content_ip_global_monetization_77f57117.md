# E2R Stock-Web v12 Residual Research — R8 loop 98 / L8 / C27

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 98
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_LIVEOPS_LAUNCH_MONETIZATION_BRIDGE_VS_ARTIST_IP_LABEL_GOVERNANCE_CYCLE_DECAY_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - game_IP_liveops_monetization_bridge_test
  - global_launch_revenue_retention_guardrail
  - artist_IP_governance_cycle_false_stage2_guard
  - content_label_high_MAE_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C27_CONTENT_IP_GLOBAL_MONETIZATION` 전용 residual research다.

C27은 “게임 IP”, “글로벌 출시”, “K-pop IP”, “아티스트 팬덤”, “웹툰/드라마 IP”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 IP가 실제 global DAU/MAU, live-ops retention, ARPU, launch revenue decay curve, platform fee, artist activity schedule, margin, FCF, EPS revision으로 내려오는지다.

```text
content IP / global monetization headline
  → launch, live-ops, fandom, distribution depth
  → retention, ARPU, repeat purchase, artist schedule, platform fee
  → revenue, margin, FCF, EPS revision bridge
  → stock-web 1D OHLC forward path
```

콘텐츠 IP는 무대 위 조명과 같다. 조명이 켜지는 순간은 화려하지만, 돈은 관객이 다시 들어오고, 굿즈와 결제와 구독이 반복될 때 남는다. C27은 “IP가 있다”와 “IP가 반복 매출로 변한다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["259960","251270","352820","035900"],"profile_paths":["atlas/symbol_profiles/259/259960.json","atlas/symbol_profiles/251/251270.json","atlas/symbol_profiles/352/352820.json","atlas/symbol_profiles/035/035900.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv","atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv","atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv","atlas/ohlcv_tradable_by_symbol_year/035/035900/2024.csv"],"validation_scope":"2024 trigger-level forward path; 259960, 251270, 352820 have zero corporate-action candidates. 035900 caveats are historical and end 2013, outside selected 2024 local windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C27 at 24 rows, 6 rows short of the 30-row minimum stability zone.
- Existing registry shows C27 parsed through `R8 loop 97`.
- This output uses `R8 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C27 loop 97 emphasized media studio / kids animation / content distribution. This file shifts to game IP live-ops, game launch monetization, artist IP governance/cycle decay, and K-pop activity schedule false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C27-R8L98-01 | 259960 | 크래프톤 | 2024-02-13 | 2024-02-13 | 230000 | 355000 | 217500 | 54.35% | -5.43% | Global game IP/live-ops monetization path worked with controlled MAE. |
| C27-R8L98-02 | 251270 | 넷마블 | 2024-05-08 | 2024-05-08 | 60700 | 72400 | 52400 | 19.28% | -13.67% | Global game launch IP created MFE, but launch decay and retention proof are required. |
| C27-R8L98-03 | 352820 | 하이브 | 2024-03-27 | 2024-03-27 | 224000 | 236000 | 157700 | 5.36% | -29.60% | Artist IP/global fandom label failed without clean schedule, governance, and margin bridge. |
| C27-R8L98-04 | 035900 | JYP Ent. | 2024-03-27 | 2024-03-27 | 72500 | 74900 | 43100 | 3.31% | -40.55% | K-pop IP cycle label produced tiny MFE and severe MAE; hard false Stage2 candidate. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C27-R8L98-01","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_REVENUE_MARGIN_BRIDGE","symbol":"259960","name":"크래프톤","trigger_type":"game_ip_global_liveops_revenue_margin_bridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":230000,"peak_price":355000,"peak_date":"2024-08-22","trough_price":217500,"trough_date":"2024-02-26","mfe_pct":54.35,"mae_pct":-5.43,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_liveops_ARPU_margin_URLs","residual_flag":"positive_game_IP_liveops_path_but_requires_retention_ARPU_margin_FCF_URLs","dedupe_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|259960|game_ip_global_liveops_revenue_margin_bridge|2024-02-13"}
{"row_type":"trigger","case_id":"C27-R8L98-02","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LAUNCH_MONETIZATION_WITH_RETENTION_GUARD","symbol":"251270","name":"넷마블","trigger_type":"game_ip_global_launch_monetization_with_retention_guard","trigger_date":"2024-05-08","entry_date":"2024-05-08","entry_price":60700,"peak_price":72400,"peak_date":"2024-05-10","trough_price":52400,"trough_date":"2024-06-24","mfe_pct":19.28,"mae_pct":-13.67,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_launch_decay_guard","residual_flag":"game_launch_IP_MFE_positive_but_retention_revenue_decay_margin_bridge_required","dedupe_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|251270|game_ip_global_launch_monetization_with_retention_guard|2024-05-08"}
{"row_type":"trigger","case_id":"C27-R8L98-03","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_IP_GLOBAL_FANDOM_GOVERNANCE_CYCLE_FALSE_STAGE2","symbol":"352820","name":"하이브","trigger_type":"artist_ip_global_fandom_governance_cycle_false_stage2","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":224000,"peak_price":236000,"peak_date":"2024-04-01","trough_price":157700,"trough_date":"2024-09-23","mfe_pct":5.36,"mae_pct":-29.60,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"artist_IP_fandom_label_low_MFE_high_MAE_without_schedule_governance_margin_bridge","dedupe_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|352820|artist_ip_global_fandom_governance_cycle_false_stage2|2024-03-27"}
{"row_type":"trigger","case_id":"C27-R8L98-04","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_ARTIST_IP_ACTIVITY_SCHEDULE_LOW_MFE_HIGH_MAE","symbol":"035900","name":"JYP Ent.","trigger_type":"kpop_artist_ip_activity_schedule_low_mfe_high_mae","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":72500,"peak_price":74900,"peak_date":"2024-03-27","trough_price":43100,"trough_date":"2024-09-09","mfe_pct":3.31,"mae_pct":-40.55,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"Kpop_artist_IP_label_tiny_MFE_high_MAE_without_activity_margin_revision_bridge","dedupe_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|035900|kpop_artist_ip_activity_schedule_low_mfe_high_mae|2024-03-27"}
```

## 6. Score-return alignment

### 6.1 Game IP monetization winner family

`259960` is the cleanest C27 positive row. The forward path suggests live-ops, global monetization, ARPU/retention, and margin bridge were being repriced. `251270` also produced launch-driven MFE, but its drawdown shows that launch events need retention and revenue-decay checks before Green.

### 6.2 Artist IP label false Stage2

`352820` and `035900` are the warning family. Global fandom and artist IP can sound durable, but without activity schedule, governance clarity, platform monetization, margin and revision bridge, the forward path becomes low-MFE/high-MAE. These rows should not inherit game-IP monetization scores.

### 6.3 Mechanism

C27 should behave like a theater ledger. Opening night is not enough; the important question is whether the seats fill again, merchandise repeats, platform fees clear, and margin survives after promotion costs.

## 7. Raw component score simulation

| symbol | IP strength | monetization/retention | global distribution | margin/FCF bridge | price confirmation | MAE/governance guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 259960 | 23 | 20 | 18 | 16 | 20 | -3 | 74 | Stage3-Yellow/Green candidate |
| 251270 | 19 | 12 | 13 | 8 | 10 | -7 | 55 | Stage2→Yellow with launch-decay guard |
| 352820 | 20 | 6 | 10 | 5 | 3 | -14 | 30 | Stage2/local 4B watch |
| 035900 | 16 | 4 | 7 | 3 | 1 | -18 | 13 | Hard counterexample/local 4B |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c27_content_IP_requires_retention_monetization_margin_bridge","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"stage2_required_bridge","rule":"Do not promote content IP/global monetization labels above Stage2 unless retention, ARPU, repeat purchase, global distribution depth, artist schedule, platform fee, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["352820","035900"],"counterbalanced_by":["259960","251270"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c27_game_IP_liveops_positive_delta","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Game IP names with verified live-ops retention, ARPU, global distribution and margin/FCF bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["259960"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c27_game_launch_decay_guard","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"stage2_to_yellow_with_launch_decay_guard","rule":"Game launch IP rows can become Yellow when launch revenue is strong, but Green requires retention, post-launch decay and margin evidence.","supporting_cases":["251270"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c27_artist_IP_governance_cycle_false_stage2_guard","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"local_4b_watch_guard","rule":"Artist IP/fandom rows with low MFE and high MAE should remain local 4B watch when governance, activity schedule, margin and revision bridge are absent.","supporting_cases":["352820","035900"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c27_Kpop_activity_schedule_high_MAE_guard","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"hard_counterexample_or_local_4b","rule":"K-pop activity-cycle labels with tiny MFE and severe MAE should be hard counterexamples unless activity schedule and margin evidence repairs the row.","supporting_cases":["035900"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","round":"R8","loop":"98","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C27 should separate game IP live-ops/global launch monetization from artist IP or K-pop fandom labels that fail without activity schedule, governance clarity, retention and margin bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_launch_decay_guard","local_4b_watch_guard","hard_counterexample_or_local_4b"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","sample_count":4,"avg_mfe_pct":20.58,"avg_mae_pct":-22.31,"median_mfe_pct":12.32,"median_mae_pct":-21.64,"interpretation":"C27 upside is strongest when IP converts into live-ops retention and global monetization; artist IP labels without schedule/governance/margin evidence produce poor asymmetry."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - local 2024 OHLC rows were checked from stock-web tradable shards
  - selected local windows avoid active corporate-action contamination
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C27 R8 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c27_content_IP_requires_retention_monetization_margin_bridge -> stage2_required_bridge
  2. c27_game_IP_liveops_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c27_game_launch_decay_guard -> stage2_to_yellow_with_launch_decay_guard
  4. c27_artist_IP_governance_cycle_false_stage2_guard -> local_4b_watch_guard
  5. c27_Kpop_activity_schedule_high_MAE_guard -> hard_counterexample_or_local_4b

Expected behavior:
- Content IP/global monetization vocabulary alone should not create Green.
- Retention, ARPU, repeat purchase, global distribution depth, artist schedule, platform fee, margin, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Artist IP and K-pop activity-cycle rows with low MFE/high MAE should stay capped until non-price evidence repairs the row.
```
