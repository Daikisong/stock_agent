# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
scheduled_round: R8
scheduled_loop: 73
completed_round: R8
completed_loop: 73
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM
output_file: e2r_stock_web_v12_residual_round_R8_loop_73_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`. Rollback reference: `e2r_2_0_baseline_reference`.

This MD does not re-prove the global Stage2 bonus. It tests a narrower R8 residual: software and security names often rerate when the market sees recurring contract retention, seat expansion, cloud migration, regulated demand, or renewal evidence. The trap is that the same chart shape can come from a political premium, AI theme, or security ticker label without contract evidence. In C28, the moat is not the logo on the ticker; it is the renewal loop.

| existing calibrated axis | status | C28 interpretation |
|---|---|---|
| stage2_actionable_evidence_bonus | existing_axis_tested | useful only if non-price retention/contract evidence exists |
| stage3_yellow_total_min | existing_axis_kept | Yellow threshold works after component quality is repaired |
| stage3_green_total_min / revision_min | existing_axis_kept | no weakening proposed |
| price_only_blowoff_blocks_positive_stage | existing_axis_strengthened | theme-only security/software spikes must remain watch-only |
| full_4b_requires_non_price_evidence | existing_axis_strengthened | price peaks are overlays, not exits, unless slowdown/valuation/retention decay appears |
| hard_4c_thesis_break_routes_to_4c | existing_axis_kept | no hard 4C promotion reversal proposed here |

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R8 |
| scheduled_loop | 73 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION |
| fine_archetype_id | SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM |
| round_sector_consistency | pass |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; residual_false_positive_mining; 4B_non_price_requirement_stress_test; coverage_gap_fill |

R8 allows platform/content/software/security. C28 is selected because local artifacts already cover R8 loop 71 C26 and R8 loop 72 C27, while C28 software/security contract-retention coverage is still thin.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts/source-code restrictions were honored: no `src/e2r` code was opened and no production patch was written. Local prior outputs show R8 loop 71 covered C26 and R8 loop 72 covered C27. This run therefore fills the R8/C28 coverage gap for loop 73.

| duplicate check | result |
|---|---|
| scheduled_round | R8 |
| scheduled_loop | 73 |
| same canonical as prior R8 loop 71/72 | no; C28 was not used there |
| reused case count | 0 |
| new symbol count | 4 |
| new independent case ratio | 1.00 |
| hard duplicate key conflicts | 0 |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Stock-Web manifest confirms raw/unadjusted OHLC, `tradable_raw` calibration basis, and manifest max date 2026-02-20. Schema confirms tradable shard columns `d,o,h,l,c,v,a,mc,s,m` and the MFE/MAE formulas.

## 5. Historical Eligibility Gate

| case_id | entry_date | 180D forward available | corporate_action_window_status | calibration_usable | reason |
|---|---:|---:|---|---:|---|
| R8L73_C28_012510_DUZON_AI_ERP_CLOUD_CONTRACT_RETENTION | 2024-01-18 | true | clean_180D_window | true | CA candidates only 2002/2006/2009 |
| R8L73_C28_263860_GENIANS_ZERO_TRUST_CONTRACT_RETENTION | 2023-05-17 | true | clean_180D_window | true | CA candidates only 2018 |
| R8L73_C28_053800_AHNLAB_POLITICAL_SECURITY_THEME | 2022-03-23 | true | clean_180D_window | true | CA candidate only 2005 |
| R8L73_C28_030520_HANCOM_AI_THEME_WITHOUT_RETENTION | 2024-01-10 | true | clean_180D_window | true | CA candidates end in 2006 |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rule |
|---|---|---|
| enterprise_erp_ai_cloud_retention | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | recurring enterprise software, cloud migration, and AI upsell can be Stage2-Actionable if customer/contract retention evidence exists |
| zero_trust_security_contract_retention | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | security product expansion can be promoted only when demand is contract/renewal/regulated-use driven |
| political_event_premium_not_contract_retention | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | security ticker + political premium is watch-only; do not grant software-retention score |
| ai_office_theme_without_contract_retention | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | AI software optionality without enterprise renewal/ARPU evidence is capped |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | trigger_type | entry_date | entry_price | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---|
| R8L73_C28_012510_DUZON_AI_ERP_CLOUD_CONTRACT_RETENTION | 012510 | 더존비즈온 | structural_success | positive | Stage2-Actionable | 2024-01-18 | 40,800 | current_profile_missed_structural |
| R8L73_C28_263860_GENIANS_ZERO_TRUST_CONTRACT_RETENTION | 263860 | 지니언스 | structural_success | positive | Stage2-Actionable | 2023-05-17 | 11,770 | current_profile_too_late |
| R8L73_C28_053800_AHNLAB_POLITICAL_SECURITY_THEME | 053800 | 안랩 | price_moved_without_evidence | counterexample | Stage2-WatchOnly | 2022-03-23 | 175,800 | current_profile_false_positive |
| R8L73_C28_030520_HANCOM_AI_THEME_WITHOUT_RETENTION | 030520 | 한글과컴퓨터 | false_positive_green | counterexample | Stage2-WatchOnly | 2024-01-10 | 24,750 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| label | count | cases |
|---|---:|---|
| positive_case_count | 2 | 더존비즈온; 지니언스 |
| counterexample_count | 2 | 안랩; 한글과컴퓨터 |
| 4B_case_count | 4 | all cases have local/full-window peak overlay checks |
| 4C_case_count | 1 | 안랩 price-theme false-break label, not production hard 4C |
| calibration_usable_case_count | 4 | all representative cases |
| calibration_usable_trigger_count | 4 | all representative triggers |

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | source note |
|---|---|---|---|---|---|
| 더존비즈온 | ['public_event_or_disclosure', 'customer_or_order_quality', 'capacity_or_volume_route', 'early_revision_signal'] | ['confirmed_revision', 'margin_bridge', 'financial_visibility', 'repeat_order_or_conversion', 'low_red_team_risk'] | ['valuation_blowoff', 'positioning_overheat'] | [] | stock-web rows show 2024-01-18 close 40,800, 2024-07-08 high 78,300, and profile CA candidates only in 2002/2006/2009, outside the window. |
| 지니언스 | ['public_event_or_disclosure', 'customer_or_order_quality', 'policy_or_regulatory_optionality', 'early_revision_signal'] | ['multiple_public_sources', 'repeat_order_or_conversion', 'financial_visibility'] | ['positioning_overheat'] | [] | stock-web rows show 2023-05-17 close 11,770 and 2023-06-13 high 17,640; profile CA dates are 2018 only, outside the 2023 window. |
| 안랩 | ['relative_strength'] | [] | ['price_only_local_peak', 'positioning_overheat'] | ['thesis_evidence_broken'] | stock-web rows show 2022-03-23 close 175,800, 2022-03-24 high 218,500, and 2022-10-21 low 58,900; profile CA candidate is 2005 only. |
| 한글과컴퓨터 | ['relative_strength', 'public_event_or_disclosure'] | [] | ['valuation_blowoff', 'positioning_overheat', 'price_only_local_peak'] | [] | stock-web rows show 2024-01-10 close 24,750, 2024-01-22 high 38,450, and 2024-08-05 low 15,100; profile CA candidates end in 2006. |

## 10. Price Data Source Map

| symbol | company | tradable shard | profile | corporate-action status |
|---:|---|---|---|---|
| 012510 | 더존비즈온 | atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv | atlas/symbol_profiles/012/012510.json | clean_180D_window |
| 263860 | 지니언스 | atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv | atlas/symbol_profiles/263/263860.json | clean_180D_window |
| 053800 | 안랩 | atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv | atlas/symbol_profiles/053/053800.json | clean_180D_window |
| 030520 | 한글과컴퓨터 | atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv | atlas/symbol_profiles/030/030520.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_date | entry_date | entry_price | same_entry_group_id | dedupe_for_aggregate | aggregate_group_role |
|---|---|---:|---:|---:|---|---:|---|
| R8L73_C28_012510_T1_STAGE2_AI_ERP_CLOUD_CONTRACT_RETENTION | R8L73_C28_012510_DUZON_AI_ERP_CLOUD_CONTRACT_RETENTION | 2024-01-18 | 2024-01-18 | 40,800 | 012510_2024-01-18_40800 | true | representative |
| R8L73_C28_263860_T1_STAGE2_ZERO_TRUST_SECURITY_RETENTION | R8L73_C28_263860_GENIANS_ZERO_TRUST_CONTRACT_RETENTION | 2023-05-17 | 2023-05-17 | 11,770 | 263860_2023-05-17_11770 | true | representative |
| R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME | R8L73_C28_053800_AHNLAB_POLITICAL_SECURITY_THEME | 2022-03-23 | 2022-03-23 | 175,800 | 053800_2022-03-23_175800 | true | representative |
| R8L73_C28_030520_T1_STAGE2_AI_OFFICE_THEME_WITHOUT_RETENTION | R8L73_C28_030520_HANCOM_AI_THEME_WITHOUT_RETENTION | 2024-01-10 | 2024-01-10 | 24,750 | 030520_2024-01-10_24750 | true | representative |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 012510 | 2024-01-18 | 40,800 | 37.99% | -11.27% | 60.78% | -11.27% | 91.91% | -11.27% | 2024-07-08 | 78,300 | -42.66% |
| 263860 | 2023-05-17 | 11,770 | 49.87% | -0.68% | 49.87% | -9.09% | 49.87% | -9.18% | 2023-06-13 | 17,640 | -39.40% |
| 053800 | 2022-03-23 | 175,800 | 24.29% | -46.59% | 24.29% | -53.92% | 24.29% | -66.50% | 2022-03-24 | 218,500 | -73.04% |
| 030520 | 2024-01-10 | 24,750 | 55.35% | -8.48% | 55.35% | -20.20% | 55.35% | -38.99% | 2024-01-22 | 38,450 | -60.73% |

## 13. Current Calibrated Profile Stress Test

| case | current profile verdict | actual 180D MFE / MAE | residual label |
|---|---|---|---|
| 더존비즈온 | current_profile_missed_structural | 91.91% / -11.27% | residual_error |
| 지니언스 | current_profile_too_late | 49.87% / -9.18% | residual_error |
| 안랩 | current_profile_false_positive | 24.29% / -66.50% | residual_error |
| 한글과컴퓨터 | current_profile_false_positive | 55.35% / -38.99% | residual_error |

Required stress answers:

1. Current profile can still over-credit price-only software/security moves when the ticker category looks structurally attractive.  
2. Real MFE/MAE alignment is better when the score distinguishes retention/renewal evidence from theme premium.  
3. Stage2 bonus is useful for 더존비즈온/지니언스 but too generous for 안랩/한글과컴퓨터 if customer/contract evidence is zero.  
4. Yellow 75 is acceptable after C28 component repair.  
5. Green 87/revision 55 should remain strict.  
6. Price-only blowoff guard is strengthened.  
7. Full 4B non-price requirement is strengthened because local peaks are common in software/security themes.  
8. Hard 4C routing is kept; most C28 theme collapses should be watch-only or 4B overlay unless customer/contract thesis breaks.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable | Yellow/Green implication | green_lateness_ratio | interpretation |
|---|---:|---|---:|---|
| 더존비즈온 | 2024-01-18 | Yellow after contract/AI-cloud monetization bridge confirmation | 0.39 | current profile may be too late if it waits for full financial confirmation |
| 지니언스 | 2023-05-17 | Yellow only after security contract/renewal evidence accumulates | 0.47 | smallcap security names need bridge but not price-only promotion |
| 안랩 | watch-only | should not Yellow/Green | n/a | price-only political premium must be blocked |
| 한글과컴퓨터 | watch-only | should not Yellow/Green without retention bridge | n/a | AI office optionality is not ARR/retention evidence |

## 15. 4B Local vs Full-window Timing Audit

| case | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 더존비즈온 | 0.93 | 0.93 | valuation_blowoff; positioning_overheat | good overlay only after retention/revision slowdown check |
| 지니언스 | 0.88 | 0.88 | positioning_overheat | post-spike 4B watch; not hard 4B without contract slowdown |
| 안랩 | 1.00 | 1.00 | price_only; event premium | price-only full-window peak is not positive evidence |
| 한글과컴퓨터 | 1.00 | 1.00 | price_only; valuation_blowoff | AI theme local peak without retention bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 더존비즈온 | not_applicable | no thesis break in 180D; 4B valuation overlay only |
| 지니언스 | not_applicable | no hard thesis break; post-spike confirmation needed |
| 안랩 | false_break_price_theme_only_not_fundamental_4C | the safer rule is to prevent promotion, not to declare business 4C |
| 한글과컴퓨터 | thesis_break_watch_only | AI optionality decayed; no hard contract break was needed at entry |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_name = c28_contract_retention_bridge_bonus
rule = For C28, Stage2-Actionable promotion requires at least one non-price customer/contract/retention bridge: enterprise renewal, cloud migration, regulated security demand, maintenance/ARR visibility, or repeat license expansion.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_name = c28_theme_premium_cap
rule = Security/software ticker category, AI office theme, political event premium, or pure relative strength cannot by itself create Stage2-Actionable or Stage3. If contract_score == 0 and customer_quality_score <= 4, cap at Stage2-WatchOnly and route price spikes to 4B overlay.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 47.57 | -23.62 | 55.35 | -31.48 | 0.5 | mixed |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 47.57 | -23.62 | 55.35 | -31.48 | 0.5 | worse_mixed |
| P1_sector_specific_C28_retention_bridge | sector_specific | 4 | 55.33 | -10.18 | 70.89 | -10.22 | 0.0 | improved |
| P2_canonical_C28_theme_cap | canonical_archetype_specific | 4 | 47.57 | -23.62 | 55.35 | -31.48 | 0.0 | improved_guardrail |
| P3_counterexample_guard_profile | counterexample_guard | 2 | 39.82 | -37.06 | 39.82 | -52.75 | 0.0 | guardrail_passed |

## 20. Score-Return Alignment Matrix

| symbol | weighted_before | stage_before | weighted_after | stage_after | MFE_90D | MAE_90D | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 012510 | 87 | Stage3-Green | 94 | Stage3-Green | 60.78% | -11.27% | aligned |
| 263860 | 81 | Stage3-Yellow | 86 | Stage3-Yellow | 49.87% | -9.09% | aligned |
| 053800 | 79 | Stage3-Yellow | 56 | Stage2-Watch | 24.29% | -53.92% | guardrail_needed |
| 030520 | 70 | Stage2-Actionable | 52 | Stage2-Watch | 55.35% | -20.20% | guardrail_needed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM | 2 | 2 | 4 | 1 | 4 | 0 | 4 | 4 | 3 | true | true | C28 now has positive/counterexample and 4B theme-cap coverage; future holdout should add pure ARR/SaaS renewal cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: current_profile_missed_structural; current_profile_too_late; current_profile_false_positive
new_axis_proposed: c28_contract_retention_bridge_bonus; c28_theme_premium_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- historical trigger-level calibration only
- Songdaiki/stock-web tradable 1D OHLC rows
- raw/unadjusted marcap basis
- 30D/90D/180D MFE/MAE and peak/drawdown comparison
- C28 software/security retention vs theme premium residual rule discovery

Non-validation scope:

- no live candidate scan
- no investment recommendation
- no production scoring change
- no stock_agent code inspection or patch
- no broker/API/autotrading logic

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_contract_retention_bridge_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"ERP/security software receives Stage2 promotion only when retention/renewal/contract or monetization bridge exists","selects positive cases while excluding theme-only counterexamples","R8L73_C28_012510_T1_STAGE2_AI_ERP_CLOUD_CONTRACT_RETENTION|R8L73_C28_263860_T1_STAGE2_ZERO_TRUST_SECURITY_RETENTION",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_theme_premium_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"political/AI/security ticker price premium without customer or contract evidence remains watch-only","reduces false positives in AhnLab/Hancom cases","R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME|R8L73_C28_030520_T1_STAGE2_AI_OFFICE_THEME_WITHOUT_RETENTION",4,4,2,medium,canonical_shadow_only,"strengthens price-only blowoff guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R8L73_C28_012510_DUZON_AI_ERP_CLOUD_CONTRACT_RETENTION","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L73_C28_012510_T1_STAGE2_AI_ERP_CLOUD_CONTRACT_RETENTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"ERP/그룹웨어/클라우드형 업무 소프트웨어는 단발성 테마가 아니라 기존 고객 기반, 전환비용, 구독·유지보수성 매출, AI/클라우드 업셀 가능성이 함께 보일 때 C28 Stage2-Actionable로 볼 수 있다. 2024년 초 더존비즈온은 AI/ERP 클라우드 전환 기대와 기존 기업고객 기반이 결합된 software retention bridge 표본이다."}
{"row_type":"case","case_id":"R8L73_C28_263860_GENIANS_ZERO_TRUST_CONTRACT_RETENTION","symbol":"263860","company_name":"지니언스","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R8L73_C28_263860_T1_STAGE2_ZERO_TRUST_SECURITY_RETENTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"제로트러스트/NAC/EDR 성격의 보안 소프트웨어는 신규 수주 자체보다 유지율·갱신·레퍼런스 확산이 핵심이다. 2023년 지니언스는 보안 수요와 제품군 확장 기대가 가격에 반영됐지만, C28에서는 대형 플랫폼 score보다 별도 security-contract bridge로 포착해야 한다."}
{"row_type":"case","case_id":"R8L73_C28_053800_AHNLAB_POLITICAL_SECURITY_THEME","symbol":"053800","company_name":"안랩","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"안랩 2022년 3월 움직임은 보안 제품·계약 유지율·갱신율·수주잔고가 아니라 정치/인물 프리미엄과 price-only blowoff에 가까웠다. C28에서는 security ticker라는 이유만으로 software contract retention score를 주면 안 된다는 대표 반례다."}
{"row_type":"case","case_id":"R8L73_C28_030520_HANCOM_AI_THEME_WITHOUT_RETENTION","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R8L73_C28_030520_T1_STAGE2_AI_OFFICE_THEME_WITHOUT_RETENTION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guardrail_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"AI 오피스/문서 소프트웨어 테마는 강한 MFE를 만들 수 있지만, 기업계약 갱신·클라우드 전환·ARPU 상승·유지율 evidence가 없으면 C28의 Stage3 evidence가 아니다. 한글과컴퓨터 2024년 1월 경로는 price-only AI optionality와 contract-retention bridge를 분리해야 하는 반례다."}
{"row_type":"trigger","trigger_id":"R8L73_C28_012510_T1_STAGE2_AI_ERP_CLOUD_CONTRACT_RETENTION","case_id":"R8L73_C28_012510_DUZON_AI_ERP_CLOUD_CONTRACT_RETENTION","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM","sector":"enterprise_software","primary_archetype":"enterprise_erp_ai_cloud_retention","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-18","evidence_available_at_that_date":"ERP/그룹웨어/클라우드형 업무 소프트웨어는 단발성 테마가 아니라 기존 고객 기반, 전환비용, 구독·유지보수성 매출, AI/클라우드 업셀 가능성이 함께 보일 때 C28 Stage2-Actionable로 볼 수 있다. 2024년 초 더존비즈온은 AI/ERP 클라우드 전환 기대와 기존 기업고객 기반이 결합된 software retention bridge 표본이다.","evidence_source":"stock-web rows show 2024-01-18 close 40,800, 2024-07-08 high 78,300, and profile CA candidates only in 2002/2006/2009, outside the window.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-18","entry_price":40800,"MFE_30D_pct":37.99,"MFE_90D_pct":60.78,"MFE_180D_pct":91.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.27,"MAE_90D_pct":-11.27,"MAE_180D_pct":-11.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300,"drawdown_after_peak_pct":-42.66,"green_lateness_ratio":0.39,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"valuation_repricing_near_full_window_peak_requires_retention_slowdown_check","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_contract_retention_bridge","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"012510_2024-01-18_40800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L73_C28_263860_T1_STAGE2_ZERO_TRUST_SECURITY_RETENTION","case_id":"R8L73_C28_263860_GENIANS_ZERO_TRUST_CONTRACT_RETENTION","symbol":"263860","company_name":"지니언스","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM","sector":"security_software","primary_archetype":"zero_trust_security_contract_retention","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-17","evidence_available_at_that_date":"제로트러스트/NAC/EDR 성격의 보안 소프트웨어는 신규 수주 자체보다 유지율·갱신·레퍼런스 확산이 핵심이다. 2023년 지니언스는 보안 수요와 제품군 확장 기대가 가격에 반영됐지만, C28에서는 대형 플랫폼 score보다 별도 security-contract bridge로 포착해야 한다.","evidence_source":"stock-web rows show 2023-05-17 close 11,770 and 2023-06-13 high 17,640; profile CA dates are 2018 only, outside the 2023 window.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-17","entry_price":11770,"MFE_30D_pct":49.87,"MFE_90D_pct":49.87,"MFE_180D_pct":49.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.68,"MAE_90D_pct":-9.09,"MAE_180D_pct":-9.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-13","peak_price":17640,"drawdown_after_peak_pct":-39.4,"green_lateness_ratio":0.47,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"security_contract_success_but_post_spike_retention_confirmation_needed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_smallcap_security_contract_retention","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"263860_2023-05-17_11770","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME","case_id":"R8L73_C28_053800_AHNLAB_POLITICAL_SECURITY_THEME","symbol":"053800","company_name":"안랩","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM","sector":"security_software","primary_archetype":"political_event_premium_not_contract_retention","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-WatchOnly","trigger_date":"2022-03-23","evidence_available_at_that_date":"안랩 2022년 3월 움직임은 보안 제품·계약 유지율·갱신율·수주잔고가 아니라 정치/인물 프리미엄과 price-only blowoff에 가까웠다. C28에서는 security ticker라는 이유만으로 software contract retention score를 주면 안 된다는 대표 반례다.","evidence_source":"stock-web rows show 2022-03-23 close 175,800, 2022-03-24 high 218,500, and 2022-10-21 low 58,900; profile CA candidate is 2005 only.","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-03-23","entry_price":175800,"MFE_30D_pct":24.29,"MFE_90D_pct":24.29,"MFE_180D_pct":24.29,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-46.59,"MAE_90D_pct":-53.92,"MAE_180D_pct":-66.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-24","peak_price":218500,"drawdown_after_peak_pct":-73.04,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_theme_full_window_peak_not_positive_stage","four_b_evidence_type":["price_only","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"false_break_price_theme_only_not_fundamental_4C","trigger_outcome_label":"price_only_theme_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"053800_2022-03-23_175800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R8L73_C28_030520_T1_STAGE2_AI_OFFICE_THEME_WITHOUT_RETENTION","case_id":"R8L73_C28_030520_HANCOM_AI_THEME_WITHOUT_RETENTION","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_SOFTWARE_CONTRACT_RETENTION_VS_THEME_PREMIUM","sector":"software_ai_office","primary_archetype":"ai_office_theme_without_contract_retention","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-WatchOnly","trigger_date":"2024-01-10","evidence_available_at_that_date":"AI 오피스/문서 소프트웨어 테마는 강한 MFE를 만들 수 있지만, 기업계약 갱신·클라우드 전환·ARPU 상승·유지율 evidence가 없으면 C28의 Stage3 evidence가 아니다. 한글과컴퓨터 2024년 1월 경로는 price-only AI optionality와 contract-retention bridge를 분리해야 하는 반례다.","evidence_source":"stock-web rows show 2024-01-10 close 24,750, 2024-01-22 high 38,450, and 2024-08-05 low 15,100; profile CA candidates end in 2006.","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","profile_path":"atlas/symbol_profiles/030/030520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-10","entry_price":24750,"MFE_30D_pct":55.35,"MFE_90D_pct":55.35,"MFE_180D_pct":55.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.48,"MAE_90D_pct":-20.2,"MAE_180D_pct":-38.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-22","peak_price":38450,"drawdown_after_peak_pct":-60.73,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"ai_theme_local_peak_without_contract_retention_bridge","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"ai_theme_high_MFE_but_poor_structural_alignment","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"030520_2024-01-10_24750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow","case_id":"R8L73_C28_012510_DUZON_AI_ERP_CLOUD_CONTRACT_RETENTION","trigger_id":"R8L73_C28_012510_T1_STAGE2_AI_ERP_CLOUD_CONTRACT_RETENTION","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":3,"margin_bridge_score":14,"revision_score":12,"relative_strength_score":13,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":87,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":14,"backlog_visibility_score":3,"margin_bridge_score":16,"revision_score":12,"relative_strength_score":13,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":94,"stage_label_after":"Stage3-Green","changed_components":["contract_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow separates recurring contract/retention bridge from security/software theme premium. Price-only or AI/political optionality is capped; contract retention and renewal evidence can promote.","MFE_90D_pct":60.78,"MAE_90D_pct":-11.27,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow","case_id":"R8L73_C28_263860_GENIANS_ZERO_TRUST_CONTRACT_RETENTION","trigger_id":"R8L73_C28_263860_T1_STAGE2_ZERO_TRUST_SECURITY_RETENTION","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":12,"customer_quality_score":12,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":2,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":12,"customer_quality_score":15,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow separates recurring contract/retention bridge from security/software theme premium. Price-only or AI/political optionality is capped; contract retention and renewal evidence can promote.","MFE_90D_pct":49.87,"MAE_90D_pct":-9.09,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow","case_id":"R8L73_C28_053800_AHNLAB_POLITICAL_SECURITY_THEME","trigger_id":"R8L73_C28_053800_T1_STAGE2_PRICE_ONLY_POLITICAL_SECURITY_THEME","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":18,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":24,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow separates recurring contract/retention bridge from security/software theme premium. Price-only or AI/political optionality is capped; contract retention and renewal evidence can promote.","MFE_90D_pct":24.29,"MAE_90D_pct":-53.92,"score_return_alignment_label":"guardrail_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow","case_id":"R8L73_C28_030520_HANCOM_AI_THEME_WITHOUT_RETENTION","trigger_id":"R8L73_C28_030520_T1_STAGE2_AI_OFFICE_THEME_WITHOUT_RETENTION","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":13,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":21,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage2-Watch","changed_components":["contract_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C28 shadow separates recurring contract/retention bridge from security/software theme premium. Price-only or AI/political optionality is capped; contract retention and renewal evidence can promote.","MFE_90D_pct":55.35,"MAE_90D_pct":-20.2,"score_return_alignment_label":"guardrail_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R8","loop":"73","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_missed_structural","current_profile_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/&lt;prefix&gt;/&lt;ticker&gt;/&lt;year&gt;.csv.
- Symbol profile pattern: atlas/symbol_profiles/&lt;prefix&gt;/&lt;ticker&gt;.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 73
next_round = R9
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files checked:

- `atlas/manifest.json` — manifest max_date, row counts, price adjustment status.
- `atlas/schema.json` — tradable/raw columns and MFE/MAE formulas.
- `atlas/symbol_profiles/012/012510.json` — 더존비즈온 profile, CA candidates outside tested window.
- `atlas/symbol_profiles/263/263860.json` — 지니언스 profile, CA candidates outside tested window.
- `atlas/symbol_profiles/053/053800.json` — 안랩 profile, CA candidate outside tested window.
- `atlas/symbol_profiles/030/030520.json` — 한글과컴퓨터 profile, CA candidates outside tested window.
- `atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv`.
- `atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv`.

Narrative evidence is used only for historical event timing/context. Quantitative calibration uses only stock-web tradable OHLC rows.

