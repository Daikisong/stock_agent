# E2R v12 Residual Research — R12 / L10 / C32 Governance Control Premium Tender Cap

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R12
selected_loop = 101
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_GO_PRIVATE_DELISING_AND_MINOR_HOLDER_RISK
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Why this residual pass exists

C32의 핵심은 **지배권 이벤트가 실제 현금화 경로로 닫히는지**와 **공개매수 가격이 주가의 천장으로 작동하는지**를 분리하는 것이다. 같은 “지배구조 premium”이라도 시장은 두 얼굴을 보인다. 하나는 공개매수·상장폐지·소수주주 매수청구처럼 현금 가격표가 붙는 얼굴이고, 다른 하나는 가격표 없이 “지배권 분쟁”이라는 이름만 달고 뛰는 얼굴이다.

이번 pass는 기존 C32 top covered symbols인 `000670`, `010130`, `180640`을 반복하지 않았다. 새로 고른 네 종목은 모두 2024년에 stock-web 1D OHLC row로 이벤트 이후 가격이 공개매수/상장폐지 cap 근처로 붙거나, cap이 깨지고 재가격화되는 경로를 확인할 수 있는 케이스다.

```text
static_no_repeat_index_C32_rows = 3
static_no_repeat_index_C32_top_symbols = 000670, 010130, 180640
this_md_new_symbols = 003410, 115390, 119860, 005390
this_md_reused_symbols = none
static_coverage_gap_if_accepted = C32 rows 3 -> 7
conversation_local_C32_gap_if_accepted = C32 rows 3 -> 7
still_need_to_30 = about 23
```

## 2. Validation scope

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false

stock_web_price_atlas_access_allowed = true
stock_web_price_atlas_access_required = true
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row = true
```

Non-price evidence는 이번 단일 실행에서 정식 URL 검증까지 끝내지 않았다. 따라서 모든 비가격 catalyst는 `source_proxy_only / evidence_url_pending=true`로 낮은 신뢰 버킷에 둔다. 단, 가격경로는 `Songdaiki/stock-web`의 symbol profile과 2024/2025 daily shard로 확인했다.

## 3. Stock-web data checks

| symbol | name | stock-web status | available window used | profile note |
|---|---|---|---|---|
| 003410 | 쌍용C&E | inactive_or_delisted_like | 2024-01-02 to 2024-06-20 | 2024년 상장폐지형 tender cap 관찰 가능 |
| 115390 | 락앤락 | inactive_or_delisted_like | 2024-01-02 to 2024-11-19 | 공개매수 이후 cap 고착/저유동성 구간 관찰 가능 |
| 119860 | 커넥트웨이브 | inactive_or_delisted_like | 2024-01-02 to 2024-09-03 | PE tender cap 이후 tail-risk row 관찰 가능 |
| 005390 | 신성통상 | inactive_or_delisted_like | 2024-01-02 to 2025-04-17 | 최초 cap 이후 소수주주/조건 재가격화 반례 관찰 가능 |

## 4. Aggregate finding

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 1
local_4b_watch_count = 3
current_profile_error_count = 4
```

Interpretation:

- C32는 “좋은 지배구조 이벤트”보다 **상방이 현금 가격표에 의해 제한되는지**가 먼저다.
- 공개매수 가격이 사실상 천장이 되면, Stage3-Green으로 승격시키는 대신 `tender_cap_realization_watch`나 `local_4b_watch`로 보수적으로 눌러야 한다.
- 단, 005390처럼 cap이 확정된 듯 보이다가 소수주주/조건/재공개매수 기대가 붙으면 최초 cap 이후에도 high-MAE와 재가격화가 공존한다.
- 따라서 C32는 `control_premium_cash_bridge`만 볼 것이 아니라 `tender_price_cap`, `minority_holder_block`, `delisting_completion_probability`, `post_cap_tail_risk`를 분리해야 한다.

## 5. Trigger-level table

| symbol | entry_date | entry_price | trigger_type | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | outcome |
|---|---:|---:|---|---:|---:|---:|---|
| 003410 쌍용C&E | 2024-02-05 | 6940 | Stage2_Actionable | 1.44% / -2.31% | 1.87% / -2.31% | 1.87% / -2.31% | positive_guardrail |
| 115390 락앤락 | 2024-04-18 | 8680 | Stage3_Yellow | 2.42% / -0.58% | 2.42% / -0.58% | 2.42% / -4.72% | mixed_positive |
| 119860 커넥트웨이브 | 2024-04-29 | 17880 | Stage2_Actionable | 0.34% / -0.67% | 2.35% / -8.05% | 2.35% / -8.05% | positive_with_tail_risk |
| 005390 신성통상 | 2024-06-21 | 2295 | Local_4B_Watch | 23.75% / -8.93% | 23.75% / -8.93% | 23.75% / -11.98% | counterexample_high_mae |


## 6. Case notes

### 6.1 003410 쌍용C&E — clean go-private cap

- Entry: 2024-02-05 close 6,940.
- Path: 2024-02-05부터 7,000원 부근으로 급격히 붙고, 이후 7,000~7,070원의 좁은 박스 안에 고정된다.
- Mechanism: upside가 business rerating이 아니라 공개매수/상장폐지 현금가격에 의해 닫히는 구조다.
- Residual lesson: `go_private_tender_cap_detected=true`이면 valuation upside score를 아무리 높게 주더라도 Green 승격이 아니라 cap-watch로 가야 한다.

### 6.2 115390 락앤락 — PE tender cap with low upside after confirmation

- Entry: 2024-04-18 close 8,680.
- Path: 8,680 근처로 가격이 고정되고 30D high가 8,890에 그친다.
- Mechanism: 공개매수 가격표가 붙는 순간부터 주가는 기업가치 재평가라기보다는 cash-out probability를 가격화한다.
- Residual lesson: 가격이 cap 근처까지 이미 도달한 뒤 Stage3로 따라붙으면 MFE는 작고, 시간이 갈수록 tail MAE만 남는다.

### 6.3 119860 커넥트웨이브 — PE tender cap plus tail wick risk

- Entry: 2024-04-29 close 17,880.
- Path: 17,880~18,000원 부근에 붙지만, 2024-06-21 low 16,440 같은 꼬리 리스크가 남는다.
- Mechanism: 상장폐지형 공개매수라고 해서 path가 무위험 현금등가물이 되지는 않는다. 잔여 물량, 절차, 유동성, 지수/강제매도 꼬리가 MAE를 만든다.
- Residual lesson: `tender_cap_near_price=true`와 `low_liquidity_tail_risk=true`가 동시에 뜨면 upside score보다 execution risk score를 먼저 본다.

### 6.4 005390 신성통상 — initial cap failure / minority repricing counterexample

- Entry: 2024-06-21 close 2,295.
- Path: 최초 cap 부근에서 평평해지는 듯했지만 2024-07-24 high 2,840까지 재가격화되고, 이후 2025-03-27 low 2,020까지 밀린다.
- Mechanism: 오너/지배주주 공개매수는 무조건 clean cap이 아니다. 소수주주 반발, 가격 조정 기대, 실패/재시도 가능성이 오히려 변동성을 키울 수 있다.
- Residual lesson: C32에서 `tender_price_cap`만으로 안정 positive를 주면 안 된다. `minority_holder_acceptance_uncertain=true`면 high-MAE guard를 같이 켜야 한다.

## 7. Current calibrated profile stress test

The current calibrated profile already blocks many price-only blowoffs, but C32 needs a more specific branch. Governance events are like a bridge with a tollgate: after the tender price is posted, the road may still be paved, but the tollgate fixes the exit value. A general valuation or mispricing score sees the bridge; the C32 rule must see the tollgate.

| residual error | observed in | proposed guard |
|---|---|---|
| Treating tender-cap as durable rerating | 003410, 115390, 119860 | `tender_price_cap_blocks_green=true` |
| Assigning upside to late chase after cap reached | 115390, 119860 | `post_cap_late_chase_mfe_penalty=true` |
| Ignoring minority-holder / completion risk | 005390 | `minority_acceptance_uncertain_high_mae_guard=true` |
| Failing to separate cash bridge from governance headline | all 4 | `control_premium_cash_bridge_required=true` |

## 8. Proposed shadow rule

```text
rule_id = C32_GOVERNANCE_TENDER_CAP_GUARD_V1
scope = canonical_archetype_id:C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
production_scoring_changed = false
shadow_weight_only = true

IF governance/control-premium event exists
AND tender_offer_or_go_private_cash_price_is_identifiable
AND current_price / tender_price >= 0.97
THEN:
  block Stage3-Green unlock
  cap max positive classification at Stage2-Actionable or Local-4B-Watch
  require explicit remaining spread >= 8% plus completion probability evidence for positive upgrade

IF tender_offer_or_go_private event exists
AND minority_holder_acceptance_uncertain OR tender terms can be revised/rejected
THEN:
  add high_MAE_guard
  require separate evidence for acceptance ratio / court or board process / revised offer probability
```

Expected effect:

```text
- Clean cap cases: avoid false Green; keep as controlled cash-bridge watch.
- Late chase cases: avoid positive stage if MFE left is too small.
- Minority-risk cases: preserve counterexample signal even when price spikes above first offer.
```

## 9. Machine-readable case rows

```jsonl
{"row_type": "case", "research_session": "post_calibrated_sector_archetype_residual_research", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GO_PRIVATE_TENDER_CAP_CEMENT_DELISING_BRIDGE", "case_id": "C32_R12L101_1_003410_2024-02-05", "symbol": "003410", "name": "쌍용C&E", "event_evidence": "최대주주/PEF의 공개매수·상장폐지 경로로 가격이 공개매수가 부근에 붙은 go-private tender-cap 구조", "source_quality": "source_proxy_only", "evidence_url_pending": true, "price_source": "Songdaiki/stock-web", "outcome": "positive_guardrail", "novelty_check": "new_symbol_for_C32_in_this_session; not in static top covered C32 symbols"}
{"row_type": "case", "research_session": "post_calibrated_sector_archetype_residual_research", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PE_TENDER_OFFER_CAP_CONSUMER_BRAND_DELISING_BRIDGE", "case_id": "C32_R12L101_2_115390_2024-04-18", "symbol": "115390", "name": "락앤락", "event_evidence": "PE sponsor 공개매수 이후 가격이 공개매수가/상장폐지 기대 상단에 고정되는 cap 구조", "source_quality": "source_proxy_only", "evidence_url_pending": true, "price_source": "Songdaiki/stock-web", "outcome": "mixed_positive", "novelty_check": "new_symbol_for_C32_in_this_session; not in static top covered C32 symbols"}
{"row_type": "case", "research_session": "post_calibrated_sector_archetype_residual_research", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "MBK_TENDER_CAP_PLATFORM_DELISING_BRIDGE", "case_id": "C32_R12L101_3_119860_2024-04-29", "symbol": "119860", "name": "커넥트웨이브", "event_evidence": "PE sponsor 공개매수/상장폐지 경로. 가격은 cap 부근에 붙지만 일부 꼬리 리스크 존재", "source_quality": "source_proxy_only", "evidence_url_pending": true, "price_source": "Songdaiki/stock-web", "outcome": "positive_with_tail_risk", "novelty_check": "new_symbol_for_C32_in_this_session; not in static top covered C32 symbols"}
{"row_type": "case", "research_session": "post_calibrated_sector_archetype_residual_research", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "OWNER_TENDER_MINOR_HOLDER_RESISTANCE_AND_REPRICING_RISK", "case_id": "C32_R12L101_4_005390_2024-06-21", "symbol": "005390", "name": "신성통상", "event_evidence": "오너 측 공개매수/상장폐지 시도 성격. 최초 cap 이후 소수주주·조건·재공개매수 리스크가 남는 구조", "source_quality": "source_proxy_only", "evidence_url_pending": true, "price_source": "Songdaiki/stock-web", "outcome": "counterexample_high_mae", "novelty_check": "new_symbol_for_C32_in_this_session; not in static top covered C32 symbols"}
```

## 10. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GO_PRIVATE_TENDER_CAP_CEMENT_DELISING_BRIDGE", "symbol": "003410", "name": "쌍용C&E", "trigger_type": "Stage2_Actionable", "entry_date": "2024-02-05", "entry_price": 6940, "mfe_30d_pct": 1.44, "mae_30d_pct": -2.31, "mfe_30d_high": 7040, "mae_30d_low": 6780, "mfe_30d_high_date": "2024-03-15", "mae_30d_low_date": "2024-03-05", "mfe_90d_pct": 1.87, "mae_90d_pct": -2.31, "mfe_90d_high": 7070, "mae_90d_low": 6780, "mfe_90d_high_date": "2024-04-24", "mae_90d_low_date": "2024-03-05", "mfe_180d_pct": 1.87, "mae_180d_pct": -2.31, "mfe_180d_high": 7070, "mae_180d_low": 6780, "mfe_180d_high_date": "2024-04-24", "mae_180d_low_date": "2024-03-05", "window_180_truncated_by_delisting_or_available_data": true, "last_available_price_date_for_window": "2024-06-20", "current_profile_interpretation": "Stage3-Yellow-like if treated as governance rerating", "outcome": "positive_guardrail", "source_note": "source_proxy_only / evidence_url_pending=true; stock-web 2024 row 확인"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "PE_TENDER_OFFER_CAP_CONSUMER_BRAND_DELISING_BRIDGE", "symbol": "115390", "name": "락앤락", "trigger_type": "Stage3_Yellow", "entry_date": "2024-04-18", "entry_price": 8680, "mfe_30d_pct": 2.42, "mae_30d_pct": -0.58, "mfe_30d_high": 8890, "mae_30d_low": 8630, "mfe_30d_high_date": "2024-05-08", "mae_30d_low_date": "2024-05-14", "mfe_90d_pct": 2.42, "mae_90d_pct": -0.58, "mfe_90d_high": 8890, "mae_90d_low": 8630, "mfe_90d_high_date": "2024-05-08", "mae_90d_low_date": "2024-05-14", "mfe_180d_pct": 2.42, "mae_180d_pct": -4.72, "mfe_180d_high": 8890, "mae_180d_low": 8270, "mfe_180d_high_date": "2024-05-08", "mae_180d_low_date": "2024-10-11", "window_180_truncated_by_delisting_or_available_data": false, "last_available_price_date_for_window": "2024-11-19", "current_profile_interpretation": "Stage3-Yellow/Local-4B if late chase not capped", "outcome": "mixed_positive", "source_note": "source_proxy_only / evidence_url_pending=true; stock-web 2024 row 확인"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "MBK_TENDER_CAP_PLATFORM_DELISING_BRIDGE", "symbol": "119860", "name": "커넥트웨이브", "trigger_type": "Stage2_Actionable", "entry_date": "2024-04-29", "entry_price": 17880, "mfe_30d_pct": 0.34, "mae_30d_pct": -0.67, "mfe_30d_high": 17940, "mae_30d_low": 17760, "mfe_30d_high_date": "2024-05-22", "mae_30d_low_date": "2024-05-24", "mfe_90d_pct": 2.35, "mae_90d_pct": -8.05, "mfe_90d_high": 18300, "mae_90d_low": 16440, "mfe_90d_high_date": "2024-06-26", "mae_90d_low_date": "2024-06-21", "mfe_180d_pct": 2.35, "mae_180d_pct": -8.05, "mfe_180d_high": 18300, "mae_180d_low": 16440, "mfe_180d_high_date": "2024-06-26", "mae_180d_low_date": "2024-06-21", "window_180_truncated_by_delisting_or_available_data": true, "last_available_price_date_for_window": "2024-09-03", "current_profile_interpretation": "Stage3-Yellow-like if event ignored and platform rerating assumed", "outcome": "positive_with_tail_risk", "source_note": "source_proxy_only / evidence_url_pending=true; stock-web 2024 row 확인"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "OWNER_TENDER_MINOR_HOLDER_RESISTANCE_AND_REPRICING_RISK", "symbol": "005390", "name": "신성통상", "trigger_type": "Local_4B_Watch", "entry_date": "2024-06-21", "entry_price": 2295, "mfe_30d_pct": 23.75, "mae_30d_pct": -8.93, "mfe_30d_high": 2840, "mae_30d_low": 2090, "mfe_30d_high_date": "2024-07-24", "mae_30d_low_date": "2024-08-05", "mfe_90d_pct": 23.75, "mae_90d_pct": -8.93, "mfe_90d_high": 2840, "mae_90d_low": 2090, "mfe_90d_high_date": "2024-07-24", "mae_90d_low_date": "2024-08-05", "mfe_180d_pct": 23.75, "mae_180d_pct": -11.98, "mfe_180d_high": 2840, "mae_180d_low": 2020, "mfe_180d_high_date": "2024-07-24", "mae_180d_low_date": "2025-03-27", "window_180_truncated_by_delisting_or_available_data": false, "last_available_price_date_for_window": "2025-04-17", "current_profile_interpretation": "Local-4B/Stage3 if price spike treated as governance premium unlock", "outcome": "counterexample_high_mae", "source_note": "source_proxy_only / evidence_url_pending=true; stock-web 2024/2025 row 확인"}
```

## 11. Raw component score breakdown

```jsonl
{"row_type": "score_simulation", "profile_proxy": "e2r_2_1_stock_web_calibrated", "symbol": "003410", "name": "쌍용C&E", "trigger_type": "Stage2_Actionable", "component_scores": {"EPS": 2, "Visibility": 16, "Bottleneck": 2, "Mispricing": 18, "Valuation": 19, "Capital": 13, "Info": 4, "total": 74}, "score_sum": 74, "stage2_actionable_evidence_bonus_applied": true, "stage3_yellow_total_min": 75, "stage3_green_total_min": 87, "stage3_green_revision_min": 55, "pre_shadow_profile_decision": "stage2_actionable_only", "post_shadow_decision": "block_green_and_route_to_tender_cap_watch", "reason": "C32 tender/go-private cap transforms upside into cash-bridge spread; residual upside must be measured against tender cap, not generic valuation rerating"}
{"row_type": "score_simulation", "profile_proxy": "e2r_2_1_stock_web_calibrated", "symbol": "115390", "name": "락앤락", "trigger_type": "Stage3_Yellow", "component_scores": {"EPS": 1, "Visibility": 17, "Bottleneck": 2, "Mispricing": 20, "Valuation": 20, "Capital": 13, "Info": 4, "total": 77}, "score_sum": 77, "stage2_actionable_evidence_bonus_applied": true, "stage3_yellow_total_min": 75, "stage3_green_total_min": 87, "stage3_green_revision_min": 55, "pre_shadow_profile_decision": "would_allow_yellow_or_local_4b_watch", "post_shadow_decision": "block_green_and_route_to_tender_cap_watch", "reason": "C32 tender/go-private cap transforms upside into cash-bridge spread; residual upside must be measured against tender cap, not generic valuation rerating"}
{"row_type": "score_simulation", "profile_proxy": "e2r_2_1_stock_web_calibrated", "symbol": "119860", "name": "커넥트웨이브", "trigger_type": "Stage2_Actionable", "component_scores": {"EPS": 1, "Visibility": 18, "Bottleneck": 3, "Mispricing": 19, "Valuation": 20, "Capital": 13, "Info": 4, "total": 78}, "score_sum": 78, "stage2_actionable_evidence_bonus_applied": true, "stage3_yellow_total_min": 75, "stage3_green_total_min": 87, "stage3_green_revision_min": 55, "pre_shadow_profile_decision": "would_allow_yellow_or_local_4b_watch", "post_shadow_decision": "block_green_and_route_to_tender_cap_watch", "reason": "C32 tender/go-private cap transforms upside into cash-bridge spread; residual upside must be measured against tender cap, not generic valuation rerating"}
{"row_type": "score_simulation", "profile_proxy": "e2r_2_1_stock_web_calibrated", "symbol": "005390", "name": "신성통상", "trigger_type": "Local_4B_Watch", "component_scores": {"EPS": 1, "Visibility": 12, "Bottleneck": 3, "Mispricing": 20, "Valuation": 19, "Capital": 10, "Info": 5, "total": 70}, "score_sum": 70, "stage2_actionable_evidence_bonus_applied": true, "stage3_yellow_total_min": 75, "stage3_green_total_min": 87, "stage3_green_revision_min": 55, "pre_shadow_profile_decision": "stage2_actionable_only", "post_shadow_decision": "block_green_and_route_to_tender_cap_watch", "reason": "C32 tender/go-private cap transforms upside into cash-bridge spread; residual upside must be measured against tender cap, not generic valuation rerating"}
```

## 12. Aggregate / shadow-weight / residual rows

```jsonl
{"row_type": "aggregate", "round": "R12", "loop": 101, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 4, "reused_case_count": 0, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "calibration_usable_trigger_count": 4, "positive_case_count": 1, "mixed_positive_count": 2, "counterexample_count": 1, "local_4b_watch_count": 3, "current_profile_error_count": 4, "static_index_rows_before": 3, "static_index_rows_after_if_accepted": 7, "still_need_to_30": 23}
{"row_type": "shadow_weight", "rule_id": "C32_GOVERNANCE_TENDER_CAP_GUARD_V1", "scope": "canonical_archetype_id:C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "production_scoring_changed": false, "shadow_weight_only": true, "proposed_axis_positive": ["control_premium_cash_bridge_required", "tender_price_remaining_spread_required", "delisting_completion_probability_required"], "proposed_axis_guard": ["tender_price_cap_blocks_green", "post_cap_late_chase_mfe_penalty", "minority_acceptance_uncertain_high_mae_guard"], "do_not_propose_new_weight_delta": false}
{"row_type": "residual_contribution", "label": "canonical_archetype_rule_candidate", "new_axis_proposed": "C32_tender_price_cap_blocks_green | C32_minority_holder_acceptance_high_MAE_guard | C32_control_premium_cash_bridge_required", "existing_axis_strengthened": "price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail", "existing_axis_weakened": null, "next_recommended_archetypes": ["C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "C15_MATERIAL_SPREAD_SUPERCYCLE", "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "C22_INSURANCE_RATE_CYCLE_RESERVE"]}
```


## 13. Deferred Coding Agent Handoff Prompt

```text
Do not execute this in the research session.

You are a coding agent working in Songdaiki/stock_agent after the research MDs have been collected.

Goal:
- Add a canonical-archetype-specific shadow rule candidate for:
  C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
- Do not change production scoring immediately.
- Add tests/fixtures only if the existing calibration ingestion framework supports shadow rules.

Research file to ingest:
- e2r_stock_web_v12_residual_round_R12_loop_101_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Core proposed rule:
1. If a governance/control premium event has an identifiable tender/go-private cash price and current_price/tender_price >= 0.97, block Stage3-Green and route to tender_cap_watch unless remaining spread and completion-probability evidence are explicit.
2. If minority-holder acceptance, revised offer risk, or delisting completion risk is uncertain, add high_MAE_guard and avoid positive upgrade from price spike alone.
3. Preserve C32 as a separate branch from generic valuation/mispricing rerating.

Do not:
- patch production scoring without batch approval
- infer brokerage/live-trading behavior
- use non-stock-web price sources for the historical trigger rows
```

## 14. Final residual contribution summary

```text
selected_round = R12
selected_loop = 101
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
new_independent_case_count = 4
reused_case_count = 0
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 1
current_profile_error_count = 4
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C32_tender_price_cap_blocks_green | C32_minority_holder_acceptance_high_MAE_guard | C32_control_premium_cash_bridge_required
```
