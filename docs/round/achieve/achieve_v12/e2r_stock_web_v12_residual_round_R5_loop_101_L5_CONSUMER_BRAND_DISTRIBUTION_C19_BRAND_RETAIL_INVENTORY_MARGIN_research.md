# E2R Stock-Web v12 Residual Research — R5 / Loop 101 / C19_BRAND_RETAIL_INVENTORY_MARGIN

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 101
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection Rationale

`V12_Research_No_Repeat_Index.md` still classifies `C19_BRAND_RETAIL_INVENTORY_MARGIN` as Priority 0: 21 rows, 12 symbols, with repeated coverage concentrated in `004170`, `036620`, `282330`, `023530`, `298540`, and `007070`. This loop therefore adds four new C19-mapped symbols: `111770`, `081660`, `020000`, and `069960`.

This is not a live scan and not a production scoring patch. It is a historical trigger-level residual calibration file using `Songdaiki/stock-web` 1D OHLCV rows.

## 2. Price Atlas Validation

Stock-web manifest confirms:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
```

Profile checks:

| symbol | name | profile status | corporate-action overlap with entry~D+180 |
|---|---|---|---|
| 081660 | 휠라홀딩스 / 미스토홀딩스 | active_like, raw_unadjusted_marcap | none; historical candidate outside selected 2024 window |
| 069960 | 현대백화점 | active_like, raw_unadjusted_marcap | none |
| 111770 | 영원무역 | active_like, raw_unadjusted_marcap | none |
| 020000 | 한섬 | active_like, raw_unadjusted_marcap | none; historical candidates outside selected 2024 window |

All four rows are calibration-usable under the 30D/90D/180D trigger-row requirement.

## 3. Case Compression

C19 should not treat every department-store, apparel, OEM, or retail vocabulary rebound as a durable rerating. The durable route is:

```text
inventory normalization / sell-through improvement
  -> gross-margin or operating-margin bridge
  -> channel quality / pricing discipline
  -> earnings revision or cash conversion
  -> controlled Stage2-Actionable or Stage3-Yellow
```

The false-positive route is:

```text
retail / brand / fashion rebound label
  -> local MFE after oversold price move
  -> no sell-through or inventory-turn evidence
  -> margin bridge fades
  -> high MAE / failed rerating
  -> Stage2 watch or local 4B cap
```

## 4. Case Table

| case_id | symbol | role | entry | 180D MFE/MAE | residual lesson |
|---|---|---:|---:|---:|---|
| C19-R5-L101-081660-2024-04-01 | 081660 휠라홀딩스 | structural_success + 4B watch | 38,550 | +16.60 / -5.19 | brand cleanup can work when inventory/margin bridge is visible, but Green still needs revision proof |
| C19-R5-L101-069960-2024-01-29 | 069960 현대백화점 | mixed_positive | 51,200 | +20.90 / -13.96 | retail value/reopening label produced MFE, but sell-through durability was capped by later drawdown |
| C19-R5-L101-111770-2024-01-29 | 111770 영원무역 | failed_rerating_counterexample | 44,400 | +18.69 / -27.70 | OEM/apparel rebound without clear inventory-to-margin bridge became a high-MAE failed rerating |
| C19-R5-L101-020000-2024-02-07 | 020000 한섬 | failed_rerating_counterexample | 21,550 | +0.46 / -27.42 | domestic fashion inventory label produced little upside and persistent MAE |

## 5. Machine-Readable Case Rows

```jsonl
{"row_type":"case","case_id":"C19-R5-L101-081660-2024-04-01","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","symbol":"081660","name":"휠라홀딩스","case_role":"structural_success","summary":"brand_inventory_cleanup_margin_bridge_with_local_4b_watch","novelty_basis":"new_symbol_for_C19_not_in_no_repeat_top_covered_symbols","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C19-R5-L101-069960-2024-01-29","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","symbol":"069960","name":"현대백화점","case_role":"mixed_positive","summary":"department_store_retail_value_rebound_with_sellthrough_durability_gap","novelty_basis":"new_symbol_for_C19_not_in_no_repeat_top_covered_symbols","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C19-R5-L101-111770-2024-01-29","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","symbol":"111770","name":"영원무역","case_role":"failed_rerating_counterexample","summary":"apparel_oem_rebound_without_inventory_to_margin_revision_followthrough","novelty_basis":"new_symbol_for_C19_not_in_no_repeat_top_covered_symbols","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C19-R5-L101-020000-2024-02-07","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","symbol":"020000","name":"한섬","case_role":"failed_rerating_counterexample","summary":"domestic_fashion_inventory_label_without_sellthrough_margin_revision_bridge","novelty_basis":"new_symbol_for_C19_not_in_no_repeat_top_covered_symbols","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 6. Machine-Readable Trigger Rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","case_id":"C19-R5-L101-081660-2024-04-01","symbol":"081660","name":"휠라홀딩스","trigger_type":"Stage2-Actionable","entry_date":"2024-04-01","entry_price":38550,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":7.13,"MAE_30D_pct":-3.24,"MFE_90D_pct":15.56,"MAE_90D_pct":-5.19,"MFE_180D_pct":16.60,"MAE_180D_pct":-5.19,"same_entry_group_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN:081660:2024-04-01:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated","corporate_action_window_check":"profile corporate_action_candidate_dates do not overlap entry_date_to_D180","source_proxy_only":true,"evidence_url_pending":true,"case_role":"structural_success","path_label":"brand_inventory_cleanup_margin_bridge_with_local_4b_watch","current_profile_error_type":"calibrated_profile_underweights_brand_cleanup_when_inventory_margin_bridge_exists_but_green_must_stay_blocked_without_revision","stage_call":"Stage2-Actionable -> Stage3-Yellow candidate; local 4B watch if price runs ahead of margin proof","raw_component_score_breakdown":{"EPS/FCF Explosion":12,"Earnings Visibility and Quality":17,"Bottleneck and Pricing Power":6,"Market Mispricing":15,"Valuation Rerating Runway":13,"Capital Allocation":7,"Information Confidence":9},"simulated_total_score":79,"score_return_alignment":"positive"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","case_id":"C19-R5-L101-069960-2024-01-29","symbol":"069960","name":"현대백화점","trigger_type":"Stage2-Actionable","entry_date":"2024-01-29","entry_price":51200,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":20.90,"MAE_30D_pct":-1.95,"MFE_90D_pct":20.90,"MAE_90D_pct":-8.50,"MFE_180D_pct":20.90,"MAE_180D_pct":-13.96,"same_entry_group_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN:069960:2024-01-29:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated","corporate_action_window_check":"profile corporate_action_candidate_dates do not overlap entry_date_to_D180","source_proxy_only":true,"evidence_url_pending":true,"case_role":"mixed_positive","path_label":"department_store_retail_value_rebound_with_sellthrough_durability_gap","current_profile_error_type":"retail_value_rebound_generates_MFE_but_needs_sellthrough_margin_bridge_before_actionable_stage","stage_call":"Stage2-Actionable -> local Stage4B watch; not Green","raw_component_score_breakdown":{"EPS/FCF Explosion":9,"Earnings Visibility and Quality":16,"Bottleneck and Pricing Power":6,"Market Mispricing":15,"Valuation Rerating Runway":14,"Capital Allocation":7,"Information Confidence":10},"simulated_total_score":77,"score_return_alignment":"mixed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","case_id":"C19-R5-L101-111770-2024-01-29","symbol":"111770","name":"영원무역","trigger_type":"Stage2","entry_date":"2024-01-29","entry_price":44400,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":18.69,"MAE_30D_pct":-4.50,"MFE_90D_pct":18.69,"MAE_90D_pct":-27.70,"MFE_180D_pct":18.69,"MAE_180D_pct":-27.70,"same_entry_group_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN:111770:2024-01-29:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated","corporate_action_window_check":"profile corporate_action_candidate_dates do not overlap entry_date_to_D180","source_proxy_only":true,"evidence_url_pending":true,"case_role":"failed_rerating_counterexample","path_label":"apparel_oem_rebound_without_inventory_to_margin_revision_followthrough","current_profile_error_type":"short_MFE_from_rebound_should_not_count_as_actionable_without_inventory_turn_and_margin_revision","stage_call":"Stage2 watch only; high-MAE guard should cap at local 4B","raw_component_score_breakdown":{"EPS/FCF Explosion":5,"Earnings Visibility and Quality":11,"Bottleneck and Pricing Power":5,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":8},"simulated_total_score":58,"score_return_alignment":"negative"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","case_id":"C19-R5-L101-020000-2024-02-07","symbol":"020000","name":"한섬","trigger_type":"Stage2","entry_date":"2024-02-07","entry_price":21550,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":0.46,"MAE_30D_pct":-12.71,"MFE_90D_pct":0.46,"MAE_90D_pct":-19.03,"MFE_180D_pct":0.46,"MAE_180D_pct":-27.42,"same_entry_group_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN:020000:2024-02-07:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated","corporate_action_window_check":"profile corporate_action_candidate_dates do not overlap entry_date_to_D180","source_proxy_only":true,"evidence_url_pending":true,"case_role":"failed_rerating_counterexample","path_label":"domestic_fashion_inventory_label_without_sellthrough_margin_revision_bridge","current_profile_error_type":"brand_inventory_label_false_positive_when_sellthrough_and_margin_revision_are_absent","stage_call":"Stage1/Stage2 watch; not Stage2-Actionable","raw_component_score_breakdown":{"EPS/FCF Explosion":4,"Earnings Visibility and Quality":10,"Bottleneck and Pricing Power":4,"Market Mispricing":12,"Valuation Rerating Runway":9,"Capital Allocation":4,"Information Confidence":7},"simulated_total_score":50,"score_return_alignment":"negative"}
```

## 7. Machine-Readable Score Simulation Rows

```jsonl
{"row_type":"score_simulation","case_id":"C19-R5-L101-081660-2024-04-01","symbol":"081660","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS/FCF Explosion":12,"Earnings Visibility and Quality":17,"Bottleneck and Pricing Power":6,"Market Mispricing":15,"Valuation Rerating Runway":13,"Capital Allocation":7,"Information Confidence":9},"total_score":79,"current_profile_proxy_stage":"Stage2-Actionable -> Stage3-Yellow candidate; local 4B watch if price outruns margin evidence","stage3_green_allowed":false,"reason_stage3_green_blocked":"C19 requires explicit sell-through, inventory-turn, and margin revision bridge before Green."}
{"row_type":"score_simulation","case_id":"C19-R5-L101-069960-2024-01-29","symbol":"069960","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS/FCF Explosion":9,"Earnings Visibility and Quality":16,"Bottleneck and Pricing Power":6,"Market Mispricing":15,"Valuation Rerating Runway":14,"Capital Allocation":7,"Information Confidence":10},"total_score":77,"current_profile_proxy_stage":"Stage2-Actionable -> local Stage4B watch; not Green","stage3_green_allowed":false,"reason_stage3_green_blocked":"retail value rebound and department-store label need sell-through durability and margin proof."}
{"row_type":"score_simulation","case_id":"C19-R5-L101-111770-2024-01-29","symbol":"111770","trigger_type":"Stage2","raw_component_score_breakdown":{"EPS/FCF Explosion":5,"Earnings Visibility and Quality":11,"Bottleneck and Pricing Power":5,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":8},"total_score":58,"current_profile_proxy_stage":"Stage2 watch only; high-MAE guard should cap at local 4B","stage3_green_allowed":false,"reason_stage3_green_blocked":"MFE came before durable inventory/margin conversion; 90D/180D MAE invalidates Actionable."}
{"row_type":"score_simulation","case_id":"C19-R5-L101-020000-2024-02-07","symbol":"020000","trigger_type":"Stage2","raw_component_score_breakdown":{"EPS/FCF Explosion":4,"Earnings Visibility and Quality":10,"Bottleneck and Pricing Power":4,"Market Mispricing":12,"Valuation Rerating Runway":9,"Capital Allocation":4,"Information Confidence":7},"total_score":50,"current_profile_proxy_stage":"Stage1/Stage2 watch; not Stage2-Actionable","stage3_green_allowed":false,"reason_stage3_green_blocked":"domestic fashion inventory label had almost no MFE and deep MAE; no sell-through or margin revision bridge."}
```

## 8. Machine-Readable Aggregate / Shadow / Residual Rows

```jsonl
{"row_type":"aggregate_metric","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_VS_RETAIL_LABEL_PRICE_ONLY_FALSE_POSITIVE","representative_trigger_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":4,"median_MFE_180D_pct":17.65,"median_MAE_180D_pct":-20.69,"new_axis_proposed":"C19_sellthrough_inventory_turn_margin_revision_bridge_required | C19_retail_brand_label_high_MAE_guard","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail"}
{"row_type":"shadow_weight","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_sellthrough_inventory_turn_margin_revision_bridge_required","proposed_effect":"increase visibility/information requirement for C19 Stage2-Actionable; do not loosen Green","safe_axis":"stage2_required_bridge","shadow_only":true,"production_scoring_changed":false}
{"row_type":"residual_contribution","selected_round":"R5","selected_loop":101,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_found":true,"new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"description":"C19 needs company-level sell-through, inventory-turn, and margin revision proof. Retail or apparel rebound labels create local MFE but repeatedly decay into high-MAE rows when the bridge is missing."}
```

## 9. Residual Rule Candidate

```text
new_axis_proposed =
  C19_sellthrough_inventory_turn_margin_revision_bridge_required
  C19_retail_brand_label_high_MAE_guard

existing_axis_strengthened =
  stage2_required_bridge
  price_only_blowoff_blocks_positive_stage
  full_4b_requires_non_price_evidence
  local_4b_watch_guard
  high_MAE_guardrail

existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

C19 should raise the importance of evidence that links inventory cleanup to gross margin, operating margin, and revision. Price-only retail/value rebound or apparel inventory vocabulary should be capped as Stage2 watch or local 4B unless sell-through durability is visible.

## 10. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 11. Final Research State

```text
completed_round = R5
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false

auto_selected_coverage_gap = C19 rows 21 -> 25 if accepted; still Priority 0, need 5 to 30
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during the research run.

Later coding agent task:
1. Ingest this MD as a v12_sector_archetype_residual artifact.
2. Validate that all trigger rows have canonical trigger_type, entry_date, entry_price, 30D/90D/180D MFE and MAE, price_data_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
3. Add C19_sellthrough_inventory_turn_margin_revision_bridge_required as a shadow-only candidate axis.
4. Stress-test whether C19 should require explicit sell-through, inventory-turn, gross-margin or OPM revision evidence before Stage2-Actionable.
5. Do not loosen Stage3-Green.
6. Keep this as shadow_weight_only until more C19 positive cases are added.
```
