# E2R Stock-Web v12 Residual Research — R10 / Loop 90

```yaml
scheduled_round: R10
scheduled_loop: 90
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MID_SMALL_BUILDER_PF_LIQUIDITY_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_SECTOR_POLICY_SUPPORT_HEADLINE

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
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 90
next_round: R11
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 90
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
```

Selected symbols for this run:

```text
014790 HL D&I
010780 아이에스동서
005960 동부건설
```

They avoid the C30 top-covered symbols and recent R10 symbols.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
014790: same archetype, new symbol, mid-builder PF/liquidity support bridge
010780: same archetype, new symbol, housing/PF exposure without actionable balance-sheet repair
005960: same archetype, new symbol, small builder policy-support false-positive / shallow-MFE path
```

---

## 3. Price-atlas validation

Manifest fields checked:

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
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
014790 HL D&I
  profile: atlas/symbol_profiles/014/014790.json
  first_date: 1995-05-03
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,728
  corporate_action_candidate_dates:
    1996-01-03, 1997-11-03, 1997-12-27, 1999-12-21, 2010-04-28, 2012-02-06
  2024 entry~D+180 contamination: none

010780 아이에스동서
  profile: atlas/symbol_profiles/010/010780.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,705
  corporate_action_candidate_dates:
    1997-01-03, 1999-08-10, 2002-03-18, 2002-05-20, 2004-06-15, 2005-06-17,
    2005-09-15, 2005-10-10, 2008-08-08, 2011-07-29
  2024 entry~D+180 contamination: none

005960 동부건설
  profile: atlas/symbol_profiles/005/005960.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,653
  corporate_action_candidate_dates:
    1997-01-31, 1999-06-16, 2000-02-22, 2012-09-10, 2014-05-16, 2015-09-04, 2016-11-04
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-03-27
Korea builder liquidity / real-estate PF support policy frame
```

Follow-up policy frame:

```text
2024-05-13
tighter real-estate PF assessment and restructuring acceleration frame
```

C30 is not a simple "construction sector support" or "PF policy exists" archetype. It asks whether a company-specific bridge exists:

```text
PF headline / construction liquidity support
  -> project-level refinancing
  -> default-risk ringfencing
  -> cash collection
  -> net debt or liquidity repair
  -> order backlog margin quality
  -> OP/EPS/FCF conversion
```

The residual error is that a policy firewall can be mistaken for a company escape route. The firewall prevents the neighborhood from burning down; it does not repair every house.

---

## 5. Case 1 — 014790 HL D&I

```yaml
case_id: C30_R10L90_014790_2024_03_27
symbol: "014790"
name: "HL D&I"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MID_SMALL_BUILDER_PF_LIQUIDITY_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_SECTOR_POLICY_SUPPORT_HEADLINE
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price_basis: close
entry_price: 2010
classification: positive_with_company_specific_repair_watch
calibration_usable: true
```

### Evidence interpretation

HL D&I is the constructive mid-builder case in this grid. The trigger is not just "PF support exists." The constructive read is:

```text
small/mid builder risk premium was compressed
  -> price had already washed out
  -> later rebound showed the market accepting some survivability bridge
  -> no 2024 corporate-action contamination in the calibration window
```

The case is still not a clean Green unless company-specific PF, order, and liquidity repair evidence is visible. It is a positive path, but it should remain a guarded positive.

### Price path

Key Stock-Web rows:

```text
2024-03-27: close 2,010
2024-03-28: high 2,025 / close 2,015
2024-04-08: low 1,968 / close 1,976
2024-07-19: high 2,645 / close 2,540
2024-08-23: high 2,880 / close 2,870
2024-09-11: low 2,380 / close 2,400
```

Approximate path from entry close:

```text
entry_close: 2,010
peak_high: 2,880
MFE: +43.3%
worst_low: 1,968
MAE: -2.1%
```

### Interpretation

This is the positive control:

```text
Stage2-Actionable: allowed if firm-specific liquidity/PF bridge is present.
Stage3-Green: still requires project-level and earnings bridge.
4B watch: mild, because MFE exceeded 40% and mid-builder liquidity beta is volatile.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  sector_policy_support: medium_high
  company_specific_repair_bridge: medium
  price_confirmation: high
  drawdown_penalty: low
  PF_opacity_penalty: medium
  actionability_cap: Yellow/Actionable unless company bridge confirms
```

---

## 6. Case 2 — 010780 아이에스동서

```yaml
case_id: C30_R10L90_010780_2024_03_27
symbol: "010780"
name: "아이에스동서"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MID_SMALL_BUILDER_PF_LIQUIDITY_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_SECTOR_POLICY_SUPPORT_HEADLINE
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price_basis: close
entry_price: 29250
classification: hard_4c_candidate_policy_support_without_company_specific_repair_bridge
calibration_usable: true
```

### Evidence interpretation

아이에스동서 shows the typical C30 trap. It can look like a better-quality construction / property-exposed name, but if the model cannot connect policy support to company-level PF reduction, cash collection, and earnings repair, the trade is still a high-MAE false-positive.

### Price path

Key Stock-Web rows:

```text
2024-03-27: close 29,250
2024-03-28: high 30,000 / close 29,450
2024-03-29: high 30,450 / close 28,750
2024-08-05: low 20,350 / close 20,600
2024-08-27: high 24,900 / close 24,850
2024-09-09: low 21,300 / close 21,700
```

Approximate path from entry close:

```text
entry_close: 29,250
peak_high: 30,450
MFE: +4.1%
worst_low: 20,350
MAE: -30.4%
```

### Interpretation

This is the hard guardrail case.

```text
Stage2-Watch: allowed from PF policy context.
Stage2-Actionable: blocked unless company-specific repair bridge exists.
Stage3-Green: blocked.
Hard 4C candidate: yes.
```

The price path says the sector headline did not become an equity escape route.

### Stress-test components

```text
raw_component_score_proxy:
  sector_policy_support: medium_high
  company_specific_repair_bridge: weak
  price_confirmation: weak
  drawdown_penalty: high
  PF_opacity_penalty: high
  4C_guard_required: yes
```

---

## 7. Case 3 — 005960 동부건설

```yaml
case_id: C30_R10L90_005960_2024_03_27
symbol: "005960"
name: "동부건설"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: MID_SMALL_BUILDER_PF_LIQUIDITY_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_SECTOR_POLICY_SUPPORT_HEADLINE
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price_basis: close
entry_price: 5030
classification: counterexample_shallow_mfe_policy_support_false_positive
calibration_usable: true
```

### Evidence interpretation

동부건설 is the shallow-MFE false-positive case. It did not fail as violently as 아이에스동서, but it still failed the actionability test. If a model opens Actionable merely because the government is supporting builders, it will catch names where there is no visible bridge to balance-sheet repair or profit recovery.

### Price path

Key Stock-Web rows:

```text
2024-03-27: close 5,030
2024-03-28: high 5,070 / close 5,010
2024-07-18: high 4,985 / close 4,930
2024-08-05: low 4,365 / close 4,435
2024-09-09: low 4,175 / close 4,330
```

Approximate path from entry close:

```text
entry_close: 5,030
peak_high: 5,070
MFE: +0.8%
worst_low: 4,175
MAE: -17.0%
```

### Interpretation

This is a C30 false-positive but not the hardest 4C.

```text
Stage2-Watch: possible.
Stage2-Actionable: blocked by shallow MFE and no bridge.
Stage3-Green: blocked.
Hard 4C: no, but false-positive guard applies.
```

### Stress-test components

```text
raw_component_score_proxy:
  sector_policy_support: medium
  company_specific_repair_bridge: weak
  price_confirmation: failed
  drawdown_penalty: medium_high
  actionability_cap: Watch only
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C30 grid:

```text
014790 HL D&I:
  positive path when mid-builder risk premium compresses and price confirms.
  Still needs company-specific PF/liquidity bridge before Green.

010780 아이에스동서:
  hard 4C candidate.
  Generic PF policy support did not prevent large forward drawdown.

005960 동부건설:
  shallow-MFE false-positive.
  Policy support headline did not become an actionable equity path.
```

Shared rule:

```text
C30 is not "government supports construction."
C30 is "support + project-level refinancing + liquidity repair + balance-sheet survival + earnings conversion."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L90_014790_2024_03_27","scheduled_round":"R10","scheduled_loop":90,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_LIQUIDITY_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_SECTOR_POLICY_SUPPORT_HEADLINE","symbol":"014790","name":"HL D&I","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":2010,"peak_high":2880,"peak_date":"2024-08-23","worst_low":1968,"worst_low_date":"2024-04-08","mfe_pct":43.3,"mae_pct":-2.1,"classification":"positive_with_company_specific_repair_watch","calibration_usable":true,"evidence_family":"mid_builder_pf_liquidity_support_to_survivability_repair_bridge","residual_error":"positive_path_still_needs_company_specific_pf_balance_sheet_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_pf_support_and_low_mae_price_confirmation_align_but_require_bridge_for_green"}
{"row_type":"case","case_id":"C30_R10L90_010780_2024_03_27","scheduled_round":"R10","scheduled_loop":90,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_LIQUIDITY_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_SECTOR_POLICY_SUPPORT_HEADLINE","symbol":"010780","name":"아이에스동서","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":29250,"peak_high":30450,"peak_date":"2024-03-29","worst_low":20350,"worst_low_date":"2024-08-05","mfe_pct":4.1,"mae_pct":-30.4,"classification":"hard_4c_candidate_policy_support_without_company_specific_repair_bridge","calibration_usable":true,"evidence_family":"housing_pf_exposure_policy_support_without_cash_collection_repair_bridge","residual_error":"generic_policy_support_can_overpromote_property_exposed_builder","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_without_company_specific_repair_bridge"}
{"row_type":"case","case_id":"C30_R10L90_005960_2024_03_27","scheduled_round":"R10","scheduled_loop":90,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_LIQUIDITY_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_SECTOR_POLICY_SUPPORT_HEADLINE","symbol":"005960","name":"동부건설","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":5030,"peak_high":5070,"peak_date":"2024-03-28","worst_low":4175,"worst_low_date":"2024-09-09","mfe_pct":0.8,"mae_pct":-17.0,"classification":"counterexample_shallow_mfe_policy_support_false_positive","calibration_usable":true,"evidence_family":"small_builder_policy_support_without_refinancing_or_backlog_margin_bridge","residual_error":"policy_support_headline_does_not_create_actionable_equity_path","shadow_rule_candidate":"cap_at_watch_if_builder_has_no_project_refinancing_cash_collection_or_margin_bridge"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":90,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_SMALL_BUILDER_PF_LIQUIDITY_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_SECTOR_POLICY_SUPPORT_HEADLINE","case_count":3,"positive_case_count":1,"counterexample_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":90,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_COMPANY_SPECIFIC_PF_REPAIR_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30, do not open Stage2-Actionable or Stage3-Green from construction liquidity support, real-estate PF soft-landing, or sector policy headline alone. Require company-specific refinancing, PF exposure reduction, cash collection, impaired project ringfence, margin/order conversion, and post-trigger price survival. If MFE is shallow and MAE is large, route to false-positive or hard-4C candidate.","expected_effect":"Reduce mid/small builder PF policy false positives while preserving positive cases where price confirms and company-specific repair bridge exists.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":90,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"mid_small_builder_pf_policy_false_positive_guard","contribution":"Adds one mid-builder positive and two policy-support false positives to separate sector soft-landing policy from company-specific balance-sheet repair.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_COMPANY_SPECIFIC_PF_REPAIR_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK:

  Do not open Stage3-Green from:
    - government construction liquidity support headline alone
    - real-estate PF soft-landing headline alone
    - syndicated loan / guarantee headline alone
    - sector-wide restructuring headline alone
    - one-day builder relief rally alone

  Require at least two of:
    - project-level refinancing or maturity extension
    - PF exposure reduction
    - default-risk ringfence
    - cash collection / receivables improvement
    - net debt or liquidity repair
    - order backlog margin quality
    - OP/EPS/FCF conversion
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -20%:
    route to C30 false-positive / hard-4C candidate.

  If MFE > 30% but company-specific bridge remains weak:
    allow Actionable or Yellow, but cap Green until repair evidence appears.

  For small/mid builders:
    raise evidence threshold because PF opacity is higher.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_90_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 construction/PF cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_COMPANY_SPECIFIC_PF_REPAIR_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks sector PF policy support from Green without company-specific repair bridge,
   - allows Actionable when PF support plus price confirmation and low MAE align,
   - routes shallow-MFE/high-MAE builder cases to C30 false-positive or hard-4C.

Expected next schedule:
completed_round = R10
completed_loop = 90
next_round = R11
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```
