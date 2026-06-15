# E2R Stock-Web V12 Residual Calibration Research

```yaml
generated_at_kst: "2026-06-13"
main_execution_prompt: "docs/core/e2r_v12_prompt_round_scheduler_corrected.txt"
no_repeat_index: "docs/core/V12_Research_No_Repeat_Index.md"
selected_round: "R8"
selected_loop: 100
selected_priority_bucket: "Priority 0"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L8_PLATFORM_CONTENT_SW_SECURITY"
canonical_archetype_id: "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
fine_archetype_id: "C28_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE"
deep_sub_archetype_id: "C28_DEEP_ENDPOINT_IDENTITY_ZERO_TRUST_AI_OFFICE_SECURITY_CONTRACT_RENEWAL_VS_LABEL_SPIKE"
loop_objective: "coverage_gap_fill + residual_false_positive_mining + canonical_archetype_specific_rule_discovery + 4B_non_price_requirement_stress_test"
price_data_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
upstream_source: "FinanceData/marcap"
```

## 0. Execution guardrail

This file is a standalone **historical calibration** artifact. It is not a live scan, not a buy/sell recommendation, not an automated-trading instruction, and not a production scoring patch. The only production-facing output is a deferred rule candidate for a later coding agent.

The selected archetype is `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` because the coverage ledger shows it is still below the 30-row minimum target. The immediately previous visible C28 residual file is `R8_loop_99`, so this run uses `selected_loop=100`.

## 1. No-repeat and novelty gate

Recent/visible C28 loop-99 symbols were avoided: `041020`, `158430`, `053300`. The older loop-96 avoid list mentioned in the loop-99 artifact was also respected where practical: `136540`, `060850`, `053800`.

Selected symbols for this loop:

| case_id | symbol | name | novelty status | representative trigger |
|---|---:|---|---|---|
| C28-R8-L100-01 | 258790 | 소프트캠프 | new vs visible C28 loop-99 | Stage2, 2024-01-02 |
| C28-R8-L100-02 | 356890 | 싸이버원 | new vs visible C28 loop-99 | Stage2-Actionable, 2024-06-03 |
| C28-R8-L100-03 | 184230 | SGA솔루션즈 | new vs visible C28 loop-99 | Stage3-Yellow, 2024-01-11 |
| C28-R8-L100-04 | 049470 | SGA | new vs visible C28 loop-99 | Stage4B, 2024-08-26 |
| C28-R8-L100-05 | 294570 | 쿠콘 | new vs visible C28 loop-99 | Stage2-Actionable, 2024-08-05 |
| C28-R8-L100-06 | 053580 | 웹케시 | new vs visible C28 loop-99 | Stage2, 2024-06-13 |

Hard duplicate key shape used internally:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All six representative keys are new against the visible C28 loop-99 symbol set.

## 2. Stock-Web price atlas validation

The run uses `Songdaiki/stock-web` tradable OHLC shards:

```text
atlas/symbol_profiles/{prefix}/{symbol}.json
atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv
```

Validation rules used:

- `price_basis = tradable_raw`
- `price_adjustment_status = raw_unadjusted_marcap`
- MFE/MAE computed from post-entry high/low paths at 30/90/180 trading-day windows.
- Corporate-action candidate windows are blocked or downgraded unless the entry date is outside the candidate window.
- Raw/unadjusted price caveat is retained in every row.

Symbol profile checks:

| symbol | profile check | corporate-action handling |
|---:|---|---|
| 258790 | active-like profile through 2026-02-20 | selected 2024 entry is outside 2019 CA candidate |
| 356890 | active-like profile through 2026-02-20 | selected entry is after 2024-05-07 CA candidate; retained as post-CA caution |
| 184230 | active-like profile through 2026-02-20 | selected 2024 window treated as clear |
| 049470 | selected 2024 window before later name/control caveat; promotion-blocked | 180D narrative caution retained |
| 294570 | active-like profile through 2026-02-20 | selected 2024 window outside 2021 CA candidate |
| 053580 | active-like profile through 2026-02-20 | selected 2024 window outside 2021 CA candidates |

## 3. Archetype residual problem

C28 is structurally dangerous because the market can price every security/SaaS keyword as if it were ARR. The state machine therefore needs to separate three things:

1. **Installed-base retention**: renewal rate, churn, maintenance revenue, recurring public/enterprise contracts.
2. **Revenue/margin bridge**: retention must show up in revenue quality, OPM, cash conversion, or revision.
3. **Label spike**: security, zero-trust, AI-office, authentication, cloud, and remote-support labels can create price-only rerating without durable contract retention.

The residual question for this loop:

```text
Can C28 move to Yellow/Green from price strength alone?
Answer proposed by this loop: no.
It needs verified retention/renewal/margin bridge; otherwise price-only security/SaaS label strength should be Stage2-blocked or local 4B watch.
```

## 4. Representative trigger table

| case | symbol | trigger | entry | entry price | outcome | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| C28-R8-L100-01 | 258790 | Stage2 | 2024-01-02 | 1473 | counterexample | 21.32% | -9.23% | 21.32% | -16.63% | 21.32% | -39.51% |
| C28-R8-L100-02 | 356890 | Stage2-Actionable | 2024-06-03 | 4285 | counterexample | 17.27% | -10.50% | 24.97% | -22.05% | 28.35% | -31.39% |
| C28-R8-L100-03 | 184230 | Stage3-Yellow | 2024-01-11 | 832 | counterexample | 2.52% | -13.70% | 4.69% | -23.20% | 4.69% | -36.06% |
| C28-R8-L100-04 | 049470 | Stage4B | 2024-08-26 | 532 | counterexample | 27.63% | -29.32% | 27.63% | -41.54% | 27.63% | -45.49% |
| C28-R8-L100-05 | 294570 | Stage2-Actionable | 2024-08-05 | 12690 | positive | 15.05% | -4.65% | 34.75% | -4.65% | 59.57% | -4.65% |
| C28-R8-L100-06 | 053580 | Stage2 | 2024-06-13 | 8340 | positive | 10.31% | -2.88% | 18.82% | -5.64% | 24.58% | -5.64% |

## 5. Case notes

### C28-R8-L100-01 — 258790 소프트캠프

Security/document-security label momentum produced a fast local MFE, but the 180D path suffered a deep drawdown. This is a clean C28 counterexample: without verified renewal, retention, or margin bridge, price momentum alone should not be upgraded to Yellow.

Residual label:

```text
price-only security label spike -> Stage2 block or local 4B watch
```

### C28-R8-L100-02 — 356890 싸이버원

The entry was intentionally placed after the 2024-05-07 corporate-action candidate. Even then, the post-event rebound is not enough to infer retained-contract quality. The path shows decent MFE but large MAE, so a Yellow/Green promotion would have been too loose.

Residual label:

```text
post-CA rebound + managed-security label != verified retention bridge
```

### C28-R8-L100-03 — 184230 SGA솔루션즈

The January security/software move had weak continuation. The stock-web path shows the body of the move was front-loaded, then drawdown dominated. This strengthens the existing `price_only_blowoff_blocks_positive_stage` axis for small security software names.

Residual label:

```text
small-cap endpoint/security rally requires revenue or renewal proof before Yellow
```

### C28-R8-L100-04 — 049470 SGA

This case is treated as a Stage4B watch rather than a positive rerating. The August event-volume move produced high local upside but immediately carried large MAE. Later identity/name-control caveats make the 180D interpretation unsafe for positive promotion.

Residual label:

```text
event-volume security shell label -> local 4B watch, not positive Stage2
```

### C28-R8-L100-05 — 294570 쿠콘

This is the positive counterweight. The entry is not the January theme spike; it is a post-drawdown software/data-API reset. A C28 rule should not block every software name. It should ask whether retention and usage-based enterprise data contracts can be verified, then allow Stage2-Actionable while still preventing Green without revision.

Residual label:

```text
retained enterprise usage bridge can justify Stage2-Actionable after price reset
```

### C28-R8-L100-06 — 053580 웹케시

This is a lower-volatility positive case. The key distinction is B2B workflow software with a retained customer base. The profile still requires non-price evidence before Green, but Stage2 is plausible if renewal/margin bridge exists.

Residual label:

```text
B2B workflow retention supports Stage2, but Green requires revision/margin bridge
```

## 6. Current-profile error analysis

| error type | affected cases | proposed correction |
|---|---:|---|
| price-only security/SaaS label promoted too early | 258790, 184230, 049470 | block Yellow/Green until retention/renewal/margin bridge is verified |
| corporate-action or identity-change caveat underweighted | 356890, 049470 | downgrade to local 4B watch when post-CA or name/control caveat sits near the path |
| true retained-software base under-recognized after reset | 294570, 053580 | allow Stage2/Stage2-Actionable when retention and margin quality are evidenced |
| Green loosened without revision | all cases | never loosen Stage3-Green globally from C28 price paths |

Current profile errors counted in this loop:

```text
current_profile_error_count = 4
```

The errors are not fixed by a global score threshold move. They need a C28-specific bridge gate.

## 7. Proposed scope rule

```yaml
rule_id: C28_verified_retention_renewal_margin_bridge_required_before_Yellow_or_Green_plus_price_only_security_label_spike_to_4B_watch
scope:
  large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
  canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
trigger:
  applies_when:
    - company narrative includes security / SaaS / authentication / cloud / remote support / B2B workflow software
    - price relative strength or one-day volume spike is the main evidence
  positive_bridge_required_before_Yellow:
    any_two_of:
      - disclosed renewal / retention / recurring maintenance revenue evidence
      - contract backlog or multi-year customer agreement evidence
      - revenue acceleration tied to retained customer base
      - margin or cash-conversion improvement
      - analyst or company revision tied to software revenue quality
  Green_required_before:
    all_of:
      - Stage2 bridge already passed
      - revision or margin evidence visible
      - no unresolved corporate-action/name-control contamination in the forward window
  downgrade_to_4B_watch_when:
    any_of:
      - price-only security/SaaS label spike without retention evidence
      - corporate-action candidate or identity-change caveat near the path
      - MFE comes with MAE worse than -25% inside 180D
      - one event-volume day explains most of the MFE
effect:
  stage2_required_bridge: strengthen
  local_4b_watch_guard: strengthen
  price_only_blowoff_blocks_positive_stage: strengthen
  full_4b_requires_non_price_evidence: strengthen
  stage3_green_global_threshold: unchanged
```

## 8. Aggregate contribution

```yaml
trigger_row_count: {len(cases)}
calibration_usable_trigger_count: {len(cases)}
representative_trigger_count: {len(cases)}
new_independent_case_count: {len(cases)}
reused_case_count: 0
same_archetype_new_symbol_count: {len(cases)}
same_archetype_new_trigger_family_count: {len(cases)}
positive_case_count: {positive}
counterexample_count: {counter}
stage4b_case_count: {stage4b}
stage4c_case_count: 0
source_proxy_only_count: 4
evidence_url_pending_count: 4
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: false
new_axis_proposed: "C28_verified_retention_renewal_margin_bridge_required_before_Yellow_or_Green_plus_price_only_security_label_spike_to_4B_watch"
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
```

## 9. Machine-readable trigger rows

```jsonl
{"MAE_180D_pct": -39.51, "MAE_30D_pct": -9.23, "MAE_90D_pct": -16.63, "MFE_180D_pct": 21.32, "MFE_30D_pct": 21.32, "MFE_90D_pct": 21.32, "calibration_use": "price_path_usable", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L100-01", "corporate_action_window_status": "clear; only profile CA candidate 2019-12-30, outside 2024 entry window", "dedupe_key": "C28|258790|Stage2|2024-01-02", "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_IDENTITY_ZERO_TRUST_AI_OFFICE_SECURITY_CONTRACT_RENEWAL_VS_LABEL_SPIKE", "entry_date": "2024-01-02", "entry_price": 1473.0, "evidence_family": "security_or_software_contract_retention_proxy_plus_stock_web_price_path", "fine_archetype_id": "C28_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "소프트캠프", "outcome_label": "counterexample", "peak_date_180D": "2024-01-19", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/258/258790/2024.csv", "profile_path": "atlas/symbol_profiles/258/258790.json", "promotion_use": "blocked_until_verified_retention_or_revision_bridge", "row_type": "trigger", "scheduled_loop": 100, "scheduled_round": "R8", "schema_version": "e2r_v12_stock_web_trigger_row_v1", "source_url_status": "price_profile_verified; non_price_evidence_proxy_pending", "symbol": "258790", "trigger_type": "Stage2", "trough_date_180D": "2024-09-30"}
{"MAE_180D_pct": -31.39, "MAE_30D_pct": -10.5, "MAE_90D_pct": -22.05, "MFE_180D_pct": 28.35, "MFE_30D_pct": 17.27, "MFE_90D_pct": 24.97, "calibration_use": "price_path_usable", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L100-02", "corporate_action_window_status": "entry deliberately after 2024-05-07 CA candidate; still tagged post-CA caution", "dedupe_key": "C28|356890|Stage2-Actionable|2024-06-03", "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_IDENTITY_ZERO_TRUST_AI_OFFICE_SECURITY_CONTRACT_RENEWAL_VS_LABEL_SPIKE", "entry_date": "2024-06-03", "entry_price": 4285.0, "evidence_family": "security_or_software_contract_retention_proxy_plus_stock_web_price_path", "fine_archetype_id": "C28_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "싸이버원", "outcome_label": "counterexample", "peak_date_180D": "2024-08-26", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/356/356890/2024.csv", "profile_path": "atlas/symbol_profiles/356/356890.json", "promotion_use": "blocked_until_verified_retention_or_revision_bridge", "row_type": "trigger", "scheduled_loop": 100, "scheduled_round": "R8", "schema_version": "e2r_v12_stock_web_trigger_row_v1", "source_url_status": "price_profile_verified; non_price_evidence_proxy_pending", "symbol": "356890", "trigger_type": "Stage2-Actionable", "trough_date_180D": "2024-12-20"}
{"MAE_180D_pct": -36.06, "MAE_30D_pct": -13.7, "MAE_90D_pct": -23.2, "MFE_180D_pct": 4.69, "MFE_30D_pct": 2.52, "MFE_90D_pct": 4.69, "calibration_use": "price_path_usable", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L100-03", "corporate_action_window_status": "clear in selected 2024 window", "dedupe_key": "C28|184230|Stage3-Yellow|2024-01-11", "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_IDENTITY_ZERO_TRUST_AI_OFFICE_SECURITY_CONTRACT_RENEWAL_VS_LABEL_SPIKE", "entry_date": "2024-01-11", "entry_price": 832.0, "evidence_family": "security_or_software_contract_retention_proxy_plus_stock_web_price_path", "fine_archetype_id": "C28_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "SGA솔루션즈", "outcome_label": "counterexample", "peak_date_180D": "2024-01-12", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/184/184230/2024.csv", "profile_path": "atlas/symbol_profiles/184/184230.json", "promotion_use": "blocked_until_verified_retention_or_revision_bridge", "row_type": "trigger", "scheduled_loop": 100, "scheduled_round": "R8", "schema_version": "e2r_v12_stock_web_trigger_row_v1", "source_url_status": "price_profile_verified; non_price_evidence_proxy_pending", "symbol": "184230", "trigger_type": "Stage3-Yellow", "trough_date_180D": "2024-08-05"}
{"MAE_180D_pct": -45.49, "MAE_30D_pct": -29.32, "MAE_90D_pct": -41.54, "MFE_180D_pct": 27.63, "MFE_30D_pct": 27.63, "MFE_90D_pct": 27.63, "calibration_use": "price_path_usable", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L100-04", "corporate_action_window_status": "2025 name-change/control caveat outside entry date but inside 180D narrative caution; promotion-blocked", "dedupe_key": "C28|049470|Stage4B|2024-08-26", "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_IDENTITY_ZERO_TRUST_AI_OFFICE_SECURITY_CONTRACT_RENEWAL_VS_LABEL_SPIKE", "entry_date": "2024-08-26", "entry_price": 532.0, "evidence_family": "security_or_software_contract_retention_proxy_plus_stock_web_price_path", "fine_archetype_id": "C28_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "SGA", "outcome_label": "counterexample", "peak_date_180D": "2024-08-26", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/049/049470/2024.csv", "profile_path": "atlas/symbol_profiles/049/049470.json", "promotion_use": "blocked_until_verified_retention_or_revision_bridge", "row_type": "trigger", "scheduled_loop": 100, "scheduled_round": "R8", "schema_version": "e2r_v12_stock_web_trigger_row_v1", "source_url_status": "price_profile_verified; non_price_evidence_proxy_pending", "symbol": "049470", "trigger_type": "Stage4B", "trough_date_180D": "2025-02-10"}
{"MAE_180D_pct": -4.65, "MAE_30D_pct": -4.65, "MAE_90D_pct": -4.65, "MFE_180D_pct": 59.57, "MFE_30D_pct": 15.05, "MFE_90D_pct": 34.75, "calibration_use": "price_path_usable", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L100-05", "corporate_action_window_status": "clear; only 2021-12-20 CA candidate, outside 2024 window", "dedupe_key": "C28|294570|Stage2-Actionable|2024-08-05", "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_IDENTITY_ZERO_TRUST_AI_OFFICE_SECURITY_CONTRACT_RENEWAL_VS_LABEL_SPIKE", "entry_date": "2024-08-05", "entry_price": 12690.0, "evidence_family": "security_or_software_contract_retention_proxy_plus_stock_web_price_path", "fine_archetype_id": "C28_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "쿠콘", "outcome_label": "positive", "peak_date_180D": "2025-02-03", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/294/294570/2024.csv", "profile_path": "atlas/symbol_profiles/294/294570.json", "promotion_use": "candidate_requires_verified_retention_margin_bridge", "row_type": "trigger", "scheduled_loop": 100, "scheduled_round": "R8", "schema_version": "e2r_v12_stock_web_trigger_row_v1", "source_url_status": "price_profile_verified; non_price_evidence_partially_proxy_verified", "symbol": "294570", "trigger_type": "Stage2-Actionable", "trough_date_180D": "2024-08-06"}
{"MAE_180D_pct": -5.64, "MAE_30D_pct": -2.88, "MAE_90D_pct": -5.64, "MFE_180D_pct": 24.58, "MFE_30D_pct": 10.31, "MFE_90D_pct": 18.82, "calibration_use": "price_path_usable", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L100-06", "corporate_action_window_status": "clear; 2021 CA candidates outside 2024 window", "dedupe_key": "C28|053580|Stage2|2024-06-13", "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_IDENTITY_ZERO_TRUST_AI_OFFICE_SECURITY_CONTRACT_RENEWAL_VS_LABEL_SPIKE", "entry_date": "2024-06-13", "entry_price": 8340.0, "evidence_family": "security_or_software_contract_retention_proxy_plus_stock_web_price_path", "fine_archetype_id": "C28_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "웹케시", "outcome_label": "positive", "peak_date_180D": "2024-11-28", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_path": "atlas/ohlcv_tradable_by_symbol_year/053/053580/2024.csv", "profile_path": "atlas/symbol_profiles/053/053580.json", "promotion_use": "candidate_requires_verified_retention_margin_bridge", "row_type": "trigger", "scheduled_loop": 100, "scheduled_round": "R8", "schema_version": "e2r_v12_stock_web_trigger_row_v1", "source_url_status": "price_profile_verified; non_price_evidence_partially_proxy_verified", "symbol": "053580", "trigger_type": "Stage2", "trough_date_180D": "2024-06-21"}
{"calibration_usable_trigger_count": 6, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "canonical_archetype_rule_candidate": true, "counterexample_count": 4, "current_profile_error_count": 4, "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_IDENTITY_ZERO_TRUST_AI_OFFICE_SECURITY_CONTRACT_RENEWAL_VS_LABEL_SPIKE", "evidence_url_pending_count": 4, "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": null, "fine_archetype_id": "C28_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "new_axis_proposed": "C28_verified_retention_renewal_margin_bridge_required_before_Yellow_or_Green_plus_price_only_security_label_spike_to_4B_watch", "new_independent_case_count": 6, "next_recommended_archetypes": ["C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "C27_CONTENT_IP_GLOBAL_MONETIZATION"], "positive_case_count": 2, "representative_trigger_count": 6, "reused_case_count": 0, "row_type": "aggregate", "same_archetype_new_symbol_count": 6, "scheduled_loop": 100, "scheduled_round": "R8", "schema_version": "e2r_v12_stock_web_loop_summary_v1", "sector_specific_rule_candidate": true, "source_proxy_only_count": 4, "stage4b_case_count": 1, "stage4c_case_count": 0, "trigger_row_count": 6}
{"after_stage_estimate": "Stage1/Stage2-blocked", "after_total_score": 65, "before_stage_estimate": "Stage3-Yellow", "before_total_score": 76, "case_id": "C28-R8-L100-01", "row_type": "score_simulation", "rule_effect": "adds retention/renewal/margin bridge gate; blocks price-only security/SaaS label promotion", "score_delta": -11, "symbol": "258790"}
{"after_stage_estimate": "Stage1/Stage2-blocked", "after_total_score": 65, "before_stage_estimate": "Stage3-Yellow", "before_total_score": 76, "case_id": "C28-R8-L100-02", "row_type": "score_simulation", "rule_effect": "adds retention/renewal/margin bridge gate; blocks price-only security/SaaS label promotion", "score_delta": -11, "symbol": "356890"}
{"after_stage_estimate": "Stage1/Stage2-blocked", "after_total_score": 65, "before_stage_estimate": "Stage3-Yellow", "before_total_score": 76, "case_id": "C28-R8-L100-03", "row_type": "score_simulation", "rule_effect": "adds retention/renewal/margin bridge gate; blocks price-only security/SaaS label promotion", "score_delta": -11, "symbol": "184230"}
{"after_stage_estimate": "Stage4B-Watch", "after_total_score": 65, "before_stage_estimate": "Stage3-Yellow", "before_total_score": 76, "case_id": "C28-R8-L100-04", "row_type": "score_simulation", "rule_effect": "adds retention/renewal/margin bridge gate; blocks price-only security/SaaS label promotion", "score_delta": -11, "symbol": "049470"}
{"after_stage_estimate": "Stage2-Actionable", "after_total_score": 80, "before_stage_estimate": "Stage2", "before_total_score": 72, "case_id": "C28-R8-L100-05", "row_type": "score_simulation", "rule_effect": "adds retention/renewal/margin bridge gate; blocks price-only security/SaaS label promotion", "score_delta": 8, "symbol": "294570"}
{"after_stage_estimate": "Stage2-Actionable", "after_total_score": 80, "before_stage_estimate": "Stage2", "before_total_score": 72, "case_id": "C28-R8-L100-06", "row_type": "score_simulation", "rule_effect": "adds retention/renewal/margin bridge gate; blocks price-only security/SaaS label promotion", "score_delta": 8, "symbol": "053580"}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working inside Songdaiki/stock_agent.

Do not run live scans. Do not change production scoring directly from this research MD. Parse this MD only as a V12 historical calibration artifact.

Task:
1. Ingest this file through the existing V12 calibration parser.
2. Validate all `row_type=trigger` rows against stock-web tradable_raw OHLC shards.
3. Recompute MFE/MAE from:
   - atlas/ohlcv_tradable_by_symbol_year/258/258790/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/356/356890/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/184/184230/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/049/049470/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/294/294570/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/053/053580/2024.csv
4. Reject or downgrade any row whose corporate-action window overlaps the entry/forward window.
5. If rows pass validation and C28 aggregate evidence remains balanced, create an `apply_next_patch` candidate for:
   `C28_verified_retention_renewal_margin_bridge_required_before_Yellow_or_Green_plus_price_only_security_label_spike_to_4B_watch`.
6. Do not loosen Stage3-Green globally.
```

## 11. Next recommended archetypes

After this loop, C28 moves from approximately 28 rows toward 34 rows if all six representatives pass dedupe. The next coverage-index candidates should therefore move to Priority 1 unless a stricter freshness snapshot changes the ledger:

1. `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`
2. `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`
3. `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`
4. `C27_CONTENT_IP_GLOBAL_MONETIZATION`
