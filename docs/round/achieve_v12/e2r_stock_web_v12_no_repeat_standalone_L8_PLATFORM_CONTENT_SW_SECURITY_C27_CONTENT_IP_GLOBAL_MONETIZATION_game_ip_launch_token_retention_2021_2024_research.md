# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C27 — Game IP launch / token monetization retention guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_LAUNCH_TOKEN_RETENTION_REVENUE_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_game_ip_launch_token_retention_2021_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C27_CONTENT_IP_GLOBAL_MONETIZATION current coverage:
rows=51, symbols=19, date range=2016-03-24~2024-05-10, good/bad S2=16/3, 4B/4C=8/4
top covered symbols: 035900(7), 253450(5), 352820(5), 122870(4), 036420(3)
```

This run avoids those top-covered C27 symbols and adds 293490, 112040, and 225570.  
Each row uses a new `C27 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
293490 카카오게임즈: corporate_action_candidate_count=0.
112040 위메이드: 2022 event window uses clean tradable rows; 2021 corporate-action candidates are treated as outside this selected entry window.
225570 넥슨게임즈: 2024 forward window clean; corporate-action candidates are old or in 2022, outside the selected 2024 test window.
```

## 3. Research thesis

C27 should not treat every hit-IP or launch headline as durable monetization. It should test whether attention becomes repeatable revenue:

```text
content/game IP launch or monetization attention
→ early revenue-rank or distribution proof
→ retention and payer conversion
→ live-ops/content cadence
→ margin and revision bridge
→ rerating
```

The first download is applause. The second month is business. C27 should pay for the second month.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C27_293490_KAKAOGAMES_20210629_GAME_IP_LAUNCH_STAGE2_SUCCESS | 293490 | positive_game_ip_launch_stage2_success_with_later_4b | 2021-06-29 | 59700 | 116000 on 2021-11-17 | 57200 on 2021-07-01 | 77.55% | 94.3% | 94.3% | -4.19% | -44.91% |
| C27_112040_WEMADE_20220103_P2E_TOKEN_IP_PREMIUM_4B_COUNTEREXAMPLE | 112040 | token_ip_monetization_blowoff_counterexample | 2022-01-03 | 183900 | 188100 on 2022-01-03 | 45600 on 2022-09-28 | 2.28% | 2.28% | 2.28% | -75.2% | -75.76% |
| C27_225570_NEXONGAMES_20240703_GLOBAL_LAUNCH_PREMIUM_FALSE_GREEN | 225570 | global_game_launch_retention_false_green_counterexample | 2024-07-03 | 17900 | 30200 on 2024-08-01 | 12870 on 2024-11-15 | 68.72% | 68.72% | 68.72% | -28.1% | -57.38% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Game-IP launch traction and early revenue-rank evidence can be a valid Stage2 route.
- 293490 is the positive anchor: launch traction produced a large MFE with low initial MAE, but the later peak still demanded 4B discipline.

### Stage3 / Green
- C27 Green should require retention, payer conversion, live-ops cadence, margin and revision evidence.
- A launch spike without retention proof is not enough. A game can top the chart and still fail to become a durable annuity.

### 4B
- 112040 and 225570 are the local 4B/counterexample guards. Price capitalized the token/IP or global launch story before the retention/revenue bridge was durable.
- Full 4B should require non-price evidence such as payer-decay, regulatory/platform friction, revenue-rank fade, or revision deceleration.

### 4C
- No hard accounting break is asserted.
- The C27 break mode is monetization durability failure: users arrive, but retention, payer conversion, live-ops cadence, token/platform durability or revisions do not carry the valuation.

## 6. Raw component score breakdown

```json
{
  "C27_112040_WEMADE_20220103_P2E_TOKEN_IP_PREMIUM_4B_COUNTEREXAMPLE": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 24,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4
  },
  "C27_225570_NEXONGAMES_20240703_GLOBAL_LAUNCH_PREMIUM_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 32,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  },
  "C27_293490_KAKAOGAMES_20210629_GAME_IP_LAUNCH_STAGE2_SUCCESS": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 58,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C27 guard:
```text
if game_ip_launch_attention and early_revenue_rank_visible:
    allow_stage2_actionable = true

if launch_or_token_price_premium and no retention_payer_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and retention_or_monetization_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 112040 / 2022-01-03: P2E/token-linked IP premium can be over-promoted if token economy, regulatory durability and cash conversion are not required.
- 225570 / 2024-07-03: global launch attention can look like Green, but the later drawdown argues for Yellow/local 4B unless retention and payer conversion hold.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -4.19, "MAE_30D_pct": -4.19, "MAE_90D_pct": -4.19, "MFE_180D_pct": 94.3, "MFE_30D_pct": 77.55, "MFE_90D_pct": 94.3, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_293490_KAKAOGAMES_20210629_GAME_IP_LAUNCH_STAGE2_SUCCESS", "case_role": "positive_game_ip_launch_stage2_success_with_later_4b", "company_name": "카카오게임즈", "corporate_action_window_status": "clean_forward_window_or_event_specific_caveat_noted", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when game-IP launch traction and revenue-rank evidence appeared, but Green still requires retention, payer conversion, live-ops cadence and revision durability.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.91, "entry_date": "2021-06-29", "entry_price": 59700, "evidence_family": "game_ip_launch_initial_revenue_rank_global_monetization_route", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_TOKEN_RETENTION_REVENUE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2021-07-01", "low_price_180d": 57200, "peak_date": "2021-11-17", "peak_price": 116000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/293/293490.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 11, "total": 58, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C27_293490_KAKAOGAMES_20210629_GAME_IP_LAUNCH_STAGE2_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_ip_attention", "launch_revenue_rank_or_global_distribution_signal", "early_monetization_or_relative_strength"], "stage3_evidence_fields": ["retention_and_payer_conversion_required", "live_ops_content_cadence_required", "revenue_or_margin_revision_bridge_required"], "stage4b_evidence_fields": ["launch_or_token_ip_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["retention_or_payer_fade", "token_regulatory_or_platform_monetization_break", "revision_bridge_failure_after_launch"], "symbol": "293490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv", "trigger_date": "2021-06-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -75.2, "MAE_30D_pct": -47.91, "MAE_90D_pct": -64.65, "MFE_180D_pct": 2.28, "MFE_30D_pct": 2.28, "MFE_90D_pct": 2.28, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_112040_WEMADE_20220103_P2E_TOKEN_IP_PREMIUM_4B_COUNTEREXAMPLE", "case_role": "token_ip_monetization_blowoff_counterexample", "company_name": "위메이드", "corporate_action_window_status": "clean_forward_window_or_event_specific_caveat_noted", "current_profile_error": true, "current_profile_verdict": "P2E/token-linked game-IP premium should route to local 4B or counterexample unless retention, regulatory durability, token-economy cash conversion and accounting/revision bridge close.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -75.76, "entry_date": "2022-01-03", "entry_price": 183900, "evidence_family": "p2e_token_game_ip_price_premium_without_retention_regulatory_cashflow_bridge", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_TOKEN_RETENTION_REVENUE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-09-28", "low_price_180d": 45600, "peak_date": "2022-01-03", "peak_price": 188100, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/112/112040.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 24, "valuation_rerating_runway": 1, "visibility_quality": 4}, "reuse_reason": null, "same_entry_group_id": "C27_112040_WEMADE_20220103_P2E_TOKEN_IP_PREMIUM_4B_COUNTEREXAMPLE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_ip_attention", "launch_revenue_rank_or_global_distribution_signal", "early_monetization_or_relative_strength"], "stage3_evidence_fields": ["retention_and_payer_conversion_required", "live_ops_content_cadence_required", "revenue_or_margin_revision_bridge_required"], "stage4b_evidence_fields": ["launch_or_token_ip_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["retention_or_payer_fade", "token_regulatory_or_platform_monetization_break", "revision_bridge_failure_after_launch"], "symbol": "112040", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv", "trigger_date": "2022-01-03", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -28.1, "MAE_30D_pct": -7.88, "MAE_90D_pct": -27.26, "MFE_180D_pct": 68.72, "MFE_30D_pct": 68.72, "MFE_90D_pct": 68.72, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_225570_NEXONGAMES_20240703_GLOBAL_LAUNCH_PREMIUM_FALSE_GREEN", "case_role": "global_game_launch_retention_false_green_counterexample", "company_name": "넥슨게임즈", "corporate_action_window_status": "clean_forward_window_or_event_specific_caveat_noted", "current_profile_error": true, "current_profile_verdict": "Global launch price premium should stay Yellow/local 4B unless retention, payer conversion, content update cadence and revenue revision evidence remain visible after launch week.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -57.38, "entry_date": "2024-07-03", "entry_price": 17900, "evidence_family": "global_game_launch_price_premium_without_retention_payer_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_TOKEN_RETENTION_REVENUE_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2024-11-15", "low_price_180d": 12870, "peak_date": "2024-08-01", "peak_price": 30200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/225/225570.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 32, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C27_225570_NEXONGAMES_20240703_GLOBAL_LAUNCH_PREMIUM_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_ip_attention", "launch_revenue_rank_or_global_distribution_signal", "early_monetization_or_relative_strength"], "stage3_evidence_fields": ["retention_and_payer_conversion_required", "live_ops_content_cadence_required", "revenue_or_margin_revision_bridge_required"], "stage4b_evidence_fields": ["launch_or_token_ip_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["retention_or_payer_fade", "token_regulatory_or_platform_monetization_break", "revision_bridge_failure_after_launch"], "symbol": "225570", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv", "trigger_date": "2024-07-03", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "GAME_IP_LAUNCH_TOKEN_RETENTION_REVENUE_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "game_ip_global_monetization_retention_counterexample_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C27 content/game-IP monetization rows should allow Stage2 on early launch/revenue-rank traction, but Stage3 Green requires retention, payer conversion, live-ops cadence, platform/regulatory durability, margin and revision bridge; launch/token price premium without retention proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C27 + symbol + trigger_type + entry_date.
3. Add C27-specific launch/retention/payer-conversion/live-ops/revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C27_STAGE2_ALLOWED_ON_EARLY_LAUNCH_REVENUE_RANK_TRACTION
- C27_GREEN_REQUIRES_RETENTION_PAYER_LIVEOPS_MARGIN_REVISION
- C27_TOKEN_IP_PREMIUM_LOCAL_4B
- C27_GLOBAL_LAUNCH_WITHOUT_RETENTION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

