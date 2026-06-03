# E2R Stock-Web v12 Residual Research — R8 Loop 76 / L8 / C27

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 76,
  "computed_next_round": "R9",
  "computed_next_loop": 76,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "content_IP_global_monetization_guardrail",
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

Previous completed state in this interactive run: R7 / loop 76.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 76
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
computed_next_round = R9
computed_next_loop = 76
```

R8 was routed to C27 because loop 75 used C28.  
This file tests content-IP global monetization rather than software/security contract retention.

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
194480 / 데브시스터즈 / game IP global launch monetization
206560 / 덱스터 / VFX content production pipeline bridge
207760 / 미스터블루 / webtoon IP theme spike fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
194480 and 207760 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C27 is not “content stock went up.”

The mechanism must pass through:

```text
content IP / game / webtoon / VFX service
→ global launch, distribution, user traffic or production pipeline
→ paid conversion, licensing, royalty or order backlog
→ margin bridge
→ durable rerating
```

An IP headline is a trailer.  
C27 asks whether the audience buys tickets, subscriptions, in-app items, licenses, or production orders.

---

## Case 1 — Positive with lifecycle 4B: 194480 / 데브시스터즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is global launch, DAU/MAU, IAP revenue, platform revenue, royalty/licensing and margin bridge evidence.

```text
evidence_family = GAME_IP_GLOBAL_LAUNCH_DAU_IAP_REVENUE_PLATFORM_ROYALTY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch_and_sharecount_validation
trigger_date = 2024-02-22
entry_date = 2024-02-23
entry_price = 42,550
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv`:

```text
2024-02-23,42550,42550,41050,41050
2024-03-11,47200,50200,47050,49100
2024-05-14,57000,61200,57000,57800
2024-06-26,65800,76300,65000,75700
2024-08-05,48050,48050,42250,42800
2024-10-25,34200,34350,33750,34350
```

### Backtest

```text
MFE_30D  = +17.98%
MAE_30D  = -6.93%
MFE_90D  = +79.32%
MAE_90D  = -6.93%
MFE_180D = +79.32%
MAE_180D = -20.68%
peak_180 = 76,300 on 2024-06-26
trough_180 = 33,750 on 2024-10-25
peak_to_later_drawdown = -55.77%
```

### Interpretation

This is a C27 positive-shaped path, but not permanent Green.  
The MFE says the game IP monetization story became tradable. The later drawdown says the model needs lifecycle 4B if revenue bridge decays.

Correct treatment:

```text
verified global launch / DAU / IAP / margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Positive boundary: 206560 / 덱스터

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is VFX/content production pipeline, order backlog, global IP service revenue, delivery schedule and margin bridge evidence.

```text
evidence_family = VFX_CONTENT_PRODUCTION_PIPELINE_ORDER_BACKLOG_GLOBAL_IP_SERVICE_MARGIN_BRIDGE
case_role = positive_boundary_with_source_repair
trigger_date = 2024-08-20
entry_date = 2024-08-21
entry_price = 6,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/206/206560/2024.csv`:

```text
2024-08-21,6000,7040,5790,6710
2024-08-22,6660,7230,6560,6630
2024-09-05,5970,7350,5940,6990
2024-09-27,7130,8240,7070,7550
2024-11-01,7490,7660,7370,7370
```

### Backtest

```text
MFE_30D  = +37.33%
MAE_30D  = -3.50%
MFE_90D  = +37.33%
MAE_90D  = -3.50%
MFE_180D = +37.33%
MAE_180D = -3.50%
peak_180 = 8,240 on 2024-09-27
trough_180 = 5,790 on 2024-08-21
peak_to_later_drawdown = -10.56%
```

### Interpretation

This is a positive boundary row.  
It should not be promoted merely because price behaved well; it needs order and margin evidence. But it prevents C27 from overfitting only to labels/games/webtoons.

Correct treatment:

```text
source repair first
possible Stage2-Yellow
protect if production pipeline / backlog / margin bridge is confirmed
```

---

## Case 3 — Counterexample / local 4B: 207760 / 미스터블루

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests webtoon/IP/platform theme MFE without enough paid-content, global distribution, licensing and margin bridge.

```text
evidence_family = WEBTOON_IP_PLATFORM_THEME_SPIKE_WITH_WEAK_PAID_CONTENT_GLOBAL_REVENUE_MARGIN_BRIDGE
case_role = counterexample_webtoon_theme_local4b_with_sharecount_validation
trigger_date = 2024-01-23
entry_date = 2024-01-24
entry_price = 2,260
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/207/207760/2024.csv`:

```text
2024-01-24,2260,2865,2240,2865
2024-01-25,2660,3015,2540,2765
2024-02-20,2765,3190,2670,2955
2024-06-03,2870,2995,2675,2730
2024-08-05,1575,1578,1290,1380
2024-09-09,1230,1300,1190,1274
```

### Backtest

```text
MFE_30D  = +41.15%
MAE_30D  = -3.76%
MFE_90D  = +41.15%
MAE_90D  = -3.76%
MFE_180D = +41.15%
MAE_180D = -47.35%
peak_180 = 3,190 on 2024-02-20
trough_180 = 1,190 on 2024-09-09
peak_to_later_drawdown = -62.70%
```

### Interpretation

This is the dangerous C27 false-positive shape.  
The early MFE was real, but it did not prove durable monetization.

Correct treatment:

```text
webtoon/IP theme spike
→ no paid-content/global/licensing/margin bridge
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
do_not_raise_generic_C27_content_IP_weight = true
do_not_treat_all_content_IP_MFE_as_Green = true
do_not_convert_content_IP_drawdown_to_hard_4C_without_non_price_revenue_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE
```

This fine archetype covers:

```text
1. game IP global launch / IAP / margin bridge → Stage2 possible after source repair
2. VFX/content production pipeline / order backlog → boundary Stage2 possible after source repair
3. webtoon/IP theme spike without paid-content/global margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "76", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GameIPGlobalLaunchMonetizationBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should allow game-IP positives when global launch, DAU/MAU, IAP revenue, platform monetization, royalty/licensing and margin bridge are visible. Devsisters produced large MFE but later post-peak drawdown and share-count movement require lifecycle local 4B and validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy DAU/MAU, paid content, global launch/distribution, licensing/royalty, production backlog and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE", "symbol": "206560", "company_name": "덱스터", "round": "R8", "loop": "76", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-BoundaryPositive-VFXContentProductionPipelineBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should not only include idol/label/game names; VFX/content production pipelines can be C27 when order backlog, production schedule, global IP service revenue and margin bridge are visible. Dexter produced controlled-MAE follow-through, but needs non-price order/pipeline evidence before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy DAU/MAU, paid content, global launch/distribution, licensing/royalty, production backlog and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE", "symbol": "207760", "company_name": "미스터블루", "round": "R8", "loop": "76", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / WebtoonIPThemeSpikeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should not treat webtoon/IP/platform theme spikes as durable Stage2 unless paid-content revenue, subscriber/traffic conversion, global distribution, licensing and margin bridge are visible. Mr. Blue produced large MFE but later collapsed into a high-MAE local 4B path; share-count movement requires validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy DAU/MAU, paid content, global launch/distribution, licensing/royalty, production backlog and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION", "case_id": "R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION", "symbol": "194480", "company_name": "데브시스터즈", "round": "R8", "loop": "76", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-Actionable-GameIPGlobalLaunchMonetizationBridgeWithLifecycle4B", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 42550.0, "evidence_available_at_that_date": "GAME_IP_GLOBAL_LAUNCH_DAU_IAP_REVENUE_PLATFORM_ROYALTY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DEVSISTERS_2024_COOKIE_RUN_GAME_IP_GLOBAL_LAUNCH_DAU_IAP_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["content_IP", "global_launch_or_distribution_candidate", "revenue_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "paid_content_licensing_or_order_backlog_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv", "profile_path": "atlas/symbol_profiles/194/194480.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.98, "MFE_90D_pct": 79.32, "MFE_180D_pct": 79.32, "MAE_30D_pct": -6.93, "MAE_90D_pct": -6.93, "MAE_180D_pct": -20.68, "peak_date": "2024-06-26", "peak_price": 76300.0, "drawdown_after_peak_pct": -55.77, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_content_IP_peak_if_monetization_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_revenue_user_licensing_backlog_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "current_profile_verdict": "C27 should allow game-IP positives when global launch, DAU/MAU, IAP revenue, platform monetization, royalty/licensing and margin bridge are visible. Devsisters produced large MFE but later post-peak drawdown and share-count movement require lifecycle local 4B and validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C27_CONTENT_IP_194480_2024-02-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE", "case_id": "R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE", "symbol": "206560", "company_name": "덱스터", "round": "R8", "loop": "76", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-BoundaryPositive-VFXContentProductionPipelineBridge", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 6000.0, "evidence_available_at_that_date": "VFX_CONTENT_PRODUCTION_PIPELINE_ORDER_BACKLOG_GLOBAL_IP_SERVICE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DEXTER_2024_VFX_CONTENT_PRODUCTION_GLOBAL_IP_SERVICE_ORDER_BACKLOG_MARGIN_BRIDGE", "stage2_evidence_fields": ["content_IP", "global_launch_or_distribution_candidate", "revenue_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "paid_content_licensing_or_order_backlog_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/206/206560/2024.csv", "profile_path": "atlas/symbol_profiles/206/206560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 37.33, "MFE_90D_pct": 37.33, "MFE_180D_pct": 37.33, "MAE_30D_pct": -3.5, "MAE_90D_pct": -3.5, "MAE_180D_pct": -3.5, "peak_date": "2024-09-27", "peak_price": 8240.0, "drawdown_after_peak_pct": -10.56, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_content_IP_peak_if_monetization_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_revenue_user_licensing_backlog_or_margin_break", "trigger_outcome_label": "positive_boundary_with_source_repair", "current_profile_verdict": "C27 should not only include idol/label/game names; VFX/content production pipelines can be C27 when order backlog, production schedule, global IP service revenue and margin bridge are visible. Dexter produced controlled-MAE follow-through, but needs non-price order/pipeline evidence before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C27_CONTENT_IP_206560_2024-08-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE", "case_id": "R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE", "symbol": "207760", "company_name": "미스터블루", "round": "R8", "loop": "76", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail", "trigger_type": "Stage2-FalsePositive / WebtoonIPThemeSpikeFade", "trigger_date": "2024-01-23", "entry_date": "2024-01-24", "entry_price": 2260.0, "evidence_available_at_that_date": "WEBTOON_IP_PLATFORM_THEME_SPIKE_WITH_WEAK_PAID_CONTENT_GLOBAL_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MRBLUE_2024_WEBTOON_IP_PLATFORM_PAID_CONTENT_GLOBAL_DISTRIBUTION_LICENSING_MARGIN_BRIDGE", "stage2_evidence_fields": ["content_IP", "global_launch_or_distribution_candidate", "revenue_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "paid_content_licensing_or_order_backlog_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/207/207760/2024.csv", "profile_path": "atlas/symbol_profiles/207/207760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 41.15, "MFE_90D_pct": 41.15, "MFE_180D_pct": 41.15, "MAE_30D_pct": -3.76, "MAE_90D_pct": -3.76, "MAE_180D_pct": -47.35, "peak_date": "2024-02-20", "peak_price": 3190.0, "drawdown_after_peak_pct": -62.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_content_IP_peak_if_monetization_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_revenue_user_licensing_backlog_or_margin_break", "trigger_outcome_label": "counterexample_webtoon_theme_local4b_with_sharecount_validation", "current_profile_verdict": "C27 should not treat webtoon/IP/platform theme spikes as durable Stage2 unless paid-content revenue, subscriber/traffic conversion, global distribution, licensing and margin bridge are visible. Mr. Blue produced large MFE but later collapsed into a high-MAE local 4B path; share-count movement requires validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C27_CONTENT_IP_207760_2024-01-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION", "trigger_id": "TRG_R8L76-C27-194480-DEVSISTERS-GAME-IP-GLOBAL-LAUNCH-MONETIZATION", "symbol": "194480", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"content_IP_score": 13, "global_distribution_score": 13, "paid_content_or_IAP_score": 14, "licensing_or_backlog_score": 12, "margin_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"content_IP_score": 15, "global_distribution_score": 15, "paid_content_or_IAP_score": 16, "licensing_or_backlog_score": 14, "margin_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["global_distribution_score", "paid_content_or_IAP_score", "licensing_or_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global launch/distribution, DAU/MAU/IAP, paid-content conversion, licensing/backlog and margin bridge; cap content/IP theme spikes when monetization evidence is absent or stale.", "MFE_90D_pct": 79.32, "MAE_90D_pct": -6.93, "score_return_alignment_label": "content_IP_positive_with_lifecycle_4b", "current_profile_verdict": "C27 should allow game-IP positives when global launch, DAU/MAU, IAP revenue, platform monetization, royalty/licensing and margin bridge are visible. Devsisters produced large MFE but later post-peak drawdown and share-count movement require lifecycle local 4B and validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE", "trigger_id": "TRG_R8L76-C27-206560-DEXTER-VFX-CONTENT-PRODUCTION-PIPELINE", "symbol": "206560", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"content_IP_score": 13, "global_distribution_score": 13, "paid_content_or_IAP_score": 10, "licensing_or_backlog_score": 12, "margin_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"content_IP_score": 15, "global_distribution_score": 15, "paid_content_or_IAP_score": 12, "licensing_or_backlog_score": 14, "margin_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["global_distribution_score", "paid_content_or_IAP_score", "licensing_or_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global launch/distribution, DAU/MAU/IAP, paid-content conversion, licensing/backlog and margin bridge; cap content/IP theme spikes when monetization evidence is absent or stale.", "MFE_90D_pct": 37.33, "MAE_90D_pct": -3.5, "score_return_alignment_label": "content_IP_positive_with_lifecycle_4b", "current_profile_verdict": "C27 should not only include idol/label/game names; VFX/content production pipelines can be C27 when order backlog, production schedule, global IP service revenue and margin bridge are visible. Dexter produced controlled-MAE follow-through, but needs non-price order/pipeline evidence before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE", "trigger_id": "TRG_R8L76-C27-207760-MRBLUE-WEBTOON-IP-THEME-SPIKE-FADE", "symbol": "207760", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"content_IP_score": 6, "global_distribution_score": 3, "paid_content_or_IAP_score": 3, "licensing_or_backlog_score": 2, "margin_bridge_score": 2, "relative_strength_score": 14, "execution_risk_score": 18, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"content_IP_score": 3, "global_distribution_score": 2, "paid_content_or_IAP_score": 1, "licensing_or_backlog_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 21, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 38, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["global_distribution_score", "paid_content_or_IAP_score", "licensing_or_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global launch/distribution, DAU/MAU/IAP, paid-content conversion, licensing/backlog and margin bridge; cap content/IP theme spikes when monetization evidence is absent or stale.", "MFE_90D_pct": 41.15, "MAE_90D_pct": -3.76, "score_return_alignment_label": "false_positive_content_IP_bridge_gap", "current_profile_verdict": "C27 should not treat webtoon/IP/platform theme spikes as durable Stage2 unless paid-content revenue, subscriber/traffic conversion, global distribution, licensing and margin bridge are visible. Mr. Blue produced large MFE but later collapsed into a high-MAE local 4B path; share-count movement requires validation."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 76, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_WEBTOON_VFX_CONTENT_IP_GLOBAL_MONETIZATION_BRIDGE_VS_THEME_SPIKE_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C27 content-IP symbols outside top-covered JYP/StudioDragon/HYBE/YG set, +3 game/webtoon/VFX trigger families, +2 content monetization positives, +1 webtoon theme-spike local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 76, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "axis": "game_webtoon_vfx_content_IP_global_monetization_bridge_vs_theme_spike_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C27 should split verified content-IP monetization rerating from content/theme beta. Stage2 requires global launch/distribution, DAU/MAU or paid-content conversion, licensing/royalty/order backlog and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["194480", "206560", "207760"], "share_count_validation_required": ["194480", "207760"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 76, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C27 needs monetization proof. Devsisters and Dexter show game/VFX content-IP positives after source repair; Mr. Blue shows webtoon/IP theme MFE fading into local 4B when paid-content, global distribution and margin bridge are absent."}
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
194480:
  corporate_action_candidate_dates = none
  selected window = 2024-02-23~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

206560:
  corporate_action_candidate_dates = 2016-12-21, 2017-01-09
  selected window = 2024-08-21~D+180
  contamination = false

207760:
  corporate_action_candidate_dates = 2015-11-23, 2022-12-19, 2023-01-10
  selected window = 2024-01-24~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C27 rows are source_proxy_only / evidence_url_pending.
194480 and 207760 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C27 rule-shape discovery,
but coding-agent promotion requires non-proxy DAU/MAU, paid-content, global launch/distribution, licensing/royalty, production backlog and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R8/C27 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and two rows need share-count validation.

Candidate axis:
game_webtoon_vfx_content_IP_global_monetization_bridge_vs_theme_spike_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 194480, 206560 and 207760.
4. Validate 194480 and 207760 share-count changes inside the selected window.
5. Keep generic C27 content-IP weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - content IP, game, webtoon or VFX/service exposure is explicit,
   - global launch, distribution, user traffic or production backlog is visible,
   - paid conversion, IAP, licensing, royalty or order revenue exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is content/IP theme beta only,
   - monetization or margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price DAU/revenue collapse, licensing/order loss, platform ranking failure, financing or margin break.
9. Emit before/after diagnostics and reject if verified content monetization positives are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 76
next_round = R9
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

