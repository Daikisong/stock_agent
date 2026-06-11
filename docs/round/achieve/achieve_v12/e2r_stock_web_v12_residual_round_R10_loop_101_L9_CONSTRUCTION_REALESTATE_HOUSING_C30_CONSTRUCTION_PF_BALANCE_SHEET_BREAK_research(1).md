# E2R v12 Stock-Web Residual Research — R10 / Loop 101 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R10
selected_loop = 101
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = PF_BALANCE_SHEET_REPAIR_ORDERBOOK_CASHFLOW_BRIDGE_VS_LOW_PBR_REBOUND
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 0. Selection / No-Repeat

`V12_Research_No_Repeat_Index.md`의 Priority 0에서 `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`는 rows=3, need_to_30=27로 표시되어 있다. 기존 top-covered 조합은 `009410`, `034300`, `183190`이므로 이번 실행에서는 이를 피하고 `294870`, `006360`, `047040`, `375500` 네 개의 신규 C30 symbol을 사용했다.

이번 연구는 live 후보 탐색이 아니라, stock-web 1D OHLC row로 과거 trigger-level residual을 보강하는 C30 전용 샘플이다.

## 1. Research Question

C30은 단순한 건설주 반등이 아니다. PF/유동성/재무제표 hard break가 실제로 완화되고, 그것이 수주잔고의 질, margin normalization, working-capital/cash conversion으로 이어질 때만 positive로 볼 수 있다.

비유하면 건설주는 겉으로는 같은 철골 구조처럼 보여도, 한쪽은 기초공사가 말라 굳는 중이고 다른 한쪽은 지하수 압력이 그대로 남아 있다. 가격은 둘 다 튀지만, cash bridge가 없는 가격 반등은 물기 많은 콘크리트처럼 시간이 지나며 균열이 올라온다.

## 2. Coverage Contribution

| metric | value |
|---|---:|
| selected_priority_bucket | Priority 0 |
| static_index_rows_before | 3 |
| expected_rows_after_acceptance | 7 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 4 |
| calibration_usable_trigger_count | 4 |
| positive_case_count | 1 |
| mixed_positive_count | 1 |
| counterexample_count | 2 |
| local_4b_watch_count | 3 |
| current_profile_error_count | 4 |

## 3. Source Validation

All price rows were checked from `Songdaiki/stock-web` 1D tradable shards.

| symbol | name | profile status | source shard |
|---|---|---|---|
| 294870 | HDC현대산업개발 | active_like, raw_unadjusted_marcap | `atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv` |
| 006360 | GS건설 | active_like, raw_unadjusted_marcap | `atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv` |
| 047040 | 대우건설 | active_like, raw_unadjusted_marcap | `atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv` |
| 375500 | DL이앤씨 | active_like, raw_unadjusted_marcap | `atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv` |

Caveat: 비가격 evidence는 이번 MD에서 `source_proxy_only / evidence_url_pending=true`로 낮은 신뢰 버킷에 둔다. 이 MD의 강한 근거는 가격 경로와 residual behavior이며, coding-agent batch 반영 전에는 각 케이스의 PF/유동성/현금흐름 원문 evidence URL을 별도 보강해야 한다.

## 4. Trigger-Level Results

| symbol | entry_date | entry_price | classification | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | residual reading |
|---|---:|---:|---|---:|---:|---:|---|
| 294870 | 2024-01-26 | 17,530 | mixed_positive | +18.37% / -8.33% | +18.37% / -11.58% | +60.87% / -11.58% | PF repair + orderbook relief can work, but volatility says Green promotion needs cash bridge |
| 006360 | 2024-04-29 | 15,640 | positive | +6.91% / -6.71% | +39.07% / -7.61% | +39.07% / -7.61% | true repair path; margin/cash bridge needed to separate from generic construction beta |
| 047040 | 2024-07-15 | 4,260 | counterexample | +16.55% / -13.73% | +16.55% / -20.77% | +16.55% / -20.77% | event spike looked actionable but later MAE showed lack of durable bridge |
| 375500 | 2024-04-29 | 36,650 | counterexample | +2.32% / -10.10% | +7.78% / -21.28% | +7.78% / -21.28% | low-PBR/balance-sheet label without revision follow-through failed |

## 5. Case Notes

### 5.1 HDC현대산업개발 / 294870 — mixed positive

Entry was set at 2024-01-26 close 17,530. The stock-web row sequence shows a fast 30D/90D MFE into 20,750 and later 180D peak at 28,200. However, the path first went through a double-digit drawdown. This is not a pure false positive, but it is not a clean Green either. The C30 rule should require the non-price story to show actual PF/liquidity repair and project cash conversion before allowing full promotion.

### 5.2 GS건설 / 006360 — positive

Entry was set at 2024-04-29 close 15,640. The path had limited early downside and then expanded to a 21,750 peak. This is the cleanest C30 positive in the batch: the price action looks like the market was beginning to pay for repair, not merely for low valuation. The rule lesson is not “raise all builders”; it is “raise only if repair links to backlog quality, margin normalization, and cash conversion.”

### 5.3 대우건설 / 047040 — counterexample

Entry was set at 2024-07-15 close 4,260. The path produced a high local MFE via a short event spike, but the later 90D/180D MAE reached roughly -20.77%. This is the exact C30 trap: price heat compresses the chart like a spring, but if the PF/cash bridge is not real, the spring gives back the move.

### 5.4 DL이앤씨 / 375500 — counterexample

Entry was set at 2024-04-29 close 36,650. Despite a short positive wiggle, 90D/180D downside dominated. This row argues for blocking low-PBR construction labels from becoming positive unless revision and cashflow evidence arrive.

## 6. Current Calibrated Profile Stress Test

The current v12 profile already blocks many price-only 4B rows, but C30 needs its own rule because construction/PF cases can look deceptively “fundamental” even when the only actual evidence is low valuation plus sector rebound.

Residual errors found:

1. **False Green risk**: if PF headline, low valuation, and price recovery are scored as three separate evidence strands, the model can double-count the same mean-reversion story.
2. **Local 4B under-detection**: a 30D MFE spike in construction names can be a short-covering/relief burst rather than balance-sheet repair.
3. **Cash bridge missingness**: C30 should not be positive unless debt maturity, working capital, margin normalization, and orderbook quality form one chain.
4. **Long-window MAE dominates**: 047040 and 375500 show that early MFE is insufficient without 90/180D holding quality.

## 7. Proposed Shadow Rule

```text
C30_pf_balance_sheet_hard_break_vs_repair_bridge_required = true

Positive/Green promotion requires:
- explicit PF/liquidity risk relief or balance-sheet repair evidence,
- refinancing/maturity/working-capital pressure improvement,
- orderbook quality and margin normalization,
- cash conversion or FCF path,
- no dominant price-only event spike.

If only low-PBR, construction beta, policy headline, or short squeeze:
- cap at Stage2 or Stage2-Actionable,
- route to local_4B_watch when 30D MFE is high but 90/180D MAE risk is unresolved,
- block Green even when total score clears generic threshold.
```

## 8. Machine-Readable JSONL

```jsonl
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R10", "selected_loop": 101, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_REPAIR_ORDERBOOK_CASHFLOW_BRIDGE_VS_LOW_PBR_REBOUND", "symbol": "294870", "name": "HDC현대산업개발", "market": "KOSPI", "trigger_type": "Stage2-Actionable", "trigger_family": "PF_balance_sheet_repair_rebound_with_orderbook_visibility", "entry_date": "2024-01-26", "entry_price": 17530.0, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv", "mfe_30d_pct": 18.3685, "mae_30d_pct": -8.3286, "mfe_90d_pct": 18.3685, "mae_90d_pct": -11.5801, "mfe_180d_pct": 60.8671, "mae_180d_pct": -11.5801, "peak_date_180d": "2024-08-26", "peak_price_180d": 28200.0, "trough_date_180d": "2024-04-19", "trough_price_180d": 15500.0, "classification": "mixed_positive", "current_profile_error": "Stage2 could be right, but needs 4B/local volatility guard before full positive promotion", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "raw_component_score_breakdown": {"eps_revision": 12, "visibility": 18, "bottleneck": 6, "mispricing": 17, "valuation": 18, "capital": 10, "info": 8, "total": 89}, "profile_stage_proxy": "Stage3-Green_without_C30_guard", "proposed_guard_result": "Stage2-Actionable_or_local_4B_watch_until_cash_bridge"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R10", "selected_loop": 101, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_REPAIR_ORDERBOOK_CASHFLOW_BRIDGE_VS_LOW_PBR_REBOUND", "symbol": "006360", "name": "GS건설", "market": "KOSPI", "trigger_type": "Stage2-Actionable", "trigger_family": "post_pf_risk_repair_backlog_margin_recovery", "entry_date": "2024-04-29", "entry_price": 15640.0, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv", "mfe_30d_pct": 6.9054, "mae_30d_pct": -6.7136, "mfe_90d_pct": 39.0665, "mae_90d_pct": -7.6087, "mfe_180d_pct": 39.0665, "mae_180d_pct": -7.6087, "peak_date_180d": "2024-08-27", "peak_price_180d": 21750.0, "trough_date_180d": "2024-06-19", "trough_price_180d": 14450.0, "classification": "positive", "current_profile_error": "global profile under-separates true repair/cash conversion from generic construction beta", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "raw_component_score_breakdown": {"eps_revision": 18, "visibility": 20, "bottleneck": 8, "mispricing": 17, "valuation": 16, "capital": 13, "info": 8, "total": 100}, "profile_stage_proxy": "Stage3-Green", "proposed_guard_result": "Positive only if orderbook-to-margin-to-cash bridge is explicit"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R10", "selected_loop": 101, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_REPAIR_ORDERBOOK_CASHFLOW_BRIDGE_VS_LOW_PBR_REBOUND", "symbol": "047040", "name": "대우건설", "market": "KOSPI", "trigger_type": "Stage2", "trigger_family": "construction_beta_event_spike_without_clean_cash_bridge", "entry_date": "2024-07-15", "entry_price": 4260.0, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "mfe_30d_pct": 16.5493, "mae_30d_pct": -13.7324, "mfe_90d_pct": 16.5493, "mae_90d_pct": -20.7746, "mfe_180d_pct": 16.5493, "mae_180d_pct": -20.7746, "peak_date_180d": "2024-07-18", "peak_price_180d": 4965.0, "trough_date_180d": "2024-11-13", "trough_price_180d": 3375.0, "classification": "counterexample", "current_profile_error": "event spike can look like actionable PF relief, but post-peak MAE shows weak durable bridge", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "raw_component_score_breakdown": {"eps_revision": 8, "visibility": 12, "bottleneck": 4, "mispricing": 18, "valuation": 16, "capital": 8, "info": 14, "total": 80}, "profile_stage_proxy": "Stage3-Yellow_false_positive_risk", "proposed_guard_result": "local_4B_watch_or_Stage2_only"}
{"row_type": "trigger", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "selected_round": "R10", "selected_loop": 101, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_BALANCE_SHEET_REPAIR_ORDERBOOK_CASHFLOW_BRIDGE_VS_LOW_PBR_REBOUND", "symbol": "375500", "name": "DL이앤씨", "market": "KOSPI", "trigger_type": "Stage2", "trigger_family": "low_pbr_balance_sheet_label_without_revision_followthrough", "entry_date": "2024-04-29", "entry_price": 36650.0, "price_source": "Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "mfe_30d_pct": 2.3192, "mae_30d_pct": -10.0955, "mfe_90d_pct": 7.7763, "mae_90d_pct": -21.2824, "mfe_180d_pct": 7.7763, "mae_180d_pct": -21.2824, "peak_date_180d": "2024-06-13", "peak_price_180d": 39500.0, "trough_date_180d": "2024-08-08", "trough_price_180d": 28850.0, "classification": "counterexample", "current_profile_error": "low valuation and balance-sheet label can pass Stage2, but no revision/cash bridge produced negative asymmetry", "evidence_quality": "source_proxy_only", "evidence_url_pending": true, "raw_component_score_breakdown": {"eps_revision": 5, "visibility": 10, "bottleneck": 4, "mispricing": 17, "valuation": 20, "capital": 12, "info": 8, "total": 76}, "profile_stage_proxy": "Stage3-Yellow_false_positive_risk", "proposed_guard_result": "Stage2_only_or_4B_if_price_only"}
{"row_type": "aggregate", "selected_round": "R10", "selected_loop": 101, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 4, "reused_case_count": 0, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "calibration_usable_case_count": 4, "calibration_usable_trigger_count": 4, "positive_case_count": 1, "mixed_positive_count": 1, "counterexample_count": 2, "local_4b_watch_count": 3, "current_profile_error_count": 4, "coverage_static_index_rows_before": 3, "coverage_static_index_rows_after_if_accepted": 7, "coverage_conversation_local_rows_before": 3, "coverage_conversation_local_rows_after_if_accepted": 7, "need_to_30_after_if_accepted": 23}
{"row_type": "shadow_weight_candidate", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_axis_proposed": ["C30_pf_balance_sheet_hard_break_vs_repair_bridge_required", "C30_orderbook_margin_cash_conversion_required", "C30_low_pbr_price_only_false_positive_guard", "C30_event_spike_local_4b_high_MAE_guard"], "suggested_rule_logic": "Do not promote construction/PF names above Stage2-Actionable unless non-price evidence links PF/liquidity risk relief to orderbook quality, margin normalization, working-capital/cash conversion, and refinancing maturity extension. Price-only low-PBR rebound or news spike should remain Stage2/local-4B even if 30D MFE is high.", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "narrative_only", "summary": "C30 behaves like a pressure valve: if PF stress relief actually opens a cashflow path, the rebound can sustain; if it is merely low-PBR or event-spike heat, MAE later eats the early MFE.", "deferred_handoff_executed_now": false}
```

## 9. Residual Contribution Summary

```text
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C30_pf_balance_sheet_hard_break_vs_repair_bridge_required | C30_orderbook_margin_cash_conversion_required | C30_low_pbr_price_only_false_positive_guard | C30_event_spike_local_4b_high_MAE_guard
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff in the research session.

```text
You are a coding agent for Songdaiki/stock_agent. Batch-ingest this standalone v12 residual research MD only after it is placed under docs/round. Do not alter production scoring from this file alone. Parse the JSONL rows and add them to the v12 calibration corpus if they pass schema validation. Treat all evidence_url_pending=true rows as source-proxy-only and require original evidence URL backfill before permanent promotion decisions. Candidate shadow rule to evaluate: C30_pf_balance_sheet_hard_break_vs_repair_bridge_required. Compare against existing C30 rows and update coverage_matrix / archetype runtime reports only through the normal calibration ingestion pipeline.
```
