# E2R Stock-Web v12 Residual Research — R11 / Loop 97

```yaml
scheduled_round: R11
scheduled_loop: 97
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE

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
waste_treatment_case_count: 2
pollution_control_holding_case_count: 1
environment_policy_case_count: 3
public_treatment_capacity_case_count: 2
policy_to_cashflow_margin_bridge_missing_count: 2
inactive_or_row_presence_caveat_count: 2
governance_or_exit_event_confound_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 97
next_round: R12
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_97_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 97
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R11 can use L10 policy / event / miscellaneous branches. This run uses:

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Selected fine branch:

```text
waste treatment / environmental regulation / public treatment capacity / permit economics
treatment volume, unit price, incineration/landfill capacity, regional permit moat,
cashflow, capex, and margin bridge
vs generic environmental-policy label spike
```

This deliberately avoids:
- R11 loop96 C32 tender / governance branch: `119860`, `115390`, `008930`
- R12 loop96 low-birthrate / baby-product policy branch: `407400`, `159580`, `014100`
- R12 loop95 carbon / CCUS branch: `083420`, `448280`, `119650`
- R11 loop95 tourism branch: `034230`, `950170`, `008770`
- R12 loop94 education branch: `096240`, `072870`, `095720`
- C31 top-covered names: `013990`, `003550`, `015760`, `032350`, `114090`, `000270`

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rows: 97
symbols: 70
date_range: 2020-01-23~2025-01-17
good/bad S2: 35/25
4B/4C: 5/0
URL pending/proxy: 25/25
top covered symbols:
  013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
```

Selected symbols:

```text
029960 코엔텍
067900 와이엔텍
009440 KC그린홀딩스
```

They avoid the C31 top-covered list and the recent L10 policy/governance names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
029960: same archetype, new symbol, waste-treatment public capacity / permit-moat positive with inactive-profile and possible event cap
067900: same archetype, new symbol, waste-treatment / environmental service Watch cap without strong policy-to-cashflow margin acceleration
009440: same archetype, new symbol, environmental / pollution-control holding label hard-4C after policy label failed cashflow and trust bridge
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
029960 코엔텍
  profile: atlas/symbol_profiles/029/029960.json
  first_date: 2004-06-18
  last_date: 2025-05-27 in tradable profile
  raw_last_date: 2025-06-13
  market: KOSDAQ
  tradable_ohlcv rows: 5,168
  non_tradable_zero_volume rows: 16
  corporate_action_candidate_dates:
    2006-05-08
  2024 entry~D+180 contamination: none
  caveat:
    inactive/delisted-like row-presence inference after the selected window.
    For this C31 branch, treat the price path as capped positive / event-confounded, not ordinary environmental-policy Green.

067900 와이엔텍
  profile: atlas/symbol_profiles/067/067900.json
  first_date: 2005-12-23
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 4,971
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2016-11-24
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside selected 2024 validation window.

009440 KC그린홀딩스
  profile: atlas/symbol_profiles/009/009440.json
  name history:
    한국코트렐 -> KC코트렐 -> KC그린홀딩스
  first_date: 1995-05-04
  last_date: 2025-03-19 in tradable profile
  raw_last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,388
  corporate_action_candidate_dates:
    historical windows outside the selected 2024 validation window
  2024 entry~D+180 contamination: none
  caveat:
    row-presence / raw-last-date divergence and severe 2024 drawdown require trust cap.
```

---

## 4. Archetype residual problem

C31 is a policy / subsidy / legislation / event archetype. In this fine branch, the trigger is environmental regulation, waste treatment capacity, disposal-price policy, public treatment demand, and permit scarcity. It is not a generic "environment stock" or "green policy" label.

The model can over-score:

```text
waste treatment / incineration / landfill label
environmental regulation headline
pollution-control / green holding label
public treatment capacity shortage story
permit moat / local monopoly label
ESG or circular-economy theme
one-day environmental-policy volume spike
```

The bridge must be stricter:

```text
environment / waste policy event
  -> named regulation, budget, or public treatment demand
  -> disposal volume and unit price
  -> incineration / landfill / collection capacity
  -> permit and regional monopoly durability
  -> capex, maintenance, and utilization
  -> contract duration and customer concentration
  -> cash collection, working capital, and FCF
  -> margin / OP conversion
  -> event / listing / tradeability trust
  -> price survival after the first environmental-policy spike
```

A C31 environmental-policy thesis is like a waste-treatment gate with a permit lock. The headline says more waste needs a place to go, but equity value appears only when the company has the permitted gate, waste actually flows through it, unit price holds, capex does not leak cash, and the margin line survives.

---

## 5. Case 1 — 029960 코엔텍

```yaml
case_id: C31_R11L97_029960_2024_02_01
symbol: "029960"
name: "코엔텍"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 6600
classification: positive_capped_waste_treatment_permit_capacity_cashflow_bridge_with_inactive_profile_event_caveat
calibration_usable: true
```

### Evidence interpretation

코엔텍 is the constructive environmental/waste-treatment control, but with an event cap.

The useful C31 read is not simply:

```text
환경 / 폐기물주가 좋다
```

It is:

```text
waste-treatment capacity and permit moat
  -> public/private disposal demand
  -> unit-price and utilization stability
  -> cashflow and margin visibility
  -> low drawdown and price survival
```

The forward path produced a strong MFE with controlled downside. However, the profile later becomes inactive/delisted-like by row presence. That means the move should not be treated as ordinary environmental-policy Green without checking event / governance / exit mechanics. The price path is valid as a capped positive, but needs an event/confound cap.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 6,620 / low 6,480 / close 6,600
2024-04-30: close 7,000
2024-08-05: low 6,540 / close 6,640
2024-09-27: high 7,800 / close 7,780
2024-12-03: high 9,030 / close 9,000
2024-12-26: high 9,060 / close 9,060
```

Approximate path from entry close:

```text
entry_close: 6,600
peak_high: 9,060
MFE: +37.3%
worst_low_after_entry: 6,480
MAE: -1.8%
```

### Interpretation

This is a C31 capped positive:

```text
Stage2-Actionable: possible if permitted capacity, treatment volume, unit price, contract durability, and margin bridge are explicit.
Stage3-Green: blocked as ordinary policy Green because inactive/delisted-like profile requires event/tradeability cap.
Local 4B: monitor if event mechanics or policy-to-cashflow evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  waste_treatment_relevance: high
  permit_capacity_moat: high
  volume_unit_price_bridge: medium_high
  cashflow_margin_bridge: medium_high
  public_policy_signal: medium
  price_confirmation: high
  drawdown_penalty: low
  inactive_profile_event_caveat: high
  ordinary_green_block: yes
```

---

## 6. Case 2 — 067900 와이엔텍

```yaml
case_id: C31_R11L97_067900_2024_02_01
symbol: "067900"
name: "와이엔텍"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 7310
classification: watch_cap_waste_treatment_environmental_service_label_without_strong_incremental_policy_cashflow_margin_bridge
calibration_usable: true
```

### Evidence interpretation

와이엔텍 is the waste-treatment Watch cap.

The label is relevant:

```text
waste treatment / environmental service
  -> treatment demand and permit-capacity relevance
  -> public/environmental policy readthrough
  -> local regional treatment economics
```

But the path did not justify Actionable/Green from the selected February trigger. MFE was modest, and the stock later drew down materially in August/September. This is not an outright hard failure, but it proves that environmental service relevance is not enough without incremental volume, unit price, contract, and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 7,320 / close 7,310
2024-04-11: high 7,490 / close 6,860
2024-05-10: high 7,820 / close 7,700
2024-08-05: low 6,150 / close 6,300
2024-09-06: low 6,220 / close 6,290
2024-10-25: low 6,250 / close 6,310
```

Approximate path from entry close:

```text
entry_close: 7,310
peak_high: 7,830
MFE: +7.1%
worst_low_after_entry: 6,150
MAE: -15.9%
```

### Interpretation

This is a Watch/Yellow cap:

```text
Stage2-Watch: valid from waste-treatment and environmental-service relevance.
Stage2-Actionable: blocked unless unit-price, volume, permit capacity, contract, capex, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no, because MFE/MAE do not cross hard thresholds.
```

### Stress-test components

```text
raw_component_score_proxy:
  waste_treatment_relevance: high
  permit_capacity_bridge: medium
  unit_price_volume_bridge: weak_to_medium
  contract_duration_bridge: weak_to_medium
  margin_fcf_bridge: weak_to_medium
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 009440 KC그린홀딩스

```yaml
case_id: C31_R11L97_009440_2024_02_01
symbol: "009440"
name: "KC그린홀딩스"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3010
classification: hard_4c_candidate_environmental_pollution_control_holding_label_without_policy_cashflow_margin_trust_survival
calibration_usable: true
```

### Evidence interpretation

KC그린홀딩스 is the environmental-policy hard guardrail.

The label can fool the model:

```text
environmental / pollution-control holding company
  -> green policy / circular-economy / regulation readthrough
  -> policy-stock event beta
  -> environmental infrastructure optionality
```

But from the selected February entry, the path produced only a modest MFE and then a severe drawdown. The bridge from environmental label to contract, treatment volume, unit price, cash collection, balance-sheet trust, and margin was not proven. Later event-like spikes in September/October should not retroactively validate the failed February setup.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 3,075 / close 3,010
2024-02-27: high 3,315 / close 3,280
2024-04-17: low 2,260 / close 2,280
2024-05-07: low 1,838 / close 1,840
2024-08-19: low 711 / close 743
2024-09-09: high 1,411 / close 1,275
2024-10-02: high 1,182 / close 1,000
2024-11-08: high 1,094 / close 894
```

Approximate path from entry close:

```text
entry_close: 3,010
peak_high_first_phase: 3,315
MFE: +10.1%
worst_low_after_entry: 705
MAE: -76.6%
```

### Interpretation

This is a hard C31 false-positive:

```text
Stage2-Watch: possible from environmental/pollution-control relevance.
Stage2-Actionable: blocked unless named regulation, contract, volume, unit price, cashflow, balance-sheet, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by modest MFE and extreme MAE.
Row/tradeability caveat: yes, tradable last-date/raw-last-date divergence and severe price deterioration require trust cap.
Event-window separation: later September/October spikes are new windows, not rescue of the February trigger.
```

The lesson is that environmental holding-company salience is not policy-to-cashflow survival.

### Stress-test components

```text
raw_component_score_proxy:
  environmental_policy_label: high
  pollution_control_infra_signal: medium
  contract_volume_unit_price_bridge: weak
  cashflow_margin_bridge: weak
  balance_sheet_trust: weak
  event_window_separation_required: medium_high
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
waste_treatment_case_count: 2
pollution_control_holding_case_count: 1
environment_policy_case_count: 3
public_treatment_capacity_case_count: 2
policy_to_cashflow_margin_bridge_missing_count: 2
inactive_or_row_presence_caveat_count: 2
governance_or_exit_event_confound_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C31 environment / waste policy grid:

```text
029960 코엔텍:
  waste-treatment capacity / permit-moat capped positive;
  strong MFE and low MAE, but inactive-profile/event caveat blocks ordinary Green.

067900 와이엔텍:
  waste-treatment environmental-service relevance;
  shallow MFE and material MAE, Watch/Yellow cap.

009440 KC그린홀딩스:
  environmental / pollution-control holding label failed;
  modest MFE and extreme MAE, hard 4C with trust cap.
```

Shared rule:

```text
C31 environment policy is not "environmental label is hot."
C31 environment policy is "regulation creates demand, permitted capacity captures volume, unit price holds, capex and maintenance stay contained, cash is collected, and OP/FCF margin survives."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R11L97_029960_2024_02_01","scheduled_round":"R11","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE","symbol":"029960","name":"코엔텍","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":6600,"peak_high":9060,"peak_date":"2024-12-26","worst_low_after_entry":6480,"worst_low_after_entry_date":"2024-02-01","mfe_pct":37.3,"mae_pct":-1.8,"classification":"positive_capped_waste_treatment_permit_capacity_cashflow_bridge_with_inactive_profile_event_caveat","calibration_usable":true,"inactive_or_row_presence_caveat":true,"governance_or_exit_event_confound_caveat":true,"evidence_family":"waste_treatment_permit_capacity_public_disposal_volume_unit_price_cashflow_margin_bridge","residual_error":"waste_policy_positive_requires_capped_green_when_inactive_profile_or_exit_event_confound_exists","shadow_rule_candidate":"allow_capped_actionable_when_permit_capacity_and_cashflow_bridge_confirm_but_block_ordinary_green_under_inactive_profile_caveat"}
{"row_type":"case","case_id":"C31_R11L97_067900_2024_02_01","scheduled_round":"R11","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE","symbol":"067900","name":"와이엔텍","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":7310,"peak_high":7830,"peak_date":"2024-05-13","worst_low_after_entry":6150,"worst_low_after_entry_date":"2024-08-05","mfe_pct":7.1,"mae_pct":-15.9,"classification":"watch_cap_waste_treatment_environmental_service_label_without_strong_incremental_policy_cashflow_margin_bridge","calibration_usable":true,"evidence_family":"waste_treatment_environmental_service_label_without_incremental_unit_price_volume_contract_margin_bridge","residual_error":"environmental_service_relevance_can_overpromote_without_incremental_policy_to_cashflow_margin_evidence","shadow_rule_candidate":"cap_waste_treatment_label_at_watch_yellow_if_mfe_shallow_and_unit_price_volume_bridge_missing"}
{"row_type":"case","case_id":"C31_R11L97_009440_2024_02_01","scheduled_round":"R11","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE","symbol":"009440","name":"KC그린홀딩스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3010,"peak_high_first_phase":3315,"peak_date":"2024-02-27","worst_low_after_entry":705,"worst_low_after_entry_date":"2024-08-20","mfe_pct":10.1,"mae_pct":-76.6,"classification":"hard_4c_candidate_environmental_pollution_control_holding_label_without_policy_cashflow_margin_trust_survival","calibration_usable":true,"inactive_or_row_presence_caveat":true,"event_window_separation_required":true,"evidence_family":"environmental_pollution_control_holding_label_without_contract_volume_unit_price_cashflow_margin_trust_bridge","residual_error":"environmental_policy_label_can_fail_when_contract_cashflow_margin_and_trust_bridge_missing","shadow_rule_candidate":"route_environmental_holding_policy_label_to_hard_4c_if_mfe_modest_mae_extreme_and_cashflow_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"waste_treatment_case_count":2,"pollution_control_holding_case_count":1,"environment_policy_case_count":3,"public_treatment_capacity_case_count":2,"policy_to_cashflow_margin_bridge_missing_count":2,"inactive_or_row_presence_caveat_count":2,"governance_or_exit_event_confound_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":97,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_ENVIRONMENT_WASTE_POLICY_CAPACITY_CASHFLOW_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 environmental/waste-treatment policy cases, do not open Stage2-Actionable or Stage3-Green from waste treatment, incineration, landfill, environmental regulation, pollution-control, green holding, permit moat, public treatment capacity shortage, ESG/circular-economy, or one-day environmental-policy volume-spike labels alone. Require named regulation/budget/public demand, disposal volume and unit price, incineration/landfill/collection capacity, permit and regional monopoly durability, capex/maintenance/utilization control, contract duration and customer concentration, cash collection/working capital/FCF, margin/OP conversion, event/listing/tradeability trust, and post-trigger price survival. Waste-treatment positives with large MFE and low MAE may be capped Actionable when permit capacity and cashflow bridge are explicit, but ordinary Green must be blocked if inactive/delisted-like profile or governance/exit event confound exists. Waste-treatment labels with shallow MFE should cap at Watch/Yellow without incremental unit-price and volume evidence. Environmental/pollution-control holding labels with modest MFE and extreme MAE should route to hard-4C when cashflow, balance-sheet, and trust bridge are missing.","expected_effect":"Preserve true environmental/waste-treatment policy-to-cashflow positives while reducing generic environmental-policy, pollution-control holding, permit-moat, and ESG-label false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":97,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"environment_waste_policy_capacity_cashflow_margin_trust_guard","contribution":"Adds one waste-treatment capped positive, one waste-treatment Watch cap, and one environmental holding hard-4C counterexample to calibrate C31 environmental policy demand, permit capacity, disposal volume, unit price, cash collection, margin, and tradeability/event trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_ENVIRONMENT_WASTE_POLICY_CAPACITY_CASHFLOW_MARGIN_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [environmental_regulation, waste_treatment, public_treatment_capacity, permit_moat, circular_economy]:

  Do not open Stage3-Green from:
    - waste treatment / incineration / landfill label alone
    - environmental regulation headline alone
    - pollution-control / green holding label alone
    - public treatment capacity shortage story alone
    - permit moat / local monopoly label alone
    - ESG or circular-economy theme alone
    - one-day environmental-policy stock volume spike alone

  Require at least two of:
    - named regulation, budget, or public treatment demand
    - disposal volume and unit price
    - incineration / landfill / collection capacity
    - permit and regional monopoly durability
    - capex, maintenance, and utilization control
    - contract duration / customer concentration check
    - cash collection / working capital / FCF
    - margin / OP conversion
    - event / listing / tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the environmental-policy headline

  If MFE < 8% and MAE < -30%:
    route to C31 hard-4C candidate.

  If MFE > 15% but inactive/delisted-like or exit-event caveat exists:
    score as capped positive, not ordinary Green.

  If MFE is shallow and unit-price/volume bridge is stale:
    cap at Watch/Yellow.

  If later event-like spikes appear after severe first-phase failure:
    create a new event window; do not retroactively validate the first trigger.

  Distinguish:
    - companies where environmental policy becomes permitted volume, unit price, cash collection, and margin
    - from environmental labels where balance-sheet, event, or tradeability trust breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 environmental/waste-treatment policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_ENVIRONMENT_WASTE_POLICY_CAPACITY_CASHFLOW_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 environment-policy cases agree, consider implementing a canonical guard that:
   - blocks environmental/waste-policy Green without regulation/budget, volume, unit price, capacity, permit, capex, cash collection, and margin bridge,
   - preserves waste-treatment positives only as capped Actionable when price survival and cashflow evidence are fresh,
   - blocks ordinary Green when inactive/delisted-like or exit-event caveat exists,
   - caps shallow-MFE waste-treatment labels at Watch/Yellow without unit-price and volume evidence,
   - routes modest-MFE/extreme-MAE environmental holding labels to hard-4C,
   - separates later event windows from failed first triggers.

Expected next schedule:
completed_round = R11
completed_loop = 97
next_round = R12
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 97
next_round = R12
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
