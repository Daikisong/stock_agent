# E2R v12 Residual Research — R7 / Loop 104 / L7_BIO_HEALTHCARE_MEDICAL / C24_BIO_TRIAL_DATA_EVENT_RISK

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R7
selected_loop = 104
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = BIO_TRIAL_DATA_BINARY_EVENT_HIGH_MAE_GUARD
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Why this loop exists

C24는 바이오/헬스케어 안에서도 C23과 다르다. C23은 승인 이후 매출, royalty, reimbursement, commercialization bridge를 본다. C24는 그 직전의 얇은 얼음판이다. 임상 데이터, FDA/규제 binary event, 학회 발표, 중간 결과, 재도전 trial timeline 같은 말들이 가격을 먼저 밀어 올리지만, 실제 현금흐름은 아직 문밖에 있다.

이번 루프의 목적은 **가격 spike를 Stage3로 착각하지 않게 만드는 shadow rule**이다. 특히 다음 잔여 오류를 겨냥한다.

```text
residual_target =
  price-only bio event spike
  + binary approval/trial readout
  + weak commercial/cash bridge
  + high MAE / gap-down risk
```

## 2. No-repeat / novelty check

```text
static_index_priority_bucket = Priority 0
static_index_row_count_before = 13
static_index_need_to_30_before = 17
conversation_local_recent_archetypes_avoided =
  C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  C16_STRATEGIC_RESOURCE_POLICY_SUPPLY

selected_new_cases =
  028300 HLB
  140410 메지온
  215600 신라젠
  323990 박셀바이오

duplicate_key_basis =
  canonical_archetype_id + symbol + trigger_type + entry_date

reused_case_count = 0
new_independent_case_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

## 3. Price-source validation scope

All price rows were read from `Songdaiki/stock-web` daily tradable OHLC shards. The atlas profile caveat still applies: raw/unadjusted FinanceData/marcap OHLC, with corporate-action candidate windows blocked by default. For this run, 2024 trigger windows were outside the older major split candidates for HLB and within the modern tradable rows. 신라젠 has a 2024-07-09 corporate-action candidate; the post-event interpretation is therefore tagged with a caveat and not used as a clean long-horizon positive.

```text
primary_price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
non_price_event_evidence = source_proxy_only
evidence_url_pending = true
```

## 4. Trigger-level backtest summary

| case | ticker | entry | entry price | outcome | 30D MFE | 30D MAE | 90D MFE | 90D MAE | 180D MFE | 180D MAE | interpretation |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| HLB FDA/binary event spike | 028300 | 2024-04-25 | 109,600 | counterexample | +4.29% | -58.80% | +4.29% | -58.80% | +4.29% | -58.80% | price-only binary event should not be Stage3 |
| 메지온 trial redo timeline | 140410 | 2024-03-04 | 45,250 | mixed | +10.94% | -16.24% | +10.94% | -21.55% | +10.94% | -40.33% | Stage2 only until trial timing de-risk |
| 신라젠 oncology data spike | 215600 | 2024-05-16 | 4,565 | counterexample | +11.50% | -23.33% | +11.50% | -34.72% | +11.50% | -34.72% | endpoint/capital-structure overhang caps stage |
| 박셀바이오 local trial-data spike | 323990 | 2024-05-17 | 17,240 | positive_local_only | +46.17% | -13.52% | +46.17% | -13.52% | +46.17% | -13.52% | tradable local MFE, but Green persistence blocked |

## 5. Case notes

### 5.1 HLB — 028300 — binary approval risk as Stage3 false-positive

HLB is the cleanest C24 warning sign. Before the decisive regulatory outcome, the chart already behaved like a passed exam. Price reached 112,600 on 2024-04-25 and 114,300 on 2024-04-30, but then fell into the 67,100 limit-down row on 2024-05-17 and 45,150 low on 2024-05-21. This is exactly the shape C24 must catch: a thesis is not proven merely because the market has rehearsed the good ending.

```text
entry_date = 2024-04-25
entry_price = 109600
peak_price = 114300
trough_price = 45150
mfe_30d_pct = +4.29
mae_30d_pct = -58.80
current_profile_error = Stage3-Yellow possible from price/revision/event excitement
shadow_fix = binary_event_pre_approval_stage_cap
```

### 5.2 메지온 — 140410 — trial redo can be Stage2, not Green

메지온 shows the slower version of the same problem. The event was not an immediate hard failure like HLB, but the path after the 2024-03-04 entry still gave only a short MFE burst to 50,200 before grinding down to 27,000 by 2024-09-30. This is not a 4C thesis break if trial redesign/timeline remains alive, but it is a timing trap for Stage3.

```text
entry_date = 2024-03-04
entry_price = 45250
peak_price = 50200
trough_price = 27000
mfe_180d_pct = +10.94
mae_180d_pct = -40.33
shadow_fix = trial_redo_timeline_delay_guard
```

### 5.3 신라젠 — 215600 — data headline with corporate-action caveat

신라젠 had a visible data/headline spike around 2024-05-16, but the entry path quickly lost structure. The 2024-07-09 corporate-action candidate in stock-web means post-July interpretation must be cautious. Even before that, the price dropped from the 5,090 high to 3,500/2,980 area. This is useful as a C24 counterexample because the event can be tradeable, but it should not be promoted without registrational endpoint clarity and clean capital structure.

```text
entry_date = 2024-05-16
entry_price = 4565
peak_price = 5090
trough_price = 2980
mfe_90d_pct = +11.50
mae_90d_pct = -34.72
shadow_fix = endpoint_and_capital_structure_guard
```

### 5.4 박셀바이오 — 323990 — local MFE exists, persistence does not

박셀바이오는 C24의 positive side를 제공한다. 2024-05-17 entry 이후 2024-05-22 high 25,200까지 local MFE가 +46% 이상 발생했다. 하지만 이후 14,910 low까지 밀렸기 때문에, 이 케이스는 “Stage2-local positive”이지 “Stage3-Green 지속형”이 아니다. C24 rule은 이런 케이스를 죽이면 안 되고, 시간 제한을 둔 local action으로 살려야 한다.

```text
entry_date = 2024-05-17
entry_price = 17240
peak_price = 25200
trough_price = 14910
mfe_30d_pct = +46.17
mae_30d_pct = -13.52
shadow_fix = local_mfe_allowed_but_green_blocked_without_confirmation
```

## 6. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "case_id": "C24_R7L104_028300_20240425_HLB_PRE_FDA_BINARY_EVENT_SPIKE", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_BINARY_APPROVAL_TRIAL_DATA_SPIKE_HIGH_MAE_PRICE_ONLY_FALSE_POSITIVE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "symbol": "028300", "name": "HLB", "trigger_type": "Stage3-Yellow", "entry_date": "2024-04-25", "entry_price": 109600, "entry_price_basis": "close", "evidence_snapshot": "source_proxy_only: FDA/clinical binary event expectation was already priced into equity before decisive approval/commercial cash bridge; post-entry path shows CRL-style gap risk rather than orderly commercialization.", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "mfe_30d_pct": 4.29, "mae_30d_pct": -58.8, "mfe_90d_pct": 4.29, "mae_90d_pct": -58.8, "mfe_180d_pct": 4.29, "mae_180d_pct": -58.8, "peak_date": "2024-04-30", "peak_price": 114300, "trough_date": "2024-05-21", "trough_price": 45150, "outcome_label": "counterexample", "current_profile_error": "price momentum + event anticipation can reach Stage3, but binary data/regulatory failure creates immediate high-MAE path.", "proposed_rule_hit": "C24_binary_event_high_MAE_cap"}
{"row_type": "trigger", "case_id": "C24_R7L104_140410_20240304_MEZZION_TRIAL_REDOSING_PATH", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_REDO_DATA_TIMELINE_DELAYED_READTHROUGH_VS_PRICE_SPIKE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "symbol": "140410", "name": "메지온", "trigger_type": "Stage2-Actionable", "entry_date": "2024-03-04", "entry_price": 45250, "entry_price_basis": "close", "evidence_snapshot": "source_proxy_only: trial re-design/data-timeline expectation produced near-term MFE, but no immediate approval/reimbursement/cash bridge; long drawdown before later rerating.", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/140/140410/2024.csv", "mfe_30d_pct": 10.94, "mae_30d_pct": -16.24, "mfe_90d_pct": 10.94, "mae_90d_pct": -21.55, "mfe_180d_pct": 10.94, "mae_180d_pct": -40.33, "peak_date": "2024-03-06", "peak_price": 50200, "trough_date": "2024-09-30", "trough_price": 27000, "outcome_label": "mixed", "current_profile_error": "Stage2 can be defensible, but Stage3/Green before trial-data de-risking overstates timing and drawdown risk.", "proposed_rule_hit": "C24_trial_redo_timeline_delay_guard"}
{"row_type": "trigger", "case_id": "C24_R7L104_215600_20240516_SILLAJEN_ONCOLYTIC_DATA_EVENT_SPIKE", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_PRICE_SPIKE_WITH_CAPITAL_STRUCTURE_OVERHANG", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "symbol": "215600", "name": "신라젠", "trigger_type": "Stage2-Actionable", "entry_date": "2024-05-16", "entry_price": 4565, "entry_price_basis": "close", "evidence_snapshot": "source_proxy_only: oncology trial/data headline generated tradable spike, but continuation was blocked by lack of validated pivotal/commercial bridge and later capital-structure/corporate-action caveat.", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/215/215600/2024.csv", "mfe_30d_pct": 11.5, "mae_30d_pct": -23.33, "mfe_90d_pct": 11.5, "mae_90d_pct": -34.72, "mfe_180d_pct": 11.5, "mae_180d_pct": -34.72, "peak_date": "2024-05-16", "peak_price": 5090, "trough_date": "2024-07-05", "trough_price": 2980, "outcome_label": "counterexample", "current_profile_error": "Headline/data spike can appear actionable, but absence of clean registrational endpoint and financing/corporate-action caveat should block Stage3.", "proposed_rule_hit": "C24_capital_structure_and_endpoint_guard"}
{"row_type": "trigger", "case_id": "C24_R7L104_323990_20240517_VAXCELL_TRIAL_DATA_SPIKE_REVERSAL", "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK", "fine_archetype_id": "BIO_TRIAL_DATA_EVENT_LOCAL_MFE_WITH_REVERSAL_RISK", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "symbol": "323990", "name": "박셀바이오", "trigger_type": "Stage2-Actionable", "entry_date": "2024-05-17", "entry_price": 17240, "entry_price_basis": "close", "evidence_snapshot": "source_proxy_only: trial/data headline produced sharp local MFE, but follow-through failed without confirmatory endpoint/commercial bridge; useful positive only for local-actionable, not Stage3 Green.", "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/323/323990/2024.csv", "mfe_30d_pct": 46.17, "mae_30d_pct": -13.52, "mfe_90d_pct": 46.17, "mae_90d_pct": -13.52, "mfe_180d_pct": 46.17, "mae_180d_pct": -13.52, "peak_date": "2024-05-22", "peak_price": 25200, "trough_date": "2024-06-27", "trough_price": 14910, "outcome_label": "positive_local_only", "current_profile_error": "Local MFE is real, but Stage3-Green persistence is not supported without data validation and post-spike base.", "proposed_rule_hit": "C24_local_mfe_requires_fast_decay_guard"}
```

## 7. Score simulation rows

```jsonl
{"row_type": "score_simulation", "symbol": "028300", "name": "HLB", "base_total_proxy": 78.5, "revision_component": 48.0, "price_component": 21.0, "evidence_component": 9.5, "current_profile_stage": "Stage3-Yellow false-positive", "proposed_shadow_stage": "4B-local-watch / C24 binary cap"}
{"row_type": "score_simulation", "symbol": "140410", "name": "메지온", "base_total_proxy": 74.0, "revision_component": 45.0, "price_component": 18.0, "evidence_component": 11.0, "current_profile_stage": "Stage2-Actionable borderline", "proposed_shadow_stage": "Stage2 only until pivotal/data timing de-risk"}
{"row_type": "score_simulation", "symbol": "215600", "name": "신라젠", "base_total_proxy": 72.5, "revision_component": 38.0, "price_component": 24.0, "evidence_component": 10.5, "current_profile_stage": "Stage2-Actionable false-positive risk", "proposed_shadow_stage": "Stage2 capped / no Stage3"}
{"row_type": "score_simulation", "symbol": "323990", "name": "박셀바이오", "base_total_proxy": 76.0, "revision_component": 40.0, "price_component": 26.0, "evidence_component": 10.0, "current_profile_stage": "Stage2-Actionable local-positive", "proposed_shadow_stage": "Stage2 local only; Green blocked"}
```

## 8. Aggregate residual contribution

```json
{
  "row_type": "aggregate",
  "selected_round": "R7",
  "selected_loop": 104,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C24_BIO_TRIAL_DATA_EVENT_RISK",
  "new_independent_case_count": 4,
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 1,
  "mixed_positive_count": 1,
  "counterexample_count": 2,
  "local_4b_watch_count": 3,
  "current_profile_error_count": 4,
  "static_index_rows_before": 13,
  "static_index_rows_after_if_accepted": 17,
  "still_priority_0_need_to_30": 13,
  "residual_error_cluster": "bio_binary_event_price_only_spike_high_MAE",
  "primary_shadow_rule_candidate": "C24_bio_binary_event_stage3_cap_until_confirmatory_data_or_cash_bridge"
}
```

## 9. Proposed shadow rules

### 9.1 C24 binary event stage cap

```text
rule_id = C24_bio_binary_event_stage3_cap
if canonical_archetype_id == C24_BIO_TRIAL_DATA_EVENT_RISK
and event_type in {trial_readout, FDA_decision, regulatory_binary, phase_result, conference_data}
and commercial_cash_bridge_confirmed == false
and confirmatory_endpoint_or_approval_quality < high
then max_stage = Stage2-Actionable
block_stage3_green = true
```

### 9.2 C24 high-MAE price-only guard

```text
rule_id = C24_high_MAE_price_only_guard
if price_component >= 22
and non_price_evidence in {source_proxy_only, headline_only, pre_event_expectation}
and binary_event_unresolved == true
then add_shadow_penalty = -5.0
force_local_4b_watch = true
```

### 9.3 C24 local-positive preservation

```text
rule_id = C24_local_trial_data_mfe_preservation
if trial_data_event_has_actual_readout == true
and 30d_MFE_history_for_similar_cases >= 25%
and commercial_bridge_confirmed == false
then allow_stage2_actionable_local = true
but require_fast_decay_window = 10_to_30_trading_days
block_stage3_green = true
```

### 9.4 C24 endpoint/capital-structure guard

```text
rule_id = C24_endpoint_capital_structure_guard
if endpoint_quality in {surrogate_unclear, exploratory, non_registrational}
or capital_structure_caveat == true
or corporate_action_candidate_near_window == true
then max_stage = Stage2
require_manual_caveat = true
```

## 10. Handoff prompt for later coding agent

```text
You are a coding agent working in Songdaiki/stock_agent.

Do not use this MD as a live trading recommendation.
Batch-ingest this MD only as v12 residual calibration evidence.

Task:
1. Add C24_BIO_TRIAL_DATA_EVENT_RISK residual rows from this MD to the v12 calibration registry.
2. Preserve all trigger rows as historical examples.
3. Implement only shadow-rule candidates unless the batch reviewer explicitly promotes them:
   - C24_bio_binary_event_stage3_cap
   - C24_high_MAE_price_only_guard
   - C24_local_trial_data_mfe_preservation
   - C24_endpoint_capital_structure_guard
4. Do not change production scoring without a separate review.
5. Ensure C24 binary events cannot become Stage3-Green from price strength alone.
6. Ensure genuine local MFE cases remain Stage2-actionable when the trial data readout is real but commercial cash bridge is still absent.
7. Keep source_proxy_only rows lower confidence until external evidence URLs are attached.
```

## 11. Final residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed =
  C24_bio_binary_event_stage3_cap
  C24_high_MAE_price_only_guard
  C24_trial_redo_timeline_delay_guard
  C24_local_trial_data_mfe_preservation
  C24_endpoint_capital_structure_guard

existing_axis_strengthened =
  stage2_required_bridge
  price_only_blowoff_blocks_positive_stage
  full_4b_requires_non_price_evidence
  local_4b_watch_guard
  high_MAE_guardrail

existing_axis_weakened = null
do_not_propose_new_weight_delta = false

next_recommended_archetypes =
  C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
  C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  C19_BRAND_RETAIL_INVENTORY_MARGIN
  C27_CONTENT_IP_GLOBAL_MONETIZATION
  C02_POWER_GRID_DATACENTER_CAPEX
```
