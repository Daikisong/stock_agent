# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R3
loop = 70
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = multiple
loop_objective = coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4C_thesis_break_timing_test | 4B_non_price_requirement_stress_test
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
```

This file is historical calibration research only. It is not an investment recommendation, not a current/live candidate scan, and not a repository patch.


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

The research question is not whether the global Stage2 bonus or price-only 4B guard exists. The question is whether C13 needs a more specific rule: named customer/JV/AMPC headlines only promote durable stages when they close into utilization, margin, or minimum-volume evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_ids =
  - CELL_MAKER_IRA_AMPC_EARLY_OPTIONALITY
  - STELLANTIS_US_JV_FIRST_PLANT_DELAYED_RERATING
  - STELLANTIS_US_JV_SECOND_PLANT_FAR_OUT_CAPACITY_GUARD
  - BLUEOVAL_SK_DOE_LOAN_HIGH_MFE_HIGH_MAE_COUNTEREXAMPLE
```

C13 is treated as a bridge archetype. The headline is usually policy/JV/AMPC, but the price path depends on whether the bridge reaches a real plant utilization ramp, AMPC-to-margin conversion, or minimum-volume/take-or-pay quality.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact use was limited to the calibration registry and search-level duplicate avoidance.

```text
stock_agent_code_accessed = false
stock_agent_src_e2r_accessed = false
github_search_exact_C13_BATTERY_JV_UTILIZATION_AMPC_IRA = 0 exact file hits
md_registry_reviewed_for_duplicate_context = true
manual_previous_round_context = prior loop R3/C12 already produced, so this loop advances to C13
```

This loop does not repeat the immediately previous C12 customer call-off/cathode contract row. It moves to C13 and uses a distinct evidence family: IRA/AMPC/JV/funding-to-utilization conversion.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest reports:

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

Validation result:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

## 5. Historical Eligibility Gate

All representative trigger rows satisfy the 180 trading-day historical window requirement and have clean 180D windows.

| symbol | profile_path | price_shard_path | corporate_action_window_status |
| --- | --- | --- | --- |
| 373220 | atlas/symbol_profiles/373/373220.json | atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv|atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv | clean_180D_window |
| 006400 | atlas/symbol_profiles/006/006400.json | atlas/ohlcv_tradable_by_symbol_year/006/006400/2022.csv | clean_180D_window |
| 006400 | atlas/symbol_profiles/006/006400.json | atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv|atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | clean_180D_window |
| 096770 | atlas/symbol_profiles/096/096770.json | atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv|atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv | clean_180D_window; 2024-11-20 corporate-action candidate is outside this 180D window |

Notes:

- LG에너지솔루션 has no corporate-action candidates in its profile during the tested window.
- 삼성SDI has historic corporate-action candidates, but none overlap the 2022 or 2023 tested 180D windows.
- SK이노베이션 has a 2024-11-20 corporate-action candidate, but the 2023-06-23 BlueOval SK 180D test window ends before that candidate date, so the representative window remains usable.

## 6. Canonical Archetype Compression Map

```text
fine_archetype -> canonical_archetype_id

CELL_MAKER_IRA_AMPC_EARLY_OPTIONALITY
  -> C13_BATTERY_JV_UTILIZATION_AMPC_IRA

STELLANTIS_US_JV_FIRST_PLANT_DELAYED_RERATING
  -> C13_BATTERY_JV_UTILIZATION_AMPC_IRA

STELLANTIS_US_JV_SECOND_PLANT_FAR_OUT_CAPACITY_GUARD
  -> C13_BATTERY_JV_UTILIZATION_AMPC_IRA

BLUEOVAL_SK_DOE_LOAN_HIGH_MFE_HIGH_MAE_COUNTEREXAMPLE
  -> C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

Compression principle: a C13 row is not a generic “battery theme” row. It must contain a policy/JV/AMPC/funding route and then be split by whether that route becomes utilization or profit evidence.

## 7. Case Selection Summary

| case_id | symbol | company | fine_archetype | case_type | positive/counterexample | new_independent | independent_weight | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | 373220 | LG에너지솔루션 | CELL_MAKER_IRA_AMPC_EARLY_OPTIONALITY | structural_success | positive | True | 1.0 | The post-IRA Stage2 entry captured a +38.70% 90D/180D MFE, but the later peak was price-only; full 4B would still require non-price slowdown evidence. |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | 006400 | 삼성SDI | STELLANTIS_US_JV_FIRST_PLANT_DELAYED_RERATING | stage2_promote_candidate | positive | True | 1.0 | The first U.S. JV route did not pay in 30D, but it matured into a 180D MFE of +33.16%. This supports a delayed-rerating shadow route when customer identity + plant route are both named. |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | 006400 | 삼성SDI | STELLANTIS_US_JV_SECOND_PLANT_FAR_OUT_CAPACITY_GUARD | failed_rerating | counterexample | True | 0.5 | The same named-customer/JV pattern that worked in 2022 failed in 2023 when the announcement was repeat/far-out and not tied to immediate utilization or earnings conversion. |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | 096770 | SK이노베이션 | BLUEOVAL_SK_DOE_LOAN_HIGH_MFE_HIGH_MAE_COUNTEREXAMPLE | high_mae_success | counterexample | True | 1.0 | The event created a 30D MFE, but the drawdown and 180D MAE show why C13 needs a funding-loss/utilization guard rather than raw policy/JV promotion. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
calibration_usable_case_count = 4
new_independent_case_count = 4
new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
```

The balance is intentional. The positive cases show that named customer + plant/JV/policy route can work. The counterexamples show that the same raw ingredients fail when the capacity is far out, repeat-announcement quality is weaker, or the equity story is dominated by funding losses.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
| --- | --- | --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | policy_or_regulatory_optionality, capacity_or_volume_route, customer_or_order_quality | financial_visibility | price_only_local_peak | - |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | public_event_or_disclosure, capacity_or_volume_route, customer_or_order_quality | repeat_order_or_conversion | valuation_blowoff, price_only_local_peak | - |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | public_event_or_disclosure, capacity_or_volume_route, customer_or_order_quality | - | explicit_event_cap, margin_or_backlog_slowdown | thesis_evidence_broken |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | public_event_or_disclosure, capacity_or_volume_route, policy_or_regulatory_optionality | - | capital_raise_or_overhang, margin_or_backlog_slowdown, positioning_overheat | thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | corporate_action_window_status |
| --- | --- | --- | --- |
| 373220 | atlas/symbol_profiles/373/373220.json | atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv|atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv | clean_180D_window |
| 006400 | atlas/symbol_profiles/006/006400.json | atlas/ohlcv_tradable_by_symbol_year/006/006400/2022.csv | clean_180D_window |
| 006400 | atlas/symbol_profiles/006/006400.json | atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv|atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | clean_180D_window |
| 096770 | atlas/symbol_profiles/096/096770.json | atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv|atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv | clean_180D_window; 2024-11-20 corporate-action candidate is outside this 180D window |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown_after_peak | current_profile_verdict | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | 373220 | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 453500 | 13.78 | -7.39 | 38.7 | -8.49 | 38.7 | -8.49 | 2022-11-11 / 629000 | -33.07 | current_profile_correct | positive |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | 006400 | Stage2-Actionable | 2022-05-24 | 2022-05-25 | 588000 | 1.7 | -14.8 | 7.99 | -14.8 | 33.16 | -14.8 | 2022-11-14 / 783000 | -13.15 | current_profile_correct | positive |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | 006400 | Stage2-Actionable | 2023-10-11 | 2023-10-12 | 535000 | 0.75 | -22.06 | 0.75 | -36.07 | 0.75 | -38.32 | 2023-10-12 / 539000 | -38.78 | current_profile_too_early | counterexample |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | 096770 | Stage2-Actionable | 2023-06-22 | 2023-06-23 | 182600 | 25.68 | -13.58 | 25.68 | -34.23 | 25.68 | -41.13 | 2023-07-26 / 229500 | -53.16 | current_profile_false_positive | counterexample |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger metrics

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown_after_peak | current_profile_verdict | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | 373220 | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 453500 | 13.78 | -7.39 | 38.7 | -8.49 | 38.7 | -8.49 | 2022-11-11 / 629000 | -33.07 | current_profile_correct | positive |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | 006400 | Stage2-Actionable | 2022-05-24 | 2022-05-25 | 588000 | 1.7 | -14.8 | 7.99 | -14.8 | 33.16 | -14.8 | 2022-11-14 / 783000 | -13.15 | current_profile_correct | positive |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | 006400 | Stage2-Actionable | 2023-10-11 | 2023-10-12 | 535000 | 0.75 | -22.06 | 0.75 | -36.07 | 0.75 | -38.32 | 2023-10-12 / 539000 | -38.78 | current_profile_too_early | counterexample |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | 096770 | Stage2-Actionable | 2023-06-22 | 2023-06-23 | 182600 | 25.68 | -13.58 | 25.68 | -34.23 | 25.68 | -41.13 | 2023-07-26 / 229500 | -53.16 | current_profile_false_positive | counterexample |

### Interpretation

- LG에너지솔루션 IRA enactment entry produced strong 90D/180D MFE, but the observed peak was price-only and therefore not a standalone full 4B.
- 삼성SDI first Kokomo JV was a delayed success: the 30D window was weak, but the 180D window captured the structural rerating.
- 삼성SDI second Kokomo JV is the archetype counterexample: same named customer, but far-out production and no near-term utilization conversion created almost no MFE and heavy MAE.
- SK이노베이션 BlueOval SK loan is a high-MFE/high-MAE counterexample: the funding/JV headline produced a tradable rally, but not a durable rerating.

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | reason |
| --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | current_profile_correct | The post-IRA Stage2 entry captured a +38.70% 90D/180D MFE, but the later peak was price-only; full 4B would still require non-price slowdown evidence. |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | current_profile_correct | The first U.S. JV route did not pay in 30D, but it matured into a 180D MFE of +33.16%. This supports a delayed-rerating shadow route when customer identity + plant route are both named. |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | current_profile_too_early | The same named-customer/JV pattern that worked in 2022 failed in 2023 when the announcement was repeat/far-out and not tied to immediate utilization or earnings conversion. |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | current_profile_false_positive | The event created a 30D MFE, but the drawdown and 180D MAE show why C13 needs a funding-loss/utilization guard rather than raw policy/JV promotion. |

Stress-test answers:

1. **Stage2 bonus:** Useful for LGES and Samsung first Kokomo; too permissive if applied to far-out repeat JV capacity without utilization conversion.
2. **Yellow 75:** Kept. C13 rows should not reach Yellow just because a JV exists.
3. **Green 87 / revision 55:** Kept and strengthened for C13. Green requires AMPC-to-margin, utilization, or revision evidence.
4. **Price-only blowoff guard:** Kept. LGES and SKI show price peaks that cannot be treated as full 4B without non-price evidence.
5. **Full 4B non-price requirement:** Strengthened for C13 through funding-overhang and utilization-delay 4B overlays.
6. **Hard 4C routing:** Strengthened when repeated margin/utilization failure breaks the C13 thesis.

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2-Actionable works when:
  named_customer_or_policy_route = true
  AND capacity_or_volume_route = true
  AND either first-time route novelty or credible utilization path exists

Stage3-Yellow should require:
  confirmed utilization OR AMPC-to-margin evidence OR repeat order/minimum-volume evidence

Stage3-Green should require:
  revision_score >= current Green revision floor
  AND AMPC/JV evidence is already flowing into earnings, not only capex announcements
```

Green lateness audit:

| case_id | Stage2 entry | Stage3/Green comparison | green_lateness_ratio | verdict |
| --- | --- | --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | 2022-08-17 / 453500 | no confirmed Green trigger | not_applicable | not_applicable |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | 2022-05-25 / 588000 | delayed Green proxy | 0.32 | Green not severely late |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | 2023-10-12 / 535000 | no confirmed Green trigger | not_applicable | not_applicable |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | 2023-06-23 / 182600 | no confirmed Green trigger | not_applicable | not_applicable |

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | four_b_timing_verdict |
| --- | --- | --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | 1.0 | 1.0 | price_only | local_peak_detected_but_price_only_not_full_4B |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | 1.0 | 1.0 | valuation_blowoff, price_only | good_full_window_4B_timing_if_valuation_and_order_timing_confirmed |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | 1.0 | 1.0 | explicit_event_cap, margin_or_backlog_slowdown | good_full_window_4B_timing_if_event_cap_or_far_out_utilization_guard_applied |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | 1.0 | 1.0 | capital_raise_or_overhang, margin_or_backlog_slowdown | good_full_window_4B_timing_when_funding_or_loss_evidence_confirmed |

The key C13 observation is that local peaks created by policy/JV headlines are often not full 4B unless a non-price overhang appears. For SKI, the overhang is funding/loss burden. For Samsung second Kokomo, the overhang is far-out utilization and event-cap quality.

## 16. 4C Protection Audit

| case_id | four_c_protection_label | 4C interpretation |
| --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | thesis_break_watch_only | Hard 4C applies when the C13 thesis breaks through utilization/margin/funding evidence, not when price merely falls. |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | thesis_break_watch_only | Hard 4C applies when the C13 thesis breaks through utilization/margin/funding evidence, not when price merely falls. |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | hard_4c_success | Hard 4C applies when the C13 thesis breaks through utilization/margin/funding evidence, not when price merely falls. |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | hard_4c_success | Hard 4C applies when the C13 thesis breaks through utilization/margin/funding evidence, not when price merely falls. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = funding_overhang_4b_overlay
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate_delta = +1 guard axis
```

Rule candidate:

> In L3 battery rows, a policy/JV/loan headline should not promote above Stage2-Actionable when the issuer’s equity story is dominated by funding burden, losses, or delayed customer ramp. Treat it as Stage2 event optionality plus 4B/4C overlay, not as structural Green.

Backtest support: SK이노베이션 BlueOval SK produced +25.68% MFE but -41.13% 180D MAE and -53.16% drawdown after peak.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
preferred_rule = named_customer_utilization_ampc_conversion_guard
```

Rule candidate:

```text
if C13 and named_customer_or_policy_route:
    allow Stage2-Actionable
if C13 and far_out_capacity_without_utilization_or_ampc_margin:
    block Stage3-Yellow/Green
if C13 and first_named_customer_route + credible utilization path:
    allow delayed-rerating Stage2-Actionable bonus
if C13 and funding_overhang/loss burden dominates:
    keep positive stage capped and attach 4B/4C risk overlay
```

This is not a global rule. It is specific to battery JV/AMPC/utilization paths.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_4B_local | avg_4B_full | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | current calibrated proxy | none | 4 | one representative per case | 18.28 | -23.4 | 24.57 | -25.69 | 0.0 | 0 | 0 | n/a | 1.0 | 1.0 | mixed |
| P0b | e2r_2_0_baseline_reference | rollback reference | older baseline, no stock-web v12 residual guard | 4 | one representative per case | 18.28 | -23.4 | 24.57 | -25.69 | 0.0 | 0 | 0 | n/a | 1.0 | 1.0 | mixed |
| P1 | sector_specific_candidate_profile | L3 battery AMPC/JV guard | sector named-customer utilization guard | 4 | one representative per case | 18.28 | -23.4 | 24.57 | -25.69 | 0.5 | 0 | 0 | n/a | 1.0 | 1.0 | mixed |
| P2 | canonical_archetype_candidate_profile | C13-specific utilization/AMPC conversion guard | named_customer_minimum_volume_bonus + far_out_capacity_guard + funding_overhang_4B | 4 | one representative per case | 18.28 | -23.4 | 24.57 | -25.69 | 0.5 | 0 | 0 | n/a | 1.0 | 1.0 | P2/P3 improve counterexample separation |
| P3 | counterexample_guard_profile | strict guard for far-out capacity/funding loss | blocks Stage3 for far-out/funding-loss rows | 4 | one representative per case | 18.28 | -23.4 | 24.57 | -25.69 | 0.0 | 0 | 0 | n/a | 1.0 | 1.0 | P2/P3 improve counterexample separation |

## 20. Score-Return Alignment Matrix

| case_id | P0 score/stage | P2 score/stage | 180D outcome | alignment verdict |
| --- | --- | --- | --- | --- |
| R3L70_C13_373220_IRA_ENACTMENT_STAGE2 | 63.3 / Stage2-Actionable | 65.8 / Stage2-Actionable | MFE 38.7%, MAE -8.49% | aligned_positive |
| R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO | 59.0 / Stage2 | 62.0 / Stage2-Actionable delayed-rerating candidate | MFE 33.16%, MAE -14.8% | aligned_positive |
| R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO | 36.2 / Watch/Blocked | 24.2 / Stage2/Blocked by C13 far_out_capacity_guard | MFE 0.75%, MAE -38.32% | aligned_counterexample |
| R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN | 42.7 / Watch/Blocked | 31.7 / Stage2-Actionable; no Stage3 until AMPC-to-margin closes | MFE 25.68%, MAE -41.13% | aligned_counterexample |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | multiple: see case rows | 2 | 2 | 3 | 2 | 4 | 0 | 4 | 4 | 2 | True | True | C13 now has positive/counterexample balance; still needs C13 holdout outside Korea and more post-2025 rows after manifest max date. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
  - far_out_capacity_false_positive
  - funding_overhang_high_mfe_high_mae
  - AMPC_to_margin_conversion_missing

new_axis_proposed:
  - named_customer_minimum_volume_bonus
  - far_out_capacity_guard
  - funding_overhang_4b_overlay
  - ampc_to_margin_conversion_required_for_green

existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
validated:
  - Stock-Web manifest fields
  - stock-web tradable_raw OHLCV rows for selected symbols
  - representative trigger entry dates and entry prices
  - 30D/90D/180D MFE/MAE calculations from stock-web row windows
  - corporate-action overlap checks from symbol profiles
  - C13 positive/counterexample balance
  - current calibrated profile stress test
```

Non-validation scope:

```text
not_validated:
  - current/live candidate discovery
  - production scoring code
  - stock_agent src/e2r implementation
  - broker execution
  - investment recommendation
  - post-2026-02-20 stock-web prices
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,named_customer_minimum_volume_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,Named customer plus concrete plant/JV route worked when first route was new and capacity-to-revenue was plausible.,Positive cases had +38.70% and +33.16% 180D MFE.,R3L70_C13_373220_T1_STAGE2_ACTIONABLE_IRA_ENACTMENT|R3L70_C13_006400_T1_STAGE2_ACTIONABLE_STELLANTIS_FIRST_KOKOMO,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,far_out_capacity_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,Repeat/far-out capacity announcements created poor 180D alignment without near-term utilization or AMPC-to-margin evidence.,Samsung second Kokomo row had +0.75% MFE180 and -38.32% MAE180.,R3L70_C13_006400_T2_STAGE2_ACTIONABLE_SECOND_KOKOMO_COUNTEREXAMPLE,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,funding_overhang_4b_overlay,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,A policy/loan/JV headline can produce MFE but still fail durable rerating when funding burden and operating losses dominate.,SKI BlueOval loan row: +25.68% MFE180 but -41.13% MAE180 and -53.16% drawdown after peak.,R3L70_C13_096770_T1_STAGE2_ACTIONABLE_BLUEOVAL_SK_LOAN,4,4,2,medium,sector_shadow_only,not production; post-calibrated residual
shadow_weight,ampc_to_margin_conversion_required_for_green,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"Green should require AMPC-to-margin or utilization evidence, not just policy eligibility.",Separates LGES/Samsung first-stage positives from Samsung second/SKI counterexamples.,R3L70_C13_373220_T1_STAGE2_ACTIONABLE_IRA_ENACTMENT|R3L70_C13_006400_T1_STAGE2_ACTIONABLE_STELLANTIS_FIRST_KOKOMO|R3L70_C13_006400_T2_STAGE2_ACTIONABLE_SECOND_KOKOMO_COUNTEREXAMPLE|R3L70_C13_096770_T1_STAGE2_ACTIONABLE_BLUEOVAL_SK_LOAN,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "source_name": "FinanceData/marcap", "source_repo_url": "https://github.com/FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L70_C13_373220_IRA_ENACTMENT_STAGE2", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "CELL_MAKER_IRA_AMPC_EARLY_OPTIONALITY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R3L70_C13_373220_T1_STAGE2_ACTIONABLE_IRA_ENACTMENT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "The post-IRA Stage2 entry captured a +38.70% 90D/180D MFE, but the later peak was price-only; full 4B would still require non-price slowdown evidence."}
{"row_type": "case", "case_id": "R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "STELLANTIS_US_JV_FIRST_PLANT_DELAYED_RERATING", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R3L70_C13_006400_T1_STAGE2_ACTIONABLE_STELLANTIS_FIRST_KOKOMO", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "The first U.S. JV route did not pay in 30D, but it matured into a 180D MFE of +33.16%. This supports a delayed-rerating shadow route when customer identity + plant route are both named."}
{"row_type": "case", "case_id": "R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "STELLANTIS_US_JV_SECOND_PLANT_FAR_OUT_CAPACITY_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R3L70_C13_006400_T2_STAGE2_ACTIONABLE_SECOND_KOKOMO_COUNTEREXAMPLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "The same named-customer/JV pattern that worked in 2022 failed in 2023 when the announcement was repeat/far-out and not tied to immediate utilization or earnings conversion."}
{"row_type": "case", "case_id": "R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN", "symbol": "096770", "company_name": "SK이노베이션", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BLUEOVAL_SK_DOE_LOAN_HIGH_MFE_HIGH_MAE_COUNTEREXAMPLE", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R3L70_C13_096770_T1_STAGE2_ACTIONABLE_BLUEOVAL_SK_LOAN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The event created a 30D MFE, but the drawdown and 180D MAE show why C13 needs a funding-loss/utilization guard rather than raw policy/JV promotion."}
{"row_type": "trigger", "trigger_id": "R3L70_C13_373220_T1_STAGE2_ACTIONABLE_IRA_ENACTMENT", "case_id": "R3L70_C13_373220_IRA_ENACTMENT_STAGE2", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "CELL_MAKER_IRA_AMPC_EARLY_OPTIONALITY", "sector": "배터리·EV·그린모빌리티", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-16", "evidence_available_at_that_date": "U.S. IRA signing created AMPC/production-credit optionality for U.S. battery manufacturing. LGES already had U.S. JV/plant exposure, so this was a Stage2-Actionable policy-to-utilization bridge, not a confirmed Green revision event.", "evidence_source": "U.S. Inflation Reduction Act signing; stock-web rows atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv and 2023.csv.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv|atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-08-17", "entry_price": 453500, "MFE_30D_pct": 13.78, "MFE_90D_pct": 38.7, "MFE_180D_pct": 38.7, "MFE_1Y_pct": 38.7, "MFE_2Y_pct": null, "MAE_30D_pct": -7.39, "MAE_90D_pct": -8.49, "MAE_180D_pct": -8.49, "MAE_1Y_pct": -33.07, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-11", "peak_price": 629000, "drawdown_after_peak_pct": -33.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "local_peak_detected_but_price_only_not_full_4B", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_with_price_only_local_peak_risk", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L70_C13_373220_IRA_ENACTMENT_STAGE2_entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R3L70_C13_006400_T1_STAGE2_ACTIONABLE_STELLANTIS_FIRST_KOKOMO", "case_id": "R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "STELLANTIS_US_JV_FIRST_PLANT_DELAYED_RERATING", "sector": "배터리·EV·그린모빌리티", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-05-24", "evidence_available_at_that_date": "Stellantis-Samsung SDI first Kokomo battery JV/plant announcement created a concrete U.S. capacity route; AMPC was not yet a fully confirmed earnings line, so this is Stage2/Stage2-Actionable rather than Stage3-Green.", "evidence_source": "Stellantis/Samsung SDI first Kokomo JV public announcement; stock-web rows atlas/ohlcv_tradable_by_symbol_year/006/006400/2022.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": ["repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2022.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-05-25", "entry_price": 588000, "MFE_30D_pct": 1.7, "MFE_90D_pct": 7.99, "MFE_180D_pct": 33.16, "MFE_1Y_pct": 33.16, "MFE_2Y_pct": null, "MAE_30D_pct": -14.8, "MAE_90D_pct": -14.8, "MAE_180D_pct": -14.8, "MAE_1Y_pct": -14.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-14", "peak_price": 783000, "drawdown_after_peak_pct": -13.15, "green_lateness_ratio": 0.32, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_valuation_and_order_timing_confirmed", "four_b_evidence_type": ["valuation_blowoff", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "delayed_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO_entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R3L70_C13_006400_T2_STAGE2_ACTIONABLE_SECOND_KOKOMO_COUNTEREXAMPLE", "case_id": "R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "STELLANTIS_US_JV_SECOND_PLANT_FAR_OUT_CAPACITY_GUARD", "sector": "배터리·EV·그린모빌리티", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-11", "evidence_available_at_that_date": "Second Kokomo plant was public and customer-linked, but production was far out and did not provide near-term utilization/AMPC earnings conversion. This tests whether the current profile promotes a repeated JV announcement too early.", "evidence_source": "Public announcement of the second Stellantis-Samsung SDI Kokomo plant; stock-web rows atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv and 2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv|atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-10-12", "entry_price": 535000, "MFE_30D_pct": 0.75, "MFE_90D_pct": 0.75, "MFE_180D_pct": 0.75, "MFE_1Y_pct": 0.75, "MFE_2Y_pct": null, "MAE_30D_pct": -22.06, "MAE_90D_pct": -36.07, "MAE_180D_pct": -38.32, "MAE_1Y_pct": -38.32, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-10-12", "peak_price": 539000, "drawdown_after_peak_pct": -38.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_event_cap_or_far_out_utilization_guard_applied", "four_b_evidence_type": ["explicit_event_cap", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating_false_positive_guard", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO_entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R3L70_C13_096770_T1_STAGE2_ACTIONABLE_BLUEOVAL_SK_LOAN", "case_id": "R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN", "symbol": "096770", "company_name": "SK이노베이션", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BLUEOVAL_SK_DOE_LOAN_HIGH_MFE_HIGH_MAE_COUNTEREXAMPLE", "sector": "배터리·EV·그린모빌리티", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4C_thesis_break_timing_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-22", "evidence_available_at_that_date": "DOE conditional loan to BlueOval SK gave a concrete financing/JV route, but the equity path remained hostage to SK On losses, funding burden, and EV demand. This is a high-MFE/high-MAE counterexample: playable event, weak durable rerating.", "evidence_source": "DOE/Reuters-style public loan report for BlueOval SK; stock-web rows atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv and 2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv|atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv", "profile_path": "atlas/symbol_profiles/096/096770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-23", "entry_price": 182600, "MFE_30D_pct": 25.68, "MFE_90D_pct": 25.68, "MFE_180D_pct": 25.68, "MFE_1Y_pct": 25.68, "MFE_2Y_pct": null, "MAE_30D_pct": -13.58, "MAE_90D_pct": -34.23, "MAE_180D_pct": -41.13, "MAE_1Y_pct": -41.13, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 229500, "drawdown_after_peak_pct": -53.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_when_funding_or_loss_evidence_confirmed", "four_b_evidence_type": ["capital_raise_or_overhang", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "high_mfe_high_mae_failed_durable_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2024-11-20 corporate-action candidate is outside this 180D window", "same_entry_group_id": "R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN_entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L70_C13_373220_IRA_ENACTMENT_STAGE2", "trigger_id": "R3L70_C13_373220_T1_STAGE2_ACTIONABLE_IRA_ENACTMENT", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 70, "policy_or_regulatory_score": 85, "valuation_repricing_score": 60, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 55, "ampc_conversion_score": 45, "funding_overhang_score": 20, "far_out_capacity_score": 15}, "weighted_score_before": 63.3, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 70, "policy_or_regulatory_score": 85, "valuation_repricing_score": 60, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 55, "ampc_conversion_score": 45, "funding_overhang_score": 20, "far_out_capacity_score": 15}, "weighted_score_after": 63.3, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "P0 current proxy; no shadow delta applied.", "MFE_90D_pct": 38.7, "MAE_90D_pct": -8.49, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C13_shadow_named_customer_utilization_ampc_guard", "case_id": "R3L70_C13_373220_IRA_ENACTMENT_STAGE2", "trigger_id": "R3L70_C13_373220_T1_STAGE2_ACTIONABLE_IRA_ENACTMENT", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 70, "policy_or_regulatory_score": 85, "valuation_repricing_score": 60, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 55, "ampc_conversion_score": 45, "funding_overhang_score": 20, "far_out_capacity_score": 15}, "weighted_score_before": 63.3, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 50, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 70, "policy_or_regulatory_score": 85, "valuation_repricing_score": 60, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 55, "ampc_conversion_score": 45, "funding_overhang_score": 20, "far_out_capacity_score": 15}, "weighted_score_after": 65.8, "stage_label_after": "Stage2-Actionable", "changed_components": ["utilization_score", "ampc_conversion_score", "funding_overhang_score", "far_out_capacity_score"], "component_delta_explanation": "C13 shadow guard rewards named customer + plant route only when utilization/AMPC-to-margin evidence closes; penalizes far-out capacity and funding-loss overhang.", "MFE_90D_pct": 38.7, "MAE_90D_pct": -8.49, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO", "trigger_id": "R3L70_C13_006400_T1_STAGE2_ACTIONABLE_STELLANTIS_FIRST_KOKOMO", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 65, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 45, "customer_quality_score": 80, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 50, "ampc_conversion_score": 35, "funding_overhang_score": 25, "far_out_capacity_score": 35}, "weighted_score_before": 59.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 65, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 45, "customer_quality_score": 80, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 50, "ampc_conversion_score": 35, "funding_overhang_score": 25, "far_out_capacity_score": 35}, "weighted_score_after": 59.0, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "P0 current proxy; no shadow delta applied.", "MFE_90D_pct": 7.99, "MAE_90D_pct": -14.8, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C13_shadow_named_customer_utilization_ampc_guard", "case_id": "R3L70_C13_006400_STELLANTIS_FIRST_KOKOMO", "trigger_id": "R3L70_C13_006400_T1_STAGE2_ACTIONABLE_STELLANTIS_FIRST_KOKOMO", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 65, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 45, "customer_quality_score": 80, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 50, "ampc_conversion_score": 35, "funding_overhang_score": 25, "far_out_capacity_score": 35}, "weighted_score_before": 59.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 65, "backlog_visibility_score": 55, "margin_bridge_score": 35, "revision_score": 25, "relative_strength_score": 45, "customer_quality_score": 80, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 40, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 50, "ampc_conversion_score": 45, "funding_overhang_score": 25, "far_out_capacity_score": 35}, "weighted_score_after": 62.0, "stage_label_after": "Stage2-Actionable delayed-rerating candidate", "changed_components": ["utilization_score", "ampc_conversion_score", "funding_overhang_score", "far_out_capacity_score"], "component_delta_explanation": "C13 shadow guard rewards named customer + plant route only when utilization/AMPC-to-margin evidence closes; penalizes far-out capacity and funding-loss overhang.", "MFE_90D_pct": 7.99, "MAE_90D_pct": -14.8, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO", "trigger_id": "R3L70_C13_006400_T2_STAGE2_ACTIONABLE_SECOND_KOKOMO_COUNTEREXAMPLE", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 15, "relative_strength_score": 20, "customer_quality_score": 78, "policy_or_regulatory_score": 60, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 20, "ampc_conversion_score": 10, "funding_overhang_score": 35, "far_out_capacity_score": 85}, "weighted_score_before": 36.2, "stage_label_before": "Watch/Blocked", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 15, "relative_strength_score": 20, "customer_quality_score": 78, "policy_or_regulatory_score": 60, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 20, "ampc_conversion_score": 10, "funding_overhang_score": 35, "far_out_capacity_score": 85}, "weighted_score_after": 36.2, "stage_label_after": "Watch/Blocked", "changed_components": [], "component_delta_explanation": "P0 current proxy; no shadow delta applied.", "MFE_90D_pct": 0.75, "MAE_90D_pct": -36.07, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "C13_shadow_named_customer_utilization_ampc_guard", "case_id": "R3L70_C13_006400_STELLANTIS_SECOND_KOKOMO", "trigger_id": "R3L70_C13_006400_T2_STAGE2_ACTIONABLE_SECOND_KOKOMO_COUNTEREXAMPLE", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 15, "relative_strength_score": 20, "customer_quality_score": 78, "policy_or_regulatory_score": 60, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 20, "ampc_conversion_score": 10, "funding_overhang_score": 35, "far_out_capacity_score": 85}, "weighted_score_before": 36.2, "stage_label_before": "Watch/Blocked", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 15, "relative_strength_score": 20, "customer_quality_score": 78, "policy_or_regulatory_score": 60, "valuation_repricing_score": 35, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 10, "ampc_conversion_score": 5, "funding_overhang_score": 35, "far_out_capacity_score": 95}, "weighted_score_after": 24.2, "stage_label_after": "Stage2/Blocked by C13 far_out_capacity_guard", "changed_components": ["utilization_score", "ampc_conversion_score", "funding_overhang_score", "far_out_capacity_score"], "component_delta_explanation": "C13 shadow guard rewards named customer + plant route only when utilization/AMPC-to-margin evidence closes; penalizes far-out capacity and funding-loss overhang.", "MFE_90D_pct": 0.75, "MAE_90D_pct": -36.07, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN", "trigger_id": "R3L70_C13_096770_T1_STAGE2_ACTIONABLE_BLUEOVAL_SK_LOAN", "symbol": "096770", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 45, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 65, "customer_quality_score": 70, "policy_or_regulatory_score": 80, "valuation_repricing_score": 45, "execution_risk_score": 80, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 20, "ampc_conversion_score": 15, "funding_overhang_score": 85, "far_out_capacity_score": 55}, "weighted_score_before": 42.7, "stage_label_before": "Watch/Blocked", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 45, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 65, "customer_quality_score": 70, "policy_or_regulatory_score": 80, "valuation_repricing_score": 45, "execution_risk_score": 80, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 20, "ampc_conversion_score": 15, "funding_overhang_score": 85, "far_out_capacity_score": 55}, "weighted_score_after": 42.7, "stage_label_after": "Watch/Blocked", "changed_components": [], "component_delta_explanation": "P0 current proxy; no shadow delta applied.", "MFE_90D_pct": 25.68, "MAE_90D_pct": -34.23, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C13_shadow_named_customer_utilization_ampc_guard", "case_id": "R3L70_C13_096770_BLUEOVAL_SK_DOE_LOAN", "trigger_id": "R3L70_C13_096770_T1_STAGE2_ACTIONABLE_BLUEOVAL_SK_LOAN", "symbol": "096770", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 45, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 65, "customer_quality_score": 70, "policy_or_regulatory_score": 80, "valuation_repricing_score": 45, "execution_risk_score": 80, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 20, "ampc_conversion_score": 15, "funding_overhang_score": 85, "far_out_capacity_score": 55}, "weighted_score_before": 42.7, "stage_label_before": "Watch/Blocked", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 45, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 65, "customer_quality_score": 70, "policy_or_regulatory_score": 80, "valuation_repricing_score": 45, "execution_risk_score": 80, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "utilization_score": 10, "ampc_conversion_score": 5, "funding_overhang_score": 95, "far_out_capacity_score": 55}, "weighted_score_after": 31.7, "stage_label_after": "Stage2-Actionable; no Stage3 until AMPC-to-margin closes", "changed_components": ["utilization_score", "ampc_conversion_score", "funding_overhang_score", "far_out_capacity_score"], "component_delta_explanation": "C13 shadow guard rewards named customer + plant route only when utilization/AMPC-to-margin evidence closes; penalizes far-out capacity and funding-loss overhang.", "MFE_90D_pct": 25.68, "MAE_90D_pct": -34.23, "score_return_alignment_label": "aligned_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R3", "loop": "70", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 1, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["far_out_capacity_false_positive", "funding_overhang_high_mfe_high_mae", "AMPC_to_margin_conversion_missing"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = R3_loop_71_C14_EV_DEMAND_SLOWDOWN_4B_4C
reason = C13 now has balanced positive/counterexample coverage; next residual gap is EV demand slowdown and 4B/4C transition timing.
```

## 28. Source Notes

Stock-web files consulted:

```text
atlas/manifest.json
atlas/symbol_profiles/373/373220.json
atlas/symbol_profiles/006/006400.json
atlas/symbol_profiles/096/096770.json
atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv
atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2022.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv
atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv
atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv
```

Research artifact files consulted only for duplicate avoidance:

```text
data/e2r/calibration/md_registry.jsonl
GitHub search exact query: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```
