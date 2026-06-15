# E2R v12 Residual Research — R5 / L5 / C19 BRAND_RETAIL_INVENTORY_MARGIN / loop 187

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
live_candidate_mode = false
current_stock_discovery_allowed = false
selected_round = R5
selected_loop = 187
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = mixed_c19_department_store_dutyfree_fashion_inventory_margin_leaf_set
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
output_filename = e2r_stock_web_v12_residual_round_R5_loop_187_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
```

## 1. Selection / No-Repeat Rationale

The original No-Repeat Index lists `C19_BRAND_RETAIL_INVENTORY_MARGIN` at 50 representative rows, already above the minimum 50-row line, but still one of the thinnest Priority 2 quality-repair areas. The prior session pass for this archetype, loop 159, covered Emart, Lotte Shopping, Brand X, FILA/Misto, F&F, BGF Retail, and Hyundai Department Store. This loop intentionally avoids that set and concentrates on a different fine leaf: department-store/duty-free/fashion brand inventory-margin quality, segment purity, and entry timing.

Hard duplicate avoidance:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
all_rows_new_vs_session_loop159 = true
same_archetype_allowed = true
same_symbol_same_entry_reused = false
```

## 2. Price Atlas Confirmation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
entry_price_basis = close(c) on entry_date
MFE_MAE_formula = strict post-entry N tradable rows; max(high) and min(low) versus entry close
corporate_action_window_rule = block if candidate overlaps entry_date through D+180
corporate_action_contaminated_180D_rows = 0
```

All trigger rows below have complete 30D/90D/180D MFE and MAE fields. No row uses price data after the stock-web manifest max date.

## 3. Core Finding

C19 should not read retail/brand earnings as a single warm lamp. The same headline can mean three different things:

1. **True margin repair**: inventory, markdown, SG&A and channel mix improve together.
2. **Segment-offset illusion**: one bright segment hides a weak listed-entity or weak fashion/retail core.
3. **Turnaround with entry danger**: the thesis is right, but the stock first forces a deep drawdown.

This loop therefore proposes a narrower C19 gate: Stage2-Actionable requires both a **retail/brand margin-quality bridge** and a **listed-entity purity bridge**. If the signal is only a segment result, one quarter of OP recovery, sales growth without margin, or a headline already followed by local peak extension, keep it at Stage2-Watch or attach local 4B/high-MAE guard.

## 4. Case Table

| case_id | ticker | name | trigger_date | entry_date | type | direction | MFE90 | MAE90 | MFE180 | MAE180 | read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C19_187_001 | 004170 | 신세계 | 2024-05-08 | 2024-05-09 | Stage2 | counterexample | 0.96 | -21.63 | 0.96 | -29.42 | counterexample |
| C19_187_002 | 008770 | 호텔신라 | 2024-04-30 | 2024-05-02 | 4B | counterexample | 5.04 | -23.04 | 5.04 | -37.57 | counterexample |
| C19_187_003 | 031430 | 신세계인터내셔날 | 2024-05-08 | 2024-05-09 | Stage2 | counterexample | 0.0 | -30.72 | 0.0 | -46.06 | counterexample |
| C19_187_004 | 020000 | 한섬 | 2024-11-07 | 2024-11-08 | 4C | positive | 7.48 | -7.94 | 17.16 | -11.94 | positive |
| C19_187_005 | 093050 | LF | 2024-06-19 | 2024-06-20 | Stage2 | positive | 7.09 | -9.85 | 15.5 | -9.85 | positive |
| C19_187_006 | 071840 | 롯데하이마트 | 2024-01-24 | 2024-01-25 | Stage2 | counterexample | 11.55 | -8.49 | 11.55 | -19.12 | counterexample |
| C19_187_007 | 028260 | 삼성물산 | 2024-04-24 | 2024-04-25 | Stage2 | counterexample | 5.0 | -13.72 | 5.0 | -25.12 | counterexample |
| C19_187_008 | 078520 | 에이블씨엔씨 | 2023-06-23 | 2023-06-26 | Stage2 | positive | 92.89 | -29.46 | 92.89 | -29.46 | positive |

## 5. Case Notes

### C19_187_001 — Shinsegae / Q1 subsidiary flourish but duty-free quality gap
Shinsegae's Q1 headline showed operating-profit growth and subsidiary support, while Shinsegae International and Central City also helped. But the stock path was unforgiving: only +0.96% MFE through 180D and -29.42% MAE. This is a clean C19 false-positive case. Good department-store or subsidiary growth is not enough if duty-free/retail margin durability and consolidated quality are not separately proven.

### C19_187_002 — Hotel Shilla / duty-free sales up, operating margin down
Hotel Shilla is the textbook C19 trap: revenue rose, especially duty-free sales, but operating profit fell sharply and operating margin compressed. The price path gives the answer: +5.04% MFE and -37.57% MAE by 180D. Sales growth is the storefront; margin quality is the cash register.

### C19_187_003 — Shinsegae International / cosmetics offset cannot rescue fashion drag
Q1 cosmetics were strong and OP improved, but sales were slightly down and the fashion/portfolio restructuring gap remained. The stock never made a positive post-entry MFE in the calculated windows and reached -46.06% MAE by 180D. This should be Stage2-Watch at best unless consolidated brand/fashion margin durability is visible.

### C19_187_004 — Handsome / weak-quarter language should not become hard 4C too early
Handsome's Q3 OP fell due to weak domestic fashion consumption and unusually warm weather. The event looked like a thesis-break phrase, but the price path was not a hard 4C collapse: D180 MFE was +17.16% and MAE was -11.94%. The correct rule is false-4C audit: weather/consumption wording requires second confirmation before hard 4C.

### C19_187_005 — LF / cost-efficiency margin repair, but segment purity matters
LF had signs of cost-efficiency and margin recovery, but finance-segment noise and non-fashion contribution polluted the pure C19 read. The price path was low-MAE and modestly positive: +15.50% MFE / -9.85% MAE by 180D. This is not Green material; it is a Stage2-Watch-to-Actionable candidate only if fashion margin repair is separated from non-fashion profit.

### C19_187_006 — Lotte Himart / operating-profit return with sales decay
Lotte Himart returned to operating profit after losses, helped by premium appliances and private brands, but sales were still down sharply. The path gave only +11.55% MFE and -19.12% MAE by 180D. This is a low-alpha C19 repair, not a clean rerating.

### C19_187_007 — Samsung C&T / segment-only fashion signal, listed-entity dilution
Samsung C&T's fashion segment was resilient, but the listed company is not a pure fashion/retail C19 exposure. The stock path gave only +5.00% MFE and -25.12% MAE by 180D. Segment-only positives should not open C19 Stage2-Actionable unless segment materiality is large enough.

### C19_187_008 — Able C&C / true turnaround with high-MAE entry risk
Able C&C's overseas success and restructuring finally delivered a visible profit turnaround. The thesis worked: D90/D180 MFE was +92.89%. But entry still required a -29.46% drawdown. This is not a block; it is a Stage2-Actionable-with-staged-entry case.

## 6. Machine-Readable Trigger Rows JSONL

```jsonl
{"row_type": "trigger", "case_id": "C19_187_001", "symbol": "004170", "company_name": "신세계", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_DEPARTMENT_STORE_SUBSIDIARY_DUTYFREE_MARGIN_DRAG", "trigger_date": "2024-05-08", "entry_date": "2024-05-09", "entry_price": 177100.0, "trigger_type": "Stage2", "trigger_subtype": "department_store_q1_subsidiary_flourish_but_dutyfree_risk", "MFE_30D_pct": 0.96, "MAE_30D_pct": -11.97, "MFE_90D_pct": 0.96, "MAE_90D_pct": -21.63, "MFE_180D_pct": 0.96, "MAE_180D_pct": -29.42, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_url": "https://www.yna.co.kr/view/AKR20240508092851527", "evidence_summary": "Q1 OP grew and subsidiaries helped, but price path immediately rejected the headline; duty-free/subsidiary quality and margin durability needed stronger confirmation.", "observed_outcome": "counterexample_high_MAE", "recommended_stage": "Stage2-Watch-or-Block", "current_profile_error_label": "good headline but inventory/duty-free margin bridge not enough"}
{"row_type": "trigger", "case_id": "C19_187_002", "symbol": "008770", "company_name": "호텔신라", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_DUTYFREE_REVENUE_UP_MARGIN_DOWN", "trigger_date": "2024-04-30", "entry_date": "2024-05-02", "entry_price": 57500.0, "trigger_type": "4B", "trigger_subtype": "dutyfree_sales_growth_operating_margin_collapse", "MFE_30D_pct": 5.04, "MAE_30D_pct": -3.48, "MFE_90D_pct": 5.04, "MAE_90D_pct": -23.04, "MFE_180D_pct": 5.04, "MAE_180D_pct": -37.57, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_url": "https://www.asiae.co.kr/en/print.htm?idxno=2024043017053041393", "evidence_summary": "Duty-free sales rose, but operating profit dropped sharply and OPM compressed; revenue growth without margin quality became a long drawdown.", "observed_outcome": "4B_high_MAE_counterexample", "recommended_stage": "Stage2-Watch-or-Block", "current_profile_error_label": "sales growth only; margin bridge missing"}
{"row_type": "trigger", "case_id": "C19_187_003", "symbol": "031430", "company_name": "신세계인터내셔날", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_COSMETICS_OFFSET_FASHION_DRAG", "trigger_date": "2024-05-08", "entry_date": "2024-05-09", "entry_price": 18260.0, "trigger_type": "Stage2", "trigger_subtype": "cosmetics_record_quarter_but_fashion_restructuring_gap", "MFE_30D_pct": 0.0, "MAE_30D_pct": -8.6, "MFE_90D_pct": 0.0, "MAE_90D_pct": -30.72, "MFE_180D_pct": 0.0, "MAE_180D_pct": -46.06, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_url": "https://www.mk.co.kr/en/economy/11010674", "evidence_summary": "Q1 OP improved and cosmetics hit record sales, but fashion restructuring/consumption drag dominated the price path; a segment offset cannot substitute for consolidated margin durability.", "observed_outcome": "hard_counterexample", "recommended_stage": "Stage2-Watch-or-Block", "current_profile_error_label": "positive segment offset over-read"}
{"row_type": "trigger", "case_id": "C19_187_004", "symbol": "020000", "company_name": "한섬", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_FASHION_WEATHER_SLOWDOWN_FALSE_4C", "trigger_date": "2024-11-07", "entry_date": "2024-11-08", "entry_price": 15500.0, "trigger_type": "4C", "trigger_subtype": "fashion_consumption_weather_weakness_false_break_audit", "MFE_30D_pct": 3.35, "MAE_30D_pct": -7.94, "MFE_90D_pct": 7.48, "MAE_90D_pct": -7.94, "MFE_180D_pct": 17.16, "MAE_180D_pct": -11.94, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_url": "https://v.daum.net/v/9iYBjg1mCC", "evidence_summary": "Q3 OP fell on weak domestic fashion consumption and abnormal warm weather, but subsequent MFE/MAE was not a thesis-collapse profile; weak-quarter language alone should be 4C-Watch, not hard 4C.", "observed_outcome": "false_4C_watch_positive", "recommended_stage": "Stage2-Watch", "current_profile_error_label": "hard 4C too early on weather/consumption wording"}
{"row_type": "trigger", "case_id": "C19_187_005", "symbol": "093050", "company_name": "LF", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_FASHION_COST_EFFICIENCY_MARGIN_RECOVERY", "trigger_date": "2024-06-19", "entry_date": "2024-06-20", "entry_price": 14520.0, "trigger_type": "Stage2", "trigger_subtype": "cost_efficiency_margin_recovery_but_finance_segment_pollution", "MFE_30D_pct": 1.86, "MAE_30D_pct": -7.02, "MFE_90D_pct": 7.09, "MAE_90D_pct": -9.85, "MFE_180D_pct": 15.5, "MAE_180D_pct": -9.85, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_url": "https://m.kisrating.com/fileDown.do?fileName=rs20240619-41.pdf&gubun=2&menuCd=R8", "evidence_summary": "KIS noted cost-efficiency and operating-margin recovery in 2024, while also highlighting finance-segment noise. The clean low-MAE path supports Stage2-Watch/Actionable only when fashion margin bridge is separated from non-fashion profits.", "observed_outcome": "low_MAE_positive_watch", "recommended_stage": "Stage2-Watch", "current_profile_error_label": "needs segment purity, but low MAE confirms watch quality"}
{"row_type": "trigger", "case_id": "C19_187_006", "symbol": "071840", "company_name": "롯데하이마트", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_ELECTRONICS_RETAIL_TURNAROUND_WITH_SALES_DECAY", "trigger_date": "2024-01-24", "entry_date": "2024-01-25", "entry_price": 9780.0, "trigger_type": "Stage2", "trigger_subtype": "profit_turnaround_with_revenue_decline_inventory_mix_gap", "MFE_30D_pct": 11.55, "MAE_30D_pct": -2.04, "MFE_90D_pct": 11.55, "MAE_90D_pct": -8.49, "MFE_180D_pct": 11.55, "MAE_180D_pct": -19.12, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_url": "https://en.yna.co.kr/view/AEN20240124009400320", "evidence_summary": "The company returned to operating profit, helped by high value-added appliances and private brands, but sales still fell sharply; path showed limited MFE and worsening MAE into D180.", "observed_outcome": "low_alpha_counterexample", "recommended_stage": "Stage2-Watch-or-Block", "current_profile_error_label": "profit repair without sales/reorder durability"}
{"row_type": "trigger", "case_id": "C19_187_007", "symbol": "028260", "company_name": "삼성물산", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_SEGMENT_ONLY_FASHION_SIGNAL_ENTITY_DILUTION", "trigger_date": "2024-04-24", "entry_date": "2024-04-25", "entry_price": 150100.0, "trigger_type": "Stage2", "trigger_subtype": "fashion_segment_resilient_but_conglomerate_dilution", "MFE_30D_pct": 3.13, "MAE_30D_pct": -11.73, "MFE_90D_pct": 5.0, "MAE_90D_pct": -13.72, "MFE_180D_pct": 5.0, "MAE_180D_pct": -25.12, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_url": "https://news.samsungcnt.com/ko/%EC%A0%84%EC%B2%B4%EA%B8%B0%EC%82%AC/%EC%A0%84%EC%82%AC%EA%B3%B5%ED%86%B5/2024-04-%EC%82%BC%EC%84%B1%EB%AC%BC%EC%82%B0-2024%EB%85%84-1%EB%B6%84%EA%B8%B0-%EC%8B%A4%EC%A0%81-%EB%B0%9C%ED%91%9C/", "evidence_summary": "Fashion segment held near prior-year levels despite weak consumption, but the listed entity is not a pure fashion/retail C19 exposure; segment-only positives diluted into a -25% D180 MAE path.", "observed_outcome": "segment_contaminated_counterexample", "recommended_stage": "Stage2-Watch-or-Block", "current_profile_error_label": "segment-only signal; listed-entity purity missing"}
{"row_type": "trigger", "case_id": "C19_187_008", "symbol": "078520", "company_name": "에이블씨엔씨", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_BUDGET_BEAUTY_OVERSEAS_RESTRUCTURING_TURNAROUND", "trigger_date": "2023-06-23", "entry_date": "2023-06-26", "entry_price": 7740.0, "trigger_type": "Stage2", "trigger_subtype": "missha_overseas_cost_restructuring_high_MAE_positive", "MFE_30D_pct": 5.04, "MAE_30D_pct": -29.46, "MFE_90D_pct": 92.89, "MAE_90D_pct": -29.46, "MFE_180D_pct": 92.89, "MAE_180D_pct": -29.46, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_url": "https://www.globalcosmeticsnews.com/able-cc-turns-first-profit-on-back-of-international-success/", "evidence_summary": "Missha/Able C&C returned to profit on overseas sales and restructuring. The case worked with huge MFE, but early MAE was also severe, so C19 needs staged-entry and 4B/high-MAE guard even for correct turnarounds.", "observed_outcome": "high_MAE_positive", "recommended_stage": "Stage2-Actionable-with-4B-entry-guard", "current_profile_error_label": "true turnaround but entry required drawdown guard"}
```

## 7. Score Simulation JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C19_187_001", "symbol": "004170", "score_proxy_note": "shadow stress-test only; not production scorer output", "raw_component_score_breakdown": {"eps_fcf": 14, "visibility": 9, "bottleneck": 5, "mispricing": 14, "valuation": 16, "capital": 5, "info": 16}, "score_total_proxy": 79, "current_profile_expected_failure": "good headline but inventory/duty-free margin bridge not enough", "suggested_override": "Stage2-Watch-or-Block"}
{"row_type": "score_simulation", "case_id": "C19_187_002", "symbol": "008770", "score_proxy_note": "shadow stress-test only; not production scorer output", "raw_component_score_breakdown": {"eps_fcf": 14, "visibility": 9, "bottleneck": 5, "mispricing": 14, "valuation": 16, "capital": 5, "info": 16}, "score_total_proxy": 79, "current_profile_expected_failure": "sales growth only; margin bridge missing", "suggested_override": "Stage2-Watch-or-Block"}
{"row_type": "score_simulation", "case_id": "C19_187_003", "symbol": "031430", "score_proxy_note": "shadow stress-test only; not production scorer output", "raw_component_score_breakdown": {"eps_fcf": 14, "visibility": 9, "bottleneck": 5, "mispricing": 14, "valuation": 16, "capital": 5, "info": 16}, "score_total_proxy": 79, "current_profile_expected_failure": "positive segment offset over-read", "suggested_override": "Stage2-Watch-or-Block"}
{"row_type": "score_simulation", "case_id": "C19_187_004", "symbol": "020000", "score_proxy_note": "shadow stress-test only; not production scorer output", "raw_component_score_breakdown": {"eps_fcf": 16, "visibility": 18, "bottleneck": 8, "mispricing": 15, "valuation": 15, "capital": 6, "info": 14}, "score_total_proxy": 92, "current_profile_expected_failure": "hard 4C too early on weather/consumption wording", "suggested_override": "Stage2-Watch"}
{"row_type": "score_simulation", "case_id": "C19_187_005", "symbol": "093050", "score_proxy_note": "shadow stress-test only; not production scorer output", "raw_component_score_breakdown": {"eps_fcf": 16, "visibility": 18, "bottleneck": 8, "mispricing": 15, "valuation": 15, "capital": 6, "info": 14}, "score_total_proxy": 92, "current_profile_expected_failure": "needs segment purity, but low MAE confirms watch quality", "suggested_override": "Stage2-Watch"}
{"row_type": "score_simulation", "case_id": "C19_187_006", "symbol": "071840", "score_proxy_note": "shadow stress-test only; not production scorer output", "raw_component_score_breakdown": {"eps_fcf": 14, "visibility": 12, "bottleneck": 5, "mispricing": 14, "valuation": 16, "capital": 5, "info": 13}, "score_total_proxy": 79, "current_profile_expected_failure": "profit repair without sales/reorder durability", "suggested_override": "Stage2-Watch-or-Block"}
{"row_type": "score_simulation", "case_id": "C19_187_007", "symbol": "028260", "score_proxy_note": "shadow stress-test only; not production scorer output", "raw_component_score_breakdown": {"eps_fcf": 14, "visibility": 12, "bottleneck": 5, "mispricing": 14, "valuation": 16, "capital": 5, "info": 13}, "score_total_proxy": 79, "current_profile_expected_failure": "segment-only signal; listed-entity purity missing", "suggested_override": "Stage2-Watch-or-Block"}
{"row_type": "score_simulation", "case_id": "C19_187_008", "symbol": "078520", "score_proxy_note": "shadow stress-test only; not production scorer output", "raw_component_score_breakdown": {"eps_fcf": 16, "visibility": 18, "bottleneck": 8, "mispricing": 15, "valuation": 11, "capital": 6, "info": 16}, "score_total_proxy": 90, "current_profile_expected_failure": "true turnaround but entry required drawdown guard", "suggested_override": "Stage2-Actionable-with-4B-entry-guard"}
```

## 8. Aggregate / Residual Contribution JSONL

```jsonl
{"row_type": "aggregate", "selected_round": "R5", "selected_loop": 187, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "mixed_c19_department_store_dutyfree_fashion_inventory_margin_leaf_set", "new_independent_case_count": 8, "usable_trigger_row_count": 8, "representative_trigger_count": 8, "positive_case_count": 3, "counterexample_count": 5, "stage4b_watch_or_overlay_count": 5, "stage4c_or_false4c_audit_count": 1, "current_profile_error_count": 7, "index_baseline_coverage_before": "C19 rows 50", "index_baseline_coverage_after_if_accepted": "C19 rows 58", "session_aware_after_loop159_loop187_if_accepted": "about C19 rows 66", "shadow_rule_candidate": "C19_SEGMENT_PURITY_INVENTORY_MARGIN_AND_ENTRY_GUARD_V2"}
```

## 9. Shadow Rule Candidate

```text
rule_id = C19_SEGMENT_PURITY_INVENTORY_MARGIN_AND_ENTRY_GUARD_V2
rule_scope = canonical_archetype:C19_BRAND_RETAIL_INVENTORY_MARGIN
production_scoring_changed = false
shadow_weight_only = true
```

Rule proposal:

```text
IF canonical_archetype_id == C19_BRAND_RETAIL_INVENTORY_MARGIN:
  require_stage2_actionable_bridge = (
    inventory_or_markdown_quality_confirmed
    OR sgna_efficiency_confirmed
    OR gross_margin_or_op_margin_expansion_confirmed
  )
  AND require_entity_purity_bridge = (
    listed_entity_retail_brand_segment_materiality_high
    OR segment_signal_backed_by_consolidated_op_or_revision
  )

  block_or_demote_to_stage2_watch IF:
    sales_growth_only_without_margin
    OR one_quarter_rebound_only
    OR segment_positive_diluted_by_conglomerate_entity
    OR dutyfree_or_retail_revenue_up_but_margin_down
    OR fashion_weather_consumption_wording_without_second_confirmation

  attach_local_4b_or_staged_entry_guard IF:
    MFE90_positive_but_MAE90 <= -20
    OR true turnaround has high early drawdown
```

Expected effect:

```text
- Reduce false Stage2 promotions in department-store/duty-free/fashion headlines.
- Avoid hard 4C on temporary weather/consumption shocks without second confirmation.
- Keep true high-MFE turnarounds like Able C&C usable, but with staged-entry/high-MAE guard.
```

## 10. Validation Scope

```text
validation_scope = historical_trigger_level_research_only
stock_agent_code_opened = false
stock_agent_code_patched = false
production_profile_changed = false
all_usable_rows_have_30_90_180_MFE_MAE = true
all_rows_use_stock_web_tradable_raw = true
entry_date_forward_180D_available = true
corporate_action_contaminated_180D_window = false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not treat this MD as an instruction to change production scoring blindly.

Input artifact:
- e2r_stock_web_v12_residual_round_R5_loop_187_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md

Tasks:
1. Parse trigger JSONL rows.
2. Validate required fields: entry_date, entry_price, trigger_type, MFE/MAE 30/90/180, large_sector_id, canonical_archetype_id.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Treat C19_SEGMENT_PURITY_INVENTORY_MARGIN_AND_ENTRY_GUARD_V2 as a shadow rule candidate only.
5. Compare against existing v12 promotion decisions and applied scoring specs.
6. Promote only if independent rows outside this MD confirm the same failure mode.
7. Preserve production_scoring_changed=false unless batch validation explicitly produces an apply_next_patch decision.
```

## 12. Next Research State

```text
completed_round = R5
completed_loop = 187
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|C22_INSURANCE_RATE_CYCLE_RESERVE|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
