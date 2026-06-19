# E2R Stock-Web v12 Residual Research — R2 / C09 Advanced Equipment Valuation Blowoff

## Metadata

- `research_session`: `post_calibrated_sector_archetype_residual_research`
- `mode`: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- `selected_round`: `R2`
- `selected_loop`: `210`
- `large_sector_id`: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- `canonical_archetype_id`: `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`
- `fine_archetype_id`: `C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1`
- `selection_basis`: `docs/core/V12_Research_No_Repeat_Index.md`
- `selected_priority_bucket`: `Priority 1 quality reinforcement / direct-equipment-order vs valuation blowoff / missing hard-4C boundary`
- `round_schedule_status`: `coverage_index_selected`
- `round_sector_consistency`: `pass`
- `production_scoring_changed`: `False`
- `shadow_weight_only`: `True`
- `stock_agent_code_accessed`: `False`
- `stock_agent_code_patched`: `False`
- `current_stock_discovery_allowed`: `False`
- `primary_price_source`: `Songdaiki/stock-web`
- `price_basis`: `tradable_raw`
- `price_adjustment_status`: `raw_unadjusted_marcap`
- `stock_web_manifest_max_date`: `2026-02-20`
- `output_filename`: `e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md`

## Source files read

- https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json

## Coverage / novelty check

`V12_Research_No_Repeat_Index.md` shows all C01~C32 canonical archetypes above 80 representative rows, so this run is not raw row-filling. C09 already has broad coverage but still has a poor 4B/4C balance and needs direct equipment-order evidence to be separated from valuation-only advanced-equipment blowoff. The hard duplicate key is `canonical_archetype_id + symbol + trigger_type + entry_date`; all rows below are new for this run's C09 scope.

```text
C09 snapshot from no-repeat index: rows=291, symbols=77, positives/counter=59/101, 4B/4C=56/2
new_independent_case_count: 8
new_independent_trigger_count: 8
unique_symbol_count: 6
stage2_actionable_count: 3
stage4b_count: 5
hard_4c_count: 0
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## Research objective

C09 is the semiconductor bucket where advanced equipment language can look very persuasive: HPA/HPO, ALD, laser annealing, overlay metrology, EUV pellicle, memory deposition. The residual problem is that the market often trades these names like scarce bottleneck tools before the issuer-level order, shipment, revenue, or margin bridge is visible. This run tests when C09 should preserve Stage2-Actionable and when it should route the row to local 4B/watch because the evidence is mostly valuation or product-profile heat.

## Evidence references

- **HPSP / HPA-HPO R&D and concentration** — https://www.imec-int.com/en/press/hpsp-expands-its-rd-capabilities-and-study-hpa-and-hpo — HPSP strengthened HPA/HPO R&D programs; useful technology evidence but not, by itself, repeat-order conversion.
- **HPSP / GENI-SYS revenue concentration** — https://w4.kirs.or.kr/download/research_eng/250516_HPSP_EN%20%28%EC%88%98%EC%A0%95%EB%B3%B8%29.pdf — KIRS notes high-pressure hydrogen annealing equipment is more than 90% of HPSP sales and discusses the 2024-to-2025 derating.
- **Jusung / ALD-CVD profile** — https://w4.kirs.or.kr/download/research_eng/250103_Jusung_Engineering_Updated_EN.pdf — Jusung's core semiconductor equipment exposure is ALD/CVD; used as issuer-level product route.
- **EO Technics / overstated HBM laser expectations** — https://w4.kirs.or.kr/download/research_eng/250612_%EC%9D%B4%EC%98%A4%ED%85%8C%ED%81%AC%EB%8B%89%EC%8A%A4%28%EA%B8%80%EC%84%B8%29_EN%28%EC%88%98%EC%A0%95%EB%B3%B8%29.pdf — Report says early-2024 stock surge reflected overstated laser annealing/grooving HBM expectations; direct C09 4B evidence.
- **Oros / overlay metrology profile** — https://www.asiae.co.kr/en/article/2024101608115052617 — FS Research diagnosed HBM post-processing equipment demand but this remains product/profile unless order conversion is shown.
- **Oros / high valuation with HBM contribution expectation** — https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%98%A4%EB%A1%9C%EC%8A%A4%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80.pdf — eBEST report explicitly discusses high valuation and HBM metrology contribution possibility.
- **FST / EUV pellicle and inspection tools** — https://www.fstc.co.kr/bbs/board.php?bo_table=media&wr_id=38 — FST developed EUV pellicle mounter/demounter and inspection tools; product-profile evidence.
- **FST / EUV pellicle localization theme** — https://www.mk.co.kr/en/business/11000125 — EUV pellicle localization and Samsung EUV pellicle progress provide sector tailwind but not issuer-level revenue conversion.
- **Wonik IPS / memory process-transition order recovery** — https://w4.kirs.or.kr/download/research_eng/%EC%9B%90%EC%9D%B5IPS_EN.pdf — KIRS Feb 2025 report ties memory process-transition investment to equipment orders.
- **SEMI / capex recovery backdrop** — https://www.semi.org/en/semi-press-release/global-semiconductor-manufacturing-industry-reports-solid-q4-2024-results-semi-reports — Memory-related capex rebounded sharply in Q4 2024; macro backdrop for reopen rows, not sufficient alone.

## Trigger-level price table

| symbol | name | trigger | entry | close | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | peak180 | trough180 | post-peak DD | usable |
|---|---|---|---:|---:|---:|---:|---:|---|---|---:|---|
| 403870 | HPSP | Stage4B | 2024-02-13 | 59,300 | 7.76/-16.95 | 7.76/-39.88 | 7.76/-61.80 | 2024-02-15 63,900 | 2024-08-05 22,650 | -64.55 | true |
| 036930 | Jusung Engineering | Stage2-Actionable | 2024-02-16 | 31,200 | 30.61/-2.56 | 32.85/-2.56 | 32.85/-29.33 | 2024-04-08 41,450 | 2024-09-09 22,050 | -46.80 | true |
| 039030 | EO Technics | Stage4B | 2024-04-30 | 240,500 | 4.99/-21.79 | 4.99/-46.20 | 4.99/-52.81 | 2024-05-09 252,500 | 2024-11-29 113,500 | -55.05 | true |
| 322310 | AUROS Technology | Stage4B | 2024-01-24 | 34,650 | 17.60/-22.94 | 17.60/-33.33 | 17.60/-56.33 | 2024-02-27 40,750 | 2024-09-09 15,130 | -62.87 | true |
| 036810 | FST | Stage2-Actionable | 2024-02-13 | 21,900 | 13.93/-3.20 | 91.10/-3.20 | 91.10/-22.15 | 2024-06-11 41,850 | 2024-10-28 17,050 | -59.26 | true |
| 036810 | FST | Stage4B | 2024-06-10 | 39,600 | 5.68/-25.25 | 5.68/-55.63 | 5.68/-64.17 | 2024-06-11 41,850 | 2024-12-09 14,190 | -66.09 | true |
| 240810 | Wonik IPS | Stage4B | 2024-04-25 | 36,950 | 5.01/-9.34 | 9.07/-19.22 | 9.07/-42.76 | 2024-07-04 40,300 | 2024-12-09 21,150 | -47.52 | true |
| 240810 | Wonik IPS | Stage2-Actionable | 2025-02-11 | 25,950 | 9.83/-9.44 | 9.83/-19.85 | 169.36/-19.85 | 2025-11-04 69,900 | 2025-04-09 20,800 | -11.44 | true |

## Case notes

- **403870**: HPSP had real scarcity value in HPA/HPO, but the February 2024 row arrived during a valuation blowoff. The 180D path shows only +7.76% MFE and -61.80% MAE, so C09 should classify the row as local 4B/watch unless repeat order or revenue conversion is visible.
- **036930**: Jusung has direct ALD/CVD relevance and memory capex sensitivity. The February 2024 row generated +32.85% 180D MFE but later -29.33% MAE; this preserves Stage2-Actionable but blocks Yellow/Green.
- **039030**: EO Technics is the cleanest C09 late-expectation stress row. The KIRS note explicitly says the early-2024 surge reflected overstated HBM laser annealing/grooving expectations; the 180D forward path had +4.99% MFE and -52.81% MAE.
- **322310**: AUROS/Oros has a valid overlay metrology/HBM profile, but the January 2024 row behaved like a product-profile valuation row: +17.60% MFE and -56.33% MAE. Keep it 4B/watch without order/revenue proof.
- **036810**: FST is useful because it shows both sides: the February 2024 EUV-pellicle optionality row produced +91.10% MFE, but the June 2024 post-spike row produced +5.68% MFE and -64.17% MAE. Same issuer, different evidence timing.
- **240810**: Wonik IPS separates a 2024 memory-capex beta 4B row from a 2025 order-recovery reopen row. The 2025 row had +169.36% 180D MFE with -19.85% MAE, but the rule still requires supplier-level order/revenue conversion before Yellow/Green.

## Score simulation / raw component breakdown

Component order is `EPS/Visibility/Bottleneck/Mispricing/Valuation/Capital/Info`. This is a shadow stress test, not a production patch.

| symbol | trigger | component vector | raw total | calibrated decision stress |
|---|---|---|---:|---|
| 403870 | Stage4B | 8/10/10/8/4/3/22 | 65 | route to local 4B/watch; price-only or profile-only blowoff cannot be positive stage |
| 036930 | Stage2-Actionable | 15/16/14/10/8/4/8 | 75 | preserve Stage2-Actionable; block Stage3-Green until supplier-level conversion repeats |
| 039030 | Stage4B | 8/10/10/8/4/3/22 | 65 | route to local 4B/watch; price-only or profile-only blowoff cannot be positive stage |
| 322310 | Stage4B | 8/10/10/8/4/3/22 | 65 | route to local 4B/watch; price-only or profile-only blowoff cannot be positive stage |
| 036810 | Stage2-Actionable | 18/18/15/12/10/5/9 | 87 | preserve Stage2-Actionable; block Stage3-Green until supplier-level conversion repeats |
| 036810 | Stage4B | 8/10/10/8/4/3/22 | 65 | route to local 4B/watch; price-only or profile-only blowoff cannot be positive stage |
| 240810 | Stage4B | 8/10/10/8/4/3/22 | 65 | route to local 4B/watch; price-only or profile-only blowoff cannot be positive stage |
| 240810 | Stage2-Actionable | 18/18/15/12/10/5/9 | 87 | preserve Stage2-Actionable; block Stage3-Green until supplier-level conversion repeats |

## Residual contribution summary

```text
canonical_rule_candidate: C09_DIRECT_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_GATE_V1
sector_rule_candidate: L2_ADVANCED_EQUIPMENT_ORDER_CONVERSION_AND_GREEN_BRAKE_GATE_V1
loop_contribution_label: c09_direct_order_vs_valuation_blowoff_quality_repair
new_axis_proposed: no_global_axis
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - stage2_required_bridge
  - stage3_green_not_loosened
existing_axis_refined:
  - local_4b_watch_guard
existing_axis_weakened: none
do_not_propose_new_weight_delta: false
```

## Proposed shadow rule

```text
C09_DIRECT_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_GATE_V1

- Advanced equipment language alone — HPA/HPO, ALD, laser annealing, overlay metrology, EUV pellicle, deposition, inspection — creates at most Stage2 or local 4B/watch.
- Stage2-Actionable requires at least one issuer-level second bridge: named customer, purchase order, shipment, customer qualification, repeat tool order, recognized revenue, operating-margin conversion, or backlog-to-revenue conversion.
- If evidence arrives after a fast valuation rerating and the row has weak supplier-order conversion, route to local Stage4B/watch even if the long-term technology story is valid.
- High MAE on a valid direct-order row is a Stage3-Yellow/Green brake, not a Stage2 deletion signal.
- Hard Stage4C requires non-price thesis break: failed qualification, order cancellation, customer loss, revenue/margin collapse, or weak offset quality. Price drawdown alone is not enough.
- Stage3-Green remains blocked until order/revenue/margin conversion repeats across more than one evidence family.
```

## Machine-readable JSONL rows

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 210, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1", "symbol": "403870", "name": "HPSP", "trigger_type": "Stage4B", "evidence_date": "2024-02-13", "trigger_date": "2024-02-13", "entry_date": "2024-02-13", "entry_price": 59300.0, "entry_ohlcv": {"o": 49400.0, "h": 62400.0, "l": 49250.0, "c": 59300.0, "v": 15671806.0, "a": 919628142300.0, "mc": 4917566000200.0, "s": 82926914, "m": "KOSDAQ"}, "mfe_30d_pct": 7.76, "mae_30d_pct": -16.95, "mfe_90d_pct": 7.76, "mae_90d_pct": -39.88, "mfe_180d_pct": 7.76, "mae_180d_pct": -61.8, "peak_180d_date": "2024-02-15", "peak_180d_high": 63900.0, "trough_180d_date": "2024-08-05", "trough_180d_low": 22650.0, "post_peak_drawdown_180d_pct": -64.55, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "entry_row_exists": true, "available_forward_rows_180d": 180, "window_180d_corporate_action_contaminated": false, "calibration_usable": true}, "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 10, "bottleneck_pricing": 10, "market_mispricing": 8, "valuation_rerating": 4, "capital_allocation": 3, "information_confidence": 22}, "score_total_shadow": 65, "current_profile_error_type": "valuation_blowoff_positive_stage_risk", "residual_label": "valuation_blowoff_local_4b_watch", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 210, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1", "symbol": "036930", "name": "Jusung Engineering", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-02-16", "trigger_date": "2024-02-16", "entry_date": "2024-02-16", "entry_price": 31200.0, "entry_ohlcv": {"o": 32000.0, "h": 32200.0, "l": 31050.0, "c": 31200.0, "v": 463669.0, "a": 14552789450.0, "mc": 1505375414400.0, "s": 48249212, "m": "KOSDAQ GLOBAL"}, "mfe_30d_pct": 30.61, "mae_30d_pct": -2.56, "mfe_90d_pct": 32.85, "mae_90d_pct": -2.56, "mfe_180d_pct": 32.85, "mae_180d_pct": -29.33, "peak_180d_date": "2024-04-08", "peak_180d_high": 41450.0, "trough_180d_date": "2024-09-09", "trough_180d_low": 22050.0, "post_peak_drawdown_180d_pct": -46.8, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "entry_row_exists": true, "available_forward_rows_180d": 180, "window_180d_corporate_action_contaminated": false, "calibration_usable": true}, "raw_component_score_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 16, "bottleneck_pricing": 14, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 8}, "score_total_shadow": 75, "current_profile_error_type": "green_overpromotion_risk", "residual_label": "direct_order_bridge_preserved_green_blocked", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 210, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1", "symbol": "039030", "name": "EO Technics", "trigger_type": "Stage4B", "evidence_date": "2024-04-30", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 240500.0, "entry_ohlcv": {"o": 246000.0, "h": 249000.0, "l": 239500.0, "c": 240500.0, "v": 82886.0, "a": 20107003000.0, "mc": 2962851775000.0, "s": 12319550, "m": "KOSDAQ GLOBAL"}, "mfe_30d_pct": 4.99, "mae_30d_pct": -21.79, "mfe_90d_pct": 4.99, "mae_90d_pct": -46.2, "mfe_180d_pct": 4.99, "mae_180d_pct": -52.81, "peak_180d_date": "2024-05-09", "peak_180d_high": 252500.0, "trough_180d_date": "2024-11-29", "trough_180d_low": 113500.0, "post_peak_drawdown_180d_pct": -55.05, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "entry_row_exists": true, "available_forward_rows_180d": 180, "window_180d_corporate_action_contaminated": false, "calibration_usable": true}, "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 10, "bottleneck_pricing": 10, "market_mispricing": 8, "valuation_rerating": 4, "capital_allocation": 3, "information_confidence": 22}, "score_total_shadow": 65, "current_profile_error_type": "valuation_blowoff_positive_stage_risk", "residual_label": "valuation_blowoff_local_4b_watch", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 210, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1", "symbol": "322310", "name": "AUROS Technology", "trigger_type": "Stage4B", "evidence_date": "2024-01-24", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 34650.0, "entry_ohlcv": {"o": 31050.0, "h": 36600.0, "l": 30800.0, "c": 34650.0, "v": 4400841.0, "a": 151461147900.0, "mc": 324550680300.0, "s": 9366542, "m": "KOSDAQ"}, "mfe_30d_pct": 17.6, "mae_30d_pct": -22.94, "mfe_90d_pct": 17.6, "mae_90d_pct": -33.33, "mfe_180d_pct": 17.6, "mae_180d_pct": -56.33, "peak_180d_date": "2024-02-27", "peak_180d_high": 40750.0, "trough_180d_date": "2024-09-09", "trough_180d_low": 15130.0, "post_peak_drawdown_180d_pct": -62.87, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "entry_row_exists": true, "available_forward_rows_180d": 180, "window_180d_corporate_action_contaminated": false, "calibration_usable": true}, "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 10, "bottleneck_pricing": 10, "market_mispricing": 8, "valuation_rerating": 4, "capital_allocation": 3, "information_confidence": 22}, "score_total_shadow": 65, "current_profile_error_type": "valuation_blowoff_positive_stage_risk", "residual_label": "valuation_blowoff_local_4b_watch", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 210, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1", "symbol": "036810", "name": "FST", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-02-13", "trigger_date": "2024-02-13", "entry_date": "2024-02-13", "entry_price": 21900.0, "entry_ohlcv": {"o": 21900.0, "h": 22250.0, "l": 21700.0, "c": 21900.0, "v": 161963.0, "a": 3561910600.0, "mc": 476473679100.0, "s": 21756789, "m": "KOSDAQ"}, "mfe_30d_pct": 13.93, "mae_30d_pct": -3.2, "mfe_90d_pct": 91.1, "mae_90d_pct": -3.2, "mfe_180d_pct": 91.1, "mae_180d_pct": -22.15, "peak_180d_date": "2024-06-11", "peak_180d_high": 41850.0, "trough_180d_date": "2024-10-28", "trough_180d_low": 17050.0, "post_peak_drawdown_180d_pct": -59.26, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "entry_row_exists": true, "available_forward_rows_180d": 180, "window_180d_corporate_action_contaminated": false, "calibration_usable": true}, "raw_component_score_breakdown": {"eps_fcf_explosion": 18, "earnings_visibility": 18, "bottleneck_pricing": 15, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 5, "information_confidence": 9}, "score_total_shadow": 87, "current_profile_error_type": "green_overpromotion_risk", "residual_label": "direct_order_bridge_preserved_green_blocked", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 210, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1", "symbol": "036810", "name": "FST", "trigger_type": "Stage4B", "evidence_date": "2024-06-10", "trigger_date": "2024-06-10", "entry_date": "2024-06-10", "entry_price": 39600.0, "entry_ohlcv": {"o": 38350.0, "h": 40450.0, "l": 37600.0, "c": 39600.0, "v": 1134422.0, "a": 44785721450.0, "mc": 861568844400.0, "s": 21756789, "m": "KOSDAQ"}, "mfe_30d_pct": 5.68, "mae_30d_pct": -25.25, "mfe_90d_pct": 5.68, "mae_90d_pct": -55.63, "mfe_180d_pct": 5.68, "mae_180d_pct": -64.17, "peak_180d_date": "2024-06-11", "peak_180d_high": 41850.0, "trough_180d_date": "2024-12-09", "trough_180d_low": 14190.0, "post_peak_drawdown_180d_pct": -66.09, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "entry_row_exists": true, "available_forward_rows_180d": 180, "window_180d_corporate_action_contaminated": false, "calibration_usable": true}, "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 10, "bottleneck_pricing": 10, "market_mispricing": 8, "valuation_rerating": 4, "capital_allocation": 3, "information_confidence": 22}, "score_total_shadow": 65, "current_profile_error_type": "valuation_blowoff_positive_stage_risk", "residual_label": "valuation_blowoff_local_4b_watch", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 210, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1", "symbol": "240810", "name": "Wonik IPS", "trigger_type": "Stage4B", "evidence_date": "2024-04-25", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 36950.0, "entry_ohlcv": {"o": 35550.0, "h": 38650.0, "l": 35150.0, "c": 36950.0, "v": 592357.0, "a": 22206821550.0, "mc": 1813650141950.0, "s": 49083901, "m": "KOSDAQ GLOBAL"}, "mfe_30d_pct": 5.01, "mae_30d_pct": -9.34, "mfe_90d_pct": 9.07, "mae_90d_pct": -19.22, "mfe_180d_pct": 9.07, "mae_180d_pct": -42.76, "peak_180d_date": "2024-07-04", "peak_180d_high": 40300.0, "trough_180d_date": "2024-12-09", "trough_180d_low": 21150.0, "post_peak_drawdown_180d_pct": -47.52, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "entry_row_exists": true, "available_forward_rows_180d": 180, "window_180d_corporate_action_contaminated": false, "calibration_usable": true}, "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 10, "bottleneck_pricing": 10, "market_mispricing": 8, "valuation_rerating": 4, "capital_allocation": 3, "information_confidence": 22}, "score_total_shadow": 65, "current_profile_error_type": "valuation_blowoff_positive_stage_risk", "residual_label": "valuation_blowoff_local_4b_watch", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_210_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "round": "R2", "loop": 210, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "C09_ADVANCED_EQUIPMENT_DIRECT_ORDER_VS_VALUATION_BLOWOFF_GATE_V1", "symbol": "240810", "name": "Wonik IPS", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-02-11", "trigger_date": "2025-02-11", "entry_date": "2025-02-11", "entry_price": 25950.0, "entry_ohlcv": {"o": 24050.0, "h": 27250.0, "l": 23500.0, "c": 25950.0, "v": 1854019.0, "a": 48487931100.0, "mc": 1273727230950.0, "s": 49083901, "m": "KOSDAQ GLOBAL"}, "mfe_30d_pct": 9.83, "mae_30d_pct": -9.44, "mfe_90d_pct": 9.83, "mae_90d_pct": -19.85, "mfe_180d_pct": 169.36, "mae_180d_pct": -19.85, "peak_180d_date": "2025-11-04", "peak_180d_high": 69900.0, "trough_180d_date": "2025-04-09", "trough_180d_low": 20800.0, "post_peak_drawdown_180d_pct": -11.44, "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "entry_row_exists": true, "available_forward_rows_180d": 180, "window_180d_corporate_action_contaminated": false, "calibration_usable": true}, "raw_component_score_breakdown": {"eps_fcf_explosion": 18, "earnings_visibility": 18, "bottleneck_pricing": 15, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 5, "information_confidence": 9}, "score_total_shadow": 87, "current_profile_error_type": "green_overpromotion_risk", "residual_label": "direct_order_bridge_preserved_green_blocked", "production_scoring_changed": false, "shadow_weight_only": true}
```

## Batch ingest self-audit

```text
standard_v12_filename: true
filename_round_matches_metadata: true
filename_loop_matches_metadata: true
round_sector_consistency: true
canonical_archetype_id_present: true
large_sector_id_present: true
all_trigger_rows_have_entry_price: true
all_trigger_rows_have_actual_entry_ohlcv: true
all_trigger_rows_have_30_90_180_mfe_mae: true
same_entry_deduplicated: true
corporate_action_contaminated_rows_excluded_from_promotion: true
insufficient_forward_window_rows_excluded_from_promotion: true
source_proxy_only_count_zero: true
evidence_url_pending_count_zero: true
production_scoring_changed_false: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## Deferred Coding Agent Handoff Prompt — do not execute in this research run

```text
Read this MD together with other v12 C09/C10/C07/C08 L2 research files. Do not loosen Stage3-Green globally. Consider only a scope-limited C09 shadow rule that requires issuer-level order / shipment / qualification / revenue / margin conversion before Stage2-Actionable or Yellow, and routes post-rerating advanced-equipment profile rows to local 4B/watch. Preserve Stage2-Actionable when a direct supplier bridge exists; use high MAE as a Yellow/Green brake rather than Stage2 deletion. Do not modify production scoring without batch validation, dedupe, and promotion planning.
```

## Next Research State

```text
completed_round = R2
completed_loop = 210
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 quality reinforcement / C09 direct-order vs valuation blowoff
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes:
- C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_FAILED_QUALIFICATION_4C_DIRECT_ROW_REPAIR
- C06_HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_PASS_DIRECT_REVENUE_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```