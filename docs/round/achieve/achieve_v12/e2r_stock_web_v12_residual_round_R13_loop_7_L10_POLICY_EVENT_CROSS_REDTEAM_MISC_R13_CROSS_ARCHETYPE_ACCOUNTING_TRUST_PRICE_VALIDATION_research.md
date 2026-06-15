# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 7
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: DEFENSE_CONTRACT_POLICY_SUBSIDY_AND_FINANCIAL_LABEL_TO_CASH_BRIDGE_VALIDATION
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13 is not a sector-positive discovery round. It is a cross-archetype checkpoint. This loop compares recent C03, C31, C21 and C22 cases and asks one question:

```text
Did the headline turn into a traceable listed-company accounting bridge?
```

The prior local `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` run reached loop 6, so this continuation is loop 7.

---

## 1. Research thesis

Accounting trust means the score can trace the story into one of the following:

```text
signed contract
delivery schedule
backlog
order/revenue
margin
cash conversion
capital return
reserve/solvency
tax credit/subsidy that reaches the company
```

If the bridge is present and price validates, Stage2 should survive. If the story is only a sector label or policy headline, Stage2 should be capped or blocked.

This loop splits seven routes:

1. **Signed defense export contract with delivery/backlog bridge** — keep Stage2.
2. **Defense export-system adoption chain** — keep Stage2; positive control.
3. **Policy headline plus real company-specific revenue bridge** — keep Stage2 but cap policy contribution.
4. **Policy/subsidy label without execution bridge** — block Stage2.
5. **Equipment/capex bridge with high MFE but deep MAE** — local 4B; require order/margin refresh.
6. **Direct financial ROE/capital-return bridge** — keep Stage2.
7. **Insurance-adjacent GA distribution label** — reclassify; cap C22 accounting-trust credit.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Symbol caveats:

```yaml
012450:
  name: 한화에어로스페이스
  source_archetype: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  relevant_window_after_old_corporate_action_candidates: true

079550:
  name: LIG넥스원
  source_archetype: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  corporate_action_candidate_count: 0
  calibration_caveat: clean

000660:
  name: SK하이닉스
  source_archetype: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  relevant_window_after_old_corporate_action_candidates: true

005930:
  name: 삼성전자
  source_archetype: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  relevant_window_clean_for_2024: true

042700:
  name: 한미반도체
  source_archetype: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  relevant_window_after_old_corporate_action_candidates: true

005940:
  name: NH투자증권
  source_archetype: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  relevant_window_after_old_corporate_action_candidates: true

244920:
  name: 에이플러스에셋
  source_archetype: C22_INSURANCE_RATE_CYCLE_RESERVE
  corporate_action_candidate_count: 0
  calibration_caveat: clean
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"SIGNED_DEFENSE_EXPORT_CONTRACT_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","entry_date":"2024-07-10","entry_close":256500,"price_basis":"tradable_raw","mfe_30d_pct":28.65,"mae_30d_pct":-3.70,"mfe_90d_pct":42.11,"mae_90d_pct":-3.70,"mfe_180d_pct":65.69,"mae_180d_pct":-3.70,"forward_high_30d":330000,"forward_low_30d":247000,"forward_high_90d":364500,"forward_low_90d":247000,"forward_high_180d":425000,"forward_low_180d":247000,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|012450|Stage2-Actionable|2024-07-10","accounting_bridge":"signed Romania K9/K10 package, quantity, ammunition/support and delivery schedule","route":"KeepStage2_DirectContractBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"DEFENSE_EXPORT_SYSTEM_ADOPTION_CHAIN_ACCOUNTING_TRUST_POSITIVE_CONTROL","source_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"079550","name":"LIG넥스원","trigger_type":"Stage2-Actionable","entry_date":"2024-02-07","entry_close":113400,"price_basis":"tradable_raw","mfe_30d_pct":64.46,"mae_30d_pct":-0.53,"mfe_90d_pct":64.46,"mae_90d_pct":-0.53,"mfe_180d_pct":119.58,"mae_180d_pct":-0.53,"forward_high_30d":186500,"forward_low_30d":112800,"forward_high_90d":186500,"forward_low_90d":112800,"forward_high_180d":249000,"forward_low_180d":112800,"calibration_usable":true,"case_role":"positive_control","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|079550|Stage2-Actionable|2024-02-07","accounting_bridge":"Cheongung-II/M-SAM export-system adoption chain and follow-on Middle East orders","route":"KeepStage2_PositiveControl"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"POLICY_HEADLINE_WITH_HBM_REVENUE_BRIDGE_CONTRIBUTION_CAP","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"000660","name":"SK하이닉스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":200000,"price_basis":"tradable_raw","mfe_30d_pct":21.50,"mae_30d_pct":-5.90,"mfe_90d_pct":24.25,"mae_90d_pct":-24.20,"mfe_180d_pct":24.25,"mae_180d_pct":-27.65,"forward_high_30d":243000,"forward_low_30d":188200,"forward_high_90d":248500,"forward_low_90d":151600,"forward_high_180d":248500,"forward_low_180d":144700,"calibration_usable":true,"case_role":"validated_but_contribution_cap","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|000660|Stage2-Actionable|2024-05-23","accounting_bridge":"policy headline overlapped with HBM/AI memory revenue bridge","route":"KeepStage2_CapPolicyContribution_Local4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"POLICY_SUBSIDY_LABEL_WITHOUT_EXECUTION_BRIDGE_STAGE2_BLOCK","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"005930","name":"삼성전자","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-23","entry_close":78300,"price_basis":"tradable_raw","mfe_30d_pct":5.36,"mae_30d_pct":-6.13,"mfe_90d_pct":13.41,"mae_90d_pct":-10.34,"mfe_180d_pct":13.41,"mae_180d_pct":-36.27,"forward_high_30d":82500,"forward_low_30d":73500,"forward_high_90d":88800,"forward_low_90d":70200,"forward_high_180d":88800,"forward_low_180d":49900,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005930|Stage2-FalsePositive|2024-05-23","accounting_bridge":"broad semiconductor policy/subsidy label without validated execution bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"EQUIPMENT_CAPEX_BRIDGE_HIGH_MFE_HIGH_MAE_CASH_REFRESH_REQUIRED","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"042700","name":"한미반도체","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":146400,"price_basis":"tradable_raw","mfe_30d_pct":34.02,"mae_30d_pct":-5.67,"mfe_90d_pct":34.02,"mae_90d_pct":-32.99,"mfe_180d_pct":34.02,"mae_180d_pct":-45.97,"forward_high_30d":196200,"forward_low_30d":138100,"forward_high_90d":196200,"forward_low_90d":98100,"forward_high_180d":196200,"forward_low_180d":79100,"calibration_usable":true,"case_role":"high_MFE_high_MAE_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|042700|Stage2-Actionable|2024-05-23","accounting_bridge":"HBM equipment/capex order bridge but deep MAE requires backlog and margin refresh","route":"Local4B_RequireOrderMarginRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"SECURITIES_ROE_CAPITAL_RETURN_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":11420,"price_basis":"tradable_raw","mfe_30d_pct":14.71,"mae_30d_pct":-2.36,"mfe_90d_pct":14.71,"mae_90d_pct":-2.36,"mfe_180d_pct":26.09,"mae_180d_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"positive_financial_control","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005940|Stage2-Actionable|2024-02-26","accounting_bridge":"securities ROE, brokerage/IB/WM flow and capital-return bridge","route":"KeepStage2_FinancialDirectBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"INSURANCE_ADJACENT_GA_LABEL_RECLASSIFY_ACCOUNTING_TRUST_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"accounting_trust_cap_reclassification","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|244920|Stage2-Watch|2024-05-10","accounting_bridge":"GA commission bridge, not reserve/solvency/rate-cycle bridge","route":"Stage2Cap_Reclassify"}
```

---

## 4. Case analysis

### 4.1 Hanwha Aerospace / 012450 — direct contract bridge validates accounting trust

The Romania K9/K10 export package is specific enough to pass the accounting-trust gate. It has named platforms, quantities, ammunition/support and a delivery window. The stock path validates that bridge.

```yaml
entry_close: 256500
90d_high: 364500
90d_low: 247000
180d_high: 425000
180d_low: 247000
route: KeepStage2_DirectContractBridge
```

This is the archetypal R13 escape hatch. Do not zero Stage2 when the contract is signed and delivery/backlog bridge is traceable.

---

### 4.2 LIG Nex1 / 079550 — export-system adoption chain is the clean positive control

LIG Nex1 is the cleanest control row. The M-SAM / Cheongung-II export chain is not a one-day label. It is a system adoption pattern across countries. The price path shows high MFE and almost no MAE.

```yaml
entry_close: 113400
90d_high: 186500
90d_low: 112800
180d_high: 249000
180d_low: 112800
route: KeepStage2_PositiveControl
```

---

### 4.3 SK Hynix / 000660 — policy support is valid only through HBM revenue bridge

SK Hynix had a positive path after the Korea semiconductor support package, but this should not be credited wholly to policy. The accounting bridge is HBM/AI memory demand, ASP, allocation and revenue.

```yaml
entry_close: 200000
90d_high: 248500
90d_low: 151600
180d_low: 144700
route: KeepStage2_CapPolicyContribution_Local4B
```

The rain helped, but the roots were HBM.

---

### 4.4 Samsung Electronics / 005930 — broad policy label failed

Samsung is the counterexample to broad policy learning. The same policy headline applied, but price validation failed badly by the 180D window.

```yaml
entry_close: 78300
90d_high: 88800
90d_low: 70200
180d_low: 49900
route: Stage2FalsePositiveBlock
```

A policy umbrella does not stop a company-specific execution storm.

---

### 4.5 Hanmi Semiconductor / 042700 — equipment bridge exists, but cash refresh is required

Hanmi had a real HBM equipment/capex bridge and large MFE. But the subsequent drawdown is too deep for Green.

```yaml
entry_close: 146400
30d_high: 196200
90d_low: 98100
180d_low: 79100
route: Local4B_RequireOrderMarginRefresh
```

The bridge was tradable, but the belt slipped. R13 should require order backlog, customer concentration, margin and cash conversion refresh before Green.

---

### 4.6 NH Investment & Securities / 005940 — financial accounting trust is validated

NH Investment & Securities validates that accounting trust is not limited to industrial contracts. ROE, brokerage flow, IB/WM earnings and capital-return expectations can also be a real bridge when price confirms.

```yaml
entry_close: 11420
180d_high: 14400
180d_low: 11150
route: KeepStage2_FinancialDirectBridge
```

---

### 4.7 A Plus Asset / 244920 — GA distribution belongs elsewhere

A Plus Asset has an insurance-adjacent commission bridge, but not a C22 reserve/solvency/rate-cycle bridge.

```yaml
entry_close: 4100
90d_high: 4500
90d_low: 3535
route: Stage2Cap_Reclassify
```

This is an accounting taxonomy issue. The revenue source is real, but it belongs under distribution commission economics, not insurance reserve-cycle economics.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
accounting_trust_validated_count: 3
positive_control_count: 1
policy_contribution_cap_count: 1
local_4B_cash_refresh_required_count: 1
stage2_false_positive_count: 1
reclassification_cap_count: 1
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 012450 | C03 | KeepStage2 | +42.11 / -3.70 | +65.69 / -3.70 | signed contract/accounting bridge validated |
| 079550 | C03 | positive control | +64.46 / -0.53 | +119.58 / -0.53 | export-system adoption chain validates |
| 000660 | C31 | cap policy contribution | +24.25 / -24.20 | +24.25 / -27.65 | policy works only through HBM revenue bridge |
| 005930 | C31 | hard block | +13.41 / -10.34 | +13.41 / -36.27 | policy label fails without execution |
| 042700 | C31 | local 4B | +34.02 / -32.99 | +34.02 / -45.97 | equipment bridge needs order/margin refresh |
| 005940 | C21 | KeepStage2 | +14.71 / -2.36 | +26.09 / -2.36 | ROE/capital-return bridge validates |
| 244920 | C22 | reclassify/cap | +9.76 / -13.78 | +14.63 / -13.78 | GA distribution is not reserve-cycle trust |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"012450","raw_direct_contract_bridge":5,"raw_revenue_margin_cash_bridge":4,"raw_policy_or_label_risk":0,"raw_price_validation":4,"raw_accounting_trust":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_DirectContractBridge"}
{"row_type":"score_simulation","symbol":"079550","raw_direct_contract_bridge":5,"raw_revenue_margin_cash_bridge":5,"raw_policy_or_label_risk":0,"raw_price_validation":5,"raw_accounting_trust":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PositiveControl"}
{"row_type":"score_simulation","symbol":"000660","raw_direct_contract_bridge":1,"raw_revenue_margin_cash_bridge":5,"raw_policy_or_label_risk":2,"raw_price_validation":3,"raw_accounting_trust":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"CapPolicyContribution_Local4B"}
{"row_type":"score_simulation","symbol":"005930","raw_direct_contract_bridge":0,"raw_revenue_margin_cash_bridge":1,"raw_policy_or_label_risk":5,"raw_price_validation":0,"raw_accounting_trust":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"042700","raw_direct_contract_bridge":2,"raw_revenue_margin_cash_bridge":3,"raw_policy_or_label_risk":3,"raw_price_validation":2,"raw_accounting_trust":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_RequireOrderMarginRefresh"}
{"row_type":"score_simulation","symbol":"005940","raw_direct_contract_bridge":0,"raw_revenue_margin_cash_bridge":4,"raw_policy_or_label_risk":1,"raw_price_validation":4,"raw_accounting_trust":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_FinancialDirectBridge"}
{"row_type":"score_simulation","symbol":"244920","raw_direct_contract_bridge":0,"raw_revenue_margin_cash_bridge":2,"raw_policy_or_label_risk":4,"raw_price_validation":1,"raw_accounting_trust":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_Reclassify"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The profile can still confuse three different situations:

```text
A. direct contract / direct ROE bridge
B. broad policy / sector beneficiary label
C. adjacent business model that belongs to another archetype
```

The wrong model treats all three as "positive headline." The correct model asks where the money goes. A contract is an invoice path. A policy is rain. A label is only a signboard. R13 should credit the invoice, cap the rain, and ignore the signboard unless cash appears.

### Rule candidate

```text
R13_ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V7

if signed_contract_or_direct_revenue_margin_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -15:
    accounting_trust_validated = true
    keep_stage2_actionable_bonus = true
```

```text
if broad_policy_or_sector_label == true
and company_specific_order_tax_credit_revenue_margin_bridge == false:
    accounting_trust_validated = false
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if broad_policy_headline == true
and dominant_driver_is_company_specific_demand_or_cycle == true:
    cap_policy_contribution = true
    require_source_archetype_reclassification = true
```

```text
if MFE_30D_pct >= +25
and MAE_90D_pct <= -25
and refreshed_order_margin_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if adjacent_business_model_label == true
and accounting_bridge_belongs_to_other_axis == true:
    stage2_actionable_bonus = 0
    reclassify_to_correct_archetype = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_accounting_trust_price_validation_candidate
new_axis_proposed: R13_ACCOUNTING_TRUST_PRICE_ALIGNMENT_GATE_V7
existing_axis_strengthened:
  - direct_contract_or_direct_revenue_bridge_keep_stage2
  - policy_label_without_company_bridge_stage2_block
  - policy_contribution_cap_when_company_cycle_dominates
  - high_MFE_high_MAE_requires_cash_bridge_refresh
  - adjacent_business_model_reclassification_guard
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_valueup_and_energy_policy_controls
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_underwriting_controls
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```
