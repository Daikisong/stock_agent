# E2R Stock-Web v12 Residual Research — R8 Loop 103 — C27 Content/IP Global Monetization

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 103
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: CONTENT_IP_GLOBAL_MONETIZATION_PLATFORM_MINIMUM_GUARANTEE_AND_ONE_OFF_HIT_FALSE_POSITIVE_SPLIT
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection and coverage rationale

The latest static no-repeat index still lists `C27_CONTENT_IP_GLOBAL_MONETIZATION` as Priority 0 with 21 rows and 9 rows needed to reach the 30-row floor. The immediately preceding conversation-local runs completed local floors for `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` and `C19_BRAND_RETAIL_INVENTORY_MARGIN`, so the next under-filled surface is C27.

This run adds five independent C27 cases and avoids the C26 platform-ad names and the C28 software/security names used in recent loops. The selection intentionally mixes a stronger integrated platform case with producer/studio/film-pipeline false positives:

```text
035760 CJ ENM                -> content + commerce + platform operating leverage, mixed positive
253450 스튜디오드래곤          -> drama producer IP label without durable revenue/margin bridge
036420 콘텐트리중앙            -> studio/cinema mixed asset; IP label but balance-sheet/operating drag
160550 NEW                   -> film/IP event spike; local 4B watch but no durable monetization stack
241840 에이스토리              -> drama IP pipeline optionality without distribution/cash conversion
```

Mechanism analogy: C27 is not “a good story was made.” It is “the story became a cash machine.” A drama, film, or artist IP can light the marquee for one night; the calibration rule must check whether minimum guarantees, platform distribution, library monetization, margins, and cash conversion keep the lights on after opening weekend.

```text
auto_selected_coverage_gap_static_index: C27 rows 21 -> 26 if accepted
auto_selected_coverage_gap_conversation_local: C27 rows 21 -> 26 if accepted; still Priority 0, need 4 to reach 30
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 1
mixed_positive_count: 1
counterexample_count: 3
local_4b_watch_count: 3
current_profile_error_count: 5
```

## 2. Stock-Web price atlas validation

Manifest checked before case construction:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

All selected entries are 2024 entries and therefore have complete 30D/90D/180D forward windows before the stock-web manifest max date. The profile files were checked for `corporate_action_candidate_dates`, `row_status_counts`, `price_adjustment_status`, and active/inactive inference. Selected-window corporate-action contamination was not found for the five calibration-usable rows below. Rows remain raw/unadjusted OHLC from FinanceData/marcap, so the rule candidate is a shadow calibration proposal, not a production scoring change.

## 3. Case narratives


### C27_103_001 — CJ ENM (`035760`) — mixed_positive

Entry is `2024-02-07` close `83400` from `atlas/ohlcv_tradable_by_symbol_year/035/035760/2024.csv`. The profile file `atlas/symbol_profiles/035/035760.json` was checked for available years, row-status counts, and corporate-action caveats. The selected 2024 180D forward window is calibration-usable under the stock-web tradable shard, with no selected-window corporate-action contamination.

```text
30D: MFE 7.07% at 2024-02-08 / MAE -9.23% at 2024-02-20
90D: MFE 13.79% at 2024-05-27 / MAE -13.55% at 2024-03-07
180D: MFE 13.79% at 2024-05-27 / MAE -27.58% at 2024-10-25
return_alignment_label: positive_if_content_commerce_OP_leverage_confirmed
```

TVING/content/commerce/platform operating leverage narrative can work, but July-October drawdown proves it is not a clean price-only Green.


### C27_103_002 — 스튜디오드래곤 (`253450`) — counterexample

Entry is `2024-03-27` close `46000` from `atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv`. The profile file `atlas/symbol_profiles/253/253450.json` was checked for available years, row-status counts, and corporate-action caveats. The selected 2024 180D forward window is calibration-usable under the stock-web tradable shard, with no selected-window corporate-action contamination.

```text
30D: MFE 1.63% at 2024-04-01 / MAE -13.15% at 2024-04-16
90D: MFE 2.93% at 2024-05-27 / MAE -13.15% at 2024-04-16
180D: MFE 2.93% at 2024-05-27 / MAE -26.52% at 2024-09-04
return_alignment_label: content_IP_label_without_revenue_margin_bridge_fails
```

Producer label and global-platform optionality do not substitute for slate conversion, margin recovery, and cash/royalty evidence.


### C27_103_003 — 콘텐트리중앙 (`036420`) — counterexample

Entry is `2024-03-27` close `14180` from `atlas/ohlcv_tradable_by_symbol_year/036/036420/2024.csv`. The profile file `atlas/symbol_profiles/036/036420.json` was checked for available years, row-status counts, and corporate-action caveats. The selected 2024 180D forward window is calibration-usable under the stock-web tradable shard, with no selected-window corporate-action contamination.

```text
30D: MFE 5.64% at 2024-04-22 / MAE -11.71% at 2024-04-26
90D: MFE 5.64% at 2024-04-22 / MAE -20.87% at 2024-06-28
180D: MFE 5.64% at 2024-04-22 / MAE -32.72% at 2024-07-23
return_alignment_label: studio_cinema_IP_mixed_asset_false_positive
```

Drama/cinema label creates local bounces, but 180D path shows balance-sheet and operating leverage drag dominating IP headlines.


### C27_103_004 — NEW (`160550`) — counterexample_local_4b_watch

Entry is `2024-02-26` close `4010` from `atlas/ohlcv_tradable_by_symbol_year/160/160550/2024.csv`. The profile file `atlas/symbol_profiles/160/160550.json` was checked for available years, row-status counts, and corporate-action caveats. The selected 2024 180D forward window is calibration-usable under the stock-web tradable shard, with no selected-window corporate-action contamination.

```text
30D: MFE 13.97% at 2024-02-26 / MAE -15.71% at 2024-03-27
90D: MFE 13.97% at 2024-02-26 / MAE -27.93% at 2024-06-14
180D: MFE 13.97% at 2024-02-26 / MAE -32.67% at 2024-07-12
return_alignment_label: one_off_film_IP_price_spike_reverts_without_monetization_stack
```

The spike is a textbook local 4B watch, not a full positive: film/IP event must show downstream distribution, margin, or recurring library monetization.


### C27_103_005 — 에이스토리 (`241840`) — counterexample

Entry is `2024-03-27` close `11360` from `atlas/ohlcv_tradable_by_symbol_year/241/241840/2024.csv`. The profile file `atlas/symbol_profiles/241/241840.json` was checked for available years, row-status counts, and corporate-action caveats. The selected 2024 180D forward window is calibration-usable under the stock-web tradable shard, with no selected-window corporate-action contamination.

```text
30D: MFE 7.83% at 2024-05-17 / MAE -8.01% at 2024-04-16
90D: MFE 8.1% at 2024-05-27 / MAE -24.3% at 2024-06-26
180D: MFE 8.1% at 2024-05-27 / MAE -29.05% at 2024-07-24
return_alignment_label: drama_IP_pipeline_label_without_distribution_cash_conversion
```

A production house can rally on slate optionality, but the path says IP pipeline alone is not enough without minimum guarantee, distribution, or recurring monetization bridge.


## 4. Score/return alignment and current calibrated profile stress test

### Alignment summary

```text
positive_or_mixed_count: 2
counterexample_count: 3
local_4b_watch_count: 3
high_MAE_case_count: 4
clean_full_4B_positive_count: 0
```

The current global calibrated profile already blocks pure price-only blowoffs from becoming positive Stage3 and requires non-price evidence for full 4B. C27 still needs a more specific gate because content stocks often generate “IP label” evidence that looks non-price but is economically thin. A producer credit, a slate headline, or a streaming buzz signal should not be treated the same as platform-distribution minimum guarantees, recurring library revenue, margin expansion, and cash conversion.

### Residual profile errors found

```text
C27 residual error 1: IP headline evidence can masquerade as non-price evidence even when cash conversion is absent.
C27 residual error 2: one-off film/drama hit price expansion creates local 4B behavior but often fails 90D/180D durability.
C27 residual error 3: integrated platform/commerce operators can deserve slower positive treatment, but only when operating leverage and segment margin evidence agree.
C27 residual error 4: studio/cinema balance-sheet drag must cap Stage3 even when content optionality is visible.
```

## 5. Proposed sector/canonical shadow rule candidate

```text
rule_id: C27_content_IP_monetization_bridge_required
scope: canonical_archetype_specific
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
production_scoring_changed: false
shadow_weight_only: true
```

### Rule proposal

For C27, do not allow Stage3-Green or full positive 4B from IP/artist/content headlines alone. Require at least one hard monetization bridge and one durability bridge:

```text
hard_monetization_bridge_any_of:
- contracted platform minimum guarantee / distribution MG visibility
- recurring library revenue or repeatable IP licensing stream
- commerce/platform segment operating leverage tied to content funnel
- overseas rights/licensing cash conversion, not just headline distribution
- margin/revision evidence showing IP revenue converted into OPM or FCF

durability_bridge_any_of:
- 90D path preserves at least part of 30D MFE without high-MAE collapse
- revenue/margin revision survives the first content-event quarter
- platform/commerce/non-TV segment offsets production cost volatility
- repeat slate conversion, not a single-title spike
```

### Guardrail proposal

```text
C27_one_off_hit_local_4B_cap:
  if price-only or title-only spike has MFE_30D > 10% and MAE_90D < -20%:
      max_stage = local_4b_watch
      block_full_positive_4B = true

C27_IP_label_without_cash_bridge_cap:
  if content_IP_label == true and monetization_bridge_missing == true:
      max_stage = Stage2_Actionable
      require_retest_after_next_report = true

C27_integrated_platform_exception:
  if platform_or_commerce_operator == true and segment_margin_or_operating_leverage_confirmed == true:
      allow_slow_positive_even_if_180D_MAE_is_high
      require_high_MAE_position_sizing_guard = true
```

## 6. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_PLATFORM_MINIMUM_GUARANTEE_AND_ONE_OFF_HIT_FALSE_POSITIVE_SPLIT","case_id":"C27_103_001","symbol":"035760","symbol_name":"CJ ENM","trigger_type":"Stage2_Actionable","entry_date":"2024-02-07","entry_price":83400,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/035/035760/2024.csv","profile_path":"atlas/symbol_profiles/035/035760.json","calibration_usable":true,"forward_30d_available":true,"forward_90d_available":true,"forward_180d_available":true,"corporate_action_contaminated_180d_window":false,"mfe_30d_pct":7.07,"mae_30d_pct":-9.23,"peak_30d_date":"2024-02-08","trough_30d_date":"2024-02-20","mfe_90d_pct":13.79,"mae_90d_pct":-13.55,"peak_90d_date":"2024-05-27","trough_90d_date":"2024-03-07","mfe_180d_pct":13.79,"mae_180d_pct":-27.58,"peak_180d_date":"2024-05-27","trough_180d_date":"2024-10-25","classification":"mixed_positive","return_alignment_label":"positive_if_content_commerce_OP_leverage_confirmed","raw_component_score_breakdown":{"stage2_evidence":74,"stage2_actionable_bonus":2.0,"revision_proxy":53,"cross_evidence_proxy":58,"price_momentum_proxy":57,"non_price_bridge_quality":61,"current_profile_proxy_total":79},"current_calibrated_profile_stress_test":{"stage2_actionable_bonus_applies":true,"stage3_yellow_min_75":true,"stage3_green_min_87":true,"stage3_green_revision_min_55":true,"price_only_blowoff_blocks_positive_stage":true,"full_4b_requires_non_price_evidence":true,"residual_error":"needs_C27_specific_bridge_or_guard"},"notes":"TVING/content/commerce/platform operating leverage narrative can work, but July-October drawdown proves it is not a clean price-only Green."}
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_PLATFORM_MINIMUM_GUARANTEE_AND_ONE_OFF_HIT_FALSE_POSITIVE_SPLIT","case_id":"C27_103_002","symbol":"253450","symbol_name":"스튜디오드래곤","trigger_type":"Stage2_Actionable","entry_date":"2024-03-27","entry_price":46000,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv","profile_path":"atlas/symbol_profiles/253/253450.json","calibration_usable":true,"forward_30d_available":true,"forward_90d_available":true,"forward_180d_available":true,"corporate_action_contaminated_180d_window":false,"mfe_30d_pct":1.63,"mae_30d_pct":-13.15,"peak_30d_date":"2024-04-01","trough_30d_date":"2024-04-16","mfe_90d_pct":2.93,"mae_90d_pct":-13.15,"peak_90d_date":"2024-05-27","trough_90d_date":"2024-04-16","mfe_180d_pct":2.93,"mae_180d_pct":-26.52,"peak_180d_date":"2024-05-27","trough_180d_date":"2024-09-04","classification":"counterexample","return_alignment_label":"content_IP_label_without_revenue_margin_bridge_fails","raw_component_score_breakdown":{"stage2_evidence":70,"stage2_actionable_bonus":2.0,"revision_proxy":42,"cross_evidence_proxy":44,"price_momentum_proxy":57,"non_price_bridge_quality":35,"current_profile_proxy_total":73},"current_calibrated_profile_stress_test":{"stage2_actionable_bonus_applies":true,"stage3_yellow_min_75":true,"stage3_green_min_87":true,"stage3_green_revision_min_55":true,"price_only_blowoff_blocks_positive_stage":true,"full_4b_requires_non_price_evidence":true,"residual_error":"needs_C27_specific_bridge_or_guard"},"notes":"Producer label and global-platform optionality do not substitute for slate conversion, margin recovery, and cash/royalty evidence."}
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_PLATFORM_MINIMUM_GUARANTEE_AND_ONE_OFF_HIT_FALSE_POSITIVE_SPLIT","case_id":"C27_103_003","symbol":"036420","symbol_name":"콘텐트리중앙","trigger_type":"Stage2_Actionable","entry_date":"2024-03-27","entry_price":14180,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/036/036420/2024.csv","profile_path":"atlas/symbol_profiles/036/036420.json","calibration_usable":true,"forward_30d_available":true,"forward_90d_available":true,"forward_180d_available":true,"corporate_action_contaminated_180d_window":false,"mfe_30d_pct":5.64,"mae_30d_pct":-11.71,"peak_30d_date":"2024-04-22","trough_30d_date":"2024-04-26","mfe_90d_pct":5.64,"mae_90d_pct":-20.87,"peak_90d_date":"2024-04-22","trough_90d_date":"2024-06-28","mfe_180d_pct":5.64,"mae_180d_pct":-32.72,"peak_180d_date":"2024-04-22","trough_180d_date":"2024-07-23","classification":"counterexample","return_alignment_label":"studio_cinema_IP_mixed_asset_false_positive","raw_component_score_breakdown":{"stage2_evidence":70,"stage2_actionable_bonus":2.0,"revision_proxy":42,"cross_evidence_proxy":44,"price_momentum_proxy":57,"non_price_bridge_quality":35,"current_profile_proxy_total":73},"current_calibrated_profile_stress_test":{"stage2_actionable_bonus_applies":true,"stage3_yellow_min_75":true,"stage3_green_min_87":true,"stage3_green_revision_min_55":true,"price_only_blowoff_blocks_positive_stage":true,"full_4b_requires_non_price_evidence":true,"residual_error":"needs_C27_specific_bridge_or_guard"},"notes":"Drama/cinema label creates local bounces, but 180D path shows balance-sheet and operating leverage drag dominating IP headlines."}
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_PLATFORM_MINIMUM_GUARANTEE_AND_ONE_OFF_HIT_FALSE_POSITIVE_SPLIT","case_id":"C27_103_004","symbol":"160550","symbol_name":"NEW","trigger_type":"Stage3_Yellow","entry_date":"2024-02-26","entry_price":4010,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/160/160550/2024.csv","profile_path":"atlas/symbol_profiles/160/160550.json","calibration_usable":true,"forward_30d_available":true,"forward_90d_available":true,"forward_180d_available":true,"corporate_action_contaminated_180d_window":false,"mfe_30d_pct":13.97,"mae_30d_pct":-15.71,"peak_30d_date":"2024-02-26","trough_30d_date":"2024-03-27","mfe_90d_pct":13.97,"mae_90d_pct":-27.93,"peak_90d_date":"2024-02-26","trough_90d_date":"2024-06-14","mfe_180d_pct":13.97,"mae_180d_pct":-32.67,"peak_180d_date":"2024-02-26","trough_180d_date":"2024-07-12","classification":"counterexample_local_4b_watch","return_alignment_label":"one_off_film_IP_price_spike_reverts_without_monetization_stack","raw_component_score_breakdown":{"stage2_evidence":70,"stage2_actionable_bonus":2.0,"revision_proxy":42,"cross_evidence_proxy":44,"price_momentum_proxy":68,"non_price_bridge_quality":35,"current_profile_proxy_total":73},"current_calibrated_profile_stress_test":{"stage2_actionable_bonus_applies":true,"stage3_yellow_min_75":true,"stage3_green_min_87":true,"stage3_green_revision_min_55":true,"price_only_blowoff_blocks_positive_stage":true,"full_4b_requires_non_price_evidence":true,"residual_error":"needs_C27_specific_bridge_or_guard"},"notes":"The spike is a textbook local 4B watch, not a full positive: film/IP event must show downstream distribution, margin, or recurring library monetization."}
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"CONTENT_IP_GLOBAL_MONETIZATION_PLATFORM_MINIMUM_GUARANTEE_AND_ONE_OFF_HIT_FALSE_POSITIVE_SPLIT","case_id":"C27_103_005","symbol":"241840","symbol_name":"에이스토리","trigger_type":"Stage2_Actionable","entry_date":"2024-03-27","entry_price":11360,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/241/241840/2024.csv","profile_path":"atlas/symbol_profiles/241/241840.json","calibration_usable":true,"forward_30d_available":true,"forward_90d_available":true,"forward_180d_available":true,"corporate_action_contaminated_180d_window":false,"mfe_30d_pct":7.83,"mae_30d_pct":-8.01,"peak_30d_date":"2024-05-17","trough_30d_date":"2024-04-16","mfe_90d_pct":8.1,"mae_90d_pct":-24.3,"peak_90d_date":"2024-05-27","trough_90d_date":"2024-06-26","mfe_180d_pct":8.1,"mae_180d_pct":-29.05,"peak_180d_date":"2024-05-27","trough_180d_date":"2024-07-24","classification":"counterexample","return_alignment_label":"drama_IP_pipeline_label_without_distribution_cash_conversion","raw_component_score_breakdown":{"stage2_evidence":70,"stage2_actionable_bonus":2.0,"revision_proxy":42,"cross_evidence_proxy":44,"price_momentum_proxy":57,"non_price_bridge_quality":35,"current_profile_proxy_total":73},"current_calibrated_profile_stress_test":{"stage2_actionable_bonus_applies":true,"stage3_yellow_min_75":true,"stage3_green_min_87":true,"stage3_green_revision_min_55":true,"price_only_blowoff_blocks_positive_stage":true,"full_4b_requires_non_price_evidence":true,"residual_error":"needs_C27_specific_bridge_or_guard"},"notes":"A production house can rally on slate optionality, but the path says IP pipeline alone is not enough without minimum guarantee, distribution, or recurring monetization bridge."}
```

## 7. Aggregate / shadow-weight / residual contribution rows

```jsonl
{"row_type":"aggregate","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":5,"reused_case_count":0,"calibration_usable_case_count":5,"calibration_usable_trigger_count":5,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":3,"local_4b_watch_count":3,"current_profile_error_count":5,"auto_selected_coverage_gap_static_index":"C27 rows 21 -> 26 if accepted","auto_selected_coverage_gap_conversation_local":"C27 rows 21 -> 26 if accepted; still Priority 0, need 4 to reach 30"}
{"row_type":"shadow_weight","selected_round":"R8","selected_loop":103,"canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","production_scoring_changed":false,"shadow_weight_only":true,"rule_candidate":"C27_content_IP_monetization_bridge_required","suggested_effect":"raise non-price quality requirement for content/IP evidence; cap one-off hit spikes at local_4b_watch unless monetization and durability bridges exist","do_not_propose_new_weight_delta":false}
{"row_type":"residual_contribution","selected_round":"R8","selected_loop":103,"canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":["C27_content_IP_monetization_bridge_required","C27_one_off_hit_local_4B_cap","C27_platform_distribution_MG_or_segment_margin_bridge_required","C27_high_MAE_title_event_guard"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":null}
```

## 8. Deferred Coding Agent Handoff Prompt — do not execute in this research run

```text
You are the later batch coding agent for Songdaiki/stock_agent. Do not treat this Markdown as a production patch by itself. In a separate implementation session, ingest all accepted v12 residual MD files, parse the machine-readable rows, deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date, and evaluate whether the proposed C27 shadow rule should become a profile-level canonical-archetype guard.

Implementation target, if accepted after batch review:
- Add or revise a C27 canonical-archetype guard requiring content/IP monetization bridge evidence.
- Distinguish one-off title/hit/artist-event spikes from recurring platform/library/distribution monetization.
- Preserve integrated platform positives only when operating leverage or segment margin evidence confirms the bridge.
- Keep production_scoring_changed=false until the batch reviewer approves.
```

## 9. Completion state

```text
completed_round = R8
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = CONTENT_IP_GLOBAL_MONETIZATION_PLATFORM_MINIMUM_GUARANTEE_AND_ONE_OFF_HIT_FALSE_POSITIVE_SPLIT
new_independent_case_count = 5
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
calibration_usable case 수 = 5
calibration_usable trigger 수 = 5
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 3
local_4b_watch_count = 3
current_profile_error_count = 5
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C27_content_IP_monetization_bridge_required | C27_one_off_hit_local_4B_cap | C27_platform_distribution_MG_or_segment_margin_bridge_required | C27_high_MAE_title_event_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
next_recommended_archetypes = C27_CONTENT_IP_GLOBAL_MONETIZATION_second_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```
