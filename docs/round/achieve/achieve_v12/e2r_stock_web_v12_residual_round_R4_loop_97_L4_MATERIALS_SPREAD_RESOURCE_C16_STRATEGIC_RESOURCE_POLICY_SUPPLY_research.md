# E2R Stock-Web v12 Residual Research — R4 loop 97 / L4 / C16

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 97
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: COPPER_LITHIUM_RESOURCE_TRADING_OFFTAKE_MARGIN_BRIDGE_VS_RESOURCE_POLICY_LABEL_HIGH_MAE_EVENT_CAP
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - high_MAE_guardrail
  - strategic_resource_policy_supply_bridge_test
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` 전용 residual research다.

C16은 “구리·리튬·자원·공급망·정책”이라는 단어가 보였다는 이유로 Green을 주는 bucket이 아니다. C16은 다음 다리를 확인해야 한다.

```text
strategic resource / policy / supply-chain headline
  → offtake / physical supply / trading volume / production ramp
  → price pass-through / margin capture / cash conversion
  → stock-web 1D OHLC forward path
```

자원 테마는 불꽃처럼 빠르게 붙는다. 하지만 그 불꽃이 용광로가 되려면 실제 물량, 판매처, 스프레드, 현금흐름이 필요하다. 이번 샘플은 그 차이를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["006260","047050","005490","001120"],"profile_paths":["atlas/symbol_profiles/006/006260.json","atlas/symbol_profiles/047/047050.json","atlas/symbol_profiles/005/005490.json","atlas/symbol_profiles/001/001120.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","atlas/ohlcv_tradable_by_symbol_year/047/047050/2024.csv","atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv","atlas/ohlcv_tradable_by_symbol_year/001/001120/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action caveats outside local windows are not used as local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C16 at 30 rows and asks for strategic-resource policy versus actual offtake/margin/supply-chain execution expansion.
- Existing registry shows C16 latest parsed file at R4 loop 96.
- This output uses R4 loop 97.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file uses four 2024 paths: `006260`, `047050`, `005490`, `001120`.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C16-R4L97-01 | 006260 | LS | 2024-04-12 | 2024-04-12 | 122100 | 194800 | 93300 | 59.54% | -23.59% | Copper/electrification resource supply chain was strong, but late-chase and high-MAE guardrail matter. |
| C16-R4L97-02 | 047050 | POSCO International | 2024-06-03 | 2024-06-03 | 51200 | 72800 | 44000 | 42.19% | -14.06% | Resource trading / energy supply-chain event created real MFE but still needed offtake/cash bridge. |
| C16-R4L97-03 | 005490 | POSCO Holdings | 2024-04-29 | 2024-04-29 | 407000 | 412000 | 309000 | 1.23% | -24.08% | Lithium/resource label without near-term cash conversion acted as event-cap counterexample. |
| C16-R4L97-04 | 001120 | LX International | 2024-05-20 | 2024-05-20 | 32900 | 35950 | 26200 | 9.27% | -20.36% | Resource/trading spike lacked durable margin bridge; MFE was small relative to MAE. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C16-R4L97-01","round":"R4","loop":"97","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ELECTRIFICATION_SUPPLY_CHAIN_PRICE_PASS_THROUGH_HIGH_MAE","symbol":"006260","name":"LS","trigger_type":"copper_electrification_supply_chain_price_pass_through","trigger_date":"2024-04-12","entry_date":"2024-04-12","entry_price":122100,"peak_price":194800,"peak_date":"2024-05-21","trough_price":93300,"trough_date":"2024-09-09","mfe_pct":59.54,"mae_pct":-23.59,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_high_MAE_guardrail","residual_flag":"positive_mfe_but_deep_drawdown_requires_offtake_margin_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006260|copper_electrification_supply_chain_price_pass_through|2024-04-12"}
{"row_type":"trigger","case_id":"C16-R4L97-02","round":"R4","loop":"97","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RESOURCE_TRADING_ENERGY_SUPPLY_CHAIN_EVENT_TO_CASH_BRIDGE","symbol":"047050","name":"POSCO International","trigger_type":"resource_trading_energy_supply_chain_event","trigger_date":"2024-06-03","entry_date":"2024-06-03","entry_price":51200,"peak_price":72800,"peak_date":"2024-06-14","trough_price":44000,"trough_date":"2024-08-05","mfe_pct":42.19,"mae_pct":-14.06,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_candidate","residual_flag":"fast_mfe_requires_confirmation_of_physical_supply_or_cash_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047050|resource_trading_energy_supply_chain_event|2024-06-03"}
{"row_type":"trigger","case_id":"C16-R4L97-03","round":"R4","loop":"97","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_POLICY_LABEL_WITHOUT_NEAR_TERM_CASH_CONVERSION","symbol":"005490","name":"POSCO Holdings","trigger_type":"lithium_resource_policy_label_no_cash_conversion","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":407000,"peak_price":412000,"peak_date":"2024-04-30","trough_price":309000,"trough_date":"2024-08-05","mfe_pct":1.23,"mae_pct":-24.08,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_local_4B_watch_not_Green","residual_flag":"counterexample_resource_policy_label_without_offtake_cash_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|lithium_resource_policy_label_no_cash_conversion|2024-04-29"}
{"row_type":"trigger","case_id":"C16-R4L97-04","round":"R4","loop":"97","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RESOURCE_TRADING_COMMODITY_POLICY_SPIKE_SMALL_MFE_HIGH_MAE","symbol":"001120","name":"LX International","trigger_type":"resource_trading_policy_spike_event_cap","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":32900,"peak_price":35950,"peak_date":"2024-05-21","trough_price":26200,"trough_date":"2024-08-05","mfe_pct":9.27,"mae_pct":-20.36,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap","residual_flag":"counterexample_resource_trading_label_without_durable_margin_bridge","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001120|resource_trading_policy_spike_event_cap|2024-05-20"}
```

## 6. Score-return alignment

### 6.1 Positive but volatile paths

`006260` and `047050` show that C16 can generate meaningful MFE when the market connects strategic-resource exposure with electrification, trading, or supply-chain scarcity. However, both paths also show deep post-entry drawdown. That means C16 should not be promoted by keyword alone; the bridge must be seen.

### 6.2 Counterexample paths

`005490` and `001120` show the other side. Resource/lithium/trading labels can create short event windows, but if the evidence does not prove offtake, physical supply execution, or margin/cash conversion, the path can become mostly MAE. These are classic C16 event-cap cases.

### 6.3 Mechanism

The sector behaves like a shipping port. A “resource policy” headline is a ship on the horizon. It is not cargo in the warehouse. The model should score higher only after the cargo clears customs: offtake, volume, price pass-through, margin, and cash.

## 7. Raw component score simulation

| symbol | resource/policy evidence | offtake/supply execution | margin/cash bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 006260 | 22 | 17 | 12 | 18 | -11 | 58 | Stage2/Yellow with high-MAE guardrail |
| 047050 | 19 | 16 | 13 | 16 | -7 | 57 | Stage2/Yellow candidate |
| 005490 | 17 | 7 | 4 | 1 | -12 | 17 | Event-cap / local 4B watch |
| 001120 | 14 | 8 | 5 | 4 | -10 | 21 | Event-cap / counterexample |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c16_resource_policy_requires_offtake_margin_bridge","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage2_required_bridge","rule":"Do not promote strategic-resource/policy labels above Stage2 unless at least one of offtake, physical supply execution, trading volume, price pass-through, margin bridge, or cash conversion is present.","supporting_cases":["005490","001120"],"counterbalanced_by":["006260","047050"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_high_mae_guardrail_for_policy_spikes","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"local_4b_watch_guard","rule":"If C16 price strength is mostly resource-policy vocabulary and the forward path shows high MAE without durable MFE, cap at event-cap/local 4B watch until non-price bridge is verified.","supporting_cases":["005490","001120","006260"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c16_physical_supply_cash_bridge_positive_delta","scope":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_action":"stage3_yellow_candidate_delta","rule":"If strategic-resource policy is paired with observable physical supply, offtake, price pass-through, and margin/cash bridge, allow stronger Stage3-Yellow treatment, but not Green unless drawdown risk is contained.","supporting_cases":["006260","047050"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","round":"R4","loop":"97","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C16 still needs a sharper distinction between strategic-resource label strength and actual offtake/margin/cash conversion.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","sample_count":4,"avg_mfe_pct":28.06,"avg_mae_pct":-20.52,"median_mfe_pct":25.73,"median_mae_pct":-21.98,"interpretation":"C16 resource-policy labels can produce fast upside, but drawdown is large unless offtake/margin/cash bridge is real."}
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
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C16 R4 loop 97 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c16_resource_policy_requires_offtake_margin_bridge -> stage2_required_bridge
  2. c16_high_mae_guardrail_for_policy_spikes -> local_4b_watch_guard
  3. c16_physical_supply_cash_bridge_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Resource-policy vocabulary alone should not create Green.
- Verified offtake / physical supply / price pass-through / margin or cash conversion can justify Stage3-Yellow candidate status.
- High-MAE resource-label spikes should be capped at event-cap or local 4B watch.
```
