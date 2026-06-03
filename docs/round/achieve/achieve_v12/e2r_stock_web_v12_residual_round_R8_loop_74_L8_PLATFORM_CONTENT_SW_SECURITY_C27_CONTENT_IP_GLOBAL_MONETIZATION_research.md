# E2R Stock-Web v12 Residual Research — R8 Loop 74 / L8 / C27

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 74,
  "computed_next_round": "R9",
  "computed_next_loop": 74,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "content_ip_lifecycle_decay_test"
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

Previous completed state in this interactive run: R7 / loop 74.

Therefore:

```text
scheduled_round = R8
scheduled_loop = 74
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
computed_next_round = R9
computed_next_loop = 74
```

R8 was routed to C27 because loop 73 used C26 and this run needs a content/IP monetization holdout rather than another platform/ad-revenue pass.

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
259960 / 크래프톤 / PUBG-BGMI global live-ops monetization
225570 / 넥슨게임즈 / global launch retention lifecycle
263750 / 펄어비스 / AAA trailer anticipation beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
259960 and 225570 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C27 is not “content/game stock went up.”

The mechanism is:

```text
content IP or game launch
→ global distribution / live-ops / retention
→ paying-user or ARPU conversion
→ revenue and margin bridge
→ durable rerating
```

A trailer is a poster on the theater wall.  
Monetization is the ticket counter staying busy after opening weekend.

---

## Case 1 — Positive anchor: 259960 / 크래프톤

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is PUBG/BGMI global live-ops, MAU/ARPU, regional monetization and margin bridge evidence.

```text
evidence_family = PUBG_BGMI_GLOBAL_LIVEOPS_MONETIZATION_MOBILE_PC_MARGIN_BRIDGE
case_role = positive_anchor_with_controlled_mae
trigger_date = 2024-02-08
entry_date = 2024-02-13
entry_price = 219,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv`:

```text
2024-02-13,219500,230000,219000,230000
2024-03-27,250000,265000,248000,257000
2024-08-22,346500,355000,337000,346000
2024-11-15,293500,296500,281000,289500
```

### Backtest

```text
MFE_30D  = +20.73%
MAE_30D  = -0.91%
MFE_90D  = +37.59%
MAE_90D  = -0.91%
MFE_180D = +61.73%
MAE_180D = -0.91%
peak_180 = 355,000 on 2024-08-22
trough_180 = 217,500 on 2024-02-26
peak_to_later_drawdown = -20.85%
```

### Interpretation

This is the C27 positive anchor.  
The path is not just headline heat: large MFE, controlled MAE, and durable rerating.

But even this row is marked source-repair because runtime promotion needs non-proxy monetization and margin evidence, plus share-count validation.

---

## Case 2 — Launch positive with lifecycle 4B: 225570 / 넥슨게임즈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is global launch traction, retention, payer conversion, live-ops cadence and monetization evidence.

```text
evidence_family = GLOBAL_GAME_LAUNCH_STEAM_CONSOLE_TRACTION_RETENTION_MONETIZATION_BRIDGE
case_role = positive_with_later_4b_watch_and_sharecount_validation
trigger_date = 2024-07-02
entry_date = 2024-07-03
entry_price = 18,610
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv`:

```text
2024-07-03,18610,18950,16490,17900
2024-08-01,24050,30200,23900,28800
2024-08-09,28000,30950,27550,28850
2024-12-09,13050,13290,12560,12560
```

### Backtest

```text
MFE_30D  = +66.58%
MAE_30D  = -11.39%
MFE_90D  = +66.58%
MAE_90D  = -19.67%
MFE_180D = +66.58%
MAE_180D = -32.51%
peak_180 = 31,000 on 2024-08-09
trough_180 = 12,560 on 2024-12-09
peak_to_later_drawdown = -59.48%
```

### Interpretation

This is the launch lifecycle row.  
The launch-window MFE was real, but the post-peak collapse says C27 must require retention and monetization evidence.

Correct treatment:

```text
launch/retention bridge verified → Stage2 possible
retention/monetization bridge stale → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 263750 / 펄어비스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests AAA trailer/release anticipation beta without release-date, preorder/wishlist conversion, monetization or revenue bridge.

```text
evidence_family = AAA_GAME_TRAILER_ANTICIPATION_BETA_WITH_WEAK_RELEASE_REVENUE_BRIDGE
case_role = counterexample
trigger_date = 2024-07-08
entry_date = 2024-07-09
entry_price = 44,850
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv`:

```text
2024-07-09,44850,47000,44850,46200
2024-07-10,46200,47650,45650,47600
2024-08-05,40550,40700,36550,37750
2024-12-30,27250,27800,27000,27700
```

### Backtest

```text
MFE_30D  = +6.24%
MAE_30D  = -15.83%
MFE_90D  = +6.24%
MAE_90D  = -25.08%
MFE_180D = +6.24%
MAE_180D = -39.80%
peak_180 = 47,650 on 2024-07-10
trough_180 = 27,000 on 2024-12-30
peak_to_later_drawdown = -43.34%
```

### Interpretation

This is the C27 false-positive row.  
Trailer anticipation alone did not become durable monetization. Without release/revenue bridge, this should be local 4B-watch, not Green.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C27_content_ip_weight = true
do_not_treat_all_trailer_or_launch_MFE_as_Green = true
do_not_convert_content_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE
```

This fine archetype covers:

```text
1. global live-ops monetization anchor → Stage2/Green possible after source repair
2. global launch lifecycle → Stage2 possible only if retention/monetization persists
3. trailer/release anticipation beta → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GlobalGameIPMonetizationBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should allow Stage2 when global game IP monetization is tied to live-ops, regional monetization, MAU/ARPU and margin bridge. Krafton produced a large, low-MAE rerating path; this is a positive anchor that should not be overblocked by generic content-beta guards.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy launch retention, MAU/ARPU, live-ops, monetization and revenue bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE", "symbol": "225570", "company_name": "넥슨게임즈", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GlobalLaunchRetentionBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should allow a global launch name only if launch traction converts into retention, paying-user monetization, live-ops cadence and revenue bridge. Nexon Games produced a huge launch-window MFE, but later drawdown makes lifecycle local 4B mandatory unless retention/monetization evidence refreshes.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy launch retention, MAU/ARPU, live-ops, monetization and revenue bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE", "symbol": "263750", "company_name": "펄어비스", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "case_type": "content_ip_global_monetization", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / TrailerAnticipationBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C27 should not treat trailer/release-expectation beta as durable Stage2 unless release date, preorder/wishlist conversion, monetization model and revenue timing are visible. Pearl Abyss had limited MFE and then large MAE, so this is a false Stage2/local 4B row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy launch retention, MAU/ARPU, live-ops, monetization and revenue bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION", "case_id": "R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION", "symbol": "259960", "company_name": "크래프톤", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_ip_lifecycle_decay_test", "trigger_type": "Stage2-Actionable-GlobalGameIPMonetizationBridge", "trigger_date": "2024-02-08", "entry_date": "2024-02-13", "entry_price": 219500.0, "evidence_available_at_that_date": "PUBG_BGMI_GLOBAL_LIVEOPS_MONETIZATION_MOBILE_PC_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KRAFTON_2024_PUBG_BGMI_GLOBAL_LIVEOPS_MONETIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["content_ip", "global_launch_or_liveops_candidate", "monetization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "retention_revenue_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv", "profile_path": "atlas/symbol_profiles/259/259960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.73, "MFE_90D_pct": 37.59, "MFE_180D_pct": 61.73, "MAE_30D_pct": -0.91, "MAE_90D_pct": -0.91, "MAE_180D_pct": -0.91, "peak_date": "2024-08-22", "peak_price": 355000.0, "drawdown_after_peak_pct": -20.85, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_content_ip_or_launch_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_retention_revenue_or_release_break", "trigger_outcome_label": "positive_anchor_with_controlled_mae", "current_profile_verdict": "C27 should allow Stage2 when global game IP monetization is tied to live-ops, regional monetization, MAU/ARPU and margin bridge. Krafton produced a large, low-MAE rerating path; this is a positive anchor that should not be overblocked by generic content-beta guards.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C27_CONTENT_IP_259960_2024-02-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE", "case_id": "R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE", "symbol": "225570", "company_name": "넥슨게임즈", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_ip_lifecycle_decay_test", "trigger_type": "Stage2-Actionable-GlobalLaunchRetentionBridgeWithLifecycle4B", "trigger_date": "2024-07-02", "entry_date": "2024-07-03", "entry_price": 18610.0, "evidence_available_at_that_date": "GLOBAL_GAME_LAUNCH_STEAM_CONSOLE_TRACTION_RETENTION_MONETIZATION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NEXON_GAMES_2024_GLOBAL_GAME_LAUNCH_RETENTION_MONETIZATION_BRIDGE", "stage2_evidence_fields": ["content_ip", "global_launch_or_liveops_candidate", "monetization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "retention_revenue_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv", "profile_path": "atlas/symbol_profiles/225/225570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 66.58, "MFE_90D_pct": 66.58, "MFE_180D_pct": 66.58, "MAE_30D_pct": -11.39, "MAE_90D_pct": -19.67, "MAE_180D_pct": -32.51, "peak_date": "2024-08-09", "peak_price": 31000.0, "drawdown_after_peak_pct": -59.48, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_content_ip_or_launch_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_retention_revenue_or_release_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "current_profile_verdict": "C27 should allow a global launch name only if launch traction converts into retention, paying-user monetization, live-ops cadence and revenue bridge. Nexon Games produced a huge launch-window MFE, but later drawdown makes lifecycle local 4B mandatory unless retention/monetization evidence refreshes.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C27_CONTENT_IP_225570_2024-07-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE", "case_id": "R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE", "symbol": "263750", "company_name": "펄어비스", "round": "R8", "loop": "74", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_ip_lifecycle_decay_test", "trigger_type": "Stage2-FalsePositive / TrailerAnticipationBetaFade", "trigger_date": "2024-07-08", "entry_date": "2024-07-09", "entry_price": 44850.0, "evidence_available_at_that_date": "AAA_GAME_TRAILER_ANTICIPATION_BETA_WITH_WEAK_RELEASE_REVENUE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PEARL_ABYSS_2024_AAA_GAME_TRAILER_RELEASE_REVENUE_BRIDGE", "stage2_evidence_fields": ["content_ip", "global_launch_or_liveops_candidate", "monetization_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "retention_revenue_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv", "profile_path": "atlas/symbol_profiles/263/263750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.24, "MFE_90D_pct": 6.24, "MFE_180D_pct": 6.24, "MAE_30D_pct": -15.83, "MAE_90D_pct": -25.08, "MAE_180D_pct": -39.8, "peak_date": "2024-07-10", "peak_price": 47650.0, "drawdown_after_peak_pct": -43.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_content_ip_or_launch_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_retention_revenue_or_release_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C27 should not treat trailer/release-expectation beta as durable Stage2 unless release date, preorder/wishlist conversion, monetization model and revenue timing are visible. Pearl Abyss had limited MFE and then large MAE, so this is a false Stage2/local 4B row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C27_CONTENT_IP_263750_2024-07-09", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION", "trigger_id": "TRG_R8L74-C27-259960-KRAFTON-PUBG-GLOBAL-MONETIZATION", "symbol": "259960", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"ip_quality_score": 15, "global_distribution_score": 14, "retention_or_liveops_score": 13, "monetization_revenue_score": 14, "margin_bridge_score": 12, "relative_strength_score": 14, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 5, "source_confidence_score": 2}, "weighted_score_before": 86, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"ip_quality_score": 16, "global_distribution_score": 15, "retention_or_liveops_score": 15, "monetization_revenue_score": 16, "margin_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 90, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["retention_or_liveops_score", "monetization_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global launch retention, live-ops, monetization and revenue/margin bridge; cap trailer or anticipation beta without release/revenue conversion.", "MFE_90D_pct": 37.59, "MAE_90D_pct": -0.91, "score_return_alignment_label": "aligned_positive_anchor", "current_profile_verdict": "C27 should allow Stage2 when global game IP monetization is tied to live-ops, regional monetization, MAU/ARPU and margin bridge. Krafton produced a large, low-MAE rerating path; this is a positive anchor that should not be overblocked by generic content-beta guards."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE", "trigger_id": "TRG_R8L74-C27-225570-NEXONGAMES-GLOBAL-LAUNCH-RETENTION-LIFECYCLE", "symbol": "225570", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"ip_quality_score": 15, "global_distribution_score": 14, "retention_or_liveops_score": 13, "monetization_revenue_score": 8, "margin_bridge_score": 7, "relative_strength_score": 14, "execution_risk_score": 16, "dilution_or_sharecount_risk_score": 5, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"ip_quality_score": 16, "global_distribution_score": 15, "retention_or_liveops_score": 15, "monetization_revenue_score": 9, "margin_bridge_score": 8, "relative_strength_score": 13, "execution_risk_score": 18, "dilution_or_sharecount_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2 candidate after source repair + lifecycle local 4B", "changed_components": ["retention_or_liveops_score", "monetization_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global launch retention, live-ops, monetization and revenue/margin bridge; cap trailer or anticipation beta without release/revenue conversion.", "MFE_90D_pct": 66.58, "MAE_90D_pct": -19.67, "score_return_alignment_label": "launch_positive_with_lifecycle_4b", "current_profile_verdict": "C27 should allow a global launch name only if launch traction converts into retention, paying-user monetization, live-ops cadence and revenue bridge. Nexon Games produced a huge launch-window MFE, but later drawdown makes lifecycle local 4B mandatory unless retention/monetization evidence refreshes."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE", "trigger_id": "TRG_R8L74-C27-263750-PEARLABYSS-TRAILER-ANTICIPATION-BETA-FADE", "symbol": "263750", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"ip_quality_score": 8, "global_distribution_score": 5, "retention_or_liveops_score": 2, "monetization_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 16, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"ip_quality_score": 6, "global_distribution_score": 3, "retention_or_liveops_score": 1, "monetization_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 18, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_after": 41, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["retention_or_liveops_score", "monetization_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global launch retention, live-ops, monetization and revenue/margin bridge; cap trailer or anticipation beta without release/revenue conversion.", "MFE_90D_pct": 6.24, "MAE_90D_pct": -25.08, "score_return_alignment_label": "false_positive_trailer_beta_bridge_gap", "current_profile_verdict": "C27 should not treat trailer/release-expectation beta as durable Stage2 unless release date, preorder/wishlist conversion, monetization model and revenue timing are visible. Pearl Abyss had limited MFE and then large MAE, so this is a false Stage2/local 4B row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R8", "loop": 74, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GLOBAL_GAME_IP_MONETIZATION_AND_LAUNCH_RETENTION_VS_TRAILER_OR_CONTENT_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C27 game/content IP symbols outside top-covered entertainment set, +3 liveops/launch/trailer trigger families, +1 low-MAE global IP monetization anchor, +1 launch lifecycle positive, +1 trailer-beta fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R8", "loop": 74, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "axis": "global_game_ip_monetization_and_launch_retention_vs_trailer_or_content_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C27 should split verified global game IP monetization/live-ops retention from trailer or launch-beta price spikes. Stage2 requires MAU/ARPU, retention, paying-user conversion, live-ops cadence, global distribution or revenue/margin bridge. If launch MFE fades and MAE/post-peak drawdown opens without retention evidence, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["259960", "225570", "263750"], "share_count_validation_required": ["259960", "225570"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": 74, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C27 needs monetization proof. Krafton is a low-MAE global IP monetization anchor; Nexon Games is a launch lifecycle positive requiring retention evidence; Pearl Abyss is trailer/anticipation beta fading into local 4B when release/revenue bridge is absent."}
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
  corporate_action_candidate_dates = none
  selected window = 2024-02-13~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

225570:
  corporate_action_candidate_dates = 2017-06-12, 2018-05-09, 2022-04-15
  selected window = 2024-07-03~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

263750:
  corporate_action_candidate_dates = 2021-04-16
  selected window = 2024-07-09~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C27 rows are source_proxy_only / evidence_url_pending.
259960 and 225570 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C27 rule-shape discovery,
but coding-agent promotion requires non-proxy launch, retention, MAU/ARPU, live-ops, monetization and revenue/margin evidence.
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
global_game_ip_monetization_and_launch_retention_vs_trailer_or_content_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 259960, 225570 and 263750.
4. Validate 259960 and 225570 share-count changes inside the selected window.
5. Keep generic C27 content/IP weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - global launch, IP monetization or live-ops evidence is explicit,
   - MAU/ARPU, retention, payer conversion or regional monetization is visible,
   - revenue/margin bridge exists,
   - MAE remains controlled or the signal is explicitly treated as lifecycle Stage2.
7. Consider local 4B-watch when:
   - the trigger is trailer/release/launch headline beta only,
   - retention or monetization bridge is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price retention collapse, launch failure, revenue miss, delay, cancellation or margin break.
9. Emit before/after diagnostics and reject if verified global IP monetization positives are overblocked.
```

---

## Final round state

```text
completed_round = R8
completed_loop = 74
next_round = R9
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

