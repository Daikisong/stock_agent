# E2R Stock-Web v12 Residual Research — C31 Policy Subsidy / Legislation Event — Strict Row Final Repair

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R11
selected_loop = 108
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = C31_STRICT_ROW_FINAL_REPAIR_VALUEUP_POLICY_TO_COMPANY_CASH_BRIDGE_AND_C21_C22_REROUTE
selected_priority_bucket = Priority 0 strict-row repair / final local C31 floor fill
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

The static No-Repeat Index still lists `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` as a low-coverage Priority 0 archetype. Conversation-local work has already produced several C31 narrative and cleanup files, but some of the earlier policy/value-up rows were summary-like or source-proxy rows. This run therefore performs a narrow strict-row final repair: add five complete trigger rows with 30D/90D/180D MFE and MAE fields, then keep them blocked from promotion until stock-web shard/profile and non-price URLs are refetched.

The mechanism is not “policy headline = buy.” C31 owns the bridge from a policy/subsidy/legislation/value-up headline to company-level cash, tax/tariff benefit, direct subsidy capture, capital return, or measurable profitability change. If the dominant mechanism is ROE/PBR capital return, it must be rerouted to C21. If the dominant mechanism is insurance CSM/reserve/rate-cycle quality, it must be rerouted to C22.

## 2. Stock-Web validation scope

```text
manifest_url = https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
max_date = 2026-02-20
zero_volume_and_zero_ohlc_excluded_from_calibration_shards = true
corporate_action_contaminated_windows_blocked_by_default = true
```

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_financial_policy_shard_paths_after_raw_cache_miss
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
promotion_allowed_now = false
```

## 3. Aggregate result

```json
{
  "new_independent_case_count": 5,
  "strict_row_repair_case_count": 5,
  "cross_canonical_price_row_reuse_count": 5,
  "same_archetype_new_symbol_count": 5,
  "same_archetype_new_trigger_family_count": 5,
  "calibration_usable_case_count": 5,
  "positive_case_count": 2,
  "mixed_positive_count": 2,
  "counterexample_count": 1,
  "local_4b_watch_count": 1,
  "source_proxy_only_count": 5,
  "evidence_url_pending_count": 5,
  "batch_reverification_required_count": 5,
  "current_profile_error_count": 5,
  "avg_MFE_30D_pct": 8.54,
  "avg_MAE_30D_pct": -7.88,
  "avg_MFE_90D_pct": 15.56,
  "avg_MAE_90D_pct": -12.34,
  "avg_MFE_180D_pct": 22.22,
  "avg_MAE_180D_pct": -18.9
}
```

Interpretation: C31 can act as a policy-to-cash bridge only after the company-specific path is visible. Broad value-up, subsidy, or legislation language is just a gate key; it does not open Stage3-Green by itself.

## 4. Trigger rows JSONL

```jsonl
{"source_row_type":"trigger_row_representative","schema_version":"v12_stock_web_residual","research_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R11_loop_108_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","selected_round":"R11","selected_loop":108,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRICT_ROW_FINAL_REPAIR_VALUEUP_POLICY_TO_COMPANY_CASH_BRIDGE_AND_C21_C22_REROUTE","selected_priority_bucket":"Priority 0 strict-row repair / final local C31 floor fill","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"105560","company_name":"KB금융","trigger_type":"Stage3-Yellow","trigger_family":"policy_valueup_bank_capital_return_cash_bridge","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":64400,"entry_price_basis":"prior_stock_web_tradable_raw_close_reused","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.8,"MAE_30D_pct":-4.6,"MFE_90D_pct":17.5,"MAE_90D_pct":-8.8,"MFE_180D_pct":26.4,"MAE_180D_pct":-13.9,"peak_180d_pct":26.4,"drawdown_180d_pct":-13.9,"classification":"positive","positive_or_counterexample":"positive","calibration_usable":true,"promotion_usable_without_reverification":false,"dedupe_for_aggregate":true,"duplicate_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|105560|Stage3-Yellow|2024-02-26","current_profile_error":true,"current_profile_error_type":"policy_valueup_headline_can_duplicate_C21_ROE_PBR_without_direct_cash_bridge","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse":true,"reroute_if_dominant_mechanism":"C21_if_ROE_PBR_capital_return_execution_dominates","stage2_evidence_fields":["policy_valueup_headline","sector_relative_strength","capital_return_proxy"],"stage3_evidence_fields":["verified_buyback_or_dividend_execution","ROE_bridge","company_cash_bridge"],"stage4b_evidence_fields":["local_price_spike_peak","fresh_non_price_policy_to_cash_evidence_required"],"raw_component_score_breakdown":{"EPS_FCF_Explosion":8,"Earnings_Visibility_Quality":13,"Bottleneck_Pricing_Power":5,"Market_Mispricing":15,"Valuation_Rerating_Runway":12,"Capital_Allocation":15,"Information_Confidence":4},"simulated_total_score":72,"score_return_alignment":"Positive MFE exists, but C31 should reroute to C21 unless the policy itself creates incremental cash","notes":"Policy/value-up bridge candidate; keep blocked until direct capital-return evidence is refetched."}
{"source_row_type":"trigger_row_representative","schema_version":"v12_stock_web_residual","research_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R11_loop_108_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","selected_round":"R11","selected_loop":108,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRICT_ROW_FINAL_REPAIR_VALUEUP_POLICY_TO_COMPANY_CASH_BRIDGE_AND_C21_C22_REROUTE","selected_priority_bucket":"Priority 0 strict-row repair / final local C31 floor fill","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"055550","company_name":"신한지주","trigger_type":"Stage3-Yellow","trigger_family":"policy_valueup_bank_capital_return_cash_bridge","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":44400,"entry_price_basis":"prior_stock_web_tradable_raw_close_reused","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv","profile_path":"atlas/symbol_profiles/055/055550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.1,"MAE_30D_pct":-5.8,"MFE_90D_pct":13.7,"MAE_90D_pct":-10.9,"MFE_180D_pct":22.5,"MAE_180D_pct":-15.4,"peak_180d_pct":22.5,"drawdown_180d_pct":-15.4,"classification":"mixed_positive","positive_or_counterexample":"mixed_positive","calibration_usable":true,"promotion_usable_without_reverification":false,"dedupe_for_aggregate":true,"duplicate_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|055550|Stage3-Yellow|2024-03-07","current_profile_error":true,"current_profile_error_type":"policy_label_lacks_direct_incremental_cash_bridge","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse":true,"reroute_if_dominant_mechanism":"C21_if_ROE_PBR_capital_return_execution_dominates","stage2_evidence_fields":["policy_valueup_headline","sector_relative_strength","capital_return_proxy"],"stage3_evidence_fields":["verified_buyback_or_dividend_execution","ROE_bridge","company_cash_bridge"],"stage4b_evidence_fields":["local_price_spike_peak","fresh_non_price_policy_to_cash_evidence_required"],"raw_component_score_breakdown":{"EPS_FCF_Explosion":7,"Earnings_Visibility_Quality":13,"Bottleneck_Pricing_Power":5,"Market_Mispricing":14,"Valuation_Rerating_Runway":11,"Capital_Allocation":14,"Information_Confidence":4},"simulated_total_score":68,"score_return_alignment":"Good enough for watch, not enough for C31 Green without verified policy-to-cash evidence","notes":"Treat as Stage2-Actionable unless buyback/dividend execution is verified."}
{"source_row_type":"trigger_row_representative","schema_version":"v12_stock_web_residual","research_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R11_loop_108_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","selected_round":"R11","selected_loop":108,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRICT_ROW_FINAL_REPAIR_VALUEUP_POLICY_TO_COMPANY_CASH_BRIDGE_AND_C21_C22_REROUTE","selected_priority_bucket":"Priority 0 strict-row repair / final local C31 floor fill","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"086790","company_name":"하나금융지주","trigger_type":"Stage3-Green","trigger_family":"policy_valueup_bank_capital_return_cash_bridge","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":58300,"entry_price_basis":"prior_stock_web_tradable_raw_close_reused","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.0,"MAE_30D_pct":-3.9,"MFE_90D_pct":22.8,"MAE_90D_pct":-7.5,"MFE_180D_pct":31.2,"MAE_180D_pct":-10.7,"peak_180d_pct":31.2,"drawdown_180d_pct":-10.7,"classification":"positive","positive_or_counterexample":"positive","calibration_usable":true,"promotion_usable_without_reverification":false,"dedupe_for_aggregate":true,"duplicate_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|086790|Stage3-Green|2024-02-29","current_profile_error":true,"current_profile_error_type":"C31_can_overclaim_C21_valueup_capital_return_mechanism","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse":true,"reroute_if_dominant_mechanism":"C21_if_ROE_PBR_capital_return_execution_dominates","stage2_evidence_fields":["policy_valueup_headline","sector_relative_strength","capital_return_proxy"],"stage3_evidence_fields":["verified_buyback_or_dividend_execution","ROE_bridge","company_cash_bridge"],"stage4b_evidence_fields":["local_price_spike_peak","fresh_non_price_policy_to_cash_evidence_required"],"raw_component_score_breakdown":{"EPS_FCF_Explosion":9,"Earnings_Visibility_Quality":14,"Bottleneck_Pricing_Power":5,"Market_Mispricing":15,"Valuation_Rerating_Runway":13,"Capital_Allocation":16,"Information_Confidence":4},"simulated_total_score":76,"score_return_alignment":"Strong price path, but C31 still needs direct verified policy-to-cash evidence or reroute to C21","notes":"Positive value-up path but not a pure C31 policy-subsidy row until company-level cash bridge is proven."}
{"source_row_type":"trigger_row_representative","schema_version":"v12_stock_web_residual","research_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R11_loop_108_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","selected_round":"R11","selected_loop":108,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRICT_ROW_FINAL_REPAIR_VALUEUP_POLICY_TO_COMPANY_CASH_BRIDGE_AND_C21_C22_REROUTE","selected_priority_bucket":"Priority 0 strict-row repair / final local C31 floor fill","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"316140","company_name":"우리금융지주","trigger_type":"Stage2-Actionable","trigger_family":"policy_valueup_bank_capital_return_cash_bridge","trigger_date":"2024-04-02","entry_date":"2024-04-02","entry_price":14520,"entry_price_basis":"prior_stock_web_tradable_raw_close_reused","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv","profile_path":"atlas/symbol_profiles/316/316140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.7,"MAE_30D_pct":-9.8,"MFE_90D_pct":11.0,"MAE_90D_pct":-17.5,"MFE_180D_pct":18.6,"MAE_180D_pct":-27.4,"peak_180d_pct":18.6,"drawdown_180d_pct":-27.4,"classification":"counterexample","positive_or_counterexample":"counterexample","calibration_usable":true,"promotion_usable_without_reverification":false,"dedupe_for_aggregate":true,"duplicate_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|316140|Stage2-Actionable|2024-04-02","current_profile_error":true,"current_profile_error_type":"early_policy_watch_has_MFE_but_deep_MAE_without_cash_bridge","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse":true,"reroute_if_dominant_mechanism":"C21_if_ROE_PBR_capital_return_execution_dominates","stage2_evidence_fields":["policy_valueup_headline","sector_relative_strength"],"stage3_evidence_fields":["verified_buyback_or_dividend_execution","company_cash_bridge_missing"],"stage4b_evidence_fields":["local_price_spike_peak","fresh_non_price_policy_to_cash_evidence_required"],"raw_component_score_breakdown":{"EPS_FCF_Explosion":6,"Earnings_Visibility_Quality":11,"Bottleneck_Pricing_Power":4,"Market_Mispricing":13,"Valuation_Rerating_Runway":10,"Capital_Allocation":10,"Information_Confidence":3},"simulated_total_score":57,"score_return_alignment":"Watch remains useful, but deep MAE blocks Stage3/Green promotion","notes":"Counterexample: broad policy label and value-up beta did not provide a clean company-specific C31 bridge."}
{"source_row_type":"trigger_row_representative","schema_version":"v12_stock_web_residual","research_version":"v12","research_file":"e2r_stock_web_v12_residual_round_R11_loop_108_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","selected_round":"R11","selected_loop":108,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_STRICT_ROW_FINAL_REPAIR_VALUEUP_POLICY_TO_COMPANY_CASH_BRIDGE_AND_C21_C22_REROUTE","selected_priority_bucket":"Priority 0 strict-row repair / final local C31 floor fill","source_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"138930","company_name":"BNK금융지주","trigger_type":"Stage2-Actionable","trigger_family":"policy_valueup_regional_bank_capital_return_cash_bridge","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":8370,"entry_price_basis":"prior_stock_web_tradable_raw_close_reused","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.1,"MAE_30D_pct":-15.3,"MFE_90D_pct":12.8,"MAE_90D_pct":-17.0,"MFE_180D_pct":12.4,"MAE_180D_pct":-27.1,"peak_180d_pct":12.8,"drawdown_180d_pct":-27.1,"classification":"mixed_positive","positive_or_counterexample":"mixed_positive","calibration_usable":true,"promotion_usable_without_reverification":false,"dedupe_for_aggregate":true,"duplicate_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|138930|Stage2-Actionable|2024-05-09","current_profile_error":true,"current_profile_error_type":"regional_bank_policy_beta_needs_capital_return_execution_bridge","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"cross_canonical_price_row_reuse":true,"reroute_if_dominant_mechanism":"C21_if_ROE_PBR_capital_return_execution_dominates","stage2_evidence_fields":["policy_valueup_headline","regional_bank_relative_strength"],"stage3_evidence_fields":["verified_buyback_or_dividend_execution_missing","company_cash_bridge_pending"],"stage4b_evidence_fields":["local_price_spike_peak","fresh_non_price_policy_to_cash_evidence_required"],"raw_component_score_breakdown":{"EPS_FCF_Explosion":6,"Earnings_Visibility_Quality":11,"Bottleneck_Pricing_Power":4,"Market_Mispricing":13,"Valuation_Rerating_Runway":9,"Capital_Allocation":11,"Information_Confidence":3},"simulated_total_score":57,"score_return_alignment":"Can remain early Stage2 watch, but high MAE and source proxy block Green/full4B","notes":"Mixed: positive path exists but lacks enough company-specific policy-to-cash confirmation."}
```

## 5. Score-return alignment notes

- `Stage3-Green` for C31 requires verified company-level cash conversion, not merely a policy or value-up headline.
- C21/C22 reroute must happen before score simulation when the true mechanism is capital return, CSM/reserve quality, or rate cycle rather than policy/subsidy capture itself.
- `source_proxy_only` rows are research-useful but promotion-blocked until the stock-web shard/profile and non-price evidence URLs are refetched.
- Deep MAE rows can stay as early policy watch rows but should not unlock Green/full 4B.

## 6. Current calibrated profile stress test

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual error: C31 can over-credit broad policy/value-up language if the scoring layer does not require a verified policy-to-company-cash bridge and does not reroute sector-specific financial mechanics to C21/C22 first.

## 7. Shadow rule candidates

```json
[
  {
    "shadow_rule_id": "C31_POLICY_TO_COMPANY_CASH_BRIDGE_REQUIRED",
    "scope": "canonical_archetype",
    "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
    "rule": "Stage3-Yellow or Stage3-Green requires a verified bridge from policy/subsidy/legislation/value-up headline to company-level cash, capital return, tax/tariff/subsidy capture, or operating profitability change.",
    "suggested_effect": "cap at Stage2-Actionable if bridge is missing",
    "production_scoring_changed": false
  },
  {
    "shadow_rule_id": "C31_C21_C22_REROUTE_BEFORE_SCORING",
    "scope": "cross_canonical",
    "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
    "rule": "If the dominant mechanism is bank/brokerage ROE-PBR capital return, reroute to C21. If it is insurance CSM/reserve/rate-cycle quality, reroute to C22. C31 owns only the policy-to-cash bridge.",
    "suggested_effect": "contaminant_reroute",
    "production_scoring_changed": false
  },
  {
    "shadow_rule_id": "C31_SOURCE_PROXY_ONLY_BLOCKS_GREEN_UNTIL_REVERIFIED",
    "scope": "data_quality",
    "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
    "rule": "Rows marked source_proxy_only or evidence_url_pending cannot unlock Stage3-Green/full 4B until stock-web shard and non-price evidence URLs are refetched.",
    "suggested_effect": "block_green_promotion",
    "production_scoring_changed": false
  },
  {
    "shadow_rule_id": "C31_HIGH_MAE_POLICY_LABEL_STAGE_CAP",
    "scope": "canonical_archetype",
    "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
    "rule": "If MAE_180D is below -25% and the policy-to-cash bridge is not refreshed, cap at Stage2 or local 4B watch even when early MFE is positive.",
    "suggested_effect": "high_MAE_guardrail",
    "production_scoring_changed": false
  }
]
```

## 8. Novelty and duplicate check

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
reused_case_count = 0
same_canonical_research = allowed
cross_canonical_price_row_reuse = allowed_with_batch_reverification
source_proxy_only = true
evidence_url_pending = true
new_C31_complete_trigger_rows_added = 5
conversation_local_strict_C31_rows_after_this_run_estimate = 25 -> 30
```

This run intentionally avoids immediate production-weight changes. It is a strict-row final repair artifact for later batch ingestion.

## 9. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail | source_proxy_only_block
existing_axis_weakened = null
new_axis_proposed = C31_POLICY_TO_COMPANY_CASH_BRIDGE_REQUIRED | C31_C21_C22_REROUTE_BEFORE_SCORING | C31_SOURCE_PROXY_ONLY_BLOCKS_GREEN_UNTIL_REVERIFIED | C31_HIGH_MAE_POLICY_LABEL_STAGE_CAP
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research.

You are the coding agent for Songdaiki/stock_agent. Ingest this MD only after verifying:
1. The file name matches the v12 standard regex.
2. Every trigger JSONL row has entry_date, entry_price, trigger_type, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct, large_sector_id, and canonical_archetype_id.
3. All rows marked source_proxy_only/evidence_url_pending are refetched against stock-web profile + tradable shard paths.
4. Rows whose non-price evidence remains unavailable must remain blocked_by_data_quality.
5. Reroute rows to C21/C22 if the verified mechanism is capital return or insurance reserve/CSM rather than policy/subsidy cash conversion itself.
```

## 11. Next research state

```text
completed_round = R11
completed_loop = 108
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0 strict-row repair / final local C31 floor fill
next_recommended_archetypes = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_static_reverify, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_static_reverify, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_static_reverify
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
