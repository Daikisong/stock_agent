# E2R Stock-Web v12 Residual Research — R5 Loop 114 — C20 Beauty/Food Global Distribution

## 0. Execution Metadata

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
created_at: 2026-06-07
selected_round: R5
selected_loop: "114"
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_K_BEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_BRIDGE_VS_LEGACY_CHINA_REBOUND_OR_LABEL_SPIKE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
auto_selected_coverage_gap: "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION: rows=6, need_to_30=24, need_to_50=44"
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
live_candidate_mode: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
```

## 1. Coverage / No-Repeat Selection

`C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` is still a Priority 0 coverage gap: existing rows are low relative to the 30-row minimum target.  
Previous C20 representative symbols in the No-Repeat Index were `018250`, `114840`, `192820`, `214420`, `237880`, `406820`. This run intentionally avoids those exact C20 symbol rows.

Existing registry check:
- Prior C20 file found at `R5 loop 113`, so this run uses `selected_loop = 114`.
- Same canonical repetition is allowed, but the duplicate key must not repeat `symbol + canonical_archetype_id + trigger_type + entry_date`.

This run adds:
- `003230` 삼양식품 — positive K-food export/sell-through/OPM bridge.
- `278470` 에이피알 — positive K-beauty global DTC/device distribution bridge with later 4B watch.
- `090430` 아모레퍼시픽 — counterexample: legacy China rebound/brand label without durable sell-through and margin bridge.

## 2. Thesis

C20 should not reward the label **K-food/K-beauty** by itself.  
The rerating hinge is whether the brand/export story descends into **repeat global channel demand, sell-through, ASP, OPM/revision, and cash conversion**. A headline is a spark; the bridge is the wick. Without the wick, price flares and dies.

### Proposed C20 guardrail interpretation

```text
Positive C20 bridge:
  global distribution expansion
  + repeat channel demand / sell-through
  + ASP or mix improvement
  + OPM / earnings revision
  + price path confirms with acceptable MAE

False-positive C20 label:
  K-food/K-beauty theme vocabulary
  + China reopening or one-off brand rebound
  + no durable sell-through / OPM revision
  + high MAE after small or local-only MFE
```

## 3. Case Summary

| case_id | symbol | company | role | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| C20-L114-01 | 003230 | 삼양식품 | positive | 2024-05-17 | 446500 | 60.81 / 0.00 | 60.81 / 0.00 | 106.05 / 0.00 | Stage2-Actionable worked |
| C20-L114-02 | 278470 | 에이피알 | positive + 4B watch | 2025-02-27 | 60100 | 20.63 / -8.82 | 204.99 / -8.82 | 365.06 / -8.82 | Stage2 worked, vertical rerating requires watch |
| C20-L114-03 | 090430 | 아모레퍼시픽 | counterexample | 2024-05-31 | 194200 | 3.24 / -14.68 | 3.24 / -40.32 | 3.24 / -48.76 | Stage2 false positive / block |

## 4. Price Source Validation

```text
source_repo = Songdaiki/stock-web
manifest_max_date = 2026-02-20
price_basis = tradable_raw
adjustment_status = raw_unadjusted_marcap
required_fields = entry_date, entry_price, MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct
all_required_price_fields_present = true
corporate_action_contamination_check = passed_for_selected_windows
```

## 5. Trigger Rows JSONL

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R5","selected_loop":"114","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_EXPORT_SELLTHROUGH_ASP_OPM_BRIDGE","symbol":"003230","company_name":"삼양식품","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":446500,"trigger_type":"Stage2-Actionable","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":60.81,"MAE_30D_pct":0.0,"MFE_90D_pct":60.81,"MAE_90D_pct":0.0,"MFE_180D_pct":106.05,"MAE_180D_pct":0.0,"evidence_family":"k_food_export_sellthrough_asp_capacity_opm_bridge","profile_verdict":"positive_stage2_to_green","calibration_usable":true,"current_profile_error":false,"duplicate_key":"003230|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|Stage2-Actionable|2024-05-16|2024-05-17|k_food_export_sellthrough_asp_capacity_opm_bridge","notes":"Buldak export demand, ASP/shipment/capacity and OPM bridge; not mere food-theme headline."}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R5","selected_loop":"114","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_DTC_DEVICE_GLOBAL_DISTRIBUTION_REVENUE_BRIDGE","symbol":"278470","company_name":"에이피알","trigger_date":"2025-02-27","entry_date":"2025-02-27","entry_price":60100,"trigger_type":"Stage2-Actionable","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":20.63,"MAE_30D_pct":-8.82,"MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"MFE_180D_pct":365.06,"MAE_180D_pct":-8.82,"evidence_family":"k_beauty_device_us_dtc_global_distribution_revenue_bridge","profile_verdict":"positive_stage2_to_green_with_local_4b_watch","calibration_usable":true,"current_profile_error":false,"duplicate_key":"278470|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|Stage2-Actionable|2025-02-27|2025-02-27|k_beauty_device_us_dtc_global_distribution_revenue_bridge","notes":"Global K-beauty device/DTC channel expansion and overseas sales bridge; extreme post-trigger MFE requires 4B watch after vertical rerating."}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R5","selected_loop":"114","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_BEAUTY_CHINA_REBOUND_WITHOUT_DURABLE_SELLTHROUGH_MARGIN_BRIDGE","symbol":"090430","company_name":"아모레퍼시픽","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":194200,"trigger_type":"Stage2-Actionable","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.24,"MAE_30D_pct":-14.68,"MFE_90D_pct":3.24,"MAE_90D_pct":-40.32,"MFE_180D_pct":3.24,"MAE_180D_pct":-48.76,"evidence_family":"legacy_beauty_china_rebound_without_sustained_sellthrough_margin_bridge","profile_verdict":"counterexample_stage2_false_positive_price_only_or_late_chase","calibration_usable":true,"current_profile_error":true,"duplicate_key":"090430|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|Stage2-Actionable|2024-05-31|2024-05-31|legacy_beauty_china_rebound_without_sustained_sellthrough_margin_bridge","notes":"Legacy premium beauty/China-rebound label failed after earnings and China-demand weakness; should be capped or blocked without fresh sell-through and margin bridge."}
```

## 6. Raw Component Score Breakdown

C20 runtime reference weights: `EPS/Vis/Bott/Mis/Val/Cap/Info = 22/23/12/16/13/4/10`.

| symbol | company | EPS | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | raw_total | shadow_stage | price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 003230 | 삼양식품 | 22 | 23 | 10 | 15 | 9 | 3 | 8 | 90 | Stage3-Green candidate | excellent; high MFE and low MAE |
| 278470 | 에이피알 | 20 | 22 | 9 | 14 | 8 | 3 | 8 | 84 | Stage3-Yellow/Green borderline with 4B watch | excellent but vertical; 4B proximity |
| 090430 | 아모레퍼시픽 | 8 | 12 | 5 | 5 | 3 | 3 | 8 | 44 | Stage1/Watch, not Stage2 | bad; low MFE and high MAE |

## 7. Current Calibrated Profile Stress Test

### 7.1 Positive bridge retention

`003230` and `278470` show that C20 should preserve upside sensitivity when the export/global channel story is accompanied by revenue/OPM or overseas sales evidence. The price path is not merely a one-day label bounce. Both cases have strong forward MFE and acceptable early MAE.

### 7.2 Legacy-brand / China-rebound block

`090430` shows why C20 should block or cap old-style China rebound and legacy brand label signals. The initial MFE was only 3.24%, while MAE expanded to -40.32% by 90D and -48.76% by 180D. A profile that treats generic K-beauty recovery as Stage2-Actionable would overfit the theme and underweight sell-through durability.

### 7.3 4B proximity after vertical MFE

`278470` generated very large 90D/180D MFE. This validates the positive trigger but also strengthens a local 4B watch once price outruns fresh revision evidence. The rule should not suppress the initial Stage2/Stage3 bridge, but it should add a watch state after vertical rerating.

## 8. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count_within_C20: 0
cross_canonical_reused_symbol_count: 1
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
diversity_score_summary: "new_C20_symbol=3, new_trigger_family=3, positive/counterexample=2/1, cross-canonical symbol reuse only for 003230"
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: null
existing_axis_strengthened:
  - C20_distribution_sellthrough_opm_bridge_requirement
  - C20_legacy_china_rebound_stage2_block
  - C20_vertical_mfe_local_4b_watch
existing_axis_weakened: null
```

## 9. Shadow Weight / Rule Candidate

No production scoring change is proposed in this research run.

```yaml
shadow_weight_only: true
production_scoring_changed: false
candidate_patch_type: canonical_guardrail
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
recommended_runtime_effect:
  - require explicit sell-through / global distribution / OPM bridge for Stage2-Actionable
  - cap legacy China rebound or generic beauty/food vocabulary at Watch/Stage1 unless margin/revision bridge exists
  - add local_4B_watch when 90D MFE exceeds 100% without fresh fundamental confirmation
expected_safety_effect:
  false_positive_reduction: high
  missed_positive_risk: moderate
  implementation_scope: canonical_only
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not treat this Markdown as a production patch by itself.
Ingest this file through the v12 calibration parser only after validating:
1. filename round/loop/canonical/large_sector consistency,
2. required 30/90/180D MFE/MAE fields for every trigger row,
3. price_source == Songdaiki/stock-web,
4. price_basis == tradable_raw,
5. price_adjustment_status == raw_unadjusted_marcap,
6. duplicate key uniqueness against v12_trigger_rows_representative.jsonl.

If accepted, classify this run as a C20 canonical guardrail candidate:
- strengthen C20 distribution/sell-through/OPM bridge requirement,
- block or cap legacy China rebound and label-only K-beauty/K-food triggers,
- add local 4B watch after vertical MFE without new revision evidence.

Do not change production scoring automatically.
Generate shadow-only patch candidates and require aggregate confirmation across later C20 rows.
```

## 11. Final State

```text
completed_round = R5
completed_loop = 114
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
