# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 114
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE
deep_sub_archetype_id: C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE
loop_objective: coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery
price_source: Songdaiki/stock-web
upstream_price_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: '2026-02-20'
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This file is a standalone V12 historical calibration artifact. It is not live candidate discovery, not a trade recommendation, not a code patch, and not production scoring. The research question is narrow: within `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`, when does advanced semiconductor-equipment vocabulary deserve positive Stage2/Yellow credit, and when is it only a price/theme blowoff overlay?

## 1. Current Calibrated Profile Assumption

```yaml
current_default_profile_proxy: e2r_2_1_stock_web_calibrated
previous_baseline_reference: e2r_2_0_baseline
stage2_actionable_evidence_bonus: +2.0
stage3_yellow_total_min: 75.0
stage3_green_total_min: 87.0
stage3_green_revision_min: 55.0
price_only_blowoff_blocks_positive_stage: true
full_4b_requires_non_price_evidence: true
hard_4c_thesis_break_routes_to_4c: true
```

This loop does not repeat the global rule that price-only 4B is not enough. Instead it compresses a C09-specific distinction: advanced equipment scarcity is real only when order, shipment, revenue, margin, or revision bridge is already visible. Otherwise the theme behaves like a polished lens: it concentrates attention, heats valuation, and burns the entry before the business bridge arrives.

## 2. Round / Large Sector / Canonical Archetype Scope

- `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`.
- This loop intentionally repeats C09 because the local session-adjusted row count remains below the 30-row floor after loop 113.
- Previous C09 loop 113 symbols avoided: `322310`, `403870`, `348210`, `281820`, `140860`, `240810`.
- This loop uses different C09 symbol/date groups: `036930`, `253590`, `092870`, `064290`, `083450`, `095610`, `084370`.

## 3. Previous Coverage / Duplicate Avoidance Check

```yaml
index_rows_for_C09: 10
local_session_prior_C09_loop113_representative_rows: 6
local_session_adjusted_pre_loop_rows: 16
representative_rows_added_this_loop: 7
estimated_post_loop_rows_for_C09: 23
remaining_to_30_row_floor: 7
remaining_to_50_row_preferred_depth: 27
hard_duplicate_check:
  key: canonical_archetype_id + symbol + trigger_type + entry_date
  status: pass
  previous_C09_loop113_symbol_reuse: none
```

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
price_data_source: Songdaiki/stock-web
source_url: https://github.com/Songdaiki/stock-web
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: '2026-02-20'
tradable_row_count: 14354401
symbol_count: 5414
validation_status: usable_for_historical_calibration
```

All trigger rows below include 30D/90D/180D MFE and MAE using tradable raw OHLC windows. Entry is the trigger date close or next tradable close according to evidence timing.

## 5. Historical Eligibility Gate

| gate | status | note |
|---|---|---|
| 180 trading-day forward window | pass | all entries finish before 2026-02-20 manifest max date |
| price basis | pass | tradable_raw / raw_unadjusted_marcap |
| required MFE/MAE fields | pass | every trigger has MFE_30D/90D/180D and MAE_30D/90D/180D |
| round-sector consistency | pass | C09 -> R2 / L2 |
| compact filename forbidden | pass | standard v12 filename used |
| stock_agent code access | pass | no production code patch/read required |

## 6. Canonical Archetype Compression Map

| fine/deep route | compressed canonical | reason |
|---|---|---|
| HBM tester delivery / QA-stage evidence | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | real bridge exists, but mass-production/revision proof controls Stage3 credit |
| tester/order vocabulary after local advance | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | late Yellow without margin/revenue bridge becomes blowoff risk |
| HBM inspection expectation | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | expectation-only inspection label cannot unlock Yellow |
| AI cooling / chiller equipment theme | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | theme substitution should route to 4B watch |
| front-end memory equipment beta | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | cycle beta without fresh order bridge is not enough for positive Stage3 |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current profile verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C09-L114-01 | 036930 | 주성엔지니어링 | positive | Stage2-Actionable | 2023-04-10 | 17130 | 17.34 | -13.78 | 74.55 | -13.78 | 121.83 | -13.78 | current_profile_missed_structural_if_blocked_completely |
| C09-L114-02 | 253590 | 네오셈 | positive | Stage2-Actionable | 2024-06-05 | 11280 | 53.10 | -15.96 | 53.10 | -34.22 | 53.10 | -34.22 | current_profile_correct_if_green_blocked |
| C09-L114-03 | 092870 | 엑시콘 | counterexample | Stage3-Yellow | 2024-07-04 | 22550 | 11.53 | -50.11 | 11.53 | -56.59 | 11.53 | -62.71 | current_profile_false_positive_late_yellow |
| C09-L114-04 | 064290 | 인텍플러스 | counterexample | Stage3-Yellow | 2024-07-16 | 21600 | 1.39 | -31.44 | 1.39 | -57.31 | 1.39 | -63.06 | current_profile_false_positive |
| C09-L114-05 | 083450 | GST | counterexample | Stage4B | 2024-03-15 | 55100 | 11.62 | -22.87 | 11.62 | -70.94 | 11.62 | -77.11 | current_profile_4B_too_late_if_treated_as_yellow |
| C09-L114-06 | 095610 | 테스 | counterexample | Stage3-Yellow | 2024-05-02 | 24300 | 4.12 | -9.05 | 14.40 | -34.65 | 14.40 | -46.13 | current_profile_false_positive |
| C09-L114-07 | 084370 | 유진테크 | counterexample | Stage4B | 2024-05-02 | 53200 | 12.78 | -12.22 | 12.78 | -33.55 | 12.78 | -43.05 | current_profile_4B_too_late |


## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 2
counterexample_count: 5
stage4b_case_count: 2
stage4c_case_count: 0
current_profile_error_count: 6
source_proxy_only_count: 3
evidence_url_pending_count: 3
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
```

The balance is intentionally counterexample-heavy because C09's residual risk is not missing winners; it is over-promoting advanced-equipment labels that have not yet crossed into order, revenue, margin, or revision confirmation.

## 9. Evidence Source Map

| source_id | role | URL / path | note |
|---|---|---|---|
| MAIN_PROMPT | execution prompt | https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt | v12 stock-web residual research procedure |
| NO_REPEAT_INDEX | duplicate/coverage ledger | https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md | C09 Priority 0 under-30 coverage gap |
| STOCK_WEB_MANIFEST | price source manifest | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json | max_date 2026-02-20, tradable_raw, raw_unadjusted_marcap |
| DOCS_ROUND_TREE | loop number check | https://github.com/Songdaiki/stock_agent/tree/main/docs/round | visible C09 max loop 112; local session loop113 already used |
| EVIDENCE_253590 | tester delivery evidence | https://www.thebell.co.kr/front/newsview.asp?key=202406050911561880105029 | HBM burn-in tester delivery / QA-stage evidence |
| EVIDENCE_092870 | tester/order follow-up | https://zdnet.co.kr/view/?no=20240704084503 | tester order/conversion narrative, late trigger stress test |
| EVIDENCE_064290 | inspection-equipment expectation | https://www.dailyinvest.kr/news/articleView.html?idxno=59633 | HBM inspection beneficiary expectation without bridge |
| EVIDENCE_083450 | AI cooling/chiller theme | https://v.daum.net/v/20240312102259830 | theme substitution / 4B watch |
| PRICE_SHARD_036930 | OHLC shard | atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv | tradable raw OHLC window |
| PRICE_SHARD_253590 | OHLC shard | atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv | tradable raw OHLC window |
| PRICE_SHARD_092870 | OHLC shard | atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv | tradable raw OHLC window |
| PRICE_SHARD_064290 | OHLC shard | atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv | tradable raw OHLC window |
| PRICE_SHARD_083450 | OHLC shard | atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv | tradable raw OHLC window |
| PRICE_SHARD_095610 | OHLC shard | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | tradable raw OHLC window |
| PRICE_SHARD_084370 | OHLC shard | atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv | tradable raw OHLC window |


## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | selected window | status |
|---:|---|---|---|---|---|
| 036930 | 주성엔지니어링 | atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv | atlas/symbol_profiles/036/036930.json | 2023-04-10 + 180D | usable |
| 253590 | 네오셈 | atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv | atlas/symbol_profiles/253/253590.json | 2024-06-05 + 180D | usable |
| 092870 | 엑시콘 | atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv | atlas/symbol_profiles/092/092870.json | 2024-07-04 + 180D | usable |
| 064290 | 인텍플러스 | atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv | atlas/symbol_profiles/064/064290.json | 2024-07-16 + 180D | usable |
| 083450 | GST | atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv | atlas/symbol_profiles/083/083450.json | 2024-03-15 + 180D | usable |
| 095610 | 테스 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | atlas/symbol_profiles/095/095610.json | 2024-05-02 + 180D | usable |
| 084370 | 유진테크 | atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv | atlas/symbol_profiles/084/084370.json | 2024-05-02 + 180D | usable |


## 11. Case-by-Case Trigger Grid

### C09-L114-01 — 주성엔지니어링 / 036930

memory production-cut cycle reset plus ALD/CVD advanced-node equipment beta. It is not direct equipment backlog, so C09 should cap at Actionable until order/margin bridge appears. This row keeps positive credit, but only at Stage2-Actionable because C09 Green must wait for mass-production revenue, margin, and revision proof. Stock-Web path: MFE90 74.55%, MAE90 -13.78%, MFE180 121.83%, MAE180 -13.78%.

### C09-L114-02 — 네오셈 / 253590

HBM burn-in tester delivery / QA-stage evidence creates a real bridge, but mass-production revenue visibility is still partial, so Green must remain blocked. This row keeps positive credit, but only at Stage2-Actionable because C09 Green must wait for mass-production revenue, margin, and revision proof. Stock-Web path: MFE90 53.10%, MAE90 -34.22%, MFE180 53.10%, MAE180 -34.22%.

### C09-L114-03 — 엑시콘 / 092870

memory/CXL/HBM tester order-conversion vocabulary appeared after the local advance, but the realized path says late Yellow without revenue/margin bridge is C09 blowoff, not durable rerating. This row is a residual false-positive: the vocabulary was real enough to tempt Yellow, but the 180D path says the bridge was missing. Stock-Web path: MFE90 11.53%, MAE90 -56.59%, MFE180 11.53%, MAE180 -62.71%.

### C09-L114-04 — 인텍플러스 / 064290

HBM inspection-equipment expectation existed, but confirmed shipment/revenue bridge was insufficient at the trigger date. The price path collapsed almost immediately. This row is a residual false-positive: the vocabulary was real enough to tempt Yellow, but the 180D path says the bridge was missing. Stock-Web path: MFE90 1.39%, MAE90 -57.31%, MFE180 1.39%, MAE180 -63.06%.

### C09-L114-05 — GST / 083450

AI cooling / chiller narrative substituted for verified equipment-order conversion. The case belongs in C09 as a price-and-theme blowoff guard, not a positive rerating row. This row is not a promotion row. It is a 4B overlay proving that a local advanced-equipment theme peak can be dangerous when non-price bridge is missing. Stock-Web path: MFE90 11.62%, MAE90 -70.94%, MFE180 11.62%, MAE180 -77.11%.

### C09-L114-06 — 테스 / 095610

memory capex recovery label and equipment beta existed, but fresh order backlog, margin, or revision bridge was absent at the trigger date. This row is a residual false-positive: the vocabulary was real enough to tempt Yellow, but the 180D path says the bridge was missing. Stock-Web path: MFE90 14.40%, MAE90 -34.65%, MFE180 14.40%, MAE180 -46.13%.

### C09-L114-07 — 유진테크 / 084370

front-end memory-equipment recovery and advanced process vocabulary were already priced; without fresh non-price bridge this becomes local/full-window 4B watch. This row is not a promotion row. It is a 4B overlay proving that a local advanced-equipment theme peak can be dangerous when non-price bridge is missing. Stock-Web path: MFE90 12.78%, MAE90 -33.55%, MFE180 12.78%, MAE180 -43.05%.


## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | company | role | trigger | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current profile verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C09-L114-01 | 036930 | 주성엔지니어링 | positive | Stage2-Actionable | 2023-04-10 | 17130 | 17.34 | -13.78 | 74.55 | -13.78 | 121.83 | -13.78 | current_profile_missed_structural_if_blocked_completely |
| C09-L114-02 | 253590 | 네오셈 | positive | Stage2-Actionable | 2024-06-05 | 11280 | 53.10 | -15.96 | 53.10 | -34.22 | 53.10 | -34.22 | current_profile_correct_if_green_blocked |
| C09-L114-03 | 092870 | 엑시콘 | counterexample | Stage3-Yellow | 2024-07-04 | 22550 | 11.53 | -50.11 | 11.53 | -56.59 | 11.53 | -62.71 | current_profile_false_positive_late_yellow |
| C09-L114-04 | 064290 | 인텍플러스 | counterexample | Stage3-Yellow | 2024-07-16 | 21600 | 1.39 | -31.44 | 1.39 | -57.31 | 1.39 | -63.06 | current_profile_false_positive |
| C09-L114-05 | 083450 | GST | counterexample | Stage4B | 2024-03-15 | 55100 | 11.62 | -22.87 | 11.62 | -70.94 | 11.62 | -77.11 | current_profile_4B_too_late_if_treated_as_yellow |
| C09-L114-06 | 095610 | 테스 | counterexample | Stage3-Yellow | 2024-05-02 | 24300 | 4.12 | -9.05 | 14.40 | -34.65 | 14.40 | -46.13 | current_profile_false_positive |
| C09-L114-07 | 084370 | 유진테크 | counterexample | Stage4B | 2024-05-02 | 53200 | 12.78 | -12.22 | 12.78 | -33.55 | 12.78 | -43.05 | current_profile_4B_too_late |


## 13. Current Calibrated Profile Stress Test

| profile | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 current calibrated proxy | 7 | 25.62 | -43.01 | 32.38 | -48.58 | 0.71 | weak alignment; C09 still over-promotes late theme/RS rows |
| P0b baseline reference | 7 | 25.62 | -43.01 | 32.38 | -48.58 | 0.71 | rollback reference only; no improvement |
| P1 sector candidate | 3 | 46.39 | -34.86 | 62.15 | -36.9 | 0.33 | improved but still accepts one high-MAE border case |
| P2 canonical C09 candidate | 2 | 63.83 | -24.0 | 87.47 | -24.0 | 0.00 | best alignment; strict bridge requirement |
| P3 counterexample guard | 2 | 63.83 | -24.0 | 87.47 | -24.0 | 0.00 | safest; 4B rows are overlay only |

## 14. Stage2 / Yellow / Green Comparison

- Positive C09 credit works when the trigger contains `verified equipment delivery`, `QA-to-revenue path`, or a credible process-equipment cycle bridge.
- Stage3-Yellow becomes dangerous when the only incremental evidence is advanced-equipment vocabulary plus relative strength.
- No Stage3-Green row is proposed in this loop. Green remains blocked without revenue/margin/revision durability.
- `green_lateness_ratio` is `not_applicable_no_confirmed_Stage3_Green_trigger` for all representative triggers.

## 15. 4B Local vs Full-window Timing Audit

| symbol | trigger | local/full 4B interpretation | MFE180 | MAE180 | audit verdict |
|---:|---|---|---:|---:|---|
| 083450 | Stage4B | AI cooling/chiller theme substituted for order bridge | 11.62 | -77.11 | valid local 4B watch; not positive Stage3 |
| 084370 | Stage4B | front-end equipment rally already priced | 12.78 | -43.05 | local/full-window 4B watch strengthened |

C09 4B is not a sell signal by itself. It is an overlay telling the state machine not to convert price-led advanced-equipment attention into a positive stage without non-price bridge evidence.

## 16. 4C Protection Audit

No hard 4C row is promoted in this loop. The observed failures are valuation/theme/bridge failures rather than confirmed legal, accounting, or thesis-break 4C events. `four_c_protection_label = not_applicable_no_hard_4c_trigger` for all rows.

## 17. Sector-Specific Rule Candidate

```yaml
rule_scope: sector_specific
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
rule_name: L2_advanced_equipment_theme_requires_bridge_before_Yellow
candidate: true
require_any_of:
  - verified_customer_order_or_delivery
  - order_to_revenue_conversion
  - mass_production_or_QA_to_mass_production_progress
  - margin_or_revision_bridge
route_to_watch_or_4B_if:
  - only_relative_strength
  - only_advanced_process_label
  - only_HBM_AI_theme_substitution
  - price_already_near_local_peak
```

## 18. Canonical-Archetype Rule Candidate

```yaml
rule_scope: canonical_archetype_specific
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
new_axis_proposed: C09_mass_production_order_revenue_margin_revision_bridge_required_before_Yellow_or_Green_plus_price_led_advanced_equipment_theme_to_4B_watch
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
```

## 19. Before / After Backtest Comparison

The candidate rule does not lower global thresholds. It changes eligibility. P0 allows too many theme/RS rows into positive stages; P2 allows only 036930 and 253590 as bridge-bearing C09 rows and routes the remaining five into Watch/4B overlay. This improves score-return alignment by removing cases with MFE180 under 15% and MAE180 worse than -40% from positive promotion.

## 20. Score-Return Alignment Matrix

| bucket | included symbols | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | interpretation |
|---|---|---:|---:|---:|---:|---|
| bridge-bearing positives | 036930, 253590 | 63.83 | -24.0 | 87.47 | -24.0 | positive but still not automatic Green |
| late theme / no bridge | 092870, 064290, 095610 | 9.11 | -49.52 | 9.11 | -57.3 | high drawdown, false-positive risk |
| 4B overlay rows | 083450, 084370 | 12.2 | -52.24 | 12.2 | -60.08 | do not promote; use as risk overlay |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE | 2 | 5 | 2 | 0 | 7 | 0 | 7 | 7 | 6 | true | true | index 10 -> local-session adjusted 23; need 7 to 30 / 27 to 50 |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 7
positive_case_count: 2
counterexample_count: 5
current_profile_error_count: 6
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - C09_late_Yellow_after_equipment_theme_runup
  - tester_or_inspection_label_without_mass_production_revenue_bridge
  - thermal_chiller_theme_substitution
  - front_end_equipment_beta_without_fresh_order_margin_revision_bridge
new_axis_proposed: C09_mass_production_order_revenue_margin_revision_bridge_required_before_Yellow_or_Green_plus_price_led_advanced_equipment_theme_to_4B_watch
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 7 new independent cases, 5 counterexamples, and 5 residual errors for R2/L2/C09.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- historical trigger-level calibration only
- stock-web tradable_raw OHLC windows
- C09-specific bridge/4B rule discovery
- shadow-only profile comparison

Non-validation scope:

- no live watchlist
- no current recommendation
- no brokerage API
- no production scoring patch
- no global threshold loosening

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C09_mass_production_order_revenue_margin_revision_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"Require verified order/revenue/margin/revision bridge before Yellow/Green; route price-led advanced-equipment labels to Watch/4B","P0 false positive 5/7; P2 removes false-positive promotion but keeps two positives","TRG-C09-L114-01-036930-2023-04-10|TRG-C09-L114-02-253590-2024-06-05|TRG-C09-L114-03-092870-2024-07-04|TRG-C09-L114-04-064290-2024-07-16|TRG-C09-L114-05-083450-2024-03-15|TRG-C09-L114-06-095610-2024-05-02|TRG-C09-L114-07-084370-2024-05-02",7,7,5,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C09_price_led_advanced_equipment_theme_to_4B_watch,sector_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"If evidence is price/theme/RS but order and margin bridge are missing, cap as Stage4B-Watch rather than positive Stage3","GST and Eugene Tech show 180D MAE -77.11 and -43.05 after local peak","TRG-C09-L114-05-083450-2024-03-15|TRG-C09-L114-07-084370-2024-05-02",2,2,2,medium,sector_shadow_only,"not production; strengthens local_4b_watch_guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","source_name":"FinanceData/marcap","tradable_row_count":14354401,"symbol_count":5414}
{"row_type":"case","case_id":"C09-L114-01","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C09-L114-01-036930-2023-04-10","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_bridge_pass","current_profile_verdict":"current_profile_missed_structural_if_blocked_completely","price_source":"Songdaiki/stock-web","notes":"new independent C09 symbol/trigger family in this session; not a C09 loop113 symbol-date duplicate"}
{"row_type":"case","case_id":"C09-L114-02","symbol":"253590","company_name":"네오셈","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-C09-L114-02-253590-2024-06-05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_bridge_pass","current_profile_verdict":"current_profile_correct_if_green_blocked","price_source":"Songdaiki/stock-web","notes":"new independent C09 symbol/trigger family in this session; not a C09 loop113 symbol-date duplicate"}
{"row_type":"case","case_id":"C09-L114-03","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","case_type":"counterexample","positive_or_counterexample":"counterexample","best_trigger":"TRG-C09-L114-03-092870-2024-07-04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_false_positive_late_yellow","price_source":"Songdaiki/stock-web","notes":"new independent C09 symbol/trigger family in this session; not a C09 loop113 symbol-date duplicate"}
{"row_type":"case","case_id":"C09-L114-04","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","case_type":"counterexample","positive_or_counterexample":"counterexample","best_trigger":"TRG-C09-L114-04-064290-2024-07-16","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new independent C09 symbol/trigger family in this session; not a C09 loop113 symbol-date duplicate"}
{"row_type":"case","case_id":"C09-L114-05","symbol":"083450","company_name":"GST","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","case_type":"stage4b_guardrail","positive_or_counterexample":"counterexample","best_trigger":"TRG-C09-L114-05-083450-2024-03-15","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_4B_too_late_if_treated_as_yellow","price_source":"Songdaiki/stock-web","notes":"new independent C09 symbol/trigger family in this session; not a C09 loop113 symbol-date duplicate"}
{"row_type":"case","case_id":"C09-L114-06","symbol":"095610","company_name":"테스","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","case_type":"counterexample","positive_or_counterexample":"counterexample","best_trigger":"TRG-C09-L114-06-095610-2024-05-02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new independent C09 symbol/trigger family in this session; not a C09 loop113 symbol-date duplicate"}
{"row_type":"case","case_id":"C09-L114-07","symbol":"084370","company_name":"유진테크","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","case_type":"stage4b_guardrail","positive_or_counterexample":"counterexample","best_trigger":"TRG-C09-L114-07-084370-2024-05-02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_4b_guardrail","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new independent C09 symbol/trigger family in this session; not a C09 loop113 symbol-date duplicate"}
{"row_type":"trigger","trigger_id":"TRG-C09-L114-01-036930-2023-04-10","case_id":"C09-L114-01","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-10","entry_date":"2023-04-10","entry_price":17130.0,"evidence_available_at_that_date":"memory production-cut cycle reset plus ALD/CVD advanced-node equipment beta. It is not direct equipment backlog, so C09 should cap at Actionable until order/margin bridge appears.","evidence_source":"public_memory_cycle_proxy:SAMSUNG_2023Q1_PRELIM_PRODUCTION_CUT; source_proxy_only=true","stage2_evidence_fields":["memory_cycle_recovery_proxy","advanced_ALD_CVD_equipment_beta","process_equipment_operating_leverage_optional"],"stage3_evidence_fields":["forward_price_validation_strong","advanced_node_tool_scarcity_proxy"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.34,"MFE_90D_pct":74.55,"MFE_180D_pct":121.83,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.78,"MAE_90D_pct":-13.78,"MAE_180D_pct":-13.78,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-15","peak_price":38000.0,"drawdown_after_peak_pct":-18.03,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"positive_structural_process_equipment_cycle_bridge_but_proxy_only","current_profile_verdict":"current_profile_missed_structural_if_blocked_completely","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_prior_stock_web_profile_check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|036930|Stage2-Actionable|2023-04-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"TRG-C09-L114-02-253590-2024-06-05","case_id":"C09-L114-02","symbol":"253590","company_name":"네오셈","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":11280.0,"evidence_available_at_that_date":"HBM burn-in tester delivery / QA-stage evidence creates a real bridge, but mass-production revenue visibility is still partial, so Green must remain blocked.","evidence_source":"https://www.thebell.co.kr/front/newsview.asp?key=202406050911561880105029","stage2_evidence_fields":["verified_HBM_tester_delivery","QA_stage_customer_route","tester_order_to_revenue_partial_bridge"],"stage3_evidence_fields":["direct_HBM_tester_route","strong_forward_MFE_but_high_MAE"],"stage4b_evidence_fields":["post_peak_high_MAE_guard_optional"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv","profile_path":"atlas/symbol_profiles/253/253590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.1,"MFE_90D_pct":53.1,"MFE_180D_pct":53.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.96,"MAE_90D_pct":-34.22,"MAE_180D_pct":-34.22,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-04","peak_price":17270.0,"drawdown_after_peak_pct":-57.04,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"positive_high_MAE_hbm_tester_delivery_bridge","current_profile_verdict":"current_profile_correct_if_green_blocked","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_prior_stock_web_profile_check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|253590|Stage2-Actionable|2024-06-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"trigger","trigger_id":"TRG-C09-L114-03-092870-2024-07-04","case_id":"C09-L114-03","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-04","entry_date":"2024-07-04","entry_price":22550.0,"evidence_available_at_that_date":"memory/CXL/HBM tester order-conversion vocabulary appeared after the local advance, but the realized path says late Yellow without revenue/margin bridge is C09 blowoff, not durable rerating.","evidence_source":"https://zdnet.co.kr/view/?no=20240704084503","stage2_evidence_fields":["tester_contract_or_order_proxy","memory_tester_route"],"stage3_evidence_fields":["late_relative_strength","advanced_tester_label"],"stage4b_evidence_fields":["late_entry_after_local_advance","MAE_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.53,"MFE_90D_pct":11.53,"MFE_180D_pct":11.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-50.11,"MAE_90D_pct":-56.59,"MAE_180D_pct":-62.71,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":25150.0,"drawdown_after_peak_pct":-66.56,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"counterexample_late_tester_yellow_without_margin_bridge","current_profile_verdict":"current_profile_false_positive_late_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_prior_stock_web_profile_check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|092870|Stage3-Yellow|2024-07-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"trigger","trigger_id":"TRG-C09-L114-04-064290-2024-07-16","case_id":"C09-L114-04","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-16","entry_date":"2024-07-16","entry_price":21600.0,"evidence_available_at_that_date":"HBM inspection-equipment expectation existed, but confirmed shipment/revenue bridge was insufficient at the trigger date. The price path collapsed almost immediately.","evidence_source":"https://www.dailyinvest.kr/news/articleView.html?idxno=59633","stage2_evidence_fields":["inspection_equipment_expectation","HBM_beneficiary_label"],"stage3_evidence_fields":["theme_RS_only","no_confirmed_revenue_bridge"],"stage4b_evidence_fields":["expectation_only_local_peak","MAE_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.39,"MFE_90D_pct":1.39,"MFE_180D_pct":1.39,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-31.44,"MAE_90D_pct":-57.31,"MAE_180D_pct":-63.06,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":21900.0,"drawdown_after_peak_pct":-63.56,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"counterexample_expectation_only_inspection_equipment","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_prior_stock_web_profile_check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|064290|Stage3-Yellow|2024-07-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"trigger","trigger_id":"TRG-C09-L114-05-083450-2024-03-15","case_id":"C09-L114-05","symbol":"083450","company_name":"GST","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":55100.0,"evidence_available_at_that_date":"AI cooling / chiller narrative substituted for verified equipment-order conversion. The case belongs in C09 as a price-and-theme blowoff guard, not a positive rerating row.","evidence_source":"https://v.daum.net/v/20240312102259830","stage2_evidence_fields":["AI_cooling_chiller_theme","semicap_infrastructure_label"],"stage3_evidence_fields":["local_RS_after_theme_rally"],"stage4b_evidence_fields":["price_only_blowoff","theme_substitution","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv","profile_path":"atlas/symbol_profiles/083/083450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.62,"MFE_90D_pct":11.62,"MFE_180D_pct":11.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.87,"MAE_90D_pct":-70.94,"MAE_180D_pct":-77.11,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-18","peak_price":61500.0,"drawdown_after_peak_pct":-79.5,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"local_4B_watch_valid_but_full_4B_requires_non_price_evidence","four_b_evidence_type":"price_only|positioning_overheat|valuation_blowoff","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"stage4b_theme_substitution_chiller_blowoff","current_profile_verdict":"current_profile_4B_too_late_if_treated_as_yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_prior_stock_web_profile_check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|083450|Stage4B|2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false}
{"row_type":"trigger","trigger_id":"TRG-C09-L114-06-095610-2024-05-02","case_id":"C09-L114-06","symbol":"095610","company_name":"테스","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":24300.0,"evidence_available_at_that_date":"memory capex recovery label and equipment beta existed, but fresh order backlog, margin, or revision bridge was absent at the trigger date.","evidence_source":"market_cycle_proxy:memory_capex_recovery; source_proxy_only=true","stage2_evidence_fields":["memory_equipment_cycle_beta","front_end_equipment_route"],"stage3_evidence_fields":["late_cycle_equipment_RS","no_fresh_order_margin_bridge"],"stage4b_evidence_fields":["valuation_positioning_overheat_optional"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.12,"MFE_90D_pct":14.4,"MFE_180D_pct":14.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.05,"MAE_90D_pct":-34.65,"MAE_180D_pct":-46.13,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":27800.0,"drawdown_after_peak_pct":-52.91,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":"not_applicable","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"counterexample_memory_capex_recovery_without_order_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_prior_stock_web_profile_check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|095610|Stage3-Yellow|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"TRG-C09-L114-07-084370-2024-05-02","case_id":"C09-L114-07","symbol":"084370","company_name":"유진테크","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_TESTER_INSPECTION_THERMAL_PROCESS_EQUIPMENT_PREMIUM_WITHOUT_MASS_PRODUCTION_BRIDGE","deep_sub_archetype_id":"C09_DEEP_HBM_TESTER_INSPECTION_CHILLER_ALD_CVD_ADVANCED_NODE_BLOWOFF_VS_ORDER_REVENUE_BRIDGE","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"advanced_equipment_valuation_blowoff","loop_objective":"coverage_gap_fill + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":53200.0,"evidence_available_at_that_date":"front-end memory-equipment recovery and advanced process vocabulary were already priced; without fresh non-price bridge this becomes local/full-window 4B watch.","evidence_source":"price_path_plus_positioning_proxy; source_proxy_only=true","stage2_evidence_fields":["memory_front_end_equipment_beta","advanced_process_tool_label"],"stage3_evidence_fields":["late_cycle_RS_after_fast_rally"],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff","margin_or_backlog_slowdown_unconfirmed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.78,"MFE_90D_pct":12.78,"MFE_180D_pct":12.78,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.22,"MAE_90D_pct":-33.55,"MAE_180D_pct":-43.05,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":60000.0,"drawdown_after_peak_pct":-49.5,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"local_4B_watch_valid_but_full_4B_requires_non_price_evidence","four_b_evidence_type":"price_only|positioning_overheat|valuation_blowoff","four_c_protection_label":"not_applicable_no_hard_4c_trigger","trigger_outcome_label":"stage4b_front_end_equipment_overheat_without_bridge","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_prior_stock_web_profile_check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|084370|Stage4B|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-L114-01","trigger_id":"TRG-C09-L114-01-036930-2023-04-10","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":50,"revision_score":55,"relative_strength_score":82,"customer_quality_score":58,"policy_or_regulatory_score":15,"valuation_repricing_score":62,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_before":63.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":58,"revision_score":55,"relative_strength_score":82,"customer_quality_score":58,"policy_or_regulatory_score":15,"valuation_repricing_score":54,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_after":64.5,"stage_label_after":"Stage2","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 candidate rule raises the burden for verified order/revenue/margin/revision bridge and routes late price-led advanced-equipment labels into Watch/4B instead of Yellow/Green.","MFE_90D_pct":74.55,"MAE_90D_pct":-13.78,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural_if_blocked_completely"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-L114-02","trigger_id":"TRG-C09-L114-02-253590-2024-06-05","symbol":"253590","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":58,"revision_score":55,"relative_strength_score":82,"customer_quality_score":70,"policy_or_regulatory_score":15,"valuation_repricing_score":62,"execution_risk_score":58,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_before":69.7,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":74,"backlog_visibility_score":62,"margin_bridge_score":66,"revision_score":55,"relative_strength_score":82,"customer_quality_score":70,"policy_or_regulatory_score":15,"valuation_repricing_score":54,"execution_risk_score":63,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_after":70.7,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 candidate rule raises the burden for verified order/revenue/margin/revision bridge and routes late price-led advanced-equipment labels into Watch/4B instead of Yellow/Green.","MFE_90D_pct":53.1,"MAE_90D_pct":-34.22,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct_if_green_blocked"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-L114-03","trigger_id":"TRG-C09-L114-03-092870-2024-07-04","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":82,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":52.1,"stage_label_before":"Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":90,"execution_risk_score":80,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":48.6,"stage_label_after":"Watch/Stage1.5","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 candidate rule raises the burden for verified order/revenue/margin/revision bridge and routes late price-led advanced-equipment labels into Watch/4B instead of Yellow/Green.","MFE_90D_pct":11.53,"MAE_90D_pct":-56.59,"score_return_alignment_label":"residual_error_counterexample","current_profile_verdict":"current_profile_false_positive_late_yellow"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-L114-04","trigger_id":"TRG-C09-L114-04-064290-2024-07-16","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":82,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":52.1,"stage_label_before":"Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":90,"execution_risk_score":80,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":48.6,"stage_label_after":"Watch/Stage1.5","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 candidate rule raises the burden for verified order/revenue/margin/revision bridge and routes late price-led advanced-equipment labels into Watch/4B instead of Yellow/Green.","MFE_90D_pct":1.39,"MAE_90D_pct":-57.31,"score_return_alignment_label":"residual_error_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-L114-05","trigger_id":"TRG-C09-L114-05-083450-2024-03-15","symbol":"083450","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":82,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":52.1,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":90,"execution_risk_score":80,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":48.6,"stage_label_after":"Stage4B-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 candidate rule raises the burden for verified order/revenue/margin/revision bridge and routes late price-led advanced-equipment labels into Watch/4B instead of Yellow/Green.","MFE_90D_pct":11.62,"MAE_90D_pct":-70.94,"score_return_alignment_label":"residual_error_counterexample","current_profile_verdict":"current_profile_4B_too_late_if_treated_as_yellow"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-L114-06","trigger_id":"TRG-C09-L114-06-095610-2024-05-02","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":82,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":52.1,"stage_label_before":"Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":90,"execution_risk_score":80,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":48.6,"stage_label_after":"Watch/Stage1.5","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 candidate rule raises the burden for verified order/revenue/margin/revision bridge and routes late price-led advanced-equipment labels into Watch/4B instead of Yellow/Green.","MFE_90D_pct":14.4,"MAE_90D_pct":-34.65,"score_return_alignment_label":"residual_error_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09-L114-07","trigger_id":"TRG-C09-L114-07-084370-2024-05-02","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":82,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":52.1,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":78,"customer_quality_score":52,"policy_or_regulatory_score":10,"valuation_repricing_score":90,"execution_risk_score":80,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":48.6,"stage_label_after":"Stage4B-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C09 candidate rule raises the burden for verified order/revenue/margin/revision bridge and routes late price-led advanced-equipment labels into Watch/4B instead of Yellow/Green.","MFE_90D_pct":12.78,"MAE_90D_pct":-33.55,"score_return_alignment_label":"residual_error_counterexample","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"profile_aggregate","profile_id":"P0","profile_scope":"current_calibrated_proxy","profile_hypothesis":"Current calibrated profile still over-credits C09 advanced equipment labels when bridge fields are absent.","changed_axes":[],"changed_thresholds":{"C09_yellow_bridge_required":false,"C09_green_revision_required":false},"eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":25.62,"avg_MAE_90D_pct":-43.01,"avg_MFE_180D_pct":32.38,"avg_MAE_180D_pct":-48.58,"false_positive_rate":0.71,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.0,"avg_four_b_full_window_peak_proximity":0.0,"score_return_alignment_verdict":"weak_alignment_high_drawdown"}
{"row_type":"profile_aggregate","profile_id":"P0b","profile_scope":"baseline_reference","profile_hypothesis":"Old baseline/reference has the same theme-beta vulnerability and is retained only for rollback comparison.","changed_axes":[],"changed_thresholds":{"C09_yellow_bridge_required":false,"C09_green_revision_required":false},"eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":25.62,"avg_MAE_90D_pct":-43.01,"avg_MFE_180D_pct":32.38,"avg_MAE_180D_pct":-48.58,"false_positive_rate":0.71,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.0,"avg_four_b_full_window_peak_proximity":0.0,"score_return_alignment_verdict":"weak_alignment_high_drawdown"}
{"row_type":"profile_aggregate","profile_id":"P1","profile_scope":"sector_specific_candidate_profile","profile_hypothesis":"L2 equipment names require order/revenue/margin bridge before Yellow and keep price-led advanced-equipment rallies as 4B watch.","changed_axes":["C09_verified_order_revenue_margin_revision_bridge_required","C09_price_only_local_blowoff_to_4B_watch"],"changed_thresholds":{"C09_yellow_bridge_required":true,"C09_green_revision_required":false},"eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":46.39,"avg_MAE_90D_pct":-34.86,"avg_MFE_180D_pct":62.15,"avg_MAE_180D_pct":-36.9,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.0,"avg_four_b_full_window_peak_proximity":0.0,"score_return_alignment_verdict":"improves_alignment"}
{"row_type":"profile_aggregate","profile_id":"P2","profile_scope":"canonical_archetype_candidate_profile","profile_hypothesis":"C09-specific profile allows positive credit only for verified tester/equipment delivery or structural process-equipment bridge.","changed_axes":["C09_verified_order_revenue_margin_revision_bridge_required","C09_price_only_local_blowoff_to_4B_watch"],"changed_thresholds":{"C09_yellow_bridge_required":true,"C09_green_revision_required":true},"eligible_trigger_count":2,"selected_entry_trigger_per_case":2,"avg_MFE_90D_pct":63.83,"avg_MAE_90D_pct":-24.0,"avg_MFE_180D_pct":87.47,"avg_MAE_180D_pct":-24.0,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.0,"avg_four_b_full_window_peak_proximity":0.0,"score_return_alignment_verdict":"improves_alignment"}
{"row_type":"profile_aggregate","profile_id":"P3","profile_scope":"counterexample_guard_profile","profile_hypothesis":"Guard profile excludes Stage4B/price-only rows from promotion and uses them only as risk overlays.","changed_axes":["C09_verified_order_revenue_margin_revision_bridge_required","C09_price_only_local_blowoff_to_4B_watch"],"changed_thresholds":{"C09_yellow_bridge_required":true,"C09_green_revision_required":true},"eligible_trigger_count":2,"selected_entry_trigger_per_case":2,"avg_MFE_90D_pct":63.83,"avg_MAE_90D_pct":-24.0,"avg_MFE_180D_pct":87.47,"avg_MAE_180D_pct":-24.0,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.0,"avg_four_b_full_window_peak_proximity":0.0,"score_return_alignment_verdict":"improves_alignment"}
{"row_type":"residual_contribution","round":"R2","loop":"114","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"new_trigger_family_count":7,"positive_case_count":2,"counterexample_count":5,"current_profile_error_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["C09_late_Yellow_after_equipment_theme_runup","tester_or_inspection_label_without_mass_production_revenue_bridge","thermal_chiller_theme_substitution","front_end_equipment_beta_without_fresh_order_margin_revision_bridge"],"new_axis_proposed":"C09_mass_production_order_revenue_margin_revision_bridge_required_before_Yellow_or_Green_plus_price_led_advanced_equipment_theme_to_4B_watch","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_weakened":null,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"diversity_score_summary":"new C09 symbols 7 / representative triggers 7 / positive-counterexample balance 2:5 / Stage4B overlays 2 / source_proxy_only 3","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

Self-audit note: every `row_type="trigger"` row uses canonical trigger labels, includes `entry_date`, `entry_price`, `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`, `same_entry_group_id`, `dedupe_for_aggregate`, `aggregate_group_role`, and the required Stock-Web price fields. No trigger row is missing the 30/90/180D path fields required by the v12 batch ingest gate.

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
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

```yaml
completed_round: R2
completed_loop: 114
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
next_recommended_archetypes:
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- `MAIN_EXECUTION_PROMPT`: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- `NO_REPEAT_INDEX`: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- `STOCK_WEB_MANIFEST`: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- `DOCS_ROUND_TREE`: https://github.com/Songdaiki/stock_agent/tree/main/docs/round
- This loop uses only historical calibration language. It contains no live recommendation or automated trading instruction.
