# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R5
loop = 17
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER
selection_mode = auto_coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

이번 루프는 R7/C23 바이오 루프 직후의 반복을 피하고, R5 소비재·유통·브랜드 섹터 안에서 K-beauty 글로벌 유통/재주문 경로를 검증한다. 핵심 질문은 단순한 “K-beauty 수출 호황” 내러티브가 아니라, **글로벌 채널 재주문 + SKU/브랜드 분산 + 마진/운전자본 확인**이 실제 1D OHLC 경로와 얼마나 정렬되는지다.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

본 연구는 위 global axis를 다시 증명하지 않는다. 여기서는 C20에 특화된 잔여 오류를 본다. C20은 “좋은 브랜드”보다 “잘 팔리는 채널이 반복 발주로 닫히는가”가 더 중요하다. 유통 경로는 혈관이고, 브랜드 인지도는 체온이다. 체온만 높아도 열은 날 수 있지만, 혈관이 막히면 EPS로 산소가 가지 않는다.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R5 |
| loop | 17 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION |
| fine_archetype_id | K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER |
| sector | 소비재·유통·브랜드 |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |
| current_stock_discovery_allowed | false |
| stock_agent_code_access_allowed | false |
| price_data_source | Songdaiki/stock-web |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact check:

```text
reports/e2r_calibration/ingest_summary.md checked only for coverage/duplicate avoidance.
No stock_agent src/e2r code opened.
```

The ingest summary shows broad historical calibration coverage across R1~R13, but this loop deliberately avoids repeating the prior R7/C23 FDA approval/commercialization case set and avoids R1/R2 HBM/grid representative sets. A repository search over allowed artifact scope did not surface the exact C20 case cluster `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION + 실리콘투/브이티/클리오/LG생활건강` as an already materialized calibration set.

```text
auto_selected_coverage_gap = R5/C20 K-beauty global distribution reorder vs China/duty-free counterexample gap
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields checked:

| manifest field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema basis:

```text
price_basis = tradable_raw
tradable columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
corporate-action-contaminated 180D windows are blocked by default
```

## 5. Historical Eligibility Gate

| case_id | symbol | company_name | entry_date | 180D available by manifest max_date | profile corporate-action overlap in 180D | calibration_usable |
|---|---:|---|---|---:|---|---:|
| R5L17_C20_SILICON2_2024Q1 | 257720 | 실리콘투 | 2024-05-17 | yes | none after 2022-08-02 | true |
| R5L17_C20_VT_2023Q3 | 018290 | 브이티 | 2023-11-15 | yes | none after 2019-11-08 | true |
| R5L17_C20_CLIO_2023Q2 | 237880 | 클리오 | 2023-08-11 | yes | none | true |
| R5L17_C20_LGHNH_2022_REOPEN | 051900 | LG생활건강 | 2022-11-15 | yes | none | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | global online/channel reorder, multi-country sell-through, and cosmetics export loop map to C20 rather than generic consumer brand |
| CHINA_DUTY_FREE_BRAND_SCALE_FALSE_REOPEN | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | failed global distribution rerating when growth remains concentrated in China/duty-free and margin bridge is not confirmed |
| HIGH_MAE_GLOBAL_SELLTHROUGH_REENTRY | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | same canonical archetype, but early Stage2 suffers a deep shakeout before durable channel confirmation |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | new independent? | diversity note |
|---|---:|---|---|---|---|---:|---|
| R5L17_C20_SILICON2_2024Q1 | 257720 | 실리콘투 | structural_success | positive | 2024 Q1 earnings/global distribution acceleration | true | new symbol; direct distribution/export platform route |
| R5L17_C20_VT_2023Q3 | 018290 | 브이티 | high_mae_success | positive | Reedle Shot/Japan-led sales inflection, later global rerating | true | new symbol; success after severe MAE, good for reentry guard |
| R5L17_C20_CLIO_2023Q2 | 237880 | 클리오 | structural_success | positive | overseas channel + margin/revision improvement | true | new symbol; brand/channel balance, less blowoff than distributor pure-play |
| R5L17_C20_LGHNH_2022_REOPEN | 051900 | LG생활건강 | failed_rerating | counterexample | China/duty-free reopening narrative without durable channel/margin confirmation | true | new symbol; large-brand false reopen counterexample |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 5
representative_trigger_count = 4
```

The loop is positive-heavy but includes a clean large-brand counterexample. Because C20 is a sector where channel and product proof can differ sharply by company, the result should not be promoted to a global rule. It is suitable as a **canonical-archetype shadow rule**.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|---|---|
| R5L17_C20_SILICON2_2024Q1 | 2024-05-16 | 2024 Q1 earnings and visible K-beauty distributor rerating already reflected in public filings/market data | DART/company quarterly filing; stock-web OHLC row | public_event_or_disclosure; customer_or_order_quality; relative_strength; channel_reorder_score | confirmed_revision; margin_bridge; financial_visibility; multiple_public_sources | 2024-06-19 price-only local peak watch |
| R5L17_C20_VT_2023Q3 | 2023-11-14 | Q3 result and Reedle Shot/Japan-led narrative visible, but early drawdown severe before full rerating | DART/company quarterly filing; stock-web OHLC row | public_event_or_disclosure; customer_or_order_quality; early_revision_signal | later confirmed_revision; margin_bridge; financial_visibility | high MAE, not 4C |
| R5L17_C20_CLIO_2023Q2 | 2023-08-10 | Q2 earnings/channel expansion shock visible in price row; later follow-through confirmed | DART/company quarterly filing; stock-web OHLC row | public_event_or_disclosure; channel_reorder_score; relative_strength | confirmed_revision; margin_bridge; financial_visibility | no full 4B in 180D |
| R5L17_C20_LGHNH_2022_REOPEN | 2022-11-14 | China reopening/duty-free scale narrative; no durable margin/channel confirmation | public filings/news narrative; stock-web OHLC row | public_event_or_disclosure; policy_or_regulatory_optionality | not confirmed; financial_visibility weak | thesis_evidence_broken; margin/channel slowdown |

External sector notes used for qualitative context only: AP reported U.S. imports of South Korean cosmetics reached about $1.7bn in 2024, up 54% YoY; Vogue Business cited Korea MFDS data that Korean cosmetics exports reached $10.2bn in 2024, up 20.6% from 2023. These are sector context, not live candidate recommendations.

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path(s) used | profile caveat |
|---:|---|---|---|
| 257720 | atlas/symbol_profiles/257/257720.json | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv; 2025.csv | corporate-action candidates only in 2022, outside test window |
| 018290 | atlas/symbol_profiles/018/018290.json | atlas/ohlcv_tradable_by_symbol_year/018/018290/2023.csv; 2024.csv | last corporate-action candidate 2019-11-08, outside test window |
| 237880 | atlas/symbol_profiles/237/237880.json | atlas/ohlcv_tradable_by_symbol_year/237/237880/2023.csv; 2024.csv | clean profile, no corporate-action candidates |
| 051900 | atlas/symbol_profiles/051/051900.json | atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv; 2023.csv | clean profile, no corporate-action candidates |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence split | current_profile_verdict | aggregate role |
|---|---|---:|---|---|---|---:|---|---|---|
| R5L17_T01_SILICON2_STAGE3 | R5L17_C20_SILICON2_2024Q1 | 257720 | Stage3-Green candidate | 2024-05-16 | 2024-05-17 | 29,550 | earnings + channel reorder + margin visibility | current_profile_correct | representative |
| R5L17_T02_VT_STAGE2 | R5L17_C20_VT_2023Q3 | 018290 | Stage2-Actionable | 2023-11-14 | 2023-11-15 | 20,300 | product sell-through + early revision, high MAE | current_profile_too_early | representative |
| R5L17_T03_CLIO_STAGE2 | R5L17_C20_CLIO_2023Q2 | 237880 | Stage2-Actionable | 2023-08-10 | 2023-08-11 | 21,700 | overseas channel + earnings surprise | current_profile_correct | representative |
| R5L17_T04_LGHNH_REOPEN_FALSE | R5L17_C20_LGHNH_2022_REOPEN | 051900 | Stage2 false reopen | 2022-11-14 | 2022-11-15 | 672,000 | China/duty-free reopen, no durable margin bridge | current_profile_false_positive | representative |
| R5L17_T05_SILICON2_4B_LOCAL | R5L17_C20_SILICON2_2024Q1 | 257720 | 4B overlay | 2024-06-19 | 2024-06-19 | 50,700 | price-only local blowoff, no non-price fatigue evidence | current_profile_4B_kept_watch_only | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger rows:

| trigger_id | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct | below_entry_price_flag_30D | below_entry_price_flag_90D |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|---|---|---:|---:|---|---|
| R5L17_T01_SILICON2_STAGE3 | 29,550 | 83.4 | 83.4 | 83.4 | contaminated_or_unavailable_after_share_count_change_watch | unavailable_by_scope | -6.8 | -6.8 | -21.2 | contaminated_or_unavailable | 2024-06-19 | 54,200 | -57.0 | true | true |
| R5L17_T02_VT_STAGE2 | 20,300 | 7.6 | 7.6 | 97.0 | 97.0 | unavailable_by_scope | -25.4 | -42.6 | -42.6 | -42.6 | 2024-06-19 | 40,000 | -26.3 | true | true |
| R5L17_T03_CLIO_STAGE2 | 21,700 | 23.0 | 54.4 | 66.1 | 107.4 | unavailable_by_scope | -15.2 | -15.2 | -15.2 | -15.2 | 2024-06-13 | 45,000 | -21.1 | true | true |
| R5L17_T04_LGHNH_REOPEN_FALSE | 672,000 | 9.4 | 14.9 | 14.9 | 14.9 | unavailable_by_scope | -11.8 | -17.4 | -39.5 | -39.5 | 2023-01-20 | 772,000 | -47.3 | true | true |

4B overlay trigger:

| trigger_id | entry_price | local_peak_price_after_Stage2 | full_window_peak_price_after_Stage2 | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | four_b_timing_verdict |
|---|---:|---:|---:|---:|---:|---|---|
| R5L17_T05_SILICON2_4B_LOCAL | 50,700 | 54,200 | 54,200 | 0.86 | 0.86 | price_only | high local/full proximity, but price-only; keep as watch-only, not full 4B |

Calculation notes:

```text
SILICON2 entry row: 2024-05-17 close 29,550; local/full 180D high 54,200 on 2024-06-19; 180D low 23,300 on 2024-12-09.
VT entry row: 2023-11-15 close 20,300; early low 11,650 on 2024-01-04; 180D high 40,000 on 2024-06-19.
CLIO entry row: 2023-08-11 close 21,700; 90D high 33,500 on 2023-11-09; 180D high approx 36,050 by 2024-05-02/03 window; later 1Y high 45,000 on 2024-06-13.
LGHNH entry row: 2022-11-15 close 672,000; 90D/180D high 772,000 on 2023-01-20; 180D low 406,500 on 2023-07-26.
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile judgment | MFE/MAE alignment | Stage2 bonus | Yellow 75 | Green 87/revision 55 | price-only guard | 4B non-price requirement | 4C routing | verdict |
|---|---|---|---|---|---|---|---|---|---|
| SILICON2 | likely Stage3-Green after Q1 evidence | aligned: +83.4% MFE but later drawdown | appropriate | appropriate | appropriate if channel/margin confirmed | appropriate | price-only 4B should remain watch-only | no 4C | current_profile_correct |
| VT | likely Stage2/Yellow too early | eventual +97.0% but -42.6% MAE first | too generous early | too loose before drawdown clears | Green should wait for revision/margin | appropriate | no 4B | no 4C | current_profile_too_early |
| CLIO | Stage2 then Yellow | aligned: +54.4% 90D, +66.1% 180D | appropriate | appropriate | Green only after repeat confirmation | appropriate | no 4B | no 4C | current_profile_correct |
| LGHNH | possible false reopen Stage2/Yellow | poor: +14.9% MFE vs -39.5% MAE | too generous for reopen narrative | too loose if China/duty-free only | Green should block | appropriate | no 4B | 4C should watch after channel thesis break | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

C20 needs a sector-specific distinction:

```text
Stage2-Actionable = public evidence of channel/product inflection, but may still suffer severe MAE.
Stage3-Yellow = channel reorder + gross margin / operating leverage appears, but not yet fully diversified.
Stage3-Green = multi-channel reorder + margin bridge + repeat visibility + low red-team concentration risk.
```

| case_id | Stage2 trigger | Green trigger | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| SILICON2 | 2024-05-17 | 2024-05-17 proxy | 0.00 | earnings/channel evidence was already forceful; Green not meaningfully late |
| VT | 2023-11-15 | no confirmed Green until later drawdown cleared | not_applicable | Stage2 was real but too volatile; use reentry/MAE guard |
| CLIO | 2023-08-11 | later confirmation around 2023-11/2024-05 | 0.40 proxy | Green would be somewhat late but safer |
| LGHNH | 2022-11-15 | no valid Green | not_applicable | reopen narrative should not promote without margin/channel proof |

## 15. 4B Local vs Full-window Timing Audit

Silicon2’s 2024-06-19 high is a useful 4B stress test. It had high proximity to the observed local/full 180D peak, but the evidence type is price-only. Under current calibrated profile, it should be a **watch-only local blowoff**, not a full Stage4B exit signal, unless valuation/revision slowdown, channel inventory saturation, or margin/backlog slowdown appears.

```text
existing_axis_tested = full_4b_requires_non_price_evidence
existing_axis_kept = true
```

## 16. 4C Protection Audit

LG생활건강 provides the 4C protection example. The initial 2022-11 reopen narrative produced only +14.9% MFE while the subsequent 180D low reached -39.5% from entry. When channel evidence remains China/duty-free concentrated and margin bridge remains weak, a hard 4C route should not wait for price-only collapse; it should downgrade the thesis earlier into watch/avoid.

```text
four_c_protection_label = thesis_break_watch_only_to_hard_4c_if_margin_channel_deterioration_confirms
hard_4c_routing = strengthened_within_C20
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The cases are all in L5, but the proposed rule is more precise at C20 than at all-consumer level. It should not automatically affect C18/C19 without more cases.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

Proposed C20 shadow rule:

```text
c20_global_distribution_reorder_gate:
  + channel_reorder_score only when evidence shows repeat sell-through or reordered inventory, not merely export macro.
  + distribution_platform_bonus when company monetizes many third-party/own brands through global fulfillment/channel infrastructure.
  + sku_country_diversification_bonus when sales are not dominated by one country, one duty-free channel, or one single viral SKU.
  - china_duty_free_concentration_guard when brand scale/reopening narrative lacks margin bridge and non-China growth proof.
  - high_mae_reentry_guard when Stage2 evidence is promising but MAE_90D <= -30% before revision confirmation.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | none | 4 | 4 | 40.1 | -20.5 | 65.4 | -29.6 | 25% | 0 | 1 | mixed: catches winners, too early on VT, false positive on LGHNH |
| P0b_e2r_2_0_baseline_reference | baseline reference | rollback only | 4 | 4 | 36.0 | -21.0 | 60.0 | -30.0 | 25% | 1 | 2 | worse: less discrimination between channel proof and reopen narrative |
| P1_L5_consumer_shadow_profile | sector shadow | mild channel concentration guard | 4 | 4 | 40.1 | -20.5 | 65.4 | -29.6 | 25% | 0 | 1 | insufficiently specific; L5-wide rule too broad |
| P2_C20_distribution_reorder_profile | canonical archetype shadow | reorder gate; concentration guard; high-MAE reentry guard | 4 | 3 | 48.5 | -21.5 | 82.2 | -26.5 | 0% | 0 | 1 | best alignment: excludes false reopen, keeps high-upside C20 winners |
| P3_C20_counterexample_guard_profile | counterexample guard | block China/duty-free-only reopen; block price-only Green | 4 | 3 | 48.5 | -21.5 | 82.2 | -26.5 | 0% | 0 | 1 | good as defensive overlay; not enough to promote positives alone |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | score-return alignment |
|---|---:|---|---:|---|---|
| SILICON2 | 87 | Stage3-Green | 91 | Stage3-Green | good: strong MFE and confirmed distribution/margin |
| VT | 76 | Stage3-Yellow | 78 | Stage2-Actionable / Yellow watch | improved: recognizes high-upside but blocks premature Green due MAE |
| CLIO | 80 | Stage3-Yellow | 84 | Stage3-Yellow+ | good: steady C20 success, not pure blowoff |
| LGHNH | 76 | Stage3-Yellow false reopen | 62 | Stage2-watch / blocked Green | improved: concentration guard explains poor MFE/MAE alignment |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER | 3 | 1 | 1 | 1 | 4 | 0 | 5 | 4 | 2 | false | true | still needs food/global distribution counterexamples and more post-2024 holdout rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes: [stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [C20 false reopen narrative, C20 high-MAE early Stage2, C20 price-only local 4B watch]
new_axis_proposed: [c20_global_distribution_reorder_gate, c20_china_duty_free_concentration_guard, c20_high_mae_reentry_guard]
existing_axis_strengthened: [stage3_green_revision_min within C20, full_4b_requires_non_price_evidence within C20, hard_4c_thesis_break_routes_to_4c within C20]
existing_axis_weakened: []
existing_axis_kept: [price_only_blowoff_blocks_positive_stage]
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R5/C20 K-beauty global distribution reorder vs China/duty-free counterexample gap
diversity_score_summary: high; same canonical archetype, four new symbols, four new trigger families, positive/counterexample balance present
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web tradable_raw OHLC rows for entry/peak/drawdown
- 180D forward windows by manifest max_date
- corporate-action profile caveats for selected windows
- representative trigger dedupe
- current profile residual stress test
```

Not validated:

```text
- live candidate status in 2026
- investment recommendation
- broker/API execution
- stock_agent production code behavior
- exact DART filing timestamps beyond next-trading-day conservative entry assumption
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_global_distribution_reorder_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"repeat channel/order proof distinguishes SILICON2/CLIO from LGHNH false reopen","P2 improves false_positive_rate from 25% to 0% while retaining high MFE positives","R5L17_T01_SILICON2_STAGE3|R5L17_T03_CLIO_STAGE2|R5L17_T04_LGHNH_REOPEN_FALSE",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_china_duty_free_concentration_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"large-brand reopen narrative with China/duty-free concentration produced poor MFE/MAE","blocks LGHNH-style false Yellow/Green","R5L17_T04_LGHNH_REOPEN_FALSE",4,4,1,medium,canonical_shadow_only,"not production; needs more C20 counterexamples"
shadow_weight,c20_high_mae_reentry_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"VT shows true eventual rerating but -42.6% MAE before full confirmation","keeps Stage2 but delays Green until drawdown/revision clears","R5L17_T02_VT_STAGE2",4,4,1,low,canonical_shadow_only,"not production; high-upside but high-MAE archetype"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L17_C20_SILICON2_2024Q1","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L17_T01_SILICON2_STAGE3","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_MFE_but_later_drawdown_requires_4B_watch","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"global distribution platform plus margin/revision proof"}
{"row_type":"case","case_id":"R5L17_C20_VT_2023Q3","symbol":"018290","company_name":"브이티","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"HIGH_MAE_GLOBAL_SELLTHROUGH_REENTRY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L17_T02_VT_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"eventual_MFE_positive_but_stage2_too_early_due_large_MAE","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"needs high-MAE reentry guard before Green"}
{"row_type":"case","case_id":"R5L17_C20_CLIO_2023Q2","symbol":"237880","company_name":"클리오","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L17_T03_CLIO_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_MFE_with_moderate_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"brand plus overseas channel proof; not pure price-only blowoff"}
{"row_type":"case","case_id":"R5L17_C20_LGHNH_2022_REOPEN","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"CHINA_DUTY_FREE_BRAND_SCALE_FALSE_REOPEN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L17_T04_LGHNH_REOPEN_FALSE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_MFE_large_MAE_false_reopen","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"large brand/reopen narrative without repeat global channel proof"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R5L17_T01_SILICON2_STAGE3","case_id":"R5L17_C20_SILICON2_2024Q1","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"global_distribution_reorder","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining","trigger_type":"Stage3-Green candidate","trigger_date":"2024-05-16","evidence_available_at_that_date":"2024 Q1 earnings/global distribution evidence; conservative next-trading-day close","evidence_source":"DART/company quarterly filing; stock-web OHLC","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":29550,"MFE_30D_pct":83.4,"MFE_90D_pct":83.4,"MFE_180D_pct":83.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.8,"MAE_90D_pct":-6.8,"MAE_180D_pct":-21.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.0,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_with_later_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L17_G01_SILICON2_20240517","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L17_T02_VT_STAGE2","case_id":"R5L17_C20_VT_2023Q3","symbol":"018290","company_name":"브이티","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"HIGH_MAE_GLOBAL_SELLTHROUGH_REENTRY","sector":"소비재·유통·브랜드","primary_archetype":"viral_product_global_sellthrough","loop_objective":"coverage_gap_fill|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-14","evidence_available_at_that_date":"Q3/product sell-through evidence; conservative next-trading-day close","evidence_source":"DART/company quarterly filing; stock-web OHLC","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018290/2023.csv","profile_path":"atlas/symbol_profiles/018/018290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-15","entry_price":20300,"MFE_30D_pct":7.6,"MFE_90D_pct":7.6,"MFE_180D_pct":97.0,"MFE_1Y_pct":97.0,"MFE_2Y_pct":null,"MAE_30D_pct":-25.4,"MAE_90D_pct":-42.6,"MAE_180D_pct":-42.6,"MAE_1Y_pct":-42.6,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":40000,"drawdown_after_peak_pct":-26.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L17_G02_VT_20231115","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L17_T03_CLIO_STAGE2","case_id":"R5L17_C20_CLIO_2023Q2","symbol":"237880","company_name":"클리오","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"brand_overseas_channel_reorder","loop_objective":"coverage_gap_fill|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","evidence_available_at_that_date":"Q2 earnings/channel shock; conservative next-trading-day close","evidence_source":"DART/company quarterly filing; stock-web OHLC","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237880/2023.csv","profile_path":"atlas/symbol_profiles/237/237880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-11","entry_price":21700,"MFE_30D_pct":23.0,"MFE_90D_pct":54.4,"MFE_180D_pct":66.1,"MFE_1Y_pct":107.4,"MFE_2Y_pct":null,"MAE_30D_pct":-15.2,"MAE_90D_pct":-15.2,"MAE_180D_pct":-15.2,"MAE_1Y_pct":-15.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":45000,"drawdown_after_peak_pct":-21.1,"green_lateness_ratio":0.40,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L17_G03_CLIO_20230811","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L17_T04_LGHNH_REOPEN_FALSE","case_id":"R5L17_C20_LGHNH_2022_REOPEN","symbol":"051900","company_name":"LG생활건강","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"CHINA_DUTY_FREE_BRAND_SCALE_FALSE_REOPEN","sector":"소비재·유통·브랜드","primary_archetype":"china_reopen_brand_scale_false_positive","loop_objective":"counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage2 false reopen","trigger_date":"2022-11-14","evidence_available_at_that_date":"China/duty-free reopen narrative without durable channel/margin confirmation; conservative next-trading-day close","evidence_source":"public narrative; stock-web OHLC","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv","profile_path":"atlas/symbol_profiles/051/051900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-11-15","entry_price":672000,"MFE_30D_pct":9.4,"MFE_90D_pct":14.9,"MFE_180D_pct":14.9,"MFE_1Y_pct":14.9,"MFE_2Y_pct":null,"MAE_30D_pct":-11.8,"MAE_90D_pct":-17.4,"MAE_180D_pct":-39.5,"MAE_1Y_pct":-39.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-01-20","peak_price":772000,"drawdown_after_peak_pct":-47.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_false_reopen_to_4C_watch","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L17_G04_LGHNH_20221115","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L17_T05_SILICON2_4B_LOCAL","case_id":"R5L17_C20_SILICON2_2024Q1","symbol":"257720","company_name":"실리콘투","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_GLOBAL_DISTRIBUTION_REORDER","sector":"소비재·유통·브랜드","primary_archetype":"price_only_local_peak_watch","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B overlay","trigger_date":"2024-06-19","evidence_available_at_that_date":"price-only local peak; no non-price 4B evidence confirmed at trigger","evidence_source":"stock-web OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv","profile_path":"atlas/symbol_profiles/257/257720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-19","entry_price":50700,"MFE_30D_pct":6.9,"MFE_90D_pct":6.9,"MFE_180D_pct":6.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.5,"MAE_90D_pct":-28.1,"MAE_180D_pct":-54.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":54200,"drawdown_after_peak_pct":-57.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"price_only_local_peak_watch_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success_watch_only","current_profile_verdict":"current_profile_4B_correctly_not_full_without_non_price_evidence","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L17_G01_SILICON2_20240517","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_new_4B_timing_family","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L17_C20_SILICON2_2024Q1","trigger_id":"R5L17_T01_SILICON2_STAGE3","symbol":"257720","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":18,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":87,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":21,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","margin_bridge_score","revision_score"],"component_delta_explanation":"C20 distribution-platform proof deserves channel reorder credit once margin/revision is confirmed.","MFE_90D_pct":83.4,"MAE_90D_pct":-6.8,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L17_C20_VT_2023Q3","trigger_id":"R5L17_T02_VT_STAGE2","symbol":"018290","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":13,"relative_strength_score":11,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":13,"relative_strength_score":10,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable / Yellow watch","changed_components":["execution_risk_score","relative_strength_score"],"component_delta_explanation":"High-MAE guard keeps the case alive as Stage2 but blocks early Green until drawdown/revision clears.","MFE_90D_pct":7.6,"MAE_90D_pct":-42.6,"score_return_alignment_label":"eventual_positive_but_stage_too_early","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L17_C20_CLIO_2023Q2","trigger_id":"R5L17_T03_CLIO_STAGE2","symbol":"237880","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":16,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":17,"relative_strength_score":14,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow+","changed_components":["customer_quality_score","margin_bridge_score","revision_score"],"component_delta_explanation":"Brand plus overseas reorder proof improves Yellow confidence but not enough for immediate Green.","MFE_90D_pct":54.4,"MAE_90D_pct":-15.2,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L17_C20_LGHNH_2022_REOPEN","trigger_id":"R5L17_T04_LGHNH_REOPEN_FALSE","symbol":"051900","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":7,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":12,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow false reopen","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":3,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":-18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-watch / blocked Green","changed_components":["customer_quality_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"China/duty-free concentration guard blocks brand-scale reopen narrative without margin/channel proof.","MFE_90D_pct":14.9,"MAE_90D_pct":-17.4,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_global_distribution_reorder_gate,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"repeat channel/order proof distinguishes winners from false reopen","reduces false positive while retaining positive MFE","R5L17_T01_SILICON2_STAGE3|R5L17_T03_CLIO_STAGE2",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c20_china_duty_free_concentration_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"China/duty-free reopen narrative without margin bridge created bad MAE","blocks LGHNH-style false Yellow/Green","R5L17_T04_LGHNH_REOPEN_FALSE",4,4,1,medium,canonical_shadow_only,"not production; needs more C20 counterexamples"
shadow_weight,c20_high_mae_reentry_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"high-MAE but eventual winner needs delayed Green not rejection","improves stage timing on VT","R5L17_T02_VT_STAGE2",4,4,1,low,canonical_shadow_only,"not production; high-upside but high-volatility case"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"17","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":0,"new_trigger_family_count":4,"positive_case_count":3,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C20 false reopen narrative","C20 high-MAE early Stage2","C20 price-only local 4B watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R5/C20 K-beauty global distribution reorder vs China/duty-free counterexample gap","diversity_score_summary":"high"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R5L17_SECTOR_CONTEXT_KBEAUTY_EXPORTS","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reason":"sector context only; not an individual calibration trigger","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round_candidates:
- R8 / L8_PLATFORM_CONTENT_SW_SECURITY / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
- R4 / L4_MATERIALS_SPREAD_RESOURCE / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
- R10 / L9_CONSTRUCTION_REALESTATE_HOUSING / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

## 28. Source Notes

Stock-web source files used:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/257/257720.json
atlas/symbol_profiles/018/018290.json
atlas/symbol_profiles/237/237880.json
atlas/symbol_profiles/051/051900.json
atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv
atlas/ohlcv_tradable_by_symbol_year/257/257720/2025.csv
atlas/ohlcv_tradable_by_symbol_year/018/018290/2023.csv
atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv
atlas/ohlcv_tradable_by_symbol_year/237/237880/2023.csv
atlas/ohlcv_tradable_by_symbol_year/237/237880/2024.csv
atlas/ohlcv_tradable_by_symbol_year/051/051900/2022.csv
atlas/ohlcv_tradable_by_symbol_year/051/051900/2023.csv
```

External context used only for sector narrative:

```text
AP News: K-beauty U.S. import growth context, 2024.
Vogue Business: K-beauty second coming and export growth context, 2024.
```

No stock_agent source code opened. No production scoring changed. No live recommendation made.
