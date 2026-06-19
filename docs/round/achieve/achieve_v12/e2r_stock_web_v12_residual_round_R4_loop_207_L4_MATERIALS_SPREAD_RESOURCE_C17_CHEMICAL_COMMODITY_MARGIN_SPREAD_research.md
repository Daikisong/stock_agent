# stock-web v12 residual calibration — R4 / L4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

```text
source_md_filename: e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
selected_round: R4
selected_loop: 207
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR
research_mode: post_calibrated_residual_historical_research_v12
selection_policy: coverage_index_first / no-repeat-index-as-dedup-ledger-only
production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

## 1. Execution scope and selection rationale

The main execution prompt for this run is the v12 post-calibrated residual historical research procedure. It requires actual `Songdaiki/stock-web` 1D OHLCV rows, forbids `stock_agent` code patching, live discovery, production scoring changes, and sets the hard duplicate key to `canonical_archetype_id + symbol + trigger_type + entry_date`. The selected round is therefore derived from the chosen canonical archetype rather than a strict sequential R1→R13 loop.

`V12_Research_No_Repeat_Index.md` was used only as the duplicate-avoidance ledger. The current ledger state is already beyond raw row scarcity: all C01~C32 are at or above the 80-row floor, so this run targets quality repair. Within L4, `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` has a large corpus but still needs hard-4C / offset-quality and direct-source cleanup. This batch avoids the immediately repeated C05/C01/C13/C10/C15 branches from the current session and adds a C17 chemical-spread boundary sample.

```text
hard_duplicate_key_format: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|symbol|trigger_type|entry_date
batch_duplicate_policy: no repeated symbol+trigger_type+entry_date within selected canonical
new_independent_case_count: 7
new_independent_trigger_count: 7
unique_symbol_count: 4
stage2_actionable_count: 1
stage4b_count: 4
stage4c_count: 2
```

## 2. Stock-Web price validation

```text
primary_price_source: Songdaiki/stock-web
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
tradable_schema: d,o,h,l,c,v,a,mc,s,m
mfe_mae_method: inclusive entry row; max high / min low over 30, 90, 180 tradable rows
```

Corporate-action note: Lotte Chemical (`011170`) has a profile-level corporate-action candidate on `2023-02-13`; all selected Lotte rows in this batch are 2024 or 2025 entries, so the selected 180D forward windows do not overlap that 2023 candidate. Older 2022 Lotte candidates were intentionally excluded from this run. All selected trigger rows have full 180-tradable-row forward windows before the manifest max date.

## 3. Actual entry OHLCV rows

| Symbol | Entry date | Open | High | Low | Close / entry | Volume | Amount | Market cap | Stock-Web shard |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 011170 | 2024-02-07 | 134,000 | 138,500 | 132,800 | 137,400 | 134,028 | 18,305,836,200 | 5,877,342,570,600 | `atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv` |
| 011170 | 2025-02-07 | 55,600 | 56,400 | 54,500 | 54,500 | 53,446 | 2,947,238,100 | 2,331,260,335,500 | `atlas/ohlcv_tradable_by_symbol_year/011/011170/2025.csv` |
| 011780 | 2024-01-29 | 115,300 | 128,200 | 115,200 | 125,400 | 242,536 | 29,966,832,900 | 3,579,878,946,600 | `atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv` |
| 298020 | 2022-01-05 | 550,000 | 563,000 | 534,000 | 551,000 | 120,792 | 66,334,635,000 | 2,384,552,782,000 | `atlas/ohlcv_tradable_by_symbol_year/298/298020/2022.csv` |
| 298020 | 2022-01-27 | 429,500 | 437,000 | 415,500 | 415,500 | 52,376 | 22,208,295,500 | 1,798,151,871,000 | `atlas/ohlcv_tradable_by_symbol_year/298/298020/2022.csv` |
| 009830 | 2024-02-22 | 32,950 | 33,100 | 28,900 | 29,300 | 4,885,784 | 147,306,269,000 | 5,036,451,304,800 | `atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv` |
| 009830 | 2025-01-31 | 20,100 | 20,450 | 19,620 | 19,770 | 1,318,668 | 26,175,834,270 | 3,398,315,436,720 | `atlas/ohlcv_tradable_by_symbol_year/009/009830/2025.csv` |

## 4. Trigger backtest summary

| Symbol | Company | Trigger | Entry date | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Case role |
|---|---|---|---:|---:|---:|---:|---:|---|
| 011170 | Lotte Chemical | Stage4C | 2024-02-07 | 137,400 | 1.38 / -14.99 | 1.38 / -30.06 | 1.38 / -44.32 | hard_4c_positive_control |
| 011170 | Lotte Chemical | Stage4B | 2025-02-07 | 54,500 | 46.79 / -4.95 | 46.79 / -4.95 | 46.79 / -4.95 | overhard_4c_guard_rebound_offset |
| 011780 | Kumho Petrochemical | Stage4B | 2024-01-29 | 125,400 | 30.70 / -8.13 | 30.70 / -8.13 | 33.17 / -8.13 | spread_compression_watch_positive_offset |
| 298020 | Hyosung TNC | Stage4B | 2022-01-05 | 551,000 | 10.71 / -27.31 | 10.71 / -34.39 | 10.71 / -53.09 | capacity_expansion_margin_risk_green_blocker |
| 298020 | Hyosung TNC | Stage2-Actionable | 2022-01-27 | 415,500 | 21.54 / -3.61 | 21.54 / -14.08 | 21.54 / -37.79 | true_actionable_but_green_blocked_by_high_mae |
| 009830 | Hanwha Solutions | Stage4C | 2024-02-22 | 29,300 | 12.97 / -9.56 | 17.92 / -21.50 | 17.92 / -43.48 | multi_segment_profit_break_hard_4c_control |
| 009830 | Hanwha Solutions | Stage4B | 2025-01-31 | 19,770 | 18.11 / -4.40 | 106.12 / -7.84 | 106.12 / -7.84 | non_chemical_offset_reopen_not_c17_green |

## 5. Evidence notes by case

### 5.1 Lotte Chemical — 2024 hard 4C positive control

Lotte Chemical's official 2023 business-performance release showed full-year operating loss and only partial deficit reduction through cost-lowering. In Stock-Web, the `2024-02-07` entry close was 137,400 KRW. The forward path had almost no upside (`180D MFE +1.38%`) and a deep `180D MAE -44.32%`. This is a valid C17 hard-4C positive control: the evidence is issuer-level, chemical-spread-linked, and the price path did not offer a favorable rebound window.

### 5.2 Lotte Chemical — 2025 over-hard-4C guard

Reuters later reported that Lotte's 2024 losses deepened materially amid persistent petrochemical oversupply. That headline is ugly enough for a thesis-break watch, but the `2025-02-07` entry had `180D MFE +46.79%` and only `180D MAE -4.95%`. The residual lesson is not bullish Green; it is that hard 4C should not remain sticky without fresh non-price confirmation after the loss is already priced.

### 5.3 Kumho Petrochemical — spread decline without hard 4C

Kumho Petrochemical's 2023 profitability fell because sales and spreads deteriorated. However, from the `2024-01-29` entry, Stock-Web shows `180D MFE +33.17%` and `180D MAE -8.13%`. A single spread-decline headline should be a local 4B/watch row unless there is issuer-level volume/profit collapse or offset failure.

### 5.4 Hyosung TNC — true tight-supply winner with later high-MAE cap

Hyosung TNC's 2021 spandex boom was a valid direct Stage2-Actionable signal: demand was strong, supply was tight, and operating profit surged. Yet the earlier 2022 capacity-risk report and the forward price path show why C17 Green must be strict. The `2022-01-27` record-profit row reached `180D MAE -37.79%`, and the earlier `2022-01-05` risk row reached `180D MAE -53.09%`. Record profit can preserve Stage2-Actionable, but it cannot bypass spread-duration and capacity-expansion checks.

### 5.5 Hanwha Solutions — chemical slowdown / multi-segment offset split

Hanwha Solutions' 2023 results contained both chemical weakness and non-chemical segment complexity. The `2024-02-22` row behaved like a valid hard-4C/control window, with `180D MAE -43.48%`. By contrast, the `2025-01-31` offset/reopen row had `180D MFE +106.12%` and `180D MAE -7.84%`, driven by AMPC/solar-hub style offset rather than a pure C17 chemical-spread recovery. This should reopen enterprise-level watch status, but it should not be counted as C17 chemical Green.

## 6. Raw component score simulation

C17 current-profile stress scoring uses the C17-like runtime profile as a lens, not as a production change. Component weights are interpreted as: `eps_fcf_explosion=20`, `earnings_visibility=12`, `bottleneck_pricing=18`, `market_mispricing=10`, `valuation_rerating=10`, `capital_allocation=5`, `information_confidence=25`.

| Symbol | Entry | Trigger | EPS/FCF | Visibility | Bottleneck/pricing | Mispricing | Valuation | Capital | Info | Total | Current profile error tested |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 011170 | 2024-02-07 | Stage4C | 2 | 2 | 2 | 3 | 1 | 0 | 20 | 30 | none_hard_4c_supported |
| 011170 | 2025-02-07 | Stage4B | 3 | 4 | 2 | 8 | 4 | 1 | 20 | 42 | hard_4c_too_sticky_after_loss_headline |
| 011780 | 2024-01-29 | Stage4B | 5 | 5 | 4 | 8 | 4 | 2 | 18 | 46 | hard_4c_if_spread_decline_used_alone |
| 298020 | 2022-01-05 | Stage4B | 8 | 5 | 5 | 5 | 4 | 1 | 18 | 46 | early_capacity_risk_not_reflected |
| 298020 | 2022-01-27 | Stage2-Actionable | 18 | 11 | 16 | 7 | 5 | 2 | 21 | 80 | green_if_record_profit_without_forward_capacity_check |
| 009830 | 2024-02-22 | Stage4C | 2 | 2 | 1 | 4 | 1 | 0 | 20 | 30 | none_hard_4c_supported_for_2024_window |
| 009830 | 2025-01-31 | Stage4B | 5 | 6 | 2 | 8 | 4 | 2 | 18 | 45 | chemical_4c_too_sticky_if_ampc_solar_offset_ignored |

## 7. Residual rule candidates

```text
canonical_rule_candidate:
C17_CHEMICAL_SPREAD_PERSISTENCE_AND_OFFSET_REOPEN_GATE

sector_rule_candidate:
L4_CHEMICAL_COMMODITY_MARGIN_SPREAD_DIRECT_SOURCE_GATE
```

Core residual:

1. Chemical spread / naphtha / commodity-margin headlines alone should not create Stage2-Actionable, Yellow, or Green.
2. Stage2-Actionable in C17 needs a second issuer-level bridge: segment profit conversion, forward spread persistence, utilization recovery, shipment/volume bridge, or cost/feedstock spread confirmation.
3. Hard 4C is valid when issuer-level operating loss, margin thesis break, weak offset quality, and forward price confirmation align. Lotte 2024 and Hanwha 2024 are positive controls.
4. Hard 4C must not become sticky after the loss headline is fully priced. If subsequent entry has low MAE and strong rebound, route to Stage4B/watch or capped Stage2 instead of hard 4C.
5. Tight-supply or record-profit C17 winners can be Stage2-Actionable, but capacity expansion and deep high-MAE paths block Yellow/Green.
6. Multi-segment offset such as AMPC or solar-hub benefit may repair enterprise price path, but it is not automatically a C17 chemical-spread positive bridge.

## 8. Batch ingest self-audit

```text
required_actual_stock_web_1d_ohlc_present: true
entry_price_present_for_all_rows: true
mfe_mae_30_90_180_present_for_all_rows: true
machine_readable_jsonl_present: true
price_source_validation_present: true
same_entry_duplicate_removed: true
hard_duplicate_key_checked_against_current_session_outputs: true
new_independent_ratio: 1.00
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
calibration_usable_trigger_count: 7
production_scoring_changed: false
shadow_weight_only: true
```

## 9. Machine-readable JSONL

```jsonl
{"actual_entry_ohlcv": {"a": 18305836200, "c": 137400, "d": "2024-02-07", "h": 138500, "l": 132800, "m": "KOSPI", "mc": 5877342570600, "o": 134000, "s": 42775419, "v": 134028}, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_role": "hard_4c_positive_control", "company_name": "Lotte Chemical", "current_profile_error": "none_hard_4c_supported", "entry_date": "2024-02-07", "entry_price": 137400, "evidence": {"evidence_date": "2024-02-07", "evidence_family": "official_results_operating_loss_cost_reduction", "source_url": "https://www.lottechem.com/en/news/report_view.do?bbsIdx=1062", "summary": "2023 business performance: revenue KRW 19.9491T and operating loss KRW 333.2B; deficit reduced by cost-lowering but chemical earnings still loss-making."}, "fine_archetype_id": "C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR", "hard_duplicate_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|Stage4C|2024-02-07", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "mfe_mae": {"180D": {"mae_pct": -44.32, "mfe_pct": 1.38, "peak_date": "2024-02-19", "peak_high": 139300, "trough_date": "2024-09-09", "trough_low": 76500, "window_end_date": "2024-11-05"}, "30D": {"mae_pct": -14.99, "mfe_pct": 1.38, "peak_date": "2024-02-19", "peak_high": 139300, "trough_date": "2024-03-20", "trough_low": 116800, "window_end_date": "2024-03-22"}, "90D": {"mae_pct": -30.06, "mfe_pct": 1.38, "peak_date": "2024-02-19", "peak_high": 139300, "trough_date": "2024-04-19", "trough_low": 96100, "window_end_date": "2024-06-21"}}, "price_source_validation": {"calculation": "inclusive_entry_row_max_high_min_low_over_N_tradable_rows", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "manifest_max_date": "2026-02-20", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "source_repo": "Songdaiki/stock-web", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv"}, "raw_component_score_breakdown": {"bottleneck_pricing": 2, "capital_allocation": 0, "earnings_visibility": 2, "eps_fcf_explosion": 2, "information_confidence": 20, "market_mispricing": 3, "valuation_rerating": 1}, "residual_contribution": "issuer-level operating loss and weak chemical spread evidence justify hard 4C; 180D MFE was only +1.38% while MAE reached -44.32%.", "row_type": "v12_trigger_case", "score_simulation": {"baseline_stage_candidate": "Stage2_or_4B4C_by_guardrail", "green_blocked_reason": "hard_4c_supported_by_non_price_thesis_break", "guardrail_adjusted_trigger": "Stage4C"}, "score_total": 30, "selected_loop": 207, "selected_round": "R4", "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "symbol": "011170", "trigger_type": "Stage4C"}
{"actual_entry_ohlcv": {"a": 2947238100, "c": 54500, "d": "2025-02-07", "h": 56400, "l": 54500, "m": "KOSPI", "mc": 2331260335500, "o": 55600, "s": 42775419, "v": 53446}, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_role": "overhard_4c_guard_rebound_offset", "company_name": "Lotte Chemical", "current_profile_error": "hard_4c_too_sticky_after_loss_headline", "entry_date": "2025-02-07", "entry_price": 54500, "evidence": {"evidence_date": "2025-02-10", "evidence_family": "reported_2024_loss_oversupply_persistence", "source_url": "https://www.reuters.com/markets/commodities/major-producers-south-koreas-petrochemical-hub-report-2024-losses-2025-02-10/", "summary": "Reuters reported Lotte Chemical 2024 operating losses deepened about 157% to KRW 895B amid global oversupply and sluggish demand."}, "fine_archetype_id": "C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR", "hard_duplicate_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011170|Stage4B|2025-02-07", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "mfe_mae": {"180D": {"mae_pct": -4.95, "mfe_pct": 46.79, "peak_date": "2025-03-07", "peak_high": 80000, "trough_date": "2025-02-10", "trough_low": 51800, "window_end_date": "2025-11-03"}, "30D": {"mae_pct": -4.95, "mfe_pct": 46.79, "peak_date": "2025-03-07", "peak_high": 80000, "trough_date": "2025-02-10", "trough_low": 51800, "window_end_date": "2025-03-21"}, "90D": {"mae_pct": -4.95, "mfe_pct": 46.79, "peak_date": "2025-03-07", "peak_high": 80000, "trough_date": "2025-02-10", "trough_low": 51800, "window_end_date": "2025-06-20"}}, "price_source_validation": {"calculation": "inclusive_entry_row_max_high_min_low_over_N_tradable_rows", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "manifest_max_date": "2026-02-20", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "source_repo": "Songdaiki/stock-web", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2025.csv"}, "raw_component_score_breakdown": {"bottleneck_pricing": 2, "capital_allocation": 1, "earnings_visibility": 4, "eps_fcf_explosion": 3, "information_confidence": 20, "market_mispricing": 8, "valuation_rerating": 4}, "residual_contribution": "2024 loss headline stayed ugly, but post-entry 30/90/180D MFE was +46.79% with only -4.95% MAE; loss headline needs fresh thesis-break confirmation before hard 4C persists.", "row_type": "v12_trigger_case", "score_simulation": {"baseline_stage_candidate": "Stage2_or_4B4C_by_guardrail", "green_blocked_reason": "high_MAE_or_missing_persistence_bridge", "guardrail_adjusted_trigger": "Stage4B"}, "score_total": 42, "selected_loop": 207, "selected_round": "R4", "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "symbol": "011170", "trigger_type": "Stage4B"}
{"actual_entry_ohlcv": {"a": 29966832900, "c": 125400, "d": "2024-01-29", "h": 128200, "l": 115200, "m": "KOSPI", "mc": 3579878946600, "o": 115300, "s": 28547679, "v": 242536}, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_role": "spread_compression_watch_positive_offset", "company_name": "Kumho Petrochemical", "current_profile_error": "hard_4c_if_spread_decline_used_alone", "entry_date": "2024-01-29", "entry_price": 125400, "evidence": {"evidence_date": "2024-01-29", "evidence_family": "spread_decline_profitability_drop", "source_url": "https://www.mk.co.kr/en/business/10932778", "summary": "Kumho Petrochemical profitability fell as sales and spreads declined in worsening petrochemical market conditions."}, "fine_archetype_id": "C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR", "hard_duplicate_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011780|Stage4B|2024-01-29", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "mfe_mae": {"180D": {"mae_pct": -8.13, "mfe_pct": 33.17, "peak_date": "2024-07-15", "peak_high": 167000, "trough_date": "2024-01-29", "trough_low": 115200, "window_end_date": "2024-10-25"}, "30D": {"mae_pct": -8.13, "mfe_pct": 30.7, "peak_date": "2024-02-19", "peak_high": 163900, "trough_date": "2024-01-29", "trough_low": 115200, "window_end_date": "2024-03-13"}, "90D": {"mae_pct": -8.13, "mfe_pct": 30.7, "peak_date": "2024-02-19", "peak_high": 163900, "trough_date": "2024-01-29", "trough_low": 115200, "window_end_date": "2024-06-12"}}, "price_source_validation": {"calculation": "inclusive_entry_row_max_high_min_low_over_N_tradable_rows", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "manifest_max_date": "2026-02-20", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "source_repo": "Songdaiki/stock-web", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv"}, "raw_component_score_breakdown": {"bottleneck_pricing": 4, "capital_allocation": 2, "earnings_visibility": 5, "eps_fcf_explosion": 5, "information_confidence": 18, "market_mispricing": 8, "valuation_rerating": 4}, "residual_contribution": "spread decline and profit compression were real, but 180D MFE +33.17% and MAE only -8.13% show that a single spread-decline headline should be 4B/watch, not hard 4C.", "row_type": "v12_trigger_case", "score_simulation": {"baseline_stage_candidate": "Stage2_or_4B4C_by_guardrail", "green_blocked_reason": "high_MAE_or_missing_persistence_bridge", "guardrail_adjusted_trigger": "Stage4B"}, "score_total": 46, "selected_loop": 207, "selected_round": "R4", "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "symbol": "011780", "trigger_type": "Stage4B"}
{"actual_entry_ohlcv": {"a": 66334635000, "c": 551000, "d": "2022-01-05", "h": 563000, "l": 534000, "m": "KOSPI", "mc": 2384552782000, "o": 550000, "s": 4327682, "v": 120792}, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_role": "capacity_expansion_margin_risk_green_blocker", "company_name": "Hyosung TNC", "current_profile_error": "early_capacity_risk_not_reflected", "entry_date": "2022-01-05", "entry_price": 551000, "evidence": {"evidence_date": "2022-01-05", "evidence_family": "capacity_expansion_margin_risk_forecast", "source_url": "https://www.asiae.co.kr/article/2022010508030227905", "summary": "2022 margin pressure was expected as excessive capacity expansion weighed on spandex profitability despite volume growth."}, "fine_archetype_id": "C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR", "hard_duplicate_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298020|Stage4B|2022-01-05", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "mfe_mae": {"180D": {"mae_pct": -53.09, "mfe_pct": 10.71, "peak_date": "2022-01-10", "peak_high": 610000, "trough_date": "2022-09-27", "trough_low": 258500, "window_end_date": "2022-09-28"}, "30D": {"mae_pct": -27.31, "mfe_pct": 10.71, "peak_date": "2022-01-10", "peak_high": 610000, "trough_date": "2022-01-28", "trough_low": 400500, "window_end_date": "2022-02-18"}, "90D": {"mae_pct": -34.39, "mfe_pct": 10.71, "peak_date": "2022-01-10", "peak_high": 610000, "trough_date": "2022-05-12", "trough_low": 361500, "window_end_date": "2022-05-18"}}, "price_source_validation": {"calculation": "inclusive_entry_row_max_high_min_low_over_N_tradable_rows", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "manifest_max_date": "2026-02-20", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "source_repo": "Songdaiki/stock-web", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2022.csv"}, "raw_component_score_breakdown": {"bottleneck_pricing": 5, "capital_allocation": 1, "earnings_visibility": 5, "eps_fcf_explosion": 8, "information_confidence": 18, "market_mispricing": 5, "valuation_rerating": 4}, "residual_contribution": "early capacity-expansion margin risk was a valid 4B/Green-blocker; after a small +10.71% MFE, 180D MAE reached -53.09%.", "row_type": "v12_trigger_case", "score_simulation": {"baseline_stage_candidate": "Stage2_or_4B4C_by_guardrail", "green_blocked_reason": "high_MAE_or_missing_persistence_bridge", "guardrail_adjusted_trigger": "Stage4B"}, "score_total": 46, "selected_loop": 207, "selected_round": "R4", "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "symbol": "298020", "trigger_type": "Stage4B"}
{"actual_entry_ohlcv": {"a": 22208295500, "c": 415500, "d": "2022-01-27", "h": 437000, "l": 415500, "m": "KOSPI", "mc": 1798151871000, "o": 429500, "s": 4327682, "v": 52376}, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_role": "true_actionable_but_green_blocked_by_high_mae", "company_name": "Hyosung TNC", "current_profile_error": "green_if_record_profit_without_forward_capacity_check", "entry_date": "2022-01-27", "entry_price": 415500, "evidence": {"evidence_date": "2022-01-27", "evidence_family": "tight_supply_spandex_record_profit", "source_url": "https://koreajoongangdaily.joins.com/2022/01/27/business/industry/Hyosung-TNC-spandex-operating-profit/20220127182837854.html", "summary": "Hyosung TNC 2021 sales and operating profit surged on high spandex demand and tight supply; record-profit headline was strong but later high-MAE risk emerged."}, "fine_archetype_id": "C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR", "hard_duplicate_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|298020|Stage2-Actionable|2022-01-27", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "mfe_mae": {"180D": {"mae_pct": -37.79, "mfe_pct": 21.54, "peak_date": "2022-03-04", "peak_high": 505000, "trough_date": "2022-09-27", "trough_low": 258500, "window_end_date": "2022-10-24"}, "30D": {"mae_pct": -3.61, "mfe_pct": 21.54, "peak_date": "2022-03-04", "peak_high": 505000, "trough_date": "2022-01-28", "trough_low": 400500, "window_end_date": "2022-03-16"}, "90D": {"mae_pct": -14.08, "mfe_pct": 21.54, "peak_date": "2022-03-04", "peak_high": 505000, "trough_date": "2022-05-19", "trough_low": 357000, "window_end_date": "2022-06-13"}}, "price_source_validation": {"calculation": "inclusive_entry_row_max_high_min_low_over_N_tradable_rows", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "manifest_max_date": "2026-02-20", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "source_repo": "Songdaiki/stock-web", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2022.csv"}, "raw_component_score_breakdown": {"bottleneck_pricing": 16, "capital_allocation": 2, "earnings_visibility": 11, "eps_fcf_explosion": 18, "information_confidence": 21, "market_mispricing": 7, "valuation_rerating": 5}, "residual_contribution": "tight supply and record profit support Stage2-Actionable, but capacity-cycle risk caused 180D MAE -37.79%; keep Green blocked without persistence evidence.", "row_type": "v12_trigger_case", "score_simulation": {"baseline_stage_candidate": "Stage3-Yellow", "green_blocked_reason": "high_MAE_or_missing_persistence_bridge", "guardrail_adjusted_trigger": "Stage2-Actionable"}, "score_total": 80, "selected_loop": 207, "selected_round": "R4", "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "symbol": "298020", "trigger_type": "Stage2-Actionable"}
{"actual_entry_ohlcv": {"a": 147306269000, "c": 29300, "d": "2024-02-22", "h": 33100, "l": 28900, "m": "KOSPI", "mc": 5036451304800, "o": 32950, "s": 171892536, "v": 4885784}, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_role": "multi_segment_profit_break_hard_4c_control", "company_name": "Hanwha Solutions", "current_profile_error": "none_hard_4c_supported_for_2024_window", "entry_date": "2024-02-22", "entry_price": 29300, "evidence": {"evidence_date": "2024-02-22", "evidence_family": "chemical_industry_slowdown_profit_break", "source_url": "https://koreajoongangdaily.joins.com/news/2024-02-22/business/industry/Hanwha-Solutions-logs-1st-annual-net-loss-since-2010/1987734", "summary": "Hanwha Solutions posted weaker 2023 profits and net loss; chemical industry slowdown weighed heavily, while solar offsets were not enough to avoid equity drawdown."}, "fine_archetype_id": "C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR", "hard_duplicate_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|009830|Stage4C|2024-02-22", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "mfe_mae": {"180D": {"mae_pct": -43.48, "mfe_pct": 17.92, "peak_date": "2024-05-28", "peak_high": 34550, "trough_date": "2024-11-14", "trough_low": 16560, "window_end_date": "2024-11-18"}, "30D": {"mae_pct": -9.56, "mfe_pct": 12.97, "peak_date": "2024-02-22", "peak_high": 33100, "trough_date": "2024-02-23", "trough_low": 26500, "window_end_date": "2024-04-04"}, "90D": {"mae_pct": -21.5, "mfe_pct": 17.92, "peak_date": "2024-05-28", "peak_high": 34550, "trough_date": "2024-04-26", "trough_low": 23000, "window_end_date": "2024-07-04"}}, "price_source_validation": {"calculation": "inclusive_entry_row_max_high_min_low_over_N_tradable_rows", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "manifest_max_date": "2026-02-20", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "source_repo": "Songdaiki/stock-web", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv"}, "raw_component_score_breakdown": {"bottleneck_pricing": 1, "capital_allocation": 0, "earnings_visibility": 2, "eps_fcf_explosion": 2, "information_confidence": 20, "market_mispricing": 4, "valuation_rerating": 1}, "residual_contribution": "chemical slowdown and net-loss evidence were accompanied by deep forward drawdown; 180D MAE was -43.48%, supporting hard 4C for that window.", "row_type": "v12_trigger_case", "score_simulation": {"baseline_stage_candidate": "Stage2_or_4B4C_by_guardrail", "green_blocked_reason": "hard_4c_supported_by_non_price_thesis_break", "guardrail_adjusted_trigger": "Stage4C"}, "score_total": 30, "selected_loop": 207, "selected_round": "R4", "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "symbol": "009830", "trigger_type": "Stage4C"}
{"actual_entry_ohlcv": {"a": 26175834270, "c": 19770, "d": "2025-01-31", "h": 20450, "l": 19620, "m": "KOSPI", "mc": 3398315436720, "o": 20100, "s": 171892536, "v": 1318668}, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_role": "non_chemical_offset_reopen_not_c17_green", "company_name": "Hanwha Solutions", "current_profile_error": "chemical_4c_too_sticky_if_ampc_solar_offset_ignored", "entry_date": "2025-01-31", "entry_price": 19770, "evidence": {"evidence_date": "2025-01-31", "evidence_family": "multi_segment_ampc_solar_hub_offset_reopen", "source_url": "https://www.topdaily.kr/articles/104355", "summary": "2025 coverage pointed to 4Q surplus expectations, AMPC contribution, and US Solar Hub as non-chemical offset/reopen bridge after petrochemical weakness."}, "fine_archetype_id": "C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR", "hard_duplicate_key": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|009830|Stage4B|2025-01-31", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "mfe_mae": {"180D": {"mae_pct": -7.84, "mfe_pct": 106.12, "peak_date": "2025-05-19", "peak_high": 40750, "trough_date": "2025-03-31", "trough_low": 18220, "window_end_date": "2025-10-27"}, "30D": {"mae_pct": -4.4, "mfe_pct": 18.11, "peak_date": "2025-02-14", "peak_high": 23350, "trough_date": "2025-02-03", "trough_low": 18900, "window_end_date": "2025-03-14"}, "90D": {"mae_pct": -7.84, "mfe_pct": 106.12, "peak_date": "2025-05-19", "peak_high": 40750, "trough_date": "2025-03-31", "trough_low": 18220, "window_end_date": "2025-06-13"}}, "price_source_validation": {"calculation": "inclusive_entry_row_max_high_min_low_over_N_tradable_rows", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "manifest_max_date": "2026-02-20", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "source_repo": "Songdaiki/stock-web", "stock_web_shard": "atlas/ohlcv_tradable_by_symbol_year/009/009830/2025.csv"}, "raw_component_score_breakdown": {"bottleneck_pricing": 2, "capital_allocation": 2, "earnings_visibility": 6, "eps_fcf_explosion": 5, "information_confidence": 18, "market_mispricing": 8, "valuation_rerating": 4}, "residual_contribution": "AMPC/solar hub offset created enterprise rebound, with 180D MFE +106.12% and MAE -7.84%; this reopens 4B/watch but should not be booked as C17 chemical Green.", "row_type": "v12_trigger_case", "score_simulation": {"baseline_stage_candidate": "Stage2_or_4B4C_by_guardrail", "green_blocked_reason": "high_MAE_or_missing_persistence_bridge", "guardrail_adjusted_trigger": "Stage4B"}, "score_total": 45, "selected_loop": 207, "selected_round": "R4", "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "symbol": "009830", "trigger_type": "Stage4B"}
{"calibration_usable_trigger_count": 7, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "corporate_action_contaminated_180D_count": 0, "evidence_url_pending_count": 0, "fine_archetype_id": "C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR", "insufficient_forward_window_180D_count": 0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "missing_required_mfe_mae_count": 0, "new_independent_case_count": 7, "new_independent_trigger_count": 7, "production_scoring_changed": false, "row_type": "v12_batch_aggregate", "rule_candidate": "C17_CHEMICAL_SPREAD_PERSISTENCE_AND_OFFSET_REOPEN_GATE", "selected_loop": 207, "selected_round": "R4", "shadow_weight_only": true, "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "source_proxy_only_count": 0, "stage2_actionable_count": 1, "stage4b_count": 4, "stage4c_count": 2, "unique_symbol_count": 4}
{"canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "do_not_auto_promote": true, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "production_scoring_changed": false, "proposed_rule_delta": {"bottleneck_pricing": "no_global_delta; require spread persistence not spot-margin headline", "earnings_visibility": "no_global_delta; add issuer-level loss persistence check for hard 4C", "information_confidence": "no_global_delta; direct URL quality repair only"}, "row_type": "v12_shadow_weight_proposal", "shadow_weight_only": true, "source_md_filename": "e2r_stock_web_v12_residual_round_R4_loop_207_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md"}
```

## 10. Deferred coding-agent handoff prompt

```text
Do not patch production scoring from this MD alone.
When running batch calibration, parse this MD as a v12 C17 quality-repair batch.
Use rows only if JSONL validates, entry OHLCV is present, and 30/90/180D MFE/MAE are complete.
Treat proposed C17 rule candidates as shadow-only until aggregate validation across C17 and R13 4B/4C holdout rows confirms them.
Pay special attention to sticky hard-4C errors after already-priced loss headlines and to multi-segment offset contamination.
```

## 11. Next research state

```text
completed_round: R4
completed_loop: 207
completed_large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
completed_canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
completed_fine_archetype_id: C17_NAPHTHA_CHEMICAL_SPREAD_HARD_4C_AND_OFFSET_REOPEN_REPAIR

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
