# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 73
completed_round = R1
completed_loop = 73
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP
output_file = e2r_stock_web_v12_residual_round_R1_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove the global Stage2 bonus or Green lateness axis. It stress-tests whether C04 needs a more precise split between (1) nuclear legal de-risking with identifiable supplier/prime-equipment bridge and (2) policy-only nuclear theme spikes.

## 2. Round / Large Sector / Canonical Archetype Scope

|field|value|
|---|---|
|scheduled_round|R1|
|scheduled_loop|73|
|large_sector_id|L1_INDUSTRIALS_INFRA_DEFENSE_GRID|
|canonical_archetype_id|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|
|fine_archetype_id|NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP|
|round_sector_consistency|pass|
|loop_objective|sector_specific_rule_discovery / canonical_archetype_compression / residual_false_positive_mining / residual_missed_structural_mining / 4B_non_price_requirement_stress_test / counterexample_mining / coverage_gap_fill|

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts visible in the working set already covered R1/L1/C02 power-grid CAPEX and R11/L1 C03/C04 defense/nuclear special cases. The hard duplicate key used here is `canonical_archetype_id + symbol + trigger_type + entry_date`.

This run deliberately avoids the R1 Loop 72 C02 transformer set and does not reuse the R11 C03 defense rows. Within C04, 083650, 105840, and 011700 are new symbols. 034020 is a reused symbol but a new trigger family under C04: 2025-01-17 IP/legal dispute settlement, not the prior 2024-07-18 Czech preferred-bidder event. 006910 is included only as a holdout counterexample and is explicitly marked `do_not_count_as_new_case=true`.

|case_id|hard_duplicate_status|reuse_policy|
|---|---|---|
|R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER|new C04 symbol + new trigger|count as new|
|R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE|new C04 symbol + new trigger|count as new|
|R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY|same symbol, new C04 trigger family|count with 0.5 independent weight|
|R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF|new C04 symbol + policy-only counterexample|count as new|
|R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT|reused holdout key|do not count as new|

## 4. Stock-Web OHLC Input / Price Source Validation

The price source is `Songdaiki/stock-web`, with `tradable_raw` OHLCV shards generated from FinanceData/marcap. The manifest used for this run reports `max_date=2026-02-20`, `tradable_row_count=14354401`, `symbol_count=5414`, `active_like_symbol_count=2868`, and `price_adjustment_status=raw_unadjusted_marcap`. The schema defines tradable shard columns as `d,o,h,l,c,v,a,mc,s,m`, and the calibration rules require an existing entry row, positive OHLCV, at least 180 forward tradable days, computed MFE/MAE 30/90/180D, and no 180D corporate-action contamination.

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

|case_id|symbol|entry_date|profile_path|corporate_action_window_status|forward_window_trading_days|calibration_usable|block_reasons|
|---|---|---|---|---|---|---|---|
|R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER|083650|2025-01-17|atlas/symbol_profiles/083/083650.json|clean_180D_window|180|True|[]|
|R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE|105840|2025-01-17|atlas/symbol_profiles/105/105840.json|clean_180D_window|180|True|[]|
|R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY|034020|2025-01-17|atlas/symbol_profiles/034/034020.json|clean_180D_window|180|True|[]|
|R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF|011700|2022-03-10|atlas/symbol_profiles/011/011700.json|clean_180D_window|180|True|[]|
|R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT|006910|2022-03-10|atlas/symbol_profiles/006/006910.json|clean_180D_window|180|True|[]|

## 6. Canonical Archetype Compression Map

|source observation|C04 compression|
|---|---|
|Westinghouse/KHNP settlement|Not merely C31 policy/legal news; under C04 it is nuclear project legal-delay de-risking.|
|BHI/Woojin supplier routes|Supplier bridge receives limited Yellow support only when legal blocker clears and equipment route is identifiable.|
|Doosan prime-equipment route|Prime bridge can support stronger Stage2/Yellow, but Green still waits for revision/contract visibility.|
|Yoon election nuclear policy theme|Policy-only theme remains Stage2-watch/Actionable, not Stage3 structural.|
|HanShin/Bosung theme spikes|Large MFE can be price-only blowoff; drawdown-after-peak proves need for 4B overlay split.|

## 7. Case Selection Summary

|case_id|symbol|company|role|new_independent|current_profile_verdict|best_trigger|
|---|---|---|---|---|---|---|
|R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER|083650|비에이치아이|positive|True|current_profile_missed_structural|R1L73_T083650_20250117_STAGE2A|
|R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE|105840|우진|positive|True|current_profile_missed_structural|R1L73_T105840_20250117_STAGE2A|
|R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY|034020|두산에너빌리티|positive|True|current_profile_correct|R1L73_T034020_20250117_STAGE2A|
|R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF|011700|한신기계|counterexample|True|current_profile_false_positive|R1L73_T011700_20220310_STAGE2_THEME|
|R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT|006910|보성파워텍|counterexample|False|current_profile_false_positive|R1L73_T006910_20220310_STAGE2A_HOLDOUT|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
calibration_usable_case_count = 5
new_independent_case_count = 4
reused_case_count = 1
minimum_positive_case_count_met = true
minimum_counterexample_count_met = true
minimum_new_independent_case_ratio_met = true
```

The balance is intentional: the same nuclear-policy umbrella produced both structural winners after legal de-risking and false structural signals when the evidence stopped at election/policy headline.

## 9. Evidence Source Map

|trigger_id|evidence source|Stage2 evidence|Stage3 evidence|4B/4C evidence|
|---|---|---|---|---|
|R1L73_T083650_20250117_STAGE2A|Reuters 2025-01-17 Westinghouse-KHNP/KEPCO settlement; stock-web 083650 2025 tradable shard|public_event_or_disclosure, policy_or_regulatory_optionality, customer_or_order_quality, capacity_or_volume_route, early_revision_signal|multiple_public_sources|-|
|R1L73_T105840_20250117_STAGE2A|Reuters 2025-01-17 Westinghouse-KHNP/KEPCO settlement; stock-web 105840 2025 tradable shard|public_event_or_disclosure, policy_or_regulatory_optionality, capacity_or_volume_route, early_revision_signal|multiple_public_sources|-|
|R1L73_T034020_20250117_STAGE2A|Reuters 2025-01-17 settlement; stock-web 034020 tradable shard values as parsed in prior allowed C31 artifact|public_event_or_disclosure, policy_or_regulatory_optionality, customer_or_order_quality, backlog_or_delivery_visibility, early_revision_signal|multiple_public_sources, durable_customer_confirmation, financial_visibility|-|
|R1L73_T011700_20220310_STAGE2_THEME|Reuters/KBS/public election result context; stock-web 011700 2022 tradable shard|public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength|-|price_only_local_peak, positioning_overheat|
|R1L73_T006910_20220310_STAGE2A_HOLDOUT|prior allowed C04/C31 holdout row; stock-web 006910 profile and shard path validated|public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength|-|price_only_local_peak, positioning_overheat|
|R1L73_T011700_20220504_4B_PRICE_ONLY_OVERLAY|stock-web 011700 2022 tradable shard; overlay derived from observed local/full peak||-|price_only_local_peak, positioning_overheat|

## 10. Price Data Source Map

|symbol|company|tradable_shard|profile|price_basis|adjustment|
|---|---|---|---|---|---|
|083650|비에이치아이|atlas/ohlcv_tradable_by_symbol_year/083/083650/2025.csv|atlas/symbol_profiles/083/083650.json|tradable_raw|raw_unadjusted_marcap|
|105840|우진|atlas/ohlcv_tradable_by_symbol_year/105/105840/2025.csv|atlas/symbol_profiles/105/105840.json|tradable_raw|raw_unadjusted_marcap|
|034020|두산에너빌리티|atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv|atlas/symbol_profiles/034/034020.json|tradable_raw|raw_unadjusted_marcap|
|011700|한신기계|atlas/ohlcv_tradable_by_symbol_year/011/011700/2022.csv|atlas/symbol_profiles/011/011700.json|tradable_raw|raw_unadjusted_marcap|
|006910|보성파워텍|atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv|atlas/symbol_profiles/006/006910.json|tradable_raw|raw_unadjusted_marcap|

## 11. Case-by-Case Trigger Grid

|case_id|trigger_id|trigger_type|trigger_date|entry_date|entry_price|outcome|current_profile_verdict|
|---|---|---|---|---|---|---|---|
|R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER|R1L73_T083650_20250117_STAGE2A|Stage2-Actionable|2025-01-17|2025-01-17|18080|structural_success_high_MFE_supplier_bridge|current_profile_missed_structural|
|R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE|R1L73_T105840_20250117_STAGE2A|Stage2-Actionable|2025-01-17|2025-01-17|7450|structural_success_delayed_supplier_bridge|current_profile_missed_structural|
|R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY|R1L73_T034020_20250117_STAGE2A|Stage2-Actionable|2025-01-17|2025-01-17|21750|structural_success_prime_bridge|current_profile_correct|
|R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF|R1L73_T011700_20220310_STAGE2_THEME|Stage2-ThemeSpike|2022-03-10|2022-03-10|4490|price_only_theme_blowoff_counterexample|current_profile_false_positive|
|R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT|R1L73_T006910_20220310_STAGE2A_HOLDOUT|Stage2-Actionable|2022-03-10|2022-03-10|6840|policy_only_false_positive_holdout|current_profile_false_positive|
|R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF|R1L73_T011700_20220504_4B_PRICE_ONLY_OVERLAY|Stage4B-overlay|2022-05-04|2022-05-04|13850|good_overlay_only_not_positive_stage|current_profile_correct|

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|
|R1L73_T083650_20250117_STAGE2A|2025-01-17 @ 18080|37.17|-4.04|163.27|-15.54|242.37|-15.54|2026-02-20|90000|0.0|
|R1L73_T105840_20250117_STAGE2A|2025-01-17 @ 7450|14.09|-3.09|36.24|-19.46|161.07|-19.46|2026-02-20|30100|0.0|
|R1L73_T034020_20250117_STAGE2A|2025-01-17 @ 21750|42.07|-2.76|99.77|-8.23|289.43|-8.23|2025-10-16|84700|-5.79|
|R1L73_T011700_20220310_STAGE2_THEME|2022-03-10 @ 4490|190.65|-1.67|232.96|-1.67|232.96|-1.67|2022-05-04|14950|-61.94|
|R1L73_T006910_20220310_STAGE2A_HOLDOUT|2022-03-10 @ 6840|32.31|-6.87|32.31|-28.51|32.31|-37.94|2022-03-25|9050|-53.09|
|R1L73_T011700_20220504_4B_PRICE_ONLY_OVERLAY|2022-05-04 @ 13850|7.94|-24.19|7.94|-41.81|7.94|-58.92|2022-05-04|14950|-61.94|

## 13. Current Calibrated Profile Stress Test

|case_id|current verdict|Stage2 bonus|Yellow 75|Green 87/rev55|price-only guard|4B non-price|4C routing|
|---|---|---|---|---|---|---|---|
|R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER|missed supplier bridge|slightly insufficient|too strict for legal de-risked supplier|kept strict|appropriate|not primary|watch only|
|R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE|missed supplier bridge|slightly insufficient|borderline strict|kept strict|appropriate|not primary|watch only|
|R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY|correct|adequate|adequate|kept strict|appropriate|appropriate later|watch only|
|R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF|false positive if policy-only promoted|too broad without bridge|too loose for theme|Green blocked correctly|must be strengthened|overlay only|false-break watch|
|R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT|false positive if policy-only promoted|too broad without bridge|too loose for theme|Green blocked correctly|must be strengthened|overlay only|false-break watch|

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable remains useful for C04 because legal de-risking can be visible before financial revisions. The residual error is not “Stage2 too early” in general. The error is that C04 needs two lanes: legal de-risking with supplier/prime bridge can be Yellow-eligible, while policy-only theme spikes should remain Stage2-watch/Actionable and be barred from Green.

No confirmed Stage3-Green trigger is used for promotion in this loop. Therefore `green_lateness_ratio=not_applicable` for representative Stage2 rows. The shadow rule explicitly keeps `stage3_green_revision_min=55` intact.

## 15. 4B Local vs Full-window Timing Audit

|trigger_id|4B local proximity|4B full-window proximity|evidence type|timing verdict|
|---|---|---|---|---|
|R1L73_T083650_20250117_STAGE2A|None|None|[]|not_applicable_stage2|
|R1L73_T105840_20250117_STAGE2A|None|None|[]|not_applicable_stage2|
|R1L73_T034020_20250117_STAGE2A|0.98|0.98|['valuation_blowoff', 'positioning_overheat']|good_full_window_4B_timing_if_nonprice_overheat_later|
|R1L73_T011700_20220310_STAGE2_THEME|None|None|['price_only', 'positioning_overheat']|price_only_blowoff_should_not_promote_stage3|
|R1L73_T006910_20220310_STAGE2A_HOLDOUT|None|None|['price_only', 'positioning_overheat']|price_only_blowoff_should_not_promote_stage3|
|R1L73_T011700_20220504_4B_PRICE_ONLY_OVERLAY|0.895|0.895|['price_only', 'positioning_overheat']|price_only_local_4B_not_full_4B|

## 16. 4C Protection Audit

No hard 4C is promoted from price alone. The two policy-only examples are `false_break` or `thesis_break_watch_only` because the initial thesis was never contract/revision based. For C04, hard 4C should be reserved for explicit project cancellation, legal block, qualification failure, or contract call-off. This loop strengthens the distinction between “theme exhausted” and “thesis broken.”

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

For `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`, nuclear names should not all be scored from the same policy headline. A nuclear legal de-risking event should receive limited positive treatment only when there is an identifiable equipment, customer, contract, or supplier-capacity route. Pure policy-election theme moves should be capped below Stage3 structural labels even when MFE is large.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

Proposed C04 shadow rule:

```text
if canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY:
    if legal_or_IP_overhang_removed and supplier_or_prime_equipment_route_identifiable:
        add limited C04 bridge bonus to Stage2/Yellow only
        do not allow Green unless confirmed_revision or contract/customer conversion exists
    if policy_only_theme and no company-level bridge:
        cap at Stage2-watch/Stage2-actionable
        mark price spike as 4B overlay only if positioning/valuation overheats
```

## 19. Before / After Backtest Comparison

|profile_id|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|alignment|
|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|5|112.91|-14.68|191.63|-16.57|0.4|2|mixed; misses supplier positives and can over-promote policy-only theme spikes|
|P0b_e2r_2_0_baseline_reference|5|112.91|-14.68|191.63|-16.57|0.6|3|worse; too blunt on policy themes|
|P1_C04_supplier_legal_derisking_bridge|5|112.91|-14.68|191.63|-16.57|0.2|0|best shadow profile for C04; captures BHI/Woojin/Doosan and caps HanShin/Bosung|
|P2_C04_policy_theme_counterexample_guard|2|132.63|-15.09|132.63|-19.8|0.0|0|guard only; prevents price-only success from becoming structural label|
|P3_C04_4B_overlay_only_profile|1|7.94|-41.81|7.94|-58.92|0.0|0|good overlay-only timing; not a production exit rule|

## 20. Score-Return Alignment Matrix

|case_id|score before|label before|score after|label after|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|
|R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER|72|Stage2-Actionable|79|Stage3-Yellow|163.27|-15.54|positive high-MFE but current proxy likely under-weights tier-2 supplier bridge after IP/legal de-risking|
|R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE|67|Stage2-Actionable|74|Stage2-Actionable|36.24|-19.46|positive, but high-MAE path requires supplier-quality and legal de-risking separation rather than a blanket nuclear theme boost|
|R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY|83|Stage3-Yellow|86|Stage3-Yellow|99.77|-8.23|strong positive; legal dispute resolution plus prime-equipment conversion bridge aligned with very large MFE and limited early MAE|
|R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF|76|Stage3-Yellow|58|Stage2-Watch|232.96|-1.67|price MFE was huge, but it was a policy/theme blowoff with no durable contract or revision bridge; drawdown after peak was severe|
|R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT|73|Stage2-Actionable|55|Stage2-Watch|32.31|-28.51|early price spike reversed; without contract/customer/legal-close bridge it should not be promoted above Stage2-watch/Yellow stress|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L1_INDUSTRIALS_INFRA_DEFENSE_GRID|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP|3|2|1|0|4|1|6|5|4|True|True|C04 now has legal-de-risking supplier positives plus policy-only blowoff counterexamples; still needs more formal-disclosure contract rows.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: ['R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT']
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: supplier_bridge_underweighted, policy_only_theme_overpromoted, price_only_local_4B_overlay_needed
new_axis_proposed: nuclear_legal_derisking_supplier_bridge_bonus; nuclear_policy_only_theme_stage_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated scope: historical trigger-level backtest from stock-web tradable OHLC rows, 30D/90D/180D MFE/MAE, clean 180D corporate-action windows, C04-specific score/return alignment, policy-only counterexample audit, 4B overlay split.

Non-validation scope: no live watchlist, no current candidate scan, no production scoring patch, no broker/API work, no `stock_agent` source-code inspection, no claim that these shadow weights should be promoted globally.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,nuclear_legal_derisking_supplier_bridge_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,+1,+1,"IP/legal overhang removal plus identifiable nuclear equipment/supplier route deserves limited bridge bonus, but not Green without revision or contract.","Captures BHI/Woojin delayed positives while keeping Green strict",R1L73_T083650_20250117_STAGE2A|R1L73_T105840_20250117_STAGE2A|R1L73_T034020_20250117_STAGE2A,5,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,nuclear_policy_only_theme_stage_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,weak,strong,+1,"Election/policy-only nuclear theme spikes require company-level order/customer/revision bridge before Stage3 promotion.","Reduces HanShin/Bosung false-positive structural labels",R1L73_T011700_20220310_STAGE2_THEME|R1L73_T006910_20220310_STAGE2A_HOLDOUT,5,4,2,medium,guard_shadow_only,"not production; strengthens price-only blowoff guard inside C04"
shadow_weight,nuclear_price_only_4B_overlay_split,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,kept,strengthened,+1,"Price-only local peaks after nuclear policy themes are 4B overlay only; full 4B requires non-price cap evidence.","Improves 4B annotation without changing positive-stage scoring",R1L73_T011700_20220504_4B_PRICE_ONLY_OVERLAY,1,1,1,medium_low,4B_overlay_shadow_only,"not production; local vs full-window split retained"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "R1L73_T083650_20250117_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "positive high-MFE but current proxy likely under-weights tier-2 supplier bridge after IP/legal de-risking", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "New C04 symbol. Westinghouse/KHNP settlement removed an export-IP/legal overhang; BHI had nuclear/HRSG boiler supplier optionality but no immediate prime-contract conversion. The rule candidate promotes only to Yellow, not Green."}
{"row_type": "case", "case_id": "R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE", "symbol": "105840", "company_name": "우진", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "R1L73_T105840_20250117_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "positive, but high-MAE path requires supplier-quality and legal de-risking separation rather than a blanket nuclear theme boost", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "New C04 symbol. Westinghouse settlement acted as legal de-risking; the follow-through arrived after the market recognized nuclear instrumentation exposure."}
{"row_type": "case", "case_id": "R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L73_T034020_20250117_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol appeared in prior C04 Czech-preferred-bidder path, but 2025-01-17 is a different trigger family: IP/legal dispute settlement and global nuclear-market re-entry bridge", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "score_price_alignment": "strong positive; legal dispute resolution plus prime-equipment conversion bridge aligned with very large MFE and limited early MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Reused symbol but new C04 trigger family. This case compresses C31 policy/legal de-risking into C04 nuclear project legal-delay archetype."}
{"row_type": "case", "case_id": "R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF", "symbol": "011700", "company_name": "한신기계", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R1L73_T011700_20220310_STAGE2_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "price MFE was huge, but it was a policy/theme blowoff with no durable contract or revision bridge; drawdown after peak was severe", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "New C04 counterexample symbol. Yoon election nuclear-policy inflection created strong price momentum, but not enough company-specific Stage3 evidence."}
{"row_type": "case", "case_id": "R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT", "symbol": "006910", "company_name": "보성파워텍", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R1L73_T006910_20220310_STAGE2A_HOLDOUT", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "holdout counterexample reused from prior C04/C31 nuclear policy-only rows to anchor the policy-theme cap; not counted as new evidence", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "early price spike reversed; without contract/customer/legal-close bridge it should not be promoted above Stage2-watch/Yellow stress", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Reused holdout only. Included because the same policy headline produced false-positive behavior while Westinghouse settlement produced supplier-specific positive paths."}
{"trigger_id": "R1L73_T083650_20250117_STAGE2A", "case_id": "R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER", "symbol": "083650", "company_name": "비에이치아이", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-17", "entry_date": "2025-01-17", "entry_price": 18080, "evidence_available_at_that_date": "KHNP/KEPCO-Westinghouse IP/legal dispute settlement and global nuclear cooperation headline; supplier exposure known, but no immediate firm order conversion on trigger date", "evidence_source": "Reuters 2025-01-17 Westinghouse-KHNP/KEPCO settlement; stock-web 083650 2025 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083650/2025.csv", "profile_path": "atlas/symbol_profiles/083/083650.json", "MFE_30D_pct": 37.17, "MFE_90D_pct": 163.27, "MFE_180D_pct": 242.37, "MFE_1Y_pct": 397.79, "MFE_2Y_pct": null, "MAE_30D_pct": -4.04, "MAE_90D_pct": -15.54, "MAE_180D_pct": -15.54, "MAE_1Y_pct": -15.54, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 90000, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_stage2", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_high_MFE_supplier_bridge", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "sector": "nuclear_supply_chain", "primary_archetype": "nuclear legal de-risking + supplier capacity bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "same_entry_group_id": "R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER_2025-01-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R1L73_T105840_20250117_STAGE2A", "case_id": "R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE", "symbol": "105840", "company_name": "우진", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-17", "entry_date": "2025-01-17", "entry_price": 7450, "evidence_available_at_that_date": "KHNP/KEPCO-Westinghouse dispute settlement reduced nuclear export legal overhang; instrumentation/sensor supplier exposure existed but the Stage3 conversion bridge was not yet confirmed", "evidence_source": "Reuters 2025-01-17 Westinghouse-KHNP/KEPCO settlement; stock-web 105840 2025 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2025.csv", "profile_path": "atlas/symbol_profiles/105/105840.json", "MFE_30D_pct": 14.09, "MFE_90D_pct": 36.24, "MFE_180D_pct": 161.07, "MFE_1Y_pct": 292.62, "MFE_2Y_pct": null, "MAE_30D_pct": -3.09, "MAE_90D_pct": -19.46, "MAE_180D_pct": -19.46, "MAE_1Y_pct": -19.46, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 30100, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_stage2", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_delayed_supplier_bridge", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "sector": "nuclear_supply_chain", "primary_archetype": "nuclear legal de-risking + instrumentation supplier bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "same_entry_group_id": "R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE_2025-01-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R1L73_T034020_20250117_STAGE2A", "case_id": "R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY", "symbol": "034020", "company_name": "두산에너빌리티", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-17", "entry_date": "2025-01-17", "entry_price": 21750, "evidence_available_at_that_date": "KHNP/KEPCO-Westinghouse settlement removed an IP/export legal overhang for Korea-led nuclear export projects; prime equipment exposure had clearer conversion bridge than theme-only suppliers", "evidence_source": "Reuters 2025-01-17 settlement; stock-web 034020 tradable shard values as parsed in prior allowed C31 artifact", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "MFE_30D_pct": 42.07, "MFE_90D_pct": 99.77, "MFE_180D_pct": 289.43, "MFE_1Y_pct": 289.43, "MFE_2Y_pct": null, "MAE_30D_pct": -2.76, "MAE_90D_pct": -8.23, "MAE_180D_pct": -8.23, "MAE_1Y_pct": -8.23, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-10-16", "peak_price": 84700, "drawdown_after_peak_pct": -5.79, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_if_nonprice_overheat_later", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_prime_bridge", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "sector": "nuclear_prime_equipment", "primary_archetype": "nuclear legal de-risking + prime equipment conversion bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "same_entry_group_id": "R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY_2025-01-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol appeared in prior C04 Czech-preferred-bidder path, but 2025-01-17 is a different trigger family: IP/legal dispute settlement and global nuclear-market re-entry bridge", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"trigger_id": "R1L73_T011700_20220310_STAGE2_THEME", "case_id": "R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF", "symbol": "011700", "company_name": "한신기계", "trigger_type": "Stage2-ThemeSpike", "trigger_date": "2022-03-10", "entry_date": "2022-03-10", "entry_price": 4490, "evidence_available_at_that_date": "Yoon election nuclear-policy inflection headline; company-specific contract/order/revision bridge was absent at trigger date", "evidence_source": "Reuters/KBS/public election result context; stock-web 011700 2022 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011700/2022.csv", "profile_path": "atlas/symbol_profiles/011/011700.json", "MFE_30D_pct": 190.65, "MFE_90D_pct": 232.96, "MFE_180D_pct": 232.96, "MFE_1Y_pct": 232.96, "MFE_2Y_pct": null, "MAE_30D_pct": -1.67, "MAE_90D_pct": -1.67, "MAE_180D_pct": -1.67, "MAE_1Y_pct": -26.5, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2022-05-04", "peak_price": 14950, "drawdown_after_peak_pct": -61.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_blowoff_should_not_promote_stage3", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "price_only_theme_blowoff_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "sector": "nuclear_theme_supplier", "primary_archetype": "policy-only nuclear theme without company conversion bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "same_entry_group_id": "R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF_2022-03-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"trigger_id": "R1L73_T006910_20220310_STAGE2A_HOLDOUT", "case_id": "R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT", "symbol": "006910", "company_name": "보성파워텍", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-03-10", "entry_date": "2022-03-10", "entry_price": 6840, "evidence_available_at_that_date": "Yoon election nuclear-policy inflection headline; no company-specific contract/order/revision bridge at trigger date", "evidence_source": "prior allowed C04/C31 holdout row; stock-web 006910 profile and shard path validated", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2022.csv", "profile_path": "atlas/symbol_profiles/006/006910.json", "MFE_30D_pct": 32.31, "MFE_90D_pct": 32.31, "MFE_180D_pct": 32.31, "MFE_1Y_pct": 32.31, "MFE_2Y_pct": null, "MAE_30D_pct": -6.87, "MAE_90D_pct": -28.51, "MAE_180D_pct": -37.94, "MAE_1Y_pct": -53.09, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-25", "peak_price": 9050, "drawdown_after_peak_pct": -53.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_blowoff_should_not_promote_stage3", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "policy_only_false_positive_holdout", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "sector": "nuclear_theme_supplier", "primary_archetype": "policy-only nuclear theme without company conversion bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "same_entry_group_id": "R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT_2022-03-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "holdout counterexample reused from prior C04/C31 nuclear policy-only rows to anchor the policy-theme cap; not counted as new evidence", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"trigger_id": "R1L73_T011700_20220504_4B_PRICE_ONLY_OVERLAY", "case_id": "R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF", "symbol": "011700", "company_name": "한신기계", "trigger_type": "Stage4B-overlay", "trigger_date": "2022-05-04", "entry_date": "2022-05-04", "entry_price": 13850, "evidence_available_at_that_date": "No non-price cap; this is local price/positioning overheat after policy-only theme surge", "evidence_source": "stock-web 011700 2022 tradable shard; overlay derived from observed local/full peak", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011700/2022.csv", "profile_path": "atlas/symbol_profiles/011/011700.json", "MFE_30D_pct": 7.94, "MFE_90D_pct": 7.94, "MFE_180D_pct": 7.94, "MFE_1Y_pct": 7.94, "MFE_2Y_pct": null, "MAE_30D_pct": -24.19, "MAE_90D_pct": -41.81, "MAE_180D_pct": -58.92, "MAE_1Y_pct": -64.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-04", "peak_price": 14950, "drawdown_after_peak_pct": -61.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.895, "four_b_full_window_peak_proximity": 0.895, "four_b_timing_verdict": "price_only_local_4B_not_full_4B", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "good_overlay_only_not_positive_stage", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "row_type": "trigger", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_LEGAL_DE_RISKING_SUPPLIER_BRIDGE_AND_POLICY_THEME_CAP", "sector": "nuclear_theme_supplier", "primary_archetype": "policy-only nuclear theme without company conversion bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "same_entry_group_id": "R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF_2022-05-04", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L73_C04_083650_BHI_20250117_WESTINGHOUSE_LEGAL_DERISK_SUPPLIER", "trigger_id": "R1L73_T083650_20250117_STAGE2A", "symbol": "083650", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 7, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 20, "valuation_repricing_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 8, "margin_bridge_score": 0, "revision_score": 9, "relative_strength_score": 18, "customer_quality_score": 15, "policy_or_regulatory_score": 23, "valuation_repricing_score": 0, "execution_risk_score": 7, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "backlog_visibility_score", "legal_or_contract_risk_score", "theme_only_stage_cap"], "component_delta_explanation": "Shadow-only C04 adjustment: add limited supplier/legal-de-risking bridge when IP/legal blocker clears and company has identifiable nuclear equipment route; cap policy-only theme blowoffs without contract/customer/revision bridge.", "MFE_90D_pct": 163.27, "MAE_90D_pct": -15.54, "score_return_alignment_label": "positive high-MFE but current proxy likely under-weights tier-2 supplier bridge after IP/legal de-risking", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L73_C04_105840_WOOJIN_20250117_WESTINGHOUSE_SENSOR_INSTRUMENT_BRIDGE", "trigger_id": "R1L73_T105840_20250117_STAGE2A", "symbol": "105840", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 12, "customer_quality_score": 8, "policy_or_regulatory_score": 19, "valuation_repricing_score": 0, "execution_risk_score": 9, "legal_or_contract_risk_score": 9, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 67, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 7, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 14, "customer_quality_score": 11, "policy_or_regulatory_score": 22, "valuation_repricing_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "backlog_visibility_score", "legal_or_contract_risk_score", "theme_only_stage_cap"], "component_delta_explanation": "Shadow-only C04 adjustment: add limited supplier/legal-de-risking bridge when IP/legal blocker clears and company has identifiable nuclear equipment route; cap policy-only theme blowoffs without contract/customer/revision bridge.", "MFE_90D_pct": 36.24, "MAE_90D_pct": -19.46, "score_return_alignment_label": "positive, but high-MAE path requires supplier-quality and legal de-risking separation rather than a blanket nuclear theme boost", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L73_C04_034020_DOOSAN_20250117_WESTINGHOUSE_PRIME_REENTRY", "trigger_id": "R1L73_T034020_20250117_STAGE2A", "symbol": "034020", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 12, "margin_bridge_score": 8, "revision_score": 16, "relative_strength_score": 18, "customer_quality_score": 16, "policy_or_regulatory_score": 22, "valuation_repricing_score": 0, "execution_risk_score": 6, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 83, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 10, "revision_score": 18, "relative_strength_score": 18, "customer_quality_score": 18, "policy_or_regulatory_score": 23, "valuation_repricing_score": 0, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "backlog_visibility_score", "legal_or_contract_risk_score", "theme_only_stage_cap"], "component_delta_explanation": "Shadow-only C04 adjustment: add limited supplier/legal-de-risking bridge when IP/legal blocker clears and company has identifiable nuclear equipment route; cap policy-only theme blowoffs without contract/customer/revision bridge.", "MFE_90D_pct": 99.77, "MAE_90D_pct": -8.23, "score_return_alignment_label": "strong positive; legal dispute resolution plus prime-equipment conversion bridge aligned with very large MFE and limited early MAE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L73_C04_011700_HANSHIN_20220310_YOON_NUCLEAR_THEME_BLOWOFF", "trigger_id": "R1L73_T011700_20220310_STAGE2_THEME", "symbol": "011700", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 25, "customer_quality_score": 0, "policy_or_regulatory_score": 22, "valuation_repricing_score": 12, "execution_risk_score": 14, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 8, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "backlog_visibility_score", "legal_or_contract_risk_score", "theme_only_stage_cap"], "component_delta_explanation": "Shadow-only C04 adjustment: add limited supplier/legal-de-risking bridge when IP/legal blocker clears and company has identifiable nuclear equipment route; cap policy-only theme blowoffs without contract/customer/revision bridge.", "MFE_90D_pct": 232.96, "MAE_90D_pct": -1.67, "score_return_alignment_label": "price MFE was huge, but it was a policy/theme blowoff with no durable contract or revision bridge; drawdown after peak was severe", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L73_C04_006910_BOSUNG_20220310_POLICY_ONLY_HOLDOUT", "trigger_id": "R1L73_T006910_20220310_STAGE2A_HOLDOUT", "symbol": "006910", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 22, "valuation_repricing_score": 10, "execution_risk_score": 15, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 6, "execution_risk_score": 21, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage2-Watch", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "backlog_visibility_score", "legal_or_contract_risk_score", "theme_only_stage_cap"], "component_delta_explanation": "Shadow-only C04 adjustment: add limited supplier/legal-de-risking bridge when IP/legal blocker clears and company has identifiable nuclear equipment route; cap policy-only theme blowoffs without contract/customer/revision bridge.", "MFE_90D_pct": 32.31, "MAE_90D_pct": -28.51, "score_return_alignment_label": "early price spike reversed; without contract/customer/legal-close bridge it should not be promoted above Stage2-watch/Yellow stress", "current_profile_verdict": "current_profile_false_positive"}
{"profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "profile_hypothesis": "current global calibrated profile without C04 supplier/legal-de-risking bridge", "changed_axes": [], "changed_thresholds": {}, "eligible_trigger_count": 5, "selected_entry_trigger_per_case": "representative Stage2 rows", "avg_MFE_90D_pct": 112.91, "avg_MAE_90D_pct": -14.68, "avg_MFE_180D_pct": 191.63, "avg_MAE_180D_pct": -16.57, "false_positive_rate": 0.4, "missed_structural_count": 2, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": null, "avg_four_b_full_window_peak_proximity": null, "score_return_alignment_verdict": "mixed; misses supplier positives and can over-promote policy-only theme spikes"}
{"profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "older baseline with weaker Stage2 actionability and weaker 4B/4C separation", "changed_axes": ["rollback_reference_only"], "changed_thresholds": {}, "eligible_trigger_count": 5, "selected_entry_trigger_per_case": "same", "avg_MFE_90D_pct": 112.91, "avg_MAE_90D_pct": -14.68, "avg_MFE_180D_pct": 191.63, "avg_MAE_180D_pct": -16.57, "false_positive_rate": 0.6, "missed_structural_count": 3, "late_green_count": 1, "avg_green_lateness_ratio": "worse", "avg_four_b_local_peak_proximity": 0.895, "avg_four_b_full_window_peak_proximity": 0.895, "score_return_alignment_verdict": "worse; too blunt on policy themes"}
{"profile_id": "P1_C04_supplier_legal_derisking_bridge", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "legal/IP overhang removal plus identifiable nuclear-equipment route can receive limited C04 bridge bonus, capped below Green until contract/revision evidence appears", "changed_axes": ["nuclear_legal_derisking_supplier_bridge_bonus", "prime_equipment_legal_reentry_bridge", "policy_only_theme_cap"], "changed_thresholds": {"Stage3-Green": "no Green without confirmed revision/contract", "Stage3-Yellow": "allowed only with supplier route + legal de-risking"}, "eligible_trigger_count": 5, "selected_entry_trigger_per_case": "same", "avg_MFE_90D_pct": 112.91, "avg_MAE_90D_pct": -14.68, "avg_MFE_180D_pct": 191.63, "avg_MAE_180D_pct": -16.57, "false_positive_rate": 0.2, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_primary_metric", "avg_four_b_local_peak_proximity": 0.895, "avg_four_b_full_window_peak_proximity": 0.895, "score_return_alignment_verdict": "best shadow profile for C04; captures BHI/Woojin/Doosan and caps HanShin/Bosung"}
{"profile_id": "P2_C04_policy_theme_counterexample_guard", "profile_scope": "canonical_archetype_specific_guard", "profile_hypothesis": "pure election-policy nuclear theme needs company-level order/customer/revision bridge; otherwise keep Stage2-watch or Yellow-stress only", "changed_axes": ["theme_only_stage_cap", "price_only_blowoff_blocks_positive_stage_strengthened"], "changed_thresholds": {"policy_only": "max Stage2-Watch or Stage2-Actionable, no Green"}, "eligible_trigger_count": 2, "selected_entry_trigger_per_case": "counterexample representative rows", "avg_MFE_90D_pct": 132.63, "avg_MAE_90D_pct": -15.09, "avg_MFE_180D_pct": 132.63, "avg_MAE_180D_pct": -19.8, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.895, "avg_four_b_full_window_peak_proximity": 0.895, "score_return_alignment_verdict": "guard only; prevents price-only success from becoming structural label"}
{"profile_id": "P3_C04_4B_overlay_only_profile", "profile_scope": "4B_overlay_guard", "profile_hypothesis": "local price blowoff around policy themes is an overlay; full 4B needs non-price cap evidence", "changed_axes": ["split_4B_local_vs_full_window", "full_4b_requires_non_price_evidence_strengthened"], "changed_thresholds": {"full_4B": "non-price cap required"}, "eligible_trigger_count": 1, "selected_entry_trigger_per_case": "011700 2022-05-04 overlay", "avg_MFE_90D_pct": 7.94, "avg_MAE_90D_pct": -41.81, "avg_MFE_180D_pct": 7.94, "avg_MAE_180D_pct": -58.92, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.895, "avg_four_b_full_window_peak_proximity": 0.895, "score_return_alignment_verdict": "good overlay-only timing; not a production exit rule"}
{"row_type": "residual_contribution", "round": "R1", "loop": "73", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "scheduled_round": "R1", "scheduled_loop": "73", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 1, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 3, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_false_positive", "supplier_bridge_underweighted", "policy_only_theme_overpromoted", "price_only_local_4B_overlay_needed"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "new_symbols=3; same_symbol_new_trigger_family=1; counterexamples=2; reused_holdout=1; duplicate_key_conflict=0 for aggregate"}
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
completed_round = R1
completed_loop = 73
next_round = R2
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest/schema checked in this run: `atlas/manifest.json`, `atlas/schema.json`.
- Stock-Web profile files checked in this run: `083650`, `105840`, `011700`, `006910`; 034020 path and OHLC values reuse prior allowed C31 artifact for the same 2025-01-17 trigger family.
- Price rows cited in the working run came from `atlas/ohlcv_tradable_by_symbol_year/...` shards.
- External evidence context: 2025-01-17 Westinghouse/KHNP/KEPCO dispute settlement; 2024 Czech KHNP preferred bidder event and subsequent legal overhang; 2022 Yoon nuclear-policy election inflection. External facts are used only to label historical trigger families, not to create live recommendations.

