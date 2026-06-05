# E2R Stock-Web v12 Residual Research — R7 / Loop 95

```yaml
scheduled_round: R7
scheduled_loop: 95
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: CDMO_BIOSIMILAR_TOXIN_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BIO_LABEL_SPIKE

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
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
corporate_action_caveat_avoided_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 95
next_round: R8
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_95_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 95
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate requires:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

Recent R7 branch usage:

```text
loop92: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop93: C24_BIO_TRIAL_DATA_EVENT_RISK
loop94: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

This run returns to C23 but avoids the top-covered C23 names and uses a different fine branch:

```text
CDMO / biosimilar / botulinum-toxin
regulatory and commercialization revenue-margin bridge
vs generic bio-label spike
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
207940 삼성바이오로직스
068270 셀트리온
086900 메디톡스
```

They avoid the C23 top-covered list and avoid recent R7 loop94 C25 names:

```text
loop94 avoid: 335890, 041830, 228670
```

They also avoid the recent C24 trial-data set and medical-device export set.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
207940: same archetype, new symbol, CDMO commercialization / large-scale execution positive with Green cap
068270: same archetype, new symbol, biosimilar commercialization label Watch cap without strong incremental approval-revenue bridge
086900: same archetype, new symbol, botulinum-toxin regulatory/commercialization label hard-4C without legal/regulatory revenue survival
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
207940 삼성바이오로직스
  profile: atlas/symbol_profiles/207/207940.json
  first_date: 2016-11-10
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,240
  corporate_action_candidate_dates:
    2025-11-24
  2024 entry~D+180 contamination: none
  caveat:
    2025 corporate-action candidate is outside the 2024 validation window.

068270 셀트리온
  profile: atlas/symbol_profiles/068/068270.json
  name history:
    오알켐 until 2008-08-28
    셀트리온 from 2008-08-29
  market:
    KOSDAQ until 2018-02-08
    KOSPI from 2018-02-09
  first_date: 2005-07-19
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,064
  corporate_action_candidate_dates:
    2006-10-13, 2008-06-10, 2008-09-24, 2012-06-29, 2013-03-22, 2024-01-12
  selected entry:
    2024-02-01, after the 2024-01-12 corporate-action candidate window
  entry~D+180 contamination: avoided

086900 메디톡스
  profile: atlas/symbol_profiles/086/086900.json
  first_date: 2009-01-16
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 4,215
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C23 is about regulatory approval, commercialization, and the conversion of biomedical relevance into revenue and margin. It is not a generic "bio stock" or "approval label" archetype.

The model can over-score:

```text
regulatory approval headline
FDA / EMA / domestic approval label
biosimilar / biologics commercialization label
CDMO capacity label
botulinum-toxin or aesthetic drug label
legal / settlement / license optionality
one-week bio-stock volume spike
```

The C23 bridge must be stricter:

```text
bio regulatory or commercialization event
  -> approved product or serviceable market
  -> named customer, product, or geography
  -> launch / shipment / reimbursement / prescription / utilization path
  -> manufacturing capacity and quality compliance
  -> revenue recognition
  -> gross margin and SG&A burden
  -> legal/regulatory overhang risk check
  -> price survival after the first bio-label spike
```

A C23 bio thesis is like a medicine leaving the lab. The approval stamp matters, but equity value appears only when the product reaches patients or customers, reimbursement and channel economics work, manufacturing passes quality checks, and revenue lands with margin.

---

## 5. Case 1 — 207940 삼성바이오로직스

```yaml
case_id: C23_R7L95_207940_2024_07_24
symbol: "207940"
name: "삼성바이오로직스"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: CDMO_BIOSIMILAR_TOXIN_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BIO_LABEL_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 883000
classification: positive_cdmo_commercial_execution_capacity_revenue_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

삼성바이오로직스 is the constructive C23 control.

The useful C23 read is not simply:

```text
대형 바이오가 강하다
```

It is:

```text
CDMO scale and commercial execution
  -> large-cap biologics manufacturing capacity
  -> quality and customer trust
  -> revenue and margin conversion
  -> strong post-trigger price survival
```

The forward path from the July trigger delivered meaningful MFE with controlled drawdown. This is the kind of bio commercialization profile that can support Actionable/Green, but Green still requires continuing backlog, capacity utilization, quality compliance, and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 890,000 / close 883,000
2024-07-30: high 960,000 / close 937,000
2024-08-05: low 853,000 / close 890,000
2024-08-27: high 1,005,000 / close 973,000
2024-09-25: high 1,109,000 / close 1,047,000
2024-10-22: high 1,113,000 / close 1,059,000
2024-10-31: low 1,000,000 / close 1,002,000
```

Approximate path from entry close:

```text
entry_close: 883,000
peak_high: 1,113,000
MFE: +26.0%
worst_low_after_entry: 836,000
MAE: -5.3%
```

### Interpretation

This is a C23 positive with Green cap:

```text
Stage2-Actionable: valid if CDMO customer, backlog, capacity, quality, and margin bridge are explicit.
Stage3-Green: possible with continuing utilization, revenue recognition, and OP/margin evidence.
Local 4B: not immediate, but required if price rerating outruns new capacity/backlog evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  cdmo_commercialization_relevance: very_high
  customer_capacity_bridge: high
  quality_compliance_bridge: high
  revenue_margin_bridge: high
  price_confirmation: high
  drawdown_penalty: low
  green_cap: execution_evidence_required
```

---

## 6. Case 2 — 068270 셀트리온

```yaml
case_id: C23_R7L95_068270_2024_02_01
symbol: "068270"
name: "셀트리온"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: CDMO_BIOSIMILAR_TOXIN_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BIO_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 178700
classification: watch_cap_biosimilar_commercialization_label_without_strong_incremental_approval_revenue_bridge
calibration_usable: true
```

### Evidence interpretation

셀트리온 is the large-bio Watch cap.

The company has real C23 relevance:

```text
biosimilar portfolio
commercialization and global channel
regulatory and reimbursement pathways
```

But from the selected post-corporate-action entry, the price path did not validate a strong incremental rerating. MFE was modest and MAE was controlled, which makes the case a Watch/Yellow cap rather than a hard failure. The model should require incremental approval, launch, market-share, reimbursement, and margin evidence before Actionable/Green.

### Price path

Key Stock-Web rows:

```text
2024-01-12: corporate-action candidate window in profile; selected entry is after this window
2024-02-01: high 179,800 / close 178,700
2024-02-27: high 191,400 / close 190,100
2024-03-29: high 192,800 / close 191,200
2024-04-17: low 169,700 / close 171,000
2024-05-07: high 197,000 / close 194,400
```

Approximate path from entry close:

```text
entry_close: 178,700
peak_high: 197,000
MFE: +10.2%
worst_low_after_entry: 169,700
MAE: -5.0%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from biosimilar commercialization relevance.
Stage2-Actionable: blocked unless incremental approval, launch, revenue, and margin bridge are explicit.
Stage3-Green: blocked without fresh market-share, reimbursement, and OP evidence.
Hard 4C: no, because MAE was controlled.
```

The lesson is that a large biologics platform can be relevant but still not deliver enough incremental price evidence for Actionable/Green at the selected trigger.

### Stress-test components

```text
raw_component_score_proxy:
  biosimilar_commercialization_relevance: high
  regulatory_channel_bridge: medium_high
  incremental_approval_revenue_bridge: weak_to_medium
  reimbursement_margin_bridge: weak_to_medium
  price_confirmation: modest
  drawdown_penalty: low
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 086900 메디톡스

```yaml
case_id: C23_R7L95_086900_2024_02_01
symbol: "086900"
name: "메디톡스"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: CDMO_BIOSIMILAR_TOXIN_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BIO_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 190400
classification: hard_4c_candidate_botulinum_toxin_regulatory_commercialization_label_without_legal_revenue_margin_survival
calibration_usable: true
```

### Evidence interpretation

메디톡스 is the hard C23 guardrail.

The setup had a tempting label:

```text
botulinum-toxin / aesthetic biologics
regulatory and legal optionality
commercialization and export expectation
```

But from the selected entry, the price path failed quickly. The initial MFE was shallow, while MAE crossed the hard-4C zone within the following months. This is a classic C23 trap: regulatory or legal salience without a clean commercial revenue and margin bridge.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 194,200 / close 190,400
2024-02-02: high 197,600 / close 193,700
2024-02-26: low 148,600 / close 160,100
2024-04-17: low 128,000 / close 128,100
2024-08-09: high 200,000 / close 190,100
2024-10-22: low 164,800 / close 170,500
```

Approximate path from entry close:

```text
entry_close: 190,400
peak_high_early: 197,600
MFE: +3.8%
worst_low_after_entry: 128,000
MAE: -32.8%
```

### Interpretation

This is a hard C23 false-positive:

```text
Stage2-Watch: possible from toxin/regulatory/commercialization relevance.
Stage2-Actionable: blocked unless approval/legal clarity, launch, shipments, revenue, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30%+ MAE.
```

The lesson is that regulatory salience without clean legal and revenue conversion is not commercialization.

### Stress-test components

```text
raw_component_score_proxy:
  toxin_regulatory_label: high
  commercialization_label: medium_high
  legal_overhang_clarity: weak
  revenue_shipment_bridge: weak
  margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
corporate_action_caveat_avoided_count: 2
calibration_usable_trigger_count: 3
```

The three-case C23 bio commercialization grid:

```text
207940 삼성바이오로직스:
  CDMO commercialization / capacity / quality / revenue bridge positive;
  meaningful MFE and controlled MAE, but Green still requires execution evidence.

068270 셀트리온:
  biosimilar commercialization label;
  modest MFE and low MAE, Watch/Yellow cap without incremental approval-revenue bridge.

086900 메디톡스:
  toxin regulatory/commercialization label failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C23 is not "bio/regulatory label."
C23 is "approval or commercialization becomes launch, shipment, reimbursement, revenue recognition, and margin for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C23_R7L95_207940_2024_07_24","scheduled_round":"R7","scheduled_loop":95,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CDMO_BIOSIMILAR_TOXIN_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BIO_LABEL_SPIKE","symbol":"207940","name":"삼성바이오로직스","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":883000,"peak_high":1113000,"peak_date":"2024-10-22","worst_low_after_entry":836000,"worst_low_after_entry_date":"2024-07-24","mfe_pct":26.0,"mae_pct":-5.3,"classification":"positive_cdmo_commercial_execution_capacity_revenue_margin_bridge_with_green_cap","calibration_usable":true,"evidence_family":"cdmo_commercial_execution_capacity_quality_revenue_margin_bridge","residual_error":"positive_large_cdmo_path_still_requires_execution_evidence_before_unrestricted_green","shadow_rule_candidate":"allow_actionable_when_customer_capacity_quality_and_margin_bridge_confirm_but_cap_green_without_fresh_execution"}
{"row_type":"case","case_id":"C23_R7L95_068270_2024_02_01","scheduled_round":"R7","scheduled_loop":95,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CDMO_BIOSIMILAR_TOXIN_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BIO_LABEL_SPIKE","symbol":"068270","name":"셀트리온","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":178700,"peak_high":197000,"peak_date":"2024-05-07","worst_low_after_entry":169700,"worst_low_after_entry_date":"2024-04-17","mfe_pct":10.2,"mae_pct":-5.0,"classification":"watch_cap_biosimilar_commercialization_label_without_strong_incremental_approval_revenue_bridge","calibration_usable":true,"corporate_action_caveat_avoided":true,"evidence_family":"biosimilar_commercialization_platform_without_incremental_approval_launch_revenue_margin_bridge","residual_error":"large_bio_platform_relevance_can_overpromote_without_incremental_market_share_revenue_margin_evidence","shadow_rule_candidate":"cap_large_biosimilar_platform_at_watch_yellow_if_mfe_modest_and_incremental_bridge_missing"}
{"row_type":"case","case_id":"C23_R7L95_086900_2024_02_01","scheduled_round":"R7","scheduled_loop":95,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CDMO_BIOSIMILAR_TOXIN_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BIO_LABEL_SPIKE","symbol":"086900","name":"메디톡스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":190400,"peak_high":197600,"peak_date":"2024-02-02","worst_low_after_entry":128000,"worst_low_after_entry_date":"2024-04-17","mfe_pct":3.8,"mae_pct":-32.8,"classification":"hard_4c_candidate_botulinum_toxin_regulatory_commercialization_label_without_legal_revenue_margin_survival","calibration_usable":true,"evidence_family":"botulinum_toxin_regulatory_legal_commercialization_label_without_revenue_margin_survival","residual_error":"toxin_regulatory_salience_can_fail_when_legal_clarity_and_revenue_margin_bridge_missing","shadow_rule_candidate":"route_toxin_regulatory_label_to_hard_4c_if_mfe_shallow_mae_large_and_commercial_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":95,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CDMO_BIOSIMILAR_TOXIN_REGULATORY_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_VS_BIO_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"corporate_action_caveat_avoided_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":95,"canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","rule_id":"C23_APPROVAL_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C23, do not open Stage2-Actionable or Stage3-Green from regulatory approval, FDA/EMA/domestic approval, biosimilar, CDMO capacity, botulinum-toxin, legal settlement, license optionality, or one-week bio-stock spike labels alone. Require approved product or serviceable market, named customer/product/geography, launch/shipment/reimbursement/prescription/utilization path, manufacturing capacity and quality compliance, revenue recognition, gross margin and SG&A burden check, legal/regulatory overhang risk check, and post-trigger price survival. Large CDMO positives may be Actionable when customer/capacity/quality/revenue/margin bridge confirms, but Green remains capped without fresh execution. Large biosimilar platforms with modest MFE should cap at Watch/Yellow without incremental approval-launch-revenue evidence. Toxin or legal/regulatory labels with shallow MFE and high MAE should route to hard-4C when legal clarity and commercial revenue bridge are missing.","expected_effect":"Preserve true bio commercialization positives while reducing generic approval/regulatory-label and legal-overhang false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":95,"canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","residual_type":"bio_approval_commercialization_revenue_margin_guard","contribution":"Adds one CDMO commercialization positive, one biosimilar platform Watch cap, and one toxin regulatory/commercialization hard-4C counterexample to calibrate C23 approval, launch, revenue, legal-overhang, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C23_APPROVAL_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION:

  Do not open Stage3-Green from:
    - regulatory approval headline alone
    - FDA / EMA / domestic approval label alone
    - biosimilar or biologics label alone
    - CDMO capacity label alone
    - botulinum-toxin or aesthetic drug label alone
    - legal / settlement / license optionality alone
    - one-week bio-stock volume spike alone

  Require at least two of:
    - approved product or serviceable market
    - named customer / product / geography
    - launch / shipment / reimbursement / prescription / utilization path
    - manufacturing capacity and quality compliance
    - revenue recognition
    - gross margin and SG&A burden check
    - legal / regulatory overhang risk control
    - low-MAE post-trigger price survival
    - fresh evidence after the approval/commercialization headline

  If MFE < 8% and MAE < -30%:
    route to C23 hard-4C candidate.

  If MFE is modest and MAE is controlled:
    cap at Watch/Yellow unless incremental launch/revenue evidence is explicit.

  If MFE is meaningful and MAE controlled:
    allow capped Actionable only when commercialization and margin bridge are visible.

  Distinguish:
    - CDMO/commercial platforms where capacity and customers become revenue and margin
    - from bio labels where approval or legal optionality does not reach commercial execution.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_95_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C23 bio regulatory/commercialization cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C23_APPROVAL_COMMERCIALIZATION_REVENUE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C23 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C23 cases agree, consider implementing a canonical guard that:
   - blocks bio-label Green without approval-to-launch/revenue/margin bridge,
   - preserves CDMO positives only with price survival and current execution evidence,
   - caps large biosimilar labels at Watch/Yellow without incremental launch evidence,
   - routes shallow-MFE/high-MAE toxin/regulatory/legal optionality labels to hard-4C.

Expected next schedule:
completed_round = R7
completed_loop = 95
next_round = R8
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 95
next_round = R8
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
