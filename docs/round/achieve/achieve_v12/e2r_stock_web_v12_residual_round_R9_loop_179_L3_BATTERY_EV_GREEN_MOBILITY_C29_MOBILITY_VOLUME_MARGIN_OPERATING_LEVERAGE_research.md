# E2R v12 Residual Research — R9/L3/C29 Mobility Volume-Margin Operating Leverage — loop 179

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R9
selected_loop = 179
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = mixed_c29_tire_auto_parts_thermal_logistics_margin_leaf_set
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
live_candidate_mode = false
```

## 1. Selection rationale

C29 is already above the 50-row minimum in the current No-Repeat Index, but it was touched only once in this running session and the earlier C29 pass was mostly OEM/large-parts oriented. This pass intentionally shifts the microscope to tire premium mix, OE/RE reorder, thermal-management EV-volume risk, auto-parts false-4C offset, and PCTC/CKD logistics operating leverage.

The selected output filename follows the v12 hard rule:

```text
e2r_stock_web_v12_residual_round_R9_loop_179_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

## 2. Stock-Web manifest / schema check

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
entry_price_field = c
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Corporate-action screen:

```text
161390 한국타이어앤테크놀로지: corporate_action_candidate_count=0; usable.
073240 금호타이어: candidate dates 2010-11-02, 2010-12-14, 2018-07-20; no overlap with 2024~2025 trigger windows.
002350 넥센타이어: candidate dates 1999-02-18, 1999-06-08, 1999-06-10, 2008-03-21; no overlap.
018880 한온시스템: candidate dates 2004-05-12, 2016-02-16, 2025-01-09, 2026-01-12. FY2024-loss entry 2025-02-14 has no D+180 overlap. Q1 2024 entry would overlap 2025-01-09 and is therefore narrative-only.
011210 현대위아: corporate_action_candidate_count=0; usable.
086280 현대글로비스: candidate dates 2024-07-12, 2024-08-02. 2025-05-02 entry has no D+180 overlap.
```

## 3. No-repeat / novelty check

```text
previous_session_C29_loop = 123
known_session_C29_symbols_avoided_or_not_repeated_as_exact_keys = 000270, 005380, 012330, 204320
new_loop_179_symbols = 161390, 073240, 002350, 018880, 011210, 086280
hard_duplicate_key_rule = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_found = false
```

This is not a sequential R1→R13 run. C29 drives R9/L3 metadata.

## 4. Case table

| # | ticker | name | trigger/evidence date | entry date | label | trigger type | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | interpretation |
|---:|---|---|---|---|---|---|---:|---:|---:|---|
| 1 | 161390 | 한국타이어앤테크놀로지 | 2024-05-02 | 2024-05-03 | counterexample | Stage2-FalsePositive|Local4B-Watch | 5.12/-20.02 | 5.12/-28.18 | 5.12/-34.54 | 1Q24 sales/OP were strong and OP doubled YoY, but the signal arrived after the tire margin rerating was already crowded; 90D/180D MFE stayed near 5% while MAE deepened. |
| 2 | 161390 | 한국타이어앤테크놀로지 | 2025-02-04 | 2025-02-05 | positive | Stage2-Actionable | 12.05/-2.91 | 15.36/-4.77 | 28.48/-4.77 | FY2024 OP rose 32.7% to KRW 1.7622tn and OPM reached 18.7%; after the 2024 drawdown, the reset entry had low MAE and clean 180D upside. |
| 3 | 073240 | 금호타이어 | 2024-04-30 | 2024-05-02 | counterexample | Stage2-FalsePositive|Local4B-Watch | 6.77/-16.73 | 6.77/-47.25 | 6.77/-48.02 | Q1 sales reached a 10-year first-quarter high and OP grew 167%, but price had already pulled forward the margin story; subsequent 90D/180D drawdown was severe. |
| 4 | 073240 | 금호타이어 | 2024-11-20 | 2024-11-21 | positive | Stage2-Actionable|Stage3-Yellow-Watch | 14.58/-1.81 | 21.81/-5.31 | 21.81/-8.25 | 3Q24 NDR showed RE/OE growth, high-margin tire mix, 18-inch+ mix progress, EV tire supply ratio and Vietnam CAPA utilization. Reset price made the same tire thesis more usable. |
| 5 | 002350 | 넥센타이어 | 2024-01-31 | 2024-02-01 | positive | Stage2-Actionable | 20.88/-1.88 | 20.88/-1.88 | 20.88/-15.62 | FY2023 turned to KRW 186.7bn OP from loss, with transport-cost relief and OE/RE demand recovery; early entry had clean 30D/90D MFE and shallow initial MAE. |
| 6 | 002350 | 넥센타이어 | 2024-05-29 | 2024-05-30 | counterexample | Stage2-FalsePositive|HighMAE-Guard | 3.75/-5.37 | 3.75/-15.73 | 3.75/-35.08 | 2H24 Czech expansion could improve logistics and volume, but the report itself flagged ramp/fixed-cost timing; price path showed almost no upside and deep 180D MAE. |
| 7 | 018880 | 한온시스템 | 2025-02-13 | 2025-02-14 | counterexample | Stage4C-ThesisBreak|HighMAE-Guard | 10.44/-13.88 | 10.44/-32.57 | 13.65/-32.57 | FY2024 sales grew but Q4 OP turned to loss from one-off/restructuring costs, and EV customer volume shortfall plus impairment/interest burden drove net loss. MFE was capped while MAE deepened. |
| 8 | 011210 | 현대위아 | 2025-04-30 | 2025-05-02 | positive | Stage2-Watch|False4C-Audit | 11.19/-7.18 | 31.68/-7.18 | 131.57/-7.18 | Q1 OP fell 15.9% due to Mexico utilization and incentive burden, but sales were stable and pretax profit rose. Price path argues against hard 4C on one-quarter margin drag when offset businesses remain alive. |
| 9 | 086280 | 현대글로비스 | 2025-04-30 | 2025-05-02 | positive | Stage3-Yellow|Stage2-Actionable | 27.81/-2.79 | 78.33/-2.79 | 175.35/-2.79 | 1Q25 revenue was KRW 7.2234tn and OP KRW 501.884bn; separate reports describe record quarterly OP and broad logistics/shipping/distribution strength. This is the clean C29 operating-leverage positive. |


## 5. Evidence notes

- **한국타이어앤테크놀로지 1Q24**: strong OP growth was real, but the entry was late relative to price exhaustion. This row strengthens the high-MAE/local-4B timing guard.
- **한국타이어앤테크놀로지 FY2024**: the same premium-mix thesis became usable after valuation reset; this is a reset-entry positive.
- **금호타이어 Q1 2024 vs Q3 2024**: Q1 headline was a crowded late-entry trap, while the post-drawdown Q3 NDR showed high-inch tire mix, EV tire ratio and Vietnam CAPA utilization with much lower MAE.
- **넥센타이어 FY2023 vs 2H24 report**: actual turnaround worked early; forecast-only Czech ramp/fixed-cost bridge came too late.
- **한온시스템 FY2024**: EV customer volume shortfall, restructuring/one-off costs, impairment and interest burden block C29 positive staging until margin repair is confirmed.
- **현대위아 Q1 2025**: a single-quarter OP decline should not be hard 4C when pretax profit, FX/defense/mix offset and later price path remain alive.
- **현대글로비스 Q1 2025**: PCTC/CKD/logistics operating leverage is a clean C29 positive even though it is not an OEM unit-volume case.

## 6. Current calibrated profile stress test

```text
current_profile_proxy = e2r_2_1_stock_web_calibrated / e2r_2_2 rolling selector context
profile_guardrails_in_force = stage2_required_bridge, local_4b_watch_guard, hard_4c_confirmation, price_only_blowoff_blocks_positive_stage
new_residual_error = C29 timing/reset-entry distinction still under-specified
```

Stress-test findings:

1. **Late headline false positive**: Hankook Q1 2024 and Kumho Q1 2024 show that tire OP beats can arrive after the cycle has already been priced. C29 needs an exhaustion check.
2. **Reset-entry exception**: Hankook FY2024 and Kumho Q3 2024 show that the same tire margin bridge works better after valuation reset and low-MAE entry.
3. **Forecast-only CAPA risk**: Nexen 2H24 Czech ramp report had real logic, but without run-rate utilization confirmation the 180D path was poor.
4. **EV thermal 4C confirmation**: Hanon FY2024 is the clearest negative row: sales vocabulary did not matter once volume shortfall, structure cost, impairment and net loss dominated.
5. **False hard-4C audit**: Hyundai Wia Q1 2025 shows that one quarter of margin pressure is not enough for irreversible thesis break if offset businesses and subsequent price path survive.
6. **Logistics positive boundary**: Hyundai Glovis Q1 2025 expands C29 beyond OEM/parts into mobility logistics where PCTC/CKD operating leverage is explicit.

## 7. Shadow rule candidate

```text
rule_id = C29_VOLUME_MARGIN_RESET_ENTRY_AND_OPERATIONAL_LEVERAGE_GATE_V2
target_scope = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
production_scoring_changed = false
shadow_weight_only = true
```

Proposed rule:

```text
Stage2-Actionable in C29 requires:
  1. volume / shipment / OE-RE reorder / PCTC-CKD logistics growth OR named customer/order/route evidence,
  2. margin / OP / OPM / mix / cost relief conversion bridge,
  3. either low-MAE reset entry or evidence arriving before the majority of price rerating.

Local4B or Stage2-Watch should override when:
  - OP-beat headline arrives after a major rerating,
  - CAPA/ramp is forecast-only and utilization/run-rate is not confirmed,
  - EV-volume slowdown or customer shortfall appears before margin repair,
  - MFE/MAE asymmetry is poor: e.g., 90D MFE < 10% while 90D MAE <= -20%.

Hard 4C should not fire solely on:
  - one-quarter margin drag,
  - temporary utilization loss,
  - segment-level weakness, if offset business, pretax profit, valuation reset, or subsequent low-MAE price path remains alive.
```

## 8. Machine-readable trigger rows JSONL

```jsonl
{"case_id": "C29_L179_001_HANKOOK_Q1_2024_LATE_HEADLINE_HIGH_MAE", "ticker": "161390", "name": "한국타이어앤테크놀로지", "evidence_date": "2024-05-02", "entry_date": "2024-05-03", "entry_price": 52700.0, "trigger_type": "Stage2-FalsePositive|Local4B-Watch", "case_label": "counterexample", "fine_archetype_id": "C29_TIRE_PREMIUM_MIX_LATE_HEADLINE_HIGH_MAE", "MFE_30D_pct": 5.12, "MAE_30D_pct": -20.02, "MFE_90D_pct": 5.12, "MAE_90D_pct": -28.18, "MFE_180D_pct": 5.12, "MAE_180D_pct": -34.54, "D30_end": "2024-06-18", "D90_end": "2024-09-11", "D180_end": "2025-02-03", "evidence_url": "https://www.hankookandcompany.com/ko/media/news/article-1882.do", "evidence_summary": "1Q24 sales/OP were strong and OP doubled YoY, but the signal arrived after the tire margin rerating was already crowded; 90D/180D MFE stayed near 5% while MAE deepened.", "current_profile_error": "C29 may over-credit headline OP growth without timing/exhaustion guard.", "component_scores": {"eps_fcf": 72, "visibility": 58, "bottleneck_pricing": 68, "mispricing": 34, "valuation_rerating": 35, "capital_allocation": 28, "info_confidence": 70}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|161390|Stage2-FalsePositive|Local4B-Watch|2024-05-03", "representative_for_aggregate": true}
{"case_id": "C29_L179_002_HANKOOK_FY2024_RESET_POSITIVE", "ticker": "161390", "name": "한국타이어앤테크놀로지", "evidence_date": "2025-02-04", "entry_date": "2025-02-05", "entry_price": 37750.0, "trigger_type": "Stage2-Actionable", "case_label": "positive", "fine_archetype_id": "C29_TIRE_PREMIUM_MIX_RESET_ENTRY_MARGIN_DURABILITY", "MFE_30D_pct": 12.05, "MAE_30D_pct": -2.91, "MFE_90D_pct": 15.36, "MAE_90D_pct": -4.77, "MFE_180D_pct": 28.48, "MAE_180D_pct": -4.77, "D30_end": "2025-03-19", "D90_end": "2025-06-18", "D180_end": "2025-10-30", "evidence_url": "https://www.hankooktire.com/kr/ko/company/media-list/media-detail.630981.html", "evidence_summary": "FY2024 OP rose 32.7% to KRW 1.7622tn and OPM reached 18.7%; after the 2024 drawdown, the reset entry had low MAE and clean 180D upside.", "current_profile_error": "Earlier headline looked too late, but reset valuation plus durable premium mix should be allowed as C29 positive.", "component_scores": {"eps_fcf": 78, "visibility": 69, "bottleneck_pricing": 72, "mispricing": 64, "valuation_rerating": 66, "capital_allocation": 34, "info_confidence": 72}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|161390|Stage2-Actionable|2025-02-05", "representative_for_aggregate": true}
{"case_id": "C29_L179_003_KUMHO_Q1_2024_LATE_BLOWOFF", "ticker": "073240", "name": "금호타이어", "evidence_date": "2024-04-30", "entry_date": "2024-05-02", "entry_price": 7830.0, "trigger_type": "Stage2-FalsePositive|Local4B-Watch", "case_label": "counterexample", "fine_archetype_id": "C29_TIRE_TURNAROUND_LATE_HEADLINE_BLOWOFF", "MFE_30D_pct": 6.77, "MAE_30D_pct": -16.73, "MFE_90D_pct": 6.77, "MAE_90D_pct": -47.25, "MFE_180D_pct": 6.77, "MAE_180D_pct": -48.02, "D30_end": "2024-06-17", "D90_end": "2024-09-10", "D180_end": "2025-01-31", "evidence_url": "https://www.autoview.co.kr/ko-kr/articles/91320", "evidence_summary": "Q1 sales reached a 10-year first-quarter high and OP grew 167%, but price had already pulled forward the margin story; subsequent 90D/180D drawdown was severe.", "current_profile_error": "Volume/mix OP beat without price-exhaustion test becomes a high-MAE false positive.", "component_scores": {"eps_fcf": 76, "visibility": 55, "bottleneck_pricing": 66, "mispricing": 25, "valuation_rerating": 28, "capital_allocation": 22, "info_confidence": 68}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|073240|Stage2-FalsePositive|Local4B-Watch|2024-05-02", "representative_for_aggregate": true}
{"case_id": "C29_L179_004_KUMHO_Q3_2024_MIX_REORDER_RESET_POSITIVE", "ticker": "073240", "name": "금호타이어", "evidence_date": "2024-11-20", "entry_date": "2024-11-21", "entry_price": 4425.0, "trigger_type": "Stage2-Actionable|Stage3-Yellow-Watch", "case_label": "positive", "fine_archetype_id": "C29_TIRE_PREMIUM_MIX_RESET_ENTRY", "MFE_30D_pct": 14.58, "MAE_30D_pct": -1.81, "MFE_90D_pct": 21.81, "MAE_90D_pct": -5.31, "MFE_180D_pct": 21.81, "MAE_180D_pct": -8.25, "D30_end": "2025-01-06", "D90_end": "2025-04-07", "D180_end": "2025-08-19", "evidence_url": "https://file.alphasquare.co.kr/media/pdfs/company-ir/20241120%EA%B8%88%ED%98%B8%ED%83%80%EC%9D%B4%EC%96%B4_%EC%A6%9D%EA%B6%8C%EC%82%AC_%EC%A3%BC%EA%B4%80_%EA%B5%AD%EB%82%B4_NDR%28Non-Deal_Roadshow%29.pdf", "evidence_summary": "3Q24 NDR showed RE/OE growth, high-margin tire mix, 18-inch+ mix progress, EV tire supply ratio and Vietnam CAPA utilization. Reset price made the same tire thesis more usable.", "current_profile_error": "C29 needs a reset-entry allowance when the same margin bridge appears after valuation compression.", "component_scores": {"eps_fcf": 72, "visibility": 63, "bottleneck_pricing": 70, "mispricing": 61, "valuation_rerating": 60, "capital_allocation": 24, "info_confidence": 68}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|073240|Stage2-Actionable|Stage3-Yellow-Watch|2024-11-21", "representative_for_aggregate": true}
{"case_id": "C29_L179_005_NEXEN_FY2023_TURNAROUND_EARLY_POSITIVE", "ticker": "002350", "name": "넥센타이어", "evidence_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 8000.0, "trigger_type": "Stage2-Actionable", "case_label": "positive", "fine_archetype_id": "C29_TIRE_TURNAROUND_LOGISTICS_COST_AND_UTILIZATION", "MFE_30D_pct": 20.88, "MAE_30D_pct": -1.88, "MFE_90D_pct": 20.88, "MAE_90D_pct": -1.88, "MFE_180D_pct": 20.88, "MAE_180D_pct": -15.62, "D30_end": "2024-03-18", "D90_end": "2024-06-17", "D180_end": "2024-10-30", "evidence_url": "https://www.nexentire.com/kr/investment/ir_information/ir_report/__icsFiles/afieldfile/2024/01/31/NEXENTIRE.IR.Q4_KOR.pdf", "evidence_summary": "FY2023 turned to KRW 186.7bn OP from loss, with transport-cost relief and OE/RE demand recovery; early entry had clean 30D/90D MFE and shallow initial MAE.", "current_profile_error": "This is the positive control: confirmed margin turn plus utilization/cost bridge deserves Stage2 even before consensus catches up.", "component_scores": {"eps_fcf": 76, "visibility": 62, "bottleneck_pricing": 58, "mispricing": 66, "valuation_rerating": 58, "capital_allocation": 22, "info_confidence": 66}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|002350|Stage2-Actionable|2024-02-01", "representative_for_aggregate": true}
{"case_id": "C29_L179_006_NEXEN_2H24_CZECH_RAMP_LATE_HIGH_MAE", "ticker": "002350", "name": "넥센타이어", "evidence_date": "2024-05-29", "entry_date": "2024-05-30", "entry_price": 8010.0, "trigger_type": "Stage2-FalsePositive|HighMAE-Guard", "case_label": "counterexample", "fine_archetype_id": "C29_TIRE_CAPA_RAMP_FIXED_COST_RISK", "MFE_30D_pct": 3.75, "MAE_30D_pct": -5.37, "MFE_90D_pct": 3.75, "MAE_90D_pct": -15.73, "MFE_180D_pct": 3.75, "MAE_180D_pct": -35.08, "D30_end": "2024-07-11", "D90_end": "2024-10-14", "D180_end": "2025-02-26", "evidence_url": "https://ww2.imfnsec.com/upload/R_E08/2024/05/%5B29194037%5D_002350.pdf", "evidence_summary": "2H24 Czech expansion could improve logistics and volume, but the report itself flagged ramp/fixed-cost timing; price path showed almost no upside and deep 180D MAE.", "current_profile_error": "C29 should distinguish real utilization run-rate from forecast-only CAPA ramp.", "component_scores": {"eps_fcf": 55, "visibility": 48, "bottleneck_pricing": 50, "mispricing": 30, "valuation_rerating": 32, "capital_allocation": 20, "info_confidence": 62}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|002350|Stage2-FalsePositive|HighMAE-Guard|2024-05-30", "representative_for_aggregate": true}
{"case_id": "C29_L179_007_HANON_FY2024_EV_SLOWDOWN_STRUCTURE_COST_4C", "ticker": "018880", "name": "한온시스템", "evidence_date": "2025-02-13", "entry_date": "2025-02-14", "entry_price": 4360.0, "trigger_type": "Stage4C-ThesisBreak|HighMAE-Guard", "case_label": "counterexample", "fine_archetype_id": "C29_THERMAL_MANAGEMENT_EV_VOLUME_STRUCTURE_COST_BREAK", "MFE_30D_pct": 10.44, "MAE_30D_pct": -13.88, "MFE_90D_pct": 10.44, "MAE_90D_pct": -32.57, "MFE_180D_pct": 13.65, "MAE_180D_pct": -32.57, "D30_end": "2025-03-28", "D90_end": "2025-06-27", "D180_end": "2025-11-10", "evidence_url": "https://www.hankookandcompany.com/ko/media/news/article-2260.do", "evidence_summary": "FY2024 sales grew but Q4 OP turned to loss from one-off/restructuring costs, and EV customer volume shortfall plus impairment/interest burden drove net loss. MFE was capped while MAE deepened.", "current_profile_error": "EV thermal vocabulary can mask volume and balance-sheet pressure; require realized margin repair before Stage2.", "component_scores": {"eps_fcf": 30, "visibility": 42, "bottleneck_pricing": 45, "mispricing": 36, "valuation_rerating": 32, "capital_allocation": 18, "info_confidence": 70}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|018880|Stage4C-ThesisBreak|HighMAE-Guard|2025-02-14", "representative_for_aggregate": true}
{"case_id": "C29_L179_008_HYUNDAI_WIA_Q1_2025_FALSE_4C_POSITIVE", "ticker": "011210", "name": "현대위아", "evidence_date": "2025-04-30", "entry_date": "2025-05-02", "entry_price": 42450.0, "trigger_type": "Stage2-Watch|False4C-Audit", "case_label": "positive", "fine_archetype_id": "C29_AUTO_PARTS_MIX_DEFENSE_OFFSET_FALSE_4C", "MFE_30D_pct": 11.19, "MAE_30D_pct": -7.18, "MFE_90D_pct": 31.68, "MAE_90D_pct": -7.18, "MFE_180D_pct": 131.57, "MAE_180D_pct": -7.18, "D30_end": "2025-06-18", "D90_end": "2025-09-11", "D180_end": "2026-01-27", "evidence_url": "https://www.yna.co.kr/view/AKR20250430135201527", "evidence_summary": "Q1 OP fell 15.9% due to Mexico utilization and incentive burden, but sales were stable and pretax profit rose. Price path argues against hard 4C on one-quarter margin drag when offset businesses remain alive.", "current_profile_error": "Hard 4C should not fire on single-quarter utilization language when mix/defense/FX offsets can reset the thesis.", "component_scores": {"eps_fcf": 48, "visibility": 56, "bottleneck_pricing": 52, "mispricing": 72, "valuation_rerating": 70, "capital_allocation": 30, "info_confidence": 68}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|011210|Stage2-Watch|False4C-Audit|2025-05-02", "representative_for_aggregate": true}
{"case_id": "C29_L179_009_HYUNDAI_GLOVIS_Q1_2025_PCTC_RECORD_POSITIVE", "ticker": "086280", "name": "현대글로비스", "evidence_date": "2025-04-30", "entry_date": "2025-05-02", "entry_price": 107500.0, "trigger_type": "Stage3-Yellow|Stage2-Actionable", "case_label": "positive", "fine_archetype_id": "C29_MOBILITY_LOGISTICS_PCTC_CKD_OPERATING_LEVERAGE", "MFE_30D_pct": 27.81, "MAE_30D_pct": -2.79, "MFE_90D_pct": 78.33, "MAE_90D_pct": -2.79, "MFE_180D_pct": 175.35, "MAE_180D_pct": -2.79, "D30_end": "2025-06-18", "D90_end": "2025-09-11", "D180_end": "2026-01-27", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250430000160&docno=&method=search&viewerhost=", "evidence_summary": "1Q25 revenue was KRW 7.2234tn and OP KRW 501.884bn; separate reports describe record quarterly OP and broad logistics/shipping/distribution strength. This is the clean C29 operating-leverage positive.", "current_profile_error": "C29 should allow logistics/PCTC operating leverage, not only OEM/parts unit volume, when margin and commercial bridge are explicit.", "component_scores": {"eps_fcf": 86, "visibility": 78, "bottleneck_pricing": 72, "mispricing": 76, "valuation_rerating": 78, "capital_allocation": 44, "info_confidence": 78}, "row_type": "trigger", "round": "R9", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "entry_price_field": "c", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "dedupe_key": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|086280|Stage3-Yellow|Stage2-Actionable|2025-05-02", "representative_for_aggregate": true}
```

## 9. Aggregate / shadow / residual JSONL

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 179, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "new_independent_case_count": 9, "calibration_usable_trigger_count": 9, "representative_trigger_count": 9, "positive_case_count": 5, "counterexample_count": 4, "stage4b_watch_or_overlay_count": 5, "stage4c_or_false4c_audit_count": 2, "current_profile_error_count": 6, "index_baseline_coverage_before": 90, "index_baseline_coverage_after_if_accepted": 99, "session_aware_note": "loop123 C29 used OEM/Mobis/Mando/Hyundai/Kia style cases; loop179 uses tire, thermal, auto-parts offset and logistics/PCTC cases with no exact duplicate key."}
{"row_type": "shadow_rule_candidate", "rule_id": "C29_VOLUME_MARGIN_RESET_ENTRY_AND_OPERATIONAL_LEVERAGE_GATE_V2", "target_scope": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "production_scoring_changed": false, "shadow_weight_only": true, "rule_summary": "C29 should require realized volume/mix or logistics utilization plus margin/OP conversion and should add a reset-entry guard. Late record-profit or OP-beat headlines after price exhaustion remain Local4B/HighMAE watch; reset valuation with durable premium mix, PCTC/CKD logistics leverage, or offset businesses can remain Stage2/Yellow.", "proposed_stage2_required_bridge": ["volume_or_shipment_growth", "premium_mix_or_OE_RE_reorder", "margin_or_OP_conversion", "valuation_reset_or_low_MAE_entry"], "proposed_blockers": ["late_headline_after_large_rerating", "forecast_only_CAPA_or_ramp", "EV_volume_shortfall_without_margin_repair", "single_quarter_margin_drag_without_offset_audit"]}
{"row_type": "residual_contribution", "new_axis_proposed": "c29_volume_margin_reset_entry_and_operational_leverage_gate_v2", "existing_axis_strengthened": ["price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "hard_4c_requires_non_price_thesis_break"], "existing_axis_weakened": ["hard_4c_should_not_fire_on_single_quarter_utilization_or_margin_drag_if_offset_bridge_alive"], "residual_error_found": "Current proxy can over-credit tire OP beats and under-credit reset-entry logistics/tire operating leverage; C29 needs timing and reset-entry distinction."}
```

## 10. Narrative-only blocked row

```jsonl
{"row_type":"narrative_only","case_id":"C29_L179_NARR_HANON_Q1_2024_CORPACT_BLOCKED","ticker":"018880","name":"한온시스템","evidence_date":"2024-05-09","would_be_entry_date":"2024-05-10","reason":"corporate_action_contaminated_180D_window","blocked_window_note":"018880 profile has 2025-01-09 corporate-action candidate, and the 2024-05-10 entry D+180 window ends 2025-02-07, so it overlaps.","evidence_url":"https://www.hanonsystems.com/Kr/Media/NewsDetails/293","research_use":"Narrative only: Q1 record sales and improvement-program language would have been a false positive, but strict v12 validation blocks the row."}
```

## 11. Residual contribution summary

```text
new_axis_proposed = c29_volume_margin_reset_entry_and_operational_leverage_gate_v2
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|local_4b_watch_guard|hard_4c_confirmation
existing_axis_weakened = hard_4c_should_not_fire_on_single_quarter_utilization_or_margin_drag_if_offset_bridge_alive
do_not_propose_new_weight_delta = false
loop_contribution_label = canonical_archetype_rule_candidate
```

C29 should behave less like a single OEM-volume bucket and more like a gearbox. OEM volume, tire premium mix, logistics/PCTC capacity, thermal-management content and auto-parts offset are different gears. The rule should ask whether the gear is actually engaged with margin torque, not merely whether the engine headline sounds loud.

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.

Goal: In a later coding-agent session, ingest this Markdown as a v12 research artifact. Parse trigger rows, aggregate rows, shadow_rule_candidate, residual_contribution, and narrative_only blocks. Do not change production scoring directly from a single MD. Batch this file with other v12 outputs, validate 30/90/180D MFE/MAE fields, enforce corporate-action window blocking, dedupe by canonical_archetype_id + ticker + trigger_type + entry_date, and evaluate whether C29_VOLUME_MARGIN_RESET_ENTRY_AND_OPERATIONAL_LEVERAGE_GATE_V2 should become a small scoped patch or remain shadow-only.

Expected patch direction if repeatedly confirmed:
- C29 Stage2 bridge should require volume/shipment/order/logistics utilization + margin/OP conversion.
- Add late-headline high-MAE guard for tire and auto-parts OP beats.
- Add reset-entry exception when same evidence arrives after valuation compression with low MAE.
- Add false-4C audit when one-quarter utilization/margin drag is offset by other live business bridges.
```

## 13. Next research state

```text
completed_round = R9
completed_loop = 179
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
