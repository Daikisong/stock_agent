# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R12
selected_loop: 110
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: GOVERNANCE_TENDER_CONTROL_PREMIUM_TO_CASH_EXIT_CAP_HOLDOUT_V110_SM_KOREAZINC_VALUEUP_INSURANCE_RECLASSIFICATION_SPLIT
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  direct_stock_web_shards:
    - 010130/2024: reused_from_prior_local_C16_C32_boundary_row
    - 041510/2023: source_proxy_reverify_required_from_loop_109
    - 005940/2024: reused_from_prior_local_C21_C32_boundary_row
    - 105560/2024: reused_from_prior_local_C21_C31_C32_boundary_row
    - 316140/2024: reused_from_prior_local_C21_C31_C32_boundary_row
    - 005830/2024: reused_from_prior_local_C22_C31_C32_boundary_row
    - 088350/2024: reused_from_prior_local_C22_C31_C32_boundary_row
    - 006800/2024: reused_from_prior_local_C21_C32_boundary_row
    - 000240/2024: not_recomputed_this_turn_future_control_premium_candidate
    - 008930/2024: not_recomputed_this_turn_future_governance_control_candidate
    - 115390/2024: not_recomputed_this_turn_future_tender_candidate
    - 003410/2024: not_recomputed_this_turn_future_squeezeout_tender_candidate
    - 145020/2024: not_recomputed_this_turn_future_control_premium_candidate
    - 036570/2024: not_recomputed_this_turn_governance_noise_check
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - governance_tender_to_cash_exit_gate
  - control_premium_vs_operating_archetype_reclassification_guard
  - tender_cap_minor_shareholder_risk_guard
  - valueup_capital_return_wrong_archetype_guard
  - insurance_reserve_wrong_archetype_guard
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` remains a Priority 0 archetype. The current no-repeat index marks C32 at only 3 representative rows, so it is still one of the lowest-coverage canonical archetypes. The v12 scheduler maps C32 to `R12 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.

This file continues the local C32 governance/control-premium sequence after `R12/C32 loop 109`; selected loop is therefore `110`.

This is a **dedupe-aware holdout validation / mixed source-proxy TODO** MD. It does not claim fresh independent stock-web evidence. Most trigger rows below reuse current-session stock-web-derived C21/C22/C31/C32/C16 boundary rows that already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. The SM row is explicitly marked `source_proxy_only=true` and must be directly repriced before aggregate use. Direct fresh C32 tender/control-premium candidate shards were not recomputed in this execution. Exact duplicate `same_entry_group_id` rows should be deduped during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C32 should not reward every `governance`, `value-up`, `shareholder return`, or `control issue` as the same thing.

C32 is the cash-exit and control-premium archetype:

```text
governance event / tender offer / control premium / takeover contest / squeeze-out / minority-risk event
→ formal offer or binding control battle
→ tender price / exchange ratio / premium cap
→ acceptance probability
→ settlement timing
→ downside if deal fails
→ minority-holder protections and liquidity
→ price path validation
```

The recurring false positive is:

```text
value-up capital return
low-PBR financial label
insurance reserve/capital-return mechanics
strategic-resource company with separate operating driver
generic shareholder return
governance noise without tender price
```

A tender is not normal alpha. It is more like an option with a posted exit door. Once the tender price is known, upside may be capped, downside may remain open, and the main risk becomes probability, settlement timing, and minority-holder treatment. C32 should therefore not learn a control-premium price path as an operating-sector margin signal, and it should not mistake ordinary value-up or capital-return policy for tender mechanics.

The C32 route split:

```text
formal tender / control contest + visible premium + settlement path
→ C32 can score, but cap post-offer upside and model failure downside

pre-existing operating thesis later contaminated by tender
→ cap original archetype and reclassify dominant post-event driver to C32

value-up / capital return without formal control premium
→ reclassify to C21/C31

insurance reserve / solvency / capital return
→ reclassify to C22/C31

financial low-PBR label without tender mechanics
→ hard 4C or Stage2 cap outside C32

source_proxy_only tender rows
→ no weight delta until direct stock-web reprice
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_trigger_rows: 8
  source_proxy_only_rows: 1
  narrative_only_future_todo_rows: 1
  source_archetypes:
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C32 holdout validation
    - tender/control-premium cap gate
    - governance contamination reclassification guard
    - value-up and insurance wrong-archetype guard
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
  - R4/C16 loop 115
  - R6/C21 loops 112~113
  - R6/C22 loops 111~112
  - R11/C31 loops 103~109
  - R12/C32 loops 104~109
  - R13 accounting-trust loops 12~14
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
source_proxy_reverify_required_rows:
  - 041510/2023
reason:
  - reused rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - SM tender/control row is kept as source-proxy boundary evidence and must be repriced
  - direct fresh C32 tender/control-premium candidate shards were unavailable or not recomputed in this execution
  - exact duplicate C32 keys should be deduped during batch ingest
  - this file is holdout validation / duplicate-low-value evidence only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"KOREA_ZINC_FORMAL_TENDER_CONTROL_PREMIUM_C32_POSITIVE_CAP","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_price":666000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":131.68,"MAE_30D_pct":0.00,"MFE_90D_pct":131.68,"MAE_90D_pct":0.00,"MFE_180D_pct":131.68,"MAE_180D_pct":0.00,"forward_high_30d":1543000,"forward_low_30d":666000,"forward_high_90d":1543000,"forward_low_90d":666000,"forward_high_180d":1543000,"forward_low_180d":666000,"corporate_action_window_status":"governance_tender_mechanics_dominate","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C32|010130|Stage2-Actionable|2024-09-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_C32_positive_control","reuse_reason":"same Korea Zinc governance/tender row from C16/C32 boundary files","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"formal_tender_control_premium_positive_cap","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|010130|Stage2-Actionable|2024-09-13","non_price_bridge":"formal control-premium/tender mechanics dominate the selected move; operating smelter/resource bridge should be capped after this point","score_alignment":"C32 positive-control but post-offer upside must be capped by tender/settlement mechanics and failure downside"}
{"row_type":"trigger","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"KOREA_ZINC_PRE_TENDER_OPERATING_THESIS_LATER_GOVERNANCE_CONTAMINATION_4B","symbol":"010130","name":"고려아연","trigger_type":"Stage4B","entry_date":"2024-04-09","entry_price":469000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.40,"MAE_30D_pct":-3.94,"MFE_90D_pct":16.42,"MAE_90D_pct":-3.94,"MFE_180D_pct":68.66,"MAE_180D_pct":-3.94,"forward_high_30d":499000,"forward_low_30d":450500,"forward_high_90d":546000,"forward_low_90d":450500,"forward_high_180d":791000,"forward_low_180d":450500,"corporate_action_window_status":"governance_tender_event_contamination_after_2024_09_13","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C32|010130|Stage4B|2024-04-09","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_contamination_4B","reuse_reason":"same Korea Zinc supply-tightness row with later governance contamination from C16/C32 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"pre_tender_operating_thesis_later_contaminated","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|010130|Stage4B|2024-04-09","non_price_bridge":"pre-tender smelter/supply-tightness operating thesis later contaminated by governance/control-premium event inside the 180D window","score_alignment":"local 4B / contamination cap; do not learn later tender-driven 180D MFE as C16 or generic operating alpha"}
{"row_type":"trigger","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"SM_CONTROL_BATTLE_TENDER_PREMIUM_SOURCE_PROXY_4B","symbol":"041510","name":"에스엠","trigger_type":"Stage4B","entry_date":"2023-02-10","entry_price":114700,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.10,"corporate_action_window_status":"source_proxy_tender_control_reverify_required","forward_window_trading_days":180,"calibration_usable":false,"source_proxy_only":true,"batch_reverification_required":true,"same_entry_group_id":"C32|041510|Stage4B|2023-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_source_proxy_tender_4B","reuse_reason":"same SM control battle/tender boundary row from C27/C32 guardrails; direct stock-web reprice required","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"source_proxy_control_battle_tender_4B","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|041510|Stage4B|2023-02-10","non_price_bridge":"content IP value existed, but selected event was dominated by control battle / tender / control-premium mechanics rather than recurring IP monetization","score_alignment":"source-proxy C32 4B; reprice before use and cap C27 contribution if tender mechanics dominate"}
{"row_type":"trigger","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"SECURITIES_CAPITAL_RETURN_POSITIVE_BUT_NOT_TENDER_RECLASSIFY_C21","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":11420,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.71,"MAE_30D_pct":-2.36,"MFE_90D_pct":14.71,"MAE_90D_pct":-2.36,"MFE_180D_pct":26.09,"MAE_180D_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C32|005940|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_positive_elsewhere","reuse_reason":"same securities capital-return positive row from C21/C32 boundary guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"capital_return_not_tender_reclassify_C21","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|005940|Stage2-Watch|2024-02-26","non_price_bridge":"securities ROE/PBR capital-return bridge with contained MAE and later validation, but no formal tender/control-premium mechanics","score_alignment":"cap C32 contribution; reclassify to C21 capital-return execution"}
{"row_type":"trigger","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_LOCAL_4B_NOT_CONTROL_PREMIUM","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_price":87900,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C32|105560|Stage4B|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_4B","reuse_reason":"same KB value-up/capital-return local-4B row from C21/C31/C32 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"bank_valueup_not_control_premium","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|105560|Stage4B|2024-07-26","non_price_bridge":"bank Value-up and capital-return bridge exists, but there is no formal tender, squeeze-out or control-premium settlement path","score_alignment":"cap C32 contribution; reclassify to C21/C31 and require CET1, payout, buyback and credit-cost refresh"}
{"row_type":"trigger","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LOW_PBR_BANK_VALUEUP_LABEL_NOT_TENDER_CAP","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_price":16180,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.08,"MAE_30D_pct":-15.08,"MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"MFE_180D_pct":5.69,"MAE_180D_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C32|316140|Stage2-Watch|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_label_cap","reuse_reason":"same low-PBR bank value-up cap row from C21/C31/C32 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"low_PBR_valueup_not_tender_cap","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|316140|Stage2-Watch|2024-07-26","non_price_bridge":"low-PBR bank value-up label without differentiated execution and without formal control-premium/tender mechanics","score_alignment":"Stage2-Watch/cap outside C32; reclassify to C21/C31 if payout/buyback evidence appears"}
{"row_type":"trigger","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"INSURANCE_RESERVE_CAPITAL_RETURN_POSITIVE_ELSEWHERE_RECLASSIFY_C22","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_price":95000,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.79,"MAE_30D_pct":-4.11,"MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"MFE_180D_pct":30.53,"MAE_180D_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C32|005830|Stage2-Watch|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_positive_elsewhere","reuse_reason":"same DB Insurance positive row from C22/C31/C32 controls","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"insurance_reserve_not_tender_reclassify_C22","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|005830|Stage2-Watch|2024-02-26","non_price_bridge":"nonlife reserve quality, loss-ratio discipline and capital-return bridge; positive but not tender/control-premium mechanics","score_alignment":"cap C32 contribution; reclassify to C22/C31 rather than learn as governance premium"}
{"row_type":"trigger","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_WITHOUT_CONTROL_PREMIUM_HARD_4C","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage4C","entry_date":"2024-02-26","entry_price":8680,"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.53,"MAE_30D_pct":-10.71,"MFE_90D_pct":5.53,"MAE_90D_pct":-20.16,"MFE_180D_pct":5.53,"MAE_180D_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"corporate_action_window_status":"not_flagged_in_current_session","forward_window_trading_days":180,"calibration_usable":true,"source_proxy_only":false,"batch_reverification_required":false,"same_entry_group_id":"C32|006800|Stage4C|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","reuse_reason":"same low-PBR brokerage hard-block row from C21/C32 guardrails","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"financial_label_without_tender_hard_4C","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|006800|Stage4C|2024-02-26","non_price_bridge":"low-PBR brokerage / shareholder-return label lacked capital-return execution and had no formal tender/control-premium mechanics","score_alignment":"hard 4C outside C32; cheapness or governance language alone failed"}
```

---

## 5. Narrative-only future TODO

```jsonl
{"row_type":"narrative_only_future_todo","selected_round":"R12","selected_loop":110,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"C32_TRUE_TENDER_CONTROL_PREMIUM_REPRICE_TODO_AFTER_CACHE_MISS","candidate_symbols":["041510","010130","000240","008930","115390","003410","145020","036570","192400","001720"],"candidate_names":["에스엠","고려아연","한국앤컴퍼니","한미사이언스","락앤락","쌍용C&E","휴젤","엔씨소프트-governance_noise_check","쿠쿠홀딩스","신영증권"],"why_not_trigger_row_now":"fresh stock-web symbol-year shards for true tender/control-premium/squeeze-out/minority-risk cases were not recomputed in this execution; no fresh 30D/90D/180D MFE/MAE computed here","calibration_usable":false,"score_alignment":"future run should compute stock-web windows before counting new C32 evidence; distinguish formal tender/control premium from value-up capital return, insurance reserve mechanics, operating sector rerating and generic governance noise"}
```

---

## 6. Case analysis

### 6.1 Korea Zinc / 010130 — true C32 positive-control and contamination guard

```yaml
formal_tender_row:
  entry_date: 2024-09-13
  entry_price: 666000
  90D_MFE_MAE: +131.68 / 0.00
  180D_MFE_MAE: +131.68 / 0.00
  route: C32 positive-control with tender cap

pre_tender_operating_row:
  entry_date: 2024-04-09
  entry_price: 469000
  90D_MFE_MAE: +16.42 / -3.94
  180D_MFE_MAE: +68.66 / -3.94
  route: local 4B / governance contamination cap
```

The first row is a direct C32 case: control-premium/tender mechanics dominate. The second row shows why C32 must contaminate downstream interpretation: later tender MFE should not be learned as strategic-resource or smelter-margin alpha.

### 6.2 SM Entertainment / 041510 — control battle / tender source-proxy

```yaml
entry_date: 2023-02-10
90D_MFE_MAE: +40.54 / -21.10
route: source_proxy 4B
```

This is structurally C32, but it is kept `source_proxy_only=true`. Direct stock-web reprice is required before aggregate use. The lesson is still clear: when tender/control battle dominates, C27 content-IP learning must be capped.

### 6.3 Financial value-up rows — not C32 unless tender exists

```yaml
not_C32_rows:
  - 005940: securities capital-return positive, reclassify C21.
  - 105560: bank value-up capital-return 4B, reclassify C21/C31.
  - 316140: low-PBR value-up label cap, reclassify C21/C31.
  - 006800: low-PBR brokerage label hard 4C.
```

These rows use governance/value-up vocabulary but do not have tender mechanics. C32 should not become the bucket for all shareholder-return language.

### 6.4 Insurance capital-return row — positive elsewhere

```yaml
005830:
  90D_MFE_MAE: +27.05 / -9.26
  route: reclassify C22/C31
```

This row is positive, but the mechanism is reserve quality, solvency/capital return, and insurance accounting. It is not a control-premium settlement case.

---

## 7. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 8
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 1
batch_reverification_required_count: 1
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 2
counterexample_count: 6
local_4B_watch_count: 3
hard_4C_count: 1
wrong_archetype_reclassification_count: 5
current_profile_error_count: 6
diversity_score_summary: "formal tender positive, pre-tender contamination, source-proxy control battle, value-up wrong archetype, insurance reclassification, low-PBR hard 4C covered"
loop_contribution_label: duplicate_low_value_loop_with_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C32 lesson |
|---|---:|---:|---:|---|
| 010130 | formal tender positive | +131.68 / 0.00 | +131.68 / 0.00 | true C32 control-premium mechanics |
| 010130 | pre-tender contamination | +16.42 / -3.94 | +68.66 / -3.94 | cap operating archetype after tender |
| 041510 | control battle proxy | +40.54 / -21.10 | +40.54 / -21.10 | reprice; cap C27 if tender dominates |
| 005940 | C21 reclassify | +14.71 / -2.36 | +26.09 / -2.36 | capital return is not tender |
| 105560 | value-up 4B | +18.20 / -15.81 | +18.20 / -15.81 | bank value-up belongs C21/C31 |
| 316140 | value-up cap | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR label not C32 |
| 005830 | insurance reclassify | +27.05 / -9.26 | +30.53 / -9.26 | reserve/capital-return belongs C22/C31 |
| 006800 | financial label 4C | +5.53 / -20.16 | +5.53 / -23.96 | no tender, no execution |

---

## 8. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":86,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":84,"stage_label_after":"Stage2_Actionable_TenderCap","changed_components":["margin_bridge_score"],"component_delta_explanation":"Formal tender/control-premium mechanics dominate. Score as C32, not as smelter margin or resource policy.","MFE_90D_pct":131.68,"MAE_90D_pct":0.00,"score_return_alignment_label":"formal_tender_control_premium_positive","current_profile_verdict":"current_profile_correct_if_post_offer_upside_cap_applied"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":58,"stage_label_after":"Stage4B_governance_contamination_cap","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Pre-tender operating thesis became contaminated by later control-premium mechanics inside the 180D window.","MFE_90D_pct":16.42,"MAE_90D_pct":-3.94,"score_return_alignment_label":"pre_tender_later_contamination_4B","current_profile_verdict":"requires_contamination_cap"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"041510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":62,"stage_label_after":"Stage4B_source_reprice_required","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Control battle/tender mechanics likely dominate, but source-proxy row must be repriced before aggregate use.","MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"source_proxy_only":true,"score_return_alignment_label":"source_proxy_control_battle_4B","current_profile_verdict":"reverify_before_use"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"005940","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":70,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":48,"stage_label_after":"Reclassify_C21","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Securities capital-return economics are real but not tender/control-premium mechanics.","MFE_90D_pct":14.71,"MAE_90D_pct":-2.36,"score_return_alignment_label":"capital_return_positive_elsewhere","current_profile_verdict":"requires_C21_reclassification"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"105560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":49,"stage_label_after":"Stage4B_reclassify_C21_C31","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Bank value-up bridge lacks control-premium/tender settlement; route to C21/C31, not C32.","MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"score_return_alignment_label":"bank_valueup_not_tender","current_profile_verdict":"requires_reclassification"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"316140","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":41,"stage_label_after":"Stage2_cap_reclassify_C21_C31","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Low-PBR value-up label has no tender mechanics and lacked differentiated execution.","MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"score_return_alignment_label":"low_PBR_valueup_not_C32","current_profile_verdict":"current_profile_false_positive_if_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"005830","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":2,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_after":48,"stage_label_after":"Reclassify_C22_C31","changed_components":["margin_bridge_score","revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","accounting_trust_risk_score"],"component_delta_explanation":"Insurance reserve/capital-return bridge is positive elsewhere but not governance tender premium.","MFE_90D_pct":27.05,"MAE_90D_pct":-9.26,"score_return_alignment_label":"insurance_positive_elsewhere_not_C32","current_profile_verdict":"requires_C22_reclassification"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","symbol":"006800","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":60,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Low-PBR brokerage label lacked tender mechanics and capital-return execution; price path rejected it.","MFE_90D_pct":5.53,"MAE_90D_pct":-20.16,"score_return_alignment_label":"financial_label_no_tender_hard_4C","current_profile_verdict":"current_profile_false_positive_if_stage2"}
```

---

## 9. Current calibrated profile stress test

The C32 governance/tender cap gate held:

```text
formal tender/control-premium event
→ C32 can score, but post-offer upside must be capped and failure downside modeled

pre-existing operating thesis later contaminated by tender
→ local 4B / contamination cap

source-proxy control battle row
→ reprice before aggregate use

capital-return and value-up rows without tender
→ reclassify to C21/C31

insurance reserve/capital-return row
→ reclassify to C22/C31

low-PBR financial label without formal control premium
→ Stage2 cap or hard 4C
```

### Rule candidate retained, not newly proposed

```text
C32_GOVERNANCE_TENDER_CONTROL_PREMIUM_TO_CASH_EXIT_CAP_GATE_V110_HELD_OUT

if C32
and governance_control_premium_tender_or_squeezeout_label == true
and formal_offer_price_exchange_ratio_acceptance_probability_settlement_or_minority_protection_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C32
and formal_tender_or_control_premium_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    apply_post_offer_upside_cap = true
    require_failure_downside_and_settlement_timing_model = true
```

```text
if C32
and operating_archetype_row_later_contaminated_by_tender == true:
    local_4B_watch = true
    cap_original_archetype_contribution = true
    require_C32_reclassification_for_post_event_window = true
```

```text
if C32
and valueup_capital_return_or_lowPBR_label == true
and formal_tender_control_premium_mechanics == false:
    cap_C32_contribution = true
    require_reclassification_to_C21_or_C31 = true
```

```text
if C32
and insurance_reserve_capital_return_bridge == true
and tender_mechanics == false:
    cap_C32_contribution = true
    require_reclassification_to_C22_or_C31 = true
```

```text
if C32
and financial_governance_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20
and formal_tender_mechanics == false:
    route = Stage4C
```

---

## 10. Profile comparison shadow-only summary

```yaml
profile_comparison:
  P0_e2r_2_2_rolling_calibrated_proxy:
    hypothesis: current rolling profile with bridge/4B/4C guards
    eligible_trigger_count: 7
    source_proxy_trigger_count: 1
    avg_MFE_90D_pct: 32.27
    avg_MAE_90D_pct: -8.45
    false_positive_risk: high_if_valueup_or_operating_rows_are_left_as_C32
    verdict: adequate_only_with_C32_tender_cap_and_reclassification_gate
  P0b_e2r_2_1_reference:
    hypothesis: prior calibrated profile may overcredit governance/value-up language if not separated from tender mechanics
    eligible_trigger_count: 7
    false_positive_risk: higher
    verdict: inferior
  P1_sector_specific_candidate_profile:
    hypothesis: L10 governance rows require formal tender/control-premium cash-exit mechanics
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P2_canonical_archetype_candidate_profile:
    hypothesis: C32 requires cash-exit mechanics, not generic governance or value-up labels
    changed_axes: none_new_holdout_only
    verdict: pass_holdout
  P3_counterexample_guard_profile:
    hypothesis: financial/insurance value-up rows without tender reclassify or hard-block
    changed_axes: none_new_holdout_only
    verdict: strongest_for_false_positive_control
```

---

## 11. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | GOVERNANCE_TENDER_CONTROL_PREMIUM_HOLDOUT_V110 | 2 | 6 | 3 | 1 | 0 | 8 | 7 | 0 | 6 | false | false | 27 |

---

## 12. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 7
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 8
source_proxy_only_count: 1
batch_reverification_required_count: 1
narrative_only_future_todo_count: 1
narrative_only_or_rejected_count: 2
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only_and_reverify_proxy_rows
```

---

## 13. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 8
reused_case_ids:
  - C32|010130|Stage2-Actionable|2024-09-13
  - C32|010130|Stage4B|2024-04-09
  - C32|041510|Stage4B|2023-02-10
  - C32|005940|Stage2-Watch|2024-02-26
  - C32|105560|Stage4B|2024-07-26
  - C32|316140|Stage2-Watch|2024-07-26
  - C32|005830|Stage2-Watch|2024-02-26
  - C32|006800|Stage4C|2024-02-26
new_symbol_count: 0
new_trigger_family_count: 0
source_proxy_only_count: 1
batch_reverification_required_count: 1
narrative_only_future_todo_count: 1
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - C32_governance_tender_control_premium_cash_exit_cap_gate
  - adjacent_archetype_reclassification_guard
residual_error_types_found:
  - operating_row_later_governance_tender_contamination
  - valueup_label_without_tender_mechanics
  - insurance_reserve_wrong_archetype
  - financial_lowPBR_label_without_control_premium
  - source_proxy_control_battle_reprice_gap
new_axis_proposed: null
existing_axis_strengthened:
  - C32_GOVERNANCE_TENDER_CONTROL_PREMIUM_TO_CASH_EXIT_CAP_GATE_V110_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: all rows are reused/source-proxy holdout validation after direct fresh C32 tender/control-premium candidates were not recomputed
loop_contribution_label: duplicate_low_value_loop_with_proxy_reverify_todo
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R12","loop":"110","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":0,"reused_case_count":8,"new_symbol_count":0,"new_trigger_family_count":0,"source_proxy_only_count":1,"batch_reverification_required_count":1,"narrative_only_future_todo_count":1,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","C32_governance_tender_control_premium_cash_exit_cap_gate","adjacent_archetype_reclassification_guard"],"residual_error_types_found":["operating_row_later_governance_tender_contamination","valueup_label_without_tender_mechanics","insurance_reserve_wrong_archetype","financial_lowPBR_label_without_control_premium","source_proxy_control_battle_reprice_gap"],"loop_contribution_label":"duplicate_low_value_loop_with_proxy_reverify_todo","do_not_propose_new_weight_delta":true}
```

---

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat this R12/C32 loop 110 as holdout validation only. Batch it with C32 loops 104~109, C16 governance-contamination rows, C21/C31 value-up rows, C22 insurance capital-return rows, and R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrails. If exact same_entry_group_id rows already exist, dedupe them. Preserve the C32 governance/tender/control-premium-to-cash-exit cap gate, post-offer upside cap, failure-downside model requirement, and adjacent-archetype reclassification guard. Do not create a new weight delta from this loop because no new independent case was added and one true control-battle row is source_proxy_only. Future research should directly reprice 에스엠(041510), 고려아연(010130), 한국앤컴퍼니(000240), 한미사이언스(008930), 락앤락(115390), 쌍용C&E(003410), 휴젤(145020), 엔씨소프트(036570), 신영증권(001720), 쿠쿠홀딩스(192400), and other formal tender/control-premium/minority-risk cases when stock-web shards are accessible.
```

---

## 15. Next research state

```yaml
completed_round: R12
completed_loop: 110
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
```
