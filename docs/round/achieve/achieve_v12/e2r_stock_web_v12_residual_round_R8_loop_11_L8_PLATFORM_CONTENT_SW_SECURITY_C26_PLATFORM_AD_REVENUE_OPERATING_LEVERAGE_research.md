# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R8",
  "scheduled_loop": 11,
  "completed_round": "R8",
  "completed_loop": 11,
  "next_round": "R9",
  "next_loop": 11,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "residual_false_positive_mining",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

This loop adds **3** new independent cases, **2** counterexamples, and **3** residual/current-profile errors for **R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE**.

## 1. Current Calibrated Profile Assumption

Current proxy profile is treated as `e2r_2_1_stock_web_calibrated_proxy`.

Applied global axes assumed present:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The purpose is not to re-prove those global axes. The residual question is narrower:

```text
In C26 platform/ad/commerce/live-streaming cases, when does platform traffic or headline revenue become monetizable operating leverage, and when is it just a price/theme or governance/regulatory overhang?
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R8
scheduled_loop = 11
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG
round_sector_consistency = pass
```

R8 is consistent with L8. C26 is used rather than C27/C28 because all selected cases turn on platform traffic, search/commerce advertising, livestreaming monetization, or platform governance/regulatory permission to monetize.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were not used to inspect source code. The prior generated round state from the immediately preceding v12 output was:

```text
completed_round = R7
completed_loop = 11
next_round = R8
next_loop = 11
```

GitHub code search for `e2r_stock_web_v12_residual_round_R8_loop_11` in `Songdaiki/stock_agent` returned no existing file in the accessible repository index during this run. Therefore this file is treated as the first R8/Loop 11 residual MD.

Duplicate avoidance result:

```text
same_symbol_same_trigger_date_duplicates = 0
same_entry_group_duplicates = 0
new_symbol_count = 3
new_trigger_family_count = 3
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Validation:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

Important caveat: these are raw/unadjusted OHLC rows. Corporate-action candidate windows are blocked by default. None of the representative trigger windows in this MD overlap the profile-level corporate-action candidate dates inspected for SOOP, NAVER, or Kakao.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available by manifest max_date | profile CA overlap in 180D | calibration_usable |
| --- | --- | ---: | --- | --- | --- |
| R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023 | 067160 | 2023-12-07 | yes | no | true |
| R8L11_C26_NAVER_Q1_2024_EARNINGS_COUNTEREXAMPLE | 035420 | 2024-05-03 | yes | no | true |
| R8L11_C26_KAKAO_PLATFORM_REGULATION_2021 | 035720 | 2021-09-08 | yes | no | true |

SOOP profile candidate dates end in 2011, so the 2023-12 to 2024-08 window is clean. NAVER profile candidate dates end in 2018, so the 2024 window is clean. Kakao has a 2021-04-15 profile discontinuity candidate, but the representative 2021-09-08 to 2022-05/06 window does not overlap it.

## 6. Canonical Archetype Compression Map

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  ├─ forced traffic / creator migration to monetizable domestic platform
  ├─ search-platform + commerce earnings with competitive risk
  └─ platform regulatory/governance overhang that blocks take-rate/affiliate expansion optionality
```

This compresses a possible fine-archetype explosion into one canonical C26 rule: **platform scale is only valuable if the monetization rail is durable, legal, and not already neutralized by competition or regulatory overhang.**

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023 | 067160 | SOOP | structural_success | positive | R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07 | current_profile_too_late | traffic migration became a platform monetization/operating-leverage path; early evidence had much better MFE/MAE than waiting for confirmed earnings |
| R8L11_C26_NAVER_Q1_2024_EARNINGS_COUNTEREXAMPLE | 035420 | NAVER | failed_rerating | counterexample | R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03 | current_profile_false_positive | headline platform/search/commerce earnings were real, but competitive e-commerce and AI-cost/multiple overhang kept the rerating from holding |
| R8L11_C26_KAKAO_PLATFORM_REGULATION_2021 | 035720 | 카카오 | 4C_success | counterexample | R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08 | current_profile_4C_too_late | platform ecosystem scale could not protect the stock once regulatory/governance trust became the dominant evidence family |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
4B_case_count = 1
4C_case_count = 1
new_independent_case_count = 3
```

Balance is sufficient for a shadow-only C26 rule candidate. It is not sufficient for a global profile change.

## 9. Evidence Source Map

| case_id | evidence family | source note |
| --- | --- | --- |
| SOOP migration | Twitch Korea exit / forced creator-user migration / domestic monetization rail | Twitch Korea exit was announced for February 27, 2024; stock-web rows show the immediate 2023-12-06/07 reaction and later full-window peak. |
| NAVER earnings | search-platform advertising + e-commerce earnings, but competitive/multiple risk | Q1 2024 report showed revenue and operating profit growth, e-commerce/search-platform growth, and competition from AliExpress/Temu. |
| Kakao regulation | platform regulatory/governance thesis break | Used as C26 regulatory/governance overhang example; the price path shows the collapse from a platform premium regime into a de-risking regime. |

External source URLs used for narrative grounding:

```text
- https://en.wikipedia.org/wiki/Twitch_(service)
- https://www.wsj.com/articles/naver-1q-rev-krw2-526t-vs-krw2-280t-035420-se-666b7aff
- https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/
- https://www.reuters.com/business/south-korea-court-decide-arrest-warrant-kakao-founder-2024-07-22/
```

## 10. Price Data Source Map

| symbol | company | profile_path | price shards used | profile caveat |
| --- | --- | --- | --- | --- |
| 067160 | SOOP | atlas/symbol_profiles/067/067160.json | 2023.csv, 2024.csv | raw/unadjusted; CA candidates not in tested window |
| 035420 | NAVER | atlas/symbol_profiles/035/035420.json | 2024.csv | raw/unadjusted; CA candidates not in tested window |
| 035720 | 카카오 | atlas/symbol_profiles/035/035720.json | 2021.csv, 2022.csv | raw/unadjusted; 2021-04-15 CA candidate outside tested window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | current_profile_verdict | trigger_outcome_label | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07 | 067160 | Stage2-Actionable | 2023-12-06 | 2023-12-07 | 76600 | 45.43 | 82.25 | 87.73 | -6.01 | -6.01 | -6.01 | 2024-07-11 | 143800 | current_profile_too_late | structural_success_high_MFE_clean_180D | True |
| R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26 | 067160 | Stage3-Green | 2024-04-26 | 2024-04-26 | 122200 | 3.03 | 17.68 | 17.68 | -15.38 | -15.63 | -15.63 | 2024-07-11 | 143800 | current_profile_too_late | late_green_still_positive_but_high_MAE | False |
| R8L11_C26_SOOP_T3_4B_OVERLAY_2024-02-28 | 067160 | Stage4B-Overlay | 2024-02-28 | 2024-02-28 | 129900 | 7.47 | 7.47 | 10.7 | -17.86 | -20.63 | -20.63 | 2024-07-11 | 143800 | current_profile_correct | 4B_overlay_success_not_full_window_exit | False |
| R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03 | 035420 | Stage2-Actionable | 2024-05-03 | 2024-05-03 | 194600 | 2.0 | 2.0 | 2.0 | -14.7 | -22.35 | -22.35 | 2024-05-07 | 198500 | current_profile_false_positive | failed_rerating_high_MAE | True |
| R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08 | 035720 | Stage4C-ThesisBreak | 2021-09-08 | 2021-09-08 | 138500 | 9.39 | 9.39 | 9.39 | -20.22 | -36.97 | -42.24 | 2021-09-08 | 151500 | current_profile_4C_too_late | 4C_success_platform_regulatory_break | True |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger table

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | current_profile_verdict | trigger_outcome_label | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07 | 067160 | Stage2-Actionable | 2023-12-06 | 2023-12-07 | 76600 | 45.43 | 82.25 | 87.73 | -6.01 | -6.01 | -6.01 | 2024-07-11 | 143800 | current_profile_too_late | structural_success_high_MFE_clean_180D | True |
| R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03 | 035420 | Stage2-Actionable | 2024-05-03 | 2024-05-03 | 194600 | 2.0 | 2.0 | 2.0 | -14.7 | -22.35 | -22.35 | 2024-05-07 | 198500 | current_profile_false_positive | failed_rerating_high_MAE | True |
| R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08 | 035720 | Stage4C-ThesisBreak | 2021-09-08 | 2021-09-08 | 138500 | 9.39 | 9.39 | 9.39 | -20.22 | -36.97 | -42.24 | 2021-09-08 | 151500 | current_profile_4C_too_late | 4C_success_platform_regulatory_break | True |

### 12.2 SOOP label comparison / 4B overlay

The SOOP case is the important positive residual. Stage2-Actionable on 2023-12-07 had the cleanest MFE/MAE profile. Waiting until April 2024 for Green confirmation still worked, but it consumed roughly **67.9%** of the upside from the Stage2 entry to the full observed peak.

```text
SOOP Stage2 entry = 76,600
SOOP Stage3-Green comparison entry = 122,200
SOOP full-window peak = 143,800
green_lateness_ratio = (122,200 - 76,600) / (143,800 - 76,600) = 0.679
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | verdict | why |
| --- | --- | --- | --- |
| SOOP | Stage2/Yellow, Green only after conversion evidence | current_profile_too_late | the forced migration was monetizable earlier than confirmed earnings; late Green missed most upside |
| NAVER | Yellow / near Green from real earnings | current_profile_false_positive | headline earnings were real, but MFE was thin and MAE was large |
| Kakao | 4B/4C only after risk became obvious | current_profile_4C_too_late | platform regulatory/governance shock should cap positive labels immediately |

Axis answers:

```text
stage2_actionable_evidence_bonus: useful for SOOP; too permissive for NAVER if used on headline earnings alone.
yellow_threshold_75: acceptable but needs C26 guard fields.
green_threshold_87 / revision_min_55: too late for direct forced-migration monetization; too permissive if headline EPS lacks durability.
price_only_blowoff_guard: kept; SOOP 4B remains overlay-only unless non-price deterioration appears.
full_4b_non_price_requirement: kept.
hard_4c_routing: strengthened for platform-regulatory thesis breaks.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable timing | Green timing | comparison |
| --- | --- | --- | --- |
| SOOP | 2023-12-07 at 76,600 | 2024-04-26 at 122,200 | Green late; Stage2 captured the migration wedge |
| NAVER | 2024-05-03 at 194,600 | no clean Green | headline earnings should not become Green |
| Kakao | n/a | n/a | positive labels should be blocked by 4C route |

## 15. 4B Local vs Full-window Timing Audit

SOOP price-only 4B overlay:

```text
Stage2_Actionable entry = 76,600
4B overlay entry = 129,900
local_peak_after_stage2 = 139,600
full_window_peak_after_stage2 = 143,800

four_b_local_peak_proximity = 0.846
four_b_full_window_peak_proximity = 0.793
four_b_timing_verdict = price_only_local_4B_not_full_exit
```

The existing full-4B non-price requirement is kept. The 4B row is useful as a risk overlay, not a production exit proof.

## 16. 4C Protection Audit

Kakao is the hard 4C example.

```text
entry_price = 138,500
MFE_180D_pct = +9.39
MAE_180D_pct = -42.24
1Y observed low proxy = 66,200
drawdown_after_peak_pct = -56.30
four_c_protection_label = hard_4c_success
```

The lesson is not “every platform controversy is 4C.” The threshold is narrower: when the evidence attacks take-rate legality, affiliate expansion, financial optionality, or governance trust, the case stops being a positive operating-leverage setup.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L8_C26_PLATFORM_MONETIZATION_RISK_SPLIT

Positive promotion:
  +2 shadow bonus if a traffic migration event is forced, external, and maps directly into the subject company's monetization rail.

Negative cap:
  cap at Stage2/Yellow if platform earnings are headline-positive but durable traffic retention, operating leverage, and competitive pressure are unresolved.

Hard risk:
  route to 4B/4C if platform regulatory/governance evidence directly attacks take-rate, affiliate expansion, financial optionality, or user trust.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

C26 should distinguish:
1. monetizable forced migration,
2. ordinary traffic / MAU / headline revenue growth,
3. positive earnings with competitive multiple risk,
4. platform-regulatory thesis break.
```

This is canonical-specific, not global. It should not affect C27 content IP or C28 security contract retention unless future R8 loops independently reproduce the same pattern.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | current profile catches global lateness rules but over-promotes headline platform earnings and underweights direct traffic migration option value. | none | 31.21 | -21.78 | 33.04 | -23.53 | 2/3 | 1 | 1 | mixed |
| P0b_e2r_2_0_baseline_reference | rollback_reference | old baseline would be more easily pulled into price/scale narratives. | rollback only | 31.21 | -21.78 | 33.04 | -23.53 | 2/3+ | 1 | 1 | worse |
| P1_L8_sector_specific_candidate_profile | sector_specific | Platform traffic migration earns early Stage2 bonus only when monetizable destination, creator/customer migration route, and take-rate economics are observable. | traffic_migration_monetization_boost + regulatory_overhang_guard | 31.21 | -21.78 | 33.04 | -23.53 | 1/3 | 0 | 0 | improved |
| P2_C26_canonical_candidate_profile | canonical_archetype_specific | Headline ad/commerce revenue gets capped below Green unless operating leverage, traffic retention, and competitive pressure are all resolved. | headline_earnings_green_cap + direct_migration_stage2_boost | 31.21 | -21.78 | 33.04 | -23.53 | 1/3 | 0 | 0 | improved |
| P3_C26_counterexample_guard_profile | guard | Regulatory/governance platform pressure routes to 4B/4C even if user scale remains intact. | platform_regulatory_thesis_break_guard | 31.21 | -21.78 | 33.04 | -23.53 | 0-1/3 | 0 | 0 | best guard |

## 20. Score-Return Alignment Matrix

| trigger_id | score before | label before | score after | label after | MFE_90D | MAE_90D | alignment |
| --- | ---: | --- | ---: | --- | ---: | ---: | --- |
| R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07 | 76 | Stage3-Yellow | 84 | Stage2-Actionable/early C26 Yellow, not full Green until conversion evidence | 82.25 | -6.01 | structural_success_high_MFE_clean_180D |
| R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26 | 88 | Stage3-Green | 88 | Stage3-Green but late | 17.68 | -15.63 | late_green_still_positive_but_high_MAE |
| R8L11_C26_SOOP_T3_4B_OVERLAY_2024-02-28 | 80 | 4B-watch | 80 | 4B-overlay-only | 7.47 | -20.63 | 4B_overlay_success_not_full_window_exit |
| R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03 | 82 | Stage3-Yellow/near-Green | 71 | Stage2-Actionable only / Green blocked | 2.0 | -22.35 | failed_rerating_high_MAE |
| R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08 | 82 | Stage3-Yellow/Green-risk | 49 | 4C-ThesisBreak | 9.39 | -36.97 | 4C_success_platform_regulatory_break |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG | 1 | 2 | 1 | 1 | 3 | 0 | 5 | 3 | 3 | True | True | C26 now has direct migration positive + headline earnings failed-rerating + regulatory/governance thesis-break counterexample; still needs non-KR overseas platform holdout. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late
  - current_profile_false_positive
  - current_profile_4C_too_late
  - high_MAE_after_headline_earnings
new_axis_proposed:
  - c26_direct_monetizable_traffic_migration_bonus
  - c26_headline_platform_earnings_green_cap
  - c26_platform_regulatory_governance_4c_guard
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus, but only where migration is monetizable
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened:
  - stage3_green_total_min / revision_min only for C26 forced monetizable migration cases; not globally
existing_axis_kept:
  - price-only blowoff guard
  - full 4B non-price requirement
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web tradable OHLC rows for 067160, 035420, 035720
- profile-level corporate action candidate windows
- 30D / 90D / 180D MFE and MAE direction
- Green lateness for SOOP
- price-only 4B overlay vs full-window peak split
- platform-regulatory 4C guard candidate
```

Not validated:

```text
- production scoring code
- live watchlist
- current investment attractiveness
- brokerage execution
- global rule promotion
- exact intraday evidence timestamps beyond public-event date
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_direct_monetizable_traffic_migration_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,"0","2","+2","SOOP shows that a platform receiving a forced migration of creators/users can produce early upside before confirmed earnings if monetization rails are native and observable.","reduces missed structural count from 1 to 0 without promoting NAVER/Kakao.","R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07",3,3,2,medium_low,canonical_archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_headline_platform_earnings_green_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,"none","cap Green unless durable traffic retention + operating leverage + competitive risk resolved","new_guard","NAVER Q1 2024 had real earnings but poor forward MFE/MAE; earnings alone should stay Stage2/Yellow.","blocks one false positive Green-like promotion.","R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03",3,3,2,medium,canonical_archetype_shadow_only,"not production; no global threshold change"
shadow_weight,c26_platform_regulatory_governance_4c_guard,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,"soft legal risk","hard 4C route when platform take-rate/affiliate expansion/financial optionality is directly attacked","strengthen_4C_route","Kakao platform-regulatory shock had severe MAE and should not be treated as ordinary valuation compression.","routes dominant non-price regulatory thesis break away from positive Stage labels.","R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08",3,3,2,medium_low,sector_shadow_only,"not production; historical calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "symbol": "067160", "company_name": "SOOP", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "traffic migration became a platform monetization/operating-leverage path; early evidence had much better MFE/MAE than waiting for confirmed earnings", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Twitch Korea exit created a discrete supply-side creator/user migration shock. SOOP/AfreecaTV was not merely a theme; its own platform could absorb streamers and virtual-gift/ad monetization."}
{"row_type": "case", "case_id": "R8L11_C26_NAVER_Q1_2024_EARNINGS_COUNTEREXAMPLE", "symbol": "035420", "company_name": "NAVER", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "headline platform/search/commerce earnings were real, but competitive e-commerce and AI-cost/multiple overhang kept the rerating from holding", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Positive operating profit and platform/search/commerce data should not be enough for Green when margin durability and valuation overhang are unresolved."}
{"row_type": "case", "case_id": "R8L11_C26_KAKAO_PLATFORM_REGULATION_2021", "symbol": "035720", "company_name": "카카오", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "platform ecosystem scale could not protect the stock once regulatory/governance trust became the dominant evidence family", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "This is used as a hard platform-regulatory thesis-break example, not as a live view on Kakao."}
```

### 25.3 trigger rows

```jsonl
{"trigger_id": "R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "symbol": "067160", "company_name": "SOOP", "sector": "platform_live_streaming", "primary_archetype": "creator/user traffic migration to monetizable domestic platform", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-06", "entry_date": "2023-12-07", "entry_price": 76600, "evidence_available_at_that_date": "Twitch announced Korea exit; SOOP/AfreecaTV was an immediately investable domestic livestreaming platform beneficiary. Entry uses next tradable close after the first spike because the event was absorbed intraday on 2023-12-06.", "evidence_source": "Twitch Korea exit public announcement; stock-web rows 2023-12-06/07 and 2024 follow-through.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": ["repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv|atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "MFE_30D_pct": 45.43, "MFE_90D_pct": 82.25, "MFE_180D_pct": 87.73, "MFE_1Y_pct": 87.73, "MFE_2Y_pct": null, "MAE_30D_pct": -6.01, "MAE_90D_pct": -6.01, "MAE_180D_pct": -6.01, "MAE_1Y_pct": -6.01, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 143800, "drawdown_after_peak_pct": -27.0, "green_lateness_ratio": "not_applicable_stage2_base", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_clean_180D", "current_profile_verdict": "current_profile_too_late", "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C26_SOOP_2023-12-07_76600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 16, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable/early C26 Yellow, not full Green until conversion evidence", "row_type": "trigger", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true}
{"trigger_id": "R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "symbol": "067160", "company_name": "SOOP", "sector": "platform_live_streaming", "primary_archetype": "confirmed conversion / monetization after migration", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 122200, "evidence_available_at_that_date": "By late April 2024, the market had more evidence that migration had not been a one-day traffic shock. Waiting this long, however, spent a large portion of the upside from the December entry.", "evidence_source": "stock-web price confirmation row and post-migration platform monetization narrative.", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "MFE_30D_pct": 3.03, "MFE_90D_pct": 17.68, "MFE_180D_pct": 17.68, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.38, "MAE_90D_pct": -15.63, "MAE_180D_pct": -15.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 143800, "drawdown_after_peak_pct": -27.0, "green_lateness_ratio": 0.679, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_still_positive_but_high_MAE", "current_profile_verdict": "current_profile_too_late", "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C26_SOOP_2024-04-26_122200", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case used only for Green lateness audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green but late", "row_type": "trigger", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true}
{"trigger_id": "R8L11_C26_SOOP_T3_4B_OVERLAY_2024-02-28", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "symbol": "067160", "company_name": "SOOP", "sector": "platform_live_streaming", "primary_archetype": "post-migration valuation/positioning overlay", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-02-28", "entry_date": "2024-02-28", "entry_price": 129900, "evidence_available_at_that_date": "Price had already repriced sharply into the migration story. Non-price deterioration was not yet strong enough for a full 4B exit; it is treated as a risk overlay.", "evidence_source": "stock-web 2024-02-28 row; price/positioning-only 4B audit.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "MFE_30D_pct": 7.47, "MFE_90D_pct": 7.47, "MFE_180D_pct": 10.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.86, "MAE_90D_pct": -20.63, "MAE_180D_pct": -20.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 143800, "drawdown_after_peak_pct": -27.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.846, "four_b_full_window_peak_proximity": 0.793, "four_b_timing_verdict": "price_only_local_4B_not_full_exit", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success_not_full_window_exit", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C26_SOOP_2024-02-28_129900", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used only for 4B timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "4B-overlay-only", "row_type": "trigger", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true}
{"trigger_id": "R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03", "case_id": "R8L11_C26_NAVER_Q1_2024_EARNINGS_COUNTEREXAMPLE", "symbol": "035420", "company_name": "NAVER", "sector": "search_commerce_platform", "primary_archetype": "headline platform/search-commerce earnings without durable rerating", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-03", "entry_date": "2024-05-03", "entry_price": 194600, "evidence_available_at_that_date": "NAVER reported strong Q1 2024 earnings with search-platform advertising and e-commerce growth, but competition and future AI/cost pressure meant the score should not promote to Green on headline EPS alone.", "evidence_source": "WSJ/FactSet earnings article; stock-web 2024-05-03 and forward rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "MFE_30D_pct": 2.0, "MFE_90D_pct": 2.0, "MFE_180D_pct": 2.0, "MFE_1Y_pct": 2.0, "MFE_2Y_pct": null, "MAE_30D_pct": -14.7, "MAE_90D_pct": -22.35, "MAE_180D_pct": -22.35, "MAE_1Y_pct": -22.35, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 198500, "drawdown_after_peak_pct": -23.88, "green_lateness_ratio": "not_applicable_no_green", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "headline_earnings_not_enough_for_positive_stage", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C26_NAVER_2024-05-03_194600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 18, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/near-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 16, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -8, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable only / Green blocked", "row_type": "trigger", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true}
{"trigger_id": "R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08", "case_id": "R8L11_C26_KAKAO_PLATFORM_REGULATION_2021", "symbol": "035720", "company_name": "카카오", "sector": "messenger_fintech_platform", "primary_archetype": "platform-regulatory thesis break", "trigger_type": "Stage4C-ThesisBreak", "trigger_date": "2021-09-08", "entry_date": "2021-09-08", "entry_price": 138500, "evidence_available_at_that_date": "Kakao's platform/fintech expansion premium was hit by Korean platform-regulatory and governance scrutiny. The event family is not price-only; it attacks permissible take rate, affiliate expansion, and financial-platform optionality.", "evidence_source": "public platform-regulatory scrutiny; stock-web 2021-09-08 and 2022 forward rows.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "explicit_event_cap", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["regulatory_rejection", "accounting_or_trust_break", "thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv|atlas/ohlcv_tradable_by_symbol_year/035/035720/2022.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "MFE_30D_pct": 9.39, "MFE_90D_pct": 9.39, "MFE_180D_pct": 9.39, "MFE_1Y_pct": 9.39, "MFE_2Y_pct": null, "MAE_30D_pct": -20.22, "MAE_90D_pct": -36.97, "MAE_180D_pct": -42.24, "MAE_1Y_pct": -52.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-09-08", "peak_price": 151500, "drawdown_after_peak_pct": -56.3, "green_lateness_ratio": "not_applicable_4C", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4c_thesis_break_route", "four_b_evidence_type": ["legal_or_regulatory_block", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success_platform_regulatory_break", "current_profile_verdict": "current_profile_4C_too_late", "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R8L11_C26_KAKAO_2021-09-08_138500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": 0, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/Green-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 10, "policy_or_regulatory_score": -16, "valuation_repricing_score": 6, "execution_risk_score": -10, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -8}, "weighted_score_after": 49, "stage_label_after": "4C-ThesisBreak", "row_type": "trigger", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "TRAFFIC_MIGRATION_AD_COMMERCE_OPERATING_LEVERAGE_VS_REGULATORY_PLATFORM_OVERHANG", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "trigger_id": "R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 16, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable/early C26 Yellow, not full Green until conversion evidence", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 82.25, "MAE_90D_pct": -6.01, "score_return_alignment_label": "structural_success_high_MFE_clean_180D", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "trigger_id": "R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 16, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable/early C26 Yellow, not full Green until conversion evidence", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 82.25, "MAE_90D_pct": -6.01, "score_return_alignment_label": "structural_success_high_MFE_clean_180D", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "trigger_id": "R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 16, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable/early C26 Yellow, not full Green until conversion evidence", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 82.25, "MAE_90D_pct": -6.01, "score_return_alignment_label": "structural_success_high_MFE_clean_180D", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "trigger_id": "R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 16, "customer_quality_score": 10, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 14, "policy_or_regulatory_score": 10, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable/early C26 Yellow, not full Green until conversion evidence", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 82.25, "MAE_90D_pct": -6.01, "score_return_alignment_label": "structural_success_high_MFE_clean_180D", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "trigger_id": "R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green but late", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 17.68, "MAE_90D_pct": -15.63, "score_return_alignment_label": "late_green_still_positive_but_high_MAE", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "trigger_id": "R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green but late", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 17.68, "MAE_90D_pct": -15.63, "score_return_alignment_label": "late_green_still_positive_but_high_MAE", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "trigger_id": "R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green but late", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 17.68, "MAE_90D_pct": -15.63, "score_return_alignment_label": "late_green_still_positive_but_high_MAE", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R8L11_C26_SOOP_TWITCH_EXIT_MIGRATION_2023", "trigger_id": "R8L11_C26_SOOP_T2_STAGE3_GREEN_CONFIRMATION_2024-04-26", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 14, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green but late", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 17.68, "MAE_90D_pct": -15.63, "score_return_alignment_label": "late_green_still_positive_but_high_MAE", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C26_NAVER_Q1_2024_EARNINGS_COUNTEREXAMPLE", "trigger_id": "R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 18, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/near-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 16, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -8, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable only / Green blocked", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 2.0, "MAE_90D_pct": -22.35, "score_return_alignment_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R8L11_C26_NAVER_Q1_2024_EARNINGS_COUNTEREXAMPLE", "trigger_id": "R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 18, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/near-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 16, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -8, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable only / Green blocked", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 2.0, "MAE_90D_pct": -22.35, "score_return_alignment_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R8L11_C26_NAVER_Q1_2024_EARNINGS_COUNTEREXAMPLE", "trigger_id": "R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 18, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/near-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 16, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -8, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable only / Green blocked", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 2.0, "MAE_90D_pct": -22.35, "score_return_alignment_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R8L11_C26_NAVER_Q1_2024_EARNINGS_COUNTEREXAMPLE", "trigger_id": "R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 18, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/near-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 16, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -8, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable only / Green blocked", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 2.0, "MAE_90D_pct": -22.35, "score_return_alignment_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L11_C26_KAKAO_PLATFORM_REGULATION_2021", "trigger_id": "R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": 0, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/Green-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 10, "policy_or_regulatory_score": -16, "valuation_repricing_score": 6, "execution_risk_score": -10, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -8}, "weighted_score_after": 49, "stage_label_after": "4C-ThesisBreak", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 9.39, "MAE_90D_pct": -36.97, "score_return_alignment_label": "4C_success_platform_regulatory_break", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R8L11_C26_KAKAO_PLATFORM_REGULATION_2021", "trigger_id": "R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": 0, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/Green-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 10, "policy_or_regulatory_score": -16, "valuation_repricing_score": 6, "execution_risk_score": -10, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -8}, "weighted_score_after": 49, "stage_label_after": "4C-ThesisBreak", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 9.39, "MAE_90D_pct": -36.97, "score_return_alignment_label": "4C_success_platform_regulatory_break", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R8L11_C26_KAKAO_PLATFORM_REGULATION_2021", "trigger_id": "R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": 0, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/Green-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 10, "policy_or_regulatory_score": -16, "valuation_repricing_score": 6, "execution_risk_score": -10, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -8}, "weighted_score_after": 49, "stage_label_after": "4C-ThesisBreak", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 9.39, "MAE_90D_pct": -36.97, "score_return_alignment_label": "4C_success_platform_regulatory_break", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R8L11_C26_KAKAO_PLATFORM_REGULATION_2021", "trigger_id": "R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": 0, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/Green-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 4, "customer_quality_score": 10, "policy_or_regulatory_score": -16, "valuation_repricing_score": 6, "execution_risk_score": -10, "legal_or_contract_risk_score": -18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -8}, "weighted_score_after": 49, "stage_label_after": "4C-ThesisBreak", "changed_components": ["policy_or_regulatory_score", "revision_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Shadow-only C26 profile separates monetizable traffic migration from headline earnings and regulatory/governance platform overhang.", "MFE_90D_pct": 9.39, "MAE_90D_pct": -36.97, "score_return_alignment_label": "4C_success_platform_regulatory_break", "current_profile_verdict": "current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows

```jsonl
{"row_type": "shadow_weight", "axis": "c26_direct_monetizable_traffic_migration_bonus", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "baseline_value": 0, "tested_value": 2, "delta": "+2", "reason": "SOOP shows that a platform receiving a forced migration of creators/users can produce early upside before confirmed earnings if monetization rails are native and observable.", "backtest_effect": "reduces missed structural count from 1 to 0 without promoting NAVER/Kakao.", "trigger_ids": "R8L11_C26_SOOP_T1_STAGE2_ACTIONABLE_2023-12-07", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "medium_low", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "shadow_weight", "axis": "c26_headline_platform_earnings_green_cap", "scope": "canonical_archetype_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "baseline_value": "none", "tested_value": "cap Green unless durable traffic retention + operating leverage + competitive risk resolved", "delta": "new_guard", "reason": "NAVER Q1 2024 had real earnings but poor forward MFE/MAE; earnings alone should stay Stage2/Yellow.", "backtest_effect": "blocks one false positive Green-like promotion.", "trigger_ids": "R8L11_C26_NAVER_T1_STAGE2_EARNINGS_2024-05-03", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; no global threshold change"}
{"row_type": "shadow_weight", "axis": "c26_platform_regulatory_governance_4c_guard", "scope": "sector_specific", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "baseline_value": "soft legal risk", "tested_value": "hard 4C route when platform take-rate/affiliate expansion/financial optionality is directly attacked", "delta": "strengthen_4C_route", "reason": "Kakao platform-regulatory shock had severe MAE and should not be treated as ordinary valuation compression.", "backtest_effect": "routes dominant non-price regulatory thesis break away from positive Stage labels.", "trigger_ids": "R8L11_C26_KAKAO_T1_REGULATORY_4C_2021-09-08", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "medium_low", "proposal_type": "sector_shadow_only", "notes": "not production; historical calibration only"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R8", "loop": "11", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late", "current_profile_false_positive", "current_profile_4C_too_late", "high_MAE_after_headline_earnings"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
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
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
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
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 11
next_round = R9
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files inspected:

```text
https://github.com/Songdaiki/stock-web/blob/main/atlas/manifest.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/067/067160.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/035/035420.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/035/035420/2024.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/035/035720.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/035/035720/2022.csv
```

External narrative sources used only for trigger evidence context:

```text
Twitch Korea exit:
https://en.wikipedia.org/wiki/Twitch_(service)

NAVER Q1 2024 earnings:
https://www.wsj.com/articles/naver-1q-rev-krw2-526t-vs-krw2-280t-035420-se-666b7aff

Kakao platform/governance regulatory overhang context:
https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/
https://www.reuters.com/business/south-korea-court-decide-on-arrest-warrant-for-kakao-founder-2024-07-22/
```
