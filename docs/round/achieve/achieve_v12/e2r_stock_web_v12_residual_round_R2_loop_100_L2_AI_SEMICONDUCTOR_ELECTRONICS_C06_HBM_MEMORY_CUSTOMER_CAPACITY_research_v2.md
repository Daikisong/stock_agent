# E2R Stock-Web v12 Residual Research — R2 loop 100 / L2 / C06

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 100
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_PRODUCER_CUSTOMER_CAPACITY_ASP_FCF_BRIDGE_VS_MEMORY_LABEL_BETA_AND_NON_HBM_FOUNDRY_DECAY
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - HBM_mix_customer_capacity_ASP_FCF_bridge_test
  - memory_beta_false_positive_guardrail
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

이번 파일은 `C06_HBM_MEMORY_CUSTOMER_CAPACITY` 전용 residual research다.

C06은 “HBM”, “메모리 회복”, “AI memory”, “반도체 대형주”라는 label만으로 Green을 주는 bucket이 아니다. C06의 핵심은 고객 CAPA, HBM mix, ASP, FCF 전환이 실제로 보이는지다.

```text
HBM / memory customer capacity headline
  → customer qualification / capacity allocation / mix uplift
  → ASP / bit shipment / utilization
  → FCF / margin / EPS revision bridge
  → stock-web 1D OHLC forward path
```

HBM은 같은 메모리라도 다른 엔진이다. 단순 DRAM cycle은 바람이고, HBM customer capacity와 ASP/FCF bridge는 터빈이다. 바람이 불어도 터빈이 연결되지 않으면 전력은 나오지 않는다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["000660","005930","014680","000990"],"profile_paths":["atlas/symbol_profiles/000/000660.json","atlas/symbol_profiles/005/005930.json","atlas/symbol_profiles/014/014680.json","atlas/symbol_profiles/000/000990.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv","atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats are outside local 2024 windows and are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C06 at 21 rows, 9 rows short of the 30-row minimum stability zone.
- Registry shows C06 parsed through `R2 loop 99`.
- This output uses `R2 loop 100`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file shifts from the prior package/substrate/test-handler family into direct memory producer, large-cap HBM lag, memory chemical/material beta, and non-HBM foundry beta decay.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C06-R2L100-01 | 000660 | SK하이닉스 | 2024-03-26 | 2024-03-26 | 176600 | 248500 | 169500 | 40.71% | -4.02% | HBM mix/customer capacity leader path; strong positive bridge candidate. |
| C06-R2L100-02 | 005930 | 삼성전자 | 2024-04-02 | 2024-04-02 | 85000 | 88800 | 55800 | 4.47% | -34.35% | Memory/HBM label without enough HBM mix/ASP bridge; high-MAE counterexample. |
| C06-R2L100-03 | 014680 | 한솔케미칼 | 2024-03-20 | 2024-03-20 | 200000 | 214000 | 172100 | 7.00% | -13.95% | Memory material/HBM supply-chain label had weak asymmetry without FCF/margin bridge. |
| C06-R2L100-04 | 000990 | DB하이텍 | 2024-06-20 | 2024-06-20 | 57100 | 58900 | 35200 | 3.15% | -38.35% | Non-HBM foundry/memory beta spike failed; hard false-positive guardrail. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C06-R2L100-01","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_PRODUCER_CUSTOMER_CAPACITY_ASP_FCF_LEADER","symbol":"000660","name":"SK하이닉스","trigger_type":"hbm_memory_producer_customer_capacity_asp_fcf_leader","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":176600,"peak_price":248500,"peak_date":"2024-07-11","trough_price":169500,"trough_date":"2024-04-19","mfe_pct":40.71,"mae_pct":-4.02,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_URLs","residual_flag":"positive_hbm_mix_customer_capacity_ASP_FCF_bridge_candidate","dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|hbm_memory_producer_customer_capacity_asp_fcf_leader|2024-03-26"}
{"row_type":"trigger","case_id":"C06-R2L100-02","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"LARGE_CAP_MEMORY_HBM_LABEL_LAG_HIGH_MAE_COUNTEREXAMPLE","symbol":"005930","name":"삼성전자","trigger_type":"large_cap_memory_hbm_label_lag_high_mae","trigger_date":"2024-04-02","entry_date":"2024-04-02","entry_price":85000,"peak_price":88800,"peak_date":"2024-07-11","trough_price":55800,"trough_date":"2024-10-25","mfe_pct":4.47,"mae_pct":-34.35,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch_not_Green","residual_flag":"counterexample_memory_label_without_sufficient_HBM_mix_ASP_FCF_bridge","dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|large_cap_memory_hbm_label_lag_high_mae|2024-04-02"}
{"row_type":"trigger","case_id":"C06-R2L100-03","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_CHEMICAL_MATERIAL_HBM_SUPPLYCHAIN_WEAK_BRIDGE","symbol":"014680","name":"한솔케미칼","trigger_type":"memory_chemical_material_hbm_supplychain_weak_bridge","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":200000,"peak_price":214000,"peak_date":"2024-03-21","trough_price":172100,"trough_date":"2024-07-18","mfe_pct":7.00,"mae_pct":-13.95,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_Yellow_watch","residual_flag":"material_supplychain_label_needs_customer_capacity_margin_FCF_bridge","dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|014680|memory_chemical_material_hbm_supplychain_weak_bridge|2024-03-20"}
{"row_type":"trigger","case_id":"C06-R2L100-04","round":"R2","loop":"100","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"NON_HBM_FOUNDRY_MEMORY_BETA_FALSE_STAGE2","symbol":"000990","name":"DB하이텍","trigger_type":"non_hbm_foundry_memory_beta_false_stage2","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":57100,"peak_price":58900,"peak_date":"2024-06-20","trough_price":35200,"trough_date":"2024-09-09","mfe_pct":3.15,"mae_pct":-38.35,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_4C_watch","residual_flag":"non_HBM_memory_foundry_beta_spike_decayed_without_customer_capacity_ASP_bridge","dedupe_key":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000990|non_hbm_foundry_memory_beta_false_stage2|2024-06-20"}
```

## 6. Score-return alignment

### 6.1 True HBM customer-capacity winner

`000660` is the positive family. The return profile shows that the market was not merely buying “memory recovery”; it was repricing HBM customer capacity, mix, ASP, and FCF conversion. This is the C06 row that can justify Stage3-Yellow/Green candidate treatment after URL verification.

### 6.2 Large-cap HBM label lag

`005930` is the critical counterexample. Same broad memory sector, but the stock path after the spring HBM/memory label did not sustain the early move. This row says C06 should not mechanically transfer SK Hynix-style HBM score to all memory producers.

### 6.3 Materials and foundry false positives

`014680` and `000990` show the weaker periphery. Materials or foundry beta can move with memory headlines, but without direct HBM customer-capacity allocation, ASP uplift, utilization, and FCF bridge, MFE stays small while MAE opens. These are Stage2/Yellow-watch or hard 4C-watch rows.

## 7. Raw component score simulation

| symbol | HBM/customer capacity | ASP/mix bridge | FCF/margin bridge | price confirmation | MAE/logic guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 000660 | 25 | 23 | 20 | 22 | -2 | 88 | Stage3-Yellow/Green candidate |
| 005930 | 15 | 7 | 5 | 3 | -17 | 13 | Stage2/local 4B watch |
| 014680 | 14 | 8 | 6 | 5 | -7 | 26 | Stage2/Yellow watch |
| 000990 | 6 | 3 | 2 | 2 | -18 | -5 | Hard counterexample / 4C watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c06_hbm_requires_customer_capacity_asp_fcf_bridge","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"stage2_required_bridge","rule":"Do not promote memory/HBM labels above Stage2 unless customer capacity allocation, HBM mix, ASP uplift, utilization, margin, FCF, or EPS revision bridge is visible.","supporting_cases":["005930","014680","000990"],"counterbalanced_by":["000660"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c06_hbm_leader_positive_delta","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"HBM producer leaders with visible customer capacity, ASP/mix uplift, and FCF bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["000660"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c06_large_cap_peer_transfer_guard","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"canonical_boundary_guard","rule":"Do not transfer HBM leader score to all memory large caps; each producer needs its own customer capacity, HBM mix, and FCF bridge.","supporting_cases":["005930"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c06_non_hbm_beta_false_stage2_guard","scope":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","candidate_action":"hard_4c_watch","rule":"Non-HBM foundry or generic memory beta with small MFE and deep MAE should be marked hard counterexample/4C watch rather than Stage2 persistence.","supporting_cases":["000990"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","round":"R2","loop":"100","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C06 should separate true HBM customer-capacity/ASP/FCF winners from generic memory, material, or non-HBM foundry beta.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","canonical_boundary_guard","hard_4c_watch"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","sample_count":4,"avg_mfe_pct":13.83,"avg_mae_pct":-22.67,"median_mfe_pct":5.74,"median_mae_pct":-24.15,"interpretation":"C06 upside is concentrated in true HBM customer-capacity leaders; generic memory labels create poor asymmetry when ASP/FCF bridge is absent."}
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
  - historical corporate-action profile caveats, where present, are outside local 2024 windows
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
  1. c06_hbm_requires_customer_capacity_asp_fcf_bridge -> stage2_required_bridge
  2. c06_hbm_leader_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c06_large_cap_peer_transfer_guard -> canonical_boundary_guard
  4. c06_non_hbm_beta_false_stage2_guard -> hard_4c_watch

Expected behavior:
- Memory/HBM vocabulary alone should not create Green.
- Customer capacity allocation, HBM mix, ASP, utilization, margin, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Large-cap peer transfer and non-HBM foundry beta must be guarded when MFE is small and MAE dominates.
```
