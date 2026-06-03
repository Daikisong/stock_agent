# E2R Stock-Web v12 Residual Research — R8 Loop 80 / L8 / C27

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 80,
  "computed_next_round": "R9",
  "computed_next_loop": 80,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "content_IP_global_monetization_guardrail",
    "game_IP_liveops_global_revenue_margin_bridge",
    "game_theme_fade_boundary",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R7 / loop 80.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 80
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
computed_next_round = R9
computed_next_loop = 80
```

R8 was routed to C27 because loop 79 R8 used C28.  
This file tests game/content IP monetization instead of platform ad leverage or SW/security contract retention.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C27 concentration in:

```text
035900, 253450, 352820, 122870, 036420
```

This run uses three different symbols:

```text
259960 / 크래프톤 / game IP global live-ops monetization bridge
194480 / 데브시스터즈 / cookie/game IP global launch lifecycle
293490 / 카카오게임즈 / game portfolio theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C27 is not “게임주가 올랐다.”

The mechanism must pass through:

```text
game / content IP
→ global launch or live-ops cadence
→ user retention, sales ranking or monetization metrics
→ revenue conversion
→ operating leverage and margin bridge
→ durable rerating
```

콘텐츠 IP는 불꽃놀이가 아니라 오래 타는 심지다.  
C27이 보려는 것은 첫 점화가 실제 유저 체류, 매출 전환, 마진으로 계속 타는지다.

---

## Case 1 — Game IP global live-ops positive: 259960 / 크래프톤

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is global live-ops, user metrics, PUBG/IP monetization, publishing cadence, revenue conversion and margin bridge evidence.

```text
evidence_family = GAME_IP_GLOBAL_LIVEOPS_PUBG_REVENUE_USER_METRICS_MARGIN_BRIDGE
case_role = positive_game_IP_global_liveops_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 212,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv`:

```text
2024-02-01,212000,217500,208500,214000
2024-02-14,227500,243000,226500,239500
2024-03-27,250000,265000,248000,257000
2024-06-21,293000,297000,290000,297000
2024-08-13,317500,331000,305500,331000
2024-08-22,346500,355000,337000,346000
2024-09-04,310000,318500,308000,310500
```

### Backtest

```text
MFE_30D  = +14.62%
MAE_30D  = -1.65%
MFE_90D  = +40.09%
MAE_90D  = -1.65%
MFE_180D = +67.45%
MAE_180D = -1.65%
peak_180 = 355,000 on 2024-08-22
trough_180 = 208,500 on 2024-02-01
peak_to_later_drawdown = -13.24%
```

### Interpretation

This is a clean C27 game-IP monetization positive.  
The MFE was strong and entry-basis MAE was shallow.

Correct treatment:

```text
verified global live-ops / user metrics / revenue / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Game IP launch lifecycle positive: 194480 / 데브시스터즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is Cookie Run / game IP global launch, live-ops cadence, user acquisition, sales ranking, revenue and margin bridge evidence.

```text
evidence_family = COOKIE_RUN_GAME_IP_GLOBAL_LAUNCH_LIVEOPS_REVENUE_MARKETING_MARGIN_BRIDGE
case_role = positive_game_IP_launch_with_later_high_MAE_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 40,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv`:

```text
2024-02-01,40100,40800,39000,39750
2024-02-07,37250,37900,36250,37200
2024-03-11,47200,50200,47050,49100
2024-05-10,50800,57500,50800,57000
2024-06-24,59100,62300,56100,57300
2024-06-26,65800,76300,65000,75700
2024-10-25,34200,34350,33750,34350
```

### Backtest

```text
MFE_30D  = +25.19%
MAE_30D  = -9.60%
MFE_90D  = +55.36%
MAE_90D  = -9.60%
MFE_180D = +90.27%
MAE_180D = -15.84%
peak_180 = 76,300 on 2024-06-26
trough_180 = 33,750 on 2024-10-25
peak_to_later_drawdown = -55.77%
```

### Interpretation

This is a lifecycle C27 positive.  
The launch/IP MFE was real, but post-peak fade forces live-ops and margin refresh.

Correct treatment:

```text
verified launch / live-ops / user acquisition / sales ranking / revenue bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 293490 / 카카오게임즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests game portfolio / new-title theme beta without enough global IP traction, user retention, revenue and margin bridge.

```text
evidence_family = GAME_PORTFOLIO_NEW_TITLE_THEME_WITH_WEAK_GLOBAL_IP_REVENUE_MARGIN_BRIDGE
case_role = counterexample_game_portfolio_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 24,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/293/293490/2024.csv`:

```text
2024-02-01,24300,24700,24000,24500
2024-02-08,25450,26450,25400,25450
2024-03-07,23200,23300,22800,22950
2024-04-08,21850,21900,21250,21350
2024-08-05,19140,19170,17300,17400
2024-09-10,16780,16860,16440,16620
2024-10-25,16910,16910,16400,16580
```

### Backtest

```text
MFE_30D  = +8.85%
MAE_30D  = -6.17%
MFE_90D  = +8.85%
MAE_90D  = -12.35%
MFE_180D = +8.85%
MAE_180D = -32.51%
peak_180 = 26,450 on 2024-02-08
trough_180 = 16,400 on 2024-10-25
peak_to_later_drawdown = -37.99%
```

### Interpretation

This is a C27 false-positive / local-4B boundary.  
The early new-title/portfolio MFE did not become durable IP monetization rerating.

Correct treatment:

```text
game portfolio theme beta
→ no verified user retention / global monetization / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
game_IP_monetization_bridge_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C27_game_content_theme_weight = true
do_not_treat_all_game_IP_MFE_as_Green = true
do_not_convert_game_theme_drawdown_to_hard_4C_without_non_price_title_failure_user_churn_revenue_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE
```

This fine archetype covers:

```text
1. global game IP live-ops monetization bridge → Stage2 possible after source repair
2. game IP launch / live-ops bridge → Stage2 possible, lifecycle-managed
3. game portfolio/new-title beta without user/revenue bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L80-C27-259960-KRAFTON-GAME-IP-GLOBAL-LIVEOPS-MONETIZATION", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "80", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GameIPGlobalLiveOpsRevenueMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should protect game-IP positives only when global live-ops, user metrics, monetization, publishing cadence, revenue conversion and margin bridge are visible. Krafton produced strong MFE with almost no entry-basis MAE, so it should not be overblocked after source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy game/content IP launch, live-ops, user metrics, global monetization, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L80-C27-194480-DEVSISTERS-COOKIE-IP-GLOBAL-LAUNCH-MARGIN", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "80", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-CookieIPGlobalLaunchLiveOpsRevenueBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should allow game-IP launch/live-ops positives when global launch cadence, user acquisition, sales ranking, revenue conversion and margin bridge are visible. Devsisters produced large MFE, but later drawdown makes lifecycle 4B necessary if post-launch metrics fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy game/content IP launch, live-ops, user metrics, global monetization, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L80-C27-293490-KAKAOGAMES-GAME-PORTFOLIO-THEME-FADE", "symbol": "293490", "company_name": "카카오게임즈", "round": "R8", "loop": "80", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / GamePortfolioThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should not treat game portfolio or new-title theme beta as durable Stage2 unless global IP traction, launch metrics, user retention, revenue conversion and margin bridge are visible. Kakao Games had small MFE and then a persistent MAE/downtrend path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy game/content IP launch, live-ops, user metrics, global monetization, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L80-C27-259960-KRAFTON-GAME-IP-GLOBAL-LIVEOPS-MONETIZATION", "case_id": "R8L80-C27-259960-KRAFTON-GAME-IP-GLOBAL-LIVEOPS-MONETIZATION", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "80", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-Actionable-GameIPGlobalLiveOpsRevenueMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 212000.0, "evidence_available_at_that_date": "GAME_IP_GLOBAL_LIVEOPS_PUBG_REVENUE_USER_METRICS_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KRAFTON_2024_GAME_IP_GLOBAL_LIVEOPS_USER_METRICS_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["game_content_IP_candidate", "global_liveops_or_launch_metrics_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "user_retention_or_sales_ranking_candidate"], "stage4b_evidence_fields": ["content_game_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.62, "MFE_90D_pct": 40.09, "MFE_180D_pct": 67.45, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -1.65, "peak_date": "2024-08-22", "peak_price": 355000.0, "drawdown_after_peak_pct": -13.24, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_game_IP_peak_if_launch_liveops_user_metrics_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_title_failure_user_churn_revenue_collapse_margin_or_financing_break", "trigger_outcome_label": "positive_game_IP_global_liveops_with_later_4b_watch", "current_profile_verdict": "C27 should protect game-IP positives only when global live-ops, user metrics, monetization, publishing cadence, revenue conversion and margin bridge are visible. Krafton produced strong MFE with almost no entry-basis MAE, so it should not be overblocked after source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C27_GAME_IP_259960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L80-C27-194480-DEVSISTERS-COOKIE-IP-GLOBAL-LAUNCH-MARGIN", "case_id": "R8L80-C27-194480-DEVSISTERS-COOKIE-IP-GLOBAL-LAUNCH-MARGIN", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "80", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-Lifecycle-CookieIPGlobalLaunchLiveOpsRevenueBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 40100.0, "evidence_available_at_that_date": "COOKIE_RUN_GAME_IP_GLOBAL_LAUNCH_LIVEOPS_REVENUE_MARKETING_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DEVSISTERS_2024_COOKIE_RUN_GAME_IP_GLOBAL_LAUNCH_LIVEOPS_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["game_content_IP_candidate", "global_liveops_or_launch_metrics_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "user_retention_or_sales_ranking_candidate"], "stage4b_evidence_fields": ["content_game_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.19, "MFE_90D_pct": 55.36, "MFE_180D_pct": 90.27, "MAE_30D_pct": -9.6, "MAE_90D_pct": -9.6, "MAE_180D_pct": -15.84, "peak_date": "2024-06-26", "peak_price": 76300.0, "drawdown_after_peak_pct": -55.77, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_game_IP_peak_if_launch_liveops_user_metrics_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_title_failure_user_churn_revenue_collapse_margin_or_financing_break", "trigger_outcome_label": "positive_game_IP_launch_with_later_high_MAE_4b_watch", "current_profile_verdict": "C27 should allow game-IP launch/live-ops positives when global launch cadence, user acquisition, sales ranking, revenue conversion and margin bridge are visible. Devsisters produced large MFE, but later drawdown makes lifecycle 4B necessary if post-launch metrics fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C27_GAME_IP_194480_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L80-C27-293490-KAKAOGAMES-GAME-PORTFOLIO-THEME-FADE", "case_id": "R8L80-C27-293490-KAKAOGAMES-GAME-PORTFOLIO-THEME-FADE", "symbol": "293490", "company_name": "카카오게임즈", "round": "R8", "loop": "80", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-FalsePositive / GamePortfolioThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 24300.0, "evidence_available_at_that_date": "GAME_PORTFOLIO_NEW_TITLE_THEME_WITH_WEAK_GLOBAL_IP_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KAKAO_GAMES_2024_GAME_PORTFOLIO_NEW_TITLE_GLOBAL_IP_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["game_content_IP_candidate", "global_liveops_or_launch_metrics_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "user_retention_or_sales_ranking_candidate"], "stage4b_evidence_fields": ["content_game_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293490/2024.csv", "profile_path": "atlas/symbol_profiles/293/293490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.85, "MFE_90D_pct": 8.85, "MFE_180D_pct": 8.85, "MAE_30D_pct": -6.17, "MAE_90D_pct": -12.35, "MAE_180D_pct": -32.51, "peak_date": "2024-02-08", "peak_price": 26450.0, "drawdown_after_peak_pct": -37.99, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_game_IP_peak_if_launch_liveops_user_metrics_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_title_failure_user_churn_revenue_collapse_margin_or_financing_break", "trigger_outcome_label": "counterexample_game_portfolio_theme_local4b", "current_profile_verdict": "C27 should not treat game portfolio or new-title theme beta as durable Stage2 unless global IP traction, launch metrics, user retention, revenue conversion and margin bridge are visible. Kakao Games had small MFE and then a persistent MAE/downtrend path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C27_GAME_IP_293490_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L80-C27-259960-KRAFTON-GAME-IP-GLOBAL-LIVEOPS-MONETIZATION", "trigger_id": "TRG_R8L80-C27-259960-KRAFTON-GAME-IP-GLOBAL-LIVEOPS-MONETIZATION", "symbol": "259960", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"game_IP_score": 14, "global_liveops_launch_score": 14, "user_metrics_score": 13, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"game_IP_score": 16, "global_liveops_launch_score": 16, "user_metrics_score": 15, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["game_IP_score", "global_liveops_launch_score", "user_metrics_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified game/content IP, live-ops or launch metrics, user retention, global monetization, revenue conversion and margin bridge; cap game theme beta when bridge fails to refresh.", "MFE_90D_pct": 40.09, "MAE_90D_pct": -1.65, "score_return_alignment_label": "game_IP_global_monetization_positive_with_lifecycle_4b", "current_profile_verdict": "C27 should protect game-IP positives only when global live-ops, user metrics, monetization, publishing cadence, revenue conversion and margin bridge are visible. Krafton produced strong MFE with almost no entry-basis MAE, so it should not be overblocked after source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L80-C27-194480-DEVSISTERS-COOKIE-IP-GLOBAL-LAUNCH-MARGIN", "trigger_id": "TRG_R8L80-C27-194480-DEVSISTERS-COOKIE-IP-GLOBAL-LAUNCH-MARGIN", "symbol": "194480", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"game_IP_score": 14, "global_liveops_launch_score": 14, "user_metrics_score": 13, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"game_IP_score": 16, "global_liveops_launch_score": 16, "user_metrics_score": 15, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["game_IP_score", "global_liveops_launch_score", "user_metrics_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified game/content IP, live-ops or launch metrics, user retention, global monetization, revenue conversion and margin bridge; cap game theme beta when bridge fails to refresh.", "MFE_90D_pct": 55.36, "MAE_90D_pct": -9.6, "score_return_alignment_label": "game_IP_global_monetization_positive_with_lifecycle_4b", "current_profile_verdict": "C27 should allow game-IP launch/live-ops positives when global launch cadence, user acquisition, sales ranking, revenue conversion and margin bridge are visible. Devsisters produced large MFE, but later drawdown makes lifecycle 4B necessary if post-launch metrics fade."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L80-C27-293490-KAKAOGAMES-GAME-PORTFOLIO-THEME-FADE", "trigger_id": "TRG_R8L80-C27-293490-KAKAOGAMES-GAME-PORTFOLIO-THEME-FADE", "symbol": "293490", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"game_IP_score": 5, "global_liveops_launch_score": 3, "user_metrics_score": 2, "revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 44, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"game_IP_score": 3, "global_liveops_launch_score": 1, "user_metrics_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["game_IP_score", "global_liveops_launch_score", "user_metrics_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified game/content IP, live-ops or launch metrics, user retention, global monetization, revenue conversion and margin bridge; cap game theme beta when bridge fails to refresh.", "MFE_90D_pct": 8.85, "MAE_90D_pct": -12.35, "score_return_alignment_label": "false_positive_game_portfolio_bridge_gap", "current_profile_verdict": "C27 should not treat game portfolio or new-title theme beta as durable Stage2 unless global IP traction, launch metrics, user retention, revenue conversion and margin bridge are visible. Kakao Games had small MFE and then a persistent MAE/downtrend path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 80, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE_VS_GAME_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C27 game/content IP symbols outside top-covered 035900/253450/352820/122870/036420 set, +3 global live-ops/cookie-IP/game-portfolio trigger families, +2 game IP monetization positives, +1 game portfolio local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 80, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "axis": "game_IP_global_liveops_monetization_margin_bridge_vs_game_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C27 should split verified game/content IP monetization rerating from generic game portfolio/new-title theme beta. Stage2 requires IP quality, global live-ops or launch metrics, user retention/sales ranking, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["259960", "194480", "293490"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 80, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "game_IP_monetization_bridge_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C27 needs content/game IP, global live-ops, launch metrics, user retention, revenue conversion and margin proof. Krafton and Devsisters show game-IP monetization positives after source repair; Kakao Games shows game portfolio theme beta fading into local 4B when user/revenue/margin bridge is absent or stale."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
259960:
  name = 크래프톤
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

194480:
  name = 데브시스터즈
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

293490:
  name = 카카오게임즈
  market = KOSDAQ GLOBAL during 2024
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C27 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C27 rule-shape discovery,
but coding-agent promotion requires non-proxy game/content IP launch, live-ops, user metrics, global monetization, revenue conversion and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C27 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
game_IP_global_liveops_monetization_margin_bridge_vs_game_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 259960, 194480 and 293490.
4. Keep generic C27 content/game-IP weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - game/content IP quality is explicit,
   - global launch or live-ops cadence is visible,
   - user retention, sales ranking or monetization metrics exist,
   - revenue conversion and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is game/content theme beta only,
   - user/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price title failure, user churn, revenue collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified game-IP monetization positives are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 80
next_round = R9
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

