# E2R Stock-Web v12 Residual Research — R10 / Loop 91

```yaml
scheduled_round: R10
scheduled_loop: 91
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 91
next_round: R11
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 91
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is a hard L9 construction / real-estate round. The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
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

Recent R10 files already used:

```text
loop88: 047040, 012630, 021320
loop89: 000720, 003070, 002780
loop90: 014790, 010780, 005960
```

Selected symbols for this run:

```text
013360 일성건설
001470 삼부토건
002410 범양건영
```

They avoid the C30 top-covered symbols and the recent R10 loop88~90 symbols.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
013360: same archetype, new symbol, small-builder policy relief / local risk-premium compression branch
001470: same archetype, new symbol, construction-policy/political beta false-positive and balance-sheet trust branch
002410: same archetype, new symbol, small-builder PF policy-support false-positive branch
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
013360 일성건설
  profile: atlas/symbol_profiles/013/013360.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,709
  corporate_action_candidate_dates:
    1996-01-03, 1998-12-21, 2000-04-21, 2000-08-18, 2003-01-07, 2017-05-18
  2024 entry~D+180 contamination: none

001470 삼부토건
  profile: atlas/symbol_profiles/001/001470.json
  first_date: 1995-05-02
  last_date: 2025-03-31 in tradable shard
  raw_last_date: 2026-02-20
  tradable_ohlcv rows: 7,422
  corporate_action_candidate_dates:
    1996-01-03, 2016-05-13, 2016-12-23, 2017-10-31, 2018-09-18, 2019-05-02
  2024 entry~D+180 contamination: none
  caveat:
    inactive_or_delisted_like / row-presence caveat appears after the research window.
    This strengthens accounting/listing-trust caution but does not contaminate the 2024 entry window.

002410 범양건영
  profile: atlas/symbol_profiles/002/002410.json
  first_date: 1995-05-02
  last_date: 2025-03-20 in tradable shard
  raw_last_date: 2026-02-20
  tradable_ohlcv rows: 6,992
  corporate_action_candidate_dates:
    1996-01-03, 2009-12-21, 2014-07-07, 2015-07-09, 2015-12-30, 2017-12-06
  2024 entry~D+180 contamination: none
  caveat:
    inactive_or_delisted_like / row-presence caveat appears after the research window.
    Treat as additional balance-sheet/listing-trust warning for later validation.
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-03-27
Korea builder liquidity / real-estate PF support policy frame.
```

Follow-up policy frame:

```text
2024-05-13
Real-estate PF profitability assessment and restructuring acceleration frame.
```

C30 does not ask whether the government created a sector firewall. It asks whether the firewall actually repaired a listed builder's balance sheet.

The failure mode is:

```text
government support headline
  -> small builders and construction themes bounce
  -> model reads bounce as Stage2 Actionable
  -> company-specific PF, cash collection, and order-margin bridge is missing
  -> high MAE or listing/accounting trust issue follows
```

A PF policy is like emergency scaffolding around a building. It may stop collapse at the street level. It does not repair every cracked beam inside each company.

---

## 5. Case 1 — 013360 일성건설

```yaml
case_id: C30_R10L91_013360_2024_03_27
symbol: "013360"
name: "일성건설"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price_basis: close
entry_price: 1267
classification: positive_local_risk_premium_relief_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

일성건설 is the positive-control case in this small-builder grid.

The price path shows that some small-builder risk premium can compress after the PF-support frame. It did not produce the same high-MAE failure as 삼부토건 or 범양건영.

However, the case should not be read as automatic Stage3-Green. The path is a tradable relief / local rerating case. Green still needs:

```text
company-specific PF exposure reduction
project-level refinancing
cash collection
order backlog margin
OP/FCF conversion
```

### Price path

Key Stock-Web rows:

```text
2024-03-27: close 1,267
2024-04-09: high 1,484 / close 1,380
2024-04-11: high 1,583 / close 1,380
2024-04-22: high 1,541 / close 1,449
2024-07-01: high 1,447 / close 1,308
2024-07-23: high 1,860 / close 1,663
2024-08-05: low 1,288 / close 1,340
2024-09-09: low 1,270 / close 1,343
```

Approximate path from entry close:

```text
entry_close: 1,267
peak_high: 1,860
MFE: +46.8%
worst_low_after_entry_checked: 1,189 on 2024-04-17
MAE: -6.2%
```

### Interpretation

This is a C30 positive, but with a cap:

```text
Stage2-Actionable: allowed only if company-specific PF/liquidity bridge is present.
Stage3-Green: blocked unless repair evidence is explicit.
Local 4B: attach after +40% MFE because small-builder relief rallies are volatile.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  sector_policy_support: medium_high
  small_builder_relief_beta: high
  company_specific_repair_bridge: medium_or_unclear
  price_confirmation: high
  drawdown_penalty: low_to_medium
  local_4b_overlay: required
```

---

## 6. Case 2 — 001470 삼부토건

```yaml
case_id: C30_R10L91_001470_2024_03_27
symbol: "001470"
name: "삼부토건"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price_basis: close
entry_price: 1993
classification: hard_4c_candidate_construction_policy_beta_without_balance_sheet_trust_bridge
calibration_usable: true
```

### Evidence interpretation

삼부토건 is the hard guardrail case.

It can attract construction-policy, reconstruction, small-builder, and political-beta attention. But C30 cannot promote that mix into Actionable without balance-sheet trust and project-level evidence.

The forward path was severe. The later tradable-row caveat after 2025 adds an additional trust warning, but the 2024 price path already failed by itself.

### Price path

Key Stock-Web rows:

```text
2024-03-27: close 1,993
2024-03-28: high 2,085 / close 2,000
2024-03-29: high 2,165 / close 1,731
2024-04-23: low 1,245 / close 1,352
2024-05-29: high 1,924 / close 1,781
2024-07-22: high 1,959 / close 1,879
2024-08-05: low 1,150 / close 1,259
2024-08-20: low 562 / close 681
2024-09-06: low 458 / close 458
```

Approximate path from entry close:

```text
entry_close: 1,993
peak_high: 2,165
MFE: +8.6%
worst_low: 458
MAE: -77.0%
```

### Interpretation

This is a hard 4C candidate:

```text
Stage2-Watch: possible only as a speculative construction-theme name.
Stage2-Actionable: blocked.
Stage3-Green: blocked.
Hard 4C: yes.
```

The mistake is clear:

```text
construction-policy beta != PF repair
political construction beta != cash-flow conversion
```

### Stress-test components

```text
raw_component_score_proxy:
  sector_policy_support: medium
  political/construction_beta: high
  balance_sheet_trust: weak
  company_specific_pf_repair_bridge: weak
  price_confirmation: failed
  drawdown_penalty: extreme
  hard_4c_guard: required
```

---

## 7. Case 3 — 002410 범양건영

```yaml
case_id: C30_R10L91_002410_2024_03_27
symbol: "002410"
name: "범양건영"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price_basis: close
entry_price: 1611
classification: hard_4c_candidate_small_builder_policy_support_without_pf_repair_bridge
calibration_usable: true
```

### Evidence interpretation

범양건영 is the quieter hard-4C case.

It did not collapse like 삼부토건, but the path still failed the C30 Actionable test. A small builder can get a brief relief bid after PF support, but without:

```text
project-level refinancing
cash collection
receivables repair
debt maturity extension
profitable backlog
margin conversion
```

the policy headline is not enough.

### Price path

Key Stock-Web rows:

```text
2024-03-27: close 1,611
2024-04-09: high 1,570 / close 1,511
2024-04-22: high 1,775 / close 1,615
2024-07-10: high 1,568 / close 1,313
2024-07-12: high 1,534 / close 1,342
2024-08-05: low 1,198 / close 1,198
2024-09-11: low 1,135 / close 1,141
2024-09-25: low 1,114 / close 1,166
```

Approximate path from entry close:

```text
entry_close: 1,611
peak_high: 1,775
MFE: +10.2%
worst_low: 1,114
MAE: -30.9%
```

### Interpretation

This is a hard 4C candidate or at least strong false-positive guard:

```text
Stage2-Watch: possible.
Stage2-Actionable: blocked without company-specific repair bridge.
Stage3-Green: blocked.
Hard 4C: yes by shallow-MFE / high-MAE threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  sector_policy_support: medium
  small_builder_relief_beta: medium
  company_specific_pf_repair_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3
```

The three-case C30 grid:

```text
013360 일성건설:
  small-builder relief rally can work as a local positive,
  but Green requires company-specific PF/cash-flow repair.

001470 삼부토건:
  construction-policy / political beta without balance-sheet trust becomes hard 4C.

002410 범양건영:
  small-builder policy support without PF repair bridge produces shallow MFE and high MAE.
```

Shared rule:

```text
C30 is not "builders received policy support."
C30 is "this builder's PF exposure, liquidity, and project economics were repaired enough to support equity value."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L91_013360_2024_03_27","scheduled_round":"R10","scheduled_loop":91,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA","symbol":"013360","name":"일성건설","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":1267,"peak_high":1860,"peak_date":"2024-07-23","worst_low":1189,"worst_low_date":"2024-04-17","mfe_pct":46.8,"mae_pct":-6.2,"classification":"positive_local_risk_premium_relief_with_4b_watch","calibration_usable":true,"evidence_family":"small_builder_policy_relief_price_survival_but_pf_repair_bridge_needed","residual_error":"positive_relief_path_still_needs_company_specific_pf_cashflow_bridge_before_green","shadow_rule_candidate":"allow_actionable_only_if_pf_repair_bridge_confirms; attach_4b_after_small_builder_mfe_gt_40"}
{"row_type":"case","case_id":"C30_R10L91_001470_2024_03_27","scheduled_round":"R10","scheduled_loop":91,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA","symbol":"001470","name":"삼부토건","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":1993,"peak_high":2165,"peak_date":"2024-03-29","worst_low":458,"worst_low_date":"2024-09-06","mfe_pct":8.6,"mae_pct":-77.0,"classification":"hard_4c_candidate_construction_policy_beta_without_balance_sheet_trust_bridge","calibration_usable":true,"evidence_family":"construction_policy_political_beta_without_balance_sheet_trust_or_pf_repair","residual_error":"policy_beta_can_create_catastrophic_false_positive_without_company_specific_repair_bridge","shadow_rule_candidate":"route_to_hard_4c_if_construction_policy_beta_mfe_lt_10_and_mae_extreme"}
{"row_type":"case","case_id":"C30_R10L91_002410_2024_03_27","scheduled_round":"R10","scheduled_loop":91,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA","symbol":"002410","name":"범양건영","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":1611,"peak_high":1775,"peak_date":"2024-04-22","worst_low":1114,"worst_low_date":"2024-09-25","mfe_pct":10.2,"mae_pct":-30.9,"classification":"hard_4c_candidate_small_builder_policy_support_without_pf_repair_bridge","calibration_usable":true,"evidence_family":"small_builder_policy_support_without_project_refinancing_cash_collection_margin_bridge","residual_error":"small_builder_policy_support_can_overpromote_to_actionable_without_repair_evidence","shadow_rule_candidate":"block_actionable_green_when_mfe_shallow_mae_large_and_pf_repair_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":91,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":91,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_SMALL_BUILDER_PF_REPAIR_AND_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30 small/mid builders, do not open Stage2-Actionable or Stage3-Green from construction liquidity support, PF soft-landing, political construction beta, or one-off relief rally alone. Require company-specific PF exposure reduction, project-level refinancing, debt maturity extension, cash collection, receivables repair, profitable backlog, margin/OP/FCF conversion, and listing/accounting trust. If MFE is shallow and MAE is large, route to false-positive or hard-4C. If MFE is large but bridge is not explicit, preserve local positive but attach 4B watch.","expected_effect":"Reduce small-builder construction-policy false positives while preserving rare relief positives with low MAE and company-specific repair evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":91,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"small_builder_pf_policy_false_positive_and_trust_guard","contribution":"Adds one small-builder relief positive and two hard-4C small-builder false positives to calibrate C30 PF repair, trust, and 4B/4C routing.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_SMALL_BUILDER_PF_REPAIR_AND_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
AND company_type in [small_builder, mid_builder, construction_policy_beta]:

  Do not open Stage3-Green from:
    - builder liquidity support headline alone
    - real-estate PF soft-landing headline alone
    - political construction beta alone
    - reconstruction / overseas construction theme alone
    - one-week small-builder relief rally alone

  Require at least two of:
    - project-level refinancing
    - PF exposure reduction
    - debt maturity extension
    - cash collection / receivables repair
    - profitable order backlog
    - net debt / liquidity repair
    - OP/FCF conversion
    - clean listing/accounting trust
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -30%:
    route to C30 hard-4C candidate.

  If MFE > 40% but bridge is not explicit:
    allow local positive / Yellow only and attach 4B watch.

  If later row-presence, listing, or accounting trust caveat appears:
    add trust penalty in retrospective validation even if 2024 entry window is not corporate-action contaminated.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_91_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 small-builder PF/policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_SMALL_BUILDER_PF_REPAIR_AND_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks small-builder policy Green without PF/cash-flow/trust bridge,
   - preserves low-MAE local positives only below Green until repair evidence appears,
   - routes shallow-MFE/high-MAE small-builder names to hard-4C,
   - adds listing/accounting trust penalty when later row-presence or listing caveats appear.

Expected next schedule:
completed_round = R10
completed_loop = 91
next_round = R11
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 91
next_round = R11
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
