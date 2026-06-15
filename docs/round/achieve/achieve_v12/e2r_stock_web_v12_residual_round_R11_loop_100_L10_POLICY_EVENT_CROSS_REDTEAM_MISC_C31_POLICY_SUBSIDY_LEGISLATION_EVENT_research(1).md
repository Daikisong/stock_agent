# E2R Stock-Web v12 Residual Research — R11 Loop 100 — C31 Policy / Subsidy / Legislation Event

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata

```yaml
output_filename: e2r_stock_web_v12_residual_round_R11_loop_100_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
selected_round: R11
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: POLICY_TO_CASHFLOW_BRIDGE_VALUEUP_TARIFF_TELEMEDICINE_VS_POLICY_LABEL_SPIKE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
  - sector_specific_rule_discovery
```

### Selection basis

`V12_Research_No_Repeat_Index.md` lists `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` as Priority 0 with 3 rows, need to 30 = 27, need to 50 = 47. The investigation point is whether a policy headline converts into law/budget/company cashflow. Existing registry already has an R11 loop 99 C31 file and an R12 loop 91 C31 file, so under the v12 loop rule the next R11/C31 loop is `100`.

The v12 prompt requires actual stock-web 1D OHLC, complete 30/90/180D MFE/MAE for every usable trigger, standard filename, and no production scoring change.

## 2. Price source validation

```yaml
primary_price_source: Songdaiki/stock-web
source_basis: FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
forward_windows_complete: true
corporate_action_window_blocked: true
```

Source paths used:

```text
Songdaiki/stock-web/atlas/manifest.json
Songdaiki/stock-web/atlas/symbol_profiles/105/105560.json
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
Songdaiki/stock-web/atlas/symbol_profiles/015/015760.json
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv
Songdaiki/stock-web/atlas/symbol_profiles/032/032620.json
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/032/032620/2024.csv
```

External evidence notes used only for non-price bridge classification:

```text
- Korea Corporate Value-up Programme / follow-up incentives: Reuters, 2024-03-14 and 2024-04-02.
- Korea temporary full telemedicine allowance during trainee-doctor walkout: Reuters, 2024-02-23.
```

## 3. Research thesis

C31 should **not** reward a policy word by itself. Policy is a bridge only if the route from government action to company-level cashflow is visible.

The scoring metaphor is simple: policy headline is a gate opening; it is not the cargo arriving. The useful signal appears only when one can see the cargo route: law or rule, budget or tariff, reimbursement or tax incentive, company-specific disclosure, then revenue/cash return/margin.

This loop therefore tests three policy families:

1. **Value-up policy with company-specific capital-return bridge** — possible positive.
2. **Regulated utility tariff/recovery expectation without enough confirmed cash bridge** — counterexample / 4B watch.
3. **Temporary telemedicine access expansion without reimbursement/revenue bridge** — hard false-positive risk.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | polarity | bridge verdict |
|---|---:|---|---|---|---:|---|---|
| C31_105560_2024_VALUEUP_POLICY_COMPANY_RETURN_BRIDGE | 105560 | KB금융 | 2024-02-26 | 2024-02-26 | 62,500 | positive | policy + company-specific capital return / ROE-PBR route |
| C31_015760_2024_TARIFF_POLICY_EXPECTATION_CASHFLOW_BRIDGE_TEST | 015760 | 한국전력 | 2024-02-19 | 2024-02-19 | 23,200 | counterexample | tariff/recovery expectation needs concrete pass-through/debt/dividend path |
| C31_032620_2024_TELEMEDICINE_TEMPORARY_ALLOWANCE_LABEL_SPIKE | 032620 | 유비케어 | 2024-02-23 | 2024-02-23 | 7,170 | counterexample | temporary policy access was not reimbursement or recurring revenue |

## 5. Backtest result table

| symbol | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | path read |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 105560 | 62,500 | +25.76% | -4.48% | +44.00% | -4.48% | +66.24% | -4.48% | low-MAE structural policy-to-cash positive |
| 015760 | 23,200 | +9.70% | -6.25% | +9.70% | -18.06% | +9.70% | -18.06% | policy expectation spike faded without cashflow confirmation |
| 032620 | 7,170 | +10.32% | -33.05% | +10.32% | -40.03% | +10.32% | -53.77% | temporary policy-access label spike, severe drawdown |

## 6. Raw trigger rows JSONL

```jsonl
{"MAE_180D_pct": -4.48, "MAE_30D_pct": -4.48, "MAE_90D_pct": -4.48, "MFE_180D_pct": 66.24, "MFE_30D_pct": 25.76, "MFE_90D_pct": 44.0, "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_105560_2024_VALUEUP_POLICY_COMPANY_RETURN_BRIDGE", "case_polarity": "positive", "current_profile_verdict": "missed_structural_if_policy_headline_discounted_after_company_cash_bridge", "duplicate_key": "105560|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|Stage2_Actionable|2024-02-26|2024-02-26|62500|policy_valueup_to_company_capital_return_execution", "entry_date": "2024-02-26", "entry_price": 62500.0, "evidence_family": "policy_valueup_to_company_capital_return_execution", "fine_archetype_id": "VALUEUP_POLICY_TO_COMPANY_CAPITAL_RETURN_CASH_BRIDGE_VS_GENERIC_POLICY_HEADLINE", "forward_window_complete": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "name": "KB금융", "non_price_bridge": "policy headline was paired with company-specific capital-return/ROE/PBR bridge, so the policy mechanism had an observable cash-return route rather than pure theme beta.", "peak_date_used": "2024-10-25", "peak_price_used": 103900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "round": "R11", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "symbol": "105560", "trigger_date": "2024-02-26", "trigger_type": "Stage2_Actionable", "trough_date_used": "2024-02-26", "trough_price_used": 59700.0}
{"MAE_180D_pct": -18.06, "MAE_30D_pct": -6.25, "MAE_90D_pct": -18.06, "MFE_180D_pct": 9.7, "MFE_30D_pct": 9.7, "MFE_90D_pct": 9.7, "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_015760_2024_TARIFF_POLICY_EXPECTATION_CASHFLOW_BRIDGE_TEST", "case_polarity": "counterexample", "current_profile_verdict": "false_positive_risk_if_policy_expectation_gets_stage2_without_tariff_debt_cash_bridge", "duplicate_key": "015760|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|Stage2_Actionable|2024-02-19|2024-02-19|23200|regulated_tariff_policy_expectation_without_confirmed_cashflow_bridge", "entry_date": "2024-02-19", "entry_price": 23200.0, "evidence_family": "regulated_tariff_policy_expectation_without_confirmed_cashflow_bridge", "fine_archetype_id": "UTILITY_TARIFF_POLICY_TO_CASHFLOW_BRIDGE_VS_TARIFF_FREEZE_BALANCE_SHEET_DRAG", "forward_window_complete": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "name": "한국전력", "non_price_bridge": "regulated-utility policy expectation was not enough unless tariff recovery, debt reduction, fuel-cost pass-through, and dividend path were concrete.", "peak_date_used": "2024-03-14", "peak_price_used": 25450.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "round": "R11", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "symbol": "015760", "trigger_date": "2024-02-19", "trigger_type": "Stage2_Actionable", "trough_date_used": "2024-05-30", "trough_price_used": 19010.0}
{"MAE_180D_pct": -53.77, "MAE_30D_pct": -33.05, "MAE_90D_pct": -40.03, "MFE_180D_pct": 10.32, "MFE_30D_pct": 10.32, "MFE_90D_pct": 10.32, "calibration_usable": true, "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "case_id": "C31_032620_2024_TELEMEDICINE_TEMPORARY_ALLOWANCE_LABEL_SPIKE", "case_polarity": "counterexample", "current_profile_verdict": "hard_false_positive_if_temporary_policy_access_is_scored_as_structural_legislation", "duplicate_key": "032620|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|Stage2_Actionable|2024-02-23|2024-02-23|7170|telemedicine_temporary_access_policy_without_reimbursement_revenue_margin_bridge", "entry_date": "2024-02-23", "entry_price": 7170.0, "evidence_family": "telemedicine_temporary_access_policy_without_reimbursement_revenue_margin_bridge", "fine_archetype_id": "TELEMEDICINE_TEMPORARY_ACCESS_POLICY_VS_REIMBURSEMENT_REVENUE_BRIDGE", "forward_window_complete": true, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "loop": 100, "name": "유비케어", "non_price_bridge": "temporary access expansion alone did not prove reimbursement, adoption, order, recurring revenue, or margin conversion for the listed software vendor.", "peak_date_used": "2024-02-23", "peak_price_used": 7910.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "round": "R11", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "symbol": "032620", "trigger_date": "2024-02-23", "trigger_type": "Stage2_Actionable", "trough_date_used": "2024-11-14", "trough_price_used": 3315.0}
```

## 7. Score / return alignment

### 7.1 Positive alignment — KB금융 / 105560

- Entry: 2024-02-26 close 62,500.
- 30D high used: 78,600; 180D high used: 103,900.
- 30D/90D/180D MAE stayed shallow relative to the upside path.
- This was not simply a policy keyword. It had a company-level capital-return and valuation-efficiency bridge, so C31 should allow Stage2/Stage3 support only after the policy bridge becomes company-specific.

Raw component score sketch:

```yaml
case_id: C31_105560_2024_VALUEUP_POLICY_COMPANY_RETURN_BRIDGE
EPS_revision: 14
visibility: 22
bottleneck_or_policy_mechanism: 24
mispricing: 16
valuation_risk: -4
capital_return_or_cash_bridge: 22
info_quality: 8
raw_total: 102
current_calibrated_stage_simulation: Stage3_Green_candidate
profile_error_type: missed_structural_if_policy_headline_discounted_after_company_cash_bridge
```

### 7.2 Counterexample — 한국전력 / 015760

- Entry: 2024-02-19 close 23,200.
- The stock briefly reached 25,450 but later fell to 19,010 in the 90D/180D path.
- Regulated tariff policy expectation did not deserve structural Stage2 unless tariff recovery, debt reduction, fuel-cost pass-through, and shareholder return path were visible.

Raw component score sketch:

```yaml
case_id: C31_015760_2024_TARIFF_POLICY_EXPECTATION_CASHFLOW_BRIDGE_TEST
EPS_revision: 4
visibility: 8
bottleneck_or_policy_mechanism: 18
mispricing: 10
valuation_risk: -8
capital_return_or_cash_bridge: 2
info_quality: 5
raw_total: 39
current_calibrated_stage_simulation: Stage2_false_positive_or_4B_watch
profile_error_type: false_positive_risk_if_policy_expectation_gets_stage2_without_tariff_debt_cash_bridge
```

### 7.3 Counterexample — 유비케어 / 032620

- Entry: 2024-02-23 close 7,170.
- Same-day high reached 7,910, then the 180D path fell to 3,315.
- Temporary telemedicine permission during system disruption was not the same as durable legislation, reimbursement, platform adoption, recurring order, or margin conversion.

Raw component score sketch:

```yaml
case_id: C31_032620_2024_TELEMEDICINE_TEMPORARY_ALLOWANCE_LABEL_SPIKE
EPS_revision: 2
visibility: 6
bottleneck_or_policy_mechanism: 18
mispricing: 8
valuation_risk: -14
capital_return_or_cash_bridge: 0
info_quality: 4
raw_total: 24
current_calibrated_stage_simulation: hard_false_positive_if_policy_headline_scored_as_structural
profile_error_type: policy_label_spike_without_reimbursement_revenue_bridge
```

## 8. 4B local vs full-window proximity

| symbol | local 4B risk | full-window read | note |
|---:|---|---|---|
| 105560 | low | positive continuation | local strength followed through because policy was company-specific and cash-return linked |
| 015760 | medium | weak follow-through | policy expectation produced spike but not enough durable cashflow bridge |
| 032620 | high | hard decay | temporary policy access produced event spike and severe 180D drawdown |

## 9. Residual contribution summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
diversity_score_summary: new_symbol=3, new_trigger_family=3, positive/counterexample=1/2, 4B_guard_case=2
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

### Rule candidate

```yaml
rule_candidate_id: C31_POLICY_TO_CASHFLOW_BRIDGE_REQUIREMENT
scope:
  large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
  canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
proposal_type: shadow_only
rule_text: >
  For C31, policy/subsidy/legislation evidence may contribute to Stage2 or Stage3 only when at least one company-specific bridge is visible:
  law/rule finalization, budget or tariff pass-through, reimbursement, tax incentive captured by the company, signed contract/order, capital-return execution, or observable revenue/margin conversion.
  Temporary access, campaign pledge, task-force headline, or policy vocabulary alone should be capped at Watch/4B unless cashflow bridge evidence appears.
positive_support:
  - 105560 policy + company capital-return bridge, low MAE and +66.24% 180D MFE
counterexample_support:
  - 015760 tariff/recovery expectation without enough cash bridge, +9.70% max MFE and -18.06% MAE
  - 032620 temporary telemedicine access without reimbursement/revenue bridge, +10.32% max MFE and -53.77% MAE
expected_effect: reduce policy-label false positives while preserving cases where policy becomes company-level cashflow
```

## 10. Validation scope

```yaml
validation_scope:
  price_source: Songdaiki/stock-web
  price_basis: tradable_raw
  adjustment_status: raw_unadjusted_marcap
  forward_mfe_mae_fields_complete: true
  entry_date_present: true
  entry_price_present: true
  trigger_type_is_canonical_stage_label: true
  non_price_bridge_present: true
  duplicate_check_against_no_repeat_index: pass
  production_scoring_changed: false
  handoff_prompt_executed_now: false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.

You are the later batch implementation agent for stock_agent E2R v12 calibration.

Input MD:
e2r_stock_web_v12_residual_round_R11_loop_100_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse the JSONL trigger rows.
2. Validate stock-web price source fields:
   - price_source == Songdaiki/stock-web
   - price_basis == tradable_raw
   - price_adjustment_status == raw_unadjusted_marcap
   - 30/90/180D MFE and MAE are complete.
3. Dedupe with key:
   symbol + canonical_archetype_id + trigger_type + trigger_date + entry_date + entry_price + evidence_family.
4. Treat this as shadow-only evidence for:
   C31_POLICY_SUBSIDY_LEGISLATION_EVENT.
5. Do not change production scoring directly.
6. Candidate shadow rule:
   C31 policy evidence requires law/budget/tariff/reimbursement/company-cashflow bridge before Stage2/Stage3; temporary access or policy vocabulary alone is Watch/4B capped.
```

## 12. Completed research state

```text
completed_round = R11
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
