# E2R Stock-Web v12 Residual Research — R2 loop 100 / L2 / C06

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 100
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_BRIDGE_VS_GENERIC_MEMORY_BETA_AND_OSAT_CAPACITY_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - HBM_customer_capacity_mix_ASP_FCF_bridge_test
  - memory_major_relative_winner_vs_lagging_peer_guard
  - OSAT_capacity_false_stage2_guard
  - HBM_leader_late_chase_event_cap_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C06_HBM_MEMORY_CUSTOMER_CAPACITY` 전용 residual research다.

C06은 “HBM”, “메모리 회복”, “고객 CAPA”, “AI 서버 메모리”, “패키징/OSAT capacity”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 고객 CAPA와 HBM mix가 실제 ASP, bit shipment, supply allocation, gross margin, FCF, EPS revision으로 내려오는지다.

```text
HBM memory / customer CAPA headline
  → customer allocation / HBM mix / supply qualification
  → ASP and bit shipment / capacity conversion
  → gross margin / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

HBM CAPA는 고속도로의 전용 차선과 같다. 차선이 만들어져도 실제 고객 차량이 계속 들어오고 통행료가 올라야 이익이 된다. C06은 “AI 메모리 도로가 생겼다”와 “통행료가 현금으로 쌓인다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["000660","005930","036540"],"profile_paths":["atlas/symbol_profiles/000/000660.json","atlas/symbol_profiles/005/005930.json","atlas/symbol_profiles/036/036540.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv"],"validation_scope":"2024 trigger-level forward path; 000660 caveats are historical and end 2003, 005930 caveats include 2018, and 036540 caveats end 2016, so selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C06 at 21 rows, 9 rows short of the 30-row minimum stability zone.
- Existing registry shows C06 parsed through `R2 loop 99`.
- This output uses `R2 loop 100`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file separates direct HBM memory leader, HBM leader late-chase, lagging memory-major HBM/capacity catch-up, and OSAT capacity false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C06-R2L100-01 | 000660 | SK하이닉스 | 2024-03-21 | 2024-03-21 | 170000 | 248500 | 144700 | 46.18% | -14.88% | Direct HBM/customer-CAPA mix winner; positive but full-window drawdown requires sizing and FCF proof. |
| C06-R2L100-02 | 005930 | 삼성전자 | 2024-03-20 | 2024-03-20 | 76900 | 88800 | 49900 | 15.47% | -35.11% | Memory-major HBM/capacity catch-up had MFE but failed relative to leader without HBM mix/ASP proof. |
| C06-R2L100-03 | 036540 | SFA반도체 | 2024-01-24 | 2024-01-24 | 7480 | 8150 | 3305 | 8.96% | -55.82% | OSAT/package capacity label made a short spike then hard high-MAE false Stage2. |
| C06-R2L100-04 | 000660 | SK하이닉스 | 2024-07-11 | 2024-07-11 | 241000 | 248500 | 144700 | 3.11% | -39.96% | Same HBM leader, late-chase after price extension became local 4B/event-cap. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C06-R2L100-01","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"DIRECT_HBM_MEMORY_CUSTOMER_CAPACITY_MIX_ASP_FCF_LEADER","symbol":"000660","name":"SK하이닉스","trigger_type":"direct_hbm_memory_customer_capacity_mix_asp_fcf_leader","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":170000,"peak_price":248500,"peak_date":"2024-07-11","trough_price":144700,"trough_date":"2024-09-19","mfe_pct":46.18,"mae_pct":-14.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_with_sizing_guard","residual_flag":"direct_HBM_memory_leader_positive_but_requires_customer_allocation_ASP_FCF_URLs","dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|direct_hbm_memory_customer_capacity_mix_asp_fcf_leader|2024-03-21"}
{"row_type":"trigger","case_id":"C06-R2L100-02","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_MAJOR_HBM_CAPACITY_CATCHUP_LAGGING_PEER_HIGH_MAE","symbol":"005930","name":"삼성전자","trigger_type":"memory_major_hbm_capacity_catchup_lagging_peer_high_mae","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":76900,"peak_price":88800,"peak_date":"2024-07-11","trough_price":49900,"trough_date":"2024-11-14","mfe_pct":15.47,"mae_pct":-35.11,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_relative_lag_guard","residual_flag":"memory_major_HBM_catchup_label_failed_without_mix_ASP_FCF_relative_proof","dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|memory_major_hbm_capacity_catchup_lagging_peer_high_mae|2024-03-20"}
{"row_type":"trigger","case_id":"C06-R2L100-03","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"OSAT_PACKAGE_CAPACITY_HBM_LABEL_FALSE_STAGE2_HIGH_MAE","symbol":"036540","name":"SFA반도체","trigger_type":"osat_package_capacity_hbm_label_false_stage2_high_mae","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":7480,"peak_price":8150,"peak_date":"2024-01-24","trough_price":3305,"trough_date":"2024-09-09","mfe_pct":8.96,"mae_pct":-55.82,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"OSAT_capacity_HBM_label_short_spike_decayed_without_customer_capacity_FCF_bridge","dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|036540|osat_package_capacity_hbm_label_false_stage2_high_mae|2024-01-24"}
{"row_type":"trigger","case_id":"C06-R2L100-04","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"000660","name":"SK하이닉스","trigger_type":"hbm_memory_leader_late_chase_price_only_extension_4b","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":241000,"peak_price":248500,"peak_date":"2024-07-11","trough_price":144700,"trough_date":"2024-09-19","mfe_pct":3.11,"mae_pct":-39.96,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_HBM_leader_late_entry_without_fresh_customer_allocation_FCF_evidence","dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|hbm_memory_leader_late_chase_price_only_extension_4b|2024-07-11"}
```

## 6. Score-return alignment

### 6.1 Direct HBM leader can work, but needs sizing

`000660` early is the constructive C06 path. It produced strong MFE because the market treated HBM/customer capacity and mix as real earnings drivers. But the full-window trough shows why C06 should still demand HBM customer allocation, ASP/mix and FCF evidence before Green.

### 6.2 Memory-major catch-up is not the same as HBM leadership

`005930` had a March trigger and reached a July high, but then fell far below entry. This is the C06 relative-lag warning: “memory major + HBM catch-up” should not inherit the same score as a verified HBM mix leader unless the non-price bridge proves customer qualification, supply allocation, ASP, and FCF conversion.

### 6.3 OSAT/package capacity label can be a false Stage2

`036540` is the hard counterexample row. It had OSAT/package capacity and memory-cycle vocabulary, but the price path showed tiny MFE and severe MAE. C06 should not treat OSAT capacity as HBM customer capacity unless end-customer loading, utilization, gross margin and cash conversion are verified.

### 6.4 Same leader, different entry

The `000660` late-chase row shows timing risk. The same HBM memory leader became poor risk/reward when the trigger was mostly price extension. C06 needs a local 4B/event-cap rule when fresh customer allocation or FCF evidence is absent.

## 7. Raw component score simulation

| symbol | HBM/customer capacity | mix/ASP bridge | FCF/revision bridge | price confirmation | MAE/relative guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 000660 early | 24 | 22 | 18 | 20 | -7 | 77 | Stage3-Yellow/Green candidate with sizing guard |
| 005930 | 19 | 9 | 7 | 8 | -16 | 27 | Stage2/Yellow with relative-lag guard |
| 036540 | 11 | 4 | 2 | 1 | -25 | -7 | Hard counterexample / 4C watch |
| 000660 late | 24 | 6 | 5 | 2 | -18 | 19 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c06_hbm_requires_customer_allocation_mix_ASP_FCF_bridge","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"stage2_required_bridge","rule":"Do not promote HBM memory/customer capacity labels above Stage2 unless customer allocation, qualification, HBM mix, ASP, bit shipment, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["005930","036540","000660_late"],"counterbalanced_by":["000660_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c06_direct_HBM_leader_positive_delta","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Direct HBM memory leaders with verified customer allocation, HBM mix uplift, ASP and FCF conversion can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["000660_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c06_memory_major_relative_lag_guard","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"stage2_to_yellow_with_relative_lag_guard","rule":"Memory-major HBM catch-up rows should be capped when MFE is modest and later MAE dominates; Green requires relative proof versus direct HBM leaders.","supporting_cases":["005930"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c06_OSAT_capacity_false_stage2_guard","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"hard_4c_watch","rule":"OSAT/package capacity labels with tiny MFE and severe MAE should be hard counterexamples unless customer loading, utilization, margin and cash conversion repair the thesis.","supporting_cases":["036540"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c06_HBM_leader_late_chase_4B_guard","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"local_4b_watch_guard","rule":"If a direct HBM memory leader entry follows a price extension and lacks fresh customer allocation/FCF evidence, cap at local 4B or event-cap.","supporting_cases":["000660_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","round":"R2","loop":"100","positive_rows":1,"counterexample_rows":3,"new_symbol_count":3,"primary_residual":"C06 should separate verified direct HBM memory customer-capacity winners from lagging memory-major catch-up rows, OSAT/package-capacity false Stage2 rows, and late-chase price-only extensions.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_relative_lag_guard","hard_4c_watch","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","sample_count":4,"avg_mfe_pct":18.43,"avg_mae_pct":-36.44,"median_mfe_pct":12.22,"median_mae_pct":-37.54,"interpretation":"C06 has strong upside only when HBM customer capacity converts into mix, ASP and FCF; generic memory catch-up, OSAT capacity, and late-chase rows show poor asymmetry."}
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
- Ingest this C06 R2 loop 100 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c06_hbm_requires_customer_allocation_mix_ASP_FCF_bridge -> stage2_required_bridge
  2. c06_direct_HBM_leader_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c06_memory_major_relative_lag_guard -> stage2_to_yellow_with_relative_lag_guard
  4. c06_OSAT_capacity_false_stage2_guard -> hard_4c_watch
  5. c06_HBM_leader_late_chase_4B_guard -> local_4b_watch_guard

Expected behavior:
- HBM/customer-capacity vocabulary alone should not create Green.
- Customer allocation, qualification, HBM mix, ASP, bit shipment, margin, FCF, or EPS revision can justify Stage3-Yellow/Green.
- OSAT/package capacity and late-chase memory leader rows should remain capped until fresh non-price evidence appears.
```
