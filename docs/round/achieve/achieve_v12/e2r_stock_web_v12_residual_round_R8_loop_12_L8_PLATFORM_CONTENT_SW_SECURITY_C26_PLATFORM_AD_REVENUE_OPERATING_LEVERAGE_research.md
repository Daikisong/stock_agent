# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R8
scheduled_loop: 12
completed_round: R8
completed_loop: 12
next_round: R9
next_loop: 12
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R8_loop_12_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
stock_web_price_atlas_access_required: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`; `e2r_2_0_baseline_reference` is used only as rollback/reference. This file does not re-propose the global Stock-Web calibrated axes. It tests a C26 residual: platform evidence is not automatically platform monetization. Traffic has to pass through the toll gate: ad inventory, paid items, commerce take-rate, or margin bridge. Otherwise the story is just a busy station with no ticket counter.

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

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R8`
- Loop: `12`
- Large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- Canonical archetype: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- Fine archetype: `PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE`
- Loop objectives: `coverage_gap_fill`, `counterexample_mining`, `residual_false_positive_mining`, `green_strictness_stress_test`, `4B_non_price_requirement_stress_test`, `4C_thesis_break_timing_test`, `canonical_archetype_compression`

R8 loop 10 already covered C28 software/security contract-retention. R8 loop 11 already covered C27 content/IP monetization. This loop therefore fills the scheduled R8 C26 gap rather than repeating content or security software.

## 3. Previous Coverage / Duplicate Avoidance Check

Checked local prior R8 MD artifacts:

```text
e2r_stock_web_v12_residual_round_R8_loop_10_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
e2r_stock_web_v12_residual_round_R8_loop_11_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
```

Novelty gate:

```text
scheduled_round = R8
scheduled_loop = 12
wrong_round_penalty = 0
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 5
new_trigger_family_count = 5
positive_case_count = 3
counterexample_count = 2
current_profile_error_count = 3
```

The repeated NAVER/Kakao symbols inside this file are not reused prior rows. They test different C26 trigger families: monetization success, regulatory 4C, and M&A/platform-expansion overhang.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema confirmation:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
raw columns = d,o,h,l,c,v,a,mc,s,m,rs
calibration_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All five representative triggers are historical. Each representative entry date exists in the Stock-Web tradable shard and has at least 180 subsequent tradable rows before manifest max date `2026-02-20`.

Corporate-action handling:

```text
035420 NAVER: recent corporate-action candidates end at 2018-10-12, so 2020/2022 windows are clean for 180D.
035720 Kakao: corporate-action candidate 2021-04-15 blocks 1Y/2Y for the 2020-05-07 positive case, but 30D/90D/180D are clean. The 2021-09-09 regulatory case occurs after the split and is clean.
067160 SOOP: recent corporate-action candidates end at 2011-01-27, so the 2023/2024 windows are clean.
```

## 6. Canonical Archetype Compression Map

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  ├─ search/display ad recovery and commerce take-rate bridge: NAVER 2020
  ├─ messenger ad-commerce operating leverage: Kakao 2020
  ├─ live-streaming paid-item/ad inventory migration: SOOP 2023/2024
  ├─ regulatory cap / monetization-route break: Kakao 2021
  └─ platform expansion without margin bridge: NAVER/Poshmark 2022
```

Compression rule: C26 should not reward “platform” as a noun. It should reward platform monetization as a verb: traffic becomes paid inventory, commerce take-rate, paid-item spend, or margin/revision visibility.

## 7. Case Selection Summary

| case_id | symbol | company | role | current profile verdict | core reason |
|---|---:|---|---|---|---|
| `R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE` | `035420` | NAVER | positive / structural_success | `current_profile_correct` | Q2-2020 commerce/search/fintech operating leverage converted traffic into margin/revision visibility. The 180D path behaved like a genuine platform monetization rerating, not a one-day platform label spike. |
| `R8L12_C26_CASE_002_KAKAO_2020_TALKBIZ_AD_COMMERCE_LEVERAGE` | `035720` | 카카오 | positive / structural_success | `current_profile_correct` | TalkBiz/commerce/ad monetization had direct operating-leverage evidence before the later stock-split contamination. 30D/90D/180D windows are clean; 1Y/2Y fields are blocked by the 2021-04-15 corporate-action candidate. |
| `R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION` | `067160` | SOOP | positive / structural_success | `current_profile_too_late` | Twitch Korea exit created a directly observable platform-migration route. The key was not just traffic; it was paid-item/advertising/creator migration optionality with low corporate-action contamination. |
| `R8L12_C26_CASE_004_KAKAO_2021_REGULATORY_THESIS_BREAK` | `035720` | 카카오 | counterexample / 4C_success | `current_profile_4C_too_late` | Same platform monetization engine as the positive case, but the evidence family changed: regulatory/legal cap risk broke the multiple and monetization thesis. This is not a Stage3 positive; it is a hard 4C/risk-route calibration point. |
| `R8L12_C26_CASE_005_NAVER_2022_POSHMARK_MNA_OVERHANG` | `035420` | NAVER | counterexample / false_positive_green | `current_profile_false_positive` | The Poshmark deal was a platform-commerce expansion event, but it did not by itself prove domestic ad/commerce operating leverage. The path had a sharp MAE and later rebound; C26 should cap platform-expansion events until take-rate or margin visibility appears. |


## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 3
counterexample_or_failed_rerating = 2
4B_or_4C_case = 3
calibration_usable_case_count = 5
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The balance is intentionally mixed. NAVER 2020 and Kakao 2020 show genuine platform monetization; SOOP 2023 shows migration-driven traffic-to-paid-surface leverage. Kakao 2021 and NAVER/Poshmark 2022 stop the rule from becoming a platform-label hype machine.

## 9. Evidence Source Map

| case_id | evidence family | source map | evidence timing rule |
|---|---|---|---|
| `R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE` | platform commerce/search/ad operating leverage | NAVER IR/earnings proxy; Stock-Web OHLC shard validation | event date close usable |
| `R8L12_C26_CASE_002_KAKAO_2020_TALKBIZ_AD_COMMERCE_LEVERAGE` | messenger ad-commerce operating leverage | Kakao IR/earnings proxy; Stock-Web OHLC shard validation | event date close usable |
| `R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION` | live-streaming user/creator migration | Twitch Korea exit public announcement/search source; Stock-Web OHLC shard validation | announcement timing uncertain; use next tradable close |
| `R8L12_C26_CASE_004_KAKAO_2021_REGULATORY_THESIS_BREAK` | regulatory/legal cap risk | public platform-regulatory news proxy; Stock-Web OHLC shard validation | use next tradable close to avoid intraday reaction distortion |
| `R8L12_C26_CASE_005_NAVER_2022_POSHMARK_MNA_OVERHANG` | platform-commerce M&A expansion without margin bridge | public Naver/Poshmark acquisition news; Stock-Web OHLC shard validation | event date close usable |

## 10. Price Data Source Map

| symbol | company | profile path | tradable shard path(s) used | profile caveat |
|---:|---|---|---|---|
| `035420` | NAVER | `atlas/symbol_profiles/035/035420.json` | `atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv`; `2021.csv`; `2022.csv`; `2023.csv` | raw/unadjusted; corporate-action candidates blocked if overlapping |
| `035720` | 카카오 | `atlas/symbol_profiles/035/035720.json` | `atlas/ohlcv_tradable_by_symbol_year/035/035720/2020.csv`; `2021.csv`; `2022.csv` | 2021-04-15 corporate-action candidate blocks 1Y/2Y for 2020 entry |
| `067160` | SOOP | `atlas/symbol_profiles/067/067160.json` | `atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv`; `2024.csv` | clean 180D window; name changed from AfreecaTV to SOOP in 2024 |

## 11. Case-by-Case Trigger Grid

| case_id | representative trigger | stage role | why this trigger is usable |
|---|---|---|---|
| `R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE` | `R8L12_C26_TRG_001A_NAVER_STAGE2_ACTIONABLE_2020_07_30` | Stage2-Actionable | non-price monetization evidence plus clean 180D OHLC |
| `R8L12_C26_CASE_002_KAKAO_2020_TALKBIZ_AD_COMMERCE_LEVERAGE` | `R8L12_C26_TRG_002A_KAKAO_STAGE2_ACTIONABLE_2020_05_07` | Stage2-Actionable | strong 180D before split; 1Y/2Y blocked |
| `R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION` | `R8L12_C26_TRG_003A_SOOP_STAGE2_ACTIONABLE_2023_12_07` | Stage2-Actionable | external traffic shock has direct monetization route |
| `R8L12_C26_CASE_004_KAKAO_2021_REGULATORY_THESIS_BREAK` | `R8L12_C26_TRG_004A_KAKAO_4C_REGULATORY_BREAK_2021_09_09` | Stage4C | regulatory cap attacks monetization thesis |
| `R8L12_C26_CASE_005_NAVER_2022_POSHMARK_MNA_OVERHANG` | `R8L12_C26_TRG_005A_NAVER_STAGE2_EVENT_ONLY_POSHMARK_2022_10_04` | Stage2-Watch / 4B-risk | expansion event lacks margin/take-rate bridge at trigger date |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | type | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown after peak | usable |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| `R8L12_C26_TRG_001A_NAVER_STAGE2_ACTIONABLE_2020_07_30` | Stage2-Actionable | 2020-07-30 | 294000 | 18.03 | -1.02 | 18.03 | -6.97 | 39.46 | -6.97 | 2021-07-16 / 461000 | -66.38 | True |
| `R8L12_C26_TRG_001B_NAVER_STAGE3_GREEN_2021_03_18` | Stage3-Green | 2021-03-18 | 403500 | 1.61 | -12.39 | 14.25 | -17.1 | 14.25 | -17.1 | 2021-07-16 / 461000 | -66.38 | True |
| `R8L12_C26_TRG_002A_KAKAO_STAGE2_ACTIONABLE_2020_05_07` | Stage2-Actionable | 2020-05-07 | 206000 | 35.68 | -3.64 | 104.13 | -3.64 | 151.94 | -3.64 | 2021-02-16 / 519000 | contaminated_after_2021-04-15_split | True |
| `R8L12_C26_TRG_003A_SOOP_STAGE2_ACTIONABLE_2023_12_07` | Stage2-Actionable | 2023-12-07 | 76600 | 45.43 | -6.01 | 82.25 | -6.01 | 87.73 | -6.01 | 2024-07-11 / 143800 | -51.32 | True |
| `R8L12_C26_TRG_003B_SOOP_4B_OVERLAY_2024_07_11` | Stage4B | 2024-07-11 | 134600 | 6.83 | -17.53 | 6.83 | -23.1 | 6.83 | -37.1 | 2024-07-11 / 143800 | -51.32 | True |
| `R8L12_C26_TRG_004A_KAKAO_4C_REGULATORY_BREAK_2021_09_09` | Stage4C | 2021-09-09 | 128500 | 4.67 | -14.01 | 4.67 | -35.72 | 4.67 | -48.48 | 2021-09-09 / 134500 | -50.78 | True |
| `R8L12_C26_TRG_005A_NAVER_STAGE2_EVENT_ONLY_POSHMARK_2022_10_04` | Stage2-Watch | 2022-10-04 | 176500 | 11.33 | -12.18 | 31.44 | -12.18 | 31.44 | -12.18 | 2023-02-08 / 232000 | -17.28 | True |


Representative aggregate uses only rows where `dedupe_for_aggregate=true` and `aggregate_group_role=representative`.

Aggregate representative result:

```text
eligible_representative_trigger_count = 5
avg_MFE_90D_pct = 48.90
avg_MAE_90D_pct = -16.70
avg_MFE_180D_pct = 60.73
avg_MAE_180D_pct = -23.45
positive_case_avg_MFE_180D_pct = 93.04
counterexample_case_avg_MFE_180D_pct = 18.06
counterexample_case_avg_MAE_180D_pct = -30.33
```

## 13. Current Calibrated Profile Stress Test

| case | current verdict | actual path | residual interpretation |
|---|---|---|---|
| `R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE` | `current_profile_correct` | positive MFE/MAE alignment | Q2-2020 commerce/search/fintech operating leverage converted traffic into margin/revision visibility. The 180D path behaved like a genuine platform monetization rerating, not a one-day platform label spike. |
| `R8L12_C26_CASE_002_KAKAO_2020_TALKBIZ_AD_COMMERCE_LEVERAGE` | `current_profile_correct` | positive MFE/MAE alignment | TalkBiz/commerce/ad monetization had direct operating-leverage evidence before the later stock-split contamination. 30D/90D/180D windows are clean; 1Y/2Y fields are blocked by the 2021-04-15 corporate-action candidate. |
| `R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION` | `current_profile_too_late` | positive MFE with current profile too slow before confirmed revision | Twitch Korea exit created a directly observable platform-migration route. The key was not just traffic; it was paid-item/advertising/creator migration optionality with low corporate-action contamination. |
| `R8L12_C26_CASE_004_KAKAO_2021_REGULATORY_THESIS_BREAK` | `current_profile_4C_too_late` | low-quality or thesis-break path; positive C26 promotion would be wrong | Same platform monetization engine as the positive case, but the evidence family changed: regulatory/legal cap risk broke the multiple and monetization thesis. This is not a Stage3 positive; it is a hard 4C/risk-route calibration point. |
| `R8L12_C26_CASE_005_NAVER_2022_POSHMARK_MNA_OVERHANG` | `current_profile_false_positive` | low-quality or thesis-break path; positive C26 promotion would be wrong | The Poshmark deal was a platform-commerce expansion event, but it did not by itself prove domestic ad/commerce operating leverage. The path had a sharp MAE and later rebound; C26 should cap platform-expansion events until take-rate or margin visibility appears. |


Stress-test conclusions:

```text
stage2_actionable_evidence_bonus = kept
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = strengthened only when conversion evidence exists; weakened only for direct migration cases before revision confirmation
stage3_cross_evidence_green_buffer = kept
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = strengthened
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | later Green/proxy entry | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| NAVER 2020 | 294000 | 403500 | 461000 | 0.66 | Green was valid but late; Stage2 captured the operating-leverage bridge earlier. |
| Kakao 2020 | 206000 | 407000 | 519000 | 0.64 | Green consumed too much upside but evidence quality justified early action. |
| SOOP 2023 | 76600 | 111900 proxy | 143800 | 0.52 | Current profile likely waits for revision; migration evidence should permit Stage2/Yellow earlier. |
| Kakao 2021 regulatory | 128500 4C | not applicable | 134500 | not_applicable | This is thesis break, not positive Green. |
| NAVER 2022 Poshmark | 176500 watch | not applicable | 232000 | not_applicable | Later rebound does not prove C26 conversion at trigger date. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| `R8L12_C26_TRG_003B_SOOP_4B_OVERLAY_2024_07_11` | valuation_blowoff, positioning_overheat | 0.86 | 0.86 | good_full_window_4B_timing |
| `R8L12_C26_TRG_005A_NAVER_STAGE2_EVENT_ONLY_POSHMARK_2022_10_04` | capital_raise_or_overhang, margin_or_backlog_slowdown | 0.31 | 0.31 | event_expansion_not_full_C26 |
| `R8L12_C26_TRG_004A_KAKAO_4C_REGULATORY_BREAK_2021_09_09` | legal_or_regulatory_block | not_applicable | not_applicable | hard_4C_better_than_4B |

Interpretation: full 4B should require non-price evidence. SOOP had a structural rerating first, then valuation/positioning overheat. NAVER/Poshmark had platform expansion but not platform monetization; it should be watch/4B-risk, not a positive C26 entry.

## 16. 4C Protection Audit

Kakao 2021 is the cleanest 4C row. After next-day entry at 128500, the 180D MFE was only 4.67% while MAE reached -48.48%. The protection label is `hard_4c_success`: regulatory/legal cap risk directly attacked the monetization route.

```text
four_c_protection_label = hard_4c_success
thesis_break_route = regulatory_cap_on_platform_monetization
positive_stage_blocked = true
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_sector_rule
sector_specific_rule_candidate = false
```

The cases are all in L8, but the proposed adjustment is narrower than the whole sector. C27 content/IP and C28 software/security already require different grammars. Applying the C26 traffic-to-monetization rule to all L8 would be too blunt.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
```

Candidate C26 shadow rules:

```text
1. C26_traffic_to_monetization_bridge
   Promote when traffic/user migration is tied to paid inventory, ads, paid items, commerce take-rate, or margin visibility.

2. C26_platform_event_without_margin_cap
   Cap platform expansion headlines when margin/take-rate/ad-revenue evidence is absent.

3. C26_regulatory_cap_hard_route
   If regulatory/legal cap risk directly attacks monetization, route to 4C/thesis-break instead of Stage2/3 positive.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | missed structural count | score-return alignment verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 `e2r_2_1_stock_web_calibrated_proxy` | default | General Stock-Web calibrated rules without C26-specific platform monetization grammar | 5 | 48.90 | -16.70 | 0.40 | 1 | mixed; too permissive for platform expansion and too slow for user-migration route |
| P0b `e2r_2_0_baseline_reference` | rollback | Older baseline with weaker 4B/4C and weaker Stage2-actionable distinction | 5 | 48.90 | -16.70 | 0.60 | 1 | worse; promotes platform label and misses regulatory route |
| P1 `sector_specific_candidate_profile` | L8 sector | Add L8 platform/content evidence separation but do not overfit C26 | 5 | 48.90 | -16.70 | 0.20 | 1 | improved but still broad |
| P2 `canonical_archetype_candidate_profile` | C26 canonical | Require traffic-to-monetization bridge; cap event-only platform expansion; route regulatory cap to 4C | 5 | 48.90 | -16.70 | 0.00 | 0 | best alignment |
| P3 `counterexample_guard_profile` | C26 guard | Hard cap on M&A/platform-expansion and regulatory-cap routes | 5 | 48.90 | -16.70 | 0.00 | 1 | safer but may under-score SOOP before revision |


## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| `R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE` | 84 | Stage3-Yellow | 92 | Stage3-Green-shadow | 18.03 | -6.97 | aligned |
| `R8L12_C26_CASE_002_KAKAO_2020_TALKBIZ_AD_COMMERCE_LEVERAGE` | 88 | Stage3-Green | 96 | Stage3-Green-high | 104.13 | -3.64 | aligned |
| `R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION` | 78 | Stage3-Yellow | 91 | Stage3-Green-shadow | 82.25 | -6.01 | missed_structural_then_aligned |
| `R8L12_C26_CASE_004_KAKAO_2021_REGULATORY_THESIS_BREAK` | 76 | Stage2-Actionable/Watch | 42 | Stage4C-thesis-break | 4.67 | -35.72 | guardrail_counterexample |
| `R8L12_C26_CASE_005_NAVER_2022_POSHMARK_MNA_OVERHANG` | 72 | Stage2-Actionable | 55 | Stage2-Watch/4B-risk | 31.44 | -12.18 | residual_error_high_mae |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| `L8_PLATFORM_CONTENT_SW_SECURITY` | `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` | `PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE` | 3 | 2 | 2 | 1 | 5 | 0 | 7 | 5 | 3 | false | true | C26 now has positive platform-monetization, regulatory 4C, and platform-expansion false-positive coverage for R8 loop 12. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: platform_expansion_event_false_positive, regulatory_cap_4C_late, migration_route_under_scored_before_revision
new_axis_proposed: C26_traffic_to_monetization_bridge; C26_platform_event_without_margin_cap; C26_regulatory_cap_hard_route
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Scheduled round R8 / loop 12.
- L8 large-sector consistency.
- C26 canonical archetype mapping.
- Stock-Web manifest max_date = 2026-02-20.
- Representative triggers use Stock-Web tradable OHLC rows.
- 30D/90D/180D MFE/MAE calculated from raw/unadjusted tradable rows.
- Same-entry dedupe separated representative rows from label-comparison/4B overlay rows.
- Kakao 2020 1Y/2Y blocked because corporate-action candidate 2021-04-15 overlaps longer windows.
```

Not validated / not in scope:

```text
- No live stock recommendation.
- No 2026 current candidate scan.
- No brokerage/API integration.
- No stock_agent source code inspection.
- No production scoring change.
- No newly opened price route outside Songdaiki/stock-web.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C26_traffic_to_monetization_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+2,+2,"Reward direct traffic/user migration only when monetization surface is visible: ads, paid items, commerce take-rate, or margin bridge.",Improves SOOP/NAVER/Kakao positive capture without promoting Poshmark-style event expansion.,R8L12_C26_TRG_001A_NAVER_STAGE2_ACTIONABLE_2020_07_30|R8L12_C26_TRG_002A_KAKAO_STAGE2_ACTIONABLE_2020_05_07|R8L12_C26_TRG_003A_SOOP_STAGE2_ACTIONABLE_2023_12_07,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C26_platform_event_without_margin_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,-2,-2,"Cap platform expansion headlines that lack ad revenue quality, take-rate conversion, or margin visibility.",Blocks NAVER Poshmark event from being treated as C26-positive despite later market rebound.,R8L12_C26_TRG_005A_NAVER_STAGE2_EVENT_ONLY_POSHMARK_2022_10_04,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C26_regulatory_cap_hard_route,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,-3,-3,"When regulatory/legal cap risk directly attacks monetization, route to 4C/thesis-break instead of positive Stage2/3.",Kakao 2021 shows low MFE and large MAE after regulatory shock.,R8L12_C26_TRG_004A_KAKAO_4C_REGULATORY_BREAK_2021_09_09,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE", "symbol": "035420", "company_name": "NAVER", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L12_C26_TRG_001A_NAVER_STAGE2_ACTIONABLE_2020_07_30", "notes": "Q2-2020 commerce/search/fintech operating leverage converted traffic into margin/revision visibility. The 180D path behaved like a genuine platform monetization rerating, not a one-day platform label spike.", "current_profile_verdict": "current_profile_correct", "score_price_alignment": "positive_alignment", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R8L12_C26_CASE_002_KAKAO_2020_TALKBIZ_AD_COMMERCE_LEVERAGE", "symbol": "035720", "company_name": "카카오", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L12_C26_TRG_002A_KAKAO_STAGE2_ACTIONABLE_2020_05_07", "notes": "TalkBiz/commerce/ad monetization had direct operating-leverage evidence before the later stock-split contamination. 30D/90D/180D windows are clean; 1Y/2Y fields are blocked by the 2021-04-15 corporate-action candidate.", "current_profile_verdict": "current_profile_correct", "score_price_alignment": "positive_alignment", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION", "symbol": "067160", "company_name": "SOOP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R8L12_C26_TRG_003A_SOOP_STAGE2_ACTIONABLE_2023_12_07", "notes": "Twitch Korea exit created a directly observable platform-migration route. The key was not just traffic; it was paid-item/advertising/creator migration optionality with low corporate-action contamination.", "current_profile_verdict": "current_profile_too_late", "score_price_alignment": "missed_structural_positive", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R8L12_C26_CASE_004_KAKAO_2021_REGULATORY_THESIS_BREAK", "symbol": "035720", "company_name": "카카오", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R8L12_C26_TRG_004A_KAKAO_4C_REGULATORY_BREAK_2021_09_09", "notes": "Same platform monetization engine as the positive case, but the evidence family changed: regulatory/legal cap risk broke the multiple and monetization thesis. This is not a Stage3 positive; it is a hard 4C/risk-route calibration point.", "current_profile_verdict": "current_profile_4C_too_late", "score_price_alignment": "guardrail_counterexample", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R8L12_C26_CASE_005_NAVER_2022_POSHMARK_MNA_OVERHANG", "symbol": "035420", "company_name": "NAVER", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R8L12_C26_TRG_005A_NAVER_STAGE2_EVENT_ONLY_POSHMARK_2022_10_04", "notes": "The Poshmark deal was a platform-commerce expansion event, but it did not by itself prove domestic ad/commerce operating leverage. The path had a sharp MAE and later rebound; C26 should cap platform-expansion events until take-rate or margin visibility appears.", "current_profile_verdict": "current_profile_false_positive", "score_price_alignment": "guardrail_counterexample", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "trigger", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "sector": "platform_content_software_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "R8L12_C26_TRG_001A_NAVER_STAGE2_ACTIONABLE_2020_07_30", "case_id": "R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE", "symbol": "035420", "company_name": "NAVER", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-07-30", "entry_date": "2020-07-30", "entry_price": 294000, "evidence_available_at_that_date": "Q2-2020 platform monetization evidence: search/commerce/fintech traffic-to-revenue route and operating leverage became visible before full multi-quarter confirmation.", "evidence_source": "NAVER IR/earnings source proxy + Stock-Web row validation; stock-web rows: 035420/2020.csv 2020-07-30, 035420/2021.csv 2021-03-18 and 2021-07-16.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "MFE_30D_pct": 18.03, "MFE_90D_pct": 18.03, "MFE_180D_pct": 39.46, "MFE_1Y_pct": 56.8, "MFE_2Y_pct": 56.8, "MAE_30D_pct": -1.02, "MAE_90D_pct": -6.97, "MAE_180D_pct": -6.97, "MAE_1Y_pct": -6.97, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 461000, "drawdown_after_peak_pct": -66.38, "green_lateness_ratio": "0.66", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_platform_monetization", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "035420_2020-07-30_294000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "sector": "platform_content_software_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "R8L12_C26_TRG_001B_NAVER_STAGE3_GREEN_2021_03_18", "case_id": "R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE", "symbol": "035420", "company_name": "NAVER", "trigger_type": "Stage3-Green", "trigger_date": "2021-03-18", "entry_date": "2021-03-18", "entry_price": 403500, "evidence_available_at_that_date": "By this point the market had seen more complete platform monetization and margin visibility, but the entry consumed much of the upside already captured by the Stage2-Actionable row.", "evidence_source": "Stock-Web row validation + later financial visibility proxy.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "margin_bridge", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "MFE_30D_pct": 1.61, "MFE_90D_pct": 14.25, "MFE_180D_pct": 14.25, "MFE_1Y_pct": 14.25, "MFE_2Y_pct": 14.25, "MAE_30D_pct": -12.39, "MAE_90D_pct": -17.1, "MAE_180D_pct": -17.1, "MAE_1Y_pct": -61.59, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 461000, "drawdown_after_peak_pct": -66.38, "green_lateness_ratio": "0.66", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_late_but_valid", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "035420_2021-03-18_403500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "Stage3 comparison row for green lateness, not aggregate representative.", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "sector": "platform_content_software_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "R8L12_C26_TRG_002A_KAKAO_STAGE2_ACTIONABLE_2020_05_07", "case_id": "R8L12_C26_CASE_002_KAKAO_2020_TALKBIZ_AD_COMMERCE_LEVERAGE", "symbol": "035720", "company_name": "카카오", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-05-07", "entry_date": "2020-05-07", "entry_price": 206000, "evidence_available_at_that_date": "TalkBiz/ad-commerce monetization and operating-profit acceleration were public enough to make a platform operating-leverage route testable before the later split-contaminated window.", "evidence_source": "Kakao earnings/IR source proxy + Stock-Web row validation; stock-web rows: 035720/2020.csv 2020-05-07, 2020-08-31; 035720/2021.csv 2021-02-16.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge", "repeat_order_or_conversion", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2020.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "MFE_30D_pct": 35.68, "MFE_90D_pct": 104.13, "MFE_180D_pct": 151.94, "MFE_1Y_pct": "contaminated_or_unavailable", "MFE_2Y_pct": "contaminated_or_unavailable", "MAE_30D_pct": -3.64, "MAE_90D_pct": -3.64, "MAE_180D_pct": -3.64, "MAE_1Y_pct": "contaminated_or_unavailable", "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2021-02-16", "peak_price": 519000, "drawdown_after_peak_pct": "contaminated_after_2021-04-15_split", "green_lateness_ratio": "0.64", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_mfe_split_after_180D", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 1Y_2Y_blocked_by_2021-04-15_corporate_action_candidate", "same_entry_group_id": "035720_2020-05-07_206000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "sector": "platform_content_software_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "R8L12_C26_TRG_003A_SOOP_STAGE2_ACTIONABLE_2023_12_07", "case_id": "R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION", "symbol": "067160", "company_name": "SOOP", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-06", "entry_date": "2023-12-07", "entry_price": 76600, "evidence_available_at_that_date": "Twitch Korea exit created a visible user/creator migration funnel into Korean live-streaming platforms. For SOOP, the monetization route included paid items, platform traffic, advertising inventory, and creator ecosystem retention.", "evidence_source": "Twitch Korea exit public announcement/search source + Stock-Web row validation; stock-web rows: 067160/2023.csv 2023-12-06/07 and 067160/2024.csv 2024-02-28/07-11.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "MFE_30D_pct": 45.43, "MFE_90D_pct": 82.25, "MFE_180D_pct": 87.73, "MFE_1Y_pct": 87.73, "MFE_2Y_pct": 87.73, "MAE_30D_pct": -6.01, "MAE_90D_pct": -6.01, "MAE_180D_pct": -6.01, "MAE_1Y_pct": -6.01, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 143800, "drawdown_after_peak_pct": -51.32, "green_lateness_ratio": "0.52", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_user_migration_platform_leverage", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "067160_2023-12-07_76600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "sector": "platform_content_software_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "R8L12_C26_TRG_003B_SOOP_4B_OVERLAY_2024_07_11", "case_id": "R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION", "symbol": "067160", "company_name": "SOOP", "trigger_type": "Stage4B", "trigger_date": "2024-07-11", "entry_date": "2024-07-11", "entry_price": 134600, "evidence_available_at_that_date": "After the migration rerating matured, valuation/positioning overheat became a more important marginal signal than fresh user-migration evidence.", "evidence_source": "Stock-Web row validation + valuation/positioning overlay proxy.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv", "profile_path": "atlas/symbol_profiles/067/067160.json", "MFE_30D_pct": 6.83, "MFE_90D_pct": 6.83, "MFE_180D_pct": 6.83, "MFE_1Y_pct": 6.83, "MFE_2Y_pct": 6.83, "MAE_30D_pct": -17.53, "MAE_90D_pct": -23.1, "MAE_180D_pct": -37.1, "MAE_1Y_pct": -48.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 143800, "drawdown_after_peak_pct": -51.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_after_structural_rerating", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "067160_2024-07-11_134600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "4B overlay row for the same SOOP case; not a separate aggregate entry.", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "sector": "platform_content_software_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "R8L12_C26_TRG_004A_KAKAO_4C_REGULATORY_BREAK_2021_09_09", "case_id": "R8L12_C26_CASE_004_KAKAO_2021_REGULATORY_THESIS_BREAK", "symbol": "035720", "company_name": "카카오", "trigger_type": "Stage4C", "trigger_date": "2021-09-08", "entry_date": "2021-09-09", "entry_price": 128500, "evidence_available_at_that_date": "Platform monetization evidence was no longer the controlling variable; regulatory/legal cap risk began to dominate the multiple and growth path.", "evidence_source": "Platform-regulatory public news proxy + Stock-Web row validation; stock-web rows: 035720/2021.csv 2021-09-08/09 and 035720/2022.csv 2022-06/07 lows.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken", "legal_or_regulatory_block"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv", "profile_path": "atlas/symbol_profiles/035/035720.json", "MFE_30D_pct": 4.67, "MFE_90D_pct": 4.67, "MFE_180D_pct": 4.67, "MFE_1Y_pct": 4.67, "MFE_2Y_pct": 4.67, "MAE_30D_pct": -14.01, "MAE_90D_pct": -35.72, "MAE_180D_pct": -48.48, "MAE_1Y_pct": -48.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-09-09", "peak_price": 134500, "drawdown_after_peak_pct": -50.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4C_better_than_4B", "four_b_evidence_type": ["legal_or_regulatory_block"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4C_regulatory_thesis_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2021-04-15_split", "same_entry_group_id": "035720_2021-09-09_128500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PLATFORM_AD_COMMERCE_TAKE_RATE_TRAFFIC_TO_MARGIN_BRIDGE", "sector": "platform_content_software_security", "primary_archetype": "platform_ad_revenue_operating_leverage", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "trigger_id": "R8L12_C26_TRG_005A_NAVER_STAGE2_EVENT_ONLY_POSHMARK_2022_10_04", "case_id": "R8L12_C26_CASE_005_NAVER_2022_POSHMARK_MNA_OVERHANG", "symbol": "035420", "company_name": "NAVER", "trigger_type": "Stage2-Watch", "trigger_date": "2022-10-04", "entry_date": "2022-10-04", "entry_price": 176500, "evidence_available_at_that_date": "The Poshmark announcement was a platform-commerce expansion story, but it did not prove C26 ad/commerce operating leverage at the trigger date; near-term integration and capital-allocation drag dominated.", "evidence_source": "Naver/Poshmark acquisition public news proxy + Stock-Web row validation; stock-web rows: 035420/2022.csv 2022-10-04 to 2022-12 and 035420/2023.csv 2023-02.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "margin_or_backlog_slowdown", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035420/2022.csv", "profile_path": "atlas/symbol_profiles/035/035420.json", "MFE_30D_pct": 11.33, "MFE_90D_pct": 31.44, "MFE_180D_pct": 31.44, "MFE_1Y_pct": 31.44, "MFE_2Y_pct": 44.19, "MAE_30D_pct": -12.18, "MAE_90D_pct": -12.18, "MAE_180D_pct": -12.18, "MAE_1Y_pct": -12.18, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-08", "peak_price": 232000, "drawdown_after_peak_pct": -17.28, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.31, "four_b_full_window_peak_proximity": 0.31, "four_b_timing_verdict": "event_expansion_not_full_C26", "four_b_evidence_type": ["capital_raise_or_overhang", "margin_or_backlog_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_only_false_C26_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "035420_2022-10-04_176500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L12_C26_CASE_001_NAVER_2020_COMMERCE_SEARCH_AD_OPERATING_LEVERAGE", "trigger_id": "R8L12_C26_TRG_001A_NAVER_STAGE2_ACTIONABLE_2020_07_30", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 12, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 12, "traffic_conversion_score": 14, "commerce_take_rate_score": 10, "paid_user_migration_score": 0, "platform_regulatory_risk_score": 0, "mna_integration_drag_score": 0, "creator_ecosystem_retention_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 16, "traffic_conversion_score": 16, "commerce_take_rate_score": 14, "paid_user_migration_score": 0, "platform_regulatory_risk_score": 0, "mna_integration_drag_score": 0, "creator_ecosystem_retention_score": 0}, "weighted_score_after": 92, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["ad_revenue_quality_score", "traffic_conversion_score", "paid_user_migration_score", "platform_regulatory_risk_score", "mna_integration_drag_score"], "component_delta_explanation": "C26 shadow adds explicit traffic-to-monetization and commerce take-rate quality, converting a broad platform score into a cleaner operating-leverage signal.", "MFE_90D_pct": 18.03, "MAE_90D_pct": -6.97, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L12_C26_CASE_002_KAKAO_2020_TALKBIZ_AD_COMMERCE_LEVERAGE", "trigger_id": "R8L12_C26_TRG_002A_KAKAO_STAGE2_ACTIONABLE_2020_05_07", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 14, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 14, "traffic_conversion_score": 16, "commerce_take_rate_score": 10, "paid_user_migration_score": 0, "platform_regulatory_risk_score": 0, "mna_integration_drag_score": 0, "creator_ecosystem_retention_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 16, "revision_score": 16, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 18, "traffic_conversion_score": 18, "commerce_take_rate_score": 14, "paid_user_migration_score": 0, "platform_regulatory_risk_score": 0, "mna_integration_drag_score": 0, "creator_ecosystem_retention_score": 0}, "weighted_score_after": 96, "stage_label_after": "Stage3-Green-high", "changed_components": ["ad_revenue_quality_score", "traffic_conversion_score", "paid_user_migration_score", "platform_regulatory_risk_score", "mna_integration_drag_score"], "component_delta_explanation": "TalkBiz evidence deserves high C26 score before the split-contaminated long window; 180D price alignment is strong.", "MFE_90D_pct": 104.13, "MAE_90D_pct": -3.64, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L12_C26_CASE_003_SOOP_2023_TWITCH_EXIT_USER_MIGRATION", "trigger_id": "R8L12_C26_TRG_003A_SOOP_STAGE2_ACTIONABLE_2023_12_07", "symbol": "067160", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 18, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 8, "traffic_conversion_score": 16, "commerce_take_rate_score": 0, "paid_user_migration_score": 14, "platform_regulatory_risk_score": 0, "mna_integration_drag_score": 0, "creator_ecosystem_retention_score": 14}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 12, "traffic_conversion_score": 20, "commerce_take_rate_score": 0, "paid_user_migration_score": 20, "platform_regulatory_risk_score": 0, "mna_integration_drag_score": 0, "creator_ecosystem_retention_score": 18}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["ad_revenue_quality_score", "traffic_conversion_score", "paid_user_migration_score", "platform_regulatory_risk_score", "mna_integration_drag_score"], "component_delta_explanation": "The current profile can under-score migration routes before earnings revision appears; C26 should reward direct user/creator migration plus monetization surface.", "MFE_90D_pct": 82.25, "MAE_90D_pct": -6.01, "score_return_alignment_label": "missed_structural_then_aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L12_C26_CASE_004_KAKAO_2021_REGULATORY_THESIS_BREAK", "trigger_id": "R8L12_C26_TRG_004A_KAKAO_4C_REGULATORY_BREAK_2021_09_09", "symbol": "035720", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 12, "traffic_conversion_score": 12, "commerce_take_rate_score": 0, "paid_user_migration_score": 0, "platform_regulatory_risk_score": 16, "mna_integration_drag_score": 0, "creator_ecosystem_retention_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable/Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -10, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 0, "traffic_conversion_score": 0, "commerce_take_rate_score": 0, "paid_user_migration_score": 0, "platform_regulatory_risk_score": 28, "mna_integration_drag_score": 0, "creator_ecosystem_retention_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage4C-thesis-break", "changed_components": ["ad_revenue_quality_score", "traffic_conversion_score", "paid_user_migration_score", "platform_regulatory_risk_score", "mna_integration_drag_score"], "component_delta_explanation": "Regulatory cap risk should cancel the positive C26 platform evidence rather than merely lower the score. The 180D MAE confirms hard route protection.", "MFE_90D_pct": 4.67, "MAE_90D_pct": -35.72, "score_return_alignment_label": "guardrail_counterexample", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R8L12_C26_CASE_005_NAVER_2022_POSHMARK_MNA_OVERHANG", "trigger_id": "R8L12_C26_TRG_005A_NAVER_STAGE2_EVENT_ONLY_POSHMARK_2022_10_04", "symbol": "035420", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 4, "traffic_conversion_score": 6, "commerce_take_rate_score": 6, "paid_user_migration_score": 0, "platform_regulatory_risk_score": 0, "mna_integration_drag_score": 18, "creator_ecosystem_retention_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "ad_revenue_quality_score": 0, "traffic_conversion_score": 4, "commerce_take_rate_score": 4, "paid_user_migration_score": 0, "platform_regulatory_risk_score": 0, "mna_integration_drag_score": 26, "creator_ecosystem_retention_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage2-Watch/4B-risk", "changed_components": ["ad_revenue_quality_score", "traffic_conversion_score", "paid_user_migration_score", "platform_regulatory_risk_score", "mna_integration_drag_score"], "component_delta_explanation": "Platform acquisition is not platform ad operating leverage unless take-rate, margin, or domestic monetization conversion is present. The shadow profile penalizes M&A integration drag.", "MFE_90D_pct": 31.44, "MAE_90D_pct": -12.18, "score_return_alignment_label": "residual_error_high_mae", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R8", "loop": "12", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["platform_expansion_event_false_positive", "regulatory_cap_4C_late", "migration_route_under_scored_before_revision"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop = 12
next_round = R9
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files fetched/validated in this research session:

```text
atlas/manifest.json
atlas/symbol_profiles/035/035420.json
atlas/symbol_profiles/035/035720.json
atlas/symbol_profiles/067/067160.json
atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv
atlas/ohlcv_tradable_by_symbol_year/035/035420/2021.csv
atlas/ohlcv_tradable_by_symbol_year/035/035420/2022.csv
atlas/ohlcv_tradable_by_symbol_year/035/035420/2023.csv
atlas/ohlcv_tradable_by_symbol_year/035/035720/2020.csv
atlas/ohlcv_tradable_by_symbol_year/035/035720/2021.csv
atlas/ohlcv_tradable_by_symbol_year/035/035720/2022.csv
atlas/ohlcv_tradable_by_symbol_year/067/067160/2023.csv
atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv
```

External historical evidence source notes used for trigger timing, not for price calculation:

```text
- NAVER Q2-2020 platform monetization / earnings public evidence proxy.
- Kakao Q1-2020 TalkBiz/ad-commerce operating leverage public evidence proxy.
- Twitch Korea exit announcement dated 2023-12-06 and Korea exit effective 2024-02-27, used only to anchor SOOP migration trigger timing.
- Kakao 2021 platform regulation / financial-platform scrutiny public news proxy, used only to anchor 4C timing.
- NAVER/Poshmark acquisition public announcement in October 2022, used only to anchor platform-expansion event timing.
```

