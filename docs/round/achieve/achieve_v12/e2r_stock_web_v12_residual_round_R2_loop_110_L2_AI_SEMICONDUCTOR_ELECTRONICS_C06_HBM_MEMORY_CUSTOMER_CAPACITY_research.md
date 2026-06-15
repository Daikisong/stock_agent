# E2R Stock-Web v12 Residual Research — R2 / C06 HBM Memory Customer Capacity / Loop 110

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
completed_round: R2
completed_loop: 110
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: mixed_C06_hbm_adjacent_osat_test_packaging_proxy_decontamination_third_pass
loop_objective: coverage_gap_fill | counterexample_mining | HBM_adjacent_proxy_decontamination | C06_C07_C08_OSAT_boundary_validation | local_4B_watch_test
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scheduler decision

`V12_Research_No_Repeat_Index.md` 기준으로 C06은 static ledger에서 `17 rows`, `need-to-30 13`으로 남아 있는 Priority 0 canonical이다. 이 세션에서 이미 생성한 C06 loop 108과 loop 109의 symbol set은 `000660, 005930, 222800, 353200, 011070, 007660, 356860, 195870, 007810, 009150`로 확인했기 때문에 이번 loop는 해당 symbol을 전부 피했다.

이번 목적은 pure HBM memory supplier가 아닌 **HBM-adjacent OSAT / test socket / probe-card PCB / 2.5D packaging proxy**가 C06 Green으로 과승격되는 잔여 오류를 찾는 것이다. 같은 C06이어도 이 경계는 중요하다. HBM은 전력선처럼 생태계 전체를 밝히지만, 모든 전선이 발전소는 아니다. C06의 발전소는 고객 capacity allocation, shipment/revenue recognition, margin bridge다.

## 2. Stock-Web manifest and schema check

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema rule used:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable requires entry row, 180 forward tradable rows, complete 30/90/180D MFE·MAE, and clean 180D corporate-action window.
```

## 3. Novelty and duplicate check

```yaml
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
same_archetype_new_regime: HBM-adjacent proxy decontamination after pure HBM supplier / substrate passes
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
```

## 4. Case summary

| symbol | company | role | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 067310 | 하나마이크론 | positive_with_4B_watch | Stage2-Actionable | 2023-10-23 | 2023-10-24 | 28,050 | 22.99% | -14.44% | 22.99% | -32.01% | current_profile_mixed_stage2_ok_green_too_fast |
| 058470 | 리노공업 | positive_with_4B_watch | Stage2-Actionable | 2024-01-24 | 2024-01-25 | 225,000 | 37.33% | -16.49% | 37.33% | -27.11% | current_profile_mixed_stage2_ok_green_boundary_cap_needed |
| 219130 | 타이거일렉 | positive_with_4B_watch | Stage2-Actionable | 2024-01-24 | 2024-01-25 | 25,000 | 81.20% | -9.60% | 81.20% | -40.16% | current_profile_mixed_stage2_ok_green_boundary_cap_needed |
| 033640 | 네패스 | counterexample | Stage2-Actionable | 2024-05-20 | 2024-05-21 | 17,870 | 2.80% | -55.06% | 2.80% | -66.76% | current_profile_false_positive |
| 131970 | 두산테스나 | counterexample | Stage2-Actionable | 2024-07-13 | 2024-07-15 | 41,900 | 2.86% | -45.47% | 2.86% | -47.26% | current_profile_false_positive |

## 5. Evidence sources

| symbol | company | evidence source |
|---|---|---|
| 067310 | 하나마이크론 | https://www.businesspost.co.kr/BP?command=article_view&num=330599 |
| 058470 | 리노공업 | https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2020%2F2024012310041539K_02_05.pdf&inlineYn=Y&saveKey=research.pdf |
| 219130 | 타이거일렉 | https://ssl.pstatic.net/imgstock/upload/research/company/1706051001659.pdf |
| 033640 | 네패스 | https://www.e4ds.com/sub_view.asp?ch=2&idx=18989&t=0 |
| 131970 | 두산테스나 | https://www.thelec.kr/news/articleView.html?idxno=29053 |

## 6. Corporate-action and price-window validation

| symbol | profile_path | corporate_action_candidate_dates | 180D status |
|---|---|---|---|
| 067310 | atlas/symbol_profiles/067/067310.json | 2009-11-10, 2021-12-29 | clean_180D_window |
| 058470 | atlas/symbol_profiles/058/058470.json | 2013-06-13, 2013-07-08, 2025-04-25 | clean_180D_window |
| 219130 | atlas/symbol_profiles/219/219130.json | none | clean_180D_window |
| 033640 | atlas/symbol_profiles/033/033640.json | 2000-05-02, 2001-05-11, 2004-01-26 | clean_180D_window |
| 131970 | atlas/symbol_profiles/131/131970.json | 2020-09-15, 2020-10-07 | clean_180D_window |

All five rows use `tradable_raw` rows from `atlas/ohlcv_tradable_by_symbol_year`. None of the listed corporate-action candidate dates overlaps the entry_date through D+180 trading-day window. Therefore all five trigger rows are marked `calibration_usable=true`.

## 7. Case interpretation

### 7.1 067310 하나마이크론 — HBM backend proxy positive, but not pure C06 Green

BusinessPost framed HBM demand as a backend opportunity and explicitly connected Hana Micron with Samsung/SK hynix packaging and test work. The price path gave enough 90D MFE to justify Stage2-Actionable and possibly a sector watch, but the 180D MAE and peak drawdown argue against opening C06 Green from HBM proxy language alone. The rule pressure is clear: HBM backend exposure should require customer allocation plus shipment/revenue/margin evidence before Stage3.

### 7.2 058470 리노공업 — test socket catalyst, positive-with-4B watch

Samsung Securities treated HBM package test sockets as a potential domestic value-chain benefit if R&D sockets moved to mass production. Leeno’s 90D MFE confirms that the market could price this catalyst. But this is a C06/C08 boundary, not a pure memory customer/capacity case. It belongs in Stage2-Actionable plus local 4B watch unless socket revenue conversion and HBM customer adoption are explicit.

### 7.3 219130 타이거일렉 — probe-card PCB recovery can explode, but C06 should cap the proxy

Tiger Elec had the cleanest short-window path in this pass. KIRS noted DRAM probe-card PCB qualification and NAND utilization recovery. Yet the same report also warned that the lack of new CAPA limited the thesis. The 180D drawdown after a huge MFE is exactly why the C06 shadow rule needs a proxy cap: memory test PCB beta is useful evidence, not equivalent to HBM memory capacity allocation.

### 7.4 033640 네패스 — 2.5D/HBM technology roadmap false Stage2

Nepes had legitimate advanced packaging technology language, and the source described 2.5D packaging as used to integrate AI semiconductors and HBM. However, commercialization and mass-production timing were still future-facing. The price path was almost all MAE with no real MFE. This is a clean counterexample: technology roadmap without named customer revenue bridge should be blocked from C06 Stage2/3 promotion.

### 7.5 131970 두산테스나 — general OSAT strategy is not HBM capacity allocation

TheElec reported Doosan Group’s plan to build Doosan Tesna into an integrated OSAT, but also noted that additional capabilities were needed for full turnkey backend service. This was a corporate strategy/OSAT expansion event, not an HBM memory customer capacity allocation event. The price path confirms the distinction: MFE was negligible and MAE was severe.

## 8. Residual conclusion

C06 should become stricter about **proxy contamination**. HBM-adjacent exposure has three layers:

1. **Pure C06:** memory supplier/customer capacity allocation, HBM shipment/revenue recognition, ASP/mix/margin revision.
2. **Boundary Stage2:** OSAT, socket, probe-card PCB, package substrate, 2.5D packaging, and AI substrate evidence with some customer quality but weak revenue bridge.
3. **Blocked / local 4B:** technology roadmap, future commercialization, capacity target, or theme language without named customer allocation and near-term conversion.

The proposed sector/canonical rule is:

```text
C06_PURE_HBM_CAPACITY_REQUIRES_CUSTOMER_ALLOCATION_SHIPMENT_REVENUE_MARGIN_BRIDGE_WITH_PROXY_4B_CAP_THIRD_PASS
```

This strengthens:

```text
stage2_required_bridge
local_4b_watch_guard
full_4b_requires_non_price_evidence
price_only_blowoff_blocks_positive_stage
```

## 9. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C06_R2L110_067310_HBM_OSAT_SKHYNIX_PACKAGING_CAPACITY_POSITIVE_WITH_4B_WATCH_20231023","symbol":"067310","company_name":"하나마이크론","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_OSAT_SKHYNIX_PACKAGING_CAPACITY_POSITIVE_WITH_4B_WATCH","case_type":"structural_success_with_watch","positive_or_counterexample":"positive","best_trigger":"C06_R2L110_067310_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_mixed_stage2_ok_green_too_fast","price_source":"Songdaiki/stock-web","notes":"hbm_backend_capacity_proxy_positive_but_late_chase_4b_watch"}
{"row_type":"trigger","trigger_id":"C06_R2L110_067310_T1","case_id":"C06_R2L110_067310_HBM_OSAT_SKHYNIX_PACKAGING_CAPACITY_POSITIVE_WITH_4B_WATCH_20231023","symbol":"067310","company_name":"하나마이크론","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_OSAT_SKHYNIX_PACKAGING_CAPACITY_POSITIVE_WITH_4B_WATCH","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | HBM_adjacent_proxy_decontamination | C06_C07_C08_OSAT_boundary_validation | local_4B_watch_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-23","evidence_available_at_that_date":"BusinessPost reported that HBM demand growth could increase work for backend companies, and described Hana Micron as a Samsung/SK hynix semiconductor packaging and test contractor with SK hynix-linked backend outsourcing through Hana Micron Vina.","evidence_source":"https://www.businesspost.co.kr/BP?command=article_view&num=330599","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067310/2023.csv","profile_path":"atlas/symbol_profiles/067/067310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-24","entry_price":28050.0,"MFE_30D_pct":22.99,"MAE_30D_pct":-13.73,"MFE_90D_pct":22.99,"MAE_90D_pct":-14.44,"MFE_180D_pct":22.99,"MAE_180D_pct":-32.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-08","peak_price":34500.0,"drawdown_after_peak_pct":-44.72,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"post_peak_4B_watch_needed","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_backend_capacity_proxy_positive_but_late_chase_4b_watch","current_profile_verdict":"current_profile_mixed_stage2_ok_green_too_fast","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|067310|2023-10-24|28050.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L110_067310_HBM_OSAT_SKHYNIX_PACKAGING_CAPACITY_POSITIVE_WITH_4B_WATCH_20231023","trigger_id":"C06_R2L110_067310_T1","symbol":"067310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":70,"margin_bridge_score":58,"revision_score":62,"relative_strength_score":86,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":78,"execution_risk_score":48,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":64,"margin_bridge_score":52,"revision_score":58,"relative_strength_score":78,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":64,"execution_risk_score":62,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable + local_4B_watch","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Third-pass C06 rule separates pure HBM customer/capacity allocation from OSAT, test-socket, probe-card PCB, and 2.5D packaging proxies unless shipment/revenue/margin conversion is visible.","MFE_90D_pct":22.99,"MAE_90D_pct":-14.44,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_mixed_stage2_ok_green_too_fast"}
{"row_type":"case","case_id":"C06_R2L110_058470_HBM_TEST_SOCKET_RND_TO_MASS_PRODUCTION_OPTIONALITY_POSITIVE_WITH_4B_WATCH_20240124","symbol":"058470","company_name":"리노공업","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TEST_SOCKET_RND_TO_MASS_PRODUCTION_OPTIONALITY_POSITIVE_WITH_4B_WATCH","case_type":"structural_success_with_watch","positive_or_counterexample":"positive","best_trigger":"C06_R2L110_058470_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_mixed_stage2_ok_green_boundary_cap_needed","price_source":"Songdaiki/stock-web","notes":"hbm_test_socket_positive_but_c06_pure_memory_green_cap"}
{"row_type":"trigger","trigger_id":"C06_R2L110_058470_T1","case_id":"C06_R2L110_058470_HBM_TEST_SOCKET_RND_TO_MASS_PRODUCTION_OPTIONALITY_POSITIVE_WITH_4B_WATCH_20240124","symbol":"058470","company_name":"리노공업","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TEST_SOCKET_RND_TO_MASS_PRODUCTION_OPTIONALITY_POSITIVE_WITH_4B_WATCH","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | HBM_adjacent_proxy_decontamination | C06_C07_C08_OSAT_boundary_validation | local_4B_watch_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","evidence_available_at_that_date":"Samsung Securities described HBM package test sockets as a potential value-chain area and said domestic companies supplying R&D test sockets, including Leeno and ISC, could benefit if HBM sockets moved beyond R&D into mass production.","evidence_source":"https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2020%2F2024012310041539K_02_05.pdf&inlineYn=Y&saveKey=research.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":225000.0,"MFE_30D_pct":11.33,"MAE_30D_pct":-16.49,"MFE_90D_pct":37.33,"MAE_90D_pct":-16.49,"MFE_180D_pct":37.33,"MAE_180D_pct":-27.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000.0,"drawdown_after_peak_pct":-46.93,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"post_peak_4B_watch_needed","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_test_socket_positive_but_c06_pure_memory_green_cap","current_profile_verdict":"current_profile_mixed_stage2_ok_green_boundary_cap_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|058470|2024-01-25|225000.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L110_058470_HBM_TEST_SOCKET_RND_TO_MASS_PRODUCTION_OPTIONALITY_POSITIVE_WITH_4B_WATCH_20240124","trigger_id":"C06_R2L110_058470_T1","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":55,"margin_bridge_score":62,"revision_score":64,"relative_strength_score":84,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":78,"execution_risk_score":45,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":42,"backlog_visibility_score":50,"margin_bridge_score":56,"revision_score":58,"relative_strength_score":80,"customer_quality_score":78,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":66,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable + local_4B_watch","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Third-pass C06 rule separates pure HBM customer/capacity allocation from OSAT, test-socket, probe-card PCB, and 2.5D packaging proxies unless shipment/revenue/margin conversion is visible.","MFE_90D_pct":37.33,"MAE_90D_pct":-16.49,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_mixed_stage2_ok_green_boundary_cap_needed"}
{"row_type":"case","case_id":"C06_R2L110_219130_DRAM_PROBE_CARD_PCB_QUAL_NAND_UTILIZATION_RECOVERY_POSITIVE_WITH_4B_WATCH_20240124","symbol":"219130","company_name":"타이거일렉","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"DRAM_PROBE_CARD_PCB_QUAL_NAND_UTILIZATION_RECOVERY_POSITIVE_WITH_4B_WATCH","case_type":"structural_success_with_watch","positive_or_counterexample":"positive","best_trigger":"C06_R2L110_219130_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_mixed_stage2_ok_green_boundary_cap_needed","price_source":"Songdaiki/stock-web","notes":"memory_test_pcb_positive_but_c06_hbm_capacity_proxy_cap"}
{"row_type":"trigger","trigger_id":"C06_R2L110_219130_T1","case_id":"C06_R2L110_219130_DRAM_PROBE_CARD_PCB_QUAL_NAND_UTILIZATION_RECOVERY_POSITIVE_WITH_4B_WATCH_20240124","symbol":"219130","company_name":"타이거일렉","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"DRAM_PROBE_CARD_PCB_QUAL_NAND_UTILIZATION_RECOVERY_POSITIVE_WITH_4B_WATCH","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | HBM_adjacent_proxy_decontamination | C06_C07_C08_OSAT_boundary_validation | local_4B_watch_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","evidence_available_at_that_date":"KIRS described Tiger Elec as a semiconductor inspection PCB maker, noted DRAM probe-card PCB qualification with FormFactor in 2023, and expected NAND utilization recovery to support probe-card demand while warning that lack of new capacity investment limited the upside.","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1706051001659.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv","profile_path":"atlas/symbol_profiles/219/219130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":25000.0,"MFE_30D_pct":41.6,"MAE_30D_pct":-9.6,"MFE_90D_pct":81.2,"MAE_90D_pct":-9.6,"MFE_180D_pct":81.2,"MAE_180D_pct":-40.16,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":45300.0,"drawdown_after_peak_pct":-66.98,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"post_peak_4B_watch_needed","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"memory_test_pcb_positive_but_c06_hbm_capacity_proxy_cap","current_profile_verdict":"current_profile_mixed_stage2_ok_green_boundary_cap_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|219130|2024-01-25|25000.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L110_219130_DRAM_PROBE_CARD_PCB_QUAL_NAND_UTILIZATION_RECOVERY_POSITIVE_WITH_4B_WATCH_20240124","trigger_id":"C06_R2L110_219130_T1","symbol":"219130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":52,"backlog_visibility_score":58,"margin_bridge_score":60,"revision_score":62,"relative_strength_score":90,"customer_quality_score":76,"policy_or_regulatory_score":0,"valuation_repricing_score":82,"execution_risk_score":48,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":48,"backlog_visibility_score":50,"margin_bridge_score":52,"revision_score":58,"relative_strength_score":84,"customer_quality_score":72,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":70,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable + local_4B_watch","changed_components":["backlog_visibility_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Third-pass C06 rule separates pure HBM customer/capacity allocation from OSAT, test-socket, probe-card PCB, and 2.5D packaging proxies unless shipment/revenue/margin conversion is visible.","MFE_90D_pct":81.2,"MAE_90D_pct":-9.6,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_mixed_stage2_ok_green_boundary_cap_needed"}
{"row_type":"case","case_id":"C06_R2L110_033640_AI_HBM_25D_PACKAGING_TECHNOLOGY_WITHOUT_CUSTOMER_REVENUE_FALSE_STAGE2_20240520","symbol":"033640","company_name":"네패스","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_HBM_25D_PACKAGING_TECHNOLOGY_WITHOUT_CUSTOMER_REVENUE_FALSE_STAGE2","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_R2L110_033640_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"advanced_packaging_technology_optional_revenue_delay_false_stage2"}
{"row_type":"trigger","trigger_id":"C06_R2L110_033640_T1","case_id":"C06_R2L110_033640_AI_HBM_25D_PACKAGING_TECHNOLOGY_WITHOUT_CUSTOMER_REVENUE_FALSE_STAGE2_20240520","symbol":"033640","company_name":"네패스","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_HBM_25D_PACKAGING_TECHNOLOGY_WITHOUT_CUSTOMER_REVENUE_FALSE_STAGE2","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | HBM_adjacent_proxy_decontamination | C06_C07_C08_OSAT_boundary_validation | local_4B_watch_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-20","evidence_available_at_that_date":"e4ds reported that Nepes completed PoP technology and was pursuing 2.5D packaging commercialization; it explained that 2.5D packaging integrates AI semiconductors and HBM, but the commercial mass-production target was still in the future and customer revenue was not yet confirmed.","evidence_source":"https://www.e4ds.com/sub_view.asp?ch=2&idx=18989&t=0","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033640/2024.csv","profile_path":"atlas/symbol_profiles/033/033640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-21","entry_price":17870.0,"MFE_30D_pct":2.8,"MAE_30D_pct":-16.06,"MFE_90D_pct":2.8,"MAE_90D_pct":-55.06,"MFE_180D_pct":2.8,"MAE_180D_pct":-66.76,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-30","peak_price":18370.0,"drawdown_after_peak_pct":-67.66,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"event_or_theme_stage2_should_be_capped_before_drawdown","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"advanced_packaging_technology_optional_revenue_delay_false_stage2","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|033640|2024-05-21|17870.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L110_033640_AI_HBM_25D_PACKAGING_TECHNOLOGY_WITHOUT_CUSTOMER_REVENUE_FALSE_STAGE2_20240520","trigger_id":"C06_R2L110_033640_T1","symbol":"033640","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":42,"margin_bridge_score":35,"revision_score":42,"relative_strength_score":55,"customer_quality_score":55,"policy_or_regulatory_score":5,"valuation_repricing_score":68,"execution_risk_score":62,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":30,"margin_bridge_score":24,"revision_score":30,"relative_strength_score":45,"customer_quality_score":42,"policy_or_regulatory_score":5,"valuation_repricing_score":42,"execution_risk_score":84,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12},"weighted_score_after":58,"stage_label_after":"Stage1/Watch + local_4B_cap","changed_components":["contract_score","margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Third-pass C06 rule separates pure HBM customer/capacity allocation from OSAT, test-socket, probe-card PCB, and 2.5D packaging proxies unless shipment/revenue/margin conversion is visible.","MFE_90D_pct":2.8,"MAE_90D_pct":-55.06,"score_return_alignment_label":"misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_R2L110_131970_GENERAL_OSAT_TURNKEY_EXPANSION_WITHOUT_HBM_CUSTOMER_CAPACITY_FALSE_STAGE2_20240713","symbol":"131970","company_name":"두산테스나","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"GENERAL_OSAT_TURNKEY_EXPANSION_WITHOUT_HBM_CUSTOMER_CAPACITY_FALSE_STAGE2","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C06_R2L110_131970_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"score_price_alignment":"misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"general_osat_turnkey_theme_not_c06_hbm_capacity_false_positive"}
{"row_type":"trigger","trigger_id":"C06_R2L110_131970_T1","case_id":"C06_R2L110_131970_GENERAL_OSAT_TURNKEY_EXPANSION_WITHOUT_HBM_CUSTOMER_CAPACITY_FALSE_STAGE2_20240713","symbol":"131970","company_name":"두산테스나","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"GENERAL_OSAT_TURNKEY_EXPANSION_WITHOUT_HBM_CUSTOMER_CAPACITY_FALSE_STAGE2","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill | counterexample_mining | HBM_adjacent_proxy_decontamination | C06_C07_C08_OSAT_boundary_validation | local_4B_watch_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-13","evidence_available_at_that_date":"TheElec reported Doosan Group’s plan to grow Doosan Tesna into an integrated OSAT and noted that additional capability such as bumping would be needed for a full turnkey backend service; the event was OSAT expansion, not confirmed HBM customer capacity allocation.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=29053","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131970/2024.csv","profile_path":"atlas/symbol_profiles/131/131970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-15","entry_price":41900.0,"MFE_30D_pct":2.86,"MAE_30D_pct":-30.19,"MFE_90D_pct":2.86,"MAE_90D_pct":-45.47,"MFE_180D_pct":2.86,"MAE_180D_pct":-47.26,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":43100.0,"drawdown_after_peak_pct":-48.72,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"event_or_theme_stage2_should_be_capped_before_drawdown","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"general_osat_turnkey_theme_not_c06_hbm_capacity_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|131970|2024-07-15|41900.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L110_131970_GENERAL_OSAT_TURNKEY_EXPANSION_WITHOUT_HBM_CUSTOMER_CAPACITY_FALSE_STAGE2_20240713","trigger_id":"C06_R2L110_131970_T1","symbol":"131970","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":28,"backlog_visibility_score":40,"margin_bridge_score":36,"revision_score":40,"relative_strength_score":48,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":64,"execution_risk_score":60,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":28,"margin_bridge_score":22,"revision_score":30,"relative_strength_score":40,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":38,"execution_risk_score":86,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":56,"stage_label_after":"Stage1/Watch + local_4B_cap","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Third-pass C06 rule separates pure HBM customer/capacity allocation from OSAT, test-socket, probe-card PCB, and 2.5D packaging proxies unless shipment/revenue/margin conversion is visible.","MFE_90D_pct":2.86,"MAE_90D_pct":-45.47,"score_return_alignment_label":"misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"aggregate","aggregate_id":"C06_R2L110_AGGREGATE","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","case_count":5,"trigger_count":5,"calibration_usable_rows":5,"representative_rows":5,"positive_case_count":3,"counterexample_count":2,"4B_case_count":5,"4C_case_count":0,"avg_MFE_90D_pct":29.44,"avg_MAE_90D_pct":-28.21,"avg_MFE_180D_pct":29.44,"avg_MAE_180D_pct":-42.66,"current_profile_error_count":4,"residual_pattern":"HBM-adjacent OSAT/test/packaging proxies can create valid Stage2 watch but fail C06 Green without customer capacity allocation, shipment/revenue recognition, and margin bridge."}
{"row_type":"shadow_weight","shadow_weight_id":"C06_R2L110_SHADOW_RULE","round":"R2","loop":"110","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","proposed_rule_candidate":"C06_PURE_HBM_CAPACITY_REQUIRES_CUSTOMER_ALLOCATION_SHIPMENT_REVENUE_MARGIN_BRIDGE_WITH_PROXY_4B_CAP_THIRD_PASS","do_not_propose_new_weight_delta":false,"shadow_weight_only":true,"strengthen_components":["customer_quality_score","capacity_allocation_score","margin_bridge_score","execution_risk_score"],"cap_conditions":["HBM-adjacent OSAT/test/socket/PCB/2.5D packaging proxy without named memory customer allocation","technology roadmap without revenue recognition","fast MFE followed by >25% 180D MAE"],"existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"]}
{"row_type":"residual_contribution","residual_contribution_id":"C06_R2L110_RESIDUAL","round":"R2","loop":"110","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"current_profile_error_count":4,"loop_contribution_label":"canonical_archetype_rule_candidate","coverage_effect":"No-Repeat static C06 17 -> 22 from this file alone; current-session adjusted C06 loop_108/109/110 moves 17 -> 32 if all accepted."}
```

## 10. Batch ingest self-audit

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

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation coding agent for Songdaiki/stock_agent. Do not execute this handoff inside the research session. When the user explicitly starts a batch ingestion/implementation session, ingest this standalone V12 research MD together with other docs/round files. Parse all machine-readable JSONL rows, validate the Stock-Web entry_date / entry_price / MFE_30D_pct / MAE_30D_pct / MFE_90D_pct / MAE_90D_pct / MFE_180D_pct / MAE_180D_pct fields, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and evaluate the shadow rule candidate C06_PURE_HBM_CAPACITY_REQUIRES_CUSTOMER_ALLOCATION_SHIPMENT_REVENUE_MARGIN_BRIDGE_WITH_PROXY_4B_CAP_THIRD_PASS. Do not treat this MD alone as production scoring authority; combine it with the full V12 corpus and only apply a safe patch if aggregate evidence supports it.
```

## 12. Next research state

```text
completed_round = R2
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_followup_if_below_50 | C27_CONTENT_IP_GLOBAL_MONETIZATION | C05_EPC_MEGA_CONTRACT_MARGIN_GAP_followup_if_below_50 | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
