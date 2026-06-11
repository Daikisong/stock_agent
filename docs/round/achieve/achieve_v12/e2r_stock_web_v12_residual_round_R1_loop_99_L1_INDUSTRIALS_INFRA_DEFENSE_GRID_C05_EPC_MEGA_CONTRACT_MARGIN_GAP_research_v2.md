# E2R Stock-Web v12 Residual Research — R1 loop 99 / L1 / C05

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 99
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: DOMESTIC_CONSTRUCTION_OVERSEAS_EPC_COST_OVERRUN_WORKING_CAPITAL_MARGIN_GAP_VS_CONTRACT_HEADLINE_AND_REBOUND_THEME
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - EPC_contract_to_margin_cash_bridge_test
  - cost_overrun_working_capital_guardrail
  - domestic_construction_rebound_false_stage2_guard
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

이번 파일은 `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` 전용 residual research다.

C05는 “대형 EPC 계약”, “해외 플랜트 수주”, “건설 반등”, “주택 회복”, “저PBR 건설주” 같은 headline을 그대로 Stage3-Green으로 올리는 bucket이 아니다. 핵심은 계약이 실제 공정 진행, 원가 통제, change order, working capital, 미청구공사/매출채권, OPM/FCF/EPS revision으로 내려오는지다.

```text
mega EPC / construction contract headline
  → scope quality / cost-to-complete / change-order protection
  → execution schedule / working capital / receivable and unbilled work
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

EPC 계약은 거대한 설계도와 같다. 설계도 위의 숫자는 커도, 철근·인건비·환율·공정 지연이 새면 마진은 바닥 배수구로 빠진다. C05는 “계약서 크기”와 “현금으로 남는 공사”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["028050","000720","006360","375500"],"profile_paths":["atlas/symbol_profiles/028/028050.json","atlas/symbol_profiles/000/000720.json","atlas/symbol_profiles/006/006360.json","atlas/symbol_profiles/375/375500.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv"],"validation_scope":"2024 trigger-level forward path; 028050 caveats are 1997/1999/2016 and outside local 2024 windows; 000720 caveats are 1998/1999/2001/2004 and outside selected 2024 windows; 006360 caveats are 1999/2014 and outside selected 2024 windows; 375500 caveats are 2022 and outside selected 2024 windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C05 at 33 rows and asks for Mega EPC 계약, 원가초과, working capital, margin gap expansion.
- Existing registry shows C05 parsed through `R1 loop 98`.
- This output uses `R1 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C05 loop 97/98 focused on heat exchanger/plant EPC and LNG project equipment/fittings. This file shifts to listed EPC/constructor margin-gap and domestic construction rebound false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C05-R1L99-01 | 028050 | 삼성E&A | 2024-04-03 | 2024-04-03 | 25300 | 29300 | 17740 | 15.81% | -29.88% | Overseas EPC/plant order label had MFE, but later drawdown says margin and working-capital bridge failed. |
| C05-R1L99-02 | 000720 | 현대건설 | 2024-07-31 | 2024-07-31 | 33450 | 34150 | 27800 | 2.09% | -16.89% | Large contractor rebound label had almost no forward MFE before domestic/EPC margin risk dominated. |
| C05-R1L99-03 | 006360 | GS건설 | 2024-07-26 | 2024-07-26 | 19210 | 21750 | 16650 | 13.22% | -13.33% | Housing/construction recovery was tradable, but MAE requires cost and receivable guardrails. |
| C05-R1L99-04 | 375500 | DL이앤씨 | 2024-07-26 | 2024-07-26 | 34350 | 36000 | 28600 | 4.80% | -16.74% | EPC/construction value rebound remained weak without visible margin/FCF bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C05-R1L99-01","round":"R1","loop":"99","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"OVERSEAS_PLANT_EPC_CONTRACT_WORKING_CAPITAL_MARGIN_GAP","symbol":"028050","name":"삼성E&A","trigger_type":"overseas_plant_epc_contract_working_capital_margin_gap","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":25300,"peak_price":29300,"peak_date":"2024-07-30","trough_price":17740,"trough_date":"2024-10-31","mfe_pct":15.81,"mae_pct":-29.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"EPC_order_label_failed_without_cost_to_complete_working_capital_OPM_bridge","dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|overseas_plant_epc_contract_working_capital_margin_gap|2024-04-03"}
{"row_type":"trigger","case_id":"C05-R1L99-02","round":"R1","loop":"99","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"MAJOR_CONTRACTOR_REBOUND_LOW_MFE_MARGIN_GAP_FALSE_STAGE2","symbol":"000720","name":"현대건설","trigger_type":"major_contractor_rebound_low_mfe_margin_gap_false_stage2","trigger_date":"2024-07-31","entry_date":"2024-07-31","entry_price":33450,"peak_price":34150,"peak_date":"2024-07-31","trough_price":27800,"trough_date":"2024-10-25","mfe_pct":2.09,"mae_pct":-16.89,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"construction_rebound_label_low_MFE_without_margin_FCF_repair","dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|major_contractor_rebound_low_mfe_margin_gap_false_stage2|2024-07-31"}
{"row_type":"trigger","case_id":"C05-R1L99-03","round":"R1","loop":"99","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"HOUSING_CONSTRUCTION_RECOVERY_WITH_COST_RECEIVABLE_GUARD","symbol":"006360","name":"GS건설","trigger_type":"housing_construction_recovery_with_cost_receivable_guard","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":19210,"peak_price":21750,"peak_date":"2024-08-27","trough_price":16650,"trough_date":"2024-08-05","mfe_pct":13.22,"mae_pct":-13.33,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_working_capital_guard","residual_flag":"tradable_recovery_but_requires_cost_overrun_receivables_and_OPM_bridge","dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|housing_construction_recovery_with_cost_receivable_guard|2024-07-26"}
{"row_type":"trigger","case_id":"C05-R1L99-04","round":"R1","loop":"99","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_VALUE_REBOUND_WEAK_MFE_FCF_MARGIN_GAP","symbol":"375500","name":"DL이앤씨","trigger_type":"construction_value_rebound_weak_mfe_fcf_margin_gap","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":34350,"peak_price":36000,"peak_date":"2024-07-31","trough_price":28600,"trough_date":"2024-08-05","mfe_pct":4.80,"mae_pct":-16.74,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"weak_construction_value_rebound_without_FCF_OPM_project_margin_bridge","dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|construction_value_rebound_weak_mfe_fcf_margin_gap|2024-07-26"}
```

## 6. Score-return alignment

### 6.1 EPC headline is not margin bridge

`028050` is the most explicit C05 warning in this sample. The row produced MFE after the spring EPC/order narrative, but later drawdown overwhelmed the initial bridge. That implies C05 should demand cost-to-complete, change-order protection, working-capital stability, OPM and FCF evidence before promotion.

### 6.2 Major contractor rebound false Stage2

`000720` and `375500` show the low-MFE contractor-rebound family. Construction value or project recovery vocabulary can look cheap, but the forward path had little upside and material drawdown. These rows should remain Stage2/local 4B unless margin and cash conversion repair is visible.

### 6.3 Tradable recovery but not Green

`006360` is the middle case. It had a real rebound MFE after the July trigger, but the MAE and event history argue for a staged treatment. It can be Yellow only if cost-overrun repair, receivable quality and OPM bridge are verified.

## 7. Raw component score simulation

| symbol | contract/rebound evidence | scope/cost bridge | working capital/receivables | OPM/FCF bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 028050 | 18 | 7 | 5 | 5 | 8 | -14 | 29 | Stage2/local 4B watch |
| 000720 | 14 | 5 | 5 | 4 | 1 | -8 | 21 | Stage2/local 4B watch |
| 006360 | 16 | 9 | 8 | 7 | 10 | -7 | 43 | Stage2/Yellow with guard |
| 375500 | 14 | 6 | 6 | 5 | 3 | -8 | 26 | Stage2/local 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c05_epc_contract_requires_cost_working_capital_OPM_FCF_bridge","scope":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","candidate_action":"stage2_required_bridge","rule":"Do not promote EPC/mega-contract/construction rebound labels above Stage2 unless scope quality, cost-to-complete, change-order protection, working capital, receivable/unbilled-work quality, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["028050","000720","375500"],"counterbalanced_by":["006360"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c05_major_contractor_low_MFE_false_stage2_guard","scope":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","candidate_action":"local_4b_watch_guard","rule":"Major-contractor rebound rows with low MFE and meaningful MAE should remain local 4B watch until project-margin and cash-conversion evidence repairs the row.","supporting_cases":["000720","375500"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c05_epc_margin_gap_high_MAE_guard","scope":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","candidate_action":"high_MAE_guardrail","rule":"EPC/order rows that create short MFE but later deep MAE should be capped unless cost-to-complete, working capital, and OPM/FCF bridge is URL-verified.","supporting_cases":["028050"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c05_tradable_recovery_yellow_only_after_cost_repair","scope":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","candidate_action":"stage2_to_yellow_with_working_capital_guard","rule":"Construction recovery rows can become Yellow only after cost-overrun repair, receivable quality, and OPM bridge are visible; theme rebound alone is insufficient.","supporting_cases":["006360"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","round":"R1","loop":"99","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C05 should separate EPC/contract/rebound labels from actual cost-to-complete, working-capital, receivable, OPM and FCF conversion; most contractor rebounds in this sample remained Stage2/local 4B.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","high_MAE_guardrail","stage2_to_yellow_with_working_capital_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","sample_count":4,"avg_mfe_pct":8.98,"avg_mae_pct":-19.21,"median_mfe_pct":9.01,"median_mae_pct":-16.82,"interpretation":"C05 contract/construction rebound labels showed poor asymmetry unless working-capital and margin repair can be proven; price rebound alone is not enough for Green."}
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
- Ingest this C05 R1 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c05_epc_contract_requires_cost_working_capital_OPM_FCF_bridge -> stage2_required_bridge
  2. c05_major_contractor_low_MFE_false_stage2_guard -> local_4b_watch_guard
  3. c05_epc_margin_gap_high_MAE_guard -> high_MAE_guardrail
  4. c05_tradable_recovery_yellow_only_after_cost_repair -> stage2_to_yellow_with_working_capital_guard

Expected behavior:
- EPC/mega-contract/construction rebound vocabulary alone should not create Green.
- Scope quality, cost-to-complete, change-order protection, working capital, receivable/unbilled-work quality, OPM, FCF, or EPS revision can justify Stage3-Yellow.
- Low-MFE contractor rebounds and high-MAE EPC rows should stay local 4B or Stage2 until project-margin/cash evidence repairs the row.
```
