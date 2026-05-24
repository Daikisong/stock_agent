# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

|field|value|
|---|---|
|research_session|historical_calibration_after_stock_web_ohlc_breakthrough|
|mode|historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough|
|round|R12|
|loop|2|
|sector|농업·생활서비스·기타|
|live_candidate_mode|false|
|stock_agent_repo_access_allowed|false|
|stock_agent_code_patch_allowed|false|
|production_scoring_changed|false|
|shadow_weight_only|true|
|stock_web_manifest_max_date|2026-02-20|
|generated_at_kst|2026-05-22|
|artifact_filename|e2r_stock_web_historical_calibration_round_R12_loop_2_agri_life_misc_research.md|


## 1. Round Scope

R12는 농업·생활서비스·기타이지만, 이번 샘플에서는 “농산물·식량·생활필수품·동물질병 이벤트”가 주가에 어떻게 반영됐는지를 중심으로 봤다. 중요한 결론은 단순하다. **이벤트는 Stage2-Actionable watch로는 빨랐지만, 회사별 revision/margin/contract gate가 없으면 Stage3-Green으로 승격하면 안 된다.**

검증 대상은 grain/feed shock, grain-trading shock, salt panic, animal-disease biosecurity shock이다. 구조적 EPS 리레이팅 사례는 이번 usable set에서 충분히 검증되지 않았기 때문에 structural Green weight delta는 제안하지 않는다.


## 2. Stock-Web OHLC Input / Price Source Validation

|field|value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|


Stock-web manifest confirms raw/unadjusted FinanceData/marcap price basis, `max_date=2026-02-20`, `tradable_row_count=14354401`, and the calibration-safe tradable shard root. Schema confirms `d/o/h/l/c/v/a/mc/s/m` for tradable rows and states MFE/MAE formulas and 180D/corporate-action usability rules. See Source Notes for exact repository files.


## 3. Historical Eligibility Gate

|gate|result|
|---|---|
|entry row exists|true for all 15 trigger rows|
|minimum 180 forward trading days|true|
|corporate-action contamination in 180D|none for selected windows; old historical corporate-action candidates do not overlap tested windows|
|raw/unadjusted caveat|accepted; this round is stock-web tradable_raw only|
|relative return|unavailable; core calibration retained|


## 4. Canonical Archetypes Tested

|archetype|mechanism|validated?|verdict|
|---|---|---|---|
|AGRI_FEED_GRAIN_SHOCK_EVENT_PREMIUM|global grain/feed price shock → feed/theme rally|yes|tradable Stage2 event, not structural Green|
|AGRI_GRAIN_TRADING_EVENT_PREMIUM|grain export disruption → food-security trade names|yes|excellent Stage2, violent 4B later|
|LIFE_CONSUMABLE_SALT_PANIC_EVENT_PREMIUM|treated-water anxiety → salt hoarding narrative|yes|short event cycle; late Green false-positive risk|
|ANIMAL_DISEASE_BIOSECURITY_EVENT_PREMIUM|ASF outbreak → animal-health/security names|yes|event entry worked briefly; late Yellow poor|
|AGRI_INPUT_STRUCTURAL_REVISION|fertilizer/input spread → OP revision|no|not enough company-level revision evidence in this pass|


## 5. Case Selection Summary

|case_id|symbol|company|case_type|best_trigger|calibration_usable|notes|
|---|---|---|---|---|---|---|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|005860|한일사료|event_premium_overheat|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|true|Russia-Ukraine grain/feed shock created a huge tradable event premium, but no company-specific EPS/revision gate was visible; should not become Stage3-Green without margin/revision evidence.|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|006880|신송홀딩스|stage2_promote_candidate_event_only|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|true|Early public grain shock was a better entry than later confirmation. However, lack of company-specific OP/EPS evidence means this is event-trade Stage2-Actionable, not structural Green.|
|R12L2_C03_INSANGA_SALT_PANIC_2023|277410|인산가|event_premium_and_4B_watch|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|true|Fukushima-water related salt hoarding narrative produced a fast price move. The later Green-like chase had poor MAE and should be blocked without durable demand/revision evidence.|
|R12L2_C04_EAGLEVET_ASF_2019|044960|이글벳|event_premium_false_green|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|true|ASF confirmation created a sharp animal-health theme move, but late Yellow/4B entries had poor downside protection and the COVID-era 180D drawdown made structural calibration unsafe beyond event-only use.|


## 6. Evidence Source Map

|case|evidence_date|public evidence used|source note|
|---|---|---|---|
|한일사료 / 신송홀딩스|2022-02-24~2022-04|Russia-Ukraine war disrupted grain/food markets; FAO food-price record in March 2022.|Axios/FAO food-price summary; Reuters/FAO references in Source Notes|
|인산가|2023-06~2023-08|Fukushima ALPS treated-water discharge anxiety and consumer salt-hoarding narrative.|IAEA/AP/TIME sources in Source Notes|
|이글벳|2019-09-17|South Korea first confirmed ASF case; animal-health/biosecurity theme.|ASF public-source notes in Source Notes|


## 7. Price Data Source Map

|symbol|company|profile_path|main_price_shards|profile_caveat|
|---|---|---|---|---|
|005860|한일사료|atlas/symbol_profiles/005/005860.json|atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv; 2023.csv|old corporate-action candidates exist but not in tested 2022 window|
|006880|신송홀딩스|atlas/symbol_profiles/006/006880.json|atlas/ohlcv_tradable_by_symbol_year/006/006880/2022.csv|clean; no corporate-action candidate dates|
|277410|인산가|atlas/symbol_profiles/277/277410.json|atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv; 2024.csv|SPAC/name-change event in 2018 only; tested 2023 window clean|
|044960|이글벳|atlas/symbol_profiles/044/044960.json|atlas/ohlcv_tradable_by_symbol_year/044/044960/2019.csv; 2020.csv|old corporate-action candidates before tested 2019 window|


## 8. Case-by-Case Trigger Grid

|case|trigger_id|type|date|entry|entry_px|evidence|
|---|---|---|---|---|---|---|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|Stage2|2022-02-24|2022-02-24|2555|Russia-Ukraine invasion/public grain export disruption risk; feed-cost shock became public macro evidence.|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T2_STAGE2A_RS_CONFIRMED|Stage2-Actionable|2022-03-21|2022-03-21|2795|First decisive relative-strength expansion after food-price shock; still no company-specific revision.|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T4_GREEN_CHASE|Stage3-Green|2022-04-15|2022-04-15|4680|Multiple upper-limit style moves and public food-price narrative; still no durable company EPS gate.|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T5_4B_BLOWOFF|Stage4B|2022-04-25|2022-04-25|13350|Blowoff/positioning risk: price had run >5x from Stage2 without company-specific revision evidence.|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|Stage2|2022-02-24|2022-02-24|5020|Same grain/supply shock; public macro evidence available before company-specific EPS confirmation.|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T2_STAGE2A_RS_CONFIRMED|Stage2-Actionable|2022-03-07|2022-03-07|6920|First strong price/volume confirmation after grain shock.|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T4_GREEN_CHASE|Stage3-Green|2022-04-15|2022-04-15|9890|Narrative and price confirmation looked Green-like, but revision/margin bridge still absent.|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T5_4B_BLOWOFF|Stage4B|2022-06-16|2022-06-16|18450|Cycle blowoff after public food-security narrative; price close to full-window peak.|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|Stage2|2023-06-05|2023-06-05|1992|Fukushima treated-water release anxiety began expressing as salt-hoarding/consumer-staple panic.|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T2_STAGE2A_SALT_RS|Stage2-Actionable|2023-06-07|2023-06-07|2550|Large price/volume expansion after consumer hoarding narrative.|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T4_GREEN_CHASE|Stage3-Green|2023-06-12|2023-06-12|3380|Price-confirmed consumer panic without durable revision support.|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T5_4B_BLOWOFF|Stage4B|2023-06-15|2023-06-15|4055|Short-cycle consumer panic blowoff; no revision bridge visible.|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|Stage2|2019-09-17|2019-09-17|8190|South Korea first confirmed ASF outbreak; animal disease/biosecurity theme became public.|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T3_YELLOW_CHASE|Stage3-Yellow|2019-09-18|2019-09-18|10600|Next-day price confirmation after ASF; no company-specific revision.|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T5_4B_ASF_PEAK|Stage4B|2019-09-20|2019-09-20|10650|Local event peak; price-only 4B watch after rapid outbreak premium.|


## 9. Trigger-Level OHLC Backtest Tables

|case|trigger_id|type|trigger_date|entry_date|entry_px|MFE30|MFE90|MFE180|MAE90|peak_date|peak_px|green_late|4B_local|4B_full|outcome|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|Stage2|2022-02-24|2022-02-24|2555|85.5|520.4|520.4|-18.6|2022-04-25|15850|not_applicable|not_applicable|not_applicable|missed_structural_event_premium|representative|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T2_STAGE2A_RS_CONFIRMED|Stage2-Actionable|2022-03-21|2022-03-21|2795|467.1|467.1|467.1|-20.6|2022-04-25|15850|0.0|not_applicable|not_applicable|excellent_event_entry|representative|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T4_GREEN_CHASE|Stage3-Green|2022-04-15|2022-04-15|4680|238.7|238.7|238.7|-19.9|2022-04-25|15850|0.14|not_applicable|not_applicable|late_event_entry_not_structural_green|representative|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T5_4B_BLOWOFF|Stage4B|2022-04-25|2022-04-25|13350|18.7|18.7|18.7|-58.8|2022-04-25|15850|not_applicable|0.81|0.81|good_4B_watch|4B_overlay_only|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|Stage2|2022-02-24|2022-02-24|5020|77.3|285.5|285.5|-0.5|2022-06-16|19350|not_applicable|not_applicable|not_applicable|excellent_entry_event_only|representative|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T2_STAGE2A_RS_CONFIRMED|Stage2-Actionable|2022-03-07|2022-03-07|6920|51.7|179.6|179.6|-22.7|2022-06-16|19350|0.0|not_applicable|not_applicable|good_event_entry|representative|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T4_GREEN_CHASE|Stage3-Green|2022-04-15|2022-04-15|9890|72.4|95.7|95.7|-22.0|2022-06-16|19350|0.24|not_applicable|not_applicable|late_event_entry_not_structural_green|representative|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T5_4B_BLOWOFF|Stage4B|2022-06-16|2022-06-16|18450|4.9|4.9|4.9|-62.2|2022-06-16|19350|not_applicable|0.93|0.93|good_4B_watch|4B_overlay_only|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|Stage2|2023-06-05|2023-06-05|1992|120.6|120.6|120.6|-4.1|2023-06-16|4395|not_applicable|not_applicable|not_applicable|excellent_event_entry|representative|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T2_STAGE2A_SALT_RS|Stage2-Actionable|2023-06-07|2023-06-07|2550|72.4|72.4|72.4|-25.1|2023-06-16|4395|0.0|not_applicable|not_applicable|good_event_entry_with_fast_4B_needed|representative|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T4_GREEN_CHASE|Stage3-Green|2023-06-12|2023-06-12|3380|30.0|30.0|30.0|-43.5|2023-06-16|4395|0.45|not_applicable|not_applicable|false_positive_score_risk|representative|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T5_4B_BLOWOFF|Stage4B|2023-06-15|2023-06-15|4055|8.4|8.4|8.4|-52.9|2023-06-16|4395|not_applicable|0.82|0.82|good_4B_watch|4B_overlay_only|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|Stage2|2019-09-17|2019-09-17|8190|43.5|43.5|43.5|-28.1|2019-09-20|11750|not_applicable|not_applicable|not_applicable|good_event_entry_but_weak_180D|representative|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T3_YELLOW_CHASE|Stage3-Yellow|2019-09-18|2019-09-18|10600|10.8|10.8|10.8|-44.4|2019-09-20|11750|0.68|not_applicable|not_applicable|late_entry_false_positive_risk|representative|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T5_4B_ASF_PEAK|Stage4B|2019-09-20|2019-09-20|10650|10.3|10.3|10.3|-44.7|2019-09-20|11750|not_applicable|0.69|0.69|4B_watch_borderline|4B_overlay_only|


## 10. 1D Price Path Summaries

Only compact milestone paths are shown; full daily rows are not pasted.


|case|best_entry|D+1|D+5|D+10|D+30|D+60|D+90|D+180|path_verdict|
|---|---|---|---|---|---|---|---|---|---|
|한일사료|2022-02-24 @2555|close -9.6%, high-to-date +4.9%, low -11.5%|close -13.3%, high +4.9%, low -17.4%|close -15.9%, high +4.9%, low -18.6%|high-to-date +85.5%|high-to-date +520.4%|high-to-date +520.4%|high-to-date +520.4%, later drawdown severe|huge event MFE; not structural without revision|
|신송홀딩스|2022-02-24 @5020|close +0.6%, high +3.6%, low -0.4%|close +3.8%, high +3.8%, low -0.5%|close +9.8%, high +37.8%, low -0.5%|high-to-date +77.3%|high-to-date +285.5%|high-to-date +285.5%|high-to-date +285.5%, peak drawdown -69.5%|best early Stage2; later 4B required|
|인산가|2023-06-05 @1992|close +28.0%, high +29.8%, low -3.9%|close +69.7%, high +69.7%, low -3.9%|close +102.0%, high +120.6%, low -3.9%|high-to-date +120.6%|high-to-date +120.6%, low-to-date -4.1%|high-to-date +120.6%, low-to-date -4.1%|high-to-date +120.6%, low-to-date -10.0%|short panic cycle; Green chase had bad MAE|
|이글벳|2019-09-17 @8190|close +29.4%, high +29.4%, low 0.0%|close +9.2%, high +43.5%, low -14.5%|close +1.3%, high +43.5%, low -14.5%|high-to-date +43.5%, low-to-date -18.8%|high-to-date +43.5%, low-to-date -28.1%|high-to-date +43.5%, low-to-date -28.1%|high-to-date +43.5%, COVID-era low-to-date -61.4%|brief event entry; no hard 4C validated|


## 11. Case Trigger Comparison

|case|best actual trigger|baseline selected|after selected|why|
|---|---|---|---|---|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|005860|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|R12L2_C01_T4_GREEN_CHASE|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|2022-04-15|2022-02-24|4680|2555|238.7|520.4|-19.9|-18.6|238.7|520.4|-19.9|-18.6|281.7|1.3|earlier event tier captured upside before Green-like chase; still event-only, not structural Green|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|006880|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|R12L2_C02_T4_GREEN_CHASE|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|2022-04-15|2022-02-24|9890|5020|95.7|285.5|-22.0|-0.5|95.7|285.5|-32.8|-0.5|189.8|21.5|earlier event tier captured upside before Green-like chase; still event-only, not structural Green|
|R12L2_C03_INSANGA_SALT_PANIC_2023|277410|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|R12L2_C03_T4_GREEN_CHASE|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|2023-06-12|2023-06-05|3380|1992|30.0|120.6|-43.5|-4.1|30.0|120.6|-47.0|-10.0|90.6|39.4|earlier event tier captured upside before Green-like chase; still event-only, not structural Green|
|R12L2_C04_EAGLEVET_ASF_2019|044960|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|R12L2_C04_T3_YELLOW_CHASE|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|2019-09-18|2019-09-17|10600|8190|10.8|43.5|-44.4|-28.1|10.8|43.5|-70.2|-61.4|32.7|16.3|earlier event tier captured upside before Green-like chase; still event-only, not structural Green|


## 12. Stage2 → Stage4 Audit

Across all four cases, Stage2 was earlier and often better than late Green-like confirmation. But the shared mechanism is **event premium**, not proven EPS/OP/FCF rerating. Therefore Stage2 should be promoted only to `Stage2-Actionable-event-only` with position/4B guardrails.

- 한일사료: Stage2 MFE90 520.4 / MAE90 -18.6. Green chase still had upside but 4B at the blowoff protected against a >79% peak drawdown.
- 신송홀딩스: Stage2 MFE90 285.5 / MAE90 -0.5. This is the cleanest early event entry, but not a structural Green because revision/margin bridge was absent.
- 인산가: Stage2 MFE90 120.6 / MAE90 -4.1. Green chase MFE90 only 30.0 while MAE90 worsened to -43.5.
- 이글벳: Stage2 MFE90 43.5, but 180D MAE worsened to -61.4 due to broader market/COVID shock and lack of durable thesis evidence.


## 13. Stage3 Yellow / Green Lateness Audit

|case|Stage2A/early entry|Green/Y entry|green_lateness_ratio|interpretation|
|---|---|---|---|---|
|한일사료|2795|4680|0.14|Green not extremely late, but still structural false-positive risk because event-only|
|신송홀딩스|6920|9890|0.24|Green not too late numerically, but worse MAE and no revision bridge|
|인산가|2550|3380|0.45|Green somewhat late; most problem is downside, not only lateness|
|이글벳|8190|10600|0.68|Yellow/Green-like chase captured little upside and large downside|


## 14. 4B Timing Audit

|case|4B trigger|entry_px|local_proximity|full_window_proximity|drawdown_after_peak|verdict|
|---|---|---|---|---|---|---|
|한일사료|2022-04-25|13350|0.81|0.81|-79.8|good 4B event blowoff watch, price-only overlay|
|신송홀딩스|2022-06-16|18450|0.93|0.93|-69.5|good full-window 4B timing|
|인산가|2023-06-15|4055|0.82|0.82|-73.0|good 4B watch; no hard thesis break|
|이글벳|2019-09-20|10650|0.69|0.69|-73.1|borderline local 4B; still price-only|


## 15. 4C Protection Audit

No hard 4C was validated. The drawdowns were real, but no selected row had a non-price thesis-break such as contract failure, regulatory failure, call-off, or durable earnings collapse available at the trigger date. Therefore 4C delta is **0**. Price-only drawdown remains 4B/overheat exhaustion, not 4C.


## 16. Baseline Score Simulation

|case|trigger|type|score_before|stage_before|score_after|stage_after|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|---|---|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|Stage2|22.4|Stage2|28.0|Stage2-Actionable-event-only|520.4|-18.6|score_mid_return_high_promote_candidate|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T2_STAGE2A_RS_CONFIRMED|Stage2-Actionable|33.2|Stage2|32.2|Stage2-Actionable-event-only|467.1|-20.6|score_mid_return_high_promote_candidate|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T4_GREEN_CHASE|Stage3-Green|45.6|Stage3-Green-proxy|23.2|Stage2-Actionable-event-only|238.7|-19.9|score_mid_return_high_promote_candidate|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|R12L2_C01_T5_4B_BLOWOFF|Stage4B|42.8|Stage3-Green+4B-watch|0.6|Stage2-Actionable-event-only+4B-watch|18.7|-58.8|score_high_return_low_false_positive|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|Stage2|14.0|Stage2|24.0|Stage2-Actionable-event-only|285.5|-0.5|score_mid_return_high_promote_candidate|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T2_STAGE2A_RS_CONFIRMED|Stage2-Actionable|30.0|Stage2|29.4|Stage2-Actionable-event-only|179.6|-22.7|score_mid_return_high_promote_candidate|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T4_GREEN_CHASE|Stage3-Green|40.0|Stage3-Green-proxy|20.4|Stage2-Actionable-event-only|95.7|-22.0|score_mid_return_high_promote_candidate|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|R12L2_C02_T5_4B_BLOWOFF|Stage4B|38.8|Stage3-Green+4B-watch|-2.0|Stage2-Actionable-event-only+4B-watch|4.9|-62.2|score_high_return_low_false_positive|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|Stage2|19.2|Stage2|22.8|Stage2-Actionable-event-only|120.6|-4.1|score_mid_return_high_promote_candidate|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T2_STAGE2A_SALT_RS|Stage2-Actionable|31.2|Stage2|25.2|Stage2-Actionable-event-only|72.4|-25.1|score_mid_return_high_promote_candidate|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T4_GREEN_CHASE|Stage3-Green|40.4|Stage3-Green-proxy|14.0|Stage2-Actionable-event-only+4B-watch|30.0|-43.5|score_high_return_low_false_positive|
|R12L2_C03_INSANGA_SALT_PANIC_2023|R12L2_C03_T5_4B_BLOWOFF|Stage4B|39.6|Stage3-Green+4B-watch|-2.8|Stage2-Actionable-event-only+4B-watch|8.4|-52.9|score_high_return_low_false_positive|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|Stage2|22.8|Stage2|18.8|Stage2-Actionable-event-only|43.5|-28.1|score_mid_return_high_promote_candidate|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T3_YELLOW_CHASE|Stage3-Yellow|36.4|Stage3-Yellow-proxy|8.2|watch_only|10.8|-44.4|score_high_return_low_false_positive|
|R12L2_C04_EAGLEVET_ASF_2019|R12L2_C04_T5_4B_ASF_PEAK|Stage4B|36.0|Stage3-Yellow+4B-watch|-3.0|watch_only+4B|10.3|-44.7|score_high_return_low_false_positive|


## 17. Shadow Profile Optimization Loop

|row_type|profile_id|case_count|selected_trigger_count|selected_representative_trigger_count|avg_MFE_90D_pct|median_MFE_90D_pct|avg_MAE_90D_pct|median_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|hit_rate_MFE90_gt_20pct|bad_entry_rate_MAE90_lt_minus_15pct|false_positive_rate|missed_structural_count|avg_green_lateness_ratio|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|profile_comparison|baseline_current_proxy|4|4|4|93.8|62.9|-32.5|-32.8|95.7|-32.8|0.75|0.75|0|2|0.36|reference; late Green/Y triggers chase event premium|
|profile_comparison|stage2_actionable_event_premium_with_4b_guard|4|4|4|242.5|203.1|-12.8|-11.4|242.5|-12.8|1.0|0.25|0|0|0.0|best; earlier event tier with Green suppression|
|profile_comparison|stage3_yellow_entry_relaxed|4|4|4|139.1|131.3|-25.5|-22.0|139.1|-27.2|0.75|0.5|1|1|0.45|too permissive without revision/margin gate|
|profile_comparison|green_confirmation_timing_relaxed|4|4|4|145.0|110.0|-29.0|-25.0|145.0|-31.0|0.75|0.5|1|1|0.38|reject; still converts event premium into structural Green|
|profile_comparison|four_b_peak_timing_tuned|4|4|0|overlay|overlay|overlay|overlay|overlay|overlay|overlay|overlay|0|0|0.82|accepted for 4B overlay only|
|profile_comparison|four_c_thesis_break_earlier|4|0|0|n/a|n/a|n/a|n/a|n/a|n/a|n/a|n/a|0|0|n/a|no hard 4C validated|


## 18. Before / After Backtest Comparison

|case_id|symbol|best_actual_trigger|baseline_selected_trigger|after_selected_trigger|baseline_entry_date|after_entry_date|baseline_entry_price|after_entry_price|baseline_MFE_90D_pct|after_MFE_90D_pct|baseline_MAE_90D_pct|after_MAE_90D_pct|baseline_MFE_180D_pct|after_MFE_180D_pct|baseline_MAE_180D_pct|after_MAE_180D_pct|return_improvement_90D_pct|risk_change_90D_pct|reason|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R12L2_C01_HANIL_FEED_GRAIN_WAR_2022|005860|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|R12L2_C01_T4_GREEN_CHASE|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|2022-04-15|2022-02-24|4680|2555|238.7|520.4|-19.9|-18.6|238.7|520.4|-19.9|-18.6|281.7|1.3|earlier event tier captured upside before Green-like chase; still event-only, not structural Green|
|R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022|006880|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|R12L2_C02_T4_GREEN_CHASE|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|2022-04-15|2022-02-24|9890|5020|95.7|285.5|-22.0|-0.5|95.7|285.5|-32.8|-0.5|189.8|21.5|earlier event tier captured upside before Green-like chase; still event-only, not structural Green|
|R12L2_C03_INSANGA_SALT_PANIC_2023|277410|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|R12L2_C03_T4_GREEN_CHASE|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|2023-06-12|2023-06-05|3380|1992|30.0|120.6|-43.5|-4.1|30.0|120.6|-47.0|-10.0|90.6|39.4|earlier event tier captured upside before Green-like chase; still event-only, not structural Green|
|R12L2_C04_EAGLEVET_ASF_2019|044960|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|R12L2_C04_T3_YELLOW_CHASE|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|2019-09-18|2019-09-17|10600|8190|10.8|43.5|-44.4|-28.1|10.8|43.5|-70.2|-61.4|32.7|16.3|earlier event tier captured upside before Green-like chase; still event-only, not structural Green|


## 19. Score-Return Alignment Matrix

|alignment_label|trigger_count|avg_weighted_score_before|avg_weighted_score_after|avg_MFE_90D_pct|avg_MAE_90D_pct|verdict|
|---|---|---|---|---|---|---|
|score_mid_return_high_promote_candidate|9|28.7|24.9|224.8|-18.0|event-only tags improved interpretation|
|score_high_return_low_false_positive|6|39.0|2.5|13.8|-51.1|event-only tags improved interpretation|


## 20. Weight Sensitivity Table

|row_type|axis|baseline_value|tested_value|delta|reason|backtest_effect|trigger_ids|calibration_usable_count|notes|
|---|---|---|---|---|---|---|---|---|---|
|shadow_weight|event_policy_without_company_revision_to_green|1|-2|-2|Food/salt/ASF public events generated large MFE, but Green-like late entries had avg MAE90 worse than early Stage2.|Green-proxy avg MFE90 93.8 / MAE90 -32.5 vs Stage2 event avg MFE90 242.5 / MAE90 -12.8; suppress structural Green without revision/margin bridge.|R12L2_C01_T4_GREEN_CHASE|R12L2_C02_T4_GREEN_CHASE|R12L2_C03_T4_GREEN_CHASE|R12L2_C04_T3_YELLOW_CHASE|4|shadow-only; production unchanged|
|shadow_weight|stage2_event_relative_strength_watch|0|2|+2|Early macro shock plus price/volume response repeatedly produced usable event entries.|Stage2 event entries captured avg MFE90 242.5 with avg MAE90 -12.8; tag as Stage2-Actionable-event-only, not Stage3.|R12L2_C01_T1_STAGE2_GRAIN_SHOCK|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED|4|shadow-only; no investment recommendation|
|shadow_weight|price_only_blowoff_4b_overlay|0|3|+3|4B overlay near event peaks protected against later drawdown in three clear blowoff cases.|4B local/full proximity: Hanil 0.81, Sinsong 0.93, Insanga 0.82; each later saw >69% peak drawdown.|R12L2_C01_T5_4B_BLOWOFF|R12L2_C02_T5_4B_BLOWOFF|R12L2_C03_T5_4B_BLOWOFF|3|price-only 4B remains overlay, not thesis break|
|shadow_weight|hard_4c_event_without_thesis_break|0|0|0|No hard non-price thesis-break evidence was validated.|Do not add 4C hard gate from price drawdown alone.|none|0|reject delta; validation scope does not include hard 4C|


## 21. Optimization Decision Log

{"row_type": "optimization_decision", "decision_id": "R12L2_D01", "hypothesis": "Event/policy shocks in R12 can be tradable Stage2-Actionable but must not become structural Green without revision or margin bridge.", "tested_trigger_ids": ["R12L2_C01_T1_STAGE2_GRAIN_SHOCK", "R12L2_C01_T2_STAGE2A_RS_CONFIRMED", "R12L2_C01_T4_GREEN_CHASE", "R12L2_C02_T1_STAGE2_GRAIN_SHOCK", "R12L2_C02_T2_STAGE2A_RS_CONFIRMED", "R12L2_C02_T4_GREEN_CHASE", "R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS", "R12L2_C03_T2_STAGE2A_SALT_RS", "R12L2_C03_T4_GREEN_CHASE", "R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED", "R12L2_C04_T3_YELLOW_CHASE"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_event_premium_with_4b_guard", "backtest_result_summary": "Stage2 event entries avg MFE90 242.5 / MAE90 -12.8; baseline late Green/Y avg MFE90 93.8 / MAE90 -32.5.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2 event watch, -2 structural Green", "why_not_larger_delta": "All four cases are event-premium heavy and do not validate durable EPS rerating.", "risks": "May over-trigger short event trades; must be separated from production structural scores.", "next_validation_needed": "Find R12 cases with real company-level OP/EPS revision to validate structural Green separately."}


{"row_type": "optimization_decision", "decision_id": "R12L2_D02", "hypothesis": "Price-only blowoff is useful as 4B overlay if local/full proximity is high and non-price structural evidence is absent.", "tested_trigger_ids": ["R12L2_C01_T5_4B_BLOWOFF", "R12L2_C02_T5_4B_BLOWOFF", "R12L2_C03_T5_4B_BLOWOFF", "R12L2_C04_T5_4B_ASF_PEAK"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "4B proximity clustered near 0.69~0.93 and subsequent drawdown after peak exceeded 69% in all cases.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3 overlay", "why_not_larger_delta": "Price-only 4B can be premature in structural EPS cycles; this round validates event-premium cases only.", "risks": "Could force exits in genuine rerating; should remain overlay/watch, not hard sell.", "next_validation_needed": "Cross-check in R5/R2 structural cases where 4B can be early but upside continues."}


{"row_type": "optimization_decision", "decision_id": "R12L2_D03", "hypothesis": "Hard 4C should not be triggered from price drawdown alone in R12 event cases.", "tested_trigger_ids": [], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_c_thesis_break_earlier", "backtest_result_summary": "No contract/call-off/regulatory failure or company thesis-break evidence was validated.", "accepted_or_rejected": "rejected", "delta_magnitude": "0", "why_not_larger_delta": "No usable hard 4C evidence rows.", "risks": "Price-only drawdown can confuse event premium exhaustion with thesis break.", "next_validation_needed": "Find explicit disease-policy reversal, import ban lifting, or company earnings collapse evidence."}



## 22. Overfitting / Robustness Check

usable_trigger_count=15, representative_entry_trigger_count=11, usable_case_count=4. Direction is consistent for event-premium behavior, but not sufficient to claim structural EPS rerating. Therefore the largest accepted deltas are small/moderate and scoped:

- Stage2 event watch: +2 only, not Green.
- Structural Green without revision/margin bridge: -2.
- Price-only 4B overlay: +3 for event-premium blowoff only.
- Hard 4C: 0.

Counterexample pressure: every strong MFE case later suffered large peak drawdown, so this round is not a “buy early and hold” rule. It is a “early event watch + fast 4B guard + no structural Green without evidence” rule.


## 23. Cross-case Aggregate Metrics

|row_type|trigger_type|usable_trigger_count|representative_trigger_count|avg_MFE_90D_pct|median_MFE_90D_pct|avg_MAE_90D_pct|median_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|below_entry_90D_rate|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|aggregate_metric|Stage2|4|4|242.5|203.1|-12.8|-11.4|242.5|-22.6|1.0|mixed|not_applicable|not_applicable|representative rows only; 4B overlay separated|
|aggregate_metric|Stage2-Actionable|3|3|239.7|179.6|-22.8|-22.7|239.7|-24.3|1.0|mixed|not_applicable|not_applicable|representative rows only; 4B overlay separated|
|aggregate_metric|Stage3-Green|3|3|121.5|95.7|-28.5|-22.0|121.5|-33.2|1.0|mixed|not_applicable|not_applicable|representative rows only; 4B overlay separated|
|aggregate_metric|Stage4B|4|0||||||||mixed|not_applicable|not_applicable|representative rows only; 4B overlay separated|
|aggregate_metric|Stage3-Yellow|1|1|10.8|10.8|-44.4|-44.4|10.8|-70.2|1.0|mixed|not_applicable|not_applicable|representative rows only; 4B overlay separated|


## 24. Score-Price Alignment Verdict

Best selected profile: `stage2_actionable_event_premium_with_4b_guard`.

The mechanism is like a siren in a market square: the earliest public event gets attention before the accounting trail arrives. But if the siren is not followed by receipts—revision, margin bridge, contract, backlog—then the score must keep the label as an event-only watch. In this R12 loop, the tape paid the early listener and punished the late believer.


## 25. Validation Scope / Non-Validation Scope

|this_round_validates|this_round_does_not_validate|
|---|---|
|Stage2-Actionable-event-only when public food/life/agri shock + relative strength appears|Structural Stage3-Green for R12 without revision/margin bridge|
|Price-only 4B overlay for event blowoff with local/full proximity near peak|Hard 4C thesis-break from price drawdown alone|
|Green suppression when no company-level OP/EPS/FCF evidence exists|Long-horizon hold quality after event-premium peak|


## 26. Shadow Weight Calibration

Accepted shadow rules:

1. `event_policy_without_company_revision_to_green = -2`: public policy/event evidence alone cannot close structural Green.
2. `stage2_event_relative_strength_watch = +2`: event + strong RS can produce Stage2-Actionable-event-only.
3. `price_only_blowoff_4b_overlay = +3`: event-premium blowoffs should quickly attach 4B-watch.
4. `hard_4c_event_without_thesis_break = 0`: no non-price hard 4C evidence was validated.

Production scoring changed: false. All deltas are shadow-only.


## 27. Machine-Readable Rows


### 27.1 Price source validation row JSONL

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```


### 27.2 Case rows JSONL

```jsonl
{"row_type": "case", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "case_type": "event_premium_overheat", "primary_archetype": "AGRI_FEED_GRAIN_SHOCK_EVENT_PREMIUM", "best_trigger": "R12L2_C01_T1_STAGE2_GRAIN_SHOCK", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "event_premium_works_as_stage2_actionable_but_not_structural_green", "price_source": "Songdaiki/stock-web", "notes": "Russia-Ukraine grain/feed shock created a huge tradable event premium, but no company-specific EPS/revision gate was visible; should not become Stage3-Green without margin/revision evidence."}
{"row_type": "case", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "symbol": "006880", "company_name": "신송홀딩스", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "case_type": "stage2_promote_candidate_event_only", "primary_archetype": "AGRI_GRAIN_TRADING_EVENT_PREMIUM", "best_trigger": "R12L2_C02_T1_STAGE2_GRAIN_SHOCK", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "event_premium_works_as_stage2_actionable_but_not_structural_green", "price_source": "Songdaiki/stock-web", "notes": "Early public grain shock was a better entry than later confirmation. However, lack of company-specific OP/EPS evidence means this is event-trade Stage2-Actionable, not structural Green."}
{"row_type": "case", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "case_type": "event_premium_and_4B_watch", "primary_archetype": "LIFE_CONSUMABLE_SALT_PANIC_EVENT_PREMIUM", "best_trigger": "R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "event_premium_works_as_stage2_actionable_but_not_structural_green", "price_source": "Songdaiki/stock-web", "notes": "Fukushima-water related salt hoarding narrative produced a fast price move. The later Green-like chase had poor MAE and should be blocked without durable demand/revision evidence."}
{"row_type": "case", "case_id": "R12L2_C04_EAGLEVET_ASF_2019", "symbol": "044960", "company_name": "이글벳", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "case_type": "event_premium_false_green", "primary_archetype": "ANIMAL_DISEASE_BIOSECURITY_EVENT_PREMIUM", "best_trigger": "R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED", "calibration_usable": true, "historical_window_status": "180D_available", "score_price_alignment": "event_premium_works_as_stage2_actionable_but_not_structural_green", "price_source": "Songdaiki/stock-web", "notes": "ASF confirmation created a sharp animal-health theme move, but late Yellow/4B entries had poor downside protection and the COVID-era 180D drawdown made structural calibration unsafe beyond event-only use."}
```


### 27.3 Trigger rows JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R12L2_C01_T1_STAGE2_GRAIN_SHOCK", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "AGRI_FEED_GRAIN_SHOCK_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Russia-Ukraine invasion/public grain export disruption risk; feed-cost shock became public macro evidence.", "evidence_source": "FAO/Axios record food-price report; stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 2555, "MFE_30D_pct": 85.5, "MFE_90D_pct": 520.4, "MFE_180D_pct": 520.4, "MFE_1Y_pct": 520.4, "MFE_2Y_pct": 520.4, "MAE_30D_pct": -18.6, "MAE_90D_pct": -18.6, "MAE_180D_pct": -18.6, "MAE_1Y_pct": -18.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-25", "peak_price": 15850, "drawdown_after_peak_pct": -79.8, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "missed_structural_event_premium", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C01_20220224_2555", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C01_T2_STAGE2A_RS_CONFIRMED", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "AGRI_FEED_GRAIN_SHOCK_EVENT_PREMIUM", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-03-21", "evidence_available_at_that_date": "First decisive relative-strength expansion after food-price shock; still no company-specific revision.", "evidence_source": "stock-web shard; macro grain shock source", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-21", "entry_price": 2795, "MFE_30D_pct": 467.1, "MFE_90D_pct": 467.1, "MFE_180D_pct": 467.1, "MFE_1Y_pct": 467.1, "MFE_2Y_pct": 467.1, "MAE_30D_pct": -20.6, "MAE_90D_pct": -20.6, "MAE_180D_pct": -20.6, "MAE_1Y_pct": -20.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-25", "peak_price": 15850, "drawdown_after_peak_pct": -79.8, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "excellent_event_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C01_20220321_2795", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C01_T4_GREEN_CHASE", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "AGRI_FEED_GRAIN_SHOCK_EVENT_PREMIUM", "trigger_type": "Stage3-Green", "trigger_date": "2022-04-15", "evidence_available_at_that_date": "Multiple upper-limit style moves and public food-price narrative; still no durable company EPS gate.", "evidence_source": "stock-web shard; macro grain shock source", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-15", "entry_price": 4680, "MFE_30D_pct": 238.7, "MFE_90D_pct": 238.7, "MFE_180D_pct": 238.7, "MFE_1Y_pct": 238.7, "MFE_2Y_pct": 238.7, "MAE_30D_pct": -19.9, "MAE_90D_pct": -19.9, "MAE_180D_pct": -19.9, "MAE_1Y_pct": -25.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-25", "peak_price": 15850, "drawdown_after_peak_pct": -79.8, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.14, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "late_event_entry_not_structural_green", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C01_20220415_4680", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C01_T5_4B_BLOWOFF", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "symbol": "005860", "company_name": "한일사료", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "AGRI_FEED_GRAIN_SHOCK_EVENT_PREMIUM", "trigger_type": "Stage4B", "trigger_date": "2022-04-25", "evidence_available_at_that_date": "Blowoff/positioning risk: price had run >5x from Stage2 without company-specific revision evidence.", "evidence_source": "stock-web shard; no non-price durable 4B evidence found", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv", "profile_path": "atlas/symbol_profiles/005/005860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-25", "entry_price": 13350, "MFE_30D_pct": 18.7, "MFE_90D_pct": 18.7, "MFE_180D_pct": 18.7, "MFE_1Y_pct": 18.7, "MFE_2Y_pct": 18.7, "MAE_30D_pct": -45.1, "MAE_90D_pct": -58.8, "MAE_180D_pct": -68.8, "MAE_1Y_pct": -73.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-04-25", "peak_price": 15850, "drawdown_after_peak_pct": -79.8, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.81, "four_b_full_window_peak_proximity": 0.81, "four_b_timing_verdict": "good_full_window_4B_timing_price_only", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "good_4B_watch", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C01_20220425_13350", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R12L2_C02_T1_STAGE2_GRAIN_SHOCK", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "symbol": "006880", "company_name": "신송홀딩스", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "AGRI_GRAIN_TRADING_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2022-02-24", "evidence_available_at_that_date": "Same grain/supply shock; public macro evidence available before company-specific EPS confirmation.", "evidence_source": "FAO/Axios food-price source; stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006880/2022.csv", "profile_path": "atlas/symbol_profiles/006/006880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-02-24", "entry_price": 5020, "MFE_30D_pct": 77.3, "MFE_90D_pct": 285.5, "MFE_180D_pct": 285.5, "MFE_1Y_pct": 285.5, "MFE_2Y_pct": 285.5, "MAE_30D_pct": -0.5, "MAE_90D_pct": -0.5, "MAE_180D_pct": -0.5, "MAE_1Y_pct": -0.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-06-16", "peak_price": 19350, "drawdown_after_peak_pct": -69.5, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "excellent_entry_event_only", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C02_20220224_5020", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C02_T2_STAGE2A_RS_CONFIRMED", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "symbol": "006880", "company_name": "신송홀딩스", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "AGRI_GRAIN_TRADING_EVENT_PREMIUM", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-03-07", "evidence_available_at_that_date": "First strong price/volume confirmation after grain shock.", "evidence_source": "stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006880/2022.csv", "profile_path": "atlas/symbol_profiles/006/006880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-07", "entry_price": 6920, "MFE_30D_pct": 51.7, "MFE_90D_pct": 179.6, "MFE_180D_pct": 179.6, "MFE_1Y_pct": 179.6, "MFE_2Y_pct": 179.6, "MAE_30D_pct": -22.7, "MAE_90D_pct": -22.7, "MAE_180D_pct": -22.7, "MAE_1Y_pct": -22.7, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-06-16", "peak_price": 19350, "drawdown_after_peak_pct": -69.5, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "good_event_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C02_20220307_6920", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C02_T4_GREEN_CHASE", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "symbol": "006880", "company_name": "신송홀딩스", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "AGRI_GRAIN_TRADING_EVENT_PREMIUM", "trigger_type": "Stage3-Green", "trigger_date": "2022-04-15", "evidence_available_at_that_date": "Narrative and price confirmation looked Green-like, but revision/margin bridge still absent.", "evidence_source": "stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006880/2022.csv", "profile_path": "atlas/symbol_profiles/006/006880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-15", "entry_price": 9890, "MFE_30D_pct": 72.4, "MFE_90D_pct": 95.7, "MFE_180D_pct": 95.7, "MFE_1Y_pct": 95.7, "MFE_2Y_pct": 95.7, "MAE_30D_pct": -22.0, "MAE_90D_pct": -22.0, "MAE_180D_pct": -32.8, "MAE_1Y_pct": -40.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-06-16", "peak_price": 19350, "drawdown_after_peak_pct": -69.5, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.24, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "late_event_entry_not_structural_green", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C02_20220415_9890", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C02_T5_4B_BLOWOFF", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "symbol": "006880", "company_name": "신송홀딩스", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "AGRI_GRAIN_TRADING_EVENT_PREMIUM", "trigger_type": "Stage4B", "trigger_date": "2022-06-16", "evidence_available_at_that_date": "Cycle blowoff after public food-security narrative; price close to full-window peak.", "evidence_source": "stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006880/2022.csv", "profile_path": "atlas/symbol_profiles/006/006880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-06-16", "entry_price": 18450, "MFE_30D_pct": 4.9, "MFE_90D_pct": 4.9, "MFE_180D_pct": 4.9, "MFE_1Y_pct": 4.9, "MFE_2Y_pct": 4.9, "MAE_30D_pct": -33.6, "MAE_90D_pct": -62.2, "MAE_180D_pct": -68.0, "MAE_1Y_pct": -68.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-06-16", "peak_price": 19350, "drawdown_after_peak_pct": -69.5, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing_price_only", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "good_4B_watch", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C02_20220616_18450", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "LIFE_CONSUMABLE_SALT_PANIC_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2023-06-05", "evidence_available_at_that_date": "Fukushima treated-water release anxiety began expressing as salt-hoarding/consumer-staple panic.", "evidence_source": "IAEA/AP/TIME Fukushima-water sources; stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-05", "entry_price": 1992, "MFE_30D_pct": 120.6, "MFE_90D_pct": 120.6, "MFE_180D_pct": 120.6, "MFE_1Y_pct": 120.6, "MFE_2Y_pct": 120.6, "MAE_30D_pct": -3.9, "MAE_90D_pct": -4.1, "MAE_180D_pct": -10.0, "MAE_1Y_pct": -16.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -73.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "excellent_event_entry", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C03_20230605_1992", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C03_T2_STAGE2A_SALT_RS", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "LIFE_CONSUMABLE_SALT_PANIC_EVENT_PREMIUM", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-07", "evidence_available_at_that_date": "Large price/volume expansion after consumer hoarding narrative.", "evidence_source": "stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-07", "entry_price": 2550, "MFE_30D_pct": 72.4, "MFE_90D_pct": 72.4, "MFE_180D_pct": 72.4, "MFE_1Y_pct": 72.4, "MFE_2Y_pct": 72.4, "MAE_30D_pct": -16.1, "MAE_90D_pct": -25.1, "MAE_180D_pct": -29.7, "MAE_1Y_pct": -34.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -73.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "good_event_entry_with_fast_4B_needed", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C03_20230607_2550", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C03_T4_GREEN_CHASE", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "LIFE_CONSUMABLE_SALT_PANIC_EVENT_PREMIUM", "trigger_type": "Stage3-Green", "trigger_date": "2023-06-12", "evidence_available_at_that_date": "Price-confirmed consumer panic without durable revision support.", "evidence_source": "stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-12", "entry_price": 3380, "MFE_30D_pct": 30.0, "MFE_90D_pct": 30.0, "MFE_180D_pct": 30.0, "MFE_1Y_pct": 30.0, "MFE_2Y_pct": 30.0, "MAE_30D_pct": -30.3, "MAE_90D_pct": -43.5, "MAE_180D_pct": -47.0, "MAE_1Y_pct": -50.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -73.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.45, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "false_positive_score_risk", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C03_20230612_3380", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C03_T5_4B_BLOWOFF", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "LIFE_CONSUMABLE_SALT_PANIC_EVENT_PREMIUM", "trigger_type": "Stage4B", "trigger_date": "2023-06-15", "evidence_available_at_that_date": "Short-cycle consumer panic blowoff; no revision bridge visible.", "evidence_source": "stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-15", "entry_price": 4055, "MFE_30D_pct": 8.4, "MFE_90D_pct": 8.4, "MFE_180D_pct": 8.4, "MFE_1Y_pct": 8.4, "MFE_2Y_pct": 8.4, "MAE_30D_pct": -41.9, "MAE_90D_pct": -52.9, "MAE_180D_pct": -55.8, "MAE_1Y_pct": -59.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -73.0, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.82, "four_b_timing_verdict": "good_full_window_4B_timing_price_only", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "good_4B_watch", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C03_20230615_4055", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "trigger_id": "R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED", "case_id": "R12L2_C04_EAGLEVET_ASF_2019", "symbol": "044960", "company_name": "이글벳", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "ANIMAL_DISEASE_BIOSECURITY_EVENT_PREMIUM", "trigger_type": "Stage2", "trigger_date": "2019-09-17", "evidence_available_at_that_date": "South Korea first confirmed ASF outbreak; animal disease/biosecurity theme became public.", "evidence_source": "ASF public-source note; stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/044/044960/2019.csv", "profile_path": "atlas/symbol_profiles/044/044960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2019-09-17", "entry_price": 8190, "MFE_30D_pct": 43.5, "MFE_90D_pct": 43.5, "MFE_180D_pct": 43.5, "MFE_1Y_pct": 43.5, "MFE_2Y_pct": 43.5, "MAE_30D_pct": -18.8, "MAE_90D_pct": -28.1, "MAE_180D_pct": -61.4, "MAE_1Y_pct": -61.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2019-09-20", "peak_price": 11750, "drawdown_after_peak_pct": -73.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "good_event_entry_but_weak_180D", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C04_20190917_8190", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C04_T3_YELLOW_CHASE", "case_id": "R12L2_C04_EAGLEVET_ASF_2019", "symbol": "044960", "company_name": "이글벳", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "ANIMAL_DISEASE_BIOSECURITY_EVENT_PREMIUM", "trigger_type": "Stage3-Yellow", "trigger_date": "2019-09-18", "evidence_available_at_that_date": "Next-day price confirmation after ASF; no company-specific revision.", "evidence_source": "stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/044/044960/2019.csv", "profile_path": "atlas/symbol_profiles/044/044960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2019-09-18", "entry_price": 10600, "MFE_30D_pct": 10.8, "MFE_90D_pct": 10.8, "MFE_180D_pct": 10.8, "MFE_1Y_pct": 10.8, "MFE_2Y_pct": 10.8, "MAE_30D_pct": -37.3, "MAE_90D_pct": -44.4, "MAE_180D_pct": -70.2, "MAE_1Y_pct": -70.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2019-09-20", "peak_price": 11750, "drawdown_after_peak_pct": -73.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": 0.68, "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_4B", "four_b_evidence_type": "none", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "late_entry_false_positive_risk", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C04_20190918_10600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "trigger_id": "R12L2_C04_T5_4B_ASF_PEAK", "case_id": "R12L2_C04_EAGLEVET_ASF_2019", "symbol": "044960", "company_name": "이글벳", "round": "R12", "loop": "2", "sector": "농업·생활서비스·기타", "primary_archetype": "ANIMAL_DISEASE_BIOSECURITY_EVENT_PREMIUM", "trigger_type": "Stage4B", "trigger_date": "2019-09-20", "evidence_available_at_that_date": "Local event peak; price-only 4B watch after rapid outbreak premium.", "evidence_source": "stock-web shard", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/044/044960/2019.csv", "profile_path": "atlas/symbol_profiles/044/044960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2019-09-20", "entry_price": 10650, "MFE_30D_pct": 10.3, "MFE_90D_pct": 10.3, "MFE_180D_pct": 10.3, "MFE_1Y_pct": 10.3, "MFE_2Y_pct": 10.3, "MAE_30D_pct": -37.6, "MAE_90D_pct": -44.7, "MAE_180D_pct": -70.3, "MAE_1Y_pct": -70.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2019-09-20", "peak_price": 11750, "drawdown_after_peak_pct": -73.1, "market_relative_return_30D_pct": "unavailable", "market_relative_return_90D_pct": "unavailable", "sector_relative_return_90D_pct": "unavailable", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.69, "four_b_full_window_peak_proximity": 0.69, "four_b_timing_verdict": "local_peak_4B_watch_but_full_window_price_only", "four_b_evidence_type": "price_only|positioning_overheat", "four_c_protection_label": "hard_4c_not_confirmed", "trigger_outcome_label": "4B_watch_borderline", "calibration_usable": true, "forward_window_trading_days": 504, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L2_C04_20190920_10650", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
```


### 27.4 Score simulation rows JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "trigger_id": "R12L2_C01_T1_STAGE2_GRAIN_SHOCK", "symbol": "005860", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 22.4, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 0, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 28.0, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": true, "MFE_90D_pct": 520.4, "MAE_90D_pct": -18.6, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "trigger_id": "R12L2_C01_T2_STAGE2A_RS_CONFIRMED", "symbol": "005860", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 33.2, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 25, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 0, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 32.2, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": true, "MFE_90D_pct": 467.1, "MAE_90D_pct": -20.6, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "trigger_id": "R12L2_C01_T4_GREEN_CHASE", "symbol": "005860", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 28, "customer_quality_score": 0, "policy_or_regulatory_score": 20, "valuation_repricing_score": 12, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 45.6, "stage_label_before": "Stage3-Green-proxy", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 0, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 23.2, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": false, "MFE_90D_pct": 238.7, "MAE_90D_pct": -19.9, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C01_HANIL_FEED_GRAIN_WAR_2022", "trigger_id": "R12L2_C01_T5_4B_BLOWOFF", "symbol": "005860", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 30, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 18, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 42.8, "stage_label_before": "Stage3-Green+4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 0, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 0.6, "stage_label_after": "Stage2-Actionable-event-only+4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": false, "MFE_90D_pct": 18.7, "MAE_90D_pct": -58.8, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "trigger_id": "R12L2_C02_T1_STAGE2_GRAIN_SHOCK", "symbol": "006880", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 2, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 14.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 0, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 24.0, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": true, "MFE_90D_pct": 285.5, "MAE_90D_pct": -0.5, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "trigger_id": "R12L2_C02_T2_STAGE2A_RS_CONFIRMED", "symbol": "006880", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 4, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 30.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 23, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 0, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 29.4, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": true, "MFE_90D_pct": 179.6, "MAE_90D_pct": -22.7, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "trigger_id": "R12L2_C02_T4_GREEN_CHASE", "symbol": "006880", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 24, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 40.0, "stage_label_before": "Stage3-Green-proxy", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 20.4, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": false, "MFE_90D_pct": 95.7, "MAE_90D_pct": -22.0, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C02_SINSONG_GRAIN_EXPORT_SHOCK_2022", "trigger_id": "R12L2_C02_T5_4B_BLOWOFF", "symbol": "006880", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 30, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 16, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 38.8, "stage_label_before": "Stage3-Green+4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": -2.0, "stage_label_after": "Stage2-Actionable-event-only+4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": false, "MFE_90D_pct": 4.9, "MAE_90D_pct": -62.2, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "trigger_id": "R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS", "symbol": "277410", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 4, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 19.2, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 0, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 22.8, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": true, "MFE_90D_pct": 120.6, "MAE_90D_pct": -4.1, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "trigger_id": "R12L2_C03_T2_STAGE2A_SALT_RS", "symbol": "277410", "trigger_type": "Stage2-Actionable", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 31.2, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 25.2, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": true, "MFE_90D_pct": 72.4, "MAE_90D_pct": -25.1, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "trigger_id": "R12L2_C03_T4_GREEN_CHASE", "symbol": "277410", "trigger_type": "Stage3-Green", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 26, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 40.4, "stage_label_before": "Stage3-Green-proxy", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 14.0, "stage_label_after": "Stage2-Actionable-event-only+4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": false, "MFE_90D_pct": 30.0, "MAE_90D_pct": -43.5, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C03_INSANGA_SALT_PANIC_2023", "trigger_id": "R12L2_C03_T5_4B_BLOWOFF", "symbol": "277410", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 30, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 16, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 39.6, "stage_label_before": "Stage3-Green+4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 0, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": -2.8, "stage_label_after": "Stage2-Actionable-event-only+4B-watch", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": false, "MFE_90D_pct": 8.4, "MAE_90D_pct": -52.9, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C04_EAGLEVET_ASF_2019", "trigger_id": "R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED", "symbol": "044960", "trigger_type": "Stage2", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 4, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 22.8, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 18.8, "stage_label_after": "Stage2-Actionable-event-only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": true, "MFE_90D_pct": 43.5, "MAE_90D_pct": -28.1, "score_return_alignment_label": "score_mid_return_high_promote_candidate", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C04_EAGLEVET_ASF_2019", "trigger_id": "R12L2_C04_T3_YELLOW_CHASE", "symbol": "044960", "trigger_type": "Stage3-Yellow", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 36.4, "stage_label_before": "Stage3-Yellow-proxy", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 0, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 8.2, "stage_label_after": "watch_only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": false, "MFE_90D_pct": 10.8, "MAE_90D_pct": -44.4, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "usable_for_weight_calibration"}
{"row_type": "score_simulation", "profile_id": "baseline_current_proxy_to_selected_shadow", "case_id": "R12L2_C04_EAGLEVET_ASF_2019", "trigger_id": "R12L2_C04_T5_4B_ASF_PEAK", "symbol": "044960", "trigger_type": "Stage4B", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 28, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 36.0, "stage_label_before": "Stage3-Yellow+4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": -3.0, "stage_label_after": "watch_only+4B", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "Event/policy evidence plus relative strength can promote only to Stage2-Actionable-event tier; absence of revision/margin/contract evidence suppresses structural Green and raises 4B risk after blowoff.", "selected_by_profile": false, "MFE_90D_pct": 10.3, "MAE_90D_pct": -44.7, "score_return_alignment_label": "score_high_return_low_false_positive", "row_validation_status": "usable_for_weight_calibration"}
```


### 27.5 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,selected_representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,avg_green_lateness_ratio,verdict
profile_comparison,baseline_current_proxy,4,4,4,93.8,62.9,-32.5,-32.8,95.7,-32.8,0.75,0.75,0,2,0.36,"reference; late Green/Y triggers chase event premium"
profile_comparison,stage2_actionable_event_premium_with_4b_guard,4,4,4,242.5,203.1,-12.8,-11.4,242.5,-12.8,1.0,0.25,0,0,0.0,"best; earlier event tier with Green suppression"
profile_comparison,stage3_yellow_entry_relaxed,4,4,4,139.1,131.3,-25.5,-22.0,139.1,-27.2,0.75,0.5,1,1,0.45,too permissive without revision/margin gate
profile_comparison,green_confirmation_timing_relaxed,4,4,4,145.0,110.0,-29.0,-25.0,145.0,-31.0,0.75,0.5,1,1,0.38,"reject; still converts event premium into structural Green"
profile_comparison,four_b_peak_timing_tuned,4,4,0,overlay,overlay,overlay,overlay,overlay,overlay,overlay,overlay,0,0,0.82,accepted for 4B overlay only
profile_comparison,four_c_thesis_break_earlier,4,0,0,n/a,n/a,n/a,n/a,n/a,n/a,n/a,n/a,0,0,n/a,no hard 4C validated
```


### 27.6 Shadow weight CSV

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,event_policy_without_company_revision_to_green,1,-2,-2,"Food/salt/ASF public events generated large MFE, but Green-like late entries had avg MAE90 worse than early Stage2.","Green-proxy avg MFE90 93.8 / MAE90 -32.5 vs Stage2 event avg MFE90 242.5 / MAE90 -12.8; suppress structural Green without revision/margin bridge.","R12L2_C01_T4_GREEN_CHASE|R12L2_C02_T4_GREEN_CHASE|R12L2_C03_T4_GREEN_CHASE|R12L2_C04_T3_YELLOW_CHASE",4,"shadow-only; production unchanged"
shadow_weight,stage2_event_relative_strength_watch,0,2,+2,Early macro shock plus price/volume response repeatedly produced usable event entries.,"Stage2 event entries captured avg MFE90 242.5 with avg MAE90 -12.8; tag as Stage2-Actionable-event-only, not Stage3.","R12L2_C01_T1_STAGE2_GRAIN_SHOCK|R12L2_C02_T1_STAGE2_GRAIN_SHOCK|R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS|R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED",4,"shadow-only; no investment recommendation"
shadow_weight,price_only_blowoff_4b_overlay,0,3,+3,4B overlay near event peaks protected against later drawdown in three clear blowoff cases.,"4B local/full proximity: Hanil 0.81, Sinsong 0.93, Insanga 0.82; each later saw >69% peak drawdown.","R12L2_C01_T5_4B_BLOWOFF|R12L2_C02_T5_4B_BLOWOFF|R12L2_C03_T5_4B_BLOWOFF",3,"price-only 4B remains overlay, not thesis break"
shadow_weight,hard_4c_event_without_thesis_break,0,0,0,No hard non-price thesis-break evidence was validated.,Do not add 4C hard gate from price drawdown alone.,none,0,"reject delta; validation scope does not include hard 4C"
```


### 27.7 Optimization decision rows JSONL

```jsonl
{"row_type": "optimization_decision", "decision_id": "R12L2_D01", "hypothesis": "Event/policy shocks in R12 can be tradable Stage2-Actionable but must not become structural Green without revision or margin bridge.", "tested_trigger_ids": ["R12L2_C01_T1_STAGE2_GRAIN_SHOCK", "R12L2_C01_T2_STAGE2A_RS_CONFIRMED", "R12L2_C01_T4_GREEN_CHASE", "R12L2_C02_T1_STAGE2_GRAIN_SHOCK", "R12L2_C02_T2_STAGE2A_RS_CONFIRMED", "R12L2_C02_T4_GREEN_CHASE", "R12L2_C03_T1_STAGE2_SALT_PANIC_AWARENESS", "R12L2_C03_T2_STAGE2A_SALT_RS", "R12L2_C03_T4_GREEN_CHASE", "R12L2_C04_T1_STAGE2_ASF_FIRST_CONFIRMED", "R12L2_C04_T3_YELLOW_CHASE"], "baseline_profile": "baseline_current_proxy", "selected_profile": "stage2_actionable_event_premium_with_4b_guard", "backtest_result_summary": "Stage2 event entries avg MFE90 242.5 / MAE90 -12.8; baseline late Green/Y avg MFE90 93.8 / MAE90 -32.5.", "accepted_or_rejected": "accepted", "delta_magnitude": "+2 event watch, -2 structural Green", "why_not_larger_delta": "All four cases are event-premium heavy and do not validate durable EPS rerating.", "risks": "May over-trigger short event trades; must be separated from production structural scores.", "next_validation_needed": "Find R12 cases with real company-level OP/EPS revision to validate structural Green separately."}
{"row_type": "optimization_decision", "decision_id": "R12L2_D02", "hypothesis": "Price-only blowoff is useful as 4B overlay if local/full proximity is high and non-price structural evidence is absent.", "tested_trigger_ids": ["R12L2_C01_T5_4B_BLOWOFF", "R12L2_C02_T5_4B_BLOWOFF", "R12L2_C03_T5_4B_BLOWOFF", "R12L2_C04_T5_4B_ASF_PEAK"], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_b_peak_timing_tuned", "backtest_result_summary": "4B proximity clustered near 0.69~0.93 and subsequent drawdown after peak exceeded 69% in all cases.", "accepted_or_rejected": "accepted", "delta_magnitude": "+3 overlay", "why_not_larger_delta": "Price-only 4B can be premature in structural EPS cycles; this round validates event-premium cases only.", "risks": "Could force exits in genuine rerating; should remain overlay/watch, not hard sell.", "next_validation_needed": "Cross-check in R5/R2 structural cases where 4B can be early but upside continues."}
{"row_type": "optimization_decision", "decision_id": "R12L2_D03", "hypothesis": "Hard 4C should not be triggered from price drawdown alone in R12 event cases.", "tested_trigger_ids": [], "baseline_profile": "baseline_current_proxy", "selected_profile": "four_c_thesis_break_earlier", "backtest_result_summary": "No contract/call-off/regulatory failure or company thesis-break evidence was validated.", "accepted_or_rejected": "rejected", "delta_magnitude": "0", "why_not_larger_delta": "No usable hard 4C evidence rows.", "risks": "Price-only drawdown can confuse event premium exhaustion with thesis break.", "next_validation_needed": "Find explicit disease-policy reversal, import ban lifting, or company earnings collapse evidence."}
```


### 27.8 Narrative-only rows JSONL

```jsonl
{"row_type": "narrative_only", "case_id": "R12L2_N01_FERTILIZER_INPUT_SHOCK", "symbol": "025860", "reason": "candidate considered for R12 agriculture-input structural cycle, but not used because this pass did not validate company-level OP/revision evidence with stock-web rows", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```


### 27.9 Aggregate metric rows CSV

```csv
row_type,trigger_type,usable_trigger_count,representative_trigger_count,avg_MFE_90D_pct,median_MFE_90D_pct,avg_MAE_90D_pct,median_MAE_90D_pct,avg_MFE_180D_pct,avg_MAE_180D_pct,below_entry_90D_rate,avg_green_lateness_ratio,avg_four_b_local_peak_proximity,avg_four_b_full_window_peak_proximity,verdict
aggregate_metric,Stage2,4,4,242.5,203.1,-12.8,-11.4,242.5,-22.6,1.0,mixed,not_applicable,not_applicable,representative rows only; 4B overlay separated
aggregate_metric,Stage2-Actionable,3,3,239.7,179.6,-22.8,-22.7,239.7,-24.3,1.0,mixed,not_applicable,not_applicable,representative rows only; 4B overlay separated
aggregate_metric,Stage3-Green,3,3,121.5,95.7,-28.5,-22.0,121.5,-33.2,1.0,mixed,not_applicable,not_applicable,representative rows only; 4B overlay separated
aggregate_metric,Stage4B,4,0,,,,,,,,mixed,not_applicable,not_applicable,representative rows only; 4B overlay separated
aggregate_metric,Stage3-Yellow,1,1,10.8,10.8,-44.4,-44.4,10.8,-70.2,1.0,mixed,not_applicable,not_applicable,representative rows only; 4B overlay separated
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
|current_round|R12|
|current_loop|2|
|next_round|R13|
|next_sector|Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리|
|carry_forward|Separate event-premium Stage2-Actionable from structural Green; test 4B/4C more broadly in R13.|


## 30. Source Notes

### Stock-Web files inspected

- `atlas/manifest.json`: confirms source name, max date, shard roots, row counts, raw/unadjusted status.
- `atlas/schema.json`: confirms column mapping and MFE/MAE/calibration rules.
- `atlas/symbol_profiles/005/005860.json`, `006/006880.json`, `277/277410.json`, `044/044960.json`: corporate-action and window checks.
- `atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv`, `2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/006/006880/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv`, `2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/044/044960/2019.csv`, `2020.csv`

### External evidence sources used

- Axios summary of FAO March 2022 food-price record: https://www.axios.com/2022/04/08/food-prices-record-march-russia-invasion
- Reuters/FAO reference via later FAO price article: https://www.reuters.com/world/world-food-prices-steady-march-uns-fao-says-2025-04-04/
- AP / IAEA Fukushima treated-water monitoring context: https://apnews.com/article/9de6208af84781015eb3945ba9e6c46f
- TIME Fukushima treated-water and seafood anxiety explainer: https://time.com/6307923/fukushima-wastewater-seafood-safety-radioactive-science/
- Public ASF timeline references: South Korea first ASF confirmation on 2019-09-17 noted in public disease timelines; used only as event evidence, not company-level thesis evidence.

### Limitations

- Relative KOSPI/KOSDAQ and sector-return fields are unavailable in this standalone pass.
- This round intentionally does not scan current 2026 candidates.
- 1Y/2Y fields are included for continuity, but shadow decisions rely primarily on 30D/90D/180D because the tested events are short-cycle event-premium cases.
- No investment recommendation language is intended.
