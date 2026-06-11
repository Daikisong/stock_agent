---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R6
selected_loop: 101
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_DIVIDEND_LABEL_FALSE_POSITIVE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R v12 Residual Research — R6 / L6 / C21

## 0. Selection & novelty check

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
static_index_rows = 6
static_index_need_to_30 = 24
conversation_local_recent_outputs_checked = C22, C25, C03, C16, C17, C23, C05, C24, C13, C12, C28, C19, C27, C02, C18, C26, C29, C30, C31, C32, C04, C15, C20
selected_after = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
selected_now = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

이번 C21 연구는 은행/금융지주의 **ROE·PBR·value-up·자본환원 headline**이 실제 주주환원 실행력과 capital flexibility로 이어지는지 확인한다. 핵심은 “낮은 PBR이라서 오른다”가 아니라, ROE 안정성·CET1/자본비율 여력·배당/자사주 실행·감익/충당금/정책 cap을 함께 본다는 점이다.

중복 방지상 이전 대화 산출물에서 C22 보험 rate cycle/CSM 축은 이미 DB손해보험·삼성생명·한화생명·한화손해보험으로 채웠으므로, 이번에는 보험이 아닌 은행/금융지주 중심으로 독립 케이스를 구성했다.

## 1. Validation scope

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
stock_web_price_atlas_access_required = true
```

가격 검증에 사용한 stock-web shard/profile:

```text
profiles:
- atlas/symbol_profiles/105/105560.json  # KB금융
- atlas/symbol_profiles/086/086790.json  # 하나금융지주
- atlas/symbol_profiles/055/055550.json  # 신한지주
- atlas/symbol_profiles/024/024110.json  # 기업은행

OHLCV:
- atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv
```

Profile caveat check:

```text
105560_KB금융: corporate_action_candidate_count=0, has_major_raw_discontinuity=false
086790_하나금융지주: corporate_action_candidate_count=0, has_major_raw_discontinuity=false
055550_신한지주: corporate_action_candidate_count=0, has_major_raw_discontinuity=false
024110_기업은행: corporate_action_candidate_count=4, historical candidates 1998/2000/2003 only; 2024 test window not blocked
```

Non-price evidence is intentionally marked as low-trust unless separately verified later:

```text
non_price_evidence_mode = source_proxy_only
evidence_url_pending = true
```

## 2. Archetype hypothesis

C21의 잔여 오류는 단순하다. 시장이 낮은 PBR을 보면 마치 눌린 스프링처럼 생각하지만, 은행주는 스프링 아래에 **자본규제·충당금·정책은행 cap·주주환원 실행력**이라는 무게추가 붙어 있다. 이 무게추가 가벼운 종목은 value-up headline 이후에도 rerating이 이어지고, 무게추가 무거운 종목은 첫 번째 점프만 남기고 다시 제자리로 돌아온다.

### Proposed C21-specific rule candidate

```text
C21_bank_valueup_capital_return_execution_bridge_required = true

Green/positive requires at least 3 of 5:
1. ROE level or revision is stable/improving, not just low PBR.
2. CET1/capital buffer or equivalent capital flexibility supports payout.
3. Explicit buyback/cancellation/dividend policy execution exists, not only “value-up theme”.
4. Credit-cost/asset-quality drag is not overwhelming the payout story.
5. 30D MFE is followed by 90D/180D persistence, not a one-week low-PBR squeeze.

Guardrail:
- low_PBR_plus_dividend_label_only must not unlock Stage3-Green.
- state_policy_bank_or_capital_constraint should cap at Stage2/Stage2-Actionable unless execution evidence is explicit.
- price_only_valueup_blowoff should remain local_4B_watch or Yellow, not full positive.
```

## 3. Case matrix

| case_id | symbol | name | entry_date | entry_price | classification | residual issue |
|---|---:|---|---:|---:|---|---|
| C21-KB-20240201 | 105560 | KB금융 | 2024-02-01 | 61,300 | positive | value-up rerating persisted into 180D; execution bridge should be rewarded |
| C21-HANA-20240201 | 086790 | 하나금융지주 | 2024-02-01 | 52,000 | positive | strong initial rerating but weaker than KB; still durable enough with capital-return bridge |
| C21-SHINHAN-20240201 | 055550 | 신한지주 | 2024-02-01 | 42,500 | mixed_positive | late 180D strength, but early drift and policy/execution gap require lower confidence than KB |
| C21-IBK-20240314 | 024110 | 기업은행 | 2024-03-14 | 15,700 | counterexample | late value-up/low-PBR chase without capital flexibility; sharp MAE after peak |

## 4. Trigger-level backtest rows

Assumption: windows use trading sessions available in the 2024 stock-web shard after `entry_date`. MFE uses window high vs entry close. MAE uses window low vs entry close. All prices are raw/unadjusted stock-web values.

```jsonl
{"row_type":"trigger","case_id":"C21-KB-20240201","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","symbol":"105560","name":"KB금융","trigger_type":"Stage2_Actionable_CapitalReturn_ValueUp_Bridge","entry_date":"2024-02-01","entry_price":61300,"price_source_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","evidence_mode":"source_proxy_only","evidence_url_pending":true,"classification":"positive","mfe_30d_pct":28.22,"mae_30d_pct":-5.87,"peak_30d_date":"2024-03-14","peak_30d_price":78600,"trough_30d_date":"2024-02-01","trough_30d_price":57700,"mfe_90d_pct":36.05,"mae_90d_pct":-5.87,"peak_90d_date":"2024-05-13","peak_90d_price":83400,"trough_90d_date":"2024-02-01","trough_90d_price":57700,"mfe_180d_pct":69.49,"mae_180d_pct":-5.87,"peak_180d_date":"2024-10-25","peak_180d_price":103900,"trough_180d_date":"2024-02-01","trough_180d_price":57700,"dedupe_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|105560|Stage2_Actionable_CapitalReturn_ValueUp_Bridge|2024-02-01"}
{"row_type":"trigger","case_id":"C21-HANA-20240201","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","symbol":"086790","name":"하나금융지주","trigger_type":"Stage2_Actionable_CapitalReturn_ValueUp_Bridge","entry_date":"2024-02-01","entry_price":52000,"price_source_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","evidence_mode":"source_proxy_only","evidence_url_pending":true,"classification":"positive","mfe_30d_pct":24.23,"mae_30d_pct":-7.88,"peak_30d_date":"2024-03-14","peak_30d_price":64600,"trough_30d_date":"2024-02-01","trough_30d_price":47900,"mfe_90d_pct":25.58,"mae_90d_pct":-7.88,"peak_90d_date":"2024-05-13","peak_90d_price":65300,"trough_90d_date":"2024-02-01","trough_90d_price":47900,"mfe_180d_pct":33.27,"mae_180d_pct":-7.88,"peak_180d_date":"2024-08-27","peak_180d_price":69300,"trough_180d_date":"2024-02-01","trough_180d_price":47900,"dedupe_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|086790|Stage2_Actionable_CapitalReturn_ValueUp_Bridge|2024-02-01"}
{"row_type":"trigger","case_id":"C21-SHINHAN-20240201","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","symbol":"055550","name":"신한지주","trigger_type":"Stage2_Actionable_CapitalReturn_ValueUp_Bridge","entry_date":"2024-02-01","entry_price":42500,"price_source_path":"atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv","evidence_mode":"source_proxy_only","evidence_url_pending":true,"classification":"mixed_positive","mfe_30d_pct":21.18,"mae_30d_pct":-6.24,"peak_30d_date":"2024-03-14","peak_30d_price":51500,"trough_30d_date":"2024-02-26","trough_30d_price":39850,"mfe_90d_pct":21.18,"mae_90d_pct":-6.24,"peak_90d_date":"2024-03-14","peak_90d_price":51500,"trough_90d_date":"2024-02-26","trough_90d_price":39850,"mfe_180d_pct":52.00,"mae_180d_pct":-6.24,"peak_180d_date":"2024-08-26","peak_180d_price":64600,"trough_180d_date":"2024-02-26","trough_180d_price":39850,"dedupe_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|055550|Stage2_Actionable_CapitalReturn_ValueUp_Bridge|2024-02-01"}
{"row_type":"trigger","case_id":"C21-IBK-20240314","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","symbol":"024110","name":"기업은행","trigger_type":"Stage3_Yellow_LowPBR_Dividend_Label_LateChase","entry_date":"2024-03-14","entry_price":15700,"price_source_path":"atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv","evidence_mode":"source_proxy_only","evidence_url_pending":true,"classification":"counterexample","mfe_30d_pct":1.97,"mae_30d_pct":-20.32,"peak_30d_date":"2024-03-15","peak_30d_price":16010,"trough_30d_date":"2024-04-15","trough_30d_price":12510,"mfe_90d_pct":1.97,"mae_90d_pct":-20.32,"peak_90d_date":"2024-03-15","peak_90d_price":16010,"trough_90d_date":"2024-04-15","trough_90d_price":12510,"mfe_180d_pct":1.97,"mae_180d_pct":-20.32,"peak_180d_date":"2024-03-15","peak_180d_price":16010,"trough_180d_date":"2024-04-15","trough_180d_price":12510,"dedupe_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|024110|Stage3_Yellow_LowPBR_Dividend_Label_LateChase|2024-03-14"}
```

## 5. Score-return alignment

| case_id | intended current profile stage | observed path | alignment result |
|---|---|---|---|
| C21-KB-20240201 | Stage2-Actionable → Stage3-Yellow candidate | 30D +28.2%, 90D +36.1%, 180D +69.5% | current profile under-rewards if capital-return execution bridge is not explicit |
| C21-HANA-20240201 | Stage2-Actionable | 30D +24.2%, 90D +25.6%, 180D +33.3% | good but lower persistence than KB; should remain Yellow unless execution evidence is strong |
| C21-SHINHAN-20240201 | Stage2-Actionable / mixed | 30D +21.2%, 90D flat vs first peak, 180D +52.0% | should not be penalized as simple low-PBR beta, but needs lag allowance |
| C21-IBK-20240314 | would be false Stage3-Yellow if low-PBR/dividend is over-weighted | MFE capped near +2%, MAE about -20% | current profile needs C21-specific state/policy-cap guard |

## 6. Current calibrated profile stress test

Current profile assumptions:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

### Raw component score simulation

```jsonl
{"row_type":"score_simulation","case_id":"C21-KB-20240201","symbol":"105560","stage2_base":66.0,"stage2_actionable_bonus":2.0,"revision_component":55.0,"capital_return_execution_component":17.0,"roe_pbr_bridge_component":14.0,"price_component":8.0,"evidence_quality_penalty":-3.0,"simulated_total":83.0,"simulated_stage":"Stage3-Yellow","profile_error":"under_green_without_c21_execution_axis","reason":"capital-return persistence and 180D price path are strong, but generic profile has no bank-specific payout execution bridge."}
{"row_type":"score_simulation","case_id":"C21-HANA-20240201","symbol":"086790","stage2_base":65.0,"stage2_actionable_bonus":2.0,"revision_component":51.0,"capital_return_execution_component":14.0,"roe_pbr_bridge_component":13.0,"price_component":6.5,"evidence_quality_penalty":-3.0,"simulated_total":78.5,"simulated_stage":"Stage3-Yellow","profile_error":"mostly_aligned_but_needs_persistence_filter","reason":"positive path but weaker 180D persistence than KB; should not become Green without explicit payout execution."}
{"row_type":"score_simulation","case_id":"C21-SHINHAN-20240201","symbol":"055550","stage2_base":63.0,"stage2_actionable_bonus":2.0,"revision_component":47.0,"capital_return_execution_component":12.0,"roe_pbr_bridge_component":12.0,"price_component":6.5,"evidence_quality_penalty":-3.0,"simulated_total":73.0,"simulated_stage":"Stage2-Actionable/Yellow-border","profile_error":"lagged_positive_can_be_misread_as_false_negative","reason":"30/90D stall would suppress score, but later 180D MFE shows delayed rerating; needs C21 lag allowance."}
{"row_type":"score_simulation","case_id":"C21-IBK-20240314","symbol":"024110","stage2_base":61.0,"stage2_actionable_bonus":2.0,"revision_component":35.0,"capital_return_execution_component":4.0,"roe_pbr_bridge_component":8.0,"price_component":2.0,"evidence_quality_penalty":-4.0,"state_policy_cap_penalty":-7.0,"simulated_total":54.0,"simulated_stage":"Stage2_or_reject","profile_error":"false_positive_if_low_pbr_dividend_overweighted","reason":"late chase had poor MFE/MAE; policy-bank/state-cap guard should block Stage3."}
```

## 7. 4B local vs full-window proximity split

```jsonl
{"row_type":"narrative_only","topic":"4B_split","case_id":"C21-KB-20240201","local_4b_watch":false,"full_4b_positive":true,"reason":"post-entry path made new 180D high months later; not a one-day value-up squeeze."}
{"row_type":"narrative_only","topic":"4B_split","case_id":"C21-HANA-20240201","local_4b_watch":false,"full_4b_positive":true,"reason":"initial spike was strong, but later August high validates persistence enough for positive classification."}
{"row_type":"narrative_only","topic":"4B_split","case_id":"C21-SHINHAN-20240201","local_4b_watch":true,"full_4b_positive":true,"reason":"first 90D was not decisive; later 180D strength saves it. Add lag-aware but execution-gated rule."}
{"row_type":"narrative_only","topic":"4B_split","case_id":"C21-IBK-20240314","local_4b_watch":true,"full_4b_positive":false,"reason":"entry was near late local high; next 30D/90D/180D MFE was capped while MAE expanded."}
```

## 8. Aggregate

```jsonl
{"row_type":"aggregate","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":2,"mixed_positive_count":1,"counterexample_count":1,"local_4b_watch_count":2,"current_profile_error_count":4,"auto_selected_coverage_gap_static_index":"C21 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30","diversity_score_summary":"C21 shortage fill; KB금융·하나금융지주·신한지주·기업은행; positive/mixed/counterexample balanced"}
```

## 9. Shadow rule proposal

```jsonl
{"row_type":"shadow_weight","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","proposal_id":"C21_bank_valueup_capital_return_execution_bridge_required","do_not_propose_new_weight_delta":false,"production_scoring_changed":false,"shadow_weight_only":true,"new_axis_proposed":["C21_bank_capital_return_execution_bridge_required","C21_low_PBR_dividend_label_false_positive_guard","C21_state_policy_bank_cap_guard","C21_lagged_rerating_allowed_if_execution_evidence_exists"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[]}
```

Implementation idea for later coding session, not now:

```text
If canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:
  require bank_capital_return_execution_bridge for Green.
  add + small bonus only when payout execution is explicit and ROE/CET1/revision are supportive.
  cap low_PBR + dividend-only + value-up headline at Stage2/Yellow unless execution bridge exists.
  add penalty for state/policy-bank cap or credit-cost overhang if evidence is not offset.
  preserve delayed-positive cases by allowing 180D persistence to rescue score only when execution bridge is present.
```

## 10. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C21_bank_capital_return_execution_bridge_required | C21_low_PBR_dividend_label_false_positive_guard | C21_state_policy_bank_cap_guard","why_it_matters":"Generic value-up scoring cannot distinguish bank rerating with actual capital-return execution from low-PBR/dividend late chase. KB/Hana show positive bridge; IBK shows false-positive cap; Shinhan shows lagged-positive caveat."}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent for Songdaiki/stock_agent. Do not use this handoff unless the user explicitly asks for batch implementation.

Input research MD:
- e2r_stock_web_v12_residual_round_R6_loop_101_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Add a C21-specific shadow rule candidate, not production by default.
2. Implement a bank/financial value-up bridge feature that requires:
   - capital return execution evidence,
   - ROE/PBR bridge quality,
   - capital adequacy/payout capacity proxy,
   - credit-cost or policy-cap guard.
3. Cap low-PBR + dividend-only cases at Stage2/Yellow unless execution evidence is explicit.
4. Preserve delayed-positive cases where 180D persistence is real, but only when the execution bridge exists.
5. Add tests using the four dedupe keys in this MD.
6. Do not alter global scoring weights unless multiple C21 MDs confirm the axis.

Expected rows:
- C21-KB-20240201 positive
- C21-HANA-20240201 positive
- C21-SHINHAN-20240201 mixed_positive
- C21-IBK-20240314 counterexample
```

## 12. Final metadata

```text
selected_round: R6
selected_loop: 101
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_DIVIDEND_LABEL_FALSE_POSITIVE
new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 4
calibration_usable trigger 수: 4
positive_case_count: 2
mixed_positive_count: 1
counterexample_count: 1
local_4b_watch_count: 2
current_profile_error_count: 4
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
next_recommended_archetypes: C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```
