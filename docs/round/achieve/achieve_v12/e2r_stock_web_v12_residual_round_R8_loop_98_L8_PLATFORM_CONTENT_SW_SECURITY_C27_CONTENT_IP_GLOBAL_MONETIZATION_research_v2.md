# E2R Stock-Web v12 Residual Research — R8 loop 98 / L8 / C27

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 98
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_LIVEOPS_KPOP_FANDOM_DRAMA_IP_GLOBAL_MONETIZATION_MARGIN_BRIDGE_VS_ARTIST_GOVERNANCE_AND_STUDIO_CONTENT_LABEL_DECAY
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - global_IP_repeat_monetization_bridge_test
  - one_off_hit_vs_recurring_liveops_guardrail
  - artist_governance_and_studio_margin_guardrail
  - high_MAE_guardrail
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

C27은 “글로벌 IP”, “K-pop”, “게임 흥행”, “드라마 콘텐츠”, “웹툰/애니메이션”이라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 콘텐츠/IP가 일회성 흥행에서 끝나는지, 아니면 liveops·fandom·플랫폼 정산·merch·licensing·windowing·margin/revision으로 반복 매출화되는지다.

```text
content/IP/global hit headline
  → repeat monetization / liveops / fandom ARPU / licensing
  → platform distribution / windowing / catalog leverage
  → margin / cash conversion / EPS revision bridge
  → stock-web 1D OHLC forward path
```

IP는 씨앗이고 monetization은 수확이다. 씨앗이 유명해도, 밭이 매년 열매를 맺으려면 플랫폼·팬덤·과금·라이선스·마진 구조가 계속 돌아야 한다. C27은 “한 번 터진 흥행”과 “반복적으로 돈이 되는 IP 엔진”을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["259960","251270","352820","253450"],"profile_paths":["atlas/symbol_profiles/259/259960.json","atlas/symbol_profiles/251/251270.json","atlas/symbol_profiles/352/352820.json","atlas/symbol_profiles/253/253450.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv","atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv","atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv","atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv"],"validation_scope":"2024 trigger-level forward path; all four selected profiles show no local 2024 corporate-action contamination in the selected windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C27 at 24 rows and asks for IP monetization, global platform conversion, and one-off hit counterexamples.
- Registry shows C27 parsed through `R8 loop 97`.
- This output uses `R8 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file focuses on game live-service monetization, game launch event-cap, K-pop fandom/artist governance risk, and drama studio content label decay.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C27-R8L98-01 | 259960 | 크래프톤 | 2024-02-13 | 2024-02-13 | 230000 | 355000 | 210500 | 54.35% | -8.48% | Global game IP/live-service monetization path worked with controlled drawdown. |
| C27-R8L98-02 | 251270 | 넷마블 | 2024-05-08 | 2024-05-08 | 60700 | 72400 | 52400 | 19.28% | -13.67% | Game IP launch rerating was tradable, but needs retention/liveops proof before Green. |
| C27-R8L98-03 | 352820 | 하이브 | 2024-03-27 | 2024-03-27 | 224000 | 238500 | 157700 | 6.47% | -29.60% | K-pop fandom/IP label decayed under artist/governance risk; false Stage2 guardrail. |
| C27-R8L98-04 | 253450 | 스튜디오드래곤 | 2024-05-09 | 2024-05-09 | 46400 | 47350 | 33000 | 2.05% | -28.88% | Drama studio/global platform label failed without content slate margin/windowing bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C27-R8L98-01","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_GAME_IP_LIVEOPS_REPEAT_MONETIZATION_MARGIN_BRIDGE","symbol":"259960","name":"크래프톤","trigger_type":"global_game_ip_liveops_repeat_monetization_margin_bridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":230000,"peak_price":355000,"peak_date":"2024-08-22","trough_price":210500,"trough_date":"2024-03-06","mfe_pct":54.35,"mae_pct":-8.48,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_liveops_margin_URLs","residual_flag":"positive_repeat_game_IP_monetization_path_but_requires_exact_liveops_ARPU_margin_URLs","dedupe_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|259960|global_game_ip_liveops_repeat_monetization_margin_bridge|2024-02-13"}
{"row_type":"trigger","case_id":"C27-R8L98-02","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_LAUNCH_RERATING_EVENT_CAP_RETENTION_GUARD","symbol":"251270","name":"넷마블","trigger_type":"game_ip_launch_rerating_event_cap_retention_guard","trigger_date":"2024-05-08","entry_date":"2024-05-08","entry_price":60700,"peak_price":72400,"peak_date":"2024-05-10","trough_price":52400,"trough_date":"2024-06-24","mfe_pct":19.28,"mae_pct":-13.67,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_retention_guard","residual_flag":"one_off_game_IP_launch_needs_retention_liveops_margin_bridge_before_Green","dedupe_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|251270|game_ip_launch_rerating_event_cap_retention_guard|2024-05-08"}
{"row_type":"trigger","case_id":"C27-R8L98-03","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"KPOP_FANDOM_IP_ARTIST_GOVERNANCE_RISK_FALSE_STAGE2","symbol":"352820","name":"하이브","trigger_type":"kpop_fandom_ip_artist_governance_risk_false_stage2","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":224000,"peak_price":238500,"peak_date":"2024-04-22","trough_price":157700,"trough_date":"2024-09-23","mfe_pct":6.47,"mae_pct":-29.60,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"Kpop_global_IP_label_without_artist_governance_and_margin_bridge_became_high_MAE_false_stage2","dedupe_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|352820|kpop_fandom_ip_artist_governance_risk_false_stage2|2024-03-27"}
{"row_type":"trigger","case_id":"C27-R8L98-04","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"DRAMA_STUDIO_GLOBAL_PLATFORM_CONTENT_LABEL_DECAY","symbol":"253450","name":"스튜디오드래곤","trigger_type":"drama_studio_global_platform_content_label_decay","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":46400,"peak_price":47350,"peak_date":"2024-05-27","trough_price":33000,"trough_date":"2024-08-05","mfe_pct":2.05,"mae_pct":-28.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_local_4B_watch","residual_flag":"global_drama_content_label_failed_without_slate_windowing_margin_bridge","dedupe_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|253450|drama_studio_global_platform_content_label_decay|2024-05-09"}
```

## 6. Score-return alignment

### 6.1 Repeat monetization winner

`259960` is the cleanest C27 positive in this sample. The path shows the difference between “game IP exists” and “game IP monetizes repeatedly.” A live-service global game with durable paying users, ARPU, platform distribution, and margin conversion can deserve stronger C27 treatment after URL verification.

### 6.2 Launch-event positive but not automatic Green

`251270` shows the middle case. A new game/IP launch can create MFE, but the forward path still needs retention, payer conversion, liveops cadence, and marketing-cost discipline. Without those, this is Stage2/Yellow or event-cap, not Green.

### 6.3 Artist governance and production-studio false positives

`352820` and `253450` show the false-positive family. K-pop and drama labels can sound globally monetizable, but artist-governance risk, slate timing, platform bargaining power, production cost, and margin recognition can dominate. The model should not score “global fandom” or “global content” as if it were verified repeat monetization.

## 7. Raw component score simulation

| symbol | IP/global evidence | repeat monetization | platform/windowing bridge | margin/revision bridge | price confirmation | MAE/logic guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 259960 | 23 | 22 | 18 | 18 | 22 | -4 | 79 | Stage3-Yellow/Green candidate |
| 251270 | 20 | 11 | 10 | 8 | 13 | -7 | 45 | Stage2/Yellow with retention guard |
| 352820 | 19 | 8 | 7 | 5 | 4 | -14 | 29 | Stage2/local 4B watch |
| 253450 | 15 | 5 | 5 | 3 | 1 | -14 | 15 | Event-cap / false Stage2 |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c27_ip_requires_repeat_monetization_margin_bridge","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"stage2_required_bridge","rule":"Do not promote content/IP/global labels above Stage2 unless repeat monetization, liveops retention, fandom ARPU, licensing, windowing, platform distribution, margin, cash conversion, or EPS revision bridge is visible.","supporting_cases":["352820","253450"],"counterbalanced_by":["259960","251270"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c27_game_liveops_positive_delta","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Global game IP with verified live-service retention, payer conversion, ARPU, and margin bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["259960"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c27_one_off_launch_event_cap_guard","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"local_4b_watch_guard","rule":"One-off game/content launches should remain event-cap or Yellow until post-launch retention, liveops cadence, and margin durability are verified.","supporting_cases":["251270"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c27_artist_governance_studio_margin_false_stage2_guard","scope":"C27_CONTENT_IP_GLOBAL_MONETIZATION","candidate_action":"false_stage2_block","rule":"K-pop artist/governance risk and drama-studio slate/windowing risk should block Green when MAE dominates MFE and no repeat-monetization margin bridge is visible.","supporting_cases":["352820","253450"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","round":"R8","loop":"98","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C27 needs sharper separation between repeat IP monetization engines and one-off hit, artist-governance, or content-slate label risk.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","local_4b_watch_guard","false_stage2_block"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","sample_count":4,"avg_mfe_pct":20.54,"avg_mae_pct":-20.16,"median_mfe_pct":12.88,"median_mae_pct":-21.28,"interpretation":"C27 can produce strong upside when IP monetization is recurring and margin-backed; content/fandom labels without repeat monetization often decay into high-MAE false Stage2 paths."}
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
  - no selected local window was rejected for corporate-action contamination
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
  1. c27_ip_requires_repeat_monetization_margin_bridge -> stage2_required_bridge
  2. c27_game_liveops_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c27_one_off_launch_event_cap_guard -> local_4b_watch_guard
  4. c27_artist_governance_studio_margin_false_stage2_guard -> false_stage2_block

Expected behavior:
- Content/IP/global vocabulary alone should not create Green.
- Repeat monetization, liveops retention, fandom ARPU, licensing, windowing, platform distribution, margin, cash conversion, or EPS revision can justify Stage3-Yellow/Green.
- One-off launch, artist-governance, and studio-slate risk should cap rows at event-cap/local 4B or false Stage2 when MAE dominates.
```
