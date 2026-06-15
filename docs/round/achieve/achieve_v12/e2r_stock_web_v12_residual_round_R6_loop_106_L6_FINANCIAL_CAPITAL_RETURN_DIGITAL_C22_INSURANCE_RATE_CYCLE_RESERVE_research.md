# e2r stock-web v12 residual research — R6 / L6 / C22

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R6
selected_loop = 106
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_AND_REINSURANCE_VALUEUP_RATE_RESERVE_CAPITAL_POLICY_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE
output = one_standalone_markdown_file
stock_agent_code_access = false
stock_agent_code_patch = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Execution boundary

This file is a standalone historical calibration / sector-archetype residual research artifact.
It is not a live scan, not a recommendation list, not a trading signal, and not a code patch.

The execution followed the v12 constraint that only `Songdaiki/stock-web` price rows are used for OHLC path measurement. `stock_agent` code is not opened or inferred. The `stock_agent` No-Repeat Index is used only as a coverage and duplicate-avoidance ledger.

## 2. Selection rationale

`C22_INSURANCE_RATE_CYCLE_RESERVE` remains in Priority 1 according to the No-Repeat Index snapshot:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE | rows = 42 | need_to_50 = 8
조사 포인트 = 보험 rate cycle, reserve quality, capital return
```

Prior C22 work already used the non-life insurer set:

```text
000810 삼성화재
005830 DB손해보험
001450 현대해상
138040 메리츠금융지주
000370 한화손해보험
000540 흥국화재
000400 롯데손해보험
```

This loop therefore extends C22 into life insurance and reinsurance without reusing those previous C22 symbols:

```text
032830 삼성생명
088350 한화생명
003690 코리안리
085620 미래에셋생명
```

The goal is to test whether the same "insurance / value-up / capital return" label survives when moved from non-life insurers into life insurers and reinsurance. This matters because C22 is not supposed to reward a sector tag alone. It should reward the actual bridge:

```text
rate cycle + reserve quality + solvency/capital policy + shareholder-return execution
```

## 3. Price source

```text
price_repo = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

Source shard examples:

```text
atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv
atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv
atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv
```

## 4. External event spine

Primary historical trigger:

```text
trigger_date = 2024-02-28
event = Korea Corporate Value-up Programme follow-up / shareholder-return pressure
source = Reuters, 2024-02-28
secondary_source = Reuters, 2024-03-14 follow-up acceleration and bolder measures discussion
```

Interpretation for C22:

The event is not an insurer-specific earnings revision by itself. It is a policy/capital-return pressure event that can become C22-positive only when the insurer has enough reserve quality, solvency visibility, capital return credibility, and earnings persistence. Otherwise, the model should treat it as a broad financial/value-up sympathy label and demote to Stage2-watch or 4C.

## 5. Case summary table

| case_id | symbol | name | trigger_date | entry_date | entry_close | peak_date | peak_high | trough_date | trough_low | MFE | MAE | label |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C22_R6_L106_001 | 032830 | 삼성생명 | 2024-02-28 | 2024-02-29 | 96,900 | 2024-11-18 | 111,000 | 2024-04-19 | 76,600 | +14.55% | -20.95% | high-MAE positive watch |
| C22_R6_L106_002 | 088350 | 한화생명 | 2024-02-28 | 2024-02-29 | 3,150 | 2024-03-15 | 3,345 | 2024-12-17 | 2,440 | +6.19% | -22.54% | low-MFE/high-MAE counterexample |
| C22_R6_L106_003 | 003690 | 코리안리 | 2024-02-28 | 2024-02-29 | 8,040 | 2024-11-05 | 9,550 | 2024-04-12 | 7,600 | +18.78% | -5.47% | reinsurance positive with share-count caveat |
| C22_R6_L106_004 | 085620 | 미래에셋생명 | 2024-02-28 | 2024-02-29 | 4,880 | 2024-06-27 | 6,140 | 2024-03-29 | 4,445 | +25.82% | -8.91% | delayed positive / liquidity watch |

Formula:

```text
MFE% = (post_entry_peak_high - entry_close) / entry_close * 100
MAE% = (post_entry_trough_low - entry_close) / entry_close * 100
```

## 6. Case notes

### 6.1 C22_R6_L106_001 — 삼성생명 / high-MAE positive watch

```text
symbol = 032830
entry_date = 2024-02-29
entry_close = 96,900
post_entry_peak_high = 111,000 on 2024-11-18
post_entry_trough_low = 76,600 on 2024-04-19
MFE = +14.55%
MAE = -20.95%
```

삼성생명은 life-insurer value-up candidate로 볼 수 있지만, entry 이후 path가 깨끗하지 않다. 2024-02-29 entry close 96,900 이후 2024-11-18 high 111,000까지는 올라갔으나, 중간에 2024-04-19 low 76,600까지 밀렸다. 이것은 C22에서 "대형 생보 + value-up"만으로 Stage3-Green을 주면 안 된다는 증거다.

C22 positive로 보려면 단순 PBR/금융주 라벨이 아니라 다음의 bridge가 필요하다.

```text
capital policy visibility
reserve / solvency quality
sustainable shareholder return
earnings quality under rate-cycle conditions
```

Recommended scoring treatment:

```text
Stage2-Actionable 가능
Stage3-Yellow 조건부 가능
Stage3-Green 자동승격 금지
4B watch 필요
```

### 6.2 C22_R6_L106_002 — 한화생명 / life-insurance value-up label counterexample

```text
symbol = 088350
entry_date = 2024-02-29
entry_close = 3,150
post_entry_peak_high = 3,345 on 2024-03-15
post_entry_trough_low = 2,440 on 2024-12-17
MFE = +6.19%
MAE = -22.54%
```

한화생명은 same-sector sympathy가 약하게 작동했지만 C22 품질점수로 승격하기 어려운 반례다. Entry 이후 MFE는 +6.19%에 그쳤고, 이후 -22.54% MAE가 발생했다. 이 케이스는 life-insurance balance-sheet / capital policy / reserve quality 확인 없이 "보험 + value-up"을 긍정 점수로 넣으면 residual error가 난다는 것을 보여준다.

Recommended scoring treatment:

```text
Stage2 이하
Stage2-Actionable 제한
Stage3 reject
4C-prone label false positive
```

### 6.3 C22_R6_L106_003 — 코리안리 / reinsurance positive with share-count caveat

```text
symbol = 003690
entry_date = 2024-02-29
entry_close = 8,040
post_entry_peak_high = 9,550 on 2024-11-05
post_entry_trough_low = 7,600 on 2024-04-12
MFE = +18.78%
MAE = -5.47%
```

코리안리는 손보/생보와 다른 reinsurance book이다. 같은 C22 안에서도 pure life-insurer value-up sympathy와 구분해야 한다. Entry 이후 peak까지의 path는 relatively clean했고, MAE도 -5.47%로 제한적이었다. 따라서 C22 positive로 사용할 수 있다.

다만 2024-11-25 이후 stock-web row에서 share-count field가 바뀌는 구간이 보이므로, peak 측정은 2024-11-05 local peak까지만 사용하고, 이후 full-window extrapolation은 narrative-only caveat로 둔다.

Recommended scoring treatment:

```text
Stage2-Actionable 가능
Stage3-Yellow 조건부 가능
Stage3-Green은 reserve / combined-ratio / capital-return evidence 추가 필요
post-2024-11-25 share-count shifted window = narrative caveat
```

### 6.4 C22_R6_L106_004 — 미래에셋생명 / delayed positive with liquidity watch

```text
symbol = 085620
entry_date = 2024-02-29
entry_close = 4,880
post_entry_peak_high = 6,140 on 2024-06-27
post_entry_trough_low = 4,445 on 2024-03-29
MFE = +25.82%
MAE = -8.91%
```

미래에셋생명은 delayed-positive case다. Entry 직후에는 4,445까지 밀렸지만, 6월에 6,140 high까지 올라 MFE +25.82%를 만들었다. 이 케이스는 broad value-up sympathy가 무조건 실패하는 것은 아니지만, liquidity / capital policy / actual shareholder-return evidence를 확인해야 한다는 쪽이다.

Recommended scoring treatment:

```text
Stage2 가능
Stage2-Actionable 조건부 가능
Stage3-Yellow는 capital policy confirmation 필요
Stage3-Green 자동승격 금지
```

## 7. Residual diagnosis

Current calibrated profile likely residual errors:

```text
error_1 = 보험 섹터 라벨만 보고 C22를 과가점하는 경우
error_2 = 생보/손보/재보험을 같은 보험 bucket으로 뭉개는 경우
error_3 = value-up policy headline을 실제 capital-return execution으로 오인하는 경우
error_4 = high-MAE positive를 Green-quality positive로 착각하는 경우
```

C22 should behave like an underwriting machine, not like a banner. A banner says "insurance". The machine asks: "Is the capital actually returnable, and are reserve/loss/solvency conditions durable enough for that return?"

## 8. Shadow rule candidate

### 8.1 New axis

```text
axis_id = c22_life_reinsurance_reserve_quality_capital_policy_bridge_required_for_stage2_actionable_shadow_only
scope = C22_INSURANCE_RATE_CYCLE_RESERVE
production_change_now = false
shadow_weight_only = true
```

Rule:

```text
For C22, do not upgrade from broad insurance/value-up sympathy to Stage2-Actionable or Stage3 unless at least one of the following bridge evidences is present:

1. explicit shareholder-return policy / dividend / buyback / payout-ratio improvement
2. reserve quality or solvency-ratio improvement
3. rate-cycle improvement tied to underwriting or spread margin
4. recurrent earnings improvement after IFRS17/CSM/reserve normalization
5. reinsurance pricing / loss-cycle improvement with capital return visibility
```

Negative filters:

```text
- "insurance" sector tag only
- value-up headline only
- low PBR / financial-stock sympathy only
- one-day policy spike without capital-policy evidence
- life-insurer rally without solvency / reserve / shareholder-return confirmation
```

### 8.2 Strengthen existing 4B / 4C handling

```text
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C22 insurance value-up/rate-cycle rallies
```

If MFE is positive but MAE exceeds roughly -15% before durable continuation, classify as:

```text
positive_with_high_MAE_watch
not Green-quality positive
```

If MFE < +8% and MAE < -20%, classify as:

```text
C22 label false positive
4C-prone residual
```

## 9. Machine-readable rows

### 9.1 case rows

```jsonl
{"row_type":"case","case_id":"C22_R6_L106_001","round":"R6","loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_REINSURANCE_VALUEUP_RATE_RESERVE_CAPITAL_POLICY_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE","symbol":"032830","name":"삼성생명","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":96900,"peak_date":"2024-11-18","peak_high":111000,"trough_date":"2024-04-19","trough_low":76600,"mfe_pct":14.55,"mae_pct":-20.95,"classification":"high_MAE_positive_watch","calibration_usable":true,"source_price_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv"}
{"row_type":"case","case_id":"C22_R6_L106_002","round":"R6","loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_REINSURANCE_VALUEUP_RATE_RESERVE_CAPITAL_POLICY_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE","symbol":"088350","name":"한화생명","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":3150,"peak_date":"2024-03-15","peak_high":3345,"trough_date":"2024-12-17","trough_low":2440,"mfe_pct":6.19,"mae_pct":-22.54,"classification":"low_MFE_high_MAE_counterexample","calibration_usable":true,"source_price_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv"}
{"row_type":"case","case_id":"C22_R6_L106_003","round":"R6","loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_REINSURANCE_VALUEUP_RATE_RESERVE_CAPITAL_POLICY_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE","symbol":"003690","name":"코리안리","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":8040,"peak_date":"2024-11-05","peak_high":9550,"trough_date":"2024-04-12","trough_low":7600,"mfe_pct":18.78,"mae_pct":-5.47,"classification":"reinsurance_positive_with_share_count_caveat","calibration_usable":true,"source_price_path":"atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv"}
{"row_type":"case","case_id":"C22_R6_L106_004","round":"R6","loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_REINSURANCE_VALUEUP_RATE_RESERVE_CAPITAL_POLICY_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE","symbol":"085620","name":"미래에셋생명","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":4880,"peak_date":"2024-06-27","peak_high":6140,"trough_date":"2024-03-29","trough_low":4445,"mfe_pct":25.82,"mae_pct":-8.91,"classification":"delayed_positive_liquidity_watch","calibration_usable":true,"source_price_path":"atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv"}
```

### 9.2 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C22_VALUEUP_2024_02_28","trigger_date":"2024-02-28","trigger_family":"korea_valueup_shareholder_return_pressure","source_url":"https://www.reuters.com/markets/asia/skorea-considering-penalties-firms-failing-boost-shareholder-return-2024-02-28/","expected_bridge":"capital_return_policy_reserve_quality_solvent_distribution_capacity","applies_to_cases":["C22_R6_L106_001","C22_R6_L106_002","C22_R6_L106_003","C22_R6_L106_004"]}
{"row_type":"trigger","trigger_id":"C22_VALUEUP_FOLLOWUP_2024_03_14","trigger_date":"2024-03-14","trigger_family":"valueup_followup_acceleration_bolder_measures","source_url":"https://www.reuters.com/markets/asia/south-korea-regulator-speed-up-corporate-reforms-eyes-bold-measures-2024-03-14/","expected_bridge":"tax_incentive_stewardship_index_policy_pressure_but_not_company_specific_execution","applies_to_cases":["C22_R6_L106_001","C22_R6_L106_002","C22_R6_L106_003","C22_R6_L106_004"]}
```

### 9.3 score simulation row

```jsonl
{"row_type":"score_simulation","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","baseline_problem":"insurance_or_valueup_label_can_overpromote_life_insurers_without_reserve_or_capital_policy_bridge","proposed_shadow_axis":"c22_life_reinsurance_reserve_quality_capital_policy_bridge_required_for_stage2_actionable_shadow_only","stage2_actionable_condition":"explicit capital return or reserve/solvency/rate-cycle bridge","stage3_yellow_condition":"capital return plus earnings/reserve quality confirmation","stage3_green_condition":"durable post-entry path with limited MAE and verified capital policy execution","negative_condition":"low-MFE/high-MAE value-up sympathy or life-insurance label only","production_change_now":false}
```

### 9.4 aggregate row

```jsonl
{"row_type":"aggregate","round":"R6","loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_REINSURANCE_VALUEUP_RATE_RESERVE_CAPITAL_POLICY_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"positive_case_count":3,"counterexample_count":1,"current_profile_error_count":3,"verified_url_repair_needed_count":1}
```

### 9.5 shadow weight row

```jsonl
{"row_type":"shadow_weight","axis_id":"c22_life_reinsurance_reserve_quality_capital_policy_bridge_required_for_stage2_actionable_shadow_only","scope":"C22_INSURANCE_RATE_CYCLE_RESERVE","suggested_effect":"demote insurance/value-up label-only cases; allow Stage2-Actionable only with reserve/solvency/capital policy bridge; prevent high-MAE positives from becoming Green","production_change_now":false}
```

### 9.6 residual contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":106,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c22_life_reinsurance_reserve_quality_capital_policy_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C22 insurance value-up/rate-cycle rallies","existing_axis_weakened":null}
```

### 9.7 narrative-only / caveat row

```jsonl
{"row_type":"narrative_only","symbol":"003690","name":"코리안리","reason":"stock-web row shows share-count field change after 2024-11-25; pre-2024-11-05 peak used for MFE; post-shift full-window extension not used for calibration","calibration_usable":false,"source_price_path":"atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv"}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not re-run research. Do not browse for live candidates. Use this Markdown only as a batch calibration artifact.

Task:
- Ingest the machine-readable JSONL rows in this MD.
- Add the cases to the v12 calibration registry if and only if no duplicate exists under:
  canonical_archetype_id + symbol + trigger_type + entry_date
- Treat all weight changes as shadow-only.
- Do not change production scoring immediately.
- Add or update a shadow axis candidate:
  c22_life_reinsurance_reserve_quality_capital_policy_bridge_required_for_stage2_actionable_shadow_only
- Preserve the classification distinction:
  high_MAE_positive_watch != Green-quality positive
  low_MFE_high_MAE_counterexample != neutral
  reinsurance_positive_with_share_count_caveat != full-window clean positive
- Respect the narrative-only caveat for 003690 post-2024-11-25 share-count shifted window.
- After batch ingestion, report:
  new rows added
  duplicates skipped
  rejected rows
  affected archetype coverage count
  shadow rule candidates created/updated
```

## 11. Final run summary

```text
이번 라운드: R6 / Loop 106 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_round: R6
selected_loop: 106
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_AND_REINSURANCE_VALUEUP_RATE_RESERVE_CAPITAL_POLICY_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE

new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable case 수: 4
calibration_usable trigger 수: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 3
verified_url_repair_needed_count: 1

diversity_score_summary: C22 Priority 1 보강 + 삼성생명 high-MAE positive watch + 한화생명 low-MFE/high-MAE counterexample + 코리안리 reinsurance positive with share-count caveat + 미래에셋생명 delayed positive/liquidity watch
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C22 rows 42, 50-row target까지 8 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c22_life_reinsurance_reserve_quality_capital_policy_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C22 insurance value-up/rate-cycle rallies
existing_axis_weakened: null
next_recommended_archetypes: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```
