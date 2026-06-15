# E2R v12 Stock-Web Residual Research — R1 / Loop 105 / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 105
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_EXPORT_HEADLINE_PRICE_ONLY_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Executive summary

이번 루프는 C03 방산 수출 프레임워크/수주잔고 축의 빈칸을 채우는 잔여 보정 연구다. 기존 글로벌 보정은 `Stage2-Actionable +2`, Green 문턱 상향, price-only 4B 차단으로 큰 오탐을 많이 줄였지만, 방산은 뉴스가 “계약 → 납품 → 매출 인식 → 마진/운전자본”으로 늦게 굴러가는 특성 때문에 일반 수주/정책/지정학 테마와 조금 다르게 움직인다. 포탄이 발사되고 목표물까지 날아가는 동안 탄도 보정을 하듯, C03은 headline 자체가 아니라 **정부 고객, 예산·파이낸싱, 계약 효력, 납품 스케줄, 수출허가/offset/localization, backlog-to-margin conversion**의 중간 궤도를 확인해야 한다.

이번 연구의 핵심 결론은 다음과 같다.

```text
C03 should not be treated as generic order backlog.
C03 needs an explicit export-framework-to-backlog-to-delivery-to-margin bridge.
Defense export headlines can be Stage2-Actionable, but Green should require at least one non-price bridge:
  - signed contract / framework conversion / firm order
  - named sovereign customer and funding visibility
  - delivery schedule or backlog conversion cadence
  - margin / working-capital / capacity bridge
  - license, offset, localization, or political delay risk cleared or bounded
```

이번 샘플은 stock-web 1D OHLCV row를 직접 확인한 4개 독립 사례다.

| case_id | symbol | name | trigger_date | entry_price | classification | profile residual |
|---|---:|---|---:|---:|---|---|
| C03-R1L105-01 | 012450 | 한화에어로스페이스 | 2024-02-27 | 179100 | positive | calibrated profile can still under-rank export backlog compounding when delivery/margin bridge exists |
| C03-R1L105-02 | 079550 | LIG넥스원 | 2024-03-06 | 168500 | positive/mixed | strong eventual MFE but high MAE demands government-customer/funding/delivery bridge |
| C03-R1L105-03 | 064350 | 현대로템 | 2024-02-22 | 34500 | mixed_positive | export/platform backlog works only when rail/defense mix and margin bridge are separated |
| C03-R1L105-04 | 272210 | 한화시스템 | 2024-03-06 | 18450 | counterexample/local_4b_watch | defense/space/systems label can create price-only false positive without backlog conversion clarity |

## 2. Source and validation scope

### 2.1 Allowed source use

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_research_artifact_access_allowed = true
stock_agent_research_artifact_access_purpose = coverage_gap_and_duplicate_avoidance_only
stock_web_price_atlas_access_required = true
```

Used stock_agent artifact:

```text
docs/core/V12_Research_No_Repeat_Index.md
```

Used stock-web price routes:

```text
atlas/symbol_profiles/012/012450.json
atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv
atlas/symbol_profiles/079/079550.json
atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
atlas/symbol_profiles/064/064350.json
atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv
atlas/symbol_profiles/047/047810.json
atlas/ohlcv_tradable_by_symbol_year/047/047810/2024.csv
atlas/symbol_profiles/272/272210.json
atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv
```

KAI `047810` was checked as a candidate but not used in the final 4-case set because it is better as a later second-pass aircraft/platform-delivery sub-archetype case. The final 4-case set emphasizes one major positive, two bridge-sensitive mixed positives, and one label-driven counterexample.

### 2.2 Data caveat

```text
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_windows_avoid_known_corporate_action_candidate_dates = true
```

All selected trigger windows are in 2024 and away from each selected symbol's listed corporate-action candidate dates. The raw/unadjusted caveat remains in the metadata because stock-web inherits FinanceData/marcap raw pricing.

## 3. Novelty / no-repeat check

```text
static_index_status = C03 rows 9 / need 21 to 30
conversation_local_C03_this_session = none before this file
new_independent_case_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
reused_case_count = 0
auto_selected_coverage_gap_static_index = C03 rows 9 -> 13 if accepted; still Priority 0, need 17 to 30
```

Novelty choices:

```text
- use 012450 as fully confirmed backlog-delivery-margin compounder
- use 079550 as missile/precision-defense export framework case with high-MAE guard
- use 064350 as land-system/platform export and operating leverage bridge case
- use 272210 as defense-system/space/ICT label false-positive guard
```

## 4. Case studies

### 4.1 C03-R1L105-01 — 012450 한화에어로스페이스: export backlog compounding with delivery/margin bridge

```text
symbol = 012450
name = 한화에어로스페이스
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
trigger_type = Stage3-Yellow
entry_date = 2024-02-27
entry_price = 179100
price_route = atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv
stock_web_profile_route = atlas/symbol_profiles/012/012450.json
```

Observed price path from stock-web:

```text
2024-02-27 close = 179100
2024-04-02 high = 245000
2024-06-19 high = 256000
2024-10-17 high = 395000
2024-11-12 high = 425000
```

Backtest result:

| horizon | max_high | min_low | MFE_pct | MAE_pct | note |
|---:|---:|---:|---:|---:|---|
| 30D | 245000 | 179200 | 36.80 | 0.06 | almost no adverse excursion after trigger close |
| 90D | 256000 | 179200 | 42.94 | 0.06 | export backlog thesis persists beyond first spike |
| 180D | 425000 | 179200 | 137.30 | 0.06 | full compounding case; Green may under-rank if delivery bridge is treated as generic backlog |

Interpretation: this is the cleanest C03 positive. The stock did not merely react to a defense headline. It became a backlog-to-delivery-to-margin compounder. The current calibrated profile blocks price-only 4B correctly, but C03 needs a route that allows Green if non-price bridge evidence is present and the drawdown profile stays controlled.

### 4.2 C03-R1L105-02 — 079550 LIG넥스원: sovereign customer/funding bridge matters

```text
symbol = 079550
name = LIG넥스원
trigger_type = Stage3-Yellow
entry_date = 2024-03-06
entry_price = 168500
price_route = atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
stock_web_profile_route = atlas/symbol_profiles/079/079550.json
```

Observed price path from stock-web:

```text
2024-03-06 close = 168500
2024-03-11 high = 191300
2024-05-23 low = 149900
2024-06-28 high = 221500
2024-11-08 high = 271500
```

Backtest result:

| horizon | max_high | min_low | MFE_pct | MAE_pct | note |
|---:|---:|---:|---:|---:|---|
| 30D | 191300 | 159500 | 13.53 | -5.34 | early positive, but not low-risk |
| 90D | 221500 | 149900 | 31.45 | -11.04 | material MFE coexists with painful shakeout |
| 180D | 271500 | 149900 | 61.13 | -11.04 | positive if bridge is sovereign-funded and backlog-visible |

Interpretation: LIG넥스원 shows why C03 needs a high-MAE guard rather than a simple binary positive. The eventual MFE is strong, but the signal must carry an explicit named-customer/funding/contract-conversion bridge. Without that bridge, the same chart shape could be misread as a generic geopolitical beta chase.

### 4.3 C03-R1L105-03 — 064350 현대로템: platform export plus operating leverage, but mixed exposure needs separation

```text
symbol = 064350
name = 현대로템
trigger_type = Stage2-Actionable
entry_date = 2024-02-22
entry_price = 34500
price_route = atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv
stock_web_profile_route = atlas/symbol_profiles/064/064350.json
```

Observed price path from stock-web:

```text
2024-02-22 close = 34500
2024-03-12 low = 29900
2024-06-17 high = 43000
2024-08-14 high = 54800
2024-10-18 high = 68000
```

Backtest result:

| horizon | max_high | min_low | MFE_pct | MAE_pct | note |
|---:|---:|---:|---:|---:|---|
| 30D | 39600 | 29900 | 14.78 | -13.33 | early signal has heavy shakeout |
| 90D | 43000 | 29900 | 24.64 | -13.33 | positive but requires patience and bridge confirmation |
| 180D | 68000 | 29900 | 97.10 | -13.33 | major MFE once backlog/platform theme is accepted |

Interpretation: this is not a clean immediate Green. It should be allowed as Stage2-Actionable or Yellow when export/platform backlog, delivery capacity, and margin bridge are visible, but the initial MAE is too high for an unguarded Green. C03 should separate defense export backlog from non-defense rail or mobility revenue so that mixed exposure does not receive an automatic defense premium.

### 4.4 C03-R1L105-04 — 272210 한화시스템: defense/space/system label false-positive guard

```text
symbol = 272210
name = 한화시스템
trigger_type = 4B-Watch
entry_date = 2024-03-06
entry_price = 18450
price_route = atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv
stock_web_profile_route = atlas/symbol_profiles/272/272210.json
```

Observed price path from stock-web:

```text
2024-03-06 close = 18450
2024-04-03 high = 18990
2024-04-26 high = 20000
2024-06-18 high = 22450
2024-06-05 low = 16810
```

Backtest result:

| horizon | max_high | min_low | MFE_pct | MAE_pct | note |
|---:|---:|---:|---:|---:|---|
| 30D | 18990 | 17050 | 2.93 | -7.59 | weak follow-through after label spike |
| 90D | 20000 | 16810 | 8.40 | -8.89 | insufficient for Green; mostly range-bound |
| 180D | 22450 | 16170 | 21.68 | -12.36 | positive MFE exists, but poor alignment versus risk |

Interpretation: this is the counterexample. Defense/space/systems wording alone should not become a C03 Green. The company may belong in the defense ecosystem, but if the event lacks firm export backlog, conversion schedule, customer funding, and margin bridge, the result is a price-only or label-driven 4B watch at best.

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C03-R1L105-01","symbol":"012450","name":"한화에어로스페이스","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_EXPORT_HEADLINE_PRICE_ONLY_FALSE_POSITIVE","trigger_type":"Stage3-Yellow","entry_date":"2024-02-27","entry_price":179100,"MFE_30D_pct":36.80,"MAE_30D_pct":0.06,"MFE_90D_pct":42.94,"MAE_90D_pct":0.06,"MFE_180D_pct":137.30,"MAE_180D_pct":0.06,"peak_price_180D":425000,"trough_price_180D":179200,"classification":"positive","source_price_route":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C03-R1L105-02","symbol":"079550","name":"LIG넥스원","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_EXPORT_HEADLINE_PRICE_ONLY_FALSE_POSITIVE","trigger_type":"Stage3-Yellow","entry_date":"2024-03-06","entry_price":168500,"MFE_30D_pct":13.53,"MAE_30D_pct":-5.34,"MFE_90D_pct":31.45,"MAE_90D_pct":-11.04,"MFE_180D_pct":61.13,"MAE_180D_pct":-11.04,"peak_price_180D":271500,"trough_price_180D":149900,"classification":"mixed_positive","source_price_route":"atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C03-R1L105-03","symbol":"064350","name":"현대로템","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_EXPORT_HEADLINE_PRICE_ONLY_FALSE_POSITIVE","trigger_type":"Stage2-Actionable","entry_date":"2024-02-22","entry_price":34500,"MFE_30D_pct":14.78,"MAE_30D_pct":-13.33,"MFE_90D_pct":24.64,"MAE_90D_pct":-13.33,"MFE_180D_pct":97.10,"MAE_180D_pct":-13.33,"peak_price_180D":68000,"trough_price_180D":29900,"classification":"mixed_positive","source_price_route":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C03-R1L105-04","symbol":"272210","name":"한화시스템","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_EXPORT_HEADLINE_PRICE_ONLY_FALSE_POSITIVE","trigger_type":"4B-Watch","entry_date":"2024-03-06","entry_price":18450,"MFE_30D_pct":2.93,"MAE_30D_pct":-7.59,"MFE_90D_pct":8.40,"MAE_90D_pct":-8.89,"MFE_180D_pct":21.68,"MAE_180D_pct":-12.36,"peak_price_180D":22450,"trough_price_180D":16170,"classification":"counterexample","source_price_route":"atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv","evidence_url_pending":true,"source_proxy_only":true}
```

## 6. Score-return alignment and current profile stress test

| case_id | profile proxy stage | observed result | alignment | residual error |
|---|---|---|---|---|
| C03-R1L105-01 | Stage3-Yellow/Green candidate | 180D MFE +137.30 / MAE +0.06 | strong positive | under-rank if treated as generic order backlog without defense export bridge |
| C03-R1L105-02 | Stage3-Yellow candidate | 180D MFE +61.13 / MAE -11.04 | positive but volatile | needs high-MAE guard and named government/funding bridge |
| C03-R1L105-03 | Stage2-Actionable / Yellow candidate | 180D MFE +97.10 / MAE -13.33 | mixed positive | mixed defense/rail exposure requires operating leverage and margin bridge separation |
| C03-R1L105-04 | 4B-Watch / block Green | 180D MFE +21.68 / MAE -12.36 | weak/risky | label-only defense-system vocabulary should not promote to Green |

Current calibrated profile stress-test result:

```text
stage2_actionable_evidence_bonus = useful but insufficient alone
stage3_yellow_total_min = should allow C03 positives when bridge evidence exists
stage3_green_total_min = should require C03-specific export/backlog/delivery/margin bridge
price_only_blowoff_blocks_positive_stage = strongly confirmed
full_4b_requires_non_price_evidence = strongly confirmed
hard_4c_thesis_break_routes_to_4c = unchanged
```

## 7. Proposed shadow rule candidate

```text
rule_id = C03_export_framework_backlog_delivery_margin_bridge_required
scope = canonical_archetype_specific
production_scoring_changed = false
shadow_weight_only = true
```

### 7.1 Positive bridge conditions

A C03 case may be promoted from Stage2-Actionable to Stage3-Yellow or Stage3-Green only if at least two of the following are present:

```text
1. named sovereign or quasi-sovereign customer
2. firm contract, framework converted to order, or disclosed backlog addition
3. delivery schedule / production slot / capacity lock / long-lead visibility
4. funding, export-credit, budget, or government-to-government route visible
5. margin or cash-conversion bridge, not only revenue headline
6. license / export control / offset / localization risk bounded
```

For Stage3-Green, require:

```text
C03_green_required_bridge_count >= 3
C03_delivery_or_backlog_conversion_required = true
C03_price_only_green_allowed = false
```

### 7.2 Negative / guard conditions

```text
C03_label_only_defense_theme_guard = true
C03_geopolitical_headline_without_customer_or_contract_cap = Stage2-Actionable or 4B-Watch
C03_high_MAE_guard_threshold = MAE_90D_pct <= -10 requires additional bridge confirmation before Green
C03_mixed_exposure_guard = if defense exposure is mixed with rail/ICT/space platform, require segment-level conversion evidence
C03_export_license_offset_delay_guard = unresolved license/offset/localization risk caps Green
```

## 8. Aggregate metric row

```json
{
  "row_type": "aggregate_metric",
  "schema_family": "v12_sector_archetype_residual",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "sample_trigger_count": 4,
  "positive_case_count": 1,
  "mixed_positive_count": 2,
  "counterexample_count": 1,
  "local_4b_watch_count": 1,
  "median_MFE_180D_pct": 79.12,
  "median_MAE_180D_pct": -11.70,
  "mean_MFE_180D_pct": 79.30,
  "mean_MAE_180D_pct": -9.17,
  "coverage_gap_static_index_before": 9,
  "coverage_gap_static_index_after_if_accepted": 13,
  "priority_bucket_after_if_accepted": "Priority 0"
}
```

## 9. Shadow weight row

```json
{
  "row_type": "shadow_weight",
  "rule_id": "C03_export_framework_backlog_delivery_margin_bridge_required",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "candidate_weight_delta": {
    "stage2_actionable_bridge_bonus": 0.5,
    "stage3_yellow_bridge_bonus": 1.0,
    "stage3_green_bridge_requirement": "hard_gate",
    "price_only_defense_label_penalty": -2.0,
    "high_MAE_without_bridge_green_block": true
  },
  "do_not_apply_now": true,
  "requires_batch_validation": true
}
```

## 10. Residual contribution summary

```text
new_axis_proposed = C03_export_framework_to_backlog_delivery_margin_bridge_required | C03_government_customer_funding_and_delivery_schedule_required | C03_license_offset_localization_delay_guard | C03_price_only_geopolitical_headline_high_MAE_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
```

This loop adds useful residual information because C03 behaves like a slow revenue conveyor belt rather than a simple event. A generic order backlog rule asks whether the order exists. C03 asks whether the shell has cleared the barrel: contract, customer, funding, permit, delivery slot, capacity, and margin all need to align.

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When a later coding agent batch-applies v12 residual rules, inspect this MD together with other accepted C03 files.

Task:
- Add a canonical-archetype-specific shadow rule candidate for C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.
- Do not change production scoring until batch validation confirms lift.
- Candidate rule name: C03_export_framework_backlog_delivery_margin_bridge_required.
- Require explicit bridge evidence for Stage3-Green:
  named sovereign customer, firm contract/framework conversion, delivery schedule/backlog conversion, funding visibility, margin/cash bridge, and bounded export/license/offset risk.
- Add a green block for defense/geopolitical/space/system label-only events without backlog conversion evidence.
- Add a high-MAE guard: if MAE_90D_pct <= -10, require extra bridge evidence before Green.
- Add mixed-exposure guard for names where defense is combined with rail, ICT, space, or platform/system segments.
- Preserve global rules: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c.
- Use this MD's trigger rows only if every row has entry_date, entry_price, trigger_type, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct, large_sector_id, and canonical_archetype_id.
```

## 12. Next recommended archetypes

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C24_BIO_TRIAL_DATA_EVENT_RISK
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```
