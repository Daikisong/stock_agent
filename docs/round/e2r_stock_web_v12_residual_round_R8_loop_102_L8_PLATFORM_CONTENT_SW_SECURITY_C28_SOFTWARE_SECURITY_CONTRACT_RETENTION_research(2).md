# E2R Stock-Web V12 Residual Calibration Research

## 0. Research Metadata

```json
{
  "row_type": "research_metadata",
  "generated_at_kst": "2026-06-13",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_version": "v12",
  "main_execution_prompt": "docs/core/e2r_v12_prompt_round_scheduler_corrected.txt",
  "no_repeat_index": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_round": "R8",
  "selected_loop": 102,
  "selected_priority_bucket": "Priority 1-under-50 after local-session adjustment; published index Priority 0",
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE",
  "deep_sub_archetype_id": "C28_DEEP_ERP_CLOUD_MSP_IDENTITY_REMOTE_SUPPORT_PKI_AI_DATA_SECURITY_RETENTION_VS_LABEL_SPIKE",
  "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery",
  "price_data_source": "Songdaiki/stock-web",
  "upstream_source": "FinanceData/marcap",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false
}
```

This file is a standalone v12 historical calibration artifact. It is not a live scan, not a current stock recommendation, not a broker/API workflow, and not a production scoring patch. The deferred handoff prompt appears only for a later batch implementation session.

## 1. Scheduler Decision

- Scheduler mode: `coverage_index_first`.
- Published No-Repeat priority: `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` is Priority 0 with 28 rows in the index snapshot.
- Local-session status before this loop: C28 loop100 and loop101 add about 13 representative cases, bringing local C28 to about 41.
- This loop adds 7 representative triggers and brings local-session adjusted C28 to about 48, still slightly below the 50-row practical calibration band.
- Selected round/sector derivation: C28 maps to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`.

## 2. Scope and Residual Problem

`C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` should not mean every software/security label spike is treated as recurring ARR. The residual problem in this loop is the same hinge as a renewal contract: the value is not in the label on the door, but in whether the customer keeps paying after the first door opens.

Working mechanism:

```text
enterprise/security/cloud/software contract signal -> retention or renewal proof -> revenue quality -> margin/FCF bridge -> sustainable rerating
```

The counter-mechanism is label gravity: AI security, quantum security, cloud ERP, remote support, and data analytics can pull price up briefly, but without renewal and margin bridge the price path often leaks through the floor.

## 3. No-Repeat and Novelty Gate

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Avoided local loop100 symbols: `258790`, `356890`, `184230`, `049470`, `294570`, `053580`.
Avoided local loop101 symbols: `053800`, `263860`, `150900`, `434480`, `411080`, `430690`, `208350`.

Selected representative cases:

| case_id | symbol | company | novelty status | representative trigger |
|---|---:|---|---|---|
| C28-R8-L102-01 | 012510 | 더존비즈온 | new vs local C28 loop100/101 | Stage2-Actionable, 2024-02-02 |
| C28-R8-L102-02 | 018260 | 삼성에스디에스 | new vs local C28 loop100/101 | Stage2-Actionable, 2024-01-26 |
| C28-R8-L102-03 | 203650 | 드림시큐리티 | new vs local C28 loop100/101 | Stage4B, 2024-06-17 |
| C28-R8-L102-04 | 131370 | 알서포트 | new vs local C28 loop100/101 | Stage4B, 2024-07-09 |
| C28-R8-L102-05 | 060850 | 영림원소프트랩 | new vs local C28 loop100/101 | Stage2, 2024-04-01 |
| C28-R8-L102-06 | 065370 | 위세아이텍 | new vs local C28 loop100/101 | Stage4B, 2024-02-22 |
| C28-R8-L102-07 | 307950 | 현대오토에버 | new vs local C28 loop100/101 | Stage2-Actionable, 2024-01-29 |

Novelty summary:

```text
new_independent_case_count = 7
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 7
hard_duplicate_count = 0
representative_trigger_count = 7
```

## 4. Stock-Web Price Atlas Validation

Price source and validation basis:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

The selected 2024 entry windows have a 180-trading-day forward window before the manifest max date. Rows with known split/merger/capital-action overlap inside entry~D+180 would be blocked; this loop uses proxy-safe 2024 windows and retains URL-repair flags where operating evidence is source-proxy-only.

Symbol profile checks:

| symbol | company | profile path | profile handling |
|---:|---|---|---|
| 012510 | 더존비즈온 | `atlas/symbol_profiles/012/012510.json` | selected 2024 entry path; no in-window CA contamination used for calibration |
| 018260 | 삼성에스디에스 | `atlas/symbol_profiles/018/018260.json` | selected 2024 entry path; no in-window CA contamination used for calibration |
| 203650 | 드림시큐리티 | `atlas/symbol_profiles/203/203650.json` | selected 2024 entry path; no in-window CA contamination used for calibration |
| 131370 | 알서포트 | `atlas/symbol_profiles/131/131370.json` | selected 2024 entry path; no in-window CA contamination used for calibration |
| 060850 | 영림원소프트랩 | `atlas/symbol_profiles/060/060850.json` | selected 2024 entry path; no in-window CA contamination used for calibration |
| 065370 | 위세아이텍 | `atlas/symbol_profiles/065/065370.json` | selected 2024 entry path; no in-window CA contamination used for calibration |
| 307950 | 현대오토에버 | `atlas/symbol_profiles/307/307950.json` | selected 2024 entry path; no in-window CA contamination used for calibration |

## 5. Representative Trigger-Level OHLC Table

| case | symbol | company | trigger | entry | entry_price | outcome | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| C28-R8-L102-01 | 012510 | 더존비즈온 | Stage2-Actionable | 2024-02-02 | 49700 | positive | 28.77% | -4.63% | 53.92% | -7.85% | 64.18% | -11.67% |
| C28-R8-L102-02 | 018260 | 삼성에스디에스 | Stage2-Actionable | 2024-01-26 | 158400 | positive | 12.37% | -5.68% | 20.65% | -8.14% | 28.22% | -16.41% |
| C28-R8-L102-03 | 203650 | 드림시큐리티 | Stage4B | 2024-06-17 | 4050 | counterexample | 13.58% | -14.32% | 18.27% | -25.19% | 33.09% | -31.11% |
| C28-R8-L102-04 | 131370 | 알서포트 | Stage4B | 2024-07-09 | 3560 | counterexample | 6.74% | -15.45% | 12.08% | -23.60% | 19.66% | -31.18% |
| C28-R8-L102-05 | 060850 | 영림원소프트랩 | Stage2 | 2024-04-01 | 8500 | counterexample | 4.94% | -12.71% | 9.65% | -21.76% | 14.47% | -36.00% |
| C28-R8-L102-06 | 065370 | 위세아이텍 | Stage4B | 2024-02-22 | 11380 | counterexample | 11.95% | -20.65% | 11.95% | -33.91% | 11.95% | -54.48% |
| C28-R8-L102-07 | 307950 | 현대오토에버 | Stage2-Actionable | 2024-01-29 | 163000 | counterexample | 8.28% | -10.74% | 12.64% | -16.88% | 19.33% | -28.16% |

## 6. Case Notes

### C28-R8-L102-01 — 012510 더존비즈온

- Trigger: `Stage2-Actionable` on `2024-02-02`, entry `2024-02-02` at `49700`.
- Evidence family: `cloud_ERP_Amaranth10_WEHAGO_recurring_revenue_bridge`.
- Evidence URL status: `source_proxy_only_or_pending_url_repair`; keep promotion blocked until direct URL repair unless this row is used only for negative/guardrail aggregate.
- Path result: MFE90 `53.92%`, MAE90 `-7.85%`, MFE180 `64.18%`, MAE180 `-11.67%`.
- Residual label: `too_conservative_if_verified_ERP_cloud_retention_revenue_bridge_is_ignored`.
- Mechanism note: ERP/cloud subscription-style revenue and enterprise customer stickiness can be a real C28 bridge, but Green still needs margin/revision confirmation.

### C28-R8-L102-02 — 018260 삼성에스디에스

- Trigger: `Stage2-Actionable` on `2024-01-26`, entry `2024-01-26` at `158400`.
- Evidence family: `enterprise_cloud_security_MSP_backlog_revenue_bridge`.
- Evidence URL status: `source_proxy_only_or_pending_url_repair`; keep promotion blocked until direct URL repair unless this row is used only for negative/guardrail aggregate.
- Path result: MFE90 `20.65%`, MAE90 `-8.14%`, MFE180 `28.22%`, MAE180 `-16.41%`.
- Residual label: `too_conservative_if_cloud_security_MSP_revenue_bridge_is_downgraded_to_generic_IT_label`.
- Mechanism note: Large-enterprise cloud/security/MSP revenue base supports Actionable when financial bridge is present; upside is less explosive but drawdown control is better than label-only peers.

### C28-R8-L102-03 — 203650 드림시큐리티

- Trigger: `Stage4B` on `2024-06-17`, entry `2024-06-17` at `4050`.
- Evidence family: `PKI_authentication_quantum_security_label_without_renewal_margin_bridge`.
- Evidence URL status: `source_proxy_only_or_pending_url_repair`; keep promotion blocked until direct URL repair unless this row is used only for negative/guardrail aggregate.
- Path result: MFE90 `18.27%`, MAE90 `-25.19%`, MFE180 `33.09%`, MAE180 `-31.11%`.
- Residual label: `false_positive_if_PKI_or_quantum_security_label_is_promoted_without_contract_retention_bridge`.
- Mechanism note: Security-authentication label gives local spikes but lacks durable retention/margin evidence; the path is high-MAE and should stay 4B-watch.

### C28-R8-L102-04 — 131370 알서포트

- Trigger: `Stage4B` on `2024-07-09`, entry `2024-07-09` at `3560`.
- Evidence family: `remote_support_SaaS_export_label_without_net_retention_or_margin_revision`.
- Evidence URL status: `source_proxy_only_or_pending_url_repair`; keep promotion blocked until direct URL repair unless this row is used only for negative/guardrail aggregate.
- Path result: MFE90 `12.08%`, MAE90 `-23.60%`, MFE180 `19.66%`, MAE180 `-31.18%`.
- Residual label: `false_positive_if_remote_support_SaaS_story_is_treated_as_contract_retention_without_NRR_or_revision`.
- Mechanism note: Remote-support SaaS label needs NRR/renewal evidence; otherwise it behaves like a label spike with incomplete bridge.

### C28-R8-L102-05 — 060850 영림원소프트랩

- Trigger: `Stage2` on `2024-03-29`, entry `2024-04-01` at `8500`.
- Evidence family: `ERP_cloud_conversion_without_margin_FCF_bridge`.
- Evidence URL status: `source_proxy_only_or_pending_url_repair`; keep promotion blocked until direct URL repair unless this row is used only for negative/guardrail aggregate.
- Path result: MFE90 `9.65%`, MAE90 `-21.76%`, MFE180 `14.47%`, MAE180 `-36.00%`.
- Residual label: `false_positive_if_cloud_ERP_conversion_label_is_actionable_without_margin_or_FCF_bridge`.
- Mechanism note: ERP cloud conversion is relevant to C28, but without measured retention, margin, and FCF conversion it should not become Yellow.

### C28-R8-L102-06 — 065370 위세아이텍

- Trigger: `Stage4B` on `2024-02-22`, entry `2024-02-22` at `11380`.
- Evidence family: `AI_data_security_analytics_label_without_recurring_contract_bridge`.
- Evidence URL status: `source_proxy_only_or_pending_url_repair`; keep promotion blocked until direct URL repair unless this row is used only for negative/guardrail aggregate.
- Path result: MFE90 `11.95%`, MAE90 `-33.91%`, MFE180 `11.95%`, MAE180 `-54.48%`.
- Residual label: `false_positive_if_AI_data_security_label_is_promoted_without_recurring_contract_bridge`.
- Mechanism note: AI/data-security language without recurring contract evidence created a classic price-only label spike and deep 180D drawdown.

### C28-R8-L102-07 — 307950 현대오토에버

- Trigger: `Stage2-Actionable` on `2024-01-29`, entry `2024-01-29` at `163000`.
- Evidence family: `enterprise_software_connected_car_service_revenue_bridge_with_valuation_MAE_guard`.
- Evidence URL status: `source_proxy_only_or_pending_url_repair`; keep promotion blocked until direct URL repair unless this row is used only for negative/guardrail aggregate.
- Path result: MFE90 `12.64%`, MAE90 `-16.88%`, MFE180 `19.33%`, MAE180 `-28.16%`.
- Residual label: `current_profile_may_overgrade_large_enterprise_software_if_valuation_and_customer_pull_are_not_checked`.
- Mechanism note: Enterprise software revenue is real, but valuation and customer-pull timing can still turn Actionable into high-MAE if entry is late.

## 7. Positive / Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 5
stage4b_case_count = 3
stage4c_case_count = 0
current_profile_error_count = 7
source_proxy_only_count = 5
evidence_url_pending_count = 5
promotion_blocked_until_url_repair = true_for_proxy_rows
```

Two positive rows show that C28 should not mechanically block enterprise software/security businesses when retention-like revenue quality is visible. Five counterexample rows show why generic security/software/AI labels should remain Stage2-blocked or local 4B watch until renewal, contract retention, revenue, margin, and FCF conversion are demonstrated.

## 8. Current Calibrated Profile Stress Test

Current profile assumptions stressed:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
```

Residual readout:

- The profile is directionally right to block price-only C28 label spikes.
- The remaining error is subtype recognition: cloud ERP/MSP/security revenue base should be treated differently from one-off AI/security headlines.
- C28 needs a scoped bridge rule rather than a lower global threshold.

## 9. Raw Component Score Breakdown

| case | EPS/rev | visibility | bottleneck | mispricing | valuation | capital | info | total | simulated current profile state |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C28-R8-L102-01 | 18 | 22 | 6 | 15 | 12 | 8 | 8 | 89 | Stage2-Actionable allowed, Green withheld until revision bridge |
| C28-R8-L102-02 | 17 | 22 | 5 | 12 | 11 | 10 | 8 | 85 | Stage2-Actionable allowed, Green withheld until revision bridge |
| C28-R8-L102-03 | 9 | 14 | 7 | 15 | 8 | 6 | 7 | 66 | Stage2/4B watch; Yellow blocked by missing retention/revenue/margin bridge |
| C28-R8-L102-04 | 8 | 13 | 5 | 12 | 9 | 6 | 9 | 62 | Stage2/4B watch; Yellow blocked by missing retention/revenue/margin bridge |
| C28-R8-L102-05 | 7 | 15 | 5 | 12 | 10 | 7 | 8 | 64 | Stage2/4B watch; Yellow blocked by missing retention/revenue/margin bridge |
| C28-R8-L102-06 | 5 | 12 | 4 | 16 | 7 | 5 | 10 | 59 | Stage2/4B watch; Yellow blocked by missing retention/revenue/margin bridge |
| C28-R8-L102-07 | 16 | 21 | 7 | 12 | 5 | 9 | 8 | 78 | Stage2/4B watch; Yellow blocked by missing retention/revenue/margin bridge |

## 10. Machine-Readable Trigger Rows JSONL

```jsonl
{"row_type": "trigger", "research_version": "v12", "case_id": "C28-R8-L102-01", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "symbol": "012510", "company": "더존비즈온", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 49700, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 28.77, "MAE_30D_pct": -4.63, "MFE_90D_pct": 53.92, "MAE_90D_pct": -7.85, "MFE_180D_pct": 64.18, "MAE_180D_pct": -11.67, "polarity": "positive", "evidence_family": "cloud_ERP_Amaranth10_WEHAGO_recurring_revenue_bridge", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "promotion_blocked_until_url_repair": false, "current_profile_error_type": "too_conservative_if_verified_ERP_cloud_retention_revenue_bridge_is_ignored", "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2024-02-02"}
{"row_type": "trigger", "research_version": "v12", "case_id": "C28-R8-L102-02", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "symbol": "018260", "company": "삼성에스디에스", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "entry_date": "2024-01-26", "entry_price": 158400, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 12.37, "MAE_30D_pct": -5.68, "MFE_90D_pct": 20.65, "MAE_90D_pct": -8.14, "MFE_180D_pct": 28.22, "MAE_180D_pct": -16.41, "polarity": "positive", "evidence_family": "enterprise_cloud_security_MSP_backlog_revenue_bridge", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": false, "evidence_url_pending": false, "promotion_blocked_until_url_repair": false, "current_profile_error_type": "too_conservative_if_cloud_security_MSP_revenue_bridge_is_downgraded_to_generic_IT_label", "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|018260|Stage2-Actionable|2024-01-26"}
{"row_type": "trigger", "research_version": "v12", "case_id": "C28-R8-L102-03", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "symbol": "203650", "company": "드림시큐리티", "trigger_type": "Stage4B", "trigger_date": "2024-06-17", "entry_date": "2024-06-17", "entry_price": 4050, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 13.58, "MAE_30D_pct": -14.32, "MFE_90D_pct": 18.27, "MAE_90D_pct": -25.19, "MFE_180D_pct": 33.09, "MAE_180D_pct": -31.11, "polarity": "counterexample", "evidence_family": "PKI_authentication_quantum_security_label_without_renewal_margin_bridge", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true, "current_profile_error_type": "false_positive_if_PKI_or_quantum_security_label_is_promoted_without_contract_retention_bridge", "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|203650|Stage4B|2024-06-17"}
{"row_type": "trigger", "research_version": "v12", "case_id": "C28-R8-L102-04", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "symbol": "131370", "company": "알서포트", "trigger_type": "Stage4B", "trigger_date": "2024-07-09", "entry_date": "2024-07-09", "entry_price": 3560, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 6.74, "MAE_30D_pct": -15.45, "MFE_90D_pct": 12.08, "MAE_90D_pct": -23.6, "MFE_180D_pct": 19.66, "MAE_180D_pct": -31.18, "polarity": "counterexample", "evidence_family": "remote_support_SaaS_export_label_without_net_retention_or_margin_revision", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true, "current_profile_error_type": "false_positive_if_remote_support_SaaS_story_is_treated_as_contract_retention_without_NRR_or_revision", "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|131370|Stage4B|2024-07-09"}
{"row_type": "trigger", "research_version": "v12", "case_id": "C28-R8-L102-05", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "symbol": "060850", "company": "영림원소프트랩", "trigger_type": "Stage2", "trigger_date": "2024-03-29", "entry_date": "2024-04-01", "entry_price": 8500, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 4.94, "MAE_30D_pct": -12.71, "MFE_90D_pct": 9.65, "MAE_90D_pct": -21.76, "MFE_180D_pct": 14.47, "MAE_180D_pct": -36.0, "polarity": "counterexample", "evidence_family": "ERP_cloud_conversion_without_margin_FCF_bridge", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true, "current_profile_error_type": "false_positive_if_cloud_ERP_conversion_label_is_actionable_without_margin_or_FCF_bridge", "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|060850|Stage2|2024-04-01"}
{"row_type": "trigger", "research_version": "v12", "case_id": "C28-R8-L102-06", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "symbol": "065370", "company": "위세아이텍", "trigger_type": "Stage4B", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 11380, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 11.95, "MAE_30D_pct": -20.65, "MFE_90D_pct": 11.95, "MAE_90D_pct": -33.91, "MFE_180D_pct": 11.95, "MAE_180D_pct": -54.48, "polarity": "counterexample", "evidence_family": "AI_data_security_analytics_label_without_recurring_contract_bridge", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true, "current_profile_error_type": "false_positive_if_AI_data_security_label_is_promoted_without_recurring_contract_bridge", "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|065370|Stage4B|2024-02-22"}
{"row_type": "trigger", "research_version": "v12", "case_id": "C28-R8-L102-07", "selected_round": "R8", "selected_loop": 102, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "symbol": "307950", "company": "현대오토에버", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-29", "entry_date": "2024-01-29", "entry_price": 163000, "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "MFE_30D_pct": 8.28, "MAE_30D_pct": -10.74, "MFE_90D_pct": 12.64, "MAE_90D_pct": -16.88, "MFE_180D_pct": 19.33, "MAE_180D_pct": -28.16, "polarity": "counterexample", "evidence_family": "enterprise_software_connected_car_service_revenue_bridge_with_valuation_MAE_guard", "calibration_usable": true, "representative_for_aggregate": true, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true, "current_profile_error_type": "current_profile_may_overgrade_large_enterprise_software_if_valuation_and_customer_pull_are_not_checked", "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|307950|Stage2-Actionable|2024-01-29"}
```

## 11. Machine-Readable Case Rows JSONL

```jsonl
{"row_type": "case", "case_id": "C28-R8-L102-01", "symbol": "012510", "company": "더존비즈온", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "novelty_status": "new_symbol_vs_local_C28_loop100_loop101", "polarity": "positive", "residual_error_type": "too_conservative_if_verified_ERP_cloud_retention_revenue_bridge_is_ignored", "calibration_usable": true, "representative_trigger_count": 1}
{"row_type": "case", "case_id": "C28-R8-L102-02", "symbol": "018260", "company": "삼성에스디에스", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "novelty_status": "new_symbol_vs_local_C28_loop100_loop101", "polarity": "positive", "residual_error_type": "too_conservative_if_cloud_security_MSP_revenue_bridge_is_downgraded_to_generic_IT_label", "calibration_usable": true, "representative_trigger_count": 1}
{"row_type": "case", "case_id": "C28-R8-L102-03", "symbol": "203650", "company": "드림시큐리티", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "novelty_status": "new_symbol_vs_local_C28_loop100_loop101", "polarity": "counterexample", "residual_error_type": "false_positive_if_PKI_or_quantum_security_label_is_promoted_without_contract_retention_bridge", "calibration_usable": true, "representative_trigger_count": 1}
{"row_type": "case", "case_id": "C28-R8-L102-04", "symbol": "131370", "company": "알서포트", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "novelty_status": "new_symbol_vs_local_C28_loop100_loop101", "polarity": "counterexample", "residual_error_type": "false_positive_if_remote_support_SaaS_story_is_treated_as_contract_retention_without_NRR_or_revision", "calibration_usable": true, "representative_trigger_count": 1}
{"row_type": "case", "case_id": "C28-R8-L102-05", "symbol": "060850", "company": "영림원소프트랩", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "novelty_status": "new_symbol_vs_local_C28_loop100_loop101", "polarity": "counterexample", "residual_error_type": "false_positive_if_cloud_ERP_conversion_label_is_actionable_without_margin_or_FCF_bridge", "calibration_usable": true, "representative_trigger_count": 1}
{"row_type": "case", "case_id": "C28-R8-L102-06", "symbol": "065370", "company": "위세아이텍", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "novelty_status": "new_symbol_vs_local_C28_loop100_loop101", "polarity": "counterexample", "residual_error_type": "false_positive_if_AI_data_security_label_is_promoted_without_recurring_contract_bridge", "calibration_usable": true, "representative_trigger_count": 1}
{"row_type": "case", "case_id": "C28-R8-L102-07", "symbol": "307950", "company": "현대오토에버", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_CLOUD_RENEWAL_REVENUE_MARGIN_BRIDGE", "novelty_status": "new_symbol_vs_local_C28_loop100_loop101", "polarity": "counterexample", "residual_error_type": "current_profile_may_overgrade_large_enterprise_software_if_valuation_and_customer_pull_are_not_checked", "calibration_usable": true, "representative_trigger_count": 1}
```

## 12. Score Simulation Rows JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C28-R8-L102-01", "symbol": "012510", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "component_scores": {"eps": 18, "visibility": 22, "bottleneck": 6, "mispricing": 15, "valuation": 12, "capital": 8, "info": 8}, "raw_total_score": 89, "simulated_stage_without_C28_bridge_guard": "Stage3-Yellow", "simulated_stage_with_C28_bridge_guard": "Stage2-Actionable", "bridge_required": "verified_retention_renewal_revenue_margin_or_FCF_bridge", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8-L102-02", "symbol": "018260", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "component_scores": {"eps": 17, "visibility": 22, "bottleneck": 5, "mispricing": 12, "valuation": 11, "capital": 10, "info": 8}, "raw_total_score": 85, "simulated_stage_without_C28_bridge_guard": "Stage3-Yellow", "simulated_stage_with_C28_bridge_guard": "Stage2-Actionable", "bridge_required": "verified_retention_renewal_revenue_margin_or_FCF_bridge", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8-L102-03", "symbol": "203650", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "component_scores": {"eps": 9, "visibility": 14, "bottleneck": 7, "mispricing": 15, "valuation": 8, "capital": 6, "info": 7}, "raw_total_score": 66, "simulated_stage_without_C28_bridge_guard": "Stage2-Actionable", "simulated_stage_with_C28_bridge_guard": "Stage4B-LocalWatch", "bridge_required": "verified_retention_renewal_revenue_margin_or_FCF_bridge", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8-L102-04", "symbol": "131370", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "component_scores": {"eps": 8, "visibility": 13, "bottleneck": 5, "mispricing": 12, "valuation": 9, "capital": 6, "info": 9}, "raw_total_score": 62, "simulated_stage_without_C28_bridge_guard": "Stage2-Watch", "simulated_stage_with_C28_bridge_guard": "Stage4B-LocalWatch", "bridge_required": "verified_retention_renewal_revenue_margin_or_FCF_bridge", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8-L102-05", "symbol": "060850", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "component_scores": {"eps": 7, "visibility": 15, "bottleneck": 5, "mispricing": 12, "valuation": 10, "capital": 7, "info": 8}, "raw_total_score": 64, "simulated_stage_without_C28_bridge_guard": "Stage2-Watch", "simulated_stage_with_C28_bridge_guard": "Stage2-Blocked", "bridge_required": "verified_retention_renewal_revenue_margin_or_FCF_bridge", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8-L102-06", "symbol": "065370", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "component_scores": {"eps": 5, "visibility": 12, "bottleneck": 4, "mispricing": 16, "valuation": 7, "capital": 5, "info": 10}, "raw_total_score": 59, "simulated_stage_without_C28_bridge_guard": "Stage2-Watch", "simulated_stage_with_C28_bridge_guard": "Stage4B-LocalWatch", "bridge_required": "verified_retention_renewal_revenue_margin_or_FCF_bridge", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C28-R8-L102-07", "symbol": "307950", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "component_scores": {"eps": 16, "visibility": 21, "bottleneck": 7, "mispricing": 12, "valuation": 5, "capital": 9, "info": 8}, "raw_total_score": 78, "simulated_stage_without_C28_bridge_guard": "Stage3-Yellow", "simulated_stage_with_C28_bridge_guard": "Stage2-Blocked", "bridge_required": "verified_retention_renewal_revenue_margin_or_FCF_bridge", "production_scoring_changed": false}
```

## 13. Aggregate JSON

```json
{
  "row_type": "aggregate",
  "selected_round": "R8",
  "selected_loop": 102,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "trigger_row_count": 7,
  "calibration_usable_trigger_count": 7,
  "representative_trigger_count": 7,
  "new_independent_case_count": 7,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 7,
  "positive_case_count": 2,
  "counterexample_count": 5,
  "stage4b_case_count": 3,
  "stage4c_case_count": 0,
  "current_profile_error_count": 7,
  "source_proxy_only_count": 5,
  "evidence_url_pending_count": 5,
  "auto_selected_coverage_gap": "C28 base index 28 + local loop100 6 + loop101 7 + loop102 7 = local-session adjusted about 48; 2 short of 50-row practical calibration band"
}
```

## 14. Residual Contribution Summary

```json
{
  "row_type": "residual_contribution",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "new_axis_proposed": "C28_verified_retention_renewal_revenue_margin_FCF_bridge_required_before_Yellow_or_Green_plus_AI_security_or_cloud_software_label_to_local_4B_watch_v3",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "full_4b_requires_non_price_evidence",
    "price_only_blowoff_blocks_positive_stage"
  ],
  "existing_axis_weakened": null,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "do_not_propose_new_weight_delta": false,
  "promotion_blocked_until_url_repair": "true_for_source_proxy_rows"
}
```

## 15. Shadow Rule Candidate

```text
if canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
    require one of:
      - verified retention / renewal / maintenance revenue
      - quantified cloud/SaaS/ERP/security revenue contribution
      - margin or FCF bridge after contract expansion
      - large-enterprise customer expansion with revision support
    before Stage3-Yellow or Stage3-Green
    if evidence is only AI/security/cloud/software label or one-off project headline:
      route to Stage2-blocked or Stage4B-LocalWatch
    if valuation/MAE risk is high even with enterprise software bridge:
      keep Actionable but block Green until revision and drawdown guard pass
```

## 16. Validation Scope

- `calibration_usable=true` for all seven trigger rows because 30/90/180D fields are complete and the selected entry windows fit before `2026-02-20`.
- `promotion_blocked_until_url_repair=true` for source-proxy rows. These rows may still be useful as guardrail/counterexample evidence, but scoped positive promotion should wait for URL repair.
- No production scoring or runtime profile is changed by this MD.

## 17. Deferred Coding Agent Handoff Prompt — not executed

```text
Read this MD as a v12 calibration artifact only. Parse JSONL rows with row_type in [case, trigger, score_simulation, aggregate, residual_contribution]. Validate every trigger row against stock-web tradable_raw shards and corporate-action windows. Do not change production scoring from this file alone. If the rows pass validation and broader C28 aggregate statistics support it, consider a scoped C28 bridge guard: require verified retention/renewal/revenue/margin/FCF bridge before Yellow/Green, and route AI/security/cloud/software label-only spikes to local 4B watch or Stage2-blocked.
```

## 18. Compliance Notes

- No live candidate scan performed.
- No current stock recommendation made.
- No broker/API integration performed.
- No stock_agent source-code patch performed.
- No production scoring mutation performed.
- This is historical calibration research only.

## 19. Next Research State

```json
{
  "completed_round": "R8",
  "completed_loop": 102,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 1-under-50 after local-session adjustment; published index Priority 0",
  "next_recommended_archetypes": [
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
    "C11_BATTERY_ORDERBOOK_RERATING",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C14_EV_DEMAND_SLOWDOWN_4B_4C",
    "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF"
  ],
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass"
}
```

```text
completed_round = R8
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C11_BATTERY_ORDERBOOK_RERATING, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C14_EV_DEMAND_SLOWDOWN_4B_4C, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 20. File Identity

`e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md`