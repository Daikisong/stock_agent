# E2R Stock-Web v12 Residual Research — R10 / Loop 97

```yaml
scheduled_round: R10
scheduled_loop: 97
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE

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
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
mep_building_services_case_count: 2
industrial_epc_case_count: 1
project_cashflow_receivables_bridge_missing_count: 2
construction_label_to_margin_bridge_missing_count: 2
row_presence_or_old_corporate_action_caveat_count: 2
name_change_or_old_raw_discontinuity_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 97
next_round: R11
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 97
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is a hard L9 construction / real-estate / housing round.

The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

The selected fine branch is:

```text
MEP / building services / industrial EPC / specialty construction
project cashflow, receivables, backlog, cost discipline, margin, and row-trust bridge
vs generic construction-label spike
```

This deliberately avoids:
- C30 top-covered names:
  `002990`, `294870`, `375500`, `004960`, `013580`, `006360`
- recent R10 loop88~96 outputs:
  `047040`, `012630`, `021320`,
  `000720`, `003070`, `002780`,
  `014790`, `010780`, `005960`,
  `013360`, `001470`, `002410`,
  `034300`, `009410`, `002460`,
  `035890`, `013120`, `017000`,
  `001260`, `010960`, `001840`,
  `028100`, `002150`, `025950`,
  `028050`, `097230`, `026150`

Selected symbols:

```text
011560 세보엠이씨
010400 우진아이엔에스
016250 SGC E&C / SGC이테크건설
```

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

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
011560: same archetype, new symbol, MEP/building-services local positive with Green cap after large MFE
010400: same archetype, new symbol, building-services contractor hard-4C candidate with shallow MFE and severe MAE
016250: same archetype, new symbol, industrial EPC / plant construction Watch cap with name-change and stale project-cashflow bridge
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
011560 세보엠이씨
  profile: atlas/symbol_profiles/011/011560.json
  first_date: 1996-12-23
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,770
  non_tradable_zero_volume rows: 509
  corporate_action_candidate_dates:
    1999-09-21, 1999-10-11, 2000-11-20, 2005-05-16, 2006-04-28
  2024 entry~D+180 contamination: none
  caveat:
    high historical non-tradable zero-volume count and old raw-discontinuity caveat exist outside the selected 2024 validation window.

010400 우진아이엔에스
  profile: atlas/symbol_profiles/010/010400.json
  first_date: 2018-09-14
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,822
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

016250 SGC E&C / SGC이테크건설
  profile: atlas/symbol_profiles/016/016250.json
  name history:
    이테크이앤씨 -> 이테크건설 -> SGC이테크건설 -> SGC E&C
  selected early-2024 trigger name:
    SGC이테크건설
  later 2024 name:
    SGC E&C from 2024-04-19
  first_date: 1999-12-28
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,413
  non_tradable_zero_volume rows: 30
  corporate_action_candidate_dates:
    2020-12-08, 2021-04-09, 2022-04-08, 2023-04-07, 2025-06-25
  2024 entry~D+180 contamination: none
  caveat:
    2024 name-change narrative caveat, but no 2024 corporate-action candidate inside the selected validation window.
```

---

## 4. Archetype residual problem

C30 is about PF, construction project cashflow, receivables, backlog quality, cost escalation, accounting/listing trust, and margin survival. It is not a generic "construction contractor stock moved" archetype.

The model can over-score:

```text
MEP / building services label
plant / industrial EPC label
specialty construction label
construction policy or infrastructure theme
private-sector building CAPEX or cleanroom capex readthrough
low-PBR construction contractor label
one-week construction-stock volume spike
```

The C30 bridge must be stricter:

```text
construction / engineering / building-services event
  -> company-specific project exposure
  -> backlog quality and execution timing
  -> project cash collection and receivables
  -> cost escalation, subcontractor, and labor risk
  -> funding terms and working-capital burden
  -> margin / FCF conversion
  -> accounting / listing / tradeability trust
  -> price survival after the first construction-label spike
```

A C30 thesis is like a project ledger in a site office. A new contract board may look impressive, but the equity only improves when work is billed, receivables become cash, cost overruns are contained, and the margin line is trusted.

---

## 5. Case 1 — 011560 세보엠이씨

```yaml
case_id: C30_R10L97_011560_2024_02_01
symbol: "011560"
name: "세보엠이씨"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 8520
classification: positive_mep_building_services_project_backlog_cashflow_bridge_with_green_cap_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

세보엠이씨 is the constructive C30 control in this set.

The useful C30 read is not simply:

```text
건설 / 설비공사업체가 강하다
```

It is:

```text
MEP / building services contractor relevance
  -> project backlog and execution timing
  -> receivables-to-cash and cost discipline
  -> strong May price confirmation
  -> Green cap after large rerating
```

The forward path produced a very large MFE from the February entry. MAE was controlled. This preserves positive classification. However, Green should still be capped after a large rerating unless project cash collection, receivables, cost discipline, and margin evidence refresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 8,520 / close 8,520
2024-02-21: high 9,500 / close 8,560
2024-03-11: high 9,650 / close 9,400
2024-05-22: high 13,860 / close 13,210
2024-05-29: high 14,940 / close 14,500
2024-08-05: low 9,300 / close 9,670
2024-10-29: high 10,300 / close 10,250
```

Approximate path from entry close:

```text
entry_close: 8,520
peak_high: 14,940
MFE: +75.4%
worst_low_after_entry: 8,460
MAE: -0.7%
```

### Interpretation

This is a C30 positive with Green cap:

```text
Stage2-Actionable: possible if project exposure, backlog quality, receivables, and margin bridge are explicit.
Stage3-Green: blocked unless fresh project-cashflow and cost-discipline evidence appears after the large MFE.
Local 4B: monitor after +70% MFE if execution evidence becomes stale.
Hard 4C: no.
Row/tradeability caveat: historical only, outside 2024 validation window.
```

### Stress-test components

```text
raw_component_score_proxy:
  mep_building_services_relevance: high
  project_backlog_bridge: medium_high
  receivables_cash_collection_bridge: medium
  cost_subcontractor_labor_bridge: medium
  margin_fcf_bridge: medium_high
  price_confirmation: very_high
  drawdown_penalty: very_low
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 010400 우진아이엔에스

```yaml
case_id: C30_R10L97_010400_2024_02_01
symbol: "010400"
name: "우진아이엔에스"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5200
classification: hard_4c_candidate_building_services_contractor_label_without_project_cashflow_margin_survival
calibration_usable: true
```

### Evidence interpretation

우진아이엔에스 is the hard C30 guardrail.

The setup can look relevant:

```text
building services / mechanical installation / construction contractor
  -> private building CAPEX or public construction readthrough
  -> small contractor recovery label
  -> low-float construction-stock beta
```

But from the selected February entry, the stock produced only shallow MFE and then entered a hard drawdown zone. The project-cashflow, receivables, backlog, cost-control, and margin bridge was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,380 / close 5,200
2024-02-19: high 5,410 / close 5,370
2024-04-17: low 4,415 / close 4,435
2024-08-05: low 3,000 / close 3,020
2024-09-12: low 3,165 / close 3,180
2024-10-31: low 3,165 / close 3,180
```

Approximate path from entry close:

```text
entry_close: 5,200
peak_high_after_entry: 5,410
MFE: +4.0%
worst_low_after_entry: 3,000
MAE: -42.3%
```

### Interpretation

This is a hard C30 false-positive:

```text
Stage2-Watch: possible from building-services and construction relevance.
Stage2-Actionable: blocked unless named project, backlog, receivables, cost control, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that a building-services contractor label is not project-cashflow survival.

### Stress-test components

```text
raw_component_score_proxy:
  building_services_label: high
  project_exposure_bridge: weak
  receivables_cashflow_bridge: weak
  cost_margin_bridge: weak
  working_capital_bridge: weak_to_medium
  price_confirmation_after_entry: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 016250 SGC E&C / SGC이테크건설

```yaml
case_id: C30_R10L97_016250_2024_02_01
symbol: "016250"
name_at_trigger: "SGC이테크건설"
later_2024_name: "SGC E&C"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 18790
classification: watch_cap_industrial_epc_contractor_label_without_fresh_project_cashflow_margin_bridge
calibration_usable: true
```

### Evidence interpretation

SGC이테크건설 / SGC E&C is the industrial EPC / plant-construction Watch cap.

The label is relevant:

```text
industrial EPC / plant construction contractor
  -> project backlog and execution timing
  -> industrial capex and construction-margin optionality
```

But from the selected February entry, the path did not validate Actionable/Green. Incremental MFE was shallow, and the stock drew down materially into spring and autumn. It did not cross the hard threshold, but the project-cashflow and margin bridge was not strong enough for Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 19,100 / close 18,790
2024-02-02: high 19,110 / close 18,590
2024-04-17: low 15,010 / close 15,010
2024-08-05: high 18,740 / low 15,640 / close 17,400
2024-10-29: low 15,080 / close 15,170
2024-11-04: low 14,600 / close 15,170
```

Approximate path from entry close:

```text
entry_close: 18,790
peak_high_after_entry: 19,110
MFE: +1.7%
worst_low_after_entry: 14,600
MAE: -22.3%
```

### Interpretation

This is a Watch/Yellow cap:

```text
Stage2-Watch: valid from industrial EPC and plant-construction relevance.
Stage2-Actionable: blocked unless project exposure, execution timing, receivables, working capital, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MAE did not cross the hard threshold.
Name-change caveat: yes, 2024 SGC이테크건설 -> SGC E&C.
```

The lesson is that an industrial EPC label is not project cash collection.

### Stress-test components

```text
raw_component_score_proxy:
  industrial_epc_relevance: high
  project_backlog_bridge: weak_to_medium
  receivables_cashflow_bridge: weak
  cost_margin_bridge: weak_to_medium
  price_confirmation: shallow
  drawdown_penalty: material
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
mep_building_services_case_count: 2
industrial_epc_case_count: 1
project_cashflow_receivables_bridge_missing_count: 2
construction_label_to_margin_bridge_missing_count: 2
row_presence_or_old_corporate_action_caveat_count: 2
name_change_or_old_raw_discontinuity_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C30 MEP / industrial EPC grid:

```text
011560 세보엠이씨:
  MEP / building-services local positive;
  large MFE and low MAE, but Green requires fresh receivables/cashflow/margin evidence.

010400 우진아이엔에스:
  building-services contractor label failed;
  shallow MFE and high MAE, hard 4C.

016250 SGC E&C / SGC이테크건설:
  industrial EPC contractor relevance;
  shallow MFE and material MAE, Watch/Yellow cap.
```

Shared rule:

```text
C30 is not "construction contractor label is hot."
C30 is "project exposure, receivables, cash collection, backlog quality, cost risk, working capital, margin/FCF conversion, and tradeability trust are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L97_011560_2024_02_01","scheduled_round":"R10","scheduled_loop":97,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"011560","name":"세보엠이씨","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":8520,"peak_high":14940,"peak_date":"2024-05-29","worst_low_after_entry":8460,"worst_low_after_entry_date":"2024-02-06","mfe_pct":75.4,"mae_pct":-0.7,"classification":"positive_mep_building_services_project_backlog_cashflow_bridge_with_green_cap_after_large_mfe","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"mep_building_services_project_backlog_receivables_cash_collection_cost_margin_bridge","residual_error":"positive_mep_construction_path_requires_green_cap_after_large_mfe_without_refreshed_project_cashflow_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_project_backlog_receivables_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C30_R10L97_010400_2024_02_01","scheduled_round":"R10","scheduled_loop":97,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"010400","name":"우진아이엔에스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5200,"peak_high":5410,"peak_date":"2024-02-19","worst_low_after_entry":3000,"worst_low_after_entry_date":"2024-08-05","mfe_pct":4.0,"mae_pct":-42.3,"classification":"hard_4c_candidate_building_services_contractor_label_without_project_cashflow_margin_survival","calibration_usable":true,"evidence_family":"building_services_contractor_label_without_named_project_receivables_cost_margin_bridge","residual_error":"building_services_contractor_label_can_fail_when_project_cashflow_and_margin_bridge_missing","shadow_rule_candidate":"route_building_services_contractor_label_to_hard_4c_if_mfe_shallow_mae_large_and_cashflow_bridge_missing"}
{"row_type":"case","case_id":"C30_R10L97_016250_2024_02_01","scheduled_round":"R10","scheduled_loop":97,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"016250","name_at_trigger":"SGC이테크건설","later_2024_name":"SGC E&C","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":18790,"peak_high":19110,"peak_date":"2024-02-02","worst_low_after_entry":14600,"worst_low_after_entry_date":"2024-11-04","mfe_pct":1.7,"mae_pct":-22.3,"classification":"watch_cap_industrial_epc_contractor_label_without_fresh_project_cashflow_margin_bridge","calibration_usable":true,"name_change_or_old_raw_discontinuity_caveat":true,"evidence_family":"industrial_epc_plant_construction_label_without_refreshed_project_receivables_working_capital_margin_bridge","residual_error":"industrial_epc_relevance_can_overpromote_without_project_cashflow_and_margin_refresh","shadow_rule_candidate":"cap_industrial_epc_contractor_label_at_watch_yellow_if_mfe_shallow_and_project_cashflow_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":97,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"mep_building_services_case_count":2,"industrial_epc_case_count":1,"project_cashflow_receivables_bridge_missing_count":2,"construction_label_to_margin_bridge_missing_count":2,"row_presence_or_old_corporate_action_caveat_count":2,"name_change_or_old_raw_discontinuity_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":97,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_MEP_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30 MEP/building-services/industrial-EPC/specialty-construction cases, do not open Stage2-Actionable or Stage3-Green from MEP, building services, mechanical installation, plant construction, industrial EPC, specialty contractor, construction policy, private building CAPEX, cleanroom capex readthrough, low-PBR construction contractor, or one-week construction-stock volume-spike labels alone. Require company-specific project exposure, backlog quality and execution timing, project cash collection and receivables, cost escalation/subcontractor/labor risk control, funding terms and working-capital burden, margin/FCF conversion, accounting/listing/tradeability trust, and post-trigger price survival. MEP positives with large MFE may be capped Actionable when project backlog, receivables, and margin bridge are explicit, but Green requires fresh evidence. Building-services labels with shallow MFE and high MAE should route to hard-4C when project cashflow and margin bridge are missing. Industrial-EPC labels with shallow MFE and material MAE should cap at Watch/Yellow unless project-cashflow evidence refreshes.","expected_effect":"Preserve true construction project-cashflow positives while reducing MEP/building-services/EPC contractor label false positives where receivables, cost, working-capital, margin, and trust evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":97,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"mep_epc_project_cashflow_receivables_margin_trust_guard","contribution":"Adds one MEP/building-services positive, one building-services hard-4C, and one industrial EPC Watch cap to calibrate C30 project exposure, receivables, cash collection, cost risk, working capital, margin/FCF, and row/tradeability trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_MEP_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
AND company_type in [mep_building_services, mechanical_installation, industrial_epc, plant_construction, specialty_contractor]:

  Do not open Stage3-Green from:
    - MEP / building-services label alone
    - mechanical installation / plant construction label alone
    - industrial EPC label alone
    - construction policy or infrastructure theme alone
    - private building CAPEX or cleanroom capex readthrough alone
    - low-PBR construction-contractor rerating alone
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

  If MFE < 8% and MAE < -35%:
    route to C30 hard-4C candidate.

  If MFE > 20% but project-cashflow evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is shallow and the bridge is contractor label only:
    cap at Watch/Yellow unless receivables and margin evidence refreshes.

  If row-presence or old corporate-action caveat exists:
    apply additional trust cap, but do not contaminate clean 2024 rows.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_97_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 MEP/building-services/industrial-EPC cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_MEP_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks MEP/building-services/EPC Green without project exposure, backlog, receivables, cost risk, working capital, and margin bridge,
   - preserves MEP positives only with price survival and fresh project-cashflow evidence,
   - routes shallow-MFE/high-MAE building-services labels to hard-4C,
   - caps shallow-MFE/material-MAE industrial-EPC labels at Watch/Yellow,
   - applies row-presence, old corporate-action, and name-change trust caveats.

Expected next schedule:
completed_round = R10
completed_loop = 97
next_round = R11
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 97
next_round = R11
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
