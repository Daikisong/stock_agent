# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 113
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_RESERVE_CSM_KICS_CAPITAL_RETURN_HOLDOUT_V113_NONLIFE_LIFE_REINSURANCE_GA_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 005830/2024: cache_miss_observed_this_turn
    - 088350/2024: cache_miss_observed_this_turn
    - 000810/2024: cache_miss_observed_this_turn
    - 001450/2024: cache_miss_observed_this_turn
    - 032830/2024: cache_miss_or_not_recomputed_this_turn
    - 085620/2024: cache_miss_or_not_recomputed_this_turn
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - reserve_quality_CSM_KICS_capital_return_gate
  - nonlife_vs_life_vs_reinsurance_route_split
  - GA_distribution_reclassification_guard
  - low_MFE_life_valueup_false_positive_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C22_INSURANCE_RATE_CYCLE_RESERVE` remains Priority 0 in the current no-repeat index. The v12 scheduler maps C21~C22 to `R6 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.

This file continues the local C22 sequence after `R6/C22 loop 112`; selected loop is therefore `113`.

This is a **dedupe-aware holdout validation / cache-miss TODO** MD. It does not claim fresh independent stock-web evidence because direct insurance candidate shards cache-missed or additional insurance shards were not recomputed in this execution. The trigger rows below reuse current-session stock-web-derived C22/C21/C31/C32 rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C22 is not `insurance stock + Value-up`.

C22 is the insurance accounting bridge:

```text
insurance rate cycle / reserve quality / CSM / K-ICS / loss ratio / solvency / capital return
→ book-value trust
→ earnings quality
→ distributable capital
→ payout or buyback capacity
→ price path validation
```

Insurance accounting is a dam. Value-up is the rain cloud, but C22 only scores when the reservoir level, spillway strength and release schedule are visible. In practical scoring terms, the stock must show evidence that reserve quality, CSM/K-ICS, loss-ratio discipline or capital-return execution has moved from label into distributable economics.

The recurrent false-positive routes:

```text
life insurer label without CSM/K-ICS/payout bridge
GA / insurance distribution commission economics misfiled as reserve-cycle insurance
low-PBR financial beta with no reserve or capital return execution
one-off MFE without reserve quality or solvency bridge
```

The C22 route split:

```text
nonlife reserve/loss-ratio/capital-return bridge
→ Stage2 can survive

insurance holdco with K-ICS/capital-return compounding
→ Stage2 can survive, Green blocked until execution refresh

life insurer value-up label without CSM/K-ICS/payout
→ cap / Stage2 false positive

reinsurance rate-cycle discipline
→ Watch or slow positive, depending on underwriting and reserve evidence

GA / distribution commission bridge
→ reclassify away from C22

high MFE without reserve/solvency bridge
→ local 4B or reclassification, not Green
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 7
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C22 holdout validation
    - reserve/CSM/K-ICS/capital-return bridge split
    - GA/distribution reclassification guard
    - low-MFE life-insurer false-positive guard
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R6/C22 loop 109
  - R6/C22 loop 110
  - R6/C22 loop 111
  - R6/C22 loop 112
  - R6/C21 loop 113
  - R11/C31 loops 103~108
  - R12/C32 loops 104~108
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - direct C22 insurance candidate shards cache-missed or additional candidate shards were not recomputed in this execution
  - exact duplicate C22 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_RESERVE_LOSS_RATIO_CAPITAL_RETURN_POSITIVE_CONTROL","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_price":95000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.79,"MAE_30D_pct":-4.11,"MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"MFE_180D_pct":30.53,"MAE_180D_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C22|005830|Stage2-Actionable|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same DB Insurance C22/C31/C32 financial-control row from current session","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"nonlife_positive_control","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage2-Actionable|2024-02-26","non_price_bridge":"nonlife reserve quality, loss-ratio discipline and capital-return bridge","score_alignment":"keep Stage2; allow Yellow only while reserve quality, payout and capital-return execution stay refreshed"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_HOLDCO_KICS_CAPITAL_RETURN_COMPOUNDING_POSITIVE","symbol":"138040","name":"메리츠금융지주","trigger_type":"Stage2-Actionable","entry_date":"2024-08-16","entry_price":88800,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.50,"MAE_30D_pct":-1.46,"MFE_90D_pct":20.72,"MAE_90D_pct":-1.46,"MFE_180D_pct":43.47,"MAE_180D_pct":-1.46,"forward_high_30d":99900,"forward_low_30d":87500,"forward_high_90d":107200,"forward_low_90d":87500,"forward_high_180d":127400,"forward_low_180d":87500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C22|138040|Stage2-Actionable|2024-08-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","reuse_reason":"same insurance holdco capital-return C22 row from loop 109","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"insurance_holdco_positive_control","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|138040|Stage2-Actionable|2024-08-16","non_price_bridge":"insurance holdco capital-return execution, K-ICS buffer and compounding bridge","score_alignment":"keep Stage2; low MAE and durable 180D MFE support bridge if capital return remains explicit"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_CSM_KICS_CAPITAL_RETURN_HIGH_MAE_LOCAL_4B","symbol":"032830","name":"삼성생명","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_price":94700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.71,"MAE_30D_pct":-13.20,"MFE_90D_pct":17.21,"MAE_90D_pct":-13.20,"MFE_180D_pct":17.21,"MAE_180D_pct":-22.60,"forward_high_30d":102000,"forward_low_30d":82200,"forward_high_90d":111000,"forward_low_90d":82200,"forward_high_180d":111000,"forward_low_180d":73300,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C22|032830|Stage4B|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","reuse_reason":"same Samsung Life C22 high-MAE row from loop 109","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"life_positive_with_high_MAE_4B","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|032830|Stage4B|2024-07-26","non_price_bridge":"life-insurance CSM, K-ICS and capital-return bridge exists but high MAE requires reserve/capital buffer refresh","score_alignment":"local 4B; Stage2 can open but Green blocked until CSM/K-ICS/payout evidence refreshes"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"REINSURANCE_RATE_CYCLE_RESERVE_LOW_VOL_CONTROL","symbol":"003690","name":"코리안리","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":7930,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.81,"MAE_30D_pct":-1.01,"MFE_90D_pct":6.81,"MAE_90D_pct":-5.42,"MFE_180D_pct":13.49,"MAE_180D_pct":-5.42,"forward_high_30d":8470,"forward_low_30d":7850,"forward_high_90d":8470,"forward_low_90d":7500,"forward_high_180d":9000,"forward_low_180d":7500,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C22|003690|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_reinsurance_control","reuse_reason":"same Korean Re C22 control row from loop 111","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"reinsurance_low_vol_control","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|003690|Stage2-Watch|2024-02-26","non_price_bridge":"reinsurance pricing, reserve discipline and underwriting-cycle bridge","score_alignment":"Stage2-Watch; reinsurance discipline is valid but MFE is modest"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_SOLVENCY_CSM_CAPITAL_BRIDGE_FALSE_POSITIVE","symbol":"088350","name":"한화생명","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-11","entry_price":3150,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.86,"MAE_30D_pct":-14.29,"MFE_90D_pct":2.86,"MAE_90D_pct":-14.29,"MFE_180D_pct":2.86,"MAE_180D_pct":-24.76,"forward_high_30d":3240,"forward_low_30d":2700,"forward_high_90d":3240,"forward_low_90d":2700,"forward_high_180d":3240,"forward_low_180d":2370,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C22|088350|Stage2-FalsePositive|2024-07-11","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_false_positive","reuse_reason":"same Hanwha Life value-up label false-positive row from loop 109","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"life_label_false_positive","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|088350|Stage2-FalsePositive|2024-07-11","non_price_bridge":"life-insurance Value-up label without CSM, K-ICS, reserve quality or capital-return execution bridge","score_alignment":"cap or false-positive block; label-only life insurance exposure failed"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_INSURANCE_DISTRIBUTION_COMMISSION_BRIDGE_RECLASSIFICATION_CAP","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_price":4100,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.76,"MAE_30D_pct":-2.32,"MFE_90D_pct":9.76,"MAE_90D_pct":-13.78,"MFE_180D_pct":14.63,"MAE_180D_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C22|244920|Stage2-Watch|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_reclassification_control","reuse_reason":"same A Plus Asset GA row from C22/C32 controls","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"GA_distribution_reclassification","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|244920|Stage2-Watch|2024-05-10","non_price_bridge":"insurance distribution / GA commission bridge, not reserve quality or solvency bridge","score_alignment":"cap C22 contribution and reclassify to insurance distribution commission axis"}
{"row_type":"trigger","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_DISTRIBUTION_HIGH_MFE_BUT_NOT_C22_GREEN_LOCAL_4B","symbol":"211050","name":"인카금융서비스","trigger_type":"Stage4B","entry_date":"2024-05-02","entry_price":4925,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.57,"MAE_30D_pct":-4.57,"MFE_90D_pct":31.57,"MAE_90D_pct":-16.35,"MFE_180D_pct":31.57,"MAE_180D_pct":-16.35,"forward_high_30d":6480,"forward_low_30d":4700,"forward_high_90d":6480,"forward_low_90d":4120,"forward_high_180d":6480,"forward_low_180d":4120,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"same_entry_group_id":"C22|211050|Stage4B|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_reclassification_4B","reuse_reason":"same INCA GA high-MFE row from C22 loop 110","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"GA_high_MFE_reclassification_4B","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|211050|Stage4B|2024-05-02","non_price_bridge":"GA distribution / commission platform economics, not reserve/CSM/K-ICS bridge","score_alignment":"local 4B or reclassification; high MFE should not be learned as C22 Green"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_trigger_todo","selected_round":"R6","selected_loop":113,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"C22_NEW_INSURANCE_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["000810","001450","000540","085620","079160"],"candidate_names":["삼성화재","현대해상","흥국화재","미래에셋생명","CJ CGV insurance-noise-exclusion-check"],"why_not_trigger_row_now":"stock-web symbol-year shards cache-missed or were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting these as new C22 evidence; exclude non-insurance false positives if ticker/noise mismatch appears"}
```

---

## 6. Case analysis

### 6.1 Nonlife positive bridge — DB Insurance / 005830

```yaml
entry_close: 95000
90D_MFE_MAE: +27.05 / -9.26
180D_MFE_MAE: +30.53 / -9.26
route: KeepStage2
```

DB Insurance is the positive-control. It passes because the bridge is nonlife reserve quality, loss-ratio discipline and capital return. This is the insurance equivalent of a bridge that actually reaches the ledger.

### 6.2 Insurance holdco compounding bridge — Meritz Financial / 138040

```yaml
entry_close: 88800
90D_MFE_MAE: +20.72 / -1.46
180D_MFE_MAE: +43.47 / -1.46
route: KeepStage2
```

This is the strongest low-MAE positive in the holdout set. It should not be treated as generic financial beta if capital-return execution and buffer quality are visible.

### 6.3 Life insurance high-MAE 4B — Samsung Life / 032830

```yaml
entry_close: 94700
90D_MFE_MAE: +17.21 / -13.20
180D_MFE_MAE: +17.21 / -22.60
route: local 4B
```

The CSM/K-ICS/capital-return bridge may exist, but high MAE says no Green until reserve/capital buffer and payout evidence refresh.

### 6.4 Reinsurance low-volatility control — Korean Re / 003690

```yaml
entry_close: 7930
90D_MFE_MAE: +6.81 / -5.42
180D_MFE_MAE: +13.49 / -5.42
route: Stage2-Watch
```

This is a watch-quality control. It is closer to C22 than GA rows, but MFE is modest and should not force promotion.

### 6.5 Life label false positive — Hanwha Life / 088350

```yaml
entry_close: 3150
90D_MFE_MAE: +2.86 / -14.29
180D_MFE_MAE: +2.86 / -24.76
route: Stage2 false-positive / cap
```

Life-insurance label alone did not produce reserve/capital-return validation.

### 6.6 GA distribution reclassification — A Plus Asset / 244920 and INCA / 211050

```yaml
244920:
  90D_MFE_MAE: +9.76 / -13.78
  route: reclassification cap

211050:
  90D_MFE_MAE: +31.57 / -16.35
  route: local 4B / reclassification
```

The bridge can be real, but it is a distribution-commission bridge, not reserve quality or solvency. The 211050 high-MFE row is especially dangerous because it could tempt the scorer to learn the wrong axis.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 7
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 3
counterexample_count: 4
local_4B_watch_count: 2
hard_or_false_positive_count: 1
wrong_archetype_reclassification_count: 2
current_profile_error_count: 4
diversity_score_summary: "nonlife positive, insurance holdco positive, life 4B, reinsurance watch, life false positive, GA reclassification and GA high-MFE 4B covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C22 lesson |
|---|---:|---:|---:|---|
| 005830 | nonlife positive | +27.05 / -9.26 | +30.53 / -9.26 | reserve/capital bridge validates |
| 138040 | holdco positive | +20.72 / -1.46 | +43.47 / -1.46 | K-ICS/capital-return compounding validates |
| 032830 | life 4B | +17.21 / -13.20 | +17.21 / -22.60 | CSM/K-ICS needs refresh |
| 003690 | reinsurance watch | +6.81 / -5.42 | +13.49 / -5.42 | underwriting control, not Green |
| 088350 | life false positive | +2.86 / -14.29 | +2.86 / -24.76 | label-only life fails |
| 244920 | GA reclassify | +9.76 / -13.78 | +14.63 / -13.78 | distribution, not reserve |
| 211050 | GA high-MFE 4B | +31.57 / -16.35 | +31.57 / -16.35 | high MFE belongs elsewhere |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":85,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":85,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"Nonlife reserve quality and capital return bridge validated with controlled MAE.","MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"score_return_alignment_label":"nonlife_reserve_capital_return_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"138040","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":1,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":87,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":1,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":87,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"Insurance holdco capital-return execution and K-ICS buffer compounding validated with very low MAE.","MFE_90D_pct":20.72,"MAE_90D_pct":-1.46,"score_return_alignment_label":"insurance_holdco_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":67,"stage_label_after":"Stage4B_CSM_KICS_refresh","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Life-insurance bridge may exist, but high MAE requires CSM/K-ICS/payout refresh before Green.","MFE_90D_pct":17.21,"MAE_90D_pct":-13.20,"score_return_alignment_label":"life_insurance_high_MAE_local_4B","current_profile_verdict":"current_profile_correct_if_4B"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"003690","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":68,"stage_label_after":"Stage2-Watch","changed_components":[],"component_delta_explanation":"Reinsurance rate-cycle bridge is legitimate but MFE is modest; watch/control is better than promotion.","MFE_90D_pct":6.81,"MAE_90D_pct":-5.42,"score_return_alignment_label":"reinsurance_watch_control","current_profile_verdict":"current_profile_correct_if_watch"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":39,"stage_label_after":"Stage2_FalsePositive_Block","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Life-insurance Value-up label lacked CSM/K-ICS/reserve/payout bridge and produced weak MFE with large 180D MAE.","MFE_90D_pct":2.86,"MAE_90D_pct":-14.29,"score_return_alignment_label":"life_label_false_positive","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"244920","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":65,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":45,"stage_label_after":"Reclassify_distribution_commission_axis","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"GA distribution commission bridge is not C22 reserve/CSM/K-ICS mechanics.","MFE_90D_pct":9.76,"MAE_90D_pct":-13.78,"score_return_alignment_label":"GA_distribution_reclassification","current_profile_verdict":"requires_reclassification"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","symbol":"211050","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":55,"stage_label_after":"Stage4B_reclassify_distribution","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"High MFE belongs to GA distribution economics, not C22 reserve/solvency; Green must be blocked.","MFE_90D_pct":31.57,"MAE_90D_pct":-16.35,"score_return_alignment_label":"GA_high_MFE_wrong_C22_bridge","current_profile_verdict":"current_profile_overcredits_if_C22_Green"}
```

---

## 9. Current calibrated profile stress test

The C22 reserve/CSM/K-ICS/capital-return gate held:

```text
nonlife reserve/loss-ratio/capital-return bridge
→ keep Stage2

insurance holdco K-ICS/capital-return bridge
→ keep Stage2

life CSM/K-ICS bridge with high MAE
→ local 4B, no Green

reinsurance rate-cycle discipline with modest MFE
→ Watch/control

life Value-up label without reserve/capital bridge
→ cap or false-positive block

GA distribution commission economics
→ reclassify away from C22

high MFE GA row
→ local 4B / reclassification, not Green
```

### Rule candidate retained, not newly proposed

```text
C22_RESERVE_CSM_KICS_CAPITAL_RETURN_GATE_V113_HELD_OUT

if C22
and insurance_rate_cycle_Valueup_or_reserve_label == true
and reserve_quality_CSM_KICS_solvency_loss_ratio_or_capital_return_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C22
and reserve_quality_or_capital_return_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if C22
and life_insurance_CSM_KICS_bridge == true
and MAE_180D_pct <= -20:
    local_4B_watch = true
    block_stage3_green_until_CSM_KICS_payout_refresh = true
```

```text
if C22
and life_insurance_Valueup_label == true
and MFE_90D_pct < +10
and MAE_180D_pct <= -20
and reserve_CSM_KICS_capital_return_bridge == false:
    route = Stage2_FalsePositive_Block
```

```text
if C22
and GA_distribution_or_commission_bridge == true
and reserve_solvency_bridge == false:
    cap_C22_contribution = true
    require_reclassification_to_distribution_commission_axis = true
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_1_stock_web_calibrated_proxy:
    hypothesis: current profile with global Stage2 bridge and 4C guards
    eligible_trigger_count: 7
    avg_MFE_90D_pct: 21.45
    avg_MAE_90D_pct: -11.85
    false_positive_risk: high_if_life_label_or_GA_rows_are_left_as_generic_C22
    verdict: adequate_only_with_C22_reserve_CSM_KICS_gate
  P0b_e2r_2_0_baseline_reference:
    hypothesis: older profile pays too much for insurance/Value-up labels
    eligible_trigger_count: 7
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L6 insurance names require reserve/CSM/K-ICS/capital-return bridge
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C22 requires insurance accounting bridge, not distribution commission
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: life-label false positive and GA misclassification rows should be blocked or reclassified
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_RESERVE_CSM_KICS_HOLDOUT_V113 | 3 | 4 | 2 | 1 | 0 | 7 | 7 | 0 | 4 | false | false | 24 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 7
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 7
reused_case_ids:
  - C22|005830|Stage2-Actionable|2024-02-26
  - C22|138040|Stage2-Actionable|2024-08-16
  - C22|032830|Stage4B|2024-07-26
  - C22|003690|Stage2-Watch|2024-02-26
  - C22|088350|Stage2-FalsePositive|2024-07-11
  - C22|244920|Stage2-Watch|2024-05-10
  - C22|211050|Stage4B|2024-05-02
new_symbol_count: 0
new_trigger_family_count: 0
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C22_reserve_CSM_KICS_capital_return_gate
  - GA_distribution_reclassification_guard
residual_error_types_found:
  - life_insurance_label_without_CSM_KICS
  - GA_distribution_wrong_archetype
  - high_MFE_wrong_bridge
  - reinsurance_watch_not_green
new_axis_proposed: null
existing_axis_strengthened:
  - C22_RESERVE_CSM_KICS_CAPITAL_RETURN_GATE_V113_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows reused holdout validation after direct fresh C22 insurance candidate shards cache-missed or were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_cache_miss_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"113","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":0,"reused_case_count":7,"new_symbol_count":0,"new_trigger_family_count":0,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C22_reserve_CSM_KICS_capital_return_gate","GA_distribution_reclassification_guard"],"residual_error_types_found":["life_insurance_label_without_CSM_KICS","GA_distribution_wrong_archetype","high_MFE_wrong_bridge","reinsurance_watch_not_green"],"loop_contribution_label":"duplicate_low_value_loop_with_cache_miss_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R6/C22 loop 113 as holdout validation only. Batch it with C22 loops 109~112, C21/C31/C32 financial-policy guardrails, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C22 reserve/CSM/K-ICS/capital-return gate and GA distribution reclassification guard, but do not create a new weight delta from this loop because no new independent case was added. Future research should reprice 삼성화재(000810), 현대해상(001450), 흥국화재(000540), 미래에셋생명(085620) when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R6
completed_loop: 113
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```
