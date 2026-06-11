---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 98
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CATHODE_COPPER_FOIL_SILICON_ANODE_CUSTOMER_CONTRACT_CALLOFF_RISK_BRIDGE_VS_CONTRACT_LABEL_PRICE_SPIKE
loop_contribution_label: canonical_archetype_rule_candidate
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
source_proxy_only: true
evidence_url_pending: true
created_at: 2026-06-06
---

# E2R v12 residual research — R3 loop 98 / L3 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK

## 0. Scope lock

```text
selected_round = R3
selected_loop = 98
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = CATHODE_COPPER_FOIL_SILICON_ANODE_CUSTOMER_CONTRACT_CALLOFF_RISK_BRIDGE_VS_CONTRACT_LABEL_PRICE_SPIKE
```

This is a **historical trigger-level residual research** file. It does not run live discovery, does not patch `stock_agent`, and does not change production scoring. The aim is to stress-test the residual C12 rule: a battery customer contract is not enough by itself; the evidence must survive into shipment acceptance, customer call-off discipline, utilization, margin, and revision.

## 1. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","schema_formula_mfe":"(max high from entry_date through N tradable rows / entry_price - 1) * 100","schema_formula_mae":"(min low from entry_date through N tradable rows / entry_price - 1) * 100","data_quality_policy":"corporate-action windows blocked by default; all selected 2024 windows avoid profile corporate-action candidate dates"}
```

Checked Stock-Web symbol profiles and 2024 tradable shards for:

```text
003670 포스코퓨처엠
005070 코스모신소재
020150 롯데에너지머티리얼즈
078600 대주전자재료
```

All price rows below use `tradable_raw` OHLC from `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv`. Non-price evidence is deliberately marked `source_proxy_only=true` / `evidence_url_pending=true`; this file is therefore **not promotion-ready** until exact public source URLs are attached.

## 2. Research thesis

C12 is the place where the contract book turns into a trap if the customer can slow, defer, call off, or re-time orders. It differs from C11 orderbook rerating because C12 is not asking “is the contract big?” but “can the customer actually take the contracted volume without forcing utilization, ASP, working capital, or margin down?”

The residual pattern is:

```text
customer contract label
  → price spike or relief rally
  → shipment / customer acceptance / take-or-pay / utilization bridge absent
  → EV demand or customer inventory shock
  → high MAE, weak follow-through, local 4B watch or hard 4C risk
```

A C12-positive case should show contract quality plus delivery conversion. A C12-counterexample shows that “contract” is a paper bridge: it sounds solid, but the road under it can still be hollow if the customer is allowed to pull shipment timing back.

## 3. Case matrix

| case_id | symbol | name | role | trigger date | entry date | entry price | interpretation |
|---|---:|---|---|---|---|---:|---|
| C12-R3L98-001 | 003670 | 포스코퓨처엠 | cathode/anode material contract label | 2024-04-24 | 2024-04-24 | 297000 | Counterexample: contract/order narrative did not protect from later customer/demand repricing. |
| C12-R3L98-002 | 005070 | 코스모신소재 | cathode material / utilization bridge | 2024-06-13 | 2024-06-13 | 178200 | Counterexample: late material rally without durable customer call-off proof produced high MAE. |
| C12-R3L98-003 | 020150 | 롯데에너지머티리얼즈 | copper foil / customer contract quality | 2024-05-16 | 2024-05-16 | 49550 | Provisional positive-to-Yellow: MFE existed, but contract quality still needs margin/utilization evidence. |
| C12-R3L98-004 | 078600 | 대주전자재료 | silicon-anode optionality / customer ramp | 2024-06-12 | 2024-06-12 | 160000 | Counterexample: large pre-entry run left little post-entry asymmetry once call-off risk was priced. |

## 4. Backtest trigger rows

```jsonl
{"row_type":"trigger","case_id":"C12-R3L98-001","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CONTRACT_CALLOFF_RISK","symbol":"003670","name":"포스코퓨처엠","trigger_type":"customer_contract_label_without_calloff_protection","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":297000,"entry_price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.68,"mae_30d_pct":-15.66,"mfe_90d_pct":1.68,"mae_90d_pct":-34.18,"mfe_180d_pct":1.68,"mae_180d_pct":-34.18,"peak_price_used":302000,"trough_price_used":195500,"current_profile_expected_stage":"Stage3-Yellow_or_4B_watch","observed_alignment":"negative_asymmetry_after_contract_label","residual_flag":"false_stage2_if_contract_label_not_calloff_protected","source_proxy_only":true,"evidence_url_pending":true,"aggregate_eligible":true}
{"row_type":"trigger","case_id":"C12-R3L98-002","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_MATERIAL_LATE_RALLY_CALLOFF_RISK","symbol":"005070","name":"코스모신소재","trigger_type":"customer_material_contract_label_late_cycle","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":178200,"entry_price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.57,"mae_30d_pct":-26.21,"mfe_90d_pct":1.57,"mae_90d_pct":-46.13,"mfe_180d_pct":1.57,"mae_180d_pct":-46.13,"peak_price_used":181000,"trough_price_used":96000,"current_profile_expected_stage":"4B_watch_or_4C_if_guidance_break","observed_alignment":"late rally reversed into deep drawdown","residual_flag":"calloff_risk_guard_required","source_proxy_only":true,"evidence_url_pending":true,"aggregate_eligible":true}
{"row_type":"trigger","case_id":"C12-R3L98-003","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_CUSTOMER_CONTRACT_QUALITY","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"copper_foil_customer_contract_margin_bridge_test","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":49550,"entry_price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.48,"mae_30d_pct":-10.19,"mfe_90d_pct":19.48,"mae_90d_pct":-13.52,"mfe_180d_pct":19.48,"mae_180d_pct":-13.52,"peak_price_used":59200,"trough_price_used":42850,"current_profile_expected_stage":"Stage2_to_Yellow_only_if_customer_volume_bridge_exists","observed_alignment":"positive_MFE_but_volatile_customer_risk","residual_flag":"positive_case_needs_contract_quality_confirmation","source_proxy_only":true,"evidence_url_pending":true,"aggregate_eligible":true}
{"row_type":"trigger","case_id":"C12-R3L98-004","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SILICON_ANODE_CUSTOMER_RAMP_CALLOFF_RISK","symbol":"078600","name":"대주전자재료","trigger_type":"silicon_anode_customer_ramp_event_cap","trigger_date":"2024-06-12","entry_date":"2024-06-12","entry_price":160000,"entry_price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.13,"mae_30d_pct":-26.31,"mfe_90d_pct":2.13,"mae_90d_pct":-26.31,"mfe_180d_pct":2.13,"mae_180d_pct":-26.31,"peak_price_used":163400,"trough_price_used":117900,"current_profile_expected_stage":"4B_watch","observed_alignment":"optionality_spike_without_post_entry_calloff_protection","residual_flag":"event_cap_required_after_vertical_move","source_proxy_only":true,"evidence_url_pending":true,"aggregate_eligible":true}
```

## 5. Aggregate metric

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","trigger_count":4,"aggregate_eligible_count":4,"positive_or_constructive_count":1,"counterexample_count":3,"avg_mfe_90d_pct":6.22,"avg_mae_90d_pct":-30.03,"median_mfe_90d_pct":1.85,"median_mae_90d_pct":-30.25,"hit_rate_mfe90_gt_20pct":0.0,"high_mae90_lt_minus25pct_rate":0.75,"dominant_residual":"contract_label_without_customer_calloff_protection_creates_false_stage2_or_late_4B","promotion_ready":false,"blocker":"source_proxy_only_and_evidence_url_pending"}
```

## 6. Raw component score simulation

The score simulation is directional and shadow-only. It is not a runtime patch.

| component | current generic contract-label interpretation | C12 residual adjustment candidate |
|---|---:|---:|
| industrial_evidence_score | +8 to +12 if customer/contract vocabulary exists | +0 to +4 unless customer call-off protection, delivery conversion, and shipment timing are explicit |
| revision_score | may rise on orderbook narrative | require actual consensus/guide-through revision; no bonus for old contract backlog alone |
| price_stage_score | may over-reward rebound MFE | cap at Yellow or 4B-watch if price already ran before call-off evidence |
| risk_penalty | generic EV slowdown penalty | add C12-specific call-off/demand-risk penalty when utilization/margin bridge missing |

```jsonl
{"row_type":"score_simulation","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_group":"contract_label_without_calloff_protection","baseline_risk":"Stage2_false_positive_or_late_Yellow","shadow_stage_after_rule":"Yellow_watch_or_4B_watch","reason":"high_MAE_frequency_is_too_large_to_promote_contract_label_without_customer_acceptance_and_margin_bridge"}
{"row_type":"score_simulation","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_group":"contract_quality_with_volume_bridge","baseline_risk":"under-recognized_positive_if_real_delivery_conversion_exists","shadow_stage_after_rule":"Stage2_to_Yellow_candidate","reason":"020150-style MFE shows the rule should not blanket-demote all contract cases; it should demand customer quality proof"}
```

## 7. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"stage2_required_bridge","candidate_rule":"Do not award Stage2 actionable bonus for customer contract vocabulary unless at least one of: explicit shipment acceptance, take-or-pay / non-cancellable volume, customer utilization evidence, margin guidance/revision bridge, or working-capital-normalized cash conversion is present.","suggested_delta":-2.0,"promotion_ready":false,"blocker":"evidence_url_pending"}
{"row_type":"shadow_weight","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"local_4b_watch_guard","candidate_rule":"If entry follows a contract-label price spike but the next visible evidence is EV demand/call-off risk rather than delivery conversion, cap at local 4B-watch even when MFE exists.","suggested_delta":1.0,"promotion_ready":false,"blocker":"source_proxy_only"}
{"row_type":"shadow_weight","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"hard_4c_confirmation","candidate_rule":"If customer call-off, utilization cut, or margin guidance break is confirmed after a contract-driven rerating, upgrade from watch to hard 4C without waiting for price-only breakdown.","suggested_delta":1.0,"promotion_ready":false,"blocker":"needs_exact_non_price_URLs"}
```

## 8. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","contribution_type":"counterexample_mining","summary":"Adds four C12 rows focused on customer contract / call-off risk in cathode, copper foil, and silicon-anode materials. Three of four rows show high MAE or poor post-entry asymmetry when contract vocabulary was not supported by delivery/utilization/margin evidence."}
{"row_type":"residual_contribution","round":"R3","loop":"98","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","contribution_type":"rule_candidate","summary":"Proposes C12-specific bridge requirement: customer contract evidence must be translated into shipment acceptance, call-off protection, utilization, margin/revision, or cash conversion before Stage2 bonus or Green promotion can be considered."}
```

## 9. Validation scope and caveats

```text
usable_for_registry = true
usable_for_production_patch = false
reason = source_proxy_only / evidence_url_pending
price_data = actual Stock-Web 1D OHLC rows
non_price_evidence = proxy narrative only, exact URL pending
corporate_action_window = no selected 2024 entry window overlaps profile corporate-action candidate dates listed in the checked profiles
```

This MD should enter the residual ledger, not the applied-weight ledger. Promotion requires exact source URLs for the customer contract, shipment/call-off, utilization, and margin/revision evidence.

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.

Later coding-agent task:
1. Ingest this MD as a v12 sector-archetype residual research file.
2. Parse all JSONL rows with row_type in {trigger, aggregate_metric, score_simulation, shadow_weight, residual_contribution, price_source_validation}.
3. Validate price_source = Songdaiki/stock-web, price_basis = tradable_raw, price_adjustment_status = raw_unadjusted_marcap.
4. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Keep all shadow_weight rows blocked from promotion until exact non-price source URLs are attached.
6. If URL evidence is later supplied and data quality passes, evaluate the C12 stage2_required_bridge and local_4b_watch_guard candidates against v12 promotion rules.
```
