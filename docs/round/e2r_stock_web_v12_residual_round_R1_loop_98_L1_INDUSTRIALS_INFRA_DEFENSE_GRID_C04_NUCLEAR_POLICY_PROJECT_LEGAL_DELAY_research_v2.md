# E2R Stock-Web v12 Residual Research — R1 loop 98 / L1 / C04

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 98
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_EPC_DESIGN_OM_PROJECT_BRIDGE_VS_POLICY_HEADLINE_AND_LEGAL_DELAY_HIGH_MAE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - policy_headline_to_final_contract_bridge_test
  - legal_delay_and_project_timing_guardrail
  - intraday_spike_high_MAE_guardrail
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

C04는 “원전 정책”, “우선협상대상자”, “체코 원전”, “SMR”, “원전 재개”라는 headline만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 정책 headline이 실제 최종계약, EPC 범위, 기자재 납품, 설계·O&M 매출, 법적 지연 리스크, working capital, OPM/FCF로 내려오는지다.

```text
nuclear policy / preferred bidder headline
  → final contract / EPC scope / legal challenge status
  → delivery schedule / engineering or O&M revenue recognition
  → margin / working capital / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

원전 정책 headline은 발전소 부지에 꽂힌 깃발과 같다. 깃발이 꽂혔다고 전기가 흐르지는 않는다. 최종계약, 법적 분쟁 해소, 설계·기자재·정비의 실제 매출 인식이 송전선처럼 이어져야 이익이 된다. C04는 깃발과 송전선을 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["034020","052690","051600","083650"],"profile_paths":["atlas/symbol_profiles/034/034020.json","atlas/symbol_profiles/052/052690.json","atlas/symbol_profiles/051/051600.json","atlas/symbol_profiles/083/083650.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv","atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv"],"validation_scope":"2024 trigger-level forward path; 052690 and 051600 have zero corporate-action candidates; 034020 caveats are 2019/2020 and outside the selected 2024 windows; 083650 old caveats are outside the selected 2024 windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C04 at 31 rows and asks for preferred bidder / policy headline versus final contract / legal delay separation.
- Existing registry shows C04 parsed through `R1 loop 97`.
- This output uses `R1 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file focuses on July 2024 Czech-nuclear policy spike mechanics: main equipment/EPC, engineering/design, O&M, and small EPC/supplier optionality.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C04-R1L98-01 | 034020 | 두산에너빌리티 | 2024-07-18 | 2024-07-18 | 21000 | 25000 | 15150 | 19.05% | -27.86% | Main equipment/EPC policy spike had MFE but failed without final contract and margin bridge. |
| C04-R1L98-02 | 052690 | 한전기술 | 2024-07-18 | 2024-07-18 | 82000 | 98100 | 61600 | 19.63% | -24.88% | Engineering/design headline had sharp spike but legal/final-contract guardrail is required. |
| C04-R1L98-03 | 051600 | 한전KPS | 2024-07-18 | 2024-07-18 | 38900 | 47450 | 35850 | 21.98% | -7.84% | O&M/maintenance exposure had better drawdown control, but revenue bridge still needed. |
| C04-R1L98-04 | 083650 | 비에이치아이 | 2024-07-18 | 2024-07-18 | 8810 | 11880 | 7100 | 34.85% | -19.41% | Small EPC/boiler supplier optionality had MFE but high-MAE event-cap risk remains. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C04-R1L98-01","round":"R1","loop":"98","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_MAIN_EQUIPMENT_EPC_POLICY_SPIKE_HIGH_MAE_GUARD","symbol":"034020","name":"두산에너빌리티","trigger_type":"nuclear_main_equipment_epc_policy_spike_high_mae_guard","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":21000,"peak_price":25000,"peak_date":"2024-07-18","trough_price":15150,"trough_date":"2024-08-05","mfe_pct":19.05,"mae_pct":-27.86,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_Yellow_with_legal_delay_guard","residual_flag":"policy_headline_spike_without_final_contract_margin_bridge_high_MAE","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|034020|nuclear_main_equipment_epc_policy_spike_high_mae_guard|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L98-02","round":"R1","loop":"98","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_ENGINEERING_DESIGN_POLICY_HEADLINE_LEGAL_DELAY_GUARD","symbol":"052690","name":"한전기술","trigger_type":"nuclear_engineering_design_policy_headline_legal_delay_guard","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":82000,"peak_price":98100,"peak_date":"2024-07-18","trough_price":61600,"trough_date":"2024-08-05","mfe_pct":19.63,"mae_pct":-24.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_final_contract_guard","residual_flag":"engineering_design_event_needs_final_contract_and_revenue_recognition_bridge","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|nuclear_engineering_design_policy_headline_legal_delay_guard|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L98-03","round":"R1","loop":"98","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_OM_MAINTENANCE_REVENUE_BRIDGE_CONTROLLED_MAE","symbol":"051600","name":"한전KPS","trigger_type":"nuclear_om_maintenance_revenue_bridge_controlled_mae","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":38900,"peak_price":47450,"peak_date":"2024-07-18","trough_price":35850,"trough_date":"2024-08-05","mfe_pct":21.98,"mae_pct":-7.84,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_O&M_revenue_URLs","residual_flag":"better_controlled_OM_path_but_requires_revenue_contract_bridge","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|nuclear_om_maintenance_revenue_bridge_controlled_mae|2024-07-18"}
{"row_type":"trigger","case_id":"C04-R1L98-04","round":"R1","loop":"98","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"SMALL_EPC_SUPPLIER_NUCLEAR_OPTIONALITY_EVENT_CAP_HIGH_MAE","symbol":"083650","name":"비에이치아이","trigger_type":"small_epc_supplier_nuclear_optionality_event_cap_high_mae","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":8810,"peak_price":11880,"peak_date":"2024-10-24","trough_price":7100,"trough_date":"2024-08-05","mfe_pct":34.85,"mae_pct":-19.41,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_Stage2_to_Yellow_with_high_MAE_guard","residual_flag":"small_supplier_optionality_requires_order_scope_margin_bridge_before_promotion","dedupe_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|083650|small_epc_supplier_nuclear_optionality_event_cap_high_mae|2024-07-18"}
```

## 6. Score-return alignment

### 6.1 Policy spike without contract bridge

`034020` and `052690` are the core C04 warning pair. Both reacted sharply to the nuclear policy/preferred-bidder catalyst, but the forward path quickly exposed deep drawdown. The model should therefore refuse Green until final contract, legal-challenge status, EPC scope, revenue recognition, and OPM/FCF bridge are visible.

### 6.2 O&M is different from EPC headline beta

`051600` had a better MAE profile than the main equipment and design names. That suggests C04 should not treat all nuclear-policy names as one beta basket. O&M/maintenance names can be more stable, but still need actual maintenance scope and recurring revenue evidence before promotion.

### 6.3 Small supplier optionality

`083650` shows a classic optionality path. The small supplier can create MFE after the event, but the drawdown and delay risk are too large for Green. This row should be event-cap or Yellow only after actual order scope and margin visibility appears.

## 7. Raw component score simulation

| symbol | policy/project evidence | final contract/legal bridge | revenue recognition | margin/FCF bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 034020 | 23 | 7 | 8 | 5 | 10 | -13 | 40 | Stage2/Yellow with legal-delay guard |
| 052690 | 22 | 7 | 8 | 5 | 10 | -12 | 40 | Stage2/Yellow with final-contract guard |
| 051600 | 18 | 12 | 14 | 10 | 13 | -4 | 63 | Stage3-Yellow candidate pending O&M proof |
| 083650 | 17 | 6 | 6 | 4 | 18 | -10 | 41 | Event-cap / Yellow with high-MAE guard |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c04_policy_headline_requires_final_contract_legal_margin_bridge","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage2_required_bridge","rule":"Do not promote nuclear policy/preferred-bidder/project headlines above Stage2 unless final contract, legal challenge status, EPC scope, delivery schedule, revenue recognition, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["034020","052690"],"counterbalanced_by":["051600","083650"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_OM_revenue_bridge_positive_delta","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"stage3_yellow_candidate_delta","rule":"O&M/maintenance nuclear names with verified recurring scope and revenue bridge can receive Stage3-Yellow treatment, but Green still requires contract and margin proof.","supporting_cases":["051600"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_small_supplier_optionality_event_cap_guard","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"local_4b_watch_guard","rule":"Small EPC/supplier nuclear optionality should remain event-cap or local 4B watch when order scope, delivery, and margin bridge are not verified.","supporting_cases":["083650"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c04_intraday_policy_spike_high_MAE_guard","scope":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","candidate_action":"high_MAE_guardrail","rule":"If a nuclear policy trigger produces same-day MFE but later deep MAE before contract evidence arrives, cap at Stage2/Yellow and require non-price bridge before promotion.","supporting_cases":["034020","052690","083650"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","round":"R1","loop":"98","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C04 needs sharper separation between nuclear policy/preferred-bidder spikes and final contract, legal-delay, O&M revenue, EPC scope, margin and FCF conversion.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_candidate_delta","local_4b_watch_guard","high_MAE_guardrail"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","sample_count":4,"avg_mfe_pct":23.88,"avg_mae_pct":-20.00,"median_mfe_pct":20.81,"median_mae_pct":-22.15,"interpretation":"C04 policy headlines can create fast MFE, but contract/legal/revenue bridge absence often converts the path into high-MAE Stage2 or event-cap rather than Green."}
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
- Ingest this C04 R1 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c04_policy_headline_requires_final_contract_legal_margin_bridge -> stage2_required_bridge
  2. c04_OM_revenue_bridge_positive_delta -> stage3_yellow_candidate_delta
  3. c04_small_supplier_optionality_event_cap_guard -> local_4b_watch_guard
  4. c04_intraday_policy_spike_high_MAE_guard -> high_MAE_guardrail

Expected behavior:
- Nuclear policy/preferred-bidder vocabulary alone should not create Green.
- Final contract, legal challenge status, EPC scope, delivery schedule, revenue recognition, margin, FCF, or EPS revision can justify Stage3-Yellow.
- Same-day policy spike with later deep MAE should remain Stage2/Yellow or event-cap until non-price bridge is verified.
```
