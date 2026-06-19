# E2R Stock-Web v12 Residual Research — R5 / C18 Consumer Export Channel Reorder

```yaml
artifact_type: stock_web_v12_sector_archetype_residual_calibration
schema_version: e2r_v12_residual_md_v1
selected_round: R5
selected_loop: 133
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selection_mode: coverage_index_first_quality_repair
selected_priority_bucket: Priority 0/1 quality repair — C18 URL/proxy quality, export-channel reorder versus one-off stocking split, 4B/4C taxonomy repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_BRIDGE
price_source: Songdaiki/stock-web
primary_price_route: atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
current_live_scan_performed: false
stock_agent_code_patch_performed: false
```

## 1. Execution contract read-back

This run follows the v12 prompt as a historical calibration/backtest MD generation task only. It does not perform current/live discovery, production scoring changes, auto-trading, or `stock_agent` code patches. The usable trigger rows below use canonical stage labels only, actual Stock-Web daily OHLC rows, complete 30D/90D/180D MFE and MAE fields, same-entry dedupe keys, and standalone Markdown output.

The No-Repeat Index is used only as duplicate-avoidance and coverage-quality ledger. Its latest state has moved past raw row filling: every C01~C32 canonical scope is above the old 80-row threshold, so C18 is selected for source/proxy repair, entry-date/price hygiene, and positive/counterexample balance rather than row-count rescue. C18 is a useful quality-repair zone because consumer export stories often confuse true reorder pull with viral SKU heat, one-off channel stocking, or stale overseas-brand premium.

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
selected_archetype_this_run: C18_CONSUMER_EXPORT_CHANNEL_REORDER
novelty_basis:
  - R5/L5 consumer export channel scope was not used in the immediately preceding execution chain.
  - Cases emphasize K-food/global channel reorder, overseas revenue mix, repeat retail distribution, and stale brand/proxy failure.
  - Same-entry duplicate groups are separated by symbol, trigger date, entry date, and evidence family.
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 4
counterexample_count: 2
stage4b_case_count: 1
stage4c_case_count: 1
source_proxy_only_count: 1
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 5
```

## 3. Case universe

| case_id | symbol | company | trigger_date | entry_date | trigger_type | evidence family | calibration use | interpretation |
|---|---:|---|---|---|---|---|---|---|
| C18-R5L133-01 | 003230 | Samyang Foods | 2024-03-21 | 2024-03-22 | Stage3-Green | buldak_overseas_sales_record_export_mix_miryang_capacity | usable | positive_clean_green |
| C18-R5L133-02 | 005180 | Binggrae | 2023-08-16 | 2023-08-17 | Stage3-Yellow | record_H1_overseas_exports_icecream_channel | usable | positive_stage3_yellow |
| C18-R5L133-03 | 004370 | Nongshim | 2023-07-13 | 2023-07-14 | Stage4B | us_sales_target_global_ramyun_channel_long_dated | usable | counterexample_4b_long_dated_target |
| C18-R5L133-04 | 097950 | CJ CheilJedang | 2024-05-14 | 2024-05-16 | Stage3-Yellow | Q1_profit_overseas_food_bibigo_us_sales | usable | positive_with_high_MAE_watch |
| C18-R5L133-05 | 271560 | Orion | 2024-08-16 | 2024-08-19 | Stage2-Actionable | official_2Q_results_overseas_subsidiary_reorder_quality | usable | positive_stage2_actionable |
| C18-R5L133-06 | 383220 | F&F | 2024-04-17 | 2024-04-18 | Stage4C | fashion_brand_channel_estimate_cut_sellthrough_risk | usable | counterexample_4c_brand_channel_proxy_break |

## 4. Evidence and source map

| case_id | evidence_url | price_shard_url | source_quality | source_proxy_only |
|---|---|---|---|---|
| C18-R5L133-01 | https://www.yna.co.kr/view/AKR20240321039600030 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv | direct_company_reported_news | false |
| C18-R5L133-02 | https://www.kedglobal.com/food-beverage/newsView/ked202308160003 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/005/005180/2023.csv | direct_market_reporting | false |
| C18-R5L133-03 | https://en.yna.co.kr/view/AEN20230713006300320 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv | direct_company_reported_news | false |
| C18-R5L133-04 | https://www.kedglobal.com/earnings/newsView/ked202405140005 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv | direct_market_reporting | false |
| C18-R5L133-05 | https://www.orionworld.com/en/invest/finance/78 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv | official_IR_results_archive | false |
| C18-R5L133-06 | https://securities.miraeasset.com/bbs/download/2125457.pdf?attachmentId=2125457 | https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv | broker_proxy_plus_public_earnings_context | true |

### Case evidence notes

- **C18-R5L133-01 / Samyang Foods.** The trigger is the March 2024 disclosure/reporting that Buldak-driven overseas sales exceeded KRW 800bn for the first time, overseas revenue grew about 34% year over year, and overseas mix reached roughly 68%. Entry is conservatively set to the next tradable close. This is the clean C18 case: the shelf was not just full; the cash register was ringing.
- **C18-R5L133-02 / Binggrae.** The trigger is record first-half overseas exports, with ice cream export momentum tied to Melona/Samanco-style K-dessert demand. The forward path is positive but slower than Samyang, so it supports Yellow rather than automatic Green.
- **C18-R5L133-03 / Nongshim.** The US expansion target and Shin Ramyun global channel are real, but the trigger is a long-dated 2030 ambition. MFE appears early, yet 180D MAE and distant target quality require 4B/watch rather than Green.
- **C18-R5L133-04 / CJ CheilJedang.** Q1 2024 profit beat and overseas food/US sales bridge validate the export-channel thesis. However, conglomerate dilution and 180D drawdown mean C18 credit should remain drawdown-aware.
- **C18-R5L133-05 / Orion.** Official IR evidence of overseas subsidiaries and 2Q results cadence supports a durable but quieter overseas channel. This case prevents the model from overfitting C18 only to viral ramen/ice-cream SKUs.
- **C18-R5L133-06 / F&F.** The trigger is an estimate-cut / demand-quality warning around a fashion-brand channel story. Because the main evidence is broker-proxy and the later drawdown is large, it is kept out of positive promotion statistics but retained as a 4C taxonomy row.

## 5. Stock-Web price rows and MFE/MAE summary

MFE/MAE are calculated from entry close using forward trading-day windows. Values use Stock-Web raw/unadjusted tradable OHLC convention. No 180D window has a share-count discontinuity above the corporate-action screen threshold in this run.

| case_id | symbol | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_180D_date | trough_180D_date | shares_change_180D_max_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| C18-R5L133-01 | 003230 | 193,000 | 63.47 | -2.07 | 272.02 | -2.07 | 281.87 | -2.07 | 2024-12-16 | 2024-03-22 | 0.00 |
| C18-R5L133-02 | 005180 | 55,400 | 6.50 | -7.22 | 9.93 | -12.00 | 39.17 | -12.00 | 2024-05-13 | 2023-10-20 | 0.00 |
| C18-R5L133-03 | 004370 | 404,500 | 21.14 | -4.20 | 23.61 | -4.20 | 23.61 | -14.09 | 2023-10-10 | 2024-02-29 | 0.00 |
| C18-R5L133-04 | 097950 | 329,000 | 23.86 | -0.15 | 23.86 | -8.81 | 23.86 | -29.33 | 2024-06-26 | 2025-01-23 | 0.00 |
| C18-R5L133-05 | 271560 | 92,000 | 8.70 | -6.09 | 15.76 | -6.09 | 38.37 | -6.09 | 2025-05-09 | 2024-09-09 | 0.00 |
| C18-R5L133-06 | 383220 | 65,300 | 12.56 | -3.22 | 17.00 | -27.79 | 17.00 | -27.79 | 2024-07-17 | 2024-08-05 | 0.00 |

## 6. Trigger JSONL

```jsonl
{"row_type": "trigger", "case_id": "C18-R5L133-01", "symbol": "003230", "company": "Samyang Foods", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_BRIDGE", "trigger_date": "2024-03-21", "entry_date": "2024-03-22", "entry_price": 193000, "trigger_type": "Stage3-Green", "evidence_family": "buldak_overseas_sales_record_export_mix_miryang_capacity", "source_url": "https://www.yna.co.kr/view/AKR20240321039600030", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv", "source_quality": "direct_company_reported_news", "source_proxy_only": false, "MFE_30D_pct": 63.47, "MFE_90D_pct": 272.02, "MFE_180D_pct": 281.87, "MAE_30D_pct": -2.07, "MAE_90D_pct": -2.07, "MAE_180D_pct": -2.07, "peak_180D_date": "2024-12-16", "peak_180D_high": 737000, "trough_180D_date": "2024-03-22", "trough_180D_low": 189000, "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "003230_2024-03-22_C18_buldak_export_record", "classification": "positive_clean_green", "current_profile_error": "undercredit_clean_export_reorder_green"}
{"row_type": "trigger", "case_id": "C18-R5L133-02", "symbol": "005180", "company": "Binggrae", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_BRIDGE", "trigger_date": "2023-08-16", "entry_date": "2023-08-17", "entry_price": 55400, "trigger_type": "Stage3-Yellow", "evidence_family": "record_H1_overseas_exports_icecream_channel", "source_url": "https://www.kedglobal.com/food-beverage/newsView/ked202308160003", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/005/005180/2023.csv", "source_quality": "direct_market_reporting", "source_proxy_only": false, "MFE_30D_pct": 6.5, "MFE_90D_pct": 9.93, "MFE_180D_pct": 39.17, "MAE_30D_pct": -7.22, "MAE_90D_pct": -12.0, "MAE_180D_pct": -12.0, "peak_180D_date": "2024-05-13", "peak_180D_high": 77100, "trough_180D_date": "2023-10-20", "trough_180D_low": 48750, "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "005180_2023-08-17_C18_icecream_export_record", "classification": "positive_stage3_yellow", "current_profile_error": "mild_undercredit_export_reorder_with_slow_confirmation"}
{"row_type": "trigger", "case_id": "C18-R5L133-03", "symbol": "004370", "company": "Nongshim", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_BRIDGE", "trigger_date": "2023-07-13", "entry_date": "2023-07-14", "entry_price": 404500, "trigger_type": "Stage4B", "evidence_family": "us_sales_target_global_ramyun_channel_long_dated", "source_url": "https://en.yna.co.kr/view/AEN20230713006300320", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/004/004370/2023.csv", "source_quality": "direct_company_reported_news", "source_proxy_only": false, "MFE_30D_pct": 21.14, "MFE_90D_pct": 23.61, "MFE_180D_pct": 23.61, "MAE_30D_pct": -4.2, "MAE_90D_pct": -4.2, "MAE_180D_pct": -14.09, "peak_180D_date": "2023-10-10", "peak_180D_high": 500000, "trough_180D_date": "2024-02-29", "trough_180D_low": 347500, "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "004370_2023-07-14_C18_us_target_long_dated", "classification": "counterexample_4b_long_dated_target", "current_profile_error": "green_too_easy_on_long_dated_channel_target"}
{"row_type": "trigger", "case_id": "C18-R5L133-04", "symbol": "097950", "company": "CJ CheilJedang", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_BRIDGE", "trigger_date": "2024-05-14", "entry_date": "2024-05-16", "entry_price": 329000, "trigger_type": "Stage3-Yellow", "evidence_family": "Q1_profit_overseas_food_bibigo_us_sales", "source_url": "https://www.kedglobal.com/earnings/newsView/ked202405140005", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv", "source_quality": "direct_market_reporting", "source_proxy_only": false, "MFE_30D_pct": 23.86, "MFE_90D_pct": 23.86, "MFE_180D_pct": 23.86, "MAE_30D_pct": -0.15, "MAE_90D_pct": -8.81, "MAE_180D_pct": -29.33, "peak_180D_date": "2024-06-26", "peak_180D_high": 407500, "trough_180D_date": "2025-01-23", "trough_180D_low": 232500, "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "097950_2024-05-16_C18_overseas_food_Q1_profit", "classification": "positive_with_high_MAE_watch", "current_profile_error": "stage2_actionable_valid_but_green_needs_drawdown_confirmation"}
{"row_type": "trigger", "case_id": "C18-R5L133-05", "symbol": "271560", "company": "Orion", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_BRIDGE", "trigger_date": "2024-08-16", "entry_date": "2024-08-19", "entry_price": 92000, "trigger_type": "Stage2-Actionable", "evidence_family": "official_2Q_results_overseas_subsidiary_reorder_quality", "source_url": "https://www.orionworld.com/en/invest/finance/78", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv", "source_quality": "official_IR_results_archive", "source_proxy_only": false, "MFE_30D_pct": 8.7, "MFE_90D_pct": 15.76, "MFE_180D_pct": 38.37, "MAE_30D_pct": -6.09, "MAE_90D_pct": -6.09, "MAE_180D_pct": -6.09, "peak_180D_date": "2025-05-09", "peak_180D_high": 127300, "trough_180D_date": "2024-09-09", "trough_180D_low": 86400, "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "271560_2024-08-19_C18_orion_overseas_subsidiaries", "classification": "positive_stage2_actionable", "current_profile_error": "undercredit_durable_overseas_subsidiary_channel"}
{"row_type": "trigger", "case_id": "C18-R5L133-06", "symbol": "383220", "company": "F&F", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_BRIDGE", "trigger_date": "2024-04-17", "entry_date": "2024-04-18", "entry_price": 65300, "trigger_type": "Stage4C", "evidence_family": "fashion_brand_channel_estimate_cut_sellthrough_risk", "source_url": "https://securities.miraeasset.com/bbs/download/2125457.pdf?attachmentId=2125457", "price_shard_url": "https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv", "source_quality": "broker_proxy_plus_public_earnings_context", "source_proxy_only": true, "MFE_30D_pct": 12.56, "MFE_90D_pct": 17.0, "MFE_180D_pct": 17.0, "MAE_30D_pct": -3.22, "MAE_90D_pct": -27.79, "MAE_180D_pct": -27.79, "peak_180D_date": "2024-07-17", "peak_180D_high": 76400, "trough_180D_date": "2024-08-05", "trough_180D_low": 47150, "corporate_action_candidate_180D": false, "calibration_usable": true, "same_entry_group_id": "383220_2024-04-18_C18_brand_proxy_estimate_cut", "classification": "counterexample_4c_brand_channel_proxy_break", "current_profile_error": "stale_export_brand_premium_should_route_to_4c"}
```

## 7. Raw component breakdown

Component order: `eps_fcf_explosion / earnings_visibility / bottleneck_pricing / market_mispricing / valuation_rerating / capital_allocation / information_confidence`.

| case_id | before | after | residual comment |
|---|---|---|---|
| C18-R5L133-01 | 23/21/13/12/11/5/8 | 28/26/15/13/12/5/10 | overseas revenue mix + export record + repeat Buldak demand justifies true Green |
| C18-R5L133-02 | 20/17/10/11/10/5/7 | 22/21/11/11/10/5/8 | record exports deserve Yellow, but slower follow-through keeps Green gated |
| C18-R5L133-03 | 20/16/10/13/12/5/7 | 18/16/10/11/9/5/7 | long-dated US target creates channel vocabulary but not near-term reorder proof |
| C18-R5L133-04 | 21/19/10/10/9/6/8 | 22/22/10/10/9/6/9 | overseas food OP bridge is valid but conglomerate/high-MAE profile gates Green |
| C18-R5L133-05 | 18/18/10/9/8/7/8 | 19/21/10/9/8/7/9 | official overseas subsidiaries give durable Stage2 without viral overcredit |
| C18-R5L133-06 | 16/12/8/12/10/5/5 | 12/9/7/8/6/5/5 | stale brand/channel proxy plus estimate cut should invert into 4C |

## 8. Score and stage simulation

| case_id | old_profile_stage | residual_adjusted_stage | score_after | stage_error_type |
|---|---|---|---:|---|
| C18-R5L133-01 | Stage3-Yellow | Stage3-Green | 94 | undercredit_clean_reorder |
| C18-R5L133-02 | Stage2-Actionable | Stage3-Yellow | 82 | mild_undercredit_record_exports |
| C18-R5L133-03 | Stage3-Yellow | Stage4B | 69 | overcredit_long_dated_channel_target |
| C18-R5L133-04 | Stage3-Yellow | Stage3-Yellow + 4B watch | 81 | high_MAE_requires_confirmation |
| C18-R5L133-05 | Stage2 | Stage2-Actionable | 76 | undercredit_durable_overseas_subsidiary |
| C18-R5L133-06 | Stage2 | Stage4C | 58 | stale_brand_proxy_not_cut_fast_enough |

## 9. Same-entry dedupe groups

```yaml
same_entry_groups:
  - group_id: 003230_2024-03-22_C18_buldak_export_record
    representative_case_id: C18-R5L133-01
    duplicate_count: 0
  - group_id: 005180_2023-08-17_C18_icecream_export_record
    representative_case_id: C18-R5L133-02
    duplicate_count: 0
  - group_id: 004370_2023-07-14_C18_us_target_long_dated
    representative_case_id: C18-R5L133-03
    duplicate_count: 0
  - group_id: 097950_2024-05-16_C18_overseas_food_Q1_profit
    representative_case_id: C18-R5L133-04
    duplicate_count: 0
  - group_id: 271560_2024-08-19_C18_orion_overseas_subsidiaries
    representative_case_id: C18-R5L133-05
    duplicate_count: 0
  - group_id: 383220_2024-04-18_C18_brand_proxy_estimate_cut
    representative_case_id: C18-R5L133-06
    duplicate_count: 0
```

## 10. Residual contribution

```yaml
diversity_score_summary: 6 symbols / 6 trigger families / 4 positive / 2 counterexamples / 1 4B / 1 4C / 1 source-proxy-only row
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C18 export-channel reorder quality repair — true reorder and overseas earnings conversion versus viral SKU, long-dated target, or stale brand-channel proxy overcredit
sector_specific_rule_candidate: L5 consumer export channel signals should require sell-through, reorder, named retail/geographic channel, overseas revenue mix, or margin/revision bridge before Stage2-Actionable; viral SKU or overseas-brand vocabulary alone should cap at watch/4B.
canonical_archetype_rule_candidate: C18 requires at least two of named overseas channel, repeated reorder/sell-through evidence, overseas revenue mix acceleration, margin/OP revision, and company-level guidance before Stage3-Green. Stale brand premium plus estimate/sell-through/margin deterioration should route to 4C.
loop_contribution_label: C18_export_channel_reorder_vs_oneoff_stocking_quality_repair
new_axis_proposed: C18_EXPORT_CHANNEL_REORDER_SELLTHROUGH_BRIDGE_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
existing_axis_weakened: []
```

### Suggested shadow weight delta

```yaml
component_order:
  - eps_fcf_explosion
  - earnings_visibility
  - bottleneck_pricing
  - market_mispricing
  - valuation_rerating
  - capital_allocation
  - information_confidence
before: [22, 20, 12, 13, 12, 6, 8]
after:  [22, 23, 12, 11, 10, 6, 10]
delta:  [0, 3, 0, -2, -2, 0, 2]
interpretation: increase earnings-visibility and information-confidence weight only when reorder/sell-through/revenue conversion is direct; reduce generic market-mispricing and valuation-rerating credit for viral SKU, long-dated target, or old overseas-brand proxy.
```

## 11. Proposed rule text

> For `C18_CONSUMER_EXPORT_CHANNEL_REORDER`, Stage2-Actionable should require at least two direct bridges among named overseas retail/geographic channel, repeated reorder or sell-through evidence, overseas revenue mix acceleration, margin/OP revision, and company-level guidance. Stage3-Green requires both channel conversion and earnings/margin confirmation. Viral product exposure, a long-dated market-share target, or stale overseas-brand premium without dated reorder evidence should cap at watch/Stage4B; if accompanied by estimate cuts, sell-through deterioration, or margin break, route to Stage4C.

## 12. Batch ingest self-audit

```yaml
standard_v12_filename: pass
filename_round_matches_metadata: pass
filename_loop_matches_metadata: pass
large_sector_consistency: pass
canonical_archetype_consistency: pass
trigger_jsonl_present: pass
canonical_stage_labels_only: pass
complete_MFE_MAE_30_90_180: pass
entry_date_present: pass
entry_price_present: pass
calibration_usable_flags_present: pass
same_entry_group_ids_present: pass
source_proxy_only_flags_present: pass
evidence_url_pending: 0
rows_missing_required_mfe_mae: 0
production_scoring_changed: false
shadow_weight_only: true
```

## 13. Deferred Coding Agent Handoff Prompt

```text
Read this MD as a v12 residual calibration candidate for R5 / C18_CONSUMER_EXPORT_CHANNEL_REORDER. Do not patch production scoring directly. Parse the JSONL trigger rows, validate all six required MFE/MAE fields, dedupe by same_entry_group_id, and compare against the current C18 representative corpus. If accepted, create a shadow-only rule candidate named C18_EXPORT_CHANNEL_REORDER_SELLTHROUGH_BRIDGE_GATE. The rule should increase information-confidence and earnings-visibility only when direct reorder/sell-through/overseas revenue conversion exists, while capping viral SKU, long-dated market-share target, or stale overseas-brand premium at Stage4B/Stage4C depending on margin/sell-through deterioration. Keep source_proxy_only rows out of positive promotion statistics but retain them for guardrail taxonomy.
```

## 14. Completed state

```yaml
completed: true
completed_round: R5
completed_loop: 133
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C18 URL/proxy quality and export-channel reorder bridge repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_BRIDGE
new_axis_proposed: C18_EXPORT_CHANNEL_REORDER_SELLTHROUGH_BRIDGE_GATE
next_recommended_archetypes:
  - C19_BRAND_RETAIL_INVENTORY_MARGIN
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
```
