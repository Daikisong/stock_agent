# E2R Stock-Web v12 Residual Research — R2 / L2 / C10 Memory Recovery Equipment Cycle

```text
selected_round: R2
selected_loop: 206
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_MEMORY_MATERIALS_CONSUMABLES_AND_TEST_INTERFACE_CONVERSION_GATE_V6

loop_objective:
C10 안에서 기존 top-symbol memory equipment 반복을 피하고,
semiconductor materials / consumables / test-interface suppliers의
issuer-level order·revenue·margin conversion과 product-profile-only evidence를 분리한다.

production_scoring_changed: false
shadow_weight_only: true
```

## 1. Execution Basis

This research file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`: no `stock_agent` source-code access, no live scan, no production patch, and mandatory Songdaiki/stock-web actual 1D OHLCV rows.

The No-Repeat Index is used only as a duplicate-avoidance and coverage ledger. It shows that all C01~C32 archetypes are above 80 rows and the next work is quality repair rather than raw row filling. C10 remains a Priority 1 target for early memory-cycle false positives and supplier order conversion.

## 2. Stock-Web Price Atlas Validation

```text
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_columns: d,o,h,l,c,v,a,mc,s,m
profile_checked: true
corporate_action_180D_overlap_count: 0
insufficient_forward_window_count: 0
```

## 3. Novelty / No-Repeat Check

```text
new_independent_case_count: 6
reused_case_count: 0
new_symbol_count: 6
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 4
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 4
current_profile_error_count: 4
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
new_independent_case_ratio: 1.00
```

Diversity summary: this loop avoids the current C10 top-symbol cluster (`240810`, `084370`, `095610`, `036930`, `319660`, `166090`) and instead uses six suppliers from materials, quartzware, chemicals, probe-card/test-interface, and scrubber/chiller equipment. The failure axis is not “memory recovery is early”; it is whether the row contains an issuer-level second bridge.

## 4. Evidence Matrix

| symbol | company | role | evidence family | evidence summary | source |
|---|---|---|---|---|---|
| 104830 | Wonik Materials | positive_control_with_high_MFE | official_financial_recovery_semiconductor_special_gas | 2024 annual financials show operating profit recovering from KRW24.7bn in 2023 to KRW51.9bn in 2024, with semiconductor special-gas exposure. This is issuer-level conversion evidence, not only customer memory beta. | https://www.wimco.co.kr/en/ir/financial |
| 357780 | Soulbrain | guarded_positive_high_MAE | nand_recovery_material_demand_bridge | Mirae Asset’s March 2024 semiconductor note was positive on Soulbrain because NAND was on a recovery trajectory; company financials later show 2024 OP above 2023. The evidence is a material-demand bridge, but high 180D MAE makes Green unsafe. | https://securities.miraeasset.com/bbs/download/2124787.pdf?attachmentId=2124787 |
| 074600 | Wonik QnC | profile_financial_cap_counterexample | quartzware_financial_profile_without_customer_order | Wonik QnC is a quartz/ceramic wafer-process supplier and its financial profile confirms semiconductor exposure, but the selected evidence does not give named customer order, shipment, or margin-conversion bridge. Cap at Stage2 despite later 180D MFE. | https://www.wonikqnc.com/en/investment/financial.php |
| 014680 | Hansol Chemical | overhard_4c_counterexample | customer_capex_cut_recovery_delay | Kiwoom/Asiae reported delayed earnings recovery and lowered target price because Samsung Electronics was expected to reduce semiconductor capex in 2025. The negative evidence is real, but later 180D MFE argues against sticky hard 4C without issuer-level order/margin collapse. | https://www.asiae.co.kr/en/article/2024111908182310032 |
| 131290 | TSE | product_pipeline_only_false_positive | memory_test_interface_product_pipeline | TSE’s 2024 IR material describes high-speed memory-device test interface capability and memory probe-card exposure. The evidence is relevant but product-roadmap oriented, with no named order or revenue conversion in this trigger window. | https://files-scs.pstatic.net/2024/09/02/nqmg6IpTkv/%ED%8B%B0%EC%97%90%EC%8A%A4%EC%9D%B4%2024%EB%85%848%EC%9B%94%20IR%EC%9E%90%EB%A3%8C.pdf |
| 036200 | UNISEM | sector_beta_profile_only_high_MAE | sector_recovery_plus_equipment_profile_without_issuer_order | SEMI reported Q1 2024 semiconductor manufacturing improvement and UNISEM is a gas-scrubber/chiller equipment supplier. But this trigger is sector beta plus equipment profile, not issuer order conversion; subsequent 180D MAE confirms profile-only rows need 4B/watch cap. | https://www.semi.org/en/resources/member-directory/unisem-co-ltd |

## 5. Actual 1D OHLCV Forward Path

MFE/MAE are calculated from the stock-web entry close against the max high / min low in the following 30, 90, and 180 tradable-row windows.

| symbol | company | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| 104830 | Wonik Materials | Stage2-Actionable | 2025-03-18 | 20,850 | 8.87 / -16.45 | 18.47 / -16.45 | 74.82 / -16.45 | 2025-10-10 | 2025-04-09 |
| 357780 | Soulbrain | Stage2-Actionable | 2024-03-15 | 287,500 | 12.00 / -2.78 | 24.70 / -12.35 | 24.70 / -44.49 | 2024-05-28 | 2024-12-09 |
| 074600 | Wonik QnC | Stage2 | 2025-03-18 | 20,350 | 5.90 / -25.06 | 5.90 / -25.06 | 36.86 / -25.06 | 2025-10-10 | 2025-04-09 |
| 014680 | Hansol Chemical | Stage4C | 2024-11-19 | 107,100 | 1.96 / -16.06 | 38.28 / -18.77 | 74.88 / -18.77 | 2025-07-30 | 2025-02-03 |
| 131290 | TSE | Stage2 | 2024-09-02 | 48,550 | 12.26 / -16.89 | 15.35 / -27.91 | 15.35 / -27.91 | 2024-10-25 | 2024-12-09 |
| 036200 | UNISEM | Stage4B | 2024-05-14 | 9,770 | 26.71 / -2.87 | 27.74 / -37.87 | 27.74 / -46.67 | 2024-07-04 | 2024-12-09 |

## 6. Case Notes

### 104830 Wonik Materials — Stage2-Actionable
2024 annual financials give issuer-level conversion evidence: operating profit recovered materially from the prior year. Because this is not merely memory beta, Stage2-Actionable is preserved. However, C10 Green still needs repeat order, shipment, or cashflow confirmation.

### 357780 Soulbrain — Stage2-Actionable with Green Brake
The evidence combines NAND/material demand recovery and issuer financial improvement. The stock path still suffered a deep 180D MAE, so this is a clean example of “valid Actionable, unsafe Green.”

### 074600 Wonik QnC — Stage2 Cap
Quartzware exposure is real and the 180D path eventually worked. But the evidence lacks a named customer, order, shipment, or margin-recognition bridge in the trigger window. That makes it a Stage2 cap rather than Actionable.

### 014680 Hansol Chemical — Stage4C Stress, Demote-to-4B Candidate
The capex-cut/delayed-recovery evidence is negative. Yet the later price path recovered strongly. C10 should not make hard 4C sticky unless the issuer-level order, margin, or customer thesis actually breaks.

### 131290 TSE — Product Pipeline Only
The 2024 IR material supports relevance to high-speed memory testing, but it is product-roadmap evidence. Without named order or recognized revenue, the correct route is Stage2 cap.

### 036200 UNISEM — Profile-Only / Sector-Beta 4B
UNISEM has semiconductor scrubber/chiller exposure and the macro semiconductor manufacturing cycle improved in 1Q24. But this trigger has no issuer-level order conversion. The later deep MAE supports a 4B/watch cap.

## 7. Residual Contribution

```text
loop_contribution_label: canonical_archetype_rule_candidate
existing_axis_tested:
- stage2_required_bridge
- local_4b_watch_guard
- hard_4c_confirmation
- stage3_green_not_loosened

existing_axis_strengthened:
- stage2_required_bridge
- stage3_green_not_loosened

existing_axis_weakened:
- none

new_axis_proposed:
- no_global_axis

sector_specific_rule_candidate:
L2_MEMORY_SUPPLIER_LEVEL_CONVERSION_GATE_V6

canonical_archetype_rule_candidate:
C10_MATERIALS_CONSUMABLES_TEST_INTERFACE_SECOND_BRIDGE_GATE_V6
```

### Rule Candidate

```text
C10_MEMORY_MATERIALS_CONSUMABLES_TEST_INTERFACE_SECOND_BRIDGE_GATE_V6

- Customer-level memory recovery, DRAM/NAND/HBM macro recovery, or product-profile exposure alone cannot create Stage2-Actionable or Stage3-Yellow.
- Stage2-Actionable requires at least one issuer-level second bridge:
  supplier order, recognized revenue, shipment, named customer route,
  qualification/adoption, margin conversion, or repeat reorder.
- Financial recovery can act as a second bridge only when tied to semiconductor material/component demand, not when it is generic annual recovery.
- High MAE on a valid direct-bridge row blocks Yellow/Green first; it does not erase Stage2-Actionable.
- Product roadmap, market-size, or equipment-profile evidence remains Stage2 or local Stage4B/watch until order/revenue conversion appears.
- Hard Stage4C requires confirmed customer capex pushout, order cancellation, revenue/margin collapse, or weak offset quality; capex-cut language alone should not be sticky hard 4C.
```

This loop adds 6 new independent cases, 4 counterexamples, and 4 residual errors for R2/L2/C10.

## 8. Machine-readable JSONL Trigger Rows

```jsonl
{"MAE_180D_pct": -16.45, "MAE_30D_pct": -16.45, "MAE_90D_pct": -16.45, "MFE_180D_pct": 74.82, "MFE_30D_pct": 8.87, "MFE_90D_pct": 18.47, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_206_104830_20250318_stage2a", "case_role": "positive_control_with_high_MFE", "company_name": "Wonik Materials", "corporate_action_window_status": "clear_180D_no_candidate_overlap", "current_profile_expected": "Stage2-Actionable / guarded Stage3-Yellow candidate", "dedupe_for_aggregate": true, "entry_date": "2025-03-18", "entry_high": 21900.0, "entry_low": 20700.0, "entry_open": 21850.0, "entry_price": 20850.0, "entry_volume": 101008, "evidence_date": "2025-03-18", "evidence_family": "official_financial_recovery_semiconductor_special_gas", "fine_archetype_id": "C10_MEMORY_MATERIALS_CONSUMABLES_AND_TEST_INTERFACE_CONVERSION_GATE_V6", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_180D_date": "2025-10-10", "peak_30D_date": "2025-03-20", "peak_90D_date": "2025-07-29", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard": "atlas/ohlcv_tradable_by_symbol_year/104/104830/2025.csv", "production_scoring_changed": false, "profile_path": "atlas/symbol_profiles/104/104830.json", "raw_component_score_breakdown": {"bottleneck_pricing": 13, "capital_allocation": 5, "earnings_visibility": 17, "eps_fcf_explosion": 17, "information_confidence": 15, "market_mispricing": 11, "valuation_rerating": 9}, "research_file": "e2r_stock_web_v12_residual_round_R2_loop_206_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "residual_contribution": "Stage2-Actionable is preserved; Yellow/Green still need repeat order or cashflow bridge.", "row_type": "trigger", "same_entry_group_id": "C10|104830|Stage2-Actionable|2025-03-18", "score_total_current_proxy": 87, "selected_loop": 206, "selected_round": "R2", "shadow_weight_only": true, "source_quality": "direct_company_financial_page", "source_url": "https://www.wimco.co.kr/en/ir/financial", "symbol": "104830", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-04-09", "trough_30D_date": "2025-04-09", "trough_90D_date": "2025-04-09"}
{"MAE_180D_pct": -44.49, "MAE_30D_pct": -2.78, "MAE_90D_pct": -12.35, "MFE_180D_pct": 24.7, "MFE_30D_pct": 12.0, "MFE_90D_pct": 24.7, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_206_357780_20240315_stage2a", "case_role": "guarded_positive_high_MAE", "company_name": "Soulbrain", "corporate_action_window_status": "clear_180D_no_candidate_overlap", "current_profile_expected": "Stage2-Actionable, Green blocked by high-MAE", "dedupe_for_aggregate": true, "entry_date": "2024-03-15", "entry_high": 291500.0, "entry_low": 282500.0, "entry_open": 288500.0, "entry_price": 287500.0, "entry_volume": 30456, "evidence_date": "2024-03-15", "evidence_family": "nand_recovery_material_demand_bridge", "fine_archetype_id": "C10_MEMORY_MATERIALS_CONSUMABLES_AND_TEST_INTERFACE_CONVERSION_GATE_V6", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_180D_date": "2024-05-28", "peak_30D_date": "2024-03-21", "peak_90D_date": "2024-05-28", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard": "atlas/ohlcv_tradable_by_symbol_year/357/357780/2024.csv", "production_scoring_changed": false, "profile_path": "atlas/symbol_profiles/357/357780.json", "raw_component_score_breakdown": {"bottleneck_pricing": 13, "capital_allocation": 4, "earnings_visibility": 16, "eps_fcf_explosion": 14, "information_confidence": 16, "market_mispricing": 11, "valuation_rerating": 9}, "research_file": "e2r_stock_web_v12_residual_round_R2_loop_206_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "residual_contribution": "Valid Stage2-Actionable bridge but MAE shows memory-material rows require Green brake.", "row_type": "trigger", "same_entry_group_id": "C10|357780|Stage2-Actionable|2024-03-15", "score_total_current_proxy": 83, "selected_loop": 206, "selected_round": "R2", "shadow_weight_only": true, "source_quality": "direct_broker_pdf_with_issuer_material_bridge", "source_url": "https://securities.miraeasset.com/bbs/download/2124787.pdf?attachmentId=2124787", "symbol": "357780", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-12-09", "trough_30D_date": "2024-04-22", "trough_90D_date": "2024-07-25"}
{"MAE_180D_pct": -25.06, "MAE_30D_pct": -25.06, "MAE_90D_pct": -25.06, "MFE_180D_pct": 36.86, "MFE_30D_pct": 5.9, "MFE_90D_pct": 5.9, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_206_074600_20250318_stage2", "case_role": "profile_financial_cap_counterexample", "company_name": "Wonik QnC", "corporate_action_window_status": "clear_180D_no_candidate_overlap", "current_profile_expected": "Stage2 cap", "dedupe_for_aggregate": true, "entry_date": "2025-03-18", "entry_high": 21150.0, "entry_low": 20100.0, "entry_open": 21150.0, "entry_price": 20350.0, "entry_volume": 256682, "evidence_date": "2025-03-18", "evidence_family": "quartzware_financial_profile_without_customer_order", "fine_archetype_id": "C10_MEMORY_MATERIALS_CONSUMABLES_AND_TEST_INTERFACE_CONVERSION_GATE_V6", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_180D_date": "2025-10-10", "peak_30D_date": "2025-03-21", "peak_90D_date": "2025-03-21", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard": "atlas/ohlcv_tradable_by_symbol_year/074/074600/2025.csv", "production_scoring_changed": false, "profile_path": "atlas/symbol_profiles/074/074600.json", "raw_component_score_breakdown": {"bottleneck_pricing": 12, "capital_allocation": 4, "earnings_visibility": 13, "eps_fcf_explosion": 12, "information_confidence": 13, "market_mispricing": 12, "valuation_rerating": 8}, "research_file": "e2r_stock_web_v12_residual_round_R2_loop_206_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "residual_contribution": "Profile/financial exposure can be true but not Actionable without customer or order route.", "row_type": "trigger", "same_entry_group_id": "C10|074600|Stage2|2025-03-18", "score_total_current_proxy": 74, "selected_loop": 206, "selected_round": "R2", "shadow_weight_only": true, "source_quality": "direct_company_financial_page_but_no_triggered_order", "source_url": "https://www.wonikqnc.com/en/investment/financial.php", "symbol": "074600", "trigger_type": "Stage2", "trough_180D_date": "2025-04-09", "trough_30D_date": "2025-04-09", "trough_90D_date": "2025-04-09"}
{"MAE_180D_pct": -18.77, "MAE_30D_pct": -16.06, "MAE_90D_pct": -18.77, "MFE_180D_pct": 74.88, "MFE_30D_pct": 1.96, "MFE_90D_pct": 38.28, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_206_014680_20241119_stage4c_stress", "case_role": "overhard_4c_counterexample", "company_name": "Hansol Chemical", "corporate_action_window_status": "clear_180D_no_candidate_overlap", "current_profile_expected": "Stage4C stress / should demote to Stage4B-watch if offset appears", "dedupe_for_aggregate": true, "entry_date": "2024-11-19", "entry_high": 108300.0, "entry_low": 103000.0, "entry_open": 104600.0, "entry_price": 107100.0, "entry_volume": 43948, "evidence_date": "2024-11-19", "evidence_family": "customer_capex_cut_recovery_delay", "fine_archetype_id": "C10_MEMORY_MATERIALS_CONSUMABLES_AND_TEST_INTERFACE_CONVERSION_GATE_V6", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_180D_date": "2025-07-30", "peak_30D_date": "2024-11-20", "peak_90D_date": "2025-03-18", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard": "atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv", "production_scoring_changed": false, "profile_path": "atlas/symbol_profiles/014/014680.json", "raw_component_score_breakdown": {"bottleneck_pricing": 7, "capital_allocation": 4, "earnings_visibility": 8, "eps_fcf_explosion": 6, "information_confidence": 18, "market_mispricing": 9, "valuation_rerating": 7}, "research_file": "e2r_stock_web_v12_residual_round_R2_loop_206_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "residual_contribution": "Customer capex cut language is not enough for sticky hard 4C when forward path recovers.", "row_type": "trigger", "same_entry_group_id": "C10|014680|Stage4C|2024-11-19", "score_total_current_proxy": 59, "selected_loop": 206, "selected_round": "R2", "shadow_weight_only": true, "source_quality": "direct_news_report_on_broker_downgrade", "source_url": "https://www.asiae.co.kr/en/article/2024111908182310032", "symbol": "014680", "trigger_type": "Stage4C", "trough_180D_date": "2025-02-03", "trough_30D_date": "2024-12-09", "trough_90D_date": "2025-02-03"}
{"MAE_180D_pct": -27.91, "MAE_30D_pct": -16.89, "MAE_90D_pct": -27.91, "MFE_180D_pct": 15.35, "MFE_30D_pct": 12.26, "MFE_90D_pct": 15.35, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_206_131290_20240902_stage2", "case_role": "product_pipeline_only_false_positive", "company_name": "TSE", "corporate_action_window_status": "clear_180D_no_candidate_overlap", "current_profile_expected": "Stage2 cap", "dedupe_for_aggregate": true, "entry_date": "2024-09-02", "entry_high": 49400.0, "entry_low": 48050.0, "entry_open": 49300.0, "entry_price": 48550.0, "entry_volume": 53200, "evidence_date": "2024-09-02", "evidence_family": "memory_test_interface_product_pipeline", "fine_archetype_id": "C10_MEMORY_MATERIALS_CONSUMABLES_AND_TEST_INTERFACE_CONVERSION_GATE_V6", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_180D_date": "2024-10-25", "peak_30D_date": "2024-10-14", "peak_90D_date": "2024-10-25", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard": "atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv", "production_scoring_changed": false, "profile_path": "atlas/symbol_profiles/131/131290.json", "raw_component_score_breakdown": {"bottleneck_pricing": 14, "capital_allocation": 4, "earnings_visibility": 11, "eps_fcf_explosion": 10, "information_confidence": 15, "market_mispricing": 11, "valuation_rerating": 8}, "research_file": "e2r_stock_web_v12_residual_round_R2_loop_206_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "residual_contribution": "Product capability alone should not become Actionable until order/revenue conversion appears.", "row_type": "trigger", "same_entry_group_id": "C10|131290|Stage2|2024-09-02", "score_total_current_proxy": 73, "selected_loop": 206, "selected_round": "R2", "shadow_weight_only": true, "source_quality": "direct_company_ir_product_material", "source_url": "https://files-scs.pstatic.net/2024/09/02/nqmg6IpTkv/%ED%8B%B0%EC%97%90%EC%8A%A4%EC%9D%B4%2024%EB%85%848%EC%9B%94%20IR%EC%9E%90%EB%A3%8C.pdf", "symbol": "131290", "trigger_type": "Stage2", "trough_180D_date": "2024-12-09", "trough_30D_date": "2024-09-09", "trough_90D_date": "2024-12-09"}
{"MAE_180D_pct": -46.67, "MAE_30D_pct": -2.87, "MAE_90D_pct": -37.87, "MFE_180D_pct": 27.74, "MFE_30D_pct": 26.71, "MFE_90D_pct": 27.74, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "case_id": "C10_206_036200_20240514_stage4b", "case_role": "sector_beta_profile_only_high_MAE", "company_name": "UNISEM", "corporate_action_window_status": "clear_180D_no_candidate_overlap", "current_profile_expected": "Stage4B watch / Stage2 cap", "dedupe_for_aggregate": true, "entry_date": "2024-05-14", "entry_high": 9880.0, "entry_low": 9490.0, "entry_open": 9580.0, "entry_price": 9770.0, "entry_volume": 703602, "evidence_date": "2024-05-14", "evidence_family": "sector_recovery_plus_equipment_profile_without_issuer_order", "fine_archetype_id": "C10_MEMORY_MATERIALS_CONSUMABLES_AND_TEST_INTERFACE_CONVERSION_GATE_V6", "forward_window_trading_days": 180, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "peak_180D_date": "2024-07-04", "peak_30D_date": "2024-05-29", "peak_90D_date": "2024-07-04", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard": "atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv", "production_scoring_changed": false, "profile_path": "atlas/symbol_profiles/036/036200.json", "raw_component_score_breakdown": {"bottleneck_pricing": 11, "capital_allocation": 4, "earnings_visibility": 10, "eps_fcf_explosion": 8, "information_confidence": 13, "market_mispricing": 12, "valuation_rerating": 8}, "research_file": "e2r_stock_web_v12_residual_round_R2_loop_206_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md", "residual_contribution": "Macro manufacturing recovery + supplier profile is insufficient for Actionable and produces high MAE.", "row_type": "trigger", "same_entry_group_id": "C10|036200|Stage4B|2024-05-14", "score_total_current_proxy": 66, "selected_loop": 206, "selected_round": "R2", "shadow_weight_only": true, "source_quality": "direct_industry_member_profile_plus_macro_sector_context", "source_url": "https://www.semi.org/en/resources/member-directory/unisem-co-ltd", "symbol": "036200", "trigger_type": "Stage4B", "trough_180D_date": "2024-12-09", "trough_30D_date": "2024-05-14", "trough_90D_date": "2024-09-19"}
```

## 9. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff during the research run.

When applying this batch later, parse this MD as a v12 result file. Validate the JSONL rows, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and treat any delta as shadow-only until aggregate validation confirms it. Candidate patch scope is C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE and L2_AI_SEMICONDUCTOR_ELECTRONICS only. Do not loosen Stage3-Green globally.
```

## 11. Next Research State

```text
completed_round: R2
completed_loop: 206
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
