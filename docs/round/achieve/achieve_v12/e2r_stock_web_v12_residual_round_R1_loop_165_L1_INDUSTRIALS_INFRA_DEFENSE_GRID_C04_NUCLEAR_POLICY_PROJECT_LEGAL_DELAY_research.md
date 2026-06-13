# E2R v12 Residual Research — R1/L1/C04 Nuclear Policy Project Legal Delay
```yaml
completed_round: "R1"
completed_loop: 165
selected_round: "R1"
selected_loop: 165
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 2 quality-repair after session-aware P0/P1/thin-P2 clearing"
round_schedule_status: "coverage_index_selected_not_sequential"
round_sector_consistency: "pass"
large_sector_id: "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
canonical_archetype_id: "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY"
fine_archetype_id: "mixed_c04_czech_project_legal_delay_domestic_policy_smr_supplier_leaf_set"
price_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_patch_allowed: false
live_candidate_mode: false
auto_trading_allowed: false
output_filename: "e2r_stock_web_v12_residual_round_R1_loop_165_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md"
```

## 1. Selection / no-repeat rationale

- The static No-Repeat Index lists C04 with 71 representative rows, already above the 50-row floor, so this is not a volume-filling pass. It is a quality-repair pass after this session already cleared multiple P0/P1 gaps.
- C04 still has a hard modeling problem: nuclear headlines arrive in layers — preferred bidder, legal appeal, settlement, final contract, domestic power-plan policy, SMR supply-chain expansion. Treating every layer as the same Stage2 signal either buys too early into legal delay or misses the legal-risk-relief inflection.
- This file avoids the session-local C01/C02/C03/C05 industrial backlog/defense/EPC sets and isolates C04 nuclear project/legal-delay behavior. Existing high-frequency top symbols are allowed only when the trigger family is different, because C04 is dominated by a few true project-exposure names.

## 2. Price atlas validation

| item | value |
|---|---|
| primary_price_source | Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| source_name | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| max_date | 2026-02-20 |
| MFE/MAE formula | inclusive window from entry_date through D+N tradable rows; max high / min low vs entry close |

Corporate-action profile check: no selected entry-to-D180 window overlaps the corporate-action candidate dates visible in the stock-web symbol profiles. Historical candidates for these tickers are outside 2024-2026 windows: 034020 has 2019/2020 candidates; 052690 and 051600 have none; 047040 has 2001/2003/2011; 105840 has 2012; 032820 has 2003-2009; 011700 has 1998/2006; 083650 has 2006/2015.

## 3. Evidence spine

- 2024-07-17: KHNP was selected as preferred bidder for two Czech nuclear units, with Team Korea including KEPCO E&C, KEPCO Nuclear Fuel, KEPCO KPS, Doosan Enerbility, and Daewoo E&C.
- 2024-10-30/31: Czech UOHS temporarily blocked contract signing after appeals, then rejected/stopped the appeals; CEZ still targeted contract conclusion by the following March. This is a legal-delay watch, not an automatic hard 4C.
- 2025-01-17: Westinghouse, KEPCO, and KHNP announced a global settlement of the IP dispute. This is the cleanest C04 legal-risk-relief trigger before the final Czech signing.
- 2025-02-21: Korea confirmed the 11th Basic Plan, including construction of two nuclear plants and one domestic SMR by 2038. This supports domestic policy beta but does not, by itself, identify company-level contract share.
- 2025-05-20: BHI-specific SMR/BOP supply-chain evidence adds an execution bridge beyond generic policy beta.

## 4. Case table

| case_id | ticker | name | trigger | entry | type | outcome | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | rule lesson |
|---|---:|---|---|---|---|---|---:|---:|---:|---|
| C04_165_001 | 034020 | 두산에너빌리티 | 2025-01-17 | 2025-01-20 @ 21900 | Stage2-Actionable | positive | 41.1/-1.37 | 120.09/-8.86 | 286.76/-8.86 | too_late_if_wait_final_contract |
| C04_165_002 | 052690 | 한전기술 | 2024-07-17 | 2024-07-18 @ 82000 | Stage2-Watch | counterexample | 19.63/-24.88 | 19.63/-24.88 | 19.63/-39.94 | false_positive_if_preferred_bidder_equals_signed_contract |
| C04_165_003 | 051600 | 한전KPS | 2024-07-17 | 2024-07-18 @ 38900 | Stage2-Actionable | positive | 21.98/-7.84 | 24.04/-7.84 | 26.22/-7.84 | current_profile_ok_but_should_prefer_low_mae_service_bridge |
| C04_165_004 | 047040 | 대우건설 | 2024-07-17 | 2024-07-18 @ 4250 | Stage2-Watch | counterexample | 16.82/-16.59 | 16.82/-20.59 | 16.82/-30.82 | false_positive_if_consortium_name_without_margin_bridge |
| C04_165_005 | 034020 | 두산에너빌리티 | 2024-10-31 | 2024-10-31 @ 20050 | Stage4C-Audit | positive | 13.72/-15.66 | 54.11/-15.66 | 260.1/-15.66 | hard_4c_too_early_on_legal_delay_wording |
| C04_165_006 | 052690 | 한전기술 | 2025-01-17 | 2025-01-20 @ 64600 | Stage2-Actionable | positive | 17.49/-5.42 | 21.98/-22.91 | 88.39/-22.91 | ok_direction_but_missing_high_mae_entry_guard |
| C04_165_007 | 105840 | 우진 | 2025-02-21 | 2025-02-21 @ 8160 | Stage2-Watch | positive | 2.21/-23.77 | 62.99/-26.47 | 138.36/-26.47 | too_early_actionable_without_new_order_or_mae_guard |
| C04_165_008 | 032820 | 우리기술 | 2025-02-21 | 2025-02-21 @ 2140 | Stage2-Watch | positive | 3.5/-27.24 | 144.86/-32.1 | 161.68/-32.1 | actionable_needs_signed_contract_or_staged_entry_guard |
| C04_165_009 | 011700 | 한신기계 | 2025-02-21 | 2025-02-21 @ 3415 | Stage2-FalsePositive | counterexample | 0.88/-28.99 | 53.15/-30.89 | 53.15/-30.89 | theme_only_false_positive |
| C04_165_010 | 083650 | 비에이치아이 | 2025-05-20 | 2025-05-20 @ 38400 | Stage2-Actionable | positive | 23.96/-12.89 | 54.69/-12.89 | 110.42/-12.89 | current_profile_may_underweight_supplier_execution_bridge |

## 5. Case notes

### C04_165_001 — 034020 두산에너빌리티
- evidence_family: `westinghouse_ip_settlement_czech_legal_risk_relief`
- fine_archetype_id: `C04_CZECH_LEGAL_RISK_RELIEF_WESTINGHOUSE_SETTLEMENT`
- evidence: Westinghouse/KEPCO/KHNP IP dispute settlement removed the largest legal overhang before Czech contract finalization; Doosan had direct reactor-equipment exposure.
- price path: entry 2025-01-20 close 21900; 30D 41.1/-1.37; 90D 120.09/-8.86; 180D 286.76/-8.86.
- stress-test judgment: Stage2-Actionable -> Stage3-Yellow/Green candidate, but staged-entry guard. current_profile_error_type=`too_late_if_wait_final_contract`.
- evidence_url: https://www.world-nuclear-news.org/articles/westinghouse-reaches-agreement-on-ip-with-korean-companies

### C04_165_002 — 052690 한전기술
- evidence_family: `czech_preferred_bidder_without_final_contract`
- fine_archetype_id: `C04_CZECH_PREFERRED_BIDDER_FINAL_CONTRACT_GAP`
- evidence: Preferred bidder headline carried design-contract optionality, but no final contract and unresolved legal risk made early Actionable too aggressive.
- price path: entry 2024-07-18 close 82000; 30D 19.63/-24.88; 90D 19.63/-24.88; 180D 19.63/-39.94.
- stress-test judgment: Stage2-Watch -> local 4B/high-MAE guard. current_profile_error_type=`false_positive_if_preferred_bidder_equals_signed_contract`.
- evidence_url: https://en.yna.co.kr/view/AEN20240716006751320

### C04_165_003 — 051600 한전KPS
- evidence_family: `czech_preferred_bidder_om_service_bridge`
- fine_archetype_id: `C04_CZECH_PREFERRED_BIDDER_OM_SERVICE_VISIBILITY`
- evidence: KEPCO KPS was named in Team Korea; maintenance/O&M and service visibility produced cleaner low-MAE path than design/EPC names.
- price path: entry 2024-07-18 close 38900; 30D 21.98/-7.84; 90D 24.04/-7.84; 180D 26.22/-7.84.
- stress-test judgment: Stage2-Actionable -> Stage3-Yellow with low-MAE service exposure. current_profile_error_type=`current_profile_ok_but_should_prefer_low_mae_service_bridge`.
- evidence_url: https://en.yna.co.kr/view/AEN20240716006751320

### C04_165_004 — 047040 대우건설
- evidence_family: `czech_preferred_bidder_epc_margin_gap`
- fine_archetype_id: `C04_CZECH_EPC_CONSORTIUM_MARGIN_GAP`
- evidence: Daewoo E&C was named in the consortium, but the nuclear headline did not yet create contract share, margin, or working-capital visibility for equity rerating.
- price path: entry 2024-07-18 close 4250; 30D 16.82/-16.59; 90D 16.82/-20.59; 180D 16.82/-30.82.
- stress-test judgment: Stage2-Watch -> 4B/false-positive block. current_profile_error_type=`false_positive_if_consortium_name_without_margin_bridge`.
- evidence_url: https://en.yna.co.kr/view/AEN20240716006751320

### C04_165_005 — 034020 두산에너빌리티
- evidence_family: `czech_uohs_appeal_rejection_temporary_block_not_final`
- fine_archetype_id: `C04_LEGAL_DELAY_FALSE_4C_AUDIT_PROJECT_STILL_ALIVE`
- evidence: Reuters reported both temporary block and next-day rejection/termination of appeals, with CEZ still targeting contract conclusion; legal-delay vocabulary alone should not force hard 4C.
- price path: entry 2024-10-31 close 20050; 30D 13.72/-15.66; 90D 54.11/-15.66; 180D 260.1/-15.66.
- stress-test judgment: legal-delay watch -> false-4C audit -> recovery/Green later. current_profile_error_type=`hard_4c_too_early_on_legal_delay_wording`.
- evidence_url: https://www.reuters.com/business/energy/czech-watchdog-rejects-appeals-nuclear-power-tender-2024-10-31/

### C04_165_006 — 052690 한전기술
- evidence_family: `westinghouse_settlement_design_contract_visibility`
- fine_archetype_id: `C04_CZECH_LEGAL_RISK_RELIEF_DESIGN_VISIBILITY`
- evidence: IP settlement improved design/export legal visibility, but design-engineering beta still had a -22.9% 90D/180D MAE and requires staged entry.
- price path: entry 2025-01-20 close 64600; 30D 17.49/-5.42; 90D 21.98/-22.91; 180D 88.39/-22.91.
- stress-test judgment: Stage2-Actionable -> high-MAE guard -> Stage3-Yellow later. current_profile_error_type=`ok_direction_but_missing_high_mae_entry_guard`.
- evidence_url: https://www.world-nuclear-news.org/articles/westinghouse-reaches-agreement-on-ip-with-korean-companies

### C04_165_007 — 105840 우진
- evidence_family: `11th_basic_plan_domestic_nuclear_instrumentation_proxy`
- fine_archetype_id: `C04_DOMESTIC_NUCLEAR_POLICY_INSTRUMENTATION_ORDER_BRIDGE`
- evidence: 11th power plan confirmed new nuclear/SMR policy; Woojin had prior KHNP ICI contracts and nuclear instrumentation bridge, but policy entry suffered -26% MAE before upside.
- price path: entry 2025-02-21 close 8160; 30D 2.21/-23.77; 90D 62.99/-26.47; 180D 138.36/-26.47.
- stress-test judgment: Stage2-Watch -> high-MAE positive, not immediate Actionable. current_profile_error_type=`too_early_actionable_without_new_order_or_mae_guard`.
- evidence_url: https://www.shinkim.com/eng/media/newsletter/2763

### C04_165_008 — 032820 우리기술
- evidence_family: `11th_basic_plan_mmis_control_system_proxy`
- fine_archetype_id: `C04_DOMESTIC_NUCLEAR_POLICY_MMIS_PROXY_HIGH_MAE`
- evidence: Woori Technology has MMIS/I&C nuclear-system exposure; 11th plan and SMR policy created upside, but without signed project/contract bridge MAE exceeded -32%.
- price path: entry 2025-02-21 close 2140; 30D 3.5/-27.24; 90D 144.86/-32.1; 180D 161.68/-32.1.
- stress-test judgment: Stage2-Watch -> huge MFE but severe drawdown/4B guard. current_profile_error_type=`actionable_needs_signed_contract_or_staged_entry_guard`.
- evidence_url: https://www.wooritg.com/ko/business/system/

### C04_165_009 — 011700 한신기계
- evidence_family: `11th_basic_plan_theme_only_compressor_proxy`
- fine_archetype_id: `C04_DOMESTIC_NUCLEAR_POLICY_THEME_ONLY_COMPRESSOR_PROXY`
- evidence: Hanshin Machinery had nuclear-theme sensitivity but no project share/revenue bridge; 180D close remained negative despite mid-window spike.
- price path: entry 2025-02-21 close 3415; 30D 0.88/-28.99; 90D 53.15/-30.89; 180D 53.15/-30.89.
- stress-test judgment: Stage2 false positive -> local 4B -> reject Green. current_profile_error_type=`theme_only_false_positive`.
- evidence_url: https://www.shinkim.com/eng/media/newsletter/2763

### C04_165_010 — 083650 비에이치아이
- evidence_family: `bhi_smr_bop_supply_chain_execution_bridge`
- fine_archetype_id: `C04_SMR_BOP_SUPPLY_CHAIN_EXECUTION_BRIDGE`
- evidence: KB framed BHI as a Korean nuclear manufacturing/execution bridge with first-system auxiliary equipment capability; price path had >100% 180D MFE with manageable MAE.
- price path: entry 2025-05-20 close 38400; 30D 23.96/-12.89; 90D 54.69/-12.89; 180D 110.42/-12.89.
- stress-test judgment: Stage2-Actionable -> Stage3-Yellow with order/execution bridge. current_profile_error_type=`current_profile_may_underweight_supplier_execution_bridge`.
- evidence_url: https://kbthink.com/securities-view.html?docId=20250507142724950K

## 6. Aggregate result

```json
{
  "row_type": "v12_aggregate_metrics_candidate",
  "round": "R1",
  "loop": 165,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "row_count": 10,
  "unique_case_count": 10,
  "unique_symbol_count": 8,
  "positive_case_count": 7,
  "counterexample_count": 3,
  "stage4b_or_high_mae_count": 6,
  "current_profile_error_count": 9,
  "avg_MFE_30D_pct": 16.13,
  "avg_MAE_30D_pct": -16.46,
  "avg_MFE_90D_pct": 57.24,
  "avg_MAE_90D_pct": -20.31,
  "avg_MFE_180D_pct": 116.15,
  "avg_MAE_180D_pct": -22.84,
  "rule_candidate": "C04_LEGAL_RISK_LAYERING_AND_PROJECT_CONTRACT_CONFIRMATION_GATE_V1"
}
```

## 7. Trigger rows JSONL

```jsonl
{"case_id":"C04_165_001","ticker":"034020","company_name":"두산에너빌리티","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_CZECH_LEGAL_RISK_RELIEF_WESTINGHOUSE_SETTLEMENT","trigger_date":"2025-01-17","trigger_type":"Stage2-Actionable","entry_date":"2025-01-20","entry_price":21900,"entry_market":"KOSPI","MFE_30D_pct":41.1,"MAE_30D_pct":-1.37,"MFE_90D_pct":120.09,"MAE_90D_pct":-8.86,"MFE_180D_pct":286.76,"MAE_180D_pct":-8.86,"close_30D_pct":19.86,"close_90D_pct":116.89,"close_180D_pct":265.3,"D30_end_date":"2025-03-10","D90_end_date":"2025-06-09","D180_end_date":"2025-10-21","peak_180D_date":"2025-10-16","trough_180D_date":"2025-04-09","outcome":"positive","stage_path":"Stage2-Actionable -> Stage3-Yellow/Green candidate, but staged-entry guard","evidence_family":"westinghouse_ip_settlement_czech_legal_risk_relief","evidence_summary":"Westinghouse/KEPCO/KHNP IP dispute settlement removed the largest legal overhang before Czech contract finalization; Doosan had direct reactor-equipment exposure.","evidence_url":"https://www.world-nuclear-news.org/articles/westinghouse-reaches-agreement-on-ip-with-korean-companies","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv","profile_path":"atlas/symbol_profiles/034/034020.json","forward_rows_available":262,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"too_late_if_wait_final_contract","high_mae_guard":false,"local_4b_watch":false,"score_total_shadow":100,"component_scores":{"eps_fcf":21,"visibility":22,"bottleneck":18,"mispricing":15,"valuation":11,"capital_allocation":4,"information_confidence":9}}
{"case_id":"C04_165_002","ticker":"052690","company_name":"한전기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_CZECH_PREFERRED_BIDDER_FINAL_CONTRACT_GAP","trigger_date":"2024-07-17","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_price":82000,"entry_market":"KOSPI","MFE_30D_pct":19.63,"MAE_30D_pct":-24.88,"MFE_90D_pct":19.63,"MAE_90D_pct":-24.88,"MFE_180D_pct":19.63,"MAE_180D_pct":-39.94,"close_30D_pct":-18.17,"close_90D_pct":-17.68,"close_180D_pct":-30.12,"D30_end_date":"2024-08-30","D90_end_date":"2024-12-02","D180_end_date":"2025-04-17","peak_180D_date":"2024-07-18","trough_180D_date":"2024-12-10","outcome":"counterexample","stage_path":"Stage2-Watch -> local 4B/high-MAE guard","evidence_family":"czech_preferred_bidder_without_final_contract","evidence_summary":"Preferred bidder headline carried design-contract optionality, but no final contract and unresolved legal risk made early Actionable too aggressive.","evidence_url":"https://en.yna.co.kr/view/AEN20240716006751320","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","forward_rows_available":384,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"false_positive_if_preferred_bidder_equals_signed_contract","high_mae_guard":true,"local_4b_watch":true,"score_total_shadow":76,"component_scores":{"eps_fcf":14,"visibility":18,"bottleneck":12,"mispricing":10,"valuation":8,"capital_allocation":4,"information_confidence":10}}
{"case_id":"C04_165_003","ticker":"051600","company_name":"한전KPS","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_CZECH_PREFERRED_BIDDER_OM_SERVICE_VISIBILITY","trigger_date":"2024-07-17","trigger_type":"Stage2-Actionable","entry_date":"2024-07-18","entry_price":38900,"entry_market":"KOSPI","MFE_30D_pct":21.98,"MAE_30D_pct":-7.84,"MFE_90D_pct":24.04,"MAE_90D_pct":-7.84,"MFE_180D_pct":26.22,"MAE_180D_pct":-7.84,"close_30D_pct":7.07,"close_90D_pct":22.11,"close_180D_pct":2.44,"D30_end_date":"2024-08-30","D90_end_date":"2024-12-02","D180_end_date":"2025-04-17","peak_180D_date":"2024-12-03","trough_180D_date":"2024-08-05","outcome":"positive","stage_path":"Stage2-Actionable -> Stage3-Yellow with low-MAE service exposure","evidence_family":"czech_preferred_bidder_om_service_bridge","evidence_summary":"KEPCO KPS was named in Team Korea; maintenance/O&M and service visibility produced cleaner low-MAE path than design/EPC names.","evidence_url":"https://en.yna.co.kr/view/AEN20240716006751320","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv","profile_path":"atlas/symbol_profiles/051/051600.json","forward_rows_available":384,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"current_profile_ok_but_should_prefer_low_mae_service_bridge","high_mae_guard":false,"local_4b_watch":false,"score_total_shadow":91,"component_scores":{"eps_fcf":17,"visibility":23,"bottleneck":11,"mispricing":13,"valuation":12,"capital_allocation":5,"information_confidence":10}}
{"case_id":"C04_165_004","ticker":"047040","company_name":"대우건설","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_CZECH_EPC_CONSORTIUM_MARGIN_GAP","trigger_date":"2024-07-17","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_price":4250,"entry_market":"KOSPI","MFE_30D_pct":16.82,"MAE_30D_pct":-16.59,"MFE_90D_pct":16.82,"MAE_90D_pct":-20.59,"MFE_180D_pct":16.82,"MAE_180D_pct":-30.82,"close_30D_pct":-5.18,"close_90D_pct":-14.59,"close_180D_pct":-23.65,"D30_end_date":"2024-08-30","D90_end_date":"2024-12-02","D180_end_date":"2025-04-17","peak_180D_date":"2024-07-18","trough_180D_date":"2025-04-09","outcome":"counterexample","stage_path":"Stage2-Watch -> 4B/false-positive block","evidence_family":"czech_preferred_bidder_epc_margin_gap","evidence_summary":"Daewoo E&C was named in the consortium, but the nuclear headline did not yet create contract share, margin, or working-capital visibility for equity rerating.","evidence_url":"https://en.yna.co.kr/view/AEN20240716006751320","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","forward_rows_available":384,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"false_positive_if_consortium_name_without_margin_bridge","high_mae_guard":true,"local_4b_watch":true,"score_total_shadow":63,"component_scores":{"eps_fcf":10,"visibility":14,"bottleneck":8,"mispricing":9,"valuation":8,"capital_allocation":5,"information_confidence":9}}
{"case_id":"C04_165_005","ticker":"034020","company_name":"두산에너빌리티","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_LEGAL_DELAY_FALSE_4C_AUDIT_PROJECT_STILL_ALIVE","trigger_date":"2024-10-31","trigger_type":"Stage4C-Audit","entry_date":"2024-10-31","entry_price":20050,"entry_market":"KOSPI","MFE_30D_pct":13.72,"MAE_30D_pct":-15.66,"MFE_90D_pct":54.11,"MAE_90D_pct":-15.66,"MFE_180D_pct":260.1,"MAE_180D_pct":-15.66,"close_30D_pct":-11.07,"close_90D_pct":28.68,"close_180D_pct":224.69,"D30_end_date":"2024-12-12","D90_end_date":"2025-03-18","D180_end_date":"2025-07-29","peak_180D_date":"2025-06-30","trough_180D_date":"2024-12-10","outcome":"positive","stage_path":"legal-delay watch -> false-4C audit -> recovery/Green later","evidence_family":"czech_uohs_appeal_rejection_temporary_block_not_final","evidence_summary":"Reuters reported both temporary block and next-day rejection/termination of appeals, with CEZ still targeting contract conclusion; legal-delay vocabulary alone should not force hard 4C.","evidence_url":"https://www.reuters.com/business/energy/czech-watchdog-rejects-appeals-nuclear-power-tender-2024-10-31/","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","forward_rows_available":316,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"hard_4c_too_early_on_legal_delay_wording","high_mae_guard":false,"local_4b_watch":false,"score_total_shadow":102,"component_scores":{"eps_fcf":18,"visibility":20,"bottleneck":18,"mispricing":17,"valuation":13,"capital_allocation":4,"information_confidence":12}}
{"case_id":"C04_165_006","ticker":"052690","company_name":"한전기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_CZECH_LEGAL_RISK_RELIEF_DESIGN_VISIBILITY","trigger_date":"2025-01-17","trigger_type":"Stage2-Actionable","entry_date":"2025-01-20","entry_price":64600,"entry_market":"KOSPI","MFE_30D_pct":17.49,"MAE_30D_pct":-5.42,"MFE_90D_pct":21.98,"MAE_90D_pct":-22.91,"MFE_180D_pct":88.39,"MAE_180D_pct":-22.91,"close_30D_pct":1.39,"close_90D_pct":13.62,"close_180D_pct":64.09,"D30_end_date":"2025-03-10","D90_end_date":"2025-06-09","D180_end_date":"2025-10-21","peak_180D_date":"2025-06-25","trough_180D_date":"2025-04-09","outcome":"positive","stage_path":"Stage2-Actionable -> high-MAE guard -> Stage3-Yellow later","evidence_family":"westinghouse_settlement_design_contract_visibility","evidence_summary":"IP settlement improved design/export legal visibility, but design-engineering beta still had a -22.9% 90D/180D MAE and requires staged entry.","evidence_url":"https://www.world-nuclear-news.org/articles/westinghouse-reaches-agreement-on-ip-with-korean-companies","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv","profile_path":"atlas/symbol_profiles/052/052690.json","forward_rows_available":262,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"ok_direction_but_missing_high_mae_entry_guard","high_mae_guard":true,"local_4b_watch":true,"score_total_shadow":91,"component_scores":{"eps_fcf":16,"visibility":22,"bottleneck":14,"mispricing":13,"valuation":10,"capital_allocation":4,"information_confidence":12}}
{"case_id":"C04_165_007","ticker":"105840","company_name":"우진","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_DOMESTIC_NUCLEAR_POLICY_INSTRUMENTATION_ORDER_BRIDGE","trigger_date":"2025-02-21","trigger_type":"Stage2-Watch","entry_date":"2025-02-21","entry_price":8160,"entry_market":"KOSPI","MFE_30D_pct":2.21,"MAE_30D_pct":-23.77,"MFE_90D_pct":62.99,"MAE_90D_pct":-26.47,"MFE_180D_pct":138.36,"MAE_180D_pct":-26.47,"close_30D_pct":-23.77,"close_90D_pct":23.77,"close_180D_pct":73.9,"D30_end_date":"2025-04-07","D90_end_date":"2025-07-07","D180_end_date":"2025-11-18","peak_180D_date":"2025-10-16","trough_180D_date":"2025-04-09","outcome":"positive","stage_path":"Stage2-Watch -> high-MAE positive, not immediate Actionable","evidence_family":"11th_basic_plan_domestic_nuclear_instrumentation_proxy","evidence_summary":"11th power plan confirmed new nuclear/SMR policy; Woojin had prior KHNP ICI contracts and nuclear instrumentation bridge, but policy entry suffered -26% MAE before upside.","evidence_url":"https://www.shinkim.com/eng/media/newsletter/2763","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/105/105840/2025.csv","profile_path":"atlas/symbol_profiles/105/105840.json","forward_rows_available":209,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"too_early_actionable_without_new_order_or_mae_guard","high_mae_guard":true,"local_4b_watch":true,"score_total_shadow":80,"component_scores":{"eps_fcf":14,"visibility":15,"bottleneck":12,"mispricing":15,"valuation":10,"capital_allocation":4,"information_confidence":10}}
{"case_id":"C04_165_008","ticker":"032820","company_name":"우리기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_DOMESTIC_NUCLEAR_POLICY_MMIS_PROXY_HIGH_MAE","trigger_date":"2025-02-21","trigger_type":"Stage2-Watch","entry_date":"2025-02-21","entry_price":2140,"entry_market":"KOSDAQ","MFE_30D_pct":3.5,"MAE_30D_pct":-27.24,"MFE_90D_pct":144.86,"MAE_90D_pct":-32.1,"MFE_180D_pct":161.68,"MAE_180D_pct":-32.1,"close_30D_pct":-26.87,"close_90D_pct":96.5,"close_180D_pct":78.04,"D30_end_date":"2025-04-07","D90_end_date":"2025-07-07","D180_end_date":"2025-11-18","peak_180D_date":"2025-10-30","trough_180D_date":"2025-04-09","outcome":"positive","stage_path":"Stage2-Watch -> huge MFE but severe drawdown/4B guard","evidence_family":"11th_basic_plan_mmis_control_system_proxy","evidence_summary":"Woori Technology has MMIS/I&C nuclear-system exposure; 11th plan and SMR policy created upside, but without signed project/contract bridge MAE exceeded -32%.","evidence_url":"https://www.wooritg.com/ko/business/system/","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/032/032820/2025.csv","profile_path":"atlas/symbol_profiles/032/032820.json","forward_rows_available":209,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"actionable_needs_signed_contract_or_staged_entry_guard","high_mae_guard":true,"local_4b_watch":true,"score_total_shadow":80,"component_scores":{"eps_fcf":12,"visibility":14,"bottleneck":13,"mispricing":18,"valuation":9,"capital_allocation":4,"information_confidence":10}}
{"case_id":"C04_165_009","ticker":"011700","company_name":"한신기계","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_DOMESTIC_NUCLEAR_POLICY_THEME_ONLY_COMPRESSOR_PROXY","trigger_date":"2025-02-21","trigger_type":"Stage2-FalsePositive","entry_date":"2025-02-21","entry_price":3415,"entry_market":"KOSPI","MFE_30D_pct":0.88,"MAE_30D_pct":-28.99,"MFE_90D_pct":53.15,"MAE_90D_pct":-30.89,"MFE_180D_pct":53.15,"MAE_180D_pct":-30.89,"close_30D_pct":-28.99,"close_90D_pct":10.1,"close_180D_pct":-13.32,"D30_end_date":"2025-04-07","D90_end_date":"2025-07-07","D180_end_date":"2025-11-18","peak_180D_date":"2025-06-19","trough_180D_date":"2025-04-09","outcome":"counterexample","stage_path":"Stage2 false positive -> local 4B -> reject Green","evidence_family":"11th_basic_plan_theme_only_compressor_proxy","evidence_summary":"Hanshin Machinery had nuclear-theme sensitivity but no project share/revenue bridge; 180D close remained negative despite mid-window spike.","evidence_url":"https://www.shinkim.com/eng/media/newsletter/2763","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/011/011700/2025.csv","profile_path":"atlas/symbol_profiles/011/011700.json","forward_rows_available":209,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"theme_only_false_positive","high_mae_guard":true,"local_4b_watch":true,"score_total_shadow":58,"component_scores":{"eps_fcf":8,"visibility":9,"bottleneck":7,"mispricing":15,"valuation":7,"capital_allocation":4,"information_confidence":8}}
{"case_id":"C04_165_010","ticker":"083650","company_name":"비에이치아이","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_SMR_BOP_SUPPLY_CHAIN_EXECUTION_BRIDGE","trigger_date":"2025-05-20","trigger_type":"Stage2-Actionable","entry_date":"2025-05-20","entry_price":38400,"entry_market":"KOSDAQ","MFE_30D_pct":23.96,"MAE_30D_pct":-12.89,"MFE_90D_pct":54.69,"MAE_90D_pct":-12.89,"MFE_180D_pct":110.42,"MAE_180D_pct":-12.89,"close_30D_pct":-0.13,"close_90D_pct":25.39,"close_180D_pct":93.75,"D30_end_date":"2025-07-03","D90_end_date":"2025-09-26","D180_end_date":"2026-02-11","peak_180D_date":"2026-01-29","trough_180D_date":"2025-06-02","outcome":"positive","stage_path":"Stage2-Actionable -> Stage3-Yellow with order/execution bridge","evidence_family":"bhi_smr_bop_supply_chain_execution_bridge","evidence_summary":"KB framed BHI as a Korean nuclear manufacturing/execution bridge with first-system auxiliary equipment capability; price path had >100% 180D MFE with manageable MAE.","evidence_url":"https://kbthink.com/securities-view.html?docId=20250507142724950K","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard":"atlas/ohlcv_tradable_by_symbol_year/083/083650/2025.csv","profile_path":"atlas/symbol_profiles/083/083650.json","forward_rows_available":184,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"calibration_usable_reason":"complete_30_90_180_mfe_mae_and_no_2024_2026_corporate_action_overlap","current_profile_error_type":"current_profile_may_underweight_supplier_execution_bridge","high_mae_guard":false,"local_4b_watch":false,"score_total_shadow":97,"component_scores":{"eps_fcf":18,"visibility":18,"bottleneck":18,"mispricing":16,"valuation":12,"capital_allocation":5,"information_confidence":10}}
```

## 8. Score simulation JSONL

```jsonl
{"row_type":"score_simulation","case_id":"C04_165_001","ticker":"034020","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"eps_fcf":21,"visibility":22,"bottleneck":18,"mispricing":15,"valuation":11,"capital_allocation":4,"information_confidence":9},"shadow_total_score":100,"simulated_stage_without_new_rule":"Stage2-Actionable","simulated_stage_with_C04_gate":"Stage2-Actionable","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_002","ticker":"052690","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-Watch","raw_component_score_breakdown":{"eps_fcf":14,"visibility":18,"bottleneck":12,"mispricing":10,"valuation":8,"capital_allocation":4,"information_confidence":10},"shadow_total_score":76,"simulated_stage_without_new_rule":"Stage2-Actionable","simulated_stage_with_C04_gate":"Stage2-FalsePositive/4B-Watch","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_003","ticker":"051600","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"eps_fcf":17,"visibility":23,"bottleneck":11,"mispricing":13,"valuation":12,"capital_allocation":5,"information_confidence":10},"shadow_total_score":91,"simulated_stage_without_new_rule":"Stage2-Actionable","simulated_stage_with_C04_gate":"Stage2-Actionable","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_004","ticker":"047040","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-Watch","raw_component_score_breakdown":{"eps_fcf":10,"visibility":14,"bottleneck":8,"mispricing":9,"valuation":8,"capital_allocation":5,"information_confidence":9},"shadow_total_score":63,"simulated_stage_without_new_rule":"Stage2-Watch","simulated_stage_with_C04_gate":"Stage2-FalsePositive/4B-Watch","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_005","ticker":"034020","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage4C-Audit","raw_component_score_breakdown":{"eps_fcf":18,"visibility":20,"bottleneck":18,"mispricing":17,"valuation":13,"capital_allocation":4,"information_confidence":12},"shadow_total_score":102,"simulated_stage_without_new_rule":"Stage2-Actionable","simulated_stage_with_C04_gate":"Stage2-Actionable","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_006","ticker":"052690","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"eps_fcf":16,"visibility":22,"bottleneck":14,"mispricing":13,"valuation":10,"capital_allocation":4,"information_confidence":12},"shadow_total_score":91,"simulated_stage_without_new_rule":"Stage2-Actionable","simulated_stage_with_C04_gate":"Stage2-Watch/high-MAE","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_007","ticker":"105840","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-Watch","raw_component_score_breakdown":{"eps_fcf":14,"visibility":15,"bottleneck":12,"mispricing":15,"valuation":10,"capital_allocation":4,"information_confidence":10},"shadow_total_score":80,"simulated_stage_without_new_rule":"Stage2-Actionable","simulated_stage_with_C04_gate":"Stage2-Watch/high-MAE","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_008","ticker":"032820","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-Watch","raw_component_score_breakdown":{"eps_fcf":12,"visibility":14,"bottleneck":13,"mispricing":18,"valuation":9,"capital_allocation":4,"information_confidence":10},"shadow_total_score":80,"simulated_stage_without_new_rule":"Stage2-Actionable","simulated_stage_with_C04_gate":"Stage2-Watch/high-MAE","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_009","ticker":"011700","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-FalsePositive","raw_component_score_breakdown":{"eps_fcf":8,"visibility":9,"bottleneck":7,"mispricing":15,"valuation":7,"capital_allocation":4,"information_confidence":8},"shadow_total_score":58,"simulated_stage_without_new_rule":"Stage2-Watch","simulated_stage_with_C04_gate":"Stage2-FalsePositive/4B-Watch","alignment":"needs_C04_specific_gate"}
{"row_type":"score_simulation","case_id":"C04_165_010","ticker":"083650","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"eps_fcf":18,"visibility":18,"bottleneck":18,"mispricing":16,"valuation":12,"capital_allocation":5,"information_confidence":10},"shadow_total_score":97,"simulated_stage_without_new_rule":"Stage2-Actionable","simulated_stage_with_C04_gate":"Stage2-Actionable","alignment":"needs_C04_specific_gate"}
```

## 9. Narrative-only / blocked row

```jsonl
{"row_type":"narrative_only_audit","ticker":"034020","company_name":"두산에너빌리티","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","trigger_date":"2025-06-05","event":"Czech KHNP final contract signed after court cleared the way","evidence_url":"https://apnews.com/article/czech-nuclear-reactors-edf-khnp-south-korea-3e411cd3693ee4f0c4ecf4fe1d0f799f","calibration_usable":false,"blocked_reason":"insufficient_forward_window_in_stock_web_for_full_180_tradable_rows_by_manifest_max_date_2026-02-20","note":"Useful for next atlas refresh; not used in aggregate metrics here."}
```

## 10. Residual rule candidate

**C04_LEGAL_RISK_LAYERING_AND_PROJECT_CONTRACT_CONFIRMATION_GATE_V1**

C04 should not be treated as one flat nuclear-policy bucket. The gate needs four layers:

1. **Preferred-bidder layer:** allow Stage2-Watch, but do not auto-promote to Actionable unless direct company role, contract share, engineering/O&M/supplier bridge, or low-MAE service exposure is visible.
2. **Legal-delay layer:** temporary court/antitrust delay should create 4B/4C-watch only when project economics or award probability actually breaks. Legal-delay vocabulary alone can be a false hard-4C.
3. **Legal-risk-relief layer:** IP/lawsuit settlement before final contract can be an early Stage2-Actionable event for direct reactor/design names, but high-MAE staged-entry guard remains required.
4. **Domestic policy / SMR layer:** new reactor/SMR policy should remain Stage2-Watch for proxy names unless hard commercial bridge exists: named customer, supply contract, O&M share, BOP/auxiliary equipment capability, or revenue/margin conversion.

Suggested shadow rule:

```text
if canonical_archetype_id == C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY:
    if evidence_layer == preferred_bidder and not direct_company_bridge:
        cap_stage = Stage2-Watch
    if evidence_layer == legal_delay and project_award_probability_not_broken:
        block_hard_4C = true
    if evidence_layer == legal_risk_relief and direct_company_bridge:
        allow_stage2_actionable = true
        require_high_mae_guard = true
    if evidence_layer == domestic_policy_or_smr and not commercial_bridge:
        cap_stage = Stage2-Watch_or_4B-Watch
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute in this research session. Later coding agent should ingest this MD as a standalone v12 research artifact, parse the JSONL trigger rows, validate MFE/MAE fields, dedupe by canonical_archetype_id + ticker + trigger_type + entry_date, and evaluate whether C04_LEGAL_RISK_LAYERING_AND_PROJECT_CONTRACT_CONFIRMATION_GATE_V1 is safe for shadow-to-profile promotion. Production scoring must not be changed unless batch validation across all v12 artifacts approves it.

## 12. Next research state

```text
completed_round = R1
completed_loop = 165
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/thin-P2 clearing
next_recommended_archetypes = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|C15_MATERIAL_SPREAD_SUPERCYCLE|C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
