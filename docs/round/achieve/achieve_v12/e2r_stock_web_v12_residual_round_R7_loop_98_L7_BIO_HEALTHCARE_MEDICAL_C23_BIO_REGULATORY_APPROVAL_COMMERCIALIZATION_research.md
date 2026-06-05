# E2R Stock-Web v12 Residual Research — R7 / Loop 98

```yaml
scheduled_round: R7
scheduled_loop: 98
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BIOSIMILAR_BOTOX_VACCINE_APPROVAL_COMMERCIALIZATION_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_REGULATORY_LABEL_SPIKE

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
hard_4c_candidate_count: 1
biosimilar_commercialization_case_count: 1
botulinum_toxin_global_approval_case_count: 1
vaccine_biologic_commercialization_case_count: 1
regulatory_approval_to_launch_bridge_missing_count: 1
commercial_revenue_margin_bridge_missing_count: 1
late_chase_case_count: 1
market_segment_or_old_corporate_action_caveat_count: 2
row_presence_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 98
next_round: R8
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_98_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 98
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate requires:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

Recent R7 branch usage:

```text
loop93: C24_BIO_TRIAL_DATA_EVENT_RISK
loop94: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop95: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop96: C24_BIO_TRIAL_DATA_EVENT_RISK
loop97: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

This run returns to C23 after the R7 branch cycle.

Selected fine branch:

```text
biosimilar / botulinum toxin / vaccine or biologic commercialization
regulatory approval, launch timing, partner / geography, reimbursement,
manufacturing scale, channel adoption, revenue recognition, and margin bridge
vs generic regulatory-approval or bio-commercialization label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rows: 26
symbols: 14
date_range: 2022-06-29~2024-08-21
good/bad S2: 8/5
4B/4C: 0/2
URL pending/proxy: 0/0
top covered symbols:
  UNKNOWN_SYMBOL(6), 028300(4), 000100(2), 039200(2), 195940(2), 003850(1)
```

Selected symbols:

```text
000250 삼천당제약
145020 휴젤
206650 유바이오로직스
```

They avoid the C23 top-covered list and recent R7 branch names:

```text
loop97 C25 avoid:
  226400, 065510, 263690

loop96 C24 avoid:
  196170, 235980, 217730

loop95 C23 avoid:
  207940, 068270, 086900

loop94 C25 avoid:
  335890, 041830, 228670

C23 top-covered avoid:
  028300, 000100, 039200, 195940, 003850
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
000250: same archetype, new symbol, biosimilar / regulatory commercialization positive with very large MFE and Green cap
145020: same archetype, new symbol, botulinum toxin global approval / commercialization positive with Green cap
206650: same archetype, new symbol, vaccine/biologic commercialization late-chase hard-4C candidate when launch/revenue/margin bridge was missing
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
000250 삼천당제약
  profile: atlas/symbol_profiles/000/000250.json
  first_date: 2000-10-04
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,258
  non_tradable_zero_volume rows: 2
  corporate_action_candidate_dates:
    2002-04-22
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action / raw-discontinuity caveat exists outside selected 2024 validation window.

145020 휴젤
  profile: atlas/symbol_profiles/145/145020.json
  first_date: 2015-12-24
  last_date: 2026-02-20
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  tradable_ohlcv rows: 2,489
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2017-07-31, 2020-07-08, 2020-07-31
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action windows are outside selected 2024 validation window.

206650 유바이오로직스
  profile: atlas/symbol_profiles/206/206650.json
  first_date: 2017-01-24
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 2,221
  non_tradable_zero_volume rows: 2
  corporate_action_candidate_dates: none
  2024 selected late-entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C23 is about regulatory approval and commercialization. It is not a generic "bio approval news" or "pipeline value" archetype.

The model can over-score:

```text
regulatory approval headline
FDA / EMA / domestic approval label
biosimilar or formulation platform label
botulinum toxin / aesthetic biologic approval label
vaccine / biologic commercialization story
partner / license-out rumor
one-week bio-stock volume spike
late chase after approval rerating
```

The C23 bridge must be stricter:

```text
bio approval / commercialization event
  -> named product, indication, geography, and regulator
  -> approval status and label scope
  -> launch timing and partner / distributor
  -> reimbursement / pricing / formulary or channel access
  -> manufacturing scale, COGS, and quality-risk control
  -> inventory, batch release, and supply continuity
  -> royalty / milestone / product revenue recognition
  -> SG&A, launch cost, and margin / OP conversion
  -> event-window separation after a failed first trigger
  -> price survival after the first regulatory-label spike
```

A C23 thesis is like a drug leaving the regulator's gate. Approval opens the gate, but equity value appears only when the product is launched, reimbursed, distributed, supplied at scale, recognized as revenue, and still leaves margin after launch costs.

---

## 5. Case 1 — 000250 삼천당제약

```yaml
case_id: C23_R7L98_000250_2024_02_01
symbol: "000250"
name: "삼천당제약"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BIOSIMILAR_BOTOX_VACCINE_APPROVAL_COMMERCIALIZATION_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_REGULATORY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 64200
classification: positive_biosimilar_regulatory_commercialization_partner_revenue_bridge_with_green_cap_after_very_large_mfe
calibration_usable: true
```

### Evidence interpretation

삼천당제약 is the constructive C23 biosimilar / regulatory commercialization control.

The useful C23 read is not simply:

```text
바이오시밀러 / 허가 기대주가 강하다
```

It is:

```text
biosimilar / formulation / regulatory commercialization relevance
  -> approval and partner/geography optionality
  -> launch and product-revenue conversion optionality
  -> very large March-July price confirmation
  -> later Green cap because launch/reimbursement/margin evidence must refresh
```

The forward path produced a very large MFE and remained far above the entry for much of the validation window. However, after such a large rerating, C23 should not stay unrestricted Green unless approval scope, partner launch timing, reimbursement, supply, revenue recognition, and margin evidence are current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 64,800 / low 61,900 / close 64,200
2024-02-28: high 79,200 / close 77,200
2024-03-25: high 111,100 / close 111,100
2024-03-26: high 143,400 / close 140,400
2024-04-01: high 151,200 / close 140,700
2024-07-24: high 189,100 / close 185,200
2024-08-05: low 145,500 / close 152,600
2024-09-06: low 128,400 / close 132,500
```

Approximate path from entry close:

```text
entry_close: 64,200
peak_high: 189,100
MFE: +194.5%
worst_low_after_entry: 61,900
MAE: -3.6%
```

### Interpretation

This is a C23 positive with Green cap:

```text
Stage2-Actionable: possible if product/geography/regulator, partner, launch, reimbursement, and revenue bridge are explicit.
Stage3-Green: blocked after +190% MFE unless fresh commercialization and margin evidence appears.
Local 4B: monitor if price outruns launch/revenue evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  biosimilar_regulatory_relevance: high
  approval_partner_bridge: high
  launch_reimbursement_bridge: medium_high
  revenue_recognition_bridge: medium
  manufacturing_supply_bridge: medium
  margin_op_bridge: medium
  price_confirmation: extreme
  drawdown_penalty: low
  green_cap: required_after_extreme_mfe
```

---

## 6. Case 2 — 145020 휴젤

```yaml
case_id: C23_R7L98_145020_2024_02_01
symbol: "145020"
name: "휴젤"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BIOSIMILAR_BOTOX_VACCINE_APPROVAL_COMMERCIALIZATION_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_REGULATORY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 160000
classification: positive_botulinum_toxin_global_approval_commercialization_channel_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

휴젤 is the botulinum toxin / global approval and commercialization positive.

The setup had strong C23 relevance:

```text
botulinum toxin / aesthetic biologic
  -> global regulatory approval and channel access
  -> commercialization and distributor launch optionality
  -> price confirmation into July-August and October
```

The forward path produced a large MFE with controlled early drawdown. This is a C23 positive. Still, regulatory approval alone is not enough. Green should require launch timing, channel sell-in/sell-through, pricing, supply continuity, and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 161,300 / low 150,300 / close 160,000
2024-02-20: high 182,700 / close 181,400
2024-03-04: high 219,000 / close 202,500
2024-04-29: high 223,000 / close 221,000
2024-07-24: high 251,000 / close 246,500
2024-08-19: high 294,500 / close 286,500
2024-10-17: high 301,000 / close 293,000
2024-10-25: low 263,500 / close 268,500
```

Approximate path from entry close:

```text
entry_close: 160,000
peak_high: 301,000
MFE: +88.1%
worst_low_after_entry: 147,100
MAE: -8.1%
```

### Interpretation

This is a C23 positive with Green cap:

```text
Stage2-Actionable: possible if approval, geography, channel partner, launch timing, and margin bridge are explicit.
Stage3-Green: blocked without fresh launch / channel / supply / margin evidence after large MFE.
Local 4B: monitor after +80% MFE if commercialization evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  botulinum_toxin_regulatory_relevance: high
  global_approval_bridge: high
  channel_launch_bridge: medium_high
  pricing_supply_bridge: medium
  margin_op_bridge: medium_high
  price_confirmation: very_high
  drawdown_penalty: low
  green_cap: required_after_large_mfe
```

---

## 7. Case 3 — 206650 유바이오로직스

```yaml
case_id: C23_R7L98_206650_2024_04_15
symbol: "206650"
name: "유바이오로직스"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BIOSIMILAR_BOTOX_VACCINE_APPROVAL_COMMERCIALIZATION_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_REGULATORY_LABEL_SPIKE
trigger_date: 2024-04-15
entry_date: 2024-04-15
entry_price_basis: close
entry_price: 13900
classification: hard_4c_candidate_vaccine_biologic_commercialization_late_chase_without_launch_revenue_margin_survival
calibration_usable: true
```

### Evidence interpretation

유바이오로직스 is the vaccine / biologic commercialization late-chase guardrail.

The label can fool the model:

```text
vaccine / biologic platform
regulatory or commercialization expectation
global public-health / supply optionality
one-day bio-commercialization volume spike
```

The stock had earlier positive momentum, but from the selected April 15 late-entry close the path did not validate incremental approval-to-launch, procurement, supply, revenue recognition, or margin evidence. The late entry had shallow MFE and then moved into a hard drawdown zone.

### Price path

Key Stock-Web rows:

```text
2024-04-15: high 14,400 / close 13,900
2024-04-22: high 14,500 / close 13,550
2024-05-02: close 13,390
2024-08-05: low 9,350 / close 9,890
2024-09-06: low 9,790 / close 9,830
2024-10-29: high 15,780 / close 15,480
```

Approximate path from late entry close:

```text
entry_close: 13,900
peak_high_before_later_reignition: 14,500
MFE: +4.3%
worst_low_after_entry: 9,350
MAE: -32.7%
```

The October 29 spike should be treated as a renewed event window, not a rescue of the April late-entry trigger.

### Interpretation

This is a hard C23 false-positive candidate:

```text
Stage2-Watch: possible from vaccine / biologic commercialization relevance.
Stage2-Actionable: blocked unless product, regulator, launch, procurement, supply, revenue, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30%+ MAE.
Event-window separation: yes, later October spike should be separated.
```

The lesson is that a vaccine or biologic commercialization label is not launch-revenue survival.

### Stress-test components

```text
raw_component_score_proxy:
  vaccine_biologic_label: high
  regulatory_commercialization_signal: medium_high
  product_launch_bridge: weak
  procurement_revenue_bridge: weak
  manufacturing_supply_bridge: weak_to_medium
  margin_op_bridge: weak
  price_confirmation_after_late_entry: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
biosimilar_commercialization_case_count: 1
botulinum_toxin_global_approval_case_count: 1
vaccine_biologic_commercialization_case_count: 1
regulatory_approval_to_launch_bridge_missing_count: 1
commercial_revenue_margin_bridge_missing_count: 1
late_chase_case_count: 1
market_segment_or_old_corporate_action_caveat_count: 2
row_presence_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C23 approval / commercialization grid:

```text
000250 삼천당제약:
  biosimilar / regulatory commercialization positive;
  extreme MFE and low MAE, but Green requires fresh launch, reimbursement, revenue, and margin evidence.

145020 휴젤:
  botulinum toxin / global approval commercialization positive;
  large MFE and controlled MAE, but Green requires fresh launch/channel/supply/margin evidence.

206650 유바이오로직스:
  vaccine / biologic commercialization late chase failed;
  shallow MFE and hard-zone MAE, hard 4C candidate with event-window separation.
```

Shared rule:

```text
C23 is not "approval or commercialization label is hot."
C23 is "approval scope, launch timing, partner/distributor, reimbursement/channel access, manufacturing supply, revenue recognition, and margin conversion are visible for this product."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C23_R7L98_000250_2024_02_01","scheduled_round":"R7","scheduled_loop":98,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_BOTOX_VACCINE_APPROVAL_COMMERCIALIZATION_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_REGULATORY_LABEL_SPIKE","symbol":"000250","name":"삼천당제약","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":64200,"peak_high":189100,"peak_date":"2024-07-24","worst_low_after_entry":61900,"worst_low_after_entry_date":"2024-02-01","mfe_pct":194.5,"mae_pct":-3.6,"classification":"positive_biosimilar_regulatory_commercialization_partner_revenue_bridge_with_green_cap_after_very_large_mfe","calibration_usable":true,"market_segment_or_old_corporate_action_caveat":true,"evidence_family":"biosimilar_regulatory_commercialization_partner_launch_reimbursement_revenue_margin_bridge","residual_error":"extreme_biosimilar_commercialization_rerating_requires_green_cap_without_refreshed_launch_revenue_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_approval_partner_and_launch_revenue_bridge_confirm_but_cap_green_after_extreme_mfe"}
{"row_type":"case","case_id":"C23_R7L98_145020_2024_02_01","scheduled_round":"R7","scheduled_loop":98,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_BOTOX_VACCINE_APPROVAL_COMMERCIALIZATION_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_REGULATORY_LABEL_SPIKE","symbol":"145020","name":"휴젤","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":160000,"peak_high":301000,"peak_date":"2024-10-17","worst_low_after_entry":147100,"worst_low_after_entry_date":"2024-02-13","mfe_pct":88.1,"mae_pct":-8.1,"classification":"positive_botulinum_toxin_global_approval_commercialization_channel_margin_bridge_with_green_cap","calibration_usable":true,"market_segment_or_old_corporate_action_caveat":true,"evidence_family":"botulinum_toxin_global_approval_channel_partner_launch_pricing_supply_margin_bridge","residual_error":"botox_global_approval_positive_requires_green_cap_without_refreshed_launch_channel_supply_margin_evidence","shadow_rule_candidate":"preserve_botulinum_toxin_approval_positive_but_cap_green_after_large_mfe_without_fresh_commercialization_evidence"}
{"row_type":"case","case_id":"C23_R7L98_206650_2024_04_15","scheduled_round":"R7","scheduled_loop":98,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_BOTOX_VACCINE_APPROVAL_COMMERCIALIZATION_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_REGULATORY_LABEL_SPIKE","symbol":"206650","name":"유바이오로직스","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":13900,"peak_high_before_later_reignition":14500,"peak_date":"2024-04-22","worst_low_after_entry":9350,"worst_low_after_entry_date":"2024-08-05","mfe_pct":4.3,"mae_pct":-32.7,"classification":"hard_4c_candidate_vaccine_biologic_commercialization_late_chase_without_launch_revenue_margin_survival","calibration_usable":true,"row_presence_caveat":true,"event_window_separation_required":true,"evidence_family":"vaccine_biologic_commercialization_late_chase_without_product_launch_procurement_revenue_margin_bridge","residual_error":"vaccine_biologic_commercialization_label_can_fail_when_launch_revenue_and_margin_bridge_missing","shadow_rule_candidate":"route_vaccine_biologic_late_chase_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_commercial_revenue_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":98,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_BOTOX_VACCINE_APPROVAL_COMMERCIALIZATION_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_REGULATORY_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"biosimilar_commercialization_case_count":1,"botulinum_toxin_global_approval_case_count":1,"vaccine_biologic_commercialization_case_count":1,"regulatory_approval_to_launch_bridge_missing_count":1,"commercial_revenue_margin_bridge_missing_count":1,"late_chase_case_count":1,"market_segment_or_old_corporate_action_caveat_count":2,"row_presence_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":98,"canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","rule_id":"C23_APPROVAL_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C23 bio regulatory approval/commercialization cases, do not open Stage2-Actionable or Stage3-Green from regulatory approval, FDA/EMA/domestic approval, biosimilar/formulation platform, botulinum toxin/aesthetic biologic approval, vaccine/biologic commercialization, partner/license-out rumor, one-week bio-stock volume spike, or late chase after approval rerating labels alone. Require named product/indication/geography/regulator, approval status and label scope, launch timing and partner/distributor, reimbursement/pricing/formulary or channel access, manufacturing scale/COGS/quality-risk control, inventory/batch release/supply continuity, royalty/milestone/product revenue recognition, SG&A/launch cost and margin/OP conversion, event-window separation after failed first trigger, and post-trigger price survival. Biosimilar or botulinum-toxin positives with very large MFE may be capped Actionable when approval, partner, launch, revenue, and margin bridge are explicit, but Green requires fresh evidence. Vaccine/biologic commercialization late chases with shallow MFE and hard-zone MAE should route to hard-4C when launch/revenue/margin bridge is missing.","expected_effect":"Preserve true bio approval-to-commercialization positives while reducing regulatory-label, partner-rumor, vaccine/biologic, and late-chase false positives where launch, reimbursement, supply, revenue recognition, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":98,"canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","residual_type":"approval_launch_reimbursement_revenue_margin_guard","contribution":"Adds one biosimilar commercialization positive, one botulinum-toxin approval commercialization positive, and one vaccine/biologic late-chase hard-4C candidate to calibrate C23 approval scope, launch timing, partner/channel, reimbursement, supply, revenue recognition, event-window separation, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C23_APPROVAL_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION:

  Do not open Stage3-Green from:
    - regulatory approval headline alone
    - FDA / EMA / domestic approval label alone
    - biosimilar or formulation platform label alone
    - botulinum toxin / aesthetic biologic approval label alone
    - vaccine / biologic commercialization story alone
    - partner / license-out rumor alone
    - one-week bio-stock volume spike alone
    - late chase after approval rerating alone

  Require at least two of:
    - named product / indication / geography / regulator
    - approval status and label scope
    - launch timing and partner / distributor
    - reimbursement / pricing / formulary or channel access
    - manufacturing scale / COGS / quality-risk control
    - inventory / batch release / supply continuity
    - royalty / milestone / product revenue recognition
    - SG&A / launch cost and margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the approval/commercialization headline

  If MFE < 8% and MAE <= -30%:
    route to C23 hard-4C candidate.

  If MFE > 50% but launch/revenue/margin evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If later event-like spikes appear after first-phase failure:
    create a new event window; do not retroactively validate the earlier failed trigger.

  Distinguish:
    - products where approval becomes launch, reimbursement, channel access, revenue, and margin
    - from approval labels where launch cost, reimbursement friction, supply, or delayed revenue breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_98_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C23 bio regulatory approval/commercialization cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C23_APPROVAL_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C23 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C23 cases agree, consider implementing a canonical guard that:
   - blocks approval/commercialization Green without product/geography/regulator, launch, partner/channel, reimbursement, supply, revenue recognition, and margin bridge,
   - preserves biosimilar and botulinum-toxin positives only with price survival and fresh commercialization evidence,
   - caps very-large-MFE bio approval reratings until launch/revenue evidence refreshes,
   - routes shallow-MFE/hard-zone-MAE vaccine/biologic late chases to hard-4C,
   - separates renewed event windows from earlier failed approval/commercialization triggers,
   - applies market-segment, old corporate-action, and row-presence caveats when needed.

Expected next schedule:
completed_round = R7
completed_loop = 98
next_round = R8
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 98
next_round = R8
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
