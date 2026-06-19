# e2r_stock_web_v12_residual_round_R1_loop_143_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research

## 0. Machine-readable run metadata

```yaml
run_id: e2r_stock_web_v12_residual_round_R1_loop_143_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
created_at: 2026-06-15
selected_round: R1
selected_loop: 143
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C04 direct URL/source-proxy repair, legal-delay 4B vs hard-4C split, supplier-execution bridge validation
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE
loop_objective: sector_specific_rule_discovery; canonical_archetype_rule_candidate; positive_case_balance; hard_4c_transition_timing_test; legal_delay_watch_vs_kill_split; source_proxy_quality_repair; complete_30_90_180_MFE_MAE
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection rationale and no-repeat audit

This run follows the v12 coverage-index-first rule rather than a mechanical R1→R13 cycle. The immediately preceding generated scope in this session was C03. The current run therefore moves to C04 within the same L1 industrials / infrastructure / defense / grid family, but uses different trigger dates and evidence families: Doosan/KHNP/Doosan Skoda lifecycle cooperation on 2024-09-20, the Czech UOHS temporary block on 2024-10-30, and the Korea-Czech Nuclear Industry Conference held on 2025-02-25.

Existing C04 work already covered the 2024-07-17 Czech preferred-bidder event, 2024-08-27 appeal overhang, and 2025-01-17 Westinghouse/KEPCO/KHNP settlement path. This file avoids those trigger-row keys and only reuses them as background context where needed.

```yaml
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 4
counterexample_count: 3
stage4b_case_count: 3
stage4c_case_count: 1
source_proxy_only_count: 3
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 4
```

## 2. Evidence map

| evidence_id | date | source | summary | role in calibration |
|---|---|---|---|---|
| E01 | 2024-09-20 | Doosan Enerbility | Doosan attended the Korea-Czechia Nuclear Power Full Lifecycle Cooperation Agreement Ceremony at Doosan Skoda Power; KHNP and Doosan Enerbility signed an MOU with Doosan Skoda Power for Czech steam-turbine supply. | Direct project/supplier bridge; positive C04 evidence when paired with named turbine role. |
| E02 | 2024-10-30 | Reuters / Czech UOHS | Czech anti-monopoly office temporarily blocked conclusion of KHNP contract after Westinghouse and EDF challenges; CEZ stated it did not expect schedule impact. | Legal-delay 4B trigger; should block Green but not hard 4C without final contract loss. |
| E03 | 2025-01-16 | U.S. DOE | Westinghouse, KEPCO, and KHNP settlement agreement framed broader U.S.-Korea civil nuclear cooperation. | Background de-risking context; not used as a duplicate trigger row. |
| E04 | 2025-02-25 | KAIF | Korea-Czech Nuclear Industry Conference in Prague brought Korean and Czech nuclear players together; sponsors included KHNP, KEPCO KPS, KEPCO E&C, KEPCO NF, Doosan Enerbility, and others. | Supplier-ecosystem bridge; useful to split direct service/engineering roles from loose proxy suppliers. |
| E05 | standing capability | KEPCO KPS | KEPCO KPS states it maintains primary and secondary control systems of nuclear power plants and provides plant maintenance engineering. | Service bridge for C04 Stage2-Actionable when tied to Czech supplier ecosystem. |
| E06 | standing capability | Woori Technology | Woori describes nuclear I&C, MMIS, and monitoring/control systems for nuclear plants. | Direct nuclear capability but no named Czech contract; proxy-risk calibration. |
| E07 | standing capability | KEPCO E&C / Iljin Power | KEPCO E&C described Iljin Power as specialized in routine maintenance of power plants and manufacturing nuclear/renewable equipment. | Weak C04 supplier proxy unless named project award appears. |
| E08 | standing capability | KAIF Korean Nuclear Vendors List | Lists Doosan Heavy Industries & Construction in manufacturing, Woojin in MMIS/BOP manufacturing, and KEPCO KPS in management/maintenance. | Supplier taxonomy anchor; not sufficient alone for positive promotion. |

## 3. Trigger price table

| case_id | symbol | name | trigger_date | entry_date | trigger_type | entry_close | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_180D_date | trough_180D_date | outcome | source_proxy_only |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|
| T01 | 034020 | Doosan Enerbility | 2024-09-20 | 2024-09-23 | Stage2-Actionable | 18200 | 21.70 | -5.82 | 38.19 | -7.09 | 281.32 | -7.09 | 2025-06-23 | 2024-12-10 | positive | false |
| T02 | 105840 | Woojin | 2024-09-20 | 2024-09-23 | Stage4B | 8120 | 9.24 | -7.14 | 9.24 | -30.67 | 63.79 | -30.67 | 2025-06-19 | 2024-12-09 | counterexample | true |
| T03 | 052690 | KEPCO E&C | 2024-10-30 | 2024-10-31 | Stage4B | 68800 | 4.80 | -28.42 | 10.32 | -28.42 | 76.89 | -28.42 | 2025-06-25 | 2024-12-10 | positive_guardrail | false |
| T04 | 032820 | Woori Technology | 2024-10-30 | 2024-10-31 | Stage4B | 2170 | 12.90 | -24.79 | 12.90 | -25.30 | 141.47 | -33.04 | 2025-07-01 | 2025-04-09 | counterexample | true |
| T05 | 094820 | Iljin Power | 2024-10-30 | 2024-10-31 | Stage4C | 9910 | 8.68 | -30.37 | 8.68 | -30.37 | 39.15 | -30.37 | 2025-05-26 | 2024-12-09 | counterexample | true |
| T06 | 051600 | KEPCO KPS | 2025-02-25 | 2025-02-26 | Stage2-Actionable | 42400 | 4.13 | -10.38 | 54.25 | -10.38 | 54.25 | -10.38 | 2025-06-25 | 2025-04-09 | positive | false |
| T07 | 034020 | Doosan Enerbility | 2025-02-25 | 2025-02-26 | Stage3-Yellow | 27600 | 2.17 | -27.68 | 161.59 | -27.68 | 252.90 | -27.68 | 2025-10-29 | 2025-04-09 | positive | false |


## 4. Case notes

### T01 — 034020 Doosan Enerbility

- trigger_date / entry_date: 2024-09-20 / 2024-09-23
- evidence_family: Doosan/KHNP/Doosan Skoda steam-turbine MOU at Korea-Czech lifecycle cooperation ceremony
- source_url: https://www.doosanenerbility.com/en/about/news_board_view?id=21000643
- stage_read: direct supplier bridge; not merely policy headline
- price_path: 30D 21.70/-5.82, 90D 38.19/-7.09, 180D 281.32/-7.09. Peak date 2025-06-23, trough date 2024-12-10.
- calibration_use: calibration_usable=true, source_proxy_only=false, current_profile_error=false

### T02 — 105840 Woojin

- trigger_date / entry_date: 2024-09-20 / 2024-09-23
- evidence_family: nuclear instrumentation supplier list / no Czech project execution bridge
- source_url: https://www.asiae.co.kr/en/article/2023080710104933891
- stage_read: supplier relevance exists, but Czech-specific contract bridge absent; high drawdown requires 4B watch cap
- price_path: 30D 9.24/-7.14, 90D 9.24/-30.67, 180D 63.79/-30.67. Peak date 2025-06-19, trough date 2024-12-09.
- calibration_use: calibration_usable=true, source_proxy_only=true, current_profile_error=true

### T03 — 052690 KEPCO E&C

- trigger_date / entry_date: 2024-10-30 / 2024-10-31
- evidence_family: Czech UOHS temporary block after Westinghouse/EDF appeals
- source_url: https://www.reuters.com/business/energy/czech-watchdog-prohibits-nuclear-power-contract-signing-amid-appeals-2024-10-30/
- stage_read: legal delay should block Green but not hard 4C without final contract loss; later MFE validates watch-not-kill
- price_path: 30D 4.80/-28.42, 90D 10.32/-28.42, 180D 76.89/-28.42. Peak date 2025-06-25, trough date 2024-12-10.
- calibration_use: calibration_usable=true, source_proxy_only=false, current_profile_error=false

### T04 — 032820 Woori Technology

- trigger_date / entry_date: 2024-10-30 / 2024-10-31
- evidence_family: nuclear I&C capability plus Czech legal-delay sympathy
- source_url: https://www.wooritg.com/en/business/system/
- stage_read: direct nuclear I&C capability exists, but no named Dukovany role; high MAE says do not promote above watch before contract evidence
- price_path: 30D 12.90/-24.79, 90D 12.90/-25.30, 180D 141.47/-33.04. Peak date 2025-07-01, trough date 2025-04-09.
- calibration_use: calibration_usable=true, source_proxy_only=true, current_profile_error=true

### T05 — 094820 Iljin Power

- trigger_date / entry_date: 2024-10-30 / 2024-10-31
- evidence_family: generic nuclear maintenance/manufacturing supplier sympathy under legal-delay shock
- source_url: https://www.kepco-enc.com/board.es?act=view&bid=0039&list_no=34827&mid=a20501000000&nPage=14&tag=
- stage_read: source-proxy and small-cap price path: treat as 4C/invalid-positive unless Czech-specific award appears
- price_path: 30D 8.68/-30.37, 90D 8.68/-30.37, 180D 39.15/-30.37. Peak date 2025-05-26, trough date 2024-12-09.
- calibration_use: calibration_usable=true, source_proxy_only=true, current_profile_error=true

### T06 — 051600 KEPCO KPS

- trigger_date / entry_date: 2025-02-25 / 2025-02-26
- evidence_family: Korea-Czech Nuclear Industry Conference with KEPCO KPS sponsor/maintenance role
- source_url: https://kaif.or.kr/en/?c=254&s=&sw=industrial&gp=1&gbn=viewok&ix=29135
- stage_read: service/maintenance bridge is weaker than turbine/EPC but enough for Stage2-Actionable when conference + NPP maintenance capability align
- price_path: 30D 4.13/-10.38, 90D 54.25/-10.38, 180D 54.25/-10.38. Peak date 2025-06-25, trough date 2025-04-09.
- calibration_use: calibration_usable=true, source_proxy_only=false, current_profile_error=false

### T07 — 034020 Doosan Enerbility

- trigger_date / entry_date: 2025-02-25 / 2025-02-26
- evidence_family: post-settlement Czech supplier ecosystem + direct turbine/BOP bridge for Doosan
- source_url: https://kaif.or.kr/en/?c=254&s=&sw=industrial&gp=1&gbn=viewok&ix=29135
- stage_read: structural winner but early MAE was severe; Green requires drawdown-aware confirmation after legal/procurement clarity
- price_path: 30D 2.17/-27.68, 90D 161.59/-27.68, 180D 252.90/-27.68. Peak date 2025-10-29, trough date 2025-04-09.
- calibration_use: calibration_usable=true, source_proxy_only=false, current_profile_error=true


## 5. Residual rule discovery

### 5.1 What the current profile can misread

C04 is not a simple “nuclear policy is bullish” archetype. The Czech project shows three distinct mechanisms:

1. **Project role bridge** — named project, named customer/government body, named component or service role, and dated delivery path. Doosan Enerbility has the clearest bridge through Doosan Skoda turbine language.
2. **Legal-delay overhang** — UOHS/EDF/Westinghouse appeals are real 4B evidence, but a preliminary block is not automatically a thesis break. If CEZ/KHNP still expect schedule continuity and later legal/procurement clarity arrives, hard 4C overkills the winner.
3. **Supplier-proxy heat** — nuclear I&C, maintenance, or component capability may be real, but without a Dukovany-specific award, it should not receive the same Stage2-Actionable credit as a direct turbine/EPC/sponsor role.

### 5.2 Proposed shadow axis

```yaml
new_axis_proposed: C04_NUCLEAR_PROJECT_LEGAL_DELAY_EXECUTION_BRIDGE_GATE
axis_type: archetype_specific_guardrail
production_scoring_changed: false
shadow_weight_only: true
rule_text: >
  For C04 nuclear policy/project cases, do not open Stage2-Actionable or Green from
  policy/preferred-bidder headlines alone. Require at least two of: named customer or
  government project, named company role/component/service, signed MOU/contract or sponsor
  role tied to project execution, delivery/backlog/revenue timing, and legal/procurement
  clearance. Treat appeals, watchdog blocks, and court halts as Stage4B unless there is
  confirmed contract cancellation, project award loss, or direct company guidance break.
```

### 5.3 Suggested shadow weight direction

```yaml
before_component_shape: policy_event: high; bottleneck_role: medium; legal_risk: medium; company_execution: medium; proxy_penalty: low
suggested_after_component_shape: policy_event: lower; bottleneck_role: higher; legal_risk: conditional_4b; company_execution: higher; proxy_penalty: higher
suggested_shadow_weight_delta:
  policy_event_headline: -2
  named_project_role: +2
  legal_delay_watch_guard: +2
  source_proxy_penalty: +2
  drawdown_aware_confirmation: +1
```

## 6. Batch-ingest JSONL trigger rows

```jsonl
{"MAE_180D_pct": -7.09, "MAE_30D_pct": -5.82, "MAE_90D_pct": -7.09, "MFE_180D_pct": 281.32, "MFE_30D_pct": 21.7, "MFE_90D_pct": 38.19, "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "T01", "current_profile_error": false, "entry_amount": 71987217900.0, "entry_close": 18200.0, "entry_date": "2024-09-23", "entry_high": 18720.0, "entry_low": 18120.0, "entry_open": 18300.0, "entry_price": 18200.0, "entry_volume": 3924727, "evidence_family": "Doosan/KHNP/Doosan Skoda steam-turbine MOU at Korea-Czech lifecycle cooperation ceremony", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market_cap": 11658212857200.0, "name": "Doosan Enerbility", "outcome": "positive", "peak_180D_date": "2025-06-23", "peak_180D_high": 69400.0, "row_type": "trigger", "same_entry_group_id": "034020::2024-09-23::2024-09-20::Doosan/KHNP/Doosan Skoda steam-t", "source_proxy_only": false, "stage_view": "direct supplier bridge; not merely policy headline", "symbol": "034020", "trigger_date": "2024-09-20", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-12-10", "trough_180D_low": 16910.0, "url": "https://www.doosanenerbility.com/en/about/news_board_view?id=21000643"}
{"MAE_180D_pct": -30.67, "MAE_30D_pct": -7.14, "MAE_90D_pct": -30.67, "MFE_180D_pct": 63.79, "MFE_30D_pct": 9.24, "MFE_90D_pct": 9.24, "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "T02", "current_profile_error": true, "entry_amount": 951369960.0, "entry_close": 8120.0, "entry_date": "2024-09-23", "entry_high": 8230.0, "entry_low": 8050.0, "entry_open": 8160.0, "entry_price": 8120.0, "entry_volume": 116794, "evidence_family": "nuclear instrumentation supplier list / no Czech project execution bridge", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market_cap": 165027745680.0, "name": "Woojin", "outcome": "counterexample", "peak_180D_date": "2025-06-19", "peak_180D_high": 13300.0, "row_type": "trigger", "same_entry_group_id": "105840::2024-09-23::2024-09-20::nuclear instrumentation supplier", "source_proxy_only": true, "stage_view": "supplier relevance exists, but Czech-specific contract bridge absent; high drawdown requires 4B watch cap", "symbol": "105840", "trigger_date": "2024-09-20", "trigger_type": "Stage4B", "trough_180D_date": "2024-12-09", "trough_180D_low": 5630.0, "url": "https://www.asiae.co.kr/en/article/2023080710104933891"}
{"MAE_180D_pct": -28.42, "MAE_30D_pct": -28.42, "MAE_90D_pct": -28.42, "MFE_180D_pct": 76.89, "MFE_30D_pct": 4.8, "MFE_90D_pct": 10.32, "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "T03", "current_profile_error": false, "entry_amount": 23276102300.0, "entry_close": 68800.0, "entry_date": "2024-10-31", "entry_high": 69800.0, "entry_low": 66000.0, "entry_open": 68000.0, "entry_price": 68800.0, "entry_volume": 344602, "evidence_family": "Czech UOHS temporary block after Westinghouse/EDF appeals", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market_cap": 2629536000000.0, "name": "KEPCO E&C", "outcome": "positive_guardrail", "peak_180D_date": "2025-06-25", "peak_180D_high": 121700.0, "row_type": "trigger", "same_entry_group_id": "052690::2024-10-31::2024-10-30::Czech UOHS temporary block after", "source_proxy_only": false, "stage_view": "legal delay should block Green but not hard 4C without final contract loss; later MFE validates watch-not-kill", "symbol": "052690", "trigger_date": "2024-10-30", "trigger_type": "Stage4B", "trough_180D_date": "2024-12-10", "trough_180D_low": 49250.0, "url": "https://www.reuters.com/business/energy/czech-watchdog-prohibits-nuclear-power-contract-signing-amid-appeals-2024-10-30/"}
{"MAE_180D_pct": -33.04, "MAE_30D_pct": -24.79, "MAE_90D_pct": -25.3, "MFE_180D_pct": 141.47, "MFE_30D_pct": 12.9, "MFE_90D_pct": 12.9, "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "T04", "current_profile_error": true, "entry_amount": 15774663970.0, "entry_close": 2170.0, "entry_date": "2024-10-31", "entry_high": 2210.0, "entry_low": 2145.0, "entry_open": 2150.0, "entry_price": 2170.0, "entry_volume": 7265249, "evidence_family": "nuclear I&C capability plus Czech legal-delay sympathy", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market_cap": 344724134160.0, "name": "Woori Technology", "outcome": "counterexample", "peak_180D_date": "2025-07-01", "peak_180D_high": 5240.0, "row_type": "trigger", "same_entry_group_id": "032820::2024-10-31::2024-10-30::nuclear I&C capability plus Czec", "source_proxy_only": true, "stage_view": "direct nuclear I&C capability exists, but no named Dukovany role; high MAE says do not promote above watch before contract evidence", "symbol": "032820", "trigger_date": "2024-10-30", "trigger_type": "Stage4B", "trough_180D_date": "2025-04-09", "trough_180D_low": 1453.0, "url": "https://www.wooritg.com/en/business/system/"}
{"MAE_180D_pct": -30.37, "MAE_30D_pct": -30.37, "MAE_90D_pct": -30.37, "MFE_180D_pct": 39.15, "MFE_30D_pct": 8.68, "MFE_90D_pct": 8.68, "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "T05", "current_profile_error": true, "entry_amount": 2676047050.0, "entry_close": 9910.0, "entry_date": "2024-10-31", "entry_high": 10080.0, "entry_low": 9780.0, "entry_open": 9800.0, "entry_price": 9910.0, "entry_volume": 269152, "evidence_family": "generic nuclear maintenance/manufacturing supplier sympathy under legal-delay shock", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market_cap": 149430006190.0, "name": "Iljin Power", "outcome": "counterexample", "peak_180D_date": "2025-05-26", "peak_180D_high": 13790.0, "row_type": "trigger", "same_entry_group_id": "094820::2024-10-31::2024-10-30::generic nuclear maintenance/manu", "source_proxy_only": true, "stage_view": "source-proxy and small-cap price path: treat as 4C/invalid-positive unless Czech-specific award appears", "symbol": "094820", "trigger_date": "2024-10-30", "trigger_type": "Stage4C", "trough_180D_date": "2024-12-09", "trough_180D_low": 6900.0, "url": "https://www.kepco-enc.com/board.es?act=view&bid=0039&list_no=34827&mid=a20501000000&nPage=14&tag="}
{"MAE_180D_pct": -10.38, "MAE_30D_pct": -10.38, "MAE_90D_pct": -10.38, "MFE_180D_pct": 54.25, "MFE_30D_pct": 4.13, "MFE_90D_pct": 54.25, "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "T06", "current_profile_error": false, "entry_amount": 4927425100.0, "entry_close": 42400.0, "entry_date": "2025-02-26", "entry_high": 42900.0, "entry_low": 42200.0, "entry_open": 42900.0, "entry_price": 42400.0, "entry_volume": 116095, "evidence_family": "Korea-Czech Nuclear Industry Conference with KEPCO KPS sponsor/maintenance role", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market_cap": 1908000000000.0, "name": "KEPCO KPS", "outcome": "positive", "peak_180D_date": "2025-06-25", "peak_180D_high": 65400.0, "row_type": "trigger", "same_entry_group_id": "051600::2025-02-26::2025-02-25::Korea-Czech Nuclear Industry Con", "source_proxy_only": false, "stage_view": "service/maintenance bridge is weaker than turbine/EPC but enough for Stage2-Actionable when conference + NPP maintenance capability align", "symbol": "051600", "trigger_date": "2025-02-25", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-04-09", "trough_180D_low": 38000.0, "url": "https://kaif.or.kr/en/?c=254&s=&sw=industrial&gp=1&gbn=viewok&ix=29135"}
{"MAE_180D_pct": -27.68, "MAE_30D_pct": -27.68, "MAE_90D_pct": -27.68, "MFE_180D_pct": 252.9, "MFE_30D_pct": 2.17, "MFE_90D_pct": 161.59, "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "T07", "current_profile_error": true, "entry_amount": 217247791300.0, "entry_close": 27600.0, "entry_date": "2025-02-26", "entry_high": 28200.0, "entry_low": 27200.0, "entry_open": 28000.0, "entry_price": 27600.0, "entry_volume": 7857812, "evidence_family": "post-settlement Czech supplier ecosystem + direct turbine/BOP bridge for Doosan", "evidence_url_pending": false, "fine_archetype_id": "CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "market_cap": 17679487629600.0, "name": "Doosan Enerbility", "outcome": "positive", "peak_180D_date": "2025-10-29", "peak_180D_high": 97400.0, "row_type": "trigger", "same_entry_group_id": "034020::2025-02-26::2025-02-25::post-settlement Czech supplier e", "source_proxy_only": false, "stage_view": "structural winner but early MAE was severe; Green requires drawdown-aware confirmation after legal/procurement clarity", "symbol": "034020", "trigger_date": "2025-02-25", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-04-09", "trough_180D_low": 19960.0, "url": "https://kaif.or.kr/en/?c=254&s=&sw=industrial&gp=1&gbn=viewok&ix=29135"}
```

## 7. Batch ingest self-audit

```yaml
standard_filename: pass
filename_round_loop_matches_metadata: pass
canonical_archetype_id_valid: pass
large_sector_id_valid: pass
round_sector_consistency: pass
stock_web_price_source_used: pass
entry_date_rule_documented: pass
all_trigger_rows_have_entry_price: pass
all_trigger_rows_have_MFE_30D_pct: pass
all_trigger_rows_have_MFE_90D_pct: pass
all_trigger_rows_have_MFE_180D_pct: pass
all_trigger_rows_have_MAE_30D_pct: pass
all_trigger_rows_have_MAE_90D_pct: pass
all_trigger_rows_have_MAE_180D_pct: pass
source_url_present_for_all_rows: pass
evidence_url_pending_count: 0
source_proxy_only_count: 3
calibration_usable_trigger_count: 7
narrative_only_rows_due_incomplete_180D: 0
no_repeat_duplicate_key_check: pass
same_symbol_same_trigger_date_same_entry_date_reuse: none
```

## 8. Deferred coding-agent handoff prompt

```text
Apply no production code change. Add this file as a v12 calibration candidate only.
If promoted later, implement an archetype-specific C04 guardrail named
C04_NUCLEAR_PROJECT_LEGAL_DELAY_EXECUTION_BRIDGE_GATE. The guardrail should lower credit
for policy/preferred-bidder headlines without named company role, require execution bridge
for Stage2-Actionable, route legal/procurement challenge headlines to Stage4B rather than
hard 4C unless contract loss/project cancellation/guidance break is confirmed, and apply
source_proxy_only penalty to generic nuclear supplier sympathy rows.
```

## 9. Final state

```yaml
completed: true
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selected_round: R1
selected_loop: 143
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_LEGAL_DELAY_SUPPLIER_EXECUTION_BRIDGE
loop_contribution_label: C04_legal_delay_execution_bridge_proxy_quality_repair
new_axis_proposed: C04_NUCLEAR_PROJECT_LEGAL_DELAY_EXECUTION_BRIDGE_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
existing_axis_weakened: null
next_recommended_archetypes:
  - C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
```
