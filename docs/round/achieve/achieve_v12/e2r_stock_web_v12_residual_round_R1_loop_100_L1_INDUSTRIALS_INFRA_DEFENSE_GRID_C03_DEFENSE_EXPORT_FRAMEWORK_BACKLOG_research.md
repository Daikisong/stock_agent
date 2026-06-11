# E2R Stock-Web v12 Residual Research — R1 / L1 / C03 Defense Export Framework Backlog

```text
selected_round = R1
selected_loop = 100
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_PRICE_ONLY_DEFENSE_BETA
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection and novelty check

The No-Repeat ledger shows `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` with 9 representative rows, 8 symbols, and top covered symbols concentrated in `103140`, `005870`, `042660`, `047810`, `065450`, and `077970`. The selected C03 bucket is still below the 30-row minimum stability zone, so this run fills the gap without reusing those dominant symbol paths.

This run adds four independent symbol paths:

| symbol | name | new C03 angle | prior top-covered duplicate risk |
|---|---|---|---|
| 012450 | 한화에어로스페이스 | integrated ground/engine/defense export framework and backlog conversion | low |
| 079550 | LIG넥스원 | guided weapon export framework and customer-quality backlog | low |
| 064350 | 현대로템 | tank-platform export backlog with delayed price follow-through | low |
| 272210 | 한화시스템 | defense electronics/satellite spike without direct backlog-margin bridge | low |

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No row in this file reuses the current top-covered C03 symbols or an existing hard duplicate from the index.

## 2. Price validation scope

Stock-Web atlas scope:

```text
atlas_version = 1.0.0
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Corporate-action filter:

| symbol | corporate action candidate dates in profile | 2024 selected window contamination |
|---|---|---|
| 012450 | old candidates only, latest listed candidate 2009-02-20 | no |
| 079550 | none | no |
| 064350 | 2020-08-14 | no |
| 272210 | 2021-06-23 | no |

All four trigger windows use tradable 2024 OHLC rows and include complete 30D / 90D / 180D MFE and MAE fields.

## 3. Core thesis compression

C03 should not mean “any defense theme went up.” The reusable rule is narrower:

> **Defense export framework backlog becomes Stage2-Actionable only when the export framework can be mapped to delivery schedule, customer quality, capacity/bottleneck, and margin or cash conversion.**

The sector-specific error left after global v12 calibration is subtle. The current global guard already blocks price-only blowoff, but C03 still needs a more explicit **export-framework-to-margin bridge**. Defense contracts often arrive as long framework headlines. The market may price them immediately, while revenue recognition and margin conversion arrive later like a long train after the whistle. If the train is real, Stage2 should appear before the financial statement fully proves it. If the whistle is only a theme headline, it should stay local 4B/watch.

## 4. Case table

| case | symbol | trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---|---|---:|---:|---:|---:|---|
| C03-A | 012450 | Stage2-Actionable | 2024-02-14 / 146,300 | +53.79 / -8.34 | +74.98 / -8.34 | +190.50 / -8.34 | early export-backlog bridge was highly actionable |
| C03-B | 079550 | Stage2-Actionable | 2024-02-14 / 127,000 | +50.63 / -9.13 | +74.41 / -9.13 | +113.78 / -9.13 | guided-weapon customer quality acted before full earnings confirmation |
| C03-C | 064350 | Stage2 | 2024-03-29 / 36,800 | +16.71 / -7.34 | +46.74 / -7.34 | +84.78 / -7.34 | platform backlog worked, but the path was slower and required delivery-margin distinction |
| C03-D | 272210 | Stage4B local watch | 2024-06-18 / 21,700 | +3.46 / -14.70 | +3.46 / -23.83 | +39.17 / -23.83 | price-only defense electronics spike was a bad Stage2 unless export backlog bridge is verified |

## 5. Residual profile stress test

### 5.1 What current calibrated profile already handles

The current calibrated profile already has good global gates:

```text
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
stage2_actionable_evidence_bonus = +2.0
```

These global rules correctly prevent a generic defense-theme spike from automatically becoming Stage3 or full 4B.

### 5.2 What C03 still needs

C03 needs a sector-specific bridge that distinguishes:

```text
export framework headline
  -> named customer / government framework
  -> delivery schedule or order conversion
  -> production bottleneck or customer quality
  -> margin / FCF / revision bridge
```

Without that bridge, the scorer can still make two opposite mistakes:

1. It may wait too long for realized earnings in true backlog conversion cases like 012450 and 079550.
2. It may over-promote theme-only spikes like 272210's June 2024 local move before a direct export-backlog-to-margin bridge is verified.

## 6. Raw component score simulation

C03 current archetype weights from the index:

```text
EPS/FCF = 20
Visibility = 24
Bottleneck = 17
Mispricing = 14
Valuation = 14
Capital = 6
Information = 5
```

| symbol | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | simulated total | shadow stage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 012450 | 16 | 20 | 16 | 11 | 11 | 4 | 4 | 82 | Stage2-Actionable / Stage3-Yellow watch |
| 079550 | 15 | 19 | 15 | 12 | 10 | 3 | 4 | 78 | Stage2-Actionable |
| 064350 | 13 | 16 | 12 | 12 | 9 | 3 | 4 | 69 | Stage2 with delayed conversion |
| 272210 | 9 | 10 | 8 | 9 | 7 | 2 | 3 | 48 | Stage4B local watch, not positive Stage2 |

## 7. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "case_id": "C03_012450_2024_02_14_stage2_actionable_export_framework_backlog", "symbol": "012450", "name": "한화에어로스페이스", "market": "KOSPI", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CONGLOMERATE_DEFENSE_BETA", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-14", "entry_price": 146300.0, "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "ohlcv_path": "atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv", "entry_ohlc": {"o": 135900.0, "h": 155000.0, "l": 134100.0, "c": 146300.0}, "MFE_30D_pct": 53.79, "MAE_30D_pct": -8.34, "MFE_90D_pct": 74.98, "MAE_90D_pct": -8.34, "MFE_180D_pct": 190.5, "MAE_180D_pct": -8.34, "peak_30D_date": "2024-03-27", "trough_30D_date": "2024-02-14", "peak_90D_date": "2024-06-19", "trough_90D_date": "2024-02-14", "peak_180D_date": "2024-11-12", "trough_180D_date": "2024-02-14", "forward_window_complete": true, "corporate_action_contamination": false, "case_polarity": "positive", "current_profile_error": "too_late_if_waiting_for_reported_margin_only", "evidence_source_type": "source_proxy", "evidence_url_status": "pending_url_repair", "evidence_proxy": "defense_export_framework/backlog delivery visibility and ground-platform ammunition ecosystem proxy; verify with company IR/DART in batch handoff", "component_scores": {"EPS_FCF": 16, "Visibility": 20, "Bottleneck": 16, "Mispricing": 11, "Valuation": 11, "Capital": 4, "Info": 4}, "total_score_simulated": 82}
{"row_type": "trigger", "case_id": "C03_079550_2024_02_14_stage2_actionable_guided_weapon_export_backlog", "symbol": "079550", "name": "LIG넥스원", "market": "KOSPI", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GUIDED_WEAPON_EXPORT_FRAMEWORK_BACKLOG_CUSTOMER_QUALITY_BRIDGE", "trigger_type": "Stage2-Actionable", "entry_date": "2024-02-14", "entry_price": 127000.0, "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "ohlcv_path": "atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv", "entry_ohlc": {"o": 117200.0, "h": 132700.0, "l": 115400.0, "c": 127000.0}, "MFE_30D_pct": 50.63, "MAE_30D_pct": -9.13, "MFE_90D_pct": 74.41, "MAE_90D_pct": -9.13, "MFE_180D_pct": 113.78, "MAE_180D_pct": -9.13, "peak_30D_date": "2024-03-11", "trough_30D_date": "2024-02-14", "peak_90D_date": "2024-06-28", "trough_90D_date": "2024-02-14", "peak_180D_date": "2024-11-08", "trough_180D_date": "2024-02-14", "forward_window_complete": true, "corporate_action_contamination": false, "case_polarity": "positive", "current_profile_error": "underweights_customer_quality_and_export_visibility_vs_generic_defense_beta", "evidence_source_type": "source_proxy", "evidence_url_status": "pending_url_repair", "evidence_proxy": "guided weapon/export customer-quality backlog proxy; verify with company IR/DART in batch handoff", "component_scores": {"EPS_FCF": 15, "Visibility": 19, "Bottleneck": 15, "Mispricing": 12, "Valuation": 10, "Capital": 3, "Info": 4}, "total_score_simulated": 78}
{"row_type": "trigger", "case_id": "C03_064350_2024_03_29_stage2_tank_platform_export_backlog_delayed_followthrough", "symbol": "064350", "name": "현대로템", "market": "KOSPI", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "TANK_PLATFORM_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE_DELAYED_MFE", "trigger_type": "Stage2", "entry_date": "2024-03-29", "entry_price": 36800.0, "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "ohlcv_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv", "entry_ohlc": {"o": 34350.0, "h": 38800.0, "l": 34100.0, "c": 36800.0}, "MFE_30D_pct": 16.71, "MAE_30D_pct": -7.34, "MFE_90D_pct": 46.74, "MAE_90D_pct": -7.34, "MFE_180D_pct": 84.78, "MAE_180D_pct": -7.34, "peak_30D_date": "2024-04-25", "trough_30D_date": "2024-03-29", "peak_90D_date": "2024-08-13", "trough_90D_date": "2024-03-29", "peak_180D_date": "2024-10-18", "trough_180D_date": "2024-03-29", "forward_window_complete": true, "corporate_action_contamination": false, "case_polarity": "mixed_positive", "current_profile_error": "would_mark_price_spike_as_early_success_without_distinguishing_delivery_margin_bridge", "evidence_source_type": "source_proxy", "evidence_url_status": "pending_url_repair", "evidence_proxy": "tank/export platform backlog and delivery schedule proxy; verify with company IR/DART in batch handoff", "component_scores": {"EPS_FCF": 13, "Visibility": 16, "Bottleneck": 12, "Mispricing": 12, "Valuation": 9, "Capital": 3, "Info": 4}, "total_score_simulated": 69}
{"row_type": "trigger", "case_id": "C03_272210_2024_06_18_stage4b_local_defense_electronics_spike_without_backlog_margin_bridge", "symbol": "272210", "name": "한화시스템", "market": "KOSPI", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_ELECTRONICS_SATELLITE_SPIKE_NO_EXPORT_BACKLOG_MARGIN_BRIDGE", "trigger_type": "Stage4B", "entry_date": "2024-06-18", "entry_price": 21700.0, "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "ohlcv_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv", "entry_ohlc": {"o": 19500.0, "h": 22450.0, "l": 19350.0, "c": 21700.0}, "MFE_30D_pct": 3.46, "MAE_30D_pct": -14.7, "MFE_90D_pct": 3.46, "MAE_90D_pct": -23.82, "MFE_180D_pct": 39.17, "MAE_180D_pct": -23.82, "peak_30D_date": "2024-06-18", "trough_30D_date": "2024-06-21", "peak_90D_date": "2024-06-18", "trough_90D_date": "2024-09-09", "peak_180D_date": "2024-11-14", "trough_180D_date": "2024-09-09", "forward_window_complete": true, "corporate_action_contamination": false, "case_polarity": "counterexample", "local_4b_watch": true, "current_profile_error": "price_only_defense_electronics_spike_would_be_overpromoted_without_export_framework_backlog_bridge", "evidence_source_type": "source_proxy", "evidence_url_status": "pending_url_repair", "evidence_proxy": "defense electronics/satellite theme spike without directly verified export framework backlog or margin bridge proxy", "component_scores": {"EPS_FCF": 9, "Visibility": 10, "Bottleneck": 8, "Mispricing": 9, "Valuation": 7, "Capital": 2, "Info": 3}, "total_score_simulated": 48}
```

## 8. Aggregate rows

```jsonl
{"row_type":"aggregate","selected_round":"R1","selected_loop":100,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":2,"mixed_positive_count":1,"counterexample_count":1,"local_4b_watch_count":1,"current_profile_error_count":4,"coverage_gap_before_rows":9,"coverage_gap_after_rows_if_accepted":13,"target_min_rows":30,"still_priority_0":true}
{"row_type":"shadow_weight","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","new_axis_proposed":"C03_export_framework_backlog_delivery_margin_bridge_required","existing_axis_strengthened":"stage2_required_bridge | full_4b_requires_non_price_evidence | price_only_blowoff_blocks_positive_stage | local_4b_watch_guard","existing_axis_weakened":null,"do_not_propose_new_weight_delta":false,"safe_patch_candidate":true}
{"row_type":"residual_contribution","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_pattern":"true defense export framework winners need earlier Stage2-Actionable; price-only defense electronics spikes need local 4B/watch until delivery-margin bridge is verified","implementation_priority":"medium_high"}
```

## 9. Proposed shadow rule

```text
C03_export_framework_backlog_delivery_margin_bridge_required:

For C03, Stage2-Actionable requires at least two of:
1. named export customer / government framework / platform program,
2. backlog or order conversion evidence,
3. delivery schedule or production capacity constraint,
4. margin / FCF / revision bridge,
5. repeated non-price confirmation within the forward evidence window.

If only price momentum or defense-theme vocabulary is present:
- keep as Stage4B local watch,
- do not count as positive Stage2,
- require later confirmation before full 4B or Stage3.
```

This rule should not loosen Stage3-Green. It should only sharpen Stage2-Actionable and local 4B classification inside C03.

## 10. Positive and counterexample balance

Positive cases:

```text
012450: high positive MFE and limited MAE after export/backlog bridge.
079550: high positive MFE and limited MAE after guided-weapon customer-quality bridge.
```

Mixed case:

```text
064350: eventual strong 180D path, but early path was not clean enough to treat every tank-platform headline as immediate Green.
```

Counterexample:

```text
272210: June 2024 spike had poor 30D/90D alignment and deep MAE before later recovery. It should be local 4B/watch unless export backlog and margin bridge are independently verified.
```

## 11. Validation caveats

- Price data is raw/unadjusted FinanceData/marcap transformed into stock-web tradable shards.
- 2024 selected windows do not overlap each symbol's corporate-action candidate dates.
- Evidence URLs are intentionally marked pending because this run uses source proxies and is not a live-current evidence crawl.
- This file is a research handoff artifact only. It does not patch stock_agent code or production scoring.

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later batch coding agent for Songdaiki/stock_agent.

Do not treat this MD as a production patch by itself.
Parse the JSONL rows in this file and validate:
- all trigger rows have entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct;
- all rows use price_source Songdaiki/stock-web and price_basis tradable_raw;
- no row duplicates canonical_archetype_id + symbol + trigger_type + entry_date in the existing validated registry;
- C03 stays mapped to R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID.

Candidate safe patch:
Add or strengthen a C03-specific guard:
C03_export_framework_backlog_delivery_margin_bridge_required.

Semantics:
- Stage2-Actionable can be earlier than reported margin only when named export framework / backlog conversion / delivery schedule / bottleneck / margin-revision bridge are present.
- Price-only defense electronics spikes remain local 4B/watch and do not become positive Stage2.
- Do not loosen Stage3-Green thresholds.
- Do not change production scoring without aggregate evidence across multiple MDs.
```

## 13. Completion state

```text
completed_round = R1
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_PRICE_ONLY_DEFENSE_BETA
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 2
mixed_positive_count = 1
counterexample_count = 1
local_4b_watch_count = 1
current_profile_error_count = 4
auto_selected_coverage_gap = C03 rows 9 -> 13 if accepted; still Priority 0, need 17 to 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C03_export_framework_backlog_delivery_margin_bridge_required
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
next_recommended_archetypes = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C24_BIO_TRIAL_DATA_EVENT_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```
