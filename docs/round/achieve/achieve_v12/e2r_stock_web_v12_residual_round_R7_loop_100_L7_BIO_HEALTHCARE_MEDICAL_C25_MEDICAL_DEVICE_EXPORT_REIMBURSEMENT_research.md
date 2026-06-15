# E2R Stock-Web v12 Residual Research — R7 / L7 / C25

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Execution metadata

```yaml
file_name: e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
selected_round: R7
selected_loop: 100
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_EXPORT_INSTALL_BASE_AND_DENTAL_DEVICE_REIMBURSEMENT_BRIDGE_VS_EVENT_CAP_FALSE_POSITIVE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
primary_validation_window: 2024-01-02_to_2024-12-30
```

### Selection rationale

No-Repeat Index 기준 C25는 6 representative rows / 4 symbols로 30-row 안정권에 크게 미달한다. 기존 대표 symbol은 `145720`, `214150`, `099190`, `336570`에 몰려 있으므로 이번 실행은 반복을 피하기 위해 다음 네 종목으로 신규 symbol coverage를 채운다.

```text
new_symbols:
- 214450 파마리서치
- 335890 비올
- 228670 레이
- 287410 제이시스메디칼

existing_top_symbols_avoided:
- 145720
- 214150
- 099190
- 336570
```

C25의 핵심 질문은 “의료기기/미용기기/치과기기 label이 실제 수출·설치대수·소모품·reimbursement·마진 revision으로 연결되는가”다. 가격만 오른 경우는 Stage2/Green이 아니라 local 4B 또는 false-positive로 묶어야 한다.

---

## 2. Stock-Web source validation

```yaml
manifest_path: atlas/manifest.json
manifest_max_date: 2026-02-20
source_name: FinanceData/marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
calibration_caveat: raw_unadjusted_marcap; corporate-action-contaminated windows blocked by default
```

### Symbol profile checks

```jsonl
{"symbol":"214450","name":"파마리서치","source_profile":"atlas/symbol_profiles/214/214450.json","status_inferred":"active_like","corporate_action_candidate_count":0,"calibration_caveat":"","price_data_source":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap"}
{"symbol":"335890","name":"비올","source_profile":"atlas/symbol_profiles/335/335890.json","status_inferred":"inactive_or_delisted_like","corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2020-11-26"],"calibration_window_2024_blocked_by_corporate_action":false,"price_data_source":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap"}
{"symbol":"228670","name":"레이","source_profile":"atlas/symbol_profiles/228/228670.json","status_inferred":"active_like","corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2021-06-03","2021-06-23"],"calibration_window_2024_blocked_by_corporate_action":false,"price_data_source":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap"}
{"symbol":"287410","name":"제이시스메디칼","source_profile":"atlas/symbol_profiles/287/287410.json","status_inferred":"inactive_or_delisted_like","last_tradable_date_observed":"2024-10-18","corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2020-12-24","2021-03-31"],"calibration_window_2024_blocked_by_corporate_action":false,"price_data_source":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap"}
```

주의: `335890`, `287410`은 profile상 inactive/delisted-like로 추론된다. 단, 2024년 본 calibration window 자체는 corporate-action candidate date와 겹치지 않는다. `287410`은 2024-10-18까지 tradable rows가 있으므로 2024-01-22 entry는 180D forward window에 필요한 관측 가능성을 확보한다. 이후 tender/event cap 성격이 강하므로 positive 승격 근거가 아니라 local 4B/event-cap guardrail로 분류한다.

---

## 3. Case thesis compression

### Fine/deep route

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  -> aesthetic_device_export_install_base_margin_revision_bridge
  -> consumable_or_repeat_procurement_visibility
  -> reimbursement_or_channel_quality_check
  -> false_positive_guard:
       price_only_device_label
       dental_equipment_export_label_without_order_margin_followthrough
       tender_event_cap_without_new operating evidence
```

### C25 residual rule candidate

```text
C25_positive_stage_requires:
- device/procedure installed-base expansion OR export shipment acceleration
- repeat consumable/procedure revenue visibility
- margin or revision bridge
- reimbursement/channel quality where applicable
- no price-only/tender-only blowoff

C25_local_4b_watch_if:
- price MFE is large but evidence is tender/event/cap or sector beta only
- installed-base or export bridge is not refreshed
- 90D/180D MFE exists but MAE is also elevated or route becomes event capped
```

---

## 4. Trigger-level backtest rows

Every usable trigger row includes entry_date, entry_price, trigger_type, 30/90/180D MFE/MAE, path source, and dedupe key.

```jsonl
{"row_type":"trigger","version":"v12_stock_web","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALL_BASE_AND_DENTAL_DEVICE_REIMBURSEMENT_BRIDGE_VS_EVENT_CAP_FALSE_POSITIVE","symbol":"214450","name":"파마리서치","case_label":"PDRN_skinbooster_export_margin_revision_bridge_positive","trigger_type":"Stage2-Actionable","entry_date":"2024-03-25","entry_price":98700.0,"entry_basis":"close","source_path":"atlas/ohlcv_tradable_by_symbol_year/214/214450/2024.csv","forward_window_trading_days":{"30":30,"90":90,"180":180},"MFE_30D_pct":46.00,"MAE_30D_pct":-8.00,"MFE_90D_pct":70.92,"MAE_90D_pct":-8.00,"MFE_180D_pct":173.56,"MAE_180D_pct":-8.00,"peak_price_180D":270000.0,"trough_price_180D":90800.0,"path_class":"positive","current_profile_error_type":"too_conservative_without_C25_export_margin_bridge","evidence_source_type":"stock_web_price_proxy_plus_research_memory","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214450|Stage2-Actionable|2024-03-25","representative_for_aggregate":true}
{"row_type":"trigger","version":"v12_stock_web","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALL_BASE_AND_DENTAL_DEVICE_REIMBURSEMENT_BRIDGE_VS_EVENT_CAP_FALSE_POSITIVE","symbol":"335890","name":"비올","case_label":"RF_micro_needling_export_device_bridge_mixed_high_MAE","trigger_type":"Stage2","entry_date":"2024-03-13","entry_price":8480.0,"entry_basis":"close","source_path":"atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv","forward_window_trading_days":{"30":30,"90":90,"180":180},"MFE_30D_pct":41.86,"MAE_30D_pct":-13.92,"MFE_90D_pct":41.86,"MAE_90D_pct":-13.92,"MFE_180D_pct":41.86,"MAE_180D_pct":-21.82,"peak_price_180D":12030.0,"trough_price_180D":6630.0,"path_class":"mixed_positive_high_MAE","current_profile_error_type":"needs_high_MAE_guard_even_when_device_export_label_hits","evidence_source_type":"stock_web_price_proxy_plus_research_memory","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|335890|Stage2|2024-03-13","representative_for_aggregate":true}
{"row_type":"trigger","version":"v12_stock_web","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALL_BASE_AND_DENTAL_DEVICE_REIMBURSEMENT_BRIDGE_VS_EVENT_CAP_FALSE_POSITIVE","symbol":"228670","name":"레이","case_label":"dental_digital_export_label_without_order_margin_followthrough_counterexample","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-02","entry_price":23450.0,"entry_basis":"close","source_path":"atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv","forward_window_trading_days":{"30":30,"90":90,"180":180},"MFE_30D_pct":7.04,"MAE_30D_pct":-20.90,"MFE_90D_pct":7.04,"MAE_90D_pct":-37.06,"MFE_180D_pct":7.04,"MAE_180D_pct":-67.59,"peak_price_180D":25100.0,"trough_price_180D":7600.0,"path_class":"counterexample","current_profile_error_type":"price_and_device_vocabulary_would_overadmit_without_order_margin_bridge","evidence_source_type":"stock_web_price_proxy_plus_research_memory","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|228670|Stage2-FalsePositive|2024-01-02","representative_for_aggregate":true}
{"row_type":"trigger","version":"v12_stock_web","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALL_BASE_AND_DENTAL_DEVICE_REIMBURSEMENT_BRIDGE_VS_EVENT_CAP_FALSE_POSITIVE","symbol":"287410","name":"제이시스메디칼","case_label":"aesthetic_device_tender_event_cap_local_4b_not_operating_green","trigger_type":"Stage4B","entry_date":"2024-01-22","entry_price":9000.0,"entry_basis":"close","source_path":"atlas/ohlcv_tradable_by_symbol_year/287/287410/2024.csv","forward_window_trading_days":{"30":30,"90":90,"180":180},"MFE_30D_pct":2.22,"MAE_30D_pct":-17.44,"MFE_90D_pct":43.89,"MAE_90D_pct":-17.89,"MFE_180D_pct":43.89,"MAE_180D_pct":-17.89,"peak_price_180D":12950.0,"trough_price_180D":7390.0,"path_class":"local_4b_event_cap","local_4b_watch":true,"full_4b_allowed":false,"current_profile_error_type":"needs_tender_event_cap_guard_not_positive_stage","evidence_source_type":"stock_web_price_proxy_plus_research_memory","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|287410|Stage4B|2024-01-22","representative_for_aggregate":true}
```

---

## 5. Score / return alignment

### Raw component score simulation

Component order:

```text
1 EPS/FCF Explosion
2 Earnings Visibility and Quality
3 Bottleneck and Pricing Power
4 Market Mispricing
5 Valuation Rerating Runway
6 Capital Allocation
7 Information Confidence
```

```jsonl
{"row_type":"score_simulation","symbol":"214450","trigger_type":"Stage2-Actionable","entry_date":"2024-03-25","raw_component_score":{"eps_fcf_explosion":18,"earnings_visibility_quality":22,"bottleneck_pricing_power":13,"market_mispricing":14,"valuation_rerating_runway":13,"capital_allocation":7,"information_confidence":9},"total_score_before_guard":96,"guard_adjustment":-4,"total_score_after_guard":92,"simulated_stage":"Stage3-Yellow_to_Green_watch","actual_path_label":"positive","alignment":"positive but Green still needs non-price source repair"}
{"row_type":"score_simulation","symbol":"335890","trigger_type":"Stage2","entry_date":"2024-03-13","raw_component_score":{"eps_fcf_explosion":16,"earnings_visibility_quality":18,"bottleneck_pricing_power":15,"market_mispricing":13,"valuation_rerating_runway":12,"capital_allocation":5,"information_confidence":7},"total_score_before_guard":86,"guard_adjustment":-8,"total_score_after_guard":78,"simulated_stage":"Stage3-Yellow_watch","actual_path_label":"mixed_high_MAE","alignment":"needs high-MAE guard and source repair"}
{"row_type":"score_simulation","symbol":"228670","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-02","raw_component_score":{"eps_fcf_explosion":8,"earnings_visibility_quality":11,"bottleneck_pricing_power":8,"market_mispricing":10,"valuation_rerating_runway":8,"capital_allocation":4,"information_confidence":6},"total_score_before_guard":55,"guard_adjustment":-6,"total_score_after_guard":49,"simulated_stage":"Stage1_or_Stage2_reject","actual_path_label":"counterexample","alignment":"device vocabulary without order/margin bridge should not enter Stage2"}
{"row_type":"score_simulation","symbol":"287410","trigger_type":"Stage4B","entry_date":"2024-01-22","raw_component_score":{"eps_fcf_explosion":10,"earnings_visibility_quality":11,"bottleneck_pricing_power":12,"market_mispricing":18,"valuation_rerating_runway":16,"capital_allocation":5,"information_confidence":4},"total_score_before_guard":76,"guard_adjustment":-12,"total_score_after_guard":64,"simulated_stage":"Stage4B_local_watch_not_positive","actual_path_label":"local_4b_event_cap","alignment":"MFE arrived through event cap, not operating bridge"}
```

---

## 6. Aggregate contribution

```jsonl
{"row_type":"aggregate","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","selected_round":"R7","selected_loop":100,"new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":1,"local_4b_watch_count":1,"current_profile_error_count":4,"avg_MFE_90D_pct":40.92,"avg_MAE_90D_pct":-19.71,"avg_MFE_180D_pct":66.59,"avg_MAE_180D_pct":-28.83,"stage2_hit_rate_MFE90_ge_20pct":0.75,"stage2_bad_entry_rate_MAE90_le_minus20pct":0.25,"diversity_score_summary":"Priority 0 C25 shortage fill; 4 new symbols; 4 trigger families; 1 clean positive, 1 mixed high-MAE positive, 1 dental counterexample, 1 tender/event-cap local 4B"}
```

Interpretation:

```text
C25는 clean positive가 없지는 않다. 214450처럼 export/procedure revenue/margin revision bridge가 붙으면 Stage2-Actionable 이후 큰 MFE가 열린다.
하지만 335890처럼 MFE가 먼저 나와도 180D MAE가 -20%를 넘는 경우가 있고, 228670처럼 device/dental export label만으로는 long-window drawdown이 훨씬 크다.
287410은 MFE가 event/tender cap으로 실현된 local 4B이지, operating Green으로 승격할 근거가 아니다.
```

---

## 7. Shadow rule proposal

```jsonl
{"row_type":"shadow_weight","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","proposal_id":"C25_export_install_base_margin_revision_bridge_required_v1","safe_patch_axis":"stage2_required_bridge","direction":"strengthen","rule":"C25 Stage2-Actionable requires at least one non-price bridge among export shipment acceleration, installed-base/procedure count growth, consumable/repeat revenue visibility, reimbursement/channel quality, or margin/revision confirmation.","expected_effect":"admit 214450-like clean positives while rejecting 228670-like device-vocabulary false positives","do_not_propose_new_weight_delta":false}
{"row_type":"shadow_weight","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","proposal_id":"C25_high_MAE_device_beta_guard_v1","safe_patch_axis":"local_4b_watch_guard","direction":"strengthen","rule":"If MFE90 >= 20 but MAE180 <= -20 and evidence remains source_proxy_only or price-only, keep as Stage3-Yellow/4B-watch rather than Green.","expected_effect":"keeps 335890-like mixed routes out of unconditional positive promotion","do_not_propose_new_weight_delta":false}
{"row_type":"shadow_weight","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","proposal_id":"C25_tender_event_cap_guard_v1","safe_patch_axis":"full_4b_requires_non_price_evidence","direction":"strengthen","rule":"Tender, delisting, ownership, or capped event-price behavior may validate local 4B MFE but cannot be counted as operating Stage2/Green without new operating evidence.","expected_effect":"classifies 287410-like paths as local_4B_event_cap rather than positive operating bridge","do_not_propose_new_weight_delta":false}
```

---

## 8. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","selected_round":"R7","selected_loop":100,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_axis_proposed":"C25_export_install_base_margin_revision_bridge_required","existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","local_4b_watch_guard","full_4b_requires_non_price_evidence","high_MAE_guardrail"],"existing_axis_weakened":[],"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate","coverage_gap_before_rows":6,"coverage_gap_after_rows_if_accepted":10,"target_min_rows":30,"remaining_to_30_rows":20}
```

---

## 9. Narrative-only notes

```jsonl
{"row_type":"narrative_only","topic":"214450 positive route","summary":"Clean C25 positive requires a bridge from procedure/device demand into margin and revision. The path produced high 30D/90D/180D MFE with controlled drawdown, so it is useful as positive training material after source URL repair."}
{"row_type":"narrative_only","topic":"335890 mixed route","summary":"Aesthetic device export label can produce fast MFE, but the 180D MAE crossed -20%. C25 should not treat early MFE as sufficient unless installed-base/consumable/revision bridge remains fresh."}
{"row_type":"narrative_only","topic":"228670 false positive route","summary":"Dental device/export vocabulary without order margin follow-through had poor long-window alignment. This is a clean counterexample for price-only or label-only Stage2 admission."}
{"row_type":"narrative_only","topic":"287410 local 4B route","summary":"Tender or ownership-event cap can create MFE after earlier drawdown, but this is not the same as operating medical-device rerating. It belongs in local 4B watch, not operating Green."}
```

---

## 10. Validation checklist

```yaml
must_use_actual_stock_web_1D_OHLC: pass
must_include_backtest_result: pass
must_include_score_return_alignment: pass
must_include_current_calibrated_profile_stress_test: pass
must_include_positive_and_counterexample_balance: pass
must_include_large_sector_id: pass
must_include_canonical_archetype_id: pass
must_include_novelty_check: pass
must_include_residual_contribution_summary: pass
must_output_every_usable_trigger_as_jsonl: pass
must_deduplicate_same_entry_triggers_for_aggregate: pass
must_split_4b_local_vs_full_window_proximity: pass
must_include_raw_component_score_breakdown: pass
must_include_validation_scope: pass
must_use_standard_v12_result_filename: pass
must_never_use_compact_filename: pass
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row: pass
trigger_rows_missing_required_price_fields_are_forbidden: pass
stock_agent_code_patch_written: false
handoff_prompt_executed_now: false
```

---

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this section in the research session. It is for a later batch implementation session.

```text
You are the coding agent for Songdaiki/stock_agent.

Input artifact:
reports/e2r_calibration/v12/e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md

Task:
1. Parse all JSONL rows in sections 4~8.
2. Validate that each trigger has entry_date, entry_price, trigger_type, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
3. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add representative rows only if no duplicate exists.
5. Treat source_proxy_only/evidence_url_pending rows as research-valid but promotion-limited until source URL repair.
6. Consider safe patch candidates:
   - C25_export_install_base_margin_revision_bridge_required_v1
   - C25_high_MAE_device_beta_guard_v1
   - C25_tender_event_cap_guard_v1
7. Do not loosen Stage3-Green thresholds.
8. Do not convert tender/event cap MFE into operating positive evidence.
9. Keep all changes shadow/rolling-calibration only unless batch promotion gate passes.
```

---

## 12. Completion state

```yaml
completed_round: R7
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_EXPORT_INSTALL_BASE_AND_DENTAL_DEVICE_REIMBURSEMENT_BRIDGE_VS_EVENT_CAP_FALSE_POSITIVE
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_case_count: 1
mixed_positive_count: 1
counterexample_count: 1
local_4b_watch_count: 1
current_profile_error_count: 4
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C25 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C25_export_install_base_margin_revision_bridge_required
existing_axis_strengthened:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
  - high_MAE_guardrail
existing_axis_weakened: []
next_recommended_archetypes:
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```
