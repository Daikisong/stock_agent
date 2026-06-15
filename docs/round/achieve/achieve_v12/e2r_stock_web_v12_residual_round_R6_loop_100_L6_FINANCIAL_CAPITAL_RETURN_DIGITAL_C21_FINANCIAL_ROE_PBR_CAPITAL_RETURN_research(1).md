# E2R Stock-Web v12 Residual Research — R6 / C21 Financial ROE-PBR Capital Return

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
```

## 1. File / scheduler metadata

```yaml
standard_v12_result_filename: e2r_stock_web_v12_residual_round_R6_loop_100_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
selected_round: R6
selected_loop: 100
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_AND_BROKERAGE_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIVIDEND_LABEL_OPPORTUNITY_COST
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
source_basis: FinanceData/marcap transformed into stock-web symbol-year shards
```

### Selection rationale

No-Repeat Index shows C21 with only 6 representative rows, 5 symbols, and top covered symbols `323410`, `003530`, `024110`, `030610`, `086790`. This run deliberately uses four symbols outside that top-covered set: `105560`, `055550`, `316140`, and `039490`. The goal is not to re-prove the global value-up rule, but to separate three paths that look similar in a headline feed:

1. **High-quality bank capital return bridge**: ROE/PBR discount narrows because CET1/capital return execution and credit-cost stability support the rerating.
2. **Weak/slow bank dividend label**: value-up language appears, but MFE is below the Stage2-actionable hurdle and the signal becomes opportunity-cost false positive rather than hard 4C.
3. **Brokerage beta / capital return overlay**: PBR/ROE rerating works but needs trading-activity and capital-return confirmation; otherwise it becomes a beta rally with later retracement.

The practical rule candidate is therefore:

```text
C21_CET1_CAPITAL_RETURN_CREDIT_COST_BRIDGE_REQUIRED
```

A financial ticker should not get Stage2-Actionable merely because it is low PBR or mentioned in value-up/capital return discourse. For C21, the bridge needs evidence of actual shareholder-yield execution, ROE durability, CET1 or capital buffer comfort, and no obvious credit-cost/reserve deterioration.

---

## 2. Stock-Web atlas validation scope

`Songdaiki/stock-web` manifest snapshot used in this run:

```yaml
atlas_version: 1.0.0
generated_at: 2026-05-21T16:28:39.421691+00:00
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
notes:
  - Raw/unadjusted OHLC.
  - Zero-volume and zero-OHLC rows excluded from calibration shards.
  - Corporate-action-contaminated windows blocked from calibration by default.
```

Symbol profile validation:

| symbol | name | profile status | corporate-action window near 2024 trigger? | calibration caveat |
|---|---|---|---|---|
| 105560 | KB금융 | active_like | none | clean 2024 calibration window |
| 055550 | 신한지주 | active_like | none | clean 2024 calibration window |
| 316140 | 우리금융지주 | active_like | none | clean 2024 calibration window |
| 039490 | 키움증권 | active_like | only old 2008 candidate | 2024 window usable; old CA window irrelevant |

All price rows below use `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/2024.csv`. Entry prices are close prices on the trigger date. MFE/MAE windows are computed from subsequent tradable rows over 30/90/180 trading-day style windows, using high for MFE and low for MAE. The numbers are rounded to two decimals.

---

## 3. Trigger-level backtest cases

### Case C21-100-01 — KB금융 / bank value-up + capital return bridge

```yaml
case_id: C21_R6_L100_105560_2024-02-01_STAGE2_ACTIONABLE
symbol: "105560"
name: KB금융
trigger_type: Stage2-Actionable
entry_date: 2024-02-01
entry_price: 61300
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_route: high_quality_bank_valueup_CET1_capital_return_ROE_PBR_bridge
outcome_label: positive
current_profile_error_type: too_conservative_without_C21_specific_bridge
```

Price path:

| window | peak/high used | trough/low used | MFE % | MAE % | interpretation |
|---:|---:|---:|---:|---:|---|
| 30D | 78,600 | 59,700 | +28.22 | -2.61 | Early Stage2-Actionable was validated quickly. |
| 90D | 83,400 | 59,700 | +36.05 | -2.61 | Follow-through remained orderly. |
| 180D | 103,900 | 59,700 | +69.49 | -2.61 | C21 bridge was durable; low-PBR label became capital-return rerating. |

Residual lesson: this is the model case where C21 deserves a stronger Stage2-Actionable interpretation. The decisive feature is not `bank + low PBR`; it is `bank + ROE durability + capital-return credibility + low MAE entry quality`.

---

### Case C21-100-02 — 신한지주 / slower but valid capital return rerating

```yaml
case_id: C21_R6_L100_055550_2024-02-01_STAGE2_ACTIONABLE
symbol: "055550"
name: 신한지주
trigger_type: Stage2-Actionable
entry_date: 2024-02-01
entry_price: 42500
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_route: bank_holding_valueup_shareholder_yield_ROE_stability_bridge
outcome_label: positive
current_profile_error_type: too_conservative_if_capital_return_bridge_confirmed
```

Price path:

| window | peak/high used | trough/low used | MFE % | MAE % | interpretation |
|---:|---:|---:|---:|---:|---|
| 30D | 51,500 | 39,850 | +21.18 | -6.24 | Valid but less clean than KB금융. |
| 90D | 51,500 | 39,850 | +21.18 | -6.24 | Stage2 works; not a Green unlock without stronger revision/capital return evidence. |
| 180D | 64,600 | 39,850 | +52.00 | -6.24 | Rerating eventually follows, but with more entry noise. |

Residual lesson: C21 should differentiate **clean bank rerating** from **noisy but acceptable bank rerating**. 신한지주 confirms the archetype, but the lower MFE/MAE quality argues for Stage2/Stage2-Actionable rather than automatic Stage3-Green.

---

### Case C21-100-03 — 우리금융지주 / dividend-value-up label with opportunity-cost false positive

```yaml
case_id: C21_R6_L100_316140_2024-02-01_STAGE2_LABEL_COUNTEREXAMPLE
symbol: "316140"
name: 우리금융지주
trigger_type: Stage2
entry_date: 2024-02-01
entry_price: 14410
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_route: dividend_valueup_label_without_fast_ROE_PBR_repricing
outcome_label: counterexample
current_profile_error_type: false_positive_if_stage2_actionable_given_to_dividend_label_only
```

Price path:

| window | peak/high used | trough/low used | MFE % | MAE % | interpretation |
|---:|---:|---:|---:|---:|---|
| 30D | 15,500 | 13,990 | +7.56 | -2.91 | Low MAE, but no actionable upside. |
| 90D | 15,500 | 13,740 | +7.56 | -4.65 | Fails Stage2-Actionable payoff despite benign downside. |
| 180D | 17,100 | 13,740 | +18.67 | -4.65 | Under +20% 180D MFE; opportunity-cost false positive. |

Residual lesson: the false positive is not a crash. It is subtler: a slow, dividend-like financial with low MAE but insufficient MFE. C21 needs a separate **opportunity-cost false positive** tag when MFE remains below the actionability threshold.

---

### Case C21-100-04 — 키움증권 / brokerage beta with ROE/capital return overlay

```yaml
case_id: C21_R6_L100_039490_2024-02-01_STAGE2_ACTIONABLE_BROKERAGE
symbol: "039490"
name: 키움증권
trigger_type: Stage2-Actionable
entry_date: 2024-02-01
entry_price: 107600
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_route: brokerage_ROE_PBR_valueup_capital_return_beta_bridge
outcome_label: positive_with_cycle_beta_caveat
current_profile_error_type: too_conservative_if_brokerage_capital_return_and_market_activity_bridge_confirmed
```

Price path:

| window | peak/high used | trough/low used | MFE % | MAE % | interpretation |
|---:|---:|---:|---:|---:|---|
| 30D | 136,600 | 105,500 | +26.95 | -1.95 | Strong early broker rerating. |
| 90D | 136,600 | 105,500 | +26.95 | -1.95 | Still validated, but not bank-like visibility. |
| 180D | 146,400 | 105,500 | +36.06 | -1.95 | Good path; requires trading activity/capital-return bridge. |

Residual lesson: securities firms can pass C21, but the required bridge differs from banks. The check should be `brokerage ROE/PBR + trading activity + capital return`, not only low PBR.

---

## 4. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C21_R6_L100_105560_2024-02-01_STAGE2_ACTIONABLE","selected_round":"R6","selected_loop":100,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_AND_BROKERAGE_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIVIDEND_LABEL_OPPORTUNITY_COST","symbol":"105560","name":"KB금융","trigger_type":"Stage2-Actionable","entry_date":"2024-02-01","entry_price":61300,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.22,"MAE_30D_pct":-2.61,"MFE_90D_pct":36.05,"MAE_90D_pct":-2.61,"MFE_180D_pct":69.49,"MAE_180D_pct":-2.61,"peak_180D_price":103900,"trough_180D_price":59700,"outcome_label":"positive","current_profile_error_type":"too_conservative_without_C21_specific_bridge","evidence_source_proxy":"historical bank value-up/capital-return bridge; external URL pending","evidence_url_pending":true,"representative_for_aggregate":true}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C21_R6_L100_055550_2024-02-01_STAGE2_ACTIONABLE","selected_round":"R6","selected_loop":100,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_AND_BROKERAGE_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIVIDEND_LABEL_OPPORTUNITY_COST","symbol":"055550","name":"신한지주","trigger_type":"Stage2-Actionable","entry_date":"2024-02-01","entry_price":42500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":21.18,"MAE_30D_pct":-6.24,"MFE_90D_pct":21.18,"MAE_90D_pct":-6.24,"MFE_180D_pct":52.00,"MAE_180D_pct":-6.24,"peak_180D_price":64600,"trough_180D_price":39850,"outcome_label":"positive","current_profile_error_type":"too_conservative_if_capital_return_bridge_confirmed","evidence_source_proxy":"historical bank value-up/capital-return bridge; external URL pending","evidence_url_pending":true,"representative_for_aggregate":true}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C21_R6_L100_316140_2024-02-01_STAGE2_LABEL_COUNTEREXAMPLE","selected_round":"R6","selected_loop":100,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_AND_BROKERAGE_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIVIDEND_LABEL_OPPORTUNITY_COST","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2","entry_date":"2024-02-01","entry_price":14410,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.56,"MAE_30D_pct":-2.91,"MFE_90D_pct":7.56,"MAE_90D_pct":-4.65,"MFE_180D_pct":18.67,"MAE_180D_pct":-4.65,"peak_180D_price":17100,"trough_180D_price":13740,"outcome_label":"counterexample","current_profile_error_type":"false_positive_if_stage2_actionable_given_to_dividend_label_only","evidence_source_proxy":"historical bank dividend/value-up label; external URL pending","evidence_url_pending":true,"representative_for_aggregate":true}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C21_R6_L100_039490_2024-02-01_STAGE2_ACTIONABLE_BROKERAGE","selected_round":"R6","selected_loop":100,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_AND_BROKERAGE_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIVIDEND_LABEL_OPPORTUNITY_COST","symbol":"039490","name":"키움증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-01","entry_price":107600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":26.95,"MAE_30D_pct":-1.95,"MFE_90D_pct":26.95,"MAE_90D_pct":-1.95,"MFE_180D_pct":36.06,"MAE_180D_pct":-1.95,"peak_180D_price":146400,"trough_180D_price":105500,"outcome_label":"positive_with_cycle_beta_caveat","current_profile_error_type":"too_conservative_if_brokerage_capital_return_and_market_activity_bridge_confirmed","evidence_source_proxy":"historical brokerage ROE/PBR value-up/capital-return beta bridge; external URL pending","evidence_url_pending":true,"representative_for_aggregate":true}
```

---

## 5. Aggregate alignment

| metric | value |
|---|---:|
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 4 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 4 |
| positive_case_count | 3 |
| counterexample_count | 1 |
| 4B_case_count | 0 |
| 4C_case_count | 0 |
| current_profile_error_count | 4 |
| average_MFE_30D_pct | 20.98 |
| average_MAE_30D_pct | -3.43 |
| average_MFE_90D_pct | 22.94 |
| average_MAE_90D_pct | -3.86 |
| average_MFE_180D_pct | 44.06 |
| average_MAE_180D_pct | -3.86 |

Interpretation:

- C21 has a strong asymmetry when the capital-return bridge is real: KB금융 and 신한지주 both provide clean Stage2-Actionable validation.
- The weak row is not a crash row. 우리금융지주 shows the false-positive class specific to financials: low downside, but insufficient upside and delayed repricing.
- 키움증권 confirms that brokerage can belong in C21, but it needs a different non-price bridge from banks. The bridge is trading activity / risk appetite / capital return, not just low PBR.

---

## 6. Raw component score breakdown proxy

Current C21 weights in the No-Repeat snapshot are:

```text
EPS/FCF: 15
Visibility: 20
Bottleneck/Pricing: 5
Market Mispricing: 15
Valuation Rerating: 25
Capital Allocation: 15
Information Confidence: 5
```

| symbol | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital Allocation | Info | total proxy | resulting label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 105560 | 14 | 18 | 3 | 14 | 23 | 14 | 4 | 90 | Stage2-Actionable / Stage3-Yellow watch |
| 055550 | 13 | 17 | 3 | 13 | 21 | 12 | 4 | 83 | Stage2-Actionable |
| 316140 | 11 | 14 | 3 | 12 | 18 | 9 | 4 | 71 | Stage2 only / no actionable bonus |
| 039490 | 13 | 15 | 3 | 14 | 20 | 11 | 4 | 80 | Stage2-Actionable with brokerage beta caveat |

C21 should therefore not raise every value-up financial. It should reward the joint presence of capital allocation and valuation rerating only when the financial-quality bridge is observable.

---

## 7. Residual rule proposal

### New axis candidate

```yaml
new_axis_proposed: C21_CET1_CAPITAL_RETURN_CREDIT_COST_BRIDGE_REQUIRED
axis_type: stage2_required_bridge
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
safe_to_shadow: true
production_scoring_changed: false
```

Rule text:

```text
For C21 financial ROE/PBR/capital-return cases, Stage2-Actionable requires at least two non-price bridges:
1. explicit or inferable shareholder-yield execution path, such as buyback/cancellation/dividend policy improvement,
2. ROE durability or credit-cost/reserve/NIM stability,
3. capital buffer comfort such as CET1, solvency, leverage or risk-weighted asset constraint not blocking payout,
4. segment-specific confirmation for brokerages, such as transaction activity, market turnover beta, or fee-income/revision bridge.

If only low-PBR/value-up vocabulary exists, keep as Stage2 watch or narrative-only; do not grant Stage2-Actionable bonus.
```

### Existing axes strengthened

```yaml
existing_axis_strengthened:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
```

---

## 8. Score-return alignment notes

- `105560` and `055550` validate that C21 can have high-quality MFE/MAE structure. The stronger bank cases generated +69.49% and +52.00% 180D MFE with sub-7% MAE.
- `316140` is the important counterexample. It does not break down enough for 4C, but its 180D MFE remained below +20%. This should be counted as **bad actionability**, not as a hard thesis break.
- `039490` shows that brokerage cases should not be excluded. However, the driver is more cyclical. A brokerage-specific bridge should include market activity, fee income and capital return, otherwise the signal can be misclassified as a bank-like defensive rerating.

---

## 9. Deferred Coding Agent Handoff Prompt — DO NOT EXECUTE IN THIS RUN

```text
You are the later batch implementation coding agent for Songdaiki/stock_agent.
Do not treat this Markdown file as production truth without batch validation.

Input artifact:
- e2r_stock_web_v12_residual_round_R6_loop_100_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Parse the JSONL trigger rows.
2. Validate the hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Recalculate 30D/90D/180D MFE/MAE from Songdaiki/stock-web tradable_raw shards.
4. If rows pass validation, add them to the v12 calibration corpus.
5. Treat the proposed axis only as a shadow rule candidate:
   C21_CET1_CAPITAL_RETURN_CREDIT_COST_BRIDGE_REQUIRED.
6. Do not loosen Stage3-Green thresholds.
7. Do not globally raise all financial value-up cases.
8. Prefer a C21-scoped stage2_required_bridge patch if repeated rows confirm the pattern.
```

---

## 10. Completion state

```yaml
completed_round: R6
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_AND_BROKERAGE_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIVIDEND_LABEL_OPPORTUNITY_COST
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 4
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C21 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C21_CET1_CAPITAL_RETURN_CREDIT_COST_BRIDGE_REQUIRED
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | stage2_required_bridge
existing_axis_weakened: null
next_recommended_archetypes:
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```
