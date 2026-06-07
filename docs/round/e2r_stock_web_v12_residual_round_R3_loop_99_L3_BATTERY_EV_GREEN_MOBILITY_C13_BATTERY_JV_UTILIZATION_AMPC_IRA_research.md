---
schema_family: v12_sector_archetype_residual
round: R3
loop: 99
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: CELL_MAKER_JV_AMPC_UTILIZATION_CASH_CONVERSION_BRIDGE_VS_POLICY_CREDIT_LABEL_SPIKE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | AMPC_cash_conversion_guardrail | high_MAE_guardrail | canonical_archetype_compression
price_source_repo: Songdaiki/stock-web
price_source_name: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
research_created_at: 2026-06-06
evidence_url_status: evidence_url_pending
source_quality_mode: source_proxy_only
production_patch_ready: false
---

# E2R Stock-Web v12 Residual Research — R3 loop 99 — L3 — C13_BATTERY_JV_UTILIZATION_AMPC_IRA

## 0. Executive conclusion

This standalone residual file expands **C13_BATTERY_JV_UTILIZATION_AMPC_IRA** with cell-maker / parent-company cases where the market can re-rate on **IRA / AMPC / US JV / utilization** vocabulary before the non-price bridge is fully proven.

The working conclusion is intentionally conservative:

> AMPC/IRA/JV exposure can support Stage2-Yellow only when it is connected to operating utilization, customer take-up, and cash conversion. If the signal is merely accounting credit, subsidy vocabulary, or capacity headline without utilization and margin bridge, the row should be capped at Yellow or local 4B-watch rather than promoted to Stage3-Green.

The C13 rule should not behave like a policy-label detector. It should behave like a toll-gate: the policy credit is only useful when batteries actually pass through the JV factory gate and cash comes out the other side.

---

## 1. Coverage and no-repeat decision

- selected_round: R3
- selected_large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
- selected_canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
- selected_loop: 99
- no-repeat basis: new canonical/symbol/trigger_type/entry_date combinations.
- prior latest registry anchor: C13 had R3 loop 98 before this run.
- this file contributes 4 case rows and 4 representative trigger rows.

---

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","symbol":"373220","name":"LG에너지솔루션","price_source_repo":"Songdaiki/stock-web","price_source_name":"FinanceData/marcap","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","profile_path":"atlas/symbol_profiles/373/373220.json","shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","entry_row_exists":true,"data_quality_label":"clean_tradable_path","corporate_action_candidate_count":0,"window_180D_corporate_action_contaminated":false}
{"row_type":"price_source_validation","symbol":"006400","name":"삼성SDI","price_source_repo":"Songdaiki/stock-web","price_source_name":"FinanceData/marcap","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","profile_path":"atlas/symbol_profiles/006/006400.json","shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","entry_row_exists":true,"data_quality_label":"usable_with_caveat","corporate_action_candidate_count":3,"window_180D_corporate_action_contaminated":false,"note":"profile has historical corporate-action caveat, but 2024 calibration window is outside listed historical CA dates"}
{"row_type":"price_source_validation","symbol":"096770","name":"SK이노베이션","price_source_repo":"Songdaiki/stock-web","price_source_name":"FinanceData/marcap","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","profile_path":"atlas/symbol_profiles/096/096770.json","shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","entry_row_exists":true,"data_quality_label":"usable_with_caveat","corporate_action_candidate_count":1,"window_180D_corporate_action_contaminated":true,"note":"2024-11-20 corporate-action candidate blocks full 180D promotion use; 30D/90D path retained as residual evidence"}
{"row_type":"price_source_validation","symbol":"051910","name":"LG화학","price_source_repo":"Songdaiki/stock-web","price_source_name":"FinanceData/marcap","price_basis":"tradable_raw","adjustment_status":"raw_unadjusted_marcap","profile_path":"atlas/symbol_profiles/051/051910.json","shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","entry_row_exists":true,"data_quality_label":"clean_tradable_path","corporate_action_candidate_count":0,"window_180D_corporate_action_contaminated":false}
```

---

## 3. Representative trigger rows

```jsonl
{"row_type":"trigger","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"LGES_US_JV_AMPC_UTILIZATION_CASH_CONVERSION_VS_POLICY_CREDIT_LABEL","symbol":"373220","name":"LG에너지솔루션","trigger_type":"JV_AMPC_UTILIZATION_YELLOW_NOT_GREEN","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":385000,"as_of_stage_current_profile":"Stage2-Yellow","suggested_stage_v12_shadow":"Stage2-Yellow","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.12,"mae_30d_pct":-15.32,"mfe_90d_pct":3.12,"mae_90d_pct":-16.23,"mfe_180d_pct":3.12,"mae_180d_pct":-16.23,"peak_price_180d":397000,"trough_price_180d":322500,"window_180D_corporate_action_contaminated":false,"source_proxy_only":true,"evidence_url_pending":true,"residual_label":"AMPC/JV vocabulary generated only weak upside and meaningful drawdown without visible utilization/cash conversion bridge"}
{"row_type":"trigger","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SAMSUNG_SDI_US_JV_RAMP_VS_POLICY_CREDIT_AND_EU_DEMAND_FADE","symbol":"006400","name":"삼성SDI","trigger_type":"JV_RAMP_HIGH_MAE_GUARDRAIL","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":459500,"as_of_stage_current_profile":"Stage2-Yellow","suggested_stage_v12_shadow":"Stage2-Yellow_with_high_MAE_guardrail","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.62,"mae_30d_pct":-12.95,"mfe_90d_pct":7.62,"mae_90d_pct":-23.61,"mfe_180d_pct":7.62,"mae_180d_pct":-23.61,"peak_price_180d":494500,"trough_price_180d":351000,"window_180D_corporate_action_contaminated":false,"source_proxy_only":true,"evidence_url_pending":true,"residual_label":"initial JV/ramp rerating was tradable but later drawdown was too deep for Green without confirmed utilization and margin bridge"}
{"row_type":"trigger","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SK_ON_PARENT_FUNDING_AMPC_OPTIONALITY_VS_CORPORATE_ACTION_CONTAMINATED_FULL_WINDOW","symbol":"096770","name":"SK이노베이션","trigger_type":"AMPC_PARENT_FUNDING_EVENT_CAP","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":121000,"as_of_stage_current_profile":"Stage2-Yellow","suggested_stage_v12_shadow":"event_cap_local_4B_watch","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.03,"mae_30d_pct":-11.82,"mfe_90d_pct":6.03,"mae_90d_pct":-11.82,"mfe_180d_pct":null,"mae_180d_pct":null,"peak_price_90d":128300,"trough_price_90d":106700,"window_180D_corporate_action_contaminated":true,"source_proxy_only":true,"evidence_url_pending":true,"residual_label":"funding/AMPC optionality had event-style MFE but full window is blocked by corporate-action contamination and non-price bridge remained insufficient"}
{"row_type":"trigger","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"LGCHEM_PARENT_BATTERY_MATERIAL_JV_OPTIONALITY_VS_SUBSIDIARY_AMPC_LOOKTHROUGH","symbol":"051910","name":"LG화학","trigger_type":"PARENT_LOOKTHROUGH_AMPC_DISCOUNT","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":395500,"as_of_stage_current_profile":"Stage2-Yellow","suggested_stage_v12_shadow":"Stage2-Yellow_or_event_cap","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.17,"mae_30d_pct":-11.50,"mfe_90d_pct":4.17,"mae_90d_pct":-17.57,"mfe_180d_pct":4.17,"mae_180d_pct":-17.57,"peak_price_180d":412000,"trough_price_180d":326000,"window_180D_corporate_action_contaminated":false,"source_proxy_only":true,"evidence_url_pending":true,"residual_label":"parent-company AMPC/JV look-through did not produce enough direct utilization/cash conversion evidence for Green"}
```

---

## 4. Case notes

### 4.1 373220 LG에너지솔루션 — C13 Yellow, not Green

- C13 interpretation: direct cell maker with clear AMPC/JV vocabulary.
- Residual issue: the price path after 2024-04-24 shows limited MFE and a deep drawdown, so AMPC vocabulary alone would have over-promoted the case.
- Shadow rule: require utilization/cash conversion bridge before Green.

### 4.2 006400 삼성SDI — high-MAE guardrail

- C13 interpretation: US JV/ramp narrative can create a fast MFE.
- Residual issue: the post-trigger path carried high MAE; the initial MFE does not justify Green unless utilization and operating margin bridge are visible.
- Shadow rule: Stage2-Yellow is acceptable; Green requires non-price utilization/revision confirmation.

### 4.3 096770 SK이노베이션 — parent funding / event-cap

- C13 interpretation: SK On parent exposure and AMPC/funding optionality.
- Residual issue: the 2024-06-20 event path shows event-driven upside, but full 180D calibration is blocked by corporate-action candidate contamination.
- Shadow rule: use local 30D/90D as residual evidence only; do not allow this row to promote a production patch.

### 4.4 051910 LG화학 — parent look-through discount

- C13 interpretation: parent-company battery material / LGES look-through optionality.
- Residual issue: AMPC/JV value is indirect. Without direct cash conversion into parent earnings, the path should remain Yellow/event-cap.
- Shadow rule: parent look-through requires additional discount / cash conversion proof.

---

## 5. Aggregate metric

```jsonl
{"row_type":"aggregate_metric","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","sample_trigger_rows":4,"positive_rows":0,"yellow_watch_rows":3,"counterexample_rows":1,"clean_180d_rows":3,"blocked_180d_rows":1,"median_mfe_90d_pct":5.10,"median_mae_90d_pct":-14.70,"green_promotion_ready_rows":0,"production_patch_ready":false,"dominant_residual_error":"AMPC/IRA/JV label can overstate rerating quality when utilization/cash-conversion bridge is not explicit"}
```

---

## 6. Score simulation

```jsonl
{"row_type":"score_simulation","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile":"current_e2r_2_2","case_group":"policy_credit_or_JV_label_only","expected_stage":"Stage2-Yellow_or_local_4B_watch","failure_mode":"label-driven MFE with high MAE"}
{"row_type":"score_simulation","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile":"v12_shadow_candidate","case_group":"AMPC_plus_utilization_plus_cash_conversion","expected_stage":"Stage3-Yellow_to_Green_candidate","required_non_price_bridge":["JV utilization rate","customer take-up / shipment acceptance","AMPC cash recognition quality","gross margin or EBITDA bridge","revision confirmation"]}
{"row_type":"score_simulation","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile":"v12_shadow_candidate","case_group":"parent_lookthrough_AMPC","expected_stage":"Stage2-Yellow_or_event_cap","required_discount":"parent-company look-through must be discounted unless direct earnings and cash distribution bridge is visible"}
```

---

## 7. Shadow weight / rule candidate

```jsonl
{"row_type":"shadow_weight","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"stage2_required_bridge","direction":"tighten","component":"industrial_logic","suggested_delta":-0.15,"guardrail":"Do not promote AMPC/IRA/JV label-only cases to Green without utilization and cash conversion bridge"}
{"row_type":"shadow_weight","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"high_MAE_guardrail","direction":"add","component":"price_stage","suggested_rule":"If MFE is single-digit and MAE exceeds -12% within 90D, cap at Yellow unless revision and margin bridge appear"}
{"row_type":"shadow_weight","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"parent_lookthrough_discount","direction":"add","component":"capital_allocation_and_governance","suggested_rule":"Parent-company AMPC/JV exposure should receive lower confidence than direct cell-maker AMPC cash conversion unless dividend, equity-method, or explicit earnings bridge is visible"}
```

---

## 8. Residual contribution

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","contribution_type":"coverage_gap_fill","rows_added":4,"new_symbols_added":["373220","006400","096770","051910"],"new_trigger_families":["JV_AMPC_UTILIZATION_YELLOW_NOT_GREEN","JV_RAMP_HIGH_MAE_GUARDRAIL","AMPC_PARENT_FUNDING_EVENT_CAP","PARENT_LOOKTHROUGH_AMPC_DISCOUNT"]}
{"row_type":"residual_contribution","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","contribution_type":"promotion_safety","production_patch_ready":false,"reason":"all non-price evidence remains source_proxy_only/evidence_url_pending; one row has 180D corporate-action contamination; several rows require utilization/cash-conversion URL verification before scoring-profile patch"}
```

---

## 9. Deferred Coding Agent Handoff Prompt

Ingest this MD as a v12 residual research artifact.

Expected parser behavior:
- accept schema_family `v12_sector_archetype_residual`
- preserve `round=R3`, `loop=99`, `large_sector_id=L3_BATTERY_EV_GREEN_MOBILITY`, `canonical_archetype_id=C13_BATTERY_JV_UTILIZATION_AMPC_IRA`
- parse 4 trigger rows, 4 price_source_validation rows, aggregate_metric, score_simulation, shadow_weight, and residual_contribution rows
- mark rows as `source_proxy_only=true` and `evidence_url_pending=true`
- do not treat as production patch until URL evidence validates utilization/cash conversion bridge

Recommended next manual URL-verification targets:
1. company filings or IR materials showing AMPC cash recognition, not only accounting credit
2. US JV utilization / ramp schedule / customer shipment acceptance
3. margin or EBITDA bridge attributable to AMPC/JV utilization
4. parent-company look-through mechanics for LG화학 and SK이노베이션
