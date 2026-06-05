# E2R Stock-Web v12 Residual Research — R1 / Loop 95

```yaml
scheduled_round: R1
scheduled_loop: 95
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: LAND_SYSTEMS_DEFENSE_ELECTRONICS_RUGGED_COMPUTING_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE

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
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 95
next_round: R2
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_94_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12, after R13 closes, the next round is:

```text
scheduled_round = R1
scheduled_loop = previous_loop + 1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 95
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 hard gate requires:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage:

```text
loop91: C01_ORDER_BACKLOG_MARGIN_BRIDGE
loop92: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
loop93: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
loop94: C02_POWER_GRID_DATACENTER_CAPEX
```

This run selects:

```text
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

The selected fine branch is:

```text
land systems / defense electronics / rugged computing
export framework, order backlog, delivery, and margin bridge
vs generic defense-theme late chase
```

This deliberately avoids the loop94 C02 grid-CAPEX branch and returns R1 to defense/export backlog without reusing the top-covered C03 names.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rows: 21
symbols: 12
date_range: 2022-07-28~2024-09-20
good/bad S2: 11/3
4B/4C: 0/0
URL pending/proxy: 7/7
top covered symbols:
  079550(4), 047810(3), 065450(3), 005870(2), 103140(2), 003570(1)
```

Selected symbols:

```text
064350 현대로템
272210 한화시스템
448710 코츠테크놀로지
```

They avoid the C03 top-covered symbols and avoid the most recent R1 loop94 C02 names:

```text
loop94 avoid: 103590, 199820, 237750
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
064350: same archetype, new symbol, land-systems export/backlog positive with post-rerating 4B watch
272210: same archetype, new symbol, defense-electronics late-chase Watch cap without fresh order/margin bridge
448710: same archetype, new symbol, rugged defense computing theme spike hard-4C without backlog/delivery survival
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
064350 현대로템
  profile: atlas/symbol_profiles/064/064350.json
  first_date: 2013-10-30
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,021
  corporate_action_candidate_dates:
    2020-08-14
  2024 entry~D+180 contamination: none

272210 한화시스템
  profile: atlas/symbol_profiles/272/272210.json
  first_date: 2019-11-13
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,539
  corporate_action_candidate_dates:
    2021-06-23
  2024 entry~D+180 contamination: none

448710 코츠테크놀로지
  profile: atlas/symbol_profiles/448/448710.json
  first_date: 2023-08-10
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 613
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C03 is about defense export frameworks, order backlog, delivery conversion, and margin. It is not a generic "defense stock" or "geopolitical tension" archetype.

The model can over-score:

```text
defense export headline
geopolitical tension
land-system / missile / radar / rugged computer label
NATO / Poland / Middle East readthrough
one-week defense-stock volume spike
late chase after a defense rerating
```

The C03 bridge must be stricter:

```text
defense export / framework event
  -> named customer or country
  -> signed contract / framework agreement / order conversion
  -> backlog visibility
  -> production capacity and delivery schedule
  -> FX, warranty, localization, and working-capital risk
  -> margin / OP conversion
  -> price survival after the first defense-theme spike
```

A defense export thesis is like a military convoy order. The headline says vehicles may be needed, but C03 asks whether this company has the signed route, production slot, delivery date, and enough margin after localization and warranty cost.

---

## 5. Case 1 — 064350 현대로템

```yaml
case_id: C03_R1L95_064350_2024_02_22
symbol: "064350"
name: "현대로템"
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: LAND_SYSTEMS_DEFENSE_ELECTRONICS_RUGGED_COMPUTING_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE
trigger_date: 2024-02-22
entry_date: 2024-02-22
entry_price_basis: close
entry_price: 34500
classification: positive_land_systems_export_backlog_delivery_margin_bridge_with_4b_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

현대로템 is the constructive C03 control.

The useful C03 read is not simply:

```text
방산주가 강하다
```

It is:

```text
land systems / armored platform export relevance
  -> defense export framework and backlog visibility
  -> delivery and production-capacity bridge
  -> strong price confirmation
  -> later price survival
```

The forward path was strongly aligned with the C03 thesis. However, after a large rerating, the model should attach local 4B unless fresh order conversion, delivery, and margin evidence refresh the thesis.

### Price path

Key Stock-Web rows:

```text
2024-02-22: high 34,500 / close 34,500
2024-03-12: low 29,900 / close 30,000
2024-03-29: high 38,800 / close 36,800
2024-04-09: high 41,850 / close 41,150
2024-07-24: high 48,300 / close 47,950
2024-08-14: high 54,800 / close 54,600
2024-09-20: high 57,100 / close 56,100
2024-10-17: high 67,500 / close 67,100
2024-10-18: high 68,000 / close 65,000
```

Approximate path from entry close:

```text
entry_close: 34,500
peak_high: 68,000
MFE: +97.1%
worst_low_after_entry: 29,900
MAE: -13.3%
```

### Interpretation

This is a C03 positive with 4B after rerating:

```text
Stage2-Actionable: valid if named export/customer, backlog, and delivery bridge are explicit.
Stage3-Green: possible only with order conversion, production capacity, and OP/margin evidence.
Local 4B: required after near-doubling MFE unless fresh backlog/delivery evidence appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  defense_export_relevance: very_high
  land_systems_backlog_bridge: high
  order_delivery_visibility: high
  margin_fx_warranty_bridge: medium
  price_confirmation: very_high
  drawdown_penalty: medium
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 272210 한화시스템

```yaml
case_id: C03_R1L95_272210_2024_07_24
symbol: "272210"
name: "한화시스템"
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: LAND_SYSTEMS_DEFENSE_ELECTRONICS_RUGGED_COMPUTING_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 22250
classification: watch_cap_defense_electronics_late_chase_without_fresh_order_margin_bridge
calibration_usable: true
```

### Evidence interpretation

한화시스템 is the defense-electronics late-chase Watch cap.

The label is very plausible:

```text
defense electronics / radar / system integration
  -> export and defense framework readthrough
  -> sector momentum after a prior rerating
```

But from the selected late entry, MFE was shallow and later drawdown was material. The issue is not that the company lacks defense relevance; the issue is that C03 should not keep opening Actionable/Green from a late sector label without fresh order, delivery, and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 22,750 / close 22,250
2024-07-30: high 23,400 / close 20,500
2024-08-05: low 17,090 / close 18,270
2024-09-09: low 16,530 / close 16,890
2024-10-22: high 19,300 / close 19,300
2024-10-29: high 19,800 / close 19,320
```

Approximate path from entry close:

```text
entry_close: 22,250
peak_high_after_entry: 23,400
MFE: +5.2%
worst_low_after_entry: 16,530
MAE: -25.7%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from defense-electronics and systems relevance.
Stage2-Actionable: blocked unless fresh order conversion, delivery schedule, and margin bridge are explicit.
Stage3-Green: blocked from the selected late entry.
Hard 4C: not primary, but shallow MFE and high MAE make it a strong false-positive guard.
```

The lesson is that defense-electronics quality is not the same as fresh backlog monetization after a sector rerating.

### Stress-test components

```text
raw_component_score_proxy:
  defense_electronics_relevance: high
  export_framework_readthrough: medium_high
  fresh_order_conversion_bridge: weak
  delivery_margin_bridge: weak_to_medium
  price_confirmation_after_entry: shallow
  drawdown_penalty: high
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 448710 코츠테크놀로지

```yaml
case_id: C03_R1L95_448710_2024_04_09
symbol: "448710"
name: "코츠테크놀로지"
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: LAND_SYSTEMS_DEFENSE_ELECTRONICS_RUGGED_COMPUTING_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE
trigger_date: 2024-04-09
entry_date: 2024-04-09
entry_price_basis: close
entry_price: 28700
classification: hard_4c_candidate_rugged_defense_computing_theme_spike_without_backlog_delivery_survival
calibration_usable: true
```

### Evidence interpretation

코츠테크놀로지 is the hard C03 guardrail.

The setup looked attractive:

```text
rugged defense computer / embedded board label
defense electronics supply-chain sympathy
one-day high-volume defense-component spike
```

But the forward price path did not validate order conversion or delivery-margin survival. From the selected close, MFE was shallow while the later downside was severe. This is exactly the kind of "small defense component label" that should be hard-4C unless backlog and margin bridge are current.

### Price path

Key Stock-Web rows:

```text
2024-04-09: high 29,750 / close 28,700
2024-04-17: low 24,250 / close 24,450
2024-08-05: low 17,650 / close 19,030
2024-09-09: low 15,760 / close 16,660
2024-10-23: high 25,400 / close 22,150
2024-11-04: low 20,550 / close 20,800
```

Approximate path from entry close:

```text
entry_close: 28,700
peak_high_after_entry: 29,750
MFE: +3.7%
worst_low_after_entry: 15,760
MAE: -45.1%
```

### Interpretation

This is a hard C03 false-positive:

```text
Stage2-Watch: possible from rugged defense computing and defense-electronics relevance.
Stage2-Actionable: blocked unless customer/order/backlog/delivery bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that defense-component adjacency is not export backlog.

### Stress-test components

```text
raw_component_score_proxy:
  rugged_defense_computing_label: high
  defense_electronics_sympathy: high
  named_customer_order_bridge: weak
  backlog_delivery_bridge: weak
  margin_bridge: weak
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
calibration_usable_trigger_count: 3
```

The three-case C03 defense export grid:

```text
064350 현대로템:
  land-systems export/backlog positive;
  strong MFE and price survival, but 4B required after large rerating.

272210 한화시스템:
  defense-electronics late chase;
  shallow MFE and material MAE, Watch/Yellow cap without fresh order/margin bridge.

448710 코츠테크놀로지:
  rugged defense-computing theme spike failed;
  shallow MFE and severe MAE, hard 4C.
```

Shared rule:

```text
C03 is not "defense label is hot."
C03 is "customer, contract, framework conversion, backlog, delivery, capacity, and margin are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C03_R1L95_064350_2024_02_22","scheduled_round":"R1","scheduled_loop":95,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"LAND_SYSTEMS_DEFENSE_ELECTRONICS_RUGGED_COMPUTING_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE","symbol":"064350","name":"현대로템","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":34500,"peak_high":68000,"peak_date":"2024-10-18","worst_low_after_entry":29900,"worst_low_after_entry_date":"2024-03-12","mfe_pct":97.1,"mae_pct":-13.3,"classification":"positive_land_systems_export_backlog_delivery_margin_bridge_with_4b_after_large_mfe","calibration_usable":true,"evidence_family":"land_systems_defense_export_framework_backlog_delivery_margin_bridge","residual_error":"positive_defense_export_path_requires_4b_after_large_mfe_without_fresh_backlog_delivery_margin_evidence","shadow_rule_candidate":"preserve_positive_when_export_backlog_and_delivery_bridge_confirm_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C03_R1L95_272210_2024_07_24","scheduled_round":"R1","scheduled_loop":95,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"LAND_SYSTEMS_DEFENSE_ELECTRONICS_RUGGED_COMPUTING_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE","symbol":"272210","name":"한화시스템","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":22250,"peak_high":23400,"peak_date":"2024-07-30","worst_low_after_entry":16530,"worst_low_after_entry_date":"2024-09-09","mfe_pct":5.2,"mae_pct":-25.7,"classification":"watch_cap_defense_electronics_late_chase_without_fresh_order_margin_bridge","calibration_usable":true,"evidence_family":"defense_electronics_systems_late_chase_without_fresh_order_delivery_margin_bridge","residual_error":"defense_electronics_quality_can_overpromote_without_current_order_conversion_and_margin_bridge","shadow_rule_candidate":"cap_defense_electronics_late_chase_at_watch_yellow_if_mfe_shallow_and_fresh_backlog_bridge_missing"}
{"row_type":"case","case_id":"C03_R1L95_448710_2024_04_09","scheduled_round":"R1","scheduled_loop":95,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"LAND_SYSTEMS_DEFENSE_ELECTRONICS_RUGGED_COMPUTING_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE","symbol":"448710","name":"코츠테크놀로지","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":28700,"peak_high":29750,"peak_date":"2024-04-09","worst_low_after_entry":15760,"worst_low_after_entry_date":"2024-09-09","mfe_pct":3.7,"mae_pct":-45.1,"classification":"hard_4c_candidate_rugged_defense_computing_theme_spike_without_backlog_delivery_survival","calibration_usable":true,"evidence_family":"rugged_defense_computing_theme_spike_without_named_customer_backlog_delivery_margin_bridge","residual_error":"small_defense_component_label_can_fail_when_order_backlog_delivery_margin_bridge_missing","shadow_rule_candidate":"route_rugged_defense_computing_theme_spike_to_hard_4c_if_mfe_shallow_mae_large_and_backlog_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":95,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"LAND_SYSTEMS_DEFENSE_ELECTRONICS_RUGGED_COMPUTING_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_LATE_CHASE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":95,"canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","rule_id":"C03_DEFENSE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C03, do not open Stage2-Actionable or Stage3-Green from defense export, geopolitical tension, land-system, defense-electronics, rugged-computing, NATO/Poland/Middle-East readthrough, or one-week defense-stock volume spike labels alone. Require named customer/country, signed contract or framework conversion, backlog visibility, production capacity and delivery schedule, FX/warranty/localization/working-capital risk check, margin/OP conversion, and post-trigger price survival. Land-systems positives with large MFE should attach local 4B unless fresh backlog/delivery/margin evidence appears. Defense-electronics late chases with shallow MFE and material MAE should cap at Watch/Yellow without fresh order conversion. Small defense-computing/component spikes with shallow MFE and high MAE should route to hard-4C when named-customer backlog and delivery bridge are missing.","expected_effect":"Preserve true defense export/backlog positives while reducing generic defense-theme and component-label false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":95,"canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","residual_type":"defense_export_backlog_delivery_margin_guard","contribution":"Adds one land-systems export/backlog positive with 4B-after-large-MFE, one defense-electronics late-chase Watch cap, and one rugged defense-computing hard-4C counterexample to calibrate C03 named-customer, backlog, delivery, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C03_DEFENSE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG:

  Do not open Stage3-Green from:
    - defense export headline alone
    - geopolitical tension label alone
    - land-system / missile / radar / rugged computer label alone
    - NATO / Poland / Middle East readthrough alone
    - one-week defense-stock volume spike alone

  Require at least two of:
    - named customer or country
    - signed contract / framework agreement / order conversion
    - backlog visibility
    - production capacity and delivery schedule
    - FX / warranty / localization / working-capital risk containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the defense-export headline

  If MFE < 10% and MAE < -35%:
    route to C03 hard-4C candidate.

  If MFE is shallow and MAE is material:
    cap at Watch/Yellow unless fresh order conversion is explicit.

  If MFE > 50%:
    preserve positive classification but attach local 4B unless backlog/delivery/margin evidence refreshes the thesis.

  Distinguish:
    - prime land-systems names where framework converts into signed backlog and delivery
    - from defense-electronics/component labels where theme heat does not reach orders or margin.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C03 defense export/backlog cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C03_DEFENSE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C03 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C03 cases agree, consider implementing a canonical guard that:
   - blocks defense-theme Green without named customer, contract/framework conversion, backlog, delivery, and margin bridge,
   - preserves prime land-systems positives only with price survival and fresh order evidence,
   - attaches local 4B after large MFE,
   - caps defense-electronics late chases at Watch/Yellow without fresh order conversion,
   - routes shallow-MFE/high-MAE defense-computing/component spikes to hard-4C.

Expected next schedule:
completed_round = R1
completed_loop = 95
next_round = R2
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 95
next_round = R2
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
