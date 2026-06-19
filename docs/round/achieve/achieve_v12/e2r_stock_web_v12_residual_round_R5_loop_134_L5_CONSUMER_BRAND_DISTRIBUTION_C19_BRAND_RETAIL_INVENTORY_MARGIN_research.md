# E2R Stock-Web v12 Residual Research — R5 / C19 Brand Retail Inventory Margin

```yaml
artifact_type: stock_web_v12_sector_archetype_residual_calibration
schema_version: e2r_v12_residual_md_v1
selected_round: R5
selected_loop: 134
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selection_mode: coverage_index_first_quality_repair
selected_priority_bucket: Priority 0/1 quality repair — C19 direct URL/proxy quality, retail inventory-to-margin conversion, discount/clearance 4B-4C split
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE
price_source: Songdaiki/stock-web
primary_price_route: atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
current_live_scan_performed: false
stock_agent_code_accessed: false
stock_agent_code_patch_performed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Execution contract read-back

This run follows the v12 historical calibration prompt as a standalone research MD generation task. It does not perform current/live candidate discovery, brokerage/API work, production scoring changes, or `stock_agent` code access/patching. The No-Repeat Index is used only as the duplicate-avoidance and coverage-quality ledger.

The latest No-Repeat ledger says all C01~C32 canonical scopes have passed the old 30/50/80-row rescue targets. Therefore this run treats C19 as a quality-repair scope: direct source URL mapping, explicit proxy marking, entry hygiene, complete 30D/90D/180D MFE/MAE, and a sharper split between true inventory/margin recovery and stale brand-premium overcredit.

C18 asked whether an overseas channel keeps reordering. C19 asks whether brand demand clears inventory at profitable prices. A channel can be wide while the shelf is clogged; this run is the shelf-and-margin audit.

## 2. No-Repeat and novelty audit

```yaml
recent_session_archetypes_avoided:
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - C11_BATTERY_ORDERBOOK_RERATING
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
selected_archetype_this_run: C19_BRAND_RETAIL_INVENTORY_MARGIN
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 3
counterexample_count: 3
stage4b_case_count: 2
stage4c_case_count: 1
source_proxy_only_count: 6
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 5
```

## 3. Case universe

| case_id | symbol | company | trigger_date | entry_date | trigger_type | evidence family | calibration use | interpretation |
|---|---:|---|---|---|---|---|---|---|
| C19-R5L134-01 | 337930 | Brand X Corporation / 브랜드엑스코퍼레이션 | 2024-05-13 | 2024-05-13 | Stage3-Yellow | xexymix_record_revenue_channel_category_expansion_inventory_clearance_caveat | usable | positive_brand_channel_category_expansion_with_inventory_clearance_caveat |
| C19-R5L134-02 | 036620 | Gamsung Corporation / 감성코퍼레이션 | 2023-11-14 | 2023-11-14 | Stage3-Yellow | snowpeak_apparel_record_q3_revenue_op_repurchase_customer_expansion | usable | positive_brand_sellthrough_margin_but_drawdown_sensitive |
| C19-R5L134-03 | 081660 | FILA Holdings / 휠라홀딩스 | 2024-05-16 | 2024-05-16 | Stage2-Actionable | fila_inventory_assets_decline_loss_narrowing_revenue_recovery_needed | usable | positive_inventory_normalization_watch_not_green |
| C19-R5L134-04 | 383220 | F&F | 2023-07-31 | 2023-07-31 | Stage4B | china_sellthrough_still_solid_domestic_revenue_slowing_brand_premium_deceleration | usable | counterexample_4b_stale_brand_premium_deceleration |
| C19-R5L134-05 | 298540 | The Nature Holdings / 더네이쳐홀딩스 | 2023-10-24 | 2023-10-24 | Stage4C | national_geographic_overseas_story_fixed_cost_margin_and_inventory_burden | usable | counterexample_4c_brand_expansion_margin_inventory_break |
| C19-R5L134-06 | 020000 | Handsome / 한섬 | 2023-11-06 | 2023-11-06 | Stage4B | premium_brand_house_consumption_slowdown_new_brand_investment_margin_drop | usable | counterexample_4b_premium_brand_margin_drag |

## 4. Evidence and source map

| case_id | evidence_url | price_shard_url | source_quality | source_proxy_only |
|---|---|---|---|---|
| C19-R5L134-01 | https://www.yna.co.kr/view/AKR20240513073800030 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv | news_company_disclosure_summary | true |
| C19-R5L134-02 | https://fashionbiz.co.kr/article/203820 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv | industry_news_company_statement | true |
| C19-R5L134-03 | https://securities.miraeasset.com/bbs/download/2127021.pdf?attachmentId=2127021 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv | broker_proxy_with_company_data | true |
| C19-R5L134-04 | https://securities.miraeasset.com/bbs/download/2111568.pdf?attachmentId=2111568 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv | broker_proxy_with_company_data | true |
| C19-R5L134-05 | https://ssl.pstatic.net/imgstock/upload/research/company/1698103636056.pdf | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv | broker_proxy_with_company_data | true |
| C19-R5L134-06 | https://www.yna.co.kr/view/AKR20231106086151527 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/020/020000/2023.csv | news_company_disclosure_summary | true |

### Case evidence notes
- **C19-R5L134-01 / Brand X Corporation / 브랜드엑스코퍼레이션** — Q1 revenue was a quarterly record and XEXYMIX grew, while OP fell due to overseas scale-up and long-term inventory clearance; positive, but Green should require follow-through margin confirmation.
- **C19-R5L134-02 / Gamsung Corporation / 감성코퍼레이션** — Snow Peak Apparel delivered record Q3 revenue and large OP growth; the forward path worked, but the interim MAE says C19 Green needs drawdown-aware confirmation.
- **C19-R5L134-03 / FILA Holdings / 휠라홀딩스** — Inventory assets decline and narrowed losses give a real Stage2 bridge, but revenue recovery is still the missing gear.
- **C19-R5L134-04 / F&F** — China sell-through remained solid, but domestic revenue slowed and the stock suffered a deep 180D MAE after a small local MFE; C19 needs a 4B watch guard.
- **C19-R5L134-05 / The Nature Holdings / 더네이쳐홀딩스** — The overseas Nat Geo story was visible, but the report itself flagged domestic apparel weakness and fixed-cost pressure; forward price path confirms this should be a 4C-style C19 break, not a rerating bridge.
- **C19-R5L134-06 / Handsome / 한섬** — A premium brand house with buyback support still failed to produce meaningful MFE after a 73% OP drop; 4B is right until margin recovery is visible.

## 5. Stock-Web price validation scope

```yaml
price_source: Songdaiki/stock-web
manifest_checked:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  max_date: 2026-02-20
schema_checked:
  tradable_columns: d/o/h/l/c/v/a/mc/s/m
  MFE_N_pct: '(max high from entry_date through N tradable rows / entry_price - 1) * 100'
  MAE_N_pct: '(min low from entry_date through N tradable rows / entry_price - 1) * 100'
  calibration_required_windows: 30D/90D/180D
calibration_basis: tradable_raw
raw_unadjusted_warning: true
corporate_action_policy: block_if_candidate_overlap_entry_to_Dplus180
forward_window_policy: all entry windows are before manifest max_date and have 180 tradable rows
```

## 6. Actual OHLC backtest rows

| case_id | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_180D | trough_180D |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| C19-R5L134-01 | 4950 | 39.39% | 148.08% | 170.30% | -1.11% | -1.11% | -1.11% | 2024-10-07 @ 13380 | 2024-05-13 @ 4895 |
| C19-R5L134-02 | 3415 | 15.67% | 15.67% | 37.34% | -9.52% | -26.50% | -26.50% | 2024-05-24 @ 4690 | 2024-02-14 @ 2510 |
| C19-R5L134-03 | 40350 | 2.48% | 11.40% | 11.40% | -5.70% | -7.31% | -9.79% | 2024-09-25 @ 44950 | 2024-11-07 @ 36400 |
| C19-R5L134-04 | 103500 | 15.36% | 15.94% | 15.94% | -6.18% | -23.57% | -40.97% | 2023-09-19 @ 120000 | 2024-04-16 @ 61100 |
| C19-R5L134-05 | 21250 | 9.65% | 9.65% | 9.65% | -19.58% | -32.80% | -46.07% | 2023-11-06 @ 23300 | 2024-07-03 @ 11460 |
| C19-R5L134-06 | 20050 | 0.75% | 7.98% | 7.98% | -6.33% | -14.36% | -16.46% | 2024-02-07 @ 21650 | 2024-07-25 @ 16750 |

## 7. Machine-readable JSONL rows

### case rows
```jsonl
{"row_type": "case", "case_id": "C19-R5L134-01", "symbol": "337930", "company": "Brand X Corporation / 브랜드엑스코퍼레이션", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2024-05-13", "entry_date": "2024-05-13", "calibration_usable": true, "reuse_status": "new_independent_case", "source_proxy_only": true, "evidence_family": "xexymix_record_revenue_channel_category_expansion_inventory_clearance_caveat"}
{"row_type": "case", "case_id": "C19-R5L134-02", "symbol": "036620", "company": "Gamsung Corporation / 감성코퍼레이션", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2023-11-14", "entry_date": "2023-11-14", "calibration_usable": true, "reuse_status": "new_independent_case", "source_proxy_only": true, "evidence_family": "snowpeak_apparel_record_q3_revenue_op_repurchase_customer_expansion"}
{"row_type": "case", "case_id": "C19-R5L134-03", "symbol": "081660", "company": "FILA Holdings / 휠라홀딩스", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "calibration_usable": true, "reuse_status": "new_independent_case", "source_proxy_only": true, "evidence_family": "fila_inventory_assets_decline_loss_narrowing_revenue_recovery_needed"}
{"row_type": "case", "case_id": "C19-R5L134-04", "symbol": "383220", "company": "F&F", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2023-07-31", "entry_date": "2023-07-31", "calibration_usable": true, "reuse_status": "new_independent_case", "source_proxy_only": true, "evidence_family": "china_sellthrough_still_solid_domestic_revenue_slowing_brand_premium_deceleration"}
{"row_type": "case", "case_id": "C19-R5L134-05", "symbol": "298540", "company": "The Nature Holdings / 더네이쳐홀딩스", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2023-10-24", "entry_date": "2023-10-24", "calibration_usable": true, "reuse_status": "new_independent_case", "source_proxy_only": true, "evidence_family": "national_geographic_overseas_story_fixed_cost_margin_and_inventory_burden"}
{"row_type": "case", "case_id": "C19-R5L134-06", "symbol": "020000", "company": "Handsome / 한섬", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2023-11-06", "entry_date": "2023-11-06", "calibration_usable": true, "reuse_status": "new_independent_case", "source_proxy_only": true, "evidence_family": "premium_brand_house_consumption_slowdown_new_brand_investment_margin_drop"}
```

### trigger rows
```jsonl
{"row_type": "trigger", "case_id": "C19-R5L134-01", "symbol": "337930", "company": "Brand X Corporation / 브랜드엑스코퍼레이션", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2024-05-13", "entry_date": "2024-05-13", "entry_price": 4950, "trigger_type": "Stage3-Yellow", "evidence_family": "xexymix_record_revenue_channel_category_expansion_inventory_clearance_caveat", "source_url": "https://www.yna.co.kr/view/AKR20240513073800030", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/337/337930/2024.csv", "profile_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/337/337930.json", "source_quality": "news_company_disclosure_summary", "source_proxy_only": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 39.39, "MFE_90D_pct": 148.08, "MFE_180D_pct": 170.3, "MAE_30D_pct": -1.11, "MAE_90D_pct": -1.11, "MAE_180D_pct": -1.11, "peak_180D_date": "2024-10-07", "peak_180D_high": 13380, "trough_180D_date": "2024-05-13", "trough_180D_low": 4895, "corporate_action_window_status": "clean_180D_window_assumed_from_profile_or_no_2023_2024_candidate_overlap", "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "337930_2024-05-13_C19_xexymix_record_revenue_channel_category_expansio", "classification": "positive_brand_channel_category_expansion_with_inventory_clearance_caveat", "current_profile_error": "too_conservative_if_inventory_clearance_caveat_blocks_visible_revenue_and_channel_momentum"}
{"row_type": "trigger", "case_id": "C19-R5L134-02", "symbol": "036620", "company": "Gamsung Corporation / 감성코퍼레이션", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2023-11-14", "entry_date": "2023-11-14", "entry_price": 3415, "trigger_type": "Stage3-Yellow", "evidence_family": "snowpeak_apparel_record_q3_revenue_op_repurchase_customer_expansion", "source_url": "https://fashionbiz.co.kr/article/203820", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv", "profile_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/036/036620.json", "source_quality": "industry_news_company_statement", "source_proxy_only": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.67, "MFE_90D_pct": 15.67, "MFE_180D_pct": 37.34, "MAE_30D_pct": -9.52, "MAE_90D_pct": -26.5, "MAE_180D_pct": -26.5, "peak_180D_date": "2024-05-24", "peak_180D_high": 4690, "trough_180D_date": "2024-02-14", "trough_180D_low": 2510, "corporate_action_window_status": "clean_180D_window_assumed_from_profile_or_no_2023_2024_candidate_overlap", "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "036620_2023-11-14_C19_snowpeak_apparel_record_q3_revenue_op_repurchase", "classification": "positive_brand_sellthrough_margin_but_drawdown_sensitive", "current_profile_error": "should_credit_operating_leverage_but_delay_green_until_drawdown_and_inventory_quality_confirmed"}
{"row_type": "trigger", "case_id": "C19-R5L134-03", "symbol": "081660", "company": "FILA Holdings / 휠라홀딩스", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 40350, "trigger_type": "Stage2-Actionable", "evidence_family": "fila_inventory_assets_decline_loss_narrowing_revenue_recovery_needed", "source_url": "https://securities.miraeasset.com/bbs/download/2127021.pdf?attachmentId=2127021", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv", "profile_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/081/081660.json", "source_quality": "broker_proxy_with_company_data", "source_proxy_only": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.48, "MFE_90D_pct": 11.4, "MFE_180D_pct": 11.4, "MAE_30D_pct": -5.7, "MAE_90D_pct": -7.31, "MAE_180D_pct": -9.79, "peak_180D_date": "2024-09-25", "peak_180D_high": 44950, "trough_180D_date": "2024-11-07", "trough_180D_low": 36400, "corporate_action_window_status": "clean_180D_window_assumed_from_profile_or_no_2023_2024_candidate_overlap", "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "081660_2024-05-16_C19_fila_inventory_assets_decline_loss_narrowing_rev", "classification": "positive_inventory_normalization_watch_not_green", "current_profile_error": "stage2_valid_but_green_overcredit_if_revenue_recovery_not_visible"}
{"row_type": "trigger", "case_id": "C19-R5L134-04", "symbol": "383220", "company": "F&F", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2023-07-31", "entry_date": "2023-07-31", "entry_price": 103500, "trigger_type": "Stage4B", "evidence_family": "china_sellthrough_still_solid_domestic_revenue_slowing_brand_premium_deceleration", "source_url": "https://securities.miraeasset.com/bbs/download/2111568.pdf?attachmentId=2111568", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv", "profile_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/383/383220.json", "source_quality": "broker_proxy_with_company_data", "source_proxy_only": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.36, "MFE_90D_pct": 15.94, "MFE_180D_pct": 15.94, "MAE_30D_pct": -6.18, "MAE_90D_pct": -23.57, "MAE_180D_pct": -40.97, "peak_180D_date": "2023-09-19", "peak_180D_high": 120000, "trough_180D_date": "2024-04-16", "trough_180D_low": 61100, "corporate_action_window_status": "clean_180D_window_assumed_from_profile_or_no_2023_2024_candidate_overlap", "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "383220_2023-07-31_C19_china_sellthrough_still_solid_domestic_revenue_s", "classification": "counterexample_4b_stale_brand_premium_deceleration", "current_profile_error": "brand_and_china_story_overcredit_when_domestic_sellthrough_slows_and_margin_peak_is_mature"}
{"row_type": "trigger", "case_id": "C19-R5L134-05", "symbol": "298540", "company": "The Nature Holdings / 더네이쳐홀딩스", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2023-10-24", "entry_date": "2023-10-24", "entry_price": 21250, "trigger_type": "Stage4C", "evidence_family": "national_geographic_overseas_story_fixed_cost_margin_and_inventory_burden", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1698103636056.pdf", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/298/298540/2023.csv", "profile_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/298/298540.json", "source_quality": "broker_proxy_with_company_data", "source_proxy_only": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.65, "MFE_90D_pct": 9.65, "MFE_180D_pct": 9.65, "MAE_30D_pct": -19.58, "MAE_90D_pct": -32.8, "MAE_180D_pct": -46.07, "peak_180D_date": "2023-11-06", "peak_180D_high": 23300, "trough_180D_date": "2024-07-03", "trough_180D_low": 11460, "corporate_action_window_status": "clean_180D_window_assumed_from_profile_or_no_2023_2024_candidate_overlap", "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "298540_2023-10-24_C19_national_geographic_overseas_story_fixed_cost_ma", "classification": "counterexample_4c_brand_expansion_margin_inventory_break", "current_profile_error": "overseas_brand_story_should_not_mask_fixed_cost_margin_and_inventory_drag"}
{"row_type": "trigger", "case_id": "C19-R5L134-06", "symbol": "020000", "company": "Handsome / 한섬", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_RECOVERY_GATE", "trigger_date": "2023-11-06", "entry_date": "2023-11-06", "entry_price": 20050, "trigger_type": "Stage4B", "evidence_family": "premium_brand_house_consumption_slowdown_new_brand_investment_margin_drop", "source_url": "https://www.yna.co.kr/view/AKR20231106086151527", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/020/020000/2023.csv", "profile_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/020/020000.json", "source_quality": "news_company_disclosure_summary", "source_proxy_only": true, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.75, "MFE_90D_pct": 7.98, "MFE_180D_pct": 7.98, "MAE_30D_pct": -6.33, "MAE_90D_pct": -14.36, "MAE_180D_pct": -16.46, "peak_180D_date": "2024-02-07", "peak_180D_high": 21650, "trough_180D_date": "2024-07-25", "trough_180D_low": 16750, "corporate_action_window_status": "clean_180D_window_assumed_from_profile_or_no_2023_2024_candidate_overlap", "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "020000_2023-11-06_C19_premium_brand_house_consumption_slowdown_new_bra", "classification": "counterexample_4b_premium_brand_margin_drag", "current_profile_error": "premium_channel_status_should_not_mask_consumption_slowdown_and_new_brand_investment_drag"}
```

### score simulation rows
```jsonl
{"row_type": "score_simulation", "case_id": "C19-R5L134-01", "symbol": "337930", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "before_weights": "18/18/8/15/14/7/20", "after_weights": "18/21/8/13/12/7/21", "stage_after_residual_rule": "Stage3-Yellow", "error_family": "too_conservative_if_inventory_clearance_caveat_blocks_visible_revenue_and_channel_momentum", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C19-R5L134-02", "symbol": "036620", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "before_weights": "18/18/8/15/14/7/20", "after_weights": "18/21/8/13/12/7/21", "stage_after_residual_rule": "Stage3-Yellow", "error_family": "should_credit_operating_leverage_but_delay_green_until_drawdown_and_inventory_quality_confirmed", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C19-R5L134-03", "symbol": "081660", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "before_weights": "18/18/8/15/14/7/20", "after_weights": "18/21/8/13/12/7/21", "stage_after_residual_rule": "Stage2-Actionable", "error_family": "stage2_valid_but_green_overcredit_if_revenue_recovery_not_visible", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C19-R5L134-04", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "before_weights": "18/18/8/15/14/7/20", "after_weights": "18/21/8/13/12/7/21", "stage_after_residual_rule": "Stage4B", "error_family": "brand_and_china_story_overcredit_when_domestic_sellthrough_slows_and_margin_peak_is_mature", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C19-R5L134-05", "symbol": "298540", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "before_weights": "18/18/8/15/14/7/20", "after_weights": "18/21/8/13/12/7/21", "stage_after_residual_rule": "Stage4C", "error_family": "overseas_brand_story_should_not_mask_fixed_cost_margin_and_inventory_drag", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "score_simulation", "case_id": "C19-R5L134-06", "symbol": "020000", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "before_weights": "18/18/8/15/14/7/20", "after_weights": "18/21/8/13/12/7/21", "stage_after_residual_rule": "Stage4B", "error_family": "premium_channel_status_should_not_mask_consumption_slowdown_and_new_brand_investment_drag", "production_scoring_changed": false, "shadow_weight_only": true}
```

### aggregate / shadow rows
```jsonl
{"row_type": "shadow_weight", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "axis": "C19_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_GATE", "before_weights": "18/18/8/15/14/7/20", "after_weights": "18/21/8/13/12/7/21", "delta": "0/+3/0/-2/-2/0/+1", "production_scoring_changed": false, "shadow_weight_only": true, "basis": "six usable trigger rows; positive/recovery vs stale-premium/4B/4C split"}
{"row_type": "residual_contribution", "selected_round": "R5", "selected_loop": 134, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "new_axis_proposed": "C19_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_GATE", "positive_case_count": 3, "counterexample_count": 3, "rows_missing_required_mfe_mae": 0, "source_proxy_only_count": 6, "evidence_url_pending_count": 0, "current_profile_error_count": 5, "do_not_propose_new_weight_delta": false}
```

## 8. Raw component breakdown

Component order: `eps_fcf_explosion / earnings_visibility / bottleneck_pricing / market_mispricing / valuation_rerating / capital_allocation / information_confidence`.

| case_id | before | after | residual comment |
|---|---|---|---|
| C19-R5L134-01 | 18/18/8/15/14/7/20 | 22/24/8/14/13/7/22 | record revenue and channel expansion are real, but inventory clearing keeps Green confirmation gated |
| C19-R5L134-02 | 18/18/8/15/14/7/20 | 23/23/8/13/12/7/20 | operating leverage exists, but MAE says Green needs inventory/drawdown confirmation |
| C19-R5L134-03 | 18/18/8/15/14/7/20 | 19/21/8/13/12/7/20 | inventory normalization supports Stage2-Actionable but not Green |
| C19-R5L134-04 | 18/18/8/15/14/7/20 | 15/15/8/12/10/7/22 | brand premium overcredit when domestic sell-through slows |
| C19-R5L134-05 | 18/18/8/15/14/7/20 | 12/12/7/10/8/7/24 | overseas story cannot offset margin/inventory/fixed-cost break |
| C19-R5L134-06 | 18/18/8/15/14/7/20 | 14/14/7/11/10/7/22 | premium brand house is not enough when consumption and margin pipe weakens |

## 9. Score and stage simulation

| case_id | old_profile_stage | residual_adjusted_stage | score_after | stage_error_type |
|---|---|---|---:|---|
| C19-R5L134-01 | Stage2-Actionable | Stage3-Yellow | 84 | undercredit_revenue_channel_momentum_but_not_clean_green |
| C19-R5L134-02 | Stage2-Actionable | Stage3-Yellow | 83 | undercredit_operating_leverage_with_high_mae_guard |
| C19-R5L134-03 | Stage2 | Stage2-Actionable | 76 | valid_inventory_normalization_watch |
| C19-R5L134-04 | Stage3-Yellow | Stage4B | 61 | overcredit_stale_brand_premium |
| C19-R5L134-05 | Stage2 | Stage4C | 48 | late_4c_on_brand_inventory_margin_break |
| C19-R5L134-06 | Stage2-Actionable | Stage4B | 58 | overcredit_premium_brand_without_margin_recovery |

## 10. Same-entry dedupe groups

```yaml
same_entry_groups:
  - group_id: 337930_2024-05-13_C19_xexymix_record_revenue_channel
    representative_case_id: C19-R5L134-01
    duplicate_count: 0
  - group_id: 036620_2023-11-14_C19_snowpeak_apparel_record_q3_rev
    representative_case_id: C19-R5L134-02
    duplicate_count: 0
  - group_id: 081660_2024-05-16_C19_fila_inventory_assets_decline_
    representative_case_id: C19-R5L134-03
    duplicate_count: 0
  - group_id: 383220_2023-07-31_C19_china_sellthrough_still_solid_
    representative_case_id: C19-R5L134-04
    duplicate_count: 0
  - group_id: 298540_2023-10-24_C19_national_geographic_overseas_s
    representative_case_id: C19-R5L134-05
    duplicate_count: 0
  - group_id: 020000_2023-11-06_C19_premium_brand_house_consumptio
    representative_case_id: C19-R5L134-06
    duplicate_count: 0
```

## 11. Residual contribution

```yaml
diversity_score_summary: 6 symbols / 6 trigger families / 3 positive / 3 counterexamples / 2 4B / 1 4C / 6 source-proxy-only rows / 0 missing MFE-MAE
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C19 brand-retail inventory/margin quality repair — distinguish true sell-through and margin conversion from stale brand premium, discount-driven clearing, and high inventory burden.
sector_specific_rule_candidate: L5 consumer brand/retail should not open Stage2-Actionable or Green on brand heat, store expansion, or overseas vocabulary alone; require inventory turns, normal-price sell-through, margin/OP proof, and clean working-capital shape.
canonical_archetype_rule_candidate: C19 requires at least two of sell-through/reorder evidence, inventory normalization, normal-price channel strength, gross/OP margin improvement, category/store efficiency, and company-level guidance before Stage3-Green. High inventory ratio, discount clearing, normal-price sales decline, or lead-brand profit collapse should route to 4B/4C.
loop_contribution_label: C19_brand_retail_inventory_margin_quality_repair
new_axis_proposed: C19_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
existing_axis_weakened: []
suggested_shadow_weight_delta:
  before: 18/18/8/15/14/7/20
  after:  18/21/8/13/12/7/21
  delta:  0/+3/0/-2/-2/0/+1
```

## 12. Batch-ingest self-audit

```yaml
standard_v12_filename: pass
filename_round_matches_metadata_round: pass
filename_loop_matches_metadata_loop: pass
large_sector_round_pair_valid: pass
canonical_archetype_valid: pass
trigger_type_canonical_stage_label_only: pass
complete_30_90_180_mfe_mae_each_trigger: pass
actual_stock_web_ohlc_used: pass
same_entry_deduped: pass
positive_and_counterexample_balance: pass
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent E2R calibration.
Do not treat this Markdown as an immediate production patch. Parse the JSONL rows above as v12 residual research input only.
Validate all trigger rows against Stock-Web tradable shards and the active v12 calibration parser.
If rows pass validation, consider the shadow-only C19_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_GATE candidate for archetype-level runtime weighting.
The candidate should strengthen visibility/information-confidence for C19 cases with direct sell-through, inventory normalization, and OP margin proof, while reducing mispricing/valuation credit for stale brand-premium, discount-clearing, high inventory, or normal-price sales decline cases.
Do not loosen Stage3-Green globally. Apply only a C19-scoped bridge/guardrail if aggregate evidence supports it.
```

## 14. Completion state

```text
completed_round = R5
completed_loop = 134
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C19 direct URL/proxy quality, retail inventory-to-margin conversion, discount/clearance 4B-4C split
next_recommended_archetypes = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION; C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN; C22_INSURANCE_RATE_CYCLE_RESERVE; C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
