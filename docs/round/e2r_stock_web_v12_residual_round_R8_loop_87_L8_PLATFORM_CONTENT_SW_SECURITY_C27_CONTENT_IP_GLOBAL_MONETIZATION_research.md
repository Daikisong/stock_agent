# E2R Stock-Web v12 Residual Research — R8 Loop 87 / L8 / C27

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 87,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 87,
  "computed_next_round": "R9",
  "computed_next_loop": 87,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_id": "GAME_IP_BLOCKCHAIN_KPOP_ARTIST_FANDOM_PLATFORM_GLOBAL_MONETIZATION_REVENUE_MARGIN_BRIDGE_VS_CONTENT_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "content_IP_global_monetization_guardrail",
    "game_IP_and_Kpop_fandom_revenue_to_margin_bridge_test",
    "content_IP_theme_MFE_vs_paid_user_ARPU_contract_revenue_bridge_test",
    "local_4B_timing_after_content_IP_MFE",
    "hard_4C_non_price_IP_launch_user_churn_or_margin_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
    "corporate_action_window_caveat_review",
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

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 87
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
computed_next_round = R9
computed_next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

R8 is the platform / content / software / security round. This run selects C27 because loop87 has reached R8 after R7/C25, loop86 R8 used C28, and loop85 R8 used C26. The selected route is game IP, K-pop IP and fandom-platform monetization.

The tested mechanism:

```text
content IP / game launch / artist IP / fandom platform headline
→ paid users or revenue
→ ARPU / take-rate / revenue recognition
→ release cadence and retention
→ fan or user monetization
→ gross / OP margin conversion
→ durable rerating or content-theme fade
```

C27 is the stage plus the cash register. The audience matters, but the rerating holds only when users, ARPU, releases and margins line up.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C27 top-covered symbols include `035900`, `194480`, `259960`, `352820`, `225570`, and `253450`. This run avoids that top-covered set and uses:

```text
112040 / 위메이드
122870 / 와이지엔터테인먼트
376300 / 디어유
```

All three are treated as new independent C27 content/IP global monetization cases for this loop.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 112040 | 위메이드 | `atlas/symbol_profiles/112/112040.json` | old CA candidates through 2021; selected 2024 forward window clean |
| 122870 | 와이지엔터테인먼트 | `atlas/symbol_profiles/122/122870.json` | old CA candidates through 2014; selected 2024 forward window clean |
| 376300 | 디어유 | `atlas/symbol_profiles/376/376300.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R8L87-C27-01 | 112040 | 2024-02-13 | 46,950 | 180D | clean | true |
| R8L87-C27-02 | 122870 | 2024-02-13 | 42,500 | 180D | clean | true |
| R8L87-C27-03 | 376300 | 2024-02-13 | 32,500 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C27_CONTENT_IP_GLOBAL_MONETIZATION | GAME_IP_BLOCKCHAIN_GLOBAL_MONETIZATION | keep Stage2 with local 4B if paid users, revenue recognition and margin bridge are repaired |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | KPOP_ARTIST_IP_LOW_MFE_FADE | reject low-MFE K-pop IP rebound without release/tour/fan-monetization bridge |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | FANDOM_PLATFORM_PAID_USER_HIGH_MAE_FADE | reject fandom-platform MFE without subscriber, ARPU, churn and margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R8L87-C27-01 | 112040 | 위메이드 | Stage2-Actionable | 2024-02-13 | 46,950 | 71.46 | -37.81 | current_profile_partially_correct_local_4B_revenue_margin_watch_needed |
| R8L87-C27-02 | 122870 | 와이지엔터테인먼트 | Stage2-FalsePositive | 2024-02-13 | 42,500 | 12.82 | -29.53 | current_profile_false_positive_low_MFE_content_IP_theme |
| R8L87-C27-03 | 376300 | 디어유 | Stage2-FalsePositive | 2024-02-13 | 32,500 | 21.54 | -45.72 | current_profile_false_positive_high_MAE_fandom_platform_theme |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C27 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: paid users, ARPU/take-rate, launch/release cadence, fan/user retention, revenue recognition, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 112040 | `atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv` | `atlas/symbol_profiles/112/112040.json` |
| 122870 | `atlas/ohlcv_tradable_by_symbol_year/122/122870/2024.csv` | `atlas/symbol_profiles/122/122870.json` |
| 376300 | `atlas/ohlcv_tradable_by_symbol_year/376/376300/2024.csv` | `atlas/symbol_profiles/376/376300.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 112040 / 위메이드

C27 game-IP / blockchain global monetization positive with local 4B watch. The February trigger produced a large MFE into March, but the later drawdown shows that clean Green requires paid-user, ARPU, revenue-recognition and margin bridge repair.

### Case 2 — 122870 / 와이지엔터테인먼트

C27 K-pop artist-IP monetization false positive. The MFE was limited and later drawdown was larger. Release cadence, tour economics and fan platform monetization must be explicit before this route can validate Stage2.

### Case 3 — 376300 / 디어유

C27 fandom-platform monetization counterexample. The February MFE faded into a deep MAE by September. Paid-user growth, churn control, ARPU and margin conversion are required before clean Stage2.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 112040 | 46,950 | 71.46 | -1.49 | 71.46 | -18.64 | 71.46 | -37.81 | 2024-03-20 / 80,500 | -63.73 |
| 122870 | 42,500 | 11.06 | -6.12 | 12.82 | -7.76 | 12.82 | -29.53 | 2024-04-01 / 47,950 | -37.54 |
| 376300 | 32,500 | 21.54 | -11.85 | 21.54 | -15.69 | 21.54 | -45.72 | 2024-02-26 / 39,500 | -55.34 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R8L87-C27-01 | Stage2-Actionable if game-IP revenue bridge exists | large MFE, later deep drawdown | partially correct; local 4B/IP-revenue bridge needed |
| R8L87-C27-02 | risk of treating K-pop IP rebound as Stage2 | low MFE / deeper MAE | false positive |
| R8L87-C27-03 | risk of treating fandom platform MFE as Stage2 | MFE then high MAE | false positive / high-MAE guardrail |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C27, the residual is whether content/IP MFE becomes clean Stage2/Green before paid users, ARPU/take-rate, release cadence, retention and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R8L87-C27-01 | 0.85 | 0.75 | local 4B watch after game-IP MFE if user/revenue/margin bridge stalls |
| R8L87-C27-02 | 0.35 | 0.30 | K-pop artist-IP theme rejected without release/tour/fan monetization bridge |
| R8L87-C27-03 | 0.35 | 0.30 | fandom-platform MFE rejected without paid-user/ARPU/churn margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_IP_launch_user_revenue_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C27 hard 4C requires confirmed launch failure, content schedule break, paid-user churn, ARPU deterioration, revenue-recognition break, contract/artist-roster loss, or margin thesis break.

## 17. Sector / Canonical Rule Candidate

```text
rule_scope = no_new_global_rule
canonical_archetype_rule_candidate = C27_content_IP_paid_user_ARPU_revenue_margin_bridge_required
confidence = low
production_scoring_changed = false
shadow_weight_only = true
```

## 18. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 35.27 | -14.03 | may over-credit content/IP theme MFE without monetization bridge | needs C27 paid-user/revenue margin repair |
| P1 canonical shadow bridge profile | 3 | keeps 112040 with watch | demotes 122870/376300 | better alignment, source repair required |

## 19. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | canonical rule |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | GAME_IP_BLOCKCHAIN_KPOP_ARTIST_FANDOM_PLATFORM_GLOBAL_MONETIZATION_REVENUE_MARGIN_BRIDGE_VS_CONTENT_THEME_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | yes |

## 20. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - content_IP_theme_false_positive_low_MFE_high_MAE
  - paid_user_ARPU_revenue_margin_bridge_required
  - game_IP_large_MFE_then_high_drawdown_local_4B_needed
  - fandom_platform_paid_user_MFE_then_high_MAE_false_positive
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_IP_launch_user_revenue_margin_break
new_axis_proposed: false
existing_axis_strengthened:
  - C27_content_IP_paid_user_ARPU_revenue_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
do_not_propose_new_weight_delta: true
```

## 21. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- paid-user or ARPU evidence
- release / launch cadence
- fan or user retention
- revenue recognition and margin conversion
- production scoring implementation
```

## 22. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C27_content_IP_paid_user_ARPU_revenue_margin_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"Require paid-user or revenue evidence, ARPU/take-rate, release cadence, fan/user retention and gross/OP margin conversion before clean Stage2/Green","keeps 112040 with local 4B/IP-revenue watch; demotes 122870/376300","R8L87-C27-01-S2A-20240213|R8L87-C27-02-S2FP-20240213|R8L87-C27-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 23. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L87-C27-01", "symbol": "112040", "company_name": "위메이드", "round": "R8", "loop": 87, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_BLOCKCHAIN_KPOP_ARTIST_FANDOM_PLATFORM_GLOBAL_MONETIZATION_REVENUE_MARGIN_BRIDGE_VS_CONTENT_THEME_FADE", "case_type": "game_IP_blockchain_global_monetization_large_MFE_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L87-C27-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_game_IP_MFE_but_high_post_peak_drawdown_requires_revenue_margin_bridge", "current_profile_verdict": "current_profile_partially_correct_local_4B_revenue_margin_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C27 game-IP positives need launch quality, paid user retention, ARPU, platform/revenue recognition and gross/OP margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R8L87-C27-01-S2A-20240213", "case_id": "R8L87-C27-01", "symbol": "112040", "company_name": "위메이드", "round": "R8", "loop": 87, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_BLOCKCHAIN_KPOP_ARTIST_FANDOM_PLATFORM_GLOBAL_MONETIZATION_REVENUE_MARGIN_BRIDGE_VS_CONTENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail|paid_user_ARPU_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "game IP / blockchain platform / global monetization and launch-event proxy; primary user, revenue, token-platform and margin bridge evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["content_IP_proxy", "global_monetization_proxy", "platform_or_release_proxy"], "stage3_evidence_fields": ["paid_user_or_revenue", "ARPU_or_take_rate", "launch_or_release_cadence", "fan_or_user_retention", "margin_conversion"], "stage4b_evidence_fields": ["content_IP_MFE_without_revenue_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_IP_launch_user_churn_revenue_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv", "profile_path": "atlas/symbol_profiles/112/112040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 46950, "MFE_30D_pct": 71.46, "MAE_30D_pct": -1.49, "MFE_90D_pct": 71.46, "MAE_90D_pct": -18.64, "MFE_180D_pct": 71.46, "MAE_180D_pct": -37.81, "peak_date": "2024-03-20", "peak_price": 80500, "drawdown_after_peak_pct": -63.73, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "local_4B_watch_after_game_IP_MFE_if_user_revenue_margin_bridge_stalls", "four_b_evidence_type": ["content_IP_MFE_without_revenue_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_IP_launch_user_revenue_or_margin_break", "trigger_outcome_label": "large_game_IP_MFE_but_high_post_peak_drawdown_requires_revenue_margin_bridge", "current_profile_verdict": "current_profile_partially_correct_local_4B_revenue_margin_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2021_CA_candidates", "same_entry_group_id": "R8L87-C27-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L87-C27-01", "trigger_id": "R8L87-C27-01-S2A-20240213", "symbol": "112040", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"IP_strength_score": 55, "global_monetization_score": 45, "paid_user_or_revenue_score": 40, "ARPU_or_take_rate_score": 35, "launch_or_release_cadence_score": 40, "margin_bridge_score": 35, "platform_quality_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 85, "execution_risk_score": 65, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"IP_strength_score": 55, "global_monetization_score": 45, "paid_user_or_revenue_score": 40, "ARPU_or_take_rate_score": 35, "launch_or_release_cadence_score": 40, "margin_bridge_score": 35, "platform_quality_score": 45, "relative_strength_score": 70, "valuation_blowoff_risk_score": 95, "execution_risk_score": 75, "source_quality_score": 10, "4B_watch_score": 90, "4C_watch_score": 25}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/IP-revenue margin watch", "changed_components": ["paid_user_or_revenue_score", "ARPU_or_take_rate_score", "launch_or_release_cadence_score", "margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C27 requires content/IP MFE to convert into paid users, ARPU/take-rate, release cadence, fan/user retention, revenue recognition and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 71.46, "MAE_90D_pct": -18.64, "score_return_alignment_label": "large_game_IP_MFE_but_high_post_peak_drawdown_requires_revenue_margin_bridge", "current_profile_verdict": "current_profile_partially_correct_local_4B_revenue_margin_watch_needed"}
{"row_type": "case", "case_id": "R8L87-C27-02", "symbol": "122870", "company_name": "와이지엔터테인먼트", "round": "R8", "loop": 87, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_BLOCKCHAIN_KPOP_ARTIST_FANDOM_PLATFORM_GLOBAL_MONETIZATION_REVENUE_MARGIN_BRIDGE_VS_CONTENT_THEME_FADE", "case_type": "Kpop_artist_IP_global_monetization_low_MFE_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R8L87-C27-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_then_deep_MAE_Kpop_IP_monetization_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_content_IP_theme", "price_source": "Songdaiki/stock-web", "notes": "K-pop content/IP rebound should remain RiskWatch unless release cadence, tour monetization, fan platform conversion and margin bridge are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R8L87-C27-02-S2FP-20240213", "case_id": "R8L87-C27-02", "symbol": "122870", "company_name": "와이지엔터테인먼트", "round": "R8", "loop": 87, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_BLOCKCHAIN_KPOP_ARTIST_FANDOM_PLATFORM_GLOBAL_MONETIZATION_REVENUE_MARGIN_BRIDGE_VS_CONTENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail|paid_user_ARPU_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "K-pop artist IP / global tour and content monetization proxy without confirmed release schedule, tour economics, fan monetization or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["content_IP_proxy", "global_monetization_proxy", "platform_or_release_proxy"], "stage3_evidence_fields": ["paid_user_or_revenue", "ARPU_or_take_rate", "launch_or_release_cadence", "fan_or_user_retention", "margin_conversion"], "stage4b_evidence_fields": ["content_IP_MFE_without_revenue_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_IP_launch_user_churn_revenue_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/122/122870/2024.csv", "profile_path": "atlas/symbol_profiles/122/122870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 42500, "MFE_30D_pct": 11.06, "MAE_30D_pct": -6.12, "MFE_90D_pct": 12.82, "MAE_90D_pct": -7.76, "MFE_180D_pct": 12.82, "MAE_180D_pct": -29.53, "peak_date": "2024-04-01", "peak_price": 47950, "drawdown_after_peak_pct": -37.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "Kpop_artist_IP_theme_rejected_without_release_schedule_tour_fan_monetization_margin_bridge", "four_b_evidence_type": ["content_IP_MFE_without_revenue_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_IP_launch_user_revenue_or_margin_break", "trigger_outcome_label": "low_MFE_then_deep_MAE_Kpop_IP_monetization_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_content_IP_theme", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2014_CA_candidate", "same_entry_group_id": "R8L87-C27-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L87-C27-02", "trigger_id": "R8L87-C27-02-S2FP-20240213", "symbol": "122870", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"IP_strength_score": 35, "global_monetization_score": 20, "paid_user_or_revenue_score": 10, "ARPU_or_take_rate_score": 5, "launch_or_release_cadence_score": 10, "margin_bridge_score": 5, "platform_quality_score": 20, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"IP_strength_score": 35, "global_monetization_score": 20, "paid_user_or_revenue_score": 0, "ARPU_or_take_rate_score": 0, "launch_or_release_cadence_score": 0, "margin_bridge_score": 0, "platform_quality_score": 20, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 92, "4C_watch_score": 70}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Content-IP monetization RiskWatch", "changed_components": ["paid_user_or_revenue_score", "ARPU_or_take_rate_score", "launch_or_release_cadence_score", "margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C27 requires content/IP MFE to convert into paid users, ARPU/take-rate, release cadence, fan/user retention, revenue recognition and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 12.82, "MAE_90D_pct": -7.76, "score_return_alignment_label": "low_MFE_then_deep_MAE_Kpop_IP_monetization_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_content_IP_theme"}
{"row_type": "case", "case_id": "R8L87-C27-03", "symbol": "376300", "company_name": "디어유", "round": "R8", "loop": 87, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_BLOCKCHAIN_KPOP_ARTIST_FANDOM_PLATFORM_GLOBAL_MONETIZATION_REVENUE_MARGIN_BRIDGE_VS_CONTENT_THEME_FADE", "case_type": "fandom_platform_paid_user_IP_monetization_MFE_then_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L87-C27-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "fandom_platform_MFE_then_high_MAE_paid_user_monetization_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_fandom_platform_theme", "price_source": "Songdaiki/stock-web", "notes": "Fandom-platform IP monetization should not validate C27 unless paid-user growth, churn, ARPU, artist roster expansion and margin conversion are source-repaired."}
{"row_type": "trigger", "trigger_id": "R8L87-C27-03-S2FP-20240213", "case_id": "R8L87-C27-03", "symbol": "376300", "company_name": "디어유", "round": "R8", "loop": 87, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "GAME_IP_BLOCKCHAIN_KPOP_ARTIST_FANDOM_PLATFORM_GLOBAL_MONETIZATION_REVENUE_MARGIN_BRIDGE_VS_CONTENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|content_IP_global_monetization_guardrail|paid_user_ARPU_revenue_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "fandom platform / artist-IP monetization / paid-user expansion proxy without confirmed subscriber growth, churn control, ARPU or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["content_IP_proxy", "global_monetization_proxy", "platform_or_release_proxy"], "stage3_evidence_fields": ["paid_user_or_revenue", "ARPU_or_take_rate", "launch_or_release_cadence", "fan_or_user_retention", "margin_conversion"], "stage4b_evidence_fields": ["content_IP_MFE_without_revenue_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_IP_launch_user_churn_revenue_or_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/376/376300/2024.csv", "profile_path": "atlas/symbol_profiles/376/376300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 32500, "MFE_30D_pct": 21.54, "MAE_30D_pct": -11.85, "MFE_90D_pct": 21.54, "MAE_90D_pct": -15.69, "MFE_180D_pct": 21.54, "MAE_180D_pct": -45.72, "peak_date": "2024-02-26", "peak_price": 39500, "drawdown_after_peak_pct": -55.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "fandom_platform_MFE_rejected_without_paid_user_ARPU_churn_margin_bridge", "four_b_evidence_type": ["content_IP_MFE_without_revenue_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_IP_launch_user_revenue_or_margin_break", "trigger_outcome_label": "fandom_platform_MFE_then_high_MAE_paid_user_monetization_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_fandom_platform_theme", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R8L87-C27-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L87-C27-03", "trigger_id": "R8L87-C27-03-S2FP-20240213", "symbol": "376300", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "raw_component_scores_before": {"IP_strength_score": 35, "global_monetization_score": 20, "paid_user_or_revenue_score": 10, "ARPU_or_take_rate_score": 5, "launch_or_release_cadence_score": 10, "margin_bridge_score": 5, "platform_quality_score": 20, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 85, "source_quality_score": 15, "4B_watch_score": 80, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"IP_strength_score": 35, "global_monetization_score": 20, "paid_user_or_revenue_score": 0, "ARPU_or_take_rate_score": 0, "launch_or_release_cadence_score": 0, "margin_bridge_score": 0, "platform_quality_score": 20, "relative_strength_score": 35, "valuation_blowoff_risk_score": 75, "execution_risk_score": 95, "source_quality_score": 5, "4B_watch_score": 92, "4C_watch_score": 70}, "weighted_score_after": 42, "stage_label_after": "Rejected-Stage2 / Content-IP monetization RiskWatch", "changed_components": ["paid_user_or_revenue_score", "ARPU_or_take_rate_score", "launch_or_release_cadence_score", "margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C27 requires content/IP MFE to convert into paid users, ARPU/take-rate, release cadence, fan/user retention, revenue recognition and margin bridge before clean Stage2/Green.", "MFE_90D_pct": 21.54, "MAE_90D_pct": -15.69, "score_return_alignment_label": "fandom_platform_MFE_then_high_MAE_paid_user_monetization_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_fandom_platform_theme"}
{"row_type": "shadow_weight", "axis": "C27_content_IP_paid_user_ARPU_revenue_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Content/IP global monetization requires paid-user or revenue evidence, ARPU/take-rate, release cadence, fan/user retention and gross/OP margin conversion; content-theme MFE without bridge fades into high MAE or low-MFE false positive.", "backtest_effect": "keeps 112040 with local 4B/IP-revenue watch; demotes 122870/376300 content-IP monetization false positives", "trigger_ids": "R8L87-C27-01-S2A-20240213|R8L87-C27-02-S2FP-20240213|R8L87-C27-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R8", "loop": 87, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["content_IP_theme_false_positive_low_MFE_high_MAE", "paid_user_ARPU_revenue_margin_bridge_required", "game_IP_large_MFE_then_high_drawdown_local_4B_needed", "fandom_platform_paid_user_MFE_then_high_MAE_false_positive", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_IP_launch_user_revenue_margin_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 24. Deferred Coding Agent Handoff Prompt

Use only `calibration_usable=true` rows. Do not treat `source_proxy_only/evidence_url_pending` rows as runtime promotion-ready. For C27, test a canonical guard requiring paid-user or revenue evidence, ARPU/take-rate, release cadence, fan/user retention and gross/OP margin conversion before clean Stage2/Green.

## 25. Next Round State

```text
completed_round = R8
completed_loop = 87
next_round = R9
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 26. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
