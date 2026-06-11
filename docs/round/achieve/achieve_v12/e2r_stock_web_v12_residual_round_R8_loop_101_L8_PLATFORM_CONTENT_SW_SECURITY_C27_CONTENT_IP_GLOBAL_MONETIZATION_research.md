# E2R Stock-Web v12 Residual Research — R8 / L8 / C27

```text
filename = e2r_stock_web_v12_residual_round_R8_loop_101_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R8
selected_loop = 101
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Coverage / novelty check

`V12_Research_No_Repeat_Index.md`에서 C27은 21 rows / 12 symbols이고, 반복 위험 symbol은 352820, 253450, 259960, 041510, 263750, 035900 계열이다.  
이번 loop는 그 반복 구간을 피하고, **게임 IP / 글로벌 출시 / liveops / single-title pipeline** 쪽 신규 symbol 4개를 C27에 압축했다.

```text
existing_high_repeat_avoided = 352820, 253450, 259960, 041510, 263750, 035900
new_symbols = 112040, 194480, 095660, 293490
new_independent_case_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
reused_case_count = 0
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_detected = false
```

## 2. Stock-Web atlas validation

Stock-Web manifest basis:

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "ohlcv_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "research_pack_default_price_basis": "tradable_raw",
  "corporate_action_contaminated_windows_blocked_by_default": true
}
```

Symbol validation summary:

| symbol | name | profile status | 2024 calibration window |
|---|---|---|---|
| 112040 | 위메이드 | active_like / caveat: historical CA candidates only | usable, not inside CA window |
| 194480 | 데브시스터즈 | active_like / no CA candidate | usable |
| 095660 | 네오위즈 | active_like / caveat: historical CA candidates only | usable, not inside CA window |
| 293490 | 카카오게임즈 | active_like / no CA candidate | usable |

## 3. Trigger-level backtest rows

| case_id | symbol | name | trigger | entry | entry_price | class | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE |
|---|---:|---|---|---|---:|---|---:|---:|---:|
| C27-R8-L101-001 | 112040 | 위메이드 | Stage2-Actionable | 2024-03-11 | 55,000 | mixed_positive_local_4b | 46.36% / -17.45% | 46.36% / -28.18% | 46.36% / -46.91% |
| C27-R8-L101-002 | 194480 | 데브시스터즈 | Stage2-Actionable | 2024-03-07 | 45,050 | positive_with_high_MAE_watch | 12.99% / -3.88% | 69.37% / -3.88% | 69.37% / -20.11% |
| C27-R8-L101-003 | 095660 | 네오위즈 | Stage2 | 2024-02-02 | 26,400 | counterexample | 8.71% / -18.94% | 8.71% / -26.52% | 8.71% / -33.52% |
| C27-R8-L101-004 | 293490 | 카카오게임즈 | Stage2 | 2024-03-11 | 23,850 | counterexample | 1.05% / -10.90% | 1.05% / -20.38% | 1.05% / -31.15% |

Aggregate:

```text
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 2
current_profile_error_count = 4
average_MFE_30D_pct = 17.28
average_MAE_30D_pct = -12.79
average_MFE_90D_pct = 31.37
average_MAE_90D_pct = -19.74
average_MFE_180D_pct = 31.37
average_MAE_180D_pct = -32.92
```

## 4. Case notes

### C27-R8-L101-001 — 112040 위메이드

Entry uses 2024-03-11 close 55,000. The local IP/global launch path produced a vertical price MFE into 2024-03-20 high 80,500, but the same 180D path later printed a deep drawdown toward the 29,200 area.  
This is not a clean Stage3-Green example. It is a **Stage2-Actionable → local 4B watch** case unless monetization evidence is refreshed by user/revenue retention, liveops durability, royalty/platform take-rate, and operating leverage.

Raw component proxy:

```json
{"eps_fcf": 12, "quality": 12, "bottleneck": 7, "mispricing": 14, "rerating": 10, "capital": 4, "info": 8}
```

### C27-R8-L101-002 — 194480 데브시스터즈

Entry uses 2024-03-07 close 45,050. This case has the best C27 alignment in the set: IP monetization and title reacceleration produced a later 90D high around 76,300.  
However, after the MFE extension, MAE expanded enough that C27 should not treat one title/event as a permanent rerating without retention and margin revision follow-through.

Raw component proxy:

```json
{"eps_fcf": 13, "quality": 13, "bottleneck": 8, "mispricing": 15, "rerating": 13, "capital": 5, "info": 9}
```

### C27-R8-L101-003 — 095660 네오위즈

Entry uses 2024-02-02 close 26,400. The row is a counterexample: single-title/global-console vocabulary produced only a small MFE and then a large MAE.  
For C27, prior title quality is not enough. The residual rule should require fresh liveops conversion, new launch monetization, booking/revenue proof, or margin revision.

Raw component proxy:

```json
{"eps_fcf": 7, "quality": 9, "bottleneck": 6, "mispricing": 10, "rerating": 8, "capital": 4, "info": 7}
```

### C27-R8-L101-004 — 293490 카카오게임즈

Entry uses 2024-03-11 close 23,850. The pipeline label did not create meaningful upside and the downside expanded across the 90D/180D windows.  
This is a clean C27 false-positive case: portfolio/pipeline vocabulary without hit validation, user retention, global monetization, or operating margin bridge should not receive Stage2-Actionable bonus.

Raw component proxy:

```json
{"eps_fcf": 6, "quality": 8, "bottleneck": 5, "mispricing": 11, "rerating": 8, "capital": 4, "info": 7}
```

## 5. Machine-readable JSONL trigger rows

```jsonl
{"schema_version": "v12_trigger_row_1", "case_id": "C27-R8-L101-001", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "112040", "name": "위메이드", "entry_date": "2024-03-11", "entry_price": 55000, "trigger_type": "Stage2-Actionable", "trigger_family": "game_ip_global_launch_web3_liveops_spike_then_4b", "classification": "mixed_positive_local_4b", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 46.36, "MAE_30D_pct": -17.45, "MFE_90D_pct": 46.36, "MAE_90D_pct": -28.18, "MFE_180D_pct": 46.36, "MAE_180D_pct": -46.91, "peak_price_used": 80500, "trough_price_used": 29200, "current_profile_error_type": "local_4b_after_ip_price_mfe", "evidence_url_pending": true, "source_proxy_only": true, "usable_for_calibration": true, "corporate_action_window_blocked": false, "notes": "Global IP launch/liveops label created a strong price MFE, but the window quickly becomes local 4B unless user/revenue retention and margin bridge appear."}
{"schema_version": "v12_trigger_row_1", "case_id": "C27-R8-L101-002", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "194480", "name": "데브시스터즈", "entry_date": "2024-03-07", "entry_price": 45050, "trigger_type": "Stage2-Actionable", "trigger_family": "cookie_run_new_title_global_ip_monetization_reacceleration", "classification": "positive_with_high_MAE_watch", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 12.99, "MAE_30D_pct": -3.88, "MFE_90D_pct": 69.37, "MAE_90D_pct": -3.88, "MFE_180D_pct": 69.37, "MAE_180D_pct": -20.11, "peak_price_used": 76300, "trough_price_used": 36050, "current_profile_error_type": "local_4b_after_ip_price_mfe", "evidence_url_pending": true, "source_proxy_only": true, "usable_for_calibration": true, "corporate_action_window_blocked": false, "notes": "New title/IP monetization had real follow-through to June, but post-spike drawdown argues for local 4B if retention/ARPU bridge is not sustained."}
{"schema_version": "v12_trigger_row_1", "case_id": "C27-R8-L101-003", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "095660", "name": "네오위즈", "entry_date": "2024-02-02", "entry_price": 26400, "trigger_type": "Stage2", "trigger_family": "single_title_global_console_ip_label_without_new_monetization_bridge", "classification": "counterexample", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 8.71, "MAE_30D_pct": -18.94, "MFE_90D_pct": 8.71, "MAE_90D_pct": -26.52, "MFE_180D_pct": 8.71, "MAE_180D_pct": -33.52, "peak_price_used": 28700, "trough_price_used": 17550, "current_profile_error_type": "stage2_without_ip_monetization_bridge", "evidence_url_pending": true, "source_proxy_only": true, "usable_for_calibration": true, "corporate_action_window_blocked": false, "notes": "A known global IP label without fresh launch, DAU/ARPU or margin revision bridge produced weak upside and large downside."}
{"schema_version": "v12_trigger_row_1", "case_id": "C27-R8-L101-004", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE", "symbol": "293490", "name": "카카오게임즈", "entry_date": "2024-03-11", "entry_price": 23850, "trigger_type": "Stage2", "trigger_family": "portfolio_game_pipeline_label_without_hit_revenue_conversion", "classification": "counterexample", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 1.05, "MAE_30D_pct": -10.9, "MFE_90D_pct": 1.05, "MAE_90D_pct": -20.38, "MFE_180D_pct": 1.05, "MAE_180D_pct": -31.15, "peak_price_used": 24100, "trough_price_used": 16420, "current_profile_error_type": "stage2_without_ip_monetization_bridge", "evidence_url_pending": true, "source_proxy_only": true, "usable_for_calibration": true, "corporate_action_window_blocked": false, "notes": "Pipeline/theme vocabulary without hit confirmation, retention, booking/revenue conversion, and margin revision behaved as a false positive."}
```

## 6. Score-return alignment

C27 does not reward “content/IP label” itself. The return profile splits cleanly:

```text
positive route = IP label + fresh launch/liveops evidence + revenue/ARPU/retention bridge + margin revision
false-positive route = pipeline/title vocabulary only + price spike or no follow-through + missing monetization bridge
local_4B route = large MFE arrives before retention/margin proof, then MAE widens
```

Current calibrated profile stress test:

```text
stage2_actionable_evidence_bonus = helpful only when evidence is monetization-specific
price_only_blowoff_blocks_positive_stage = should remain true
full_4b_requires_non_price_evidence = should remain true
hard_4c_thesis_break_routes_to_4c = unchanged
```

Residual error:

```text
C27 still needs a specific bridge:
1. fresh title/liveops/global launch evidence
2. user retention or booking/revenue conversion
3. margin/revision follow-through
4. post-spike MAE guard when only IP/pipeline label exists
```

## 7. Shadow rule candidate

```yaml
shadow_rule_candidate:
  id: C27_GAME_IP_GLOBAL_MONETIZATION_BRIDGE_REQUIRED
  scope:
    large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
    canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
  condition:
    requires_at_least_two:
      - fresh_global_launch_or_liveops_event
      - booking_revenue_or_ARPU_conversion
      - retention_or_rank_persistence
      - margin_revision_or_OP_leverage
      - licensing_or_platform_monetization_contract
  blocks:
    - content_ip_label_only
    - game_pipeline_vocabulary_only
    - single_title_hype_without_monetization_bridge
    - price_MFE_without_non_price_followthrough
  stage_effect:
    if_bridge_missing: cap_at_Stage2_or_local_4B_watch
    if_bridge_confirmed: allow_Stage2_Actionable_and_Yellow_watch
    if_post_spike_MAE_high: route_to_local_4B_watch
```

```yaml
shadow_weight_delta_candidate:
  do_not_apply_now: true
  scope: C27_CONTENT_IP_GLOBAL_MONETIZATION
  proposed_axis:
    Earnings_Visibility_and_Quality: "+2 when booking/revenue/retention bridge confirmed"
    Information_Confidence: "+2 when launch/retention/margin evidence is source-backed"
    Valuation_Rerating_Runway: "-2 when only pipeline/IP label exists"
    Market_Mispricing: "-1 when post-spike MAE > 20% without fresh monetization proof"
```

## 8. Residual contribution summary

```text
new_axis_proposed = C27_game_ip_global_monetization_retention_margin_bridge_required | C27_pipeline_label_high_MAE_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When batch-applying v12 residual research MDs:
1. Parse all JSONL rows in this MD.
2. Validate required fields:
   - large_sector_id
   - canonical_archetype_id
   - symbol
   - entry_date
   - entry_price
   - trigger_type
   - MFE_30D_pct / MAE_30D_pct
   - MFE_90D_pct / MAE_90D_pct
   - MFE_180D_pct / MAE_180D_pct
3. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add C27-specific shadow rule candidate:
   C27_GAME_IP_GLOBAL_MONETIZATION_BRIDGE_REQUIRED.
5. Do not loosen Stage3-Green thresholds.
6. Keep price_only_blowoff_blocks_positive_stage = true.
7. Use this MD only as shadow calibration evidence until aggregate validation passes.
```

## 10. Completion state

```text
completed_round = R8
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = GAME_IP_GLOBAL_LAUNCH_LIVEOPS_MONETIZATION_BRIDGE_VS_PIPELINE_LABEL_FALSE_POSITIVE
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 2
current_profile_error_count = 4
auto_selected_coverage_gap = C27 rows 21 -> 25 if accepted; still Priority 0, need 5 to 30
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
