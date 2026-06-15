# E2R Stock-Web V12 Residual Research — R6 / C21 Financial ROE-PBR Capital Return Quality Holdout

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R6
selected_loop: 101
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: mixed_C21_financial_roe_pbr_capital_return_quality_holdout
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality holdout; C21 static rows=79, symbols=23, guidance=URL/proxy 보강 + 반례/4B 균형 확인
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
output_filename: e2r_stock_web_v12_residual_round_R6_loop_101_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: '2026-02-20'
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

이번 실행은 R6 금융 섹터의 C21 품질 holdout이다. 정적 No-Repeat Index에서 C21은 이미 79 rows로 50 row 이상 구역이므로 단순 수량 채우기가 아니라, ROE/PBR/자본환원 축의 URL 보강, 4B watch, 반례 균형 확인이 목적이다.

- Static top-covered C21 symbols include `105560`, `055550`, `316140`, `005940`, `005830`, `006800`; 이번 파일은 이 top-covered set을 피했다.
- 이번 case set은 `138040`, `175330`, `024110`, `138930`, `039490`, `071050`으로 구성했다.
- hard duplicate key인 `canonical_archetype_id + symbol + trigger_type + entry_date` 기준으로 이 세션의 기존 C21 생성물은 없으므로 신규 holdout row로 취급한다.
- 단, Priority 2 quality holdout이므로 새 weight delta는 작게 제안하고, rule candidate 중심으로 남긴다.

## 2. Stock-Web manifest/schema confirmation

Stock-Web manifest confirms `max_date=2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, and calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. All rows below use tradable 1D OHLCV and the entry-date close as `entry_price`. 30D/90D/180D MFE uses the maximum high in the forward N tradable-row window, and MAE uses the minimum low in that same window.

## 3. Case thesis summary

C21에서는 “저PBR + 밸류업 발표”를 바로 Stage3로 열면 안 된다. 금융주는 자본을 덜 쓰고 ROE를 끌어올릴 수 있는지, CET1 또는 자본비율이 주주환원을 지탱하는지, buyback/cancel 또는 배당성향 공식이 실행 가능한지, 그리고 자산건전성·브로커리지 변동성·정책은행 제약이 있는지를 같이 봐야 한다.

이번 holdout의 핵심 분해는 다음과 같다.

1. **명시적 주주환원율 + 자본배치 공식**: 메리츠금융지주, JB금융지주.
2. **정책·자본비율 제약이 있는 delayed positive**: 기업은행.
3. **자사주/배당 계획은 있지만 asset-quality overhang이 Green을 막는 케이스**: BNK금융지주.
4. **좋은 계획이지만 180D window에서 즉시 Green이 아니라 실행 확인이 필요했던 케이스**: 키움증권.
5. **주주환원 목표가 없어도 ROE-growth path가 너무 강하면 current profile이 늦어질 수 있는 반례**: 한국금융지주.

## 4. Human-readable case table

| symbol | name | trigger_date | entry_date | entry_price | role | trigger_type | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | DD after peak | rule read |
|---|---|---:|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 138040 | 메리츠금융지주 | 2024-07-04 | 2024-07-05 | 83400 | positive | Stage3-Green | 8.1535 | -11.8705 | 28.5372 | -11.8705 | 52.7578 | -11.8705 | 2025-03-06 | 127400 | -9.8901 | explicit_shareholder_return_rate_plus_capital_allocation_framework |
| 175330 | JB금융지주 | 2024-09-24 | 2024-09-25 | 15030 | positive | Stage3-Green | 24.4844 | -1.3972 | 36.3939 | -1.3972 | 48.3699 | -1.3972 | 2025-06-17 | 22300 | -8.0717 | high_roe_target_plus_shareholder_return_formula |
| 024110 | 기업은행 | 2024-12-05 | 2024-12-06 | 14600 | delayed_positive | Stage3-Yellow | 1.9863 | -3.2192 | 8.6986 | -8.2877 | 53.4247 | -8.2877 | 2025-07-15 | 22400 | -17.4107 | payout_formula_present_but_policy_bank_cet1_execution_needed |
| 138930 | BNK금융지주 | 2024-08-01 | 2024-08-02 | 9440 | counterexample_with_4b_watch | Stage2-Actionable | 9.5339 | -8.8983 | 26.0593 | -8.8983 | 30.2966 | -8.8983 | 2025-01-31 | 12300 | -24.7154 | capital_return_present_but_asset_quality_overhang_blocks_green |
| 039490 | 키움증권 | 2024-05-28 | 2024-05-29 | 129500 | counterexample_delayed_execution | Stage2-Actionable | 8.4170 | -7.7992 | 13.0502 | -11.0425 | 13.0502 | -14.6718 | 2024-07-16 | 146400 | -24.5219 | excellent_plan_but_entry_window_needs_execution_confirmation |
| 071050 | 한국금융지주 | 2025-05-26 | 2025-05-27 | 100200 | positive_capital_return_absence_counterexample | Stage3-Yellow | 51.9960 | -2.0958 | 63.6727 | -2.0958 | 197.4052 | -2.0958 | 2026-02-20 | 298000 | -6.2081 | high_roe_growth_can_rerate_even_without_buyback_but_green_requires_payout_or_repeat_eps |


## 5. Case notes

### 5.1 138040 메리츠금융지주 — explicit capital allocation positive

Evidence was not a generic low-PBR rally. The event linked shareholder return to capital allocation: the company approved a value-up plan and disclosed that through FY2025 it would return at least 50% of consolidated net income, then compare internal investment return, buyback return, and cash dividend return from FY2026 onward. The price path opened with moderate drawdown: MFE180 `52.7578%`, MAE180 `-11.8705%`. This supports Stage3-Green only when explicit shareholder-return formula and capital-allocation mechanism are both visible.

### 5.2 175330 JB금융지주 — high-ROE + explicit shareholder-return formula positive

JBFG is the cleanest C21 row in this pass. The trigger disclosed long-term goals of ROE 15%, shareholder return ratio 50%, and buyback/cancellation share 40%, plus a 2026 intermediate route of ROE 13%+, shareholder return 45%, and buyback/cancel on return above a 28% cash payout. The 180D window produced MFE180 `48.3699%` with only MAE180 `-1.3972%`. This is the C21 ideal: ROE, PBR, capital return, and execution formula align.

### 5.3 024110 기업은행 — delayed positive, not immediate Green

IBK disclosed ROE 10%+, payout 40%+, PBR 1.0 target, and quarterly dividend introduction. The path was initially sleepy and even negative through 90D, then caught up strongly by 180D. This row argues against an immediate Stage3-Green on the announcement day: policy-bank constraints and CET1/payout execution need confirmation. However, if the profile waits for too much realized execution, it misses the later 180D MFE of `53.4247%`.

### 5.4 138930 BNK금융지주 — capital return with asset-quality overhang

BNK had Q2 profit improvement, CET1 improvement, buyback cancellation, interim dividend, and an additional buyback/cancel plan. But the same release showed NPL and delinquency deterioration. The path still generated MFE180 `30.2966%`, but post-peak drawdown reached `-24.7154%`. This row says C21 should not treat capital return in isolation; asset-quality overhang should cap Green and add local 4B watch.

### 5.5 039490 키움증권 — excellent plan, execution timing matters

Kiwoom was an early value-up leader with ROE 15%, shareholder return 30%, PBR 1x goal and treasury-share cancellation route. Yet the 180D window from the plan date did not confirm a clean immediate rerating: MFE180 `13.0502%`, MAE180 `-14.6718%`, and drawdown after peak `-24.5219%`. This is not thesis failure; it is a timing/confirmation row. It should be Stage2-Actionable until execution/ROE delivery tightens.

### 5.6 071050 한국금융지주 — no explicit buyback, but ROE-growth path can still rerate

한국금융지주는 2030년 ROE 15%+와 자기자본 15조원 목표를 제시했지만, explicit buyback/cancel or payout ratio target was not the core of the plan. A rule that requires buyback/cancel for every C21 Green would have missed a large move: MFE180 `197.4052%`, MAE180 `-2.0958%`. The rule should therefore split C21 into two gates: capital-return execution for bank-like balance sheets, and ROE-growth compounding for brokerage/financial holding names, with Green still requiring repeat EPS/ROE or shareholder-return follow-through.

## 6. Machine-readable trigger rows JSONL

```jsonl
{"symbol": "138040", "name": "메리츠금융지주", "trigger_date": "2024-07-04", "trigger_type": "Stage3-Green", "case_role": "positive", "evidence_family": "valueup_50pct_shareholder_return_capital_allocation", "evidence_summary": "금융지주 1호 밸류업 실행계획. 2025년까지 연결 당기순이익의 50% 이상 주주환원, 2026년부터 내부투자수익률·자사주매입수익률·현금배당수익률 비교 기반 자본배치.", "evidence_url": "https://news.einfomax.co.kr/news/articleView.html?idxno=4315880", "rule_read": "explicit_shareholder_return_rate_plus_capital_allocation_framework", "entry_date": "2024-07-05", "entry_price": 83400.0, "MFE_30D_pct": 8.1535, "MAE_30D_pct": -11.8705, "peak_30D_date": "2024-08-16", "peak_30D_price": 90200.0, "trough_30D_date": "2024-08-05", "trough_30D_price": 73500.0, "MFE_90D_pct": 28.5372, "MAE_90D_pct": -11.8705, "peak_90D_date": "2024-10-21", "peak_90D_price": 107200.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 73500.0, "MFE_180D_pct": 52.7578, "MAE_180D_pct": -11.8705, "peak_180D_date": "2025-03-06", "peak_180D_price": 127400.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 73500.0, "peak_date": "2025-03-06", "peak_price": 127400.0, "post_peak_low_180D": 114800.0, "drawdown_after_peak_180D_pct": -9.8901, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "selected_round": "R6", "selected_loop": 101, "fine_archetype_id": "mixed_C21_financial_roe_pbr_capital_return_quality_holdout", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": false, "residual_error_type": "none_or_minor"}
{"symbol": "175330", "name": "JB금융지주", "trigger_date": "2024-09-24", "trigger_type": "Stage3-Green", "case_role": "positive", "evidence_family": "roe15_shareholder_return50_buyback_cancel_plan", "evidence_summary": "장기 목표 ROE 15%, 주주환원율 50%, 자사주 매입·소각 비중 40%; 2026년까지 ROE 13% 이상, 주주환원율 45%, PBR 1배까지 지속 추진.", "evidence_url": "https://www.jbfg.com/ko/prcenter/press/detail/1144.do", "rule_read": "high_roe_target_plus_shareholder_return_formula", "entry_date": "2024-09-25", "entry_price": 15030.0, "MFE_30D_pct": 24.4844, "MAE_30D_pct": -1.3972, "peak_30D_date": "2024-10-25", "peak_30D_price": 18710.0, "trough_30D_date": "2024-10-02", "trough_30D_price": 14820.0, "MFE_90D_pct": 36.3939, "MAE_90D_pct": -1.3972, "peak_90D_date": "2024-12-03", "peak_90D_price": 20500.0, "trough_90D_date": "2024-10-02", "trough_90D_price": 14820.0, "MFE_180D_pct": 48.3699, "MAE_180D_pct": -1.3972, "peak_180D_date": "2025-06-17", "peak_180D_price": 22300.0, "trough_180D_date": "2024-10-02", "trough_180D_price": 14820.0, "peak_date": "2025-06-17", "peak_price": 22300.0, "post_peak_low_180D": 20500.0, "drawdown_after_peak_180D_pct": -8.0717, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "selected_round": "R6", "selected_loop": 101, "fine_archetype_id": "mixed_C21_financial_roe_pbr_capital_return_quality_holdout", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": false, "residual_error_type": "none_or_minor"}
{"symbol": "024110", "name": "기업은행", "trigger_date": "2024-12-05", "trigger_type": "Stage3-Yellow", "case_role": "delayed_positive", "evidence_family": "policy_bank_roe10_payout40_quarterly_dividend_plan", "evidence_summary": "기업가치 제고 계획에서 ROE 10% 이상, 배당성향 40% 이상, PBR 1.0 목표와 분기배당 도입 추진 제시.", "evidence_url": "https://www.etnews.com/20241205000454", "rule_read": "payout_formula_present_but_policy_bank_cet1_execution_needed", "entry_date": "2024-12-06", "entry_price": 14600.0, "MFE_30D_pct": 1.9863, "MAE_30D_pct": -3.2192, "peak_30D_date": "2025-01-21", "peak_30D_price": 14890.0, "trough_30D_date": "2024-12-09", "trough_30D_price": 14130.0, "MFE_90D_pct": 8.6986, "MAE_90D_pct": -8.2877, "peak_90D_date": "2025-03-04", "peak_90D_price": 15870.0, "trough_90D_date": "2025-04-09", "trough_90D_price": 13390.0, "MFE_180D_pct": 53.4247, "MAE_180D_pct": -8.2877, "peak_180D_date": "2025-07-15", "peak_180D_price": 22400.0, "trough_180D_date": "2025-04-09", "trough_180D_price": 13390.0, "peak_date": "2025-07-15", "peak_price": 22400.0, "post_peak_low_180D": 18500.0, "drawdown_after_peak_180D_pct": -17.4107, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "selected_round": "R6", "selected_loop": 101, "fine_archetype_id": "mixed_C21_financial_roe_pbr_capital_return_quality_holdout", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "residual_error_type": "too_late_if_waits_for_execution_only"}
{"symbol": "138930", "name": "BNK금융지주", "trigger_date": "2024-08-01", "trigger_type": "Stage2-Actionable", "case_role": "counterexample_with_4b_watch", "evidence_family": "q2_profit_cet1_buyback_cancel_asset_quality_risk", "evidence_summary": "2Q24 순이익 증가와 CET1 개선, 자사주 소각·중간배당·하반기 200억원 매입소각 계획이 있었지만 고정이하여신비율·연체율 상승이 병존.", "evidence_url": "https://www.bnkfg.com/02/03.jsp?dataPageNo=8&dataSeqNo=6531&dataWhere=", "rule_read": "capital_return_present_but_asset_quality_overhang_blocks_green", "entry_date": "2024-08-02", "entry_price": 9440.0, "MFE_30D_pct": 9.5339, "MAE_30D_pct": -8.8983, "peak_30D_date": "2024-08-26", "peak_30D_price": 10340.0, "trough_30D_date": "2024-08-05", "trough_30D_price": 8600.0, "MFE_90D_pct": 26.0593, "MAE_90D_pct": -8.8983, "peak_90D_date": "2024-12-03", "peak_90D_price": 11900.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 8600.0, "MFE_180D_pct": 30.2966, "MAE_180D_pct": -8.8983, "peak_180D_date": "2025-01-31", "peak_180D_price": 12300.0, "trough_180D_date": "2024-08-05", "trough_180D_price": 8600.0, "peak_date": "2025-01-31", "peak_price": 12300.0, "post_peak_low_180D": 9260.0, "drawdown_after_peak_180D_pct": -24.7154, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "selected_round": "R6", "selected_loop": 101, "fine_archetype_id": "mixed_C21_financial_roe_pbr_capital_return_quality_holdout", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "residual_error_type": "false_positive_if_capital_return_ignores_asset_quality"}
{"symbol": "039490", "name": "키움증권", "trigger_date": "2024-05-28", "trigger_type": "Stage2-Actionable", "case_role": "counterexample_delayed_execution", "evidence_family": "first_valueup_roe15_return30_pbr1_buyback_cancel", "evidence_summary": "상장사 최초 기업가치 제고 계획. ROE 15%, 주주환원율 30%, PBR 1배 이상 목표와 자사주 소각이 제시됐으나 180D 가격경로는 즉시 Green보다 실행 확인 대기 성격.", "evidence_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240528000399&langTpCd=0&method=search&orgid=G&rcpno=20240528000399&tran=Y", "rule_read": "excellent_plan_but_entry_window_needs_execution_confirmation", "entry_date": "2024-05-29", "entry_price": 129500.0, "MFE_30D_pct": 8.417, "MAE_30D_pct": -7.7992, "peak_30D_date": "2024-07-10", "peak_30D_price": 140400.0, "trough_30D_date": "2024-06-18", "trough_30D_price": 119400.0, "MFE_90D_pct": 13.0502, "MAE_90D_pct": -11.0425, "peak_90D_date": "2024-07-16", "peak_90D_price": 146400.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 115200.0, "MFE_180D_pct": 13.0502, "MAE_180D_pct": -14.6718, "peak_180D_date": "2024-07-16", "peak_180D_price": 146400.0, "trough_180D_date": "2024-12-09", "trough_180D_price": 110500.0, "peak_date": "2024-07-16", "peak_price": 146400.0, "post_peak_low_180D": 110500.0, "drawdown_after_peak_180D_pct": -24.5219, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "selected_round": "R6", "selected_loop": 101, "fine_archetype_id": "mixed_C21_financial_roe_pbr_capital_return_quality_holdout", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "residual_error_type": "false_positive_if_plan_equals_execution"}
{"symbol": "071050", "name": "한국금융지주", "trigger_date": "2025-05-26", "trigger_type": "Stage3-Yellow", "case_role": "positive_capital_return_absence_counterexample", "evidence_family": "roe15_growth_valueup_without_explicit_buyback", "evidence_summary": "2030년 ROE 15% 이상·자기자본 15조원 목표. 자사주 매입·소각 또는 주주환원율 수치를 명확히 제시하지 않았지만 ROE growth route가 가격경로를 열었다.", "evidence_url": "https://news.bizwatch.co.kr/article/market/2025/05/27/0006", "rule_read": "high_roe_growth_can_rerate_even_without_buyback_but_green_requires_payout_or_repeat_eps", "entry_date": "2025-05-27", "entry_price": 100200.0, "MFE_30D_pct": 51.996, "MAE_30D_pct": -2.0958, "peak_30D_date": "2025-07-09", "peak_30D_price": 152300.0, "trough_30D_date": "2025-05-27", "trough_30D_price": 98100.0, "MFE_90D_pct": 63.6727, "MAE_90D_pct": -2.0958, "peak_90D_date": "2025-07-14", "peak_90D_price": 164000.0, "trough_90D_date": "2025-05-27", "trough_90D_price": 98100.0, "MFE_180D_pct": 197.4052, "MAE_180D_pct": -2.0958, "peak_180D_date": "2026-02-20", "peak_180D_price": 298000.0, "trough_180D_date": "2025-05-27", "trough_180D_price": 98100.0, "peak_date": "2026-02-20", "peak_price": 298000.0, "post_peak_low_180D": 279500.0, "drawdown_after_peak_180D_pct": -6.2081, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "selected_round": "R6", "selected_loop": 101, "fine_archetype_id": "mixed_C21_financial_roe_pbr_capital_return_quality_holdout", "calibration_usable": true, "corporate_action_contaminated_180D_window": false, "source_proxy_only": false, "evidence_url_pending": false, "current_profile_error": true, "residual_error_type": "too_late_if_buyback_required_for_all_C21"}
```

## 7. Machine-readable score simulation JSONL

```jsonl
{"symbol": "138040", "name": "메리츠금융지주", "case_role": "positive", "raw_component_score_breakdown": {"eps_profitability": 14, "visibility": 19, "bottleneck_pricing": 3, "mispricing": 14, "valuation_rerating": 23, "capital_allocation": 15, "information_confidence": 5}, "simulated_total_score": 93, "current_profile_risk": "acceptable", "suggested_stage_after_shadow_rule": "Stage3-Green"}
{"symbol": "175330", "name": "JB금융지주", "case_role": "positive", "raw_component_score_breakdown": {"eps_profitability": 14, "visibility": 19, "bottleneck_pricing": 3, "mispricing": 14, "valuation_rerating": 23, "capital_allocation": 15, "information_confidence": 5}, "simulated_total_score": 93, "current_profile_risk": "acceptable", "suggested_stage_after_shadow_rule": "Stage3-Green"}
{"symbol": "024110", "name": "기업은행", "case_role": "delayed_positive", "raw_component_score_breakdown": {"eps_profitability": 12, "visibility": 17, "bottleneck_pricing": 2, "mispricing": 12, "valuation_rerating": 20, "capital_allocation": 13, "information_confidence": 5}, "simulated_total_score": 81, "current_profile_risk": "acceptable", "suggested_stage_after_shadow_rule": "Stage3-Yellow"}
{"symbol": "138930", "name": "BNK금융지주", "case_role": "counterexample_with_4b_watch", "raw_component_score_breakdown": {"eps_profitability": 10, "visibility": 13, "bottleneck_pricing": 1, "mispricing": 11, "valuation_rerating": 15, "capital_allocation": 10, "information_confidence": 4}, "simulated_total_score": 64, "current_profile_risk": "over_green", "suggested_stage_after_shadow_rule": "Stage2-Watch_with_local_4B_cap"}
{"symbol": "039490", "name": "키움증권", "case_role": "counterexample_delayed_execution", "raw_component_score_breakdown": {"eps_profitability": 11, "visibility": 14, "bottleneck_pricing": 2, "mispricing": 10, "valuation_rerating": 16, "capital_allocation": 12, "information_confidence": 5}, "simulated_total_score": 70, "current_profile_risk": "over_green", "suggested_stage_after_shadow_rule": "Stage2-Watch_with_local_4B_cap"}
{"symbol": "071050", "name": "한국금융지주", "case_role": "positive_capital_return_absence_counterexample", "raw_component_score_breakdown": {"eps_profitability": 15, "visibility": 18, "bottleneck_pricing": 2, "mispricing": 14, "valuation_rerating": 20, "capital_allocation": 7, "information_confidence": 5}, "simulated_total_score": 81, "current_profile_risk": "over_green", "suggested_stage_after_shadow_rule": "Stage3-Yellow"}
```

## 8. Aggregate and residual contribution

```json
{
  "row_count": 6,
  "positive_case_count": 4,
  "counterexample_count": 3,
  "local_4b_watch_count": 4,
  "avg_MFE_180D_pct": 65.8841,
  "avg_MAE_180D_pct": -7.8702,
  "median_MFE_180D_pct": 50.5639,
  "median_MAE_180D_pct": -8.593,
  "rows_with_MFE180_ge_30": 5,
  "rows_with_MAE90_le_minus_10": 2
}
```

### Residual error found

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN should not be a one-factor low-PBR/value-up headline rule.
The residual error is a split problem:
1. Over-Green risk: value-up plan or buyback/cancel headline is not enough if asset-quality, policy-bank, or brokerage-cycle volatility is unresolved.
2. Too-late risk: explicit buyback/cancel should not be mandatory for all C21 rows if ROE growth and earnings compounding are already visible.
```

## 9. Shadow rule candidate

```text
C21_ROE_PBR_CAPITAL_RETURN_REQUIRES_CAPITAL_RETURN_FORMULA_OR_HIGH_ROE_GROWTH_BRIDGE_WITH_ASSET_QUALITY_AND_EXECUTION_4B_CAP
```

### Proposed gate

```text
For C21 Stage3-Yellow:
- require at least two of:
  1. ROE target or realized ROE improvement above sector cost-of-equity threshold,
  2. explicit shareholder-return formula: payout, buyback/cancel, or total shareholder return ratio,
  3. CET1/capital-ratio runway or capital-light ROE expansion route,
  4. valuation/PBR discount explicitly linked to capital allocation or ROE spread,
  5. repeat EPS/earnings visibility.

For C21 Stage3-Green:
- require either:
  A. explicit shareholder-return execution + ROE/CET1 support + low asset-quality red flag, or
  B. high-ROE growth compounding + repeat earnings delivery + low leverage/trust red flag.

Apply local 4B cap when:
- plan exists but execution is not yet confirmed,
- NPL/delinquency/credit-cost deterioration offsets capital return,
- post-peak drawdown exceeds -15% inside the 180D window,
- shareholder return is present but ROE route is cyclical or brokerage-beta heavy.
```

## 10. Existing axis strengthened / weakened

```yaml
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened:
  - none
new_axis_proposed:
  - C21_ROE_PBR_CAPITAL_RETURN_SPLIT_BANK_CAPITAL_RETURN_VS_BROKERAGE_ROE_GROWTH
```

## 11. Validation scope

```yaml
validation_scope:
  included_symbols: ['138040','175330','024110','138930','039490','071050']
  excluded_top_covered_static_C21_symbols: ['105560','055550','316140','005940','005830','006800']
  trigger_window_basis: next tradable date after evidence trigger
  forward_windows: [30D, 90D, 180D]
  price_source: Songdaiki/stock-web tradable shards
  corporate_action_policy: profile candidate overlap in entry~D+180 blocks calibration usability
  screened_corporate_action_contaminated_candidates: []
  insufficient_forward_window_rows: 0
  calibration_usable_rows: 6
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later coding-agent session. Do not treat this Markdown as an already-approved production patch.
Ingest this file only through the V12 batch calibration path.
Validate every JSONL trigger row for required fields:
- selected_round
- selected_loop
- large_sector_id
- canonical_archetype_id
- symbol
- trigger_type
- entry_date
- entry_price
- MFE_30D_pct / MAE_30D_pct
- MFE_90D_pct / MAE_90D_pct
- MFE_180D_pct / MAE_180D_pct
Reject any row if corporate action candidate overlaps entry_date through D+180 in Stock-Web profiles.
If accepted, evaluate the shadow rule candidate:
C21_ROE_PBR_CAPITAL_RETURN_REQUIRES_CAPITAL_RETURN_FORMULA_OR_HIGH_ROE_GROWTH_BRIDGE_WITH_ASSET_QUALITY_AND_EXECUTION_4B_CAP
as a C21-local rule candidate only. Do not apply a global patch without comparing against existing C21 rows.
```

## 13. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 14. Next research state

```yaml
completed_round: R6
completed_loop: 101
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 C21 quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_holdout_only_if_new_capital_return_or_ROE_growth_path
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_quality_holdout
```
