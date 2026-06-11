# E2R Stock-Web v12 Residual Research — R1 loop 98 / L1 / C04

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 98
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_PREFERRED_BIDDER_PROJECT_AWARD_LEGAL_FINAL_CONTRACT_BRIDGE_VS_POLICY_SPIKE_EVENT_CAP
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - high_MAE_guardrail
  - nuclear_project_legal_delay_timing_test
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` 전용 residual research다.

C04는 “원전 정책/수주 기대/우선협상대상자”라는 headline을 곧바로 Green으로 바꾸는 bucket이 아니다. C04의 핵심은 다음 다리를 확인하는 것이다.

```text
nuclear policy / preferred bidder / project award headline
  → final contract / legal appeal risk / project timeline
  → company-specific scope / margin / revenue timing
  → stock-web 1D OHLC forward path
```

원전 테마는 발전소처럼 긴 시간축을 가진다. 불이 켜지는 순간은 headline이지만, 전기가 계통에 들어오는 순간은 final contract와 수행범위가 확정될 때다. 이번 샘플은 그 사이의 legal/final-contract gap을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["034020","052690","051600","083650"],"profile_paths":["atlas/symbol_profiles/034/034020.json","atlas/symbol_profiles/052/052690.json","atlas/symbol_profiles/051/051600.json","atlas/symbol_profiles/083/083650.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv","atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv"],"validation_scope":"2024-07-18 trigger family with 180D local forward window through 2025-01-14 where available; old corporate-action profile caveats outside local windows are not local rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C04 at 31 rows and asks for preferred-bidder/policy headline versus final contract/legal delay separation.
- Existing registry shows C04 latest parsed file at `R1 loop 97`.
- This output uses `R1 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file uses four 2024 paths: `034020`, `052690`, `051600`, `083650`.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C04-R1L98-01 | 034020 | 두산에너빌리티 | 2024-07-18 | 2024-07-18 | 21000 | 25000 | 15150 | 19.05% | -27.86% | Large-cap nuclear EPC/equipment proxy: event spike, then legal/final-contract gap drawdown. |
| C04-R1L98-02 | 052690 | 한전기술 | 2024-07-18 | 2024-07-18 | 82000 | 98100 | 49900 | 19.63% | -39.15% | Design/project scope proxy: huge policy spike but weak durability without final contract timeline. |
| C04-R1L98-03 | 051600 | 한전KPS | 2024-07-18 | 2024-07-18 | 38900 | 49100 | 35850 | 26.22% | -7.84% | Maintenance/operation scope behaves better; recurring service bridge dampens legal-delay drawdown. |
| C04-R1L98-04 | 083650 | 비에이치아이 | 2024-07-18 | 2024-07-18 | 8810 | 19920 | 7000 | 126.11% | -20.54% | Smaller project/equipment optionality eventually repriced, but only after deep MAE and later confirmation. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C04-R1L98-01","round":"R1","loop":"98","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_EPC_EQUIPMENT_PREFERRED_BIDDER_EVENT_CAP","symbol":"034020","name":"두산에너빌리티","trigger_type":"nuclear_preferred_bidder_policy_spike_event_cap","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":21000,"peak_price":25000,"peak_date":"2024-07-18","trough_price":15150,"trough_date":"2024-08-05","mfe_pct":19.05,"mae_pct":-27.86,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap_not_Green","residual_flag":"counterexample_policy_spike_without_final_contract_margin_bridge","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|034020|nuclear_preferred_bidder_policy_spike_event_cap|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L98-02","round":"R1","loop":"98","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_DESIGN_PROJECT_SCOPE_POLICY_SPIKE_LEGAL_DELAY","symbol":"052690","name":"한전기술","trigger_type":"nuclear_design_project_scope_policy_spike_legal_delay","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":82000,"peak_price":98100,"peak_date":"2024-07-18","trough_price":49900,"trough_date":"2024-12-09","mfe_pct":19.63,"mae_pct":-39.15,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"high_MAE_policy_design_scope_without_durable_contract_timeline","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|nuclear_design_project_scope_policy_spike_legal_delay|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L98-03","round":"R1","loop":"98","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_MAINTENANCE_OPERATION_RECURRING_SERVICE_BRIDGE","symbol":"051600","name":"한전KPS","trigger_type":"nuclear_maintenance_operation_recurring_service_bridge","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":38900,"peak_price":49100,"peak_date":"2024-12-03","trough_price":35850,"trough_date":"2024-08-05","mfe_pct":26.22,"mae_pct":-7.84,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_URLs","residual_flag":"positive_service_bridge_lower_MAE_than_policy_pure_play","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|nuclear_maintenance_operation_recurring_service_bridge|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L98-04","round":"R1","loop":"98","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_EQUIPMENT_OPTIONALITY_LATE_CONFIRMATION_HIGH_MAE","symbol":"083650","name":"비에이치아이","trigger_type":"nuclear_equipment_optionality_late_confirmation","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":8810,"peak_price":19920,"peak_date":"2024-11-22","trough_price":7000,"trough_date":"2024-09-09","mfe_pct":126.11,"mae_pct":-20.54,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"large_MFE_after_deep_MAE_requires_project_scope_confirmation","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|083650|nuclear_equipment_optionality_late_confirmation|2024-07-18"}
```

## 6. Score-return alignment

### 6.1 Policy spike without contract bridge

`034020` and `052690` show the classic C04 failure mode. The price responds to a major nuclear project/policy headline, but when the model cannot see final contract timing, legal appeal risk resolution, company-specific scope, or margin recognition, the forward path becomes a high-MAE event spike. These should not become automatic Stage3-Green rows.

### 6.2 Recurring service bridge

`051600` behaves differently. Maintenance/operation exposure is less binary than EPC/design optionality. The drawdown is much smaller and the later path has steadier follow-through. This suggests C04 should treat maintenance/service scope differently from pure project-award headlines.

### 6.3 Late confirmation optionality

`083650` shows why C04 cannot simply reject all legal-delay headlines. Equipment optionality can reprice hard, but the path first goes through deep MAE. This is a position-sizing and staging problem: Stage2/Yellow can be allowed, but Green should wait for project scope, order, or revenue bridge.

## 7. Raw component score simulation

| symbol | policy/project evidence | final contract/legal clarity | company-specific scope | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 034020 | 21 | 6 | 12 | 9 | -12 | 36 | Event-cap / local 4B watch |
| 052690 | 23 | 5 | 14 | 8 | -14 | 36 | Event-cap / high-MAE watch |
| 051600 | 17 | 12 | 18 | 17 | -4 | 60 | Stage3-Yellow candidate |
| 083650 | 18 | 8 | 16 | 24 | -10 | 56 | Stage2/Yellow with high-MAE guardrail |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c04_nuclear_policy_requires_final_contract_or_scope_bridge","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage2_required_bridge","rule":"Do not promote nuclear policy/preferred-bidder headlines above Stage2 unless final contract timeline, legal-risk resolution, company-specific scope, or revenue/margin bridge is visible.","supporting_cases":["034020","052690"],"counterbalanced_by":["051600","083650"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_policy_spike_high_mae_guardrail","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"local_4b_watch_guard","rule":"If the first move is a price-only nuclear policy spike and no final-contract/legal clarity exists, cap at event-cap/local 4B watch until non-price bridge arrives.","supporting_cases":["034020","052690"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_service_scope_positive_delta","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage3_yellow_candidate_delta","rule":"Recurring nuclear maintenance/service scope may deserve stronger Stage3-Yellow treatment than pure project-award headlines when MAE is contained and forward path confirms.","supporting_cases":["051600"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_equipment_optionality_late_confirmation","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage2_to_yellow_with_position_guardrail","rule":"Nuclear equipment optionality can create large later MFE, but if early MAE is deep, Green should wait for order/project-scope confirmation.","supporting_cases":["083650"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","round":"R1","loop":"98","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C04 should distinguish nuclear policy/preferred-bidder headlines from final-contract/legal clarity and recurring service/equipment scope.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","sample_count":4,"avg_mfe_pct":47.75,"avg_mae_pct":-23.85,"median_mfe_pct":22.93,"median_mae_pct":-24.20,"interpretation":"C04 can produce large MFE, but policy-only spikes have severe MAE unless final contract, service scope, or equipment order bridge is visible."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - local 2024/2025 OHLC rows were checked from stock-web tradable shards
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C04 R1 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c04_nuclear_policy_requires_final_contract_or_scope_bridge -> stage2_required_bridge
  2. c04_policy_spike_high_mae_guardrail -> local_4b_watch_guard
  3. c04_service_scope_positive_delta -> stage3_yellow_candidate_delta
  4. c04_equipment_optionality_late_confirmation -> stage2_to_yellow_with_position_guardrail

Expected behavior:
- Nuclear policy / preferred-bidder vocabulary alone should not create Green.
- Final contract, legal clarity, company-specific scope, or revenue/margin bridge can permit Stage3-Yellow.
- Maintenance/service scope can be treated more constructively than pure project-award optionality.
- Deep-MAE equipment optionality requires sizing/staging guardrails before any Green promotion.
```
