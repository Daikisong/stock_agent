# E2R V12 No-Repeat Standalone Residual Research
## C02 Power Grid / Datacenter CAPEX — transformer winners vs cable-theme high-MAE counterexample

```text
selected_round = R1
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_TRANSFORMER_DATACENTER_CAPEX_WITH_CABLE_THEME_COUNTEREXAMPLE
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduler_override_applied = true
production_scoring_changed = false
shadow_weight_only = true
```

## 1. No-Repeat / selection basis

`V12_Research_No_Repeat_Index.md`의 coverage table에는 `C02_POWER_GRID_DATACENTER_CAPEX`가 대표 coverage row로 잡혀 있지 않다. 기존 R1 coverage에서 C03/C04는 보이지만 C02는 비어 있으므로, 이번 실행은 round scheduler loop 번호를 계승하지 않고 R1 universe 안의 under-covered C02를 선택했다.

중복 회피 판정:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
selected_keys:
- C02_POWER_GRID_DATACENTER_CAPEX + 010120 + Stage2-Actionable + 2024-03-05
- C02_POWER_GRID_DATACENTER_CAPEX + 267260 + Stage2-Actionable + 2023-01-27
- C02_POWER_GRID_DATACENTER_CAPEX + 001440 + Stage3-Yellow + 2024-05-13
- C02_POWER_GRID_DATACENTER_CAPEX + 010120 + Stage4B + 2024-07-24

hard_duplicate_avoided = true
new_independent_case_count = 4
reused_case_count = 0
```

## 2. Stock-Web manifest and price-source validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

Manifest anchor:

```text
atlas/manifest.json
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
```

Profile caveats checked:

```text
010120 LS ELECTRIC: corporate_action_candidate_dates = 1995-09-28, 1999-04-08, 1999-07-26, 2003-04-16. No overlap with 2024 windows.
267260 HD현대일렉트릭: corporate_action_candidate_dates = 2017-11-17, 2017-11-28, 2017-12-11, 2018-11-23, 2018-12-18, 2019-12-30. No overlap with 2023 windows.
001440 대한전선: corporate_action_candidate_dates include 2024-04-02. Entry is 2024-05-13, so the 2024-04-02 candidate does not overlap entry_date~D+180.
```

## 3. Thesis

C02 should not be a generic "electric equipment/theme" bucket. The positive route is narrower:

```text
grid/datacenter CAPEX
-> transformer/switchgear/order backlog
-> margin and EPS/FCF revision
-> old-frame mispricing
-> price path validation
```

The counterexample route is:

```text
cable/grid theme price extension
-> weak or unverified EPS/FCF bridge
-> high-MAE path
-> Green must be blocked or capped at watch/yellow
```

This is different from C03 defense backlog and C04 nuclear policy delay. C02 requires a grid/datacenter capacity bottleneck and transformer/switchgear revenue conversion bridge.

## 4. Case summary

| case_id | symbol | company | role | trigger | entry | entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | result |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|
| C02_NO_REPEAT_010120_LS_ELECTRIC_20240305_GRID_DC_STAGE2 | 010120 | LS ELECTRIC | positive | Stage2-Actionable | 2024-03-05 | 77,800 | 102.6992 / -8.9974 | 213.6247 / -8.9974 | 252.8278 / -8.9974 | strong C02 structural success |
| C02_NO_REPEAT_267260_HD_HYUNDAI_ELECTRIC_20230127_TRANSFORMER_STAGE2 | 267260 | HD현대일렉트릭 | positive | Stage2-Actionable | 2023-01-27 | 38,800 | 18.299 / -5.1546 | 41.7526 / -5.1546 | 116.4948 / -5.1546 | early transformer rerating success |
| C02_NO_REPEAT_001440_TAIHAN_CABLE_20240513_CABLE_THEME_HIGH_MAE | 001440 | 대한전선 | counterexample | Stage3-Yellow stress | 2024-05-13 | 18,110 | 15.6819 / -22.4186 | 15.6819 / -43.291 | 15.6819 / -44.7819 | high-MAE cable-theme false Green guard |
| C02_NO_REPEAT_010120_LS_ELECTRIC_20240724_LOCAL_4B_PEAK | 010120 | LS ELECTRIC | 4B | Stage4B | 2024-07-24 | 260,000 | 5.5769 / -44.2308 | 5.5769 / -51.4615 | 5.5769 / -51.4615 | good full-window 4B peak capture |

## 5. Stock-Web OHLC anchors

### 5.1 HD현대일렉트릭 / 267260

```text
profile: atlas/symbol_profiles/267/267260.json
tradable shard: atlas/ohlcv_tradable_by_symbol_year/267/267260/2023.csv

entry row:
2023-01-27,36800.0,39300.0,36800.0,38800.0,...

forward anchors:
2023-03-03 high = 45,900
2023-06-08 high = 55,000
2023-07-26 high = 84,000
2023-09-01 low = 61,400
```

### 5.2 LS ELECTRIC / 010120

```text
profile: atlas/symbol_profiles/010/010120.json
tradable shard: atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv

Stage2 entry row:
2024-03-05,71600.0,80500.0,70800.0,77800.0,...

forward anchors:
2024-04-12 high = 157,700
2024-05-29 high = 244,000
2024-07-24 high = 274,500
2024-09-09 low = 126,200

Stage4B entry row:
2024-07-24,258000.0,274500.0,255000.0,260000.0,...
```

### 5.3 대한전선 / 001440

```text
profile: atlas/symbol_profiles/001/001440.json
tradable shard: atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv

entry row:
2024-05-13,15000.0,18900.0,14640.0,18110.0,...

forward anchors:
2024-05-21 high = 20,950
2024-06-13 low = 14,050
2024-09-09 low = 10,270
2024-12-09 low = 10,000
```

## 6. Stage evidence separation

### Stage2 evidence fields

```text
010120 / LS ELECTRIC:
- public earnings and order/backlog narrative proxy
- switchgear / power equipment demand route
- datacenter/grid CAPEX bottleneck route
- relative strength confirmed by 2024-03-05 Stock-Web row
- low initial MAE with high 30D/90D MFE

267260 / HD현대일렉트릭:
- public earnings and transformer backlog narrative proxy
- North America / grid transformer demand route
- margin and revision bridge proxy
- early price path confirmed by 2023-01-27 Stock-Web row
```

### Stage3 evidence fields

```text
Required for Green:
- confirmed EPS/FCF revision
- backlog or delivery visibility
- margin conversion
- multiple non-price evidence families
- no cable-theme-only proxy
```

The two positive cases would support Stage2/Stage3-Yellow earlier than a generic industrial score. However, because exact primary evidence URLs were not attached in this standalone run, this MD should be used as shadow evidence until later ingestion verifies source URLs.

### 4B evidence fields

```text
010120 / 2024-07-24:
- local and full-window peak proximity = 1.0
- price reached 274,500 high on entry date
- later 180D MAE reached -51.4615% from the 260,000 entry close
- this supports non-price 4B overlay after structural success, not a price-only 4B from the first breakout
```

### 4C evidence fields

```text
No hard 4C thesis-break is proposed.
The cable-theme counterexample is a Green/Stage2 guardrail case, not a hard thesis-break.
```

## 7. Current calibrated profile stress test

Current calibrated profile assumptions already block price-only blowoff and require non-price evidence for full 4B. This C02 run tests a narrower residual:

```text
residual = C02 is under-covered as its own canonical route.
positive failure mode = transformer/switchgear winners may be detected too late if C02 is folded into generic industrials.
counterexample failure mode = cable/grid theme extensions can look like C02 but lack EPS/FCF and margin bridge.
```

Stress-test conclusion:

```text
1. C02 should not loosen Stage3-Green global threshold.
2. C02 should receive a scoped Stage2/Yelllow observation route when transformer/switchgear backlog + margin/revision evidence exists.
3. C02 cable-theme extension should require non-price bridge before Stage2/Green promotion.
4. C02 4B overlay is useful after structural success; price-only cable blowoff should remain watch/counterexample.
```

## 8. Positive / counterexample balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 1
4B_or_4C_case = 1
calibration_usable_case_count = 4
counterexample_search_incomplete = false
```

This is enough for a standalone residual MD, but not enough for global default promotion because source URLs remain pending.

## 9. Residual contribution summary

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
loop_contribution_label = new_independent_signal
do_not_propose_new_weight_delta = false
promotion_blocker = evidence_url_pending_source_proxy_only
```

One-line contribution:

```text
This standalone loop adds 4 new independent cases, 1 counterexample, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.
```

## 10. Machine-readable rows

### case rows

```jsonl
{"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_NO_REPEAT_010120_LS_ELECTRIC_20240305_GRID_DC_STAGE2", "case_type": "structural_success", "company_name": "LS ELECTRIC", "do_not_count_as_new_case": false, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "evidence_url_pending": true, "fine_archetype_id": "GRID_EQUIPMENT_DATACENTER_CAPEX_EXPORT_BACKLOG", "hard_duplicate_avoided": true, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_type": "case", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "source_proxy_only": true, "stock_web_manifest_max_date": "2026-02-20", "symbol": "010120", "trigger_family": "earnings_revision_plus_grid_datacenter_order_visibility"}
{"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_NO_REPEAT_267260_HD_HYUNDAI_ELECTRIC_20230127_TRANSFORMER_STAGE2", "case_type": "structural_success", "company_name": "HD현대일렉트릭", "do_not_count_as_new_case": false, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "evidence_url_pending": true, "fine_archetype_id": "TRANSFORMER_EXPORT_BACKLOG_OLD_FRAME_RERATING", "hard_duplicate_avoided": true, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_type": "case", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "source_proxy_only": true, "stock_web_manifest_max_date": "2026-02-20", "symbol": "267260", "trigger_family": "transformer_backlog_margin_revision"}
{"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_NO_REPEAT_001440_TAIHAN_CABLE_20240513_CABLE_THEME_HIGH_MAE", "case_type": "price_moved_without_evidence", "company_name": "대한전선", "do_not_count_as_new_case": false, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "evidence_url_pending": true, "fine_archetype_id": "CABLE_THEME_PRICE_ONLY_CAPEX_EXTENSION", "hard_duplicate_avoided": true, "independent_evidence_weight": 1.0, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_type": "case", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "source_proxy_only": true, "stock_web_manifest_max_date": "2026-02-20", "symbol": "001440", "trigger_family": "cable_theme_blowoff_without_eps_fcf_bridge"}
{"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_NO_REPEAT_010120_LS_ELECTRIC_20240724_LOCAL_4B_PEAK", "case_type": "4B_overlay_success", "company_name": "LS ELECTRIC", "do_not_count_as_new_case": false, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "evidence_url_pending": true, "fine_archetype_id": "GRID_EQUIPMENT_FULL_WINDOW_4B_PEAK_CAPTURE", "hard_duplicate_avoided": true, "independent_evidence_weight": 0.5, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "positive_or_counterexample": "neutral_guardrail", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_type": "case", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "source_proxy_only": true, "stock_web_manifest_max_date": "2026-02-20", "symbol": "010120", "trigger_family": "valuation_blowoff_non_price_4b_overlay"}
```

### trigger rows

```jsonl
{"MAE_180D_pct": -8.9974, "MAE_30D_pct": -8.9974, "MAE_90D_pct": -8.9974, "MFE_180D_pct": 252.8278, "MFE_30D_pct": 102.6992, "MFE_90D_pct": 213.6247, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_NO_REPEAT_010120_LS_ELECTRIC_20240305_GRID_DC_STAGE2", "company_name": "LS ELECTRIC", "current_profile_verdict": "current_profile_missed_structural_scope_C02_absent_or_underweighted", "dedupe_for_aggregate": true, "drawdown_after_peak_pct": -54.0255, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "entry_date": "2024-03-05", "entry_price": 77800, "evidence_family": "earnings|order_backlog|datacenter_capex_theme|stock_web_ohlc", "forward_window_trading_days": 180, "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "peak_date": "2024-07-24", "peak_price": 274500, "peak_return_from_entry_pct": 252.8278, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "010120", "trigger_date": "2024-03-05", "trigger_id": "C02_010120_20240305_STAGE2_GRID_DC_ORDER_VISIBILITY", "trigger_outcome_label": "good_stage2_high_mfe_low_initial_mae", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -5.1546, "MAE_30D_pct": -5.1546, "MAE_90D_pct": -5.1546, "MFE_180D_pct": 116.4948, "MFE_30D_pct": 18.299, "MFE_90D_pct": 41.7526, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_NO_REPEAT_267260_HD_HYUNDAI_ELECTRIC_20230127_TRANSFORMER_STAGE2", "company_name": "HD현대일렉트릭", "current_profile_verdict": "current_profile_missed_structural_scope_C02_absent_or_underweighted", "dedupe_for_aggregate": true, "drawdown_after_peak_pct": -26.9048, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "entry_date": "2023-01-27", "entry_price": 38800, "evidence_family": "earnings|transformer_backlog|north_america_grid|stock_web_ohlc", "forward_window_trading_days": 180, "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "peak_date": "2023-07-26", "peak_price": 84000, "peak_return_from_entry_pct": 116.4948, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "267260", "trigger_date": "2023-01-27", "trigger_id": "C02_267260_20230127_STAGE2_TRANSFORMER_BACKLOG", "trigger_outcome_label": "good_stage2_good_forward_return", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -44.7819, "MAE_30D_pct": -22.4186, "MAE_90D_pct": -43.291, "MFE_180D_pct": 15.6819, "MFE_30D_pct": 15.6819, "MFE_90D_pct": 15.6819, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_NO_REPEAT_001440_TAIHAN_CABLE_20240513_CABLE_THEME_HIGH_MAE", "company_name": "대한전선", "current_profile_verdict": "current_profile_false_positive_risk_if_cable_theme_treated_as_C02_green", "dedupe_for_aggregate": true, "drawdown_after_peak_pct": -52.2673, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "entry_date": "2024-05-13", "entry_price": 18110, "evidence_family": "price_theme|cable_capex_story|insufficient_eps_fcf_bridge|stock_web_ohlc", "forward_window_trading_days": 180, "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "peak_date": "2024-05-21", "peak_price": 20950, "peak_return_from_entry_pct": 15.6819, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "001440", "trigger_date": "2024-05-13", "trigger_id": "C02_001440_20240513_PRICE_ONLY_CABLE_THEME_COUNTEREXAMPLE", "trigger_outcome_label": "bad_stage2_or_false_green_high_mae_counterexample", "trigger_type": "Stage3-Yellow"}
{"MAE_180D_pct": -51.4615, "MAE_30D_pct": -44.2308, "MAE_90D_pct": -51.4615, "MFE_180D_pct": 5.5769, "MFE_30D_pct": 5.5769, "MFE_90D_pct": 5.5769, "aggregate_group_role": "representative", "calibration_usable": true, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "case_id": "C02_NO_REPEAT_010120_LS_ELECTRIC_20240724_LOCAL_4B_PEAK", "company_name": "LS ELECTRIC", "current_profile_verdict": "current_profile_correct_if_non_price_4B_overlay_allowed_for_C02", "dedupe_for_aggregate": true, "drawdown_after_peak_pct": -54.0255, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "entry_date": "2024-07-24", "entry_price": 260000, "evidence_family": "valuation_blowoff|non_price_grid_backlog_context|stock_web_ohlc", "forward_window_trading_days": 180, "four_b_full_window_peak_proximity": 1.0, "four_b_local_peak_proximity": 1.0, "guardrail_usable": true, "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "peak_date": "2024-07-24", "peak_price": 274500, "peak_return_from_entry_pct": 5.5769, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20", "symbol": "010120", "trigger_date": "2024-07-24", "trigger_id": "C02_010120_20240724_STAGE4B_FULL_WINDOW_PEAK_CAPTURE", "trigger_outcome_label": "good_4b_timing", "trigger_type": "Stage4B"}
```

### score_simulation rows

```jsonl
{"as_of_date": "2024-03-05", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "current_profile_stress_result": "C02-specific visibility/bottleneck weighting would have upgraded Stage2 confidence without lowering Green threshold.", "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_scores_after": {"bottleneck_pricing": 20, "capital_allocation": 4, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 5, "market_mispricing": 14, "valuation_rerating": 12}, "raw_component_scores_before": {"bottleneck_pricing": 16, "capital_allocation": 3, "earnings_visibility": 15, "eps_fcf_explosion": 15, "information_confidence": 4, "market_mispricing": 11, "valuation_rerating": 9}, "row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "simulation_id": "C02_component_proxy_010120_stage2", "stock_web_manifest_max_date": "2026-02-20", "symbol": "010120"}
{"as_of_date": "2024-05-13", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "current_profile_stress_result": "C02 cable/theme extension needs EPS/FCF bridge and contract/margin evidence; price-only or capacity story should remain below Green.", "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "raw_component_scores_after": {"bottleneck_pricing": 13, "capital_allocation": 2, "earnings_visibility": 6, "eps_fcf_explosion": 8, "information_confidence": 3, "market_mispricing": 8, "valuation_rerating": 6}, "raw_component_scores_before": {"bottleneck_pricing": 14, "capital_allocation": 2, "earnings_visibility": 7, "eps_fcf_explosion": 9, "information_confidence": 2, "market_mispricing": 12, "valuation_rerating": 8}, "row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "simulation_id": "C02_component_proxy_001440_counter", "stock_web_manifest_max_date": "2026-02-20", "symbol": "001440"}
```

### aggregate_metric rows

```jsonl
{"bad_stage2_count": 1, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "counterexample_count": 1, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "evidence_url_pending_count": 4, "good_4b_timing_count": 1, "good_stage2_count": 2, "group_name": "canonical_archetype_id", "group_value": "C02_POWER_GRID_DATACENTER_CAPEX", "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "positive_case_count": 2, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "row_count": 4, "row_type": "aggregate_metric", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "source_proxy_only_count": 4, "stage2_bad_entry_rate_MAE90_le_minus_20": 0.3333, "stage2_hit_rate_MFE90_ge_20": 0.6667, "stage4b_case_count": 1, "stock_web_manifest_max_date": "2026-02-20", "unique_symbol_count": 3}
```

### shadow_weight rows

```jsonl
{"axis": "stage2_required_bridge", "candidate_value": "require_non_price_bridge_for_cable_theme_extension", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "reason": "C02 positives need transformer/grid/datacenter backlog and margin/revision bridge; cable-theme proxy row had high MAE and weak EPS/FCF bridge.", "row_type": "shadow_weight", "schema_family": "v12_sector_archetype_residual", "scope": "canonical_archetype:C02_POWER_GRID_DATACENTER_CAPEX", "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20"}
{"axis": "archetype_weight_runtime_candidate", "candidate_value": {"bottleneck_pricing": 19, "capital_allocation": 5, "earnings_visibility": 24, "eps_fcf_explosion": 21, "information_confidence": 5, "market_mispricing": 14, "valuation_rerating": 12}, "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "reason": "Visibility and bottleneck deserve higher weight for proven transformer/grid equipment, but not for price-only cable proxies.", "row_type": "shadow_weight", "schema_family": "v12_sector_archetype_residual", "scope": "canonical_archetype:C02_POWER_GRID_DATACENTER_CAPEX", "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20"}
```

### residual_contribution rows

```jsonl
{"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "conclusion": "C02 is absent from No-Repeat coverage table and should be filled with new symbols and failure modes before any runtime C02 weight is promoted.", "counterexample_count": 1, "current_profile_error_count": 2, "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "new_independent_case_count": 4, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "residual_id": "C02_scope_missing_or_undercovered", "residual_type": "coverage_gap_fill", "reused_case_count": 0, "row_type": "residual_contribution", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20"}
```

### narrative_only rows

```jsonl
{"canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "duplicate_check_basis": "docs/core/V12_Research_No_Repeat_Index.md", "hard_duplicate_avoided": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "note": "Primary evidence URLs should be attached in later ingestion; this standalone run used source-name-level public earnings/order/backlog proxies plus exact Stock-Web OHLC rows for quantitative validation.", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocker": "source_proxy_only_and_evidence_url_pending", "row_type": "narrative_only", "schema_family": "v12_sector_archetype_residual", "selected_round": "R1", "stock_web_manifest_max_date": "2026-02-20"}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff inside the research runner.

When batching this MD into stock_agent:
1. Place this file under docs/round or the configured v12 input root.
2. Verify primary evidence URLs for LS ELECTRIC, HD현대일렉트릭, and 대한전선 before promotion.
3. Keep production scoring unchanged unless run-v12-calibration generates apply_next_patch.
4. Add or verify C02_POWER_GRID_DATACENTER_CAPEX in runtime archetype seed before applying archetype-specific weight.
5. Treat this MD as C02 shadow evidence:
   - transformer/switchgear backlog + margin/revision = positive route
   - cable theme without EPS/FCF bridge = counterexample route
   - LS ELECTRIC 2024-07-24 = non-price full-window 4B overlay support
6. Do not use future MFE/MAE/peak as live scoring inputs; use them only for historical calibration.
```

## 12. Final state

```text
completed_as_standalone_no_repeat = true
selected_round = R1
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_TRANSFORMER_DATACENTER_CAPEX_WITH_CABLE_THEME_COUNTEREXAMPLE
round_schedule_status = scheduler_override_no_loop
round_sector_consistency = pass
hard_duplicate_avoided = true
index_update_needed = true
```

