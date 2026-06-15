# E2R v12 Historical Calibration — R6 / C21 Financial ROE·PBR Capital Return

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R6
selected_loop = 105
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_QUALITY_BRIDGE_VS_DIGITAL_BANK_HIGH_PBR_FALSE_POSITIVE
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection basis

`V12_Research_No_Repeat_Index.md` 기준으로 C21은 Priority 1의 마지막 부족축이다.

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN = 48 rows
need_to_50 = 2
selected_priority_bucket = Priority 1
round_sector_consistency = pass
```

이번 실행에서는 C21의 같은 테마라도 **저PBR/ROE/자본환원 bridge가 있는 금융지주**와 **디지털은행/고PBR 금융 라벨 false positive**를 분리한다.
중복 방지 기준은 `canonical_archetype_id + symbol + trigger_type + entry_date`이며, 이번 3개 case는 모두 새 symbol / 새 trigger family로 처리한다.

## 2. Source and validation scope

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

사용한 외부 trigger source는 2024-02-28 Reuters의 Korea Corporate Value-up Programme follow-up 보도다. 해당 보도는 상장사의 shareholder return 기준 미달 시 제재 검토, 저평가 업종인 banks/automakers의 동반 상승, 그리고 장기 reform effort를 언급한다.

```text
primary_external_trigger_url = https://www.reuters.com/markets/asia/skorea-considering-penalties-firms-failing-boost-shareholder-return-2024-02-28/
secondary_external_trigger_url = https://www.reuters.com/markets/asia/south-korea-regulator-speed-up-corporate-reforms-eyes-bold-measures-2024-03-14/
company_level_capital_return_url_repair_needed = true
```

주의: 이번 MD는 live 후보 탐색이 아니라 historical calibration이다. `stock_agent` 코드/production scoring은 열람하거나 수정하지 않았다.

## 3. Case table

| case_id | ticker | name | trigger | entry | peak | trough | MFE | MAE | classification |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| C21_KBFG_2024_VALUEUP_CAPITAL_RETURN_BRIDGE | 105560 | KB금융 | 2024-02-28 value-up / bank shareholder-return repricing | 2024-02-29 @ 63,500 | 2024-10-25 @ 103,900 | 2024-04-19 @ 62,000 | +63.62% | -2.36% | positive |
| C21_HANAFG_2024_VALUEUP_CAPITAL_RETURN_HIGH_MAE | 086790 | 하나금융지주 | 2024-02-28 value-up / financial-holding capital return bridge | 2024-02-29 @ 56,600 | 2024-10-25 @ 69,200 | 2024-04-19 @ 51,600 | +22.26% | -8.83% | positive_high_MAE_watch |
| C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE | 323410 | 카카오뱅크 | 2024-02-28 financial/value-up sympathy label | 2024-02-29 @ 28,450 | 2024-03-14 @ 29,600 | 2024-09-09 @ 19,450 | +4.04% | -31.63% | counterexample_hard_4C |

## 4. Interpretation

### 4.1 KB금융 — C21 positive

KB금융은 C21에서 가장 교과서적인 positive에 가깝다.
공통 catalyst는 Korea Corporate Value-up follow-up이고, price path는 entry 이후 거의 바로 회복하면서 4월의 shallow pullback을 견디고 10월까지 재평가가 이어졌다.

Mechanism은 단순하다.
은행은 성장주가 아니라 자본의 저수지다. 저수지에 물이 충분하고, 수문을 열어 배당·자사주·소각으로 돌려줄 의지가 보이면 PBR discount가 줄어든다. 이때 가격은 단순 theme rally가 아니라 “자본정책이 ROE/PBR을 다시 번역한 경로”가 된다.

Calibration note:

```text
entry_price = 63500
peak_price = 103900
mfe_pct = +63.62
trough_price = 62000
mae_pct = -2.36
classification = positive
```

Shadow rule implication:

```text
if C21 and bank_level_capital_return_bridge_verified and ROE/PBR_discount_context_present:
    allow Stage3-Green candidate even when full-window 4B proximity exists
else:
    keep Stage2-Actionable only
```

### 4.2 하나금융지주 — positive but high-MAE watch

하나금융지주는 방향은 맞았지만 path quality가 KB보다 약하다.
Entry 56,600에서 peak 69,200까지 MFE는 충분히 양수였으나, 4월 low 51,600까지 MAE -8.83%가 발생했다. 이는 C21에서 **정책 라벨만으로 Green을 주면 안 되고, capital return quality / CET1 / dividend-backs / buyback-cancellation bridge를 더 확인해야 한다**는 증거다.

Calibration note:

```text
entry_price = 56600
peak_price = 69200
mfe_pct = +22.26
trough_price = 51600
mae_pct = -8.83
classification = positive_high_mae_watch
```

Shadow rule implication:

```text
if C21 positive but MAE worse than -8% before durable breakout:
    Stage2-Actionable stays
    Green requires company-level capital return evidence and lower drawdown confirmation
```

### 4.3 카카오뱅크 — financial label false positive / hard 4C

카카오뱅크는 같은 “금융” 이름표를 달고 있지만 C21의 value bank가 아니다.
Entry 28,450 이후 peak 29,600으로 MFE +4.04%에 그쳤고, 9월에는 19,450까지 빠져 MAE -31.63%가 발생했다.

이 케이스의 핵심은 C21이 “은행이면 된다”가 아니라는 점이다.
저PBR 금융지주의 자본환원은 얼어붙은 저수지의 수문을 여는 이야기지만, 디지털은행 고PBR 라벨은 성장 기대와 플랫폼 멀티플의 이야기다. 두 이야기를 같은 bucket에 넣으면 모델은 같은 물을 다른 컵에 담았다고 착각한다.

Calibration note:

```text
entry_price = 28450
peak_price = 29600
mfe_pct = +4.04
trough_price = 19450
mae_pct = -31.63
classification = counterexample_hard_4C
```

Shadow rule implication:

```text
if C21 and digital_bank_or_high_pbr_fintech and no explicit capital_return_bridge:
    block Stage2-Actionable
    route to 4C / reject unless profitability + capital policy are independently verified
```

## 5. Score / return alignment

```text
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
```

Current calibrated profile already blocks pure price-only blowoff and hard 4C thesis breaks, but C21 still needs a more specific separator:

1. Financial sector sympathy is not enough.
2. Bank-level ROE/PBR discount and shareholder-return bridge should matter.
3. Digital bank / fintech label must not inherit old-bank value-up score automatically.
4. Full-window 4B should not automatically reject a verified bank capital-return bridge, but it should cap an unverified one.

## 6. Machine-readable rows

### 6.1 case rows

```jsonl
{"row_type": "case", "case_id": "C21_KBFG_2024_VALUEUP_CAPITAL_RETURN_BRIDGE", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "selected_round": "R6", "ticker": "105560", "name": "KB금융", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 63500, "peak_date": "2024-10-25", "peak_price": 103900, "trough_date": "2024-04-19", "trough_price": 62000, "mfe_pct": 63.62, "mae_pct": -2.36, "classification": "positive", "calibration_usable": true, "evidence_family": "corporate_value_up_bank_roe_pbr_capital_return_bridge", "duplicate_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|105560|valueup_capital_return_bridge|2024-02-29"}
{"row_type": "case", "case_id": "C21_HANAFG_2024_VALUEUP_CAPITAL_RETURN_HIGH_MAE", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "selected_round": "R6", "ticker": "086790", "name": "하나금융지주", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 56600, "peak_date": "2024-10-25", "peak_price": 69200, "trough_date": "2024-04-19", "trough_price": 51600, "mfe_pct": 22.26, "mae_pct": -8.83, "classification": "positive_high_mae_watch", "calibration_usable": true, "evidence_family": "corporate_value_up_bank_roe_pbr_capital_return_bridge_high_mae", "duplicate_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|086790|valueup_capital_return_bridge_high_mae|2024-02-29"}
{"row_type": "case", "case_id": "C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "selected_round": "R6", "ticker": "323410", "name": "카카오뱅크", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 28450, "peak_date": "2024-03-14", "peak_price": 29600, "trough_date": "2024-09-09", "trough_price": 19450, "mfe_pct": 4.04, "mae_pct": -31.63, "classification": "counterexample_hard_4c", "calibration_usable": true, "evidence_family": "digital_bank_fintech_valueup_label_without_capital_return_bridge", "duplicate_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|323410|digital_bank_valueup_false_positive|2024-02-29"}
```

### 6.2 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "C21_KBFG_2024_VALUEUP_CAPITAL_RETURN_BRIDGE_T1", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "ticker": "105560", "name": "KB금융", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 63500, "mfe_pct": 63.62, "mae_pct": -2.36, "peak_date": "2024-10-25", "trough_date": "2024-04-19", "classification": "positive", "calibration_usable": true, "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|105560|valueup_capital_return_bridge|2024-02-29"}
{"row_type": "trigger", "trigger_id": "C21_HANAFG_2024_VALUEUP_CAPITAL_RETURN_HIGH_MAE_T1", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "ticker": "086790", "name": "하나금융지주", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 56600, "mfe_pct": 22.26, "mae_pct": -8.83, "peak_date": "2024-10-25", "trough_date": "2024-04-19", "classification": "positive_high_mae_watch", "calibration_usable": true, "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|086790|valueup_capital_return_bridge_high_mae|2024-02-29"}
{"row_type": "trigger", "trigger_id": "C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE_T1", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "ticker": "323410", "name": "카카오뱅크", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 28450, "mfe_pct": 4.04, "mae_pct": -31.63, "peak_date": "2024-03-14", "trough_date": "2024-09-09", "classification": "counterexample_hard_4c", "calibration_usable": true, "dedupe_key": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|323410|digital_bank_valueup_false_positive|2024-02-29"}
```

### 6.3 score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "C21_KBFG_2024_VALUEUP_CAPITAL_RETURN_BRIDGE", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "current_profile_stage_estimate": "Stage2-Actionable_or_Stage3-Yellow", "proposed_shadow_stage": "Stage3-Green_if_company_level_capital_return_bridge_verified", "raw_component_score_breakdown": {"theme_fit": 18, "capital_return_specificity": 17, "roe_pbr_discount_resolution": 14, "non_price_evidence": 15, "price_confirmation": 14, "4b_full_window_penalty": -4, "source_url_repair_penalty": -2}, "shadow_total": 72, "shadow_note": "현 profile이 full 4B를 과도 차단하지 말고, bank-level capital return bridge가 있으면 C21 sector-specific Green exception 후보."}
{"row_type": "score_simulation", "case_id": "C21_HANAFG_2024_VALUEUP_CAPITAL_RETURN_HIGH_MAE", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "current_profile_stage_estimate": "Stage2-Actionable", "proposed_shadow_stage": "Stage2-Actionable_high_MAE_watch", "raw_component_score_breakdown": {"theme_fit": 17, "capital_return_specificity": 13, "roe_pbr_discount_resolution": 13, "non_price_evidence": 12, "price_confirmation": 11, "mae_penalty": -7, "source_url_repair_penalty": -2}, "shadow_total": 57, "shadow_note": "방향은 맞지만 -8%대 MAE가 발생해 Green 자동승격 금지. reserve/ROE/자본정책 quality 추가 확인 필요."}
{"row_type": "score_simulation", "case_id": "C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "current_profile_stage_estimate": "Stage2_possible_false_positive", "proposed_shadow_stage": "4C_or_reject", "raw_component_score_breakdown": {"theme_fit": 10, "capital_return_specificity": 1, "roe_pbr_discount_resolution": 2, "non_price_evidence": 2, "price_confirmation": -8, "hard_4c_drawdown": -18, "digital_bank_high_pbr_penalty": -7}, "shadow_total": -18, "shadow_note": "금융/은행 라벨만으로 C21에 태우면 안 되는 반례. ROE/PBR 저평가 + 명시 자본환원 bridge 없음."}
```

### 6.4 aggregate row

```jsonl
{"row_type": "aggregate", "selected_round": "R6", "selected_loop": 105, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "verified_url_repair_needed_count": 2, "auto_selected_coverage_gap": "C21 rows 48, 50-row target까지 2 부족", "loop_contribution_label": "canonical_archetype_rule_candidate"}
```

### 6.5 shadow weight row

```jsonl
{"row_type": "shadow_weight", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_axis_proposed": "c21_bank_roe_pbr_capital_return_quality_bridge_required_for_stage2_actionable_shadow_only", "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to C21 value-up/bank rallies", "existing_axis_weakened": null, "production_scoring_changed": false, "shadow_weight_only": true, "suggested_effect": "금융주 value-up 라벨에 점수를 주되, bank-level ROE/PBR 저평가 + CET1/배당/자사주/소각 bridge가 없으면 Stage2 이상 제한."}
```

### 6.6 residual contribution row

```jsonl
{"row_type": "residual_contribution", "residual_error_type": ["financial_sector_label_false_positive", "capital_return_bridge_under_specified", "digital_bank_high_pbr_not_same_as_value_bank"], "why_current_profile_still_misses": "Global calibrated profile은 price-only blowoff와 4B/4C는 잡지만, C21 내부에서 value bank와 digital/high-PBR bank를 갈라내는 capital-return-quality 축이 약하다.", "batch_handoff_priority": "medium_high"}
```

## 7. Proposed shadow rule

```text
new_axis_proposed = c21_bank_roe_pbr_capital_return_quality_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C21 value-up/bank rallies
existing_axis_weakened = null
production_scoring_changed = false
```

Proposed gating:

```text
if canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:
    require at least one of:
        - explicit dividend / buyback / cancellation / shareholder-return policy
        - credible ROE improvement + PBR discount resolution setup
        - bank-level capital return plan with CET1 / capital ratio support
    and reject / cap if:
        - only "financial sector value-up" headline
        - digital bank / fintech high-PBR sympathy without capital return bridge
        - MFE < +8% and MAE < -20% within the same 180D window
```

## 8. Validation caveats

```text
company_level_capital_return_url_repair_needed_count = 2
source_proxy_only_cases = ["KB금융", "하나금융지주"]
reason = "Reuters value-up source verifies sector catalyst, but batch implementation should attach direct company-level capital return / buyback / dividend policy URLs."
```

This caveat does not block the price-path calibration row, because the price rows are verified in stock-web. It does mean the shadow rule should not be promoted to production until the company-level evidence URLs are repaired.

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not re-run live scans.

Read this MD as one historical calibration artifact for:
- selected_round = R6
- large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
- canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
- fine_archetype_id = BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_QUALITY_BRIDGE_VS_DIGITAL_BANK_HIGH_PBR_FALSE_POSITIVE

Ingest only machine-readable JSONL blocks if schema-compatible.
Do not apply production weight changes directly.
Add or stage a shadow-only axis candidate:
c21_bank_roe_pbr_capital_return_quality_bridge_required_for_stage2_actionable_shadow_only

Before production promotion:
1. Verify company-level capital return URLs for KB금융 and 하나금융지주.
2. Confirm no duplicate keys:
   - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|105560|valueup_capital_return_bridge|2024-02-29
   - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|086790|valueup_capital_return_bridge_high_mae|2024-02-29
   - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|323410|digital_bank_valueup_false_positive|2024-02-29
3. Keep KakaoBank as a hard negative separator for digital-bank/high-PBR fintech sympathy.
4. Do not modify live trading, broker APIs, or production scoring unless batch approval exists.
```

## 10. Final summary

```text
selected_round = R6
selected_loop = 105
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
new_independent_case_count = 3
reused_case_count = 0
calibration_usable_case_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
verified_url_repair_needed_count = 2
auto_selected_coverage_gap = C21 rows 48, 50-row target까지 2 부족
loop_contribution_label = canonical_archetype_rule_candidate
next_recommended_archetypes = C22_INSURANCE_RATE_CYCLE_RESERVE, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```
