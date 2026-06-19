# E2R Stock-Web V12 Residual Research — R1 C03 Defense Export Framework Backlog

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 112
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2
deep_sub_archetype_id = C03_DEEP_PRIME_DIRECT_EXPORT_CONTRACT_SUPPLIER_PROXY_HIGH_MAE_AND_THEME_LABEL_4B_4C_FILTER
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection basis

`V12_Research_No_Repeat_Index.md`의 published index 기준 C03은 `62 rows`인 Priority 2 quality-repair 구역이다. 이번 세션의 앞선 실행에서 Priority 0/1 및 several exact-50 groups가 로컬 50-row band까지 보강된 상태였으므로, 이번 loop는 minimum coverage fill이 아니라 **C03 positive-balance repair + prime direct contract vs supplier/theme proxy 분리 + high-MAE 4B/4C guardrail** 목적으로 선택했다.

Visible `docs/round` 기준 C03 표준 V12 파일은 `R1_loop_111`까지 존재하므로 이번 표준 파일은 `R1_loop_112`로 설정했다. 동일 C03 내에서도 같은 `symbol + trigger_type + entry_date` 반복은 피하고, direct contract / supplier-direct / framework negotiation / supply-chain proxy / theme proxy route를 분리했다.

## 2. Price atlas validation scope

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
entry_price_basis = entry_date close
forward_window_definition = entry row inclusive, 30/90/180 tradable rows
```

All 8 trigger rows below have complete `MFE_30D_pct`, `MAE_30D_pct`, `MFE_90D_pct`, `MAE_90D_pct`, `MFE_180D_pct`, and `MAE_180D_pct`. The KAI 2025 Philippines contract was checked but excluded from this MD because the 2025-06-04 entry had only 175 tradable rows available by the manifest max date; it remains narrative-only for future URL repair and is not used here.

Profile caveat check: visible profile rows showed historical corporate-action candidates for Hanwha Aerospace, Hanwha Systems, Hyundai Rotem, SNT Dynamics, and Victek, but the candidate dates visible in the profile are outside the selected 2024~2025 entry-to-D+180 windows. LIG Nex1, KAI, and Poongsan profiles showed no corporate-action candidates in the checked profile snippets. Therefore this MD sets `blocked_by_corporate_action=false` for all usable rows.

## 3. Event/evidence frame

- Direct prime contract route: Hanwha Aerospace Romania K9/K10 order and LIG Nex1 Saudi M-SAM II order are clean C03 positives because they tie a named issuer to a signed export framework/backlog event.
- Supplier-direct route: Hanwha Systems is stronger than generic theme proxies because the radar package is tied to the Cheongung-II export system, but still needs issuer-level margin bridge before Green.
- Framework-negotiation route: Hyundai Rotem K2 Poland production/second-batch headlines were directionally right but carried -32% MAE before the 180D payoff, so C03 should not treat framework talk as clean Stage3 without financing/signing visibility.
- Supply-chain and theme-proxy routes: Poongsan, SNT Dynamics, and Victek show why C03 needs a separate local-4B/high-MAE watch. Sympathy exposure can still produce MFE, but entry quality is fragile unless the issuer has direct backlog conversion.

## 4. Trigger summary table

| symbol | name | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | case_class |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 012450 | 한화에어로스페이스 | Stage3-Yellow | 2024-07-10 | 256500 | 28.65 | -3.7 | 65.69 | -3.7 | 246.98 | -3.7 | positive |
| 079550 | LIG넥스원 | Stage3-Yellow | 2024-02-06 | 113000 | 69.29 | -4.78 | 91.59 | -4.78 | 134.51 | -4.78 | positive |
| 272210 | 한화시스템 | Stage2-Actionable | 2024-07-10 | 18860 | 24.07 | -9.38 | 60.13 | -12.35 | 130.12 | -12.35 | positive |
| 064350 | 현대로템 | Stage2 | 2024-10-25 | 64300 | 8.09 | -26.59 | 46.97 | -32.12 | 242.92 | -32.12 | counterexample_high_mae_then_payoff |
| 047810 | 한국항공우주 | Stage2 | 2024-07-10 | 49600 | 19.35 | -3.23 | 42.34 | -3.23 | 97.58 | -3.23 | positive |
| 103140 | 풍산 | Stage2 | 2024-06-19 | 58700 | 21.12 | -2.39 | 26.06 | -19.93 | 26.06 | -21.38 | counterexample_proxy_low_quality |
| 003570 | SNT다이내믹스 | Stage2 | 2024-10-25 | 26800 | 3.92 | -32.01 | 39.93 | -39.33 | 120.15 | -39.33 | counterexample_high_mae_supplier_proxy |
| 065450 | 빅텍 | Stage4B-Local | 2024-07-10 | 4880 | 19.47 | -7.58 | 19.47 | -12.81 | 19.47 | -26.02 | counterexample_theme_proxy |

## 5. Machine-readable trigger rows JSONL

```jsonl
{"MAE_180D_pct": -3.7, "MAE_30D_pct": -3.7, "MAE_90D_pct": -3.7, "MFE_180D_pct": 246.98, "MFE_30D_pct": 28.65, "MFE_90D_pct": 65.69, "blocked_by_corporate_action": false, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_class": "positive", "current_profile_error": false, "dedupe_key": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|012450|Stage3-Yellow|2024-07-10", "entry_date": "2024-07-10", "entry_price": 256500.0, "evidence_note": "Romania K9/K10 direct order; backlog bridge visible.", "evidence_quality": "verified_url", "fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "forward_window_trading_days": 180, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "한화에어로스페이스", "peak_180D_date": "2025-05-07", "peak_30D_date": "2024-07-30", "peak_90D_date": "2024-11-12", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested_trigger_date": "2024-07-10", "selected_round": "R1", "stage4b_local": false, "stage4c": false, "symbol": "012450", "trigger_family": "direct_contract_k9_romania", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-08-05", "trough_30D_date": "2024-08-05", "trough_90D_date": "2024-08-05", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -4.78, "MAE_30D_pct": -4.78, "MAE_90D_pct": -4.78, "MFE_180D_pct": 134.51, "MFE_30D_pct": 69.29, "MFE_90D_pct": 91.59, "blocked_by_corporate_action": false, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_class": "positive", "current_profile_error": false, "dedupe_key": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|079550|Stage3-Yellow|2024-02-06", "entry_date": "2024-02-06", "entry_price": 113000.0, "evidence_note": "Saudi Cheongung M-SAM II export contract; direct export bridge.", "evidence_quality": "verified_url", "fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "forward_window_trading_days": 180, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "LIG넥스원", "peak_180D_date": "2024-10-22", "peak_30D_date": "2024-03-11", "peak_90D_date": "2024-06-19", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested_trigger_date": "2024-02-06", "selected_round": "R1", "stage4b_local": false, "stage4c": false, "symbol": "079550", "trigger_family": "direct_contract_msam_saudi", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-02-06", "trough_30D_date": "2024-02-06", "trough_90D_date": "2024-02-06", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -12.35, "MAE_30D_pct": -9.38, "MAE_90D_pct": -12.35, "MFE_180D_pct": 130.12, "MFE_30D_pct": 24.07, "MFE_90D_pct": 60.13, "blocked_by_corporate_action": false, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_class": "positive", "current_profile_error": true, "dedupe_key": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|272210|Stage2-Actionable|2024-07-10", "entry_date": "2024-07-10", "entry_price": 18860.0, "evidence_note": "MFR radar supplier in Cheongung II package; not prime, but direct supplier route.", "evidence_quality": "verified_url", "fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "forward_window_trading_days": 180, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "한화시스템", "peak_180D_date": "2025-03-19", "peak_30D_date": "2024-07-30", "peak_90D_date": "2024-11-14", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested_trigger_date": "2024-07-10", "selected_round": "R1", "stage4b_local": false, "stage4c": false, "symbol": "272210", "trigger_family": "supplier_direct_mfr_saudi", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-09-09", "trough_30D_date": "2024-08-05", "trough_90D_date": "2024-09-09", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -32.12, "MAE_30D_pct": -26.59, "MAE_90D_pct": -32.12, "MFE_180D_pct": 242.92, "MFE_30D_pct": 8.09, "MFE_90D_pct": 46.97, "blocked_by_corporate_action": false, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_class": "counterexample_high_mae_then_payoff", "current_profile_error": true, "dedupe_key": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|064350|Stage2|2024-10-25", "entry_date": "2024-10-25", "entry_price": 64300.0, "evidence_note": "K2 localization/second-batch headline before final contract; huge payoff but severe initial MAE.", "evidence_quality": "verified_url", "fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "forward_window_trading_days": 180, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "현대로템", "peak_180D_date": "2025-06-23", "peak_30D_date": "2024-11-20", "peak_90D_date": "2025-02-21", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested_trigger_date": "2024-10-25", "selected_round": "R1", "stage4b_local": true, "stage4c": false, "symbol": "064350", "trigger_family": "framework_negotiation_k2_poland", "trigger_type": "Stage2", "trough_180D_date": "2024-12-10", "trough_30D_date": "2024-12-05", "trough_90D_date": "2024-12-10", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -3.23, "MAE_30D_pct": -3.23, "MAE_90D_pct": -3.23, "MFE_180D_pct": 97.58, "MFE_30D_pct": 19.35, "MFE_90D_pct": 42.34, "blocked_by_corporate_action": false, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_class": "positive", "current_profile_error": true, "dedupe_key": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|047810|Stage2|2024-07-10", "entry_date": "2024-07-10", "entry_price": 49600.0, "evidence_note": "FA-50 export/service framework proxy; treat as Stage2 until fresh signed contract bridge.", "evidence_quality": "source_proxy_only", "fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "forward_window_trading_days": 180, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "한국항공우주", "peak_180D_date": "2025-03-18", "peak_30D_date": "2024-08-16", "peak_90D_date": "2024-11-14", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested_trigger_date": "2024-07-10", "selected_round": "R1", "stage4b_local": false, "stage4c": false, "symbol": "047810", "trigger_family": "aircraft_export_framework_fa50_proxy", "trigger_type": "Stage2", "trough_180D_date": "2024-08-05", "trough_30D_date": "2024-08-05", "trough_90D_date": "2024-08-05", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -21.38, "MAE_30D_pct": -2.39, "MAE_90D_pct": -19.93, "MFE_180D_pct": 26.06, "MFE_30D_pct": 21.12, "MFE_90D_pct": 26.06, "blocked_by_corporate_action": false, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_class": "counterexample_proxy_low_quality", "current_profile_error": true, "dedupe_key": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|103140|Stage2|2024-06-19", "entry_date": "2024-06-19", "entry_price": 58700.0, "evidence_note": "Ammo/copper supply-chain proxy moved with artillery demand but issuer-level export backlog bridge was weak.", "evidence_quality": "source_proxy_only", "fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "forward_window_trading_days": 180, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "풍산", "peak_180D_date": "2024-10-22", "peak_30D_date": "2024-07-10", "peak_90D_date": "2024-10-22", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested_trigger_date": "2024-06-19", "selected_round": "R1", "stage4b_local": true, "stage4c": false, "symbol": "103140", "trigger_family": "ammo_supply_chain_proxy", "trigger_type": "Stage2", "trough_180D_date": "2024-12-09", "trough_30D_date": "2024-07-30", "trough_90D_date": "2024-08-05", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.33, "MAE_30D_pct": -32.01, "MAE_90D_pct": -39.33, "MFE_180D_pct": 120.15, "MFE_30D_pct": 3.92, "MFE_90D_pct": 39.93, "blocked_by_corporate_action": false, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_class": "counterexample_high_mae_supplier_proxy", "current_profile_error": true, "dedupe_key": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|003570|Stage2|2024-10-25", "entry_date": "2024-10-25", "entry_price": 26800.0, "evidence_note": "Supplier proxy around K2 localization; payoff came only after -39% drawdown, so Stage2 needs high-MAE guard.", "evidence_quality": "source_proxy_only", "fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "forward_window_trading_days": 180, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "SNT다이내믹스", "peak_180D_date": "2025-06-23", "peak_30D_date": "2024-10-29", "peak_90D_date": "2025-03-10", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested_trigger_date": "2024-10-25", "selected_round": "R1", "stage4b_local": true, "stage4c": false, "symbol": "003570", "trigger_family": "k2_powerpack_supplier_proxy", "trigger_type": "Stage2", "trough_180D_date": "2024-12-09", "trough_30D_date": "2024-12-05", "trough_90D_date": "2024-12-09", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -26.02, "MAE_30D_pct": -7.58, "MAE_90D_pct": -12.81, "MFE_180D_pct": 19.47, "MFE_30D_pct": 19.47, "MFE_90D_pct": 19.47, "blocked_by_corporate_action": false, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "case_class": "counterexample_theme_proxy", "current_profile_error": true, "dedupe_key": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|065450|Stage4B-Local|2024-07-10", "entry_date": "2024-07-10", "entry_price": 4880.0, "evidence_note": "Electronic-warfare/K-defense label spike without verifiable export backlog conversion; hard 4C if no issuer bridge appears.", "evidence_quality": "source_proxy_only", "fine_archetype_id": "C03_DEFENSE_EXPORT_PRIME_AND_SUPPLIER_FRAMEWORK_BACKLOG_BRIDGE_V2", "forward_window_trading_days": 180, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "name": "빅텍", "peak_180D_date": "2024-08-07", "peak_30D_date": "2024-08-07", "peak_90D_date": "2024-08-07", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "requested_trigger_date": "2024-07-10", "selected_round": "R1", "stage4b_local": true, "stage4c": true, "symbol": "065450", "trigger_family": "defense_theme_proxy_no_backlog", "trigger_type": "Stage4B-Local", "trough_180D_date": "2025-04-07", "trough_30D_date": "2024-08-05", "trough_90D_date": "2024-11-15", "upstream_source": "FinanceData/marcap"}
```

## 6. Score / return alignment simulation JSONL

```jsonl
{"case_class": "positive", "current_profile_residual": false, "raw_component_score_breakdown": {"backlog_visibility": 84, "drawdown_guard": 86, "evidence_quality": 82, "margin_bridge": 72, "revision_confirmation": 58, "valuation_discipline": 65}, "recommended_shadow_rule_effect": "allow Stage3-Yellow only when direct contract/backlog bridge is present; Green still requires revision/margin confirmation", "symbol": "012450", "trigger_type": "Stage3-Yellow"}
{"case_class": "positive", "current_profile_residual": false, "raw_component_score_breakdown": {"backlog_visibility": 84, "drawdown_guard": 86, "evidence_quality": 82, "margin_bridge": 72, "revision_confirmation": 58, "valuation_discipline": 65}, "recommended_shadow_rule_effect": "allow Stage3-Yellow only when direct contract/backlog bridge is present; Green still requires revision/margin confirmation", "symbol": "079550", "trigger_type": "Stage3-Yellow"}
{"case_class": "positive", "current_profile_residual": true, "raw_component_score_breakdown": {"backlog_visibility": 84, "drawdown_guard": 86, "evidence_quality": 82, "margin_bridge": 72, "revision_confirmation": 58, "valuation_discipline": 65}, "recommended_shadow_rule_effect": "allow Stage3-Yellow only when direct contract/backlog bridge is present; Green still requires revision/margin confirmation", "symbol": "272210", "trigger_type": "Stage2-Actionable"}
{"case_class": "counterexample_high_mae_then_payoff", "current_profile_residual": true, "raw_component_score_breakdown": {"backlog_visibility": 55, "drawdown_guard": 20, "evidence_quality": 62, "margin_bridge": 42, "revision_confirmation": 36, "valuation_discipline": 38}, "recommended_shadow_rule_effect": "Stage2 only, with local 4B/high-MAE watch until contract signing and issuer-level margin bridge arrive", "symbol": "064350", "trigger_type": "Stage2"}
{"case_class": "positive", "current_profile_residual": true, "raw_component_score_breakdown": {"backlog_visibility": 84, "drawdown_guard": 86, "evidence_quality": 82, "margin_bridge": 72, "revision_confirmation": 58, "valuation_discipline": 65}, "recommended_shadow_rule_effect": "allow Stage3-Yellow only when direct contract/backlog bridge is present; Green still requires revision/margin confirmation", "symbol": "047810", "trigger_type": "Stage2"}
{"case_class": "counterexample_proxy_low_quality", "current_profile_residual": true, "raw_component_score_breakdown": {"backlog_visibility": 35, "drawdown_guard": 40, "evidence_quality": 48, "margin_bridge": 28, "revision_confirmation": 25, "valuation_discipline": 33}, "recommended_shadow_rule_effect": "block Yellow/Green; route to local 4B watch or hard 4C if no issuer-level bridge appears", "symbol": "103140", "trigger_type": "Stage2"}
{"case_class": "counterexample_high_mae_supplier_proxy", "current_profile_residual": true, "raw_component_score_breakdown": {"backlog_visibility": 55, "drawdown_guard": 20, "evidence_quality": 62, "margin_bridge": 42, "revision_confirmation": 36, "valuation_discipline": 38}, "recommended_shadow_rule_effect": "Stage2 only, with local 4B/high-MAE watch until contract signing and issuer-level margin bridge arrive", "symbol": "003570", "trigger_type": "Stage2"}
{"case_class": "counterexample_theme_proxy", "current_profile_residual": true, "raw_component_score_breakdown": {"backlog_visibility": 35, "drawdown_guard": 40, "evidence_quality": 48, "margin_bridge": 28, "revision_confirmation": 25, "valuation_discipline": 33}, "recommended_shadow_rule_effect": "block Yellow/Green; route to local 4B watch or hard 4C if no issuer-level bridge appears", "symbol": "065450", "trigger_type": "Stage4B-Local"}
```

## 7. Aggregate residual contribution

```json
{
  "selected_round": "R1",
  "selected_loop": 112,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "trigger_row_count": 8,
  "calibration_usable_trigger_count": 8,
  "representative_trigger_count": 8,
  "new_independent_case_count": 8,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 8,
  "same_archetype_new_trigger_family_count": 8,
  "positive_case_count": 4,
  "counterexample_count": 4,
  "stage4b_case_count": 4,
  "stage4c_case_count": 1,
  "current_profile_error_count": 6,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "promotion_blocked_until_url_repair": "true_for_source_proxy_rows",
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 8. Residual finding

C03 needs a sharper split between **prime/direct export backlog** and **supplier-or-theme readthrough**. The direct-contract rows produced clean low-MAE payoff paths: Hanwha Aerospace and LIG Nex1 both had strong MFE with shallow MAE, and Hanwha Systems was still acceptable as a supplier-direct route. But Hyundai Rotem and SNT Dynamics show that even ultimately successful framework/supplier routes can pass through -30% to -39% MAE before payoff. The machine should not score those like clean direct Stage3 evidence.

The failure mode is not “defense export is bad.” It is more precise: **framework headlines and supply-chain sympathy often act like a spring door**. They can open into a real rerating if signed order, financing, delivery schedule, and margin bridge follow; without those, they swing back into local 4B/high-MAE territory.

## 9. Shadow rule candidate

```json
{
  "axis": "C03_direct_export_backlog_bridge_required_before_Yellow_or_Green",
  "scope": "canonical_archetype_id == C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "rule_type": "sector_specific_shadow_rule_candidate",
  "positive_condition": [
    "issuer is named prime contractor or named direct system supplier",
    "signed contract or government-confirmed procurement framework exists",
    "backlog/delivery schedule is visible",
    "margin/revision bridge is at least directionally supported"
  ],
  "watch_condition": [
    "framework negotiation without signed financing/signing visibility",
    "supplier proxy exposure without issuer-level order conversion",
    "defense theme label with MFE potential but MAE90 <= -20%"
  ],
  "stage_effect": "allow Stage3-Yellow only for direct backlog bridge; supplier/framework routes stay Stage2 or local 4B watch until non-price bridge confirms",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "full_4b_requires_non_price_evidence",
    "price_only_blowoff_blocks_positive_stage"
  ],
  "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_when only generic proxy headline is present; use local 4B first unless issuer-level bridge breaks"
}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session. Later coding-agent task:

In stock_agent batch calibration, ingest this MD as a V12 standalone result. Preserve all trigger JSONL rows with complete 30/90/180D MFE/MAE. For C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, evaluate a shadow rule candidate named C03_direct_export_backlog_bridge_required_before_Yellow_or_Green.

Expected implementation behavior:
1. Do not change production scoring directly from this single MD.
2. Add the rows to v12 trigger validation/dedupe flow.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Treat source_proxy_only rows as blocked for promotion until URL repair.
5. Test whether C03 direct prime/direct supplier rows deserve Stage3-Yellow, while framework/supplier/theme proxy rows require local 4B/high-MAE guard until signed order, financing, delivery, and margin bridge are visible.
```

## 11. Completion state

```text
completed_round = R1
completed_loop = 112
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
