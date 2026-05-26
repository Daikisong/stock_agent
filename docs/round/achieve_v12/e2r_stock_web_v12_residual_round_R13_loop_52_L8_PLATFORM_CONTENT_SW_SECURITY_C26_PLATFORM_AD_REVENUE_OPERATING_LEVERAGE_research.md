# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
repo_session = later_batch_implementation_only
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

- round: `R13`
- loop: `52`
- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`
- fine_archetype_id: `COMMERCE_PAYMENT_ADTECH_PLATFORM_OPERATING_LEVERAGE_GUARD`
- loop_objective: `auto_coverage_gap_fill, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test, green_strictness_stress_test, stage2_actionable_bonus_stress_test`
- investment recommendation language: intentionally excluded.
- live scan: not performed.
- brokerage API / auto-trading: not touched.
- stock_agent code: not opened.

This file is historical calibration research only. It is not a live watchlist, investment recommendation, or repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-propose the existing global axes. It stress-tests the remaining C26 residual: **whether platform-looking evidence is truly owned traffic / owned commerce inventory / margin conversion, or only payment volume, ad-agency pass-through, or event-premium narrative**.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| large_sector_id | `L8_PLATFORM_CONTENT_SW_SECURITY` |
| canonical_archetype_id | `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` |
| fine_archetype_id | `COMMERCE_PAYMENT_ADTECH_PLATFORM_OPERATING_LEVERAGE_GUARD` |
| sector | 플랫폼·콘텐츠·SW·보안 |
| primary_archetype | Platform ad revenue / commerce traffic / payment-rail operating leverage |
| excluded adjacent archetypes | C27 pure content IP monetization, C28 software/security contract retention |

Compression thesis: C26 should promote **owned traffic + monetization conversion + margin bridge** earlier than full Green, but should discount **payment volume without take-rate leverage**, **ad agency/re-seller recovery**, and **event-premium crypto/AI themes**.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts or already generated local research MDs were used only for coverage and duplicate avoidance. No production code was opened.

Observed C26 prior coverage in local artifact set:

- R8 loop 10: NAVER, Kakao, SOOP, Nasmedia, Incross.
- R13 loop 16: SOOP, NAVER, Kakao.
- R13 loop 34/37: NAVER, Kakao, SOOP, Nasmedia, Incross.
- Repeated symbols excluded for this loop: `035420`, `035720`, `067160`, `089600`, `216050`.

Auto-selected coverage gap:

```text
auto_selected_coverage_gap = C26 had owned internet-platform and ad-rep coverage, but lacked Cafe24-style commerce-platform optionality, PG/payment volume guard, payment-token event-premium blowoff, AI-adtech pass-through guard, and PlayD-style agency proxy coverage.
```

Novelty classification:

```text
required_new_independent_case_ratio = 0.60
calibration_usable_case_count = 5
new_independent_case_count = 5
new_independent_case_ratio = 1.00
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
reused_case_count = 0
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

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

Price source validation row:

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

Important caveats:

- Price basis is `tradable_raw`, not adjusted close.
- Corporate-action candidate windows are blocked by default.
- This loop uses clean 180D windows based on the symbol profile candidate dates listed below.
- 1Y/2Y fields are not used for weight calibration in this loop and are left `null` in JSONL; 30D/90D/180D are the calibration windows.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | profile caveat | 180D forward available | calibration_usable |
|---|---|---|---|---|---|
| 042000 | 카페24 | atlas/symbol_profiles/042/042000.json | corporate-action candidates only in 2021; tested 2023-2024 window clean | true | true |
| 060250 | NHN KCP | atlas/symbol_profiles/060/060250.json | 2021-12-20 corporate-action candidate exists, so this loop uses 2024 only | true | true |
| 064260 | 다날 | atlas/symbol_profiles/064/064260.json | tested 2021-2022 window is after older 2016 corporate-action candidates | true | true |
| 214270 | FSN | atlas/symbol_profiles/214/214270.json | 2021-11-08 candidate blocks the 2021 bubble window, so this loop uses 2024 clean event window | true | true |
| 237820 | 플레이디 | atlas/symbol_profiles/237/237820.json | no corporate-action candidates | true | true |

All representative trigger rows meet the historical eligibility gate:

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward 180 trading days available = true
high/low/close/volume present = true
MFE/MAE 30D/90D/180D calculated = true
corporate_action_contaminated_180D_window = false
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression rationale |
|---|---|---|
| CREATOR_COMMERCE_PLATFORM_TRAFFIC_OPTIONALITY | C26 | Owned merchant/creator traffic can behave like platform operating leverage before full earnings revision. |
| PAYMENT_PLATFORM_VOLUME_WITH_MARGIN_DURABILITY_TEST | C26 | Payment volume only counts if take-rate and margin bridge close; otherwise it is watch-only. |
| PAYMENT_TOKEN_EVENT_PREMIUM_BLOWOFF_GUARD | C26 | Payment-token optionality is not operating leverage without regulatory and revenue durability. |
| AI_ADTECH_THEME_PASS_THROUGH_FALSE_POSITIVE | C26 | AI/adtech theme without owned inventory is a pass-through false-positive risk. |
| DIGITAL_AD_AGENCY_RECOVERY_WITHOUT_OWNED_PLATFORM | C26 | Ad agency recovery can rally tactically but should not become Green without durable owned-platform evidence. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | calibration_usable |
|---|---:|---|---|---|---|---|---|
| C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE | 042000 | 카페24 | structural_success | positive | TRG_C26_CAFE24_2023_12_06_STAGE2A | current_profile_missed_structural | true |
| C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN | 060250 | NHN KCP | failed_rerating | counterexample | TRG_C26_NHNKCP_2024_02_14_STAGE2A | current_profile_false_positive | true |
| C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF | 064260 | 다날 | 4B_overlay_success | counterexample | TRG_C26_DANAL_2021_11_17_STAGE2A | current_profile_4B_too_late | true |
| C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH | 214270 | FSN | false_positive_green | counterexample | TRG_C26_FSN_2024_02_01_STAGE2A | current_profile_false_positive | true |
| C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY | 237820 | 플레이디 | failed_rerating | counterexample | TRG_C26_PLAYD_2021_02_10_STAGE2A | current_profile_false_positive | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 4
4B_case_count = 2
4C_case_count = 0
minimum_positive_case_count_satisfied = true
minimum_counterexample_count_satisfied = true
minimum_calibration_usable_case_count_satisfied = true
```

The balance is deliberately counterexample-heavy because earlier C26 loops already proved owned internet-platform positives. This loop adds the missing guardrail surface: payment volume, crypto/payment event premium, AI/adtech pass-through, and agency proxy recovery.

## 9. Evidence Source Map

| case_id | trigger evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE | strategic commerce-platform optionality | public_event_or_disclosure; customer_or_order_quality; capacity_or_volume_route | no confirmed revision at Stage2 | valuation/event premium 4B after June 2024 blowoff |
| C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN | PG/payment relief rally | public_event_or_disclosure; volume route | insufficient take-rate/margin bridge | false-positive guard |
| C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF | payment-token optionality | public event; regulatory optionality; relative strength | no durable revision confirmation | valuation blowoff / event cap 4B |
| C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH | AI/adtech theme | public event; relative strength | no owned traffic / no margin bridge | false-positive guard |
| C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY | ad-cycle agency proxy | public event; relative strength; early recovery | no owned inventory confirmation | false-positive guard |

## 10. Price Data Source Map

| symbol | price_shard_path(s) used | profile_path | stock_web_manifest_max_date |
|---:|---|---|---|
| 042000 | atlas/ohlcv_tradable_by_symbol_year/042/042000/2023.csv; atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv | atlas/symbol_profiles/042/042000.json | 2026-02-20 |
| 060250 | atlas/ohlcv_tradable_by_symbol_year/060/060250/2024.csv | atlas/symbol_profiles/060/060250.json | 2026-02-20 |
| 064260 | atlas/ohlcv_tradable_by_symbol_year/064/064260/2021.csv; atlas/ohlcv_tradable_by_symbol_year/064/064260/2022.csv | atlas/symbol_profiles/064/064260.json | 2026-02-20 |
| 214270 | atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv | atlas/symbol_profiles/214/214270.json | 2026-02-20 |
| 237820 | atlas/ohlcv_tradable_by_symbol_year/237/237820/2021.csv | atlas/symbol_profiles/237/237820.json | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | trigger_outcome_label | current_profile_verdict | aggregate_group_role |
|---|---|---|---|---|---:|---:|---:|---|---|---|
| TRG_C26_CAFE24_2023_12_06_STAGE2A | C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE | Stage2-Actionable | 2023-12-05 | 2023-12-06 | 22150 | 55.08 | -29.98 | structural_success | current_profile_missed_structural | representative |
| TRG_C26_CAFE24_2024_06_20_4B | C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE | 4B | 2024-06-20 | 2024-06-20 | 41750 | 2.87 | -42.87 | 4B_overlay_success | current_profile_4B_too_late | 4B_overlay_only |
| TRG_C26_NHNKCP_2024_02_14_STAGE2A | C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN | Stage2-Actionable | 2024-02-14 | 2024-02-14 | 11770 | 32.54 | -22.09 | failed_rerating | current_profile_false_positive | representative |
| TRG_C26_DANAL_2021_11_17_STAGE2A | C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF | Stage2-Actionable | 2021-11-17 | 2021-11-17 | 10800 | 74.54 | -13.43 | price_moved_without_evidence | current_profile_4B_too_late | representative |
| TRG_C26_DANAL_2021_12_13_4B | C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF | 4B | 2021-12-13 | 2021-12-13 | 17200 | 9.59 | -45.64 | 4B_overlay_success | current_profile_4B_too_late | 4B_overlay_only |
| TRG_C26_FSN_2024_02_01_STAGE2A | C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH | Stage2-Actionable | 2024-02-01 | 2024-02-01 | 3245 | 16.33 | -41.6 | false_positive_green | current_profile_false_positive | representative |
| TRG_C26_PLAYD_2021_02_10_STAGE2A | C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY | Stage2-Actionable | 2021-02-10 | 2021-02-10 | 8940 | 40.38 | -7.05 | failed_rerating | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TRG_C26_CAFE24_2023_12_06_STAGE2A | 22150 | 55.08 | 0.0 | 55.08 | -29.98 | 93.91 | -33.82 | 2024-06-26 | 42950 | -65.89 |
| TRG_C26_CAFE24_2024_06_20_4B | 41750 | 2.87 | -33.89 | 2.87 | -42.87 | 2.87 | -42.87 | 2024-06-26 | 42950 | -65.89 |
| TRG_C26_NHNKCP_2024_02_14_STAGE2A | 11770 | 32.54 | -6.71 | 32.54 | -22.09 | 32.54 | -31.1 | 2024-02-20 | 15600 | -48.01 |
| TRG_C26_DANAL_2021_11_17_STAGE2A | 10800 | 74.54 | -11.94 | 74.54 | -13.43 | 74.54 | -39.91 | 2021-12-13 | 18850 | -65.57 |
| TRG_C26_DANAL_2021_12_13_4B | 17200 | 9.59 | -36.05 | 9.59 | -45.64 | 9.59 | -62.27 | 2021-12-13 | 18850 | -65.57 |
| TRG_C26_FSN_2024_02_01_STAGE2A | 3245 | 16.33 | -17.26 | 16.33 | -41.6 | 16.33 | -52.23 | 2024-02-02 | 3775 | -58.94 |
| TRG_C26_PLAYD_2021_02_10_STAGE2A | 8940 | 40.38 | -7.05 | 40.38 | -7.05 | 40.38 | -20.02 | 2021-03-31 | 12550 | -43.03 |

Interpretation:

- Cafe24 is the positive Stage2 evidence: 180D MFE was very large, but the path later needed a 4B overlay because the event premium ran ahead of confirmed revision.
- NHN KCP shows why payment volume alone should not be C26 Green: early MFE was tradable, but 90D/180D MAE was too large.
- Danal shows event-premium blowoff: Stage2 may flag option value, but 4B must arrive before the post-peak drawdown dominates.
- FSN and PlayD are pass-through / agency-proxy false positives: current calibrated profile still over-promotes if it reads relative strength as platform leverage.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile decision | actual MFE/MAE alignment | residual verdict |
|---|---|---|---|
| C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE | likely too cautious at Stage2, then too slow on 4B | MFE_180D +93.91%, MAE_180D -33.82% | current_profile_missed_structural + 4B_too_late |
| C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN | may over-promote payment volume | MFE_90D +32.54%, MAE_90D -22.09% | current_profile_false_positive |
| C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF | may allow theme to remain positive too long | MFE_180D +74.54%, MAE_180D -39.91% | current_profile_4B_too_late |
| C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH | may read relative strength as platform leverage | MFE_180D +16.33%, MAE_180D -52.23% | current_profile_false_positive |
| C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY | may over-promote ad-cycle recovery | MFE_180D +40.38%, MAE_180D -20.02% | current_profile_false_positive |

Answers to required stress-test questions:

1. Stage2 bonus was useful for Cafe24, but too permissive for payment/adtech/agency proxy rows.
2. Yellow threshold 75 still lets too many pass-through names into false-positive territory unless C26-specific guards are added.
3. Green threshold 87 / revision 55 should be kept, and for C26 should require owned traffic plus margin bridge.
4. Price-only blowoff guard is correct and should be strengthened inside C26 for crypto-payment and AI/adtech event premium.
5. Full 4B non-price requirement is correct; Danal and Cafe24 show why the evidence type must be non-price valuation/event premium, not merely a local top.
6. Hard 4C routing was not the main issue in this loop; the earlier residual is 4B timing and false positive prevention.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green-like confirmation status | green_lateness_ratio | interpretation |
|---|---:|---|---|---|
| C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE | 22150 | no confirmed Green at Stage2; conditional later | not_applicable | Stage2 is correct, but Green must wait for revision/margin bridge. |
| C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN | 11770 | no Green confirmation | not_applicable | Volume route without margin bridge should stay Stage2/watch. |
| C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF | 10800 | no Green confirmation | not_applicable | Event premium should not become Green. |
| C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH | 3245 | no Green confirmation | not_applicable | Pass-through adtech theme is not platform leverage. |
| C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY | 8940 | no Green confirmation | not_applicable | Agency recovery should not cross Green without owned inventory. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---|---:|---:|---|---|
| TRG_C26_CAFE24_2024_06_20_4B | 0.94 | 0.94 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| TRG_C26_DANAL_2021_12_13_4B | 0.80 | 0.80 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |

Cafe24 and Danal both show that C26 needs a 4B overlay when event premium becomes the driver. The local and full-window proximity are separated explicitly; these are not price-only sell signals because the overlay evidence is valuation/event-premium exhaustion.

## 16. 4C Protection Audit

Hard 4C is not the primary calibration target here. Labels used:

| case_id | four_c_protection_label | comment |
|---|---|---|
| C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE | thesis_break_watch_only | No clean hard thesis break; 4B is enough. |
| C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN | false_break | Drawdown reflects failed rerating rather than a single hard thesis break. |
| C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF | hard_4c_late / thesis_break_watch_only | Regulatory/event premium should have been watched after 4B. |
| C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH | false_break | Theme false positive; not a hard 4C thesis break. |
| C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY | false_break | Agency-proxy fade; not a hard 4C event. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
candidate_rule = Owned traffic / owned commerce inventory should receive Stage2 credit only when conversion-to-margin path is plausible; pass-through ad agency, payment volume, crypto-payment, and AI/adtech event premium must be guarded below Green until revision and margin bridge close.
```

Sector-specific effect:

- Promotes Cafe24-like cases earlier than Green when platform traffic route is credible.
- Blocks NHN KCP, FSN, PlayD, Danal-like cases from false Green when the evidence is volume/theme/pass-through rather than durable platform operating leverage.
- Keeps existing global Stage2 and Green thresholds intact.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
new_axis_proposed = c26_owned_traffic_conversion_bonus; c26_payment_volume_margin_guard; c26_ad_agency_pass_through_discount; c26_event_premium_4b_guard
```

Candidate C26 rule:

```text
if owned_traffic_score high AND monetization_conversion_score high AND margin_bridge_score improving:
    allow Stage2-Actionable earlier than confirmed Green
else if payment_volume_without_margin_bridge OR ad_agency_pass_through OR crypto/AI event premium:
    cap at Stage2/watch; block Stage3-Green until revision_score and margin_bridge_score close
if valuation/event premium after large move and no confirmed revision:
    attach 4B overlay; do not wait for hard 4C
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global calibrated proxy | none | 5 | 34.77 | -23.22 | 51.54 | -35.42 | 0.8 | 0 | 0 | over-promotes payment/ad-agency proxies |
| P0b | e2r_2_0_baseline_reference | rollback reference | looser Green | 5 | 34.77 | -23.22 | 51.54 | -35.42 | 0.8 | 0 | 1 | worse false-positive risk |
| P1 | sector_specific_candidate_profile | L8 owned traffic / pass-through split | owned traffic bonus, pass-through discount | 5 | 34.77 | -23.22 | 51.54 | -35.42 | 0.2 | 0 | 0 | better alignment |
| P2 | canonical_archetype_candidate_profile | C26 creator commerce + payment guard | commerce optionality bonus, payment margin guard | 5 | 34.77 | -23.22 | 51.54 | -35.42 | 0.2 | 0 | 0 | best current candidate |
| P3 | counterexample_guard_profile | strict anti-theme guard | event premium blocks Green | 5 | 34.77 | -23.22 | 51.54 | -35.42 | 0.0 | 1 | 0 | safer but may miss Cafe24-like Stage2 |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE | 78.0 | Stage3-Yellow / high Stage2 | 84.5 | Stage3-Yellow-high / conditional Green | 55.08 | -29.98 | aligned |
| C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN | 76.0 | Stage3-Yellow | 69.0 | Stage2 / watch only | 32.54 | -22.09 | current_profile_overpromoted_or_requires_guard |
| C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF | 79.0 | Stage3-Yellow risk | 66.5 | 4B risk overlay / no positive Green | 74.54 | -13.43 | current_profile_overpromoted_or_requires_guard |
| C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH | 75.0 | Stage3-Yellow | 65.0 | Stage2 / watch only | 16.33 | -41.6 | current_profile_overpromoted_or_requires_guard |
| C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY | 75.5 | Stage3-Yellow | 67.0 | Stage2 / watch only | 40.38 | -7.05 | current_profile_overpromoted_or_requires_guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | COMMERCE_PAYMENT_ADTECH_PLATFORM_OPERATING_LEVERAGE_GUARD | 1 | 4 | 2 | 0 | 5 | 0 | 7 | 5 | 5 | true | true | Payment/adtech/agency false-positive guard partly filled; remaining gap is app-store/platform take-rate cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: payment_volume_without_margin_bridge_false_positive, ad_agency_pass_through_false_positive, event_premium_blowoff_needs_4B_overlay, owned_creator_commerce_stage2_missed_structural
new_axis_proposed: c26_owned_traffic_conversion_bonus; c26_payment_volume_margin_guard; c26_ad_agency_pass_through_discount; c26_event_premium_4b_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: avg=23.8; same_archetype_new_symbol_count=5; repeated_same_symbol_penalty=0; repeated_same_trigger_date_penalty=0; schema_rematerialization_penalty=0
auto_selected_coverage_gap: C26 previous coverage concentrated on NAVER/Kakao/SOOP/Nasmedia/Incross; this loop adds commerce-platform, PG/payment, crypto-payment, AI-adtech and agency-proxy cases.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest fields and max_date.
- Symbol profile availability and corporate-action candidate dates.
- 30D/90D/180D MFE/MAE using stock-web tradable raw OHLC rows.
- Representative trigger dedupe by same_entry_group_id.
- Current calibrated profile stress test as research proxy, not production score.

Not validated:

- Live scan or current candidate discovery.
- Broker API, auto-trading, or execution logic.
- `stock_agent/src/e2r` code or production scoring patch.
- 1Y/2Y calibration metrics; fields are kept as `null` in JSONL for this loop.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_owned_commerce_creator_traffic_stage2_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+1.0,+1.0,"Owned merchant/creator traffic plus commerce conversion can justify Stage2 before full revision confirmation.","Cafe24 captured large 180D MFE but needs 4B overlay after valuation blowoff.",TRG_C26_CAFE24_2023_12_06_STAGE2A,5,5,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_payment_volume_without_margin_bridge_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,+1.5,+1.5,"Payment/PG volume without take-rate or margin bridge should not be promoted to Green.","NHN KCP and Danal show tradable rallies but large 90D/180D drawdowns.",TRG_C26_NHNKCP_2024_02_14_STAGE2A|TRG_C26_DANAL_2021_11_17_STAGE2A,5,5,4,medium,canonical_shadow_only,"not production; guard applied before Green"
shadow_weight,c26_ad_agency_pass_through_discount,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,-2.0,-2.0,"Agency/reseller ad-cycle recovery lacks owned inventory and should remain Stage2/watch unless revision and margin bridge close.","FSN and PlayD were current-profile false-positive stress tests.",TRG_C26_FSN_2024_02_01_STAGE2A|TRG_C26_PLAYD_2021_02_10_STAGE2A,5,5,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE", "symbol": "042000", "company_name": "카페24", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "CREATOR_COMMERCE_PLATFORM_TRAFFIC_OPTIONALITY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_C26_CAFE24_2023_12_06_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Google/YouTube commerce route created credible first-party merchant traffic optionality; price path showed large MFE but high later MAE, so Stage2 works while Green needs revision confirmation.", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Owned commerce platform optionality should receive Stage2 shadow credit, but 4B overlay is required once valuation/event premium outruns confirmed revenue revision."}
{"row_type": "case", "case_id": "C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN", "symbol": "060250", "company_name": "NHN KCP", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PAYMENT_PLATFORM_VOLUME_WITH_MARGIN_DURABILITY_TEST", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_C26_NHNKCP_2024_02_14_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "PG/payment volume rebound produced a tradable short rally, but no durable owned-ad platform or margin bridge appeared; 90D/180D drawdown invalidates Green promotion.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Payment rails are adjacent to C26 only when take-rate/margin leverage is visible; volume without margin bridge should remain watch-only."}
{"row_type": "case", "case_id": "C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF", "symbol": "064260", "company_name": "다날", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PAYMENT_TOKEN_EVENT_PREMIUM_BLOWOFF_GUARD", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_C26_DANAL_2021_11_17_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Payment/crypto optionality generated very large MFE, but the path was a valuation/event-premium blowoff with severe post-peak drawdown.", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "This is useful as 4B timing evidence, not as positive platform operating-leverage evidence."}
{"row_type": "case", "case_id": "C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH", "symbol": "214270", "company_name": "FSN", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AI_ADTECH_THEME_PASS_THROUGH_FALSE_POSITIVE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_C26_FSN_2024_02_01_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "AI/adtech theme spike lacked owned inventory, advertiser retention, and confirmed margin bridge; 90D/180D MAE dominated the small early MFE.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2021 bubble was blocked because of a profile corporate-action candidate; clean 2024 event window still shows the same pass-through false-positive risk."}
{"row_type": "case", "case_id": "C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY", "symbol": "237820", "company_name": "플레이디", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "DIGITAL_AD_AGENCY_RECOVERY_WITHOUT_OWNED_PLATFORM", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_C26_PLAYD_2021_02_10_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Ad-cycle recovery created a sharp tactical rally, but 180D path lacked durable owned-platform operating leverage and faded below entry-zone support.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Agency/reseller exposure can be tradable but should not be Stage3-Green without revision and margin bridge."}
{"row_type": "trigger", "trigger_id": "TRG_C26_CAFE24_2023_12_06_STAGE2A", "case_id": "C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE", "symbol": "042000", "company_name": "카페24", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "CREATOR_COMMERCE_PLATFORM_TRAFFIC_OPTIONALITY", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "platform ad revenue / commerce traffic operating leverage", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-05", "evidence_available_at_that_date": "Google/YouTube commerce route and strategic platform partnership optionality became public; stock-web row shows immediate 2023-12-06 repricing.", "evidence_source": "public press/disclosure summary; stock-web tradable shards 2023/2024", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042000/2023.csv|atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv", "profile_path": "atlas/symbol_profiles/042/042000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-12-06", "entry_price": 22150, "MFE_30D_pct": 55.08, "MFE_90D_pct": 55.08, "MFE_180D_pct": 93.91, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": 0.0, "MAE_90D_pct": -29.98, "MAE_180D_pct": -33.82, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 42950, "drawdown_after_peak_pct": -65.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_CAFE24_2023_12_06_22150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_CAFE24_2024_06_20_4B", "case_id": "C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE", "symbol": "042000", "company_name": "카페24", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "CREATOR_COMMERCE_PLATFORM_TRAFFIC_OPTIONALITY", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "platform ad revenue / commerce traffic operating leverage", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test", "trigger_type": "4B", "trigger_date": "2024-06-20", "evidence_available_at_that_date": "Event-premium and valuation overheat became the dominant risk after a very large move without enough confirmed revenue revision to justify full Green continuation.", "evidence_source": "stock-web 2024 peak window; narrative valuation overlay", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042000/2024.csv", "profile_path": "atlas/symbol_profiles/042/042000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-20", "entry_price": 41750, "MFE_30D_pct": 2.87, "MFE_90D_pct": 2.87, "MFE_180D_pct": 2.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -33.89, "MAE_90D_pct": -42.87, "MAE_180D_pct": -42.87, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 42950, "drawdown_after_peak_pct": -65.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_CAFE24_2024_06_20_41750", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_NHNKCP_2024_02_14_STAGE2A", "case_id": "C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN", "symbol": "060250", "company_name": "NHN KCP", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PAYMENT_PLATFORM_VOLUME_WITH_MARGIN_DURABILITY_TEST", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "platform ad revenue / commerce traffic operating leverage", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "evidence_available_at_that_date": "Payment/PG relief and volume-route narrative became visible; however the evidence was not an owned ad-inventory or margin-bridge confirmation.", "evidence_source": "public earnings/news summary; stock-web 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/060/060250/2024.csv", "profile_path": "atlas/symbol_profiles/060/060250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-14", "entry_price": 11770, "MFE_30D_pct": 32.54, "MFE_90D_pct": 32.54, "MFE_180D_pct": 32.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.71, "MAE_90D_pct": -22.09, "MAE_180D_pct": -31.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 15600, "drawdown_after_peak_pct": -48.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "false_break", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_NHNKCP_2024_02_14_11770", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_DANAL_2021_11_17_STAGE2A", "case_id": "C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF", "symbol": "064260", "company_name": "다날", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PAYMENT_TOKEN_EVENT_PREMIUM_BLOWOFF_GUARD", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "platform ad revenue / commerce traffic operating leverage", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-11-17", "evidence_available_at_that_date": "Payment-token/paycoin optionality narrative accelerated; evidence was event-premium/optionality rather than confirmed platform operating leverage.", "evidence_source": "public event/theme summary; stock-web 2021/2022 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064260/2021.csv|atlas/ohlcv_tradable_by_symbol_year/064/064260/2022.csv", "profile_path": "atlas/symbol_profiles/064/064260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-11-17", "entry_price": 10800, "MFE_30D_pct": 74.54, "MFE_90D_pct": 74.54, "MFE_180D_pct": 74.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.94, "MAE_90D_pct": -13.43, "MAE_180D_pct": -39.91, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-12-13", "peak_price": 18850, "drawdown_after_peak_pct": -65.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_DANAL_2021_11_17_10800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_DANAL_2021_12_13_4B", "case_id": "C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF", "symbol": "064260", "company_name": "다날", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "PAYMENT_TOKEN_EVENT_PREMIUM_BLOWOFF_GUARD", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "platform ad revenue / commerce traffic operating leverage", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test", "trigger_type": "4B", "trigger_date": "2021-12-13", "evidence_available_at_that_date": "Peak-window valuation/event premium; full 4B should require non-price overheat/optionality exhaustion, not price-only blowoff alone.", "evidence_source": "stock-web peak window; event-premium overlay", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064260/2021.csv|atlas/ohlcv_tradable_by_symbol_year/064/064260/2022.csv", "profile_path": "atlas/symbol_profiles/064/064260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-12-13", "entry_price": 17200, "MFE_30D_pct": 9.59, "MFE_90D_pct": 9.59, "MFE_180D_pct": 9.59, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -36.05, "MAE_90D_pct": -45.64, "MAE_180D_pct": -62.27, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-12-13", "peak_price": 18850, "drawdown_after_peak_pct": -65.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_DANAL_2021_12_13_17200", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_FSN_2024_02_01_STAGE2A", "case_id": "C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH", "symbol": "214270", "company_name": "FSN", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "AI_ADTECH_THEME_PASS_THROUGH_FALSE_POSITIVE", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "platform ad revenue / commerce traffic operating leverage", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "AI/adtech theme repricing without owned traffic/inventory or confirmed margin bridge; 2024 window chosen because 2021 bubble overlaps a profile corporate-action candidate.", "evidence_source": "public theme/news summary; stock-web 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214270/2024.csv", "profile_path": "atlas/symbol_profiles/214/214270.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 3245, "MFE_30D_pct": 16.33, "MFE_90D_pct": 16.33, "MFE_180D_pct": 16.33, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.26, "MAE_90D_pct": -41.6, "MAE_180D_pct": -52.23, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 3775, "drawdown_after_peak_pct": -58.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_FSN_2024_02_01_3245", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_C26_PLAYD_2021_02_10_STAGE2A", "case_id": "C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY", "symbol": "237820", "company_name": "플레이디", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "fine_archetype_id": "DIGITAL_AD_AGENCY_RECOVERY_WITHOUT_OWNED_PLATFORM", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "platform ad revenue / commerce traffic operating leverage", "loop_objective": "auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test|green_strictness_stress_test|stage2_actionable_bonus_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-02-10", "evidence_available_at_that_date": "Digital advertising recovery proxy; the company is closer to an agency/performance-marketing conduit than owned platform inventory.", "evidence_source": "public ad-cycle summary; stock-web 2021 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/237/237820/2021.csv", "profile_path": "atlas/symbol_profiles/237/237820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-10", "entry_price": 8940, "MFE_30D_pct": 40.38, "MFE_90D_pct": 40.38, "MFE_180D_pct": 40.38, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.05, "MAE_90D_pct": -7.05, "MAE_180D_pct": -20.02, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-31", "peak_price": 12550, "drawdown_after_peak_pct": -43.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "false_break", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C26_PLAYD_2021_02_10_8940", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_CAFE24_202312_GOOGLE_YOUTUBE_COMMERCE_ROUTE", "trigger_id": "TRG_C26_CAFE24_2023_12_06_STAGE2A", "symbol": "042000", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 42, "revision_score": 35, "relative_strength_score": 86, "customer_quality_score": 82, "policy_or_regulatory_score": 62, "valuation_repricing_score": 72, "execution_risk_score": 44, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": "unknown_or_not_supported", "creator_commerce_conversion_score": "unknown_or_not_supported", "payment_take_rate_durability_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "event_premium_guard": "unknown_or_not_supported"}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow / high Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 42, "revision_score": 35, "relative_strength_score": 86, "customer_quality_score": 82, "policy_or_regulatory_score": 62, "valuation_repricing_score": 72, "execution_risk_score": 44, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": 88, "creator_commerce_conversion_score": 84, "payment_take_rate_durability_score": 0, "ad_agency_pass_through_risk_score": 0, "payment_token_event_premium_score": 0, "event_premium_guard": 22}, "weighted_score_after": 84.5, "stage_label_after": "Stage3-Yellow-high / conditional Green", "changed_components": ["owned_traffic_score", "creator_commerce_conversion_score", "payment_take_rate_durability_score", "ad_agency_pass_through_risk_score", "event_premium_guard"], "component_delta_explanation": "C26 shadow profile rewards owned traffic / owned commerce inventory / conversion-to-margin and discounts payment volume or ad agency pass-through without margin bridge. Theme blowoff rows route to 4B, not positive Stage3.", "MFE_90D_pct": 55.08, "MAE_90D_pct": -29.98, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_NHNKCP_202402_PG_RELIEF_RALLY_NO_DURABLE_MARGIN", "trigger_id": "TRG_C26_NHNKCP_2024_02_14_STAGE2A", "symbol": "060250", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 38, "revision_score": 44, "relative_strength_score": 76, "customer_quality_score": 58, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": "unknown_or_not_supported", "creator_commerce_conversion_score": "unknown_or_not_supported", "payment_take_rate_durability_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "event_premium_guard": "unknown_or_not_supported"}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 38, "revision_score": 44, "relative_strength_score": 76, "customer_quality_score": 58, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": 36, "creator_commerce_conversion_score": 0, "payment_take_rate_durability_score": 38, "ad_agency_pass_through_risk_score": 0, "payment_token_event_premium_score": 0, "event_premium_guard": 60}, "weighted_score_after": 69.0, "stage_label_after": "Stage2 / watch only", "changed_components": ["owned_traffic_score", "creator_commerce_conversion_score", "payment_take_rate_durability_score", "ad_agency_pass_through_risk_score", "event_premium_guard"], "component_delta_explanation": "C26 shadow profile rewards owned traffic / owned commerce inventory / conversion-to-margin and discounts payment volume or ad agency pass-through without margin bridge. Theme blowoff rows route to 4B, not positive Stage3.", "MFE_90D_pct": 32.54, "MAE_90D_pct": -22.09, "score_return_alignment_label": "current_profile_overpromoted_or_requires_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_DANAL_202111_PAYCOIN_PAYMENT_THEME_BLOWOFF", "trigger_id": "TRG_C26_DANAL_2021_11_17_STAGE2A", "symbol": "064260", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 22, "relative_strength_score": 95, "customer_quality_score": 45, "policy_or_regulatory_score": 70, "valuation_repricing_score": 92, "execution_risk_score": 62, "legal_or_contract_risk_score": 58, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": "unknown_or_not_supported", "creator_commerce_conversion_score": "unknown_or_not_supported", "payment_take_rate_durability_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "event_premium_guard": "unknown_or_not_supported"}, "weighted_score_before": 79.0, "stage_label_before": "Stage3-Yellow risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 22, "relative_strength_score": 95, "customer_quality_score": 45, "policy_or_regulatory_score": 70, "valuation_repricing_score": 92, "execution_risk_score": 62, "legal_or_contract_risk_score": 58, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": 28, "creator_commerce_conversion_score": 0, "payment_take_rate_durability_score": 0, "ad_agency_pass_through_risk_score": 0, "payment_token_event_premium_score": 92, "event_premium_guard": 88}, "weighted_score_after": 66.5, "stage_label_after": "4B risk overlay / no positive Green", "changed_components": ["owned_traffic_score", "creator_commerce_conversion_score", "payment_take_rate_durability_score", "ad_agency_pass_through_risk_score", "event_premium_guard"], "component_delta_explanation": "C26 shadow profile rewards owned traffic / owned commerce inventory / conversion-to-margin and discounts payment volume or ad agency pass-through without margin bridge. Theme blowoff rows route to 4B, not positive Stage3.", "MFE_90D_pct": 74.54, "MAE_90D_pct": -13.43, "score_return_alignment_label": "current_profile_overpromoted_or_requires_guard", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_FSN_202402_AI_ADTECH_THEME_PASS_THROUGH", "trigger_id": "TRG_C26_FSN_2024_02_01_STAGE2A", "symbol": "214270", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 28, "relative_strength_score": 82, "customer_quality_score": 36, "policy_or_regulatory_score": 10, "valuation_repricing_score": 76, "execution_risk_score": 50, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": "unknown_or_not_supported", "creator_commerce_conversion_score": "unknown_or_not_supported", "payment_take_rate_durability_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "event_premium_guard": "unknown_or_not_supported"}, "weighted_score_before": 75.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 24, "revision_score": 28, "relative_strength_score": 82, "customer_quality_score": 36, "policy_or_regulatory_score": 10, "valuation_repricing_score": 76, "execution_risk_score": 50, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": 24, "creator_commerce_conversion_score": 0, "payment_take_rate_durability_score": 0, "ad_agency_pass_through_risk_score": 88, "payment_token_event_premium_score": 0, "event_premium_guard": 76}, "weighted_score_after": 65.0, "stage_label_after": "Stage2 / watch only", "changed_components": ["owned_traffic_score", "creator_commerce_conversion_score", "payment_take_rate_durability_score", "ad_agency_pass_through_risk_score", "event_premium_guard"], "component_delta_explanation": "C26 shadow profile rewards owned traffic / owned commerce inventory / conversion-to-margin and discounts payment volume or ad agency pass-through without margin bridge. Theme blowoff rows route to 4B, not positive Stage3.", "MFE_90D_pct": 16.33, "MAE_90D_pct": -41.6, "score_return_alignment_label": "current_profile_overpromoted_or_requires_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c26_shadow", "case_id": "C26_PLAYD_202102_AD_RECOVERY_AGENCY_PROXY", "trigger_id": "TRG_C26_PLAYD_2021_02_10_STAGE2A", "symbol": "237820", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 36, "revision_score": 42, "relative_strength_score": 78, "customer_quality_score": 38, "policy_or_regulatory_score": 8, "valuation_repricing_score": 68, "execution_risk_score": 42, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": "unknown_or_not_supported", "creator_commerce_conversion_score": "unknown_or_not_supported", "payment_take_rate_durability_score": "unknown_or_not_supported", "ad_agency_pass_through_risk_score": "unknown_or_not_supported", "event_premium_guard": "unknown_or_not_supported"}, "weighted_score_before": 75.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 36, "revision_score": 42, "relative_strength_score": 78, "customer_quality_score": 38, "policy_or_regulatory_score": 8, "valuation_repricing_score": 68, "execution_risk_score": 42, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "owned_traffic_score": 20, "creator_commerce_conversion_score": 0, "payment_take_rate_durability_score": 0, "ad_agency_pass_through_risk_score": 84, "payment_token_event_premium_score": 0, "event_premium_guard": 62}, "weighted_score_after": 67.0, "stage_label_after": "Stage2 / watch only", "changed_components": ["owned_traffic_score", "creator_commerce_conversion_score", "payment_take_rate_durability_score", "ad_agency_pass_through_risk_score", "event_premium_guard"], "component_delta_explanation": "C26 shadow profile rewards owned traffic / owned commerce inventory / conversion-to-margin and discounts payment volume or ad agency pass-through without margin bridge. Theme blowoff rows route to 4B, not positive Stage3.", "MFE_90D_pct": 40.38, "MAE_90D_pct": -7.05, "score_return_alignment_label": "current_profile_overpromoted_or_requires_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "52", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_canonical_archetype_count": 0, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["payment_volume_without_margin_bridge_false_positive", "ad_agency_pass_through_false_positive", "event_premium_blowoff_needs_4B_overlay", "owned_creator_commerce_stage2_missed_structural"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "avg=23.8; same_archetype_new_symbol_count=5; repeated_same_symbol_penalty=0; repeated_same_trigger_date_penalty=0", "auto_selected_coverage_gap": "C26 previous coverage concentrated on NAVER/Kakao/SOOP/Nasmedia/Incross; this loop adds commerce-platform, PG/payment, crypto-payment, AI-adtech and agency-proxy cases."}
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
next_round = R13_loop_53
recommended_scope = L8_PLATFORM_CONTENT_SW_SECURITY / C27_CONTENT_IP_GLOBAL_MONETIZATION
reason = after C26 commerce/payment/adtech guard and C28 security retention guard, refresh C27 with non-game content IP and platform monetization residual cases.
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json` from `Songdaiki/stock-web`, max_date `2026-02-20`.
- Symbol profiles: `042000`, `060250`, `064260`, `214270`, `237820` under `atlas/symbol_profiles/<prefix>/<ticker>.json`.
- OHLC rows used: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv` for the stated years.
- Evidence source notes are used as historical trigger annotations; no current/live stock discovery was performed.
