# E2R v12 Residual Research — R1/L1/C04 Nuclear Supplier Execution vs Policy Proxy High-MAE Gate — Second-Pass Holdout
```yaml
completed_round: "R1"
completed_loop: 202
selected_round: "R1"
selected_loop: 202
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 2 quality-repair after session-aware P0/P1/R13 clearing"
round_schedule_status: "coverage_index_selected_not_sequential"
round_sector_consistency: "pass"
large_sector_id: "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
canonical_archetype_id: "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY"
fine_archetype_id: "C04_SUPPLIER_EXECUTION_VS_POLICY_PROXY_HIGH_MAE_GATE_V2"
price_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_patch_allowed: false
live_candidate_mode: false
auto_trading_allowed: false
output_filename: "e2r_stock_web_v12_residual_round_R1_loop_202_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md"
```

> Execution note: This loop follows the user-visible loop 201 C31 policy/subsidy pass and switches back to a C04 quality-repair holdout. It is not a sequential R1~R13 rotation; the selected canonical archetype drives the round/sector metadata.

## 1. Selection / no-repeat rationale

The static No-Repeat Index lists C04 with 71 representative rows, already above the 50-row floor, so this is a quality-repair pass rather than a shortage-fill pass. Session-local loop 165 already tested the first C04 layer: Czech preferred bidder, legal delay, Westinghouse settlement, 11th Basic Plan, and BHI supplier execution. This loop deliberately avoids reusing the same C04 direct project set as the only evidence spine.

This second pass tests a thinner but important C04 failure mode: **small and mid-cap nuclear suppliers often rerate on the same policy/project headline, but their price paths separate sharply depending on whether the evidence is a true commercial bridge or just nuclear vocabulary.** In lived market terms, the policy headline is the parade; the issuer-specific contract is the cash register. C04 should not mistake the parade for the cash register.

Novelty check:

- new independent case count: 8
- same-archetype new symbol count: 7
- reused symbol with new trigger family: 1 (`083650`, but trigger_date changed from 2025-05-20 in loop165 to 2025-02-12 signed Shin-Hanul BOP contract)
- hard duplicate key repeated: 0
- reused previous C04 direct Czech/settlement rows: 0
- positive/counterexample balance: 4 positive / 4 counterexample

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

Profile/corporate-action check: selected 2024-2025 windows are not marked as corporate-action contaminated for calibration. For `006910` and `042370`, profile candidate dates are historical and outside the entry-to-D180 windows. For `126720`, `130660`, and `457550`, profiles show zero corporate-action candidate dates. Remaining issuers were checked through stock-web active universe/profile paths and local symbol-year tradable shards; no entry-to-D180 corporate-action overlap was detected.

## 3. Evidence spine

- 2024-07-17: Czech Republic selected KHNP as preferred bidder for two new nuclear units. This opened the C04 export-project headline layer, but it did not automatically create issuer-specific orders for every listed nuclear proxy.
- 2025-02-12: BHI announced two KHNP contracts totaling KRW 100.1bn to supply auxiliary equipment for Shin Hanul Units 3 and 4. This is a hard commercial bridge.
- 2025-02-21: Korea finalized the 11th Basic Plan, including two large nuclear units and one SMR by 2038. This is a binding policy layer, but for small suppliers it still needs an O&M, BOP, I&C, radiation-management, or revenue-timing bridge before clean Stage2-Actionable.

## 4. Case table

| case_id | ticker | name | trigger | entry | type | outcome | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | rule lesson |
|---|---:|---|---|---|---|---|---:|---:|---:|---|
| C04_202_001 | 006910 | 보성파워텍 | 2024-07-17 | 2024-07-18 @ 3630 | Stage2-FalsePositive | counterexample | 17.91/-29.48 | 17.91/-29.48 | 17.91/-42.15 | proxy-only nuclear supplier vocabulary needs an issuer-specific order or project-share bridge before Stage2-Actionable. |
| C04_202_002 | 042370 | 비츠로테크 | 2024-07-17 | 2024-07-18 @ 8640 | Stage2-FalsePositive | counterexample | 6.37/-25.58 | 6.37/-25.81 | 6.37/-30.56 | qualification is not the same as signed export work; C04 should require contract ladder confirmation. |
| C04_202_003 | 083650 | 비에이치아이 | 2025-02-12 | 2025-02-12 @ 21950 | Stage2-Actionable | positive | 12.98/-18.95 | 116.86/-30.43 | 182.0/-30.43 | signed BOP contract is Actionable, but C04 nuclear suppliers still need staged-entry sizing when early MAE exceeds 30%. |
| C04_202_004 | 046120 | 오르비텍 | 2025-02-21 | 2025-02-21 @ 2665 | Stage2-Watch | positive | 1.88/-24.2 | 146.53/-25.48 | 146.53/-25.48 | service/proxy exposure can work, but only as Watch/staged entry until a new KHNP contract or run-rate bridge appears. |
| C04_202_005 | 094820 | 일진파워 | 2025-02-21 | 2025-02-21 @ 9350 | Stage2-Watch | positive | 5.67/-19.36 | 47.49/-21.71 | 62.67/-21.71 | maintenance-service exposure deserves Watch/Actionable only when policy becomes recurring maintenance revenue, not just theme beta. |
| C04_202_006 | 126720 | 수산인더스트리 | 2025-02-21 | 2025-02-21 @ 22050 | Stage2-Watch | counterexample | 0.68/-20.82 | 37.64/-22.13 | 37.64/-22.13 | broad plant-service exposure needs a named nuclear O&M/order bridge; otherwise mid-window MFE is 4B, not clean Stage2. |
| C04_202_007 | 130660 | 한전산업 | 2025-02-21 | 2025-02-21 @ 11740 | Stage2-FalsePositive | counterexample | 0.77/-23.34 | 44.72/-25.72 | 44.72/-25.72 | O&M category evidence is not enough; C04 should require KHNP site, contract period, or revenue visibility. |
| C04_202_008 | 457550 | 우진엔텍 | 2025-02-21 | 2025-02-21 @ 20300 | Stage2-Watch | positive | 2.22/-32.02 | 106.9/-33.89 | 106.9/-33.89 | pure-play I&C maintenance can be Watch-positive, but the entry quality is too volatile for instant Stage2-Actionable. |

## 5. Case notes


### C04_202_001 — 006910 보성파워텍
- evidence_family: `czech_preferred_bidder_small_equipment_proxy_without_order_bridge`
- fine_archetype_id: `C04_CZECH_PREFERRED_BIDDER_THEME_PROXY_STRUCTURAL_STEEL`
- evidence: 보성파워텍은 원자력 분야 진출과 원전 관련 기자재/철구조물 이력이 있으나, Czech preferred bidder headline itself did not identify a new order, contract share, delivery schedule, or margin bridge for this issuer.
- price path: entry 2024-07-18 close 3630; 30D 17.91/-29.48; 90D 17.91/-29.48; 180D 17.91/-42.15. D180 end 2025-04-17, peak 2024-07-18, trough 2025-04-04.
- stress-test judgment: Czech preferred-bidder theme proxy -> local 4B -> reject Actionable. current_profile_error_type=`false_positive_if_czech_bidder_headline_maps_to_generic_nuclear_proxy`.
- evidence_url: https://www.bosungpower.co.kr/company/intro.do
- supporting_evidence_url: https://en.yna.co.kr/view/AEN20240716006751320

### C04_202_002 — 042370 비츠로테크
- evidence_family: `czech_preferred_bidder_vitzro_qualified_supplier_no_new_contract`
- fine_archetype_id: `C04_CZECH_PREFERRED_BIDDER_QUALIFIED_SUPPLIER_WITHOUT_NEW_ORDER`
- evidence: 비츠로테크는 한수원 유자격 공급자와 원전용 차단기 납품 자격/이력을 보유하지만, July 2024 Czech headline did not create a new named order or revenue-timing bridge for the listed entity.
- price path: entry 2024-07-18 close 8640; 30D 6.37/-25.58; 90D 6.37/-25.81; 180D 6.37/-30.56. D180 end 2025-04-17, peak 2024-07-18, trough 2024-12-09.
- stress-test judgment: qualified supplier vocabulary -> high-MAE false positive. current_profile_error_type=`supplier_qualification_overweighted_without_commercial_conversion`.
- evidence_url: https://www.electimes.com/news/articleView.html?idxno=302988
- supporting_evidence_url: https://en.yna.co.kr/view/AEN20240716006751320

### C04_202_003 — 083650 비에이치아이
- evidence_family: `bhi_shinhanul_34_auxiliary_equipment_signed_contract`
- fine_archetype_id: `C04_SHINHANUL_BOP_SIGNED_CONTRACT_HIGH_MAE_STAGED_ENTRY`
- evidence: BHI signed two KHNP contracts worth KRW 100.1bn to supply auxiliary equipment for Shin Hanul Units 3 and 4; this is a real commercial bridge, but entry still suffered a deep March/April drawdown before the rerating opened.
- price path: entry 2025-02-12 close 21950; 30D 12.98/-18.95; 90D 116.86/-30.43; 180D 182.0/-30.43. D180 end 2025-11-07, peak 2025-10-13, trough 2025-04-07.
- stress-test judgment: signed domestic nuclear BOP contract -> high-MAE staged positive -> Stage3 later. current_profile_error_type=`good_direction_but_needs_high_mae_staged_entry_guard_even_with_signed_contract`.
- evidence_url: https://www.venturesquare.net/en/988533/
- supporting_evidence_url: https://www.bhi.co.kr/e_menu1_2

### C04_202_004 — 046120 오르비텍
- evidence_family: `11th_basic_plan_orbitech_radiation_management_proxy`
- fine_archetype_id: `C04_DOMESTIC_NUCLEAR_POLICY_RADIATION_MANAGEMENT_HIGH_MAE`
- evidence: 오르비텍 has nuclear plant radiation-management and in-service inspection exposure; the 11th Basic Plan created a strong second-half rerating, but the first 30 trading days were almost pure drawdown.
- price path: entry 2025-02-21 close 2665; 30D 1.88/-24.2; 90D 146.53/-25.48; 180D 146.53/-25.48. D180 end 2025-11-18, peak 2025-06-27, trough 2025-04-09.
- stress-test judgment: 11th Basic Plan -> nuclear radiation-management proxy -> high-MAE positive. current_profile_error_type=`actionable_if_wait_for_project_contract_but_watch_positive_with_high_mae`.
- evidence_url: https://www.orbitech.co.kr/bbs/?category=%EB%B0%A9%EC%82%AC%EC%84%A0%EA%B4%80%EB%A6%AC&so_table=business
- supporting_evidence_url: https://www.reuters.com/business/energy/south-korea-plans-two-new-large-nuclear-reactors-more-renewables-energy-mix-2025-02-21/

### C04_202_005 — 094820 일진파워
- evidence_family: `11th_basic_plan_iljin_power_nuclear_maintenance_bridge`
- fine_archetype_id: `C04_DOMESTIC_NUCLEAR_POLICY_MAINTENANCE_SERVICE_BRIDGE`
- evidence: 일진파워 has power-plant maintenance and nuclear business divisions, plus disclosed overseas nuclear construction/commissioning ambitions; the policy trigger opened upside but not a clean low-MAE entry.
- price path: entry 2025-02-21 close 9350; 30D 5.67/-19.36; 90D 47.49/-21.71; 180D 62.67/-21.71. D180 end 2025-12-26, peak 2025-12-22, trough 2025-04-09.
- stress-test judgment: 11th Basic Plan -> nuclear maintenance/service bridge -> staged positive. current_profile_error_type=`underweight_maintenance_bridge_but_needs_mae_guard`.
- evidence_url: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240814002740&docno=&method=search&viewerhost=
- supporting_evidence_url: https://www.shinkim.com/eng/media/newsletter/2763

### C04_202_006 — 126720 수산인더스트리
- evidence_family: `11th_basic_plan_soosan_industries_broad_plant_service`
- fine_archetype_id: `C04_DOMESTIC_NUCLEAR_POLICY_BROAD_PLANT_SERVICE_LOW_DURABILITY`
- evidence: 수산인더스트리 lists nuclear among its plant-service domains, but the policy event did not show a new nuclear project share, O&M contract, or earnings bridge; 180D close was negative despite a mid-window MFE.
- price path: entry 2025-02-21 close 22050; 30D 0.68/-20.82; 90D 37.64/-22.13; 180D 37.64/-22.13. D180 end 2025-11-18, peak 2025-06-20, trough 2025-04-09.
- stress-test judgment: 11th Basic Plan -> plant-service broad exposure -> spike but no durable close. current_profile_error_type=`false_positive_if_broad_plant_service_maps_to_nuclear_policy_actionable`.
- evidence_url: https://www.soosanind.co.kr/
- supporting_evidence_url: https://www.shinkim.com/eng/media/newsletter/2763

### C04_202_007 — 130660 한전산업
- evidence_family: `11th_basic_plan_kepid_nuclear_om_proxy`
- fine_archetype_id: `C04_DOMESTIC_NUCLEAR_POLICY_OM_PROXY_LOW_FOLLOWTHROUGH`
- evidence: 한전산업 has nuclear O&M business exposure, but the 11th-plan policy announcement did not identify a company-level contract or margin bridge; 180D close stayed negative after a temporary spike.
- price path: entry 2025-02-21 close 11740; 30D 0.77/-23.34; 90D 44.72/-25.72; 180D 44.72/-25.72. D180 end 2025-11-18, peak 2025-06-25, trough 2025-04-09.
- stress-test judgment: 11th Basic Plan -> O&M proxy -> high-MAE low follow-through. current_profile_error_type=`o_m_proxy_false_positive_without_company_specific_contract`.
- evidence_url: https://www.kepid.co.kr/kepid/business/powerstation02.asp
- supporting_evidence_url: https://www.reuters.com/business/energy/south-korea-plans-two-new-large-nuclear-reactors-more-renewables-energy-mix-2025-02-21/

### C04_202_008 — 457550 우진엔텍
- evidence_family: `11th_basic_plan_woojin_entech_ic_maintenance_proxy`
- fine_archetype_id: `C04_DOMESTIC_NUCLEAR_POLICY_IC_MAINTENANCE_PUREPLAY_HIGH_MAE`
- evidence: 우진엔텍 has KHNP-qualified nuclear I&C maintenance credentials; the policy event eventually produced large upside, but the first 30/90D drawdown makes immediate Actionable unsafe.
- price path: entry 2025-02-21 close 20300; 30D 2.22/-32.02; 90D 106.9/-33.89; 180D 106.9/-33.89. D180 end 2025-11-18, peak 2025-06-27, trough 2025-04-09.
- stress-test judgment: 11th Basic Plan -> nuclear I&C maintenance pure-play -> very high-MAE positive. current_profile_error_type=`good_pureplay_but_requires_staged_entry_high_mae_guard`.
- evidence_url: https://woojinntec.com/company/history.php
- supporting_evidence_url: https://www.shinkim.com/eng/media/newsletter/2763


## 6. Trigger rows JSONL

```jsonl
{"case_id": "C04_202_001", "ticker": "006910", "company_name": "보성파워텍", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "C04_CZECH_PREFERRED_BIDDER_THEME_PROXY_STRUCTURAL_STEEL", "trigger_date": "2024-07-17", "trigger_type": "Stage2-FalsePositive", "entry_date": "2024-07-18", "entry_price": 3630.0, "entry_market": "KOSDAQ", "MFE_30D_pct": 17.91, "MAE_30D_pct": -29.48, "MFE_90D_pct": 17.91, "MAE_90D_pct": -29.48, "MFE_180D_pct": 17.91, "MAE_180D_pct": -42.15, "close_30D_pct": -18.73, "close_90D_pct": -21.9, "close_180D_pct": -24.24, "D30_end_date": "2024-08-30", "D90_end_date": "2024-12-02", "D180_end_date": "2025-04-17", "peak_180D_date": "2024-07-18", "trough_180D_date": "2025-04-04", "outcome": "counterexample", "stage_path": "Czech preferred-bidder theme proxy -> local 4B -> reject Actionable", "evidence_family": "czech_preferred_bidder_small_equipment_proxy_without_order_bridge", "evidence_summary": "보성파워텍은 원자력 분야 진출과 원전 관련 기자재/철구조물 이력이 있으나, Czech preferred bidder headline itself did not identify a new order, contract share, delivery schedule, or margin bridge for this issuer.", "evidence_url": "https://www.bosungpower.co.kr/company/intro.do", "supporting_evidence_url": "https://en.yna.co.kr/view/AEN20240716006751320", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv", "profile_path": "atlas/symbol_profiles/006/006910.json", "forward_rows_available": 384, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_and_no_entry_to_D180_corporate_action_overlap_detected_in_profile_check", "current_profile_error_type": "false_positive_if_czech_bidder_headline_maps_to_generic_nuclear_proxy", "high_mae_guard": true, "local_4b_watch": true, "score_total_shadow": 58, "component_scores": {"eps_fcf": 8, "visibility": 9, "bottleneck": 8, "mispricing": 14, "valuation": 8, "capital_allocation": 4, "information_confidence": 7}}
{"case_id": "C04_202_002", "ticker": "042370", "company_name": "비츠로테크", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "C04_CZECH_PREFERRED_BIDDER_QUALIFIED_SUPPLIER_WITHOUT_NEW_ORDER", "trigger_date": "2024-07-17", "trigger_type": "Stage2-FalsePositive", "entry_date": "2024-07-18", "entry_price": 8640.0, "entry_market": "KOSDAQ", "MFE_30D_pct": 6.37, "MAE_30D_pct": -25.58, "MFE_90D_pct": 6.37, "MAE_90D_pct": -25.81, "MFE_180D_pct": 6.37, "MAE_180D_pct": -30.56, "close_30D_pct": -15.62, "close_90D_pct": -19.56, "close_180D_pct": -11.81, "D30_end_date": "2024-08-30", "D90_end_date": "2024-12-02", "D180_end_date": "2025-04-17", "peak_180D_date": "2024-07-18", "trough_180D_date": "2024-12-09", "outcome": "counterexample", "stage_path": "qualified supplier vocabulary -> high-MAE false positive", "evidence_family": "czech_preferred_bidder_vitzro_qualified_supplier_no_new_contract", "evidence_summary": "비츠로테크는 한수원 유자격 공급자와 원전용 차단기 납품 자격/이력을 보유하지만, July 2024 Czech headline did not create a new named order or revenue-timing bridge for the listed entity.", "evidence_url": "https://www.electimes.com/news/articleView.html?idxno=302988", "supporting_evidence_url": "https://en.yna.co.kr/view/AEN20240716006751320", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/042/042370/2024.csv", "profile_path": "atlas/symbol_profiles/042/042370.json", "forward_rows_available": 351, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_and_no_entry_to_D180_corporate_action_overlap_detected_in_profile_check", "current_profile_error_type": "supplier_qualification_overweighted_without_commercial_conversion", "high_mae_guard": true, "local_4b_watch": true, "score_total_shadow": 61, "component_scores": {"eps_fcf": 8, "visibility": 12, "bottleneck": 9, "mispricing": 13, "valuation": 8, "capital_allocation": 4, "information_confidence": 7}}
{"case_id": "C04_202_003", "ticker": "083650", "company_name": "비에이치아이", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "C04_SHINHANUL_BOP_SIGNED_CONTRACT_HIGH_MAE_STAGED_ENTRY", "trigger_date": "2025-02-12", "trigger_type": "Stage2-Actionable", "entry_date": "2025-02-12", "entry_price": 21950.0, "entry_market": "KOSDAQ", "MFE_30D_pct": 12.98, "MAE_30D_pct": -18.95, "MFE_90D_pct": 116.86, "MAE_90D_pct": -30.43, "MFE_180D_pct": 182.0, "MAE_180D_pct": -30.43, "close_30D_pct": -18.0, "close_90D_pct": 90.66, "close_180D_pct": 89.07, "D30_end_date": "2025-03-27", "D90_end_date": "2025-06-26", "D180_end_date": "2025-11-07", "peak_180D_date": "2025-10-13", "trough_180D_date": "2025-04-07", "outcome": "positive", "stage_path": "signed domestic nuclear BOP contract -> high-MAE staged positive -> Stage3 later", "evidence_family": "bhi_shinhanul_34_auxiliary_equipment_signed_contract", "evidence_summary": "BHI signed two KHNP contracts worth KRW 100.1bn to supply auxiliary equipment for Shin Hanul Units 3 and 4; this is a real commercial bridge, but entry still suffered a deep March/April drawdown before the rerating opened.", "evidence_url": "https://www.venturesquare.net/en/988533/", "supporting_evidence_url": "https://www.bhi.co.kr/e_menu1_2", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/083/083650/2025.csv", "profile_path": "atlas/symbol_profiles/083/083650.json", "forward_rows_available": 216, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_and_no_entry_to_D180_corporate_action_overlap_detected_in_profile_check", "current_profile_error_type": "good_direction_but_needs_high_mae_staged_entry_guard_even_with_signed_contract", "high_mae_guard": true, "local_4b_watch": true, "score_total_shadow": 93, "component_scores": {"eps_fcf": 17, "visibility": 20, "bottleneck": 18, "mispricing": 15, "valuation": 10, "capital_allocation": 4, "information_confidence": 9}}
{"case_id": "C04_202_004", "ticker": "046120", "company_name": "오르비텍", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "C04_DOMESTIC_NUCLEAR_POLICY_RADIATION_MANAGEMENT_HIGH_MAE", "trigger_date": "2025-02-21", "trigger_type": "Stage2-Watch", "entry_date": "2025-02-21", "entry_price": 2665.0, "entry_market": "KOSDAQ", "MFE_30D_pct": 1.88, "MAE_30D_pct": -24.2, "MFE_90D_pct": 146.53, "MAE_90D_pct": -25.48, "MFE_180D_pct": 146.53, "MAE_180D_pct": -25.48, "close_30D_pct": -23.64, "close_90D_pct": 55.72, "close_180D_pct": 45.59, "D30_end_date": "2025-04-07", "D90_end_date": "2025-07-07", "D180_end_date": "2025-11-18", "peak_180D_date": "2025-06-27", "trough_180D_date": "2025-04-09", "outcome": "positive", "stage_path": "11th Basic Plan -> nuclear radiation-management proxy -> high-MAE positive", "evidence_family": "11th_basic_plan_orbitech_radiation_management_proxy", "evidence_summary": "오르비텍 has nuclear plant radiation-management and in-service inspection exposure; the 11th Basic Plan created a strong second-half rerating, but the first 30 trading days were almost pure drawdown.", "evidence_url": "https://www.orbitech.co.kr/bbs/?category=%EB%B0%A9%EC%82%AC%EC%84%A0%EA%B4%80%EB%A6%AC&so_table=business", "supporting_evidence_url": "https://www.reuters.com/business/energy/south-korea-plans-two-new-large-nuclear-reactors-more-renewables-energy-mix-2025-02-21/", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2025.csv", "profile_path": "atlas/symbol_profiles/046/046120.json", "forward_rows_available": 209, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_and_no_entry_to_D180_corporate_action_overlap_detected_in_profile_check", "current_profile_error_type": "actionable_if_wait_for_project_contract_but_watch_positive_with_high_mae", "high_mae_guard": true, "local_4b_watch": true, "score_total_shadow": 79, "component_scores": {"eps_fcf": 11, "visibility": 15, "bottleneck": 13, "mispricing": 17, "valuation": 9, "capital_allocation": 4, "information_confidence": 10}}
{"case_id": "C04_202_005", "ticker": "094820", "company_name": "일진파워", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "C04_DOMESTIC_NUCLEAR_POLICY_MAINTENANCE_SERVICE_BRIDGE", "trigger_date": "2025-02-21", "trigger_type": "Stage2-Watch", "entry_date": "2025-02-21", "entry_price": 9350.0, "entry_market": "KOSDAQ", "MFE_30D_pct": 5.67, "MAE_30D_pct": -19.36, "MFE_90D_pct": 47.49, "MAE_90D_pct": -21.71, "MFE_180D_pct": 62.67, "MAE_180D_pct": -21.71, "close_30D_pct": -18.82, "close_90D_pct": 11.02, "close_180D_pct": 37.22, "D30_end_date": "2025-04-07", "D90_end_date": "2025-08-13", "D180_end_date": "2025-12-26", "peak_180D_date": "2025-12-22", "trough_180D_date": "2025-04-09", "outcome": "positive", "stage_path": "11th Basic Plan -> nuclear maintenance/service bridge -> staged positive", "evidence_family": "11th_basic_plan_iljin_power_nuclear_maintenance_bridge", "evidence_summary": "일진파워 has power-plant maintenance and nuclear business divisions, plus disclosed overseas nuclear construction/commissioning ambitions; the policy trigger opened upside but not a clean low-MAE entry.", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240814002740&docno=&method=search&viewerhost=", "supporting_evidence_url": "https://www.shinkim.com/eng/media/newsletter/2763", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2025.csv", "profile_path": "atlas/symbol_profiles/094/094820.json", "forward_rows_available": 182, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_and_no_entry_to_D180_corporate_action_overlap_detected_in_profile_check", "current_profile_error_type": "underweight_maintenance_bridge_but_needs_mae_guard", "high_mae_guard": true, "local_4b_watch": true, "score_total_shadow": 82, "component_scores": {"eps_fcf": 13, "visibility": 17, "bottleneck": 12, "mispricing": 16, "valuation": 11, "capital_allocation": 4, "information_confidence": 9}}
{"case_id": "C04_202_006", "ticker": "126720", "company_name": "수산인더스트리", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "C04_DOMESTIC_NUCLEAR_POLICY_BROAD_PLANT_SERVICE_LOW_DURABILITY", "trigger_date": "2025-02-21", "trigger_type": "Stage2-Watch", "entry_date": "2025-02-21", "entry_price": 22050.0, "entry_market": "KOSPI", "MFE_30D_pct": 0.68, "MAE_30D_pct": -20.82, "MFE_90D_pct": 37.64, "MAE_90D_pct": -22.13, "MFE_180D_pct": 37.64, "MAE_180D_pct": -22.13, "close_30D_pct": -20.77, "close_90D_pct": 12.02, "close_180D_pct": -9.07, "D30_end_date": "2025-04-07", "D90_end_date": "2025-07-07", "D180_end_date": "2025-11-18", "peak_180D_date": "2025-06-20", "trough_180D_date": "2025-04-09", "outcome": "counterexample", "stage_path": "11th Basic Plan -> plant-service broad exposure -> spike but no durable close", "evidence_family": "11th_basic_plan_soosan_industries_broad_plant_service", "evidence_summary": "수산인더스트리 lists nuclear among its plant-service domains, but the policy event did not show a new nuclear project share, O&M contract, or earnings bridge; 180D close was negative despite a mid-window MFE.", "evidence_url": "https://www.soosanind.co.kr/", "supporting_evidence_url": "https://www.shinkim.com/eng/media/newsletter/2763", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/126/126720/2025.csv", "profile_path": "atlas/symbol_profiles/126/126720.json", "forward_rows_available": 242, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_and_no_entry_to_D180_corporate_action_overlap_detected_in_profile_check", "current_profile_error_type": "false_positive_if_broad_plant_service_maps_to_nuclear_policy_actionable", "high_mae_guard": true, "local_4b_watch": true, "score_total_shadow": 64, "component_scores": {"eps_fcf": 9, "visibility": 11, "bottleneck": 8, "mispricing": 15, "valuation": 9, "capital_allocation": 4, "information_confidence": 8}}
{"case_id": "C04_202_007", "ticker": "130660", "company_name": "한전산업", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "C04_DOMESTIC_NUCLEAR_POLICY_OM_PROXY_LOW_FOLLOWTHROUGH", "trigger_date": "2025-02-21", "trigger_type": "Stage2-FalsePositive", "entry_date": "2025-02-21", "entry_price": 11740.0, "entry_market": "KOSPI", "MFE_30D_pct": 0.77, "MAE_30D_pct": -23.34, "MFE_90D_pct": 44.72, "MAE_90D_pct": -25.72, "MFE_180D_pct": 44.72, "MAE_180D_pct": -25.72, "close_30D_pct": -23.34, "close_90D_pct": 12.78, "close_180D_pct": -3.24, "D30_end_date": "2025-04-07", "D90_end_date": "2025-07-07", "D180_end_date": "2025-11-18", "peak_180D_date": "2025-06-25", "trough_180D_date": "2025-04-09", "outcome": "counterexample", "stage_path": "11th Basic Plan -> O&M proxy -> high-MAE low follow-through", "evidence_family": "11th_basic_plan_kepid_nuclear_om_proxy", "evidence_summary": "한전산업 has nuclear O&M business exposure, but the 11th-plan policy announcement did not identify a company-level contract or margin bridge; 180D close stayed negative after a temporary spike.", "evidence_url": "https://www.kepid.co.kr/kepid/business/powerstation02.asp", "supporting_evidence_url": "https://www.reuters.com/business/energy/south-korea-plans-two-new-large-nuclear-reactors-more-renewables-energy-mix-2025-02-21/", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/130/130660/2025.csv", "profile_path": "atlas/symbol_profiles/130/130660.json", "forward_rows_available": 209, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_and_no_entry_to_D180_corporate_action_overlap_detected_in_profile_check", "current_profile_error_type": "o_m_proxy_false_positive_without_company_specific_contract", "high_mae_guard": true, "local_4b_watch": true, "score_total_shadow": 63, "component_scores": {"eps_fcf": 9, "visibility": 12, "bottleneck": 8, "mispricing": 15, "valuation": 8, "capital_allocation": 4, "information_confidence": 7}}
{"case_id": "C04_202_008", "ticker": "457550", "company_name": "우진엔텍", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "C04_DOMESTIC_NUCLEAR_POLICY_IC_MAINTENANCE_PUREPLAY_HIGH_MAE", "trigger_date": "2025-02-21", "trigger_type": "Stage2-Watch", "entry_date": "2025-02-21", "entry_price": 20300.0, "entry_market": "KOSDAQ", "MFE_30D_pct": 2.22, "MAE_30D_pct": -32.02, "MFE_90D_pct": 106.9, "MAE_90D_pct": -33.89, "MFE_180D_pct": 106.9, "MAE_180D_pct": -33.89, "close_30D_pct": -31.53, "close_90D_pct": 38.92, "close_180D_pct": 1.48, "D30_end_date": "2025-04-07", "D90_end_date": "2025-07-07", "D180_end_date": "2025-11-18", "peak_180D_date": "2025-06-27", "trough_180D_date": "2025-04-09", "outcome": "positive", "stage_path": "11th Basic Plan -> nuclear I&C maintenance pure-play -> very high-MAE positive", "evidence_family": "11th_basic_plan_woojin_entech_ic_maintenance_proxy", "evidence_summary": "우진엔텍 has KHNP-qualified nuclear I&C maintenance credentials; the policy event eventually produced large upside, but the first 30/90D drawdown makes immediate Actionable unsafe.", "evidence_url": "https://woojinntec.com/company/history.php", "supporting_evidence_url": "https://www.shinkim.com/eng/media/newsletter/2763", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/457/457550/2025.csv", "profile_path": "atlas/symbol_profiles/457/457550.json", "forward_rows_available": 242, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_and_no_entry_to_D180_corporate_action_overlap_detected_in_profile_check", "current_profile_error_type": "good_pureplay_but_requires_staged_entry_high_mae_guard", "high_mae_guard": true, "local_4b_watch": true, "score_total_shadow": 81, "component_scores": {"eps_fcf": 12, "visibility": 16, "bottleneck": 14, "mispricing": 18, "valuation": 9, "capital_allocation": 4, "information_confidence": 8}}
```

## 7. Score simulation JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C04_202_001", "ticker": "006910", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "trigger_type": "Stage2-FalsePositive", "raw_component_score_breakdown": {"eps_fcf": 8, "visibility": 9, "bottleneck": 8, "mispricing": 14, "valuation": 8, "capital_allocation": 4, "information_confidence": 7}, "shadow_total_score": 58, "simulated_stage_without_new_rule": "Stage2-Watch", "simulated_stage_with_C04_gate": "Stage2-FalsePositive/4B-Watch", "alignment": "needs_C04_supplier_proxy_gate_v2"}
{"row_type": "score_simulation", "case_id": "C04_202_002", "ticker": "042370", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "trigger_type": "Stage2-FalsePositive", "raw_component_score_breakdown": {"eps_fcf": 8, "visibility": 12, "bottleneck": 9, "mispricing": 13, "valuation": 8, "capital_allocation": 4, "information_confidence": 7}, "shadow_total_score": 61, "simulated_stage_without_new_rule": "Stage2-Watch", "simulated_stage_with_C04_gate": "Stage2-FalsePositive/4B-Watch", "alignment": "needs_C04_supplier_proxy_gate_v2"}
{"row_type": "score_simulation", "case_id": "C04_202_003", "ticker": "083650", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "trigger_type": "Stage2-Actionable", "raw_component_score_breakdown": {"eps_fcf": 17, "visibility": 20, "bottleneck": 18, "mispricing": 15, "valuation": 10, "capital_allocation": 4, "information_confidence": 9}, "shadow_total_score": 93, "simulated_stage_without_new_rule": "Stage2-Actionable", "simulated_stage_with_C04_gate": "Stage2-Watch/4B-Guard", "alignment": "needs_C04_supplier_proxy_gate_v2"}
{"row_type": "score_simulation", "case_id": "C04_202_004", "ticker": "046120", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "trigger_type": "Stage2-Watch", "raw_component_score_breakdown": {"eps_fcf": 11, "visibility": 15, "bottleneck": 13, "mispricing": 17, "valuation": 9, "capital_allocation": 4, "information_confidence": 10}, "shadow_total_score": 79, "simulated_stage_without_new_rule": "Stage2-Actionable", "simulated_stage_with_C04_gate": "Stage2-Watch/4B-Guard", "alignment": "needs_C04_supplier_proxy_gate_v2"}
{"row_type": "score_simulation", "case_id": "C04_202_005", "ticker": "094820", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "trigger_type": "Stage2-Watch", "raw_component_score_breakdown": {"eps_fcf": 13, "visibility": 17, "bottleneck": 12, "mispricing": 16, "valuation": 11, "capital_allocation": 4, "information_confidence": 9}, "shadow_total_score": 82, "simulated_stage_without_new_rule": "Stage2-Actionable", "simulated_stage_with_C04_gate": "Stage2-Watch/4B-Guard", "alignment": "needs_C04_supplier_proxy_gate_v2"}
{"row_type": "score_simulation", "case_id": "C04_202_006", "ticker": "126720", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "trigger_type": "Stage2-Watch", "raw_component_score_breakdown": {"eps_fcf": 9, "visibility": 11, "bottleneck": 8, "mispricing": 15, "valuation": 9, "capital_allocation": 4, "information_confidence": 8}, "shadow_total_score": 64, "simulated_stage_without_new_rule": "Stage2-Watch", "simulated_stage_with_C04_gate": "Stage2-FalsePositive/4B-Watch", "alignment": "needs_C04_supplier_proxy_gate_v2"}
{"row_type": "score_simulation", "case_id": "C04_202_007", "ticker": "130660", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "trigger_type": "Stage2-FalsePositive", "raw_component_score_breakdown": {"eps_fcf": 9, "visibility": 12, "bottleneck": 8, "mispricing": 15, "valuation": 8, "capital_allocation": 4, "information_confidence": 7}, "shadow_total_score": 63, "simulated_stage_without_new_rule": "Stage2-Watch", "simulated_stage_with_C04_gate": "Stage2-FalsePositive/4B-Watch", "alignment": "needs_C04_supplier_proxy_gate_v2"}
{"row_type": "score_simulation", "case_id": "C04_202_008", "ticker": "457550", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "trigger_type": "Stage2-Watch", "raw_component_score_breakdown": {"eps_fcf": 12, "visibility": 16, "bottleneck": 14, "mispricing": 18, "valuation": 9, "capital_allocation": 4, "information_confidence": 8}, "shadow_total_score": 81, "simulated_stage_without_new_rule": "Stage2-Actionable", "simulated_stage_with_C04_gate": "Stage2-Watch/4B-Guard", "alignment": "needs_C04_supplier_proxy_gate_v2"}
```

## 8. Aggregate / shadow rule rows JSONL

```jsonl
{"row_type": "aggregate_summary", "selected_round": "R1", "selected_loop": 202, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "new_independent_case_count": 8, "reused_symbol_new_trigger_count": 1, "same_archetype_new_symbol_count": 7, "same_archetype_new_trigger_family_count": 8, "calibration_usable_case_count": 8, "calibration_usable_trigger_count": 8, "positive_case_count": 4, "counterexample_count": 4, "stage4b_watch_or_overlay_count": 8, "stage4c_or_false4c_audit_count": 0, "current_profile_error_count": 7, "coverage_before_index_baseline": "C04 rows 71", "coverage_after_if_accepted_index_baseline": "C04 rows 79", "session_aware_after_loop165_loop202_if_accepted": "about C04 rows 89", "new_axis_proposed": "c04_supplier_execution_vs_policy_proxy_high_mae_gate_v2"}
{"row_type": "shadow_weight_candidate", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "rule_id": "C04_SUPPLIER_EXECUTION_VS_POLICY_PROXY_HIGH_MAE_GATE_V2", "production_scoring_changed": false, "shadow_weight_only": true, "do_not_propose_new_weight_delta": false, "intended_effect": "Require issuer-specific commercial bridge for C04 policy/proxy names; allow Actionable for signed nuclear BOP/O&M contracts but add high-MAE staged-entry guard.", "positive_condition": "direct named nuclear project/contract/O&M/BOP/I&C service bridge plus revenue timing or recurring service visibility", "downgrade_condition": "generic nuclear policy, qualified supplier status, product category, or broad plant-service exposure without company-level order/margin/revenue bridge", "mae_guard_condition": "if MAE90 <= -25 and MFE180 remains high, use Stage2-Watch/staged-entry rather than clean Stage2-Actionable"}
```

## 9. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c04_supplier_execution_vs_policy_proxy_high_mae_gate_v2
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c_should_not_fire_on_policy_or_legal_words_alone
existing_axis_weakened = none
do_not_propose_new_weight_delta = false
production_scoring_changed = false
shadow_weight_only = true
```

### Proposed C04 rule candidate

`C04_SUPPLIER_EXECUTION_VS_POLICY_PROXY_HIGH_MAE_GATE_V2`

C04 should treat nuclear policy and project headlines as layered gates:

1. **Project/policy layer**: preferred bidder, 11th Basic Plan, SMR policy, legal-delay relief. This can create Stage2-Watch, but not clean Actionable for every proxy.
2. **Issuer bridge layer**: named KHNP/Team Korea contract, BOP package, O&M service period, I&C/radiation-management service contract, or clearly attributable revenue timing. This can unlock Stage2-Actionable.
3. **Entry-quality layer**: even hard-bridge suppliers can show severe MAE before rerating. If `MAE90 <= -25` but `MFE180 >= 50`, do not call the thesis false; tag as staged-entry/high-MAE guard.
4. **Proxy block layer**: product category, qualified-supplier status, broad plant-service exposure, or nuclear vocabulary without new commercial conversion should remain Stage2-Watch / Stage2-FalsePositive / local 4B, especially when 180D close is negative.

Mechanically, this is a transformer-substation rule for nuclear evidence. The policy current enters the system, but only names with a transformer — contract, service period, or revenue bridge — should receive usable voltage. Product-category proxies are wires lying near the substation, not power-delivery evidence.

## 10. Validation scope

```text
validation_scope = historical_trigger_level_residual_research
stock_web_price_atlas_access_required = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = satisfied
must_deduplicate_same_entry_triggers_for_aggregate = satisfied
minimum_new_symbol_count = satisfied
minimum_positive_case_count = satisfied
minimum_counterexample_count = satisfied
```

## 11. Narrative-only / blocked rows

```jsonl
{"row_type":"narrative_only_audit","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","event_date":"2025-06-04","event":"Czech final contract signing","reason":"manifest max_date 2026-02-20 leaves insufficient complete D+180 trading-window safety margin for a strict new trigger; useful for narrative but not this loop's calibration row","evidence_url":"https://en.yna.co.kr/view/AEN20250604012653315","calibration_usable":false}
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Later coding-agent task:
1. Ingest this MD as a standard v12 research result.
2. Parse all trigger rows under `Trigger rows JSONL`.
3. Validate required fields: ticker, trigger_type, entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct, large_sector_id, canonical_archetype_id.
4. Deduplicate by canonical_archetype_id + ticker + trigger_type + entry_date.
5. If accepted, add this candidate to C04 scope only:
   rule_id = C04_SUPPLIER_EXECUTION_VS_POLICY_PROXY_HIGH_MAE_GATE_V2
   target = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
   effect = require issuer-specific commercial bridge for C04 supplier/proxy Stage2-Actionable; downgrade generic policy/product proxies; add high-MAE staged-entry guard for signed contracts and pure-play services.
6. Do not loosen Stage3-Green global thresholds.
7. Do not apply this rule outside C04 without a separate R13 or sector-specific validation pass.
```

## 13. Next research state

```text
completed_round = R1
completed_loop = 202
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes = C31_POLICY_SUBSIDY_LEGISLATION_EVENT|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
