# E2R Stock-Web v12 Residual Research — R4 / loop 90 / C16 Strategic Resource Policy Supply

```text
scheduled_round: R4
scheduled_loop: 90
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: EAST_SEA_GAS_FIELD_POLICY_EXPLORATION_TO_RESERVE_CASHFLOW_BRIDGE

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year

production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Why this case set exists

R4 loop88 already handled `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`, and R4 loop89 handled `C15_MATERIAL_SPREAD_SUPERCYCLE`.  
This run therefore moves to the remaining R4 resource-policy branch:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

The residual question is narrow:

> When a national resource policy headline appears, does E2R over-promote policy/resource label sympathy into Stage2-Actionable or Stage3-Green before there is company-specific reserve, drilling, ownership, offtake, or cashflow evidence?

The selected trigger family is Korea's June 2024 East Sea oil/gas exploration headline.  
The policy event was real, but the market reaction split into two very different paths:

1. a relatively direct gas/public-utility proxy that maintained a stronger path after the headline, and
2. petroleum/oil-distributor sympathy names that made fast local spikes and then faded hard.

This is a clean C16 residual because it separates **resource policy existence** from **shareholder-economics conversion**.

---

## 2. No-repeat / novelty check

No-Repeat Index snapshot used:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:
rows = 36
symbols = 23
date range = 2022-10-20~2024-10-11
good/bad S2 = 14/9
4B/4C = 2/0
URL pending/proxy = 17/17
top covered symbols = 047400(6), 005490(3), 012320(3), 001570(2), 081150(2), 101670(2)
```

This run avoids the C16 top-covered symbols and uses three new C16 symbols:

```text
036460 한국가스공사
004090 한국석유
024060 흥구석유
```

Hard duplicate key avoided:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All three rows use a new C16 trigger family:

```text
east_sea_oil_gas_policy_exploration_headline
trigger_date = 2024-06-03
```

---

## 3. Stock-Web atlas validation

Manifest basis:

```text
atlas_version: 1.0.0
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
inactive_or_delisted_like_symbol_count: 2,546
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile contamination check:

```text
036460 한국가스공사:
  corporate_action_candidate_count = 0
  calibration_caveat = none

004090 한국석유:
  corporate_action_candidate_dates = 1997-08-07, 2021-04-15, 2021-05-07
  2024 trigger window not blocked

024060 흥구석유:
  corporate_action_candidate_dates = 1997-09-11, 1998-04-08, 1998-08-24, 2008-08-26, 2008-10-06, 2008-10-24
  2024 trigger window not blocked
```

---

## 4. Historical trigger event

```text
trigger_date: 2024-06-03
trigger_family: East Sea oil/gas exploration policy headline
policy_context:
  - South Korean President Yoon approved exploratory drilling for potential offshore oil/gas prospects near Pohang.
  - Public headline estimate cited up to 14 billion barrels of oil and gas.
  - The event was a policy/exploration authorization, not a proven reserve or company-specific production cashflow event.
  - Publicly discussed drilling success probability was about 20%, meaning the event carried high geological uncertainty.
```

C16 interpretation:

```text
The policy headline is valid evidence for C16 Watch/Stage2 interest.
It is not sufficient evidence for Stage3-Green unless company-level exposure is explicit:
  - upstream project equity or operator economics,
  - named drilling/service contract scope,
  - reserve confirmation,
  - offtake/equipment/service conversion,
  - regulated earnings bridge,
  - or credible cashflow timing.
```

---

## 5. Case table

| ticker | name | entry date | entry close | peak high / date | MFE | trough low / date | MAE | classification |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 036460 | 한국가스공사 | 2024-06-04 | 39,400 | 64,500 / 2024-06-20 | +63.71% | 37,750 / 2024-11-01 | -4.19% | positive with local 4B watch |
| 004090 | 한국석유 | 2024-06-04 | 23,300 | 28,100 / 2024-06-05 | +20.60% | 15,540 / 2024-07-25 | -33.30% | counterexample / price-only sympathy |
| 024060 | 흥구석유 | 2024-06-04 | 19,240 | 21,400 / 2024-08-05 | +11.23% | 12,690 / 2024-07-25 | -34.04% | hard 4C candidate |

---

## 6. Case notes

### 6.1 036460 한국가스공사 — positive, but not unguarded Green

Stock-Web rows show the policy event immediately repriced 한국가스공사:

```text
2024-06-03: o 29,800 / h 38,700 / l 29,700 / c 38,700
2024-06-04: o 40,800 / h 49,350 / l 38,750 / c 39,400
2024-06-20: o 59,200 / h 64,500 / l 56,500 / c 63,500
```

The clean forward path:

```text
entry_close = 39,400
peak_high = 64,500
MFE = +63.71%
late 2024 low observed in checked window = 37,750
MAE = -4.19%
```

This is a usable positive C16 row because 한국가스공사 is not just a generic petroleum label. It has a gas-policy and public energy-infrastructure connection that can plausibly attract resource-policy capital.  
Still, the event itself was exploration authorization, not proven reserve monetization. So the correct treatment is:

```text
Stage2-Actionable: possible
Stage3-Yellow: possible when volume + policy confirmation + direct public gas proxy evidence align
Stage3-Green: require reserve/drilling/cashflow bridge or strong post-trigger non-price evidence
4B overlay: required after the fast +60% move unless non-price evidence catches up
```

### 6.2 004090 한국석유 — local spike, then high-MAE counterexample

Stock-Web rows:

```text
2024-06-03: o 13,890 / h 17,950 / l 13,850 / c 17,950
2024-06-04: o 21,650 / h 23,300 / l 21,500 / c 23,300
2024-06-05: o 23,650 / h 28,100 / l 21,600 / c 23,300
2024-07-25: o 16,140 / h 16,600 / l 15,540 / c 15,660
```

Forward result:

```text
entry_close = 23,300
peak_high = 28,100
MFE = +20.60%
trough_low = 15,540
MAE = -33.30%
```

This is the classic C16 false-positive shape:

```text
policy headline exists
ticker has oil/petroleum label
price jumps immediately
but company-specific reserve/cashflow path is absent
local spike fades into deep drawdown
```

Calibration implication:

```text
Do not give Stage3-Green to petroleum-label sympathy without a project economics bridge.
If the case reaches only local +20% MFE and later -30% MAE, classify as local 4B / Stage2 false positive.
```

### 6.3 024060 흥구석유 — hard 4C candidate

Stock-Web rows:

```text
2024-06-03: o 12,510 / h 16,250 / l 12,510 / c 16,250
2024-06-04: o 17,520 / h 20,950 / l 17,510 / c 19,240
2024-07-25: o 13,000 / h 13,230 / l 12,690 / c 12,700
2024-08-05: o 19,680 / h 21,400 / l 18,040 / c 19,560
```

Forward result:

```text
entry_close = 19,240
peak_high = 21,400
MFE = +11.23%
trough_low = 12,690
MAE = -34.04%
```

This is weaker than 한국석유 because MFE is shallow relative to the drawdown. It should not even be promoted into a positive local 4B row unless there is a very explicit non-price contract or cashflow route.

Calibration implication:

```text
Generic distributor/geopolitical-oil beta should be capped at Watch.
If it lacks project economics and delivers shallow MFE with -30% MAE, route to hard 4C candidate.
```

---

## 7. Score / return alignment stress test

### 7.1 Current calibrated profile behavior

Current calibrated proxy:

```text
profile = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

### 7.2 Residual error

The calibrated profile already blocks pure price-only blowoff better than the old baseline.  
The residual C16 error is more specific:

```text
policy evidence can look like real fundamental evidence,
but exploration authorization is not the same as reserve confirmation or company cashflow.
```

This is why generic oil/gas sympathy names can still sneak into Stage2-Actionable if the model treats "national resource policy + sector label + volume" as enough evidence.

### 7.3 Raw component score simulation

| ticker | policy evidence | company bridge | price confirmation | 4B/4C risk | simulated outcome |
|---|---:|---:|---:|---:|---|
| 036460 | high | medium | high | local 4B after fast +60% | Stage2-Actionable / Yellow, Green only with reserve/cashflow evidence |
| 004090 | high headline | low | local only | high 4B / false-positive | Watch or capped Stage2, not Green |
| 024060 | high headline | very low | weak local | hard 4C candidate | Watch only / 4C if thesis treated as company-specific |

---

## 8. Shadow rule candidate

```text
rule_id:
  C16_RESOURCE_POLICY_EXPLORATION_REQUIRES_RESERVE_CASHFLOW_BRIDGE

trigger_condition:
  canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  and trigger_type in [
    exploration_policy_headline,
    strategic_resource_discovery_headline,
    government_drilling_authorization,
    offshore_oil_gas_reserve_estimate
  ]

positive_stage_cap:
  If company_specific_bridge_score < threshold:
    max_stage = Watch or Stage2
    Stage3-Green blocked

required_non_price_bridge_for_Green:
  at least two of:
    - project equity / operator / named service scope
    - confirmed reserves or drilling result
    - explicit government/KNOC/utility contract route
    - offtake / regulated earnings / tariff recovery route
    - revenue/margin/EPS timing bridge
    - credible balance-sheet capacity to participate

price_guard:
  If 20D MFE > +25% but no non-price confirmation:
    local_4b_watch = true

hard_4c_route:
  If MFE < +15% and MAE <= -25% within 90D:
    classify as C16 policy-sympathy false positive / hard 4C candidate
```

No production scoring is changed in this MD. This is a shadow-rule candidate only.

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type": "trigger_case", "schema_version": "e2r_v12_residual_case_v1", "scheduled_round": "R4", "scheduled_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "EAST_SEA_GAS_FIELD_POLICY_EXPLORATION_TO_RESERVE_CASHFLOW_BRIDGE", "ticker": "036460", "name": "한국가스공사", "trigger_type": "east_sea_oil_gas_policy_exploration_headline", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 39400, "window_basis": "stock_web_tradable_raw_1d_ohlcv", "mfe_peak_date": "2024-06-20", "mfe_peak_high": 64500, "mfe_pct": 63.71, "mae_trough_date": "2024-11-01", "mae_trough_low": 37750, "mae_pct": -4.19, "classification": "positive_with_local_4B_watch", "stage2_residual_error": true, "production_scoring_changed": false, "shadow_rule_only": true}
{"row_type": "trigger_case", "schema_version": "e2r_v12_residual_case_v1", "scheduled_round": "R4", "scheduled_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "EAST_SEA_GAS_FIELD_POLICY_EXPLORATION_TO_RESERVE_CASHFLOW_BRIDGE", "ticker": "004090", "name": "한국석유", "trigger_type": "east_sea_oil_gas_policy_exploration_headline", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 23300, "window_basis": "stock_web_tradable_raw_1d_ohlcv", "mfe_peak_date": "2024-06-05", "mfe_peak_high": 28100, "mfe_pct": 20.6, "mae_trough_date": "2024-07-25", "mae_trough_low": 15540, "mae_pct": -33.3, "classification": "counterexample_price_only_sympathy", "stage2_residual_error": true, "production_scoring_changed": false, "shadow_rule_only": true}
{"row_type": "trigger_case", "schema_version": "e2r_v12_residual_case_v1", "scheduled_round": "R4", "scheduled_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "EAST_SEA_GAS_FIELD_POLICY_EXPLORATION_TO_RESERVE_CASHFLOW_BRIDGE", "ticker": "024060", "name": "흥구석유", "trigger_type": "east_sea_oil_gas_policy_exploration_headline", "trigger_date": "2024-06-03", "entry_date": "2024-06-04", "entry_price": 19240, "window_basis": "stock_web_tradable_raw_1d_ohlcv", "mfe_peak_date": "2024-08-05", "mfe_peak_high": 21400, "mfe_pct": 11.23, "mae_trough_date": "2024-07-25", "mae_trough_low": 12690, "mae_pct": -34.04, "classification": "hard_4c_candidate", "stage2_residual_error": true, "production_scoring_changed": false, "shadow_rule_only": true}
{"row_type": "aggregate", "schema_version": "e2r_v12_residual_aggregate_v1", "scheduled_round": "R4", "scheduled_loop": 90, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "EAST_SEA_GAS_FIELD_POLICY_EXPLORATION_TO_RESERVE_CASHFLOW_BRIDGE", "new_independent_case_count": 3, "same_archetype_new_symbol_count": 3, "positive_case_count": 1, "counterexample_count": 2, "local_4b_overlay_case_count": 2, "hard_4c_candidate_count": 1, "calibration_usable_trigger_count": 3, "residual_contribution_label": "residual_error_found", "do_not_propose_new_weight_delta": true}
{"row_type": "shadow_rule_candidate", "schema_version": "e2r_v12_shadow_rule_candidate_v1", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "rule_name": "resource_policy_exploration_headline_requires_company_specific_reserve_cashflow_bridge", "rule_logic": ["Exploration-policy headlines may open Watch/Yellow, not Green, unless company-specific reserve/offtake/equity/cashflow exposure is demonstrated.", "Oil/gas distributor or generic petroleum label sympathy is price-only unless it has direct project economics, committed offtake, upstream equity, or regulated earnings bridge.", "If post-trigger MFE is shallow or local-only and 60D/180D MAE breaches -25% without reserve confirmation, classify as 4C candidate or Stage2 false-positive."], "production_scoring_changed": false, "handoff_only": true}
```

---

## 10. Residual contribution summary

```text
completed_round: R4
completed_loop: 90

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

next_round: R5
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during research generation.
This handoff is for later batch implementation only.

Context:
- Source research MD:
  e2r_stock_web_v12_residual_round_R4_loop_90_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
- canonical_archetype_id:
  C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
- fine_archetype_id:
  EAST_SEA_GAS_FIELD_POLICY_EXPLORATION_TO_RESERVE_CASHFLOW_BRIDGE

Task:
1. Review the machine-readable trigger_case rows.
2. Add a C16-specific shadow rule candidate, not a production weight change:
   resource_policy_exploration_headline_requires_company_specific_reserve_cashflow_bridge.
3. Enforce that exploration-policy and strategic-resource discovery headlines cannot open Stage3-Green without explicit company-specific reserve/offtake/cashflow bridge.
4. Add local 4B watch when policy-resource names move >25% before non-price evidence catches up.
5. Add hard 4C candidate routing for generic oil/gas/petroleum sympathy names with MFE <15% and MAE <= -25% within 90D.
6. Do not change global stage thresholds from this MD alone.
7. Keep this change as archetype-specific / shadow-rule candidate unless corroborated by later C16 rows.

Expected tests:
- 036460 should remain Stage2-Actionable/Yellow eligible, Green only with stronger non-price bridge.
- 004090 should be capped below Green as policy-sympathy false positive.
- 024060 should be hard-4C candidate when no project economics bridge exists.

Production scoring changed by this handoff: false unless explicitly approved in a later implementation session.
```
