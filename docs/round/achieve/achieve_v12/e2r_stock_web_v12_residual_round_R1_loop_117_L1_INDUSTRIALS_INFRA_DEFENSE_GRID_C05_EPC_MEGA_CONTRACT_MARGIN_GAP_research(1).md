# E2R Stock-Web V12 Residual Research — C05 EPC Mega Contract Margin Gap V117

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R1_loop_117_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
selected_round: R1
selected_loop: 117
selection_basis: docs/core/V12_Research_No_Repeat_Index.md used as no-repeat ledger only
selected_priority_bucket: Priority 1 static ledger C05 rows=47 / need-to-50=3; current-session C05 already above 50, so this is a new-symbol quality holdout focused on working-capital, cash-collection and cleanroom/plant EPC margin conversion
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: mixed_C05_epc_cleanroom_power_plant_order_cash_margin_holdout_v117
loop_objective:
  - holdout_validation
  - counterexample_mining
  - working_capital_cash_collection_gate
  - revenue_recognition_margin_bridge_gate
  - local_4B_watch_guard_stress_test
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

The no-repeat ledger still marks `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` as a Priority 1 archetype with `47` representative rows and only `3` rows needed to reach the 50-row practical calibration band. The current conversation has already produced several C05 passes, so this run is not a simple count-fill. It is a quality holdout that deliberately avoids the visible prior C05 core set:

```text
028050 삼성E&A
006360 GS건설
000720 현대건설
047040 대우건설
375500 DL이앤씨
045100 한양이엔지
011560 세보엠이씨
053080 케이엔솔
016250 SGC E&C
037350 성도이엔지
011930 신성이엔지
013580 계룡건설
014790 HL D&I
021320 KCC건설
```

This file uses six new C05 symbols / trigger families:

```text
028260 삼성물산 — overseas desalination/power EPC final contract
004960 한신공영 — public works order / backlog profitability bridge
083650 비에이치아이 — HRSG power-plant supply contract
003070 코오롱글로벌 — H1 order growth without realized margin bridge
002150 도화엔지니어링 — engineering/EPC/O&M quality but low C05 rerating
010400 우진아이엔에스 — cleanroom equipment contract with small-scale/high-MAE cap
```

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No row in this file repeats a visible prior C05 hard key from the current session.

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
028260: corporate_action_candidate_dates=[2015-09-15], no overlap with 2024-12-11~180D
004960: corporate_action_candidate_dates=[1998-09-19, 2001-06-20, 2002-04-03, 2002-05-24, 2002-11-14], no overlap with 2024-03-13~180D
083650: corporate_action_candidate_dates=[2006-06-16, 2006-07-12, 2015-04-10, 2015-05-12], no overlap with 2024-03-05~180D
003070: corporate_action_candidate_dates=[1997-01-03, 1999-10-22, 2004-12-30, 2010-11-23, 2012-01-11, 2014-05-23, 2017-08-01, 2023-01-31, 2025-12-11], no overlap with 2024-08-12~180D
002150: corporate_action_candidate_dates=[2013-02-01, 2013-02-26], no overlap with 2024-06-18~180D
010400: corporate_action_candidate_dates=[], clean 180D window
```

## 3. Core finding

C05 should not treat every EPC, cleanroom, public works or plant equipment headline as a clean Stage3 rerating. The mechanism has five doors:

```text
named contract / backlog
→ delivery or construction progress
→ revenue recognition
→ realized margin / cost-control
→ working-capital or cash collection
```

`028260` and `083650` passed enough of the named-contract and shallow-MAE tests to remain positive, but both still need a margin/cash bridge before Stage3-Green. `003070`, `002150`, and `010400` show the other side of the bridge: real business evidence can open MFE, but without realized margin or cash conversion the path either stalls or suffers local 4B drawdown. `004960` is a low-volatility Stage2 case: backlog/profitability evidence exists, but the price path does not justify Stage3 promotion yet.

## 4. Machine-readable trigger rows JSONL

```jsonl
{"case_id": "C05_V117_028260_SAMSUNG_CNT_QATAR_DESAL_POWER_EPC_20241211", "symbol": "028260", "company": "삼성물산", "trigger_date": "2024-12-11", "entry_date": "2024-12-11", "entry_price": 116500.0, "trigger_type": "Stage3-Yellow", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_overseas_power_desalination_epc_final_contract_margin_bridge", "evidence_family": "Qatar Facility E desalination and combined-cycle power plant EPC contract", "evidence_url": "https://news.samsungcnt.com/en/features/engineering-construction/2024-12-samsung-campt-secures-2-84-billion-desalination-and-power-plant-project-in-qatar/", "non_price_evidence_summary": "Samsung C&T E&C announced a $2.84B EPC contract for Qatar Facility E desalination and combined-cycle power project in consortium with Sumitomo. Project completion target is 2029, so Stage3 needs a long-duration revenue/margin bridge rather than headline contract value alone.", "MFE_30D_pct": 6.3519, "MAE_30D_pct": -3.5193, "MFE_90D_pct": 17.4249, "MAE_90D_pct": -7.2103, "MFE_180D_pct": 62.1459, "MAE_180D_pct": -7.2103, "peak_date_180D": "2025-07-17", "peak_price_180D": 188900.0, "drawdown_after_peak_180D_pct": -17.7872, "classification": "positive_stage3_yellow_with_long_duration_cash_gate", "profile_error": "Current profile should allow C05 positive when named EPC contract plus shallow MAE confirms entry quality, but Green should wait for execution margin/cash bridge.", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "price_basis": "tradable_raw", "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "eps_fcf_explosion": 62, "earnings_visibility": 70, "bottleneck_pricing": 58, "market_mispricing": 62, "valuation_rerating": 66, "capital_allocation": 48, "information_confidence": 86, "simulated_total": 79.6, "simulated_stage": "Stage3-Yellow"}
{"case_id": "C05_V117_004960_HANSHIN_PUBLIC_WORKS_ORDER_BACKLOG_20240313", "symbol": "004960", "company": "한신공영", "trigger_date": "2024-03-13", "entry_date": "2024-03-13", "entry_price": 6900.0, "trigger_type": "Stage2-Actionable", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_public_order_backlog_profitability_recovery_gate", "evidence_family": "public works order and backlog/profitability recovery commentary", "evidence_url": "https://www.yna.co.kr/view/AKR20240313115900003", "non_price_evidence_summary": "한신공영은 2024-03-13 공공공사 수주와 도시정비/공공공사 수주잔고를 제시했고, 원가 상승분 선반영 이후 수익성 개선 기대를 언급했다. 다만 단일 order size and cash-collection bridge are not enough for Stage3.", "MFE_30D_pct": 2.3188, "MAE_30D_pct": -10.7246, "MFE_90D_pct": 5.6522, "MAE_90D_pct": -10.7246, "MFE_180D_pct": 15.5072, "MAE_180D_pct": -10.7246, "peak_date_180D": "2024-11-12", "peak_price_180D": 7970.0, "drawdown_after_peak_180D_pct": -17.8168, "classification": "stage2_positive_low_mfe_margin_bridge_pending", "profile_error": "Stage2 can open on backlog/profitability bridge, but low 90D/180D MFE and unfinished margin/cash bridge argue against Stage3 promotion.", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "price_basis": "tradable_raw", "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "eps_fcf_explosion": 45, "earnings_visibility": 55, "bottleneck_pricing": 40, "market_mispricing": 52, "valuation_rerating": 48, "capital_allocation": 34, "information_confidence": 74, "simulated_total": 66.0, "simulated_stage": "Stage2-Actionable"}
{"case_id": "C05_V117_083650_BHI_DAEWOO_HRSG_GONGJU_20240305", "symbol": "083650", "company": "비에이치아이", "trigger_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 8590.0, "trigger_type": "Stage3-Yellow", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_power_plant_hrsg_contract_to_delivery_margin_gate", "evidence_family": "Daewoo E&C Gongju gas power plant HRSG supply contract", "evidence_url": "https://www.mk.co.kr/en/business/10957352", "non_price_evidence_summary": "BHI signed a 550MW HRSG supply contract worth KRW 47.5B with Daewoo E&C for Gongju natural-gas power plant and will supply HRSG plus condenser. Strong C05 contract evidence, but 180D price verticality requires local 4B watch.", "MFE_30D_pct": 27.3574, "MAE_30D_pct": -9.7788, "MFE_90D_pct": 41.6764, "MAE_90D_pct": -10.8265, "MFE_180D_pct": 131.8976, "MAE_180D_pct": -18.5099, "peak_date_180D": "2024-11-22", "peak_price_180D": 19920.0, "drawdown_after_peak_180D_pct": -15.512, "classification": "positive_with_vertical_mfe_local_4b_watch", "profile_error": "Named contract and customer quality justify Stage3-Yellow, but very high 180D MFE demands a local 4B overlay unless follow-on revenue/margin conversion is verified.", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "price_basis": "tradable_raw", "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "eps_fcf_explosion": 65, "earnings_visibility": 68, "bottleneck_pricing": 70, "market_mispricing": 72, "valuation_rerating": 78, "capital_allocation": 36, "information_confidence": 82, "simulated_total": 83.2, "simulated_stage": "Stage3-Yellow"}
{"case_id": "C05_V117_003070_KOLON_GLOBAL_H1_ORDER_BACKLOG_20240812", "symbol": "003070", "company": "코오롱글로벌", "trigger_date": "2024-08-12", "entry_date": "2024-08-12", "entry_price": 9830.0, "trigger_type": "Stage4B", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_construction_order_growth_without_margin_cash_bridge", "evidence_family": "2024 H1 construction order growth / backlog recovery headline", "evidence_url": "https://v.daum.net/v/20240812094715955", "non_price_evidence_summary": "코오롱글로벌은 2024년 상반기 건설부문 신규수주 2.4조원을 발표했다. Headline order recovery produced fast MFE, but no realized margin/cash bridge; post-peak drawdown was severe.", "MFE_30D_pct": 31.1292, "MAE_30D_pct": -8.3418, "MFE_90D_pct": 31.1292, "MAE_90D_pct": -19.4303, "MFE_180D_pct": 31.1292, "MAE_180D_pct": -19.4303, "peak_date_180D": "2024-08-27", "peak_price_180D": 12890.0, "drawdown_after_peak_180D_pct": -38.557, "classification": "counterexample_fast_mfe_without_margin_cash_bridge", "profile_error": "Order growth alone can create a tradable MFE burst, but Stage3 persistence fails without margin/working-capital bridge; local 4B cap required after the fast peak.", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "price_basis": "tradable_raw", "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "eps_fcf_explosion": 42, "earnings_visibility": 48, "bottleneck_pricing": 36, "market_mispricing": 58, "valuation_rerating": 42, "capital_allocation": 28, "information_confidence": 70, "simulated_total": 61.2, "simulated_stage": "Stage4B-LocalWatch"}
{"case_id": "C05_V117_002150_DOHWA_IR_ENGINEERING_EPC_O_AND_M_20240618", "symbol": "002150", "company": "도화엔지니어링", "trigger_date": "2024-06-18", "entry_date": "2024-06-18", "entry_price": 7770.0, "trigger_type": "Stage2-Actionable", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_engineering_epc_om_backlog_low_mfe_holdout", "evidence_family": "2024 IR engineering / EPC / O&M and long-term PPA income bridge", "evidence_url": "https://www.dohwa.co.kr/download/file/202406180015359275231461ba0414", "non_price_evidence_summary": "Dohwa's 2024 IR discussed engineering, EPC/O&M/investment-development and stable long-term PPA income. The business model has quality, but C05 mega-contract rerating was not visible in price path.", "MFE_30D_pct": 6.5637, "MAE_30D_pct": -5.0193, "MFE_90D_pct": 6.5637, "MAE_90D_pct": -18.2754, "MFE_180D_pct": 6.5637, "MAE_180D_pct": -19.8198, "peak_date_180D": "2024-07-25", "peak_price_180D": 8280.0, "drawdown_after_peak_180D_pct": -24.7585, "classification": "counterexample_quality_business_but_no_c05_rerating", "profile_error": "Stable PPA/O&M evidence should not be compressed into C05 mega-contract Stage3; keep Stage2 until backlog-to-margin catalyst appears.", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "price_basis": "tradable_raw", "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "eps_fcf_explosion": 35, "earnings_visibility": 52, "bottleneck_pricing": 34, "market_mispricing": 44, "valuation_rerating": 35, "capital_allocation": 34, "information_confidence": 68, "simulated_total": 57.4, "simulated_stage": "Stage2-Actionable"}
{"case_id": "C05_V117_010400_WOOJININS_CLEANROOM_GS_E_AND_C_20220817", "symbol": "010400", "company": "우진아이엔에스", "trigger_date": "2022-08-17", "entry_date": "2022-08-17", "entry_price": 6300.0, "trigger_type": "Stage4B", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_cleanroom_mechanical_work_small_contract_high_mae_gate", "evidence_family": "GS E&C Gwacheon cleanroom-equipment construction contract", "evidence_url": "https://cm.asiae.co.kr/article/2022081716015130153", "non_price_evidence_summary": "우진아이엔에스는 GS건설과 과천 상상자이타워 클린룸 설비 공사 계약을 체결했다. Contract evidence is real, but amount is too small for clean Stage3 and 90D/180D MAE breached -20%.", "MFE_30D_pct": 23.8095, "MAE_30D_pct": -9.2063, "MFE_90D_pct": 23.8095, "MAE_90D_pct": -21.1905, "MFE_180D_pct": 38.0952, "MAE_180D_pct": -21.1905, "peak_date_180D": "2023-01-06", "peak_price_180D": 8700.0, "drawdown_after_peak_180D_pct": -37.8161, "classification": "counterexample_small_contract_high_mae_local_4b", "profile_error": "Contract headline opened MFE, but small contract scale and high MAE require local 4B until repeated delivery/revenue/margin bridge appears.", "calibration_usable": true, "representative_for_aggregate": true, "corporate_action_contaminated_180D": false, "source_proxy_only": false, "evidence_url_pending": false, "price_basis": "tradable_raw", "window_180D_corporate_action_contaminated": false, "insufficient_forward_window": false, "eps_fcf_explosion": 40, "earnings_visibility": 42, "bottleneck_pricing": 38, "market_mispricing": 54, "valuation_rerating": 40, "capital_allocation": 24, "information_confidence": 72, "simulated_total": 59.4, "simulated_stage": "Stage4B-LocalWatch"}
```

## 5. Score simulation JSONL

```jsonl
{"case_id": "C05_V117_028260_SAMSUNG_CNT_QATAR_DESAL_POWER_EPC_20241211", "symbol": "028260", "company": "삼성물산", "eps_fcf_explosion": 62, "earnings_visibility": 70, "bottleneck_pricing": 58, "market_mispricing": 62, "valuation_rerating": 66, "capital_allocation": 48, "information_confidence": 86, "simulated_total": 79.6, "simulated_stage": "Stage3-Yellow", "profile_error": "Current profile should allow C05 positive when named EPC contract plus shallow MAE confirms entry quality, but Green should wait for execution margin/cash bridge."}
{"case_id": "C05_V117_004960_HANSHIN_PUBLIC_WORKS_ORDER_BACKLOG_20240313", "symbol": "004960", "company": "한신공영", "eps_fcf_explosion": 45, "earnings_visibility": 55, "bottleneck_pricing": 40, "market_mispricing": 52, "valuation_rerating": 48, "capital_allocation": 34, "information_confidence": 74, "simulated_total": 66.0, "simulated_stage": "Stage2-Actionable", "profile_error": "Stage2 can open on backlog/profitability bridge, but low 90D/180D MFE and unfinished margin/cash bridge argue against Stage3 promotion."}
{"case_id": "C05_V117_083650_BHI_DAEWOO_HRSG_GONGJU_20240305", "symbol": "083650", "company": "비에이치아이", "eps_fcf_explosion": 65, "earnings_visibility": 68, "bottleneck_pricing": 70, "market_mispricing": 72, "valuation_rerating": 78, "capital_allocation": 36, "information_confidence": 82, "simulated_total": 83.2, "simulated_stage": "Stage3-Yellow", "profile_error": "Named contract and customer quality justify Stage3-Yellow, but very high 180D MFE demands a local 4B overlay unless follow-on revenue/margin conversion is verified."}
{"case_id": "C05_V117_003070_KOLON_GLOBAL_H1_ORDER_BACKLOG_20240812", "symbol": "003070", "company": "코오롱글로벌", "eps_fcf_explosion": 42, "earnings_visibility": 48, "bottleneck_pricing": 36, "market_mispricing": 58, "valuation_rerating": 42, "capital_allocation": 28, "information_confidence": 70, "simulated_total": 61.2, "simulated_stage": "Stage4B-LocalWatch", "profile_error": "Order growth alone can create a tradable MFE burst, but Stage3 persistence fails without margin/working-capital bridge; local 4B cap required after the fast peak."}
{"case_id": "C05_V117_002150_DOHWA_IR_ENGINEERING_EPC_O_AND_M_20240618", "symbol": "002150", "company": "도화엔지니어링", "eps_fcf_explosion": 35, "earnings_visibility": 52, "bottleneck_pricing": 34, "market_mispricing": 44, "valuation_rerating": 35, "capital_allocation": 34, "information_confidence": 68, "simulated_total": 57.4, "simulated_stage": "Stage2-Actionable", "profile_error": "Stable PPA/O&M evidence should not be compressed into C05 mega-contract Stage3; keep Stage2 until backlog-to-margin catalyst appears."}
{"case_id": "C05_V117_010400_WOOJININS_CLEANROOM_GS_E_AND_C_20220817", "symbol": "010400", "company": "우진아이엔에스", "eps_fcf_explosion": 40, "earnings_visibility": 42, "bottleneck_pricing": 38, "market_mispricing": 54, "valuation_rerating": 40, "capital_allocation": 24, "information_confidence": 72, "simulated_total": 59.4, "simulated_stage": "Stage4B-LocalWatch", "profile_error": "Contract headline opened MFE, but small contract scale and high MAE require local 4B until repeated delivery/revenue/margin bridge appears."}
```

## 6. Aggregate row

```json
{
  "aggregate_id": "C05_V117_AGGREGATE",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "mixed_C05_epc_cleanroom_power_plant_order_cash_margin_holdout_v117",
  "trigger_row_count": 6,
  "calibration_usable_rows": 6,
  "representative_rows": 6,
  "positive_case_count": 3,
  "counterexample_count": 3,
  "stage4b_count": 2,
  "stage4c_count": 0,
  "current_profile_error_count": 6,
  "avg_MFE_180D_pct": 47.5565,
  "avg_MAE_180D_pct": -16.1476,
  "source_proxy_only_rows": 0,
  "evidence_url_pending_rows": 0,
  "corporate_action_contaminated_rows": 0,
  "insufficient_forward_window_rows": 0
}
```

## 7. Residual contribution summary

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C05_EPC_CONTRACT_REQUIRES_REVENUE_MARGIN_WORKING_CAPITAL_AND_CASH_COLLECTION_GATE_V117
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
current_profile_error_count: 6
positive_case_count: 3
counterexample_count: 3
```

### Proposed canonical shadow rule

```text
C05_EPC_CONTRACT_REQUIRES_REVENUE_MARGIN_WORKING_CAPITAL_AND_CASH_COLLECTION_GATE_V117
```

Rule wording:

```text
For C05, Stage2-Actionable can open on named EPC/plant/cleanroom/public-works contract evidence, but Stage3-Yellow requires at least two of: delivery/progress confirmation, revenue recognition timing, realized margin/cost-control bridge, working-capital or cash-collection improvement, or repeat customer/contract quality. If MFE opens before these bridges appear and MAE90/MAE180 breaches roughly -18% to -20%, apply local Stage4B watch rather than full Stage3 persistence.
```

## 8. Shadow weight suggestion

```json
{
  "shadow_weight_id": "C05_V117_EPC_MARGIN_CASH_GATE",
  "scope": "canonical_archetype_specific",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "do_not_apply_now": true,
  "suggested_component_delta": {
    "earnings_visibility": "+2 when revenue-recognition timing is explicit",
    "information_confidence": "+2 when contract counterparty, amount, period and delivery scope are all explicit",
    "valuation_rerating": "cap at Stage2 if working-capital/cash-collection bridge is absent",
    "market_mispricing": "allow local 4B overlay when fast MFE is followed by MAE90/MAE180 breach"
  },
  "guardrail": "Do not promote C05 to Stage3-Green on contract headline alone; require margin/cash bridge or shallow MAE confirmation."
}
```

## 9. Validation scope

```yaml
uses_stock_web_actual_ohlcv: true
uses_no_repeat_index_as_ledger_only: true
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
complete_30_90_180_mfe_mae_in_every_trigger_row: true
trigger_rows_missing_required_price_fields: 0
entry_price_missing_rows: 0
entry_date_missing_rows: 0
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for Songdaiki/stock_agent. Do not treat this single MD as a production patch by itself. Ingest this V12 result with the other files under docs/round using the existing v12 calibration pipeline. Validate machine-readable trigger rows, deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date, and only consider the proposed C05 shadow rule if the aggregate remains representative after batch dedupe. Preserve production scoring until the normal batch promotion process emits an apply_next_patch decision.
```

## 11. Batch Ingest Self-Audit

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

## 12. Next research state

```text
completed_round = R1
completed_loop = 117
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C05 quality holdout after current-session C05 fills
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path | C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_or_cash_collection_path
```
