# E2R Stock-Web v12 Residual Research — R4 loop 100 / L4 / C16

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 100
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: CRITICAL_METAL_SMELTING_COPPER_SUPPLY_CHAIN_LITHIUM_RESOURCE_POLICY_OFFTAKE_MARGIN_FCF_BRIDGE_VS_RESOURCE_LABEL_AND_LITHIUM_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill_to_50
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - offtake_to_margin_FCF_bridge_test
  - strategic_resource_policy_execution_guardrail
  - critical_metal_smelter_positive_delta
  - copper_supply_chain_positive_with_sizing_guard
  - lithium_resource_policy_false_stage2_guard
  - copper_foil_localization_false_stage2_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` 전용 residual research다.

C16은 “전략자원”, “핵심광물”, “리튬”, “동/비철”, “중국 공급망 차단”, “자원 안보”, “정부 정책 수혜”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 정책·공급망 narrative가 실제 offtake, smelting/refining capacity, procurement, inventory valuation, spread, ASP, working capital, OPM, FCF, EPS revision으로 내려오는지다.

```text
strategic resource / policy / supply-chain headline
  → offtake, refining, smelting, procurement, localization
  → volume, ASP, spread, inventory valuation, cost pass-through
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

전략자원은 지도 위 광산 표시와 같다. 표시가 있어도 광석을 캐고, 제련하고, 고객에게 팔고, 재고와 스프레드가 현금으로 바뀌어야 가치가 된다. C16은 “자원이 있다”와 “자원이 마진으로 흐른다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["010130","006260","103140","005490","020150"],"profile_paths":["atlas/symbol_profiles/010/010130.json","atlas/symbol_profiles/006/006260.json","atlas/symbol_profiles/103/103140.json","atlas/symbol_profiles/005/005490.json","atlas/symbol_profiles/020/020150.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv","atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv"],"validation_scope":"2024 trigger-level forward path; 010130/103140/005490/020150 have zero corporate-action candidates; 006260 caveats are historical 1996/1999. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C16 at 30 rows and 20 rows short of the 50-row practical calibration target.
- Existing registry shows C16 parsed through `R4 loop 99`.
- This output uses `R4 loop 100`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C16 loops covered lithium resource policy, East Sea gas, aluminum/nonferrous, copper supply chain, and gas/LNG/lithium/rare-earth labels. This file compresses critical-metal smelting, copper supply-chain holdco, copper/munition strategic-metal spread, lithium-resource false Stage2, and copper-foil localization false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C16-R4L100-01 | 010130 | 고려아연 | 2024-09-13 | 2024-09-13 | 666000 | 1543000 | 655000 | 131.68% | -1.65% | Critical metal smelting/refining scarcity rerating worked, but governance squeeze must be separated from offtake margin. |
| C16-R4L100-02 | 006260 | LS | 2024-04-11 | 2024-04-11 | 114900 | 194800 | 93300 | 69.54% | -18.80% | Copper/electrification supply-chain rerating worked, but full-window drawdown requires sizing and FCF guard. |
| C16-R4L100-03 | 103140 | 풍산 | 2024-03-07 | 2024-03-07 | 46100 | 74000 | 44300 | 60.52% | -3.90% | Copper strategic-metal plus defense demand path worked with controlled early MAE. |
| C16-R4L100-04 | 005490 | POSCO홀딩스 | 2024-03-04 | 2024-03-04 | 458000 | 471000 | 309000 | 2.84% | -32.53% | Lithium resource policy label failed without visible offtake, price, margin and FCF conversion. |
| C16-R4L100-05 | 020150 | 롯데에너지머티리얼즈 | 2024-03-21 | 2024-03-21 | 47050 | 52400 | 30500 | 11.37% | -35.18% | Copper-foil localization/resource-security label made MFE but decayed without utilization and margin bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C16-R4L100-01","round":"R4","loop":"100","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"CRITICAL_METAL_SMELTER_REFINING_SCARCITY_OFFTAKE_MARGIN_BRIDGE","symbol":"010130","name":"고려아연","trigger_type":"critical_metal_smelter_refining_scarcity_offtake_margin_bridge","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000,"peak_price":1543000,"peak_date":"2024-10-29","trough_price":655000,"trough_date":"2024-09-13","mfe_pct":131.68,"mae_pct":-1.65,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_offtake_smelt_margin_URLs","residual_flag":"critical_metal_smelter_positive_but_governance_squeeze_must_be_separated_from_offtake_margin_FCF_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|critical_metal_smelter_refining_scarcity_offtake_margin_bridge|2024-09-13"}
{"row_type":"trigger","case_id":"C16-R4L100-02","round":"R4","loop":"100","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ELECTRIFICATION_SUPPLY_CHAIN_HOLDCO_POSITIVE_WITH_FCF_GUARD","symbol":"006260","name":"LS","trigger_type":"copper_electrification_supply_chain_holdco_positive_with_fcf_guard","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":114900,"peak_price":194800,"peak_date":"2024-05-21","trough_price":93300,"trough_date":"2024-09-09","mfe_pct":69.54,"mae_pct":-18.80,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_sizing_guard","residual_flag":"copper_supply_chain_positive_but_requires_cable_backlog_inventory_spread_OPM_FCF_URLs","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006260|copper_electrification_supply_chain_holdco_positive_with_fcf_guard|2024-04-11"}
{"row_type":"trigger","case_id":"C16-R4L100-03","round":"R4","loop":"100","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_STRATEGIC_METAL_DEFENSE_DEMAND_SPREAD_MARGIN_BRIDGE","symbol":"103140","name":"풍산","trigger_type":"copper_strategic_metal_defense_demand_spread_margin_bridge","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":46100,"peak_price":74000,"peak_date":"2024-10-22","trough_price":44300,"trough_date":"2024-03-13","mfe_pct":60.52,"mae_pct":-3.90,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_copper_spread_defense_margin_URLs","residual_flag":"copper_strategic_metal_path_positive_but_requires_spread_volume_inventory_OPM_FCF_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|103140|copper_strategic_metal_defense_demand_spread_margin_bridge|2024-03-07"}
{"row_type":"trigger","case_id":"C16-R4L100-04","round":"R4","loop":"100","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_POLICY_LABEL_FALSE_STAGE2_HIGH_MAE","symbol":"005490","name":"POSCO홀딩스","trigger_type":"lithium_resource_policy_label_false_stage2_high_mae","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":458000,"peak_price":471000,"peak_date":"2024-03-05","trough_price":309000,"trough_date":"2024-08-05","mfe_pct":2.84,"mae_pct":-32.53,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"lithium_resource_policy_label_failed_without_offtake_price_margin_FCF_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|lithium_resource_policy_label_false_stage2_high_mae|2024-03-04"}
{"row_type":"trigger","case_id":"C16-R4L100-05","round":"R4","loop":"100","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_FOIL_LOCALIZATION_RESOURCE_SECURITY_FALSE_STAGE2_HIGH_MAE","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"copper_foil_localization_resource_security_false_stage2_high_mae","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":47050,"peak_price":52400,"peak_date":"2024-03-27","trough_price":30500,"trough_date":"2024-08-05","mfe_pct":11.37,"mae_pct":-35.18,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"copper_foil_resource_security_label_decayed_without_customer_pull_utilization_margin_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|020150|copper_foil_localization_resource_security_false_stage2_high_mae|2024-03-21"}
```

## 6. Score-return alignment

### 6.1 Critical-metal and copper supply-chain winners

`010130`, `006260`, and `103140` are the constructive C16 family. These rows show that strategic-resource scarcity, smelting/refining importance, copper electrification, and defense-adjacent copper demand can create large MFE. Still, the scorer must ask whether the move is supported by offtake, volume, spread, inventory, OPM and FCF rather than governance squeeze or commodity beta alone.

### 6.2 Lithium resource policy label false Stage2

`005490` is the hard warning row. Lithium resource policy and vertical-integration vocabulary sounded strategic, but the selected 2024 forward path produced tiny MFE and deep MAE. C16 should cap these rows unless offtake, lithium price, ramp schedule, capex discipline, margin and cash conversion repair the thesis.

### 6.3 Localization / copper-foil false Stage2

`020150` shows the localization trap. Copper foil can be framed as strategic-resource supply-chain security, but if utilization, customer pull, inventory and margin do not hold, the row should stay Stage2/local 4B.

## 7. Raw component score simulation

| symbol | resource/policy evidence | offtake/supply execution | spread/ASP bridge | OPM/FCF bridge | price confirmation | MAE/theme guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 010130 | 24 | 18 | 17 | 13 | 25 | -2 | 95 | Stage3-Yellow/Green candidate |
| 006260 | 21 | 15 | 15 | 11 | 20 | -8 | 74 | Stage3-Yellow with sizing guard |
| 103140 | 19 | 14 | 16 | 12 | 18 | -3 | 76 | Stage3-Yellow candidate |
| 005490 | 20 | 5 | 3 | 2 | 1 | -16 | 15 | Hard counterexample/local 4B |
| 020150 | 17 | 5 | 4 | 3 | 5 | -17 | 17 | Stage2/local 4B |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c16_resource_policy_requires_offtake_spread_OPM_FCF_bridge","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage2_required_bridge","rule":"Do not promote strategic-resource/policy/supply-chain labels above Stage2 unless offtake, procurement, smelting/refining capacity, localization execution, volume, ASP, spread, inventory valuation, cost pass-through, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["005490","020150"],"counterbalanced_by":["010130","006260","103140"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_critical_metal_smelter_positive_delta","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Critical-metal smelting/refining rows can receive strong Stage3-Yellow/Green candidate treatment when offtake, production, spread and FCF evidence are URL-verified; governance squeeze should be separately capped.","supporting_cases":["010130"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_copper_supply_chain_positive_with_sizing_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage3_yellow_candidate_with_sizing_guard","rule":"Copper supply-chain and strategic-metal rows can become Yellow/Stage3 when spread, volume, inventory and margin evidence appears, but meaningful MAE requires sizing guard.","supporting_cases":["006260","103140"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_lithium_resource_policy_false_stage2_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"hard_counterexample_or_local_4b","rule":"Lithium resource policy rows with tiny MFE and large MAE should remain local 4B or hard counterexample unless offtake, ramp, lithium price, margin and FCF evidence repairs the row.","supporting_cases":["005490"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_copper_foil_localization_false_stage2_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage2_or_local_4b_watch","rule":"Copper foil/localization/resource-security rows require customer pull, utilization, inventory and OPM evidence; high MAE blocks Green even when the localization vocabulary sounds strategic.","supporting_cases":["020150"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","round":"R4","loop":"100","positive_rows":3,"counterexample_rows":2,"new_symbol_count":5,"primary_residual":"C16 should separate critical-metal smelter and copper strategic-metal winners from lithium resource policy and copper-foil localization labels that fail without offtake, utilization, spread, OPM and FCF bridge.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage3_yellow_candidate_with_sizing_guard","hard_counterexample_or_local_4b","stage2_or_local_4b_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","sample_count":5,"avg_mfe_pct":55.19,"avg_mae_pct":-18.41,"median_mfe_pct":60.52,"median_mae_pct":-18.80,"interpretation":"C16 has large upside when resource scarcity closes into smelting, copper supply-chain or strategic-metal margin, but lithium/localization labels need strict offtake, utilization and FCF guardrails."}
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
- Ingest this C16 R4 loop 100 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c16_resource_policy_requires_offtake_spread_OPM_FCF_bridge -> stage2_required_bridge
  2. c16_critical_metal_smelter_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c16_copper_supply_chain_positive_with_sizing_guard -> stage3_yellow_candidate_with_sizing_guard
  4. c16_lithium_resource_policy_false_stage2_guard -> hard_counterexample_or_local_4b
  5. c16_copper_foil_localization_false_stage2_guard -> stage2_or_local_4b_watch

Expected behavior:
- Strategic-resource/policy/supply-chain vocabulary alone should not create Green.
- Offtake, procurement, smelting/refining capacity, localization execution, volume, ASP, spread, inventory valuation, OPM, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Lithium resource policy and copper-foil localization rows with high MAE should stay capped until fresh non-price evidence appears.
```
