# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only
scheduled_round = R2
scheduled_loop = 13
completed_round = R2
completed_loop = 13
next_round = R3
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE
output_file = e2r_stock_web_v12_residual_round_R2_loop_13_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_web_manifest_max_date = 2026-02-20
```

This loop adds **6** new independent cases, **3** counterexamples, and **3** residual errors for `R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`.

## 1. Current Calibrated Profile Assumption

`e2r_2_1_stock_web_calibrated_proxy` is treated as the current default. The already-applied global axes are not re-promoted. This run stress-tests whether C07 needs a more specific split between **direct HBM equipment order/customer qualification** and **price-only HBM theme beta**.

## 2. Round / Large Sector / Canonical Archetype Scope

The previous local v12 state completed `R1 / Loop 13`, so the sequential scheduler advances to `R2 / Loop 13`. R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`. The selected canonical archetype is `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`, not broad C06 memory-customer capacity and not C08 socket-customer-quality. The common mechanism is equipment order visibility plus relative strength.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show older R2 calibration files through loop 9 under broad `ai_semiconductor_electronic_components` naming, while the local v12 state now starts R2 loop 13 from the prior R1 loop 13 output. This file avoids making a new production patch and treats all selected rows as post-calibrated residual research. Same canonical archetype repetition is allowed; same `symbol + trigger_date + entry_date + evidence family` repetition is not used here.

## 4. Stock-Web OHLC Input / Price Source Validation

|source_name|source_repo_url|price_adjustment_status|min_date|max_date|tradable_row_count|raw_row_count|symbol_count|active_like_symbol_count|inactive_or_delisted_like_symbol_count|calibration_shard_root|raw_shard_root|schema_path|universe_path|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|FinanceData/marcap|https://github.com/FinanceData/marcap|raw_unadjusted_marcap|1995-05-02|2026-02-20|14354401|15214118|5414|2868|2546|atlas/ohlcv_tradable_by_symbol_year|atlas/ohlcv_raw_by_symbol_year|atlas/schema.json|atlas/universe/all_symbols.csv|

The stock-web schema defines tradable columns `d,o,h,l,c,v,a,mc,s,m`, raw row status under `atlas/ohlcv_raw_by_symbol_year`, and MFE/MAE as max-high/min-low over forward tradable rows. The manifest max date is `2026-02-20`, so all 2023/2024 representative triggers have sufficient 180D forward windows.

## 5. Historical Eligibility Gate

All representative triggers are historical, exist in the stock-web tradable shard, have at least 180 forward tradable rows, and are treated as `clean_180D_window` for this research file. The rows are for calibration research only and are not live candidate discovery.

## 6. Canonical Archetype Compression Map

|fine_archetype|canonical|rule|
|---|---|---|
|HBM_TCBONDER_ORDER_ROUTE|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|direct order/customer-quality plus relative strength can bridge earlier than late revision confirmation|
|HBM_TEST_HANDLER_QUALIFICATION_ROUTE|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|test handler qualification/order conversion is valid only with durable customer quality|
|HBM_REFLOW_DESCUM_PROCESS_ROUTE|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|package-process equipment can qualify if order-intake quality is visible|
|HBM_THEME_WITHOUT_ORDER|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|relative strength alone is capped at Stage2-Watch or blocked|
|CXL_TESTER_THEME_BETA|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|theme/news beta without customer conversion is not positive Stage2A/Green evidence|

## 7. Case Selection Summary

|case_id|symbol|company|case_type|positive_or_counterexample|best_trigger|current_profile_verdict|
|---|---|---|---|---|---|---|
|R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925|042700|한미반도체|structural_success|positive|R2L13_C07_042700_STAGE2A_20230925|current_profile_too_late|
|R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119|089030|테크윙|structural_success|positive|R2L13_C07_089030_STAGE2A_20240119|current_profile_too_late|
|R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119|031980|피에스케이홀딩스|structural_success|positive|R2L13_C07_031980_STAGE2A_20240119|current_profile_correct|
|R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213|039440|에스티아이|high_mae_success|counterexample|R2L13_C07_039440_STAGE2WATCH_20240213|current_profile_false_positive|
|R2L13_C07_YEST_PRICEONLY_BLOWOFF_20240327|122640|예스티|price_moved_without_evidence|counterexample|R2L13_C07_122640_PRICEONLY_20240327|current_profile_correct|
|R2L13_C07_NEOSEM_CXL_TESTER_THEME_20240122|253590|네오셈|failed_rerating|counterexample|R2L13_C07_253590_STAGE2WATCH_20240122|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

Positive structural successes: 3. Counterexamples / failed rerating / price-only blowoff: 3. 4B overlay rows: 4. 4C/thesis-break labels: 3. This balance is intentional: the research is not trying to prove that all HBM equipment relative strength is good. It tests when relative strength is a conveyor belt carrying confirmed order evidence, and when it is only a loud signboard with no freight behind it.

## 9. Evidence Source Map

|case_id|evidence_source|stage2|stage3|stage4b|stage4c|
|---|---|---|---|---|---|
|R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925|historical public disclosure/news proxy + stock-web 042700 tradable shard|public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route|confirmed_revision, durable_customer_confirmation, repeat_order_or_conversion, financial_visibility|valuation_blowoff, positioning_overheat||
|R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119|historical public disclosure/news proxy + stock-web 089030 tradable shard|customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal|confirmed_revision, durable_customer_confirmation, financial_visibility|valuation_blowoff, positioning_overheat||
|R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119|historical public disclosure/news proxy + stock-web 031980 tradable shard|customer_or_order_quality, relative_strength, capacity_or_volume_route|margin_bridge, financial_visibility, multiple_public_sources|valuation_blowoff, positioning_overheat||
|R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213|historical public theme/news proxy + stock-web 039440 tradable shard|relative_strength, capacity_or_volume_route|multiple_public_sources|price_only_local_peak, positioning_overheat|thesis_evidence_broken|
|R2L13_C07_YEST_PRICEONLY_BLOWOFF_20240327|historical public theme/news proxy + stock-web 122640 tradable shard|relative_strength||price_only_local_peak, positioning_overheat|thesis_evidence_broken|
|R2L13_C07_NEOSEM_CXL_TESTER_THEME_20240122|historical public theme/news proxy + stock-web 253590 tradable shard|relative_strength, public_event_or_disclosure||price_only_local_peak, positioning_overheat|thesis_evidence_broken|

## 10. Price Data Source Map

|symbol|company|price_shard_path|profile_path|entry_date|entry_price|corporate_action_window_status|
|---|---|---|---|---|---|---|
|042700|한미반도체|atlas/ohlcv_tradable_by_symbol_year/042/042700/2023.csv|atlas/symbol_profiles/042/042700.json|2023-09-25|49800|clean_180D_window|
|089030|테크윙|atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv|atlas/symbol_profiles/089/089030.json|2024-01-19|14600|clean_180D_window|
|031980|피에스케이홀딩스|atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv|atlas/symbol_profiles/031/031980.json|2024-01-19|27250|clean_180D_window|
|039440|에스티아이|atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv|atlas/symbol_profiles/039/039440.json|2024-02-13|33650|clean_180D_window|
|122640|예스티|atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv|atlas/symbol_profiles/122/122640.json|2024-03-27|28350|clean_180D_window|
|253590|네오셈|atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv|atlas/symbol_profiles/253/253590.json|2024-01-22|14270|clean_180D_window|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company|trigger_type|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|verdict|aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R2L13_C07_042700_STAGE2A_20230925|042700|한미반도체|Stage2-Actionable|2023-09-25|49800|68.67|-2.41|294.0|-2.41|current_profile_too_late|representative|
|R2L13_C07_089030_STAGE2A_20240119|089030|테크윙|Stage2-Actionable|2024-01-19|14600|279.45|-11.71|384.93|-11.71|current_profile_too_late|representative|
|R2L13_C07_031980_STAGE2A_20240119|031980|피에스케이홀딩스|Stage2-Actionable|2024-01-19|27250|116.51|-5.69|213.03|-5.69|current_profile_correct|representative|
|R2L13_C07_039440_STAGE2WATCH_20240213|039440|에스티아이|Stage2|2024-02-13|33650|28.53|-7.58|28.53|-40.56|current_profile_false_positive|representative|
|R2L13_C07_122640_PRICEONLY_20240327|122640|예스티|price_moved_without_evidence|2024-03-27|28350|5.47|-39.47|5.47|-39.47|current_profile_correct|representative|
|R2L13_C07_253590_STAGE2WATCH_20240122|253590|네오셈|Stage2|2024-01-22|14270|20.18|-37.84|20.18|-37.84|current_profile_false_positive|representative|
|R2L13_C07_042700_4B_20240614|042700|한미반도체|Stage4B|2024-06-14|179900|9.06|-41.34|9.06|-41.34|current_profile_correct|4B_overlay_only|
|R2L13_C07_089030_4B_20240711|089030|테크윙|Stage4B|2024-07-11|68700|3.06|-57.63|3.06|-57.63|current_profile_correct|4B_overlay_only|
|R2L13_C07_031980_4B_20240619|031980|피에스케이홀딩스|Stage4B|2024-06-19|76500|11.5|-49.67|11.5|-49.67|current_profile_correct|4B_overlay_only|
|R2L13_C07_039440_4B_20240313|039440|에스티아이|Stage4B|2024-03-13|38750|11.61|-19.74|11.61|-48.39|current_profile_correct|4B_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R2L13_C07_042700_STAGE2A_20230925|2023-09-25|49800|33.53|68.67|294.0|-2.41|-2.41|-2.41|2024-06-14|196200|-41.34|
|R2L13_C07_089030_STAGE2A_20240119|2024-01-19|14600|63.36|279.45|384.93|-11.71|-11.71|-11.71|2024-07-11|70800|-57.63|
|R2L13_C07_031980_STAGE2A_20240119|2024-01-19|27250|58.9|116.51|213.03|-5.69|-5.69|-5.69|2024-06-19|85300|-54.86|
|R2L13_C07_039440_STAGE2WATCH_20240213|2024-02-13|33650|28.53|28.53|28.53|-6.09|-7.58|-40.56|2024-03-13|43250|-53.76|
|R2L13_C07_122640_PRICEONLY_20240327|2024-03-27|28350|5.47|5.47|5.47|-35.06|-39.47|-39.47|2024-03-27|29900|-42.61|
|R2L13_C07_253590_STAGE2WATCH_20240122|2024-01-22|14270|8.97|20.18|20.18|-37.84|-37.84|-37.84|2024-03-07|17150|-47.2|
|R2L13_C07_042700_4B_20240614|2024-06-14|179900|9.06|9.06|9.06|-26.57|-41.34|-41.34|2024-06-14|196200|-41.34|
|R2L13_C07_089030_4B_20240711|2024-07-11|68700|3.06|3.06|3.06|-43.81|-57.63|-57.63|2024-07-11|70800|-57.63|
|R2L13_C07_031980_4B_20240619|2024-06-19|76500|11.5|11.5|11.5|-31.11|-49.67|-49.67|2024-06-19|85300|-54.86|
|R2L13_C07_039440_4B_20240313|2024-03-13|38750|11.61|11.61|11.61|-19.74|-19.74|-48.39|2024-03-13|43250|-53.76|

## 13. Current Calibrated Profile Stress Test

The current calibrated profile is directionally useful: it already blocks pure price-only blowoff from becoming a positive Stage3 signal. The residual error is subtler. In C07, some direct-order winners are still too late because the model waits for broad revision confirmation. At the same time, HBM equipment theme names with only relative strength can be over-scored if the profile does not require customer/order quality.

|case_id|P0_verdict|stage2_bonus|yellow_75|green_87_revision_55|price_only_blowoff|full_4B_non_price|hard_4C|
|---|---|---|---|---|---|---|---|
|R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925|current_profile_too_late|kept but order-gated|kept|strengthened with direct-order bridge|kept|kept|kept|
|R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119|current_profile_too_late|kept but order-gated|kept|strengthened with qualification bridge|kept|kept|kept|
|R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119|current_profile_correct|kept but order-gated|kept|kept with package-process visibility|kept|kept|kept|
|R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213|current_profile_false_positive|too generous without customer bridge|too low for theme beta|weakened for unsupported theme|strengthened|kept|kept|
|R2L13_C07_YEST_PRICEONLY_BLOWOFF_20240327|current_profile_correct|not applicable|kept|kept|strengthened|kept|kept|
|R2L13_C07_NEOSEM_CXL_TESTER_THEME_20240122|current_profile_false_positive|too generous for theme beta|too low for tester theme without customer evidence|weakened for unsupported theme|strengthened|kept|kept|

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable is useful in C07 only when the trigger contains a non-price bridge: named customer/order quality, qualification route, or package-process capacity/order-intake evidence. Stage3-Green can be allowed before full consensus revision when this bridge is unusually direct. Conversely, price-only HBM beta should remain below Stage2A/Green even when the first 10~30D price path looks strong.

Green lateness ratios are applicable to the three positives: Hanmi `0.18`, Techwing `0.22`, PSK Holdings `0.31`. The counterexamples are `not_applicable` because they should not receive confirmed Green from the observed trigger.

## 15. 4B Local vs Full-window Timing Audit

|trigger_id|four_b_local_peak_proximity|four_b_full_window_peak_proximity|four_b_timing_verdict|four_b_evidence_type|
|---|---|---|---|---|
|R2L13_C07_042700_4B_20240614|0.94|0.94|good_full_window_4B_timing|valuation_blowoff, positioning_overheat, revision_slowdown_watch|
|R2L13_C07_089030_4B_20240711|0.96|0.96|good_full_window_4B_timing|valuation_blowoff, positioning_overheat|
|R2L13_C07_031980_4B_20240619|0.88|0.88|good_full_window_4B_timing_if_revision_slowdown_visible|valuation_blowoff, positioning_overheat, revision_slowdown_watch|
|R2L13_C07_039440_4B_20240313|0.90|0.90|good_4B_for_theme_without_order_conversion|price_only, valuation_blowoff, positioning_overheat|
|R2L13_C07_122640_PRICEONLY_20240327|1.00|1.00|price_only_local_4B_too_early_and_not_positive_stage|price_only, positioning_overheat|

## 16. 4C Protection Audit

Hard 4C is not proposed for direct-order structural winners. For STI/YEST/NEOSEM, 4C is not a same-day label; it becomes relevant after the thesis fails to convert and the drawdown from local peak becomes evidence of a broken rerating route. The proposed guard is: do not label 4C merely from a volatility break, but use 4C when order/customer evidence remains absent after the price-only local peak fails.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = false`. This sample is all within R2 and all within C07, so it should not become a broad L2 rule for every AI/semiconductor archetype. C06 memory-capacity and C08 socket-customer-quality need their own checks.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

Proposed C07 shadow rule:

```text
if canonical_archetype_id == C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH:
    Stage2A/Green promotion requires:
        customer_quality_score >= 70
        OR order_intake_quality_score >= 70
        OR direct_equipment_qualification_route == true
    and relative_strength_score >= 70

    if relative_strength_score is high but customer/order evidence is missing:
        cap at Stage2-Watch
        block Stage3-Green

    if post-rerating valuation/positioning expands and non-price slowdown/overheat evidence exists:
        allow 4B overlay
        do not treat 4B as thesis break unless order/customer evidence breaks
```

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|changed_thresholds|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|Existing profile catches broad Stage2 bonus and price-only blowoff, but still treats some HBM equipment relative strength too uniformly.|none|none|6|6|85.0|-17.95|151.0|-23.61|2/6|2|2|0.24|0.93|0.93|mixed; strong positives work but theme names still over-score|
|P0b_e2r_2_0_baseline_reference|rollback_reference|Older baseline over-promotes relative strength in all AI/HBM equipment names and is later on direct-order positives.|rollback reference only|older baseline|6|6|85.0|-17.95|151.0|-23.61|3/6|3|3|0.46|0.93|0.93|worse on counterexamples and late on winners|
|P1_L2_HBM_equipment_sector_shadow_profile|sector_specific|L2 HBM equipment names need order-intake/customer-quality gate before relative strength becomes Stage2A/Green.|customer_quality_gate + order_intake_quality + price_only_theme_penalty|Stage2A requires customer/order-quality OR durable equipment qualification route|6|6|119.1|-6.6|296.99|-6.6|0/6 after guard|0|0|0.24|0.93|0.93|improved, but still sector-limited evidence set|
|P2_C07_order_relative_strength_archetype_shadow_profile|canonical_archetype_specific|C07 should compress TC-bonder/test-handler/reflow cases into direct-order + relative-strength rule, while blocking price-only HBM beta.|direct_order_customer_quality_gate + relative_strength_confirmation + overheat overlay|Green allowed at 87 when order/customer-quality bridge substitutes for late revision confirmation|6|6|119.1|-6.6|296.99|-6.6|0/6 after guard|0|0|0.24|0.93|0.93|best candidate; explains positive/counterexample split|
|P3_C07_counterexample_guard_profile|guard_profile|Theme-only HBM/CXL/tester relative strength remains Stage2-Watch/Blocked until non-price evidence appears.|price_only_HBM_theme_block + customer_quality_min|Stage2A forbidden when customer_quality_score<40 and order_intake_quality unsupported|6|6|14.49|-28.63|18.06|-39.3|0/3 counterexamples promoted|0|0|not_applicable|1.0|1.0|protects against high-MAE false positives|

## 20. Score-Return Alignment Matrix

|case_id|P0_score|P0_label|P2_score|P2_label|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|
|R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925|84|Stage3-Yellow+|91|Stage3-Green|68.67|-2.41|positive promoted earlier|
|R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119|79|Stage3-Yellow|89|Stage3-Green|279.45|-11.71|positive promoted earlier|
|R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119|77|Stage3-Yellow|87|Stage3-Green|116.51|-5.69|positive promoted at threshold|
|R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213|76|Stage3-Yellow|68|Stage2-Watch|28.53|-7.58|counterexample capped before 180D drawdown|
|R2L13_C07_YEST_PRICEONLY_BLOWOFF_20240327|66|Stage2-Watch|49|Blocked-PriceOnly|5.47|-39.47|price-only blowoff blocked|
|R2L13_C07_NEOSEM_CXL_TESTER_THEME_20240122|70|Stage2-Actionable?|55|Stage2-Watch/Blocked|20.18|-37.84|theme beta capped|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L2_AI_SEMICONDUCTOR_ELECTRONICS|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE|3|3|4|3|6|0|10|6|3|false|true|C07 initial v12 loop-13 coverage filled; C06/HBM memory customer-capacity and C08/test-socket customer quality remain separate follow-up candidates|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - direct_order_green_late
  - theme_relative_strength_false_positive
  - 4B_after_price_only_local_peak
new_axis_proposed:
  - C07_direct_order_customer_quality_gate
  - C07_price_only_HBM_theme_block
  - C07_4B_after_rerating_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated scope:

```text
- historical trigger-level calibration only
- R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS only
- C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH only
- stock-web tradable_raw OHLC basis
- 30D / 90D / 180D MFE and MAE
- positive vs counterexample balance
- 4B local vs full-window split
```

Non-validation scope:

```text
- not a current/live candidate scan
- not an investment recommendation
- not a stock_agent code patch
- not a production scoring change
- not a brokerage/API automation design
- not a global rule promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_direct_order_customer_quality_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Direct HBM equipment orders/qualification deserve earlier Green bridge than generic revision-only Green.","raises positives while keeping counterexamples capped",R2L13_C07_042700_STAGE2A_20230925|R2L13_C07_089030_STAGE2A_20240119|R2L13_C07_031980_STAGE2A_20240119,6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C07_price_only_HBM_theme_block,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Relative strength alone in HBM equipment/tester names should not promote Stage2A/Green without customer/order quality.","blocks YEST/NEOSEM/STI false-positive promotion",R2L13_C07_039440_STAGE2WATCH_20240213|R2L13_C07_122640_PRICEONLY_20240327|R2L13_C07_253590_STAGE2WATCH_20240122,6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C07_4B_after_rerating_overlay,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"HBM equipment winners often need 4B overlay after valuation/positioning expansion even when thesis remains intact.","improves exit/risk overlay without changing positive entry rule",R2L13_C07_042700_4B_20240614|R2L13_C07_089030_4B_20240711|R2L13_C07_031980_4B_20240619|R2L13_C07_039440_4B_20240313,4,0,2,low,canonical_shadow_only,"4B overlay only; not entry calibration"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L13_C07_042700_STAGE2A_20230925","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive promoted","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"direct HBM TC bonder/customer order route converted into a long MFE window; P0 was not wrong directionally, but the Green label was late without a C07 direct-order bridge."}
{"row_type":"case","case_id":"R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119","symbol":"089030","company_name":"테크윙","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L13_C07_089030_STAGE2A_20240119","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive promoted","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"HBM test-handler evidence plus relative strength created a large 90D/180D MFE before full revision confirmation."}
{"row_type":"case","case_id":"R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L13_C07_031980_STAGE2A_20240119","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive promoted","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM-adjacent reflow/descum equipment route worked when price strength was paired with order-intake and package-process visibility."}
{"row_type":"case","case_id":"R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R2L13_C07_039440_STAGE2WATCH_20240213","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample capped/guarded","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"HBM reflow theme strength had a tradable local move, but insufficient customer/order conversion exposed a large 180D MAE."}
{"row_type":"case","case_id":"R2L13_C07_YEST_PRICEONLY_BLOWOFF_20240327","symbol":"122640","company_name":"예스티","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R2L13_C07_122640_PRICEONLY_20240327","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample capped/guarded","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"late price-only HBM equipment spike behaved as 4B overlay, not positive Stage2/3 evidence."}
{"row_type":"case","case_id":"R2L13_C07_NEOSEM_CXL_TESTER_THEME_20240122","symbol":"253590","company_name":"네오셈","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R2L13_C07_253590_STAGE2WATCH_20240122","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample capped/guarded","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"tester/CXL/HBM theme beta moved first, then suffered high MAE before durable order evidence could carry the score."}
{"row_type":"trigger","trigger_id":"R2L13_C07_042700_STAGE2A_20230925","case_id":"R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-25","evidence_available_at_that_date":"named customer/order-quality + TC-bonder route + relative strength","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","durable_customer_confirmation","repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2023.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-25","entry_price":49800,"MFE_30D_pct":33.53,"MFE_90D_pct":68.67,"MFE_180D_pct":294.0,"MFE_1Y_pct":294.0,"MFE_2Y_pct":null,"MAE_30D_pct":-2.41,"MAE_90D_pct":-2.41,"MAE_180D_pct":-2.41,"MAE_1Y_pct":-2.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-41.34,"green_lateness_ratio":"0.18","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925_2023-09-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C07_089030_STAGE2A_20240119","case_id":"R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119","symbol":"089030","company_name":"테크윙","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-19","evidence_available_at_that_date":"HBM test-handler order/qualification route + relative strength","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","durable_customer_confirmation","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-19","entry_price":14600,"MFE_30D_pct":63.36,"MFE_90D_pct":279.45,"MFE_180D_pct":384.93,"MFE_1Y_pct":384.93,"MFE_2Y_pct":null,"MAE_30D_pct":-11.71,"MAE_90D_pct":-11.71,"MAE_180D_pct":-11.71,"MAE_1Y_pct":-11.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":"0.22","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119_2024-01-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C07_031980_STAGE2A_20240119","case_id":"R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-19","evidence_available_at_that_date":"HBM package-process equipment route + order-intake quality + relative strength","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","profile_path":"atlas/symbol_profiles/031/031980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-19","entry_price":27250,"MFE_30D_pct":58.9,"MFE_90D_pct":116.51,"MFE_180D_pct":213.03,"MFE_1Y_pct":213.03,"MFE_2Y_pct":null,"MAE_30D_pct":-5.69,"MAE_90D_pct":-5.69,"MAE_180D_pct":-5.69,"MAE_1Y_pct":-5.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":85300,"drawdown_after_peak_pct":-54.86,"green_lateness_ratio":"0.31","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119_2024-01-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C07_039440_STAGE2WATCH_20240213","case_id":"R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-02-13","evidence_available_at_that_date":"HBM reflow theme + relative strength, but no durable customer/order bridge at trigger","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv","profile_path":"atlas/symbol_profiles/039/039440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-13","entry_price":33650,"MFE_30D_pct":28.53,"MFE_90D_pct":28.53,"MFE_180D_pct":28.53,"MFE_1Y_pct":28.53,"MFE_2Y_pct":null,"MAE_30D_pct":-6.09,"MAE_90D_pct":-7.58,"MAE_180D_pct":-40.56,"MAE_1Y_pct":-40.56,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":43250,"drawdown_after_peak_pct":-53.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_4B_too_early_without_customer_conversion","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213_2024-02-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C07_122640_PRICEONLY_20240327","case_id":"R2L13_C07_YEST_PRICEONLY_BLOWOFF_20240327","symbol":"122640","company_name":"예스티","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"price_moved_without_evidence","trigger_date":"2024-03-27","evidence_available_at_that_date":"late HBM-equipment price spike without enough order/revision support","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv","profile_path":"atlas/symbol_profiles/122/122640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-27","entry_price":28350,"MFE_30D_pct":5.47,"MFE_90D_pct":5.47,"MFE_180D_pct":5.47,"MFE_1Y_pct":5.47,"MFE_2Y_pct":null,"MAE_30D_pct":-35.06,"MAE_90D_pct":-39.47,"MAE_180D_pct":-39.47,"MAE_1Y_pct":-39.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":29900,"drawdown_after_peak_pct":-42.61,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_and_not_positive_stage","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_YEST_PRICEONLY_BLOWOFF_20240327_2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C07_253590_STAGE2WATCH_20240122","case_id":"R2L13_C07_NEOSEM_CXL_TESTER_THEME_20240122","symbol":"253590","company_name":"네오셈","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-01-22","evidence_available_at_that_date":"tester/CXL/HBM theme strength with weak customer/order-quality confirmation","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv","profile_path":"atlas/symbol_profiles/253/253590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-22","entry_price":14270,"MFE_30D_pct":8.97,"MFE_90D_pct":20.18,"MFE_180D_pct":20.18,"MFE_1Y_pct":20.18,"MFE_2Y_pct":null,"MAE_30D_pct":-37.84,"MAE_90D_pct":-37.84,"MAE_180D_pct":-37.84,"MAE_1Y_pct":-37.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":17150,"drawdown_after_peak_pct":-47.2,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_and_theme_strength_needs_customer_quality_gate","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_NEOSEM_CXL_TESTER_THEME_20240122_2024-01-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L13_C07_042700_4B_20240614","case_id":"R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-14","evidence_available_at_that_date":"valuation blowoff and positioning overheat after positive thesis","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","durable_customer_confirmation","repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","revision_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-14","entry_price":179900,"MFE_30D_pct":9.06,"MFE_90D_pct":9.06,"MFE_180D_pct":9.06,"MFE_1Y_pct":9.06,"MFE_2Y_pct":null,"MAE_30D_pct":-26.57,"MAE_90D_pct":-41.34,"MAE_180D_pct":-41.34,"MAE_1Y_pct":-41.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-41.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925_2024-06-14","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R2L13_C07_089030_4B_20240711","case_id":"R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119","symbol":"089030","company_name":"테크윙","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-07-11","evidence_available_at_that_date":"post-rerating valuation/positioning overlay","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","durable_customer_confirmation","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-11","entry_price":68700,"MFE_30D_pct":3.06,"MFE_90D_pct":3.06,"MFE_180D_pct":3.06,"MFE_1Y_pct":3.06,"MFE_2Y_pct":null,"MAE_30D_pct":-43.81,"MAE_90D_pct":-57.63,"MAE_180D_pct":-57.63,"MAE_1Y_pct":-57.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119_2024-07-11","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R2L13_C07_031980_4B_20240619","case_id":"R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-19","evidence_available_at_that_date":"local/full-window high after order-repricing move","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","revision_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","profile_path":"atlas/symbol_profiles/031/031980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-19","entry_price":76500,"MFE_30D_pct":11.5,"MFE_90D_pct":11.5,"MFE_180D_pct":11.5,"MFE_1Y_pct":11.5,"MFE_2Y_pct":null,"MAE_30D_pct":-31.11,"MAE_90D_pct":-49.67,"MAE_180D_pct":-49.67,"MAE_1Y_pct":-49.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":85300,"drawdown_after_peak_pct":-54.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"good_full_window_4B_timing_if_revision_slowdown_visible","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119_2024-06-19","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R2L13_C07_039440_4B_20240313","case_id":"R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_TCBONDER_ORDER_ROUTE","sector":"AI·반도체·전자부품","primary_archetype":"HBM equipment order and relative strength","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-03-13","evidence_available_at_that_date":"theme rerating local peak without enough conversion evidence","evidence_source":"historical public disclosure/news proxy + Songdaiki/stock-web tradable shard","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv","profile_path":"atlas/symbol_profiles/039/039440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-13","entry_price":38750,"MFE_30D_pct":11.61,"MFE_90D_pct":11.61,"MFE_180D_pct":11.61,"MFE_1Y_pct":11.61,"MFE_2Y_pct":null,"MAE_30D_pct":-19.74,"MAE_90D_pct":-19.74,"MAE_180D_pct":-48.39,"MAE_1Y_pct":-48.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":43250,"drawdown_after_peak_pct":-53.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_4B_for_theme_without_order_conversion","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213_2024-03-13","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"R2L13_C07_HANMI_TCBONDER_DIRECT_ORDER_20230925","trigger_id":"R2L13_C07_042700_STAGE2A_20230925","symbol":"042700","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":72,"backlog_visibility_score":65,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":90,"customer_quality_score":88,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow+","raw_component_scores_after":{"contract_score":82,"backlog_visibility_score":78,"margin_bridge_score":65,"revision_score":62,"relative_strength_score":90,"customer_quality_score":92,"policy_or_regulatory_score":0,"valuation_repricing_score":75,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","order_intake_quality_score","price_only_hbm_theme_penalty","relative_strength_confirmation_gate"],"component_delta_explanation":"C07 shadow separates direct HBM equipment order/customer qualification from price-only HBM beta.","MFE_90D_pct":68.67,"MAE_90D_pct":-2.41,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"R2L13_C07_TECHWING_HBM_TEST_HANDLER_20240119","trigger_id":"R2L13_C07_089030_STAGE2A_20240119","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":48,"relative_strength_score":92,"customer_quality_score":75,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":68,"margin_bridge_score":58,"revision_score":60,"relative_strength_score":95,"customer_quality_score":84,"policy_or_regulatory_score":0,"valuation_repricing_score":72,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","order_intake_quality_score","price_only_hbm_theme_penalty","relative_strength_confirmation_gate"],"component_delta_explanation":"C07 shadow separates direct HBM equipment order/customer qualification from price-only HBM beta.","MFE_90D_pct":279.45,"MAE_90D_pct":-11.71,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"R2L13_C07_PSKHOLDINGS_REFLOW_ROUTE_20240119","trigger_id":"R2L13_C07_031980_STAGE2A_20240119","symbol":"031980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":48,"margin_bridge_score":55,"revision_score":48,"relative_strength_score":88,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":66,"margin_bridge_score":65,"revision_score":58,"relative_strength_score":90,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":87,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","order_intake_quality_score","price_only_hbm_theme_penalty","relative_strength_confirmation_gate"],"component_delta_explanation":"C07 shadow separates direct HBM equipment order/customer qualification from price-only HBM beta.","MFE_90D_pct":116.51,"MAE_90D_pct":-5.69,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"R2L13_C07_STI_REFLOW_THEME_HIGH_MAE_20240213","trigger_id":"R2L13_C07_039440_STAGE2WATCH_20240213","symbol":"039440","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":40,"revision_score":35,"relative_strength_score":85,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":35,"revision_score":35,"relative_strength_score":75,"customer_quality_score":38,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Watch","changed_components":["customer_quality_score","order_intake_quality_score","price_only_hbm_theme_penalty","relative_strength_confirmation_gate"],"component_delta_explanation":"C07 shadow separates direct HBM equipment order/customer qualification from price-only HBM beta.","MFE_90D_pct":28.53,"MAE_90D_pct":-7.58,"score_return_alignment_label":"counterexample_guarded","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"R2L13_C07_YEST_PRICEONLY_BLOWOFF_20240327","trigger_id":"R2L13_C07_122640_PRICEONLY_20240327","symbol":"122640","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":88,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":78,"execution_risk_score":-5,"legal_or_contract_risk_score":-10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":15,"relative_strength_score":45,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":-20,"legal_or_contract_risk_score":-15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Blocked-PriceOnly","changed_components":["customer_quality_score","order_intake_quality_score","price_only_hbm_theme_penalty","relative_strength_confirmation_gate"],"component_delta_explanation":"C07 shadow separates direct HBM equipment order/customer qualification from price-only HBM beta.","MFE_90D_pct":5.47,"MAE_90D_pct":-39.47,"score_return_alignment_label":"counterexample_guarded","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","case_id":"R2L13_C07_NEOSEM_CXL_TESTER_THEME_20240122","trigger_id":"R2L13_C07_253590_STAGE2WATCH_20240122","symbol":"253590","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":20,"margin_bridge_score":30,"revision_score":25,"relative_strength_score":92,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":74,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable?","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":18,"margin_bridge_score":26,"revision_score":22,"relative_strength_score":58,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":48,"execution_risk_score":-25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage2-Watch/Blocked","changed_components":["customer_quality_score","order_intake_quality_score","price_only_hbm_theme_penalty","relative_strength_confirmation_gate"],"component_delta_explanation":"C07 shadow separates direct HBM equipment order/customer qualification from price-only HBM beta.","MFE_90D_pct":20.18,"MAE_90D_pct":-37.84,"score_return_alignment_label":"counterexample_guarded","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"13","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","scheduled_round":"R2","scheduled_loop":"13","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":3,"counterexample_count":3,"current_profile_error_count":3,"diversity_score_summary":"six R2/C07 symbols, direct-order positives balanced against price-only/HBM-theme counterexamples","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["direct_order_green_late","theme_relative_strength_false_positive","4B_after_price_only_local_peak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 13
next_round = R3
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json` from `Songdaiki/stock-web`, max date `2026-02-20`, raw/unadjusted marcap basis.
- Stock-Web schema: `atlas/schema.json`, tradable columns `d,o,h,l,c,v,a,mc,s,m`, MFE/MAE definition over forward tradable rows.
- Price shards used: `042700/2023`, `042700/2024`, `089030/2024`, `031980/2024`, `039440/2024`, `122640/2024`, `253590/2024`.
- Evidence labels are historical public-disclosure/news proxies used only for trigger classification; price metrics are from stock-web tradable OHLC rows.

