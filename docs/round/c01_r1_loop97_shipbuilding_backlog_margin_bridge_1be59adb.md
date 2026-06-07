# E2R Stock-Web v12 Residual Research — R1 loop 97 / L1 / C01

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 97
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ORDER_BACKLOG_MARGIN_BRIDGE_VS_SHIPYARD_BACKLOG_LABEL_AND_LATE_CHASE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - order_backlog_to_margin_bridge_test
  - shipbuilding_delivery_cash_conversion_guardrail
  - shipyard_late_chase_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C01_ORDER_BACKLOG_MARGIN_BRIDGE` 전용 residual research다.

C01은 “수주잔고”, “조선 업황”, “선가 상승”, “수주 뉴스”라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 수주잔고가 실제 선가/환율/공정 진행률, 비용 안정, 납기, 선수금/운전자본, OPM/FCF/EPS revision으로 내려오는지다.

```text
order backlog / shipbuilding cycle headline
  → firm order and delivery schedule
  → vessel price, FX, cost-to-complete, working capital
  → OPM / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

수주잔고는 조선소의 도크 예약표와 같다. 예약표가 꽉 찼다고 바로 이익이 찍히지는 않는다. 높은 선가로 계약된 배가 제때 건조되고, 원가와 환율이 새지 않고, 인도와 현금 회수가 이어질 때 마진 다리가 완성된다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["009540","010140","042660"],"profile_paths":["atlas/symbol_profiles/009/009540.json","atlas/symbol_profiles/010/010140.json","atlas/symbol_profiles/042/042660.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/009/009540/2024.csv","atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv","atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv"],"validation_scope":"2024 trigger-level forward path; selected local windows avoid active corporate-action contamination. 009540 caveats end 2018, 010140 caveats include 2021, and 042660 caveats are in 2023 before selected 2024 rows."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C01 at 16 rows, 14 rows short of the 30-row minimum stability zone.
- Existing registry shows C01 parsed through `R1 loop 96`.
- This output uses `R1 loop 97`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C01 rows touched ship engine, ship parts, construction machinery, hydraulic components. This file shifts to main shipyard/backlog margin bridge and late-chase timing guard.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C01-R1L97-01 | 009540 | HD한국조선해양 | 2024-04-24 | 2024-04-24 | 129400 | 187000 | 127100 | 44.51% | -1.78% | Holding/shipyard backlog-to-margin rerating worked strongly with contained MAE. |
| C01-R1L97-02 | 010140 | 삼성중공업 | 2024-04-18 | 2024-04-18 | 9540 | 12280 | 8910 | 28.72% | -6.60% | Main shipyard backlog/margin bridge worked, but still needs OPM/FCF proof. |
| C01-R1L97-03 | 042660 | 한화오션 | 2024-04-18 | 2024-04-18 | 33300 | 36400 | 28800 | 9.31% | -13.51% | Shipyard backlog label had MFE, but conversion risk and MAE require margin guard. |
| C01-R1L97-04 | 010140 | 삼성중공업 | 2024-07-26 | 2024-07-26 | 11870 | 12280 | 9530 | 3.45% | -19.71% | Same positive shipyard story became poor risk/reward when chased after extension. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C01-R1L97-01","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_HOLDING_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"009540","name":"HD한국조선해양","trigger_type":"shipbuilding_holding_order_backlog_margin_bridge","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":129400,"peak_price":187000,"peak_date":"2024-07-22","trough_price":127100,"trough_date":"2024-05-07","mfe_pct":44.51,"mae_pct":-1.78,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_OPM_FCF_URLs","residual_flag":"positive_shipbuilding_backlog_margin_path_but_requires_delivery_cash_conversion_URLs","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|009540|shipbuilding_holding_order_backlog_margin_bridge|2024-04-24"}
{"row_type":"trigger","case_id":"C01-R1L97-02","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"MAIN_SHIPYARD_BACKLOG_OPM_FCF_BRIDGE","symbol":"010140","name":"삼성중공업","trigger_type":"main_shipyard_backlog_opm_fcf_bridge","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":9540,"peak_price":12280,"peak_date":"2024-07-26","trough_price":8910,"trough_date":"2024-06-13","mfe_pct":28.72,"mae_pct":-6.60,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_margin_cash_URLs","residual_flag":"positive_main_shipyard_backlog_path_but_OPM_FCF_bridge_required","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|main_shipyard_backlog_opm_fcf_bridge|2024-04-18"}
{"row_type":"trigger","case_id":"C01-R1L97-03","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPYARD_BACKLOG_CONVERSION_MARGIN_GUARD","symbol":"042660","name":"한화오션","trigger_type":"shipyard_backlog_conversion_margin_guard","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":33300,"peak_price":36400,"peak_date":"2024-04-24","trough_price":28800,"trough_date":"2024-05-31","mfe_pct":9.31,"mae_pct":-13.51,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_margin_guard","residual_flag":"shipyard_backlog_label_needs_delivery_cost_OPM_bridge_before_promotion","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|shipyard_backlog_conversion_margin_guard|2024-04-18"}
{"row_type":"trigger","case_id":"C01-R1L97-04","round":"R1","loop":"97","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPYARD_LEADER_LATE_CHASE_PRICE_ONLY_EXTENSION_4B","symbol":"010140","name":"삼성중공업","trigger_type":"shipyard_leader_late_chase_price_only_extension_4b","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":11870,"peak_price":12280,"peak_date":"2024-07-26","trough_price":9530,"trough_date":"2024-09-06","mfe_pct":3.45,"mae_pct":-19.71,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Local_4B_watch_or_event_cap_not_Green","residual_flag":"same_shipyard_story_late_chase_without_fresh_margin_delivery_evidence","dedupe_key":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|shipyard_leader_late_chase_price_only_extension_4b|2024-07-26"}
```

## 6. Score-return alignment

### 6.1 Backlog-to-margin positive family

`009540` and `010140` early are the constructive C01 rows. They show the market rewarding a shipbuilding backlog story when it looked tied to higher vessel prices, improving delivery mix, and potential margin conversion. These rows can support Stage3-Yellow/Green candidates only after exact OPM, FCF, delivery, and cash-conversion evidence is verified.

### 6.2 Backlog label with conversion risk

`042660` is the middle case. The same shipyard/backlog language produced a fast MFE, but the drawdown was larger than the peak upside cushion. This should stay Stage2/Yellow until cost-to-complete, delivery schedule, and working-capital/margin repair are visible.

### 6.3 Same story, different entry

`010140` late is the timing guard. Even when the broad backlog thesis is working, a late entry after price extension can have poor asymmetry. C01 needs a local 4B/event-cap rule when fresh delivery/margin evidence is absent.

## 7. Raw component score simulation

| symbol | order backlog evidence | delivery schedule | vessel price / FX | OPM / FCF bridge | price confirmation | MAE / late-chase guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 009540 | 23 | 18 | 18 | 16 | 23 | -2 | 80 | Stage3-Yellow/Green candidate |
| 010140 early | 22 | 17 | 16 | 13 | 18 | -4 | 72 | Stage3-Yellow candidate |
| 042660 | 20 | 10 | 9 | 6 | 6 | -8 | 43 | Stage2/Yellow with margin guard |
| 010140 late | 22 | 6 | 5 | 4 | 2 | -15 | 24 | Local 4B/event-cap |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c01_backlog_requires_delivery_margin_cash_bridge","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","candidate_action":"stage2_required_bridge","rule":"Do not promote order-backlog/shipbuilding-cycle labels above Stage2 unless firm order quality, delivery schedule, vessel price/FX, cost-to-complete, working capital, OPM, FCF, or EPS revision bridge is visible.","supporting_cases":["042660","010140_late"],"counterbalanced_by":["009540","010140_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c01_shipbuilding_backlog_positive_delta","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Shipbuilding names with visible backlog quality, delivery cadence, vessel price/FX advantage, and OPM/FCF bridge can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["009540","010140_early"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c01_shipyard_conversion_margin_guard","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","candidate_action":"stage2_to_yellow_with_margin_guard","rule":"Shipyard backlog rows with meaningful MAE should stay Stage2/Yellow unless cost-to-complete, working-capital, and margin repair are verified.","supporting_cases":["042660"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c01_shipyard_late_chase_4b_guard","scope":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","candidate_action":"local_4b_watch_guard","rule":"If a shipyard backlog entry follows a large price extension and lacks fresh delivery/margin evidence, cap at local 4B or event-cap.","supporting_cases":["010140_late"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","round":"R1","loop":"97","positive_rows":2,"counterexample_rows":2,"new_symbol_count":3,"primary_residual":"C01 should separate genuine shipbuilding backlog-to-margin conversion from shipyard backlog labels with cost/delivery risk and late-chase price-only extension.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_margin_guard","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","sample_count":4,"avg_mfe_pct":21.50,"avg_mae_pct":-10.40,"median_mfe_pct":19.02,"median_mae_pct":-10.06,"interpretation":"C01 shipbuilding backlog rows can produce strong upside when margin/cash conversion is credible, but conversion-risk and late-chase rows need strict 4B/Yellow guardrails."}
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
- Ingest this C01 R1 loop 97 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c01_backlog_requires_delivery_margin_cash_bridge -> stage2_required_bridge
  2. c01_shipbuilding_backlog_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c01_shipyard_conversion_margin_guard -> stage2_to_yellow_with_margin_guard
  4. c01_shipyard_late_chase_4b_guard -> local_4b_watch_guard

Expected behavior:
- Order backlog / shipbuilding-cycle vocabulary alone should not create Green.
- Firm order quality, delivery schedule, vessel price/FX, cost-to-complete, working capital, OPM, FCF, or EPS revision can justify Stage3-Yellow/Green.
- Conversion-risk and late-chase rows should remain Stage2/Yellow or local 4B until margin/cash evidence appears.
```
