# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
output_file = e2r_stock_web_v12_residual_round_R11_loop_132_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
selected_round = R11
selected_loop = 132
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / over_50_rows_quality_repair / C31 rows 118
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY

mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

이번 loop는 새 C31 종목을 무작정 늘리는 작업이 아니다. 이미 C31은 50 row 이상이므로, 목적은 `정책/보조금/입법 이벤트`라는 큰 라벨 안에서 **정책 headline → 실제 기업가치 실현 bridge**가 있는 경우와, **저PBR/공기업/정책 proxy만 있는 경우**를 분리하는 품질 보강이다.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Global rule은 이미 작동한다고 가정한다. 이번 residual은 “C31에서 어떤 정책 이벤트가 Stage2-Actionable까지 갈 수 있고, 어떤 정책 proxy는 Stage2-watch에 갇혀야 하는가”다.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R11
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY
```

C31은 일반 sector positive 연구가 아니라 정책·입법·보조금·제도 이벤트가 각 종목에 어떤 bridge를 만드는지 검사하는 scope다. 이번 loop의 시장 사건은 2024-02-26 한국 Corporate Value-Up Program 발표다.

## 3. Previous Coverage / Duplicate Avoidance Check

```text
NO_REPEAT_INDEX_STATUS:
C31_POLICY_SUBSIDY_LEGISLATION_EVENT rows = 118
priority_bucket = Priority 2
guidance = 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선

previous_session_outputs_excluded:
C02, C09, C14, C10, C06, C07, C11, C01, C28, C12, C05, C23, C27, C08, C19

hard_duplicate_key:
canonical_archetype_id + symbol + trigger_type + entry_date
```

이번 5개 trigger는 모두 `C31 + symbol + trigger_type + 2024-02-26` 조합이 서로 다르고, case role도 금융지주 positive, 보험 positive, 지주사 counterexample, 공기업 counterexample으로 갈라진다.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

사용한 shard:

| symbol | company | tradable_shard | profile |
| --- | --- | --- | --- |
| 105560 | KB금융 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json |
| 316140 | 우리금융지주 | atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv | atlas/symbol_profiles/316/316140.json |
| 005830 | DB손해보험 | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | atlas/symbol_profiles/005/005830.json |
| 004990 | 롯데지주 | atlas/ohlcv_tradable_by_symbol_year/004/004990/2024.csv | atlas/symbol_profiles/004/004990.json |
| 015760 | 한국전력 | atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv | atlas/symbol_profiles/015/015760.json |


## 5. Historical Eligibility Gate

| symbol | entry_date | entry_price | forward_window | corp_action_window | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| 105560 | 2024-02-26 | 62500 | 180 | clean_180D_window | true |
| 316140 | 2024-02-26 | 14630 | 180 | clean_180D_window | true |
| 005830 | 2024-02-26 | 95000 | 180 | clean_180D_window; profile has old 1999 corporate-action candidate outside window | true |
| 004990 | 2024-02-26 | 28800 | 180 | clean_180D_window | true |
| 015760 | 2024-02-26 | 24850 | 180 | clean_180D_window | true |


DB손해보험의 profile에는 과거 1999-07-20 corporate-action candidate가 있으나 이번 entry window와 겹치지 않으므로 2024-02-26 기준 30/90/180D calibration에는 사용 가능으로 둔다.

## 6. Canonical Archetype Compression Map

```text
fine_archetype:
KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY

compresses_to:
C31_POLICY_SUBSIDY_LEGISLATION_EVENT

sub-routes:
1. policy_event + firm_level_shareholder_return_bridge -> Stage2-Actionable candidate
2. policy_event + financial_ROE/PBR/capital_return sensitivity -> Stage2 or Stage2-Actionable candidate
3. policy_event + low_PBR_holdco_proxy only -> Stage2-watch or 4B overlay, not Green
4. policy_event + regulated_state_utility/tariff debt proxy -> counterexample, not shareholder-return bridge
```

## 7. Case Selection Summary

| symbol | company | role | trigger | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105560 | KB금융 | positive | Stage2-Actionable | 2024-02-26 | 62500 | 44.0 | -4.48 | 60.0 | -4.48 | current_profile_too_late_without_firm_level_bridge_field |
| 316140 | 우리금융지주 | positive | Stage2 | 2024-02-26 | 14630 | 5.95 | -4.92 | 16.88 | -6.08 | current_profile_correct_if_capped_at_stage2_until_firm_plan |
| 005830 | DB손해보험 | positive | Stage2-Actionable | 2024-02-26 | 95000 | 20.21 | -4.11 | 30.53 | -4.11 | current_profile_too_late_when_policy_and_roe_return_bridge_coexist |
| 004990 | 롯데지주 | counterexample | Stage2 | 2024-02-26 | 28800 | 7.29 | -15.62 | 7.29 | -30.38 | current_profile_false_positive_if_policy_score_not_capped |
| 015760 | 한국전력 | counterexample | Stage2 | 2024-02-26 | 24850 | 2.41 | -23.14 | 2.41 | -26.8 | current_profile_false_positive_if_policy_subsidy_event_not_separated_from_shareholder_return |


## 8. Positive vs Counterexample Balance

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
new_trigger_family_count = 5
calibration_usable_trigger_count = 5
representative_trigger_count = 5
positive_case_count = 3
counterexample_count = 2
stage4b_overlay_count = 2
stage4c_case_count = 2
current_profile_error_count = 4
```

Positive/control은 KB금융, 우리금융지주, DB손해보험이다. Counterexample/guardrail은 롯데지주, 한국전력이다. C31의 표면 단어는 모두 “정책 이벤트”지만, 가격경로는 bridge 유무에 따라 완전히 갈라진다.

## 9. Evidence Source Map

| source | url | use |
| --- | --- | --- |
| FSC 2024-02-26 Corporate Value-Up Program press release | https://www.fsc.go.kr/eng/pr010101/81778 | Official policy event; voluntary disclosure, tax incentives, value-up index/ETF, ROE/PBR/dividend metrics. |
| Reuters 2024-02-26 Korea reform steps | https://www.reuters.com/markets/asia/south-korea-unveils-reform-measures-tackle-korea-discount-2024-02-26/ | Market reaction and disappointment risk; useful for not over-crediting policy headline. |
| FSC 2024-05-02 draft guidelines | https://www.fsc.go.kr/eng/pr010101/82213 | Guidelines are voluntary and future-oriented; disclosure begins when companies are ready. |
| Kim & Chang 2024-06-05 finalized guidelines | https://www.kimchang.com/en/insights/detail.kc?idx=29708&sch_section=4 | Finalized guidelines took effect 2024-05-27; key indicators include PBR/PER/ROE/shareholder return. |
| Kim & Chang details | https://www.kimchang.com/en/insights/detail.kc?idx=29303&sch_section=4 | Program includes low-PBR/PER disclosure and shareholder return / recapitalization / long-term investment information. |


As-of evidence 해석:

- 2024-02-26에는 정부가 Corporate Value-Up Program의 framework를 공개했다.
- 같은 시점에 모든 기업이 강제 실행해야 하는 법적 의무가 생긴 것은 아니므로, “정책 발표”는 기본적으로 Stage2-watch 재료다.
- Actionable로 올리려면 각 기업의 board-level plan, 배당·자사주 소각·ROE target·자본효율 개선, 또는 index/ETF/rebalancing flow 같은 bridge가 필요하다.
- 저PBR/지주사/공기업이라는 proxy만 있으면 정책 score를 cap해야 한다.

## 10. Price Data Source Map

| symbol | entry row | 30D extreme | 90D extreme | 180D extreme |
| --- | --- | --- | --- | --- |
| 105560 | 2024-02-26 c=62500 | high 78600 / low 59700 | high 90000 / low 59700 | high 100000 / low 59700 |
| 316140 | 2024-02-26 c=14630 | high 15500 / low 14100 | high 15500 / low 13910 | high 17100 / low 13740 |
| 005830 | 2024-02-26 c=95000 | high 110000 / low 91100 | high 114200 / low 91100 | high 124000 / low 91100 |
| 004990 | 2024-02-26 c=28800 | high 30900 / low 27800 | high 30900 / low 24300 | high 30900 / low 20050 |
| 015760 | 2024-02-26 c=24850 | high 25450 / low 21100 | high 25450 / low 19100 | high 25450 / low 18190 |


## 11. Case-by-Case Trigger Grid

| symbol | company | trigger_family | trigger_type | role | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105560 | KB금융 | value_up_policy_plus_bank_roe_pbr_shareholder_return | Stage2-Actionable | positive | 2024-02-26 | 62500 | 25.76 | -4.48 | 44.0 | -4.48 | 60.0 | -4.48 |
| 316140 | 우리금융지주 | value_up_policy_plus_financial_holdco_soft_bridge | Stage2 | positive | 2024-02-26 | 14630 | 5.95 | -3.62 | 5.95 | -4.92 | 16.88 | -6.08 |
| 005830 | DB손해보험 | value_up_policy_plus_insurance_roe_capital_return | Stage2-Actionable | positive | 2024-02-26 | 95000 | 15.79 | -4.11 | 20.21 | -4.11 | 30.53 | -4.11 |
| 004990 | 롯데지주 | value_up_policy_low_pbr_holdco_proxy_without_return_bridge | Stage2 | counterexample | 2024-02-26 | 28800 | 7.29 | -3.47 | 7.29 | -15.62 | 7.29 | -30.38 |
| 015760 | 한국전력 | policy_headline_state_utility_tariff_regulation_proxy | Stage2 | counterexample | 2024-02-26 | 24850 | 2.41 | -15.09 | 2.41 | -23.14 | 2.41 | -26.8 |


## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Positive/control rows

| symbol | why positive | price path |
| --- | --- | --- |
| 105560 KB금융 | policy + financial shareholder-return bridge | +44.00% MFE90 with only -4.48% MAE90; +60.00% MFE180 |
| 316140 우리금융지주 | policy + financial holdco bridge but company-specific plan still soft at entry | +5.95% MFE90 / -4.92% MAE90; +16.88% MFE180 |
| 005830 DB손해보험 | policy + insurance ROE/capital-return bridge | +20.21% MFE90 / -4.11% MAE90; +30.53% MFE180 |


### 12.2 Counterexample/guardrail rows

| symbol | why counterexample | price path |
| --- | --- | --- |
| 004990 롯데지주 | low-PBR/holdco proxy without firm-level value realization bridge | +7.29% MFE90 but -15.62% MAE90; -30.38% MAE180 |
| 015760 한국전력 | regulated state-utility policy/tariff proxy, not shareholder-return bridge | +2.41% MFE90 but -23.14% MAE90; -26.80% MAE180 |


## 13. Current Calibrated Profile Stress Test

| symbol | current profile issue | residual |
| --- | --- | --- |
| 105560 | too conservative if it treats the event as broad C31 only | firm-level capital-return bridge should unlock Actionable |
| 316140 | mostly correct if capped at Stage2 before explicit company plan | do not force Yellow/Green at the policy announcement date |
| 005830 | too conservative if insurance ROE/capital-return sensitivity is ignored | Actionable allowed, Green restricted by peak drawdown |
| 004990 | false positive if low-PBR policy proxy receives full policy score | needs policy score cap and 4B overlay |
| 015760 | false positive if state utility tariff/policy headline is treated as value-up | regulated utility policy proxy must be separated |


## 14. Stage2 / Yellow / Green Comparison

```text
Stage2:
- broad official policy event
- low-PBR/PBR/ROE context
- market-wide attention

Stage2-Actionable:
- company-level shareholder return, capital efficiency, buyback/cancel/dividend/ROE target
- sector with clean mechanism from policy to valuation repricing
- low drawdown profile in 30/90D window

Stage3-Yellow:
- policy + actual company plan + credible implementation route
- price/return alignment survives beyond headline window
- not just low-PBR proxy

Stage3-Green:
- generally blocked at first policy announcement date
- requires firm-level disclosure/implementation, revision, and durable rerating evidence
```

이번 loop에서는 Green unlock을 제안하지 않는다. C31 broad policy는 촛불이고, 회사별 bridge가 심지와 기름이다. 촛불만 보고 온 집이 따뜻해졌다고 쓰면 profile은 Lotte/KEPCO 같은 proxy trap에 걸린다.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local 4B cue | full-window result | rule implication |
| --- | --- | --- | --- |
| 004990 | 2024-03-05 local peak 30900 after value-up headline | 180D low 20050, drawdown after peak -35.11% | local policy-proxy blowoff should not become positive Stage3 |
| 015760 | 2024-03-14 local peak 25450 | 180D low 18190, drawdown after peak -28.53% | regulated policy proxy requires non-price value bridge before any positive credit |
| 005830 | positive MFE but peak drawdown -19.76% | not full 4C, but post-peak 4B watch | Actionable yes; Green no |


## 16. 4C Protection Audit

4C는 “정책이 마음에 안 든다”가 아니라 thesis break다.

```text
C31 hard/soft 4C criteria:
- policy event remains voluntary and company has no plan after implementation window
- firm-level value-up plan lacks shareholder-return, ROE, or capital-efficiency bridge
- regulated/political constraints prevent value realization
- low-PBR proxy produces price squeeze but no implementation evidence, then high MAE
```

이번 loop에서 롯데지주와 한국전력은 4C-like protection candidate다. 단, hard 4C보다는 `Stage2-watch cap + 4B overlay + no Green`이 우선이다.

## 17. Sector-Specific Rule Candidate

```text
rule_id = L10_POLICY_EVENT_VALUE_REALIZATION_GATE
scope = large_sector L10 / C31
candidate:
A broad policy/subsidy/legislation event should give only Stage2-watch credit until a firm-level realization bridge appears.
```

Sector-specific gating:

```text
if policy_event_is_voluntary_only:
    policy_or_regulatory_score_cap = 8~10
if firm_level_plan_has_board_role_and_shareholder_return_or_ROE_target:
    add firm_level_value_realization_bridge_score
if stock_is_low_pbr_proxy_only:
    block Stage2-Actionable and Stage3
if stock_is_regulated_state_utility_or_tariff_proxy:
    treat as counterexample unless shareholder-return bridge exists
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_rule_id = C31_POLICY_EVENT_REQUIRES_FIRM_LEVEL_VALUE_REALIZATION_BRIDGE

positive route:
official policy + firm-specific return/capital-efficiency bridge + price path confirmation

counterexample route:
official policy + low-PBR/policy proxy + no company plan + high MAE

recommended shadow delta:
- cap broad C31 policy score unless bridge fields exist
- add bridge field for board-level value-up plan / shareholder return / ROE target / buyback cancel / dividend policy / capital allocation
- add regulated-policy-proxy penalty for tariff/public-utility cases
```

## 19. Before / After Backtest Comparison

| profile | logic | effect | judgment |
| --- | --- | --- | --- |
| P0_baseline_policy_event_uncapped | Broad policy event gives full C31 credit | KB/DB positive; Lotte/KEPCO false positives remain | weak |
| P1_current_e2r_2_2_proxy | Global stage2_required_bridge applies, but C31 bridge taxonomy is under-specified | positives survive but noisy low-PBR proxies still reach Stage2 | medium |
| P2_shadow_bridge_gate | C31 broad policy capped unless firm-level value realization bridge exists | bank/insurance positives retained; holdco/utility proxies downweighted | best |
| P3_strict_green_block | No C31 policy event can exceed Stage2-Actionable before company plan | false positives lower; some KB/DB early rerating may be too late | conservative |
| P4_4B_overlay_focus | Policy-proxy peak without non-price bridge goes local 4B only | works for Lotte/KEPCO but not sufficient for positive recognition | guardrail_only |


## 20. Score-Return Alignment Matrix

| symbol | company | score_before | stage_before | score_after | stage_after | MFE90 | MAE90 | profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105560 | KB금융 | 72.0 | Stage2 | 78.0 | Stage2-Actionable | 44.0 | -4.48 | current_profile_too_late_without_firm_level_bridge_field |
| 316140 | 우리금융지주 | 68.0 | Stage2 | 71.0 | Stage2 | 5.95 | -4.92 | current_profile_correct_if_capped_at_stage2_until_firm_plan |
| 005830 | DB손해보험 | 73.0 | Stage2 | 78.5 | Stage2-Actionable | 20.21 | -4.11 | current_profile_too_late_when_policy_and_roe_return_bridge_coexist |
| 004990 | 롯데지주 | 70.0 | Stage2 | 62.0 | Stage2-watch | 7.29 | -15.62 | current_profile_false_positive_if_policy_score_not_capped |
| 015760 | 한국전력 | 69.0 | Stage2 | 58.5 | Stage2-watch | 2.41 | -23.14 | current_profile_false_positive_if_policy_subsidy_event_not_separated_from_shareholder_return |


## 21. Coverage Matrix

```text
selected_canonical = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
pre_loop_rows_from_index = 118
local_new_usable_trigger_rows = 5
post_commit_representative_effect = quality_repair, not raw quantity target
positive_added = 3
counterexample_added = 2
4B_overlay_added = 2
4C_protection_candidate_added = 2
URL/proxy repair contribution = high
```

## 22. Residual Contribution Summary

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
new_trigger_family_count = 5
tested_existing_calibrated_axes:
- stage2_required_bridge
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

residual_error_types_found:
- policy_proxy_false_positive
- low_pbr_without_firm_level_bridge
- regulated_state_utility_policy_proxy
- firm_level_value_up_bridge_underweighted

loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web 2024 tradable_raw rows
- entry date = 2024-02-26 where available
- 30D / 90D / 180D MFE and MAE
- profile corporate-action caveats where available
- evidence available at or around policy trigger date
```

Not validated in this MD:

```text
- no live candidate recommendation
- no present-day portfolio implication
- no production scoring patch
- no brokerage/API/trading instruction
- no KRX disclosure scrape for every later company-specific value-up plan
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_POLICY_EVENT_REQUIRES_FIRM_LEVEL_VALUE_REALIZATION_BRIDGE,canonical,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"cap broad voluntary policy score and add bridge score only for board-level shareholder-return/ROE/value-up plan","reduces false positives in low-PBR/state-policy proxies while preserving bank/insurance value-up positives","TR_R11L132_C31_105560_KB_VALUEUP_CAPITAL_RETURN|TR_R11L132_C31_316140_WOORI_VALUEUP_SOFT_POSITIVE|TR_R11L132_C31_005830_DB_INSURANCE_VALUEUP_CAPITAL_RETURN|TR_R11L132_C31_004990_LOTTE_POLICY_PROXY_COUNTEREXAMPLE|TR_R11L132_C31_015760_KEPCO_REGULATED_POLICY_COUNTEREXAMPLE",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L132_C31_105560_KB_VALUEUP_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "case_type": "policy_event_with_firm_level_capital_return_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_policy_bridge", "current_profile_verdict": "current_profile_too_late_without_firm_level_bridge_field", "price_source": "Songdaiki/stock-web", "notes": "정부 Corporate Value-Up 발표와 금융지주 ROE/PBR/주주환원 민감도가 결합된 케이스. 단순 정책 headline이 아니라 capital return bridge가 붙을 때 C31 가중을 허용해야 함."}
{"row_type": "trigger", "trigger_id": "TR_R11L132_C31_105560_KB_VALUEUP_CAPITAL_RETURN", "case_id": "R11L132_C31_105560_KB_VALUEUP_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "loop_objective": "quality_repair|source_proxy_replacement|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 62500, "evidence_available_at_that_date": "정부 Corporate Value-Up 발표와 금융지주 ROE/PBR/주주환원 민감도가 결합된 케이스. 단순 정책 headline이 아니라 capital return bridge가 붙을 때 C31 가중을 허용해야 함.", "evidence_source": "FSC Corporate Value-Up Program 2024-02-26; Reuters 2024-02-26; KRX/Kim&Chang guideline summaries; stock-web OHLC shard", "stage2_evidence_fields": ["official_value_up_program", "low_pbr_policy_context", "shareholder_return_bridge", "financial_roe_pbr_sensitivity"], "stage3_evidence_fields": ["capital_return_visibility", "valuation_repricing", "institutional_index_flow_option"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.76, "MFE_90D_pct": 44.0, "MFE_180D_pct": 60.0, "MAE_30D_pct": -4.48, "MAE_90D_pct": -4.48, "MAE_180D_pct": -4.48, "peak_date": "2024-10-28", "peak_price": 100000, "drawdown_after_peak_pct": -12.2, "green_lateness_ratio": 0.4, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "strong_positive_policy_bridge", "current_profile_verdict": "current_profile_too_late_without_firm_level_bridge_field", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|105560|Stage2-Actionable|2024-02-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R11L132_C31_316140_WOORI_VALUEUP_SOFT_POSITIVE", "symbol": "316140", "company_name": "우리금융지주", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "case_type": "policy_event_with_delayed_company_plan_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "moderate_positive_but_not_green", "current_profile_verdict": "current_profile_correct_if_capped_at_stage2_until_firm_plan", "price_source": "Songdaiki/stock-web", "notes": "금융지주 value-up 민감도는 있으나 2024-02-26 당일에는 회사별 plan/implementation이 아직 부족하므로 Stage2 cap이 적절."}
{"row_type": "trigger", "trigger_id": "TR_R11L132_C31_316140_WOORI_VALUEUP_SOFT_POSITIVE", "case_id": "R11L132_C31_316140_WOORI_VALUEUP_SOFT_POSITIVE", "symbol": "316140", "company_name": "우리금융지주", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "loop_objective": "quality_repair|source_proxy_replacement|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 14630, "evidence_available_at_that_date": "금융지주 value-up 민감도는 있으나 2024-02-26 당일에는 회사별 plan/implementation이 아직 부족하므로 Stage2 cap이 적절.", "evidence_source": "FSC Corporate Value-Up Program 2024-02-26; Reuters 2024-02-26; KRX/Kim&Chang guideline summaries; stock-web OHLC shard", "stage2_evidence_fields": ["official_value_up_program", "low_pbr_policy_context", "financial_shareholder_return_sensitivity"], "stage3_evidence_fields": ["later_company_plan_visibility_pending_at_trigger"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv", "profile_path": "atlas/symbol_profiles/316/316140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.95, "MFE_90D_pct": 5.95, "MFE_180D_pct": 16.88, "MAE_30D_pct": -3.62, "MAE_90D_pct": -4.92, "MAE_180D_pct": -6.08, "peak_date": "2024-10-25", "peak_price": 17100, "drawdown_after_peak_pct": -9.77, "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "trigger_outcome_label": "moderate_positive_but_not_green", "current_profile_verdict": "current_profile_correct_if_capped_at_stage2_until_firm_plan", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|316140|Stage2|2024-02-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R11L132_C31_005830_DB_INSURANCE_VALUEUP_CAPITAL_RETURN", "symbol": "005830", "company_name": "DB손해보험", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "case_type": "policy_event_with_insurance_roe_capital_return_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_peak_drawdown_requires_stage3_caution", "current_profile_verdict": "current_profile_too_late_when_policy_and_roe_return_bridge_coexist", "price_source": "Songdaiki/stock-web", "notes": "저PBR 보험/금융 업종에서 value-up 정책과 ROE/자본환원 기대가 결합될 때 90D 성과가 충분했지만, 180D 이후 peak drawdown이 커 Green은 제한."}
{"row_type": "trigger", "trigger_id": "TR_R11L132_C31_005830_DB_INSURANCE_VALUEUP_CAPITAL_RETURN", "case_id": "R11L132_C31_005830_DB_INSURANCE_VALUEUP_CAPITAL_RETURN", "symbol": "005830", "company_name": "DB손해보험", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "loop_objective": "quality_repair|source_proxy_replacement|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 95000, "evidence_available_at_that_date": "저PBR 보험/금융 업종에서 value-up 정책과 ROE/자본환원 기대가 결합될 때 90D 성과가 충분했지만, 180D 이후 peak drawdown이 커 Green은 제한.", "evidence_source": "FSC Corporate Value-Up Program 2024-02-26; Reuters 2024-02-26; KRX/Kim&Chang guideline summaries; stock-web OHLC shard", "stage2_evidence_fields": ["official_value_up_program", "insurance_roe_pbr_sensitivity", "capital_return_bridge"], "stage3_evidence_fields": ["sector_repricing", "valuation_repricing"], "stage4b_evidence_fields": ["post_peak_drawdown_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.79, "MFE_90D_pct": 20.21, "MFE_180D_pct": 30.53, "MAE_30D_pct": -4.11, "MAE_90D_pct": -4.11, "MAE_180D_pct": -4.11, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -19.76, "green_lateness_ratio": 0.007, "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": "peak_within_30D_then_full_window_drawdown", "trigger_outcome_label": "positive_but_peak_drawdown_requires_stage3_caution", "current_profile_verdict": "current_profile_too_late_when_policy_and_roe_return_bridge_coexist", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile has old 1999 corporate-action candidate outside window", "same_entry_group_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005830|Stage2-Actionable|2024-02-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R11L132_C31_004990_LOTTE_POLICY_PROXY_COUNTEREXAMPLE", "symbol": "004990", "company_name": "롯데지주", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "case_type": "policy_event_low_pbr_proxy_without_value_realization_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_low_pbr_policy_proxy", "current_profile_verdict": "current_profile_false_positive_if_policy_score_not_capped", "price_source": "Songdaiki/stock-web", "notes": "저PBR/지주사라는 proxy만으로 value-up 수혜를 부여하면 90D/180D MAE가 커진다. 회사별 자사주 소각, 배당, ROE target, asset disposal 같은 value realization bridge가 없으면 Stage2-watch로 제한."}
{"row_type": "trigger", "trigger_id": "TR_R11L132_C31_004990_LOTTE_POLICY_PROXY_COUNTEREXAMPLE", "case_id": "R11L132_C31_004990_LOTTE_POLICY_PROXY_COUNTEREXAMPLE", "symbol": "004990", "company_name": "롯데지주", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "loop_objective": "quality_repair|source_proxy_replacement|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 28800, "evidence_available_at_that_date": "저PBR/지주사라는 proxy만으로 value-up 수혜를 부여하면 90D/180D MAE가 커진다. 회사별 자사주 소각, 배당, ROE target, asset disposal 같은 value realization bridge가 없으면 Stage2-watch로 제한.", "evidence_source": "FSC Corporate Value-Up Program 2024-02-26; Reuters 2024-02-26; KRX/Kim&Chang guideline summaries; stock-web OHLC shard", "stage2_evidence_fields": ["official_value_up_program", "low_pbr_policy_context"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["local_policy_proxy_blowoff_without_non_price_bridge"], "stage4c_evidence_fields": ["persistent_no_company_level_value_realization_bridge"], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004990/2024.csv", "profile_path": "atlas/symbol_profiles/004/004990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.29, "MFE_90D_pct": 7.29, "MFE_180D_pct": 7.29, "MAE_30D_pct": -3.47, "MAE_90D_pct": -15.62, "MAE_180D_pct": -30.38, "peak_date": "2024-03-05", "peak_price": 30900, "drawdown_after_peak_pct": -35.11, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": "peak_within_30D_then_full_window_drawdown", "trigger_outcome_label": "false_positive_low_pbr_policy_proxy", "current_profile_verdict": "current_profile_false_positive_if_policy_score_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|004990|Stage2|2024-02-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "case", "case_id": "R11L132_C31_015760_KEPCO_REGULATED_POLICY_COUNTEREXAMPLE", "symbol": "015760", "company_name": "한국전력", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "case_type": "policy_event_state_utility_proxy_without_shareholder_return_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_regulated_policy_proxy", "current_profile_verdict": "current_profile_false_positive_if_policy_subsidy_event_not_separated_from_shareholder_return", "price_source": "Songdaiki/stock-web", "notes": "정책 이벤트/공기업/요금정책 기대를 value-up shareholder-return 이벤트와 같은 C31 positive로 처리하면 high-MAE가 발생. 규제/요금/부채 구조는 shareholder return bridge가 아니므로 정책 score cap 필요."}
{"row_type": "trigger", "trigger_id": "TR_R11L132_C31_015760_KEPCO_REGULATED_POLICY_COUNTEREXAMPLE", "case_id": "R11L132_C31_015760_KEPCO_REGULATED_POLICY_COUNTEREXAMPLE", "symbol": "015760", "company_name": "한국전력", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_SHAREHOLDER_RETURN_BRIDGE_VS_LOW_PBR_PROXY", "loop_objective": "quality_repair|source_proxy_replacement|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 24850, "evidence_available_at_that_date": "정책 이벤트/공기업/요금정책 기대를 value-up shareholder-return 이벤트와 같은 C31 positive로 처리하면 high-MAE가 발생. 규제/요금/부채 구조는 shareholder return bridge가 아니므로 정책 score cap 필요.", "evidence_source": "FSC Corporate Value-Up Program 2024-02-26; Reuters 2024-02-26; KRX/Kim&Chang guideline summaries; stock-web OHLC shard", "stage2_evidence_fields": ["policy_event_context"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["policy_proxy_peak_unconfirmed_by_shareholder_return"], "stage4c_evidence_fields": ["regulated_state_utility_value_realization_absent"], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv", "profile_path": "atlas/symbol_profiles/015/015760.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.41, "MFE_90D_pct": 2.41, "MFE_180D_pct": 2.41, "MAE_30D_pct": -15.09, "MAE_90D_pct": -23.14, "MAE_180D_pct": -26.8, "peak_date": "2024-03-14", "peak_price": 25450, "drawdown_after_peak_pct": -28.53, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": "peak_within_30D_then_full_window_drawdown", "trigger_outcome_label": "false_positive_regulated_policy_proxy", "current_profile_verdict": "current_profile_false_positive_if_policy_subsidy_event_not_separated_from_shareholder_return", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|015760|Stage2|2024-02-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy_shadow_test", "case_id": "R11L132_C31_105560_KB_VALUEUP_CAPITAL_RETURN", "trigger_id": "TR_R11L132_C31_105560_KB_VALUEUP_CAPITAL_RETURN", "symbol": "105560", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 72.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 16, "firm_level_value_realization_bridge_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 78.0, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score_cap", "firm_level_value_realization_bridge_score", "execution_risk_score"], "component_delta_explanation": "Voluntary broad policy alone is capped; company-level shareholder-return/ROE bridge unlocks actionable credit; regulated/pure low-PBR proxy is downweighted.", "MFE_90D_pct": 44.0, "MAE_90D_pct": -4.48, "score_return_alignment_label": "strong_positive_policy_bridge", "current_profile_verdict": "current_profile_too_late_without_firm_level_bridge_field"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy_shadow_test", "case_id": "R11L132_C31_316140_WOORI_VALUEUP_SOFT_POSITIVE", "trigger_id": "TR_R11L132_C31_316140_WOORI_VALUEUP_SOFT_POSITIVE", "symbol": "316140", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 68.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 16, "firm_level_value_realization_bridge_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 71.0, "stage_label_after": "Stage2", "changed_components": ["policy_or_regulatory_score_cap", "firm_level_value_realization_bridge_score", "execution_risk_score"], "component_delta_explanation": "Voluntary broad policy alone is capped; company-level shareholder-return/ROE bridge unlocks actionable credit; regulated/pure low-PBR proxy is downweighted.", "MFE_90D_pct": 5.95, "MAE_90D_pct": -4.92, "score_return_alignment_label": "moderate_positive_but_not_green", "current_profile_verdict": "current_profile_correct_if_capped_at_stage2_until_firm_plan"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy_shadow_test", "case_id": "R11L132_C31_005830_DB_INSURANCE_VALUEUP_CAPITAL_RETURN", "trigger_id": "TR_R11L132_C31_005830_DB_INSURANCE_VALUEUP_CAPITAL_RETURN", "symbol": "005830", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 6, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 73.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 16, "firm_level_value_realization_bridge_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 78.5, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score_cap", "firm_level_value_realization_bridge_score", "execution_risk_score"], "component_delta_explanation": "Voluntary broad policy alone is capped; company-level shareholder-return/ROE bridge unlocks actionable credit; regulated/pure low-PBR proxy is downweighted.", "MFE_90D_pct": 20.21, "MAE_90D_pct": -4.11, "score_return_alignment_label": "positive_but_peak_drawdown_requires_stage3_caution", "current_profile_verdict": "current_profile_too_late_when_policy_and_roe_return_bridge_coexist"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy_shadow_test", "case_id": "R11L132_C31_004990_LOTTE_POLICY_PROXY_COUNTEREXAMPLE", "trigger_id": "TR_R11L132_C31_004990_LOTTE_POLICY_PROXY_COUNTEREXAMPLE", "symbol": "004990", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 12, "execution_risk_score": 12, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 70.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 7, "firm_level_value_realization_bridge_score": 0, "execution_risk_score": 16, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 62.0, "stage_label_after": "Stage2-watch", "changed_components": ["policy_or_regulatory_score_cap", "firm_level_value_realization_bridge_score", "execution_risk_score"], "component_delta_explanation": "Voluntary broad policy alone is capped; company-level shareholder-return/ROE bridge unlocks actionable credit; regulated/pure low-PBR proxy is downweighted.", "MFE_90D_pct": 7.29, "MAE_90D_pct": -15.62, "score_return_alignment_label": "false_positive_low_pbr_policy_proxy", "current_profile_verdict": "current_profile_false_positive_if_policy_score_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy_shadow_test", "case_id": "R11L132_C31_015760_KEPCO_REGULATED_POLICY_COUNTEREXAMPLE", "trigger_id": "TR_R11L132_C31_015760_KEPCO_REGULATED_POLICY_COUNTEREXAMPLE", "symbol": "015760", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 12, "execution_risk_score": 12, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 69.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 7, "firm_level_value_realization_bridge_score": 0, "execution_risk_score": 16, "legal_or_contract_risk_score": 3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 58.5, "stage_label_after": "Stage2-watch", "changed_components": ["policy_or_regulatory_score_cap", "firm_level_value_realization_bridge_score", "execution_risk_score"], "component_delta_explanation": "Voluntary broad policy alone is capped; company-level shareholder-return/ROE bridge unlocks actionable credit; regulated/pure low-PBR proxy is downweighted.", "MFE_90D_pct": 2.41, "MAE_90D_pct": -23.14, "score_return_alignment_label": "false_positive_regulated_policy_proxy", "current_profile_verdict": "current_profile_false_positive_if_policy_subsidy_event_not_separated_from_shareholder_return"}
{"row_type": "residual_contribution", "round": "R11", "loop": "132", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["policy_proxy_false_positive", "low_pbr_without_firm_level_bridge", "regulated_state_utility_policy_proxy", "firm_level_value_up_bridge_underweighted"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied `e2r_2_2_rolling_calibrated` profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Tasks

```text
1. Ingest this MD only as a V12 research result.
2. Validate filename, metadata, trigger rows, MFE/MAE fields, entry dates, and stock-web paths.
3. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
4. Treat shadow_weight rows as canonical_archetype rule candidates, not production scoring changes.
5. Add or strengthen the C31 bridge gate only if aggregate evidence from multiple MDs confirms it.
6. Preserve production_scoring_changed=false for this research artifact.
```

### Candidate patch concept

```text
C31_POLICY_EVENT_REQUIRES_FIRM_LEVEL_VALUE_REALIZATION_BRIDGE:
- broad official policy event alone -> Stage2-watch cap
- firm-level value-up plan / shareholder-return / ROE target / capital allocation -> Stage2-Actionable candidate
- low-PBR proxy without company bridge -> block Stage3-Yellow/Green
- regulated state utility / tariff-policy proxy -> add execution/regulatory risk penalty
```

## 27. Next Round State

```text
completed_round = R11
completed_loop = 132
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / over_50_rows_quality_repair / C31 rows 118
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_URL_REPAIR
C18_CONSUMER_EXPORT_CHANNEL_REORDER_URL_REPAIR
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_4B_4C_REPAIR
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_COUNTEREXAMPLE_REPAIR
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_HARD_4C_REPAIR
```

## 28. Source Notes

```text
Primary prompt:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

No-repeat index:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md

Stock-web manifest:
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json

Policy/evidence:
https://www.fsc.go.kr/eng/pr010101/81778
https://www.reuters.com/markets/asia/south-korea-unveils-reform-measures-tackle-korea-discount-2024-02-26/
https://www.fsc.go.kr/eng/pr010101/82213
https://www.kimchang.com/en/insights/detail.kc?idx=29708&sch_section=4
https://www.kimchang.com/en/insights/detail.kc?idx=29303&sch_section=4

Price shards:
atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv
atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv
atlas/ohlcv_tradable_by_symbol_year/004/004990/2024.csv
atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 1
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
