# E2R v12 Stock-Web Sector/Archetype Residual Research — R1/L1/C05 Hard 4C Direct Break & Offset Reopen Repair

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
selected_round = R1
selected_loop = 205
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement: margin/working-capital failure, hard 4C timing, direct URL repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Execution scope

This standalone research file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as the execution procedure. It does not open or patch `stock_agent` source code, does not perform live discovery, does not recommend current stocks, and does not change production scoring. The only purpose is to add C05 residual evidence using actual Songdaiki/stock-web 1D OHLCV rows.

The No-Repeat Index is used only as a duplicate ledger and coverage-quality guide. The cumulative ledger has moved past raw row filling: all C01~C32 archetypes have at least 80 representative rows. C05 still needs balance work around margin/working-capital failure, hard 4C transition timing, and offset/reopen logic.

## 2. Stock-Web price-atlas validation

```text
price_atlas_repo = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
active_like_symbol_count = 2,868
inactive_or_delisted_like_symbol_count = 2,546
```

MFE/MAE method: entry close vs max high / min low over inclusive 30/90/180 tradable-row windows. Raw OHLC is unadjusted. If a corporate-action candidate date intersects the entry~D+180 window, the row is blocked from promotion/weight calibration.

## 3. Novelty / duplicate check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This batch avoids the immediately prior C05 keys already used for GS E&C 2023-07/2023-08/2024-02/2024-04/2025-02, Hyundai E&C 2023-06/2024-04/2024-07/2024-10/2025-01, Samsung E&A 2023-04/2024-04/2024-07/2025-01/2025-02, DL E&C 2024-05/2024-08/2024-10/2025-02, Daewoo E&C 2023-02/2024-01/2025-02/2025-04, and HDC 2022-01/2022-05.

```text
new_independent_case_count = 6
new_independent_trigger_count = 6
unique_symbol_count_usable = 2
calibration_usable_trigger_count = 6
narrative_only_blocked_count = 3
stage2_count = 2
stage2_actionable_count = 1
stage4b_count = 1
stage4c_count = 2
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
corporate_action_contaminated_180D_count_for_usable_rows = 0
insufficient_forward_window_180D_count = 0
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 4. Actual entry OHLC rows

| symbol | entry_date | actual stock-web row |
|---|---:|---|
| `006360` | 2023-05-09 | `2023-05-09,21600.0,21800.0,21250.0,21550.0,655556,14149448900,1844281109500,85581490,KOSPI` |
| `006360` | 2023-10-20 | `2023-10-20,13260.0,13470.0,12930.0,13370.0,562200,7416786850,1144224521300,85581490,KOSPI` |
| `294870` | 2022-02-07 | `2022-02-07,16150.0,16500.0,15400.0,15500.0,2247486,35549133000,1021563615000,65907330,KOSPI` |
| `294870` | 2022-03-30 | `2022-03-30,15200.0,17550.0,15150.0,15700.0,6306714,101820639850,1034745081000,65907330,KOSPI` |
| `294870` | 2025-01-31 | `2025-01-31,17160.0,17160.0,16470.0,16600.0,325939,5417011880,1094061678000,65907330,KOSPI` |
| `294870` | 2025-05-26 | `2025-05-26,25750.0,25800.0,23250.0,23550.0,570339,13748928425,1552117621500,65907330,KOSPI` |
| `009410` | 2023-12-28 | `2023-12-28,1940.0,3005.0,1935.0,2315.0,34856588,89005260319,90051411870,38899098,KOSPI` |
| `009410` | 2024-01-08 | `2024-01-08,3275.0,3730.0,3160.0,3195.0,18634887,64095280815,124282618110,38899098,KOSPI` |
| `009410` | 2024-01-12 | `2024-01-12,4000.0,4035.0,3035.0,3050.0,21721692,71523204150,118642248900,38899098,KOSPI` |


## 5. Case matrix — calibration-usable rows

| # | symbol | company | trigger | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak/trough 180D | role |
|---:|---|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | 006360 | GS E&C | Stage4C | 2023-05-09 | 21,550 | 2.78 / -4.64 | 2.78 / -37.96 | 2.78 / -41.21 | 2023-05-24 / 2023-10-10 | direct_quality_failure_early_break |
| 2 | 006360 | GS E&C | Stage4B | 2023-10-20 | 13,370 | 30.14 / -4.41 | 30.14 / -4.41 | 30.14 / -4.41 | 2023-11-23 / 2023-10-24 | management_reset_after_quality_break |
| 3 | 294870 | HDC Hyundai Development | Stage2 | 2022-02-07 | 15,500 | 24.19 / -4.84 | 24.19 / -28.39 | 24.19 / -36.97 | 2022-03-14 / 2022-10-27 | order_headline_false_positive_under_trust_break |
| 4 | 294870 | HDC Hyundai Development | Stage4C | 2022-03-30 | 15,700 | 11.78 / -11.78 | 11.78 / -33.44 | 11.78 / -37.77 | 2022-03-30 / 2022-10-27 | business_license_suspension_direct_break |
| 5 | 294870 | HDC Hyundai Development | Stage2 | 2025-01-31 | 16,600 | 31.02 / -4.4 | 67.77 / -4.4 | 67.77 / -4.4 | 2025-06-12 / 2025-02-03 | recovery_but_margin_quality_cap |
| 6 | 294870 | HDC Hyundai Development | Stage2-Actionable | 2025-05-26 | 23,550 | 18.26 / -8.07 | 18.26 / -18.17 | 18.26 / -22.93 | 2025-06-12 / 2025-11-07 | credit_recovery_positive_control_with_mae_cap |


## 6. Narrative-only / blocked rows

These rows are useful for taxonomy but must not be used for weight promotion because the stock-web profile flags `009410` corporate-action candidate `2024-10-31`, and that date falls inside the entry~180D window.

| # | symbol | company | trigger | entry_date | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | blocked reason |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | 009410 | Taeyoung E&C | Stage4C | 2023-12-28 | 77.54 / -16.41 | 163.93 / -16.41 | 163.93 / -16.41 | corporate-action candidate 2024-10-31 inside 180D window |
| 2 | 009410 | Taeyoung E&C | Stage4B | 2024-01-08 | 28.64 / -31.77 | 91.24 / -31.77 | 91.24 / -35.05 | corporate-action candidate 2024-10-31 inside 180D window |
| 3 | 009410 | Taeyoung E&C | Stage4B | 2024-01-12 | 32.3 / -28.52 | 100.33 / -28.52 | 100.33 / -31.97 | corporate-action candidate 2024-10-31 inside 180D window |


## 7. Case notes

### 7.1 GS E&C / 006360 / 2023-05-09 / Stage4C

This row captures the earlier non-price break before the later formal suspension-order headlines. GS E&C had already admitted faulty construction and missing rebar after the Geomdan parking-lot collapse. The forward path was classic hard-break behavior: 180D MFE only +2.78% versus MAE -41.21%. C05 should not wait for the later administrative penalty if a construction-quality trust break is already issuer-confirmed.

### 7.2 GS E&C / 006360 / 2023-10-20 / Stage4B

The CEO replacement after the quality scandal is not a new bullish bridge by itself, but it changes the 4C state from “fresh thesis break” to “repair/watch.” The forward path gave +30.14% / -4.41% over 180D. The residual is not to erase the quality failure, but to split a hard 4C event from later management-reset offset evidence.

### 7.3 HDC Hyundai Development / 294870 / 2022-02-07 / Stage2

Order, financing, or rebound headlines after a fatal construction-trust break can create false Stage2-Actionable signals. The path had +24.19% MFE but -36.97% MAE over 180D. This is a capped Stage2/watch row: backlog/order language must not override unresolved license, brand, and project-cancellation risk.

### 7.4 HDC Hyundai Development / 294870 / 2022-03-30 / Stage4C

Business suspension and possible license penalties are direct operating-permission damage. The path had +11.78% MFE and -37.77% MAE over 180D. This is a hard 4C positive-control row for C05: confirmed operating-permission break plus weak offset quality should override order/backlog language.

### 7.5 HDC Hyundai Development / 294870 / 2025-01-31 / Stage2

The 2024 performance discussion showed recovery but still weak margin quality. The price path later produced +67.77% MFE with only -4.40% MAE, so the current profile can be too late, but the evidence at entry still lacked enough cash-conversion support for Stage2-Actionable/Yellow. Treat as Stage2 recovery watch.

### 7.6 HDC Hyundai Development / 294870 / 2025-05-26 / Stage2-Actionable

The credit-rating/financial-improvement recognition is a valid reopen bridge after a hard trust-break cycle. However, 180D MAE reached -22.93%, so the correct residual is “Actionable reopen allowed, Green blocked until cash/working-capital conversion.”

### 7.7 Taeyoung E&C / 009410 / blocked taxonomy rows

Taeyoung is the cleanest construction liquidity/PF stress example, but the price series is not clean for weight calibration because `009410` has a corporate-action candidate on 2024-10-31 inside the relevant 180D windows. These rows remain useful as narrative-only C05/C30-adjacent taxonomy: workout filing = hard break, parent liquidity injection/creditor approval = offset/watch, later capital restructuring = price-source contamination.

## 8. Raw component score breakdown

Base component order: `EPS/Visibility/Bottleneck/Mispricing/Valuation/Capital/Info`.

| case type | EPS | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| direct construction-quality admission | 4 | 4 | 2 | 6 | 3 | 2 | 24 | hard 4C should not wait for price confirmation |
| management reset after break | 6 | 7 | 3 | 8 | 4 | 5 | 18 | local 4B/watch; split from hard break |
| order headline under unresolved trust break | 6 | 5 | 3 | 8 | 4 | 4 | 16 | Stage2 cap; Actionable blocked |
| operating-permission/business suspension | 4 | 4 | 2 | 6 | 2 | 2 | 27 | hard 4C direct proof |
| recovery without cash conversion | 9 | 11 | 5 | 10 | 8 | 6 | 13 | Stage2 watch; no Yellow/Green |
| credit recovery after trust-break cycle | 11 | 14 | 6 | 10 | 8 | 8 | 16 | Stage2-Actionable reopen, Green blocked by MAE/cash gap |

## 9. Residual contribution summary

```text
rule_candidate = C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_GATE_V3
sector_rule_candidate = L1_CONSTRUCTION_QUALITY_TRUST_BREAK_AND_REOPEN_GATE
production_scoring_changed = false
shadow_weight_only = true
```

Core residual:

1. Construction-quality admission, fatal safety failure, operating-permission suspension, license cancellation risk, or confirmed liquidity workout are direct non-price thesis-break evidence.
2. Hard 4C should not wait for price collapse when the issuer itself or regulator confirms the break.
3. Order/backlog/financing headlines after a trust break stay capped at Stage2/watch until legal, license, brand, and cash-conversion damage is resolved.
4. Management replacement, parent liquidity injection, creditor approval, or court injunction can move hard-break rows to Stage4B/watch, but not to Stage2-Actionable unless operating margin/cash bridge appears.
5. A later credit-rating or financial-improvement bridge can reopen Stage2-Actionable, but high MAE or missing working-capital/FCF conversion blocks Yellow/Green.
6. Corporate-action-contaminated construction workouts should be left as narrative-only taxonomy unless a clean 180D stock-web window exists.

## 10. Shadow rule proposal

This is not a production patch. It is a batch-handoff candidate only.

```yaml
shadow_rule_candidate:
  id: C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_GATE_V3
  scope:
    large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
    canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  hard_4c_when:
    any_confirmed_direct_break:
      - issuer_admits_construction_quality_failure
      - regulator_seeks_or_imposes_business_suspension
      - license_cancellation_or_operating_permission_risk
      - debt_workout_or_liquidity_failure_without_clean_offset
      - project_rebuild_cost_or_compensation_obligation
  cap_positive_stage_when:
    - order_or_backlog_headline_after_trust_break
    - financing_or_parent_support_without_cash_conversion
    - management_change_without_margin_recovery
    - corporate_action_contaminated_forward_window
  reopen_to_stage2_actionable_when:
    required_second_bridge:
      - credit_rating_or_financial_improvement
      - verified_margin_recovery
      - clean working_capital_or_cash_conversion
      - order/backlog quality converted to operating profit
  stage_effect:
    hard_4c_can_precede_price_confirmation: true
    stage2_actionable_requires_second_bridge_after_trust_break: true
    stage3_yellow_requires_margin_plus_cash_bridge: true
    stage3_green_blocked_if_180d_mae_below_minus_20_without_fcf: true
  suggested_shadow_delta:
    information_confidence: +0.4 when direct quality/license/liquidity break is confirmed
    capital_allocation: -0.3 when support is financing-only without cash conversion
    earnings_visibility: +0.3 when credit/margin/cash bridge reopens the thesis
```

## 11. Machine-readable JSONL trigger rows

```jsonl
{"schema_version":"e2r_v12_trigger_row_v1","row_id":"R1_L205_C05_01_006360_2023-05-09_Stage4C","source_row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"round":"R1","loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"006360","company":"GS E&C","market":"KOSPI","trigger_type":"Stage4C","entry_date":"2023-05-09","entry_price":21550.0,"actual_1d_ohlcv":{"d":"2023-05-09","o":21600.0,"h":21800.0,"l":21250.0,"c":21550.0,"v":655556,"a":14149448900.0,"mc":1844281109500.0,"s":85581490,"m":"KOSPI"},"case_role":"direct_quality_failure_early_break","evidence_family":"construction_quality_admission_missing_rebar","evidence_summary":"GS E&C admitted/apologized for faulty construction at the Geomdan parking-lot collapse, including missing rebar and site inspections; this is direct non-price trust-break evidence before the later suspension-order cycle.","source_url":"https://www.koreatimes.co.kr/business/companies/20230509/gs-ec-admits-to-faulty-construction-of-apartment-underground-parking-lot-in-incheon","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","profile_corporate_action_candidate_dates":["1999-05-07","1999-12-01","2014-06-25"],"corporate_action_overlap_180D":[],"corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":2.78,"mae_30d_pct":-4.64,"mfe_90d_pct":2.78,"mae_90d_pct":-37.96,"mfe_180d_pct":2.78,"mae_180d_pct":-41.21,"peak_180d_date":"2023-05-24","peak_180d_price":22150.0,"trough_180d_date":"2023-10-10","trough_180d_price":12670.0,"end_180d_date":"2024-01-30"},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_breakdown":{"eps_fcf_explosion":4,"earnings_visibility":4,"bottleneck_pricing":2,"market_mispricing":6,"valuation_rerating":3,"capital_allocation":2,"information_confidence":24},"score_total":45,"score_revision":15,"current_profile_error":"hard_4c_too_late_if_waiting_for_formal_suspension","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C05_hard_4c_direct_break_and_offset_reopen_repair","production_scoring_changed":false,"shadow_weight_only":true,"representative_for_aggregate":true,"new_independent_trigger":true},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4C|2023-05-09"}
{"schema_version":"e2r_v12_trigger_row_v1","row_id":"R1_L205_C05_02_006360_2023-10-20_Stage4B","source_row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"round":"R1","loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"006360","company":"GS E&C","market":"KOSPI","trigger_type":"Stage4B","entry_date":"2023-10-20","entry_price":13370.0,"actual_1d_ohlcv":{"d":"2023-10-20","o":13260.0,"h":13470.0,"l":12930.0,"c":13370.0,"v":562200,"a":7416786850.0,"mc":1144224521300.0,"s":85581490,"m":"KOSPI"},"case_role":"management_reset_after_quality_break","evidence_family":"ceo_change_brand_repair_after_quality_failure","evidence_summary":"GS E&C replaced its long-serving CEO with the controlling family successor after the collapse; this is non-price 4B/watch evidence, not a clean hard 4C continuation once rebuild/compensation/legal contest offsets are visible.","source_url":"https://www.koreatimes.co.kr/business/companies/20231020/gs-ec-replaces-ceo-with-owners-son","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","profile_corporate_action_candidate_dates":["1999-05-07","1999-12-01","2014-06-25"],"corporate_action_overlap_180D":[],"corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":30.14,"mae_30d_pct":-4.41,"mfe_90d_pct":30.14,"mae_90d_pct":-4.41,"mfe_180d_pct":30.14,"mae_180d_pct":-4.41,"peak_180d_date":"2023-11-23","peak_180d_price":17400.0,"trough_180d_date":"2023-10-24","trough_180d_price":12780.0,"end_180d_date":"2024-07-12"},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":7,"bottleneck_pricing":3,"market_mispricing":8,"valuation_rerating":4,"capital_allocation":5,"information_confidence":18},"score_total":51,"score_revision":22,"current_profile_error":"overhard_4c_if_management_reset_is_not_split_from_operating_break","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C05_hard_4c_direct_break_and_offset_reopen_repair","production_scoring_changed":false,"shadow_weight_only":true,"representative_for_aggregate":true,"new_independent_trigger":true},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4B|2023-10-20"}
{"schema_version":"e2r_v12_trigger_row_v1","row_id":"R1_L205_C05_03_294870_2022-02-07_Stage2","source_row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"round":"R1","loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"294870","company":"HDC Hyundai Development","market":"KOSPI","trigger_type":"Stage2","entry_date":"2022-02-07","entry_price":15500.0,"actual_1d_ohlcv":{"d":"2022-02-07","o":16150.0,"h":16500.0,"l":15400.0,"c":15500.0,"v":2247486,"a":35549133000.0,"mc":1021563615000.0,"s":65907330,"m":"KOSPI"},"case_role":"order_headline_false_positive_under_trust_break","evidence_family":"order_or_financing_headline_after_fatal_collapse","evidence_summary":"A post-collapse order/financing rebound headline appeared while brand trust, project cancellation, and license risk remained unresolved; the forward path shows why order language after a trust break should stay capped at Stage2/watch.","source_url":"https://www.asiae.co.kr/en/print.htm?idxno=2022020711253835522","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","profile_corporate_action_candidate_dates":["2020-03-26"],"corporate_action_overlap_180D":[],"corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":24.19,"mae_30d_pct":-4.84,"mfe_90d_pct":24.19,"mae_90d_pct":-28.39,"mfe_180d_pct":24.19,"mae_180d_pct":-36.97,"peak_180d_date":"2022-03-14","peak_180d_price":19250.0,"trough_180d_date":"2022-10-27","trough_180d_price":9770.0,"end_180d_date":"2022-10-28"},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":5,"bottleneck_pricing":3,"market_mispricing":8,"valuation_rerating":4,"capital_allocation":4,"information_confidence":16},"score_total":52,"score_revision":20,"current_profile_error":"stage2_false_positive_if_order_headline_ignores_trust_break","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C05_hard_4c_direct_break_and_offset_reopen_repair","production_scoring_changed":false,"shadow_weight_only":true,"representative_for_aggregate":true,"new_independent_trigger":true},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage2|2022-02-07"}
{"schema_version":"e2r_v12_trigger_row_v1","row_id":"R1_L205_C05_04_294870_2022-03-30_Stage4C","source_row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"round":"R1","loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"294870","company":"HDC Hyundai Development","market":"KOSPI","trigger_type":"Stage4C","entry_date":"2022-03-30","entry_price":15700.0,"actual_1d_ohlcv":{"d":"2022-03-30","o":15200.0,"h":17550.0,"l":15150.0,"c":15700.0,"v":6306714,"a":101820639850.0,"mc":1034745081000.0,"s":65907330,"m":"KOSPI"},"case_role":"business_license_suspension_direct_break","evidence_family":"operating_permission_break_business_suspension","evidence_summary":"Seoul imposed an eight-month business suspension after the Gwangju collapse and the company also faced potential additional license penalties; direct operating-permission damage supports hard 4C rather than mere 4B.","source_url":"https://koreajoongangdaily.joins.com/2022/03/30/business/industry/HDC-Building-collapse-Gwangju/20220330162503613.html","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","profile_corporate_action_candidate_dates":["2020-03-26"],"corporate_action_overlap_180D":[],"corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":11.78,"mae_30d_pct":-11.78,"mfe_90d_pct":11.78,"mae_90d_pct":-33.44,"mfe_180d_pct":11.78,"mae_180d_pct":-37.77,"peak_180d_date":"2022-03-30","peak_180d_price":17550.0,"trough_180d_date":"2022-10-27","trough_180d_price":9770.0,"end_180d_date":"2022-12-16"},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_breakdown":{"eps_fcf_explosion":4,"earnings_visibility":4,"bottleneck_pricing":2,"market_mispricing":6,"valuation_rerating":2,"capital_allocation":2,"information_confidence":27},"score_total":47,"score_revision":12,"current_profile_error":"confirmed_hard_4c_should_not_be_delayed_until_price_confirmation","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C05_hard_4c_direct_break_and_offset_reopen_repair","production_scoring_changed":false,"shadow_weight_only":true,"representative_for_aggregate":true,"new_independent_trigger":true},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage4C|2022-03-30"}
{"schema_version":"e2r_v12_trigger_row_v1","row_id":"R1_L205_C05_05_294870_2025-01-31_Stage2","source_row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"round":"R1","loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"294870","company":"HDC Hyundai Development","market":"KOSPI","trigger_type":"Stage2","entry_date":"2025-01-31","entry_price":16600.0,"actual_1d_ohlcv":{"d":"2025-01-31","o":17160.0,"h":17160.0,"l":16470.0,"c":16600.0,"v":325939,"a":5417011880.0,"mc":1094061678000.0,"s":65907330,"m":"KOSPI"},"case_role":"recovery_but_margin_quality_cap","evidence_family":"annual_profit_slowdown_minimized_loss_recovery_watch","evidence_summary":"2024 annual sales were up but operating profit was down; the recovery narrative was present, yet the margin bridge was still not strong enough for Actionable/Yellow despite a strong later price path.","source_url":"https://en.topdaily.kr/articles/4498","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2025.csv","profile_path":"atlas/symbol_profiles/294/294870.json","profile_corporate_action_candidate_dates":["2020-03-26"],"corporate_action_overlap_180D":[],"corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":31.02,"mae_30d_pct":-4.4,"mfe_90d_pct":67.77,"mae_90d_pct":-4.4,"mfe_180d_pct":67.77,"mae_180d_pct":-4.4,"peak_180d_date":"2025-06-12","peak_180d_price":27850.0,"trough_180d_date":"2025-02-03","trough_180d_price":15870.0,"end_180d_date":"2025-10-27"},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_breakdown":{"eps_fcf_explosion":9,"earnings_visibility":11,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":6,"information_confidence":13},"score_total":62,"score_revision":32,"current_profile_error":"too_late_price_path_but_correct_stage2_cap_without_margin_cash_bridge","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C05_hard_4c_direct_break_and_offset_reopen_repair","production_scoring_changed":false,"shadow_weight_only":true,"representative_for_aggregate":true,"new_independent_trigger":true},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage2|2025-01-31"}
{"schema_version":"e2r_v12_trigger_row_v1","row_id":"R1_L205_C05_06_294870_2025-05-26_Stage2_Actionable","source_row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"round":"R1","loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"294870","company":"HDC Hyundai Development","market":"KOSPI","trigger_type":"Stage2-Actionable","entry_date":"2025-05-26","entry_price":23550.0,"actual_1d_ohlcv":{"d":"2025-05-26","o":25750.0,"h":25800.0,"l":23250.0,"c":23550.0,"v":570339,"a":13748928425.0,"mc":1552117621500.0,"s":65907330,"m":"KOSPI"},"case_role":"credit_recovery_positive_control_with_mae_cap","evidence_family":"credit_rating_financial_improvement_recovery","evidence_summary":"HDC Hyundai Development received a credit-rating boost / financial-improvement recognition after rebuilding operating stability, but the post-entry MAE still argues against Yellow/Green without cash-conversion proof.","source_url":"https://biz.chosun.com/en/en-realestate/2025/05/26/4XWZSHVIIND6HO5MXQE5SYR43E/","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2025.csv","profile_path":"atlas/symbol_profiles/294/294870.json","profile_corporate_action_candidate_dates":["2020-03-26"],"corporate_action_overlap_180D":[],"corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":18.26,"mae_30d_pct":-8.07,"mfe_90d_pct":18.26,"mae_90d_pct":-18.17,"mfe_180d_pct":18.26,"mae_180d_pct":-22.93,"peak_180d_date":"2025-06-12","peak_180d_price":27850.0,"trough_180d_date":"2025-11-07","trough_180d_price":18150.0,"end_180d_date":"2026-02-19"},"score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_breakdown":{"eps_fcf_explosion":11,"earnings_visibility":14,"bottleneck_pricing":6,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":8,"information_confidence":16},"score_total":73,"score_revision":45,"current_profile_error":"actionable_reopen_allowed_but_green_blocked_by_mae_and_cashflow_gap","stage3_green_blocked":true,"production_scoring_changed":false,"shadow_weight_only":true},"residual_contribution":{"label":"C05_hard_4c_direct_break_and_offset_reopen_repair","production_scoring_changed":false,"shadow_weight_only":true,"representative_for_aggregate":true,"new_independent_trigger":true},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage2-Actionable|2025-05-26"}
```

## 12. Narrative-only / blocked JSONL rows

```jsonl
{"schema_version":"e2r_v12_narrative_only_v1","source_row_type":"narrative_only_blocked","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"009410","company":"Taeyoung E&C","trigger_type":"Stage4C","entry_date":"2023-12-28","entry_price":2315.0,"actual_1d_ohlcv":{"d":"2023-12-28","o":1940.0,"h":3005.0,"l":1935.0,"c":2315.0,"v":34856588,"a":89005260319.0,"mc":90051411870.0,"s":38899098,"m":"KOSPI"},"case_role":"liquidity_workout_direct_break_but_corporate_action_contaminated","evidence_family":"debt_workout_liquidity_crunch_pf_exposure","evidence_summary":"Taeyoung E&C filed for debt workout due to liquidity stress and PF exposure; as a construction-sector hard break it is useful taxonomy, but the 180D price window crosses a 2024-10-31 corporate-action candidate.","source_url":"https://www.reuters.com/markets/asia/south-korea-moves-reassure-markets-builder-seeks-restructure-debt-2023-12-28/","mfe_30d_pct":77.54,"mae_30d_pct":-16.41,"mfe_90d_pct":163.93,"mae_90d_pct":-16.41,"mfe_180d_pct":163.93,"mae_180d_pct":-16.41,"peak_180d_date":"2024-10-31","trough_180d_date":"2023-12-28","end_180d_date":"2025-05-15","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv","profile_path":"atlas/symbol_profiles/009/009410.json","profile_corporate_action_candidate_dates":["2007-05-03","2020-09-22","2024-10-31"],"corporate_action_overlap_180D":["2024-10-31"],"corporate_action_contamination_180D":true,"insufficient_forward_window_180D":false,"calibration_usable":false,"blocked_reason":"corporate_action_contaminated_180D_window"},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|009410|Stage4C|2023-12-28"}
{"schema_version":"e2r_v12_narrative_only_v1","source_row_type":"narrative_only_blocked","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"009410","company":"Taeyoung E&C","trigger_type":"Stage4B","entry_date":"2024-01-08","entry_price":3195.0,"actual_1d_ohlcv":{"d":"2024-01-08","o":3275.0,"h":3730.0,"l":3160.0,"c":3195.0,"v":18634887,"a":64095280815.0,"mc":124282618110.0,"s":38899098,"m":"KOSPI"},"case_role":"self_rescue_offset_but_corporate_action_contaminated","evidence_family":"self_rescue_liquidity_injection_offset","evidence_summary":"Parent/self-rescue liquidity support created an offset bridge after the workout filing; the row is useful for 4B offset taxonomy but not promotion-usable due to the same 180D corporate-action contamination.","source_url":"https://koreajoongangdaily.joins.com/news/2024-01-08/business/industry/Taeyoung-Group-to-stick-to-original-debt-restructuring-plans-for-EC/1953226","mfe_30d_pct":28.64,"mae_30d_pct":-31.77,"mfe_90d_pct":91.24,"mae_90d_pct":-31.77,"mfe_180d_pct":91.24,"mae_180d_pct":-35.05,"peak_180d_date":"2024-10-31","trough_180d_date":"2025-02-05","end_180d_date":"2025-05-22","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv","profile_path":"atlas/symbol_profiles/009/009410.json","profile_corporate_action_candidate_dates":["2007-05-03","2020-09-22","2024-10-31"],"corporate_action_overlap_180D":["2024-10-31"],"corporate_action_contamination_180D":true,"insufficient_forward_window_180D":false,"calibration_usable":false,"blocked_reason":"corporate_action_contaminated_180D_window"},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|009410|Stage4B|2024-01-08"}
{"schema_version":"e2r_v12_narrative_only_v1","source_row_type":"narrative_only_blocked","research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":205,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_REPAIR_V3","symbol":"009410","company":"Taeyoung E&C","trigger_type":"Stage4B","entry_date":"2024-01-12","entry_price":3050.0,"actual_1d_ohlcv":{"d":"2024-01-12","o":4000.0,"h":4035.0,"l":3035.0,"c":3050.0,"v":21721692,"a":71523204150.0,"mc":118642248900.0,"s":38899098,"m":"KOSPI"},"case_role":"creditor_approval_offset_but_corporate_action_contaminated","evidence_family":"creditor_workout_approval_offset","evidence_summary":"Creditors approved the workout process, creating a survival/restructuring offset; the 180D window still intersects the capital-change candidate and remains blocked from weight calibration.","source_url":"https://www.kedglobal.com/corporate-restructuring/newsView/ked202401120004","mfe_30d_pct":32.3,"mae_30d_pct":-28.52,"mfe_90d_pct":100.33,"mae_90d_pct":-28.52,"mfe_180d_pct":100.33,"mae_180d_pct":-31.97,"peak_180d_date":"2024-10-31","trough_180d_date":"2025-02-05","end_180d_date":"2025-05-28","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009410/2024.csv","profile_path":"atlas/symbol_profiles/009/009410.json","profile_corporate_action_candidate_dates":["2007-05-03","2020-09-22","2024-10-31"],"corporate_action_overlap_180D":["2024-10-31"],"corporate_action_contamination_180D":true,"insufficient_forward_window_180D":false,"calibration_usable":false,"blocked_reason":"corporate_action_contaminated_180D_window"},"duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|009410|Stage4B|2024-01-12"}
```

## 13. Batch Ingest Self-Audit

```text
required_filename_regex_match = true
filename_round_matches_metadata = true
filename_loop_matches_metadata = true
selected_round = R1
selected_loop = 205
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
round_sector_consistency = pass
main_prompt_followed = true
no_repeat_index_used_as_duplicate_ledger_only = true
stock_agent_code_opened = false
stock_agent_code_patched = false
production_scoring_changed = false
shadow_weight_only = true
live_candidate_scan_performed = false
auto_trading_or_brokerage_api_used = false
actual_stock_web_1D_OHLCV_used = true
actual_entry_ohlcv_in_every_usable_trigger = true
complete_30_90_180_mfe_mae_in_every_usable_trigger = true
calibration_usable_trigger_count = 6
narrative_only_blocked_count = 3
missing_entry_price_count = 0
missing_entry_date_count = 0
missing_required_mfe_mae_count = 0
corporate_action_contaminated_180D_count_for_usable_rows = 0
corporate_action_contaminated_180D_count_for_blocked_rows = 3
insufficient_forward_window_180D_count = 0
source_proxy_only_count = 0
evidence_url_pending_count = 0
```

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research generation.

When batch-applying v12 research artifacts, ingest this MD as a standard v12 result file.
Parse all usable trigger JSONL rows under C05_EPC_MEGA_CONTRACT_MARGIN_GAP.
Keep the 009410 Taeyoung rows as narrative-only / blocked because stock-web profile flags corporate_action_candidate_dates=[2024-10-31] inside the 180D windows.
Evaluate C05_HARD_4C_DIRECT_BREAK_AND_OFFSET_REOPEN_GATE_V3 only as a scope-limited C05/L1 shadow candidate.
Do not loosen global Stage3-Green thresholds.
Do not treat order/backlog/financing headlines after construction trust-breaks as Actionable without legal/license/cash conversion repair.
Do allow Stage2-Actionable reopen after a hard-break cycle only when credit/margin/cash bridge appears, and keep Green blocked when 180D MAE is deep or FCF is missing.
```

## 15. Next Research State

```text
completed_round = R1
completed_loop = 205
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement: C05 margin/working-capital failure and hard 4C timing
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
