# E2R Stock-Web v12 Residual Research — R4 / L4 / C16

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 0. Executive metadata

```text
selected_round = R4
selected_loop = 106
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = STRATEGIC_RESOURCE_OFFTAKE_RECYCLING_AND_SUPPLY_CHAIN_CASH_BRIDGE_VS_RESOURCE_LABEL_BLOWOFF
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

This run follows the v12 constraint that the output is only a standalone historical calibration / sector-archetype residual research Markdown file. It does not open `stock_agent` source code, patch production scoring, run live scans, or create a watchlist.

The chosen archetype is `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`. The No-Repeat Index shows C16 at 30 rows, still 20 rows short of the 50-row practical calibration target. The stated research point is strategic-resource policy plus actual offtake / margin / supply-chain execution. This run avoids the prior C16 symbol set that already used POSCO Holdings, LS, and Geumyang, and instead uses POSCO International, SungEel HiTech, and Cosmo Chemical.

## 1. Price source validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

The manifest confirms `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `max_date = 2026-02-20`, `tradable_row_count = 14354401`, `symbol_count = 5414`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.

## 2. Archetype thesis

C16 is not “anything related to lithium, nickel, graphite, copper, cobalt, rare earths, or recycling.” The useful separator is narrower:

```text
C16 positive path =
    explicit resource control / offtake / processing capacity / recycling feedstock / customer conversion
    + plausible margin or cash conversion
    + price action that does not immediately become pure 4B/4C blowoff

C16 false-positive path =
    resource label, policy headline, battery recycling theme, or commodity scarcity beta
    without company-specific offtake, processing ramp, funding, or margin bridge
```

The mechanism is similar to a port crane versus a warehouse sticker. A real C16 trigger has a crane: material moves through a contracted route and becomes revenue or margin. A weak C16 trigger only has a sticker that says “critical minerals,” but no loading schedule, no buyer, no conversion margin, and no proof that the warehouse is not empty.

## 3. Case set

### Case 1 — POSCO International (`047050`) — positive but 4B watch

```text
case_id = C16_047050_2023_RESOURCE_TRADING_ENERGY_ECO_MATERIAL_BRIDGE
ticker = 047050
name = POSCO International
trigger_family = energy_resource_trading_and_eco_material_supply_chain_bridge
trigger_date = 2023-07-14
entry_date = 2023-07-14
entry_price = 48450
post_entry_peak_date = 2023-07-26
post_entry_peak_price = 96700
post_entry_trough_date = 2023-07-14
post_entry_trough_price = 46050
MFE_pct = +99.59
MAE_pct = -4.95
classification = positive_with_full_4b_watch
calibration_usable = true
```

Evidence logic: POSCO International is structurally closer to a C16 bridge than a simple resource-label stock because the company is an energy/resource development and international trading platform, and after the POSCO Energy merger it carries an integrated energy/resource and eco-friendly materials narrative rather than only a short-lived commodity keyword. The price path supports “positive but full 4B watch,” not clean Green: the stock nearly doubled from the 2023-07-14 entry to the 2023-07-26 high, so the move was powerful but also blowoff-prone.

Price rows used:
- 2023-07-14: close 48,450; high 50,400; low 46,050.
- 2023-07-26: high 96,700; close 85,100.
- 2023-07-27: low 65,000; close 66,600, confirming sharp post-peak volatility.

Calibration interpretation:
```text
current_profile_error = partial
error_type = full_4b_risk_underestimated_if_resource_bridge_is_overweighted
profile_expected = Stage2_Actionable_or_Yellow_with_4B_watch
profile_wrong_if = Stage3_Green_without_company_specific_cash_bridge_and_event_cap
```

### Case 2 — SungEel HiTech (`365340`) — recycling-policy label hard counterexample

```text
case_id = C16_365340_2023_BATTERY_RECYCLING_POLICY_LABEL_FADE
ticker = 365340
name = SungEel HiTech
trigger_family = battery_recycling_critical_mineral_policy_label
trigger_date = 2023-03-02
entry_date = 2023-03-02
entry_price = 178500
post_entry_peak_date = 2023-03-06
post_entry_peak_price = 187500
post_entry_trough_date = 2023-10-31
post_entry_trough_price = 94200
MFE_pct = +5.04
MAE_pct = -47.23
classification = hard_counterexample_4c
calibration_usable = true
```

Evidence logic: battery recycling has true strategic value because black mass can be processed back into lithium, nickel, cobalt, manganese, copper, and graphite supply chains, and policy frameworks such as IRA/EU battery rules can favor recyclates. But the stock path shows that recycling-policy vocabulary alone was not enough. From the March 2023 spike, the forward path carried very low MFE and severe MAE.

Price rows used:
- 2023-03-02: close 178,500; high 186,000.
- 2023-03-06: high 187,500.
- 2023-10-31: low 94,200; close 94,700.

Calibration interpretation:
```text
current_profile_error = true
error_type = policy_recycling_label_too_easily_routes_to_stage2_actionable
profile_expected = Stage1_or_Stage2_watch_with_4C_guard
profile_wrong_if = Stage2_Actionable_without_feedstock_customer_margin_bridge
```

### Case 3 — Cosmo Chemical (`005420`) — cobalt/nickel recycling blowoff counterexample

```text
case_id = C16_005420_2023_COBALT_NICKEL_RECYCLING_RESOURCE_LABEL_BLOWOFF
ticker = 005420
name = Cosmo Chemical
trigger_family = cobalt_nickel_recycling_and_secondary_battery_resource_label
trigger_date = 2023-04-03
entry_date = 2023-04-03
entry_price = 64800
post_entry_peak_date = 2023-04-10
post_entry_peak_price = 94600
post_entry_trough_date = 2023-06-29
post_entry_trough_price = 46000
MFE_pct = +45.99
MAE_pct = -29.01
classification = high_MFE_high_MAE_resource_label_blowoff_counterexample
calibration_usable = true
```

Evidence logic: Cosmo Chemical’s route is the classic C16 trap. It had enough cobalt/nickel/recycling language to produce a strong short-term MFE, but not enough verified conversion bridge to keep the path from becoming a drawdown machine. A scoring model that only sees “resource + recycling + policy” will over-score this unless it demands actual feedstock, offtake, funding, operating ramp, and margin conversion.

Price rows used:
- 2023-04-03: close 64,800; high 64,800.
- 2023-04-10: high 94,600.
- 2023-06-29: low 46,000; close 46,100.

Calibration interpretation:
```text
current_profile_error = true
error_type = high_MFE_disguises_low_quality_resource_label
profile_expected = Stage2_Actionable_event_cap_or_4B_watch
profile_wrong_if = Stage3_Yellow_or_Green_on_resource_label_alone
```

### Narrative-only blocked comparator — STX (`011810`)

```text
case_id = C16_011810_2023_NICKEL_LITHIUM_LABEL_BLOCKED
ticker = 011810
name = STX
trigger_family = nickel_lithium_resource_trading_label
calibration_usable = false
blocked_reason = corporate_action_contaminated_window
```

STX was considered because the price path and story fit a resource-label blowoff, but the profile includes corporate-action candidate dates in 2023-09-15 and 2024-01-05, and the symbol profile flags major raw discontinuity. Under v12 rules, this belongs in narrative-only / blocked comparator space, not in the calibration aggregate.

## 4. Aggregate result

```json
{
  "aggregate_id": "R4_L4_C16_LOOP_106_AGG",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "blocked_narrative_only_count": 1,
  "current_profile_error_count": 3,
  "average_MFE_pct": 50.21,
  "average_MAE_pct": -27.06,
  "main_separator": "resource_supply_offtake_cash_bridge_vs_resource_label_blowoff"
}
```

The aggregate is intentionally asymmetric: one powerful positive case, two severe counterexamples, and one blocked comparator. This is appropriate for C16 because strategic-resource narratives can be explosive, but the same explosion often means price-only 4B unless there is a hard bridge from policy/resource label to contracted supply and cash conversion.

## 5. Raw component score simulation

### Current calibrated profile stress test

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

### Proposed C16 overlay

```text
c16_resource_supply_bridge_score =
    +2.0 if signed/offtake/customer contract exists
    +1.5 if processing/ramp capacity is already operating or near-commissioned
    +1.5 if feedstock source is secured and not merely aspirational
    +1.0 if margin/cash conversion is visible within 2 reporting periods
    -2.0 if evidence is only resource-label, policy-label, recycling-label, or commodity scarcity headline
    -2.0 if MFE is high but MAE exceeds 25% inside the 180D window
    -3.0 if corporate-action contamination, M&A contamination, or pure beta theme dominates
```

### Stage routing impact

```text
if C16 label exists but no company-specific offtake/feedstock/processing/cash bridge:
    cap_stage = Stage2_watch
    block_stage3_green = true

if MFE_30D >= 40% and MAE_180D <= -25%:
    route_to = high_MFE_high_MAE_4B_or_4C_review

if resource supply bridge is verified and early MAE <= -10%:
    allow_stage2_actionable = true
    allow_stage3_yellow = true only with revision or cash conversion
    stage3_green_requires = signed/customer/offtake + margin bridge + non-price evidence
```

## 6. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C16_047050_2023_RESOURCE_TRADING_ENERGY_ECO_MATERIAL_BRIDGE","ticker":"047050","name":"POSCO International","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","trigger_family":"energy_resource_trading_and_eco_material_supply_chain_bridge","entry_date":"2023-07-14","entry_price":48450,"peak_date":"2023-07-26","peak_price":96700,"trough_date":"2023-07-14","trough_price":46050,"mfe_pct":99.59,"mae_pct":-4.95,"classification":"positive_with_full_4b_watch","calibration_usable":true}
{"row_type":"case","case_id":"C16_365340_2023_BATTERY_RECYCLING_POLICY_LABEL_FADE","ticker":"365340","name":"SungEel HiTech","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","trigger_family":"battery_recycling_critical_mineral_policy_label","entry_date":"2023-03-02","entry_price":178500,"peak_date":"2023-03-06","peak_price":187500,"trough_date":"2023-10-31","trough_price":94200,"mfe_pct":5.04,"mae_pct":-47.23,"classification":"hard_counterexample_4c","calibration_usable":true}
{"row_type":"case","case_id":"C16_005420_2023_COBALT_NICKEL_RECYCLING_RESOURCE_LABEL_BLOWOFF","ticker":"005420","name":"Cosmo Chemical","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","trigger_family":"cobalt_nickel_recycling_and_secondary_battery_resource_label","entry_date":"2023-04-03","entry_price":64800,"peak_date":"2023-04-10","peak_price":94600,"trough_date":"2023-06-29","trough_price":46000,"mfe_pct":45.99,"mae_pct":-29.01,"classification":"high_MFE_high_MAE_resource_label_blowoff_counterexample","calibration_usable":true}
{"row_type":"narrative_only","case_id":"C16_011810_2023_NICKEL_LITHIUM_LABEL_BLOCKED","ticker":"011810","name":"STX","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","trigger_family":"nickel_lithium_resource_trading_label","calibration_usable":false,"blocked_reason":"corporate_action_contaminated_window"}
{"row_type":"shadow_weight","rule_id":"c16_resource_supply_offtake_cash_bridge_required","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","proposal":"require company-specific offtake/feedstock/processing/cash bridge before Stage2-Actionable or higher","weight_delta_candidate":-2.0,"production_scoring_changed":false}
{"row_type":"residual_contribution","loop":"R4_L4_C16_loop_106","new_independent_case_count":3,"blocked_narrative_only_count":1,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"do_not_propose_new_weight_delta":false}
```

## 7. Residual contribution summary

```text
new_independent_case_count = 3
blocked_narrative_only_count = 1
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable case 수 = 3
calibration_usable trigger 수 = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 3
verified_url_repair_needed_count = 2
```

```text
diversity_score_summary =
  C16 Priority 1 보강 +
  POSCO International resource/energy supply-chain positive with 4B watch +
  SungEel HiTech recycling-policy low-MFE hard 4C +
  Cosmo Chemical cobalt/nickel recycling high-MFE/high-MAE blowoff +
  STX corporate-action-contaminated blocked comparator
```

```text
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C16 rows 30, 50-row target까지 20 부족
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c16_resource_supply_offtake_processing_cash_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C16 strategic-resource/resource-label rallies
existing_axis_weakened = null
next_recommended_archetypes = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C15_MATERIAL_SPREAD_SUPERCYCLE
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.
Do not execute this handoff during the research session that generated this MD.

Batch-ingest this MD as one v12 residual research artifact.
Extract the JSONL rows under "Machine-readable JSONL rows".
Do not change production scoring immediately.
Add only shadow-rule candidates and calibration rows.

Candidate shadow rule:
- rule_id: c16_resource_supply_offtake_processing_cash_bridge_required_for_stage2_actionable_shadow_only
- scope: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
- behavior:
  1. If C16 evidence is only resource label / policy label / recycling label / commodity scarcity headline, cap at Stage2_watch.
  2. Require at least one hard bridge among signed offtake/customer contract, secured feedstock, processing ramp, operating capacity, or cash/margin conversion before Stage2-Actionable.
  3. If MFE is high but MAE_180D <= -25%, route to high_MFE_high_MAE_4B_or_4C_review.
  4. Corporate-action-contaminated resource-label spikes must remain narrative-only / rejected for calibration.

Suggested tests:
- POSCO International 2023 should remain positive but not clean Green without 4B watch.
- SungEel HiTech 2023 should be blocked from Stage2-Actionable on recycling-policy label alone.
- Cosmo Chemical 2023 should become high-MFE/high-MAE blowoff counterexample.
- STX 2023 should be rejected or narrative-only if corporate-action contamination overlaps the forward calibration window.
```
