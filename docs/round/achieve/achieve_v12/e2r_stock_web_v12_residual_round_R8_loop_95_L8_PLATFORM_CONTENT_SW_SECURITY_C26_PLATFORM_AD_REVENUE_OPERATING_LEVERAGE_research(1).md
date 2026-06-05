# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R8
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R8_loop_95_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R7 loop 95 is R8 / loop 95. R8 is the L8 platform/content/software/security round, and this run fills C26 platform ad-revenue operating leverage rather than repeating the immediately preceding R8 loop 94 C28 software/security file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 95
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R9
computed_next_loop = 95
```

C26 is an advertising-budget-to-operating-leverage archetype. A platform or ad-tech label is only the billboard; the cash machine is advertiser budget recovery, client retention, traffic monetization, recurring contract quality, take-rate, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE = 13 rows / 10 symbols / good-bad Stage2 2-6 / 4B-4C 0-1
top covered symbols include 042000(2), 214270(2), 237820(2), 030000(1), 035420(1), 035720(1)
previous R8 loop-89 C26 symbols avoided: 067160, 216050, 273060
previous R8 loop-90 C27 symbols avoided: 419530, 408900, 417180
previous R8 loop-91 C28 symbols avoided: 170790, 136540, 356890
previous R8 loop-92 C26 symbols avoided: 042000, 089600, 123570
previous R8 loop-93 C27 symbols avoided: 194480, 035760, 160550
previous R8 loop-94 C28 symbols avoided: 030520, 053800, 434480
previous R7 loop-95 C23 symbols avoided: 000250, 085660, 293780
```

Selected rows avoid hard duplicates and top repeated C26 symbols:

```text
214320 / Stage2-Actionable / 2024-01-17
236810 / Stage2-Actionable / 2024-01-08
417860 / Stage4B / 2024-01-09
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 214320 | atlas/symbol_profiles/214/214320.json | selected 2024 window clean after old 2023 CA candidates |
| 236810 | atlas/symbol_profiles/236/236810.json | selected 2024 window clean after old 2022 CA candidates |
| 417860 | atlas/symbol_profiles/417/417860.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R8L95_C26_INNOCEAN_2024_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_POSITIVE | 214320 | 2024-01-17 | yes | 180 | yes | yes | true |
| R8L95_C26_NBT_2024_REWARD_AD_PLATFORM_FALSE_STAGE2 | 236810 | 2024-01-08 | yes | 180 | yes | yes | true |
| R8L95_C26_OBZEN_2024_AI_MARKETING_SAAS_EVENT_CAP_4B | 417860 | 2024-01-09 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE | Positive Stage2 requires advertiser budget recovery, client retention, channel mix, margin and revision bridge. |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | REWARD_AD_PLATFORM_FALSE_STAGE2 | Reward-ad/traffic monetization watch without budget, retention and margin bridge can become false Stage2. |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | AI_MARKETING_SAAS_EVENT_CAP_4B | AI marketing/ad-tech SaaS event premium should route to 4B when recurring contract and margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R8L95_C26_INNOCEAN_2024_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_POSITIVE | 214320 | 이노션 | positive | Ad-agency/platform operating-leverage bridge produced moderate MFE with shallow early MAE. |
| R8L95_C26_NBT_2024_REWARD_AD_PLATFORM_FALSE_STAGE2 | 236810 | 엔비티 | counterexample | Reward-ad platform premium had short MFE and then high/persistent MAE. |
| R8L95_C26_OBZEN_2024_AI_MARKETING_SAAS_EVENT_CAP_4B | 417860 | 오브젠 | counterexample / 4B | AI marketing/SaaS event premium capped at the January spike and then de-rated deeply. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Innocean ad-agency/platform operating-leverage bridge | historical public/report proxy | true | true | shadow-only positive |
| NBT reward-ad platform false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Obzen AI marketing/SaaS event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 214320 | atlas/ohlcv_tradable_by_symbol_year/214/214320/2024.csv | atlas/symbol_profiles/214/214320.json |
| 236810 | atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv | atlas/symbol_profiles/236/236810.json |
| 417860 | atlas/ohlcv_tradable_by_symbol_year/417/417860/2024.csv | atlas/symbol_profiles/417/417860.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R8L95_C26_INNOCEAN_2024_STAGE2_ACTIONABLE_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE | 214320 | Stage2-Actionable | 2024-01-17 | 20150 | positive | ad-agency/platform operating-leverage bridge worked |
| R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH | 236810 | Stage2-Actionable | 2024-01-08 | 9580 | counterexample | reward-ad platform false Stage2 |
| R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP | 417860 | Stage4B | 2024-01-09 | 28000 | counterexample/4B | AI marketing SaaS event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R8L95_C26_INNOCEAN_2024_STAGE2_ACTIONABLE_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE | 20150 | 13.15 | -1.19 | 20.60 | -1.19 | 20.60 | -2.58 | 2024-05-03 | 24300 | -19.22 |
| R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH | 9580 | 10.65 | -27.35 | 10.65 | -34.97 | 10.65 | -53.76 | 2024-01-08 | 10600 | -56.23 |
| R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP | 28000 | 7.68 | -29.07 | 7.68 | -51.68 | 7.68 | -53.75 | 2024-01-09 | 30150 | -53.75 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C26 Stage2 needs ad-budget / client-retention / traffic monetization / contract quality / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing reward-ad or AI-marketing event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE ad-tech/platform rows cannot promote without durable margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether platform/ad-tech narrative becomes advertiser budget, retention and margin.

| symbol | stage quality | explanation |
|---|---|---|
| 214320 | good_stage2_with_later_watch | Ad-agency operating-leverage bridge produced moderate MFE with shallow MAE. |
| 236810 | bad_stage2 | Reward-ad platform watch lacked budget/retention/margin bridge and had high MAE. |
| 417860 | good_4B | AI marketing event premium capped at the January spike and later suffered deep MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 236810 reward-ad false Stage2 | 0.90 | 0.90 | false Stage2 due missing ad-budget/retention/margin bridge |
| 417860 AI marketing SaaS cap | 0.93 | 0.93 | good full-window 4B timing after January AI/ad-tech event spike |
| 214320 ad agency bridge | n/a | n/a | positive Stage2, but later ad-agency valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 236810 / 417860
```

No hard 4C candidate is proposed. R8 loop 95 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L8 platform/ad-revenue operating-leverage cases, Stage2 requires verified advertiser budget recovery, client retention, traffic monetization, recurring contract quality, take-rate, operating leverage, margin, or revision bridge. Platform, ad-tech, reward ad, AI marketing, SaaS, digital agency or traffic label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rule = C26 should split true advertiser-budget/client-retention/margin positives from reward-ad false Stage2 and AI-marketing event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 12.98 | -29.28 | 0.67 | mixed; C26 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 12.98 | -29.28 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L8 budget/retention/margin bridge required | 2 | 15.63 | -18.08 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C26 bridge vs event-cap split | 2 | 15.63 | -18.08 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing ad-tech/platform themes as positive | 1 | 20.60 | -1.19 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 214320 ad agency bridge | 65 | Stage2-Watch | 73 | Stage2-Actionable | 20.60 | -1.19 | ad_agency_operating_leverage_positive |
| 236810 reward-ad false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 10.65 | -34.97 | reward_ad_platform_false_stage2 |
| 417860 AI marketing cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 7.68 | -51.68 | AI_marketing_SaaS_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C26 Innocean ad-agency operating-leverage positive, NBT reward-ad platform false Stage2, and Obzen AI-marketing SaaS event-cap 4B split while avoiding top repeated C26 symbols and previous R8/R7 loop symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: ad_agency_operating_leverage_positive, reward_ad_platform_false_stage2, AI_marketing_SaaS_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C26 platform ad-revenue operating-leverage bridge vs false Stage2 / event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,C26_requires_ad_budget_client_retention_traffic_monetization_margin_revision_bridge,0,"C26 Stage2 should require advertiser budget recovery, client retention, traffic monetization, recurring contract quality, take-rate, operating leverage, margin, or revision bridge, not platform/ad-tech/AI-marketing label alone","Innocean positive worked; NBT and Obzen event/watch rows failed positive-stage promotion","R8L95_C26_INNOCEAN_2024_STAGE2_ACTIONABLE_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE|R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH|R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,cap_bridge_missing_reward_ad_and_AI_marketing_event_premiums_as_4B_watch,0,"Reward-ad, AI-marketing and ad-tech event premiums can peak before ad budget, contract retention and margin bridge is proven","NBT had short MFE then high MAE; Obzen showed 4B event-cap behavior after January AI-marketing spike","R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH|R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,configured,block_positive_stage_when_ad_platform_theme_has_high_or_persistent_MAE_without_margin_bridge,0,"High or persistent MAE after bridge-missing C26 entries should block Stage2/Stage3 promotion unless advertiser budget, retention and margin evidence survives","NBT MAE90=-34.97 and Obzen MAE90=-51.68","R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH|R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L95_C26_INNOCEAN_2024_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_POSITIVE", "symbol": "214320", "company_name": "이노션", "round": "R8", "loop": "95", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP", "case_type": "moderate_structural_success_with_later_ad_agency_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R8L95_C26_INNOCEAN_2024_STAGE2_ACTIONABLE_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Advertising agency/platform operating-leverage bridge produced moderate MFE with very shallow early MAE. C26 works when platform/ad-revenue narrative maps into advertiser budget recovery, digital/overseas channel mix, client retention, operating leverage, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C26_positive_requires_ad_budget_client_retention_channel_mix_margin_revision_bridge_not_platform_ad_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2023 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R8L95_C26_NBT_2024_REWARD_AD_PLATFORM_FALSE_STAGE2", "symbol": "236810", "company_name": "엔비티", "round": "R8", "loop": "95", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP", "case_type": "failed_rerating_reward_ad_platform_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Reward-ad / platform traffic-monetization watch had only a short event premium and then persistent high MAE. C26 Stage2 should not be awarded without advertiser budget recovery, active user/traffic monetization, retention, take-rate, operating leverage, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_reward_ad_platform_watch_counts_without_ad_budget_retention_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R8L95_C26_OBZEN_2024_AI_MARKETING_SAAS_EVENT_CAP_4B", "symbol": "417860", "company_name": "오브젠", "round": "R8", "loop": "95", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "AI marketing/SaaS personalization event premium capped at the January spike and then de-rated deeply. C26 should route bridge-missing AI marketing/ad-tech platform premiums to 4B unless enterprise contract retention, recurring revenue, advertiser budget, customer expansion, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_AI_marketing_SaaS_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R8L95_C26_INNOCEAN_2024_STAGE2_ACTIONABLE_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE", "case_id": "R8L95_C26_INNOCEAN_2024_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_POSITIVE", "symbol": "214320", "company_name": "이노션", "round": "R8", "loop": "95", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP", "sector": "ad_agency_platform_budget_recovery_operating_leverage", "primary_archetype": "advertiser_budget_client_retention_channel_mix_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-17", "entry_date": "2024-01-17", "entry_price": 20150.0, "evidence_available_at_that_date": "advertiser budget recovery, client-retention quality, digital/overseas channel mix, operating leverage and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["advertiser_budget_recovery_proxy", "client_retention_proxy", "digital_channel_mix_proxy", "operating_leverage_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_ad_agency_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214320/2024.csv", "profile_path": "atlas/symbol_profiles/214/214320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.15, "MFE_90D_pct": 20.6, "MFE_180D_pct": 20.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.19, "MAE_90D_pct": -1.19, "MAE_180D_pct": -2.58, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-03", "peak_price": 24300.0, "drawdown_after_peak_pct": -19.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_ad_agency_valuation_4B_watch_needed", "four_b_evidence_type": ["advertiser_budget_bridge", "client_retention", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_ad_agency_platform_operating_leverage_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2023_CA", "same_entry_group_id": "R8L95_C26_214320_2024-01-17_20150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH", "case_id": "R8L95_C26_NBT_2024_REWARD_AD_PLATFORM_FALSE_STAGE2", "symbol": "236810", "company_name": "엔비티", "round": "R8", "loop": "95", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP", "sector": "reward_ad_platform_traffic_monetization_watch", "primary_archetype": "reward_ad_platform_watch_without_ad_budget_retention_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-08", "entry_date": "2024-01-08", "entry_price": 9580.0, "evidence_available_at_that_date": "reward-ad platform traffic monetization and ad-tech rebound watch without confirmed advertiser budget recovery, take-rate or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["reward_ad_platform_watch", "traffic_monetization_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["short_MFE_then_persistent_MAE", "ad_budget_retention_margin_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/236/236810/2024.csv", "profile_path": "atlas/symbol_profiles/236/236810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.65, "MFE_90D_pct": 10.65, "MFE_180D_pct": 10.65, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.35, "MAE_90D_pct": -34.97, "MAE_180D_pct": -53.76, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-08", "peak_price": 10600.0, "drawdown_after_peak_pct": -56.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "reward_ad_platform_watch_was_false_stage2_due_missing_ad_budget_retention_margin_bridge", "four_b_evidence_type": ["reward_ad_platform_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_reward_ad_platform_watch_without_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_reward_ad_platform_watch_counts_without_ad_budget_retention_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R8L95_C26_236810_2024-01-08_9580", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP", "case_id": "R8L95_C26_OBZEN_2024_AI_MARKETING_SAAS_EVENT_CAP_4B", "symbol": "417860", "company_name": "오브젠", "round": "R8", "loop": "95", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP", "sector": "AI_marketing_SaaS_personalization_event_premium", "primary_archetype": "AI_marketing_SaaS_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-09", "entry_date": "2024-01-09", "entry_price": 28000.0, "evidence_available_at_that_date": "AI marketing/SaaS personalization event premium after January AI/ad-tech spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["AI_marketing_event", "SaaS_personalization_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "contract_retention_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/417/417860/2024.csv", "profile_path": "atlas/symbol_profiles/417/417860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.68, "MFE_90D_pct": 7.68, "MFE_180D_pct": 7.68, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -29.07, "MAE_90D_pct": -51.68, "MAE_180D_pct": -53.75, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-09", "peak_price": 30150.0, "drawdown_after_peak_pct": -53.75, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing_AI_marketing_SaaS_event_cap", "four_b_evidence_type": ["AI_marketing_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_AI_marketing_SaaS_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_AI_marketing_SaaS_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R8L95_C26_417860_2024-01-09_28000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L95_C26_INNOCEAN_2024_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_POSITIVE", "trigger_id": "R8L95_C26_INNOCEAN_2024_STAGE2_ACTIONABLE_AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE", "symbol": "214320", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 65, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 45, "margin_bridge_score": 50, "revision_score": 50, "relative_strength_score": 60, "customer_quality_score": 55, "policy_or_regulatory_score": 0, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "ad_agency_platform_operating_leverage_positive", "MFE_90D_pct": 20.6, "MAE_90D_pct": -1.19, "score_return_alignment_label": "ad_agency_operating_leverage_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L95_C26_NBT_2024_REWARD_AD_PLATFORM_FALSE_STAGE2", "trigger_id": "R8L95_C26_NBT_2024_STAGE2_FALSE_POSITIVE_REWARD_AD_PLATFORM_WATCH", "symbol": "236810", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "reward_ad_platform_false_stage2", "MFE_90D_pct": 10.65, "MAE_90D_pct": -34.97, "score_return_alignment_label": "reward_ad_platform_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_reward_ad_platform_watch_counts_without_ad_budget_retention_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L95_C26_OBZEN_2024_AI_MARKETING_SAAS_EVENT_CAP_4B", "trigger_id": "R8L95_C26_OBZEN_2024_STAGE4B_AI_MARKETING_SAAS_EVENT_CAP", "symbol": "417860", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "AI_marketing_SaaS_event_cap_4B_guard", "MFE_90D_pct": 7.68, "MAE_90D_pct": -51.68, "score_return_alignment_label": "AI_marketing_SaaS_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_AI_marketing_SaaS_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "95", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AD_AGENCY_PLATFORM_OPERATING_LEVERAGE_BRIDGE_VS_REWARD_AD_PLATFORM_FALSE_STAGE2_AND_AI_MARKETING_SAAS_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["ad_agency_operating_leverage_positive", "reward_ad_platform_false_stage2", "AI_marketing_SaaS_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C26 rows need explicit advertiser budget recovery, client retention, traffic monetization, recurring contract quality, take-rate, operating leverage, margin or revision bridge before positive promotion.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that bridge-missing C26 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 95
next_round = R9
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
