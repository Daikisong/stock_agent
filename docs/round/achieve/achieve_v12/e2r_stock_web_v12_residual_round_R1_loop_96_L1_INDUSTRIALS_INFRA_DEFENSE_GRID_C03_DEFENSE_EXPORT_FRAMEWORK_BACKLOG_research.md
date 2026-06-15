# E2R Stock-Web v12 Residual Research — R1 loop 96 / L1 / C03

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 96
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_DEFENSE_THEME_EVENT_CAP
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
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

이번 파일은 `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` 전용 residual research다. 목적은 방산 export/framework/backlog headline을 반복 증명하는 것이 아니라, 그 headline이 실제로 다음 경로로 번역되는지 확인하는 것이다.

```text
export framework / government customer / backlog
  → delivery schedule / acceptance
  → margin conversion / revision bridge
  → stock-web 1D OHLC forward path
```

C03은 단순 “방산 테마”가 아니다. 방산 수출은 긴 다리다. 계약·MOU·정부 발표가 첫 교각이고, 납품 일정과 인식 매출이 중간 교각이며, 마진과 revision이 마지막 교각이다. 마지막 교각이 없으면 가격은 강을 건너기 전에 들뜬다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["012450","079550","064350","047810"],"profile_paths":["atlas/symbol_profiles/012/012450.json","atlas/symbol_profiles/079/079550.json","atlas/symbol_profiles/064/064350.json","atlas/symbol_profiles/047/047810.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv","atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv"],"validation_scope":"2024 trigger-level forward path only; old corporate-action candidate dates outside the local windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index priority 1 has C03 at 30 rows and asks for defense export contract, backlog, delivery schedule, and margin conversion expansion.
- Existing registry shows C03 latest parsed file at `R1 loop 95`.
- This output uses `R1 loop 96`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file uses four 2024 paths: `012450`, `079550`, `064350`, `047810`.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C03-R1L96-01 | 012450 | 한화에어로스페이스 | 2024-02-26 | 2024-02-26 | 166200 | 425000 | 155800 | 155.72% | -6.26% | Export backlog + delivery/margin bridge positive path. |
| C03-R1L96-02 | 079550 | LIG넥스원 | 2024-02-14 | 2024-02-14 | 127000 | 265000 | 115400 | 108.66% | -9.13% | Defense electronics/export backlog path; strong but volatile. |
| C03-R1L96-03 | 064350 | 현대로템 | 2024-02-22 | 2024-02-22 | 34500 | 68000 | 29900 | 97.10% | -13.33% | Land systems / K2 export framework path, but rail/defense mix and MAE guardrail matter. |
| C03-R1L96-04 | 047810 | 한국항공우주 | 2024-05-28 | 2024-05-28 | 58600 | 60500 | 48000 | 3.24% | -18.09% | Aerospace export headline/event path without enough margin/revision bridge; event-cap counterexample. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C03-R1L96-01","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE","symbol":"012450","name":"한화에어로스페이스","trigger_type":"defense_export_backlog_delivery_margin_bridge","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":166200,"peak_price":425000,"peak_date":"2024-11-12","trough_price":155800,"trough_date":"2024-02-26","mfe_pct":155.72,"mae_pct":-6.26,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Stage3-Green_candidate","residual_flag":"positive_bridge_confirmation_but_requires_exact_delivery_margin_url","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|defense_export_backlog_delivery_margin_bridge|2024-02-26"}
{"row_type":"trigger","case_id":"C03-R1L96-02","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_ELECTRONICS_EXPORT_BACKLOG_MARGIN_BRIDGE","symbol":"079550","name":"LIG넥스원","trigger_type":"defense_electronics_export_backlog_framework","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":127000,"peak_price":265000,"peak_date":"2024-10-22","trough_price":115400,"trough_date":"2024-02-14","mfe_pct":108.66,"mae_pct":-9.13,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate","residual_flag":"positive_but_high_entry_day_volatility","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|079550|defense_electronics_export_backlog_framework|2024-02-14"}
{"row_type":"trigger","case_id":"C03-R1L96-03","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"LAND_SYSTEMS_EXPORT_FRAMEWORK_DELIVERY_BACKLOG","symbol":"064350","name":"현대로템","trigger_type":"land_systems_export_framework_backlog","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":34500,"peak_price":68000,"peak_date":"2024-10-18","trough_price":29900,"trough_date":"2024-03-12","mfe_pct":97.10,"mae_pct":-13.33,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_MAE_guardrail","residual_flag":"land_systems_positive_but_rail_defense_mix_requires_margin_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|land_systems_export_framework_backlog|2024-02-22"}
{"row_type":"trigger","case_id":"C03-R1L96-04","round":"R1","loop":"96","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"AEROSPACE_EXPORT_FRAMEWORK_EVENT_CAP_COUNTEREXAMPLE","symbol":"047810","name":"한국항공우주","trigger_type":"aerospace_export_framework_event_cap","trigger_date":"2024-05-28","entry_date":"2024-05-28","entry_price":58600,"peak_price":60500,"peak_date":"2024-10-30","trough_price":48000,"trough_date":"2024-08-05","mfe_pct":3.24,"mae_pct":-18.09,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap_not_Green","residual_flag":"counterexample_export_headline_without_revision_margin_bridge","dedupe_key":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|047810|aerospace_export_framework_event_cap|2024-05-28"}
```

## 6. Score-return alignment

### 6.1 Positive alignment

`012450` and `079550` show that C03 can deserve a higher sector-specific bridge score when the evidence is not just “defense theme” but export backlog plus delivery acceptance plus margin/revision visibility. In those cases the return path is not a single candle; the move keeps reloading through later windows. That behavior is exactly what C03 should catch.

### 6.2 Guardrail alignment

`064350` shows a useful middle case. It works as a C03 positive, but it is not a clean pure-defense profile. The stock can be driven by land systems export expectation while the company still has a rail/industrial mix. That means Stage3-Green should require evidence of defense-margin conversion rather than just K2 export vocabulary.

### 6.3 Counterexample alignment

`047810` is the event-cap case. It has defense/aerospace export vocabulary, but the 2024 path does not reward a May chase unless the model can see a stronger margin/revision bridge. MFE is tiny and MAE is deep. This is not a “no defense exposure” failure; it is a “framework headline without near-term conversion bridge” failure.

## 7. Raw component score simulation

| symbol | industrial evidence | order/backlog bridge | revision/margin bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 012450 | 23 | 24 | 20 | 20 | -3 | 84 | Stage3-Yellow/Green candidate pending URLs |
| 079550 | 22 | 21 | 17 | 19 | -5 | 74 | Stage3-Yellow candidate |
| 064350 | 20 | 20 | 13 | 18 | -8 | 63 | Stage2/Yellow with MAE guardrail |
| 047810 | 16 | 12 | 6 | 4 | -12 | 26 | Event-cap / counterexample |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c03_export_backlog_delivery_margin_bridge","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage2_required_bridge","rule":"Do not promote defense export/framework headlines above Stage2 unless at least one of delivery schedule, backlog conversion, margin guidance, or revision bridge is present.","supporting_cases":["047810"],"counterbalanced_by":["012450","079550","064350"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_pure_theme_event_cap","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"local_4b_watch_guard","rule":"If price is extended but evidence is only defense theme / export discussion without contract-quality backlog or margin conversion, cap at Yellow or local 4B watch.","supporting_cases":["047810"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c03_backlog_margin_bridge_positive_delta","scope":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"If export backlog, delivery schedule, customer/government visibility, and margin/revision bridge are all present, allow stronger Stage3-Yellow/Green candidate treatment even after prior price strength, subject to MAE guardrail.","supporting_cases":["012450","079550"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","round":"R1","loop":"96","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C03 needs stronger distinction between export/backlog conversion and generic defense theme event-cap.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","stage3_yellow_to_green_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","sample_count":4,"avg_mfe_pct":91.18,"avg_mae_pct":-11.70,"median_mfe_pct":102.88,"median_mae_pct":-11.23,"interpretation":"C03 has strong upside when backlog/margin conversion is real, but event-cap and high-MAE guardrails are needed for framework-only or late-chase entries."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - 012450 and 064350 have old corporate-action profile caveats outside the local 2024 window; local 2024 rows used here are not blocked by those historical profile dates
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C03 R1 loop 96 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.
- Candidate axes to test after URL verification:
  1. c03_export_backlog_delivery_margin_bridge -> stage2_required_bridge
  2. c03_pure_theme_event_cap -> local_4b_watch_guard
  3. c03_backlog_margin_bridge_positive_delta -> stage3_yellow_to_green_candidate_delta

Expected behavior:
- Defense export framework alone should not create Green.
- Export backlog plus delivery schedule plus margin/revision bridge can justify Stage3-Yellow/Green candidate status.
- Late price-only defense theme chase should be capped at event-cap or local 4B watch.
```
