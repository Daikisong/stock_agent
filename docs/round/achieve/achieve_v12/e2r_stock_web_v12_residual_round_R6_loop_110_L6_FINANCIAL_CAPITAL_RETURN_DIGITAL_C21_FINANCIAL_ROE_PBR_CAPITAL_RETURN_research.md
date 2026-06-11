# E2R Stock-Web v12 Residual Research — R6 / Loop 110 / C21

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 110
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIGITAL_FINANCE_HIGH_PBR_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: false
```

## 1. Selection and no-repeat check

The main execution prompt was treated as the operating contract: this run is not live discovery, not auto-trading, not a code patch, and not a production scoring change. The required output is a standalone historical calibration Markdown artifact using actual `Songdaiki/stock-web` 1D OHLC.

`V12_Research_No_Repeat_Index.md` shows `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` at **6 representative rows / 5 unique symbols**, below the 30-row minimum target. The current listed C21 symbols are `323410`, `003530`, `024110`, `030610`, and `086790`, so this pass avoids those symbols and uses three new C21 symbols: `055550`, `175330`, and `377300`.

The existing registry has R6/C21 through loop 109, so by the v12 scheduler rule this run uses:

```text
selected_loop = max(existing loop for R6 + C21) + 1 = 110
```

## 2. Archetype thesis

C21 is not a generic "financial stock is cheap" bucket. The C21 bridge requires:

```text
low PBR / valuation discount
+ durable ROE or ROE recovery
+ CET1 / capital buffer or equivalent balance sheet support
+ explicit shareholder return execution
```

The failure route is equally important:

```text
financial label
+ policy/value-up headline
+ high PBR digital-finance story
- no durable ROE
- no cash capital return
= Stage2-FalsePositive or 4B watch, not Green
```

This run therefore separates bank-holding rerating from digital-financial price spikes.

## 3. External context

Public context: Korea's Corporate Value-up Programme was aimed at improving shareholder returns and reducing valuation discounts. Reuters reported that Korean authorities were considering penalties for companies failing to meet shareholder-return criteria after the initial reform package disappointed some investors. This supports using shareholder-return execution as a hard bridge rather than letting a policy label alone open Green.

External reference:
- Reuters, 2024-02-28, "S.Korea considering penalties on firms failing to boost shareholder return"

## 4. Price source validation

```json
{
  "row_type": "price_source_validation",
  "price_source": "Songdaiki/stock-web",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "corporate_action_windows_blocked_by_default": true,
  "symbols_checked": ["055550", "175330", "377300"]
}
```

## 5. Case table

| case_id | symbol | name | verdict | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C21_055550_SHINHAN_VALUEUP_CAPITAL_RETURN_2024_07_26 | 055550 | 신한지주 | positive | 2024-07-26 | 58,000 | 10.69% | -11.03% | 11.38% | -11.03% | 11.38% | -18.02% |
| C21_175330_JB_FINANCIAL_ROE_PBR_CAPITAL_RETURN_2024_10_25 | 175330 | JB금융지주 | positive_with_high_MAE_watch | 2024-10-25 | 18,290 | 4.26% | -5.30% | 12.08% | -14.82% | 12.08% | -14.82% |
| C21_377300_KAKAOPAY_DIGITAL_FINANCE_FALSE_STAGE2_2024_01_11 | 377300 | 카카오페이 | counterexample | 2024-01-11 | 58,000 | 3.79% | -21.90% | 3.79% | -40.00% | 3.79% | -55.00% |

## 6. Case notes

### 6.1 Shinhan Financial Group / 055550 — positive Stage2-Actionable

`055550` is a bank-holding rerating case where the score should depend on ROE/PBR/capital-return execution rather than policy vocabulary alone. The entry row is 2024-07-26 at close 58,000. The initial path produced a same-window high of 64,200 on 2024-07-29 and 64,600 by 2024-08-26, while the downside trough was 51,600 on 2024-08-05 and 47,550 on 2025-01-02.

Interpretation:

```text
Stage2-Actionable = allowed
Stage3-Green = not automatic
4B watch = only if vertical move occurs without follow-through capital-return confirmation
```

The 180D MFE was positive but not explosive. This is exactly the kind of case where Stage2 should be earlier than Green and Green should require continued capital-return execution.

### 6.2 JB Financial Group / 175330 — positive but high-MAE watch

`175330` is a regional-bank C21 case. The entry row is 2024-10-25 at close 18,290. The path reached 20,500 by 2024-12-03 but also pulled back to 15,580 on 2025-01-03. This is a useful residual case because it says:

```text
high ROE + low PBR + shareholder return = Stage2/Yellow bridge
regional bank volatility + credit/capital sensitivity = Green delay or high-MAE guard
```

It strengthens the rule that a regional-bank capital-return case can be usable, but only if the profile does not treat low PBR alone as enough.

### 6.3 Kakao Pay / 377300 — counterexample

`377300` is a digital-finance label false positive. The entry row is 2024-01-11 at close 58,000 after a sharp intraday high. The price briefly reached 60,200 on the same day, but then fell to 45,300 by 2024-02-01, 34,800 by 2024-04-12, and 26,100 by 2024-06-27.

This row should harden the C21 rule:

```text
digital finance label ≠ C21
platform payment label ≠ capital-return rerating
high PBR + no durable ROE + no explicit cash return = Stage2-FalsePositive / 4B watch
```

## 7. JSONL trigger rows

```jsonl
{"row_type":"trigger","case_id":"C21_055550_SHINHAN_VALUEUP_CAPITAL_RETURN_2024_07_26","symbol":"055550","name":"신한지주","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIGITAL_FINANCE_HIGH_PBR_FALSE_POSITIVE","trigger_type":"Stage2-Actionable","trigger_family":"bank_holding_valueup_cet1_roe_capital_return_execution_bridge","evidence_family":"ROE_CET1_capital_return_execution","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":58000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":10.69,"MAE_30D_pct":-11.03,"MFE_90D_pct":11.38,"MAE_90D_pct":-11.03,"MFE_180D_pct":11.38,"MAE_180D_pct":-18.02,"peak_30D_date":"2024-07-29","trough_30D_date":"2024-08-05","peak_90D_date":"2024-08-26","trough_90D_date":"2024-08-05","peak_180D_date":"2024-08-26","trough_180D_date":"2025-01-02","profile_verdict":"positive","current_profile_error":false,"calibration_usable":true,"novelty":"new_C21_symbol; existing C21 representative symbols avoided","notes":"Bank-holding value-up case with explicit shareholder-return/ROE/CET1 bridge; MFE positive but not a vertical blowoff, so Stage2 is preferred to Green unless capital-return execution continues."}
{"row_type":"trigger","case_id":"C21_175330_JB_FINANCIAL_ROE_PBR_CAPITAL_RETURN_2024_10_25","symbol":"175330","name":"JB금융지주","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIGITAL_FINANCE_HIGH_PBR_FALSE_POSITIVE","trigger_type":"Stage2-Actionable","trigger_family":"regional_bank_high_roe_pbr_discount_capital_return_bridge","evidence_family":"regional_bank_ROE_PBR_capital_return","trigger_date":"2024-10-25","entry_date":"2024-10-25","entry_price":18290,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.26,"MAE_30D_pct":-5.3,"MFE_90D_pct":12.08,"MAE_90D_pct":-14.82,"MFE_180D_pct":12.08,"MAE_180D_pct":-14.82,"peak_30D_date":"2024-11-20","trough_30D_date":"2024-11-04","peak_90D_date":"2024-12-03","trough_90D_date":"2025-01-03","peak_180D_date":"2024-12-03","trough_180D_date":"2025-01-03","profile_verdict":"positive_with_high_MAE_watch","current_profile_error":false,"calibration_usable":true,"novelty":"new_C21_symbol; regional-bank capital-return bridge not in top repeated C21 symbols","notes":"Positive but slower and more volatile than large banks. Treat as Stage2 or Yellow candidate only when ROE persistence plus shareholder-return execution is visible; avoid Green based on low PBR alone."}
{"row_type":"trigger","case_id":"C21_377300_KAKAOPAY_DIGITAL_FINANCE_FALSE_STAGE2_2024_01_11","symbol":"377300","name":"카카오페이","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_DIGITAL_FINANCE_HIGH_PBR_FALSE_POSITIVE","trigger_type":"Stage2-FalsePositive","trigger_family":"digital_finance_high_pbr_no_ROE_no_capital_return_false_positive","evidence_family":"digital_finance_label_without_ROE_PBR_capital_return","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":58000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.79,"MAE_30D_pct":-21.9,"MFE_90D_pct":3.79,"MAE_90D_pct":-40.0,"MFE_180D_pct":3.79,"MAE_180D_pct":-55.0,"peak_30D_date":"2024-01-11","trough_30D_date":"2024-02-01","peak_90D_date":"2024-01-11","trough_90D_date":"2024-04-12","peak_180D_date":"2024-01-11","trough_180D_date":"2024-06-27","profile_verdict":"counterexample","current_profile_error":true,"calibration_usable":true,"novelty":"new_C21_symbol; digital-financial high-PBR label false-positive route","notes":"Digital finance/platform label is not C21 unless the case has actual ROE, low-PBR rerating logic, and cash capital return. This route should be capped as Stage2-FalsePositive or 4B watch after spike."}
```

## 8. Score / return alignment

```json
{
  "score_return_alignment": [
    {
      "symbol": "055550",
      "expected_stage": "Stage2-Actionable",
      "observed_path": "modest positive MFE with meaningful macro drawdown",
      "alignment": "good",
      "profile_implication": "Stage2 bridge should trigger before Green; Green requires continued capital-return execution."
    },
    {
      "symbol": "175330",
      "expected_stage": "Stage2-Actionable or Stage3-Yellow with high-MAE guard",
      "observed_path": "positive 90D/180D MFE but nontrivial MAE",
      "alignment": "mixed_positive",
      "profile_implication": "Regional bank rerating needs capital-return execution and credit/capital-buffer guard."
    },
    {
      "symbol": "377300",
      "expected_stage": "Stage2-FalsePositive",
      "observed_path": "low MFE, severe MAE",
      "alignment": "strong_counterexample",
      "profile_implication": "Digital-finance label should be blocked from C21 without ROE/PBR/capital-return bridge."
    }
  ]
}
```

## 9. Current calibrated profile stress test

```json
{
  "current_profile_error_count": 1,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "tested_rules": [
    "C21_stage2_required_ROE_PBR_capital_return_bridge",
    "C21_low_PBR_without_capital_return_stage2_block",
    "C21_digital_finance_high_PBR_false_positive_guard",
    "C21_regional_bank_high_MAE_guard"
  ],
  "rule_candidate": {
    "sector_specific_rule_candidate": false,
    "canonical_archetype_rule_candidate": true,
    "new_axis_proposed": null,
    "existing_axis_strengthened": [
      "C21_ROE_PBR_capital_return_execution_requirement",
      "C21_regional_bank_credit_capital_buffer_high_MAE_guard",
      "C21_digital_finance_label_without_cash_return_stage2_block"
    ],
    "existing_axis_weakened": []
  }
}
```

## 10. Residual contribution summary

```json
{
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "diversity_score_summary": "new_C21_symbol=3, new_trigger_family=3, positive/counterexample=2/1, digital-finance high-PBR false-positive guard=1",
  "do_not_propose_new_weight_delta": false,
  "auto_selected_coverage_gap": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN: rows=6, need_to_30=24, need_to_50=44",
  "sector_specific_rule_candidate": false,
  "canonical_archetype_rule_candidate": true,
  "new_axis_proposed": null,
  "existing_axis_strengthened": "C21_ROE_PBR_capital_return_execution_requirement; C21_regional_bank_credit_capital_buffer_high_MAE_guard; C21_digital_finance_label_without_cash_return_stage2_block",
  "existing_axis_weakened": null
}
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the research session. This section is for a later coding-agent batch ingest session.

```text
Read this MD as one v12 historical calibration artifact.

Ingest all JSONL rows under "JSONL trigger rows".
Validate that:
- selected_round == R6
- selected_loop == 110
- large_sector_id == L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
- canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
- price_source == Songdaiki/stock-web
- price_basis == tradable_raw
- price_adjustment_status == raw_unadjusted_marcap
- every trigger row has entry_date, entry_price, MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct

Do not change production scoring from this single artifact.
Use it only as shadow evidence for:
- C21_ROE_PBR_capital_return_execution_requirement
- C21_regional_bank_credit_capital_buffer_high_MAE_guard
- C21_digital_finance_label_without_cash_return_stage2_block
```

## 12. Final research state

```text
completed_round = R6
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
