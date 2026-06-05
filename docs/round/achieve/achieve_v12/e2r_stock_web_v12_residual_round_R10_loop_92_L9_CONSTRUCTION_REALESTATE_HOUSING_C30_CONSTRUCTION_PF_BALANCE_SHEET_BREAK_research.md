# E2R Stock-Web v12 Residual Research — R10 / Loop 92

```yaml
scheduled_round: R10
scheduled_loop: 92
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA

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
accounting_or_listing_trust_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 92
next_round: R11
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 92
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is a hard L9 construction / real-estate / housing round. The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

The selected fine branch is:

```text
PF workout / parent support / regional-builder balance-sheet trust bridge
vs policy relief beta
```

This deliberately avoids the previous R10 loop91 branch, which focused on small-builder policy relief and political construction beta.

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
loop91: 013360, 001470, 002410
```

Selected symbols:

```text
034300 신세계건설
009410 태영건설
002460 HS화성 / 화성산업
```

They avoid the C30 top-covered symbols and the recent R10 loop88~91 symbols.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
034300: same archetype, new symbol, parent-support / balance-sheet trust repair positive with later listing-trust caveat
009410: same archetype, new symbol, PF workout / trading halt / balance-sheet trust hard-4C branch
002460: same archetype, new symbol, regional-builder policy relief label without sufficient repair bridge
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
034300 신세계건설
  profile: atlas/symbol_profiles/034/034300.json
  first_date: 1999-06-25
  raw_last_date: 2025-02-21
  tradable last_date: 2025-01-24
  tradable_ohlcv rows: 6,312
  market history:
    KOSDAQ 1999-06-25~2002-06-14
    KOSPI 2002-06-17~2025-02-21
  corporate_action_candidate_dates:
    1999-11-16, 2024-02-06
  2024 selected entry after the 2024-02-06 candidate: entry~D+180 direct contamination avoided
  caveat:
    later inactive_or_delisted_like row-presence signal exists; use listing/trust cap

009410 태영건설
  profile: atlas/symbol_profiles/009/009410.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,576
  non_tradable_zero_volume rows: 189
  corporate_action_candidate_dates:
    2007-05-03, 2020-09-22, 2024-10-31
  2024 selected entry~D+180 avoids the 2024-10-31 corporate-action candidate, but trading-halt / row-gap caveat is central evidence
  caveat:
    2024 row gap between 2024-03-13 and 2024-10-31 implies tradeability/trust risk

002460 HS화성 / 화성산업
  profile: atlas/symbol_profiles/002/002460.json
  name history:
    화성산업 until 2024-07-09
    HS화성 from 2024-07-10
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,764
  corporate_action_candidate_dates:
    1996-01-03, 1997-12-17, 2002-02-08
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C30 is not a generic construction-policy relief trade.

The model can over-score:

```text
PF support headline
builder liquidity support
parent-company support
regional housing exposure
workout headline
relief rally
low-price construction beta
```

The C30 bridge is narrower:

```text
PF exposure
  -> refinancing / workout clarity
  -> parent or lender support quality
  -> project cash collection
  -> debt maturity extension
  -> order backlog and margin
  -> accounting / listing trust
  -> post-trigger price survival
```

A PF rescue headline is emergency scaffolding. It may keep the building standing, but equity value only returns when the cracked beams, cash leaks, and trust gaps are actually repaired.

---

## 5. Case 1 — 034300 신세계건설

```yaml
case_id: C30_R10L92_034300_2024_02_07
symbol: "034300"
name: "신세계건설"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA
trigger_date: 2024-02-06
entry_date: 2024-02-07
entry_price_basis: close
entry_price: 11460
classification: positive_local_parent_support_balance_sheet_repair_with_listing_trust_cap
calibration_usable: true
```

### Evidence interpretation

신세계건설 is the positive-control case, but only with a trust cap.

The useful C30 bridge is:

```text
parent / sponsor support
  -> balance-sheet repair expectation
  -> PF liquidity stress compression
  -> later tender / controlled exit or support perception
  -> price confirmation
```

The path produced a large MFE after the February support-related reset. However, this is not a clean Green because the profile later shows inactive_or_delisted_like row-presence inference and the 2024 price path includes a post-support capital-structure caveat.

### Price path

Key Stock-Web rows:

```text
2024-02-06: corporate-action candidate / share-count change area in profile
2024-02-07: close 11,460
2024-04-16: low 9,980 / close 10,090
2024-05-28: high 13,980 / close 12,310
2024-05-30: high 18,650 / close 14,700
2024-07-01: high 16,990 / close 14,000
2024-08-05: low 11,150 / close 11,420
2024-09-30: high 18,340 / close 18,160
```

Approximate path from entry close:

```text
entry_close: 11,460
peak_high: 18,650
MFE: +62.7%
worst_low_after_entry: 9,850 on 2024-04-26
MAE: -14.0%
later row/status caveat: present after research window
```

### Interpretation

This is a local positive, not an unrestricted Green:

```text
Stage2-Actionable: allowed only if parent-support / debt-repair bridge is explicit.
Stage3-Green: blocked by listing/trust/capital-structure caveat until confirmed.
Local 4B: required after +60% MFE.
Hard 4C: no for the original entry, but post-spike re-entry without support terms is unsafe.
```

### Stress-test components

```text
raw_component_score_proxy:
  parent_support_signal: high
  pf_repair_bridge: medium_high
  accounting_listing_trust_caveat: high
  price_confirmation: very_high
  drawdown_penalty: medium
  local_4b_overlay: required
  green_cap: yes
```

---

## 6. Case 2 — 009410 태영건설

```yaml
case_id: C30_R10L92_009410_2024_01_11
symbol: "009410"
name: "태영건설"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA
trigger_date: 2024-01-11
entry_date: 2024-01-11
entry_price_basis: close
entry_price: 3765
classification: hard_4c_candidate_pf_workout_relief_spike_with_trading_halt_and_trust_gap
calibration_usable: true
```

### Evidence interpretation

태영건설 is the hard guardrail case.

It had the strongest headline relevance to the PF stress / workout / relief frame. That is exactly why it is dangerous for the model. If C30 is allowed to promote:

```text
PF workout attention
  -> liquidity support hope
  -> relief rally
```

without actual equity-value repair, the forward path becomes a hard false positive.

The path showed:

```text
short relief spike
large immediate drawdown
row-gap / tradeability caveat
later 2024 corporate-action candidate
```

### Price path

Key Stock-Web rows:

```text
2024-01-11: high 4,110 / close 3,765
2024-01-12: high 4,035 / close 3,050
2024-01-25: low 2,180 / close 2,200
2024-02-26: high 2,965 / close 2,525
2024-03-13: close 2,310
2024-10-31: next visible 2024 tradable row after long gap; corporate-action candidate area
```

Approximate path from entry close, pre-October corporate-action window:

```text
entry_close: 3,765
peak_high: 4,110
MFE: +9.2%
worst_low_before_long_gap: 2,180
MAE: -42.1%
tradeability/trust caveat: severe
```

### Interpretation

This is a hard C30 false-positive:

```text
Stage2-Watch: possible only as crisis monitoring.
Stage2-Actionable: blocked.
Stage3-Green: blocked.
Hard 4C: yes.
```

The key lesson:

```text
PF workout attention is not balance-sheet repair.
Relief volume is not equity trust.
```

### Stress-test components

```text
raw_component_score_proxy:
  pf_stress_relevance: very_high
  workout_relief_headline: high
  actual_equity_repair_bridge: weak
  tradeability_trust_penalty: extreme
  price_confirmation: failed
  drawdown_penalty: high
  hard_4c_guard: required
```

---

## 7. Case 3 — 002460 HS화성 / 화성산업

```yaml
case_id: C30_R10L92_002460_2024_01_29
symbol: "002460"
name_at_trigger: "화성산업"
current_or_latest_name: "HS화성"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA
trigger_date: 2024-01-29
entry_date: 2024-01-29
entry_price_basis: close
entry_price: 10500
classification: watch_cap_regional_builder_policy_relief_without_strong_pf_repair_bridge
calibration_usable: true
```

### Evidence interpretation

HS화성 / 화성산업 is the regional-builder cap case.

It did not show the catastrophic trust failure of 태영건설. It also did not show the strong repair-led rerating of 신세계건설. The price path was mostly a slow drift after a modest early MFE.

The model risk is over-certainty:

```text
regional builder
  -> PF policy support
  -> low-PBR / housing recovery hope
  -> model opens Actionable
  -> no strong PF repair or margin bridge
  -> drawdown accumulates
```

### Price path

Key Stock-Web rows:

```text
2024-01-29: close 10,500
2024-02-05: high 11,170 / close 11,170
2024-02-19: high 11,230 / close 11,170
2024-03-21: low 9,880 / close 9,900
2024-08-05: low 8,760 / close 8,980
2024-09-25: low 8,470 / close 8,470
2024-10-08: high 9,250 / close 9,100
```

Approximate path from entry close:

```text
entry_close: 10,500
peak_high: 11,230
MFE: +7.0%
worst_low: 8,470
MAE: -19.3%
```

### Interpretation

This is a Watch / Yellow cap case:

```text
Stage2-Watch: valid.
Stage2-Actionable: blocked unless project-level PF repair or profitable backlog bridge is explicit.
Stage3-Green: blocked.
Hard 4C: not extreme, but false-positive guard applies.
```

This case protects the model from promoting every stable regional builder merely because the sector received policy attention.

### Stress-test components

```text
raw_component_score_proxy:
  regional_builder_relevance: medium_high
  pf_policy_relief_signal: medium
  company_specific_repair_bridge: weak
  backlog_margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
accounting_or_listing_trust_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C30 grid:

```text
034300 신세계건설:
  parent-support / repair-perception positive,
  but local 4B and listing/trust cap required.

009410 태영건설:
  PF workout relief spike failed badly.
  Low MFE, high MAE, row-gap and trust caveat; hard 4C.

002460 HS화성 / 화성산업:
  regional-builder policy relief cap case.
  Shallow MFE and medium MAE without repair bridge.
```

Shared rule:

```text
C30 is not "construction policy support exists."
C30 is "this builder's PF exposure, liquidity, project cash flow, and trust problem are repaired enough to support equity value."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L92_034300_2024_02_07","scheduled_round":"R10","scheduled_loop":92,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA","symbol":"034300","name":"신세계건설","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":11460,"peak_high":18650,"peak_date":"2024-05-30","worst_low_after_entry":9850,"worst_low_after_entry_date":"2024-04-26","mfe_pct":62.7,"mae_pct":-14.0,"classification":"positive_local_parent_support_balance_sheet_repair_with_listing_trust_cap","calibration_usable":true,"evidence_family":"parent_support_pf_liquidity_repair_with_later_listing_trust_caveat","residual_error":"positive_repair_path_requires_4b_and_trust_cap_not_green","shadow_rule_candidate":"allow_local_actionable_if_parent_support_terms_confirm_but_cap_green_for_listing_trust_caveat"}
{"row_type":"case","case_id":"C30_R10L92_009410_2024_01_11","scheduled_round":"R10","scheduled_loop":92,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA","symbol":"009410","name":"태영건설","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":3765,"peak_high":4110,"peak_date":"2024-01-11","worst_low_before_long_gap":2180,"worst_low_before_long_gap_date":"2024-01-25","mfe_pct":9.2,"mae_pct":-42.1,"classification":"hard_4c_candidate_pf_workout_relief_spike_with_trading_halt_and_trust_gap","calibration_usable":true,"evidence_family":"pf_workout_relief_headline_without_equity_repair_tradeability_trust_gap","residual_error":"pf_workout_attention_can_overpromote_without_balance_sheet_repair","shadow_rule_candidate":"route_pf_workout_relief_spike_to_hard_4c_if_mfe_shallow_mae_large_and_row_gap_or_trust_caveat_exists"}
{"row_type":"case","case_id":"C30_R10L92_002460_2024_01_29","scheduled_round":"R10","scheduled_loop":92,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA","symbol":"002460","name_at_trigger":"화성산업","current_or_latest_name":"HS화성","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":10500,"peak_high":11230,"peak_date":"2024-02-19","worst_low":8470,"worst_low_date":"2024-09-25","mfe_pct":7.0,"mae_pct":-19.3,"classification":"watch_cap_regional_builder_policy_relief_without_strong_pf_repair_bridge","calibration_usable":true,"evidence_family":"regional_builder_policy_relief_without_company_specific_pf_repair_or_margin_bridge","residual_error":"stable_regional_builder_label_can_overpromote_to_actionable_without_repair_evidence","shadow_rule_candidate":"cap_regional_builder_policy_relief_at_watch_yellow_if_mfe_shallow_and_pf_repair_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":92,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"accounting_or_listing_trust_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":92,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_PF_REPAIR_PARENT_SUPPORT_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30, do not open Stage2-Actionable or Stage3-Green from PF policy relief, builder liquidity support, parent-support headline, workout attention, or regional-builder label alone. Require company-specific PF exposure reduction, refinancing/workout terms, parent or lender support quality, project cash collection, debt maturity extension, profitable backlog, margin/OP/FCF conversion, and accounting/listing/tradeability trust. Parent-support positives with large MFE but later listing/trust caveat should remain local positives with 4B cap, not Green. PF-workout relief spikes with shallow MFE, high MAE, row gap, or tradeability caveat should route to hard-4C. Regional-builder relief cases with shallow MFE should cap at Watch/Yellow unless repair bridge is explicit.","expected_effect":"Reduce PF policy and workout false positives while preserving rare parent-support repair positives with explicit trust and balance-sheet evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":92,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"pf_repair_parent_support_regional_builder_trust_guard","contribution":"Adds one parent-support local positive with listing/trust cap, one PF-workout hard-4C, and one regional-builder Watch cap to calibrate C30 balance-sheet repair and trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_PF_REPAIR_PARENT_SUPPORT_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK:

  Do not open Stage3-Green from:
    - PF policy support headline alone
    - builder liquidity support headline alone
    - parent-support headline alone
    - workout attention alone
    - regional-builder or housing-recovery label alone
    - one-week relief rally alone

  Require at least two of:
    - company-specific PF exposure reduction
    - project-level refinancing / workout terms
    - parent or lender support quality
    - debt maturity extension
    - cash collection / receivables repair
    - profitable backlog / margin bridge
    - OP/FCF conversion
    - accounting / listing / tradeability trust
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -30%:
    route to C30 hard-4C candidate.

  If MFE > 50% but listing/trust caveat exists:
    preserve as local positive only and attach 4B cap; block Green.

  If regional-builder case has MFE < 10% and no explicit PF repair bridge:
    cap at Watch/Yellow.

  If row gap, trading halt, corporate-action caveat, or inactive/listing-trust signal appears:
    apply trust penalty even when raw OHLC is technically available.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_92_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 PF/workout/parent-support/regional-builder cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_PF_REPAIR_PARENT_SUPPORT_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks PF policy/workout Green without company-specific repair and trust bridge,
   - preserves parent-support positives only as capped local positives when listing/trust caveats exist,
   - routes shallow-MFE/high-MAE workout cases with row gaps to hard-4C,
   - caps regional-builder relief cases at Watch/Yellow without PF/cash-flow repair evidence.

Expected next schedule:
completed_round = R10
completed_loop = 92
next_round = R11
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 92
next_round = R11
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
