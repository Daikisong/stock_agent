# E2R v12 Stock-Web Residual Research — R9 / L3 / C29 Mobility Volume-Margin Operating Leverage

```text
research_mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R9
selected_loop = 220
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/direct-evidence quality repair + sector balance refresh
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection and novelty rationale

The current No-Repeat Index says the v12 corpus is no longer in a simple 30/50/80-row filling phase. The next work should prioritize direct URL/proxy-quality repair, missing-price repair, false-positive taxonomy, and residual error cleanup. C29 is not row-starved, but it has enough mobility/OEM and supplier cases to support a targeted quality refresh. This run avoids the immediately repeated C05/C10/C13 loop pattern and tests a new C29 fine axis: **record OEM margin / supplier offset quality / peak-cycle Green blocker**.

Hard duplicate key used for avoidance:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This batch uses fresh C29 trigger families in this session:

- OEM record margin with weak forward MFE and deep MAE.
- Tire premium-mix operating leverage that is valid Stage2-Actionable but not Yellow/Green.
- Electrification/EV supplier weakness with A/S, China/India, or order-book offset.
- Parts supplier reopen where annual operating-profit, module/core parts, or business-mix bridge is visible.

## 2. Stock-Web price source validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
tradable_schema = d,o,h,l,c,v,a,mc,s,m
```

All usable trigger rows below have 30D/90D/180D forward windows inside Stock-Web's manifest max date. Corporate-action candidate windows were checked at profile level when visible in the symbol profile. Hanon Systems is kept as a narrative-only blocked diagnostic because its 2025-01-09 corporate-action candidate falls inside the 180D window after the 2024-08-08 event row.

## 3. Batch summary

```text
new_independent_case_count = 7
new_independent_trigger_count = 7
unique_symbol_count_usable = 6
stage2_count = 1
stage2_actionable_count = 5
stage4b_count = 1
stage4c_count = 0
narrative_only_blocked_count = 1
positive_or_reopen_case_count = 4
counterexample_or_guardrail_case_count = 4
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count_for_usable_rows = 0
insufficient_forward_window_180D_count_for_usable_rows = 0
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 4. Trigger-level price table

| symbol | name | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| 005380 | Hyundai Motor | Stage2-Actionable | 2024-07-25 | 251500 | 6.16/-13.92 | 6.16/-21.55 | 6.16/-30.10 | 2024-08-29 | 2025-04-11 |
| 000270 | Kia | Stage2-Actionable | 2024-07-26 | 112100 | 5.71/-15.25 | 5.71/-20.16 | 5.71/-27.48 | 2024-07-26 | 2025-04-11 |
| 161390 | Hankook Tire & Technology | Stage2-Actionable | 2024-05-02 | 54700 | 6.58/-22.94 | 6.58/-30.80 | 6.58/-36.93 | 2024-05-02 | 2024-10-29 |
| 012330 | Hyundai Mobis | Stage4B | 2024-07-26 | 225500 | 2.22/-11.09 | 18.40/-11.09 | 28.16/-11.09 | 2025-03-25 | 2024-08-05 |
| 012330 | Hyundai Mobis | Stage2-Actionable | 2025-01-31 | 263500 | 2.09/-8.73 | 10.25/-11.95 | 24.10/-11.95 | 2025-09-09 | 2025-04-14 |
| 204320 | HL Mando | Stage2 | 2025-02-05 | 42300 | 11.11/-6.50 | 11.11/-24.11 | 11.11/-24.11 | 2025-02-13 | 2025-06-16 |
| 011210 | Hyundai Wia | Stage2-Actionable | 2025-01-24 | 39950 | 16.65/-7.63 | 26.16/-7.63 | 45.18/-7.63 | 2025-10-22 | 2025-02-03 |

## 5. Case notes


### Case 1. 005380 Hyundai Motor — Stage2-Actionable

- evidence_date: `2024-07-25`
- evidence_family: `record_Q2_OP_margin_US_SUV_HEV_mix`
- source_url: https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q2-business-results-0000000801
- entry_date: `2024-07-25` / entry_close: `251500`
- actual entry OHLCV: `o=253000, h=255000, l=247500, c=251500, v=832753`
- 30D MFE/MAE: `6.16% / -13.92%`
- 90D MFE/MAE: `6.16% / -21.55%`
- 180D MFE/MAE: `6.16% / -30.10%`, peak `2024-08-29`, trough `2025-04-11`
- stress-test label: `green_overrisk_if_record_margin_repeated_without_volume_cash_bridge`

Interpretation: `Stage2-Actionable` is preserved only when volume/mix/margin evidence is issuer-level. Large OEM record-margin rows with weak subsequent MFE and deep MAE are not bearish by themselves, but they are strong evidence for a Yellow/Green escalation brake. Supplier rows with offset quality should route to Stage4B/watch before hard 4C unless volume, order, or margin thesis breaks are confirmed.


### Case 2. 000270 Kia — Stage2-Actionable

- evidence_date: `2024-07-26`
- evidence_family: `record_Q2_OP_margin_product_mix`
- source_url: https://worldwide.kia.com/en/newsroom/view/?id=161729
- entry_date: `2024-07-26` / entry_close: `112100`
- actual entry OHLCV: `o=118500, h=118500, l=110000, c=112100, v=1582067`
- 30D MFE/MAE: `5.71% / -15.25%`
- 90D MFE/MAE: `5.71% / -20.16%`
- 180D MFE/MAE: `5.71% / -27.48%`, peak `2024-07-26`, trough `2025-04-11`
- stress-test label: `green_overrisk_if_record_margin_repeated_without_volume_cash_bridge`

Interpretation: `Stage2-Actionable` is preserved only when volume/mix/margin evidence is issuer-level. Large OEM record-margin rows with weak subsequent MFE and deep MAE are not bearish by themselves, but they are strong evidence for a Yellow/Green escalation brake. Supplier rows with offset quality should route to Stage4B/watch before hard 4C unless volume, order, or margin thesis breaks are confirmed.


### Case 3. 161390 Hankook Tire & Technology — Stage2-Actionable

- evidence_date: `2024-05-02`
- evidence_family: `premium_tire_mix_OP_growth`
- source_url: https://www.hankooktire.com/mea/en/company/media-list/media-detail.630032.html
- entry_date: `2024-05-02` / entry_close: `54700`
- actual entry OHLCV: `o=57700, h=58300, l=54700, c=54700, v=575783`
- 30D MFE/MAE: `6.58% / -22.94%`
- 90D MFE/MAE: `6.58% / -30.80%`
- 180D MFE/MAE: `6.58% / -36.93%`, peak `2024-05-02`, trough `2024-10-29`
- stress-test label: `yellow_green_high_mae_brake_needed`

Interpretation: `Stage2-Actionable` is preserved only when volume/mix/margin evidence is issuer-level. Large OEM record-margin rows with weak subsequent MFE and deep MAE are not bearish by themselves, but they are strong evidence for a Yellow/Green escalation brake. Supplier rows with offset quality should route to Stage4B/watch before hard 4C unless volume, order, or margin thesis breaks are confirmed.


### Case 4. 012330 Hyundai Mobis — Stage4B

- evidence_date: `2024-07-26`
- evidence_family: `EV_electrification_weakness_AS_margin_offset`
- source_url: https://en.topdaily.kr/articles/1942
- entry_date: `2024-07-26` / entry_close: `225500`
- actual entry OHLCV: `o=227500, h=230500, l=221000, c=225500, v=313091`
- 30D MFE/MAE: `2.22% / -11.09%`
- 90D MFE/MAE: `18.40% / -11.09%`
- 180D MFE/MAE: `28.16% / -11.09%`, peak `2025-03-25`, trough `2024-08-05`
- stress-test label: `hard_4c_overrisk_if_offset_quality_ignored`

Interpretation: `Stage4B` is preserved only when volume/mix/margin evidence is issuer-level. Large OEM record-margin rows with weak subsequent MFE and deep MAE are not bearish by themselves, but they are strong evidence for a Yellow/Green escalation brake. Supplier rows with offset quality should route to Stage4B/watch before hard 4C unless volume, order, or margin thesis breaks are confirmed.


### Case 5. 012330 Hyundai Mobis — Stage2-Actionable

- evidence_date: `2025-01-31`
- evidence_family: `4Q24_beat_module_core_AS_margin_bridge`
- source_url: https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2329976
- entry_date: `2025-01-31` / entry_close: `263500`
- actual entry OHLCV: `o=266000, h=268500, l=259500, c=263500, v=288546`
- 30D MFE/MAE: `2.09% / -8.73%`
- 90D MFE/MAE: `10.25% / -11.95%`
- 180D MFE/MAE: `24.10% / -11.95%`, peak `2025-09-09`, trough `2025-04-14`
- stress-test label: `yellow_green_high_mae_brake_needed`

Interpretation: `Stage2-Actionable` is preserved only when volume/mix/margin evidence is issuer-level. Large OEM record-margin rows with weak subsequent MFE and deep MAE are not bearish by themselves, but they are strong evidence for a Yellow/Green escalation brake. Supplier rows with offset quality should route to Stage4B/watch before hard 4C unless volume, order, or margin thesis breaks are confirmed.


### Case 6. 204320 HL Mando — Stage2

- evidence_date: `2025-02-05`
- evidence_family: `FY2024_growth_margin_orders_but_debt_tax_guardrail`
- source_url: https://englishdart.fss.or.kr/report/downloadEng.do?dcmNo=10289586&flNm=HL+Mando+4Q24+results_vf_revised.pdf
- entry_date: `2025-02-05` / entry_close: `42300`
- actual entry OHLCV: `o=41950, h=42500, l=41750, c=42300, v=87882`
- 30D MFE/MAE: `11.11% / -6.50%`
- 90D MFE/MAE: `11.11% / -24.11%`
- 180D MFE/MAE: `11.11% / -24.11%`, peak `2025-02-13`, trough `2025-06-16`
- stress-test label: `stage2_actionable_cap_until_second_bridge_repeats`

Interpretation: `Stage2` is preserved only when volume/mix/margin evidence is issuer-level. Large OEM record-margin rows with weak subsequent MFE and deep MAE are not bearish by themselves, but they are strong evidence for a Yellow/Green escalation brake. Supplier rows with offset quality should route to Stage4B/watch before hard 4C unless volume, order, or margin thesis breaks are confirmed.


### Case 7. 011210 Hyundai Wia — Stage2-Actionable

- evidence_date: `2025-01-24`
- evidence_family: `FY2024_revenue_OP_auto_parts_special_business_mix`
- source_url: https://biz.chosun.com/en/en-industry/2025/01/24/4G2N4YKVVRHUTCKCVERKULPVYA/
- entry_date: `2025-01-24` / entry_close: `39950`
- actual entry OHLCV: `o=39450, h=40400, l=39450, c=39950, v=52209`
- 30D MFE/MAE: `16.65% / -7.63%`
- 90D MFE/MAE: `26.16% / -7.63%`
- 180D MFE/MAE: `45.18% / -7.63%`, peak `2025-10-22`, trough `2025-02-03`
- stress-test label: `yellow_green_high_mae_brake_needed`

Interpretation: `Stage2-Actionable` is preserved only when volume/mix/margin evidence is issuer-level. Large OEM record-margin rows with weak subsequent MFE and deep MAE are not bearish by themselves, but they are strong evidence for a Yellow/Green escalation brake. Supplier rows with offset quality should route to Stage4B/watch before hard 4C unless volume, order, or margin thesis breaks are confirmed.


### Narrative-only blocked diagnostic — 018880 Hanon Systems

- evidence_date: `2024-08-08`
- trigger_type: `Stage4B / blocked_from_weight_calibration`
- source_url: https://www.hanonsystems.com/En/Media/NewsDetails/316
- entry_date: `2024-08-08` / entry_close: `4065`
- 180D MFE/MAE before blocking: `18.45% / -23.37%`
- blocked_reason: `corporate_action_candidate_2025-01-09_inside_180D_forward_window`

Interpretation: Hanon is useful taxonomy evidence for EV-thermal supplier slowdown with temporary-factor offset, but it is not used for weight calibration in this batch because the 180D price window is contaminated by a Stock-Web corporate-action candidate.

## 6. Residual contribution summary

```text
rule_candidate:
C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1

sector_rule_candidate:
L3_MOBILITY_VOLUME_MARGIN_SECOND_BRIDGE_AND_PEAK_CYCLE_GREEN_BLOCKER

core_residual:
- OEM record revenue / record operating profit / high OPM is not enough for Stage3-Yellow or Stage3-Green when volume growth, incentive pressure, tariff risk, or demand slowdown is visible.
- Stage2-Actionable requires at least one issuer-level second bridge: volume growth, mix improvement, operating-profit margin conversion, shareholder/capital-return support, order backlog, named customer route, or margin/cash conversion.
- Supplier weakness caused by EV/electrification slowdown routes first to Stage4B/watch when A/S margin, China/India sales, order-book, or business-mix offset is visible.
- High MAE after valid OEM or supplier bridge blocks Yellow/Green first; it does not erase Stage2-Actionable.
- Stage4C requires confirmed non-price thesis break: volume collapse, incentive/tariff margin break, order cancellation, customer loss, liquidity stress, or weak offset quality.
```

## 7. Current calibrated profile stress-test

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated / e2r_2_2_rolling_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Stress-test result:

- Hyundai/Kia/Hankook show that strong reported margin can still be a late-cycle evidence row; 180D MFE is weak while MAE is deep.
- Hyundai Mobis 2024-07-26 shows that an EV/electrification slowdown row should not be sticky hard 4C when A/S margin offset survives.
- Hyundai Mobis 2025-01-31, HL Mando 2025-02-05, and Hyundai Wia 2025-01-24 show that supplier/parts reopen requires realized profit, order, or business-mix bridge, not just automotive beta.

## 8. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "research_session": "v12_residual", "selected_round": "R9", "selected_loop": 220, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1", "symbol": "005380", "name": "Hyundai Motor", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-07-25", "entry_date": "2024-07-25", "entry_price": 251500.0, "entry_ohlcv": {"o": 253000.0, "h": 255000.0, "l": 247500.0, "c": 251500.0, "v": 832753, "a": 209029957500.0, "mc": 52668172036500.0, "m": "KOSPI"}, "price_source_validation": {"source_repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard": "atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv", "forward_rows_180d": 181, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "mfe_mae": {"mfe_30d_pct": 6.16, "mae_30d_pct": -13.92, "mfe_90d_pct": 6.16, "mae_90d_pct": -21.55, "mfe_180d_pct": 6.16, "mae_180d_pct": -30.1, "peak_180d_date": "2024-08-29", "trough_180d_date": "2025-04-11"}, "evidence_family": "record_Q2_OP_margin_US_SUV_HEV_mix", "case_role": "late_cycle_oem_record_margin_guardrail", "source_url": "https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q2-business-results-0000000801", "score_simulation": {"eps_fcf_explosion": 16, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 8, "information_confidence": 8, "weighted_total": 80}, "current_profile_error_label": "green_overrisk_if_record_margin_repeated_without_volume_cash_bridge", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_session": "v12_residual", "selected_round": "R9", "selected_loop": 220, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1", "symbol": "000270", "name": "Kia", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-07-26", "entry_date": "2024-07-26", "entry_price": 112100.0, "entry_ohlcv": {"o": 118500.0, "h": 118500.0, "l": 110000.0, "c": 112100.0, "v": 1582067, "a": 178615434250.0, "mc": 44824128545700.0, "m": "KOSPI"}, "price_source_validation": {"source_repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard": "atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv", "forward_rows_180d": 181, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "mfe_mae": {"mfe_30d_pct": 5.71, "mae_30d_pct": -15.25, "mfe_90d_pct": 5.71, "mae_90d_pct": -20.16, "mfe_180d_pct": 5.71, "mae_180d_pct": -27.48, "peak_180d_date": "2024-07-26", "trough_180d_date": "2025-04-11"}, "evidence_family": "record_Q2_OP_margin_product_mix", "case_role": "late_cycle_oem_record_margin_guardrail", "source_url": "https://worldwide.kia.com/en/newsroom/view/?id=161729", "score_simulation": {"eps_fcf_explosion": 16, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 8, "information_confidence": 8, "weighted_total": 80}, "current_profile_error_label": "green_overrisk_if_record_margin_repeated_without_volume_cash_bridge", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_session": "v12_residual", "selected_round": "R9", "selected_loop": 220, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1", "symbol": "161390", "name": "Hankook Tire & Technology", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-05-02", "entry_date": "2024-05-02", "entry_price": 54700.0, "entry_ohlcv": {"o": 57700.0, "h": 58300.0, "l": 54700.0, "c": 54700.0, "v": 575783, "a": 32075194600.0, "mc": 6775966274300.0, "m": "KOSPI"}, "price_source_validation": {"source_repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "forward_rows_180d": 181, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "mfe_mae": {"mfe_30d_pct": 6.58, "mae_30d_pct": -22.94, "mfe_90d_pct": 6.58, "mae_90d_pct": -30.8, "mfe_180d_pct": 6.58, "mae_180d_pct": -36.93, "peak_180d_date": "2024-05-02", "trough_180d_date": "2024-10-29"}, "evidence_family": "premium_tire_mix_OP_growth", "case_role": "tire_mix_input_cost_high_mae_guardrail", "source_url": "https://www.hankooktire.com/mea/en/company/media-list/media-detail.630032.html", "score_simulation": {"eps_fcf_explosion": 16, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 8, "information_confidence": 8, "weighted_total": 80}, "current_profile_error_label": "yellow_green_high_mae_brake_needed", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_session": "v12_residual", "selected_round": "R9", "selected_loop": 220, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1", "symbol": "012330", "name": "Hyundai Mobis", "trigger_type": "Stage4B", "evidence_date": "2024-07-26", "entry_date": "2024-07-26", "entry_price": 225500.0, "entry_ohlcv": {"o": 227500.0, "h": 230500.0, "l": 221000.0, "c": 225500.0, "v": 313091, "a": 70761292500.0, "mc": 20970393697000.0, "m": "KOSPI"}, "price_source_validation": {"source_repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard": "atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv", "forward_rows_180d": 181, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "mfe_mae": {"mfe_30d_pct": 2.22, "mae_30d_pct": -11.09, "mfe_90d_pct": 18.4, "mae_90d_pct": -11.09, "mfe_180d_pct": 28.16, "mae_180d_pct": -11.09, "peak_180d_date": "2025-03-25", "trough_180d_date": "2024-08-05"}, "evidence_family": "EV_electrification_weakness_AS_margin_offset", "case_role": "electrification_slowdown_with_AS_offset", "source_url": "https://en.topdaily.kr/articles/1942", "score_simulation": {"eps_fcf_explosion": 8, "earnings_visibility": 10, "bottleneck_pricing": 6, "market_mispricing": 9, "valuation_rerating": 8, "capital_allocation": 5, "information_confidence": 14, "weighted_total": 60}, "current_profile_error_label": "hard_4c_overrisk_if_offset_quality_ignored", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_session": "v12_residual", "selected_round": "R9", "selected_loop": 220, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1", "symbol": "012330", "name": "Hyundai Mobis", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-01-31", "entry_date": "2025-01-31", "entry_price": 263500.0, "entry_ohlcv": {"o": 266000.0, "h": 268500.0, "l": 259500.0, "c": 263500.0, "v": 288546, "a": 76052252500.0, "mc": 24504207269000.0, "m": "KOSPI"}, "price_source_validation": {"source_repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard": "atlas/ohlcv_tradable_by_symbol_year/012/012330/2025.csv", "forward_rows_180d": 181, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "mfe_mae": {"mfe_30d_pct": 2.09, "mae_30d_pct": -8.73, "mfe_90d_pct": 10.25, "mae_90d_pct": -11.95, "mfe_180d_pct": 24.1, "mae_180d_pct": -11.95, "peak_180d_date": "2025-09-09", "trough_180d_date": "2025-04-14"}, "evidence_family": "4Q24_beat_module_core_AS_margin_bridge", "case_role": "module_core_parts_margin_reopen", "source_url": "https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2329976", "score_simulation": {"eps_fcf_explosion": 16, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 8, "information_confidence": 8, "weighted_total": 80}, "current_profile_error_label": "yellow_green_high_mae_brake_needed", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_session": "v12_residual", "selected_round": "R9", "selected_loop": 220, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1", "symbol": "204320", "name": "HL Mando", "trigger_type": "Stage2", "evidence_date": "2025-02-05", "entry_date": "2025-02-05", "entry_price": 42300.0, "entry_ohlcv": {"o": 41950.0, "h": 42500.0, "l": 41750.0, "c": 42300.0, "v": 87882, "a": 3701851750.0, "mc": 1986286176000.0, "m": "KOSPI"}, "price_source_validation": {"source_repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard": "atlas/ohlcv_tradable_by_symbol_year/204/204320/2025.csv", "forward_rows_180d": 181, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "mfe_mae": {"mfe_30d_pct": 11.11, "mae_30d_pct": -6.5, "mfe_90d_pct": 11.11, "mae_90d_pct": -24.11, "mfe_180d_pct": 11.11, "mae_180d_pct": -24.11, "peak_180d_date": "2025-02-13", "trough_180d_date": "2025-06-16"}, "evidence_family": "FY2024_growth_margin_orders_but_debt_tax_guardrail", "case_role": "order_backlog_but_margin_cap", "source_url": "https://englishdart.fss.or.kr/report/downloadEng.do?dcmNo=10289586&flNm=HL+Mando+4Q24+results_vf_revised.pdf", "score_simulation": {"eps_fcf_explosion": 13, "earnings_visibility": 15, "bottleneck_pricing": 7, "market_mispricing": 11, "valuation_rerating": 10, "capital_allocation": 7, "information_confidence": 9, "weighted_total": 72}, "current_profile_error_label": "stage2_actionable_cap_until_second_bridge_repeats", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_session": "v12_residual", "selected_round": "R9", "selected_loop": 220, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1", "symbol": "011210", "name": "Hyundai Wia", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-01-24", "entry_date": "2025-01-24", "entry_price": 39950.0, "entry_ohlcv": {"o": 39450.0, "h": 40400.0, "l": 39450.0, "c": 39950.0, "v": 52209, "a": 2089052500.0, "mc": 1086443565850.0, "m": "KOSPI"}, "price_source_validation": {"source_repo": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "shard": "atlas/ohlcv_tradable_by_symbol_year/011/011210/2025.csv", "forward_rows_180d": 181, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "mfe_mae": {"mfe_30d_pct": 16.65, "mae_30d_pct": -7.63, "mfe_90d_pct": 26.16, "mae_90d_pct": -7.63, "mfe_180d_pct": 45.18, "mae_180d_pct": -7.63, "peak_180d_date": "2025-10-22", "trough_180d_date": "2025-02-03"}, "evidence_family": "FY2024_revenue_OP_auto_parts_special_business_mix", "case_role": "auto_parts_defense_mix_profit_bridge", "source_url": "https://biz.chosun.com/en/en-industry/2025/01/24/4G2N4YKVVRHUTCKCVERKULPVYA/", "score_simulation": {"eps_fcf_explosion": 16, "earnings_visibility": 18, "bottleneck_pricing": 8, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 8, "information_confidence": 8, "weighted_total": 80}, "current_profile_error_label": "yellow_green_high_mae_brake_needed", "representative_for_aggregate": true, "production_scoring_changed": false, "shadow_weight_only": true}
```

## 9. Batch Ingest Self-Audit

```text
filename_matches_required_regex = true
compact_filename_forbidden = pass
metadata_round_matches_filename_round = true
metadata_loop_matches_filename_loop = true
selected_archetype_drives_round = true
invalid_round_sector_pair = false
stock_agent_code_accessed = false
stock_agent_code_patched = false
production_scoring_changed = false
live_candidate_mode = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
all_usable_trigger_rows_have_entry_price = true
all_usable_trigger_rows_have_actual_entry_ohlcv = true
all_usable_trigger_rows_have_30_90_180_mfe_mae = true
all_usable_trigger_rows_have_stock_web_shard_path = true
corporate_action_contaminated_usable_rows = 0
insufficient_forward_window_usable_rows = 0
narrative_only_blocked_rows = 1
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

When batch-applying v12 research artifacts, parse this MD as a standard v12 result file.
Use the JSONL rows above as trigger-level calibration rows.
Do not treat narrative-only blocked Hanon Systems as promotion evidence.
Consider adding only a scope-limited C29/L3 mobility rule candidate:
C29_OEM_SUPPLIER_VOLUME_MARGIN_MIX_AND_PEAK_CYCLE_GATE_V1.
Do not loosen Stage3-Green globally.
Preserve Stage2/Stage2-Actionable when direct volume/mix/margin/order bridge exists.
Apply high-MAE rows as Yellow/Green escalation brake, not Stage2 deletion.
```

## 11. Next Research State

```text
completed_round = R9
completed_loop = 220
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 direct URL/proxy quality repair + C29 sector-balance refresh
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
