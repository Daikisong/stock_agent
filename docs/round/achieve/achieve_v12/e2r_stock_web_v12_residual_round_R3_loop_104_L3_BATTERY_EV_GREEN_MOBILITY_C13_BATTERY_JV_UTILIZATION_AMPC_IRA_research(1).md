# E2R Stock-Web v12 residual research — R3 loop 104 — C13_BATTERY_JV_UTILIZATION_AMPC_IRA

## 0. Metadata

```yaml
research_id: R3_L104_C13_AMPC_IRA_UTILIZATION_BRIDGE
selected_round: R3
selected_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C13 AMPC/IRA duration, JV/localization utilization failure, direct URL/proxy repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE
loop_objective:
  - sector_specific_rule_discovery
  - canonical_archetype_rule_candidate
  - counterexample_mining
  - positive_case_balance
  - 4C_thesis_break_timing_test
  - holdout_validation
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Source and scheduler check

- Main execution prompt read: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat ledger read: `docs/core/V12_Research_No_Repeat_Index.md`.
- The ledger says all C01~C32 scopes exceed 80 representative rows, so the active task is quality repair rather than raw row filling. The Priority 1 list still names C13 as a balance/quality repair target, especially for AMPC/IRA durability and JV utilization failure cases.
- Stock-Web manifest basis: FinanceData/marcap, `raw_unadjusted_marcap`, `tradable_raw`, `atlas/ohlcv_tradable_by_symbol_year`, manifest max date `2026-02-20`.
- Schema basis: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

## 2. Novelty and no-repeat audit

This run deliberately avoids the previous C13 pattern centered on listed battery-cell makers and their direct JV/AMPC rows. It uses battery-material and component suppliers where IRA/FEOC/localization vocabulary is abundant but utilization and revenue conversion quality differs sharply.

```yaml
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 3
counterexample_count: 4
stage4b_case_count: 2
stage4c_case_count: 3
source_proxy_only_count: 2
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 7
```

Hard duplicate check:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
all_keys_unique_in_this_md = true
same_symbol_same_trigger_date_research = false
schema_rematerialization_only = false
```

## 3. Case table — complete 30/90/180D MFE/MAE

| case_id | symbol | name | trigger_date | entry_date | trigger_type | outcome | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | source_proxy_only |
|---|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| C13-L104-001 | 348370 | 엔켐 | 2024-01-25 | 2024-01-25 | Stage3-Green | positive | 215.58 | 247.27 | 247.27 | -5.55 | -5.55 | -5.55 | false |
| C13-L104-002 | 020150 | 롯데에너지머티리얼즈 | 2024-08-06 | 2024-08-06 | Stage2-Actionable | positive_but_4B_watch | 32.13 | 32.13 | 32.13 | -10.71 | -39.51 | -41.82 | false |
| C13-L104-003 | 011790 | SKC | 2024-05-06 | 2024-05-07 | Stage4B | counterexample | 73.46 | 73.46 | 73.46 | -12.14 | -12.14 | -21.68 | true |
| C13-L104-004 | 336370 | 솔루스첨단소재 | 2024-10-04 | 2024-10-04 | Stage4C | counterexample | 16.79 | 16.79 | 16.79 | -28.26 | -37.76 | -44.72 | false |
| C13-L104-005 | 393890 | 더블유씨피 | 2024-02-04 | 2024-02-05 | Stage4C | counterexample | 21.92 | 21.92 | 21.92 | -4.31 | -26.35 | -62.09 | true |
| C13-L104-006 | 357780 | 솔브레인 | 2023-03-31 | 2023-04-03 | Stage2-Actionable | positive | 4.10 | 23.76 | 30.89 | -10.58 | -10.58 | -10.58 | false |
| C13-L104-007 | 278280 | 천보 | 2024-01-17 | 2024-01-18 | Stage4C | counterexample | 5.27 | 5.27 | 5.27 | -14.56 | -25.00 | -48.31 | false |

## 4. Actual Stock-Web OHLC rows used

| symbol | entry_date | open | high | low | close/entry | volume | peak_180D_date | peak_180D_high | trough_180D_date | trough_180D_low |
|---:|---|---:|---:|---:|---:|---:|---|---:|---|---:|
| 348370 | 2024-01-25 | 115600 | 124200 | 111000 | 113600 | 1144652 | 2024-04-08 | 394500 | 2024-01-26 | 107300 |
| 020150 | 2024-08-06 | 32200 | 34700 | 32200 | 34550 | 311633 | 2024-09-05 | 45650 | 2025-04-09 | 20100 |
| 011790 | 2024-05-07 | 115100 | 117200 | 111400 | 115300 | 291125 | 2024-06-18 | 200000 | 2024-12-09 | 90300 |
| 336370 | 2024-10-04 | 12170 | 12540 | 12150 | 12210 | 112479 | 2024-10-07 | 14260 | 2025-04-09 | 6750 |
| 393890 | 2024-02-05 | 41600 | 41800 | 40500 | 40600 | 118090 | 2024-03-07 | 49500 | 2024-10-25 | 15390 |
| 357780 | 2023-04-03 | 235500 | 235500 | 229000 | 231500 | 25887 | 2023-12-11 | 303000 | 2023-04-27 | 207000 |
| 278280 | 2024-01-18 | 95900 | 97200 | 94400 | 94800 | 29672 | 2024-02-21 | 99800 | 2024-08-05 | 49000 |

## 5. Evidence notes by case

### C13-L104-001 — 348370 엔켐 — positive Green path

Enchem's North America electrolyte evidence is unusually clean for C13 because the trigger links customer supply, local production and IRA/FEOC geography. The article reports contracts with global top-tier customers including LG Energy Solution and SK On, a Georgia plant with 40,000 tons of annual electrolyte capacity, supply to SK On's Georgia plant and Ultium Cells, and planned supply to BlueOval/SK On-Ford and Ultium Tennessee. This is not merely policy vocabulary; it is a customer-and-plant bridge.

Stage interpretation: `Stage3-Green`, but with a note that the enormous 90D MFE is a right-tail outcome, not an excuse to loosen C13 broadly.

### C13-L104-002 — 020150 롯데에너지머티리얼즈 — positive, but Green blocked by drawdown

The official Q2 2024 release says North American sales increased 243% YoY, sales and operating profit improved, and the company remained profitable in copper foil. However, it also discloses inventory valuation, global logistics cost and policy uncertainty. Price confirmed both sides: strong 30D MFE, then a deep 90D/180D drawdown.

Stage interpretation: `Stage2-Actionable` with local 4B watch. The case is usable as a positive evidence bridge, but not as Green evidence without utilization/margin durability.

### C13-L104-003 — 011790 SKC — utilization/cost stress despite localization narrative

SK Nexilis had a genuine copper-foil localization story, but the trigger evidence was not positive conversion. It was voluntary retirement, cost relocation to Malaysia/overseas, and Q1 operating loss. The price path gave a short squeeze-like MFE, then deteriorated. This is exactly where C13 needs a utilization-to-profit gate.

Stage interpretation: `Stage4B`. Do not treat overseas copper-foil capacity as positive C13 evidence when the contemporaneous proof is fixed-cost and utilization stress.

### C13-L104-004 — 336370 솔루스첨단소재 — long-dated incentive without current utilization

Solus has direct company evidence for Europe/Quebec battery foil bases and a North America first-plant narrative. But the case's October 2024 setup remained long-dated and capex/incentive-led, not current utilization or revenue-led. The Stock-Web path showed shallow early MFE and severe 30/90/180D MAE.

Stage interpretation: `Stage4C` when market outcome confirms that incentive/headline evidence lacked customer and revenue conversion.

### C13-L104-005 — 393890 더블유씨피 — IRA separator component tailwind without confirmed North America contract

WCP's CEO described FEOC/IRA opportunity and plans to accelerate North America entry, but the same source says location was still under consideration and future overseas contracts would be decided later. The price path had a brief 30D MFE but then a 180D collapse.

Stage interpretation: `Stage4C`. Separator classification and policy vocabulary are not enough; contract, plant decision and utilization bridge are required.

### C13-L104-006 — 357780 솔브레인 — product bridge plus policy tailwind, but no named customer contract

Soulbrain's company page directly shows electrolyte and lead-tab secondary battery materials. The Treasury/IRS 30D guidance created a real policy tailwind for Korean FTA-source materials, but the stock-specific evidence lacks a named North America customer or JV contract.

Stage interpretation: `Stage2-Actionable`. Product + policy bridge earns a watchable positive, but not Green.

### C13-L104-007 — 278280 천보 — regulatory comment without conversion

The company-side regulatory comment identifies electrolyte salts/additives, but the stock-specific bridge is thin: no named customer, no utilization proof, no current revenue or margin bridge. The Stock-Web outcome was a low-MFE/high-MAE failure.

Stage interpretation: `Stage4C`. Policy-eligibility language alone should not unlock positive stage credit.

## 6. Score/return alignment and component stress test

Component order is `EPS/FCF`, `Visibility`, `Bottleneck/Pricing`, `Market Mispricing`, `Valuation Rerating`, `Capital Allocation`, `Information Confidence`.

| case_id | symbol | EPS | Vis | Bott | Mis | Val | Cap | Info | current_total_proxy | after_shadow_rule | current_profile_error |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C13-L104-001 | 348370 | 20 | 24 | 13 | 11 | 8 | 12 | 15 | 103 | 105 | too_late_or_undercredited |
| C13-L104-002 | 020150 | 13 | 21 | 11 | 10 | 8 | 10 | 13 | 78 | 74 | green_too_early_without_utilization_drawdown_gate |
| C13-L104-003 | 011790 | 7 | 9 | 8 | 16 | 15 | 5 | 16 | 74 | 63 | false_positive_or_4c_too_late |
| C13-L104-004 | 336370 | 3 | 5 | 5 | 8 | 6 | 5 | 30 | 62 | 62 | false_positive_or_4c_too_late |
| C13-L104-005 | 393890 | 3 | 5 | 5 | 8 | 6 | 5 | 30 | 62 | 62 | false_positive_or_4c_too_late |
| C13-L104-006 | 357780 | 13 | 21 | 11 | 10 | 8 | 10 | 13 | 86 | 88 | too_late_or_undercredited |
| C13-L104-007 | 278280 | 3 | 5 | 5 | 8 | 6 | 5 | 30 | 62 | 62 | false_positive_or_4c_too_late |

Return alignment notes:

- `348370` confirms that C13 can be a true structural winner when customer supply + US local production + capacity response all arrive together.
- `020150` and `011790` show why Green cannot be unlocked by North America vocabulary alone. Both had sharp MFE, but the forward drawdown says margin/utilization quality must stay in the rule.
- `336370`, `393890`, and `278280` are the cleanest counterexamples: incentive, IRA component status, and additive/electrolyte vocabulary did not become utilization, customer, revenue, or margin proof.
- `357780` is a Stage2-positive control: actual product exposure plus policy tailwind can matter, but without named customer economics it stays below Yellow/Green.

## 7. JSONL trigger rows

```jsonl
{"row_type":"trigger","research_id":"R3_L104_C13_AMPC_IRA_UTILIZATION_BRIDGE","case_id":"C13-L104-001","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE","symbol":"348370","name":"엔켐","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":113600.0,"trigger_type":"Stage3-Green","outcome_label":"positive","MFE_30D_pct":215.58,"MFE_90D_pct":247.27,"MFE_180D_pct":247.27,"MAE_30D_pct":-5.55,"MAE_90D_pct":-5.55,"MAE_180D_pct":-5.55,"peak_180D_date":"2024-04-08","peak_180D_high":394500.0,"trough_180D_date":"2024-01-26","trough_180D_low":107300.0,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"source_proxy_only":false,"evidence_url":"https://www.asiae.co.kr/en/article/2024012508342937399","evidence_family":"customer_supply_contracts_plus_US_local_capacity_plus_FEOC_IRA_tailwind","trigger_family":"NORTH_AMERICA_ELECTROLYTE_SUPPLY_CONTRACTS_AND_LOCAL_PRODUCTION","current_profile_error":"too_late_or_undercredited","component_breakdown":{"eps_fcf":20,"visibility":24,"bottleneck":13,"mispricing":11,"valuation":8,"capital":12,"info":15},"score_total_current_proxy":103,"score_total_after_shadow_rule":105,"do_not_count_as_new_case":false}
{"row_type":"trigger","research_id":"R3_L104_C13_AMPC_IRA_UTILIZATION_BRIDGE","case_id":"C13-L104-002","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_date":"2024-08-06","entry_date":"2024-08-06","entry_price":34550.0,"trigger_type":"Stage2-Actionable","outcome_label":"positive_but_4B_watch","MFE_30D_pct":32.13,"MFE_90D_pct":32.13,"MFE_180D_pct":32.13,"MAE_30D_pct":-10.71,"MAE_90D_pct":-39.51,"MAE_180D_pct":-41.82,"peak_180D_date":"2024-09-05","peak_180D_high":45650.0,"trough_180D_date":"2025-04-09","trough_180D_low":20100.0,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"source_proxy_only":false,"evidence_url":"https://lotteenergymaterials.com/en/pr/promotion_detail.do?seq=79","evidence_family":"North_America_sales_growth_plus_copper_foil_customer_tests_plus_profit_bridge","trigger_family":"NORTH_AMERICA_COPPER_FOIL_SALES_AND_CUSTOMER_QUALITY_TEST","current_profile_error":"green_too_early_without_utilization_drawdown_gate","component_breakdown":{"eps_fcf":13,"visibility":21,"bottleneck":11,"mispricing":10,"valuation":8,"capital":10,"info":13},"score_total_current_proxy":78,"score_total_after_shadow_rule":74,"do_not_count_as_new_case":false}
{"row_type":"trigger","research_id":"R3_L104_C13_AMPC_IRA_UTILIZATION_BRIDGE","case_id":"C13-L104-003","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE","symbol":"011790","name":"SKC","trigger_date":"2024-05-06","entry_date":"2024-05-07","entry_price":115300.0,"trigger_type":"Stage4B","outcome_label":"counterexample","MFE_30D_pct":73.46,"MFE_90D_pct":73.46,"MFE_180D_pct":73.46,"MAE_30D_pct":-12.14,"MAE_90D_pct":-12.14,"MAE_180D_pct":-21.68,"peak_180D_date":"2024-06-18","peak_180D_high":200000.0,"trough_180D_date":"2024-12-09","trough_180D_low":90300.0,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"source_proxy_only":true,"evidence_url":"https://www.mk.co.kr/en/business/11008446","evidence_family":"voluntary_retirement_plus_Malaysia_relocation_plus_Q1_operating_loss","trigger_family":"COPPER_FOIL_UTILIZATION_COST_RELOCATION_AND_OPERATING_LOSS","current_profile_error":"false_positive_or_4c_too_late","component_breakdown":{"eps_fcf":7,"visibility":9,"bottleneck":8,"mispricing":16,"valuation":15,"capital":5,"info":16},"score_total_current_proxy":74,"score_total_after_shadow_rule":63,"do_not_count_as_new_case":false}
{"row_type":"trigger","research_id":"R3_L104_C13_AMPC_IRA_UTILIZATION_BRIDGE","case_id":"C13-L104-004","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE","symbol":"336370","name":"솔루스첨단소재","trigger_date":"2024-10-04","entry_date":"2024-10-04","entry_price":12210.0,"trigger_type":"Stage4C","outcome_label":"counterexample","MFE_30D_pct":16.79,"MFE_90D_pct":16.79,"MFE_180D_pct":16.79,"MAE_30D_pct":-28.26,"MAE_90D_pct":-37.76,"MAE_180D_pct":-44.72,"peak_180D_date":"2024-10-07","peak_180D_high":14260.0,"trough_180D_date":"2025-04-09","trough_180D_low":6750.0,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"source_proxy_only":false,"evidence_url":"https://www.solusadvancedmaterials.com/en/business/b-foil/","evidence_family":"North_America_first_plant_plus_government_incentive_but_2026_mass_production","trigger_family":"QUEBEC_COPPER_FOIL_INCENTIVE_LONG_DATED_CAPACITY","current_profile_error":"false_positive_or_4c_too_late","component_breakdown":{"eps_fcf":3,"visibility":5,"bottleneck":5,"mispricing":8,"valuation":6,"capital":5,"info":30},"score_total_current_proxy":62,"score_total_after_shadow_rule":62,"do_not_count_as_new_case":false}
{"row_type":"trigger","research_id":"R3_L104_C13_AMPC_IRA_UTILIZATION_BRIDGE","case_id":"C13-L104-005","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE","symbol":"393890","name":"더블유씨피","trigger_date":"2024-02-04","entry_date":"2024-02-05","entry_price":40600.0,"trigger_type":"Stage4C","outcome_label":"counterexample","MFE_30D_pct":21.92,"MFE_90D_pct":21.92,"MFE_180D_pct":21.92,"MAE_30D_pct":-4.31,"MAE_90D_pct":-26.35,"MAE_180D_pct":-62.09,"peak_180D_date":"2024-03-07","peak_180D_high":49500.0,"trough_180D_date":"2024-10-25","trough_180D_low":15390.0,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"source_proxy_only":true,"evidence_url":"https://www.mk.co.kr/en/business/10936153","evidence_family":"FEOC_IRA_tailwind_plus_customer_plan_but_location_and_contract_unconfirmed","trigger_family":"IRA_SEPARATOR_COMPONENT_NORTH_AMERICA_CONSIDERATION_NOT_CONFIRMED","current_profile_error":"false_positive_or_4c_too_late","component_breakdown":{"eps_fcf":3,"visibility":5,"bottleneck":5,"mispricing":8,"valuation":6,"capital":5,"info":30},"score_total_current_proxy":62,"score_total_after_shadow_rule":62,"do_not_count_as_new_case":false}
{"row_type":"trigger","research_id":"R3_L104_C13_AMPC_IRA_UTILIZATION_BRIDGE","case_id":"C13-L104-006","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE","symbol":"357780","name":"솔브레인","trigger_date":"2023-03-31","entry_date":"2023-04-03","entry_price":231500.0,"trigger_type":"Stage2-Actionable","outcome_label":"positive","MFE_30D_pct":4.1,"MFE_90D_pct":23.76,"MFE_180D_pct":30.89,"MAE_30D_pct":-10.58,"MAE_90D_pct":-10.58,"MAE_180D_pct":-10.58,"peak_180D_date":"2023-12-11","peak_180D_high":303000.0,"trough_180D_date":"2023-04-27","trough_180D_low":207000.0,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"source_proxy_only":false,"evidence_url":"https://www.soulbrain.co.kr/en/m23.php","evidence_family":"Treasury_30D_guidance_plus_company_electrolyte_supply_business","trigger_family":"IRA_ELECTROLYTE_MATERIAL_QUALIFYING_SOURCE_PLUS_COMPANY_PRODUCT_BRIDGE","current_profile_error":"too_late_or_undercredited","component_breakdown":{"eps_fcf":13,"visibility":21,"bottleneck":11,"mispricing":10,"valuation":8,"capital":10,"info":13},"score_total_current_proxy":86,"score_total_after_shadow_rule":88,"do_not_count_as_new_case":false}
{"row_type":"trigger","research_id":"R3_L104_C13_AMPC_IRA_UTILIZATION_BRIDGE","case_id":"C13-L104-007","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE","symbol":"278280","name":"천보","trigger_date":"2024-01-17","entry_date":"2024-01-18","entry_price":94800.0,"trigger_type":"Stage4C","outcome_label":"counterexample","MFE_30D_pct":5.27,"MFE_90D_pct":5.27,"MFE_180D_pct":5.27,"MAE_30D_pct":-14.56,"MAE_90D_pct":-25.0,"MAE_180D_pct":-48.31,"peak_180D_date":"2024-02-21","peak_180D_high":99800.0,"trough_180D_date":"2024-08-05","trough_180D_low":49000.0,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"source_proxy_only":false,"evidence_url":"https://www.regulations.gov/comment/IRS-2023-0059-0010","evidence_family":"company_regulatory_comment_plus_electrolyte_salts_additives_but_no_customer_utilization_bridge","trigger_family":"ELECTROLYTE_ADDITIVE_IRA_COMMENT_WITHOUT_REVENUE_CONVERSION","current_profile_error":"false_positive_or_4c_too_late","component_breakdown":{"eps_fcf":3,"visibility":5,"bottleneck":5,"mispricing":8,"valuation":6,"capital":5,"info":30},"score_total_current_proxy":62,"score_total_after_shadow_rule":62,"do_not_count_as_new_case":false}
```

## 8. Aggregate and residual contribution

```yaml
aggregate_scope: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
representative_trigger_candidate_count: 7
positive_case_count: 3
counterexample_count: 4
4B_case_count: 2
4C_case_count: 3
source_proxy_only_count: 2
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
calibration_usable_rate: 1.00
residual_error_family:
  - IRA_or_FEOC_vocabulary_overcredit
  - long_dated_capacity_incentive_without_utilization
  - North_America_localization_without_customer_revenue_bridge
  - copper_foil_separator_electrolyte_component_tailwind_without_margin_durability
```

Residual contribution summary:

C13 should not score AMPC/IRA/JV/localization words as if they are cash. The evidence must show whether the credit/localization tailwind has passed through the pipe into customer shipments, plant utilization, revenue, margin, or capital recovery. If the tailwind is still only a map arrow on a factory plan, the correct stage is Watch/4B/4C, not Green.

## 9. Shadow rule candidate

```yaml
new_axis_proposed: C13_AMPC_IRA_LOCALIZATION_UTILIZATION_REVENUE_GATE
sector_specific_rule_candidate: L3 battery materials/component localization should require customer shipment/utilization/revenue/margin bridge before positive stage escalation.
canonical_archetype_rule_candidate: |
  For C13_BATTERY_JV_UTILIZATION_AMPC_IRA, AMPC/IRA/FEOC/JV/North-America localization evidence
  can open Stage2 only when at least two of the following are present:
    1. named customer or JV plant receiving product,
    2. plant already operating or shipment started,
    3. utilization/capacity conversion evidence,
    4. revenue/OP/margin bridge,
    5. credit/subsidy recognized in financials,
    6. capex funding and timeline de-risked.
  If evidence is only future plant/incentive/policy vocabulary, cap at Stage4B watch.
  If forward outcome and non-price evidence confirm no customer/utilization/revenue bridge, route to Stage4C.
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - drawdown_aware_confirmation
  - information_confidence_gate
existing_axis_weakened: null
suggested_shadow_weight_delta:
  before_EPS_Vis_Bott_Mis_Val_Cap_Info: 20/18/14/12/10/10/16
  after_EPS_Vis_Bott_Mis_Val_Cap_Info: 19/21/13/10/9/12/16
  delta: -1/+3/-1/-2/-1/+2/0
production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: false
```

Mechanism:

AMPC/IRA is wind at the harbor mouth. C13 only becomes a rerating engine when that wind turns a real turbine: customer plant, local production, utilization, shipments, accounting credit and margin. Otherwise the stock is sailing on a weather forecast, not on propulsion.

## 10. Batch ingest self-audit

```yaml
required_filename_regex_pass: true
filename: e2r_stock_web_v12_residual_round_R3_loop_104_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
filename_round: R3
metadata_round: R3
filename_loop: 104
metadata_loop: 104
large_sector_id_valid: true
canonical_archetype_id_valid: true
round_sector_consistency: pass
trigger_type_canonical_labels_only: true
all_trigger_rows_have_MFE_30D_pct: true
all_trigger_rows_have_MFE_90D_pct: true
all_trigger_rows_have_MFE_180D_pct: true
all_trigger_rows_have_MAE_30D_pct: true
all_trigger_rows_have_MAE_90D_pct: true
all_trigger_rows_have_MAE_180D_pct: true
entry_price_present_all_rows: true
entry_date_present_all_rows: true
price_basis_tradable_raw_all_rows: true
raw_all_basis_used_for_calibration: false
corporate_action_180D_blocked_rows: 0
insufficient_forward_window_rows: 0
source_url_present_all_rows: true
source_proxy_rows_flagged: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not rerun this research as a live scan. Parse this Markdown as one v12 residual calibration result.

Scope:
- large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
- canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
- fine_archetype_id = IRA_BATTERY_MATERIAL_LOCALIZATION_UTILIZATION_REVENUE_GATE

Candidate patch:
- axis = C13_AMPC_IRA_LOCALIZATION_UTILIZATION_REVENUE_GATE
- production_scoring_changed_in_research = false
- apply only through batch calibration if enough representative rows survive validation.

Validation steps:
1. Parse JSONL rows under section 7.
2. Confirm every row has entry_date, entry_price, MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Respect source_proxy_only flags.
5. Do not loosen Stage3-Green thresholds.
6. Treat this as a shadow rule candidate, not an immediate production patch.
```

## 12. Completion state

```yaml
completed_round: R3
completed_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality repair — C13 AMPC/IRA duration, JV/localization utilization failure, direct URL/proxy repair
next_recommended_archetypes:
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
