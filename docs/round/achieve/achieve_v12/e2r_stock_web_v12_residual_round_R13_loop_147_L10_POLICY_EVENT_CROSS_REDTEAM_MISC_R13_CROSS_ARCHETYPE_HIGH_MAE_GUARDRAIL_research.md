# E2R Stock-Web v12 Residual Research — R13 / High-MAE guardrail / loop 147

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R13
selected_loop: 147
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V147
output_file: e2r_stock_web_v12_residual_round_R13_loop_147_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: R13 cross-archetype high-MAE URL-verified mini holdout after session-adjusted Priority-0/Priority-1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection / novelty note

This pass is not a new sector-specific positive case search. It is an R13 high-MAE guardrail replay using URL-verified source-sector rows that had not yet been consumed by the local R13 replay ledger at the time of selection. The static No-Repeat Index still shows Priority 0/1 archetypes, but the current long session has already added repeated C02/C05/C06/C07/C09/C10/C11/C12/C14/C28 and R13 rows. Therefore the safest incremental contribution is a small, non-double-counted R13 holdout with `do_not_count_as_new_sector_case=true` and `independent_evidence_weight=0.25`.

Hard duplicate key checked manually for the local session:

```text
source_canonical_archetype_id + symbol + trigger_type + entry_date
```

All five rows use URL-present source-sector evidence and keep their source Cxx coverage out of this R13 aggregate.

## 2. Stock-Web price atlas confirmation

```yaml
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: [KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI]
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_path: atlas/schema.json
```

MFE/MAE fields were inherited from source-sector rows that used actual Stock-Web 1D OHLCV shards. Formula: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

## 3. R13 thesis summary

High MFE does not automatically validate Stage2 or Stage3 persistence. These rows all had real event evidence, but the price path still opened meaningful 90D/180D downside when the second bridge was not reconfirmed. R13 should therefore force a local Stage4B overlay when the following pattern appears:

```text
valid event / contract / platform / policy evidence
  -> missing second bridge confirmation
  -> MAE90 or MAE180 deepens beyond the holdout guardrail
  -> cap Stage2 persistence or require local Stage4B overlay
```

## 4. Case narratives

### 215100 로보로보 — positive_with_guardrail

- source canonical: `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` / source large sector: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`
- trigger: `2023-12-14` -> entry `2023-12-14` / source trigger type `4B`
- evidence family: education_service_robot_policy_theme_delayed_MFE_high_MAE
- source: https://en.yna.co.kr/view/AEN20231214003600320
- price path: entry close 4755.0; MFE90 22.6078%, MAE90 -11.6719%; MFE180 45.9516%, MAE180 -31.6509%; peak 2024-05-22 / 6940.0; post-peak drawdown -53.17%.
- R13 implication: 정책/보조금 이벤트가 회사별 계약·매출·마진으로 이어지는 second bridge가 약했다.

### 251270 넷마블 — counterexample_high_MAE

- source canonical: `C27_CONTENT_IP_GLOBAL_MONETIZATION` / source large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- trigger: `2024-05-08` -> entry `2024-05-08` / source trigger type `4B`
- evidence family: source-sector event evidence with URL verification
- source: https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=4808
- price path: entry close 60700; MFE90 19.28%, MAE90 -13.67%; MFE180 19.28%, MAE180 -30.23%; peak 2024-05-10 / 72400; post-peak drawdown -41.51%.
- R13 implication: IP·게임·팬플랫폼 이벤트가 durable revenue, retention/LTV, platform contribution bridge 없이 빠르게 소진될 수 있었다.

### 352820 하이브 — positive_with_guardrail

- source canonical: `C27_CONTENT_IP_GLOBAL_MONETIZATION` / source large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- trigger: `2023-04-24` -> entry `2023-04-24` / source trigger type `Stage2-Actionable`
- evidence family: source-sector event evidence with URL verification
- source: https://koreajoongangdaily.joins.com/2023/04/24/entertainment/kpop/Korea-Kpop-Weverse/20230424161919743.html
- price path: entry close 259000.0; MFE90 20.6564%, MAE90 -11.583%; MFE180 20.6564%, MAE180 -27.2587%; peak 2023-06-22 / 312500.0; post-peak drawdown -39.712%.
- R13 implication: IP·게임·팬플랫폼 이벤트가 durable revenue, retention/LTV, platform contribution bridge 없이 빠르게 소진될 수 있었다.

### 259960 크래프톤 — positive_with_guardrail

- source canonical: `C27_CONTENT_IP_GLOBAL_MONETIZATION` / source large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- trigger: `2023-05-19` -> entry `2023-05-22` / source trigger type `Stage2-Actionable`
- evidence family: source-sector event evidence with URL verification
- source: https://www.reuters.com/technology/krafton-gets-approval-resume-battle-royale-game-india-2023-05-19/
- price path: entry close 200500; MFE90 4.24%, MAE90 -27.18%; MFE180 21.2%, MAE180 -27.23%; peak 2024-02-14 / 243000; post-peak drawdown -6.79%.
- R13 implication: IP·게임·팬플랫폼 이벤트가 durable revenue, retention/LTV, platform contribution bridge 없이 빠르게 소진될 수 있었다.

### 018260 삼성에스디에스 — positive_with_guardrail

- source canonical: `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` / source large sector: `L8_PLATFORM_CONTENT_SW_SECURITY`
- trigger: `2024-10-31` -> entry `2024-11-01` / source trigger type `Stage2-Actionable`
- evidence family: source-sector event evidence with URL verification
- source: https://www.samsungsds.com/en/news/3q-20241031.html
- price path: entry close 142600.0; MFE90 7.99%, MAE90 -20.69%; MFE180 39.41%, MAE180 -23.56%; peak 2025-06-24 / 198800.0; post-peak drawdown -22.03%.
- R13 implication: 클라우드/AI/SW 성장 headline이 recurring revenue, renewal, margin bridge로 재확인되기 전에는 MAE 방어가 필요했다.

## 5. Backtest result table

| symbol | name | source canonical | trigger | entry | source trigger | R13 overlay | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak/date | post-peak DD |
|---|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 215100 | 로보로보 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 2023-12-14 | 2023-12-14 | 4B | Stage4B-LocalWatch | 4755.0 | 22.6078 | -5.4679 | 22.6078 | -11.6719 | 45.9516 | -31.6509 | 2024-05-22 / 6940.0 | -53.17 |
| 251270 | 넷마블 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2024-05-08 | 2024-05-08 | 4B | Stage4B-LocalWatch | 60700 | 19.28 | -11.7 | 19.28 | -13.67 | 19.28 | -30.23 | 2024-05-10 / 72400 | -41.51 |
| 352820 | 하이브 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2023-04-24 | 2023-04-24 | Stage2-Actionable | Stage4B-LocalWatch | 259000.0 | 16.9884 | -4.4402 | 20.6564 | -11.583 | 20.6564 | -27.2587 | 2023-06-22 / 312500.0 | -39.712 |
| 259960 | 크래프톤 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2023-05-19 | 2023-05-22 | Stage2-Actionable | Stage4B-LocalWatch | 200500 | 4.24 | -9.08 | 4.24 | -27.18 | 21.2 | -27.23 | 2024-02-14 / 243000 | -6.79 |
| 018260 | 삼성에스디에스 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 2024-10-31 | 2024-11-01 | Stage2-Actionable | Stage4B-LocalWatch | 142600.0 | 7.99 | -7.92 | 7.99 | -20.69 | 39.41 | -23.56 | 2025-06-24 / 198800.0 | -22.03 |

## 6. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 147, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V147", "source_round": "R11", "source_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "source_file": "e2r_stock_web_v12_residual_round_R11_loop_112_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "symbol": "215100", "name": "로보로보", "trigger_date": "2023-12-14", "entry_date": "2023-12-14", "entry_price": 4755.0, "source_trigger_type": "4B", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "education_service_robot_policy_theme_delayed_MFE_high_MAE", "evidence_url": "https://en.yna.co.kr/view/AEN20231214003600320", "MFE_30D_pct": 22.6078, "MAE_30D_pct": -5.4679, "MFE_90D_pct": 22.6078, "MAE_90D_pct": -11.6719, "MFE_180D_pct": 45.9516, "MAE_180D_pct": -31.6509, "peak_date": "2024-05-22", "peak_price": 6940.0, "drawdown_after_peak_pct": -53.17, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 147, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V147", "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "symbol": "251270", "name": "넷마블", "trigger_date": "2024-05-08", "entry_date": "2024-05-08", "entry_price": 60700, "source_trigger_type": "4B", "trigger_type": "Stage4B", "classification": "counterexample_high_MAE", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=4808", "MFE_30D_pct": 19.28, "MAE_30D_pct": -11.7, "MFE_90D_pct": 19.28, "MAE_90D_pct": -13.67, "MFE_180D_pct": 19.28, "MAE_180D_pct": -30.23, "peak_date": "2024-05-10", "peak_price": 72400, "drawdown_after_peak_pct": -41.51, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 147, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V147", "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "symbol": "352820", "name": "하이브", "trigger_date": "2023-04-24", "entry_date": "2023-04-24", "entry_price": 259000.0, "source_trigger_type": "Stage2-Actionable", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://koreajoongangdaily.joins.com/2023/04/24/entertainment/kpop/Korea-Kpop-Weverse/20230424161919743.html", "MFE_30D_pct": 16.9884, "MAE_30D_pct": -4.4402, "MFE_90D_pct": 20.6564, "MAE_90D_pct": -11.583, "MFE_180D_pct": 20.6564, "MAE_180D_pct": -27.2587, "peak_date": "2023-06-22", "peak_price": 312500.0, "drawdown_after_peak_pct": -39.712, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 147, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V147", "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "symbol": "259960", "name": "크래프톤", "trigger_date": "2023-05-19", "entry_date": "2023-05-22", "entry_price": 200500, "source_trigger_type": "Stage2-Actionable", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://www.reuters.com/technology/krafton-gets-approval-resume-battle-royale-game-india-2023-05-19/", "MFE_30D_pct": 4.24, "MAE_30D_pct": -9.08, "MFE_90D_pct": 4.24, "MAE_90D_pct": -27.18, "MFE_180D_pct": 21.2, "MAE_180D_pct": -27.23, "peak_date": "2024-02-14", "peak_price": 243000, "drawdown_after_peak_pct": -6.79, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R13", "loop": 147, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V147", "source_round": "R8", "source_large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "source_file": "e2r_stock_web_v12_residual_round_R8_loop_101_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "symbol": "018260", "name": "삼성에스디에스", "trigger_date": "2024-10-31", "entry_date": "2024-11-01", "entry_price": 142600.0, "source_trigger_type": "Stage2-Actionable", "trigger_type": "Stage4B", "classification": "positive_with_guardrail", "evidence_family": "url_verified_source_sector_event_with_missing_second_bridge", "evidence_url": "https://www.samsungsds.com/en/news/3q-20241031.html", "MFE_30D_pct": 7.99, "MAE_30D_pct": -7.92, "MFE_90D_pct": 7.99, "MAE_90D_pct": -20.69, "MFE_180D_pct": 39.41, "MAE_180D_pct": -23.56, "peak_date": "2025-06-24", "peak_price": 198800.0, "drawdown_after_peak_pct": -22.03, "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_sector_case": true, "independent_evidence_weight": 0.25, "current_profile_error": true, "production_scoring_patch_applied": false}
```

## 7. Score / return alignment

```jsonl
{"row_type": "score_simulation", "case_id": "R13_V147_215100_20231214_HIGH_MAE_BRIDGE_GAP", "symbol": "215100", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "current_profile_proxy_score": 53.43, "shadow_rule_score_delta": -6, "shadow_adjusted_score": 47.43, "shadow_stage_effect": "Stage2 persistence capped; Stage4B-LocalWatch overlay required", "score_return_alignment_note": "alignment improved: high-MAE path capped until second bridge confirmation"}
{"row_type": "score_simulation", "case_id": "R13_V147_251270_20240508_HIGH_MAE_BRIDGE_GAP", "symbol": "251270", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "current_profile_proxy_score": 50.9, "shadow_rule_score_delta": -6, "shadow_adjusted_score": 44.9, "shadow_stage_effect": "Stage2 persistence capped; Stage4B-LocalWatch overlay required", "score_return_alignment_note": "alignment improved: high-MAE path capped until second bridge confirmation"}
{"row_type": "score_simulation", "case_id": "R13_V147_352820_20230424_HIGH_MAE_BRIDGE_GAP", "symbol": "352820", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "current_profile_proxy_score": 51.34, "shadow_rule_score_delta": -4, "shadow_adjusted_score": 47.34, "shadow_stage_effect": "Stage2 persistence capped; Stage4B-LocalWatch overlay required", "score_return_alignment_note": "alignment improved: high-MAE path capped until second bridge confirmation"}
{"row_type": "score_simulation", "case_id": "R13_V147_259960_20230522_HIGH_MAE_BRIDGE_GAP", "symbol": "259960", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "current_profile_proxy_score": 51.4, "shadow_rule_score_delta": -4, "shadow_adjusted_score": 47.4, "shadow_stage_effect": "Stage2 persistence capped; Stage4B-LocalWatch overlay required", "score_return_alignment_note": "alignment improved: high-MAE path capped until second bridge confirmation"}
{"row_type": "score_simulation", "case_id": "R13_V147_018260_20241101_HIGH_MAE_BRIDGE_GAP", "symbol": "018260", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "current_profile_proxy_score": 53.59, "shadow_rule_score_delta": -4, "shadow_adjusted_score": 49.59, "shadow_stage_effect": "Stage2 persistence capped; Stage4B-LocalWatch overlay required", "score_return_alignment_note": "alignment improved: high-MAE path capped until second bridge confirmation"}
```

Aggregate:

```json
{
  "row_type": "aggregate",
  "research_file": "e2r_stock_web_v12_residual_round_R13_loop_147_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md",
  "selected_round": "R13",
  "selected_loop": 147,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "trigger_row_count": 5,
  "calibration_usable_rows": 5,
  "representative_rows": 5,
  "unique_symbol_count": 5,
  "unique_source_canonical_count": 3,
  "unique_source_large_sector_count": 2,
  "positive_with_guardrail_count": 4,
  "counterexample_count": 5,
  "stage4b_overlay_count": 5,
  "stage4c_count": 0,
  "avg_MFE_30D_pct": 14.2212,
  "avg_MAE_30D_pct": -7.7216,
  "avg_MFE_90D_pct": 14.9548,
  "avg_MAE_90D_pct": -16.959,
  "avg_MFE_180D_pct": 29.2996,
  "avg_MAE_180D_pct": -27.9859,
  "rows_MAE180_le_minus_20pct": 5,
  "rows_MAE180_le_minus_30pct": 2,
  "rows_MFE180_ge_20pct": 4,
  "source_proxy_only_rows": 0,
  "evidence_url_pending_rows": 0,
  "do_not_count_as_new_sector_case": true,
  "independent_evidence_weight": 0.25,
  "production_code_patch_included": false,
  "production_scoring_patch_applied": false,
  "handoff_prompt_executed_now": false,
  "ready_for_batch_ingest": true
}
```

## 8. Current calibrated profile stress test

The current profile already has `stage2_required_bridge` and `local_4b_watch_guard`. The residual error is not absence of a global 4B rule; it is persistence. A row can begin as legitimate Stage2, but if the second bridge does not appear and MAE90/MAE180 deepens, the model should decay the Stage2 evidence rather than keep it warm.

```json
{
  "row_type": "residual_contribution",
  "contribution_label": "r13_high_mae_guardrail_holdout",
  "residual_error_found": true,
  "current_profile_error_count": 5,
  "main_residual": "Stage2/Stage3 persistence remains too sticky when URL-verified evidence lacks second bridge confirmation and MAE90/MAE180 breaches guardrail levels.",
  "suggested_shadow_axis": "R13_second_bridge_confirmation_or_stage4b_overlay"
}
```

## 9. Shadow rule candidate

```json
{
  "row_type": "shadow_weight_candidate",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "rule_id": "R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V147",
  "rule_effect": "When valid source-sector evidence is followed by MAE90 or MAE180 below the guardrail without delivery/revenue/margin/FCF/utilization/retention/cash bridge confirmation, cap Stage2 persistence and require a local Stage4B overlay.",
  "proposed_axes": [
    "second_bridge_confirmation_required",
    "mae90_mae180_stage2_decay",
    "local_4b_overlay_for_high_mae",
    "do_not_count_as_new_sector_case_for_r13_replay"
  ],
  "shadow_only": true
}
```

## 10. Validation scope

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
uses_current_session_source_rows_for_r13_reuse: true
do_not_count_as_new_sector_case: true
independent_evidence_weight: 0.25
jsonl_trigger_row_count: 5
calibration_usable_rows: 5
representative_rows: 5
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

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this during the research run. In the later batch-implementation session, ingest this Markdown together with the other V12 research MD files. Treat the trigger rows as R13 replay rows, not as fresh Cxx sector coverage. Test the shadow rule R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V147 against v12_trigger_rows_representative.jsonl. If accepted, implement only a scope-limited shadow/profile patch that decays Stage2 persistence or applies local 4B overlay when MAE90/MAE180 breaches without a second bridge confirmation. Do not alter production scoring directly unless the batch promotion decision applies the patch.
```

## 12. Completed research state

```text
completed_round = R13
completed_loop = 147
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = R13 cross-archetype high-MAE URL-verified mini holdout
next_recommended_archetypes = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_holdout_quality_only | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path | C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```