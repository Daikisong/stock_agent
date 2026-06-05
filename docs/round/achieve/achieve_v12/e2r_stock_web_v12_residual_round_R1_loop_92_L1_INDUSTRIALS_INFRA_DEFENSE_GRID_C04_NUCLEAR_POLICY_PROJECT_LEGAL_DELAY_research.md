# E2R Stock-Web v12 Residual Research — R1 / Loop 92

```yaml
scheduled_round: R1
scheduled_loop: 92
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_TO_CONTRACT_EARNINGS_BRIDGE_VS_POLICY_EXPORT_HEADLINE_AND_LEGAL_DELAY

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
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 92
next_round: R2
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 92
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage already covered:

```text
loop88: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
loop89: C02_POWER_GRID_DATACENTER_CAPEX
loop90: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
loop91: C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

This run therefore selects the under-covered R1 branch:

```text
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
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
052690 한전기술
051600 한전KPS
015760 한국전력
```

These avoid the C04 top-covered symbols and avoid recent R1 loop91 C01 symbols:

```text
010620, 082740, 267270
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
052690: same archetype, new symbol, nuclear engineering policy-export local-burst / legal-delay branch
051600: same archetype, new symbol, nuclear O&M / service bridge positive-control branch
015760: same archetype, new symbol, utility parent / policy halo capped-positive branch
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
052690 한전기술
  profile: atlas/symbol_profiles/052/052690.json
  first_date: 2009-12-14
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,984
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

051600 한전KPS
  profile: atlas/symbol_profiles/051/051600.json
  first_date: 2007-12-14
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,482
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

015760 한국전력
  profile: atlas/symbol_profiles/015/015760.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,765
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-07-17 / 2024-07-18
Czech government selects Korea Hydro & Nuclear Power as preferred bidder for new Dukovany nuclear reactors.
```

Legal-delay frame:

```text
2024-10-30
Czech competition watchdog temporarily prohibits contract signing amid appeals from Westinghouse and EDF.
```

This is exactly C04:

```text
nuclear policy / export project
  -> preferred bidder or policy headline
  -> final contract not yet signed
  -> legal challenge / appeal risk
  -> project scope and listed-company share uncertain
  -> revenue and margin bridge delayed
```

The model can over-score:

```text
Korea nuclear export headline
Czech preferred bidder
nuclear policy support
nuclear engineering label
nuclear maintenance label
utility parent halo
```

The bridge must be stricter:

```text
preferred bidder
  -> final contract
  -> legal challenge cleared
  -> company-specific workshare
  -> booking / backlog recognition
  -> margin and timing
  -> price survival after headline spike
```

A preferred-bidder headline is a door opening. It is not the same as signed backlog walking through the door.

---

## 5. Case 1 — 052690 한전기술

```yaml
case_id: C04_R1L92_052690_2024_07_18
symbol: "052690"
name: "한전기술"
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_TO_CONTRACT_EARNINGS_BRIDGE_VS_POLICY_EXPORT_HEADLINE_AND_LEGAL_DELAY
trigger_date: 2024-07-17
entry_date: 2024-07-18
entry_price_basis: close
entry_price: 82000
classification: local_burst_high_mae_nuclear_engineering_policy_headline_without_final_contract_bridge
calibration_usable: true
```

### Evidence interpretation

한전기술 is the cleanest nuclear-engineering headline exposure. It reacted violently to the Czech preferred-bidder event.

However, the path shows the C04 problem clearly:

```text
nuclear export headline
  -> very large intraday spike
  -> entry close already far below high
  -> post-event MAE appears before durable contract earnings bridge
```

The stock was the correct theme stock, but the event was still preferred-bidder stage, not final contract / revenue recognition.

### Price path

Key Stock-Web rows:

```text
2024-07-17: close 76,600
2024-07-18: high 98,100 / close 82,000
2024-07-19: low 73,100 / close 73,400
2024-08-05: low 61,600 / close 63,300
2024-09-09: low 62,500 / close 65,300
2024-09-19: high 73,000 / close 72,800
2024-10-21: high 73,300 / close 72,000
```

Approximate path from entry close:

```text
entry_close: 82,000
peak_high: 98,100
MFE: +19.6%
worst_low: 61,600
MAE: -24.9%
peak_to_later_low_drawdown: -37.2%
```

### Interpretation

This is a local-burst / high-MAE counterexample:

```text
Stage2-Watch: valid.
Stage2-Actionable: only as event-trading / 4B, not durable Green.
Stage3-Green: blocked until final contract, legal challenge clearance, workshare and margin bridge.
Hard 4C: borderline, but local-burst failure is the primary classification.
```

### Stress-test components

```text
raw_component_score_proxy:
  nuclear_policy_relevance: high
  project_workshare_relevance: high
  final_contract_status: not_yet
  legal_delay_risk: high
  price_confirmation_intraday: high
  post_event_price_survival: weak
  local_4b_overlay: required
```

---

## 6. Case 2 — 051600 한전KPS

```yaml
case_id: C04_R1L92_051600_2024_07_18
symbol: "051600"
name: "한전KPS"
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_TO_CONTRACT_EARNINGS_BRIDGE_VS_POLICY_EXPORT_HEADLINE_AND_LEGAL_DELAY
trigger_date: 2024-07-17
entry_date: 2024-07-18
entry_price_basis: close
entry_price: 38900
classification: positive_capped_nuclear_om_service_bridge_with_contract_watch
calibration_usable: true
```

### Evidence interpretation

한전KPS is the positive control in this set.

The signal is not pure construction EPC. It is service / O&M / maintenance relevance around nuclear project and nuclear fleet export credibility. The price path showed better survival than 한전기술 after the headline.

But C04 still requires a cap:

```text
O&M relevance
  -> project service workshare
  -> final contract
  -> revenue timing
  -> margin bridge
```

Without that bridge, Green is premature.

### Price path

Key Stock-Web rows:

```text
2024-07-17: close 37,600
2024-07-18: high 47,450 / close 38,900
2024-07-22: high 39,900 / close 39,650
2024-08-05: low 35,850 / close 37,000
2024-08-21: high 43,500 / close 43,200
2024-09-19: high 43,650 / close 43,150
```

Approximate path from entry close:

```text
entry_close: 38,900
peak_high: 47,450
MFE: +22.0%
worst_low: 35,850
MAE: -7.8%
```

### Interpretation

This is a capped positive:

```text
Stage2-Actionable: allowed if O&M/service workshare bridge is explicit.
Stage3-Green: blocked until final contract and earnings bridge.
4B: mild watch due to event-spike high.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  nuclear_service_relevance: high
  final_contract_status: not_yet
  legal_delay_risk: medium_high
  price_survival: medium_high
  drawdown_penalty: low_to_medium
  green_cap: yes
```

---

## 7. Case 3 — 015760 한국전력

```yaml
case_id: C04_R1L92_015760_2024_07_18
symbol: "015760"
name: "한국전력"
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_TO_CONTRACT_EARNINGS_BRIDGE_VS_POLICY_EXPORT_HEADLINE_AND_LEGAL_DELAY
trigger_date: 2024-07-17
entry_date: 2024-07-18
entry_price_basis: close
entry_price: 19610
classification: watch_positive_utility_parent_policy_halo_not_direct_project_green
calibration_usable: true
```

### Evidence interpretation

한국전력 is the parent/utility halo case. It did not fail the price path. But it also should not be treated as a clean C04 Green just because the nuclear export headline was good.

The bridge is mixed:

```text
utility parent / national nuclear ecosystem
  -> policy halo and eventual earnings possibility
  -> but regulated utility economics, tariff policy, debt, and project workshare dilute the direct Czech-project bridge
```

This case prevents C04 from being too negative, but also prevents over-promotion.

### Price path

Key Stock-Web rows:

```text
2024-07-17: close 19,580
2024-07-18: high 20,400 / close 19,610
2024-08-05: low 18,190 / close 18,400
2024-08-21: high 21,200 / close 21,000
2024-08-27: high 22,850 / close 22,750
2024-09-25: low 19,840 / close 19,840
```

Approximate path from entry close:

```text
entry_close: 19,610
peak_high: 22,950
MFE: +17.0%
worst_low: 18,190
MAE: -7.2%
```

### Interpretation

This is a watch-positive / capped-positive case:

```text
Stage2-Watch: valid.
Stage2-Actionable: allowed only if policy/export project ties to earnings or debt/tariff improvement bridge.
Stage3-Green: blocked from nuclear headline alone.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  nuclear_policy_halo: high
  direct_project_workshare: weak_to_medium
  regulated_utility_financials: high_risk
  price_survival: medium_high
  green_cap: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C04 nuclear grid:

```text
052690 한전기술:
  correct nuclear-engineering theme,
  but preferred-bidder headline produced local burst and high MAE before final contract bridge.

051600 한전KPS:
  better price survival and service/O&M relevance,
  but still capped until contract/workshare/margin bridge appears.

015760 한국전력:
  utility parent policy halo can work as Watch/Yellow,
  but regulated utility economics and weak direct project workshare block Green.
```

Shared rule:

```text
C04 is not "nuclear export headline = Green."
C04 is "nuclear project headline clears legal delay, becomes final contract, maps to company-specific workshare, and converts to margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C04_R1L92_052690_2024_07_18","scheduled_round":"R1","scheduled_loop":92,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_TO_CONTRACT_EARNINGS_BRIDGE_VS_POLICY_EXPORT_HEADLINE_AND_LEGAL_DELAY","symbol":"052690","name":"한전기술","trigger_date":"2024-07-17","entry_date":"2024-07-18","entry_price":82000,"peak_high":98100,"peak_date":"2024-07-18","worst_low":61600,"worst_low_date":"2024-08-05","mfe_pct":19.6,"mae_pct":-24.9,"peak_to_later_low_drawdown_pct":-37.2,"classification":"local_burst_high_mae_nuclear_engineering_policy_headline_without_final_contract_bridge","calibration_usable":true,"evidence_family":"nuclear_engineering_preferred_bidder_headline_without_final_contract_workshare_margin_bridge","residual_error":"preferred_bidder_headline_can_overpromote_before_legal_delay_and_final_contract_clear","shadow_rule_candidate":"keep_preferred_bidder_spike_as_4b_watch_until_final_contract_workshare_margin_bridge_confirms"}
{"row_type":"case","case_id":"C04_R1L92_051600_2024_07_18","scheduled_round":"R1","scheduled_loop":92,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_TO_CONTRACT_EARNINGS_BRIDGE_VS_POLICY_EXPORT_HEADLINE_AND_LEGAL_DELAY","symbol":"051600","name":"한전KPS","trigger_date":"2024-07-17","entry_date":"2024-07-18","entry_price":38900,"peak_high":47450,"peak_date":"2024-07-18","worst_low":35850,"worst_low_date":"2024-08-05","mfe_pct":22.0,"mae_pct":-7.8,"classification":"positive_capped_nuclear_om_service_bridge_with_contract_watch","calibration_usable":true,"evidence_family":"nuclear_om_service_workshare_policy_bridge_with_price_survival","residual_error":"positive_path_still_needs_final_contract_and_service_margin_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_om_service_workshare_bridge_confirms_but_cap_green_until_contract_signed"}
{"row_type":"case","case_id":"C04_R1L92_015760_2024_07_18","scheduled_round":"R1","scheduled_loop":92,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_TO_CONTRACT_EARNINGS_BRIDGE_VS_POLICY_EXPORT_HEADLINE_AND_LEGAL_DELAY","symbol":"015760","name":"한국전력","trigger_date":"2024-07-17","entry_date":"2024-07-18","entry_price":19610,"peak_high":22950,"peak_date":"2024-08-28","worst_low":18190,"worst_low_date":"2024-08-05","mfe_pct":17.0,"mae_pct":-7.2,"classification":"watch_positive_utility_parent_policy_halo_not_direct_project_green","calibration_usable":true,"evidence_family":"utility_parent_nuclear_policy_halo_without_direct_project_workshare_margin_bridge","residual_error":"nuclear_policy_halo_can_overpromote_regulated_utility_without_direct_earnings_bridge","shadow_rule_candidate":"cap_utility_parent_nuclear_policy_halo_at_watch_yellow_until_project_and_tariff_debt_bridge_confirm"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":92,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_TO_CONTRACT_EARNINGS_BRIDGE_VS_POLICY_EXPORT_HEADLINE_AND_LEGAL_DELAY","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":92,"canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","rule_id":"C04_FINAL_CONTRACT_WORKSHARE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C04, do not open Stage2-Actionable or Stage3-Green from nuclear policy, export preferred-bidder, or national project headline alone. Require final contract or high-probability contract path, legal challenge clearance, company-specific workshare, booking/backlog recognition, revenue timing, margin bridge, and price survival. Preferred-bidder spikes with high MAE should remain local 4B/Watch. Utility-parent policy halo should cap at Watch/Yellow unless direct earnings, tariff, debt, or project workshare bridge is explicit.","expected_effect":"Reduce nuclear export headline false positives while preserving service/O&M or engineering positives when final contract, workshare, and margin bridge appear.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":92,"canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","residual_type":"nuclear_policy_project_legal_delay_bridge_guard","contribution":"Adds one nuclear service/O&M capped positive, one engineering headline local-burst failure, and one utility-parent policy-halo cap case to calibrate C04 final-contract/legal-delay/workshare rules.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C04_FINAL_CONTRACT_WORKSHARE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY:

  Do not open Stage3-Green from:
    - nuclear policy headline alone
    - preferred-bidder headline alone
    - national nuclear export headline alone
    - one-day nuclear theme spike alone
    - utility parent halo alone

  Require at least two of:
    - final contract or very high-probability contract path
    - legal challenge / appeal risk cleared or bounded
    - company-specific workshare
    - booking / backlog recognition
    - revenue timing
    - margin / OP conversion
    - low-MAE price survival after the first headline

  If MFE > 15% but MAE < -20%:
    classify as local 4B / event burst, not Green.

  If MFE > 20% and MAE remains controlled:
    allow Actionable only if workshare and service/revenue bridge is explicit.

  If the company is a regulated utility parent:
    cap at Watch/Yellow unless direct project economics, tariff, debt, or earnings bridge is explicit.

  If legal challenge prevents final signing:
    block Green and require revalidation after the legal milestone.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C04 nuclear-policy/project-delay cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C04_FINAL_CONTRACT_WORKSHARE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C04 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C04 cases agree, consider implementing a canonical guard that:
   - blocks preferred-bidder nuclear-policy Green without final contract, legal clearance, and workshare bridge,
   - preserves service/O&M positives only when price survival and earnings bridge confirm,
   - caps utility-parent policy halo at Watch/Yellow,
   - routes high-MFE/high-MAE engineering headline spikes to local 4B/event-burst instead of Green.

Expected next schedule:
completed_round = R1
completed_loop = 92
next_round = R2
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 92
next_round = R2
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
