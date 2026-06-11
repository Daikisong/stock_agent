# E2R Stock-Web v12 Residual Research — R6 loop 99 / L6 / C22

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R6
selected_loop: 99
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NONLIFE_LIFE_INSURANCE_RATE_RESERVE_KICS_CSM_CAPITAL_RETURN_BRIDGE_VS_INSURANCE_VALUEUP_LABEL_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - rate_cycle_reserve_quality_guardrail
  - KICS_CSM_capital_buffer_bridge_test
  - high_MAE_guardrail
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C22_INSURANCE_RATE_CYCLE_RESERVE` 전용 residual research다.

C22는 “보험”, “저PBR”, “밸류업”, “금리 수혜”라는 라벨을 곧바로 Green으로 바꾸는 bucket이 아니다. 보험주는 장부 위의 숫자만 보는 것이 아니라, 그 숫자가 실제로 지급여력·reserve 질·손해율·자본환원으로 버틸 수 있는지를 봐야 한다.

```text
insurance rate cycle / value-up / capital return label
  → loss ratio / reserve adequacy / CSM quality / K-ICS buffer
  → sustainable dividend or buyback capacity
  → ROE and solvency-consistent capital return
  → stock-web 1D OHLC forward path
```

보험사는 물을 막는 둑과 같다. 보험료율이 올라오는 것은 강수량이 줄어드는 일이고, reserve quality와 K-ICS buffer는 둑의 두께다. 자본환원은 둑을 허물지 않고 물을 나눠줄 수 있을 때만 지속된다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["000810","005830","001450","032830"],"profile_paths":["atlas/symbol_profiles/000/000810.json","atlas/symbol_profiles/005/005830.json","atlas/symbol_profiles/001/001450.json","atlas/symbol_profiles/032/032830.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv"],"validation_scope":"2024 trigger-level forward path; historical corporate-action profile caveats outside local 2024 windows are treated as profile caveats, not local row rejection."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 1 lists C22 at 42 rows and asks for insurance rate cycle, reserve quality, and capital return expansion.
- Existing registry shows C22 parsed through `R6 loop 98`.
- This output uses `R6 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- This file focuses on nonlife leader, nonlife peer, weak reserve/price asymmetry peer, and life-insurance K-ICS/CSM capital-buffer bridge.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C22-R6L99-01 | 000810 | 삼성화재 | 2024-02-01 | 2024-02-01 | 289500 | 393500 | 265000 | 35.92% | -8.46% | Nonlife reserve quality + capital-return bridge worked; Green requires solvency-consistent return proof. |
| C22-R6L99-02 | 005830 | DB손해보험 | 2024-02-01 | 2024-02-01 | 91900 | 124000 | 86500 | 34.93% | -5.88% | Clean nonlife rate/reserve/capital-return positive path; good C22 candidate. |
| C22-R6L99-03 | 001450 | 현대해상 | 2024-02-01 | 2024-02-01 | 35450 | 36800 | 30250 | 3.81% | -14.67% | Same nonlife label but weak follow-through; reserve/capital-return bridge cannot be assumed. |
| C22-R6L99-04 | 032830 | 삼성생명 | 2024-02-01 | 2024-02-01 | 76000 | 108500 | 68900 | 42.76% | -9.34% | Life-insurance K-ICS/CSM/capital-surplus path worked, but CSM quality and payout policy must be verified. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C22-R6L99-01","round":"R6","loop":"99","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_LEADER_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE","symbol":"000810","name":"삼성화재","trigger_type":"nonlife_leader_reserve_quality_capital_return_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":289500,"peak_price":393500,"peak_date":"2024-06-28","trough_price":265000,"trough_date":"2024-02-01","mfe_pct":35.92,"mae_pct":-8.46,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_URLs","residual_flag":"positive_nonlife_reserve_quality_but_requires_KICS_and_payout_policy_bridge","dedupe_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|000810|nonlife_leader_reserve_quality_capital_return_bridge|2024-02-01"}
{"row_type":"trigger","case_id":"C22-R6L99-02","round":"R6","loop":"99","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_RATE_RESERVE_CAPITAL_RETURN_CLEAN_POSITIVE","symbol":"005830","name":"DB손해보험","trigger_type":"nonlife_rate_reserve_capital_return_clean_positive","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":91900,"peak_price":124000,"peak_date":"2024-08-22","trough_price":86500,"trough_date":"2024-04-12","mfe_pct":34.93,"mae_pct":-5.88,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_URLs","residual_flag":"best_nonlife_positive_if_loss_ratio_reserve_and_payout_bridge_verified","dedupe_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|005830|nonlife_rate_reserve_capital_return_clean_positive|2024-02-01"}
{"row_type":"trigger","case_id":"C22-R6L99-03","round":"R6","loop":"99","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_PEER_VALUEUP_LABEL_WEAK_RESERVE_CAPITAL_BRIDGE","symbol":"001450","name":"현대해상","trigger_type":"nonlife_peer_valueup_label_weak_reserve_capital_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":35450,"peak_price":36800,"peak_date":"2024-02-05","trough_price":30250,"trough_date":"2024-10-18","mfe_pct":3.81,"mae_pct":-14.67,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_or_local_4B_watch","residual_flag":"counterexample_same_nonlife_label_without_enough_reserve_capital_return_bridge","dedupe_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|001450|nonlife_peer_valueup_label_weak_reserve_capital_bridge|2024-02-01"}
{"row_type":"trigger","case_id":"C22-R6L99-04","round":"R6","loop":"99","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_CSM_KICS_CAPITAL_SURPLUS_BRIDGE","symbol":"032830","name":"삼성생명","trigger_type":"life_insurance_csm_kics_capital_surplus_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":76000,"peak_price":108500,"peak_date":"2024-03-08","trough_price":68900,"trough_date":"2024-02-01","mfe_pct":42.76,"mae_pct":-9.34,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_CSM_KICS_URLs","residual_flag":"life_positive_requires_CSM_quality_KICS_and_shareholder_return_bridge","dedupe_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|032830|life_insurance_csm_kics_capital_surplus_bridge|2024-02-01"}
```

## 6. Score-return alignment

### 6.1 Nonlife quality winner family

`000810` and `005830` show the C22 positive family. The first leg comes from value-up/rate-cycle recognition, but the durable leg requires loss ratio stability, reserve quality, and shareholder-return capacity. DB손해보험 had the cleaner MFE/MAE asymmetry in this sample, while 삼성화재 had strong MFE but needed explicit solvency/payout validation before Green.

### 6.2 Same label, weaker bridge

`001450` is the useful counterexample. It had the same nonlife insurance label, but MFE stayed small while MAE later dominated. That tells the model not to transfer the leader score to all insurers. C22 should not reward “insurance” as a blanket sector beta; it should reward reserve quality and capital-return bridge.

### 6.3 Life-insurance bridge

`032830` shows the life-insurance version of C22. The path can work very strongly when the market recognizes capital surplus, CSM/K-ICS buffer, and value-up potential. But the evidence burden differs from nonlife: CSM quality, K-ICS, liability duration, dividend policy, and unrealized gains matter more than simple motor/loss-ratio rate cycle.

## 7. Raw component score simulation

| symbol | rate/reserve evidence | K-ICS/CSM/capital buffer | shareholder return bridge | price confirmation | MAE guardrail | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---|
| 000810 | 22 | 20 | 18 | 21 | -4 | 77 | Stage3-Yellow/Green candidate |
| 005830 | 22 | 19 | 18 | 22 | -3 | 78 | Stage3-Yellow/Green candidate |
| 001450 | 15 | 9 | 7 | 3 | -8 | 26 | Stage2/local 4B watch |
| 032830 | 18 | 23 | 17 | 24 | -5 | 77 | Stage3-Yellow candidate |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c22_insurance_requires_reserve_quality_capital_bridge","scope":"C22_INSURANCE_RATE_CYCLE_RESERVE","candidate_action":"stage2_required_bridge","rule":"Do not promote insurance/value-up labels above Stage2 unless reserve adequacy, loss ratio quality, CSM/K-ICS buffer, or shareholder-return capacity is visible.","supporting_cases":["001450"],"counterbalanced_by":["000810","005830","032830"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c22_peer_transfer_guard","scope":"C22_INSURANCE_RATE_CYCLE_RESERVE","candidate_action":"canonical_boundary_guard","rule":"Do not transfer leader scores across all insurers; peer insurers need their own reserve/capital-return bridge and cannot rely on sector beta alone.","supporting_cases":["001450"],"counterbalanced_by":["000810","005830"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c22_nonlife_leader_positive_delta","scope":"C22_INSURANCE_RATE_CYCLE_RESERVE","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Nonlife leaders with loss-ratio stability, reserve quality, capital surplus, and verified payout policy can receive stronger Stage3-Yellow/Green candidate treatment.","supporting_cases":["000810","005830"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c22_life_csm_kics_bridge_positive_delta","scope":"C22_INSURANCE_RATE_CYCLE_RESERVE","candidate_action":"stage3_yellow_candidate_delta","rule":"Life insurers with CSM quality, K-ICS buffer, and explicit shareholder-return bridge can receive Stage3-Yellow treatment, but Green requires liability/reserve-quality confirmation.","supporting_cases":["032830"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","round":"R6","loop":"99","positive_rows":3,"counterexample_rows":1,"new_symbol_count":4,"primary_residual":"C22 should separate sector-wide insurance/value-up beta from company-specific reserve quality, K-ICS/CSM buffer, and shareholder-return execution.","candidate_patch_axes":["stage2_required_bridge","canonical_boundary_guard","stage3_yellow_to_green_candidate_delta","stage3_yellow_candidate_delta"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","sample_count":4,"avg_mfe_pct":29.36,"avg_mae_pct":-9.59,"median_mfe_pct":35.43,"median_mae_pct":-8.90,"interpretation":"C22 can produce strong upside when reserve/capital-return bridge is real, but peer-transfer from insurance label alone creates false Stage2 risk."}
```

## 10. Validation flags

```text
usable_for_ledger: true
usable_for_production_patch: false
reason_not_promotion_ready:
  - source_proxy_only=true
  - evidence_url_pending=true
  - non-price exact URLs must be verified before applying weight deltas
  - local 2024 OHLC rows were checked from stock-web tradable shards
  - historical corporate-action profile caveats are outside the local 2024 trigger windows used here
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C22 R6 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c22_insurance_requires_reserve_quality_capital_bridge -> stage2_required_bridge
  2. c22_peer_transfer_guard -> canonical_boundary_guard
  3. c22_nonlife_leader_positive_delta -> stage3_yellow_to_green_candidate_delta
  4. c22_life_csm_kics_bridge_positive_delta -> stage3_yellow_candidate_delta

Expected behavior:
- Insurance/value-up vocabulary alone should not create Green.
- Reserve adequacy, loss ratio quality, K-ICS/CSM buffer, and shareholder-return capacity can justify Stage3-Yellow.
- Nonlife leader scores should not be transferred mechanically to weaker peers.
- Life insurers need separate CSM/K-ICS/liability-duration proof before promotion.
```
