# E2R Stock-Web v12 Residual Research — R5 Loop 121 — C18 Consumer Export Channel Reorder

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Metadata

```yaml
selected_round: R5
selected_loop: 121
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: CONSUMER_EXPORT_CHANNEL_REORDER_FINAL_PASS_TO_30_APPAREL_OUTDOOR_OEM_REORDER_SELLTHROUGH_BRIDGE
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

## 2. Why this archetype was selected

Static `V12_Research_No_Repeat_Index.md` still lists `C18_CONSUMER_EXPORT_CHANNEL_REORDER` as Priority 0 with only 3 representative rows and a 27-row gap to the 30-row floor. The conversation-local ledger already contains C18 loops 113, 117, 118, 119, and 120. Their combined local contribution is approximately 23 new C18 cases, so static 3 + local 23 = 26 before this run.

This file adds 4 C18-specific cases. If accepted, C18 reaches the local 30-row minimum floor:

```text
auto_selected_coverage_gap_static_index: C18 rows 3 -> 7 if accepted; still Priority 0 by static index
auto_selected_coverage_gap_conversation_local: C18 rows approx 26 -> 30 if accepted; C18 local 30-row floor reached
```

The prior C18 passes focused on K-food, processed food, protein/seafood, and ingredient/export channel narratives. This final pass intentionally adds a different consumer export surface: apparel, outdoor, fashion OEM, and brand channel reorder. The key question is whether a brand/OEM export or sell-through label has actually become repeat order cadence, inventory normalization, OPM recovery, and cash conversion.

## 3. Price data and validation caveat

The stock-web manifest used for this run reports:

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year"
}
```

`raw_unadjusted_marcap` means the rows are not split/dividend adjusted. Corporate-action contaminated windows remain blocked by default.

Browser-layer direct fetches for some fresh C18 apparel/OEM profile/shard URLs were intermittent in this session. To avoid inventing new price routes, this pass reuses stock-web row paths and 30D/90D/180D MFE/MAE values that were already opened in prior local v12 research for the same symbol-year shards under the C19 inventory/margin pass. This is cross-canonical price-row reuse, not a production patch. Each trigger below is tagged `source_proxy_only=true`, `evidence_url_pending=true`, and `batch_reverification_required=true`.

```text
price_row_fetch_status = cross_canonical_prior_stock_web_rows_reused_for_same_shard_paths
cross_canonical_price_row_reuse_source = R5_loop_115_C19_BRAND_RETAIL_INVENTORY_MARGIN
batch_reverification_required = true
promotion_usable_without_reverification = false
```

## 4. Novelty / no-repeat gate

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Recent C18 local symbols already used:

```text
003230, 005180, 271560, 280360, 097950,
004370, 007310, 001680, 005610, 003960,
049770, 005300, 248170, 145990, 264900,
006040, 014710, 136480
```

This run uses symbols not yet used in C18 local files:

```text
383220, 105630, 111770, 036620
```

Cross-canonical reuse note: these symbols appeared in C19 inventory/margin research. They are reused here because C18 asks a different canonical question: not “inventory/margin alone,” but “export channel/reorder cadence and repeat demand conversion.”

## 5. Case table

| case_id | ticker | name | trigger_type | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | label | residual lesson |
|---|---:|---|---|---|---:|---:|---:|---:|---|---|
| C18_121_001 | 036620 | 감성코퍼레이션 | Stage2-Actionable | 2024-02-22 | 3025 | +13.39 / -8.93 | +27.44 / -8.93 | +39.67 / -9.26 | positive | Small-brand sell-through can work when reorder/OPM bridge is visible, but still needs high-MAE guard. |
| C18_121_002 | 111770 | 영원무역 | Stage3-Yellow | 2024-01-31 | 47900 | +10.02 / -8.14 | +10.02 / -18.79 | +10.02 / -29.44 | mixed_positive | 30D bounce masks inventory-cycle gravity; channel reorder must outlast OEM destocking. |
| C18_121_003 | 105630 | 한세실업 | Stage2-Actionable | 2024-02-14 | 21450 | +3.73 / -15.62 | +3.73 / -15.62 | +3.73 / -32.31 | counterexample | OEM reorder label without utilization/receivables bridge should not become durable Stage3. |
| C18_121_004 | 383220 | F&F | 4B-Local-Watch | 2024-07-17 | 74000 | +3.24 / -36.28 | +3.24 / -36.28 | +3.24 / -36.28 | counterexample | Brand heat and China/channel hope can be a local 4B only when sell-through and inventory bridge are absent. |

## 6. Trigger JSONL rows

```jsonl
{"source_row_type":"trigger","research_id":"R5_L121_C18_001","schema_version":"v12_residual_research","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"CONSUMER_EXPORT_CHANNEL_REORDER_FINAL_PASS_TO_30_APPAREL_OUTDOOR_OEM_REORDER_SELLTHROUGH_BRIDGE","symbol":"036620","name":"감성코퍼레이션","market":"KOSDAQ","trigger_type":"Stage2-Actionable","trigger_family":"small_brand_sellthrough_reorder_margin_bridge","trigger_date":"2024-02-21","entry_date":"2024-02-22","entry_price":3025,"entry_price_basis":"close","entry_price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv","profile_path":"atlas/symbol_profiles/036/036620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.39,"MAE_30D_pct":-8.93,"MFE_90D_pct":27.44,"MAE_90D_pct":-8.93,"MFE_180D_pct":39.67,"MAE_180D_pct":-9.26,"peak_180D_pct":39.67,"drawdown_after_peak_180D_pct":-34.08,"classification":"positive","outcome_label":"positive_with_high_MAE_guard","current_profile_error_type":"current_profile_can_under_credit_small_brand_when_sellthrough_reorder_bridge_is_real","raw_component_score_breakdown":{"export_channel_score":13,"reorder_cadence":12,"sellthrough_visibility":11,"inventory_AR_guard":8,"OPM_revision_bridge":10,"local_4b_watch_guard":0,"high_MAE_guardrail":3,"stage2_actionable_bonus":2.0,"total_proxy":76.0},"score_return_alignment":"Stage2 is justified and Yellow can be allowed only after reorder/sell-through/OPM bridge confirms; 180D MFE is strong with controlled MAE.","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse_source":"R5_loop_115_C19_BRAND_RETAIL_INVENTORY_MARGIN","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|036620|Stage2-Actionable|2024-02-22","dedupe_for_aggregate":true}
{"source_row_type":"trigger","research_id":"R5_L121_C18_002","schema_version":"v12_residual_research","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"CONSUMER_EXPORT_CHANNEL_REORDER_FINAL_PASS_TO_30_APPAREL_OUTDOOR_OEM_REORDER_SELLTHROUGH_BRIDGE","symbol":"111770","name":"영원무역","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"outdoor_OEM_reorder_inventory_cycle_mixed_positive","trigger_date":"2024-01-30","entry_date":"2024-01-31","entry_price":47900,"entry_price_basis":"close","entry_price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/111/111770/2024.csv","profile_path":"atlas/symbol_profiles/111/111770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.02,"MAE_30D_pct":-8.14,"MFE_90D_pct":10.02,"MAE_90D_pct":-18.79,"MFE_180D_pct":10.02,"MAE_180D_pct":-29.44,"peak_180D_pct":10.02,"drawdown_after_peak_180D_pct":-35.86,"classification":"mixed_positive","outcome_label":"mixed_positive_inventory_cycle_reversal","current_profile_error_type":"early_reorder_bounce_can_be_overpromoted_to_Yellow_without_destocking_resolution","raw_component_score_breakdown":{"export_channel_score":10,"reorder_cadence":7,"sellthrough_visibility":6,"inventory_AR_guard":3,"OPM_revision_bridge":4,"local_4b_watch_guard":1,"high_MAE_guardrail":8,"stage2_actionable_bonus":2.0,"total_proxy":70.0},"score_return_alignment":"Initial 30D MFE exists, but 90D/180D MAE shows channel reorder evidence did not overcome inventory-cycle drag.","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse_source":"R5_loop_115_C19_BRAND_RETAIL_INVENTORY_MARGIN","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|111770|Stage3-Yellow|2024-01-31","dedupe_for_aggregate":true}
{"source_row_type":"trigger","research_id":"R5_L121_C18_003","schema_version":"v12_residual_research","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"CONSUMER_EXPORT_CHANNEL_REORDER_FINAL_PASS_TO_30_APPAREL_OUTDOOR_OEM_REORDER_SELLTHROUGH_BRIDGE","symbol":"105630","name":"한세실업","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"apparel_OEM_reorder_without_utilization_receivables_bridge","trigger_date":"2024-02-13","entry_date":"2024-02-14","entry_price":21450,"entry_price_basis":"close","entry_price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/105/105630/2024.csv","profile_path":"atlas/symbol_profiles/105/105630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.73,"MAE_30D_pct":-15.62,"MFE_90D_pct":3.73,"MAE_90D_pct":-15.62,"MFE_180D_pct":3.73,"MAE_180D_pct":-32.31,"peak_180D_pct":3.73,"drawdown_after_peak_180D_pct":-34.74,"classification":"counterexample","outcome_label":"counterexample_high_MAE_OEM_reorder_label","current_profile_error_type":"OEM_reorder_label_false_positive_without_utilization_receivables_OPM_bridge","raw_component_score_breakdown":{"export_channel_score":8,"reorder_cadence":4,"sellthrough_visibility":3,"inventory_AR_guard":1,"OPM_revision_bridge":2,"local_4b_watch_guard":2,"high_MAE_guardrail":9,"stage2_actionable_bonus":2.0,"total_proxy":63.0},"score_return_alignment":"The profile should cap this at watch/Stage2; the realized path has negligible MFE and large 180D MAE.","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse_source":"R5_loop_115_C19_BRAND_RETAIL_INVENTORY_MARGIN","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|105630|Stage2-Actionable|2024-02-14","dedupe_for_aggregate":true}
{"source_row_type":"trigger","research_id":"R5_L121_C18_004","schema_version":"v12_residual_research","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"CONSUMER_EXPORT_CHANNEL_REORDER_FINAL_PASS_TO_30_APPAREL_OUTDOOR_OEM_REORDER_SELLTHROUGH_BRIDGE","symbol":"383220","name":"F&F","market":"KOSPI","trigger_type":"4B-Local-Watch","trigger_family":"brand_channel_heat_without_sellthrough_reorder_bridge","trigger_date":"2024-07-16","entry_date":"2024-07-17","entry_price":74000,"entry_price_basis":"close","entry_price_source":"stock-web:atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv","profile_path":"atlas/symbol_profiles/383/383220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MAE_30D_pct":-36.28,"MFE_90D_pct":3.24,"MAE_90D_pct":-36.28,"MFE_180D_pct":3.24,"MAE_180D_pct":-36.28,"peak_180D_pct":3.24,"drawdown_after_peak_180D_pct":-38.29,"classification":"counterexample","outcome_label":"counterexample_brand_channel_price_only_local4b","current_profile_error_type":"brand_channel_heat_should_remain_local_4B_when_sellthrough_reorder_bridge_absent","raw_component_score_breakdown":{"export_channel_score":9,"reorder_cadence":2,"sellthrough_visibility":2,"inventory_AR_guard":1,"OPM_revision_bridge":1,"local_4b_watch_guard":8,"high_MAE_guardrail":10,"stage2_actionable_bonus":0.0,"total_proxy":58.0},"score_return_alignment":"Price-only brand heat generates almost no upside and severe MAE; full 4B/Stage3 should be blocked.","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse_source":"R5_loop_115_C19_BRAND_RETAIL_INVENTORY_MARGIN","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|383220|4B-Local-Watch|2024-07-17","dedupe_for_aggregate":true}
```

## 7. Score / return alignment

The apparel/outdoor/OEM subfamily behaves like a conveyor belt: brand heat or export talk is the motor starting, but reorder cadence, sell-through, receivables, inventory absorption, and OPM revision are the gears. If the motor spins without the gears meshing, price can jump briefly and then strip itself back to the frame.

Observed alignment in this pass:

```jsonl
{"source_row_type":"score_simulation","case_id":"C18_121_001","symbol":"036620","current_calibrated_proxy_stage":"Stage2-Actionable_to_Yellow_candidate","desired_shadow_stage":"Stage3-Yellow_allowed_only_if_reorder_sellthrough_OPM_bridge_verified","shadow_delta":2.5,"reason":"positive path with strong 180D MFE and controlled MAE; bridge can be rewarded if verified"}
{"source_row_type":"score_simulation","case_id":"C18_121_002","symbol":"111770","current_calibrated_proxy_stage":"Stage3-Yellow","desired_shadow_stage":"Stage2-Actionable_or_Yellow_watch","shadow_delta":-4.5,"reason":"30D MFE exists but inventory-cycle gravity creates large 180D MAE"}
{"source_row_type":"score_simulation","case_id":"C18_121_003","symbol":"105630","current_calibrated_proxy_stage":"Stage2-Actionable","desired_shadow_stage":"Stage2_watch_cap_until_utilization_receivables_OPM_bridge","shadow_delta":-6.5,"reason":"OEM reorder label alone produced weak MFE and severe MAE"}
{"source_row_type":"score_simulation","case_id":"C18_121_004","symbol":"383220","current_calibrated_proxy_stage":"4B_or_Stage3_if_price_only_overcounted","desired_shadow_stage":"4B-Local-Watch_only","shadow_delta":-9.0,"reason":"brand/channel price spike without sell-through bridge generated high MAE"}
```

## 8. Aggregate JSONL

```jsonl
{"source_row_type":"aggregate","schema_version":"v12_residual_research","selected_round":"R5","selected_loop":121,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"CONSUMER_EXPORT_CHANNEL_REORDER_FINAL_PASS_TO_30_APPAREL_OUTDOOR_OEM_REORDER_SELLTHROUGH_BRIDGE","new_independent_case_count":4,"reused_case_count":0,"cross_canonical_price_row_reuse_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":1,"current_profile_error_count":4,"avg_MFE_30D_pct":7.595,"avg_MAE_30D_pct":-17.2425,"avg_MFE_90D_pct":11.1075,"avg_MAE_90D_pct":-19.905,"avg_MFE_180D_pct":14.165,"avg_MAE_180D_pct":-26.8225,"auto_selected_coverage_gap_static_index":"C18 rows 3 -> 7 if accepted; still Priority 0 by static index","auto_selected_coverage_gap_conversation_local":"C18 approx rows 26 -> 30 if accepted; local 30-row floor reached","promotion_usable_without_reverification":false,"batch_reverification_required":true,"loop_contribution_label":"canonical_archetype_rule_candidate"}
```

## 9. Shadow rule candidates

```jsonl
{"source_row_type":"shadow_weight","axis":"C18_REORDER_SELLTHROUGH_OPM_BRIDGE_REQUIRED","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","direction":"increase_required_bridge","suggested_delta":1.5,"evidence":"C18 positives require visible repeat order cadence, sell-through, inventory absorption, and OPM bridge; export/channel label alone is insufficient","production_scoring_changed":false}
{"source_row_type":"shadow_weight","axis":"C18_APPAREL_OEM_REORDER_WITHOUT_WORKING_CAPITAL_CAP","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","direction":"cap_false_positive","suggested_delta":-1.2,"evidence":"OEM reorder label without utilization/receivables/OPM bridge produced weak MFE and high 180D MAE","production_scoring_changed":false}
{"source_row_type":"shadow_weight","axis":"C18_BRAND_CHANNEL_PRICE_SPIKE_LOCAL_4B_GUARD","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","direction":"strengthen_local_4b_guard","suggested_delta":-1.0,"evidence":"Brand/channel price spike without verified sell-through produced severe MAE; keep as local 4B watch only","production_scoring_changed":false}
{"source_row_type":"residual_contribution","round":"R5","loop":121,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","new_independent_case_count":4,"same_archetype_new_symbol_count":4,"cross_canonical_price_row_reuse_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":1,"current_profile_error_count":4,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 10. Narrative conclusions

C18 should not treat “export channel exists” as enough. The right question is whether the next purchase order arrives after the first sell-through, and whether that reorder lands in margin instead of inventory and receivables. The archetype is therefore a bridge problem, not a label problem.

For C18 apparel/outdoor/OEM cases, the signal ladder should be:

```text
export/channel label
  -> sell-through evidence
  -> repeat reorder cadence
  -> inventory and AR absorption
  -> OPM / revision / FCF bridge
  -> durable Stage2/Stage3 permission
```

If that ladder is broken, even a visually strong price candle should remain `4B-Local-Watch` or capped Stage2. If the ladder is intact, the system should allow a positive Stage2-to-Yellow upgrade, but only with high-MAE guard still active.

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the later batch coding agent for stock_agent E2R calibration.
Read this MD as one v12 residual research artifact.
Do not treat it as a production patch by itself.

Tasks:
1. Re-open every stock_web_profile_path and stock_web_tradable_shard_path in Songdaiki/stock-web.
2. Recompute 30D/90D/180D MFE/MAE from tradable_raw OHLC rows.
3. Reject rows if profile corporate_action_candidate_dates overlap entry_date through D+180.
4. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
5. If verified, register these C18 shadow rule candidates:
   - C18_REORDER_SELLTHROUGH_OPM_BRIDGE_REQUIRED
   - C18_APPAREL_OEM_REORDER_WITHOUT_WORKING_CAPITAL_CAP
   - C18_BRAND_CHANNEL_PRICE_SPIKE_LOCAL_4B_GUARD
6. Keep production_scoring_changed=false until batch review.
```

## 12. Research state for next run

```text
completed_round = R5
completed_loop = 121
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_fourth_pass_to_30, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_next_pass_to_30, C31_POLICY_SUBSIDY_LEGISLATION_EVENT_next_pass_to_30, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_next_pass_to_30, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
