# E2R Stock-Web V12 Residual Calibration Research

```yaml
generated_at_kst: "2026-06-13"
main_execution_prompt: "docs/core/e2r_v12_prompt_round_scheduler_corrected.txt"
no_repeat_index: "docs/core/V12_Research_No_Repeat_Index.md"
selected_round: "R8"
selected_loop: 101
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L8_PLATFORM_CONTENT_SW_SECURITY"
canonical_archetype_id: "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"
fine_archetype_id: "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE"
deep_sub_archetype_id: "C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE"
loop_objective: "coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery"
price_data_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
upstream_source: "FinanceData/marcap"
```

## 0. Execution guardrail

This file is a standalone historical calibration artifact. It is not a live scan, not a current stock recommendation, not an automated-trading instruction, and not a production scoring patch. The only production-facing material is a deferred shadow-rule candidate for a later coding-agent batch.

The selected archetype is `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` because the published coverage ledger shows C28 at 28 rows, and this conversation has only one prior local C28 standard file (`R8_loop_100`). After that local loop, C28 remains below the 50-row practical calibration band, while most Priority-0 archetypes in this session have already been brought above the 30-row stability band.

## 1. No-repeat and novelty gate

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Previous local C28 loop-100 symbols were avoided: `258790`, `356890`, `184230`, `049470`, `294570`, `053580`. Two older/well-covered C28 software-security symbols are reused only as new trigger-family/date examples because C28 needs positive balance repair: `053800`, `263860`.

Selected symbols for this loop:

| case_id | symbol | name | novelty status | representative trigger |
|---|---:|---|---|---|
| C28-R8-L101-01 | 053800 | 안랩 | reused symbol, new trigger family/date | Stage2-Actionable, 2024-10-02 |
| C28-R8-L101-02 | 263860 | 지니언스 | reused symbol, new trigger family/date | Stage2-Actionable, 2024-08-01 |
| C28-R8-L101-03 | 150900 | 파수 | new vs local loop-100 | Stage4B, 2024-03-27 |
| C28-R8-L101-04 | 434480 | 모니터랩 | new vs local loop-100 | Stage4B, 2024-07-18 |
| C28-R8-L101-05 | 411080 | 샌즈랩 | new vs local loop-100 | Stage4B, 2024-05-03 |
| C28-R8-L101-06 | 430690 | 한싹 | new vs local loop-100 | Stage4B, 2024-08-21 |
| C28-R8-L101-07 | 208350 | 지란지교시큐리티 | new vs local loop-100 | Stage2, 2024-07-01 entry |

Novelty summary:

```text
new_independent_case_count = 7
same_archetype_new_symbol_count = 5
reused_symbol_new_trigger_family_count = 2
representative_trigger_count = 7
hard_duplicate_count = 0
```

## 2. Stock-Web price atlas validation

This run uses the `Songdaiki/stock-web` tradable OHLC shards:

```text
atlas/symbol_profiles/{prefix}/{symbol}.json
atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv
```

Validation rules used:

- `price_basis = tradable_raw`
- `price_adjustment_status = raw_unadjusted_marcap`
- MFE/MAE computed from post-entry high/low paths at 30/90/180 trading-day windows.
- Corporate-action candidate windows are blocked or downgraded unless the selected entry window is outside the candidate range.
- Raw/unadjusted price caveat is retained in every machine-readable row.

Symbol profile checks:

| symbol | name | profile path | CA candidates | handling |
|---:|---|---|---|---|
| 053800 | 안랩 | `atlas/symbol_profiles/053/053800.json` | `2005-03-31` | selected 2024 window clear; old split candidate far outside 180D |
| 263860 | 지니언스 | `atlas/symbol_profiles/263/263860.json` | `2018-02-22` | selected 2024 window clear; old CA candidate outside 180D |
| 150900 | 파수 | `atlas/symbol_profiles/150/150900.json` | `none` | no corporate-action candidate in profile |
| 434480 | 모니터랩 | `atlas/symbol_profiles/434/434480.json` | `none` | no corporate-action candidate in profile |
| 411080 | 샌즈랩 | `atlas/symbol_profiles/411/411080.json` | `none` | no corporate-action candidate in profile |
| 430690 | 한싹 | `atlas/symbol_profiles/430/430690.json` | `2024-04-29, 2024-05-24` | entry placed after 2024 CA candidates; promotion caution retained |
| 208350 | 지란지교시큐리티 | `atlas/symbol_profiles/208/208350.json` | `2016-09-09, 2019-10-21` | selected 2024 window clear; older CA candidates outside 180D |

Narrative-only exclusion:

| symbol | name | reason |
|---:|---|---|
| 042510 | 라온시큐어 | relevant digital-ID/FIDO evidence, but the 2024-08 entry path overlaps a 2025-05-07 corporate-action candidate and is excluded from calibration rows. |

## 3. Archetype residual problem

C28 is structurally tricky because the market can price every cybersecurity, SaaS, zero-trust, authentication, AI-security, and cloud-security keyword as if it were recurring ARR. In reality, Korean security-software names often mix product license, maintenance, SI/project revenue, consulting, public-sector cycles, and one-off certification or project headlines.

Residual question:

```text
Can C28 move to Yellow/Green from security-label price strength alone?
Answer proposed by this loop: no.
C28 needs verified retention, renewal, revenue quality, margin bridge, or customer expansion that maps into financials.
Otherwise, security-label strength is Stage2-blocked or local 4B watch.
```

## 4. Representative trigger-level OHLC table

| case | symbol | name | trigger | entry | entry price | outcome | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| C28-R8-L101-01 | 053800 | 안랩 | Stage2-Actionable | 2024-10-02 | 54100 | positive | 17.38% | -4.99% | 65.25% | -4.99% | 115.71% | -4.99% |
| C28-R8-L101-02 | 263860 | 지니언스 | Stage2-Actionable | 2024-08-01 | 9980 | positive | 19.54% | -10.82% | 19.54% | -14.03% | 135.97% | -14.03% |
| C28-R8-L101-03 | 150900 | 파수 | Stage4B | 2024-03-27 | 6580 | counterexample | 20.21% | -9.12% | 20.21% | -20.97% | 20.21% | -37.54% |
| C28-R8-L101-04 | 434480 | 모니터랩 | Stage4B | 2024-07-18 | 4230 | counterexample | 27.19% | -30.26% | 39.01% | -30.26% | 45.15% | -34.28% |
| C28-R8-L101-05 | 411080 | 샌즈랩 | Stage4B | 2024-05-03 | 11900 | counterexample | 10.34% | -22.86% | 10.34% | -56.13% | 10.34% | -56.13% |
| C28-R8-L101-06 | 430690 | 한싹 | Stage4B | 2024-08-21 | 5960 | counterexample | 44.46% | -8.72% | 44.46% | -44.80% | 44.46% | -44.80% |
| C28-R8-L101-07 | 208350 | 지란지교시큐리티 | Stage2 | 2024-07-01 | 3575 | counterexample | 4.34% | -22.80% | 8.53% | -22.80% | 8.53% | -30.07% |

## 5. Case notes

### C28-R8-L101-01 — 053800 안랩

- Trigger: `Stage2-Actionable` on `2024-10-02`, entry `2024-10-02` at `54100`.
- Evidence family: `verified_endpoint_security_revenue_base`.
- Evidence URL: https://m.boannews.com/html/detail.html?idx=131659&skind=8
- Path result: MFE90 `65.25%`, MAE90 `-4.99%`, MFE180 `115.71%`, MAE180 `-4.99%`.
- Residual label: `verified endpoint/NAC-like security revenue base -> allow Actionable, Green still needs revision bridge`.
- Current profile stress: `too_conservative_if_recurring_security_revenue_base_is_ignored`.

### C28-R8-L101-02 — 263860 지니언스

- Trigger: `Stage2-Actionable` on `2024-08-01`, entry `2024-08-01` at `9980`.
- Evidence family: `verified_NAC_EDR_zero_trust_revenue_bridge`.
- Evidence URL: https://www.genians.co.kr/pr-room/press/20240801
- Path result: MFE90 `19.54%`, MAE90 `-14.03%`, MFE180 `135.97%`, MAE180 `-14.03%`.
- Residual label: `NAC/EDR revenue bridge and customer expansion -> do not block Stage2-Actionable`.
- Current profile stress: `too_conservative_if_NAC_EDR_revenue_bridge_is_not_recognized`.

### C28-R8-L101-03 — 150900 파수

- Trigger: `Stage4B` on `2024-03-27`, entry `2024-03-27` at `6580`.
- Evidence family: `data_security_platform_label_without_near_term_revision`.
- Evidence URL: https://www.fasoo.ai/solutions/fasoo-data-security-platform
- Path result: MFE90 `20.21%`, MAE90 `-20.97%`, MFE180 `20.21%`, MAE180 `-37.54%`.
- Residual label: `data security platform label without renewal/revision bridge -> local 4B watch`.
- Current profile stress: `false_positive_if_data_security_label_is_promoted_without_renewal_or_revision_bridge`.

### C28-R8-L101-04 — 434480 모니터랩

- Trigger: `Stage4B` on `2024-07-18`, entry `2024-07-18` at `4230`.
- Evidence family: `SASE_cloud_security_customer_count_without_margin_bridge`.
- Evidence URL: https://m.boannews.com/html/detail.html?idx=131425
- Path result: MFE90 `39.01%`, MAE90 `-30.26%`, MFE180 `45.15%`, MAE180 `-34.28%`.
- Residual label: `SASE/customer-count story with high MAE -> local 4B watch until margin bridge`.
- Current profile stress: `false_positive_if_customer_count_and_overseas_label_promote_without_margin_bridge`.

### C28-R8-L101-05 — 411080 샌즈랩

- Trigger: `Stage4B` on `2024-05-03`, entry `2024-05-03` at `11900`.
- Evidence family: `AI_threat_intelligence_government_project_without_recurring_contract_bridge`.
- Evidence URL: https://securities.miraeasset.com/bbs/download/2129356.pdf?attachmentId=2129356
- Path result: MFE90 `10.34%`, MAE90 `-56.13%`, MFE180 `10.34%`, MAE180 `-56.13%`.
- Residual label: `AI threat-intelligence project headline without recurring revenue bridge -> 4B watch`.
- Current profile stress: `false_positive_if_AI_security_project_headline_is_treated_as_retention_bridge`.

### C28-R8-L101-06 — 430690 한싹

- Trigger: `Stage4B` on `2024-08-21`, entry `2024-08-21` at `5960`.
- Evidence family: `cloud_network_separation_security_growth_after_CA_window`.
- Evidence URL: https://w4.kirs.or.kr/download/research/240821_%ED%95%9C%EC%8B%B9.pdf
- Path result: MFE90 `44.46%`, MAE90 `-44.80%`, MFE180 `44.46%`, MAE180 `-44.80%`.
- Residual label: `cloud/network-separation security story after CA window still needs maintenance revenue bridge`.
- Current profile stress: `false_positive_if_network_separation_security_growth_is_promoted_without_stable_retention_bridge`.

### C28-R8-L101-07 — 208350 지란지교시큐리티

- Trigger: `Stage2` on `2024-06-30`, entry `2024-07-01` at `3575`.
- Evidence family: `mail_document_security_export_customer_story_without_revision`.
- Evidence URL: https://story.jiran.com/%EC%84%B8%EA%B3%84%EB%A1%9C-%EB%8F%84%EC%A0%84%ED%95%98%EB%8A%94-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD-%EC%82%AC%EC%9D%B4%EB%B2%84-%EB%B3%B4%EC%95%88-%EA%B8%B0%EC%97%85%EB%93%A4-%E2%91%A6-%EC%A7%80/
- Path result: MFE90 `8.53%`, MAE90 `-22.80%`, MFE180 `8.53%`, MAE180 `-30.07%`.
- Residual label: `overseas customer narrative without quantified revenue retention -> Stage2-blocked`.
- Current profile stress: `false_positive_if_customer_story_is_treated_as_contract_retention_without_revenue_bridge`.


## 6. Positive / counterexample balance

```text
positive_case_count = 2
counterexample_count = 5
stage4b_case_count = 4
stage4c_case_count = 0
current_profile_error_count = 7
```

Positive rows (`053800`, `263860`) show that C28 should not blindly block real enterprise security-software businesses with verified revenue/customer bridge. The five counterexample rows show the opposite edge: security labels, AI threat-intelligence headlines, SASE customer-count stories, network-separation growth claims, and overseas customer narratives are not enough for Yellow/Green when renewal/revenue/margin bridge is absent or the path carries high MAE.

## 7. Current calibrated profile stress test

Current global profile assumptions retained:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual error pattern found:

1. The current profile can still be too conservative when a C28 company has real revenue/customer bridge but the bridge is classified only as generic software quality.
2. It can also be too loose when security-label, AI-security, or SASE wording is promoted without renewal, ARR/maintenance, revenue, or margin evidence.
3. Therefore the desired rule is not global threshold loosening. It is a C28-specific bridge gate.

## 8. Local 4B versus full 4B split

Local 4B watch applies when price has already paid for the security narrative but non-price bridge has not caught up. Full 4B should remain reserved for confirmed non-price deterioration: lost renewal, customer churn, failed revenue conversion, margin break, or credibility/trust impairment.

This loop mainly strengthens local 4B watch, not full 4B or 4C.

## 9. Residual rule candidate

```text
rule_id = C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_v2
scope = canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
if security/SaaS/zero-trust/authentication/cloud-security label exists but verified renewal/revenue/margin bridge is absent:
    cap at Stage2-blocked or local_4B_watch
if verified revenue/customer/retention bridge exists and MAE is controlled:
    allow Stage2-Actionable
if revision_score < 55:
    do not allow Stage3-Green
```

## 10. Shadow weight candidate, not applied

```yaml
shadow_weight_only: true
production_scoring_changed: false
contract_score: "+2 shadow when renewal/retention is verified"
margin_bridge_score: "+2 shadow when security revenue converts to OPM/FCF"
revision_score: "+1 shadow when customer expansion appears in guidance or estimates"
valuation_repricing_score: "-2 shadow when move is price-only label spike"
information_confidence_gate: "+1 verified URL / contract / filing bridge requirement"
```

## 11. Coverage matrix contribution

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE | 2 | 5 | 4 | 0 | 7 | 2 | 7 | 7 | 7 | true | true | published 28 -> local-session adjusted about 41; need about 9 to 50 |

```text
published_index_C28_rows = 28
local_loop100_representative_triggers = 6
this_loop101_representative_triggers = 7
local_session_adjusted_C28_rows_estimate = approximately 41
need_to_50_after_this_loop = approximately 9
```

## 12. Data-quality and promotion caveats

- `150900` is retained as `source_proxy_only=true` because the trigger date is a security-platform proxy rather than a single dated contract/revenue event.
- `411080` uses a broker/news digest PDF as proxy for the May 2024 project and certification headlines.
- `042510` is explicitly narrative-only because its most attractive 2024 digital-ID path overlaps a later raw corporate-action candidate within 180 trading days.
- Rows with `source_proxy_only=true` should not be used for positive promotion until URL repair is completed.

## 13. Machine-readable rows

```jsonl
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-01", "current_profile_error": "too_conservative_if_recurring_security_revenue_base_is_ignored", "entry_date": "2024-10-02", "evidence_family": "verified_endpoint_security_revenue_base", "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "안랩", "novelty_status": "new independent hard-key; symbol may be previously covered only when explicitly noted", "outcome_label": "positive", "residual_label": "verified endpoint/NAC-like security revenue base -> allow Actionable, Green still needs revision bridge", "row_type": "case", "symbol": "053800", "trigger_date": "2024-10-02", "trigger_type": "Stage2-Actionable"}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-02", "current_profile_error": "too_conservative_if_NAC_EDR_revenue_bridge_is_not_recognized", "entry_date": "2024-08-01", "evidence_family": "verified_NAC_EDR_zero_trust_revenue_bridge", "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "지니언스", "novelty_status": "new independent hard-key; symbol may be previously covered only when explicitly noted", "outcome_label": "positive", "residual_label": "NAC/EDR revenue bridge and customer expansion -> do not block Stage2-Actionable", "row_type": "case", "symbol": "263860", "trigger_date": "2024-08-01", "trigger_type": "Stage2-Actionable"}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-03", "current_profile_error": "false_positive_if_data_security_label_is_promoted_without_renewal_or_revision_bridge", "entry_date": "2024-03-27", "evidence_family": "data_security_platform_label_without_near_term_revision", "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "파수", "novelty_status": "new independent hard-key; symbol may be previously covered only when explicitly noted", "outcome_label": "counterexample", "residual_label": "data security platform label without renewal/revision bridge -> local 4B watch", "row_type": "case", "symbol": "150900", "trigger_date": "2024-03-27", "trigger_type": "Stage4B"}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-04", "current_profile_error": "false_positive_if_customer_count_and_overseas_label_promote_without_margin_bridge", "entry_date": "2024-07-18", "evidence_family": "SASE_cloud_security_customer_count_without_margin_bridge", "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "모니터랩", "novelty_status": "new independent hard-key; symbol may be previously covered only when explicitly noted", "outcome_label": "counterexample", "residual_label": "SASE/customer-count story with high MAE -> local 4B watch until margin bridge", "row_type": "case", "symbol": "434480", "trigger_date": "2024-07-18", "trigger_type": "Stage4B"}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-05", "current_profile_error": "false_positive_if_AI_security_project_headline_is_treated_as_retention_bridge", "entry_date": "2024-05-03", "evidence_family": "AI_threat_intelligence_government_project_without_recurring_contract_bridge", "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "샌즈랩", "novelty_status": "new independent hard-key; symbol may be previously covered only when explicitly noted", "outcome_label": "counterexample", "residual_label": "AI threat-intelligence project headline without recurring revenue bridge -> 4B watch", "row_type": "case", "symbol": "411080", "trigger_date": "2024-05-03", "trigger_type": "Stage4B"}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-06", "current_profile_error": "false_positive_if_network_separation_security_growth_is_promoted_without_stable_retention_bridge", "entry_date": "2024-08-21", "evidence_family": "cloud_network_separation_security_growth_after_CA_window", "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "한싹", "novelty_status": "new independent hard-key; symbol may be previously covered only when explicitly noted", "outcome_label": "counterexample", "residual_label": "cloud/network-separation security story after CA window still needs maintenance revenue bridge", "row_type": "case", "symbol": "430690", "trigger_date": "2024-08-21", "trigger_type": "Stage4B"}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-07", "current_profile_error": "false_positive_if_customer_story_is_treated_as_contract_retention_without_revenue_bridge", "entry_date": "2024-07-01", "evidence_family": "mail_document_security_export_customer_story_without_revision", "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "name": "지란지교시큐리티", "novelty_status": "new independent hard-key; symbol may be previously covered only when explicitly noted", "outcome_label": "counterexample", "residual_label": "overseas customer narrative without quantified revenue retention -> Stage2-blocked", "row_type": "case", "symbol": "208350", "trigger_date": "2024-06-30", "trigger_type": "Stage2"}
{"MAE_180D_pct": -4.99, "MAE_1Y_pct": -4.99, "MAE_30D_pct": -4.99, "MAE_90D_pct": -4.99, "MFE_180D_pct": 115.71, "MFE_1Y_pct": 115.71, "MFE_2Y_pct": null, "MFE_30D_pct": 17.38, "MFE_90D_pct": 65.25, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-01", "company_name": "안랩", "corporate_action_window_status": "clear_for_selected_180D_window", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.1, "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|Stage2-Actionable|2024-10-02", "entry_date": "2024-10-02", "entry_price": 54100.0, "evidence_available_at_that_date": "verified_endpoint_security_revenue_base", "evidence_family": "verified_endpoint_security_revenue_base", "evidence_source": "https://m.boannews.com/html/detail.html?idx=131659&skind=8", "evidence_url": "https://m.boannews.com/html/detail.html?idx=131659&skind=8", "evidence_url_pending": false, "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4B_trigger", "four_c_protection_label": "not_applicable_no_4C_trigger", "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "loop": "101", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "name": "안랩", "outcome_label": "positive", "peak_date": "2025-04-07", "peak_price": 116700.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv", "primary_archetype": "software_security_contract_retention", "profile_corporate_action_candidate_dates": ["2005-03-31"], "profile_error": "too_conservative_if_recurring_security_revenue_base_is_ignored", "profile_path": "atlas/symbol_profiles/053/053800.json", "reuse_reason": "reused_symbol_new_trigger_family_date", "round": "R8", "row_type": "trigger", "same_entry_group_id": "C28|053800|Stage2-Actionable|2024-10-02", "sector": "platform_content_sw_security", "source_proxy_only": false, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources", "repeat_order_or_conversion", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "053800", "trigger_date": "2024-10-02", "trigger_id": "C28-R8-L101-01-Stage2-Actionable-2024-10-02", "trigger_outcome_label": "positive_verified_endpoint_security_revenue_base", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -14.03, "MAE_1Y_pct": -14.03, "MAE_30D_pct": -10.82, "MAE_90D_pct": -14.03, "MFE_180D_pct": 135.97, "MFE_1Y_pct": 139.48, "MFE_2Y_pct": null, "MFE_30D_pct": 19.54, "MFE_90D_pct": 19.54, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-02", "company_name": "지니언스", "corporate_action_window_status": "clear_for_selected_180D_window", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -26.41, "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2-Actionable|2024-08-01", "entry_date": "2024-08-01", "entry_price": 9980.0, "evidence_available_at_that_date": "verified_NAC_EDR_zero_trust_revenue_bridge", "evidence_family": "verified_NAC_EDR_zero_trust_revenue_bridge", "evidence_source": "https://www.genians.co.kr/pr-room/press/20240801", "evidence_url": "https://www.genians.co.kr/pr-room/press/20240801", "evidence_url_pending": false, "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4B_trigger", "four_c_protection_label": "not_applicable_no_4C_trigger", "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "loop": "101", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "name": "지니언스", "outcome_label": "positive", "peak_date": "2025-04-28", "peak_price": 23550.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv", "primary_archetype": "software_security_contract_retention", "profile_corporate_action_candidate_dates": ["2018-02-22"], "profile_error": "too_conservative_if_NAC_EDR_revenue_bridge_is_not_recognized", "profile_path": "atlas/symbol_profiles/263/263860.json", "reuse_reason": "reused_symbol_new_trigger_family_date", "round": "R8", "row_type": "trigger", "same_entry_group_id": "C28|263860|Stage2-Actionable|2024-08-01", "sector": "platform_content_sw_security", "source_proxy_only": false, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources", "repeat_order_or_conversion", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "263860", "trigger_date": "2024-08-01", "trigger_id": "C28-R8-L101-02-Stage2-Actionable-2024-08-01", "trigger_outcome_label": "positive_verified_NAC_EDR_zero_trust_revenue_bridge", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -37.54, "MAE_1Y_pct": -37.54, "MAE_30D_pct": -9.12, "MAE_90D_pct": -20.97, "MFE_180D_pct": 20.21, "MFE_1Y_pct": 20.21, "MFE_2Y_pct": null, "MFE_30D_pct": 20.21, "MFE_90D_pct": 20.21, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-03", "company_name": "파수", "corporate_action_window_status": "clear_for_selected_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.04, "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|150900|Stage4B|2024-03-27", "entry_date": "2024-03-27", "entry_price": 6580.0, "evidence_available_at_that_date": "data_security_platform_label_without_near_term_revision", "evidence_family": "data_security_platform_label_without_near_term_revision", "evidence_source": "https://www.fasoo.ai/solutions/fasoo-data-security-platform", "evidence_url": "https://www.fasoo.ai/solutions/fasoo-data-security-platform", "evidence_url_pending": true, "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "four_b_full_window_peak_proximity": 1.0, "four_b_local_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_watch_not_full_4B", "four_c_protection_label": "not_applicable_no_4C_trigger", "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "loop": "101", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "name": "파수", "outcome_label": "counterexample", "peak_date": "2024-04-01", "peak_price": 7910.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv", "primary_archetype": "software_security_contract_retention", "profile_corporate_action_candidate_dates": [], "profile_error": "false_positive_if_data_security_label_is_promoted_without_renewal_or_revision_bridge", "profile_path": "atlas/symbol_profiles/150/150900.json", "reuse_reason": null, "round": "R8", "row_type": "trigger", "same_entry_group_id": "C28|150900|Stage4B|2024-03-27", "sector": "platform_content_sw_security", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "150900", "trigger_date": "2024-03-27", "trigger_id": "C28-R8-L101-03-Stage4B-2024-03-27", "trigger_outcome_label": "counterexample_data_security_platform_label_without_near_term_revision", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -34.28, "MAE_1Y_pct": -34.28, "MAE_30D_pct": -30.26, "MAE_90D_pct": -30.26, "MFE_180D_pct": 45.15, "MFE_1Y_pct": 45.15, "MFE_2Y_pct": null, "MFE_30D_pct": 27.19, "MFE_90D_pct": 39.01, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-04", "company_name": "모니터랩", "corporate_action_window_status": "clear_for_selected_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -43.81, "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|434480|Stage4B|2024-07-18", "entry_date": "2024-07-18", "entry_price": 4230.0, "evidence_available_at_that_date": "SASE_cloud_security_customer_count_without_margin_bridge", "evidence_family": "SASE_cloud_security_customer_count_without_margin_bridge", "evidence_source": "https://m.boannews.com/html/detail.html?idx=131425", "evidence_url": "https://m.boannews.com/html/detail.html?idx=131425", "evidence_url_pending": false, "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "four_b_full_window_peak_proximity": 1.0, "four_b_local_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_watch_not_full_4B", "four_c_protection_label": "not_applicable_no_4C_trigger", "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "loop": "101", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "name": "모니터랩", "outcome_label": "counterexample", "peak_date": "2025-02-06", "peak_price": 6140.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/434/434480/2024.csv", "primary_archetype": "software_security_contract_retention", "profile_corporate_action_candidate_dates": [], "profile_error": "false_positive_if_customer_count_and_overseas_label_promote_without_margin_bridge", "profile_path": "atlas/symbol_profiles/434/434480.json", "reuse_reason": null, "round": "R8", "row_type": "trigger", "same_entry_group_id": "C28|434480|Stage4B|2024-07-18", "sector": "platform_content_sw_security", "source_proxy_only": false, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "434480", "trigger_date": "2024-07-18", "trigger_id": "C28-R8-L101-04-Stage4B-2024-07-18", "trigger_outcome_label": "counterexample_SASE_cloud_security_customer_count_without_margin_bridge", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -56.13, "MAE_1Y_pct": -56.13, "MAE_30D_pct": -22.86, "MAE_90D_pct": -56.13, "MFE_180D_pct": 10.34, "MFE_1Y_pct": 10.34, "MFE_2Y_pct": null, "MFE_30D_pct": 10.34, "MFE_90D_pct": 10.34, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-05", "company_name": "샌즈랩", "corporate_action_window_status": "clear_for_selected_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -60.24, "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|411080|Stage4B|2024-05-03", "entry_date": "2024-05-03", "entry_price": 11900.0, "evidence_available_at_that_date": "AI_threat_intelligence_government_project_without_recurring_contract_bridge", "evidence_family": "AI_threat_intelligence_government_project_without_recurring_contract_bridge", "evidence_source": "https://securities.miraeasset.com/bbs/download/2129356.pdf?attachmentId=2129356", "evidence_url": "https://securities.miraeasset.com/bbs/download/2129356.pdf?attachmentId=2129356", "evidence_url_pending": false, "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_b_full_window_peak_proximity": 1.0, "four_b_local_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_watch_not_full_4B", "four_c_protection_label": "not_applicable_no_4C_trigger", "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "loop": "101", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "name": "샌즈랩", "outcome_label": "counterexample", "peak_date": "2024-05-03", "peak_price": 13130.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/411/411080/2024.csv", "primary_archetype": "software_security_contract_retention", "profile_corporate_action_candidate_dates": [], "profile_error": "false_positive_if_AI_security_project_headline_is_treated_as_retention_bridge", "profile_path": "atlas/symbol_profiles/411/411080.json", "reuse_reason": null, "round": "R8", "row_type": "trigger", "same_entry_group_id": "C28|411080|Stage4B|2024-05-03", "sector": "platform_content_sw_security", "source_proxy_only": true, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "411080", "trigger_date": "2024-05-03", "trigger_id": "C28-R8-L101-05-Stage4B-2024-05-03", "trigger_outcome_label": "counterexample_AI_threat_intelligence_government_project_without_recurring_contract_bridge", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.8, "MAE_1Y_pct": -44.8, "MAE_30D_pct": -8.72, "MAE_90D_pct": -44.8, "MFE_180D_pct": 44.46, "MFE_1Y_pct": 44.46, "MFE_2Y_pct": null, "MFE_30D_pct": 44.46, "MFE_90D_pct": 44.46, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-06", "company_name": "한싹", "corporate_action_window_status": "entry_after_CA_candidates_promotion_caution", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.79, "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|430690|Stage4B|2024-08-21", "entry_date": "2024-08-21", "entry_price": 5960.0, "evidence_available_at_that_date": "cloud_network_separation_security_growth_after_CA_window", "evidence_family": "cloud_network_separation_security_growth_after_CA_window", "evidence_source": "https://w4.kirs.or.kr/download/research/240821_%ED%95%9C%EC%8B%B9.pdf", "evidence_url": "https://w4.kirs.or.kr/download/research/240821_%ED%95%9C%EC%8B%B9.pdf", "evidence_url_pending": false, "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_b_full_window_peak_proximity": 1.0, "four_b_local_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_watch_not_full_4B", "four_c_protection_label": "not_applicable_no_4C_trigger", "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "loop": "101", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "name": "한싹", "outcome_label": "counterexample", "peak_date": "2024-08-28", "peak_price": 8610.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/430/430690/2024.csv", "primary_archetype": "software_security_contract_retention", "profile_corporate_action_candidate_dates": ["2024-04-29", "2024-05-24"], "profile_error": "false_positive_if_network_separation_security_growth_is_promoted_without_stable_retention_bridge", "profile_path": "atlas/symbol_profiles/430/430690.json", "reuse_reason": null, "round": "R8", "row_type": "trigger", "same_entry_group_id": "C28|430690|Stage4B|2024-08-21", "sector": "platform_content_sw_security", "source_proxy_only": false, "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "430690", "trigger_date": "2024-08-21", "trigger_id": "C28-R8-L101-06-Stage4B-2024-08-21", "trigger_outcome_label": "counterexample_cloud_network_separation_security_growth_after_CA_window", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -30.07, "MAE_1Y_pct": -30.07, "MAE_30D_pct": -22.8, "MAE_90D_pct": -22.8, "MFE_180D_pct": 8.53, "MFE_1Y_pct": 8.53, "MFE_2Y_pct": null, "MFE_30D_pct": 4.34, "MFE_90D_pct": 8.53, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-07", "company_name": "지란지교시큐리티", "corporate_action_window_status": "clear_for_selected_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -35.57, "duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|208350|Stage2|2024-07-01", "entry_date": "2024-07-01", "entry_price": 3575.0, "evidence_available_at_that_date": "mail_document_security_export_customer_story_without_revision", "evidence_family": "mail_document_security_export_customer_story_without_revision", "evidence_source": "https://story.jiran.com/%EC%84%B8%EA%B3%84%EB%A1%9C-%EB%8F%84%EC%A0%84%ED%95%98%EB%8A%94-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD-%EC%82%AC%EC%9D%B4%EB%B2%84-%EB%B3%B4%EC%95%88-%EA%B8%B0%EC%97%85%EB%93%A4-%E2%91%A6-%EC%A7%80/", "evidence_url": "https://story.jiran.com/%EC%84%B8%EA%B3%84%EB%A1%9C-%EB%8F%84%EC%A0%84%ED%95%98%EB%8A%94-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD-%EC%82%AC%EC%9D%B4%EB%B2%84-%EB%B3%B4%EC%95%88-%EA%B8%B0%EC%97%85%EB%93%A4-%E2%91%A6-%EC%A7%80/", "evidence_url_pending": false, "fine_archetype_id": "C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable_no_4B_trigger", "four_c_protection_label": "not_applicable_no_4C_trigger", "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "loop": "101", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "name": "지란지교시큐리티", "outcome_label": "counterexample", "peak_date": "2024-08-28", "peak_price": 3880.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/208/208350/2024.csv", "primary_archetype": "software_security_contract_retention", "profile_corporate_action_candidate_dates": ["2016-09-09", "2019-10-21"], "profile_error": "false_positive_if_customer_story_is_treated_as_contract_retention_without_revenue_bridge", "profile_path": "atlas/symbol_profiles/208/208350.json", "reuse_reason": null, "round": "R8", "row_type": "trigger", "same_entry_group_id": "C28|208350|Stage2|2024-07-01", "sector": "platform_content_sw_security", "source_proxy_only": false, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "208350", "trigger_date": "2024-06-30", "trigger_id": "C28-R8-L101-07-Stage2-2024-07-01", "trigger_outcome_label": "counterexample_mail_document_security_export_customer_story_without_revision", "trigger_type": "Stage2", "upstream_source": "FinanceData/marcap"}
{"after_stage_estimate": "Stage2-Actionable", "after_total_score": 80, "before_stage_estimate": "Stage2", "before_total_score": 73, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-01", "row_type": "score_simulation", "rule_effect": "requires verified retention/renewal/revenue/margin bridge before Yellow/Green; otherwise C28 security-label strength is capped at Stage2-blocked or local 4B watch", "scores_after": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 62, "contract_score": 70, "customer_quality_score": 76, "dilution_cb_risk_score": 8, "execution_risk_score": 18, "legal_or_contract_risk_score": 10, "margin_bridge_score": 58, "policy_or_regulatory_score": 52, "relative_strength_score": 62, "revision_score": 50, "valuation_repricing_score": 54}, "scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 52, "contract_score": 62, "customer_quality_score": 70, "dilution_cb_risk_score": 8, "execution_risk_score": 22, "legal_or_contract_risk_score": 12, "margin_bridge_score": 48, "policy_or_regulatory_score": 48, "relative_strength_score": 54, "revision_score": 44, "valuation_repricing_score": 52}, "symbol": "053800"}
{"after_stage_estimate": "Stage2-Actionable", "after_total_score": 82, "before_stage_estimate": "Stage2", "before_total_score": 74, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-02", "row_type": "score_simulation", "rule_effect": "requires verified retention/renewal/revenue/margin bridge before Yellow/Green; otherwise C28 security-label strength is capped at Stage2-blocked or local 4B watch", "scores_after": {"accounting_trust_risk_score": 6, "backlog_visibility_score": 66, "contract_score": 76, "customer_quality_score": 82, "dilution_cb_risk_score": 5, "execution_risk_score": 16, "legal_or_contract_risk_score": 6, "margin_bridge_score": 62, "policy_or_regulatory_score": 64, "relative_strength_score": 62, "revision_score": 54, "valuation_repricing_score": 58}, "scores_before": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 55, "contract_score": 64, "customer_quality_score": 74, "dilution_cb_risk_score": 5, "execution_risk_score": 20, "legal_or_contract_risk_score": 8, "margin_bridge_score": 52, "policy_or_regulatory_score": 60, "relative_strength_score": 58, "revision_score": 46, "valuation_repricing_score": 55}, "symbol": "263860"}
{"after_stage_estimate": "Stage4B-Watch", "after_total_score": 66, "before_stage_estimate": "Stage3-Yellow", "before_total_score": 77, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-03", "row_type": "score_simulation", "rule_effect": "requires verified retention/renewal/revenue/margin bridge before Yellow/Green; otherwise C28 security-label strength is capped at Stage2-blocked or local 4B watch", "scores_after": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 38, "contract_score": 50, "customer_quality_score": 62, "dilution_cb_risk_score": 6, "execution_risk_score": 38, "legal_or_contract_risk_score": 10, "margin_bridge_score": 34, "policy_or_regulatory_score": 50, "relative_strength_score": 52, "revision_score": 32, "valuation_repricing_score": 46}, "scores_before": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 46, "contract_score": 58, "customer_quality_score": 68, "dilution_cb_risk_score": 6, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "margin_bridge_score": 40, "policy_or_regulatory_score": 52, "relative_strength_score": 64, "revision_score": 38, "valuation_repricing_score": 60}, "symbol": "150900"}
{"after_stage_estimate": "Stage4B-Watch", "after_total_score": 65, "before_stage_estimate": "Stage3-Yellow", "before_total_score": 76, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-04", "row_type": "score_simulation", "rule_effect": "requires verified retention/renewal/revenue/margin bridge before Yellow/Green; otherwise C28 security-label strength is capped at Stage2-blocked or local 4B watch", "scores_after": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 42, "contract_score": 54, "customer_quality_score": 68, "dilution_cb_risk_score": 7, "execution_risk_score": 42, "legal_or_contract_risk_score": 8, "margin_bridge_score": 32, "policy_or_regulatory_score": 48, "relative_strength_score": 58, "revision_score": 30, "valuation_repricing_score": 48}, "scores_before": {"accounting_trust_risk_score": 8, "backlog_visibility_score": 50, "contract_score": 60, "customer_quality_score": 72, "dilution_cb_risk_score": 7, "execution_risk_score": 34, "legal_or_contract_risk_score": 8, "margin_bridge_score": 39, "policy_or_regulatory_score": 50, "relative_strength_score": 66, "revision_score": 36, "valuation_repricing_score": 64}, "symbol": "434480"}
{"after_stage_estimate": "Stage4B-Watch", "after_total_score": 63, "before_stage_estimate": "Stage3-Yellow", "before_total_score": 78, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-05", "row_type": "score_simulation", "rule_effect": "requires verified retention/renewal/revenue/margin bridge before Yellow/Green; otherwise C28 security-label strength is capped at Stage2-blocked or local 4B watch", "scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 36, "contract_score": 48, "customer_quality_score": 54, "dilution_cb_risk_score": 14, "execution_risk_score": 54, "legal_or_contract_risk_score": 8, "margin_bridge_score": 28, "policy_or_regulatory_score": 58, "relative_strength_score": 52, "revision_score": 28, "valuation_repricing_score": 44}, "scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 44, "contract_score": 56, "customer_quality_score": 60, "dilution_cb_risk_score": 12, "execution_risk_score": 42, "legal_or_contract_risk_score": 8, "margin_bridge_score": 34, "policy_or_regulatory_score": 66, "relative_strength_score": 72, "revision_score": 32, "valuation_repricing_score": 68}, "symbol": "411080"}
{"after_stage_estimate": "Stage4B-Watch", "after_total_score": 65, "before_stage_estimate": "Stage3-Yellow", "before_total_score": 78, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-06", "row_type": "score_simulation", "rule_effect": "requires verified retention/renewal/revenue/margin bridge before Yellow/Green; otherwise C28 security-label strength is capped at Stage2-blocked or local 4B watch", "scores_after": {"accounting_trust_risk_score": 12, "backlog_visibility_score": 38, "contract_score": 54, "customer_quality_score": 62, "dilution_cb_risk_score": 8, "execution_risk_score": 48, "legal_or_contract_risk_score": 8, "margin_bridge_score": 34, "policy_or_regulatory_score": 56, "relative_strength_score": 58, "revision_score": 30, "valuation_repricing_score": 50}, "scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 46, "contract_score": 62, "customer_quality_score": 66, "dilution_cb_risk_score": 8, "execution_risk_score": 38, "legal_or_contract_risk_score": 8, "margin_bridge_score": 42, "policy_or_regulatory_score": 62, "relative_strength_score": 70, "revision_score": 35, "valuation_repricing_score": 66}, "symbol": "430690"}
{"after_stage_estimate": "Stage2-blocked", "after_total_score": 61, "before_stage_estimate": "Stage2-Actionable", "before_total_score": 73, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-07", "row_type": "score_simulation", "rule_effect": "requires verified retention/renewal/revenue/margin bridge before Yellow/Green; otherwise C28 security-label strength is capped at Stage2-blocked or local 4B watch", "scores_after": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 34, "contract_score": 48, "customer_quality_score": 62, "dilution_cb_risk_score": 8, "execution_risk_score": 42, "legal_or_contract_risk_score": 8, "margin_bridge_score": 28, "policy_or_regulatory_score": 42, "relative_strength_score": 38, "revision_score": 28, "valuation_repricing_score": 40}, "scores_before": {"accounting_trust_risk_score": 10, "backlog_visibility_score": 42, "contract_score": 56, "customer_quality_score": 70, "dilution_cb_risk_score": 8, "execution_risk_score": 34, "legal_or_contract_risk_score": 8, "margin_bridge_score": 36, "policy_or_regulatory_score": 46, "relative_strength_score": 48, "revision_score": 34, "valuation_repricing_score": 48}, "symbol": "208350"}
{"calibration_usable_trigger_count": 7, "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_count": 7, "counterexample_count": 5, "current_profile_error_count": 7, "evidence_url_pending_count": 1, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "new_symbol_count_estimate": 5, "positive_case_count": 2, "proposed_axis": "C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_plus_security_label_spike_to_local_4B_watch_v2", "representative_trigger_count": 7, "reused_symbol_new_trigger_family_count": 2, "row_type": "aggregate", "selected_loop": 101, "selected_round": "R8", "source_proxy_only_count": 2, "stage4b_case_count": 4, "stage4c_case_count": 0}
{"axis": "stage2_required_bridge + local_4b_watch_guard", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "do_not_apply_now": true, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "reason": "This is a research artifact only; production scoring is not changed in this run.", "row_type": "shadow_weight_candidate", "weight_delta_proposal": {"contract_score": "+2 shadow", "information_confidence_gate": "+1 verified URL/contract requirement", "margin_bridge_score": "+2 shadow", "revision_score": "+1 shadow", "valuation_repricing_score": "-2 for price-only label spike"}}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "contribution_label": "canonical_archetype_rule_candidate", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": [], "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "new_axis_proposed": "C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_plus_security_label_spike_to_local_4B_watch_v2", "promotion_blocked_until_url_repair": "true_for_proxy_rows_only", "row_type": "residual_contribution"}
{"canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "case_id": "C28-R8-L101-N1", "evidence_url": "https://www.venturesquare.net/936046/", "name": "라온시큐어", "note": "digital-ID/FIDO evidence is relevant to C28, but the 2024-08 entry path overlaps the 2025-05-07 raw corporate-action candidate; keep for narrative repair only.", "profile_corporate_action_candidate_dates": ["2023-12-18", "2025-05-07"], "reason": "excluded_from_calibration_due_to_corporate_action_candidate_overlap_in_180D_window", "row_type": "narrative_only", "symbol": "042510", "trigger_date": "2024-08-13", "trigger_type": "Stage2-Actionable"}
```

## 14. Aggregate result

```json
{
  "calibration_usable_trigger_count": 7,
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "case_count": 7,
  "counterexample_count": 5,
  "current_profile_error_count": 7,
  "evidence_url_pending_count": 1,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "new_symbol_count_estimate": 5,
  "positive_case_count": 2,
  "proposed_axis": "C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_plus_security_label_spike_to_local_4B_watch_v2",
  "representative_trigger_count": 7,
  "reused_symbol_new_trigger_family_count": 2,
  "row_type": "aggregate",
  "selected_loop": 101,
  "selected_round": "R8",
  "source_proxy_only_count": 2,
  "stage4b_case_count": 4,
  "stage4c_case_count": 0
}
```

## 15. Score simulation summary

| case | before | after | interpretation |
|---|---|---|---|
| C28-R8-L101-01 | Stage2 / 73 | Stage2-Actionable / 80 | too_conservative_if_recurring_security_revenue_base_is_ignored |
| C28-R8-L101-02 | Stage2 / 74 | Stage2-Actionable / 82 | too_conservative_if_NAC_EDR_revenue_bridge_is_not_recognized |
| C28-R8-L101-03 | Stage3-Yellow / 77 | Stage4B-Watch / 66 | false_positive_if_data_security_label_is_promoted_without_renewal_or_revision_bridge |
| C28-R8-L101-04 | Stage3-Yellow / 76 | Stage4B-Watch / 65 | false_positive_if_customer_count_and_overseas_label_promote_without_margin_bridge |
| C28-R8-L101-05 | Stage3-Yellow / 78 | Stage4B-Watch / 63 | false_positive_if_AI_security_project_headline_is_treated_as_retention_bridge |
| C28-R8-L101-06 | Stage3-Yellow / 78 | Stage4B-Watch / 65 | false_positive_if_network_separation_security_growth_is_promoted_without_stable_retention_bridge |
| C28-R8-L101-07 | Stage2-Actionable / 73 | Stage2-blocked / 61 | false_positive_if_customer_story_is_treated_as_contract_retention_without_revenue_bridge |


## 16. Residual contribution summary

```text
new_independent_case_count: 7
reused_case_count: 2
reused_case_ids: C28-R8-L101-01|C28-R8-L101-02
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_required_bridge|local_4b_watch_guard|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
residual_error_types_found: missed_structural_security_revenue_bridge|false_positive_security_label_without_retention_bridge|local_4B_watch_needed
new_axis_proposed: C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_plus_security_label_spike_to_local_4B_watch_v2
existing_axis_strengthened: stage2_required_bridge|local_4b_watch_guard|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min|stage3_green_revision_min|hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

```json
{
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "contribution_label": "canonical_archetype_rule_candidate",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_weakened": [],
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "new_axis_proposed": "C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_plus_security_label_spike_to_local_4B_watch_v2",
  "promotion_blocked_until_url_repair": "true_for_proxy_rows_only",
  "row_type": "residual_contribution"
}
```

## 17. Rejected / narrative-only rows

```json
{
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "case_id": "C28-R8-L101-N1",
  "evidence_url": "https://www.venturesquare.net/936046/",
  "name": "라온시큐어",
  "note": "digital-ID/FIDO evidence is relevant to C28, but the 2024-08 entry path overlaps the 2025-05-07 raw corporate-action candidate; keep for narrative repair only.",
  "profile_corporate_action_candidate_dates": [
    "2023-12-18",
    "2025-05-07"
  ],
  "reason": "excluded_from_calibration_due_to_corporate_action_candidate_overlap_in_180D_window",
  "row_type": "narrative_only",
  "symbol": "042510",
  "trigger_date": "2024-08-13",
  "trigger_type": "Stage2-Actionable"
}
```


## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 18. What this loop does not claim

- It does not claim that all security-software companies are counterexamples.
- It does not lower Stage3-Green thresholds.
- It does not apply a production profile change.
- It does not create a live watchlist.
- It does not infer future returns.

## 19. Why this is not schema rematerialization

The loop adds a new C28 sub-axis around retention/renewal/revenue/margin bridge versus security-label spike. It also provides a mixed set of positive and counterexample cases, rather than repeating the prior loop-100 remote-support / AI-office / data-API route.

## 20. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not use this MD alone to patch production scoring. Batch it with the surrounding V12 residual corpus.

Read this artifact as a C28 canonical-archetype candidate:
- candidate axis: C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_v2
- strengthen: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
- do not lower Stage3-Green global threshold
- do not treat security/SaaS/zero-trust/AI-security wording as ARR unless renewal/revenue/margin bridge is verified
- rows with source_proxy_only=true require URL repair before positive promotion

Implementation shape, if later accepted:
if canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
    require one of [verified renewal, retained enterprise customer expansion, recurring maintenance/ARR proxy, revenue bridge, margin bridge] before Stage2-Actionable or Stage3-Yellow
    cap price-only security-label spike at Stage2-blocked or local_4B_watch
    require revision_score >= 55 and non-price bridge before Stage3-Green
```

## 21. Validation scope

```text
usable_trigger_rows = 7
representative_trigger_rows = 7
calibration_usable = true for all representative triggers
narrative_only_or_rejected_rows = 1
corporate_action_contaminated_trigger_rows = 0
price_fields_complete = true
```

## 22. Source notes

The file uses stock-web OHLC for all path calculations. Non-price evidence URLs are carried in each machine-readable row. Some evidence is intentionally marked source-proxy because the goal of this loop is residual discovery, not final promotion.

## 23. Final next-round state

```text
completed_round = R8
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = C28_SECURITY_SAAS_ZERO_TRUST_AUTHENTICATION_RENEWAL_MARGIN_BRIDGE
deep_sub_archetype_id = C28_DEEP_ENDPOINT_NAC_CERTIFICATE_SASE_THREAT_INTEL_RETENTION_VS_SECURITY_LABEL_SPIKE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

## 24. Compact execution summary

```text
trigger_row_count = 7
calibration_usable_trigger_count = 7
representative_trigger_count = 7
new_independent_case_count = 7
new_symbol_count = 5
reused_symbol_new_trigger_family_count = 2
positive_case_count = 2
counterexample_count = 5
stage4b_case_count = 4
stage4c_case_count = 0
current_profile_error_count = 7
source_proxy_only_count = 2
evidence_url_pending_count = 1
```

## 25. Files read / price shards used

```text
atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv
atlas/ohlcv_tradable_by_symbol_year/053/053800/2025.csv
atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv
atlas/ohlcv_tradable_by_symbol_year/263/263860/2025.csv
atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv
atlas/ohlcv_tradable_by_symbol_year/150/150900/2025.csv
atlas/ohlcv_tradable_by_symbol_year/434/434480/2024.csv
atlas/ohlcv_tradable_by_symbol_year/434/434480/2025.csv
atlas/ohlcv_tradable_by_symbol_year/411/411080/2024.csv
atlas/ohlcv_tradable_by_symbol_year/411/411080/2025.csv
atlas/ohlcv_tradable_by_symbol_year/430/430690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/430/430690/2025.csv
atlas/ohlcv_tradable_by_symbol_year/208/208350/2024.csv
atlas/ohlcv_tradable_by_symbol_year/208/208350/2025.csv
```

## 26. Ingest expectations

All representative trigger rows include complete 30/90/180D MFE/MAE fields. The narrative-only row is intentionally excluded from calibration promotion. The filename, metadata round, and metadata loop are consistent.

## 27. One-line residual thesis

C28 can reward true retained security-software revenue, but it must punish security-label rerating that lacks renewal, revenue, margin, or revision bridge.

## 28. End marker

```text
v12_stock_web_residual_research_md_complete = true
```
