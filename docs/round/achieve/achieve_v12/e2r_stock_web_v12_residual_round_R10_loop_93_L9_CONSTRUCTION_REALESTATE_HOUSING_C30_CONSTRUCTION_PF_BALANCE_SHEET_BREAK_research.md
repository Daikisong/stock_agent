# E2R Stock-Web v12 Residual Research — R10 / Loop 93

```yaml
scheduled_round: R10
scheduled_loop: 93
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE

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
accounting_or_listing_trust_caveat_count: 0
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 93
next_round: R11
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 93
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is a hard L9 construction / real-estate / housing round.

The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

The selected fine branch is:

```text
regional housing / PF exposure / presale and backlog margin trust bridge
vs small-builder policy relief spike
```

This deliberately avoids the prior R10 loop92 branch:

```text
PF workout / parent support / regional-builder balance-sheet trust bridge
```

It also avoids the heavily used top-covered C30 symbols and the recent R10 loop88~92 sets.

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
```

Selected symbols:

```text
035890 서희건설
013120 동원개발
017000 신원종합개발
```

They avoid the C30 top-covered list and recent R10 loop88~92 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
035890: same archetype, new symbol, regional housing / presale backlog price-survival positive branch
013120: same archetype, new symbol, regional developer policy relief label without repair bridge Watch cap
017000: same archetype, new symbol, small-builder relief spike / political-construction beta hard-4C branch
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
035890 서희건설
  profile: atlas/symbol_profiles/035/035890.json
  first_date: 1999-12-24
  last_date: 2025-08-11
  raw_last_date: 2026-02-20
  tradable_ohlcv rows: 6,310
  non_tradable_zero_volume rows: 135
  corporate_action_candidate_dates:
    2000-10-23, 2000-11-07, 2003-12-10, 2004-11-19, 2005-05-17,
    2006-02-17, 2007-07-19, 2012-01-06, 2012-07-12
  2024 entry~D+180 contamination: none
  status_inferred: active_like
  caveat:
    latest tradable last_date differs from raw_last_date; this is not inside the 2024 validation window.

013120 동원개발
  profile: atlas/symbol_profiles/013/013120.json
  first_date: 1996-07-01
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,565
  non_tradable_zero_volume rows: 857
  corporate_action_candidate_dates:
    1999-08-03, 2015-12-01
  2024 entry~D+180 contamination: none
  status_inferred: active_like

017000 신원종합개발
  profile: atlas/symbol_profiles/017/017000.json
  first_date: 1996-07-11
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,870
  non_tradable_zero_volume rows: 552
  corporate_action_candidate_dates:
    1999-01-04, 1999-10-26, 1999-12-14, 2000-03-03,
    2002-06-25, 2003-12-22, 2009-05-14, 2015-05-26
  2024 entry~D+180 contamination: none
  status_inferred: active_like
```

---

## 4. Archetype residual problem

C30 is about construction PF / balance-sheet break, not a generic housing-policy or small-builder rally.

The model can over-score:

```text
housing-policy relief
PF stabilization headline
regional builder label
small-builder political beta
presale recovery hope
construction low-PBR sympathy
one-week construction-stock spike
```

The C30 bridge must be stricter:

```text
housing / construction relief event
  -> company-specific PF exposure check
  -> project cash collection
  -> presale and backlog quality
  -> debt maturity and funding terms
  -> cost escalation and margin risk
  -> accounting / listing / tradeability trust
  -> price survival after the first relief spike
```

A construction rally is like scaffolding around a half-built apartment. It can make the site look safer, but equity value returns only when the financing, presales, cost ledger, and trust beams hold weight.

---

## 5. Case 1 — 035890 서희건설

```yaml
case_id: C30_R10L93_035890_2024_08_20
symbol: "035890"
name: "서희건설"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE
trigger_date: 2024-08-20
entry_date: 2024-08-20
entry_price_basis: close
entry_price: 1405
classification: positive_capped_regional_housing_presale_backlog_price_survival_bridge
calibration_usable: true
```

### Evidence interpretation

서희건설 is the constructive control in this set.

The useful C30 read is not simply:

```text
regional builder went up
```

It is:

```text
regional housing / presale backlog relevance
  -> relatively controlled post-trigger drawdown
  -> gradual price confirmation
  -> policy relief interpreted through price survival
```

The path did not create a violent one-day relief spike. It behaved more like a controlled regional-builder rerating. That makes it a capped C30 positive.

### Price path

Key Stock-Web rows:

```text
2024-08-20: high 1,407 / close 1,405
2024-08-21: high 1,459 / close 1,458
2024-08-26: high 1,483 / close 1,476
2024-09-12: high 1,518 / close 1,500
2024-10-10: high 1,621 / close 1,577
2024-10-28: low 1,378 / close 1,417
```

Approximate path from entry close:

```text
entry_close: 1,405
peak_high: 1,621
MFE: +15.4%
worst_low_after_entry: 1,378
MAE: -1.9%
```

### Interpretation

This is a C30 capped positive:

```text
Stage2-Actionable: allowed if PF exposure, presale, backlog, and cash-flow bridge are explicit.
Stage3-Green: blocked without margin, debt-maturity, and project-cash evidence.
Local 4B: not mandatory from this path alone, but keep Watch if later trust gap appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  regional_housing_relevance: high
  presale_backlog_bridge: medium_high
  pf_exposure_clarity: medium
  price_survival: high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 013120 동원개발

```yaml
case_id: C30_R10L93_013120_2024_02_05
symbol: "013120"
name: "동원개발"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE
trigger_date: 2024-02-05
entry_date: 2024-02-05
entry_price_basis: close
entry_price: 3100
classification: watch_cap_regional_developer_policy_relief_without_pf_cashflow_repair_bridge
calibration_usable: true
```

### Evidence interpretation

동원개발 is the regional-developer Watch cap.

It had a stable builder/developer label and was exposed to the same broad housing-policy relief frame. But the path did not show enough evidence for Actionable/Green. The stock did not collapse like a hard PF crisis, but it drifted into a material drawdown.

The model risk is over-certainty:

```text
regional developer
  -> housing policy support
  -> low-volatility builder label
  -> model opens Actionable
  -> no clear PF/cash-flow/margin repair bridge
  -> slow MAE accumulates
```

### Price path

Key Stock-Web rows:

```text
2024-02-05: high 3,120 / close 3,100
2024-02-06: high 3,140 / close 3,085
2024-02-13: high 3,115 / close 3,110
2024-03-08: low 2,840 / close 2,865
2024-08-05: low 2,460 / close 2,510
2024-09-20: high 2,870 / close 2,710
```

Approximate path from entry close:

```text
entry_close: 3,100
peak_high: 3,140
MFE: +1.3%
worst_low_after_entry: 2,460
MAE: -20.6%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from regional housing relevance.
Stage2-Actionable: blocked unless PF exposure, cash collection, presale, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not extreme, but false-positive guard applies.
```

This case is not about disaster. It is about preventing a stable-looking builder from being over-promoted without company-specific repair evidence.

### Stress-test components

```text
raw_component_score_proxy:
  regional_developer_label: medium_high
  housing_policy_relief_signal: medium
  pf_cashflow_repair_bridge: weak
  margin_backlog_bridge: weak
  price_confirmation: failed
  drawdown_penalty: medium_high
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 017000 신원종합개발

```yaml
case_id: C30_R10L93_017000_2024_08_20
symbol: "017000"
name: "신원종합개발"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE
trigger_date: 2024-08-20
entry_date: 2024-08-20
entry_price_basis: close
entry_price: 4080
classification: hard_4c_candidate_small_builder_policy_relief_spike_without_repair_trust_bridge
calibration_usable: true
```

### Evidence interpretation

신원종합개발 is the hard guardrail case.

It had the classic C30 trap:

```text
small builder
  -> policy or political construction beta
  -> violent spike
  -> model reads it as balance-sheet repair
  -> no durable PF / cash-flow / margin bridge
  -> large MAE follows
```

The stock had already accelerated into the trigger. The post-trigger MFE was shallow while the later downside became large. This is the shape of a hard C30 false positive.

### Price path

Key Stock-Web rows:

```text
2024-08-09: high 3,405 / close 3,405
2024-08-12: high 3,840 / close 3,455
2024-08-19: high 4,150 / close 4,150
2024-08-20: high 4,280 / close 4,080
2024-09-27: low 3,220 / close 3,405
2024-10-24: low 2,995 / close 3,015
2024-11-07: low 2,710 / close 2,815
```

Approximate path from entry close:

```text
entry_close: 4,080
peak_high: 4,280
MFE: +4.9%
worst_low_after_entry: 2,710
MAE: -33.6%
```

### Interpretation

This is a hard C30 false-positive:

```text
Stage2-Watch: possible from small-builder / policy-relief relevance.
Stage2-Actionable: blocked without project-level PF repair and trust bridge.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and large MAE.
```

The key lesson:

```text
small-builder spike is not PF repair.
Construction policy beta is not balance-sheet trust.
```

### Stress-test components

```text
raw_component_score_proxy:
  small_builder_policy_beta: high
  pf_repair_bridge: weak
  project_cashflow_bridge: weak
  margin_trust_bridge: weak
  price_confirmation: shallow_after_trigger
  drawdown_penalty: high
  hard_4c_guard: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
accounting_or_listing_trust_caveat_count: 0
calibration_usable_trigger_count: 3
```

The three-case C30 regional-housing grid:

```text
035890 서희건설:
  regional housing / presale backlog positive;
  controlled MAE and gradual MFE, but Green still requires PF and cash-flow bridge.

013120 동원개발:
  stable regional-developer label did not validate Actionable.
  Shallow MFE and material MAE, Watch/Yellow cap.

017000 신원종합개발:
  small-builder policy spike failed.
  Shallow post-trigger MFE and large MAE, hard 4C.
```

Shared rule:

```text
C30 is not "housing policy relief."
C30 is "this builder's PF exposure, presale backlog, debt maturity, project cash flow, and margin trust are repaired enough to support equity value."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L93_035890_2024_08_20","scheduled_round":"R10","scheduled_loop":93,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE","symbol":"035890","name":"서희건설","trigger_date":"2024-08-20","entry_date":"2024-08-20","entry_price":1405,"peak_high":1621,"peak_date":"2024-10-10","worst_low_after_entry":1378,"worst_low_after_entry_date":"2024-10-28","mfe_pct":15.4,"mae_pct":-1.9,"classification":"positive_capped_regional_housing_presale_backlog_price_survival_bridge","calibration_usable":true,"evidence_family":"regional_housing_presale_backlog_pf_exposure_price_survival_bridge","residual_error":"positive_path_still_needs_pf_cashflow_margin_trust_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_presale_backlog_pf_and_cashflow_bridge_confirm_but_cap_green_without_margin_trust_evidence"}
{"row_type":"case","case_id":"C30_R10L93_013120_2024_02_05","scheduled_round":"R10","scheduled_loop":93,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE","symbol":"013120","name":"동원개발","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":3100,"peak_high":3140,"peak_date":"2024-02-06","worst_low_after_entry":2460,"worst_low_after_entry_date":"2024-08-05","mfe_pct":1.3,"mae_pct":-20.6,"classification":"watch_cap_regional_developer_policy_relief_without_pf_cashflow_repair_bridge","calibration_usable":true,"evidence_family":"regional_developer_housing_policy_relief_without_pf_cash_collection_margin_bridge","residual_error":"stable_regional_developer_label_can_overpromote_without_company_specific_repair_evidence","shadow_rule_candidate":"cap_regional_developer_policy_relief_at_watch_yellow_if_mfe_shallow_and_pf_cashflow_bridge_missing"}
{"row_type":"case","case_id":"C30_R10L93_017000_2024_08_20","scheduled_round":"R10","scheduled_loop":93,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE","symbol":"017000","name":"신원종합개발","trigger_date":"2024-08-20","entry_date":"2024-08-20","entry_price":4080,"peak_high":4280,"peak_date":"2024-08-20","worst_low_after_entry":2710,"worst_low_after_entry_date":"2024-11-07","mfe_pct":4.9,"mae_pct":-33.6,"classification":"hard_4c_candidate_small_builder_policy_relief_spike_without_repair_trust_bridge","calibration_usable":true,"evidence_family":"small_builder_policy_relief_spike_without_pf_repair_project_cashflow_margin_trust_bridge","residual_error":"small_builder_policy_spike_can_fail_when_pf_repair_and_trust_bridge_missing","shadow_rule_candidate":"route_small_builder_policy_spike_to_hard_4c_if_mfe_shallow_mae_large_and_repair_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":93,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"accounting_or_listing_trust_caveat_count":0,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":93,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_REGIONAL_HOUSING_PF_CASHFLOW_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30 regional housing and small-builder cases, do not open Stage2-Actionable or Stage3-Green from housing policy relief, regional developer label, small-builder spike, presale recovery hope, or one-week construction-stock volume spike alone. Require company-specific PF exposure reduction, presale/backlog quality, project cash collection, debt maturity and funding terms, cost escalation and margin risk check, accounting/listing/tradeability trust, and post-trigger price survival. Regional housing names with controlled MAE may be capped positives only when presale/backlog and cash-flow bridge are explicit. Stable regional-developer labels with shallow MFE should cap at Watch/Yellow without PF repair evidence. Small-builder policy spikes with shallow MFE and large MAE should route to hard-4C.","expected_effect":"Reduce construction policy and small-builder false positives while preserving rare regional housing positives with controlled MAE and explicit PF/cash-flow trust bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":93,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"regional_housing_pf_cashflow_trust_guard","contribution":"Adds one regional housing capped positive, one stable-developer Watch cap, and one small-builder hard-4C counterexample to calibrate C30 PF/cash-flow/trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_REGIONAL_HOUSING_PF_CASHFLOW_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
AND company_type in [regional_builder, residential_developer, small_builder]:

  Do not open Stage3-Green from:
    - housing policy relief headline alone
    - regional builder label alone
    - presale recovery hope alone
    - low-PBR construction label alone
    - small-builder political / policy beta alone
    - one-week construction-stock volume spike alone

  Require at least two of:
    - company-specific PF exposure reduction
    - presale or backlog quality
    - project cash collection / receivables repair
    - debt maturity extension or funding clarity
    - cost escalation and margin-risk containment
    - OP/FCF conversion
    - accounting / listing / tradeability trust
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -30%:
    route to C30 hard-4C candidate.

  If MFE < 5% and MAE is material:
    cap at Watch/Yellow unless explicit PF/cash-flow repair appears.

  If MFE > 15% and MAE remains controlled:
    allow capped Actionable only if presale/backlog and PF trust bridge are explicit.

  If the rally is a small-builder spike after prior acceleration:
    block Green unless the repair evidence is company-specific and current.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_93_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 regional-housing / PF-cashflow / small-builder cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_REGIONAL_HOUSING_PF_CASHFLOW_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks housing-policy Green without PF/cash-flow/trust bridge,
   - preserves regional housing positives only with controlled MAE and presale/backlog evidence,
   - caps stable regional developers at Watch/Yellow without repair bridge,
   - routes shallow-MFE/high-MAE small-builder policy spikes to hard-4C.

Expected next schedule:
completed_round = R10
completed_loop = 93
next_round = R11
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 93
next_round = R11
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
