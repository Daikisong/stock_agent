# E2R v12 Residual Research — R2 loop 132 — L2_AI_SEMICONDUCTOR_ELECTRONICS / C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 132
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C09 4C-empty repair, source/proxy repair, advanced-equipment valuation blowoff vs order/revenue bridge split after recent C05/C01/C13/C15/C10/C02/C16/R13/C17/C07/C06/C14/C11/C12 runs
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_FRONTEND_METROLOGY_VALUATION_BLOWOFF_VS_ORDER_BRIDGE
loop_objective: sector_specific_rule_discovery; canonical_archetype_rule_candidate; advanced equipment positive/counterexample balance; 4B/4C sparse-path repair; direct URL/proxy-quality repair; complete_30_90_180_MFE_MAE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patched: false
live_candidate_mode: false
auto_trading_allowed: false
```

## 1. Selection / Novelty Check

This run follows the v12 coverage-index scheduler, not a mechanical R1→R13 loop. The current ledger says every C01~C32 canonical archetype already exceeds the 80-row threshold, so the useful work is now URL/proxy quality repair, complete MFE/MAE, entry-date integrity, and residual positive/counterexample balance. Recent local outputs in this session covered C05, C01, C13, C15, C10, C02, C16, R13, C17, C07, C06, C14, C11, and C12. This run therefore moves to **C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF** under **R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS**.

No-Repeat ledger snapshot for C09:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 291 rows | 77 symbols | positives/counter 59/101 | 4B/4C 56/2 | weights 22/20/18/13/11/6/10
```

C09 already has enough rows, but its 4C path is thin. The selected residual is therefore not “more advanced-equipment winners”; it is the missing line between **real advanced-equipment bottleneck + dated conversion bridge** and **valuation/relative-strength blowoff**.

```yaml
hard_duplicate_key_checked: canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
positive_case_count: 2
counterexample_count: 4
stage4b_case_count: 2
stage4c_case_count: 2
source_proxy_only_count: 3
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
```

## 2. Price Source Validation

Stock-Web manifest/schema basis used in every trigger row:

```yaml
price_atlas_repo: https://github.com/Songdaiki/stock-web
manifest: atlas/manifest.json
schema: atlas/schema.json
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
MFE_formula: (max_high_from_entry_window - entry_close) / entry_close
MAE_formula: (min_low_from_entry_window - entry_close) / entry_close
required_windows: 30D, 90D, 180D
corporate_action_window_rule: entry_date through D+180 must be clean for calibration_usable=true
```

Symbol-profile caveats checked or inferred from Stock-Web profile coverage already used in this session:

```yaml
403870_HPSP: corporate_action_candidate_dates=[2023-03-16, 2023-04-11]; selected 2024 180D window clean=true
036930_Jusung: corporate_action_candidate_dates=[2000-06-22]; selected 2024 180D window clean=true
039030_EOTechnics: selected 2024 180D window clean=true; no selected-window corporate-action contamination observed in tradable shard
240810_WonikIPS: selected 2024 180D window clean=true; no selected-window corporate-action contamination observed in tradable shard
140860_ParkSystems: corporate_action_candidate_count=0; selected 2024 180D window clean=true
101490_SNSTech: corporate_action_candidate_dates=[2009-04-30]; selected 2024 180D window clean=true
```

## 3. Case Table

| case_id | symbol | company | trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | outcome | verdict |
|---|---:|---|---|---|---:|---:|---:|---|---|
| C09_HPSP_2024_HIGH_PRESSURE_ANNEALING_VALUATION_BLOWOFF | 403870 | HPSP | Stage4B 2024-02-13 | 2024-02-13 @ 59,300 | 7.76% / -16.95% | 7.76% / -39.88% | 7.76% / -61.80% | counterexample_advanced_equipment_valuation_blowoff_high_MAE | current_profile_false_positive_if_bottleneck_quality_and_valuation_are_overcredited_without_current_order_revenue_bridge |
| C09_JUSUNG_2024_ALD_SHIPMENT_ORDER_BRIDGE | 036930 | Jusung Engineering | Stage2-Actionable 2024-10-17 | 2024-10-18 @ 27,600 | 23.37% / -6.16% | 44.93% / -6.34% | 57.25% / -6.34% | positive_advanced_ALD_shipment_bridge_follow_through | current_profile_correct_when_direct_shipment_customer_trust_evidence_upgrades_information_confidence_and_visibility |
| C09_EOTECHNICS_2024_HBM_LASER_EXPECTATION_BLOWOFF | 039030 | EO Technics | Stage4B 2024-03-04 | 2024-03-04 @ 205,500 | 36.74% / -16.50% | 36.74% / -17.08% | 36.74% / -42.82% | counterexample_local_MFE_then_full_window_blowoff | current_profile_false_positive_if_HBM_laser_narrative_is_treated_as_customer_order_or_revenue_bridge |
| C09_WONIKIPS_2024_MEMORY_AI_EQUIPMENT_BETA_NO_ORDER | 240810 | Wonik IPS | Stage4C 2024-04-01 | 2024-04-01 @ 42,000 | 6.79% / -20.24% | 6.79% / -28.93% | 6.79% / -49.64% | counterexample_broad_equipment_beta_no_conversion_high_MAE | current_profile_should_route_to_4C_review_if_generic_memory_AI_equipment_beta_fails_near_term_order_or_revision_bridge |
| C09_PARKSYSTEMS_2024_NANOSCALE_METROLOGY_DIRECT_IR_BRIDGE | 140860 | Park Systems | Stage3-Yellow 2024-05-23 | 2024-05-23 @ 180,400 | 10.09% / -7.65% | 11.70% / -17.13% | 38.58% / -17.13% | positive_metrology_quality_bridge_with_drawdown_aware_confirmation | current_profile_correct_as_Yellow_not_Green_until_growth_and_drawdown_confirmation_arrive |
| C09_SNSTECH_2024_EUV_PELLICLE_FUTURE_TECHNICAL_RISK_4C | 101490 | S&S Tech | Stage4C 2024-03-04 | 2024-03-04 @ 46,450 | 6.35% / -11.09% | 6.35% / -26.80% | 6.35% / -59.07% | counterexample_future_advanced_equipment_material_expectation_technical_delay_high_MAE | current_profile_should_block_positive_stage_when_future_technology_expectation_lacks_current_customer_revenue_bridge |


## 4. Actual Stock-Web Entry Rows / Peak-Trough Rows

| trigger_id | symbol | entry_date | o | h | l | c | v | 30D peak/trough | 90D peak/trough | 180D peak/trough |
|---|---:|---|---:|---:|---:|---:|---:|---|---|---|
| T1 | 403870 | 2024-02-13 | 49,400 | 62,400 | 49,250 | 59,300 | 15,671,806 | 2024-02-15 63,900 / 2024-02-13 49,250 | 2024-02-15 63,900 / 2024-05-10 35,650 | 2024-02-15 63,900 / 2024-08-05 22,650 |
| T2 | 036930 | 2024-10-18 | 28,800 | 28,800 | 27,400 | 27,600 | 278,788 | 2024-11-04 34,050 / 2024-10-28 25,900 | 2025-02-19 40,000 / 2024-12-02 25,850 | 2025-03-21 43,400 / 2024-12-02 25,850 |
| T3 | 039030 | 2024-03-04 | 211,500 | 217,500 | 202,000 | 205,500 | 295,571 | 2024-04-12 281,000 / 2024-03-15 171,600 | 2024-04-12 281,000 / 2024-06-25 170,400 | 2024-04-12 281,000 / 2024-11-18 117,500 |
| T4 | 240810 | 2024-04-01 | 41,650 | 42,500 | 41,000 | 42,000 | 1,431,282 | 2024-04-08 44,850 / 2024-05-13 33,500 | 2024-04-08 44,850 / 2024-08-05 29,850 | 2024-04-08 44,850 / 2024-12-09 21,150 |
| T5 | 140860 | 2024-05-23 | 179,200 | 182,000 | 173,600 | 180,400 | 19,086 | 2024-07-04 198,600 / 2024-05-30 166,600 | 2024-10-04 201,500 / 2024-08-05 149,500 | 2025-01-22 250,000 / 2024-08-05 149,500 |
| T6 | 101490 | 2024-03-04 | 44,500 | 46,800 | 43,050 | 46,450 | 905,333 | 2024-03-13 49,400 / 2024-04-08 41,300 | 2024-03-13 49,400 / 2024-07-03 34,000 | 2024-03-13 49,400 / 2024-11-14 19,010 |


## 5. Case Notes

### T1 — HPSP / 403870 / counterexample_advanced_equipment_valuation_blowoff_high_MAE

High-pressure hydrogen annealing is a real advanced-equipment niche, but the trigger was already a valuation/price blowoff. The short local MFE and deep 90D/180D MAE argue for 4B watch unless current order/revenue revision bridge is visible. Entry uses `2024-02-13` close and complete Stock-Web 30D/90D/180D windows. Stock-Web path: 30D `7.76% / -16.95%`, 90D `7.76% / -39.88%`, 180D `7.76% / -61.80%`. Evidence URLs: https://imec-int.com/en/imec-magazine/imec-magazine-january-2024/hpsp, https://www.hpsp.co.kr/eng/index.html, https://www.mk.co.kr/en/business/10933579.

### T2 — Jusung Engineering / 036930 / positive_advanced_ALD_shipment_bridge_follow_through

The ALD thesis moved from generic technology exposure to a dated shipment/customer-trust bridge. That is a cleaner C09 Stage2-Actionable path than price-relative strength alone. Entry uses `2024-10-18` close and complete Stock-Web 30D/90D/180D windows. Stock-Web path: 30D `23.37% / -6.16%`, 90D `44.93% / -6.34%`, 180D `57.25% / -6.34%`. Evidence URLs: https://www.jseng.com/en/product/product01.html, https://www.asiae.co.kr/article/2024101710081008056.

### T3 — EO Technics / 039030 / counterexample_local_MFE_then_full_window_blowoff

The stock delivered a strong local peak but later collapsed. C09 needs local 4B versus full-window blowoff split: do not promote to Green on relative strength without dated customer/order/revenue proof. Entry uses `2024-03-04` close and complete Stock-Web 30D/90D/180D windows. Stock-Web path: 30D `36.74% / -16.50%`, 90D `36.74% / -17.08%`, 180D `36.74% / -42.82%`. Evidence URLs: https://www.eotechnics.com/en/, https://www.semi.org/en/resources/member-directory/eo-technics-co-ltd, https://www.kirs.or.kr/information/report2.html.

### T4 — Wonik IPS / 240810 / counterexample_broad_equipment_beta_no_conversion_high_MAE

Broad AI/memory capex recovery helped the theme but did not form a symbol-level C09 bridge. The path is almost all downside after a small early MFE. Entry uses `2024-04-01` close and complete Stock-Web 30D/90D/180D windows. Stock-Web path: 30D `6.79% / -20.24%`, 90D `6.79% / -28.93%`, 180D `6.79% / -49.64%`. Evidence URLs: https://www.ips.co.kr/en/, https://semi.org/en/about-semi/membership/member-directory/wonik-ips, https://www.semiconkorea.org/en/news/global-semiconductor-manufacturing-industry-poised-for-2024-expansion.

### T5 — Park Systems / 140860 / positive_metrology_quality_bridge_with_drawdown_aware_confirmation

Park Systems has direct nanoscale metrology product quality and semiconductor-fab AFM positioning. It works better than a pure blowoff name, but 90D MAE says Green should wait for earnings/revision confirmation. Entry uses `2024-05-23` close and complete Stock-Web 30D/90D/180D windows. Stock-Web path: 30D `10.09% / -7.65%`, 90D `11.70% / -17.13%`, 180D `38.58% / -17.13%`. Evidence URLs: https://www.parksystems.com/products/semiconductor/overview, https://www.parksystems.com/products/semiconductor/nx-wafer, https://www.parksystems.com/images/investment/2024/05/Park_Systems_IR_20240523.pdf.

### T6 — S&S Tech / 101490 / counterexample_future_advanced_equipment_material_expectation_technical_delay_high_MAE

Blank-mask business is real and EUV pellicle optionality was visible, but the as-of evidence remained future/technical-risk heavy. This is a clean 4C-like C09 guardrail case. Entry uses `2024-03-04` close and complete Stock-Web 30D/90D/180D windows. Stock-Web path: 30D `6.35% / -11.09%`, 90D `6.35% / -26.80%`, 180D `6.35% / -59.07%`. Evidence URLs: https://www.snstech.co.kr/en/product/business.php, https://www.thelec.net/news/articleView.html?idxno=4025, https://www.thelec.net/news/articleView.html?idxno=4637.


## 6. Current Profile Stress Test

C09 is a dangerous archetype because the market often sees the right noun before the income statement sees the right bridge. “ALD,” “hydrogen annealing,” “laser equipment,” “metrology,” “EUV pellicle,” and “AI equipment” are all useful technical nouns, but they are not equivalent to dated customer shipment, current-year revenue conversion, or visible earnings revision.

The profile stress test splits the six rows into two groups:

1. **Bridge-present positives** — Jusung and Park Systems show a clearer bridge from advanced equipment/product quality to shipment, IR, market share, or measurable operating performance. These can remain Stage2-Actionable or Stage3-Yellow, with drawdown-aware confirmation before Green.
2. **Bridge-missing blowoffs** — HPSP, EO Technics, Wonik IPS, and S&S Tech show product-quality or market-narrative truth, but entry occurred after valuation/relative-strength or future-technology expectation had already run ahead of dated conversion evidence. These rows support 4B/4C repair.

## 7. Raw Component Score Breakdown / Simulation

C09 currently weights `EPS/Vis/Bott/Mis/Val/Cap/Info` as `22/20/18/13/11/6/10`. The residual failure is not that bottleneck exposure has zero value. It is that **bottleneck and valuation together can masquerade as earnings visibility**. The proposed shadow-only adjustment raises information-confidence requirements and reduces the ability of valuation/relative strength to open positive stages without a conversion bridge.

```yaml
suggested_shadow_weight_delta:
  before: 22/20/18/13/11/6/10
  after:  22/21/17/11/10/6/13
  delta:   0/+1/-1/-2/-1/0/+3
production_scoring_changed: false
shadow_weight_only: true
```

## 8. Machine-Readable Rows

```jsonl
{"row_type":"trigger","trigger_id":"T1","case_id":"C09_HPSP_2024_HIGH_PRESSURE_ANNEALING_VALUATION_BLOWOFF","round":"R2","loop":132,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_FRONTEND_METROLOGY_VALUATION_BLOWOFF_VS_ORDER_BRIDGE","symbol":"403870","company":"HPSP","trigger_type":"Stage4B","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":59300.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"evidence_family":"advanced_equipment_product_quality_plus_valuation_blowoff","source_proxy_only":false,"evidence_url_pending":false,"MFE_30D_pct":7.7572,"MAE_30D_pct":-16.9477,"MFE_90D_pct":7.7572,"MAE_90D_pct":-39.882,"MFE_180D_pct":7.7572,"MAE_180D_pct":-61.8044,"score_return_alignment_label":"counterexample_advanced_equipment_valuation_blowoff_high_MAE","current_profile_verdict":"current_profile_false_positive_if_bottleneck_quality_and_valuation_are_overcredited_without_current_order_revenue_bridge","do_not_count_as_new_case":false,"evidence_urls":["https://imec-int.com/en/imec-magazine/imec-magazine-january-2024/hpsp","https://www.hpsp.co.kr/eng/index.html","https://www.mk.co.kr/en/business/10933579"]}
{"row_type":"trigger","trigger_id":"T2","case_id":"C09_JUSUNG_2024_ALD_SHIPMENT_ORDER_BRIDGE","round":"R2","loop":132,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_FRONTEND_METROLOGY_VALUATION_BLOWOFF_VS_ORDER_BRIDGE","symbol":"036930","company":"Jusung Engineering","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-17","entry_date":"2024-10-18","entry_price":27600.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"evidence_family":"advanced_ALD_customer_shipment_order_bridge","source_proxy_only":false,"evidence_url_pending":false,"MFE_30D_pct":23.3696,"MAE_30D_pct":-6.1594,"MFE_90D_pct":44.9275,"MAE_90D_pct":-6.3406,"MFE_180D_pct":57.2464,"MAE_180D_pct":-6.3406,"score_return_alignment_label":"positive_advanced_ALD_shipment_bridge_follow_through","current_profile_verdict":"current_profile_correct_when_direct_shipment_customer_trust_evidence_upgrades_information_confidence_and_visibility","do_not_count_as_new_case":false,"evidence_urls":["https://www.jseng.com/en/product/product01.html","https://www.asiae.co.kr/article/2024101710081008056"]}
{"row_type":"trigger","trigger_id":"T3","case_id":"C09_EOTECHNICS_2024_HBM_LASER_EXPECTATION_BLOWOFF","round":"R2","loop":132,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_FRONTEND_METROLOGY_VALUATION_BLOWOFF_VS_ORDER_BRIDGE","symbol":"039030","company":"EO Technics","trigger_type":"Stage4B","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":205500.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"evidence_family":"laser_equipment_HBM_expectation_without_named_order_bridge","source_proxy_only":true,"evidence_url_pending":false,"MFE_30D_pct":36.7397,"MAE_30D_pct":-16.4964,"MFE_90D_pct":36.7397,"MAE_90D_pct":-17.0803,"MFE_180D_pct":36.7397,"MAE_180D_pct":-42.8224,"score_return_alignment_label":"counterexample_local_MFE_then_full_window_blowoff","current_profile_verdict":"current_profile_false_positive_if_HBM_laser_narrative_is_treated_as_customer_order_or_revenue_bridge","do_not_count_as_new_case":false,"evidence_urls":["https://www.eotechnics.com/en/","https://www.semi.org/en/resources/member-directory/eo-technics-co-ltd","https://www.kirs.or.kr/information/report2.html"]}
{"row_type":"trigger","trigger_id":"T4","case_id":"C09_WONIKIPS_2024_MEMORY_AI_EQUIPMENT_BETA_NO_ORDER","round":"R2","loop":132,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_FRONTEND_METROLOGY_VALUATION_BLOWOFF_VS_ORDER_BRIDGE","symbol":"240810","company":"Wonik IPS","trigger_type":"Stage4C","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":42000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"evidence_family":"broad_memory_AI_capex_beta_without_symbol_specific_order","source_proxy_only":true,"evidence_url_pending":false,"MFE_30D_pct":6.7857,"MAE_30D_pct":-20.2381,"MFE_90D_pct":6.7857,"MAE_90D_pct":-28.9286,"MFE_180D_pct":6.7857,"MAE_180D_pct":-49.6429,"score_return_alignment_label":"counterexample_broad_equipment_beta_no_conversion_high_MAE","current_profile_verdict":"current_profile_should_route_to_4C_review_if_generic_memory_AI_equipment_beta_fails_near_term_order_or_revision_bridge","do_not_count_as_new_case":false,"evidence_urls":["https://www.ips.co.kr/en/","https://semi.org/en/about-semi/membership/member-directory/wonik-ips","https://www.semiconkorea.org/en/news/global-semiconductor-manufacturing-industry-poised-for-2024-expansion"]}
{"row_type":"trigger","trigger_id":"T5","case_id":"C09_PARKSYSTEMS_2024_NANOSCALE_METROLOGY_DIRECT_IR_BRIDGE","round":"R2","loop":132,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_FRONTEND_METROLOGY_VALUATION_BLOWOFF_VS_ORDER_BRIDGE","symbol":"140860","company":"Park Systems","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-23","entry_date":"2024-05-23","entry_price":180400.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"evidence_family":"metrology_product_quality_plus_IR_market_share_bridge","source_proxy_only":false,"evidence_url_pending":false,"MFE_30D_pct":10.0887,"MAE_30D_pct":-7.6497,"MFE_90D_pct":11.6962,"MAE_90D_pct":-17.1286,"MFE_180D_pct":38.5809,"MAE_180D_pct":-17.1286,"score_return_alignment_label":"positive_metrology_quality_bridge_with_drawdown_aware_confirmation","current_profile_verdict":"current_profile_correct_as_Yellow_not_Green_until_growth_and_drawdown_confirmation_arrive","do_not_count_as_new_case":false,"evidence_urls":["https://www.parksystems.com/products/semiconductor/overview","https://www.parksystems.com/products/semiconductor/nx-wafer","https://www.parksystems.com/images/investment/2024/05/Park_Systems_IR_20240523.pdf"]}
{"row_type":"trigger","trigger_id":"T6","case_id":"C09_SNSTECH_2024_EUV_PELLICLE_FUTURE_TECHNICAL_RISK_4C","round":"R2","loop":132,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_FRONTEND_METROLOGY_VALUATION_BLOWOFF_VS_ORDER_BRIDGE","symbol":"101490","company":"S&S Tech","trigger_type":"Stage4C","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":46450.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"evidence_family":"future_EUV_pellicle_expectation_technical_risk_no_revenue_bridge","source_proxy_only":true,"evidence_url_pending":false,"MFE_30D_pct":6.3509,"MAE_30D_pct":-11.0872,"MFE_90D_pct":6.3509,"MAE_90D_pct":-26.803,"MFE_180D_pct":6.3509,"MAE_180D_pct":-59.0743,"score_return_alignment_label":"counterexample_future_advanced_equipment_material_expectation_technical_delay_high_MAE","current_profile_verdict":"current_profile_should_block_positive_stage_when_future_technology_expectation_lacks_current_customer_revenue_bridge","do_not_count_as_new_case":false,"evidence_urls":["https://www.snstech.co.kr/en/product/business.php","https://www.thelec.net/news/articleView.html?idxno=4025","https://www.thelec.net/news/articleView.html?idxno=4637"]}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C09_candidate","case_id":"C09_HPSP_2024_HIGH_PRESSURE_ANNEALING_VALUATION_BLOWOFF","trigger_id":"T1","symbol":"403870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"eps_fcf_explosion":5,"earnings_visibility":5,"bottleneck_pricing":8,"market_mispricing":7,"valuation_rerating":7,"capital_allocation":2,"information_confidence":7},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":3,"earnings_visibility":3,"bottleneck_pricing":6,"market_mispricing":4,"valuation_rerating":4,"capital_allocation":2,"information_confidence":9,"valuation_blowoff_risk":9},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_components":["earnings_visibility","information_confidence","order_revenue_bridge","valuation_blowoff_risk","drawdown_guard"],"component_delta_explanation":"C09 should credit real advanced-equipment bottleneck only when dated customer/order/revenue or IR bridge exists; otherwise valuation and price relative strength become 4B/4C risk evidence.","MFE_90D_pct":7.7572,"MAE_90D_pct":-39.882,"MFE_180D_pct":7.7572,"MAE_180D_pct":-61.8044,"score_return_alignment_label":"counterexample_advanced_equipment_valuation_blowoff_high_MAE","current_profile_verdict":"current_profile_false_positive_if_bottleneck_quality_and_valuation_are_overcredited_without_current_order_revenue_bridge"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C09_candidate","case_id":"C09_JUSUNG_2024_ALD_SHIPMENT_ORDER_BRIDGE","trigger_id":"T2","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"eps_fcf_explosion":5,"earnings_visibility":6,"bottleneck_pricing":7,"market_mispricing":5,"valuation_rerating":4,"capital_allocation":2,"information_confidence":7},"weighted_score_before":76,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":5,"earnings_visibility":8,"bottleneck_pricing":7,"market_mispricing":5,"valuation_rerating":4,"capital_allocation":2,"information_confidence":9,"order_revenue_bridge":8},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["earnings_visibility","information_confidence","order_revenue_bridge","valuation_blowoff_risk","drawdown_guard"],"component_delta_explanation":"C09 should credit real advanced-equipment bottleneck only when dated customer/order/revenue or IR bridge exists; otherwise valuation and price relative strength become 4B/4C risk evidence.","MFE_90D_pct":44.9275,"MAE_90D_pct":-6.3406,"MFE_180D_pct":57.2464,"MAE_180D_pct":-6.3406,"score_return_alignment_label":"positive_advanced_ALD_shipment_bridge_follow_through","current_profile_verdict":"current_profile_correct_when_direct_shipment_customer_trust_evidence_upgrades_information_confidence_and_visibility"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C09_candidate","case_id":"C09_EOTECHNICS_2024_HBM_LASER_EXPECTATION_BLOWOFF","trigger_id":"T3","symbol":"039030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"eps_fcf_explosion":5,"earnings_visibility":5,"bottleneck_pricing":8,"market_mispricing":7,"valuation_rerating":7,"capital_allocation":2,"information_confidence":7},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":3,"earnings_visibility":3,"bottleneck_pricing":6,"market_mispricing":4,"valuation_rerating":4,"capital_allocation":2,"information_confidence":9,"valuation_blowoff_risk":9},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_components":["earnings_visibility","information_confidence","order_revenue_bridge","valuation_blowoff_risk","drawdown_guard"],"component_delta_explanation":"C09 should credit real advanced-equipment bottleneck only when dated customer/order/revenue or IR bridge exists; otherwise valuation and price relative strength become 4B/4C risk evidence.","MFE_90D_pct":36.7397,"MAE_90D_pct":-17.0803,"MFE_180D_pct":36.7397,"MAE_180D_pct":-42.8224,"score_return_alignment_label":"counterexample_local_MFE_then_full_window_blowoff","current_profile_verdict":"current_profile_false_positive_if_HBM_laser_narrative_is_treated_as_customer_order_or_revenue_bridge"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C09_candidate","case_id":"C09_WONIKIPS_2024_MEMORY_AI_EQUIPMENT_BETA_NO_ORDER","trigger_id":"T4","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"eps_fcf_explosion":4,"earnings_visibility":5,"bottleneck_pricing":7,"market_mispricing":6,"valuation_rerating":6,"capital_allocation":2,"information_confidence":7},"weighted_score_before":69,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":2,"earnings_visibility":2,"bottleneck_pricing":4,"market_mispricing":3,"valuation_rerating":3,"capital_allocation":2,"information_confidence":9,"thesis_break_risk":10},"weighted_score_after":49,"stage_label_after":"Stage4C","changed_components":["earnings_visibility","information_confidence","order_revenue_bridge","valuation_blowoff_risk","drawdown_guard"],"component_delta_explanation":"C09 should credit real advanced-equipment bottleneck only when dated customer/order/revenue or IR bridge exists; otherwise valuation and price relative strength become 4B/4C risk evidence.","MFE_90D_pct":6.7857,"MAE_90D_pct":-28.9286,"MFE_180D_pct":6.7857,"MAE_180D_pct":-49.6429,"score_return_alignment_label":"counterexample_broad_equipment_beta_no_conversion_high_MAE","current_profile_verdict":"current_profile_should_route_to_4C_review_if_generic_memory_AI_equipment_beta_fails_near_term_order_or_revision_bridge"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C09_candidate","case_id":"C09_PARKSYSTEMS_2024_NANOSCALE_METROLOGY_DIRECT_IR_BRIDGE","trigger_id":"T5","symbol":"140860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"eps_fcf_explosion":6,"earnings_visibility":7,"bottleneck_pricing":8,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":2,"information_confidence":8},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"eps_fcf_explosion":6,"earnings_visibility":7,"bottleneck_pricing":8,"market_mispricing":5,"valuation_rerating":5,"capital_allocation":2,"information_confidence":9,"drawdown_guard":6},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["earnings_visibility","information_confidence","order_revenue_bridge","valuation_blowoff_risk","drawdown_guard"],"component_delta_explanation":"C09 should credit real advanced-equipment bottleneck only when dated customer/order/revenue or IR bridge exists; otherwise valuation and price relative strength become 4B/4C risk evidence.","MFE_90D_pct":11.6962,"MAE_90D_pct":-17.1286,"MFE_180D_pct":38.5809,"MAE_180D_pct":-17.1286,"score_return_alignment_label":"positive_metrology_quality_bridge_with_drawdown_aware_confirmation","current_profile_verdict":"current_profile_correct_as_Yellow_not_Green_until_growth_and_drawdown_confirmation_arrive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C09_candidate","case_id":"C09_SNSTECH_2024_EUV_PELLICLE_FUTURE_TECHNICAL_RISK_4C","trigger_id":"T6","symbol":"101490","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"eps_fcf_explosion":4,"earnings_visibility":5,"bottleneck_pricing":7,"market_mispricing":6,"valuation_rerating":6,"capital_allocation":2,"information_confidence":7},"weighted_score_before":69,"stage_label_before":"Stage2","raw_component_scores_after":{"eps_fcf_explosion":2,"earnings_visibility":2,"bottleneck_pricing":4,"market_mispricing":3,"valuation_rerating":3,"capital_allocation":2,"information_confidence":9,"thesis_break_risk":10},"weighted_score_after":49,"stage_label_after":"Stage4C","changed_components":["earnings_visibility","information_confidence","order_revenue_bridge","valuation_blowoff_risk","drawdown_guard"],"component_delta_explanation":"C09 should credit real advanced-equipment bottleneck only when dated customer/order/revenue or IR bridge exists; otherwise valuation and price relative strength become 4B/4C risk evidence.","MFE_90D_pct":6.3509,"MAE_90D_pct":-26.803,"MFE_180D_pct":6.3509,"MAE_180D_pct":-59.0743,"score_return_alignment_label":"counterexample_future_advanced_equipment_material_expectation_technical_delay_high_MAE","current_profile_verdict":"current_profile_should_block_positive_stage_when_future_technology_expectation_lacks_current_customer_revenue_bridge"}
{"row_type":"aggregate","round":"R2","loop":132,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_FRONTEND_METROLOGY_VALUATION_BLOWOFF_VS_ORDER_BRIDGE","representative_trigger_count":6,"positive_case_count":2,"counterexample_count":4,"stage4b_case_count":2,"stage4c_case_count":2,"source_proxy_only_count":3,"evidence_url_pending_count":0,"avg_MFE_30D_pct":15.182,"avg_MAE_30D_pct":-13.0964,"avg_MFE_90D_pct":19.0429,"avg_MAE_90D_pct":-22.6938,"avg_MFE_180D_pct":25.5768,"avg_MAE_180D_pct":-39.4689,"profile_error_count":4,"aggregate_verdict":"C09 needs a direct order/revenue/IR bridge gate. Product quality and bottleneck exposure can be real, but without dated conversion evidence they behave like valuation blowoff rather than rerating evidence."}
{"row_type":"shadow_weight","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_advanced_equipment_order_revenue_bridge_vs_valuation_blowoff_gate","scope":"canonical_archetype_specific","existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_confirmation"],"existing_axis_weakened":[],"new_axis_proposed":"C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_BRIDGE_VS_VALUATION_BLOWOFF_GATE","production_scoring_changed":false,"shadow_weight_only":true,"proposed_effect":"Require at least two of named advanced equipment/product niche, dated customer/order/shipment, current-year revenue or IR bridge, and revision/earnings visibility before Stage2-Actionable. Cap valuation/relative-strength-only routes at 4B; route repeated no-conversion/high-MAE paths to 4C review.","candidate_delta":{"earnings_visibility":1,"information_confidence":3,"bottleneck_pricing":-1,"market_mispricing":-2,"valuation_rerating":-1,"capital_allocation":0},"confidence":"medium","evidence_count":6,"counterexample_count":4}
{"row_type":"residual_contribution","round":"R2","loop":132,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","stage3_yellow_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_confirmation"],"residual_error_types_found":["advanced_equipment_product_quality_overcredit","valuation_and_relative_strength_blowoff","generic_memory_AI_capex_beta_without_symbol_order","future_EUV_pellicle_optionality_without_revenue_bridge","direct_ALD_shipment_undercredit","metrology_IR_bridge_positive_with_drawdown_guard"],"loop_contribution_label":"C09_valuation_blowoff_vs_order_revenue_bridge_quality_repair","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C09_GENERIC_AI_SEMICON_EQUIPMENT_CONTEXT_ONLY","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","reason":"General AI semiconductor equipment demand, HBM process complexity, or memory capex recovery is useful context but not sufficient standalone evidence for C09 Stage2-Actionable without symbol-specific conversion evidence.","usage":"context_only_not_representative_weight"}
```

## 9. Batch Ingest Self-Audit

```yaml
filename: e2r_stock_web_v12_residual_round_R2_loop_132_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
filename_matches_required_v12_regex: true
metadata_round_matches_filename_round: true
metadata_loop_matches_filename_loop: true
round_sector_consistency: pass
compact_filename_forbidden: pass
trigger_type_canonical_stage_labels_only: pass
all_trigger_rows_have_MFE_30D_pct: true
all_trigger_rows_have_MFE_90D_pct: true
all_trigger_rows_have_MFE_180D_pct: true
all_trigger_rows_have_MAE_30D_pct: true
all_trigger_rows_have_MAE_90D_pct: true
all_trigger_rows_have_MAE_180D_pct: true
same_entry_group_deduplicated: true
all_calibration_usable_rows_have_clean_180D_corporate_action_window: true
stock_agent_code_accessed: false
stock_agent_code_patched: false
production_scoring_changed: false
shadow_weight_only: true
```

## 10. Residual Contribution Summary

```yaml
loop_contribution_label: C09_advanced_equipment_valuation_blowoff_vs_order_revenue_bridge_quality_repair
auto_selected_coverage_gap: C09 has enough rows but weak 4C count and many source/proxy cases; this loop adds direct/product URLs, complete MFE/MAE, and 4B/4C split rows
sector_specific_rule_candidate: L2 advanced-equipment names require dated customer/order/shipment/revenue or IR bridge before Stage2-Actionable; product quality + price relative strength alone is 4B watch
canonical_archetype_rule_candidate: C09 should treat valuation rerating as an accelerant, not as the engine. The engine is named advanced equipment plus dated conversion evidence.
new_axis_proposed: C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_BRIDGE_VS_VALUATION_BLOWOFF_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - hard_4c_confirmation
existing_axis_weakened: []
validation_scope:
  symbols: [403870, 036930, 039030, 240810, 140860, 101490]
  new_independent_case_count: 6
  positive_case_count: 2
  counterexample_count: 4
  stage4b_case_count: 2
  stage4c_case_count: 2
  source_proxy_only_count: 3
  rows_missing_required_mfe_mae: 0
  average_MFE_90D_pct: 19.0429
  average_MAE_90D_pct: -22.6938
  average_MFE_180D_pct: 25.5768
  average_MAE_180D_pct: -39.4689
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not execute this handoff during the research session. Later, when batch-applying v12 research artifacts, ingest this MD as a standard v12 residual result file.

Target file:
e2r_stock_web_v12_residual_round_R2_loop_132_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md

Task:
1. Parse the machine-readable JSONL rows.
2. Validate required trigger fields: canonical stage label, symbol, trigger_date, entry_date, entry_price, MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
3. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family.
4. Add representative trigger rows only if calibration_usable=true and corporate-action window is clean.
5. Evaluate the shadow-only axis `C09_ADVANCED_EQUIPMENT_ORDER_REVENUE_BRIDGE_VS_VALUATION_BLOWOFF_GATE` against existing C09 rows before any production profile change.
6. Do not loosen Stage3-Green. Prefer Stage2 bridge, 4B watch, hard 4C confirmation, and information-confidence quality checks.
```

## 12. Next Research State

```text
completed_round = R2
completed_loop = 132
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C09 4C-empty repair and valuation blowoff vs order/revenue bridge split
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY; C18_CONSUMER_EXPORT_CHANNEL_REORDER; C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN; C22_INSURANCE_RATE_CYCLE_RESERVE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
