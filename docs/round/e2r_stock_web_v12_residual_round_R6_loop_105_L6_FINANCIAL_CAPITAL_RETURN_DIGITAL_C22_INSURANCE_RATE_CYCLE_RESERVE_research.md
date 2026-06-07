# E2R v12 Residual Research — R6 / L6 / C22 Insurance Rate Cycle Reserve

```text
file_name = e2r_stock_web_v12_residual_round_R6_loop_105_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R6
selected_loop = 105
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = NONLIFE_INSURANCE_VALUEUP_RATE_CYCLE_RESERVE_QUALITY_BRIDGE_VS_SMALL_INSURER_AND_MA_THEME_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale

C22는 No-Repeat Index에서 `rows=42`, `need_to_50=8`인 Priority 1 구역이다. 직전 C22 산출물은 삼성화재, DB손해보험, 현대해상 위주였으므로 이번 run은 `메리츠금융지주 / 한화손해보험 / 흥국화재 / 롯데손해보험`으로 새 symbol set을 잡았다.

공통 historical trigger는 2024-02-28 Korea Corporate Value-up Programme 후속 강화 기대다. 이 trigger는 보험주와 금융주 전반에 한 번에 불을 붙인 난로 같은 역할을 했지만, C22의 진짜 판별 포인트는 “불꽃이 있었다”가 아니라 그 열이 reserve quality, loss ratio, capital buffer, shareholder return policy로 오래 전달됐는지다.

## 2. Validation scope

```text
validation_scope = historical_trigger_level
current_candidate_scan = false
live_watchlist = false
brokerage_or_auto_trade = false
price_route_hunt = false
stock_agent_code_patch = false
```

Stock-web `tradable_raw` shard만 사용했다. Raw/unadjusted OHLC이므로 corporate action contamination은 profile 기준으로 차단 대상이나, 이번 2024 entry windows에서 profile상 직접 차단 사유는 발견하지 않았다.

## 3. Case summary

| case | ticker | entry | peak / MFE | trough / MAE | classification |
|---|---:|---:|---:|---:|---|
| Meritz Financial | 138040 | 2024-02-29 / 83,100 | 2024-10-21 / 107,200 / +29.00% | 2024-04-17 / 72,800 / -12.39% | positive_high_MAE_watch |
| Hanwha General Insurance | 000370 | 2024-02-29 / 4,800 | 2024-09-05 / 5,870 / +22.29% | 2024-04-11 / 4,205 / -12.40% | positive_high_MAE_watch |
| Heungkuk Fire & Marine | 000540 | 2024-02-29 / 4,905 | 2024-03-15 / 4,935 / +0.61% | 2024-11-15 / 3,200 / -34.76% | hard_counterexample_low_MFE_high_MAE |
| Lotte Non-Life | 000400 | 2024-02-29 / 2,860 | 2024-06-21 / 4,075 / +42.48% | 2024-11-20 / 1,909 / -33.25% | counterexample_high_MFE_hard_fade_MA_contaminated |

## 4. Case notes

### 4.1 138040 메리츠금융지주 — positive, but not free Green

Meritz had a clean directional response. Entry at 83,100 on 2024-02-29 eventually reached 107,200 on 2024-10-21. However, the path first moved through a 72,800 low on 2024-04-17. That means the event had enough fuel for MFE, but the drawdown says C22 should not treat “insurance + value-up” as a clean Green bridge by itself.

Interpretation:

```text
keep = positive C22 route
block = immediate Stage3-Green on headline/price alone
require = reserve quality + capital return policy + loss-ratio/K-ICS evidence
```

### 4.2 000370 한화손해보험 — small-insurer beta can work, but only as watch

Hanwha General Insurance reached +22.29% MFE from the same entry date, but its early -12.40% MAE means this is not a quiet compounding path. In E2R terms, this is a spring that stretches both ways. It is useful as a Stage2-Actionable watch candidate, not as a blind Green confirmation.

### 4.3 000540 흥국화재 — same label, almost no MFE

Heungkuk Fire is the cleanest false-positive in this batch. Entry at 4,905 produced only +0.61% MFE before sliding into a -34.76% 180D MAE and -40% full-window drawdown. This is the case that prevents a broad “all insurers benefit from value-up” rule.

### 4.4 000400 롯데손해보험 — high MFE but contaminated by theme/M&A/fade

Lotte Non-Life produced +42.48% MFE, but the same path later printed -33.25% 180D MAE and an even lower full-window trough. This is not a durable reserve-cycle proof. It is closer to M&A/theme beta plus price-only overheat, then 4C-like fade.

## 5. Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff globally, but C22 still needs a canonical-specific separator.

Residual failure pattern:

```text
insurance_valueup_label + low_PBR_or_small_insurer_beta
    -> can produce local MFE
    -> but without reserve quality / loss ratio / capital buffer / explicit capital-return bridge
    -> frequently becomes high-MAE or full-window 4C
```

The calibrated profile should therefore avoid scoring “insurance sector + value-up headline” as a sufficient Stage2-Actionable proof. It needs bridge evidence, not just the ticker sitting in the right sector.

## 6. Proposed shadow rule

```text
new_axis_proposed =
  c22_reserve_quality_capital_return_loss_ratio_bridge_required_for_stage2_actionable_shadow_only

rule =
  For C22 candidates, do not promote above Stage2 unless at least two of the following
  are present:
    1. reserve quality / reserve release or reserve adequacy evidence
    2. loss ratio or combined ratio improvement evidence
    3. capital buffer / K-ICS / solvency evidence
    4. explicit shareholder return policy, buyback, dividend, cancellation, or payout bridge
    5. durable rate-cycle underwriting margin evidence

downgrade =
  small-insurer beta spike, M&A/sale rumor, and value-up sympathy without quality bridge
  should route to Stage2-watch, 4B-watch, or 4C depending on MAE and thesis break.
```

## 7. Machine-readable rows

### 7.1 case rows

```jsonl
{"row_type": "case", "case_id": "C22_R6L105_138040_MERITZ_VALUEUP_INSURANCE_CAPITAL_RETURN", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_INSURANCE_VALUEUP_RATE_CYCLE_RESERVE_QUALITY_BRIDGE_VS_SMALL_INSURER_AND_MA_THEME_FALSE_POSITIVE", "ticker": "138040", "name": "메리츠금융지주", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 83100, "peak_date_180d": "2024-10-21", "peak_price_180d": 107200, "mfe_180d_pct": 29.0, "trough_date_180d": "2024-04-17", "trough_price_180d": 72800, "mae_180d_pct": -12.39, "classification": "positive_high_MAE_watch", "trigger_family": "valueup_insurance_capital_return_quality_bridge", "calibration_usable": true, "duplicate_status": "new_symbol_trigger_family_not_in_current_session_outputs", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "notes": "보험/금융지주 capital return proxy는 강한 MFE를 만들었지만 early MAE가 커서 reserve quality + capital return bridge 없이는 Green 자동승격 금지."}
{"row_type": "case", "case_id": "C22_R6L105_000370_HANWHA_GI_VALUEUP_SMALL_INSURER_HIGH_MAE", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_INSURANCE_VALUEUP_RATE_CYCLE_RESERVE_QUALITY_BRIDGE_VS_SMALL_INSURER_AND_MA_THEME_FALSE_POSITIVE", "ticker": "000370", "name": "한화손해보험", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 4800, "peak_date_180d": "2024-09-05", "peak_price_180d": 5870, "mfe_180d_pct": 22.29, "trough_date_180d": "2024-04-11", "trough_price_180d": 4205, "mae_180d_pct": -12.4, "classification": "positive_high_MAE_watch", "trigger_family": "small_nonlife_valueup_rate_cycle_reserve_quality_watch", "calibration_usable": true, "duplicate_status": "new_symbol_trigger_family_not_in_current_session_outputs", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "notes": "소형 손보주는 value-up/rate-cycle 수혜로 MFE가 열렸지만 MAE가 두 자릿수라 reserve quality와 자본정책 검증 없이 Green은 과하다."}
{"row_type": "case", "case_id": "C22_R6L105_000540_HEUNGKUK_VALUEUP_LOW_MFE_RESERVE_QUALITY_FAIL", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_INSURANCE_VALUEUP_RATE_CYCLE_RESERVE_QUALITY_BRIDGE_VS_SMALL_INSURER_AND_MA_THEME_FALSE_POSITIVE", "ticker": "000540", "name": "흥국화재", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 4905, "peak_date_180d": "2024-03-15", "peak_price_180d": 4935, "mfe_180d_pct": 0.61, "trough_date_180d": "2024-11-15", "trough_price_180d": 3200, "mae_180d_pct": -34.76, "classification": "hard_counterexample_low_MFE_high_MAE", "trigger_family": "small_nonlife_valueup_label_without_quality_bridge", "calibration_usable": true, "duplicate_status": "new_symbol_trigger_family_not_in_current_session_outputs", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "notes": "같은 value-up/보험 라벨이지만 forward MFE가 거의 없고 full-window hard fade가 뚜렷하다.", "full_window_trough_date": "2024-12-09", "full_window_trough_price": 2930, "full_window_mae_pct": -40.27}
{"row_type": "case", "case_id": "C22_R6L105_000400_LOTTE_NONLIFE_MA_THEME_HIGH_MFE_HARD_FADE", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "NONLIFE_INSURANCE_VALUEUP_RATE_CYCLE_RESERVE_QUALITY_BRIDGE_VS_SMALL_INSURER_AND_MA_THEME_FALSE_POSITIVE", "ticker": "000400", "name": "롯데손해보험", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 2860, "peak_date_180d": "2024-06-21", "peak_price_180d": 4075, "mfe_180d_pct": 42.48, "trough_date_180d": "2024-11-20", "trough_price_180d": 1909, "mae_180d_pct": -33.25, "classification": "counterexample_high_MFE_hard_fade_MA_contaminated", "trigger_family": "insurance_valueup_MA_theme_contamination_without_reserve_quality", "calibration_usable": true, "duplicate_status": "new_symbol_trigger_family_not_in_current_session_outputs", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "notes": "MFE는 컸지만 이후 급격한 full-window 4C 경로. 보험 rate/reserve가 아니라 M&A/price-only 테마가 섞인 경로로 분리해야 한다.", "full_window_trough_date": "2024-12-09", "full_window_trough_price": 1814, "full_window_mae_pct": -36.57}
```

### 7.2 trigger rows

```jsonl
{"row_type": "trigger", "case_id": "C22_R6L105_138040_MERITZ_VALUEUP_INSURANCE_CAPITAL_RETURN", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "ticker": "138040", "trigger_type": "valueup_insurance_capital_return_quality_bridge", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 83100, "entry_rule": "next_tradable_close_after_verified_macro_policy_trigger", "trigger_source_url": "https://www.reuters.com/markets/asia/skorea-considering-penalties-firms-failing-boost-shareholder-return-2024-02-28/", "stock_web_profile_path": "atlas/symbol_profiles/138/138040.json", "stock_web_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv"}
{"row_type": "trigger", "case_id": "C22_R6L105_000370_HANWHA_GI_VALUEUP_SMALL_INSURER_HIGH_MAE", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "ticker": "000370", "trigger_type": "small_nonlife_valueup_rate_cycle_reserve_quality_watch", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 4800, "entry_rule": "next_tradable_close_after_verified_macro_policy_trigger", "trigger_source_url": "https://www.reuters.com/markets/asia/skorea-considering-penalties-firms-failing-boost-shareholder-return-2024-02-28/", "stock_web_profile_path": "atlas/symbol_profiles/000/000370.json", "stock_web_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv"}
{"row_type": "trigger", "case_id": "C22_R6L105_000540_HEUNGKUK_VALUEUP_LOW_MFE_RESERVE_QUALITY_FAIL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "ticker": "000540", "trigger_type": "small_nonlife_valueup_label_without_quality_bridge", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 4905, "entry_rule": "next_tradable_close_after_verified_macro_policy_trigger", "trigger_source_url": "https://www.reuters.com/markets/asia/skorea-considering-penalties-firms-failing-boost-shareholder-return-2024-02-28/", "stock_web_profile_path": "atlas/symbol_profiles/000/000540.json", "stock_web_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv"}
{"row_type": "trigger", "case_id": "C22_R6L105_000400_LOTTE_NONLIFE_MA_THEME_HIGH_MFE_HARD_FADE", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "ticker": "000400", "trigger_type": "insurance_valueup_MA_theme_contamination_without_reserve_quality", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 2860, "entry_rule": "next_tradable_close_after_verified_macro_policy_trigger", "trigger_source_url": "https://www.reuters.com/markets/asia/skorea-considering-penalties-firms-failing-boost-shareholder-return-2024-02-28/", "stock_web_profile_path": "atlas/symbol_profiles/000/000400.json", "stock_web_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv"}
```

### 7.3 score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "C22_R6L105_138040_MERITZ_VALUEUP_INSURANCE_CAPITAL_RETURN", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"event_strength": 12, "sector_alignment": 13, "revision_or_capital_return_bridge": 7, "price_action": 12, "risk_penalty": -4, "source_quality_penalty": -2}, "simulated_old_stage": "Stage2_or_Stage2_Actionable_candidate", "simulated_shadow_stage_after_c22_rule": "Stage2-Actionable", "current_profile_error": "over_green_risk_if_price_only_MFE_is_treated_as_quality_bridge", "new_shadow_axis": "c22_reserve_quality_capital_return_loss_ratio_bridge_required_for_stage2_actionable"}
{"row_type": "score_simulation", "case_id": "C22_R6L105_000370_HANWHA_GI_VALUEUP_SMALL_INSURER_HIGH_MAE", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"event_strength": 12, "sector_alignment": 13, "revision_or_capital_return_bridge": 7, "price_action": 12, "risk_penalty": -4, "source_quality_penalty": -2}, "simulated_old_stage": "Stage2_or_Stage2_Actionable_candidate", "simulated_shadow_stage_after_c22_rule": "Stage2-Actionable", "current_profile_error": "over_green_risk_if_price_only_MFE_is_treated_as_quality_bridge", "new_shadow_axis": "c22_reserve_quality_capital_return_loss_ratio_bridge_required_for_stage2_actionable"}
{"row_type": "score_simulation", "case_id": "C22_R6L105_000540_HEUNGKUK_VALUEUP_LOW_MFE_RESERVE_QUALITY_FAIL", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"event_strength": 8, "sector_alignment": 13, "revision_or_capital_return_bridge": 2, "price_action": 3, "risk_penalty": -8, "source_quality_penalty": -2}, "simulated_old_stage": "Stage2_or_Stage2_Actionable_candidate", "simulated_shadow_stage_after_c22_rule": "4C_or_reject", "current_profile_error": "false_positive_if_insurance_valueup_label_gets_stage2_without_reserve_quality", "new_shadow_axis": "c22_reserve_quality_capital_return_loss_ratio_bridge_required_for_stage2_actionable"}
{"row_type": "score_simulation", "case_id": "C22_R6L105_000400_LOTTE_NONLIFE_MA_THEME_HIGH_MFE_HARD_FADE", "current_profile_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"event_strength": 8, "sector_alignment": 13, "revision_or_capital_return_bridge": 2, "price_action": 12, "risk_penalty": -8, "source_quality_penalty": -2}, "simulated_old_stage": "Stage2_or_Stage2_Actionable_candidate", "simulated_shadow_stage_after_c22_rule": "4C_or_reject", "current_profile_error": "false_positive_if_insurance_valueup_label_gets_stage2_without_reserve_quality", "new_shadow_axis": "c22_reserve_quality_capital_return_loss_ratio_bridge_required_for_stage2_actionable"}
```

### 7.4 aggregate row

```jsonl
{"row_type": "aggregate", "selected_round": "R6", "selected_loop": 105, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 4, "dedup_key_rule": "canonical_archetype_id + ticker + trigger_type + entry_date", "dedup_keys": ["C22_INSURANCE_RATE_CYCLE_RESERVE|138040|valueup_insurance_capital_return_quality_bridge|2024-02-29", "C22_INSURANCE_RATE_CYCLE_RESERVE|000370|small_nonlife_valueup_rate_cycle_reserve_quality_watch|2024-02-29", "C22_INSURANCE_RATE_CYCLE_RESERVE|000540|small_nonlife_valueup_label_without_quality_bridge|2024-02-29", "C22_INSURANCE_RATE_CYCLE_RESERVE|000400|insurance_valueup_MA_theme_contamination_without_reserve_quality|2024-02-29"], "coverage_gap_basis": "No-Repeat Index static C22 rows=42 need_to_50=8; this run adds four non-overlapping symbol/trigger combinations."}
```

### 7.5 shadow weight row

```jsonl
{"row_type": "shadow_weight", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_axis_proposed": "c22_reserve_quality_capital_return_loss_ratio_bridge_required_for_stage2_actionable_shadow_only", "direction": "block_or_downgrade", "production_scoring_changed": false, "shadow_weight_only": true, "rule_text": "C22 보험 rate/value-up 후보는 price MFE나 value-up headline만으로 Stage2-Actionable 이상으로 올리지 않는다. reserve quality, loss ratio, K-ICS/capital buffer, shareholder return policy 중 최소 2개 bridge가 있어야 Stage2-Actionable을 허용한다. M&A/sale rumor와 small-insurer beta spike는 separate 4B/4C watch로 라우팅한다."}
```

### 7.6 residual contribution row

```jsonl
{"row_type": "residual_contribution", "loop_contribution_label": "canonical_archetype_rule_candidate", "residual_error_pattern": "small_insurer_valueup_or_MA_theme_can_create_MFE_without_durable_reserve_quality_bridge", "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to C22 insurance rate/value-up rallies", "existing_axis_weakened": null}
```

## 8. Residual contribution summary

```text
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 2
counterexample_count = 2
current_profile_error_count = 4
verified_url_repair_needed_count = 3
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation coding agent. Do not rerun live scans.
Read this standalone Markdown together with other v12 residual research MD files.
Extract only machine-readable rows under section 7.
Do not treat this file as production scoring by itself.
Batch-ingest the case / trigger / score_simulation / aggregate / shadow_weight /
residual_contribution rows into the v12 calibration research artifact layer.
Then evaluate whether the proposed C22 shadow-only axis should become a
profile rule after enough independent C22 cases accumulate.

Candidate axis:
c22_reserve_quality_capital_return_loss_ratio_bridge_required_for_stage2_actionable_shadow_only

Implementation caution:
- Do not add ticker-specific rules.
- Do not punish all small insurers automatically.
- Use the rule only as a bridge requirement for Stage2-Actionable or above.
- Keep M&A/sale-rumor contamination separate from true insurance reserve/rate-cycle evidence.
```
