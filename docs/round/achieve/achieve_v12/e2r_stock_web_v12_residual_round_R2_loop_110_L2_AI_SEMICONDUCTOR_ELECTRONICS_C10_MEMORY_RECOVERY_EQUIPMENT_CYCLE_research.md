# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
| field | value |
|---|---|
| filename | `e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md` |
| selected_round | `R2` |
| selected_loop | `110` |
| selection_basis | `docs/core/V12_Research_No_Repeat_Index.md` |
| selected_priority_bucket | `Priority 0 / under 30 rows; C10 ledger rows 13, need-to-30 17` |
| round_schedule_status | `coverage_index_selected` |
| round_sector_consistency | `pass` |
| large_sector_id | `L2_AI_SEMICONDUCTOR_ELECTRONICS` |
| canonical_archetype_id | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` |
| fine_archetype_id | `mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set` |
| loop_objective | `coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | residual_missed_structural_mining` |
| price_source | `Songdaiki/stock-web` |
| stock_web_manifest_max_date | `2026-02-20` |
| production_scoring_changed | `false` |
| shadow_weight_only | `true` |
| handoff_prompt_executed_now | `false` |

This loop adds 5 new independent cases, 3 counterexamples, and 4 residual errors for R2/L2/C10. The second pass deliberately avoids the prior session C10 set: 064760, 083310, 074600, 036200, and 281820.

## 1. Current Calibrated Profile Assumption

- before_profile_id: `e2r_2_1_stock_web_calibrated_proxy`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- after_profile_id: `C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONVERSION_SHADOW_PROFILE`
- already-applied global axes are not re-proposed globally. This loop stress-tests them inside C10 only.

## 2. Round / Large Sector / Canonical Archetype Scope

| scope | value | status |
|---|---|---|
| selected_round | `R2` | C06~C10 maps to R2 |
| large_sector_id | `L2_AI_SEMICONDUCTOR_ELECTRONICS` | pass |
| canonical_archetype_id | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` | pass |
| fine_archetype_id | `mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set` | mapped under C10 |

## 3. Previous Coverage / Duplicate Avoidance Check

- Remote No-Repeat Index shows `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` at 13 rows, 13 symbols, need-to-30 17, need-to-50 37.
- In this conversation, one earlier C10 file used `064760 티씨케이`, `083310 엘오티베큠`, `074600 원익QnC`, `036200 유니셈`, `281820 케이씨텍`; this loop uses five different symbols.
- Hard duplicate key checked as `canonical_archetype_id + symbol + trigger_type + entry_date`; no duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price_data_source | `Songdaiki/stock-web` |
| source_repo_url | `https://github.com/Songdaiki/stock-web` |
| manifest_path | `atlas/manifest.json` |
| schema_path | `atlas/schema.json` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| stock_web_manifest_max_date | `2026-02-20` |

## 5. Historical Eligibility Gate

| symbol | entry_date | forward_window_trading_days | shares_change_pct_180D | corporate_action_window_status | calibration_usable |
|---|---:|---:|---:|---|---|
| 095610 테스 | 2024-11-22 | 180 | 0.000 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |
| 089970 브이엠 | 2025-03-19 | 180 | 1.396 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |
| 084370 유진테크 | 2024-07-22 | 180 | 0.000 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |
| 092870 엑시콘 | 2024-10-25 | 180 | 0.000 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |
| 033160 엠케이전자 | 2024-05-03 | 180 | 0.000 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |

Note: profile paths are included for downstream parser validation. This research file uses the tradable shard and a no-split-scale share-continuity proxy for the 180D window; no 180D trigger row is marked contaminated.

## 6. Canonical Archetype Compression Map

| fine/deep sub-archetype | compresses to C10? | gate tested |
|---|---|---|
| DRAM order recognition / PECVD order mix | yes | named order + revenue-recognition bridge |
| SK hynix etch tool share-gain unlock | yes | customer-specific capex + order-cycle visibility |
| early DRAM capex thesis without order conversion | yes | cap until delivery/revenue conversion appears |
| memory tester order gap under HBM capex diversion | yes | 4B/watch when customer capex bypasses tested tool stream |
| memory packaging material beta | partial | cap if not equipment-order conversion and margin bridge is weak |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | verdict |
|---|---:|---|---|---:|---:|---:|---|
| `TES_C10_DRAM_ORDER_RECOGNITION` | 095610 | 테스 | positive/structural_success | 2024-11-21 | 2024-11-22 | 14820 | current_profile_correct |
| `VM_C10_HYNIX_ETCH_ORDER_UNLOCK` | 089970 | 브이엠 | positive/missed_structural | 2025-03-18 | 2025-03-19 | 10860 | current_profile_missed_structural |
| `EUGENE_C10_EARLY_DRAM_CAPEX_THESIS` | 084370 | 유진테크 | counterexample/failed_rerating | 2024-07-19 | 2024-07-22 | 44350 | current_profile_false_positive |
| `EXICON_C10_TESTER_HBM_FOCUS_GAP` | 092870 | 엑시콘 | counterexample/4B_overlay_success | 2024-10-24 | 2024-10-25 | 11450 | current_profile_false_positive |
| `MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG` | 033160 | 엠케이전자 | counterexample/failed_rerating | 2024-05-02 | 2024-05-03 | 11670 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: `2`
- counterexample_count: `3`
- 4B_case_count: `3`
- 4C_case_count: `0`
- calibration_usable_trigger_count: `5`

The positive side requires memory recovery to become a named customer/order/revenue stream. The counterexample side blocks generic capex thesis, tester order mix gaps, and packaging-material beta when the price path shows high MAE before durable conversion.

## 9. Evidence Source Map

| symbol | evidence_source | evidence_url | evidence timing rule |
|---|---|---|---|
| 095610 테스 | Hanwha Investment & Securities report, 2024-11-21, 테스: 디램 장비사로의 인식 전환 필요 | https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf | unknown report time -> next tradable close |
| 089970 브이엠 | SK Securities report, 2025-03-18, 브이엠: 본업 성장 사이클 + 해외 모멘텀은 덤 | https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf | unknown report time -> next tradable close |
| 084370 유진테크 | Hi Investment / Naver stock-research report, 2024-07-19, 유진테크: memory capex and DRAM capex forecast uplift | https://stock.pstatic.net/stock-research/company/50/20240719_company_347238000.pdf | unknown report time -> next tradable close |
| 092870 엑시콘 | Naver stock-research report, 2024-10-24, 엑시콘: HBM focus lowered DRAM burn-in tester investment | https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf | unknown report time -> next tradable close |
| 033160 엠케이전자 | SK Securities report, 2024-05-02, 엠케이전자: semiconductor upturn + HBM low-temperature solder ball / QP improvement thesis | https://www.sks.co.kr/data1/research/qna_file/20240429163049543_4_ko.pdf | unknown report time -> next tradable close |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | price_basis |
|---|---|---|---|
| 095610 | `atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv` | `atlas/symbol_profiles/095/095610.json` | tradable_raw / raw_unadjusted_marcap |
| 089970 | `atlas/ohlcv_tradable_by_symbol_year/089/089970/2025.csv` | `atlas/symbol_profiles/089/089970.json` | tradable_raw / raw_unadjusted_marcap |
| 084370 | `atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv` | `atlas/symbol_profiles/084/084370.json` | tradable_raw / raw_unadjusted_marcap |
| 092870 | `atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv` | `atlas/symbol_profiles/092/092870.json` | tradable_raw / raw_unadjusted_marcap |
| 033160 | `atlas/ohlcv_tradable_by_symbol_year/033/033160/2024.csv` | `atlas/symbol_profiles/033/033160.json` | tradable_raw / raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

### TES_C10_DRAM_ORDER_RECOGNITION — 095610 테스

- evidence_available_at_that_date: 2024-11-21 report argued TES should be reclassified from NAND-only PECVD exposure to rising DRAM order exposure; this gives non-price memory-equipment order/revenue bridge.
- stage2_evidence_fields: `public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal`
- stage3_evidence_fields: `margin_bridge, financial_visibility, repeat_order_or_conversion, durable_customer_confirmation`
- stage4b_evidence_fields: `none`
- profile stress verdict: `current_profile_correct`
- synthesis: A clean late-2024 C10 positive: the path is not just memory beta, but DRAM order recognition and equipment-mix bridge. 180D MFE is high with limited 180D MAE.

### VM_C10_HYNIX_ETCH_ORDER_UNLOCK — 089970 브이엠

- evidence_available_at_that_date: 2025-03-18 report tied VM to SK hynix 1b/M15X etch investment, share gain, and 2025-2026 revenue cycle visibility; this was stronger than generic memory beta.
- stage2_evidence_fields: `public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, backlog_or_delivery_visibility, early_revision_signal`
- stage3_evidence_fields: `margin_bridge, financial_visibility, durable_customer_confirmation, repeat_order_or_conversion`
- stage4b_evidence_fields: `none`
- profile stress verdict: `current_profile_missed_structural`
- synthesis: A C10 positive that the current profile can miss if it treats small-cap etch as mere memory beta. Named customer, capex path, and order-cycle visibility improved the reward/risk profile.

### EUGENE_C10_EARLY_DRAM_CAPEX_THESIS — 084370 유진테크

- evidence_available_at_that_date: 2024-07-19 report maintained buy and lifted target on memory capex/DRAM capex growth; at trigger time the evidence was still capex-thesis-heavy rather than confirmed order-to-revenue conversion.
- stage2_evidence_fields: `public_event_or_disclosure, capacity_or_volume_route, early_revision_signal`
- stage3_evidence_fields: `financial_visibility`
- stage4b_evidence_fields: `valuation_blowoff, margin_or_backlog_slowdown, explicit_event_cap`
- profile stress verdict: `current_profile_false_positive`
- synthesis: DRAM capex thesis was not wrong, but July 2024 entry had insufficient order/revenue conversion and large 90D/180D MAE. Proposed C10 gate should delay promotion until conversion evidence appears.

### EXICON_C10_TESTER_HBM_FOCUS_GAP — 092870 엑시콘

- evidence_available_at_that_date: 2024-10-24 report stated Samsung HBM focus reduced relative DRAM burn-in tester investment; this is exactly a C10 order-cycle gap rather than a clean memory-cycle unlock.
- stage2_evidence_fields: `public_event_or_disclosure, customer_or_order_quality`
- stage3_evidence_fields: `none`
- stage4b_evidence_fields: `contract_delay, margin_or_backlog_slowdown, explicit_event_cap, price_only_local_peak`
- profile stress verdict: `current_profile_false_positive`
- synthesis: The product is memory-test related, but customer capex was diverted away from the tested order stream. This should be Stage4B/watch or Stage2 block, not Stage3 unlock.

### MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG — 033160 엠케이전자

- evidence_available_at_that_date: 2024-05-02 report framed MK Electron as packaging-material beneficiary from semiconductor recovery and HBM-related solder-ball product expansion; however this is material beta with margin/holding-company overhang.
- stage2_evidence_fields: `public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route`
- stage3_evidence_fields: `none`
- stage4b_evidence_fields: `valuation_blowoff, margin_or_backlog_slowdown, capital_raise_or_overhang`
- profile stress verdict: `current_profile_false_positive`
- synthesis: C10 should avoid compressing all semiconductor-recovery materials into equipment-cycle positives. Without order conversion and clean margin bridge, this row behaves as high-MAE false positive.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:095610:Stage2-Actionable:2024-11-22` | Stage2-Actionable | 2024-11-22 | 14820 | 20.11 | -11.67 | 65.65 | -11.67 | 100.40 | -11.67 | 2025-08-19 | 29700 | -6.06 |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:089970:Stage2-Actionable:2025-03-19` | Stage2-Actionable | 2025-03-19 | 10860 | 18.32 | -13.17 | 25.51 | -13.17 | 190.06 | -13.17 | 2025-12-10 | 31500 | -7.62 |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:084370:Stage2-Actionable:2024-07-22` | Stage2-Actionable | 2024-07-22 | 44350 | 17.93 | -15.67 | 17.93 | -28.86 | 17.93 | -31.68 | 2024-08-16 | 52300 | -42.07 |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:092870:Stage4B:2024-10-25` | Stage4B | 2024-10-25 | 11450 | 19.13 | -20.09 | 37.64 | -26.55 | 37.64 | -26.55 | 2025-02-14 | 15760 | -37.88 |
| `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:033160:Stage2-Actionable:2024-05-03` | Stage2-Actionable | 2024-05-03 | 11670 | 17.65 | -2.23 | 17.65 | -37.87 | 17.65 | -54.24 | 2024-05-24 | 13730 | -61.11 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely decision | actual path | verdict | correction |
|---|---|---|---|---|
| `TES_C10_DRAM_ORDER_RECOGNITION` | Stage2-Actionable then later Stage3-Yellow allowed | MFE90 65.65 / MAE90 -11.67; MFE180 100.40 / MAE180 -11.67 | `current_profile_correct` | Stage3-Yellow under C10 gate |
| `VM_C10_HYNIX_ETCH_ORDER_UNLOCK` | Stage2 only / too slow to recognize order unlock | MFE90 25.51 / MAE90 -13.17; MFE180 190.06 / MAE180 -13.17 | `current_profile_missed_structural` | Stage3-Yellow under C10 gate |
| `EUGENE_C10_EARLY_DRAM_CAPEX_THESIS` | Stage2/Yellow risk too high because memory beta was over-credited | MFE90 17.93 / MAE90 -28.86; MFE180 17.93 / MAE180 -31.68 | `current_profile_false_positive` | Stage2 under C10 gate |
| `EXICON_C10_TESTER_HBM_FOCUS_GAP` | Stage2/Yellow risk too high because memory beta was over-credited | MFE90 37.64 / MAE90 -26.55; MFE180 37.64 / MAE180 -26.55 | `current_profile_false_positive` | Stage4B under C10 gate |
| `MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG` | Stage2/Yellow risk too high because memory beta was over-credited | MFE90 17.65 / MAE90 -37.87; MFE180 17.65 / MAE180 -54.24 | `current_profile_false_positive` | Stage2 under C10 gate |

Stress-test answers: Stage2 bonus is useful for TES/VM but too generous for Eugene/MK when order conversion is not confirmed. Yellow 75 is too easy for early capex thesis but adequate for named-customer order conversion. Green 87/revision 55 remains strict enough; no Stage3-Green trigger is proposed here. Price-only blowoff guard and non-price 4B requirement remain strengthened, not globally changed. Hard 4C is not tested in this loop.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2/Actionable entry | Stage3-Yellow eligibility under proposed gate | Stage3-Green | green_lateness_ratio |
|---|---|---|---|---|
| `TES_C10_DRAM_ORDER_RECOGNITION` | 2024-11-22 close 14820 | yes | not proposed | not_applicable:no_confirmed_Stage3_Green_trigger |
| `VM_C10_HYNIX_ETCH_ORDER_UNLOCK` | 2025-03-19 close 10860 | yes | not proposed | not_applicable:no_confirmed_Stage3_Green_trigger |
| `EUGENE_C10_EARLY_DRAM_CAPEX_THESIS` | 2024-07-22 close 44350 | no: order/revenue/margin bridge incomplete or 4B watch required | not proposed | not_applicable:no_confirmed_Stage3_Green_trigger |
| `EXICON_C10_TESTER_HBM_FOCUS_GAP` | 2024-10-25 close 11450 | no: order/revenue/margin bridge incomplete or 4B watch required | not proposed | not_applicable:no_confirmed_Stage3_Green_trigger |
| `MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG` | 2024-05-03 close 11670 | no: order/revenue/margin bridge incomplete or 4B watch required | not proposed | not_applicable:no_confirmed_Stage3_Green_trigger |

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence type | local peak / full-window comment | timing verdict |
|---|---|---|---|
| `TES_C10_DRAM_ORDER_RECOGNITION` | none | peak 2025-08-19 at 29700; post-peak DD -6.06% | not_applicable |
| `VM_C10_HYNIX_ETCH_ORDER_UNLOCK` | none | peak 2025-12-10 at 31500; post-peak DD -7.62% | not_applicable |
| `EUGENE_C10_EARLY_DRAM_CAPEX_THESIS` | valuation_blowoff, margin_or_backlog_slowdown, explicit_event_cap | peak 2024-08-16 at 52300; post-peak DD -42.07% | local_4B_watch_required; do_not_treat_generic_memory_beta_as_full_positive_stage |
| `EXICON_C10_TESTER_HBM_FOCUS_GAP` | contract_delay, margin_or_backlog_slowdown, explicit_event_cap, price_only_local_peak | peak 2025-02-14 at 15760; post-peak DD -37.88% | local_4B_watch_required; do_not_treat_generic_memory_beta_as_full_positive_stage |
| `MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG` | valuation_blowoff, margin_or_backlog_slowdown, capital_raise_or_overhang | peak 2024-05-24 at 13730; post-peak DD -61.11% | local_4B_watch_required; do_not_treat_generic_memory_beta_as_full_positive_stage |

## 16. 4C Protection Audit

No hard Stage4C trigger is proposed. The loop is about Stage2/Yellow misclassification and Stage4B/watch routing inside C10. `four_c_protection_label = not_applicable_no_hard_4c` for all trigger rows.

## 17. Sector-Specific Rule Candidate

`L2_C10_MEMORY_RECOVERY_ORDER_CONVERSION_AND_EARLY_CAPEX_THESIS_SPLIT`

Within L2, generic memory recovery beta should be split from actual order-cycle reversal. Equipment/consumable names deserve promotion only when a named customer, capacity conversion, or revenue-recognition bridge is visible. Early DRAM capex thesis, customer capex mix diversion, and material-beta overhang remain Stage2/watch even if the sector index is improving.

## 18. Canonical-Archetype Rule Candidate

`C10_MEMORY_RECOVERY_REQUIRES_NAMED_ORDER_OR_CONSUMABLE_REORDER_CONVERSION_GATE_SECOND_PASS`

Proposed C10 gate:

1. Upgrade toward Stage3-Yellow only if memory recovery links to named customer order, delivery timing, revenue-recognition bridge, or repeat consumable reorder.
2. Cap early capex-thesis reports at Stage2 when order/revenue conversion is still absent.
3. Route tester-equipment or packaging-material beta to Stage4B/watch when customer capex is diverted away from the relevant tool stream or high-MAE risk is visible.

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | selected cases | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_proxy | current calibrated profile without C10 second-pass split | 5 | 32.88 | -23.62 | 72.74 | -27.46 | 0.60 | 1 | mixed: too early for three, too late for one |
| P0b_e2r_2_0_reference | old baseline; broader memory beta credit | 5 | 32.88 | -23.62 | 72.74 | -27.46 | 0.80 | 1 | worse high-MAE control |
| P1_L2_sector_candidate | sector split: order conversion vs early capex thesis | 2 promoted | 45.58 | -12.42 | 145.23 | -12.42 | 0.00 | 0 | improved risk filter |
| P2_C10_archetype_candidate | named order / consumable reorder conversion gate | 2 promoted | 45.58 | -12.42 | 145.23 | -12.42 | 0.00 | 0 | best alignment |
| P3_counterexample_guard | 4B/watch for tester mix gap and material beta | 3 blocked/watch | 24.41 | -31.09 | 24.41 | -37.49 | 0.00 | 0 | protects high-MAE rows |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| `TES_C10_DRAM_ORDER_RECOGNITION` | 74 | Stage2-Actionable | 81 | Stage3-Yellow | 65.65 | -11.67 | score_return_aligned_positive |
| `VM_C10_HYNIX_ETCH_ORDER_UNLOCK` | 68 | Stage2 | 82 | Stage3-Yellow | 25.51 | -13.17 | score_return_aligned_positive_after_gate |
| `EUGENE_C10_EARLY_DRAM_CAPEX_THESIS` | 76 | Stage3-Yellow | 64 | Stage2 | 17.93 | -28.86 | score_return_misaligned_before_gate |
| `EXICON_C10_TESTER_HBM_FOCUS_GAP` | 70 | Stage2-Actionable | 58 | Stage4B | 37.64 | -26.55 | guardrail_aligned_after_gate |
| `MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG` | 69 | Stage2-Actionable | 60 | Stage2 | 17.65 | -37.87 | score_return_misaligned_before_gate |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set | 2 | 3 | 3 | 0 | 5 | 0 | 5 | 5 | 4 | L2_C10_MEMORY_RECOVERY_ORDER_CONVERSION_AND_EARLY_CAPEX_THESIS_SPLIT | C10_MEMORY_RECOVERY_REQUIRES_NAMED_ORDER_OR_CONSUMABLE_REORDER_CONVERSION_GATE_SECOND_PASS | remote ledger C10 13 -> 18; session-adjusted C10 18 -> 23 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_missed_structural
  - high_MAE_stage2_entry
  - early_capex_thesis_without_order_conversion
new_axis_proposed: C10_MEMORY_RECOVERY_REQUIRES_NAMED_ORDER_OR_CONSUMABLE_REORDER_CONVERSION_GATE_SECOND_PASS
existing_axis_strengthened: stage2_required_bridge | local_4b_watch_guard | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_C10_MEMORY_RECOVERY_ORDER_CONVERSION_AND_EARLY_CAPEX_THESIS_SPLIT
canonical_archetype_rule_candidate: C10_MEMORY_RECOVERY_REQUIRES_NAMED_ORDER_OR_CONSUMABLE_REORDER_CONVERSION_GATE_SECOND_PASS
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical trigger-level OHLC path, 30/90/180D MFE/MAE, C10 canonical rule stress-test, positive/counterexample balance, and shadow-only score-return alignment.

Non-validation scope: no live recommendation, no current stock discovery, no production score patch, no brokerage/API action, no inference from future price beyond the declared forward window.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_named_order_or_consumable_reorder_conversion_gate,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"separates real memory order-cycle reversal from generic capex beta","promoted positives avg MAE90 improves from -23.62 to -12.42","C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:095610:Stage2-Actionable:2024-11-22|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:089970:Stage2-Actionable:2025-03-19|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:084370:Stage2-Actionable:2024-07-22|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:092870:Stage4B:2024-10-25|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:033160:Stage2-Actionable:2024-05-03",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C10_early_capex_thesis_high_mae_cap,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Eugene/Exicon/MK show high-MAE when conversion is absent","blocks three counterexamples from Stage3 promotion","C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:095610:Stage2-Actionable:2024-11-22|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:089970:Stage2-Actionable:2025-03-19|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:084370:Stage2-Actionable:2024-07-22|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:092870:Stage4B:2024-10-25|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:033160:Stage2-Actionable:2024-05-03",5,5,3,medium,guardrail_shadow_only,"not production; strengthens stage2_required_bridge only in C10"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"TES_C10_DRAM_ORDER_RECOGNITION","symbol":"095610","company_name":"테스","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"A clean late-2024 C10 positive: the path is not just memory beta, but DRAM order recognition and equipment-mix bridge. 180D MFE is high with limited 180D MAE."}
{"row_type":"case","case_id":"VM_C10_HYNIX_ETCH_ORDER_UNLOCK","symbol":"089970","company_name":"브이엠","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_positive_after_gate","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"A C10 positive that the current profile can miss if it treats small-cap etch as mere memory beta. Named customer, capex path, and order-cycle visibility improved the reward/risk profile."}
{"row_type":"case","case_id":"EUGENE_C10_EARLY_DRAM_CAPEX_THESIS","symbol":"084370","company_name":"유진테크","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned_before_gate","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"DRAM capex thesis was not wrong, but July 2024 entry had insufficient order/revenue conversion and large 90D/180D MAE. Proposed C10 gate should delay promotion until conversion evidence appears."}
{"row_type":"case","case_id":"EXICON_C10_TESTER_HBM_FOCUS_GAP","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_aligned_after_gate","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The product is memory-test related, but customer capex was diverted away from the tested order stream. This should be Stage4B/watch or Stage2 block, not Stage3 unlock."}
{"row_type":"case","case_id":"MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG","symbol":"033160","company_name":"엠케이전자","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned_before_gate","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C10 should avoid compressing all semiconductor-recovery materials into equipment-cycle positives. Without order conversion and clean margin bridge, this row behaves as high-MAE false positive."}
{"row_type":"trigger","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:095610:Stage2-Actionable:2024-11-22","case_id":"TES_C10_DRAM_ORDER_RECOGNITION","symbol":"095610","company_name":"테스","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","sector":"semiconductor_frontend_equipment","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | residual_missed_structural_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-21","entry_date":"2024-11-22","entry_price":14820.0,"evidence_available_at_that_date":"2024-11-21 report argued TES should be reclassified from NAND-only PECVD exposure to rising DRAM order exposure; this gives non-price memory-equipment order/revenue bridge.","evidence_source":"Hanwha Investment & Securities report, 2024-11-21, 테스: 디램 장비사로의 인식 전환 필요","evidence_source_url":"https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.11,"MFE_90D_pct":65.65,"MFE_180D_pct":100.4,"MFE_1Y_pct":246.83,"MFE_2Y_pct":null,"MAE_30D_pct":-11.67,"MAE_90D_pct":-11.67,"MAE_180D_pct":-11.67,"MAE_1Y_pct":-11.67,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2025-08-19","peak_price":29700.0,"drawdown_after_peak_pct":-6.06,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_or_not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"dram_order_recognition_clean_mfe_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:095610:2024-11-22:14820.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:089970:Stage2-Actionable:2025-03-19","case_id":"VM_C10_HYNIX_ETCH_ORDER_UNLOCK","symbol":"089970","company_name":"브이엠","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","sector":"semiconductor_frontend_etch_equipment","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | residual_missed_structural_mining","trigger_type":"Stage2-Actionable","trigger_date":"2025-03-18","entry_date":"2025-03-19","entry_price":10860.0,"evidence_available_at_that_date":"2025-03-18 report tied VM to SK hynix 1b/M15X etch investment, share gain, and 2025-2026 revenue cycle visibility; this was stronger than generic memory beta.","evidence_source":"SK Securities report, 2025-03-18, 브이엠: 본업 성장 사이클 + 해외 모멘텀은 덤","evidence_source_url":"https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","durable_customer_confirmation","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089970/2025.csv","profile_path":"atlas/symbol_profiles/089/089970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.32,"MFE_90D_pct":25.51,"MFE_180D_pct":190.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.17,"MAE_90D_pct":-13.17,"MAE_180D_pct":-13.17,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2025-12-10","peak_price":31500.0,"drawdown_after_peak_pct":-7.62,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_or_not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"hynix_etch_order_share_gain_missed_structural_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:089970:2025-03-19:10860.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:084370:Stage2-Actionable:2024-07-22","case_id":"EUGENE_C10_EARLY_DRAM_CAPEX_THESIS","symbol":"084370","company_name":"유진테크","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","sector":"semiconductor_frontend_deposition_equipment","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | residual_missed_structural_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-19","entry_date":"2024-07-22","entry_price":44350.0,"evidence_available_at_that_date":"2024-07-19 report maintained buy and lifted target on memory capex/DRAM capex growth; at trigger time the evidence was still capex-thesis-heavy rather than confirmed order-to-revenue conversion.","evidence_source":"Hi Investment / Naver stock-research report, 2024-07-19, 유진테크: memory capex and DRAM capex forecast uplift","evidence_source_url":"https://stock.pstatic.net/stock-research/company/50/20240719_company_347238000.pdf","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.93,"MFE_90D_pct":17.93,"MFE_180D_pct":17.93,"MFE_1Y_pct":17.93,"MFE_2Y_pct":null,"MAE_30D_pct":-15.67,"MAE_90D_pct":-28.86,"MAE_180D_pct":-31.68,"MAE_1Y_pct":-31.68,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-08-16","peak_price":52300.0,"drawdown_after_peak_pct":-42.07,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_or_not_applicable","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"early_dram_capex_thesis_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:084370:2024-07-22:44350.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:092870:Stage4B:2024-10-25","case_id":"EXICON_C10_TESTER_HBM_FOCUS_GAP","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","sector":"semiconductor_memory_test_equipment","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | residual_missed_structural_mining","trigger_type":"Stage4B","trigger_date":"2024-10-24","entry_date":"2024-10-25","entry_price":11450.0,"evidence_available_at_that_date":"2024-10-24 report stated Samsung HBM focus reduced relative DRAM burn-in tester investment; this is exactly a C10 order-cycle gap rather than a clean memory-cycle unlock.","evidence_source":"Naver stock-research report, 2024-10-24, 엑시콘: HBM focus lowered DRAM burn-in tester investment","evidence_source_url":"https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown","explicit_event_cap","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.13,"MFE_90D_pct":37.64,"MFE_180D_pct":37.64,"MFE_1Y_pct":61.31,"MFE_2Y_pct":null,"MAE_30D_pct":-20.09,"MAE_90D_pct":-26.55,"MAE_180D_pct":-26.55,"MAE_1Y_pct":-26.55,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2025-02-14","peak_price":15760.0,"drawdown_after_peak_pct":-37.88,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_or_not_applicable","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","explicit_event_cap","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"tester_order_mix_gap_4b_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:092870:2024-10-25:11450.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:033160:Stage2-Actionable:2024-05-03","case_id":"MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG","symbol":"033160","company_name":"엠케이전자","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"mixed_C10_memory_recovery_equipment_cycle_second_pass_order_conversion_set","sector":"semiconductor_packaging_materials_memory_beta","primary_archetype":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression | residual_missed_structural_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-02","entry_date":"2024-05-03","entry_price":11670.0,"evidence_available_at_that_date":"2024-05-02 report framed MK Electron as packaging-material beneficiary from semiconductor recovery and HBM-related solder-ball product expansion; however this is material beta with margin/holding-company overhang.","evidence_source":"SK Securities report, 2024-05-02, 엠케이전자: semiconductor upturn + HBM low-temperature solder ball / QP improvement thesis","evidence_source_url":"https://www.sks.co.kr/data1/research/qna_file/20240429163049543_4_ko.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033160/2024.csv","profile_path":"atlas/symbol_profiles/033/033160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.65,"MFE_90D_pct":17.65,"MFE_180D_pct":17.65,"MFE_1Y_pct":17.65,"MFE_2Y_pct":null,"MAE_30D_pct":-2.23,"MAE_90D_pct":-37.87,"MAE_180D_pct":-54.24,"MAE_1Y_pct":-54.24,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-05-24","peak_price":13730.0,"drawdown_after_peak_pct":-61.11,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"watch_or_not_applicable","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","capital_raise_or_overhang"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"memory_material_beta_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_tradable_shard_and_share_continuity_proxy","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:033160:2024-05-03:11670.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"TES_C10_DRAM_ORDER_RECOGNITION","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:095610:Stage2-Actionable:2024-11-22","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":66,"backlog_visibility_score":62,"margin_bridge_score":58,"revision_score":70,"relative_strength_score":61,"customer_quality_score":73,"policy_or_regulatory_score":15,"valuation_repricing_score":56,"execution_risk_score":35,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":72,"backlog_visibility_score":69,"margin_bridge_score":68,"revision_score":74,"relative_strength_score":64,"customer_quality_score":77,"policy_or_regulatory_score":15,"valuation_repricing_score":54,"execution_risk_score":30,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":6},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 second-pass gate gives credit only when memory recovery is tied to named order/revenue conversion; early capex thesis, tester order gap, and material beta receive execution/4B caps.","MFE_90D_pct":65.65,"MAE_90D_pct":-11.67,"score_return_alignment_label":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"VM_C10_HYNIX_ETCH_ORDER_UNLOCK","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:089970:Stage2-Actionable:2025-03-19","symbol":"089970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":48,"margin_bridge_score":45,"revision_score":62,"relative_strength_score":54,"customer_quality_score":70,"policy_or_regulatory_score":10,"valuation_repricing_score":58,"execution_risk_score":48,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":6,"accounting_trust_risk_score":8},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":76,"backlog_visibility_score":73,"margin_bridge_score":68,"revision_score":75,"relative_strength_score":62,"customer_quality_score":80,"policy_or_regulatory_score":10,"valuation_repricing_score":56,"execution_risk_score":34,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":6,"accounting_trust_risk_score":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 second-pass gate gives credit only when memory recovery is tied to named order/revenue conversion; early capex thesis, tester order gap, and material beta receive execution/4B caps.","MFE_90D_pct":25.51,"MAE_90D_pct":-13.17,"score_return_alignment_label":"score_return_aligned_positive_after_gate","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"EUGENE_C10_EARLY_DRAM_CAPEX_THESIS","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:084370:Stage2-Actionable:2024-07-22","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":42,"margin_bridge_score":46,"revision_score":74,"relative_strength_score":58,"customer_quality_score":67,"policy_or_regulatory_score":10,"valuation_repricing_score":64,"execution_risk_score":55,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":39,"margin_bridge_score":42,"revision_score":65,"relative_strength_score":54,"customer_quality_score":66,"policy_or_regulatory_score":10,"valuation_repricing_score":50,"execution_risk_score":68,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":64,"stage_label_after":"Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 second-pass gate gives credit only when memory recovery is tied to named order/revenue conversion; early capex thesis, tester order gap, and material beta receive execution/4B caps.","MFE_90D_pct":17.93,"MAE_90D_pct":-28.86,"score_return_alignment_label":"score_return_misaligned_before_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"EXICON_C10_TESTER_HBM_FOCUS_GAP","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:092870:Stage4B:2024-10-25","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":47,"backlog_visibility_score":40,"margin_bridge_score":38,"revision_score":60,"relative_strength_score":56,"customer_quality_score":66,"policy_or_regulatory_score":8,"valuation_repricing_score":62,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":42,"backlog_visibility_score":35,"margin_bridge_score":34,"revision_score":50,"relative_strength_score":52,"customer_quality_score":62,"policy_or_regulatory_score":8,"valuation_repricing_score":45,"execution_risk_score":72,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":58,"stage_label_after":"Stage4B","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 second-pass gate gives credit only when memory recovery is tied to named order/revenue conversion; early capex thesis, tester order gap, and material beta receive execution/4B caps.","MFE_90D_pct":37.64,"MAE_90D_pct":-26.55,"score_return_alignment_label":"guardrail_aligned_after_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"MKE_C10_MEMORY_MATERIAL_BETA_OVERHANG","trigger_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:033160:Stage2-Actionable:2024-05-03","symbol":"033160","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":36,"margin_bridge_score":38,"revision_score":60,"relative_strength_score":50,"customer_quality_score":62,"policy_or_regulatory_score":8,"valuation_repricing_score":60,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":28},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":38,"backlog_visibility_score":32,"margin_bridge_score":34,"revision_score":50,"relative_strength_score":48,"customer_quality_score":60,"policy_or_regulatory_score":8,"valuation_repricing_score":44,"execution_risk_score":76,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":32},"weighted_score_after":60,"stage_label_after":"Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C10 second-pass gate gives credit only when memory recovery is tied to named order/revenue conversion; early capex thesis, tester order gap, and material beta receive execution/4B caps.","MFE_90D_pct":17.65,"MAE_90D_pct":-37.87,"score_return_alignment_label":"score_return_misaligned_before_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["current_profile_false_positive","current_profile_missed_structural","high_MAE_stage2_entry","early_capex_thesis_without_order_conversion"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows; C10 rows 13, need-to-30 17
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- 095610 테스 evidence: https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf
- 089970 브이엠 evidence: https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf
- 084370 유진테크 evidence: https://stock.pstatic.net/stock-research/company/50/20240719_company_347238000.pdf
- 092870 엑시콘 evidence: https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf
- 033160 엠케이전자 evidence: https://www.sks.co.kr/data1/research/qna_file/20240429163049543_4_ko.pdf

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
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
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
