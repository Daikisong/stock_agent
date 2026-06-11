# E2R Stock-Web v12 Residual Research — R1 loop 99 / L1 / C05

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 99
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: CONSTRUCTION_EPC_ORDER_MARGIN_WORKING_CAPITAL_BRIDGE_VS_RESIDENTIAL_POLICY_BETA_AND_CHANNEL_BREAK
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - margin_gap_guardrail
  - working_capital_guardrail
  - high_MAE_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` 전용 residual research다.

C05는 “대형 EPC 계약”, “플랜트 수주”, “건설 수주”, “해외 프로젝트”라는 headline을 그대로 Green으로 올리는 bucket이 아니다. 이 archetype의 핵심은 계약 금액이 매출·마진·현금흐름으로 내려오는 과정에서 누가 원가초과와 working capital gap을 흡수하는지 확인하는 것이다.

```text
mega EPC / construction / plant / project headline
  → contract scope / cost escalation / change order protection
  → billing schedule / working capital / unbilled receivable control
  → gross margin / OPM / EPS revision bridge
  → stock-web 1D OHLC forward path
```

EPC 계약은 큰 배를 수주한 것과 비슷하다. 배를 띄우는 것과 목적지에 이윤을 싣고 도착하는 것은 다르다. 철판값·인건비·공기 지연·미청구공사가 배 밑으로 물처럼 들어오면, 계약 headline은 곧바로 margin gap으로 바뀐다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["006360","375500","294870","097230"],"profile_paths":["atlas/symbol_profiles/006/006360.json","atlas/symbol_profiles/375/375500.json","atlas/symbol_profiles/294/294870.json","atlas/symbol_profiles/097/097230.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C05 at 33 rows and asks for mega EPC contract, cost overrun, working capital, and margin-gap expansion.
- Registry shows C05 parsed through `R1 loop 98`.
- This output uses `R1 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file intentionally avoids the earlier Samsung E&A / Hyundai E&C / Doosan Enerbility cluster and uses a different construction/EPC margin-gap family.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C05-R1L99-01 | 006360 | GS건설 | 2024-04-30 | 2024-04-30 | 16480 | 21750 | 14460 | 31.98% | -12.26% | Construction margin-recovery path worked, but only with material drawdown and strict cost/working-capital proof. |
| C05-R1L99-02 | 375500 | DL이앤씨 | 2024-06-13 | 2024-06-13 | 35200 | 39500 | 28600 | 12.22% | -18.75% | Project/EPC headline spike was mostly event-cap unless margin and billing bridge followed. |
| C05-R1L99-03 | 294870 | HDC현대산업개발 | 2024-07-12 | 2024-07-12 | 18350 | 28200 | 17700 | 53.68% | -3.54% | Residential construction/policy beta was strong, but it is not clean EPC unless margin/revenue bridge is verified. |
| C05-R1L99-04 | 097230 | HJ중공업 | 2024-06-03 | 2024-06-03 | 3460 | 3785 | 2180 | 9.39% | -36.99% | Contractor/project optionality failed after a small MFE; high-MAE counterexample for project-label Stage2. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C05-R1L99-01","round":"R1","loop":"99","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_MARGIN_RECOVERY_WORKING_CAPITAL_BRIDGE_HIGH_MAE","symbol":"006360","name":"GS건설","trigger_type":"construction_margin_recovery_working_capital_bridge","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":16480,"peak_price":21750,"peak_date":"2024-08-27","trough_price":14460,"trough_date":"2024-06-18","mfe_pct":31.98,"mae_pct":-12.26,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_with_margin_bridge","residual_flag":"positive_mfe_but_requires_cost_working_capital_bridge_before_green","dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|construction_margin_recovery_working_capital_bridge|2024-04-30"}
{"row_type":"trigger","case_id":"C05-R1L99-02","round":"R1","loop":"99","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_PROJECT_EVENT_CAP_WITHOUT_BILLING_MARGIN_BRIDGE","symbol":"375500","name":"DL이앤씨","trigger_type":"epc_project_event_cap_without_billing_margin_bridge","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":35200,"peak_price":39500,"peak_date":"2024-06-13","trough_price":28600,"trough_date":"2024-08-05","mfe_pct":12.22,"mae_pct":-18.75,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_event_cap_not_Green","residual_flag":"headline_spike_decayed_without_margin_working_capital_bridge","dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|epc_project_event_cap_without_billing_margin_bridge|2024-06-13"}
{"row_type":"trigger","case_id":"C05-R1L99-03","round":"R1","loop":"99","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"RESIDENTIAL_CONSTRUCTION_POLICY_BETA_MARGIN_RECOVERY_ADJACENT","symbol":"294870","name":"HDC현대산업개발","trigger_type":"residential_construction_policy_beta_margin_recovery_adjacent","trigger_date":"2024-07-12","entry_date":"2024-07-12","entry_price":18350,"peak_price":28200,"peak_date":"2024-08-26","trough_price":17700,"trough_date":"2024-07-12","mfe_pct":53.68,"mae_pct":-3.54,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_but_not_clean_EPC","residual_flag":"positive_path_but_should_not_be_counted_as_clean_EPC_without_margin_bridge","dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|residential_construction_policy_beta_margin_recovery_adjacent|2024-07-12"}
{"row_type":"trigger","case_id":"C05-R1L99-04","round":"R1","loop":"99","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONTRACTOR_PROJECT_OPTIONALITY_SMALL_MFE_HIGH_MAE_COUNTEREXAMPLE","symbol":"097230","name":"HJ중공업","trigger_type":"contractor_project_optionality_small_mfe_high_mae","trigger_date":"2024-06-03","entry_date":"2024-06-03","entry_price":3460,"peak_price":3785,"peak_date":"2024-06-19","trough_price":2180,"trough_date":"2024-10-31","mfe_pct":9.39,"mae_pct":-36.99,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4C_watch","residual_flag":"project_label_small_mfe_then_deep_mae_without_cash_margin_bridge","dedupe_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|097230|contractor_project_optionality_small_mfe_high_mae|2024-06-03"}
```

## 6. Score-return alignment

### 6.1 Constructive but not automatic Green

`006360` and `294870` show why C05 cannot be simply bearish on construction/project names. When the market sees margin recovery, cost normalization, or policy-supported construction demand, the upside can be meaningful. But the scoring should ask whether the move is driven by a true EPC/order-margin bridge or by residential beta.

### 6.2 Headline spike and working-capital gap

`375500` is the classic C05 event-cap pattern. The event day had a tradable spike, but the forward path quickly exposed that headline size alone is not enough. If billing schedule, change-order protection, cost-to-complete, and working-capital discipline are missing, C05 should stop at Stage2/Yellow watch.

### 6.3 Hard counterexample family

`097230` is a stronger warning. A contractor/project optionality narrative created a small MFE, but then the path was dominated by MAE. This is the archetype’s trapdoor: project labels can look like backlog until cash conversion breaks.

## 7. Raw component score simulation

| symbol | contract/project evidence | margin bridge | working-capital/billing bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 006360 | 18 | 16 | 12 | 18 | -6 | 58 | Stage3-Yellow candidate |
| 375500 | 17 | 8 | 5 | 7 | -9 | 28 | Event-cap / local 4B watch |
| 294870 | 14 | 12 | 7 | 24 | -2 | 55 | Adjacent Stage3-Yellow, not clean EPC |
| 097230 | 13 | 4 | 3 | 4 | -15 | 9 | Hard counterexample / 4C watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c05_epc_requires_margin_working_capital_bridge","scope":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","candidate_action":"stage2_required_bridge","rule":"Do not promote EPC/construction/project headlines above Stage2 unless margin bridge, cost-to-complete protection, billing schedule, change order, or working-capital control is visible.","supporting_cases":["375500","097230"],"counterbalanced_by":["006360","294870"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c05_event_spike_high_mae_guardrail","scope":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","candidate_action":"local_4b_watch_guard","rule":"If contract/project MFE is paired with deep MAE and no verified non-price bridge, cap at event-cap/local 4B watch until billing or margin evidence arrives.","supporting_cases":["375500","097230"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c05_residential_policy_beta_not_clean_epc","scope":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","candidate_action":"canonical_boundary_guard","rule":"Residential construction policy beta can be positive, but should not be counted as clean EPC mega-contract success unless margin and cash conversion mechanics match C05.","supporting_cases":["294870"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c05_cost_working_capital_positive_delta","scope":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","candidate_action":"stage3_yellow_candidate_delta","rule":"If construction/EPC names show margin recovery plus cost-to-complete and working-capital control, allow stronger Stage3-Yellow treatment, but require URL-verified non-price evidence before Green.","supporting_cases":["006360"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","round":"R1","loop":"99","positive_rows":2,"counterexample_rows":2,"new_symbol_count":4,"primary_residual":"C05 needs sharper separation between project/contract headline, residential construction beta, and true EPC margin/working-capital bridge.","candidate_patch_axes":["stage2_required_bridge","local_4b_watch_guard","canonical_boundary_guard","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","sample_count":4,"avg_mfe_pct":26.82,"avg_mae_pct":-17.89,"median_mfe_pct":22.10,"median_mae_pct":-15.51,"interpretation":"C05 can produce strong upside when margin recovery is real, but EPC/project labels need strict billing, working-capital, and cost-to-complete proof to avoid event-cap/high-MAE traps."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - local 2024 OHLC rows were checked from stock-web tradable shards
  - historical corporate-action profile caveats are outside the local 2024 trigger windows used here
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C05 R1 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c05_epc_requires_margin_working_capital_bridge -> stage2_required_bridge
  2. c05_event_spike_high_mae_guardrail -> local_4b_watch_guard
  3. c05_residential_policy_beta_not_clean_epc -> canonical_boundary_guard
  4. c05_cost_working_capital_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- EPC/contract/construction vocabulary alone should not create Green.
- Cost-to-complete, billing schedule, change-order protection, working-capital control, OPM, or EPS revision can justify Stage3-Yellow.
- Residential policy beta must not be credited as clean EPC mega-contract success unless margin/cash mechanics match C05.
- Contractor/project names with small MFE and deep MAE should become event-cap/local 4B watch or 4C watch.
```
