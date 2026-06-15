# E2R Stock-Web v12 Residual Research — R4 loop 97 / L4 / C16

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 97
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: SMELTER_GOVERNANCE_LITHIUM_COPPER_FOIL_RESOURCE_POLICY_OFFTAKE_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - strategic_resource_policy_to_offtake_margin_bridge_test
  - governance_squeeze_vs_supply_execution_guardrail
  - resource_label_false_stage2_guard
  - high_MAE_guardrail
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

C16은 “전략자원”, “핵심광물”, “리튬”, “니켈”, “동박”, “제련”, “공급망 정책”이라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 정책/자원 narrative가 실제 offtake, long-term supply, tolling/smelting margin, inventory/cost pass-through, FCF, EPS revision으로 내려오는지다.

```text
strategic resource / policy supply headline
  → offtake or supply contract / resource access / processing capacity
  → shipment cadence / price pass-through / inventory valuation
  → smelting or material margin / FCF / EPS revision
  → stock-web 1D OHLC forward path
```

전략자원 정책은 지도 위에 그어진 광맥 표시와 같다. 지도에 광맥이 있어도 굴착권, 운송로, 제련 설비, 고객 offtake, 마진 계약이 연결되지 않으면 현금은 나오지 않는다. C16은 “자원이 중요하다”와 “그 자원이 회사 이익으로 들어온다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["010130","005490","336370","003670"],"profile_paths":["atlas/symbol_profiles/010/010130.json","atlas/symbol_profiles/005/005490.json","atlas/symbol_profiles/336/336370.json","atlas/symbol_profiles/003/003670.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv","atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv","atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv"],"validation_scope":"2024 trigger-level forward path; 010130 and 005490 have zero corporate-action candidates; 336370 caveats are January 2024 so the selected March trigger is after the caveat windows; 003670 caveats are 2015/2021 and outside selected 2024 local windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C16 at 30 rows and asks for strategic resource policy plus real offtake/margin/supply-chain execution expansion.
- Existing registry shows C16 parsed through `R4 loop 96`.
- This output uses `R4 loop 97`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates smelter/resource-control governance squeeze, POSCO lithium/offtake label decay, copper-foil strategic supply optionality, and battery-material capacity peer-transfer risk.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C16-R4L97-01 | 010130 | 고려아연 | 2024-09-13 | 2024-09-13 | 666000 | 1543000 | 655000 | 131.68% | -1.65% | Resource smelter/control squeeze produced extreme MFE, but governance squeeze must not be mistaken for normal offtake-margin bridge. |
| C16-R4L97-02 | 005490 | POSCO홀딩스 | 2024-03-04 | 2024-03-04 | 458000 | 471000 | 309000 | 2.84% | -32.53% | Lithium/resource policy label failed without verified offtake, price, and FCF bridge. |
| C16-R4L97-03 | 336370 | 솔루스첨단소재 | 2024-03-27 | 2024-03-27 | 16970 | 21700 | 11200 | 27.87% | -34.00% | Copper-foil strategic supply optionality generated MFE, but call-off/margin risk later dominated. |
| C16-R4L97-04 | 003670 | 포스코퓨처엠 | 2024-09-02 | 2024-09-02 | 246500 | 264000 | 201000 | 7.10% | -18.46% | Battery-material capacity/resource policy label had weak MFE and needs its own supply/offtake cash bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C16-R4L97-01","round":"R4","loop":"97","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RESOURCE_SMELTER_CONTROL_GOVERNANCE_SQUEEZE_NOT_NORMAL_OFFTAKE_BRIDGE","symbol":"010130","name":"고려아연","trigger_type":"resource_smelter_control_governance_squeeze_not_normal_offtake_bridge","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000,"peak_price":1543000,"peak_date":"2024-10-29","trough_price":655000,"trough_date":"2024-09-13","mfe_pct":131.68,"mae_pct":-1.65,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Special_event_cap_or_Stage3-Yellow_with_governance_squeeze_guard","residual_flag":"resource_control_price_path_extreme_but_not_normal_supply_margin_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|010130|resource_smelter_control_governance_squeeze_not_normal_offtake_bridge|2024-09-13"}
{"row_type":"trigger","case_id":"C16-R4L97-02","round":"R4","loop":"97","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_POLICY_OFFTAKE_FCF_FALSE_STAGE2","symbol":"005490","name":"POSCO홀딩스","trigger_type":"lithium_resource_policy_offtake_fcf_false_stage2","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":458000,"peak_price":471000,"peak_date":"2024-03-05","trough_price":309000,"trough_date":"2024-08-05","mfe_pct":2.84,"mae_pct":-32.53,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"strategic_lithium_resource_label_failed_without_offtake_price_FCF_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|lithium_resource_policy_offtake_fcf_false_stage2|2024-03-04"}
{"row_type":"trigger","case_id":"C16-R4L97-03","round":"R4","loop":"97","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_FOIL_STRATEGIC_SUPPLY_OPTIONALITY_HIGH_MAE_GUARD","symbol":"336370","name":"솔루스첨단소재","trigger_type":"copper_foil_strategic_supply_optionality_high_mae_guard","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":16970,"peak_price":21700,"peak_date":"2024-04-12","trough_price":11200,"trough_date":"2024-09-10","mfe_pct":27.87,"mae_pct":-34.00,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"strategic_copper_foil_supply_optional_MFE_but_delivery_calloff_margin_bridge_required","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|336370|copper_foil_strategic_supply_optionality_high_mae_guard|2024-03-27"}
{"row_type":"trigger","case_id":"C16-R4L97-04","round":"R4","loop":"97","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"BATTERY_MATERIAL_RESOURCE_POLICY_CAPACITY_PEER_TRANSFER_FALSE_STAGE2","symbol":"003670","name":"포스코퓨처엠","trigger_type":"battery_material_resource_policy_capacity_peer_transfer_false_stage2","trigger_date":"2024-09-02","entry_date":"2024-09-02","entry_price":246500,"peak_price":264000,"peak_date":"2024-09-30","trough_price":201000,"trough_date":"2024-09-10","mfe_pct":7.10,"mae_pct":-18.46,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"material_capacity_policy_label_should_not_inherit_resource_control_score_without_cash_margin_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|003670|battery_material_resource_policy_capacity_peer_transfer_false_stage2|2024-09-02"}
```

## 6. Score-return alignment

### 6.1 Resource-control squeeze is not ordinary resource-margin proof

`010130` is the extreme positive path, but it is also a boundary case. The price path shows how strategic smelter/resource control can create a massive move. However, this should not be credited as a normal offtake-margin bridge. The model needs a governance/event-squeeze guard so the scorer does not confuse control premium with ordinary resource supply execution.

### 6.2 Lithium/resource policy label failure

`005490` is the clean false-stage row. A broad strategic lithium/resource policy narrative had almost no forward MFE after the selected trigger and later produced deep MAE. This says C16 should require offtake, realized price, cost curve, and FCF evidence before promoting large resource-platform labels.

### 6.3 Copper-foil optionality and material peer-transfer risk

`336370` and `003670` show the middle and weak families. Copper-foil strategic supply can move when the market sees optionality, but high MAE requires a delivery/margin guard. Battery-material resource/capacity names should not inherit the score of resource-control or cell-maker policy beneficiaries unless their own shipment and cash-conversion bridge is visible.

## 7. Raw component score simulation

| symbol | policy/resource evidence | offtake/supply bridge | price pass-through / inventory | margin/FCF bridge | price confirmation | MAE/event guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 010130 | 24 | 11 | 10 | 8 | 25 | -6 | 72 | Special-event Yellow with governance guard |
| 005490 | 18 | 5 | 4 | 3 | 1 | -16 | 15 | Stage2/local 4B watch |
| 336370 | 17 | 9 | 7 | 5 | 15 | -16 | 37 | Yellow optionality with high-MAE guard |
| 003670 | 14 | 6 | 5 | 3 | 4 | -9 | 23 | Stage2/local 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c16_strategy_resource_requires_offtake_margin_fcf_bridge","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage2_required_bridge","rule":"Do not promote strategic resource/policy/lithium/copper/nickel labels above Stage2 unless offtake, supply contract, resource access, processing capacity, price pass-through, inventory valuation, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["005490","003670"],"counterbalanced_by":["010130","336370"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_resource_control_governance_squeeze_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"special_event_cap_guard","rule":"Resource-control or governance-squeeze paths can be very positive, but should be marked special-event-cap unless ordinary supply, offtake, smelting margin, and cash-conversion evidence is separately verified.","supporting_cases":["010130"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_copper_foil_optional_high_mae_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage2_to_yellow_with_high_MAE_guardrail","rule":"Copper-foil/resource-supply optionality can be Yellow only when delivery, call-off, price pass-through, and margin conversion are visible; high MAE blocks Green.","supporting_cases":["336370"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_resource_policy_false_stage2_guard","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"local_4b_watch_guard","rule":"Broad lithium/resource policy or battery-material capacity labels with small MFE and large MAE should remain local 4B watch or false Stage2 until offtake and FCF evidence repairs the row.","supporting_cases":["005490","003670"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","round":"R4","loop":"97","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C16 needs sharper separation between special resource-control/governance squeeze, strategic resource policy labels, and actual offtake/margin/FCF execution.","candidate_patch_axes":["stage2_required_bridge","special_event_cap_guard","stage2_to_yellow_with_high_MAE_guardrail","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","sample_count":4,"avg_mfe_pct":42.37,"avg_mae_pct":-21.66,"median_mfe_pct":17.49,"median_mae_pct":-25.50,"interpretation":"C16 can show explosive upside in resource-control special events, but ordinary strategic-resource labels produce poor asymmetry without offtake, delivery, margin and FCF bridge."}
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
- Ingest this C16 R4 loop 97 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c16_strategy_resource_requires_offtake_margin_fcf_bridge -> stage2_required_bridge
  2. c16_resource_control_governance_squeeze_guard -> special_event_cap_guard
  3. c16_copper_foil_optional_high_mae_guard -> stage2_to_yellow_with_high_MAE_guardrail
  4. c16_resource_policy_false_stage2_guard -> local_4b_watch_guard

Expected behavior:
- Strategic resource/policy vocabulary alone should not create Green.
- Offtake, supply contract, resource access, processing capacity, price pass-through, margin, FCF or EPS revision can justify Stage3-Yellow.
- Resource-control/governance squeeze paths must be tagged as special-event-cap unless ordinary supply-margin evidence is separately verified.
```
