---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 99
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
created_at_kst: 2026-06-06
---

# E2R v12 residual research — R7 / L7 / C24 BIO_TRIAL_DATA_EVENT_RISK

## 0. Executive summary

이번 연구는 `C24_BIO_TRIAL_DATA_EVENT_RISK`의 30-row 최소 안정권을 채우기 위한 Priority 0 보강이다.
No-Repeat Index 기준 C24는 27 rows이며, 30-row minimum까지 3 rows가 부족했다. 따라서 이번 루프는 **새 symbol 3개 / 새 trigger family 3개 / positive 1개 + counterexample 2개**로 구성했다.

C24의 핵심은 임상/데이터/승인 전 이벤트가 실제 value bridge인지, 아니면 단순한 pre-approval price spike인지 구분하는 것이다. 바이오 이벤트는 불꽃놀이처럼 보인다. 불꽃이 높게 터질수록 더 밝아 보이지만, 그 빛이 발전소가 아니라 화약이면 꺼진 뒤 남는 것은 어둠과 낙폭이다. 이 아키타입에서는 “데이터 → endpoint quality → regulatory/commercial path → funding runway”로 이어지는 다리 없는 가격 반응을 positive stage로 세지 않는 것이 핵심이다.

## 1. Scope and novelty check

```text
selected_round = R7
selected_loop = 99
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C

novelty_basis = V12_Research_No_Repeat_Index.md
priority_bucket = Priority 0
pre_loop_rows = 27
need_to_30 = 3
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

### Duplicate policy

Hard duplicate key used for this MD:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This loop avoids repeating the previous C24 corpus by using:

```text
028300 / stage3_yellow_preapproval_data_event_blowoff / 2024-03-08
950220 / stage2_actionable_clinical_data_event_without_conversion_bridge / 2024-04-30
298380 / stage2_actionable_biotech_data_platform_validation / 2024-02-23
```

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_source":"Songdaiki/stock-web","manifest_path":"atlas/manifest.json","source_name":"FinanceData/marcap","price_adjustment_status":"raw_unadjusted_marcap","price_basis":"tradable_raw","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows blocked by default."}
```

Symbol profile checks:

```jsonl
{"row_type":"price_source_validation","symbol":"028300","name":"HLB","profile_path":"atlas/symbol_profiles/028/028300.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","status_inferred":"active_like","corporate_action_window_used":false}
{"row_type":"price_source_validation","symbol":"950220","name":"네오이뮨텍","profile_path":"atlas/symbol_profiles/950/950220.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv","status_inferred":"active_like","corporate_action_window_used":false}
{"row_type":"price_source_validation","symbol":"298380","name":"에이비엘바이오","profile_path":"atlas/symbol_profiles/298/298380.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv","status_inferred":"active_like","corporate_action_window_used":false}
```

## 3. Case table

| case_id | symbol | name | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE % | MAE % | peak DD % | classification |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C24_R7_L99_028300_HLB_2024_PRE_APPROVAL_DATA_SPIKE_TO_CRL_BREAK | 028300 | HLB | 2024-03-08 | 98000 | 2024-03-26 | 129000 | 2024-05-20 | 47000 | 31.63 | -52.04 | -63.57 | counterexample_hard_4c_preapproval_trial_regulatory_event_break |
| C24_R7_L99_950220_NEOT_2024_DATA_EVENT_SPIKE_FADE | 950220 | 네오이뮨텍 | 2024-04-30 | 1830 | 2024-05-14 | 2120 | 2024-07-29 | 1412 | 15.85 | -22.84 | -33.40 | counterexample_data_event_spike_decay_high_mae |
| C24_R7_L99_298380_ABLBIO_2024_DATA_PLATFORM_EVENT_POSITIVE_BRIDGE | 298380 | 에이비엘바이오 | 2024-02-23 | 22500 | 2024-03-13 | 30500 | 2024-04-08 | 22000 | 35.56 | -2.22 | -27.87 | positive_data_event_with_platform_validation_and_limited_mae |

## 4. Case notes

### 4.1 HLB — pre-approval data/regulatory optimism to hard 4C

HLB is the cleanest negative C24 template in this batch. The entry is not a current recommendation and not a live signal. It is a historical trigger row used to test whether the current calibrated profile still grants too much credit to a pre-approval data/regulatory event when the non-price bridge is incomplete.

The 2024 price path shows a sharp run from the March entry zone into a late-March high, followed by a May hard break. This is exactly the kind of path C24 should punish: a pre-approval event can behave like Stage3-Yellow in the chart, but the thesis still depends on binary regulatory survival. In E2R terms, this should be a 4B/4C guardrail stress case, not a positive evidence case.

### 4.2 NeoImmuneTech — clinical-data pulse without durable conversion bridge

NeoImmuneTech shows a smaller but useful C24 counterexample. The event pulse produced short MFE, yet the signal lost structure and moved into high-MAE decay. The important distinction is that the chart did not need to collapse immediately to become a bad Stage2-Actionable candidate. The signal failed because the event did not turn into a durable endpoint-quality/regulatory/partner/funding bridge.

For C24, this is the difference between a match and a lamp. A match is bright for a moment; a lamp has a power line. This case is the match.

### 4.3 ABL Bio — platform/data validation with limited early MAE

ABL Bio is the positive control. Its entry is still a clinical/platform-data event proxy, so it should not unlock Stage3-Green. However, the price path shows a better shape than the two counterexamples: MFE was strong, MAE was shallow, and the signal behaved like a tradable Stage2-Actionable bridge rather than a naked binary blowoff.

This is not a claim that every ABL Bio event is C24-positive. It is a narrow rule: when data/platform validation has recognizable follow-through and limited early MAE, Stage2-Actionable may be allowed. Stage3-Green still needs stronger evidence.

## 5. Machine-readable case rows

```jsonl
{"row_type": "case", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C", "case_id": "C24_R7_L99_028300_HLB_2024_PRE_APPROVAL_DATA_SPIKE_TO_CRL_BREAK", "symbol": "028300", "name": "HLB", "entry_date": "2024-03-08", "entry_close": 98000, "peak_date": "2024-03-26", "peak_high": 129000, "trough_date": "2024-05-20", "trough_low": 47000, "mfe_90d_pct": 31.6327, "mae_90d_pct": -52.0408, "peak_to_trough_drawdown_pct": -63.5659, "classification": "counterexample_hard_4c_preapproval_trial_regulatory_event_break", "evidence_family": "preapproval_trial_regulatory_data_event_proxy_only", "path_label": "approval_expected_price_spike_to_hard_4c", "calibration_usable": true, "source_quality": "source_proxy_only", "evidence_url_status": "pending"}
{"row_type": "case", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C", "case_id": "C24_R7_L99_950220_NEOT_2024_DATA_EVENT_SPIKE_FADE", "symbol": "950220", "name": "네오이뮨텍", "entry_date": "2024-04-30", "entry_close": 1830, "peak_date": "2024-05-14", "peak_high": 2120, "trough_date": "2024-07-29", "trough_low": 1412, "mfe_90d_pct": 15.847, "mae_90d_pct": -22.8415, "peak_to_trough_drawdown_pct": -33.3962, "classification": "counterexample_data_event_spike_decay_high_mae", "evidence_family": "clinical_data_poster_press_release_proxy_only", "path_label": "data_event_spike_then_decay", "calibration_usable": true, "source_quality": "source_proxy_only", "evidence_url_status": "pending"}
{"row_type": "case", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C", "case_id": "C24_R7_L99_298380_ABLBIO_2024_DATA_PLATFORM_EVENT_POSITIVE_BRIDGE", "symbol": "298380", "name": "에이비엘바이오", "entry_date": "2024-02-23", "entry_close": 22500, "peak_date": "2024-03-13", "peak_high": 30500, "trough_date": "2024-04-08", "trough_low": 22000, "mfe_90d_pct": 35.5556, "mae_90d_pct": -2.2222, "peak_to_trough_drawdown_pct": -27.8689, "classification": "positive_data_event_with_platform_validation_and_limited_mae", "evidence_family": "biotech_platform_data_event_with_followthrough_proxy_only", "path_label": "data_platform_validation_to_tradeable_mfe", "calibration_usable": true, "source_quality": "source_proxy_only", "evidence_url_status": "pending"}
```

## 6. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C", "trigger_id": "C24_R7_L99_028300_HLB_2024_PRE_APPROVAL_DATA_SPIKE_TO_CRL_BREAK_TRIGGER", "symbol": "028300", "name": "HLB", "trigger_type": "stage3_yellow_preapproval_data_event_blowoff", "trigger_date": "2024-03-08", "entry_date": "2024-03-08", "entry_price": 98000, "mfe_90d_pct": 31.6327, "mae_90d_pct": -52.0408, "peak_date": "2024-03-26", "peak_price": 129000, "trough_date": "2024-05-20", "trough_price": 47000, "classification": "counterexample_hard_4c_preapproval_trial_regulatory_event_break", "current_profile_stage": "Stage3-Yellow", "shadow_rule_stage": "4C", "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|028300|stage3_yellow_preapproval_data_event_blowoff|2024-03-08", "calibration_usable": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C", "trigger_id": "C24_R7_L99_950220_NEOT_2024_DATA_EVENT_SPIKE_FADE_TRIGGER", "symbol": "950220", "name": "네오이뮨텍", "trigger_type": "stage2_actionable_clinical_data_event_without_conversion_bridge", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 1830, "mfe_90d_pct": 15.847, "mae_90d_pct": -22.8415, "peak_date": "2024-05-14", "peak_price": 2120, "trough_date": "2024-07-29", "trough_price": 1412, "classification": "counterexample_data_event_spike_decay_high_mae", "current_profile_stage": "Stage2-Actionable", "shadow_rule_stage": "Stage2-Watch", "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|950220|stage2_actionable_clinical_data_event_without_conversion_bridge|2024-04-30", "calibration_usable": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C", "trigger_id": "C24_R7_L99_298380_ABLBIO_2024_DATA_PLATFORM_EVENT_POSITIVE_BRIDGE_TRIGGER", "symbol": "298380", "name": "에이비엘바이오", "trigger_type": "stage2_actionable_biotech_data_platform_validation", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 22500, "mfe_90d_pct": 35.5556, "mae_90d_pct": -2.2222, "peak_date": "2024-03-13", "peak_price": 30500, "trough_date": "2024-04-08", "trough_price": 22000, "classification": "positive_data_event_with_platform_validation_and_limited_mae", "current_profile_stage": "Stage2-Actionable", "shadow_rule_stage": "Stage2-Actionable", "dedupe_key": "C24_BIO_TRIAL_DATA_EVENT_RISK|298380|stage2_actionable_biotech_data_platform_validation|2024-02-23", "calibration_usable": true}
```

## 7. Score simulation rows

```jsonl
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "symbol": "028300", "entry_date": "2024-03-08", "raw_component_score_breakdown": {"evidence_quality": 10, "data_endpoint_quality": 8, "regulatory_path_visibility": 3, "partner_or_platform_validation": 4, "funding_runway": 4, "price_action_quality": 18, "red_team_risk_penalty": -22}, "current_profile_total_proxy": 82.0, "current_profile_stage": "Stage3-Yellow", "shadow_rule_stage": "4C", "profile_error_flag": true, "profile_error_type": "binary_event_overcredit"}
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "symbol": "950220", "entry_date": "2024-04-30", "raw_component_score_breakdown": {"evidence_quality": 8, "data_endpoint_quality": 7, "regulatory_path_visibility": 4, "partner_or_platform_validation": 3, "funding_runway": 4, "price_action_quality": 12, "red_team_risk_penalty": -14}, "current_profile_total_proxy": 72.0, "current_profile_stage": "Stage2-Actionable", "shadow_rule_stage": "Stage2-Watch", "profile_error_flag": true, "profile_error_type": "binary_event_overcredit"}
{"row_type": "score_simulation", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "99", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "symbol": "298380", "entry_date": "2024-02-23", "raw_component_score_breakdown": {"evidence_quality": 15, "data_endpoint_quality": 14, "regulatory_path_visibility": 8, "partner_or_platform_validation": 14, "funding_runway": 8, "price_action_quality": 12, "red_team_risk_penalty": -5}, "current_profile_total_proxy": 76.0, "current_profile_stage": "Stage2-Actionable", "shadow_rule_stage": "Stage2-Actionable", "profile_error_flag": false, "profile_error_type": "none"}
```

## 8. Aggregate metric rows

```jsonl
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","case_count":3,"trigger_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"median_mfe_90d_pct":31.6327,"median_mae_90d_pct":-22.8415,"worst_mae_90d_pct":-52.0408,"positive_to_counterexample_balance":"1:2","coverage_gap_filled_to_30_minimum":true}
```

## 9. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_axis_proposed":"c24_endpoint_partner_regulatory_runway_bridge_required_for_stage2_actionable_shadow_only","shadow_rule":"For C24, clinical/data/pre-approval event price spikes must remain Stage2-Watch or 4B/4C watch unless endpoint quality, regulatory path, partner/platform validation, and funding runway are all present. Stage2-Actionable can be allowed only when early MAE is controlled and non-price validation exists. Stage3-Green remains blocked by default for binary clinical events.","do_not_propose_new_weight_delta":false,"production_scoring_changed":false}
```

### Rule in plain English

C24 should not ask, “Did the chart move?”
It should ask, “Did the data event earn a bridge?”

A C24 event needs four planks:

```text
1. endpoint quality or interpretable clinical/platform data
2. regulatory path visibility or clear next milestone
3. partner/platform validation or commercial sponsor quality
4. funding runway / dilution risk control
```

If those planks are missing, price momentum is a bridge painted on water. It can be traded as volatility, but it should not be promoted as structural Stage2-Actionable or Stage3-Green.

## 10. 4B local vs full-window split

```jsonl
{"row_type":"stage_transition_summary","symbol":"028300","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","entry_date":"2024-03-08","local_4b_watch":true,"full_window_4b":true,"hard_4c":true,"reason":"pre-approval data/regulatory event ran first, then collapsed after thesis break; hard 4C should override price-only strength"}
{"row_type":"stage_transition_summary","symbol":"950220","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","entry_date":"2024-04-30","local_4b_watch":true,"full_window_4b":false,"hard_4c":false,"reason":"short event pulse with later high-MAE decay; watch-only unless endpoint/regulatory/partner bridge appears"}
{"row_type":"stage_transition_summary","symbol":"298380","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","entry_date":"2024-02-23","local_4b_watch":false,"full_window_4b":false,"hard_4c":false,"reason":"data/platform validation path produced controlled MAE and tradeable MFE; Stage2-Actionable allowed but Green blocked"}
```

## 11. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_found":true,"current_profile_error_count":2,"new_axis_proposed":"c24_endpoint_partner_regulatory_runway_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C24 pre-approval clinical/data event spikes","existing_axis_weakened":null}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","coverage_effect":"C24 moves from 27 rows toward 30-row minimum with 3 calibration-usable cases","next_recommended_archetypes":["C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION"]}
```

## 12. Validation caveats

- This is historical calibration research only.
- It is not a current stock recommendation.
- It does not patch `stock_agent` production scoring.
- Evidence URL collection is deferred; this MD marks the evidence as `source_proxy_only` / `evidence_url_pending`.
- All price rows are from `Songdaiki/stock-web` tradable raw OHLCV shards.
- C24 positive cases should not unlock Stage3-Green by themselves, because binary clinical event risk remains structurally different from orderbook/margin/cash-flow evidence.

## 13. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent in a later batch implementation session.

Do not rerun this research. Read this MD as one v12 residual research artifact.

Task:
1. Ingest the machine-readable JSONL rows in this file.
2. Preserve the canonical scope:
   - large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
   - canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
   - fine_archetype_id = BIO_TRIAL_DATA_PREAPPROVAL_EVENT_RISK_VS_PLATFORM_DATA_VALIDATION_AND_HARD_4C
3. Add the shadow candidate axis only as a non-production proposal:
   c24_endpoint_partner_regulatory_runway_bridge_required_for_stage2_actionable_shadow_only
4. Do not loosen Stage3-Green.
5. Enforce that C24 pre-approval/data-event price spikes require endpoint quality, regulatory path, partner/platform validation, and funding runway before Stage2-Actionable.
6. Route hard binary thesis breaks to 4C when post-event price path validates thesis failure.
7. Keep production scoring unchanged unless a later batch promotion decision approves this axis.

Expected output:
- parsed trigger rows
- aggregate metric update
- promotion decision candidate
- no direct trading output
```

## 14. Final one-line result

C24 was filled with three calibration-usable historical rows: one controlled positive data/platform validation case and two counterexamples showing why pre-approval clinical/data event price spikes need endpoint/regulatory/partner/runway bridge evidence before positive-stage promotion.
