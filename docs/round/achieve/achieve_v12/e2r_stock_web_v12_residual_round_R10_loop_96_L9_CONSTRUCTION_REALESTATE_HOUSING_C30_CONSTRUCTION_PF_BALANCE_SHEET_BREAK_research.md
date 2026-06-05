# E2R Stock-Web v12 Residual Research — R10 / Loop 96

```yaml
scheduled_round: R10
scheduled_loop: 96
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE

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
hard_4c_candidate_count: 2
epc_engineering_case_count: 1
civil_specialty_construction_case_count: 1
mixed_construction_shipbuilding_case_count: 1
name_change_caveat_count: 1
row_presence_or_tradeability_caveat_count: 2
project_cashflow_trust_bridge_missing_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 96
next_round: R11
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 96
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is a hard L9 construction / real-estate / housing round.

The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

The selected fine branch is:

```text
EPC engineering / civil specialty construction / mixed construction contractor
project cashflow, receivables, backlog, margin, and tradeability trust bridge
vs generic construction-label spike
```

This deliberately avoids:
- the loop95 R10 engineering / groundwork / small-builder set: `028100`, `002150`, `025950`;
- the loop94 small/regional/civil-builder set: `001260`, `010960`, `001840`;
- the loop93 regional housing branch: `035890`, `013120`, `017000`;
- the loop92 PF-workout branch: `034300`, `009410`, `002460`;
- the C30 top-covered names.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rows: 81
symbols: 31
date_range: 2022-01-12~2024-08-26
good/bad S2: 16/29
4B/4C: 3/4
URL pending/proxy: 20/25
top covered symbols:
  002990(6), 294870(6), 375500(6), 004960(5), 013580(5), 006360(4)
```

Recent R10 outputs already used:

```text
loop88: 047040, 012630, 021320
loop89: 000720, 003070, 002780
loop90: 014790, 010780, 005960
loop91: 013360, 001470, 002410
loop92: 034300, 009410, 002460
loop93: 035890, 013120, 017000
loop94: 001260, 010960, 001840
loop95: 028100, 002150, 025950
```

Selected symbols:

```text
028050 삼성엔지니어링 / 삼성E&A
097230 HJ중공업
026150 특수건설
```

They avoid the C30 top-covered list and avoid recent R10 loop88~95 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
028050: same archetype, new symbol, EPC engineering / project-backlog positive with name-change caveat and 4B after later MAE
097230: same archetype, new symbol, mixed construction / shipbuilding contractor hard-4C without project-cashflow trust survival
026150: same archetype, new symbol, civil specialty construction event-spike hard-4C with row/tradeability caveat
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
028050 삼성엔지니어링 / 삼성E&A
  profile: atlas/symbol_profiles/028/028050.json
  name history:
    삼성엔지니어링 from 2002-02-19 to 2024-04-05
    삼성E&A from 2024-04-08
  selected 2024 trigger name:
    삼성엔지니어링
  later 2024 name:
    삼성E&A
  first_date: 1997-01-03
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,265
  non_tradable_zero_volume rows: 13
  corporate_action_candidate_dates:
    historical only, latest 2016-02-26
  2024 entry~D+180 contamination: none
  caveat:
    2024 name change affects narrative labeling, not the raw-price validation window.

097230 HJ중공업
  profile: atlas/symbol_profiles/097/097230.json
  name history:
    한진중공업 until 2022-01-13
    HJ중공업 from 2022-01-14
  first_date: 2007-08-31
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,493
  non_tradable_zero_volume rows: 60
  corporate_action_candidate_dates:
    2013-04-05, 2014-08-29, 2019-05-21, 2019-05-23
  2024 entry~D+180 contamination: none
  caveat:
    mixed construction / shipbuilding identity and historical row-presence caveat require trust cap.

026150 특수건설
  profile: atlas/symbol_profiles/026/026150.json
  first_date: 1997-08-06
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,709
  non_tradable_zero_volume rows: 391
  corporate_action_candidate_dates:
    1998-01-15, 2000-05-02, 2009-07-15, 2018-11-02
  2024 entry~D+180 contamination: none
  caveat:
    high historical non-tradable zero-volume count adds row/tradeability trust cap even though 2024 window is clean.
```

---

## 4. Archetype residual problem

C30 is about PF, project cashflow, receivables, backlog quality, cost overrun risk, accounting trust, and tradeability. It is not a generic "construction stock is moving" archetype.

The model can over-score:

```text
EPC / plant engineering label
civil specialty construction label
underground / tunnel / rail-infrastructure label
mixed construction / shipbuilding contractor label
construction policy or infrastructure theme
one-week construction-stock volume spike
```

The C30 bridge must be stricter:

```text
construction / engineering / infrastructure event
  -> company-specific project exposure
  -> backlog quality and execution timing
  -> project cash collection and receivables
  -> cost escalation, subcontractor, and labor risk
  -> funding terms and working-capital burden
  -> margin / FCF conversion
  -> accounting / listing / tradeability trust
  -> price survival after the first construction-label spike
```

A C30 thesis is like a construction site ledger. A new project signboard may look impressive, but equity value only improves when the work is billed, cash is collected, cost overruns are contained, and the ledger is trusted.

---

## 5. Case 1 — 028050 삼성엔지니어링 / 삼성E&A

```yaml
case_id: C30_R10L96_028050_2024_02_01
symbol: "028050"
name_at_trigger: "삼성엔지니어링"
current_or_later_2024_name: "삼성E&A"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 23250
classification: local_positive_epc_engineering_project_backlog_cashflow_bridge_with_name_change_and_4b_after_later_mae
calibration_usable: true
```

### Evidence interpretation

삼성엔지니어링 / 삼성E&A is the constructive C30 control in this set.

The useful C30 read is not simply:

```text
EPC / 건설 엔지니어링주가 강하다
```

It is:

```text
EPC engineering and project-backlog relevance
  -> order backlog and execution timing
  -> project cashflow and receivables bridge
  -> cost and margin discipline
  -> strong initial price confirmation
```

The forward path produced a meaningful MFE into July/August. But the later drawdown into the autumn shows that even a high-quality EPC name needs refreshed project-cash, backlog, and margin evidence before it stays Green. The 2024 name change from 삼성엔지니어링 to 삼성E&A is a narrative caveat, not a price-discontinuity contamination.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 23,300 / close 23,250
2024-02-28: high 26,350 / close 26,000
2024-03-15: high 28,150 / close 25,700
2024-04-30: high 27,000 / close 26,450
2024-07-30: high 29,300 / close 28,300
2024-08-01: high 29,300 / close 28,400
2024-08-05: low 23,450 / close 24,600
2024-09-27: low 22,350 / close 22,350
2024-10-25: low 18,180 / close 18,420
2024-11-01: low 17,550 / close 17,800
```

Approximate path from entry close:

```text
entry_close: 23,250
peak_high: 29,300
MFE: +26.0%
worst_low_after_entry: 17,550
MAE: -24.5%
```

### Interpretation

This is a C30 local positive with 4B after later MAE:

```text
Stage2-Actionable: possible only if backlog, project execution, receivables, and margin bridge are explicit.
Stage3-Green: blocked without fresh project-cash and cost-discipline evidence.
Local 4B: required after +26% MFE and later material MAE.
Hard 4C: no, because meaningful MFE came first and MAE did not cross the hard threshold.
Name-change caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  epc_engineering_relevance: high
  project_backlog_bridge: medium_high
  receivables_cashflow_bridge: medium
  cost_margin_bridge: medium
  price_confirmation: high_initial
  post_rerating_survival: weak_later
  local_4b_overlay: required
```

---

## 6. Case 2 — 097230 HJ중공업

```yaml
case_id: C30_R10L96_097230_2024_02_01
symbol: "097230"
name: "HJ중공업"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3480
classification: hard_4c_candidate_mixed_construction_shipbuilding_label_without_project_cashflow_trust_survival
calibration_usable: true
```

### Evidence interpretation

HJ중공업 is the mixed construction / shipbuilding hard guardrail.

The label can appear relevant:

```text
construction and infrastructure contractor
shipbuilding / heavy-industry overlap
public project and civil-work optionality
turnaround or balance-sheet repair hope
```

But from the selected February trigger, the price path did not validate C30 project-cashflow repair. MFE was shallow, and the stock later fell into a hard drawdown zone. The mixed identity also creates a cross-sector interpretation problem: shipbuilding/heavy-industry salience should not be counted as C30 PF or construction cashflow repair unless the project cash and trust bridge is explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 3,500 / close 3,480
2024-02-07: high 3,735 / close 3,735
2024-03-13: high 3,720 / close 3,420
2024-04-16: low 2,875 / close 2,890
2024-08-05: low 2,700 / close 2,790
2024-09-09: low 2,585 / close 2,705
2024-10-25: low 2,200 / close 2,210
2024-10-31: low 2,180 / close 2,290
```

Approximate path from entry close:

```text
entry_close: 3,480
peak_high: 3,735
MFE: +7.3%
worst_low_after_entry: 2,180
MAE: -37.4%
```

### Interpretation

This is a hard C30 false-positive:

```text
Stage2-Watch: possible from construction / infrastructure relevance.
Stage2-Actionable: blocked unless project cash collection, receivables, funding, backlog, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -35%+ MAE.
Cross-sector caveat: yes, construction / shipbuilding identity can distort the C30 read.
Row/tradeability caveat: yes, historical non-tradable zero-volume rows exist outside the 2024 window.
```

The lesson is that a mixed contractor label is not project-cashflow trust.

### Stress-test components

```text
raw_component_score_proxy:
  construction_infra_relevance: medium_high
  shipbuilding_cross_sector_confound: high
  project_cashflow_bridge: weak
  receivables_backlog_bridge: weak_to_medium
  margin_fcf_bridge: weak
  trust_bridge: weak_to_medium
  price_confirmation_after_entry: failed
  hard_4c_guard: yes
```

---

## 7. Case 3 — 026150 특수건설

```yaml
case_id: C30_R10L96_026150_2024_07_30
symbol: "026150"
name: "특수건설"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE
trigger_date: 2024-07-30
entry_date: 2024-07-30
entry_price_basis: close
entry_price: 7920
classification: hard_4c_candidate_civil_specialty_construction_event_spike_without_project_cashflow_margin_trust_survival
calibration_usable: true
```

### Evidence interpretation

특수건설 is the civil specialty-construction event-spike hard guardrail.

The setup can fool a construction-policy model:

```text
specialty civil construction
underground / tunnel / rail-infrastructure label
one-day construction-policy or infrastructure spike
small-cap construction beta
```

But from the selected July spike close, the stock produced only a shallow MFE and then moved into a hard drawdown zone. The bridge from infrastructure label to named project, backlog quality, receivables, cash collection, and margin survival was missing. The high historical non-tradable zero-volume count adds a trust cap.

### Price path

Key Stock-Web rows:

```text
2024-07-24: close 6,780
2024-07-30: high 8,090 / close 7,920
2024-07-31: high 8,140 / close 7,460
2024-08-05: low 6,350 / close 6,460
2024-08-29: low 6,160 / close 6,200
2024-09-09: low 5,530 / close 5,840
2024-10-21: low 5,470 / close 5,500
2024-10-23: high 7,000 / close 6,470
```

Approximate path from event-spike close:

```text
entry_close: 7,920
peak_high_after_entry: 8,140
MFE: +2.8%
worst_low_after_entry: 5,470
MAE: -30.9%
```

### Interpretation

This is a hard C30 false-positive candidate:

```text
Stage2-Watch: possible from specialty civil construction and infrastructure relevance.
Stage2-Actionable: blocked unless named project, cash collection, backlog execution, cost risk, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes by shallow MFE and -30%+ MAE.
Row/tradeability caveat: yes, high historical zero-volume count.
```

The lesson is that tunnel / infrastructure price heat is not project cashflow.

### Stress-test components

```text
raw_component_score_proxy:
  civil_specialty_construction_label: high
  infrastructure_policy_signal: medium_high
  named_project_bridge: weak
  receivables_cashflow_bridge: weak
  cost_margin_bridge: weak
  price_confirmation_after_entry: failed
  row_tradeability_trust: weak_to_medium
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
epc_engineering_case_count: 1
civil_specialty_construction_case_count: 1
mixed_construction_shipbuilding_case_count: 1
name_change_caveat_count: 1
row_presence_or_tradeability_caveat_count: 2
project_cashflow_trust_bridge_missing_count: 2
calibration_usable_trigger_count: 3
```

The three-case C30 EPC / specialty-construction grid:

```text
028050 삼성엔지니어링 / 삼성E&A:
  EPC engineering local positive;
  meaningful MFE first, later material MAE, 4B required.

097230 HJ중공업:
  mixed construction / shipbuilding contractor failed;
  shallow MFE and high MAE, hard 4C.

026150 특수건설:
  specialty civil-construction event spike failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C30 is not "construction or infrastructure label is hot."
C30 is "project exposure, project cash collection, receivables, backlog quality, funding, cost risk, margin, FCF, and tradeability trust are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L96_028050_2024_02_01","scheduled_round":"R10","scheduled_loop":96,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"028050","name_at_trigger":"삼성엔지니어링","current_or_later_2024_name":"삼성E&A","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":23250,"peak_high":29300,"peak_date":"2024-07-30","worst_low_after_entry":17550,"worst_low_after_entry_date":"2024-11-01","mfe_pct":26.0,"mae_pct":-24.5,"classification":"local_positive_epc_engineering_project_backlog_cashflow_bridge_with_name_change_and_4b_after_later_mae","calibration_usable":true,"name_change_caveat":true,"evidence_family":"epc_engineering_project_backlog_receivables_cashflow_cost_margin_bridge","residual_error":"epc_project_backlog_positive_requires_4b_after_material_mae_without_refreshed_project_cashflow_margin_evidence","shadow_rule_candidate":"preserve_epc_engineering_positive_but_attach_4b_after_mfe_when_project_cashflow_bridge_is_not_refreshed"}
{"row_type":"case","case_id":"C30_R10L96_097230_2024_02_01","scheduled_round":"R10","scheduled_loop":96,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"097230","name":"HJ중공업","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3480,"peak_high":3735,"peak_date":"2024-02-07","worst_low_after_entry":2180,"worst_low_after_entry_date":"2024-10-31","mfe_pct":7.3,"mae_pct":-37.4,"classification":"hard_4c_candidate_mixed_construction_shipbuilding_label_without_project_cashflow_trust_survival","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"cross_sector_confound_caveat":true,"evidence_family":"mixed_construction_shipbuilding_label_without_project_cashflow_receivables_margin_trust_bridge","residual_error":"mixed_contractor_label_can_fail_when_project_cashflow_and_trust_bridge_missing","shadow_rule_candidate":"route_mixed_construction_shipbuilding_label_to_hard_4c_if_mfe_shallow_mae_large_and_cashflow_bridge_missing"}
{"row_type":"case","case_id":"C30_R10L96_026150_2024_07_30","scheduled_round":"R10","scheduled_loop":96,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"026150","name":"특수건설","trigger_date":"2024-07-30","entry_date":"2024-07-30","entry_price":7920,"peak_high":8140,"peak_date":"2024-07-31","worst_low_after_entry":5470,"worst_low_after_entry_date":"2024-10-21","mfe_pct":2.8,"mae_pct":-30.9,"classification":"hard_4c_candidate_civil_specialty_construction_event_spike_without_project_cashflow_margin_trust_survival","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"civil_specialty_construction_infra_event_spike_without_named_project_receivables_cashflow_margin_bridge","residual_error":"specialty_construction_event_spike_can_fail_when_project_cashflow_and_margin_bridge_missing","shadow_rule_candidate":"route_civil_specialty_construction_spike_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_project_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":96,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"epc_engineering_case_count":1,"civil_specialty_construction_case_count":1,"mixed_construction_shipbuilding_case_count":1,"name_change_caveat_count":1,"row_presence_or_tradeability_caveat_count":2,"project_cashflow_trust_bridge_missing_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":96,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30 EPC engineering, civil specialty construction, mixed contractor, infrastructure, and small-builder cases, do not open Stage2-Actionable or Stage3-Green from EPC/plant engineering, civil specialty construction, tunnel/rail/underground infrastructure, mixed construction/shipbuilding contractor, construction policy, infrastructure theme, or one-week construction-stock spike labels alone. Require company-specific project exposure, backlog quality and execution timing, project cash collection and receivables, cost escalation/subcontractor/labor risk control, funding terms and working-capital burden, margin/FCF conversion, accounting/listing/tradeability trust, and post-trigger price survival. EPC engineering positives with meaningful MFE followed by material MAE should remain local 4B unless project-cashflow and margin evidence refreshes. Mixed contractor labels with cross-sector confounds should route to hard-4C when construction cashflow and trust bridge are missing. Civil specialty construction event spikes with shallow MFE and hard-zone MAE should route to hard-4C, especially when row/tradeability caveats exist.","expected_effect":"Reduce construction-label, EPC-theme, mixed-contractor, and civil-specialty late-spike false positives while preserving project-cashflow positives with receivables, backlog, cost, margin, and trust evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":96,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"project_cashflow_receivables_margin_trust_guard","contribution":"Adds one EPC engineering local positive, one mixed construction/shipbuilding hard-4C, and one civil specialty construction hard-4C candidate to calibrate C30 project cashflow, receivables, backlog quality, cost risk, margin, and tradeability trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
AND company_type in [epc_engineering, civil_specialty_construction, mixed_contractor, infrastructure_contractor, small_builder]:

  Do not open Stage3-Green from:
    - EPC / plant engineering label alone
    - civil specialty construction label alone
    - tunnel / rail / underground infrastructure label alone
    - mixed construction / shipbuilding contractor label alone
    - construction policy or infrastructure theme alone
    - one-week construction-stock volume spike alone

  Require at least two of:
    - company-specific project exposure
    - backlog quality and execution timing
    - project cash collection and receivables
    - cost escalation / subcontractor / labor-risk containment
    - funding terms / working-capital burden clarity
    - margin / FCF conversion
    - accounting / listing / tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the construction-project headline

  If MFE < 10% and MAE < -30%:
    route to C30 hard-4C candidate.

  If MFE > 15% but later MAE is material:
    preserve as local 4B / capped positive, not Green, unless project-cashflow and margin evidence appears.

  If mixed-sector confound exists:
    require the construction-specific cashflow bridge before counting the move as C30 validation.

  If row-presence or tradeability caveat exists:
    apply additional trust cap.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_96_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 EPC / civil specialty construction / mixed contractor cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks EPC/construction-label Green without project exposure, project cashflow, receivables, backlog quality, cost risk, and margin bridge,
   - preserves EPC positives only with price survival and fresh project-cashflow evidence,
   - routes mixed construction/shipbuilding labels to hard-4C when construction cashflow bridge is missing,
   - routes civil specialty construction event spikes with shallow-MFE/hard-zone-MAE to hard-4C,
   - applies name-change, row-presence, and tradeability caveats.

Expected next schedule:
completed_round = R10
completed_loop = 96
next_round = R11
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 96
next_round = R11
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
