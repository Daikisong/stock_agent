---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
file_name: e2r_stock_web_v12_residual_round_R1_loop_103_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
selected_round: R1
selected_loop: 103
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_CONTRACT_BACKLOG_DELIVERY_SCHEDULE_MARGIN_BRIDGE_VS_FRAMEWORK_MOU_EVENT_CAP
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R v12 residual research — R1 / L1 / C03 defense export backlog bridge

## 1. Research purpose

This run tests **C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG** after the first stock-web calibration pass.  The specific residual question is:

> When Korean defense names move on export headlines, can the current calibrated profile distinguish a hard export contract with backlog/delivery schedule from a framework/MOU or expected follow-on contract that has not yet become executable backlog?

The working distinction is intentionally narrow:

- **Positive C03 bridge**: signed export contract, named buyer/country, size, delivery window, backlog expansion, and enough non-price evidence to support Stage2-Actionable / Stage3-Yellow.
- **Counterexample / event-cap**: summit statement, framework agreement, expected follow-on order, or negotiation-complete language without the executable contract. This can still produce short MFE, but should not loosen Green and should remain 4B-watchable if price outruns contract certainty.

This file does not patch `stock_agent`; it is a standalone research artifact for later batch ingestion.

## 2. Price-source validation

`Songdaiki/stock-web` manifest snapshot used by this research:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis = tradable_raw
```

Corporate-action windows are avoided for the selected 2024 event windows.  All three selected symbols have active-like stock-web symbol profiles and 2024 tradable shard rows.

## 3. Novelty / no-repeat check

No-Repeat Index says Priority 1 begins with C03 at 30 rows, with the research point: defense export contracts, backlog, delivery schedule, and margin conversion. This run adds three new C03 trigger families:

1. `ROMANIA_K9_EXECUTABLE_CONTRACT_BACKLOG_BRIDGE` — Hanwha Aerospace / Romania K9 + K10 order.
2. `IRAQ_CHEONGUNG_II_MISSILE_EXPORT_ORDER_BRIDGE` — LIG Nex1 / Iraq M-SAM II order.
3. `POLAND_K2_FOLLOW_ON_FRAMEWORK_EVENT_CAP` — Hyundai Rotem / Poland K2 follow-on expectation without 2024 final executable contract.

Hard duplicate policy applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No reused prior case is intentionally introduced.

## 4. Case set summary

| case_id | symbol | name | trigger_date | entry_date | entry_close | peak_high | trough_low | MFE % | MAE % | classification |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| C03-103-01 | 012450 | Hanwha Aerospace | 2024-07-09 | 2024-07-10 | 256500 | 395000 | 247000 | 54.00 | -3.70 | positive_contract_backlog_bridge |
| C03-103-02 | 079550 | LIG Nex1 | 2024-09-20 | 2024-09-20 | 211000 | 270000 | 208000 | 27.96 | -1.42 | positive_missile_export_backlog_bridge |
| C03-103-03 | 064350 | Hyundai Rotem | 2024-10-25 | 2024-10-25 | 64300 | 69500 | 43650 | 8.09 | -32.12 | counterexample_framework_event_cap |

Calculation convention:

```text
MFE_pct = (post_entry_peak_high / entry_close - 1) * 100
MAE_pct = (post_entry_trough_low / entry_close - 1) * 100
```

## 5. Case detail

### 5.1 C03-103-01 — 012450 Hanwha Aerospace / Romania K9 contract

**Evidence family:** executable export contract + delivery schedule + backlog bridge.

Reuters reported on 2024-07-09 that Hanwha Aerospace secured a roughly $1 billion Romania order for 54 K9 self-propelled howitzers, ammunition, and 36 K10 resupply vehicles. The contract runs to July 2029 and the report also notes the defense backlog had expanded sharply from end-2021 to March 2024.

**Stock-web OHLC row evidence:**

```text
2024-07-09,251500,254500,245500,252000,...
2024-07-10,257500,273500,255500,256500,...  <-- entry_close
2024-08-05,285000,293000,247000,267000,...  <-- post-entry trough_low used for MAE
2024-10-17,385500,395000,381500,393000,...  <-- peak_high used for MFE
```

**Path result:**

```text
entry_close = 256500
peak_high = 395000
trough_low = 247000
MFE = +54.00%
MAE = -3.70%
```

**Interpretation:**

This is a clean C03 positive. The move was not just a generic defense beta; the evidence stack had contract value, buyer, product, delivery horizon, and backlog reinforcement. A calibrated profile should allow Stage2-Actionable / Yellow pressure when contract certainty and delivery visibility are present. Green should still wait for margin conversion, production cadence, and working-capital confirmation, but this case is not a price-only blowoff.

### 5.2 C03-103-02 — 079550 LIG Nex1 / Iraq Cheongung-II order

**Evidence family:** executable missile-defense export order + country expansion + system validation.

Reuters reported that LIG Nex1 won a 3.71 trillion won / $2.8 billion Iraq order to export mid-range surface-to-air missile defense systems. The report explicitly links the order to M-SAM II / Cheongung-II, following earlier UAE and Saudi export lines, making this a meaningful export-product repeatability case rather than a one-off domestic procurement event.

**Stock-web OHLC row evidence:**

```text
2024-09-19,209500,211000,205500,206500,...
2024-09-20,214500,218500,208500,211000,...  <-- entry_close
2024-09-27,215500,217500,208000,210500,...  <-- post-entry trough_low used for MAE
2024-11-07,263500,270000,257000,269000,...  <-- peak_high used for MFE
```

**Path result:**

```text
entry_close = 211000
peak_high = 270000
trough_low = 208000
MFE = +27.96%
MAE = -1.42%
```

**Interpretation:**

This is a second positive bridge, but different from Hanwha: the product is missile-defense rather than artillery. The stronger signal is repeat exportability of the same air-defense system family across multiple countries. The residual rule should reward repeatable export item status, but still require backlog-to-revenue schedule and margin evidence before Green.

### 5.3 C03-103-03 — 064350 Hyundai Rotem / Poland K2 follow-on expectation

**Evidence family:** framework / expected follow-on contract / not-yet-executable backlog.

Reuters reported in October 2024 that Korean and Polish leaders agreed to push to finalize a new K2 export contract by year-end and that a deal on producing K2 tanks in Poland could be signed in coming weeks. However, the final follow-on Poland K2 contract did not become an executable 2024 contract; Reuters later reported the contract signing in 2025. This makes the 2024 event a high-quality C03 counterexample: strong strategic language, but not yet booked backlog.

**Stock-web OHLC row evidence:**

```text
2024-10-25,63400,65100,62300,64300,...   <-- entry_close
2024-11-20,66700,69500,65900,67100,...   <-- peak_high used for MFE
2024-12-10,44800,46200,43650,46000,...   <-- post-entry trough_low used for MAE
```

**Path result:**

```text
entry_close = 64300
peak_high = 69500
trough_low = 43650
MFE = +8.09%
MAE = -32.12%
```

**Interpretation:**

This case is the guardrail. A C03 system should not treat “expected contract by year-end” or “main issues agreed” as equivalent to executable backlog. It may justify watchlist / Stage2 observation because the export framework is real, but it should not receive the same Stage2-Actionable bonus as signed Hanwha/LIG contracts. If price already embeds the follow-on deal before signature, it should become `local_4B_watch_guard` or `framework_event_cap`, not positive Stage3 evidence.

## 6. Score alignment stress test

| case_id | old likely profile behavior | residual error | desired v12 shadow response |
|---|---|---|---|
| C03-103-01 | Correctly identifies defense export theme; may underweight delivery schedule | Mild false-lateness risk | Add C03 contract/delivery bridge support for Stage2-Actionable |
| C03-103-02 | Correctly identifies export order; may overfit generic defense beta | Moderate classification risk | Require repeat export system + signed order + contract value |
| C03-103-03 | May treat Poland K2 framework language as near-contract evidence | High false-positive risk | Block Stage2-Actionable unless executable contract/backlog exists |

## 7. Shadow rule candidate

```text
new_axis_proposed = c03_signed_export_contract_backlog_delivery_bridge_required_for_stage2_actionable_shadow_only
```

Proposed behavior:

```text
IF canonical_archetype_id == C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
AND evidence contains signed export contract OR binding executable order
AND evidence contains at least two of {buyer_country, contract_value, product/system, delivery_schedule, backlog_disclosure, repeat-export product family}
THEN allow C03 Stage2-Actionable bridge candidate.

IF evidence is only {MOU, framework agreement, summit statement, expected year-end contract, negotiation in progress, local production discussion}
AND no executable contract or regulatory filing confirms order/backlog
THEN block Stage2-Actionable bonus and route to framework_event_cap / local_4B_watch_guard.
```

This is a shadow rule only. It does not change production scoring.

## 8. Machine-readable rows

```jsonl
{"row_type":"price_source_validation","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":103,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"row_type":"case","case_id":"C03-103-01","symbol":"012450","name":"Hanwha Aerospace","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"ROMANIA_K9_EXECUTABLE_CONTRACT_BACKLOG_BRIDGE","trigger_date":"2024-07-09","entry_date":"2024-07-10","entry_close":256500,"mfe_90d_pct":54.00,"mae_90d_pct":-3.70,"classification":"positive_contract_backlog_bridge","calibration_usable":true}
{"row_type":"trigger","case_id":"C03-103-01","symbol":"012450","trigger_type":"signed_export_contract_backlog_bridge","trigger_family":"ROMANIA_K9_K10_CONTRACT","trigger_date":"2024-07-09","entry_date":"2024-07-10","entry_price":256500,"peak_date":"2024-10-17","peak_high":395000,"trough_date":"2024-08-05","trough_low":247000,"mfe_pct":54.00,"mae_pct":-3.70,"source_proxy":"Reuters Romania K9 contract report; stock-web 012/012450/2024.csv"}
{"row_type":"case","case_id":"C03-103-02","symbol":"079550","name":"LIG Nex1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"IRAQ_CHEONGUNG_II_MISSILE_EXPORT_ORDER_BRIDGE","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_close":211000,"mfe_90d_pct":27.96,"mae_90d_pct":-1.42,"classification":"positive_missile_export_backlog_bridge","calibration_usable":true}
{"row_type":"trigger","case_id":"C03-103-02","symbol":"079550","trigger_type":"signed_export_contract_backlog_bridge","trigger_family":"IRAQ_MSAM_II_EXPORT_ORDER","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":211000,"peak_date":"2024-11-07","peak_high":270000,"trough_date":"2024-09-27","trough_low":208000,"mfe_pct":27.96,"mae_pct":-1.42,"source_proxy":"Reuters Iraq missile systems order; stock-web 079/079550/2024.csv"}
{"row_type":"case","case_id":"C03-103-03","symbol":"064350","name":"Hyundai Rotem","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"POLAND_K2_FOLLOW_ON_FRAMEWORK_EVENT_CAP","trigger_date":"2024-10-25","entry_date":"2024-10-25","entry_close":64300,"mfe_90d_pct":8.09,"mae_90d_pct":-32.12,"classification":"counterexample_framework_event_cap","calibration_usable":true}
{"row_type":"trigger","case_id":"C03-103-03","symbol":"064350","trigger_type":"framework_expected_contract_event_cap","trigger_family":"POLAND_K2_FOLLOW_ON_NOT_YET_EXECUTABLE","trigger_date":"2024-10-25","entry_date":"2024-10-25","entry_price":64300,"peak_date":"2024-11-20","peak_high":69500,"trough_date":"2024-12-10","trough_low":43650,"mfe_pct":8.09,"mae_pct":-32.12,"source_proxy":"Reuters Poland K2 follow-on expectation; stock-web 064/064350/2024.csv"}
{"row_type":"aggregate_metric","selected_round":"R1","selected_loop":103,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","case_count":3,"positive_case_count":2,"counterexample_count":1,"avg_mfe_pct":30.02,"avg_mae_pct":-12.41,"current_profile_error_count":1,"residual_label":"framework_mou_vs_signed_export_contract_separation"}
{"row_type":"score_simulation","selected_round":"R1","selected_loop":103,"canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","rule_axis":"c03_signed_export_contract_backlog_delivery_bridge_required_for_stage2_actionable_shadow_only","positive_bridge_cases":2,"blocked_framework_cases":1,"expected_effect":"reduce C03 false positive from MOU/framework expectation while preserving signed export contract positives"}
{"row_type":"shadow_weight","selected_round":"R1","selected_loop":103,"canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","new_axis_proposed":"c03_signed_export_contract_backlog_delivery_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C03 framework/MOU defense export rallies","do_not_propose_new_weight_delta":false,"production_scoring_changed":false}
{"row_type":"residual_contribution","selected_round":"R1","selected_loop":103,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","loop_contribution_label":"canonical_archetype_rule_candidate","summary":"C03 should distinguish signed export contract/backlog bridge from framework or expected follow-on contract. Hanwha and LIG are positive signed-order cases; Hyundai Rotem shows high-MAE event-cap when framework language preceded executable contract."}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff during the research session.

Later coding agent task:
- Ingest this MD as a v12 sector/archetype residual research artifact.
- Validate JSONL rows.
- Check duplicate key: canonical_archetype_id + symbol + trigger_type + entry_date.
- Add no direct production scoring change from this file alone.
- Consider shadow axis: c03_signed_export_contract_backlog_delivery_bridge_required_for_stage2_actionable_shadow_only.
- Confirm that C03 Stage2-Actionable requires executable export contract/order plus at least two non-price bridge fields.
- Confirm that framework/MOU/year-end expected contracts route to framework_event_cap / local_4B_watch_guard unless signed order/backlog evidence appears.
```

## 10. Final residual summary

```text
selected_round: R1
selected_loop: 103
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_CONTRACT_BACKLOG_DELIVERY_SCHEDULE_MARGIN_BRIDGE_VS_FRAMEWORK_MOU_EVENT_CAP
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
diversity_score_summary: C03 Priority 1 first-axis coverage with artillery, missile-defense, and tank follow-on framework separation
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C03 rows 30, 50-row target까지 20 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c03_signed_export_contract_backlog_delivery_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C03 framework/MOU defense export rallies
existing_axis_weakened: null
next_recommended_archetypes: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```
