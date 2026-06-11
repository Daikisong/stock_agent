# E2R v12 Sector-Archetype Residual Research — R1 Loop 106 / C05 EPC Mega Contract Margin Gap

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 106
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = EPC_MEGA_CONTRACT_ORDERBOOK_COST_OVERRUN_MARGIN_BRIDGE_VS_PRICE_ONLY_ORDER_HEADLINE
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection basis

이번 실행은 `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`의 v12 절차를 그대로 따른다. 해당 프롬프트는 현재/live 종목 탐색이나 `stock_agent` 코드 패치가 아니라, `Songdaiki/stock-web`의 실제 1D OHLCV row로 과거 trigger-level residual research Markdown을 만드는 절차다. 핵심 제약은 `must_use_actual_stock_web_1D_OHLC=true`, `must_include_backtest_result=true`, `must_include_complete_30_90_180_mfe_mae_in_every_trigger_row=true`, `production_scoring_changed=false`, `shadow_weight_only=true`다.

No-Repeat 기준으로 C05는 Priority 0에 남아 있다.

```text
static_index_row = C05_EPC_MEGA_CONTRACT_MARGIN_GAP | rows=13 | need_to_30=17 | 조사 포인트=EPC mega 계약, 원가초과, working capital, margin gap
conversation_local_prior_c05 = 0
this_pass_adds = 4
if_accepted_static_gap = 13 -> 17
still_priority_0 = true
```

이번 산출물은 C05의 핵심 오류, 즉 **EPC/플랜트/건설 수주 헤드라인이 가격으로 먼저 튀지만 실제 프로젝트 마진·원가초과·working capital이 뒤따르지 않으면 4B/Stage3 신호가 오래 버티지 못하는 문제**를 겨냥한다.  

## 2. Validation scope and caveat

가격 경로는 `Songdaiki/stock-web`의 symbol-year CSV shard에서 확인했다. 비가격 이벤트는 이번 실행에서 외부 공시/뉴스 URL 검증을 새로 뚫지 않고 `source_proxy_only / evidence_url_pending=true`로 낮은 신뢰 버킷에 둔다. 따라서 이 MD의 용도는 production 반영이 아니라 batch coding agent가 나중에 여러 MD를 모아 검토할 수 있는 residual calibration handoff다.

사용한 가격 shard:

| symbol | name | stock-web profile | 2024 shard | caveat |
|---|---|---|---|---|
| 000720 | 현대건설 | `atlas/symbol_profiles/000/000720.json` | `atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv` | raw_unadjusted_marcap |
| 006360 | GS건설 | `atlas/symbol_profiles/006/006360.json` | `atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv` + 2025 continuation | raw_unadjusted_marcap |
| 028050 | 삼성E&A | `atlas/symbol_profiles/028/028050.json` | `atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv` | name changed from 삼성엔지니어링 to 삼성E&A in 2024 |
| 375500 | DL이앤씨 | `atlas/symbol_profiles/375/375500.json` | `atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv` | raw_unadjusted_marcap |

## 3. Core finding

C05는 단순 수주잔고형 C01과 닮았지만, 엔진은 다르다. C01은 "물량이 쌓였고 그 물량이 매출·마진·FCF로 흘러가는가"가 핵심이다. C05는 거기에 **원가초과와 working capital이라는 누수 밸브**가 하나 더 붙어 있다. EPC 프로젝트는 수주가 물탱크에 물을 붓는 행위라면, 원가·클레임·납기 지연은 밑바닥에 생긴 구멍이다. 수주액만 보면 물이 차오르는 듯 보이지만, 마진 브릿지가 없으면 실제 물높이는 올라가지 않는다.

따라서 C05는 다음과 같이 분리해야 한다.

```text
positive C05:
  order headline / backlog
  + cost-overrun containment
  + project gross margin or OPM revision
  + working-capital / cash conversion visibility
  + delivery schedule visibility
  = Stage3 candidate, sometimes after a painful MAE

false positive C05:
  order headline / EPC label / low-PBR contractor rebound
  + no margin bridge
  + no working-capital conversion
  + local 4B or price-only volume spike
  = Stage2-Watch or Reject
```

## 4. Case-level summary

| case | symbol | entry | result | 30d MFE/MAE | 90d MFE/MAE | 180d MFE/MAE | interpretation |
|---|---|---:|---|---:|---:|---:|---|
| Hyundai E&C mixed | 000720 | 2024-01-26 close 33,100 | mixed positive | +7.25 / -3.47 | +8.76 / -3.47 | +8.76 / -16.01 | early orderbook/contractor rerating worked, but long horizon faded without stronger margin/cash bridge |
| GS E&C repair positive | 006360 | 2024-04-30 close 16,480 | positive with high MAE | +1.46 / -12.32 | +31.98 / -12.32 | +31.98 / -12.32 | delayed positive only after repair/cost visibility; early entry suffered large MAE |
| Samsung E&A counter | 028050 | 2024-02-28 close 26,000 | counterexample | +8.27 / -7.88 | +8.27 / -16.92 | +8.27 / -36.42 | order/plant label and price spike failed without sustained margin bridge |
| DL E&C counter | 375500 | 2024-04-29 close 36,650 | counterexample | +7.78 / -9.82 | +7.78 / -21.28 | +7.78 / -21.28 | low-PBR/contractor rebound was not enough; margin/PF/working-capital drag dominated |

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger_row", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R1", "selected_loop": 106, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_ORDERBOOK_COST_OVERRUN_MARGIN_BRIDGE_VS_PRICE_ONLY_ORDER_HEADLINE", "case_id": "C05_R1L106_000720_2024_01_26_ORDERBOOK_MARGIN_MIXED", "symbol": "000720", "name": "현대건설", "trigger_type": "Stage2_Actionable", "entry_date": "2024-01-26", "entry_price": 33100.0, "entry_price_basis": "close", "price_source_repo": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "price_source_lines_proxy": ["turn786:L22-L44", "turn787:L3-L68", "turn799:L3-L69"], "mfe_30d_pct": 7.25, "mae_30d_pct": -3.47, "close_30d_pct": 1.96, "peak_30d_date": "2024-02-26", "trough_30d_date": "2024-01-26", "mfe_90d_pct": 8.76, "mae_90d_pct": -3.47, "close_90d_pct": 6.95, "peak_90d_date": "2024-05-09", "trough_90d_date": "2024-01-26", "mfe_180d_pct": 8.76, "mae_180d_pct": -16.01, "close_180d_pct": -9.21, "peak_180d_date": "2024-05-09", "trough_180d_date": "2024-10-25", "local_4b_proximity": true, "full_window_4b": false, "hard_4c": false, "outcome_label": "mixed_positive", "current_profile_error": "current profile can over-reward backlog/order headline without checking sustained gross margin and working-capital conversion; early 30/90d looks acceptable but 180d fades", "non_price_evidence_status": "source_proxy_only", "evidence_url_pending": true}
{"row_type": "trigger_row", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R1", "selected_loop": 106, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_ORDERBOOK_COST_OVERRUN_MARGIN_BRIDGE_VS_PRICE_ONLY_ORDER_HEADLINE", "case_id": "C05_R1L106_006360_2024_04_30_COST_PROVISION_RECOVERY_POSITIVE", "symbol": "006360", "name": "GS건설", "trigger_type": "Stage2_Actionable", "entry_date": "2024-04-30", "entry_price": 16480.0, "entry_price_basis": "close", "price_source_repo": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv", "price_source_lines_proxy": ["turn790:L43-L71", "turn791:L3-L70", "turn792:L3-L70", "turn798:L4-L15"], "mfe_30d_pct": 1.46, "mae_30d_pct": -12.32, "close_30d_pct": -11.1, "peak_30d_date": "2024-04-30", "trough_30d_date": "2024-06-19", "mfe_90d_pct": 31.98, "mae_90d_pct": -12.32, "close_90d_pct": 24.39, "peak_90d_date": "2024-08-27", "trough_90d_date": "2024-06-19", "mfe_180d_pct": 31.98, "mae_180d_pct": -12.32, "close_180d_pct": 3.94, "peak_180d_date": "2024-08-27", "trough_180d_date": "2024-06-19", "local_4b_proximity": false, "full_window_4b": false, "hard_4c": false, "outcome_label": "positive_with_high_MAE", "current_profile_error": "positive path exists only after repair/cost visibility and balance-sheet stress begins to fade; naive stage2 at the first headline suffers a deep MAE before rerating", "non_price_evidence_status": "source_proxy_only", "evidence_url_pending": true}
{"row_type": "trigger_row", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R1", "selected_loop": 106, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_ORDERBOOK_COST_OVERRUN_MARGIN_BRIDGE_VS_PRICE_ONLY_ORDER_HEADLINE", "case_id": "C05_R1L106_028050_2024_02_28_PLANT_ORDER_MARGIN_GAP_COUNTER", "symbol": "028050", "name": "삼성E&A", "trigger_type": "Stage2_Actionable", "entry_date": "2024-02-28", "entry_price": 26000.0, "entry_price_basis": "close", "price_source_repo": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv", "price_source_lines_proxy": ["turn782:L43-L70", "turn783:L3-L70", "turn796:L3-L70"], "mfe_30d_pct": 8.27, "mae_30d_pct": -7.88, "close_30d_pct": -3.85, "peak_30d_date": "2024-03-15", "trough_30d_date": "2024-03-25", "mfe_90d_pct": 8.27, "mae_90d_pct": -16.92, "close_90d_pct": -7.69, "peak_90d_date": "2024-03-15", "trough_90d_date": "2024-06-18", "mfe_180d_pct": 8.27, "mae_180d_pct": -36.42, "close_180d_pct": -35.19, "peak_180d_date": "2024-03-15", "trough_180d_date": "2024-11-14", "local_4b_proximity": true, "full_window_4b": false, "hard_4c": false, "outcome_label": "counterexample", "current_profile_error": "order/plant/EPC label and temporary price extension can look actionable, but the absence of margin revision and cash-conversion bridge leaves a severe 180d drawdown", "non_price_evidence_status": "source_proxy_only", "evidence_url_pending": true}
{"row_type": "trigger_row", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R1", "selected_loop": 106, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_ORDERBOOK_COST_OVERRUN_MARGIN_BRIDGE_VS_PRICE_ONLY_ORDER_HEADLINE", "case_id": "C05_R1L106_375500_2024_04_29_EPC_LOW_PBR_REBOUND_COUNTER", "symbol": "375500", "name": "DL이앤씨", "trigger_type": "Stage2_Actionable", "entry_date": "2024-04-29", "entry_price": 36650.0, "entry_price_basis": "close", "price_source_repo": "Songdaiki/stock-web", "price_source_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "price_source_lines_proxy": ["turn794:L23-L44", "turn795:L3-L70", "turn797:L3-L70"], "mfe_30d_pct": 7.78, "mae_30d_pct": -9.82, "close_30d_pct": -3.95, "peak_30d_date": "2024-06-13", "trough_30d_date": "2024-05-30", "mfe_90d_pct": 7.78, "mae_90d_pct": -21.28, "close_90d_pct": -15.01, "peak_90d_date": "2024-06-13", "trough_90d_date": "2024-08-08", "mfe_180d_pct": 7.78, "mae_180d_pct": -21.28, "close_180d_pct": -16.37, "peak_180d_date": "2024-06-13", "trough_180d_date": "2024-08-08", "local_4b_proximity": true, "full_window_4b": false, "hard_4c": false, "outcome_label": "counterexample", "current_profile_error": "price-only contractor rebound and orderbook narrative does not separate EPC margin recovery from housing/PF and working-capital drag", "non_price_evidence_status": "source_proxy_only", "evidence_url_pending": true}
```

## 6. Score simulation JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C05_R1L106_000720_2024_01_26_ORDERBOOK_MARGIN_MIXED", "symbol": "000720", "trigger_type": "Stage2_Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"evidence_quality": 13, "actionability": 14, "revision_or_margin_bridge": 9, "price_structure": 15, "sector_context": 11, "risk_penalty": -3}, "simulated_total_before_shadow": 75, "simulated_stage_before_shadow": "Stage3_Yellow", "shadow_rule_delta": -4, "simulated_total_after_shadow": 71, "simulated_stage_after_shadow": "Stage2_Watch", "proposed_shadow_rule": "C05_EPC_MARGIN_BRIDGE_REQUIRED_AND_COST_OVERRUN_GUARD"}
{"row_type": "score_simulation", "case_id": "C05_R1L106_006360_2024_04_30_COST_PROVISION_RECOVERY_POSITIVE", "symbol": "006360", "trigger_type": "Stage2_Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"evidence_quality": 16, "actionability": 14, "revision_or_margin_bridge": 14, "price_structure": 13, "sector_context": 11, "risk_penalty": -2}, "simulated_total_before_shadow": 78, "simulated_stage_before_shadow": "Stage3_Yellow", "shadow_rule_delta": 3, "simulated_total_after_shadow": 81, "simulated_stage_after_shadow": "Stage3_Yellow_delayed_until_margin_bridge", "proposed_shadow_rule": "C05_EPC_MARGIN_BRIDGE_REQUIRED_AND_COST_OVERRUN_GUARD"}
{"row_type": "score_simulation", "case_id": "C05_R1L106_028050_2024_02_28_PLANT_ORDER_MARGIN_GAP_COUNTER", "symbol": "028050", "trigger_type": "Stage2_Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"evidence_quality": 13, "actionability": 14, "revision_or_margin_bridge": 6, "price_structure": 15, "sector_context": 11, "risk_penalty": -5}, "simulated_total_before_shadow": 73, "simulated_stage_before_shadow": "Stage2_Actionable", "shadow_rule_delta": -7, "simulated_total_after_shadow": 66, "simulated_stage_after_shadow": "Watch_or_Reject", "proposed_shadow_rule": "C05_EPC_MARGIN_BRIDGE_REQUIRED_AND_COST_OVERRUN_GUARD"}
{"row_type": "score_simulation", "case_id": "C05_R1L106_375500_2024_04_29_EPC_LOW_PBR_REBOUND_COUNTER", "symbol": "375500", "trigger_type": "Stage2_Actionable", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"evidence_quality": 13, "actionability": 14, "revision_or_margin_bridge": 6, "price_structure": 15, "sector_context": 11, "risk_penalty": -5}, "simulated_total_before_shadow": 73, "simulated_stage_before_shadow": "Stage2_Actionable", "shadow_rule_delta": -7, "simulated_total_after_shadow": 66, "simulated_stage_after_shadow": "Watch_or_Reject", "proposed_shadow_rule": "C05_EPC_MARGIN_BRIDGE_REQUIRED_AND_COST_OVERRUN_GUARD"}
```

## 7. Aggregate row

```json
{
  "row_type": "aggregate",
  "selected_round": "R1",
  "selected_loop": 106,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "EPC_MEGA_CONTRACT_ORDERBOOK_COST_OVERRUN_MARGIN_BRIDGE_VS_PRICE_ONLY_ORDER_HEADLINE",
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "calibration_usable_case_count": 4,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 1,
  "mixed_positive_count": 1,
  "counterexample_count": 2,
  "local_4b_watch_count": 3,
  "current_profile_error_count": 4,
  "auto_selected_coverage_gap_static_index": "C05 rows 13 -> 17 if accepted; still Priority 0, need 13 to 30",
  "coverage_basis": "docs/core/V12_Research_No_Repeat_Index.md plus conversation-local generated MD ledger",
  "novel_symbols": [
    "000720",
    "006360",
    "028050",
    "375500"
  ],
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4
}
```

## 8. Shadow rule candidate

```json
{
  "row_type": "shadow_weight_candidate",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "production_scoring_changed": false,
  "do_not_propose_new_weight_delta": false,
  "shadow_rule_id": "C05_EPC_MARGIN_BRIDGE_REQUIRED_AND_COST_OVERRUN_GUARD",
  "rule_text": "For EPC / mega contract / plant-contractor labels, Stage3 promotion requires explicit bridge from order headline to project margin, cost-overrun containment, working-capital/cash conversion, and delivery schedule visibility. Price-only orderbook or low-PBR rebound remains Stage2-Watch unless non-price evidence confirms margin conversion.",
  "positive_adjustment": "+2 to +3 only when margin revision, cost provision clarity, or cash conversion improves after the order headline",
  "negative_adjustment": "-4 to -7 when orderbook grows but gross margin/OPM, provision, or working-capital evidence is absent; cap local 4B as Watch",
  "expected_effect": "preserve GS건설-style delayed positive while blocking 삼성E&A/DL이앤씨-style price-only orderbook false positives"
}
```

## 9. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C05_EPC_margin_working_capital_bridge_required | C05_cost_overrun_provision_guard | C05_price_only_orderbook_headline_cap | C05_high_MAE_delayed_positive_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

### What this adds

이번 C05 샘플의 정보량은 "EPC 수주가 있다/없다"가 아니다. 핵심은 **수주가 손익계산서와 현금흐름표로 건너가는 다리의 강도**다.

- 006360은 90d/180d에서 상승 여지가 있었지만, entry 직후 -12%대 MAE를 감수해야 했다. 즉 C05 positive는 빠른 Green보다 **delayed Yellow → margin/cost confirmation → Green 검토**가 더 안전하다.
- 028050과 375500은 local 4B 또는 가격 탄력만으로는 Stage3가 되면 안 된다. 수주/플랜트/저PBR contractor label은 **마진 bridge가 없을 때 사막의 신기루**처럼 사라진다.
- 000720은 30/90d는 양호하지만 180d에서 되밀렸다. 이 축은 중기 가격 반등만으로는 충분하지 않고, 계약 품질·원가·working capital을 분리해야 한다.

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the batch implementation agent for E2R 2.1 calibration.

Do not use this Markdown as a direct production patch. Treat it as one residual research input among many v12 MD files.

Task:
- Read the C05_EPC_MEGA_CONTRACT_MARGIN_GAP rows from this MD.
- Compare against other v12 C05/C01/C30/C31 residual files.
- If enough independent cases agree, implement only a shadow/canonical-archetype rule candidate, not a broad global scoring change.

Candidate rule:
C05_EPC_MARGIN_BRIDGE_REQUIRED_AND_COST_OVERRUN_GUARD

Proposed behavior:
1. For EPC / mega contract / plant contractor signals, require at least one non-price evidence bridge:
   - project gross margin or OPM revision,
   - cost-overrun/provision clarity,
   - working-capital/cash-conversion visibility,
   - delivery schedule/customer funding visibility.
2. If only order headline, backlog amount, EPC label, low-PBR rebound, or local 4B price action exists, cap at Stage2-Watch.
3. Allow delayed Stage3-Yellow/Green when price initially has high MAE but non-price evidence later confirms margin/cash bridge.
4. Preserve existing global guards:
   - price_only_blowoff_blocks_positive_stage = true
   - full_4b_requires_non_price_evidence = true
   - hard_4c_thesis_break_routes_to_4c = true

Do not change production scoring unless this rule is supported by multiple accepted MDs and aggregate tests.
```

## 11. Next recommended archetypes

```text
C24_BIO_TRIAL_DATA_EVENT_RISK
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
C19_BRAND_RETAIL_INVENTORY_MARGIN
C27_CONTENT_IP_GLOBAL_MONETIZATION
```

## 12. Run footer

```text
selected_round = R1
selected_loop = 106
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
price_source = Songdaiki/stock-web
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable case 수 = 4
calibration_usable trigger 수 = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4
auto_selected_coverage_gap_static_index = C05 rows 13 -> 17 if accepted; still Priority 0, need 13 to 30
source_proxy_only = true
evidence_url_pending = true
```
