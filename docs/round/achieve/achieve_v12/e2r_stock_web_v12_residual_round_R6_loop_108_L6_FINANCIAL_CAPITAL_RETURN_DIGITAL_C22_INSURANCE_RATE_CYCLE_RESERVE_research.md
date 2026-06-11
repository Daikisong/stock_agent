# E2R v12 residual calibration research — C22_INSURANCE_RATE_CYCLE_RESERVE

```text
file_name = e2r_stock_web_v12_residual_round_R6_loop_108_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R6
selected_loop = 108
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_INSURANCE_VALUEUP_RESERVE_CAPITAL_POLICY_BRIDGE_VS_GA_DISTRIBUTION_LABEL_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Execution guardrail

This file is a standalone historical calibration / sector-archetype residual research artifact. It is not a live stock recommendation, not a watchlist, not a broker/API task, and not a production scoring patch.

The only price source used for MFE/MAE is `Songdaiki/stock-web` under `atlas/ohlcv_tradable_by_symbol_year`. The price basis is raw/unadjusted FinanceData/marcap-derived OHLCV, so corporate-action-contaminated windows are blocked unless a local window ends before the corporate-action candidate date.

## 2. Coverage and duplicate-avoidance rationale

`C22_INSURANCE_RATE_CYCLE_RESERVE` remains in the Priority 1 coverage-gap list with 42 rows and 8 rows needed to reach the 50-row practical calibration target.

Already-used C22 case families avoided in this run:

- large non-life insurers: Samsung Fire, DB Insurance, Hyundai Marine
- non-life/value-up small insurers: Meritz Financial, Hanwha General Insurance, Heungkuk Fire, Lotte Non-Life
- life/reinsurance: Samsung Life, Hanwha Life, Korean Re, Mirae Asset Life

This run adds a new direct life-insurer case plus two insurance-distribution / GA boundary cases:

1. Dongyang Life — direct life insurer value-up / capital-policy path.
2. A Plus Asset — GA / insurance sales-distribution label boundary.
3. Incar Financial Service — GA / insurance sales-distribution label with corporate-action full-window block.

## 3. Common trigger spine

```text
trigger_family = Korea Corporate Value-up / shareholder-return follow-up
trigger_date = 2024-02-28 / 2024-02-29
external_source_proxy = Reuters, 2024-02-28, South Korea considering penalties on firms failing to boost shareholder return
calibration_entry_rule = next available stock-web close on or immediately after trigger
primary_entry_date = 2024-02-29
```

Why this belongs in C22:

- Insurance names are repeatedly pulled into the value-up / capital return trade because balance-sheet-heavy insurers can look like low-PBR, capital-return candidates.
- C22 should not award points simply for the word "insurance."
- For direct insurers, the missing bridge is reserve quality, solvency, rate cycle, shareholder-return execution, and capital policy.
- For GA / insurance agency / distribution businesses, the missing bridge is even more basic: they are sales-channel intermediaries, not underwriting reserve-cycle vehicles.

## 4. Case table

| case_id | symbol | name | role | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | calibration_status |
|---|---:|---|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C22_R6L108_082640_20240229 | 082640 | Dongyang Life | direct life-insurer positive, high-MAE watch | 2024-02-28 | 2024-02-29 | 5,820 | 2024-07-02 | 9,340 | 2024-12-23 | 4,430 | +60.48% | -23.88% | usable_positive_high_MAE |
| C22_R6L108_244920_20240229 | 244920 | A Plus Asset | GA/distribution boundary, no reserve bridge | 2024-02-28 | 2024-02-29 | 4,040 | 2024-12-03 | 4,840 | 2024-04-19 | 3,700 | +19.80% | -8.42% | usable_boundary_false_positive_watch |
| C22_R6L108_211050_20240229 | 211050 | Incar Financial Service | GA/distribution local window, full-window blocked | 2024-02-28 | 2024-02-29 | 19,390 | 2024-04-12 | 24,600 | 2024-02-29 | 18,300 | +26.87% | -5.62% | local_window_usable_full_window_blocked |

## 5. Case notes

### 5.1 Dongyang Life — direct life-insurer value-up positive, but high-MAE

**Stock-web identity and caveat**

```text
symbol = 082640
name = 동양생명
market = KOSPI
corporate_action_candidate_dates = 2017-04-11
2024 trigger window = not corporate-action contaminated
```

**Price path**

```text
entry_date = 2024-02-29
entry_close = 5,820
peak_date = 2024-07-02
peak_high = 9,340
trough_date = 2024-12-23
trough_low = 4,430
MFE = +60.48%
MAE = -23.88%
```

**Interpretation**

Dongyang Life behaves like a true C22 candidate because it is a listed life insurer, not merely an insurance-sales distributor. The path from `5,820` to `9,340` shows that the value-up / capital-policy trade could work outside the already-used Samsung Life / Hanwha Life / Mirae Asset Life set.

However, the later fall to `4,430` is too large to allow automatic Stage3-Green promotion. C22 needs a reserve-quality and capital-policy execution bridge. The correct classification is:

```text
Stage2-Actionable watch = possible
Stage3-Yellow = only if reserve/solvency/shareholder-return evidence is present
Stage3-Green = not allowed from value-up label alone
4B watch = yes, because full-window drawdown is material
```

### 5.2 A Plus Asset — GA/distribution boundary, not reserve-cycle insurer

**Stock-web identity and caveat**

```text
symbol = 244920
name = 에이플러스에셋
market = KOSPI
corporate_action_candidate_dates = []
2024 trigger window = clean
```

**Price path**

```text
entry_date = 2024-02-29
entry_close = 4,040
peak_date = 2024-12-03
peak_high = 4,840
trough_date = 2024-04-19
trough_low = 3,700
MFE = +19.80%
MAE = -8.42%
```

**Interpretation**

A Plus Asset can be pulled into an "insurance" or "financial product sales" bucket, but it is structurally different from the C22 underwriting reserve-cycle target. It is closer to a GA / financial sales channel. That business can have earnings momentum, but its mechanism is not insurance-rate cycle, reserve quality, solvency relief, or capital return from an underwriting balance sheet.

The price path had a moderate MFE, but the right residual lesson is not "score all insurance distributors." The right rule is:

```text
GA / insurance sales-distribution label alone = not C22 positive
C22 reserve/rate-cycle score = 0 unless the company itself underwrites insurance risk
Possible separate archetype = financial product distribution / GA operating leverage
```

### 5.3 Incar Financial Service — GA/distribution local positive, full-window blocked

**Stock-web identity and caveat**

```text
symbol = 211050
name = 인카금융서비스
market_history = KONEX -> KOSDAQ
corporate_action_candidate_dates = 2018-07-18, 2022-06-22, 2022-07-13, 2024-04-29
2024-02-29 entry to 2024-04-12 local window = usable
full-window after 2024-04-29 = blocked by corporate-action candidate
```

**Price path**

```text
entry_date = 2024-02-29
entry_close = 19,390
local_peak_date = 2024-04-12
local_peak_high = 24,600
local_trough_date = 2024-02-29
local_trough_low = 18,300
local_MFE = +26.87%
local_MAE = -5.62%
full_window_status = blocked_after_2024-04-29_corporate_action_candidate
```

**Interpretation**

This is the more dangerous GA boundary case. A naive classifier can see "insurance service" and give C22 credit. The local price path before the corporate-action candidate date also looks strong. But the mechanism is not underwriting reserve quality. It is insurance sales/distribution, and full-window calibration is blocked by the stock-web corporate-action candidate.

The correct treatment is:

```text
usable local price-path stress row = yes
full-window MFE/MAE = blocked
C22 positive score = no direct reserve-cycle score
classification = GA distribution label false-positive / separate archetype candidate
```

## 6. Residual profile error

The current calibrated profile can still make three related errors:

1. It can over-score life insurers on value-up labels without reserve-quality, solvency, and capital-return execution evidence.
2. It can mistake insurance-sales / GA companies for underwriting insurers.
3. It can ignore corporate-action contamination after local GA rallies.

The mechanism is the difference between an insurer and a broker.
An insurer is like a reservoir: rate cycle, reserve quality, solvency, and capital policy determine how much water can safely be released to shareholders. A GA / insurance agency is more like the canal gatekeeper: it can earn tolls on flow, but it does not own the reservoir risk. C22 should score the reservoir, not just the gate.

## 7. Proposed shadow rule

```text
rule_id = c22_underwriting_reserve_capital_policy_bridge_required_vs_ga_distribution_label
scope = C22_INSURANCE_RATE_CYCLE_RESERVE
status = shadow_only
production_scoring_changed = false

positive_requirements:
  - company is a direct insurer or reinsurer
  - identifiable underwriting reserve / solvency / rate-cycle exposure
  - capital return or capital policy bridge exists
  - shareholder-return/value-up headline is supported by insurer-specific evidence

penalties:
  - insurance sales agency / GA / broker / distributor without underwriting risk => C22 score capped at Stage1/Stage2 watch
  - value-up label only, no reserve/capital bridge => no Stage3-Green
  - local rally followed by corporate-action candidate => full-window blocked or narrative-only
  - high-MAE after value-up headline => force 4B watch unless later evidence repairs thesis
```

## 8. Machine-readable rows

### 8.1 case rows

```jsonl
{"row_type":"case","case_id":"C22_R6L108_082640_20240229","symbol":"082640","name":"Dongyang Life","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_RESERVE_CAPITAL_POLICY_BRIDGE","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":5820,"peak_date":"2024-07-02","peak_high":9340,"trough_date":"2024-12-23","trough_low":4430,"mfe_pct":60.48,"mae_pct":-23.88,"classification":"positive_high_MAE_watch","calibration_usable":true,"full_window_blocked":false}
{"row_type":"case","case_id":"C22_R6L108_244920_20240229","symbol":"244920","name":"A Plus Asset","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_INSURANCE_DISTRIBUTION_LABEL_BOUNDARY","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":4040,"peak_date":"2024-12-03","peak_high":4840,"trough_date":"2024-04-19","trough_low":3700,"mfe_pct":19.80,"mae_pct":-8.42,"classification":"ga_distribution_boundary_false_positive_watch","calibration_usable":true,"full_window_blocked":false}
{"row_type":"case","case_id":"C22_R6L108_211050_20240229","symbol":"211050","name":"Incar Financial Service","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_INSURANCE_DISTRIBUTION_LOCAL_RALLY_CORPORATE_ACTION_BLOCK","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":19390,"peak_date":"2024-04-12","peak_high":24600,"trough_date":"2024-02-29","trough_low":18300,"mfe_pct":26.87,"mae_pct":-5.62,"classification":"local_window_usable_full_window_blocked","calibration_usable":true,"full_window_blocked":true,"corporate_action_candidate_date":"2024-04-29"}
```

### 8.2 score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C22_R6L108_082640_20240229","old_behavior":"value_up_life_insurer_label_may_upgrade_too_fast","new_behavior":"require_reserve_solvency_capital_policy_bridge_before_stage3_green","expected_effect":"reduce_high_MAE_green_false_positive"}
{"row_type":"score_simulation","case_id":"C22_R6L108_244920_20240229","old_behavior":"insurance_related_distribution_company_can_be_misread_as_insurer","new_behavior":"GA_distribution_without_underwriting_risk_gets_no_C22_reserve_score","expected_effect":"reduce_business_model_false_positive"}
{"row_type":"score_simulation","case_id":"C22_R6L108_211050_20240229","old_behavior":"local_GA_rally_can_inflate_C22_score","new_behavior":"use_only_local_window_before_corporate_action_and_block_full_window","expected_effect":"prevent_split_contaminated_MFE_MAE"}
```

### 8.3 aggregate row

```jsonl
{"row_type":"aggregate","selected_round":"R6","selected_loop":108,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"calibration_usable_case_count":3,"positive_case_count":1,"boundary_false_positive_count":2,"full_window_blocked_count":1,"current_profile_error_count":3,"verified_url_repair_needed_count":2}
```

### 8.4 shadow weight row

```jsonl
{"row_type":"shadow_weight","rule_id":"c22_underwriting_reserve_capital_policy_bridge_required_vs_ga_distribution_label","scope":"C22_INSURANCE_RATE_CYCLE_RESERVE","production_scoring_changed":false,"proposed_change":"Cap non-underwriting GA/insurance-distribution labels below Stage2-Actionable for C22 unless direct underwriting reserve/capital-policy evidence exists; direct life insurers still require reserve/solvency/capital-return bridge before Stage3-Green.","target_error":"insurance_label_false_positive_and_high_MAE_valueup_rally"}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not rerun live scans. Read this MD as a historical residual calibration artifact only.

Implement no immediate production score changes unless batch review approves. Convert the following shadow-only finding into a candidate rule in the C22 calibration review queue:

Rule candidate:
- ID: c22_underwriting_reserve_capital_policy_bridge_required_vs_ga_distribution_label
- Scope: C22_INSURANCE_RATE_CYCLE_RESERVE
- If company is direct insurer/reinsurer, require insurer-specific evidence of reserve quality, solvency, rate cycle, and capital return policy before Stage3-Green.
- If company is GA/insurance agency/broker/distribution business without underwriting reserve risk, cap C22 score below Stage2-Actionable and consider separate archetype routing.
- If price window crosses stock-web corporate-action candidate, block full-window MFE/MAE or mark narrative-only.

Cases:
- 082640 Dongyang Life: direct life-insurer value-up positive with high-MAE watch.
- 244920 A Plus Asset: GA / insurance distribution boundary false positive.
- 211050 Incar Financial Service: GA local rally with 2024-04-29 corporate-action full-window block.

Do not alter production scoring until this rule is reviewed alongside other C22 residual MDs.
```

## 10. Final summary metadata

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable case 수 = 3
calibration_usable trigger 수 = 3
positive_case_count = 1
boundary_false_positive_count = 2
counterexample_count = 2
full_window_blocked_count = 1
current_profile_error_count = 3
verified_url_repair_needed_count = 2

diversity_score_summary = C22 Priority 1 보강 + 동양생명 direct life-insurer high-MAE positive + A Plus Asset GA/distribution boundary + Incar Financial Service local GA rally/full-window corporate-action block
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C22 rows 42, 50-row target까지 8 부족
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c22_underwriting_reserve_capital_policy_bridge_required_vs_ga_distribution_label
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C22 insurance/value-up/rate-cycle rallies
existing_axis_weakened = null
next_recommended_archetypes = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```
