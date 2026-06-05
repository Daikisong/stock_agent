# E2R Stock-Web v12 Residual Research — R10 / Loop 94

```yaml
scheduled_round: R10
scheduled_loop: 94
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE

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
listing_or_row_presence_caveat_count: 1
accounting_or_listing_trust_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 94
next_round: R11
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_94_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 94
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is a hard L9 construction / real-estate / housing round.

The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

The selected fine branch is:

```text
small / regional / civil builders
policy-relief and housing-infra theme spikes
vs actual PF, cash-flow, backlog, and trust repair
```

This deliberately avoids:
- the loop93 R10 regional housing branch using `035890`, `013120`, `017000`;
- the loop92 R10 PF-workout branch using `034300`, `009410`, `002460`;
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
```

Selected symbols:

```text
001260 남광토건
010960 삼호개발
001840 이화공영
```

They avoid the C30 top-covered list and avoid recent R10 loop88~93 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
001260: same archetype, new symbol, civil/regional construction relief positive with 4B watch
010960: same archetype, new symbol, civil construction / infrastructure label Watch cap without PF-cashflow repair bridge
001840: same archetype, new symbol, small construction policy-theme late spike hard-4C with row-presence/trust caveat
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
001260 남광토건
  profile: atlas/symbol_profiles/001/001260.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,561
  non_tradable_zero_volume rows: 204
  corporate_action_candidate_dates:
    1999-05-13, 1999-05-20, 2004-05-06, 2005-06-03,
    2007-12-26, 2009-07-02, 2012-04-17, 2013-02-15,
    2015-04-20, 2016-02-05
  2024 entry~D+180 contamination: none
  status_inferred: active_like

010960 삼호개발
  profile: atlas/symbol_profiles/010/010960.json
  first_date: 2002-07-16
  last_date: 2026-02-20
  market:
    KOSDAQ until 2005-05-11
    KOSPI from 2005-05-12
  tradable_ohlcv rows: 5,825
  corporate_action_candidate_dates:
    2008-08-29, 2010-06-11
  2024 entry~D+180 contamination: none
  status_inferred: active_like

001840 이화공영
  profile: atlas/symbol_profiles/001/001840.json
  first_date: 1996-07-30
  last_date: 2025-04-01
  raw_last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,423
  non_tradable_zero_volume rows: 999
  corporate_action_candidate_dates:
    1997-12-11, 1998-01-31, 2003-12-01, 2003-12-29,
    2010-04-22, 2010-05-17, 2014-07-18
  2024 entry~D+180 contamination: none
  status_inferred: active_like
  caveat:
    latest tradable last_date differs from raw_last_date and non_tradable_zero_volume count is high.
    This does not directly contaminate the 2024 entry window, but it requires row-presence/tradeability trust caution.
```

---

## 4. Archetype residual problem

C30 is about construction PF, balance-sheet repair, project cash flow, and trust. It is not a generic "construction stock is moving" or "housing policy relief" label.

The model can over-score:

```text
housing policy relief
regional builder label
civil construction / infrastructure label
small construction company spike
political construction beta
low-PBR builder sympathy
one-week construction-stock volume spike
```

The C30 bridge must be stricter:

```text
construction / real-estate relief event
  -> company-specific PF exposure
  -> project cash collection and receivables
  -> presale / backlog quality
  -> debt maturity and funding terms
  -> cost escalation and margin risk
  -> accounting / listing / tradeability trust
  -> price survival after the first policy or construction-theme spike
```

A C30 construction rally is like fresh scaffolding around an old building. It looks safer, but equity value only improves when the beams, financing, receivables, margins, and trust actually hold weight.

---

## 5. Case 1 — 001260 남광토건

```yaml
case_id: C30_R10L94_001260_2024_07_24
symbol: "001260"
name: "남광토건"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 6950
classification: positive_capped_civil_regional_construction_relief_price_survival_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

남광토건 is the constructive control in this R10 set.

The useful C30 read is not:

```text
small construction stock spiked
```

It is:

```text
civil/regional construction relevance
  -> construction-relief theme
  -> price confirmation after trigger
  -> controlled enough drawdown for a capped positive
```

The path had a meaningful MFE after the July trigger, while the later MAE stayed below the hard-failure zone. That makes it a capped C30 positive, not a Green.

### Price path

Key Stock-Web rows:

```text
2024-07-24: close 6,950
2024-07-30: high 8,550 / close 7,580
2024-07-31: high 8,340 / close 7,830
2024-08-05: low 6,450 / close 6,530
2024-09-25: high 6,600 / close 6,570
2024-11-06: high 7,200 / close 7,050
```

Approximate path from entry close:

```text
entry_close: 6,950
peak_high: 8,550
MFE: +23.0%
worst_low_after_entry: 5,950
MAE: -14.4%
```

### Interpretation

This is a C30 capped positive with 4B watch:

```text
Stage2-Actionable: allowed only if PF exposure, project cash collection, and backlog/margin bridge are explicit.
Stage3-Green: blocked without debt-maturity, cash-flow, and margin trust evidence.
Local 4B: required after +20% MFE unless fresh project-cash and trust evidence appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  civil_regional_construction_relevance: high
  policy_relief_signal: medium_high
  pf_cashflow_bridge: medium_or_unclear
  price_confirmation: medium_high
  drawdown_penalty: medium
  green_cap: yes
  local_4b_overlay: required_after_theme_mfe
```

---

## 6. Case 2 — 010960 삼호개발

```yaml
case_id: C30_R10L94_010960_2024_07_30
symbol: "010960"
name: "삼호개발"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE
trigger_date: 2024-07-30
entry_date: 2024-07-30
entry_price_basis: close
entry_price: 3650
classification: watch_cap_civil_construction_infra_label_without_pf_cashflow_repair_bridge
calibration_usable: true
```

### Evidence interpretation

삼호개발 is the Watch/Yellow cap case.

The setup had construction/civil-infra relevance:

```text
civil construction / infrastructure work
  -> construction policy or infrastructure relief sympathy
  -> stable balance-sheet-looking builder label
```

But the forward path did not validate Actionable/Green. The MFE was effectively exhausted at the trigger, and the later drift was negative.

### Price path

Key Stock-Web rows:

```text
2024-07-30: high 3,650 / close 3,650
2024-07-31: high 3,645 / close 3,600
2024-08-05: low 3,255 / close 3,310
2024-08-19: low 3,215 / close 3,275
2024-09-06: low 3,225 / close 3,250
2024-10-14: low 3,090 / close 3,120
2024-11-07: high 3,290 / close 3,175
```

Approximate path from entry close:

```text
entry_close: 3,650
peak_high_after_entry: 3,650
MFE: 0.0%
worst_low_after_entry: 3,090
MAE: -15.3%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from civil construction and infrastructure relevance.
Stage2-Actionable: blocked unless project-level cash flow, receivables, backlog, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MAE did not cross hard threshold, but actionability is capped.
```

The lesson is that stable civil-construction relevance is not enough. The C30 bridge must show balance-sheet repair or project cash-flow strength.

### Stress-test components

```text
raw_component_score_proxy:
  civil_construction_label: medium_high
  infrastructure_theme_signal: medium
  pf_cashflow_bridge: weak
  backlog_margin_bridge: weak
  price_confirmation_after_entry: failed
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 001840 이화공영

```yaml
case_id: C30_R10L94_001840_2024_07_31
symbol: "001840"
name: "이화공영"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE
trigger_date: 2024-07-31
entry_date: 2024-07-31
entry_price_basis: close
entry_price: 3765
classification: hard_4c_candidate_small_construction_policy_theme_late_spike_without_pf_cashflow_trust_bridge
calibration_usable: true
```

### Evidence interpretation

이화공영 is the hard guardrail case.

The trigger had the classic C30 late-spike trap:

```text
small construction company
  -> housing/infrastructure/policy theme heat
  -> one-day extreme volume and price spike
  -> model mistakes spike for balance-sheet repair
  -> no durable PF / cash-flow / trust bridge
```

From the selected close after the spike, additional MFE was shallow while the later downside was severe. The profile also has a row-presence/tradeability caveat outside the 2024 window, so this case should carry extra trust caution.

### Price path

Key Stock-Web rows:

```text
2024-07-30: high 3,025 / close 3,025
2024-07-31: high 3,930 / close 3,765
2024-08-02: high 4,000 / close 3,530
2024-08-05: low 2,855 / close 3,055
2024-08-20: high 3,890 / close 3,730
2024-09-06: low 2,535 / close 2,535
2024-10-22: low 2,300 / close 2,315
```

Approximate path from entry close:

```text
entry_close: 3,765
peak_high_after_entry: 4,000
MFE: +6.2%
worst_low_after_entry: 2,300
MAE: -38.9%
```

### Interpretation

This is a hard C30 false-positive:

```text
Stage2-Watch: possible from small construction and policy-theme relevance.
Stage2-Actionable: blocked without PF exposure, project-cash, and trust bridge.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and large MAE.
Accounting/listing/tradeability trust caveat: yes, due profile row-presence caveat outside the validation window.
```

The lesson is that a small construction spike is not balance-sheet repair.

### Stress-test components

```text
raw_component_score_proxy:
  small_construction_policy_beta: high
  pf_repair_bridge: weak
  project_cashflow_bridge: weak
  accounting_listing_tradeability_trust: weak_to_medium
  price_confirmation_after_entry: shallow
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
listing_or_row_presence_caveat_count: 1
accounting_or_listing_trust_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C30 small/regional/civil builder grid:

```text
001260 남광토건:
  civil/regional construction relief positive;
  meaningful MFE and non-hard MAE, but Green requires PF/cash-flow trust bridge.

010960 삼호개발:
  civil construction / infrastructure label failed to confirm after entry;
  Watch/Yellow cap without project-cash and margin bridge.

001840 이화공영:
  small construction policy-theme late spike failed;
  shallow MFE and high MAE, hard 4C with row-presence/trust caveat.
```

Shared rule:

```text
C30 is not "construction theme is hot."
C30 is "PF exposure, receivables, presales/backlog, debt maturity, project cash, margin, and trust are repaired enough for equity value."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L94_001260_2024_07_24","scheduled_round":"R10","scheduled_loop":94,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE","symbol":"001260","name":"남광토건","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":6950,"peak_high":8550,"peak_date":"2024-07-30","worst_low_after_entry":5950,"worst_low_after_entry_date":"2024-10-04","mfe_pct":23.0,"mae_pct":-14.4,"classification":"positive_capped_civil_regional_construction_relief_price_survival_with_4b_watch","calibration_usable":true,"evidence_family":"civil_regional_construction_policy_relief_price_survival_without_full_pf_cashflow_trust_bridge","residual_error":"positive_construction_relief_path_requires_4b_and_green_block_without_pf_cashflow_margin_trust_evidence","shadow_rule_candidate":"allow_capped_actionable_when_civil_builder_price_survival_confirms_but_require_pf_cashflow_trust_for_green"}
{"row_type":"case","case_id":"C30_R10L94_010960_2024_07_30","scheduled_round":"R10","scheduled_loop":94,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE","symbol":"010960","name":"삼호개발","trigger_date":"2024-07-30","entry_date":"2024-07-30","entry_price":3650,"peak_high":3650,"peak_date":"2024-07-30","worst_low_after_entry":3090,"worst_low_after_entry_date":"2024-10-14","mfe_pct":0.0,"mae_pct":-15.3,"classification":"watch_cap_civil_construction_infra_label_without_pf_cashflow_repair_bridge","calibration_usable":true,"evidence_family":"civil_construction_infrastructure_label_without_project_cashflow_backlog_margin_bridge","residual_error":"stable_civil_construction_label_can_overpromote_without_pf_cash_collection_and_margin_repair","shadow_rule_candidate":"cap_civil_construction_label_at_watch_yellow_if_mfe_absent_and_cashflow_bridge_missing"}
{"row_type":"case","case_id":"C30_R10L94_001840_2024_07_31","scheduled_round":"R10","scheduled_loop":94,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE","symbol":"001840","name":"이화공영","trigger_date":"2024-07-31","entry_date":"2024-07-31","entry_price":3765,"peak_high":4000,"peak_date":"2024-08-02","worst_low_after_entry":2300,"worst_low_after_entry_date":"2024-10-22","mfe_pct":6.2,"mae_pct":-38.9,"classification":"hard_4c_candidate_small_construction_policy_theme_late_spike_without_pf_cashflow_trust_bridge","calibration_usable":true,"listing_or_row_presence_caveat":true,"evidence_family":"small_construction_policy_theme_late_spike_without_pf_project_cashflow_tradeability_trust_bridge","residual_error":"small_builder_policy_theme_spike_can_fail_when_pf_cashflow_and_trust_bridge_missing","shadow_rule_candidate":"route_small_construction_late_spike_to_hard_4c_if_mfe_shallow_mae_large_and_trust_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":94,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"listing_or_row_presence_caveat_count":1,"accounting_or_listing_trust_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":94,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_SMALL_CIVIL_BUILDER_PF_CASHFLOW_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30 small, regional, and civil builders, do not open Stage2-Actionable or Stage3-Green from construction-theme heat, housing-policy relief, infrastructure sympathy, civil-construction label, small-builder political beta, low-PBR builder label, or one-week construction-stock spike alone. Require company-specific PF exposure, project cash collection and receivables, presale/backlog quality, debt maturity and funding terms, cost escalation and margin-risk check, accounting/listing/tradeability trust, and post-trigger price survival. Capped positives may be allowed when MFE is meaningful and MAE is controlled, but Green requires explicit PF/cash-flow/margin trust. Civil-construction labels with absent MFE should cap at Watch/Yellow. Small construction late spikes with shallow MFE and high MAE should route to hard-4C, especially when row-presence or tradeability trust caveats exist.","expected_effect":"Reduce construction-theme and small-builder late-spike false positives while preserving rare C30 positives with price survival and explicit PF/cash-flow/trust bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":94,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"small_civil_builder_pf_cashflow_trust_guard","contribution":"Adds one civil/regional construction capped positive, one civil-construction Watch cap, and one small construction hard-4C with row-presence caveat to calibrate C30 PF, cash-flow, and trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_SMALL_CIVIL_BUILDER_PF_CASHFLOW_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
AND company_type in [small_builder, regional_builder, civil_construction, infrastructure_contractor]:

  Do not open Stage3-Green from:
    - housing policy relief headline alone
    - infrastructure or civil-construction label alone
    - small-builder political / policy beta alone
    - construction-stock volume spike alone
    - low-PBR builder label alone

  Require at least two of:
    - company-specific PF exposure reduction
    - project cash collection / receivables repair
    - presale or backlog quality
    - debt maturity / funding clarity
    - cost escalation and margin-risk containment
    - OP/FCF conversion
    - accounting / listing / tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the policy/construction headline

  If MFE < 10% and MAE < -30%:
    route to C30 hard-4C candidate.

  If MFE is absent and cash-flow bridge is weak:
    cap at Watch/Yellow.

  If MFE is meaningful but bridge is not refreshed:
    preserve as capped positive or local 4B, not Green.

  If row-presence or tradeability trust caveat exists:
    apply additional trust cap even if the price path has a temporary MFE.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_94_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 small/regional/civil-builder PF/cash-flow cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_SMALL_CIVIL_BUILDER_PF_CASHFLOW_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks construction-theme Green without PF/cash-flow/backlog/margin/trust bridge,
   - preserves civil/regional positives only with price survival and fresh project-cash evidence,
   - caps civil-construction labels at Watch/Yellow when MFE is absent,
   - routes shallow-MFE/high-MAE small-builder late spikes to hard-4C,
   - applies extra cap when row-presence or tradeability caveats exist.

Expected next schedule:
completed_round = R10
completed_loop = 94
next_round = R11
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 94
next_round = R11
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
