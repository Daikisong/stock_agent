# E2R Stock-Web v12 Residual Research — R1 / Loop 93

```yaml
scheduled_round: R1
scheduled_loop: 93
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: INDUSTRIAL_PLANT_UNDERGROUND_EPC_ORDER_MARGIN_CASHFLOW_BRIDGE_VS_CONTRACT_HEADLINE_BETA

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
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 93
next_round: R2
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 93
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 hard gate requires:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage already covered:

```text
loop88: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
loop89: C02_POWER_GRID_DATACENTER_CAPEX
loop90: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
loop91: C01_ORDER_BACKLOG_MARGIN_BRIDGE
loop92: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

This run returns to C05, but deliberately avoids the previously top-covered C05 set and uses a different fine branch:

```text
industrial plant / underground civil EPC / order margin and cash-flow bridge
vs generic contract-headline beta
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rows: 10
symbols: 9
date_range: 2023-03-31~2024-07-12
good/bad S2: 3/4
4B/4C: 0/0
URL pending/proxy: 0/0
top covered symbols:
  053690(2), 002150(1), 011560(1), 023350(1), 023960(1), 054930(1)
```

Selected symbols:

```text
016250 SGC E&C
028050 삼성E&A
028100 동아지질
```

They avoid the top-covered C05 symbols and avoid the recent R1 loop91/92 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
016250: same archetype, new symbol, industrial EPC local-positive / margin-cashflow bridge branch
028050: same archetype, new symbol, large plant EPC headline / order-margin bridge failure branch
028100: same archetype, new symbol, underground civil EPC/infrastructure theme spike without margin bridge
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
016250 SGC E&C
  profile: atlas/symbol_profiles/016/016250.json
  name history:
    이테크이앤씨 until 2005-05-30
    이테크건설 until 2020-12-07
    SGC이테크건설 until 2024-04-18
    SGC E&C from 2024-04-19
  first_date: 1999-12-28
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,413
  corporate_action_candidate_dates:
    2020-12-08, 2021-04-09, 2022-04-08, 2023-04-07, 2025-06-25
  2024 entry~D+180 contamination: none

028050 삼성E&A
  profile: atlas/symbol_profiles/028/028050.json
  name history:
    삼성엔지니어링 until 2024-04-05
    삼성E&A from 2024-04-08
  first_date: 1997-01-03
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,265
  corporate_action_candidate_dates:
    1997-08-22, 1999-01-13, 1999-05-26, 1999-09-29, 2016-02-26
  2024 entry~D+180 contamination: none

028100 동아지질
  profile: atlas/symbol_profiles/028/028100.json
  first_date: 2009-06-12
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,114
  corporate_action_candidate_dates:
    2022-02-21
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C05 is not a generic "big contract" or "EPC stock" label.

The model can over-score:

```text
mega contract
plant EPC order
infrastructure / underground works headline
name-change or restructuring story
Middle East / energy transition / civil-infra order beta
one-week volume burst after a contract rumor
```

The bridge must be narrower:

```text
contract or project headline
  -> scope and margin quality
  -> execution risk
  -> cost escalation and FX risk
  -> payment milestone / working capital
  -> backlog recognition
  -> OP / FCF conversion
  -> price survival after the first contract spike
```

An EPC contract headline is a blueprint, not a finished building. C05 asks whether the blueprint becomes profitable work after labor, materials, FX, warranty, and working-capital drag.

---

## 5. Case 1 — 016250 SGC E&C

```yaml
case_id: C05_R1L93_016250_2024_07_24
symbol: "016250"
name: "SGC E&C"
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: INDUSTRIAL_PLANT_UNDERGROUND_EPC_ORDER_MARGIN_CASHFLOW_BRIDGE_VS_CONTRACT_HEADLINE_BETA
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 14900
classification: positive_capped_industrial_epc_margin_cashflow_bridge
calibration_usable: true
```

### Evidence interpretation

SGC E&C is the constructive control in this set.

The useful C05 read is not simply:

```text
EPC contractor is cheap
```

It is:

```text
industrial EPC / plant-construction exposure
  -> order execution and cash collection visibility
  -> controlled downside before the move
  -> later price confirmation
```

The stock produced a meaningful MFE after the July trigger and did not materially break below the entry close in the checked window. This is the right shape for a capped C05 positive.

### Price path

Key Stock-Web rows:

```text
2024-07-24: close 14,900
2024-08-05: high 18,740 / close 17,400
2024-08-28: high 17,950 / close 16,450
2024-09-06: low 15,240 / close 15,260
2024-11-04: low 14,600 / close 15,170
```

Approximate path from entry close:

```text
entry_close: 14,900
peak_high: 18,740
MFE: +25.8%
worst_low_after_entry: 14,600
MAE: -2.0%
```

### Interpretation

This is a C05 capped positive:

```text
Stage2-Actionable: allowed if order execution / cash-flow bridge is explicit.
Stage3-Green: blocked without confirmed margin / FCF conversion.
Local 4B: monitor after +25% MFE but not mandatory from initial path alone.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  epc_order_relevance: medium_high
  margin_quality_bridge: medium
  working_capital_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 028050 삼성E&A

```yaml
case_id: C05_R1L93_028050_2024_02_28
symbol: "028050"
name_at_trigger: "삼성엔지니어링"
current_or_latest_name: "삼성E&A"
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: INDUSTRIAL_PLANT_UNDERGROUND_EPC_ORDER_MARGIN_CASHFLOW_BRIDGE_VS_CONTRACT_HEADLINE_BETA
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 26000
classification: hard_4c_candidate_large_plant_epc_headline_without_margin_revision_bridge
calibration_usable: true
```

### Evidence interpretation

삼성E&A is the large plant-EPC guardrail.

The company is a real EPC platform, but C05 specifically asks whether order headlines and project visibility become margin and cash-flow conversion. The forward path says a broad plant-EPC label was not enough at this trigger.

The model risk:

```text
large plant EPC label
  -> project/order headline
  -> energy-transition or overseas EPC beta
  -> no fresh margin revision bridge
  -> later high MAE
```

### Price path

Key Stock-Web rows:

```text
2024-02-28: high 26,350 / close 26,000
2024-03-15: high 28,150 / close 25,700
2024-07-30: high 29,300 / close 28,300
2024-08-05: low 23,450 / close 24,600
2024-09-27: low 22,350 / close 22,350
2024-10-31: low 17,740 / close 17,860
```

Approximate path from entry close:

```text
entry_close: 26,000
peak_high: 29,300
MFE: +12.7%
worst_low: 17,740
MAE: -31.8%
```

### Interpretation

This is a hard C05 guardrail case:

```text
Stage2-Watch: valid from large EPC relevance.
Stage2-Actionable: blocked unless margin / revision / cash-flow bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that a large, high-quality EPC name can still be a false positive if the trigger lacks a fresh margin bridge.

### Stress-test components

```text
raw_component_score_proxy:
  large_epc_label_quality: high
  contract_headline_relevance: medium_high
  margin_revision_bridge: weak
  working_capital_risk_check: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 028100 동아지질

```yaml
case_id: C05_R1L93_028100_2024_01_30
symbol: "028100"
name: "동아지질"
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: INDUSTRIAL_PLANT_UNDERGROUND_EPC_ORDER_MARGIN_CASHFLOW_BRIDGE_VS_CONTRACT_HEADLINE_BETA
trigger_date: 2024-01-30
entry_date: 2024-01-30
entry_price_basis: close
entry_price: 14980
classification: hard_4c_candidate_underground_civil_epc_theme_spike_without_margin_cashflow_bridge
calibration_usable: true
```

### Evidence interpretation

동아지질 is the underground civil-infra false-positive.

It can look like an infrastructure/EPC winner when underground works, TBM, GTX, or civil-infra themes become active. But C05 requires more than theme relevance. It needs the contract to translate into executable, profitable backlog.

The price path shows a one-day spike, then a long fade.

### Price path

Key Stock-Web rows:

```text
2024-01-30: high 15,620 / close 14,980
2024-02-01: high 15,090 / close 14,550
2024-03-12: low 12,850 / close 12,890
2024-07-30: high 15,570 / close 14,260
2024-08-05: low 11,550 / close 11,820
2024-09-09: low 11,960 / close 12,290
```

Approximate path from entry close:

```text
entry_close: 14,980
peak_high: 15,620
MFE: +4.3%
worst_low: 11,550
MAE: -22.9%
```

### Interpretation

This is a C05 false-positive / hard-4C candidate:

```text
Stage2-Watch: allowed from underground/civil infra theme relevance.
Stage2-Actionable: blocked unless contract scope, margin, and cash-flow bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes for shallow MFE and material MAE.
```

The lesson is that civil-infra theme heat does not equal profitable EPC backlog.

### Stress-test components

```text
raw_component_score_proxy:
  underground_infra_label: high
  contract_scope_bridge: weak
  margin_cashflow_bridge: weak
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
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3
```

The three-case C05 grid:

```text
016250 SGC E&C:
  industrial EPC local-positive with controlled MAE;
  Actionable only when margin/cash-flow bridge is explicit.

028050 삼성E&A:
  large plant-EPC label failed without fresh margin revision;
  shallow MFE and high MAE, hard 4C.

028100 동아지질:
  underground civil-infra theme spike failed;
  shallow MFE and material MAE, hard 4C.
```

Shared rule:

```text
C05 is not "big EPC/order headline."
C05 is "project scope, cost control, working capital, and backlog recognition convert the order into margin and cash flow."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C05_R1L93_016250_2024_07_24","scheduled_round":"R1","scheduled_loop":93,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"INDUSTRIAL_PLANT_UNDERGROUND_EPC_ORDER_MARGIN_CASHFLOW_BRIDGE_VS_CONTRACT_HEADLINE_BETA","symbol":"016250","name":"SGC E&C","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":14900,"peak_high":18740,"peak_date":"2024-08-05","worst_low_after_entry":14600,"worst_low_after_entry_date":"2024-11-04","mfe_pct":25.8,"mae_pct":-2.0,"classification":"positive_capped_industrial_epc_margin_cashflow_bridge","calibration_usable":true,"evidence_family":"industrial_epc_order_execution_margin_working_capital_bridge","residual_error":"positive_path_still_needs_explicit_margin_and_fcf_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_order_execution_margin_cashflow_bridge_confirms_but_cap_green_without_op_fcf_conversion"}
{"row_type":"case","case_id":"C05_R1L93_028050_2024_02_28","scheduled_round":"R1","scheduled_loop":93,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"INDUSTRIAL_PLANT_UNDERGROUND_EPC_ORDER_MARGIN_CASHFLOW_BRIDGE_VS_CONTRACT_HEADLINE_BETA","symbol":"028050","name_at_trigger":"삼성엔지니어링","current_or_latest_name":"삼성E&A","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":26000,"peak_high":29300,"peak_date":"2024-07-30","worst_low":17740,"worst_low_date":"2024-10-31","mfe_pct":12.7,"mae_pct":-31.8,"classification":"hard_4c_candidate_large_plant_epc_headline_without_margin_revision_bridge","calibration_usable":true,"evidence_family":"large_plant_epc_label_without_fresh_margin_revision_working_capital_bridge","residual_error":"large_epc_quality_can_overpromote_without_project_margin_cashflow_conversion","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_margin_revision_bridge_missing"}
{"row_type":"case","case_id":"C05_R1L93_028100_2024_01_30","scheduled_round":"R1","scheduled_loop":93,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"INDUSTRIAL_PLANT_UNDERGROUND_EPC_ORDER_MARGIN_CASHFLOW_BRIDGE_VS_CONTRACT_HEADLINE_BETA","symbol":"028100","name":"동아지질","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":14980,"peak_high":15620,"peak_date":"2024-01-30","worst_low":11550,"worst_low_date":"2024-08-05","mfe_pct":4.3,"mae_pct":-22.9,"classification":"hard_4c_candidate_underground_civil_epc_theme_spike_without_margin_cashflow_bridge","calibration_usable":true,"evidence_family":"underground_civil_infra_epc_theme_without_contract_margin_cashflow_bridge","residual_error":"civil_infra_theme_can_spike_without_profitable_backlog_conversion","shadow_rule_candidate":"route_underground_infra_epc_theme_to_4c_if_mfe_shallow_and_margin_cashflow_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":93,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"INDUSTRIAL_PLANT_UNDERGROUND_EPC_ORDER_MARGIN_CASHFLOW_BRIDGE_VS_CONTRACT_HEADLINE_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":93,"canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","rule_id":"C05_PROJECT_MARGIN_CASHFLOW_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C05, do not open Stage2-Actionable or Stage3-Green from EPC, mega contract, plant order, underground civil-infra, overseas project, or one-week contract headline alone. Require project scope, margin quality, cost escalation control, FX/commodity risk check, payment milestone and working-capital bridge, backlog recognition, OP/FCF conversion, and post-trigger price survival. Industrial EPC names with controlled MAE may be capped positives only when margin and cash-flow bridge are explicit. Large plant EPC or civil-infra theme names with shallow MFE and high MAE should route to hard-4C unless fresh margin revision evidence appears.","expected_effect":"Reduce EPC contract-headline false positives while preserving industrial EPC positives with visible margin, working-capital, and cash-flow conversion.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":93,"canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","residual_type":"epc_project_margin_cashflow_guard","contribution":"Adds one industrial EPC capped positive and two plant/civil-infra EPC hard-4C counterexamples to calibrate C05 project-margin and cash-flow requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C05_PROJECT_MARGIN_CASHFLOW_BRIDGE_REQUIRED

IF canonical_archetype_id == C05_EPC_MEGA_CONTRACT_MARGIN_GAP:

  Do not open Stage3-Green from:
    - EPC / plant order headline alone
    - mega contract headline alone
    - underground civil-infra / TBM / GTX label alone
    - overseas project label alone
    - one-week contract-rumor volume spike alone

  Require at least two of:
    - project scope clarity
    - margin quality or margin revision
    - cost escalation / commodity / labor risk control
    - FX and payment milestone visibility
    - working-capital containment
    - backlog recognition
    - OP / FCF conversion
    - low-MAE post-trigger price survival

  If MFE < 15% and MAE < -20%:
    route to C05 hard-4C candidate unless fresh margin evidence appears.

  If MFE > 20% and MAE remains controlled:
    allow capped Actionable only if margin/cash-flow bridge is explicit.

  Distinguish:
    - industrial EPC cases with visible execution and cash-flow conversion
    - from large plant-EPC or underground civil-infra labels where valuation follows headline but margin bridge is missing.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_93_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C05 EPC/project margin gap cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C05_PROJECT_MARGIN_CASHFLOW_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C05 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C05 cases agree, consider implementing a canonical guard that:
   - blocks EPC contract-headline Green without project margin and cash-flow bridge,
   - preserves industrial EPC capped positives only with low MAE and execution evidence,
   - routes shallow-MFE/high-MAE large plant-EPC or civil-infra theme cases to hard-4C,
   - separates true project margin conversion from generic order beta.

Expected next schedule:
completed_round = R1
completed_loop = 93
next_round = R2
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 93
next_round = R2
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
