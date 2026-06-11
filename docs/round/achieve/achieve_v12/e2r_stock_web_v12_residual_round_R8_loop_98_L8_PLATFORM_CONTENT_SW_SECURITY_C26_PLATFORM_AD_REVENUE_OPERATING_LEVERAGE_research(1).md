# E2R Stock-Web v12 Residual Research
## R8 / loop 98 / L8_PLATFORM_CONTENT_SW_SECURITY / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

```text
schema_family = v12_sector_archetype_residual
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R8
selected_loop = 98
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = SEARCH_COMMERCE_AD_PLATFORM_OPERATING_LEVERAGE_VS_ADTECH_LABEL_FALSE_STAGE2

price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

---

## 1. Coverage / novelty gate

Repo index 기준 `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`는 3 rows / 3 symbols에 머문 초저커버리지 구역이다.  
이 세션 로컬 산출물 기준으로 R8/C26 loop 97을 이미 수행했으므로 이번 실행은 R8/C26 loop 98로 잡았다.

```text
repo_index_visible_top_symbols = 035420, 042000, 237820
local_prior_C26_symbols = 067160, 089600, 035720
this_run_symbols = 035420, 214270, 216050
new_visible_C26_symbol_count = 2
reused_visible_C26_symbol_count = 1
same_archetype_new_trigger_family_count = 3
```

중복 방지 기준:

```text
dedupe_key = symbol + canonical_archetype_id + trigger_type + entry_date + evidence_family
```

이번 실행은 같은 C26 안에서 다음 세 가지를 분리한다.

1. 진짜 platform ad / search-commerce operating leverage가 확인되는 대형 플랫폼 positive-control.
2. ad-tech / marketing-service label spike가 있지만 ARPU·retention·margin bridge가 약한 false Stage2.
3. 광고경기 회복 label은 있으나 MFE가 작고 forward MAE가 커지는 low-quality Stage2.

---

## 2. Stock-Web source validation

```json
{
  "price_source": "Songdaiki/stock-web",
  "source_basis": "FinanceData/marcap transformed into assistant-readable symbol-year CSV shards",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "manifest_max_date": "2026-02-20",
  "corporate_action_policy": "block contaminated windows by default"
}
```

Symbol validation summary:

```json
{"symbol":"035420","name":"NAVER","profile_path":"atlas/symbol_profiles/035/035420.json","status_inferred":"active_like","calibration_caveat":"historic corporate-action candidates exist, but no 2024/2025 forward-window contamination used"}
{"symbol":"214270","name":"FSN","profile_path":"atlas/symbol_profiles/214/214270.json","status_inferred":"active_like","calibration_caveat":"historic corporate-action candidates exist, but no 2024/2025 forward-window contamination used"}
{"symbol":"216050","name":"인크로스","profile_path":"atlas/symbol_profiles/216/216050.json","status_inferred":"active_like","calibration_caveat":"historic corporate-action candidates exist, but no 2024/2025 forward-window contamination used"}
```

---

## 3. Case table

| case_id | symbol | name | trigger_type | entry_date | entry_price | result_label | thesis |
|---|---:|---|---|---:|---:|---|---|
| C26_NAVER_2024_Q4_SEARCH_COMMERCE_AD_LEVERAGE | 035420 | NAVER | Stage2 | 2024-11-08 | 174600 | positive_control | Search-platform / commerce ad operating leverage was visible enough to avoid over-blocking C26. |
| C26_FSN_2024_ADTECH_LABEL_HIGH_MAE | 214270 | FSN | Stage2 | 2024-07-18 | 2105 | counterexample | Ad-tech / marketing label spike produced MFE but high MAE, so it needs bridge-gating. |
| C26_INCROSS_2024_AD_RECOVERY_LOW_MFE | 216050 | 인크로스 | Stage2 | 2024-10-23 | 7320 | counterexample | Ad recovery label made a short bounce, but MFE was not durable and 180D MAE widened. |

---

## 4. Trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C26_NAVER_2024_Q4_SEARCH_COMMERCE_AD_LEVERAGE","symbol":"035420","name":"NAVER","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"SEARCH_COMMERCE_AD_PLATFORM_OPERATING_LEVERAGE","trigger_type":"Stage2","trigger_date":"2024-11-08","entry_date":"2024-11-08","entry_price":174600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_window_complete":true,"corporate_action_contaminated":false,"result_label":"positive_control","current_profile_verdict":"under_credit_if_platform_ad_recovery_block_is_too_strict","evidence_family":"search_platform_ad_and_commerce_operating_leverage","calibration_usable":true}
{"row_type":"trigger","case_id":"C26_FSN_2024_ADTECH_LABEL_HIGH_MAE","symbol":"214270","name":"FSN","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"ADTECH_MARKETING_SERVICE_LABEL_HIGH_MAE","trigger_type":"Stage2","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":2105,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.63,"MAE_30D_pct":-26.37,"MFE_90D_pct":19.00,"MAE_90D_pct":-26.37,"MFE_180D_pct":19.00,"MAE_180D_pct":-49.64,"forward_window_complete":true,"corporate_action_contaminated":false,"result_label":"counterexample","current_profile_verdict":"false_positive_if_label_only_stage2_bonus_applied","evidence_family":"adtech_label_without_platform_arpu_retention_margin_bridge","calibration_usable":true}
{"row_type":"trigger","case_id":"C26_INCROSS_2024_AD_RECOVERY_LOW_MFE","symbol":"216050","name":"인크로스","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_RECOVERY_LOW_MFE_HIGH_FADE","trigger_type":"Stage2","trigger_date":"2024-10-23","entry_date":"2024-10-23","entry_price":7320,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":11.48,"MAE_30D_pct":-5.19,"MFE_90D_pct":11.48,"MAE_90D_pct":-6.56,"MFE_180D_pct":11.48,"MAE_180D_pct":-15.85,"forward_window_complete":true,"corporate_action_contaminated":false,"result_label":"counterexample","current_profile_verdict":"weak_stage2_if_no_operating_leverage_bridge","evidence_family":"ad_recovery_label_without_durable_margin_or_arpu_bridge","calibration_usable":true}
```

---

## 5. Score / return alignment

### 5.1 NAVER — positive control

NAVER의 경우 `search-platform advertising sales`와 e-commerce core business가 실제 earnings bridge로 연결되는 케이스다.  
2024-11-08 close 174,600원을 entry로 잡으면, 2024-12-12 high 220,000원, 2025-02-07 high 235,500원까지 올라간다.  
동시에 worst low는 2024-11-11 low 171,500원으로 제한돼 C26 positive-control에 가깝다.

```text
entry = 174600
30D high = 220000
30D low = 171500
90D high = 235500
90D low = 171500
180D high = 235500
180D low = 171500

MFE_30D = +26.00%
MAE_30D = -1.78%
MFE_90D = +34.88%
MAE_90D = -1.78%
MFE_180D = +34.88%
MAE_180D = -1.78%
```

Interpretation:

```text
C26에서 platform-level ad/search-commerce monetization이 확인될 경우,
광고경기 label 전체를 막는 over-block은 위험하다.
다만 대형 플랫폼의 경우에도 AI capex / non-ad margin pressure가 생기면 4B watch를 분리한다.
```

### 5.2 FSN — ad-tech label high-MAE counterexample

FSN은 ad-tech / digital marketing vocabulary가 가격 spike를 만들었지만, platform ARPU·retention·margin bridge가 부족하면 C26 Stage2를 과하게 주면 안 되는 counterexample다.

```text
entry = 2105
30D high = 2455
30D low = 1550
90D high = 2505
90D low = 1550
180D high = 2505
180D low = 1060

MFE_30D = +16.63%
MAE_30D = -26.37%
MFE_90D = +19.00%
MAE_90D = -26.37%
MFE_180D = +19.00%
MAE_180D = -49.64%
```

Interpretation:

```text
MFE가 있어도 MAE가 동시에 깊어지는 ad-tech smallcap label은
C26 positive가 아니라 local_4B_watch 또는 Stage2-FalsePositive로 처리해야 한다.
```

### 5.3 Incross — weak ad recovery label counterexample

Incross는 short bounce는 있었지만, MFE가 11%대에 묶이고 180D low가 6,160원까지 내려갔다.  
이 케이스는 ad recovery headline만으로 C26 Stage2-Actionable bonus를 주면 scoring drift가 생긴다는 반례다.

```text
entry = 7320
30D high = 8160
30D low = 6940
90D high = 8160
90D low = 6840
180D high = 8160
180D low = 6160

MFE_30D = +11.48%
MAE_30D = -5.19%
MFE_90D = +11.48%
MAE_90D = -6.56%
MFE_180D = +11.48%
MAE_180D = -15.85%
```

Interpretation:

```text
Low-MFE ad recovery case는 high-MAE가 아니더라도
return alignment가 약하므로 Stage2-Actionable bonus를 줄이면 안 된다.
```

---

## 6. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE",
  "loop": 98,
  "new_independent_case_count": 3,
  "reused_case_count": 1,
  "same_archetype_new_symbol_count_visible_index_basis": 2,
  "same_archetype_new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": null,
  "existing_axis_strengthened": [
    "C26_platform_level_ad_search_commerce_operating_leverage_escape_hatch",
    "C26_adtech_label_without_arpu_retention_margin_bridge_stage2_block",
    "C26_low_MFE_ad_recovery_stage2_bonus_cap",
    "C26_high_MAE_local_4B_watch_for_smallcap_adtech_spike"
  ]
}
```

---

## 7. Rule candidate

```text
rule_id = C26_PLATFORM_AD_OPERATING_LEVERAGE_BRIDGE_GATE
scope = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE

if canonical_archetype_id == C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
and trigger_type == Stage2
and platform_level_search_ad_or_commerce_ad_revenue_growth == true
and operating_profit_or_margin_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_if_cross_evidence_present = true
```

```text
if canonical_archetype_id == C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
and adtech_or_marketing_service_label == true
and platform_level_ARPU_retention_or_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if canonical_archetype_id == C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
and MFE_90D_pct < +15
and no_operating_leverage_bridge == true:
    stage2_actionable_bonus = 0
    score_contribution_cap = true
```

```text
if canonical_archetype_id == C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
and MFE_30D_pct >= +15
and MAE_90D_pct <= -25
and refreshed_non_price_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

---

## 8. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not execute this handoff during the research run.

Task:
- Ingest this MD as a v12 sector-archetype residual research artifact.
- Parse trigger JSONL rows.
- Validate stock-web price fields.
- Do not change production scoring directly.
- Only prepare shadow-rule candidates for C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.
- Candidate axes:
  1. C26_platform_level_ad_search_commerce_operating_leverage_escape_hatch
  2. C26_adtech_label_without_arpu_retention_margin_bridge_stage2_block
  3. C26_low_MFE_ad_recovery_stage2_bonus_cap
  4. C26_high_MAE_local_4B_watch_for_smallcap_adtech_spike
```

---

## 9. Next research state

```text
completed_round = R8
completed_loop = 98
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C15_MATERIAL_SPREAD_SUPERCYCLE, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```
