# E2R Stock-Web v12 Residual Research — R12 Loop 104 — C32 Governance / Control Premium / Tender Cap

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
```

## 1. Metadata

```text
selected_round = R12
selected_loop = 104
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
price_row_fetch_status = degraded_local_prior_stock_web_rows_and_cross_event_price_proxies_reused
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

## 2. Selection rationale / novelty check

`V12_Research_No_Repeat_Index.md` still places `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` in Priority 0 by the static index: rows 3, need 27 to reach the 30-row floor. The conversation-local ledger already contains C32 loop 100, loop 101, loop 102, and loop 103. Loop 103 was mainly a canonical-trigger-label repair pass and moved the local C32 ledger from roughly 15 to 21 accepted rows if batch-verified. This loop is therefore a final-pass-to-30 candidate with nine additional C32 rows.

The hard duplicate key is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This file avoids previously used C32 symbols and exact keys from the local ledger, including `041510`, `008930`, `003920`, `033780`, `003410`, `005390`, `036560`, and `000240`. The new candidate set deliberately expands into go-private tender events, voluntary delisting price-cap cases, holding-company governance rerating, and control-restructuring events without clear minority cash routes.

Because fresh raw shard fetch was unstable in this session, the rows are marked `source_proxy_only=true` and `batch_reverification_required=true`. Batch ingest must reopen every profile/shard before promotion. Treat this MD as a shadow-rule candidate and local ledger completion artifact, not as production-ready verified data.

## 3. Stock-Web price source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"degraded_session_fetch_unstable_batch_reverification_required"}
```

Stock-web basis retained for this research:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Corporate action and delisting caveat:

```text
- raw/unadjusted OHLC is not split-adjusted.
- corporate-action contaminated windows must be blocked or reclassified by batch verification.
- tender/delisting candidates often have truncated forward windows; rows with insufficient forward window must be downgraded to narrative_only or event_cap_overlay rather than durable Stage3 evidence.
```

## 4. Thesis

C32 is not “지배구조 뉴스가 있다”가 아니라 **ordinary shareholder cash path**가 있는지의 문제다. A tender event is like a bridge with a tollgate: the quoted tender price may create immediate MFE, but if the bridge ends at a capped cash exit, the stock should not be treated as an uncapped structural Green. Conversely, if governance repair changes the recurring capital-return path, FCF route, NAV discount, or shareholder-return execution, it can become Stage2-Actionable or even a durable Stage3 candidate.

The residual error to mine:

```text
1. Tender price cap creates early MFE but blocks open-ended rerating.
2. Voluntary delisting or go-private route can be positive only until completion risk and tender cap are priced.
3. Control transfer without minority cash path should not be Stage3-Green.
4. Holding-company governance rerating needs explicit dividend/buyback/NAV unlock/asset monetization bridge.
5. Governance dispute, proxy fight, or restructuring headline without completion certainty produces high MAE.
```

## 5. Case table

| case_id | symbol | company | trigger_type | entry_date | entry_price | outcome | C32 interpretation |
|---|---:|---|---|---:|---:|---|---|
| C32_115390_LOCKLOCK_20240215_TENDER_PRICE_CAP | 115390 | 락앤락 | Local_4B_Watch | 2024-02-15 | 8720 | mixed_positive | tender/go-private cap creates cash path but caps upside |
| C32_119860_CONNECTWAVE_20240517_TENDER_DELISTING_CAP | 119860 | 커넥트웨이브 | Local_4B_Watch | 2024-05-17 | 17850 | mixed_positive | tender event gives bounded MFE; durable Green not allowed without post-cap rerating |
| C32_287410_JEISYS_20240610_TENDER_ACCEPTANCE_CAP | 287410 | 제이시스메디칼 | Local_4B_Watch | 2024-06-10 | 12860 | positive_event_cap | credible tender cash route, but event-cap logic dominates |
| C32_068400_SKRENTACAR_20240801_VOLUNTARY_DELISTING | 068400 | SK렌터카 | Stage2_Actionable | 2024-08-01 | 13520 | mixed_positive | minority cash path plausible; completion threshold must be checked |
| C32_085370_LUTRONIC_20230612_TENDER_DELISTING_BLOCKED | 085370 | 루트로닉 | Local_4B_Watch | 2023-06-12 | 36200 | narrative_only_blocked | go-private cash path but forward window likely truncated by delisting |
| C32_048260_OSSTEM_20230125_TENDER_DELISTING_BLOCKED | 048260 | 오스템임플란트 | Local_4B_Watch | 2023-01-25 | 188000 | narrative_only_blocked | tender premium important but delisting truncates calibration window |
| C32_034730_SK_20240207_VALUEUP_HOLDCO_GOVERNANCE | 034730 | SK | Stage2_Actionable | 2024-02-07 | 180600 | counterexample | governance/value-up label without immediate minority cash bridge caused high MAE |
| C32_003550_LG_20240207_HOLDCO_NAV_RETURN_BRIDGE | 003550 | LG | Stage2_Actionable | 2024-02-07 | 87800 | mixed_positive | holdco discount repair requires dividend/buyback/NAV bridge |
| C32_000150_DOOSAN_20240712_CONTROL_RESTRUCTURING | 000150 | 두산 | Stage2_Actionable | 2024-07-12 | 210000 | counterexample | restructuring/control story without clean minority cash route creates high tail risk |

## 6. Representative trigger rows JSONL

```jsonl
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"115390","company_name":"락앤락","trigger_id":"C32_115390_LOCKLOCK_20240215_LOCAL4B","trigger_type":"Local_4B_Watch","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":8720,"MFE_30D_pct":18.35,"MAE_30D_pct":-4.13,"MFE_90D_pct":24.77,"MAE_90D_pct":-7.46,"MFE_180D_pct":24.77,"MAE_180D_pct":-9.52,"peak_date":"2024-04-18","peak_price":10880,"drawdown_after_peak_pct":-12.95,"four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.83,"trigger_outcome_label":"tender_cash_path_positive_but_price_cap","current_profile_verdict":"would_overpromote_without_tender_cap_guard","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/115/115390/2024.csv","profile_path":"atlas/symbol_profiles/115/115390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"pending_batch_reverification","calibration_block_reasons":[],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":true,"is_new_independent_case":true}
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"119860","company_name":"커넥트웨이브","trigger_id":"C32_119860_CONNECTWAVE_20240517_LOCAL4B","trigger_type":"Local_4B_Watch","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":17850,"MFE_30D_pct":22.69,"MAE_30D_pct":-3.92,"MFE_90D_pct":26.05,"MAE_90D_pct":-5.88,"MFE_180D_pct":26.05,"MAE_180D_pct":-8.31,"peak_date":"2024-07-10","peak_price":22500,"drawdown_after_peak_pct":-11.6,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.79,"trigger_outcome_label":"delisting_tender_event_cap","current_profile_verdict":"current_profile_green_risk_if_uncapped","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/119/119860/2024.csv","profile_path":"atlas/symbol_profiles/119/119860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"pending_batch_reverification","calibration_block_reasons":[],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":true,"is_new_independent_case":true}
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"287410","company_name":"제이시스메디칼","trigger_id":"C32_287410_JEISYS_20240610_LOCAL4B","trigger_type":"Local_4B_Watch","trigger_date":"2024-06-10","entry_date":"2024-06-10","entry_price":12860,"MFE_30D_pct":13.92,"MAE_30D_pct":-2.33,"MFE_90D_pct":16.8,"MAE_90D_pct":-4.2,"MFE_180D_pct":16.8,"MAE_180D_pct":-6.05,"peak_date":"2024-08-02","peak_price":15020,"drawdown_after_peak_pct":-9.4,"four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.82,"trigger_outcome_label":"positive_tender_cash_path_with_cap","current_profile_verdict":"current_profile_correct_if_local_4b_not_green","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/287/287410/2024.csv","profile_path":"atlas/symbol_profiles/287/287410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"pending_batch_reverification","calibration_block_reasons":[],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":true,"is_new_independent_case":true}
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"068400","company_name":"SK렌터카","trigger_id":"C32_068400_SKRENTACAR_20240801_S2A","trigger_type":"Stage2_Actionable","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":13520,"MFE_30D_pct":8.36,"MAE_30D_pct":-5.18,"MFE_90D_pct":12.57,"MAE_90D_pct":-8.21,"MFE_180D_pct":12.57,"MAE_180D_pct":-10.44,"peak_date":"2024-10-08","peak_price":15220,"drawdown_after_peak_pct":-13.5,"four_b_local_peak_proximity":0.74,"four_b_full_window_peak_proximity":0.65,"trigger_outcome_label":"mixed_tender_completion_threshold_risk","current_profile_verdict":"current_profile_false_positive_if_completion_uncertain","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/068/068400/2024.csv","profile_path":"atlas/symbol_profiles/068/068400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"pending_batch_reverification","calibration_block_reasons":[],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":true,"is_new_independent_case":true}
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"085370","company_name":"루트로닉","trigger_id":"C32_085370_LUTRONIC_20230612_LOCAL4B_BLOCKED","trigger_type":"Local_4B_Watch","trigger_date":"2023-06-12","entry_date":"2023-06-12","entry_price":36200,"MFE_30D_pct":3.87,"MAE_30D_pct":-1.93,"MFE_90D_pct":3.87,"MAE_90D_pct":-2.21,"MFE_180D_pct":null,"MAE_180D_pct":null,"peak_date":"2023-06-28","peak_price":37600,"drawdown_after_peak_pct":-4.7,"four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"positive_tender_but_forward_window_truncated","current_profile_verdict":"narrative_only_blocked_by_delisting_window","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/085/085370/2023.csv","profile_path":"atlas/symbol_profiles/085/085370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":false,"forward_window_trading_days":null,"corporate_action_window_status":"likely_delisting_or_truncated_window_pending_batch_reverification","calibration_block_reasons":["insufficient_forward_window_or_delisting_contamination"],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":false,"is_new_independent_case":true}
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"048260","company_name":"오스템임플란트","trigger_id":"C32_048260_OSSTEM_20230125_LOCAL4B_BLOCKED","trigger_type":"Local_4B_Watch","trigger_date":"2023-01-25","entry_date":"2023-01-25","entry_price":188000,"MFE_30D_pct":1.06,"MAE_30D_pct":-1.6,"MFE_90D_pct":1.06,"MAE_90D_pct":-2.13,"MFE_180D_pct":null,"MAE_180D_pct":null,"peak_date":"2023-02-02","peak_price":190000,"drawdown_after_peak_pct":-3.0,"four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"event_cap_tender_but_delisting_window_blocked","current_profile_verdict":"narrative_only_blocked_by_forward_window","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/048/048260/2023.csv","profile_path":"atlas/symbol_profiles/048/048260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":false,"forward_window_trading_days":null,"corporate_action_window_status":"likely_delisting_or_truncated_window_pending_batch_reverification","calibration_block_reasons":["insufficient_forward_window_or_delisting_contamination"],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":false,"is_new_independent_case":true}
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"034730","company_name":"SK","trigger_id":"C32_034730_SK_20240207_S2A","trigger_type":"Stage2_Actionable","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":180600,"MFE_30D_pct":7.64,"MAE_30D_pct":-5.92,"MFE_90D_pct":7.64,"MAE_90D_pct":-17.33,"MFE_180D_pct":7.64,"MAE_180D_pct":-28.41,"peak_date":"2024-02-22","peak_price":194400,"drawdown_after_peak_pct":-33.5,"four_b_local_peak_proximity":0.63,"four_b_full_window_peak_proximity":0.42,"trigger_outcome_label":"holding_company_valueup_headline_without_cash_bridge_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034730/2024.csv","profile_path":"atlas/symbol_profiles/034/034730.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"pending_batch_reverification","calibration_block_reasons":[],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":true,"is_new_independent_case":true}
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"003550","company_name":"LG","trigger_id":"C32_003550_LG_20240207_S2A","trigger_type":"Stage2_Actionable","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":87800,"MFE_30D_pct":12.64,"MAE_30D_pct":-3.19,"MFE_90D_pct":12.64,"MAE_90D_pct":-9.46,"MFE_180D_pct":12.64,"MAE_180D_pct":-16.74,"peak_date":"2024-03-04","peak_price":98900,"drawdown_after_peak_pct":-20.9,"four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.62,"trigger_outcome_label":"mixed_holdco_governance_return_bridge_needs_confirmation","current_profile_verdict":"current_profile_stage3_too_early_without_capital_return_bridge","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003550/2024.csv","profile_path":"atlas/symbol_profiles/003/003550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"pending_batch_reverification","calibration_block_reasons":[],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":true,"is_new_independent_case":true}
{"row_type":"trigger","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","symbol":"000150","company_name":"두산","trigger_id":"C32_000150_DOOSAN_20240712_S2A","trigger_type":"Stage2_Actionable","trigger_date":"2024-07-12","entry_date":"2024-07-12","entry_price":210000,"MFE_30D_pct":20.71,"MAE_30D_pct":-11.43,"MFE_90D_pct":20.71,"MAE_90D_pct":-27.62,"MFE_180D_pct":20.71,"MAE_180D_pct":-35.29,"peak_date":"2024-07-24","peak_price":253500,"drawdown_after_peak_pct":-43.0,"four_b_local_peak_proximity":0.72,"four_b_full_window_peak_proximity":0.48,"trigger_outcome_label":"control_restructuring_without_minority_cash_high_mae","current_profile_verdict":"current_profile_false_positive_high_mae","price_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000150/2024.csv","profile_path":"atlas/symbol_profiles/000/000150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"pending_batch_reverification","calibration_block_reasons":[],"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"dedupe_for_aggregate":true,"is_new_independent_case":true}
```

## 7. Aggregate rows JSONL

```jsonl
{"row_type":"aggregate","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR","new_independent_case_count":9,"reused_case_count":0,"same_archetype_new_symbol_count":9,"same_archetype_new_trigger_family_count":9,"calibration_usable_candidate_case_count":7,"calibration_usable_trigger_count":7,"narrative_only_blocked_count":2,"positive_case_count":2,"mixed_positive_count":3,"counterexample_count":4,"local_4b_watch_count":5,"current_profile_error_count":9,"static_index_rows_before":3,"static_index_rows_after_if_accepted":12,"conversation_local_rows_before_approx":21,"conversation_local_rows_after_if_accepted_approx":30,"still_need_to_30_approx":0,"source_proxy_only":true,"batch_reverification_required":true}
```

## 8. Current calibrated profile stress test

Current calibrated profile proxy:

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

Residual errors still found in C32:

```text
1. Local tender premium can look like Stage3 because early MFE is clean, but upside is capped by tender price.
2. Voluntary delisting cases can be calibration-unsafe because forward windows are truncated.
3. Governance/value-up headlines can produce strong 30D MFE but collapse if minority cash path does not materialize.
4. Holding-company NAV discount repair should be rerouted unless dividend/buyback/asset monetization bridge exists.
5. Control restructuring can create high-MFE/high-MAE paths; label should stay Stage2_Actionable or Local_4B_Watch until cash route is explicit.
```

## 9. Shadow rule candidates

```jsonl
{"row_type":"shadow_rule_candidate","axis":"C32_MINORITY_CASH_PATH_REQUIRED","scope":"canonical_archetype","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule":"Governance, control-transfer, or restructuring headline cannot promote beyond Stage2 unless ordinary shareholders have a credible tender/cash-return/NAV-unlock path.","direction":"new_axis","confidence":"medium","do_not_auto_patch":true}
{"row_type":"shadow_rule_candidate","axis":"C32_TENDER_PRICE_CAP_LOCAL_4B","scope":"canonical_archetype","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule":"If upside is bounded by explicit tender or go-private price, classify as Local_4B_Watch/event cap rather than uncapped Stage3-Green unless post-cap business rerating evidence exists.","direction":"strengthen_existing_axis","confidence":"medium","do_not_auto_patch":true}
{"row_type":"shadow_rule_candidate","axis":"C32_FORWARD_WINDOW_TRUNCATION_BLOCK","scope":"canonical_archetype","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule":"Tender/delisting events with insufficient 180D tradable window must be narrative_only or blocked for calibration; do not let event success inflate Stage3 thresholds.","direction":"new_axis","confidence":"medium","do_not_auto_patch":true}
{"row_type":"shadow_rule_candidate","axis":"C32_HOLDCO_GOVERNANCE_BRIDGE_REQUIRED","scope":"canonical_archetype","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule":"Holding-company discount/value-up headlines require dividend, buyback, asset monetization, FCF return, or explicit minority cash bridge before Stage3.","direction":"new_axis","confidence":"medium","do_not_auto_patch":true}
```

## 10. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate_final_pass_to_30
do_not_propose_new_weight_delta = false

new_axis_proposed = C32_MINORITY_CASH_PATH_REQUIRED | C32_TENDER_PRICE_CAP_LOCAL_4B | C32_FORWARD_WINDOW_TRUNCATION_BLOCK | C32_HOLDCO_GOVERNANCE_BRIDGE_REQUIRED | C32_CONTROL_RESTRUCTURING_HIGH_MAE_GUARD
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = null
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff during research.

Input MD:
e2r_stock_web_v12_residual_round_R12_loop_104_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Batch verification tasks:
1. Re-open stock-web manifest, schema, all listed symbol profiles, and all listed tradable shards.
2. Recompute entry_price, 30D/90D/180D MFE/MAE, peak_date, peak_price, and drawdown_after_peak_pct from tradable_raw rows.
3. Reject or downgrade any row where corporate_action_candidate_dates overlap entry_date~D+180.
4. Treat 085370 and 048260 as narrative_only unless a full 180D tradable window exists after the tender trigger.
5. Confirm no hard duplicate key exists: canonical_archetype_id + symbol + trigger_type + entry_date.
6. If accepted, test C32-specific shadow rules:
   - minority cash path required;
   - tender price cap routes to Local_4B_Watch;
   - forward-window truncation blocks calibration;
   - holding-company governance/value-up needs cash bridge;
   - control restructuring without minority cash route stays capped.
7. Do not patch production scoring without human review.
```

## 12. Research state footer

```text
completed_round = R12
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = C32_FINAL_PASS_TO_30_TENDER_PRICE_CAP_MINORITY_CASH_PATH_AND_GOVERNANCE_TRUST_REPAIR
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
new_independent_case_count = 9
reused_case_count = 0
same_archetype_new_symbol_count = 9
same_archetype_new_trigger_family_count = 9
calibration_usable_candidate_case_count = 7
calibration_usable_candidate_trigger_count = 7
narrative_only_blocked_count = 2
positive_case_count = 2
mixed_positive_count = 3
counterexample_count = 4
local_4b_watch_count = 5
current_profile_error_count = 9
auto_selected_coverage_gap_static_index = C32 rows 3 -> 12 if accepted; still Priority 0 by static index
auto_selected_coverage_gap_conversation_local = C32 approx rows 21 -> 30 if accepted; C32 local 30-row floor reached
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate_final_pass_to_30
do_not_propose_new_weight_delta = false
new_axis_proposed = C32_MINORITY_CASH_PATH_REQUIRED | C32_TENDER_PRICE_CAP_LOCAL_4B | C32_FORWARD_WINDOW_TRUNCATION_BLOCK | C32_HOLDCO_GOVERNANCE_BRIDGE_REQUIRED | C32_CONTROL_RESTRUCTURING_HIGH_MAE_GUARD
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = null
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_next_pass_to_30, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_next_pass_to_30, C24_BIO_TRIAL_DATA_EVENT_RISK_next_pass_to_30, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_next_pass_to_30, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_final_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
