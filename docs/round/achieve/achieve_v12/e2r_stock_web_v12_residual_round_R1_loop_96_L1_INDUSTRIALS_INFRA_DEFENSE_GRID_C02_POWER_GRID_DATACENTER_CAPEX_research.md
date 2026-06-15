# E2R Stock-Web v12 Residual Research — R1 loop 96 / L1 / C02

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 96
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_SWITCHGEAR_DATACENTER_CAPEX_BACKLOG_CAPA_LOCK_ASP_MARGIN_BRIDGE_VS_POWER_THEME_LATE_CHASE_4B
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - power_grid_backlog_ASP_margin_bridge_test
  - late_chase_high_MAE_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C02_POWER_GRID_DATACENTER_CAPEX` 전용 residual research다.

C02는 “전력기기”, “변압기”, “AI 데이터센터 전력망”, “북미 grid CAPEX” 같은 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 CAPEX cycle이 실제 backlog, CAPA lock, ASP, margin/revision으로 내려오는지다.

```text
power grid / datacenter CAPEX headline
  → transformer / switchgear / cable backlog
  → capacity lock / ASP or mix uplift
  → delivery schedule / margin / EPS revision
  → stock-web 1D OHLC forward path
```

전력망 CAPEX는 전기가 흐르는 송전선과 같다. headline은 전압이고, backlog와 CAPA lock은 구리선의 굵기다. 선이 얇으면 번개처럼 튀는 가격은 오래 가지 못하고, 선이 굵으면 전류가 매출과 마진으로 계속 흐른다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["267260","298040","010120","103590"],"profile_paths":["atlas/symbol_profiles/267/267260.json","atlas/symbol_profiles/298/298040.json","atlas/symbol_profiles/010/010120.json","atlas/symbol_profiles/103/103590.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection. 103590 has a 2024-02-13 corporate-action candidate, so entries after that window are used."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C02 at 24 rows, 6 rows short of the 30-row minimum stability zone.
- Existing registry shows C02 parsed through `R1 loop 95`.
- This output uses `R1 loop 96`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file uses power-grid leaders and one late-chase counterexample row to separate structural backlog from price-only extension.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C02-R1L96-01 | 267260 | HD현대일렉트릭 | 2024-04-11 | 2024-04-11 | 232000 | 363000 | 200000 | 56.47% | -13.79% | Transformer leader CAPA/backlog/margin bridge positive path, but sizing guard needed. |
| C02-R1L96-02 | 298040 | 효성중공업 | 2024-03-04 | 2024-03-04 | 222500 | 325000 | 195000 | 46.07% | -12.36% | Heavy transformer/grid backlog repricing worked; margin/revision bridge required before Green. |
| C02-R1L96-03 | 010120 | LS ELECTRIC | 2024-04-04 | 2024-04-04 | 106000 | 274500 | 94400 | 158.96% | -10.94% | Switchgear/datacenter CAPEX positive path, but entry-day drawdown and later blowoff risk matter. |
| C02-R1L96-04 | 103590 | 일진전기 | 2024-03-18 | 2024-03-18 | 17200 | 30250 | 15570 | 75.87% | -9.48% | Cable/transformer supply-chain CAPEX path worked when demand converted into backlog/mix. |
| C02-R1L96-05 | 010120 | LS ELECTRIC | 2024-07-23 | 2024-07-23 | 259000 | 274500 | 145000 | 5.98% | -44.02% | Same sector label, but late-chase without fresh bridge became high-MAE 4B/event-cap case. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C02-R1L96-01","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_LEADER_BACKLOG_CAPA_LOCK_ASP_MARGIN_BRIDGE","symbol":"267260","name":"HD현대일렉트릭","trigger_type":"transformer_leader_backlog_capa_lock_asp_margin_bridge","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":232000,"peak_price":363000,"peak_date":"2024-07-11","trough_price":200000,"trough_date":"2024-04-16","mfe_pct":56.47,"mae_pct":-13.79,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_URLs","residual_flag":"positive_transformer_backlog_path_but_requires_exact_backlog_ASP_margin_URLs","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|267260|transformer_leader_backlog_capa_lock_asp_margin_bridge|2024-04-11"}
{"row_type":"trigger","case_id":"C02-R1L96-02","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HEAVY_TRANSFORMER_GRID_BACKLOG_MARGIN_REVISION_BRIDGE","symbol":"298040","name":"효성중공업","trigger_type":"heavy_transformer_grid_backlog_margin_revision_bridge","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":222500,"peak_price":325000,"peak_date":"2024-04-05","trough_price":195000,"trough_date":"2024-03-04","mfe_pct":46.07,"mae_pct":-12.36,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_margin_URLs","residual_flag":"positive_grid_backlog_repricing_but_margin_bridge_required","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|298040|heavy_transformer_grid_backlog_margin_revision_bridge|2024-03-04"}
{"row_type":"trigger","case_id":"C02-R1L96-03","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE","symbol":"010120","name":"LS ELECTRIC","trigger_type":"switchgear_datacenter_capex_order_margin_bridge","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":106000,"peak_price":274500,"peak_date":"2024-07-24","trough_price":94400,"trough_date":"2024-04-04","mfe_pct":158.96,"mae_pct":-10.94,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_URLs","residual_flag":"very_strong_positive_path_but_requires_order_margin_and_price_extension_guardrail","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|010120|switchgear_datacenter_capex_order_margin_bridge|2024-04-04"}
{"row_type":"trigger","case_id":"C02-R1L96-04","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_TRANSFORMER_SUPPLYCHAIN_BACKLOG_MIX_BRIDGE","symbol":"103590","name":"일진전기","trigger_type":"power_cable_transformer_supplychain_backlog_mix_bridge","trigger_date":"2024-03-18","entry_date":"2024-03-18","entry_price":17200,"peak_price":30250,"peak_date":"2024-05-29","trough_price":15570,"trough_date":"2024-03-18","mfe_pct":75.87,"mae_pct":-9.48,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_mix_URLs","residual_flag":"positive_supplychain_bridge_after_corporate_action_candidate_window","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|103590|power_cable_transformer_supplychain_backlog_mix_bridge|2024-03-18"}
{"row_type":"trigger","case_id":"C02-R1L96-05","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_LATE_CHASE_PRICE_ONLY_EXTENSION_4B_EVENT_CAP","symbol":"010120","name":"LS ELECTRIC","trigger_type":"switchgear_late_chase_price_only_extension_4b_event_cap","trigger_date":"2024-07-23","entry_date":"2024-07-23","entry_price":259000,"peak_price":274500,"peak_date":"2024-07-24","trough_price":145000,"trough_date":"2024-08-05","mfe_pct":5.98,"mae_pct":-44.02,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"counterexample_same_sector_label_late_chase_without_fresh_order_margin_bridge","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|010120|switchgear_late_chase_price_only_extension_4b_event_cap|2024-07-23"}
```

## 6. Score-return alignment

### 6.1 Structural grid CAPEX winners

`267260`, `298040`, `010120`, and `103590` show the constructive C02 family. The successful rows are not just “power theme” rows. They reflect a market belief that backlog visibility, CAPA lock, ASP/mix, and margin expansion are converting into earnings.

### 6.2 Same label, different timing

The `010120` late-chase row is the key counterexample. The company and sector are the same, but the entry point changed from bridge-confirming to price-only extension. MFE was small while MAE was severe. This argues that C02 needs a late-chase guardrail even for the best names.

### 6.3 Mechanism

C02 behaves like a transformer. Backlog and CAPA lock step up the voltage, but the model still needs insulation: delivery timing, ASP, margin, and revision evidence. Without that insulation, the price move can arc into 4B/event-cap.

## 7. Raw component score simulation

| symbol | backlog/CAPA evidence | ASP/mix bridge | margin/revision bridge | price confirmation | MAE/late-chase guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 267260 | 24 | 21 | 19 | 22 | -6 | 80 | Stage3-Yellow/Green candidate |
| 298040 | 22 | 18 | 17 | 19 | -6 | 70 | Stage3-Yellow candidate |
| 010120 early | 23 | 21 | 18 | 25 | -5 | 82 | Stage3-Yellow/Green candidate |
| 103590 | 19 | 16 | 13 | 21 | -5 | 64 | Stage3-Yellow candidate |
| 010120 late | 15 | 7 | 5 | 3 | -20 | 10 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c02_power_grid_requires_backlog_capa_asp_margin_bridge","scope":"C02_POWER_GRID_DATACENTER_CAPEX","candidate_action":"stage2_required_bridge","rule":"Do not promote power-grid/datacenter CAPEX labels above Stage2 unless backlog, capacity lock, ASP/mix, delivery schedule, margin, or EPS revision bridge is visible.","supporting_cases":["010120_late_chase"],"counterbalanced_by":["267260","298040","010120_early","103590"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c02_transformer_backlog_positive_delta","scope":"C02_POWER_GRID_DATACENTER_CAPEX","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Transformer/switchgear leaders with backlog duration, CAPA lock, ASP/mix uplift, and margin revision can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["267260","298040","010120_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c02_late_chase_price_only_4b_guard","scope":"C02_POWER_GRID_DATACENTER_CAPEX","candidate_action":"local_4b_watch_guard","rule":"If C02 entry follows a large price extension and lacks fresh order/margin evidence, cap at local 4B watch or event-cap even for sector leaders.","supporting_cases":["010120_late_chase"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c02_supplychain_mix_bridge_yellow_delta","scope":"C02_POWER_GRID_DATACENTER_CAPEX","candidate_action":"stage3_yellow_candidate_delta","rule":"Power-cable or equipment supply-chain names can be Yellow candidates when backlog and product-mix bridge are visible, but Green requires margin/cash conversion proof.","supporting_cases":["103590"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","round":"R1","loop":"96","positive_rows":4,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C02 should distinguish structural grid/datacenter backlog plus CAPA/ASP/margin bridge from late price-only extension in the same sector.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","local_4b_watch_guard","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","sample_count":5,"avg_mfe_pct":68.67,"avg_mae_pct":-18.12,"median_mfe_pct":56.47,"median_mae_pct":-12.36,"interpretation":"C02 has very strong upside when backlog/CAPA/ASP/margin bridge is real, but late-chase entries can flip the same sector label into severe 4B/event-cap drawdown."}
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
  - 103590 has a 2024-02-13 corporate-action candidate, so this file uses post-window 2024-03-18 trigger row
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C02 R1 loop 96 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c02_power_grid_requires_backlog_capa_asp_margin_bridge -> stage2_required_bridge
  2. c02_transformer_backlog_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c02_late_chase_price_only_4b_guard -> local_4b_watch_guard
  4. c02_supplychain_mix_bridge_yellow_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Power-grid/datacenter CAPEX vocabulary alone should not create Green.
- Backlog, capacity lock, ASP/mix, delivery schedule, margin, or EPS revision can justify Stage3-Yellow/Green.
- Late price-only extension should be capped at local 4B/event-cap even for sector leaders.
```
