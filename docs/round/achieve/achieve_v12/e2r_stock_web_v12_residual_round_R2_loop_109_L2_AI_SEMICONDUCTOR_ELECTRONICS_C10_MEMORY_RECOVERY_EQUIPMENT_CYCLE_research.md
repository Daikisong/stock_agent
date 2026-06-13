# E2R Stock-Web V12 Residual Research — R2 loop 109 / L2 / C10

```yaml
selected_round: R2
selected_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: mixed_C10_memory_recovery_equipment_cycle_set
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
  - sector_specific_rule_discovery
output_filename: e2r_stock_web_v12_residual_round_R2_loop_109_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: '2026-02-20'
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` marks `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` as Priority 0 with 13 representative rows, leaving 17 rows to the 30-row stability floor and 37 rows to the 50-row practical calibration zone. Previous local outputs in this session already covered C18, C26, C29, C30, C02, C09, and C14, so this loop selects the next under-covered R2 canonical rather than mechanically rotating rounds.

C10 is the memory recovery equipment-cycle bucket. It should not merely capture "semiconductor mood improved". The calibration question is narrower: when does memory capex recovery become company-specific order, consumable reorder, utilization, segment-margin, or revenue-conversion evidence, and when is it just a fast beta rally that should be capped by local 4B watch?

## 2. Stock-Web manifest / schema validation

Manifest snapshot used:

```json
{ "atlas_version": "1.0.0", "generated_at": "2026-05-21T16:28:39.421691+00:00", "source_name": "FinanceData/marcap", "price_adjustment_status": "raw_unadjusted_marcap", "min_date": "1995-05-02", "max_date": "2026-02-20", "tradable_row_count": 14354401, "symbol_count": 5414 }
```

Schema basis used:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration usable requires entry row, positive OHLCV, 180 forward tradable rows, and non-contaminated 180D corporate-action window.
```

Price shards used:

```text
atlas/ohlcv_tradable_by_symbol_year/064/064760/2023.csv
atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv
atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv
atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv
atlas/ohlcv_tradable_by_symbol_year/074/074600/2025.csv
atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv
atlas/ohlcv_tradable_by_symbol_year/036/036200/2025.csv
atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv
atlas/ohlcv_tradable_by_symbol_year/281/281820/2025.csv
```

Profile checks:

```text
064760 티씨케이: corporate_action_candidate_count=0, last_date=2026-02-20, 180D window clean.
083310 엘오티베큠: corporate_action_candidate_dates=[2007-05-29, 2007-06-19], no overlap with 2024 trigger window.
074600 원익QnC: corporate_action_candidate_dates=[2004-06-25, 2004-07-21, 2017-04-28, 2017-05-24], no overlap with 2024-2025 trigger window.
036200 유니셈: corporate_action_candidate_dates=[2000-04-03, 2000-05-25, 2016-12-20, 2017-01-11], no overlap with 2024-2025 trigger window.
281820 케이씨텍: corporate_action_candidate_count=0, last_date=2026-02-20, 180D window clean.
```

## 3. Case set overview

|case_id|symbol|name|trigger_type|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|role|expected_shadow_route|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C10_064760_2023-11-23_Stage3-Yellow|064760|티씨케이|Stage3-Yellow|2023-11-23|99400|39.94|-6.34|50.8|-7.14|positive|Stage3-Yellow_or_green_watch_confirmed_consumable_reorder|
|C10_083310_2024-02-05_Stage2|083310|엘오티베큠|Stage2|2024-02-05|19390|26.1|-16.04|26.1|-52.04|counterexample|Stage2_block_or_4B_watch_due_non_memory_solar_mix|
|C10_074600_2024-10-23_Stage2|074600|원익QnC|Stage2|2024-10-23|24400|2.05|-31.64|2.05|-37.5|counterexample|Stage2_block_until_quartz_reorder_and_memory_demand_confirmed|
|C10_036200_2024-05-10_Stage2|036200|유니셈|Stage2|2024-05-10|9910|25.93|-38.75|25.93|-47.43|counterexample|Stage2_local_only_then_4B_watch_due_short_cycle_blowoff|
|C10_281820_2024-05-24_Stage2-Actionable|281820|케이씨텍|Stage2-Actionable|2024-05-24|37150|58.82|-20.73|58.82|-32.3|positive|Stage2-Actionable_then_local_4B_watch_after_fast_MFE|


## 4. Price-path calculation table

|symbol|entry|price|MFE30/MAE30|MFE90/MAE90|MFE180/MAE180|peak180|DD_after_peak|window_end|
|---|---|---|---|---|---|---|---|---|
|064760|2023-11-23|99400|19.32 / -4.12|39.94 / -6.34|50.8 / -7.14|2024-06-14 @ 149900|-38.43|2024-08-16|
|083310|2024-02-05|19390|26.1 / -1.19|26.1 / -16.04|26.1 / -52.04|2024-02-23 @ 24450|-61.96|2024-11-01|
|074600|2024-10-23|24400|2.05 / -26.97|2.05 / -31.64|2.05 / -37.5|2024-10-23 @ 24900|-38.76|2025-07-18|
|036200|2024-05-10|9910|24.92 / -4.64|25.93 / -38.75|25.93 / -47.43|2024-07-04 @ 12480|-58.25|2025-02-07|
|281820|2024-05-24|37150|34.59 / -1.75|58.82 / -20.73|58.82 / -32.3|2024-07-11 @ 59000|-57.37|2025-02-20|


## 5. Evidence notes by case

### 5.1 064760 티씨케이 — positive consumable reorder / NAND SiC focus ring route

Trigger evidence on 2023-11-23 tied the thesis to Lam Research share gains, Samsung 8th-generation V-NAND expansion, NAND turnaround, and SiC focus-ring sales recovery. This is a cleaner C10 positive than a generic semi equipment beta because the bridge runs through a consumable/parts reorder route attached to customer process adoption. The Stock-Web path confirmed a strong 180D MFE of +50.80% with only -7.14% MAE from entry, although the post-peak drawdown still shows why C10 should not be automatically Green without revision confirmation.

### 5.2 083310 엘오티베큠 — non-memory/solar mix contamination counterexample

The 2024-02-05 review showed excellent FY2023 headline profit and good 4Q23 profitability, but the driver was solar pump price/mix and diversification, not a clean memory equipment order cycle. The price path is a textbook local 4B watch: +26.10% MFE inside 30D, then -52.04% MAE by 180D and -61.96% drawdown after the 180D peak. C10 should decontaminate non-memory revenue drivers before accepting Stage2.

### 5.3 074600 원익QnC — quartz utilization thesis but memory-demand lag counterexample

The 2024-10-23 trigger cited 80-85% quartz utilization and expected 2025 quartz growth. That sounded C10-adjacent, but the same evidence set also carried a lowered 2024 operating-profit estimate and sector weakness. Stock-Web rejected the entry path: MFE never exceeded +2.05% while 180D MAE reached -37.50%. This case argues for a gate that distinguishes true consumable reorder/utilization confirmation from a forward-year expectation while the current-year estimate is still being cut.

### 5.4 036200 유니셈 — chiller/scrubber short-cycle blowoff

The 2024-05-10 trigger had real non-price support: 1Q24 sales and operating profit improved, and chiller equipment sales were presented as a recovery driver. However, the forward path turned into a short-cycle blowoff: +25.93% MFE by 90D, followed by -47.43% MAE by 180D. This is not a clean failure at the event date, but a failure of late 4B routing. C10 should route fast MFE plus missing durable order bridge to local 4B watch before the full-window collapse.

### 5.5 281820 케이씨텍 — CMP step-count positive, but peak guard required

The 2024-05-24 report linked the thesis to rising CMP process counts, memory customer CMP equipment supply, and HBM/high-performance semiconductor demand. The path validated the upside side: +58.82% 180D MFE. But after the 2024-07-11 peak, drawdown reached -57.37%, and 180D MAE was -32.30%. This is a positive C10 signal only if the profile also adds a 4B peak guard: Stage2-Actionable was justified, Green permanence was not.

## 6. Current calibrated profile stress test

C10 current seed weights from the No-Repeat table are interpreted as:

```text
EPS / Visibility / Bottleneck / Mispricing / Valuation / Capital / Info = 22 / 18 / 14 / 12 / 10 / 5 / 19
```

|symbol|current_total|shadow_total|delta|current_error|score_note|
|---|---|---|---|---|---|
|064760|74.0|75.7|1.7|false|Stage3-Yellow_or_green_watch_confirmed_consumable_reorder|
|083310|65.1|41.0|-24.1|true|Stage2_block_or_4B_watch_due_non_memory_solar_mix|
|074600|67.2|49.1|-18.1|true|Stage2_block_until_quartz_reorder_and_memory_demand_confirmed|
|036200|65.8|47.2|-18.6|true|Stage2_local_only_then_4B_watch_due_short_cycle_blowoff|
|281820|70.9|66.3|-4.6|true|Stage2-Actionable_then_local_4B_watch_after_fast_MFE|


Raw component-score simulation:

```jsonl
{"row_type": "score_simulation", "case_id": "C10_064760_2023-11-23_Stage3_Yellow", "weights_profile": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE EPS/Vis/Bott/Mis/Val/Cap/Info = 22/18/14/12/10/5/19", "current_proxy_component_scores": {"eps_fcf_explosion": 82, "earnings_visibility": 82, "bottleneck_pricing": 76, "market_mispricing": 64, "valuation_rerating": 58, "capital_allocation": 45, "information_confidence": 78}, "shadow_component_scores": {"eps_fcf_explosion": 84, "earnings_visibility": 84, "bottleneck_pricing": 80, "market_mispricing": 64, "valuation_rerating": 58, "capital_allocation": 45, "information_confidence": 80}, "current_proxy_total_score": 74.0, "shadow_total_score": 75.7, "shadow_delta": 1.7, "score_return_alignment": "positive"}
{"row_type": "score_simulation", "case_id": "C10_083310_2024-02-05_Stage2", "weights_profile": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE EPS/Vis/Bott/Mis/Val/Cap/Info = 22/18/14/12/10/5/19", "current_proxy_component_scores": {"eps_fcf_explosion": 78, "earnings_visibility": 70, "bottleneck_pricing": 58, "market_mispricing": 64, "valuation_rerating": 54, "capital_allocation": 40, "information_confidence": 64}, "shadow_component_scores": {"eps_fcf_explosion": 45, "earnings_visibility": 42, "bottleneck_pricing": 35, "market_mispricing": 40, "valuation_rerating": 35, "capital_allocation": 35, "information_confidence": 45}, "current_proxy_total_score": 65.1, "shadow_total_score": 41.0, "shadow_delta": -24.1, "score_return_alignment": "negative_or_guardrail"}
{"row_type": "score_simulation", "case_id": "C10_074600_2024-10-23_Stage2", "weights_profile": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE EPS/Vis/Bott/Mis/Val/Cap/Info = 22/18/14/12/10/5/19", "current_proxy_component_scores": {"eps_fcf_explosion": 74, "earnings_visibility": 74, "bottleneck_pricing": 66, "market_mispricing": 62, "valuation_rerating": 56, "capital_allocation": 40, "information_confidence": 70}, "shadow_component_scores": {"eps_fcf_explosion": 48, "earnings_visibility": 54, "bottleneck_pricing": 50, "market_mispricing": 44, "valuation_rerating": 40, "capital_allocation": 38, "information_confidence": 56}, "current_proxy_total_score": 67.2, "shadow_total_score": 49.1, "shadow_delta": -18.1, "score_return_alignment": "negative_or_guardrail"}
{"row_type": "score_simulation", "case_id": "C10_036200_2024-05-10_Stage2", "weights_profile": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE EPS/Vis/Bott/Mis/Val/Cap/Info = 22/18/14/12/10/5/19", "current_proxy_component_scores": {"eps_fcf_explosion": 74, "earnings_visibility": 72, "bottleneck_pricing": 64, "market_mispricing": 66, "valuation_rerating": 54, "capital_allocation": 35, "information_confidence": 66}, "shadow_component_scores": {"eps_fcf_explosion": 52, "earnings_visibility": 48, "bottleneck_pricing": 48, "market_mispricing": 46, "valuation_rerating": 36, "capital_allocation": 35, "information_confidence": 50}, "current_proxy_total_score": 65.8, "shadow_total_score": 47.2, "shadow_delta": -18.6, "score_return_alignment": "negative_or_guardrail"}
{"row_type": "score_simulation", "case_id": "C10_281820_2024-05-24_Stage2_Actionable", "weights_profile": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE EPS/Vis/Bott/Mis/Val/Cap/Info = 22/18/14/12/10/5/19", "current_proxy_component_scores": {"eps_fcf_explosion": 78, "earnings_visibility": 74, "bottleneck_pricing": 82, "market_mispricing": 66, "valuation_rerating": 52, "capital_allocation": 42, "information_confidence": 72}, "shadow_component_scores": {"eps_fcf_explosion": 74, "earnings_visibility": 70, "bottleneck_pricing": 80, "market_mispricing": 60, "valuation_rerating": 44, "capital_allocation": 42, "information_confidence": 66}, "current_proxy_total_score": 70.9, "shadow_total_score": 66.3, "shadow_delta": -4.6, "score_return_alignment": "positive"}
```

Interpretation:

- `064760` shows that C10 can work when the memory recovery bridge is customer/process/consumable-specific.
- `281820` shows that even a valid C10 upside setup needs a peak/4B guard after fast MFE.
- `083310`, `074600`, and `036200` show the residual error: the current profile can still over-accept equipment-cycle beta if non-memory mix, forward-year expectation, or short-cycle headline recovery is not filtered.

## 7. Local 4B vs full-window 4B split

```text
local_4B_watch_cases:
  - 083310: MFE30 +26.10%, MAE180 -52.04%, non-memory solar mix decontamination required.
  - 036200: MFE90 +25.93%, MAE180 -47.43%, chiller/scrubber recovery needed durable order bridge.
  - 281820: MFE180 +58.82%, DD-after-peak -57.37%, valid upside but requires peak guard.

full_4B_or_4C_cases:
  - none routed to hard 4C in this loop.
  - no confirmed thesis break such as order cancellation, qualification failure, or accounting/trust break was used.
```

C10 should therefore not simply punish every high-MAE case. The more precise guard is: if fast MFE occurs before company-specific order/revenue/margin confirmation, route to local 4B watch; if a non-memory revenue driver is responsible for the evidence, block C10 Stage2 until segment decontamination is explicit.

## 8. Shadow rule candidate

```yaml
sector_specific_rule_candidate: L2_C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONSUMABLE_GATE
canonical_archetype_rule_candidate: C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONSUMABLE_GATE_WITH_NON_MEMORY_MIX_CAP
new_axis_proposed:
  - C10_NON_MEMORY_REVENUE_MIX_DECONTAMINATION
  - C10_CONSUMABLE_REORDER_OR_CUSTOMER_CAPEX_CONFIRMATION_GATE
  - C10_FAST_MFE_HIGH_MAE_LOCAL_4B_WATCH
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: []
do_not_propose_new_weight_delta: false
```

Proposed behavior:

```text
If canonical_archetype_id == C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:
  require at least one of:
    - signed customer capex / equipment order / backlog conversion
    - consumable reorder or utilization confirmation
    - segment-level semi equipment revenue and margin bridge
    - customer-specific process adoption bridge
  penalize if:
    - evidence driver is non-memory, solar, display, or generic diversification
    - evidence is only a forward-year expectation while current-year estimates are being cut
    - fast MFE occurs without follow-through evidence
  route to:
    - Stage3-Yellow only when bridge + price path + low MAE align
    - Stage2-Actionable when bridge exists but peak/DD risk is high
    - local 4B watch when MFE30/90 >= 20% and MAE180 <= -30% without durable bridge
    - Stage2 block when non-memory mix is the real driver
```

## 9. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "case_id": "C10_064760_2023-11-23_Stage3_Yellow", "selected_round": "R2", "selected_loop": 109, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "NAND_SIC_FOCUS_RING_REORDER_MEMORY_RECOVERY", "symbol": "064760", "company_name": "티씨케이", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-11-23", "entry_date": "2023-11-23", "entry_price": 99400.0, "MFE_30D_pct": 19.32, "MAE_30D_pct": -4.12, "MFE_90D_pct": 39.94, "MAE_90D_pct": -6.34, "MFE_180D_pct": 50.8, "MAE_180D_pct": -7.14, "peak_180D_date": "2024-06-14", "peak_180D_price": 149900.0, "drawdown_after_peak_180D_pct": -38.43, "window_180D_end_date": "2024-08-16", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1700695558043.pdf", "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "2023-11-23 report framed Lam Research share gains and Samsung V8/V-NAND expansion as a SiC focus ring sales recovery route; 2024 revenue/OP were forecast to rebound materially.", "outcome_label": "positive_structural_success", "current_profile_error": false, "expected_shadow_route": "Stage3-Yellow_or_green_watch_confirmed_consumable_reorder", "loop_contribution_label": "canonical_archetype_rule_candidate"}
{"row_type": "trigger", "case_id": "C10_083310_2024-02-05_Stage2", "selected_round": "R2", "selected_loop": 109, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "DRY_VACUUM_PUMP_SOLAR_MIX_DECONTAMINATION", "symbol": "083310", "company_name": "엘오티베큠", "trigger_type": "Stage2", "trigger_date": "2024-02-05", "entry_date": "2024-02-05", "entry_price": 19390.0, "MFE_30D_pct": 26.1, "MAE_30D_pct": -1.19, "MFE_90D_pct": 26.1, "MAE_90D_pct": -16.04, "MFE_180D_pct": 26.1, "MAE_180D_pct": -52.04, "peak_180D_date": "2024-02-23", "peak_180D_price": 24450.0, "drawdown_after_peak_180D_pct": -61.96, "window_180D_end_date": "2024-11-01", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://kbthink.com/securities-view.html?docId=20240202162927173K", "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "2024-02-05 4Q23 review showed strong FY2023 profit but the driver was solar pump price/mix and diversification, not a clean memory recovery order bridge.", "outcome_label": "counterexample_high_mae_4b_watch", "current_profile_error": true, "expected_shadow_route": "Stage2_block_or_4B_watch_due_non_memory_solar_mix", "loop_contribution_label": "canonical_archetype_rule_candidate"}
{"row_type": "trigger", "case_id": "C10_074600_2024-10-23_Stage2", "selected_round": "R2", "selected_loop": 109, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "QUARTZ_UTILIZATION_RECOVERY_BUT_MEMORY_DEMAND_LAG", "symbol": "074600", "company_name": "원익QnC", "trigger_type": "Stage2", "trigger_date": "2024-10-23", "entry_date": "2024-10-23", "entry_price": 24400.0, "MFE_30D_pct": 2.05, "MAE_30D_pct": -26.97, "MFE_90D_pct": 2.05, "MAE_90D_pct": -31.64, "MFE_180D_pct": 2.05, "MAE_180D_pct": -37.5, "peak_180D_date": "2024-10-23", "peak_180D_price": 24900.0, "drawdown_after_peak_180D_pct": -38.76, "window_180D_end_date": "2025-07-18", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://www.thevaluenews.co.kr/news/186129", "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "2024-10-23 reports cited quartz utilization of 80–85% and expected 2025 quartz growth, while simultaneously noting semiconductor weakness and lowered 2024 operating profit estimate.", "outcome_label": "counterexample_false_stage2", "current_profile_error": true, "expected_shadow_route": "Stage2_block_until_quartz_reorder_and_memory_demand_confirmed", "loop_contribution_label": "canonical_archetype_rule_candidate"}
{"row_type": "trigger", "case_id": "C10_036200_2024-05-10_Stage2", "selected_round": "R2", "selected_loop": 109, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "CHILLER_SCRUBBER_Q1_RECOVERY_SHORT_CYCLE_BLOWOFF", "symbol": "036200", "company_name": "유니셈", "trigger_type": "Stage2", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 9910.0, "MFE_30D_pct": 24.92, "MAE_30D_pct": -4.64, "MFE_90D_pct": 25.93, "MAE_90D_pct": -38.75, "MFE_180D_pct": 25.93, "MAE_180D_pct": -47.43, "peak_180D_date": "2024-07-04", "peak_180D_price": 12480.0, "drawdown_after_peak_180D_pct": -58.25, "window_180D_end_date": "2025-02-07", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://securities.miraeasset.com/bbs/download/2126817.pdf?attachmentId=2126817", "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "2024-05-10 news highlighted 1Q24 sales/OP growth and chiller equipment sales strength after semiconductor recovery/tax investment expectations, but the price path became a high-MAE full-window failure.", "outcome_label": "counterexample_local_mfe_full_window_mae", "current_profile_error": true, "expected_shadow_route": "Stage2_local_only_then_4B_watch_due_short_cycle_blowoff", "loop_contribution_label": "canonical_archetype_rule_candidate"}
{"row_type": "trigger", "case_id": "C10_281820_2024-05-24_Stage2_Actionable", "selected_round": "R2", "selected_loop": 109, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "CMP_STEP_COUNT_MEMORY_HBM_CAPEX_LEVERAGE_WITH_4B_WATCH", "symbol": "281820", "company_name": "케이씨텍", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-24", "entry_date": "2024-05-24", "entry_price": 37150.0, "MFE_30D_pct": 34.59, "MAE_30D_pct": -1.75, "MFE_90D_pct": 58.82, "MAE_90D_pct": -20.73, "MFE_180D_pct": 58.82, "MAE_180D_pct": -32.3, "peak_180D_date": "2024-07-11", "peak_180D_price": 59000.0, "drawdown_after_peak_180D_pct": -57.37, "window_180D_end_date": "2025-02-20", "calibration_usable": true, "window_180D_corporate_action_contaminated": false, "source_url": "https://www.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01439926638892200", "source_proxy_only": false, "evidence_url_pending": false, "evidence_summary": "2024-05-24 DS/Edaily report tied KCTech to increasing CMP process steps, memory customer CMP equipment supply, and HBM/high-performance semiconductor demand.", "outcome_label": "positive_with_required_4b_peak_guard", "current_profile_error": true, "expected_shadow_route": "Stage2-Actionable_then_local_4B_watch_after_fast_MFE", "loop_contribution_label": "canonical_archetype_rule_candidate"}
```

## 10. Machine-readable aggregate / shadow / residual rows

```jsonl
{"row_type": "aggregate", "selected_round": "R2", "selected_loop": 109, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 3, "4B_case_count": 3, "4C_case_count": 0, "current_profile_error_count": 4, "calibration_usable_rows": 5, "representative_rows": 5, "source_proxy_only_rows": 0, "evidence_url_pending_rows": 0, "diversity_score_summary": "5 new symbols / 5 fine trigger families / positive 2 + counterexample 3 + 4B timing audit", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "shadow_weight", "axis": "C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONSUMABLE_GATE_WITH_NON_MEMORY_MIX_CAP", "scope": "canonical_archetype_specific", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "proposed_effect": "Increase information-confidence penalty and visibility decontamination when the recovery trigger is a generic memory beta or non-memory/solar mix rather than signed customer capex, consumable reorder, utilization, or segment-margin confirmation.", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": [], "new_axis_proposed": ["C10_NON_MEMORY_REVENUE_MIX_DECONTAMINATION", "C10_CONSUMABLE_REORDER_OR_CUSTOMER_CAPEX_CONFIRMATION_GATE", "C10_FAST_MFE_HIGH_MAE_LOCAL_4B_WATCH"]}
{"row_type": "residual_contribution", "this_loop_summary": "This loop adds 5 new independent cases, 3 counterexamples, and 4 residual errors for R2/L2/C10.", "main_residual_error": "C10 current proxy can still over-accept equipment beta when a short-cycle memory recovery headline lacks customer order/revenue conversion, or when the actual driver is solar/non-memory mix.", "rule_candidate": "C10 memory recovery equipment cycles need a bridge from macro recovery to company-specific equipment order, consumable reorder, utilization, or segment-margin conversion before Stage2/Yellow promotion; local MFE without durable bridge should route to 4B watch."}
{"row_type": "narrative_only", "note": "C10 is not C07 HBM order relative strength and not C09 advanced-equipment optionality. The selected cases isolate memory/legacy equipment-cycle beta and consumable recovery paths."}
```

## 11. Novelty and duplicate audit

```yaml
new_independent_case_count: 5
reused_case_count: 0
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 3
4B_case_count: 3
4C_case_count: 0
current_profile_error_count: 4
diversity_score_summary: 5 new symbols / 5 fine trigger families / positive 2 + counterexample 3 + 4B timing audit
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

Hard duplicate check:

```text
No row repeats canonical_archetype_id + symbol + trigger_type + entry_date from the visible top-covered C10 symbols in the current No-Repeat Index.
Selected symbols intentionally avoid the displayed C10 top-covered set: 036810, 036930, 067310, 079370, 084370, 095610.
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent. Do not rerun research. Ingest this MD as one V12 residual research artifact.

Task:
1. Parse machine-readable trigger rows, score_simulation rows, aggregate row, shadow_weight row, and residual_contribution row.
2. Validate that all trigger rows have selected_round=R2, selected_loop=109, large_sector_id=L2_AI_SEMICONDUCTOR_ELECTRONICS, canonical_archetype_id=C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.
3. Validate each trigger row has entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
4. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Treat the shadow axis as a candidate only: C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CONSUMABLE_GATE_WITH_NON_MEMORY_MIX_CAP.
6. Do not modify production scoring unless multiple accepted C10 rows across the batch support the same axis.
7. Add rejected ledger notes only if any row fails source, price, corporate action, or forward-window checks.
```

## 13. Final research state

```text
completed_round = R2
completed_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C11_BATTERY_ORDERBOOK_RERATING | C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

Next execution should again read the latest `V12_Research_No_Repeat_Index.md`; it should not mechanically proceed to R3. Based on the current ledger, the next high-value coverage candidates after C10 are C06, C07, C11, and C01 unless the ledger changes.

## 14. Batch Ingest Self-Audit

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
