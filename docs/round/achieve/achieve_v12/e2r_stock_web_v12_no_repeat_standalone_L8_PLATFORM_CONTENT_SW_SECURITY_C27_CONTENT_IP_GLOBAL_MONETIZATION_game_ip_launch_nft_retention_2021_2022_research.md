# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C27 — Content IP global monetization / game launch retention guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_LAUNCH_NFT_RETENTION_MONETIZATION_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_game_ip_launch_nft_retention_2021_2022_research.md
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

This run avoids those top-covered C27 symbols and adds 293490, 112040, and 259960.  
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
112040 위메이드: selected test window begins after 2021-09-13 and 2021-10-06 corporate-action candidates; post-event rows are used with caveat.
259960 크래프톤: corporate_action_candidate_count=0.
```

## 3. Research thesis

C27 should not treat every launch, download rank, NFT platform, or global IP headline as durable monetization. It should test whether attention becomes paying users and revisions:

```text
content/game IP attention
→ launch or revenue-rank proof
→ retention cohort and live-ops cadence
→ global monetization quality
→ margin and cash-flow bridge
→ revision-backed rerating
```

The launch is the opening night. Green should pay for repeat attendance, not only the queue outside the theater.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C27_293490_KAKAOGAMES_20210629_ODIN_GLOBAL_IP_MONETIZATION_STAGE2 | 293490 | positive_game_ip_launch_monetization_stage2_success_with_later_4b | 2021-06-29 | 56000 | 116000 on 2021-11-17 | 55600 on 2021-06-29 | 89.29% | 89.29% | 107.14% | -0.71% | -26.03% |
| C27_112040_WEMADE_20211122_NFT_WEMIX_IP_PRICE_PREMIUM_4B | 112040 | nft_tokenized_game_ip_price_premium_counterexample | 2021-11-22 | 236700 | 245700 on 2021-11-22 | 52000 on 2022-06-23 | 3.8% | 3.8% | 3.8% | -78.03% | -78.84% |
| C27_259960_KRAFTON_20211112_GLOBAL_GAME_IP_RELEASE_FALSE_GREEN | 259960 | global_game_release_false_green_counterexample | 2021-11-12 | 535000 | 580000 on 2021-11-17 | 212500 on 2022-07-01 | 8.41% | 8.41% | 8.41% | -60.28% | -63.36% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- A game-IP launch can be a valid Stage2 route when revenue rank, early user response, and monetization visibility appear before the valuation has fully capitalized the IP.
- 293490 is the positive anchor. The Odin-related launch path produced a large MFE with low early MAE. The row still becomes a later 4B lesson once the IP success is fully priced and retention/revision evidence must be refreshed.

### Stage3 / Green
- C27 Green should require retention cohorts, ARPU or monetization quality, global expansion cadence, margin and revision confirmation.
- 259960 shows why a global game-release headline should stay Yellow if launch attention is not followed by retention and monetization proof.

### 4B
- 112040 is the clean tokenized-IP/NFT 4B counterexample. The price had already capitalized WEMIX/NFT optionality; without token-economics, retention, cash-flow and revision support, the forward drawdown was severe.
- 293490 also required later 4B discipline after a valid launch thesis matured into a high-expectation valuation state.

### 4C
- No hard delisting, regulation, or launch-cancellation break is asserted.
- The C27 break mode is monetization decay: the IP can remain known, but retention, ARPU, live-ops, token economics, margin and revisions fail to support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C27_112040_WEMADE_20211122_NFT_WEMIX_IP_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C27_259960_KRAFTON_20211112_GLOBAL_GAME_IP_RELEASE_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 30,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C27_293490_KAKAOGAMES_20210629_ODIN_GLOBAL_IP_MONETIZATION_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 56,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C27 guard:
```text
if content_ip_launch_attention and revenue_rank_retention_monetization_bridge_visible:
    allow_stage2_actionable = true

if tokenized_ip_or_game_release_price_premium and no retention_arpu_cashflow_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and retention_or_monetization_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 112040 / 2021-11-22: tokenized game-IP/NFT premium can be over-promoted if the model treats platform narrative as cash-flow and retention evidence.
- 259960 / 2021-11-12: global game-release attention can look like Green, but the forward path argues for Yellow/counterexample unless retention, monetization and revision evidence close.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -0.71, "MAE_30D_pct": -2.14, "MAE_90D_pct": -2.14, "MFE_180D_pct": 107.14, "MFE_30D_pct": 89.29, "MFE_90D_pct": 89.29, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_293490_KAKAOGAMES_20210629_ODIN_GLOBAL_IP_MONETIZATION_STAGE2", "case_role": "positive_game_ip_launch_monetization_stage2_success_with_later_4b", "company_name": "카카오게임즈", "corporate_action_window_status": "corporate_action_candidate_count=0", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when a new game IP launch, early revenue rank and monetization visibility created a clear rerating route. Green still requires retention, live-ops durability, overseas expansion, margin and revision bridge; after the November price run, the same evidence required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -26.03, "entry_date": "2021-06-29", "entry_price": 56000, "evidence_family": "game_ip_launch_revenue_rank_retention_global_monetization_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_NFT_RETENTION_MONETIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2021-06-29", "low_price_180d": 55600, "peak_date": "2021-11-17", "peak_price": 116000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/293/293490.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 10, "total": 56, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C27_293490_KAKAOGAMES_20210629_ODIN_GLOBAL_IP_MONETIZATION_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_IP_launch_attention", "revenue_rank_or_download_visibility", "global_monetization_or_live_ops_route"], "stage3_evidence_fields": ["retention_cohort_required", "ARPU_or_user_monetization_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["content_IP_or_tokenized_IP_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["retention_or_user_activity_fade", "token_economics_or_platform_quality_failure", "monetization_margin_revision_bridge_failure"], "symbol": "293490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv", "trigger_date": "2021-06-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -78.03, "MAE_30D_pct": -37.35, "MAE_90D_pct": -59.53, "MFE_180D_pct": 3.8, "MFE_30D_pct": 3.8, "MFE_90D_pct": 3.8, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_112040_WEMADE_20211122_NFT_WEMIX_IP_PRICE_PREMIUM_4B", "case_role": "nft_tokenized_game_ip_price_premium_counterexample", "company_name": "위메이드", "corporate_action_window_status": "selected 2021-11-22 window is after 2021-09-13 and 2021-10-06 corporate-action candidates; post-event tradable rows used with caveat", "current_profile_error": true, "current_profile_verdict": "NFT/tokenized game-IP premium should route to local 4B or counterexample unless token economics, retention, user monetization, cash-flow quality, regulation and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -78.84, "entry_date": "2021-11-22", "entry_price": 236700, "evidence_family": "tokenized_game_ip_nft_platform_price_premium_without_retention_cashflow_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_NFT_RETENTION_MONETIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-06-23", "low_price_180d": 52000, "peak_date": "2021-11-22", "peak_price": 245700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/112/112040.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C27_112040_WEMADE_20211122_NFT_WEMIX_IP_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_IP_launch_attention", "revenue_rank_or_download_visibility", "global_monetization_or_live_ops_route"], "stage3_evidence_fields": ["retention_cohort_required", "ARPU_or_user_monetization_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["content_IP_or_tokenized_IP_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["retention_or_user_activity_fade", "token_economics_or_platform_quality_failure", "monetization_margin_revision_bridge_failure"], "symbol": "112040", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2021.csv", "trigger_date": "2021-11-22", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -60.28, "MAE_30D_pct": -16.17, "MAE_90D_pct": -53.55, "MFE_180D_pct": 8.41, "MFE_30D_pct": 8.41, "MFE_90D_pct": 8.41, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_259960_KRAFTON_20211112_GLOBAL_GAME_IP_RELEASE_FALSE_GREEN", "case_role": "global_game_release_false_green_counterexample", "company_name": "크래프톤", "corporate_action_window_status": "corporate_action_candidate_count=0", "current_profile_error": true, "current_profile_verdict": "Global game-release attention should stay Yellow if launch downloads or IP brand are not followed by retention, monetization, live-ops cadence, margin and revision evidence. Price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.36, "entry_date": "2021-11-12", "entry_price": 535000, "evidence_family": "global_game_release_download_launch_attention_without_retention_monetization_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_NFT_RETENTION_MONETIZATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-07-01", "low_price_180d": 212500, "peak_date": "2021-11-17", "peak_price": 580000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/259/259960.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 30, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C27_259960_KRAFTON_20211112_GLOBAL_GAME_IP_RELEASE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["content_or_game_IP_launch_attention", "revenue_rank_or_download_visibility", "global_monetization_or_live_ops_route"], "stage3_evidence_fields": ["retention_cohort_required", "ARPU_or_user_monetization_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["content_IP_or_tokenized_IP_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["retention_or_user_activity_fade", "token_economics_or_platform_quality_failure", "monetization_margin_revision_bridge_failure"], "symbol": "259960", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/259/259960/2021.csv", "trigger_date": "2021-11-12", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "GAME_IP_LAUNCH_NFT_RETENTION_MONETIZATION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "content_ip_global_monetization_game_launch_nft_retention_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C27 content-IP/global monetization rows should allow Stage2 on early game-IP launch evidence only when revenue rank, retention, global expansion and monetization quality can plausibly reach revisions; NFT/tokenized IP or game-release price premium without retention/cash-flow bridge should route to local 4B or counterexample.",
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
3. Add C27-specific game-IP launch / retention / tokenized-IP cash-flow guard only as a shadow candidate until more rows exist.

Candidate rule:
- C27_STAGE2_ALLOWED_ON_LAUNCH_REVENUE_RANK_RETENTION_BRIDGE
- C27_GREEN_REQUIRES_RETENTION_ARPU_GLOBAL_EXPANSION_MARGIN_REVISION
- C27_TOKENIZED_IP_PRICE_PREMIUM_LOCAL_4B
- C27_GAME_RELEASE_WITHOUT_RETENTION_MONETIZATION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

