# E2R Stock-Web v12 Residual Research — R3 / C13 Battery JV Utilization AMPC IRA

```text
output_file: e2r_stock_web_v12_residual_round_R3_loop_204_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
created_at: 2026-06-16
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
```

## 1. Selection / No-Repeat Check

```text
selected_round: R3
selected_loop: 204
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4

hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
novelty_policy: same canonical allowed; same symbol/date/trigger disallowed
```

R3/C13 was selected because the No-Repeat Index now says every canonical archetype is above the 80-row floor, so the next work is not raw coverage filling but direct evidence quality, URL/proxy repair, and balance reinforcement. C13 specifically remains a Priority 1 balance target for AMPC/IRA persistence and JV/utilization failure-mode repair.

This loop avoids the immediately preceding C10 memory-equipment run and focuses on battery separator, copper foil, cathode, and electrolyte rows where the model can confuse policy/JV/subsidy language with a real utilization or ex-subsidy margin bridge.

## 2. Price Source Validation

```text
price_source: Songdaiki/stock-web
manifest: atlas/manifest.json
schema: atlas/schema.json
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
tradable_columns: d,o,h,l,c,v,a,mc,s,m
MFE_N_pct: (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct: (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Profile-level corporate-action checks:

| symbol | profile last_date | corporate_action_candidate_count | candidate dates relevant to entry~D+180 | calibration use |
|---|---:|---:|---|---|
| 361610 | 2026-02-20 | 0 | none | usable |
| 020150 | 2026-02-20 | 0 | none | usable |
| 011790 | 2026-02-20 | 2 | only 1998/2001, outside window | usable |
| 278280 | 2026-02-20 | 0 | none | usable |
| 066970 | 2026-02-20 | 2 | 2016/2021, outside window | usable |
| 247540 | 2026-02-20 | 2 | 2022 only, outside window | usable |
| 393890 | 2026-02-20 | 0 | none | usable |

## 3. Coverage Matrix

```text
new_independent_case_count: 8
new_independent_trigger_count: 8
unique_symbol_count: 7

stage2_count: 0
stage2_actionable_count: 1
stage4b_count: 5
stage4c_count: 2

positive_or_reopen_case_count: 2
offset_or_guardrail_case_count: 4
hard_4c_positive_control_count: 2
current_profile_error_count: 5

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 4. Trigger Summary

| symbol | name | trigger | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | role |
|---|---|---|---:|---:|---:|---:|---:|---|
| 361610 | SK IE Technology | Stage4C | 2024-07-31 | 37300 | 2.01/-20.11 | 3.89/-39.28 | 3.89/-48.23 | hard_4c_positive_control |
| 361610 | SK IE Technology | Stage4B | 2025-02-06 | 23700 | 29.54/-6.54 | 29.54/-18.52 | 48.10/-18.52 | hard_4c_stickiness_error |
| 020150 | LOTTE Energy Materials | Stage4B | 2025-01-24 | 23050 | 36.88/-12.15 | 36.88/-15.57 | 36.88/-15.57 | loss_with_north_america_offset |
| 011790 | SKC / SK Nexilis | Stage4B | 2025-02-11 | 153700 | 6.90/-24.33 | 6.90/-44.11 | 6.90/-44.11 | growth_pillars_without_current_profit |
| 278280 | Chunbo | Stage2-Actionable | 2024-09-03 | 61300 | 7.18/-15.01 | 7.18/-42.25 | 7.18/-50.98 | direct_export_bridge_high_mae_cap |
| 066970 | L&F | Stage4B | 2024-05-09 | 150300 | 17.76/-2.53 | 17.76/-44.84 | 17.76/-48.97 | inventory_loss_with_product_offset_watch |
| 247540 | EcoPro BM | Stage4B | 2025-02-11 | 120700 | 17.40/-11.02 | 17.40/-32.81 | 49.13/-32.81 | inventory_loss_reversal_watch |
| 393890 | W-Scope Chungju Plant / WCP | Stage4C | 2024-11-14 | 13170 | 5.85/-17.69 | 5.85/-44.27 | 5.85/-48.75 | separator_chasm_true_break |

## 5. Case Notes

### 5.1 361610 SK IE Technology — Stage4C / Stage4B split

SK IE Technology's Q2 2024 result was a true utilization failure row: net loss, operating loss, and revenue collapse were all visible, so the 2024-07-31 row is a hard 4C positive-control row. The forward path also agrees: 180D MFE was only 3.89% while 180D MAE was -48.23%.

The 2025-02-06 annual-loss row looks ugly, but it should not stay sticky hard 4C if the evidence only says FY2024 red and does not confirm customer-contract collapse. The 180D MFE/MAE pair of 48.10% / -18.52% argues for Stage4B/watch with a reopen clock rather than permanent 4C.

### 5.2 020150 LOTTE Energy Materials — loss with North America offset

The FY2024 row shows operating loss, but the company also disclosed sales growth from diversified customers and North America despite EV slowdown. That is not enough for Actionable, but it is enough to avoid a hard 4C thesis-break label. This is a Stage4B offset-quality row: 180D MFE/MAE was 36.88% / -15.57%.

### 5.3 011790 SKC / SK Nexilis — growth pillars without current profit

SKC's 2024 revenue grew, but operating losses widened. The battery-materials pillar still lacked current operating conversion, so this is not Actionable; it belongs in Stage4B/watch. The deep 90D/180D MAE shows why Green must stay blocked even when the narrative contains copper-foil recovery language.

### 5.4 278280 Chunbo — direct export bridge but Green blocker

Chunbo is the cleanest direct-bridge row in this batch: North America-bound additive/electrolyte shipments are a better bridge than policy language alone. But the 180D MAE was -50.98%, so the row should be Stage2-Actionable with a high-MAE Green blocker, not Yellow/Green.

### 5.5 066970 L&F — inventory valuation loss with product offset watch

L&F's Q1 2024 loss was tied to inventory valuation and raw-material price decline. NCMA/product shipment language can be an offset, but the forward path was still deeply negative. This supports Stage4B/watch and blocks Actionable until shipment/margin conversion is explicit.

### 5.6 247540 EcoPro BM — inventory-loss reversal watch

EcoPro BM's FY2024 loss and revenue shrink were real, but the later inventory-loss reversal thesis is an offset-quality signal. Because the 180D MFE was 49.13% while MAE was -32.81%, hard 4C should not be sticky; Stage4B/watch is the safer calibration label.

### 5.7 393890 WCP — separator chasm hard break

WCP's Q3 2024 operating-loss row is a cleaner hard-4C control than broad battery-material weakness: separator demand, EV chasm, and flexible new-line timing all point to a non-price utilization thesis break. The 180D path confirms the weakness with 5.85% MFE and -48.75% MAE.

## 6. Score / Return Alignment

```text
current_profile_proxy: e2r_2_2_rolling_calibrated
canonical_runtime_weight_C13: EPS/Vis/Bott/Mis/Val/Cap/Info = 20/18/14/12/10/10/16
stage3_green_not_loosened: true
stage2_required_bridge_axis: strengthened
local_4b_watch_guard_axis: strengthened
hard_4c_confirmation_axis: strengthened
```

Residual finding:

```text
- AMPC / IRA / JV / North America / customer diversification language is not enough for Actionable.
- Utilization rebound, shipment/call-off, ex-subsidy margin, direct customer volume, or actual operating conversion is the second bridge.
- Deep MAE on a direct-bridge row should block Yellow/Green first; it should not delete Stage2-Actionable.
- Ugly operating-loss rows with explicit offset or later recovery path should route to Stage4B/watch before hard 4C.
- Hard 4C should be reserved for utilization/call-off/margin thesis break plus weak offset quality.
```

## 7. Machine-Readable Trigger Rows JSONL

```jsonl
{"row_type": "trigger", "research_version": "v12_stock_web_residual", "selected_round": "R3", "selected_loop": 204, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4", "case_id": "C13_LOOP204_01_361610_2024-07-31", "symbol": "361610", "symbol_name": "SK IE Technology", "trigger_type": "Stage4C", "entry_date": "2024-07-31", "entry_price": 37300.0, "entry_ohlcv": {"o": 37100.0, "h": 37600.0, "l": 36600.0, "c": 37300.0, "v": 121162.0, "a": 4483486150.0, "m": "KOSPI"}, "mfe_30d_pct": 2.01, "mae_30d_pct": -20.11, "mfe_90d_pct": 3.89, "mae_90d_pct": -39.28, "mfe_180d_pct": 3.89, "mae_180d_pct": -48.23, "peak_180d_date": "2024-10-07", "peak_180d_price": 38750.0, "trough_180d_date": "2025-04-09", "trough_180d_price": 19310.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_summary": "Q2 2024 net loss / operating loss, revenue collapse, separator demand weakness", "evidence_url": "https://www.koreatimes.co.kr/business/companies/20240731/korean-companysk-ie-technology-reports-losses-in-q2", "case_role": "hard_4c_positive_control", "component_scores": {"eps_fcf_explosion": 5, "earnings_visibility": 5, "bottleneck_pricing": 4, "market_mispricing": 5, "valuation_rerating": 4, "capital_allocation": 5, "information_confidence": 16}, "raw_total_score": 44, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12_stock_web_residual", "selected_round": "R3", "selected_loop": 204, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4", "case_id": "C13_LOOP204_02_361610_2025-02-06", "symbol": "361610", "symbol_name": "SK IE Technology", "trigger_type": "Stage4B", "entry_date": "2025-02-06", "entry_price": 23700.0, "entry_ohlcv": {"o": 24100.0, "h": 24150.0, "l": 22700.0, "c": 23700.0, "v": 239250.0, "a": 5574330700.0, "m": "KOSPI"}, "mfe_30d_pct": 29.54, "mae_30d_pct": -6.54, "mfe_90d_pct": 29.54, "mae_90d_pct": -18.52, "mfe_180d_pct": 48.1, "mae_180d_pct": -18.52, "peak_180d_date": "2025-10-27", "peak_180d_price": 35100.0, "trough_180d_date": "2025-04-09", "trough_180d_price": 19310.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_summary": "FY2024 operating loss and revenue fall, but no explicit customer contract collapse; later utilization-recovery possibility", "evidence_url": "https://en.yna.co.kr/view/AEN20250206009600320", "case_role": "hard_4c_stickiness_error", "component_scores": {"eps_fcf_explosion": 6, "earnings_visibility": 6, "bottleneck_pricing": 4, "market_mispricing": 5, "valuation_rerating": 4, "capital_allocation": 6, "information_confidence": 14}, "raw_total_score": 45, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12_stock_web_residual", "selected_round": "R3", "selected_loop": 204, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4", "case_id": "C13_LOOP204_03_020150_2025-01-24", "symbol": "020150", "symbol_name": "LOTTE Energy Materials", "trigger_type": "Stage4B", "entry_date": "2025-01-24", "entry_price": 23050.0, "entry_ohlcv": {"o": 23150.0, "h": 23300.0, "l": 22550.0, "c": 23050.0, "v": 83993.0, "a": 1933601250.0, "m": "KOSPI"}, "mfe_30d_pct": 36.88, "mae_30d_pct": -12.15, "mfe_90d_pct": 36.88, "mae_90d_pct": -15.57, "mfe_180d_pct": 36.88, "mae_180d_pct": -15.57, "peak_180d_date": "2025-02-20", "peak_180d_price": 31550.0, "trough_180d_date": "2025-05-22", "trough_180d_price": 19460.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_summary": "FY2024 operating loss but sales increased from diversified customer base and North America sales", "evidence_url": "https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=128", "case_role": "loss_with_north_america_offset", "component_scores": {"eps_fcf_explosion": 8, "earnings_visibility": 8, "bottleneck_pricing": 7, "market_mispricing": 6, "valuation_rerating": 5, "capital_allocation": 7, "information_confidence": 13}, "raw_total_score": 54, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12_stock_web_residual", "selected_round": "R3", "selected_loop": 204, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4", "case_id": "C13_LOOP204_04_011790_2025-02-11", "symbol": "011790", "symbol_name": "SKC / SK Nexilis", "trigger_type": "Stage4B", "entry_date": "2025-02-11", "entry_price": 153700.0, "entry_ohlcv": {"o": 158900.0, "h": 164300.0, "l": 152500.0, "c": 153700.0, "v": 653541.0, "a": 103868653200.0, "m": "KOSPI"}, "mfe_30d_pct": 6.9, "mae_30d_pct": -24.33, "mfe_90d_pct": 6.9, "mae_90d_pct": -44.11, "mfe_180d_pct": 6.9, "mae_180d_pct": -44.11, "peak_180d_date": "2025-02-11", "peak_180d_price": 164300.0, "trough_180d_date": "2025-05-23", "trough_180d_price": 85900.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_summary": "FY2024 revenue growth but wider operating loss; EV battery, semiconductor, eco-friendly pillars as offset", "evidence_url": "https://www.skc.kr/m/eng/Conmmunication/news/newsDetail.do?seq=1625", "case_role": "growth_pillars_without_current_profit", "component_scores": {"eps_fcf_explosion": 7, "earnings_visibility": 7, "bottleneck_pricing": 6, "market_mispricing": 7, "valuation_rerating": 6, "capital_allocation": 8, "information_confidence": 14}, "raw_total_score": 55, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12_stock_web_residual", "selected_round": "R3", "selected_loop": 204, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4", "case_id": "C13_LOOP204_05_278280_2024-09-03", "symbol": "278280", "symbol_name": "Chunbo", "trigger_type": "Stage2-Actionable", "entry_date": "2024-09-03", "entry_price": 61300.0, "entry_ohlcv": {"o": 61000.0, "h": 62500.0, "l": 59900.0, "c": 61300.0, "v": 25780.0, "a": 1584695700.0, "m": "KOSDAQ"}, "mfe_30d_pct": 7.18, "mae_30d_pct": -15.01, "mfe_90d_pct": 7.18, "mae_90d_pct": -42.25, "mfe_180d_pct": 7.18, "mae_180d_pct": -50.98, "peak_180d_date": "2024-10-08", "peak_180d_price": 65700.0, "trough_180d_date": "2025-04-09", "trough_180d_price": 30050.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_summary": "North America-bound P-additive and F-electrolyte shipments expanded after 1Q inventory-loss bottom", "evidence_url": "https://securities.miraeasset.com/bbs/download/2130998.pdf?attachmentId=2130998", "case_role": "direct_export_bridge_high_mae_cap", "component_scores": {"eps_fcf_explosion": 12, "earnings_visibility": 11, "bottleneck_pricing": 9, "market_mispricing": 7, "valuation_rerating": 6, "capital_allocation": 8, "information_confidence": 13}, "raw_total_score": 66, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12_stock_web_residual", "selected_round": "R3", "selected_loop": 204, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4", "case_id": "C13_LOOP204_06_066970_2024-05-09", "symbol": "066970", "symbol_name": "L&F", "trigger_type": "Stage4B", "entry_date": "2024-05-09", "entry_price": 150300.0, "entry_ohlcv": {"o": 154400.0, "h": 154900.0, "l": 150000.0, "c": 150300.0, "v": 224619.0, "a": 34016848700.0, "m": "KOSPI"}, "mfe_30d_pct": 17.76, "mae_30d_pct": -2.53, "mfe_90d_pct": 17.76, "mae_90d_pct": -44.84, "mfe_180d_pct": 17.76, "mae_180d_pct": -48.97, "peak_180d_date": "2024-06-13", "peak_180d_price": 177000.0, "trough_180d_date": "2025-01-03", "trough_180d_price": 76700.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_summary": "Q1 2024 sales loss and inventory valuation loss; NCMA95 / shipment growth offset still not enough for Actionable", "evidence_url": "https://www.asiae.co.kr/en/article/2024050915570493698", "case_role": "inventory_loss_with_product_offset_watch", "component_scores": {"eps_fcf_explosion": 7, "earnings_visibility": 7, "bottleneck_pricing": 6, "market_mispricing": 6, "valuation_rerating": 5, "capital_allocation": 7, "information_confidence": 15}, "raw_total_score": 53, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12_stock_web_residual", "selected_round": "R3", "selected_loop": 204, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4", "case_id": "C13_LOOP204_07_247540_2025-02-11", "symbol": "247540", "symbol_name": "EcoPro BM", "trigger_type": "Stage4B", "entry_date": "2025-02-11", "entry_price": 120700.0, "entry_ohlcv": {"o": 120900.0, "h": 124000.0, "l": 118600.0, "c": 120700.0, "v": 674615.0, "a": 81965667400.0, "m": "KOSDAQ GLOBAL"}, "mfe_30d_pct": 17.4, "mae_30d_pct": -11.02, "mfe_90d_pct": 17.4, "mae_90d_pct": -32.81, "mfe_180d_pct": 49.13, "mae_180d_pct": -32.81, "peak_180d_date": "2025-10-27", "peak_180d_price": 180000.0, "trough_180d_date": "2025-05-27", "trough_180d_price": 81100.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_summary": "FY2024 loss and revenue shrink; inventory valuation loss/reversal expectation supports watch rather than sticky 4C", "evidence_url": "https://pulse.mk.co.kr/news/english/11237868", "case_role": "inventory_loss_reversal_watch", "component_scores": {"eps_fcf_explosion": 8, "earnings_visibility": 8, "bottleneck_pricing": 7, "market_mispricing": 7, "valuation_rerating": 6, "capital_allocation": 7, "information_confidence": 14}, "raw_total_score": 57, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12_stock_web_residual", "selected_round": "R3", "selected_loop": 204, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_REPAIR_V4", "case_id": "C13_LOOP204_08_393890_2024-11-14", "symbol": "393890", "symbol_name": "W-Scope Chungju Plant / WCP", "trigger_type": "Stage4C", "entry_date": "2024-11-14", "entry_price": 13170.0, "entry_ohlcv": {"o": 13690.0, "h": 13940.0, "l": 13170.0, "c": 13170.0, "v": 203563.0, "a": 2743756140.0, "m": "KOSDAQ GLOBAL"}, "mfe_30d_pct": 5.85, "mae_30d_pct": -17.69, "mfe_90d_pct": 5.85, "mae_90d_pct": -44.27, "mfe_180d_pct": 5.85, "mae_180d_pct": -48.75, "peak_180d_date": "2024-11-14", "peak_180d_price": 13940.0, "trough_180d_date": "2025-04-09", "trough_180d_price": 6750.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence_summary": "Q3 2024 separator operating loss, EV chasm, flexible capex/new-line timing", "evidence_url": "https://zdnet.co.kr/view/?no=20241114180902", "case_role": "separator_chasm_true_break", "component_scores": {"eps_fcf_explosion": 5, "earnings_visibility": 5, "bottleneck_pricing": 4, "market_mispricing": 4, "valuation_rerating": 4, "capital_allocation": 5, "information_confidence": 18}, "raw_total_score": 45, "production_scoring_changed": false, "shadow_weight_only": true}
```

## 8. Shadow Rule Candidate

```text
canonical_archetype_rule_candidate:
C13_EX_SUBSIDY_MARGIN_UTILIZATION_DIRECT_BRIDGE_GATE_V4

sector_rule_candidate:
L3_BATTERY_POLICY_TO_EX_SUBSIDY_AND_UTILIZATION_GATE_V4

rule_text:
AMPC/IRA/JV/regional supply-chain language alone does not create Stage2-Actionable or Yellow.
C13 Stage2-Actionable requires at least one direct second bridge:
eligible production volume, utilization rebound, customer pull/call-off,
shipment conversion, ex-subsidy margin, order/backlog-to-revenue,
or direct customer/JV supply route.

If reported operating profit is materially supported by tax credits or if reported losses come from
under-utilization / inventory adjustment / customer delay, Green remains blocked until ex-credit economics
or utilization recovery is visible.

Loss rows with explicit customer, North America, ESS, inventory-reversal, or product-shipment offset route to
Stage4B/watch before hard 4C. Hard 4C requires non-price utilization or margin thesis break plus weak offset quality.
```

## 9. Residual Contribution Summary

```text
loop_contribution_label:
C13_policy_subsidy_language_vs_direct_utilization_bridge_repair

new_axis_proposed:
no_global_axis

existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- hard_4c_confirmation
- stage3_green_not_loosened

existing_axis_refined:
- high_MAE_green_blocker_not_stage2_deletion
- hard_4c_stickiness_reopen_clock

existing_axis_weakened:
none

do_not_propose_new_weight_delta:
false
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When batch-applying later, parse this MD as a standard v12 result file.
Use every JSONL trigger row with calibration_usable=true.
Do not change production scoring directly from this file alone.
Aggregate with the full v12 corpus, then test whether C13-specific profile logic needs:
1. a stricter Stage2-Actionable second-bridge requirement for AMPC/IRA/JV language,
2. a Stage4B/watch route for ugly loss rows with explicit offset quality,
3. a hard-4C confirmation gate for utilization/call-off/margin break,
4. a Green blocker when AMPC/tax-credit or high-MAE is the main support.
```

## 11. Next Research State

```text
completed_round: R3
completed_loop: 204
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
