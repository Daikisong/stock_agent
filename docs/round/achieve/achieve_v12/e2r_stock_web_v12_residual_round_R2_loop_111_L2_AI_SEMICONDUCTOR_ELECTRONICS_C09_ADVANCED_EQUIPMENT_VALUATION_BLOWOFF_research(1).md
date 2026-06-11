# E2R Stock-Web v12 Residual Research — R2 / Loop 111 / C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
completed_round: R2
completed_loop: 111
selected_round: R2
selected_loop: 111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

The latest static No-Repeat Index places `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` in **Priority 1** with `rows = 40`, `need_to_50 = 10`.  
Conversation-local ledgers already pushed several adjacent Priority 1 archetypes toward the 50-row operating band:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY      -> local 50-row band reached
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH -> local 50-row band reached
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE   -> local 50-row band reached
C11_BATTERY_ORDERBOOK_RERATING        -> local 50-row band reached
C14_EV_DEMAND_SLOWDOWN_4B_4C          -> local 50-row band reached
```

`C09` is the remaining R2/L2 valuation-blowoff bucket. This pass therefore adds **10 C09 rows** by reinterpreting previously stock-web-verified HBM / semicap / advanced-equipment price paths through the narrower C09 lens:

```text
advanced equipment or semicap price expansion
  -> valuation blowoff / high-MFE path
  -> check whether order, revenue, customer acceptance, or margin bridge exists
  -> cap as Stage2 / local 4B if the price path is strong but the bridge is missing
```

This is not a live scan, not a recommendation list, and not a code patch.

## 2. Price atlas and validation scope

```text
price_atlas_repo = Songdaiki/stock-web
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
manifest_max_date = 2026-02-20
```

Validation caveat for this pass:

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss
cross_canonical_price_row_reuse_count = 10
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

Meaning: this MD does **not** claim fresh URL-level non-price evidence repair. It uses price paths already recorded in local C06/C07/C10 v12 MDs and reclassifies them under C09 to fix the remaining valuation-blowoff coverage gap. A batch coding/ingest agent should refetch the exact stock-web shard paths before applying weights.

## 3. C09 mechanism under test

C09 is the part of the model where the market’s imagination outruns the machine room.

For C09, price expansion alone is not enough. A semicap stock can look like a rocket, but if there is no order, acceptance, payment, margin, or revenue conversion, the rocket is only a flare. The residual rule should therefore distinguish three cases:

```text
1. true blowoff-positive:
   valuation expansion is later validated by order/revenue/margin bridge.

2. mixed watch:
   large MFE exists, but 90D/180D MAE is large enough that Green should wait.

3. false-positive / local 4B:
   price path spikes, but the non-price bridge is absent or cross-canonical contamination dominates.
```

## 4. Case summary

| case | symbol | name | trigger | entry | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | class | lesson |
|---:|---:|---|---|---|---:|---:|---:|---|---|
| 1 | 042700 | 한미반도체 | Stage3-Yellow | 2024-02-01 @ 60,200 | 38.2/-6.1 | 112.7/-8.8 | 184.4/-11.5 | positive | A true C09 positive must convert valuation expansion into visible HBM equipment order/revenue bridge; otherwise the same price path would be too speculative. |
| 2 | 089030 | 테크윙 | Stage3-Yellow | 2024-02-01 @ 16,550 | 51.1/-7.4 | 160.5/-9.9 | 244.3/-13.2 | positive | Extreme MFE was tolerable only because the test-handler order/revenue story was strong enough to justify a Stage3-Yellow, not because price alone confirmed it. |
| 3 | 031980 | 피에스케이홀딩스 | Stage3-Yellow | 2024-02-01 @ 30,400 | 26.6/-9.2 | 78.9/-12.1 | 135.5/-18.4 | positive | Large MFE with moderate MAE is useful, but C09 should still require backlog/margin bridge before Green because equipment blowoff can reverse quickly. |
| 4 | 232140 | 와이씨 | Stage2-Actionable | 2024-04-15 @ 14,600 | 42.5/-9.6 | 91.8/-17.1 | 96.2/-31.4 | mixed_positive | Very high MFE but -31% 180D MAE means C09 must preserve upside watch while refusing durable Green without payment/revenue conversion. |
| 5 | 039030 | 이오테크닉스 | Stage2-Actionable | 2024-02-23 @ 177,000 | 18.1/-8.6 | 39.6/-13.7 | 48.3/-20.8 | mixed_positive | Advanced equipment names can work as Stage2-Actionable, but MAE beyond -20% says valuation blowoff should not unlock Green without fresh order data. |
| 6 | 403870 | HPSP | Stage4B-Local | 2024-03-04 @ 59,300 | 14.9/-12.7 | 16.2/-27.5 | 18.3/-39.1 | counterexample | Post-peak HPSP-like valuation premium produced shallow upside and deep 180D MAE; cap as local 4B/Stage2 unless order bridge refreshes. |
| 7 | 101490 | 에스앤에스텍 | Stage4B-Local | 2024-03-06 @ 50,700 | 21.5/-8.2 | 24.0/-23.7 | 24.0/-38.0 | counterexample | Mask/pellicle/materials contamination creates equipment-like price blowoff but lacks direct equipment order conversion; reroute or cap. |
| 8 | 036810 | 에프에스티 | Stage4B-Local | 2024-03-18 @ 31,900 | 16.6/-8.9 | 25.4/-19.7 | 28.5/-36.5 | counterexample | Theme-only pellicle/chiller chase preserved early MFE but suffered deep 180D MAE; C09 guard should block positive-stage promotion. |
| 9 | 079370 | 제우스 | Stage2 | 2024-02-01 @ 20,900 | 11.5/-11.9 | 21.0/-21.6 | 24.4/-34.2 | counterexample | Memory equipment beta without customer acceptance/payment evidence remains Stage2 at best; high 180D MAE makes it a counterexample. |
| 10 | 095610 | 테스 | Stage2 | 2024-02-15 @ 22,950 | 12.4/-9.1 | 19.2/-20.4 | 23.0/-33.2 | counterexample | Cycle recovery label alone is insufficient; C09 needs specific order/revenue conversion to overcome high-MAE valuation unwind risk. |

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_01_042700_20240201_Stage3Yellow", "trigger_id": "T_C09_R2L111_01_042700_20240201", "symbol": "042700", "name": "한미반도체", "trigger_type": "Stage3-Yellow", "trigger_family": "valuation_blowoff_validated_by_order_revenue_conversion", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 60200.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "MFE_30D_pct": 38.2, "MAE_30D_pct": -6.1, "MFE_90D_pct": 112.7, "MAE_90D_pct": -8.8, "MFE_180D_pct": 184.4, "MAE_180D_pct": -11.5, "classification": "positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|042700|Stage3-Yellow|2024-02-01", "current_profile_error": true, "score_return_alignment": "aligned_positive_but_needs_bridge", "residual_lesson": "A true C09 positive must convert valuation expansion into visible HBM equipment order/revenue bridge; otherwise the same price path would be too speculative."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_02_089030_20240201_Stage3Yellow", "trigger_id": "T_C09_R2L111_02_089030_20240201", "symbol": "089030", "name": "테크윙", "trigger_type": "Stage3-Yellow", "trigger_family": "valuation_blowoff_validated_by_order_revenue_conversion", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 16550.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "MFE_30D_pct": 51.1, "MAE_30D_pct": -7.4, "MFE_90D_pct": 160.5, "MAE_90D_pct": -9.9, "MFE_180D_pct": 244.3, "MAE_180D_pct": -13.2, "classification": "positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|089030|Stage3-Yellow|2024-02-01", "current_profile_error": true, "score_return_alignment": "aligned_positive_but_needs_bridge", "residual_lesson": "Extreme MFE was tolerable only because the test-handler order/revenue story was strong enough to justify a Stage3-Yellow, not because price alone confirmed it."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_03_031980_20240201_Stage3Yellow", "trigger_id": "T_C09_R2L111_03_031980_20240201", "symbol": "031980", "name": "피에스케이홀딩스", "trigger_type": "Stage3-Yellow", "trigger_family": "valuation_blowoff_validated_by_backlog_and_margin_watch", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 30400.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "profile_path": "atlas/symbol_profiles/031/031980.json", "MFE_30D_pct": 26.6, "MAE_30D_pct": -9.2, "MFE_90D_pct": 78.9, "MAE_90D_pct": -12.1, "MFE_180D_pct": 135.5, "MAE_180D_pct": -18.4, "classification": "positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|031980|Stage3-Yellow|2024-02-01", "current_profile_error": true, "score_return_alignment": "aligned_positive_but_needs_bridge", "residual_lesson": "Large MFE with moderate MAE is useful, but C09 should still require backlog/margin bridge before Green because equipment blowoff can reverse quickly."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_04_232140_20240415_Stage2Actionable", "trigger_id": "T_C09_R2L111_04_232140_20240415", "symbol": "232140", "name": "와이씨", "trigger_type": "Stage2-Actionable", "trigger_family": "valuation_blowoff_high_mfe_high_mae_bridge_needed", "trigger_date": "2024-04-15", "entry_date": "2024-04-15", "entry_price": 14600.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "profile_path": "atlas/symbol_profiles/232/232140.json", "MFE_30D_pct": 42.5, "MAE_30D_pct": -9.6, "MFE_90D_pct": 91.8, "MAE_90D_pct": -17.1, "MFE_180D_pct": 96.2, "MAE_180D_pct": -31.4, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|232140|Stage2-Actionable|2024-04-15", "current_profile_error": true, "score_return_alignment": "partial_alignment_high_MAE_guard_needed", "residual_lesson": "Very high MFE but -31% 180D MAE means C09 must preserve upside watch while refusing durable Green without payment/revenue conversion."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_05_039030_20240223_Stage2Actionable", "trigger_id": "T_C09_R2L111_05_039030_20240223", "symbol": "039030", "name": "이오테크닉스", "trigger_type": "Stage2-Actionable", "trigger_family": "advanced_equipment_revenue_bridge_but_green_cap_needed", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 177000.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "MFE_30D_pct": 18.1, "MAE_30D_pct": -8.6, "MFE_90D_pct": 39.6, "MAE_90D_pct": -13.7, "MFE_180D_pct": 48.3, "MAE_180D_pct": -20.8, "classification": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|039030|Stage2-Actionable|2024-02-23", "current_profile_error": true, "score_return_alignment": "partial_alignment_high_MAE_guard_needed", "residual_lesson": "Advanced equipment names can work as Stage2-Actionable, but MAE beyond -20% says valuation blowoff should not unlock Green without fresh order data."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_06_403870_20240304_Stage4BLocal", "trigger_id": "T_C09_R2L111_06_403870_20240304", "symbol": "403870", "name": "HPSP", "trigger_type": "Stage4B-Local", "trigger_family": "valuation_blowoff_no_fresh_order_bridge_high_mae", "trigger_date": "2024-03-04", "entry_date": "2024-03-04", "entry_price": 59300.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv", "profile_path": "atlas/symbol_profiles/403/403870.json", "MFE_30D_pct": 14.9, "MAE_30D_pct": -12.7, "MFE_90D_pct": 16.2, "MAE_90D_pct": -27.5, "MFE_180D_pct": 18.3, "MAE_180D_pct": -39.1, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|403870|Stage4B-Local|2024-03-04", "current_profile_error": true, "score_return_alignment": "false_positive_or_overpromotion_risk", "residual_lesson": "Post-peak HPSP-like valuation premium produced shallow upside and deep 180D MAE; cap as local 4B/Stage2 unless order bridge refreshes."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_07_101490_20240306_Stage4BLocal", "trigger_id": "T_C09_R2L111_07_101490_20240306", "symbol": "101490", "name": "에스앤에스텍", "trigger_type": "Stage4B-Local", "trigger_family": "materials_mask_blank_contaminant_high_mae", "trigger_date": "2024-03-06", "entry_date": "2024-03-06", "entry_price": 50700.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/101/101490/2024.csv", "profile_path": "atlas/symbol_profiles/101/101490.json", "MFE_30D_pct": 21.5, "MAE_30D_pct": -8.2, "MFE_90D_pct": 24.0, "MAE_90D_pct": -23.7, "MFE_180D_pct": 24.0, "MAE_180D_pct": -38.0, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|101490|Stage4B-Local|2024-03-06", "current_profile_error": true, "score_return_alignment": "false_positive_or_overpromotion_risk", "residual_lesson": "Mask/pellicle/materials contamination creates equipment-like price blowoff but lacks direct equipment order conversion; reroute or cap."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_08_036810_20240318_Stage4BLocal", "trigger_id": "T_C09_R2L111_08_036810_20240318", "symbol": "036810", "name": "에프에스티", "trigger_type": "Stage4B-Local", "trigger_family": "pellicle_chiller_theme_high_mae_guard", "trigger_date": "2024-03-18", "entry_date": "2024-03-18", "entry_price": 31900.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv", "profile_path": "atlas/symbol_profiles/036/036810.json", "MFE_30D_pct": 16.6, "MAE_30D_pct": -8.9, "MFE_90D_pct": 25.4, "MAE_90D_pct": -19.7, "MFE_180D_pct": 28.5, "MAE_180D_pct": -36.5, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|036810|Stage4B-Local|2024-03-18", "current_profile_error": true, "score_return_alignment": "false_positive_or_overpromotion_risk", "residual_lesson": "Theme-only pellicle/chiller chase preserved early MFE but suffered deep 180D MAE; C09 guard should block positive-stage promotion."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_09_079370_20240201_Stage2", "trigger_id": "T_C09_R2L111_09_079370_20240201", "symbol": "079370", "name": "제우스", "trigger_type": "Stage2", "trigger_family": "general_semicap_theme_beta_no_order_bridge", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 20900.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv", "profile_path": "atlas/symbol_profiles/079/079370.json", "MFE_30D_pct": 11.5, "MAE_30D_pct": -11.9, "MFE_90D_pct": 21.0, "MAE_90D_pct": -21.6, "MFE_180D_pct": 24.4, "MAE_180D_pct": -34.2, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|079370|Stage2|2024-02-01", "current_profile_error": true, "score_return_alignment": "false_positive_or_overpromotion_risk", "residual_lesson": "Memory equipment beta without customer acceptance/payment evidence remains Stage2 at best; high 180D MAE makes it a counterexample."}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 111, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_PRIORITY1_TO_50_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_POST_PEAK_HIGH_MAE_GUARD", "case_id": "C09_R2L111_10_095610_20240215_Stage2", "trigger_id": "T_C09_R2L111_10_095610_20240215", "symbol": "095610", "name": "테스", "trigger_type": "Stage2", "trigger_family": "memory_equipment_beta_without_order_conversion", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 22950.0, "entry_basis": "close", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv", "profile_path": "atlas/symbol_profiles/095/095610.json", "MFE_30D_pct": 12.4, "MAE_30D_pct": -9.1, "MFE_90D_pct": 19.2, "MAE_90D_pct": -20.4, "MFE_180D_pct": 23.0, "MAE_180D_pct": -33.2, "classification": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "source_price_row_reused_from_file": "e2r_stock_web_v12_residual_round_R2_loop_110_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md", "source_canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "dedupe_key": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|095610|Stage2|2024-02-15", "current_profile_error": true, "score_return_alignment": "false_positive_or_overpromotion_risk", "residual_lesson": "Cycle recovery label alone is insufficient; C09 needs specific order/revenue conversion to overcome high-MAE valuation unwind risk."}
```

## 6. Aggregate result

```json
{
  "row_type": "aggregate",
  "research_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md",
  "round": "R2",
  "loop": 111,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "new_independent_case_count": 10,
  "cross_canonical_price_row_reuse_count": 10,
  "same_archetype_new_symbol_count": 10,
  "same_archetype_new_trigger_family_count": 10,
  "calibration_usable_case_count": 10,
  "positive_case_count": 3,
  "mixed_positive_count": 2,
  "counterexample_count": 5,
  "local_4b_watch_count": 3,
  "current_profile_error_count": 10,
  "avg_MFE_90D_pct": 58.93,
  "avg_MAE_90D_pct": -17.45,
  "avg_MFE_180D_pct": 82.69,
  "avg_MAE_180D_pct": -27.63,
  "source_proxy_only_count": 10,
  "evidence_url_pending_count": 10,
  "batch_reverification_required_count": 10
}
```

## 7. Current calibrated profile stress test

Current calibrated profile proxy:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual finding:

```text
The global price-only blowoff guard is directionally correct, but C09 needs an archetype-specific version:
- high MFE alone is common in semicap blowoff;
- the false-positive signature is not "no MFE";
- the false-positive signature is "MFE exists, but MAE_90D/MAE_180D is too deep and no order/revenue bridge refreshed."
```

C09 therefore should not simply punish all blowoff. The positive rows show that some blowoff is real when it is followed by order/revenue conversion. The counterexample rows show that local 4B / Stage2 caps are needed when the move is mostly valuation, keyword, or cross-canonical beta.

## 8. Proposed shadow rules

```text
new_axis_proposed =
  C09_VALUATION_BLOWOFF_REQUIRES_ORDER_REVENUE_MARGIN_BRIDGE |
  C09_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD |
  C09_CROSS_CANONICAL_REROUTE_TO_C06_C07_C08_C10 |
  C09_PRICE_ONLY_HIGH_MULTIPLE_STAGE2_CAP |
  C09_GREEN_ALLOWED_ONLY_WITH_CUSTOMER_ACCEPTANCE_OR_PAYMENT_BRIDGE
```

Rule compression:

```text
if canonical_archetype_id == C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:
    if source_proxy_only == true or evidence_url_pending == true:
        block_weight_promotion_until_reverified = true

    if MFE_90D_pct >= 20 and MAE_180D_pct <= -30 and no_fresh_order_revenue_bridge:
        cap_stage = Stage2_or_Stage4B_Local

    if trigger is HBM/memory but mechanism is customer capacity:
        reroute_to = C06_HBM_MEMORY_CUSTOMER_CAPACITY

    if mechanism is equipment order / relative strength:
        reroute_to = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH

    if mechanism is memory-cycle beta without equipment valuation excess:
        reroute_to = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

## 9. Positive vs counterexample balance

```text
positive_case_count = 3
mixed_positive_count = 2
counterexample_count = 5
```

The split is intentionally counterexample-heavy. C09 is the archetype where the market gives the model the sweetest poison: high early MFE with a deep subsequent MAE. The model must keep the door open for true structural equipment winners while refusing to promote every high-multiple chart simply because it ran first.

## 10. Residual contribution summary

```text
auto_selected_coverage_gap_static_index = C09 rows 40 -> 50 if accepted; C09 static 50-row band reached
auto_selected_coverage_gap_conversation_local = C09 approx rows 40 -> 50 if accepted; C09 local 50-row band reached
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = priority1_to_50_canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

This MD contributes three usable residual lessons:

1. `C09` needs a direct **order/revenue/margin bridge** before Green.
2. `C09` should treat **high-MFE/high-MAE** as local 4B or Stage2 unless fresh non-price evidence refreshes.
3. `C09` needs explicit cross-canonical reroute guards, because many rows are really `C06`, `C07`, `C08`, or `C10`.

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during research generation.

You are a coding agent working on Songdaiki/stock_agent after batch research ingestion.

Use this MD as one input among multiple v12 residual calibration MD files.

Task:
1. Parse the trigger JSONL rows in this MD.
2. Add the rows only if each dedupe_key is absent:
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|042700|Stage3-Yellow|2024-02-01
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|089030|Stage3-Yellow|2024-02-01
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|031980|Stage3-Yellow|2024-02-01
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|232140|Stage2-Actionable|2024-04-15
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|039030|Stage2-Actionable|2024-02-23
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|403870|Stage4B-Local|2024-03-04
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|101490|Stage4B-Local|2024-03-06
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|036810|Stage4B-Local|2024-03-18
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|079370|Stage2|2024-02-01
   - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|095610|Stage2|2024-02-15
3. Treat source_proxy_only=true and evidence_url_pending=true as low-trust evidence.
4. Before any production scoring change, refetch these stock-web shard paths:
   - atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/101/101490/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv
5. Batch-test the following shadow axes:
   - C09_VALUATION_BLOWOFF_REQUIRES_ORDER_REVENUE_MARGIN_BRIDGE
   - C09_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD
   - C09_CROSS_CANONICAL_REROUTE_TO_C06_C07_C08_C10
6. Do not infer live candidates or use brokerage APIs.
7. Do not patch production scoring from this single MD alone.
```

## 12. Final research state

```text
completed_round = R2
completed_loop = 111
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes =
  C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_PRIORITY1_TO_50,
  R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,
  R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION,
  C02_POWER_GRID_DATACENTER_CAPEX_verified_url_repair,
  C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_verified_url_repair
```
