# E2R v12 Residual Research — R8 loop 98 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 98
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SECURITY_SOFTWARE_ENTERPRISE_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_THEME_AND_DEFENSIVE_SERVICE_EVENT_CAP
loop_contribution_label: canonical_archetype_rule_candidate
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source_repo: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
non_price_evidence_status: source_proxy_only__evidence_url_pending
validation_scope: C28 residual coverage gap fill; no production promotion until exact source URLs are backfilled
```

## 1. Research objective

This residual pass tests whether the C28 bucket should reward **recurring software/security contract retention** only when it is tied to renewal, ARR-like maintenance, enterprise contract backlog, or sticky managed-service evidence. The failure mode is familiar: security, AI software, or cyber-policy words can create a tradable MFE, but without renewal/retention/margin continuity the move behaves like an event-cap or local 4B watch rather than Stage3-Green.

The working rule is simple: a software or security name becomes E2R-positive only when the bridge is **contract → recurring revenue / renewal → margin or revision**. A security theme, political event, one-off system order, or hardware-like security service label is insufficient.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_source_repo":"Songdaiki/stock-web","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","max_date":"2026-02-20","schema_checked":true,"mfe_mae_formula":"MFE_N_pct=(max high from entry through N tradable rows / entry_price - 1)*100; MAE_N_pct=(min low from entry through N tradable rows / entry_price - 1)*100","data_quality_label":"usable_with_caveat","note":"All selected trigger windows are outside symbol-profile corporate-action candidate dates. Non-price evidence remains source_proxy_only and must be URL-backfilled before promotion."}
```

## 3. Novelty and duplicate check

The selected canonical is C28. Existing registry coverage already includes C28 through R8 loop 97, so this file uses loop 98 for the same R8/C28 pair. It avoids reusing the current session's C27 IP/contents sample and focuses on a different failure family: **security/SaaS/enterprise software retention bridge versus theme spike**.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No intentional duplicate row is used. The selected symbols and trigger families are:

```text
053800 AhnLab — security theme spike without explicit retention bridge
058970 EMRO — enterprise procurement SaaS / AI optionality with high-MAE path
307950 Hyundai AutoEver — enterprise/vehicle software contract bridge, positive but timing-sensitive
136540 Wins — network security recurring-maintenance candidate with weak liquidity/weak MFE
012750 S1 — defensive security-service recurring contract, not pure software; used as boundary case
```

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | trigger_type | C28 interpretation | evidence quality | 180D label |
|---|---:|---|---|---|---:|---|---|---|---|
| C28-R8-L98-001 | 307950 | 현대오토에버 | 2024-04-24 | 2024-04-24 | 154200 | enterprise_software_contract_bridge | positive C28 bridge: enterprise/vehicle software revenue can rerate if renewal/backlog/revision is visible | source_proxy_only | constructive but timing-sensitive |
| C28-R8-L98-002 | 058970 | 엠로 | 2024-03-21 | 2024-03-21 | 63600 | procurement_saas_ai_optionality | MFE exists, but SaaS/AI label needs renewal/revenue proof; high-MAE guard required | source_proxy_only | high_MAE_yellow |
| C28-R8-L98-003 | 053800 | 안랩 | 2024-04-11 | 2024-04-11 | 64800 | security_theme_spike_no_retention_bridge | security/political/cyber theme created spike but no sticky contract bridge; event-cap/4B-watch | source_proxy_only | false_stage2_or_event_cap |
| C28-R8-L98-004 | 136540 | 윈스 | 2024-01-22 | 2024-01-22 | 13040 | network_security_maintenance_recurring | recurring-maintenance candidate but weak liquidity/weak MFE; not enough for Green | source_proxy_only | weak_positive_yellow |
| C28-R8-L98-005 | 012750 | 에스원 | 2024-04-23 | 2024-04-23 | 63200 | defensive_security_service_boundary | recurring security service is stable but not high-revision software; boundary case should not over-score C28 | source_proxy_only | defensive_yellow |
| C28-R8-L98-006 | 307950 | 현대오토에버 | 2024-07-03 | 2024-07-03 | 168300 | software_revision_followthrough | follow-through test after earlier bridge; MFE improves but MAE still matters | source_proxy_only | positive_followthrough |

## 5. JSONL trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_ENTERPRISE_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_THEME_AND_DEFENSIVE_SERVICE_EVENT_CAP","case_id":"C28-R8-L98-001","symbol":"307950","name":"현대오토에버","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":154200,"trigger_type":"enterprise_software_contract_bridge","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":12.6,"mae_30d_pct":-5.5,"mfe_90d_pct":18.0,"mae_90d_pct":-5.6,"mfe_180d_pct":18.0,"mae_180d_pct":-7.8,"peak_price_observed":181900,"trough_price_observed":142000,"score_alignment":"Stage2_to_Yellow_valid_when_contract_bridge_visible","residual_flag":"timing_sensitive_positive","evidence_url_status":"pending","source_proxy_only":true,"do_not_promote_yet":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_ENTERPRISE_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_THEME_AND_DEFENSIVE_SERVICE_EVENT_CAP","case_id":"C28-R8-L98-002","symbol":"058970","name":"엠로","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":63600,"trigger_type":"procurement_saas_ai_optionality","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.1,"mae_30d_pct":-5.7,"mfe_90d_pct":20.0,"mae_90d_pct":-12.0,"mfe_180d_pct":20.0,"mae_180d_pct":-15.6,"peak_price_observed":76300,"trough_price_observed":53700,"score_alignment":"MFE_without_clean_retention_bridge_should_not_be_Green","residual_flag":"high_MAE_yellow_guardrail","evidence_url_status":"pending","source_proxy_only":true,"do_not_promote_yet":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_ENTERPRISE_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_THEME_AND_DEFENSIVE_SERVICE_EVENT_CAP","case_id":"C28-R8-L98-003","symbol":"053800","name":"안랩","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":64800,"trigger_type":"security_theme_spike_no_retention_bridge","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":16.7,"mae_30d_pct":-4.3,"mfe_90d_pct":16.7,"mae_90d_pct":-13.6,"mfe_180d_pct":16.7,"mae_180d_pct":-13.6,"peak_price_observed":75600,"trough_price_observed":56000,"score_alignment":"Theme_MFE_must_be_event_capped_without_renewal_or_retention_bridge","residual_flag":"false_stage2_event_cap","evidence_url_status":"pending","source_proxy_only":true,"do_not_promote_yet":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_ENTERPRISE_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_THEME_AND_DEFENSIVE_SERVICE_EVENT_CAP","case_id":"C28-R8-L98-004","symbol":"136540","name":"윈스","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":13040,"trigger_type":"network_security_maintenance_recurring","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.1,"mae_30d_pct":-4.0,"mfe_90d_pct":3.1,"mae_90d_pct":-5.9,"mfe_180d_pct":3.1,"mae_180d_pct":-8.4,"peak_price_observed":13440,"trough_price_observed":11950,"score_alignment":"Recurrence_word_alone_is_not_enough_when_MFE_is_weak_and_liquidity_is_low","residual_flag":"weak_positive_yellow_only","evidence_url_status":"pending","source_proxy_only":true,"do_not_promote_yet":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_ENTERPRISE_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_THEME_AND_DEFENSIVE_SERVICE_EVENT_CAP","case_id":"C28-R8-L98-005","symbol":"012750","name":"에스원","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":63200,"trigger_type":"defensive_security_service_boundary","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.3,"mae_30d_pct":-6.2,"mfe_90d_pct":1.3,"mae_90d_pct":-10.8,"mfe_180d_pct":1.3,"mae_180d_pct":-10.8,"peak_price_observed":64000,"trough_price_observed":56400,"score_alignment":"Defensive_recurring_service_should_not_inherit_SaaS_Green_bonus_without_revision","residual_flag":"boundary_case_event_cap","evidence_url_status":"pending","source_proxy_only":true,"do_not_promote_yet":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_ENTERPRISE_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_THEME_AND_DEFENSIVE_SERVICE_EVENT_CAP","case_id":"C28-R8-L98-006","symbol":"307950","name":"현대오토에버","trigger_date":"2024-07-03","entry_date":"2024-07-03","entry_price":168300,"trigger_type":"software_revision_followthrough","price_source_repo":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":8.1,"mae_30d_pct":-4.3,"mfe_90d_pct":8.1,"mae_90d_pct":-4.3,"mfe_180d_pct":8.1,"mae_180d_pct":-8.7,"peak_price_observed":181900,"trough_price_observed":153500,"score_alignment":"Followthrough_validates_Yellow_to_Green_only_if_contract_retention_evidence_backfilled","residual_flag":"positive_followthrough_requires_url_backfill","evidence_url_status":"pending","source_proxy_only":true,"do_not_promote_yet":true}
```

## 6. Raw component score stress test

| case_id | industrial_logic | evidence_quality | revision_bridge | price_action | valuation_risk | stage_candidate_before_guard | stage_after_C28_guard |
|---|---:|---:|---:|---:|---:|---|---|
| C28-R8-L98-001 | 22 | 12 | 12 | 15 | -4 | Stage3-Yellow | Stage3-Yellow; Green only after exact contract/retention URL |
| C28-R8-L98-002 | 19 | 8 | 8 | 16 | -8 | Stage3-Yellow | Stage2/Yellow high-MAE guard |
| C28-R8-L98-003 | 14 | 5 | 3 | 17 | -9 | Stage2 | event-cap / local 4B watch |
| C28-R8-L98-004 | 15 | 9 | 4 | 4 | -3 | Stage2 | Yellow only; no Green promotion |
| C28-R8-L98-005 | 13 | 10 | 3 | 3 | -2 | Stage2 | defensive boundary; no SaaS bonus |
| C28-R8-L98-006 | 21 | 11 | 10 | 12 | -4 | Stage3-Yellow | Yellow→Green candidate only with exact source proof |

## 7. Aggregate metric

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","trigger_count":6,"positive_bridge_count":2,"counterexample_count":4,"avg_mfe_90d_pct":11.2,"avg_mae_90d_pct":-8.7,"median_mfe_90d_pct":10.1,"median_mae_90d_pct":-9.6,"high_mae_case_count":3,"event_cap_case_count":2,"source_proxy_only_ratio":1.0,"promotion_ready":false,"reason_not_promotion_ready":"exact non-price evidence URLs are pending; rows are useful for residual ledger and shadow rule design only"}
```

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"stage2_required_bridge","candidate":"For C28, require at least one of renewal/retention/ARR-like maintenance backlog/enterprise contract expansion/revision bridge before Stage2 becomes actionable.","evidence_basis":"AhnLab and Wins show that security labels can create either short MFE or weak movement without durable rerating.","production_scoring_changed":false,"do_not_promote_yet":true}
{"row_type":"shadow_weight","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"local_4b_watch_guard","candidate":"If C28 move is driven by AI/security/political/cyber headline but no renewal or recurring revenue bridge appears within the trigger window, cap at Yellow or local 4B watch even when MFE_30D is positive.","evidence_basis":"AhnLab and EMRO produce MFE but also high-MAE or evidence weakness.","production_scoring_changed":false,"do_not_promote_yet":true}
{"row_type":"shadow_weight","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"green_promotion_gate","candidate":"Green requires contract-retention evidence plus revision/margin bridge; price action alone should never carry C28 to Green.","evidence_basis":"Hyundai AutoEver works as constructive follow-through only when enterprise software contract evidence is backfilled; S1 boundary case should not inherit SaaS bonus.","production_scoring_changed":false,"do_not_promote_yet":true}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","contribution_type":"coverage_gap_fill","summary":"Adds six C28 rows across enterprise software, procurement SaaS, cyber-security, network security, and defensive security-service boundary cases."}
{"row_type":"residual_contribution","round":"R8","loop":"98","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","contribution_type":"rule_candidate","summary":"Proposes stricter C28 Stage2/Green bridge: renewal/retention/ARR-like maintenance or enterprise contract evidence must be present; AI/security label alone is event-capped."}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this during research. Use it only in a later batch implementation session.

```text
You are the later coding agent for Songdaiki/stock_agent. Ingest this standalone v12 residual MD as a research artifact only. Do not infer production rule changes from it unless the non-price evidence URLs are backfilled. Parse JSONL rows under row_type=trigger, aggregate_metric, shadow_weight, residual_contribution. Add these rows to the v12 calibration ledger if they pass schema validation. Treat all rows as source_proxy_only and promotion_ready=false. Candidate implementation after further corroboration: C28 requires a contract-retention/renewal/ARR-like maintenance/revision bridge before Stage2 can be actionable or Green can be considered; security/AI/cyber label spikes without bridge should be event-capped or local 4B watch.
```

## 11. Final verdict

C28 should not behave like a generic software/security theme bucket. It needs a sticky-revenue bridge. The pattern is:

```text
contract / renewal / recurring maintenance / enterprise expansion
  → revenue retention or backlog durability
  → margin or revision bridge
  → Stage2 actionable / Stage3-Yellow
  → Green only after exact source evidence and price-return alignment
```

Without that chain, C28 is mostly a theme label. Theme labels can create MFE, but they are not enough to carry Green.
