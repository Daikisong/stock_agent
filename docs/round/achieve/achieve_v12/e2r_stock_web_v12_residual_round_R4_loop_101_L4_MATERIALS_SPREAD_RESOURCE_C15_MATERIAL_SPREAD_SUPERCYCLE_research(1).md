# E2R v12 Residual Calibration Research — R4 / L4 / C15 Material Spread Supercycle

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R4
selected_loop = 101
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = NONFERROUS_COPPER_ZINC_AND_STEEL_SPREAD_ASP_MARGIN_BRIDGE_VS_COMMODITY_LABEL_GOVERNANCE_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Why this loop exists

C15 was still a shallow bucket in the no-repeat index: **C15_MATERIAL_SPREAD_SUPERCYCLE = 6 rows**, with 24 rows still needed to reach the 30-row minimum. The intended calibration question is not “did copper, zinc, steel, lithium, or gold go up?” The question is whether a commodity move became **company-level ASP, shipment volume, margin, working-capital, and FCF conversion**.

This loop therefore adds four independent historical trigger rows that deliberately mix:

- a true positive-like copper/defense-margin bridge,
- a governance/tender contaminant that can masquerade as a material supercycle,
- a steel/lithium label false positive,
- a rebar/scrap-spread counterexample where demand and inventory absorb the spread.

The useful rule shape is simple: commodity price is only the weather. C15 should score the roof, not the rain. A metal price move must enter the company’s P&L through sellable ASP, volumes, and cash conversion before it deserves positive Stage3 treatment.

---

## 2. Source validation scope

### 2.1 Allowed source boundary

This research used the v12 permitted scope only:

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
stock_web_price_atlas_access_required = true
stock_agent_research_artifact_access_purpose = coverage_gap_and_duplicate_avoidance_only
```

### 2.2 Price source files inspected

```text
Songdaiki/stock_agent/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
Songdaiki/stock_agent/docs/core/V12_Research_No_Repeat_Index.md
Songdaiki/stock-web/atlas/symbol_profiles/103/103140.json
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv
Songdaiki/stock-web/atlas/symbol_profiles/010/010130.json
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv
Songdaiki/stock-web/atlas/symbol_profiles/005/005490.json
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv
Songdaiki/stock-web/atlas/symbol_profiles/084/084010.json
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/084/084010/2024.csv
```

### 2.3 Validation caveats

```text
non_price_evidence_status = source_proxy_only
evidence_url_pending = true
price_rows_validated_from_stock_web = true
raw_unadjusted_price_caveat = true
corporate_action_windows_blocked_by_default = true
```

The stock-web profile caveat is preserved. POSCO홀딩스, 풍산, and 고려아연 had no corporate-action candidate caveat in the inspected windows. 대한제강 has historical corporate-action candidates, but the flagged dates are outside the 2024 window used here; the row is still marked with a calibration caveat because the profile reports a major raw discontinuity history.

---

## 3. Novelty / no-repeat check

| case_id | symbol | name | proposed trigger | no-repeat key | novelty decision |
|---|---:|---|---|---|---|
| C15-101-01 | 103140 | 풍산 | 2024-03-07 copper + defense margin bridge ignition | `C15_MATERIAL_SPREAD_SUPERCYCLE/103140/Stage2_Actionable/2024-03-07` | new C15 key; symbol may appear elsewhere but not as this C15 trigger |
| C15-101-02 | 010130 | 고려아연 | 2024-09-13 material label contaminated by control-premium/tender dynamics | `C15_MATERIAL_SPREAD_SUPERCYCLE/010130/Stage3_Yellow_Local4BWatch/2024-09-13` | new C15 key; intentionally cross-archetype contaminant vs C32 |
| C15-101-03 | 005490 | POSCO홀딩스 | 2024-02-01 steel/lithium beta rebound without margin conversion | `C15_MATERIAL_SPREAD_SUPERCYCLE/005490/Stage2_FalsePositive/2024-02-01` | new C15 key |
| C15-101-04 | 084010 | 대한제강 | 2024-02-05 rebar/scrap spread label absorbed by weak construction demand | `C15_MATERIAL_SPREAD_SUPERCYCLE/084010/Stage2_FalsePositive/2024-02-05` | new C15 key; profile caveat retained |

---

## 4. Trigger-level backtest results

All returns use the inspected 1D OHLC rows from stock-web. Entry price is the trigger-date close. MFE uses forward-window maximum high. MAE uses forward-window minimum low. Windows are treated as calendar-day forward windows over available trading rows.

| case | entry date | entry price | 30D MFE | 30D MAE | 90D MFE | 90D MAE | 180D MFE | 180D MAE | peak / trough note | label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 풍산 | 2024-03-07 | 46,100 | +16.7% | -3.9% | +71.1% | -3.9% | +71.1% | -3.9% | 2024-05-14 high 78,900 | positive |
| 고려아연 | 2024-09-13 | 666,000 | +20.3% | -1.7% | +131.7% | -1.7% | +131.7% | -1.7% | 2024-10-29 high 1,543,000; later peak drawdown >50% into 2025 | mixed / contaminant |
| POSCO홀딩스 | 2024-02-01 | 437,000 | +5.7% | -4.6% | +7.8% | -15.1% | +7.8% | -18.8% | 2024-06-28 low 355,000 inside 180D | counterexample |
| 대한제강 | 2024-02-05 | 14,000 | +1.8% | -8.2% | +1.8% | -8.6% | +1.8% | -19.3% | 2024-07-08 low 11,300 inside 180D | counterexample |

### 4.1 Case interpretation

#### C15-101-01 — 풍산 / positive bridge

풍산 is the clearest positive row in this set. The 2024-03-07 row was not merely a commodity-beta candle: it followed a copper-price and defense-demand narrative that could plausibly map into both metal ASP and munitions margin. The price path then behaved like a real Stage3 transition: low MAE, strong 90D follow-through, and a May peak above 70% MFE.

Calibration implication: C15 can allow Stage3-Yellow/Green only when commodity spread is paired with **company-level ASP/volume/margin bridge** or an adjacent backlog/defense margin bridge. Commodity price alone should not be enough.

#### C15-101-02 — 고려아연 / mixed positive but wrong archetype risk

고려아연 produced a spectacular price path after the 2024-09-13 trigger, but the mechanism was not clean C15. The row looks like a material spread supercycle if the model only sees “zinc/gold/silver smelter + price breakout.” Yet the actual market behavior was dominated by control-premium/tender/governance dynamics. That belongs closer to C32 than pure C15.

Calibration implication: C15 should have a **governance/tender contaminant detector**. If the trigger is dominated by tender price, control premium, minority-holder risk, or squeeze mechanics, C15 should not grant a clean materials-supercycle positive even when MFE is extreme. The right action is reroute or dual-tag with C32, then cap the C15 contribution.

#### C15-101-03 — POSCO홀딩스 / steel-lithium label false positive

POSCO홀딩스 shows why material labels are dangerous. A global steel/lithium recovery story can look attractive, but the inspected 2024 path did not produce positive 180D alignment. The stock had only shallow upside and then a deep MAE drawdown. This is exactly the false-positive shape the calibrated profile should suppress: price and macro headline are visible, but company-specific margin and FCF conversion are missing.

Calibration implication: C15 needs a hard bridge from commodity/recovery label to actual margin/FCF revision. Without it, Stage2-Actionable should remain capped and price-only blowoff should be blocked from positive Stage3.

#### C15-101-04 — 대한제강 / rebar-scrap spread absorbed by demand weakness

대한제강 is a negative calibration row. Even if rebar/scrap spread temporarily improves, construction demand and inventory pressure can eat the spread before it reaches equity returns. The 180D MFE stayed below 2% while MAE exceeded -19%. This is a classic spread-label trap: the spread exists, but the customer channel cannot digest it.

Calibration implication: C15 must require end-demand or volume confirmation for steel/rebar cases. Spread alone is not enough because weak demand turns better input cost into idle capacity, receivable risk, and valuation compression.

---

## 5. Current calibrated profile stress test

Current profile proxy:

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

### 5.1 Residual errors found

| error_id | residual failure mode | affected cases | current profile risk | proposed correction |
|---|---|---|---|---|
| C15-E01 | commodity headline without company margin bridge can still look actionable | POSCO홀딩스, 대한제강 | false Stage2-Actionable / local 4B watch | require ASP/volume/margin/FCF bridge before Stage2-Actionable bonus |
| C15-E02 | governance/tender squeeze can masquerade as material supercycle | 고려아연 | wrong-archetype positive; inflated C15 MFE credit | route to C32 or dual-tag and cap C15 contribution |
| C15-E03 | mixed copper + defense case deserves positive score but not from commodity price alone | 풍산 | under-explains success if only C15 spread score is used | allow bridge credit when metal ASP and backlog/margin evidence co-exist |
| C15-E04 | local 4B after commodity spike can still be price-only | 고려아연, POSCO홀딩스, 대한제강 | local 4B over-trust | enforce `full_4b_requires_non_price_evidence` and add C15-specific late-chase high-MAE guard |

### 5.2 Score-return alignment

| case | old likely behavior | corrected behavior | reason |
|---|---|---|---|
| 풍산 | Stage2-Actionable or weak Stage3-Yellow | Stage3-Yellow eligible; Green only if margin/FCF revision is verified | price path supports positive, but mechanism needs bridge evidence |
| 고려아연 | Stage3-Green if MFE-only | C15 capped / reroute to C32 governance-control premium | extreme MFE is real but not a pure material spread event |
| POSCO홀딩스 | Stage2-Actionable by steel/lithium label | Stage2 only or 4B-watch if price extended | return alignment is poor without margin bridge |
| 대한제강 | Stage2 by spread label | Stage2 false-positive / 4C watch if demand deterioration appears | weak volume/demand destroys spread translation |

---

## 6. Raw component score breakdown simulation

These are shadow-only calibration rows. They do not change production scoring.

```jsonl
{"row_type":"score_simulation","case_id":"C15-101-01","symbol":"103140","name":"풍산","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","trigger_date":"2024-03-07","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores":{"price_momentum":22.0,"volume_attention":13.0,"revision_or_margin_bridge":18.0,"cross_evidence":11.0,"risk_penalty":-3.0,"stage2_actionable_bonus":2.0},"simulated_total":63.0,"corrected_total_with_C15_bridge":77.0,"corrected_stage":"Stage3-Yellow","rationale":"positive price path is supported only when copper ASP plus defense/backlog margin bridge is present"}
{"row_type":"score_simulation","case_id":"C15-101-02","symbol":"010130","name":"고려아연","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","trigger_date":"2024-09-13","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores":{"price_momentum":29.0,"volume_attention":18.0,"revision_or_margin_bridge":8.0,"cross_evidence":9.0,"governance_contaminant_penalty":-14.0,"stage2_actionable_bonus":0.0},"simulated_total":50.0,"corrected_total_with_C15_cap":58.0,"corrected_stage":"C32_REROUTE_OR_C15_CAP","rationale":"MFE was extreme but mechanism was governance/tender/control-premium rather than clean material spread"}
{"row_type":"score_simulation","case_id":"C15-101-03","symbol":"005490","name":"POSCO홀딩스","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","trigger_date":"2024-02-01","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores":{"price_momentum":11.0,"volume_attention":8.0,"revision_or_margin_bridge":4.0,"cross_evidence":5.0,"risk_penalty":-11.0,"stage2_actionable_bonus":0.0},"simulated_total":17.0,"corrected_stage":"Stage2_FalsePositive","rationale":"steel/lithium recovery label lacked 90D/180D return alignment"}
{"row_type":"score_simulation","case_id":"C15-101-04","symbol":"084010","name":"대한제강","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","trigger_date":"2024-02-05","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","raw_component_scores":{"price_momentum":5.0,"volume_attention":3.0,"revision_or_margin_bridge":2.0,"cross_evidence":3.0,"demand_absorption_penalty":-13.0,"stage2_actionable_bonus":0.0},"simulated_total":0.0,"corrected_stage":"Stage2_FalsePositive_OR_4C_Watch","rationale":"spread label was absorbed by weak rebar demand and produced poor MFE/MAE alignment"}
```

---

## 7. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","case_id":"C15-101-01","symbol":"103140","name":"풍산","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NONFERROUS_COPPER_ZINC_AND_STEEL_SPREAD_ASP_MARGIN_BRIDGE_VS_COMMODITY_LABEL_GOVERNANCE_FALSE_POSITIVE","trigger_type":"Stage2_Actionable","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":46100.0,"entry_price_field":"close","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","mfe_30d_pct":16.70,"mae_30d_pct":-3.90,"mfe_90d_pct":71.15,"mae_90d_pct":-3.90,"mfe_180d_pct":71.15,"mae_180d_pct":-3.90,"peak_date":"2024-05-14","peak_high":78900.0,"peak_mfe_pct":71.15,"max_drawdown_after_peak_pct":-27.38,"classification":"positive","current_profile_error":"success_under_explained_without_company_margin_bridge","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","case_id":"C15-101-02","symbol":"010130","name":"고려아연","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NONFERROUS_COPPER_ZINC_AND_STEEL_SPREAD_ASP_MARGIN_BRIDGE_VS_COMMODITY_LABEL_GOVERNANCE_FALSE_POSITIVE","trigger_type":"Stage3_Yellow_Local4BWatch","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000.0,"entry_price_field":"close","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv + 2025.csv","mfe_30d_pct":20.27,"mae_30d_pct":-1.65,"mfe_90d_pct":131.68,"mae_90d_pct":-1.65,"mfe_180d_pct":131.68,"mae_180d_pct":-1.65,"peak_date":"2024-10-29","peak_high":1543000.0,"peak_mfe_pct":131.68,"max_drawdown_after_peak_pct":-54.89,"classification":"mixed_positive_wrong_archetype_contaminant","current_profile_error":"extreme_MFE_can_overcredit_C15_when_governance_tender_controls_path","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","case_id":"C15-101-03","symbol":"005490","name":"POSCO홀딩스","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NONFERROUS_COPPER_ZINC_AND_STEEL_SPREAD_ASP_MARGIN_BRIDGE_VS_COMMODITY_LABEL_GOVERNANCE_FALSE_POSITIVE","trigger_type":"Stage2_FalsePositive","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":437000.0,"entry_price_field":"close","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv","mfe_30d_pct":5.72,"mae_30d_pct":-4.58,"mfe_90d_pct":7.78,"mae_90d_pct":-15.10,"mfe_180d_pct":7.78,"mae_180d_pct":-18.76,"peak_date":"2024-03-05","peak_high":471000.0,"peak_mfe_pct":7.78,"max_drawdown_after_peak_pct":-24.63,"classification":"counterexample","current_profile_error":"steel_lithium_material_label_without_margin_FCF_bridge","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","case_id":"C15-101-04","symbol":"084010","name":"대한제강","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NONFERROUS_COPPER_ZINC_AND_STEEL_SPREAD_ASP_MARGIN_BRIDGE_VS_COMMODITY_LABEL_GOVERNANCE_FALSE_POSITIVE","trigger_type":"Stage2_FalsePositive","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":14000.0,"entry_price_field":"close","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/084/084010/2024.csv","mfe_30d_pct":1.79,"mae_30d_pct":-8.21,"mfe_90d_pct":1.79,"mae_90d_pct":-8.57,"mfe_180d_pct":1.79,"mae_180d_pct":-19.29,"peak_date":"2024-02-19","peak_high":14250.0,"peak_mfe_pct":1.79,"max_drawdown_after_peak_pct":-20.70,"classification":"counterexample","current_profile_error":"spread_label_absorbed_by_weak_demand_and_inventory_channel","source_proxy_only":true,"evidence_url_pending":true,"profile_caveat":"corporate_action_candidate_history_outside_2024_window"}
```

---

## 8. Aggregate row

```jsonl
{"row_type":"aggregate","selected_round":"R4","selected_loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":4,"auto_selected_coverage_gap_static_index":"C15 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30","do_not_propose_new_weight_delta":false,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate"}
```

---

## 9. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","rule_id":"C15_company_ASP_volume_margin_FCF_bridge_required","target":"C15_MATERIAL_SPREAD_SUPERCYCLE","proposed_effect":"require at least one company-level bridge before Stage2-Actionable bonus and at least two bridges before Stage3-Green","status":"candidate_only","production_scoring_changed":false}
{"row_type":"shadow_weight","rule_id":"C15_governance_tender_contaminant_reroute_or_cap","target":"C15_MATERIAL_SPREAD_SUPERCYCLE","proposed_effect":"if tender/control-premium/minority-holder mechanics dominate, cap C15 contribution and route to C32 governance-control premium","status":"candidate_only","production_scoring_changed":false}
{"row_type":"shadow_weight","rule_id":"C15_material_label_high_MAE_guard","target":"C15_MATERIAL_SPREAD_SUPERCYCLE","proposed_effect":"commodity label with 90D MAE worse than -12% and no margin bridge should remain Stage2 false-positive or 4B watch","status":"candidate_only","production_scoring_changed":false}
{"row_type":"shadow_weight","rule_id":"C15_steel_rebar_demand_absorption_guard","target":"C15_MATERIAL_SPREAD_SUPERCYCLE","proposed_effect":"steel/rebar spread requires end-demand, shipment, inventory, and receivable confirmation; otherwise spread improvement is not scored as supercycle","status":"candidate_only","production_scoring_changed":false}
```

### 9.1 Suggested pseudo-logic

```text
IF canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE:
    material_price_headline_only = commodity_price_up AND NOT company_margin_bridge
    company_margin_bridge = ASP_or_spread_evidence + volume_or_backlog_evidence + FCF_or_OPM_revision
    governance_contaminant = tender_offer OR control_premium OR minority_holder_risk OR squeeze_mechanics

    IF governance_contaminant:
        cap_C15_positive_contribution
        add_or_reroute_to_C32

    IF material_price_headline_only:
        block_stage2_actionable_bonus
        block_stage3_green

    IF steel_or_rebar AND weak_end_demand_or_inventory_pressure:
        route_to_stage2_false_positive_or_4C_watch

    IF company_margin_bridge >= 2 AND 90D_MFE_positive AND 90D_MAE_controlled:
        allow_stage3_yellow

    IF company_margin_bridge >= 3 AND revision_score >= 55 AND no_4B_price_only:
        allow_stage3_green_candidate
```

---

## 10. Residual contribution summary

```text
new_axis_proposed = C15_company_ASP_volume_margin_FCF_bridge_required | C15_governance_tender_contaminant_reroute_or_cap | C15_steel_rebar_demand_absorption_guard | C15_material_label_high_MAE_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

This loop adds four C15 rows and strengthens the distinction between a real material supercycle and a commodity-label echo. The key residual is not a lack of price confirmation; the key residual is **misattribution**. A model that sees only price and commodity nouns will over-credit POSCO-style and 고려아연-style rows, while under-explaining 풍산-style rows where the bridge to company margin is real.

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent for stock_agent. Do not execute this prompt during the research run that generated this MD.

Read this MD as one standalone v12 residual research artifact:
- round: R4
- large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
- canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
- file: e2r_stock_web_v12_residual_round_R4_loop_101_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

Batch-ingest the JSONL rows under sections 6-9 only after checking against the central no-repeat registry.

Do not patch production scoring immediately from a single MD. Instead, add these rows to the calibration corpus and evaluate whether the following C15-specific shadow rules are supported across a larger sample:
1. C15_company_ASP_volume_margin_FCF_bridge_required
2. C15_governance_tender_contaminant_reroute_or_cap
3. C15_material_label_high_MAE_guard
4. C15_steel_rebar_demand_absorption_guard

Preserve these constraints:
- production_scoring_changed = false unless batch review accepts the rule.
- source_proxy_only rows remain low-confidence until evidence URLs are attached.
- never treat extreme MFE alone as positive Stage3 evidence.
- keep C32 governance-control premium distinct from C15 material spread unless dual-tagging is explicitly supported.
```

---

## 12. Final metadata

```text
selected_round = R4
selected_loop = 101
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = NONFERROUS_COPPER_ZINC_AND_STEEL_SPREAD_ASP_MARGIN_BRIDGE_VS_COMMODITY_LABEL_GOVERNANCE_FALSE_POSITIVE
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable case count = 4
calibration_usable trigger count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4
auto_selected_coverage_gap_static_index = C15 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
source_proxy_only = true
evidence_url_pending = true
next_recommended_archetypes = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```
