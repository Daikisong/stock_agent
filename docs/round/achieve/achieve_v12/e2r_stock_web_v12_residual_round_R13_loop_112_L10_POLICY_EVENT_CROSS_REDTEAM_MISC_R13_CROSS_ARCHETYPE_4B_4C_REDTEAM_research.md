# E2R Stock-Web v12 Residual Research — R13 / 4B·4C timing red-team / loop 112

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R13
selected_loop: 112
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112
output_file: e2r_stock_web_v12_residual_round_R13_loop_112_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: R13 cross-archetype 4B/4C URL-verified holdout after session-adjusted Priority-0/Priority-1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection / novelty note

This run is not a fresh Cxx sector-positive search. It is an R13 cross-archetype red-team pass using URL-verified source-sector rows that had not been consumed by the local `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` ledger for the same `symbol + entry_date` at selection time. The No-Repeat Index is used only as the duplicate/coverage ledger; source-sector evidence is replayed with `do_not_count_as_new_sector_case=true` and `independent_evidence_weight=0.25`.

The residual question is narrow: when should deep MAE after valid evidence be treated as local Stage4B timing risk, and when should it escalate to hard Stage4C thesis break? This holdout is deliberately 4B-heavy: none of the selected URL-verified rows has confirmed non-price thesis destruction, so the output strengthens **local 4B timing** rather than broadening hard 4C.

Hard duplicate key checked conceptually:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM + symbol + trigger_type + entry_date
```

## 2. Stock-Web price atlas confirmation

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: [KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI]
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_path: atlas/schema.json
```

MFE/MAE fields are inherited from the source-sector rows that used actual Stock-Web 1D OHLCV shards. Formula: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

## 3. R13 thesis summary

4B and 4C are not the same brake. These rows had real event, contract, technology, IP, platform, order, or policy evidence, but the second bridge did not harden fast enough. The correct response is not to declare every case dead; it is to require a local Stage4B overlay until delivery, revenue recognition, utilization, retention, cash collection, or margin bridge appears.

```text
valid source-sector evidence
  -> no confirmed thesis break
  -> deep MAE90 / MAE180 or peak drawdown
  -> Stage4B-LocalWatch, not hard Stage4C
```

## 4. Case narratives

### 222800 심텍 — positive_with_guardrail

- source canonical: `C06_HBM_MEMORY_CUSTOMER_CAPACITY` / source large sector: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- trigger: `2024-03-12` -> entry `2024-03-12` / source trigger type `Stage4B-LocalWatch`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://www.insightkorea.co.kr/news/articleView.html?idxno=130797
- price path: entry close 28750.0; MFE90 29.5652% / MAE90 -3.6522% ; MFE180 29.5652% / MAE180 -63.0261% ; peak 2024-06-20 / 37250.0; post-peak drawdown -71.4631% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 011070 LG이노텍 — counterexample_4B_timing

- source canonical: `C06_HBM_MEMORY_CUSTOMER_CAPACITY` / source large sector: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- trigger: `2024-08-09` -> entry `2024-08-12` / source trigger type `Stage4B-LocalWatch`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://www.thelec.kr/news/articleView.html?idxno=29542
- price path: entry close 250500.0; MFE90 12.3752% / MAE90 -39.1218% ; MFE180 12.3752% / MAE180 -51.6966% ; peak 2024-09-02 / 281500.0; post-peak drawdown -57.016% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 006340 대원전선 — positive_with_guardrail

- source canonical: `C02_POWER_GRID_DATACENTER_CAPEX` / source large sector: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- trigger: `2024-05-22` -> entry `2024-05-22` / source trigger type `Stage2-Watch`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://www.komachine.com/en/companies/daewon-cable
- price path: entry close 3295.0; MFE90 54.78% / MAE90 -37.48% ; MFE180 58.12% / MAE180 -48.86% ; peak None / None; post-peak drawdown None% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 035900 JYP Ent. — counterexample_4B_timing

- source canonical: `C27_CONTENT_IP_GLOBAL_MONETIZATION` / source large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- trigger: `2023-06-09` -> entry `2023-06-09` / source trigger type `Stage4B-LocalWatch`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://en.yna.co.kr/view/AEN20230609001200315
- price path: entry close 131200.0; MFE90 11.7378% / MAE90 -23.9329% ; MFE180 11.7378% / MAE180 -45.122% ; peak 2023-07-25 / 146600.0; post-peak drawdown -50.8868% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 225570 넥슨게임즈 — counterexample_4B_timing

- source canonical: `C27_CONTENT_IP_GLOBAL_MONETIZATION` / source large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- trigger: `2023-08-03` -> entry `2023-08-03` / source trigger type `Stage4B-LocalWatch`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://www.asiae.co.kr/en/article/2023080313542087577
- price path: entry close 22100.0; MFE90 2.9412% / MAE90 -36.6063% ; MFE180 2.9412% / MAE180 -43.1222% ; peak 2023-08-03 / 22750.0; post-peak drawdown -44.7473% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 026150 특수건설 — positive_with_guardrail

- source canonical: `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` / source large sector: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- trigger: `2024-06-28` -> entry `2024-06-28` / source trigger type `Stage4B-LocalWatch`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240628000898&langTpCd=0&method=search&orgid=K&rcpno=20240628000898&tran=Y
- price path: entry close 7640.0; MFE90 18.05% / MAE90 -24.77% ; MFE180 30.42% / MAE180 -38.9% ; peak 2024-10-07 / None; post-peak drawdown -53.2% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 051910 LG화학 — positive_with_guardrail

- source canonical: `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` / source large sector: `L4_MATERIALS_SPREAD_RESOURCE`
- trigger: `2024-01-31` -> entry `2024-02-01` / source trigger type `Stage4B`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://securities.miraeasset.com/bbs/download/2121597.pdf?attachmentId=2121597
- price path: entry close 430000.0; MFE90 20.9302% / MAE90 -18.6047% ; MFE180 20.9302% / MAE180 -38.7209% ; peak None / None; post-peak drawdown None% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 033100 제룡전기 — positive_with_guardrail

- source canonical: `C02_POWER_GRID_DATACENTER_CAPEX` / source large sector: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- trigger: `2024-03-08` -> entry `2024-03-08` / source trigger type `Stage3-Yellow`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://ssl.pstatic.net/imgstock/upload/research/company/1709852777300.pdf
- price path: entry close 51500.0; MFE90 126.21% / MAE90 -4.85% ; MFE180 128.93% / MAE180 -37.86% ; peak None / None; post-peak drawdown None% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 036930 주성엔지니어링 — counterexample_4B_timing

- source canonical: `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` / source large sector: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- trigger: `2024-04-02` -> entry `2024-04-03` / source trigger type `Stage2-Actionable`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://ssl.pstatic.net/imgstock/upload/research/company/1712019166097.pdf
- price path: entry close 35300.0; MFE90 17.42% / MAE90 -37.25% ; MFE180 17.42% / MAE180 -37.54% ; peak 2024-04-08 / 41450.0; post-peak drawdown -46.8% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

### 307950 현대오토에버 — counterexample_4B_timing

- source canonical: `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` / source large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- trigger: `2024-07-26` -> entry `2024-07-26` / source trigger type `Stage2-Actionable`
- evidence family: URL-verified source-sector evidence with missing or delayed second bridge
- source: https://www.mk.co.kr/en/it/11077963
- price path: entry close 166500.0; MFE90 3.54% / MAE90 -26.13% ; MFE180 3.54% / MAE180 -35.74% ; peak 2024-07-30 / 172400.0; post-peak drawdown -37.94% .
- R13 implication: evidence was real, but the absence of a second bridge means this should remain local Stage4B timing risk instead of hard 4C thesis break.

## 5. Backtest result table

| symbol | name | source canonical | entry | source trigger | R13 overlay | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak/date | post-peak DD |
|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 222800 | 심텍 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 2024-03-12 | Stage4B-LocalWatch | Stage4B-LocalWatch | 28750.0 | 19.8261 | -3.6522 | 29.5652 | -3.6522 | 29.5652 | -63.0261 | 2024-06-20 / 37250.0 | -71.4631 |
| 011070 | LG이노텍 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 2024-08-12 | Stage4B-LocalWatch | Stage4B-LocalWatch | 250500.0 | 12.3752 | -12.3752 | 12.3752 | -39.1218 | 12.3752 | -51.6966 | 2024-09-02 / 281500.0 | -57.016 |
| 006340 | 대원전선 | C02_POWER_GRID_DATACENTER_CAPEX | 2024-05-22 | Stage2-Watch | Stage4B-LocalWatch | 3295.0 | 37.48 | -12.44 | 54.78 | -37.48 | 58.12 | -48.86 | None / None | None |
| 035900 | JYP Ent. | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2023-06-09 | Stage4B-LocalWatch | Stage4B-LocalWatch | 131200.0 | 7.1646 | -6.7835 | 11.7378 | -23.9329 | 11.7378 | -45.122 | 2023-07-25 / 146600.0 | -50.8868 |
| 225570 | 넥슨게임즈 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2023-08-03 | Stage4B-LocalWatch | Stage4B-LocalWatch | 22100.0 | 2.9412 | -30.4072 | 2.9412 | -36.6063 | 2.9412 | -43.1222 | 2023-08-03 / 22750.0 | -44.7473 |
| 026150 | 특수건설 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 2024-06-28 | Stage4B-LocalWatch | Stage4B-LocalWatch | 7640.0 | 6.23 | -17.84 | 18.05 | -24.77 | 30.42 | -38.9 | 2024-10-07 / None | -53.2 |
| 051910 | LG화학 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 2024-02-01 | Stage4B | Stage4B-LocalWatch | 430000.0 | 20.9302 | -3.0233 | 20.9302 | -18.6047 | 20.9302 | -38.7209 | None / None | None |
| 033100 | 제룡전기 | C02_POWER_GRID_DATACENTER_CAPEX | 2024-03-08 | Stage3-Yellow | Stage4B-LocalWatch | 51500.0 | 65.44 | -4.85 | 126.21 | -4.85 | 128.93 | -37.86 | None / None | None |
| 036930 | 주성엔지니어링 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 2024-04-03 | Stage2-Actionable | Stage4B-LocalWatch | 35300.0 | 17.42 | -10.34 | 17.42 | -37.25 | 17.42 | -37.54 | 2024-04-08 / 41450.0 | -46.8 |
| 307950 | 현대오토에버 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 2024-07-26 | Stage2-Actionable | Stage4B-LocalWatch | 166500.0 | 3.54 | -16.1 | 3.54 | -26.13 | 3.54 | -35.74 | 2024-07-30 / 172400.0 | -37.94 |

## 6. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": "R2", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "symbol": "222800", "name": "심텍", "trigger_date": "2024-03-12", "entry_date": "2024-03-12", "entry_price": 28750.0, "source_trigger_type": "Stage4B-LocalWatch", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://www.insightkorea.co.kr/news/articleView.html?idxno=130797", "MFE_30D_pct": 19.8261, "MAE_30D_pct": -3.6522, "MFE_90D_pct": 29.5652, "MAE_90D_pct": -3.6522, "MFE_180D_pct": 29.5652, "MAE_180D_pct": -63.0261, "peak_date": "2024-06-20", "peak_price": 37250.0, "drawdown_after_peak_pct": -71.4631, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": "R2", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_111_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "symbol": "011070", "name": "LG이노텍", "trigger_date": "2024-08-09", "entry_date": "2024-08-12", "entry_price": 250500.0, "source_trigger_type": "Stage4B-LocalWatch", "trigger_type": "Stage4B", "classification": "counterexample_4B_timing", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://www.thelec.kr/news/articleView.html?idxno=29542", "MFE_30D_pct": 12.3752, "MAE_30D_pct": -12.3752, "MFE_90D_pct": 12.3752, "MAE_90D_pct": -39.1218, "MFE_180D_pct": 12.3752, "MAE_180D_pct": -51.6966, "peak_date": "2024-09-02", "peak_price": 281500.0, "drawdown_after_peak_pct": -57.016, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": null, "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_143_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "symbol": "006340", "name": "대원전선", "trigger_date": "2024-05-22", "entry_date": "2024-05-22", "entry_price": 3295.0, "source_trigger_type": "Stage2-Watch", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://www.komachine.com/en/companies/daewon-cable", "MFE_30D_pct": 37.48, "MAE_30D_pct": -12.44, "MFE_90D_pct": 54.78, "MAE_90D_pct": -37.48, "MFE_180D_pct": 58.12, "MAE_180D_pct": -48.86, "peak_date": null, "peak_price": null, "drawdown_after_peak_pct": null, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "symbol": "035900", "name": "JYP Ent.", "trigger_date": "2023-06-09", "entry_date": "2023-06-09", "entry_price": 131200.0, "source_trigger_type": "Stage4B-LocalWatch", "trigger_type": "Stage4B", "classification": "counterexample_4B_timing", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://en.yna.co.kr/view/AEN20230609001200315", "MFE_30D_pct": 7.1646, "MAE_30D_pct": -6.7835, "MFE_90D_pct": 11.7378, "MAE_90D_pct": -23.9329, "MFE_180D_pct": 11.7378, "MAE_180D_pct": -45.122, "peak_date": "2023-07-25", "peak_price": 146600.0, "drawdown_after_peak_pct": -50.8868, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "symbol": "225570", "name": "넥슨게임즈", "trigger_date": "2023-08-03", "entry_date": "2023-08-03", "entry_price": 22100.0, "source_trigger_type": "Stage4B-LocalWatch", "trigger_type": "Stage4B", "classification": "counterexample_4B_timing", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://www.asiae.co.kr/en/article/2023080313542087577", "MFE_30D_pct": 2.9412, "MAE_30D_pct": -30.4072, "MFE_90D_pct": 2.9412, "MAE_90D_pct": -36.6063, "MFE_180D_pct": 2.9412, "MAE_180D_pct": -43.1222, "peak_date": "2023-08-03", "peak_price": 22750.0, "drawdown_after_peak_pct": -44.7473, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": null, "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "symbol": "026150", "name": "특수건설", "trigger_date": "2024-06-28", "entry_date": "2024-06-28", "entry_price": 7640.0, "source_trigger_type": "Stage4B-LocalWatch", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240628000898&langTpCd=0&method=search&orgid=K&rcpno=20240628000898&tran=Y", "MFE_30D_pct": 6.23, "MAE_30D_pct": -17.84, "MFE_90D_pct": 18.05, "MAE_90D_pct": -24.77, "MFE_180D_pct": 30.42, "MAE_180D_pct": -38.9, "peak_date": "2024-10-07", "peak_price": null, "drawdown_after_peak_pct": -53.2, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": "R4", "source_large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "source_canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "source_file": "e2r_stock_web_v12_residual_round_R4_loop_142_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md", "symbol": "051910", "name": "LG화학", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 430000.0, "source_trigger_type": "Stage4B", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://securities.miraeasset.com/bbs/download/2121597.pdf?attachmentId=2121597", "MFE_30D_pct": 20.9302, "MAE_30D_pct": -3.0233, "MFE_90D_pct": 20.9302, "MAE_90D_pct": -18.6047, "MFE_180D_pct": 20.9302, "MAE_180D_pct": -38.7209, "peak_date": null, "peak_price": null, "drawdown_after_peak_pct": null, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": null, "source_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "source_file": "e2r_stock_web_v12_residual_round_R1_loop_143_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "symbol": "033100", "name": "제룡전기", "trigger_date": "2024-03-08", "entry_date": "2024-03-08", "entry_price": 51500.0, "source_trigger_type": "Stage3-Yellow", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1709852777300.pdf", "MFE_30D_pct": 65.44, "MAE_30D_pct": -4.85, "MFE_90D_pct": 126.21, "MAE_90D_pct": -4.85, "MFE_180D_pct": 128.93, "MAE_180D_pct": -37.86, "peak_date": null, "peak_price": null, "drawdown_after_peak_pct": null, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": "R2", "source_large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "source_canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "source_file": "e2r_stock_web_v12_residual_round_R2_loop_114_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md", "symbol": "036930", "name": "주성엔지니어링", "trigger_date": "2024-04-02", "entry_date": "2024-04-03", "entry_price": 35300.0, "source_trigger_type": "Stage2-Actionable", "trigger_type": "Stage4B", "classification": "counterexample_4B_timing", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1712019166097.pdf", "MFE_30D_pct": 17.42, "MAE_30D_pct": -10.34, "MFE_90D_pct": 17.42, "MAE_90D_pct": -37.25, "MFE_180D_pct": 17.42, "MAE_180D_pct": -37.54, "peak_date": "2024-04-08", "peak_price": 41450.0, "drawdown_after_peak_pct": -46.8, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "fine_archetype_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_HOLDOUT_V112", "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_101_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "symbol": "307950", "name": "현대오토에버", "trigger_date": "2024-07-26", "entry_date": "2024-07-26", "entry_price": 166500.0, "source_trigger_type": "Stage2-Actionable", "trigger_type": "Stage4B", "classification": "counterexample_4B_timing", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://www.mk.co.kr/en/it/11077963", "MFE_30D_pct": 3.54, "MAE_30D_pct": -16.1, "MFE_90D_pct": 3.54, "MAE_90D_pct": -26.13, "MFE_180D_pct": 3.54, "MAE_180D_pct": -35.74, "peak_date": "2024-07-30", "peak_price": 172400.0, "drawdown_after_peak_pct": -37.94, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
```

## 7. Score simulations / aggregate / residual rows

```jsonl
{"row_type": "score_simulation", "case_id": "R13_V112_222800_20240312_4B_4C_TIMING", "symbol": "222800", "source_canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "current_profile_proxy_score": 49.46, "shadow_rule_score_delta": -8, "shadow_adjusted_score": 41.46, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 37.0, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_011070_20240812_4B_4C_TIMING", "symbol": "011070", "source_canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "current_profile_proxy_score": 48.78, "shadow_rule_score_delta": -8, "shadow_adjusted_score": 40.78, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 48.3, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_006340_20240522_4B_4C_TIMING", "symbol": "006340", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "current_profile_proxy_score": 52.89, "shadow_rule_score_delta": -8, "shadow_adjusted_score": 44.89, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 51.1, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_035900_20230609_4B_4C_TIMING", "symbol": "035900", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "current_profile_proxy_score": 49.53, "shadow_rule_score_delta": -8, "shadow_adjusted_score": 41.53, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 54.9, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_225570_20230803_4B_4C_TIMING", "symbol": "225570", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "current_profile_proxy_score": 48.9, "shadow_rule_score_delta": -8, "shadow_adjusted_score": 40.9, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 56.9, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_026150_20240628_4B_4C_TIMING", "symbol": "026150", "source_canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "current_profile_proxy_score": 52.18, "shadow_rule_score_delta": -6, "shadow_adjusted_score": 46.18, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 61.1, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_051910_20240201_4B_4C_TIMING", "symbol": "051910", "source_canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "current_profile_proxy_score": 51.25, "shadow_rule_score_delta": -6, "shadow_adjusted_score": 45.25, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 61.3, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_033100_20240308_4B_4C_TIMING", "symbol": "033100", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "current_profile_proxy_score": 54.27, "shadow_rule_score_delta": -6, "shadow_adjusted_score": 48.27, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 62.1, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_036930_20240403_4B_4C_TIMING", "symbol": "036930", "source_canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "current_profile_proxy_score": 51.05, "shadow_rule_score_delta": -6, "shadow_adjusted_score": 45.05, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 62.5, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "score_simulation", "case_id": "R13_V112_307950_20240726_4B_4C_TIMING", "symbol": "307950", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "current_profile_proxy_score": 49.89, "shadow_rule_score_delta": -6, "shadow_adjusted_score": 43.89, "shadow_stage_effect": "Stage4B-LocalWatch overlay; do not route to hard 4C without non-price thesis break", "raw_component_score_breakdown": {"non_price_evidence_bridge": 52, "price_path_risk": 64.3, "information_confidence": 58, "thesis_break_confirmation": 15}, "score_return_alignment_note": "alignment improved by separating local 4B timing risk from confirmed 4C thesis break"}
{"row_type": "aggregate", "research_file": "e2r_stock_web_v12_residual_round_R13_loop_112_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md", "selected_round": "R13", "selected_loop": 112, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "trigger_row_count": 10, "calibration_usable_rows": 10, "representative_rows": 10, "unique_symbol_count": 10, "unique_source_canonical_count": 7, "unique_source_large_sector_count": 4, "positive_with_guardrail_count": 5, "counterexample_count": 10, "stage4b_overlay_count": 10, "stage4c_count": 0, "avg_MFE_30D_pct": 19.3347, "avg_MAE_30D_pct": -11.7811, "avg_MFE_90D_pct": 29.755, "avg_MAE_90D_pct": -25.2398, "avg_MFE_180D_pct": 31.598, "avg_MAE_180D_pct": -44.0588, "rows_MAE180_le_minus_30pct": 10, "rows_MAE180_le_minus_40pct": 5, "source_proxy_only_rows": 0, "evidence_url_pending_rows": 0, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "ready_for_batch_ingest": true}
{"row_type": "shadow_weight_candidate", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM", "rule_id": "R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_LOCAL_4B_NOT_HARD_4C_V112", "rule_effect": "When URL-verified source-sector evidence is followed by deep MAE90/MAE180 without a confirmed non-price thesis break, apply Stage4B-LocalWatch and suppress hard 4C routing until delivery/revenue/margin/FCF/utilization/retention/cash bridge failure is explicit.", "proposed_axes": ["local_4b_timing_split", "hard_4c_requires_confirmed_thesis_break", "second_bridge_confirmation_required", "do_not_count_as_new_sector_case_for_r13_replay"], "shadow_only": true}
{"row_type": "residual_contribution", "contribution_label": "r13_4b_4c_timing_url_verified_holdout", "residual_error_found": true, "current_profile_error_count": 10, "main_residual": "Current profile can still blur deep-MAE timing risk and hard thesis break. This pass supports local 4B overlays while resisting hard 4C escalation without non-price thesis destruction.", "suggested_shadow_axis": "R13_local_4B_vs_hard_4C_timing_split"}
```

## 8. Current calibrated profile stress test

The current calibrated profile already contains `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`. The residual error here is the seam between 4B and 4C. A row can be too dangerous to keep as warm Stage2/Stage3 because MAE is deep, but still not broken enough for hard 4C when the thesis has not been explicitly cancelled, rejected, or disproven.

## 9. Shadow rule candidate

```text
R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_LOCAL_4B_NOT_HARD_4C_V112
```

Rule mechanics:

```text
IF source-sector evidence is URL-verified
AND MAE90 or MAE180 breaches the high-MAE guardrail
AND no explicit contract cancellation / regulatory rejection / thesis break / customer call-off is confirmed
THEN apply Stage4B-LocalWatch overlay and require second bridge confirmation before Stage2/Stage3 persistence.
Do not route to hard Stage4C unless the non-price thesis break is explicit.
```

## 10. Validation scope

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
uses_current_session_source_rows_for_r13_reuse: true
do_not_count_as_new_sector_case: true
independent_evidence_weight: 0.25
jsonl_trigger_row_count: 10
calibration_usable_rows: 10
representative_rows: 10
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this during the research run. In the later batch-implementation session, ingest this Markdown with the other V12 research MD files. Treat rows as R13 replay rows, not fresh Cxx sector coverage. Test the shadow rule R13_4B_4C_TIMING_SPLIT_URL_VERIFIED_LOCAL_4B_NOT_HARD_4C_V112 against v12_trigger_rows_representative.jsonl. If accepted, implement only a scope-limited shadow/profile patch that applies local 4B overlay to URL-verified deep-MAE rows lacking second bridge confirmation, while requiring explicit non-price thesis destruction for hard 4C. Do not alter production scoring directly unless the batch promotion decision applies the patch.
```

## 12. Completed research state

```text
completed_round = R13
completed_loop = 112
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = R13 cross-archetype 4B/4C URL-verified timing holdout
next_recommended_archetypes = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path | C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
