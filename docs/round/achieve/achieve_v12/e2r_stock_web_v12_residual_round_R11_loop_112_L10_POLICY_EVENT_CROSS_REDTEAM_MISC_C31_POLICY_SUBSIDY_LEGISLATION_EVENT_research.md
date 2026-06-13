# E2R Stock-Web V12 Residual Research — R11 / C31 POLICY SUBSIDY LEGISLATION EVENT

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R11
selected_loop: 112
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: mixed_C31_robot_policy_subsidy_legislation_to_company_cash_bridge_holdout
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout; static C31 rows=118, guidance=URL/proxy repair, policy-to-company cash bridge, counterexample/4B balance
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` shows C31 as a Priority 2, already high-coverage canonical. Therefore this loop is not a quantity-fill loop. It is a quality holdout pass for the policy-to-company-cashflow bridge problem.

The selected trigger family is **Korea's advanced robotics policy package** around `2023-12-14`: the government announced a 3 trillion won robotics industry support plan through 2030, followed by the 4th Intelligent Robot Basic Plan for 2024-2028. This is a clean C31 policy/subsidy/legislation headline, but it does not automatically produce company-level orders, revenue recognition, margin bridge, or FCF.

This loop adds **7 calibration-usable trigger rows**, **7 robot-policy trigger families**, and **5 current-profile stress errors** for `R11/L10/C31`.

## 2. Stock-Web manifest/schema confirmation

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_shard_columns: d,o,h,l,c,v,a,mc,s,m
MFE_formula: max high from entry_date through N tradable rows / entry_price - 1
MAE_formula: min low from entry_date through N tradable rows / entry_price - 1
corporate_action_rule: 180D window blocked when corporate-action candidate overlaps
manifest_max_date: 2026-02-20
```

## 3. Case summary

| symbol | name | trigger_date | trigger_type | classification | evidence_family | MFE_180D_pct | MAE_180D_pct | drawdown_after_peak_pct |
|---|---|---:|---|---|---|---:|---:|---:|
| 056080 | 유진로봇 | 2023-12-14 | Stage2-Actionable | counterexample_low_MFE_high_MAE_policy_label | robot_policy_service_robot_headline_without_contract_bridge | 7.298 | -54.5613 | -57.6518 |
| 090360 | 로보스타 | 2023-12-14 | 4B | positive_with_local_4B_watch_no_company_cash_bridge | industrial_robot_policy_to_manufacturing_robot_capex_theme | 40.5694 | -29.5374 | -49.8734 |
| 108490 | 로보티즈 | 2023-12-14 | 4B | counterexample_high_MAE_after_policy_theme_MFE | service_robot_actuator_policy_theme_without_reorder_bridge | 28.6232 | -46.1232 | -58.1127 |
| 215100 | 로보로보 | 2023-12-14 | 4B | positive_price_path_but_bridge_absent_4B_watch | education_service_robot_policy_theme_delayed_MFE_high_MAE | 45.9516 | -31.6509 | -53.17 |
| 270660 | 에브리봇 | 2023-12-14 | 4B | positive_MFE_but_extreme_post_peak_4B | service_robot_policy_adoption_theme_fast_blowoff | 381.5745 | -5.0251 | -74.1391 |
| 277810 | 레인보우로보틱스 | 2023-12-14 | 4B | counterexample_policy_theme_not_incremental_company_cash_bridge | humanoid_robot_policy_and_largecap_valuation_boundary | 18.0947 | -38.5006 | -47.9236 |
| 117730 | 티로보틱스 | 2023-12-14 | 4B | counterexample_customer_capex_timing_gap_high_MAE | factory_automation_robot_policy_capex_timing_gap | 26.8229 | -60.4688 | -68.8296 |

## 4. Actual Stock-Web price-path table

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | corporate_action_180D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 056080 | 2023-12-14 | 11510 | 7.298 | -8.775 | 7.298 | -31.9722 | 7.298 | -54.5613 | 2024-01-12 | 12350 | -57.6518 | False |
| 090360 | 2023-12-14 | 28100 | 34.1637 | -3.7367 | 40.5694 | -3.7367 | 40.5694 | -29.5374 | 2024-02-27 | 39500 | -49.8734 | False |
| 108490 | 2023-12-14 | 27600 | 28.6232 | -2.1739 | 28.6232 | -22.1014 | 28.6232 | -46.1232 | 2024-01-12 | 35500 | -58.1127 | False |
| 215100 | 2023-12-14 | 4755 | 22.6078 | -5.4679 | 22.6078 | -11.6719 | 45.9516 | -31.6509 | 2024-05-22 | 6940 | -53.17 | False |
| 270660 | 2023-12-14 | 11940 | 119.8492 | -5.0251 | 381.5745 | -5.0251 | 381.5745 | -5.0251 | 2024-02-23 | 57500 | -74.1391 | False |
| 277810 | 2023-12-14 | 177400 | 6.708 | -10.372 | 18.0947 | -18.9402 | 18.0947 | -38.5006 | 2024-03-22 | 209500 | -47.9236 | False |
| 117730 | 2023-12-14 | 19200 | 26.8229 | -12.5 | 26.8229 | -12.5 | 26.8229 | -60.4688 | 2024-01-16 | 24350 | -68.8296 | False |

## 5. Case notes

### 5.1 Yujin Robot — policy label without company cash bridge

The national robotics support package could open a Stage2 watch window, but Yujin Robot's path shows the problem with treating policy exposure as a direct cashflow bridge. MFE_180D was only **7.298%** while MAE_180D reached **-54.5613%**. This should be capped at Stage2-Watch unless a named order, funded deployment program, or margin bridge is present.

### 5.2 Robostar — policy theme MFE, then local 4B

Robostar had meaningful 90D MFE after the robot policy headline, but the 180D MAE of **-29.5374%** and post-peak drawdown of **-49.8734%** show that C31 should add a local 4B overlay when policy momentum is not refreshed by company-level order conversion.

### 5.3 Robotis — actuator/service robot exposure is not enough

Robotis is a useful boundary case. It had real robotics exposure and early MFE, but the policy event alone did not protect the 180D path. This is a C31 counterexample against letting policy category membership stand in for budget allocation, customer order, or utilization evidence.

### 5.4 Roborobo and Everybot — strong price path but poor bridge discipline

Roborobo and Everybot show why C31 needs a two-step interpretation. Both had large MFE after the policy event, but both also experienced severe drawdowns. C31 should preserve the positive evidence only as a price-path stress case and require non-price bridge evidence before Stage3-Yellow.

### 5.5 Rainbow Robotics and T-Robotics — valuation and customer-capex timing gate

Rainbow Robotics and T-Robotics show the same pattern at different scales: a policy event can reprice the robotics category, but if the event does not specify funded company-level contracts, deployment volume, shipment schedule, or margin bridge, the calibrated profile should not keep Stage2/3 open without a local 4B cap.

## 6. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R11", "loop": "112", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "mixed_C31_robot_policy_subsidy_legislation_to_company_cash_bridge_holdout", "symbol": "056080", "name": "유진로봇", "trigger_date": "2023-12-14", "entry_date": "2023-12-14", "entry_price": 11510.0, "trigger_type": "Stage2-Actionable", "classification": "counterexample_low_MFE_high_MAE_policy_label", "evidence_family": "robot_policy_service_robot_headline_without_contract_bridge", "evidence_url": "https://en.yna.co.kr/view/AEN20231214003600320", "MFE_30D_pct": 7.298, "MAE_30D_pct": -8.775, "MFE_90D_pct": 7.298, "MAE_90D_pct": -31.9722, "MFE_180D_pct": 7.298, "MAE_180D_pct": -54.5613, "peak_date": "2024-01-12", "peak_price": 12350.0, "drawdown_after_peak_pct": -57.6518, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R11", "loop": "112", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "mixed_C31_robot_policy_subsidy_legislation_to_company_cash_bridge_holdout", "symbol": "090360", "name": "로보스타", "trigger_date": "2023-12-14", "entry_date": "2023-12-14", "entry_price": 28100.0, "trigger_type": "4B", "classification": "positive_with_local_4B_watch_no_company_cash_bridge", "evidence_family": "industrial_robot_policy_to_manufacturing_robot_capex_theme", "evidence_url": "https://world.kbs.co.kr/service/news_view.htm?Seq_Code=182436&lang=e", "MFE_30D_pct": 34.1637, "MAE_30D_pct": -3.7367, "MFE_90D_pct": 40.5694, "MAE_90D_pct": -3.7367, "MFE_180D_pct": 40.5694, "MAE_180D_pct": -29.5374, "peak_date": "2024-02-27", "peak_price": 39500.0, "drawdown_after_peak_pct": -49.8734, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": false, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R11", "loop": "112", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "mixed_C31_robot_policy_subsidy_legislation_to_company_cash_bridge_holdout", "symbol": "108490", "name": "로보티즈", "trigger_date": "2023-12-14", "entry_date": "2023-12-14", "entry_price": 27600.0, "trigger_type": "4B", "classification": "counterexample_high_MAE_after_policy_theme_MFE", "evidence_family": "service_robot_actuator_policy_theme_without_reorder_bridge", "evidence_url": "https://www.businesskorea.co.kr/news/articleView.html?idxno=209659", "MFE_30D_pct": 28.6232, "MAE_30D_pct": -2.1739, "MFE_90D_pct": 28.6232, "MAE_90D_pct": -22.1014, "MFE_180D_pct": 28.6232, "MAE_180D_pct": -46.1232, "peak_date": "2024-01-12", "peak_price": 35500.0, "drawdown_after_peak_pct": -58.1127, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R11", "loop": "112", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "mixed_C31_robot_policy_subsidy_legislation_to_company_cash_bridge_holdout", "symbol": "215100", "name": "로보로보", "trigger_date": "2023-12-14", "entry_date": "2023-12-14", "entry_price": 4755.0, "trigger_type": "4B", "classification": "positive_price_path_but_bridge_absent_4B_watch", "evidence_family": "education_service_robot_policy_theme_delayed_MFE_high_MAE", "evidence_url": "https://en.yna.co.kr/view/AEN20231214003600320", "MFE_30D_pct": 22.6078, "MAE_30D_pct": -5.4679, "MFE_90D_pct": 22.6078, "MAE_90D_pct": -11.6719, "MFE_180D_pct": 45.9516, "MAE_180D_pct": -31.6509, "peak_date": "2024-05-22", "peak_price": 6940.0, "drawdown_after_peak_pct": -53.17, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R11", "loop": "112", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "mixed_C31_robot_policy_subsidy_legislation_to_company_cash_bridge_holdout", "symbol": "270660", "name": "에브리봇", "trigger_date": "2023-12-14", "entry_date": "2023-12-14", "entry_price": 11940.0, "trigger_type": "4B", "classification": "positive_MFE_but_extreme_post_peak_4B", "evidence_family": "service_robot_policy_adoption_theme_fast_blowoff", "evidence_url": "https://www.businesskorea.co.kr/news/articleView.html?idxno=209659", "MFE_30D_pct": 119.8492, "MAE_30D_pct": -5.0251, "MFE_90D_pct": 381.5745, "MAE_90D_pct": -5.0251, "MFE_180D_pct": 381.5745, "MAE_180D_pct": -5.0251, "peak_date": "2024-02-23", "peak_price": 57500.0, "drawdown_after_peak_pct": -74.1391, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": false, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R11", "loop": "112", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "mixed_C31_robot_policy_subsidy_legislation_to_company_cash_bridge_holdout", "symbol": "277810", "name": "레인보우로보틱스", "trigger_date": "2023-12-14", "entry_date": "2023-12-14", "entry_price": 177400.0, "trigger_type": "4B", "classification": "counterexample_policy_theme_not_incremental_company_cash_bridge", "evidence_family": "humanoid_robot_policy_and_largecap_valuation_boundary", "evidence_url": "https://world.kbs.co.kr/service/news_view.htm?Seq_Code=182436&lang=e", "MFE_30D_pct": 6.708, "MAE_30D_pct": -10.372, "MFE_90D_pct": 18.0947, "MAE_90D_pct": -18.9402, "MFE_180D_pct": 18.0947, "MAE_180D_pct": -38.5006, "peak_date": "2024-03-22", "peak_price": 209500.0, "drawdown_after_peak_pct": -47.9236, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R11", "loop": "112", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "mixed_C31_robot_policy_subsidy_legislation_to_company_cash_bridge_holdout", "symbol": "117730", "name": "티로보틱스", "trigger_date": "2023-12-14", "entry_date": "2023-12-14", "entry_price": 19200.0, "trigger_type": "4B", "classification": "counterexample_customer_capex_timing_gap_high_MAE", "evidence_family": "factory_automation_robot_policy_capex_timing_gap", "evidence_url": "https://en.yna.co.kr/view/AEN20231214003600320", "MFE_30D_pct": 26.8229, "MAE_30D_pct": -12.5, "MFE_90D_pct": 26.8229, "MAE_90D_pct": -12.5, "MFE_180D_pct": 26.8229, "MAE_180D_pct": -60.4688, "peak_date": "2024-01-16", "peak_price": 24350.0, "drawdown_after_peak_pct": -68.8296, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "production_scoring_patch_applied": false}
```

## 7. Machine-readable score simulation rows

```jsonl
{"row_type": "score_simulation", "symbol": "056080", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_current_proxy": "e2r_2_2_rolling_calibrated", "pre_shadow_expected_stage": "Stage2-Watch", "post_shadow_expected_stage": "Stage2-Watch+local_4B", "policy_headline_score": 70, "legislation_budget_score": 62, "company_cashflow_bridge_score": 30, "local_4b_overlay_score": 80, "rule_candidate": "C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP"}
{"row_type": "score_simulation", "symbol": "090360", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_current_proxy": "e2r_2_2_rolling_calibrated", "pre_shadow_expected_stage": "Stage2-Actionable", "post_shadow_expected_stage": "Stage2-Actionable+bridge_required", "policy_headline_score": 70, "legislation_budget_score": 62, "company_cashflow_bridge_score": 42, "local_4b_overlay_score": 80, "rule_candidate": "C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP"}
{"row_type": "score_simulation", "symbol": "108490", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_current_proxy": "e2r_2_2_rolling_calibrated", "pre_shadow_expected_stage": "Stage2-Actionable", "post_shadow_expected_stage": "Stage2-Watch+local_4B", "policy_headline_score": 70, "legislation_budget_score": 62, "company_cashflow_bridge_score": 30, "local_4b_overlay_score": 80, "rule_candidate": "C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP"}
{"row_type": "score_simulation", "symbol": "215100", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_current_proxy": "e2r_2_2_rolling_calibrated", "pre_shadow_expected_stage": "Stage2-Actionable", "post_shadow_expected_stage": "Stage2-Watch+local_4B", "policy_headline_score": 70, "legislation_budget_score": 62, "company_cashflow_bridge_score": 30, "local_4b_overlay_score": 80, "rule_candidate": "C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP"}
{"row_type": "score_simulation", "symbol": "270660", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_current_proxy": "e2r_2_2_rolling_calibrated", "pre_shadow_expected_stage": "Stage2-Actionable", "post_shadow_expected_stage": "Stage2-Actionable+bridge_required", "policy_headline_score": 70, "legislation_budget_score": 62, "company_cashflow_bridge_score": 42, "local_4b_overlay_score": 80, "rule_candidate": "C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP"}
{"row_type": "score_simulation", "symbol": "277810", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_current_proxy": "e2r_2_2_rolling_calibrated", "pre_shadow_expected_stage": "Stage2-Actionable", "post_shadow_expected_stage": "Stage2-Watch+local_4B", "policy_headline_score": 70, "legislation_budget_score": 62, "company_cashflow_bridge_score": 30, "local_4b_overlay_score": 80, "rule_candidate": "C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP"}
{"row_type": "score_simulation", "symbol": "117730", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "baseline_current_proxy": "e2r_2_2_rolling_calibrated", "pre_shadow_expected_stage": "Stage2-Actionable", "post_shadow_expected_stage": "Stage2-Watch+local_4B", "policy_headline_score": 70, "legislation_budget_score": 62, "company_cashflow_bridge_score": 30, "local_4b_overlay_score": 80, "rule_candidate": "C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP"}
```

## 8. Aggregate metric row

```json
{
  "row_type": "aggregate_metric",
  "round": "R11",
  "loop": "112",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "calibration_usable_rows": 7,
  "representative_rows": 7,
  "positive_case_count": 3,
  "counterexample_count": 4,
  "local_4B_watch_count": 6,
  "4C_case_count": 0,
  "current_profile_error_count": 5,
  "avg_MFE_180D_pct": 78.4192,
  "avg_MAE_180D_pct": -37.981,
  "source_proxy_only_rows": 0,
  "evidence_url_pending_rows": 0,
  "corporate_action_contaminated_rows": 0
}
```

## 9. Shadow rule candidate

```text
C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP
```

### Rule intuition

C31 should not interpret a policy headline as a company-level rerating by itself. The policy must pass at least one of these gates before Stage3-Yellow:

1. budget line explicitly allocated to the company or its named consortium;
2. government procurement, deployment, or subsidy program with company-level order visibility;
3. customer order / shipment / revenue recognition evidence after the policy;
4. margin or FCF bridge showing that the policy changed company economics.

If those gates are absent but the stock shows fast MFE, route to `Stage2-Watch + local_4B`. If MAE90/MAE180 is already below -30% without bridge refresh, cap Stage2-Actionable and prevent Stage3 promotion.

## 10. Residual contribution summary

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C31_policy_to_company_cash_bridge_robot_theme_4B_cap
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
residual_error_found: true
```

## 11. Validation scope

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 7
calibration_usable_rows: 7
representative_rows: 7
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent. Do not run this handoff inside the research session. In a separate coding session, ingest this MD with the other V12 result files, parse every jsonl trigger row, validate required MFE/MAE fields, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and evaluate whether the following shadow rule should be added as a scoped C31 rule candidate:

C31_POLICY_EVENT_REQUIRES_BUDGET_CONTRACT_ORDER_REVENUE_OR_MARGIN_BRIDGE_WITH_ROBOT_THEME_4B_CAP

Preserve production-safety: generate patch specs only after aggregate validation, promotion-decision checks, and rejected-row audit. Do not change production scoring based on this single MD alone.
```

## 13. Next research state

```text
completed_round = R11
completed_loop = 112
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality holdout / C31 rows=118 / robot policy-to-cashflow bridge
next_recommended_archetypes = C31_POLICY_SUBSIDY_LEGISLATION_EVENT_holdout_only_if_new_policy_cash_bridge | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_quality_holdout
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
