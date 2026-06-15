# E2R Stock-Web v12 Residual Research — R1 loop 96 / L1 / C02

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 96
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_SWITCHGEAR_DATACENTER_CAPEX_BACKLOG_CAPA_LOCK_ASP_MARGIN_BRIDGE_VS_POWER_CABLE_OPTIONALITY_AND_LATE_CHASE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - power_grid_backlog_CAPA_lock_ASP_margin_bridge_test
  - datacenter_capex_order_conversion_test
  - power_cable_high_MAE_guardrail
  - transformer_leader_late_chase_guardrail
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

C02는 “전력기기”, “전력망”, “데이터센터”, “AI 전력”, “전선/케이블”, “변압기 수혜”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 grid/datacenter CAPEX narrative가 실제 수주잔고, CAPA lock, ASP, 납기, 북미/중동/데이터센터 고객, gross margin, OPM/FCF/revision으로 내려오는지다.

```text
power grid / datacenter capex headline
  → firm order / backlog quality / CAPA lock
  → delivery schedule / ASP / customer mix
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

전력 CAPEX는 변전소의 차단기와 같다. 전압이 높아도 회로가 닫히지 않으면 전류가 흐르지 않는다. C02는 “전력 테마가 켜졌다”와 “수주·CAPA·ASP·마진 회로가 닫혔다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["267260","010120","298040","103590"],"profile_paths":["atlas/symbol_profiles/267/267260.json","atlas/symbol_profiles/010/010120.json","atlas/symbol_profiles/298/298040.json","atlas/symbol_profiles/103/103590.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv"],"validation_scope":"2024 trigger-level forward path; 267260 historical caveats end 2019, 010120 caveats end 2003, 298040 has zero corporate-action candidates, and 103590 has a 2024-02-13 caveat so selected March/April forward rows are treated as post-caveat windows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C02 at 24 rows, 6 rows short of the 30-row minimum stability zone.
- Existing registry shows C02 parsed through `R1 loop 95`.
- This output uses `R1 loop 96`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C02 rows covered transformer/grid backlog, grid automation false Stage2, transmission fitting event-cap. This file compresses transformer CAPA-lock leaders, switchgear/datacenter order conversion, heavy transformer/capacity bridge, power-cable optionality high MAE, and transformer leader late-chase timing risk.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C02-R1L96-01 | 267260 | HD현대일렉트릭 | 2024-04-18 | 2024-04-18 | 239000 | 374500 | 210000 | 56.69% | -12.13% | Transformer CAPA-lock/backlog/ASP rerating worked, but early drawdown needs sizing guard. |
| C02-R1L96-02 | 010120 | LS ELECTRIC | 2024-04-04 | 2024-04-04 | 106000 | 274500 | 105500 | 158.96% | -0.47% | Switchgear/datacenter/grid capex order bridge worked with very controlled MAE. |
| C02-R1L96-03 | 298040 | 효성중공업 | 2024-03-04 | 2024-03-04 | 222500 | 469000 | 221500 | 110.79% | -0.45% | Heavy transformer/CAPA expansion path worked with strong MFE and near-flat MAE. |
| C02-R1L96-04 | 103590 | 일진전기 | 2024-04-04 | 2024-04-04 | 23200 | 30250 | 16600 | 30.39% | -28.45% | Power cable/transmission optionality made MFE, but high MAE requires backlog/ASP/margin guard. |
| C02-R1L96-05 | 267260 | HD현대일렉트릭 | 2024-07-24 | 2024-07-24 | 365500 | 374500 | 225500 | 2.46% | -38.30% | Same transformer leader, late-chase after extension became local 4B/event-cap. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C02-R1L96-01","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_CAPA_LOCK_BACKLOG_ASP_MARGIN_BRIDGE","symbol":"267260","name":"HD현대일렉트릭","trigger_type":"transformer_capa_lock_backlog_asp_margin_bridge","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":239000,"peak_price":374500,"peak_date":"2024-07-24","trough_price":210000,"trough_date":"2024-04-23","mfe_pct":56.69,"mae_pct":-12.13,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_backlog_OPM_URLs","residual_flag":"strong_transformer_backlog_path_but_requires_CAPA_lock_ASP_OPM_FCF_URLs","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|267260|transformer_capa_lock_backlog_asp_margin_bridge|2024-04-18"}
{"row_type":"trigger","case_id":"C02-R1L96-02","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SWITCHGEAR_DATACENTER_GRID_CAPEX_ORDER_MARGIN_BRIDGE","symbol":"010120","name":"LS ELECTRIC","trigger_type":"switchgear_datacenter_grid_capex_order_margin_bridge","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":106000,"peak_price":274500,"peak_date":"2024-07-24","trough_price":105500,"trough_date":"2024-04-05","mfe_pct":158.96,"mae_pct":-0.47,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_order_margin_URLs","residual_flag":"switchgear_datacenter_grid_capex_path_worked_but_exact_order_OPM_URLs_required","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|010120|switchgear_datacenter_grid_capex_order_margin_bridge|2024-04-04"}
{"row_type":"trigger","case_id":"C02-R1L96-03","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HEAVY_TRANSFORMER_CAPA_EXPANSION_BACKLOG_MARGIN_BRIDGE","symbol":"298040","name":"효성중공업","trigger_type":"heavy_transformer_capa_expansion_backlog_margin_bridge","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":222500,"peak_price":469000,"peak_date":"2024-05-28","trough_price":221500,"trough_date":"2024-03-12","mfe_pct":110.79,"mae_pct":-0.45,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_CAPA_margin_URLs","residual_flag":"heavy_transformer_positive_path_but_requires_backlog_CAPA_OPM_FCF_evidence","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|298040|heavy_transformer_capa_expansion_backlog_margin_bridge|2024-03-04"}
{"row_type":"trigger","case_id":"C02-R1L96-04","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_TRANSMISSION_OPTIONALITY_HIGH_MAE_GUARD","symbol":"103590","name":"일진전기","trigger_type":"power_cable_transmission_optionality_high_mae_guard","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":23200,"peak_price":30250,"peak_date":"2024-05-29","trough_price":16600,"trough_date":"2024-09-09","mfe_pct":30.39,"mae_pct":-28.45,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_high_MAE_guardrail","residual_flag":"power_cable_optional_MFE_but_high_MAE_requires_backlog_ASP_margin_bridge","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|103590|power_cable_transmission_optionality_high_mae_guard|2024-04-04"}
{"row_type":"trigger","case_id":"C02-R1L96-05","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"267260","name":"HD현대일렉트릭","trigger_type":"transformer_leader_late_chase_price_only_extension_4b","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":365500,"peak_price":374500,"peak_date":"2024-07-24","trough_price":225500,"trough_date":"2024-09-09","mfe_pct":2.46,"mae_pct":-38.30,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_transformer_leader_late_chase_without_fresh_backlog_margin_evidence","dedupe_key":"C02_POWER_GRID_DATACENTER_CAPEX|267260|transformer_leader_late_chase_price_only_extension_4b|2024-07-24"}
```

## 6. Score-return alignment

### 6.1 Transformer / switchgear true winners

`267260`, `010120`, and `298040` show the constructive C02 family. These are not just “AI electricity” theme rows. The price path suggests the market was repricing firm order quality, CAPA lock, ASP, delivery schedule, and margin conversion in transformer/switchgear-heavy businesses.

### 6.2 Cable optionality needs guardrails

`103590` shows a middle case. Power cable and transmission optionality can create meaningful MFE, but drawdown later became too large for automatic Green. This row should require backlog quality, cable ASP, raw-material pass-through, delivery cadence, and margin evidence.

### 6.3 Same leader, different timing

The `267260` late-chase row is the hard timing guard. The same transformer/CAPA thesis became poor risk/reward when the trigger was mostly price extension. C02 therefore needs a local 4B/event-cap rule when fresh backlog/margin evidence is absent.

## 7. Raw component score simulation

| symbol | grid/datacenter evidence | backlog/CAPA lock | ASP/customer mix | OPM/FCF bridge | price confirmation | MAE/late-chase guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 267260 early | 24 | 22 | 20 | 18 | 22 | -6 | 80 | Stage3-Yellow/Green candidate |
| 010120 | 23 | 21 | 18 | 17 | 25 | -1 | 86 | Stage3-Yellow/Green candidate |
| 298040 | 22 | 20 | 17 | 16 | 24 | -1 | 82 | Stage3-Yellow/Green candidate |
| 103590 | 18 | 11 | 10 | 7 | 13 | -14 | 45 | Stage2/Yellow with high-MAE guard |
| 267260 late | 24 | 7 | 5 | 4 | 2 | -18 | 24 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c02_grid_capex_requires_backlog_CAPA_ASP_margin_bridge","scope":"C02_POWER_GRID_DATACENTER_CAPEX","candidate_action":"stage2_required_bridge","rule":"Do not promote power grid/datacenter capex labels above Stage2 unless firm order quality, backlog, CAPA lock, ASP, delivery schedule, customer mix, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["103590","267260_late"],"counterbalanced_by":["267260_early","010120","298040"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c02_transformer_switchgear_positive_delta","scope":"C02_POWER_GRID_DATACENTER_CAPEX","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Transformer and switchgear leaders with visible backlog, CAPA lock, ASP uplift, and OPM/FCF bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["267260_early","010120","298040"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c02_power_cable_high_MAE_guard","scope":"C02_POWER_GRID_DATACENTER_CAPEX","candidate_action":"stage2_to_yellow_with_high_MAE_guardrail","rule":"Power cable/transmission optionality can be Yellow only when backlog, ASP, delivery cadence, raw-material pass-through, and margin conversion are verified; high MAE blocks Green.","supporting_cases":["103590"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c02_transformer_late_chase_4b_guard","scope":"C02_POWER_GRID_DATACENTER_CAPEX","candidate_action":"local_4b_watch_guard","rule":"If a transformer/grid leader entry follows a large price extension and lacks fresh backlog/margin evidence, cap at local 4B or event-cap.","supporting_cases":["267260_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","round":"R1","loop":"96","positive_rows":3,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C02 should separate true transformer/switchgear CAPA-lock and ASP/margin winners from power-cable optionality with high MAE and transformer-leader late-chase price-only extension.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_high_MAE_guardrail","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","sample_count":5,"avg_mfe_pct":71.85,"avg_mae_pct":-15.16,"median_mfe_pct":56.69,"median_mae_pct":-12.13,"interpretation":"C02 has explosive upside when backlog, CAPA lock, ASP, and margin bridge are credible; optional cable rows and late-chase leader entries require strict 4B/Yellow guardrails."}
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
- Ingest this C02 R1 loop 96 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c02_grid_capex_requires_backlog_CAPA_ASP_margin_bridge -> stage2_required_bridge
  2. c02_transformer_switchgear_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c02_power_cable_high_MAE_guard -> stage2_to_yellow_with_high_MAE_guardrail
  4. c02_transformer_late_chase_4b_guard -> local_4b_watch_guard

Expected behavior:
- Power grid/datacenter CAPEX vocabulary alone should not create Green.
- Firm order quality, backlog, CAPA lock, ASP, delivery schedule, customer mix, OPM, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Cable optionality and late-chase transformer rows should remain capped until fresh backlog/margin evidence appears.
```
