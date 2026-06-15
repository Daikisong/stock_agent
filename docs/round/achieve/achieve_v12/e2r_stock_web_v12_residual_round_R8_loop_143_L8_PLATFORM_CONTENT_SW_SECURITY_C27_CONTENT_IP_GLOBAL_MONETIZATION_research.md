# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 143
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: CONTENT_IP_REPEAT_CASH_BRIDGE_HOLDOUT_V143_WEBTOON_FILM_KIDS_GAME_ARTIST_SLATE_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 036570/2024: cache_miss_observed_this_turn
    - 112040/2024: cache_miss_observed_this_turn
    - 078340/2024: cache_miss_observed_this_turn
    - 194480/2024: cache_miss_observed_this_turn
    - 263720/2024: reused_from_prior_local_C27_loop_142
    - 086980/2024: reused_from_prior_local_C27_loop_142
    - 419530/2024: reused_from_prior_local_C27_loop_142
    - 259960/2024: reused_from_prior_local_C27_source_proxy_loop_107
    - 263750/2024: reused_from_prior_local_C27_source_proxy_loop_107
    - 293490/2024: reused_from_prior_local_C27_source_proxy_loop_107
    - 035900/2024: reused_from_prior_local_C27_source_proxy_loop_107
    - 253450/2024: reused_from_prior_local_C27_source_proxy_loop_107
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - content_IP_hit_to_repeat_cash_bridge_gate
  - source_proxy_reverification_required
  - webtoon_anime_game_option_stack_4B_guard
  - one_off_film_hit_cap_guard
  - kids_character_IP_merchandise_licensing_4B_guard
  - game_launch_expectation_hard_4B_4C_split
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C27_CONTENT_IP_GLOBAL_MONETIZATION` remains Priority 0 in the no-repeat index. The v12 scheduler maps C26~C28 to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`.

This file continues the local C27 sequence after `R8/C27 loop 142`; selected loop is therefore `143`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence. Direct raw stock-web shard attempts for new C27 game/content candidates returned cache miss in this execution, so the file reuses prior C27 rows as holdout and reclassification evidence. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C27 should not reward `content`, `IP`, `global fandom`, `game launch`, `drama slate`, `webtoon`, or `box-office hit` as labels.

C27 should reward monetization that repeats and reaches the listed company:

```text
content IP / webtoon / film / game / artist / drama / character franchise
→ distribution or release
→ paid consumption, box office, licensing, royalty, merchandise, live-service or catalog revenue
→ repeatable slate / sequel / franchise / library monetization
→ margin and cash conversion
→ price path validation
```

The recurring false positive is:

```text
one-off hit
artist comeback cycle
game launch hope
drama slate label
global fandom noise
IP recognition without listed-company take-rate
control-premium or tender event misfiled as content value
```

C27 is the library archetype. A hit is a spark; a monetizable IP library is a furnace. The score should rise when the spark lights recurring cash: royalties, licensing, merchandise, sequel economics, live-service revenue, subscriptions, fan-platform commerce or box-office profit-share that can repeat.

The C27 route split in this holdout:

```text
direct box-office or paid distribution cash bridge
→ Stage2 can survive, but one-off hit cap remains

webtoon / anime / game option stack with high MFE and high MAE
→ local 4B until listed-company royalty/licensing cash bridge refresh

kids character IP / merchandise ecosystem
→ Stage2 can open, but deep MAE forces 4B until margin mix refresh

global game IP / live-service monetization
→ Stage2 can survive after direct reprice and revenue/cash proof

game launch expectation without retention
→ local 4B

artist cycle / drama slate / game portfolio label without cash bridge
→ hard 4C

control battle / tender mechanics
→ reclassify to C32, not C27
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 8
  source_proxy_only_rows: 5
  reused_stock_web_rows: 8
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C27_CONTENT_IP_GLOBAL_MONETIZATION
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C27 holdout validation
    - repeat-cash IP monetization gate
    - one-off hit cap guard
    - source-proxy reprice TODO
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R8/C27 loop 107
  - R8/C27 loop 142
  - R12/C32 governance/control-premium contamination rows
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - directly requested new C27 candidate shards cache-missed in this execution
  - all non-proxy reused rows already contain complete 30D/90D/180D MFE and MAE
  - source_proxy_only rows retain required fields but must be directly repriced before aggregate use
  - this file is holdout validation only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"SOLO_LEVELING_WEBTOON_ANIME_GAME_OPTION_STACK_HIGH_MFE_HIGH_MAE_4B","symbol":"263720","name":"디앤씨미디어","trigger_type":"Stage4B","entry_date":"2024-01-08","entry_price":29850,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.31,"MAE_30D_pct":-19.26,"MFE_90D_pct":29.31,"MAE_90D_pct":-26.30,"MFE_180D_pct":29.31,"MAE_180D_pct":-27.81,"forward_high_30d":38600,"forward_low_30d":24100,"forward_high_90d":38600,"forward_low_90d":22000,"forward_high_180d":38600,"forward_low_180d":21550,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C27|263720|Stage4B|2024-01-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_webtoon_4B","reuse_reason":"same D&C Media Solo Leveling webtoon/anime/game option-stack row from C27 loop 142","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"webtoon_anime_game_option_stack_4B","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|263720|Stage4B|2024-01-08","non_price_bridge":"Solo Leveling webtoon/IP expansion into anime and broader cross-media option stack","score_alignment":"local 4B; high MAE blocks Green until royalty/licensing/game/drama cash bridge refresh"}
{"row_type":"trigger","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"EXHUMA_BOX_OFFICE_CASH_BRIDGE_ONE_OFF_HIT_WITH_LIBRARY_CAP","symbol":"086980","name":"쇼박스","trigger_type":"Stage2-Actionable","entry_date":"2024-02-22","entry_price":3670,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.84,"MAE_30D_pct":-0.41,"MFE_90D_pct":23.84,"MAE_90D_pct":-6.40,"MFE_180D_pct":23.84,"MAE_180D_pct":-6.40,"forward_high_30d":4545,"forward_low_30d":3655,"forward_high_90d":4545,"forward_low_90d":3435,"forward_high_180d":4545,"forward_low_180d":3435,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C27|086980|Stage2-Actionable|2024-02-22","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_oneoff_positive","reuse_reason":"same Showbox Exhuma box-office row from C27 loop 142","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"box_office_cash_bridge_positive_with_cap","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|086980|Stage2-Actionable|2024-02-22","non_price_bridge":"Exhuma box-office success distributed by Showbox with direct theatrical cash bridge","score_alignment":"keep Stage2-Actionable; cap Stage3-Green unless slate/library repeat monetization is confirmed"}
{"row_type":"trigger","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"TEENIEPING_KIDS_CHARACTER_IP_MERCH_FILM_THEME_PARK_LONG_TAIL_MONETIZATION_4B","symbol":"419530","name":"SAMG엔터","trigger_type":"Stage4B","entry_date":"2024-09-09","entry_price":15610,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.75,"MAE_30D_pct":-7.75,"MFE_90D_pct":25.75,"MAE_90D_pct":-24.22,"MFE_180D_pct":91.22,"MAE_180D_pct":-30.75,"forward_high_30d":19630,"forward_low_30d":14400,"forward_high_90d":19630,"forward_low_90d":11830,"forward_high_180d":29850,"forward_low_180d":10810,"corporate_action_window_status":"not_flagged_in_prior_local_validation","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C27|419530|Stage4B|2024-09-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_character_IP_4B","reuse_reason":"same SAMG Teenieping kids-character IP row from C27 loop 142","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"kids_character_IP_long_tail_4B","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|419530|Stage4B|2024-09-09","non_price_bridge":"Catch! Teenieping / Heartsping kids character IP monetization across broadcast, film, merchandise, parks and overseas licensing","score_alignment":"local 4B; deep drawdown requires merchandise/licensing/margin refresh before Green"}
{"row_type":"trigger","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GLOBAL_GAME_IP_LIVE_SERVICE_MONETIZATION_POSITIVE_CONTROL_SOURCE_PROXY","symbol":"259960","name":"크래프톤","trigger_type":"Stage2-Actionable","entry_date":"2024-02-13","entry_price":212500,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.35,"MAE_30D_pct":-4.00,"MFE_90D_pct":38.59,"MAE_90D_pct":-4.00,"MFE_180D_pct":46.35,"MAE_180D_pct":-4.00,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|259960|Stage2-Actionable|2024-02-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control_source_proxy","reuse_reason":"same Krafton global game IP live-service row from C27 loop 107; direct reprice required","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"global_game_IP_live_service_positive_proxy","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|259960|Stage2-Actionable|2024-02-13","non_price_bridge":"global game IP and live-service monetization candidate with margin/cash durability","score_alignment":"Stage2 proxy only; Green blocked until live-service revenue, margin and settlement cash proof"}
{"row_type":"trigger","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_LAUNCH_EXPECTATION_HIGH_MAE_LOCAL_4B_SOURCE_PROXY","symbol":"263750","name":"펄어비스","trigger_type":"Stage4B","entry_date":"2024-06-03","entry_price":42100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.38,"MAE_30D_pct":-8.67,"MFE_90D_pct":29.45,"MAE_90D_pct":-23.16,"MFE_180D_pct":29.45,"MAE_180D_pct":-35.39,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|263750|Stage4B|2024-06-03","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_game_launch_4B_source_proxy","reuse_reason":"same Pearl Abyss game-launch expectation row from C27 loop 107; direct reprice required","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"game_launch_expectation_local_4B","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|263750|Stage4B|2024-06-03","non_price_bridge":"game launch expectation and IP optionality without confirmed launch revenue, live-service retention or cash bridge","score_alignment":"local 4B/source-proxy; block Green until launch monetization and retention proof"}
{"row_type":"trigger","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_PORTFOLIO_LABEL_WITHOUT_NEW_IP_RETENTION_HARD_4C_SOURCE_PROXY","symbol":"293490","name":"카카오게임즈","trigger_type":"Stage4C","entry_date":"2024-03-29","entry_price":25000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.20,"MAE_30D_pct":-15.60,"MFE_90D_pct":3.20,"MAE_90D_pct":-31.20,"MFE_180D_pct":3.20,"MAE_180D_pct":-42.00,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|293490|Stage4C|2024-03-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_game_label_hard_4C_source_proxy","reuse_reason":"same Kakao Games portfolio-label hard 4C row from C27 loop 107; direct reprice required","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"game_portfolio_label_hard_4C","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|293490|Stage4C|2024-03-29","non_price_bridge":"game portfolio label without new IP retention, global monetization or margin bridge","score_alignment":"hard 4C/source-proxy; game label failed IP monetization gate"}
{"row_type":"trigger","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"ARTIST_CYCLE_IP_LABEL_WITHOUT_MARGIN_FOLLOWTHROUGH_HARD_4C_SOURCE_PROXY","symbol":"035900","name":"JYP Ent.","trigger_type":"Stage4C","entry_date":"2024-01-29","entry_price":95100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.21,"MAE_30D_pct":-18.82,"MFE_90D_pct":2.21,"MAE_90D_pct":-34.91,"MFE_180D_pct":2.21,"MAE_180D_pct":-44.27,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|035900|Stage4C|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_artist_cycle_hard_4C_source_proxy","reuse_reason":"same JYP artist-cycle hard 4C row from C27 loop 107; direct reprice required","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"artist_cycle_hard_4C","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|035900|Stage4C|2024-01-29","non_price_bridge":"artist comeback/cycle label without durable global IP margin, catalog compounding or cash bridge","score_alignment":"hard 4C/source-proxy; artist-cycle label failed monetization durability test"}
{"row_type":"trigger","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"DRAMA_SLATE_PLATFORM_DISTRIBUTION_LABEL_NO_MARGIN_CASH_HARD_4C_SOURCE_PROXY","symbol":"253450","name":"스튜디오드래곤","trigger_type":"Stage4C","entry_date":"2024-02-15","entry_price":48900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.91,"MAE_30D_pct":-13.09,"MFE_90D_pct":4.91,"MAE_90D_pct":-27.61,"MFE_180D_pct":4.91,"MAE_180D_pct":-38.04,"corporate_action_window_status":"batch_reverification_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C27|253450|Stage4C|2024-02-15","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_drama_slate_hard_4C_source_proxy","reuse_reason":"same Studio Dragon drama-slate hard 4C row from C27 loop 107; direct reprice required","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"drama_slate_platform_distribution_hard_4C","novelty_key":"C27_CONTENT_IP_GLOBAL_MONETIZATION|253450|Stage4C|2024-02-15","non_price_bridge":"drama slate/platform distribution label without retained margin, second-window monetization or cash bridge","score_alignment":"hard 4C/source-proxy; content slate label failed global IP monetization gate"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R8","selected_loop":143,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_NEW_GAME_CONTENT_IP_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["036570","112040","078340","194480","095660","225570","181710","207760","950170"],"candidate_names":["엔씨소프트","위메이드","컴투스","데브시스터즈","네오위즈","넥슨게임즈","NHN","미스터블루","JTC-content_tourism_noise_check"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards for new game/content IP candidates cache-missed or were unavailable in this execution; no fresh independent 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C27 evidence; distinguish repeat IP cashflow from one-off launch, content hit, C26 platform ARPU, C28 software retention, and C32 tender/governance mechanics"}
```

---

## 6. Case analysis

### 6.1 Webtoon/anime/game option stack — D&C Media / 263720

```yaml
entry_price: 29850
90D_MFE_MAE: +29.31 / -26.30
180D_MFE_MAE: +29.31 / -27.81
route: local 4B
```

The IP recognition was real, but the drawdown says the market did not have enough listed-company cash capture evidence. C27 should keep the row local 4B until royalty, licensing, game/drama option and margin bridge are refreshed.

### 6.2 One-off film hit — Showbox / 086980

```yaml
entry_price: 3670
90D_MFE_MAE: +23.84 / -6.40
180D_MFE_MAE: +23.84 / -6.40
route: Stage2-Actionable with one-off cap
```

This is the cleanest non-proxy row in this holdout. The hit had direct theatrical cash logic and shallow drawdown. Still, one film should not unlock Green without a repeatable slate/library bridge.

### 6.3 Kids character IP — SAMG Entertainment / 419530

```yaml
entry_price: 15610
90D_MFE_MAE: +25.75 / -24.22
180D_MFE_MAE: +91.22 / -30.75
route: local 4B
```

The long-tail IP engine is plausible: broadcast, film, toys, merchandise, parks, licensing. But deep drawdown demands revenue mix and margin proof before promotion.

### 6.4 Game IP and launch rows

```yaml
259960:
  role: global game IP live-service positive proxy
  90D_MFE_MAE: +38.59 / -4.00
  route: Stage2 proxy, reprice required

263750:
  role: game launch expectation
  90D_MFE_MAE: +29.45 / -23.16
  route: local 4B

293490:
  role: game portfolio label
  90D_MFE_MAE: +3.20 / -31.20
  route: hard 4C
```

Game IP works when live-service revenue, user retention, ARPPU/DAU, and settlement cash are visible. Launch hope without post-launch monetization is a 4B at best, and a generic portfolio label is 4C.

### 6.5 Artist cycle and drama slate hard blocks

```yaml
035900:
  90D_MFE_MAE: +2.21 / -34.91
  route: hard 4C

253450:
  90D_MFE_MAE: +4.91 / -27.61
  route: hard 4C
```

Artist comeback and drama slate labels failed the repeat-cash gate. C27 needs catalog/touring/platform or retained margin evidence, not only a content calendar.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 8
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 5
batch_reverification_required_count: 5
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 6
local_4B_watch_count: 4
hard_4C_count: 3
wrong_archetype_reclassification_count: 0
current_profile_error_count: 6
diversity_score_summary: "webtoon option-stack 4B, box-office positive with one-off cap, kids character IP 4B, global game IP positive proxy, game launch 4B, game portfolio 4C, artist cycle 4C and drama slate 4C covered"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C27 lesson |
|---|---:|---:|---:|---|
| 263720 | webtoon option stack 4B | +29.31 / -26.30 | +29.31 / -27.81 | IP recognition needs cash bridge |
| 086980 | film hit positive cap | +23.84 / -6.40 | +23.84 / -6.40 | one-off hit cap |
| 419530 | kids IP 4B | +25.75 / -24.22 | +91.22 / -30.75 | long-tail IP needs margin refresh |
| 259960 | game IP proxy | +38.59 / -4.00 | +46.35 / -4.00 | live-service bridge can work |
| 263750 | launch hope 4B | +29.45 / -23.16 | +29.45 / -35.39 | launch expectation needs retention |
| 293490 | game label 4C | +3.20 / -31.20 | +3.20 / -42.00 | portfolio label failed |
| 035900 | artist cycle 4C | +2.21 / -34.91 | +2.21 / -44.27 | comeback label failed |
| 253450 | drama slate 4C | +4.91 / -27.61 | +4.91 / -38.04 | retained margin absent |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"263720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_quality":4,"global_distribution":3,"repeat_monetization":2,"margin_bridge":1,"cash_conversion":1,"relative_strength":4,"event_quality":3,"execution_risk":5,"accounting_trust_risk":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"IP_quality":4,"global_distribution":3,"repeat_monetization":1,"margin_bridge":0,"cash_conversion":0,"relative_strength":2,"event_quality":2,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":54,"stage_label_after":"Stage4B","changed_components":["repeat_monetization","margin_bridge","cash_conversion","relative_strength","event_quality","accounting_trust_risk"],"component_delta_explanation":"Webtoon/anime option stack had MFE but no refreshed listed-company cash bridge and high MAE.","MFE_90D_pct":29.31,"MAE_90D_pct":-26.30,"score_return_alignment_label":"webtoon_IP_option_stack_4B","current_profile_verdict":"current_profile_too_generous_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"086980","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_quality":3,"global_distribution":2,"repeat_monetization":2,"margin_bridge":3,"cash_conversion":3,"relative_strength":3,"event_quality":4,"execution_risk":2,"accounting_trust_risk":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"IP_quality":3,"global_distribution":2,"repeat_monetization":1,"margin_bridge":3,"cash_conversion":3,"relative_strength":3,"event_quality":4,"execution_risk":2,"accounting_trust_risk":2},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable_one_off_cap","changed_components":["repeat_monetization"],"component_delta_explanation":"Box-office cash bridge validated, but one-off film hit needs slate/library repeat proof before Green.","MFE_90D_pct":23.84,"MAE_90D_pct":-6.40,"score_return_alignment_label":"direct_box_office_positive_cap","current_profile_verdict":"current_profile_correct_if_one_off_cap_applied"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"419530","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_quality":4,"global_distribution":3,"repeat_monetization":3,"margin_bridge":2,"cash_conversion":1,"relative_strength":5,"event_quality":3,"execution_risk":5,"accounting_trust_risk":4},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"IP_quality":4,"global_distribution":3,"repeat_monetization":2,"margin_bridge":1,"cash_conversion":0,"relative_strength":3,"event_quality":3,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":59,"stage_label_after":"Stage4B_character_IP_refresh","changed_components":["repeat_monetization","margin_bridge","cash_conversion","relative_strength","accounting_trust_risk"],"component_delta_explanation":"Kids character IP can become a licensing/merchandising flywheel, but deep drawdown requires margin and cash refresh.","MFE_90D_pct":25.75,"MAE_90D_pct":-24.22,"score_return_alignment_label":"kids_character_IP_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"259960","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_quality":5,"global_distribution":4,"repeat_monetization":4,"margin_bridge":4,"cash_conversion":3,"relative_strength":4,"event_quality":3,"execution_risk":2,"accounting_trust_risk":2},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"IP_quality":5,"global_distribution":4,"repeat_monetization":4,"margin_bridge":4,"cash_conversion":3,"relative_strength":4,"event_quality":3,"execution_risk":2,"accounting_trust_risk":2},"weighted_score_after":80,"stage_label_after":"Stage2_proxy_reverify_required","changed_components":[],"component_delta_explanation":"Global game IP and live-service economics are a valid C27 bridge, but direct stock-web and revenue/cash evidence require reverify.","MFE_90D_pct":38.59,"MAE_90D_pct":-4.00,"source_proxy_only":true,"score_return_alignment_label":"game_IP_live_service_positive_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"263750","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_quality":3,"global_distribution":2,"repeat_monetization":2,"margin_bridge":1,"cash_conversion":0,"relative_strength":4,"event_quality":3,"execution_risk":5,"accounting_trust_risk":4},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"IP_quality":3,"global_distribution":2,"repeat_monetization":1,"margin_bridge":0,"cash_conversion":0,"relative_strength":2,"event_quality":2,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":52,"stage_label_after":"Stage4B_launch_expectation","changed_components":["repeat_monetization","margin_bridge","relative_strength","event_quality","accounting_trust_risk"],"component_delta_explanation":"Game launch expectation created MFE, but launch revenue and retention bridge were absent; high MAE blocks Green.","MFE_90D_pct":29.45,"MAE_90D_pct":-23.16,"source_proxy_only":true,"score_return_alignment_label":"game_launch_expectation_4B_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"293490","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_quality":2,"global_distribution":1,"repeat_monetization":1,"margin_bridge":1,"cash_conversion":0,"relative_strength":0,"event_quality":1,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_before":56,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"IP_quality":2,"global_distribution":1,"repeat_monetization":0,"margin_bridge":0,"cash_conversion":0,"relative_strength":0,"event_quality":0,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":37,"stage_label_after":"Stage4C","changed_components":["repeat_monetization","margin_bridge","event_quality"],"component_delta_explanation":"Game portfolio label lacked new IP retention or global monetization bridge and had deep MAE.","MFE_90D_pct":3.20,"MAE_90D_pct":-31.20,"source_proxy_only":true,"score_return_alignment_label":"game_portfolio_label_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"035900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_quality":3,"global_distribution":2,"repeat_monetization":1,"margin_bridge":1,"cash_conversion":0,"relative_strength":0,"event_quality":1,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"IP_quality":3,"global_distribution":2,"repeat_monetization":0,"margin_bridge":0,"cash_conversion":0,"relative_strength":0,"event_quality":0,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":39,"stage_label_after":"Stage4C","changed_components":["repeat_monetization","margin_bridge","event_quality"],"component_delta_explanation":"Artist-cycle label lacked durable catalog/touring/platform margin bridge and price path was poor.","MFE_90D_pct":2.21,"MAE_90D_pct":-34.91,"source_proxy_only":true,"score_return_alignment_label":"artist_cycle_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_quality":2,"global_distribution":2,"repeat_monetization":1,"margin_bridge":1,"cash_conversion":0,"relative_strength":0,"event_quality":1,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"IP_quality":2,"global_distribution":1,"repeat_monetization":0,"margin_bridge":0,"cash_conversion":0,"relative_strength":0,"event_quality":0,"execution_risk":5,"accounting_trust_risk":5},"weighted_score_after":37,"stage_label_after":"Stage4C","changed_components":["global_distribution","repeat_monetization","margin_bridge","event_quality"],"component_delta_explanation":"Drama slate/platform distribution label lacked retained margin and cash bridge.","MFE_90D_pct":4.91,"MAE_90D_pct":-27.61,"source_proxy_only":true,"score_return_alignment_label":"drama_slate_hard_4C_proxy","current_profile_verdict":"reverify_before_use"}
```

---

## 9. Current calibrated profile stress test

The C27 repeat-cash IP monetization gate held:

```text
direct box-office cash bridge
→ Stage2 can survive, but one-off cap remains

webtoon / anime / game option stack
→ local 4B until listed-company royalty/licensing cash is visible

kids character IP ecosystem
→ local 4B until merchandise/licensing margin is refreshed

global game IP with live-service economics
→ Stage2 can survive after direct reprice and revenue/cash proof

game launch expectation
→ local 4B

generic game portfolio, artist cycle, drama slate
→ hard 4C without repeat cash bridge
```

### Rule candidate retained, not newly proposed

```text
C27_CONTENT_IP_REPEAT_CASH_BRIDGE_GATE_V143_HELD_OUT

if C27
and content_IP_hit_game_drama_artist_or_character_label == true
and repeat_monetization_royalty_licensing_merchandise_live_service_distribution_margin_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C27
and direct_box_office_or_paid_distribution_cash_bridge == true
and MFE_90D_pct >= +15
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    apply_one_off_hit_cap_until_slate_or_library_repeat_bridge = true
```

```text
if C27
and IP_option_stack_or_character_flywheel == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -20
and listed_company_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C27
and game_launch_or_artist_cycle_or_drama_slate_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage4C
```

```text
if C27
and governance_tender_control_premium_mechanics_dominate == true:
    cap_C27_contribution = true
    require_reclassification_to_C32 = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with bridge/4B/4C guards
    eligible_trigger_count: 3
    source_proxy_trigger_count: 5
    avg_MFE_90D_pct: 24.16
    avg_MAE_90D_pct: -22.85
    false_positive_risk: high_if_IP_label_or_launch_label_is_left_actionable
    verdict: adequate_only_with_C27_repeat_cash_bridge_gate
  P0b_e2r_2_1_reference:
    hypothesis: prior profile may overcredit IP recognition and one-off hit labels
    eligible_trigger_count: 3
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L8 content/IP rows require repeat cash and margin bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C27 requires repeat monetization, not content hit vocabulary
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: launch hope, artist cycle and slate labels without repeat cash route to 4B/4C
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | source_proxy_only_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | CONTENT_IP_REPEAT_CASH_BRIDGE_HOLDOUT_V143 | 2 | 6 | 4 | 3 | 0 | 8 | 3 | 5 | 0 | 6 | false | false | 9 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 3
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 8
source_proxy_only_count: 5
batch_reverification_required_count: 5
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 6
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only_and_reverify_proxy_rows
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 8
reused_case_ids:
  - C27|263720|Stage4B|2024-01-08
  - C27|086980|Stage2-Actionable|2024-02-22
  - C27|419530|Stage4B|2024-09-09
  - C27|259960|Stage2-Actionable|2024-02-13
  - C27|263750|Stage4B|2024-06-03
  - C27|293490|Stage4C|2024-03-29
  - C27|035900|Stage4C|2024-01-29
  - C27|253450|Stage4C|2024-02-15
new_symbol_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 5
batch_reverification_required_count: 5
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C27_content_IP_repeat_cash_bridge_gate
  - C32_governance_reclassification_guard
residual_error_types_found:
  - one_off_hit_without_library_repeat
  - IP_option_stack_without_listed_company_cash
  - kids_character_IP_high_MAE
  - game_launch_expectation_without_retention
  - artist_cycle_without_recurring_cash_bridge
  - drama_slate_without_retained_margin
new_axis_proposed: null
existing_axis_strengthened:
  - C27_CONTENT_IP_REPEAT_CASH_BRIDGE_GATE_V143_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C27 candidate shards cache-missed or were unavailable
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"143","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":0,"reused_case_count":8,"new_symbol_count":0,"new_trigger_family_count":0,"source_proxy_only_count":5,"batch_reverification_required_count":5,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C27_content_IP_repeat_cash_bridge_gate","C32_governance_reclassification_guard"],"residual_error_types_found":["one_off_hit_without_library_repeat","IP_option_stack_without_listed_company_cash","kids_character_IP_high_MAE","game_launch_expectation_without_retention","artist_cycle_without_recurring_cash_bridge","drama_slate_without_retained_margin"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R8/C27 loop 143 as holdout validation only. Batch it with C27 loops 107 and 142, C26/C28 adjacent L8 rows, C32 governance/tender contamination rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C27 content-IP repeat-cash bridge, one-off-hit cap, IP-option-stack 4B guard, artist-cycle hard-4C guard, and C32 tender reclassification guard. Do not create a new weight delta from this loop because no new independent case was added and five rows are source_proxy_only. Future research should directly reprice 엔씨소프트(036570), 위메이드(112040), 컴투스(078340), 데브시스터즈(194480), 네오위즈(095660), 넥슨게임즈(225570), NHN(181710), 미스터블루(207760), 디앤씨미디어(263720), SAMG엔터(419530) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R8
completed_loop: 143
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```
