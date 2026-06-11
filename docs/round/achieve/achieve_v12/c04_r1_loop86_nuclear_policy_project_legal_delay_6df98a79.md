# E2R Stock-Web v12 Residual Research — R1 loop 86 / L1 / C04

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 86
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_PROJECT_FINAL_CONTRACT_DELIVERY_MARGIN_BRIDGE_VS_SMALLCAP_POLICY_THEME_LEGAL_DELAY_EVENT_CAP
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill_to_50
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - preferred_bidder_to_final_contract_bridge_test
  - legal_delay_and_final_contract_guardrail
  - nuclear_prime_engineering_OM_separation
  - smallcap_policy_theme_false_stage2_guard
  - project_margin_FCF_bridge_test
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

C04는 “원전 정책”, “우선협상대상자”, “체코 원전”, “SMR”, “원전 수출”, “정책 수혜”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 정책 headline이 실제 final contract, financing, legal appeal/competition challenge, delivery scope, engineering/service workshare, working capital, OPM, FCF, EPS revision으로 내려오는지다.

```text
nuclear policy / preferred bidder / export project headline
  → final EPC or equipment contract / legal appeal clearance
  → scope, delivery schedule, workshare, financing, acceptance
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

원전 우선협상은 거대한 문 앞에서 받은 번호표와 같다. 번호표를 받았다고 터빈이 돌아가고 매출이 찍히는 것은 아니다. 최종계약, 법적 지연, 금융조달, 납품 범위, 검수와 마진이 닫혀야 번호표가 현금으로 바뀐다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["034020","052690","051600","083650","006910"],"profile_paths":["atlas/symbol_profiles/034/034020.json","atlas/symbol_profiles/052/052690.json","atlas/symbol_profiles/051/051600.json","atlas/symbol_profiles/083/083650.json","atlas/symbol_profiles/006/006910.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv","atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv","atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv"],"validation_scope":"2024 Czech nuclear preferred-bidder trigger-level forward path. 034020 caveats end 2020; 052690 and 051600 have zero corporate-action candidates; 083650 caveats end 2015; 006910 caveats end 2016. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C04 at 31 rows and 19 rows short of the 50-row practical calibration target.
- Registry shows C04 parsed through `R1 loop 85`.
- This output uses `R1 loop 86`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file focuses on Czech preferred-bidder shock and separates prime/EPC, engineering, O&M/service, boiler/auxiliary equipment, and smallcap policy-theme rows.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C04-R1L86-01 | 034020 | 두산에너빌리티 | 2024-07-18 | 2024-07-18 | 21000 | 25000 | 15150 | 19.05% | -27.86% | Nuclear prime/equipment preferred-bidder spike faded; final contract and margin bridge required. |
| C04-R1L86-02 | 052690 | 한전기술 | 2024-07-18 | 2024-07-18 | 82000 | 98100 | 61600 | 19.63% | -24.88% | Engineering scope had MFE, but legal/final-contract delay risk created high drawdown. |
| C04-R1L86-03 | 051600 | 한전KPS | 2024-07-18 | 2024-07-18 | 38900 | 47450 | 35850 | 21.98% | -7.84% | O&M/service row was more resilient; Yellow candidate if recurring service scope is verified. |
| C04-R1L86-04 | 083650 | 비에이치아이 | 2024-07-18 | 2024-07-18 | 8810 | 10530 | 7000 | 19.52% | -20.54% | Boiler/auxiliary equipment optionality made MFE but needs workshare/delivery/margin proof. |
| C04-R1L86-05 | 006910 | 보성파워텍 | 2024-07-18 | 2024-07-18 | 3630 | 4280 | 2560 | 17.91% | -29.48% | Smallcap nuclear policy theme spiked, then decayed; local 4B/false Stage2 guard. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C04-R1L86-01","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_PRIME_EQUIPMENT_PREFERRED_BIDDER_FINAL_CONTRACT_MARGIN_BRIDGE","symbol":"034020","name":"두산에너빌리티","trigger_type":"nuclear_prime_equipment_preferred_bidder_final_contract_margin_bridge","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":21000,"peak_price":25000,"peak_date":"2024-07-18","trough_price":15150,"trough_date":"2024-08-05","mfe_pct":19.05,"mae_pct":-27.86,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_final_contract_OPM_FCF_guard","residual_flag":"preferred_bidder_prime_spike_high_MAE_requires_final_contract_scope_margin_FCF_bridge","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|034020|nuclear_prime_equipment_preferred_bidder_final_contract_margin_bridge|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L86-02","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_ENGINEERING_SCOPE_PREFERRED_BIDDER_LEGAL_DELAY_GUARD","symbol":"052690","name":"한전기술","trigger_type":"nuclear_engineering_scope_preferred_bidder_legal_delay_guard","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":82000,"peak_price":98100,"peak_date":"2024-07-18","trough_price":61600,"trough_date":"2024-08-05","mfe_pct":19.63,"mae_pct":-24.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_scope_legal_delay_guard","residual_flag":"engineering_policy_spike_needs_final_scope_legal_clearance_revenue_OPM_bridge","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|nuclear_engineering_scope_preferred_bidder_legal_delay_guard|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L86-03","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_OM_SERVICE_SCOPE_RECURRING_MARGIN_RESILIENT_YELLOW","symbol":"051600","name":"한전KPS","trigger_type":"nuclear_om_service_scope_recurring_margin_resilient_yellow","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":38900,"peak_price":47450,"peak_date":"2024-07-18","trough_price":35850,"trough_date":"2024-08-05","mfe_pct":21.98,"mae_pct":-7.84,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_service_scope_margin_URLs","residual_flag":"OM_service_row_more_resilient_but_requires_recurring_service_scope_OPM_FCF_evidence","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|nuclear_om_service_scope_recurring_margin_resilient_yellow|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L86-04","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_AUXILIARY_EQUIPMENT_WORKSHARE_OPTIONALITY_HIGH_MAE_GUARD","symbol":"083650","name":"비에이치아이","trigger_type":"nuclear_auxiliary_equipment_workshare_optionality_high_mae_guard","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":8810,"peak_price":10530,"peak_date":"2024-07-18","trough_price":7000,"trough_date":"2024-09-09","mfe_pct":19.52,"mae_pct":-20.54,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_workshare_margin_guard","residual_flag":"auxiliary_equipment_optional_MFE_but_requires_final_workshare_delivery_acceptance_OPM_bridge","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|083650|nuclear_auxiliary_equipment_workshare_optionality_high_mae_guard|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L86-05","round":"R1","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"SMALLCAP_NUCLEAR_POLICY_THEME_SPIKE_FALSE_STAGE2_LOCAL_4B","symbol":"006910","name":"보성파워텍","trigger_type":"smallcap_nuclear_policy_theme_spike_false_stage2_local_4b","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":3630,"peak_price":4280,"peak_date":"2024-07-18","trough_price":2560,"trough_date":"2024-08-05","mfe_pct":17.91,"mae_pct":-29.48,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_false_Stage2","residual_flag":"smallcap_nuclear_policy_theme_spike_decayed_without_final_contract_workshare_margin_bridge","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|006910|smallcap_nuclear_policy_theme_spike_false_stage2_local_4b|2024-07-18"}
```

## 6. Score-return alignment

### 6.1 Preferred bidder is not final contract

`034020` and `052690` both had huge intraday spikes on the preferred-bidder trigger, but the full-window forward path quickly opened deep drawdown. C04 should therefore not promote preferred-bidder headlines to Green unless final contract, legal appeal clearance, scope, financing, delivery schedule and margin bridge are visible.

### 6.2 Service/O&M is a different quality bucket

`051600` behaved better than the prime-equipment and engineering spikes. It still needs URL-verified service scope and recurring O&M economics, but the smaller drawdown suggests O&M/service can be a separate Yellow candidate family.

### 6.3 Equipment workshare and smallcap theme need strict caps

`083650` made event-driven MFE but later carried high MAE, so workshare and delivery proof are mandatory. `006910` is the clean false Stage2 row: smallcap policy-theme price action without final contract or workshare evidence should be local 4B or event-cap.

## 7. Raw component score simulation

| symbol | policy/project specificity | final contract/legal clearance | scope/workshare | OPM/FCF bridge | price confirmation | MAE/event-cap guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 034020 | 22 | 6 | 8 | 5 | 9 | -13 | 37 | Stage2→Yellow with contract guard |
| 052690 | 22 | 5 | 9 | 5 | 9 | -12 | 38 | Stage2→Yellow with legal-delay guard |
| 051600 | 17 | 8 | 12 | 8 | 13 | -4 | 54 | Stage3-Yellow candidate |
| 083650 | 17 | 4 | 7 | 4 | 8 | -10 | 30 | Stage2→Yellow high-MAE guard |
| 006910 | 11 | 1 | 2 | 1 | 4 | -14 | 5 | Local 4B / false Stage2 |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c04_preferred_bidder_requires_final_contract_legal_scope_margin_bridge","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage2_required_bridge","rule":"Do not promote nuclear policy/preferred-bidder/export-project labels above Stage2 unless final contract, legal appeal clearance, financing, scope, delivery schedule, workshare, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["034020","052690","083650","006910"],"counterbalanced_by":["051600"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_OM_service_resilient_yellow_delta","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage3_yellow_candidate_delta","rule":"Nuclear O&M/service rows can receive Yellow treatment when recurring service scope, long-term contract, margin and cash bridge are URL-verified.","supporting_cases":["051600"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_prime_engineering_event_cap_guard","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage2_to_yellow_with_contract_guard","rule":"Prime equipment and engineering rows after preferred-bidder headlines should be event-capped until final contract and legal delay risk are resolved.","supporting_cases":["034020","052690"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_auxiliary_equipment_workshare_high_MAE_guard","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage2_to_yellow_with_workshare_guard","rule":"Auxiliary equipment rows need confirmed workshare, delivery acceptance and OPM bridge; high MAE blocks Green even if intraday MFE is large.","supporting_cases":["083650"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_smallcap_policy_theme_false_stage2_guard","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"local_4b_or_false_stage2_guard","rule":"Smallcap nuclear policy-theme rows with event spike and high MAE should stay local 4B unless final contract/workshare/margin evidence repairs the row.","supporting_cases":["006910"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","round":"R1","loop":"86","positive_rows":1,"counterexample_rows":4,"new_symbol_count":5,"primary_residual":"C04 should separate preferred-bidder policy spikes from final-contract/legal-clearance revenue bridges; O&M/service rows appear more resilient, while prime equipment, engineering, auxiliary equipment and smallcap theme rows need event-cap or local 4B guards until workshare and margin evidence appears.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","stage2_to_yellow_with_contract_guard","stage2_to_yellow_with_workshare_guard","local_4b_or_false_stage2_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","sample_count":5,"avg_mfe_pct":19.62,"avg_mae_pct":-22.12,"median_mfe_pct":19.52,"median_mae_pct":-24.88,"interpretation":"C04 preferred-bidder rows produced clear event MFE but poor full-window asymmetry; final contract, legal clearance, workshare, OPM and FCF bridge are mandatory before promotion."}
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
- Ingest this C04 R1 loop 86 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c04_preferred_bidder_requires_final_contract_legal_scope_margin_bridge -> stage2_required_bridge
  2. c04_OM_service_resilient_yellow_delta -> stage3_yellow_candidate_delta
  3. c04_prime_engineering_event_cap_guard -> stage2_to_yellow_with_contract_guard
  4. c04_auxiliary_equipment_workshare_high_MAE_guard -> stage2_to_yellow_with_workshare_guard
  5. c04_smallcap_policy_theme_false_stage2_guard -> local_4b_or_false_stage2_guard

Expected behavior:
- Nuclear policy/preferred-bidder vocabulary alone should not create Green.
- Final contract, legal appeal clearance, financing, scope, delivery schedule, workshare, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Smallcap policy-theme and preferred-bidder spikes should be event-capped until fresh non-price evidence appears.
```
