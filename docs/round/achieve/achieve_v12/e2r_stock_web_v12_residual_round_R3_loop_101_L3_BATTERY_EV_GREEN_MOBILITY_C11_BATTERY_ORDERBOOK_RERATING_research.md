---
report_type: e2r_stock_web_v12_residual_research
selected_round: R3
selected_loop: 101
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: mixed_C11_orderbook_margin_fcf_conversion_set
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
standard_filename: e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
---

# E2R stock-web v12 residual round — R3 loop 101 / L3_BATTERY_EV_GREEN_MOBILITY / C11_BATTERY_ORDERBOOK_RERATING

## 0. Execution posture

This standalone research note follows `e2r_v12_prompt_round_scheduler_corrected.txt` as a historical calibration artifact. It does **not** patch `stock_agent` code or production scoring. `V12_Research_No_Repeat_Index.md` is used only as a duplicate-avoidance and coverage ledger.

Selected canonical is `C11_BATTERY_ORDERBOOK_RERATING`, because the ledger shows the archetype remains below the 30-row minimum coverage target. The loop is assigned as `R3_loop_101` after the existing C11 R3 compact history reached loop 100; this file uses the standard long ingest filename.

## 1. Round and sector coordinates

```yaml
selected_round: R3
selected_loop: 101
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: mixed_C11_orderbook_margin_fcf_conversion_set
loop_objective: coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
previous_index_rows_for_canonical: 18
expected_rows_after_acceptance: 23
```

## 2. Canonical hypothesis

`C11_BATTERY_ORDERBOOK_RERATING` should not promote a company only because a large contract headline exists. The proposed split is:

1. **Named customer + multi-year volume + capacity/localization route** can unlock Stage2-Actionable and sometimes Stage3-Yellow.
2. **Stage3-Green should require margin/FCF pass-through**, utilization, ASP stability, or repeat quarterly confirmation.
3. **Large orderbook + weak margin bridge + high-MAE path** should activate 4B watch even when MFE is initially attractive.
4. Cathode, electrolyte, separator, and copper foil orderbooks need different contamination checks: cathode ASP/lithium lag, electrolyte localization/customer lock-in, separator utilization, and copper foil spread/utilization.

## 3. Case set summary

| Symbol | Company | Trigger type | Entry date | Entry price | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | Role |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 003670 | 포스코퓨처엠 | Stage3-Yellow | 2023-02-15 | 229,000 | 21.40% | -7.64% | 84.50% | -7.64% | 203.06% | -7.64% | positive |
| 348370 | 엔켐 | Stage2-Actionable | 2023-09-12 | 62,300 | 2.25% | -17.34% | 128.25% | -20.87% | 533.23% | -20.87% | positive |
| 066970 | 엘앤에프 | Stage4B | 2023-02-28 | 262,000 | 33.40% | -16.41% | 33.40% | -16.41% | 33.40% | -51.18% | counterexample |
| 393890 | 더블유씨피 | Stage4B | 2023-08-02 | 79,000 | 6.96% | -29.75% | 6.96% | -51.52% | 6.96% | -62.15% | counterexample |
| 011790 | SKC | Stage2-Actionable | 2023-02-20 | 97,300 | 24.36% | -7.30% | 25.69% | -7.30% | 25.69% | -30.11% | counterexample |

Aggregate 90D path: average MFE `55.76%`, average MAE `-20.75%`. Aggregate 180D path: average MFE `160.47%`, average MAE `-34.39%`.

## 4. Evidence map

| Symbol | Company | Fine archetype | Evidence interpretation | Source |
|---|---|---|---|---|
| 003670 | 포스코퓨처엠 | C11_CATHODE_NAMED_CUSTOMER_MULTI_YEAR_CONTRACT | 10-year KRW 40T high-nickel cathode supply contract with Samsung SDI; orderbook quality is named customer and duration-backed, but Green should still require margin/FCF conversion confirmation. | https://newsroom.posco.com/en/posco-chemical-lands-40-trillion-krw-cathode-materials-supply-contract-for-samsung-sdis-batteries/ |
| 348370 | 엔켐 | C11_ELECTROLYTE_US_LOCALIZATION_CUSTOMER_PIPELINE | US localization/capacity expansion and top-tier customer pipeline pointed to orderbook conversion optionality; the early drawdown was large, but the 90D/180D path shows a missed structural rerating if the model waited for clean quarterly margin proof only. | https://www.asiae.co.kr/en/article/2023091208380574442 |
| 066970 | 엘앤에프 | C11_CATHODE_ORDERBOOK_HIGH_MAE_FALSE_GREEN | Large Tesla cathode supply contract created an apparent orderbook rerating, but the 180D path shows large adverse excursion; contract value without margin/FCF pass-through should cap Stage3 and activate 4B watch after fast MFE. | https://www.kedglobal.com/batteries/newsView/ked202302280017 |
| 393890 | 더블유씨피 | C11_SEPARATOR_SUPPLY_CONTRACT_DEMAND_SLOWDOWN_COUNTEREXAMPLE | Multi-year Samsung SDI separator supply route looked like backlog visibility, but the forward path had very low MFE and deep 90D/180D MAE; separator orderbook must be gated by utilization, ASP, and margin conversion. | https://www.thelec.net/news/articleView.html?idxno=4607 |
| 011790 | SKC | C11_COPPER_FOIL_ORDERBOOK_SPREAD_UTILIZATION_CAP | SK nexilis signed a mid/long-term Northvolt copper foil contract; the price path had tradable MFE but a deeper 180D drawdown, showing copper foil orderbook needs spread/utilization and balance-sheet risk gates before Stage3. | https://www.skc.kr/m/eng/Conmmunication/pr/newsDetail.do?gubun=&seq=1511 |

## 5. Positive cases

### 5.1 POSCO Future M / 003670

A 10-year KRW 40T cathode supply contract with Samsung SDI is a clean named-customer orderbook signal. The 180D MFE of `203.06%` confirms that the orderbook signal was not just a headline. However, the post-peak drawdown of `-66.64%` also says Stage3-Green should not be permanent without margin/FCF follow-through. This case supports Stage3-Yellow/Green unlocking, but it strengthens a post-rerating 4B watch.

### 5.2 Enchem / 348370

The September 2023 localization/capacity/customer-pipeline signal had weak early price confirmation: 30D MFE was only `2.25%` and 30D MAE was `-17.34%`. But the 90D and 180D paths were `128.25%` and `533.23%`. This is a missed-structural case if the profile waits too long for reported quarterly margin before allowing Stage2-Actionable.

## 6. Counterexamples and 4B watch cases

### 6.1 L&F / 066970

The Tesla cathode contract created an apparent large-orderbook rerating. The first 30D MFE was `33.40%`, but full-window MAE reached `-51.18%`. This is the canonical warning: contract value alone can create tradable MFE but still fail as a durable Stage3 signal when margin/FCF conversion is not proven.

### 6.2 WCP / 393890

The Samsung SDI separator supply route produced only `6.96%` MFE while 90D/180D MAE reached `-51.52%` and `-62.15%`. This is a strong false-positive counterexample for separator orderbook headlines without utilization and profitability confirmation.

### 6.3 SKC / 011790

SK nexilis' Northvolt copper foil contract generated a tradable 90D MFE of `25.69%`, but the 180D MAE of `-30.11%` and post-peak drawdown of `-44.40%` show that copper foil supply contracts need spread/utilization gates before Stage3.

## 7. Current profile stress test

| Symbol | Before rule score | Before stage | After rule score | After stage | Interpretation |
|---|---:|---|---:|---|---|
| 003670 | 82 | Stage3-Yellow | 86 | Stage3-Yellow | Correct positive, Green withheld until margin/FCF confirmation |
| 348370 | 64 | Stage2 | 76 | Stage2-Actionable | Missed structural if localization/customer pipeline is underweighted |
| 066970 | 86 | Stage3-Yellow | 68 | Stage4B | False positive reduced by high-MAE and margin bridge cap |
| 393890 | 78 | Stage3-Yellow | 55 | Stage4B | Separator headline capped by utilization/profitability gate |
| 011790 | 76 | Stage3-Yellow | 63 | Stage2-Actionable | Copper foil orderbook remains actionable but not Stage3 |

## 8. Proposed residual rule candidate

```yaml
sector_specific_rule_candidate: L3_C11_ORDERBOOK_MARGIN_FCF_CONVERSION_AND_HIGH_MAE_SPLIT
canonical_archetype_rule_candidate: C11_ORDERBOOK_REQUIRES_CUSTOMER_QUALITY_MARGIN_FCF_BRIDGE_WITH_HIGH_MAE_CAP
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed:
  - C11_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_GATE
  - C11_HIGH_MAE_ORDERBOOK_4B_CAP
  - C11_CUSTOMER_NAMED_ORDERBOOK_WITH_CAPACITY_LOCALIZATION_UNLOCK
existing_axis_strengthened:
  - stage2_required_bridge
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
```

Rule draft:

```text
For C11, large orderbook value is not enough for Stage3-Green.
Stage2-Actionable can be unlocked by named customer + contract duration + capacity/localization route.
Stage3-Yellow requires customer quality plus credible backlog conversion path.
Stage3-Green requires margin/FCF pass-through, utilization, ASP stability, or repeated quarterly confirmation.
If MFE is fast but 90D/180D MAE exceeds -30% without margin bridge confirmation, route to 4B watch rather than persistent Stage3.
```

## 9. Price-source validation

All selected trigger rows use `Songdaiki/stock-web` tradable OHLCV shards. Price basis is `tradable_raw`; price adjustment status is `raw_unadjusted_marcap`. Each selected row has at least 180 forward tradable rows before the stock-web manifest max date of `2026-02-20`. A simple share-count discontinuity scan on selected 180D windows did not identify a corporate-action contamination flag.

## 10. Machine-readable case rows

```jsonl
{"row_type": "case", "case_id": "C11_003670_POSCO_FUTURE_M_20230215_SAMSUNG_SDI_CATHODE_10Y_CONTRACT", "symbol": "003670", "company_name": "POSCO Future M", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_CATHODE_NAMED_CUSTOMER_MULTI_YEAR_CONTRACT", "case_role": "positive", "trigger_count": 1, "calibration_usable": true, "representative_trigger_id": "C11_003670_20230215_Stage3-Yellow", "new_symbol_for_this_loop": true, "new_trigger_family_for_this_loop": true, "residual_error_type": "profile_correct_with_4B_watch", "case_summary": "10-year KRW 40T high-nickel cathode supply contract with Samsung SDI; orderbook quality is named customer and duration-backed, but Green should still require margin/FCF conversion confirmation."}
{"row_type": "case", "case_id": "C11_348370_ENCHEM_20230912_US_ELECTROLYTE_LOCALIZATION_CAPACITY", "symbol": "348370", "company_name": "Enchem", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_ELECTROLYTE_US_LOCALIZATION_CUSTOMER_PIPELINE", "case_role": "positive", "trigger_count": 1, "calibration_usable": true, "representative_trigger_id": "C11_348370_20230912_Stage2-Actionable", "new_symbol_for_this_loop": true, "new_trigger_family_for_this_loop": true, "residual_error_type": "missed_structural", "case_summary": "US localization/capacity expansion and top-tier customer pipeline pointed to orderbook conversion optionality; the early drawdown was large, but the 90D/180D path shows a missed structural rerating if the model waited for clean quarterly margin proof only."}
{"row_type": "case", "case_id": "C11_066970_LNF_20230228_TESLA_CATHODE_ORDERBOOK_HIGH_MAE", "symbol": "066970", "company_name": "L&F", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_CATHODE_ORDERBOOK_HIGH_MAE_FALSE_GREEN", "case_role": "counterexample", "trigger_count": 1, "calibration_usable": true, "representative_trigger_id": "C11_066970_20230228_Stage4B", "new_symbol_for_this_loop": true, "new_trigger_family_for_this_loop": true, "residual_error_type": "false_positive_or_late_4B", "case_summary": "Large Tesla cathode supply contract created an apparent orderbook rerating, but the 180D path shows large adverse excursion; contract value without margin/FCF pass-through should cap Stage3 and activate 4B watch after fast MFE."}
{"row_type": "case", "case_id": "C11_393890_WCP_20230802_SAMSUNG_SDI_SEPARATOR_SUPPLY_HIGH_MAE", "symbol": "393890", "company_name": "WCP", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_SEPARATOR_SUPPLY_CONTRACT_DEMAND_SLOWDOWN_COUNTEREXAMPLE", "case_role": "counterexample", "trigger_count": 1, "calibration_usable": true, "representative_trigger_id": "C11_393890_20230802_Stage4B", "new_symbol_for_this_loop": true, "new_trigger_family_for_this_loop": true, "residual_error_type": "false_positive_or_late_4B", "case_summary": "Multi-year Samsung SDI separator supply route looked like backlog visibility, but the forward path had very low MFE and deep 90D/180D MAE; separator orderbook must be gated by utilization, ASP, and margin conversion."}
{"row_type": "case", "case_id": "C11_011790_SKC_20230220_NORTHVOLT_COPPER_FOIL_ORDERBOOK_MARGIN_RISK", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_COPPER_FOIL_ORDERBOOK_SPREAD_UTILIZATION_CAP", "case_role": "counterexample", "trigger_count": 1, "calibration_usable": true, "representative_trigger_id": "C11_011790_20230220_Stage2-Actionable", "new_symbol_for_this_loop": true, "new_trigger_family_for_this_loop": true, "residual_error_type": "false_positive_or_late_4B", "case_summary": "SK nexilis signed a mid/long-term Northvolt copper foil contract; the price path had tradable MFE but a deeper 180D drawdown, showing copper foil orderbook needs spread/utilization and balance-sheet risk gates before Stage3."}
```

## 11. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "C11_003670_20230215_Stage3-Yellow", "case_id": "C11_003670_POSCO_FUTURE_M_20230215_SAMSUNG_SDI_CATHODE_10Y_CONTRACT", "symbol": "003670", "company_name": "POSCO Future M", "company_name_kr": "포스코퓨처엠", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_CATHODE_NAMED_CUSTOMER_MULTI_YEAR_CONTRACT", "sector": "battery_materials_cathode", "primary_archetype": "named_customer_multi_year_cathode_orderbook_margin_bridge", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-02-15", "evidence_available_at_that_date": "2023-02-15T09:00:00+09:00", "evidence_source": "https://newsroom.posco.com/en/posco-chemical-lands-40-trillion-krw-cathode-materials-supply-contract-for-samsung-sdis-batteries/", "evidence_summary": "10-year KRW 40T high-nickel cathode supply contract with Samsung SDI; orderbook quality is named customer and duration-backed, but Green should still require margin/FCF conversion confirmation.", "stage2_evidence_fields": ["named_customer_orderbook", "multi_year_contract", "large_contract_value", "battery_supply_chain_capacity_route"], "stage3_evidence_fields": ["customer_quality", "backlog_visibility", "orderbook_size", "volume_route_visible"], "stage4b_evidence_fields": ["later_full_window_peak_drawdown_requires_4B_watch_after_fast_rerating"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-15", "entry_price": 229000.0, "MFE_30D_pct": 21.4, "MFE_90D_pct": 84.5, "MFE_180D_pct": 203.06, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.64, "MAE_90D_pct": -7.64, "MAE_180D_pct": -7.64, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000.0, "drawdown_after_peak_pct": -66.64, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_full_window_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_timing_verdict": "not_initial_4B; post_peak_4B_watch_needed", "four_b_evidence_type": "orderbook_event_cap|margin_FCF_bridge_unconfirmed|high_MAE_guardrail", "four_c_protection_label": "none", "trigger_outcome_label": "positive_structural_orderbook_with_late_4B_drawdown_watch", "current_profile_verdict": "profile_correct_if_green_requires_margin_bridge_not_contract_size_only", "calibration_usable": true, "forward_window_trading_days": 459, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_share_discontinuity_detected_in_180D_window", "same_entry_group_id": "C11_BATTERY_ORDERBOOK_RERATING|003670|Stage3-Yellow|2023-02-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C11_348370_20230912_Stage2-Actionable", "case_id": "C11_348370_ENCHEM_20230912_US_ELECTROLYTE_LOCALIZATION_CAPACITY", "symbol": "348370", "company_name": "Enchem", "company_name_kr": "엔켐", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_ELECTROLYTE_US_LOCALIZATION_CUSTOMER_PIPELINE", "sector": "battery_materials_electrolyte", "primary_archetype": "electrolyte_us_localization_capacity_customer_pipeline", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-09-12", "evidence_available_at_that_date": "2023-09-12T09:00:00+09:00", "evidence_source": "https://www.asiae.co.kr/en/article/2023091208380574442", "evidence_summary": "US localization/capacity expansion and top-tier customer pipeline pointed to orderbook conversion optionality; the early drawdown was large, but the 90D/180D path shows a missed structural rerating if the model waited for clean quarterly margin proof only.", "stage2_evidence_fields": ["US_localization_capacity", "customer_pipeline", "battery_electrolyte_demand_route", "capacity_expansion_visible"], "stage3_evidence_fields": ["customer_quality_partial", "capacity_visibility", "localized_supply_chain_optional_orderbook"], "stage4b_evidence_fields": ["early_MAE_exceeds_20pct_requires_position_sizing_or_Stage2_not_Green"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2023.csv", "profile_path": "atlas/symbol_profiles/348/348370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-12", "entry_price": 62300.0, "MFE_30D_pct": 2.25, "MFE_90D_pct": 128.25, "MFE_180D_pct": 533.23, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.34, "MAE_90D_pct": -20.87, "MAE_180D_pct": -20.87, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 394500.0, "drawdown_after_peak_pct": -36.25, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_full_window_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_timing_verdict": "Stage2_Actionable_allowed_but_Green_blocked_until_margin_FCF", "four_b_evidence_type": "orderbook_event_cap|margin_FCF_bridge_unconfirmed|high_MAE_guardrail", "four_c_protection_label": "none", "trigger_outcome_label": "positive_missed_structural_after_high_initial_MAE", "current_profile_verdict": "current_profile_too_late_if_it_requires_reported_margin_before_Stage2_Actionable", "calibration_usable": true, "forward_window_trading_days": 315, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_share_discontinuity_detected_in_180D_window", "same_entry_group_id": "C11_BATTERY_ORDERBOOK_RERATING|348370|Stage2-Actionable|2023-09-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C11_066970_20230228_Stage4B", "case_id": "C11_066970_LNF_20230228_TESLA_CATHODE_ORDERBOOK_HIGH_MAE", "symbol": "066970", "company_name": "L&F", "company_name_kr": "엘앤에프", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_CATHODE_ORDERBOOK_HIGH_MAE_FALSE_GREEN", "sector": "battery_materials_cathode", "primary_archetype": "large_customer_orderbook_without_margin_fcf_conversion", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2023-02-28", "evidence_available_at_that_date": "2023-02-28T09:00:00+09:00", "evidence_source": "https://www.kedglobal.com/batteries/newsView/ked202302280017", "evidence_summary": "Large Tesla cathode supply contract created an apparent orderbook rerating, but the 180D path shows large adverse excursion; contract value without margin/FCF pass-through should cap Stage3 and activate 4B watch after fast MFE.", "stage2_evidence_fields": ["large_named_customer_contract", "cathode_orderbook", "battery_materials_volume_route"], "stage3_evidence_fields": ["customer_quality_visible", "backlog_visibility_partial"], "stage4b_evidence_fields": ["high_theme_rerating_after_large_contract", "margin_FCF_bridge_unproven", "MFE33pct_then_MAE51pct"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-28", "entry_price": 262000.0, "MFE_30D_pct": 33.4, "MFE_90D_pct": 33.4, "MFE_180D_pct": 33.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.41, "MAE_90D_pct": -16.41, "MAE_180D_pct": -51.18, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-03", "peak_price": 349500.0, "drawdown_after_peak_pct": -63.4, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_full_window_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_timing_verdict": "should_route_to_Stage4B_watch_after_fast_contract_rerating", "four_b_evidence_type": "orderbook_event_cap|margin_FCF_bridge_unconfirmed|high_MAE_guardrail", "four_c_protection_label": "none", "trigger_outcome_label": "counterexample_large_orderbook_false_green_high_MAE", "current_profile_verdict": "current_profile_false_positive_if_contract_value_overweights_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 450, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_share_discontinuity_detected_in_180D_window", "same_entry_group_id": "C11_BATTERY_ORDERBOOK_RERATING|066970|Stage4B|2023-02-28", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C11_393890_20230802_Stage4B", "case_id": "C11_393890_WCP_20230802_SAMSUNG_SDI_SEPARATOR_SUPPLY_HIGH_MAE", "symbol": "393890", "company_name": "WCP", "company_name_kr": "더블유씨피", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_SEPARATOR_SUPPLY_CONTRACT_DEMAND_SLOWDOWN_COUNTEREXAMPLE", "sector": "battery_materials_separator", "primary_archetype": "separator_supply_contract_without_profit_conversion", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2023-08-02", "evidence_available_at_that_date": "2023-08-02T09:00:00+09:00", "evidence_source": "https://www.thelec.net/news/articleView.html?idxno=4607", "evidence_summary": "Multi-year Samsung SDI separator supply route looked like backlog visibility, but the forward path had very low MFE and deep 90D/180D MAE; separator orderbook must be gated by utilization, ASP, and margin conversion.", "stage2_evidence_fields": ["customer_supply_route", "separator_orderbook", "multi_year_volume_route"], "stage3_evidence_fields": ["backlog_visibility_partial"], "stage4b_evidence_fields": ["low_MFE_deep_MAE", "demand_slowdown_utilization_risk", "margin_conversion_unconfirmed"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-02", "entry_price": 79000.0, "MFE_30D_pct": 6.96, "MFE_90D_pct": 6.96, "MFE_180D_pct": 6.96, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -29.75, "MAE_90D_pct": -51.52, "MAE_180D_pct": -62.15, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-02", "peak_price": 84500.0, "drawdown_after_peak_pct": -64.62, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_full_window_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_timing_verdict": "initial_Stage4B_or_Stage2_block_preferred_over_Stage3", "four_b_evidence_type": "orderbook_event_cap|margin_FCF_bridge_unconfirmed|high_MAE_guardrail", "four_c_protection_label": "none", "trigger_outcome_label": "counterexample_orderbook_without_margin_conversion", "current_profile_verdict": "current_profile_false_positive_if_separator_supply_news_promotes_Stage3", "calibration_usable": true, "forward_window_trading_days": 344, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_share_discontinuity_detected_in_180D_window", "same_entry_group_id": "C11_BATTERY_ORDERBOOK_RERATING|393890|Stage4B|2023-08-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C11_011790_20230220_Stage2-Actionable", "case_id": "C11_011790_SKC_20230220_NORTHVOLT_COPPER_FOIL_ORDERBOOK_MARGIN_RISK", "symbol": "011790", "company_name": "SKC", "company_name_kr": "SKC", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "C11_COPPER_FOIL_ORDERBOOK_SPREAD_UTILIZATION_CAP", "sector": "battery_materials_copper_foil", "primary_archetype": "copper_foil_supply_contract_spread_utilization_risk", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-20", "evidence_available_at_that_date": "2023-02-20T09:00:00+09:00", "evidence_source": "https://www.skc.kr/m/eng/Conmmunication/pr/newsDetail.do?gubun=&seq=1511", "evidence_summary": "SK nexilis signed a mid/long-term Northvolt copper foil contract; the price path had tradable MFE but a deeper 180D drawdown, showing copper foil orderbook needs spread/utilization and balance-sheet risk gates before Stage3.", "stage2_evidence_fields": ["mid_long_term_supply_contract", "named_customer", "copper_foil_orderbook", "European_battery_supply_chain"], "stage3_evidence_fields": ["customer_quality_partial", "backlog_visibility_partial"], "stage4b_evidence_fields": ["spread_utilization_uncertainty", "MFE25pct_then_MAE30pct", "not_full_Stage3_without_margin_bridge"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv", "profile_path": "atlas/symbol_profiles/011/011790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-20", "entry_price": 97300.0, "MFE_30D_pct": 24.36, "MFE_90D_pct": 25.69, "MFE_180D_pct": 25.69, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.3, "MAE_90D_pct": -7.3, "MAE_180D_pct": -30.11, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-05", "peak_price": 122300.0, "drawdown_after_peak_pct": -44.4, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_full_window_peak_proximity": "not_computed_no_prior_Stage2_anchor_in_same_loop", "four_b_timing_verdict": "Stage2_Actionable_with_4B_watch_after_fast_MFE", "four_b_evidence_type": "orderbook_event_cap|margin_FCF_bridge_unconfirmed|high_MAE_guardrail", "four_c_protection_label": "none", "trigger_outcome_label": "counterexample_stage2_actionable_but_not_stage3_without_spread_margin", "current_profile_verdict": "current_profile_too_generous_if_named_supply_contract_counts_as_full_orderbook_quality", "calibration_usable": true, "forward_window_trading_days": 456, "calibration_block_reasons": [], "corporate_action_window_status": "clean_no_share_discontinuity_detected_in_180D_window", "same_entry_group_id": "C11_BATTERY_ORDERBOOK_RERATING|011790|Stage2-Actionable|2023-02-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

## 12. Price source validation rows

```jsonl
{"row_type": "price_source_validation", "price_data_repo": "Songdaiki/stock-web", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "usable_rule": "180 forward tradable rows present and no detected 180D corporate action share discontinuity in selected windows", "selected_case_count": 5, "calibration_usable_rows": 5, "MFE_MAE_method": "MFE_N_pct=max(high from entry_date through N tradable rows)/entry_price-1; MAE_N_pct=min(low from entry_date through N tradable rows)/entry_price-1"}
```

## 13. Score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "C11_003670_POSCO_FUTURE_M_20230215_SAMSUNG_SDI_CATHODE_10Y_CONTRACT", "symbol": "003670", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "before_rule_total_score": 82, "after_rule_total_score": 86, "before_rule_stage": "Stage3-Yellow", "after_rule_stage": "Stage3-Yellow", "rule_candidate": "C11_ORDERBOOK_REQUIRES_CUSTOMER_QUALITY_MARGIN_FCF_BRIDGE_WITH_HIGH_MAE_CAP", "rationale": "contract_quality_high_but_Green_requires_margin_FCF_confirmation", "not_production_patch": true}
{"row_type": "score_simulation", "case_id": "C11_348370_ENCHEM_20230912_US_ELECTROLYTE_LOCALIZATION_CAPACITY", "symbol": "348370", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "before_rule_total_score": 64, "after_rule_total_score": 76, "before_rule_stage": "Stage2", "after_rule_stage": "Stage2-Actionable", "rule_candidate": "C11_ORDERBOOK_REQUIRES_CUSTOMER_QUALITY_MARGIN_FCF_BRIDGE_WITH_HIGH_MAE_CAP", "rationale": "localization_capacity_pipeline_should_unlock_actionable_watch", "not_production_patch": true}
{"row_type": "score_simulation", "case_id": "C11_066970_LNF_20230228_TESLA_CATHODE_ORDERBOOK_HIGH_MAE", "symbol": "066970", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "before_rule_total_score": 86, "after_rule_total_score": 68, "before_rule_stage": "Stage3-Yellow", "after_rule_stage": "Stage4B", "rule_candidate": "C11_ORDERBOOK_REQUIRES_CUSTOMER_QUALITY_MARGIN_FCF_BRIDGE_WITH_HIGH_MAE_CAP", "rationale": "contract_value_overweight_reduced_by_margin_FCF_and_high_MAE_cap", "not_production_patch": true}
{"row_type": "score_simulation", "case_id": "C11_393890_WCP_20230802_SAMSUNG_SDI_SEPARATOR_SUPPLY_HIGH_MAE", "symbol": "393890", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "before_rule_total_score": 78, "after_rule_total_score": 55, "before_rule_stage": "Stage3-Yellow", "after_rule_stage": "Stage4B", "rule_candidate": "C11_ORDERBOOK_REQUIRES_CUSTOMER_QUALITY_MARGIN_FCF_BRIDGE_WITH_HIGH_MAE_CAP", "rationale": "separator_supply_news_downweighted_by_utilization_and_MAE_gate", "not_production_patch": true}
{"row_type": "score_simulation", "case_id": "C11_011790_SKC_20230220_NORTHVOLT_COPPER_FOIL_ORDERBOOK_MARGIN_RISK", "symbol": "011790", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "before_rule_total_score": 76, "after_rule_total_score": 63, "before_rule_stage": "Stage3-Yellow", "after_rule_stage": "Stage2-Actionable", "rule_candidate": "C11_ORDERBOOK_REQUIRES_CUSTOMER_QUALITY_MARGIN_FCF_BRIDGE_WITH_HIGH_MAE_CAP", "rationale": "copper_foil_orderbook_capped_until_spread_utilization_bridge", "not_production_patch": true}
```

## 14. Residual contribution rows

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 101, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "selected_priority_bucket": "Priority 0 / under 30 rows", "previous_index_rows": 18, "new_representative_rows": 5, "expected_rows_after_acceptance": 23, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 4, "average_MFE_90D_pct": 55.76, "average_MAE_90D_pct": -20.75, "average_MFE_180D_pct": 160.47, "average_MAE_180D_pct": -34.39, "sector_specific_rule_candidate": "L3_C11_ORDERBOOK_MARGIN_FCF_CONVERSION_AND_HIGH_MAE_SPLIT", "canonical_archetype_rule_candidate": "C11_ORDERBOOK_REQUIRES_CUSTOMER_QUALITY_MARGIN_FCF_BRIDGE_WITH_HIGH_MAE_CAP", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": ["C11_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_GATE", "C11_HIGH_MAE_ORDERBOOK_4B_CAP", "C11_CUSTOMER_NAMED_ORDERBOOK_WITH_CAPACITY_LOCALIZATION_UNLOCK"], "existing_axis_strengthened": ["stage2_required_bridge", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": null, "do_not_propose_new_weight_delta": false}
```

## 15. Batch ingest self-audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 16. Deferred coding-agent handoff prompt

```text
Do not execute during research. Later, after this Markdown is placed under docs/round, run the v12 calibration ingestion pipeline and verify that five C11 trigger rows are parsed as calibration_usable representative rows. Confirm no hard duplicate exists for canonical_archetype_id + symbol + trigger_type + entry_date. Evaluate the candidate C11_ORDERBOOK_REQUIRES_CUSTOMER_QUALITY_MARGIN_FCF_BRIDGE_WITH_HIGH_MAE_CAP as a shadow rule only; do not directly overwrite production scoring without batch aggregation support.
```

## 17. Next recommended archetypes

```yaml
next_recommended_archetypes:
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  - C11_BATTERY_ORDERBOOK_RERATING_followup_if_still_below_30
```
