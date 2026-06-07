# E2R Stock-Web v12 Residual Research — R4 loop 99 / L4 / C15

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 99
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_ZINC_STEEL_SPECIAL_STEEL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_MATERIAL_SUPERCYCLE_LABEL_HIGH_MAE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - high_MAE_guardrail
  - material_spread_bridge_test
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C15_MATERIAL_SPREAD_SUPERCYCLE` 전용 residual research다.

C15는 “원자재 가격이 오른다”, “소재 supercycle이다”라는 문장을 곧바로 Stage3-Green으로 바꾸는 bucket이 아니다. C15에서 필요한 다리는 다음과 같다.

```text
commodity / material spread headline
  → company-specific ASP / volume / product mix
  → input-cost pass-through / margin capture
  → earnings or cash-flow bridge
  → stock-web 1D OHLC forward path
```

소재 spread는 바람과 돛의 관계다. 바람이 강해도, 돛이 찢어져 있거나 배가 반대 방향을 보고 있으면 앞으로 나가지 않는다. 이번 샘플은 “구리/아연/철강 가격 분위기”와 “회사별 spread capture”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["103140","010130","004020","001430"],"profile_paths":["atlas/symbol_profiles/103/103140.json","atlas/symbol_profiles/010/010130.json","atlas/symbol_profiles/004/004020.json","atlas/symbol_profiles/001/001430.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","atlas/ohlcv_tradable_by_symbol_year/004/004020/2024.csv","atlas/ohlcv_tradable_by_symbol_year/001/001430/2024.csv"],"validation_scope":"2024 trigger-level forward path; governance/tender style contamination is explicitly blocked from promotion when it enters the window."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C15 at 33 rows and asks for spread supercycle versus company-specific ASP/volume/margin conversion expansion.
- Existing registry shows C15 latest parsed file at `R4 loop 98`.
- This output uses `R4 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file uses four 2024 paths: `103140`, `010130`, `004020`, `001430`.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C15-R4L99-01 | 103140 | 풍산 | 2024-04-12 | 2024-04-12 | 61600 | 78900 | 47000 | 28.08% | -23.70% | Copper/product-spread positive MFE, but high-MAE guardrail required. |
| C15-R4L99-02 | 010130 | 고려아연 | 2024-05-20 | 2024-05-20 | 528000 | 557000 | 445000 | 5.49% | -15.72% | Zinc/precious-metal spread label did not become clean C15 Green before later governance contamination. |
| C15-R4L99-03 | 004020 | 현대제철 | 2024-04-29 | 2024-04-29 | 32600 | 32800 | 23750 | 0.61% | -27.15% | Generic steel spread/rebar recovery label failed without actual margin bridge. |
| C15-R4L99-04 | 001430 | 세아베스틸지주 | 2024-05-14 | 2024-05-14 | 23850 | 25700 | 16640 | 7.76% | -30.23% | Special steel/product mix spike failed to hold; margin bridge required before promotion. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C15-R4L99-01","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_PRODUCT_SPREAD_MARGIN_BRIDGE_HIGH_MAE","symbol":"103140","name":"풍산","trigger_type":"copper_product_spread_margin_bridge_high_mae","trigger_date":"2024-04-12","entry_date":"2024-04-12","entry_price":61600,"peak_price":78900,"peak_date":"2024-05-14","trough_price":47000,"trough_date":"2024-08-05","mfe_pct":28.08,"mae_pct":-23.70,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_high_MAE_guardrail","residual_flag":"positive_mfe_but_needs_margin_cash_bridge_and_drawdown_guardrail","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|103140|copper_product_spread_margin_bridge_high_mae|2024-04-12"}
{"row_type":"trigger","case_id":"C15-R4L99-02","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ZINC_PRECIOUS_METAL_SMELTING_SPREAD_VS_GOVERNANCE_CONTAMINATION","symbol":"010130","name":"고려아연","trigger_type":"zinc_precious_metal_spread_governance_contamination_guard","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":528000,"peak_price":557000,"peak_date":"2024-08-28","trough_price":445000,"trough_date":"2024-08-05","mfe_pct":5.49,"mae_pct":-15.72,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap_not_Green","residual_flag":"later_governance_price_path_should_not_be_counted_as_clean_C15_spread_success","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010130|zinc_precious_metal_spread_governance_contamination_guard|2024-05-20"}
{"row_type":"trigger","case_id":"C15-R4L99-03","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"BLAST_FURNACE_STEEL_SPREAD_FALSE_STAGE2","symbol":"004020","name":"현대제철","trigger_type":"generic_steel_spread_false_stage2","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":32600,"peak_price":32800,"peak_date":"2024-04-30","trough_price":23750,"trough_date":"2024-09-09","mfe_pct":0.61,"mae_pct":-27.15,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_4B_watch","residual_flag":"counterexample_steel_label_without_margin_bridge","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|004020|generic_steel_spread_false_stage2|2024-04-29"}
{"row_type":"trigger","case_id":"C15-R4L99-04","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIAL_STEEL_PRODUCT_MIX_SPREAD_FALSE_STAGE2_HIGH_MAE","symbol":"001430","name":"세아베스틸지주","trigger_type":"special_steel_product_mix_spread_false_stage2","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":23850,"peak_price":25700,"peak_date":"2024-05-16","trough_price":16640,"trough_date":"2024-08-05","mfe_pct":7.76,"mae_pct":-30.23,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap","residual_flag":"counterexample_special_steel_spike_without_margin_cash_bridge","dedupe_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|001430|special_steel_product_mix_spread_false_stage2|2024-05-14"}
```

## 6. Score-return alignment

### 6.1 Positive but dangerous path

`103140` shows why C15 exists. Copper/product-spread exposure can generate strong MFE when the market sees metal price and product ASP momentum. But the same path also produced deep drawdown. This should be a Stage2/Yellow candidate with MAE guardrail, not automatic Green.

### 6.2 Contamination guard

`010130` shows why C15 needs contamination control. A later explosive price move can be driven by governance/tender/control-premium dynamics rather than clean material spread. C15 must avoid counting that as a pure spread-supercycle success.

### 6.3 Steel false-positive family

`004020` and `001430` show the false-positive family. “Steel spread” and “special steel product mix” vocabulary can create short spikes, but without actual margin bridge the path becomes low-MFE/high-MAE. These should feed `stage2_required_bridge` and `local_4b_watch_guard`.

## 7. Raw component score simulation

| symbol | material/spread evidence | ASP/volume/product mix | margin/cash bridge | price confirmation | contamination/MAE guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 103140 | 22 | 18 | 12 | 17 | -11 | 58 | Stage2/Yellow with MAE guardrail |
| 010130 | 17 | 12 | 7 | 5 | -12 | 29 | Event-cap / contamination guard |
| 004020 | 15 | 6 | 3 | 1 | -13 | 12 | 4B watch / false Stage2 |
| 001430 | 16 | 8 | 4 | 4 | -14 | 18 | Event-cap / high-MAE false Stage2 |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c15_spread_requires_company_specific_margin_cash_bridge","scope":"C15_MATERIAL_SPREAD_SUPERCYCLE","candidate_action":"stage2_required_bridge","rule":"Do not promote generic material/spread/supercycle labels above Stage2 unless company-specific ASP, volume, product mix, input-cost pass-through, margin, or cash-flow bridge is visible.","supporting_cases":["004020","001430"],"counterbalanced_by":["103140"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c15_high_mae_spread_guardrail","scope":"C15_MATERIAL_SPREAD_SUPERCYCLE","candidate_action":"local_4b_watch_guard","rule":"If MFE is small or drawdown dominates after a material spread headline, cap at local 4B watch/event-cap until non-price bridge is verified.","supporting_cases":["004020","001430","010130"],"counterbalanced_by":["103140"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c15_governance_contamination_block","scope":"C15_MATERIAL_SPREAD_SUPERCYCLE","candidate_action":"blocked_by_logic_risk","rule":"Do not count later governance/tender/control-premium price paths as C15 spread-supercycle success unless the forward window is explicitly split and the spread bridge independently explains the move.","supporting_cases":["010130"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c15_copper_product_spread_positive_delta","scope":"C15_MATERIAL_SPREAD_SUPERCYCLE","candidate_action":"stage3_yellow_candidate_delta","rule":"If copper/product spread evidence is paired with ASP/mix and margin bridge, allow stronger Stage3-Yellow treatment, but keep drawdown guardrail active.","supporting_cases":["103140"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","round":"R4","loop":"99","positive_rows":1,"counterexample_rows":3,"new_symbol_count":4,"primary_residual":"C15 needs stronger separation between material price/supercycle label and company-specific spread/margin/cash bridge, plus contamination control for governance-driven paths.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","blocked_by_logic_risk","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","sample_count":4,"avg_mfe_pct":10.49,"avg_mae_pct":-24.20,"median_mfe_pct":6.63,"median_mae_pct":-25.43,"interpretation":"C15 material-spread headlines tend to produce poor asymmetry unless company-specific spread capture is visible; copper/product spread can work, but high-MAE and contamination guards are required."}
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
  - 010130 later 2024 governance/control-premium-style path is explicitly blocked from clean C15 promotion
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C15 R4 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c15_spread_requires_company_specific_margin_cash_bridge -> stage2_required_bridge
  2. c15_high_mae_spread_guardrail -> local_4b_watch_guard
  3. c15_governance_contamination_block -> blocked_by_logic_risk
  4. c15_copper_product_spread_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Generic material/supercycle vocabulary alone should not create Green.
- Company-specific ASP, volume, product mix, margin, or cash-flow bridge can justify Stage3-Yellow.
- High-MAE spread spikes should be capped at local 4B watch/event-cap.
- Governance or control-premium price paths must not be credited to C15 spread-supercycle logic.
```
