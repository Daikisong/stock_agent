# E2R Stock-Web v12 Residual Research — R10 / Loop 95

```yaml
scheduled_round: R10
scheduled_loop: 95
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE

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
engineering_design_case_count: 1
groundwork_specialty_construction_case_count: 1
small_builder_policy_spike_case_count: 1
row_presence_or_tradeability_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 95
next_round: R11
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_95_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 95
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is a hard L9 construction / real-estate / housing round.

The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

The selected fine branch is:

```text
engineering design / groundwork-specialty construction / small-builder policy spike
PF, project-cash, receivables, backlog, margin, and trust bridge
vs generic construction-policy spike
```

This deliberately avoids:
- loop94 R10 small/regional/civil-builder set using `001260`, `010960`, `001840`;
- loop93 regional housing branch using `035890`, `013120`, `017000`;
- loop92 PF-workout branch using `034300`, `009410`, `002460`;
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
```

Selected symbols:

```text
028100 동아지질
002150 도화엔지니어링
025950 동신건설
```

They avoid the C30 top-covered list and avoid recent R10 loop88~94 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
028100: same archetype, new symbol, groundwork / underground infrastructure capped positive with project-cash trust requirement
002150: same archetype, new symbol, engineering-design / infrastructure-service Watch cap without PF/backlog/cashflow operating bridge
025950: same archetype, new symbol, small-builder policy spike hard-4C with row-presence/tradeability caveat
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
028100 동아지질
  profile: atlas/symbol_profiles/028/028100.json
  first_date: 2009-06-12
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,114
  corporate_action_candidate_dates:
    2022-02-21
  2024 entry~D+180 contamination: none

002150 도화엔지니어링
  profile: atlas/symbol_profiles/002/002150.json
  name history:
    도화 until 2011-04-11
    도화엔지니어링 from 2011-04-12
  first_date: 2010-08-12
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,813
  non_tradable_zero_volume rows: 6
  corporate_action_candidate_dates:
    2013-02-01, 2013-02-26
  2024 entry~D+180 contamination: none

025950 동신건설
  profile: atlas/symbol_profiles/025/025950.json
  first_date: 1996-07-31
  raw_first_date: 1996-07-01
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,709
  non_tradable_zero_volume rows: 713
  corporate_action_candidate_dates:
    1997-12-02, 2003-11-26, 2004-01-20
  2024 entry~D+180 contamination: none
  caveat:
    high historical non-tradable zero-volume count exists outside the 2024 validation window.
    This does not directly contaminate the selected 2024 trigger window, but adds trust caution for small-builder spikes.
```

---

## 4. Archetype residual problem

C30 is about PF, project cash flow, receivables, backlog quality, margin risk, and accounting / listing / tradeability trust. It is not a generic "construction policy is hot" label.

The model can over-score:

```text
construction policy relief
engineering / infrastructure service label
groundwork or underground construction label
small builder political beta
housing / regional development headline
one-day construction-stock volume spike
```

The C30 bridge must be stricter:

```text
construction / infrastructure / housing event
  -> company-specific PF or project exposure
  -> receivables and project cash collection
  -> backlog quality and execution timing
  -> cost escalation / subcontractor / labor risk
  -> funding terms and debt maturity
  -> accounting / listing / tradeability trust
  -> margin / FCF conversion
  -> price survival after the first policy or construction-theme spike
```

A C30 construction thesis is like scaffolding around a building. The scaffolding may make the site look safer, but equity value only improves if financing, receivables, backlog, cost, and trust actually hold the structure.

---

## 5. Case 1 — 028100 동아지질

```yaml
case_id: C30_R10L95_028100_2024_07_24
symbol: "028100"
name: "동아지질"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 13320
classification: positive_capped_groundwork_underground_infra_project_execution_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

동아지질 is the constructive control in this R10 set.

The useful C30 read is not:

```text
건설주가 움직였다
```

It is:

```text
groundwork / underground infrastructure relevance
  -> infrastructure and construction project execution
  -> specialty construction backlog optionality
  -> post-trigger price confirmation
  -> manageable but still material drawdown
```

The forward path delivered meaningful MFE after the July trigger. The drawdown stayed below hard-failure territory. Therefore this is a capped positive, not an unrestricted Green. It still needs project-cash, backlog, and margin trust before Actionable/Green.

### Price path

Key Stock-Web rows:

```text
2024-07-24: close 13,320
2024-07-30: high 15,570 / close 14,260
2024-08-05: low 11,550 / close 11,820
2024-08-12: high 14,500 / close 14,080
2024-10-11: high 14,450 / close 12,510
2024-10-23: high 14,100 / close 13,250
```

Approximate path from entry close:

```text
entry_close: 13,320
peak_high: 15,570
MFE: +16.9%
worst_low_after_entry: 11,550
MAE: -13.3%
```

### Interpretation

This is a C30 capped positive with 4B watch:

```text
Stage2-Actionable: possible only if project-cash collection, receivables, backlog quality, and margin bridge are explicit.
Stage3-Green: blocked without funding, project execution, and trust evidence.
Local 4B: monitor after mid-teen MFE because construction project economics can reverse quickly.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  groundwork_infra_relevance: high
  project_execution_bridge: medium_high
  pf_cashflow_bridge: weak_to_medium
  backlog_margin_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: medium
  green_cap: yes
```

---

## 6. Case 2 — 002150 도화엔지니어링

```yaml
case_id: C30_R10L95_002150_2024_07_24
symbol: "002150"
name: "도화엔지니어링"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 7840
classification: watch_cap_engineering_design_infra_service_label_without_pf_project_cashflow_margin_bridge
calibration_usable: true
```

### Evidence interpretation

도화엔지니어링 is the engineering-service Watch cap.

The label is relevant:

```text
engineering design / infrastructure service
  -> public infrastructure and construction-policy relevance
  -> project backlog and design-order optionality
```

But C30 should not promote this label to Actionable/Green unless the bridge is explicit:

```text
project order
cash collection
receivables
cost and margin control
trust / execution evidence
```

The forward price path had shallow MFE and a material drawdown, so it is a Watch/Yellow cap.

### Price path

Key Stock-Web rows:

```text
2024-07-24: close 7,840
2024-07-25: high 8,280 / close 7,800
2024-08-05: low 6,350 / close 6,660
2024-09-06: low 6,660 / close 6,740
2024-10-29: low 6,530 / close 6,560
2024-11-06: high 7,020 / close 6,980
```

Approximate path from entry close:

```text
entry_close: 7,840
peak_high: 8,280
MFE: +5.6%
worst_low_after_entry: 6,350
MAE: -19.0%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from engineering and infrastructure-service relevance.
Stage2-Actionable: blocked unless project cash, backlog, receivables, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MAE did not cross hard threshold.
```

The lesson is that engineering-design relevance is not PF/project-cash repair.

### Stress-test components

```text
raw_component_score_proxy:
  engineering_design_relevance: high
  infrastructure_policy_signal: medium_high
  project_cashflow_bridge: weak
  backlog_receivables_bridge: weak_to_medium
  margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 025950 동신건설

```yaml
case_id: C30_R10L95_025950_2024_03_25
symbol: "025950"
name: "동신건설"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE
trigger_date: 2024-03-25
entry_date: 2024-03-25
entry_price_basis: close
entry_price: 30850
classification: hard_4c_candidate_small_builder_policy_spike_without_pf_project_cashflow_trust_bridge
calibration_usable: true
```

### Evidence interpretation

동신건설 is the hard C30 guardrail.

The trigger has the classic small-builder trap shape:

```text
small construction company
  -> policy / regional-development / political beta
  -> one-day high-volume construction spike
  -> model mistakes price heat for balance-sheet repair
  -> no durable PF, project-cash, receivables, backlog, or margin bridge
```

From the selected close after the March spike, the stock produced almost no incremental MFE and then fell sharply. The high historical non-tradable zero-volume count also adds a trust cap, even though it does not directly contaminate the selected 2024 window.

### Price path

Key Stock-Web rows:

```text
2024-03-14: high 27,450 / close 26,500
2024-03-18: high 27,950 / close 27,350
2024-03-25: high 31,850 / close 30,850
2024-04-11: low 20,000 / close 20,000
2024-08-05: low 17,530 / close 18,480
2024-10-02: high 22,800 / close 20,500
2024-10-31: high 24,100 / close 23,700
```

Approximate path from entry close:

```text
entry_close: 30,850
peak_high_after_entry: 31,850
MFE: +3.2%
worst_low_after_entry: 17,530
MAE: -43.2%
```

### Interpretation

This is a hard C30 false-positive:

```text
Stage2-Watch: possible from small-builder and construction-policy relevance.
Stage2-Actionable: blocked without PF, project-cash, backlog, margin, and trust bridge.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -40%+ MAE.
Row/tradeability caveat: yes, from high historical non-tradable zero-volume count outside the selected 2024 window.
```

The lesson is that small-builder policy heat is not balance-sheet repair.

### Stress-test components

```text
raw_component_score_proxy:
  small_builder_policy_beta: high
  pf_repair_bridge: weak
  project_cashflow_bridge: weak
  backlog_margin_bridge: weak
  accounting_tradeability_trust: weak_to_medium
  price_confirmation_after_entry: failed
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
engineering_design_case_count: 1
groundwork_specialty_construction_case_count: 1
small_builder_policy_spike_case_count: 1
row_presence_or_tradeability_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C30 engineering/groundwork/small-builder grid:

```text
028100 동아지질:
  groundwork / underground infrastructure capped positive;
  meaningful MFE and non-hard MAE, but Green requires project-cash/backlog/margin trust.

002150 도화엔지니어링:
  engineering-design / infrastructure-service relevance;
  shallow MFE and material MAE, Watch/Yellow cap without project cash bridge.

025950 동신건설:
  small-builder policy spike failed;
  shallow MFE and high MAE, hard 4C with row/tradeability caveat.
```

Shared rule:

```text
C30 is not "construction policy or infra label is hot."
C30 is "project cash collection, receivables, backlog quality, funding terms, cost risk, margin, and trust are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L95_028100_2024_07_24","scheduled_round":"R10","scheduled_loop":95,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE","symbol":"028100","name":"동아지질","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":13320,"peak_high":15570,"peak_date":"2024-07-30","worst_low_after_entry":11550,"worst_low_after_entry_date":"2024-08-05","mfe_pct":16.9,"mae_pct":-13.3,"classification":"positive_capped_groundwork_underground_infra_project_execution_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"groundwork_underground_infra_project_execution_backlog_cashflow_margin_bridge","residual_error":"positive_specialty_construction_path_requires_green_cap_without_project_cashflow_margin_trust_evidence","shadow_rule_candidate":"allow_capped_actionable_when_project_execution_price_survival_confirms_but_require_cashflow_trust_for_green"}
{"row_type":"case","case_id":"C30_R10L95_002150_2024_07_24","scheduled_round":"R10","scheduled_loop":95,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE","symbol":"002150","name":"도화엔지니어링","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":7840,"peak_high":8280,"peak_date":"2024-07-25","worst_low_after_entry":6350,"worst_low_after_entry_date":"2024-08-05","mfe_pct":5.6,"mae_pct":-19.0,"classification":"watch_cap_engineering_design_infra_service_label_without_pf_project_cashflow_margin_bridge","calibration_usable":true,"evidence_family":"engineering_design_infra_service_label_without_project_cash_receivables_margin_bridge","residual_error":"engineering_service_relevance_can_overpromote_without_project_cashflow_and_margin_conversion","shadow_rule_candidate":"cap_engineering_design_label_at_watch_yellow_if_mfe_shallow_and_cashflow_bridge_missing"}
{"row_type":"case","case_id":"C30_R10L95_025950_2024_03_25","scheduled_round":"R10","scheduled_loop":95,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE","symbol":"025950","name":"동신건설","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":30850,"peak_high":31850,"peak_date":"2024-03-25","worst_low_after_entry":17530,"worst_low_after_entry_date":"2024-08-05","mfe_pct":3.2,"mae_pct":-43.2,"classification":"hard_4c_candidate_small_builder_policy_spike_without_pf_project_cashflow_trust_bridge","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"small_builder_policy_spike_without_pf_project_cashflow_backlog_margin_tradeability_trust_bridge","residual_error":"small_builder_policy_spike_can_fail_when_pf_cashflow_margin_and_trust_bridge_missing","shadow_rule_candidate":"route_small_builder_policy_spike_to_hard_4c_if_mfe_shallow_mae_large_and_trust_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":95,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"engineering_design_case_count":1,"groundwork_specialty_construction_case_count":1,"small_builder_policy_spike_case_count":1,"row_presence_or_tradeability_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":95,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_PROJECT_CASHFLOW_BACKLOG_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30 engineering, groundwork, specialty construction, and small-builder cases, do not open Stage2-Actionable or Stage3-Green from construction policy, infrastructure-service, groundwork, engineering-design, regional development, small-builder political beta, or one-day construction-stock spike labels alone. Require company-specific PF or project exposure, project cash collection and receivables, backlog quality and execution timing, cost escalation/subcontractor/labor risk check, funding terms and debt maturity, accounting/listing/tradeability trust, margin/FCF conversion, and post-trigger price survival. Specialty construction names with meaningful MFE and controlled MAE may be capped Actionable when project execution and cashflow bridge are explicit, but Green requires trust. Engineering-design labels with shallow MFE should cap at Watch/Yellow without project-cash evidence. Small-builder policy spikes with shallow MFE and high MAE should route to hard-4C, especially when row-presence or tradeability caveats exist.","expected_effect":"Reduce construction-policy, engineering-label, and small-builder late-spike false positives while preserving rare project-execution positives with cashflow, backlog, margin, and trust evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":95,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"project_cashflow_backlog_margin_trust_guard","contribution":"Adds one groundwork/specialty-construction capped positive, one engineering-design Watch cap, and one small-builder policy-spike hard-4C with row/tradeability caveat to calibrate C30 project cashflow, receivables, backlog, margin, and trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_PROJECT_CASHFLOW_BACKLOG_MARGIN_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
AND company_type in [engineering_design, groundwork_specialty_construction, small_builder, infrastructure_contractor]:

  Do not open Stage3-Green from:
    - construction policy headline alone
    - engineering / infrastructure-service label alone
    - groundwork / underground-construction label alone
    - regional development label alone
    - small-builder political beta alone
    - one-day construction-stock volume spike alone

  Require at least two of:
    - company-specific PF / project exposure clarity
    - project cash collection / receivables repair
    - backlog quality and execution timing
    - cost escalation / subcontractor / labor risk containment
    - funding terms / debt maturity clarity
    - accounting / listing / tradeability trust
    - margin / FCF conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the construction-policy headline

  If MFE < 10% and MAE < -30%:
    route to C30 hard-4C candidate.

  If MFE is shallow and cashflow bridge is weak:
    cap at Watch/Yellow.

  If MFE is meaningful but trust bridge is incomplete:
    preserve as capped positive or local 4B, not Green.

  If row-presence or tradeability caveat exists:
    apply additional trust cap, even if a temporary MFE appears.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_95_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 engineering/groundwork/small-builder project-cashflow cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_PROJECT_CASHFLOW_BACKLOG_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks construction-policy Green without project cashflow, receivables, backlog, margin, and trust bridge,
   - preserves specialty-construction positives only with price survival and fresh execution evidence,
   - caps engineering-design labels at Watch/Yellow without project-cash evidence,
   - routes shallow-MFE/high-MAE small-builder policy spikes to hard-4C,
   - applies additional trust cap when row-presence or tradeability caveats exist.

Expected next schedule:
completed_round = R10
completed_loop = 95
next_round = R11
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 95
next_round = R11
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
