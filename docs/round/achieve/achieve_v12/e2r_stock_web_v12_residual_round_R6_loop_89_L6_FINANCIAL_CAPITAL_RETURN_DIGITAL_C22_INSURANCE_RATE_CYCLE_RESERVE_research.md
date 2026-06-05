# E2R Stock-Web v12 Residual Research — R6 Loop 89 / C22 Insurance Rate Cycle Reserve

```yaml
schema_version: e2r_stock_web_v12_residual_research_md
scheduled_round: R6
scheduled_loop: 89
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_INSURANCE_BETA
research_mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
do_not_propose_new_weight_delta: true
completed_round: R6
completed_loop: 89
next_round: R7
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
```

## 1. Execution scope

This file follows the v12 sequential scheduler after `R5 / loop 89`, so the scheduled slot is `R6 / loop 89`.

R6 must map to:

```text
L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

Within R6, this run avoids another C21 bank/value-up loop and instead expands:

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_INSURANCE_BETA
```

This is not a live recommendation file. It is a historical trigger-level residual calibration file using `Songdaiki/stock-web` daily OHLCV rows.

## 2. No-Repeat / novelty check

No-Repeat Index snapshot for C22:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
rows: 37
symbols: 12
date range: 2024-01-24~2024-08-22
good/bad Stage2: 10/11
4B/4C: 2/0
URL pending/proxy: 10/10
top covered symbols: 000370(7), 003690(7), 082640(6), 000540(4), 000810(3), 005830(3)
```

Avoided high-repeat symbols:

```text
000370, 003690, 082640, 000540, 000810, 005830
```

Selected symbols:

```text
032830 삼성생명
001450 현대해상
088350 한화생명
```

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All three selected rows are new C22 symbol/failure-mode expansions relative to the visible top-covered list.

## 3. Stock-Web validation scope

Stock-Web manifest basis:

```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
max_date: 2026-02-20
tradable_row_count: 14,354,401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
```

Profile status:

| Symbol | Name | profile last_date | row_status | corp-action candidate overlap with 2024-02-01~D+180? | calibration usable |
|---|---|---:|---|---|---|
| 032830 | 삼성생명 | 2026-02-20 | active_like | none | true |
| 001450 | 현대해상 | 2026-02-20 | active_like | candidate 2004-07-13 only; no 2024 overlap | true |
| 088350 | 한화생명 | 2026-02-20 | active_like | none | true |

## 4. Historical trigger thesis

### C22 residual question

C22 should not treat all insurance rallies as the same animal.

The weak form is:

```text
low PBR insurance beta
+ value-up / rate-cycle headline
+ sector sympathy
```

The stronger C22 bridge is:

```text
IFRS17/CSM visibility
+ reserve adequacy
+ rate/pricing cycle quality
+ solvency/capital buffer
+ explicit dividend/buyback/capital-return path
+ ROE/PBR rerating bridge
```

The residual error this run tests:

```text
If C22 Stage2-Actionable is opened merely by low-PBR insurance beta,
then high-MAE false positives can enter before reserve/capital-return quality is proven.
```

## 5. Case grid

| case_id | symbol | name | entry | entry_price | verdict | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---|---:|---:|---|---:|---:|---:|---:|---:|---:|
| R6L89_C22_032830_2024_02_01_VALUEUP_CSM_RESERVE_CAPITAL_RETURN_POSITIVE | 032830 | 삼성생명 | 2024-02-01 | 76,000 | positive_with_local_4b_overlay | +41.84% | -3.16% | +42.76% | -3.16% | +42.76% | -3.16% |
| R6L89_C22_001450_2024_02_01_RATE_CYCLE_RESERVE_FADE_COUNTEREXAMPLE | 001450 | 현대해상 | 2024-02-01 | 35,450 | counterexample_high_mae | +3.81% | -13.68% | +3.81% | -14.39% | +3.67% | -16.36% |
| R6L89_C22_088350_2024_02_01_LIFE_INSURANCE_LOW_PBR_BETA_COUNTEREXAMPLE | 088350 | 한화생명 | 2024-02-01 | 3,355 | counterexample_high_mae | +13.71% | -10.88% | +13.71% | -16.39% | +13.71% | -19.52% |

## 6. Case notes

### 6.1 삼성생명 / 032830 — positive with local 4B overlay

Entry is 2024-02-01 close 76,000. Stock-Web shows same-day high 76,800 and then rapid follow-through: 2024-02-23 close 95,600, 2024-02-28 high/close 102,900, and 2024-03-05 high 107,800. This creates a strong 30D/90D MFE path with shallow observed MAE after entry.

Interpretation:

```text
C22 positive candidate when low-PBR rerating is joined by life-insurance capital/CSM/reserve quality and shareholder-return bridge.
```

However, the path exceeds +40% quickly, so it should also trigger a local 4B watch if no fresh non-price evidence arrives after the rerating move.

### 6.2 현대해상 / 001450 — counterexample

Entry is 2024-02-01 close 35,450. The path briefly touches 36,800 on 2024-02-05, but the follow-through fails. It falls to 30,600 by 2024-03-29 and later reaches 29,650 around late October. This is a poor Stage2-Actionable candidate if the only input is insurance beta / rate-cycle sympathy.

Interpretation:

```text
P&C rate-cycle headline without reserve-quality, loss-ratio, and capital-return bridge should remain Watch/Stage1.
```

### 6.3 한화생명 / 088350 — counterexample

Entry is 2024-02-01 close 3,355. It spikes to a 2024-02-13 high of 3,815, but this is below a +20% MFE threshold and reverses into a 2024-04-05 low of 2,805 and 2024-08-05 low of 2,700. This is an archetypal low-PBR insurance beta false-positive.

Interpretation:

```text
Life-insurance beta alone is not enough. C22 needs CSM quality, capital buffer, solvency, and explicit capital-return mechanics.
```

## 7. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","case_id":"R6L89_C22_032830_2024_02_01_VALUEUP_CSM_RESERVE_CAPITAL_RETURN_POSITIVE","symbol":"032830","name":"삼성생명","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_INSURANCE_BETA","trigger_type":"insurance_rate_reserve_capital_return_bridge","trigger_family":"CSM_reserve_capital_return_bridge","evidence_date":"2024-02-01","entry_date":"2024-02-01","entry_price":76000,"peak_30d_price":107800,"peak_30d_date":"2024-03-05","trough_30d_price":73600,"trough_30d_date":"2024-02-02","mfe_30d_pct":41.84,"mae_30d_pct":-3.16,"peak_90d_price":108500,"peak_90d_date":"2024-03-08","trough_90d_price":73600,"trough_90d_date":"2024-02-02","mfe_90d_pct":42.76,"mae_90d_pct":-3.16,"peak_180d_price":108500,"peak_180d_date":"2024-03-08","trough_180d_price":73600,"trough_180d_date":"2024-02-02","mfe_180d_pct":42.76,"mae_180d_pct":-3.16,"case_verdict":"positive_with_local_4b_overlay","current_profile_error":false,"calibration_usable":true,"source_proxy_pending":true,"corporate_action_contaminated_180d_window":false,"novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|032830|insurance_rate_reserve_capital_return_bridge|2024-02-01","raw_component_score_breakdown":{"eps_fcf_explosion":12,"earnings_visibility":17,"bottleneck_pricing":10,"market_mispricing":13,"valuation_rerating":14,"capital_allocation":5,"information_confidence":4,"total_proxy":75,"revision_proxy":55},"stage_alignment":"Stage2-Actionable at entry, Stage3-Yellow once CSM/reserve/capital-return evidence is explicit; local 4B watch after >40% MFE without fresh non-price confirmation."}
{"row_type":"trigger","case_id":"R6L89_C22_001450_2024_02_01_RATE_CYCLE_RESERVE_FADE_COUNTEREXAMPLE","symbol":"001450","name":"현대해상","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_INSURANCE_BETA","trigger_type":"pnc_insurance_rate_cycle_without_reserve_quality_bridge","trigger_family":"rate_cycle_beta_without_reserve_quality","evidence_date":"2024-02-01","entry_date":"2024-02-01","entry_price":35450,"peak_30d_price":36800,"peak_30d_date":"2024-02-05","trough_30d_price":30600,"trough_30d_date":"2024-02-28","mfe_30d_pct":3.81,"mae_30d_pct":-13.68,"peak_90d_price":36800,"peak_90d_date":"2024-02-05","trough_90d_price":30350,"trough_90d_date":"2024-04-08","mfe_90d_pct":3.81,"mae_90d_pct":-14.39,"peak_180d_price":36750,"peak_180d_date":"2024-07-31","trough_180d_price":29650,"trough_180d_date":"2024-10-25","mfe_180d_pct":3.67,"mae_180d_pct":-16.36,"case_verdict":"counterexample_high_mae","current_profile_error":true,"calibration_usable":true,"source_proxy_pending":true,"corporate_action_contaminated_180d_window":false,"novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|001450|pnc_insurance_rate_cycle_without_reserve_quality_bridge|2024-02-01","raw_component_score_breakdown":{"eps_fcf_explosion":7,"earnings_visibility":10,"bottleneck_pricing":9,"market_mispricing":11,"valuation_rerating":8,"capital_allocation":3,"information_confidence":3,"total_proxy":51,"revision_proxy":38},"stage_alignment":"Watch/Stage1 only unless reserve quality, loss-ratio improvement, and capital-return mechanics are explicit; low-PBR/rate beta alone should not unlock Stage2-Actionable."}
{"row_type":"trigger","case_id":"R6L89_C22_088350_2024_02_01_LIFE_INSURANCE_LOW_PBR_BETA_COUNTEREXAMPLE","symbol":"088350","name":"한화생명","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_INSURANCE_BETA","trigger_type":"life_insurance_low_pbr_beta_without_capital_return_bridge","trigger_family":"life_insurance_low_pbr_beta_without_CSM_capital_return","evidence_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3355,"peak_30d_price":3815,"peak_30d_date":"2024-02-13","trough_30d_price":2990,"trough_30d_date":"2024-02-28","mfe_30d_pct":13.71,"mae_30d_pct":-10.88,"peak_90d_price":3815,"peak_90d_date":"2024-02-13","trough_90d_price":2805,"trough_90d_date":"2024-04-05","mfe_90d_pct":13.71,"mae_90d_pct":-16.39,"peak_180d_price":3815,"peak_180d_date":"2024-02-13","trough_180d_price":2700,"trough_180d_date":"2024-08-05","mfe_180d_pct":13.71,"mae_180d_pct":-19.52,"case_verdict":"counterexample_high_mae","current_profile_error":true,"calibration_usable":true,"source_proxy_pending":true,"corporate_action_contaminated_180d_window":false,"novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|088350|life_insurance_low_pbr_beta_without_capital_return_bridge|2024-02-01","raw_component_score_breakdown":{"eps_fcf_explosion":6,"earnings_visibility":9,"bottleneck_pricing":7,"market_mispricing":12,"valuation_rerating":9,"capital_allocation":2,"information_confidence":3,"total_proxy":48,"revision_proxy":34},"stage_alignment":"Do not upgrade beyond Watch/Stage1 on sector-low-PBR beta; require CSM quality, solvency/capital buffer, and explicit payout/buyback path."}
```

## 8. Aggregate metrics

```jsonl
{"row_type":"aggregate_metric","scheduled_round":"R6","scheduled_loop":89,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"IFRS17_CSM_RESERVE_RATE_CYCLE_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_INSURANCE_BETA","new_independent_case_count":3,"same_archetype_new_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":0,"calibration_usable_trigger_count":3,"current_profile_error_count":2,"source_proxy_pending_count":3,"mean_mfe_90d_pct":20.09,"mean_mae_90d_pct":-11.31,"positive_to_counterexample_ratio":"1:2","residual_error_found":true,"do_not_propose_new_weight_delta":true}
```

## 9. Shadow rule candidate

```jsonl
{"row_type":"shadow_weight","scheduled_round":"R6","scheduled_loop":89,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","shadow_rule_id":"C22_REQUIRE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_BEFORE_STAGE2_ACTIONABLE","rule_type":"stage2_required_bridge","proposal_strength":"watch_only","production_scoring_changed":false,"rule_text":"For C22 insurance names, low-PBR/value-up/rate-cycle beta alone should not unlock Stage2-Actionable. Require at least two of: explicit CSM/reserve quality, solvency/capital buffer, loss-ratio/pricing improvement, dividend/buyback/capital-return mechanics, and earnings/ROE bridge. Without that bridge, cap at Watch/Stage1 or Stage2-non-actionable even if sector beta produces local MFE.","positive_support_case_ids":["R6L89_C22_032830_2024_02_01_VALUEUP_CSM_RESERVE_CAPITAL_RETURN_POSITIVE"],"counterexample_case_ids":["R6L89_C22_001450_2024_02_01_RATE_CYCLE_RESERVE_FADE_COUNTEREXAMPLE","R6L89_C22_088350_2024_02_01_LIFE_INSURANCE_LOW_PBR_BETA_COUNTEREXAMPLE"],"rollback_condition":"If future C22 rows show repeat +20% MFE with <10% MAE from low-PBR/rate beta alone across at least 5 independent symbols, demote this guard from required bridge to soft penalty.","do_not_apply_now":true}
```

## 10. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":89,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","loop_contribution_label":"residual_error_found","coverage_gap_filled":"C22 insurance rate/reserve cycle: new non-top-covered symbols and bridge-vs-beta counterexamples","new_axis_proposed":null,"existing_axis_strengthened":"stage2_required_bridge for insurance reserve/capital-return quality","existing_axis_weakened":null,"why_not_global_delta":"Only three source-proxy-pending rows; this supports a C22-specific guard candidate, not a global score change.","next_research_hint":"R7 loop89 should proceed to L7_BIO_HEALTHCARE_MEDICAL and avoid repeating prior C25 if possible."}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.

When batch-applying v12 residual research, parse this MD as C22_INSURANCE_RATE_CYCLE_RESERVE evidence only.
Use the JSONL trigger rows, aggregate_metric, shadow_weight, and residual_contribution rows.
Do not change production scoring directly from this single file.
Consider a scoped, reversible C22 guard candidate:

- scope:
  large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
  canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE

- candidate:
  C22_REQUIRE_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_BEFORE_STAGE2_ACTIONABLE

- rationale:
  032830 is a positive control, but 001450 and 088350 show that low-PBR / insurance beta can create false Stage2-Actionable candidates without CSM, reserve quality, solvency/capital buffer, and capital-return bridge.

- implementation constraints:
  production_scoring_changed must remain false in research stage.
  apply only after broader v12 batch review confirms enough independent supporting rows.
```

## 12. Final scheduler metadata

```text
completed_round: R6
completed_loop: 89
next_round: R7
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
```
