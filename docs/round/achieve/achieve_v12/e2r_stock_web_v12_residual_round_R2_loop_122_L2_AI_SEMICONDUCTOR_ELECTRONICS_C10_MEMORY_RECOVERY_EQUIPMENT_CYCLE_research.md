# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_122_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selected_round: R2
selected_loop: 122
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under_30_representative_rows / C10 rows 13 need_to_30 17 need_to_50 37 before local follow-up; session-local previous C10 loop_121 avoided by new symbol/date/evidence families
round_schedule_status: coverage_index_selected
round_sector_consistency: pass: C06-C10 maps to R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_EQUIPMENT_PARTS_UTILIZATION_RECOVERY_CONVERSION_VS_LATE_COMPONENT_REPRICE
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
investment_recommendation: false
loop_objective:
  - coverage_gap_fill
  - followup_new_symbol_date_family
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - stage2_actionable_bonus_stress_test
  - canonical_archetype_compression
  - sector_specific_rule_discovery
```

This MD is a standalone historical calibration artifact. It does not recommend any current position, does not scan live candidates, does not patch `stock_agent`, and does not change production scoring. It only creates shadow-rule evidence for later batch ingestion.

## 1. Coverage-Index Selection

- `V12_Research_No_Repeat_Index.md` still lists `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` as Priority 0 with 13 representative rows before this local follow-up.
- Previous session-local C10 loop `121` used EugeneTech, PSK, TES, Wonik IPS, VM, Exicon, and PSK Holdings. This follow-up avoids those strict keys and uses six new symbols: Jusung Engineering, KCTech, KoMiCo, Hana Materials, Wonik QnC, and TCK.
- C10 maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`; no R13 naming is used because this is sector-specific, not cross-archetype red-team.

```text
strict_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_count = 0
new_independent_case_ratio = 1.00
minimum_new_symbol_count_pass = true
minimum_positive_case_count_pass = true
minimum_counterexample_count_pass = true
```

## 2. Stock-Web Price Atlas Validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
entry_price_basis = close c column on entry_date
MFE_basis = max high h over forward 30/90/180 trading-row windows
MAE_basis = min low l over forward 30/90/180 trading-row windows
```

All six selected rows have complete 30D/90D/180D windows inside the stock-web manifest horizon. Corporate-action candidate dates visible in the profiles are historical and outside the entry-to-D+180 windows used here, so the selected trigger rows are `calibration_usable=true`.

## 3. Evidence Ledger

| evidence_id | source | as_of use | URL/proxy note |
|---|---|---|---|
| EV_C10_FU122_JUSUNG_20240806_ETNEWS_BUSINESSKOREA | 주성엔지니어링 / 2024-08-06 | 2Q24 result confirmed revenue recovery, operating profit turnaround, high margin, semiconductor/ALD equipment delivery and backlog language. This is not just memory beta; it is equipment revenue/margin conversion. | https://www.etnews.com/20240806000292 ; https://www.businesskorea.co.kr/news/articleView.html?idxno=222514 |
| EV_C10_FU122_KCTECH_20240603_MIRAE | 케이씨텍 / 2024-06-03 | CMP equipment and slurry exposure had direct C10 relevance and 2H24 memory capex attention, but the stock had already repriced sharply and later gave back most of the move. The correct output is Stage2-Actionable evidence plus local 4B overlay, not fresh Green. | https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2323858 |
| EV_C10_FU122_KOMICO_20250404_IR | 코미코 / 2025-04-04 | IR deck shows 4Q24 revenue of KRW 127.8bn, YoY +42.0%, and explicitly links cleaning/coating demand growth to recovery of memory chip manufacturer utilization rates; OP also improved YoY. This is a direct utilization-to-service-volume bridge. | https://file.alphasquare.co.kr/media/pdfs/company-ir/20250404%EC%BD%94%EB%AF%B8%EC%BD%94_%ED%9A%8C%EC%82%AC%EC%86%8C%EA%B0%9C_%EB%B0%8F_%EA%B2%BD%EC%98%81%ED%98%84%ED%99%A9_%EC%84%A4%EB%AA%85.pdf |
| EV_C10_FU122_HANA_MATERIALS_20240516_HANA_SECURITIES | 하나머티리얼즈 / 2024-05-15 | 1Q24 review said parts shipments were recovering with memory utilization, Si part sales rose QoQ, and SiC-related other parts rose sharply; the same source warned NAND investment recovery would take time and benefits would reflect later. Price path turns this into local 4B/guardrail. | https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/05/15/HanaM_240516.pdf |
| EV_C10_FU122_WONIK_QNC_20240308_DAILYINVEST | 원익QnC / 2024-03-08 | Reports framed 4Q23 as the earnings trough and 2024 quartz revenue as recovering with semiconductor cycle/utilization improvement. This was a valid C10 watch signal, but the later price path shows that quartz-cycle confirmation needs a 4B profit-lock overlay after rapid MFE. | https://www.dailyinvest.kr/news/articleView.html?idxno=57546 |
| EV_C10_FU122_TCK_20250204_DAILYINVEST | 티씨케이 / 2025-02-04 | The article connected 2024 memory utilization recovery to SiC demand, V8 NAND SiC focus-ring demand, DRAM utilization recovery and low customer SiC ring inventory, while forecasting 2025 growth and margin improvement. This is a direct memory-utilization-to-consumables route. | https://www.dailyinvest.kr/news/articleView.html?idxno=63240 |

## 4. Mechanism Compression

C10 is not a generic “memory upcycle” label. The useful chain is narrower:

```text
memory ASP / utilization / capex recovery
  -> equipment, parts, consumables, cleaning/coating or CMP demand
  -> shipment / revenue / margin conversion
  -> price path with acceptable MAE or a separate local 4B after fast MFE
```

If the chain stops at memory beta, the row stays Stage2-watch. If the conversion bridge is real but the stock has already delivered a large MFE and then opens a large MAE path, the right output is not new Green; it is `Stage4B_watch` or `Stage2-Actionable+4B`.

## 5. Case Notes

### C10_FU122_036930_20240806 — 주성엔지니어링 (036930)

- **Trigger:** `Stage2-Actionable` on `2024-08-06`; entry `2024-08-06` at `25100`.
- **Evidence family:** `ALD_equipment_delivery_margin_recovery_after_2Q24_result`.
- **Evidence summary:** 2Q24 result confirmed revenue recovery, operating profit turnaround, high margin, semiconductor/ALD equipment delivery and backlog language. This is not just memory beta; it is equipment revenue/margin conversion.
- **Path:** MFE30/90/180 = `20.52 / 35.66 / 72.91`; MAE30/90/180 = `-12.15 / -12.15 / -12.15`; peak `2025-03-21` at `43400`, post-peak drawdown `-23.5%`.
- **Calibration verdict:** `positive`; current profile residual = `current_profile_too_late_if_waiting_for_later_sector_confirmation`; shadow label = `Stage2-Actionable`.

### C10_FU122_281820_20240603 — 케이씨텍 (281820)

- **Trigger:** `Stage4B` on `2024-06-03`; entry `2024-06-03` at `38900`.
- **Evidence family:** `CMP_equipment_memory_supplier_capex_2H24_but_crowded_entry`.
- **Evidence summary:** CMP equipment and slurry exposure had direct C10 relevance and 2H24 memory capex attention, but the stock had already repriced sharply and later gave back most of the move. The correct output is Stage2-Actionable evidence plus local 4B overlay, not fresh Green.
- **Path:** MFE30/90/180 = `51.67 / 51.67 / 51.67`; MAE30/90/180 = `-3.08 / -24.29 / -35.35`; peak `2024-07-11` at `59000`, post-peak drawdown `-57.37%`.
- **Calibration verdict:** `counterexample`; current profile residual = `current_profile_4b_too_late_after_fast_reprice`; shadow label = `Stage2-Actionable+Stage4B_watch`.

### C10_FU122_183300_20250404 — 코미코 (183300)

- **Trigger:** `Stage2-Actionable` on `2025-04-04`; entry `2025-04-04` at `56900`.
- **Evidence family:** `cleaning_coating_demand_from_memory_utilization_recovery`.
- **Evidence summary:** IR deck shows 4Q24 revenue of KRW 127.8bn, YoY +42.0%, and explicitly links cleaning/coating demand growth to recovery of memory chip manufacturer utilization rates; OP also improved YoY. This is a direct utilization-to-service-volume bridge.
- **Path:** MFE30/90/180 = `15.11 / 41.48 / 125.83`; MAE30/90/180 = `-11.6 / -11.6 / -11.6`; peak `2025-10-20` at `128500`, post-peak drawdown `-37.82%`.
- **Calibration verdict:** `positive`; current profile residual = `current_profile_undercredits_parts_service_utilization_recovery`; shadow label = `Stage2-Actionable`.

### C10_FU122_166090_20240516 — 하나머티리얼즈 (166090)

- **Trigger:** `Stage4B` on `2024-05-15`; entry `2024-05-16` at `53500`.
- **Evidence family:** `Si_SiC_parts_recovery_report_with_NAND_recovery_timing_risk`.
- **Evidence summary:** 1Q24 review said parts shipments were recovering with memory utilization, Si part sales rose QoQ, and SiC-related other parts rose sharply; the same source warned NAND investment recovery would take time and benefits would reflect later. Price path turns this into local 4B/guardrail.
- **Path:** MFE30/90/180 = `24.49 / 29.53 / 29.53`; MAE30/90/180 = `-8.79 / -48.22 / -59.16`; peak `2024-07-02` at `69300`, post-peak drawdown `-68.47%`.
- **Calibration verdict:** `counterexample`; current profile residual = `current_profile_false_positive_if_report_language_upgrades_to_yellow_without_forward_NAND_order_survival`; shadow label = `Stage4B_watch`.

### C10_FU122_074600_20240315 — 원익QnC (074600)

- **Trigger:** `Stage4B` on `2024-03-08`; entry `2024-03-15` at `28800`.
- **Evidence family:** `quartz_revenue_recovery_report_but_cycle_peak_risk`.
- **Evidence summary:** Reports framed 4Q23 as the earnings trough and 2024 quartz revenue as recovering with semiconductor cycle/utilization improvement. This was a valid C10 watch signal, but the later price path shows that quartz-cycle confirmation needs a 4B profit-lock overlay after rapid MFE.
- **Path:** MFE30/90/180 = `22.92 / 42.36 / 42.36`; MAE30/90/180 = `-1.56 / -1.56 / -42.08`; peak `2024-06-07` at `41000`, post-peak drawdown `-59.32%`.
- **Calibration verdict:** `counterexample`; current profile residual = `current_profile_4b_too_late_for_components_after_early_MFE`; shadow label = `Stage2-Actionable+Stage4B_watch`.

### C10_FU122_064760_20250204 — 티씨케이 (064760)

- **Trigger:** `Stage2-Actionable` on `2025-02-04`; entry `2025-02-04` at `72300`.
- **Evidence family:** `SiC_focus_ring_dram_NAND_utilization_recovery_and_low_inventory_route`.
- **Evidence summary:** The article connected 2024 memory utilization recovery to SiC demand, V8 NAND SiC focus-ring demand, DRAM utilization recovery and low customer SiC ring inventory, while forecasting 2025 growth and margin improvement. This is a direct memory-utilization-to-consumables route.
- **Path:** MFE30/90/180 = `30.43 / 44.26 / 174.55`; MAE30/90/180 = `-2.21 / -2.21 / -2.21`; peak `2025-10-10` at `198500`, post-peak drawdown `-17.43%`.
- **Calibration verdict:** `positive`; current profile residual = `current_profile_too_late_if_it_requires_equipment_PO_and_undercredits_consumable_utilization`; shadow label = `Stage2-Actionable`.

## 6. Price Path Table

| case_id | symbol | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | post-peak DD | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| C10_FU122_036930_20240806 | 036930 | Stage2-Actionable | 2024-08-06 | 25100 | 20.52 | 35.66 | 72.91 | -12.15 | -12.15 | -12.15 | 2025-03-21 / 43400 | -23.5 | positive |
| C10_FU122_281820_20240603 | 281820 | Stage4B | 2024-06-03 | 38900 | 51.67 | 51.67 | 51.67 | -3.08 | -24.29 | -35.35 | 2024-07-11 / 59000 | -57.37 | counterexample |
| C10_FU122_183300_20250404 | 183300 | Stage2-Actionable | 2025-04-04 | 56900 | 15.11 | 41.48 | 125.83 | -11.6 | -11.6 | -11.6 | 2025-10-20 / 128500 | -37.82 | positive |
| C10_FU122_166090_20240516 | 166090 | Stage4B | 2024-05-16 | 53500 | 24.49 | 29.53 | 29.53 | -8.79 | -48.22 | -59.16 | 2024-07-02 / 69300 | -68.47 | counterexample |
| C10_FU122_074600_20240315 | 074600 | Stage4B | 2024-03-15 | 28800 | 22.92 | 42.36 | 42.36 | -1.56 | -1.56 | -42.08 | 2024-06-07 / 41000 | -59.32 | counterexample |
| C10_FU122_064760_20250204 | 064760 | Stage2-Actionable | 2025-02-04 | 72300 | 30.43 | 44.26 | 174.55 | -2.21 | -2.21 | -2.21 | 2025-10-10 / 198500 | -17.43 | positive |

## 7. Current Profile Stress Test

| pattern | rows | residual error | shadow correction |
|---|---|---|---|
| direct equipment/revenue/margin conversion | Jusung, KoMiCo, TCK | current profile can under-credit non-PO consumable/utilization routes if it waits only for formal equipment order language | allow Stage2-Actionable when utilization recovery is explicitly tied to shipment/revenue/OP margin bridge |
| crowded component-cycle confirmation | KCTech, Hana Materials, Wonik QnC | Stage2/Yellow can arrive after a 20%+ MFE and miss deep MAE | add local 4B/profit-lock overlay after fast MFE when forward order/margin survival is not yet durable |
| memory beta only | any row without utilization/order/revenue bridge | generic memory recovery headlines should not unlock Yellow/Green | keep Stage2-watch unless the bridge reaches conversion evidence |

## 8. Proposed Shadow Rule

```text
rule_candidate = C10_MEMORY_RECOVERY_REQUIRES_UTILIZATION_OR_ORDER_TO_REVENUE_MARGIN_BRIDGE_WITH_LATE_COMPONENT_4B_CAP

IF canonical_archetype_id == C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:
  Stage2-watch is allowed for memory ASP/capex/utilization recovery plus credible equipment/parts exposure.
  Stage2-Actionable requires at least one direct bridge:
    - named customer/order/shipment route,
    - utilization recovery explicitly tied to parts or cleaning/coating demand,
    - revenue or OP margin conversion visible in result/IR/report,
    - consumables inventory drawdown/reorder route.
  Stage3-Yellow requires conversion bridge + forward survival, not just beta or relative strength.
  If MFE30 or MFE90 already exceeds roughly 20-30% and fresh conversion evidence is not incremental,
    apply local Stage4B watch / profit-lock overlay.
  If MAE90 or MAE180 breaches roughly -35% after a late report headline,
    treat as counterexample against new Yellow/Green even if the source language was true.
```

## 9. Machine-Readable Rows

### 9.1 case rows
```jsonl
{"row_type":"case","case_id":"C10_FU122_036930_20240806","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"ALD_EQUIPMENT_DELIVERY_MARGIN_RECOVERY_AFTER_MEMORY_CUSTOMER_ORDER","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late_if_waiting_for_later_sector_confirmation","price_source":"Songdaiki/stock-web","notes":"2Q24 result confirmed revenue recovery, operating profit turnaround, high margin, semiconductor/ALD equipment delivery and backlog language. This is not just memory beta; it is equipment revenue/margin conversion."}
{"row_type":"case","case_id":"C10_FU122_281820_20240603","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CMP_EQUIPMENT_MEMORY_CAPEX_ATTENTION_AFTER_FAST_REPRICE","case_type":"high_mfe_then_deep_mae_guardrail","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_guardrail","current_profile_verdict":"current_profile_4b_too_late_after_fast_reprice","price_source":"Songdaiki/stock-web","notes":"CMP equipment and slurry exposure had direct C10 relevance and 2H24 memory capex attention, but the stock had already repriced sharply and later gave back most of the move. The correct output is Stage2-Actionable evidence plus local 4B over"}
{"row_type":"case","case_id":"C10_FU122_183300_20250404","symbol":"183300","company_name":"코미코","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CLEANING_COATING_UTILIZATION_RECOVERY_TO_REVENUE_OP_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_undercredits_parts_service_utilization_recovery","price_source":"Songdaiki/stock-web","notes":"IR deck shows 4Q24 revenue of KRW 127.8bn, YoY +42.0%, and explicitly links cleaning/coating demand growth to recovery of memory chip manufacturer utilization rates; OP also improved YoY. This is a direct utilization-to-service-volume bridg"}
{"row_type":"case","case_id":"C10_FU122_166090_20240516","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SI_SIC_PARTS_NAND_UTILIZATION_RECOVERY_BUT_4B_AFTER_REPRICE","case_type":"real_recovery_but_late_component_reprice","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_guardrail","current_profile_verdict":"current_profile_false_positive_if_report_language_upgrades_to_yellow_without_forward_NAND_order_survival","price_source":"Songdaiki/stock-web","notes":"1Q24 review said parts shipments were recovering with memory utilization, Si part sales rose QoQ, and SiC-related other parts rose sharply; the same source warned NAND investment recovery would take time and benefits would reflect later. Pr"}
{"row_type":"case","case_id":"C10_FU122_074600_20240315","symbol":"074600","company_name":"원익QnC","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_PARTS_CYCLE_RECOVERY_WITH_PEAK_RISK_AND_DRAWNDOWN","case_type":"component_cycle_peak_risk","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_guardrail","current_profile_verdict":"current_profile_4b_too_late_for_components_after_early_MFE","price_source":"Songdaiki/stock-web","notes":"Reports framed 4Q23 as the earnings trough and 2024 quartz revenue as recovering with semiconductor cycle/utilization improvement. This was a valid C10 watch signal, but the later price path shows that quartz-cycle confirmation needs a 4B p"}
{"row_type":"case","case_id":"C10_FU122_064760_20250204","symbol":"064760","company_name":"티씨케이","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SIC_FOCUS_RING_MEMORY_UTILIZATION_RECOVERY_WITH_MARGIN_OPTIONALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late_if_it_requires_equipment_PO_and_undercredits_consumable_utilization","price_source":"Songdaiki/stock-web","notes":"The article connected 2024 memory utilization recovery to SiC demand, V8 NAND SiC focus-ring demand, DRAM utilization recovery and low customer SiC ring inventory, while forecasting 2025 growth and margin improvement. This is a direct memor"}
```

### 9.2 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"T_036930_20240806_Stage2_Actionable","case_id":"C10_FU122_036930_20240806","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"ALD_EQUIPMENT_DELIVERY_MARGIN_RECOVERY_AFTER_MEMORY_CUSTOMER_ORDER","sector":"semiconductor memory equipment / parts / consumables recovery cycle","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-06","entry_date":"2024-08-06","entry_price":25100,"evidence_available_at_that_date":"2Q24 result confirmed revenue recovery, operating profit turnaround, high margin, semiconductor/ALD equipment delivery and backlog language. This is not just memory beta; it is equipment revenue/margin conversion.","evidence_source":"EV_C10_FU122_JUSUNG_20240806_ETNEWS_BUSINESSKOREA","evidence_url":"https://www.etnews.com/20240806000292 ; https://www.businesskorea.co.kr/news/articleView.html?idxno=222514","evidence_family":"ALD_equipment_delivery_margin_recovery_after_2Q24_result","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","atlas/ohlcv_tradable_by_symbol_year/036/036930/2025.csv","atlas/ohlcv_tradable_by_symbol_year/036/036930/2026.csv"],"profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.52,"MFE_90D_pct":35.66,"MFE_180D_pct":72.91,"MAE_30D_pct":-12.15,"MAE_90D_pct":-12.15,"MAE_180D_pct":-12.15,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-21","peak_price":43400,"drawdown_after_peak_pct":-23.5,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"corporate_action_overlap_180D":false,"corporate_action_candidate_dates":["2000-06-22"],"calibration_usable":true,"validation_status":"pass","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|036930|Stage2-Actionable|2024-08-06","is_representative_for_aggregate":true,"positive_or_counterexample":"positive","current_profile_verdict":"current_profile_too_late_if_waiting_for_later_sector_confirmation","price_return_alignment":"aligned_positive"}
{"row_type":"trigger","trigger_id":"T_281820_20240603_Stage4B","case_id":"C10_FU122_281820_20240603","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CMP_EQUIPMENT_MEMORY_CAPEX_ATTENTION_AFTER_FAST_REPRICE","sector":"semiconductor memory equipment / parts / consumables recovery cycle","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-06-03","entry_date":"2024-06-03","entry_price":38900,"evidence_available_at_that_date":"CMP equipment and slurry exposure had direct C10 relevance and 2H24 memory capex attention, but the stock had already repriced sharply and later gave back most of the move. The correct output is Stage2-Actionable evidence plus local 4B overlay, not fresh Green.","evidence_source":"EV_C10_FU122_KCTECH_20240603_MIRAE","evidence_url":"https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2323858","evidence_family":"CMP_equipment_memory_supplier_capex_2H24_but_crowded_entry","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["fast_reprice","post_peak_drawdown","insufficient_fresh_order_or_margin_survival"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv","atlas/ohlcv_tradable_by_symbol_year/281/281820/2025.csv","atlas/ohlcv_tradable_by_symbol_year/281/281820/2026.csv"],"profile_path":"atlas/symbol_profiles/281/281820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":51.67,"MFE_90D_pct":51.67,"MFE_180D_pct":51.67,"MAE_30D_pct":-3.08,"MAE_90D_pct":-24.29,"MAE_180D_pct":-35.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":59000,"drawdown_after_peak_pct":-57.37,"four_b_local_peak_proximity":"local_4B_after_fast_MFE","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_should_cap_fresh_positive_after_fast_reprice","corporate_action_overlap_180D":false,"corporate_action_candidate_dates":[],"calibration_usable":true,"validation_status":"pass","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|281820|Stage4B|2024-06-03","is_representative_for_aggregate":true,"positive_or_counterexample":"counterexample","current_profile_verdict":"current_profile_4b_too_late_after_fast_reprice","price_return_alignment":"counterexample_or_guardrail"}
{"row_type":"trigger","trigger_id":"T_183300_20250404_Stage2_Actionable","case_id":"C10_FU122_183300_20250404","symbol":"183300","company_name":"코미코","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CLEANING_COATING_UTILIZATION_RECOVERY_TO_REVENUE_OP_BRIDGE","sector":"semiconductor memory equipment / parts / consumables recovery cycle","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-04","entry_date":"2025-04-04","entry_price":56900,"evidence_available_at_that_date":"IR deck shows 4Q24 revenue of KRW 127.8bn, YoY +42.0%, and explicitly links cleaning/coating demand growth to recovery of memory chip manufacturer utilization rates; OP also improved YoY. This is a direct utilization-to-service-volume bridge.","evidence_source":"EV_C10_FU122_KOMICO_20250404_IR","evidence_url":"https://file.alphasquare.co.kr/media/pdfs/company-ir/20250404%EC%BD%94%EB%AF%B8%EC%BD%94_%ED%9A%8C%EC%82%AC%EC%86%8C%EA%B0%9C_%EB%B0%8F_%EA%B2%BD%EC%98%81%ED%98%84%ED%99%A9_%EC%84%A4%EB%AA%85.pdf","evidence_family":"cleaning_coating_demand_from_memory_utilization_recovery","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/183/183300/2025.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/183/183300/2024.csv","atlas/ohlcv_tradable_by_symbol_year/183/183300/2025.csv","atlas/ohlcv_tradable_by_symbol_year/183/183300/2026.csv"],"profile_path":"atlas/symbol_profiles/183/183300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.11,"MFE_90D_pct":41.48,"MFE_180D_pct":125.83,"MAE_30D_pct":-11.6,"MAE_90D_pct":-11.6,"MAE_180D_pct":-11.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-20","peak_price":128500,"drawdown_after_peak_pct":-37.82,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"corporate_action_overlap_180D":false,"corporate_action_candidate_dates":[],"calibration_usable":true,"validation_status":"pass","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|183300|Stage2-Actionable|2025-04-04","is_representative_for_aggregate":true,"positive_or_counterexample":"positive","current_profile_verdict":"current_profile_undercredits_parts_service_utilization_recovery","price_return_alignment":"aligned_positive"}
{"row_type":"trigger","trigger_id":"T_166090_20240516_Stage4B","case_id":"C10_FU122_166090_20240516","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SI_SIC_PARTS_NAND_UTILIZATION_RECOVERY_BUT_4B_AFTER_REPRICE","sector":"semiconductor memory equipment / parts / consumables recovery cycle","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-05-15","entry_date":"2024-05-16","entry_price":53500,"evidence_available_at_that_date":"1Q24 review said parts shipments were recovering with memory utilization, Si part sales rose QoQ, and SiC-related other parts rose sharply; the same source warned NAND investment recovery would take time and benefits would reflect later. Price path turns this into local 4B/guardrail.","evidence_source":"EV_C10_FU122_HANA_MATERIALS_20240516_HANA_SECURITIES","evidence_url":"https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/05/15/HanaM_240516.pdf","evidence_family":"Si_SiC_parts_recovery_report_with_NAND_recovery_timing_risk","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["fast_reprice","post_peak_drawdown","insufficient_fresh_order_or_margin_survival"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv","atlas/ohlcv_tradable_by_symbol_year/166/166090/2025.csv","atlas/ohlcv_tradable_by_symbol_year/166/166090/2026.csv"],"profile_path":"atlas/symbol_profiles/166/166090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.49,"MFE_90D_pct":29.53,"MFE_180D_pct":29.53,"MAE_30D_pct":-8.79,"MAE_90D_pct":-48.22,"MAE_180D_pct":-59.16,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":69300,"drawdown_after_peak_pct":-68.47,"four_b_local_peak_proximity":"local_4B_after_fast_MFE","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_should_cap_fresh_positive_after_fast_reprice","corporate_action_overlap_180D":false,"corporate_action_candidate_dates":["2018-06-14","2018-07-10"],"calibration_usable":true,"validation_status":"pass","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|166090|Stage4B|2024-05-16","is_representative_for_aggregate":true,"positive_or_counterexample":"counterexample","current_profile_verdict":"current_profile_false_positive_if_report_language_upgrades_to_yellow_without_forward_NAND_order_survival","price_return_alignment":"counterexample_or_guardrail"}
{"row_type":"trigger","trigger_id":"T_074600_20240315_Stage4B","case_id":"C10_FU122_074600_20240315","symbol":"074600","company_name":"원익QnC","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_PARTS_CYCLE_RECOVERY_WITH_PEAK_RISK_AND_DRAWNDOWN","sector":"semiconductor memory equipment / parts / consumables recovery cycle","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-03-08","entry_date":"2024-03-15","entry_price":28800,"evidence_available_at_that_date":"Reports framed 4Q23 as the earnings trough and 2024 quartz revenue as recovering with semiconductor cycle/utilization improvement. This was a valid C10 watch signal, but the later price path shows that quartz-cycle confirmation needs a 4B profit-lock overlay after rapid MFE.","evidence_source":"EV_C10_FU122_WONIK_QNC_20240308_DAILYINVEST","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=57546","evidence_family":"quartz_revenue_recovery_report_but_cycle_peak_risk","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["fast_reprice","post_peak_drawdown","insufficient_fresh_order_or_margin_survival"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv","atlas/ohlcv_tradable_by_symbol_year/074/074600/2025.csv","atlas/ohlcv_tradable_by_symbol_year/074/074600/2026.csv"],"profile_path":"atlas/symbol_profiles/074/074600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.92,"MFE_90D_pct":42.36,"MFE_180D_pct":42.36,"MAE_30D_pct":-1.56,"MAE_90D_pct":-1.56,"MAE_180D_pct":-42.08,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-07","peak_price":41000,"drawdown_after_peak_pct":-59.32,"four_b_local_peak_proximity":"local_4B_after_fast_MFE","four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_should_cap_fresh_positive_after_fast_reprice","corporate_action_overlap_180D":false,"corporate_action_candidate_dates":["2004-06-25","2004-07-21","2017-04-28","2017-05-24"],"calibration_usable":true,"validation_status":"pass","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|074600|Stage4B|2024-03-15","is_representative_for_aggregate":true,"positive_or_counterexample":"counterexample","current_profile_verdict":"current_profile_4b_too_late_for_components_after_early_MFE","price_return_alignment":"counterexample_or_guardrail"}
{"row_type":"trigger","trigger_id":"T_064760_20250204_Stage2_Actionable","case_id":"C10_FU122_064760_20250204","symbol":"064760","company_name":"티씨케이","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SIC_FOCUS_RING_MEMORY_UTILIZATION_RECOVERY_WITH_MARGIN_OPTIONALITY","sector":"semiconductor memory equipment / parts / consumables recovery cycle","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-04","entry_date":"2025-02-04","entry_price":72300,"evidence_available_at_that_date":"The article connected 2024 memory utilization recovery to SiC demand, V8 NAND SiC focus-ring demand, DRAM utilization recovery and low customer SiC ring inventory, while forecasting 2025 growth and margin improvement. This is a direct memory-utilization-to-consumables route.","evidence_source":"EV_C10_FU122_TCK_20250204_DAILYINVEST","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=63240","evidence_family":"SiC_focus_ring_dram_NAND_utilization_recovery_and_low_inventory_route","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064760/2025.csv","price_shard_paths":["atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv","atlas/ohlcv_tradable_by_symbol_year/064/064760/2025.csv","atlas/ohlcv_tradable_by_symbol_year/064/064760/2026.csv"],"profile_path":"atlas/symbol_profiles/064/064760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.43,"MFE_90D_pct":44.26,"MFE_180D_pct":174.55,"MAE_30D_pct":-2.21,"MAE_90D_pct":-2.21,"MAE_180D_pct":-2.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-10","peak_price":198500,"drawdown_after_peak_pct":-17.43,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"corporate_action_overlap_180D":false,"corporate_action_candidate_dates":[],"calibration_usable":true,"validation_status":"pass","dedupe_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|064760|Stage2-Actionable|2025-02-04","is_representative_for_aggregate":true,"positive_or_counterexample":"positive","current_profile_verdict":"current_profile_too_late_if_it_requires_equipment_PO_and_undercredits_consumable_utilization","price_return_alignment":"aligned_positive"}
```

### 9.3 score simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C10_shadow","case_id":"C10_FU122_036930_20240806","trigger_id":"T_036930_20240806_Stage2_Actionable","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable_or_Yellow_risk","raw_component_scores_after":{"backlog_visibility_score":12,"margin_bridge_score":14,"customer_quality_score":8,"valuation_repricing_score":-3},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["memory_utilization_to_order_revenue_margin_bridge","component_cycle_late_4B_overlay"],"component_delta_explanation":"C10 shadow gate gives credit only when memory recovery maps into equipment/consumables shipment, revenue, margin or utilization conversion; late component-cycle confirmation after fast MFE is capped by local 4B.","MFE_90D_pct":35.66,"MAE_90D_pct":-12.15,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late_if_waiting_for_later_sector_confirmation"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C10_shadow","case_id":"C10_FU122_281820_20240603","trigger_id":"T_281820_20240603_Stage4B","symbol":"281820","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"backlog_visibility_score":8,"margin_bridge_score":4,"relative_strength_score":12,"valuation_repricing_score":-16,"execution_risk_score":-8},"weighted_score_after":66,"stage_label_after":"Stage2-Actionable+Stage4B_watch","changed_components":["memory_utilization_to_order_revenue_margin_bridge","component_cycle_late_4B_overlay"],"component_delta_explanation":"C10 shadow gate gives credit only when memory recovery maps into equipment/consumables shipment, revenue, margin or utilization conversion; late component-cycle confirmation after fast MFE is capped by local 4B.","MFE_90D_pct":51.67,"MAE_90D_pct":-24.29,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_4b_too_late_after_fast_reprice"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C10_shadow","case_id":"C10_FU122_183300_20250404","trigger_id":"T_183300_20250404_Stage2_Actionable","symbol":"183300","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable_or_Yellow_risk","raw_component_scores_after":{"earnings_visibility_score":12,"margin_bridge_score":10,"customer_quality_score":8,"information_confidence_score":10},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["memory_utilization_to_order_revenue_margin_bridge","component_cycle_late_4B_overlay"],"component_delta_explanation":"C10 shadow gate gives credit only when memory recovery maps into equipment/consumables shipment, revenue, margin or utilization conversion; late component-cycle confirmation after fast MFE is capped by local 4B.","MFE_90D_pct":41.48,"MAE_90D_pct":-11.6,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_undercredits_parts_service_utilization_recovery"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C10_shadow","case_id":"C10_FU122_166090_20240516","trigger_id":"T_166090_20240516_Stage4B","symbol":"166090","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"backlog_visibility_score":6,"margin_bridge_score":-6,"execution_risk_score":-12,"valuation_repricing_score":-14},"weighted_score_after":66,"stage_label_after":"Stage4B_watch","changed_components":["memory_utilization_to_order_revenue_margin_bridge","component_cycle_late_4B_overlay"],"component_delta_explanation":"C10 shadow gate gives credit only when memory recovery maps into equipment/consumables shipment, revenue, margin or utilization conversion; late component-cycle confirmation after fast MFE is capped by local 4B.","MFE_90D_pct":29.53,"MAE_90D_pct":-48.22,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_false_positive_if_report_language_upgrades_to_yellow_without_forward_NAND_order_survival"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C10_shadow","case_id":"C10_FU122_074600_20240315","trigger_id":"T_074600_20240315_Stage4B","symbol":"074600","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"earnings_visibility_score":8,"margin_bridge_score":4,"relative_strength_score":8,"valuation_repricing_score":-14,"execution_risk_score":-8},"weighted_score_after":66,"stage_label_after":"Stage2-Actionable+Stage4B_watch","changed_components":["memory_utilization_to_order_revenue_margin_bridge","component_cycle_late_4B_overlay"],"component_delta_explanation":"C10 shadow gate gives credit only when memory recovery maps into equipment/consumables shipment, revenue, margin or utilization conversion; late component-cycle confirmation after fast MFE is capped by local 4B.","MFE_90D_pct":42.36,"MAE_90D_pct":-1.56,"score_return_alignment_label":"counterexample_or_guardrail","current_profile_verdict":"current_profile_4b_too_late_for_components_after_early_MFE"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_to_C10_shadow","case_id":"C10_FU122_064760_20250204","trigger_id":"T_064760_20250204_Stage2_Actionable","symbol":"064760","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable_or_Yellow_risk","raw_component_scores_after":{"earnings_visibility_score":12,"customer_quality_score":10,"margin_bridge_score":10,"valuation_repricing_score":2},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["memory_utilization_to_order_revenue_margin_bridge","component_cycle_late_4B_overlay"],"component_delta_explanation":"C10 shadow gate gives credit only when memory recovery maps into equipment/consumables shipment, revenue, margin or utilization conversion; late component-cycle confirmation after fast MFE is capped by local 4B.","MFE_90D_pct":44.26,"MAE_90D_pct":-2.21,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late_if_it_requires_equipment_PO_and_undercredits_consumable_utilization"}
```

### 9.4 aggregate / shadow / residual rows
```jsonl
{"row_type":"aggregate","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":6,"calibration_usable_trigger_count":6,"representative_trigger_count":6,"positive_case_count":3,"counterexample_count":3,"stage4b_overlay_count":3,"stage4c_case_count":0,"current_profile_error_count":6,"new_independent_ratio":1.0,"hard_duplicate_count":0,"post_commit_static_estimate":"C10 static rows 13 + 6 local representative rows = 19; need_to_30 becomes 11, assuming no batch dedupe collision."}
{"row_type":"shadow_weight_candidate","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","rule_candidate":"C10_MEMORY_RECOVERY_REQUIRES_UTILIZATION_OR_ORDER_TO_REVENUE_MARGIN_BRIDGE_WITH_LATE_COMPONENT_4B_CAP","direction":"increase C10 credit for direct utilization/order/revenue/margin conversion in equipment, parts and consumables; increase local 4B cap for component-cycle confirmation after 20%+ MFE or deep post-peak drawdown; do not add raw memory beta weight","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","round":"R2","loop":122,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["utilization_recovery_undercredited_for_consumables","memory_beta_overcredited_without_forward_order_survival","late_component_cycle_report_needs_local_4B","high_MFE_then_deep_MAE_requires_profit_lock_overlay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 10. Validation Scope

```text
stock_agent_code_accessed = false
stock_agent_code_patched = false
live_candidate_mode = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
stock_web_price_atlas_access_required = true
actual_stock_web_1D_OHLC_used = true
trigger_rows_missing_required_price_fields = 0
trigger_type_must_be_canonical_stage_label = pass
calibration_usable_trigger_count = 6
representative_trigger_count = 6
hard_duplicate_count = 0
```

## 11. Residual Contribution Summary

This loop adds a C10-specific distinction that was not fully isolated by the earlier C10 set: **memory recovery can be confirmed through parts/consumables/utilization routes, but component-cycle confirmation after a sharp run needs a local 4B cap even when the fundamental language is correct.**

The positive controls are Jusung, KoMiCo, and TCK. The counterexample/guardrail rows are KCTech, Hana Materials, and Wonik QnC. The guardrail is not saying the businesses were bad; it says the timing was wrong for fresh Stage3 credit after the first repricing wave.

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during the research session.
Later, in a coding-agent batch session, ingest this MD together with other v12 research files.
Validate filename, metadata round/loop consistency, required MFE/MAE fields, canonical_archetype_id, large_sector_id, and hard duplicate key.
If the trigger rows pass validation, include them as candidate C10 representative rows and evaluate the shadow rule:
C10_MEMORY_RECOVERY_REQUIRES_UTILIZATION_OR_ORDER_TO_REVENUE_MARGIN_BRIDGE_WITH_LATE_COMPONENT_4B_CAP.
Do not change production scoring unless the batch promotion planner accepts the patch across the full v12 corpus.
```

## 13. Next Research State

```text
completed_round = R2
completed_loop = 122
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under_30_representative_rows / C10 rows 13 need_to_30 17 need_to_50 37 before local follow-up; session-local previous C10 loop_121 avoided by new symbol/date/evidence families
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = [
  C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_symbols_only
  C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_followup_new_order_route
  C11_BATTERY_ORDERBOOK_RERATING_followup_margin_FCF_bridge
  C01_ORDER_BACKLOG_MARGIN_BRIDGE_followup_new_symbol_only
  C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_followup_to_50
]
```