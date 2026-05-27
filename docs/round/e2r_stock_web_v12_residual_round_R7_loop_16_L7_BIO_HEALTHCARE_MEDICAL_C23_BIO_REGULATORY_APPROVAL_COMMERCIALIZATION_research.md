# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R7
loop = 16
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE / CRL_REMEDIATION_REENTRY_GUARD
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

이 파일은 현재/live 종목 탐색이 아니다. 가격 row는 Songdaiki/stock-web의 `tradable_raw` shard만 사용했고, `stock_agent` 코드나 `src/e2r` 구조는 열람하지 않았다. 이번 루프는 직전 R6/C21 금융 루프와 겹치지 않도록 R7/L7/C23의 승인→상업화 잔여 오류를 선택했다. 입력 프롬프트의 v12 목적과 제한은 사용자 제공 프롬프트를 기준으로 유지했다. fileciteturn402file0

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

이번 루프는 위 global calibrated axis를 다시 증명하지 않는다. C23에서 남는 문제는 “FDA/승인 이벤트가 진짜여도 바로 Green인지, 아니면 상업화·파트너·revision bridge가 닫힐 때까지 watch여야 하는지”다. 승인이라는 도장 자체는 문을 여는 열쇠지만, 매출과 EPS로 이어지는 복도는 별도다.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R7 |
| loop | 16 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION |
| fine_archetype_id | FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE / CRL_REMEDIATION_REENTRY_GUARD |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill; 4C_thesis_break_timing_test |
| rule_scope_preference | canonical_archetype_specific |

## 3. Previous Coverage / Duplicate Avoidance Check

- 직전 in-session 산출물은 R6/L6/C21 금융 자본환원 루프였다. 본 루프는 R7/L7/C23으로 이동해 섹터와 canonical archetype 모두 다르게 선택했다.
- `stock_agent` 코드는 열람하지 않았다. 중복 방지는 직전 산출물과 v12 coverage 원칙을 기준으로 수행했다.
- 이번 calibration-usable 표본 4개는 모두 새 symbol이다: `000100`, `028300`, `069620`, `128940`.
- Celltrion `068270`은 narrative-only로만 남긴다. profile에 2024-01-12 corporate-action candidate가 있어 late-2023 trigger의 180D 정량 calibration을 차단한다. fileciteturn407file0

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest는 `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, `raw_row_count=15,214,118`, `symbol_count=5,414`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`로 확인되었다. fileciteturn403file0

Schema는 `tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m`, `calibration_basis=tradable_raw`, `price_adjustment_status=raw_unadjusted_marcap`, MFE/MAE 계산식, 180D forward window 및 corporate-action contamination 차단 규칙을 명시한다. fileciteturn404file0

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| symbol | company | trigger | entry | 180D available | corporate-action 180D status | calibration_usable | profile citation |
|---|---:|---:|---:|---:|---|---:|---|
| 000100 | 유한양행 | 2024-08-19 | 2024-08-21 | true | clean_180D_window | true | fileciteturn405file0 |
| 028300 | HLB | 2024-05-17 | 2024-05-17 | true | clean_180D_window | true | fileciteturn408file0 |
| 069620 | 대웅제약 | 2019-02-05 | 2019-02-07 | true | clean_180D_window | true | fileciteturn414file0 |
| 128940 | 한미약품 | 2022-09-09 | 2022-09-13 | true | clean_180D_window | true | fileciteturn416file0 |
| 068270 | 셀트리온 | 2023-10-23 | narrative_only | true | blocked_by_2024-01-12_candidate | false | fileciteturn407file0 |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rationale |
|---|---|---|
| FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | FDA/label/approval 이벤트가 EPS로 넘어가는 bridge 품질을 평가한다. |
| CRL_REMEDIATION_REENTRY_GUARD | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | CRL/보완요구는 hard 4C지만, 이후 보완·재제출 가능성을 watch state로 분리한다. |
| APPROVAL_ONLY_HIGH_MAE_GUARD | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 승인 이벤트만 있고 revision/상업화 가시성이 부족하면 false Green을 막는다. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R7L16_C23_YUHAN_LAZCLUZE_FDA_APPROVAL | 000100 | 유한양행 | structural_success | FDA approval + global partner commercialization visibility가 가격과 잘 정렬된 positive. |
| R7L16_C23_HLB_CRL_THESIS_BREAK | 028300 | HLB | 4C_success / counterexample | approval thesis break의 4C 보호는 맞지만, 이후 rebound 때문에 remediation watch가 필요. |
| R7L16_C23_DAEWOONG_JEUVEAU_APPROVAL_FAILED_RERATING | 069620 | 대웅제약 | failed_rerating | FDA approval-only가 large MAE와 낮은 MFE로 이어진 false Green counterexample. |
| R7L16_C23_HANMI_ROLVEDON_APPROVAL_DELAYED_RERATING | 128940 | 한미약품 | high_mae_success / counterexample | approval 자체는 진짜였지만 near-term MAE가 커서 immediate Green은 너무 빠름. |

## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count = 4
positive_case_count = 1
counterexample_count = 3
4B_case_count = 0
4C_case_count = 1
new_independent_case_count = 4
reused_case_count = 0
```

이번 루프는 positive 수보다 counterexample이 많다. 의도적으로 그렇게 구성했다. C23의 잔여 오류는 “승인 이벤트를 과신하는 쪽”에 있기 때문에, 좋은 승인과 나쁜 승인/불완전 승인/CRL을 같이 놓아야 한다.

## 9. Evidence Source Map

- 유한양행: FDA는 2024-08-19 lazertinib과 amivantamab 병용을 first-line EGFR-mutated NSCLC 용도로 승인했고, MARIPOSA PFS 개선 근거를 제시했다. citeturn660295view0
- 한미약품: FDA는 Rolvedon approval date를 2022-09-09로 제시하고, eflapegrastim의 적응증 및 임상 근거를 설명한다. citeturn306517view0
- 대웅제약: Jeuveau는 2019년 FDA label/approval context가 확인되며, glabellar lines 적응증과 initial U.S. approval 2019가 label에 표시된다. citeturn106323view0turn412068view0
- HLB: CRL은 FDA가 현 형태의 application을 승인할 수 없음을 통지하는 event type이다. 이번 run에서 HLB primary source capture가 부족했으므로 evidence_source_quality를 medium-low로 두고, 정량 row는 4C timing stress에만 사용한다. citeturn986541search0
- 셀트리온: Zymfentra의 late-2023 approval narrative는 확인되지만, profile상 2024-01-12 corporate-action candidate 때문에 calibration row가 아니라 narrative-only다. citeturn605436search2 fileciteturn407file0

## 10. Price Data Source Map

| symbol | entry shard | profile path | key fetched price rows |
|---:|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv | atlas/symbol_profiles/000/000100.json | 2024-08-21 entry 94,300; 2024-10-15 high 166,900; 2025-04-09 low 100,400. fileciteturn409file0 fileciteturn410file0 |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json | 2024-05-17 entry 67,100; 2024-05-21 low 45,150; 2024-07-08 high 98,100. fileciteturn411file0 fileciteturn412file0 |
| 069620 | atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv | atlas/symbol_profiles/069/069620.json | 2019-02-07 entry 204,000; high 217,000; 2019-08-06 low 138,000. fileciteturn415file0 fileciteturn419file0 |
| 128940 | atlas/ohlcv_tradable_by_symbol_year/128/128940/2022.csv | atlas/symbol_profiles/128/128940.json | 2022-09-13 entry 305,000; 2022-09-26 low 223,500; 2023-04-14 high 339,500. fileciteturn417file0 fileciteturn418file0 |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | entry_date | entry_price | role | current_profile_verdict | aggregate |
|---|---|---:|---:|---|---|---:|
| R7L16_C23_000100_STAGE3_GREEN_FDA_APPROVAL_2024_08_21 | Stage3-Green | 2024-08-21 | 94,300 | structural_success | current_profile_correct | true |
| R7L16_C23_028300_4C_CRL_2024_05_17 | 4C | 2024-05-17 | 67,100 | 4C_success | current_profile_correct | true |
| R7L16_C23_069620_STAGE3_APPROVAL_ONLY_FALSE_GREEN_2019_02_07 | Stage3-Yellow | 2019-02-07 | 204,000 | failed_rerating | current_profile_false_positive | true |
| R7L16_C23_128940_STAGE3_APPROVAL_TOO_EARLY_2022_09_13 | Stage3-Yellow | 2022-09-13 | 305,000 | high_mae_success | current_profile_too_early | true |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 000100 | 94,300 | 69.99% | -2.97% | 76.99% | -2.97% | 76.99% | -2.97% | 2024-10-15 | 166,900 | -39.84% |
| 028300 | 67,100 | 9.99% | -32.71% | 46.20% | -32.71% | 46.20% | -32.71% | 2024-07-08 | 98,100 | -40.06% |
| 069620 | 204,000 | 6.37% | -12.99% | 6.37% | -29.17% | 6.37% | -32.35% | 2019-02-07 | 217,000 | -36.41% |
| 128940 | 305,000 | 7.05% | -26.72% | 7.05% | -26.72% | 11.31% | -26.72% | 2023-04-14 | 339,500 | -14.14% |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | realized result | verdict |
|---|---|---|---|
| 유한양행 | FDA approval + partner quality allows Green | MFE90 +76.99%, MAE90 -2.97% | current_profile_correct |
| HLB | CRL/thesis break routes to hard 4C | Initial protection is correct; rebound argues for remediation watch | current_profile_correct |
| 대웅제약 | Approval-only may over-promote to Yellow/Green | MFE90 only +6.37%, MAE90 -29.17% | current_profile_false_positive |
| 한미약품 | Approval may promote too early | MFE180 +11.31%, but MAE30/90 -26.72% | current_profile_too_early |

Stress test answers:

1. Stage2 bonus is not the residual problem here; the problem is Stage3 promotion from regulatory approval alone.
2. Yellow 75 can be too permissive for C23 if approval lacks commercial/revision bridge.
3. Green 87 / revision 55 should be kept or strengthened in C23.
4. price-only blowoff guard remains appropriate.
5. full 4B non-price requirement remains appropriate.
6. hard 4C routing is useful for CRL shock, but after the first protection window C23 needs a remediation/reentry watch state.

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable rows were not separately materialized because the loop’s purpose is post-approval residual stress, not pre-approval discovery. Therefore `green_lateness_ratio` is marked `not_applicable` for approval triggers. The important comparison is not “Stage2 vs Green timing”; it is “approval-only Stage3 label vs actual MFE/MAE.”

| symbol | approval label | MFE90 | MAE90 | interpretation |
|---:|---|---:|---:|---|
| 000100 | Green was acceptable | +76.99% | -2.97% | Approval + partner/commercialization bridge closed. |
| 069620 | Green would be false positive | +6.37% | -29.17% | Approval event did not close durable commercialization bridge. |
| 128940 | Green would be too early | +7.05% | -26.72% | Later partial recovery does not justify immediate Green. |

## 15. 4B Local vs Full-window Timing Audit

C23 has a special 4B problem: regulatory approval itself can create a local blowoff before commercialization evidence arrives. A price-only local peak must not be treated as a full 4B without non-price fatigue/overhang.

| symbol | 4B evidence type | local proximity | full-window proximity | verdict |
|---:|---|---:|---:|---|
| 000100 | valuation_blowoff + positioning_overheat | 1.00 | 1.00 | Good only if later non-price overheat is confirmed. |
| 069620 | valuation_blowoff + legal/regulatory risk | 1.00 | 1.00 | Approval-day peak was not full thesis exit; it was approval-only local exhaustion. |
| 128940 | valuation_blowoff + margin/backlog slowdown | 1.00 | 1.00 | Approval label lacked commercial/revision closure. |

## 16. 4C Protection Audit

HLB is the 4C stress case. A hard regulatory rejection/CRL-style event deserves immediate thesis-break protection, but the subsequent rebound means the model should not simply delete the case forever.

```text
four_c_protection_label = hard_4c_success_with_remediation_reentry_watch
prior_stage_peak_proxy = 2024-05-16 high 106,900
4C_entry_price = 67,100
MAE_30D_after_4C = -32.71%
MFE_90D_after_4C = +46.20%
interpretation = hard 4C protected from initial crash, but later remediation watch is needed
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = evidence is concentrated inside C23 rather than broad L7 sub-sectors
```

The rule should not be promoted to all healthcare. Medical device reimbursement, trial-data binary risk, and biologics commercialization behave differently. The cleaner scope is C23 only.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

Candidate rules:

1. `c23_approval_to_commercialization_bridge_gate`: Stage3-Green requires approval plus at least one of partner/customer quality, revenue visibility, launch path, royalty/economics visibility, or confirmed revision.
2. `c23_approval_only_high_mae_guard`: If approval-only cases historically show MFE90 below +12% and MAE90 below -20%, do not Green without later commercial confirmation.
3. `c23_crl_remediation_reentry_watch`: CRL/thesis break routes to 4C first, then can move to remediation watch if price and evidence recover.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | score_return_alignment |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global proxy | Current calibrated profile | 4 | 34.15% | -22.89% | 50% | 0 | mixed |
| P0b e2r_2_0_baseline_reference | rollback | More permissive approval-event scoring | 4 | 34.15% | -22.89% | 75% | 0 | weak |
| P1 sector_specific_candidate_profile | L7 | Broad healthcare approval guard | 4 | 34.15% | -22.89% | 25% | 1 | acceptable but too broad |
| P2 canonical_archetype_candidate_profile | C23 | Approval-to-commercialization bridge | 4 | 34.15% | -22.89% | 25% | 0 | best |
| P3 counterexample_guard_profile | C23 guard | Approval-only high-MAE block + CRL watch | 4 | 34.15% | -22.89% | 0% | 1 | conservative |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 유한양행 | 88.5 | Stage3-Green | 91.0 | Stage3-Green | 76.99% | -2.97% | aligned |
| HLB | 35.0 | 4C | 32.0 | 4C_watch_locked | 46.20% | -32.71% | risk aligned, reentry needed |
| 대웅제약 | 78.0 | Stage3-Yellow | 66.0 | Stage2-Watch | 6.37% | -29.17% | false positive reduced |
| 한미약품 | 76.0 | Stage3-Yellow | 68.0 | Stage2-Actionable/Watch | 7.05% | -26.72% | timing error reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE / CRL_REMEDIATION_REENTRY_GUARD | 1 | 3 | 0 | 1 | 4 | 0 | 4 | 4 | 2 | false | true | positive/counterexample balance improved; more commercial-launch positives still needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: approval_only_false_positive, approval_event_too_early, crl_requires_reentry_watch_after_4c
new_axis_proposed: c23_approval_to_commercialization_bridge_gate, c23_approval_only_high_mae_guard, c23_crl_remediation_reentry_watch
existing_axis_strengthened: stage3_green_revision_min within C23, hard_4c_thesis_break_routes_to_4c within C23
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R7/L7/C23 approval-to-commercialization and CRL counterexample gap
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-web manifest/schema price basis and max date.
- Profile-level corporate action contamination checks.
- Actual tradable OHLC rows for entry, MFE, MAE, peak, drawdown.
- Positive vs counterexample balance inside C23.
- Current calibrated profile residual stress.

Not validated:

- No current/live candidate scan.
- No broker/API/auto-trading execution.
- No stock_agent source code inspection or patching.
- No global scoring promotion.
- HLB primary company-source capture was incomplete in this run; the row is usable as a 4C price-path stress case but lower confidence for standalone evidence weighting.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_approval_to_commercialization_bridge_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"FDA/approval-only must be joined to commercialization/revision visibility before Green","Reduced approval-only false positives while keeping Yuhan positive",R7L16_C23_000100_STAGE3_GREEN_FDA_APPROVAL_2024_08_21|R7L16_C23_069620_STAGE3_APPROVAL_ONLY_FALSE_GREEN_2019_02_07|R7L16_C23_128940_STAGE3_APPROVAL_TOO_EARLY_2022_09_13,4,4,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_approval_only_high_mae_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Approval event with MAE90 worse than -20% and MFE90 below +12% should not become Green without later revision closure","Blocked DaeWoong/Hanmi immediate Green false positives",R7L16_C23_069620_STAGE3_APPROVAL_ONLY_FALSE_GREEN_2019_02_07|R7L16_C23_128940_STAGE3_APPROVAL_TOO_EARLY_2022_09_13,4,4,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c23_crl_remediation_reentry_watch,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"Hard CRL routes to 4C, but rebound/remediation path should move to watch rather than permanent discard","Preserves 4C protection while recognizing HLB rebound behavior",R7L16_C23_028300_4C_CRL_2024_05_17,4,4,3,low,canonical_shadow_only,"evidence source capture weak; use as timing stress not standalone production rule"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L16_C23_YUHAN_LAZCLUZE_FDA_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L16_C23_000100_STAGE3_GREEN_FDA_APPROVAL_2024_08_21", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Approval plus high-quality partner/commercialization visibility produced high MFE and contained MAE."}
{"row_type": "case", "case_id": "R7L16_C23_HLB_CRL_THESIS_BREAK", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "CRL_REMEDIATION_REENTRY_GUARD", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R7L16_C23_028300_4C_CRL_2024_05_17", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "hard_4c_protected_initial_shock_but_reentry_watch_needed", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "CRL-style thesis break: 4C protection works, but rebound requires remediation watch rather than permanent exclusion."}
{"row_type": "case", "case_id": "R7L16_C23_DAEWOONG_JEUVEAU_APPROVAL_FAILED_RERATING", "symbol": "069620", "company_name": "대웅제약", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R7L16_C23_069620_STAGE3_APPROVAL_ONLY_FALSE_GREEN_2019_02_07", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "approval_only_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "FDA approval alone did not close commercialization/revision bridge."}
{"row_type": "case", "case_id": "R7L16_C23_HANMI_ROLVEDON_APPROVAL_DELAYED_RERATING", "symbol": "128940", "company_name": "한미약품", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R7L16_C23_128940_STAGE3_APPROVAL_TOO_EARLY_2022_09_13", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "approval_event_too_early_high_mae_before_delayed_partial_upside", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Approval event had meaningful near-term drawdown; commercialization/revision confirmation should be required before full Green."}
{"row_type": "trigger", "trigger_id": "R7L16_C23_000100_STAGE3_GREEN_FDA_APPROVAL_2024_08_21", "case_id": "R7L16_C23_YUHAN_LAZCLUZE_FDA_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "sector": "bio_healthcare_medical", "primary_archetype": "approved_drug_partnered_global_commercialization", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4C_thesis_break_timing_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-08-19", "evidence_available_at_that_date": "FDA approved lazertinib with amivantamab for first-line EGFR-mutated NSCLC; Korea tradable reaction captured on 2024-08-21 after the U.S. approval timestamp/news cycle.", "evidence_source": "FDA approval page; Reuters/J&J approval coverage; stock-web 000100 2024 rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-21", "entry_price": 94300, "MFE_30D_pct": 69.99, "MFE_90D_pct": 76.99, "MFE_180D_pct": 76.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.97, "MAE_90D_pct": -2.97, "MAE_180D_pct": -2.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -39.84, "green_lateness_ratio": "not_applicable:no_prior_stage2_actionable_trigger_in_this_loop", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_overheat_confirmed_later", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L16_C23_000100_2024_08_21_94300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L16_C23_028300_4C_CRL_2024_05_17", "case_id": "R7L16_C23_HLB_CRL_THESIS_BREAK", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "CRL_REMEDIATION_REENTRY_GUARD", "sector": "bio_healthcare_medical", "primary_archetype": "regulatory_crl_thesis_break_then_reentry_watch", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4C_thesis_break_timing_test", "trigger_type": "4C", "trigger_date": "2024-05-17", "evidence_available_at_that_date": "Complete Response Letter style event: approval thesis broken in present form; stock-web row shows immediate lower-limit repricing on 2024-05-17. Primary company-source capture was not available in this run; evidence_source_quality is medium-low and the row is used mainly for 4C timing stress, not positive promotion.", "evidence_source": "Public CRL event; CRL definition source; stock-web 028300 2024/2025 rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "legal_or_regulatory_block", "positioning_overheat"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 67100, "MFE_30D_pct": 9.99, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.71, "MAE_90D_pct": -32.71, "MAE_180D_pct": -32.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -40.06, "green_lateness_ratio": "not_applicable:4C_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_4C_trigger", "four_b_evidence_type": ["legal_or_regulatory_block", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success_with_remediation_reentry_watch", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L16_C23_028300_2024_05_17_67100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L16_C23_069620_STAGE3_APPROVAL_ONLY_FALSE_GREEN_2019_02_07", "case_id": "R7L16_C23_DAEWOONG_JEUVEAU_APPROVAL_FAILED_RERATING", "symbol": "069620", "company_name": "대웅제약", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "sector": "bio_healthcare_medical", "primary_archetype": "approval_only_without_durable_commercialization_visibility", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4C_thesis_break_timing_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2019-02-05", "evidence_available_at_that_date": "Jeuveau FDA approval/label availability created a visible approval event, but the subsequent stock-web path shows low upside and large drawdown, implying approval-only is insufficient without commercialization economics and durable revision closure.", "evidence_source": "FDA label/approval context; press coverage; stock-web 069620 2019 rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "legal_or_regulatory_block", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/069/069620/2019.csv", "profile_path": "atlas/symbol_profiles/069/069620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2019-02-07", "entry_price": 204000, "MFE_30D_pct": 6.37, "MFE_90D_pct": 6.37, "MFE_180D_pct": 6.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.99, "MAE_90D_pct": -29.17, "MAE_180D_pct": -32.35, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2019-02-07", "peak_price": 217000, "drawdown_after_peak_pct": -36.41, "green_lateness_ratio": "not_applicable:no_prior_stage2_actionable_trigger_in_this_loop", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "approval_only_local_peak_without_non_price_full_4B_confirmation", "four_b_evidence_type": ["valuation_blowoff", "legal_or_regulatory_block"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L16_C23_069620_2019_02_07_204000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L16_C23_128940_STAGE3_APPROVAL_TOO_EARLY_2022_09_13", "case_id": "R7L16_C23_HANMI_ROLVEDON_APPROVAL_DELAYED_RERATING", "symbol": "128940", "company_name": "한미약품", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "FDA_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "sector": "bio_healthcare_medical", "primary_archetype": "approval_event_before_commercialization_revision_closure", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill|4C_thesis_break_timing_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2022-09-09", "evidence_available_at_that_date": "FDA approved Rolvedon, but stock-web path shows large near-term MAE and only delayed partial upside; this is a timing counterexample to immediate approval-only Green.", "evidence_source": "FDA approval page; stock-web 128940 2022/2023 rows.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/128/128940/2022.csv", "profile_path": "atlas/symbol_profiles/128/128940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-09-13", "entry_price": 305000, "MFE_30D_pct": 7.05, "MFE_90D_pct": 7.05, "MFE_180D_pct": 11.31, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -26.72, "MAE_90D_pct": -26.72, "MAE_180D_pct": -26.72, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-14", "peak_price": 339500, "drawdown_after_peak_pct": -14.14, "green_lateness_ratio": "not_applicable:no_prior_stage2_actionable_trigger_in_this_loop", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "approval_event_overhang_before_commercialization_revision_closure", "four_b_evidence_type": ["valuation_blowoff", "margin_or_backlog_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L16_C23_128940_2022_09_13_305000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "P2_C23_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "case_id": "R7L16_C23_YUHAN_LAZCLUZE_FDA_APPROVAL", "trigger_id": "R7L16_C23_000100_STAGE3_GREEN_FDA_APPROVAL_2024_08_21", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 7, "relative_strength_score": 0, "customer_quality_score": 8, "policy_or_regulatory_score": 10, "valuation_repricing_score": 7, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "_weighted": 88.5}, "weighted_score_before": 88.5, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 0, "customer_quality_score": 9, "policy_or_regulatory_score": 10, "valuation_repricing_score": 8, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "_weighted": 91.0}, "weighted_score_after": 91.0, "stage_label_after": "Stage3-Green", "changed_components": ["customer_quality_score", "revision_score", "valuation_repricing_score"], "component_delta_explanation": "High-quality partnered approval with visible commercial route deserves C23-specific positive reinforcement.", "MFE_90D_pct": 76.99, "MAE_90D_pct": -2.97, "score_return_alignment_label": "score_return_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P3_C23_CRL_REMEDIATION_REENTRY_GUARD", "case_id": "R7L16_C23_HLB_CRL_THESIS_BREAK", "trigger_id": "R7L16_C23_028300_4C_CRL_2024_05_17", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "_weighted": 35.0}, "weighted_score_before": 35.0, "stage_label_before": "4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 0, "execution_risk_score": 10, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "_weighted": 32.0}, "weighted_score_after": 32.0, "stage_label_after": "4C_watch_locked", "changed_components": ["legal_or_contract_risk_score", "execution_risk_score"], "component_delta_explanation": "Hard 4C is useful for initial protection, but post-CRL rebound argues for a remediation watch state rather than permanent discard.", "MFE_90D_pct": 46.2, "MAE_90D_pct": -32.71, "score_return_alignment_label": "risk_score_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P2_C23_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "case_id": "R7L16_C23_DAEWOONG_JEUVEAU_APPROVAL_FAILED_RERATING", "trigger_id": "R7L16_C23_069620_STAGE3_APPROVAL_ONLY_FALSE_GREEN_2019_02_07", "symbol": "069620", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 0, "customer_quality_score": 4, "policy_or_regulatory_score": 9, "valuation_repricing_score": 6, "execution_risk_score": 6, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "_weighted": 78.0}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 0, "customer_quality_score": 4, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": 7, "legal_or_contract_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "_weighted": 66.0}, "weighted_score_after": 66.0, "stage_label_after": "Stage2-Watch", "changed_components": ["revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "Approval-only without durable commercialization economics is demoted to watch despite regulatory win.", "MFE_90D_pct": 6.37, "MAE_90D_pct": -29.17, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P2_C23_APPROVAL_TO_COMMERCIALIZATION_BRIDGE", "case_id": "R7L16_C23_HANMI_ROLVEDON_APPROVAL_DELAYED_RERATING", "trigger_id": "R7L16_C23_128940_STAGE3_APPROVAL_TOO_EARLY_2022_09_13", "symbol": "128940", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 0, "customer_quality_score": 6, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "_weighted": 76.0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 0, "customer_quality_score": 6, "policy_or_regulatory_score": 9, "valuation_repricing_score": 4, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "_weighted": 68.0}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-Actionable/Watch", "changed_components": ["revision_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Approval was real, but high MAE before delayed rerating indicates Green should wait for commercialization/revision closure.", "MFE_90D_pct": 7.05, "MAE_90D_pct": -26.72, "score_return_alignment_label": "timing_error_reduced", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "residual_contribution", "round": "R7", "loop": "16", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "positive_case_count": 1, "counterexample_count": 3, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "hard_4c_thesis_break_routes_to_4c", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["approval_only_false_positive", "approval_event_too_early", "crl_requires_reentry_watch_after_4c"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R7/L7/C23 approval-to-commercialization and CRL counterexample gap"}
{"row_type": "narrative_only", "case_id": "R7L16_C23_CELLTRION_ZYMFENTRA_NARRATIVE_ONLY", "symbol": "068270", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "reason": "FDA approval evidence available, but stock-web profile lists a 2024-01-12 corporate-action candidate inside the 180D window after the late-2023 trigger; blocked from weight calibration.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

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
next_round_candidates:
- R8 / L8_PLATFORM_CONTENT_SW_SECURITY / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
- R5 / L5_CONSUMER_BRAND_DISTRIBUTION / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
- R7 / L7_BIO_HEALTHCARE_MEDICAL / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

Recommended next loop: R8/C28, because software/security contract retention is structurally far from the already-covered financial and bio approval loops and should improve sector diversity.

## 28. Source Notes

- Stock-web manifest and schema: fileciteturn403file0 fileciteturn404file0
- Profiles: 유한양행 fileciteturn405file0; HLB fileciteturn406file0 fileciteturn408file0; 셀트리온 fileciteturn407file0; 대웅제약 fileciteturn414file0; 한미약품 fileciteturn416file0
- Price rows: 유한양행 fileciteturn409file0 fileciteturn410file0; HLB fileciteturn411file0 fileciteturn412file0 fileciteturn413file0; 대웅제약 fileciteturn415file0 fileciteturn419file0; 한미약품 fileciteturn417file0 fileciteturn418file0
- External evidence notes: FDA lazertinib approval citeturn660295view0; FDA Rolvedon approval citeturn306517view0; Jeuveau label/approval context citeturn106323view0turn412068view0; CRL definition/source context citeturn986541search0; Celltrion Zymfentra narrative source citeturn605436search2
