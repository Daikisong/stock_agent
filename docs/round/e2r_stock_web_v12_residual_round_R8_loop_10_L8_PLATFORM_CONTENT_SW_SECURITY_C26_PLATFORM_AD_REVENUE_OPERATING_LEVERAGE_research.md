# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R8
loop = 10
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_AD_OPERATING_LEVERAGE_OWNED_TRAFFIC_VS_AGENCY_RESELLER
output_file = e2r_stock_web_v12_residual_round_R8_loop_10_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not live candidate research, not a stock recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The purpose of this loop is not to re-prove those global axes. It tests a remaining C26 residual: **generic digital advertising recovery looks similar in text, but the stock path separates owned-platform ad-product conversion from agency/reseller recovery**.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_AD_OPERATING_LEVERAGE_OWNED_TRAFFIC_VS_AGENCY_RESELLER
loop_objective = residual_missed_structural_mining / residual_false_positive_mining / sector_specific_rule_discovery / canonical_archetype_compression / 4B_non_price_requirement_stress_test / coverage_gap_fill
```

The working compression is:

```text
C26 positive core:
owned traffic + ad product conversion + margin bridge + revision confirmation

C26 counterexample guard:
ad agency / reseller / media buying recovery without owned traffic or durable operating leverage

C26 4B overlay:
price-only local peak is insufficient; full 4B needs margin slowdown, revision slowdown, policy/regulatory cap, or other non-price evidence
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were used only for coverage awareness and duplicate avoidance. The ingest artifact reports 398 discovered MD files, 107 result MDs, 1,940 validated trigger rows, 1,376 representative aggregate rows, and coverage across R1~R13. It also shows many rejected rows came from missing/invalid price source fields, supporting continued strict use of stock-web price fields.

The applied calibration artifact already contains global adjustments for Stage2 actionable evidence, Yellow threshold, stricter Green, Green revision minimum, cross-evidence buffer, full 4B non-price requirement, and hard 4C routing. This loop therefore avoids proposing another global ad-recovery rule.

Novelty check:

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
new_fine_archetype_count = 3
new_trigger_family_count = 4
required_new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest values used:

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
markets = ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
price_basis = tradable_raw
```

Schema basis:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative triggers below meet the v12 historical gate:

```text
- trigger_date is a past event
- entry_date exists in stock-web tradable shard
- at least 180 forward trading rows are available
- high / low / close / volume are present
- MFE_30D / 90D / 180D and MAE_30D / 90D / 180D are computed
- 180D corporate-action contamination is not present for representative windows
```

Kakao has a later 2021-04-15 corporate-action candidate in the profile, but the 2020-05-08 representative 180D window ends before that. Incross has a 2022-07-11 corporate-action candidate, outside the 2021-02-10 representative window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| OWNED_SEARCH_COMMERCE_AD_PRODUCT_MARGIN_BRIDGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Owned traffic, ad product conversion, and commerce/search margin bridge |
| TALKBIZ_AD_PRODUCT_COMMERCE_OPERATING_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Messenger/social graph ad product with commerce conversion and margin bridge |
| LIVE_STREAMING_CREATOR_PLATFORM_ARPU_AD_OPERATING_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Creator platform ARPU and recurring monetization operating leverage |
| AD_AGENCY_RESELLER_RECOVERY_WITHOUT_OWNED_TRAFFIC_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Negative guard: ad recovery without owned traffic is not enough |
| ADTECH_RESELLER_WITHOUT_DURABLE_OPERATING_LEVERAGE | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | Negative guard: adtech/reseller optionality without durable conversion |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---:|---|
| R8L10_C26_035420_NAVER_2020_owned_search_commerce_ad_leverage | 035420 | NAVER | positive | Stage2-Actionable | 2020-04-27 | 197,500 | 75.7 | -2.53 | current_profile_too_late |
| R8L10_C26_035720_KAKAO_2020_talkbiz_ad_commerce_leverage | 035720 | 카카오 | positive | Stage2-Actionable | 2020-05-08 | 206,000 | 104.13 | -0.97 | current_profile_too_late |
| R8L10_C26_067160_SOOP_2021_streaming_ad_donation_operating_leverage | 067160 | SOOP | positive | Stage2-Actionable | 2021-05-03 | 89,500 | 91.4 | -2.01 | current_profile_too_late |
| R8L10_C26_089600_NASMEDIA_2021_ad_recovery_reseller_false_positive | 089600 | KT나스미디어 | counterexample | Stage3-Yellow | 2021-02-10 | 41,050 | 8.53 | -16.44 | current_profile_false_positive |
| R8L10_C26_216050_INCROSS_2021_adtech_reseller_no_durable_platform_leverage | 216050 | 인크로스 | counterexample | Stage3-Yellow | 2021-02-10 | 51,500 | 23.3 | -6.41 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 5
calibration_usable_trigger_count = 6
```

Interpretation:

- NAVER, Kakao, and SOOP show that C26 can move early when owned traffic and ad-product conversion produce a visible margin bridge.
- Nasmedia and Incross show that ad recovery or adtech optionality can look semantically similar, but if the company is closer to agency/reseller economics, the return profile weakens and MAE rises.
- The residual is not “make Stage2 earlier”; it is “separate platform-owned operating leverage from ad-recovery pass-through.”

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| 035420 | owned search/commerce ad product | disclosure, owned traffic, early revision | margin bridge, financial visibility | none |
| 035720 | TalkBiz/commercial ad product | disclosure, product conversion, early revision | confirmed revision, margin bridge | later regulatory overlay; not trained as positive |
| 067160 | creator platform ARPU/ad leverage | platform ARPU, paid-item conversion | margin bridge, repeat monetization | price-only local 4B overlay |
| 089600 | agency/reseller ad recovery | disclosure, ad recovery | weak multi-source confirmation | valuation/ad-cycle peak |
| 216050 | adtech/reseller optionality | disclosure, adtech recovery | weak durability | price-only valuation peak |

## 10. Price Data Source Map

| symbol | profile_path | representative shard |
|---|---|---|
| 035420 | atlas/symbol_profiles/035/035420.json | atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv |
| 035720 | atlas/symbol_profiles/035/035720.json | atlas/ohlcv_tradable_by_symbol_year/035/035720/2020.csv |
| 067160 | atlas/symbol_profiles/067/067160.json | atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv |
| 089600 | atlas/symbol_profiles/089/089600.json | atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv |
| 216050 | atlas/symbol_profiles/216/216050.json | atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_90D_pct | peak_date | peak_price | aggregate? |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|
| TRG_NAVER_2020Q1_STAGE2_ACTIONABLE_2020_04_27 | 035420 | Stage2-Actionable | 2020-04-27 | 197,500 | 25.32 | 75.7 | 75.7 | -2.53 | 2020-08-27 | 347,000 | True |
| TRG_KAKAO_2020Q1_STAGE2_ACTIONABLE_2020_05_08 | 035720 | Stage2-Actionable | 2020-05-08 | 206,000 | 40.29 | 104.13 | 104.13 | -0.97 | 2020-08-31 | 420,500 | True |
| TRG_SOOP_2021Q1_STAGE2_ACTIONABLE_2021_05_03 | 067160 | Stage2-Actionable | 2021-05-03 | 89,500 | 25.59 | 91.4 | 178.32 | -2.01 | 2021-11-09 | 249,100 | True |
| TRG_NASMEDIA_2021_AD_RECOVERY_FALSE_POSITIVE_2021_02_10 | 089600 | Stage3-Yellow | 2021-02-10 | 41,050 | 6.94 | 8.53 | 9.38 | -16.44 | 2021-06-24 | 44,900 | True |
| TRG_INCROSS_2021_ADTECH_RECOVERY_FALSE_POSITIVE_2021_02_10 | 216050 | Stage3-Yellow | 2021-02-10 | 51,500 | 17.28 | 23.3 | 23.3 | -6.41 | 2021-03-29 | 63,500 | True |
| TRG_SOOP_2021_PRICE_LOCAL_4B_OVERLAY_2021_11_09 | 067160 | 4B-overlay | 2021-11-09 | 237,000 | 2.28 | 2.28 | 2.28 | -35.0 | 2021-11-09 | 249,100 | False |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows:

| symbol | entry | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | outcome |
|---|---:|---:|---:|---:|---:|---|
| 035420 NAVER | 2020-04-27 | 197,500 | +25.32 / -2.53 | +75.70 / -2.53 | +75.70 / -2.53 | structural_success |
| 035720 Kakao | 2020-05-08 | 206,000 | +40.29 / -0.97 | +104.13 / -0.97 | +104.13 / -0.97 | structural_success |
| 067160 SOOP | 2021-05-03 | 89,500 | +25.59 / -2.01 | +91.40 / -2.01 | +178.32 / -2.01 | structural_success |
| 089600 Nasmedia | 2021-02-10 | 41,050 | +6.94 / -16.44 | +8.53 / -16.44 | +9.38 / -16.44 | failed_rerating |
| 216050 Incross | 2021-02-10 | 51,500 | +17.28 / -6.41 | +23.30 / -6.41 | +23.30 / -6.41 | failed_rerating |

## 13. Current Calibrated Profile Stress Test

- **NAVER (035420)**: P0 verdict `current_profile_too_late`. current calibrated profile likely waited for stronger confirmed revision; price path shows Stage2/actionable evidence already captured most of the C26 operating-leverage rerating.
- **카카오 (035720)**: P0 verdict `current_profile_too_late`. Current calibrated profile protects against late/false Green but still under-recognizes C26 platform-owned ad-product conversion when margin bridge is already visible.
- **SOOP (067160)**: P0 verdict `current_profile_too_late`. The price path rewards platform-level ARPU/margin leverage. A generic ad recovery score would under-explain why this case outperformed agency/reseller peers.
- **KT나스미디어 (089600)**: P0 verdict `current_profile_false_positive`. P0 would over-credit sector ad recovery as platform operating leverage; return path shows weak upside and high MAE.
- **인크로스 (216050)**: P0 verdict `current_profile_false_positive`. Moderate MFE existed but not a durable C26 rerating. The case argues for a reseller/agency discount rather than a broad ad-recovery bonus.

Answers to required questions:

```text
1. P0 judged owned-platform cases as Yellow/late-Green candidates, not early C26 Green.
2. That was partially wrong: NAVER/Kakao/SOOP showed strong MFE with low MAE from Stage2-Actionable dates.
3. Existing Stage2 bonus was useful but insufficient for owned-platform ad-product conversion.
4. Yellow threshold 75 was appropriate; the problem is not Yellow access.
5. Green threshold 87 / revision 55 remains generally appropriate, but C26 needs component-specific bridge scoring.
6. price-only blowoff guard remains appropriate.
7. full 4B non-price requirement remains appropriate.
8. hard 4C routing is not directly tested here; regulatory/policy shocks should remain thesis-break overlays only.
```

## 14. Stage2 / Yellow / Green Comparison

Green lateness audit:

| symbol | Stage2/actionable entry | assumed Green confirmation | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 035420 | 197,500 | ~254,000 proxy | 347,000 | 0.38 | Green somewhat late |
| 035720 | 206,000 | ~294,000 proxy | 420,500 | 0.41 | Green somewhat late |
| 067160 | 89,500 | ~165,000 proxy | 249,100 | 0.47 | Green somewhat late |
| 089600 | 41,050 | no valid Green | 44,900 | N/A | false positive guard case |
| 216050 | 51,500 | no valid Green | 63,500 | N/A | failed durability case |

## 15. 4B Local vs Full-window Timing Audit

The SOOP price-only overlay is useful as a 4B timing stress case, but not as a full 4B production rule.

```text
TRG_SOOP_2021_PRICE_LOCAL_4B_OVERLAY_2021_11_09
four_b_local_peak_proximity = 1.0
four_b_full_window_peak_proximity = 1.0
four_b_evidence_type = price_only / valuation_blowoff
four_b_timing_verdict = price_only_local_4B_not_full_4B_without_non_price_evidence
```

Conclusion: keep `full_4b_requires_non_price_evidence`, and add C26-specific non-price vocabulary: margin slowdown, ad take-rate slowdown, user/creator growth deceleration, advertiser budget compression, and regulatory/platform fee cap.

## 16. 4C Protection Audit

No representative hard 4C row is proposed in this loop. Kakao’s later regulatory/policy risk is noted as a thesis-break overlay candidate but not quantified in this MD because the loop objective is C26 positive/counterexample separation.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_routing = kept
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
candidate = L8_owned_platform_ad_operating_leverage_gate
```

Rule candidate:

```text
If a platform/ad case has:
  owned_traffic_score high
  ad_product_conversion_score high
  margin_bridge_score high
  revision_score at least mid
then allow C26-specific positive promotion.

If the case is mainly:
  media buying
  agency/reseller recovery
  adtech optionality without owned inventory
then apply agency_reseller_discount_guard.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
candidate = c26_owned_traffic_ad_product_margin_bridge_gate
```

Preferred canonical rule:

```text
C26 Green/near-Green should require at least two of:
- owned traffic / captive user graph
- ad product conversion route
- operating margin bridge
- recurring advertiser/merchant/customer conversion
- confirmed revision or visible earnings quality

C26 should discount:
- generic ad recovery
- media-buying agency exposure
- reseller economics
- price-only theme blowoff
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current global calibrated | none | 5 | 5 | 60.61 | -5.67 | 78.17 | -5.67 | 40% | 2 | 3 | partially aligned; over-promotes agency/recovery and under-promotes owned platform leverage |
| P0b_e2r_2_0_baseline_reference | rollback reference | no stock-web v12 adjustments | 5 | 5 | 60.61 | -5.67 | 78.17 | -5.67 | 60% | 1 | 2 | worse; weaker Green discipline and no C26 split |
| P1_L8_sector_specific_candidate | sector shadow | owned traffic gate; reseller discount | 5 | 5 | 60.61 | -5.67 | 78.17 | -5.67 | 0% | 0 | 1 | improved |
| P2_C26_archetype_candidate | canonical shadow | C26 owned ad product + margin bridge | 5 | 5 | 60.61 | -5.67 | 78.17 | -5.67 | 0% | 0 | 1 | improved; preferred scope |
| P3_counterexample_guard_profile | guard shadow | agency/reseller discount; no price-only promotion | 2 | 2 | 15.92 | -11.43 | 16.34 | -11.43 | 0% | 0 | 0 | improved false-positive control |


## 20. Score-Return Alignment Matrix

| case | P0 verdict | return alignment | proposed correction |
|---|---|---|---|
| NAVER 2020 | too late | strong MFE / low MAE | add owned traffic + ad product + margin bridge positive gate |
| Kakao 2020 | too late | strong MFE / low MAE | add TalkBiz conversion and margin bridge component |
| SOOP 2021 | too late | very strong 180D MFE | add platform ARPU/retention supplement |
| Nasmedia 2021 | false positive | weak MFE / high MAE | agency/reseller discount |
| Incross 2021 | false positive | moderate local MFE, no durable rerating | agency/reseller discount and no Green promotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | PLATFORM_AD_OPERATING_LEVERAGE_OWNED_TRAFFIC_VS_AGENCY_RESELLER | 3 | 2 | 1 | 0 | 5 | 0 | 6 | 5 | 5 | true | true | Need holdout for global ad platforms and app-store/platform-fee regulatory 4C |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_too_late_for_owned_platform_ad_leverage
  - current_profile_false_positive_for_agency_reseller_ad_recovery
  - price_only_local_peak_not_full_4B
new_axis_proposed:
  - c26_owned_traffic_ad_product_margin_bridge_gate
  - c26_agency_reseller_discount_guard
  - c26_price_local_peak_requires_margin_or_revision_slowdown_for_full_4b
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema checked
- symbol profiles checked
- tradable shard paths identified
- 30D/90D/180D MFE/MAE computed from stock-web raw-unadjusted tradable rows
- representative trigger dedupe fields included
- current calibrated profile stress test included
```

Not validated:

```text
- no live candidate scan
- no current Stage3 recommendation
- no stock_agent code access or patch
- no brokerage/API work
- no production scoring change
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c26_owned_traffic_ad_product_margin_bridge_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Owned traffic + ad product conversion + margin bridge separated NAVER/Kakao/SOOP from agency/reseller names","Raised positive structural cases without raising agency false positives","TRG_NAVER_2020Q1_STAGE2_ACTIONABLE_2020_04_27|TRG_KAKAO_2020Q1_STAGE2_ACTIONABLE_2020_05_08|TRG_SOOP_2021Q1_STAGE2_ACTIONABLE_2021_05_03",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_agency_reseller_discount_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Ad recovery without owned traffic or durable margin bridge produced weak MFE/high MAE","Reduced Nasmedia/Incross false positives","TRG_NASMEDIA_2021_AD_RECOVERY_FALSE_POSITIVE_2021_02_10|TRG_INCROSS_2021_ADTECH_RECOVERY_FALSE_POSITIVE_2021_02_10",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c26_price_local_peak_requires_margin_or_revision_slowdown_for_full_4b,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Price-only platform-ad blowoffs can be local peaks but not full 4B without non-price slowdown","Kept full_4b_requires_non_price_evidence and added C26-specific evidence vocabulary","TRG_SOOP_2021_PRICE_LOCAL_4B_OVERLAY_2021_11_09",1,0,0,low,overlay_shadow_only,"4B overlay only; not positive-entry calibration"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R8L10_C26_035420_NAVER_2020_owned_search_commerce_ad_leverage","symbol":"035420","company_name":"NAVER","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"OWNED_SEARCH_COMMERCE_AD_PRODUCT_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_NAVER_2020Q1_STAGE2_ACTIONABLE_2020_04_27","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current calibrated profile likely waited for stronger confirmed revision; price path shows Stage2/actionable evidence already captured most of the C26 operating-leverage rerating.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Representative positive case: owned traffic + commerce/search ad product conversion had a margin bridge; not a generic ad recovery row."}
{"row_type":"case","case_id":"R8L10_C26_035720_KAKAO_2020_talkbiz_ad_commerce_leverage","symbol":"035720","company_name":"카카오","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALKBIZ_AD_PRODUCT_COMMERCE_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_KAKAO_2020Q1_STAGE2_ACTIONABLE_2020_05_08","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Current calibrated profile protects against late/false Green but still under-recognizes C26 platform-owned ad-product conversion when margin bridge is already visible.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Representative positive case. Later regulatory risk should train 4C/overlay only, not positive-entry weights."}
{"row_type":"case","case_id":"R8L10_C26_067160_SOOP_2021_streaming_ad_donation_operating_leverage","symbol":"067160","company_name":"SOOP","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_CREATOR_PLATFORM_ARPU_AD_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_SOOP_2021Q1_STAGE2_ACTIONABLE_2021_05_03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"The price path rewards platform-level ARPU/margin leverage. A generic ad recovery score would under-explain why this case outperformed agency/reseller peers.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive case but not identical to NAVER/Kakao: creator ecosystem monetization adds ARPU/retention evidence."}
{"row_type":"case","case_id":"R8L10_C26_089600_NASMEDIA_2021_ad_recovery_reseller_false_positive","symbol":"089600","company_name":"KT나스미디어","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_RESELLER_RECOVERY_WITHOUT_OWNED_TRAFFIC_LEVERAGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_NASMEDIA_2021_AD_RECOVERY_FALSE_POSITIVE_2021_02_10","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"P0 would over-credit sector ad recovery as platform operating leverage; return path shows weak upside and high MAE.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample. Useful because the evidence is semantically close to C26 but economically closer to agency/reseller cyclicality."}
{"row_type":"case","case_id":"R8L10_C26_216050_INCROSS_2021_adtech_reseller_no_durable_platform_leverage","symbol":"216050","company_name":"인크로스","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_RESELLER_WITHOUT_DURABLE_OPERATING_LEVERAGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_INCROSS_2021_ADTECH_RECOVERY_FALSE_POSITIVE_2021_02_10","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Moderate MFE existed but not a durable C26 rerating. The case argues for a reseller/agency discount rather than a broad ad-recovery bonus.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample with some upside but poor persistence; should not train Green promotion."}
{"row_type":"trigger","trigger_id":"TRG_NAVER_2020Q1_STAGE2_ACTIONABLE_2020_04_27","case_id":"R8L10_C26_035420_NAVER_2020_owned_search_commerce_ad_leverage","symbol":"035420","company_name":"NAVER","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"OWNED_SEARCH_COMMERCE_AD_PRODUCT_MARGIN_BRIDGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":["residual_missed_structural_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2020-04-24","evidence_available_at_that_date":"2020 Q1 resilience: commerce/search/payment traffic conversion and early margin bridge visible after earnings/news flow; exact intraday timing treated as next-trading-day close.","evidence_source":"Historical company disclosure / earnings-call summary / contemporaneous analyst note proxy; price verified in stock-web 035420 2020 shard.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv","profile_path":"atlas/symbol_profiles/035/035420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-04-27","entry_price":197500,"MFE_30D_pct":25.32,"MFE_90D_pct":75.7,"MFE_180D_pct":75.7,"MFE_1Y_pct":107.59,"MFE_2Y_pct":null,"MAE_30D_pct":-2.53,"MAE_90D_pct":-2.53,"MAE_180D_pct":-2.53,"MAE_1Y_pct":-2.53,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2020-08-27","peak_price":347000,"drawdown_after_peak_pct":-19.31,"green_lateness_ratio":"0.38","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L10_C26_035420_NAVER_2020_owned_search_commerce_ad_leverage__2020-04-27__197500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_KAKAO_2020Q1_STAGE2_ACTIONABLE_2020_05_08","case_id":"R8L10_C26_035720_KAKAO_2020_talkbiz_ad_commerce_leverage","symbol":"035720","company_name":"카카오","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALKBIZ_AD_PRODUCT_COMMERCE_OPERATING_LEVERAGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":["residual_missed_structural_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2020-05-07","evidence_available_at_that_date":"2020 Q1 TalkBiz/ad-commerce growth and platform operating leverage visible; disclosure timing conservatively uses next-day close.","evidence_source":"Historical company disclosure / earnings-call summary / contemporaneous analyst note proxy; price verified in stock-web 035720 2020 shard.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2020.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-05-08","entry_price":206000,"MFE_30D_pct":40.29,"MFE_90D_pct":104.13,"MFE_180D_pct":104.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.97,"MAE_90D_pct":-0.97,"MAE_180D_pct":-0.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2020-08-31","peak_price":420500,"drawdown_after_peak_pct":-22.83,"green_lateness_ratio":"0.41","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; later 2021-04-15 corporate-action candidate is outside this 180D calibration window","same_entry_group_id":"R8L10_C26_035720_KAKAO_2020_talkbiz_ad_commerce_leverage__2020-05-08__206000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_SOOP_2021Q1_STAGE2_ACTIONABLE_2021_05_03","case_id":"R8L10_C26_067160_SOOP_2021_streaming_ad_donation_operating_leverage","symbol":"067160","company_name":"SOOP","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_CREATOR_PLATFORM_ARPU_AD_OPERATING_LEVERAGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":["residual_missed_structural_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2021-04-30","evidence_available_at_that_date":"Streaming platform revenue/ARPU leverage and ad/paid-item conversion visible after Q1 result window.","evidence_source":"Historical company disclosure / earnings-call summary / contemporaneous analyst note proxy; price verified in stock-web 067160 2021 shard.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-03","entry_price":89500,"MFE_30D_pct":25.59,"MFE_90D_pct":91.4,"MFE_180D_pct":178.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.01,"MAE_90D_pct":-2.01,"MAE_180D_pct":-2.01,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-11-09","peak_price":249100,"drawdown_after_peak_pct":-16.3,"green_lateness_ratio":"0.47","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L10_C26_067160_SOOP_2021_streaming_ad_donation_operating_leverage__2021-05-03__89500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_NASMEDIA_2021_AD_RECOVERY_FALSE_POSITIVE_2021_02_10","case_id":"R8L10_C26_089600_NASMEDIA_2021_ad_recovery_reseller_false_positive","symbol":"089600","company_name":"KT나스미디어","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_RESELLER_RECOVERY_WITHOUT_OWNED_TRAFFIC_LEVERAGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":["residual_missed_structural_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"trigger_type":"Stage3-Yellow","trigger_date":"2021-02-10","evidence_available_at_that_date":"Digital advertising recovery and media-buying rebound narrative visible, but owned traffic/product conversion and margin bridge were weak.","evidence_source":"Historical earnings/news/analyst proxy; price verified in stock-web 089600 2021 shard.","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv","profile_path":"atlas/symbol_profiles/089/089600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-10","entry_price":41050,"MFE_30D_pct":6.94,"MFE_90D_pct":8.53,"MFE_180D_pct":9.38,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.44,"MAE_90D_pct":-16.44,"MAE_180D_pct":-16.44,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-24","peak_price":44900,"drawdown_after_peak_pct":-14.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"local valuation/ad-cycle peak but not full C26 structural 4B","four_b_evidence_type":["valuation_blowoff","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L10_C26_089600_NASMEDIA_2021_ad_recovery_reseller_false_positive__2021-02-10__41050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_INCROSS_2021_ADTECH_RECOVERY_FALSE_POSITIVE_2021_02_10","case_id":"R8L10_C26_216050_INCROSS_2021_adtech_reseller_no_durable_platform_leverage","symbol":"216050","company_name":"인크로스","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_RESELLER_WITHOUT_DURABLE_OPERATING_LEVERAGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":["residual_missed_structural_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"trigger_type":"Stage3-Yellow","trigger_date":"2021-02-10","evidence_available_at_that_date":"Adtech/media recovery and affiliated-platform optionality visible, but durable owned-traffic conversion and sustained margin bridge were not confirmed.","evidence_source":"Historical earnings/news/analyst proxy; price verified in stock-web 216050 2021 shard.","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv","profile_path":"atlas/symbol_profiles/216/216050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-10","entry_price":51500,"MFE_30D_pct":17.28,"MFE_90D_pct":23.3,"MFE_180D_pct":23.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.41,"MAE_90D_pct":-6.41,"MAE_180D_pct":-6.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-29","peak_price":63500,"drawdown_after_peak_pct":-19.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local full-window peak existed but positive promotion quality was weak","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; later 2022-07-11 corporate-action candidate outside this window","same_entry_group_id":"R8L10_C26_216050_INCROSS_2021_adtech_reseller_no_durable_platform_leverage__2021-02-10__51500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_SOOP_2021_PRICE_LOCAL_4B_OVERLAY_2021_11_09","case_id":"R8L10_C26_067160_SOOP_2021_streaming_ad_donation_operating_leverage","symbol":"067160","company_name":"SOOP","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_CREATOR_PLATFORM_ARPU_AD_OPERATING_LEVERAGE","sector":"플랫폼·콘텐츠·SW·보안","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":["residual_missed_structural_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","coverage_gap_fill"],"trigger_type":"4B-overlay","trigger_date":"2021-11-09","evidence_available_at_that_date":"Local price/valuation peak after a major platform rerating. No clean non-price slowdown evidence at the local peak.","evidence_source":"stock-web price path plus historical valuation/price-only local peak proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-09","entry_price":237000,"MFE_30D_pct":2.28,"MFE_90D_pct":2.28,"MFE_180D_pct":2.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.03,"MAE_90D_pct":-35.0,"MAE_180D_pct":-44.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-09","peak_price":249100,"drawdown_after_peak_pct":-35.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L10_C26_067160_SOOP_2021_streaming_ad_donation_operating_leverage__2021-11-09__237000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case; 4B overlay timing comparison only","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C26_035420_NAVER_2020_owned_search_commerce_ad_leverage","trigger_id":"TRG_NAVER_2020Q1_STAGE2_ACTIONABLE_2020_04_27","symbol":"035420","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":74,"revision_score":54,"relative_strength_score":78,"customer_quality_score":86,"policy_or_regulatory_score":18,"valuation_repricing_score":69,"execution_risk_score":24,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":92,"ad_product_conversion_score":84},"weighted_score_before":84.2,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":82,"revision_score":58,"relative_strength_score":78,"customer_quality_score":90,"policy_or_regulatory_score":18,"valuation_repricing_score":69,"execution_risk_score":22,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":95,"ad_product_conversion_score":88},"weighted_score_after":87.4,"stage_label_after":"Stage3-Green","changed_components":["owned_traffic_score","ad_product_conversion_score","margin_bridge_score","agency_reseller_exposure_score"],"component_delta_explanation":"C26 shadow profile rewards owned traffic + ad product conversion + margin bridge; discounts ad agency/reseller exposure without durable operating leverage.","MFE_90D_pct":75.7,"MAE_90D_pct":-2.53,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C26_035720_KAKAO_2020_talkbiz_ad_commerce_leverage","trigger_id":"TRG_KAKAO_2020Q1_STAGE2_ACTIONABLE_2020_05_08","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":77,"revision_score":56,"relative_strength_score":86,"customer_quality_score":88,"policy_or_regulatory_score":26,"valuation_repricing_score":64,"execution_risk_score":28,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":94,"ad_product_conversion_score":90},"weighted_score_before":85.9,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":85,"revision_score":61,"relative_strength_score":86,"customer_quality_score":92,"policy_or_regulatory_score":26,"valuation_repricing_score":64,"execution_risk_score":26,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":97,"ad_product_conversion_score":93},"weighted_score_after":88.8,"stage_label_after":"Stage3-Green","changed_components":["owned_traffic_score","ad_product_conversion_score","margin_bridge_score","agency_reseller_exposure_score"],"component_delta_explanation":"C26 shadow profile rewards owned traffic + ad product conversion + margin bridge; discounts ad agency/reseller exposure without durable operating leverage.","MFE_90D_pct":104.13,"MAE_90D_pct":-0.97,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C26_067160_SOOP_2021_streaming_ad_donation_operating_leverage","trigger_id":"TRG_SOOP_2021Q1_STAGE2_ACTIONABLE_2021_05_03","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":70,"revision_score":52,"relative_strength_score":82,"customer_quality_score":78,"policy_or_regulatory_score":12,"valuation_repricing_score":66,"execution_risk_score":30,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":88,"ad_product_conversion_score":80,"arpu_retention_score":84},"weighted_score_before":81.6,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":78,"revision_score":58,"relative_strength_score":82,"customer_quality_score":84,"policy_or_regulatory_score":12,"valuation_repricing_score":66,"execution_risk_score":27,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":92,"ad_product_conversion_score":86,"arpu_retention_score":89},"weighted_score_after":86.9,"stage_label_after":"Stage3-Yellow-high / conditional Green","changed_components":["owned_traffic_score","ad_product_conversion_score","margin_bridge_score","agency_reseller_exposure_score"],"component_delta_explanation":"C26 shadow profile rewards owned traffic + ad product conversion + margin bridge; discounts ad agency/reseller exposure without durable operating leverage.","MFE_90D_pct":91.4,"MAE_90D_pct":-2.01,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C26_089600_NASMEDIA_2021_ad_recovery_reseller_false_positive","trigger_id":"TRG_NASMEDIA_2021_AD_RECOVERY_FALSE_POSITIVE_2021_02_10","symbol":"089600","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":42,"revision_score":50,"relative_strength_score":54,"customer_quality_score":42,"policy_or_regulatory_score":8,"valuation_repricing_score":58,"execution_risk_score":45,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":22,"ad_product_conversion_score":34,"agency_reseller_exposure_score":78},"weighted_score_before":76.4,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":34,"revision_score":45,"relative_strength_score":54,"customer_quality_score":36,"policy_or_regulatory_score":8,"valuation_repricing_score":52,"execution_risk_score":48,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":18,"ad_product_conversion_score":27,"agency_reseller_exposure_score":88},"weighted_score_after":68.2,"stage_label_after":"Stage2 / watch only","changed_components":["owned_traffic_score","ad_product_conversion_score","margin_bridge_score","agency_reseller_exposure_score"],"component_delta_explanation":"C26 shadow profile rewards owned traffic + ad product conversion + margin bridge; discounts ad agency/reseller exposure without durable operating leverage.","MFE_90D_pct":8.53,"MAE_90D_pct":-16.44,"score_return_alignment_label":"current_profile_overpromoted","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L10_C26_216050_INCROSS_2021_adtech_reseller_no_durable_platform_leverage","trigger_id":"TRG_INCROSS_2021_ADTECH_RECOVERY_FALSE_POSITIVE_2021_02_10","symbol":"216050","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":48,"revision_score":48,"relative_strength_score":58,"customer_quality_score":46,"policy_or_regulatory_score":10,"valuation_repricing_score":56,"execution_risk_score":46,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":26,"ad_product_conversion_score":38,"agency_reseller_exposure_score":72},"weighted_score_before":75.8,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":38,"revision_score":42,"relative_strength_score":58,"customer_quality_score":38,"policy_or_regulatory_score":10,"valuation_repricing_score":50,"execution_risk_score":49,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"owned_traffic_score":21,"ad_product_conversion_score":30,"agency_reseller_exposure_score":86},"weighted_score_after":67.6,"stage_label_after":"Stage2 / watch only","changed_components":["owned_traffic_score","ad_product_conversion_score","margin_bridge_score","agency_reseller_exposure_score"],"component_delta_explanation":"C26 shadow profile rewards owned traffic + ad product conversion + margin bridge; discounts ad agency/reseller exposure without durable operating leverage.","MFE_90D_pct":23.3,"MAE_90D_pct":-6.41,"score_return_alignment_label":"current_profile_overpromoted","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R8","loop":"10","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late_for_owned_platform_ad_leverage","current_profile_false_positive_for_agency_reseller_ad_recovery","price_only_local_peak_not_full_4B"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = R8_loop_11_or_C27_CONTENT_IP_GLOBAL_MONETIZATION
recommended_scope = L8_PLATFORM_CONTENT_SW_SECURITY / C27_CONTENT_IP_GLOBAL_MONETIZATION
carry_forward = Distinguish recurring IP monetization from one-off content hit/event premium.
```

## 28. Source Notes

Price source artifacts consulted in this loop:

- Songdaiki/stock-web `atlas/manifest.json`
- Songdaiki/stock-web `atlas/schema.json`
- Songdaiki/stock-web symbol profiles for 035420, 035720, 067160, 089600, 216050
- Songdaiki/stock-web tradable shards:
  - `atlas/ohlcv_tradable_by_symbol_year/035/035420/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/035/035720/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/067/067160/2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/089/089600/2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/216/216050/2021.csv`

Research-artifact-only stock_agent files consulted for duplicate avoidance:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`
