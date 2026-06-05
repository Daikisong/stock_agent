# E2R Stock-Web v12 Residual Research — R6 / Loop 98

```yaml
scheduled_round: R6
scheduled_loop: 98
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_GA_DISTRIBUTION_IFRS17_CSM_KICS_RATE_CYCLE_COMMISSION_MARGIN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_SPIKE

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 0
life_insurance_rate_reserve_case_count: 1
ga_insurance_distribution_case_count: 2
insurance_commission_margin_case_count: 2
rate_cycle_reserve_bridge_missing_count: 1
commission_quality_margin_bridge_missing_count: 1
kics_csm_execution_bridge_missing_count: 1
short_listing_or_market_transfer_caveat_count: 2
row_presence_or_old_corporate_action_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 98
next_round: R7
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_98_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 98
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

R6 hard gate requires:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

Recent R6 branch usage:

```text
loop94: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop95: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop96: C22_INSURANCE_RATE_CYCLE_RESERVE
loop97: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

This run returns to C22 after the R6 branch cycle.

Selected fine branch:

```text
life insurance / GA insurance distribution / insurance agency commission economics
interest-rate cycle, IFRS17 CSM, K-ICS capital buffer, reserve sensitivity,
new-contract CSM, persistency, sales commission, platform scale, and margin bridge
vs generic insurance / Value-up / rate-cycle label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
rows: 37
symbols: 12
date_range: 2024-01-24~2024-08-22
good/bad S2: 10/11
4B/4C: 2/0
URL pending/proxy: 10/10
top covered symbols:
  000370(7), 003690(7), 082640(6), 000540(4), 000810(3), 005830(3)
```

Selected symbols:

```text
085620 미래에셋생명
244920 에이플러스에셋
211050 인카금융서비스
```

They avoid the C22 top-covered list and avoid the most recent R6 loop96 C22 large-insurer set:

```text
loop96 C22 avoid:
  032830, 088350, 000400

C22 top-covered avoid:
  000370, 003690, 082640, 000540, 000810, 005830
```

One caveat:

```text
085620 appeared in a prior C21 financial/capital-return context, not in this C22 insurance-reserve fine branch.
The duplicate key is canonical_archetype_id + symbol + trigger_type + entry_date, so this is not a C22 duplicate.
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
085620: same archetype, new C22 branch symbol, life-insurance rate/reserve local burst followed by material MAE, 4B / Watch cap
244920: same archetype, new symbol, GA insurance-distribution commission positive with Green cap
211050: same archetype, new symbol, GA insurance-distribution positive after post-corporate-action entry with market-transfer / row-trust cap
```

---

## 3. Price-atlas validation

Manifest fields checked from stock-web:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
inactive_or_delisted_like_symbol_count: 2,546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
085620 미래에셋생명
  profile: atlas/symbol_profiles/085/085620.json
  first_date: 2015-07-08
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,606
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2018-03-23
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside selected 2024 validation window.

244920 에이플러스에셋
  profile: atlas/symbol_profiles/244/244920.json
  first_date: 2020-11-20
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,286
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    shorter listed history versus older insurers, but no 2024 corporate-action contamination.

211050 인카금융서비스
  profile: atlas/symbol_profiles/211/211050.json
  market history:
    KONEX from 2015-11-16 to 2022-02-15
    KOSDAQ from 2022-02-16
  first_date: 2015-11-18 in tradable profile
  raw_first_date: 2015-11-16
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,224
  non_tradable_zero_volume rows: 293
  corporate_action_candidate_dates:
    2018-07-18, 2022-06-22, 2022-07-13, 2024-04-29
  selected entry:
    2024-05-02, after the 2024-04-29 raw-discontinuity candidate
  selected entry~D+180 contamination:
    none after the selected entry, but historical and immediate pre-entry caveat remains.
  caveat:
    KONEX-to-KOSDAQ migration, high historical non-tradable zero-volume count, and 2024-04-29 pre-entry corporate-action candidate require trust cap.
```

---

## 4. Archetype residual problem

C22 is about insurance rate cycles, reserve sensitivity, IFRS17 / CSM quality, K-ICS capital buffers, policy mix, lapse/persistency, and shareholder-return or commission economics. It is not a generic "insurance / financial Value-up stock is hot" archetype.

The model can over-score:

```text
insurance label
life-insurance or non-life-insurance label
interest-rate cycle headline
Korea Value-up financial label
IFRS17 / CSM headline without quality check
K-ICS / capital-buffer simplification
GA / insurance agency platform label
commission growth headline
one-week insurance stock volume spike
```

The C22 bridge must be stricter:

```text
insurance / reserve / distribution event
  -> insurance type and liability duration
  -> CSM quality and new-contract CSM
  -> K-ICS ratio, capital buffer, and regulatory room
  -> reserve sensitivity to interest rate and discount curve
  -> lapse / persistency / surrender behavior
  -> crediting-rate and investment spread
  -> product mix and loss/claims risk where relevant
  -> commission quality, churn, and sales-force productivity for GA names
  -> acquisition cost, platform cost, and compliance risk
  -> dividend / buyback / capital return room
  -> margin / OP / EV conversion
  -> price survival after the first insurance-label spike
```

A C22 insurance thesis is like an insurance balance sheet with two clocks. One clock is the rate/reserve clock, where discount rates, CSM, K-ICS, and lapse assumptions slowly move the liability. The other is the sales clock, where new policies, commissions, persistency, and compliance costs decide whether top-line growth becomes durable margin.

---

## 5. Case 1 — 085620 미래에셋생명

```yaml
case_id: C22_R6L98_085620_2024_02_01
symbol: "085620"
name: "미래에셋생명"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_GA_DISTRIBUTION_IFRS17_CSM_KICS_RATE_CYCLE_COMMISSION_MARGIN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5770
classification: local_burst_life_insurance_valueup_rate_reserve_label_material_mae_4b_watch_cap
calibration_usable: true
```

### Evidence interpretation

미래에셋생명 is the life-insurance rate/reserve local-burst case.

The setup had real C22 relevance:

```text
life insurance
  -> rate-cycle and reserve sensitivity
  -> CSM / K-ICS / capital-buffer readthrough
  -> Korea Value-up financial salience
  -> early February price spike
```

But the forward path did not sustain the early rerating. The stock produced a meaningful local MFE and then gave back into a material drawdown zone. That means the label should not remain Green unless CSM quality, reserve sensitivity, K-ICS buffer, new-contract economics, and capital-return evidence refresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 6,420 / close 5,770
2024-02-05: high 6,490 / close 6,390
2024-02-06: high 6,500 / close 6,240
2024-03-29: low 4,445 / close 4,500
2024-04-09: high 5,360 / close 4,790
2024-08-05: low 4,660 / close 4,950
2024-10-11: high 5,450 / close 5,240
```

Approximate path from entry close:

```text
entry_close: 5,770
peak_high: 6,500
MFE: +12.7%
worst_low_after_entry: 4,445
MAE: -23.0%
```

### Interpretation

This is a C22 local burst / Watch cap:

```text
Stage2-Watch: valid from life-insurance and rate/reserve relevance.
Stage2-Actionable: possible only if CSM, reserve sensitivity, K-ICS, persistency, and capital-return bridge are explicit.
Stage3-Green: blocked after material MAE and stale reserve/capital evidence.
Local 4B: required if the initial insurance/Value-up spike is not refreshed by fundamentals.
Hard 4C: no, because MFE was meaningful and MAE did not cross hard threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  life_insurance_relevance: high
  rate_cycle_reserve_signal: medium_high
  csm_quality_bridge: weak_to_medium
  kics_capital_buffer_bridge: weak_to_medium
  persistency_lapse_bridge: weak
  shareholder_return_bridge: weak_to_medium
  price_confirmation: medium_initial
  later_drawdown_penalty: material
  local_4b_overlay: required
```

---

## 6. Case 2 — 244920 에이플러스에셋

```yaml
case_id: C22_R6L98_244920_2024_02_01
symbol: "244920"
name: "에이플러스에셋"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_GA_DISTRIBUTION_IFRS17_CSM_KICS_RATE_CYCLE_COMMISSION_MARGIN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 4045
classification: capped_positive_ga_insurance_distribution_commission_margin_bridge_with_short_listing_caveat
calibration_usable: true
```

### Evidence interpretation

에이플러스에셋 is the GA insurance-distribution capped positive.

The useful C22 read is not simply:

```text
보험 관련주가 움직였다
```

It is:

```text
GA / insurance distribution platform
  -> new-policy sales and commission income
  -> sales-force productivity and persistency
  -> compliance / churn / acquisition cost discipline
  -> later price survival and gradual rerating
```

The forward path produced an initial spike, a modest drawdown, and later recovery / rerating into August-November. This is a positive distribution case, but it is not bank-like capital return or insurer-reserve Green. It needs current commission quality, persistency, sales-force productivity, compliance cost, and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,385 / close 4,045
2024-02-13: high 4,300 / close 4,230
2024-08-05: low 3,535 / close 3,585
2024-08-16: high 4,530 / close 4,230
2024-08-20: high 4,480 / close 4,480
2024-11-08: high 4,700 / close 4,555
```

Approximate path from entry close:

```text
entry_close: 4,045
peak_high: 4,700
MFE: +16.2%
worst_low_after_entry: 3,535
MAE: -12.6%
```

### Interpretation

This is a C22 capped positive:

```text
Stage2-Actionable: possible if new-contract commission quality, persistency, sales productivity, acquisition cost, and margin bridge are explicit.
Stage3-Green: blocked without fresh evidence on churn, compliance cost, and sustainable OP conversion.
Local 4B: monitor if commission growth outruns persistency or cost evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  ga_distribution_relevance: high
  commission_growth_bridge: medium_high
  persistency_churn_bridge: medium
  acquisition_cost_bridge: weak_to_medium
  compliance_cost_bridge: weak_to_medium
  margin_op_bridge: medium
  price_confirmation: medium
  drawdown_penalty: moderate
  green_cap: yes
```

---

## 7. Case 3 — 211050 인카금융서비스

```yaml
case_id: C22_R6L98_211050_2024_05_02
symbol: "211050"
name: "인카금융서비스"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_GA_DISTRIBUTION_IFRS17_CSM_KICS_RATE_CYCLE_COMMISSION_MARGIN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_SPIKE
trigger_date: 2024-05-02
entry_date: 2024-05-02
entry_price_basis: close
entry_price: 4925
classification: positive_ga_insurance_distribution_scale_commission_margin_bridge_with_market_transfer_row_trust_cap
calibration_usable: true
```

### Evidence interpretation

인카금융서비스 is the stronger GA insurance-distribution positive, but with row/trust caveat.

The selected entry is deliberately after the 2024-04-29 raw-discontinuity candidate. From that post-event base, the stock produced strong MFE into November. The business bridge is not reserve sensitivity; it is:

```text
GA distribution scale
  -> policy sales and new-contract commission
  -> sales-force productivity
  -> persistency and churn control
  -> compliance / platform / acquisition cost discipline
  -> margin conversion
```

This is a valid C22 distribution positive, but the market-transfer and historical row caveats mean it should be capped unless price and data trust are refreshed.

### Price path

Key Stock-Web rows:

```text
2024-04-29: corporate-action/raw-discontinuity candidate window
2024-05-02: high 4,925 / close 4,925
2024-05-08: high 6,480 / close 5,700
2024-05-16: high 6,270 / close 6,270
2024-08-05: low 3,700 / close 4,095
2024-08-14: high 5,640 / close 5,200
2024-09-05: low 4,200 / close 4,300
2024-11-15: high 6,690 / close 6,400
```

Approximate path from post-event entry close:

```text
entry_close: 4,925
peak_high: 6,690
MFE: +35.8%
worst_low_after_entry: 3,700
MAE: -24.9%
```

### Interpretation

This is a C22 positive with trust cap:

```text
Stage2-Actionable: possible if commission quality, persistency, sales-force productivity, and OP bridge are explicit.
Stage3-Green: blocked without fresh data-trust and commission-margin evidence.
Local 4B: monitor because the path includes material MAE before the November high.
Hard 4C: no.
Market-transfer / row-trust caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  ga_distribution_scale_relevance: high
  commission_quality_bridge: medium_high
  persistency_churn_bridge: medium
  salesforce_productivity_bridge: medium_high
  compliance_acquisition_cost_bridge: weak_to_medium
  margin_op_bridge: medium_high
  price_confirmation: high
  row_trust_caveat: high
  green_cap: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 0
life_insurance_rate_reserve_case_count: 1
ga_insurance_distribution_case_count: 2
insurance_commission_margin_case_count: 2
rate_cycle_reserve_bridge_missing_count: 1
commission_quality_margin_bridge_missing_count: 1
kics_csm_execution_bridge_missing_count: 1
short_listing_or_market_transfer_caveat_count: 2
row_presence_or_old_corporate_action_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C22 insurance grid:

```text
085620 미래에셋생명:
  life-insurance rate/reserve label local burst;
  meaningful MFE first, then material MAE, Watch/4B cap.

244920 에이플러스에셋:
  GA insurance distribution capped positive;
  moderate MFE, moderate drawdown, needs commission quality / persistency / margin bridge.

211050 인카금융서비스:
  GA insurance distribution stronger positive from post-corporate-action entry;
  large MFE but material MAE and market-transfer / row-trust cap.
```

Shared rule:

```text
C22 is not "insurance label or Value-up financial label is hot."
C22 is "CSM quality, K-ICS capital room, reserve sensitivity, persistency, commission quality, sales productivity, acquisition/compliance cost, and OP/capital-return conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C22_R6L98_085620_2024_02_01","scheduled_round":"R6","scheduled_loop":98,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_GA_DISTRIBUTION_IFRS17_CSM_KICS_RATE_CYCLE_COMMISSION_MARGIN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_SPIKE","symbol":"085620","name":"미래에셋생명","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5770,"peak_high":6500,"peak_date":"2024-02-06","worst_low_after_entry":4445,"worst_low_after_entry_date":"2024-03-29","mfe_pct":12.7,"mae_pct":-23.0,"classification":"local_burst_life_insurance_valueup_rate_reserve_label_material_mae_4b_watch_cap","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"life_insurance_rate_cycle_ifrs17_csm_kics_reserve_persistency_capital_return_bridge","residual_error":"life_insurance_valueup_rate_label_can_create_mfe_but_needs_4b_when_csm_kics_reserve_evidence_not_refreshed","shadow_rule_candidate":"classify_meaningful_mfe_then_material_mae_life_insurance_rate_cases_as_local_4b_or_watch_without_fresh_csm_kics_evidence"}
{"row_type":"case","case_id":"C22_R6L98_244920_2024_02_01","scheduled_round":"R6","scheduled_loop":98,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_GA_DISTRIBUTION_IFRS17_CSM_KICS_RATE_CYCLE_COMMISSION_MARGIN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_SPIKE","symbol":"244920","name":"에이플러스에셋","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":4045,"peak_high":4700,"peak_date":"2024-11-08","worst_low_after_entry":3535,"worst_low_after_entry_date":"2024-08-05","mfe_pct":16.2,"mae_pct":-12.6,"classification":"capped_positive_ga_insurance_distribution_commission_margin_bridge_with_short_listing_caveat","calibration_usable":true,"short_listing_or_row_presence_caveat":true,"evidence_family":"ga_insurance_distribution_new_policy_commission_persistency_salesforce_productivity_margin_bridge","residual_error":"ga_distribution_positive_requires_green_cap_without_refreshed_commission_quality_persistency_and_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_commission_quality_persistency_and_margin_bridge_confirm_but_cap_green_without_fresh_evidence"}
{"row_type":"case","case_id":"C22_R6L98_211050_2024_05_02","scheduled_round":"R6","scheduled_loop":98,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_GA_DISTRIBUTION_IFRS17_CSM_KICS_RATE_CYCLE_COMMISSION_MARGIN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_SPIKE","symbol":"211050","name":"인카금융서비스","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":4925,"peak_high":6690,"peak_date":"2024-11-15","worst_low_after_entry":3700,"worst_low_after_entry_date":"2024-08-05","mfe_pct":35.8,"mae_pct":-24.9,"classification":"positive_ga_insurance_distribution_scale_commission_margin_bridge_with_market_transfer_row_trust_cap","calibration_usable":true,"market_transfer_or_row_presence_caveat":true,"pre_entry_corporate_action_caveat":true,"evidence_family":"ga_distribution_scale_new_policy_commission_salesforce_productivity_persistency_compliance_cost_margin_bridge","residual_error":"ga_distribution_scale_positive_requires_trust_cap_when_market_transfer_row_presence_and_pre_entry_raw_discontinuity_caveat_exists","shadow_rule_candidate":"preserve_ga_distribution_positive_but_cap_green_when_row_trust_or_commission_margin_evidence_is_not_refreshed"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":98,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_GA_DISTRIBUTION_IFRS17_CSM_KICS_RATE_CYCLE_COMMISSION_MARGIN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":0,"life_insurance_rate_reserve_case_count":1,"ga_insurance_distribution_case_count":2,"insurance_commission_margin_case_count":2,"rate_cycle_reserve_bridge_missing_count":1,"commission_quality_margin_bridge_missing_count":1,"kics_csm_execution_bridge_missing_count":1,"short_listing_or_market_transfer_caveat_count":2,"row_presence_or_old_corporate_action_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":98,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","rule_id":"C22_INSURANCE_CSM_KICS_PERSISTENCY_COMMISSION_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C22 insurance rate-cycle/reserve and insurance-distribution cases, do not open Stage2-Actionable or Stage3-Green from insurance label, life-insurance/non-life-insurance label, interest-rate cycle headline, Korea Value-up financial label, IFRS17/CSM headline without quality check, K-ICS/capital-buffer simplification, GA/insurance-agency platform label, commission-growth headline, or one-week insurance stock volume spike alone. Require insurance type and liability duration, CSM quality and new-contract CSM, K-ICS ratio/capital buffer/regulatory room, reserve sensitivity to interest rate and discount curve, lapse/persistency/surrender behavior, crediting-rate and investment spread, product mix and claims risk where relevant, commission quality/churn/sales-force productivity for GA names, acquisition/platform/compliance cost control, dividend/buyback/capital-return room, margin/OP/EV conversion, and post-trigger price survival. Life-insurance rate-cycle cases with meaningful MFE followed by material MAE should remain local 4B or Watch without fresh CSM/K-ICS/reserve evidence. GA distribution positives may be capped Actionable when commission quality, persistency, and margin bridge are explicit, but Green requires fresh evidence and row/trust caveats must cap market-transfer or pre-entry corporate-action cases.","expected_effect":"Preserve true insurance reserve/capital and GA distribution positives while reducing insurance-label, Value-up, CSM headline, and commission-growth false positives where persistency, capital, reserve, compliance, acquisition cost, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":98,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"insurance_csm_kics_persistency_commission_margin_guard","contribution":"Adds one life-insurance rate/reserve 4B Watch case and two GA insurance-distribution positives to calibrate C22 CSM/K-ICS/reserve sensitivity, persistency, commission quality, sales productivity, compliance/acquisition cost, market-transfer trust, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C22_INSURANCE_CSM_KICS_PERSISTENCY_COMMISSION_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE:

  Do not open Stage3-Green from:
    - insurance label alone
    - life-insurance / non-life-insurance label alone
    - interest-rate cycle headline alone
    - Korea Value-up financial label alone
    - IFRS17 / CSM headline without quality check alone
    - K-ICS / capital-buffer simplification alone
    - GA / insurance agency platform label alone
    - commission growth headline alone
    - one-week insurance-stock volume spike alone

  Require at least two of:
    - insurance type and liability duration
    - CSM quality and new-contract CSM
    - K-ICS ratio / capital buffer / regulatory room
    - reserve sensitivity to interest rate and discount curve
    - lapse / persistency / surrender behavior
    - crediting-rate and investment spread
    - product mix and claims risk where relevant
    - commission quality / churn / sales-force productivity for GA names
    - acquisition / platform / compliance cost containment
    - dividend / buyback / capital-return room
    - margin / OP / EV conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the insurance/rate headline

  If MFE < 8% and MAE < -30%:
    route to C22 hard-4C candidate.

  If MFE > 10% but CSM/K-ICS/reserve evidence is stale:
    preserve as local 4B / Watch, not Green.

  If the company is GA / insurance-distribution rather than insurer:
    require commission quality, persistency, sales productivity, compliance cost, and OP margin before Actionable.

  If market-transfer, row-presence, or pre-entry raw-discontinuity caveat exists:
    apply additional trust cap even when price path is positive.

  Distinguish:
    - insurers where rate/reserve/CSM/K-ICS becomes capital and shareholder value
    - from GA platforms where new-policy commission becomes durable margin only if persistency and compliance cost behave.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_98_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C22 insurance rate/reserve / GA distribution cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C22_INSURANCE_CSM_KICS_PERSISTENCY_COMMISSION_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C22 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C22 cases agree, consider implementing a canonical guard that:
   - blocks insurance Green without CSM, K-ICS, reserve sensitivity, persistency, capital buffer, and margin bridge,
   - treats life-insurance rate/Value-up cases with MFE then material MAE as local 4B or Watch,
   - distinguishes GA/insurance distribution from insurer reserve economics,
   - requires commission quality, churn, sales-force productivity, acquisition/compliance cost, and OP margin for GA Actionable,
   - applies market-transfer, pre-entry corporate-action, row-presence, and old corporate-action caveats when needed.

Expected next schedule:
completed_round = R6
completed_loop = 98
next_round = R7
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R6
completed_loop = 98
next_round = R7
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
