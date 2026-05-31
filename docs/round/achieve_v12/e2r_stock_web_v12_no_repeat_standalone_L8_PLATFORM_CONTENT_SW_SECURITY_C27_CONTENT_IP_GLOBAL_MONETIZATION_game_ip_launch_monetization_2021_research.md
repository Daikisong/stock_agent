# E2R V12 No-Repeat Standalone Residual Research
## R8 / L8 / C27 — Game IP launch monetization and 4B guard

metadata:
```text
selected_round: R8
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_LAUNCH_MONETIZATION_4B_GUARD
loop_objective: coverage_gap_fill|positive_counterexample_balance|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_game_ip_launch_monetization_2021_research.md
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

This run avoids the top-covered C27 symbols and adds 194480, 293490, and 078340.  
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
078340 컴투스: 2021/2022 forward window clean; corporate-action candidate is 2007-07-18.
```

## 3. Research thesis

C27 should not treat every content rally as durable IP monetization. The mechanism must close:

```text
game/content launch or IP attention
→ sales rank / users / global traction
→ repeat monetization and revenue quality
→ operating leverage / revision bridge
→ rerating
```

The positive cases show that a real hit can move EPS bodyweight quickly. The counterexample shows the opposite: when the market buys the symbol of an IP/metaverse/token story without cash-flow proof, the same narrative becomes a paper lantern in a storm.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING | 194480 | positive_structural_success_with_later_4b | 2021-01-21 | 17250 | 199500 on 2021-09-27 | 15050 on 2021-01-21 | 300.0% | 833.33% | 1056.52% | -12.75% | -41.1% |
| C27_293490_KAKAOGAMES_20210629_ODIN_LAUNCH_STAGE2_TO_4B | 293490 | positive_launch_success_but_full_4b_needed | 2021-06-29 | 59700 | 116000 on 2021-11-17 | 55600 on 2021-06-29 | 77.55% | 77.55% | 94.3% | -6.87% | -44.91% |
| C27_078340_COM2US_20211110_METAVERSE_NFT_IP_BLOWOFF_FALSE_GREEN | 078340 | false_green_counterexample | 2021-11-10 | 169300 | 183300 on 2021-11-11 | 66300 on 2022-04-12 | 8.27% | 8.27% | 8.27% | -60.84% | -63.83% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Game launch, sales-rank attention, and IP monetization routes are valid Stage2 research triggers.
- 293490 shows that Stage2 can be useful before the full durability bridge is visible.

### Stage3 / Green
- C27 Green should require repeat monetization, revenue quality, and revision evidence.
- 194480 is the strongest positive anchor because the price path reflects a real hit-cycle rerating, not just vague IP optionality.

### 4B
- 194480 and 293490 both require later 4B discipline after the market capitalizes the launch hit.
- The 4B trigger should separate valid launch success from exhaustion after a hit-cycle price run.

### 4C
- 078340 is not a hard accounting-break case.
- It is a content/IP thesis-quality break: metaverse/NFT/IP premium failed to close into durable monetization, retention, or revision.

## 6. Raw component score breakdown

```json
{
  "C27_078340_COM2US_20211110_METAVERSE_NFT_IP_BLOWOFF_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING": {
    "bottleneck_pricing_power": 11,
    "capital_allocation": 2,
    "eps_fcf_explosion": 16,
    "information_confidence": 4,
    "market_mispricing": 13,
    "total": 71,
    "valuation_rerating_runway": 12,
    "visibility_quality": 13
  },
  "C27_293490_KAKAOGAMES_20210629_ODIN_LAUNCH_STAGE2_TO_4B": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 2,
    "eps_fcf_explosion": 13,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 60,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C27 guard:
```text
if content_ip_attention and no repeat_monetization_or_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if hit_cycle_price_run and launch_revision_bridge_is_mature:
    route_to_local_or_full_4B_watch = true

if token_or_metaverse_premium and no cashflow_quality:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 078340 / 2021-11-10: metaverse/NFT/IP premium can be over-promoted if C27 treats narrative heat as monetization evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.75, "MAE_30D_pct": -12.75, "MAE_90D_pct": -12.75, "MFE_180D_pct": 1056.52, "MFE_30D_pct": 300.0, "MFE_90D_pct": 833.33, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING", "case_role": "positive_structural_success_with_later_4b", "company_name": "데브시스터즈", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Green can be justified only when global launch traction converts into sales rank, repeat monetization, and revision; later 4B discipline is still required after the hit-cycle blowoff.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.1, "entry_date": "2021-01-21", "entry_price": 17250, "evidence_family": "cookie_run_kingdom_global_ip_hit_monetization_rerating", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_MONETIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2021-01-21", "low_price_180d": 15050, "peak_date": "2021-09-27", "peak_price": 199500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/194/194480.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 11, "capital_allocation": 2, "eps_fcf_explosion": 16, "information_confidence": 4, "market_mispricing": 13, "total": 71, "valuation_rerating_runway": 12, "visibility_quality": 13}, "reuse_reason": null, "same_entry_group_id": "C27_194480_DEVSISTERS_20210121_COOKIE_RUN_KINGDOM_GLOBAL_IP_RERATING", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["game_or_content_launch_attention", "sales_rank_or_user_traction_claim", "ip_global_monetization_route"], "stage3_evidence_fields": ["repeat_monetization_required", "revenue_quality_and_operating_leverage_required", "revision_bridge_required"], "stage4b_evidence_fields": ["hit_cycle_or_token_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hit_decay_or_sales_rank_fade", "metaverse_token_premium_without_cashflow", "revision_or_retention_break"], "symbol": "194480", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/194/194480/2021.csv", "trigger_date": "2021-01-21", "trigger_type": "Stage3-Green", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -6.87, "MAE_30D_pct": -6.87, "MAE_90D_pct": -6.87, "MFE_180D_pct": 94.3, "MFE_30D_pct": 77.55, "MFE_90D_pct": 77.55, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_293490_KAKAOGAMES_20210629_ODIN_LAUNCH_STAGE2_TO_4B", "case_role": "positive_launch_success_but_full_4b_needed", "company_name": "카카오게임즈", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was usable when launch traction and ranking proof appeared, but Green requires durable monetization and revision bridge; after peak, full-window 4B watch matters.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.91, "entry_date": "2021-06-29", "entry_price": 59700, "evidence_family": "odin_domestic_launch_sales_rank_to_operating_leverage", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_MONETIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2021-06-29", "low_price_180d": 55600, "peak_date": "2021-11-17", "peak_price": 116000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/293/293490.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 2, "eps_fcf_explosion": 13, "information_confidence": 4, "market_mispricing": 11, "total": 60, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C27_293490_KAKAOGAMES_20210629_ODIN_LAUNCH_STAGE2_TO_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["game_or_content_launch_attention", "sales_rank_or_user_traction_claim", "ip_global_monetization_route"], "stage3_evidence_fields": ["repeat_monetization_required", "revenue_quality_and_operating_leverage_required", "revision_bridge_required"], "stage4b_evidence_fields": ["hit_cycle_or_token_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hit_decay_or_sales_rank_fade", "metaverse_token_premium_without_cashflow", "revision_or_retention_break"], "symbol": "293490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv", "trigger_date": "2021-06-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -60.84, "MAE_30D_pct": -21.44, "MAE_90D_pct": -38.45, "MFE_180D_pct": 8.27, "MFE_30D_pct": 8.27, "MFE_90D_pct": 8.27, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "case_id": "C27_078340_COM2US_20211110_METAVERSE_NFT_IP_BLOWOFF_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "컴투스", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Metaverse/NFT/IP premium should not become Green without repeat monetization, revenue quality, and revision bridge; this is a local 4B/counterexample row.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.83, "entry_date": "2021-11-10", "entry_price": 169300, "evidence_family": "metaverse_nft_ip_price_premium_without_durable_monetization_bridge", "evidence_url_pending": false, "fine_archetype_id": "GAME_IP_LAUNCH_MONETIZATION_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "low_date_180d": "2022-04-12", "low_price_180d": 66300, "peak_date": "2021-11-11", "peak_price": 183300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/078/078340.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C27_078340_COM2US_20211110_METAVERSE_NFT_IP_BLOWOFF_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R8", "source_proxy_only": false, "stage2_evidence_fields": ["game_or_content_launch_attention", "sales_rank_or_user_traction_claim", "ip_global_monetization_route"], "stage3_evidence_fields": ["repeat_monetization_required", "revenue_quality_and_operating_leverage_required", "revision_bridge_required"], "stage4b_evidence_fields": ["hit_cycle_or_token_premium_blowoff", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["hit_decay_or_sales_rank_fade", "metaverse_token_premium_without_cashflow", "revision_or_retention_break"], "symbol": "078340", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078340/2021.csv", "trigger_date": "2021-11-10", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "GAME_IP_LAUNCH_MONETIZATION_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "loop_contribution_label": "content_ip_launch_and_4b_guard_added",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R8",
  "shadow_rule_candidate": "C27 content/IP rerating should permit Green only when launch traction closes into repeat monetization, revenue quality, and revision bridge; metaverse/token/IP price premium without cashflow should route to local 4B or counterexample.",
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
3. Add C27-specific repeat monetization / revenue quality / revision bridge logic only as a shadow candidate until more rows exist.

Candidate rule:
- C27_CONTENT_IP_GREEN_REQUIRES_REPEAT_MONETIZATION_REVISION
- C27_HIT_CYCLE_PRICE_RUN_LOCAL_OR_FULL_4B
- C27_METAVERSE_TOKEN_PREMIUM_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

