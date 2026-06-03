# E2R Stock-Web v12 Residual Research — R8 Loop 78 / L8 / C27

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 78,
  "computed_next_round": "R9",
  "computed_next_loop": 78,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "content_IP_global_monetization_guardrail",
    "game_launch_DAU_revenue_retention_margin_bridge_vs_IP_theme_beta",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R7 / loop 78.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 78
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
computed_next_round = R9
computed_next_loop = 78
```

R8 was routed to C27 because loop 77 used C26.  
This file tests game/content IP global monetization rather than platform ad revenue or software/security contract retention.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C27 is concentrated in:

```text
035900, 253450, 352820, 122870, 036420
```

This run uses three different symbols:

```text
225570 / 넥슨게임즈 / global game launch and live-ops monetization bridge
194480 / 데브시스터즈 / game-IP reacceleration and global monetization bridge
095660 / 네오위즈 / game-IP theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
225570 and 194480 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C27 is not “게임주가 올랐다.”

The mechanism must pass through:

```text
content IP / game launch or major update
→ global user traction
→ retention and live-ops cadence
→ revenue rank / monetization
→ margin or operating leverage bridge
→ durable rerating
```

게임 IP는 첫날 다운로드 숫자가 아니라 서버에 남아 있는 사람들이다.  
C27이 보려는 것은 출시의 불꽃이 유저 유지, 매출 순위, 라이브 운영, 마진으로 이어지는지다.

---

## Case 1 — Positive with validation: 225570 / 넥슨게임즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is global launch traction, concurrent users/DAU, live-ops retention, monetization and margin bridge evidence.

```text
evidence_family = GAME_IP_GLOBAL_LAUNCH_CONCURRENT_USERS_DAU_LIVEOPS_REVENUE_RETENTION_MARGIN_BRIDGE
case_role = positive_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-07-02
entry_date = 2024-07-03
entry_price = 18,610
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv`:

```text
2024-07-03,18610,18950,16490,17900
2024-07-08,20500,22400,20050,21500
2024-07-24,21300,22750,21200,22000
2024-08-01,24050,30200,23900,28800
2024-08-09,28000,30950,27550,28850
2024-09-10,15360,15360,14760,14860
2024-10-25,14600,14680,14410,14550
```

### Backtest

```text
MFE_30D  = +66.31%
MAE_30D  = -11.39%
MFE_90D  = +66.31%
MAE_90D  = -20.69%
MFE_180D = +66.31%
MAE_180D = -20.69%
peak_180 = 30,950 on 2024-08-09
trough_180 = 14,760 on 2024-09-10
peak_to_later_drawdown = -52.31%
```

### Interpretation

This is a C27 game-launch MFE candidate, not permanent Green.  
The initial launch traction was price-relevant, but the later drawdown says user retention, revenue rank and margin evidence must refresh.

Correct treatment:

```text
verified launch / user retention / monetization / margin bridge → Stage2 possible
share-count validation first
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Positive with validation: 194480 / 데브시스터즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is game-IP update/launch traction, DAU retention, revenue rank, overseas channel and margin bridge evidence.

```text
evidence_family = GAME_IP_GLOBAL_REACCELERATION_LAUNCH_UPDATE_DAU_REVENUE_MARGIN_BRIDGE
case_role = positive_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 39,750
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv`:

```text
2024-02-01,40100,40800,39000,39750
2024-02-06,38350,38400,37000,37200
2024-03-11,47200,50200,47050,49100
2024-05-10,50800,57500,50800,57000
2024-06-26,65800,76300,65000,75700
2024-08-05,48050,48050,42250,42800
2024-10-25,34200,34350,33750,34350
```

### Backtest

```text
MFE_30D  = +26.29%
MAE_30D  = -6.92%
MFE_90D  = +91.95%
MAE_90D  = -6.92%
MFE_180D = +91.95%
MAE_180D = -15.09%
peak_180 = 76,300 on 2024-06-26
trough_180 = 33,750 on 2024-10-25
peak_to_later_drawdown = -55.77%
```

### Interpretation

This is a C27 game-IP reacceleration positive with lifecycle risk.  
The MFE was large and early MAE was controlled, but monetization evidence must refresh after the peak.

Correct treatment:

```text
verified IP reacceleration / DAU / revenue rank / margin bridge → Stage2 possible
share-count validation first
bridge stale after peak → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 095660 / 네오위즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests game-IP / PC-console title beta without enough live-ops, revenue and margin bridge.

```text
evidence_family = GAME_IP_CONSOLE_PC_THEME_WITH_WEAK_LIVEOPS_REVENUE_MARGIN_BRIDGE
case_role = counterexample_game_IP_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 25,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/095/095660/2024.csv`:

```text
2024-02-01,25350,25450,24650,25150
2024-02-02,25300,28700,25000,26400
2024-02-27,22800,23200,22600,22650
2024-04-08,20950,20950,20350,20550
2024-08-05,19810,19950,17550,17830
2024-10-25,19860,19990,19400,19490
```

### Backtest

```text
MFE_30D  = +13.21%
MAE_30D  = -10.65%
MFE_90D  = +13.21%
MAE_90D  = -23.87%
MFE_180D = +13.21%
MAE_180D = -30.77%
peak_180 = 28,700 on 2024-02-02
trough_180 = 17,550 on 2024-08-05
peak_to_later_drawdown = -38.85%
```

### Interpretation

This is the C27 game-IP false-positive boundary.  
A brief theme spike did not become durable monetization.

Correct treatment:

```text
game-IP / PC-console theme beta
→ no verified user retention / live-ops / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C27_game_IP_theme_weight = true
do_not_treat_all_game_IP_MFE_as_Green = true
do_not_convert_game_IP_drawdown_to_hard_4C_without_non_price_launch_user_revenue_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE
```

This fine archetype covers:

```text
1. global launch / live-ops monetization bridge → Stage2 possible after source repair
2. IP reacceleration / update revenue bridge → Stage2 possible, lifecycle-managed
3. PC-console/game-IP theme beta without live-ops revenue bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L78-C27-225570-NEXON-GAMES-GLOBAL-LAUNCH-LIVEOPS", "symbol": "225570", "company_name": "넥슨게임즈", "round": "R8", "loop": "78", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE", "case_type": "content_IP_global_monetization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GameIPGlobalLaunchLiveOpsBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should allow game-IP launch positives when global launch, user traction, live-ops retention, monetization and operating-leverage bridge are visible. Nexon Games produced large MFE, but the later post-peak drawdown means user/revenue/retention evidence must refresh. Share-count changes inside the window need validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy launch/update traction, user retention, revenue rank, overseas channel, content pipeline and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L78-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-MONETIZATION", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "78", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE", "case_type": "content_IP_global_monetization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GameIPReaccelerationGlobalMonetizationBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should preserve game-IP monetization positives only when launch/update traction, DAU retention, revenue rank, overseas channel and margin bridge are visible. Devsisters produced very large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle 4B if IP monetization evidence fades. Share-count movement inside the raw shard requires validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy launch/update traction, user retention, revenue rank, overseas channel, content pipeline and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L78-C27-095660-NEOWIZ-GAME-IP-THEME-FADE", "symbol": "095660", "company_name": "네오위즈", "round": "R8", "loop": "78", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE", "case_type": "content_IP_global_monetization", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / GameIPThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should not treat game-IP or PC/console title beta as durable Stage2 unless user retention, live-ops, revenue rank, content pipeline and margin bridge are visible. Neowiz had a brief MFE and then a large drawdown, making it a local 4B-watch boundary rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy launch/update traction, user retention, revenue rank, overseas channel, content pipeline and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L78-C27-225570-NEXON-GAMES-GLOBAL-LAUNCH-LIVEOPS", "case_id": "R8L78-C27-225570-NEXON-GAMES-GLOBAL-LAUNCH-LIVEOPS", "symbol": "225570", "company_name": "넥슨게임즈", "round": "R8", "loop": "78", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-Actionable-GameIPGlobalLaunchLiveOpsBridgeWithLifecycle4B", "trigger_date": "2024-07-02", "entry_date": "2024-07-03", "entry_price": 18610.0, "evidence_available_at_that_date": "GAME_IP_GLOBAL_LAUNCH_CONCURRENT_USERS_DAU_LIVEOPS_REVENUE_RETENTION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NEXON_GAMES_2024_GLOBAL_LAUNCH_LIVEOPS_USERS_REVENUE_RETENTION_MARGIN_BRIDGE", "stage2_evidence_fields": ["content_IP_or_game_launch_candidate", "user_retention_or_revenue_rank_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "overseas_channel_or_content_pipeline_candidate"], "stage4b_evidence_fields": ["game_IP_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv", "profile_path": "atlas/symbol_profiles/225/225570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 66.31, "MFE_90D_pct": 66.31, "MFE_180D_pct": 66.31, "MAE_30D_pct": -11.39, "MAE_90D_pct": -20.69, "MAE_180D_pct": -20.69, "peak_date": "2024-08-09", "peak_price": 30950.0, "drawdown_after_peak_pct": -52.31, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_game_IP_peak_if_users_revenue_retention_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_launch_failure_user_churn_revenue_rank_collapse_pipeline_delay_margin_or_financing_break", "trigger_outcome_label": "positive_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C27 should allow game-IP launch positives when global launch, user traction, live-ops retention, monetization and operating-leverage bridge are visible. Nexon Games produced large MFE, but the later post-peak drawdown means user/revenue/retention evidence must refresh. Share-count changes inside the window need validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C27_GAME_IP_225570_2024-07-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L78-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-MONETIZATION", "case_id": "R8L78-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-MONETIZATION", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "78", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-Actionable-GameIPReaccelerationGlobalMonetizationBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 39750.0, "evidence_available_at_that_date": "GAME_IP_GLOBAL_REACCELERATION_LAUNCH_UPDATE_DAU_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DEVSISTERS_2024_GAME_IP_LAUNCH_UPDATE_GLOBAL_REVENUE_DAU_MARGIN_BRIDGE", "stage2_evidence_fields": ["content_IP_or_game_launch_candidate", "user_retention_or_revenue_rank_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "overseas_channel_or_content_pipeline_candidate"], "stage4b_evidence_fields": ["game_IP_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.29, "MFE_90D_pct": 91.95, "MFE_180D_pct": 91.95, "MAE_30D_pct": -6.92, "MAE_90D_pct": -6.92, "MAE_180D_pct": -15.09, "peak_date": "2024-06-26", "peak_price": 76300.0, "drawdown_after_peak_pct": -55.77, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_game_IP_peak_if_users_revenue_retention_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_launch_failure_user_churn_revenue_rank_collapse_pipeline_delay_margin_or_financing_break", "trigger_outcome_label": "positive_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C27 should preserve game-IP monetization positives only when launch/update traction, DAU retention, revenue rank, overseas channel and margin bridge are visible. Devsisters produced very large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle 4B if IP monetization evidence fades. Share-count movement inside the raw shard requires validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C27_GAME_IP_194480_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L78-C27-095660-NEOWIZ-GAME-IP-THEME-FADE", "case_id": "R8L78-C27-095660-NEOWIZ-GAME-IP-THEME-FADE", "symbol": "095660", "company_name": "네오위즈", "round": "R8", "loop": "78", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-FalsePositive / GameIPThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 25350.0, "evidence_available_at_that_date": "GAME_IP_CONSOLE_PC_THEME_WITH_WEAK_LIVEOPS_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NEOWIZ_2024_GAME_IP_PC_CONSOLE_REVENUE_LIVEOPS_MARGIN_BRIDGE", "stage2_evidence_fields": ["content_IP_or_game_launch_candidate", "user_retention_or_revenue_rank_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "overseas_channel_or_content_pipeline_candidate"], "stage4b_evidence_fields": ["game_IP_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095660/2024.csv", "profile_path": "atlas/symbol_profiles/095/095660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.21, "MFE_90D_pct": 13.21, "MFE_180D_pct": 13.21, "MAE_30D_pct": -10.65, "MAE_90D_pct": -23.87, "MAE_180D_pct": -30.77, "peak_date": "2024-02-02", "peak_price": 28700.0, "drawdown_after_peak_pct": -38.85, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_game_IP_peak_if_users_revenue_retention_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_launch_failure_user_churn_revenue_rank_collapse_pipeline_delay_margin_or_financing_break", "trigger_outcome_label": "counterexample_game_IP_theme_local4b", "current_profile_verdict": "C27 should not treat game-IP or PC/console title beta as durable Stage2 unless user retention, live-ops, revenue rank, content pipeline and margin bridge are visible. Neowiz had a brief MFE and then a large drawdown, making it a local 4B-watch boundary rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C27_GAME_IP_095660_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L78-C27-225570-NEXON-GAMES-GLOBAL-LAUNCH-LIVEOPS", "trigger_id": "TRG_R8L78-C27-225570-NEXON-GAMES-GLOBAL-LAUNCH-LIVEOPS", "symbol": "225570", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"content_IP_score": 14, "global_launch_score": 14, "user_retention_score": 13, "revenue_rank_score": 13, "margin_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 9, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"content_IP_score": 16, "global_launch_score": 16, "user_retention_score": 15, "revenue_rank_score": 15, "margin_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 10, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["content_IP_score", "global_launch_score", "user_retention_score", "revenue_rank_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified IP launch/update traction, user retention, revenue rank, overseas channel and margin bridge; cap game-IP theme beta when evidence fails to refresh.", "MFE_90D_pct": 66.31, "MAE_90D_pct": -20.69, "score_return_alignment_label": "game_IP_monetization_positive_with_lifecycle_4b", "current_profile_verdict": "C27 should allow game-IP launch positives when global launch, user traction, live-ops retention, monetization and operating-leverage bridge are visible. Nexon Games produced large MFE, but the later post-peak drawdown means user/revenue/retention evidence must refresh. Share-count changes inside the window need validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L78-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-MONETIZATION", "trigger_id": "TRG_R8L78-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-MONETIZATION", "symbol": "194480", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"content_IP_score": 14, "global_launch_score": 14, "user_retention_score": 13, "revenue_rank_score": 13, "margin_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 9, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"content_IP_score": 16, "global_launch_score": 16, "user_retention_score": 15, "revenue_rank_score": 15, "margin_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 10, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["content_IP_score", "global_launch_score", "user_retention_score", "revenue_rank_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified IP launch/update traction, user retention, revenue rank, overseas channel and margin bridge; cap game-IP theme beta when evidence fails to refresh.", "MFE_90D_pct": 91.95, "MAE_90D_pct": -6.92, "score_return_alignment_label": "game_IP_monetization_positive_with_lifecycle_4b", "current_profile_verdict": "C27 should preserve game-IP monetization positives only when launch/update traction, DAU retention, revenue rank, overseas channel and margin bridge are visible. Devsisters produced very large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle 4B if IP monetization evidence fades. Share-count movement inside the raw shard requires validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L78-C27-095660-NEOWIZ-GAME-IP-THEME-FADE", "trigger_id": "TRG_R8L78-C27-095660-NEOWIZ-GAME-IP-THEME-FADE", "symbol": "095660", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"content_IP_score": 6, "global_launch_score": 3, "user_retention_score": 2, "revenue_rank_score": 2, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 22, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"content_IP_score": 3, "global_launch_score": 1, "user_retention_score": 1, "revenue_rank_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["content_IP_score", "global_launch_score", "user_retention_score", "revenue_rank_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified IP launch/update traction, user retention, revenue rank, overseas channel and margin bridge; cap game-IP theme beta when evidence fails to refresh.", "MFE_90D_pct": 13.21, "MAE_90D_pct": -23.87, "score_return_alignment_label": "false_positive_game_IP_bridge_gap", "current_profile_verdict": "C27 should not treat game-IP or PC/console title beta as durable Stage2 unless user retention, live-ops, revenue rank, content pipeline and margin bridge are visible. Neowiz had a brief MFE and then a large drawdown, making it a local 4B-watch boundary rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 78, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_GAME_IP_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "post_corporate_action_validation_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C27 game/IP symbols outside top-covered 035900/253450/352820/122870/036420 set, +3 global-launch/reacceleration/PC-console trigger families, +2 game-IP monetization positives, +1 game-IP beta local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 78, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "axis": "game_IP_global_launch_liveops_monetization_bridge_vs_game_IP_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C27 should split verified game/content IP global monetization rerating from generic IP/theme beta. Stage2 requires launch or update traction, user retention, revenue rank, overseas channel, content pipeline and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["225570", "194480", "095660"], "share_count_validation_required": ["225570", "194480"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 78, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C27 needs IP monetization proof. Nexon Games and Devsisters show game-IP launch/reacceleration MFE candidates after source repair; Neowiz shows game-IP theme beta fading into local 4B when launch traction, live-ops retention, revenue and margin bridge are absent or stale."}
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
225570:
  name = 넥슨게임즈 from 2022-04-15, 넷게임즈 before that
  corporate_action_candidate_dates = 2017-06-12, 2018-05-09, 2022-04-15
  selected window = 2024-07-03~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

194480:
  name = 데브시스터즈
  corporate_action_candidate_dates = none by profile
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

095660:
  name = 네오위즈 from 2017-04-19, 네오위즈게임즈 before that
  corporate_action_candidate_dates = 2007-11-09, 2007-12-05, 2009-06-16, 2009-07-14
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C27 rows are source_proxy_only / evidence_url_pending.
225570 and 194480 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C27 rule-shape discovery,
but coding-agent promotion requires non-proxy launch/update traction, user retention, revenue rank, overseas channel, content pipeline and margin bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C27 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 225570/194480 need share-count validation.

Candidate axis:
game_IP_global_launch_liveops_monetization_bridge_vs_game_IP_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 225570, 194480 and 095660.
4. Validate 225570 and 194480 share-count changes inside the selected window.
5. Keep generic C27 content-IP/global-monetization weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - content IP / game launch or major update is explicit,
   - global user traction is visible,
   - retention and live-ops cadence are visible,
   - revenue rank / monetization bridge exists,
   - margin / operating leverage bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is game-IP or content theme beta only,
   - retention/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price launch failure, user churn, revenue-rank collapse, content-pipeline delay, financing or margin break.
9. Emit before/after diagnostics and reject if verified game-IP monetization positives are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 78
next_round = R9
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

