# E2R Stock-Web v12 Residual Research — R1 / Loop 97

```yaml
scheduled_round: R1
scheduled_loop: 97
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_DESIGN_MAINTENANCE_OPERATION_POLICY_PROJECT_AWARD_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_POLICY_LABEL_SPIKE

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
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
nuclear_design_engineering_case_count: 1
nuclear_maintenance_service_case_count: 1
nuclear_operation_policy_late_chase_case_count: 1
project_award_legal_delay_bridge_missing_count: 1
policy_to_margin_bridge_missing_count: 1
row_presence_or_tradeability_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 97
next_round: R2
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_96_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 97
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 hard gate requires:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage:

```text
loop92: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
loop93: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
loop94: C02_POWER_GRID_DATACENTER_CAPEX
loop95: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
loop96: C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

This run returns to C04 after the R1 branch cycle, but avoids the C04 top-covered names and uses a different fine branch:

```text
nuclear design engineering / nuclear maintenance service / nuclear operation contractor
project award, project delay, legal/regulatory risk, O&M service revenue, and margin bridge
vs generic nuclear-policy label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rows: 12
symbols: 7
date_range: 2022-03-10~2025-01-17
good/bad S2: 5/3
4B/4C: 1/0
URL pending/proxy: 0/0
top covered symbols:
  011700(4), 083650(3), 006910(1), 034020(1), 042370(1), 046120(1)
```

Selected symbols:

```text
051600 한전KPS
052690 한전기술
130660 한전산업
```

They avoid the C04 top-covered list and avoid recent R1 loop95~96 names:

```text
loop96 C01 avoid: 267270, 210540, 241560
loop95 C03 avoid: 064350, 272210, 448710
C04 top-covered avoid: 011700, 083650, 006910, 034020, 042370, 046120
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
051600: same archetype, new symbol, nuclear maintenance / recurring service positive with Green cap
052690: same archetype, new symbol, nuclear design / project-engineering capped positive with project-delay 4B watch
130660: same archetype, new symbol, nuclear-operation policy late chase hard-4C candidate without project-award margin bridge
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
051600 한전KPS
  profile: atlas/symbol_profiles/051/051600.json
  first_date: 2007-12-14
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,482
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

052690 한전기술
  profile: atlas/symbol_profiles/052/052690.json
  first_date: 2009-12-14
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,984
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

130660 한전산업
  profile: atlas/symbol_profiles/130/130660.json
  first_date: 2010-12-16
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,718
  non_tradable_zero_volume rows: 14
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    minor historical non-tradable zero-volume count adds a small trust cap,
    but there is no direct 2024 corporate-action contamination.
```

---

## 4. Archetype residual problem

C04 is about nuclear policy, project award, project delay, regulatory/legal risk, project economics, and margin conversion. It is not a generic "nuclear stock is hot" archetype.

The model can over-score:

```text
nuclear policy headline
Czech / overseas nuclear project rumor or preferred-bidder readthrough
SMR or reactor theme label
nuclear maintenance / design / O&M label
public utility or power-plant service label
one-week nuclear-stock volume spike
late chase after a nuclear-project news run
```

The C04 bridge must be stricter:

```text
nuclear policy / project event
  -> named project, geography, client, or contract package
  -> award status and legal / appeals / regulatory risk
  -> scope and revenue recognition timing
  -> delivery / engineering / maintenance execution
  -> margin and cost-escalation risk
  -> FX and working-capital burden
  -> recurring O&M / maintenance service stability where relevant
  -> price survival after the first nuclear-policy spike
```

A C04 nuclear thesis is like a reactor containment building. The policy headline may light up the control room, but equity value appears only when the project award is legally durable, the contract scope is clear, engineering or maintenance work is delivered, and revenue reaches margin without delays cracking the structure.

---

## 5. Case 1 — 051600 한전KPS

```yaml
case_id: C04_R1L97_051600_2024_02_01
symbol: "051600"
name: "한전KPS"
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_DESIGN_MAINTENANCE_OPERATION_POLICY_PROJECT_AWARD_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 34000
classification: positive_nuclear_maintenance_recurring_service_policy_project_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

한전KPS is the constructive C04 control in this set.

The useful C04 read is not simply:

```text
원전주가 강하다
```

It is:

```text
nuclear and thermal plant maintenance service relevance
  -> recurring O&M / inspection / outage-service revenue
  -> nuclear-policy project readthrough
  -> relatively stable downside
  -> later price confirmation
```

The forward path delivered a large MFE while maintaining a controlled drawdown. That supports positive classification. However, Green should remain capped unless O&M service order visibility, nuclear project scope, and margin evidence refreshes the thesis.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 34,500 / low 33,700 / close 34,000
2024-02-19: high 39,500 / close 38,950
2024-04-17: low 32,950 / close 33,100
2024-07-24: high 39,600 / close 38,950
2024-08-05: low 35,850 / close 37,000
2024-10-17: high 46,650 / close 44,200
2024-10-30: high 45,900 / close 45,350
```

Approximate path from entry close:

```text
entry_close: 34,000
peak_high: 46,650
MFE: +37.2%
worst_low_after_entry: 32,950
MAE: -3.1%
```

### Interpretation

This is a C04 positive with Green cap:

```text
Stage2-Actionable: possible if recurring maintenance, outage-service, nuclear scope, and margin bridge are explicit.
Stage3-Green: possible only with fresh service-order, project-scope, and margin evidence.
Local 4B: monitor after +30% MFE if policy/project evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  nuclear_maintenance_relevance: high
  recurring_service_bridge: high
  project_policy_readthrough: medium_high
  margin_op_bridge: medium_high
  price_confirmation: high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 052690 한전기술

```yaml
case_id: C04_R1L97_052690_2024_02_01
symbol: "052690"
name: "한전기술"
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_DESIGN_MAINTENANCE_OPERATION_POLICY_PROJECT_AWARD_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 64400
classification: capped_positive_nuclear_design_project_engineering_with_4b_watch_for_delay_and_award_risk
calibration_usable: true
```

### Evidence interpretation

한전기술 is the nuclear-design / project-engineering capped positive.

The setup is highly relevant:

```text
nuclear plant design and engineering
  -> overseas project / policy award readthrough
  -> design-scope and engineering margin optionality
  -> later July price confirmation
```

But C04 must not treat design relevance as automatic Green. Nuclear project cycles carry legal, appeals, regulatory, contract-scope, and timing risk. The forward path produced a meaningful MFE, but there was a material spring drawdown before the later rerating. Therefore this is a capped positive with 4B watch.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 66,200 / low 63,700 / close 64,400
2024-02-21: high 72,000 / close 71,500
2024-03-11: high 76,800 / close 71,800
2024-04-17: low 54,100 / close 54,400
2024-07-31: high 77,400 / close 76,100
2024-08-05: low 61,600 / close 63,300
2024-09-19: high 73,000 / close 72,800
```

Approximate path from entry close:

```text
entry_close: 64,400
peak_high: 77,400
MFE: +20.2%
worst_low_after_entry: 54,100
MAE: -16.0%
```

### Interpretation

This is a C04 capped positive with 4B watch:

```text
Stage2-Watch: valid from nuclear design and engineering relevance.
Stage2-Actionable: possible if named project, award status, contract scope, and timing bridge are explicit.
Stage3-Green: blocked without fresh project award, legal/regulatory clarity, and margin evidence.
Local 4B: monitor because the path includes a material pre-rerating drawdown.
Hard 4C: no.
```

The lesson is that nuclear design relevance is not the same as legally durable project revenue.

### Stress-test components

```text
raw_component_score_proxy:
  nuclear_design_relevance: very_high
  overseas_project_readthrough: high
  legal_regulatory_award_risk: medium_high
  contract_scope_bridge: weak_to_medium
  margin_op_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: medium
  local_4b_overlay: watch
```

---

## 7. Case 3 — 130660 한전산업

```yaml
case_id: C04_R1L97_130660_2024_07_24
symbol: "130660"
name: "한전산업"
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_DESIGN_MAINTENANCE_OPERATION_POLICY_PROJECT_AWARD_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_POLICY_LABEL_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 16030
classification: hard_4c_candidate_nuclear_operation_policy_late_chase_without_project_award_margin_survival
calibration_usable: true
```

### Evidence interpretation

한전산업 is the late-chase C04 guardrail.

The label can fool the model:

```text
power-plant operation / maintenance service
nuclear policy and overseas project readthrough
small-to-mid nuclear-policy beta
high-volume summer nuclear-policy spike
```

But from the selected July late-entry close, the forward path did not validate additional project award, scope, legal timing, O&M revenue, or margin evidence. MFE was shallow and the August drawdown was severe enough for a hard-4C candidate under C04 event-spike logic.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 16,270 / close 16,030
2024-07-31: high 16,680 / close 15,860
2024-08-05: low 11,920 / close 12,750
2024-08-27: low 11,860 / close 12,940
2024-09-19: high 16,720 / close 16,290
2024-10-31: low 12,600 / close 12,710
```

Approximate path from late entry close:

```text
entry_close: 16,030
peak_high_after_entry: 16,720
MFE: +4.3%
worst_low_after_entry: 11,860
MAE: -26.0%
```

### Interpretation

This is a hard C04 candidate / late-chase false-positive:

```text
Stage2-Watch: possible from nuclear O&M and policy relevance.
Stage2-Actionable: blocked unless named project, service scope, revenue timing, legal/regulatory clarity, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes by shallow MFE, large MAE, and late-policy-spike entry.
Row/tradeability caveat: minor historical zero-volume row count.
```

The lesson is that a nuclear-policy beta spike is not project-award or O&M margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  nuclear_operation_service_label: high
  policy_project_beta: high
  named_project_bridge: weak
  award_legal_timing_bridge: weak
  o_and_m_revenue_bridge: weak_to_medium
  margin_op_bridge: weak
  price_confirmation_after_entry: shallow
  drawdown_penalty: high
  hard_4c_guard: candidate
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
nuclear_design_engineering_case_count: 1
nuclear_maintenance_service_case_count: 1
nuclear_operation_policy_late_chase_case_count: 1
project_award_legal_delay_bridge_missing_count: 1
policy_to_margin_bridge_missing_count: 1
row_presence_or_tradeability_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C04 nuclear grid:

```text
051600 한전KPS:
  nuclear maintenance / recurring O&M service positive;
  strong MFE and controlled MAE, but Green requires fresh service-order and margin evidence.

052690 한전기술:
  nuclear design / engineering capped positive;
  meaningful MFE and material drawdown, 4B watch because award/legal/timing risk remains.

130660 한전산업:
  nuclear-operation policy late chase failed from the selected July entry;
  shallow MFE and large MAE, hard 4C candidate.
```

Shared rule:

```text
C04 is not "nuclear policy label is hot."
C04 is "named project, award status, legal/regulatory clarity, project scope, execution timing, O&M service revenue, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C04_R1L97_051600_2024_02_01","scheduled_round":"R1","scheduled_loop":97,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_DESIGN_MAINTENANCE_OPERATION_POLICY_PROJECT_AWARD_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_POLICY_LABEL_SPIKE","symbol":"051600","name":"한전KPS","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":34000,"peak_high":46650,"peak_date":"2024-10-17","worst_low_after_entry":32950,"worst_low_after_entry_date":"2024-04-17","mfe_pct":37.2,"mae_pct":-3.1,"classification":"positive_nuclear_maintenance_recurring_service_policy_project_bridge_with_green_cap","calibration_usable":true,"evidence_family":"nuclear_maintenance_recurring_o_and_m_service_project_policy_margin_bridge","residual_error":"positive_nuclear_service_path_requires_green_cap_without_refreshed_service_order_project_scope_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_o_and_m_service_and_margin_bridge_confirm_but_cap_green_without_fresh_project_scope_evidence"}
{"row_type":"case","case_id":"C04_R1L97_052690_2024_02_01","scheduled_round":"R1","scheduled_loop":97,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_DESIGN_MAINTENANCE_OPERATION_POLICY_PROJECT_AWARD_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_POLICY_LABEL_SPIKE","symbol":"052690","name":"한전기술","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":64400,"peak_high":77400,"peak_date":"2024-07-31","worst_low_after_entry":54100,"worst_low_after_entry_date":"2024-04-17","mfe_pct":20.2,"mae_pct":-16.0,"classification":"capped_positive_nuclear_design_project_engineering_with_4b_watch_for_delay_and_award_risk","calibration_usable":true,"evidence_family":"nuclear_design_engineering_project_award_scope_legal_delay_margin_bridge","residual_error":"nuclear_design_positive_requires_4b_watch_when_legal_award_timing_and_contract_scope_evidence_is_not_refreshed","shadow_rule_candidate":"cap_nuclear_design_project_labels_until_award_scope_legal_timing_and_margin_bridge_confirm"}
{"row_type":"case","case_id":"C04_R1L97_130660_2024_07_24","scheduled_round":"R1","scheduled_loop":97,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_DESIGN_MAINTENANCE_OPERATION_POLICY_PROJECT_AWARD_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_POLICY_LABEL_SPIKE","symbol":"130660","name":"한전산업","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":16030,"peak_high":16720,"peak_date":"2024-09-19","worst_low_after_entry":11860,"worst_low_after_entry_date":"2024-08-27","mfe_pct":4.3,"mae_pct":-26.0,"classification":"hard_4c_candidate_nuclear_operation_policy_late_chase_without_project_award_margin_survival","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"nuclear_operation_policy_late_chase_without_named_project_award_service_scope_margin_bridge","residual_error":"nuclear_policy_beta_late_chase_can_fail_when_project_award_and_o_and_m_margin_bridge_missing","shadow_rule_candidate":"route_nuclear_operation_policy_late_chase_to_hard_4c_candidate_if_mfe_shallow_mae_large_and_project_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":97,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_DESIGN_MAINTENANCE_OPERATION_POLICY_PROJECT_AWARD_LEGAL_DELAY_MARGIN_BRIDGE_VS_NUCLEAR_POLICY_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"nuclear_design_engineering_case_count":1,"nuclear_maintenance_service_case_count":1,"nuclear_operation_policy_late_chase_case_count":1,"project_award_legal_delay_bridge_missing_count":1,"policy_to_margin_bridge_missing_count":1,"row_presence_or_tradeability_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":97,"canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","rule_id":"C04_NUCLEAR_PROJECT_AWARD_LEGAL_SCOPE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C04, do not open Stage2-Actionable or Stage3-Green from nuclear policy, Czech/overseas project rumor, preferred-bidder readthrough, SMR/reactor theme, nuclear maintenance/design/O&M label, public utility service label, or one-week nuclear-stock volume spike alone. Require named project/geography/client/contract package, award status, legal/appeal/regulatory risk check, contract scope and revenue-recognition timing, delivery/engineering/maintenance execution, margin and cost-escalation risk control, FX and working-capital burden check, recurring O&M or maintenance service stability where relevant, and post-trigger price survival. Nuclear maintenance positives with large MFE and low MAE may be capped Actionable when service-order and margin bridge are explicit, but Green requires fresh evidence. Nuclear design/engineering positives with material drawdown should remain capped positive or 4B watch when award/legal/timing evidence is stale. Nuclear policy late chases with shallow MFE and large MAE should route to hard-4C candidate when named project and margin bridge are missing.","expected_effect":"Preserve true nuclear project and O&M service positives while reducing nuclear-policy label, preferred-bidder rumor, and late-chase false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":97,"canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","residual_type":"nuclear_project_award_legal_scope_margin_guard","contribution":"Adds one nuclear maintenance service positive, one nuclear design/engineering capped positive, and one nuclear operation policy late-chase hard-4C candidate to calibrate C04 project award, legal/regulatory timing, scope, recurring O&M, working-capital, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C04_NUCLEAR_PROJECT_AWARD_LEGAL_SCOPE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY:

  Do not open Stage3-Green from:
    - nuclear policy headline alone
    - Czech / overseas nuclear project rumor alone
    - preferred-bidder or finalist readthrough alone
    - SMR / reactor theme label alone
    - nuclear maintenance / design / O&M label alone
    - public utility or power-plant service label alone
    - one-week nuclear-stock volume spike alone

  Require at least two of:
    - named project / geography / client / contract package
    - award status and legal / appeals / regulatory clarity
    - contract scope and revenue-recognition timing
    - delivery / engineering / maintenance execution
    - margin and cost-escalation risk containment
    - FX / working-capital burden control
    - recurring O&M / maintenance service stability where relevant
    - low-MAE post-trigger price survival
    - fresh evidence after the nuclear-policy headline

  If MFE < 8% and MAE < -25%:
    route to C04 hard-4C candidate for late policy chases.

  If MFE > 15% but legal/project-scope evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If the case is recurring nuclear maintenance rather than project award:
    require service-order and margin evidence, not just policy beta.

  Distinguish:
    - companies where nuclear policy becomes legally durable project scope, O&M revenue, or margin
    - from nuclear labels where legal delay, appeal risk, contract uncertainty, or cost burden breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C04 nuclear policy / project legal-delay cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C04_NUCLEAR_PROJECT_AWARD_LEGAL_SCOPE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C04 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C04 cases agree, consider implementing a canonical guard that:
   - blocks nuclear-policy Green without named project, award/legal clarity, contract scope, execution, and margin bridge,
   - preserves nuclear maintenance positives only with price survival and fresh O&M service evidence,
   - caps nuclear design/engineering positives at 4B watch when award/legal timing evidence is stale,
   - routes shallow-MFE/large-MAE nuclear operation late chases to hard-4C candidate,
   - applies row-presence/tradeability caveats.

Expected next schedule:
completed_round = R1
completed_loop = 97
next_round = R2
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 97
next_round = R2
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
