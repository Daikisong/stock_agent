# E2R Stock-Web v12 Residual Research — R6 loop 98 / L6 / C21

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R6
selected_loop: 98
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_SMALL_BANK_VALUEUP_EVENT_SPIKE
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - ROE_PBR_valueup_execution_guardrail
  - CET1_capital_return_bridge_test
  - peer_transfer_guardrail
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

이번 파일은 `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` 전용 residual research다.

C21은 “저PBR”, “밸류업”, “은행주”, “금융주”라는 label을 곧바로 Green으로 바꾸는 bucket이 아니다. 이 archetype의 핵심은 ROE가 실제로 자본비용을 넘고, CET1/자본규제가 허락하는 범위 안에서 배당·자사주·소각이 반복 가능한지 확인하는 것이다.

```text
ROE/PBR/value-up/bank label
  → sustainable ROE above cost of equity
  → CET1 / capital buffer / risk-weighted asset control
  → dividend, buyback, cancellation execution
  → stock-web 1D OHLC forward path
```

금융주의 저PBR은 할인마트 가격표와 비슷하다. 싸다는 표시는 입구에 붙어 있지만, 계산대에서 진짜 남는지는 ROE·CET1·배당정책을 봐야 한다. C21은 “싸 보이는 은행”과 “자본을 실제로 돌려주는 은행”을 갈라야 한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["086790","316140","024110","006220"],"profile_paths":["atlas/symbol_profiles/086/086790.json","atlas/symbol_profiles/316/316140.json","atlas/symbol_profiles/024/024110.json","atlas/symbol_profiles/006/006220.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv","atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv","atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv"],"validation_scope":"2024 value-up trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C21 at 48 rows and asks for ROE/PBR/value-up plus actual capital-policy execution expansion.
- Existing registry shows C21 parsed through `R6 loop 97`.
- This output uses `R6 loop 98`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file focuses on bank-holding capital-return bridge versus policy-bank and small-bank event spike / peer-transfer risk.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C21-R6L98-01 | 086790 | 하나금융지주 | 2024-02-01 | 2024-02-01 | 52000 | 69300 | 47900 | 33.27% | -7.88% | Bank-holding value-up/CET1/capital-return bridge worked; leader candidate pending exact URLs. |
| C21-R6L98-02 | 316140 | 우리금융지주 | 2024-02-01 | 2024-02-01 | 14410 | 17100 | 13600 | 18.67% | -5.62% | Bank-holding capital-return path worked, but score should depend on CET1 and buyback/cancellation quality. |
| C21-R6L98-03 | 024110 | 기업은행 | 2024-02-01 | 2024-02-01 | 13130 | 16010 | 12530 | 21.93% | -4.57% | Policy-bank/value-up path produced MFE but capital discretion is different from pure bank-holding leaders. |
| C21-R6L98-04 | 006220 | 제주은행 | 2024-02-01 | 2024-02-01 | 13230 | 16050 | 8000 | 21.32% | -39.53% | Small-bank event spike / takeover-style beta; high-MAE counterexample without capital-return bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C21-R6L98-01","round":"R6","loop":"98","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_ROE_CET1_CAPITAL_RETURN_EXECUTION_LEADER","symbol":"086790","name":"하나금융지주","trigger_type":"bank_holding_roe_cet1_capital_return_execution_leader","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":52000,"peak_price":69300,"peak_date":"2024-08-27","trough_price":47900,"trough_date":"2024-02-01","mfe_pct":33.27,"mae_pct":-7.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_URLs","residual_flag":"positive_bank_holding_valueup_but_requires_CET1_payout_execution_bridge","dedupe_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|086790|bank_holding_roe_cet1_capital_return_execution_leader|2024-02-01"}
{"row_type":"trigger","case_id":"C21-R6L98-02","round":"R6","loop":"98","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_CAPITAL_RETURN_EXECUTION_FOLLOWTHROUGH","symbol":"316140","name":"우리금융지주","trigger_type":"bank_holding_capital_return_execution_followthrough","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":14410,"peak_price":17100,"peak_date":"2024-10-25","trough_price":13600,"trough_date":"2024-02-07","mfe_pct":18.67,"mae_pct":-5.62,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_CET1_URLs","residual_flag":"positive_but_green_requires_buyback_cancellation_and_CET1_buffer","dedupe_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|316140|bank_holding_capital_return_execution_followthrough|2024-02-01"}
{"row_type":"trigger","case_id":"C21-R6L98-03","round":"R6","loop":"98","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"POLICY_BANK_VALUEUP_DIVIDEND_CAPITAL_DISCRETION_GUARD","symbol":"024110","name":"기업은행","trigger_type":"policy_bank_valueup_dividend_capital_discretion_guard","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":13130,"peak_price":16010,"peak_date":"2024-03-15","trough_price":12530,"trough_date":"2024-02-01","mfe_pct":21.93,"mae_pct":-4.57,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_policy_bank_guard","residual_flag":"positive_valueup_path_but_policy_bank_capital_discretion_differs_from_bank_holding_leaders","dedupe_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|024110|policy_bank_valueup_dividend_capital_discretion_guard|2024-02-01"}
{"row_type":"trigger","case_id":"C21-R6L98-04","round":"R6","loop":"98","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BANK_VALUEUP_EVENT_SPIKE_HIGH_MAE_COUNTEREXAMPLE","symbol":"006220","name":"제주은행","trigger_type":"small_bank_valueup_event_spike_high_mae","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":13230,"peak_price":16050,"peak_date":"2024-02-01","trough_price":8000,"trough_date":"2024-10-25","mfe_pct":21.32,"mae_pct":-39.53,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Event-cap_or_hard_4B_watch_not_Green","residual_flag":"counterexample_bank_label_event_spike_without_ROE_CET1_capital_return_bridge","dedupe_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|006220|small_bank_valueup_event_spike_high_mae|2024-02-01"}
```

## 6. Score-return alignment

### 6.1 Bank-holding positive family

`086790` and `316140` show the constructive C21 family. The first signal is value-up/low-PBR recognition, but the durable signal is not the label. The durable signal is ROE persistence plus CET1 capacity plus visible dividend/buyback/cancellation execution. 하나금융 had stronger MFE; 우리금융 had moderate but still useful follow-through.

### 6.2 Policy-bank boundary

`024110` is positive but should be scored with a boundary guard. The return path worked, yet policy-bank capital discretion is not identical to bank-holding shareholder-return discretion. This can be a Stage2-to-Yellow candidate but should not inherit full leader-bank Green without evidence of payout autonomy and CET1 buffer.

### 6.3 Small-bank false Stage2

`006220` is the event-spike trap. It had a large same-day high, which can inflate MFE, but the subsequent path was dominated by MAE. The model should not treat small-bank/takeover-style volatility as the same phenomenon as bank-holding capital-return execution.

## 7. Raw component score simulation

| symbol | ROE/PBR evidence | CET1/capital buffer | capital-return execution | price confirmation | MAE/logic guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 086790 | 22 | 20 | 20 | 22 | -4 | 80 | Stage3-Yellow/Green candidate |
| 316140 | 20 | 17 | 16 | 16 | -3 | 66 | Stage3-Yellow candidate |
| 024110 | 18 | 13 | 12 | 17 | -5 | 55 | Stage2/Yellow with policy-bank guard |
| 006220 | 9 | 3 | 2 | 5 | -20 | -1 | Event-cap / hard 4B watch |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c21_valueup_requires_roe_cet1_capital_return_bridge","scope":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","candidate_action":"stage2_required_bridge","rule":"Do not promote low-PBR/value-up/financial labels above Stage2 unless sustainable ROE, CET1/capital buffer, and visible dividend/buyback/cancellation execution are present.","supporting_cases":["006220"],"counterbalanced_by":["086790","316140","024110"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c21_bank_holding_leader_positive_delta","scope":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Bank-holding names with ROE above capital cost, CET1 buffer, and explicit shareholder-return execution can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["086790","316140"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c21_policy_bank_boundary_guard","scope":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","candidate_action":"canonical_boundary_guard","rule":"Policy banks can participate in value-up trades, but should not receive the same Green treatment as bank-holding leaders unless payout autonomy and capital-return discretion are independently verified.","supporting_cases":["024110"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c21_small_bank_event_spike_high_mae_guard","scope":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","candidate_action":"local_4b_watch_guard","rule":"Small-bank price spikes with takeover/speculative beta and no ROE/CET1/capital-return bridge should be capped at event-cap or hard 4B watch even when same-day MFE is large.","supporting_cases":["006220"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","round":"R6","loop":"98","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C21 should separate bank-holding capital-return execution from generic low-PBR/value-up bank label and small-bank event-spike beta.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","canonical_boundary_guard","local_4b_watch_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sample_count":4,"avg_mfe_pct":23.80,"avg_mae_pct":-14.40,"median_mfe_pct":21.63,"median_mae_pct":-6.75,"interpretation":"C21 works well for verified bank-holding capital-return execution, but small-bank label/event spikes can create misleading MFE and severe MAE."}
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
  - historical corporate-action profile caveats, where present, are outside the local 2024 trigger windows used here
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C21 R6 loop 98 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c21_valueup_requires_roe_cet1_capital_return_bridge -> stage2_required_bridge
  2. c21_bank_holding_leader_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c21_policy_bank_boundary_guard -> canonical_boundary_guard
  4. c21_small_bank_event_spike_high_mae_guard -> local_4b_watch_guard

Expected behavior:
- Low-PBR/value-up vocabulary alone should not create Green.
- Sustainable ROE, CET1/capital buffer, dividend/buyback/cancellation execution can justify Stage3-Yellow/Green.
- Policy-bank value-up paths require payout-autonomy guardrails.
- Small-bank event spikes should not be credited as C21 capital-return success.
```
