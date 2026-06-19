# E2R Stock-Web v12 Residual Research — R3 / C13 Battery JV Utilization AMPC IRA

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection Metadata

```text
selected_round = R3
selected_loop = 203
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 quality reinforcement
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3
standard_v12_filename = e2r_stock_web_v12_residual_round_R3_loop_203_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
```

### Why this canonical was selected

The current No-Repeat ledger shows all C01~C32 archetypes above the old 30/50/80 row thresholds, so the next work is not raw coverage filling. It is quality repair. C13 remains in Priority 1 because AMPC/IRA/JV language can still be mistaken for durable earnings unless the row separates **eligible production, utilization, customer pull/call-off, shipment conversion, ex-subsidy margin, and offset quality**.

Recent in-session C13 work already covered several broad JV/AMPC rows. This loop deliberately uses different entry dates / trigger labels and emphasizes the specific residual problem: **AMPC or battery-material recovery headlines should reopen Stage2 only when a second bridge is present; high MAE should block Yellow/Green, not erase valid Stage2.**

Hard duplicate key rule used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row reuses the same C13 + symbol + trigger_type + entry_date combination from the immediately preceding C13 session notes.

## 2. Stock-Web Price Atlas Validation

```text
price_atlas_repo = Songdaiki/stock-web
manifest = atlas/manifest.json
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
tradable_schema = d,o,h,l,c,v,a,mc,s,m
```

Manifest facts used in this file:

```text
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
```

MFE/MAE method:

```text
entry_price = actual stock-web tradable close on entry_date
MFE_N = max(high from entry row through N-th forward tradable row) / entry_close - 1
MAE_N = min(low from entry row through N-th forward tradable row) / entry_close - 1
```

All selected usable rows have complete 30D/90D/180D forward windows before manifest max_date and no corporate-action candidate overlapping the selected 180D window.

## 3. Batch Coverage / Novelty Summary

```text
new_independent_case_count = 7
new_independent_trigger_count = 7
unique_symbol_count = 6
calibration_usable_case_count = 7
calibration_usable_trigger_count = 7

stage2_count = 1
stage2_actionable_count = 3
stage4b_count = 2
stage4c_count = 1

positive_or_reopen_case_count = 3
offset_or_guardrail_case_count = 3
hard_4c_offset_stress_count = 1
current_profile_error_count = 5

source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0

production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 4. Actual Entry OHLCV Rows

| symbol | entry_date | o | h | l | c | volume | amount | market_cap | market |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 373220 | 2023-04-26 | 551,000 | 572,000 | 550,000 | 567,000 | 296,105 | 166,642,321,000 | 132,678,000,000,000 | KOSPI |
| 373220 | 2025-01-31 | 353,500 | 356,500 | 346,500 | 352,000 | 147,908 | 51,977,272,500 | 82,368,000,000,000 | KOSPI |
| 006400 | 2025-01-24 | 233,000 | 234,500 | 225,000 | 226,500 | 475,862 | 108,036,156,000 | 15,575,166,045,000 | KOSPI |
| 020150 | 2025-05-09 | 22,800 | 22,800 | 22,000 | 22,000 | 71,322 | 1,581,745,725 | 1,152,040,186,000 | KOSPI |
| 003670 | 2025-04-24 | 134,500 | 135,500 | 130,100 | 130,200 | 283,955 | 37,523,019,200 | 10,085,711,244,000 | KOSPI |
| 096770 | 2025-04-30 | 95,800 | 96,800 | 93,400 | 94,400 | 306,828 | 28,950,933,300 | 14,257,682,854,400 | KOSPI |
| 066970 | 2025-04-30 | 67,900 | 67,900 | 64,800 | 64,800 | 221,793 | 14,552,374,900 | 2,353,288,075,200 | KOSPI |


## 5. Forward Price Path Results

| symbol | name | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| 373220 | LG Energy Solution | Stage2-Actionable | 2023-04-26 | 567,000 | 8.29/-6.53 | 9.35/-9.52 | 9.35/-34.48 | 2023-07-26 | 2024-01-22 |
| 373220 | LG Energy Solution | Stage4B | 2025-01-31 | 352,000 | 9.80/-7.67 | 9.80/-24.43 | 44.89/-24.43 | 2025-10-28 | 2025-05-23 |
| 006400 | Samsung SDI | Stage4C | 2025-01-24 | 226,500 | 9.71/-16.42 | 9.71/-30.38 | 34.44/-30.38 | 2025-10-27 | 2025-05-22 |
| 020150 | LOTTE Energy Materials | Stage4B | 2025-05-09 | 22,000 | 7.05/-11.55 | 28.41/-11.55 | 102.95/-11.55 | 2025-11-25 | 2025-05-22 |
| 003670 | POSCO Future M | Stage2-Actionable | 2025-04-24 | 130,200 | 4.07/-24.35 | 26.65/-24.35 | 99.69/-24.35 | 2025-10-27 | 2025-05-27 |
| 096770 | SK Innovation / SK On | Stage4B | 2025-04-30 | 94,400 | 8.26/-14.41 | 35.59/-14.41 | 46.50/-14.41 | 2025-10-29 | 2025-05-23 |
| 066970 | L&F | Stage2-Actionable | 2025-04-30 | 64,800 | 4.78/-27.47 | 40.90/-27.47 | 129.94/-27.47 | 2025-10-29 | 2025-05-26 |


## 6. Case Notes

### C13_203_01 — 373220 LG Energy Solution / Stage2-Actionable
- evidence_date: `2023-04-26`
- entry_date: `2023-04-26` / entry_close: `567,000`
- evidence_family: `IRA_AMPC_GM_JV_shipment_yield_bridge`
- direct evidence: Q1 2023 revenue/profit growth; IRA 45X AMPC recognized in operating profit; GM Ultium JV shipment/ASP/yield bridge.
- source_url: https://news.lgensol.com/company-news/press-releases/1705/
- 30D MFE/MAE: `8.29% / -6.53%`
- 90D MFE/MAE: `9.35% / -9.52%`
- 180D MFE/MAE: `9.35% / -34.48%`
- profile note: corporate_action_candidate_dates=[]
- residual read: positive_high_mae_control

### C13_203_02 — 373220 LG Energy Solution / Stage4B
- evidence_date: `2025-01-31`
- entry_date: `2025-01-31` / entry_close: `352,000`
- evidence_family: `ex_AMPC_loss_lower_utilization_capex_cut_with_ESS_offset`
- direct evidence: FY2024 OP down sharply and Q4 operating loss included IRA credit; utilization/fixed-cost pressure and capex reduction, but ESS/new-chemistry/idle-line order processing provide offset quality.
- source_url: https://www.lgcorp.com/media/release/28617
- 30D MFE/MAE: `9.80% / -7.67%`
- 90D MFE/MAE: `9.80% / -24.43%`
- 180D MFE/MAE: `44.89% / -24.43%`
- profile note: corporate_action_candidate_dates=[]
- residual read: offset_quality_watch

### C13_203_03 — 006400 Samsung SDI / Stage4C
- evidence_date: `2025-01-24`
- entry_date: `2025-01-24` / entry_close: `226,500`
- evidence_family: `battery_operating_loss_customer_inventory_adjustment_ESS_JV_offset`
- direct evidence: Q4 battery operating loss and EV/power-tool inventory adjustment; ESS record revenue and U.S. JV progress create offset that should prevent automatic hard-4C overkill.
- source_url: https://www.businesskorea.co.kr/news/articleView.html?idxno=234435
- 30D MFE/MAE: `9.71% / -16.42%`
- 90D MFE/MAE: `9.71% / -30.38%`
- 180D MFE/MAE: `34.44% / -30.38%`
- profile note: corporate_action_candidate_dates=[1996-01-03, 1998-11-03, 2014-07-15]; no overlap with 2025 entry windows
- residual read: hard_4c_with_offset_stress

### C13_203_04 — 020150 LOTTE Energy Materials / Stage4B
- evidence_date: `2025-05-09`
- entry_date: `2025-05-09` / entry_close: `22,000`
- evidence_family: `copper_foil_customer_inventory_adjustment_utilization_recovery_guidance`
- direct evidence: Q1 2025 operating loss from reduced shipments and customer inventory adjustment, but stated utilization recovery and new North America OEM/JV supply bridge for H2 turnaround.
- source_url: https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=138
- 30D MFE/MAE: `7.05% / -11.55%`
- 90D MFE/MAE: `28.41% / -11.55%`
- 180D MFE/MAE: `102.95% / -11.55%`
- profile note: corporate_action_candidate_dates=[]
- residual read: reversible_utilization_watch

### C13_203_05 — 003670 POSCO Future M / Stage2-Actionable
- evidence_date: `2025-04-24`
- entry_date: `2025-04-24` / entry_close: `130,200`
- evidence_family: `q1_profit_reopen_cathode_materials_turnaround`
- direct evidence: Q1 2025 consolidated revenue 845.4bn won and operating profit 17.2bn won after weak FY2024; direct profit reopen but still needs shipment/margin persistence before Yellow/Green.
- source_url: https://www.poscofuturem.com/en/pr/list.do?m=04&topic=18&y=2025
- 30D MFE/MAE: `4.07% / -24.35%`
- 90D MFE/MAE: `26.65% / -24.35%`
- 180D MFE/MAE: `99.69% / -24.35%`
- profile note: corporate_action_candidate_dates=[2015-05-04, 2021-02-03]; no overlap with 2025 entry windows
- residual read: direct_profit_reopen_high_mae_cap

### C13_203_06 — 096770 SK Innovation / SK On / Stage4B
- evidence_date: `2025-04-30`
- entry_date: `2025-04-30` / entry_close: `94,400`
- evidence_family: `SK_On_narrowed_loss_US_sales_output_growth_offset`
- direct evidence: SK Innovation swung to operating loss; SK On still lost money but loss narrowed and company guided North America battery sales/output improvement.
- source_url: https://www.reuters.com/business/energy/sk-innovation-expects-refining-margins-gradually-improve-q2-2025-04-30/
- 30D MFE/MAE: `8.26% / -14.41%`
- 90D MFE/MAE: `35.59% / -14.41%`
- 180D MFE/MAE: `46.50% / -14.41%`
- profile note: corporate_action_candidate_dates=[2024-11-20]; before selected 2025 entry window
- residual read: battery_loss_with_north_america_sales_offset

### C13_203_07 — 066970 L&F / Stage2-Actionable
- evidence_date: `2025-04-30`
- entry_date: `2025-04-30` / entry_close: `64,800`
- evidence_family: `NCMA95_demand_shipment_target_upgrade_customer_pull`
- direct evidence: Company indicated rising NCMA95 demand and raised 2025 shipment growth target; direct customer-pull/shipment bridge reopens Stage2-Actionable but high MAE blocks Yellow/Green.
- source_url: https://www.landf.co.kr/company/hong_7.html?action=read&board_db=news&column=&n=&num=210&page=1
- 30D MFE/MAE: `4.78% / -27.47%`
- 90D MFE/MAE: `40.90% / -27.47%`
- 180D MFE/MAE: `129.94% / -27.47%`
- profile note: corporate_action_candidate_dates=[2016-02-19, 2021-08-11]; no overlap with 2025 entry windows
- residual read: customer_pull_shipment_reopen_high_mae_cap


## 7. Raw Component Score Stress Test

Weights shown as raw component score, not production patch. Component order: `EPS/Vis/Bott/Mis/Val/Cap/Info`.

| case_id | symbol | trigger | EPS | Vis | Bott | Mis | Val | Cap | Info | total | stress label |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C13_203_01 | 373220 | Stage2-Actionable | 15 | 18 | 13 | 10 | 9 | 8 | 10 | 83 | Green_blocker_high_MAE |
| C13_203_02 | 373220 | Stage4B | 5 | 10 | 7 | 8 | 7 | 8 | 17 | 62 | Stage4B_watch_or_reopen |
| C13_203_03 | 006400 | Stage4C | 2 | 7 | 5 | 8 | 5 | 7 | 21 | 55 | Overhard_4C_offset_check |
| C13_203_04 | 020150 | Stage4B | 4 | 11 | 8 | 9 | 7 | 8 | 18 | 65 | Stage4B_watch_or_reopen |
| C13_203_05 | 003670 | Stage2-Actionable | 12 | 16 | 10 | 10 | 8 | 7 | 16 | 79 | Green_blocker_high_MAE |
| C13_203_06 | 096770 | Stage4B | 3 | 11 | 6 | 8 | 6 | 9 | 18 | 61 | Stage4B_watch_or_reopen |
| C13_203_07 | 066970 | Stage2-Actionable | 10 | 17 | 11 | 11 | 9 | 6 | 15 | 79 | Green_blocker_high_MAE |


### Score/stage alignment read

1. **LGES 2023-04-26** is a valid C13 Stage2-Actionable row because the evidence is not merely IRA language. It has AMPC recognition, GM JV operational shipment, ASP, yield and cost bridge. However, the 180D path produced only `9.35%` MFE and `-34.48%` MAE, so the row argues for a high-MAE Green blocker, not for removing Stage2.
2. **LGES 2025-01-31** and **LOTTE Energy Materials 2025-05-09** show why an ugly quarter with explicit utilization or customer-inventory pressure should often be Stage4B/watch rather than hard 4C when management gives a concrete utilization, ESS, OEM/JV, or idle-line offset route.
3. **Samsung SDI 2025-01-24** is the useful stress row. The battery segment loss and customer inventory adjustment are hard-break language, but ESS and U.S. JV progress are non-trivial offsets. Therefore C13 should require weak offset quality before hard 4C.
4. **POSCO Future M, EcoPro BM-class material recovery, and L&F-style NCMA95 demand rows** should not get automatic Yellow/Green from “profit returned” or “shipment target raised.” They need evidence that the improvement is not inventory allowance reversal, raw-material lag, or one customer program volatility.
5. **SK Innovation/SK On 2025-04-30** separates parent-level operating loss from battery-unit sales/output offset. It is a Stage4B/watch row, not a standalone C13 positive.

## 8. Residual Contribution Summary

```text
residual_axis = C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3
existing_axis_strengthened = stage2_required_bridge
existing_axis_refined = local_4b_watch_guard, hard_4c_confirmation, high_MAE_green_blocker
new_axis_proposed = false
production_scoring_changed = false
shadow_weight_only = true
```

### Proposed shadow rule candidate

```text
rule_candidate_id = C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3
scope = canonical_archetype_id:C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rule_type = shadow_guardrail_candidate
```

Candidate rule language:

```text
For C13, AMPC / IRA / JV / regional supply-chain language alone does not create Stage2-Actionable or Yellow.

Stage2-Actionable requires at least one direct second bridge:
- eligible production volume;
- utilization rebound;
- customer pull / call-off / shipment schedule;
- ex-subsidy operating margin;
- cathode / copper-foil / cell revenue conversion;
- order/backlog-to-revenue route;
- explicit customer or JV supply bridge.

If AMPC credit exceeds or materially props up reported operating profit, apply Green blocker until ex-credit economics or utilization recovery is visible.

If battery demand slowdown, inventory adjustment, customer delay, or operating loss appears but there is explicit ESS / non-EV / North America / new-model / JV / customer-pull offset, route to Stage4B/watch before hard 4C.

Hard 4C requires utilization or margin thesis break plus weak or absent offset quality. High MAE on a valid direct-bridge row blocks Yellow/Green; it does not erase Stage2-Actionable.
```

### Shadow weight note

Current C13 runtime seed in the ledger is already conservative relative to the default profile: `20/18/14/12/10/10/16`, with lower Bottleneck/Visibility/Valuation and higher Information/Capital discipline. This loop does not propose a new numeric patch. It strengthens the interpretation of Information Confidence and Capital Allocation as negative-confirmation / offset-quality gates.

```json
{
  "row_type": "shadow_weight",
  "selected_round": "R3",
  "selected_loop": 203,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "rule_candidate_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3",
  "current_seed_weight": {"eps_fcf_explosion":20,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":10,"information_confidence":16},
  "proposed_delta": {"eps_fcf_explosion":0,"earnings_visibility":0,"bottleneck_pricing":0,"market_mispricing":0,"valuation_rerating":0,"capital_allocation":0,"information_confidence":0},
  "interpretation_change_only": true,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 9. Machine-Readable JSONL Trigger Rows

```jsonl
{"row_type": "trigger", "v12_schema_version": "v12_stock_web_sector_archetype_residual", "case_id": "C13_203_01", "selected_round": "R3", "selected_loop": 203, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3", "symbol": "373220", "company_name": "LG Energy Solution", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-26", "entry_date": "2023-04-26", "entry_price": 567000.0, "actual_entry_ohlcv": {"o": 551000.0, "h": 572000.0, "l": 550000.0, "c": 567000.0, "v": 296105, "a": 166642321000.0, "mc": 132678000000000.0, "m": "KOSPI"}, "mfe_30d_pct": 8.29, "mae_30d_pct": -6.53, "mfe_90d_pct": 9.35, "mae_90d_pct": -9.52, "mfe_180d_pct": 9.35, "mae_180d_pct": -34.48, "peak_180d_date": "2023-07-26", "trough_180d_date": "2024-01-22", "calibration_usable": true, "price_source_validation": {"price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "corporate_action_contaminated_180d_window": false, "insufficient_forward_window_180d": false}, "evidence_family": "IRA_AMPC_GM_JV_shipment_yield_bridge", "evidence_summary": "Q1 2023 revenue/profit growth; IRA 45X AMPC recognized in operating profit; GM Ultium JV shipment/ASP/yield bridge.", "evidence_url": "https://news.lgensol.com/company-news/press-releases/1705/", "raw_component_score_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 18, "bottleneck_pricing": 13, "market_mispricing": 10, "valuation_rerating": 9, "capital_allocation": 8, "information_confidence": 10}, "score_total": 83, "residual_label": "positive_high_mae_control", "production_scoring_changed": false, "shadow_weight_only": true, "hard_duplicate_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Actionable|2023-04-26"}
{"row_type": "trigger", "v12_schema_version": "v12_stock_web_sector_archetype_residual", "case_id": "C13_203_02", "selected_round": "R3", "selected_loop": 203, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3", "symbol": "373220", "company_name": "LG Energy Solution", "trigger_type": "Stage4B", "trigger_date": "2025-01-31", "entry_date": "2025-01-31", "entry_price": 352000.0, "actual_entry_ohlcv": {"o": 353500.0, "h": 356500.0, "l": 346500.0, "c": 352000.0, "v": 147908, "a": 51977272500.0, "mc": 82368000000000.0, "m": "KOSPI"}, "mfe_30d_pct": 9.8, "mae_30d_pct": -7.67, "mfe_90d_pct": 9.8, "mae_90d_pct": -24.43, "mfe_180d_pct": 44.89, "mae_180d_pct": -24.43, "peak_180d_date": "2025-10-28", "trough_180d_date": "2025-05-23", "calibration_usable": true, "price_source_validation": {"price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "corporate_action_contaminated_180d_window": false, "insufficient_forward_window_180d": false}, "evidence_family": "ex_AMPC_loss_lower_utilization_capex_cut_with_ESS_offset", "evidence_summary": "FY2024 OP down sharply and Q4 operating loss included IRA credit; utilization/fixed-cost pressure and capex reduction, but ESS/new-chemistry/idle-line order processing provide offset quality.", "evidence_url": "https://www.lgcorp.com/media/release/28617", "raw_component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 10, "bottleneck_pricing": 7, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 8, "information_confidence": 17}, "score_total": 62, "residual_label": "offset_quality_watch", "production_scoring_changed": false, "shadow_weight_only": true, "hard_duplicate_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage4B|2025-01-31"}
{"row_type": "trigger", "v12_schema_version": "v12_stock_web_sector_archetype_residual", "case_id": "C13_203_03", "selected_round": "R3", "selected_loop": 203, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3", "symbol": "006400", "company_name": "Samsung SDI", "trigger_type": "Stage4C", "trigger_date": "2025-01-24", "entry_date": "2025-01-24", "entry_price": 226500.0, "actual_entry_ohlcv": {"o": 233000.0, "h": 234500.0, "l": 225000.0, "c": 226500.0, "v": 475862, "a": 108036156000.0, "mc": 15575166045000.0, "m": "KOSPI"}, "mfe_30d_pct": 9.71, "mae_30d_pct": -16.42, "mfe_90d_pct": 9.71, "mae_90d_pct": -30.38, "mfe_180d_pct": 34.44, "mae_180d_pct": -30.38, "peak_180d_date": "2025-10-27", "trough_180d_date": "2025-05-22", "calibration_usable": true, "price_source_validation": {"price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "corporate_action_contaminated_180d_window": false, "insufficient_forward_window_180d": false}, "evidence_family": "battery_operating_loss_customer_inventory_adjustment_ESS_JV_offset", "evidence_summary": "Q4 battery operating loss and EV/power-tool inventory adjustment; ESS record revenue and U.S. JV progress create offset that should prevent automatic hard-4C overkill.", "evidence_url": "https://www.businesskorea.co.kr/news/articleView.html?idxno=234435", "raw_component_score_breakdown": {"eps_fcf_explosion": 2, "earnings_visibility": 7, "bottleneck_pricing": 5, "market_mispricing": 8, "valuation_rerating": 5, "capital_allocation": 7, "information_confidence": 21}, "score_total": 55, "residual_label": "hard_4c_with_offset_stress", "production_scoring_changed": false, "shadow_weight_only": true, "hard_duplicate_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage4C|2025-01-24"}
{"row_type": "trigger", "v12_schema_version": "v12_stock_web_sector_archetype_residual", "case_id": "C13_203_04", "selected_round": "R3", "selected_loop": 203, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3", "symbol": "020150", "company_name": "LOTTE Energy Materials", "trigger_type": "Stage4B", "trigger_date": "2025-05-09", "entry_date": "2025-05-09", "entry_price": 22000.0, "actual_entry_ohlcv": {"o": 22800.0, "h": 22800.0, "l": 22000.0, "c": 22000.0, "v": 71322, "a": 1581745725.0, "mc": 1152040186000.0, "m": "KOSPI"}, "mfe_30d_pct": 7.05, "mae_30d_pct": -11.55, "mfe_90d_pct": 28.41, "mae_90d_pct": -11.55, "mfe_180d_pct": 102.95, "mae_180d_pct": -11.55, "peak_180d_date": "2025-11-25", "trough_180d_date": "2025-05-22", "calibration_usable": true, "price_source_validation": {"price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "corporate_action_contaminated_180d_window": false, "insufficient_forward_window_180d": false}, "evidence_family": "copper_foil_customer_inventory_adjustment_utilization_recovery_guidance", "evidence_summary": "Q1 2025 operating loss from reduced shipments and customer inventory adjustment, but stated utilization recovery and new North America OEM/JV supply bridge for H2 turnaround.", "evidence_url": "https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=138", "raw_component_score_breakdown": {"eps_fcf_explosion": 4, "earnings_visibility": 11, "bottleneck_pricing": 8, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 8, "information_confidence": 18}, "score_total": 65, "residual_label": "reversible_utilization_watch", "production_scoring_changed": false, "shadow_weight_only": true, "hard_duplicate_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|020150|Stage4B|2025-05-09"}
{"row_type": "trigger", "v12_schema_version": "v12_stock_web_sector_archetype_residual", "case_id": "C13_203_05", "selected_round": "R3", "selected_loop": 203, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3", "symbol": "003670", "company_name": "POSCO Future M", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-24", "entry_date": "2025-04-24", "entry_price": 130200.0, "actual_entry_ohlcv": {"o": 134500.0, "h": 135500.0, "l": 130100.0, "c": 130200.0, "v": 283955, "a": 37523019200.0, "mc": 10085711244000.0, "m": "KOSPI"}, "mfe_30d_pct": 4.07, "mae_30d_pct": -24.35, "mfe_90d_pct": 26.65, "mae_90d_pct": -24.35, "mfe_180d_pct": 99.69, "mae_180d_pct": -24.35, "peak_180d_date": "2025-10-27", "trough_180d_date": "2025-05-27", "calibration_usable": true, "price_source_validation": {"price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "corporate_action_contaminated_180d_window": false, "insufficient_forward_window_180d": false}, "evidence_family": "q1_profit_reopen_cathode_materials_turnaround", "evidence_summary": "Q1 2025 consolidated revenue 845.4bn won and operating profit 17.2bn won after weak FY2024; direct profit reopen but still needs shipment/margin persistence before Yellow/Green.", "evidence_url": "https://www.poscofuturem.com/en/pr/list.do?m=04&topic=18&y=2025", "raw_component_score_breakdown": {"eps_fcf_explosion": 12, "earnings_visibility": 16, "bottleneck_pricing": 10, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 7, "information_confidence": 16}, "score_total": 79, "residual_label": "direct_profit_reopen_high_mae_cap", "production_scoring_changed": false, "shadow_weight_only": true, "hard_duplicate_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|003670|Stage2-Actionable|2025-04-24"}
{"row_type": "trigger", "v12_schema_version": "v12_stock_web_sector_archetype_residual", "case_id": "C13_203_06", "selected_round": "R3", "selected_loop": 203, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3", "symbol": "096770", "company_name": "SK Innovation / SK On", "trigger_type": "Stage4B", "trigger_date": "2025-04-30", "entry_date": "2025-04-30", "entry_price": 94400.0, "actual_entry_ohlcv": {"o": 95800.0, "h": 96800.0, "l": 93400.0, "c": 94400.0, "v": 306828, "a": 28950933300.0, "mc": 14257682854400.0, "m": "KOSPI"}, "mfe_30d_pct": 8.26, "mae_30d_pct": -14.41, "mfe_90d_pct": 35.59, "mae_90d_pct": -14.41, "mfe_180d_pct": 46.5, "mae_180d_pct": -14.41, "peak_180d_date": "2025-10-29", "trough_180d_date": "2025-05-23", "calibration_usable": true, "price_source_validation": {"price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "corporate_action_contaminated_180d_window": false, "insufficient_forward_window_180d": false}, "evidence_family": "SK_On_narrowed_loss_US_sales_output_growth_offset", "evidence_summary": "SK Innovation swung to operating loss; SK On still lost money but loss narrowed and company guided North America battery sales/output improvement.", "evidence_url": "https://www.reuters.com/business/energy/sk-innovation-expects-refining-margins-gradually-improve-q2-2025-04-30/", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 11, "bottleneck_pricing": 6, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 9, "information_confidence": 18}, "score_total": 61, "residual_label": "battery_loss_with_north_america_sales_offset", "production_scoring_changed": false, "shadow_weight_only": true, "hard_duplicate_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|096770|Stage4B|2025-04-30"}
{"row_type": "trigger", "v12_schema_version": "v12_stock_web_sector_archetype_residual", "case_id": "C13_203_07", "selected_round": "R3", "selected_loop": 203, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3", "symbol": "066970", "company_name": "L&F", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-30", "entry_date": "2025-04-30", "entry_price": 64800.0, "actual_entry_ohlcv": {"o": 67900.0, "h": 67900.0, "l": 64800.0, "c": 64800.0, "v": 221793, "a": 14552374900.0, "mc": 2353288075200.0, "m": "KOSPI"}, "mfe_30d_pct": 4.78, "mae_30d_pct": -27.47, "mfe_90d_pct": 40.9, "mae_90d_pct": -27.47, "mfe_180d_pct": 129.94, "mae_180d_pct": -27.47, "peak_180d_date": "2025-10-29", "trough_180d_date": "2025-05-26", "calibration_usable": true, "price_source_validation": {"price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "manifest_max_date": "2026-02-20", "corporate_action_contaminated_180d_window": false, "insufficient_forward_window_180d": false}, "evidence_family": "NCMA95_demand_shipment_target_upgrade_customer_pull", "evidence_summary": "Company indicated rising NCMA95 demand and raised 2025 shipment growth target; direct customer-pull/shipment bridge reopens Stage2-Actionable but high MAE blocks Yellow/Green.", "evidence_url": "https://www.landf.co.kr/company/hong_7.html?action=read&board_db=news&column=&n=&num=210&page=1", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 17, "bottleneck_pricing": 11, "market_mispricing": 11, "valuation_rerating": 9, "capital_allocation": 6, "information_confidence": 15}, "score_total": 79, "residual_label": "customer_pull_shipment_reopen_high_mae_cap", "production_scoring_changed": false, "shadow_weight_only": true, "hard_duplicate_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|066970|Stage2-Actionable|2025-04-30"}
```

## 10. Aggregate JSONL

```jsonl
{"row_type":"aggregate","selected_round":"R3","selected_loop":203,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3","new_independent_case_count":7,"new_independent_trigger_count":7,"unique_symbol_count":6,"calibration_usable_trigger_count":7,"stage2_count":1,"stage2_actionable_count":3,"stage4b_count":2,"stage4c_count":1,"positive_or_reopen_case_count":3,"offset_or_guardrail_case_count":3,"hard_4c_offset_stress_count":1,"source_proxy_only_count":0,"evidence_url_pending_count":0,"missing_required_mfe_mae_count":0,"corporate_action_contaminated_180D_count":0,"insufficient_forward_window_180D_count":0,"production_scoring_changed":false,"shadow_weight_only":true,"ready_for_batch_ingest":true}
{"row_type":"residual_contribution","selected_round":"R3","selected_loop":203,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","residual_axis":"C13_EX_SUBSIDY_MARGIN_UTILIZATION_AND_CUSTOMER_PULL_GATE_V3","core_read":"C13 should not treat AMPC/IRA/JV terms as durable earnings without eligible volume, utilization, customer pull, shipment, ex-subsidy margin, or order-to-revenue bridge. High MAE blocks Yellow/Green, not valid Stage2. Hard 4C needs weak offset quality.","production_scoring_changed":false,"shadow_weight_only":true}
```

## 11. Batch Ingest Self-Audit

```text
standard_filename_regex_pass = true
filename_round_matches_metadata = true
filename_loop_matches_metadata = true
round_sector_pair_valid = true
canonical_archetype_known = true
large_sector_known = true
stock_agent_code_accessed = false
stock_agent_code_patched = false
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_web_actual_1D_OHLC_used = true
all_usable_trigger_rows_have_entry_date = true
all_usable_trigger_rows_have_entry_price = true
all_usable_trigger_rows_have_actual_entry_ohlcv = true
all_usable_trigger_rows_have_30_90_180_mfe_mae = true
source_proxy_only_count = 0
evidence_url_pending_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
production_scoring_changed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during the research session.

When batch-applying v12 research outputs, ingest this MD as a standard v12 result file.
Parse the JSONL trigger rows and aggregate rows.
Validate hard duplicate keys at canonical_archetype_id + symbol + trigger_type + entry_date.
Keep all changes shadow-only unless promotion planner confirms data quality and logic safety.
For C13_BATTERY_JV_UTILIZATION_AMPC_IRA, evaluate whether the existing C13 runtime gate should explicitly require one second bridge before Stage2-Actionable/Yellow:
eligible production volume, utilization rebound, customer pull/call-off, shipment schedule, ex-subsidy margin, order/backlog-to-revenue, or direct JV/customer supply bridge.
Also evaluate hard-4C offset quality: hard 4C requires utilization/margin thesis break plus weak offset quality.
Do not loosen Stage3-Green thresholds.
Do not introduce live trading logic.
```

## 13. Next Research State

```text
completed_round = R3
completed_loop = 203
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 quality reinforcement
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes = [
  "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR",
  "C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY",
  "C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR",
  "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR",
  "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH"
]
```
