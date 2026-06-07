# E2R Stock-Web v12 Residual Research — R4 loop 101 / L4 / C16

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 101
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RESOURCE_TRADING_LNG_NICKEL_RARE_EARTH_LOCALIZATION_SUPPLY_SECURITY_VS_STRATEGIC_RESOURCE_LABEL_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill_to_50
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - resource_trading_to_margin_FCF_bridge_test
  - LNG_and_mineral_offtake_execution_guardrail
  - rare_earth_magnet_theme_false_stage2_guard
  - nickel_plated_steel_localization_high_MAE_guardrail
  - STX_lithium_nickel_trading_event_cap_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`의 추가 보강이다.

직전 C16 loop 100은 critical-metal smelter, copper supply chain, lithium policy false Stage2, copper-foil localization을 다뤘다. 이번 loop 101은 자원상사, LNG/광물 trading, 리튬·니켈 trading, 희토류 magnet theme, 니켈도금 강판/localization spike를 분리한다.

```text
strategic resource / resource trading / rare-earth / nickel localization headline
  → offtake, procurement, trading spread, customer pull, qualified volume
  → inventory valuation, ASP, cost pass-through, working capital
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

전략자원 trading은 항구의 선하증권과 같다. 화물이 배에 올랐다는 말만으로 이익이 남지는 않는다. 조달 단가, 재고평가, 고객 인수, 환율, 스프레드가 맞물려야 종이가 현금으로 바뀐다. C16은 “자원 테마”와 “현금화된 공급망”을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["047050","001120","011810","047400","002710"],"profile_paths":["atlas/symbol_profiles/047/047050.json","atlas/symbol_profiles/001/001120.json","atlas/symbol_profiles/011/011810.json","atlas/symbol_profiles/047/047400.json","atlas/symbol_profiles/002/002710.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv","atlas/ohlcv_tradable_by_symbol_year/001/001120/2024.csv","atlas/ohlcv_tradable_by_symbol_year/011/011810/2024.csv","atlas/ohlcv_tradable_by_symbol_year/047/047400/2024.csv","atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv"],"validation_scope":"2024 trigger-level forward path; 047050 has a 2023-01-20 caveat and selected 2024 rows are post-caveat; 001120 caveats are historical and end 2006; 011810 has a 2024-01-05 caveat and selected rows are after that window; 047400 caveat is 2011; 002710 caveat is 2009. Selected local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C16 at 30 rows and 20 rows short of the 50-row practical calibration target.
- Repo registry shows C16 parsed through `R4 loop 99`.
- Prior local session emitted `R4 loop 100`; this file uses `R4 loop 101`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file uses symbols not used in C16 loop 100: `047050`, `001120`, `011810`, `047400`, `002710`.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C16-R4L101-01 | 047050 | 포스코인터내셔널 | 2024-01-24 | 2024-01-24 | 49850 | 61700 | 44000 | 23.77% | -11.74% | LNG/resource trading rebound worked, but later drawdown requires procurement, inventory and FCF bridge. |
| C16-R4L101-02 | 001120 | LX인터내셔널 | 2024-01-30 | 2024-01-30 | 28250 | 33000 | 25800 | 16.81% | -8.67% | Resource trading / coal-nickel exposure was steadier but not strong enough for Green without margin bridge. |
| C16-R4L101-03 | 011810 | STX | 2024-02-16 | 2024-02-16 | 10950 | 11900 | 4800 | 8.68% | -56.16% | Lithium/nickel resource trading label became high-MAE event-cap/false Stage2. |
| C16-R4L101-04 | 047400 | 유니온머티리얼 | 2024-01-18 | 2024-01-18 | 3535 | 3675 | 1940 | 3.96% | -45.12% | Rare-earth/magnet theme label produced tiny MFE and severe drawdown. |
| C16-R4L101-05 | 002710 | TCC스틸 | 2024-02-16 | 2024-02-16 | 65700 | 85900 | 27000 | 30.75% | -58.90% | Nickel-plated steel/localization spike made MFE but collapsed without durable customer pull and margin bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C16-R4L101-01","round":"R4","loop":"101","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LNG_RESOURCE_TRADING_PROCUREMENT_INVENTORY_MARGIN_BRIDGE","symbol":"047050","name":"포스코인터내셔널","trigger_type":"lng_resource_trading_procurement_inventory_margin_bridge","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":49850,"peak_price":61700,"peak_date":"2024-03-13","trough_price":44000,"trough_date":"2024-08-05","mfe_pct":23.77,"mae_pct":-11.74,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_procurement_inventory_FCF_guard","residual_flag":"resource_trading_rebound_worked_but_needs_LNG_procurement_inventory_OPM_FCF_URLs","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047050|lng_resource_trading_procurement_inventory_margin_bridge|2024-01-24"}
{"row_type":"trigger","case_id":"C16-R4L101-02","round":"R4","loop":"101","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RESOURCE_TRADING_COAL_NICKEL_EXPOSURE_STEADY_WITH_MARGIN_GUARD","symbol":"001120","name":"LX인터내셔널","trigger_type":"resource_trading_coal_nickel_exposure_steady_with_margin_guard","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":28250,"peak_price":33000,"peak_date":"2024-08-27","trough_price":25800,"trough_date":"2024-03-19","mfe_pct":16.81,"mae_pct":-8.67,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_resource_margin_guard","residual_flag":"resource_trading_steady_but_requires_commodity_price_inventory_OPM_FCF_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001120|resource_trading_coal_nickel_exposure_steady_with_margin_guard|2024-01-30"}
{"row_type":"trigger","case_id":"C16-R4L101-03","round":"R4","loop":"101","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_NICKEL_RESOURCE_TRADING_EVENT_CAP_FALSE_STAGE2","symbol":"011810","name":"STX","trigger_type":"lithium_nickel_resource_trading_event_cap_false_stage2","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":10950,"peak_price":11900,"peak_date":"2024-02-16","trough_price":4800,"trough_date":"2024-09-09","mfe_pct":8.68,"mae_pct":-56.16,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_event_cap","residual_flag":"lithium_nickel_trading_label_failed_without_offtake_inventory_margin_FCF_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|011810|lithium_nickel_resource_trading_event_cap_false_stage2|2024-02-16"}
{"row_type":"trigger","case_id":"C16-R4L101-04","round":"R4","loop":"101","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_MAGNET_THEME_LOW_MFE_HIGH_MAE_FALSE_STAGE2","symbol":"047400","name":"유니온머티리얼","trigger_type":"rare_earth_magnet_theme_low_mfe_high_mae_false_stage2","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":3535,"peak_price":3675,"peak_date":"2024-01-23","trough_price":1940,"trough_date":"2024-09-09","mfe_pct":3.96,"mae_pct":-45.12,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"rare_earth_theme_label_tiny_MFE_high_MAE_without_procurement_customer_margin_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047400|rare_earth_magnet_theme_low_mfe_high_mae_false_stage2|2024-01-18"}
{"row_type":"trigger","case_id":"C16-R4L101-05","round":"R4","loop":"101","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"NICKEL_PLATED_STEEL_LOCALIZATION_SPIKE_HIGH_MAE_GUARD","symbol":"002710","name":"TCC스틸","trigger_type":"nickel_plated_steel_localization_spike_high_mae_guard","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":65700,"peak_price":85900,"peak_date":"2024-02-21","trough_price":27000,"trough_date":"2024-08-05","mfe_pct":30.75,"mae_pct":-58.90,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guard_or_event_cap","residual_flag":"nickel_plated_steel_spike_MFE_but_customer_pull_utilization_OPM_FCF_bridge_absent_high_MAE","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|002710|nickel_plated_steel_localization_spike_high_mae_guard|2024-02-16"}
```

## 6. Score-return alignment

### 6.1 Resource trading can be Yellow only with cash bridge

`047050` and `001120` are the less broken side of this C16 sample. Both had tradable MFE and manageable initial MAE, but neither should become automatic Green from resource trading vocabulary alone. The scorer needs procurement cost, inventory valuation, commodity price exposure, customer offtake, OPM and FCF evidence.

### 6.2 Lithium/nickel and rare-earth theme labels decay fast

`011810` and `047400` are hard warning rows. Lithium/nickel trading and rare-earth magnet vocabulary created only small MFE before deep drawdown. These should be local 4B, event-cap, or hard counterexamples unless offtake and margin evidence repairs them.

### 6.3 Localization spike is still not a strategic-resource bridge

`002710` shows the tricky middle case: large MFE existed, but MAE was even larger. Nickel-plated steel/localization rows can run sharply, yet C16 should not promote them unless customer pull, utilization, ASP/mix, inventory and OPM/FCF bridge are visible.

## 7. Raw component score simulation

| symbol | resource/policy evidence | offtake/procurement execution | inventory/spread/ASP | OPM/FCF bridge | price confirmation | MAE/theme guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 047050 | 18 | 12 | 10 | 8 | 10 | -6 | 52 | Stage2→Yellow with cash guard |
| 001120 | 16 | 10 | 9 | 7 | 8 | -4 | 46 | Stage2→Yellow |
| 011810 | 17 | 3 | 2 | 1 | 2 | -25 | 0 | Hard counterexample/event-cap |
| 047400 | 15 | 2 | 2 | 1 | 0 | -20 | 0 | Hard counterexample/local 4B |
| 002710 | 18 | 6 | 5 | 3 | 12 | -25 | 19 | Stage2/Yellow high-MAE guard |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c16_resource_trading_requires_procurement_inventory_OPM_FCF_bridge","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage2_required_bridge","rule":"Do not promote resource trading/LNG/coal/nickel labels above Stage2 unless procurement cost, customer offtake, inventory valuation, commodity exposure, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["011810","047400"],"counterbalanced_by":["047050","001120"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_LNG_resource_trading_yellow_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage2_to_yellow_with_cash_guard","rule":"LNG/resource trading rows can become Yellow when procurement, inventory and FCF evidence is visible, but later drawdown blocks Green without cash conversion.","supporting_cases":["047050"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_lithium_nickel_trading_event_cap_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"hard_counterexample_or_event_cap","rule":"Lithium/nickel trading rows with small MFE and severe MAE should be event-capped or hard counterexamples unless firm offtake and margin bridge are verified.","supporting_cases":["011810"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_rare_earth_magnet_theme_false_stage2_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"hard_counterexample_or_local_4b","rule":"Rare-earth/magnet theme rows with tiny MFE and high MAE should remain local 4B unless procurement, qualified customer demand and margin evidence repairs the row.","supporting_cases":["047400"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_nickel_plated_steel_localization_high_MAE_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage2_to_yellow_with_high_MAE_guard_or_event_cap","rule":"Nickel-plated steel/localization spikes require customer pull, utilization and OPM/FCF bridge; large MFE does not override high MAE.","supporting_cases":["002710"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","round":"R4","loop":"101","positive_rows":2,"counterexample_rows":3,"new_symbol_count":5,"primary_residual":"C16 should separate steadier resource trading/LNG exposure from lithium-nickel trading, rare-earth magnet theme, and nickel-plated steel localization spikes that fail without offtake, inventory, utilization, margin and FCF bridge.","candidate_patch_axes":["stage2_required_bridge","stage2_to_yellow_with_cash_guard","hard_counterexample_or_event_cap","hard_counterexample_or_local_4b","stage2_to_yellow_with_high_MAE_guard_or_event_cap"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","sample_count":5,"avg_mfe_pct":16.79,"avg_mae_pct":-36.12,"median_mfe_pct":16.81,"median_mae_pct":-45.12,"interpretation":"C16 resource-trading/theme labels show poor asymmetry unless procurement, offtake, inventory and OPM/FCF conversion are explicit; theme spikes can make MFE but often collapse into high-MAE false Stage2."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - local 2024 OHLC rows were checked from stock-web tradable shards
  - selected local windows avoid active corporate-action contamination
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C16 R4 loop 101 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c16_resource_trading_requires_procurement_inventory_OPM_FCF_bridge -> stage2_required_bridge
  2. c16_LNG_resource_trading_yellow_guard -> stage2_to_yellow_with_cash_guard
  3. c16_lithium_nickel_trading_event_cap_guard -> hard_counterexample_or_event_cap
  4. c16_rare_earth_magnet_theme_false_stage2_guard -> hard_counterexample_or_local_4b
  5. c16_nickel_plated_steel_localization_high_MAE_guard -> stage2_to_yellow_with_high_MAE_guard_or_event_cap

Expected behavior:
- Resource trading / strategic-resource vocabulary alone should not create Green.
- Procurement cost, customer offtake, inventory valuation, commodity exposure, utilization, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Lithium/nickel trading, rare-earth magnet and nickel-plated steel localization rows with high MAE should stay capped until fresh non-price evidence appears.
```
