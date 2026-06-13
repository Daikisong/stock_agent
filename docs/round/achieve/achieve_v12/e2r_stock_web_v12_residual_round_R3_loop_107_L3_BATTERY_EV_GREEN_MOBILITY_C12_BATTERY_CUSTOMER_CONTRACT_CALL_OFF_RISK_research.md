# E2R Stock-Web V12 Residual Research — C12 Customer Contract / Call-off Risk Seventh Holdout

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R3_loop_107_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round: R3
selected_loop: 107
selection_basis: docs/core/V12_Research_No_Repeat_Index.md used as no-repeat ledger only
selected_priority_bucket: Priority 1 static ledger C12 rows=32 / need-to-50=18; current-session C12 already heavily strengthened, so this loop is a new-symbol quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: mixed_C12_component_inspection_contract_calloff_holdout_v107
loop_objective:
  - holdout_validation
  - counterexample_mining
  - customer_contract_delivery_gate
  - calloff_and_revenue_recognition_gate
  - non_c12_theme_contamination_deconfliction
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

The static no-repeat ledger still marks `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` as a Priority 1 archetype with `32` rows and `18` additional rows needed to reach the 50-row practical calibration band. This run therefore stays in R3/L3 but avoids the previously used C12 equipment core set by using a component / inspection-system / customer-contract boundary sample:

```text
251630 브이원텍
333620 엔시스
419050 삼기에너지솔루션즈
416180 신성에스티
396300 세아메카닉스
065350 신성델타테크
```

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No row in this file repeats the visible prior C12 core equipment set such as `222080`, `137400`, `299030`, `277880`, `382840`, `079810`, `262260`, `267320`, `372170`, `378340`, `083930`, `282880`, `217820`, `290670`, `382480`, `003670`, `247540`, `066970`, `051910`, `393890`, or `361610`.

## 2. Price atlas validation

Stock-Web manifest basis:

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
calibration_basis: tradable_raw
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
```

The MFE/MAE fields below use the Stock-Web schema convention:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Profile-level contamination check:

```yaml
251630: corporate_action_candidate_dates=[2019-06-04, 2019-06-25], no overlap with 2023-01-25~180D
333620: corporate_action_candidate_dates=[], clean 180D window
419050: corporate_action_candidate_dates=[2023-08-31, 2023-09-22], no overlap with 2024-12-05~180D
416180: corporate_action_candidate_dates=[], clean 180D window
396300: corporate_action_candidate_dates=[], clean 180D window
065350: corporate_action_candidate_dates=[2006-01-03, 2011-05-26], no overlap with 2023-04-28~180D
```

## 3. Core finding

C12 should not treat every battery customer, component supply, or inspection-equipment contract as a clean Stage3 rerating. The mechanism has four doors:

```text
named customer / contract headline
→ delivery timing
→ revenue recognition
→ margin / cash conversion
```

Rows that passed more of these doors, such as `251630` and `419050`, produced useful MFE. Rows where the contract was real but conversion timing, component dependency, or customer call-off risk was unresolved, such as `416180` and `396300`, suffered deep 90D/180D MAE. `065350` is a separate decontamination warning: the company has LGES battery-parts evidence, but the later extreme MFE should not be credited mechanically to C12 because non-C12 theme contamination can dominate the price path.

## 4. Machine-readable trigger rows JSONL

```jsonl
{"case_id": "C12_V107_251630_VONETECH_LG_ELECTRONICS_INSPECTION_SYSTEM_20230125", "symbol": "251630", "company": "브이원텍", "trigger_date": "2023-01-25", "entry_date": "2023-01-25", "entry_price": 7360.0, "trigger_type": "Stage3-Yellow", "source_canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_battery_inspection_system_delivery_revenue_gate", "evidence_family": "LG Electronics secondary-battery inspection-system supply contract", "evidence_url": "https://www.businesspost.co.kr/BP?command=article_view&num=304262", "non_price_evidence_summary": "LG전자와 83.14억원 규모 2차전지 검사시스템 공급계약. 계약기간은 2023-01-24~2024-03-30, 2021년 매출 대비 16.27%.", "MFE_30D_pct": 24.3207, "MAE_30D_pct": -4.212, "MFE_90D_pct": 75.8152, "MAE_90D_pct": -4.212, "MFE_180D_pct": 135.462, "MAE_180D_pct": -4.212, "peak_date_180D": "2023-09-05", "peak_price_180D": 17330.0, "drawdown_after_peak_180D_pct": -47.4322, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "classification": "positive_with_local_4b_watch", "profile_error": "current profile may underweight contract-to-delivery inspection equipment when shallow MAE confirms entry quality.", "eps_fcf_explosion": 55, "earnings_visibility": 62, "bottleneck_pricing": 48, "market_mispricing": 64, "valuation_rerating": 70, "capital_allocation": 35, "information_confidence": 78, "simulated_total": 77.4, "simulated_stage": "Stage3-Yellow"}
{"case_id": "C12_V107_333620_NSYS_GLOBAL_CELL_PILOT_LINE_20221020", "symbol": "333620", "company": "엔시스", "trigger_date": "2022-10-20", "entry_date": "2022-10-20", "entry_price": 12250.0, "trigger_type": "Stage2-Actionable", "source_canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_inspection_equipment_customer_diversification_gate", "evidence_family": "global cell customer pilot-line order and expected 2023 revenue", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1666306869717.pdf", "non_price_evidence_summary": "글로벌 셀업체 A사 파일럿 라인 46억원 수주와 2023년 매출 발생/추가 수주 기대가 확인된 검사장비 고객 다변화 표본.", "MFE_30D_pct": 10.2041, "MAE_30D_pct": -2.8571, "MFE_90D_pct": 13.8776, "MAE_90D_pct": -22.2857, "MFE_180D_pct": 34.5306, "MAE_180D_pct": -22.2857, "peak_date_180D": "2023-04-19", "peak_price_180D": 16480.0, "drawdown_after_peak_180D_pct": -29.0655, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "classification": "positive_stage2_with_mae_cap", "profile_error": "Stage2 can open, but Stage3 should wait for follow-on order/revenue recognition because MAE90 breached -20%.", "eps_fcf_explosion": 45, "earnings_visibility": 50, "bottleneck_pricing": 42, "market_mispricing": 55, "valuation_rerating": 54, "capital_allocation": 30, "information_confidence": 70, "simulated_total": 66.2, "simulated_stage": "Stage2-Actionable"}
{"case_id": "C12_V107_419050_SAMGI_LGES_COMMERCIAL_EV_PARTS_20241205", "symbol": "419050", "company": "삼기에너지솔루션즈", "trigger_date": "2024-12-05", "entry_date": "2024-12-05", "entry_price": 1850.0, "trigger_type": "Stage2-Actionable", "source_canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_named_customer_parts_contract_delivery_lag_gate", "evidence_family": "LG Energy Solution commercial-EV battery part supply contract", "evidence_url": "https://www.newspim.com/news/view/20241205000302", "non_price_evidence_summary": "LG에너지솔루션향 전기 상용차용 배터리 부품 1,437억원 공급계약. 계약금액은 전년도 매출 대비 매우 크지만 공급 시작은 2026년 이후라 revenue-recognition lag가 존재.", "MFE_30D_pct": 17.027, "MAE_30D_pct": -16.2162, "MFE_90D_pct": 17.027, "MAE_90D_pct": -20.7027, "MFE_180D_pct": 41.3514, "MAE_180D_pct": -20.7027, "peak_date_180D": "2025-08-12", "peak_price_180D": 2615.0, "drawdown_after_peak_180D_pct": -20.2677, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "classification": "positive_stage2_delayed_delivery", "profile_error": "Named contract is real, but delivery starts later; Stage3 should require shipment/revenue bridge rather than contract headline alone.", "eps_fcf_explosion": 52, "earnings_visibility": 60, "bottleneck_pricing": 46, "market_mispricing": 57, "valuation_rerating": 58, "capital_allocation": 30, "information_confidence": 76, "simulated_total": 70.8, "simulated_stage": "Stage2-Actionable"}
{"case_id": "C12_V107_416180_SHINSUNG_ST_BUSBAR_MODULE_CASE_20240620", "symbol": "416180", "company": "신성에스티", "trigger_date": "2024-06-20", "entry_date": "2024-06-20", "entry_price": 39650.0, "trigger_type": "Stage4B", "source_canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_component_customer_dependency_high_mae_gate", "evidence_family": "LGES/LS EV Korea battery component supplier report", "evidence_url": "https://w4.kirs.or.kr/download/research/240620_%EC%8B%A0%EC%84%B1%EC%97%90%EC%8A%A4%ED%8B%B03.pdf", "non_price_evidence_summary": "버스바와 배터리 모듈 케이스를 생산하고 LG전자/LG에너지솔루션/LS EV Korea 등 고객 기반이 있으나, 상장 초기/부품사 고객의존과 call-off 리스크가 남음.", "MFE_30D_pct": 26.3556, "MAE_30D_pct": -21.8159, "MFE_90D_pct": 26.3556, "MAE_90D_pct": -41.488, "MFE_180D_pct": 26.3556, "MAE_180D_pct": -43.6318, "peak_date_180D": "2024-07-10", "peak_price_180D": 50100.0, "drawdown_after_peak_180D_pct": -55.3892, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "classification": "counterexample_high_mae_component_dependency", "profile_error": "C12 headline evidence exists, but MAE90/180 below -40% demands local 4B overlay until shipment and margin bridge are visible.", "eps_fcf_explosion": 42, "earnings_visibility": 44, "bottleneck_pricing": 38, "market_mispricing": 49, "valuation_rerating": 35, "capital_allocation": 25, "information_confidence": 64, "simulated_total": 58.0, "simulated_stage": "Stage4B-LocalWatch"}
{"case_id": "C12_V107_396300_SEAH_MECHANICS_LGES_MODULE_COVER_20230519", "symbol": "396300", "company": "세아메카닉스", "trigger_date": "2023-05-19", "entry_date": "2023-05-19", "entry_price": 6610.0, "trigger_type": "Stage4B", "source_canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_battery_component_long_contract_margin_bridge_failure", "evidence_family": "LGES North America EV battery module-cover supply contract", "evidence_url": "https://www.the-tech.co.kr/mobile/article.html?no=35401", "non_price_evidence_summary": "LG에너지솔루션과 약 669억원 규모 북미향 전기차 배터리 모듈커버 공급계약, 기간 2023~2030년. 그러나 초기 180D path는 low-MFE/high-MAE.", "MFE_30D_pct": 9.8336, "MAE_30D_pct": -18.003, "MFE_90D_pct": 9.8336, "MAE_90D_pct": -37.5189, "MFE_180D_pct": 9.8336, "MAE_180D_pct": -46.5961, "peak_date_180D": "2023-05-23", "peak_price_180D": 7260.0, "drawdown_after_peak_180D_pct": -51.3774, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "classification": "counterexample_contract_headline_without_near_term_conversion", "profile_error": "Large contract exists but conversion timing/margin bridge was not enough for Stage3; local 4B cap required.", "eps_fcf_explosion": 38, "earnings_visibility": 42, "bottleneck_pricing": 35, "market_mispricing": 40, "valuation_rerating": 30, "capital_allocation": 25, "information_confidence": 72, "simulated_total": 55.6, "simulated_stage": "Stage4B-LocalWatch"}
{"case_id": "C12_V107_065350_SHINSUNG_DELTATECH_LGES_PARTS_THEME_CONTAMINATION_20230428", "symbol": "065350", "company": "신성델타테크", "trigger_date": "2023-04-28", "entry_date": "2023-04-28", "entry_price": 10930.0, "trigger_type": "Stage4B", "source_canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "C12_component_supplier_non_c12_mfe_contamination_gate", "evidence_family": "LGES heat-dissipation frame/Busbar/battery-pack parts supplier report", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1682663888090.pdf", "non_price_evidence_summary": "LG에너지솔루션 파우치형 방열판 사출물, Busbar, 배터리팩 부품 납품 근거는 있으나 이후 MFE의 상당 부분은 2차전지 계약이 아닌 별도 테마 오염 가능성이 큼.", "MFE_30D_pct": 10.979, "MAE_30D_pct": -0.4575, "MFE_90D_pct": 524.8856, "MAE_90D_pct": -6.1299, "MFE_180D_pct": 651.1436, "MAE_180D_pct": -6.1299, "peak_date_180D": "2024-01-24", "peak_price_180D": 82100.0, "drawdown_after_peak_180D_pct": -17.1742, "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "classification": "counterexample_non_c12_mfe_contamination", "profile_error": "Huge MFE should not be credited fully to C12 because dominant price driver can be unrelated theme; decontamination gate needed.", "eps_fcf_explosion": 50, "earnings_visibility": 56, "bottleneck_pricing": 45, "market_mispricing": 40, "valuation_rerating": 25, "capital_allocation": 35, "information_confidence": 66, "simulated_total": 59.5, "simulated_stage": "Stage4B-LocalWatch"}
```

## 5. Score simulation JSONL

```jsonl
{"case_id": "C12_V107_251630_VONETECH_LG_ELECTRONICS_INSPECTION_SYSTEM_20230125", "symbol": "251630", "company": "브이원텍", "eps_fcf_explosion": 55, "earnings_visibility": 62, "bottleneck_pricing": 48, "market_mispricing": 64, "valuation_rerating": 70, "capital_allocation": 35, "information_confidence": 78, "simulated_total": 77.4, "simulated_stage": "Stage3-Yellow", "profile_error": "current profile may underweight contract-to-delivery inspection equipment when shallow MAE confirms entry quality."}
{"case_id": "C12_V107_333620_NSYS_GLOBAL_CELL_PILOT_LINE_20221020", "symbol": "333620", "company": "엔시스", "eps_fcf_explosion": 45, "earnings_visibility": 50, "bottleneck_pricing": 42, "market_mispricing": 55, "valuation_rerating": 54, "capital_allocation": 30, "information_confidence": 70, "simulated_total": 66.2, "simulated_stage": "Stage2-Actionable", "profile_error": "Stage2 can open, but Stage3 should wait for follow-on order/revenue recognition because MAE90 breached -20%."}
{"case_id": "C12_V107_419050_SAMGI_LGES_COMMERCIAL_EV_PARTS_20241205", "symbol": "419050", "company": "삼기에너지솔루션즈", "eps_fcf_explosion": 52, "earnings_visibility": 60, "bottleneck_pricing": 46, "market_mispricing": 57, "valuation_rerating": 58, "capital_allocation": 30, "information_confidence": 76, "simulated_total": 70.8, "simulated_stage": "Stage2-Actionable", "profile_error": "Named contract is real, but delivery starts later; Stage3 should require shipment/revenue bridge rather than contract headline alone."}
{"case_id": "C12_V107_416180_SHINSUNG_ST_BUSBAR_MODULE_CASE_20240620", "symbol": "416180", "company": "신성에스티", "eps_fcf_explosion": 42, "earnings_visibility": 44, "bottleneck_pricing": 38, "market_mispricing": 49, "valuation_rerating": 35, "capital_allocation": 25, "information_confidence": 64, "simulated_total": 58.0, "simulated_stage": "Stage4B-LocalWatch", "profile_error": "C12 headline evidence exists, but MAE90/180 below -40% demands local 4B overlay until shipment and margin bridge are visible."}
{"case_id": "C12_V107_396300_SEAH_MECHANICS_LGES_MODULE_COVER_20230519", "symbol": "396300", "company": "세아메카닉스", "eps_fcf_explosion": 38, "earnings_visibility": 42, "bottleneck_pricing": 35, "market_mispricing": 40, "valuation_rerating": 30, "capital_allocation": 25, "information_confidence": 72, "simulated_total": 55.6, "simulated_stage": "Stage4B-LocalWatch", "profile_error": "Large contract exists but conversion timing/margin bridge was not enough for Stage3; local 4B cap required."}
{"case_id": "C12_V107_065350_SHINSUNG_DELTATECH_LGES_PARTS_THEME_CONTAMINATION_20230428", "symbol": "065350", "company": "신성델타테크", "eps_fcf_explosion": 50, "earnings_visibility": 56, "bottleneck_pricing": 45, "market_mispricing": 40, "valuation_rerating": 25, "capital_allocation": 35, "information_confidence": 66, "simulated_total": 59.5, "simulated_stage": "Stage4B-LocalWatch", "profile_error": "Huge MFE should not be credited fully to C12 because dominant price driver can be unrelated theme; decontamination gate needed."}
```

## 6. Aggregate row

```json
{
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "selected_round": "R3",
  "selected_loop": 107,
  "jsonl_trigger_row_count": 6,
  "calibration_usable_rows": 6,
  "representative_rows": 6,
  "positive_case_count": 3,
  "counterexample_count": 3,
  "stage4b_count": 3,
  "stage4c_count": 0,
  "avg_MFE_180D_pct": 149.7795,
  "avg_MAE_180D_pct": -23.9264,
  "current_profile_error_count": 5,
  "source_proxy_only_rows": 0,
  "evidence_url_pending_rows": 0,
  "proposed_rule_candidate": "C12_CUSTOMER_CONTRACT_REQUIRES_DELIVERY_REVENUE_MARGIN_CALLOFF_AND_THEME_DECONTAMINATION_GATE_V107"
}
```

## 7. Residual contribution summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
calibration_usable_rows: 6
representative_rows: 6
positive_case_count: 3
counterexample_count: 3
4B_case_count: 3
4C_case_count: 0
current_profile_error_count: 5
avg_MFE_180D_pct: 149.7795
avg_MAE_180D_pct: -23.9264
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
```

### Proposed shadow rule

```text
C12_CUSTOMER_CONTRACT_REQUIRES_DELIVERY_REVENUE_MARGIN_CALLOFF_AND_THEME_DECONTAMINATION_GATE_V107
```

Rule meaning:

```text
For C12, Stage2-Actionable can open on a named customer contract, equipment supply contract, or customer-quality evidence. Stage3-Yellow requires at least two of delivery timing, revenue recognition, margin bridge, shipment visibility, or call-off clearance. If MAE90 <= -25% or MAE180 <= -35% before those bridges are confirmed, add local Stage4B overlay. If later MFE is plausibly driven by unrelated theme contamination, keep C12 contribution capped and mark non-C12 MFE contamination.
```

## 8. Narrative case notes

### 251630 브이원텍 — positive with local 4B watch

LG전자와 2차전지 검사시스템 공급계약이 확인되며 entry 이후 shallow MAE and strong MFE path가 나왔다. This is a useful C12 positive, but the 180D peak-to-later drawdown remains large, so the positive evidence should coexist with local 4B exit/position-quality guard.

### 333620 엔시스 — Stage2 positive, not automatic Stage3

The pilot-line order and customer-diversification evidence justify Stage2-Actionable. However, MAE90 reached below -20%, so Stage3 should wait for follow-on order and revenue-recognition confirmation.

### 419050 삼기에너지솔루션즈 — named contract, delayed delivery

The LGES commercial-EV battery part contract is strong non-price evidence. Because delivery starts later than the trigger window, the row supports Stage2 and delayed-positive status, not immediate Stage3-Green.

### 416180 신성에스티 — component dependency high-MAE counterexample

The customer base and product category fit C12, but MAE90/180 breached deeply. This row strengthens the call-off / customer-dependency / margin-bridge gate.

### 396300 세아메카닉스 — long contract, weak near-term conversion

The LGES module-cover contract is real, but the 180D price path failed to confirm near-term conversion. This is a contract-headline counterexample requiring local 4B overlay.

### 065350 신성델타테크 — C12 evidence, non-C12 MFE contamination

The LGES battery-parts evidence is valid, but the later extreme MFE is not cleanly attributable to customer-contract conversion. C12 should decontaminate unrelated theme MFE before giving full positive credit.

## 9. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Ingest this MD as a C12 battery customer-contract/call-off holdout. Parse the JSONL trigger rows. Do not treat contract headline alone as Stage3. Test the proposed shadow gate:
C12_CUSTOMER_CONTRACT_REQUIRES_DELIVERY_REVENUE_MARGIN_CALLOFF_AND_THEME_DECONTAMINATION_GATE_V107.
Apply only as a shadow candidate after dedupe against existing C12 rows. Preserve Stage2-Actionable for named customer contracts, but require delivery/revenue/margin/call-off clearance for Stage3-Yellow or above. Add local 4B overlay when MAE90 <= -25% or MAE180 <= -35% before bridge confirmation. Mark non-C12 theme contamination where MFE is not attributable to customer-contract conversion.
```

## 11. Completed research state

```text
completed_round = R3
completed_loop = 107
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 static ledger C12 rows=32 / need-to-50=18; current-session C12 quality holdout
next_recommended_archetypes = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only | C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 12. Normalized machine-readable rows JSONL

The JSONL block below is the normalized batch-ingest block. Earlier compact research JSON snippets in this file are narrative-compatible, but this block carries the canonical `row_type` and required V12 fields.

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"C12_V107_T01_251630","case_id":"C12_V107_251630_VONETECH_LG_ELECTRONICS_INSPECTION_SYSTEM_20230125","symbol":"251630","company_name":"브이원텍","company":"브이원텍","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","sector":"battery_ev_green_mobility","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":["holdout_validation","counterexample_mining","customer_contract_delivery_gate","calloff_and_revenue_recognition_gate","non_c12_theme_contamination_deconfliction"],"trigger_type":"Stage3-Yellow","trigger_date":"2023-01-25","evidence_available_at_that_date":true,"evidence_source":"https://www.businesspost.co.kr/BP?command=article_view&num=304262","evidence_url":"https://www.businesspost.co.kr/BP?command=article_view&num=304262","evidence_family":"LG Electronics secondary-battery inspection-system supply contract","evidence_summary":"LG전자와 83.14억원 규모 2차전지 검사시스템 공급계약. 계약기간은 2023-01-24~2024-03-30, 2021년 매출 대비 16.27%.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["named_customer_contract","delivery_timing","revenue_recognition_window","shallow_MAE_path"],"stage4b_evidence_fields":["call_off_or_delivery_timing_risk","local_4b_watch_guard","margin_bridge_unconfirmed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/251/251630/2023.csv","profile_path":"atlas/symbol_profiles/251/251630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-25","entry_price":7360.0,"MFE_30D_pct":24.3207,"MFE_90D_pct":75.8152,"MFE_180D_pct":135.462,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.212,"MAE_90D_pct":-4.212,"MAE_180D_pct":-4.212,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-05","peak_price":17330.0,"drawdown_after_peak_pct":-47.4322,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no separate Stage3-Green comparison trigger in this holdout file","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"not_full_4b","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_with_local_4b_watch","current_profile_verdict":"current profile may underweight contract-to-delivery inspection equipment when shallow MAE confirms entry quality.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","window_180D_corporate_action_contaminated":false,"corporate_action_contaminated_180D":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_251630_Stage3-Yellow_2023-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"new symbol and new component/inspection-contract trigger family within C12 holdout","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"production_scoring_patch_applied":false}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"C12_V107_T02_333620","case_id":"C12_V107_333620_NSYS_GLOBAL_CELL_PILOT_LINE_20221020","symbol":"333620","company_name":"엔시스","company":"엔시스","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","sector":"battery_ev_green_mobility","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":["holdout_validation","counterexample_mining","customer_contract_delivery_gate","calloff_and_revenue_recognition_gate","non_c12_theme_contamination_deconfliction"],"trigger_type":"Stage2-Actionable","trigger_date":"2022-10-20","evidence_available_at_that_date":true,"evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1666306869717.pdf","evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1666306869717.pdf","evidence_family":"global cell customer pilot-line order and expected 2023 revenue","evidence_summary":"글로벌 셀업체 A사 파일럿 라인 46억원 수주와 2023년 매출 발생/추가 수주 기대가 확인된 검사장비 고객 다변화 표본.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["customer_diversification","pilot_line_order","expected_revenue_conversion"],"stage4b_evidence_fields":["call_off_or_delivery_timing_risk","local_4b_watch_guard","margin_bridge_unconfirmed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/333/333620/2022.csv","profile_path":"atlas/symbol_profiles/333/333620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-10-20","entry_price":12250.0,"MFE_30D_pct":10.2041,"MFE_90D_pct":13.8776,"MFE_180D_pct":34.5306,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.8571,"MAE_90D_pct":-22.2857,"MAE_180D_pct":-22.2857,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-19","peak_price":16480.0,"drawdown_after_peak_pct":-29.0655,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no separate Stage3-Green comparison trigger in this holdout file","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","execution_risk"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_stage2_with_mae_cap","current_profile_verdict":"Stage2 can open, but Stage3 should wait for follow-on order/revenue recognition because MAE90 breached -20%.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","window_180D_corporate_action_contaminated":false,"corporate_action_contaminated_180D":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_333620_Stage2-Actionable_2022-10-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"new symbol and new component/inspection-contract trigger family within C12 holdout","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"production_scoring_patch_applied":false}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"C12_V107_T03_419050","case_id":"C12_V107_419050_SAMGI_LGES_COMMERCIAL_EV_PARTS_20241205","symbol":"419050","company_name":"삼기에너지솔루션즈","company":"삼기에너지솔루션즈","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","sector":"battery_ev_green_mobility","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":["holdout_validation","counterexample_mining","customer_contract_delivery_gate","calloff_and_revenue_recognition_gate","non_c12_theme_contamination_deconfliction"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-12-05","evidence_available_at_that_date":true,"evidence_source":"https://www.newspim.com/news/view/20241205000302","evidence_url":"https://www.newspim.com/news/view/20241205000302","evidence_family":"LG Energy Solution commercial-EV battery part supply contract","evidence_summary":"LG에너지솔루션향 전기 상용차용 배터리 부품 1,437억원 공급계약. 계약금액은 전년도 매출 대비 매우 크지만 공급 시작은 2026년 이후라 revenue-recognition lag가 존재.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["named_customer_contract","large_contract_scale","delayed_delivery_route"],"stage4b_evidence_fields":["call_off_or_delivery_timing_risk","local_4b_watch_guard","margin_bridge_unconfirmed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/419/419050/2024.csv","profile_path":"atlas/symbol_profiles/419/419050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-12-05","entry_price":1850.0,"MFE_30D_pct":17.027,"MFE_90D_pct":17.027,"MFE_180D_pct":41.3514,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.2162,"MAE_90D_pct":-20.7027,"MAE_180D_pct":-20.7027,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-08-12","peak_price":2615.0,"drawdown_after_peak_pct":-20.2677,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no separate Stage3-Green comparison trigger in this holdout file","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","execution_risk"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_stage2_delayed_delivery","current_profile_verdict":"Named contract is real, but delivery starts later; Stage3 should require shipment/revenue bridge rather than contract headline alone.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","window_180D_corporate_action_contaminated":false,"corporate_action_contaminated_180D":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_419050_Stage2-Actionable_2024-12-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"new symbol and new component/inspection-contract trigger family within C12 holdout","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"production_scoring_patch_applied":false}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"C12_V107_T04_416180","case_id":"C12_V107_416180_SHINSUNG_ST_BUSBAR_MODULE_CASE_20240620","symbol":"416180","company_name":"신성에스티","company":"신성에스티","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","sector":"battery_ev_green_mobility","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":["holdout_validation","counterexample_mining","customer_contract_delivery_gate","calloff_and_revenue_recognition_gate","non_c12_theme_contamination_deconfliction"],"trigger_type":"Stage4B","trigger_date":"2024-06-20","evidence_available_at_that_date":true,"evidence_source":"https://w4.kirs.or.kr/download/research/240620_%EC%8B%A0%EC%84%B1%EC%97%90%EC%8A%A4%ED%8B%B03.pdf","evidence_url":"https://w4.kirs.or.kr/download/research/240620_%EC%8B%A0%EC%84%B1%EC%97%90%EC%8A%A4%ED%8B%B03.pdf","evidence_family":"LGES/LS EV Korea battery component supplier report","evidence_summary":"버스바와 배터리 모듈 케이스를 생산하고 LG전자/LG에너지솔루션/LS EV Korea 등 고객 기반이 있으나, 상장 초기/부품사 고객의존과 call-off 리스크가 남음.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["call_off_or_delivery_timing_risk","local_4b_watch_guard","margin_bridge_unconfirmed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/416/416180/2024.csv","profile_path":"atlas/symbol_profiles/416/416180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-20","entry_price":39650.0,"MFE_30D_pct":26.3556,"MFE_90D_pct":26.3556,"MFE_180D_pct":26.3556,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.8159,"MAE_90D_pct":-41.488,"MAE_180D_pct":-43.6318,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-10","peak_price":50100.0,"drawdown_after_peak_pct":-55.3892,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no separate Stage3-Green comparison trigger in this holdout file","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","execution_risk"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_high_mae_component_dependency","current_profile_verdict":"C12 headline evidence exists, but MAE90/180 below -40% demands local 4B overlay until shipment and margin bridge are visible.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","window_180D_corporate_action_contaminated":false,"corporate_action_contaminated_180D":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_416180_Stage4B_2024-06-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"new symbol and new component/inspection-contract trigger family within C12 holdout","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"production_scoring_patch_applied":false}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"C12_V107_T05_396300","case_id":"C12_V107_396300_SEAH_MECHANICS_LGES_MODULE_COVER_20230519","symbol":"396300","company_name":"세아메카닉스","company":"세아메카닉스","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","sector":"battery_ev_green_mobility","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":["holdout_validation","counterexample_mining","customer_contract_delivery_gate","calloff_and_revenue_recognition_gate","non_c12_theme_contamination_deconfliction"],"trigger_type":"Stage4B","trigger_date":"2023-05-19","evidence_available_at_that_date":true,"evidence_source":"https://www.the-tech.co.kr/mobile/article.html?no=35401","evidence_url":"https://www.the-tech.co.kr/mobile/article.html?no=35401","evidence_family":"LGES North America EV battery module-cover supply contract","evidence_summary":"LG에너지솔루션과 약 669억원 규모 북미향 전기차 배터리 모듈커버 공급계약, 기간 2023~2030년. 그러나 초기 180D path는 low-MFE/high-MAE.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["call_off_or_delivery_timing_risk","local_4b_watch_guard","margin_bridge_unconfirmed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/396/396300/2023.csv","profile_path":"atlas/symbol_profiles/396/396300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-19","entry_price":6610.0,"MFE_30D_pct":9.8336,"MFE_90D_pct":9.8336,"MFE_180D_pct":9.8336,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.003,"MAE_90D_pct":-37.5189,"MAE_180D_pct":-46.5961,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-23","peak_price":7260.0,"drawdown_after_peak_pct":-51.3774,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no separate Stage3-Green comparison trigger in this holdout file","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","execution_risk"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_contract_headline_without_near_term_conversion","current_profile_verdict":"Large contract exists but conversion timing/margin bridge was not enough for Stage3; local 4B cap required.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","window_180D_corporate_action_contaminated":false,"corporate_action_contaminated_180D":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_396300_Stage4B_2023-05-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"new symbol and new component/inspection-contract trigger family within C12 holdout","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"production_scoring_patch_applied":false}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"C12_V107_T06_065350","case_id":"C12_V107_065350_SHINSUNG_DELTATECH_LGES_PARTS_THEME_CONTAMINATION_20230428","symbol":"065350","company_name":"신성델타테크","company":"신성델타테크","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","sector":"battery_ev_green_mobility","primary_archetype":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_objective":["holdout_validation","counterexample_mining","customer_contract_delivery_gate","calloff_and_revenue_recognition_gate","non_c12_theme_contamination_deconfliction"],"trigger_type":"Stage4B","trigger_date":"2023-04-28","evidence_available_at_that_date":true,"evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1682663888090.pdf","evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1682663888090.pdf","evidence_family":"LGES heat-dissipation frame/Busbar/battery-pack parts supplier report","evidence_summary":"LG에너지솔루션 파우치형 방열판 사출물, Busbar, 배터리팩 부품 납품 근거는 있으나 이후 MFE의 상당 부분은 2차전지 계약이 아닌 별도 테마 오염 가능성이 큼.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["call_off_or_delivery_timing_risk","local_4b_watch_guard","margin_bridge_unconfirmed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/065/065350/2023.csv","profile_path":"atlas/symbol_profiles/065/065350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-28","entry_price":10930.0,"MFE_30D_pct":10.979,"MFE_90D_pct":524.8856,"MFE_180D_pct":651.1436,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.4575,"MAE_90D_pct":-6.1299,"MAE_180D_pct":-6.1299,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-24","peak_price":82100.0,"drawdown_after_peak_pct":-17.1742,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no separate Stage3-Green comparison trigger in this holdout file","four_b_local_peak_proximity":"not_applicable","four_b_full_window_peak_proximity":"not_applicable","four_b_timing_verdict":"local_4b_watch_required","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","execution_risk"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_non_c12_mfe_contamination","current_profile_verdict":"Huge MFE should not be credited fully to C12 because dominant price driver can be unrelated theme; decontamination gate needed.","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","window_180D_corporate_action_contaminated":false,"corporate_action_contaminated_180D":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_065350_Stage4B_2023-04-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","representative_for_aggregate":true,"is_new_independent_case":true,"reuse_reason":"new symbol and new component/inspection-contract trigger family within C12 holdout","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"production_scoring_patch_applied":false}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","case_id":"C12_V107_251630_VONETECH_LG_ELECTRONICS_INSPECTION_SYSTEM_20230125","symbol":"251630","company_name":"브이원텍","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C12_shadow_gate_v107","rollback_reference_profile_id":"e2r_2_0_baseline_reference","baseline_current_profile_proxy_stage":"Stage2-Actionable_or_Stage3_if_contract_headline_overweighted","shadow_rule_corrected_stage":"Stage3-Yellow","component_breakdown":{"contract_score":78,"backlog_visibility_score":62,"margin_bridge_score":55,"revision_score":70,"relative_strength_score":64,"customer_quality_score":48,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":95.788,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":55,"fcf_conversion_score":45,"theme_decontamination_risk_score":20},"simulated_total":77.4,"simulated_stage":"Stage3-Yellow","score_return_alignment":"current profile may underweight contract-to-delivery inspection equipment when shallow MAE confirms entry quality.","production_scoring_patch_applied":false}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","case_id":"C12_V107_333620_NSYS_GLOBAL_CELL_PILOT_LINE_20221020","symbol":"333620","company_name":"엔시스","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C12_shadow_gate_v107","rollback_reference_profile_id":"e2r_2_0_baseline_reference","baseline_current_profile_proxy_stage":"Stage2-Actionable_or_Stage3_if_contract_headline_overweighted","shadow_rule_corrected_stage":"Stage2-Actionable","component_breakdown":{"contract_score":70,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":54,"relative_strength_score":55,"customer_quality_score":42,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":77.71430000000001,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":40,"fcf_conversion_score":30,"theme_decontamination_risk_score":20},"simulated_total":66.2,"simulated_stage":"Stage2-Actionable","score_return_alignment":"Stage2 can open, but Stage3 should wait for follow-on order/revenue recognition because MAE90 breached -20%.","production_scoring_patch_applied":false}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","case_id":"C12_V107_419050_SAMGI_LGES_COMMERCIAL_EV_PARTS_20241205","symbol":"419050","company_name":"삼기에너지솔루션즈","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C12_shadow_gate_v107","rollback_reference_profile_id":"e2r_2_0_baseline_reference","baseline_current_profile_proxy_stage":"Stage2-Actionable_or_Stage3_if_contract_headline_overweighted","shadow_rule_corrected_stage":"Stage2-Actionable","component_breakdown":{"contract_score":76,"backlog_visibility_score":60,"margin_bridge_score":52,"revision_score":58,"relative_strength_score":57,"customer_quality_score":46,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":79.2973,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":55,"fcf_conversion_score":30,"theme_decontamination_risk_score":20},"simulated_total":70.8,"simulated_stage":"Stage2-Actionable","score_return_alignment":"Named contract is real, but delivery starts later; Stage3 should require shipment/revenue bridge rather than contract headline alone.","production_scoring_patch_applied":false}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","case_id":"C12_V107_416180_SHINSUNG_ST_BUSBAR_MODULE_CASE_20240620","symbol":"416180","company_name":"신성에스티","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C12_shadow_gate_v107","rollback_reference_profile_id":"e2r_2_0_baseline_reference","baseline_current_profile_proxy_stage":"Stage2-Actionable_or_Stage3_if_contract_headline_overweighted","shadow_rule_corrected_stage":"Stage4B-LocalWatch","component_breakdown":{"contract_score":64,"backlog_visibility_score":44,"margin_bridge_score":42,"revision_score":35,"relative_strength_score":49,"customer_quality_score":38,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":56.3682,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":40,"fcf_conversion_score":30,"theme_decontamination_risk_score":20},"simulated_total":58.0,"simulated_stage":"Stage4B-LocalWatch","score_return_alignment":"C12 headline evidence exists, but MAE90/180 below -40% demands local 4B overlay until shipment and margin bridge are visible.","production_scoring_patch_applied":false}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","case_id":"C12_V107_396300_SEAH_MECHANICS_LGES_MODULE_COVER_20230519","symbol":"396300","company_name":"세아메카닉스","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C12_shadow_gate_v107","rollback_reference_profile_id":"e2r_2_0_baseline_reference","baseline_current_profile_proxy_stage":"Stage2-Actionable_or_Stage3_if_contract_headline_overweighted","shadow_rule_corrected_stage":"Stage4B-LocalWatch","component_breakdown":{"contract_score":72,"backlog_visibility_score":42,"margin_bridge_score":38,"revision_score":30,"relative_strength_score":40,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":30,"execution_risk_score":53.4039,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":40,"fcf_conversion_score":30,"theme_decontamination_risk_score":20},"simulated_total":55.6,"simulated_stage":"Stage4B-LocalWatch","score_return_alignment":"Large contract exists but conversion timing/margin bridge was not enough for Stage3; local 4B cap required.","production_scoring_patch_applied":false}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","case_id":"C12_V107_065350_SHINSUNG_DELTATECH_LGES_PARTS_THEME_CONTAMINATION_20230428","symbol":"065350","company_name":"신성델타테크","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C12_shadow_gate_v107","rollback_reference_profile_id":"e2r_2_0_baseline_reference","baseline_current_profile_proxy_stage":"Stage2-Actionable_or_Stage3_if_contract_headline_overweighted","shadow_rule_corrected_stage":"Stage4B-LocalWatch","component_breakdown":{"contract_score":66,"backlog_visibility_score":56,"margin_bridge_score":50,"revision_score":25,"relative_strength_score":40,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":25,"execution_risk_score":93.8701,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":40,"fcf_conversion_score":30,"theme_decontamination_risk_score":80},"simulated_total":59.5,"simulated_stage":"Stage4B-LocalWatch","score_return_alignment":"Huge MFE should not be credited fully to C12 because dominant price driver can be unrelated theme; decontamination gate needed.","production_scoring_patch_applied":false}
{"row_type":"aggregate","schema_family":"v12_sector_archetype_residual","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_C12_component_inspection_contract_calloff_holdout_v107","jsonl_trigger_row_count":6,"calibration_usable_rows":6,"representative_rows":6,"new_independent_case_count":6,"reused_case_count":0,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":6,"positive_case_count":3,"counterexample_count":3,"stage4b_count":3,"stage4c_count":0,"current_profile_error_count":5,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"avg_MFE_180D_pct":149.7795,"avg_MAE_180D_pct":-23.9264,"sector_specific_rule_candidate":"L3_C12_COMPONENT_CONTRACT_DELIVERY_REVENUE_CALLOFF_GATE","canonical_archetype_rule_candidate":"C12_CUSTOMER_CONTRACT_REQUIRES_DELIVERY_REVENUE_MARGIN_CALLOFF_AND_THEME_DECONTAMINATION_GATE_V107","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"production_scoring_patch_applied":false}
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_customer_contract_delivery_revenue_calloff_gate","shadow_rule_candidate":"Stage2-Actionable can open on named customer/component/inspection-equipment contract. Stage3-Yellow requires at least two of delivery timing, revenue recognition, margin bridge, shipment visibility, or call-off clearance. If MAE90 <= -25% or MAE180 <= -35% before bridge confirmation, add local Stage4B overlay. If later MFE is plausibly unrelated to C12, cap C12 contribution and mark theme decontamination.","eligible_trigger_count":6,"confidence":"medium_high","production_scoring_patch_applied":false}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R3","loop":107,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C12_CUSTOMER_CONTRACT_REQUIRES_DELIVERY_REVENUE_MARGIN_CALLOFF_AND_THEME_DECONTAMINATION_GATE_V107","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"existing_axis_weakened":null,"summary":"This loop adds six C12 component/inspection customer-contract rows. It preserves Stage2 for named contracts but forces Stage3 to wait for delivery, revenue recognition, margin/cash bridge, or call-off clearance. It also caps non-C12 theme contamination.","production_scoring_patch_applied":false}
```

## 13. Normalized Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```
