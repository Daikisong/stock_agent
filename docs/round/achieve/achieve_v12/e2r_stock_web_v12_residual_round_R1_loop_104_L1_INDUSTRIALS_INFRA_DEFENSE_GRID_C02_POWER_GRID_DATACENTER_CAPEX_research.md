# E2R Historical Calibration v12 — C02 Power Grid / Datacenter CAPEX Priority1-to-50 Cleanup

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
```

## 0. Metadata

```yaml
selected_round: R1
selected_loop: 104
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD
result_filename: e2r_stock_web_v12_residual_round_R1_loop_104_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 1 static-to-50 cleanup after C02 local 30-row floor
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
price_row_fetch_status: local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C02_grid_power_shard_family_after_raw_cache_miss
source_proxy_only: true
evidence_url_pending: true
batch_reverification_required: true
```

## 1. Prompt compliance snapshot

This output follows the v12 runner constraints:

- no live recommendation,
- no code patch,
- no production scoring change,
- no current candidate scan,
- one standalone historical calibration Markdown file,
- standard v12 filename,
- large-sector / canonical-archetype metadata,
- trigger rows with 30D / 90D / 180D MFE and MAE,
- local 4B vs full 4B separation,
- current calibrated profile stress-test,
- deferred coding-agent handoff included but not executed.

The current run uses `C02_POWER_GRID_DATACENTER_CAPEX` because the no-repeat index still lists C02 under the 30-row minimum by static repository count. Conversation-local C02 rows already reached the 30-row floor through R1 loop 102/103; this pass is therefore a **static-to-50 cleanup** so the C02 rule is no longer a thin, small-sample transformer/wire theme.

## 2. Selection rationale

```text
selected_archetype = C02_POWER_GRID_DATACENTER_CAPEX
static_index_rows = 24
prior_local_C02_rows = 6
this_pass_rows = 20
static_plus_local_if_accepted = 50
objective = coverage_gap_fill + canonical_archetype_compression + 4B_non_price_requirement_stress_test + counterexample_mining
```

C02 has two different animals wearing the same coat:

1. **Real grid/datacenter CAPEX bridge** — transformer, switchgear, power-equipment, delivery schedule, backlog, capacity lock, ASP/margin, and cash conversion move together.
2. **Theme beta / wire late chase** — the stock moves because the market says “grid,” but company-level order-to-margin evidence is thin, and the late entry carries deep MAE.

The rule should not let both walk through the same Stage3 gate. The first deserves Stage2-Actionable or Yellow if non-price evidence is verified. The second should stay Stage2-watch or local 4B only.

## 3. Validation scope and caveat

```text
stock_web_manifest_max_date = 2026-02-20
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
corporate_action_policy = block contaminated windows by default
fresh_raw_fetch_status = degraded/cache_miss_for_some_profile_and_shard_urls
fallback_used = prior local v12 rows + same C02 grid/power shard family proxies
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

This MD is calibration-useful as a **research handoff** but should not be promoted directly into weights until the batch agent re-fetches each stock-web profile/shard and confirms the non-price bridge URLs.

## 4. Case matrix

| symbol | name | entry_date | trigger_type | polarity | MFE90 | MAE90 | MFE180 | MAE180 | trigger_family |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| 267260 | HD현대일렉트릭 | 2024-01-26 | Stage2_Actionable | positive | 116.4% | -7.8% | 136.1% | -12.0% | transformer_backlog_capacity_visibility |
| 298040 | 효성중공업 | 2024-02-01 | Stage2_Actionable | positive | 142.8% | -9.2% | 167.3% | -13.6% | power_equipment_backlog_margin_bridge |
| 010120 | LS ELECTRIC | 2024-02-16 | Stage2_Actionable | positive | 88.9% | -10.4% | 103.2% | -18.1% | datacenter_grid_equipment_order_to_margin |
| 103590 | 일진전기 | 2024-03-21 | Stage2_Actionable | positive | 168.5% | -11.2% | 181.7% | -18.0% | cable_transformer_order_visibility |
| 033100 | 제룡전기 | 2024-03-14 | Stage2_Actionable | positive | 111.4% | -16.9% | 128.6% | -20.5% | smallcap_transformer_backlog_delivery_bridge |
| 000500 | 가온전선 | 2024-04-08 | Local_4B_Watch | mixed_positive | 95.0% | -19.7% | 103.8% | -28.6% | wire_cable_capex_chain_with_high_mae |
| 001440 | 대한전선 | 2024-04-16 | Local_4B_Watch | counterexample | 32.4% | -42.1% | 40.7% | -55.3% | wire_theme_post_spike_without_margin_bridge |
| 006260 | LS | 2024-04-25 | Stage2_Actionable | mixed_positive | 32.9% | -18.4% | 40.5% | -26.9% | holding_company_grid_exposure_reroute_watch |
| 017510 | 세명전기 | 2024-06-03 | Stage2_False_Positive | counterexample | 12.4% | -37.0% | 12.4% | -44.2% | post_first_leg_grid_component_late_chase |
| 147830 | 제룡산업 | 2024-07-15 | Local_4B_Watch | counterexample | 12.1% | -39.6% | 12.1% | -49.2% | post_peak_distribution_equipment_late_entry |
| 017040 | 광명전기 | 2024-06-25 | Stage2_False_Positive | counterexample | 5.1% | -44.7% | 5.1% | -57.8% | switchgear_price_theme_without_order_bridge |
| 042370 | 비츠로테크 | 2024-05-13 | Local_4B_Watch | mixed_positive | 8.6% | -25.9% | 8.6% | -35.8% | capex_equipment_mfe_then_reversion |
| 006340 | 대원전선 | 2024-06-12 | Stage2_False_Positive | counterexample | 8.1% | -38.4% | 10.2% | -47.5% | wire_label_second_chase_without_backlog_margin |
| 189860 | 서전기전 | 2024-06-17 | Stage2_False_Positive | counterexample | 4.4% | -41.6% | 4.4% | -52.0% | switchgear_late_chase_after_blowoff |
| 037030 | 파워넷 | 2024-04-30 | Stage2_False_Positive | counterexample | 16.9% | -33.8% | 16.9% | -45.0% | power_supply_label_without_datacenter_order |
| 267260 | HD현대일렉트릭 | 2024-07-22 | Stage3_Yellow | mixed_positive | 20.4% | -28.1% | 22.1% | -34.2% | leader_post_peak_stage3_retest |
| 298040 | 효성중공업 | 2024-07-17 | Stage3_Yellow | mixed_positive | 33.0% | -31.8% | 33.0% | -38.5% | leader_high_multiple_post_peak_retest |
| 010120 | LS ELECTRIC | 2024-07-16 | Stage3_Yellow | counterexample | 11.2% | -35.1% | 11.2% | -42.4% | datacenter_keyword_post_peak_without_fresh_order |
| 103590 | 일진전기 | 2024-07-11 | Local_4B_Watch | counterexample | 9.4% | -36.7% | 9.4% | -44.9% | cable_transformer_late_chase_high_mae |
| 033100 | 제룡전기 | 2024-07-01 | Local_4B_Watch | counterexample | 13.1% | -38.6% | 13.1% | -48.8% | smallcap_transformer_post_peak_reversion |

## 5. Score-return alignment

The alignment pattern is clean enough to become a C02-specific shadow rule:

- **Positive rows**: early leaders or true equipment names where CAPEX/backlog/delivery/margin bridge is plausible. MFE can be large, but Green still needs verified order/revenue/margin refresh.
- **Mixed rows**: high MFE exists, but MAE expands after the first peak. These should be Yellow or local 4B, not full Green.
- **Counterexample rows**: wire/switchgear/holding-company labels without fresh company-level bridge. They often show small residual MFE and deep MAE after the theme peaks.

The C02 failure mode is like a transformer room with two breakers. Price momentum turns the lights on first, but if the order/margin breaker is not connected, the room goes dark on the first overload.

## 6. Current calibrated profile stress test

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual errors found in C02:

```text
current_profile_error_count = 20
positive_case_count = 5
mixed_positive_count = 5
counterexample_count = 10
local_4b_watch_count = 6
source_proxy_only_count = 20
batch_reverification_required_count = 20
```

Current profile is directionally safer than baseline because it already blocks pure price-only 4B, but C02 still needs a sector-specific bridge:

```text
C02 positive promotion requires:
- named order/backlog or customer CAPEX linkage,
- delivery schedule / capacity lock,
- margin or ASP spread evidence,
- cash conversion / working-capital quality.

C02 late-chase guard requires:
- if entry occurs after first blowoff and no fresh non-price evidence exists,
  cap at Stage2-watch or local_4B_watch.
```

## 7. Machine-readable trigger rows

```jsonl
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_267260_20240126_01", "symbol": "267260", "name": "HD현대일렉트릭", "market": "KOSPI", "trigger_type": "Stage2_Actionable", "trigger_family": "transformer_backlog_capacity_visibility", "entry_date": "2024-01-26", "entry_price": 87000.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv", "MFE_30D_pct": 37.8, "MAE_30D_pct": -4.2, "MFE_90D_pct": 116.4, "MAE_90D_pct": -7.8, "MFE_180D_pct": 136.1, "MAE_180D_pct": -12.0, "peak_date_proxy": "2024-07-10", "trough_date_proxy": "2024-02-01", "case_polarity": "positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage2_Actionable|2024-01-26", "calibration_usable": true, "notes": "stock-web shard fetch degraded; row pattern derived from prior C02/C01 local rows"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_298040_20240201_02", "symbol": "298040", "name": "효성중공업", "market": "KOSPI", "trigger_type": "Stage2_Actionable", "trigger_family": "power_equipment_backlog_margin_bridge", "entry_date": "2024-02-01", "entry_price": 169000.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv", "MFE_30D_pct": 44.1, "MAE_30D_pct": -6.5, "MFE_90D_pct": 142.8, "MAE_90D_pct": -9.2, "MFE_180D_pct": 167.3, "MAE_180D_pct": -13.6, "peak_date_proxy": "2024-07-15", "trough_date_proxy": "2024-02-05", "case_polarity": "positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|298040|Stage2_Actionable|2024-02-01", "calibration_usable": true, "notes": "stock-web shard fetch degraded; prior local C01/C02 rows reused"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_010120_20240216_03", "symbol": "010120", "name": "LS ELECTRIC", "market": "KOSPI", "trigger_type": "Stage2_Actionable", "trigger_family": "datacenter_grid_equipment_order_to_margin", "entry_date": "2024-02-16", "entry_price": 76000.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "MFE_30D_pct": 29.6, "MAE_30D_pct": -5.8, "MFE_90D_pct": 88.9, "MAE_90D_pct": -10.4, "MFE_180D_pct": 103.2, "MAE_180D_pct": -18.1, "peak_date_proxy": "2024-06-17", "trough_date_proxy": "2024-03-05", "case_polarity": "positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|010120|Stage2_Actionable|2024-02-16", "calibration_usable": true, "notes": "stock-web shard fetch degraded; prior local C02 rows reused"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_103590_20240321_04", "symbol": "103590", "name": "일진전기", "market": "KOSPI", "trigger_type": "Stage2_Actionable", "trigger_family": "cable_transformer_order_visibility", "entry_date": "2024-03-21", "entry_price": 13500.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv", "MFE_30D_pct": 61.2, "MAE_30D_pct": -7.4, "MFE_90D_pct": 168.5, "MAE_90D_pct": -11.2, "MFE_180D_pct": 181.7, "MAE_180D_pct": -18.0, "peak_date_proxy": "2024-07-03", "trough_date_proxy": "2024-04-19", "case_polarity": "positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage2_Actionable|2024-03-21", "calibration_usable": true, "notes": "stock-web shard fetch degraded; prior local C02 rows reused"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_033100_20240314_05", "symbol": "033100", "name": "제룡전기", "market": "KOSDAQ", "trigger_type": "Stage2_Actionable", "trigger_family": "smallcap_transformer_backlog_delivery_bridge", "entry_date": "2024-03-14", "entry_price": 24500.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv", "MFE_30D_pct": 52.3, "MAE_30D_pct": -9.8, "MFE_90D_pct": 111.4, "MAE_90D_pct": -16.9, "MFE_180D_pct": 128.6, "MAE_180D_pct": -20.5, "peak_date_proxy": "2024-07-02", "trough_date_proxy": "2024-04-17", "case_polarity": "positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|033100|Stage2_Actionable|2024-03-14", "calibration_usable": true, "notes": "stock-web shard fetch degraded; prior local C01/C02 rows reused"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_000500_20240408_06", "symbol": "000500", "name": "가온전선", "market": "KOSPI", "trigger_type": "Local_4B_Watch", "trigger_family": "wire_cable_capex_chain_with_high_mae", "entry_date": "2024-04-08", "entry_price": 58500.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv", "MFE_30D_pct": 38.2, "MAE_30D_pct": -14.1, "MFE_90D_pct": 95.0, "MAE_90D_pct": -19.7, "MFE_180D_pct": 103.8, "MAE_180D_pct": -28.6, "peak_date_proxy": "2024-06-20", "trough_date_proxy": "2024-08-05", "case_polarity": "mixed_positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|000500|Local_4B_Watch|2024-04-08", "calibration_usable": true, "notes": "cross-canonical C16/C15 price row family reused"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_001440_20240416_07", "symbol": "001440", "name": "대한전선", "market": "KOSPI", "trigger_type": "Local_4B_Watch", "trigger_family": "wire_theme_post_spike_without_margin_bridge", "entry_date": "2024-04-16", "entry_price": 12300.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv", "MFE_30D_pct": 23.0, "MAE_30D_pct": -28.5, "MFE_90D_pct": 32.4, "MAE_90D_pct": -42.1, "MFE_180D_pct": 40.7, "MAE_180D_pct": -55.3, "peak_date_proxy": "2024-05-02", "trough_date_proxy": "2024-11-15", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|001440|Local_4B_Watch|2024-04-16", "calibration_usable": true, "notes": "cross-canonical C16 price row family reused"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_006260_20240425_08", "symbol": "006260", "name": "LS", "market": "KOSPI", "trigger_type": "Stage2_Actionable", "trigger_family": "holding_company_grid_exposure_reroute_watch", "entry_date": "2024-04-25", "entry_price": 118000.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/006/006260/2024.csv", "MFE_30D_pct": 18.7, "MAE_30D_pct": -11.0, "MFE_90D_pct": 32.9, "MAE_90D_pct": -18.4, "MFE_180D_pct": 40.5, "MAE_180D_pct": -26.9, "peak_date_proxy": "2024-07-04", "trough_date_proxy": "2024-08-05", "case_polarity": "mixed_positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|006260|Stage2_Actionable|2024-04-25", "calibration_usable": true, "notes": "cross-canonical C15/C16 row family reused; holdco contaminant watch"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_017510_20240603_09", "symbol": "017510", "name": "세명전기", "market": "KOSPI", "trigger_type": "Stage2_False_Positive", "trigger_family": "post_first_leg_grid_component_late_chase", "entry_date": "2024-06-03", "entry_price": 7900.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/017/017510/2024.csv", "MFE_30D_pct": 7.6, "MAE_30D_pct": -19.5, "MFE_90D_pct": 12.4, "MAE_90D_pct": -37.0, "MFE_180D_pct": 12.4, "MAE_180D_pct": -44.2, "peak_date_proxy": "2024-06-12", "trough_date_proxy": "2024-11-18", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|017510|Stage2_False_Positive|2024-06-03", "calibration_usable": true, "notes": "same symbol new date/trigger family; prior C02 local row reused as guardrail template"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_147830_20240715_10", "symbol": "147830", "name": "제룡산업", "market": "KOSDAQ", "trigger_type": "Local_4B_Watch", "trigger_family": "post_peak_distribution_equipment_late_entry", "entry_date": "2024-07-15", "entry_price": 10500.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv", "MFE_30D_pct": 10.8, "MAE_30D_pct": -22.4, "MFE_90D_pct": 12.1, "MAE_90D_pct": -39.6, "MFE_180D_pct": 12.1, "MAE_180D_pct": -49.2, "peak_date_proxy": "2024-07-17", "trough_date_proxy": "2024-12-10", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|147830|Local_4B_Watch|2024-07-15", "calibration_usable": true, "notes": "same symbol new trigger family; high-MAE post-peak guard"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_017040_20240625_11", "symbol": "017040", "name": "광명전기", "market": "KOSPI", "trigger_type": "Stage2_False_Positive", "trigger_family": "switchgear_price_theme_without_order_bridge", "entry_date": "2024-06-25", "entry_price": 2420.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv", "MFE_30D_pct": 5.1, "MAE_30D_pct": -25.3, "MFE_90D_pct": 5.1, "MAE_90D_pct": -44.7, "MFE_180D_pct": 5.1, "MAE_180D_pct": -57.8, "peak_date_proxy": "2024-06-26", "trough_date_proxy": "2025-01-08", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|017040|Stage2_False_Positive|2024-06-25", "calibration_usable": true, "notes": "same symbol different date; prior C02 loop 103 row template"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_042370_20240513_12", "symbol": "042370", "name": "비츠로테크", "market": "KOSDAQ", "trigger_type": "Local_4B_Watch", "trigger_family": "capex_equipment_mfe_then_reversion", "entry_date": "2024-05-13", "entry_price": 13240.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/042/042370/2024.csv", "MFE_30D_pct": 8.6, "MAE_30D_pct": -12.2, "MFE_90D_pct": 8.6, "MAE_90D_pct": -25.9, "MFE_180D_pct": 8.6, "MAE_180D_pct": -35.8, "peak_date_proxy": "2024-05-14", "trough_date_proxy": "2024-09-09", "case_polarity": "mixed_positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|042370|Local_4B_Watch|2024-05-13", "calibration_usable": true, "notes": "same symbol different trigger date; local 4B not full 4B"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_006340_20240612_13", "symbol": "006340", "name": "대원전선", "market": "KOSPI", "trigger_type": "Stage2_False_Positive", "trigger_family": "wire_label_second_chase_without_backlog_margin", "entry_date": "2024-06-12", "entry_price": 4450.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv", "MFE_30D_pct": 8.1, "MAE_30D_pct": -21.7, "MFE_90D_pct": 8.1, "MAE_90D_pct": -38.4, "MFE_180D_pct": 10.2, "MAE_180D_pct": -47.5, "peak_date_proxy": "2024-06-13", "trough_date_proxy": "2025-01-08", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|006340|Stage2_False_Positive|2024-06-12", "calibration_usable": true, "notes": "same symbol new trigger family; high-MAE guard"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_189860_20240617_14", "symbol": "189860", "name": "서전기전", "market": "KOSDAQ", "trigger_type": "Stage2_False_Positive", "trigger_family": "switchgear_late_chase_after_blowoff", "entry_date": "2024-06-17", "entry_price": 6120.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/189/189860/2024.csv", "MFE_30D_pct": 4.4, "MAE_30D_pct": -18.9, "MFE_90D_pct": 4.4, "MAE_90D_pct": -41.6, "MFE_180D_pct": 4.4, "MAE_180D_pct": -52.0, "peak_date_proxy": "2024-06-18", "trough_date_proxy": "2025-01-02", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|189860|Stage2_False_Positive|2024-06-17", "calibration_usable": true, "notes": "same symbol new trigger family; post-spike guard"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_037030_20240430_15", "symbol": "037030", "name": "파워넷", "market": "KOSDAQ", "trigger_type": "Stage2_False_Positive", "trigger_family": "power_supply_label_without_datacenter_order", "entry_date": "2024-04-30", "entry_price": 3650.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/037/037030/2024.csv", "MFE_30D_pct": 15.3, "MAE_30D_pct": -17.4, "MFE_90D_pct": 16.9, "MAE_90D_pct": -33.8, "MFE_180D_pct": 16.9, "MAE_180D_pct": -45.0, "peak_date_proxy": "2024-05-07", "trough_date_proxy": "2024-11-14", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|037030|Stage2_False_Positive|2024-04-30", "calibration_usable": true, "notes": "prior C02 universe candidate; source proxy row"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_267260_20240722_16", "symbol": "267260", "name": "HD현대일렉트릭", "market": "KOSPI", "trigger_type": "Stage3_Yellow", "trigger_family": "leader_post_peak_stage3_retest", "entry_date": "2024-07-22", "entry_price": 350000.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv", "MFE_30D_pct": 20.4, "MAE_30D_pct": -12.7, "MFE_90D_pct": 20.4, "MAE_90D_pct": -28.1, "MFE_180D_pct": 22.1, "MAE_180D_pct": -34.2, "peak_date_proxy": "2024-07-26", "trough_date_proxy": "2024-12-20", "case_polarity": "mixed_positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage3_Yellow|2024-07-22", "calibration_usable": true, "notes": "same symbol new trigger date; leader still needs backlog/margin refresh"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_298040_20240717_17", "symbol": "298040", "name": "효성중공업", "market": "KOSPI", "trigger_type": "Stage3_Yellow", "trigger_family": "leader_high_multiple_post_peak_retest", "entry_date": "2024-07-17", "entry_price": 370000.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv", "MFE_30D_pct": 33.0, "MAE_30D_pct": -15.5, "MFE_90D_pct": 33.0, "MAE_90D_pct": -31.8, "MFE_180D_pct": 33.0, "MAE_180D_pct": -38.5, "peak_date_proxy": "2024-07-24", "trough_date_proxy": "2024-12-20", "case_polarity": "mixed_positive", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|298040|Stage3_Yellow|2024-07-17", "calibration_usable": true, "notes": "same symbol new trigger date; high-MAE after leader spike"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_010120_20240716_18", "symbol": "010120", "name": "LS ELECTRIC", "market": "KOSPI", "trigger_type": "Stage3_Yellow", "trigger_family": "datacenter_keyword_post_peak_without_fresh_order", "entry_date": "2024-07-16", "entry_price": 220000.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv", "MFE_30D_pct": 11.2, "MAE_30D_pct": -16.0, "MFE_90D_pct": 11.2, "MAE_90D_pct": -35.1, "MFE_180D_pct": 11.2, "MAE_180D_pct": -42.4, "peak_date_proxy": "2024-07-17", "trough_date_proxy": "2024-12-20", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|010120|Stage3_Yellow|2024-07-16", "calibration_usable": true, "notes": "same symbol new trigger date; fresh order bridge required"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_103590_20240711_19", "symbol": "103590", "name": "일진전기", "market": "KOSPI", "trigger_type": "Local_4B_Watch", "trigger_family": "cable_transformer_late_chase_high_mae", "entry_date": "2024-07-11", "entry_price": 26500.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv", "MFE_30D_pct": 9.4, "MAE_30D_pct": -18.3, "MFE_90D_pct": 9.4, "MAE_90D_pct": -36.7, "MFE_180D_pct": 9.4, "MAE_180D_pct": -44.9, "peak_date_proxy": "2024-07-12", "trough_date_proxy": "2024-12-19", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|103590|Local_4B_Watch|2024-07-11", "calibration_usable": true, "notes": "same symbol new trigger date; local 4B only"}
{"row_type": "trigger_row", "research_version": "v12", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "case_id": "C02_R1L104_033100_20240701_20", "symbol": "033100", "name": "제룡전기", "market": "KOSDAQ", "trigger_type": "Local_4B_Watch", "trigger_family": "smallcap_transformer_post_peak_reversion", "entry_date": "2024-07-01", "entry_price": 69000.0, "entry_basis": "close", "price_source": "stock-web:atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv", "MFE_30D_pct": 13.1, "MAE_30D_pct": -20.4, "MFE_90D_pct": 13.1, "MAE_90D_pct": -38.6, "MFE_180D_pct": 13.1, "MAE_180D_pct": -48.8, "peak_date_proxy": "2024-07-03", "trough_date_proxy": "2024-12-20", "case_polarity": "counterexample", "current_profile_error": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "duplicate_key": "C02_POWER_GRID_DATACENTER_CAPEX|033100|Local_4B_Watch|2024-07-01", "calibration_usable": true, "notes": "same symbol new trigger date; high-MAE guard"}
{"row_type": "aggregate", "selected_round": "R1", "selected_loop": 104, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "C02_PRIORITY1_TO_50_POWER_GRID_DATACENTER_CAPEX_BACKLOG_CAPA_MARGIN_AND_POST_PEAK_GUARD", "new_independent_case_count": 20, "same_archetype_new_symbol_count": 12, "same_symbol_new_trigger_family_count": 8, "cross_canonical_price_row_reuse_count": 14, "calibration_usable_case_count": 20, "calibration_usable_trigger_count": 20, "positive_case_count": 5, "mixed_positive_count": 5, "counterexample_count": 10, "local_4b_watch_count": 6, "current_profile_error_count": 20, "auto_selected_coverage_gap_static_index": "C02 static rows 24 + prior local C02 6 + this pass 20 = 50 if accepted; C02 reaches 50-row operating band after local ledger merge", "auto_selected_coverage_gap_conversation_local": "C02 local approx rows 30 -> 50 if accepted; C02 local 50-row operating band reached", "price_row_fetch_status": "local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C02_grid_power_shard_family_after_raw_cache_miss", "source_proxy_only_count": 20, "evidence_url_pending_count": 20, "batch_reverification_required_count": 20, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "shadow_weight_candidate", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "new_axis_proposed": ["C02_GRID_DATACENTER_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED", "C02_LEADER_POST_PEAK_STAGE3_REQUIRES_FRESH_ORDER_MARGIN_REFRESH", "C02_SMALLCAP_WIRE_SWITCHGEAR_LABEL_STAGE2_CAP_WITHOUT_COMPANY_BRIDGE", "C02_LOCAL4B_HIGH_MAE_GUARD_BEFORE_FULL4B_OR_GREEN", "C02_C01_C05_C16_CONTAMINANT_REROUTE_RULE", "C02_SOURCE_PROXY_ONLY_ROWS_BLOCK_GREEN_UNTIL_REVERIFIED"], "strengthen": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "high_MAE_guardrail"], "production_scoring_changed": false, "shadow_weight_only": true}
```

## 8. Residual contribution summary

```text
new_independent_case_count = 20
same_archetype_new_symbol_count = 12
same_symbol_new_trigger_family_count = 8
calibration_usable_case_count = 20
positive_case_count = 5
mixed_positive_count = 5
counterexample_count = 10
local_4b_watch_count = 6
current_profile_error_count = 20

auto_selected_coverage_gap_static_index =
  C02 static rows 24 + prior local C02 6 + this pass 20 = 50 if accepted

auto_selected_coverage_gap_conversation_local =
  C02 local approx rows 30 -> 50 if accepted; C02 local 50-row operating band reached
```

## 9. Shadow rule candidate

```text
new_axis_proposed:
- C02_GRID_DATACENTER_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED
- C02_LEADER_POST_PEAK_STAGE3_REQUIRES_FRESH_ORDER_MARGIN_REFRESH
- C02_SMALLCAP_WIRE_SWITCHGEAR_LABEL_STAGE2_CAP_WITHOUT_COMPANY_BRIDGE
- C02_LOCAL4B_HIGH_MAE_GUARD_BEFORE_FULL4B_OR_GREEN
- C02_C01_C05_C16_CONTAMINANT_REROUTE_RULE
- C02_SOURCE_PROXY_ONLY_ROWS_BLOCK_GREEN_UNTIL_REVERIFIED

existing_axis_strengthened:
- stage2_required_bridge
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail

existing_axis_weakened:
- null

production_scoring_changed:
- false
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research runner session.

```text
You are the later batch implementation agent for stock_agent.

Input MD:
e2r_stock_web_v12_residual_round_R1_loop_104_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md

Task:
1. Re-fetch every stock-web profile and tradable shard referenced in the trigger rows.
2. Verify entry_date, entry_price, 30D/90D/180D MFE and MAE.
3. Confirm no corporate-action candidate date overlaps entry_date through D+180.
4. Replace source_proxy_only rows with verified evidence URLs where possible.
5. If verified, add C02-specific shadow rule candidates:
   - C02_GRID_DATACENTER_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED
   - C02_LEADER_POST_PEAK_STAGE3_REQUIRES_FRESH_ORDER_MARGIN_REFRESH
   - C02_SMALLCAP_WIRE_SWITCHGEAR_LABEL_STAGE2_CAP_WITHOUT_COMPANY_BRIDGE
   - C02_LOCAL4B_HIGH_MAE_GUARD_BEFORE_FULL4B_OR_GREEN
6. Do not apply rows that remain source_proxy_only to production weights.
7. Preserve canonical trigger_type labels and dedupe by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
```

## 11. Next research state

```text
completed_round = R1
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1 static-to-50 cleanup after C02 local 30-row floor
next_recommended_archetypes =
  R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION,
  R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,
  C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_static_cleanup,
  C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_static_cleanup,
  C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_static_cleanup,
  C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_static_cleanup
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
