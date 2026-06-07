# E2R v12 Stock-Web Historical Calibration Research — R1 / C02 Power Grid Datacenter CAPEX

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

selected_round: R1
selected_loop: 101
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_WIRE_CABLE_PRICE_ONLY_BLOWOFF
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
auto_selected_coverage_gap: C02 rows 24, 30-row minimum까지 6 부족
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
```

## 1. Scope lock

이번 파일은 현재 종목 추천이나 live watchlist가 아니다. 목적은 `Songdaiki/stock-web`의 실제 1D OHLCV row로 C02 전력망·데이터센터 CAPEX 아키타입의 trigger-level residual을 보강하는 것이다.

C02는 단순 “전력 테마”가 아니다. 실제 calibration에서는 다음 세 축을 분리해야 한다.

```text
1. transformer / grid equipment backlog and delivery bridge
2. datacenter or grid CAPEX cycle with capacity lock / ASP / margin bridge
3. wire/cable price-only blowoff without backlog-to-margin proof
```

No-Repeat 기준으로 C02는 Priority 0이며, 최신 장부상 24 rows로 30-row minimum까지 6 rows가 부족하다. 따라서 이번 연구는 C02 자체를 피하지 않고, hard duplicate가 되기 쉬운 `canonical_archetype_id + symbol + trigger_type + entry_date` 반복을 피하면서 새 trigger family와 counterexample을 추가한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","source_repo":"Songdaiki/stock-web","manifest_path":"atlas/manifest.json","source_name":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap","min_date":"1995-05-02","max_date":"2026-02-20","tradable_row_count":14354401,"symbol_count":5414,"active_like_symbol_count":2868,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","validation_status":"pass"}
{"row_type":"price_source_validation","symbol":"033100","name":"제룡전기","profile_path":"atlas/symbol_profiles/033/033100.json","price_path":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv","status_inferred":"active_like","corporate_action_caveat":"profile has historical raw discontinuity; 2024 selected window is used as tradable_raw calibration only","validation_status":"usable_with_raw_price_caveat"}
{"row_type":"price_source_validation","symbol":"103590","name":"일진전기","profile_path":"atlas/symbol_profiles/103/103590.json","price_path":"atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv","status_inferred":"active_like","corporate_action_caveat":"2024-02-13 corporate-action candidate exists; selected entry is after this date and treated with raw-price caveat","validation_status":"usable_with_raw_price_caveat"}
{"row_type":"price_source_validation","symbol":"006340","name":"대원전선","profile_path":"atlas/symbol_profiles/006/006340.json","price_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","status_inferred":"active_like","corporate_action_caveat":"share-count change observed in 2024 rows; selected case is used as price-path stress test, not valuation proof","validation_status":"usable_for_counterexample_with_raw_price_caveat"}
```

## 3. Case set summary

| case_id | symbol | name | trigger family | entry date | entry price | peak date / high | MFE | worst low | MAE | label |
|---|---:|---|---|---|---:|---|---:|---:|---:|---|
| C02-R1L101-01 | 033100 | 제룡전기 | small transformer backlog / grid export CAPA bridge | 2024-03-04 | 27,200 | 2024-07-11 / 100,700 | +270.22% | 25,700 | -5.51% | positive |
| C02-R1L101-02 | 103590 | 일진전기 | cable + transformer order backlog bridge | 2024-03-18 | 17,200 | 2024-05-29 / 30,250 | +75.87% | 16,420 | -4.53% | positive |
| C02-R1L101-03 | 006340 | 대원전선 | wire/cable price-only blowoff | 2024-05-13 | 4,885 | 2024-05-14 / 5,260 | +7.68% | 3,285 | -32.75% | counterexample |

계산 방식은 단순하다. Entry는 trigger 다음 calibration 가능한 close 또는 trigger close로 고정하고, 이후 관측 window의 high/low로 MFE/MAE를 계산했다. 미래 가격은 그 시점 점수 산정에는 쓰지 않고, 오직 사후 calibration label과 residual rule 후보의 근거로만 쓴다.

## 4. Case narratives

### 4.1 C02-R1L101-01 — 033100 제룡전기: transformer backlog/CAPA bridge가 가격경로로 확인된 positive

제룡전기는 2024-03-04에 27,200원 close로 강한 grid-transformer repricing 구간에 들어갔다. 같은 날 stock-web row는 open 21,750, high 27,200, low 21,750, close 27,200, value 약 149.3B KRW로 급격한 liquidity regime change를 보여준다. 이후 2024-04-24 high 62,000, 2024-05-10 close 74,900, 2024-07-11 high 100,700까지 이어졌다.

이 케이스의 핵심은 단순 price spike가 아니라 “소형 변압기/전력기기 CAPA 부족 → backlog visibility → ASP/margin bridge”로 압축되는 C02 본류라는 점이다. e2r_2_1_stock_web_calibrated가 global price-only blowoff를 막는 것은 맞지만, C02에서는 price surge를 무조건 4B로 밀기보다 order/backlog/CAPA bridge가 붙으면 Stage2-Actionable 또는 Stage3-Yellow 후보로 남겨야 한다.

Residual: C02 특화 rule이 없으면 small-cap transformer rerating은 과열로만 보일 수 있다. 그러나 MAE -5.51% 대비 MFE +270.22%는 “early bridge recognition”의 가치가 매우 컸다.

### 4.2 C02-R1L101-02 — 103590 일진전기: transformer + cable backlog bridge가 price path로 검증된 positive

일진전기는 2024-03-18 close 17,200을 entry로 보면, 이후 2024-03-27 high 21,450, 2024-04-26 high 23,900, 2024-05-29 high 30,250까지 상승했다. 이 구간의 MAE는 2024-03-19 low 16,420 기준 -4.53% 수준이고, peak MFE는 +75.87%다.

이 케이스는 C02 내부에서도 “전선 테마”가 아니라 cable + transformer order backlog bridge에 가깝다. 전력망 CAPEX가 실적 bridge로 넘어갈 때 cable은 단순 구리/전선 beta가 아니라 고압·초고압/변압기 수요와 묶여야 한다.

Residual: global Stage2 bonus는 도움이 되지만, C02에서는 `grid_backlog_to_margin_bridge`가 없으면 일진전기형 transition을 과소평가하거나 뒤늦게만 잡는다. 반대로 같은 전선 label이어도 order backlog 없이 거래대금만 붙는 경우는 아래 006340처럼 방어해야 한다.

### 4.3 C02-R1L101-03 — 006340 대원전선: wire/cable price-only blowoff counterexample

대원전선은 2024-04-05부터 2024-05-13까지 wire/cable theme liquidity가 크게 터졌다. 하지만 2024-05-13 close 4,885를 late entry로 보면, 다음날 high 5,260으로 MFE는 +7.68%에 그친 반면 이후 2024-06-10 low 3,285까지 밀려 MAE -32.75%가 발생했다. 2024-05-13 이후 price path는 “전력망 theme” label만으로 Stage2-Actionable을 주면 안 된다는 반례다.

이 case는 C02의 방어축이다. C02라고 해서 모든 전선/전력 label을 backlog bridge로 취급하면 false Stage2가 늘어난다. 특히 대형 수주·CAPA lock·ASP/margin bridge가 없고, 거래대금과 가격만 먼저 간 경우는 full 4B requires non-price evidence guard가 유지되어야 한다.

## 5. Trigger rows

```jsonl
{"row_type":"trigger","case_id":"C02-R1L101-01","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"101","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_WIRE_CABLE_PRICE_ONLY_BLOWOFF","symbol":"033100","name":"제룡전기","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":27200.0,"trigger_type":"transformer_grid_backlog_capa_bridge","evidence_family":"grid_transformer_backlog_capa_asp_margin_bridge","path_label":"positive","peak_date":"2024-07-11","peak_high":100700.0,"worst_date":"2024-03-05","worst_low":25700.0,"mfe_pct":270.22,"mae_pct":-5.51,"calibration_usable":true,"duplicate_check_key":"C02_POWER_GRID_DATACENTER_CAPEX|033100|transformer_grid_backlog_capa_bridge|2024-03-04|2024-03-04","source_proxy_only":true}
{"row_type":"trigger","case_id":"C02-R1L101-02","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"101","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_WIRE_CABLE_PRICE_ONLY_BLOWOFF","symbol":"103590","name":"일진전기","trigger_date":"2024-03-18","entry_date":"2024-03-18","entry_price":17200.0,"trigger_type":"cable_transformer_backlog_bridge","evidence_family":"grid_cable_transformer_order_revenue_margin_bridge","path_label":"positive","peak_date":"2024-05-29","peak_high":30250.0,"worst_date":"2024-03-19","worst_low":16420.0,"mfe_pct":75.87,"mae_pct":-4.53,"calibration_usable":true,"duplicate_check_key":"C02_POWER_GRID_DATACENTER_CAPEX|103590|cable_transformer_backlog_bridge|2024-03-18|2024-03-18","source_proxy_only":true}
{"row_type":"trigger","case_id":"C02-R1L101-03","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"101","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_GRID_BACKLOG_DATACENTER_CAPEX_BRIDGE_VS_WIRE_CABLE_PRICE_ONLY_BLOWOFF","symbol":"006340","name":"대원전선","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":4885.0,"trigger_type":"wire_cable_price_only_blowoff","evidence_family":"price_volume_wire_cable_theme_without_backlog_margin_bridge","path_label":"counterexample","peak_date":"2024-05-14","peak_high":5260.0,"worst_date":"2024-06-10","worst_low":3285.0,"mfe_pct":7.68,"mae_pct":-32.75,"calibration_usable":true,"duplicate_check_key":"C02_POWER_GRID_DATACENTER_CAPEX|006340|wire_cable_price_only_blowoff|2024-05-10|2024-05-13","source_proxy_only":true}
```

## 6. Score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C02-R1L101-01","symbol":"033100","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores":{"order_backlog_visibility":82,"capacity_lock_or_shortage":76,"asp_margin_bridge":72,"eps_revision_proxy":63,"price_only_risk":28,"information_confidence":58},"simulated_stage_without_c02_shadow":"Stage2_or_watch_due_to_price_overheat","simulated_stage_with_c02_shadow":"Stage2-Actionable_to_Stage3-Yellow_candidate","alignment":"improves_positive_capture","reason":"C02-specific transformer backlog/CAPA bridge prevents over-penalizing early non-price-backed rerating."}
{"row_type":"score_simulation","case_id":"C02-R1L101-02","symbol":"103590","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores":{"order_backlog_visibility":76,"capacity_lock_or_shortage":66,"asp_margin_bridge":68,"eps_revision_proxy":60,"price_only_risk":35,"information_confidence":56},"simulated_stage_without_c02_shadow":"Stage2","simulated_stage_with_c02_shadow":"Stage2-Actionable","alignment":"improves_positive_capture","reason":"Cable/transformer bridge is stronger than generic wire theme; MAE stayed shallow while MFE expanded."}
{"row_type":"score_simulation","case_id":"C02-R1L101-03","symbol":"006340","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores":{"order_backlog_visibility":25,"capacity_lock_or_shortage":18,"asp_margin_bridge":20,"eps_revision_proxy":15,"price_only_risk":86,"information_confidence":34},"simulated_stage_without_c02_shadow":"false_Stage2_possible_if_theme_liquidity_overweighted","simulated_stage_with_c02_shadow":"4B_watch_or_reject_positive_stage","alignment":"reduces_false_positive","reason":"Wire/cable price-only blowoff had low MFE and high MAE after late entry."}
```

## 7. Aggregate metric rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"101","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","case_count":3,"trigger_count":3,"positive_case_count":2,"counterexample_count":1,"avg_mfe_pct":117.92,"avg_mae_pct":-14.26,"positive_avg_mfe_pct":173.05,"positive_avg_mae_pct":-5.02,"counterexample_avg_mfe_pct":7.68,"counterexample_avg_mae_pct":-32.75,"interpretation":"C02 works when transformer/cable backlog and CAPA/ASP/margin bridge are visible; wire/cable price-only late entries remain high-MAE false positives."}
{"row_type":"coverage_matrix","round":"R1","loop":"101","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","priority_bucket":"Priority 0","rows_before_from_index":24,"need_to_30_before":6,"new_calibration_usable_triggers":3,"estimated_rows_after_if_ingested":27,"remaining_need_to_30_estimate":3,"coverage_gap_fill_status":"partial_fill"}
```

## 8. Current calibrated profile stress test

Current proxy profile already has three useful global guards.

```text
stage2_actionable_evidence_bonus = +2.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
```

이번 C02 residual은 이 guard를 약화하자는 게 아니다. 오히려 두 칼날을 분리하자는 것이다.

```text
Positive unlock:
  transformer / grid equipment / cable backlog
  + capacity lock or supply shortage
  + ASP/margin or revenue conversion evidence
  + shallow MAE after entry
  => Stage2-Actionable 가능

Negative block:
  wire/cable label
  + price/volume spike only
  + no backlog-to-margin bridge
  + late entry high MAE
  => 4B watch or reject positive stage
```

즉 C02는 “전력 테마 상승”이 아니라 “grid/datacenter CAPEX → order/backlog → delivery → ASP/margin → revision”의 연쇄가 이어져야 한다. 수도관에 물이 찼는지만 보면 안 되고, 밸브가 열려 실제 터빈을 돌리는지를 확인해야 한다.

## 9. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","rule_candidate_id":"c02_grid_backlog_capa_margin_bridge_required_for_stage2_actionable_shadow_only","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"stage2_required_bridge","direction":"tighten_positive_stage_for_price_only_and_unlock_non_price_backlog_bridge","proposed_effect":"Allow Stage2-Actionable only when at least two of backlog/order visibility, capacity lock, ASP/margin bridge, or revenue conversion are present. Price-volume-only wire/cable rallies remain 4B watch.","applies_to_positive_cases":["C02-R1L101-01","C02-R1L101-02"],"applies_to_counterexamples":["C02-R1L101-03"],"production_scoring_changed":false,"handoff_required":true}
{"row_type":"shadow_weight","rule_candidate_id":"c02_full_4b_requires_non_price_evidence_wire_cable_scope_strengthening","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"full_4b_overlay_candidate","direction":"strengthen","proposed_effect":"If wire/cable or generic power-grid label has no concrete backlog/margin bridge and price has already expanded >80% within short window, keep positive stage blocked unless fresh non-price evidence appears.","applies_to_counterexamples":["C02-R1L101-03"],"production_scoring_changed":false,"handoff_required":true}
```

## 10. Residual contribution

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"101","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c02_grid_backlog_capa_margin_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C02 wire/cable price-only blowoff","existing_axis_weakened":null,"current_profile_error_count":2,"positive_case_count":2,"counterexample_count":1,"summary":"C02 needs both an unlock path for transformer/grid backlog cases and a blocking path for wire/cable price-only blowoffs."}
{"row_type":"narrative_only","round":"R1","loop":"101","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","message":"This is not a stock recommendation. Future MFE/MAE is used only for historical calibration, not for as-of-date scoring."}
```

## 11. Novelty / duplicate audit

```text
hard_duplicate_key_format:
  canonical_archetype_id + symbol + trigger_type + entry_date

selected_keys:
  C02_POWER_GRID_DATACENTER_CAPEX|033100|transformer_grid_backlog_capa_bridge|2024-03-04|2024-03-04
  C02_POWER_GRID_DATACENTER_CAPEX|103590|cable_transformer_backlog_bridge|2024-03-18|2024-03-18
  C02_POWER_GRID_DATACENTER_CAPEX|006340|wire_cable_price_only_blowoff|2024-05-10|2024-05-13

soft_duplicate_policy:
  C02 itself is intentionally reused because it is Priority 0.
  Symbol reuse risk is handled by selecting distinct trigger family and entry date.
  Existing C02 registry sample showed a transformer/grid/data-center document but not these exact duplicate keys.
```

## 12. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the research session.

```text
You are the later batch implementation agent for stock_agent.

Input artifact:
- e2r_stock_web_v12_residual_round_R1_loop_101_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md

Task:
1. Parse v12 JSONL rows from the Markdown.
2. Validate schema_family == v12_sector_archetype_residual.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add validated trigger rows to v12 calibration datasets only if they pass existing validation.
5. Do not loosen Stage3-Green thresholds.
6. Consider shadow-only axis:
   - c02_grid_backlog_capa_margin_bridge_required_for_stage2_actionable_shadow_only
   - c02_full_4b_requires_non_price_evidence_wire_cable_scope_strengthening
7. Treat source_proxy_only rows as calibration candidates requiring later URL/evidence repair before production promotion.
8. Keep production_scoring_changed=false unless a separate batch review approves it.
```

## 13. Final execution summary

```text
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
diversity_score_summary: C02 Priority 0 부족권 + transformer/cable backlog positive와 wire/cable price-only counterexample 균형
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
next_recommended_archetypes: C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
