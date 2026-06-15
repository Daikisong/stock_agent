# E2R Stock-Web V12 Residual Research — R2 loop 113 / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
## 0. Metadata
```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "output_file": "e2r_stock_web_v12_residual_round_R2_loop_113_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md",
  "selected_round": "R2",
  "selected_loop": 113,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 1-under-50 after local-session adjustment; published index Priority 0",
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "fine_archetype_id": "C10_MEMORY_RECOVERY_TEST_AUTOMATION_MATERIALS_SERVICE_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_BETA",
  "deep_sub_archetype_id": "C10_DEEP_MEMORY_TESTER_WAFER_TRANSFER_METROLOGY_OSAT_MATERIAL_SERVICE_RECOVERY_VS_LATE_CYCLE_RS_FADE",
  "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery",
  "price_data_source": "Songdaiki/stock-web",
  "upstream_source": "FinanceData/marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false,
  "stock_agent_code_accessed": false,
  "stock_agent_code_patch_written": false
}
```
## 1. Coverage-index selection

The published No-Repeat Index still lists `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` as a Priority 0 under-covered archetype with 13 representative rows, 17 rows short of the 30-row stability band and 37 rows short of the 50-row practical calibration band. In this running session, C10 loops 109/110/111/112 locally added about 23 representative triggers, so the local-session adjusted estimate before this run was about 36. This loop adds 7 more representative triggers, moving local C10 coverage to about 43: above the 30-row stability band but still below the 50-row practical calibration band.

Round is derived from the selected canonical, not from a mechanical R1→R13 rotation: `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` maps to `R2` / `L2_AI_SEMICONDUCTOR_ELECTRONICS`. No R13 or wrong-sector filename is used.
## 2. Stock-Web manifest and validation scope

Price rows use the Stock-Web atlas convention:

- `primary_price_source = Songdaiki/stock-web`
- `upstream_source = FinanceData/marcap`
- `price_basis = tradable_raw`
- `price_adjustment_status = raw_unadjusted_marcap`
- `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`
- `manifest_max_date = 2026-02-20`

Calculation convention: `entry_price` is the `c` close on `entry_date`. MFE/MAE windows use the 30/90/180 tradable rows starting at the entry row. Candidate windows with a share-count change inside the selected 180D path were not emitted as usable trigger rows.
## 3. Case table
| # | symbol | name | trigger | entry | entry price | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | outcome | residual read |
|---:|---|---|---|---|---:|---:|---:|---:|---|---|
| 1 | `089890` | 코세스 | `Stage2-Actionable` | 2025-01-15 | 7160 | 34.08/-10.34 | 34.08/-16.20 | 209.36/-16.20 | positive | too_late_if_stage2_requires_direct_equipment_order_only |
| 2 | `160980` | 싸이맥스 | `Stage2-Actionable` | 2025-01-15 | 9570 | 43.36/-3.76 | 43.36/-3.76 | 101.67/-3.76 | positive | missed_structural_recovery_if_wafer_transfer_bridge_is_underweighted |
| 3 | `322310` | 오로스테크놀로지 | `Stage2` | 2024-11-15 | 13810 | 30.99/-4.56 | 91.17/-4.56 | 91.17/-4.56 | positive | too_late_after_inventory_reset |
| 4 | `357780` | 솔브레인 | `Stage2` | 2025-01-15 | 174500 | 17.77/-7.97 | 24.07/-11.17 | 74.79/-11.17 | positive | missed_material_bridge_if_only_equipment_orders_counted |
| 5 | `089030` | 테크윙 | `Stage4B` | 2025-01-15 | 45450 | 15.51/-21.56 | 15.51/-41.91 | 42.13/-42.68 | counterexample | false_positive_if_price_RS_or_HBM_label_overrides_high_MAE |
| 6 | `092870` | 엑시콘 | `Stage4B` | 2025-01-15 | 12700 | 24.09/-11.10 | 24.09/-22.91 | 45.43/-26.38 | counterexample | false_positive_if_tester_beta_accepted_without_MAE_guard |
| 7 | `036540` | SFA반도체 | `Stage2` | 2024-11-15 | 3150 | 7.78/-10.48 | 22.70/-10.48 | 22.70/-19.05 | counterexample | false_positive_if_OSAT_proxy_counts_as_equipment_cycle_without_order_bridge |

## 4. Interpretation

C10 is not a simple “memory stocks up = equipment cycle confirmed” bucket. The cases separate three different engines:

1. **Clean bridge positives** — `089890`, `160980`, `322310`, `357780` had either order/revenue bridge, inventory-reset recovery, or material shipment bridge with controlled MAE. These are the paths where C10 can allow Stage2-Actionable or Stage2 before a broad analyst consensus catches up.
2. **Late-cycle beta false positives** — `089030`, `092870`, `036540` show why C10 should not treat tester/OSAT labels as direct equipment-cycle confirmation. MFE can appear, but the path either draws down too deeply or fails to prove a durable order/revenue/margin bridge.
3. **4B local-watch boundary** — the two `Stage4B` rows are not “avoid all HBM/memory testers” rules. They say: when price relative strength leads the evidence and MAE90 crosses roughly -20% to -40%, keep the case at local 4B watch until non-price order/revenue bridge catches up.

Aggregate path: average MFE90 is `36.43%`, average MAE90 is `-15.86%`, average MFE180 is `83.89%`, and average MAE180 is `-17.69%`. That spread is exactly the residual C10 problem: 180D upside exists, but a generic memory-recovery label lets too many high-MAE entries through.
## 5. Residual contribution summary
```json
{
  "new_independent_case_count": 7,
  "reused_case_count": 0,
  "new_symbol_count": 7,
  "same_archetype_new_symbol_count": 7,
  "same_archetype_new_trigger_family_count": 7,
  "new_trigger_family_count": 7,
  "calibration_usable_trigger_count": 7,
  "representative_trigger_count": 7,
  "positive_case_count": 4,
  "counterexample_count": 3,
  "stage4b_case_count": 2,
  "stage4c_case_count": 0,
  "current_profile_error_count": 7,
  "source_proxy_only_count": 7,
  "evidence_url_pending_count": 7,
  "promotion_blocked_until_url_repair": true,
  "diversity_score_summary": "7 symbols / 7 trigger families / positive-counterexample balance 4:3 / tester, wafer-transfer, metrology, OSAT, bonding, wet-chemical/material routes separated; cross-canonical symbol reuse is allowed but same C10 symbol-date trigger duplicates are not used.",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "auto_selected_coverage_gap": "C10 base index 13 + local loops 109/110/111/112 about 23 + loop113 7 = about 43; still about 7 short of 50-row practical calibration band"
}
```
## 6. Shadow rule candidate
```json
{
  "row_type": "shadow_rule_candidate",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "rule_id": "C10_memory_recovery_bridge_before_Yellow_and_late_cycle_MAE_to_4B_watch_v3",
  "new_axis_proposed": "C10_verified_order_revenue_margin_or_inventory_reset_bridge_required_before_Yellow_or_Green_plus_late_cycle_memory_beta_MAE_guard",
  "existing_axis_tested": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_weakened": [],
  "proposed_behavior": "For C10, direct order/revenue/margin bridge or clean inventory-reset recovery can unlock Stage2/Stage2-Actionable. Tester/OSAT/material proxy labels without bridge stay at watch; if MAE90 <= -20% or post-peak RS fade appears, route to local 4B watch rather than positive Stage3.",
  "do_not_apply_now": true,
  "requires_url_repair_before_promotion": true
}
```
## 7. Machine-readable trigger rows JSONL
```jsonl
{"row_type":"trigger","case_id":"C10_L113_01_089890","symbol":"089890","company_name":"코세스","selected_round":"R2","selected_loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_TEST_AUTOMATION_MATERIALS_SERVICE_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_BETA","deep_sub_archetype_id":"C10_DEEP_MEMORY_TESTER_WAFER_TRANSFER_METROLOGY_OSAT_MATERIAL_SERVICE_RECOVERY_VS_LATE_CYCLE_RS_FADE","trigger_type":"Stage2-Actionable","trigger_family":"backend_bonding_package_attach_memory_recovery","trigger_date":"2025-01-15","entry_date":"2025-01-15","entry_price":7160.0,"entry_price_basis":"entry_date_close_c","price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089890/2025.csv","forward_window_trading_days":180,"corporate_action_window_status":"not_flagged_in_loaded_tradable_180D_window","share_count_change_in_180D":false,"calibration_usable":true,"calibration_usable_reason":"entry row and 180 forward tradable rows available; no share-count change in selected 180D window in loaded tradable shard","dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|089890|Stage2-Actionable|2025-01-15","reuse_reason":"cross_canonical_or_same_symbol_allowed_only_if_new_trigger_family; no same C10 symbol-date trigger duplicate used in this MD","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable_without_url_repair":false,"thesis_summary":"backend bonding/package attach proxy recovered only when 2025 order/revenue confirmation followed the memory recovery wave","MFE_30D_pct":34.08,"MAE_30D_pct":-10.34,"peak_30D_date":"2025-02-19","trough_30D_date":"2025-02-03","MFE_90D_pct":34.08,"MAE_90D_pct":-16.2,"peak_90D_date":"2025-02-19","trough_90D_date":"2025-04-09","MFE_180D_pct":209.36,"MAE_180D_pct":-16.2,"peak_180D_date":"2025-10-14","trough_180D_date":"2025-04-09","case_outcome_label":"positive","current_profile_error_type":"too_late_if_stage2_requires_direct_equipment_order_only","component_scores_current_proxy":{"growth_revision":55,"order_revenue_bridge":66,"margin_fcf_bridge":58,"valuation_risk_inverse":50,"evidence_quality":45,"price_path_confirmation":74,"red_team_risk_inverse":52},"current_proxy_score_simulation":57.14,"suggested_shadow_action":"allow_Stage2_Actionable_after_verified_bridge"}
{"row_type":"trigger","case_id":"C10_L113_02_160980","symbol":"160980","company_name":"싸이맥스","selected_round":"R2","selected_loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_TEST_AUTOMATION_MATERIALS_SERVICE_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_BETA","deep_sub_archetype_id":"C10_DEEP_MEMORY_TESTER_WAFER_TRANSFER_METROLOGY_OSAT_MATERIAL_SERVICE_RECOVERY_VS_LATE_CYCLE_RS_FADE","trigger_type":"Stage2-Actionable","trigger_family":"wafer_transfer_automation_memory_recovery","trigger_date":"2025-01-15","entry_date":"2025-01-15","entry_price":9570.0,"entry_price_basis":"entry_date_close_c","price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/160/160980/2025.csv","forward_window_trading_days":180,"corporate_action_window_status":"not_flagged_in_loaded_tradable_180D_window","share_count_change_in_180D":false,"calibration_usable":true,"calibration_usable_reason":"entry row and 180 forward tradable rows available; no share-count change in selected 180D window in loaded tradable shard","dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|160980|Stage2-Actionable|2025-01-15","reuse_reason":"cross_canonical_or_same_symbol_allowed_only_if_new_trigger_family; no same C10 symbol-date trigger duplicate used in this MD","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable_without_url_repair":false,"thesis_summary":"wafer-transfer automation entered a clean recovery band with limited drawdown; order/revenue bridge should unlock Stage2-Actionable","MFE_30D_pct":43.36,"MAE_30D_pct":-3.76,"peak_30D_date":"2025-02-05","trough_30D_date":"2025-02-03","MFE_90D_pct":43.36,"MAE_90D_pct":-3.76,"peak_90D_date":"2025-02-05","trough_90D_date":"2025-02-03","MFE_180D_pct":101.67,"MAE_180D_pct":-3.76,"peak_180D_date":"2025-10-10","trough_180D_date":"2025-02-03","case_outcome_label":"positive","current_profile_error_type":"missed_structural_recovery_if_wafer_transfer_bridge_is_underweighted","component_scores_current_proxy":{"growth_revision":55,"order_revenue_bridge":66,"margin_fcf_bridge":58,"valuation_risk_inverse":50,"evidence_quality":45,"price_path_confirmation":74,"red_team_risk_inverse":52},"current_proxy_score_simulation":57.14,"suggested_shadow_action":"allow_Stage2_Actionable_after_verified_bridge"}
{"row_type":"trigger","case_id":"C10_L113_03_322310","symbol":"322310","company_name":"오로스테크놀로지","selected_round":"R2","selected_loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_TEST_AUTOMATION_MATERIALS_SERVICE_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_BETA","deep_sub_archetype_id":"C10_DEEP_MEMORY_TESTER_WAFER_TRANSFER_METROLOGY_OSAT_MATERIAL_SERVICE_RECOVERY_VS_LATE_CYCLE_RS_FADE","trigger_type":"Stage2","trigger_family":"overlay_metrology_inventory_reset_recovery","trigger_date":"2024-11-15","entry_date":"2024-11-15","entry_price":13810.0,"entry_price_basis":"entry_date_close_c","price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","forward_window_trading_days":180,"corporate_action_window_status":"not_flagged_in_loaded_tradable_180D_window","share_count_change_in_180D":false,"calibration_usable":true,"calibration_usable_reason":"entry row and 180 forward tradable rows available; no share-count change in selected 180D window in loaded tradable shard","dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|322310|Stage2|2024-11-15","reuse_reason":"cross_canonical_or_same_symbol_allowed_only_if_new_trigger_family; no same C10 symbol-date trigger duplicate used in this MD","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable_without_url_repair":false,"thesis_summary":"overlay/metrology was a late-2024 reset-to-recovery case; price path rewarded the reset only after valuation washout","MFE_30D_pct":30.99,"MAE_30D_pct":-4.56,"peak_30D_date":"2024-12-17","trough_30D_date":"2024-11-15","MFE_90D_pct":91.17,"MAE_90D_pct":-4.56,"peak_90D_date":"2025-02-19","trough_90D_date":"2024-11-15","MFE_180D_pct":91.17,"MAE_180D_pct":-4.56,"peak_180D_date":"2025-02-19","trough_180D_date":"2024-11-15","case_outcome_label":"positive","current_profile_error_type":"too_late_after_inventory_reset","component_scores_current_proxy":{"growth_revision":55,"order_revenue_bridge":66,"margin_fcf_bridge":58,"valuation_risk_inverse":50,"evidence_quality":45,"price_path_confirmation":74,"red_team_risk_inverse":52},"current_proxy_score_simulation":57.14,"suggested_shadow_action":"allow_Stage2_Actionable_after_verified_bridge"}
{"row_type":"trigger","case_id":"C10_L113_04_357780","symbol":"357780","company_name":"솔브레인","selected_round":"R2","selected_loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_TEST_AUTOMATION_MATERIALS_SERVICE_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_BETA","deep_sub_archetype_id":"C10_DEEP_MEMORY_TESTER_WAFER_TRANSFER_METROLOGY_OSAT_MATERIAL_SERVICE_RECOVERY_VS_LATE_CYCLE_RS_FADE","trigger_type":"Stage2","trigger_family":"wet_chemical_material_shipment_memory_bridge","trigger_date":"2025-01-15","entry_date":"2025-01-15","entry_price":174500.0,"entry_price_basis":"entry_date_close_c","price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/357/357780/2025.csv","forward_window_trading_days":180,"corporate_action_window_status":"not_flagged_in_loaded_tradable_180D_window","share_count_change_in_180D":false,"calibration_usable":true,"calibration_usable_reason":"entry row and 180 forward tradable rows available; no share-count change in selected 180D window in loaded tradable shard","dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|357780|Stage2|2025-01-15","reuse_reason":"cross_canonical_or_same_symbol_allowed_only_if_new_trigger_family; no same C10 symbol-date trigger duplicate used in this MD","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable_without_url_repair":false,"thesis_summary":"wet-chemical/material shipment bridge acted as a cleaner memory-cycle confirmation than generic equipment beta","MFE_30D_pct":17.77,"MAE_30D_pct":-7.97,"peak_30D_date":"2025-02-19","trough_30D_date":"2025-02-03","MFE_90D_pct":24.07,"MAE_90D_pct":-11.17,"peak_90D_date":"2025-03-17","trough_90D_date":"2025-05-27","MFE_180D_pct":74.79,"MAE_180D_pct":-11.17,"peak_180D_date":"2025-09-25","trough_180D_date":"2025-05-27","case_outcome_label":"positive","current_profile_error_type":"missed_material_bridge_if_only_equipment_orders_counted","component_scores_current_proxy":{"growth_revision":55,"order_revenue_bridge":66,"margin_fcf_bridge":58,"valuation_risk_inverse":50,"evidence_quality":45,"price_path_confirmation":74,"red_team_risk_inverse":52},"current_proxy_score_simulation":57.14,"suggested_shadow_action":"allow_Stage2_Actionable_after_verified_bridge"}
{"row_type":"trigger","case_id":"C10_L113_05_089030","symbol":"089030","company_name":"테크윙","selected_round":"R2","selected_loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_TEST_AUTOMATION_MATERIALS_SERVICE_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_BETA","deep_sub_archetype_id":"C10_DEEP_MEMORY_TESTER_WAFER_TRANSFER_METROLOGY_OSAT_MATERIAL_SERVICE_RECOVERY_VS_LATE_CYCLE_RS_FADE","trigger_type":"Stage4B","trigger_family":"memory_tester_late_cycle_rs_fade","trigger_date":"2025-01-15","entry_date":"2025-01-15","entry_price":45450.0,"entry_price_basis":"entry_date_close_c","price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2025.csv","forward_window_trading_days":180,"corporate_action_window_status":"not_flagged_in_loaded_tradable_180D_window","share_count_change_in_180D":false,"calibration_usable":true,"calibration_usable_reason":"entry row and 180 forward tradable rows available; no share-count change in selected 180D window in loaded tradable shard","dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|089030|Stage4B|2025-01-15","reuse_reason":"cross_canonical_or_same_symbol_allowed_only_if_new_trigger_family; no same C10 symbol-date trigger duplicate used in this MD","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable_without_url_repair":false,"thesis_summary":"late-cycle memory tester relative strength still carried HBM label value, but high MAE requires 4B watch unless fresh order/revenue bridge appears","MFE_30D_pct":15.51,"MAE_30D_pct":-21.56,"peak_30D_date":"2025-01-20","trough_30D_date":"2025-03-04","MFE_90D_pct":15.51,"MAE_90D_pct":-41.91,"peak_90D_date":"2025-01-20","trough_90D_date":"2025-04-09","MFE_180D_pct":42.13,"MAE_180D_pct":-42.68,"peak_180D_date":"2025-10-02","trough_180D_date":"2025-08-04","case_outcome_label":"counterexample","current_profile_error_type":"false_positive_if_price_RS_or_HBM_label_overrides_high_MAE","component_scores_current_proxy":{"growth_revision":44,"order_revenue_bridge":36,"margin_fcf_bridge":32,"valuation_risk_inverse":28,"evidence_quality":45,"price_path_confirmation":38,"red_team_risk_inverse":24},"current_proxy_score_simulation":35.29,"suggested_shadow_action":"cap_at_Stage4B_watch_until_order_revenue_margin_bridge"}
{"row_type":"trigger","case_id":"C10_L113_06_092870","symbol":"092870","company_name":"엑시콘","selected_round":"R2","selected_loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_TEST_AUTOMATION_MATERIALS_SERVICE_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_BETA","deep_sub_archetype_id":"C10_DEEP_MEMORY_TESTER_WAFER_TRANSFER_METROLOGY_OSAT_MATERIAL_SERVICE_RECOVERY_VS_LATE_CYCLE_RS_FADE","trigger_type":"Stage4B","trigger_family":"memory_tester_high_mae_beta_recovery","trigger_date":"2025-01-15","entry_date":"2025-01-15","entry_price":12700.0,"entry_price_basis":"entry_date_close_c","price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2025.csv","forward_window_trading_days":180,"corporate_action_window_status":"not_flagged_in_loaded_tradable_180D_window","share_count_change_in_180D":false,"calibration_usable":true,"calibration_usable_reason":"entry row and 180 forward tradable rows available; no share-count change in selected 180D window in loaded tradable shard","dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|092870|Stage4B|2025-01-15","reuse_reason":"cross_canonical_or_same_symbol_allowed_only_if_new_trigger_family; no same C10 symbol-date trigger duplicate used in this MD","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable_without_url_repair":false,"thesis_summary":"tester beta recovered but path carried >20% MAE, so positive MFE alone should not unlock Yellow/Green","MFE_30D_pct":24.09,"MAE_30D_pct":-11.1,"peak_30D_date":"2025-02-14","trough_30D_date":"2025-02-03","MFE_90D_pct":24.09,"MAE_90D_pct":-22.91,"peak_90D_date":"2025-02-14","trough_90D_date":"2025-04-07","MFE_180D_pct":45.43,"MAE_180D_pct":-26.38,"peak_180D_date":"2025-09-22","trough_180D_date":"2025-08-21","case_outcome_label":"counterexample","current_profile_error_type":"false_positive_if_tester_beta_accepted_without_MAE_guard","component_scores_current_proxy":{"growth_revision":44,"order_revenue_bridge":36,"margin_fcf_bridge":32,"valuation_risk_inverse":28,"evidence_quality":45,"price_path_confirmation":38,"red_team_risk_inverse":24},"current_proxy_score_simulation":35.29,"suggested_shadow_action":"cap_at_Stage4B_watch_until_order_revenue_margin_bridge"}
{"row_type":"trigger","case_id":"C10_L113_07_036540","symbol":"036540","company_name":"SFA반도체","selected_round":"R2","selected_loop":113,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_TEST_AUTOMATION_MATERIALS_SERVICE_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_BETA","deep_sub_archetype_id":"C10_DEEP_MEMORY_TESTER_WAFER_TRANSFER_METROLOGY_OSAT_MATERIAL_SERVICE_RECOVERY_VS_LATE_CYCLE_RS_FADE","trigger_type":"Stage2","trigger_family":"osat_memory_demand_proxy_without_equipment_order_bridge","trigger_date":"2024-11-15","entry_date":"2024-11-15","entry_price":3150.0,"entry_price_basis":"entry_date_close_c","price_data_source":"Songdaiki/stock-web","price_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv","forward_window_trading_days":180,"corporate_action_window_status":"not_flagged_in_loaded_tradable_180D_window","share_count_change_in_180D":false,"calibration_usable":true,"calibration_usable_reason":"entry row and 180 forward tradable rows available; no share-count change in selected 180D window in loaded tradable shard","dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|036540|Stage2|2024-11-15","reuse_reason":"cross_canonical_or_same_symbol_allowed_only_if_new_trigger_family; no same C10 symbol-date trigger duplicate used in this MD","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable_without_url_repair":false,"thesis_summary":"OSAT proxy recovered partially but lacked equipment-order conversion; this is a dull false-positive risk for C10","MFE_30D_pct":7.78,"MAE_30D_pct":-10.48,"peak_30D_date":"2024-11-27","trough_30D_date":"2024-12-09","MFE_90D_pct":22.7,"MAE_90D_pct":-10.48,"peak_90D_date":"2025-02-07","trough_90D_date":"2024-12-09","MFE_180D_pct":22.7,"MAE_180D_pct":-19.05,"peak_180D_date":"2025-02-07","trough_180D_date":"2025-04-09","case_outcome_label":"counterexample","current_profile_error_type":"false_positive_if_OSAT_proxy_counts_as_equipment_cycle_without_order_bridge","component_scores_current_proxy":{"growth_revision":44,"order_revenue_bridge":36,"margin_fcf_bridge":32,"valuation_risk_inverse":28,"evidence_quality":45,"price_path_confirmation":38,"red_team_risk_inverse":24},"current_proxy_score_simulation":35.29,"suggested_shadow_action":"cap_at_Stage4B_watch_until_order_revenue_margin_bridge"}
```
## 8. Narrative-only / rejected candidates JSONL
```jsonl
{"row_type":"narrative_only","symbol":"083450","company_name":"GST","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reason":"excluded_from_trigger_table","blocked_reason":"share_count_doubled_inside_2024_candidate_window; treat as corporate_action_or_capital_structure_contamination until profile repair","candidate_path":"C10_chiller_scrubber_memory_recovery_blowoff","calibration_usable":false}
{"row_type":"narrative_only","symbol":"036930","company_name":"주성엔지니어링","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reason":"excluded_from_trigger_table_for_early_2024_entries","blocked_reason":"loaded 2024 shard shows share_count change inside early-2024 180D windows; only later window lacked enough 180D in local 2024 shard","candidate_path":"C10_frontend_ALD_memory_capex_recovery","calibration_usable":false}
```
## 9. Batch ingest self-audit
| gate | status | note |
|---|---|---|
| `filename_matches_standard_v12_pattern` | `pass` | e2r_stock_web_v12_residual_round_R2_loop_113_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md |
| `metadata_round_loop_matches_filename` | `pass` | R2/loop 113 |
| `round_sector_consistency` | `pass` | R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS |
| `canonical_archetype_present` | `pass` | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| `all_trigger_rows_have_entry_date_price` | `pass` | 7/7 |
| `all_trigger_rows_have_30_90_180_mfe_mae` | `pass` | 7/7 |
| `price_basis_and_adjustment_status` | `pass` | tradable_raw / raw_unadjusted_marcap |
| `forward_window_trading_days_180` | `pass` | 7/7 |
| `corporate_action_window_status` | `pass` | no share-count change in selected loaded 180D window |
| `positive_and_counterexample_balance` | `pass` | 4:3 |
| `minimum_new_symbol_count` | `pass` | 7 |
| `handoff_prompt_executed_now` | `pass` | false |

## 10. Final research state
```json
{
  "completed_round": "R2",
  "completed_loop": 113,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 1-under-50 after local-session adjustment; published index Priority 0",
  "next_recommended_archetypes": [
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
    "C11_BATTERY_ORDERBOOK_RERATING",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C14_EV_DEMAND_SLOWDOWN_4B_4C"
  ],
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "one_line_summary": "This loop adds 7 new independent cases, 3 counterexamples, and 7 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE."
}
```
## 11. Deferred Coding Agent Handoff Prompt — not executed
```text

You are the later batch implementation agent for stock_agent. Do not treat this MD as a production patch by itself. In the next batch calibration pass, parse the trigger JSONL rows from `e2r_stock_web_v12_residual_round_R2_loop_113_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md` and compare them with other C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE rows. Consider a C10-specific shadow patch only if URL/evidence repair confirms the non-price evidence families.

Candidate rule to evaluate:
- canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
- rule_id: C10_memory_recovery_bridge_before_Yellow_and_late_cycle_MAE_to_4B_watch_v3
- direction: require verified order/revenue/margin/inventory-reset bridge before Stage3-Yellow/Green; route tester/OSAT/material proxy labels with MAE90 <= -20% or post-peak RS fade to local 4B watch.
- do not loosen Stage3-Green globally.
- do not apply if rows remain source_proxy_only or evidence_url_pending.
```
