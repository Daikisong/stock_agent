# E2R Stock-Web v12 Residual Research — R8 Loop 85 / L8 / C26

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R8",
  "completed_loop": 85,
  "computed_next_round": "R9",
  "computed_next_loop": 85,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "fine_archetype_id": "AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "platform_ad_revenue_operating_leverage_guardrail",
    "traffic_to_ad_revenue_take_rate_margin_bridge_test",
    "AI_ad_platform_theme_vs_retention_operating_leverage_test",
    "local_4B_timing_after_ad_platform_MFE",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
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
scheduled_loop = 85
allowed_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_large_sector = L8_PLATFORM_CONTENT_SW_SECURITY
selected_canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
computed_next_round = R9
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R8 is the platform / content / software / security round. This run selects C26 because loop83 tested C27 and loop84 tested C28.

The tested mechanism:

```text
platform / ad-tech / AI-ad / reward-ad headline
→ traffic or MAU quality
→ advertiser retention and ad spend recovery
→ ad revenue growth and take-rate
→ cost discipline and operating leverage
→ durable rerating or ad-platform theme fade
```

C26 is not “traffic went up.” It is the tollgate where traffic must become paid demand, take-rate and operating margin.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C26 top-covered symbols include `067160`, `035420`, `035720`, `089600`, `SOOP`, and `NAVER`. This run avoids that top-covered set and uses:

```text
237820 / 플레이디
216050 / 인크로스
236810 / 엔비티
```

All three are treated as new independent C26 platform/ad-revenue operating-leverage cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 237820 | 플레이디 | `atlas/symbol_profiles/237/237820.json` | no profile-level CA candidate |
| 216050 | 인크로스 | `atlas/symbol_profiles/216/216050.json` | old CA candidates through 2022; selected 2024 forward window clean |
| 236810 | 엔비티 | `atlas/symbol_profiles/236/236810.json` | old CA candidates through 2022; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R8L85-C26-01 | 237820 | 2024-02-13 | 6,250 | 180D | clean | true |
| R8L85-C26-02 | 216050 | 2024-02-13 | 10,930 | 180D | clean | true |
| R8L85-C26-03 | 236810 | 2024-02-13 | 7,410 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | AI_AD_AGENCY_THEME_MFE_LOCAL_4B | keep Stage2 only with ad revenue, retention, take-rate and OP leverage bridge; add local 4B after MFE |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | AD_TECH_REVENUE_REBOUND_FADE | reject low-MFE ad-tech rebound without advertiser retention and operating leverage |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | REWARD_AD_TRAFFIC_MONETIZATION_FADE | reject reward-platform traffic theme without MAU quality, advertiser demand and margin conversion |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R8L85-C26-01 | 237820 | 플레이디 | Stage2-Actionable | 2024-02-13 | 6,250 | 70.56 | -24.96 | current_profile_4B_too_late_after_AI_ad_theme_MFE |
| R8L85-C26-02 | 216050 | 인크로스 | Stage2-FalsePositive | 2024-02-13 | 10,930 | 4.12 | -44.01 | current_profile_false_positive_high_MAE |
| R8L85-C26-03 | 236810 | 엔비티 | Stage2-FalsePositive | 2024-02-13 | 7,410 | 23.62 | -56.48 | current_profile_false_positive_high_MAE_4B_too_late |

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

This MD creates a source-repair queue and a C26 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: traffic/MAU quality, advertiser retention, ad spend recovery, ad revenue growth, take-rate, CAC or cost discipline, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 237820 | `atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv` | `atlas/symbol_profiles/237/237820.json` |
| 216050 | `atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv` | `atlas/symbol_profiles/216/216050.json` |
| 236810 | `atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv` | `atlas/symbol_profiles/236/236810.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 237820 / 플레이디

C26 AI-ad agency positive with local 4B watch. The February entry produced a large MFE within weeks, but the later drawdown shows why ad-theme MFE cannot be treated as clean Green without source-repaired ad revenue, retention, take-rate and margin evidence.

### Case 2 — 216050 / 인크로스

C26 ad-tech revenue-rebound false positive. The MFE after the February trigger was very small, while the later MAE widened heavily. This is the clean demotion row for ad-tech rebound language.

### Case 3 — 236810 / 엔비티

C26 reward-ad traffic monetization false positive. The early MFE was tradable, but the later MAE was deep. Traffic monetization or reward-ad platform heat should not become Stage2 without MAU retention, advertiser demand and operating leverage.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 237820 | 6,250 | 70.56 | -4.80 | 70.56 | -6.24 | 70.56 | -24.96 | 2024-03-06 / 10,660 | -56.00 |
| 216050 | 10,930 | 4.12 | -8.60 | 4.12 | -29.55 | 4.12 | -44.01 | 2024-02-19 / 11,380 | -46.22 |
| 236810 | 7,410 | 23.62 | -12.55 | 23.62 | -27.26 | 23.62 | -56.48 | 2024-02-20 / 9,160 | -64.79 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R8L85-C26-01 | Stage2-Actionable if ad revenue/retention bridge exists | large MFE, later drawdown | partially correct; local 4B watch needed |
| R8L85-C26-02 | risk of treating ad-tech rebound as Stage2 | low MFE / high MAE | false positive |
| R8L85-C26-03 | risk of treating reward-ad traffic theme as Stage2 | early MFE / deep MAE | false positive / high-MAE guardrail |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C26, the residual is whether ad-platform or traffic monetization MFE becomes clean Stage2/Green before advertiser retention, ad revenue, take-rate and operating leverage are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R8L85-C26-01 | 0.85 | 0.75 | local 4B watch when ad-platform MFE outruns revenue/retention bridge |
| R8L85-C26-02 | 0.35 | 0.30 | ad-tech rebound rejected without ad revenue/take-rate/OP leverage bridge |
| R8L85-C26-03 | 0.35 | 0.30 | reward-ad traffic theme rejected without MAU retention/ad revenue bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_ad_revenue_or_retention_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C26 hard 4C requires confirmed ad-revenue deterioration, MAU/traffic quality collapse, advertiser retention break, take-rate compression, or operating leverage thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L8/C26 platform-ad rows need traffic quality, advertiser retention, ad revenue growth, take-rate and OP leverage before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
candidate_axis = C26_ad_revenue_retention_take_rate_operating_leverage_bridge_required
effect = keep ad-platform positives with local 4B watch; demote ad-tech/reward-ad traffic theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 32.77 | -21.02 | may over-credit ad-platform/AI-ad theme MFE | needs C26 revenue-retention bridge repair |
| P1 canonical shadow bridge profile | 3 | 70.56 on kept positive | demotes 216050/236810 | blocks clean Green until revenue/take-rate/OP leverage repair | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R8L85-C26-01 | 78 | Stage2-Actionable | 74 | Stage2-Actionable + local 4B/ad-revenue bridge watch | partially aligned |
| R8L85-C26-02 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Ad-platform theme RiskWatch | improved |
| R8L85-C26-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Ad-platform theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 3 | no | yes | source repair needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
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
  - ad_platform_theme_false_positive_high_MAE
  - ad_revenue_retention_take_rate_operating_leverage_bridge_required
  - local_4B_late_after_AI_ad_theme_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C26_ad_revenue_retention_take_rate_operating_leverage_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C26_ad_revenue_retention_take_rate_operating_leverage_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

## 23. Validation Scope / Non-Validation Scope

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
- traffic / MAU quality source
- advertiser retention and ad spend recovery
- take-rate and pricing
- operating leverage / margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_ad_revenue_retention_take_rate_operating_leverage_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Require traffic quality, advertiser retention, ad revenue growth, take-rate and operating leverage before clean Stage2/Green","keeps 237820 with local 4B/ad-revenue bridge watch; demotes 216050/236810","R8L85-C26-01-S2A-20240213|R8L85-C26-02-S2FP-20240213|R8L85-C26-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L85-C26-01", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": 85, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE", "case_type": "ad_agency_AI_ad_theme_MFE_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L85-C26-01-S2A-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_theme_MFE_but_local_4B_and_revenue_bridge_required", "current_profile_verdict": "current_profile_4B_too_late_after_AI_ad_theme_MFE", "price_source": "Songdaiki/stock-web", "notes": "C26 can keep Stage2 only when traffic/ad demand converts into advertiser retention, ad revenue, take-rate, cost discipline and operating-margin leverage."}
{"row_type": "trigger", "trigger_id": "R8L85-C26-01-S2A-20240213", "case_id": "R8L85-C26-01", "symbol": "237820", "company_name": "플레이디", "round": "R8", "loop": 85, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail|traffic_to_ad_revenue_take_rate_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "digital ad agency / AI-ad platform / performance-marketing demand proxy; primary ad-revenue, advertiser retention and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["traffic_or_MAU_proxy", "ad_revenue_proxy", "advertiser_retention_proxy"], "stage3_evidence_fields": ["confirmed_MAU_or_traffic_quality", "advertiser_retention", "ad_revenue_growth", "take_rate", "operating_margin_leverage"], "stage4b_evidence_fields": ["ad_platform_MFE_without_revenue_bridge", "AI_ad_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_ad_revenue_or_MAU_retention_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237820/2024.csv", "profile_path": "atlas/symbol_profiles/237/237820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 6250, "MFE_30D_pct": 70.56, "MFE_90D_pct": 70.56, "MFE_180D_pct": 70.56, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.8, "MAE_90D_pct": -6.24, "MAE_180D_pct": -24.96, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-06", "peak_price": 10660, "drawdown_after_peak_pct": -56.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "local_4B_watch_required_when_ad_platform_MFE_outruns_revenue_retention_margin_bridge", "four_b_evidence_type": ["ad_platform_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_ad_revenue_or_retention_break", "trigger_outcome_label": "large_theme_MFE_but_local_4B_and_revenue_bridge_required", "current_profile_verdict": "current_profile_4B_too_late_after_AI_ad_theme_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_no_profile_CA_candidate", "same_entry_group_id": "R8L85-C26-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L85-C26-01", "trigger_id": "R8L85-C26-01-S2A-20240213", "symbol": "237820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"traffic_or_MAU_score": 45, "ad_revenue_growth_score": 40, "advertiser_retention_score": 35, "take_rate_score": 35, "operating_leverage_score": 35, "cost_discipline_score": 35, "revision_score": 35, "relative_strength_score": 75, "theme_blowoff_risk_score": 80, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"traffic_or_MAU_score": 45, "ad_revenue_growth_score": 40, "advertiser_retention_score": 35, "take_rate_score": 35, "operating_leverage_score": 35, "cost_discipline_score": 35, "revision_score": 35, "relative_strength_score": 75, "theme_blowoff_risk_score": 90, "execution_risk_score": 65, "source_quality_score": 10, "4B_watch_score": 85}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + local 4B/ad-revenue bridge watch", "changed_components": ["ad_revenue_growth_score", "advertiser_retention_score", "take_rate_score", "operating_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C26 requires traffic/MAU or ad-demand signal to convert into advertiser retention, ad revenue, take-rate and operating leverage before clean Stage2/Green; AI/ad platform theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 70.56, "MAE_90D_pct": -6.24, "score_return_alignment_label": "large_theme_MFE_but_local_4B_and_revenue_bridge_required", "current_profile_verdict": "current_profile_4B_too_late_after_AI_ad_theme_MFE"}
{"row_type": "case", "case_id": "R8L85-C26-02", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": 85, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE", "case_type": "ad_tech_platform_revenue_rebound_low_MFE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R8L85-C26-02-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_ad_revenue_rebound_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Ad-tech rebound language should remain RiskWatch unless ad spend recovery, advertiser retention, take-rate and OP-margin leverage are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R8L85-C26-02-S2FP-20240213", "case_id": "R8L85-C26-02", "symbol": "216050", "company_name": "인크로스", "round": "R8", "loop": 85, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail|traffic_to_ad_revenue_take_rate_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "ad-tech / media-rep / platform ad-revenue rebound proxy without confirmed advertiser retention, take-rate and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["traffic_or_MAU_proxy", "ad_revenue_proxy", "advertiser_retention_proxy"], "stage3_evidence_fields": ["confirmed_MAU_or_traffic_quality", "advertiser_retention", "ad_revenue_growth", "take_rate", "operating_margin_leverage"], "stage4b_evidence_fields": ["ad_platform_MFE_without_revenue_bridge", "AI_ad_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_ad_revenue_or_MAU_retention_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/216/216050/2024.csv", "profile_path": "atlas/symbol_profiles/216/216050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 10930, "MFE_30D_pct": 4.12, "MFE_90D_pct": 4.12, "MFE_180D_pct": 4.12, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.6, "MAE_90D_pct": -29.55, "MAE_180D_pct": -44.01, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 11380, "drawdown_after_peak_pct": -46.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "ad_tech_rebound_rejected_without_ad_revenue_take_rate_operating_leverage_bridge", "four_b_evidence_type": ["ad_platform_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_ad_revenue_or_retention_break", "trigger_outcome_label": "low_MFE_high_MAE_ad_revenue_rebound_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2022_CA_candidate", "same_entry_group_id": "R8L85-C26-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L85-C26-02", "trigger_id": "R8L85-C26-02-S2FP-20240213", "symbol": "216050", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"traffic_or_MAU_score": 25, "ad_revenue_growth_score": 10, "advertiser_retention_score": 5, "take_rate_score": 5, "operating_leverage_score": 5, "cost_discipline_score": 10, "revision_score": 15, "relative_strength_score": 35, "theme_blowoff_risk_score": 70, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"traffic_or_MAU_score": 25, "ad_revenue_growth_score": 0, "advertiser_retention_score": 0, "take_rate_score": 0, "operating_leverage_score": 0, "cost_discipline_score": 10, "revision_score": 15, "relative_strength_score": 35, "theme_blowoff_risk_score": 70, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Ad-platform theme RiskWatch", "changed_components": ["ad_revenue_growth_score", "advertiser_retention_score", "take_rate_score", "operating_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C26 requires traffic/MAU or ad-demand signal to convert into advertiser retention, ad revenue, take-rate and operating leverage before clean Stage2/Green; AI/ad platform theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 4.12, "MAE_90D_pct": -29.55, "score_return_alignment_label": "low_MFE_high_MAE_ad_revenue_rebound_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "case", "case_id": "R8L85-C26-03", "symbol": "236810", "company_name": "엔비티", "round": "R8", "loop": 85, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE", "case_type": "reward_ad_platform_traffic_monetization_theme_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L85-C26-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "traffic_monetization_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Reward-ad platform MFE is not durable C26 evidence unless MAU retention, advertiser demand, take-rate and operating leverage are visible at entry."}
{"row_type": "trigger", "trigger_id": "R8L85-C26-03-S2FP-20240213", "case_id": "R8L85-C26-03", "symbol": "236810", "company_name": "엔비티", "round": "R8", "loop": 85, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_TECH_AGENCY_REWARD_PLATFORM_TRAFFIC_MONETIZATION_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AI_AD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|platform_ad_revenue_operating_leverage_guardrail|traffic_to_ad_revenue_take_rate_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "reward ad / mobile traffic monetization and platform expansion theme proxy without confirmed MAU retention, advertiser demand and margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["traffic_or_MAU_proxy", "ad_revenue_proxy", "advertiser_retention_proxy"], "stage3_evidence_fields": ["confirmed_MAU_or_traffic_quality", "advertiser_retention", "ad_revenue_growth", "take_rate", "operating_margin_leverage"], "stage4b_evidence_fields": ["ad_platform_MFE_without_revenue_bridge", "AI_ad_theme_blowoff", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_ad_revenue_or_MAU_retention_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv", "profile_path": "atlas/symbol_profiles/236/236810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 7410, "MFE_30D_pct": 23.62, "MFE_90D_pct": 23.62, "MFE_180D_pct": 23.62, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.55, "MAE_90D_pct": -27.26, "MAE_180D_pct": -56.48, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 9160, "drawdown_after_peak_pct": -64.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "reward_ad_traffic_theme_rejected_without_MAU_retention_ad_revenue_margin_bridge", "four_b_evidence_type": ["ad_platform_MFE_without_revenue_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_ad_revenue_or_retention_break", "trigger_outcome_label": "traffic_monetization_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2022_CA_candidates", "same_entry_group_id": "R8L85-C26-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L85-C26-03", "trigger_id": "R8L85-C26-03-S2FP-20240213", "symbol": "236810", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"traffic_or_MAU_score": 25, "ad_revenue_growth_score": 10, "advertiser_retention_score": 5, "take_rate_score": 5, "operating_leverage_score": 5, "cost_discipline_score": 10, "revision_score": 15, "relative_strength_score": 35, "theme_blowoff_risk_score": 70, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"traffic_or_MAU_score": 25, "ad_revenue_growth_score": 0, "advertiser_retention_score": 0, "take_rate_score": 0, "operating_leverage_score": 0, "cost_discipline_score": 10, "revision_score": 15, "relative_strength_score": 35, "theme_blowoff_risk_score": 70, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Ad-platform theme RiskWatch", "changed_components": ["ad_revenue_growth_score", "advertiser_retention_score", "take_rate_score", "operating_leverage_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C26 requires traffic/MAU or ad-demand signal to convert into advertiser retention, ad revenue, take-rate and operating leverage before clean Stage2/Green; AI/ad platform theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 23.62, "MAE_90D_pct": -27.26, "score_return_alignment_label": "traffic_monetization_theme_MFE_then_deep_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE_4B_too_late"}
{"row_type": "shadow_weight", "axis": "C26_ad_revenue_retention_take_rate_operating_leverage_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Platform/ad-revenue rerating requires traffic quality, advertiser retention, ad revenue growth, take-rate and operating leverage; AI/ad-platform theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 237820 with local 4B/ad-revenue bridge watch; demotes 216050/236810 ad-platform theme false positives", "trigger_ids": "R8L85-C26-01-S2A-20240213|R8L85-C26-02-S2FP-20240213|R8L85-C26-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R8", "loop": 85, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["ad_platform_theme_false_positive_high_MAE", "ad_revenue_retention_take_rate_operating_leverage_bridge_required", "local_4B_late_after_AI_ad_theme_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion-ready.
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.
- For C26, test a canonical-archetype guard requiring traffic quality, advertiser retention, ad revenue growth, take-rate and operating leverage before clean Stage2/Green. Keep hard 4C blocked unless a non-price ad-revenue or retention thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 85
next_round = R9
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
