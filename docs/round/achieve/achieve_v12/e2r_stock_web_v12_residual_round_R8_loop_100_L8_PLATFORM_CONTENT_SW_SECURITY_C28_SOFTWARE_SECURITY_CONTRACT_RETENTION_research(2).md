# E2R Stock-Web V12 Residual Research — C28_SOFTWARE_SECURITY_CONTRACT_RETENTION second pass

```yaml
output_file: e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
selected_round: R8
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows static ledger; C28 rows=28, need_to_30=2
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: mixed_C28_security_sw_recurring_revenue_retention_second_pass
loop_objective: coverage_gap_fill | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

V12는 순환 라운드가 아니라 coverage-index 우선 방식이다. Static No-Repeat ledger에서 C28은 `28 rows / need to 30 = 2`인 Priority 0 canonical로 남아 있으므로 R8/L8로 파생했다. 이전 C28 pass에서 쓴 `012510`, `030520`, `053800`, `434480`, `203650`은 모두 제외했고, 이번 파일은 `263860`, `150900`, `136540`, `208350`, `042510`, `131090` 새 symbol set으로 구성했다.

Hard duplicate key check:
```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION + 263860 + Stage3-Yellow + 2024-11-15 = new_in_this_session
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION + 150900 + Stage2-Actionable + 2024-12-13 = new_in_this_session
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION + 136540 + Stage2-Actionable + 2025-02-06 = new_in_this_session
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION + 208350 + Stage2-Actionable + 2025-05-08 = new_in_this_session
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION + 042510 + Stage3-Yellow + 2025-05-13 = new_in_this_session
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION + 131090 + Stage2 + 2024-05-17 = new_in_this_session
```

## 2. Price source validation

Stock-Web manifest max date is `2026-02-20`. Price basis is `tradable_raw`, adjustment status is `raw_unadjusted_marcap`, and calibration shard root is `atlas/ohlcv_tradable_by_symbol_year`. For each trigger, entry is the next tradable day after evidence date, and 30D/90D/180D MFE·MAE use the high/low path from the entry row over N tradable rows.

Corporate-action screen:
```text
263860 지니언스: entry=2024-11-15 180D_end=2025-08-12 overlap=[] status=clean_180D_window
150900 파수: entry=2024-12-13 180D_end=2025-09-10 overlap=[] status=clean_180D_window
136540 윈스: entry=2025-02-06 180D_end=2025-10-31 overlap=[] status=clean_180D_window
208350 지란지교시큐리티: entry=2025-05-08 180D_end=2026-01-29 overlap=[] status=clean_180D_window
042510 라온시큐어: entry=2025-05-13 180D_end=2026-02-03 overlap=[] status=clean_180D_window
131090 시큐브: entry=2024-05-17 180D_end=2025-02-13 overlap=[] status=clean_180D_window
```

## 3. Case set summary

| case_id | symbol | company | role | trigger | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | DD after peak | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| C28_R8L100_263860_01 | 263860 | 지니언스 | positive / structural_success | Stage3-Yellow 2024-11-14 | 2024-11-15 | 9410 | 16.79% | -8.82% | 40.81% | -8.82% | 153.99% | -8.82% | 2025-07-11 23900 | -23.01% | current_profile_missed_structural |
| C28_R8L100_150900_02 | 150900 | 파수 | counterexample / failed_rerating | Stage2-Actionable 2024-12-12 | 2024-12-13 | 5080 | 6.30% | -8.56% | 10.83% | -18.31% | 10.83% | -18.31% | 2025-04-02 5630 | -26.29% | current_profile_false_positive |
| C28_R8L100_136540_03 | 136540 | 윈스 | positive / stage2_promote_candidate | Stage2-Actionable 2025-02-05 | 2025-02-06 | 11000 | 2.45% | -6.18% | 18.00% | -6.18% | 21.82% | -6.18% | 2025-07-10 13400 | -10.30% | current_profile_correct |
| C28_R8L100_208350_04 | 208350 | 지란지교시큐리티 | positive / stage2_promote_candidate | Stage2-Actionable 2025-05-07 | 2025-05-08 | 2655 | 18.27% | -5.27% | 18.27% | -5.27% | 24.29% | -5.27% | 2025-12-01 3300 | -13.64% | current_profile_correct |
| C28_R8L100_042510_05 | 042510 | 라온시큐어 | positive / high_mae_success | Stage3-Yellow 2025-05-12 | 2025-05-13 | 9540 | 44.76% | -5.35% | 44.76% | -5.35% | 44.76% | -6.18% | 2025-06-24 13810 | -35.19% | current_profile_4B_too_late |
| C28_R8L100_131090_06 | 131090 | 시큐브 | counterexample / failed_rerating | Stage2 2024-05-16 | 2024-05-17 | 961 | 2.29% | -10.20% | 3.75% | -21.54% | 8.84% | -21.54% | 2025-01-06 1046 | -14.91% | current_profile_false_positive |

## 4. Case narratives

### C28_R8L100_263860_01 — 263860 지니언스

- Evidence date: `2024-11-14` / entry: `2024-11-15` at `9410`.
- Evidence source: https://www.genians.co.kr/pr-room/press/20241114
- Evidence: 2024년 3분기 매출·영업이익 급증, 지자체·대기업 NAC 수요 확대, 클라우드 NAC managed service 고객 지속 확보.
- Path result: MFE90 `40.81%`, MAE90 `-8.82%`, MFE180 `153.99%`, MAE180 `-8.82%`, post-peak drawdown `-23.01%`.
- Interpretation: NAC/EDR/Zero Trust core 사업과 managed service 고객 확보가 함께 보이므로 C28에서 Stage3-Yellow를 허용할 수 있는 positive holdout.

### C28_R8L100_150900_02 — 150900 파수

- Evidence date: `2024-12-12` / entry: `2024-12-13` at `5080`.
- Evidence source: https://w4.kirs.or.kr/download/research/241212_%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%ED%8C%8C%EC%88%98%28150900%29_%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B3%B4%EC%95%88%20%EC%86%94%EB%A3%A8%EC%85%98%20%EA%B0%9C%EB%B0%9C%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf
- Evidence: 데이터 보안 솔루션과 구독형 모델의 높은 갱신율 가능성은 확인되나, event 시점에는 ARR·renewal 수치와 margin bridge가 미완성.
- Path result: MFE90 `10.83%`, MAE90 `-18.31%`, MFE180 `10.83%`, MAE180 `-18.31%`, post-peak drawdown `-26.29%`.
- Interpretation: 구독형 전환 서사는 C28 Stage2 근거지만, ARR/renewal 공개와 이익률 전환이 없으면 Stage3-Green을 막아야 한다.

### C28_R8L100_136540_03 — 136540 윈스

- Evidence date: `2025-02-05` / entry: `2025-02-06` at `11000`.
- Evidence source: https://m.boannews.com/html/detail.html?idx=135835
- Evidence: 2024년 보안기업 매출 분석에서 윈스는 정부 예산 축소 영향과 통합관제 서비스 개발 방향이 함께 언급됨.
- Path result: MFE90 `18.00%`, MAE90 `-6.18%`, MFE180 `21.82%`, MAE180 `-6.18%`, post-peak drawdown `-10.30%`.
- Interpretation: 관제/보안 서비스의 안정성은 있으나 외형성장 둔화 때문에 Green보다 Stage2-Actionable이 맞는 positive control.

### C28_R8L100_208350_04 — 208350 지란지교시큐리티

- Evidence date: `2025-05-07` / entry: `2025-05-08` at `2655`.
- Evidence source: https://www.iva.or.kr/notice/BBS_0003/2646
- Evidence: 2024년 별도 매출은 소폭 감소했지만 영업이익은 73.5% 증가, 메일보안 사업부 매출 증가 확인.
- Path result: MFE90 `18.27%`, MAE90 `-5.27%`, MFE180 `24.29%`, MAE180 `-5.27%`, post-peak drawdown `-13.64%`.
- Interpretation: 메일보안 반복 수요와 이익 개선은 Stage2/Yellow boundary지만 연결 실적과 사업부 mix가 완전 Green은 아니다.

### C28_R8L100_042510_05 — 042510 라온시큐어

- Evidence date: `2025-05-12` / entry: `2025-05-13` at `9540`.
- Evidence source: https://www.boannews.com/media/view.asp?idx=137107&kind=3
- Evidence: 2024년 역대 최고 매출, 서비스 플랫폼·해외 디지털 ID·구독형 생체 인증 확대가 확인됨.
- Path result: MFE90 `44.76%`, MAE90 `-5.35%`, MFE180 `44.76%`, MAE180 `-6.18%`, post-peak drawdown `-35.19%`.
- Interpretation: 서비스/플랫폼 반복매출 route는 positive지만 급등 후 drawdown이 커서 Stage3-Yellow와 local 4B watch를 동시에 기록해야 한다.

### C28_R8L100_131090_06 — 131090 시큐브

- Evidence date: `2024-05-16` / entry: `2024-05-17` at `961`.
- Evidence source: https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516002357&docno=&method=search&viewerhost=
- Evidence: 2024년 1분기 보고서 기준 매출·수주 상황과 영업손실 확인. 보안 제품 사업은 있으나 반복계약/마진 bridge가 약함.
- Path result: MFE90 `3.75%`, MAE90 `-21.54%`, MFE180 `8.84%`, MAE180 `-21.54%`, post-peak drawdown `-14.91%`.
- Interpretation: 보안 솔루션 명목만으로 Stage2를 열면 90D MAE가 -20%를 넘는 C28 false-positive가 된다.

## 5. Current calibrated profile stress test

C28에서 residual error는 세 갈래다. 첫째, `security demand` headline만 보고 Stage3-Yellow를 열면 파수·시큐브 같은 weak-retention false positive가 생긴다. 둘째, 라온시큐어처럼 MFE가 커도 post-peak drawdown이 큰 경우 Stage3와 local 4B watch를 동시에 기록해야 한다. 셋째, 지니언스처럼 managed-service customer 확보와 이익 visibility가 같이 확인되면 current profile은 오히려 too-late가 될 수 있다.

## 6. Score simulation profile comparison

| profile_id | scope | hypothesis | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 현행 C28 gate: 보안/소프트웨어 수요와 일부 recurring evidence를 Stage2~Yellow로 허용 | 6 | 22.74% | -10.91% | 44.09% | -11.05% | 0.333 | 1 | reference_or_guard |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 구버전 baseline: contract/retention 분리가 약해 테마형 보안주를 과승격 | 6 | 22.74% | -10.91% | 44.09% | -11.05% | 0.5 | 2 | reference_or_guard |
| P1_L8_security_sw_recurring_revenue_gate | sector_specific | L8 보안/SW에서 계약·renewal·ARR/managed-service visibility를 Stage3 gate로 요구 | 6 | 22.74% | -10.91% | 44.09% | -11.05% | 0.167 | 0 | reference_or_guard |
| P2_C28_contract_retention_margin_bridge_gate | canonical_archetype_specific | C28 전용으로 recurring revenue, retention, maintenance/managed-service margin bridge를 분리 | 6 | 22.74% | -10.91% | 44.09% | -11.05% | 0.167 | 0 | best_candidate |
| P3_C28_high_mae_guard_profile | counterexample_guard | MFE가 커도 90D/180D MAE 또는 post-peak drawdown이 큰 경우 local 4B watch를 강제 | 6 | 22.74% | -10.91% | 44.09% | -11.05% | 0.0 | 1 | reference_or_guard |

## 7. Proposed shadow rule

```text
C28_SECURITY_SW_CONTRACT_RETENTION_REQUIRES_ARR_RENEWAL_MANAGED_SERVICE_MARGIN_BRIDGE_WITH_HIGH_MAE_LOCAL_4B_CAP
```

Rule mechanics:
1. Stage2-Actionable can be opened by verified public security demand, product/customer evidence, or public financial visibility.
2. Stage3-Yellow requires at least two of: ARR/renewal metric, managed-service customer expansion, maintenance/technical-support repeat revenue, or margin bridge.
3. Stage3-Green requires low red-team risk and no high-MAE/post-peak drawdown warning.
4. If MFE90 or MFE180 is high but post-peak drawdown exceeds roughly 25%, keep positive evidence but add local Stage4B watch.

## 8. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | mixed_C28_security_sw_recurring_revenue_retention_second_pass | 4 | 2 | 4 | 0 | 6 | 0 | 6 | 6 | 4 | L8_SECURITY_SW_RECURRING_REVENUE_AND_HIGH_MAE_SPLIT | C28_SECURITY_SW_CONTRACT_RETENTION_REQUIRES_ARR_RENEWAL_MANAGED_SERVICE_MARGIN_BRIDGE | static 28→34; session-adjusted C28 33→39 |

## 9. Machine-readable rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C28_R8L100_263860_01", "symbol": "263860", "company_name": "지니언스", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage3-Yellow", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_high_mfe_low_initial_mae", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "NAC/EDR/Zero Trust core 사업과 managed service 고객 확보가 함께 보이므로 C28에서 Stage3-Yellow를 허용할 수 있는 positive holdout."}
{"row_type": "case", "case_id": "C28_R8L100_150900_02", "symbol": "150900", "company_name": "파수", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "subscription_story_without_arr_bridge_high_drawdown", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "구독형 전환 서사는 C28 Stage2 근거지만, ARR/renewal 공개와 이익률 전환이 없으면 Stage3-Green을 막아야 한다."}
{"row_type": "case", "case_id": "C28_R8L100_136540_03", "symbol": "136540", "company_name": "윈스", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_mae_stage2_with_moderate_forward_mfe", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "관제/보안 서비스의 안정성은 있으나 외형성장 둔화 때문에 Green보다 Stage2-Actionable이 맞는 positive control."}
{"row_type": "case", "case_id": "C28_R8L100_208350_04", "symbol": "208350", "company_name": "지란지교시큐리티", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "margin_bridge_stage2_positive_not_full_green", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "메일보안 반복 수요와 이익 개선은 Stage2/Yellow boundary지만 연결 실적과 사업부 mix가 완전 Green은 아니다."}
{"row_type": "case", "case_id": "C28_R8L100_042510_05", "symbol": "042510", "company_name": "라온시큐어", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "Stage3-Yellow", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_mfe_but_peak_drawdown_requires_local_4b", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "서비스/플랫폼 반복매출 route는 positive지만 급등 후 drawdown이 커서 Stage3-Yellow와 local 4B watch를 동시에 기록해야 한다."}
{"row_type": "case", "case_id": "C28_R8L100_131090_06", "symbol": "131090", "company_name": "시큐브", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "weak_contract_retention_evidence_mae_over_20pct", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "보안 솔루션 명목만으로 Stage2를 열면 90D MAE가 -20%를 넘는 C28 false-positive가 된다."}
{"row_type": "trigger", "trigger_id": "C28_R8L100_263860_01_Stage3_Yellow_2024-11-15", "case_id": "C28_R8L100_263860_01", "symbol": "263860", "company_name": "지니언스", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-11-14", "entry_date": "2024-11-15", "entry_price": 9410.0, "evidence_available_at_that_date": "2024년 3분기 매출·영업이익 급증, 지자체·대기업 NAC 수요 확대, 클라우드 NAC managed service 고객 지속 확보", "evidence_source": "https://www.genians.co.kr/pr-room/press/20241114", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "security_demand", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv", "profile_path": "atlas/symbol_profiles/263/263860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.79, "MFE_90D_pct": 40.81, "MFE_180D_pct": 153.99, "MAE_30D_pct": -8.82, "MAE_90D_pct": -8.82, "MAE_180D_pct": -8.82, "peak_date": "2025-07-11", "peak_price": 23900.0, "drawdown_after_peak_pct": -23.01, "green_lateness_ratio": 0.735, "four_b_local_peak_proximity": 0.77, "four_b_full_window_peak_proximity": 0.265, "trigger_outcome_label": "structural_success_high_mfe_low_initial_mae", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage3-Yellow|2024-11-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_R8L100_150900_02_Stage2_Actionable_2024-12-13", "case_id": "C28_R8L100_150900_02", "symbol": "150900", "company_name": "파수", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-12-12", "entry_date": "2024-12-13", "entry_price": 5080.0, "evidence_available_at_that_date": "데이터 보안 솔루션과 구독형 모델의 높은 갱신율 가능성은 확인되나, event 시점에는 ARR·renewal 수치와 margin bridge가 미완성", "evidence_source": "https://w4.kirs.or.kr/download/research/241212_%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%ED%8C%8C%EC%88%98%28150900%29_%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B3%B4%EC%95%88%20%EC%86%94%EB%A3%A8%EC%85%98%20%EA%B0%9C%EB%B0%9C%20%EC%A0%84%EB%AC%B8%EA%B8%B0%EC%97%85_NICE%EB%94%94%EC%95%A4%EB%B9%84.pdf", "stage2_evidence_fields": ["public_event_or_disclosure", "security_demand", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "explicit_event_cap", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv", "profile_path": "atlas/symbol_profiles/150/150900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.3, "MFE_90D_pct": 10.83, "MFE_180D_pct": 10.83, "MAE_30D_pct": -8.56, "MAE_90D_pct": -18.31, "MAE_180D_pct": -18.31, "peak_date": "2025-04-02", "peak_price": 5630.0, "drawdown_after_peak_pct": -26.29, "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": 0.737, "four_b_full_window_peak_proximity": 1.0, "trigger_outcome_label": "subscription_story_without_arr_bridge_high_drawdown", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|150900|Stage2-Actionable|2024-12-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_R8L100_136540_03_Stage2_Actionable_2025-02-06", "case_id": "C28_R8L100_136540_03", "symbol": "136540", "company_name": "윈스", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-02-05", "entry_date": "2025-02-06", "entry_price": 11000.0, "evidence_available_at_that_date": "2024년 보안기업 매출 분석에서 윈스는 정부 예산 축소 영향과 통합관제 서비스 개발 방향이 함께 언급됨", "evidence_source": "https://m.boannews.com/html/detail.html?idx=135835", "stage2_evidence_fields": ["public_event_or_disclosure", "security_demand", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/136/136540/2025.csv", "profile_path": "atlas/symbol_profiles/136/136540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.45, "MFE_90D_pct": 18.0, "MFE_180D_pct": 21.82, "MAE_30D_pct": -6.18, "MAE_90D_pct": -6.18, "MAE_180D_pct": -6.18, "peak_date": "2025-07-10", "peak_price": 13400.0, "drawdown_after_peak_pct": -10.3, "green_lateness_ratio": 0.175, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": 0.825, "trigger_outcome_label": "low_mae_stage2_with_moderate_forward_mfe", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|136540|Stage2-Actionable|2025-02-06", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_R8L100_208350_04_Stage2_Actionable_2025-05-08", "case_id": "C28_R8L100_208350_04", "symbol": "208350", "company_name": "지란지교시큐리티", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-05-07", "entry_date": "2025-05-08", "entry_price": 2655.0, "evidence_available_at_that_date": "2024년 별도 매출은 소폭 감소했지만 영업이익은 73.5% 증가, 메일보안 사업부 매출 증가 확인", "evidence_source": "https://www.iva.or.kr/notice/BBS_0003/2646", "stage2_evidence_fields": ["public_event_or_disclosure", "security_demand", "financial_visibility"], "stage3_evidence_fields": ["margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/208/208350/2025.csv", "profile_path": "atlas/symbol_profiles/208/208350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.27, "MFE_90D_pct": 18.27, "MFE_180D_pct": 24.29, "MAE_30D_pct": -5.27, "MAE_90D_pct": -5.27, "MAE_180D_pct": -5.27, "peak_date": "2025-12-01", "peak_price": 3300.0, "drawdown_after_peak_pct": -13.64, "green_lateness_ratio": 0.248, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": 0.752, "trigger_outcome_label": "margin_bridge_stage2_positive_not_full_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|208350|Stage2-Actionable|2025-05-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_R8L100_042510_05_Stage3_Yellow_2025-05-13", "case_id": "C28_R8L100_042510_05", "symbol": "042510", "company_name": "라온시큐어", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2025-05-12", "entry_date": "2025-05-13", "entry_price": 9540.0, "evidence_available_at_that_date": "2024년 역대 최고 매출, 서비스 플랫폼·해외 디지털 ID·구독형 생체 인증 확대가 확인됨", "evidence_source": "https://www.boannews.com/media/view.asp?idx=137107&kind=3", "stage2_evidence_fields": ["public_event_or_disclosure", "security_demand", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042510/2025.csv", "profile_path": "atlas/symbol_profiles/042/042510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 44.76, "MFE_90D_pct": 44.76, "MFE_180D_pct": 44.76, "MAE_30D_pct": -5.35, "MAE_90D_pct": -5.35, "MAE_180D_pct": -6.18, "peak_date": "2025-06-24", "peak_price": 13810.0, "drawdown_after_peak_pct": -35.19, "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": 0.648, "four_b_full_window_peak_proximity": 1.0, "trigger_outcome_label": "large_mfe_but_peak_drawdown_requires_local_4b", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|042510|Stage3-Yellow|2025-05-13", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_R8L100_131090_06_Stage2_2024-05-17", "case_id": "C28_R8L100_131090_06", "symbol": "131090", "company_name": "시큐브", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "mixed_C28_security_sw_recurring_revenue_retention_second_pass", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2024-05-16", "entry_date": "2024-05-17", "entry_price": 961.0, "evidence_available_at_that_date": "2024년 1분기 보고서 기준 매출·수주 상황과 영업손실 확인. 보안 제품 사업은 있으나 반복계약/마진 bridge가 약함", "evidence_source": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516002357&docno=&method=search&viewerhost=", "stage2_evidence_fields": ["public_event_or_disclosure", "security_demand"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/131/131090/2024.csv", "profile_path": "atlas/symbol_profiles/131/131090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.29, "MFE_90D_pct": 3.75, "MFE_180D_pct": 8.84, "MAE_30D_pct": -10.2, "MAE_90D_pct": -21.54, "MAE_180D_pct": -21.54, "peak_date": "2025-01-06", "peak_price": 1046.0, "drawdown_after_peak_pct": -14.91, "green_lateness_ratio": 0.576, "four_b_local_peak_proximity": 0.851, "four_b_full_window_peak_proximity": 0.424, "trigger_outcome_label": "weak_contract_retention_evidence_mae_over_20pct", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|131090|Stage2|2024-05-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow", "case_id": "C28_R8L100_263860_01", "trigger_id": "C28_R8L100_263860_01_Stage3_Yellow_2024-11-15", "symbol": "263860", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 70, "retention_or_arr_score": 68, "revenue_visibility_score": 75, "margin_bridge_score": 72, "customer_quality_score": 70, "security_demand_score": 80, "relative_strength_score": 60, "valuation_overheat_score": 30, "execution_risk_score": 25, "accounting_trust_risk_score": 10}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 75, "retention_or_arr_score": 74, "revenue_visibility_score": 80, "margin_bridge_score": 76, "customer_quality_score": 70, "security_demand_score": 80, "relative_strength_score": 60, "valuation_overheat_score": 25, "execution_risk_score": 22, "accounting_trust_risk_score": 10}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["retention_or_arr_score", "revenue_visibility_score", "margin_bridge_score", "valuation_overheat_score", "execution_risk_score"], "component_delta_explanation": "C28에서는 보안/SW 테마 자체가 아니라 ARR/renewal/managed-service visibility와 margin bridge를 Stage3 gate로 쓰고, high-MAE 또는 post-peak drawdown은 local 4B로 분리한다.", "MFE_90D_pct": 40.81, "MAE_90D_pct": -8.82, "score_return_alignment_label": "structural_success_high_mfe_low_initial_mae", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow", "case_id": "C28_R8L100_150900_02", "trigger_id": "C28_R8L100_150900_02_Stage2_Actionable_2024-12-13", "symbol": "150900", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 55, "retention_or_arr_score": 60, "revenue_visibility_score": 48, "margin_bridge_score": 42, "customer_quality_score": 55, "security_demand_score": 75, "relative_strength_score": 42, "valuation_overheat_score": 55, "execution_risk_score": 52, "accounting_trust_risk_score": 10}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 55, "retention_or_arr_score": 45, "revenue_visibility_score": 40, "margin_bridge_score": 34, "customer_quality_score": 55, "security_demand_score": 75, "relative_strength_score": 42, "valuation_overheat_score": 62, "execution_risk_score": 60, "accounting_trust_risk_score": 10}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch", "changed_components": ["retention_or_arr_score", "revenue_visibility_score", "margin_bridge_score", "valuation_overheat_score", "execution_risk_score"], "component_delta_explanation": "C28에서는 보안/SW 테마 자체가 아니라 ARR/renewal/managed-service visibility와 margin bridge를 Stage3 gate로 쓰고, high-MAE 또는 post-peak drawdown은 local 4B로 분리한다.", "MFE_90D_pct": 10.83, "MAE_90D_pct": -18.31, "score_return_alignment_label": "subscription_story_without_arr_bridge_high_drawdown", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow", "case_id": "C28_R8L100_136540_03", "trigger_id": "C28_R8L100_136540_03_Stage2_Actionable_2025-02-06", "symbol": "136540", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 60, "retention_or_arr_score": 55, "revenue_visibility_score": 58, "margin_bridge_score": 50, "customer_quality_score": 60, "security_demand_score": 70, "relative_strength_score": 45, "valuation_overheat_score": 20, "execution_risk_score": 28, "accounting_trust_risk_score": 10}, "weighted_score_before": 67, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 60, "retention_or_arr_score": 58, "revenue_visibility_score": 60, "margin_bridge_score": 55, "customer_quality_score": 60, "security_demand_score": 70, "relative_strength_score": 45, "valuation_overheat_score": 18, "execution_risk_score": 28, "accounting_trust_risk_score": 10}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable", "changed_components": ["retention_or_arr_score", "revenue_visibility_score", "margin_bridge_score", "valuation_overheat_score", "execution_risk_score"], "component_delta_explanation": "C28에서는 보안/SW 테마 자체가 아니라 ARR/renewal/managed-service visibility와 margin bridge를 Stage3 gate로 쓰고, high-MAE 또는 post-peak drawdown은 local 4B로 분리한다.", "MFE_90D_pct": 18.0, "MAE_90D_pct": -6.18, "score_return_alignment_label": "low_mae_stage2_with_moderate_forward_mfe", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow", "case_id": "C28_R8L100_208350_04", "trigger_id": "C28_R8L100_208350_04_Stage2_Actionable_2025-05-08", "symbol": "208350", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 58, "retention_or_arr_score": 50, "revenue_visibility_score": 55, "margin_bridge_score": 64, "customer_quality_score": 52, "security_demand_score": 65, "relative_strength_score": 48, "valuation_overheat_score": 22, "execution_risk_score": 35, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 58, "retention_or_arr_score": 55, "revenue_visibility_score": 55, "margin_bridge_score": 68, "customer_quality_score": 52, "security_demand_score": 65, "relative_strength_score": 48, "valuation_overheat_score": 22, "execution_risk_score": 30, "accounting_trust_risk_score": 10}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable", "changed_components": ["retention_or_arr_score", "revenue_visibility_score", "margin_bridge_score", "valuation_overheat_score", "execution_risk_score"], "component_delta_explanation": "C28에서는 보안/SW 테마 자체가 아니라 ARR/renewal/managed-service visibility와 margin bridge를 Stage3 gate로 쓰고, high-MAE 또는 post-peak drawdown은 local 4B로 분리한다.", "MFE_90D_pct": 18.27, "MAE_90D_pct": -5.27, "score_return_alignment_label": "margin_bridge_stage2_positive_not_full_green", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow", "case_id": "C28_R8L100_042510_05", "trigger_id": "C28_R8L100_042510_05_Stage3_Yellow_2025-05-13", "symbol": "042510", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 65, "retention_or_arr_score": 62, "revenue_visibility_score": 72, "margin_bridge_score": 63, "customer_quality_score": 65, "security_demand_score": 76, "relative_strength_score": 80, "valuation_overheat_score": 70, "execution_risk_score": 48, "accounting_trust_risk_score": 10}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 65, "retention_or_arr_score": 68, "revenue_visibility_score": 75, "margin_bridge_score": 68, "customer_quality_score": 65, "security_demand_score": 76, "relative_strength_score": 80, "valuation_overheat_score": 78, "execution_risk_score": 55, "accounting_trust_risk_score": 10}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow+local_4B_watch", "changed_components": ["retention_or_arr_score", "revenue_visibility_score", "margin_bridge_score", "valuation_overheat_score", "execution_risk_score"], "component_delta_explanation": "C28에서는 보안/SW 테마 자체가 아니라 ARR/renewal/managed-service visibility와 margin bridge를 Stage3 gate로 쓰고, high-MAE 또는 post-peak drawdown은 local 4B로 분리한다.", "MFE_90D_pct": 44.76, "MAE_90D_pct": -5.35, "score_return_alignment_label": "large_mfe_but_peak_drawdown_requires_local_4b", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C28_shadow", "case_id": "C28_R8L100_131090_06", "trigger_id": "C28_R8L100_131090_06_Stage2_2024-05-17", "symbol": "131090", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 38, "retention_or_arr_score": 30, "revenue_visibility_score": 35, "margin_bridge_score": 22, "customer_quality_score": 38, "security_demand_score": 58, "relative_strength_score": 28, "valuation_overheat_score": 25, "execution_risk_score": 62, "accounting_trust_risk_score": 10}, "weighted_score_before": 61, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 30, "retention_or_arr_score": 25, "revenue_visibility_score": 28, "margin_bridge_score": 18, "customer_quality_score": 38, "security_demand_score": 58, "relative_strength_score": 28, "valuation_overheat_score": 25, "execution_risk_score": 68, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/blocked", "changed_components": ["retention_or_arr_score", "revenue_visibility_score", "margin_bridge_score", "valuation_overheat_score", "execution_risk_score"], "component_delta_explanation": "C28에서는 보안/SW 테마 자체가 아니라 ARR/renewal/managed-service visibility와 margin bridge를 Stage3 gate로 쓰고, high-MAE 또는 post-peak drawdown은 local 4B로 분리한다.", "MFE_90D_pct": 3.75, "MAE_90D_pct": -21.54, "score_return_alignment_label": "weak_contract_retention_evidence_mae_over_20pct", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R8", "loop": "100", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "new_independent_case_count": 6, "reused_case_count": 0, "new_symbol_count": 6, "new_trigger_family_count": 6, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["C28_theme_story_without_retention_bridge_false_positive", "C28_high_MFE_high_drawdown_local_4B_late", "C28_recurring_security_demand_missed_structural"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### Shadow weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C28_retention_arr_managed_service_margin_bridge_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,Stage3 requires retention/ARR/managed-service and margin bridge,Lower false positives from 파수/시큐브 while preserving 지니언스/라온/윈스/지란지교 positives,C28_R8L100_263860_01_Stage3_Yellow_2024-11-15|C28_R8L100_150900_02_Stage2_Actionable_2024-12-13|C28_R8L100_136540_03_Stage2_Actionable_2025-02-06|C28_R8L100_208350_04_Stage2_Actionable_2025-05-08|C28_R8L100_042510_05_Stage3_Yellow_2025-05-13|C28_R8L100_131090_06_Stage2_2024-05-17,6,6,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C28_high_mae_local_4b_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,High MFE with post-peak drawdown should not be treated as clean Green,Flags 라온시큐어/파수/시큐브 high-risk outcomes without deleting positive evidence,C28_R8L100_263860_01_Stage3_Yellow_2024-11-15|C28_R8L100_150900_02_Stage2_Actionable_2024-12-13|C28_R8L100_042510_05_Stage3_Yellow_2025-05-13|C28_R8L100_131090_06_Stage2_2024-05-17,4,4,2,medium,guardrail_shadow_only,not production; local 4B watch only
```

## 10. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - C28_story_without_retention_bridge_false_positive
  - C28_high_MFE_post_peak_drawdown_local_4B_late
  - C28_verified_managed_service_positive_missed_structural
new_axis_proposed: C28_SECURITY_SW_CONTRACT_RETENTION_REQUIRES_ARR_RENEWAL_MANAGED_SERVICE_MARGIN_BRIDGE_WITH_HIGH_MAE_LOCAL_4B_CAP
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L8_SECURITY_SW_RECURRING_REVENUE_AND_HIGH_MAE_SPLIT
canonical_archetype_rule_candidate: C28_SECURITY_SW_CONTRACT_RETENTION_REQUIRES_ARR_RENEWAL_MANAGED_SERVICE_MARGIN_BRIDGE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation coding agent. Do not treat this MD as an immediate production patch. Ingest the machine-readable rows, validate filename/metadata consistency, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, verify every trigger has complete 30D/90D/180D MFE/MAE and clean 180D corporate-action window, then test the shadow-only C28 retention/ARR/managed-service margin bridge gate against the existing v12 representative row corpus. Only propose production changes if aggregate validation across the full corpus supports it.
```

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 2
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 13. Next research state

```text
completed_round = R8
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C28 static 28 rows
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_followup_if_below_50 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```