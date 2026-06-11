# E2R v12 Stock-Web Residual Research — R4 / Loop 104 / C16_STRATEGIC_RESOURCE_POLICY_SUPPLY

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 104
round_schedule_status: coverage_index_selected
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_COPPER_CRITICAL_RESOURCE_SUPPLY_CHAIN_OFFTAKE_BRIDGE_VS_RESOURCE_LABEL_PRICE_ONLY_BLOWOFF
sector: materials / strategic resource / lithium / copper / smelting / offtake / supply-chain execution
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
```

## 1. Objective

This run expands `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`, the L4 archetype that tests whether a strategic-resource story is backed by actual resource access, processing/smelting capacity, offtake, customer qualification, and cash-margin conversion.

This is deliberately not a C17 commodity spread run. C17 asks whether price spreads convert to margin. C16 asks whether the firm has a durable resource/supply-chain bridge. The research question is:

```text
Can current calibrated E2R distinguish:
A. real strategic-resource supply-chain execution
from
B. resource-label / mine-MOU / policy-headline price-only blowoff?
```

## 2. Price-source validation

```jsonl
{"row_type":"price_source_validation","repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","min_date":"1995-05-02","max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","validation_status":"pass"}
{"row_type":"price_source_validation","symbol":"005490","name":"POSCO홀딩스","profile_path":"atlas/symbol_profiles/005/005490.json","price_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv","status":"active_like","corporate_action_caveat":"none observed in cited window","validation_status":"pass"}
{"row_type":"price_source_validation","symbol":"006260","name":"LS","profile_path":"atlas/symbol_profiles/006/006260.json","price_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","status":"active_like","corporate_action_caveat":"none observed in cited window","validation_status":"pass"}
{"row_type":"price_source_validation","symbol":"001570","name":"금양","profile_path":"atlas/symbol_profiles/001/001570.json","price_path":"atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv","status":"active_like_until_2025_03_21","corporate_action_caveat":"use tradable 2023 window only; later listing/status caveat not used for 2023 calibration","validation_status":"pass"}
```

## 3. Case set

| case_id | symbol | name | classification | trigger_date | entry_date | entry_close | forward_high | high_date | MFE | forward_low | low_date | MAE | core lesson |
|---|---:|---|---|---|---|---:|---:|---|---:|---:|---|---:|---|
| C16-POSCO-2023-LITHIUM-SUPPLY-BRIDGE | 005490 | POSCO홀딩스 | positive_with_full_4b_watch | 2023-04-10 | 2023-04-10 | 398500 | 764000 | 2023-07-26 | +91.72% | 358000 | 2023-04-05 / pre-entry reference; post-entry low 356000 near May | about -10% stress | real lithium/supply-chain bridge can work, but C16 still needs 4B overlay after parabolic repricing |
| C16-LS-2024-COPPER-SMELTER-BRIDGE | 006260 | LS | positive_with_event_cap_watch | 2024-04-11 | 2024-04-11 | 114900 | 194800 | 2024-05-21 | +69.54% | 112100 | 2024-04-16 | -2.44% | copper/smelting/electrification resource bridge behaves better when linked to processing assets and operating leverage |
| C16-KUMYANG-2023-LITHIUM-LABEL-BLOWOFF | 001570 | 금양 | counterexample_price_only_resource_label | 2023-07-11 | 2023-07-11 | 105900 | 194000 | 2023-07-26 | +83.19% | 84400 | 2023-10-26 | -20.30% | resource label / mine narrative without cash conversion should not become Stage2-Actionable or Green by price alone |

## 4. Case narratives

### 4.1 POSCO홀딩스 / 005490 — real strategic-resource bridge, but parabolic 4B overlay required

`005490` is a better C16 positive control than a pure lithium theme stock because the stock-level story was tied to vertically integrated lithium/battery-material supply-chain execution, not only a mine headline. The stock-web row confirms a strong entry window on 2023-04-10 at 398,500 and a later peak of 764,000 on 2023-07-26.

The important residual point is that this is a *positive bridge with a full-window blowoff tail*. Current calibrated E2R should give Stage2 / Stage2-Actionable credit for actual strategic-resource chain evidence, but it should not allow Stage3-Green to be unlocked solely by the share-price parabola.

```jsonl
{"row_type":"case","case_id":"C16-POSCO-2023-LITHIUM-SUPPLY-BRIDGE","round":"R4","loop":"104","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_UPSTREAM_PROCESSING_SUPPLY_CHAIN_BRIDGE","symbol":"005490","name":"POSCO홀딩스","classification":"positive_with_full_4b_watch","trigger_date":"2023-04-10","entry_date":"2023-04-10","entry_close":398500,"mfe_price":764000,"mfe_date":"2023-07-26","mfe_pct":91.72,"mae_price":356000,"mae_date":"2023-05-window","mae_pct":-10.66,"source_family":"strategic_resource_supply_chain_execution","evidence_family":"lithium_processing_offtake_vertical_integration","validation_scope":"historical_1d_ohlcv_stock_web","price_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv","calibration_use":"usable_positive_but_not_green_unlock"}
{"row_type":"trigger","case_id":"C16-POSCO-2023-LITHIUM-SUPPLY-BRIDGE","trigger_id":"C16-POSCO-20230410-STAGE2A","symbol":"005490","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-10","entry_date":"2023-04-10","entry_price":398500,"mfe_90d_pct":91.72,"mae_90d_pct":-10.66,"peak_date":"2023-07-26","peak_price":764000,"max_drawdown_after_peak_pct":-47.71,"local_4b_proximity":"true","full_window_4b_proximity":"true","thesis_break_4c":"false","classification":"positive_with_full_4b_watch","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|Stage2-Actionable|2023-04-10|2023-04-10"}
```

### 4.2 LS / 006260 — copper/smelting/electrification bridge with shallow early MAE

`006260` works as the copper/smelting side of C16. It is not merely “copper price up”; the group identity includes cable/electrical infrastructure and copper smelting/refining exposure. The stock-web row confirms 2024-04-11 close 114,900, shallow early MAE to 112,100 on 2024-04-16, and a forward high of 194,800 on 2024-05-21.

This is a cleaner positive C16 bridge than a mine-rights rumor because price acceptance came with a real operating asset vocabulary: copper, smelting/refining, electrical infrastructure, and supply-chain bottleneck.

```jsonl
{"row_type":"case","case_id":"C16-LS-2024-COPPER-SMELTER-BRIDGE","round":"R4","loop":"104","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_SMELTING_ELECTRIFICATION_SUPPLY_CHAIN_BRIDGE","symbol":"006260","name":"LS","classification":"positive_with_event_cap_watch","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_close":114900,"mfe_price":194800,"mfe_date":"2024-05-21","mfe_pct":69.54,"mae_price":112100,"mae_date":"2024-04-16","mae_pct":-2.44,"source_family":"copper_supply_chain_and_processing_asset","evidence_family":"copper_smelting_refining_electrification_asset_bridge","validation_scope":"historical_1d_ohlcv_stock_web","price_path":"atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv","calibration_use":"usable_positive_with_4b_watch"}
{"row_type":"trigger","case_id":"C16-LS-2024-COPPER-SMELTER-BRIDGE","trigger_id":"C16-LS-20240411-STAGE2A","symbol":"006260","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":114900,"mfe_90d_pct":69.54,"mae_90d_pct":-2.44,"peak_date":"2024-05-21","peak_price":194800,"local_4b_proximity":"true","full_window_4b_proximity":"watch","thesis_break_4c":"false","classification":"positive_with_event_cap_watch","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006260|Stage2-Actionable|2024-04-11|2024-04-11"}
```

### 4.3 금양 / 001570 — resource-label blowoff, not validated supply execution

`001570` is a useful counterexample because the stock had enormous MFE after resource/lithium-label repricing but later showed the signature of a price-first blowoff. The row shows 2023-07-11 close 105,900, a high of 194,000 on 2023-07-26, and a later low of 84,400 on 2023-10-26.

C16 should not reward this path as “resource supply chain execution” unless the evidence connects to mine economics, offtake, regulatory progress, financing, processing capacity, customer qualification, and cash-margin conversion. Without those, this is a local 4B / event-cap path.

```jsonl
{"row_type":"case","case_id":"C16-KUMYANG-2023-LITHIUM-LABEL-BLOWOFF","round":"R4","loop":"104","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RESOURCE_LABEL_PRICE_ONLY_BLOWOFF","symbol":"001570","name":"금양","classification":"counterexample_price_only_resource_label","trigger_date":"2023-07-11","entry_date":"2023-07-11","entry_close":105900,"mfe_price":194000,"mfe_date":"2023-07-26","mfe_pct":83.19,"mae_price":84400,"mae_date":"2023-10-26","mae_pct":-20.30,"source_family":"resource_label_theme_without_cash_bridge","evidence_family":"lithium_mine_label_no_validated_offtake_margin_bridge","validation_scope":"historical_1d_ohlcv_stock_web","price_path":"atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv","calibration_use":"usable_counterexample"}
{"row_type":"trigger","case_id":"C16-KUMYANG-2023-LITHIUM-LABEL-BLOWOFF","trigger_id":"C16-KUMYANG-20230711-LOCAL4B","symbol":"001570","trigger_type":"local_4B_watch","trigger_date":"2023-07-11","entry_date":"2023-07-11","entry_price":105900,"mfe_90d_pct":83.19,"mae_90d_pct":-20.30,"peak_date":"2023-07-26","peak_price":194000,"local_4b_proximity":"true","full_window_4b_proximity":"true","thesis_break_4c":"watch","classification":"counterexample_price_only_resource_label","dedupe_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001570|local_4B_watch|2023-07-11|2023-07-11"}
```

## 5. Raw component score simulation

The following simulation is shadow-only. It does not patch production scoring.

```jsonl
{"row_type":"score_simulation","case_id":"C16-POSCO-2023-LITHIUM-SUPPLY-BRIDGE","symbol":"005490","stage_current_proxy":"Stage2-Actionable","raw_component_score":{"structural_revenue_growth":16,"eps_revision":14,"margin_cash_bridge":12,"strategic_resource_supply_visibility":19,"valuation_risk":-7,"red_team_risk":-4,"information_confidence":14},"total_score_proxy":64,"stage_after_shadow_rule":"Stage2-Actionable_with_4B_watch","rule_effect":"allow_positive_but_block_green_without_cash_margin_and_no_4b_overlay_clearance"}
{"row_type":"score_simulation","case_id":"C16-LS-2024-COPPER-SMELTER-BRIDGE","symbol":"006260","stage_current_proxy":"Stage2-Actionable","raw_component_score":{"structural_revenue_growth":15,"eps_revision":13,"margin_cash_bridge":13,"strategic_resource_supply_visibility":17,"valuation_risk":-5,"red_team_risk":-3,"information_confidence":13},"total_score_proxy":63,"stage_after_shadow_rule":"Stage2-Actionable_with_event_cap_watch","rule_effect":"positive_credit_when_resource_supply_chain_ties_to_processing_asset_and_margin_path"}
{"row_type":"score_simulation","case_id":"C16-KUMYANG-2023-LITHIUM-LABEL-BLOWOFF","symbol":"001570","stage_current_proxy":"Stage2_or_Yellow_false_positive_risk","raw_component_score":{"structural_revenue_growth":8,"eps_revision":3,"margin_cash_bridge":1,"strategic_resource_supply_visibility":5,"valuation_risk":-15,"red_team_risk":-14,"information_confidence":4},"total_score_proxy":-8,"stage_after_shadow_rule":"4B_watch_or_block_positive_stage","rule_effect":"block_stage2_actionable_when_resource_label_lacks_offtake_margin_cash_bridge"}
```

## 6. Aggregate

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"104","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","case_count":3,"trigger_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"median_mfe_pct":83.19,"median_mae_pct":-10.66,"local_4b_count":3,"full_window_4b_count":2,"hard_4c_count":0,"coverage_contribution":"Priority 1 C16 +3 rows toward 50-row target","dedupe_status":"no hard duplicate detected against provided no-repeat index summary; symbol/date/trigger families selected to avoid known top repeats"}
```

## 7. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"104","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_rule_id":"c16_resource_supply_offtake_cash_bridge_required_for_stage2_actionable_shadow_only","rule_type":"stage2_required_bridge","positive_condition":"resource access or processing capacity plus offtake/customer/financing/progress evidence and at least one margin/cash conversion proxy","negative_condition":"mine-MOU/resource-label/policy headline only; no offtake, no financing, no regulatory milestone, no processing ramp, no margin/cash bridge","recommended_action":"allow Stage2-Actionable only when non-price strategic-resource bridge exists; otherwise route to watch/4B even if MFE is high","production_scoring_changed":false}
{"row_type":"shadow_weight","round":"R4","loop":"104","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","candidate_rule_id":"c16_full_4b_after_resource_blowoff_overlay","rule_type":"full_4b_overlay_candidate","positive_condition":"MFE > 60% within 60 trading days and evidence remains resource-label or early project only","negative_condition":"proven offtake/processing/customer cash bridge with shallow MAE and sustained revision support","recommended_action":"do not let parabolic resource repricing unlock Green; require post-spike consolidation and non-price proof","production_scoring_changed":false}
```

## 8. Residual contribution

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"104","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c16_resource_supply_offtake_cash_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C16 lithium/copper resource-label blowoffs","existing_axis_weakened":null,"why_it_matters":"C16 has many high-MFE resource stories; without an offtake/cash/margin bridge, current calibrated profile can still over-credit resource labels as actionable"}
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the deferred coding agent for stock_agent v12 batch calibration.

Input MD:
e2r_stock_web_v12_residual_round_R4_loop_104_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md

Task:
1. Parse the machine-readable JSONL rows.
2. Validate symbol/date/trigger dedupe keys.
3. Add the three representative C16 trigger rows if not already present:
   - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|Stage2-Actionable|2023-04-10|2023-04-10
   - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|006260|Stage2-Actionable|2024-04-11|2024-04-11
   - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|001570|local_4B_watch|2023-07-11|2023-07-11
4. Consider the shadow-only rule:
   c16_resource_supply_offtake_cash_bridge_required_for_stage2_actionable_shadow_only
5. Do not lower Green thresholds.
6. Keep production scoring unchanged unless this MD is included in a larger reviewed batch.
```

## 10. Final status

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 1
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C15_MATERIAL_SPREAD_SUPERCYCLE
```
