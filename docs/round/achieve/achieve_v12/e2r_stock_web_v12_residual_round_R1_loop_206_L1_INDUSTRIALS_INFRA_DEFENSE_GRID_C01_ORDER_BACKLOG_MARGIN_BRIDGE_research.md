# E2R v12 Stock-Web Sector/Archetype Residual Research — R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01 Shipbuilding Supplier Backlog-to-Cashflow Repair

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R1_loop_206_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round = R1
selected_loop = 206
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = C01_SHIPBUILDING_SUPPLIER_BACKLOG_TO_MARGIN_AND_CASHFLOW_GATE_V6
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement: C01 backlog-to-margin/FCF conversion repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Execution scope

This standalone research file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as the execution procedure. It does not open or patch `stock_agent` source code, does not run live discovery, does not recommend current stocks, and does not change production scoring. The only purpose is to add C01 residual evidence using actual Songdaiki/stock-web 1D OHLCV rows.

The No-Repeat Index is used only as a duplicate ledger and coverage-quality guide. The cumulative ledger has already passed raw row filling for C01~C32, so this loop targets a quality gap: shipbuilding supplier backlog/order headlines must be separated from actual delivery, margin, working-capital, and cashflow conversion.

## 2. Stock-Web price-atlas validation

```text
price_atlas_repo = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
```

MFE/MAE method: entry close vs max high / min low over inclusive 30/90/180 tradable-row windows. Raw OHLC is unadjusted. If a corporate-action candidate intersects the entry~D+180 window, the row is blocked from promotion/weight calibration. This batch has no 180D corporate-action contamination and no insufficient forward windows.

## 3. Novelty / duplicate check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This batch intentionally avoids recent C01 prime-yard and construction-equipment repetitions by moving into supplier-side LNG fittings, insulation, deck-house/tank modules, and backlog-to-margin/cash conversion.

```text
new_independent_case_count = 6
new_independent_trigger_count = 6
unique_symbol_count = 3
calibration_usable_trigger_count = 6
narrative_only_blocked_count = 0
stage2_count = 3
stage2_actionable_count = 3
stage4b_count = 0
stage4c_count = 0
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 4. Actual entry OHLC rows

| symbol | entry_date | actual stock-web row |
|---|---:|---|
| `014620` | 2025-03-20 | `2025-03-20,28200.0,28500.0,25400.0,25750.0,884479,23293476550,719160085250,27928547,KOSDAQ` |
| `014620` | 2025-05-13 | `2025-05-13,25400.0,25650.0,24500.0,25000.0,454347,11314753350,698213675000,27928547,KOSDAQ` |
| `017960` | 2024-01-18 | `2024-01-18,10630.0,10810.0,10580.0,10600.0,150307,1602049480,550229591200,51908452,KOSPI` |
| `017960` | 2025-05-16 | `2025-05-16,21850.0,21900.0,19720.0,20400.0,1299001,26691244075,1058932420800,51908452,KOSPI` |
| `075580` | 2024-04-02 | `2024-04-02,6560.0,7000.0,6500.0,6850.0,1379260,9398870090,389418773600,56849456,KOSPI` |
| `075580` | 2025-05-23 | `2025-05-23,11220.0,11440.0,10890.0,11300.0,2831019,31622744675,642398852800,56849456,KOSPI` |

## 5. Case matrix — calibration-usable rows

| # | symbol | company | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak/trough 180D | role |
|---:|---|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | `014620` | SungKwang Bend | Stage2 | 2025-03-20 | 25,750 | 14.56 / -12.43 | 43.30 / -12.43 | 50.68 / -12.43 | 2025-09-11 / 2025-04-07 | annual_report_direct_but_order_cash_bridge_missing |
| 2 | `014620` | SungKwang Bend | Stage2-Actionable | 2025-05-13 | 25,000 | 47.60 / -3.80 | 55.20 / -3.80 | 55.20 / -3.80 | 2025-09-11 / 2025-05-20 | q1_ir_order_cycle_reopen_with_green_block |
| 3 | `017960` | Korea Carbon | Stage2 | 2024-01-18 | 10,600 | 4.53 / -2.74 | 12.64 / -6.89 | 25.94 / -6.89 | 2024-08-20 / 2024-03-08 | lng_insulation_backlog_stage2_cap |
| 4 | `017960` | Korea Carbon | Stage2-Actionable | 2025-05-16 | 20,400 | 31.62 / -3.33 | 75.74 / -3.33 | 100.74 / -3.33 | 2026-01-12 / 2025-05-16 | direct_profit_margin_conversion_positive_control |
| 5 | `075580` | Sejin Heavy Industries | Stage2 | 2024-04-02 | 6,850 | 10.66 / -5.55 | 59.42 / -7.74 | 59.42 / -7.74 | 2024-07-17 / 2024-05-23 | supplier_profile_customer_route_stage2_cap |
| 6 | `075580` | Sejin Heavy Industries | Stage2-Actionable | 2025-05-23 | 11,300 | 14.60 / -9.03 | 142.48 / -9.03 | 142.48 / -9.03 | 2025-09-10 / 2025-07-07 | tank_delivery_profitability_positive_control_with_drawdown_cap |

## 6. Evidence ledger

| # | symbol | evidence date | evidence | URL | calibration use |
|---:|---|---:|---|---|---|
| 1 | `014620` | 2025-03-20 | 2024 annual report / official disclosure | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001932&method=search | Official 2024 annual report confirms reported results and provides issuer-level disclosure, but does not by itself prove 2025 order-to-cash conversion. |
| 2 | `014620` | 2025-05-13 | 2025 Q1 IR disclosure / industry Q&A | https://m.finance.daum.net/quotes/A014620/news/disclosure/20250513045998 | IR disclosure identifies 2025 Q1 management results and industry Q&A as the event, creating a more direct cycle-reopen row than a generic backlog story. |
| 3 | `017960` | 2024-01-18 | LNG order-boom / backlog report | https://www.sentv.co.kr/article/view/sentv202401180087 | K-LNG order-boom coverage cites Korea Carbon as a beneficiary with a large LNG cargo-tank insulation panel backlog, but cash/margin conversion is not yet proven at the trigger. |
| 4 | `017960` | 2025-05-16 | 1Q25 earnings surprise / order outlook | https://marketin.edaily.co.kr/News/ReadE?newsId=02217286642169576 | 1Q25 revenue and operating profit significantly beat expectations; source also ties LNGC insulation orders to expected backlog expansion and raw-material cost stability. |
| 5 | `075580` | 2024-04-02 | KIRS company report / supplier route | https://ssl.pstatic.net/imgstock/upload/research/company/1712013384054.pdf | KIRS report describes Sejin as a core HD Hyundai / Hyundai Mipo supplier with deck house, LPG/LNG tank, and module production routes, but this is still profile/order-route evidence before conversion. |
| 6 | `075580` | 2025-05-23 | 1Q25 tank delivery / margin bridge article | https://www.dailyinvest.kr/news/articleView.html?idxno=66768 | 2025 Q1 operating profit beat is linked to high-margin LCO2 tank delivery, tank shipment growth, and explicit margin outlook, providing a second bridge beyond backlog. |

## 7. Case notes

### 7.1 014620 / 2025-03-20 / Stage2

SungKwang Bend’s annual disclosure is issuer-level evidence, but the event remains a reported-result and cycle-position row. The forward path was strong enough to protect Stage2, yet the trigger lacked direct order-to-delivery, working-capital, or cash-conversion proof. This is a classic C01 cap row: backlog/cycle evidence can start the state machine but should not receive Actionable or Yellow credit by itself.

### 7.2 014620 / 2025-05-13 / Stage2-Actionable

The Q1 IR event improves evidence quality because it ties the row to current management results and industry discussion rather than a stale annual snapshot. The path was +55.20% / -3.80% over 180D. The residual is not bearish; it is a Green blocker. Actionable can reopen when the supplier cycle is live, but cashflow and repeat delivery evidence must still be required.

### 7.3 017960 / 2024-01-18 / Stage2

The LNG insulation backlog story is a real C01 bridge but still primarily backlog visibility. The path was positive, but not enough at entry to prove margin or cash conversion. Stage2 is retained, while Stage2-Actionable waits for realized profit, order delivery, or cash evidence.

### 7.4 017960 / 2025-05-16 / Stage2-Actionable

Korea Carbon’s 1Q25 earnings surprise, raw-material stability, and LNG insulation order outlook form a high-quality positive-control row. The 180D path was +100.74% / -3.33%. Even here, Green should not be loosened automatically because part of the quarter included delivery timing / swap effects and the rule still needs repeat cash or working-capital confirmation.

### 7.5 075580 / 2024-04-02 / Stage2

Sejin’s supplier-route report shows deep customer embedding with HD Hyundai and Hyundai Mipo, plus LNG/LPG tank and module capabilities. That is not the same thing as margin conversion. The row validates Stage2 but caps Actionable until tank delivery, order recognition, or profitability evidence arrives.

### 7.6 075580 / 2025-05-23 / Stage2-Actionable

The 2025 Q1 evidence is stronger: reported operating profit, high-margin tank delivery, and explicit shipment/profitability guidance create a second bridge. The path was +142.48% MFE, but the post-peak drawdown was nearly -38.87%; this supports Actionable/Yellow watch but keeps Green strict until cashflow and repeat evidence are visible.

## 8. Residual scoring interpretation

```text
rule_candidate = C01_SUPPLIER_BACKLOG_MARGIN_CASHFLOW_GATE_V6
sector_rule_candidate = L1_BACKLOG_TO_DELIVERY_MARGIN_AND_CASH_CONVERSION_GATE

core_residual:
- supplier backlog / LNG-cycle / customer-route evidence is valid Stage2 input, but it is not enough for Stage2-Actionable, Yellow, or Green.
- Stage2-Actionable needs at least one direct second bridge: delivery schedule, recognized revenue, high-margin product mix, operating-profit conversion, working-capital release, net-cash improvement, customer order quality, or repeat order.
- High MFE after supplier-cycle evidence should not loosen Stage3-Green by itself.
- High post-peak drawdown on supplier winners is a Green blocker, not a Stage2 deletion signal.
- Stage3-Green remains blocked until cashflow / working-capital conversion repeats across more than one evidence family.
```

## 9. Shadow weight / profile implication

```text
do_not_propose_new_weight_delta = false
production_scoring_changed = false
shadow_weight_only = true

shadow_profile_implication:
  C01_ORDER_BACKLOG_MARGIN_BRIDGE:
    stage2_required_bridge: strengthen
    stage2_actionable_requires_second_bridge: strengthen
    stage3_green_cashflow_requirement: strengthen
    high_MAE_or_post_peak_drawdown_green_blocker: strengthen
    backlog_headline_only_actionable_credit: weaken

component_pressure:
  earnings_visibility: + if realized profit or order-delivery bridge exists
  bottleneck_pricing: + only if product mix / high-margin delivery is explicit
  market_mispricing: no change from price-only path
  capital_allocation: + only if working-capital / net-cash evidence exists
  information_confidence: + for issuer-level IR/report or named broker/direct source, but not enough alone
```

## 10. Machine-readable JSONL trigger rows

```jsonl
{"research_file": "e2r_stock_web_v12_residual_round_R1_loop_206_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "row_id": 1, "selected_round": "R1", "selected_loop": 206, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLIER_BACKLOG_TO_MARGIN_AND_CASHFLOW_GATE_V6", "symbol": "014620", "company": "SungKwang Bend", "trigger_type": "Stage2", "trigger_date": "2025-03-20", "entry_date": "2025-03-20", "entry_price": 25750.0, "entry_ohlcv": {"d": "2025-03-20", "o": 28200.0, "h": 28500.0, "l": 25400.0, "c": 25750.0, "v": 884479, "a": 23293476550, "mc": 719160085250, "s": 27928547, "m": "KOSDAQ"}, "price_source_validation": {"repo": "Songdaiki/stock-web", "shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol_year_file": "014620_2025.csv", "manifest_max_date": "2026-02-20", "calculation": "entry close vs inclusive max high/min low over N tradable rows"}, "mfe_mae": {"30d": {"mfe_pct": 14.56, "mae_pct": -12.43, "peak_date": "2025-04-15", "trough_date": "2025-04-07"}, "90d": {"mfe_pct": 43.3, "mae_pct": -12.43, "peak_date": "2025-06-12", "trough_date": "2025-04-07"}, "180d": {"mfe_pct": 50.68, "mae_pct": -12.43, "peak_date": "2025-09-11", "trough_date": "2025-04-07", "post_peak_drawdown_pct": -34.02, "post_peak_trough_date": "2025-11-21"}}, "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence": {"label": "2024 annual report / official disclosure", "url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001932&method=search", "summary": "Official 2024 annual report confirms reported results and provides issuer-level disclosure, but does not by itself prove 2025 order-to-cash conversion."}, "case_role": "annual_report_direct_but_order_cash_bridge_missing", "profile_error": "actionable_overcredit_if_annual_result_or_cycle_backlog_headline_is_treated_as_cash_bridge", "residual_decision": "Stage2 cap; require order/delivery/cash bridge for Actionable.", "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|014620|Stage2|2025-03-20"}
{"research_file": "e2r_stock_web_v12_residual_round_R1_loop_206_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "row_id": 2, "selected_round": "R1", "selected_loop": 206, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLIER_BACKLOG_TO_MARGIN_AND_CASHFLOW_GATE_V6", "symbol": "014620", "company": "SungKwang Bend", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-05-13", "entry_date": "2025-05-13", "entry_price": 25000.0, "entry_ohlcv": {"d": "2025-05-13", "o": 25400.0, "h": 25650.0, "l": 24500.0, "c": 25000.0, "v": 454347, "a": 11314753350, "mc": 698213675000, "s": 27928547, "m": "KOSDAQ"}, "price_source_validation": {"repo": "Songdaiki/stock-web", "shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol_year_file": "014620_2025.csv", "manifest_max_date": "2026-02-20", "calculation": "entry close vs inclusive max high/min low over N tradable rows"}, "mfe_mae": {"30d": {"mfe_pct": 47.6, "mae_pct": -3.8, "peak_date": "2025-06-12", "trough_date": "2025-05-20"}, "90d": {"mfe_pct": 55.2, "mae_pct": -3.8, "peak_date": "2025-09-11", "trough_date": "2025-05-20"}, "180d": {"mfe_pct": 55.2, "mae_pct": -3.8, "peak_date": "2025-09-11", "trough_date": "2025-05-20", "post_peak_drawdown_pct": -35.7, "post_peak_trough_date": "2026-01-02"}}, "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence": {"label": "2025 Q1 IR disclosure / industry Q&A", "url": "https://m.finance.daum.net/quotes/A014620/news/disclosure/20250513045998", "summary": "IR disclosure identifies 2025 Q1 management results and industry Q&A as the event, creating a more direct cycle-reopen row than a generic backlog story."}, "case_role": "q1_ir_order_cycle_reopen_with_green_block", "profile_error": "green_overcredit_if_q1_ir_reopen_is_promoted_without_cashflow_or_repeat_delivery_bridge", "residual_decision": "Allow Actionable reopen; keep Yellow/Green blocked until cash conversion repeats.", "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|014620|Stage2-Actionable|2025-05-13"}
{"research_file": "e2r_stock_web_v12_residual_round_R1_loop_206_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "row_id": 3, "selected_round": "R1", "selected_loop": 206, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLIER_BACKLOG_TO_MARGIN_AND_CASHFLOW_GATE_V6", "symbol": "017960", "company": "Korea Carbon", "trigger_type": "Stage2", "trigger_date": "2024-01-18", "entry_date": "2024-01-18", "entry_price": 10600.0, "entry_ohlcv": {"d": "2024-01-18", "o": 10630.0, "h": 10810.0, "l": 10580.0, "c": 10600.0, "v": 150307, "a": 1602049480, "mc": 550229591200, "s": 51908452, "m": "KOSPI"}, "price_source_validation": {"repo": "Songdaiki/stock-web", "shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol_year_file": "017960_2024.csv", "manifest_max_date": "2026-02-20", "calculation": "entry close vs inclusive max high/min low over N tradable rows"}, "mfe_mae": {"30d": {"mfe_pct": 4.53, "mae_pct": -2.74, "peak_date": "2024-01-29", "trough_date": "2024-03-04"}, "90d": {"mfe_pct": 12.64, "mae_pct": -6.89, "peak_date": "2024-05-14", "trough_date": "2024-03-08"}, "180d": {"mfe_pct": 25.94, "mae_pct": -6.89, "peak_date": "2024-08-20", "trough_date": "2024-03-08", "post_peak_drawdown_pct": -21.65, "post_peak_trough_date": "2024-09-09"}}, "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence": {"label": "LNG order-boom / backlog report", "url": "https://www.sentv.co.kr/article/view/sentv202401180087", "summary": "K-LNG order-boom coverage cites Korea Carbon as a beneficiary with a large LNG cargo-tank insulation panel backlog, but cash/margin conversion is not yet proven at the trigger."}, "case_role": "lng_insulation_backlog_stage2_cap", "profile_error": "backlog_overcredit_without_delivery_margin_or_cashflow_bridge", "residual_decision": "Stage2 cap; direct backlog is real but not yet Actionable without conversion evidence.", "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|017960|Stage2|2024-01-18"}
{"research_file": "e2r_stock_web_v12_residual_round_R1_loop_206_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "row_id": 4, "selected_round": "R1", "selected_loop": 206, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLIER_BACKLOG_TO_MARGIN_AND_CASHFLOW_GATE_V6", "symbol": "017960", "company": "Korea Carbon", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-05-16", "entry_date": "2025-05-16", "entry_price": 20400.0, "entry_ohlcv": {"d": "2025-05-16", "o": 21850.0, "h": 21900.0, "l": 19720.0, "c": 20400.0, "v": 1299001, "a": 26691244075, "mc": 1058932420800, "s": 51908452, "m": "KOSPI"}, "price_source_validation": {"repo": "Songdaiki/stock-web", "shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol_year_file": "017960_2025.csv", "manifest_max_date": "2026-02-20", "calculation": "entry close vs inclusive max high/min low over N tradable rows"}, "mfe_mae": {"30d": {"mfe_pct": 31.62, "mae_pct": -3.33, "peak_date": "2025-06-30", "trough_date": "2025-05-16"}, "90d": {"mfe_pct": 75.74, "mae_pct": -3.33, "peak_date": "2025-09-08", "trough_date": "2025-05-16"}, "180d": {"mfe_pct": 100.74, "mae_pct": -3.33, "peak_date": "2026-01-12", "trough_date": "2025-05-16", "post_peak_drawdown_pct": -21.98, "post_peak_trough_date": "2026-02-02"}}, "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence": {"label": "1Q25 earnings surprise / order outlook", "url": "https://marketin.edaily.co.kr/News/ReadE?newsId=02217286642169576", "summary": "1Q25 revenue and operating profit significantly beat expectations; source also ties LNGC insulation orders to expected backlog expansion and raw-material cost stability."}, "case_role": "direct_profit_margin_conversion_positive_control", "profile_error": "missed_actionable_if_actual_profit_and_order_backlog_bridge_are_not_recognized", "residual_decision": "Valid Actionable/Yellow candidate, but Green still waits for cashflow and repeat order evidence.", "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|017960|Stage2-Actionable|2025-05-16"}
{"research_file": "e2r_stock_web_v12_residual_round_R1_loop_206_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "row_id": 5, "selected_round": "R1", "selected_loop": 206, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLIER_BACKLOG_TO_MARGIN_AND_CASHFLOW_GATE_V6", "symbol": "075580", "company": "Sejin Heavy Industries", "trigger_type": "Stage2", "trigger_date": "2024-04-02", "entry_date": "2024-04-02", "entry_price": 6850.0, "entry_ohlcv": {"d": "2024-04-02", "o": 6560.0, "h": 7000.0, "l": 6500.0, "c": 6850.0, "v": 1379260, "a": 9398870090, "mc": 389418773600, "s": 56849456, "m": "KOSPI"}, "price_source_validation": {"repo": "Songdaiki/stock-web", "shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol_year_file": "075580_2024.csv", "manifest_max_date": "2026-02-20", "calculation": "entry close vs inclusive max high/min low over N tradable rows"}, "mfe_mae": {"30d": {"mfe_pct": 10.66, "mae_pct": -5.55, "peak_date": "2024-04-24", "trough_date": "2024-04-16"}, "90d": {"mfe_pct": 59.42, "mae_pct": -7.74, "peak_date": "2024-07-17", "trough_date": "2024-05-23"}, "180d": {"mfe_pct": 59.42, "mae_pct": -7.74, "peak_date": "2024-07-17", "trough_date": "2024-05-23", "post_peak_drawdown_pct": -41.58, "post_peak_trough_date": "2024-11-15"}}, "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence": {"label": "KIRS company report / supplier route", "url": "https://ssl.pstatic.net/imgstock/upload/research/company/1712013384054.pdf", "summary": "KIRS report describes Sejin as a core HD Hyundai / Hyundai Mipo supplier with deck house, LPG/LNG tank, and module production routes, but this is still profile/order-route evidence before conversion."}, "case_role": "supplier_profile_customer_route_stage2_cap", "profile_error": "product_profile_and_customer_route_overcredit_without_delivery_or_margin_bridge", "residual_decision": "Stage2 cap until actual delivery/margin or cash conversion appears.", "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|075580|Stage2|2024-04-02"}
{"research_file": "e2r_stock_web_v12_residual_round_R1_loop_206_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md", "row_id": 6, "selected_round": "R1", "selected_loop": 206, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "C01_SHIPBUILDING_SUPPLIER_BACKLOG_TO_MARGIN_AND_CASHFLOW_GATE_V6", "symbol": "075580", "company": "Sejin Heavy Industries", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-05-23", "entry_date": "2025-05-23", "entry_price": 11300.0, "entry_ohlcv": {"d": "2025-05-23", "o": 11220.0, "h": 11440.0, "l": 10890.0, "c": 11300.0, "v": 2831019, "a": 31622744675, "mc": 642398852800, "s": 56849456, "m": "KOSPI"}, "price_source_validation": {"repo": "Songdaiki/stock-web", "shard_root": "atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "symbol_year_file": "075580_2025.csv", "manifest_max_date": "2026-02-20", "calculation": "entry close vs inclusive max high/min low over N tradable rows"}, "mfe_mae": {"30d": {"mfe_pct": 14.6, "mae_pct": -9.03, "peak_date": "2025-06-16", "trough_date": "2025-07-07"}, "90d": {"mfe_pct": 142.48, "mae_pct": -9.03, "peak_date": "2025-09-10", "trough_date": "2025-07-07"}, "180d": {"mfe_pct": 142.48, "mae_pct": -9.03, "peak_date": "2025-09-10", "trough_date": "2025-07-07", "post_peak_drawdown_pct": -38.87, "post_peak_trough_date": "2025-12-19"}}, "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "evidence": {"label": "1Q25 tank delivery / margin bridge article", "url": "https://www.dailyinvest.kr/news/articleView.html?idxno=66768", "summary": "2025 Q1 operating profit beat is linked to high-margin LCO2 tank delivery, tank shipment growth, and explicit margin outlook, providing a second bridge beyond backlog."}, "case_role": "tank_delivery_profitability_positive_control_with_drawdown_cap", "profile_error": "green_overcredit_if_high_mfe_positive_control_ignores_late_peak_drawdown_and_cashflow_gap", "residual_decision": "Valid Actionable; high post-peak drawdown and lack of repeat cash bridge keep Green blocked.", "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|075580|Stage2-Actionable|2025-05-23"}
```

## 11. Batch Ingest Self-Audit

```text
standard_filename = pass
selected_round_large_sector_consistency = pass
canonical_archetype_id_present = pass
fine_archetype_id_present = pass
actual_stock_web_ohlc_rows_present = pass
entry_price_present = pass
30_90_180D_mfe_mae_present_for_all_usable_rows = pass
corporate_action_contamination_checked = pass
insufficient_forward_window_checked = pass
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
calibration_usable_trigger_count = 6
new_independent_ratio = 1.00
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 12. Next Research State

```text
next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH

next_research_hint:
Prefer direct working-capital/cashflow or hard 4C boundary rows over adding another generic backlog/order headline.
```

## 13. Deferred Coding Agent Handoff Prompt

```text
Read this MD as one C01 v12 residual calibration input.
Do not change production scoring directly.
Parse the JSONL block, validate duplicate keys, and include only calibration_usable rows.
Suggested shadow rule candidate:
C01_SUPPLIER_BACKLOG_MARGIN_CASHFLOW_GATE_V6

Implementation hypothesis for later promotion planner:
- Add/strengthen a C01 supplier-side second-bridge gate before Actionable/Yellow/Green.
- Treat backlog/customer-route evidence as Stage2 unless realized delivery, margin, cashflow, or working-capital conversion appears.
- Use high post-peak drawdown as a Green blocker rather than a Stage2 deletion rule.
```
