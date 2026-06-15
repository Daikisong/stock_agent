# E2R v12 Residual Research — R6 / L6 / C21 FINANCIAL_ROE_PBR_CAPITAL_RETURN / loop 190

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R6
selected_loop = 190
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = mixed_c21_regional_bank_brokerage_digital_bank_valueup_leaf_set
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
live_candidate_mode = false
current_stock_discovery_allowed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
output_filename = e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

## 1. Selection / no-repeat rationale

원본 No-Repeat Index에서 C21은 79 rows인 Priority 2 품질보강 구역이다. 이번 세션에서는 loop169에서 하나금융지주·키움증권·메리츠금융지주를 이미 다뤘으므로, loop190은 같은 C21 안에서도 **regional bank / state bank / brokerage / digital bank boundary**를 보강한다.

이번 연구의 질문은 “한국 금융주는 저PBR인가?”가 아니다. 더 좁게, **저PBR·밸류업·record profit이라는 단어가 실제 C21 Stage2-Actionable로 올라가려면 어떤 돈길이 필요하냐**를 본다. C21에서 돈길은 대체로 다음 네 갈래다.

1. 자사주 매입·소각 또는 명확한 주주환원율 목표
2. CET1/RWA discipline과 배당 지속성
3. realized ROE/profit bridge
4. brokerage/holding-company cycle이 C21 자본환원으로 오염되는지 여부

```text
index_baseline_coverage_before = C21 rows 79
index_baseline_coverage_after_if_accepted = C21 rows 89
session_aware_after_loop169_loop190_if_accepted = about C21 rows 98
new_independent_case_count = 10
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 10
calibration_usable_case_count = 10
calibration_usable_trigger_count = 10
representative_trigger_count = 10
positive_case_count = 6
counterexample_count = 4
4B_watch_or_high_MAE_guard_count = 7
current_profile_error_count = 9
```

## 2. Price atlas validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
entry_price_rule = entry_date close c
MFE_MAE_rule = entry 이후 N개 tradable row 안의 max high / min low vs entry_price
forward_window_required = 180 tradable rows
manifest_after_date_prices_fabricated = false
```

All selected rows have 30D/90D/180D MFE·MAE fields and no detected 180D split-like price discontinuity in the local stock-web shards. Treasury-share count effects are treated as fundamental capital-return evidence, not an OHLC adjustment issue.

## 3. Case table

| case | symbol | trigger | label | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---|---:|---|---|---:|---:|---:|---|
| C21_L190_001_JBFG_2Q24_BUYBACK_CANCEL_EXECUTION | 175330 | Stage2-Actionable / 2024-08-06 | positive | 16.16 / -2.46 | 52.64 / -2.46 | 52.64 / -2.46 | capital-return bridge worked |
| C21_L190_002_JBFG_VALUEUP_DISCLOSURE_CONFIRMED_RETURN | 175330 | Stage2-Actionable / 2024-09-25 | positive | 24.48 / -1.40 | 36.39 / -1.40 | 48.37 / -1.40 | capital-return bridge worked |
| C21_L190_003_BNK_Q3_VALUEUP_RETURN_BRIDGE | 138930 | Stage2-Actionable / 2024-10-31 | positive | 26.06 / -2.01 | 30.30 / -2.01 | 70.02 / -2.01 | capital-return bridge worked |
| C21_L190_004_BNK_FY24_STAGED_RETURN_HIGH_MAE | 138930 | Stage2-Watch / 2025-02-10 | delayed_positive | 3.90 / -12.55 | 7.88 / -19.83 | 38.96 / -19.83 | bridge worked but staged entry was required |
| C21_L190_005_DGB_EXEC_BUYBACK_LOW_PBR_BUT_CAPITAL_NEED | 139130 | Stage2-Watch / 2024-06-10 | counterexample | 2.85 / -3.85 | 5.83 / -7.69 | 21.84 / -7.69 | non-price evidence existed but was the wrong C21 bridge |
| C21_L190_006_DGB_2Q24_RETURN_NOT_FEASIBLE_UNTIL_2027 | 139130 | Stage2-FalsePositive / 2024-07-31 | counterexample | 4.66 / -8.71 | 14.60 / -8.71 | 26.26 / -8.71 | non-price evidence existed but was the wrong C21 bridge |
| C21_L190_007_IBK_DIVIDEND_PAYOUT_STATE_BANK_LOW_ALPHA | 024110 | Stage2-Watch / 2024-02-08 | low_alpha_counterexample | 19.39 / -3.65 | 19.39 / -6.71 | 19.39 / -6.71 | dividend-yield only was capped |
| C21_L190_008_KIH_FY24_EARNINGS_DIVIDEND_REPRICING | 071050 | Stage2-Watch / 2025-03-04 | delayed_positive | 3.44 / -14.55 | 116.93 / -14.55 | 147.88 / -14.55 | bridge worked but staged entry was required |
| C21_L190_009_SAMSUNG_SECURITIES_Q1_EARNINGS_BROKERAGE_ROE | 016360 | Stage2-Actionable / 2024-05-16 | positive_with_staged_entry_guard | 2.71 / -8.12 | 26.03 / -8.12 | 30.67 / -8.12 | positive, but not Green without entry guard |
| C21_L190_010_KAKAOBANK_RECORD_PROFIT_NO_RETURN_BRIDGE | 323410 | Stage2-FalsePositive / 2024-05-08 | counterexample | 0.59 / -18.75 | 0.59 / -27.77 | 0.59 / -27.77 | non-price evidence existed but was the wrong C21 bridge |

## 4. Evidence notes by case

### 4.1 JB금융지주 — execution-positive pair

- `C21_L190_001`: 2Q24 이후 value-up·주주환원 실행 기대가 단순 저PBR을 넘어섰다. 90D MFE `52.64%`, 90D MAE `-2.46%`로 C21 positive다.
- `C21_L190_002`: 2024-09-24 공식 value-up disclosure와 50% 주주환원 목표, 자사주 소각 체계가 붙었다. 180D MAE가 `-1.40%`에 그쳐 Stage2-Actionable evidence로 좋다.
- 압축 rule: **regional bank라도 주주환원 계획이 buyback/cancellation과 ROE target으로 명문화되면 C21 Stage2-Actionable을 허용한다.**

### 4.2 BNK금융지주 — return surprise positive, late follow-through guard

- `C21_L190_003`: Q3 2024에서 주주환원 확대 가능성이 기대 이상으로 인식되며 180D MFE `70.02%`, MAE `-2.01%`를 보였다.
- `C21_L190_004`: FY24/value-up follow-through는 맞았지만 90D MFE `7.88%`, MAE `-19.83%`로 초기 진입은 나빴다. 같은 C21 positive라도 late follow-through는 Stage2-Watch + staged-entry guard가 필요하다.

### 4.3 DGB/iM금융지주 — low-PBR and executive-buyback are not enough

- `C21_L190_005`: 임원 자사주 매입과 저PBR narrative는 있었지만 PF 부담과 자본 repair가 남아 있었다. 90D MFE `5.83%`로 Actionable evidence가 약했다.
- `C21_L190_006`: 2Q24 이후에도 CET1/주주환원 확대 타이밍이 불확실했다. MFE180은 `26.26%`였지만 90D는 `14.60%`에 그쳐 delayed-watch로 보는 편이 안전하다.

### 4.4 기업은행 — dividend-yield low-alpha counterexample

- `C21_L190_007`: 고배당 매력은 있지만 국책은행 성격상 buyback/cancellation leverage가 약했다. 30/90/180D MFE가 모두 `19.39%`로 capped되어, dividend yield만으로 C21 Stage2-Actionable을 주면 과잉이다.

### 4.5 한국금융지주·삼성증권·카카오뱅크 — brokerage/digital-bank boundary

- `C21_L190_008`: 한국금융지주는 FY2024 이익·배당 회복 뒤 큰 MFE가 나왔지만, formal capital-return policy보다는 brokerage/IB cycle recovery 성격이 강하다. C21이 아니라 brokerage-cycle watch로 시작하는 게 더 정확하다.
- `C21_L190_009`: 삼성증권은 Q1 2024 안정적 이익과 brokerage ROE bridge가 확인됐다. 90D MFE `26.03%`라 Stage2-Actionable은 가능하지만, 30D MFE가 낮아 Green은 아니다.
- `C21_L190_010`: 카카오뱅크는 record profit에도 buyback/cancellation·CET1 기반 capital return bridge가 약했고, 90D MAE `-27.77%`로 clean false positive다.

## 5. Score / return alignment summary

```text
usable_trigger_row_count = 10
avg_MFE_90D_pct = 31.06
avg_MAE_90D_pct = -9.93
positive_case_count = 6
counterexample_count = 4
current_profile_error_count = 9
```

C21의 residual error는 “비가격 증거가 있느냐”가 아니라 **그 비가격 증거가 capital-return value capture인지**다. 저PBR, record profit, dividend yield, value-up vocabulary는 모두 불씨처럼 보이지만, 장작이 다르다. 자사주 소각·CET1·ROE·배당정책으로 산소가 연결된 불은 Stage2로 키워도 되지만, 단순 record profit이나 배당수익률만 있는 불씨는 금방 꺼질 수 있다.

## 6. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_001_JBFG_2Q24_BUYBACK_CANCEL_EXECUTION", "symbol": "175330", "company": "JB금융지주", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_BUYBACK_CANCELLATION_EXECUTION", "trigger_date": "2024-08-06", "entry_date": "2024-08-06", "entry_price": 13430, "trigger_type": "Stage2-Actionable", "case_label": "positive", "proposed_stage": "Stage2-Actionable", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/175/175330/<year>.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.16, "MAE_30D_pct": -2.46, "MFE_90D_pct": 52.64, "MAE_90D_pct": -2.46, "MFE_180D_pct": 52.64, "MAE_180D_pct": -2.46, "peak_180D_date": "2024-12-03", "peak_180D_price": 20500, "trough_180D_date": "2024-08-07", "trough_180D_price": 13100, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "2q24_buyback_cancellation_execution_and_roe_shareholder_return_bridge", "evidence_summary": "2Q24 실적 이후 주주환원 확대 기대와 자사주 매입·소각 실행 다리가 확인된 케이스. 단순 저PBR이 아니라 ROE/주주환원 실행이 붙었고, 90D MFE가 50%를 넘으면서 C21 positive로 작동했다.", "evidence_urls": ["https://www.jbfg.com/en/ir/value.do", "https://securities.miraeasset.com/bbs/download/2130331.pdf?attachmentId=2130331"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 18, "earnings_visibility": 22, "bottleneck_or_structural_edge": 5, "market_mispricing": 16, "valuation_rerating": 24, "capital_allocation": 18, "information_confidence": 8, "total": 111}, "current_profile_error_type": "too_conservative_if_regional_bank_execution_is_treated_as_generic_low_pbr", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|175330|Stage2-Actionable|2024-08-06", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_002_JBFG_VALUEUP_DISCLOSURE_CONFIRMED_RETURN", "symbol": "175330", "company": "JB금융지주", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_OFFICIAL_VALUEUP_PLAN_RETURN50_TREASURY_RETIREMENT", "trigger_date": "2024-09-24", "entry_date": "2024-09-25", "entry_price": 15030, "trigger_type": "Stage2-Actionable", "case_label": "positive", "proposed_stage": "Stage2-Actionable", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/175/175330/<year>.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.48, "MAE_30D_pct": -1.4, "MFE_90D_pct": 36.39, "MAE_90D_pct": -1.4, "MFE_180D_pct": 48.37, "MAE_180D_pct": -1.4, "peak_180D_date": "2025-06-17", "peak_180D_price": 22300, "trough_180D_date": "2024-10-02", "trough_180D_price": 14820, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "official_value_up_disclosure_return50_buyback_cancellation_policy", "evidence_summary": "공식 value-up disclosure에서 50% 주주환원 목표와 자사주 취득·소각 체계가 제시됐다. shallow MAE와 높은 MFE가 같이 나타난 깨끗한 C21 evidence bridge다.", "evidence_urls": ["https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20240924800069", "https://www.koreatimes.co.kr/business/banking-finance/20240924/jb-financial-unveils-long-term-measures-to-improve-corporate-governance"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 18, "earnings_visibility": 24, "bottleneck_or_structural_edge": 5, "market_mispricing": 16, "valuation_rerating": 25, "capital_allocation": 20, "information_confidence": 9, "total": 117}, "current_profile_error_type": "none_or_mild_too_late_if_waiting_for_pbr_one_after_return_policy_is_binding", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|175330|Stage2-Actionable|2024-09-25", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_003_BNK_Q3_VALUEUP_RETURN_BRIDGE", "symbol": "138930", "company": "BNK금융지주", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_RETURN_SURPRISE_WITH_SHALLOW_MAE", "trigger_date": "2024-10-31", "entry_date": "2024-10-31", "entry_price": 9440, "trigger_type": "Stage2-Actionable", "case_label": "positive", "proposed_stage": "Stage2-Actionable", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/138/138930/<year>.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.06, "MAE_30D_pct": -2.01, "MFE_90D_pct": 30.3, "MAE_90D_pct": -2.01, "MFE_180D_pct": 70.02, "MAE_180D_pct": -2.01, "peak_180D_date": "2025-07-15", "peak_180D_price": 16050, "trough_180D_date": "2024-11-18", "trough_180D_price": 9250, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "q3_valueup_shareholder_return_plan_exceeding_expectations", "evidence_summary": "Q3 실적 자체는 완벽하지 않았지만, 주주환원 확대 가능성이 시장 기대를 넘어섰고 entry 후 MAE가 얕았다. C21은 이처럼 실적 beat보다 capital-return surprise가 더 중요한 경우가 있다.", "evidence_urls": ["https://www.asiae.co.kr/en/article/2024103107465277779", "https://eng.bnkfg.com/02/01.jsp"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 17, "earnings_visibility": 21, "bottleneck_or_structural_edge": 5, "market_mispricing": 15, "valuation_rerating": 24, "capital_allocation": 18, "information_confidence": 8, "total": 108}, "current_profile_error_type": "too_late_if_profile_waits_for_clean_earnings_beat_and_underweights_return_surprise", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|138930|Stage2-Actionable|2024-10-31", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_004_BNK_FY24_STAGED_RETURN_HIGH_MAE", "symbol": "138930", "company": "BNK금융지주", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_FY24_RETURN_FOLLOWTHROUGH_WITH_HIGH_MAE_GUARD", "trigger_date": "2025-02-07", "entry_date": "2025-02-10", "entry_price": 11550, "trigger_type": "Stage2-Watch", "case_label": "delayed_positive", "proposed_stage": "Stage2-Watch + staged-entry guard", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/138/138930/<year>.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.9, "MAE_30D_pct": -12.55, "MFE_90D_pct": 7.88, "MAE_90D_pct": -19.83, "MFE_180D_pct": 38.96, "MAE_180D_pct": -19.83, "peak_180D_date": "2025-07-15", "peak_180D_price": 16050, "trough_180D_date": "2025-04-09", "trough_180D_price": 9260, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "fy2024_valueup_followthrough_but_bad_initial_entry_path", "evidence_summary": "FY2024/value-up follow-through는 살아 있었지만, 90D 구간에서 MFE가 낮고 MAE가 깊었다. bridge는 맞아도 Stage2-Actionable 즉시 승격보다 staged-entry가 맞는 케이스다.", "evidence_urls": ["https://www.koreatimes.co.kr/business/banking-finance/20250312/why-foreign-investors-increase-stakes-in-bnk-financial", "https://eng.bnkfg.com/02/01.jsp"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 15, "earnings_visibility": 20, "bottleneck_or_structural_edge": 5, "market_mispricing": 14, "valuation_rerating": 22, "capital_allocation": 16, "information_confidence": 8, "total": 100}, "current_profile_error_type": "overconfident_if_positive_return_plan_is_promoted_without_mae_guard", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|138930|Stage2-Watch|2025-02-10", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_005_DGB_EXEC_BUYBACK_LOW_PBR_BUT_CAPITAL_NEED", "symbol": "139130", "company": "iM금융지주/DGB금융지주", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_LOW_PBR_EXEC_BUYBACK_CAPITAL_NEED_COUNTEREXAMPLE", "trigger_date": "2024-06-06", "entry_date": "2024-06-10", "entry_price": 8060, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "proposed_stage": "Stage2-Watch only", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/139/139130/<year>.csv", "profile_path": "atlas/symbol_profiles/139/139130.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.85, "MAE_30D_pct": -3.85, "MFE_90D_pct": 5.83, "MAE_90D_pct": -7.69, "MFE_180D_pct": 21.84, "MAE_180D_pct": -7.69, "peak_180D_date": "2025-02-18", "peak_180D_price": 9820, "trough_180D_date": "2024-08-05", "trough_180D_price": 7440, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "executive_stock_buybacks_low_pbr_but_capital_and_pf_pressure", "evidence_summary": "임원 자사주 매입과 저PBR narrative는 있었지만 PF 부담과 자본비율 개선 필요성이 커서 주주환원 확대 visibility가 약했다. 90D MFE도 낮아 Actionable 오발 반례다.", "evidence_urls": ["https://www.koreatimes.co.kr/economy/20240606/dgb-financial-head-leads-exec-stock-buybacks-investor-relations-to-bolster-corporate-value", "https://www.imfngroup.com/main.fg"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 12, "earnings_visibility": 16, "bottleneck_or_structural_edge": 5, "market_mispricing": 15, "valuation_rerating": 19, "capital_allocation": 8, "information_confidence": 9, "total": 84}, "current_profile_error_type": "false_positive_if_exec_buyback_is_treated_as_full_shareholder_return_execution", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|139130|Stage2-Watch|2024-06-10", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_006_DGB_2Q24_RETURN_NOT_FEASIBLE_UNTIL_2027", "symbol": "139130", "company": "iM금융지주/DGB금융지주", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_PF_PROVISION_CAPITAL_RETURN_DELAY_COUNTEREXAMPLE", "trigger_date": "2024-07-30", "entry_date": "2024-07-31", "entry_price": 8150, "trigger_type": "Stage2-FalsePositive", "case_label": "counterexample", "proposed_stage": "Stage2-FalsePositive / no Actionable", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/139/139130/<year>.csv", "profile_path": "atlas/symbol_profiles/139/139130.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.66, "MAE_30D_pct": -8.71, "MFE_90D_pct": 14.6, "MAE_90D_pct": -8.71, "MFE_180D_pct": 26.26, "MAE_180D_pct": -8.71, "peak_180D_date": "2025-04-30", "peak_180D_price": 10290, "trough_180D_date": "2024-08-05", "trough_180D_price": 7440, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "2q24_disappointing_results_pf_provisions_cet1_shareholder_return_delay", "evidence_summary": "2Q24 이후 PF 충당금과 자본목표 부담이 남아, 주주환원 확대를 곧바로 Stage2-Actionable로 보기 어려웠다. MFE180은 있었지만 90D가 약해 delayed watch가 맞다.", "evidence_urls": ["https://biz.chosun.com/en/en-finance/2025/02/07/5YL7PBRTBFAXXC3JV625YK4FCI/", "https://securities.miraeasset.com/bbs/download/2130147.pdf?attachmentId=2130147"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 11, "earnings_visibility": 15, "bottleneck_or_structural_edge": 5, "market_mispricing": 14, "valuation_rerating": 18, "capital_allocation": 7, "information_confidence": 10, "total": 80}, "current_profile_error_type": "false_positive_if_generic_valueup_vocabulary_ignores_capital_repair_timing", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|139130|Stage2-FalsePositive|2024-07-31", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_007_IBK_DIVIDEND_PAYOUT_STATE_BANK_LOW_ALPHA", "symbol": "024110", "company": "기업은행", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "STATE_BANK_DIVIDEND_YIELD_LOW_ALPHA_NO_BUYBACK_LEVERAGE", "trigger_date": "2024-02-08", "entry_date": "2024-02-08", "entry_price": 13410, "trigger_type": "Stage2-Watch", "case_label": "low_alpha_counterexample", "proposed_stage": "Stage2-Watch / dividend-yield only cap", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/024/024110/<year>.csv", "profile_path": "atlas/symbol_profiles/024/024110.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.39, "MAE_30D_pct": -3.65, "MFE_90D_pct": 19.39, "MAE_90D_pct": -6.71, "MFE_180D_pct": 19.39, "MAE_180D_pct": -6.71, "peak_180D_date": "2024-03-15", "peak_180D_price": 16010, "trough_180D_date": "2024-04-15", "trough_180D_price": 12510, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "state_bank_dividend_payout_without_buyback_cancellation_leverage", "evidence_summary": "배당 매력은 있었지만 자사주 소각·PBR 재평가 leverage가 약한 국책은행 성격이 컸다. MFE180이 20%에 못 미쳐 C21에서 dividend-yield만으로 Actionable을 주면 안 되는 low-alpha 반례다.", "evidence_urls": ["https://global.ibk.co.kr/en/investor/ShareholderReturn"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 13, "earnings_visibility": 18, "bottleneck_or_structural_edge": 5, "market_mispricing": 13, "valuation_rerating": 22, "capital_allocation": 12, "information_confidence": 8, "total": 91}, "current_profile_error_type": "false_positive_if_dividend_yield_is_equated_with_capital_return_rerating", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|024110|Stage2-Watch|2024-02-08", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_008_KIH_FY24_EARNINGS_DIVIDEND_REPRICING", "symbol": "071050", "company": "한국금융지주", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_HOLDING_EARNINGS_DIVIDEND_REPRICING_BUT_NOT_PURE_VALUEUP", "trigger_date": "2025-03-04", "entry_date": "2025-03-04", "entry_price": 75600, "trigger_type": "Stage2-Watch", "case_label": "delayed_positive", "proposed_stage": "Stage2-Watch -> upgrade only after realized earnings/dividend confirmation", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/071/071050/<year>.csv", "profile_path": "atlas/symbol_profiles/071/071050.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.44, "MAE_30D_pct": -14.55, "MFE_90D_pct": 116.93, "MAE_90D_pct": -14.55, "MFE_180D_pct": 147.88, "MAE_180D_pct": -14.55, "peak_180D_date": "2025-10-31", "peak_180D_price": 187400, "trough_180D_date": "2025-04-09", "trough_180D_price": 64600, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "fy2024_earnings_dividend_recovery_without_formal_shareholder_return_policy", "evidence_summary": "FY2024 이익·DPS 회복은 매우 강한 가격경로로 이어졌지만, formal shareholder return policy가 아니라 brokerage/IB cycle 회복 성격이 섞였다. C21에서는 Stage2-Watch 후 realized earnings bridge로 업그레이드하는 게 더 안전하다.", "evidence_urls": ["https://www.koreaholdings.com/en/manage/capital", "https://www.koreainvestment.com/en/sub/vision_report"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 20, "earnings_visibility": 21, "bottleneck_or_structural_edge": 5, "market_mispricing": 16, "valuation_rerating": 20, "capital_allocation": 12, "information_confidence": 8, "total": 102}, "current_profile_error_type": "classification_boundary_between_c21_capital_return_and_brokerage_cycle_recovery", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|071050|Stage2-Watch|2025-03-04", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_009_SAMSUNG_SECURITIES_Q1_EARNINGS_BROKERAGE_ROE", "symbol": "016360", "company": "삼성증권", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_REALIZED_ROE_EARNINGS_BRIDGE_WITH_STAGED_ENTRY", "trigger_date": "2024-05-14", "entry_date": "2024-05-16", "entry_price": 38800, "trigger_type": "Stage2-Actionable", "case_label": "positive_with_staged_entry_guard", "proposed_stage": "Stage2-Actionable + initial drawdown guard", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/016/016360/<year>.csv", "profile_path": "atlas/symbol_profiles/016/016360.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.71, "MAE_30D_pct": -8.12, "MFE_90D_pct": 26.03, "MAE_90D_pct": -8.12, "MFE_180D_pct": 30.67, "MAE_180D_pct": -8.12, "peak_180D_date": "2024-12-03", "peak_180D_price": 50700, "trough_180D_date": "2024-06-05", "trough_180D_price": 35650, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "q1_2024_operating_profit_net_profit_brokerage_roe_bridge", "evidence_summary": "Q1 2024 순이익·영업이익이 안정적으로 확인되며 brokerage ROE bridge가 붙었다. 단 30D 경로는 약했으므로 immediate Green이 아니라 Stage2-Actionable + entry guard가 맞다.", "evidence_urls": ["https://en.yna.co.kr/view/AEN20240514007300320", "https://www.samsungsecurities.com/eng/invest/overview.do"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 16, "earnings_visibility": 20, "bottleneck_or_structural_edge": 5, "market_mispricing": 13, "valuation_rerating": 20, "capital_allocation": 13, "information_confidence": 8, "total": 95}, "current_profile_error_type": "too_late_if_waiting_for_full_year_brokerage_roe_confirmation", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|016360|Stage2-Actionable|2024-05-16", "aggregate_include": true, "representative_for_aggregate": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md", "case_id": "C21_L190_010_KAKAOBANK_RECORD_PROFIT_NO_RETURN_BRIDGE", "symbol": "323410", "company": "카카오뱅크", "market": "KOSPI", "selected_round": "R6", "selected_loop": 190, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_RECORD_PROFIT_WITHOUT_CAPITAL_RETURN_BRIDGE_FALSE_POSITIVE", "trigger_date": "2024-05-08", "entry_date": "2024-05-08", "entry_price": 25600, "trigger_type": "Stage2-FalsePositive", "case_label": "counterexample", "proposed_stage": "Stage2-FalsePositive / no Actionable", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_shard": "atlas/ohlcv_tradable_by_symbol_year/323/323410/<year>.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.59, "MAE_30D_pct": -18.75, "MFE_90D_pct": 0.59, "MAE_90D_pct": -27.77, "MFE_180D_pct": 0.59, "MAE_180D_pct": -27.77, "peak_180D_date": "2024-05-09", "peak_180D_price": 25750, "trough_180D_date": "2024-08-05", "trough_180D_price": 18490, "forward_rows_available": ">=180", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "calibration_usable_reason": "complete_30_90_180_mfe_mae_from_stock_web_tradable_shards; no detected 180D split-like discontinuity", "evidence_family": "record_profit_platform_bank_without_buyback_cancellation_or_pbr_execution", "evidence_summary": "디지털은행의 record profit은 있었지만, C21이 요구하는 buyback/cancellation·CET1 기반 주주환원 실행 bridge가 약했다. 가격경로도 MFE가 거의 없고 MAE가 깊어 clean false positive다.", "evidence_urls": ["https://www.koreatimes.co.kr/business/banking-finance/20240807/kakaobank-achieves-historic-high-h1-net-profit", "https://www.kakaobank.com/view/report/archive/earnings?lang=EN"], "source_url_status": "verified_url_or_official_proxy_or_search_snippet", "raw_component_score_breakdown": {"eps_or_profit_power": 17, "earnings_visibility": 18, "bottleneck_or_structural_edge": 6, "market_mispricing": 10, "valuation_rerating": 12, "capital_allocation": 3, "information_confidence": 8, "total": 74}, "current_profile_error_type": "false_positive_if_record_profit_is_mapped_to_c21_without_shareholder_return_execution", "shadow_rule_effect": "c21_capital_return_bridge_gate_v2", "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|323410|Stage2-FalsePositive|2024-05-08", "aggregate_include": true, "representative_for_aggregate": true}
```

## 7. Aggregate row JSON

```json
{
  "row_type": "aggregate",
  "research_file": "e2r_stock_web_v12_residual_round_R6_loop_190_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md",
  "selected_round": "R6",
  "selected_loop": 190,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "usable_trigger_row_count": 10,
  "representative_trigger_count": 10,
  "positive_case_count": 6,
  "counterexample_count": 4,
  "stage4b_watch_or_high_mae_guard_count": 7,
  "current_profile_error_count": 9,
  "avg_MFE_90D_pct": 31.06,
  "avg_MAE_90D_pct": -9.93,
  "index_baseline_coverage_before": "C21 rows 79",
  "index_baseline_coverage_after_if_accepted": "C21 rows 89",
  "session_aware_after_loop169_loop190_if_accepted": "about C21 rows 98"
}
```

## 8. Score simulation / shadow rule rows JSONL

```jsonl
{"row_type": "score_simulation", "rule_id": "C21_REALIZED_CAPITAL_RETURN_CET1_AND_EARNINGS_QUALITY_GATE_V2", "scope": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "positive_unlock_condition": "explicit buyback/cancellation or shareholder-return target plus CET1/RWA or realized ROE/profit bridge", "watch_cap_condition": "value-up vocabulary, record profit, dividend yield, or executive stock purchase without capital-return execution bridge", "green_constraint": "do not loosen Stage3-Green; require low-MAE timing and cross-evidence conversion before Green", "expected_profile_effect": "reduce C21 false positives from record-profit/low-PBR vocabulary while preserving regional-bank value-up positives", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "shadow_weight", "rule_id": "C21_REALIZED_CAPITAL_RETURN_CET1_AND_EARNINGS_QUALITY_GATE_V2", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "proposed_delta": "stage2_required_bridge +1 for realized buyback/cancellation/CET1 bridge; cap generic dividend-yield and record-profit rows at Watch", "do_not_propose_new_weight_delta": false, "requires_batch_validation": true}
{"row_type": "residual_contribution", "residual_error_found": "C21 rows can have non-price evidence but still be wrong if the evidence is record profit, dividend yield, or low-PBR vocabulary without shareholder value-capture bridge", "cases_supporting_error": ["C21_L190_005_DGB_EXEC_BUYBACK_LOW_PBR_BUT_CAPITAL_NEED", "C21_L190_007_IBK_DIVIDEND_PAYOUT_STATE_BANK_LOW_ALPHA", "C21_L190_010_KAKAOBANK_RECORD_PROFIT_NO_RETURN_BRIDGE"], "cases_supporting_exception": ["C21_L190_002_JBFG_VALUEUP_DISCLOSURE_CONFIRMED_RETURN", "C21_L190_003_BNK_Q3_VALUEUP_RETURN_BRIDGE"]}
```

## 9. Shadow rule candidate

```text
rule_id = C21_REALIZED_CAPITAL_RETURN_CET1_AND_EARNINGS_QUALITY_GATE_V2
scope = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
production_scoring_changed = false
shadow_weight_only = true

IF evidence is low-PBR, value-up vocabulary, record profit, dividend yield, or executive stock buying only
  AND there is no realized buyback/cancellation, explicit payout trajectory, CET1/RWA discipline, or durable ROE bridge
THEN cap at Stage2-Watch and block Stage2-Actionable.

IF evidence includes explicit shareholder-return plan with buyback/cancellation or rising payout target
  AND CET1/RWA discipline or realized ROE/profit bridge is visible
  AND entry MAE90 is not severe
THEN allow Stage2-Actionable.

IF evidence is brokerage earnings recovery only
  AND no capital-return execution is visible
THEN treat as brokerage-cycle Stage2-Watch, not C21 capital-return rerating.

IF MFE180 is high but MFE90 is weak or MAE90 <= -15%
THEN keep staged-entry / delayed-positive label and avoid immediate Green.
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this in the research session. In a later coding session, ingest this Markdown with the rest of the v12 batch and evaluate whether `C21_REALIZED_CAPITAL_RETURN_CET1_AND_EARNINGS_QUALITY_GATE_V2` should become a scoped C21 Stage2 bridge guard. Check exact duplicate keys before promotion. Do not loosen Stage3-Green thresholds. Do not change production scoring unless the batch validator confirms representative rows and promotion decisions.

## 11. Final state

```text
completed_round = R6
completed_loop = 190
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
new_independent_case_count = 10
usable_trigger_row_count = 10
representative_trigger_count = 10
positive_case_count = 6
counterexample_count = 4
4B_watch_or_high_MAE_guard_count = 7
current_profile_error_count = 9
index_baseline_coverage_before = C21 rows 79
index_baseline_coverage_after_if_accepted = C21 rows 89
session_aware_after_loop169_loop190_if_accepted = about C21 rows 98
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA|C15_MATERIAL_SPREAD_SUPERCYCLE|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```
