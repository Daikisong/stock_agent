---
title: "E2R stock-web v12 residual research — R6 loop 88 — C21 financial ROE/PBR capital return"
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R6
scheduled_loop: 88
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUE_UP_CET1_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINTECH_BETA
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
---

# 1. Research intent

This R6 / Loop 88 file tests a narrow C21 residual: **Korea Value-up / low-PBR financial rally should not automatically become Stage2-Actionable unless it is tied to durable ROE, CET1/buffer, dividend or buyback-cancellation execution, and repeatable capital-return policy.**

The current batch corpus already contains many C21 rows, so the purpose here is not to re-prove the global Stage2-Actionable bonus. It is to add a cleaner split between:

- bank holding companies where low-PBR rerating had a shareholder-return bridge; and
- finance/fintech beta where the share price moved on low-PBR / policy sympathy but lacked enough capital-return evidence.

External context: South Korea’s Corporate Value-up Programme was proposed to address low domestic valuations and encourages companies to disclose plans around capital efficiency, shareholder returns, investment, and restructuring, but the scheme is voluntary and has been criticized for weak incentives. This makes C21 especially prone to false positives when the trigger is only “low PBR / value-up theme.”

# 2. Schedule and scope gate

```text
scheduled_round = R6
scheduled_loop = 88
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_schedule_status = valid
round_sector_consistency = pass
```

R6 maps to L6 financial / capital-return / digital-finance. This file does not use R13 cross-archetype naming and does not alter runtime scoring.

# 3. No-Repeat / novelty check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C21 already has heavy coverage in older bank/value-up names. The high-repeat C21 symbols in the No-Repeat index include `006220`, `016360`, `071050`, `105560`, `138040`, and `139130`, so this run avoids those and uses:

```text
086790 Hana Financial Group
316140 Woori Financial Group
323410 KakaoBank
```

Novelty intent:

```text
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 2
hard_duplicate_observed = false
useful_expansion = true
```

# 4. Stock-web profile validation

All three symbols are active-like tradable names with no corporate-action candidate contamination in the tested 2024 forward windows.

| symbol | name | profile first_date | profile last_date | corporate_action_candidate_count | 180D contamination |
|---|---|---:|---:|---:|---|
| 086790 | 하나금융지주 | 2005-12-12 | 2026-02-20 | 0 | none |
| 316140 | 우리금융지주 | 2019-02-13 | 2026-02-20 | 0 | none |
| 323410 | 카카오뱅크 | 2021-08-06 | 2026-02-20 | 0 | none |

Stock-web source rows used:

```text
atlas/symbol_profiles/086/086790.json
atlas/symbol_profiles/316/316140.json
atlas/symbol_profiles/323/323410.json
atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv
atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv
atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv
```

# 5. Case set

## 5.1 Case A — 086790 Hana Financial Group — positive Stage2 bridge

```text
symbol = 086790
company_name = 하나금융지주
trigger_type = Stage2-Actionable-CapitalReturnBridge
trigger_date = 2024-02-01
entry_date = 2024-02-02
entry_price = 54600
case_verdict = positive
```

Why selected:

- Bank holding company with direct sensitivity to value-up, capital return, and low-PBR rerating.
- Price reaction was not merely one-day policy beta; the path continued to higher highs into March and again into July-August.
- This is the “good C21” pattern: low-PBR financial rerating + shareholder-return expectation + actual bank profitability/ROE bridge.

Representative stock-web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-02,54600.0,55900.0,51200.0,55900.0,5363608.0,289495810850.0,16342733828200.0,292356598,KOSPI
2024-03-14,61400.0,64600.0,60600.0,64600.0,2422100.0,153573748642.0,18886236230800.0,292356598,KOSPI
2024-03-25,64300.0,65200.0,61900.0,62600.0,1318501.0,83036091600.0,18301523034800.0,292356598,KOSPI
2024-07-03,63900.0,67800.0,63200.0,64600.0,1800025.0,117587864700.0,18886236230800.0,292356598,KOSPI
2024-08-27,69100.0,69300.0,65700.0,66000.0,936115.0,62208052868.0,19295535468000.0,292356598,KOSPI
```

Price-path metrics from entry open 54,600:

| window | MFE high | MFE % | MAE low | MAE % | interpretation |
|---|---:|---:|---:|---:|---|
| D+30 | 64600 | +18.32% | 51200 | -6.23% | strong early confirmation |
| D+90 | 65200 | +19.41% | 51200 | -6.23% | just under +20 but with clean drawdown |
| D+180 | 69300 | +26.92% | 51200 | -6.23% | positive rerating path |

E2R interpretation:

```text
stage2_quality = good_stage2_near_threshold
stage3_green_candidate = conditional_only
4B_local_watch = false until > +30% or post-runup non-price evidence weakens
profile_error = false
```

## 5.2 Case B — 316140 Woori Financial Group — capital-buffer bridge not strong enough early

```text
symbol = 316140
company_name = 우리금융지주
trigger_type = Stage2-Watch-CapitalReturnBridgeInsufficient
trigger_date = 2024-02-01
entry_date = 2024-02-02
entry_price = 14530
case_verdict = counterexample_or_holdout
```

Why selected:

- Same broad low-PBR / value-up bank basket as Hana.
- However, the 2024 price path did not produce the same clean +20% forward confirmation from the early-February trigger.
- This makes Woori useful as a C21 guard: do not treat all bank holding companies identically; CET1, payout room, non-bank expansion risk, and capital buffer matter.

Representative stock-web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-02,14530.0,14840.0,14020.0,14710.0,6674144.0,96939159300.0,11061176571310.0,751949461,KOSPI
2024-02-07,14200.0,14620.0,13600.0,14500.0,4325703.0,62160055840.0,10903267184500.0,751949461,KOSPI
2024-03-15,15170.0,15500.0,15060.0,15230.0,5769346.0,87920600300.0,11452190291030.0,751949461,KOSPI
2024-04-03,13970.0,14000.0,13740.0,13760.0,2355836.0,32571037750.0,10346824583360.0,751949461,KOSPI
2024-07-29,16110.0,16960.0,16010.0,16330.0,10151683.0,167581804030.0,12126519211330.0,742591501,KOSPI
```

Price-path metrics from entry open 14,530:

| window | MFE high | MFE % | MAE low | MAE % | interpretation |
|---|---:|---:|---:|---:|---|
| D+30 | 15500 | +6.68% | 13600 | -6.40% | insufficient for good Stage2 |
| D+90 | 15500 | +6.68% | 13740 | -5.44% | low-vol but low-upside holdout |
| D+180 | 16960 | +16.72% | 13740 | -5.44% | positive but not structural rerating |

E2R interpretation:

```text
stage2_quality = weak_or_holdout
stage3_green_candidate = false
profile_error = true_if_promoted_as_green
suggested_guard = require CET1/payout/buyback-cancel bridge beyond generic bank value-up beta
```

## 5.3 Case C — 323410 KakaoBank — low-PBR / digital-bank sympathy false positive

```text
symbol = 323410
company_name = 카카오뱅크
trigger_type = Stage2-FalsePositive-LowPBRDigitalBankBeta
trigger_date = 2024-02-01
entry_date = 2024-02-02
entry_price = 27250
case_verdict = counterexample
```

Why selected:

- It is in the financial/digital universe, so it can be pulled into R6 value-up sympathy screens.
- However, C21 requires ROE/PBR and capital-return logic. KakaoBank’s 2024 path shows that digital-bank beta without bank-holdco-style capital-return execution can fade badly.
- This is the cleanest counterexample in the set.

Representative stock-web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-02,27250.0,29600.0,27150.0,29300.0,2664997.0,76876558350.0,13972353614100.0,476872137,KOSPI
2024-02-15,30350.0,31200.0,29800.0,29800.0,2148690.0,65253217100.0,14210789682600.0,476872137,KOSPI
2024-04-08,25450.0,25900.0,24800.0,25750.0,615157.0,15653924950.0,12280719277750.0,476921137,KOSPI
2024-06-27,20750.0,20900.0,20050.0,20250.0,1177800.0,23893765500.0,9657754274250.0,476926137,KOSPI
2024-08-05,21050.0,21050.0,18490.0,19180.0,2077299.0,40854847400.0,9147443307660.0,476926137,KOSPI
```

Price-path metrics from entry open 27,250:

| window | MFE high | MFE % | MAE low | MAE % | interpretation |
|---|---:|---:|---:|---:|---|
| D+30 | 31200 | +14.50% | 27150 | -0.37% | early theme pop |
| D+90 | 31200 | +14.50% | 20050 | -26.42% | failed conversion |
| D+180 | 31200 | +14.50% | 18490 | -32.15% | high-MAE false positive |

E2R interpretation:

```text
stage2_quality = bad_stage2
stage3_green_candidate = false
4C_watch = if thesis was digital bank rerating without capital return bridge
profile_error = true_if_promoted_as_C21_positive
```

# 6. Machine-readable usable trigger rows

```jsonl
{"row_type":"trigger","scheduled_round":"R6","scheduled_loop":88,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUE_UP_CET1_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINTECH_BETA","symbol":"086790","company_name":"하나금융지주","trigger_type":"Stage2-Actionable-CapitalReturnBridge","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":54600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.32,"mae_30d_pct":-6.23,"mfe_90d_pct":19.41,"mae_90d_pct":-6.23,"mfe_180d_pct":26.92,"mae_180d_pct":-6.23,"case_verdict":"positive","calibration_usable":true,"corporate_action_contaminated":false,"do_not_count_as_new_case":false,"current_profile_error":false,"evidence_family":"value_up_bank_capital_return_bridge"}
{"row_type":"trigger","scheduled_round":"R6","scheduled_loop":88,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUE_UP_CET1_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINTECH_BETA","symbol":"316140","company_name":"우리금융지주","trigger_type":"Stage2-Watch-CapitalReturnBridgeInsufficient","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":14530,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.68,"mae_30d_pct":-6.40,"mfe_90d_pct":6.68,"mae_90d_pct":-5.44,"mfe_180d_pct":16.72,"mae_180d_pct":-5.44,"case_verdict":"counterexample_or_holdout","calibration_usable":true,"corporate_action_contaminated":false,"do_not_count_as_new_case":false,"current_profile_error":true,"evidence_family":"bank_value_up_without_strong_capital_buffer_bridge"}
{"row_type":"trigger","scheduled_round":"R6","scheduled_loop":88,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUE_UP_CET1_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINTECH_BETA","symbol":"323410","company_name":"카카오뱅크","trigger_type":"Stage2-FalsePositive-LowPBRDigitalBankBeta","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":27250,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":14.50,"mae_30d_pct":-0.37,"mfe_90d_pct":14.50,"mae_90d_pct":-26.42,"mfe_180d_pct":14.50,"mae_180d_pct":-32.15,"case_verdict":"counterexample","calibration_usable":true,"corporate_action_contaminated":false,"do_not_count_as_new_case":false,"current_profile_error":true,"evidence_family":"digital_bank_value_up_sympathy_without_capital_return_bridge"}
```

# 7. Raw component score breakdown

Component scores are historical research approximations, not runtime production changes.

| symbol | EPS/FCF Explosion | Earnings Visibility | Bottleneck/Pricing | Market Mispricing | Valuation Rerating | Capital Allocation | Info Confidence | total proxy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 086790 | 11 | 16 | 4 | 14 | 14 | 5 | 4 | 68 |
| 316140 | 9 | 13 | 3 | 13 | 11 | 3 | 4 | 56 |
| 323410 | 7 | 10 | 2 | 10 | 7 | 1 | 3 | 40 |

Interpretation:

```text
086790 = Stage2-Actionable but Green requires explicit shareholder-return execution / CET1 bridge.
316140 = Watch; value-up beta exists, but score should not cross Stage2-Actionable without stronger capital-return bridge.
323410 = False-positive; digital-bank sympathy is not equivalent to C21 capital-return rerating.
```

# 8. Residual contribution summary

```text
new_independent_case_count = 3
same_archetype_new_symbol_count = 3
positive_case_count = 1
counterexample_count = 2
local_4b_overlay_case_count = 0
hard_4c_case_count = 0
calibration_usable_case_count = 3
current_profile_error_count = 2
loop_contribution_label = residual_error_found
do_not_propose_new_weight_delta = true
```

Residual rule candidate:

```text
For C21, low-PBR / Korea Value-up / financial beta can open Watch.
It should become Stage2-Actionable only when at least one of the following is concrete:
  1. explicit dividend / buyback-cancellation / shareholder-return policy;
  2. CET1 or capital buffer sufficient to fund payout without weakening balance sheet;
  3. ROE or NIM / credit-cost visibility that supports sustained valuation rerating;
  4. evidence that the institution is a bank-holdco capital-return compounder, not just digital-finance sympathy beta.
```

Do not promote this to global weight delta yet. The safe use is a C21 bridge/guard note.

# 9. Deferred Coding Agent Handoff Prompt

Do not execute now.

```text
You are a coding agent maintaining Songdaiki/stock_agent.
Read this MD as one v12 historical calibration artifact only.
Do not change production scoring globally.
If batch-applying, parse the JSONL trigger rows and consider a C21-specific guard:
  - Stage2-Actionable for C21 requires explicit capital-return / CET1 / ROE bridge.
  - Digital-bank or low-PBR sympathy without payout evidence remains Watch or FalsePositiveCandidate.
  - Use 086790 as positive support and 316140/323410 as counterexample support.
Keep production_scoring_changed=false unless a later batch promotion planner approves it.
```

# 10. Final round state

```text
completed_round = R6
completed_loop = 88
next_round = R7
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
