# E2R v12 Stock-Web Sector/Archetype Residual Research

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 100
round_schedule_status: coverage_index_selected
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: ERP_CLOUD_SECURITY_CONTRACT_RETENTION_ARR_RENEWAL_BRIDGE_VS_SECURITY_THEME_BETA_SPIKE
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
```

## 1. Research objective

C28는 `software/security contract retention` 축이다. 이번 loop의 목적은 단순 보안/AI/공공계약 headline이 아니라, 매출의 반복성·계약 잔존성·renewal·ARR/RPO 성격이 있는 케이스와, 보안 테마성 스파이크 뒤에 계약/retention 증거가 약해서 stage2가 과열되는 케이스를 분리하는 것이다.

이 MD는 현재 종목 추천이 아니며, live watchlist도 아니다. 모든 price-path 검증은 `Songdaiki/stock-web`의 1D OHLCV shard를 사용한 historical trigger-level calibration이다.

## 2. No-repeat / coverage choice

```text
No-Repeat Index priority bucket: Priority 0
selected canonical: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
current rows in index: 27
need to 30: 3
investigation point: security contract, retention, ARR/renewal, theme beta counterexample
```

이번 loop는 C28의 최소 안정권 30-row까지 남은 3개 gap을 채우기 위한 coverage-first 실행이다. `C28 + symbol + trigger_type + entry_date` hard duplicate를 피하기 위해 기존 registry 검색에서 `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION 012510 053800 203650` 조합이 확인되지 않은 상태로 진행했다. 단, repository text-search 기반이므로 최종 ingest dedupe가 source of truth다.

## 3. Price source validation

```json
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","min_date":"1995-05-02","max_date":"2026-02-20","tradable_row_count":14354401,"symbol_count":5414,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","corporate_action_policy":"block contaminated windows by default"}
```

Case symbol availability:

```json
{"row_type":"price_source_validation","symbol":"012510","name":"더존비즈온","market":"KOSPI","profile_path":"atlas/symbol_profiles/012/012510.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_status":"active_like"}
{"row_type":"price_source_validation","symbol":"053800","name":"안랩","market":"KOSDAQ","profile_path":"atlas/symbol_profiles/053/053800.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv","profile_status":"active_like"}
{"row_type":"price_source_validation","symbol":"203650","name":"드림시큐리티","market":"KOSDAQ","profile_path":"atlas/symbol_profiles/203/203650.json","year_file":"atlas/ohlcv_tradable_by_symbol_year/203/203650/2024.csv","profile_status":"active_like"}
```

## 4. Case set summary

| case_id | symbol | name | role | trigger family | entry date | entry close | peak high | trough low | MFE | MAE | classification |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| C28-100-01 | 012510 | 더존비즈온 | positive | ERP/cloud/AI software contract-retention bridge | 2024-04-04 | 53,300 | 72,000 | 48,200 | +35.08% | -9.57% | positive_contract_retention_bridge |
| C28-100-02 | 053800 | 안랩 | counterexample | security theme spike without retention/ARR bridge | 2024-04-11 | 64,800 | 75,600 | 56,000 | +16.67% | -13.58% | counterexample_theme_beta_event_cap |
| C28-100-03 | 203650 | 드림시큐리티 | counterexample | authentication/security vocabulary spike without renewal bridge | 2024-02-15 | 4,020 | 4,075 | 3,150 | +1.37% | -21.64% | counterexample_low_mfe_high_mae |

### Metric definitions

```text
entry_price = entry_date close
mfe_pct = (max_high_after_entry_window - entry_price) / entry_price * 100
mae_pct = (min_low_after_entry_window - entry_price) / entry_price * 100
drawdown_from_peak_pct = (trough_low_after_peak - peak_high) / peak_high * 100
window = calibration-safe forward 1D OHLCV slice visible in stock-web shard; when exact 90-calendar boundary is unavailable in visible chunk, the conservative observed window is stated.
```

## 5. Case narratives

### C28-100-01 — 012510 더존비즈온 positive bridge

더존비즈온은 C28에서 소프트웨어 반복수요, ERP/cloud migration, enterprise workflow lock-in을 볼 수 있는 cleaner positive control이다. 2024-04-04 close 53,300을 entry로 잡으면, 같은 날 price expansion 후에도 다음 구간에서 무너지지 않고 2024-04-30 high 63,300, 2024-05-22 high 65,300, 2024-06-12 high 72,000까지 이어진다.

이 케이스는 단순 하루짜리 AI/SW theme pop과 다르다. 가격경로가 말하는 것은 "스파이크 후 바로 죽는 테마"가 아니라 "software recurring demand/enterprise contract stickiness를 시장이 다시 할인하기 시작한 뒤 추세가 이어진 상태"다. Stage2-Actionable을 허용하려면 renewal/retention/ARR/RPO 또는 ERP/cloud 계약 잔존성을 narrative-only가 아니라 evidence bridge로 요구하는 방향이 맞다.

```json
{"row_type":"case","case_id":"C28-100-01","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_CLOUD_AI_CONTRACT_RETENTION_BRIDGE","symbol":"012510","name":"더존비즈온","trigger_type":"Stage2-Actionable","trigger_family":"erp_cloud_ai_contract_retention_bridge","evidence_family":"enterprise_software_recurring_revenue_proxy","entry_date":"2024-04-04","entry_price":53300.0,"peak_date":"2024-06-12","peak_high":72000.0,"trough_date":"2024-04-09","trough_low":48200.0,"mfe_pct":35.08,"mae_pct":-9.57,"classification":"positive_contract_retention_bridge","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
```

### C28-100-02 — 053800 안랩 counterexample

안랩은 보안이라는 단어만으로는 C28 positive를 열면 안 된다는 반례다. 2024-04-11 close 64,800 이후 2024-04-12 high 75,600까지 단기 MFE가 나오지만, 그 뒤에는 4~6월 동안 60,000선까지 흘러내리고 2024-07-08 low 56,000까지 밀린다.

C28의 문제는 "보안 테마"라는 표지판이 너무 크다는 점이다. 표지판은 계약서가 아니다. 실제 renewal/ARR/retention, public contract backlog, 보안관제 반복매출이 확인되지 않으면 Stage2-Actionable bonus를 주면 theme beta가 score를 과하게 끌어올린다. 이 케이스는 C28에서 price-only/security-headline spike를 local 4B watch로 보내는 근거다.

```json
{"row_type":"case","case_id":"C28-100-02","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_THEME_SPIKE_WITHOUT_RETENTION_BRIDGE","symbol":"053800","name":"안랩","trigger_type":"Stage2-FalsePositive","trigger_family":"security_theme_beta_spike_without_arr_retention","evidence_family":"security_keyword_proxy_only","entry_date":"2024-04-11","entry_price":64800.0,"peak_date":"2024-04-12","peak_high":75600.0,"trough_date":"2024-07-08","trough_low":56000.0,"mfe_pct":16.67,"mae_pct":-13.58,"classification":"counterexample_theme_beta_event_cap","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
```

### C28-100-03 — 203650 드림시큐리티 counterexample

드림시큐리티는 인증/보안 vocabulary가 반복계약으로 이어졌는지 확인하지 않으면 Stage2가 헛도는 케이스다. 2024-02-15 close 4,020을 entry로 보면 이후 2024-03-13 high 4,075가 사실상 peak이고, 2024-04-16 low 3,150까지 빠진다. MFE는 +1.37%에 불과하지만 MAE는 -21.64%로 커진다.

이건 "좋은 기술 키워드"와 "좋은 진입조건"이 다른 물건이라는 샘플이다. 보안/인증 분야는 공공·금융·기업계약의 renewal quality가 가격추세의 척추다. 척추 없이 테마만 서 있으면 가격은 오래 서 있지 못한다.

```json
{"row_type":"case","case_id":"C28-100-03","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AUTH_SECURITY_VOCABULARY_WITHOUT_RENEWAL_BRIDGE","symbol":"203650","name":"드림시큐리티","trigger_type":"Stage2-FalsePositive","trigger_family":"auth_security_keyword_spike_without_renewal_contract","evidence_family":"security_authentication_proxy_only","entry_date":"2024-02-15","entry_price":4020.0,"peak_date":"2024-03-13","peak_high":4075.0,"trough_date":"2024-04-16","trough_low":3150.0,"mfe_pct":1.37,"mae_pct":-21.64,"classification":"counterexample_low_mfe_high_mae","calibration_usable":true,"source_proxy_only":true,"evidence_url_pending":true}
```

## 6. Trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C28-100-01","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_CLOUD_AI_CONTRACT_RETENTION_BRIDGE","symbol":"012510","name":"더존비즈온","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":53300.0,"entry_basis":"close","mfe_pct":35.08,"mae_pct":-9.57,"peak_date":"2024-06-12","peak_high":72000.0,"trough_date":"2024-04-09","trough_low":48200.0,"classification":"positive_contract_retention_bridge","calibration_usable":true,"dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|012510|Stage2-Actionable|2024-04-04|2024-04-04","novelty_check":"repository_search_no_hit_for_C28_symbol_bundle; final_ingest_dedupe_required"}
{"row_type":"trigger","case_id":"C28-100-02","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_THEME_SPIKE_WITHOUT_RETENTION_BRIDGE","symbol":"053800","name":"안랩","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":64800.0,"entry_basis":"close","mfe_pct":16.67,"mae_pct":-13.58,"peak_date":"2024-04-12","peak_high":75600.0,"trough_date":"2024-07-08","trough_low":56000.0,"classification":"counterexample_theme_beta_event_cap","calibration_usable":true,"dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053800|Stage2-FalsePositive|2024-04-11|2024-04-11","novelty_check":"repository_search_no_hit_for_C28_symbol_bundle; final_ingest_dedupe_required"}
{"row_type":"trigger","case_id":"C28-100-03","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AUTH_SECURITY_VOCABULARY_WITHOUT_RENEWAL_BRIDGE","symbol":"203650","name":"드림시큐리티","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":4020.0,"entry_basis":"close","mfe_pct":1.37,"mae_pct":-21.64,"peak_date":"2024-03-13","peak_high":4075.0,"trough_date":"2024-04-16","trough_low":3150.0,"classification":"counterexample_low_mfe_high_mae","calibration_usable":true,"dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|203650|Stage2-FalsePositive|2024-02-15|2024-02-15","novelty_check":"repository_search_no_hit_for_C28_symbol_bundle; final_ingest_dedupe_required"}
```

## 7. Score simulation

Current calibrated profile proxy:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Raw component score sketch:

| case_id | revenue quality | margin/FCF bridge | information confidence | contract/retention bridge | price action | current proxy result | residual issue |
|---|---:|---:|---:|---:|---:|---|---|
| C28-100-01 | 15 | 12 | 11 | 17 | 14 | Stage2-Actionable / Yellow watch | positive only when retention bridge exists |
| C28-100-02 | 7 | 5 | 7 | 4 | 12 | may over-score as Stage2 if security keyword is accepted | needs retention/renewal proof |
| C28-100-03 | 5 | 4 | 6 | 3 | 6 | false Stage2 if authentication theme is treated as contract quality | high-MAE guard required |

```jsonl
{"row_type":"score_simulation","case_id":"C28-100-01","profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"revenue_quality":15,"margin_fcf_bridge":12,"information_confidence":11,"contract_retention_bridge":17,"price_action":14},"simulated_total":69,"simulated_stage":"Stage2-Actionable","score_return_alignment":"good_positive_if_contract_retention_bridge_confirmed"}
{"row_type":"score_simulation","case_id":"C28-100-02","profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"revenue_quality":7,"margin_fcf_bridge":5,"information_confidence":7,"contract_retention_bridge":4,"price_action":12},"simulated_total":35,"simulated_stage":"Stage2-WatchOnly_or_4B-local","score_return_alignment":"bad_if_security_keyword_gets_stage2_bonus"}
{"row_type":"score_simulation","case_id":"C28-100-03","profile_proxy":"e2r_2_1_stock_web_calibrated","raw_component_score":{"revenue_quality":5,"margin_fcf_bridge":4,"information_confidence":6,"contract_retention_bridge":3,"price_action":6},"simulated_total":24,"simulated_stage":"Stage2-Reject","score_return_alignment":"bad_low_mfe_high_mae"}
```

## 8. Aggregate metric

```json
{"row_type":"aggregate_metric","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_CLOUD_SECURITY_CONTRACT_RETENTION_ARR_RENEWAL_BRIDGE_VS_SECURITY_THEME_BETA_SPIKE","case_count":3,"trigger_count":3,"positive_case_count":1,"counterexample_count":2,"avg_mfe_pct":17.71,"avg_mae_pct":-14.93,"median_mfe_pct":16.67,"median_mae_pct":-13.58,"current_profile_error_count":2,"residual_error_type":"security_or_software_keyword_without_retention_contract_bridge_can_over_score_stage2","calibration_usable":true}
```

## 9. Shadow rule candidate

```json
{"row_type":"shadow_weight","axis":"c28_retention_arr_renewal_bridge_required_for_stage2_actionable_shadow_only","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","direction":"tighten_stage2_actionable","suggested_rule":"For C28, Stage2-Actionable requires at least one non-price contract-retention bridge: ARR/RPO/renewal, recurring SaaS revenue, public/enterprise contract backlog with renewal evidence, or security managed-service repeat revenue. Security/software keywords alone remain Stage2-WatchOnly or local 4B if price extension is high.","positive_support_case_ids":["C28-100-01"],"counterexample_support_case_ids":["C28-100-02","C28-100-03"],"do_not_apply_live_now":true}
```

Proposed C28 compression:

```text
Good C28:
software/security evidence → repeat contract / renewal / ARR / retention → margin or FCF durability → price strength survives first pullback

Bad C28:
security/software keyword → price spike → no renewal/ARR/RPO/retention bridge → low MFE or high MAE → watch-only / local 4B
```

## 10. Residual contribution

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"diversity_score_summary":"C28 Priority 0 부족권 + ERP/cloud retention positive와 security/auth theme counterexamples 균형","new_axis_proposed":"c28_retention_arr_renewal_bridge_required_for_stage2_actionable_shadow_only","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C28 security/software keyword spikes","existing_axis_weakened":null}
{"row_type":"residual_contribution","loop_contribution_label":"canonical_archetype_rule_candidate","sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"do_not_propose_new_weight_delta":false,"next_recommended_archetypes":["C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG"]}
```

## 11. Validation scope and caveats

```text
validated_scope:
- 1D OHLCV rows from Songdaiki/stock-web tradable shards
- entry_date / entry_close / forward high / forward low manually checked in visible shard windows
- source_proxy_only = true for business-evidence narratives
- evidence_url_pending = true

not_validated_scope:
- no live scan
- no current recommendation
- no stock_agent src/e2r code access
- no production patch
- no broker/API action
```

Important caveat: this MD treats business evidence as source-proxy narrative because the execution mode prioritizes historical OHLC calibration and duplicate/coverage expansion. Coding-agent ingestion should keep these cases as shadow-rule support unless later evidence URLs confirm the contract/retention facts.

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for stock_agent E2R calibration ingestion.

Input MD:
docs/round/e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

Task:
1. Ingest the v12 JSONL rows only after schema validation.
2. Do not treat source_proxy_only rows as production-ready evidence URL rows.
3. Dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Add or evaluate a shadow-only C28 rule candidate:
   c28_retention_arr_renewal_bridge_required_for_stage2_actionable_shadow_only
5. Do not loosen Stage3-Green thresholds.
6. Do not make price-only software/security theme spikes positive Stage2-Actionable.
7. Keep full_4b_requires_non_price_evidence active for C28 software/security keyword spikes.
8. Emit applied/held decision with reason.
9. Do not run live scan or broker action.
```

## 13. Final summary

```text
selected_round: R8
selected_loop: 100
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: ERP_CLOUD_SECURITY_CONTRACT_RETENTION_ARR_RENEWAL_BRIDGE_VS_SECURITY_THEME_BETA_SPIKE
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
new_axis_proposed: c28_retention_arr_renewal_bridge_required_for_stage2_actionable_shadow_only
next_recommended_archetypes: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```
