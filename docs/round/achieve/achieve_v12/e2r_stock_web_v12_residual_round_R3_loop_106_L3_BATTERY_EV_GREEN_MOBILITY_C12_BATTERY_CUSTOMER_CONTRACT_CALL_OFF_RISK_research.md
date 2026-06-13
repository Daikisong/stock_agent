# E2R Stock-Web V12 Residual Research — R3 / C12 Battery Customer Contract Call-Off Risk / Sixth Holdout

```yaml
research_session: "post_calibrated_sector_archetype_residual_research"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R3"
selected_loop: 106
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 1 static ledger C12 rows=32 / need-to-50=18; current-session C12 already above 50, so this loop is a new-symbol quality holdout"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L3_BATTERY_EV_GREEN_MOBILITY"
canonical_archetype_id: "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK"
fine_archetype_id: "mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106"
output_filename: "e2r_stock_web_v12_residual_round_R3_loop_106_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"
price_source: "Songdaiki/stock-web"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

The static No-Repeat Index still shows C12 as a Priority 1 archetype, but the current interactive session has already produced several C12 passes. This file therefore avoids the earlier C12 symbol set and focuses on a fresh C12 failure mode: customer order or capacity evidence that still needs shipment, revenue-recognition, ASP/margin, utilization and call-off clearance.

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Current-session C12 symbols avoided include `222080`, `137400`, `299030`, `277880`, `382840`, `003670`, `083930`, `282880`, `217820`, `290670`, `382480`, `096770`, `002710`, `014820`, `001530`, `091580`, `078600`, `247540`, `336370`, `011790`, `051910`, `066970`, `361610`, `393890`, `267320`, `259630`, `372170`, `378340`, `101360`, `278280`.

New C12 symbols in this file:

```text
348370, 005070, 121600, 001780, 093370, 079810
```

## 2. Stock-Web price basis

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_path: atlas/schema.json
```

MFE/MAE uses the Stock-Web schema: max high or min low from the entry date through the next 30/90/180 tradable rows, divided by entry close. Candidate windows were checked against each symbol profile. Corporate-action candidate dates for these rows do not overlap the 180D windows.

## 3. Case summary table

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | drawdown_after_peak | current_profile_verdict | label |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| C12_R3_L106_348370_ENYCHEM_NORTH_AMERICA_ELECTROLYTE_CUSTOMER_SUPPLY_POSITIVE | 348370 | 엔켐 | Stage3-Yellow | 2024-01-25 | 113600 | 215.581 | -5.5458 | 247.2711 | -5.5458 | 247.2711 | -5.5458 | 2024-04-08 | -62.2307 | current_profile_missed_structural_then_needs_local_4b_overlay | positive |
| C12_R3_L106_005070_COSMO_CATHODE_CAPA_EXPANSION_STAGE2_GUARD | 005070 | 코스모신소재 | Stage2-Actionable | 2023-09-20 | 162700 | 11.2477 | -18.0086 | 11.2477 | -22.2495 | 19.4222 | -22.2495 | 2024-02-21 | -29.5934 | current_profile_correct_if_capped_at_stage2_watch | positive_with_guardrail |
| C12_R3_L106_121600_NANO_CNT_CUSTOMER_VOLUME_CALLOFF_COUNTEREXAMPLE | 121600 | 나노신소재 | Stage2-Actionable | 2024-07-23 | 95200 | 5.042 | -28.0462 | 5.042 | -37.7101 | 5.042 | -49.8424 | 2024-07-23 | -52.25 | current_profile_false_positive_if_stage3_opened | counterexample |
| C12_R3_L106_001780_ALUKO_LGES_MODULE_CASE_ORDER_CHASM_COUNTEREXAMPLE | 001780 | 알루코 | Stage2-Actionable | 2024-03-26 | 3830 | 18.0157 | -16.5796 | 18.0157 | -43.6031 | 18.0157 | -54.1775 | 2024-03-26 | -61.1726 | current_profile_false_positive_without_EV_demand_and_margin_gate | counterexample |
| C12_R3_L106_093370_FOOSUNG_LIPF6_CUSTOMER_INVENTORY_STOP_4C | 093370 | 후성 | Stage4C | 2023-04-17 | 14890 | 4.0967 | -15.7824 | 4.0967 | -26.1249 | 4.0967 | -35.863 | 2023-04-18 | -38.3871 | current_profile_4c_success_if_routed_immediately | counterexample |
| C12_R3_L106_079810_DNT_LGES_NOTCHING_PROCESS_SHIFT_4B_COUNTEREXAMPLE | 079810 | 디이엔티 | Stage4B | 2023-10-20 | 20750 | 10.8434 | -24.3373 | 10.8434 | -45.7831 | 10.8434 | -51.8072 | 2023-11-06 | -56.5217 | current_profile_false_positive_if_customer_spec_change_not_discounted | counterexample |

## 4. Core finding

C12 needs a stricter distinction between **customer existence** and **customer conversion**. A named customer, a supply route, or a capacity plan is only the purchase order on the desk. The rerating engine should wait for the goods to move through the factory gate: delivery timing, shipment, revenue recognition, ASP/margin bridge and call-off/inventory clearance.

```text
customer / capacity / supply headline
  -> explicit shipment or delivery timing
  -> revenue recognition
  -> ASP / margin bridge
  -> utilization, inventory, call-off risk clearance
  -> only then Stage3-Yellow / Green eligibility
```

Enchem is the positive anchor: customer list and North America supply conversion produced a large MFE. Cosmo Advanced Materials is a Stage2-positive-but-not-Stage3 row. Nano Tim, Aluko and DNT are high-MAE counterexamples where product/customer headlines lacked enough conversion evidence. Foosung is the hard-protection row: explicit customer inventory adjustment and LiPF6 production stoppage should route to Stage4C, not remain a hopeful Stage2.

Aggregate path:

```yaml
calibration_usable_rows: 6
representative_rows: 6
positive_case_count: 2
counterexample_count: 4
4B_case_count: 6
4C_case_count: 1
avg_MFE_90D_pct: 49.4194
avg_MAE_90D_pct: -30.1694
avg_MFE_180D_pct: 50.7818
avg_MAE_180D_pct: -36.5809
current_profile_error_count: 4
```

## 5. Case notes

### C12_R3_L106_348370_ENYCHEM_NORTH_AMERICA_ELECTROLYTE_CUSTOMER_SUPPLY_POSITIVE — 엔켐 (348370)

- Evidence date / source: `2024-01-25` — https://www.thelec.kr/news/articleView.html?idxno=25553
- Evidence: North America electrolyte supply: Georgia plant capacity expansion and shipments to LGES, SK On, Ultium Cells and BlueOvalSK customers.
- Price path: entry `2024-01-25` at `113600`; MFE/MAE 180D `247.2711` / `-5.5458`; peak `2024-04-08` at `394500`; post-peak drawdown `-62.2307`.
- Interpretation: This is the positive anchor: customer supply and capacity route were unusually explicit, but the fast rerating still needs a local 4B exit overlay.

### C12_R3_L106_005070_COSMO_CATHODE_CAPA_EXPANSION_STAGE2_GUARD — 코스모신소재 (005070)

- Evidence date / source: `2023-09-19` — https://securities.miraeasset.com/bbs/download/2119218.pdf?attachmentId=2119218
- Evidence: Cathode capacity expansion and 2024 revenue challenge narrative; customer demand existed, but delivery, utilization and margin conversion were still incomplete at entry.
- Price path: entry `2023-09-20` at `162700`; MFE/MAE 180D `19.4222` / `-22.2495`; peak `2024-02-21` at `194300`; post-peak drawdown `-29.5934`.
- Interpretation: Stage2 evidence was real, but the forward path did not justify a clean Stage3 without shipment and margin confirmation.

### C12_R3_L106_121600_NANO_CNT_CUSTOMER_VOLUME_CALLOFF_COUNTEREXAMPLE — 나노신소재 (121600)

- Evidence date / source: `2024-07-23` — https://securities.miraeasset.com/bbs/download/2129977.pdf?attachmentId=2129977
- Evidence: CNT conductive additive volume growth and new customer volume thesis; customer adoption was real but forward price path punished unconfirmed shipment/margin timing.
- Price path: entry `2024-07-23` at `95200`; MFE/MAE 180D `5.042` / `-49.8424`; peak `2024-07-23` at `100000`; post-peak drawdown `-52.25`.
- Interpretation: C12 should not treat CNT adoption language as a customer-contract conversion unless purchase timing, shipment, ASP and margin are visible.

### C12_R3_L106_001780_ALUKO_LGES_MODULE_CASE_ORDER_CHASM_COUNTEREXAMPLE — 알루코 (001780)

- Evidence date / source: `2024-03-26` — https://v.daum.net/v/7rOw1YSgdQ
- Evidence: LG Energy Solution end-plate / module-case supply and large accumulated order narrative; EV chasm and Europe weakness later exposed revenue/margin bridge risk.
- Price path: entry `2024-03-26` at `3830`; MFE/MAE 180D `18.0157` / `-54.1775`; peak `2024-03-26` at `4520`; post-peak drawdown `-61.1726`.
- Interpretation: A named customer order can still fail C12 if the downstream demand and margin path cannot absorb customer timing risk.

### C12_R3_L106_093370_FOOSUNG_LIPF6_CUSTOMER_INVENTORY_STOP_4C — 후성 (093370)

- Evidence date / source: `2023-04-14` — https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20230810000585&docno=&method=searchInitInfo
- Evidence: LiPF6 production stop due to electrolyte customer inventory adjustment, company inventory increase and cost burden reduction.
- Price path: entry `2023-04-17` at `14890`; MFE/MAE 180D `4.0967` / `-35.863`; peak `2023-04-18` at `15500`; post-peak drawdown `-38.3871`.
- Interpretation: This is the hard-protection row: explicit production stoppage from customer inventory adjustment is not just a 4B watch.

### C12_R3_L106_079810_DNT_LGES_NOTCHING_PROCESS_SHIFT_4B_COUNTEREXAMPLE — 디이엔티 (079810)

- Evidence date / source: `2023-10-20` — https://www.thelec.kr/news/articleView.html?idxno=23575
- Evidence: LGES notching-equipment process change from laser to press exposed single-customer and equipment-spec timing risk for DNT laser notching thesis.
- Price path: entry `2023-10-20` at `20750`; MFE/MAE 180D `10.8434` / `-51.8072`; peak `2023-11-06` at `23000`; post-peak drawdown `-56.5217`.
- Interpretation: This is a 4B-not-4C case: customer process changes can cap the thesis before there is a formal cancellation or company-wide thesis break.

## 6. Score component map

The component scores are research-proxy scores, not production values. They are used only to make the proposed C12 gate inspectable.

### 엔켐 (348370) component delta

```yaml
weighted_score_before: 74
stage_label_before: Stage2-Actionable
raw_component_scores_before: {"contract_score": 70, "backlog_visibility_score": 55, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 80, "customer_quality_score": 85, "policy_or_regulatory_score": 65, "valuation_repricing_score": 78, "execution_risk_score": 48, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 30, "accounting_trust_risk_score": 25}
weighted_score_after: 78
stage_label_after: Stage3-Yellow
raw_component_scores_after: {"contract_score": 82, "backlog_visibility_score": 68, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 78, "customer_quality_score": 90, "policy_or_regulatory_score": 65, "valuation_repricing_score": 64, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 30, "accounting_trust_risk_score": 25}
component_delta_explanation: "C12 gate discounts customer/headline evidence unless shipment, revenue recognition, ASP/margin bridge and call-off risk clearance are visible."
```

### 코스모신소재 (005070) component delta

```yaml
weighted_score_before: 69
stage_label_before: Stage2-Actionable
raw_component_scores_before: {"contract_score": 50, "backlog_visibility_score": 52, "margin_bridge_score": 35, "revision_score": 42, "relative_strength_score": 48, "customer_quality_score": 58, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 58, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 25, "accounting_trust_risk_score": 20}
weighted_score_after: 64
stage_label_after: Stage2
raw_component_scores_after: {"contract_score": 50, "backlog_visibility_score": 50, "margin_bridge_score": 30, "revision_score": 38, "relative_strength_score": 45, "customer_quality_score": 55, "policy_or_regulatory_score": 35, "valuation_repricing_score": 48, "execution_risk_score": 62, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 25, "accounting_trust_risk_score": 20}
component_delta_explanation: "C12 gate discounts customer/headline evidence unless shipment, revenue recognition, ASP/margin bridge and call-off risk clearance are visible."
```

### 나노신소재 (121600) component delta

```yaml
weighted_score_before: 68
stage_label_before: Stage2-Actionable
raw_component_scores_before: {"contract_score": 40, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 45, "relative_strength_score": 35, "customer_quality_score": 55, "policy_or_regulatory_score": 30, "valuation_repricing_score": 50, "execution_risk_score": 65, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 15}
weighted_score_after: 56
stage_label_after: Stage2-Watch
raw_component_scores_after: {"contract_score": 30, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 36, "relative_strength_score": 30, "customer_quality_score": 48, "policy_or_regulatory_score": 30, "valuation_repricing_score": 40, "execution_risk_score": 75, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 15}
component_delta_explanation: "C12 gate discounts customer/headline evidence unless shipment, revenue recognition, ASP/margin bridge and call-off risk clearance are visible."
```

### 알루코 (001780) component delta

```yaml
weighted_score_before: 72
stage_label_before: Stage2-Actionable
raw_component_scores_before: {"contract_score": 68, "backlog_visibility_score": 62, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 52, "customer_quality_score": 75, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 64, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 20}
weighted_score_after: 59
stage_label_after: Stage2-Watch
raw_component_scores_after: {"contract_score": 60, "backlog_visibility_score": 54, "margin_bridge_score": 20, "revision_score": 30, "relative_strength_score": 42, "customer_quality_score": 72, "policy_or_regulatory_score": 45, "valuation_repricing_score": 45, "execution_risk_score": 72, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 20}
component_delta_explanation: "C12 gate discounts customer/headline evidence unless shipment, revenue recognition, ASP/margin bridge and call-off risk clearance are visible."
```

### 후성 (093370) component delta

```yaml
weighted_score_before: 55
stage_label_before: Stage4B
raw_component_scores_before: {"contract_score": 35, "backlog_visibility_score": 25, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 25, "customer_quality_score": 40, "policy_or_regulatory_score": 20, "valuation_repricing_score": 35, "execution_risk_score": 85, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 30}
weighted_score_after: 38
stage_label_after: Stage4C
raw_component_scores_after: {"contract_score": 20, "backlog_visibility_score": 15, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 25, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 95, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 35}
component_delta_explanation: "C12 gate discounts customer/headline evidence unless shipment, revenue recognition, ASP/margin bridge and call-off risk clearance are visible."
```

### 디이엔티 (079810) component delta

```yaml
weighted_score_before: 66
stage_label_before: Stage2-Actionable
raw_component_scores_before: {"contract_score": 50, "backlog_visibility_score": 45, "margin_bridge_score": 25, "revision_score": 28, "relative_strength_score": 50, "customer_quality_score": 70, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 78, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 20}
weighted_score_after: 49
stage_label_after: Stage4B
raw_component_scores_after: {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 18, "revision_score": 22, "relative_strength_score": 38, "customer_quality_score": 50, "policy_or_regulatory_score": 25, "valuation_repricing_score": 40, "execution_risk_score": 86, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 20}
component_delta_explanation: "C12 gate discounts customer/headline evidence unless shipment, revenue recognition, ASP/margin bridge and call-off risk clearance are visible."
```

## 7. Shadow profile comparison

| profile_id | hypothesis | changed_axes | eligible_triggers | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current profile; Stage2 bridge and generic 4B guard already active | none | 6 | 49.4194 | -30.1694 | 50.7818 | -36.5809 | 0.6667 | 1 | mixed; still over-admits customer headline rows |
| P0b_e2r_2_0_baseline_reference | old baseline; weaker bridge requirement | rollback reference | 6 | 49.4194 | -30.1694 | 50.7818 | -36.5809 | 0.8333 | 0 | worse; would over-promote most C12 headlines |
| P1_sector_specific_L3_candidate | L3 customer-contract rows require explicit delivery/utilization/margin gate | delivery_utilization_margin_gate +1 | 4 | 68.3647 | -24.9258 | 70.4083 | -28.8664 | 0.5 | 0 | better separation but still too broad for C12 |
| P2_canonical_C12_candidate | C12 requires shipment/revenue/margin + call-off risk gate; explicit production stop routes 4C | C12_customer_contract_calloff_gate | 3 | 87.5385 | -17.9734 | 90.2633 | -21.2194 | 0.3333 | 0 | best alignment; removes CNT/module/spec-change traps |
| P3_counterexample_guard_profile | strict high-MAE guard: cap Stage3 if MAE90<-25 without bridge | high_MAE_stage3_cap | 2 | 125.6839 | -15.8354 | 125.6839 | -20.7044 | 0.0 | 1 | safer but may over-filter moderate capacity buildouts |

Best shadow candidate: `P2_canonical_C12_candidate`. It keeps Enchem and Foosung readable while capping Nano Tim, Aluko and DNT headline traps. This is a canonical-archetype rule candidate, not a production patch.

## 8. Proposed rule candidate

```text
C12_CUSTOMER_CONTRACT_REQUIRES_SHIPMENT_REVENUE_MARGIN_AND_CALLOFF_CLEARANCE_GATE_V106
```

Rule scope: `canonical_archetype_specific`.

Existing axes tested:

```text
stage2_required_bridge
local_4b_watch_guard
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

Existing axis strengthened: `stage2_required_bridge | local_4b_watch_guard | hard_4c_thesis_break_routes_to_4c`.

## 9. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106 | 2 | 4 | 6 | 1 | 6 | 0 | 6 | 6 | 4 | L3_battery_customer_contract_delivery_margin_gate | C12_CUSTOMER_CONTRACT_REQUIRES_SHIPMENT_REVENUE_MARGIN_AND_CALLOFF_CLEARANCE_GATE_V106 | static C12 32 -> 38; session-adjusted C12 remains quality-holdout only |

## 10. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: [stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [customer_headline_without_shipment_revenue_margin_bridge, customer_inventory_calloff_not_routed_hard_enough, fast_MFE_positive_without_4B_exit_overlay]
new_axis_proposed: C12_CUSTOMER_CONTRACT_REQUIRES_SHIPMENT_REVENUE_MARGIN_AND_CALLOFF_CLEARANCE_GATE_V106
existing_axis_strengthened: [stage2_required_bridge, local_4b_watch_guard, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [full_4b_requires_non_price_evidence]
sector_specific_rule_candidate: L3_battery_customer_contract_delivery_margin_gate
canonical_archetype_rule_candidate: C12_CUSTOMER_CONTRACT_REQUIRES_SHIPMENT_REVENUE_MARGIN_AND_CALLOFF_CLEARANCE_GATE_V106
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 6 new independent cases, 4 counterexamples, and 5 residual errors for R3/L3/C12.

## 11. Machine-readable rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C12_R3_L106_348370_ENYCHEM_NORTH_AMERICA_ELECTROLYTE_CUSTOMER_SUPPLY_POSITIVE","symbol":"348370","company_name":"엔켐","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"north_america_customer_supply_positive_with_4b_exit_guard","current_profile_verdict":"current_profile_missed_structural_then_needs_local_4b_overlay","price_source":"Songdaiki/stock-web","notes":"This is the positive anchor: customer supply and capacity route were unusually explicit, but the fast rerating still needs a local 4B exit overlay."}
{"row_type":"trigger","trigger_id":"C12_R3_L106_348370_ENYCHEM_NORTH_AMERICA_ELECTROLYTE_CUSTOMER_SUPPLY_POSITIVE_TRG","case_id":"C12_R3_L106_348370_ENYCHEM_NORTH_AMERICA_ELECTROLYTE_CUSTOMER_SUPPLY_POSITIVE","symbol":"348370","company_name":"엔켐","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","sector":"battery_EV_green_mobility","primary_archetype":"battery_customer_contract_calloff_risk","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":113600.0,"evidence_available_at_that_date":"North America electrolyte supply: Georgia plant capacity expansion and shipments to LGES, SK On, Ultium Cells and BlueOvalSK customers.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=25553","stage2_evidence_fields":["named_cell_customers","north_america_supply_chain","capacity_expansion_path"],"stage3_evidence_fields":["customer_supply_conversion","regional_proximity_advantage","shipment_and_capacity_bridge"],"stage4b_evidence_fields":["post_peak_drawdown_watch_after_fast_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_path":"atlas/symbol_profiles/348/348370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":215.581,"MFE_90D_pct":247.2711,"MFE_180D_pct":247.2711,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.5458,"MAE_90D_pct":-5.5458,"MAE_180D_pct":-5.5458,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-04-08","peak_price":394500.0,"drawdown_after_peak_pct":-62.2307,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"north_america_customer_supply_positive_with_4b_exit_guard","current_profile_verdict":"current_profile_missed_structural_then_needs_local_4b_overlay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_348370_2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P2_canonical_C12_candidate","case_id":"C12_R3_L106_348370_ENYCHEM_NORTH_AMERICA_ELECTROLYTE_CUSTOMER_SUPPLY_POSITIVE","trigger_id":"C12_R3_L106_348370_ENYCHEM_NORTH_AMERICA_ELECTROLYTE_CUSTOMER_SUPPLY_POSITIVE_TRG","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":55,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":80,"customer_quality_score":85,"policy_or_regulatory_score":65,"valuation_repricing_score":78,"execution_risk_score":48,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":30,"accounting_trust_risk_score":25},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":82,"backlog_visibility_score":68,"margin_bridge_score":55,"revision_score":55,"relative_strength_score":78,"customer_quality_score":90,"policy_or_regulatory_score":65,"valuation_repricing_score":64,"execution_risk_score":50,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":30,"accounting_trust_risk_score":25},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12-specific gate discounts customer/order headlines lacking shipment, revenue recognition, ASP/margin bridge or call-off risk clearance; explicit inventory/production stop can route to Stage4C.","MFE_90D_pct":247.2711,"MAE_90D_pct":-5.5458,"score_return_alignment_label":"north_america_customer_supply_positive_with_4b_exit_guard","current_profile_verdict":"current_profile_missed_structural_then_needs_local_4b_overlay"}
{"row_type":"case","case_id":"C12_R3_L106_005070_COSMO_CATHODE_CAPA_EXPANSION_STAGE2_GUARD","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive_with_guardrail","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"capacity_expansion_stage2_positive_but_not_stage3","current_profile_verdict":"current_profile_correct_if_capped_at_stage2_watch","price_source":"Songdaiki/stock-web","notes":"Stage2 evidence was real, but the forward path did not justify a clean Stage3 without shipment and margin confirmation."}
{"row_type":"trigger","trigger_id":"C12_R3_L106_005070_COSMO_CATHODE_CAPA_EXPANSION_STAGE2_GUARD_TRG","case_id":"C12_R3_L106_005070_COSMO_CATHODE_CAPA_EXPANSION_STAGE2_GUARD","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","sector":"battery_EV_green_mobility","primary_archetype":"battery_customer_contract_calloff_risk","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-19","entry_date":"2023-09-20","entry_price":162700.0,"evidence_available_at_that_date":"Cathode capacity expansion and 2024 revenue challenge narrative; customer demand existed, but delivery, utilization and margin conversion were still incomplete at entry.","evidence_source":"https://securities.miraeasset.com/bbs/download/2119218.pdf?attachmentId=2119218","stage2_evidence_fields":["cathode_capacity_expansion","customer_demand_request","supply_capacity_buildout"],"stage3_evidence_fields":["not_yet_supported_by_asp_margin_or_shipment_bridge"],"stage4b_evidence_fields":["moderate_MAE_and_post_peak_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2023.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.2477,"MFE_90D_pct":11.2477,"MFE_180D_pct":19.4222,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.0086,"MAE_90D_pct":-22.2495,"MAE_180D_pct":-22.2495,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":194300.0,"drawdown_after_peak_pct":-29.5934,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"capacity_expansion_stage2_positive_but_not_stage3","current_profile_verdict":"current_profile_correct_if_capped_at_stage2_watch","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_005070_2023-09-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P2_canonical_C12_candidate","case_id":"C12_R3_L106_005070_COSMO_CATHODE_CAPA_EXPANSION_STAGE2_GUARD","trigger_id":"C12_R3_L106_005070_COSMO_CATHODE_CAPA_EXPANSION_STAGE2_GUARD_TRG","symbol":"005070","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":52,"margin_bridge_score":35,"revision_score":42,"relative_strength_score":48,"customer_quality_score":58,"policy_or_regulatory_score":35,"valuation_repricing_score":55,"execution_risk_score":58,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":50,"backlog_visibility_score":50,"margin_bridge_score":30,"revision_score":38,"relative_strength_score":45,"customer_quality_score":55,"policy_or_regulatory_score":35,"valuation_repricing_score":48,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":25,"accounting_trust_risk_score":20},"weighted_score_after":64,"stage_label_after":"Stage2","changed_components":["contract_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12-specific gate discounts customer/order headlines lacking shipment, revenue recognition, ASP/margin bridge or call-off risk clearance; explicit inventory/production stop can route to Stage4C.","MFE_90D_pct":11.2477,"MAE_90D_pct":-22.2495,"score_return_alignment_label":"capacity_expansion_stage2_positive_but_not_stage3","current_profile_verdict":"current_profile_correct_if_capped_at_stage2_watch"}
{"row_type":"case","case_id":"C12_R3_L106_121600_NANO_CNT_CUSTOMER_VOLUME_CALLOFF_COUNTEREXAMPLE","symbol":"121600","company_name":"나노신소재","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer_volume_headline_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive_if_stage3_opened","price_source":"Songdaiki/stock-web","notes":"C12 should not treat CNT adoption language as a customer-contract conversion unless purchase timing, shipment, ASP and margin are visible."}
{"row_type":"trigger","trigger_id":"C12_R3_L106_121600_NANO_CNT_CUSTOMER_VOLUME_CALLOFF_COUNTEREXAMPLE_TRG","case_id":"C12_R3_L106_121600_NANO_CNT_CUSTOMER_VOLUME_CALLOFF_COUNTEREXAMPLE","symbol":"121600","company_name":"나노신소재","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","sector":"battery_EV_green_mobility","primary_archetype":"battery_customer_contract_calloff_risk","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-23","entry_date":"2024-07-23","entry_price":95200.0,"evidence_available_at_that_date":"CNT conductive additive volume growth and new customer volume thesis; customer adoption was real but forward price path punished unconfirmed shipment/margin timing.","evidence_source":"https://securities.miraeasset.com/bbs/download/2129977.pdf?attachmentId=2129977","stage2_evidence_fields":["CNT_conductive_additive_adoption","new_customer_volume_thesis","battery_technology_pull"],"stage3_evidence_fields":["not_yet_supported_by_confirmed_customer_ramp_or_margin_bridge"],"stage4b_evidence_fields":["high_MAE_after_customer_volume_headline"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv","profile_path":"atlas/symbol_profiles/121/121600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.042,"MFE_90D_pct":5.042,"MFE_180D_pct":5.042,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.0462,"MAE_90D_pct":-37.7101,"MAE_180D_pct":-49.8424,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-23","peak_price":100000.0,"drawdown_after_peak_pct":-52.25,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"customer_volume_headline_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive_if_stage3_opened","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_121600_2024-07-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P2_canonical_C12_candidate","case_id":"C12_R3_L106_121600_NANO_CNT_CUSTOMER_VOLUME_CALLOFF_COUNTEREXAMPLE","trigger_id":"C12_R3_L106_121600_NANO_CNT_CUSTOMER_VOLUME_CALLOFF_COUNTEREXAMPLE_TRG","symbol":"121600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":45,"relative_strength_score":35,"customer_quality_score":55,"policy_or_regulatory_score":30,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":20,"accounting_trust_risk_score":15},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":36,"relative_strength_score":30,"customer_quality_score":48,"policy_or_regulatory_score":30,"valuation_repricing_score":40,"execution_risk_score":75,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":20,"accounting_trust_risk_score":15},"weighted_score_after":56,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12-specific gate discounts customer/order headlines lacking shipment, revenue recognition, ASP/margin bridge or call-off risk clearance; explicit inventory/production stop can route to Stage4C.","MFE_90D_pct":5.042,"MAE_90D_pct":-37.7101,"score_return_alignment_label":"customer_volume_headline_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive_if_stage3_opened"}
{"row_type":"case","case_id":"C12_R3_L106_001780_ALUKO_LGES_MODULE_CASE_ORDER_CHASM_COUNTEREXAMPLE","symbol":"001780","company_name":"알루코","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"module_case_order_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive_without_EV_demand_and_margin_gate","price_source":"Songdaiki/stock-web","notes":"A named customer order can still fail C12 if the downstream demand and margin path cannot absorb customer timing risk."}
{"row_type":"trigger","trigger_id":"C12_R3_L106_001780_ALUKO_LGES_MODULE_CASE_ORDER_CHASM_COUNTEREXAMPLE_TRG","case_id":"C12_R3_L106_001780_ALUKO_LGES_MODULE_CASE_ORDER_CHASM_COUNTEREXAMPLE","symbol":"001780","company_name":"알루코","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","sector":"battery_EV_green_mobility","primary_archetype":"battery_customer_contract_calloff_risk","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":3830.0,"evidence_available_at_that_date":"LG Energy Solution end-plate / module-case supply and large accumulated order narrative; EV chasm and Europe weakness later exposed revenue/margin bridge risk.","evidence_source":"https://v.daum.net/v/7rOw1YSgdQ","stage2_evidence_fields":["LGES_module_case_supply","long_duration_component_order","battery_component_revenue_narrative"],"stage3_evidence_fields":["not_supported_without_customer_take_rate_and_margin_bridge"],"stage4b_evidence_fields":["event_premium_and_EV_chasm_high_MAE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001780/2024.csv","profile_path":"atlas/symbol_profiles/001/001780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.0157,"MFE_90D_pct":18.0157,"MFE_180D_pct":18.0157,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.5796,"MAE_90D_pct":-43.6031,"MAE_180D_pct":-54.1775,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":4520.0,"drawdown_after_peak_pct":-61.1726,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"module_case_order_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive_without_EV_demand_and_margin_gate","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_001780_2024-03-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P2_canonical_C12_candidate","case_id":"C12_R3_L106_001780_ALUKO_LGES_MODULE_CASE_ORDER_CHASM_COUNTEREXAMPLE","trigger_id":"C12_R3_L106_001780_ALUKO_LGES_MODULE_CASE_ORDER_CHASM_COUNTEREXAMPLE_TRG","symbol":"001780","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":62,"margin_bridge_score":25,"revision_score":35,"relative_strength_score":52,"customer_quality_score":75,"policy_or_regulatory_score":45,"valuation_repricing_score":60,"execution_risk_score":64,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":20,"accounting_trust_risk_score":20},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":54,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":42,"customer_quality_score":72,"policy_or_regulatory_score":45,"valuation_repricing_score":45,"execution_risk_score":72,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":20,"accounting_trust_risk_score":20},"weighted_score_after":59,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12-specific gate discounts customer/order headlines lacking shipment, revenue recognition, ASP/margin bridge or call-off risk clearance; explicit inventory/production stop can route to Stage4C.","MFE_90D_pct":18.0157,"MAE_90D_pct":-43.6031,"score_return_alignment_label":"module_case_order_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive_without_EV_demand_and_margin_gate"}
{"row_type":"case","case_id":"C12_R3_L106_093370_FOOSUNG_LIPF6_CUSTOMER_INVENTORY_STOP_4C","symbol":"093370","company_name":"후성","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer_inventory_production_stop_hard_4c_success","current_profile_verdict":"current_profile_4c_success_if_routed_immediately","price_source":"Songdaiki/stock-web","notes":"This is the hard-protection row: explicit production stoppage from customer inventory adjustment is not just a 4B watch."}
{"row_type":"trigger","trigger_id":"C12_R3_L106_093370_FOOSUNG_LIPF6_CUSTOMER_INVENTORY_STOP_4C_TRG","case_id":"C12_R3_L106_093370_FOOSUNG_LIPF6_CUSTOMER_INVENTORY_STOP_4C","symbol":"093370","company_name":"후성","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","sector":"battery_EV_green_mobility","primary_archetype":"battery_customer_contract_calloff_risk","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2023-04-14","entry_date":"2023-04-17","entry_price":14890.0,"evidence_available_at_that_date":"LiPF6 production stop due to electrolyte customer inventory adjustment, company inventory increase and cost burden reduction.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20230810000585&docno=&method=searchInitInfo","stage2_evidence_fields":["prior_electrolyte_customer_exposure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_and_margin_pressure","inventory_adjustment"],"stage4c_evidence_fields":["production_stop","customer_inventory_adjustment","ASP_and_cost_pressure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2023.csv","profile_path":"atlas/symbol_profiles/093/093370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.0967,"MFE_90D_pct":4.0967,"MFE_180D_pct":4.0967,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.7824,"MAE_90D_pct":-26.1249,"MAE_180D_pct":-35.863,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-18","peak_price":15500.0,"drawdown_after_peak_pct":-38.3871,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"margin_or_backlog_slowdown","four_c_protection_label":"hard_4c_success","trigger_outcome_label":"customer_inventory_production_stop_hard_4c_success","current_profile_verdict":"current_profile_4c_success_if_routed_immediately","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_093370_2023-04-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P2_canonical_C12_candidate","case_id":"C12_R3_L106_093370_FOOSUNG_LIPF6_CUSTOMER_INVENTORY_STOP_4C","trigger_id":"C12_R3_L106_093370_FOOSUNG_LIPF6_CUSTOMER_INVENTORY_STOP_4C_TRG","symbol":"093370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":20,"relative_strength_score":25,"customer_quality_score":40,"policy_or_regulatory_score":20,"valuation_repricing_score":35,"execution_risk_score":85,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":20,"accounting_trust_risk_score":30},"weighted_score_before":55,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":20,"customer_quality_score":25,"policy_or_regulatory_score":20,"valuation_repricing_score":25,"execution_risk_score":95,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":20,"accounting_trust_risk_score":35},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["contract_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12-specific gate discounts customer/order headlines lacking shipment, revenue recognition, ASP/margin bridge or call-off risk clearance; explicit inventory/production stop can route to Stage4C.","MFE_90D_pct":4.0967,"MAE_90D_pct":-26.1249,"score_return_alignment_label":"customer_inventory_production_stop_hard_4c_success","current_profile_verdict":"current_profile_4c_success_if_routed_immediately"}
{"row_type":"case","case_id":"C12_R3_L106_079810_DNT_LGES_NOTCHING_PROCESS_SHIFT_4B_COUNTEREXAMPLE","symbol":"079810","company_name":"디이엔티","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer_process_shift_high_mae_4b_counterexample","current_profile_verdict":"current_profile_false_positive_if_customer_spec_change_not_discounted","price_source":"Songdaiki/stock-web","notes":"This is a 4B-not-4C case: customer process changes can cap the thesis before there is a formal cancellation or company-wide thesis break."}
{"row_type":"trigger","trigger_id":"C12_R3_L106_079810_DNT_LGES_NOTCHING_PROCESS_SHIFT_4B_COUNTEREXAMPLE_TRG","case_id":"C12_R3_L106_079810_DNT_LGES_NOTCHING_PROCESS_SHIFT_4B_COUNTEREXAMPLE","symbol":"079810","company_name":"디이엔티","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","sector":"battery_EV_green_mobility","primary_archetype":"battery_customer_contract_calloff_risk","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B","trigger_date":"2023-10-20","entry_date":"2023-10-20","entry_price":20750.0,"evidence_available_at_that_date":"LGES notching-equipment process change from laser to press exposed single-customer and equipment-spec timing risk for DNT laser notching thesis.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=23575","stage2_evidence_fields":["LGES_laser_notching_supplier_history","battery_equipment_customer_dependence"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["customer_process_shift","single_customer_order_timing_risk","equipment_spec_change"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079810/2023.csv","profile_path":"atlas/symbol_profiles/079/079810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.8434,"MFE_90D_pct":10.8434,"MFE_180D_pct":10.8434,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.3373,"MAE_90D_pct":-45.7831,"MAE_180D_pct":-51.8072,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-06","peak_price":23000.0,"drawdown_after_peak_pct":-56.5217,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":"contract_delay|margin_or_backlog_slowdown|positioning_overheat","four_c_protection_label":"not_applicable","trigger_outcome_label":"customer_process_shift_high_mae_4b_counterexample","current_profile_verdict":"current_profile_false_positive_if_customer_spec_change_not_discounted","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_079810_2023-10-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P2_canonical_C12_candidate","case_id":"C12_R3_L106_079810_DNT_LGES_NOTCHING_PROCESS_SHIFT_4B_COUNTEREXAMPLE","trigger_id":"C12_R3_L106_079810_DNT_LGES_NOTCHING_PROCESS_SHIFT_4B_COUNTEREXAMPLE_TRG","symbol":"079810","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":25,"revision_score":28,"relative_strength_score":50,"customer_quality_score":70,"policy_or_regulatory_score":25,"valuation_repricing_score":60,"execution_risk_score":78,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":20,"accounting_trust_risk_score":20},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":18,"revision_score":22,"relative_strength_score":38,"customer_quality_score":50,"policy_or_regulatory_score":25,"valuation_repricing_score":40,"execution_risk_score":86,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":20,"accounting_trust_risk_score":20},"weighted_score_after":49,"stage_label_after":"Stage4B","changed_components":["contract_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12-specific gate discounts customer/order headlines lacking shipment, revenue recognition, ASP/margin bridge or call-off risk clearance; explicit inventory/production stop can route to Stage4C.","MFE_90D_pct":10.8434,"MAE_90D_pct":-45.7831,"score_return_alignment_label":"customer_process_shift_high_mae_4b_counterexample","current_profile_verdict":"current_profile_false_positive_if_customer_spec_change_not_discounted"}
{"row_type":"aggregate","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_battery_customer_contract_inventory_calloff_fifth_holdout_v106","calibration_usable_trigger_count":6,"representative_trigger_count":6,"positive_case_count":2,"counterexample_count":4,"4B_case_count":6,"4C_case_count":1,"avg_MFE_90D_pct":49.4194,"avg_MAE_90D_pct":-30.1694,"avg_MFE_180D_pct":50.7818,"avg_MAE_180D_pct":-36.5809,"current_profile_error_count":4}
{"row_type":"residual_contribution","round":"R3","loop":106,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["customer_headline_without_shipment_revenue_margin_bridge","customer_inventory_calloff_not_routed_hard_enough","fast_MFE_positive_without_4B_exit_overlay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session. In a later coding-agent batch ingest session, parse this MD as a standard V12 result file. Validate every row_type="trigger" row against entry_date, entry_price, canonical MFE_30D_pct/MFE_90D_pct/MFE_180D_pct and MAE_30D_pct/MAE_90D_pct/MAE_180D_pct. Then test the shadow-only candidate C12_CUSTOMER_CONTRACT_REQUIRES_SHIPMENT_REVENUE_MARGIN_AND_CALLOFF_CLEARANCE_GATE_V106 against v12 validated/representative rows. Apply nothing directly to production scoring without batch-level regression, duplicate grouping, and promotion-decision checks.
```

## 13. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 14. Next research state

```yaml
completed_round: R3
completed_loop: 106
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 static C12 / session-adjusted quality holdout
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_or_cash_collection_path
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
