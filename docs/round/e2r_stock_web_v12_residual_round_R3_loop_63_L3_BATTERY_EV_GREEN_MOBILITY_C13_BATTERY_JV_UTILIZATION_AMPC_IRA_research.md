# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R3
loop = 63
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This file is historical calibration research only. It is not a live scan, not an investment recommendation, not an auto-trading instruction, and not a `stock_agent` code patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual being tested here is narrower than the global profile: **C13 can be misread when a policy/JV/AMPC headline is treated like operating utilization**. A factory, a DOE loan, or an AMPC credit is a bridge; it is not the cargo crossing the bridge. The stock path asks whether the scoring profile should require a second key: utilization or margin confirmation.

## 2. Round / Large Sector / Canonical Archetype Scope

|field|value|
|---|---|
|round|R3|
|loop|63|
|large_sector_id|L3_BATTERY_EV_GREEN_MOBILITY|
|canonical_archetype_id|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|
|fine_archetype_id|BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE|
|loop_objective|coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test|
|representative symbols|373220, 006400, 096770|
|case mix|2 positive / high-MAE-success cases; 1 policy-JV false positive; 1 non-representative 4B overlay trigger|

## 3. Previous Coverage / Duplicate Avoidance Check

Permitted artifact access was used only for coverage and duplicate avoidance. The accessible repository search returned no direct `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` hit, so the loop is treated as a direct C13 coverage-gap fill. The prior C12 file covered customer call-off risk; this C13 file covers the adjacent but distinct **policy/JV/AMPC utilization bridge**.

```text
auto_selected_coverage_gap = C13 direct AMPC/JV utilization coverage absent in accessible search snapshot
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

|field|value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|price_atlas_repo|https://github.com/Songdaiki/stock-web|
|manifest_path|atlas/manifest.json|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|price_basis|tradable_raw|
|price_adjustment_status|raw_unadjusted_marcap|

The manifest says the atlas is raw/unadjusted, zero-volume and invalid OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows must be blocked by default. This file follows that rule.

## 5. Historical Eligibility Gate

|case_id|symbol|entry_date|180D window|corporate-action status|calibration_usable|
|---|---|---|---|---|---|
|C13-LGES-2024Q2-AMPC-CAPACITY-PACING|373220|2024-07-25|available through 2025-04 window|clean; profile has no corporate action candidate|true|
|C13-SDI-2024-STARPLUS-DOE-LOAN|006400|2024-12-03|available through 2025-08 window|clean; profile action dates 1996/1998/2014 only|true|
|C13-SKI-2024-BLUEOVAL-FINAL-LOAN|096770|2024-12-16|available through 2025-08 window|2024-11-20 discontinuity is pre-entry, not inside forward window|true|

Entry timing rule used: where exact intraday availability was not guaranteed, the next tradable close was used. For Reuters events dated after Korea market close, the next local trading close is used. For SKI's 2024-12-16 Reuters/DOE event, 2024-12-16 close is retained as a same-day/US pre-market policy event proxy because the event date and close are aligned in the source row; the row remains a research proxy.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE
mapped evidence families:
- finalized financing / conditional financing
- AMPC credit quality versus ex-credit operating profit
- JV nameplate capacity versus actual customer pull-through
- automaker EV capex / production uncertainty
- utilization bridge / margin bridge / revision bridge
```

Compression rule: C13 should not explode into separate scoring axes for every DOE loan, JV name, plant, and AMPC article. They compress into one two-key mechanism: **policy/JV support creates optionality; utilization and margin confirmation create rerating evidence**.

## 7. Case Selection Summary

|case_id|symbol|company|case_type|balance|best_trigger|current_profile_verdict|score_price_alignment|
|---|---|---|---|---|---|---|---|
|C13-LGES-2024Q2-AMPC-CAPACITY-PACING|373220|LG에너지솔루션|4B_too_early|positive|TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING|current_profile_4B_too_early|false_hard_4c_positive_rebound|
|C13-SDI-2024-STARPLUS-DOE-LOAN|006400|삼성SDI|failed_rerating|counterexample|TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN|current_profile_false_positive|policy_JV_false_positive_no_utilization_pullthrough|
|C13-SKI-2024-BLUEOVAL-FINAL-LOAN|096770|SK이노베이션|high_mae_success|positive|TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN|current_profile_correct|high_MAE_policy_financing_success|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
representative_trigger_count = 3
```

The positive cases are not clean straight-line winners. They are better described as **high-MAE policy/utilization cases**. That is important: C13 should promote early awareness, not immediately declare high-conviction Green. The counterexample is cleaner: a large StarPlus/DOE conditional-loan headline had tiny 180D MFE and large MAE before the later battery-sector rebound.

## 9. Evidence Source Map

|case_id|evidence_date|source|url|evidence interpretation|
|---|---|---|---|---|
|C13-LGES-2024Q2-AMPC-CAPACITY-PACING|2024-07-25|Reuters, 2024-07-25, LGES cuts sales target on weak EV demand, flags US election risk|https://www.reuters.com/technology/battery-firm-lg-energy-solution-q2-profit-plunges-weak-ev-demand-2024-07-25/|2024 Q2 result and guidance: revenue growth cut, AMPC expectation cut, capacity expansion pacing; but no hard customer cancellation and tariff / China-supply-chain angle left upside optionality.|
|C13-SDI-2024-STARPLUS-DOE-LOAN|2024-12-02|Reuters, 2024-12-02, US proposes $7.54 billion loan to Stellantis, Samsung SDI battery joint venture|https://www.reuters.com/technology/us-proposes-754-billion-loan-stellantis-samsung-sdi-battery-joint-venture-2024-12-02/|U.S. DOE conditional commitment of up to $7.54B to Stellantis/Samsung SDI StarPlus Energy JV for two Indiana EV battery plants; project capacity about 67GWh, but conditional financing did not yet prove utilization, near-term AMPC capture, or customer volume pull-through.|
|C13-SKI-2024-BLUEOVAL-FINAL-LOAN|2024-12-16|Reuters, 2024-12-16, US finalizes $9.63 billion loan for Ford, SK On joint battery venture|https://www.reuters.com/business/autos-transportation/us-finalizes-963-billion-loan-for-ford-sk-joint-battery-venture-2024-12-16/|U.S. DOE finalized a $9.63B loan for Ford/SK On BlueOval SK joint battery venture; final award improved financing visibility versus conditional award, but profitability and EV demand remained separate execution variables.|
|C13-LGES-2024Q2-AMPC-CAPACITY-PACING|2024-10-28|Reuters, 2024-10-28, Battery maker LGES offers measured 2025 outlook after slow EV demand drags down Q3 profit|https://www.reuters.com/business/energy/lg-energy-solution-q3-profit-drops-weak-ev-demand-2024-10-28/|Q3 2024 result/outlook: conservative 2025 revenue view and significant capex reduction; non-price 4B overlay arrived near the full observed local peak after the July risk trigger.|

## 10. Price Data Source Map

|symbol|company|profile_path|price_shard_path|entry_date|entry_price|
|---|---|---|---|---|---|
|373220|LG에너지솔루션|atlas/symbol_profiles/373/373220.json|atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv|2024-07-25|332500|
|006400|삼성SDI|atlas/symbol_profiles/006/006400.json|atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv|2024-12-03|261000|
|096770|SK이노베이션|atlas/symbol_profiles/096/096770.json|atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv|2024-12-16|121400|
|373220|LG에너지솔루션|atlas/symbol_profiles/373/373220.json|atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv|2024-10-28|416500|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company|trigger_type|trigger_date|entry_date|entry_price|MFE_90D|MAE_90D|MFE_180D|MAE_180D|current_profile_verdict|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING|373220|LG에너지솔루션|Stage4B-Watch|2024-07-25|2024-07-25|332500|33.53|-6.47|33.53|-6.62|current_profile_4B_too_early|representative|
|TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN|006400|삼성SDI|Stage2-Actionable|2024-12-02|2024-12-03|261000|2.68|-34.87|2.68|-39.58|current_profile_false_positive|representative|
|TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN|096770|SK이노베이션|Stage2-Actionable|2024-12-16|2024-12-16|121400|15.49|-23.64|15.49|-33.44|current_profile_correct|representative|
|TR-C13-LGES-20241028-Q3-CONSERVATIVE-2025-4B-OVERLAY|373220|LG에너지솔루션|Stage4B-Overlay|2024-10-28|2024-10-28|416500|2.52|-25.45|2.52|-34.09|current_profile_correct|4B_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|corporate_action_window_status|
|---|---|---|---|---|---|---|---|---|---|---|---|
|TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING|332500|26.02|-6.47|33.53|-6.47|33.53|-6.62|2024-10-08|444000|-39.86|clean_180D_window|
|TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN|261000|2.68|-12.07|2.68|-34.87|2.68|-39.58|2024-12-03|268000|-41.16|clean_180D_window|
|TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN|121400|8.07|-9.39|15.49|-23.64|15.49|-33.44|2025-03-13|140200|-42.37|clean_180D_window_after_2024-11-20_pre_entry_discontinuity|
|TR-C13-LGES-20241028-Q3-CONSERVATIVE-2025-4B-OVERLAY|416500|2.52|-10.92|2.52|-25.45|2.52|-34.09|2024-11-04|427000|-37.7|clean_180D_window|

Notes on the calculations:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 13. Current Calibrated Profile Stress Test

### LGES 2024 Q2 AMPC/capacity pacing

Current profile could reasonably raise a 4B/4C watch because revenue growth was cut, expected AMPC GWh was lowered, and capacity pacing appeared. The actual path warns against hard-routing the event: entry 332,500 later reached 444,000 (+33.53% MFE) before the larger drawdown. The profile should treat this as **4B-Watch**, not hard 4C, unless customer cancellation or thesis evidence break appears.

### Samsung SDI StarPlus conditional loan

Current profile can over-score this if it reads DOE conditional commitment and 67GWh nameplate as backlog or utilization. The 180D path had only +2.68% MFE and -39.58% MAE. This is the clean C13 counterexample: **conditional policy financing is not yet operating evidence**.

### SK Innovation / BlueOval SK finalized loan

This is better evidence than a conditional headline because the loan was finalized. However, the stock path still produced a high-MAE pattern: +15.49% MFE but -33.44% MAE. The correct current profile interpretation is Stage2-Actionable with a high-MAE guard, not Stage3-Green.

## 14. Stage2 / Yellow / Green Comparison

|case_id|Stage2 interpretation|Yellow/Green problem|green_lateness_ratio|
|---|---|---|---|
|LGES 2024 Q2|Stage2/4B-Watch: risk evidence plus policy optionality|No confirmed Green; hard 4C would have been too early|not_applicable|
|Samsung SDI StarPlus|Stage2-Watch only: conditional financing/nameplate capacity|Yellow would be false-positive because utilization/margin bridge was absent|not_applicable|
|SKI BlueOval SK|Stage2-Actionable: finalized financing is credible|Green still blocked by battery-unit profitability and execution risk|not_applicable|

C13 is not mainly a Green-lateness problem. It is a **false-Yellow / premature-Green problem**. The key missing component is not price momentum but utilization confirmation.

## 15. 4B Local vs Full-window Timing Audit

|trigger_id|four_b_local_peak_proximity|four_b_full_window_peak_proximity|verdict|evidence_type|
|---|---|---|---|---|
|TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING|None|None|risk_watch_not_full_4B_at_entry|revision_slowdown;margin_or_backlog_slowdown;contract_delay|
|TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN|None|None|policy_JV_headline_not_full_Stage3|legal_or_regulatory_block;contract_delay|
|TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN|None|None|Stage2_valid_but_high_MAE_guard_needed|execution_risk;margin_or_backlog_slowdown|
|TR-C13-LGES-20241028-Q3-CONSERVATIVE-2025-4B-OVERLAY|0.753|0.753|good_full_window_4B_timing|revision_slowdown;margin_or_backlog_slowdown;valuation_blowoff|

The LGES 2024-10-28 overlay is the cleanest 4B timing row. Its 4B entry price of 416,500 was about 75.3% of the move from the July entry to the full observed peak. The earlier July warning was a risk watch; the later October conservative-capex/revenue outlook is the stronger full-window 4B overlay.

## 16. 4C Protection Audit

No hard 4C is proposed in this loop. The observed evidence supports watch-only thesis risk, not direct thesis break.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not_tested
hard_4c_late = not_tested
false_break = LGES July 2024 would have been a false hard-4C if routed directly
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = l3_conditional_policy_financing_discount
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate_delta = +1 guard / discount axis
```

Proposed sector rule:

> In L3 battery/EV names, conditional policy financing, JV nameplate capacity, or expected AMPC support should not by itself promote a trigger to Stage3-Yellow. Require at least one of: finalized financing, visible production utilization, customer volume pull-through, or ex-credit margin bridge.

Backtest effect in this loop: the rule blocks the Samsung SDI false-positive while preserving SKI as Stage2-Actionable and LGES as 4B-Watch rather than hard 4C.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = c13_two_key_utilization_gate
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
candidate_delta = +1 guard / scoring compression
```

C13 should work like a two-key safety box:

```text
Key 1 = policy/JV/AMPC headline or financing visibility
Key 2 = utilization, margin bridge, customer pull-through, or confirmed revision
```

If only Key 1 exists:

```text
max_stage = Stage2-Watch or Stage2-Actionable
no Stage3-Green
Yellow only if risk is low and financing is finalized
```

If Key 1 and Key 2 both exist:

```text
Stage3-Yellow allowed
Stage3-Green allowed only if revision_score and margin_bridge_score clear the calibrated thresholds
```

## 19. Before / After Backtest Comparison

|profile_id|scope|changed_axes|avg_MFE_90D|avg_MAE_90D|false_positive_rate|alignment|
|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|none|17.23|-21.66|0.33|mixed: policy headline without utilization is weak; finalized financing can be Stage2 only|
|P0b_e2r_2_0_baseline_reference|rollback_reference|rollback reference|17.23|-21.66|0.67|worse false-positive control|
|P1_L3_sector_specific_candidate_profile|sector_specific|l3_ampc_utilization_confirmation_gate=+1 guard; conditional_loan_discount=-1|17.23|-21.66|0.0|best sector-level alignment|
|P2_C13_canonical_archetype_candidate_profile|canonical_archetype_specific|c13_two_key_utilization_gate; c13_conditional_policy_event_cap|17.23|-21.66|0.0|best canonical alignment|
|P3_counterexample_guard_profile|canonical_archetype_specific|automaker_capex_or_policy_uncertainty_discount=-2|17.23|-21.66|0.0|good false-positive control but risks over-penalizing LGES-style rebound|

## 20. Score-Return Alignment Matrix

|trigger_id|score_before|stage_before|score_after|stage_after|alignment_label|
|---|---|---|---|---|---|
|TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING|78|Stage3-Yellow-or-4B-Watch|74|Stage2-Actionable-with-4B-Watch|false_hard_4c_positive_rebound|
|TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN|76|Stage3-Yellow|62|Stage2-Watch / No-Yellow|policy_JV_false_positive_no_utilization_pullthrough|
|TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN|74|Stage2-Actionable|72|Stage2-Actionable-with-MAE-Guard|high_MAE_policy_financing_success|
|TR-C13-LGES-20241028-Q3-CONSERVATIVE-2025-4B-OVERLAY|82|Stage4B-Watch|80|Stage4B-Overlay / not hard 4C|good_non_price_4B_overlay_after_rebound|

Raw component scores are included in the machine-readable rows. They are research proxy scores, not production scores.

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE|2|1|1|0|3|0|4|3|2|True|True|C13 now has direct AMPC/JV utilization coverage; next gap is C14 EV demand 4B/4C holdout or C13 additional pure AMPC-positive cases|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_yellow_total_min
  - stage3_green_total_min
residual_error_types_found:
  - policy_JV_false_positive
  - 4B_too_early_without_cancel
  - conditional_financing_overpromotion
new_axis_proposed:
  - c13_two_key_utilization_gate
  - l3_conditional_policy_financing_discount
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C13 direct AMPC/JV utilization coverage absent in accessible search snapshot
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date and price basis
- symbol profile availability and corporate-action windows
- representative entry prices from tradable shards
- 30D/90D/180D MFE/MAE from tradable_raw rows
- positive/counterexample balance
- C13-specific residual rule proposal
- machine-readable rows for later batch ingestion
```

Not validated:

```text
- production scoring code
- live candidates
- current watchlists
- exact intraday timestamp for every historical article
- adjusted OHLC / corporate-action-adjusted price path
- broker/API execution
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c13_two_key_utilization_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,Policy/JV/AMPC support needs utilization or margin bridge before Stage3 promotion.,Reduced SDI false-positive while preserving SKI Stage2 and LGES risk-watch.,TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN|TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN|TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING,3,3,1,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,l3_conditional_policy_financing_discount,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,Conditional loans and nameplate capacity are not the same as operating utilization.,Lowered false positive rate from 0.33 to 0.00 in this mini holdout.,TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN,1,1,1,low_medium,sector_shadow_only,requires more L3 holdout cases
shadow_weight,ampc_cut_is_4b_watch_not_hard_4c_without_cancel,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"AMPC cut/capex pacing can be risk overlay, but hard 4C needs cancellation, qualification failure, or thesis evidence broken.",Avoids over-penalizing LGES 2024 July risk trigger that later had +33.5% MFE.,TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING|TR-C13-LGES-20241028-Q3-CONSERVATIVE-2025-4B-OVERLAY,2,1,0,medium,canonical_shadow_only,"strengthens full_4b_requires_non_price_evidence, does not weaken hard_4c routing"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C13-LGES-2024Q2-AMPC-CAPACITY-PACING", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "63", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE", "case_type": "4B_too_early", "positive_or_counterexample": "positive", "best_trigger": "TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_hard_4c_positive_rebound", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "AMPC/capacity cut is a risk overlay, but without customer cancellation or qualification failure it should not route directly to hard 4C. The later rebound makes an over-aggressive 4B/4C guard visible."}
{"row_type": "case", "case_id": "C13-SDI-2024-STARPLUS-DOE-LOAN", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "63", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_JV_false_positive_no_utilization_pullthrough", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Conditional loan and nameplate GWh should not be scored like running utilization. The observed path had tiny MFE and severe MAE before any durable rerating."}
{"row_type": "case", "case_id": "C13-SKI-2024-BLUEOVAL-FINAL-LOAN", "symbol": "096770", "company_name": "SK이노베이션", "round": "R3", "loop": "63", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_MAE_policy_financing_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Finalized financing is better evidence than a conditional commitment, but it remains a Stage2 financing/capacity route until utilization and battery margin bridge confirm."}
{"row_type": "trigger", "trigger_id": "TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING", "case_id": "C13-LGES-2024Q2-AMPC-CAPACITY-PACING", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "63", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-07-25", "evidence_available_at_that_date": "2024 Q2 result and guidance: revenue growth cut, AMPC expectation cut, capacity expansion pacing; but no hard customer cancellation and tariff / China-supply-chain angle left upside optionality.", "evidence_source": "Reuters, 2024-07-25, LGES cuts sales target on weak EV demand, flags US election risk", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "contract_delay", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-25", "entry_price": 332500, "MFE_30D_pct": 26.02, "MFE_90D_pct": 33.53, "MFE_180D_pct": 33.53, "MFE_1Y_pct": 33.53, "MFE_2Y_pct": null, "MAE_30D_pct": -6.47, "MAE_90D_pct": -6.47, "MAE_180D_pct": -6.62, "MAE_1Y_pct": -19.75, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-08", "peak_price": 444000, "drawdown_after_peak_pct": -39.86, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "risk_watch_not_full_4B_at_entry", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown", "contract_delay"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_hard_4c_positive_rebound", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13-LGES-2024Q2-20240725-332500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN", "case_id": "C13-SDI-2024-STARPLUS-DOE-LOAN", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "63", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-12-02", "evidence_available_at_that_date": "U.S. DOE conditional commitment of up to $7.54B to Stellantis/Samsung SDI StarPlus Energy JV for two Indiana EV battery plants; project capacity about 67GWh, but conditional financing did not yet prove utilization, near-term AMPC capture, or customer volume pull-through.", "evidence_source": "Reuters, 2024-12-02, US proposes $7.54 billion loan to Stellantis, Samsung SDI battery joint venture", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["contract_delay", "legal_or_regulatory_block", "execution_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-03", "entry_price": 261000, "MFE_30D_pct": 2.68, "MFE_90D_pct": 2.68, "MFE_180D_pct": 2.68, "MFE_1Y_pct": 35.82, "MFE_2Y_pct": null, "MAE_30D_pct": -12.07, "MAE_90D_pct": -34.87, "MAE_180D_pct": -39.58, "MAE_1Y_pct": -39.58, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 268000, "drawdown_after_peak_pct": -41.16, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "policy_JV_headline_not_full_Stage3", "four_b_evidence_type": ["legal_or_regulatory_block", "contract_delay"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_JV_false_positive_no_utilization_pullthrough", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13-SDI-2024DOE-20241203-261000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN", "case_id": "C13-SKI-2024-BLUEOVAL-FINAL-LOAN", "symbol": "096770", "company_name": "SK이노베이션", "round": "R3", "loop": "63", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-12-16", "evidence_available_at_that_date": "U.S. DOE finalized a $9.63B loan for Ford/SK On BlueOval SK joint battery venture; final award improved financing visibility versus conditional award, but profitability and EV demand remained separate execution variables.", "evidence_source": "Reuters, 2024-12-16, US finalizes $9.63 billion loan for Ford, SK On joint battery venture", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["execution_risk", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv", "profile_path": "atlas/symbol_profiles/096/096770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-16", "entry_price": 121400, "MFE_30D_pct": 8.07, "MFE_90D_pct": 15.49, "MFE_180D_pct": 15.49, "MFE_1Y_pct": 15.49, "MFE_2Y_pct": null, "MAE_30D_pct": -9.39, "MAE_90D_pct": -23.64, "MAE_180D_pct": -33.44, "MAE_1Y_pct": -33.44, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-13", "peak_price": 140200, "drawdown_after_peak_pct": -42.37, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "Stage2_valid_but_high_MAE_guard_needed", "four_b_evidence_type": ["execution_risk", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_MAE_policy_financing_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2024-11-20_pre_entry_discontinuity", "same_entry_group_id": "C13-SKI-2024BLUEOVAL-20241216-121400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR-C13-LGES-20241028-Q3-CONSERVATIVE-2025-4B-OVERLAY", "case_id": "C13-LGES-2024Q2-AMPC-CAPACITY-PACING", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "63", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "BATTERY_JV_UTILIZATION_AMPC_IRA_QUALITY_GATE", "sector": "battery_ev_green_mobility", "primary_archetype": "battery_jv_utilization_ampc_ira", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-10-28", "evidence_available_at_that_date": "Q3 2024 result/outlook: conservative 2025 revenue view and significant capex reduction; non-price 4B overlay arrived near the full observed local peak after the July risk trigger.", "evidence_source": "Reuters, 2024-10-28, Battery maker LGES offers measured 2025 outlook after slow EV demand drags down Q3 profit", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "revision_slowdown", "margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-28", "entry_price": 416500, "MFE_30D_pct": 2.52, "MFE_90D_pct": 2.52, "MFE_180D_pct": 2.52, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.92, "MAE_90D_pct": -25.45, "MAE_180D_pct": -34.09, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-04", "peak_price": 427000, "drawdown_after_peak_pct": -37.7, "green_lateness_ratio": "not_applicable:4B_overlay_only", "four_b_local_peak_proximity": 0.753, "four_b_full_window_peak_proximity": 0.753, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "good_non_price_4B_overlay_after_rebound", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C13-LGES-2024Q2-20241028-416500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13-LGES-2024Q2-AMPC-CAPACITY-PACING", "trigger_id": "TR-C13-LGES-20240725-Q2-AMPC-CUT-CAPEX-PACING", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 15, "valuation_repricing_score": 5, "execution_risk_score": 16, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow-or-4B-Watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 10, "revision_score": 12, "relative_strength_score": 9, "customer_quality_score": 12, "policy_or_regulatory_score": 14, "valuation_repricing_score": 5, "execution_risk_score": 12, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable-with-4B-Watch", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "margin_bridge_score", "revision_score", "customer_quality_score"], "component_delta_explanation": "AMPC/capacity cut is a risk overlay, but without customer cancellation or qualification failure it should not route directly to hard 4C. The later rebound makes an over-aggressive 4B/4C guard visible.", "MFE_90D_pct": 33.53, "MAE_90D_pct": -6.47, "score_return_alignment_label": "false_hard_4c_positive_rebound", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13-SDI-2024-STARPLUS-DOE-LOAN", "trigger_id": "TR-C13-SDI-20241203-STARPLUS-DOE-CONDITIONAL-LOAN", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 9, "margin_bridge_score": 3, "revision_score": 8, "relative_strength_score": 3, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 5, "execution_risk_score": 10, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 1, "revision_score": 4, "relative_strength_score": 2, "customer_quality_score": 7, "policy_or_regulatory_score": 14, "valuation_repricing_score": 4, "execution_risk_score": 18, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "Stage2-Watch / No-Yellow", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "margin_bridge_score", "revision_score", "customer_quality_score"], "component_delta_explanation": "Conditional loan and nameplate GWh should not be scored like running utilization. The observed path had tiny MFE and severe MAE before any durable rerating.", "MFE_90D_pct": 2.68, "MAE_90D_pct": -34.87, "score_return_alignment_label": "policy_JV_false_positive_no_utilization_pullthrough", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13-SKI-2024-BLUEOVAL-FINAL-LOAN", "trigger_id": "TR-C13-SKI-20241216-BLUEOVALSK-FINAL-LOAN", "symbol": "096770", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 8, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 21, "valuation_repricing_score": 5, "execution_risk_score": 12, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 8, "margin_bridge_score": 2, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 18, "valuation_repricing_score": 5, "execution_risk_score": 15, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable-with-MAE-Guard", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "margin_bridge_score", "revision_score", "customer_quality_score"], "component_delta_explanation": "Finalized financing is better evidence than a conditional commitment, but it remains a Stage2 financing/capacity route until utilization and battery margin bridge confirm.", "MFE_90D_pct": 15.49, "MAE_90D_pct": -23.64, "score_return_alignment_label": "high_MAE_policy_financing_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C13-LGES-2024Q2-AMPC-CAPACITY-PACING", "trigger_id": "TR-C13-LGES-20241028-Q3-CONSERVATIVE-2025-4B-OVERLAY", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 8, "revision_score": 12, "relative_strength_score": 12, "customer_quality_score": 12, "policy_or_regulatory_score": 13, "valuation_repricing_score": 10, "execution_risk_score": 16, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage4B-Watch", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 7, "revision_score": 10, "relative_strength_score": 10, "customer_quality_score": 11, "policy_or_regulatory_score": 12, "valuation_repricing_score": 9, "execution_risk_score": 18, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage4B-Overlay / not hard 4C", "changed_components": ["policy_or_regulatory_score", "execution_risk_score", "margin_bridge_score", "revision_score", "customer_quality_score"], "component_delta_explanation": "The later LGES trigger is a cleaner non-price 4B overlay than the July risk trigger; it supports overlay timing, not a new independent case.", "MFE_90D_pct": 2.52, "MAE_90D_pct": -25.45, "score_return_alignment_label": "good_non_price_4B_overlay_after_rebound", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R3", "loop": "63", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "avg=28.0; all three representative cases are new symbol/trigger-family coverage for C13; no same symbol+same trigger repetition", "tested_existing_calibrated_axes": ["full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_yellow_total_min", "stage3_green_total_min"], "residual_error_types_found": ["policy_JV_false_positive", "4B_too_early_without_cancel", "conditional_financing_overpromotion"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "C13 direct AMPC/JV utilization coverage absent in accessible search snapshot"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = R3_loop_64_C14_EV_DEMAND_SLOWDOWN_4B_4C
recommended_objective = holdout_validation + 4C_thesis_break_timing_test + counterexample_mining
reason = C13 now has direct utilization-gate coverage; C14 should validate whether demand slowdown evidence deserves hard 4C or only 4B watch.
```

## 28. Source Notes

Price source notes:

```text
- manifest: atlas/manifest.json
- schema: atlas/schema.json
- LGES profile: atlas/symbol_profiles/373/373220.json
- Samsung SDI profile: atlas/symbol_profiles/006/006400.json
- SK Innovation profile: atlas/symbol_profiles/096/096770.json
- all price paths: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv
```

Evidence source notes:

```text
- Reuters, 2024-07-25, LGES cuts sales target on weak EV demand, flags US election risk.
- Reuters, 2024-10-28, Battery maker LGES offers measured 2025 outlook after slow EV demand drags down Q3 profit.
- Reuters, 2024-12-02, US proposes $7.54 billion loan to Stellantis, Samsung SDI battery joint venture.
- Reuters, 2024-12-16, US finalizes $9.63 billion loan for Ford, SK On joint battery venture.
```
