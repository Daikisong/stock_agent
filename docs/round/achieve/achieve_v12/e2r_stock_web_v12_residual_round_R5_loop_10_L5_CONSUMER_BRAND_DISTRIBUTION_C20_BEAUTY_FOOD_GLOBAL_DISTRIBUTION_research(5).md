# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R5
scheduled_loop: 10
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_K_FOOD_GLOBAL_CHANNEL_REORDER_CAPACITY
output_file: e2r_stock_web_v12_residual_round_R5_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION.

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

This MD does not re-argue the global Stage2 bonus or global Green strictness. The residual question is narrower: inside C20, what distinguishes a real global channel/reorder rerating from a one-off reopening or channel narrative?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R5 |
| scheduled_loop | 10 |
| allowed large sector | L5_CONSUMER_BRAND_DISTRIBUTION |
| selected canonical | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION |
| fine archetype | K_BEAUTY_K_FOOD_GLOBAL_CHANNEL_REORDER_CAPACITY |
| loop objectives | coverage_gap_fill; sector_specific_rule_discovery; canonical_archetype_compression; stage2_actionable_bonus_stress_test; green_strictness_stress_test; 4B_non_price_requirement_stress_test; counterexample_mining |

R5 hard gate passes because this is a consumer/brand/distribution round and the selected large sector is L5_CONSUMER_BRAND_DISTRIBUTION.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts indicate prior coverage across R1~R13 and loop 1~9. For R5 loop 10, this run intentionally avoids repeating a generic consumer export template. The selected cases are treated as new independent C20 evidence because the loop focuses on product/channel/reorder quality rather than only broad consumer brand momentum.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 3
reused_case_count = 0
```

Prior global axes already applied and not re-proposed as global deltas:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Price source row:

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case_id | symbol | company | entry_date | 180D forward window | corporate-action window | calibration_usable |
|---|---:|---|---|---:|---|---|
| R5L10_C20_SAMYANG_2024_EXPORT_REORDER | 003230 | 삼양식품 | 2024-05-17 | available | clean_180D_window | true |
| R5L10_C20_COSMAX_2024_ODM_GLOBAL_CHANNEL | 192820 | 코스맥스 | 2024-05-13 | available | clean_180D_window | true |
| R5L10_C20_AMORE_2023_CHINA_REOPENING_FALSE_POSITIVE | 090430 | 아모레퍼시픽 | 2023-01-26 | available | clean_180D_window | true |

Symbol profile checks:

```text
003230 Samyang Foods: first_date=1995-05-02; last_date=2026-02-20; corporate_action_candidate_dates=[2003-07-25]; no overlap with 2024-05-17~D+180.
192820 Cosmax: first_date=2014-04-07; last_date=2026-02-20; corporate_action_candidate_dates=[]; clean.
090430 Amorepacific: first_date=2006-06-29; last_date=2026-02-20; corporate_action_candidate_dates=[2015-05-08]; no overlap with 2023-01-26~D+180.
```

## 6. Canonical Archetype Compression Map

| fine pattern | canonical mapping | interpretation |
|---|---|---|
| K-food viral export, U.S./Europe shipment, production capacity, repeated overseas sales | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Real C20 rerating when sell-through/reorder and capacity bridge are both visible. |
| K-beauty ODM global customer/channel growth, U.S./Japan/indie-brand order flow | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Valid but more volatile; needs customer/channel concentration and China exposure guard. |
| China reopening / duty-free normalization narrative without sell-through proof | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | C20 false positive if channel inventory and China weakness remain unresolved. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_family | why selected |
|---|---:|---|---|---|---|
| R5L10_C20_SAMYANG_2024_EXPORT_REORDER | 003230 | 삼양식품 | structural_success | export_reorder_capacity_bridge | K-food export demand plus capacity bridge translated into a large forward MFE with low MAE. |
| R5L10_C20_COSMAX_2024_ODM_GLOBAL_CHANNEL | 192820 | 코스맥스 | high_mae_success | global_odm_channel_growth | K-beauty ODM channel proof produced upside, but with high drawdown; this tests whether C20 needs volatility/China-exposure guard. |
| R5L10_C20_AMORE_2023_CHINA_REOPENING_FALSE_POSITIVE | 090430 | 아모레퍼시픽 | failed_rerating | china_reopening_without_sellthrough | Reopening narrative gave small MFE but large MAE; a C20 negative template for channel recovery without sell-through. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
new_independent_case_count = 3
```

The balance is sufficient for a canonical-archetype-specific shadow candidate, not for a global delta.

## 9. Evidence Source Map

| case_id | evidence available at trigger date | evidence source handling | evidence family |
|---|---|---|---|
| R5L10_C20_SAMYANG_2024_EXPORT_REORDER | 2024-05-16~2024-05-17 Q1 earnings shock / export-led operating profit beat; later 2024-06-14 analyst confirmation of U.S./Europe Buldak shipments and capacity support | MarketWatch / WSJ market talk for 2024-06-14; original earnings URL enrichment pending | export_growth; repeat_order_or_conversion; capacity_or_volume_route; margin_bridge |
| R5L10_C20_COSMAX_2024_ODM_GLOBAL_CHANNEL | 2024-05-13 Q1 earnings/channel growth recognized by market; later Q2/2H volatility showed China/customer mix sensitivity | exact_url_pending; price row validated | global_odm_channel; customer_quality; margin_bridge; china_exposure_risk |
| R5L10_C20_AMORE_2023_CHINA_REOPENING_FALSE_POSITIVE | 2023-01 reopening/travel retail recovery narrative; later 2023 reporting showed overseas business weakness, especially China, despite North America/EMEA growth | Vogue Business 2023 analysis; original company filing URL enrichment pending | china_reopening_without_sellthrough; duty_free_inventory_risk; channel_quality_gap |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry row source |
|---:|---|---|---|
| 003230 | atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv; atlas/ohlcv_tradable_by_symbol_year/003/003230/2025.csv | atlas/symbol_profiles/003/003230.json | 2024-05-17 close 446,500 |
| 192820 | atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv | atlas/symbol_profiles/192/192820.json | 2024-05-13 close 157,700 |
| 090430 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv | atlas/symbol_profiles/090/090430.json | 2023-01-26 close 143,400 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|---:|---|---|---|
| R5L10_T01_SAMYANG_STAGE2_ACTIONABLE | R5L10_C20_SAMYANG_2024_EXPORT_REORDER | Stage2-Actionable | 2024-05-16 | 2024-05-17 | 446500 | Q1 earnings shock; export channel; capacity route | margin bridge appears quickly; multiple public confirmations | none at entry |
| R5L10_T02_SAMYANG_4B_LOCAL | R5L10_C20_SAMYANG_2024_EXPORT_REORDER | 4B_overlay | 2024-06-18 | 2024-06-18 | 712000 | not positive entry | strong but extended | price-only local peak; no full 4B non-price evidence |
| R5L10_T03_COSMAX_STAGE2_ACTIONABLE | R5L10_C20_COSMAX_2024_ODM_GLOBAL_CHANNEL | Stage2-Actionable | 2024-05-13 | 2024-05-13 | 157700 | Q1 earnings/channel growth | margin bridge partial; customer channel quality | high MAE risk |
| R5L10_T04_AMORE_STAGE2_FALSE_POSITIVE | R5L10_C20_AMORE_2023_CHINA_REOPENING_FALSE_POSITIVE | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 143400 | China reopening narrative; duty-free hope | insufficient sell-through and China proof | thesis-break watch after overseas weakness |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger table

| trigger_id | symbol | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R5L10_T01_SAMYANG_STAGE2_ACTIONABLE | 003230 | 446500 | 60.8% | 0.0% | 60.8% | 0.0% | 85.4% | 0.0% | 2025-02-06 | 828000 | structural_success |
| R5L10_T03_COSMAX_STAGE2_ACTIONABLE | 192820 | 157700 | 31.9% | -6.3% | 31.9% | -26.4% | 31.9% | -26.4% | 2024-06-14 | 208000 | high_mae_success |
| R5L10_T04_AMORE_STAGE2_FALSE_POSITIVE | 090430 | 143400 | 8.6% | -12.8% | 8.6% | -27.4% | 8.6% | -34.1% | 2023-02-10 | 155800 | failed_rerating |

### 12.2 Key stock-web row excerpts used

```text
003230 2024-05-17: o=446500 h=446500 l=446500 c=446500
003230 2024-06-19: h=718000, c=673000
003230 2025-02-06: h=828000, c=809000
192820 2024-05-13: h=164700 l=147800 c=157700
192820 2024-06-14: h=208000 c=184900
192820 2024-08-13: l=116000 c=117700
090430 2023-01-26: h=146200 l=142600 c=143400
090430 2023-02-10: h=155800 c=153000
090430 2023-07-07: l=93900 c=94700
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual alignment | current_profile_verdict | explanation |
|---|---|---|---|---|
| Samyang | Stage3-Yellow / Stage3-Green after earnings confirmation | correct; high MFE and low MAE | current_profile_correct | Export channel + margin bridge + capacity route is exactly the C20 quality pattern. |
| Cosmax | Stage3-Yellow, maybe early Green if Q1 revision over-weighted | partially too early because 90D MAE exceeded -26% | current_profile_too_early | ODM channel evidence works, but C20 needs customer/channel concentration and China exposure guard before Green. |
| Amorepacific | Stage2/Yellow candidate on reopening narrative | false positive | current_profile_false_positive | Reopening narrative lacked sell-through/reorder proof; MFE small, MAE large. |

Global applied axes tested:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green entry proxy | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| Samyang | 446500 | 587000 | 828000 | 0.37 | Green somewhat late but acceptable because Stage2 captured evidence early. |
| Cosmax | 157700 | 184900 | 208000 | 0.54 | Green late and vulnerable; Yellow useful, Green should require customer/channel concentration evidence. |
| Amorepacific | 143400 | n/a | 155800 | not_applicable | No confirmed Green; Stage2 should be capped unless sell-through appears. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | entry | 4B price | local peak | full-window peak | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| R5L10_T02_SAMYANG_4B_LOCAL | 446500 | 712000 | 718000 | 828000 | 0.98 | 0.70 | price_only | price_only_local_4B_too_early |

The Samyang case is useful because price-only local 4B would have fired near June 2024, but the full window later made a materially higher high. This strengthens the already-applied rule that full 4B requires non-price evidence such as revision slowdown, margin rollover, distribution channel saturation, or valuation blowoff with evidence.

## 16. 4C Protection Audit

| case_id | 4C/protection trigger | label | protection read |
|---|---|---|---|
| Samyang | none within selected entry window | false_break | No thesis break; local price peak alone would have been false 4B, not 4C. |
| Cosmax | 2024-08-13 high-MAE shock after Q1 enthusiasm | thesis_break_watch_only | Not hard 4C; high-MAE watch because channel proof remained alive but volatility was severe. |
| Amorepacific | 2023 Q1/Q2 overseas China weakness after reopening thesis | hard_4c_late | Reopening thesis should have been downgraded earlier when China/duty-free recovery evidence failed. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
axis = l5_export_channel_reorder_quality_bridge
shadow_delta = +1 only when export/channel growth is backed by repeat order or sell-through plus capacity/margin conversion.
```

Candidate rule:

> In L5 consumer/brand/distribution, Stage2/Yellow can be pulled forward only when channel growth is supported by at least two of: repeat order/sell-through, sustained export shipment growth, margin bridge, capacity or supply route, and multiple non-price public sources. Reopening-only or platform/travel-retail normalization narratives should remain capped below Green.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
new_axis_proposed:
  - c20_export_reorder_capacity_bridge_bonus
  - c20_china_reopening_without_sellthrough_cap
  - c20_high_mae_channel_concentration_guard
```

Candidate rule:

> C20 should distinguish viral/global channel flywheel from channel normalization. For K-food/K-beauty, `customer_quality_score` and `channel_reorder_score` should count only when the evidence points to repeat sell-through, export reorder, or ODM customer order continuity. If the trigger is only China reopening, duty-free normalization, or brand marketing, cap Stage2/Yellow and block Green until sell-through/revision proof arrives.

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE_90D | avg MAE_90D | false_positive_rate | missed_structural_count | score-return alignment |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 33.8% | -17.9% | 33% | 0 | mixed; accepts Amore reopening too easily |
| P0b e2r_2_0_baseline_reference | 3 | 33.8% | -17.9% | 33% | 1 | misses early Samyang quality unless outcome-aware revision appears |
| P1 sector_specific_candidate_profile | 3 | 46.4% | -8.8% | 0% | 0 | better; blocks reopening-only case |
| P2 canonical_archetype_candidate_profile | 3 | 46.4% | -8.8% | 0% | 0 | best alignment for C20 |
| P3 counterexample_guard_profile | 3 | 46.4% | -8.8% | 0% | 0 | best false-positive protection but risks delaying high-MAE ODM cases |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| Samyang | 86 | Stage3-Yellow | 90 | Stage3-Green | 60.8% | 0.0% | improved_positive_alignment |
| Cosmax | 81 | Stage3-Yellow | 78 | Stage3-Yellow with high-MAE guard | 31.9% | -26.4% | risk_adjusted_alignment |
| Amorepacific | 76 | Stage3-Yellow | 63 | Stage1/Stage2-watch | 8.6% | -27.4% | false_positive_removed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_K_FOOD_GLOBAL_CHANNEL_REORDER_CAPACITY | 2 | 1 | 1 | 1 | 3 | 0 | 4 | 3 | 2 | true | true | Need more C18/C19 non-C20 retail inventory cases in future R5 loops. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_early
  - current_profile_false_positive
new_axis_proposed:
  - c20_export_reorder_capacity_bridge_bonus
  - c20_china_reopening_without_sellthrough_cap
  - c20_high_mae_channel_concentration_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Actual stock-web OHLC rows were used for entry price, MFE, MAE, peak, and drawdown estimates.
- Each selected representative trigger has at least 180 trading days available in stock-web.
- Corporate-action windows do not overlap the representative 180D windows.
- The research proposes shadow-only sector/canonical rules.
```

Non-validation scope:

```text
- This MD does not change production scoring.
- This MD does not create a live watchlist or current investment recommendation.
- Some evidence URLs require later exact source enrichment before production promotion.
- Research proxy scores are not production scores.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_export_reorder_capacity_bridge_bonus,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Samyang shows export reorder + capacity/margin bridge created high MFE with low MAE","improves positive alignment",R5L10_T01_SAMYANG_STAGE2_ACTIONABLE,3,3,1,medium,canonical_shadow_only,"not production; requires evidence URL enrichment"
shadow_weight,c20_china_reopening_without_sellthrough_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Amore reopening narrative had small MFE and large MAE without China sell-through proof","removes false positive",R5L10_T04_AMORE_STAGE2_FALSE_POSITIVE,3,3,1,medium,canonical_shadow_only,"cap reopening-only C20 triggers below Green"
shadow_weight,c20_high_mae_channel_concentration_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Cosmax shows ODM channel evidence can work but with severe drawdown","keeps Yellow but delays Green",R5L10_T03_COSMAX_STAGE2_ACTIONABLE,3,3,1,low,canonical_shadow_only,"requires more K-beauty ODM samples"
```

## 25. Machine-Readable Rows

### 25.1 Case rows

```jsonl
{"row_type":"case","case_id":"R5L10_C20_SAMYANG_2024_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"10","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BULDAK_US_EUROPE_EXPORT_REORDER_CAPACITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R5L10_T01_SAMYANG_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"export_reorder_capacity_bridge_aligned_with_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C20 positive: export demand plus capacity/margin bridge."}
{"row_type":"case","case_id":"R5L10_C20_COSMAX_2024_ODM_GLOBAL_CHANNEL","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"10","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_CUSTOMER_CHANNEL_GROWTH","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R5L10_T03_COSMAX_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"MFE_positive_but_high_MAE_requires_channel_concentration_guard","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"C20 high-MAE positive: ODM/global channel evidence valid but volatile."}
{"row_type":"case","case_id":"R5L10_C20_AMORE_2023_CHINA_REOPENING_FALSE_POSITIVE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"10","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_CHINA_REOPENING_WITHOUT_SELLTHROUGH","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R5L10_T04_AMORE_STAGE2_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"small_MFE_large_MAE_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C20 counterexample: reopening/duty-free hope without sell-through proof."}
```

### 25.2 Trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R5L10_T01_SAMYANG_STAGE2_ACTIONABLE","case_id":"R5L10_C20_SAMYANG_2024_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"10","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BULDAK_US_EUROPE_EXPORT_REORDER_CAPACITY","sector":"소비재·유통·브랜드","primary_archetype":"Beauty/Food global distribution","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","evidence_available_at_that_date":"Q1 earnings shock; overseas Buldak export and margin bridge recognized; later public confirmation from analyst channel described U.S./Europe shipments and capacity support.","evidence_source":"MarketWatch/WSJ market talk plus exact earnings source pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":446500,"MFE_30D_pct":60.8,"MFE_90D_pct":60.8,"MFE_180D_pct":85.4,"MFE_1Y_pct":114.6,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"MAE_1Y_pct":0.0,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-02-06","peak_price":828000,"drawdown_after_peak_pct":-9.0,"green_lateness_ratio":0.37,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L10_003230_20240517_446500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L10_T02_SAMYANG_4B_LOCAL","case_id":"R5L10_C20_SAMYANG_2024_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"10","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_BULDAK_US_EUROPE_EXPORT_REORDER_CAPACITY","sector":"소비재·유통·브랜드","primary_archetype":"Beauty/Food global distribution","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B_overlay","trigger_date":"2024-06-18","evidence_available_at_that_date":"Price-only local high after explosive rerating; no non-price revision slowdown, channel saturation, or margin rollover evidence yet.","evidence_source":"stock-web price row; non-price 4B evidence absent","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-18","entry_price":712000,"MFE_30D_pct":0.8,"MFE_90D_pct":0.8,"MFE_180D_pct":29.2,"MFE_1Y_pct":34.6,"MFE_2Y_pct":null,"MAE_30D_pct":-18.4,"MAE_90D_pct":-36.0,"MAE_180D_pct":-36.0,"MAE_1Y_pct":-36.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000,"drawdown_after_peak_pct":-36.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.70,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"false_break","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L10_003230_20240618_712000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, separate 4B timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R5L10_T03_COSMAX_STAGE2_ACTIONABLE","case_id":"R5L10_C20_COSMAX_2024_ODM_GLOBAL_CHANNEL","symbol":"192820","company_name":"코스맥스","round":"R5","loop":"10","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_CUSTOMER_CHANNEL_GROWTH","sector":"소비재·유통·브랜드","primary_archetype":"Beauty/Food global distribution","loop_objective":"stage2_actionable_bonus_stress_test|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-13","evidence_available_at_that_date":"Q1 earnings/channel growth recognized; ODM global customer/channel thesis becomes visible but later high-MAE proves the need for concentration and China exposure guard.","evidence_source":"exact_url_pending; stock-web price row validated","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv","profile_path":"atlas/symbol_profiles/192/192820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-13","entry_price":157700,"MFE_30D_pct":31.9,"MFE_90D_pct":31.9,"MFE_180D_pct":31.9,"MFE_1Y_pct":31.9,"MFE_2Y_pct":null,"MAE_30D_pct":-6.3,"MAE_90D_pct":-26.4,"MAE_180D_pct":-26.4,"MAE_1Y_pct":-26.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":208000,"drawdown_after_peak_pct":-44.2,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_only_high_mae","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L10_192820_20240513_157700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R5L10_T04_AMORE_STAGE2_FALSE_POSITIVE","case_id":"R5L10_C20_AMORE_2023_CHINA_REOPENING_FALSE_POSITIVE","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"10","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_CHINA_REOPENING_WITHOUT_SELLTHROUGH","sector":"소비재·유통·브랜드","primary_archetype":"Beauty/Food global distribution","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","evidence_available_at_that_date":"China reopening and travel retail recovery narrative; not backed by sell-through or China channel recovery proof at trigger date.","evidence_source":"Vogue Business 2023 analysis plus exact company source pending","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2023.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-26","entry_price":143400,"MFE_30D_pct":8.6,"MFE_90D_pct":8.6,"MFE_180D_pct":8.6,"MFE_1Y_pct":8.6,"MFE_2Y_pct":8.6,"MAE_30D_pct":-12.8,"MAE_90D_pct":-27.4,"MAE_180D_pct":-34.1,"MAE_1Y_pct":-34.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-10","peak_price":155800,"drawdown_after_peak_pct":-39.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L10_090430_20230126_143400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.3 Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L10_C20_SAMYANG_2024_EXPORT_REORDER","trigger_id":"R5L10_T01_SAMYANG_STAGE2_ACTIONABLE","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":17,"capacity_or_shipment_score":14},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":15,"customer_quality_score":17,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":20,"capacity_or_shipment_score":17},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","customer_quality_score","channel_reorder_score","capacity_or_shipment_score"],"component_delta_explanation":"C20 export-reorder-capacity bridge adds scoped bonus when export demand and capacity/margin route are both visible.","MFE_90D_pct":60.8,"MAE_90D_pct":0.0,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L10_C20_COSMAX_2024_ODM_GLOBAL_CHANNEL","trigger_id":"R5L10_T03_COSMAX_STAGE2_ACTIONABLE","symbol":"192820","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":16,"relative_strength_score":13,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":13,"capacity_or_shipment_score":6},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":15,"relative_strength_score":11,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":12,"capacity_or_shipment_score":6},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_high_MAE_guard","changed_components":["customer_quality_score","relative_strength_score","execution_risk_score","channel_reorder_score"],"component_delta_explanation":"C20 high-MAE channel concentration guard keeps Yellow but blocks Green until customer/channel concentration and China exposure are resolved.","MFE_90D_pct":31.9,"MAE_90D_pct":-26.4,"score_return_alignment_label":"risk_adjusted_positive","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L10_C20_AMORE_2023_CHINA_REOPENING_FALSE_POSITIVE","trigger_id":"R5L10_T04_AMORE_STAGE2_FALSE_POSITIVE","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":6,"relative_strength_score":11,"customer_quality_score":8,"policy_or_regulatory_score":15,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":5,"capacity_or_shipment_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":0,"capacity_or_shipment_score":0},"weighted_score_after":63,"stage_label_after":"Stage1_Stage2_watch","changed_components":["customer_quality_score","policy_or_regulatory_score","channel_reorder_score","execution_risk_score"],"component_delta_explanation":"C20 reopening-without-sell-through cap removes positive promotion when the trigger is only reopening/duty-free normalization.","MFE_90D_pct":8.6,"MAE_90D_pct":-27.4,"score_return_alignment_label":"false_positive_removed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.4 Residual contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"10","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"diversity_score_summary":"estimated +35: three new symbols, three trigger families, one counterexample, two residual errors, no wrong-round penalty","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_early","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R5
completed_loop = 10
next_round = R6
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
all production scoring changes = false
handoff prompt executed now = false
```

