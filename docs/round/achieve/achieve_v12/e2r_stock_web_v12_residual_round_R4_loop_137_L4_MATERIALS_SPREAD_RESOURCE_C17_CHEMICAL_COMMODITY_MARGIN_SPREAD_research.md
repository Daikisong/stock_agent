# stock-web v12 residual research — R4 loop 137 — C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

## 0. Execution envelope

- selected_round: R4
- selected_loop: 137
- large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
- canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
- fine_archetype_id: SILICONE_PAINT_MARGIN_RECOVERY_VS_SOLAR_PETCHEM_OVERSUPPLY_AND_MATERIALS_EVENT_CONTAMINATION
- price_source: Songdaiki/stock-web
- price_basis: tradable_raw
- price_adjustment_status: raw_unadjusted_marcap
- research_mode: historical_trigger_level_residual_calibration_after_stock_web_ohlc_breakthrough_v12
- production_scoring_changed: false
- shadow_weight_only: true
- created_at_kst: 2026-06-07

## 1. Selection basis and no-repeat check

Repository no-repeat index still marks C17_CHEMICAL_COMMODITY_MARGIN_SPREAD as a low-coverage bucket. Prior local C17 work used S-Oil, LG Chem, and Hyosung Chemical as the main second-pass examples. This pass uses visible-new C17 symbols on the current index basis:

- 002380 KCC
- 009830 Hanwha Solutions
- 011790 SKC

No trigger repeats the exact canonical_archetype_id + symbol + trigger_type + entry_date key from the visible index or prior local C17 pass.

## 2. Thesis of this loop

C17 should not treat every “chemical / petrochemical / materials / feedstock” headline as equivalent. The core translation chain is:

```text
feedstock or product spread
→ company-specific product mix
→ realized ASP and utilization
→ segment margin / cash-flow revision
→ price path alignment
```

This loop tests three situations:

1. KCC: positive-control where diversified chemical/materials/silicone exposure and price path showed sustained MFE before later fade.
2. Hanwha Solutions: low-quality chemical/solar/petchem label where feedstock or policy vocabulary did not protect the price path from oversupply and margin pressure.
3. SKC: high-MFE materials event contamination case where large MFE came from battery/materials narrative rather than clean C17 petrochemical margin bridge.

## 3. Trigger rows JSONL

```jsonl
{"canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","fine_archetype_id":"SILICONE_PAINT_MARGIN_RECOVERY_VS_SOLAR_PETCHEM_OVERSUPPLY_AND_MATERIALS_EVENT_CONTAMINATION","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_close":244000,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":17.62,"mae_30d_pct":-2.46,"mfe_90d_pct":20.49,"mae_90d_pct":-7.79,"mfe_180d_pct":41.39,"mae_180d_pct":-7.79,"path_label":"positive_control","calibration_usable":true,"non_price_bridge_quality":"medium","score_return_alignment":"pass","current_profile_stress_test":"C17 should allow Stage2 when company-specific chemical/materials margin bridge is visible and MAE remains contained through 90D.","residual_contribution":"Supports C17 company_specific_margin_bridge_positive_control with later 4B watch after full-window fade."}
{"canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","fine_archetype_id":"SILICONE_PAINT_MARGIN_RECOVERY_VS_SOLAR_PETCHEM_OVERSUPPLY_AND_MATERIALS_EVENT_CONTAMINATION","symbol":"009830","name":"Hanwha Solutions","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":31800,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.86,"mae_30d_pct":-11.79,"mfe_90d_pct":7.86,"mae_90d_pct":-30.35,"mfe_180d_pct":7.86,"mae_180d_pct":-37.11,"path_label":"counterexample","calibration_usable":true,"non_price_bridge_quality":"medium","score_return_alignment":"fail","current_profile_stress_test":"C17 should not grant Stage2-Actionable for feedstock substitution, petrochemical label, or solar/chemical mix when oversupply and margin bridge are not resolved.","residual_contribution":"Strengthens C17 oversupply_margin_stage2_block and low_MFE_high_MAE false-positive guard."}
{"canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","fine_archetype_id":"SILICONE_PAINT_MARGIN_RECOVERY_VS_SOLAR_PETCHEM_OVERSUPPLY_AND_MATERIALS_EVENT_CONTAMINATION","symbol":"011790","name":"SKC","trigger_type":"Stage2-Watch","entry_date":"2024-05-23","entry_close":117000,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":70.94,"mae_30d_pct":0.0,"mfe_90d_pct":70.94,"mae_90d_pct":-8.03,"mfe_180d_pct":70.94,"mae_180d_pct":-20.17,"path_label":"non_c17_event_contamination_watch","calibration_usable":true,"non_price_bridge_quality":"low_for_C17","score_return_alignment":"mixed","current_profile_stress_test":"High MFE alone should not be learned as C17 chemical spread alpha if the dominant narrative is battery/materials rather than feedstock-product margin spread.","residual_contribution":"Adds C17 non_C17_event_contamination_cap and vertical_MFE_4B_watch guard."}
```

## 4. Case notes

### 4.1 KCC (002380) — positive-control, but not unconditional Green

KCC is a chemical/materials name with coatings, building materials, and silicone-related operations. The price path from 2024-01-30 close 244,000 showed forward highs of 287,000 within 30D, 294,000 within 90D, and 345,000 within 180D. The same 90D/180D window did not break into a deep drawdown, with the worst checked low around 225,000.

This supports a C17 escape hatch: when the name has a credible company-level product/margin bridge and the 90D MAE is contained, Stage2-Actionable can be retained. However, the later fade toward late 2024 means full-window 4B watch remains necessary if no refreshed margin/revision evidence appears.

### 4.2 Hanwha Solutions (009830) — label does not equal spread bridge

The 2024-05-20 Reuters feedstock article gave a useful industry background: Korean crackers used more LPG as a cheaper feedstock, but they were still operating in low-margin and oversupplied conditions. Hanwha Solutions is a mixed solar/chemical structure rather than a clean petchem-spread conversion story. Its 2024-05-20 entry close was 31,800; forward high reached only 34,300 while 90D low fell to 22,150 and later window low reached roughly 20,000.

This is a clean C17 false-positive guard: “feedstock substitution,” “chemical,” or “solar/chemical rebound” vocabulary cannot open Stage2-Actionable when the company-specific spread-to-margin bridge is absent.

### 4.3 SKC (011790) — high MFE, but contamination from non-C17 narrative

SKC had a very strong price path after 2024-05-23 close 117,000, with 30D/90D highs up to 200,000. But this is dangerous as C17 training data. The move can be dominated by battery/materials or copper-foil-style narrative rather than clean petrochemical feedstock-product spread.

Therefore, C17 should not learn the entire MFE as chemical commodity margin alpha. It should be allowed as a 4B watch / contamination cap case, not as a clean positive.

## 5. Rule candidate

```text
rule_id = C17_COMPANY_SPECIFIC_SPREAD_MARGIN_BRIDGE_REQUIREMENT

if canonical_archetype_id == C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
and chemical_or_feedstock_label == true
and company_specific_feedstock_product_spread_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
rule_id = C17_LOW_MFE_HIGH_MAE_FALSE_POSITIVE_BLOCK

if canonical_archetype_id == C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
and MFE_90D_pct < +10
and MAE_90D_pct <= -25
and refreshed_margin_or_cash_bridge == false:
    Stage2_FalsePositive_Block = true
```

```text
rule_id = C17_NON_C17_EVENT_CONTAMINATION_CAP

if canonical_archetype_id == C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
and MFE_30D_pct >= +30
and dominant_non_price_driver not in ["feedstock_product_spread", "chemical_margin_revision", "segment_cash_bridge"]:
    cap_C17_contribution = true
    route = local_4B_watch
```

## 6. Residual contribution summary

- new_independent_case_count: 3
- reused_case_count_within_C17_visible_basis: 0
- same_archetype_new_symbol_count_visible_index_basis: 3
- same_archetype_new_trigger_family_count: 3
- calibration_usable case 수: 3
- calibration_usable trigger 수: 3
- positive_case_count: 1
- counterexample_count: 2
- current_profile_error_count: 2
- sector_specific_rule_candidate: false
- canonical_archetype_rule_candidate: true
- loop_contribution_label: canonical_archetype_rule_candidate

## 7. Existing axis strengthened

- C17_company_specific_feedstock_product_spread_margin_bridge_requirement
- C17_petchem_or_feedstock_headline_stage2_block
- C17_low_MFE_high_MAE_false_positive_block
- C17_non_C17_event_contamination_cap
- C17_vertical_MFE_local_4B_watch_after_materials_spike

## 8. Next recommended archetypes

- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
- R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
- C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
- C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
- C15_MATERIAL_SPREAD_SUPERCYCLE
