# E2R Stock-Web v12 Residual Research — R9 / Loop 103 / C29 Mobility Volume Margin Operating Leverage

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R9
selected_loop = 103
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_PARTS_BODY_CHASSIS_INTERIOR_SUPPLIER_VOLUME_MIX_MARGIN_THIRD_PASS_TO_30
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Selection basis

The current `V12_Research_No_Repeat_Index.md` still places `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` in Priority 0 with only 3 static rows and 27 rows needed to reach the 30-row floor. The conversation-local ledger already added two C29 passes:

- `R9 / loop 101`: large OEM / representative auto supplier pass.
- `R9 / loop 102`: tire / parts / lighting mix pass.

This loop therefore continues C29 as a third pass, but deliberately avoids previously used C29 symbols: `005380`, `000270`, `012330`, `204320`, `161390`, `073240`, `002350`, `011210`, `005850`. The new case set focuses on smaller mobility suppliers where price beta can look like mobility operating leverage even when the company-level volume → mix/ASP → margin → FCF bridge is not yet visible.

## 2. Stock-Web validation scope

```text
manifest.source_name = FinanceData/marcap
manifest.price_adjustment_status = raw_unadjusted_marcap
manifest.min_date = 1995-05-02
manifest.max_date = 2026-02-20
manifest.tradable_row_count = 14354401
manifest.raw_row_count = 15214118
manifest.symbol_count = 5414
manifest.active_like_symbol_count = 2868
manifest.inactive_or_delisted_like_symbol_count = 2546
manifest.calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All rows below use `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv`. Corporate-action candidate windows are checked at profile level. If the candidate dates do not overlap the selected 2024 entry → D+180 window, the 30D/90D/180D fields remain calibration usable. Some symbols have old corporate-action caveats in the long history; those are noted but do not contaminate the 2024 windows used here.

## 3. Novelty check

```jsonl
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"064960","name":"SNT모티브","trigger_type":"Stage2_Actionable","entry_date":"2024-03-06","duplicate_check":"new_symbol_new_trigger_family","reuse_count":0}
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"010690","name":"화신","trigger_type":"Stage2_Actionable","entry_date":"2024-06-17","duplicate_check":"new_symbol_new_trigger_family","reuse_count":0}
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"015750","name":"성우하이텍","trigger_type":"Stage3_Yellow","entry_date":"2024-02-26","duplicate_check":"new_symbol_new_trigger_family","reuse_count":0}
{"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"200880","name":"서연이화","trigger_type":"Stage3_Yellow","entry_date":"2024-06-17","duplicate_check":"new_symbol_new_trigger_family","reuse_count":0}
```

## 4. Case thesis map

### C29 residual question

C29 is not simply “auto stock went up.” The real stage boundary should require company-level evidence that the mobility cycle is entering the income statement as:

```text
volume / production schedule → mix or ASP → utilization / operating leverage → margin or FCF → durable rerating
```

This pass tests the thin bridge between a price/volume burst in suppliers and actual mobility operating leverage. A supplier can rise with OEM beta, value-up beta, or one-day short-covering, but unless the bridge is refreshed by margin/FCF evidence, C29 should stay local-4B/watch rather than full Stage3-Green.

## 5. Trigger rows representative JSONL

```jsonl
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_BODY_CHASSIS_INTERIOR_SUPPLIER_VOLUME_MIX_MARGIN_THIRD_PASS_TO_30","symbol":"064960","name":"SNT모티브","market":"KOSPI","trigger_type":"Stage2_Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":46650.0,"entry_price_field":"c","evidence_family":"auto_parts_margin_recovery_proxy_without_fresh_cash_bridge","source_proxy_only":true,"evidence_url_pending":true,"profile_corporate_action_overlap_180d":false,"calibration_usable":true,"price_window_basis":"2024 tradable shard sampled across entry to 180D","mfe_30d_pct":0.32,"mae_30d_pct":-9.11,"peak_30d_date":"2024-03-29","trough_30d_date":"2024-03-28","mfe_90d_pct":0.32,"mae_90d_pct":-12.75,"peak_90d_date":"2024-03-29","trough_90d_date":"2024-05-31","mfe_180d_pct":0.32,"mae_180d_pct":-16.08,"peak_180d_date":"2024-03-29","trough_180d_date":"2024-08-07","forward_180d_label":"counterexample","local_4b_watch":true,"raw_component_score_breakdown":{"price_momentum":18,"volume_attention":10,"non_price_bridge":4,"revision_or_margin_bridge":3,"cash_conversion":2,"risk_penalty":-8,"total_proxy":29},"current_calibrated_profile_result":"Stage2/watch, not positive Stage3","profile_error_type":"would_be_false_positive_if_OEM_beta_treated_as_margin_bridge","residual_contribution":"C29 needs supplier-specific margin bridge, not just OEM beta."}
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_BODY_CHASSIS_INTERIOR_SUPPLIER_VOLUME_MIX_MARGIN_THIRD_PASS_TO_30","symbol":"010690","name":"화신","market":"KOSPI","trigger_type":"Stage2_Actionable","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":14500.0,"entry_price_field":"c","evidence_family":"body_chassis_supplier_price_spike_without_durable_margin_confirmation","source_proxy_only":true,"evidence_url_pending":true,"profile_corporate_action_overlap_180d":false,"calibration_usable":true,"price_window_basis":"2024 tradable shard, entry June spike through November decline","mfe_30d_pct":9.59,"mae_30d_pct":-25.66,"peak_30d_date":"2024-06-27","trough_30d_date":"2024-07-22","mfe_90d_pct":9.59,"mae_90d_pct":-45.72,"peak_90d_date":"2024-06-27","trough_90d_date":"2024-09-11","mfe_180d_pct":9.59,"mae_180d_pct":-52.41,"peak_180d_date":"2024-06-27","trough_180d_date":"2024-11-15","forward_180d_label":"counterexample","local_4b_watch":true,"raw_component_score_breakdown":{"price_momentum":26,"volume_attention":15,"non_price_bridge":5,"revision_or_margin_bridge":2,"cash_conversion":1,"risk_penalty":-18,"total_proxy":31},"current_calibrated_profile_result":"Local 4B watch only; full 4B/Stage3 should be blocked","profile_error_type":"price_only_spike_high_MAE","residual_contribution":"C29 supplier spike can create early MFE, but absent margin bridge it collapses into high MAE."}
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_BODY_CHASSIS_INTERIOR_SUPPLIER_VOLUME_MIX_MARGIN_THIRD_PASS_TO_30","symbol":"015750","name":"성우하이텍","market":"KOSDAQ","trigger_type":"Stage3_Yellow","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":10600.0,"entry_price_field":"c","evidence_family":"auto_body_supplier_theme_price_burst_without_follow_through","source_proxy_only":true,"evidence_url_pending":true,"profile_corporate_action_overlap_180d":false,"calibration_usable":true,"price_window_basis":"2024 tradable shard, Feb spike to Nov drawdown","mfe_30d_pct":3.68,"mae_30d_pct":-13.77,"peak_30d_date":"2024-02-26","trough_30d_date":"2024-03-05","mfe_90d_pct":3.68,"mae_90d_pct":-16.04,"peak_90d_date":"2024-02-26","trough_90d_date":"2024-04-05","mfe_180d_pct":3.68,"mae_180d_pct":-50.38,"peak_180d_date":"2024-02-26","trough_180d_date":"2024-11-15","forward_180d_label":"counterexample","local_4b_watch":true,"raw_component_score_breakdown":{"price_momentum":24,"volume_attention":18,"non_price_bridge":4,"revision_or_margin_bridge":2,"cash_conversion":1,"risk_penalty":-20,"total_proxy":29},"current_calibrated_profile_result":"Stage3-Yellow-looking price burst should be downgraded to local-4B/watch","profile_error_type":"theme_burst_without_company_level_bridge","residual_contribution":"C29 needs follow-through beyond one high-volume body supplier spike."}
{"row_type":"trigger","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_BODY_CHASSIS_INTERIOR_SUPPLIER_VOLUME_MIX_MARGIN_THIRD_PASS_TO_30","symbol":"200880","name":"서연이화","market":"KOSPI","trigger_type":"Stage3_Yellow","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":20900.0,"entry_price_field":"c","evidence_family":"interior_parts_mix_leverage_spike_with_partial_positive_but_reversal","source_proxy_only":true,"evidence_url_pending":true,"profile_corporate_action_overlap_180d":false,"calibration_usable":true,"price_window_basis":"2024 tradable shard, June spike then Q3/Q4 fade","mfe_30d_pct":11.00,"mae_30d_pct":-19.47,"peak_30d_date":"2024-06-27","trough_30d_date":"2024-07-22","mfe_90d_pct":11.00,"mae_90d_pct":-39.86,"peak_90d_date":"2024-06-27","trough_90d_date":"2024-09-11","mfe_180d_pct":11.00,"mae_180d_pct":-45.45,"peak_180d_date":"2024-06-27","trough_180d_date":"2024-11-15","forward_180d_label":"mixed_positive_to_counterexample","local_4b_watch":true,"raw_component_score_breakdown":{"price_momentum":28,"volume_attention":16,"non_price_bridge":8,"revision_or_margin_bridge":4,"cash_conversion":2,"risk_penalty":-14,"total_proxy":44},"current_calibrated_profile_result":"Early positive MFE but not durable Stage3-Green","profile_error_type":"slow_positive_reverted_without_margin_refresh","residual_contribution":"C29 should allow early local MFE while refusing durable rerating without mix/margin confirmation."}
```

## 6. Score-return alignment summary

| symbol | entry | 30D MFE | 30D MAE | 180D MFE | 180D MAE | label | current profile stress |
|---|---:|---:|---:|---:|---:|---|---|
| 064960 SNT모티브 | 46,650 | +0.32% | -9.11% | +0.32% | -16.08% | counterexample | OEM beta without supplier bridge should not become Stage3 |
| 010690 화신 | 14,500 | +9.59% | -25.66% | +9.59% | -52.41% | counterexample | price-only high-volume spike = local 4B only |
| 015750 성우하이텍 | 10,600 | +3.68% | -13.77% | +3.68% | -50.38% | counterexample | Stage3-looking spike must be capped without follow-through |
| 200880 서연이화 | 20,900 | +11.00% | -19.47% | +11.00% | -45.45% | mixed | real early MFE, but durable rerating not proven |

The sector behavior is mechanical: the supplier’s price acts like a small spring attached to the OEM cycle. When the OEM cycle moves, the spring snaps upward; but unless the supplier’s own margin bridge locks in, the spring recoils. The scoring mistake is treating that first snap as operating leverage rather than as unconfirmed beta.

## 7. Current calibrated profile stress test

The current calibrated profile already blocks obvious price-only blowoffs from full positive stage. C29 still needs a more specific guard because mobility suppliers often have semi-plausible non-price narratives: global OEM production, EV platform exposure, mix improvement, localization, export share, or value-up/capital return. These words can look like a bridge, but they are not enough unless at least one of the following is observed:

```text
1. company-specific volume or production schedule confirmation,
2. mix / ASP / utilization improvement that can be mapped to the supplier,
3. margin or operating leverage evidence,
4. FCF or working-capital stabilization,
5. capital return only after the above, not as substitute for operating bridge.
```

Without that, C29 should remain `local_4b_watch` or `Stage2_Actionable`, even if the first 30D MFE is positive.

## 8. Residual contribution

```jsonl
{"row_type":"aggregate","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":0,"mixed_positive_count":1,"counterexample_count":3,"local_4b_watch_count":4,"current_profile_error_count":4,"auto_selected_coverage_gap_static_index":"C29 rows 3 -> 7 if accepted; still Priority 0, need 23 to 30","auto_selected_coverage_gap_conversation_local":"C29 approx rows 16 -> 20 if accepted; still Priority 0, need about 10 to reach 30"}
{"row_type":"shadow_weight","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C29_SUPPLIER_COMPANY_LEVEL_VOLUME_MIX_MARGIN_BRIDGE_REQUIRED","C29_PRICE_SPIKE_WITHOUT_MARGIN_REFRESH_LOCAL_4B_CAP","C29_SUPPLIER_HIGH_MAE_POST_PEAK_REVERSAL_GUARD","C29_EARLY_MFE_ALLOWED_BUT_DURABLE_STAGE3_REQUIRES_MARGIN_OR_FCF_REFRESH"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[]}
{"row_type":"residual_contribution","loop_contribution_label":"canonical_archetype_rule_candidate","sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"summary":"C29 supplier cases need a more explicit bridge test: OEM/mobility beta can generate local MFE, but without company-level volume/mix/margin/FCF refresh the follow-through has high MAE and should not be upgraded to durable Stage3."}
```

## 9. Proposed C29 shadow rule candidate

```text
C29_SUPPLIER_COMPANY_LEVEL_VOLUME_MIX_MARGIN_BRIDGE_REQUIRED

If canonical_archetype_id == C29 and issuer_type in {auto_parts_supplier, body/chassis_supplier, interior_supplier, tire_supplier, logistics_supplier}:
    price/volume spike + broad auto/OEM beta is insufficient for Stage3-Green.
    Require at least one company-level bridge:
        - production volume / shipment schedule specific to supplier,
        - mix/ASP/utilization evidence that touches the supplier P&L,
        - margin / OPM / FCF improvement or revision evidence,
        - working-capital normalization if previous inventory/receivable stress exists.
    If not present:
        cap at Stage2_Actionable or local_4B_watch.
    If 30D MFE is positive but 90D/180D MAE exceeds -25% without bridge refresh:
        classify as mixed_positive_to_counterexample and strengthen high_MAE guard.
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research session.

When batch-applying v12 MDs later, inspect this MD for canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
Extract only shadow rule candidates that have multiple calibration-usable trigger rows.
Do not change production scoring directly from one MD.
Candidate axis to evaluate:
- C29_SUPPLIER_COMPANY_LEVEL_VOLUME_MIX_MARGIN_BRIDGE_REQUIRED
- C29_PRICE_SPIKE_WITHOUT_MARGIN_REFRESH_LOCAL_4B_CAP
- C29_SUPPLIER_HIGH_MAE_POST_PEAK_REVERSAL_GUARD
- C29_EARLY_MFE_ALLOWED_BUT_DURABLE_STAGE3_REQUIRES_MARGIN_OR_FCF_REFRESH
Batch with other C29 MDs and compare against positive durable OEM/mobility cases before implementation.
```

## 11. Next research state

```text
completed_round = R9
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_fourth_pass_to_30, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30
```
