# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C27 — Content IP global monetization / game launch 4B guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_LAUNCH_GLOBAL_MONETIZATION_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_game_ip_launch_premium_2021_research.md
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

This run avoids those top-covered C27 symbols and adds 194480, 293490, and 263750.  
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
194480 데브시스터즈: corporate_action_candidate_count=0.
293490 카카오게임즈: corporate_action_candidate_count=0.
263750 펄어비스: selected window is after the 2021-04-16 corporate-action candidate and does not cross a new blocked candidate inside the test window.
```

## 3. Research thesis

C27 should not treat IP attention itself as monetization. It should test whether the IP converts into durable global revenue and margin:

```text
content / game IP launch attention
→ global revenue rank and regional distribution
→ retention and live-ops cadence
→ user acquisition efficiency and platform fee economics
→ gross margin and revision bridge
→ rerating or local 4B cap
```

An IP trailer is a spark. Green should require the fire: repeat revenue rank, retained users, live-ops cadence, and a margin revision that keeps burning after the launch week.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_STAGE2 | 194480 | positive_cookie_run_kingdom_global_ip_stage2_success_with_later_4b | 2021-01-21 | 17250 | 199500 on 2021-09-27 | 15050 on 2021-01-21 | 300.0% | 833.33% | 1056.52% | -12.75% | -27.07% |
| C27_293490_KAKAOGAMES_20211117_ODIN_IP_PREMIUM_4B | 293490 | game_ip_success_price_premium_counterexample | 2021-11-17 | 107900 | 116000 on 2021-11-17 | 46100 on 2022-06-23 | 7.51% | 7.51% | 7.51% | -57.28% | -60.26% |
| C27_263750_PEARLABYSS_20211117_PIPELINE_IP_PREMIUM_4B | 263750 | pipeline_game_ip_price_premium_counterexample | 2021-11-17 | 141000 | 145200 on 2021-11-17 | 47700 on 2022-07-04 | 2.98% | 2.98% | 2.98% | -66.17% | -67.15% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Game/content IP can be a valid Stage2 route when the launch is backed by revenue rank, global distribution, retention, live-ops monetization and margin revision evidence.
- 194480 is the positive anchor. The January 2021 Cookie Run Kingdom route produced extreme MFE because the IP launch converted into real monetization evidence rather than remaining a trailer/theme.

### Stage3 / Green
- C27 Green should require repeat global revenue rank, regional expansion, retention, UA efficiency, live-ops cadence, platform fee economics, gross margin and revision confirmation.
- A successful launch can move from Stage2 to 4B quickly once the price has already capitalized several quarters of live-ops execution.

### 4B
- 293490 is the post-success premium counterexample. Odin success was real, but the November 2021 price had already paid for much of the domestic IP outcome. Without fresh global expansion, retention and margin/revision evidence, the row becomes local 4B.
- 263750 is the pipeline-IP premium counterexample. Trailer and pipeline excitement can be powerful, but without release timing, launch conversion and revenue rank proof, it should not be Green.
- 194480 also required later 4B discipline after the Stage2 success became fully capitalized.

### 4C
- No hard game shutdown, regulatory block or accounting break is asserted.
- The C27 break mode is monetization exhaustion: the IP remains real, but revenue rank, retention, live-ops, UA efficiency, margin and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_STAGE2": {
    "global_distribution_visibility": 11,
    "information_confidence": 4,
    "ip_launch_monetization": 12,
    "margin_revision_bridge": 9,
    "market_mispricing": 12,
    "retention_liveops_quality": 10,
    "total": 68,
    "valuation_rerating_runway": 10
  },
  "C27_263750_PEARLABYSS_20211117_PIPELINE_IP_PREMIUM_4B": {
    "global_distribution_visibility": 5,
    "information_confidence": 3,
    "ip_launch_monetization": 4,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "retention_liveops_quality": 3,
    "total": 23,
    "valuation_rerating_runway": 1
  },
  "C27_293490_KAKAOGAMES_20211117_ODIN_IP_PREMIUM_4B": {
    "global_distribution_visibility": 5,
    "information_confidence": 3,
    "ip_launch_monetization": 7,
    "margin_revision_bridge": 4,
    "market_mispricing": 4,
    "retention_liveops_quality": 5,
    "total": 29,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C27 guard:
```text
if content_ip_launch and global_revenue_rank_retention_liveops_margin_bridge_visible:
    allow_stage2_actionable = true

if content_ip_price_premium and no incremental_revenue_rank_retention_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if pipeline_ip_premium and no release_to_revenue_conversion_evidence:
    route_to_counterexample_or_4B_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 293490 / 2021-11-17: successful game IP can be over-promoted if the model treats price premium as fresh global monetization and retention proof.
- 263750 / 2021-11-17: pipeline IP excitement can become price-only when release timing, launch conversion, revenue rank and margin evidence are absent.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.75, "MAE_30D_pct": -12.75, "MAE_90D_pct": -12.75, "MFE_180D_pct": 1056.52, "MFE_30D_pct": 300.0, "MFE_90D_pct": 833.33, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_STAGE2", "case_role": "positive_cookie_run_kingdom_global_ip_stage2_success_with_later_4b", "company_name": "데브시스터즈", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2021_forward_window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when a new game IP launch created visible global revenue-rank, user-retention and live-ops monetization evidence before the rerating was fully capitalized. Green still requires repeat revenue rank, regional expansion, retention, live-ops cadence, UA efficiency, margin and revision bridge; after the September 2021 premium, the same evidence required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -27.07, "entry_date": "2021-01-21", "entry_price": 17250, "evidence_family": "game_ip_launch_global_revenue_rank_user_retention_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_GLOBAL_MONETIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2021-01-21", "low_price_180d": 15050, "peak_date": "2021-09-27", "peak_price": 199500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/194/194480.json", "raw_component_score_breakdown": {"global_distribution_visibility": 11, "information_confidence": 4, "ip_launch_monetization": 12, "margin_revision_bridge": 9, "market_mispricing": 12, "retention_liveops_quality": 10, "total": 68, "valuation_rerating_runway": 10}, "reuse_reason": null, "same_entry_group_id": "C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_ip_launch_attention", "global_revenue_rank_or_distribution_visibility", "retention_liveops_margin_revision_route"], "stage3_evidence_fields": ["repeat_global_revenue_rank_required", "regional_expansion_retention_liveops_required", "UA_efficiency_margin_revision_bridge_required"], "stage4b_evidence_fields": ["content_ip_price_premium", "pipeline_or_launch_success_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["launch_to_revenue_conversion_gap", "retention_or_liveops_disappointment", "margin_revision_bridge_failure"], "symbol": "194480", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv", "trigger_date": "2021-01-21", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -57.28, "MAE_30D_pct": -20.48, "MAE_90D_pct": -40.78, "MFE_180D_pct": 7.51, "MFE_30D_pct": 7.51, "MFE_90D_pct": 7.51, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_293490_KAKAOGAMES_20211117_ODIN_IP_PREMIUM_4B", "case_role": "game_ip_success_price_premium_counterexample", "company_name": "카카오게임즈", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2021_2022_forward_window", "current_profile_error": true, "current_profile_verdict": "A successful domestic game IP should route to local 4B when the stock has already capitalized launch success and fresh global revenue, retention, live-ops, margin and revision evidence do not keep expanding after the peak.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.26, "entry_date": "2021-11-17", "entry_price": 107900, "evidence_family": "odin_game_ip_price_premium_without_incremental_global_revenue_retention_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_GLOBAL_MONETIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-06-23", "low_price_180d": 46100, "peak_date": "2021-11-17", "peak_price": 116000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/293/293490.json", "raw_component_score_breakdown": {"global_distribution_visibility": 5, "information_confidence": 3, "ip_launch_monetization": 7, "margin_revision_bridge": 4, "market_mispricing": 4, "retention_liveops_quality": 5, "total": 29, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C27_293490_KAKAOGAMES_20211117_ODIN_IP_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_ip_launch_attention", "global_revenue_rank_or_distribution_visibility", "retention_liveops_margin_revision_route"], "stage3_evidence_fields": ["repeat_global_revenue_rank_required", "regional_expansion_retention_liveops_required", "UA_efficiency_margin_revision_bridge_required"], "stage4b_evidence_fields": ["content_ip_price_premium", "pipeline_or_launch_success_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["launch_to_revenue_conversion_gap", "retention_or_liveops_disappointment", "margin_revision_bridge_failure"], "symbol": "293490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv", "trigger_date": "2021-11-17", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -66.17, "MAE_30D_pct": -19.08, "MAE_90D_pct": -35.67, "MFE_180D_pct": 2.98, "MFE_30D_pct": 2.98, "MFE_90D_pct": 2.98, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_263750_PEARLABYSS_20211117_PIPELINE_IP_PREMIUM_4B", "case_role": "pipeline_game_ip_price_premium_counterexample", "company_name": "펄어비스", "corporate_action_window_status": "selected window after 2021-04-16 corporate-action candidate; clean_2021_2022_forward_window", "current_profile_error": true, "current_profile_verdict": "Pipeline IP excitement should route to local 4B or counterexample unless release timing, launch conversion, revenue rank, retention, live-ops monetization, margin and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.15, "entry_date": "2021-11-17", "entry_price": 141000, "evidence_family": "pipeline_game_ip_trailer_price_premium_without_release_revenue_retention_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_GLOBAL_MONETIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-07-04", "low_price_180d": 47700, "peak_date": "2021-11-17", "peak_price": 145200, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/263/263750.json", "raw_component_score_breakdown": {"global_distribution_visibility": 5, "information_confidence": 3, "ip_launch_monetization": 4, "margin_revision_bridge": 3, "market_mispricing": 4, "retention_liveops_quality": 3, "total": 23, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C27_263750_PEARLABYSS_20211117_PIPELINE_IP_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_ip_launch_attention", "global_revenue_rank_or_distribution_visibility", "retention_liveops_margin_revision_route"], "stage3_evidence_fields": ["repeat_global_revenue_rank_required", "regional_expansion_retention_liveops_required", "UA_efficiency_margin_revision_bridge_required"], "stage4b_evidence_fields": ["content_ip_price_premium", "pipeline_or_launch_success_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["launch_to_revenue_conversion_gap", "retention_or_liveops_disappointment", "margin_revision_bridge_failure"], "symbol": "263750", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv", "trigger_date": "2021-11-17", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "GAME_IP_LAUNCH_GLOBAL_MONETIZATION_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "content_ip_game_launch_global_monetization_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C27 content/IP rows should allow Stage2 when a new IP launch is backed by global revenue rank, retention, live-ops monetization and margin/revision bridge, but Stage3 Green requires repeat revenue rank, regional expansion, retention, UA efficiency, live-ops cadence and revision confirmation; content-IP price premium without fresh monetization evidence should route to local 4B or counterexample.",
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
3. Add C27-specific content/game IP launch / global revenue rank / retention / live-ops / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C27_STAGE2_ALLOWED_ON_REVENUE_RANK_RETENTION_LIVEOPS_MARGIN_BRIDGE
- C27_GREEN_REQUIRES_REPEAT_REVENUE_RANK_REGIONAL_EXPANSION_UA_EFFICIENCY_REVISION
- C27_CONTENT_IP_PRICE_PREMIUM_LOCAL_4B
- C27_PIPELINE_IP_WITHOUT_RELEASE_REVENUE_CONVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

