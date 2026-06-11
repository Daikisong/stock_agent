# E2R Stock-Web v12 Residual Research

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 109
round_schedule_status: coverage_index_selected
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_SIGNED_CONTRACT_DELIVERY_BACKLOG_BRIDGE_VS_COMPONENT_THEME_LATE_SPIKE_HIGH_MAE
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | defense_export_backlog_guardrail | canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

`V12_Research_No_Repeat_Index.md` shows `C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` at only 9 representative rows / 8 symbols, with top covered symbols `103140`, `005870`, `042660`, `047810`, `065450`, `077970`. This run therefore avoids those top covered symbols and uses new C03 symbols:

- `079550` LIG넥스원
- `012450` 한화에어로스페이스
- `003570` SNT다이내믹스

Existing registry shows C03 at R1 loop 104 and R1 loop 108. Therefore this run uses `selected_loop = 109` for R1/C03.

## 2. Price-source validation

All price rows are taken from `Songdaiki/stock-web` calibration shards:

```text
atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
atlas/ohlcv_tradable_by_symbol_year/079/079550/2025.csv
atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv
atlas/ohlcv_tradable_by_symbol_year/012/012450/2025.csv
atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv
atlas/ohlcv_tradable_by_symbol_year/003/003570/2025.csv
```

Atlas basis:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
research_pack_default_price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

## 3. Research thesis

C03 is not a generic “defense theme” archetype. It requires a company-level export framework or signed contract, visible backlog/delivery schedule, government-customer payment credibility, and plausible margin conversion. The key residual question is whether the active profile still over-rewards component/theme vocabulary and under-weights signed export backlog quality.

This loop separates three routes:

1. **Signed missile export + repeat country/customer validation** — LIG넥스원.
2. **Signed platform export + delivery schedule + large backlog conversion** — 한화에어로스페이스.
3. **Component/subsystem theme or late price spike without immediate signed export-cash bridge** — SNT다이내믹스.

## 4. Cases

| case_id | symbol | name | trigger_date | entry_date | entry_price | trigger_type | result_class | why usable |
|---|---:|---|---|---|---:|---|---|---|
| C03_079550_20240919_IRAQ_MSAM | 079550 | LIG넥스원 | 2024-09-19 | 2024-09-19 | 206500 | Stage2-Actionable | positive_with_high_MAE_watch | Iraq M-SAM export order validates repeat export customer framework after Saudi/UAE line; price path confirms MFE but includes drawdown guard. |
| C03_012450_20240710_ROMANIA_K9 | 012450 | 한화에어로스페이스 | 2024-07-10 | 2024-07-10 | 256500 | Stage2-Actionable | positive | Romania K9/K10 signed order with delivery schedule and prior backlog scale validates contract-to-backlog bridge. |
| C03_003570_20241017_COMPONENT_SPIKE | 003570 | SNT다이내믹스 | 2024-10-17 | 2024-10-17 | 27500 | Stage2-FalsePositive | counterexample_high_MAE_late_repair | Component/powertrain vocabulary and defense beta created a late spike, but no same-date direct export framework/cash bridge; large MAE precedes later repair. |

## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12","selected_round":"R1","selected_loop":109,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_SIGNED_CONTRACT_DELIVERY_BACKLOG_BRIDGE_VS_COMPONENT_THEME_LATE_SPIKE_HIGH_MAE","case_id":"C03_079550_20240919_IRAQ_MSAM","symbol":"079550","name":"LIG넥스원","trigger_date":"2024-09-19","entry_date":"2024-09-19","entry_price":206500,"trigger_type":"Stage2-Actionable","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.33,"MAE_30D_pct":-0.48,"MFE_90D_pct":31.48,"MAE_90D_pct":-18.26,"MFE_180D_pct":57.14,"MAE_180D_pct":-18.26,"forward_high_30D":265000,"forward_low_30D":205500,"forward_high_90D":271500,"forward_low_90D":168800,"forward_high_180D":324500,"forward_low_180D":168800,"evidence_family":"signed_export_order_repeat_country_air_defense_system","non_price_evidence":"Iraq M-SAM export order after Saudi M-SAM export validates repeat government-customer export line; confidentiality limits margin granularity, so high-MAE watch remains.","calibration_usable":true,"representative_for_dedup":true,"profile_verdict":"profile_underweights_repeat_export_framework_but_needs_drawdown_guard"}
{"row_type":"trigger","schema_version":"v12","selected_round":"R1","selected_loop":109,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_SIGNED_CONTRACT_DELIVERY_BACKLOG_BRIDGE_VS_COMPONENT_THEME_LATE_SPIKE_HIGH_MAE","case_id":"C03_012450_20240710_ROMANIA_K9","symbol":"012450","name":"한화에어로스페이스","trigger_date":"2024-07-10","entry_date":"2024-07-10","entry_price":256500,"trigger_type":"Stage2-Actionable","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.65,"MAE_30D_pct":-3.70,"MFE_90D_pct":65.69,"MAE_90D_pct":-3.70,"MFE_180D_pct":204.48,"MAE_180D_pct":-3.70,"forward_high_30D":330000,"forward_low_30D":247000,"forward_high_90D":425000,"forward_low_90D":247000,"forward_high_180D":781000,"forward_low_180D":247000,"evidence_family":"signed_platform_export_order_delivery_schedule_backlog_scale","non_price_evidence":"Romania K9/K10 signed order with ammunition/support and 2029 delivery period; prior defense backlog scale supports conversion bridge.","calibration_usable":true,"representative_for_dedup":true,"profile_verdict":"profile_should_reward_signed_export_platform_backlog_bridge"}
{"row_type":"trigger","schema_version":"v12","selected_round":"R1","selected_loop":109,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_SIGNED_CONTRACT_DELIVERY_BACKLOG_BRIDGE_VS_COMPONENT_THEME_LATE_SPIKE_HIGH_MAE","case_id":"C03_003570_20241017_COMPONENT_SPIKE","symbol":"003570","name":"SNT다이내믹스","trigger_date":"2024-10-17","entry_date":"2024-10-17","entry_price":27500,"trigger_type":"Stage2-FalsePositive","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.55,"MAE_30D_pct":-29.71,"MFE_90D_pct":16.00,"MAE_90D_pct":-40.87,"MFE_180D_pct":114.55,"MAE_180D_pct":-40.87,"forward_high_30D":28200,"forward_low_30D":19330,"forward_high_90D":31900,"forward_low_90D":16260,"forward_high_180D":59000,"forward_low_180D":16260,"evidence_family":"component_subsystem_powertrain_theme_late_spike_no_same_date_export_cash_bridge","non_price_evidence":"Powerpack/transmission component relevance exists, but the selected late spike lacked same-date signed export framework and suffered deep MAE before later repair.","calibration_usable":true,"representative_for_dedup":true,"profile_verdict":"profile_should_block_component_theme_without_signed_export_cash_bridge_or_apply_high_MAE_watch"}
```

## 6. Raw component score breakdown

| case_id | EPS/FCF | visibility/backlog | bottleneck/export scarcity | mispricing | valuation/4B | capital quality | info quality | raw_score | proposed_stage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C03_079550_20240919_IRAQ_MSAM | 15 | 23 | 18 | 14 | 8 | 5 | 5 | 88 | Stage3-Yellow/Green watch |
| C03_012450_20240710_ROMANIA_K9 | 18 | 24 | 17 | 14 | 10 | 6 | 5 | 94 | Stage3-Green |
| C03_003570_20241017_COMPONENT_SPIKE | 8 | 9 | 7 | 8 | 3 | 4 | 4 | 43 | Stage2-FalsePositive / Watch |

## 7. Score-return alignment

| case_id | score_signal | path_alignment | interpretation |
|---|---|---|---|
| C03_079550_20240919_IRAQ_MSAM | high evidence quality but drawdown | medium-positive | Signed missile export framework worked, but confidentiality and post-spike drawdown argue for Green-watch rather than unconditional Green. |
| C03_012450_20240710_ROMANIA_K9 | high evidence quality | strong-positive | Signed export platform order plus backlog scale aligns with strong MFE and contained MAE. |
| C03_003570_20241017_COMPONENT_SPIKE | weak evidence quality | negative/high-MAE then late repair | Component theme can eventually repair, but the entry path is not a clean C03 Stage2 success because deep MAE occurs first. |

## 8. Current calibrated profile stress test

Existing C03 profile appears directionally right on signed export frameworks but still needs two guardrails:

1. **Signed export framework/backlog bridge should outrank generic defense vocabulary.**
2. **Component supplier or domestic-only subsystem events should be blocked from Stage2-Actionable unless tied to a named export framework, delivery schedule, and margin/cash bridge.**

## 9. 4B local vs full-window proximity

| case_id | local 4B watch | full-window 4B watch | reason |
|---|---|---|---|
| C03_079550_20240919_IRAQ_MSAM | yes | mild | 30D MFE > 28% then full-window drawdown > 18%; signed export evidence survives but chase entries need watch. |
| C03_012450_20240710_ROMANIA_K9 | no | no | 30/90/180D path had high MFE and low MAE; backlog bridge remained intact. |
| C03_003570_20241017_COMPONENT_SPIKE | yes | yes | price spike had poor immediate return alignment and deep MAE; later repair should not erase initial false-positive guard. |

## 10. Residual contribution summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: null
existing_axis_strengthened:
  - C03_signed_export_framework_backlog_delivery_bridge_requirement
  - C03_repeat_government_customer_export_visibility_bonus
  - C03_component_subsystem_theme_stage2_block_without_named_export_cash_bridge
  - C03_high_MAE_watch_after_late_component_spike
existing_axis_weakened: null
next_recommended_archetypes:
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When batch-applying v12 calibration artifacts, ingest this MD as a standalone v12 sector-archetype residual research result.
Validate all trigger rows against stock-web OHLC shards. Deduplicate by symbol + canonical_archetype_id + trigger_type + trigger_date + entry_date + entry_price + evidence_family. Treat the C03 component-theme row as a guardrail row, not as a positive promotion row. No production scoring change is authorized by this MD alone; it is shadow-weight evidence only.
```
