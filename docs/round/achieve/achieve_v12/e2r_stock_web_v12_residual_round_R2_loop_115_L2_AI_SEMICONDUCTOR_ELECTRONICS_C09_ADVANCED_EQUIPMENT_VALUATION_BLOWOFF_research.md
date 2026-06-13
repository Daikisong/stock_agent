# E2R Stock-Web V12 Residual Research — R2 loop 115 / L2 / C09

```yaml
research_id: R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS
output_file: e2r_stock_web_v12_residual_round_R2_loop_115_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
completed_round: R2
completed_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows / C09 ledger rows 10 need_to_30 20; session-adjusted prior C09 loop_113 + loop_114 implies 20 -> 25 after this file
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: mixed_C09_advanced_equipment_order_bridge_vs_memory_equipment_boundary_third_pass
loop_objective: coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | holdout_validation
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection / novelty check

V12 selection is coverage-index-first. The No-Repeat ledger places `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` in Priority 0 with 10 rows and 20 rows needed to reach the 30-row minimum stability zone. This file is therefore a C09 third pass, not a round-cycle continuation.

This file deliberately uses a boundary set whose symbols previously fit adjacent memory-equipment narratives but have not been used in the prior C09 loops in this conversation. The contribution is not another generic semiconductor-equipment loop; it tests whether the same semiconductor equipment evidence should be compressed under C09 valuation/optionality blowoff or under C10 memory recovery order-cycle.

Prior C09 loops in this session used: `322310`, `348210`, `240810`, `319660`, `101490`, `036930`, `140860`, `064290`, `036810`, `098460`.

This C09 loop uses only new C09 symbols: `095610`, `089970`, `084370`, `092870`, `033160`.

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No hard duplicate is intentionally reused inside C09. Cross-canonical reuse is explicitly labeled as boundary validation and is not counted as a duplicate C09 case.

```yaml
new_independent_case_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
reused_case_count: 0
minimum_new_independent_case_ratio: 1.00
hard_duplicate_detected: false
cross_canonical_boundary_reuse_declared: true
```

## 2. Research question

C09 is the trapdoor underneath advanced semiconductor equipment stories. A stock can show real process complexity, HBM adjacency, or customer capex momentum and still be a poor Stage3 if the evidence is only product optionality or valuation expansion. But if an advanced-equipment name has a visible named-customer order path and revenue bridge, treating it as mere blowoff makes the profile too late.

This loop asks:

> For equipment names near the C09/C10 boundary, which evidence belongs to a positive order/revenue bridge and which evidence should be capped as advanced-equipment optionality / local 4B?

Proposed split:

```text
C09 positive path = named customer/process demand + order visibility + delivery/revenue-recognition bridge + tolerable MAE
C09 4B/watch path = product launch, HBM adjacency, early capex thesis, or material beta without confirmed tool-stream order conversion
C10 boundary handoff = memory recovery order-cycle evidence can be promoted only after named memory customer capex is tied to the specific tool or consumable stream
```

## 3. Stock-Web OHLC input / price source validation

Price rows are from `Songdaiki/stock-web` tradable symbol-year shards. Entry price is the entry-date close column `c`. MFE/MAE formula follows the stock-web schema:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

| symbol | price_shard_path | profile_path | forward window | corporate action window status |
|---|---|---|---:|---|
| 095610 테스 | `atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv` + `2025.csv` | `atlas/symbol_profiles/095/095610.json` | 180 tradable rows | clean_180D_window_by_tradable_shard_and_share_continuity_proxy |
| 089970 브이엠 | `atlas/ohlcv_tradable_by_symbol_year/089/089970/2025.csv` + `2026.csv` | `atlas/symbol_profiles/089/089970.json` | 180 tradable rows | clean_180D_window_by_tradable_shard_and_share_continuity_proxy |
| 084370 유진테크 | `atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv` + `2025.csv` | `atlas/symbol_profiles/084/084370.json` | 180 tradable rows | clean_180D_window_by_tradable_shard_and_share_continuity_proxy |
| 092870 엑시콘 | `atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv` + `2025.csv` | `atlas/symbol_profiles/092/092870.json` | 180 tradable rows | clean_180D_window_by_tradable_shard_and_share_continuity_proxy |
| 033160 엠케이전자 | `atlas/ohlcv_tradable_by_symbol_year/033/033160/2024.csv` + `2025.csv` | `atlas/symbol_profiles/033/033160.json` | 180 tradable rows | clean_180D_window_by_tradable_shard_and_share_continuity_proxy |

All five rows are calibration-usable: entry row exists, entry_price exists, 30D/90D/180D MFE and MAE are present, and no corporate-action contamination is flagged in the 180D window.

## 4. Canonical archetype compression map

| fine/deep sub-archetype | C09 interpretation | C10 boundary note |
|---|---|---|
| DRAM PECVD order recognition | positive C09 only if order/revenue bridge exists | otherwise C10 memory recovery beta |
| Small-cap etch share-gain unlock | missed positive if capped as valuation blowoff | promote only with named customer capex path |
| Early DRAM capex optionality | local 4B if order timing is not confirmed | not enough for C10 Stage3 |
| Tester product-stream gap under HBM focus | 4B/watch despite MFE | cap until relevant tester stream order appears |
| Packaging material beta | not C09 equipment bottleneck; 4B or Stage2 cap | route outside C10 unless consumable reorder is explicit |

## 5. Case table

| symbol | name | trigger_type | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | role |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 095610 | 테스 | Stage3-Yellow | 2024-11-22 | 14,820 | 20.11 | -11.67 | 65.65 | -11.67 | 100.40 | -11.67 | 2025-08-19 | 29,700 | -6.06 | positive |
| 089970 | 브이엠 | Stage3-Yellow | 2025-03-19 | 10,860 | 18.32 | -13.17 | 25.51 | -13.17 | 190.06 | -13.17 | 2025-12-10 | 31,500 | -7.62 | positive |
| 084370 | 유진테크 | Stage4B | 2024-07-22 | 44,350 | 17.93 | -15.67 | 17.93 | -28.86 | 17.93 | -31.68 | 2024-08-16 | 52,300 | -42.07 | counterexample |
| 092870 | 엑시콘 | Stage4B | 2024-10-25 | 11,450 | 19.13 | -20.09 | 37.64 | -26.55 | 37.64 | -26.55 | 2025-02-14 | 15,760 | -37.88 | counterexample |
| 033160 | 엠케이전자 | Stage4B | 2024-05-03 | 11,670 | 17.65 | -2.23 | 17.65 | -37.87 | 17.65 | -54.24 | 2024-05-24 | 13,730 | -61.11 | counterexample |

## 6. Case notes

### Case 1. 095610 테스 — C09_DRAM_PECVD_ORDER_RECOGNITION_NOT_MERE_MEMORY_BETA

- trigger_date: `2024-11-21`
- entry_date / entry_price: `2024-11-22` / `14,820`
- trigger_type: `Stage3-Yellow`
- role: `positive`
- evidence_url: https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf

DRAM equipment re-recognition, PECVD/order mix, and revenue-recognition bridge from late-2024 semiconductor equipment cycle.

Price path: 30D MFE/MAE `20.11% / -11.67%`, 90D `65.65% / -11.67%`, 180D `100.40% / -11.67%`. Peak inside 180D was `2025-08-19` at `29,700`, followed by drawdown_after_peak `-6.06%`.

Rule interpretation: this is a positive C09 path only because order/customer/process visibility is tied to revenue conversion; it should not be flattened into generic valuation blowoff.

### Case 2. 089970 브이엠 — C09_SMALLCAP_ETCH_ORDER_VISIBILITY_MISSED_STRUCTURAL

- trigger_date: `2025-03-18`
- entry_date / entry_price: `2025-03-19` / `10,860`
- trigger_type: `Stage3-Yellow`
- role: `positive`
- evidence_url: https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf

SK hynix-linked etch investment, share gain, M15X/D1b path and 2025-2026 revenue-cycle visibility; stronger than mere sector beta.

Price path: 30D MFE/MAE `18.32% / -13.17%`, 90D `25.51% / -13.17%`, 180D `190.06% / -13.17%`. Peak inside 180D was `2025-12-10` at `31,500`, followed by drawdown_after_peak `-7.62%`.

Rule interpretation: this is a positive C09 path only because order/customer/process visibility is tied to revenue conversion; it should not be flattened into generic valuation blowoff.

### Case 3. 084370 유진테크 — C09_EARLY_DRAM_CAPEX_OPTIONALITY_HIGH_MAE_CAP

- trigger_date: `2024-07-19`
- entry_date / entry_price: `2024-07-22` / `44,350`
- trigger_type: `Stage4B`
- role: `counterexample`
- evidence_url: https://stock.pstatic.net/stock-research/company/50/20240719_company_347238000.pdf

DRAM capex uplift and process migration thesis came before sufficiently confirmed order/revenue bridge; high-MAE path argues for local 4B cap.

Price path: 30D MFE/MAE `17.93% / -15.67%`, 90D `17.93% / -28.86%`, 180D `17.93% / -31.68%`. Peak inside 180D was `2024-08-16` at `52,300`, followed by drawdown_after_peak `-42.07%`.

Rule interpretation: cap as local Stage4B/watch until named tool-stream order, delivery timing, revenue recognition, and margin bridge are confirmed.

### Case 4. 092870 엑시콘 — C09_TESTER_PRODUCT_MIX_GAP_HBM_FOCUS_LOCAL_4B

- trigger_date: `2024-10-24`
- entry_date / entry_price: `2024-10-25` / `11,450`
- trigger_type: `Stage4B`
- role: `counterexample`
- evidence_url: https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf

HBM focus lowered DRAM burn-in tester investment timing; high MFE existed but MAE and order-mix gap justify 4B/watch rather than clean Stage3.

Price path: 30D MFE/MAE `19.13% / -20.09%`, 90D `37.64% / -26.55%`, 180D `37.64% / -26.55%`. Peak inside 180D was `2025-02-14` at `15,760`, followed by drawdown_after_peak `-37.88%`.

Rule interpretation: cap as local Stage4B/watch until named tool-stream order, delivery timing, revenue recognition, and margin bridge are confirmed.

### Case 5. 033160 엠케이전자 — C09_PACKAGING_MATERIAL_BETA_NOT_ADVANCED_EQUIPMENT_ORDER

- trigger_date: `2024-05-02`
- entry_date / entry_price: `2024-05-03` / `11,670`
- trigger_type: `Stage4B`
- role: `counterexample`
- evidence_url: https://www.sks.co.kr/data1/research/qna_file/20240429163049543_4_ko.pdf

HBM low-temperature solder-ball / packaging-material beta had no clean equipment-order conversion or margin bridge; material/holding overhang dominated path.

Price path: 30D MFE/MAE `17.65% / -2.23%`, 90D `17.65% / -37.87%`, 180D `17.65% / -54.24%`. Peak inside 180D was `2024-05-24` at `13,730`, followed by drawdown_after_peak `-61.11%`.

Rule interpretation: cap as local Stage4B/watch until named tool-stream order, delivery timing, revenue recognition, and margin bridge are confirmed.

## 7. Current calibrated profile stress test

| symbol | current profile likely action | actual path | verdict | correction |
|---|---|---|---|---|
| 095610 테스 | Stage2-Actionable | MFE90 65.65 / MAE90 -11.67; MFE180 100.40 / MAE180 -11.67 | `current_profile_correct_if_C09_allows_order_bridge_positive_path` | allow Stage3-Yellow under C09 order/revenue bridge |
| 089970 브이엠 | Stage2 | MFE90 25.51 / MAE90 -13.17; MFE180 190.06 / MAE180 -13.17 | `current_profile_missed_structural_if_smallcap_equipment_is_overcapped_as_blowoff` | allow Stage3-Yellow under C09 order/revenue bridge |
| 084370 유진테크 | Stage3-Yellow | MFE90 17.93 / MAE90 -28.86; MFE180 17.93 / MAE180 -31.68 | `current_profile_false_positive_if_early_capex_thesis_gets_Stage3_weight` | route to Stage4B/watch or Stage2 cap under C09 optionality guard |
| 092870 엑시콘 | Stage2-Actionable | MFE90 37.64 / MAE90 -26.55; MFE180 37.64 / MAE180 -26.55 | `current_profile_false_positive_without_tool_stream_mix_gate` | route to Stage4B/watch or Stage2 cap under C09 optionality guard |
| 033160 엠케이전자 | Stage2-Actionable | MFE90 17.65 / MAE90 -37.87; MFE180 17.65 / MAE180 -54.24 | `current_profile_false_positive_if_material_beta_is_mapped_to_advanced_equipment_bottleneck` | route to Stage4B/watch or Stage2 cap under C09 optionality guard |

Stress-test answer: the global `price_only_blowoff_blocks_positive_stage` and `full_4b_requires_non_price_evidence` axes remain valid. The residual C09 issue is more granular: some advanced-equipment positives are being over-capped because they look like valuation blowoff, while early capex or product optionality still receives too much Stage2/Yellow credit if the exact tool-stream order bridge is absent.

## 8. 4B local vs full-window timing audit

| symbol | local/full-window observation | timing verdict |
|---|---|---|
| 095610 | peak `2025-08-19` at `29,700`, drawdown_after_peak `-6.06%` | not local 4B at entry; monitor only after peak if price outruns revision |
| 089970 | peak `2025-12-10` at `31,500`, drawdown_after_peak `-7.62%` | not local 4B at entry; monitor only after peak if price outruns revision |
| 084370 | peak `2024-08-16` at `52,300`, drawdown_after_peak `-42.07%` | local 4B/watch required at entry or immediately after fast MFE because full-window MAE validates risk |
| 092870 | peak `2025-02-14` at `15,760`, drawdown_after_peak `-37.88%` | local 4B/watch required at entry or immediately after fast MFE because full-window MAE validates risk |
| 033160 | peak `2024-05-24` at `13,730`, drawdown_after_peak `-61.11%` | local 4B/watch required at entry or immediately after fast MFE because full-window MAE validates risk |

## 9. 4C protection audit

No row is routed to hard Stage4C. The failure mode is not thesis death; it is over-crediting optional equipment narratives before the named order/revenue bridge is firm. All protection is therefore Stage2 cap or local Stage4B/watch.

```yaml
hard_4C_case_count: 0
4B_case_count: 3
4C_thesis_break_timing_test: not_primary_loop_objective
```

## 10. Before / after backtest comparison

| profile_id | hypothesis | selected cases | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_proxy | current calibrated profile without C09/C10 boundary split | 5 | 32.88 | -23.62 | 72.74 | -27.46 | 3/5 | 1 | mixed: too permissive for optionality, too strict for bridge-backed small-cap equipment |
| P1_C09_boundary_shadow | promote only signed/order/revenue bridge; cap optionality/material beta | 2 promoted | 45.58 | -12.42 | 145.23 | -12.42 | 0/2 | 0 | best precision for clean positives |
| P2_4B_counterexample_guard | block/cap high-MAE optionality rows | 3 blocked/watch | 24.41 | -31.09 | 24.41 | -37.49 | 0/3 promoted | 0 | protects three high-MAE rows |

## 11. Score-return alignment matrix

| symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 095610 | 74 | Stage2-Actionable | 82 | Stage3-Yellow | 65.65 | -11.67 | score_return_aligned_positive_after_boundary_gate |
| 089970 | 69 | Stage2 | 83 | Stage3-Yellow | 25.51 | -13.17 | score_return_aligned_positive_after_boundary_gate |
| 084370 | 76 | Stage3-Yellow | 59 | Stage4B | 17.93 | -28.86 | score_return_misaligned_before_gate_but_aligned_after_4B_cap |
| 092870 | 72 | Stage2-Actionable | 58 | Stage4B | 37.64 | -26.55 | score_return_misaligned_before_gate_but_aligned_after_4B_cap |
| 033160 | 70 | Stage2-Actionable | 55 | Stage4B | 17.65 | -37.87 | score_return_misaligned_before_gate_but_aligned_after_4B_cap |

## 12. Machine-readable rows

```jsonl
{"row_type":"trigger","research_id":"R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS","selected_round":"R2","selected_loop":115,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"095610","company_name":"테스","fine_archetype_id":"C09_DRAM_PECVD_ORDER_RECOGNITION_NOT_MERE_MEMORY_BETA","case_role":"positive","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-21","entry_date":"2024-11-22","entry_price":14820.0,"MFE_30D_pct":20.11,"MAE_30D_pct":-11.67,"MFE_90D_pct":65.65,"MAE_90D_pct":-11.67,"MFE_180D_pct":100.4,"MAE_180D_pct":-11.67,"peak_date":"2025-08-19","peak_price":29700.0,"drawdown_after_peak_pct":-6.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"calibration_usable":true,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","source_proxy_only":false,"evidence_url_pending":false,"evidence_url":"https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf","current_profile_error":"current_profile_correct_if_C09_allows_order_bridge_positive_path","raw_component_score_breakdown":{"eps_fcf_explosion":72,"earnings_visibility":76,"bottleneck_pricing":64,"market_mispricing":58,"valuation_rerating":55,"capital_allocation":42,"information_confidence":73},"score_before":74,"score_after":82,"stage_before":"Stage2-Actionable","stage_after":"Stage3-Yellow"}
{"row_type":"trigger","research_id":"R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS","selected_round":"R2","selected_loop":115,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"089970","company_name":"브이엠","fine_archetype_id":"C09_SMALLCAP_ETCH_ORDER_VISIBILITY_MISSED_STRUCTURAL","case_role":"positive","trigger_type":"Stage3-Yellow","trigger_date":"2025-03-18","entry_date":"2025-03-19","entry_price":10860.0,"MFE_30D_pct":18.32,"MAE_30D_pct":-13.17,"MFE_90D_pct":25.51,"MAE_90D_pct":-13.17,"MFE_180D_pct":190.06,"MAE_180D_pct":-13.17,"peak_date":"2025-12-10","peak_price":31500.0,"drawdown_after_peak_pct":-7.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"calibration_usable":true,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","source_proxy_only":false,"evidence_url_pending":false,"evidence_url":"https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf","current_profile_error":"current_profile_missed_structural_if_smallcap_equipment_is_overcapped_as_blowoff","raw_component_score_breakdown":{"eps_fcf_explosion":69,"earnings_visibility":77,"bottleneck_pricing":67,"market_mispricing":62,"valuation_rerating":60,"capital_allocation":40,"information_confidence":76},"score_before":69,"score_after":83,"stage_before":"Stage2","stage_after":"Stage3-Yellow"}
{"row_type":"trigger","research_id":"R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS","selected_round":"R2","selected_loop":115,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"084370","company_name":"유진테크","fine_archetype_id":"C09_EARLY_DRAM_CAPEX_OPTIONALITY_HIGH_MAE_CAP","case_role":"counterexample","trigger_type":"Stage4B","trigger_date":"2024-07-19","entry_date":"2024-07-22","entry_price":44350.0,"MFE_30D_pct":17.93,"MAE_30D_pct":-15.67,"MFE_90D_pct":17.93,"MAE_90D_pct":-28.86,"MFE_180D_pct":17.93,"MAE_180D_pct":-31.68,"peak_date":"2024-08-16","peak_price":52300.0,"drawdown_after_peak_pct":-42.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"calibration_usable":true,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","source_proxy_only":false,"evidence_url_pending":false,"evidence_url":"https://stock.pstatic.net/stock-research/company/50/20240719_company_347238000.pdf","current_profile_error":"current_profile_false_positive_if_early_capex_thesis_gets_Stage3_weight","raw_component_score_breakdown":{"eps_fcf_explosion":50,"earnings_visibility":52,"bottleneck_pricing":61,"market_mispricing":47,"valuation_rerating":45,"capital_allocation":33,"information_confidence":57},"score_before":76,"score_after":59,"stage_before":"Stage3-Yellow","stage_after":"Stage4B"}
{"row_type":"trigger","research_id":"R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS","selected_round":"R2","selected_loop":115,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"092870","company_name":"엑시콘","fine_archetype_id":"C09_TESTER_PRODUCT_MIX_GAP_HBM_FOCUS_LOCAL_4B","case_role":"counterexample","trigger_type":"Stage4B","trigger_date":"2024-10-24","entry_date":"2024-10-25","entry_price":11450.0,"MFE_30D_pct":19.13,"MAE_30D_pct":-20.09,"MFE_90D_pct":37.64,"MAE_90D_pct":-26.55,"MFE_180D_pct":37.64,"MAE_180D_pct":-26.55,"peak_date":"2025-02-14","peak_price":15760.0,"drawdown_after_peak_pct":-37.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"calibration_usable":true,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","source_proxy_only":false,"evidence_url_pending":false,"evidence_url":"https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf","current_profile_error":"current_profile_false_positive_without_tool_stream_mix_gate","raw_component_score_breakdown":{"eps_fcf_explosion":46,"earnings_visibility":48,"bottleneck_pricing":66,"market_mispricing":49,"valuation_rerating":44,"capital_allocation":30,"information_confidence":59},"score_before":72,"score_after":58,"stage_before":"Stage2-Actionable","stage_after":"Stage4B"}
{"row_type":"trigger","research_id":"R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS","selected_round":"R2","selected_loop":115,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"033160","company_name":"엠케이전자","fine_archetype_id":"C09_PACKAGING_MATERIAL_BETA_NOT_ADVANCED_EQUIPMENT_ORDER","case_role":"counterexample","trigger_type":"Stage4B","trigger_date":"2024-05-02","entry_date":"2024-05-03","entry_price":11670.0,"MFE_30D_pct":17.65,"MAE_30D_pct":-2.23,"MFE_90D_pct":17.65,"MAE_90D_pct":-37.87,"MFE_180D_pct":17.65,"MAE_180D_pct":-54.24,"peak_date":"2024-05-24","peak_price":13730.0,"drawdown_after_peak_pct":-61.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"calibration_usable":true,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","source_proxy_only":false,"evidence_url_pending":false,"evidence_url":"https://www.sks.co.kr/data1/research/qna_file/20240429163049543_4_ko.pdf","current_profile_error":"current_profile_false_positive_if_material_beta_is_mapped_to_advanced_equipment_bottleneck","raw_component_score_breakdown":{"eps_fcf_explosion":42,"earnings_visibility":43,"bottleneck_pricing":50,"market_mispricing":38,"valuation_rerating":39,"capital_allocation":30,"information_confidence":52},"score_before":70,"score_after":55,"stage_before":"Stage2-Actionable","stage_after":"Stage4B"}
{"row_type":"aggregate","research_id":"R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS","selected_round":"R2","selected_loop":115,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","usable_trigger_count":5,"positive_case_count":2,"counterexample_count":3,"local_4B_watch_count":3,"hard_4C_count":0,"mean_MFE_90D_pct":32.88,"mean_MAE_90D_pct":-23.62,"mean_MFE_180D_pct":72.74,"mean_MAE_180D_pct":-27.46,"median_MFE_180D_pct":37.64,"median_MAE_180D_pct":-26.55,"current_profile_error_count":4,"rule_candidate":"C09_C10_BOUNDARY_ORDER_REVENUE_BRIDGE_OR_OPTIONALITY_4B_CAP"}
{"row_type":"shadow_weight_candidate","research_id":"R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","rule_candidate":"C09_C10_BOUNDARY_ORDER_REVENUE_BRIDGE_OR_OPTIONALITY_4B_CAP","direction":"increase earnings_visibility/information_confidence when signed order or revenue recognition exists; reduce bottleneck/valuation credit for product optionality, early capex thesis, or material beta without tool-stream order conversion","suggested_delta_not_applied":{"earnings_visibility":2.0,"information_confidence":1.5,"bottleneck_pricing":-1.0,"valuation_rerating":-1.5},"production_scoring_patch_applied":false,"handoff_prompt_executed_now":false}
{"row_type":"residual_contribution","research_id":"R2_L115_L2_C09_ADV_EQUIPMENT_VALUATION_BLOWOFF_C10_BOUNDARY_THIRD_PASS","contribution_label":"canonical_archetype_boundary_rule_candidate","new_axis_proposed":["C09_C10_BOUNDARY_ORDER_REVENUE_BRIDGE_OR_OPTIONALITY_4B_CAP","C09_PRODUCT_OR_EARLY_CAPEX_OPTIONALITY_LOCAL_4B","C09_MATERIAL_BETA_DECONTAMINATION_GATE"],"existing_axis_strengthened":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","stage2_required_bridge"],"existing_axis_weakened":[],"next_recommended_archetypes":["C06_HBM_MEMORY_CUSTOMER_CAPACITY","C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","C11_BATTERY_ORDERBOOK_RERATING","C01_ORDER_BACKLOG_MARGIN_BRIDGE"]}
```

## 13. Source register

```yaml
main_execution_prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
stock_web_manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
stock_web_schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
profiles:
  095610: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/095/095610.json
  089970: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/089/089970.json
  084370: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/084/084370.json
  092870: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/092/092870.json
  033160: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/033/033160.json
evidence_sources:
  095610: https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf
  089970: https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf
  084370: https://stock.pstatic.net/stock-research/company/50/20240719_company_347238000.pdf
  092870: https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf
  033160: https://www.sks.co.kr/data1/research/qna_file/20240429163049543_4_ko.pdf
```

## 14. Sector-specific rule candidate

`L2_C09_ADVANCED_EQUIPMENT_ORDER_BRIDGE_VS_OPTIONALITY_BLOWOFF_SPLIT`

In L2 semiconductor equipment, C09 should not simply punish every advanced-equipment stock as valuation blowoff. The sector rule should distinguish two pathways:

1. **Order/revenue bridge pathway**: named customer or process-node demand, visible order or delivery timing, and credible revenue/margin conversion. This can become Stage3-Yellow when MAE is tolerable.
2. **Optionality / blowoff pathway**: product launch, early capex thesis, HBM adjacency, or material beta without named tool-stream order conversion. This should remain Stage2 cap or local Stage4B/watch.

## 15. Canonical-archetype rule candidate

`C09_C10_BOUNDARY_ORDER_REVENUE_BRIDGE_OR_OPTIONALITY_4B_CAP`

C09 should be used as the boundary guard for advanced-equipment valuation risk. If evidence is only memory beta, transfer-test it against C10. If evidence has a named process/customer order bridge, allow C09 positive Stage3-Yellow. If evidence lacks the exact tool-stream order/revenue bridge, cap to Stage2 or local Stage4B even if the stock shows short-window MFE.

## 16. Residual contribution summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_count: 3
4B_case_count: 3
4C_case_count: 0
current_profile_error_count: 4
loop_contribution_label: canonical_archetype_boundary_rule_candidate
new_axis_proposed:
  - C09_C10_BOUNDARY_ORDER_REVENUE_BRIDGE_OR_OPTIONALITY_4B_CAP
  - C09_PRODUCT_OR_EARLY_CAPEX_OPTIONALITY_LOCAL_4B
  - C09_MATERIAL_BETA_DECONTAMINATION_GATE
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
  - stage2_required_bridge
existing_axis_weakened: []
do_not_propose_new_weight_delta: false
```

## 17. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent. Do not treat this handoff as executed during the research session. In the next coding session only, ingest this MD together with other V12 result files under docs/round. Validate all trigger rows against the V12 parser schema. If accepted, add C09-scoped shadow rule evidence for C09_C10_BOUNDARY_ORDER_REVENUE_BRIDGE_OR_OPTIONALITY_4B_CAP. Do not change production scoring directly from one file. Aggregate with accepted C09/C10 boundary rows, update rejected ledger if any row fails MFE/MAE/corporate-action validation, and only then consider a small scoped archetype weight adjustment candidate. Preserve e2r_2_2 rollback path.
```

## 18. Next research state

```text
completed_round = R2
completed_loop = 115
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C09 rows 10 / need_to_30 20; session-adjusted C09 20 -> 25 after this file
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C11_BATTERY_ORDERBOOK_RERATING | C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 19. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
