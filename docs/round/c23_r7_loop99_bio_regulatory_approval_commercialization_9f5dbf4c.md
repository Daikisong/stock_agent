# E2R Stock-Web v12 Residual Research — R7 loop 99 / L7 / C23

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 99
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: FDA_APPROVAL_COMMERCIAL_LAUNCH_REIMBURSEMENT_REVENUE_MARGIN_BRIDGE_VS_APPROVAL_LABEL_AND_VACCINE_COMMERCIALIZATION_FALSE_STAGE2
loop_contribution_label: canonical_archetype_rule_candidate
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - regulatory_approval_to_commercial_revenue_bridge_test
  - launch_reimbursement_channel_guardrail
  - biosimilar_maturity_low_MFE_guardrail
  - vaccine_approval_commercialization_false_stage2_guard
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
source_proxy_only: true
evidence_url_pending: true
```

## 1. Scope

이번 파일은 `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` 전용 residual research다.

C23은 “FDA 승인”, “허가”, “품목허가”, “상업화”, “보험 등재”, “출시 예정”이라는 label만으로 Stage3-Green을 주는 bucket이 아니다. 핵심은 규제 승인 이벤트가 실제 launch timing, channel access, reimbursement, prescription/adoption, manufacturing supply, revenue, royalty, gross margin, FCF, EPS revision으로 내려오는지다.

```text
regulatory approval / commercialization headline
  → launch timing / channel access / reimbursement
  → prescription, adoption, shipment, royalty or product revenue
  → gross margin / FCF / EPS revision bridge
  → stock-web 1D OHLC forward path
```

승인은 병원 문 앞에서 받은 출입증과 같다. 출입증이 있어도 처방이 나가고, 보험 코드가 붙고, 유통 채널이 열리고, 매출채권이 현금으로 돌아와야 상업화가 완성된다. C23은 “허가를 받았다”와 “돈이 되기 시작했다”를 분리한다.

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","price_atlas_repo":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","manifest_max_date":"2026-02-20","notes":"Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol_set":["145020","000100","068270","195940","302440"],"profile_paths":["atlas/symbol_profiles/145/145020.json","atlas/symbol_profiles/000/000100.json","atlas/symbol_profiles/068/068270.json","atlas/symbol_profiles/195/195940.json","atlas/symbol_profiles/302/302440.json"],"year_shards":["atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv","atlas/ohlcv_tradable_by_symbol_year/068/068270/2024.csv","atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv","atlas/ohlcv_tradable_by_symbol_year/302/302440/2024.csv"],"validation_scope":"2024 trigger-level forward path; 145020 caveats are 2017/2020, 000100 caveat ends 2020, 068270 has a 2024-01-12 caveat so selected post-January rows are used, 195940 and 302440 have zero corporate-action candidates. Selected 2024 local windows avoid active corporate-action contamination."}
```

## 3. Novelty / no-repeat check

- No-Repeat Index Priority 0 lists C23 at 29 rows, 1 row short of the 30-row minimum stability zone.
- Existing registry shows C23 parsed through `R7 loop 98`.
- This output uses `R7 loop 99`.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- Prior C23 loop 98 emphasized biosimilar / botox / vaccine commercialization. This file compresses FDA botulinum-toxin launch bridge, domestic oncology approval commercialization, biosimilar mature commercialization low-MFE guard, P-CAB export/US commercialization bridge, and vaccine approval/commercialization false Stage2.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_price | trough_price | MFE | MAE | interpretation |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| C23-R7L99-01 | 145020 | 휴젤 | 2024-03-04 | 2024-03-04 | 202500 | 301000 | 172300 | 48.64% | -14.91% | Botulinum-toxin approval/global launch path worked, but launch reimbursement and margin bridge are needed. |
| C23-R7L99-02 | 000100 | 유한양행 | 2024-08-21 | 2024-08-21 | 94300 | 166900 | 93800 | 76.99% | -0.53% | Oncology approval/commercialization path worked strongly with controlled entry MAE. |
| C23-R7L99-03 | 068270 | 셀트리온 | 2024-02-27 | 2024-02-27 | 190100 | 211000 | 173000 | 10.99% | -9.00% | Mature biosimilar commercialization was steady but not a clean Green without revision bridge. |
| C23-R7L99-04 | 195940 | HK이노엔 | 2024-08-28 | 2024-08-28 | 44100 | 52000 | 40800 | 17.91% | -7.48% | P-CAB/global commercialization bridge was constructive but still needs reimbursement/channel proof. |
| C23-R7L99-05 | 302440 | SK바이오사이언스 | 2024-01-02 | 2024-01-02 | 73300 | 73700 | 48600 | 0.55% | -33.70% | Vaccine approval/commercialization label failed without repeat demand and revenue bridge. |

## 5. Usable trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C23-R7L99-01","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_FDA_APPROVAL_GLOBAL_LAUNCH_REIMBURSEMENT_MARGIN_BRIDGE","symbol":"145020","name":"휴젤","trigger_type":"botulinum_toxin_fda_approval_global_launch_reimbursement_margin_bridge","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":202500,"peak_price":301000,"peak_date":"2024-10-17","trough_price":172300,"trough_date":"2024-03-21","mfe_pct":48.64,"mae_pct":-14.91,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_candidate_pending_launch_reimbursement_margin_URLs","residual_flag":"approval_launch_positive_but_requires_channel_reimbursement_revenue_OPM_bridge","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|145020|botulinum_toxin_fda_approval_global_launch_reimbursement_margin_bridge|2024-03-04"}
{"row_type":"trigger","case_id":"C23-R7L99-02","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"ONCOLOGY_APPROVAL_COMMERCIALIZATION_REVENUE_ROYALTY_BRIDGE","symbol":"000100","name":"유한양행","trigger_type":"oncology_approval_commercialization_revenue_royalty_bridge","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":94300,"peak_price":166900,"peak_date":"2024-10-15","trough_price":93800,"trough_date":"2024-08-21","mfe_pct":76.99,"mae_pct":-0.53,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage3-Yellow_to_Green_candidate_pending_revenue_royalty_URLs","residual_flag":"oncology_approval_commercialization_path_strong_but_revenue_royalty_FCF_URLs_required","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|000100|oncology_approval_commercialization_revenue_royalty_bridge|2024-08-21"}
{"row_type":"trigger","case_id":"C23-R7L99-03","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"MATURE_BIOSIMILAR_COMMERCIALIZATION_LOW_RERATING_WITH_REVISION_GUARD","symbol":"068270","name":"셀트리온","trigger_type":"mature_biosimilar_commercialization_low_rerating_with_revision_guard","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":190100,"peak_price":211000,"peak_date":"2024-07-30","trough_price":173000,"trough_date":"2024-08-05","mfe_pct":10.99,"mae_pct":-9.00,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Yellow_with_revision_guard","residual_flag":"biosimilar_commercialization_stable_but_low_rerating_without_fresh_revenue_margin_revision_bridge","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|068270|mature_biosimilar_commercialization_low_rerating_with_revision_guard|2024-02-27"}
{"row_type":"trigger","case_id":"C23-R7L99-04","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"P_CAB_GLOBAL_COMMERCIALIZATION_REIMBURSEMENT_CHANNEL_BRIDGE","symbol":"195940","name":"HK이노엔","trigger_type":"p_cab_global_commercialization_reimbursement_channel_bridge","trigger_date":"2024-08-28","entry_date":"2024-08-28","entry_price":44100,"peak_price":52000,"peak_date":"2024-10-07","trough_price":40800,"trough_date":"2024-08-28","mfe_pct":17.91,"mae_pct":-7.48,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Stage2_to_Stage3-Yellow_with_channel_reimbursement_guard","residual_flag":"P_CAB_commercialization_constructive_but_channel_reimbursement_OPM_bridge_required","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|195940|p_cab_global_commercialization_reimbursement_channel_bridge|2024-08-28"}
{"row_type":"trigger","case_id":"C23-R7L99-05","round":"R7","loop":"99","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"VACCINE_APPROVAL_COMMERCIALIZATION_FALSE_STAGE2_REPEAT_DEMAND_DECAY","symbol":"302440","name":"SK바이오사이언스","trigger_type":"vaccine_approval_commercialization_false_stage2_repeat_demand_decay","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":73300,"peak_price":73700,"peak_date":"2024-01-02","trough_price":48600,"trough_date":"2024-08-05","mfe_pct":0.55,"mae_pct":-33.70,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","source_proxy_only":true,"evidence_url_pending":true,"current_profile_expected_stage":"Hard_counterexample_or_local_4B_watch","residual_flag":"vaccine_approval_commercialization_label_failed_without_repeat_demand_revenue_margin_bridge","dedupe_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|302440|vaccine_approval_commercialization_false_stage2_repeat_demand_decay|2024-01-02"}
```

## 6. Score-return alignment

### 6.1 Approval can work when commercialization is credible

`145020` and `000100` are the constructive C23 family. The price paths show that regulatory approval can create large MFE when the market sees launch, channel access, adoption, reimbursement, royalty or commercial revenue bridge. These rows can become Stage3-Yellow/Green candidates only after exact commercialization evidence is URL-verified.

### 6.2 Mature commercialization does not always rerate

`068270` is the steady but lower-rerating case. Mature biosimilar commercialization is not a bad row, but the forward MFE was not large enough to inherit the score of a fresh approval-to-revenue bridge. The scorer should require fresh revenue, market-share, margin, and revision evidence.

### 6.3 Approval vocabulary can be a false Stage2

`302440` is the hard warning row. Vaccine approval/commercialization vocabulary did not repair the forward path because repeat demand and commercial revenue were weak. C23 therefore needs a post-approval commercial traction guard.

### 6.4 Channel-specific commercialization

`195940` is the middle family. P-CAB/global commercialization can work, but the evidence has to move through country launch, reimbursement, channel prescription, and margin. It is a Stage2→Yellow bridge, not automatic Green.

## 7. Raw component score simulation

| symbol | approval/regulatory evidence | launch/channel/reimbursement | revenue/royalty bridge | margin/FCF bridge | price confirmation | MAE/commercial guard | shadow score | shadow stage |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 145020 | 23 | 17 | 14 | 11 | 18 | -7 | 76 | Stage3-Yellow candidate |
| 000100 | 24 | 20 | 18 | 14 | 24 | -1 | 99 | Stage3-Yellow/Green candidate |
| 068270 | 19 | 12 | 10 | 8 | 8 | -5 | 52 | Stage2→Yellow with revision guard |
| 195940 | 19 | 13 | 11 | 8 | 11 | -4 | 58 | Stage2→Yellow with channel guard |
| 302440 | 14 | 4 | 3 | 2 | 0 | -15 | 8 | Hard counterexample/local 4B |

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"c23_approval_requires_launch_reimbursement_revenue_margin_bridge","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"stage2_required_bridge","rule":"Do not promote regulatory approval/commercialization labels above Stage2 unless launch timing, channel access, reimbursement, prescription/adoption, shipment, royalty/product revenue, gross margin, FCF, or EPS revision bridge is visible.","supporting_cases":["302440","068270"],"counterbalanced_by":["145020","000100","195940"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c23_fresh_approval_commercialization_positive_delta","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"stage3_yellow_to_green_candidate_delta","rule":"Fresh approval rows with credible launch, reimbursement, revenue or royalty and margin bridge can receive stronger Stage3-Yellow/Green candidate treatment after URL verification.","supporting_cases":["145020","000100"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c23_mature_biosimilar_low_rerating_guard","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"stage2_to_yellow_with_revision_guard","rule":"Mature biosimilar commercialization rows should be capped when MFE is modest and no fresh market-share, revenue or margin revision evidence appears.","supporting_cases":["068270"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c23_vaccine_commercialization_false_stage2_guard","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"local_4b_or_hard_counterexample","rule":"Vaccine approval/commercialization labels with tiny MFE and large MAE should remain local 4B or hard counterexample unless repeat demand and revenue bridge repairs the thesis.","supporting_cases":["302440"],"production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"c23_channel_commercialization_yellow_guard","scope":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","candidate_action":"stage2_to_yellow_with_channel_reimbursement_guard","rule":"Channel-specific commercialization rows can become Yellow when country launch, reimbursement, prescription and OPM evidence is visible; Green requires stronger commercial traction.","supporting_cases":["195940"],"production_scoring_changed":false}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","round":"R7","loop":"99","positive_rows":2,"counterexample_rows":3,"new_symbol_count":5,"primary_residual":"C23 should separate fresh approval-to-commercial revenue winners from mature biosimilar low-rerating, channel-specific commercialization bridges, and vaccine commercialization labels that fail without repeat demand and margin evidence.","candidate_patch_axes":["stage2_required_bridge","stage3_yellow_to_green_candidate_delta","stage2_to_yellow_with_revision_guard","local_4b_or_hard_counterexample","stage2_to_yellow_with_channel_reimbursement_guard"],"promotion_readiness":"not_ready","blocker":"source_proxy_only; exact non-price evidence URLs pending"}
{"row_type":"aggregate_metric","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","sample_count":5,"avg_mfe_pct":31.02,"avg_mae_pct":-13.12,"median_mfe_pct":17.91,"median_mae_pct":-9.00,"interpretation":"C23 approval vocabulary can create strong upside when launch and revenue bridge are credible, but mature commercialization and vaccine labels require strict traction, reimbursement, repeat-demand and margin guardrails."}
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
  - selected local windows avoid active corporate-action contamination
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this handoff during the research session.

Goal:
- Ingest this C23 R7 loop 99 residual research file into the v12 calibration corpus.
- Validate JSONL trigger rows.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Keep production scoring unchanged unless exact non-price evidence URLs are later verified.

Candidate axes to test after URL verification:
  1. c23_approval_requires_launch_reimbursement_revenue_margin_bridge -> stage2_required_bridge
  2. c23_fresh_approval_commercialization_positive_delta -> stage3_yellow_to_green_candidate_delta
  3. c23_mature_biosimilar_low_rerating_guard -> stage2_to_yellow_with_revision_guard
  4. c23_vaccine_commercialization_false_stage2_guard -> local_4b_or_hard_counterexample
  5. c23_channel_commercialization_yellow_guard -> stage2_to_yellow_with_channel_reimbursement_guard

Expected behavior:
- Regulatory approval/commercialization vocabulary alone should not create Green.
- Launch timing, channel access, reimbursement, prescription/adoption, shipment, royalty/product revenue, gross margin, FCF or EPS revision can justify Stage3-Yellow/Green.
- Mature biosimilar and vaccine commercialization labels should remain capped unless commercial traction and margin evidence repairs the row.
```
