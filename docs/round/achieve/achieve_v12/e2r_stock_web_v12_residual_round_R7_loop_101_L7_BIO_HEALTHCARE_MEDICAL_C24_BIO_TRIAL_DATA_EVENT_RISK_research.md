# E2R Stock-Web v12 Residual Research — R7 / L7 / C24

```text
output_file = e2r_stock_web_v12_residual_round_R7_loop_101_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
selected_round = R7
selected_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Coverage-index selection

`V12_Research_No_Repeat_Index.md` 기준 C24_BIO_TRIAL_DATA_EVENT_RISK는 13 rows / 8 symbols / positives-counterexamples 1-2 / 4B-4C 1-2로 아직 Priority 0이다. 기존 반복 위험은 028300 중심으로 높고, top covered symbols는 028300, 141080, 298380, 039200, 115180, 215600이다.

이번 loop는 기존 반복 위험이 높은 028300을 피하고, C24 안에서 새 symbol과 새 trigger family를 늘린다.

```text
selected_archetype = C24_BIO_TRIAL_DATA_EVENT_RISK
selected_round = R7
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 1
local_4b_watch_count = 1
current_profile_error_count = 4
```

## 2. Source validation

Stock-web manifest basis:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Selected symbol profiles checked:

| symbol | name | profile | corporate-action window used for D+180 |
|---|---|---|---|
| 196170 | 알테오젠 | atlas/symbol_profiles/196/196170.json | not contaminated; corporate action candidates are historical 2017/2020/2021 only |
| 950160 | 코오롱티슈진 | atlas/symbol_profiles/950/950160.json | not contaminated; candidate 2022-10-25 outside selected window |
| 069620 | 대웅제약 | atlas/symbol_profiles/069/069620.json | not contaminated; no corporate action candidates |
| 128940 | 한미약품 | atlas/symbol_profiles/128/128940.json | not contaminated; no corporate action candidates |

All selected trigger rows use tradable shards and include complete 30D/90D/180D MFE/MAE.

## 3. Case table

| case_id | symbol | trigger_type | role | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---:|---|---|---:|---:|---:|---:|---|
| C24_CASE_001_196170_ALTEOGEN_SC_PLATFORM_DATA_DE_RISKING | 196170 | Stage2-Actionable | structural_success | 2024-02-21 / 93,900 | +140.15 / -10.12 | +209.90 / -10.12 | +287.11 / -10.12 | true de-risking when trial/platform data quality and license-option economics are visible |
| C24_CASE_002_950160_KOLON_TISSUEGEN_TRIAL_RESTART_EVENT_CAP | 950160 | Stage4B | local_4b_watch | 2024-01-11 / 11,690 | +13.34 / -26.35 | +37.13 / -26.35 | +86.48 / -26.35 | huge MFE but early high MAE; price spike alone should not become positive Stage |
| C24_CASE_003_069620_DAEWOONG_PHARMA_PIPELINE_OPTION_MIXED_FOLLOWTHROUGH | 069620 | Stage2 | mixed_positive | 2024-03-19 / 123,600 | +3.24 / -13.67 | +3.24 / -19.01 | +21.36 / -19.01 | delayed option value; watchlist valid, immediate Green not justified |
| C24_CASE_004_128940_HANMI_PIPELINE_LABEL_FALSE_POSITIVE | 128940 | Stage2 | failed_rerating | 2024-03-25 / 347,000 | +0.86 / -14.70 | +0.86 / -25.65 | +8.07 / -29.83 | named pipeline label without fresh value unlock became opportunity-cost / MAE trap |

## 4. Current calibrated profile stress test

The current calibrated profile already has high information-confidence weight for C24. That is directionally right, but this loop adds a split that the global profile cannot fully express:

```text
C24 is not simply "more information confidence is better".
It needs event quality, endpoint quality, source credibility, partner/license economics, and post-event price/volume follow-through.
```

Residual errors:

1. **Under-classification risk:** 196170-like data/license de-risking can look like ordinary binary biotech risk if event quality is not separated from event vocabulary.
2. **Over-classification risk:** 950160-like and 128940-like cases can look strong from price-MFE or brand/pipeline labels, but MAE and lack of fresh economic bridge make them unsuitable for positive-stage promotion.
3. **Timing risk:** 069620-like cases can show delayed payoff after long adverse drift; this argues for Stage2 watch, not immediate rejection or Green.
4. **4B proximity risk:** Large local MFE in C24 often comes from event volatility. Full 4B should still require non-price confirmation.

## 5. Proposed shadow rule

```text
new_axis_proposed =
  C24_binary_event_quality_followthrough_bridge_required
  C24_price_MFE_event_cap_4B_guard
```

Rule sketch:

```text
IF canonical_archetype_id == C24_BIO_TRIAL_DATA_EVENT_RISK
AND trigger_type in Stage2 | Stage2-Actionable
THEN require at least two of:
  - fresh trial endpoint/data quality improvement
  - partner/license/economic bridge
  - commercialization or royalty path
  - post-event follow-through with controlled MAE
  - non-price evidence after the event

IF only price spike / theme vocabulary / pipeline label exists
THEN cap at Stage2 watch or local 4B watch.
```

Expected effect:

```text
- preserve 196170-like upside capture
- avoid 128940-like label-only false positive
- keep 950160-like event-cap MFE as 4B/watch rather than full positive
- classify 069620-like delayed event path as mixed Stage2, not Green
```

## 6. Machine-readable rows

### 6.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap","price_data_source":"Songdaiki/stock-web","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","profile_paths":["atlas/symbol_profiles/196/196170.json","atlas/symbol_profiles/950/950160.json","atlas/symbol_profiles/069/069620.json","atlas/symbol_profiles/128/128940.json"],"corporate_action_window_status":"all_selected_entry_to_D180_not_contaminated"}
```

### 6.2 case rows

```jsonl
{"row_type":"case","case_id":"C24_CASE_001_196170_ALTEOGEN_SC_PLATFORM_DATA_DE_RISKING","symbol":"196170","name":"알테오젠","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE","case_role":"structural_success","trigger_family":"SC_PLATFORM_BIOLOGIC_DELIVERY_DATA_LICENSE_OPTION_REPRICING","outcome":"positive","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C24_CASE_002_950160_KOLON_TISSUEGEN_TRIAL_RESTART_EVENT_CAP","symbol":"950160","name":"코오롱티슈진","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE","case_role":"local_4b_watch","trigger_family":"TRIAL_RESTART_REGULATORY_OVERHANG_EVENT_CAP_VOLATILITY","outcome":"mixed","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C24_CASE_003_069620_DAEWOONG_PHARMA_PIPELINE_OPTION_MIXED_FOLLOWTHROUGH","symbol":"069620","name":"대웅제약","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE","case_role":"mixed_positive","trigger_family":"PHARMA_PIPELINE_DATA_OPTION_WITH_WEAK_EARLY_PRICE_CONFIRMATION","outcome":"mixed","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C24_CASE_004_128940_HANMI_PIPELINE_LABEL_FALSE_POSITIVE","symbol":"128940","name":"한미약품","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE","case_role":"failed_rerating","trigger_family":"OBESITY_PIPELINE_DATA_LABEL_WITHOUT_FRESH_VALUE_UNLOCK","outcome":"counterexample","source_proxy_only":true,"evidence_url_pending":true,"calibration_usable":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 6.3 trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R7","selected_loop":101,"case_id":"C24_CASE_001_196170_ALTEOGEN_SC_PLATFORM_DATA_DE_RISKING","symbol":"196170","name":"알테오젠","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE","trigger_type":"Stage2-Actionable","trigger_family":"SC_PLATFORM_BIOLOGIC_DELIVERY_DATA_LICENSE_OPTION_REPRICING","entry_date":"2024-02-21","entry_price":93900.0,"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_shard":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","forward_window_trading_days":180,"MFE_30D_pct":140.15,"MAE_30D_pct":-10.12,"MFE_90D_pct":209.9,"MAE_90D_pct":-10.12,"MFE_180D_pct":287.11,"MAE_180D_pct":-10.12,"peak_price_30D":225500,"trough_price_30D":84400,"peak_price_90D":291000,"trough_price_90D":84400,"peak_price_180D":363500,"trough_price_180D":84400,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C24_CASE_001_196170_ALTEOGEN_SC_PLATFORM_DATA_DE_RISKING_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url_pending":true,"source_proxy_only":true,"current_profile_error":true,"profile_error":"current profile can still under-rank cross-period data/license de-risking if it treats all trial headlines as binary risk rather than differentiated option value","case_role":"structural_success"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R7","selected_loop":101,"case_id":"C24_CASE_002_950160_KOLON_TISSUEGEN_TRIAL_RESTART_EVENT_CAP","symbol":"950160","name":"코오롱티슈진","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE","trigger_type":"Stage4B","trigger_family":"TRIAL_RESTART_REGULATORY_OVERHANG_EVENT_CAP_VOLATILITY","entry_date":"2024-01-11","entry_price":11690.0,"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_shard":"atlas/ohlcv_tradable_by_symbol_year/950/950160/2024.csv","profile_path":"atlas/symbol_profiles/950/950160.json","forward_window_trading_days":180,"MFE_30D_pct":13.34,"MAE_30D_pct":-26.35,"MFE_90D_pct":37.13,"MAE_90D_pct":-26.35,"MFE_180D_pct":86.48,"MAE_180D_pct":-26.35,"peak_price_30D":13250,"trough_price_30D":8610,"peak_price_90D":16030,"trough_price_90D":8610,"peak_price_180D":21800,"trough_price_180D":8610,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C24_CASE_002_950160_KOLON_TISSUEGEN_TRIAL_RESTART_EVENT_CAP_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url_pending":true,"source_proxy_only":true,"current_profile_error":true,"profile_error":"price-only MFE would make this look strong; C24 needs event-cap guard because early MAE was large before later spike","case_role":"local_4b_watch"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R7","selected_loop":101,"case_id":"C24_CASE_003_069620_DAEWOONG_PHARMA_PIPELINE_OPTION_MIXED_FOLLOWTHROUGH","symbol":"069620","name":"대웅제약","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE","trigger_type":"Stage2","trigger_family":"PHARMA_PIPELINE_DATA_OPTION_WITH_WEAK_EARLY_PRICE_CONFIRMATION","entry_date":"2024-03-19","entry_price":123600.0,"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_shard":"atlas/ohlcv_tradable_by_symbol_year/069/069620/2024.csv","profile_path":"atlas/symbol_profiles/069/069620.json","forward_window_trading_days":180,"MFE_30D_pct":3.24,"MAE_30D_pct":-13.67,"MFE_90D_pct":3.24,"MAE_90D_pct":-19.01,"MFE_180D_pct":21.36,"MAE_180D_pct":-19.01,"peak_price_30D":127600,"trough_price_30D":106700,"peak_price_90D":127600,"trough_price_90D":100100,"peak_price_180D":150000,"trough_price_180D":100100,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C24_CASE_003_069620_DAEWOONG_PHARMA_PIPELINE_OPTION_MIXED_FOLLOWTHROUGH_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url_pending":true,"source_proxy_only":true,"current_profile_error":true,"profile_error":"a strict early price-only filter would discard later MFE, while a loose event filter would ignore long drawdown","case_role":"mixed_positive"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R7","selected_loop":101,"case_id":"C24_CASE_004_128940_HANMI_PIPELINE_LABEL_FALSE_POSITIVE","symbol":"128940","name":"한미약품","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BINARY_TRIAL_DATA_LICENSE_OPTION_EVENT_RISK_VS_PIPELINE_LABEL_FALSE_POSITIVE","trigger_type":"Stage2","trigger_family":"OBESITY_PIPELINE_DATA_LABEL_WITHOUT_FRESH_VALUE_UNLOCK","entry_date":"2024-03-25","entry_price":347000.0,"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_shard":"atlas/ohlcv_tradable_by_symbol_year/128/128940/2024.csv","profile_path":"atlas/symbol_profiles/128/128940.json","forward_window_trading_days":180,"MFE_30D_pct":0.86,"MAE_30D_pct":-14.7,"MFE_90D_pct":0.86,"MAE_90D_pct":-25.65,"MFE_180D_pct":8.07,"MAE_180D_pct":-29.83,"peak_price_30D":350000,"trough_price_30D":296000,"peak_price_90D":350000,"trough_price_90D":258000,"peak_price_180D":375000,"trough_price_180D":243500,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C24_CASE_004_128940_HANMI_PIPELINE_LABEL_FALSE_POSITIVE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","evidence_url_pending":true,"source_proxy_only":true,"current_profile_error":true,"profile_error":"brand-name pipeline vocabulary can overstate information confidence when new binary data is absent","case_role":"failed_rerating"}
```

### 6.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C24_CASE_001_196170_ALTEOGEN_SC_PLATFORM_DATA_DE_RISKING","symbol":"196170","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS_FCF_Explosion":8,"Earnings_Visibility_and_Quality":19,"Bottleneck_and_Pricing_Power":4,"Market_Mispricing":12,"Valuation_Rerating_Runway":5,"Capital_Allocation":5,"Information_Confidence":34},"simulated_total_score":78.0,"current_profile_error":true,"score_return_alignment":"pass"}
{"row_type":"score_simulation","case_id":"C24_CASE_002_950160_KOLON_TISSUEGEN_TRIAL_RESTART_EVENT_CAP","symbol":"950160","trigger_type":"Stage4B","raw_component_score_breakdown":{"EPS_FCF_Explosion":5,"Earnings_Visibility_and_Quality":14,"Bottleneck_and_Pricing_Power":4,"Market_Mispricing":10,"Valuation_Rerating_Runway":5,"Capital_Allocation":5,"Information_Confidence":25},"simulated_total_score":66.0,"current_profile_error":true,"score_return_alignment":"mixed"}
{"row_type":"score_simulation","case_id":"C24_CASE_003_069620_DAEWOONG_PHARMA_PIPELINE_OPTION_MIXED_FOLLOWTHROUGH","symbol":"069620","trigger_type":"Stage2","raw_component_score_breakdown":{"EPS_FCF_Explosion":8,"Earnings_Visibility_and_Quality":14,"Bottleneck_and_Pricing_Power":4,"Market_Mispricing":10,"Valuation_Rerating_Runway":5,"Capital_Allocation":5,"Information_Confidence":24},"simulated_total_score":70.0,"current_profile_error":true,"score_return_alignment":"mixed"}
{"row_type":"score_simulation","case_id":"C24_CASE_004_128940_HANMI_PIPELINE_LABEL_FALSE_POSITIVE","symbol":"128940","trigger_type":"Stage2","raw_component_score_breakdown":{"EPS_FCF_Explosion":5,"Earnings_Visibility_and_Quality":14,"Bottleneck_and_Pricing_Power":4,"Market_Mispricing":10,"Valuation_Rerating_Runway":5,"Capital_Allocation":5,"Information_Confidence":24},"simulated_total_score":61.0,"current_profile_error":true,"score_return_alignment":"fail"}
```

### 6.5 aggregate_metric rows

```jsonl
{"row_type":"aggregate_metric","selected_round":"R7","selected_loop":101,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":2,"counterexample_count":1,"local_4b_watch_count":1,"current_profile_error_count":4,"median_MFE_180D_pct":53.92,"median_MAE_180D_pct":-22.68}
```

### 6.6 shadow_weight rows

```jsonl
{"row_type":"shadow_weight","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_axis_proposed":"C24_binary_event_quality_followthrough_bridge_required | C24_price_MFE_event_cap_4B_guard","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail","existing_axis_weakened":null,"suggested_shadow_delta":{"Information_Confidence":"+2 only when event source quality and follow-through bridge exist","Valuation_Rerating_Runway":"-2 when named-pipeline label has no fresh data/economic unlock","Market_Mispricing":"+1 for post-data de-risking reset with manageable MAE","Capital_Allocation":"0"},"do_not_apply_now":true,"production_scoring_changed":false}
```

### 6.7 residual_contribution rows

```jsonl
{"row_type":"residual_contribution","axis":"C24 event quality split","finding":"Not all clinical/pipeline headlines behave alike; data/license/economic follow-through separates 196170-like success from 128940-like label-only false positive."}
{"row_type":"residual_contribution","axis":"C24 event-cap local 4B","finding":"950160 produced large MFE but also early -26% MAE; this supports local 4B watch rather than immediate positive-stage promotion from price alone."}
```

### 6.8 narrative_only rows

```jsonl
{"row_type":"narrative_only","reason":"non_price_event_evidence_is_source_proxy_only","evidence_url_pending":true,"source_proxy_only":true,"note":"This loop uses stock-web for verified price path and keeps non-price event descriptions in low-trust narrative/proxy bucket until URL repair."}
```

## 7. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent for Songdaiki/stock_agent.

Do not treat this MD as production truth by itself. Batch it with other v12 residual MDs and run the normal calibration ingest/validation/dedupe pipeline.

Research file:
e2r_stock_web_v12_residual_round_R7_loop_101_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md

Suggested candidate:
- canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
- large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
- candidate axis:
  1. C24_binary_event_quality_followthrough_bridge_required
  2. C24_price_MFE_event_cap_4B_guard

Implementation direction:
- Do not loosen Stage3-Green.
- Do not remove full_4b_requires_non_price_evidence.
- Add or test a C24-specific bridge that separates:
  true data/license/economic de-risking
  vs.
  price-only / brand-pipeline / trial-restart event-cap spikes.
- Preserve all existing global guardrails unless batch evidence contradicts this single-loop finding.
```

## 9. Final research state

```text
completed_round = R7
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
new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 1
current_profile_error_count = 4
diversity_score_summary = Priority 0 C24 shortage fill; avoided 028300 repeat; added 196170/950160/069620/128940; one positive, two mixed, one counterexample, one local 4B event-cap guard.
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false

sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
new_axis_proposed = C24_binary_event_quality_followthrough_bridge_required | C24_price_MFE_event_cap_4B_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null

auto_selected_coverage_gap = C24 rows 13 -> 17 if accepted; still Priority 0, need 13 to 30.
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX
```

This loop adds 4 new independent cases, 1 counterexample, and 4 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.
